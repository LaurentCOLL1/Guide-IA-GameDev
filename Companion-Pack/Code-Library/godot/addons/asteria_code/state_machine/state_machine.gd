extends RefCounted
class_name StateMachine

var current_state: String
var _transitions: Dictionary = {}

func _init(initial_state: String) -> void:
    current_state = initial_state

func add_transition(source: String, event: String, target: String, replace: bool = false) -> bool:
    var key := source + "" + event
    if _transitions.has(key) and not replace:
        return false
    _transitions[key] = target
    return true

func can_trigger(event: String) -> bool:
    return _transitions.has(current_state + "" + event)

func trigger(event: String) -> Dictionary:
    var key := current_state + "" + event
    if not _transitions.has(key):
        return {"ok": false, "source": current_state, "event": event, "target": current_state}
    var source := current_state
    current_state = str(_transitions[key])
    return {"ok": true, "source": source, "event": event, "target": current_state}
