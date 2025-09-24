# llm_apm/utils/router.py
from typing import Optional
from ..config.settings import config


def choose_model(endpoint: str, intent: Optional[str] = None) -> str:
    """
    Basic rule-based model router.
    - cheap tasks -> gpt-35-turbo
    - generation/longform -> gpt-4.1-mini
    - default -> config.default_model or gpt-4.1-mini
    """
    endpoint = (endpoint or "").lower()
    intent = (intent or "").lower()

    # explicit cheap intents
    cheap_keywords = ["summary", "summarize", "snippet", "search", "spell", "grammar", "tokenize", "embed-check"]
    for kw in cheap_keywords:
        if kw in endpoint or kw in intent:
            return getattr(config, "cheap_model", "gpt-35-turbo")

    # heavy generation
    heavy_keywords = ["generate", "compose", "longform", "story", "essay"]
    for kw in heavy_keywords:
        if kw in endpoint or kw in intent:
            return getattr(config, "high_quality_model", "gpt-4.1-mini")

    # fallback
    return getattr(config, "default_model", "gpt-4.1-mini")
