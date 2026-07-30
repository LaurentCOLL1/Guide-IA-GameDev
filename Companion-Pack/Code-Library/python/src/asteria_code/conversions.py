from __future__ import annotations
from typing import Any

def clamp_float(value: float, minimum: float, maximum: float) -> float:
    if minimum > maximum:
        raise ValueError("minimum must be <= maximum")
    return max(minimum, min(maximum, float(value)))

def seconds_to_milliseconds(seconds: float) -> int:
    if seconds < 0:
        raise ValueError("seconds must be non-negative")
    return int(round(seconds * 1000.0))

def milliseconds_to_seconds(milliseconds: int) -> float:
    if milliseconds < 0:
        raise ValueError("milliseconds must be non-negative")
    return milliseconds / 1000.0

def parse_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, int) and value in (0, 1):
        return bool(value)
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"1", "true", "yes", "on"}:
            return True
        if normalized in {"0", "false", "no", "off"}:
            return False
    raise ValueError(f"Cannot parse boolean from {value!r}")
