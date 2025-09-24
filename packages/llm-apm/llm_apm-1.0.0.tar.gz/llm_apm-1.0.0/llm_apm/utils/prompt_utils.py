# llm_apm/utils/prompt_utils.py
from typing import Tuple, Optional
from ..config.settings import config
SYSTEM_PROMPT = getattr(config, "system_prompt", "You are a concise assistant. Answer briefly and directly.")
import re

def build_prompt_and_truncate(user_prompt: str, max_chars: Optional[int] = None) -> Tuple[str, bool, Optional[str]]:
    """
    Return (final_prompt, was_truncated, truncated_reason)
    - final_prompt: the system prompt + user prompt (normalized)
    - was_truncated: bool whether truncation occurred
    - truncated_reason: short reason string (or None)
    """
    if user_prompt is None:
        user_prompt = ""
    max_chars = max_chars or getattr(config, "prompt_max_chars", 200000)
    p = user_prompt.strip()
    was_truncated = False
    truncated_reason = None
    # normalize: collapse repeating whitespace, strip lines, limit lines
    lines = [ln.strip() for ln in p.splitlines() if ln.strip()]
    if len(" ".join(lines)) > max_chars:
        # truncate by characters after joining
        joined = " ".join(lines)
        joined = joined[:max_chars]
        # ensure no broken multibyte boundaries (safe slicing)
        p = joined
        was_truncated = True
        truncated_reason = f"truncated_to_{max_chars}_chars"
    else:
        # limit lines to avoid extremely long prompt with many lines
        if len(lines) > 5000:
            lines = lines[:5000]
            was_truncated = True
            truncated_reason = "truncated_lines_5000"
        p = "\n".join(lines)
    final_prompt = SYSTEM_PROMPT + "\n\n" + p if p else SYSTEM_PROMPT
    return final_prompt, was_truncated, truncated_reason

def compress_prompt_text(s: str, max_len: int = None) -> str:
    """
    Lightweight prompt compression:
    - normalize whitespace
    - truncate to max_len if provided
    This is intentionally conservative to avoid changing semantics.
    """
    if not s:
        return ""
    s2 = re.sub(r'\s+', ' ', s).strip()
    if max_len and len(s2) > max_len:
        s2 = s2[:max_len]
    return s2
