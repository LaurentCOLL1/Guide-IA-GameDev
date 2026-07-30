extends RefCounted
class_name InMemoryRepository

var _rows: Dictionary = {}

func _copy(value: Variant) -> Variant:
    if value is Dictionary or value is Array:
        return value.duplicate(true)
    return value

func save(entity_id: String, entity: Variant) -> bool:
    if entity_id.is_empty():
        return false
    _rows[entity_id] = _copy(entity)
    return true

func get_by_id(entity_id: String, default_value: Variant = null) -> Variant:
    if not _rows.has(entity_id):
        return default_value
    return _copy(_rows[entity_id])

func contains(entity_id: String) -> bool:
    return _rows.has(entity_id)

func remove(entity_id: String) -> bool:
    return _rows.erase(entity_id)

func list_ids() -> Array:
    var result: Array = _rows.keys()
    result.sort()
    return result

func clear() -> void:
    _rows.clear()

func count() -> int:
    return _rows.size()
