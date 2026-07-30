extends Node

func workload(seed: int, items: int) -> int:
    var values := PackedInt64Array()
    values.resize(items)
    var checksum := 0
    for index in range(items):
        values[index] = int((index * 48271 + seed) % 2147483647)
    var stride := maxi(1, int(items / 1024))
    for index in range(0, items, stride):
        checksum = int((checksum + values[index]) % 2147483647)
    values.clear()
    return checksum

func _ready() -> void:
    var output := BenchmarkCore.arg_value("--output", "user://godot-memory-summary.json")
    var repetitions := int(BenchmarkCore.arg_value("--repetitions", "7"))
    var warmups := int(BenchmarkCore.arg_value("--warmups", "2"))
    var items := int(BenchmarkCore.arg_value("--items", "50000"))
    var seed := int(BenchmarkCore.arg_value("--seed", "1701"))
    var expected := -1
    for _index in range(warmups):
        var current := workload(seed, items)
        expected = current if expected == -1 else expected
        if current != expected:
            push_error("Memory warm-up oracle changed"); get_tree().quit(1); return
    var samples: Array = []
    var values: Array[float] = []
    var memory_values: Array[float] = []
    for index in range(repetitions):
        var before := OS.get_static_memory_usage()
        var started := Time.get_ticks_usec()
        var checksum := workload(seed, items)
        var elapsed := float(Time.get_ticks_usec() - started)
        var delta := float(maxi(0, OS.get_static_memory_usage() - before))
        values.append(elapsed); memory_values.append(delta)
        samples.append({"benchmark_id":"BMK-GODOT-MEM-001","sample_index":index,"value":elapsed,"unit":"us","status":"pass" if checksum == expected else "fail","checksum":str(checksum),"secondary_value":delta,"secondary_unit":"static_memory_delta_bytes"})
    var result := {"schema_version":1,"benchmark_id":"BMK-GODOT-MEM-001","contract_version":"1.0.0","family":"memory","implementation":"godot-packed-int64-array","generated_at_utc":BenchmarkCore.timestamp_utc(),"environment":BenchmarkCore.environment(),"seed":seed,"parameters":{"items":items},"warmups":warmups,"repetitions":repetitions,"metric":"elapsed_usec","unit":"us","samples":samples,"statistics":BenchmarkCore.summarize(values),"secondary_statistics":{"static_memory_delta_bytes":BenchmarkCore.summarize(memory_values)},"oracle_status":"pass","oracle_checksum":str(expected),"evidence_level":"local-measurement","comparability":"same-environment-only","reservations":["allocator and engine state dependent","no universal performance claim"]}
    if not BenchmarkCore.write_result(output, result): get_tree().quit(1); return
    print("GODOT_MEMORY_BENCHMARK: PASS output=", output)
    get_tree().quit(0)
