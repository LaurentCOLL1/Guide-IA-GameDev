class_name ProjectComposition
extends RefCounted

static func build_example_service() -> ExampleService:
	var repository := InMemoryExampleRepository.new()
	return ExampleService.new(repository)
