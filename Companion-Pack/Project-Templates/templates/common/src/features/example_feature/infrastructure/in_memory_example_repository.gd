class_name InMemoryExampleRepository
extends RefCounted

var _records: Dictionary = {}

func add(record: ExampleRecord) -> bool:
	if record == null or not record.is_valid() or _records.has(record.record_id):
		return false
	_records[record.record_id] = record
	return true

func has(record_id: StringName) -> bool:
	return _records.has(record_id)
