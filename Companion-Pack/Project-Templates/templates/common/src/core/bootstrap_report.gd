class_name TemplateBootstrapReport
extends RefCounted

const SCHEMA_VERSION: int = 1

static func build(profile_id: StringName, project_id: StringName) -> Dictionary:
	return {
		"schema_version": SCHEMA_VERSION,
		"validation_id": "CP-PT-BOOTSTRAP-001",
		"project_id": String(project_id),
		"profile_id": String(profile_id),
		"engine_version": Engine.get_version_info().get("string", "unknown"),
		"checks": {
			"main_scene_loaded": true,
			"profile_declared": not profile_id.is_empty(),
			"project_id_declared": not project_id.is_empty()
		}
	}

static func is_valid(report: Dictionary) -> bool:
	if int(report.get("schema_version", 0)) != SCHEMA_VERSION:
		return false
	if String(report.get("validation_id", "")) != "CP-PT-BOOTSTRAP-001":
		return false
	var checks: Dictionary = report.get("checks", {})
	return (
		bool(checks.get("main_scene_loaded", false))
		and bool(checks.get("profile_declared", false))
		and bool(checks.get("project_id_declared", false))
	)
