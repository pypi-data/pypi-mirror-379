# llm_apm/core/decorators.py
import functools
import logging
import inspect
import time
from typing import Any, Callable, Optional, Dict
from contextvars import ContextVar

from ..core.timer import Timer  # keep Timer for actual measurement

logger = logging.getLogger(__name__)

# Defensive: middleware should set a fresh dict per-request.
# We allow default None so file can be used standalone; functions below handle None safely.
current_step_timer: ContextVar[Optional[dict]] = ContextVar('current_step_timer', default=None)

def _get_context() -> dict:
    """
    Return the current context dict (not None). This is defensive:
    - If middleware set a per-request dict, we'll use it.
    - If it's None, we create a transient dict (won't leak across requests).
    """
    ctx = current_step_timer.get()
    if ctx is None:
        ctx = {}
        # do NOT call current_step_timer.set(ctx) here because middleware should own lifecycle.
        # We return the local dict so decorators still function even if middleware forgot to initialize.
    return ctx

def step(step_name: str):
    """
    Decorator to time a step and publish numeric durations into the per-request ContextVar dict.
    - Stores start_time (perf_counter), running flag, duration_ms (on completion), success/error.
    - Avoids storing Timer objects in the ContextVar to reduce cross-task/thread fragility.
    Usage: @step("preprocessing")
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            timer = Timer()
            start_ts = timer.start()
            # read context defensively
            context = _get_context()
            # create/override entry for this step
            context_entry = {
                "start_time": float(start_ts),
                "running": True,
                "duration_ms": None,
                "success": None,
                "error": None
            }
            try:
                # Try to set into ContextVar only if it is already present, to avoid clobbering middleware-managed token.
                if current_step_timer.get() is not None:
                    # update the existing dict in-place (middleware's dict)
                    ctx = current_step_timer.get()
                    ctx[step_name] = context_entry
                    current_step_timer.set(ctx)
                else:
                    # use local transient dict (no set) so decorator still works
                    context[step_name] = context_entry
            except Exception:
                # Best-effort: if failing to set ContextVar, keep local copy
                try:
                    context[step_name] = context_entry
                except Exception:
                    pass

            try:
                result = func(*args, **kwargs)
                elapsed_ms = timer.stop() * 1000.0
                context_entry.update({
                    "duration_ms": float(elapsed_ms),
                    "running": False,
                    "success": True,
                    "error": None
                })
                # persist back
                try:
                    if current_step_timer.get() is not None:
                        ctx = current_step_timer.get()
                        ctx[step_name] = context_entry
                        current_step_timer.set(ctx)
                    else:
                        context[step_name] = context_entry
                except Exception:
                    pass

                logger.debug("Step '%s' completed in %.2fms", step_name, elapsed_ms)
                return result
            except Exception as e:
                try:
                    elapsed_ms = timer.stop() * 1000.0
                except Exception:
                    elapsed_ms = 0.0
                context_entry.update({
                    "duration_ms": float(elapsed_ms),
                    "running": False,
                    "success": False,
                    "error": str(e)
                })
                try:
                    if current_step_timer.get() is not None:
                        ctx = current_step_timer.get()
                        ctx[step_name] = context_entry
                        current_step_timer.set(ctx)
                    else:
                        context[step_name] = context_entry
                except Exception:
                    pass

                logger.error("Step '%s' failed after %.2fms: %s", step_name, elapsed_ms, e)
                raise

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            timer = Timer()
            start_ts = timer.start()
            context = _get_context()
            context_entry = {
                "start_time": float(start_ts),
                "running": True,
                "duration_ms": None,
                "success": None,
                "error": None
            }
            try:
                if current_step_timer.get() is not None:
                    ctx = current_step_timer.get()
                    ctx[step_name] = context_entry
                    current_step_timer.set(ctx)
                else:
                    context[step_name] = context_entry
            except Exception:
                try:
                    context[step_name] = context_entry
                except Exception:
                    pass

            try:
                result = await func(*args, **kwargs)
                elapsed_ms = timer.stop() * 1000.0
                context_entry.update({
                    "duration_ms": float(elapsed_ms),
                    "running": False,
                    "success": True,
                    "error": None
                })
                try:
                    if current_step_timer.get() is not None:
                        ctx = current_step_timer.get()
                        ctx[step_name] = context_entry
                        current_step_timer.set(ctx)
                    else:
                        context[step_name] = context_entry
                except Exception:
                    pass

                logger.debug("Step '%s' completed in %.2fms", step_name, elapsed_ms)
                return result
            except Exception as e:
                try:
                    elapsed_ms = timer.stop() * 1000.0
                except Exception:
                    elapsed_ms = 0.0
                context_entry.update({
                    "duration_ms": float(elapsed_ms),
                    "running": False,
                    "success": False,
                    "error": str(e)
                })
                try:
                    if current_step_timer.get() is not None:
                        ctx = current_step_timer.get()
                        ctx[step_name] = context_entry
                        current_step_timer.set(ctx)
                    else:
                        context[step_name] = context_entry
                except Exception:
                    pass

                logger.error("Step '%s' failed after %.2fms: %s", step_name, elapsed_ms, e)
                raise

        return async_wrapper if inspect.iscoroutinefunction(func) else sync_wrapper

    return decorator

def get_current_step_metrics() -> Dict[str, float]:
    """
    Read the current ContextVar dict and return a map of { '<step>_ms': <float> }.
    For running steps we compute a best-effort elapsed using stored start_time.
    """
    ctx = current_step_timer.get()
    metrics: Dict[str, float] = {}
    now = time.perf_counter()
    if not ctx:
        # defensive: no context available
        logger.debug("get_current_step_metrics: no current_step_timer context found")
        return metrics

    for step_name, data in list(ctx.items()):
        try:
            if not isinstance(data, dict):
                continue
            if data.get("duration_ms") is not None:
                metrics[f"{step_name}_ms"] = float(data["duration_ms"])
            else:
                # step still running or missing duration - best-effort via start_time
                start = data.get("start_time")
                if start:
                    try:
                        elapsed_ms = (now - float(start)) * 1000.0
                        metrics[f"{step_name}_ms"] = float(elapsed_ms)
                    except Exception:
                        metrics[f"{step_name}_ms"] = 0.0
                else:
                    metrics[f"{step_name}_ms"] = 0.0
        except Exception:
            # safe fallback
            metrics[f"{step_name}_ms"] = 0.0
    return metrics

def clear_step_context():
    """
    Clear the current step dict for the context. Middleware ideally should use tokens/reset;
    this function sets an empty dict so callers can call it to avoid leaks when needed.
    """
    try:
        current_step_timer.set({})
    except Exception:
        pass
