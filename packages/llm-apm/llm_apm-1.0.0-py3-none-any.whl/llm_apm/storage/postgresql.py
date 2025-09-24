# llm_apm/storage/postgresql.py
"""
PostgreSQL storage backend for LLM-APM (dynamic placeholders -> eliminates param mismatches).
This version matches your current DB columns (no session_id/user_hash/cache_* columns).
"""
import logging
from datetime import datetime, timezone, timedelta
from typing import List, Optional
import psycopg2
import psycopg2.extras
import uuid
import os
import threading
import queue
import time
import psycopg2.errors
from decimal import Decimal, ROUND_HALF_UP
from ..core.metrics import RequestMetrics

logger = logging.getLogger(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("Set DATABASE_URL env var")

def _get_conn():
    return psycopg2.connect(DATABASE_URL)

class MetricsWriter(threading.Thread):
    def __init__(self, q: "queue.Queue[RequestMetrics]", stop_event: threading.Event, max_retries: int = 3):
        super().__init__(daemon=True)
        self.q = q
        self.stop_event = stop_event
        self.max_retries = max_retries

    def run(self):
        logger.info("MetricsWriter background thread started")
        while not self.stop_event.is_set():
            try:
                metrics = self.q.get(timeout=1.0)
            except queue.Empty:
                continue
            try:
                success = self._write_with_retries(metrics)
                if not success:
                    logger.error("Failed to persist metrics after retries, dropping: %s", getattr(metrics, "request_id", "<noid>"))
            except Exception as e:
                logger.exception("Unexpected error in MetricsWriter: %s", e)
            finally:
                try:
                    self.q.task_done()
                except Exception:
                    pass
        logger.info("MetricsWriter exiting (stop_event set)")

    def _write_with_retries(self, metrics: RequestMetrics) -> bool:
        backoff = 0.5
        for attempt in range(1, self.max_retries + 1):
            try:
                _store_metrics_sync(metrics)
                return True
            except Exception as e:
                logger.warning("MetricsWriter write attempt %d failed: %s", attempt, e)
                time.sleep(backoff)
                backoff *= 2
        return False

def _store_metrics_sync(metrics: RequestMetrics) -> bool:
    conn = _get_conn()
    try:
        cur = conn.cursor()
        # ensure request_id
        if not metrics.request_id:
            metrics.request_id = str(uuid.uuid4())
        ts = metrics.timestamp or datetime.now(timezone.utc)
        user_id = metrics.user_id if metrics.user_id else None

        # Build columns and params in the same order as DB has (no session_id, no cache fields)
        columns = [
            "request_id", "timestamp",
            "total_latency_ms", "preprocessing_ms", "llm_api_call_ms",
            "postprocessing_ms", "metrics_export_ms",
            "input_tokens", "output_tokens", "total_tokens", "estimated_cost_usd",
            "model", "endpoint", "user_id",
            "error", "error_message", "error_type",
            "status_code", "request_size_bytes", "response_size_bytes"
        ]

        # Prepare Decimal for cost
        try:
            cost = getattr(metrics, "estimated_cost_usd", 0.0) or 0.0
            cost_dec = Decimal(str(cost)).quantize(Decimal("0.00000001"), rounding=ROUND_HALF_UP)
        except Exception:
            cost_dec = Decimal("0.00000000")

        params = [
            metrics.request_id, ts,
            metrics.total_latency_ms, metrics.preprocessing_ms, metrics.llm_api_call_ms,
            metrics.postprocessing_ms, metrics.metrics_export_ms,
            metrics.input_tokens, metrics.output_tokens, metrics.total_tokens, cost_dec,
            metrics.model, metrics.endpoint, user_id,
            bool(metrics.error) if metrics.error is not None else False,
            metrics.error_message, metrics.error_type,
            metrics.status_code if metrics.status_code is not None else 200,
            metrics.request_size_bytes if metrics.request_size_bytes is not None else 0,
            metrics.response_size_bytes if metrics.response_size_bytes is not None else 0
        ]

        # build SQL dynamically to match params length exactly
        col_list_sql = ", ".join(columns)
        placeholders = ", ".join(["%s"] * len(params))
        insert_sql = f"""
            INSERT INTO llm_apm.llm_metrics (
                id, {col_list_sql}
            ) VALUES (
                gen_random_uuid(), {placeholders}
            ) ON CONFLICT (request_id) DO NOTHING
        """

        # Validate counts
        placeholder_count = insert_sql.count("%s")
        if placeholder_count != len(params):
            logger.error(
                "SQL placeholder/param mismatch after dynamic build: placeholders=%d, params=%d. columns=%s params_preview=%s",
                placeholder_count, len(params), col_list_sql, repr(params[:12])
            )
            raise RuntimeError(f"SQL placeholder/param mismatch: placeholders={placeholder_count}, params={len(params)}")

        # Attempt execute
        try:
            cur.execute(insert_sql, tuple(params))
            conn.commit()
            cur.close()
            return True
        except psycopg2.errors.InvalidColumnReference:
            # DB doesn't have unique constraint supporting ON CONFLICT -> retry without ON CONFLICT
            logger.warning("ON CONFLICT failed (no unique constraint on request_id). Retrying INSERT without ON CONFLICT.")
            conn.rollback()
            fallback_sql = insert_sql.replace(" ON CONFLICT (request_id) DO NOTHING", "")
            try:
                cur.execute(fallback_sql, tuple(params))
                conn.commit()
                cur.close()
                return True
            except Exception as e:
                conn.rollback()
                logger.exception("Fallback INSERT failed: %s", e)
                raise
        except Exception as e:
            conn.rollback()
            logger.exception("Failed to store metrics (execute error): %s", e)
            raise
    finally:
        conn.close()

class PostgreSQLStorage:
    def __init__(self, queue_maxsize: int = 10000):
        logger.info("PostgreSQLStorage initialized (psycopg2 + background writer)")
        self._queue: "queue.Queue[RequestMetrics]" = queue.Queue(maxsize=queue_maxsize)
        self._stop_event = threading.Event()
        self._writer = MetricsWriter(self._queue, self._stop_event)
        self._writer.start()

    def store_metrics(self, metrics: RequestMetrics) -> bool:
        try:
            # skip pure cache hits
            if getattr(metrics, "cache_hit", False) and not getattr(metrics, "error", False):
                logger.debug("Skipping persistence for pure cache hit (request_id=%s)", getattr(metrics, "request_id", None))
                return True
        except Exception:
            pass

        try:
            self._queue.put_nowait(metrics)
            return True
        except queue.Full:
            logger.warning("Metrics queue full, falling back to synchronous write (this may block)")
            try:
                return _store_metrics_sync(metrics)
            except Exception:
                return False

    def store_metrics_sync(self, metrics: RequestMetrics) -> bool:
        return _store_metrics_sync(metrics)

    def get_metrics(self, start_time: Optional[datetime] = None, end_time: Optional[datetime] = None, limit: int = 1000) -> List[RequestMetrics]:
        conn = _get_conn()
        try:
            cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            q = "SELECT * FROM llm_apm.llm_metrics"
            params = []
            if start_time and end_time:
                q += " WHERE timestamp BETWEEN %s AND %s"
                params.extend([start_time, end_time])
            elif start_time:
                q += " WHERE timestamp >= %s"
                params.append(start_time)
            q += " ORDER BY timestamp DESC LIMIT %s"
            params.append(limit)
            cur.execute(q, tuple(params))
            rows = cur.fetchall()
            cur.close()
            result = []
            for r in rows:
                rm = RequestMetrics(
                    request_id=r.get("request_id") or str(uuid.uuid4()),
                    timestamp=r.get("timestamp") or datetime.now(timezone.utc),
                    total_latency_ms=r.get("total_latency_ms") or 0.0,
                    preprocessing_ms=r.get("preprocessing_ms") or 0.0,
                    llm_api_call_ms=r.get("llm_api_call_ms") or 0.0,
                    postprocessing_ms=r.get("postprocessing_ms") or 0.0,
                    metrics_export_ms=r.get("metrics_export_ms") or 0.0,
                    input_tokens=r.get("input_tokens") or 0,
                    output_tokens=r.get("output_tokens") or 0,
                    total_tokens=r.get("total_tokens") or 0,
                    estimated_cost_usd=float(r.get("estimated_cost_usd") or 0.0),
                    model=r.get("model") or "unknown",
                    endpoint=r.get("endpoint") or "unknown",
                    user_id=str(r["user_id"]) if r.get("user_id") else None,
                    session_id=None,
                    error=r.get("error", False),
                    error_message=r.get("error_message"),
                    error_type=r.get("error_type"),
                    status_code=r.get("status_code", 200),
                    request_size_bytes=r.get("request_size_bytes", 0),
                    response_size_bytes=r.get("response_size_bytes", 0),
                    cache_hit=False,
                    cache_lookup_ms=0.0,
                    error_context=None
                )
                result.append(rm)
            return result
        except Exception as e:
            logger.exception("Failed to get metrics: %s", e)
            return []
        finally:
            conn.close()

    def cleanup_old_data(self, days_to_keep: int = 30) -> int:
        conn = _get_conn()
        try:
            cur = conn.cursor()
            cutoff = datetime.now(timezone.utc) - timedelta(days=days_to_keep)
            cur.execute("DELETE FROM llm_apm.llm_metrics WHERE timestamp < %s", (cutoff,))
            deleted = cur.rowcount
            conn.commit()
            cur.close()
            return deleted
        except Exception as e:
            logger.exception("cleanup_old_data failed: %s", e)
            return 0
        finally:
            conn.close()

    def close(self):
        logger.info("PostgreSQLStorage shutting down: waiting for queue to drain")
        timeout_seconds = 5
        try:
            self._stop_event.set()
            self._writer.join(timeout=timeout_seconds)
        except Exception as e:
            logger.debug("Error shutting down writer: %s", e)

    def health_check(self) -> bool:
        try:
            conn = _get_conn()
            cur = conn.cursor()
            cur.execute("SELECT 1")
            cur.close()
            conn.close()
            return True
        except Exception as e:
            logger.exception("health_check failed: %s", e)
            return False

def create_storage_from_config(config=None, **kwargs):
    return PostgreSQLStorage()
