class_name ProceduralAvatar
extends Node3D

var definition: CharacterDefinition = CharacterDefinition.new()
var _skin_material: StandardMaterial3D
var _garment_material: StandardMaterial3D
var _eye_material: StandardMaterial3D
var _iris_material: StandardMaterial3D

func _ready() -> void:
	rebuild()

func apply_definition(value: CharacterDefinition) -> void:
	definition = value
	rebuild()

func rebuild() -> void:
	for child in get_children():
		remove_child(child)
		child.queue_free()

	definition.clamp_morphology()
	_prepare_materials()
	var d := MorphologyRules.dimensions(definition)

	var head_radius: float = d["head_radius"]
	var neck_height: float = d["neck_height"]
	var torso_height: float = d["torso_height"]
	var leg_height: float = d["leg_height"]
	var arm_height: float = d["arm_height"]
	var shoulder_half: float = d["shoulder_half"]
	var hip_half: float = d["hip_half"]
	var chest_depth: float = d["chest_depth"]
	var waist_depth: float = d["waist_depth"]
	var limb_radius: float = d["limb_radius"]
	var hand_size: float = d["hand_scale"]
	var foot_size: float = d["foot_scale"]
	var child_roundness: float = d["child_roundness"]
	var elder_factor: float = d["elder_factor"]

	var foot_height := maxf(0.035, foot_size * 0.32)
	var ankle_y := foot_height + leg_height * 0.03
	var hip_y := ankle_y + leg_height
	var shoulder_y := hip_y + torso_height * 0.82
	var neck_y := hip_y + torso_height + neck_height * 0.5
	var head_y := hip_y + torso_height + neck_height + head_radius * 0.98

	_add_box("Pelvis", Vector3(hip_half * 1.72, torso_height * 0.22, waist_depth * 1.35), Vector3(0.0, hip_y + torso_height * 0.10, 0.0), _skin_material)
	_add_capsule("Abdomen", maxf(waist_depth * 0.85, 0.045), torso_height * 0.44, Vector3(0.0, hip_y + torso_height * 0.35, 0.0), _skin_material, Vector3(1.0 + definition.waist_width * 0.15, 1.0, 0.92))
	_add_capsule("Chest", maxf(chest_depth, 0.05), torso_height * 0.50, Vector3(0.0, hip_y + torso_height * 0.67, 0.0), _skin_material, Vector3(shoulder_half / maxf(chest_depth, 0.001), 1.0, 1.0))

	for side in [-1.0, 1.0]:
		var leg_x := side * hip_half * 0.52
		_add_capsule("Leg", limb_radius * 1.12, leg_height, Vector3(leg_x, ankle_y + leg_height * 0.5, 0.0), _skin_material, Vector3(1.0, 1.0, 1.0 + definition.adipose_mass * 0.05))
		_add_box("Foot", Vector3(foot_size * 0.70, foot_height, foot_size * 1.45), Vector3(leg_x, foot_height * 0.5, foot_size * 0.20), _skin_material)

	for side in [-1.0, 1.0]:
		var arm_x := side * (shoulder_half + limb_radius * 1.10)
		var arm_center_y := shoulder_y - arm_height * 0.48
		_add_capsule("Arm", limb_radius, arm_height, Vector3(arm_x, arm_center_y, 0.0), _skin_material)
		_add_capsule("Hand", maxf(hand_size * 0.31, 0.025), hand_size * 1.15, Vector3(arm_x, shoulder_y - arm_height - hand_size * 0.42, 0.0), _skin_material, Vector3(0.88, 1.0, 0.58))

	_add_capsule("Neck", maxf(head_radius * 0.36, 0.035), neck_height, Vector3(0.0, neck_y, 0.0), _skin_material)
	var head_scale_x := 0.88 + definition.jaw_width * 0.10 + child_roundness * 0.04
	var head_scale_y := 1.08 - elder_factor * 0.015
	var head_scale_z := 0.92 + definition.head_scale * 0.03
	_add_sphere("Head", head_radius, Vector3(0.0, head_y, 0.0), _skin_material, Vector3(head_scale_x, head_scale_y, head_scale_z))
	_add_face(head_y, head_radius, head_scale_x)

	if definition.privacy_garment_enabled or definition.is_minor():
		_add_box("PrivacyGarment", Vector3(hip_half * 1.86, torso_height * 0.19, waist_depth * 1.52), Vector3(0.0, hip_y + torso_height * 0.075, 0.0), _garment_material)

	var anatomy_slot := Node3D.new()
	anatomy_slot.name = "AdultAnatomySlot"
	anatomy_slot.position = Vector3(0.0, hip_y + torso_height * 0.03, waist_depth * 0.55)
	anatomy_slot.set_meta("profile", definition.adult_anatomy_profile)
	anatomy_slot.set_meta("enabled", not definition.is_minor())
	add_child(anatomy_slot)

	rotation.x = deg_to_rad(-elder_factor * 3.0)

func _prepare_materials() -> void:
	_skin_material = StandardMaterial3D.new()
	_skin_material.albedo_color = MorphologyRules.skin_color(definition.skin_pigment)
	_skin_material.roughness = definition.skin_roughness
	_skin_material.metallic = 0.0

	_garment_material = StandardMaterial3D.new()
	_garment_material.albedo_color = Color(0.12, 0.15, 0.20)
	_garment_material.roughness = 0.78

	_eye_material = StandardMaterial3D.new()
	_eye_material.albedo_color = Color(0.93, 0.94, 0.92)
	_eye_material.roughness = 0.22

	_iris_material = StandardMaterial3D.new()
	_iris_material.albedo_color = Color(0.18, 0.31, 0.36)
	_iris_material.roughness = 0.18

func _add_face(head_y: float, head_radius: float, head_scale_x: float) -> void:
	var spacing := head_radius * (0.32 + definition.eye_spacing * 0.055) * head_scale_x
	var eye_y := head_y + head_radius * 0.16
	var eye_z := head_radius * 0.82
	for side in [-1.0, 1.0]:
		_add_sphere("Eye", head_radius * 0.105, Vector3(side * spacing, eye_y, eye_z), _eye_material, Vector3(1.0, 0.78, 0.48))
		_add_sphere("Iris", head_radius * 0.052, Vector3(side * spacing, eye_y, eye_z + head_radius * 0.052), _iris_material, Vector3(1.0, 1.0, 0.42))
	var nose_size := head_radius * (0.16 + definition.nose_scale * 0.045)
	_add_capsule("Nose", nose_size * 0.42, nose_size, Vector3(0.0, head_y - head_radius * 0.02, head_radius * 0.94), _skin_material, Vector3(0.72, 1.0, 0.68))

func _add_capsule(part_name: String, radius: float, height: float, position_value: Vector3, material: Material, scale_value: Vector3 = Vector3.ONE) -> MeshInstance3D:
	var mesh := CapsuleMesh.new()
	mesh.radius = maxf(radius, 0.005)
	mesh.height = maxf(height, mesh.radius * 2.05)
	mesh.radial_segments = 24
	mesh.rings = 12
	var instance := MeshInstance3D.new()
	instance.name = part_name
	instance.mesh = mesh
	instance.position = position_value
	instance.scale = scale_value
	instance.material_override = material
	instance.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_ON
	add_child(instance)
	return instance

func _add_sphere(part_name: String, radius: float, position_value: Vector3, material: Material, scale_value: Vector3 = Vector3.ONE) -> MeshInstance3D:
	var mesh := SphereMesh.new()
	mesh.radius = maxf(radius, 0.005)
	mesh.height = maxf(radius * 2.0, 0.01)
	mesh.radial_segments = 32
	mesh.rings = 18
	var instance := MeshInstance3D.new()
	instance.name = part_name
	instance.mesh = mesh
	instance.position = position_value
	instance.scale = scale_value
	instance.material_override = material
	instance.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_ON
	add_child(instance)
	return instance

func _add_box(part_name: String, size_value: Vector3, position_value: Vector3, material: Material) -> MeshInstance3D:
	var mesh := BoxMesh.new()
	mesh.size = size_value.max(Vector3(0.01, 0.01, 0.01))
	var instance := MeshInstance3D.new()
	instance.name = part_name
	instance.mesh = mesh
	instance.position = position_value
	instance.material_override = material
	instance.cast_shadow = GeometryInstance3D.SHADOW_CASTING_SETTING_ON
	add_child(instance)
	return instance
