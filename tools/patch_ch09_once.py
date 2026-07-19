from pathlib import Path

chapter_path = Path("Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md")
text = chapter_path.read_text(encoding="utf-8")

replacements = []

replacements.append((
'''\t\tTYPE_INT:
\t\t\treturn str(int(value))
\t\tTYPE_FLOAT:
\t\t\tvar number := float(value)
\t\t\tif is_nan(number) or is_inf(number):
\t\t\t\treturn ""
\t\t\treturn JSON.stringify(number)
''',
'''\t\tTYPE_INT, TYPE_FLOAT:
\t\t\tvar number := float(value)
\t\t\tif is_nan(number) or is_inf(number):
\t\t\t\treturn ""
\t\t\treturn JSON.stringify(number, "", true, true)
'''))

replacements.append((
'''static func _encode_dictionary(values: Dictionary) -> String:
\tvar keys := PackedStringArray()
\tfor key: Variant in values.keys():
\t\tif not key is String and not key is StringName:
\t\t\treturn ""
\t\tkeys.append(String(key))

\tkeys.sort()

\tvar parts := PackedStringArray()
\tfor key: String in keys:
\t\tvar encoded_value := encode(values[key])
\t\tif encoded_value.is_empty():
\t\t\treturn ""
\t\tparts.append(
\t\t\t"%s:%s" % [JSON.stringify(key), encoded_value]
\t\t)

\treturn "{" + ",".join(parts) + "}"
''',
'''static func _encode_dictionary(values: Dictionary) -> String:
\tvar normalized: Dictionary[String, Variant] = {}
\tfor original_key: Variant in values.keys():
\t\tif not original_key is String and not original_key is StringName:
\t\t\treturn ""

\t\tvar text_key := String(original_key)
\t\tif normalized.has(text_key):
\t\t\treturn ""
\t\tnormalized[text_key] = values[original_key]

\tvar keys := PackedStringArray(normalized.keys())
\tkeys.sort()

\tvar parts := PackedStringArray()
\tfor key: String in keys:
\t\tvar encoded_value := encode(normalized[key])
\t\tif encoded_value.is_empty():
\t\t\treturn ""
\t\tparts.append(
\t\t\t"%s:%s" % [JSON.stringify(key), encoded_value]
\t\t)

\treturn "{" + ",".join(parts) + "}"
'''))

replacements.append((
'''Le tri produit une représentation stable avant SHA-256.
''',
'''Le tri produit une représentation stable avant SHA-256.

Les entiers et flottants sont tous normalisés vers un nombre JSON en précision complète. Cette règle est nécessaire parce que le parseur JSON restitue les nombres sous une représentation numérique commune. Sans cette normalisation, un compteur entier pourrait produire une empreinte différente après écriture et relecture.
'''))

replacements.append((
'''\tfor profile_id: StringName in _runtime_states.keys():
\t\tvar state := _runtime_states[profile_id]
\t\trecords.append(
''',
'''\tfor profile_id: StringName in _runtime_states.keys():
\t\tvar state := _runtime_states[profile_id] as BeaconRuntimeState
\t\tif state == null:
\t\t\tpush_error("État runtime invalide : %s" % profile_id)
\t\t\treturn {}
\t\trecords.append(
'''))

old_validate = '''func validate_data(data: Dictionary) -> PackedStringArray:
\tvar errors := PackedStringArray()
\tif not data.has("records") or not data["records"] is Array:
\t\terrors.append("beacons.records doit être un tableau")
\t\treturn errors

\tvar seen: Dictionary[StringName, bool] = {}
\tfor index: int in data["records"].size():
\t\tvar value: Variant = data["records"][index]
\t\tif not value is Dictionary:
\t\t\terrors.append("beacons.records[%d] doit être un objet" % index)
\t\t\tcontinue

\t\tvar row := value as Dictionary
\t\tvar profile_id := StringName(String(row.get("profile_id", "")))
\t\tif not StableId.is_valid(profile_id):
\t\t\terrors.append("Identifiant de balise invalide à l’index %d" % index)
\t\telif seen.has(profile_id):
\t\t\terrors.append("Balise dupliquée : %s" % profile_id)
\t\telse:
\t\t\tseen[profile_id] = true

\t\tif not row.get("is_enabled", null) is bool:
\t\t\terrors.append("is_enabled invalide pour %s" % profile_id)
\t\tif int(row.get("activation_count", -1)) < 0:
\t\t\terrors.append("activation_count invalide pour %s" % profile_id)
\t\tif float(row.get("cooldown_remaining", -1.0)) < 0.0:
\t\t\terrors.append("cooldown_remaining invalide pour %s" % profile_id)

\treturn errors
'''
new_validate = '''func validate_data(data: Dictionary) -> PackedStringArray:
\tvar errors := PackedStringArray()
\tif not data.has("records") or not data["records"] is Array:
\t\terrors.append("beacons.records doit être un tableau")
\t\treturn errors

\tvar records := data["records"] as Array
\tif records.size() > 10000:
\t\terrors.append("beacons.records dépasse la limite de 10 000 entrées")
\t\treturn errors

\tvar seen: Dictionary[StringName, bool] = {}
\tfor index: int in records.size():
\t\tvar value: Variant = records[index]
\t\tif not value is Dictionary:
\t\t\terrors.append("beacons.records[%d] doit être un objet" % index)
\t\t\tcontinue

\t\tvar row := value as Dictionary
\t\tvar profile_id := StringName(String(row.get("profile_id", "")))
\t\tif not StableId.is_valid(profile_id):
\t\t\terrors.append("Identifiant de balise invalide à l’index %d" % index)
\t\telif seen.has(profile_id):
\t\t\terrors.append("Balise dupliquée : %s" % profile_id)
\t\telse:
\t\t\tseen[profile_id] = true

\t\tif not (row.get("is_enabled", null) is bool):
\t\t\terrors.append("is_enabled invalide pour %s" % profile_id)

\t\tvar count_value: Variant = row.get("activation_count", null)
\t\tif not _is_non_negative_integer(count_value):
\t\t\terrors.append("activation_count invalide pour %s" % profile_id)

\t\tvar cooldown_value: Variant = row.get("cooldown_remaining", null)
\t\tif not _is_non_negative_number(cooldown_value):
\t\t\terrors.append("cooldown_remaining invalide pour %s" % profile_id)

\treturn errors

func _is_non_negative_integer(value: Variant) -> bool:
\tif not value is int and not value is float:
\t\treturn false

\tvar number := float(value)
\treturn (
\t\tnot is_nan(number)
\t\tand not is_inf(number)
\t\tand number >= 0.0
\t\tand number <= 9007199254740991.0
\t\tand is_equal_approx(number, floor(number))
\t)

func _is_non_negative_number(value: Variant) -> bool:
\tif not value is int and not value is float:
\t\treturn false

\tvar number := float(value)
\treturn not is_nan(number) and not is_inf(number) and number >= 0.0
'''
replacements.append((old_validate, new_validate))

replacements.append((
'''\tvar feature_payload: Dictionary = {}
\tfor section: SaveSection in _sections:
\t\tvar section_key := section.key()
\t\tif section_key.is_empty() or feature_payload.has(section_key):
\t\t\tpush_error("Clé de section absente ou dupliquée : %s" % section_key)
\t\t\treturn {}
\t\tfeature_payload[section_key] = section.capture()

\tvar payload := {
\t\t"world": metadata.get("world_snapshot", {}),
\t\t"player": metadata.get("player_snapshot", {}),
\t\t"features": feature_payload,
\t}
''',
'''\tvar world_value: Variant = metadata.get("world_snapshot", {})
\tvar player_value: Variant = metadata.get("player_snapshot", {})
\tif not world_value is Dictionary or not player_value is Dictionary:
\t\tpush_error("Les snapshots world et player doivent être des dictionnaires.")
\t\treturn {}

\tvar feature_payload: Dictionary = {}
\tfor section: SaveSection in _sections:
\t\tvar section_key := String(section.key())
\t\tif section_key.is_empty() or feature_payload.has(section_key):
\t\t\tpush_error("Clé de section absente ou dupliquée : %s" % section_key)
\t\t\treturn {}

\t\tvar section_data := section.capture()
\t\tif section_data.is_empty():
\t\t\tpush_error("Capture vide ou invalide : %s" % section_key)
\t\t\treturn {}
\t\tfeature_payload[section_key] = section_data

\tvar payload := {
\t\t"world": world_value as Dictionary,
\t\t"player": player_value as Dictionary,
\t\t"features": feature_payload,
\t}
'''))

replacements.append((
'''\tvar version := int(document.get("format_version", -1))
\tif version < 1:
\t\terrors.append("format_version absent ou invalide")
\telif version > CURRENT_FORMAT_VERSION:
''',
'''\tvar version_value: Variant = document.get("format_version", null)
\tvar version := -1
\tif version_value is int or version_value is float:
\t\tvar version_number := float(version_value)
\t\tif (
\t\t\tnot is_nan(version_number)
\t\t\tand not is_inf(version_number)
\t\t\tand is_equal_approx(version_number, floor(version_number))
\t\t):
\t\t\tversion = int(version_number)

\tif version < 1:
\t\terrors.append("format_version absent ou invalide")
\telif version > CURRENT_FORMAT_VERSION:
'''))

replacements.append((
'''\tvar text := JSON.stringify(document, "\\t", false)
''',
'''\tvar text := JSON.stringify(document, "\\t", true, true)
'''))

replacements.append((
'''class_name SaveDocumentReader
extends RefCounted

func read(path: String) -> Dictionary:
\tif not FileAccess.file_exists(path):
''',
'''class_name SaveDocumentReader
extends RefCounted

const MAX_SAVE_BYTES := 16 * 1024 * 1024

func read(path: String) -> Dictionary:
\tif not FileAccess.file_exists(path):
'''))

replacements.append((
'''\tvar file := FileAccess.open(path, FileAccess.READ)
''',
'''\tvar file_size := FileAccess.get_size(path)
\tif file_size < 1 or file_size > MAX_SAVE_BYTES:
\t\tpush_error("Taille de sauvegarde refusée : %d octets" % file_size)
\t\treturn {}

\tvar file := FileAccess.open(path, FileAccess.READ)
'''))

replacements.append((
'''\tfor key: StringName in _sections.keys():
\t\tif not features.get(key, null) is Dictionary:
\t\t\terrors.append("Section absente ou invalide : %s" % key)
\t\t\tcontinue

\t\tvar section_errors := _sections[key].validate_data(
\t\t\tfeatures[key] as Dictionary
\t\t)
''',
'''\tfor key: StringName in _sections.keys():
\t\tvar serialized_key := String(key)
\t\tif not features.get(serialized_key, null) is Dictionary:
\t\t\terrors.append("Section absente ou invalide : %s" % key)
\t\t\tcontinue

\t\tvar section_errors := _sections[key].validate_data(
\t\t\tfeatures[serialized_key] as Dictionary
\t\t)
'''))

replacements.append((
'''\tfor key: StringName in _sections.keys():
\t\tvar error := _sections[key].apply_data(
\t\t\tfeatures[key] as Dictionary
\t\t)
''',
'''\tfor key: StringName in _sections.keys():
\t\tvar serialized_key := String(key)
\t\tvar error := _sections[key].apply_data(
\t\t\tfeatures[serialized_key] as Dictionary
\t\t)
'''))

replacements.append((
'''Les limites :

- fichiers plus volumineux ;
''',
'''Limites :

- fichiers plus volumineux ;
'''))

for old, new in replacements:
    if old not in text:
        raise SystemExit(f"Replacement source not found:\n{old[:180]}")
    text = text.replace(old, new, 1)

text = text.replace(
    "- limites de nombre d’éléments ;\n",
    "- limites de nombre d’éléments ;\n- entiers JSON limités à la plage exacte de 53 bits lorsqu’une précision entière est requise ;\n",
    1,
)

chapter_path.write_text(text, encoding="utf-8", newline="\n")

Path("tools/patch_ch09_once.py").unlink()
Path(".github/workflows/patch-ch09-once.yml").unlink()
