class_name BlendShapeDriver
extends RefCounted

# Naming contract for Blender shape keys exported through GLB.
# Each signed editor value drives a positive or negative target independently.
const SIGNED_TARGETS := {
	"stature": ["morph_stature_neg", "morph_stature_pos"],
	"head_scale": ["morph_head_small", "morph_head_large"],
	"shoulder_width": ["morph_shoulders_narrow", "morph_shoulders_wide"],
	"chest_volume": ["morph_chest_small", "morph_chest_large"],
	"waist_width": ["morph_waist_narrow", "morph_waist_wide"],
	"hip_width": ["morph_hips_narrow", "morph_hips_wide"],
	"torso_length": ["morph_torso_short", "morph_torso_long"],
	"arm_length": ["morph_arms_short", "morph_arms_long"],
	"leg_length": ["morph_legs_short", "morph_legs_long"],
	"muscle_mass": ["morph_muscle_low", "morph_muscle_high"],
	"adipose_mass": ["morph_adipose_low", "morph_adipose_high"],
	"hand_scale": ["morph_hands_small", "morph_hands_large"],
	"foot_scale": ["morph_feet_small", "morph_feet_large"],
	"jaw_width": ["morph_jaw_narrow", "morph_jaw_wide"],
	"nose_scale": ["morph_nose_small", "morph_nose_large"],
	"eye_spacing": ["morph_eyes_close", "morph_eyes_wide"]
}

const AGE_TARGETS := {
	"infant": "age_infant",
	"early_childhood": "age_early_childhood",
	"childhood": "age_childhood",
	"adolescence": "age_adolescence",
	"young_adult": "age_young_adult",
	"mature_adult": "age_mature_adult",
	"elder": "age_elder"
}

static func build_index(mesh_instance: MeshInstance3D) -> Dictionary:
	var result := {}
	if mesh_instance == null or mesh_instance.mesh == null:
		return result
	for index in range(mesh_instance.mesh.get_blend_shape_count()):
		result[str(mesh_instance.mesh.get_blend_shape_name(index))] = index
	return result

static func validate_contract(mesh_instance: MeshInstance3D) -> PackedStringArray:
	var index := build_index(mesh_instance)
	var missing := PackedStringArray()
	for pair in SIGNED_TARGETS.values():
		for target_name in pair:
			if not index.has(target_name):
				missing.append(target_name)
	for target_name in AGE_TARGETS.values():
		if not index.has(target_name):
			missing.append(target_name)
	return missing

static func apply(mesh_instance: MeshInstance3D, definition: CharacterDefinition) -> void:
	if mesh_instance == null or mesh_instance.mesh == null:
		return
	definition.clamp_morphology()
	var index := build_index(mesh_instance)

	for property_name in SIGNED_TARGETS.keys():
		var pair: Array = SIGNED_TARGETS[property_name]
		var value := clampf(float(definition.get(property_name)), -1.0, 1.0)
		_set_target(mesh_instance, index, pair[0], maxf(-value, 0.0))
		_set_target(mesh_instance, index, pair[1], maxf(value, 0.0))

	for stage in AGE_TARGETS.keys():
		_set_target(mesh_instance, index, AGE_TARGETS[stage], 1.0 if stage == definition.life_stage() else 0.0)

static func _set_target(mesh_instance: MeshInstance3D, index: Dictionary, target_name: String, value: float) -> void:
	if index.has(target_name):
		mesh_instance.set_blend_shape_value(int(index[target_name]), clampf(value, 0.0, 1.0))
