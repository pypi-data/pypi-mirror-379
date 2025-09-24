# llm_apm/core/monitor.py
import uuid
import logging
import time
from datetime import datetime, timezone
from typing import Optional, Dict, Any
from .timer import StepTimer
from .metrics import MetricsCollector, RequestMetrics
from ..config.settings import config
from ..storage.base import BaseStorage
from ..exporters.prometheus import PrometheusExporter
import random
import asyncio
from concurrent.futures import ThreadPoolExecutor

# import decorator helper to read ContextVar metrics
from .decorators import get_current_step_metrics, clear_step_context

logger = logging.getLogger(__name__)

_BG_EXECUTOR = ThreadPoolExecutor(max_workers=4)

class LLMMonitor:
    def __init__(self, storage: Optional[BaseStorage] = None, exporter: Optional[PrometheusExporter] = None, sampling_rate: float = None):
        self.storage = storage
        self.exporter = exporter
        self.sampling_rate = sampling_rate or getattr(config, "sampling_rate", 1.0)
        self.metrics_collector = MetricsCollector()
        try:
            if self.exporter and getattr(self.exporter, "start_http_server_flag", False):
                self.exporter.start()
        except Exception as e:
            logger.warning(f"Could not start exporter server: {e}")
        logger.info(f"LLM Monitor initialized with sampling rate: {self.sampling_rate}")

    def should_sample(self, user_id: Optional[str] = None, endpoint: Optional[str] = None) -> bool:
        try:
            from ..utils.sampler import should_sample as deterministic_should_sample
            try:
                samp = config.get_endpoint_sampling(endpoint)
            except Exception:
                samp = getattr(config, "sampling_rate", 1.0)
            return deterministic_should_sample(user_id, samp)
        except Exception:
            return random.random() < getattr(config, "sampling_rate", 1.0)

    def start_request_monitoring(self, endpoint: str, model: str, prompt: str = "", user_id: Optional[str] = None, session_id: Optional[str] = None, request_id: Optional[str] = None) -> 'RequestMonitor':
        if not self.should_sample(user_id=user_id, endpoint=endpoint):
            logger.debug("Request not sampled, skipping monitoring")
            return RequestMonitor(None, None, sample=False)
        request_id = request_id or str(uuid.uuid4())
        metrics = self.metrics_collector.create_request_metrics(
            request_id=request_id,
            model=model,
            endpoint=endpoint,
            prompt=prompt,
            user_id=user_id,
            session_id=session_id
        )
        return RequestMonitor(self, metrics)

    def record_request(self, metrics: RequestMetrics):
        try:
            metrics.timestamp = datetime.now(timezone.utc)
            self.metrics_collector.add_metrics(metrics)
            total_export_seconds = 0.0
            if self.exporter:
                try:
                    exporter_duration = self.exporter.record_request(metrics)
                    if isinstance(exporter_duration, (int, float)):
                        total_export_seconds += float(exporter_duration)
                except Exception as e:
                    logger.error(f"Exporter.record_request failed: {e}", exc_info=True)
            if self.storage:
                try:
                    start_s = time.perf_counter()
                    self.storage.store_metrics(metrics)
                    end_s = time.perf_counter()
                    storage_seconds = end_s - start_s
                    total_export_seconds += storage_seconds
                except Exception as e:
                    logger.error(f"Storage.store_metrics failed: {e}", exc_info=True)
            try:
                metrics.metrics_export_ms = total_export_seconds * 1000.0
            except Exception:
                metrics.metrics_export_ms = 0.0
            try:
                if self.exporter and getattr(self.exporter, "metrics_export_duration", None) is not None:
                    labels = {'model': metrics.model, 'endpoint': metrics.endpoint}
                    try:
                        self.exporter.metrics_export_duration.labels(**labels).observe(metrics.metrics_export_ms / 1000.0)
                    except Exception:
                        pass
            except Exception:
                pass
            logger.debug(f"Recorded metrics for request {metrics.request_id} (export_ms={metrics.metrics_export_ms:.2f})")
        except Exception as e:
            logger.error(f"Failed to record request metrics: {e}", exc_info=True)

    def get_metrics_summary(self, time_window_minutes: int = 60) -> Dict[str, Any]:
        return self.metrics_collector.get_aggregated_metrics(time_window_minutes)

    def get_model_stats(self) -> Dict[str, Any]:
        return self.metrics_collector.get_model_stats()

    def shutdown(self):
        try:
            if self.exporter:
                try:
                    self.exporter.shutdown()
                except Exception as e:
                    logger.error(f"Error shutting down exporter: {e}")
            if self.storage:
                try:
                    self.storage.close()
                except Exception as e:
                    logger.error(f"Error closing storage: {e}")
            try:
                _BG_EXECUTOR.shutdown(wait=False)
            except Exception:
                pass
            logger.info("LLM Monitor shutdown completed")
        except Exception as e:
            logger.error(f"Error during monitor shutdown: {e}", exc_info=True)


class RequestMonitor:
    def __init__(self, monitor: Optional[LLMMonitor], metrics: Optional[RequestMetrics], sample: bool = True):
        self.monitor = monitor
        self.metrics = metrics
        self.step_timer = StepTimer() if sample else None
        self.sample = sample
        self._error_occurred = False

    def __enter__(self):
        if self.sample and self.step_timer:
            self.step_timer.start_overall()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.sample:
            return
        try:
            # stop overall timer and build step map from StepTimer
            if self.step_timer and self.metrics:
                try:
                    self.step_timer.stop_overall()
                except Exception:
                    pass
            steps = self.step_timer.get_all_steps() if self.step_timer else {}

            # --- NEW: merge decorator-based ContextVar timings ---
            try:
                decorator_metrics = get_current_step_metrics()  # returns {'preprocessing_ms': val, ...}
                if isinstance(decorator_metrics, dict):
                    for k, v in decorator_metrics.items():
                        # normalize key name
                        k_norm = k
                        if k_norm.endswith("_ms"):
                            k_norm = k_norm[:-3]
                        try:
                            v_float = float(v)
                        except Exception:
                            continue
                        # prefer StepTimer values (already in steps). Only fill missing/zero.
                        if steps.get(k_norm) is None or steps.get(k_norm) == 0.0:
                            steps[k_norm] = v_float
            except Exception:
                logger.debug("Failed to merge decorator metrics", exc_info=True)
            finally:
                # clear the decorator ContextVar for this request (prevent leak)
                try:
                    clear_step_context()
                except Exception:
                    pass

            # Merge any externally attached step durations stored on metrics.steps (fallback)
            try:
                metrics_steps = getattr(self.metrics, "steps", None)
                if isinstance(metrics_steps, dict):
                    for key, val in metrics_steps.items():
                        k_norm = key
                        if k_norm.endswith("_ms"):
                            k_norm = k_norm[:-3]
                        if val is None:
                            continue
                        try:
                            v_float = float(val)
                        except Exception:
                            continue
                        if steps.get(k_norm) is None or steps.get(k_norm) == 0.0:
                            steps[k_norm] = v_float
            except Exception:
                logger.debug("Failed merging metrics.steps into step timer results", exc_info=True)

            # fallback from direct attrs
            try:
                for fallback_name in ("preprocessing", "llm_api_call", "postprocessing", "metrics_export"):
                    attr_name = f"{fallback_name}_ms"
                    if steps.get(fallback_name) is None or steps.get(fallback_name) == 0.0:
                        val = getattr(self.metrics, attr_name, None)
                        if val is not None:
                            try:
                                steps[fallback_name] = float(val)
                            except Exception:
                                pass
            except Exception:
                logger.debug("Failed merging direct metric attributes into steps", exc_info=True)

            # Extract final step durations
            preprocessing_ms = steps.get("preprocessing", 0.0)
            llm_api_call_ms = steps.get("llm_api_call", 0.0)
            postprocessing_ms = steps.get("postprocessing", 0.0)
            metrics_export_ms = steps.get("metrics_export", self.metrics.metrics_export_ms or 0.0)

            # assign to metrics
            self.metrics.preprocessing_ms = preprocessing_ms
            self.metrics.llm_api_call_ms = llm_api_call_ms
            self.metrics.postprocessing_ms = postprocessing_ms
            self.metrics.metrics_export_ms = metrics_export_ms

            # Compute totals
            measured_sum = (
                (preprocessing_ms or 0.0) +
                (llm_api_call_ms or 0.0) +
                (postprocessing_ms or 0.0) +
                (metrics_export_ms or 0.0)
            )
            self.metrics.total_latency_ms = measured_sum
            self.metrics.unaccounted_ms = 0.0

            # Error bookkeeping
            if exc_type is not None or self._error_occurred:
                self.metrics.error = True
                self.metrics.error_message = str(exc_val) if exc_val else "Unknown error"
                self.metrics.error_type = exc_type.__name__ if exc_type else "UnknownError"
                self.metrics.status_code = getattr(self.metrics, "status_code", 500)
            self.metrics.timestamp = datetime.now(timezone.utc)

            # schedule background record_request
            if self.monitor:
                try:
                    loop = None
                    try:
                        loop = asyncio.get_running_loop()
                    except RuntimeError:
                        loop = None
                    if loop:
                        loop.run_in_executor(None, self.monitor.record_request, self.metrics)
                    else:
                        def _bg_call(monitor_obj, metrics_obj):
                            try:
                                monitor_obj.record_request(metrics_obj)
                            except Exception as e:
                                logger.error("Background record_request failed", exc_info=True)
                        _BG_EXECUTOR.submit(_bg_call, self.monitor, self.metrics)
                except Exception as e:
                    logger.error(f"Failed to schedule background record_request: {e}", exc_info=True)

        except Exception as e:
            logger.error(f"Error in RequestMonitor cleanup: {e}", exc_info=True)

    # other methods (start_step, stop_current_step, update_tokens, etc.) remain unchanged...
    def start_step(self, step_name: str):
        if self.sample and self.step_timer:
            self.step_timer.start_step(step_name)

    def stop_current_step(self):
        if self.sample and self.step_timer:
            return self.step_timer.stop_current_step()
        return None

    def update_tokens(self, input_tokens: int = None, output_tokens: int = None):
        if not self.sample or not self.metrics:
            return
        if input_tokens is not None:
            self.metrics.input_tokens = input_tokens
        if output_tokens is not None:
            self.metrics.output_tokens = output_tokens
        self.metrics.total_tokens = self.metrics.input_tokens + self.metrics.output_tokens
        try:
            from ..utils.cost_calculator import cost_calculator
            self.metrics.estimated_cost_usd = cost_calculator.calculate_cost(
                self.metrics.model,
                self.metrics.input_tokens,
                self.metrics.output_tokens
            )
        except Exception:
            pass

    def update_response(self, response: str, status_code: int = 200):
        if not self.sample or not self.metrics:
            return
        self.metrics.response_size_bytes = len(response.encode('utf-8'))
        self.metrics.status_code = status_code
        try:
            from ..utils.token_counter import token_counter
            output_tokens = token_counter.count_tokens(response, self.metrics.model)
            self.update_tokens(output_tokens=output_tokens)
        except Exception:
            pass

    def record_error(self, error: Exception, status_code: int = 500):
        if not self.sample or not self.metrics:
            return
        self._error_occurred = True
        self.metrics.error = True
        self.metrics.error_message = str(error)
        self.metrics.error_type = type(error).__name__
        self.metrics.status_code = status_code
        logger.error(f"Request {self.metrics.request_id} failed: {error}")

    def get_current_metrics(self) -> Dict[str, Any]:
        if not self.sample or not self.metrics:
            return {"error": True, "message": "Not sampled"}
        steps = self.step_timer.get_all_steps() if self.step_timer else {}
        try:
            decorator_metrics = get_current_step_metrics()
            if isinstance(decorator_metrics, dict):
                for k, v in decorator_metrics.items():
                    k_norm = k
                    if k_norm.endswith("_ms"):
                        k_norm = k_norm[:-3]
                    try:
                        v_float = float(v)
                    except Exception:
                        continue
                    if steps.get(k_norm) is None or steps.get(k_norm) == 0.0:
                        steps[k_norm] = v_float
        except Exception:
            logger.debug("Failed merging decorator metrics into get_current_metrics", exc_info=True)

        try:
            metrics_steps = getattr(self.metrics, "steps", None)
            if isinstance(metrics_steps, dict):
                for key, val in metrics_steps.items():
                    k_norm = key
                    if k_norm.endswith("_ms"):
                        k_norm = k_norm[:-3]
                    if val is None:
                        continue
                    try:
                        v_float = float(val)
                    except Exception:
                        continue
                    if steps.get(k_norm) is None or steps.get(k_norm) == 0.0:
                        steps[k_norm] = v_float
        except Exception:
            pass

        try:
            for fallback_name in ("preprocessing", "llm_api_call", "postprocessing", "metrics_export"):
                if steps.get(fallback_name) is None:
                    attr_val = getattr(self.metrics, f"{fallback_name}_ms", None)
                    if attr_val is not None:
                        try:
                            steps[fallback_name] = float(attr_val)
                        except Exception:
                            pass
        except Exception:
            pass

        measured_sum = (
            steps.get("preprocessing", 0.0) +
            steps.get("llm_api_call", 0.0) +
            steps.get("postprocessing", 0.0) +
            steps.get("metrics_export", 0.0)
        )
        return {
            "request_id": self.metrics.request_id,
            "total_latency_ms": measured_sum,
            "steps": {
                "preprocessing_ms": steps.get("preprocessing", 0.0),
                "llm_api_call_ms": steps.get("llm_api_call", 0.0),
                "postprocessing_ms": steps.get("postprocessing", 0.0),
                "metrics_export_ms": steps.get("metrics_export", 0.0)
            },
            "tokens_used": self.metrics.total_tokens,
            "estimated_cost_usd": self.metrics.estimated_cost_usd,
            "error": self.metrics.error
        }
# ---------------------------------------------------------------------
# Global monitor instance helpers (used by middleware and app startup)
# ---------------------------------------------------------------------
global_monitor: Optional[LLMMonitor] = None

def get_global_monitor() -> Optional[LLMMonitor]:
    """Return the global LLMMonitor instance (or None)."""
    return global_monitor

def set_global_monitor(monitor: LLMMonitor):
    """Set the global LLMMonitor instance (used by middleware on startup)."""
    global global_monitor
    global_monitor = monitor
