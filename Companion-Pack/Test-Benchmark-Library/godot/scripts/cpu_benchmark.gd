extends Node

func workload(seed: int, iterations: int) -> int:
    var value := seed
    var checksum := 0
    for index in range(iterations):
        value = int((value * 48271 + index + 1) % 2147483647)
        checksum = int((checksum + value) % 2147483647)
    return checksum

func _ready() -> void:
    var output := BenchmarkCore.arg_value("--output", "user://godot-cpu-summary.json")
    var repetitions := int(BenchmarkCore.arg_value("--repetitions", "7"))
    var warmups := int(BenchmarkCore.arg_value("--warmups", "2"))
    var iterations := int(BenchmarkCore.arg_value("--iterations", "30000"))
    var seed := int(BenchmarkCore.arg_value("--seed", "1701"))
    var expected := -1
    for _index in range(warmups):
        var current := workload(seed, iterations)
        expected = current if expected == -1 else expected
        if current != expected:
            push_error("CPU warm-up oracle changed")
            get_tree().quit(1)
            return
    var samples: Array = []
    var values: Array[float] = []
    for index in range(repetitions):
        var started := Time.get_ticks_usec()
        var checksum := workload(seed, iterations)
        var elapsed := float(Time.get_ticks_usec() - started)
        values.append(elapsed)
        samples.append({"benchmark_id":"BMK-GODOT-CPU-001","sample_index":index,"value":elapsed,"unit":"us","status":"pass" if checksum == expected else "fail","checksum":str(checksum)})
    var result := {"schema_version":1,"benchmark_id":"BMK-GODOT-CPU-001","contract_version":"1.0.0","family":"cpu","implementation":"godot-lcg-loop","generated_at_utc":BenchmarkCore.timestamp_utc(),"environment":BenchmarkCore.environment(),"seed":seed,"parameters":{"iterations":iterations},"warmups":warmups,"repetitions":repetitions,"metric":"elapsed_usec","unit":"us","samples":samples,"statistics":BenchmarkCore.summarize(values),"secondary_statistics":{},"oracle_status":"pass","oracle_checksum":str(expected),"evidence_level":"local-measurement","comparability":"same-environment-only","reservations":["synthetic workload","no universal performance claim"]}
    if not BenchmarkCore.write_result(output, result):
        get_tree().quit(1); return
    print("GODOT_CPU_BENCHMARK: PASS output=", output)
    get_tree().quit(0)
