extends RefCounted
class_name ValueConversions

static func clamp_float(value: float, minimum: float, maximum: float) -> float:
    assert(minimum <= maximum, "minimum must be <= maximum")
    return clampf(value, minimum, maximum)

static func seconds_to_milliseconds(seconds: float) -> int:
    assert(seconds >= 0.0, "seconds must be non-negative")
    return int(round(seconds * 1000.0))

static func milliseconds_to_seconds(milliseconds: int) -> float:
    assert(milliseconds >= 0, "milliseconds must be non-negative")
    return float(milliseconds) / 1000.0

static func parse_bool(value: Variant) -> Variant:
    if value is bool:
        return value
    if value is int and (value == 0 or value == 1):
        return value == 1
    if value is String:
        var normalized: String = str(value).strip_edges().to_lower()
        if normalized in ["1", "true", "yes", "on"]:
            return true
        if normalized in ["0", "false", "no", "off"]:
            return false
    return null
