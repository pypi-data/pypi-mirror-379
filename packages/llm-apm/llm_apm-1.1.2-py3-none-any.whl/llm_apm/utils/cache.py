# llm_apm/utils/cache.py
"""
Async Redis-backed cache helpers with in-memory fallback.
Ensures responses are stored and returned exactly (use ensure_ascii=False).
Exports:
- init_redis()
- close_redis()
- make_key(obj_string, params)
- get_key(key) -> returns wrapper {"stored_at": <ts>, "value": <payload>}
- set_key(key, payload, ttl_seconds)
"""
import os
import json
import time
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

# Prefer modern redis.asyncio, fall back to legacy aioredis
aioredis_client = None
_aioredis_backend = None
try:
    # modern redis package exposes an asyncio submodule (redis>=4.2)
    import redis.asyncio as aioredis_client  # type: ignore
    _aioredis_backend = "redis.asyncio"
except Exception:
    try:
        # legacy aioredis package
        import aioredis as aioredis_client  # type: ignore
        _aioredis_backend = "aioredis"
    except Exception:
        aioredis_client = None
        _aioredis_backend = None

# expose backend name for debugging
__REDIS_ASYNC_BACKEND__ = _aioredis_backend
if __REDIS_ASYNC_BACKEND__:
    logger.info("Redis async backend available: %s", __REDIS_ASYNC_BACKEND__)
else:
    logger.info("No async redis backend available, will use in-memory cache")

REDIS_URL = os.getenv("REDIS_URL", None)
_redis_client = None

# in-memory fallback storage
_in_memory_cache: Dict[str, Dict[str, Any]] = {}  # key -> {"wrapper": {...}, "expires_at": ts}


async def init_redis(timeout_seconds: int = 5):
    """Try to connect to Redis; fall back to in-memory if unavailable."""
    global _redis_client
    if aioredis_client is None:
        logger.info("Async redis client not installed - using in-memory cache")
        _redis_client = None
        return None
    if not REDIS_URL:
        logger.info("REDIS_URL not set - using in-memory cache")
        _redis_client = None
        return None
    try:
        # modern redis.asyncio and legacy aioredis both support from_url, but
        # for legacy aioredis the constructor may differ; try to use from_url primarily.
        try:
            _redis_client = aioredis_client.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)
        except Exception:
            # fallback: try creating a client instance directly (older aioredis API)
            _redis_client = aioredis_client.Redis.from_url(REDIS_URL, encoding="utf-8", decode_responses=True)  # type: ignore
        # ping to verify connection
        await _redis_client.ping()
        logger.info("Connected to Redis at %s (backend=%s)", REDIS_URL, __REDIS_ASYNC_BACKEND__)
        return _redis_client
    except Exception as e:
        logger.warning("Failed to initialize Redis client: %s", e)
        _redis_client = None
        return None


async def close_redis():
    """Close redis connection if present."""
    global _redis_client
    try:
        if _redis_client:
            try:
                await _redis_client.close()
            except Exception:
                try:
                    _redis_client.close()
                except Exception:
                    pass
        _redis_client = None
        logger.info("Redis connection closed")
    except Exception as e:
        logger.debug("Error closing redis: %s", e)


def make_key(obj_string: str, params: Optional[Dict[str, Any]] = None) -> str:
    """Deterministic key for prompt + params."""
    import hashlib

    base = obj_string or ""
    if params:
        try:
            params_json = json.dumps(params, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        except Exception:
            params_json = str(sorted(params.items()))
        base = base + "|" + params_json
    h = hashlib.sha256(base.encode("utf-8")).hexdigest()
    return f"llm_cache:{h}"


async def get_key(key: str) -> Optional[Dict[str, Any]]:
    """
    Async get. Returns wrapper {"stored_at": ts, "value": payload} or None.
    """
    global _redis_client, _in_memory_cache
    if _redis_client:
        try:
            raw = await _redis_client.get(key)
            if not raw:
                return None
            try:
                # decode JSON exactly, preserving Unicode
                return json.loads(raw)
            except Exception as e:
                logger.debug("Failed to json.loads Redis value for key=%s: %s", key, e)
                return None
        except Exception as e:
            logger.debug("Redis GET error for key=%s: %s", key, e)
            return None

    # in-memory fallback
    entry = _in_memory_cache.get(key)
    if not entry:
        return None
    expires_at = entry.get("expires_at")
    if expires_at and time.time() > expires_at:
        _in_memory_cache.pop(key, None)
        return None
    return entry.get("wrapper")


async def set_key(key: str, payload_value: Dict[str, Any], ttl_seconds: Optional[int] = None) -> bool:
    """
    Async set: store wrapper {"stored_at": ts, "value": payload}
    Use ensure_ascii=False to preserve unicode exactly.
    """
    global _redis_client, _in_memory_cache
    wrapper = {"stored_at": time.time(), "value": payload_value}
    if _redis_client:
        try:
            raw = json.dumps(wrapper, ensure_ascii=False, separators=(",", ":"))
            # redis.asyncio and legacy aioredis accept ex= for TTL
            await _redis_client.set(key, raw, ex=ttl_seconds)
            logger.debug("Redis SET key=%s size=%d", key, len(raw))
            return True
        except Exception as e:
            logger.debug("Redis SET failed for key=%s: %s", key, e)
            return False

    # in-memory fallback
    try:
        expires_at = (time.time() + ttl_seconds) if ttl_seconds else None
        _in_memory_cache[key] = {"wrapper": wrapper, "expires_at": expires_at}
        logger.debug("In-memory cache set key=%s expires_at=%s", key, expires_at)
        return True
    except Exception as e:
        logger.debug("In-memory cache set failed for key=%s: %s", key, e)
        return False
