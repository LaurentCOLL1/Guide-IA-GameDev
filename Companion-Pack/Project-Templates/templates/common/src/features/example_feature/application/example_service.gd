class_name ExampleService
extends RefCounted

var _repository: InMemoryExampleRepository

func _init(repository: InMemoryExampleRepository) -> void:
	assert(repository != null)
	_repository = repository

func create_record(record_id: StringName, label: String) -> bool:
	var candidate := ExampleRecord.new(record_id, label)
	if not candidate.is_valid():
		return false
	return _repository.add(candidate)
