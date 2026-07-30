class_name BootstrapReport
extends RefCounted

const SCHEMA_VERSION: int = 1

var validation_id: StringName
var project_id: StringName
var profile_id: StringName
var engine_version: String
var renderer: StringName
var checks: Dictionary


func _init(
    initial_validation_id: StringName,
    initial_project_id: StringName,
    initial_profile_id: StringName,
    initial_engine_version: String,
    initial_renderer: StringName,
    initial_checks: Dictionary
) -> void:
    validation_id = initial_validation_id
    project_id = initial_project_id
    profile_id = initial_profile_id
    engine_version = initial_engine_version
    renderer = initial_renderer
    checks = initial_checks.duplicate(true)


func is_valid() -> bool:
    if validation_id.is_empty() or project_id.is_empty() or profile_id.is_empty():
        return false
    if engine_version.is_empty() or renderer.is_empty():
        return false
    for value: Variant in checks.values():
        if not value is bool or value == false:
            return false
    return true


func to_dictionary() -> Dictionary:
    return {
        "schema_version": SCHEMA_VERSION,
        "validation_id": String(validation_id),
        "project_id": String(project_id),
        "profile_id": String(profile_id),
        "engine_version": engine_version,
        "renderer": String(renderer),
        "checks": checks.duplicate(true),
        "valid": is_valid(),
    }
