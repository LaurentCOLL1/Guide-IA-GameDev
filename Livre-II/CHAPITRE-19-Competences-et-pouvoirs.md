---
title: "Livre II — Chapitre 19 : Compétences et pouvoirs"
id: "DOC-L2-CH19"
status: "reviewed"
version: "1.0.1"
lang: "fr-FR"
book: "Livre II"
chapter: 19
last-verified: "2026-07-20T16:52:26+02:00"
audit-status: "complete"
audit-date: "2026-07-20T16:52:26+02:00"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-19.md"
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

# Compétences et pouvoirs

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH19`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Niveau de raisonnement conseillé :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-19.md`.

## 1. Rôle du chapitre

Le chapitre 18 a défini l’autorité du combat : commandes typées, initiative, cibles, portée, ligne de vue, défense, dégâts, états temporaires et commit préparé.

Ce chapitre définit **ce qu’un personnage sait utiliser**. Une compétence ou un pouvoir possède une définition de conception, un état de progression, des charges, une recharge, des coûts, une forme de ciblage et une suite d’effets demandés.

Le système doit rester compatible avec les décisions déjà prises :

- la santé et l’endurance restent dans `CharacterRuntimeState` ;
- la portée, la ligne de vue, la défense, les dégâts et les états de combat restent sous l’autorité du combat ;
- une `Resource` de conception n’est jamais utilisée comme état runtime ;
- les identifiants sont stables et indépendants des textes affichés ;
- les mutations sont préparées puis committées comme un lot ;
- un agent ou une interface propose une utilisation sans imposer son résultat ;
- les plans, sélections et prévisualisations sont transitoires.

## 2. Prérequis

Le lecteur doit avoir parcouru :

- le chapitre 4 pour l’architecture feature-first ;
- le chapitre 5 pour les services injectés et le point de composition ;
- le chapitre 7 pour les `Resource`, catalogues et identifiants stables ;
- le chapitre 9 pour les sections de sauvegarde préparées avant application ;
- le chapitre 14 pour les règles de personnage ;
- le chapitre 17 pour les requêtes d’action des agents ;
- le chapitre 18 pour l’autorité de combat.

## 3. Périmètre et frontières

Ce chapitre couvre :

- définitions de compétences et pouvoirs ;
- coûts par ressource ;
- charges et recharges en ticks logiques ;
- ciblage sur soi, personnage, point ou zone ;
- effets composables de dégâts, d’état et de ressource ;
- déblocage, rang et expérience ;
- commandes d’utilisation et résultats métier ;
- préparation atomique du coût, des effets et de l’état de compétence ;
- adaptation des joueurs et agents ;
- sauvegarde stricte et restauration préparée.

Il ne couvre pas :

- l’inventaire, l’équipement, les armes possédées et les consommables du chapitre 20 ;
- les prix et transactions du chapitre 21 ;
- les lois, factions et sanctions du chapitre 23 ;
- les quêtes et conséquences narratives du chapitre 25 ;
- les outils d’édition du chapitre 26 ;
- les campagnes exécutées du chapitre 27 ;
- le multijoueur du Livre IV.

> **Frontière essentielle :** une compétence décrit et orchestre des demandes. Elle ne recalcule jamais les règles propriétaires du combat ou des personnages.

## 4. Chaîne d’autorité

> **[LECTURE] Flux d’utilisation — Ne pas saisir.**

```text
joueur / agent / scénario
    ↓ AbilityUseCommand
AbilityService
    ├── relit définition, progression et recharge
    ├── prépare les coûts
    ├── prépare les candidats d’effets
    └── prépare le nouvel état de compétence
            ↓
AbilityMutationUnitOfWork
    ├── revalide révisions et candidats
    ├── commit ressources, effets et état de compétence
    └── refuse le lot entier si une précondition échoue
            ↓
AbilityResult + événements typés
            ↓
présentation, journal, agents, narration
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Entrée :** la commande contient l’utilisateur, la compétence, les cibles proposées, le tick et les révisions attendues.
- **Préparation :** aucune autorité active n’est modifiée avant l’unité de travail.
- **Commit :** coût, effets, charge et recharge sont validés ensemble.
- **Sortie :** les consommateurs reçoivent seulement un résultat déjà committé.
- **Invariant :** une animation, un agent ou une prévisualisation ne devient jamais autorité.

## 5. Architecture retenue

> **[LECTURE] Arborescence cible — Ne pas créer depuis un terminal.**

```text
res://src/features/abilities/
├── domain/
│   ├── ability_id.gd
│   ├── ability_cost_definition.gd
│   ├── ability_target_definition.gd
│   ├── ability_effect_definition.gd
│   ├── damage_effect_definition.gd
│   ├── status_effect_definition.gd
│   ├── resource_effect_definition.gd
│   ├── ability_definition.gd
│   ├── ability_progression_state.gd
│   ├── ability_runtime_state.gd
│   ├── ability_use_command.gd
│   ├── ability_execution_plan.gd
│   └── ability_result.gd
├── application/
│   ├── ability_catalog.gd
│   ├── ability_repository.gd
│   ├── ability_resource_port.gd
│   ├── combat_ability_port.gd
│   ├── character_effect_port.gd
│   ├── ability_mutation_unit_of_work.gd
│   ├── ability_context_port.gd
│   ├── ability_progression_policy.gd
│   ├── ability_service.gd
│   └── ability_agent_action_executor.gd
├── infrastructure/
│   ├── ability_snapshot_codec.gd
│   └── ability_save_section.gd
└── presentation/
    └── ability_presentation_bridge.gd

res://data/abilities/
├── ember_bolt.tres
├── guardian_stance.tres
└── field_mend.tres

res://scenes/learning/
├── ch19_abilities_demo.tscn
└── ch19_abilities_demo.gd
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `domain` contient les données et invariants indépendants des scènes.
- `application` orchestre les ports et l’unité de travail.
- `infrastructure` encode la persistance.
- `presentation` consomme les résultats sans appliquer les règles.
- Le chapitre 20 pourra accorder une compétence depuis un objet sans déplacer son autorité dans l’inventaire.

## 6. Vocabulaire

Une **définition** est une `Resource` partagée et immuable pendant le gameplay.

Une **progression** indique si une compétence est débloquée, son rang et son expérience.

Un **état runtime** contient les charges disponibles, le prochain tick de récupération et la séquence d’utilisation.

Un **coût** est une quantité demandée à une ressource identifiée.

Un **effet** est une demande de mutation destinée à l’autorité propriétaire.

Un **candidat** est une mutation validée mais encore non committée.

Un **plan d’exécution** fige les données d’une utilisation précise.

## 7. Identifiants stables

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/domain/ability_id.gd`.**

```gdscript
class_name AbilityId
extends RefCounted

const DEFINITION_PREFIX := "ability.definition."
const USE_PREFIX := "ability.use."
const EVENT_PREFIX := "ability.event."

static func definition(slug: String) -> StringName:
	var normalized := slug.strip_edges().to_lower()
	if normalized.is_empty():
		return &""
	for character: String in normalized:
		var is_letter := character >= "a" and character <= "z"
		var is_digit := character >= "0" and character <= "9"
		if not is_letter and not is_digit and character != "_":
			return &""
	return StringName(DEFINITION_PREFIX + normalized)

static func use(
	ability_id: StringName,
	character_id: StringName,
	sequence: int,
) -> StringName:
	if not StableId.is_valid(ability_id):
		return &""
	if not CharacterId.is_valid(character_id) or sequence <= 0:
		return &""
	return StringName(
		"%s%s.%s.%d"
		% [USE_PREFIX, String(ability_id), String(character_id), sequence]
	)

static func event(use_id: StringName, sequence: int) -> StringName:
	if not StableId.is_valid(use_id) or sequence <= 0:
		return &""
	return StringName("%s%s.%d" % [EVENT_PREFIX, String(use_id), sequence])
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `definition()` normalise un slug en minuscules après suppression des espaces périphériques.
- `is_letter` et `is_digit` sont des booléens calculés pour chaque caractère.
- Seuls lettres ASCII minuscules, chiffres et `_` sont acceptés.
- `use()` corrèle définition, personnage et séquence.
- `event()` ajoute une séquence d’événement à l’utilisation.
- Une entrée invalide renvoie `&""`, jamais un identifiant partiel.

## 8. Décrire un coût

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/domain/ability_cost_definition.gd`.**

```gdscript
class_name AbilityCostDefinition
extends Resource

@export var resource_id: StringName
@export_range(0, 1000000, 1) var base_amount: int = 0
@export_range(0, 1000000, 1) var amount_per_rank: int = 0
@export var allow_zero := false

func amount_for_rank(rank: int) -> int:
	if rank < 1:
		return -1
	return base_amount + amount_per_rank * (rank - 1)

func validate() -> Error:
	if not StableId.is_valid(resource_id):
		return ERR_INVALID_DATA
	if base_amount < 0 or amount_per_rank < 0:
		return ERR_INVALID_DATA
	if not allow_zero and base_amount == 0:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `resource_id` désigne l’autorité réelle, par exemple endurance ou concentration.
- `base_amount` est le coût du rang 1.
- `amount_per_rank` ajoute un supplément pour chaque rang suivant.
- `amount_for_rank()` renvoie `-1` lorsque le rang est invalide.
- La définition ne retire aucune ressource ; elle décrit seulement un montant.

## 9. Décrire le ciblage

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/domain/ability_target_definition.gd`.**

```gdscript
class_name AbilityTargetDefinition
extends Resource

enum Mode {
	SELF,
	SINGLE_CHARACTER,
	POINT,
	AREA_AROUND_POINT,
}

enum Allegiance {
	ANY,
	SELF_ONLY,
	ALLY,
	ENEMY,
}

@export var mode: Mode = Mode.SINGLE_CHARACTER
@export var allegiance: Allegiance = Allegiance.ENEMY
@export_range(0.0, 1000.0, 0.1) var range_m := 2.0
@export_range(0.0, 1000.0, 0.1) var radius_m := 0.0
@export var requires_line_of_sight := true
@export_range(1, 128, 1) var maximum_targets := 1

func validate() -> Error:
	if mode < Mode.SELF or mode > Mode.AREA_AROUND_POINT:
		return ERR_INVALID_DATA
	if allegiance < Allegiance.ANY or allegiance > Allegiance.ENEMY:
		return ERR_INVALID_DATA
	if range_m < 0.0 or not is_finite(range_m):
		return ERR_INVALID_DATA
	if radius_m < 0.0 or not is_finite(radius_m):
		return ERR_INVALID_DATA
	if maximum_targets < 1 or maximum_targets > 128:
		return ERR_INVALID_DATA
	if mode == Mode.SELF:
		if allegiance != Allegiance.SELF_ONLY:
			return ERR_INVALID_DATA
		if range_m != 0.0 or radius_m != 0.0:
			return ERR_INVALID_DATA
	if mode == Mode.AREA_AROUND_POINT and radius_m <= 0.0:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `mode` décrit la forme de la commande.
- `allegiance` indique l’intention de conception ; le combat relit les côtés réels.
- `range_m` et `radius_m` utilisent les mètres Godot.
- `is_finite()` refuse `NaN` et les infinis.
- `maximum_targets` borne une sélection de zone.
- Le mode `SELF` impose une cible personnelle sans portée ni rayon.

## 10. Définir des effets composables

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/domain/ability_effect_definition.gd`.**

```gdscript
class_name AbilityEffectDefinition
extends Resource

@export var effect_id: StringName
@export_range(0, 1000, 1) var order: int = 0
@export var required := true

func validate() -> Error:
	if not StableId.is_valid(effect_id):
		return ERR_INVALID_DATA
	if order < 0 or order > 1000:
		return ERR_INVALID_DATA
	return OK

func duplicate_detached() -> AbilityEffectDefinition:
	return duplicate(true) as AbilityEffectDefinition
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `effect_id` sert à la corrélation et au diagnostic.
- `order` fixe un ordre canonique.
- `required` distingue un effet principal d’un effet optionnel.
- `duplicate(true)` demande une copie profonde des sous-ressources.
- Aucun nom de classe ou chemin externe n’est exécuté.

### 10.1 Dégâts demandés

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/domain/damage_effect_definition.gd`.**

```gdscript
class_name DamageEffectDefinition
extends AbilityEffectDefinition

@export var damage_type: DamagePacket.DamageType
@export_range(0, 100000000, 1) var base_amount: int = 0
@export_range(0, 100000000, 1) var amount_per_rank: int = 0
@export_range(0, 1000, 1) var armor_penetration_permille: int = 0

func amount_for_rank(rank: int) -> int:
	if rank < 1:
		return -1
	return base_amount + amount_per_rank * (rank - 1)

func validate() -> Error:
	if super.validate() != OK:
		return ERR_INVALID_DATA
	if damage_type < DamagePacket.DamageType.PHYSICAL:
		return ERR_INVALID_DATA
	if damage_type > DamagePacket.DamageType.ARCANE:
		return ERR_INVALID_DATA
	if base_amount < 0 or amount_per_rank < 0:
		return ERR_INVALID_DATA
	if armor_penetration_permille < 0:
		return ERR_INVALID_DATA
	if armor_penetration_permille > 1000:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’effet fournit un montant brut par rang.
- Le type et la pénétration réutilisent les contrats du combat.
- Il ne lit ni armure, ni résistance, ni garde.
- Le résultat final appartient à `DamageResolver`.

### 10.2 État demandé

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/domain/status_effect_definition.gd`.**

```gdscript
class_name StatusEffectDefinition
extends AbilityEffectDefinition

@export var status_definition_id: StringName
@export_range(1, 1000000, 1) var duration_ticks: int = 60
@export_range(1, 100000, 1) var stacks: int = 1

func validate() -> Error:
	if super.validate() != OK:
		return ERR_INVALID_DATA
	if not StableId.is_valid(status_definition_id):
		return ERR_INVALID_DATA
	if duration_ticks < 1 or stacks < 1:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `status_definition_id` référence un état autorisé.
- `duration_ticks` utilise la chronologie logique.
- `stacks` est une demande ; la politique de combat peut la borner ou la refuser.
- La compétence ne modifie pas directement `active_statuses`.

### 10.3 Ressource demandée

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/domain/resource_effect_definition.gd`.**

```gdscript
class_name ResourceEffectDefinition
extends AbilityEffectDefinition

@export var resource_id: StringName
@export_range(-1000000, 1000000, 1) var base_delta: int = 0
@export_range(-1000000, 1000000, 1) var delta_per_rank: int = 0

func delta_for_rank(rank: int) -> Variant:
	if rank < 1:
		return null
	return base_delta + delta_per_rank * (rank - 1)

func validate() -> Error:
	if super.validate() != OK:
		return ERR_INVALID_DATA
	if not StableId.is_valid(resource_id):
		return ERR_INVALID_DATA
	if base_delta == 0 and delta_per_rank == 0:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Un delta positif restaure ; un delta négatif consomme.
- `Variant` permet de distinguer l’entier `0` de `null`.
- Le port propriétaire borne la valeur.
- Un soin de santé passe par `CharacterRules`.

## 11. Définition complète d’une compétence

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/domain/ability_definition.gd`.**

```gdscript
class_name AbilityDefinition
extends Resource

@export var ability_id: StringName
@export var display_name_key: StringName
@export var description_key: StringName
@export_range(1, 100, 1) var maximum_rank: int = 1
@export_range(0, 1000000, 1) var base_cooldown_ticks: int = 0
@export_range(0, 1000000, 1) var cooldown_reduction_per_rank: int = 0
@export_range(1, 99, 1) var maximum_charges: int = 1
@export var costs: Array[AbilityCostDefinition] = []
@export var target: AbilityTargetDefinition
@export var effects: Array[AbilityEffectDefinition] = []

func cooldown_for_rank(rank: int) -> int:
	if rank < 1 or rank > maximum_rank:
		return -1
	var reduction := cooldown_reduction_per_rank * (rank - 1)
	return maxi(0, base_cooldown_ticks - reduction)

func validate() -> Error:
	if not StableId.is_valid(ability_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(display_name_key):
		return ERR_INVALID_DATA
	if not StableId.is_valid(description_key):
		return ERR_INVALID_DATA
	if maximum_rank < 1 or maximum_rank > 100:
		return ERR_INVALID_DATA
	if base_cooldown_ticks < 0 or cooldown_reduction_per_rank < 0:
		return ERR_INVALID_DATA
	if maximum_charges < 1 or maximum_charges > 99:
		return ERR_INVALID_DATA
	if target == null or target.validate() != OK:
		return ERR_INVALID_DATA
	if effects.is_empty() or effects.size() > 32:
		return ERR_INVALID_DATA

	var seen_costs: Dictionary[StringName, bool] = {}
	for cost: AbilityCostDefinition in costs:
		if cost == null or cost.validate() != OK:
			return ERR_INVALID_DATA
		if seen_costs.has(cost.resource_id):
			return ERR_ALREADY_EXISTS
		seen_costs[cost.resource_id] = true

	var previous_order := -1
	var seen_effects: Dictionary[StringName, bool] = {}
	for effect: AbilityEffectDefinition in effects:
		if effect == null or effect.validate() != OK:
			return ERR_INVALID_DATA
		if seen_effects.has(effect.effect_id):
			return ERR_ALREADY_EXISTS
		if effect.order < previous_order:
			return ERR_INVALID_DATA
		seen_effects[effect.effect_id] = true
		previous_order = effect.order
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les clés d’affichage restent séparées de l’identité métier.
- `cooldown_for_rank()` ne renvoie jamais une recharge négative.
- Les coûts d’une même ressource sont uniques.
- Les effets sont bornés, uniques et déjà triés.
- Le validateur refuse une définition incohérente au lieu de la corriger silencieusement.
- La `Resource` reste immuable pendant le gameplay.

## 12. Créer une compétence dans Godot

> **[APP] Godot — Créer `res://data/abilities/ember_bolt.tres` depuis `AbilityDefinition`.**

Valeurs pédagogiques :

- `ability_id` : `ability.definition.ember_bolt` ;
- rang maximal : `5` ;
- recharge : `180` ticks ;
- réduction : `12` ticks par rang ;
- une charge ;
- coût : `ability.resource.focus` ;
- ciblage : personnage ennemi, portée `18.0` m, ligne de vue requise ;
- effet : dégâts de feu.

> **[LECTURE] Résultat attendu — Ne pas saisir.**

```text
La ressource est acceptée seulement si :
- tous les identifiants sont stables ;
- les coûts sont uniques ;
- le ciblage est cohérent ;
- les effets sont valides et ordonnés ;
- les rangs, charges et recharges sont bornés.
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Cette sortie décrit les invariants de `validate()`.
- Le `.tres` ne contient ni charge courante ni tick runtime.
- Plusieurs personnages peuvent partager la même définition.

## 13. Catalogue de définitions

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/application/ability_catalog.gd`.**

```gdscript
class_name AbilityCatalog
extends RefCounted

var _definitions: Dictionary[StringName, AbilityDefinition] = {}

func register(definition: AbilityDefinition) -> Error:
	if definition == null or definition.validate() != OK:
		return ERR_INVALID_DATA
	if _definitions.has(definition.ability_id):
		return ERR_ALREADY_EXISTS
	_definitions[definition.ability_id] = (
		definition.duplicate(true) as AbilityDefinition
	)
	return OK

func get_definition(ability_id: StringName) -> AbilityDefinition:
	var stored := _definitions.get(ability_id) as AbilityDefinition
	if stored == null:
		return null
	return stored.duplicate(true) as AbilityDefinition

func all_ids_sorted() -> Array[StringName]:
	var ids: Array[StringName] = []
	ids.assign(_definitions.keys())
	ids.sort()
	return ids
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le catalogue refuse une définition invalide ou dupliquée.
- Il conserve une copie profonde.
- Il renvoie aussi une copie afin de protéger l’autorité interne.
- Les identifiants triés donnent un ordre stable.

## 14. Progression et état runtime

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/domain/ability_progression_state.gd`.**

```gdscript
class_name AbilityProgressionState
extends RefCounted

var ability_id: StringName
var unlocked := false
var rank: int = 0
var experience: int = 0

func validate(definition: AbilityDefinition) -> Error:
	if definition == null or definition.validate() != OK:
		return ERR_UNCONFIGURED
	if ability_id != definition.ability_id:
		return ERR_INVALID_DATA
	if rank < 0 or rank > definition.maximum_rank:
		return ERR_INVALID_DATA
	if unlocked and rank < 1:
		return ERR_INVALID_DATA
	if not unlocked and rank != 0:
		return ERR_INVALID_DATA
	if experience < 0 or experience > 9007199254740991:
		return ERR_INVALID_DATA
	return OK

func duplicate_detached() -> AbilityProgressionState:
	var copy := AbilityProgressionState.new()
	copy.ability_id = ability_id
	copy.unlocked = unlocked
	copy.rank = rank
	copy.experience = experience
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Une compétence verrouillée possède un rang `0`.
- Une compétence débloquée possède au moins le rang `1`.
- L’expérience reste dans la plage entière JSON sûre.
- La copie détachée protège le dépôt.

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/domain/ability_runtime_state.gd`.**

```gdscript
class_name AbilityRuntimeState
extends RefCounted

var ability_id: StringName
var available_charges: int = 0
var next_charge_tick: int = 0
var use_sequence: int = 0

func validate(definition: AbilityDefinition) -> Error:
	if definition == null or definition.validate() != OK:
		return ERR_UNCONFIGURED
	if ability_id != definition.ability_id:
		return ERR_INVALID_DATA
	if available_charges < 0:
		return ERR_INVALID_DATA
	if available_charges > definition.maximum_charges:
		return ERR_INVALID_DATA
	if next_charge_tick < 0 or use_sequence < 0:
		return ERR_INVALID_DATA
	if available_charges == definition.maximum_charges:
		if next_charge_tick != 0:
			return ERR_INVALID_DATA
	return OK

func refresh_charges(
	definition: AbilityDefinition,
	rank: int,
	logical_tick: int,
) -> Error:
	if validate(definition) != OK:
		return ERR_INVALID_DATA
	if logical_tick < 0:
		return ERR_INVALID_PARAMETER
	var cooldown := definition.cooldown_for_rank(rank)
	if cooldown < 0:
		return ERR_INVALID_DATA
	while (
		available_charges < definition.maximum_charges
		and next_charge_tick > 0
		and logical_tick >= next_charge_tick
	):
		available_charges += 1
		if available_charges == definition.maximum_charges:
			next_charge_tick = 0
		else:
			next_charge_tick += cooldown
	return OK

func duplicate_detached() -> AbilityRuntimeState:
	var copy := AbilityRuntimeState.new()
	copy.ability_id = ability_id
	copy.available_charges = available_charges
	copy.next_charge_tick = next_charge_tick
	copy.use_sequence = use_sequence
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `available_charges` compte les utilisations immédiates.
- `next_charge_tick` est zéro lorsqu’aucune recharge n’est en cours.
- La boucle récupère plusieurs charges après une longue simulation hors écran.
- Le tick logique remplace l’heure système et les `Timer`.
- L’état ne contient aucune référence de scène.

## 15. Politique de progression

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/application/ability_progression_policy.gd`.**

```gdscript
class_name AbilityProgressionPolicy
extends RefCounted

func experience_required_for_rank(rank: int) -> int:
	if rank < 1 or rank > 100:
		return -1
	return 100 * rank * rank

func grant_experience(
	state: AbilityProgressionState,
	definition: AbilityDefinition,
	amount: int,
) -> Error:
	if state == null or definition == null:
		return ERR_INVALID_PARAMETER
	if state.validate(definition) != OK:
		return ERR_INVALID_DATA
	if amount <= 0:
		return ERR_INVALID_PARAMETER
	if not state.unlocked:
		return ERR_UNAVAILABLE

	state.experience += amount
	while state.rank < definition.maximum_rank:
		var next_rank := state.rank + 1
		var required := experience_required_for_rank(next_rank)
		if required < 0 or state.experience < required:
			break
		state.rank = next_rank
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La formule est un exemple d’équilibrage, pas une norme universelle.
- L’expérience est cumulative.
- La boucle peut gagner plusieurs rangs après une récompense importante.
- La compétence doit être débloquée.
- Un changement futur de formule devra être versionné si les sauvegardes en dépendent.

## 16. Commande et résultat

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/domain/ability_use_command.gd`.**

```gdscript
class_name AbilityUseCommand
extends RefCounted

var use_id: StringName
var user_character_id: StringName
var ability_id: StringName
var target_character_ids: Array[StringName] = []
var target_point := Vector3.ZERO
var has_target_point := false
var requested_tick: int = 0
var expected_world_revision: int = 0
var expected_ability_revision: int = 0

func validate() -> Error:
	if not StableId.is_valid(use_id):
		return ERR_INVALID_DATA
	if not CharacterId.is_valid(user_character_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(ability_id):
		return ERR_INVALID_DATA
	if requested_tick < 0:
		return ERR_INVALID_DATA
	if expected_world_revision < 0 or expected_ability_revision < 0:
		return ERR_INVALID_DATA
	if has_target_point and not target_point.is_finite():
		return ERR_INVALID_DATA
	var seen: Dictionary[StringName, bool] = {}
	for target_id: StringName in target_character_ids:
		if not CharacterId.is_valid(target_id):
			return ERR_INVALID_DATA
		if seen.has(target_id):
			return ERR_ALREADY_EXISTS
		seen[target_id] = true
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La commande contient des cibles proposées, pas des cibles déjà autorisées.
- `has_target_point` distingue l’origine valide de l’absence de point.
- Les deux révisions protègent contre un monde ou un état de compétence obsolète.
- Les cibles sont valides et uniques.
- La commande ne contient ni coût final ni dégâts.

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/domain/ability_result.gd`.**

```gdscript
class_name AbilityResult
extends RefCounted

enum Status {
	RESOLVED,
	PARTIALLY_RESOLVED,
	REJECTED_INVALID_COMMAND,
	REJECTED_UNKNOWN_ABILITY,
	REJECTED_LOCKED,
	REJECTED_NO_CHARGE,
	REJECTED_COST,
	REJECTED_TARGET,
	REJECTED_STALE_REVISION,
	REJECTED_EFFECT,
	REJECTED_RESOURCE,
}

var status: Status
var use_id: StringName
var ability_id: StringName
var user_character_id: StringName
var prepared_effect_ids: Array[StringName] = []
var rejected_effect_ids: Array[StringName] = []
var message: String = ""

func is_success() -> bool:
	return status in [Status.RESOLVED, Status.PARTIALLY_RESOLVED]

func validate() -> Error:
	if status < Status.RESOLVED or status > Status.REJECTED_RESOURCE:
		return ERR_INVALID_DATA
	if not use_id.is_empty() and not StableId.is_valid(use_id):
		return ERR_INVALID_DATA
	if not ability_id.is_empty() and not StableId.is_valid(ability_id):
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `RESOLVED` et `PARTIALLY_RESOLVED` sont des utilisations consommées.
- Un effet optionnel peut être refusé sans annuler les candidats requis.
- Les identifiants préparés deviennent observables seulement après commit.
- `is_success()` empêche un retry gratuit d’un résultat partiel.

## 17. Plan d’exécution

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/domain/ability_execution_plan.gd`.**

```gdscript
class_name AbilityExecutionPlan
extends RefCounted

var use_id: StringName
var ability_id: StringName
var user_character_id: StringName
var rank: int = 0
var logical_tick: int = 0
var target_character_ids: Array[StringName] = []
var target_point := Vector3.ZERO
var has_target_point := false
var effects: Array[AbilityEffectDefinition] = []

func validate(definition: AbilityDefinition) -> Error:
	if definition == null or definition.validate() != OK:
		return ERR_UNCONFIGURED
	if not StableId.is_valid(use_id):
		return ERR_INVALID_DATA
	if ability_id != definition.ability_id:
		return ERR_INVALID_DATA
	if not CharacterId.is_valid(user_character_id):
		return ERR_INVALID_DATA
	if rank < 1 or rank > definition.maximum_rank:
		return ERR_INVALID_DATA
	if logical_tick < 0:
		return ERR_INVALID_DATA
	if has_target_point and not target_point.is_finite():
		return ERR_INVALID_DATA
	if effects.size() != definition.effects.size():
		return ERR_INVALID_DATA
	for index in effects.size():
		if effects[index] == null or effects[index].validate() != OK:
			return ERR_INVALID_DATA
		if effects[index].effect_id != definition.effects[index].effect_id:
			return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le plan fige rang, tick, cibles et effets.
- Les effets sont comparés à la définition par index et identifiant.
- Le plan ne contient ni défense ni résultat de dégâts.
- Il ne contient aucun nœud.
- Il est traité comme immuable après construction.

## 18. Ports de préparation

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/application/ability_resource_port.gd`.**

```gdscript
class_name AbilityResourcePort
extends RefCounted

class Reservation:
	extends RefCounted

	var reservation_id: StringName
	var character_id: StringName
	var amounts: Dictionary[StringName, int] = {}

	func validate() -> Error:
		if not StableId.is_valid(reservation_id):
			return ERR_INVALID_DATA
		if not CharacterId.is_valid(character_id):
			return ERR_INVALID_DATA
		for resource_id: StringName in amounts:
			if not StableId.is_valid(resource_id):
				return ERR_INVALID_DATA
			if amounts[resource_id] < 0:
				return ERR_INVALID_DATA
		return OK

func prepare_reservation(
	character_id: StringName,
	reservation_id: StringName,
	costs: Dictionary[StringName, int],
	expected_world_revision: int,
) -> Reservation:
	return null

func cancel_reservation(_reservation: Reservation) -> void:
	pass
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La réservation vérifie les ressources sans les consommer.
- Les montants sont positifs ou nuls et associés à des identifiants stables.
- Le commit n’existe pas sur ce port afin d’éviter un coût isolé.
- `cancel_reservation()` libère le candidat abandonné.

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/application/ability_mutation_unit_of_work.gd`.**

```gdscript
class_name AbilityMutationUnitOfWork
extends RefCounted

class EffectCandidate:
	extends RefCounted

	var effect_id: StringName
	var authority_id: StringName
	var payload: Dictionary = {}

	func validate() -> Error:
		if not StableId.is_valid(effect_id):
			return ERR_INVALID_DATA
		if not StableId.is_valid(authority_id):
			return ERR_INVALID_DATA
		if payload.is_empty():
			return ERR_INVALID_DATA
		return OK

func commit(
	reservation: AbilityResourcePort.Reservation,
	effect_candidates: Array[EffectCandidate],
	character_id: StringName,
	progression: AbilityProgressionState,
	runtime: AbilityRuntimeState,
	expected_world_revision: int,
	expected_ability_revision: int,
) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Un candidat possède l’identité de son effet et de son autorité.
- `payload` est construit par un port fiable ; aucune donnée joueur ne choisit une méthode.
- `commit()` reçoit coût, effets, progression, runtime et révisions.
- L’implémentation revalide tous les candidats avant de préparer les swaps.
- Aucun premier remplacement ne doit pouvoir réussir si un remplacement suivant peut encore échouer.
- Cette atomicité est une exigence à tester au chapitre 27, pas un test runtime revendiqué ici.

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/application/combat_ability_port.gd`.**

```gdscript
class_name CombatAbilityPort
extends RefCounted

func prepare_damage_effect(
	plan: AbilityExecutionPlan,
	effect: DamageEffectDefinition,
	target_id: StringName,
	expected_world_revision: int,
) -> AbilityMutationUnitOfWork.EffectCandidate:
	return null

func prepare_status_effect(
	plan: AbilityExecutionPlan,
	effect: StatusEffectDefinition,
	target_id: StringName,
	expected_world_revision: int,
) -> AbilityMutationUnitOfWork.EffectCandidate:
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le combat relit cible, portée, ligne de vue, défense et état de vie.
- Il prépare un candidat, mais ne commit rien à cette étape.
- `null` représente un refus contrôlé.
- Le service de compétences ne connaît pas les calculs de combat.

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/application/character_effect_port.gd`.**

```gdscript
class_name CharacterEffectPort
extends RefCounted

func prepare_resource_effect(
	plan: AbilityExecutionPlan,
	effect: ResourceEffectDefinition,
	target_id: StringName,
	expected_world_revision: int,
) -> AbilityMutationUnitOfWork.EffectCandidate:
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le port prépare santé, endurance ou une ressource dédiée.
- Les règles de personnage bornent les valeurs.
- Aucun état actif n’est modifié.
- Le candidat sera committé avec les autres autorités.

## 19. Dépôt et contexte

> **[LECTURE] Contrat du dépôt — Structure de référence.**

```gdscript
class_name AbilityRepository
extends RefCounted

func get_progression(
	character_id: StringName,
	ability_id: StringName,
) -> AbilityProgressionState:
	return null

func get_runtime(
	character_id: StringName,
	ability_id: StringName,
) -> AbilityRuntimeState:
	return null

func revision_for(character_id: StringName) -> int:
	return -1

func replace_all(prepared: Dictionary) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les lectures retournent des copies détachées.
- La révision est portée par personnage.
- Le dépôt ne calcule ni coûts ni effets.
- `replace_all()` sert à une restauration complète préparée.

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/application/ability_context_port.gd`.**

```gdscript
class_name AbilityContextPort
extends RefCounted

class Context:
	extends RefCounted

	var ability_revision: int = 0

	func validate() -> Error:
		return OK if ability_revision >= 0 else ERR_INVALID_DATA

func snapshot_for(_character_id: StringName) -> Context:
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le port fournit une révision fraîche à un adaptateur.
- Il n’expose ni dépôt ni progression mutable.
- `null` signifie qu’aucun contexte n’est disponible.
- Le service et l’unité de travail recontrôlent ensuite la révision.

## 20. Construire les coûts et la forme de cible

> **[LECTURE] Fonctions internes de `AbilityService` — Ne pas saisir séparément.**

```gdscript
func _build_costs(
	definition: AbilityDefinition,
	rank: int,
) -> Dictionary[StringName, int]:
	var result: Dictionary[StringName, int] = {}
	for cost: AbilityCostDefinition in definition.costs:
		var amount := cost.amount_for_rank(rank)
		if amount < 0:
			return {}
		result[cost.resource_id] = amount
	return result

func _validate_target_shape(
	command: AbilityUseCommand,
	target: AbilityTargetDefinition,
) -> Error:
	if target == null or target.validate() != OK:
		return ERR_UNCONFIGURED
	match target.mode:
		AbilityTargetDefinition.Mode.SELF:
			if not command.target_character_ids.is_empty():
				return ERR_INVALID_DATA
			if command.has_target_point:
				return ERR_INVALID_DATA
		AbilityTargetDefinition.Mode.SINGLE_CHARACTER:
			if command.target_character_ids.size() != 1:
				return ERR_INVALID_DATA
			if command.has_target_point:
				return ERR_INVALID_DATA
		AbilityTargetDefinition.Mode.POINT:
			if not command.target_character_ids.is_empty():
				return ERR_INVALID_DATA
			if not command.has_target_point:
				return ERR_INVALID_DATA
		AbilityTargetDefinition.Mode.AREA_AROUND_POINT:
			if not command.has_target_point:
				return ERR_INVALID_DATA
			if command.target_character_ids.size() > target.maximum_targets:
				return ERR_INVALID_DATA
		_:
			return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `_build_costs()` calcule un montant par ressource.
- Un dictionnaire vide peut être une compétence gratuite ; l’appelant compare aussi le nombre de coûts.
- `_validate_target_shape()` vérifie la cohérence du payload.
- Elle ne valide pas la portée ou l’allégeance réelle.
- Un point à l’origine reste valide grâce à `has_target_point`.

## 21. Construire le plan et les cibles initiales

> **[LECTURE] Construction déterministe — Suite de `ability_service.gd`.**

```gdscript
func _build_plan(
	command: AbilityUseCommand,
	definition: AbilityDefinition,
	rank: int,
) -> AbilityExecutionPlan:
	var plan := AbilityExecutionPlan.new()
	plan.use_id = command.use_id
	plan.ability_id = command.ability_id
	plan.user_character_id = command.user_character_id
	plan.rank = rank
	plan.logical_tick = command.requested_tick
	plan.target_character_ids.assign(command.target_character_ids)
	plan.target_character_ids.sort()
	plan.target_point = command.target_point
	plan.has_target_point = command.has_target_point
	for effect: AbilityEffectDefinition in definition.effects:
		plan.effects.append(effect.duplicate_detached())
	return plan

func _effective_targets(
	plan: AbilityExecutionPlan,
	target: AbilityTargetDefinition,
) -> Array[StringName]:
	var result: Array[StringName] = []
	if target.mode == AbilityTargetDefinition.Mode.SELF:
		result.append(plan.user_character_id)
	else:
		result.assign(plan.target_character_ids)
	result.sort()
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les cibles sont triées afin de produire un ordre stable.
- Les effets sont copiés profondément.
- `SELF` produit explicitement l’utilisateur.
- Une liste de zone reste candidate ; le combat la filtre.
- Le plan ne lit aucun dépôt après construction.

## 22. Préparer les effets

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/application/ability_service.gd`.**

```gdscript
class_name AbilityService
extends RefCounted

signal ability_resolved(result: AbilityResult)

class PreparedUse:
	extends RefCounted

	var result: AbilityResult
	var candidates: Array[AbilityMutationUnitOfWork.EffectCandidate] = []

var _catalog: AbilityCatalog
var _repository: AbilityRepository
var _resources: AbilityResourcePort
var _combat_port: CombatAbilityPort
var _character_port: CharacterEffectPort
var _unit_of_work: AbilityMutationUnitOfWork

func _prepare_one_effect(
	plan: AbilityExecutionPlan,
	effect: AbilityEffectDefinition,
	target_id: StringName,
	expected_world_revision: int,
) -> AbilityMutationUnitOfWork.EffectCandidate:
	if effect is DamageEffectDefinition:
		if _combat_port == null:
			return null
		return _combat_port.prepare_damage_effect(
			plan,
			effect as DamageEffectDefinition,
			target_id,
			expected_world_revision,
		)
	if effect is StatusEffectDefinition:
		if _combat_port == null:
			return null
		return _combat_port.prepare_status_effect(
			plan,
			effect as StatusEffectDefinition,
			target_id,
			expected_world_revision,
		)
	if effect is ResourceEffectDefinition:
		if _character_port == null:
			return null
		return _character_port.prepare_resource_effect(
			plan,
			effect as ResourceEffectDefinition,
			target_id,
			expected_world_revision,
		)
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `PreparedUse` regroupe un résultat provisoire et des candidats.
- Le dispatch est fermé sur trois types autorisés.
- Aucun chemin ou nom de classe fourni par les données n’est chargé.
- Chaque port prépare un candidat sans mutation active.
- Un type inconnu renvoie `null`.

> **[LECTURE] Agrégation des candidats — Suite du même fichier.**

```gdscript
func _prepare_effects(
	plan: AbilityExecutionPlan,
	definition: AbilityDefinition,
	expected_world_revision: int,
) -> PreparedUse:
	var prepared := PreparedUse.new()
	prepared.result = _result(
		AbilityResult.Status.RESOLVED,
		null,
		"compétence préparée",
	)
	prepared.result.use_id = plan.use_id
	prepared.result.ability_id = plan.ability_id
	prepared.result.user_character_id = plan.user_character_id

	var targets := _effective_targets(plan, definition.target)
	for effect: AbilityEffectDefinition in plan.effects:
		var effect_prepared := false
		for target_id: StringName in targets:
			var candidate := _prepare_one_effect(
				plan,
				effect,
				target_id,
				expected_world_revision,
			)
			if candidate != null and candidate.validate() == OK:
				prepared.candidates.append(candidate)
				effect_prepared = true
			elif effect.required:
				prepared.result.status = AbilityResult.Status.REJECTED_EFFECT
				prepared.result.message = "effet requis refusé"
				prepared.result.rejected_effect_ids.append(effect.effect_id)
				return prepared
		if effect_prepared:
			prepared.result.prepared_effect_ids.append(effect.effect_id)
		else:
			prepared.result.rejected_effect_ids.append(effect.effect_id)

	if not prepared.result.rejected_effect_ids.is_empty():
		prepared.result.status = AbilityResult.Status.PARTIALLY_RESOLVED
	return prepared
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Chaque effet est préparé pour les cibles initiales.
- Un effet requis absent arrête la préparation.
- Un effet optionnel absent produit un résultat partiel.
- `prepared_effect_ids` signifie « candidat prêt » jusqu’au commit.
- Les candidats ne deviennent observables qu’après réussite de l’unité de travail.

## 23. Exécuter une utilisation

> **[LECTURE] Entrée unique du service — Suite de `ability_service.gd`.**

```gdscript
func execute(command: AbilityUseCommand) -> AbilityResult:
	if command == null or command.validate() != OK:
		return _result(
			AbilityResult.Status.REJECTED_INVALID_COMMAND,
			command,
			"commande invalide",
		)
	if (
		_catalog == null
		or _repository == null
		or _resources == null
		or _unit_of_work == null
	):
		return _result(
			AbilityResult.Status.REJECTED_RESOURCE,
			command,
			"services obligatoires indisponibles",
		)

	var definition := _catalog.get_definition(command.ability_id)
	if definition == null or definition.validate() != OK:
		return _result(
			AbilityResult.Status.REJECTED_UNKNOWN_ABILITY,
			command,
			"compétence inconnue",
		)

	var progression := _repository.get_progression(
		command.user_character_id,
		command.ability_id,
	)
	var runtime := _repository.get_runtime(
		command.user_character_id,
		command.ability_id,
	)
	if progression == null or runtime == null:
		return _result(
			AbilityResult.Status.REJECTED_LOCKED,
			command,
			"compétence non apprise",
		)
	if progression.validate(definition) != OK or not progression.unlocked:
		return _result(
			AbilityResult.Status.REJECTED_LOCKED,
			command,
			"progression invalide ou verrouillée",
		)
	if runtime.validate(definition) != OK:
		return _result(
			AbilityResult.Status.REJECTED_RESOURCE,
			command,
			"état runtime invalide",
		)
	if _repository.revision_for(command.user_character_id) != (
		command.expected_ability_revision
	):
		return _result(
			AbilityResult.Status.REJECTED_STALE_REVISION,
			command,
			"révision de compétence obsolète",
		)

	var refresh_code := runtime.refresh_charges(
		definition,
		progression.rank,
		command.requested_tick,
	)
	if refresh_code != OK:
		return _result(
			AbilityResult.Status.REJECTED_RESOURCE,
			command,
			"recharge invalide",
		)
	if runtime.available_charges <= 0:
		return _result(
			AbilityResult.Status.REJECTED_NO_CHARGE,
			command,
			"aucune charge disponible",
		)
	if _validate_target_shape(command, definition.target) != OK:
		return _result(
			AbilityResult.Status.REJECTED_TARGET,
			command,
			"forme de cible invalide",
		)
	return _execute_prepared(command, definition, progression, runtime)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les validations communes précèdent toute réservation.
- La recharge est recalculée sur une copie runtime.
- La révision du dépôt est comparée à celle de la commande.
- Une absence de charge est un refus normal.
- La forme de cible est vérifiée avant les ports propriétaires.

> **[LECTURE] Préparation et commit — Suite de `ability_service.gd`.**

```gdscript
func _execute_prepared(
	command: AbilityUseCommand,
	definition: AbilityDefinition,
	progression: AbilityProgressionState,
	runtime: AbilityRuntimeState,
) -> AbilityResult:
	var costs := _build_costs(definition, progression.rank)
	if costs.size() != definition.costs.size():
		return _result(
			AbilityResult.Status.REJECTED_COST,
			command,
			"coûts invalides",
		)

	var reservation := _resources.prepare_reservation(
		command.user_character_id,
		command.use_id,
		costs,
		command.expected_world_revision,
	)
	if reservation == null or reservation.validate() != OK:
		return _result(
			AbilityResult.Status.REJECTED_COST,
			command,
			"ressources insuffisantes",
		)

	var plan := _build_plan(command, definition, progression.rank)
	if plan == null or plan.validate(definition) != OK:
		_resources.cancel_reservation(reservation)
		return _result(
			AbilityResult.Status.REJECTED_RESOURCE,
			command,
			"plan invalide",
		)

	var prepared := _prepare_effects(
		plan,
		definition,
		command.expected_world_revision,
	)
	if prepared == null or prepared.result == null:
		_resources.cancel_reservation(reservation)
		return _result(
			AbilityResult.Status.REJECTED_RESOURCE,
			command,
			"préparation des effets impossible",
		)
	if not prepared.result.is_success():
		_resources.cancel_reservation(reservation)
		return prepared.result

	var runtime_candidate := runtime.duplicate_detached()
	runtime_candidate.available_charges -= 1
	runtime_candidate.use_sequence += 1
	if runtime_candidate.available_charges < definition.maximum_charges:
		if runtime_candidate.next_charge_tick == 0:
			var cooldown := definition.cooldown_for_rank(progression.rank)
			runtime_candidate.next_charge_tick = (
				command.requested_tick + cooldown
			)

	var commit_code := _unit_of_work.commit(
		reservation,
		prepared.candidates,
		command.user_character_id,
		progression.duplicate_detached(),
		runtime_candidate,
		command.expected_world_revision,
		command.expected_ability_revision,
	)
	if commit_code != OK:
		_resources.cancel_reservation(reservation)
		var status := AbilityResult.Status.REJECTED_RESOURCE
		if commit_code == ERR_BUSY:
			status = AbilityResult.Status.REJECTED_STALE_REVISION
		return _result(
			status,
			command,
			"commit refusé : %s" % error_string(commit_code),
		)

	ability_resolved.emit(prepared.result)
	return prepared.result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Coûts, plan, effets et état runtime sont préparés avant toute mutation active.
- Un refus annule la réservation.
- La charge et la recharge sont modifiées sur un candidat.
- L’unité de travail reçoit le lot complet.
- `ERR_BUSY` représente une révision devenue obsolète.
- Le signal est émis seulement après commit réussi.

> **[LECTURE] Fabrique de résultat — Suite de `ability_service.gd`.**

```gdscript
func _result(
	status: AbilityResult.Status,
	command: AbilityUseCommand,
	message: String,
) -> AbilityResult:
	var result := AbilityResult.new()
	result.status = status
	result.message = message
	if command != null:
		result.use_id = command.use_id
		result.ability_id = command.ability_id
		result.user_character_id = command.user_character_id
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La fonction centralise les statuts et messages.
- Elle recopie uniquement des identifiants.
- Elle accepte `null` pour construire un résultat depuis un plan déjà validé.
- Elle ne conserve pas la commande mutable.

## 24. Adapter une action d’agent

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/application/ability_agent_action_executor.gd`.**

```gdscript
class_name AbilityAgentActionExecutor
extends AgentActionExecutor

const EXECUTOR_KEY := &"agent.executor.ability_use"

var _ability_service: AbilityService
var _ability_context: AbilityContextPort

func can_execute(request: AgentActionRequest) -> Error:
	if request == null or request.validate() != OK:
		return ERR_INVALID_DATA
	if request.executor_key != EXECUTOR_KEY:
		return ERR_UNAVAILABLE
	if not StableId.is_valid(request.action_id):
		return ERR_INVALID_DATA
	if _ability_service == null or _ability_context == null:
		return ERR_UNCONFIGURED
	return OK

func start(request: AgentActionRequest) -> Error:
	var check := can_execute(request)
	if check != OK:
		return check
	var context := _ability_context.snapshot_for(
		request.owner_character_id
	)
	if context == null or context.validate() != OK:
		return ERR_DOES_NOT_EXIST

	var command := AbilityUseCommand.new()
	command.use_id = AbilityId.use(
		request.action_id,
		request.owner_character_id,
		request.decision_sequence,
	)
	command.user_character_id = request.owner_character_id
	command.ability_id = request.action_id
	if CharacterId.is_valid(request.target_character_id):
		command.target_character_ids.append(request.target_character_id)
	command.requested_tick = request.logical_tick
	command.expected_world_revision = request.snapshot_revision
	command.expected_ability_revision = context.ability_revision

	var result := _ability_service.execute(command)
	return OK if result.is_success() else ERR_CANT_RESOLVE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’agent choisit une définition connue et une cible proposée.
- Il ne fournit ni coût, ni recharge, ni dégâts.
- La révision de compétence est relue avant construction.
- Un résultat partiel est une utilisation consommée.
- Les ciblages par point ou zone exigent un adaptateur spécialisé.

## 25. Entrée du joueur et prévisualisation

L’interface peut afficher :

- coût estimé ;
- charges ;
- temps restant ;
- portée et zone ;
- cibles survolées ;
- description localisée.

Elle ne garantit jamais le résultat. La cible peut se déplacer, mourir, changer de côté ou rendre la révision obsolète entre la prévisualisation et le clic.

> **[LECTURE] Séparation interface / autorité — Ne pas saisir.**

```text
interface :
- propose une cible ;
- affiche une estimation ;
- construit AbilityUseCommand.

service et ports :
- relisent les révisions ;
- préparent ressources et effets ;
- valident les règles propriétaires ;
- commit le lot.
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La même commande peut venir d’un joueur, d’un agent ou d’un scénario.
- L’interface ne duplique pas les règles métier.
- Une couleur verte est une aide visuelle, pas une autorisation.

## 26. Persistance

Sont persistés par `CharacterId` :

- révision ;
- identifiant de compétence ;
- déblocage ;
- rang ;
- expérience ;
- charges disponibles ;
- prochain tick de récupération ;
- séquence d’utilisation.

Ne sont pas persistés :

- définitions `.tres` ;
- plans ;
- réservations ;
- candidats d’effets ;
- prévisualisations ;
- cibles dérivées ;
- portée et ligne de vue ;
- animations, sons et VFX ;
- caches de catalogue.

## 27. Codec strict

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/infrastructure/ability_snapshot_codec.gd`.**

```gdscript
class_name AbilitySnapshotCodec
extends RefCounted

const FORMAT := "project-asteria-abilities"
const VERSION := 1
const ROOT_KEYS := ["format", "version", "characters"]
const CHARACTER_KEYS := ["character_id", "revision", "abilities"]
const ABILITY_KEYS := [
	"ability_id",
	"unlocked",
	"rank",
	"experience",
	"available_charges",
	"next_charge_tick",
	"use_sequence",
]

class DecodeResult:
	extends RefCounted

	var code: Error = FAILED
	var prepared: Dictionary = {}
	var message: String = ""

	func is_success() -> bool:
		return code == OK

func decode(
	document: Dictionary,
	catalog: AbilityCatalog,
) -> DecodeResult:
	if catalog == null:
		return _failure(ERR_UNCONFIGURED, "catalogue absent")
	if not _has_exact_keys(document, ROOT_KEYS):
		return _failure(ERR_INVALID_DATA, "clés racine invalides")
	if typeof(document.get("format")) != TYPE_STRING:
		return _failure(ERR_INVALID_DATA, "format non textuel")
	if String(document.get("format")) != FORMAT:
		return _failure(ERR_FILE_UNRECOGNIZED, "format inconnu")
	var version_value := _read_int(document.get("version"), 1, VERSION)
	if version_value == null or int(version_value) != VERSION:
		return _failure(ERR_FILE_UNRECOGNIZED, "version inconnue")
	if typeof(document.get("characters")) != TYPE_ARRAY:
		return _failure(ERR_INVALID_DATA, "characters non tabulaire")

	var prepared: Dictionary = {}
	for raw_character: Variant in document.get("characters") as Array:
		if typeof(raw_character) != TYPE_DICTIONARY:
			return _failure(ERR_INVALID_DATA, "personnage non objet")
		var decoded := _decode_character(
			raw_character as Dictionary,
			catalog,
		)
		if decoded == null:
			return _failure(ERR_INVALID_DATA, "personnage invalide")
		var character_id: StringName = decoded["character_id"]
		if prepared.has(character_id):
			return _failure(ERR_ALREADY_EXISTS, "personnage dupliqué")
		prepared[character_id] = decoded

	var result := DecodeResult.new()
	result.code = OK
	result.prepared = prepared
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le format, la version et les clés exactes sont obligatoires.
- Les types sont vérifiés avant conversion.
- Chaque personnage est unique.
- `_decode_character()` valide chaque entrée contre le catalogue et les bornes de sa définition.
- `_read_int()` suit la règle des entiers JSON sûrs du chapitre 18.
- `DecodeResult` distingue un document vide valide d’un refus.

## 28. Section de sauvegarde

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/infrastructure/ability_save_section.gd`.**

```gdscript
class_name AbilitySaveSection
extends SaveSection

var _repository: AbilityRepository
var _catalog: AbilityCatalog
var _codec := AbilitySnapshotCodec.new()
var _prepared: Dictionary = {}
var _is_prepared := false

func section_id() -> StringName:
	return &"abilities"

func prepare_restore(payload: Dictionary) -> Error:
	_prepared.clear()
	_is_prepared = false
	if _repository == null or _catalog == null:
		return ERR_UNCONFIGURED
	var decoded := _codec.decode(payload, _catalog)
	if not decoded.is_success():
		return decoded.code
	_prepared = decoded.prepared.duplicate(true)
	_is_prepared = true
	return OK

func apply_prepared() -> Error:
	if not _is_prepared:
		return ERR_UNCONFIGURED
	var code := _repository.replace_all(_prepared.duplicate(true))
	if code != OK:
		return code
	_prepared.clear()
	_is_prepared = false
	return OK

func cancel_restore() -> void:
	_prepared.clear()
	_is_prepared = false
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La préparation ne touche pas au dépôt actif.
- Les données sont dupliquées avant stockage et application.
- La préparation n’est vidée qu’après succès.
- Le coordinateur peut annuler si une autre section échoue.
- Une définition absente rend la restauration invalide.

## 29. Présentation et scène pédagogique

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/presentation/ability_presentation_bridge.gd`.**

```gdscript
class_name AbilityPresentationBridge
extends Node

var _actor_registry: ActiveCharacterRegistry

func on_ability_resolved(result: AbilityResult) -> void:
	if result == null or result.validate() != OK:
		return
	if not result.is_success():
		return
	var actor := _actor_registry.find_active(result.user_character_id)
	if actor == null:
		return
	actor.request_animation(result.ability_id)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le pont reçoit seulement un résultat committé.
- Un personnage hors écran reste valide sans animation.
- L’identifiant sert de clé de présentation.
- Aucune ressource ou santé n’est modifiée ici.

La scène `ch19_abilities_demo.tscn` doit montrer :

1. une compétence verrouillée refusée ;
2. un coût insuffisant sans charge consommée ;
3. une cible hors portée refusée par le combat ;
4. une utilisation réussie consommant coût et charge ;
5. une recharge par ticks logiques ;
6. un rang modifiant coût, effet ou recharge ;
7. un effet optionnel produisant un résultat partiel ;
8. une sauvegarde restaurant progression et recharge.

## 30. Modes Solo et Studio

### 30.1 Mode Solo

- catalogue local de `.tres` ;
- dépôt en mémoire ;
- progression simple ;
- unité de travail locale ;
- diagnostics lisibles ;
- aucune classe chargée depuis les données.

### 30.2 Mode Studio

- catalogue versionné ;
- imports contrôlés ;
- tests de propriété sur coûts et recharges ;
- migrations explicites ;
- télémétrie des refus ;
- revue des effets requis et optionnels ;
- séparation entre équilibrage, domaine et présentation.

Le Mode Studio renforce les contrôles. Il n’ajoute ni Service Locator ni Autoload universel.

## 31. Budgets, sécurité et diagnostics

Bornes pédagogiques :

| Élément | Borne |
|---|---:|
| compétences par personnage | 256 |
| effets par compétence | 32 |
| coûts par compétence | 16 |
| cibles proposées | 128 |
| rang maximal | 100 |
| charges maximales | 99 |

Ces valeurs devront être mesurées au chapitre 27.

Une définition externe doit :

- être limitée avant parsing ;
- utiliser un schéma versionné ;
- référencer uniquement des types autorisés ;
- refuser chemins, scripts et méthodes dynamiques ;
- borner coûts, rangs, ticks, cibles et montants ;
- être validée avant le catalogue.

Journaliser :

- `use_id`, `ability_id`, utilisateur ;
- rang, charge et tick ;
- révisions ;
- coûts préparés ;
- effets préparés ou refusés ;
- code de commit.

Ne pas journaliser snapshots complets, nœuds, secrets ou texte génératif non filtré.

## 32. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 32.1 Écrire directement les dégâts

**Symptôme ou risque :** la compétence contourne cible, portée, défense, garde et commit.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
target.current_health -= ability.base_damage
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la définition devient une autorité qu’elle ne possède pas.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var candidate := combat_port.prepare_damage_effect(
	plan,
	damage_effect,
	target_id,
	world_revision,
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le combat prépare l’impact après ses propres validations.

### 32.2 Utiliser un `Timer` autoritaire

**Symptôme ou risque :** pause, `time_scale` ou déchargement de scène changent la recharge métier.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
cooldown_timer.start(3.0)
await cooldown_timer.timeout
ability_ready = true
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le temps moteur et un nœud deviennent l’autorité persistante.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
runtime.next_charge_tick = logical_tick + cooldown_ticks
runtime.refresh_charges(definition, rank, current_tick)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la recharge dépend de ticks logiques sauvegardables.

### 32.3 Consommer le coût avant les effets

**Symptôme ou risque :** une ressource est perdue alors qu’une cible ou un effet requis est refusé.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
focus -= cost
var effect_code := apply_effect()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la mutation active précède les validations restantes.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var reservation := resources.prepare_reservation(...)
var candidate := combat_port.prepare_damage_effect(...)
var code := unit_of_work.commit(reservation, [candidate], ...)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** coût et effet sont committés dans le même lot.

### 32.4 Stocker la recharge dans la `Resource`

**Symptôme ou risque :** tous les personnages partagent la même recharge.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
ability_definition.remaining_cooldown = 120
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une donnée de conception partagée devient état runtime.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
runtime_state.next_charge_tick = logical_tick + cooldown_ticks
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** chaque personnage possède son état détaché.

### 32.5 Charger une classe depuis les données

**Symptôme ou risque :** une définition externe choisit du code arbitraire.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var script := load(effect.script_path)
script.new().apply(target)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le contenu contrôle un chemin et une classe exécutée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if effect is DamageEffectDefinition:
	return combat_port.prepare_damage_effect(...)
if effect is ResourceEffectDefinition:
	return character_port.prepare_resource_effect(...)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le dispatch est fermé sur des types autorisés.

### 32.6 Confondre prévisualisation et validation

**Symptôme ou risque :** une cible affichée valide est acceptée après changement du monde.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if target_preview.valid:
	apply_ability_without_recheck()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la prévisualisation peut utiliser une ancienne position ou révision.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var command := build_command_from_preview(target_preview)
var result := ability_service.execute(command)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’autorité relit toutes les données au moment de l’exécution.

### 32.7 Persister le plan

**Symptôme ou risque :** le chargement rejoue des cibles et révisions obsolètes.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
payload["pending_plan"] = current_plan
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le plan est une décision transitoire liée à un instant.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
payload["rank"] = progression.rank
payload["available_charges"] = runtime.available_charges
payload["next_charge_tick"] = runtime.next_charge_tick
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** seules les données durables sont restaurées.

### 32.8 Utiliser le nom affiché comme identité

**Symptôme ou risque :** traduction ou renommage casse les sauvegardes.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
known_abilities["Boule de feu"] = 3
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le texte localisé n’est pas stable.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
known_abilities[&"ability.definition.ember_bolt"] = 3
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’identifiant métier reste indépendant de l’affichage.

### 32.9 Ignorer un effet requis

**Symptôme ou risque :** une utilisation réussit alors que son effet principal manque.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
for effect in effects:
	prepare_effect(effect)
return success_result()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** aucun retour ni caractère requis n’est vérifié.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var candidate := prepare_effect(effect)
if candidate == null and effect.required:
	return rejected_effect_result(effect.effect_id)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** un effet requis absent bloque le lot avant commit.

### 32.10 Retenter un résultat partiel

**Symptôme ou risque :** des effets déjà committés sont exécutés deux fois.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if result.status != AbilityResult.Status.RESOLVED:
	retry(command)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** `PARTIALLY_RESOLVED` est une utilisation consommée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if not result.is_success():
	rebuild_from_fresh_snapshot()
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** seuls les vrais refus déclenchent une nouvelle décision.

## 33. Tests à préparer

### 33.1 Tests unitaires

- identifiants ;
- coûts et rangs ;
- modes de cible ;
- ordre et types d’effets ;
- recharge et récupération de plusieurs charges ;
- progression ;
- résultat partiel ;
- candidats et copies détachées ;
- codec strict.

### 33.2 Tests d’intégration

- compétence vers combat ;
- coût préparé puis cible refusée ;
- commit atomique coût, effet et charge ;
- refus sur révision obsolète ;
- soin borné par `CharacterRules` ;
- action d’agent ;
- sauvegarde et restauration.

### 33.3 Simulations

- 1, 64 et 256 compétences ;
- 1, 8 et 32 effets ;
- 1, 16 et 128 cibles ;
- récupération hors écran ;
- plusieurs personnages partageant une définition ;
- progression jusqu’au rang maximal.

## 34. Réserves runtime

Cette revue statique ne prouve pas :

- le passage de tous les extraits dans le parseur Godot 4.7.1 ;
- le comportement de `duplicate(true)` avec toutes les sous-ressources ;
- l’atomicité réelle de l’unité de travail ;
- l’exécution des ports de combat et de personnage ;
- l’instanciation de la scène pédagogique ;
- la tenue des budgets ;
- l’exécution du codec et d’une migration future ;
- le replay entre plateformes ou versions ;
- la génération d’un PDF intermédiaire.

## 35. Sources techniques

- [Godot 4.7 — `Resource`](https://docs.godotengine.org/en/4.7/classes/class_resource.html)
- [Godot 4.7 — `RefCounted`](https://docs.godotengine.org/en/4.7/classes/class_refcounted.html)
- [Godot 4.7 — `Array`](https://docs.godotengine.org/en/4.7/classes/class_array.html)
- [Godot 4.7 — `Dictionary`](https://docs.godotengine.org/en/4.7/classes/class_dictionary.html)
- [Godot 4.7 — `StringName`](https://docs.godotengine.org/en/4.7/classes/class_stringname.html)
- [Godot 4.7 — `Variant`](https://docs.godotengine.org/en/4.7/classes/class_variant.html)
- [Godot 4.7 — `Vector3`](https://docs.godotengine.org/en/4.7/classes/class_vector3.html)
- [Godot 4.7 — signaux](https://docs.godotengine.org/en/4.7/getting_started/step_by_step/signals.html)
- [Godot 4.7 — `Timer`](https://docs.godotengine.org/en/4.7/classes/class_timer.html)
- [Chapitre 7 — Données avec Resources, JSON et configurations](CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md)
- [Chapitre 9 — Sauvegardes, chargements et compatibilité](CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md)
- [Chapitre 14 — Personnages](CHAPITRE-14-Personnages.md)
- [Chapitre 17 — Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md)
- [Chapitre 18 — Combat](CHAPITRE-18-Combat.md)

## 36. Synthèse opérationnelle pour Project Asteria

Le système de compétences et pouvoirs de `Project Asteria` retient les décisions suivantes :

1. `AbilityDefinition` est une donnée de conception partagée et immuable ;
2. progression et runtime sont séparés de la définition ;
3. rang, expérience, charges et ticks de recharge sont persistés ;
4. les coûts sont préparés par identifiants de ressources ;
5. les ciblages sont déclaratifs et bornés ;
6. la prévisualisation ne remplace jamais la validation ;
7. les effets sont composables, ordonnés, copiés et limités à des types autorisés ;
8. dégâts et états restent sous l’autorité du combat ;
9. santé et endurance restent sous les règles des personnages ;
10. coût, effets, charge et recharge sont committés par une unité de travail commune ;
11. un effet requis absent bloque le lot avant commit ;
12. un résultat partiel est une utilisation consommée ;
13. les recharges utilisent des ticks logiques ;
14. plans, réservations, candidats, cibles dérivées et VFX ne sont pas persistés ;
15. le chapitre 20 pourra accorder des compétences par objets sans déplacer leurs règles.
