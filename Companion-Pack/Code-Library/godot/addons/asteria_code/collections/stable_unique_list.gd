extends RefCounted
class_name StableUniqueList

var _keys: Array[String] = []
var _values: Dictionary = {}

func add(key: String, value: Variant) -> bool:
    if key.is_empty() or _values.has(key):
        return false
    _keys.append(key)
    _values[key] = value
    return true

func replace(key: String, value: Variant) -> bool:
    if not _values.has(key):
        return false
    _values[key] = value
    return true

func remove(key: String) -> bool:
    if not _values.has(key):
        return false
    _values.erase(key)
    _keys.erase(key)
    return true

func contains(key: String) -> bool:
    return _values.has(key)

func get_value(key: String, default_value: Variant = null) -> Variant:
    return _values.get(key, default_value)

func values() -> Array:
    var result: Array = []
    for key in _keys:
        result.append(_values[key])
    return result

func size() -> int:
    return _keys.size()
