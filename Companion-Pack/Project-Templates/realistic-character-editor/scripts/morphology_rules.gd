class_name MorphologyRules
extends RefCounted

static func _smooth_segment(value: float, start: float, end: float) -> float:
	if is_equal_approx(start, end):
		return 0.0
	var t := clampf((value - start) / (end - start), 0.0, 1.0)
	return t * t * (3.0 - 2.0 * t)

static func growth_factor(age_years: float) -> float:
	var age := clampf(age_years, 0.0, 120.0)
	if age < 1.0:
		return lerpf(0.31, 0.43, _smooth_segment(age, 0.0, 1.0))
	if age < 2.0:
		return lerpf(0.43, 0.50, _smooth_segment(age, 1.0, 2.0))
	if age < 6.0:
		return lerpf(0.50, 0.67, _smooth_segment(age, 2.0, 6.0))
	if age < 12.0:
		return lerpf(0.67, 0.84, _smooth_segment(age, 6.0, 12.0))
	if age < 18.0:
		return lerpf(0.84, 1.0, _smooth_segment(age, 12.0, 18.0))
	if age <= 65.0:
		return 1.0
	return lerpf(1.0, 0.94, _smooth_segment(age, 65.0, 100.0))

static func head_fraction(age_years: float) -> float:
	var age := clampf(age_years, 0.0, 120.0)
	if age < 2.0:
		return lerpf(0.155, 0.135, _smooth_segment(age, 0.0, 2.0))
	if age < 8.0:
		return lerpf(0.135, 0.105, _smooth_segment(age, 2.0, 8.0))
	if age < 18.0:
		return lerpf(0.105, 0.088, _smooth_segment(age, 8.0, 18.0))
	return 0.088

static func dimensions(definition: CharacterDefinition) -> Dictionary:
	definition.clamp_morphology()
	var growth := growth_factor(definition.age_years)
	var adult_height := 1.72 + definition.stature * 0.22
	var body_height := adult_height * growth
	var child_roundness := 1.0 - clampf(definition.age_years / 18.0, 0.0, 1.0)
	var elder_factor := _smooth_segment(definition.age_years, 65.0, 100.0)
	var muscle := definition.muscle_mass
	var adipose := definition.adipose_mass

	var head_radius := body_height * head_fraction(definition.age_years)
	head_radius *= 1.0 + definition.head_scale * 0.16
	var neck_height := body_height * lerpf(0.035, 0.055, 1.0 - child_roundness)
	var torso_height := body_height * 0.29 * (1.0 + definition.torso_length * 0.14)
	var leg_height := body_height * 0.44 * (1.0 + definition.leg_length * 0.13)
	var arm_height := body_height * 0.34 * (1.0 + definition.arm_length * 0.13)
	var shoulder_half := body_height * 0.105 * (1.0 + definition.shoulder_width * 0.28)
	shoulder_half *= 1.0 - child_roundness * 0.18
	var hip_half := body_height * 0.092 * (1.0 + definition.hip_width * 0.30)
	var chest_depth := body_height * 0.068
	chest_depth *= 1.0 + definition.chest_volume * 0.24 + adipose * 0.16 + muscle * 0.10
	var waist_depth := body_height * 0.058
	waist_depth *= 1.0 + definition.waist_width * 0.22 + adipose * 0.22
	var limb_radius := body_height * 0.034
	limb_radius *= 1.0 + adipose * 0.20 + muscle * 0.18 + child_roundness * 0.08
	var hand_scale := body_height * 0.055 * (1.0 + definition.hand_scale * 0.18)
	var foot_scale := body_height * 0.083 * (1.0 + definition.foot_scale * 0.18)

	return {
		"body_height": body_height,
		"head_radius": head_radius,
		"neck_height": neck_height,
		"torso_height": torso_height,
		"leg_height": leg_height,
		"arm_height": arm_height,
		"shoulder_half": shoulder_half,
		"hip_half": hip_half,
		"chest_depth": chest_depth,
		"waist_depth": waist_depth,
		"limb_radius": limb_radius,
		"hand_scale": hand_scale,
		"foot_scale": foot_scale,
		"child_roundness": child_roundness,
		"elder_factor": elder_factor
	}

static func skin_color(pigment: float) -> Color:
	var p := clampf(pigment, 0.0, 1.0)
	var light := Color(0.96, 0.78, 0.66)
	var medium := Color(0.58, 0.35, 0.23)
	var dark := Color(0.18, 0.085, 0.055)
	if p < 0.55:
		return light.lerp(medium, p / 0.55)
	return medium.lerp(dark, (p - 0.55) / 0.45)
