# llm_apm/core/metrics.py
"""
Metrics collection and calculation for LLM monitoring
Includes helpers to compute derived KPIs such as percentiles, token stats,
cost projections and error rates for configurable time windows.
"""
import time
from datetime import datetime, timezone, timedelta
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass, asdict
from ..utils.token_counter import token_counter
from ..utils.cost_calculator import cost_calculator
import logging
import math

logger = logging.getLogger(__name__)

@dataclass
class RequestMetrics:
    """Data class for storing request metrics"""
    # Required identifiers
    request_id: str
    timestamp: datetime
    # Latency metrics (defaults provided to avoid dataclass ordering issues)
    total_latency_ms: float = 0.0
    preprocessing_ms: float = 0.0
    llm_api_call_ms: float = 0.0
    postprocessing_ms: float = 0.0
    metrics_export_ms: float = 0.0
    # Unaccounted time (the difference between total and sum(steps))
    unaccounted_ms: float = 0.0
    # Token metrics
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0
    # Cost metrics
    estimated_cost_usd: float = 0.0
    # Denotes where the cost value came from: "computed" or "cache" or "none"
    estimated_cost_source: str = "computed"
    # Request details
    model: str = "unknown"
    endpoint: str = "unknown"
    user_id: Optional[str] = None
    user_hash: Optional[str] = None
    session_id: Optional[str] = None
    # Experiment / optimization metadata
    experiment: Optional[str] = None
    prompt_truncated: Optional[bool] = False
    # Error tracking
    error: bool = False
    error_message: Optional[str] = None
    error_type: Optional[str] = None
    # HTTP details
    status_code: int = 200
    request_size_bytes: int = 0
    response_size_bytes: int = 0
    # Cache + extra context
    cache_hit: bool = False
    from_cache: bool = False  # new explicit flag: metrics built from cached response
    cache_lookup_ms: float = 0.0
    error_context: Optional[str] = None
    # Response quality (0..1 or custom)
    response_quality: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        if isinstance(data.get('timestamp'), datetime):
            data['timestamp'] = data['timestamp'].isoformat()
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'RequestMetrics':
        if isinstance(data.get('timestamp'), str):
            data['timestamp'] = datetime.fromisoformat(data['timestamp'])
        return cls(**data)


class MetricsCollector:
    """Collects and aggregates metrics for LLM requests and produces derived KPIs"""
    def __init__(self):
        self.metrics_history: List[RequestMetrics] = []
        self.current_metrics: Dict[str, Any] = {}

    def create_request_metrics(
        self,
        request_id: str,
        model: str,
        endpoint: str,
        prompt: str = "",
        response: str = "",
        max_tokens: Optional[int] = None,
        user_id: Optional[str] = None,
        user_hash: Optional[str] = None,
        session_id: Optional[str] = None,
        experiment: Optional[str] = None,
        prompt_truncated: Optional[bool] = False,
        from_cache: bool = False,
        cached_usage: Optional[Dict[str, int]] = None,
        cached_cost_usd: Optional[float] = None
    ) -> RequestMetrics:
        """
        Create initial request metrics object.

        If from_cache=True and cached_usage is provided, **do not** call token_counter or cost_calculator.
        cached_usage should be a dict like: {"prompt_tokens": int, "completion_tokens": int, "total_tokens": int}
        cached_cost_usd may be provided if you *want* to attach a cached cost, but by default we leave cost_source as 'cache'
        and (per your requirement) avoid computing cost on cache hits.
        """
        # Initialize tokens and cost conservatively
        input_tokens = 0
        output_tokens = 0
        total_tokens = 0
        estimated_cost = 0.0
        cost_source = "none"

        if from_cache and cached_usage:
            # Use cached usage values but DO NOT recalculate via token_counter or cost_calculator
            input_tokens = int(cached_usage.get("prompt_tokens", 0))
            output_tokens = int(cached_usage.get("completion_tokens", 0))
            total_tokens = int(cached_usage.get("total_tokens", input_tokens + output_tokens))
            if cached_cost_usd is not None:
                try:
                    estimated_cost = float(cached_cost_usd)
                    cost_source = "cache"
                except Exception:
                    estimated_cost = 0.0
                    cost_source = "cache"
            else:
                # per your requirement: do not compute cost on cache hits
                estimated_cost = 0.0
                cost_source = "cache"
        else:
            # Real request path: compute token counts & cost
            try:
                input_tokens = int(token_counter.count_tokens(prompt, model))
            except Exception:
                input_tokens = 0
            try:
                output_tokens = int(token_counter.count_tokens(response, model)) if response else 0
            except Exception:
                output_tokens = 0
            total_tokens = input_tokens + output_tokens
            try:
                estimated_cost = float(cost_calculator.calculate_cost(model, input_tokens, output_tokens))
                cost_source = "computed"
            except Exception:
                estimated_cost = 0.0
                cost_source = "computed"

        now = datetime.now(timezone.utc)
        return RequestMetrics(
            request_id=request_id,
            timestamp=now,
            total_latency_ms=0.0,
            preprocessing_ms=0.0,
            llm_api_call_ms=0.0,
            postprocessing_ms=0.0,
            metrics_export_ms=0.0,
            unaccounted_ms=0.0,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=total_tokens,
            estimated_cost_usd=estimated_cost,
            estimated_cost_source=cost_source,
            model=model,
            endpoint=endpoint,
            user_id=user_id,
            user_hash=user_hash,
            session_id=session_id,
            experiment=experiment,
            prompt_truncated=prompt_truncated,
            request_size_bytes=len(prompt.encode('utf-8')) if prompt else 0,
            response_size_bytes=len(response.encode('utf-8')) if response else 0,
            cache_hit=False,
            from_cache=bool(from_cache),
            cache_lookup_ms=0.0
        )

    def update_metrics(self, metrics: RequestMetrics, force_recalc: bool = False, **updates):
        """
        Update metrics with new values.

        - If metrics.from_cache is True and force_recalc is False, we will NOT call cost_calculator or token_counter.
          This preserves your requirement to avoid recalculating tokens/costs for cache hits.
        - If force_recalc=True, we will recompute cost from tokens (use carefully).
        """
        tokens_changed = False
        for key, value in updates.items():
            if hasattr(metrics, key):
                setattr(metrics, key, value)
                if key in ("input_tokens", "output_tokens"):
                    tokens_changed = True

        # Recalculate total tokens
        try:
            metrics.total_tokens = int(metrics.input_tokens or 0) + int(metrics.output_tokens or 0)
        except Exception:
            metrics.total_tokens = (metrics.input_tokens or 0) + (metrics.output_tokens or 0)

        # Recalculate cost only when:
        # - request is not from cache, or
        # - force_recalc=True (caller explicitly requests)
        if (not metrics.from_cache) or force_recalc:
            if tokens_changed or ('input_tokens' in updates or 'output_tokens' in updates):
                try:
                    metrics.estimated_cost_usd = float(cost_calculator.calculate_cost(
                        metrics.model,
                        int(metrics.input_tokens or 0),
                        int(metrics.output_tokens or 0)
                    ))
                    metrics.estimated_cost_source = "computed"
                except Exception:
                    # keep previous cost if calculation fails
                    logger.debug("Cost calculation failed during update_metrics", exc_info=True)
        else:
            # keep cost as-is and mark source as cache if appropriate
            if metrics.from_cache:
                metrics.estimated_cost_source = metrics.estimated_cost_source or "cache"

    def add_metrics(self, metrics: RequestMetrics):
        """Add completed metrics to history (in-memory)"""
        self.metrics_history.append(metrics)
        # Keep only last 10000 requests in memory (trim older)
        if len(self.metrics_history) > 10000:
            self.metrics_history = self.metrics_history[-5000:]

    # ---------------- Derived KPI helpers ----------------
    def _cutoff(self, minutes: int) -> float:
        return (datetime.now(timezone.utc) - timedelta(minutes=minutes)).timestamp()

    def _filter_recent(self, minutes: int) -> List[RequestMetrics]:
        cutoff_ts = self._cutoff(minutes)
        return [m for m in self.metrics_history if m.timestamp.timestamp() > cutoff_ts]

    def get_aggregated_metrics(self, time_window_minutes: int = 60) -> Dict[str, Any]:
        """Return aggregated metrics for a time window (same behavior as before)"""
        cutoff_time = datetime.now(timezone.utc).timestamp() - (time_window_minutes * 60)
        recent_metrics = [
            m for m in self.metrics_history
            if m.timestamp.timestamp() > cutoff_time
        ]
        if not recent_metrics:
            return {
                "time_window_minutes": time_window_minutes,
                "total_requests": 0,
                "error_rate": 0.0,
                "avg_latency_ms": 0.0,
                "avg_cost_usd": 0.0,
                "total_tokens": 0,
                "total_cost_usd": 0.0
            }
        total_requests = len(recent_metrics)
        error_count = sum(1 for m in recent_metrics if m.error)
        error_rate = error_count / total_requests if total_requests > 0 else 0.0
        avg_latency = sum(m.total_latency_ms for m in recent_metrics) / total_requests
        avg_cost = sum(m.estimated_cost_usd for m in recent_metrics) / total_requests
        total_tokens = sum(m.total_tokens for m in recent_metrics)
        total_cost = sum(m.estimated_cost_usd for m in recent_metrics)
        avg_preprocessing = sum(m.preprocessing_ms for m in recent_metrics) / total_requests
        avg_llm_call = sum(m.llm_api_call_ms for m in recent_metrics) / total_requests
        avg_postprocessing = sum(m.postprocessing_ms for m in recent_metrics) / total_requests
        avg_metrics_export = sum(m.metrics_export_ms for m in recent_metrics) / total_requests
        avg_unaccounted = sum(m.unaccounted_ms for m in recent_metrics) / total_requests
        return {
            "time_window_minutes": time_window_minutes,
            "total_requests": total_requests,
            "error_count": error_count,
            "error_rate": error_rate,
            "avg_latency_ms": avg_latency,
            "avg_cost_usd": avg_cost,
            "total_tokens": total_tokens,
            "total_cost_usd": total_cost,
            "step_breakdown": {
                "avg_preprocessing_ms": avg_preprocessing,
                "avg_llm_api_call_ms": avg_llm_call,
                "avg_postprocessing_ms": avg_postprocessing,
                "avg_metrics_export_ms": avg_metrics_export,
                "avg_unaccounted_ms": avg_unaccounted
            },
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

    def _percentile(self, data: List[float], p: float) -> float:
        """Compute percentile (p in 0..1) of list of numbers"""
        if not data:
            return 0.0
        data_sorted = sorted(data)
        k = (len(data_sorted)-1) * p
        f = math.floor(k)
        c = math.ceil(k)
        if f == c:
            return data_sorted[int(k)]
        d0 = data_sorted[int(f)] * (c - k)
        d1 = data_sorted[int(c)] * (k - f)
        return d0 + d1

    def latency_percentiles(self, window_minutes: int = 60, percentiles: Tuple[float, ...] = (0.5, 0.95, 0.99)) -> Dict[str, float]:
        """Return latency percentiles for total latency in given window"""
        recent = self._filter_recent(window_minutes)
        latencies = [m.total_latency_ms for m in recent if m.total_latency_ms is not None]
        result = {}
        for p in percentiles:
            result[f"p{int(p*100)}"] = self._percentile(latencies, p) if latencies else 0.0
        return result

    def step_latency_percentiles(self, step: str, window_minutes: int = 60, percentiles: Tuple[float, ...] = (0.5, 0.95, 0.99)) -> Dict[str, float]:
        """Return percentiles for a particular step (preprocessing|llm_api_call|postprocessing|metrics_export)"""
        recent = self._filter_recent(window_minutes)
        key_map = {
            "preprocessing": lambda m: m.preprocessing_ms,
            "llm_api_call": lambda m: m.llm_api_call_ms,
            "postprocessing": lambda m: m.postprocessing_ms,
            "metrics_export": lambda m: m.metrics_export_ms
        }
        getter = key_map.get(step)
        if not getter:
            return {}
        values = [getter(m) for m in recent if getter(m) is not None]
        result = {}
        for p in percentiles:
            result[f"p{int(p*100)}"] = self._percentile(values, p) if values else 0.0
        return result

    def token_stats(self, window_minutes: int = 60) -> Dict[str, Any]:
        """Return token usage aggregated (avg/median/95) for given window"""
        recent = self._filter_recent(window_minutes)
        prompt = [m.input_tokens for m in recent]
        completion = [m.output_tokens for m in recent]
        total = [m.total_tokens for m in recent]
        def summary(arr):
            if not arr:
                return {"count": 0, "avg": 0.0, "p95": 0.0}
            avg = sum(arr)/len(arr)
            p95 = self._percentile(arr, 0.95)
            return {"count": len(arr), "avg": avg, "p95": p95}
        return {
            "prompt": summary(prompt),
            "completion": summary(completion),
            "total": summary(total)
        }

    def estimate_costs(self, window_minutes: int = 60) -> Dict[str, Any]:
        """Estimate cost per request and projection using in-memory metrics for a time window"""
        recent = self._filter_recent(window_minutes)
        if not recent:
            return {"cost_per_request": 0.0, "daily_projection": 0.0, "requests_observed": 0}
        costs = [m.estimated_cost_usd for m in recent]
        avg_cost = sum(costs)/len(costs)
        # requests per observed window (per minute)
        requests_observed = len(recent)
        minutes = window_minutes
        # project daily cost: avg_cost * requests_per_minute * 60 * 24
        req_per_minute = requests_observed / minutes
        daily_projection = avg_cost * req_per_minute * 60 * 24
        return {
            "cost_per_request": avg_cost,
            "requests_observed": requests_observed,
            "requests_per_minute": req_per_minute,
            "daily_projection": daily_projection,
            "weekly_projection": daily_projection * 7,
            "monthly_projection": daily_projection * 30
        }

    def error_rate(self, window_minutes: int = 60) -> Dict[str, Any]:
        """Return error rate and breakdown by type for a window"""
        recent = self._filter_recent(window_minutes)
        total = len(recent)
        if total == 0:
            return {"total": 0, "error_rate": 0.0, "by_type": {}}
        error_count = sum(1 for m in recent if m.error)
        by_type = {}
        for m in recent:
            if m.error:
                typ = (m.error_type or "unknown").lower()
                by_type[typ] = by_type.get(typ, 0) + 1
        return {"total": total, "error_rate": error_count/total, "by_type": by_type}

    def get_model_stats(self) -> Dict[str, Any]:
        """Get statistics by model (same behavior as before)"""
        model_stats = {}
        for metrics in self.metrics_history:
            model = metrics.model
            if model not in model_stats:
                model_stats[model] = {
                    "request_count": 0,
                    "total_tokens": 0,
                    "total_cost": 0.0,
                    "total_latency": 0.0,
                    "error_count": 0
                }
            stats = model_stats[model]
            stats["request_count"] += 1
            stats["total_tokens"] += metrics.total_tokens
            stats["total_cost"] += metrics.estimated_cost_usd
            stats["total_latency"] += metrics.total_latency_ms
            if metrics.error:
                stats["error_count"] += 1
        # Calculate averages
        for model, stats in model_stats.items():
            if stats["request_count"] > 0:
                stats["avg_latency_ms"] = stats["total_latency"] / stats["request_count"]
                stats["avg_cost_usd"] = stats["total_cost"] / stats["request_count"]
                stats["error_rate"] = stats["error_count"] / stats["request_count"]
            else:
                stats["avg_latency_ms"] = 0.0
                stats["avg_cost_usd"] = 0.0
                stats["error_rate"] = 0.0
        return model_stats

    def clear_old_metrics(self, days_to_keep: int = 7):
        """Clear metrics older than specified days"""
        cutoff_time = datetime.now(timezone.utc).timestamp() - (days_to_keep * 24 * 60 * 60)
        self.metrics_history = [
            m for m in self.metrics_history
            if m.timestamp.timestamp() > cutoff_time
        ]
        logger.info(f"Cleared metrics older than {days_to_keep} days")


# Global metrics collector instance
metrics_collector = MetricsCollector()
