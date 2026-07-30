class_name BenchmarkCore
extends RefCounted

static func arg_value(name: String, fallback: String) -> String:
    var args := OS.get_cmdline_user_args()
    for index in range(args.size() - 1):
        if args[index] == name:
            return args[index + 1]
    return fallback

static func percentile(values: Array[float], quantile: float) -> float:
    var data := values.duplicate()
    data.sort()
    if data.is_empty():
        return 0.0
    if data.size() == 1:
        return data[0]
    var position := float(data.size() - 1) * quantile
    var lower := int(floor(position))
    var upper := int(ceil(position))
    if lower == upper:
        return data[lower]
    var fraction := position - float(lower)
    return data[lower] + (data[upper] - data[lower]) * fraction

static func summarize(values: Array[float]) -> Dictionary:
    var total := 0.0
    for value in values:
        total += value
    var mean := total / float(values.size())
    var variance := 0.0
    if values.size() > 1:
        for value in values:
            variance += pow(value - mean, 2.0)
        variance /= float(values.size() - 1)
    var sorted_values := values.duplicate()
    sorted_values.sort()
    var median := percentile(sorted_values, 0.5)
    var stdev := sqrt(variance)
    return {
        "count": values.size(), "min": sorted_values[0], "max": sorted_values[-1],
        "mean": mean, "median": median, "variance": variance, "stdev": stdev,
        "coefficient_of_variation": stdev / mean if mean != 0.0 else 0.0,
        "p95": percentile(sorted_values, 0.95), "p99": percentile(sorted_values, 0.99)
    }

static func environment(extra: Dictionary = {}) -> Dictionary:
    var result := {
        "os": OS.get_name(),
        "os_release": OS.get_version(),
        "architecture": Engine.get_architecture_name(),
        "runtime": "Godot %s" % Engine.get_version_info().get("string", "unknown"),
        "cpu_model": OS.get_processor_name(),
        "logical_cpu_count": OS.get_processor_count(),
        "renderer": str(ProjectSettings.get_setting("rendering/renderer/rendering_method", "unknown")),
        "adapter": RenderingServer.get_video_adapter_name(),
        "environment_id": OS.get_environment("BENCH_ENVIRONMENT_ID")
    }
    for key in extra:
        result[key] = extra[key]
    return result

static func timestamp_utc() -> String:
    return Time.get_datetime_string_from_system(true, false) + "Z"

static func write_result(path: String, value: Dictionary) -> bool:
    var file := FileAccess.open(path, FileAccess.WRITE)
    if file == null:
        push_error("Unable to open output: " + path)
        return false
    file.store_string(JSON.stringify(value, "  ") + "\n")
    file.close()
    return true
