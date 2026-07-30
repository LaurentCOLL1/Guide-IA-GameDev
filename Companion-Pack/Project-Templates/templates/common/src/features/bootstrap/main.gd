extends Node3D

const PROFILE_ID: StringName = &"__PROFILE_ID__"
const PROJECT_ID: StringName = &"__PROJECT_ID__"

func _ready() -> void:
	var report := TemplateBootstrapReport.build(PROFILE_ID, PROJECT_ID)
	if not TemplateBootstrapReport.is_valid(report):
		push_error("CP-PT-BOOTSTRAP-001: rapport invalide")
		get_tree().quit(1)
		return
	print("CP-PT-BOOTSTRAP-001 %s" % JSON.stringify(report))
