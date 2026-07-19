---
title: "Livre II — Chapitre 14 : Personnages"
id: "DOC-L2-CH14"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 14
last-verified: "2026-07-19"
audit-status: "complete"
audit-date: "2026-07-19"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-14.md"
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

# Personnages

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH14`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Niveau de raisonnement conseillé :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-14.md`.

## 1. Rôle du chapitre

Les treize premiers chapitres ont construit les fondations Godot, l’architecture, les données, la persistance et la plateforme IA locale. Le présent chapitre ouvre les douze systèmes de gameplay avec l’objet le plus transversal du jeu : le personnage.

Un personnage n’est pas seulement un modèle 3D animé. Dans `Project Asteria`, il possède :

- une identité stable ;
- une définition de conception ;
- un état runtime mutable ;
- des statistiques dérivées ;
- une représentation dans la scène ;
- un corps physique lorsque le personnage existe dans le monde ;
- un contrôleur humain, automatisé ou absent ;
- une forme persistante indépendante des nœuds ;
- des événements typés ;
- des frontières explicites avec les systèmes futurs.

Le chapitre empêche de confondre :

- nom affiché et identifiant ;
- définition partagée et état vivant ;
- valeur de base et statistique dérivée ;
- personnage logique et nœud actif ;
- contrôleur et corps physique ;
- sauvegarde et cache runtime ;
- disparition de la scène et suppression définitive du personnage.

À la fin du chapitre, le lecteur doit savoir :

- définir un identifiant stable ;
- créer une `Resource` de conception validée ;
- construire un état runtime sans modifier la ressource source ;
- recalculer des statistiques dérivées ;
- composer une scène de personnage réutilisable ;
- brancher le contrôleur du chapitre 6 sans rendre le personnage dépendant du joueur ;
- instancier et retirer un personnage proprement ;
- limiter un registre aux instances actives ;
- émettre des événements typés ;
- convertir l’état vers une section de sauvegarde ;
- refuser les données incohérentes avant leur application ;
- préparer les chapitres sur les relations, la famille, les agents, le combat et les compétences.

## 2. Prérequis

Le lecteur doit connaître :

- les classes, types et signaux des chapitres 2 et 3 ;
- l’architecture feature-first du chapitre 4 ;
- l’injection et le bootstrap du chapitre 5 ;
- les entrées, contrôleurs et `CharacterBody3D` du chapitre 6 ;
- les `Resource`, catalogues et identifiants du chapitre 7 ;
- les dépôts et transactions du chapitre 8 ;
- les sections et migrations de sauvegarde du chapitre 9 ;
- les règles de sécurité du chapitre 13.

Le chapitre réutilise notamment :

- `PlayerInputReader` ;
- `PlayerInputFrame` ;
- `PlayerController` ;
- le moteur de déplacement présenté au chapitre 6 ;
- `SaveSection` et `SaveSectionRegistry` ;
- le principe de `StableId` ;
- les événements typés ;
- la règle d’échec fermé pour les données invalides.

## 3. Périmètre et frontières

Ce chapitre définit :

- l’identité et la définition d’un personnage ;
- les attributs et statistiques de base ;
- l’état runtime ;
- la composition minimale de scène ;
- l’apparition et la disparition ;
- le registre des personnages actifs ;
- les événements fondamentaux ;
- la conversion vers la sauvegarde ;
- les parcours Solo et Studio.

Il ne définit pas encore :

- les relations sociales du chapitre 15 ;
- la parenté, l’hérédité et les générations du chapitre 16 ;
- la décision autonome des agents du chapitre 17 ;
- les dégâts, résistances et attaques du chapitre 18 ;
- les compétences et pouvoirs du chapitre 19 ;
- l’inventaire du chapitre 20 ;
- l’économie du chapitre 21 ;
- l’écologie du chapitre 22 ;
- les factions et la justice du chapitre 23 ;
- la construction du chapitre 24 ;
- les quêtes et la narration du chapitre 25 ;
- les animations finales, vêtements et visuels du Livre III.

> **Frontière essentielle :** le personnage expose des données et des opérations cohérentes. Les systèmes futurs ajoutent leurs propres états et règles sans transformer `CharacterRuntimeState` en objet universel.

## 4. Vocabulaire

- **Identité stable :** valeur persistante qui désigne le même personnage à travers scènes, sauvegardes et renommages.
- **Définition :** données de conception partagées et principalement immuables.
- **État runtime :** valeurs mutables de l’instance pendant une partie.
- **Statistique de base :** valeur enregistrée ou définie directement.
- **Statistique dérivée :** valeur recalculée à partir d’autres données.
- **Acteur de scène :** représentation active d’un personnage dans l’arbre Godot.
- **Contrôleur :** composant qui produit des intentions ; il ne constitue pas l’identité du personnage.
- **Apparition :** création d’une représentation active dans le monde.
- **Disparition :** retrait de cette représentation sans supprimer nécessairement l’existence logique.
- **Snapshot :** représentation sérialisable de l’état autoritaire à un instant.
- **Cache :** valeur reconstructible qui n’est pas sauvegardée comme autorité.

## 5. Modèle en trois couches

`Project Asteria` sépare les données du personnage en trois niveaux.

> **[LECTURE] Modèle conceptuel — Ne pas saisir.**

```text
CharacterDefinition
données de conception partagées
        ↓ instanciation
CharacterRuntimeState
état vivant d’un personnage précis
        ↓ projection
CharacterSnapshot
forme persistante versionnée
```

| Couche | Exemples | Mutable | Persistée |
|---|---|---:|---:|
| définition | espèce, portrait, attributs initiaux | exceptionnellement | comme contenu du projet |
| runtime | santé courante, position logique, état actif | oui | sélection contrôlée |
| snapshot | identifiant, définition, valeurs autoritaires | document figé | oui |
| cache | santé maximale calculée, nœud actif | oui | non |

La définition ne contient pas la santé courante.  
L’état runtime ne contient pas de référence vers une scène de relations sociales.  
Le snapshot ne contient pas de `Node`, de `Resource` partagée ou de cache dérivé.

## 6. Architecture retenue

> **[LECTURE] Architecture du système — Ne pas saisir.**

```text
CharacterCatalog
    └── CharacterDefinition
             ↓
CharacterFactory
    └── CharacterRuntimeState
             ↓
CharacterSpawner
    └── PackedScene
          └── CharacterRuntime (Node)
          └── corps CharacterBody3D
          └── représentation visuelle
          └── contrôleur optionnel
             ↓
ActiveCharacterRegistry
             ↓
CharacterSaveSection
```

Responsabilités :

| Élément | Responsabilité |
|---|---|
| `CharacterId` | valider et générer les identifiants |
| `CharacterDefinition` | stocker les données de conception |
| `CharacterCatalog` | résoudre une définition par identifiant |
| `CharacterRuntimeState` | conserver l’état mutable |
| `CharacterStatistics` | calculer les valeurs dérivées |
| `CharacterRuntime` | relier état et scène sans devenir le modèle métier |
| `CharacterFactory` | créer un état valide |
| `CharacterSpawner` | matérialiser une scène |
| `ActiveCharacterRegistry` | retrouver seulement les personnages actifs |
| `CharacterSnapshotCodec` | convertir état et dictionnaire |
| `CharacterSaveSection` | intégrer le système au chapitre 9 |

## 7. Identité stable

### 7.1 Règles

Un identifiant de personnage :

- ne dépend pas du nom affiché ;
- ne dépend pas du chemin de scène ;
- ne dépend pas d’un index de tableau ;
- reste identique après renommage ;
- possède une forme validée ;
- est créé une seule fois ;
- est conservé dans la sauvegarde.

La forme retenue pour une **instance de personnage** est :

> **[LECTURE] Forme d’identifiant — Ne pas réutiliser telle quelle.**

```text
chr_7f4c3a5e2d8b4c91a6e0f137bd52a840
```

Le préfixe facilite le diagnostic. Les trente-deux caractères hexadécimaux fournissent une représentation compacte des seize octets aléatoires.

### 7.2 Validateur et générateur

> **[VSC] Visual Studio Code — Créer `res://src/features/characters/domain/character_id.gd` :**

```gdscript
class_name CharacterId
extends RefCounted

const PREFIX := "chr_"
const HEX_LENGTH := 32

static func generate() -> String:
	var bytes := Crypto.new().generate_random_bytes(16)
	if bytes.size() != 16:
		push_error("La génération de l’identifiant a échoué.")
		return ""

	var encoded := bytes.hex_encode()
	var value := PREFIX + encoded
	if not is_valid(value):
		push_error("L’identifiant généré est invalide.")
		return ""
	return value

static func is_valid(value: String) -> bool:
	if value.length() != PREFIX.length() + HEX_LENGTH:
		return false
	if not value.begins_with(PREFIX):
		return false

	var suffix := value.substr(PREFIX.length())
	for index in range(suffix.length()):
		var code := suffix.unicode_at(index)
		var is_digit := code >= 48 and code <= 57
		var is_lower_hex := code >= 97 and code <= 102
		if not is_digit and not is_lower_hex:
			return false
	return true
```

Explication :

- `Crypto.generate_random_bytes(16)` produit seize octets aléatoires adaptés à une identité imprévisible ;
- `hex_encode()` produit deux caractères par octet ;
- le validateur refuse les majuscules afin de conserver une forme canonique ;
- une chaîne vide indique un échec de création et ne doit jamais être acceptée par la fabrique ;
- l’identifiant ne constitue pas une autorisation, conformément au chapitre 13.

L’unicité pratique ne dispense pas le catalogue et la sauvegarde de détecter les doublons.

L’identifiant d’une **définition** suit une autre convention : le `StableId` lisible du chapitre 7, par exemple `character.definition.aster`. Une définition de contenu et une instance de partie n’occupent donc pas le même espace de noms.

## 8. Définition de conception

### 8.1 Ressource `CharacterDefinition`

> **[VSC] Visual Studio Code — Créer `res://src/features/characters/domain/character_definition.gd` :**

```gdscript
class_name CharacterDefinition
extends Resource

@export var definition_id: StringName = &""
@export var display_name := ""
@export var species_id: StringName = &""
@export_multiline var biography := ""
@export var portrait: Texture2D
@export var scene: PackedScene
@export_range(1, 100, 1) var base_vitality := 10
@export_range(1, 100, 1) var base_endurance := 10
@export_range(1, 100, 1) var base_agility := 10
@export_range(1, 100, 1) var base_intellect := 10
@export var tags: Array[StringName] = []

func validate() -> PackedStringArray:
	var errors := PackedStringArray()

	if not StableId.is_valid(definition_id):
		errors.append("definition_id invalide")
	if display_name.strip_edges().is_empty():
		errors.append("display_name vide")
	if not StableId.is_valid(species_id):
		errors.append("species_id invalide")
	if scene == null:
		errors.append("scene absente")
	if base_vitality < 1 or base_vitality > 100:
		errors.append("base_vitality hors limites")
	if base_endurance < 1 or base_endurance > 100:
		errors.append("base_endurance hors limites")
	if base_agility < 1 or base_agility > 100:
		errors.append("base_agility hors limites")
	if base_intellect < 1 or base_intellect > 100:
		errors.append("base_intellect hors limites")

	var seen := {}
	for tag in tags:
		if String(tag).strip_edges().is_empty():
			errors.append("tag vide")
			continue
		if seen.has(tag):
			errors.append("tag dupliqué : %s" % tag)
			continue
		seen[tag] = true

	return errors
```

La `Resource` contient ce qui peut être partagé entre plusieurs parties ou instances. Elle ne contient pas :

- la santé courante ;
- la position actuelle ;
- une relation vers un autre personnage ;
- l’état de combat ;
- un contrôleur ;
- une référence vers le nœud actif.

### 8.2 Créer une définition

> **[APP] Godot — Dans le FileSystem, créer `res://data/characters/aster.tres` à partir de `CharacterDefinition`.**

Renseigner au minimum :

- `definition_id` avec un `StableId` de contenu, par exemple `character.definition.aster` ;
- `display_name` ;
- `species_id` ;
- les quatre attributs de base ;
- la scène de personnage ;
- les tags de contenu.

Le fichier `.tres` est une donnée de conception. Une sauvegarde référence `definition_id` ; elle ne recopie pas toute la ressource.

## 9. Catalogue des définitions

> **[VSC] Visual Studio Code — Créer `res://src/features/characters/application/character_catalog.gd` :**

```gdscript
class_name CharacterCatalog
extends RefCounted

var _by_id: Dictionary[StringName, CharacterDefinition] = {}

func register_definition(
	definition: CharacterDefinition,
) -> Error:
	if definition == null:
		push_error("Définition de personnage absente.")
		return ERR_INVALID_PARAMETER

	var errors := definition.validate()
	if not errors.is_empty():
		push_error(
			"Définition invalide %s : %s"
			% [definition.resource_path, "; ".join(errors)]
		)
		return ERR_INVALID_DATA

	if _by_id.has(definition.definition_id):
		push_error(
			"Identifiant de définition dupliqué : %s"
			% definition.definition_id
		)
		return ERR_ALREADY_EXISTS

	_by_id[definition.definition_id] = definition
	return OK

func find(definition_id: StringName) -> CharacterDefinition:
	return _by_id.get(definition_id) as CharacterDefinition

func require(definition_id: StringName) -> CharacterDefinition:
	var definition := find(definition_id)
	if definition == null:
		push_error("Définition inconnue : %s" % definition_id)
	return definition

func all_ids() -> Array[StringName]:
	var ids: Array[StringName] = []
	ids.assign(_by_id.keys())
	ids.sort()
	return ids
```

Le catalogue :

- valide avant d’enregistrer ;
- refuse les doublons ;
- ne charge pas un chemin fourni par une sauvegarde ;
- renvoie `null` lorsque l’identifiant est inconnu ;
- conserve des résultats déterministes grâce au tri de `all_ids()`.

La liste des fichiers de définition doit être explicite ou produite par un pipeline contrôlé. Le runtime n’explore pas arbitrairement les fichiers du joueur.

## 10. Attributs et statistiques dérivées

### 10.1 Distinguer base, modificateur et résultat

Le chapitre utilise quatre attributs de base :

- vitalité ;
- endurance ;
- agilité ;
- intellect.

Les statistiques dérivées initiales sont :

- santé maximale ;
- endurance maximale ;
- vitesse de marche ;
- vitesse de sprint.

Ces formules sont pédagogiques. L’équilibrage complet viendra avec les systèmes concernés.

> **[VSC] Visual Studio Code — Créer `res://src/features/characters/domain/character_statistics.gd` :**

```gdscript
class_name CharacterStatistics
extends RefCounted

static func max_health(
	definition: CharacterDefinition,
	vitality_bonus: int = 0,
) -> int:
	var vitality := maxi(1, definition.base_vitality + vitality_bonus)
	return 50 + vitality * 5

static func max_stamina(
	definition: CharacterDefinition,
	endurance_bonus: int = 0,
) -> int:
	var endurance := maxi(
		1,
		definition.base_endurance + endurance_bonus,
	)
	return 40 + endurance * 4

static func walk_speed(
	definition: CharacterDefinition,
	agility_bonus: int = 0,
) -> float:
	var agility := maxi(1, definition.base_agility + agility_bonus)
	return clampf(3.0 + float(agility) * 0.08, 3.0, 8.0)

static func sprint_speed(
	definition: CharacterDefinition,
	agility_bonus: int = 0,
) -> float:
	return walk_speed(definition, agility_bonus) * 1.6
```

Les fonctions sont pures :

- elles ne modifient pas la définition ;
- elles renvoient le même résultat pour les mêmes arguments ;
- elles peuvent être recalculées après chargement ;
- elles ne sont pas persistées comme autorité.

La santé maximale n’est pas sauvegardée tant qu’elle reste entièrement reconstructible depuis la définition et les bonus autoritaires.

## 11. État runtime

### 11.1 Objet d’état

> **[VSC] Visual Studio Code — Créer `res://src/features/characters/domain/character_runtime_state.gd` :**

```gdscript
class_name CharacterRuntimeState
extends RefCounted

var character_id := ""
var definition_id: StringName = &""
var custom_name := ""
var current_health := 1
var current_stamina := 0
var vitality_bonus := 0
var endurance_bonus := 0
var agility_bonus := 0
var intellect_bonus := 0
var world_position := Vector3.ZERO
var world_yaw := 0.0
var is_alive := true

func validate(definition: CharacterDefinition) -> PackedStringArray:
	var errors := PackedStringArray()

	if not CharacterId.is_valid(character_id):
		errors.append("character_id invalide")
	if definition == null:
		errors.append("définition absente")
		return errors
	if definition_id != definition.definition_id:
		errors.append("definition_id incohérent")
	if custom_name.length() > 64:
		errors.append("custom_name trop long")

	var bonuses := [
		vitality_bonus,
		endurance_bonus,
		agility_bonus,
		intellect_bonus,
	]
	for bonus in bonuses:
		if bonus < -100 or bonus > 100:
			errors.append("bonus d’attribut hors limites")
			break

	var health_max := CharacterStatistics.max_health(
		definition,
		vitality_bonus,
	)
	var stamina_max := CharacterStatistics.max_stamina(
		definition,
		endurance_bonus,
	)

	if current_health < 0 or current_health > health_max:
		errors.append("current_health hors limites")
	if current_stamina < 0 or current_stamina > stamina_max:
		errors.append("current_stamina hors limites")
	if is_alive != (current_health > 0):
		errors.append("is_alive incohérent avec current_health")
	if not is_finite(world_position.x):
		errors.append("world_position.x non fini")
	if not is_finite(world_position.y):
		errors.append("world_position.y non fini")
	if not is_finite(world_position.z):
		errors.append("world_position.z non fini")
	if not is_finite(world_yaw):
		errors.append("world_yaw non fini")

	return errors

func effective_name(definition: CharacterDefinition) -> String:
	var trimmed := custom_name.strip_edges()
	if not trimmed.is_empty():
		return trimmed
	return definition.display_name
```

L’état ne référence pas directement le nœud actif. Une partie peut conserver l’état d’un personnage qui n’est pas actuellement matérialisé dans la scène.

### 11.2 Fabrique

> **[VSC] Visual Studio Code — Créer `res://src/features/characters/application/character_factory.gd` :**

```gdscript
class_name CharacterFactory
extends RefCounted

func create_new(
	definition: CharacterDefinition,
	character_id: String = "",
) -> CharacterRuntimeState:
	if definition == null:
		push_error("CharacterFactory exige une définition.")
		return null

	var definition_errors := definition.validate()
	if not definition_errors.is_empty():
		push_error(
			"Définition refusée : %s"
			% "; ".join(definition_errors)
		)
		return null

	var resolved_id := character_id
	if resolved_id.is_empty():
		resolved_id = CharacterId.generate()
	if not CharacterId.is_valid(resolved_id):
		push_error("Identifiant de personnage invalide.")
		return null

	var state := CharacterRuntimeState.new()
	state.character_id = resolved_id
	state.definition_id = definition.definition_id
	state.current_health = CharacterStatistics.max_health(definition)
	state.current_stamina = CharacterStatistics.max_stamina(definition)
	state.is_alive = true

	var state_errors := state.validate(definition)
	if not state_errors.is_empty():
		push_error(
			"État initial invalide : %s"
			% "; ".join(state_errors)
		)
		return null

	return state
```

La fabrique centralise les invariants de création. Un appelant ne doit pas construire un état partiellement initialisé puis espérer qu’un nœud le corrige.

## 12. Opérations fondamentales

> **[VSC] Visual Studio Code — Créer `res://src/features/characters/domain/character_rules.gd` :**

```gdscript
class_name CharacterRules
extends RefCounted

static func apply_health_delta(
	state: CharacterRuntimeState,
	definition: CharacterDefinition,
	delta: int,
) -> int:
	if state == null or definition == null:
		push_error("État ou définition absent.")
		return 0

	var old_value := state.current_health
	var maximum := CharacterStatistics.max_health(
		definition,
		state.vitality_bonus,
	)
	state.current_health = clampi(old_value + delta, 0, maximum)
	state.is_alive = state.current_health > 0
	return state.current_health - old_value

static func spend_stamina(
	state: CharacterRuntimeState,
	amount: int,
) -> bool:
	if state == null:
		return false
	if amount < 0:
		push_error("Une dépense d’endurance ne peut pas être négative.")
		return false
	if state.current_stamina < amount:
		return false

	state.current_stamina -= amount
	return true

static func restore_stamina(
	state: CharacterRuntimeState,
	definition: CharacterDefinition,
	amount: int,
) -> int:
	if state == null or definition == null or amount <= 0:
		return 0

	var old_value := state.current_stamina
	var maximum := CharacterStatistics.max_stamina(
		definition,
		state.endurance_bonus,
	)
	state.current_stamina = mini(maximum, old_value + amount)
	return state.current_stamina - old_value
```

Le chapitre ne définit pas encore une notion de dégâts. Il fournit une variation bornée de santé. Le chapitre 18 ajoutera les sources, types, résistances et règles de combat.

## 13. Événements typés

Les signaux sont émis par le composant runtime actif. Ils transportent l’identifiant stable, jamais le nom du nœud comme identité.

> **[VSC] Visual Studio Code — Créer `res://src/features/characters/presentation/character_runtime.gd` :**

```gdscript
class_name CharacterRuntime
extends Node

signal initialized(character_id: String)
signal display_name_changed(
	character_id: String,
	old_value: String,
	new_value: String,
)
signal health_changed(
	character_id: String,
	old_value: int,
	new_value: int,
)
signal stamina_changed(
	character_id: String,
	old_value: int,
	new_value: int,
)
signal life_state_changed(character_id: String, is_alive: bool)

var definition: CharacterDefinition
var state: CharacterRuntimeState
var _initialized := false

func initialize(
	new_definition: CharacterDefinition,
	new_state: CharacterRuntimeState,
) -> bool:
	if _initialized:
		push_error("CharacterRuntime est déjà initialisé.")
		return false
	if new_definition == null or new_state == null:
		push_error("Définition ou état absent.")
		return false

	var errors := new_state.validate(new_definition)
	if not errors.is_empty():
		push_error("État refusé : %s" % "; ".join(errors))
		return false

	definition = new_definition
	state = new_state
	_initialized = true
	initialized.emit(state.character_id)
	return true

func is_initialized() -> bool:
	return _initialized

func get_character_id() -> String:
	return state.character_id if _initialized else ""

func get_display_name() -> String:
	if not _initialized:
		return ""
	return state.effective_name(definition)

func rename(new_name: String) -> bool:
	if not _initialized:
		return false

	var trimmed := new_name.strip_edges()
	if trimmed.length() > 64:
		return false

	var old_value := get_display_name()
	state.custom_name = trimmed
	var current_value := get_display_name()
	if current_value != old_value:
		display_name_changed.emit(
			state.character_id,
			old_value,
			current_value,
		)
	return true

func change_health(delta: int) -> int:
	if not _initialized:
		return 0

	var old_value := state.current_health
	var old_alive := state.is_alive
	var applied := CharacterRules.apply_health_delta(
		state,
		definition,
		delta,
	)
	if state.current_health != old_value:
		health_changed.emit(
			state.character_id,
			old_value,
			state.current_health,
		)
	if state.is_alive != old_alive:
		life_state_changed.emit(
			state.character_id,
			state.is_alive,
		)
	return applied

func spend_stamina(amount: int) -> bool:
	if not _initialized:
		return false

	var old_value := state.current_stamina
	if not CharacterRules.spend_stamina(state, amount):
		return false

	stamina_changed.emit(
		state.character_id,
		old_value,
		state.current_stamina,
	)
	return true

func restore_stamina(amount: int) -> int:
	if not _initialized:
		return 0

	var old_value := state.current_stamina
	var applied := CharacterRules.restore_stamina(
		state,
		definition,
		amount,
	)
	if applied > 0:
		stamina_changed.emit(
			state.character_id,
			old_value,
			state.current_stamina,
		)
	return applied
```

Le signal décrit un événement passé. Le receveur peut mettre à jour une interface ou transmettre un événement applicatif sans accéder à tous les champs internes.

## 14. Composition de la scène

### 14.1 Arbre minimal

Le chapitre 6 a construit une scène pédagogique centrée sur le joueur. Le chapitre 14 conserve ses composants d’entrée et de déplacement, mais introduit un composant `CharacterRuntime` partagé par tous les personnages.

> **[APP] Godot — Créer `res://src/features/characters/presentation/player_character.tscn`.**

> **[SORTIE] Arbre attendu dans le dock Scene — Ne pas saisir.**

```text
PlayerCharacter (CharacterBody3D, script de déplacement du chapitre 6)
├── CollisionShape3D
├── CharacterRuntime (Node, unique dans la scène)
├── CharacterTransformSync (Node)
├── VisualRoot (Node3D)
│   ├── ModelRoot (Node3D)
│   └── NameAnchor (Marker3D)
├── PlayerInputReader (Node)
├── CameraRig (Node3D)
│   └── PitchPivot (Node3D)
│       └── SpringArm3D
│           └── Camera3D
│               └── PlayerInteractor (Node3D)
│                   └── InteractionRay (RayCast3D)
└── PlayerController (Node)
```

Responsabilités :

- la racine `CharacterBody3D` porte le mouvement et les collisions ;
- `CharacterRuntime` porte la projection de l’état métier ;
- `VisualRoot` contient le modèle et les éléments visuels remplaçables ;
- `PlayerInputReader` produit les intentions humaines ;
- `PlayerController` orchestre le mouvement et l’interaction ;
- la caméra existe seulement pour le personnage contrôlé localement.

Une scène de personnage non-joueur pourra conserver `CharacterRuntime`, le corps et `VisualRoot`, puis remplacer le contrôleur au chapitre 17.

### 14.2 Nœud unique dans la scène

> **[APP] Godot — Sélectionner `CharacterRuntime`, activer `Unique Name in Owner` et vérifier l’accès `%CharacterRuntime`.**

Le nom unique simplifie la composition interne de la scène. Il n’est pas utilisé comme identité persistante.

## 15. Apparition et disparition

### 15.1 Initialiser avant l’entrée dans l’arbre

`_ready()` est appelé lorsque le nœud entre dans l’arbre. Le `CharacterRuntime` doit donc recevoir sa définition et son état avant `add_child()`.

> **[VSC] Visual Studio Code — Créer `res://src/features/characters/application/character_spawner.gd` :**

```gdscript
class_name CharacterSpawner
extends RefCounted

var _world_root: Node3D
var _registry: ActiveCharacterRegistry

func _init(
	world_root: Node3D,
	registry: ActiveCharacterRegistry,
) -> void:
	_world_root = world_root
	_registry = registry

func spawn(
	definition: CharacterDefinition,
	state: CharacterRuntimeState,
	spawn_transform: Transform3D,
) -> CharacterBody3D:
	if _world_root == null or _registry == null:
		push_error("CharacterSpawner non configuré.")
		return null
	if definition == null or definition.scene == null:
		push_error("Définition ou scène absente.")
		return null
	if state == null:
		push_error("État absent.")
		return null
	if _registry.contains(state.character_id):
		push_error("Personnage déjà actif : %s" % state.character_id)
		return null

	var instance := definition.scene.instantiate()
	var body := instance as CharacterBody3D
	if body == null:
		instance.free()
		push_error("La scène doit produire un CharacterBody3D.")
		return null

	var runtime := body.get_node_or_null(
		"CharacterRuntime"
	) as CharacterRuntime
	if runtime == null:
		body.free()
		push_error("CharacterRuntime absent de la scène.")
		return null

	if not runtime.initialize(definition, state):
		body.free()
		return null

	_world_root.add_child(body)
	body.global_transform = spawn_transform

	if not _registry.register(runtime, body):
		body.queue_free()
		return null

	state.world_position = body.global_position
	state.world_yaw = body.global_rotation.y
	return body

func despawn(character_id: String) -> bool:
	var body := _registry.find_body(character_id)
	if body == null:
		return false

	var runtime := _registry.find_runtime(character_id)
	if runtime != null and runtime.is_initialized():
		runtime.state.world_position = body.global_position
		runtime.state.world_yaw = body.global_rotation.y

	_registry.unregister(character_id)
	body.queue_free()
	return true
```

Points importants :

- `PackedScene.instantiate()` crée une nouvelle hiérarchie ;
- le type de racine est vérifié ;
- l’état est validé avant `add_child()` ;
- `global_transform` est affecté après l’entrée dans l’arbre ;
- le registre refuse une seconde instance active du même personnage ;
- `free()` libère immédiatement une instance refusée avant son entrée dans l’arbre ;
- `queue_free()` planifie la destruction d’une instance déjà ajoutée ;
- l’état logique reste disponible après la disparition.

### 15.2 Disparition contre suppression

`despawn()` signifie seulement que la représentation active quitte le monde chargé. La suppression définitive d’un personnage exige une opération métier distincte et, plus tard, la vérification des références sociales, familiales, narratives et de sauvegarde.

## 16. Registre des personnages actifs

Le registre ne contient que les instances actuellement matérialisées. Ce n’est ni une base de données, ni un catalogue global de tous les personnages.

> **[VSC] Visual Studio Code — Créer `res://src/features/characters/application/active_character_registry.gd` :**

```gdscript
class_name ActiveCharacterRegistry
extends RefCounted

signal character_spawned(character_id: String)
signal character_despawned(character_id: String)

var _runtime_by_id: Dictionary = {}
var _body_by_id: Dictionary = {}

func register(
	runtime: CharacterRuntime,
	body: CharacterBody3D,
) -> bool:
	if runtime == null or body == null:
		return false

	var character_id := runtime.get_character_id()
	if not CharacterId.is_valid(character_id):
		return false
	if _runtime_by_id.has(character_id):
		return false

	_runtime_by_id[character_id] = runtime
	_body_by_id[character_id] = body
	character_spawned.emit(character_id)
	return true

func unregister(character_id: String) -> void:
	if not _runtime_by_id.has(character_id):
		return

	_runtime_by_id.erase(character_id)
	_body_by_id.erase(character_id)
	character_despawned.emit(character_id)

func contains(character_id: String) -> bool:
	return _runtime_by_id.has(character_id)

func find_runtime(character_id: String) -> CharacterRuntime:
	return _runtime_by_id.get(character_id) as CharacterRuntime

func find_body(character_id: String) -> CharacterBody3D:
	return _body_by_id.get(character_id) as CharacterBody3D

func active_ids() -> PackedStringArray:
	var ids := PackedStringArray()
	for value in _runtime_by_id.keys():
		ids.append(String(value))
	ids.sort()
	return ids
```

Le registre ne doit pas :

- créer les personnages ;
- charger les sauvegardes ;
- décider qui contrôle un personnage ;
- contenir les personnages hors scène ;
- devenir un Service Locator accessible depuis tous les scripts.

Il est injecté dans les services qui ont réellement besoin d’interroger les instances actives.

## 17. Contrôleurs et possession

Le personnage ne lit pas directement `Input`. Le contrôleur du chapitre 6 lit les entrées et agit sur le corps.

> **[LECTURE] Variantes de contrôleur — Ne pas saisir.**

```text
Personnage contrôlé localement
    PlayerInputReader → PlayerController → corps

Personnage autonome, chapitre 17
    AgentDecisionSource → AgentController → corps

Personnage sans simulation physique
    aucun contrôleur → état logique seulement
```

La possession locale associe temporairement :

- une source d’intention ;
- un contrôleur ;
- une caméra ;
- un personnage actif.

Changer de personnage contrôlé ne change pas son `character_id`.

Le chapitre 17 pourra produire une intention compatible sans réintroduire de touches clavier dans le domaine.

## 18. Synchroniser la position logique

La position du nœud est une projection runtime. Elle doit être recopiée dans l’état à des points contrôlés :

- avant une sauvegarde ;
- avant une disparition ;
- lors d’un changement de zone ;
- lors d’un checkpoint ;
- jamais à chaque image si aucun consommateur ne l’exige.

> **[VSC] Visual Studio Code — Créer `res://src/features/characters/presentation/character_transform_sync.gd` :**

```gdscript
class_name CharacterTransformSync
extends Node

@export var runtime_path := NodePath("../CharacterRuntime")

@onready var _runtime := get_node(
	runtime_path
) as CharacterRuntime
@onready var _body := get_parent() as CharacterBody3D

func capture_to_state() -> bool:
	if _runtime == null or _body == null:
		return false
	if not _runtime.is_initialized():
		return false

	_runtime.state.world_position = _body.global_position
	_runtime.state.world_yaw = _body.global_rotation.y
	return true

func apply_from_state() -> bool:
	if _runtime == null or _body == null:
		return false
	if not _runtime.is_initialized():
		return false

	_body.global_position = _runtime.state.world_position
	var rotation := _body.global_rotation
	rotation.y = _runtime.state.world_yaw
	_body.global_rotation = rotation
	return true
```

Ce composant évite de sauvegarder directement un `Transform3D` si seuls la position et le lacet sont nécessaires. Il exclut volontairement l’échelle et l’inclinaison physique transitoire.

## 19. Snapshot persistant

### 19.1 Schéma

> **[LECTURE] Snapshot versionné — Ne pas saisir.**

```json
{
  "character_id": "chr_7f4c3a5e2d8b4c91a6e0f137bd52a840",
  "definition_id": "character.definition.aster",
  "custom_name": "Aster",
  "current_health": 100,
  "current_stamina": 80,
  "bonuses": {
    "vitality": 0,
    "endurance": 0,
    "agility": 0,
    "intellect": 0
  },
  "world": {
    "position": [12.5, 0.0, -4.25],
    "yaw": 1.57079632679
  },
  "is_alive": true
}
```

Le snapshot ne contient pas :

- `max_health` ;
- `max_stamina` ;
- une référence de `PackedScene` ;
- un `NodePath` ;
- le nœud actif ;
- le contrôleur ;
- la caméra ;
- des relations sociales ou familiales futures.

### 19.2 Codec

> **[VSC] Visual Studio Code — Créer `res://src/features/characters/infrastructure/character_snapshot_codec.gd` :**

```gdscript
class_name CharacterSnapshotCodec
extends RefCounted

func encode(state: CharacterRuntimeState) -> Dictionary:
	return {
		"character_id": state.character_id,
		"definition_id": String(state.definition_id),
		"custom_name": state.custom_name,
		"current_health": state.current_health,
		"current_stamina": state.current_stamina,
		"bonuses": {
			"vitality": state.vitality_bonus,
			"endurance": state.endurance_bonus,
			"agility": state.agility_bonus,
			"intellect": state.intellect_bonus,
		},
		"world": {
			"position": [
				state.world_position.x,
				state.world_position.y,
				state.world_position.z,
			],
			"yaw": state.world_yaw,
		},
		"is_alive": state.is_alive,
	}

func decode(
	value: Dictionary,
	catalog: CharacterCatalog,
) -> CharacterRuntimeState:
	var raw_character_id := value.get("character_id")
	var raw_definition_id := value.get("definition_id")
	if not (raw_character_id is String):
		push_error("character_id doit être une chaîne.")
		return null
	if not (raw_definition_id is String):
		push_error("definition_id doit être une chaîne.")
		return null

	var character_id: String = raw_character_id
	var definition_id := StringName(raw_definition_id)
	if not CharacterId.is_valid(character_id):
		push_error("character_id de snapshot invalide.")
		return null
	if not StableId.is_valid(definition_id):
		push_error("definition_id de snapshot invalide.")
		return null

	var definition := catalog.require(definition_id)
	if definition == null:
		return null

	var bonuses := value.get("bonuses", {})
	var world := value.get("world", {})
	if not (bonuses is Dictionary) or not (world is Dictionary):
		push_error("Sections bonuses ou world invalides.")
		return null

	var raw_position := world.get("position", [])
	if not (raw_position is Array) or raw_position.size() != 3:
		push_error("Position de snapshot invalide.")
		return null

	var custom_name_value := value.get("custom_name", "")
	var health_value := value.get("current_health")
	var stamina_value := value.get("current_stamina")
	var alive_value := value.get("is_alive")
	if not (custom_name_value is String):
		push_error("custom_name doit être une chaîne.")
		return null
	if not (health_value is int) or not (stamina_value is int):
		push_error("Santé ou endurance non entière.")
		return null
	if not (alive_value is bool):
		push_error("is_alive doit être booléen.")
		return null

	var bonus_keys := [
		"vitality",
		"endurance",
		"agility",
		"intellect",
	]
	for key in bonus_keys:
		if not (bonuses.get(key, 0) is int):
			push_error("Bonus non entier : %s" % key)
			return null

	for coordinate in raw_position:
		if not (coordinate is int) and not (coordinate is float):
			push_error("Coordonnée de position non numérique.")
			return null

	var yaw_value := world.get("yaw", 0.0)
	if not (yaw_value is int) and not (yaw_value is float):
		push_error("Lacet non numérique.")
		return null

	var state := CharacterRuntimeState.new()
	state.character_id = character_id
	state.definition_id = definition_id
	state.custom_name = custom_name_value
	state.current_health = health_value
	state.current_stamina = stamina_value
	state.vitality_bonus = bonuses.get("vitality", 0)
	state.endurance_bonus = bonuses.get("endurance", 0)
	state.agility_bonus = bonuses.get("agility", 0)
	state.intellect_bonus = bonuses.get("intellect", 0)
	state.world_position = Vector3(
		float(raw_position[0]),
		float(raw_position[1]),
		float(raw_position[2]),
	)
	state.world_yaw = float(yaw_value)
	state.is_alive = alive_value

	var errors := state.validate(definition)
	if not errors.is_empty():
		push_error(
			"Snapshot de personnage refusé : %s"
			% "; ".join(errors)
		)
		return null

	return state
```

Le décodeur :

- résout la définition par identifiant contrôlé ;
- refuse une définition absente ;
- valide les sections avant conversion ;
- recalcule les limites à partir de la définition ;
- refuse `NaN`, l’infini et les valeurs hors bornes via `validate()` ;
- ne modifie aucun état existant avant la fin de la validation.

## 20. Section de sauvegarde

> **[VSC] Visual Studio Code — Créer `res://src/features/characters/infrastructure/character_save_section.gd` :**

```gdscript
class_name CharacterSaveSection
extends SaveSection

const SECTION_ID := "characters"
const SECTION_VERSION := 1

var _states: Dictionary
var _catalog: CharacterCatalog
var _codec := CharacterSnapshotCodec.new()

func _init(
	states: Dictionary,
	catalog: CharacterCatalog,
) -> void:
	_states = states
	_catalog = catalog

func get_section_id() -> String:
	return SECTION_ID

func get_current_version() -> int:
	return SECTION_VERSION

func capture() -> Dictionary:
	var snapshots: Array[Dictionary] = []
	var ids := PackedStringArray()

	for value in _states.keys():
		ids.append(String(value))
	ids.sort()

	for character_id in ids:
		var state := _states.get(
			character_id
		) as CharacterRuntimeState
		if state == null:
			push_error("État de personnage absent : %s" % character_id)
			return {}

		var definition := _catalog.require(state.definition_id)
		if definition == null:
			return {}

		var errors := state.validate(definition)
		if not errors.is_empty():
			push_error(
				"État non sauvegardable %s : %s"
				% [character_id, "; ".join(errors)]
			)
			return {}

		snapshots.append(_codec.encode(state))

	return {
		"version": SECTION_VERSION,
		"characters": snapshots,
	}

func validate_and_prepare(value: Dictionary) -> Variant:
	if int(value.get("version", -1)) != SECTION_VERSION:
		return null

	var raw_characters := value.get("characters", [])
	if not (raw_characters is Array):
		return null

	var prepared := {}
	for raw_value in raw_characters:
		if not (raw_value is Dictionary):
			return null
		var state := _codec.decode(raw_value, _catalog)
		if state == null:
			return null
		if prepared.has(state.character_id):
			return null
		prepared[state.character_id] = state

	return prepared

func apply_prepared(prepared: Variant) -> bool:
	if not (prepared is Dictionary):
		return false

	_states.clear()
	for character_id in prepared:
		_states[character_id] = prepared[character_id]
	return true
```

La validation construit un dictionnaire temporaire. L’état courant n’est remplacé qu’après validation complète de tous les personnages.

La signature exacte de `SaveSection` doit rester alignée sur l’abstraction du chapitre 9. Si le Starter Kit matérialisé emploie une autre convention de nommage, l’adaptateur conserve les mêmes étapes : capturer, valider, préparer, puis appliquer.

## 21. Bootstrap

> **[VSC] Visual Studio Code — Créer `res://src/app/character_bootstrap.gd` :**

```gdscript
class_name CharacterBootstrap
extends RefCounted

var catalog := CharacterCatalog.new()
var states: Dictionary = {}
var active_registry := ActiveCharacterRegistry.new()
var factory := CharacterFactory.new()

func register_definitions(
	definitions: Array[CharacterDefinition],
) -> bool:
	var candidate := CharacterCatalog.new()
	for definition in definitions:
		var error := candidate.register_definition(definition)
		if error != OK:
			return false

	catalog = candidate
	return true

func create_character(
	definition_id: StringName,
	custom_name: String = "",
) -> CharacterRuntimeState:
	var definition := catalog.require(definition_id)
	if definition == null:
		return null

	var state := factory.create_new(definition)
	if state == null:
		return null
	var trimmed_name := custom_name.strip_edges()
	if trimmed_name.length() > 64:
		push_error("Nom personnalisé trop long.")
		return null
	state.custom_name = trimmed_name

	var state_errors := state.validate(definition)
	if not state_errors.is_empty():
		push_error(
			"État personnalisé invalide : %s"
			% "; ".join(state_errors)
		)
		return null

	if states.has(state.character_id):
		push_error("Collision d’identifiant de personnage.")
		return null

	states[state.character_id] = state
	return state

func build_save_section() -> CharacterSaveSection:
	return CharacterSaveSection.new(states, catalog)
```

Le bootstrap :

- assemble les dépendances ;
- conserve les états logiques ;
- ne place pas le catalogue ou le registre en Autoload par défaut ;
- fournit la section au registre de sauvegarde ;
- injecte le registre actif dans le spawner.

## 22. Démonstration pédagogique

> **[APP] Godot — Créer `res://scenes/learning/ch14_characters_demo.tscn`.**

Arbre conseillé :

> **[SORTIE] Arbre de démonstration — Ne pas saisir.**

```text
CharactersDemo (Node3D)
├── World (Node3D)
├── SpawnPoint (Marker3D)
├── Camera3D
├── DirectionalLight3D
├── Environment
└── DemoController (Node)
```

> **[VSC] Visual Studio Code — Créer `res://scenes/learning/ch14_characters_demo.gd` :**

```gdscript
extends Node3D

@export var definitions: Array[CharacterDefinition] = []

@onready var world := $World as Node3D
@onready var spawn_point := $SpawnPoint as Marker3D

var bootstrap := CharacterBootstrap.new()
var spawner: CharacterSpawner

func _ready() -> void:
	if not bootstrap.register_definitions(definitions):
		push_error("Catalogue de démonstration invalide.")
		return

	spawner = CharacterSpawner.new(
		world,
		bootstrap.active_registry,
	)

	if definitions.is_empty():
		push_error("Aucune définition de démonstration.")
		return

	var definition := definitions[0]
	var state := bootstrap.create_character(
		definition.definition_id,
		"Aster",
	)
	if state == null:
		return

	var body := spawner.spawn(
		definition,
		state,
		spawn_point.global_transform,
	)
	if body == null:
		return

	var runtime := bootstrap.active_registry.find_runtime(
		state.character_id
	)
	runtime.health_changed.connect(_on_health_changed)
	runtime.change_health(-10)

func _on_health_changed(
	character_id: String,
	old_value: int,
	new_value: int,
) -> void:
	print(
		"Personnage %s : santé %d → %d"
		% [character_id, old_value, new_value]
	)
```

> **[SORTIE] Forme attendue dans l’onglet Output — Ne pas saisir.**

```text
Personnage chr_<identifiant> : santé <ancienne> → <nouvelle>
```

La démonstration vérifie la chaîne :

1. charger les définitions choisies dans l’Inspector ;
2. construire le catalogue ;
3. créer l’état ;
4. instancier la scène ;
5. enregistrer l’instance active ;
6. appliquer une variation de santé ;
7. observer un signal typé.

## 23. Parcours Solo

Le Mode Solo privilégie :

- un catalogue explicite de définitions ;
- un dictionnaire d’états en mémoire ;
- une seule représentation active par identifiant ;
- une scène de joueur et quelques variantes de personnages ;
- une section de sauvegarde unique ;
- des statistiques dérivées recalculées ;
- un registre actif injecté ;
- des événements directs et typés ;
- aucune base de personnages distribuée en réseau.

Les personnages éloignés peuvent rester sous forme d’état logique sans nœud 3D actif.

## 24. Parcours Studio

Le Mode Studio ajoute :

- une convention d’identifiants et un validateur de contenu automatisé ;
- un catalogue généré par pipeline ;
- des propriétaires de schémas ;
- des variantes visuelles séparées des définitions métier ;
- des outils de prévisualisation ;
- des tests de compatibilité des snapshots ;
- des budgets d’instances actives ;
- des diagnostics de duplication ;
- une migration explicite des définitions supprimées ;
- une stratégie de streaming de zones ;
- des revues des frontières entre systèmes ;
- une traçabilité des changements d’équilibrage.

Le Studio ne transforme pas le registre actif en base globale ni le nœud de personnage en agrégat de tous les systèmes.

## 25. Tests à préparer

Le Starter Kit devra vérifier :

- génération et validation des identifiants ;
- refus des identifiants dupliqués ;
- validation des définitions ;
- création d’un état initial ;
- bornage de santé et d’endurance ;
- recalcul des statistiques ;
- renommage sans changement d’identité ;
- instanciation d’une scène valide ;
- refus d’une scène de mauvais type ;
- initialisation avant `_ready()` ;
- apparition unique par identifiant ;
- capture de position avant disparition ;
- retrait du registre ;
- encode/decode d’un snapshot ;
- refus des valeurs non finies ;
- refus d’une définition inconnue ;
- refus des doublons dans la sauvegarde ;
- application atomique de la section ;
- connexion et émission des signaux ;
- réutilisation du contrôleur du chapitre 6.

## 26. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 26.1 Utiliser le nom affiché comme identifiant

**Symptôme :** renommer le personnage casse les références.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
characters_by_id[display_name] = state
```

**Correction :** indexer avec `character_id`.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
characters_by_id[state.character_id] = state
```

**Différence :** l’identité reste stable après traduction ou renommage.

### 26.2 Modifier la `Resource` partagée

**Symptôme :** soigner une instance soigne tous les personnages utilisant la définition.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
definition.base_vitality += 5
```

**Correction :** modifier un bonus de l’état runtime.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
state.vitality_bonus += 5
```

**Différence :** la donnée de conception partagée reste intacte.

### 26.3 Sauvegarder une statistique dérivée comme autorité

**Symptôme :** une nouvelle formule laisse une ancienne valeur incohérente dans la sauvegarde.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```json
{"max_health": 120, "base_vitality": 10}
```

**Correction :** sauvegarder les entrées autoritaires et recalculer.

> **[LECTURE] Exemple corrigé — Référence.**

```json
{"vitality_bonus": 0, "current_health": 100}
```

**Différence :** `max_health` suit toujours la formule courante et les migrations.

### 26.4 Faire lire `Input` au personnage

**Symptôme :** le personnage ne peut être contrôlé que par le clavier local.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
func _physics_process(_delta):
	if Input.is_action_pressed("move_forward"):
		velocity.z -= 1.0
```

**Correction :** recevoir une intention depuis un contrôleur.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
motor.apply_input(frame, camera_basis, delta)
```

**Différence :** joueur, test et futur agent peuvent produire la même intention.

### 26.5 Confondre contrôleur et identité

**Symptôme :** changer de personnage contrôlé remplace son identité.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
state.character_id = "player"
```

**Correction :** associer temporairement un contrôleur à l’acteur.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
possession.assign_controller(state.character_id, player_controller)
```

**Différence :** la possession change sans réécrire les références persistantes.

### 26.6 Utiliser un index de tableau comme identité

**Symptôme :** supprimer une entrée décale tous les personnages.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var current_character_id := str(characters.find(state))
```

**Correction :** générer l’identifiant une seule fois.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
state.character_id = CharacterId.generate()
```

**Différence :** l’ordre du conteneur n’affecte plus l’identité.

### 26.7 Initialiser après `add_child()`

**Symptôme :** `_ready()` observe un état absent.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
world.add_child(body)
runtime.initialize(definition, state)
```

**Correction :** initialiser avant l’entrée dans l’arbre.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
runtime.initialize(definition, state)
world.add_child(body)
```

**Différence :** les callbacks de cycle de vie voient un composant cohérent.

### 26.8 Définir `global_transform` avant l’entrée dans l’arbre

**Symptôme :** le transform global est calculé sans parent de monde valide.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
body.global_transform = spawn_transform
world.add_child(body)
```

**Correction :** ajouter puis placer.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
world.add_child(body)
body.global_transform = spawn_transform
```

**Différence :** le transform global est résolu dans le bon espace parent.

### 26.9 Enregistrer deux acteurs actifs pour la même identité

**Symptôme :** les événements et sauvegardes ciblent une instance ambiguë.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
runtime_by_id[character_id] = second_runtime
```

**Correction :** refuser l’apparition dupliquée.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
if registry.contains(character_id):
	return null
```

**Différence :** une identité correspond à au plus une représentation active.

### 26.10 Traiter `queue_free()` comme une suppression métier

**Symptôme :** retirer le nœud efface implicitement l’existence logique.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
body.queue_free()
states.erase(character_id)
```

**Correction :** séparer disparition et suppression.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
spawner.despawn(character_id)
```

**Différence :** l’état reste disponible pour sauvegarde ou réapparition.

### 26.11 Sauvegarder un nœud ou une `Resource`

**Symptôme :** le document JSON dépend d’objets runtime non sérialisables.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
snapshot["runtime"] = runtime
snapshot["definition"] = definition
```

**Correction :** conserver les identifiants et valeurs primitives.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
snapshot["character_id"] = state.character_id
snapshot["definition_id"] = state.definition_id
```

**Différence :** la sauvegarde reste indépendante de l’arbre et du cache de ressources.

### 26.12 Appliquer un snapshot avant validation complète

**Symptôme :** la moitié des personnages est remplacée avant la découverte d’une erreur.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
for raw_state in raw_characters:
	states[id] = codec.decode(raw_state, catalog)
```

**Correction :** préparer puis appliquer en une étape.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
var prepared := validate_and_prepare(section)
apply_prepared(prepared)
```

**Différence :** une section invalide ne produit pas d’état partiel.

### 26.13 Faire du registre un Service Locator

**Symptôme :** tous les scripts recherchent n’importe quel personnage globalement.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
ActiveCharacters.get_singleton().find_runtime(character_id)
```

**Correction :** injecter le registre aux services concernés.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
var spawner := CharacterSpawner.new(world, active_registry)
```

**Différence :** les dépendances restent visibles et limitées.

### 26.14 Mettre les relations dans `CharacterRuntimeState`

**Symptôme :** le modèle du personnage devient responsable du chapitre 15.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
state.friendships[other_id] = 75
```

**Correction :** réserver un état séparé au système social.

> **[LECTURE] Exemple corrigé — Référence.**

```text
RelationshipState(character_id, other_character_id, affinity)
```

**Différence :** chaque système conserve son schéma, ses invariants et ses migrations.

### 26.15 Utiliser l’identifiant comme autorisation

**Symptôme :** connaître `character_id` permet toute opération.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if CharacterId.is_valid(character_id):
	delete_character(character_id)
```

**Correction :** vérifier séparément la permission de l’appelant.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
if policy.can_delete_character(actor, character_id):
	delete_character(character_id)
```

**Différence :** l’identifiant localise la cible sans accorder de pouvoir.

### 26.16 Multiplier la vitesse par `delta` deux fois

**Symptôme :** le corps se déplace très lentement et dépend du pas de physique.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
velocity = desired_velocity * delta
move_and_slide()
```

**Correction :** conserver une vitesse par seconde.

> **[LECTURE] Exemple corrigé — Référence.**

```gdscript
velocity = desired_velocity
move_and_slide()
```

**Différence :** `move_and_slide()` utilise déjà le pas de physique pour le déplacement.

## 27. Critères d’acceptation

Le lecteur peut montrer statiquement que :

- l’identité ne dépend pas du nom ou d’un index ;
- la définition ne contient aucun état courant ;
- l’état runtime ne modifie pas la `Resource` ;
- les statistiques dérivées sont recalculables ;
- le personnage ne lit pas directement les entrées ;
- corps, contrôleur, représentation et état ont des responsabilités distinctes ;
- l’initialisation précède l’entrée dans l’arbre ;
- le placement global suit `add_child()` ;
- le registre contient seulement les instances actives ;
- une identité n’a qu’une représentation active ;
- la disparition ne supprime pas l’état logique ;
- le snapshot contient seulement des données sérialisables ;
- la section est validée entièrement avant application ;
- les caches dérivés ne sont pas sauvegardés ;
- les systèmes des chapitres 15 à 19 restent séparés ;
- les modes Solo et Studio sont distingués.

## 28. Checklist Solo

- [ ] Créer `CharacterId`.
- [ ] Créer et valider `CharacterDefinition`.
- [ ] Construire le catalogue explicite.
- [ ] Créer `CharacterRuntimeState`.
- [ ] Recalculer les statistiques dérivées.
- [ ] Ajouter `CharacterRuntime` à la scène.
- [ ] Réutiliser le contrôleur du chapitre 6.
- [ ] Créer la fabrique et le spawner.
- [ ] Limiter le registre aux instances actives.
- [ ] Capturer la position avant sauvegarde ou disparition.
- [ ] Encoder et valider les snapshots.
- [ ] Enregistrer `CharacterSaveSection`.
- [ ] Préparer la démonstration.
- [ ] Conserver les systèmes futurs hors du modèle.

## 29. Checklist Studio

- [ ] Définir une politique d’identifiants.
- [ ] Générer et valider le catalogue.
- [ ] Nommer les propriétaires des schémas.
- [ ] Séparer définition métier et variantes visuelles.
- [ ] Versionner les changements d’équilibrage.
- [ ] Tester les anciennes sauvegardes.
- [ ] Détecter les définitions orphelines.
- [ ] Budgéter les instances actives.
- [ ] Préparer le streaming de zones.
- [ ] Instrumenter apparitions et disparitions.
- [ ] Revoir les frontières avec les chapitres 15 à 25.
- [ ] Automatiser les tests de contenu.

## 30. Sources techniques

Sources principales relues pour l’audit statique du 19 juillet 2026 :

- [Godot Engine 4.7 — `CharacterBody3D`](https://docs.godotengine.org/en/4.7/classes/class_characterbody3d.html) ;
- [Godot Engine 4.7 — `Node`](https://docs.godotengine.org/en/4.7/classes/class_node.html) ;
- [Godot Engine 4.7 — `Node3D`](https://docs.godotengine.org/en/4.7/classes/class_node3d.html) ;
- [Godot Engine 4.7 — `Resource`](https://docs.godotengine.org/en/4.7/classes/class_resource.html) ;
- [Godot Engine 4.7 — ressources](https://docs.godotengine.org/en/4.7/tutorials/scripting/resources.html) ;
- [Godot Engine 4.7 — `PackedScene`](https://docs.godotengine.org/en/4.7/classes/class_packedscene.html) ;
- [Godot Engine 4.7 — instancier des scènes](https://docs.godotengine.org/en/4.7/getting_started/step_by_step/instancing.html) ;
- [Godot Engine 4.7 — signaux](https://docs.godotengine.org/en/4.7/getting_started/step_by_step/signals.html) ;
- [Godot Engine 4.7 — `Crypto`](https://docs.godotengine.org/en/4.7/classes/class_crypto.html) ;
- [Godot Engine 4.7 — `StringName`](https://docs.godotengine.org/en/4.7/classes/class_stringname.html) ;
- [Godot Engine 4.7 — `Dictionary`](https://docs.godotengine.org/en/4.7/classes/class_dictionary.html) ;
- [Godot Engine 4.7 — `Array`](https://docs.godotengine.org/en/4.7/classes/class_array.html) ;
- [Godot Engine 4.7 — `Vector3`](https://docs.godotengine.org/en/4.7/classes/class_vector3.html) ;
- [Godot Engine 4.7 — `Transform3D`](https://docs.godotengine.org/en/4.7/classes/class_transform3d.html) ;
- [Godot Engine 4.7 — `JSON`](https://docs.godotengine.org/en/4.7/classes/class_json.html).

## 31. Réserves de validation

Ne sont pas exécutés :

- analyse des scripts par Godot 4.7.1 ;
- création des scènes dans l’éditeur ;
- validation de `Crypto.generate_random_bytes()` sur les plateformes exportées ;
- instanciation réelle d’un `PackedScene` ;
- ordre exact des callbacks `_enter_tree()` et `_ready()` dans le Starter Kit ;
- mouvement et collisions ;
- connexion des contrôleurs du chapitre 6 ;
- apparition et disparition dans un monde réel ;
- capture des transforms avec interpolation physique ;
- sérialisation par le pipeline complet du chapitre 9 ;
- migrations de snapshots ;
- chargement d’anciennes sauvegardes ;
- budgets de personnages actifs ;
- streaming de zones ;
- performances sur la configuration AMD de référence ;
- packaging multi-plateforme.

Les extraits GDScript ont fait l’objet d’une revue statique uniquement. Aucun fichier du Starter Kit n’est matérialisé et aucun PDF intermédiaire n’est construit.

## 32. Résultat attendu

`Project Asteria` possède désormais un système de personnages documenté avec identité stable, définition de conception, état runtime, statistiques dérivées, scène composée, contrôleurs séparés, apparition, registre actif, événements et sauvegarde validée.

Le chapitre 15 pourra ajouter les relations sociales dans un système indépendant, relié aux personnages uniquement par leurs identifiants stables.
