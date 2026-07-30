extends SceneTree

var failures: Array[String] = []

func expect(condition: bool, message: String) -> void:
    if not condition:
        failures.append(message)

func _initialize() -> void:
    test_collections()
    test_validation()
    test_serialization()
    test_services_repository()
    test_state_interaction()
    test_conversions_probe()
    if failures.is_empty():
        print("CODE_LIBRARY_GODOT_TESTS: PASS")
        quit(0)
        return
    for failure in failures:
        push_error(failure)
    print("CODE_LIBRARY_GODOT_TESTS: FAIL count=", failures.size())
    quit(1)

func test_collections() -> void:
    var values := StableUniqueList.new()
    expect(values.add("a", 1), "collection add")
    expect(not values.add("a", 2), "collection duplicate")
    expect(values.add("b", 2), "collection second")
    expect(values.values() == [1, 2], "collection order")

func test_validation() -> void:
    var validator := Validator.new()
    validator.add_rule(func(value: Variant) -> Variant:
        return ValidationIssue.new("empty", "required") if str(value).is_empty() else null
    )
    expect(not validator.validate("").is_valid(), "validation error")
    expect(validator.validate("ok").is_valid(), "validation success")

func test_serialization() -> void:
    expect(CanonicalJson.encode({"z": 1, "a": 2}) == '{"a":2,"z":1}', "canonical json")

func test_services_repository() -> void:
    var registry := ServiceRegistry.new()
    expect(registry.register("answer", 42), "service register")
    expect(registry.resolve("answer") == 42, "service resolve")
    var repository := InMemoryRepository.new()
    var source := {"items": [1]}
    repository.save("x", source)
    source.items.append(2)
    expect(repository.get_by_id("x") == {"items": [1]}, "repository defensive copy")

func test_state_interaction() -> void:
    var machine := StateMachine.new("idle")
    machine.add_transition("idle", "start", "active")
    expect(machine.trigger("start").target == "active", "state transition")
    var router := InteractionRouter.new()
    router.register("double", func(value: Variant) -> Variant: return int(value) * 2)
    expect(router.dispatch("double", 4).value == 8, "interaction result")
    expect(router.dispatch("missing").error_code == "unknown_action", "interaction missing")

func test_conversions_probe() -> void:
    expect(ValueConversions.seconds_to_milliseconds(1.25) == 1250, "seconds conversion")
    expect(ValueConversions.parse_bool("yes") == true, "bool conversion")
    var probe := TestProbe.new()
    probe.record("hit", {"damage": 2})
    expect(probe.count("hit") == 1, "probe count")
    expect(probe.last("hit").payload.damage == 2, "probe last")
