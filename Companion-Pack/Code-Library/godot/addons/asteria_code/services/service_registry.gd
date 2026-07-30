extends RefCounted
class_name ServiceRegistry

var _services: Dictionary = {}

func register(service_id: String, service: Variant, replace: bool = false) -> bool:
    if service_id.is_empty():
        return false
    if _services.has(service_id) and not replace:
        return false
    _services[service_id] = service
    return true

func resolve(service_id: String, default_value: Variant = null) -> Variant:
    return _services.get(service_id, default_value)

func contains(service_id: String) -> bool:
    return _services.has(service_id)

func remove(service_id: String) -> bool:
    return _services.erase(service_id)

func ids() -> Array:
    var result: Array = _services.keys()
    result.sort()
    return result
