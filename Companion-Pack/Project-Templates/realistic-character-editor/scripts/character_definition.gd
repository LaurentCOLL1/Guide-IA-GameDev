class_name CharacterDefinition
extends Resource

const SCHEMA_VERSION := 1

@export_range(0.0, 120.0, 0.1) var age_years: float = 28.0
@export_range(-1.0, 1.0, 0.01) var stature: float = 0.0
@export_range(-1.0, 1.0, 0.01) var head_scale: float = 0.0
@export_range(-1.0, 1.0, 0.01) var shoulder_width: float = 0.0
@export_range(-1.0, 1.0, 0.01) var chest_volume: float = 0.0
@export_range(-1.0, 1.0, 0.01) var waist_width: float = 0.0
@export_range(-1.0, 1.0, 0.01) var hip_width: float = 0.0
@export_range(-1.0, 1.0, 0.01) var torso_length: float = 0.0
@export_range(-1.0, 1.0, 0.01) var arm_length: float = 0.0
@export_range(-1.0, 1.0, 0.01) var leg_length: float = 0.0
@export_range(-1.0, 1.0, 0.01) var muscle_mass: float = 0.0
@export_range(-1.0, 1.0, 0.01) var adipose_mass: float = 0.0
@export_range(-1.0, 1.0, 0.01) var hand_scale: float = 0.0
@export_range(-1.0, 1.0, 0.01) var foot_scale: float = 0.0
@export_range(-1.0, 1.0, 0.01) var jaw_width: float = 0.0
@export_range(-1.0, 1.0, 0.01) var nose_scale: float = 0.0
@export_range(-1.0, 1.0, 0.01) var eye_spacing: float = 0.0
@export_range(0.0, 1.0, 0.01) var skin_pigment: float = 0.45
@export_range(0.0, 1.0, 0.01) var skin_roughness: float = 0.62
@export var presentation_profile: String = "androgynous"
@export var adult_anatomy_profile: String = "neutral"
@export var privacy_garment_enabled: bool = true

func is_minor() -> bool:
	return age_years < 18.0

func life_stage() -> String:
	if age_years < 2.0:
		return "infant"
	if age_years < 6.0:
		return "early_childhood"
	if age_years < 12.0:
		return "childhood"
	if age_years < 18.0:
		return "adolescence"
	if age_years < 40.0:
		return "young_adult"
	if age_years < 65.0:
		return "mature_adult"
	return "elder"

func enforce_safety_policy() -> void:
	age_years = clampf(age_years, 0.0, 120.0)
	if is_minor():
		adult_anatomy_profile = "unavailable_for_minor"
		privacy_garment_enabled = true
	elif adult_anatomy_profile == "unavailable_for_minor":
		adult_anatomy_profile = "neutral"

func clamp_morphology() -> void:
	stature = clampf(stature, -1.0, 1.0)
	head_scale = clampf(head_scale, -1.0, 1.0)
	shoulder_width = clampf(shoulder_width, -1.0, 1.0)
	chest_volume = clampf(chest_volume, -1.0, 1.0)
	waist_width = clampf(waist_width, -1.0, 1.0)
	hip_width = clampf(hip_width, -1.0, 1.0)
	torso_length = clampf(torso_length, -1.0, 1.0)
	arm_length = clampf(arm_length, -1.0, 1.0)
	leg_length = clampf(leg_length, -1.0, 1.0)
	muscle_mass = clampf(muscle_mass, -1.0, 1.0)
	adipose_mass = clampf(adipose_mass, -1.0, 1.0)
	hand_scale = clampf(hand_scale, -1.0, 1.0)
	foot_scale = clampf(foot_scale, -1.0, 1.0)
	jaw_width = clampf(jaw_width, -1.0, 1.0)
	nose_scale = clampf(nose_scale, -1.0, 1.0)
	eye_spacing = clampf(eye_spacing, -1.0, 1.0)
	skin_pigment = clampf(skin_pigment, 0.0, 1.0)
	skin_roughness = clampf(skin_roughness, 0.0, 1.0)
	enforce_safety_policy()

func reset_morphology() -> void:
	stature = 0.0
	head_scale = 0.0
	shoulder_width = 0.0
	chest_volume = 0.0
	waist_width = 0.0
	hip_width = 0.0
	torso_length = 0.0
	arm_length = 0.0
	leg_length = 0.0
	muscle_mass = 0.0
	adipose_mass = 0.0
	hand_scale = 0.0
	foot_scale = 0.0
	jaw_width = 0.0
	nose_scale = 0.0
	eye_spacing = 0.0

func to_dict() -> Dictionary:
	clamp_morphology()
	return {
		"schema_version": SCHEMA_VERSION,
		"age_years": age_years,
		"life_stage": life_stage(),
		"morphology": {
			"stature": stature,
			"head_scale": head_scale,
			"shoulder_width": shoulder_width,
			"chest_volume": chest_volume,
			"waist_width": waist_width,
			"hip_width": hip_width,
			"torso_length": torso_length,
			"arm_length": arm_length,
			"leg_length": leg_length,
			"muscle_mass": muscle_mass,
			"adipose_mass": adipose_mass,
			"hand_scale": hand_scale,
			"foot_scale": foot_scale,
			"jaw_width": jaw_width,
			"nose_scale": nose_scale,
			"eye_spacing": eye_spacing
		},
		"appearance": {
			"skin_pigment": skin_pigment,
			"skin_roughness": skin_roughness,
			"presentation_profile": presentation_profile
		},
		"anatomy": {
			"adult_anatomy_profile": adult_anatomy_profile,
			"privacy_garment_enabled": privacy_garment_enabled
		}
	}

static func from_dict(data: Dictionary) -> CharacterDefinition:
	var result := CharacterDefinition.new()
	result.age_years = float(data.get("age_years", 28.0))
	var morphology: Dictionary = data.get("morphology", {})
	for key in morphology.keys():
		if key in [
			"stature", "head_scale", "shoulder_width", "chest_volume",
			"waist_width", "hip_width", "torso_length", "arm_length",
			"leg_length", "muscle_mass", "adipose_mass", "hand_scale",
			"foot_scale", "jaw_width", "nose_scale", "eye_spacing"
		]:
			result.set(key, float(morphology[key]))
	var appearance: Dictionary = data.get("appearance", {})
	result.skin_pigment = float(appearance.get("skin_pigment", 0.45))
	result.skin_roughness = float(appearance.get("skin_roughness", 0.62))
	result.presentation_profile = str(appearance.get("presentation_profile", "androgynous"))
	var anatomy: Dictionary = data.get("anatomy", {})
	result.adult_anatomy_profile = str(anatomy.get("adult_anatomy_profile", "neutral"))
	result.privacy_garment_enabled = bool(anatomy.get("privacy_garment_enabled", true))
	result.clamp_morphology()
	return result
