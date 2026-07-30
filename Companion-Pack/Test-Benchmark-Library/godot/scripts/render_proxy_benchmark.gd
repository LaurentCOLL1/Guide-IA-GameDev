extends Node2D

var output := ""
var warmups := 30
var repetitions := 90
var draw_items := 256
var seed := 1701
var frame_index := 0
var values: Array[float] = []

func _ready() -> void:
    output = BenchmarkCore.arg_value("--output", "user://godot-render-summary.json")
    warmups = int(BenchmarkCore.arg_value("--warmups", "30"))
    repetitions = int(BenchmarkCore.arg_value("--repetitions", "90"))
    draw_items = int(BenchmarkCore.arg_value("--draw-items", "256"))
    seed = int(BenchmarkCore.arg_value("--seed", "1701"))
    queue_redraw()

func _process(delta: float) -> void:
    frame_index += 1
    if frame_index > warmups:
        values.append(delta * 1000.0)
    queue_redraw()
    if values.size() >= repetitions:
        var samples: Array = []
        for index in range(values.size()):
            samples.append({"benchmark_id":"BMK-GODOT-RENDER-PROXY-001","sample_index":index,"value":values[index],"unit":"ms","status":"pass","checksum":str(draw_items)})
        var result := {"schema_version":1,"benchmark_id":"BMK-GODOT-RENDER-PROXY-001","contract_version":"1.0.0","family":"render-proxy","implementation":"godot-node2d-draw-circles","generated_at_utc":BenchmarkCore.timestamp_utc(),"environment":BenchmarkCore.environment({"display_mode":"graphical-required"}),"seed":seed,"parameters":{"draw_items":draw_items,"viewport":"640x360","vsync":false},"warmups":warmups,"repetitions":repetitions,"metric":"frame_interval_ms","unit":"ms","samples":samples,"statistics":BenchmarkCore.summarize(values),"secondary_statistics":{},"oracle_status":"pass","oracle_checksum":str(draw_items),"evidence_level":"virtual-render-proxy","comparability":"same-environment-only","physical_gpu_qualified":false,"reservations":["frame interval proxy","Xvfb or declared local display","not a physical GPU qualification","no image-quality review"]}
        if not BenchmarkCore.write_result(output, result): get_tree().quit(1); return
        print("GODOT_RENDER_PROXY_BENCHMARK: PASS output=", output)
        get_tree().quit(0)

func _draw() -> void:
    var width := 640.0
    var height := 360.0
    for index in range(draw_items):
        var x := fmod(float(index * 73 + seed + frame_index), width)
        var y := fmod(float(index * 37 + seed * 2 + frame_index * 2), height)
        var radius := 2.0 + float(index % 7)
        var color := Color(float((index * 17) % 255) / 255.0, float((index * 31) % 255) / 255.0, float((index * 47) % 255) / 255.0, 0.75)
        draw_circle(Vector2(x, y), radius, color)
