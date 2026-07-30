from __future__ import annotations
import dataclasses
import enum
import json
import math
from collections.abc import Mapping, Sequence, Set
from typing import Any

def to_primitive(value: Any) -> Any:
    if dataclasses.is_dataclass(value) and not isinstance(value, type):
        return {field.name: to_primitive(getattr(value, field.name)) for field in dataclasses.fields(value)}
    if isinstance(value, enum.Enum):
        return to_primitive(value.value)
    if isinstance(value, Mapping):
        return {str(key): to_primitive(item) for key, item in value.items()}
    if isinstance(value, Set) and not isinstance(value, (str, bytes, bytearray)):
        return [to_primitive(item) for item in sorted(value, key=lambda item: repr(item))]
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return [to_primitive(item) for item in value]
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("Non-finite floats are not serializable")
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    raise TypeError(f"Unsupported value type: {type(value).__name__}")

def canonical_json_dumps(value: Any) -> str:
    return json.dumps(to_primitive(value), ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
