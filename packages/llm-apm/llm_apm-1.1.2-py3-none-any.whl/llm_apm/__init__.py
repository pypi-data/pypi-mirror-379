# llm_apm/__init__.py
"""
LLM Application Performance Monitoring (LLM-APM)
Minimal package exports — keep top-level API small and stable.
"""

__version__ = "1.0.0"

# Core monitor & helpers
from .core.monitor import LLMMonitor, get_global_monitor, set_global_monitor

# Step decorator & helpers (keep these at top level since they are small and widely used)
try:
    from .core.decorator import step, get_current_step_metrics, clear_step_context
except Exception:
    # graceful fallback if name/file differs or optional failure
    def _missing_step(*args, **kwargs):
        raise RuntimeError("llm_apm.step not available; import .core.decorator directly")
    step = _missing_step
    get_current_step_metrics = lambda: {}
    clear_step_context = lambda: None

# Middleware, exporter, storage, config (top-level conveniences)
from .middleware.fastapi import LLMAPMMiddleware
from .exporters.prometheus import PrometheusExporter
from .storage.postgresql import PostgreSQLStorage, create_storage_from_config
from .config.settings import LLMAPMConfig, config

# Cache helpers (try to expose but fail gracefully)
try:
    from .utils.cache import init_redis, close_redis, get_key as cache_get_key, set_key as cache_set_key, make_key as cache_make_key
except Exception:
    # provide simple fallbacks that raise if used
    def init_redis(*args, **kwargs):
        raise RuntimeError("init_redis not available; ensure llm_apm.utils.cache is importable")
    def close_redis(*args, **kwargs):
        raise RuntimeError("close_redis not available; ensure llm_apm.utils.cache is importable")
    def cache_get_key(*args, **kwargs):
        raise RuntimeError("cache_get_key not available; ensure llm_apm.utils.cache is importable")
    def cache_set_key(*args, **kwargs):
        raise RuntimeError("cache_set_key not available; ensure llm_apm.utils.cache is importable")
    def cache_make_key(*args, **kwargs):
        raise RuntimeError("cache_make_key not available; ensure llm_apm.utils.cache is importable")

__all__ = [
    "LLMMonitor",
    "get_global_monitor",
    "set_global_monitor",
    "step",
    "get_current_step_metrics",
    "clear_step_context",
    "LLMAPMMiddleware",
    "PrometheusExporter",
    "PostgreSQLStorage",
    "create_storage_from_config",
    "LLMAPMConfig",
    "config",
    "init_redis",
    "close_redis",
    "cache_get_key",
    "cache_set_key",
    "cache_make_key",
]
