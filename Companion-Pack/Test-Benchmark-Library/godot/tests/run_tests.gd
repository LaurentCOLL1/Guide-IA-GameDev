extends SceneTree

var failures: Array[String] = []

func expect(condition: bool, message: String) -> void:
    if not condition: failures.append(message)

func _initialize() -> void:
    test_percentile()
    test_summary()
    test_arguments()
    test_cpu_oracle()
    test_memory_oracle()
    if failures.is_empty():
        print("TEST_BENCHMARK_LIBRARY_GODOT_TESTS: PASS")
        quit(0); return
    for failure in failures: push_error(failure)
    print("TEST_BENCHMARK_LIBRARY_GODOT_TESTS: FAIL count=", failures.size())
    quit(1)

func test_percentile() -> void:
    expect(is_equal_approx(BenchmarkCore.percentile([0.0, 10.0], 0.5), 5.0), "percentile interpolation")

func test_summary() -> void:
    var result := BenchmarkCore.summarize([1.0, 2.0, 3.0, 4.0])
    expect(result.count == 4, "summary count")
    expect(result.has("variance"), "summary variance")
    expect(result.has("p95"), "summary p95")

func test_arguments() -> void:
    expect(BenchmarkCore.arg_value("--not-present", "fallback") == "fallback", "argument fallback")

func test_cpu_oracle() -> void:
    var value := 1701
    var checksum := 0
    for index in range(10):
        value = int((value * 48271 + index + 1) % 2147483647)
        checksum = int((checksum + value) % 2147483647)
    expect(checksum == 1838391017, "cpu oracle")

func test_memory_oracle() -> void:
    var values := PackedInt64Array([1, 2, 3])
    expect(values.size() == 3 and values[2] == 3, "packed array")
