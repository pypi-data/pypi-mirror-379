# llm_apm/utils/sampler.py
"""
Deterministic sampler and experiment/variant utilities.
- should_sample(user_id, sampling_rate): deterministic sampling by user_id (hash).
- decide_variant(user_id, variants): deterministic assignment to experiment variants.
- get_sampling_rate(): read sampling rate from config (fallback to 1.0).
"""
from typing import Optional, Dict
import hashlib
import logging

logger = logging.getLogger(__name__)


def _hash_to_fraction(key: str) -> float:
    """
    Hash a string to a deterministic fraction in [0.0, 1.0).
    Uses SHA-256 and converts the first 8 bytes to an int to keep behavior stable.
    """
    if not key:
        return 0.0
    h = hashlib.sha256(key.encode("utf-8")).digest()
    val = int.from_bytes(h[:8], "big")
    # Map to [0,1) using modulus of 1e9 for good distribution
    return (val % (10**9)) / 10**9


def should_sample(user_id: Optional[str], sampling_rate: float) -> bool:
    """
    Deterministic sampling based on user_id.
    - If sampling_rate >= 1.0 -> always sample.
    - If user_id provided -> deterministic hash-based sampling.
    - If no user_id -> fallback to probabilistic sampling.
    """
    if sampling_rate >= 1.0:
        return True
    if user_id:
        frac = _hash_to_fraction(user_id)
        return frac < sampling_rate
    # fallback: non-deterministic sampling — keep for backward compatibility
    import random
    return random.random() < sampling_rate


def decide_variant(user_id: Optional[str], variants: Optional[Dict[str, float]] = None) -> str:
    """
    Deterministic variant assignment.
    variants: mapping name -> weight (weights sum to <= 1.0; remainder goes to last key).
    Example: {'control': 0.5, 'treatment': 0.5}
    If no variants provided, returns "control".
    """
    if not variants:
        return "control"
    # Normalize ordering and weights
    items = list(variants.items())
    # Build cumulative buckets
    cumulative = []
    total = 0.0
    for name, weight in items:
        total += float(weight)
        cumulative.append((name, total))
    # If user_id missing, use a random fraction
    frac = _hash_to_fraction(user_id) if user_id else _hash_to_fraction("random_fallback")
    for name, bound in cumulative:
        if frac < bound:
            return name
    # fallback to last variant
    return items[-1][0]


def get_sampling_rate() -> float:
    """Return sampling rate from config (safe fallback to 1.0)."""
    try:
        from llm_apm.config.settings import config
        return float(getattr(config, "sampling_rate", 1.0))
    except Exception as e:
        logger.debug(f"Could not read sampling_rate from config: {e}")
        return 1.0
