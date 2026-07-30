extends SceneTree

var failures: Array[String] = []

func _initialize() -> void:
	_test_bootstrap_report()
	_test_example_feature()
	_test_generated_modules()
	if failures.is_empty():
		print("PROJECT_TEMPLATE_TESTS: PASS")
		quit(0)
		return
	for failure in failures:
		push_error(failure)
	print("PROJECT_TEMPLATE_TESTS: FAIL %d" % failures.size())
	quit(1)

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _test_bootstrap_report() -> void:
	var report := TemplateBootstrapReport.build(&"__PROFILE_ID__", &"__PROJECT_ID__")
	_expect(TemplateBootstrapReport.is_valid(report), "bootstrap report should be valid")

func _test_example_feature() -> void:
	var service := ProjectComposition.build_example_service()
	_expect(service.create_record(&"example-1", "Premier"), "first record should be accepted")
	_expect(not service.create_record(&"example-1", "Duplicate"), "duplicate should be rejected")
	_expect(not service.create_record(&"", ""), "invalid record should be rejected")

func _test_generated_modules() -> void:
	var file := FileAccess.open("res://modules.json", FileAccess.READ)
	_expect(file != null, "modules.json should be readable")
	if file == null:
		return
	var parsed: Variant = JSON.parse_string(file.get_as_text())
	_expect(parsed is Dictionary, "modules.json should contain a dictionary")
	if parsed is not Dictionary:
		return
	for module: Dictionary in parsed.get("modules", []):
		var test_path := String(module.get("test_script", ""))
		if test_path.is_empty():
			continue
		var test_script: Script = load(test_path)
		_expect(test_script != null, "module test script should load: %s" % test_path)
		if test_script == null:
			continue
		var test_instance: RefCounted = test_script.new()
		_expect(bool(test_instance.call("run")), "module test should pass: %s" % test_path)
