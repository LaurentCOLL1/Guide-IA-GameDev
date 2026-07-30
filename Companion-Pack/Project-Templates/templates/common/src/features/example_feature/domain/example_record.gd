class_name ExampleRecord
extends RefCounted

var record_id: StringName
var label: String

func _init(p_record_id: StringName, p_label: String) -> void:
	record_id = p_record_id
	label = p_label

func is_valid() -> bool:
	return not record_id.is_empty() and not label.strip_edges().is_empty()
