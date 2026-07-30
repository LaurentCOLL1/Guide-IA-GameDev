extends RefCounted
class_name CanonicalJson

static func canonicalize(value: Variant) -> Variant:
    if value is Dictionary:
        var result: Dictionary = {}
        var keys: Array = value.keys()
        keys.sort_custom(func(a: Variant, b: Variant) -> bool: return str(a) < str(b))
        for key in keys:
            result[str(key)] = canonicalize(value[key])
        return result
    if value is Array:
        var result_array: Array = []
        for item in value:
            result_array.append(canonicalize(item))
        return result_array
    return value

static func encode(value: Variant) -> String:
    return JSON.stringify(canonicalize(value), "", true, true)
