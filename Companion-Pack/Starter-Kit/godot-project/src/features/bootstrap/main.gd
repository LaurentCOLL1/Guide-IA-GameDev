class_name AsteriaBootstrap
extends Node3D

const BootstrapReportType := preload("res://src/core/bootstrap_report.gd")
const VALIDATION_ID: StringName = &"CP-SK-BOOTSTRAP-001"
const PROJECT_ID: StringName = &"project-asteria"
const ROTATION_SPEED: float = 0.5

@export_enum("solo", "studio") var environment_profile: String = "solo"
@onready var marker: MeshInstance3D = $Marker

var _report: BootstrapReport


func _ready() -> void:
    var version_info: Dictionary = Engine.get_version_info()
    _report = BootstrapReportType.new(
        VALIDATION_ID,
        PROJECT_ID,
        StringName(environment_profile),
        str(version_info.get("string", "unknown")),
        &"forward_plus",
        {
            "main_scene_loaded": true,
            "marker_available": is_instance_valid(marker),
            "local_ai_optional": true,
            "persistent_state_untouched": true,
        }
    )
    print("%s %s" % [VALIDATION_ID, JSON.stringify(_report.to_dictionary())])


func _process(delta: float) -> void:
    if is_instance_valid(marker):
        marker.rotate_y(ROTATION_SPEED * delta)


func get_bootstrap_report() -> BootstrapReport:
    return _report
