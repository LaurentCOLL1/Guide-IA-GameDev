extends RefCounted
class_name InteractionRouter

var _handlers: Dictionary = {}

func register(action: String, handler: Callable, replace: bool = false) -> bool:
    if action.is_empty() or not handler.is_valid():
        return false
    if _handlers.has(action) and not replace:
        return false
    _handlers[action] = handler
    return true

func contains(action: String) -> bool:
    return _handlers.has(action)

func dispatch(action: String, context: Variant = null) -> Dictionary:
    if not _handlers.has(action):
        return {"ok": false, "value": null, "error_code": "unknown_action"}
    var value: Variant = (_handlers[action] as Callable).call(context)
    return {"ok": true, "value": value, "error_code": ""}
