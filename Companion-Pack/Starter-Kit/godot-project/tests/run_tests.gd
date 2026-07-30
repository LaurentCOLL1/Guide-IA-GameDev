extends SceneTree

const MAIN_SCENE := preload("res://src/features/bootstrap/main.tscn")
const EXPECTED_VALIDATION_ID: String = "CP-SK-BOOTSTRAP-001"
const EXPECTED_PROJECT_ID: String = "project-asteria"

var failures: Array[String] = []


func _initialize() -> void:
    call_deferred("_run")


func _assert_true(condition: bool, message: String) -> void:
    if not condition:
        failures.append(message)


func _run() -> void:
    var instance: Node = MAIN_SCENE.instantiate()
    root.add_child(instance)
    await process_frame

    _assert_true(instance is Node3D, "La scène principale doit instancier un Node3D.")
    _assert_true(instance.has_method("get_bootstrap_report"), "Le bootstrap doit exposer get_bootstrap_report().")

    var report: Variant = null
    if instance.has_method("get_bootstrap_report"):
        report = instance.call("get_bootstrap_report")

    _assert_true(report != null, "BootstrapReport doit être créé dans _ready().")
    if report != null and report.has_method("to_dictionary"):
        var payload: Dictionary = report.call("to_dictionary")
        _assert_true(payload.get("schema_version") == 1, "schema_version doit valoir 1.")
        _assert_true(payload.get("validation_id") == EXPECTED_VALIDATION_ID, "validation_id inattendu.")
        _assert_true(payload.get("project_id") == EXPECTED_PROJECT_ID, "project_id inattendu.")
        _assert_true(payload.get("profile_id") == "solo", "Le profil par défaut doit être solo.")
        _assert_true(payload.get("renderer") == "forward_plus", "Le rendu de référence doit être Forward+.")
        _assert_true(payload.get("valid") == true, "BootstrapReport doit être valide.")
        var checks: Dictionary = payload.get("checks", {})
        _assert_true(checks.get("local_ai_optional") == true, "L'IA locale doit rester facultative.")
        _assert_true(checks.get("persistent_state_untouched") == true, "Le bootstrap ne doit pas muter d'état persistant.")
    else:
        failures.append("BootstrapReport doit exposer to_dictionary().")

    instance.queue_free()
    await process_frame

    if failures.is_empty():
        print("STARTER_KIT_TESTS: PASS")
        quit(0)
        return

    for failure: String in failures:
        push_error("STARTER_KIT_TESTS: %s" % failure)
    print("STARTER_KIT_TESTS: FAIL (%d)" % failures.size())
    quit(1)
