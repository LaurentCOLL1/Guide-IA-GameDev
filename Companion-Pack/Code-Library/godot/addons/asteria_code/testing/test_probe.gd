extends RefCounted
class_name TestProbe

var events: Array[Dictionary] = []

func record(name: String, payload: Variant = null) -> void:
    events.append({"name": name, "payload": payload})

func count(name: String = "") -> int:
    if name.is_empty():
        return events.size()
    var total := 0
    for event in events:
        if event.name == name:
            total += 1
    return total

func last(name: String = "") -> Dictionary:
    for index in range(events.size() - 1, -1, -1):
        var event: Dictionary = events[index]
        if name.is_empty() or event.name == name:
            return event.duplicate(true)
    return {}

func clear() -> void:
    events.clear()
