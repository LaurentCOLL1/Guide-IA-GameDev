extends Node

const SAVE_PATH := "user://character_profile.json"

var definition: CharacterDefinition = CharacterDefinition.new()
var avatar: ProceduralAvatar
var camera_pivot: Node3D
var camera: Camera3D
var age_control: SpinBox
var anatomy_control: OptionButton
var privacy_control: CheckBox
var status_label: Label
var controls: Dictionary = {}
var _dragging_camera := false
var _last_mouse_position := Vector2.ZERO

func _ready() -> void:
	_build_world()
	_build_interface()
	_refresh_character()

func _build_world() -> void:
	var world := Node3D.new()
	world.name = "World"
	add_child(world)

	var environment := Environment.new()
	environment.background_mode = Environment.BG_COLOR
	environment.background_color = Color(0.035, 0.045, 0.065)
	environment.ambient_light_source = Environment.AMBIENT_SOURCE_COLOR
	environment.ambient_light_color = Color(0.56, 0.62, 0.72)
	environment.ambient_light_energy = 0.72
	var world_environment := WorldEnvironment.new()
	world_environment.environment = environment
	world.add_child(world_environment)

	var key_light := DirectionalLight3D.new()
	key_light.rotation_degrees = Vector3(-38.0, -28.0, 0.0)
	key_light.light_energy = 1.25
	key_light.shadow_enabled = true
	world.add_child(key_light)

	var fill_light := OmniLight3D.new()
	fill_light.position = Vector3(-2.2, 2.6, 2.4)
	fill_light.light_energy = 2.4
	fill_light.omni_range = 7.0
	world.add_child(fill_light)

	var rim_light := OmniLight3D.new()
	rim_light.position = Vector3(2.0, 2.1, -2.0)
	rim_light.light_color = Color(0.58, 0.70, 1.0)
	rim_light.light_energy = 1.8
	rim_light.omni_range = 6.0
	world.add_child(rim_light)

	var floor_mesh := PlaneMesh.new()
	floor_mesh.size = Vector2(12.0, 12.0)
	var floor_material := StandardMaterial3D.new()
	floor_material.albedo_color = Color(0.075, 0.085, 0.105)
	floor_material.roughness = 0.88
	floor_mesh.material = floor_material
	var floor := MeshInstance3D.new()
	floor.mesh = floor_mesh
	world.add_child(floor)

	avatar = ProceduralAvatar.new()
	avatar.name = "Avatar"
	world.add_child(avatar)

	camera_pivot = Node3D.new()
	camera_pivot.name = "CameraPivot"
	camera_pivot.position = Vector3(0.0, 0.95, 0.0)
	world.add_child(camera_pivot)

	camera = Camera3D.new()
	camera.name = "Camera"
	camera.position = Vector3(0.0, 0.05, 3.5)
	camera.fov = 40.0
	camera.near = 0.03
	camera_pivot.add_child(camera)
	camera.look_at(Vector3(0.0, 0.95, 0.0), Vector3.UP)

func _build_interface() -> void:
	var canvas := CanvasLayer.new()
	canvas.name = "Interface"
	add_child(canvas)

	var margin := MarginContainer.new()
	margin.anchor_left = 0.0
	margin.anchor_top = 0.0
	margin.anchor_right = 0.0
	margin.anchor_bottom = 1.0
	margin.offset_left = 22.0
	margin.offset_top = 22.0
	margin.offset_right = 442.0
	margin.offset_bottom = -22.0
	canvas.add_child(margin)

	var panel := PanelContainer.new()
	panel.custom_minimum_size = Vector2(420.0, 0.0)
	margin.add_child(panel)

	var scroll := ScrollContainer.new()
	scroll.horizontal_scroll_mode = ScrollContainer.SCROLL_MODE_DISABLED
	panel.add_child(scroll)

	var root := VBoxContainer.new()
	root.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	root.add_theme_constant_override("separation", 9)
	scroll.add_child(root)

	var title := Label.new()
	title.text = "ASTERIA CHARACTER STUDIO"
	title.add_theme_font_size_override("font_size", 24)
	root.add_child(title)

	var subtitle := Label.new()
	subtitle.text = "Fondation morphologique Godot — prototype sans asset photoréaliste"
	subtitle.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	subtitle.modulate = Color(0.72, 0.78, 0.88)
	root.add_child(subtitle)

	_add_separator(root)
	_add_section_title(root, "Âge et stade de vie")

	var preset_row := HBoxContainer.new()
	root.add_child(preset_row)
	var preset_label := Label.new()
	preset_label.text = "Préréglage"
	preset_label.custom_minimum_size.x = 145.0
	preset_row.add_child(preset_label)
	var presets := OptionButton.new()
	presets.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	for item in ["Nourrisson", "Enfant", "Adolescent", "Jeune adulte", "Adulte mûr", "Senior"]:
		presets.add_item(item)
	presets.item_selected.connect(_on_age_preset_selected)
	preset_row.add_child(presets)

	var age_row := HBoxContainer.new()
	root.add_child(age_row)
	var age_label := Label.new()
	age_label.text = "Âge exact"
	age_label.custom_minimum_size.x = 145.0
	age_row.add_child(age_label)
	age_control = SpinBox.new()
	age_control.min_value = 0.0
	age_control.max_value = 120.0
	age_control.step = 0.1
	age_control.value = definition.age_years
	age_control.suffix = " ans"
	age_control.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	age_control.value_changed.connect(func(value: float):
		definition.age_years = value
		_refresh_character()
	)
	age_row.add_child(age_control)

	_add_separator(root)
	_add_section_title(root, "Morphologie globale")
	_add_morph_slider(root, "stature", "Taille", -1.0, 1.0)
	_add_morph_slider(root, "head_scale", "Volume de tête", -1.0, 1.0)
	_add_morph_slider(root, "shoulder_width", "Largeur épaules", -1.0, 1.0)
	_add_morph_slider(root, "chest_volume", "Volume thorax", -1.0, 1.0)
	_add_morph_slider(root, "waist_width", "Largeur taille", -1.0, 1.0)
	_add_morph_slider(root, "hip_width", "Largeur bassin", -1.0, 1.0)
	_add_morph_slider(root, "torso_length", "Longueur torse", -1.0, 1.0)
	_add_morph_slider(root, "arm_length", "Longueur bras", -1.0, 1.0)
	_add_morph_slider(root, "leg_length", "Longueur jambes", -1.0, 1.0)
	_add_morph_slider(root, "muscle_mass", "Masse musculaire", -1.0, 1.0)
	_add_morph_slider(root, "adipose_mass", "Masse adipeuse", -1.0, 1.0)
	_add_morph_slider(root, "hand_scale", "Taille mains", -1.0, 1.0)
	_add_morph_slider(root, "foot_scale", "Taille pieds", -1.0, 1.0)

	_add_separator(root)
	_add_section_title(root, "Visage et peau")
	_add_morph_slider(root, "jaw_width", "Largeur mâchoire", -1.0, 1.0)
	_add_morph_slider(root, "nose_scale", "Volume du nez", -1.0, 1.0)
	_add_morph_slider(root, "eye_spacing", "Écartement yeux", -1.0, 1.0)
	_add_morph_slider(root, "skin_pigment", "Pigmentation", 0.0, 1.0)
	_add_morph_slider(root, "skin_roughness", "Rugosité peau", 0.0, 1.0)

	_add_separator(root)
	_add_section_title(root, "Présentation et anatomie")
	var presentation_row := HBoxContainer.new()
	root.add_child(presentation_row)
	var presentation_label := Label.new()
	presentation_label.text = "Présentation"
	presentation_label.custom_minimum_size.x = 145.0
	presentation_row.add_child(presentation_label)
	var presentation := OptionButton.new()
	presentation.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	for item in ["Androgyne", "Féminine", "Masculine", "Personnalisée"]:
		presentation.add_item(item)
	presentation.item_selected.connect(func(index: int):
		definition.presentation_profile = ["androgynous", "feminine", "masculine", "custom"][index]
		_refresh_character()
	)
	presentation_row.add_child(presentation)

	var anatomy_row := HBoxContainer.new()
	root.add_child(anatomy_row)
	var anatomy_label := Label.new()
	anatomy_label.text = "Module adulte"
	anatomy_label.custom_minimum_size.x = 145.0
	anatomy_row.add_child(anatomy_label)
	anatomy_control = OptionButton.new()
	anatomy_control.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	for item in ["Neutre", "Type A", "Type B", "Module personnalisé"]:
		anatomy_control.add_item(item)
	anatomy_control.item_selected.connect(func(index: int):
		definition.adult_anatomy_profile = ["neutral", "type_a", "type_b", "custom_module"][index]
		_refresh_character()
	)
	anatomy_row.add_child(anatomy_control)

	privacy_control = CheckBox.new()
	privacy_control.text = "Sous-vêtement de confidentialité"
	privacy_control.button_pressed = true
	privacy_control.toggled.connect(func(enabled: bool):
		definition.privacy_garment_enabled = enabled
		_refresh_character()
	)
	root.add_child(privacy_control)

	var policy := Label.new()
	policy.text = "Les personnages de moins de 18 ans utilisent obligatoirement une représentation non explicite. Les modules anatomiques externes détaillés sont réservés aux adultes et doivent être fournis séparément avec provenance et licence."
	policy.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	policy.modulate = Color(0.92, 0.72, 0.44)
	root.add_child(policy)

	_add_separator(root)
	var action_row := HBoxContainer.new()
	root.add_child(action_row)
	for spec in [
		["Aléatoire", _randomize_character],
		["Réinitialiser", _reset_character],
		["Sauver", _save_character],
		["Charger", _load_character]
	]:
		var button := Button.new()
		button.text = spec[0]
		button.size_flags_horizontal = Control.SIZE_EXPAND_FILL
		button.pressed.connect(spec[1])
		action_row.add_child(button)

	status_label = Label.new()
	status_label.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	status_label.modulate = Color(0.66, 0.86, 0.72)
	root.add_child(status_label)

	var camera_help := Label.new()
	camera_help.text = "Caméra : maintenir le bouton droit et déplacer la souris. Molette : zoom."
	camera_help.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	camera_help.modulate = Color(0.65, 0.70, 0.80)
	root.add_child(camera_help)

func _add_section_title(parent: VBoxContainer, text_value: String) -> void:
	var label := Label.new()
	label.text = text_value
	label.add_theme_font_size_override("font_size", 18)
	parent.add_child(label)

func _add_separator(parent: VBoxContainer) -> void:
	parent.add_child(HSeparator.new())

func _add_morph_slider(parent: VBoxContainer, key: String, label_text: String, minimum: float, maximum: float) -> void:
	var row := HBoxContainer.new()
	parent.add_child(row)
	var label := Label.new()
	label.text = label_text
	label.custom_minimum_size.x = 145.0
	row.add_child(label)
	var slider := HSlider.new()
	slider.min_value = minimum
	slider.max_value = maximum
	slider.step = 0.01
	slider.value = float(definition.get(key))
	slider.size_flags_horizontal = Control.SIZE_EXPAND_FILL
	row.add_child(slider)
	var value_label := Label.new()
	value_label.text = _format_value(slider.value)
	value_label.horizontal_alignment = HORIZONTAL_ALIGNMENT_RIGHT
	value_label.custom_minimum_size.x = 48.0
	row.add_child(value_label)
	controls[key] = {"slider": slider, "label": value_label}
	slider.value_changed.connect(func(value: float):
		definition.set(key, value)
		value_label.text = _format_value(value)
		_refresh_character()
	)

func _format_value(value: float) -> String:
	return "%+.2f" % value

func _on_age_preset_selected(index: int) -> void:
	var ages := [0.8, 8.0, 15.0, 27.0, 52.0, 76.0]
	definition.age_years = ages[index]
	age_control.value = definition.age_years
	_refresh_character()

func _refresh_character() -> void:
	definition.clamp_morphology()
	avatar.apply_definition(definition)
	if age_control != null and not is_equal_approx(age_control.value, definition.age_years):
		age_control.set_value_no_signal(definition.age_years)
	if anatomy_control != null:
		anatomy_control.disabled = definition.is_minor()
		anatomy_control.tooltip_text = "Indisponible pour un personnage mineur." if definition.is_minor() else "Emplacement de module adulte non fourni dans ce prototype."
	if privacy_control != null:
		privacy_control.disabled = definition.is_minor()
		privacy_control.set_pressed_no_signal(definition.privacy_garment_enabled)
	if status_label != null:
		var dimensions := MorphologyRules.dimensions(definition)
		status_label.text = "Stade : %s · Taille estimée : %.2f m · Profil anatomique : %s" % [
			definition.life_stage(),
			float(dimensions["body_height"]),
			definition.adult_anatomy_profile
		]

func _randomize_character() -> void:
	var rng := RandomNumberGenerator.new()
	rng.randomize()
	for key in [
		"stature", "head_scale", "shoulder_width", "chest_volume", "waist_width",
		"hip_width", "torso_length", "arm_length", "leg_length", "muscle_mass",
		"adipose_mass", "hand_scale", "foot_scale", "jaw_width", "nose_scale", "eye_spacing"
	]:
		definition.set(key, rng.randf_range(-0.72, 0.72))
	definition.skin_pigment = rng.randf_range(0.04, 0.96)
	definition.skin_roughness = rng.randf_range(0.38, 0.82)
	_sync_controls_from_definition()
	_refresh_character()

func _reset_character() -> void:
	definition.reset_morphology()
	definition.skin_pigment = 0.45
	definition.skin_roughness = 0.62
	_sync_controls_from_definition()
	_refresh_character()

func _sync_controls_from_definition() -> void:
	for key in controls.keys():
		var slider: HSlider = controls[key]["slider"]
		var value_label: Label = controls[key]["label"]
		var value := float(definition.get(key))
		slider.set_value_no_signal(value)
		value_label.text = _format_value(value)
	if age_control != null:
		age_control.set_value_no_signal(definition.age_years)

func _save_character() -> void:
	var file := FileAccess.open(SAVE_PATH, FileAccess.WRITE)
	if file == null:
		status_label.text = "Échec de sauvegarde : %s" % FileAccess.get_open_error()
		return
	file.store_string(JSON.stringify(definition.to_dict(), "\t"))
	status_label.text = "Profil sauvegardé dans %s" % SAVE_PATH

func _load_character() -> void:
	if not FileAccess.file_exists(SAVE_PATH):
		status_label.text = "Aucune sauvegarde trouvée dans %s" % SAVE_PATH
		return
	var file := FileAccess.open(SAVE_PATH, FileAccess.READ)
	if file == null:
		status_label.text = "Impossible d’ouvrir la sauvegarde."
		return
	var parsed: Variant = JSON.parse_string(file.get_as_text())
	if typeof(parsed) != TYPE_DICTIONARY:
		status_label.text = "Sauvegarde invalide."
		return
	definition = CharacterDefinition.from_dict(parsed)
	_sync_controls_from_definition()
	_refresh_character()
	status_label.text = "Profil chargé depuis %s" % SAVE_PATH

func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventMouseButton:
		if event.button_index == MOUSE_BUTTON_RIGHT:
			_dragging_camera = event.pressed
			_last_mouse_position = event.position
		if event.pressed and event.button_index == MOUSE_BUTTON_WHEEL_UP:
			camera.position.z = maxf(1.45, camera.position.z - 0.22)
		if event.pressed and event.button_index == MOUSE_BUTTON_WHEEL_DOWN:
			camera.position.z = minf(6.5, camera.position.z + 0.22)
	elif event is InputEventMouseMotion and _dragging_camera:
		var delta := event.position - _last_mouse_position
		_last_mouse_position = event.position
		camera_pivot.rotation.y -= delta.x * 0.008
		camera_pivot.rotation.x = clampf(camera_pivot.rotation.x - delta.y * 0.006, deg_to_rad(-28.0), deg_to_rad(28.0))
