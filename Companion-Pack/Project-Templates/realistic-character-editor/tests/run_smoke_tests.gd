extends SceneTree

const CharacterDefinitionScript = preload("res://scripts/character_definition.gd")
const MorphologyRulesScript = preload("res://scripts/morphology_rules.gd")

var failures: PackedStringArray = []

func _init() -> void:
	_test_minor_policy()
	_test_adult_policy()
	_test_growth_curve()
	_test_json_round_trip()
	_test_extreme_morphology()

	if failures.is_empty():
		print("Character editor smoke tests: OK")
		quit(0)
		return

	for failure in failures:
		push_error(failure)
	quit(1)

func _expect(condition: bool, message: String) -> void:
	if not condition:
		failures.append(message)

func _test_minor_policy() -> void:
	var definition = CharacterDefinitionScript.new()
	definition.age_years = 15.0
	definition.adult_anatomy_profile = "custom_module"
	definition.privacy_garment_enabled = false
	definition.clamp_morphology()
	_expect(definition.adult_anatomy_profile == "unavailable_for_minor", "Minor anatomy profile was not blocked.")
	_expect(definition.privacy_garment_enabled, "Minor privacy garment was not forced.")

func _test_adult_policy() -> void:
	var definition = CharacterDefinitionScript.new()
	definition.age_years = 25.0
	definition.adult_anatomy_profile = "custom_module"
	definition.privacy_garment_enabled = false
	definition.clamp_morphology()
	_expect(definition.adult_anatomy_profile == "custom_module", "Adult anatomy profile was unexpectedly replaced.")
	_expect(not definition.privacy_garment_enabled, "Adult privacy preference was unexpectedly forced.")

func _test_growth_curve() -> void:
	var infant := MorphologyRulesScript.growth_factor(0.0)
	var child := MorphologyRulesScript.growth_factor(8.0)
	var adult := MorphologyRulesScript.growth_factor(25.0)
	var elder := MorphologyRulesScript.growth_factor(95.0)
	_expect(infant < child, "Infant growth factor must be lower than child growth factor.")
	_expect(child < adult, "Child growth factor must be lower than adult growth factor.")
	_expect(elder <= adult, "Elder height factor should not exceed adult factor in the current model.")

func _test_json_round_trip() -> void:
	var original = CharacterDefinitionScript.new()
	original.age_years = 42.0
	original.shoulder_width = 0.37
	original.hip_width = -0.22
	original.skin_pigment = 0.81
	var encoded := JSON.stringify(original.to_dict())
	var parsed: Variant = JSON.parse_string(encoded)
	var restored = CharacterDefinitionScript.from_dict(parsed)
	_expect(is_equal_approx(restored.age_years, original.age_years), "Age failed JSON round trip.")
	_expect(is_equal_approx(restored.shoulder_width, original.shoulder_width), "Shoulder width failed JSON round trip.")
	_expect(is_equal_approx(restored.skin_pigment, original.skin_pigment), "Skin pigment failed JSON round trip.")

func _test_extreme_morphology() -> void:
	var definition = CharacterDefinitionScript.new()
	definition.age_years = 18.0
	definition.stature = 10.0
	definition.head_scale = -10.0
	definition.adipose_mass = 10.0
	definition.clamp_morphology()
	var dimensions: Dictionary = MorphologyRulesScript.dimensions(definition)
	_expect(is_equal_approx(definition.stature, 1.0), "Stature was not clamped.")
	_expect(is_equal_approx(definition.head_scale, -1.0), "Head scale was not clamped.")
	_expect(float(dimensions["body_height"]) > 0.0, "Body height must stay positive.")
	_expect(float(dimensions["head_radius"]) > 0.0, "Head radius must stay positive.")
