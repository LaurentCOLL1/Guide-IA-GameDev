---
title: "Livre II — Chapitre 19 : Compétences et pouvoirs"
id: "DOC-L2-CH19"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 19
last-verified: "2026-07-20T15:27:31+02:00"
audit-status: "complete"
audit-date: "2026-07-20T15:27:31+02:00"
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

Le chapitre 18 a construit l’autorité du combat : une commande typée est validée, la cible, la portée et la ligne de vue sont contrôlées, les dégâts sont calculés, puis les candidats sont committés avant les événements.

Ce chapitre ajoute le système qui décrit **ce qu’un personnage sait faire**. Une compétence ou un pouvoir peut :

- posséder une définition de conception stable ;
- exiger un coût ;
- entrer en recharge ;
- imposer un mode de ciblage spécialisé ;
- produire plusieurs effets composables ;
- être débloqué et amélioré ;
- demander au combat d’appliquer un impact sans lui retirer son autorité ;
- être sauvegardé sans persister les caches, prévisualisations ou requêtes en attente.

À la fin du chapitre, le lecteur saura distinguer cinq responsabilités :

| Responsabilité | Autorité |
|---|---|
| définir une compétence | `AbilityDefinition` et ses effets de conception |
| savoir si un personnage la connaît | progression des compétences |
| réserver coût et recharge | service de compétences |
| valider cible, portée, défense et dégâts | système de combat |
| afficher animation, icône et VFX | présentation |

## 2. Prérequis

Le lecteur doit avoir parcouru :

- le chapitre 4 pour l’architecture feature-first ;
- le chapitre 5 pour les services injectés et le point de composition ;
- le chapitre 7 pour les `Resource`, catalogues et identifiants stables ;
- le chapitre 9 pour les sections de sauvegarde préparées avant application ;
- le chapitre 14 pour `CharacterId`, `CharacterRuntimeState` et `CharacterRules` ;
- le chapitre 17 pour les requêtes d’action des agents ;
- le chapitre 18 pour `CombatService`, les cibles, la portée, les dégâts, les états, les révisions et le commit.

## 3. Périmètre et frontières

Ce chapitre définit :

- les identifiants de compétences et de pouvoirs ;
- les définitions de conception ;
- les coûts et ressources de pouvoir ;
- les charges et temps de recharge ;
- les modes de ciblage déclaratifs ;
- les effets composables ;
- les commandes d’utilisation ;
- la validation d’apprentissage et d’utilisation ;
- la réservation atomique du coût et de la recharge ;
- l’adaptation vers le combat ;
- la progression par rang et expérience ;
- les événements, diagnostics, budgets et persistance.

Il ne définit pas :

- l’inventaire, l’équipement, les armes possédées ou les consommables du chapitre 20 ;
- les prix, achats et récompenses du chapitre 21 ;
- les règles écologiques du chapitre 22 ;
- les lois, factions et sanctions du chapitre 23 ;
- les quêtes et choix narratifs du chapitre 25 ;
- les arbres d’édition visuels et pipelines du chapitre 26 ;
- les campagnes de tests exécutés du chapitre 27 ;
- le multijoueur et l’autorité réseau du Livre IV.

> **Frontière essentielle :** une compétence décrit une intention et des effets demandés. Le combat conserve la décision finale sur cible, portée, ligne de vue, défense, dégâts, état de vie et commit.

<a id="ch19-authority-chain"></a>

## 4. Chaîne d’autorité

> **[LECTURE] Flux d’utilisation d’une compétence — Ne pas saisir.**

```text
joueur / agent / scénario
    ↓ AbilityUseCommand
AbilityService
    ├── vérifie apprentissage, rang et définition
    ├── vérifie coût, charges et recharge
    ├── prépare la réservation
    └── construit un AbilityExecutionPlan
            ↓ demandes d’effets typées
CombatAbilityPort / CharacterEffectPort
    ├── relisent le monde autoritaire
    ├── valident cible, portée et règles propriétaires
    └── préparent puis commit les mutations
            ↓ résultat
AbilityService
    ├── confirme coût et recharge
    └── publie événements de compétence
            ↓
présentation, journal, agents, narration
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Entrée :** une commande indique l’utilisateur, la compétence, les cibles demandées et les révisions attendues.
- **Sortie :** le service renvoie un résultat métier stable ; les ports propriétaires renvoient leurs propres résultats.
- **Invariant :** aucun effet n’est considéré comme appliqué tant que l’autorité concernée n’a pas committé ses candidats.
- **Frontière :** la compétence orchestre ; elle ne recalcule ni armure, ni résistance, ni mort.

## 5. Architecture retenue

> **[LECTURE] Arborescence cible — Ne pas créer depuis un terminal.**

```text
res://src/features/abilities/
├── domain/
│   ├── ability_id.gd
│   ├── ability_definition.gd
│   ├── ability_cost_definition.gd
│   ├── ability_target_definition.gd
│   ├── ability_effect_definition.gd
│   ├── damage_effect_definition.gd
│   ├── status_effect_definition.gd
│   ├── resource_effect_definition.gd
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

- `domain` contient les règles et données sans dépendance à une scène.
- `application` orchestre catalogues, progression, ressources et ports propriétaires.
- `infrastructure` encode la sauvegarde stricte.
- `presentation` traduit des événements committés en interface et animation.
- Le chapitre 20 pourra fournir des objets qui accordent une compétence sans déplacer la compétence dans l’inventaire.

## 6. Vocabulaire

Une **compétence** est une capacité apprise ou entraînée. Un **pouvoir** est une capacité dont la source peut être magique, biologique, technologique ou narrative. Le système utilise le terme générique `ability` pour traiter les deux avec les mêmes contrats.

Une **définition** est une `Resource` de conception partagée et immuable pendant le gameplay.

Un **état runtime** contient les charges et la prochaine disponibilité d’une compétence pour un personnage.

Une **progression** contient le rang, l’expérience et l’état de déblocage.

Un **effet** est une demande structurée : dégâts, état de combat, soin ou variation d’une ressource. Il n’est pas encore une mutation.

Un **plan d’exécution** est une copie détachée des demandes d’effets calculées pour une utilisation précise.

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
		if not (
			character >= "a" and character <= "z"
			or character >= "0" and character <= "9"
			or character == "_"
		):
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

- `definition()` transforme un slug limité en identifiant de contenu stable.
- `strip_edges()` retire les espaces de début et de fin ; `to_lower()` normalise la casse.
- La boucle refuse tout caractère hors lettres ASCII minuscules, chiffres et `_`.
- `use()` combine définition, personnage et séquence ; les mêmes arguments produisent le même résultat.
- Une entrée invalide renvoie la sentinelle `&""`, jamais un identifiant partiel.

## 8. Types de ressources consommables

Le système ne duplique pas la santé ou l’endurance. Il passe par un port qui connaît l’autorité réelle de chaque ressource.

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/domain/ability_cost_definition.gd`.**

```gdscript
class_name AbilityCostDefinition
extends Resource

enum Timing {
	ON_COMMIT,
	PER_TICK,
}

@export var resource_id: StringName
@export_range(0, 1000000, 1) var base_amount: int = 0
@export_range(0, 1000000, 1) var amount_per_rank: int = 0
@export var timing: Timing = Timing.ON_COMMIT
@export var allow_zero := false

func amount_for_rank(rank: int) -> int:
	if rank < 1:
		return -1
	var extra := amount_per_rank * (rank - 1)
	return base_amount + extra

func validate() -> Error:
	if not StableId.is_valid(resource_id):
		return ERR_INVALID_DATA
	if base_amount < 0 or amount_per_rank < 0:
		return ERR_INVALID_DATA
	if not allow_zero and base_amount == 0:
		return ERR_INVALID_DATA
	if timing < Timing.ON_COMMIT or timing > Timing.PER_TICK:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `resource_id` peut désigner `character.resource.stamina`, `ability.resource.focus` ou une autre ressource enregistrée.
- `amount_for_rank()` renvoie `-1` pour un rang invalide ; le service transforme cette sentinelle en refus contrôlé.
- `amount_per_rank * (rank - 1)` ajoute le supplément seulement après le premier rang.
- `PER_TICK` prépare les canalisations futures, mais une utilisation instantanée n’en dépend pas.
- La définition ne retire aucune ressource : elle décrit seulement un coût.

## 9. Modes de ciblage

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

- `mode` décrit la forme de la demande, pas la validation finale du monde.
- `allegiance` exprime l’intention de conception ; le combat relit les côtés réels.
- `range_m` et `radius_m` utilisent les mètres Godot et doivent être finis.
- `maximum_targets` borne une sélection de zone avant toute allocation importante.
- Une compétence `SELF` impose une cohérence stricte afin d’éviter une cible externe cachée dans une définition prétendument personnelle.

## 10. Effets composables

La classe de base fournit une identité et un ordre. Chaque sous-type transporte uniquement les données nécessaires à son autorité propriétaire.

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

- `effect_id` identifie l’effet dans les diagnostics et la sauvegarde de contenu, pas une classe à charger dynamiquement.
- `order` produit un ordre explicite entre effets.
- `required` indique si l’échec de l’effet doit faire échouer l’ensemble de l’utilisation.
- `duplicate(true)` demande une duplication profonde des sous-ressources ; le plan n’expose pas la définition partagée à une mutation runtime.

### 10.1 Effet de dégâts

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/domain/damage_effect_definition.gd`.**

```gdscript
class_name DamageEffectDefinition
extends AbilityEffectDefinition

@export var damage_type: DamagePacket.DamageType
@export_range(0, 100000000, 1) var base_amount: int = 0
@export_range(0, 100000000, 1) var amount_per_rank: int = 0
@export_range(0, 1000, 1) var armor_penetration_permille: int = 0
@export var tags: Array[StringName] = []

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
	var seen: Dictionary[StringName, bool] = {}
	for tag: StringName in tags:
		if not StableId.is_valid(tag) or seen.has(tag):
			return ERR_INVALID_DATA
		seen[tag] = true
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’effet calcule une quantité brute par rang.
- Le type, la pénétration et les tags correspondent aux données attendues par le combat.
- Il ne lit ni défense ni garde et ne produit pas la santé finale.
- Les tags sont validés et uniques ; ils ne deviennent jamais des noms de méthodes.

### 10.2 Effet d’état

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

- La compétence désigne une définition d’état autorisée.
- Le combat choisit la règle d’empilement et valide la capacité de la cible.
- `duration_ticks` utilise la chronologie logique, jamais l’heure système.
- `stacks` est une demande bornée qui peut encore être réduite ou refusée par la politique propriétaire.

### 10.3 Effet de ressource

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

- Un delta positif restaure une ressource ; un delta négatif la consomme.
- `Variant` permet de distinguer la valeur entière `0` d’un rang invalide représenté par `null`.
- Le port propriétaire borne la valeur selon la ressource réelle.
- Un soin de santé passe par `CharacterRules`; il n’écrit pas directement dans `CharacterRuntimeState`.

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
@export var tags: Array[StringName] = []

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
	if effects.is_empty():
		return ERR_INVALID_DATA

	var seen_costs: Dictionary[StringName, bool] = {}
	for cost: AbilityCostDefinition in costs:
		if cost == null or cost.validate() != OK:
			return ERR_INVALID_DATA
		if seen_costs.has(cost.resource_id):
			return ERR_ALREADY_EXISTS
		seen_costs[cost.resource_id] = true

	var seen_effects: Dictionary[StringName, bool] = {}
	var previous_order := -1
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

- Les clés d’affichage sont distinctes des identifiants métier.
- `cooldown_for_rank()` réduit la recharge sans produire une valeur négative.
- Chaque ressource ne peut apparaître qu’une fois dans `costs`, ce qui évite deux réservations ambiguës.
- Les effets sont déjà triés par `order`; le validateur refuse une définition non canonique au lieu de la réordonner silencieusement.
- La `Resource` reste immuable pendant le gameplay.

## 12. Créer une définition dans Godot

> **[APP] Godot — Créer `res://data/abilities/ember_bolt.tres` depuis `AbilityDefinition`.**

Renseigner :

- `ability_id` : `ability.definition.ember_bolt` ;
- `maximum_rank` : `5` ;
- `base_cooldown_ticks` : `180` ;
- `cooldown_reduction_per_rank` : `12` ;
- une charge ;
- un coût `ability.resource.focus` ;
- une cible `SINGLE_CHARACTER`, `ENEMY`, portée `18.0` m, ligne de vue requise ;
- un `DamageEffectDefinition` de type `FIRE`.

> **[LECTURE] Résultat attendu — Ne pas saisir.**

```text
La ressource est acceptée seulement si :
- tous les identifiants sont stables ;
- les coûts sont uniques ;
- la cible est cohérente ;
- les effets sont valides et ordonnés ;
- le rang et la recharge restent dans leurs bornes.
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Cette sortie décrit les invariants observables après `validate()`.
- Aucun état de personnage, charge courante ou tick de recharge n’est enregistré dans le `.tres`.
- Le fichier peut être partagé par tous les personnages sans mutation runtime.

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
	var result: Array[StringName] = []
	result.assign(_definitions.keys())
	result.sort()
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `register()` refuse une définition invalide ou dupliquée.
- Le catalogue conserve une copie profonde pour ne pas dépendre d’une ressource que l’appelant modifierait ensuite.
- `get_definition()` renvoie également une copie.
- `all_ids_sorted()` donne un ordre stable pour validation, affichage et sauvegarde.

## 14. Progression d’une compétence

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

- Une compétence verrouillée possède toujours un rang `0`.
- Une compétence débloquée commence au rang `1`.
- L’expérience reste un entier JSON sûr de 53 bits.
- La définition fournit la borne supérieure du rang.
- La copie détachée évite qu’une requête d’interface modifie l’état du dépôt.

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

- La formule `100 * rank * rank` est un exemple pédagogique, pas une valeur d’équilibrage universelle.
- Le rang augmente tant que l’expérience cumulée atteint le seuil suivant.
- L’expérience n’est pas consommée ; elle représente un total.
- La politique refuse l’expérience sur une compétence verrouillée.
- Un changement de formule devra être versionné si la progression sauvegardée en dépend.

## 16. État runtime : charges et recharge

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

- Les charges représentent le nombre d’utilisations immédiatement disponibles.
- `next_charge_tick` désigne la prochaine récupération ; zéro signifie qu’aucune recharge n’est en cours.
- La boucle restaure plusieurs charges lorsque beaucoup de ticks se sont écoulés hors écran.
- Le calcul utilise le tick logique et reste sauvegardable.
- L’état ne contient ni `Timer`, ni animation, ni référence de nœud.

## 17. Commande d’utilisation

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
		if not CharacterId.is_valid(target_id) or seen.has(target_id):
			return ERR_INVALID_DATA
		seen[target_id] = true
	return OK

func duplicate_detached() -> AbilityUseCommand:
	var copy := AbilityUseCommand.new()
	copy.use_id = use_id
	copy.user_character_id = user_character_id
	copy.ability_id = ability_id
	copy.target_character_ids.assign(target_character_ids)
	copy.target_point = target_point
	copy.has_target_point = has_target_point
	copy.requested_tick = requested_tick
	copy.expected_world_revision = expected_world_revision
	copy.expected_ability_revision = expected_ability_revision
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La commande transporte une sélection demandée, jamais une liste de cibles déjà autorisées.
- Les révisions rendent les décisions obsolètes détectables.
- Les cibles sont uniques et typées par `CharacterId`.
- `has_target_point` distingue le point `(0, 0, 0)` valide de l’absence de point.
- La copie détachée protège la file et le service contre une modification ultérieure de l’appelant.

## 18. Résultat métier

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
	REJECTED_RANK,
	REJECTED_NO_CHARGE,
	REJECTED_COOLDOWN,
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
var applied_effect_ids: Array[StringName] = []
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

- `PARTIALLY_RESOLVED` n’est permis que lorsque des effets non requis échouent.
- Un refus de coût ou de cible ne consomme aucune charge.
- Les identifiants d’effets appliqués et refusés permettent un diagnostic sans sérialiser les objets complets.
- `is_success()` évite de retenter une utilisation partiellement committée comme si rien ne s’était passé.

## 19. Plan d’exécution détaché

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
	if use_id.is_empty() or not StableId.is_valid(use_id):
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
		var effect := effects[index]
		if effect == null or effect.validate() != OK:
			return ERR_INVALID_DATA
		if effect.effect_id != definition.effects[index].effect_id:
			return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le plan fige le rang, les cibles et les effets pour une utilisation précise.
- L’ordre et les identifiants doivent correspondre à la définition validée.
- Le plan ne contient aucun résultat de dégâts, aucune défense et aucune référence de scène.
- Les effets sont des copies profondes ; modifier le catalogue après préparation ne change pas une utilisation déjà planifiée.

## 20. Port de ressources

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

func commit_reservation(
	reservation: Reservation,
	expected_world_revision: int,
) -> Error:
	return ERR_UNAVAILABLE

func cancel_reservation(_reservation: Reservation) -> void:
	pass
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `prepare_reservation()` vérifie la disponibilité et renvoie un candidat sans retirer de ressource active.
- `commit_reservation()` applique les coûts seulement avec la révision attendue.
- `cancel_reservation()` libère le candidat lorsque la cible ou un effet requis échoue.
- Le port peut coordonner endurance, santé et ressources propres aux pouvoirs sans les fusionner dans un même état.

## 21. Ports propriétaires des effets

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/application/combat_ability_port.gd`.**

```gdscript
class_name CombatAbilityPort
extends RefCounted

class EffectResult:
	extends RefCounted

	var code: Error = FAILED
	var applied := false
	var detail_id: StringName = &""

	func is_success() -> bool:
		return code == OK and applied

func apply_damage_effect(
	plan: AbilityExecutionPlan,
	effect: DamageEffectDefinition,
	target_id: StringName,
	expected_world_revision: int,
) -> EffectResult:
	return null

func apply_status_effect(
	plan: AbilityExecutionPlan,
	effect: StatusEffectDefinition,
	target_id: StringName,
	expected_world_revision: int,
) -> EffectResult:
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le port reçoit une demande structurée et délègue au système de combat.
- Le combat reconstruit `DamagePacket`, valide cible, portée et ligne de vue, puis commit.
- `EffectResult` distingue le code technique de l’effet réellement appliqué.
- La classe de base ne réussit jamais silencieusement.

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/application/character_effect_port.gd`.**

```gdscript
class_name CharacterEffectPort
extends RefCounted

func apply_resource_effect(
	plan: AbilityExecutionPlan,
	effect: ResourceEffectDefinition,
	target_id: StringName,
	expected_world_revision: int,
) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Ce port traite les ressources dont le propriétaire est le système de personnages ou un registre dédié.
- Un soin de santé utilise les règles du chapitre 14.
- Une restauration d’endurance ne contourne pas les bornes du personnage.
- Le service de compétences ne connaît pas la disposition interne de ces états.

## 22. Dépôt de progression et d’état runtime

> **[LECTURE] Contrat de dépôt — Structure de référence.**

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

func replace_pair(
	character_id: StringName,
	expected_revision: int,
	progression: AbilityProgressionState,
	runtime: AbilityRuntimeState,
) -> Error:
	return ERR_UNAVAILABLE

func revision_for(character_id: StringName) -> int:
	return -1

func replace_all(prepared: Dictionary) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les lectures renvoient des copies détachées.
- `replace_pair()` remplace progression et runtime dans une même opération validée.
- La révision est portée par personnage afin qu’une utilisation ne remplace pas une évolution concurrente.
- `replace_all()` sert uniquement à une restauration préparée et complète.

## 23. Construire les coûts calculés

> **[LECTURE] Fonction interne de `AbilityService` — Suite du même fichier.**

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
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La fonction transforme les définitions en montants concrets pour le rang courant.
- Les clés sont uniques grâce à `AbilityDefinition.validate()`.
- Un dictionnaire vide peut représenter une compétence gratuite ; l’appelant connaît le nombre de coûts attendus et vérifie cette ambiguïté.
- Aucun retrait n’a encore lieu.

## 24. Préparer une utilisation

> **[VSC] Visual Studio Code — Créer : `res://src/features/abilities/application/ability_service.gd`.**

```gdscript
class_name AbilityService
extends RefCounted

signal ability_resolved(result: AbilityResult)

var _catalog: AbilityCatalog
var _repository: AbilityRepository
var _resources: AbilityResourcePort
var _combat_port: CombatAbilityPort
var _character_port: CharacterEffectPort

func execute(command: AbilityUseCommand) -> AbilityResult:
	if command == null or command.validate() != OK:
		return _result(
			AbilityResult.Status.REJECTED_INVALID_COMMAND,
			command,
			"commande invalide",
		)
	if _catalog == null or _repository == null or _resources == null:
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

	var target_code := _validate_target_shape(command, definition.target)
	if target_code != OK:
		return _result(
			AbilityResult.Status.REJECTED_TARGET,
			command,
			"forme de cible invalide",
		)

	return _execute_prepared(
		command,
		definition,
		progression,
		runtime,
	)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `execute()` effectue les validations communes avant toute réservation.
- La recharge est recalculée sur une copie runtime, pas sur l’état actif.
- La forme de cible est vérifiée ici ; la validité réelle de chaque cible appartient ensuite au port propriétaire.
- Une révision obsolète produit un refus normal, pas une corruption.
- Aucune charge ni ressource n’est consommée dans cette première phase.

## 25. Valider la forme de la cible

> **[LECTURE] Validation déclarative — Suite de `ability_service.gd`.**

```gdscript
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

- La méthode vérifie seulement la cohérence du payload avec le mode déclaré.
- Une cible unique n’accepte ni zéro ni plusieurs identifiants.
- Un point exige `has_target_point = true`, même si ses coordonnées valent zéro.
- Une zone borne la liste proposée, mais le combat peut encore filtrer les cibles hors portée ou non autorisées.

## 26. Réserver, exécuter et confirmer

> **[LECTURE] Cœur de l’exécution — Suite de `ability_service.gd`.**

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

	var plan := _build_plan(
		command,
		definition,
		progression.rank,
	)
	if plan == null or plan.validate(definition) != OK:
		_resources.cancel_reservation(reservation)
		return _result(
			AbilityResult.Status.REJECTED_RESOURCE,
			command,
			"plan invalide",
		)

	var effect_result := _apply_effects(
		plan,
		definition,
		command.expected_world_revision,
	)
	if not effect_result.is_success():
		_resources.cancel_reservation(reservation)
		return effect_result

	var resource_code := _resources.commit_reservation(
		reservation,
		command.expected_world_revision,
	)
	if resource_code != OK:
		return _result(
			AbilityResult.Status.REJECTED_STALE_REVISION,
			command,
			"réservation devenue obsolète",
		)

	var runtime_candidate := runtime.duplicate_detached()
	runtime_candidate.available_charges -= 1
	runtime_candidate.use_sequence += 1
	if runtime_candidate.available_charges < definition.maximum_charges:
		if runtime_candidate.next_charge_tick == 0:
			var cooldown := definition.cooldown_for_rank(progression.rank)
			runtime_candidate.next_charge_tick = (
				command.requested_tick + cooldown
			)

	var replace_code := _repository.replace_pair(
		command.user_character_id,
		command.expected_ability_revision,
		progression.duplicate_detached(),
		runtime_candidate,
	)
	if replace_code != OK:
		return _result(
			AbilityResult.Status.REJECTED_STALE_REVISION,
			command,
			"état de compétence devenu obsolète",
		)

	ability_resolved.emit(effect_result)
	return effect_result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les coûts sont préparés avant les effets.
- Un plan invalide annule la réservation sans mutation.
- Les effets requis sont appliqués avant la consommation définitive du coût.
- La charge et la recharge sont modifiées sur un candidat.
- **Limite statique importante :** pour une atomicité parfaite entre effets, coût et état de compétence, l’implémentation runtime doit fournir une unité de travail commune. Ce contrat est explicitement réservé aux tests du chapitre 27.
- Aucun succès runtime n’est revendiqué ici.

## 27. Construire le plan

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
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les cibles sont triées pour produire le même ordre avec les mêmes données.
- Les effets conservent l’ordre canonique de la définition.
- Le plan ne lit aucun dépôt supplémentaire.
- Les copies profondes isolent l’utilisation des modifications d’éditeur ou de catalogue.

## 28. Appliquer les effets par type autorisé

> **[LECTURE] Dispatch fermé — Suite de `ability_service.gd`.**

```gdscript
func _apply_effects(
	plan: AbilityExecutionPlan,
	definition: AbilityDefinition,
	expected_world_revision: int,
) -> AbilityResult:
	var result := _result(
		AbilityResult.Status.RESOLVED,
		null,
		"compétence résolue",
	)
	result.use_id = plan.use_id
	result.ability_id = plan.ability_id
	result.user_character_id = plan.user_character_id

	var targets := _effective_targets(plan, definition.target)
	for effect: AbilityEffectDefinition in plan.effects:
		var effect_applied := false
		for target_id: StringName in targets:
			var code := _apply_one_effect(
				plan,
				effect,
				target_id,
				expected_world_revision,
			)
			if code == OK:
				effect_applied = true
			elif effect.required:
				result.status = AbilityResult.Status.REJECTED_EFFECT
				result.message = "effet requis refusé"
				result.rejected_effect_ids.append(effect.effect_id)
				return result
		if effect_applied:
			result.applied_effect_ids.append(effect.effect_id)
		else:
			result.rejected_effect_ids.append(effect.effect_id)

	if not result.rejected_effect_ids.is_empty():
		result.status = AbilityResult.Status.PARTIALLY_RESOLVED
	return result

func _apply_one_effect(
	plan: AbilityExecutionPlan,
	effect: AbilityEffectDefinition,
	target_id: StringName,
	expected_world_revision: int,
) -> Error:
	if effect is DamageEffectDefinition:
		if _combat_port == null:
			return ERR_UNCONFIGURED
		var damage_result := _combat_port.apply_damage_effect(
			plan,
			effect as DamageEffectDefinition,
			target_id,
			expected_world_revision,
		)
		return OK if damage_result != null and damage_result.is_success() else FAILED
	if effect is StatusEffectDefinition:
		if _combat_port == null:
			return ERR_UNCONFIGURED
		var status_result := _combat_port.apply_status_effect(
			plan,
			effect as StatusEffectDefinition,
			target_id,
			expected_world_revision,
		)
		return OK if status_result != null and status_result.is_success() else FAILED
	if effect is ResourceEffectDefinition:
		if _character_port == null:
			return ERR_UNCONFIGURED
		return _character_port.apply_resource_effect(
			plan,
			effect as ResourceEffectDefinition,
			target_id,
			expected_world_revision,
		)
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le dispatch utilise une liste fermée de types connus, jamais un nom de classe fourni par des données externes.
- Un effet requis arrête l’utilisation dès son refus.
- Un effet optionnel peut produire `PARTIALLY_RESOLVED`.
- Chaque port reste propriétaire de sa validation et de son commit.
- La version pédagogique applique les effets séquentiellement ; une unité de travail globale est nécessaire pour garantir un tout-ou-rien entre plusieurs autorités.

## 29. Déterminer les cibles effectives

> **[LECTURE] Cibles initiales — Suite de `ability_service.gd`.**

```gdscript
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

- `SELF` produit explicitement l’utilisateur comme cible.
- Les autres modes utilisent les identifiants proposés et triés.
- Une zone autour d’un point peut recevoir une liste candidate issue d’un port spatial ; le combat la revalide.
- La fonction ne déduit jamais une cible depuis une proximité implicite.

## 30. Adapter une action d’agent

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
	var context := _ability_context.snapshot_for(request.owner_character_id)
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

- L’agent choisit une compétence et une cible ; il ne fournit ni coût final, ni recharge, ni dégâts.
- La révision des compétences est relue au démarrage.
- `action_id` doit correspondre à une définition du catalogue ; il ne devient pas une méthode.
- Un résultat partiel est consommé comme une exécution valable.
- Les champs de point ou de zone nécessitent un adaptateur spécialisé plutôt qu’une convention cachée.

## 31. Entrée du joueur et prévisualisation

L’interface peut afficher :

- coût estimé ;
- nombre de charges ;
- temps logique restant ;
- portée et zone ;
- cibles survolées ;
- effets décrits par les clés de localisation.

La prévisualisation n’est pas autoritaire. Entre l’affichage et le clic, une cible peut se déplacer, mourir, changer de côté ou rendre la révision obsolète.

> **[LECTURE] Séparation interface / autorité — Ne pas saisir.**

```text
interface :
- propose une cible ;
- affiche une estimation ;
- construit AbilityUseCommand.

AbilityService et ports propriétaires :
- relisent les révisions ;
- valident les ressources ;
- valident les cibles ;
- commit les effets.
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’interface améliore l’expérience sans pouvoir garantir le résultat.
- La même commande peut provenir du joueur, d’un agent ou d’un scénario.
- Les règles métier ne sont pas dupliquées dans les boutons ou widgets.

## 32. Événements de compétences

Les événements minimums sont :

- compétence débloquée ;
- rang augmenté ;
- utilisation acceptée ;
- effet appliqué ;
- effet optionnel refusé ;
- charge consommée ;
- charge récupérée ;
- utilisation refusée.

Ils transportent des identifiants, ticks, rangs et statuts. Ils ne transportent ni `Resource` mutable, ni nœud, ni texte localisé comme autorité.

## 33. Sauvegarde : données persistées

Sont persistés, par `CharacterId` :

- révision de compétence ;
- compétences débloquées ;
- rang et expérience ;
- charges disponibles ;
- prochain tick de récupération ;
- séquence d’utilisation.

Ne sont pas persistés :

- définitions `.tres` ;
- icônes, animations et VFX ;
- plans d’exécution ;
- réservations en attente ;
- prévisualisations de cible ;
- listes de cibles dérivées ;
- résultats de portée ou ligne de vue ;
- caches de catalogue.

## 34. Codec strict

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
	if String(document.get("format")) != FORMAT:
		return _failure(ERR_FILE_UNRECOGNIZED, "format inconnu")
	if _read_int(document.get("version"), 1, VERSION) != VERSION:
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

- Le format et la version sont obligatoires.
- Les clés exactes refusent silencieusement aucune extension inconnue.
- Chaque personnage et compétence est validé contre le catalogue.
- Un résultat structuré distingue un document vide valide d’un échec.
- L’extrait montre l’entrée du codec ; les fonctions `_decode_character`, `_read_int`, `_has_exact_keys` et `_failure` suivent les mêmes règles strictes du chapitre 18.

## 35. Section de sauvegarde

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

- `prepare_restore()` ne modifie pas le dépôt actif.
- La préparation est dupliquée avant stockage et avant application.
- `apply_prepared()` ne vide le candidat qu’après remplacement réussi.
- Le coordinateur du chapitre 9 peut annuler l’ensemble si une autre section échoue.
- Les définitions absentes ou incompatibles rendent la restauration non valide au lieu d’être ignorées silencieusement.

## 36. Présentation

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

- Le pont reçoit seulement un résultat déjà committé.
- Un personnage hors écran ne provoque pas d’échec métier.
- L’identifiant de compétence sert de clé de présentation, pas de nom de méthode dynamique.
- L’animation ne retire aucune ressource et n’applique aucun effet.

## 37. Scène pédagogique

La scène `ch19_abilities_demo.tscn` contient :

- deux personnages du chapitre 14 ;
- un affrontement du chapitre 18 ;
- trois compétences : projectile, posture et soin ;
- une barre de ressources ;
- des boutons d’utilisation ;
- un affichage des charges, recharges et résultats ;
- un panneau de progression ;
- aucun service IA obligatoire.

Elle doit permettre de constater :

1. qu’une compétence verrouillée est refusée ;
2. qu’un coût insuffisant ne consomme aucune charge ;
3. qu’une cible hors portée est refusée par le combat ;
4. qu’une utilisation réussie consomme coût et charge ;
5. que la recharge dépend des ticks logiques ;
6. qu’un rang supérieur modifie coût, effet ou recharge selon la définition ;
7. qu’un effet optionnel peut produire un résultat partiel ;
8. qu’une sauvegarde restaure progression, charges et ticks.

## 38. Modes Solo et Studio

### 38.1 Mode Solo

- catalogue local de `.tres` ;
- dépôt en mémoire ;
- quelques ressources stables ;
- progression simple ;
- unité de travail locale ;
- diagnostics lisibles ;
- aucune génération dynamique de classe.

### 38.2 Mode Studio

- catalogue versionné et validé en CI ;
- identifiants réservés par domaine ;
- feuilles d’équilibrage importées de manière contrôlée ;
- tests de propriété sur coûts, recharges et progression ;
- migrations explicites ;
- télémétrie des refus et usages ;
- revue séparée des effets requis et optionnels.

Le Mode Studio ajoute des contrôles. Il ne transforme pas le catalogue en Service Locator et ne place pas les compétences dans un Autoload universel.

## 39. Budgets

Bornes pédagogiques :

| Élément | Borne |
|---|---:|
| compétences par personnage | 256 |
| effets par compétence | 32 |
| coûts par compétence | 16 |
| cibles proposées | 128 |
| rang maximal | 100 |
| charges maximales | 99 |
| événements récents | 512 |

Ces valeurs ne sont pas des performances garanties. Le chapitre 27 devra mesurer les scènes et simulations sur la configuration AMD de référence.

## 40. Sécurité des données externes

Une définition importée doit :

- être limitée en taille avant parsing ;
- utiliser un schéma versionné ;
- référencer uniquement des types d’effets autorisés ;
- employer des identifiants stables ;
- refuser classes, scripts, chemins et méthodes fournis par les données ;
- borner coûts, rangs, ticks, cibles et montants ;
- être validée avant enregistrement dans le catalogue.

Une sortie d’IA peut suggérer une compétence connue. Elle ne crée pas une nouvelle classe, ne choisit pas un exécuteur arbitraire et ne fixe pas les dégâts finaux.

## 41. Diagnostics

Journaliser au minimum :

- `use_id`, `ability_id`, utilisateur ;
- rang, charge et tick ;
- révisions attendues et observées ;
- coûts préparés et code de réservation ;
- identifiants d’effets appliqués ou refusés ;
- statut final ;
- durée de traitement comme télémétrie non autoritaire.

Ne pas journaliser :

- snapshots complets ;
- ressources partagées ;
- secrets ;
- texte génératif non filtré ;
- références de nœuds ;
- historique illimité.

## 42. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 42.1 Écrire les dégâts dans la définition

**Symptôme ou risque :** le fichier de compétence devient une mutation et contourne le combat.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
target.current_health -= ability.base_damage
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la définition ne valide ni portée, ni défense, ni garde, ni révision.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var effect_result := combat_port.apply_damage_effect(
	plan,
	damage_effect,
	target_id,
	world_revision,
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la compétence transmet une demande typée au système propriétaire.

### 42.2 Utiliser un `Timer` pour la recharge autoritaire

**Symptôme ou risque :** pause, `time_scale` et déchargement de scène changent la disponibilité métier.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
cooldown_timer.start(3.0)
await cooldown_timer.timeout
ability_ready = true
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la recharge dépend d’un nœud et de secondes non persistées.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
runtime.next_charge_tick = logical_tick + cooldown_ticks
runtime.refresh_charges(definition, rank, current_tick)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la disponibilité utilise des ticks logiques sauvegardables.

### 42.3 Consommer le coût avant la validation de cible

**Symptôme ou risque :** le joueur perd une ressource alors que la cible est refusée.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
focus -= cost
if not target_is_valid:
	return ERR_INVALID_DATA
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une mutation active précède une validation susceptible d’échouer.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var reservation := resources.prepare_reservation(...)
var effect_result := apply_effects(...)
if effect_result.is_success():
	resources.commit_reservation(reservation, world_revision)
else:
	resources.cancel_reservation(reservation)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le coût reste candidat tant que l’utilisation n’est pas acceptée.

### 42.4 Stocker la recharge dans la `Resource`

**Symptôme ou risque :** tous les personnages partageant la définition partagent aussi la même recharge.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
ability_definition.remaining_cooldown = 120
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une `Resource` de conception partagée devient état runtime mutable.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
runtime_state.next_charge_tick = logical_tick + cooldown_ticks
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** chaque personnage possède son propre état détaché.

### 42.5 Charger une classe depuis un nom d’effet

**Symptôme ou risque :** une donnée externe choisit du code à exécuter.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var script := load(effect.script_path)
script.new().apply(target)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le contenu peut charger un chemin ou une classe non autorisée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if effect is DamageEffectDefinition:
	return combat_port.apply_damage_effect(...)
if effect is ResourceEffectDefinition:
	return character_port.apply_resource_effect(...)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le dispatch est fermé sur des types explicitement autorisés.

### 42.6 Confondre prévisualisation et validation

**Symptôme ou risque :** une cible affichée en vert est acceptée malgré un monde devenu obsolète.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if target_preview.valid:
	apply_ability_without_recheck()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la prévisualisation peut dater d’une ancienne position ou révision.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var command := build_command_from_preview(target_preview)
var result := ability_service.execute(command)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’autorité relit les données au moment de l’exécution.

### 42.7 Persister un plan d’exécution

**Symptôme ou risque :** une sauvegarde rejoue des cibles et révisions obsolètes.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
payload["pending_plan"] = current_plan
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le plan dépend d’un instant du monde et contient des demandes transitoires.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
payload["rank"] = progression.rank
payload["available_charges"] = runtime.available_charges
payload["next_charge_tick"] = runtime.next_charge_tick
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** seules les données durables sont restaurées ; une nouvelle commande sera reconstruite.

### 42.8 Utiliser le nom affiché comme identité

**Symptôme ou risque :** une traduction ou un renommage casse les sauvegardes.

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

### 42.9 Ignorer un effet requis

**Symptôme ou risque :** une compétence est annoncée comme réussie alors que son effet principal a échoué.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
for effect in effects:
	apply_effect(effect)
return success_result()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le code ne lit ni le retour ni le caractère requis de l’effet.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var code := apply_effect(effect)
if code != OK and effect.required:
	return rejected_effect_result(effect.effect_id)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** un effet principal refusé empêche une réussite mensongère.

### 42.10 Accorder un rang hors définition

**Symptôme ou risque :** une sauvegarde ou un outil crée un rang supérieur au maximum.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
progression.rank += 1
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** aucune borne ni validation de la définition n’est consultée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if progression.rank < definition.maximum_rank:
	progression.rank += 1
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la progression respecte la borne de conception et sera revalidée avant commit.

### 42.11 Sauvegarder les définitions `.tres` dans le snapshot

**Symptôme ou risque :** la sauvegarde du joueur devient dépendante de références de ressources et de chemins.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
payload["ability_resource"] = definition
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une `Resource` n’est pas une valeur JSON stable et duplique les données de conception.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
payload["ability_id"] = String(definition.ability_id)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la sauvegarde conserve l’identité et le catalogue fournit la définition courante compatible.

### 42.12 Retenter un résultat partiel

**Symptôme ou risque :** un effet déjà appliqué est exécuté une seconde fois.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if result.status != AbilityResult.Status.RESOLVED:
	retry(command)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** `PARTIALLY_RESOLVED` peut déjà avoir committé des effets optionnels ou principaux.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if not result.is_success():
	rebuild_from_fresh_snapshot()
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les résultats partiels sont consommés et les vrais refus nécessitent une nouvelle décision.

## 43. Tests à préparer

### 43.1 Tests unitaires

- identifiants stables ;
- validation des coûts, cibles et définitions ;
- ordre des effets ;
- recharge par rang ;
- récupération de plusieurs charges ;
- progression et rang maximal ;
- coût gratuit explicitement autorisé ;
- résultat partiel ;
- copie profonde des plans ;
- refus de types d’effets inconnus ;
- codec strict, doublons et clés inconnues.

### 43.2 Tests d’intégration

- compétence vers commande de combat ;
- coût préparé puis cible refusée ;
- coût et charge après succès ;
- refus de commit sur révision obsolète ;
- soin borné par `CharacterRules` ;
- état de combat appliqué par le port ;
- action d’agent vers la même autorité ;
- sauvegarde et restauration.

### 43.3 Simulations

- 1, 64 et 256 compétences par personnage ;
- 1, 8 et 32 effets ;
- 1, 16 et 128 cibles candidates ;
- récupération hors écran sur de longues périodes ;
- plusieurs personnages utilisant la même définition partagée ;
- progression jusqu’au rang maximal ;
- répétition depuis les mêmes snapshots.

## 44. Validation légère sans PDF

> **[PS] PowerShell 7 — Depuis la racine du dépôt, lancer les validations documentaires légères.**

```powershell
python tools/validate_chapters.py
python tools/check_context_markers.py
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La première commande contrôle structure, métadonnées, liens et doublons.
- La seconde contrôle présence et cohérence sémantique des repères.
- Elles ne construisent aucun PDF.
- Leur réussite ne remplace ni le parseur Godot ni une scène exécutée.

> **[SORTIE] Résultat attendu — Ne pas saisir.**

```text
Aucune erreur bloquante.
Aucun PDF produit.
Les repères d’utilisation sont cohérents.
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Cette sortie est un critère de lecture, pas une preuve d’exécution locale.
- La preuve officielle du lot doit référencer les runs GitHub Actions réellement terminés.

## 45. Réserves runtime

Cette rédaction est une revue statique. Elle ne prouve pas :

- que tous les scripts passent le parseur Godot 4.7.1 ;
- que `duplicate(true)` recopie chaque sous-ressource comme attendu dans toutes les combinaisons ;
- que l’unité de travail coordonne réellement effets, coût, charge et progression sans mutation partielle ;
- que les ports de combat et de personnage sont exécutables ;
- que la scène pédagogique est instanciable ;
- que les recharges se comportent correctement avec pause et changement de fréquence ;
- que les performances tiennent avec 256 compétences et 128 cibles ;
- que le codec complet et ses migrations futures sont exécutables ;
- que les animations et interfaces consomment correctement les résultats ;
- qu’un replay reste identique entre plateformes et versions ;
- qu’un PDF intermédiaire a été produit.

## 46. Résumé

Les compétences et pouvoirs sont des définitions de conception associées à une progression et à un état runtime par personnage. Le service vérifie apprentissage, rang, coûts, charges, recharge et forme de cible, puis construit un plan d’effets détaché.

Les systèmes propriétaires conservent leur autorité : le combat valide et applique dégâts ou états ; les personnages bornent santé et endurance ; l’inventaire futur pourra accorder des compétences sans les posséder. Les plans, réservations, prévisualisations et caches restent transitoires.

## 47. Sources techniques

- [Godot 4.7 — `Resource`](https://docs.godotengine.org/en/4.7/classes/class_resource.html)
- [Godot 4.7 — `RefCounted`](https://docs.godotengine.org/en/4.7/classes/class_refcounted.html)
- [Godot 4.7 — `Array`](https://docs.godotengine.org/en/4.7/classes/class_array.html)
- [Godot 4.7 — `Dictionary`](https://docs.godotengine.org/en/4.7/classes/class_dictionary.html)
- [Godot 4.7 — `StringName`](https://docs.godotengine.org/en/4.7/classes/class_stringname.html)
- [Godot 4.7 — `Variant`](https://docs.godotengine.org/en/4.7/classes/class_variant.html)
- [Godot 4.7 — `Vector3`](https://docs.godotengine.org/en/4.7/classes/class_vector3.html)
- [Godot 4.7 — `Error`](https://docs.godotengine.org/en/4.7/classes/class_%40globalscope.html#enum-globalscope-error)
- [Godot 4.7 — signaux](https://docs.godotengine.org/en/4.7/getting_started/step_by_step/signals.html)
- [Godot 4.7 — `Timer`](https://docs.godotengine.org/en/4.7/classes/class_timer.html)
- [Chapitre 7 — Données avec Resources, JSON et configurations](CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md)
- [Chapitre 9 — Sauvegardes, chargements et compatibilité](CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md)
- [Chapitre 14 — Personnages](CHAPITRE-14-Personnages.md)
- [Chapitre 17 — Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md)
- [Chapitre 18 — Combat](CHAPITRE-18-Combat.md)

## 48. Synthèse opérationnelle pour Project Asteria

Le système de compétences et pouvoirs de `Project Asteria` repose sur les décisions suivantes :

1. `AbilityDefinition` constitue une donnée de conception partagée et immuable ;
2. progression et état runtime sont séparés de la définition et liés au `CharacterId` ;
3. rang, expérience, charges et ticks de recharge sont persistés ;
4. les coûts sont décrits par identifiants de ressources et réservés avant commit ;
5. aucune ressource n’est retirée directement par la définition ou la présentation ;
6. les ciblages `SELF`, personnage, point et zone sont déclaratifs et bornés ;
7. la prévisualisation ne remplace jamais la validation autoritaire ;
8. les effets sont composables, ordonnés, copiés et limités à des types autorisés ;
9. les dégâts et états passent par le système de combat ;
10. santé et endurance restent sous les règles des personnages ;
11. un effet requis refusé empêche une réussite mensongère ;
12. un résultat partiel est une exécution consommée et non un retry gratuit ;
13. les recharges utilisent des ticks logiques, jamais un `Timer` autoritaire ;
14. les plans, réservations, cibles dérivées, caches et VFX ne sont pas persistés ;
15. le chapitre 20 pourra accorder des compétences par objets sans déplacer l’autorité des compétences ni du combat.
