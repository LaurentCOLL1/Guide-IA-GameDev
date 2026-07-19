from pathlib import Path

chapter_path = Path("Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md")
text = chapter_path.read_text(encoding="utf-8")

replacements: list[tuple[str, str]] = []

replacements.append((
'''\tfor key: String in ["x", "y", "z"]:
\t\tif not data.has(key):
\t\t\terrors.append("%s.%s est absent" % [path, key])
\t\t\treturn Vector3.ZERO
\t\tif not data[key] is float and not data[key] is int:
\t\t\terrors.append("%s.%s doit être numérique" % [path, key])
\t\t\treturn Vector3.ZERO

\treturn Vector3(
''',
'''\tfor key: String in ["x", "y", "z"]:
\t\tif not data.has(key):
\t\t\terrors.append("%s.%s est absent" % [path, key])
\t\t\treturn Vector3.ZERO
\t\tif not data[key] is float and not data[key] is int:
\t\t\terrors.append("%s.%s doit être numérique" % [path, key])
\t\t\treturn Vector3.ZERO

\t\tvar number := float(data[key])
\t\tif is_nan(number) or is_inf(number):
\t\t\terrors.append("%s.%s doit être fini" % [path, key])
\t\t\treturn Vector3.ZERO

\treturn Vector3(
'''))

replacements.append((
'''class_name CanonicalJson
extends RefCounted

static func encode(value: Variant) -> String:
''',
'''class_name CanonicalJson
extends RefCounted

const MAX_EXACT_JSON_INTEGER := 9007199254740991.0

static func encode(value: Variant) -> String:
'''))

replacements.append((
'''\t\tTYPE_INT, TYPE_FLOAT:
\t\t\tvar number := float(value)
\t\t\tif is_nan(number) or is_inf(number):
\t\t\t\treturn ""
\t\t\treturn JSON.stringify(number, "", true, true)
''',
'''\t\tTYPE_INT, TYPE_FLOAT:
\t\t\tvar number := float(value)
\t\t\tif is_nan(number) or is_inf(number):
\t\t\t\treturn ""
\t\t\tif value is int and absf(number) > MAX_EXACT_JSON_INTEGER:
\t\t\t\treturn ""
\t\t\treturn JSON.stringify(number, "", true, true)
'''))

validator_anchor = '''\treturn errors
```

### 17.1 Refus des versions futures
'''
validator_extension = '''\treturn errors

func validate_current_payload(document: Dictionary) -> PackedStringArray:
\tvar errors := PackedStringArray()
\tif int(document.get("format_version", -1)) != CURRENT_FORMAT_VERSION:
\t\terrors.append("Le document n’est pas au format courant")
\t\treturn errors

\tif not document.get("payload", null) is Dictionary:
\t\terrors.append("payload doit être un objet")
\t\treturn errors

\tvar payload := document["payload"] as Dictionary
\tfor key: String in ["world", "player", "features"]:
\t\tif not payload.get(key, null) is Dictionary:
\t\t\terrors.append("payload.%s doit être un objet" % key)

\tif not errors.is_empty():
\t\treturn errors

\tvar world := payload["world"] as Dictionary
\tvar world_id := StringName(String(world.get("id", "")))
\tif not StableId.is_valid(world_id):
\t\terrors.append("payload.world.id est invalide")

\tvar player := payload["player"] as Dictionary
\tif not player.get("position", null) is Dictionary:
\t\terrors.append("payload.player.position doit être un objet")
\telse:
\t\tvar position_errors := PackedStringArray()
\t\tSaveValueCodec.dictionary_to_vector3(
\t\t\tplayer["position"] as Dictionary,
\t\t\tposition_errors,
\t\t\t"payload.player.position"
\t\t)
\t\terrors.append_array(position_errors)

\treturn errors
```

### 17.1 Refus des versions futures
'''
replacements.append((validator_anchor, validator_extension))

replacements.append((
'''func write_document(path: String, document: Dictionary) -> Error:
\tvar directory_error := DirAccess.make_dir_recursive_absolute(
''',
'''func write_document(path: String, document: Dictionary) -> Error:
\tif not path.begins_with("user://saves/"):
\t\treturn ERR_INVALID_PARAMETER

\tvar directory_error := DirAccess.make_dir_recursive_absolute(
'''))

old_backup = '''\tif FileAccess.file_exists(path):
\t\tvar backup_error := DirAccess.copy_absolute(path, backup_path)
\t\tif backup_error != OK:
\t\t\t_remove_if_exists(temporary_path)
\t\t\treturn backup_error

\tvar replace_error := DirAccess.rename_absolute(temporary_path, path)
'''
new_backup = '''\tif FileAccess.file_exists(path):
\t\tvar current_document := reader.read(path)
\t\tif _is_future_document(current_document):
\t\t\t_remove_if_exists(temporary_path)
\t\t\tpush_error("Un build ancien refuse d’écraser une sauvegarde future.")
\t\t\treturn ERR_UNAVAILABLE

\t\tvar current_errors := validator.validate_envelope(current_document)
\t\tif not current_document.is_empty() and current_errors.is_empty():
\t\t\tvar backup_error := DirAccess.copy_absolute(path, backup_path)
\t\t\tif backup_error != OK:
\t\t\t\t_remove_if_exists(temporary_path)
\t\t\t\treturn backup_error
\t\telse:
\t\t\tpush_warning(
\t\t\t\t"Le fichier principal existant est invalide ; "
\t\t\t\t+ "la copie .bak actuelle est conservée."
\t\t\t)

\tvar replace_error := DirAccess.rename_absolute(temporary_path, path)
'''
replacements.append((old_backup, new_backup))

old_read_backup = '''func read_with_backup(path: String) -> Dictionary:
\tvar reader := SaveDocumentReader.new()
\tvar validator := SaveDocumentValidator.new()

\tvar primary := reader.read(path)
\tif not primary.is_empty():
\t\tvar errors := validator.validate_envelope(primary)
\t\tif errors.is_empty():
\t\t\treturn primary

\tvar backup_path := path + ".bak"
\tvar backup := reader.read(backup_path)
\tif backup.is_empty():
\t\treturn {}

\tvar backup_errors := validator.validate_envelope(backup)
\tif not backup_errors.is_empty():
\t\treturn {}

\tpush_warning("Le slot principal est invalide ; la copie de secours est utilisée.")
\treturn backup
'''
new_read_backup = '''func read_with_backup(path: String) -> Dictionary:
\tvar reader := SaveDocumentReader.new()
\tvar validator := SaveDocumentValidator.new()

\tvar primary := reader.read(path)
\tif not primary.is_empty():
\t\tif _is_future_document(primary):
\t\t\tpush_error("Sauvegarde créée par une version plus récente.")
\t\t\treturn {}

\t\tvar errors := validator.validate_envelope(primary)
\t\tif errors.is_empty():
\t\t\treturn primary

\tvar backup_path := path + ".bak"
\tvar backup := reader.read(backup_path)
\tif backup.is_empty() or _is_future_document(backup):
\t\treturn {}

\tvar backup_errors := validator.validate_envelope(backup)
\tif not backup_errors.is_empty():
\t\treturn {}

\tpush_warning("Le slot principal est invalide ; la copie de secours est utilisée.")
\treturn backup

func _is_future_document(document: Dictionary) -> bool:
\tvar value: Variant = document.get("format_version", null)
\tif not value is int and not value is float:
\t\treturn false

\tvar number := float(value)
\tif is_nan(number) or is_inf(number):
\t\treturn false
\tif not is_equal_approx(number, floor(number)):
\t\treturn false

\treturn int(number) > SaveDocumentValidator.CURRENT_FORMAT_VERSION
'''
replacements.append((old_read_backup, new_read_backup))

replacements.append((
'''func _init() -> void:
\tregister_migration(SaveMigrationV1ToV2.new())
''',
'''func _init() -> void:
\tvar error := register_migration(SaveMigrationV1ToV2.new())
\tif error != OK:
\t\tpush_error("Enregistrement de la migration V1 vers V2 impossible.")
'''))

old_registry_end = '''\tfor key: StringName in _sections.keys():
\t\tvar serialized_key := String(key)
\t\tif not features.get(serialized_key, null) is Dictionary:
\t\t\terrors.append("Section absente ou invalide : %s" % key)
\t\t\tcontinue

\t\tvar section_errors := _sections[key].validate_data(
\t\t\tfeatures[serialized_key] as Dictionary
\t\t)
\t\tfor message: String in section_errors:
\t\t\terrors.append("%s : %s" % [key, message])

\treturn errors
'''
new_registry_end = '''\tfor key: StringName in _sections.keys():
\t\tvar serialized_key := String(key)
\t\tif not features.get(serialized_key, null) is Dictionary:
\t\t\terrors.append("Section absente ou invalide : %s" % key)
\t\t\tcontinue

\t\tvar section_errors := _sections[key].validate_data(
\t\t\tfeatures[serialized_key] as Dictionary
\t\t)
\t\tfor message: String in section_errors:
\t\t\terrors.append("%s : %s" % [key, message])

\tfor serialized_key: Variant in features.keys():
\t\tif not serialized_key is String and not serialized_key is StringName:
\t\t\terrors.append("Une clé de section n’est pas textuelle")
\t\t\tcontinue
\t\tif not _sections.has(StringName(String(serialized_key))):
\t\t\terrors.append("Section inconnue : %s" % serialized_key)

\treturn errors
'''
replacements.append((old_registry_end, new_registry_end))

old_load_tail = '''\tvar source := _store.read_with_backup(path)
\tif source.is_empty():
\t\t_load_in_progress = false
\t\treturn {}

\tvar envelope_errors := _validator.validate_envelope(source)
\tif not envelope_errors.is_empty():
\t\t_load_in_progress = false
\t\treturn {}

\tvar migrated := _migrations.migrate_to_current(source)
\tif migrated.is_empty():
\t\t_load_in_progress = false
\t\treturn {}

\tvar current_errors := _validator.validate_envelope(migrated)
\tif not current_errors.is_empty():
\t\t_load_in_progress = false
\t\treturn {}

\tvar payload := migrated["payload"] as Dictionary
\tvar features := payload.get("features", {}) as Dictionary
\tvar section_errors := _sections.validate_features(features)
\tif not section_errors.is_empty():
\t\t_load_in_progress = false
\t\treturn {}

\t_load_in_progress = false
\treturn migrated

func finish_apply(document: Dictionary) -> Error:
\tif document.is_empty():
\t\treturn ERR_INVALID_PARAMETER

\tvar payload := document["payload"] as Dictionary
\tvar features := payload["features"] as Dictionary
\treturn _sections.apply_features(features)
'''
new_load_tail = '''\tvar source := _store.read_with_backup(path)
\tif source.is_empty():
\t\t_load_in_progress = false
\t\treturn {}

\tvar envelope_errors := _validator.validate_envelope(source)
\tif not envelope_errors.is_empty():
\t\t_load_in_progress = false
\t\treturn {}

\tvar migrated := _migrations.migrate_to_current(source)
\tif migrated.is_empty():
\t\t_load_in_progress = false
\t\treturn {}

\tvar current_errors := _validator.validate_envelope(migrated)
\tcurrent_errors.append_array(
\t\t_validator.validate_current_payload(migrated)
\t)
\tif not current_errors.is_empty():
\t\t_load_in_progress = false
\t\treturn {}

\tvar slot := migrated["slot"] as Dictionary
\tvar document_slot := StringName(String(slot.get("id", "")))
\tif document_slot != slot_id:
\t\tpush_error("Le contenu du slot ne correspond pas au fichier demandé.")
\t\t_load_in_progress = false
\t\treturn {}

\tvar payload := migrated["payload"] as Dictionary
\tvar features := payload.get("features", {}) as Dictionary
\tvar section_errors := _sections.validate_features(features)
\tif not section_errors.is_empty():
\t\t_load_in_progress = false
\t\treturn {}

\treturn migrated

func finish_apply(document: Dictionary) -> Error:
\tif not _load_in_progress:
\t\treturn ERR_UNCONFIGURED
\tif document.is_empty():
\t\t_load_in_progress = false
\t\treturn ERR_INVALID_PARAMETER

\tvar payload := document["payload"] as Dictionary
\tvar features := payload["features"] as Dictionary
\tvar error := _sections.apply_features(features)
\t_load_in_progress = false
\treturn error

func cancel_load() -> void:
\t_load_in_progress = false
'''
replacements.append((old_load_tail, new_load_tail))

replacements.append((
'''La méthode retourne un document migré et validé.

Le contrôleur de transition doit ensuite :
''',
'''La méthode retourne un document migré et validé tout en conservant le verrou de chargement.

Le contrôleur de transition doit ensuite :
'''))

replacements.append((
'''4. basculer l’affichage.

### 26.2 Verrou logique
''',
'''4. appeler `finish_apply()` puis basculer l’affichage ;
5. appeler `cancel_load()` si la préparation du monde échoue.

`finish_apply()` applique ici les sections de fonctionnalités. Le contrôleur du monde reste responsable de la position du joueur, de la scène cible et de la bascule entre ancien et nouveau monde.

### 26.2 Verrou logique
'''))

replacements.append((
'''Une implémentation asynchrone devra garantir le nettoyage du verrou dans tous les chemins d’erreur.
''',
'''Le verrou de chargement reste actif entre `load_slot()` et `finish_apply()` ou `cancel_load()`. Une implémentation asynchrone devra garantir l’appel de l’une de ces deux sorties dans tous les chemins d’erreur.
'''))

for old, new in replacements:
    if old not in text:
        raise SystemExit(f"Replacement source not found:\n{old[:240]}")
    text = text.replace(old, new, 1)

chapter_path.write_text(text, encoding="utf-8", newline="\n")
Path("tools/patch_ch09_round2.py").unlink()
Path(".github/workflows/patch-ch09-round2.yml").unlink()
