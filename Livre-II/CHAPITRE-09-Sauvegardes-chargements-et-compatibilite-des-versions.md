---
title: "Livre II — Chapitre 9 : Sauvegardes, chargements et compatibilité des versions"
id: "DOC-L2-CH09"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 9
last-verified: "2026-07-19"
audit-status: "complete"
audit-date: "2026-07-19"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-09.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
recommended-reasoning: "GPT-5.6 Sol — Élevée"
---

# Sauvegardes, chargements et compatibilité des versions

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir, **[LECTURE]** exemple à étudier. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH09`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Niveau de raisonnement conseillé :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-09.md`.

## 1. Rôle du chapitre

Le chapitre 8 a créé une persistance spécialisée avec SQLite. Une base relationnelle sait conserver des lignes, appliquer des contraintes et exécuter des transactions. Elle ne définit pas, à elle seule, ce qu’est une **sauvegarde de partie**.

Une sauvegarde doit répondre à une autre question :

> Quel ensemble cohérent de données faut-il capturer pour reconstruire une partie jouable dans une version actuelle ou future du jeu ?

À la fin du chapitre, le lecteur doit savoir :

- distinguer dépôt persistant, snapshot et fichier de sauvegarde ;
- choisir une stratégie de slots manuels, automatiques et rapides ;
- définir un document JSON explicite et versionné ;
- convertir les types Godot vers des valeurs JSON ;
- capturer un état cohérent sans mélanger plusieurs instants ;
- calculer et vérifier une empreinte du contenu ;
- écrire dans un fichier temporaire puis remplacer la cible ;
- conserver une copie de secours ;
- refuser un fichier futur avant toute mutation du monde ;
- migrer une ancienne sauvegarde en mémoire ;
- valider toutes les sections avant de les appliquer ;
- charger en plusieurs phases ;
- récupérer un slot corrompu depuis sa copie `.bak` ;
- définir une politique de rotation et de rétention ;
- préparer les modes Solo et Studio.

## 2. Prérequis

Le lecteur doit connaître :

- les types, classes, tableaux et dictionnaires du chapitre 2 ;
- les scènes et signaux du chapitre 3 ;
- les frontières de modules du chapitre 4 ;
- l’injection de dépendances du chapitre 5 ;
- l’état runtime du chapitre 6 ;
- les identifiants stables, JSON et configurations du chapitre 7 ;
- les repositories, transactions et migrations SQLite du chapitre 8.

## 3. Périmètre et frontières

Ce chapitre définit :

- le snapshot cohérent d’une partie ;
- un format de sauvegarde JSON ;
- les métadonnées de slot ;
- la capture et la restauration des sections ;
- la validation et l’intégrité ;
- les migrations de sauvegarde ;
- les stratégies de remplacement et de secours ;
- les politiques de slots et de rétention.

Il ne définit pas encore :

- la mémoire vectorielle du chapitre 10 ;
- les services IA des chapitres 11 à 13 ;
- les systèmes de gameplay complets des chapitres 14 à 25 ;
- les campagnes de tests du chapitre 27 ;
- la journalisation générale du chapitre 28 ;
- les scripts Python de migration massive du chapitre 29.

> **Frontière essentielle :** une base SQLite est un mécanisme de persistance spécialisé. Une sauvegarde est un contrat de reconstruction cohérente de la partie.

## 4. Vocabulaire

### 4.1 Snapshot

Un **snapshot** est une photographie logique de l’état nécessaire pour reconstruire une partie à un instant cohérent.

Il ne s’agit pas nécessairement d’une copie brute de toute la mémoire. Il contient seulement les données durables définies par le contrat de sauvegarde.

### 4.2 Slot

Un **slot** est un emplacement nommé et stable qui reçoit une sauvegarde.

Exemples :

- `manual-01` ;
- `manual-02` ;
- `quick-01` ;
- `auto-01`.

### 4.3 Version du format

`format_version` décrit la structure du document de sauvegarde.

Cette version augmente lorsqu’une migration est nécessaire pour qu’un ancien document corresponde au nouveau contrat.

### 4.4 Version du jeu

`game_version` indique la version du jeu qui a créé le fichier. Elle aide au diagnostic, mais ne remplace pas `format_version`.

### 4.5 Migration

Une migration transforme un document ancien en document courant **avant** son application au monde.

### 4.6 Validation

La validation vérifie la structure, les types, les identifiants et les invariants.

Un JSON syntaxiquement valide peut rester inutilisable pour le jeu.

### 4.7 Intégrité

L’intégrité indique que le contenu lu correspond au contenu écrit.

Elle ne garantit ni l’authenticité, ni le chiffrement, ni l’absence de triche.

## 5. Quatre catégories à ne pas confondre

> **[LECTURE] Matrice de séparation — Ne pas saisir.**

```text
Catégorie                  Exemple                         Support principal
-------------------------  ------------------------------  --------------------------
Conception                 BeaconProfile                   .tres dans res://
Configuration              strict_data_validation          .cfg dans res:// / user://
Persistance spécialisée    état courant d’une balise       SQLite dans user://
Snapshot de partie         monde + joueur + fonctionnalités fichier versionné dans user://
```

La base SQLite peut contribuer au snapshot. Elle ne doit pas être copiée aveuglément comme unique format de sauvegarde.

## 6. Choisir le format de référence

Godot permet notamment :

- du texte avec `FileAccess.store_string()` ;
- du binaire avec `FileAccess.store_var()` ;
- des `Resource` avec `ResourceSaver` ;
- des formats personnalisés.

`Project Asteria` choisit d’abord **JSON** pour le document de sauvegarde pédagogique.

Avantages :

- lecture humaine ;
- diffs possibles pendant le développement ;
- validation explicite ;
- migrations faciles à comprendre ;
- indépendance vis-à-vis de la sérialisation automatique des objets ;
- compatibilité avec des outils externes.

Limites :

- fichiers plus volumineux ;
- absence de types comme `Vector3`, `Color` ou `Quaternion` ;
- conversions manuelles ;
- absence de commentaires standard ;
- coût de parsing supérieur à certains formats binaires.

Le passage à un conteneur binaire ou compressé pourra être décidé après mesure, sans changer les contrats de capture et de migration.

## 7. Pourquoi ne pas sérialiser les objets complets

> **[LECTURE] Exemple déconseillé — Ne pas utiliser pour des sauvegardes non fiables.**

```gdscript
file.store_var(player, true)
```

Le paramètre `true` autorise la sérialisation d’objets complets. Un chargement de données non fiables peut alors réintroduire des objets ou du code inattendus.

Le projet choisit :

- des dictionnaires composés de valeurs simples ;
- des conversions explicites ;
- aucun objet complet dans le fichier ;
- aucune confiance accordée à un fichier provenant de l’extérieur.

## 8. Organisation des slots

> **[LECTURE] Arborescence runtime — Ne pas créer dans le dépôt Git.**

```text
user://saves/
├── manual-01.asteria-save.json
├── manual-01.asteria-save.json.bak
├── manual-01.png
├── manual-02.asteria-save.json
├── quick-01.asteria-save.json
├── auto-01.asteria-save.json
├── auto-02.asteria-save.json
└── auto-03.asteria-save.json
```

Le fichier principal contient les métadonnées et le payload. La miniature reste séparée, car une image binaire n’a pas sa place dans le JSON.

### 8.1 Pourquoi éviter un fichier de métadonnées séparé au début

Deux fichiers JSON distincts pour un même slot peuvent diverger après une panne.

Le premier format conserve donc les métadonnées dans le document principal. La liste des slots doit ouvrir et valider chaque en-tête.

Une optimisation par index séparé pourra être ajoutée plus tard avec une stratégie de reconstruction.

## 9. Convention des identifiants de slot

> **[VSC] Visual Studio Code — Créer :** `res://src/core/save/save_slot_id.gd`.

```gdscript
class_name SaveSlotId
extends RefCounted

const PATTERN := "^(manual|auto|quick)-[0-9]{2}$"

static func is_valid(value: StringName) -> bool:
	if value.is_empty():
		return false

	var regex := RegEx.new()
	if regex.compile(PATTERN) != OK:
		push_error("Motif SaveSlotId invalide.")
		return false

	return regex.search(String(value)) != null

static func to_path(value: StringName) -> String:
	if not is_valid(value):
		return ""

	return "user://saves/%s.asteria-save.json" % String(value)
```

### 9.1 Explication

`PATTERN` accepte trois familles et deux chiffres.

`is_valid()` refuse les noms libres qui pourraient contenir `..`, `/` ou `\`.

`to_path()` construit le chemin seulement après validation. Un nom de slot ne doit jamais devenir directement un chemin fourni par l’utilisateur.

## 10. Contrat du document

> **[LECTURE] Exemple JSON — Structure de référence.**

```json
{
  "format": "project-asteria-save",
  "format_version": 2,
  "minimum_reader_version": 1,
  "game_version": "0.1.0",
  "created_at_utc": "2026-07-19T11:30:00",
  "slot": {
    "id": "manual-01",
    "kind": "manual",
    "display_name": "Avant la porte nord"
  },
  "metadata": {
    "play_time_seconds": 1842.5,
    "world_id": "world.training",
    "player_name": "Ariane",
    "thumbnail_file": "manual-01.png"
  },
  "integrity": {
    "algorithm": "sha256",
    "payload_sha256": "..."
  },
  "payload": {
    "world": {},
    "player": {},
    "features": {
      "beacons": {}
    }
  }
}
```

### 10.1 `format`

Cette chaîne identifie la famille du fichier.

Une application ne doit pas tenter de charger n’importe quel JSON comme une sauvegarde Asteria.

### 10.2 `format_version`

La version courante du contrat est `2` dans ce chapitre.

### 10.3 `minimum_reader_version`

Cette valeur documente la plus ancienne version de lecteur compatible avec le fichier. Le lecteur actuel vérifie surtout `format_version`, mais le champ prépare une politique plus fine.

### 10.4 Métadonnées

Les métadonnées servent à l’interface de sélection :

- temps de jeu ;
- monde ;
- nom du personnage ;
- miniature ;
- date de création.

Elles ne doivent pas être utilisées comme source d’autorité pour restaurer le gameplay.

### 10.5 Payload

Le payload contient les sections réellement appliquées au monde.

## 11. Codec des types Godot

JSON ne connaît pas `Vector3`.

> **[VSC] Visual Studio Code — Créer :** `res://src/core/save/save_value_codec.gd`.

```gdscript
class_name SaveValueCodec
extends RefCounted

static func vector3_to_dictionary(value: Vector3) -> Dictionary:
	return {
		"x": value.x,
		"y": value.y,
		"z": value.z,
	}

static func dictionary_to_vector3(
	data: Dictionary,
	errors: PackedStringArray,
	path: String
) -> Vector3:
	for key: String in ["x", "y", "z"]:
		if not data.has(key):
			errors.append("%s.%s est absent" % [path, key])
			return Vector3.ZERO
		if not data[key] is float and not data[key] is int:
			errors.append("%s.%s doit être numérique" % [path, key])
			return Vector3.ZERO

		var number := float(data[key])
		if is_nan(number) or is_inf(number):
			errors.append("%s.%s doit être fini" % [path, key])
			return Vector3.ZERO

	return Vector3(
		float(data["x"]),
		float(data["y"]),
		float(data["z"])
	)
```

### 11.1 Explication

La conversion utilise un dictionnaire explicite plutôt qu’une chaîne `"1,2,3"`.

`errors` collecte plusieurs diagnostics.

`path` indique l’emplacement logique du champ, par exemple `payload.player.position`.

La fonction ne modifie pas le monde. Elle produit une valeur temporaire après validation.

## 12. Représentation canonique pour l’empreinte

Une empreinte doit être calculée sur une représentation déterministe.

> **[VSC] Visual Studio Code — Créer :** `res://src/core/save/canonical_json.gd`.

```gdscript
class_name CanonicalJson
extends RefCounted

const MAX_EXACT_JSON_INTEGER := 9007199254740991.0

static func encode(value: Variant) -> String:
	match typeof(value):
		TYPE_NIL:
			return "null"
		TYPE_BOOL:
			return "true" if bool(value) else "false"
		TYPE_INT, TYPE_FLOAT:
			var number := float(value)
			if is_nan(number) or is_inf(number):
				return ""
			if value is int and absf(number) > MAX_EXACT_JSON_INTEGER:
				return ""
			return JSON.stringify(number, "", true, true)
		TYPE_STRING, TYPE_STRING_NAME:
			return JSON.stringify(String(value))
		TYPE_ARRAY:
			return _encode_array(value as Array)
		TYPE_DICTIONARY:
			return _encode_dictionary(value as Dictionary)
		_:
			return ""

static func _encode_array(values: Array) -> String:
	var parts := PackedStringArray()
	for value: Variant in values:
		var encoded := encode(value)
		if encoded.is_empty():
			return ""
		parts.append(encoded)

	return "[" + ",".join(parts) + "]"

static func _encode_dictionary(values: Dictionary) -> String:
	var normalized: Dictionary[String, Variant] = {}
	for original_key: Variant in values.keys():
		if not original_key is String and not original_key is StringName:
			return ""

		var text_key := String(original_key)
		if normalized.has(text_key):
			return ""
		normalized[text_key] = values[original_key]

	var keys := PackedStringArray(normalized.keys())
	keys.sort()

	var parts := PackedStringArray()
	for key: String in keys:
		var encoded_value := encode(normalized[key])
		if encoded_value.is_empty():
			return ""
		parts.append(
			"%s:%s" % [JSON.stringify(key), encoded_value]
		)

	return "{" + ",".join(parts) + "}"
```

### 12.1 Pourquoi trier les clés

Deux dictionnaires logiquement identiques peuvent avoir été construits dans un ordre différent.

Le tri produit une représentation stable avant SHA-256.

Les entiers et flottants sont tous normalisés vers un nombre JSON en précision complète. Cette règle est nécessaire parce que le parseur JSON restitue les nombres sous une représentation numérique commune. Sans cette normalisation, un compteur entier pourrait produire une empreinte différente après écriture et relecture.

### 12.2 Valeurs refusées

Le codec refuse :

- objets ;
- nœuds ;
- ressources ;
- `Callable` ;
- clés non textuelles ;
- nombres non finis.

La capture doit convertir ces valeurs avant l’écriture.

### 12.3 Limite

Ce codec est un contrat propre au projet, pas un standard universel de JSON canonique.

## 13. Calculer l’empreinte

> **[VSC] Visual Studio Code — Créer :** `res://src/core/save/save_integrity.gd`.

```gdscript
class_name SaveIntegrity
extends RefCounted

static func sha256_payload(payload: Dictionary) -> String:
	var canonical := CanonicalJson.encode(payload)
	if canonical.is_empty():
		return ""

	var context := HashingContext.new()
	if context.start(HashingContext.HASH_SHA256) != OK:
		return ""
	if context.update(canonical.to_utf8_buffer()) != OK:
		return ""

	return context.finish().hex_encode()

static func matches(payload: Dictionary, expected: String) -> bool:
	if expected.length() != 64:
		return false

	var actual := sha256_payload(payload)
	return not actual.is_empty() and actual == expected.to_lower()
```

L’empreinte détecte une modification accidentelle du payload.

Elle ne protège pas contre un attaquant capable de recalculer le hash.

## 14. Contrat d’une section de sauvegarde

Chaque fonctionnalité contribue une section.

> **[VSC] Visual Studio Code — Créer :** `res://src/core/save/save_section.gd`.

```gdscript
class_name SaveSection
extends RefCounted

func key() -> StringName:
	return &""

func capture() -> Dictionary:
	return {}

func validate_data(_data: Dictionary) -> PackedStringArray:
	return PackedStringArray()

func apply_data(_data: Dictionary) -> Error:
	return ERR_UNAVAILABLE
```

### 14.1 Responsabilités

`key()` fournit un identifiant stable.

`capture()` retourne uniquement des valeurs compatibles avec `CanonicalJson`.

`validate_data()` ne modifie rien.

`apply_data()` intervient seulement après la validation globale.

### 14.2 Règle de non-mutation

Toutes les sections sont validées avant le premier appel à `apply_data()`.

Une implémentation complexe doit encore préparer ses objets temporaires avant de remplacer l’état vivant.

## 15. Section des balises

> **[VSC] Visual Studio Code — Créer :** `res://src/features/beacons/infrastructure/beacon_save_section.gd`.

```gdscript
class_name BeaconSaveSection
extends SaveSection

var _repository: BeaconStateRepository
var _runtime_states: Dictionary[StringName, BeaconRuntimeState]

func configure(
	repository: BeaconStateRepository,
	runtime_states: Dictionary[StringName, BeaconRuntimeState]
) -> void:
	_repository = repository
	_runtime_states = runtime_states

func key() -> StringName:
	return &"beacons"

func capture() -> Dictionary:
	var records: Array[Dictionary] = []
	for profile_id: StringName in _runtime_states.keys():
		var state := _runtime_states[profile_id] as BeaconRuntimeState
		if state == null:
			push_error("État runtime invalide : %s" % profile_id)
			return {}
		records.append(
			{
				"profile_id": String(state.profile_id),
				"is_enabled": state.is_enabled,
				"activation_count": state.activation_count,
				"cooldown_remaining": state.cooldown_remaining,
			}
		)

	records.sort_custom(
		func(a: Dictionary, b: Dictionary) -> bool:
			return String(a["profile_id"]) < String(b["profile_id"])
	)

	return {"records": records}

func validate_data(data: Dictionary) -> PackedStringArray:
	var errors := PackedStringArray()
	if not data.has("records") or not data["records"] is Array:
		errors.append("beacons.records doit être un tableau")
		return errors

	var records := data["records"] as Array
	if records.size() > 10000:
		errors.append("beacons.records dépasse la limite de 10 000 entrées")
		return errors

	var seen: Dictionary[StringName, bool] = {}
	for index: int in records.size():
		var value: Variant = records[index]
		if not value is Dictionary:
			errors.append("beacons.records[%d] doit être un objet" % index)
			continue

		var row := value as Dictionary
		var profile_id := StringName(String(row.get("profile_id", "")))
		if not StableId.is_valid(profile_id):
			errors.append("Identifiant de balise invalide à l’index %d" % index)
		elif seen.has(profile_id):
			errors.append("Balise dupliquée : %s" % profile_id)
		else:
			seen[profile_id] = true

		if not (row.get("is_enabled", null) is bool):
			errors.append("is_enabled invalide pour %s" % profile_id)

		var count_value: Variant = row.get("activation_count", null)
		if not _is_non_negative_integer(count_value):
			errors.append("activation_count invalide pour %s" % profile_id)

		var cooldown_value: Variant = row.get("cooldown_remaining", null)
		if not _is_non_negative_number(cooldown_value):
			errors.append("cooldown_remaining invalide pour %s" % profile_id)

	return errors

func _is_non_negative_integer(value: Variant) -> bool:
	if not value is int and not value is float:
		return false

	var number := float(value)
	return (
		not is_nan(number)
		and not is_inf(number)
		and number >= 0.0
		and number <= 9007199254740991.0
		and is_equal_approx(number, floor(number))
	)

func _is_non_negative_number(value: Variant) -> bool:
	if not value is int and not value is float:
		return false

	var number := float(value)
	return not is_nan(number) and not is_inf(number) and number >= 0.0
```

### 15.1 Ordre déterministe

Les lignes sont triées par `profile_id`.

Cet ordre facilite les comparaisons, les empreintes et le diagnostic.

### 15.2 Validation sans application

La méthode ne modifie ni les objets runtime, ni SQLite.

L’application sera ajoutée après la définition du chargement transactionnel.

## 16. Construire le snapshot

> **[VSC] Visual Studio Code — Créer :** `res://src/core/save/save_document_builder.gd`.

```gdscript
class_name SaveDocumentBuilder
extends RefCounted

const FORMAT := "project-asteria-save"
const CURRENT_FORMAT_VERSION := 2
const MINIMUM_READER_VERSION := 1

var _sections: Array[SaveSection] = []

func configure(sections: Array[SaveSection]) -> void:
	_sections = sections

func build(
	slot_id: StringName,
	display_name: String,
	metadata: Dictionary,
	game_version: String
) -> Dictionary:
	if not SaveSlotId.is_valid(slot_id):
		return {}

	var world_value: Variant = metadata.get("world_snapshot", {})
	var player_value: Variant = metadata.get("player_snapshot", {})
	if not world_value is Dictionary or not player_value is Dictionary:
		push_error("Les snapshots world et player doivent être des dictionnaires.")
		return {}

	var feature_payload: Dictionary = {}
	for section: SaveSection in _sections:
		var section_key := String(section.key())
		if section_key.is_empty() or feature_payload.has(section_key):
			push_error("Clé de section absente ou dupliquée : %s" % section_key)
			return {}

		var section_data := section.capture()
		if section_data.is_empty():
			push_error("Capture vide ou invalide : %s" % section_key)
			return {}
		feature_payload[section_key] = section_data

	var payload := {
		"world": world_value as Dictionary,
		"player": player_value as Dictionary,
		"features": feature_payload,
	}

	var payload_hash := SaveIntegrity.sha256_payload(payload)
	if payload_hash.is_empty():
		push_error("Le payload ne peut pas être canonisé.")
		return {}

	return {
		"format": FORMAT,
		"format_version": CURRENT_FORMAT_VERSION,
		"minimum_reader_version": MINIMUM_READER_VERSION,
		"game_version": game_version,
		"created_at_utc": Time.get_datetime_string_from_system(true, false),
		"slot": {
			"id": String(slot_id),
			"kind": String(slot_id).get_slice("-", 0),
			"display_name": display_name.strip_edges(),
		},
		"metadata": {
			"play_time_seconds": maxf(
				0.0,
				float(metadata.get("play_time_seconds", 0.0))
			),
			"world_id": String(metadata.get("world_id", "")),
			"player_name": String(metadata.get("player_name", "")),
			"thumbnail_file": String(metadata.get("thumbnail_file", "")),
		},
		"integrity": {
			"algorithm": "sha256",
			"payload_sha256": payload_hash,
		},
		"payload": payload,
	}
```

### 16.1 Barrière de capture

`build()` suppose que l’appelant a établi une barrière logique :

- entrées de gameplay suspendues ;
- simulations mutables stabilisées ;
- transactions persistantes terminées ;
- capture effectuée sur le thread principal lorsque les objets Godot l’exigent.

Sans cette barrière, le joueur pourrait être capturé dans une zone tandis que son inventaire correspond déjà à l’instant suivant.

### 16.2 Métadonnées et payload

`world_snapshot` et `player_snapshot` sont retirés du dictionnaire de métadonnées avant l’écriture finale.

Ils appartiennent au payload, pas à l’écran de sélection.

## 17. Validation du document

> **[VSC] Visual Studio Code — Créer :** `res://src/core/save/save_document_validator.gd`.

```gdscript
class_name SaveDocumentValidator
extends RefCounted

const EXPECTED_FORMAT := "project-asteria-save"
const CURRENT_FORMAT_VERSION := 2

func validate_envelope(document: Dictionary) -> PackedStringArray:
	var errors := PackedStringArray()

	if String(document.get("format", "")) != EXPECTED_FORMAT:
		errors.append("Format de sauvegarde inconnu")

	var version_value: Variant = document.get("format_version", null)
	var version := -1
	if version_value is int or version_value is float:
		var version_number := float(version_value)
		if (
			not is_nan(version_number)
			and not is_inf(version_number)
			and is_equal_approx(version_number, floor(version_number))
		):
			version = int(version_number)

	if version < 1:
		errors.append("format_version absent ou invalide")
	elif version > CURRENT_FORMAT_VERSION:
		errors.append(
			"Sauvegarde future : version %d, lecteur %d"
			% [version, CURRENT_FORMAT_VERSION]
		)

	for key: String in ["slot", "metadata", "integrity", "payload"]:
		if not document.get(key, null) is Dictionary:
			errors.append("%s doit être un objet" % key)

	if not errors.is_empty():
		return errors

	var slot := document["slot"] as Dictionary
	var slot_id := StringName(String(slot.get("id", "")))
	if not SaveSlotId.is_valid(slot_id):
		errors.append("Identifiant de slot invalide")

	var integrity := document["integrity"] as Dictionary
	if String(integrity.get("algorithm", "")) != "sha256":
		errors.append("Algorithme d’intégrité non pris en charge")
	else:
		var payload := document["payload"] as Dictionary
		var expected := String(integrity.get("payload_sha256", ""))
		if not SaveIntegrity.matches(payload, expected):
			errors.append("Empreinte du payload invalide")

	return errors

func validate_current_payload(document: Dictionary) -> PackedStringArray:
	var errors := PackedStringArray()
	if int(document.get("format_version", -1)) != CURRENT_FORMAT_VERSION:
		errors.append("Le document n’est pas au format courant")
		return errors

	if not document.get("payload", null) is Dictionary:
		errors.append("payload doit être un objet")
		return errors

	var payload := document["payload"] as Dictionary
	for key: String in ["world", "player", "features"]:
		if not payload.get(key, null) is Dictionary:
			errors.append("payload.%s doit être un objet" % key)

	if not errors.is_empty():
		return errors

	var world := payload["world"] as Dictionary
	var world_id := StringName(String(world.get("id", "")))
	if not StableId.is_valid(world_id):
		errors.append("payload.world.id est invalide")

	var player := payload["player"] as Dictionary
	if not player.get("position", null) is Dictionary:
		errors.append("payload.player.position doit être un objet")
	else:
		var position_errors := PackedStringArray()
		SaveValueCodec.dictionary_to_vector3(
			player["position"] as Dictionary,
			position_errors,
			"payload.player.position"
		)
		errors.append_array(position_errors)

	return errors
```

### 17.1 Refus des versions futures

Le document est refusé avant toute migration ou application.

Un ancien programme ne doit pas deviner la signification d’un nouveau format.

### 17.2 Validation en couches

La validation complète suit cet ordre :

1. syntaxe JSON ;
2. enveloppe ;
3. version ;
4. empreinte ;
5. migrations ;
6. sections métier ;
7. préparation du monde cible ;
8. application.

## 18. Lire un document sans modifier le monde

> **[VSC] Visual Studio Code — Créer :** `res://src/core/save/save_document_reader.gd`.

```gdscript
class_name SaveDocumentReader
extends RefCounted

const MAX_SAVE_BYTES := 16 * 1024 * 1024

func read(path: String) -> Dictionary:
	if not FileAccess.file_exists(path):
		push_error("Sauvegarde absente : %s" % path)
		return {}

	var file_size := FileAccess.get_size(path)
	if file_size < 1 or file_size > MAX_SAVE_BYTES:
		push_error("Taille de sauvegarde refusée : %d octets" % file_size)
		return {}

	var file := FileAccess.open(path, FileAccess.READ)
	if file == null:
		push_error(
			"Ouverture impossible : %s"
			% error_string(FileAccess.get_open_error())
		)
		return {}

	var text := file.get_as_text()
	file.close()

	var json := JSON.new()
	var error := json.parse(text)
	if error != OK:
		push_error(
			"JSON invalide, ligne %d : %s"
			% [json.get_error_line(), json.get_error_message()]
		)
		return {}

	if not json.data is Dictionary:
		push_error("La racine de sauvegarde doit être un objet.")
		return {}

	return json.data as Dictionary
```

Une erreur retourne un dictionnaire vide et publie un diagnostic. Le service appelant doit conserver un code d’erreur distinct s’il doit différencier absence, corruption et refus de version.

## 19. Écriture temporaire et remplacement contrôlé

Godot documente `DirAccess.rename_absolute()` comme une opération de renommage ou déplacement pouvant écraser une destination accessible. La documentation ne promet pas une atomicité identique sur toutes les plateformes.

Le chapitre emploie donc l’expression **remplacement contrôlé**, et non « garantie atomique universelle ».

> **[VSC] Visual Studio Code — Créer :** `res://src/core/save/save_file_store.gd`.

```gdscript
class_name SaveFileStore
extends RefCounted

func write_document(path: String, document: Dictionary) -> Error:
	if not path.begins_with("user://saves/"):
		return ERR_INVALID_PARAMETER

	var directory_error := DirAccess.make_dir_recursive_absolute(
		path.get_base_dir()
	)
	if directory_error != OK and directory_error != ERR_ALREADY_EXISTS:
		return directory_error

	var text := JSON.stringify(document, "\t", true, true)
	var temporary_path := path + ".tmp"
	var backup_path := path + ".bak"

	var write_error := _write_text(temporary_path, text)
	if write_error != OK:
		_remove_if_exists(temporary_path)
		return write_error

	var reader := SaveDocumentReader.new()
	var written_document := reader.read(temporary_path)
	if written_document.is_empty():
		_remove_if_exists(temporary_path)
		return ERR_FILE_CORRUPT

	var validator := SaveDocumentValidator.new()
	if not validator.validate_envelope(written_document).is_empty():
		_remove_if_exists(temporary_path)
		return ERR_FILE_CORRUPT

	if FileAccess.file_exists(path):
		var current_document := reader.read(path)
		if _is_future_document(current_document):
			_remove_if_exists(temporary_path)
			push_error("Un build ancien refuse d’écraser une sauvegarde future.")
			return ERR_UNAVAILABLE

		var current_errors := validator.validate_envelope(current_document)
		if not current_document.is_empty() and current_errors.is_empty():
			var backup_error := DirAccess.copy_absolute(path, backup_path)
			if backup_error != OK:
				_remove_if_exists(temporary_path)
				return backup_error
		else:
			push_warning(
				"Le fichier principal existant est invalide ; "
				+ "la copie .bak actuelle est conservée."
			)

	var replace_error := DirAccess.rename_absolute(temporary_path, path)
	if replace_error != OK:
		_remove_if_exists(temporary_path)
		return replace_error

	return OK

func _write_text(path: String, text: String) -> Error:
	var file := FileAccess.open(path, FileAccess.WRITE)
	if file == null:
		return FileAccess.get_open_error()

	if not file.store_string(text):
		file.close()
		return ERR_FILE_CANT_WRITE

	file.flush()
	file.close()
	return OK

func _remove_if_exists(path: String) -> void:
	if FileAccess.file_exists(path):
		var error := DirAccess.remove_absolute(path)
		if error != OK:
			push_warning("Nettoyage impossible : %s" % path)
```

### 19.1 Ordre des opérations

1. créer le dossier ;
2. sérialiser ;
3. écrire dans `.tmp` ;
4. appeler `flush()` ;
5. fermer ;
6. relire ;
7. analyser et valider ;
8. copier l’ancien fichier vers `.bak` ;
9. renommer `.tmp` vers la cible.

### 19.2 Ce que `flush()` garantit

`flush()` écrit le tampon du fichier sur le disque. La documentation Godot précise que la fermeture effectue déjà un flush, mais l’appel explicite rend la barrière visible avant le remplacement.

Le chapitre ne prétend pas que cette opération protège contre toute panne matérielle, cache de contrôleur ou particularité du système de fichiers.

### 19.3 Même dossier

Le fichier temporaire reste dans le même dossier que la cible. Cela évite un déplacement entre volumes et favorise un remplacement local.

### 19.4 Copie de secours

La copie `.bak` conserve la dernière version précédemment validée.

Elle ne doit être remplacée qu’après validation du nouveau `.tmp`.

## 20. Politique de récupération

Lorsqu’un slot principal échoue :

1. ne rien appliquer ;
2. essayer le fichier `.bak` ;
3. valider l’enveloppe et l’empreinte ;
4. migrer en mémoire ;
5. valider les sections ;
6. proposer la récupération au joueur ;
7. ne pas écraser immédiatement le fichier corrompu.

> **[VSC] Visual Studio Code — Ajouter :** dans `save_file_store.gd`.

```gdscript
func read_with_backup(path: String) -> Dictionary:
	var reader := SaveDocumentReader.new()
	var validator := SaveDocumentValidator.new()

	var primary := reader.read(path)
	if not primary.is_empty():
		if _is_future_document(primary):
			push_error("Sauvegarde créée par une version plus récente.")
			return {}

		var errors := validator.validate_envelope(primary)
		if errors.is_empty():
			return primary

	var backup_path := path + ".bak"
	var backup := reader.read(backup_path)
	if backup.is_empty() or _is_future_document(backup):
		return {}

	var backup_errors := validator.validate_envelope(backup)
	if not backup_errors.is_empty():
		return {}

	push_warning("Le slot principal est invalide ; la copie de secours est utilisée.")
	return backup

func _is_future_document(document: Dictionary) -> bool:
	var value: Variant = document.get("format_version", null)
	if not value is int and not value is float:
		return false

	var number := float(value)
	if is_nan(number) or is_inf(number):
		return false
	if not is_equal_approx(number, floor(number)):
		return false

	return int(number) > SaveDocumentValidator.CURRENT_FORMAT_VERSION
```

L’interface doit informer le joueur qu’une récupération a eu lieu.

## 21. Migrations de sauvegarde

Les migrations SQLite modifient un schéma relationnel. Les migrations de sauvegarde transforment un document en mémoire.

> **V1 :** le joueur possède `position_x`, `position_y`, `position_z`.  
> **V2 :** le joueur possède `position: {x, y, z}`.

### 21.1 Contrat d’une migration

> **[VSC] Visual Studio Code — Créer :** `res://src/core/save/save_migration.gd`.

```gdscript
class_name SaveMigration
extends RefCounted

func from_version() -> int:
	return -1

func to_version() -> int:
	return -1

func migrate(_document: Dictionary) -> Error:
	return ERR_UNAVAILABLE
```

### 21.2 Migration V1 vers V2

> **[VSC] Visual Studio Code — Créer :** `res://src/core/save/save_migration_v1_to_v2.gd`.

```gdscript
class_name SaveMigrationV1ToV2
extends SaveMigration

func from_version() -> int:
	return 1

func to_version() -> int:
	return 2

func migrate(document: Dictionary) -> Error:
	if not document.get("payload", null) is Dictionary:
		return ERR_INVALID_DATA

	var payload := document["payload"] as Dictionary
	if not payload.get("player", null) is Dictionary:
		return ERR_INVALID_DATA

	var player := payload["player"] as Dictionary
	for key: String in ["position_x", "position_y", "position_z"]:
		if not player.has(key):
			return ERR_INVALID_DATA
		if not player[key] is float and not player[key] is int:
			return ERR_INVALID_DATA

	player["position"] = {
		"x": float(player["position_x"]),
		"y": float(player["position_y"]),
		"z": float(player["position_z"]),
	}
	player.erase("position_x")
	player.erase("position_y")
	player.erase("position_z")

	document["format_version"] = 2
	return OK
```

### 21.3 Recalculer l’empreinte après migration

Une migration modifie le payload. L’empreinte enregistrée correspond à l’ancien document.

Le runner :

1. vérifie l’empreinte avant migration ;
2. migre une copie en mémoire ;
3. recalcule l’empreinte de la copie ;
4. valide le format courant ;
5. n’écrit pas automatiquement le fichier.

L’ancien fichier reste intact jusqu’à une sauvegarde ultérieure explicite.

## 22. Runner de migrations

> **[VSC] Visual Studio Code — Créer :** `res://src/core/save/save_migration_runner.gd`.

```gdscript
class_name SaveMigrationRunner
extends RefCounted

const CURRENT_FORMAT_VERSION := 2

var _migrations: Dictionary[int, SaveMigration] = {}

func _init() -> void:
	var error := register_migration(SaveMigrationV1ToV2.new())
	if error != OK:
		push_error("Enregistrement de la migration V1 vers V2 impossible.")

func register_migration(migration: SaveMigration) -> Error:
	if migration == null:
		return ERR_INVALID_PARAMETER
	if migration.to_version() != migration.from_version() + 1:
		return ERR_INVALID_DATA
	if _migrations.has(migration.from_version()):
		return ERR_ALREADY_EXISTS

	_migrations[migration.from_version()] = migration
	return OK

func migrate_to_current(source: Dictionary) -> Dictionary:
	var document := source.duplicate(true)
	var version := int(document.get("format_version", -1))
	if version < 1 or version > CURRENT_FORMAT_VERSION:
		return {}

	while version < CURRENT_FORMAT_VERSION:
		if not _migrations.has(version):
			push_error("Migration de sauvegarde absente depuis %d" % version)
			return {}

		var migration := _migrations[version]
		if migration.migrate(document) != OK:
			push_error("Migration de sauvegarde échouée depuis %d" % version)
			return {}

		version = migration.to_version()

	if not document.get("payload", null) is Dictionary:
		return {}

	var payload := document["payload"] as Dictionary
	var payload_hash := SaveIntegrity.sha256_payload(payload)
	if payload_hash.is_empty():
		return {}

	document["integrity"] = {
		"algorithm": "sha256",
		"payload_sha256": payload_hash,
	}
	return document
```

### 22.1 Continuité obligatoire

Une migration passe de `N` vers `N + 1`.

Les sauts directs compliquent les combinaisons et les tests.

### 22.2 Copie profonde

`source.duplicate(true)` protège le dictionnaire original pendant la transformation.

### 22.3 Append-only

Une migration livrée ne doit pas être réécrite pour changer son sens.

Une correction ajoute une nouvelle version.

## 23. Validation des sections

> **[VSC] Visual Studio Code — Créer :** `res://src/core/save/save_section_registry.gd`.

```gdscript
class_name SaveSectionRegistry
extends RefCounted

var _sections: Dictionary[StringName, SaveSection] = {}

func register(section: SaveSection) -> Error:
	if section == null or section.key().is_empty():
		return ERR_INVALID_PARAMETER
	if _sections.has(section.key()):
		return ERR_ALREADY_EXISTS

	_sections[section.key()] = section
	return OK

func validate_features(features: Dictionary) -> PackedStringArray:
	var errors := PackedStringArray()

	for key: StringName in _sections.keys():
		var serialized_key := String(key)
		if not features.get(serialized_key, null) is Dictionary:
			errors.append("Section absente ou invalide : %s" % key)
			continue

		var section_errors := _sections[key].validate_data(
			features[serialized_key] as Dictionary
		)
		for message: String in section_errors:
			errors.append("%s : %s" % [key, message])

	for serialized_key: Variant in features.keys():
		if not serialized_key is String and not serialized_key is StringName:
			errors.append("Une clé de section n’est pas textuelle")
			continue
		if not _sections.has(StringName(String(serialized_key))):
			errors.append("Section inconnue : %s" % serialized_key)

	return errors

func apply_features(features: Dictionary) -> Error:
	for key: StringName in _sections.keys():
		var serialized_key := String(key)
		var error := _sections[key].apply_data(
			features[serialized_key] as Dictionary
		)
		if error != OK:
			return error

	return OK
```

### 23.1 Sections inconnues

Le format courant peut choisir :

- mode strict : refuser toute section inconnue ;
- mode compatible : ignorer une section déclarée optionnelle ;
- mode diagnostic : afficher puis refuser.

`Project Asteria` utilise le mode strict pour les sections obligatoires. Les sections optionnelles devront être déclarées explicitement dans une évolution du format.

## 24. Appliquer la section des balises

> **[VSC] Visual Studio Code — Ajouter :** dans `beacon_save_section.gd`.

```gdscript
func apply_data(data: Dictionary) -> Error:
	if _repository == null:
		return ERR_UNCONFIGURED

	var validation_errors := validate_data(data)
	if not validation_errors.is_empty():
		return ERR_INVALID_DATA

	var prepared: Array[BeaconStateRecord] = []
	for value: Variant in data["records"]:
		var row := value as Dictionary
		prepared.append(
			BeaconStateRecord.new(
				StringName(String(row["profile_id"])),
				bool(row["is_enabled"]),
				int(row["activation_count"]),
				float(row["cooldown_remaining"]),
				"",
				Time.get_datetime_string_from_system(true, false)
			)
		)

	for record: BeaconStateRecord in prepared:
		var error := _repository.save(record)
		if error != OK:
			return error

		var runtime_state := _runtime_states.get(record.profile_id) as BeaconRuntimeState
		if runtime_state != null:
			error = record.apply_to(runtime_state)
			if error != OK:
				return error

	return OK
```

### 24.1 Réserve transactionnelle

L’exemple prépare tous les records avant l’écriture, mais plusieurs appels `save()` doivent être enveloppés dans une transaction de repository pour garantir un lot atomique.

Le chapitre 8 a présenté les transactions. Le Starter Kit devra ajouter une méthode de lot ou un Unit of Work avant de qualifier ce chemin en `runtime-tested`.

### 24.2 Ordre d’application

La base persistante est mise à jour avant les objets runtime.

Une erreur empêche de considérer le chargement comme réussi.

## 25. Chargement en plusieurs phases

Un chargement ne doit jamais appliquer le premier champ valide dès sa lecture.

Séquence de référence :

> **[LECTURE] Pipeline de chargement — Ne pas saisir.**

```text
sélection du slot
    ↓
lecture du fichier principal ou .bak
    ↓
parse JSON
    ↓
validation de l’enveloppe et de l’empreinte
    ↓
refus des versions futures
    ↓
migration d’une copie en mémoire
    ↓
validation du format courant
    ↓
validation de toutes les sections
    ↓
préchargement du monde cible
    ↓
création d’un monde temporaire
    ↓
application des sections
    ↓
bascule vers le nouveau monde
    ↓
libération de l’ancien monde
```

L’ancien monde doit rester disponible aussi longtemps que possible.

## 26. Coordinateur de sauvegarde et chargement

> **[VSC] Visual Studio Code — Créer :** `res://src/core/save/save_coordinator.gd`.

```gdscript
class_name SaveCoordinator
extends RefCounted

var _builder: SaveDocumentBuilder
var _store: SaveFileStore
var _validator: SaveDocumentValidator
var _migrations: SaveMigrationRunner
var _sections: SaveSectionRegistry
var _save_in_progress := false
var _load_in_progress := false

func configure(
	builder: SaveDocumentBuilder,
	store: SaveFileStore,
	validator: SaveDocumentValidator,
	migrations: SaveMigrationRunner,
	sections: SaveSectionRegistry
) -> void:
	_builder = builder
	_store = store
	_validator = validator
	_migrations = migrations
	_sections = sections

func save_slot(
	slot_id: StringName,
	display_name: String,
	metadata: Dictionary,
	game_version: String
) -> Error:
	if _save_in_progress or _load_in_progress:
		return ERR_BUSY
	if not _is_configured():
		return ERR_UNCONFIGURED

	_save_in_progress = true
	var document := _builder.build(
		slot_id,
		display_name,
		metadata,
		game_version
	)
	if document.is_empty():
		_save_in_progress = false
		return ERR_INVALID_DATA

	var path := SaveSlotId.to_path(slot_id)
	var error := _store.write_document(path, document)
	_save_in_progress = false
	return error

func load_slot(slot_id: StringName) -> Dictionary:
	if _save_in_progress or _load_in_progress:
		return {}
	if not _is_configured():
		return {}

	_load_in_progress = true
	var path := SaveSlotId.to_path(slot_id)
	var source := _store.read_with_backup(path)
	if source.is_empty():
		_load_in_progress = false
		return {}

	var envelope_errors := _validator.validate_envelope(source)
	if not envelope_errors.is_empty():
		_load_in_progress = false
		return {}

	var migrated := _migrations.migrate_to_current(source)
	if migrated.is_empty():
		_load_in_progress = false
		return {}

	var current_errors := _validator.validate_envelope(migrated)
	current_errors.append_array(
		_validator.validate_current_payload(migrated)
	)
	if not current_errors.is_empty():
		_load_in_progress = false
		return {}

	var slot := migrated["slot"] as Dictionary
	var document_slot := StringName(String(slot.get("id", "")))
	if document_slot != slot_id:
		push_error("Le contenu du slot ne correspond pas au fichier demandé.")
		_load_in_progress = false
		return {}

	var payload := migrated["payload"] as Dictionary
	var features := payload.get("features", {}) as Dictionary
	var section_errors := _sections.validate_features(features)
	if not section_errors.is_empty():
		_load_in_progress = false
		return {}

	return migrated

func finish_apply(document: Dictionary) -> Error:
	if not _load_in_progress:
		return ERR_UNCONFIGURED
	if document.is_empty():
		_load_in_progress = false
		return ERR_INVALID_PARAMETER

	var payload := document["payload"] as Dictionary
	var features := payload["features"] as Dictionary
	var error := _sections.apply_features(features)
	_load_in_progress = false
	return error

func cancel_load() -> void:
	_load_in_progress = false

func _is_configured() -> bool:
	return (
		_builder != null
		and _store != null
		and _validator != null
		and _migrations != null
		and _sections != null
	)
```

### 26.1 Pourquoi `load_slot()` ne modifie pas le monde

La méthode retourne un document migré et validé tout en conservant le verrou de chargement.

Le contrôleur de transition doit ensuite :

1. précharger le monde ;
2. créer les objets cibles ;
3. appliquer le document ;
4. appeler `finish_apply()` puis basculer l’affichage ;
5. appeler `cancel_load()` si la préparation du monde échoue.

`finish_apply()` applique ici les sections de fonctionnalités. Le contrôleur du monde reste responsable de la position du joueur, de la scène cible et de la bascule entre ancien et nouveau monde.

### 26.2 Verrou logique

`_save_in_progress` et `_load_in_progress` évitent deux opérations concurrentes dans ce service.

Le verrou de chargement reste actif entre `load_slot()` et `finish_apply()` ou `cancel_load()`. Une implémentation asynchrone devra garantir l’appel de l’une de ces deux sorties dans tous les chemins d’erreur.

## 27. Bootstrap

> **[VSC] Visual Studio Code — Créer :** `res://src/app/save_bootstrap.gd`.

```gdscript
class_name SaveBootstrap
extends RefCounted

func build(
	beacon_repository: BeaconStateRepository,
	runtime_states: Dictionary[StringName, BeaconRuntimeState]
) -> SaveCoordinator:
	var beacon_section := BeaconSaveSection.new()
	beacon_section.configure(beacon_repository, runtime_states)

	var sections: Array[SaveSection] = [beacon_section]

	var builder := SaveDocumentBuilder.new()
	builder.configure(sections)

	var registry := SaveSectionRegistry.new()
	for section: SaveSection in sections:
		var error := registry.register(section)
		if error != OK:
			push_error("Enregistrement de section impossible.")
			return null

	var coordinator := SaveCoordinator.new()
	coordinator.configure(
		builder,
		SaveFileStore.new(),
		SaveDocumentValidator.new(),
		SaveMigrationRunner.new(),
		registry
	)
	return coordinator
```

Le bootstrap est le point de composition. Aucune scène de gameplay ne construit directement les services de fichier.

## 28. Types de sauvegarde

### 28.1 Slot manuel

Le joueur choisit l’emplacement et le nom d’affichage.

Politique recommandée :

- plusieurs slots ;
- confirmation avant écrasement ;
- jamais de remplacement silencieux par un autosave.

### 28.2 Quicksave

Un seul slot ou un petit anneau.

Le quicksave est pratique, mais ne doit pas supprimer les sauvegardes manuelles.

### 28.3 Autosave

L’autosave se déclenche à des points sûrs :

- fin de transition ;
- repos ;
- validation d’une quête ;
- entrée dans une zone stable ;
- intervalle raisonnable hors combat.

Éviter un autosave pendant :

- une transaction de gameplay incomplète ;
- une cinématique critique ;
- une phase de mort non résolue ;
- une migration de données ;
- une écriture précédente.

### 28.4 Checkpoint

Un checkpoint peut être invisible et lié à une séquence précise.

Il ne remplace pas nécessairement le système de slots du joueur.

## 29. Rotation et rétention

Politique Solo de référence :

> **[LECTURE] Politique initiale — Ne pas saisir.**

```text
manual : 10 slots conservés
quick  : 1 slot principal + 1 copie .bak
auto   : 3 slots en rotation
```

Rotation autosave :

> **[LECTURE] Exemple de rotation — Ne pas saisir.**

```text
auto-01 ← nouvelle sauvegarde
auto-02 ← ancien auto-01
auto-03 ← ancien auto-02
```

Une rotation doit copier ou renommer seulement des fichiers déjà validés.

Le projet ne supprime jamais une sauvegarde manuelle pour libérer un autosave.

## 30. Miniatures

La miniature est un confort d’interface, pas une donnée nécessaire au chargement.

Politique :

- format PNG ou WebP selon décision du projet ;
- nom dérivé du slot validé ;
- dimension limitée ;
- absence tolérée ;
- échec de miniature non bloquant pour le snapshot ;
- chemin relatif ou nom simple dans les métadonnées ;
- aucune lecture d’un chemin arbitraire fourni par le fichier.

La capture d’image et l’interface complète seront matérialisées dans le Starter Kit.

## 31. Liste des slots

Un écran de sélection doit afficher :

- nom du slot ;
- type ;
- date ;
- temps de jeu ;
- monde ;
- personnage ;
- version du format ;
- état : valide, récupérable, futur, corrompu ;
- présence de la miniature.

Il ne doit pas appliquer le payload pour afficher cette liste.

Un lecteur d’en-tête peut réutiliser la validation de l’enveloppe sans créer le monde.

## 32. Gestion des versions futures

Lorsqu’un fichier indique une version supérieure :

- ne pas migrer ;
- ne pas réécrire ;
- ne pas remplacer par `.bak` automatiquement ;
- afficher « sauvegarde créée par une version plus récente » ;
- conserver le fichier intact ;
- permettre une copie ou un export de diagnostic.

La rétrocompatibilité permet au nouveau jeu de lire l’ancien fichier.

La compatibilité descendante — ancien jeu lisant un nouveau fichier — n’est pas garantie.

## 33. Fichiers corrompus ou incomplets

Cas possibles :

- JSON tronqué ;
- racine non dictionnaire ;
- champ obligatoire absent ;
- hash incorrect ;
- type invalide ;
- slot incohérent ;
- migration absente ;
- identifiant métier inconnu ;
- copie `.tmp` abandonnée après une panne.

Au démarrage, le service peut supprimer les `.tmp` anciens après journalisation, mais ne doit jamais les traiter comme des slots valides.

## 34. Sécurité

Une sauvegarde est une entrée non fiable.

Règles :

- aucune exécution de code ;
- aucun chemin arbitraire ;
- aucune ressource chargée depuis un chemin fourni sans liste autorisée ;
- aucune concaténation SQL ;
- limites de taille ;
- limites de nombre d’éléments ;
- entiers JSON limités à la plage exacte de 53 bits lorsqu’une précision entière est requise ;
- validation des nombres ;
- refus de `NaN` et de l’infini ;
- pas de secret dans le fichier ;
- pas de désérialisation d’objets complets.

La triche locale n’est pas traitée comme un problème cryptographique dans ce chapitre.

## 35. Erreurs fréquentes, pièges et corrections

<!-- qa:error-correction-section -->

### 35.1 Copier directement la base SQLite comme sauvegarde

**Symptôme :** le slot dépend de fichiers WAL ouverts et ne représente pas les autres systèmes.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
DirAccess.copy_absolute(
	"user://data/asteria.sqlite3",
	"user://saves/manual-01.sqlite3"
)
```

**Correction :** construire un snapshot logique avec les repositories et les sections.

> **[LECTURE] Architecture corrigée — Étudier avant adaptation.**

```text
repositories + runtime
        ↓
SaveSection.capture()
        ↓
document versionné
```

**Différence :** le fichier SQLite reste une persistance interne ; le snapshot devient un contrat de reconstruction indépendant de l’état d’une connexion.

### 35.2 Écrire directement dans le fichier final

**Symptôme :** une panne pendant l’écriture peut tronquer la seule copie.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var file := FileAccess.open(path, FileAccess.WRITE)
file.store_string(JSON.stringify(document))
```

**Correction :** écrire, fermer, relire et valider un `.tmp` avant remplacement.

> **[LECTURE] Flux corrigé — Étudier avant adaptation.**

```text
.tmp → validation → .bak → remplacement de la cible
```

**Différence :** le fichier final précédent reste disponible tant que le temporaire n’a pas réussi les contrôles.

### 35.3 Promettre une atomicité universelle

**Symptôme :** la documentation affirme qu’un renommage protège contre toutes les pannes et plateformes.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
rename_absolute() garantit toujours une sauvegarde atomique.
```

**Correction :** parler de remplacement contrôlé et tester chaque plateforme.

> **[LECTURE] Formulation corrigée — Référence rédactionnelle.**

```text
Le fichier temporaire est renommé dans le même dossier.
La robustesse exacte doit être qualifiée sur chaque plateforme cible.
```

**Différence :** la correction ne revendique pas une garantie absente de la documentation officielle.

### 35.4 Appliquer avant validation complète

**Symptôme :** le joueur est déplacé, puis une section d’inventaire échoue.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
player.global_position = decoded_position
validate_inventory(document["payload"]["inventory"])
```

**Correction :** valider toutes les sections, préparer le monde, puis appliquer.

> **[LECTURE] Ordre corrigé — Étudier avant adaptation.**

```text
parse → migrer → valider tout → préparer → appliquer → basculer
```

**Différence :** aucune donnée du monde actif n’est modifiée pendant les contrôles.

### 35.5 Confondre version du jeu et version du format

**Symptôme :** chaque patch du jeu déclenche une migration inutile.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```json
{
  "format_version": "0.1.37"
}
```

**Correction :** séparer un entier structurel et une version d’application.

> **[LECTURE] Exemple corrigé — Référence.**

```json
{
  "format_version": 2,
  "game_version": "0.1.37"
}
```

**Différence :** `format_version` change seulement lorsque la structure exige une migration.

### 35.6 Modifier une ancienne migration

**Symptôme :** deux installations produisent des documents différents pour la même version.

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```text
Modifier SaveMigrationV1ToV2 après publication.
```

**Correction :** ajouter `SaveMigrationV2ToV3`.

> **[LECTURE] Historique corrigé — Référence.**

```text
V1 → V2 : immuable
V2 → V3 : nouvelle correction
```

**Différence :** tous les utilisateurs parcourent le même historique.

### 35.7 Utiliser le nom affiché comme clé de section

**Symptôme :** une traduction casse le chargement.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
func key() -> StringName:
	return &"Balises activées"
```

**Correction :** utiliser un identifiant stable non traduit.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
func key() -> StringName:
	return &"beacons"
```

**Différence :** l’identité du contrat ne dépend plus de l’interface.

### 35.8 Accepter n’importe quel chemin de miniature

**Symptôme :** un fichier modifié tente de lire un emplacement arbitraire.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var texture := load(document["metadata"]["thumbnail_file"])
```

**Correction :** dériver le chemin depuis le slot validé.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
var thumbnail_path := (
	"user://saves/%s.png" % String(validated_slot_id)
)
```

**Différence :** le fichier ne contrôle plus le dossier lu.

### 35.9 Traiter un hash comme un chiffrement

**Symptôme :** le guide affirme empêcher la triche avec SHA-256.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
Le hash rend la sauvegarde secrète et impossible à modifier.
```

**Correction :** présenter le hash comme un contrôle d’intégrité accidentelle.

> **[LECTURE] Formulation corrigée — Référence.**

```text
SHA-256 détecte une modification du payload si l’empreinte
n’a pas été recalculée. Il ne chiffre pas le contenu.
```

**Différence :** la propriété réelle du mécanisme est correctement décrite.

### 35.10 Lancer deux sauvegardes concurrentes

**Symptôme :** deux écritures utilisent le même `.tmp`.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
save_slot(&"auto-01")
save_slot(&"auto-01")
```

**Correction :** refuser l’opération lorsque le coordinateur est occupé.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
if save_coordinator.save_slot(...) == ERR_BUSY:
	push_warning("Une opération de sauvegarde est déjà en cours.")
```

**Différence :** un seul propriétaire écrit le slot à un instant donné.

### 35.11 Écraser le fichier corrompu dès la récupération

**Symptôme :** le diagnostic original disparaît.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var recovered := read_backup()
write_document(primary_path, recovered)
```

**Correction :** charger la copie en mémoire et demander une sauvegarde ultérieure.

> **[LECTURE] Flux corrigé — Référence.**

```text
.bak validé → partie restaurée → information au joueur
→ nouvelle sauvegarde explicite
```

**Différence :** le fichier corrompu reste disponible pour l’analyse jusqu’à une décision claire.

### 35.12 Sauvegarder pendant un état incohérent

**Symptôme :** le monde et l’inventaire correspondent à deux instants différents.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
capture_world()
await get_tree().process_frame
capture_inventory()
```

**Correction :** établir une barrière de capture et produire toutes les sections dans le même cycle logique.

> **[LECTURE] Flux corrigé — Référence.**

```text
suspendre mutations → terminer transactions → capturer toutes
les sections → reprendre la simulation
```

**Différence :** le snapshot représente un seul instant logique.

## 36. Diagnostic

### 36.1 La sauvegarde n’apparaît pas

Vérifier :

- le slot ;
- le chemin `user://saves/` ;
- l’erreur de `FileAccess.open()` ;
- les permissions ;
- le résultat de `store_string()` ;
- la validation du `.tmp`.

### 36.2 Le chargement utilise `.bak`

Le fichier principal a échoué :

- parse ;
- validation ;
- empreinte ;
- version.

Conserver le diagnostic et informer le joueur.

### 36.3 Migration absente

Le fichier est ancien, mais le runner ne possède pas la transition suivante.

Ne pas sauter la version. Ajouter la migration manquante.

### 36.4 Section absente

Le registre attend une fonctionnalité obligatoire que le document ne contient pas.

Décider explicitement si la section doit :

- être obligatoire ;
- recevoir une valeur par défaut via migration ;
- devenir optionnelle dans un futur format.

### 36.5 Hash divergent après migration

L’empreinte doit être vérifiée **avant** la migration, puis recalculée sur la copie migrée.

Ne pas comparer l’ancien hash au nouveau payload.

## 37. Parcours Solo

Le parcours Solo peut retenir :

- JSON lisible ;
- dix slots manuels ;
- un quicksave ;
- trois autosaves ;
- une copie `.bak` par slot ;
- un coordinateur unique ;
- migrations linéaires ;
- miniatures optionnelles ;
- rapports d’erreur simples.

Le développeur conserve des sauvegardes fixtures de chaque version publiée.

## 38. Parcours Studio

Le parcours Studio ajoute :

- propriétaire du format de sauvegarde ;
- revue obligatoire des migrations ;
- registre des versions ;
- fixtures anonymisées ;
- tests sur Windows et autres plateformes cibles ;
- tests de coupure pendant l’écriture ;
- limites de taille ;
- télémétrie locale respectueuse de la vie privée ;
- matrice de compatibilité build × format ;
- politique de conservation des anciennes branches de migration ;
- procédure de support pour fichiers corrompus.

## 39. Contrat de compatibilité

> **[LECTURE] Politique initiale — Ne pas saisir.**

```text
Le build courant lit :
- le format courant ;
- tous les formats publiés depuis la version 1 ;
- aucune version future.

Le build courant écrit :
- uniquement le format courant.
```

Une sauvegarde migrée en mémoire n’est pas automatiquement réécrite.

## 40. Tests préparatoires

Le chapitre 27 industrialisera les tests. Les cas à conserver dès maintenant sont :

- fichier courant valide ;
- fichier V1 valide ;
- fichier futur ;
- JSON tronqué ;
- hash divergent ;
- section absente ;
- identifiant dupliqué ;
- `.bak` valide avec principal corrompu ;
- `.tmp` abandonné ;
- disque plein simulé ;
- échec de remplacement ;
- chargement interrompu avant application ;
- transaction de repository échouée.

## 41. Scène de démonstration

> **[VSC] Visual Studio Code — Créer :** `res://scenes/learning/ch09_save_demo.gd`.

```gdscript
class_name Chapter09SaveDemo
extends Node

var _coordinator: SaveCoordinator

func configure(coordinator: SaveCoordinator) -> void:
	_coordinator = coordinator

func _ready() -> void:
	if _coordinator == null:
		push_error("SaveCoordinator absent.")
		return

	var metadata := {
		"play_time_seconds": 120.0,
		"world_id": "world.training",
		"player_name": "Ariane",
		"thumbnail_file": "manual-01.png",
		"world_snapshot": {
			"id": "world.training",
			"time_of_day": 9.5,
		},
		"player_snapshot": {
			"position": SaveValueCodec.vector3_to_dictionary(
				Vector3(2.0, 0.0, -4.0)
			),
		},
	}

	var save_error := _coordinator.save_slot(
		&"manual-01",
		"Test du chapitre 9",
		metadata,
		"0.1.0"
	)
	if save_error != OK:
		push_error("Sauvegarde impossible : %s" % error_string(save_error))
		return

	var document := _coordinator.load_slot(&"manual-01")
	if document.is_empty():
		push_error("Chargement ou validation impossible.")
		return

	print("Sauvegarde chargée en mémoire.")
	print(document["metadata"])
```

### 41.1 Explication

`configure()` injecte le coordinateur construit par le bootstrap.

`_ready()` refuse de continuer sans dépendance.

`metadata` contient à la fois les informations d’affichage et les snapshots préparatoires du monde et du joueur.

`save_slot()` capture les sections, construit le document et écrit le slot.

`load_slot()` lit, valide, migre et contrôle les sections, mais n’applique pas encore le monde.

Les deux `print()` affichent seulement des informations de démonstration.

## 42. Critères d’acceptation

Le chapitre est compris lorsque le lecteur peut expliquer et montrer que :

- la base SQLite n’est pas assimilée au fichier de sauvegarde ;
- les slots possèdent des identifiants validés ;
- le document possède `format`, `format_version` et `payload` ;
- les types Godot sont convertis explicitement ;
- les valeurs non sérialisables sont refusées ;
- le payload reçoit une empreinte déterministe ;
- le fichier final n’est pas écrit directement ;
- le `.tmp` est relu et validé ;
- la copie `.bak` précède le remplacement ;
- une version future est refusée ;
- les migrations s’enchaînent de `N` vers `N + 1` ;
- toutes les sections sont validées avant application ;
- le chargement prépare un nouveau monde avant la bascule ;
- les autosaves ne remplacent pas les slots manuels ;
- les réserves runtime sont déclarées.

## 43. Checklist Solo

- [ ] Définir les slots.
- [ ] Créer `SaveSlotId`.
- [ ] Créer les codecs de valeurs.
- [ ] Créer `CanonicalJson` et `SaveIntegrity`.
- [ ] Définir les sections.
- [ ] Construire le document.
- [ ] Valider l’enveloppe.
- [ ] Écrire via `.tmp`.
- [ ] Conserver `.bak`.
- [ ] Ajouter les migrations.
- [ ] Charger sans appliquer immédiatement.
- [ ] Ajouter la scène de démonstration.

## 44. Checklist Studio

- [ ] Nommer un propriétaire du format.
- [ ] Versionner le contrat.
- [ ] Conserver une fixture par version.
- [ ] Revoir chaque migration.
- [ ] Tester les plateformes.
- [ ] Tester les coupures d’écriture.
- [ ] Tester les limites de taille.
- [ ] Définir la rotation.
- [ ] Définir le support des fichiers corrompus.
- [ ] Documenter les sections obligatoires et optionnelles.
- [ ] Vérifier l’export et les permissions.

## 45. Sources techniques

Sources principales vérifiées le 19 juillet 2026 :

- documentation Godot 4.7, **Saving games** ;
- documentation Godot, classe **FileAccess** ;
- documentation Godot, classe **DirAccess** ;
- documentation Godot, **Runtime file loading and saving** ;
- documentation Godot 4.7, **Resources** ;
- documentation Godot, **ResourceSaver**.

Points vérifiés :

- limites de JSON ;
- existence de `store_var()` et risque des objets complets ;
- écriture UTF-8 avec `store_string()` ;
- lecture avec `get_as_text()` ;
- rôle de `flush()` et de la fermeture ;
- `rename_absolute()`, `copy_absolute()` et `remove_absolute()` ;
- sérialisation des Resources ;
- nécessité de conversions explicites pour les types Godot.

## 46. Réserves de validation

Le chapitre reste au niveau `static-review`.

Ne sont pas encore exécutés dans le Starter Kit :

- l’écriture réelle des slots sur Windows 11 ;
- une panne simulée entre chaque étape ;
- le comportement exact du remplacement sur NTFS ;
- le remplissage du disque ;
- la rotation des autosaves ;
- la génération de miniatures ;
- la migration V1 vers V2 ;
- la restauration transactionnelle de toutes les sections ;
- la création d’un monde temporaire ;
- le basculement sans perte de l’ancien monde ;
- les exports Windows sur machine propre.

Aucun PDF intermédiaire n’est construit.

## 47. Résultat attendu

À la fin de ce chapitre, `Project Asteria` possède un contrat de sauvegarde distinct de ses mécanismes internes de persistance.

Le projet sait désormais décrire :

- ce qui est capturé ;
- dans quel format ;
- sous quelle version ;
- avec quelles validations ;
- comment écrire sans remplacer prématurément la dernière copie valide ;
- comment récupérer une copie de secours ;
- comment migrer un document ancien ;
- comment refuser un document futur ;
- comment préparer un chargement avant de modifier le monde actif.

Le chapitre 10 pourra maintenant introduire la mémoire vectorielle sans lui confier la responsabilité des sauvegardes.
