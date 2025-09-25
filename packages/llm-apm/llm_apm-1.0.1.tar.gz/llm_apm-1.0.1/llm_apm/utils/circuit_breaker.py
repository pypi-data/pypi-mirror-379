# llm_apm/utils/circuit_breaker.py
import asyncio
import time
import logging
from typing import Callable, Optional

logger = logging.getLogger(__name__)

class CircuitOpen(Exception):
    pass

class CircuitBreaker:
    """
    Simple circuit breaker:
    - fail_threshold: number of failures before opening
    - recovery_time: seconds to attempt half-open
    - window_seconds: failure counting window
    """
    def __init__(self, fail_threshold: int = 5, recovery_time: int = 30, window_seconds: int = 60, name: str = "cb"):
        self.fail_threshold = fail_threshold
        self.recovery_time = recovery_time
        self.window_seconds = window_seconds
        self.name = name
        self.failures = []
        self.open_until = 0
        self._lock = asyncio.Lock()

    async def call(self, coro_func: Callable, *args, **kwargs):
        async with self._lock:
            now = time.time()
            # clean failures
            self.failures = [t for t in self.failures if now - t <= self.window_seconds]
            if self.is_open():
                # circuit is open
                raise CircuitOpen(f"Circuit {self.name} is open until {self.open_until}")
        try:
            res = await coro_func(*args, **kwargs)
            # success: maybe close circuit (nothing to do)
            return res
        except Exception as e:
            await self._register_failure()
            raise

    def is_open(self) -> bool:
        return time.time() < self.open_until

    async def _register_failure(self):
        async with self._lock:
            self.failures.append(time.time())
            if len(self.failures) >= self.fail_threshold:
                # trip
                self.open_until = time.time() + self.recovery_time
                logger.warning("Circuit %s opened until %s", self.name, self.open_until)

# simple bulkhead: concurrency limiter
class Bulkhead:
    def __init__(self, max_concurrency: int = 10):
        self.sema = asyncio.Semaphore(max_concurrency)

    async def run(self, coro_func: Callable, *args, **kwargs):
        async with self.sema:
            return await coro_func(*args, **kwargs)
