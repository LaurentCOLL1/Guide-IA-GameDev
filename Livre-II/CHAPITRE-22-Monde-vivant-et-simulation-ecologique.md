---
title: "Livre II — Chapitre 22 : Monde vivant et simulation écologique"
id: "DOC-L2-CH22"
status: "reviewed"
version: "1.0.4"
lang: "fr-FR"
book: "Livre II"
chapter: 22
last-verified: "2026-07-22T01:40:00+02:00"
audit-status: "complete"
audit-date: "2026-07-22T01:40:00+02:00"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-22.md"
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
---

# Monde vivant et simulation écologique

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH22`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  

> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-22.md`.
> **Explications de code :** structurées bloc par bloc ; les informations pédagogiques antérieures sont conservées dans des rubriques explicites, complétées seulement lorsque le bloc l’exige.

## 1. Rôle du chapitre

Les chapitres précédents ont construit les personnages, les agents, le combat, les compétences, l’inventaire et l’économie. Ils savent traiter une action locale, mais ils ne possèdent pas encore une autorité globale capable de faire évoluer les régions, populations et ressources lorsque le joueur ne les regarde pas.

Ce chapitre construit le **monde vivant** de `Project Asteria`. Il définit :

- une horloge logique globale ;
- des régions écologiques identifiées ;
- des espèces et ressources décrites par des données de conception ;
- des populations et réserves vivantes séparées des scènes ;
- des étapes de simulation déterministes et bornées ;
- des modes actif, arrière-plan et dormant ;
- des apparitions et disparitions de représentations sans création ou destruction implicite de population ;
- des récoltes coordonnées avec l’inventaire ;
- des indices écologiques transmis à l’économie sans produire de prix ;
- une persistance stricte et une restauration préparée.

Le système doit garantir que :

- le temps autoritaire ne dépend ni de l’heure système ni d’un `Timer` de scène ;
- les populations existent même sans nœud actif ;
- les quantités utilisent des entiers et des résidus déterministes ;
- une région longtemps inactive est rattrapée par une étape agrégée bornée, pas par des millions de ticks rejoués ;
- l’apparition d’un acteur ne modifie pas le nombre logique d’individus ;
- une récolte ne réduit pas une ressource sans produire le candidat d’inventaire correspondant ;
- l’écologie peut publier une rareté ou une abondance, mais jamais un prix ;
- une sortie IA ne modifie aucune population, ressource ou horloge.

## 2. Prérequis

Le lecteur doit avoir parcouru :

- le chapitre 4 pour l’architecture feature-first ;
- le chapitre 5 pour l’injection, les services et les unités de travail ;
- le chapitre 7 pour les `Resource`, catalogues et identifiants stables ;
- le chapitre 9 pour les sauvegardes préparées avant application ;
- le chapitre 14 pour l’identité logique des personnages ;
- le chapitre 17 pour les agents, les modes actif/arrière-plan/dormant et l’ordonnancement borné ;
- le chapitre 20 pour les objets, lots et transferts d’inventaire ;
- le chapitre 21 pour les contextes de prix et les transactions économiques.

## 3. Périmètre et frontières

Ce chapitre couvre :

- l’horloge logique du monde ;
- les jours, cycles et ticks persistables ;
- les définitions de régions écologiques ;
- les définitions d’espèces et de ressources ;
- les états agrégés de populations ;
- les réserves de ressources et leur régénération ;
- la capacité d’accueil ;
- les naissances et décès écologiques agrégés ;
- la simulation active, en arrière-plan et dormante ;
- le rattrapage agrégé après une longue absence ;
- la matérialisation et la dématérialisation des représentations ;
- la frontière de récolte avec l’inventaire ;
- les signaux de rareté ou d’abondance pour l’économie ;
- les observations structurées destinées aux agents ;
- la persistance du monde vivant.

Il ne couvre pas :

- les buts, plans et décisions individuelles des agents ;
- les dégâts et décès de combat ;
- l’identité et l’état des personnages nommés ;
- les prix, offres, paiements ou portefeuilles ;
- les factions, frontières politiques, lois ou sanctions ;
- la propriété foncière, les bâtiments et chaînes de production ;
- les quêtes et conséquences narratives ;
- la météo physique détaillée ;
- le multijoueur ;
- l’équilibrage final des courbes écologiques.

> **Frontière essentielle :** l’écologie possède le temps logique global, les régions, populations agrégées, ressources et transitions écologiques. Les personnages possèdent les identités individuelles ; les agents choisissent des requêtes ; l’inventaire possède les objets produits ; l’économie possède les prix et transactions.

## 4. Chaîne d’autorité

> **[LECTURE] Flux d’une étape écologique — Ne pas saisir.**

```text
WorldClockState
    ↓ tick logique courant
EcologyScheduler
    ├── sélectionne les régions échues
    ├── respecte un budget borné
    └── calcule elapsed_ticks
            ↓
RegionEcologySimulator
    ├── relit définition, état et contexte environnemental
    ├── prépare ressources et populations candidates
    ├── calcule événements et signaux dérivés
    └── valide le candidat complet
            ↓
EcologyRepository.replace_region()
            ↓
événements typés après commit
            ↓
agents, présentation, économie et matérialisation
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Point d’explication complémentaire :** L’horloge fournit un tick logique unique à tous les systèmes.

- **Point d’explication complémentaire — complément 2 :** L’ordonnanceur choisit le travail à effectuer sans changer les règles écologiques.

- **Point d’explication complémentaire — complément 3 :** Le simulateur calcule uniquement sur des copies détachées.

- **Point d’explication complémentaire — complément 4 :** Le dépôt remplace un état régional seulement après validation complète.

- **Résultat attendu et vérification :** Les consommateurs reçoivent des événements après le commit et ne peuvent pas imposer le résultat.

## 5. Architecture retenue

> **[LECTURE] Arborescence cible — Ne pas créer depuis un terminal.**

```text
res://src/features/ecology/
├── domain/
│   ├── ecology_id.gd
│   ├── world_clock_state.gd
│   ├── ecology_region_definition.gd
│   ├── species_definition.gd
│   ├── ecology_resource_definition.gd
│   ├── population_state.gd
│   ├── resource_pool_state.gd
│   ├── region_ecology_state.gd
│   ├── ecology_step_result.gd
│   ├── ecology_command_result.gd
│   ├── population_delta_command.gd
│   └── harvest_ecology_command.gd
├── application/
│   ├── ecology_catalog.gd
│   ├── ecology_repository.gd
│   ├── ecology_math.gd
│   ├── world_clock_service.gd
│   ├── ecology_environment_port.gd
│   ├── ecology_access_port.gd
│   ├── carrying_capacity_policy.gd
│   ├── region_ecology_simulator.gd
│   ├── ecology_simulation_mode.gd
│   ├── ecology_region_mode_port.gd
│   ├── ecology_tick_policy.gd
│   ├── ecology_scheduler.gd
│   ├── ecology_service.gd
│   ├── ecology_materialization_port.gd
│   ├── ecology_inventory_yield_port.gd
│   ├── ecology_transaction_commit_port.gd
│   ├── ecology_market_signal_port.gd
│   └── ecology_agent_observation_port.gd
├── infrastructure/
│   ├── ecology_snapshot_codec.gd
│   └── ecology_save_section.gd
└── presentation/
    └── ecology_presentation_bridge.gd

res://data/ecology/
├── regions/
├── species/
└── resources/

res://scenes/learning/
├── ch22_living_world_demo.tscn
└── ch22_living_world_demo.gd
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** `domain` porte les données, commandes, résultats et invariants indépendants des scènes.

- **Frontières d’autorité :** `application` orchestre l’horloge, les étapes, budgets et ports vers les autres autorités.

- **Point d’explication complémentaire :** `infrastructure` encode uniquement les données durables.

- **Valeur de retour ou code d’échec :** `presentation` transforme des résultats committés en retour visuel.

- **Point d’explication complémentaire — complément 2 :** Les définitions `.tres` restent séparées des états vivants sauvegardés.

## 6. Vocabulaire

Une **région écologique** est une unité logique de simulation. Elle peut correspondre à une vallée, une forêt, un district ou une zone maritime, sans imposer une scène Godot particulière.

Une **population** est un nombre logique d’individus appartenant à une espèce dans une région. Elle inclut les individus représentés et non représentés.

Une **représentation matérialisée** est un personnage ou acteur instancié dans une scène. Sa présence n’est pas l’autorité du nombre total d’individus.

Une **réserve de ressource** est une quantité écologique agrégée : biomasse, eau, minerai accessible ou nourriture sauvage. Elle n’est pas un inventaire.

Une **capacité d’accueil** est une limite calculée à partir de la région, des ressources et du contexte environnemental.

Un **résidu** conserve la fraction entière non encore convertie en unité complète. Il évite qu’une petite croissance quotidienne disparaisse à chaque division entière.

Une **étape agrégée** fait évoluer un état sur plusieurs ticks en une seule opération bornée.

## 7. Identifiants du monde vivant

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/domain/ecology_id.gd`.**

```gdscript
class_name EcologyId
extends RefCounted

const REGION_PREFIX := "ecology.region."
const SPECIES_PREFIX := "ecology.species."
const RESOURCE_PREFIX := "ecology.resource."
const EVENT_PREFIX := "ecology.event."
const COMMAND_PREFIX := "ecology.command."

static func region(slug: String) -> StringName:
	return _from_slug(REGION_PREFIX, slug)

static func species(slug: String) -> StringName:
	return _from_slug(SPECIES_PREFIX, slug)

static func resource(slug: String) -> StringName:
	return _from_slug(RESOURCE_PREFIX, slug)

static func event(region_id: StringName, sequence: int) -> StringName:
	if not StableId.is_valid(region_id) or sequence < 0:
		return &""
	return StringName("%s%s.%d" % [EVENT_PREFIX, region_id, sequence])

static func command(uuid_text: String) -> StringName:
	return _from_slug(COMMAND_PREFIX, uuid_text)

static func _from_slug(prefix: String, value: String) -> StringName:
	var normalized := value.strip_edges().to_lower().replace("-", "_")
	if normalized.is_empty():
		return &""
	for character: String in normalized:
		var is_letter := character >= "a" and character <= "z"
		var is_digit := character >= "0" and character <= "9"
		if not is_letter and not is_digit and character != "_":
			return &""
	return StringName(prefix + normalized)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Point d’explication complémentaire :** Chaque famille d’identifiants possède un préfixe stable.

- **Dépendances et ports utilisés :** Les régions, espèces et ressources ne dépendent pas d’un nom localisé.

- **Persistance et restauration :** Un événement est ordonné par une séquence régionale persistée.

- **Limites et réserves :** Une commande externe reçoit une identité distincte pour l’idempotence.

- **Invariants protégés :** Une entrée invalide renvoie `&""` au lieu de fabriquer une identité partielle.

## 8. Horloge logique globale

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/domain/world_clock_state.gd`.**

```gdscript
class_name WorldClockState
extends RefCounted

const MAX_SAFE_INTEGER := 9007199254740991

var logical_tick: int = 0
var ticks_per_day: int = 3600
var revision: int = 0

func validate() -> Error:
	if logical_tick < 0 or logical_tick > MAX_SAFE_INTEGER:
		return ERR_INVALID_DATA
	if ticks_per_day < 1 or ticks_per_day > 1000000:
		return ERR_INVALID_DATA
	if revision < 0:
		return ERR_INVALID_DATA
	return OK

func day_index() -> int:
	return logical_tick / ticks_per_day

func tick_in_day() -> int:
	return logical_tick % ticks_per_day

func duplicate_detached() -> WorldClockState:
	var copy := WorldClockState.new()
	copy.logical_tick = logical_tick
	copy.ticks_per_day = ticks_per_day
	copy.revision = revision
	return copy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** `logical_tick` ordonne le monde sans consulter l’heure de l’ordinateur.

- **Persistance et restauration :** `ticks_per_day` définit une convention de simulation persistable.

- **Limites et réserves — complément 2 :** `day_index()` et `tick_in_day()` sont dérivés et ne sont pas sauvegardés séparément.

- **Point d’explication complémentaire :** La plage reste compatible avec les entiers JSON exacts retenus au chapitre 9.

- **Limites et réserves — complément 3 :** La copie détachée permet de préparer une avance sans modifier l’horloge active.

## 9. Faire avancer l’horloge

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/world_clock_service.gd`.**

```gdscript
class_name WorldClockService
extends RefCounted

signal clock_advanced(previous_tick: int, current_tick: int)

var _repository: EcologyRepository

func advance(elapsed_ticks: int, expected_revision: int) -> Error:
	if _repository == null:
		return ERR_UNCONFIGURED
	var source := _repository.get_clock()
	if source == null or source.validate() != OK:
		return ERR_UNCONFIGURED
	if elapsed_ticks < 1 or elapsed_ticks > 1000000:
		return ERR_INVALID_PARAMETER
	if source.revision != expected_revision:
		return ERR_BUSY
	if source.logical_tick > WorldClockState.MAX_SAFE_INTEGER - elapsed_ticks:
		return ERR_OUT_OF_MEMORY

	var candidate := source.duplicate_detached()
	var previous_tick := candidate.logical_tick
	candidate.logical_tick += elapsed_ticks
	candidate.revision += 1
	if candidate.validate() != OK:
		return ERR_INVALID_DATA
	var code := _repository.replace_clock(candidate, expected_revision)
	if code != OK:
		return code
	clock_advanced.emit(previous_tick, candidate.logical_tick)
	return OK

func snapshot() -> WorldClockState:
	if _repository == null:
		return null
	return _repository.get_clock()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** Le service reçoit un nombre de ticks explicite ; il ne mesure pas une durée réelle (durée de l’horloge système).

- **Point d’explication complémentaire :** La révision empêche deux avances concurrentes d’écraser le même état.

- **Résultat attendu et vérification :** Le dépassement est vérifié avant l’addition.

- **Invariants protégés :** Le dépôt revalide la révision au dernier instant avant remplacement.

- **Point d’explication complémentaire — complément 2 :** Le signal est émis seulement après le commit de l’horloge candidate.

- **Limites et réserves — complément 2 :** Une adaptation Godot peut appeler `advance(1, revision)` depuis `_physics_process()`. `Time.get_ticks_usec()` peut mesurer le coût de calcul, mais ne devient jamais l’horloge du monde.

## 10. Définition d’une région écologique

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/domain/ecology_region_definition.gd`.**

```gdscript
class_name EcologyRegionDefinition
extends Resource

@export var region_id: StringName
@export var display_name_key: StringName
@export var area_units: int = 1
@export var base_fertility_bp: int = 10000
@export var water_access_bp: int = 10000
@export var habitat_tags: Array[StringName] = []

func validate() -> Error:
	if not StableId.is_valid(region_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(display_name_key):
		return ERR_INVALID_DATA
	if area_units < 1 or area_units > 1000000000:
		return ERR_INVALID_DATA
	if base_fertility_bp < 0 or base_fertility_bp > 50000:
		return ERR_INVALID_DATA
	if water_access_bp < 0 or water_access_bp > 50000:
		return ERR_INVALID_DATA
	if habitat_tags.is_empty() or habitat_tags.size() > 32:
		return ERR_INVALID_DATA
	var seen: Dictionary[StringName, bool] = {}
	for tag: StringName in habitat_tags:
		if not StableId.is_valid(tag) or seen.has(tag):
			return ERR_INVALID_DATA
		seen[tag] = true
	return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** La région est une `Resource` de conception partagée et immuable pendant le gameplay.

- **Limites et réserves — complément 2 :** `area_units` utilise une unité logique documentée par le projet, pas une surface de collision.

- **Point d’explication complémentaire :** Fertilité et accès à l’eau sont exprimés en points de base.

- **Point d’explication complémentaire — complément 2 :** Les tags sont obligatoires, stables et sans doublon.

- **Limites et réserves — complément 3 :** Aucun nombre vivant ni nœud actif n’est stocké dans cette définition.

## 11. Définition d’une espèce

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/domain/species_definition.gd`.**

```gdscript
class_name SpeciesDefinition
extends Resource

@export var species_id: StringName
@export var display_name_key: StringName
@export var habitat_tags: Array[StringName] = []
@export var base_capacity_per_area: int = 1
@export var birth_rate_bp_per_day: int = 100
@export var death_rate_bp_per_day: int = 50
@export var food_resource_id: StringName
@export var food_units_per_individual_per_day: int = 1

func validate() -> Error:
	if not StableId.is_valid(species_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(display_name_key):
		return ERR_INVALID_DATA
	if habitat_tags.is_empty() or habitat_tags.size() > 16:
		return ERR_INVALID_DATA
	var seen: Dictionary[StringName, bool] = {}
	for tag: StringName in habitat_tags:
		if not StableId.is_valid(tag) or seen.has(tag):
			return ERR_INVALID_DATA
		seen[tag] = true
	if base_capacity_per_area < 0 or base_capacity_per_area > 1000000:
		return ERR_INVALID_DATA
	for rate: int in [birth_rate_bp_per_day, death_rate_bp_per_day]:
		if rate < 0 or rate > 10000:
			return ERR_INVALID_DATA
	if food_units_per_individual_per_day < 0 or food_units_per_individual_per_day > 1000000:
		return ERR_INVALID_DATA
	if food_units_per_individual_per_day > 0:
		if not StableId.is_valid(food_resource_id):
			return ERR_INVALID_DATA
	elif not food_resource_id.is_empty() and not StableId.is_valid(food_resource_id):
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** Une espèce décrit des paramètres de conception, jamais un individu particulier.

- **Point d’explication complémentaire :** Les taux quotidiens restent entiers en points de base.

- **Point d’explication complémentaire — complément 2 :** `food_resource_id` nomme explicitement la réserve consommée lorsque la consommation est positive.

- **Point d’explication complémentaire — complément 3 :** Les tags d’habitat sont validés et dédupliqués.

- **Frontières d’autorité :** Les identités individuelles éventuelles restent sous l’autorité des personnages.

## 12. Définition d’une ressource écologique

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/domain/ecology_resource_definition.gd`.**

```gdscript
class_name EcologyResourceDefinition
extends Resource

@export var resource_id: StringName
@export var display_name_key: StringName
@export var habitat_tags: Array[StringName] = []
@export var capacity_per_area: int = 1
@export var regeneration_units_per_day: int = 0
@export var inventory_item_definition_id: StringName

func validate() -> Error:
	if not StableId.is_valid(resource_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(display_name_key):
		return ERR_INVALID_DATA
	if habitat_tags.is_empty() or habitat_tags.size() > 16:
		return ERR_INVALID_DATA
	if capacity_per_area < 0 or capacity_per_area > 1000000000:
		return ERR_INVALID_DATA
	if regeneration_units_per_day < 0 or regeneration_units_per_day > 1000000000:
		return ERR_INVALID_DATA
	if not inventory_item_definition_id.is_empty():
		if not StableId.is_valid(inventory_item_definition_id):
			return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** Une réserve écologique et un objet d’inventaire sont deux concepts distincts.

- **Limites et réserves — complément 2 :** `inventory_item_definition_id` indique seulement le rendement possible d’une récolte.

- **Point d’explication complémentaire :** La capacité et la régénération utilisent des unités entières propres à la ressource.

- **Limites et réserves — complément 3 :** Les tags limitent la présence de la ressource à des habitats compatibles.

- **Frontières d’autorité :** Le chapitre 20 reste propriétaire de la création des lots d’objets.

## 13. État d’une population

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/domain/population_state.gd`.**

```gdscript
class_name PopulationState
extends RefCounted

var species_id: StringName
var count: int = 0
var birth_residual: int = 0
var death_residual: int = 0
var revision: int = 0

func validate(ticks_per_day: int) -> Error:
	if not StableId.is_valid(species_id):
		return ERR_INVALID_DATA
	if ticks_per_day < 1 or ticks_per_day > 1000000:
		return ERR_INVALID_PARAMETER
	if count < 0 or count > 1000000000:
		return ERR_INVALID_DATA
	if birth_residual < 0 or birth_residual >= ticks_per_day:
		return ERR_INVALID_DATA
	if death_residual < 0 or death_residual >= ticks_per_day:
		return ERR_INVALID_DATA
	if revision < 0:
		return ERR_INVALID_DATA
	return OK

func duplicate_detached() -> PopulationState:
	var copy := PopulationState.new()
	copy.species_id = species_id
	copy.count = count
	copy.birth_residual = birth_residual
	copy.death_residual = death_residual
	copy.revision = revision
	return copy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Point d’explication complémentaire :** `count` inclut les individus matérialisés et non matérialisés.

- **Point d’explication complémentaire — complément 2 :** Les résidus de naissance et de décès conservent les fractions issues des calculs entiers.

- **Persistance et restauration :** Chaque résidu reste dans l’intervalle `0` à `ticks_per_day - 1`, ce qui rend le snapshot vérifiable.

- **Limites et réserves :** Une population n’enregistre ni liste de nœuds ni identités de personnages.

- **Point d’explication complémentaire — complément 3 :** `revision` protège les commandes causales préparées depuis un ancien état.

## 14. État d’une réserve de ressource

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/domain/resource_pool_state.gd`.**

```gdscript
class_name ResourcePoolState
extends RefCounted

var resource_id: StringName
var quantity_units: int = 0
var regeneration_residual: int = 0
var consumption_residual: int = 0
var revision: int = 0

func validate(maximum_units: int, ticks_per_day: int) -> Error:
	if not StableId.is_valid(resource_id):
		return ERR_INVALID_DATA
	if maximum_units < 0 or ticks_per_day < 1 or ticks_per_day > 1000000:
		return ERR_INVALID_PARAMETER
	if quantity_units < 0 or quantity_units > maximum_units:
		return ERR_INVALID_DATA
	if regeneration_residual < 0 or regeneration_residual >= ticks_per_day:
		return ERR_INVALID_DATA
	if consumption_residual < 0 or consumption_residual >= ticks_per_day:
		return ERR_INVALID_DATA
	if revision < 0:
		return ERR_INVALID_DATA
	return OK

func duplicate_detached() -> ResourcePoolState:
	var copy := ResourcePoolState.new()
	copy.resource_id = resource_id
	copy.quantity_units = quantity_units
	copy.regeneration_residual = regeneration_residual
	copy.consumption_residual = consumption_residual
	copy.revision = revision
	return copy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** La borne maximale vient de la définition et de la région, pas de l’état lui-même.

- **Point d’explication complémentaire :** Les résidus distinguent régénération et consommation afin de diagnostiquer leur origine.

- **Point d’explication complémentaire — complément 2 :** Chaque résidu est validé contre la même convention `ticks_per_day` que l’horloge sauvegardée.

- **Limites et réserves — complément 2 :** L’état ne contient aucun objet d’inventaire.

- **Invariants protégés :** La révision permet de refuser une récolte préparée depuis une ancienne quantité.

## 15. État écologique d’une région

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/domain/region_ecology_state.gd`.**

```gdscript
class_name RegionEcologyState
extends RefCounted

const MAX_POPULATIONS := 128
const MAX_RESOURCE_POOLS := 128

var region_id: StringName
var last_simulated_tick: int = 0
var revision: int = 0
var event_sequence: int = 0
var populations: Dictionary[StringName, PopulationState] = {}
var resources: Dictionary[StringName, ResourcePoolState] = {}

func validate(catalog: EcologyCatalog, ticks_per_day: int) -> Error:
	if catalog == null:
		return ERR_UNCONFIGURED
	if ticks_per_day < 1 or ticks_per_day > 1000000:
		return ERR_INVALID_PARAMETER
	if catalog.get_region(region_id) == null:
		return ERR_DOES_NOT_EXIST
	if last_simulated_tick < 0 or revision < 0 or event_sequence < 0:
		return ERR_INVALID_DATA
	if populations.size() > MAX_POPULATIONS or resources.size() > MAX_RESOURCE_POOLS:
		return ERR_OUT_OF_MEMORY

	for species_id: StringName in populations:
		var population := populations[species_id] as PopulationState
		var species := catalog.get_species(species_id)
		if population == null or population.species_id != species_id:
			return ERR_INVALID_DATA
		if species == null or not catalog.is_species_allowed(region_id, species_id):
			return ERR_INVALID_DATA
		if population.validate(ticks_per_day) != OK:
			return ERR_INVALID_DATA
		if species.food_units_per_individual_per_day > 0:
			if not resources.has(species.food_resource_id):
				return ERR_DOES_NOT_EXIST

	for resource_id: StringName in resources:
		var pool := resources[resource_id] as ResourcePoolState
		var maximum := catalog.maximum_resource_units(region_id, resource_id)
		if pool == null or pool.resource_id != resource_id:
			return ERR_INVALID_DATA
		if not catalog.is_resource_allowed(region_id, resource_id):
			return ERR_INVALID_DATA
		if pool.validate(maximum, ticks_per_day) != OK:
			return ERR_INVALID_DATA
	return OK

func duplicate_detached() -> RegionEcologyState:
	var copy := RegionEcologyState.new()
	copy.region_id = region_id
	copy.last_simulated_tick = last_simulated_tick
	copy.revision = revision
	copy.event_sequence = event_sequence
	for species_id: StringName in populations:
		copy.populations[species_id] = populations[species_id].duplicate_detached()
	for resource_id: StringName in resources:
		copy.resources[resource_id] = resources[resource_id].duplicate_detached()
	return copy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Point d’explication complémentaire :** La région regroupe les agrégats qui doivent évoluer ensemble.

- **Point d’explication complémentaire — complément 2 :** Les clés des dictionnaires sont recoupées avec les identifiants contenus dans les valeurs.

- **Résultat attendu et vérification :** Le catalogue vérifie les habitats et la présence de la ressource alimentaire déclarée par chaque espèce.

- **Persistance et restauration :** Les résidus utilisent la convention temporelle de l’horloge avant toute simulation ou restauration.

- **Point d’explication complémentaire — complément 3 :** La copie profonde prépare toutes les populations et ressources sans partager d’état mutable.

## 16. Catalogue écologique

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/ecology_catalog.gd`.**

```gdscript
class_name EcologyCatalog
extends RefCounted

var _regions: Dictionary[StringName, EcologyRegionDefinition] = {}
var _species: Dictionary[StringName, SpeciesDefinition] = {}
var _resources: Dictionary[StringName, EcologyResourceDefinition] = {}

func register_region(definition: EcologyRegionDefinition) -> Error:
	if definition == null or definition.validate() != OK:
		return ERR_INVALID_DATA
	if _regions.has(definition.region_id):
		return ERR_ALREADY_EXISTS
	_regions[definition.region_id] = definition.duplicate(true) as EcologyRegionDefinition
	return OK

func register_species(definition: SpeciesDefinition) -> Error:
	if definition == null or definition.validate() != OK:
		return ERR_INVALID_DATA
	if _species.has(definition.species_id):
		return ERR_ALREADY_EXISTS
	_species[definition.species_id] = definition.duplicate(true) as SpeciesDefinition
	return OK

func register_resource(definition: EcologyResourceDefinition) -> Error:
	if definition == null or definition.validate() != OK:
		return ERR_INVALID_DATA
	if _resources.has(definition.resource_id):
		return ERR_ALREADY_EXISTS
	_resources[definition.resource_id] = definition.duplicate(true) as EcologyResourceDefinition
	return OK

func validate_cross_references() -> Error:
	for species: SpeciesDefinition in _species.values():
		if species.food_units_per_individual_per_day > 0:
			if not _resources.has(species.food_resource_id):
				return ERR_DOES_NOT_EXIST
	return OK

func get_region(region_id: StringName) -> EcologyRegionDefinition:
	var value := _regions.get(region_id) as EcologyRegionDefinition
	return null if value == null else value.duplicate(true) as EcologyRegionDefinition

func get_species(species_id: StringName) -> SpeciesDefinition:
	var value := _species.get(species_id) as SpeciesDefinition
	return null if value == null else value.duplicate(true) as SpeciesDefinition

func get_resource(resource_id: StringName) -> EcologyResourceDefinition:
	var value := _resources.get(resource_id) as EcologyResourceDefinition
	return null if value == null else value.duplicate(true) as EcologyResourceDefinition

func is_species_allowed(region_id: StringName, species_id: StringName) -> bool:
	var region := get_region(region_id)
	var species := get_species(species_id)
	return (
		region != null
		and species != null
		and _shares_habitat(region.habitat_tags, species.habitat_tags)
	)

func is_resource_allowed(region_id: StringName, resource_id: StringName) -> bool:
	var region := get_region(region_id)
	var definition := get_resource(resource_id)
	return (
		region != null
		and definition != null
		and _shares_habitat(region.habitat_tags, definition.habitat_tags)
	)

func maximum_resource_units(region_id: StringName, resource_id: StringName) -> int:
	if not is_resource_allowed(region_id, resource_id):
		return -1
	var region := get_region(region_id)
	var definition := get_resource(resource_id)
	var value: Variant = EcologyMath.checked_multiply(
		region.area_units,
		definition.capacity_per_area,
	)
	return -1 if value == null else int(value)

func _shares_habitat(left: Array[StringName], right: Array[StringName]) -> bool:
	for tag: StringName in left:
		if tag in right:
			return true
	return false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Les trois méthodes `register_*()` valident puis copient les `Resource` de conception.

- **Valeur de retour ou code d’échec :** Les doublons sont refusés et les lectures retournent encore des copies pour préserver l’immuabilité.

- **Résultat attendu et vérification :** `validate_cross_references()` s’exécute après le chargement complet afin de vérifier les ressources alimentaires.

- **Point d’explication complémentaire :** Les compatibilités de région utilisent des tags d’habitat partagés, jamais un nom affiché.

- **Limites et réserves :** `maximum_resource_units()` renvoie `-1` pour une définition absente, un habitat incompatible ou un dépassement.

## 17. Arithmétique écologique déterministe

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/ecology_math.gd`.**

```gdscript
class_name EcologyMath
extends RefCounted

const MAX_SAFE_INTEGER := 9007199254740991
const BASIS_POINT_SCALE := 10000

class RateResult:
	extends RefCounted

	var whole_units: int = 0
	var residual: int = 0

static func checked_add(left: int, right: int) -> Variant:
	if left < -MAX_SAFE_INTEGER or left > MAX_SAFE_INTEGER:
		return null
	if right < -MAX_SAFE_INTEGER or right > MAX_SAFE_INTEGER:
		return null
	if right > 0 and left > MAX_SAFE_INTEGER - right:
		return null
	if right < 0 and left < -MAX_SAFE_INTEGER - right:
		return null
	return left + right

static func checked_multiply(left: int, right: int) -> Variant:
	if left < 0 or right < 0:
		return null
	if left == 0 or right == 0:
		return 0
	if left > MAX_SAFE_INTEGER / right:
		return null
	return left * right

static func multiply_basis_points_floor(value: int, basis_points: int) -> Variant:
	if value < 0 or basis_points < 0 or basis_points > 50000:
		return null
	var product: Variant = checked_multiply(value, basis_points)
	if product == null:
		return null
	return int(product) / BASIS_POINT_SCALE

static func accrue(
	units_per_day: int,
	elapsed_ticks: int,
	ticks_per_day: int,
	previous_residual: int,
) -> RateResult:
	if units_per_day < 0 or elapsed_ticks < 0 or ticks_per_day < 1:
		return null
	if previous_residual < 0 or previous_residual >= ticks_per_day:
		return null
	var product: Variant = checked_multiply(units_per_day, elapsed_ticks)
	if product == null:
		return null
	var numerator: Variant = checked_add(int(product), previous_residual)
	if numerator == null:
		return null
	var result := RateResult.new()
	result.whole_units = int(numerator) / ticks_per_day
	result.residual = int(numerator) % ticks_per_day
	return result
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Les additions et multiplications refusent un résultat hors de la plage entière sûre du projet.

- **Point d’explication complémentaire :** `multiply_basis_points_floor()` applique un taux déterministe sans nombre flottant.

- **Point d’explication complémentaire — complément 2 :** `accrue()` transforme un taux quotidien en unités complètes sur un intervalle de ticks.

- **Limites et réserves :** Le modulo conserve la fraction non encore transformée en unité et la validation borne le résidu.

- **Invariants protégés — complément 2 :** `Variant` permet de distinguer un calcul invalide d’un résultat entier valide égal à zéro.

## 18. Contexte environnemental

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/ecology_environment_port.gd`.**

```gdscript
class_name EcologyEnvironmentPort
extends RefCounted

class Snapshot:
	extends RefCounted

	var region_id: StringName
	var revision: int = 0
	var valid_until_tick: int = 0
	var fertility_multiplier_bp: int = 10000
	var water_multiplier_bp: int = 10000
	var hazard_multiplier_bp: int = 10000

	func validate() -> Error:
		if not StableId.is_valid(region_id):
			return ERR_INVALID_DATA
		if revision < 0 or valid_until_tick < 0:
			return ERR_INVALID_DATA
		for value: int in [
			fertility_multiplier_bp,
			water_multiplier_bp,
			hazard_multiplier_bp,
		]:
			if value < 0 or value > 50000:
				return ERR_INVALID_DATA
		return OK

func snapshot_for(_region_id: StringName, _logical_tick: int) -> Snapshot:
	return null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** Le port fournit des indices validés sans exposer une scène météo ou un nœud physique.

- **Point d’explication complémentaire :** Les multiplicateurs utilisent des points de base.

- **Invariants protégés :** `valid_until_tick` permet de refuser un contexte ancien.

- **Point d’explication complémentaire — complément 2 :** Le chapitre peut fonctionner avec un adaptateur constant lorsque la météo détaillée n’existe pas.

- **Persistance et restauration :** Une sortie IA ne peut pas fabriquer ce snapshot autoritaire.

## 19. Calculer une capacité d’accueil

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/carrying_capacity_policy.gd`.**

```gdscript
class_name CarryingCapacityPolicy
extends RefCounted

func capacity(
	region: EcologyRegionDefinition,
	species: SpeciesDefinition,
	environment: EcologyEnvironmentPort.Snapshot,
) -> int:
	if region == null or species == null or environment == null:
		return -1
	if region.validate() != OK or species.validate() != OK:
		return -1
	if environment.validate() != OK or environment.region_id != region.region_id:
		return -1
	if not _shares_habitat(region.habitat_tags, species.habitat_tags):
		return 0

	var value: Variant = EcologyMath.checked_multiply(
		region.area_units,
		species.base_capacity_per_area,
	)
	if value == null:
		return -1
	for multiplier: int in [
		region.base_fertility_bp,
		region.water_access_bp,
		environment.fertility_multiplier_bp,
		environment.water_multiplier_bp,
	]:
		value = EcologyMath.multiply_basis_points_floor(int(value), multiplier)
		if value == null:
			return -1
	return int(value)

func _shares_habitat(left: Array[StringName], right: Array[StringName]) -> bool:
	for tag: StringName in left:
		if tag in right:
			return true
	return false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Une espèce incompatible avec l’habitat reçoit une capacité nulle, distincte d’un calcul invalide.

- **Point d’explication complémentaire :** La surface et la capacité de base sont multipliées avec contrôle de dépassement.

- **Point d’explication complémentaire — complément 2 :** Fertilité et eau sont appliquées dans un ordre fixe sous forme de points de base.

- **Invariants protégés — complément 2 :** Chaque étape refuse `null` avant de transmettre sa valeur à l’étape suivante.

- **Limites et réserves :** La politique ne modifie ni la région ni la population.

## 20. Régénérer une ressource

> **[LECTURE] Étape pure — Fonction de `RegionEcologySimulator`.**

```gdscript
func _regenerate_resource(
	pool: ResourcePoolState,
	definition: EcologyResourceDefinition,
	maximum_units: int,
	elapsed_ticks: int,
	ticks_per_day: int,
) -> Error:
	var accrued := EcologyMath.accrue(
		definition.regeneration_units_per_day,
		elapsed_ticks,
		ticks_per_day,
		pool.regeneration_residual,
	)
	if accrued == null:
		return ERR_INVALID_DATA
	var next_value: Variant = EcologyMath.checked_add(
		pool.quantity_units,
		accrued.whole_units,
	)
	if next_value == null:
		return ERR_INVALID_DATA
	pool.quantity_units = mini(int(next_value), maximum_units)
	pool.regeneration_residual = accrued.residual
	pool.revision += 1
	return pool.validate(maximum_units, ticks_per_day)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** La fonction travaille sur une copie candidate reçue en paramètre.

- **Dépendances et ports utilisés :** La régénération est proportionnelle au temps logique écoulé et conserve son résidu.

- **Limites et réserves :** L’addition est contrôlée avant de limiter la quantité par la capacité régionale.

- **Limites et réserves — complément 2 :** La révision change même lorsque la capacité absorbe tout le gain, car une étape a été évaluée.

- **Point d’explication complémentaire :** La validation finale recoupe quantité, capacité, résidu et convention temporelle.

## 21. Consommation et croissance d’une population

> **[LECTURE] Étape pure — Fonction de `RegionEcologySimulator`.**

```gdscript
func _step_population(
	population: PopulationState,
	species: SpeciesDefinition,
	capacity: int,
	food_pool: ResourcePoolState,
	hazard_multiplier_bp: int,
	elapsed_ticks: int,
	ticks_per_day: int,
) -> Error:
	if capacity < 0 or hazard_multiplier_bp < 0 or hazard_multiplier_bp > 50000:
		return ERR_INVALID_PARAMETER

	var shortage := 0
	if species.food_units_per_individual_per_day > 0:
		if food_pool == null:
			return ERR_DOES_NOT_EXIST
		var food_per_day: Variant = EcologyMath.checked_multiply(
			population.count,
			species.food_units_per_individual_per_day,
		)
		if food_per_day == null:
			return ERR_INVALID_DATA
		var food_need := EcologyMath.accrue(
			int(food_per_day),
			elapsed_ticks,
			ticks_per_day,
			food_pool.consumption_residual,
		)
		if food_need == null:
			return ERR_INVALID_DATA
		var consumed := mini(food_pool.quantity_units, food_need.whole_units)
		food_pool.quantity_units -= consumed
		food_pool.consumption_residual = food_need.residual
		food_pool.revision += 1
		shortage = food_need.whole_units - consumed

	var pressure_bp := 0
	if capacity > 0 and population.count < capacity:
		var pressure_product: Variant = EcologyMath.checked_multiply(
			capacity - population.count,
			EcologyMath.BASIS_POINT_SCALE,
		)
		if pressure_product == null:
			return ERR_INVALID_DATA
		pressure_bp = int(pressure_product) / capacity

	var births_per_day: Variant = EcologyMath.multiply_basis_points_floor(
		population.count,
		species.birth_rate_bp_per_day,
	)
	if births_per_day == null:
		return ERR_INVALID_DATA
	births_per_day = EcologyMath.multiply_basis_points_floor(
		int(births_per_day),
		pressure_bp,
	)
	var deaths_per_day: Variant = EcologyMath.multiply_basis_points_floor(
		population.count,
		species.death_rate_bp_per_day,
	)
	if births_per_day == null or deaths_per_day == null:
		return ERR_INVALID_DATA
	deaths_per_day = EcologyMath.multiply_basis_points_floor(
		int(deaths_per_day),
		hazard_multiplier_bp,
	)
	if deaths_per_day == null:
		return ERR_INVALID_DATA
	deaths_per_day = EcologyMath.checked_add(int(deaths_per_day), shortage)
	if deaths_per_day == null:
		return ERR_INVALID_DATA

	var births := EcologyMath.accrue(
		int(births_per_day), elapsed_ticks, ticks_per_day, population.birth_residual
	)
	var deaths := EcologyMath.accrue(
		int(deaths_per_day), elapsed_ticks, ticks_per_day, population.death_residual
	)
	if births == null or deaths == null:
		return ERR_INVALID_DATA
	var after_births: Variant = EcologyMath.checked_add(population.count, births.whole_units)
	if after_births == null:
		return ERR_INVALID_DATA
	var after_deaths: Variant = EcologyMath.checked_add(int(after_births), -deaths.whole_units)
	if after_deaths == null:
		return ERR_INVALID_DATA
	population.count = clampi(int(after_deaths), 0, capacity)
	population.birth_residual = births.residual
	population.death_residual = deaths.residual
	population.revision += 1
	return population.validate(ticks_per_day)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** Une espèce sans consommation déclarée accepte un `food_pool` nul ; une espèce consommatrice exige la réserve identifiée par sa définition.

- **Limites et réserves — complément 2 :** La pénurie est calculée avant les naissances et devient une mortalité entière supplémentaire.

- **Point d’explication complémentaire :** La pression de croissance diminue à l’approche de la capacité et toutes les multiplications passent par `EcologyMath`.

- **Limites et réserves — complément 3 :** Le multiplicateur de danger appartient au contexte environnemental validé, jamais à une sortie générative.

- **Point d’explication complémentaire — complément 2 :** Naissances, décès et valeur finale sont contrôlés avant de mettre à jour les résidus et la révision.

- **Frontières d’autorité :** Cette politique est volontairement pédagogique. Des modèles plus réalistes pourront ajouter classes d’âge, prédation et migration sans modifier l’autorité des autres systèmes.

## 22. Résultat d’une étape écologique

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/domain/ecology_step_result.gd`.**

```gdscript
class_name EcologyStepResult
extends RefCounted

enum Status {
	COMMITTED,
	REJECTED_INVALID_STATE,
	REJECTED_STALE_REVISION,
	REJECTED_CONTEXT,
	REJECTED_BUDGET,
	REJECTED_INTERNAL,
}

var status: Status = Status.REJECTED_INTERNAL
var region_id: StringName
var previous_tick: int = 0
var current_tick: int = 0
var previous_revision: int = 0
var current_revision: int = 0
var changed_population_ids: Array[StringName] = []
var changed_resource_ids: Array[StringName] = []
var message: String = ""

func is_success() -> bool:
	return status == Status.COMMITTED

func validate() -> Error:
	if status < Status.COMMITTED or status > Status.REJECTED_INTERNAL:
		return ERR_INVALID_DATA
	if not StableId.is_valid(region_id):
		return ERR_INVALID_DATA
	if previous_tick < 0 or current_tick < previous_tick:
		return ERR_INVALID_DATA
	if previous_revision < 0 or current_revision < previous_revision:
		return ERR_INVALID_DATA
	if _validate_ids(changed_population_ids) != OK:
		return ERR_INVALID_DATA
	if _validate_ids(changed_resource_ids) != OK:
		return ERR_INVALID_DATA
	return OK

func _validate_ids(ids: Array[StringName]) -> Error:
	var previous := ""
	for stable_id: StringName in ids:
		if not StableId.is_valid(stable_id):
			return ERR_INVALID_DATA
		var current := String(stable_id)
		if not previous.is_empty() and current <= previous:
			return ERR_INVALID_DATA
		previous = current
	return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Le résultat distingue état invalide, révision obsolète, contexte absent, budget et panne interne.

- **Point d’explication complémentaire :** Les ticks et révisions avant/après rendent la transition diagnosticable.

- **Invariants protégés — complément 2 :** Les identifiants modifiés doivent être valides, uniques et déjà triés lexicalement.

- **Persistance et restauration :** Aucun snapshot mutable n’est exposé aux consommateurs.

- **Limites et réserves :** `is_success()` ne traite qu’un remplacement réellement committé comme succès.

## 23. Simuler une région sur des copies

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/region_ecology_simulator.gd`.**

```gdscript
class_name RegionEcologySimulator
extends RefCounted

const MAX_CATCH_UP_TICKS := 1000000

var _catalog: EcologyCatalog
var _environment: EcologyEnvironmentPort
var _capacity_policy := CarryingCapacityPolicy.new()

func prepare_step(
	state: RegionEcologyState,
	current_tick: int,
	ticks_per_day: int,
) -> RegionEcologyState:
	if _catalog == null or _environment == null:
		return null
	if state == null or state.validate(_catalog, ticks_per_day) != OK:
		return null
	if current_tick < state.last_simulated_tick:
		return null
	var elapsed_ticks := current_tick - state.last_simulated_tick
	if elapsed_ticks < 1 or elapsed_ticks > MAX_CATCH_UP_TICKS:
		return null
	var context := _environment.snapshot_for(state.region_id, current_tick)
	if context == null or context.validate() != OK:
		return null
	if context.region_id != state.region_id or current_tick > context.valid_until_tick:
		return null

	var candidate := state.duplicate_detached()
	if _step_resources(candidate, elapsed_ticks, ticks_per_day) != OK:
		return null
	if _step_populations(candidate, context, elapsed_ticks, ticks_per_day) != OK:
		return null
	candidate.last_simulated_tick = current_tick
	candidate.revision += 1
	return candidate if candidate.validate(_catalog, ticks_per_day) == OK else null

func _step_resources(
	candidate: RegionEcologyState,
	elapsed_ticks: int,
	ticks_per_day: int,
) -> Error:
	for resource_id: StringName in _sorted_ids(candidate.resources):
		var definition := _catalog.get_resource(resource_id)
		var pool := candidate.resources[resource_id] as ResourcePoolState
		var maximum := _catalog.maximum_resource_units(candidate.region_id, resource_id)
		if definition == null or pool == null or maximum < 0:
			return ERR_INVALID_DATA
		var code := _regenerate_resource(
			pool, definition, maximum, elapsed_ticks, ticks_per_day
		)
		if code != OK:
			return code
	return OK

func _step_populations(
	candidate: RegionEcologyState,
	context: EcologyEnvironmentPort.Snapshot,
	elapsed_ticks: int,
	ticks_per_day: int,
) -> Error:
	var region := _catalog.get_region(candidate.region_id)
	if region == null:
		return ERR_DOES_NOT_EXIST
	for species_id: StringName in _sorted_ids(candidate.populations):
		var species := _catalog.get_species(species_id)
		var population := candidate.populations[species_id] as PopulationState
		if species == null or population == null:
			return ERR_INVALID_DATA
		var capacity := _capacity_policy.capacity(region, species, context)
		if capacity < 0:
			return ERR_INVALID_DATA
		var food_pool: ResourcePoolState = null
		if species.food_units_per_individual_per_day > 0:
			food_pool = candidate.resources.get(species.food_resource_id) as ResourcePoolState
			if food_pool == null:
				return ERR_DOES_NOT_EXIST
		var code := _step_population(
			population,
			species,
			capacity,
			food_pool,
			context.hazard_multiplier_bp,
			elapsed_ticks,
			ticks_per_day,
		)
		if code != OK:
			return code
	return OK

func _sorted_ids(values: Dictionary) -> Array[StringName]:
	var ids: Array[StringName] = []
	ids.assign(values.keys())
	ids.sort()
	return ids
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Le simulateur refuse une configuration absente, un tick régressif ou un rattrapage excessif.

- **Point d’explication complémentaire :** Les ressources sont traitées dans l’ordre de leurs identifiants avant les populations qui les consomment.

- **Point d’explication complémentaire — complément 2 :** Chaque espèce lit explicitement sa réserve alimentaire et sa capacité d’accueil calculée.

- **Limites et réserves :** L’ordre lexical rend déterministe le partage pédagogique d’une même ressource entre plusieurs populations.

- **Valeur de retour ou code d’échec :** Le tick simulé et la révision changent uniquement sur le candidat, puis l’ensemble est revalidé avant retour.

## 24. Dépôt écologique

> **[LECTURE] Contrat du dépôt — Structure de référence.**

```gdscript
class_name EcologyRepository
extends RefCounted

func get_clock() -> WorldClockState:
	return null

func replace_clock(
	_candidate: WorldClockState,
	_expected_revision: int,
) -> Error:
	return ERR_UNAVAILABLE

func get_region(_region_id: StringName) -> RegionEcologyState:
	return null

func all_region_ids_sorted() -> Array[StringName]:
	return []

func replace_region(
	_candidate: RegionEcologyState,
	_expected_revision: int,
) -> Error:
	return ERR_UNAVAILABLE

func find_command_result(
	_command_id: StringName,
	_fingerprint: String,
) -> EcologyCommandResult:
	return null

func has_conflicting_fingerprint(
	_command_id: StringName,
	_fingerprint: String,
) -> bool:
	return false

func replace_all(_prepared: Dictionary) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Point d’explication complémentaire :** Les lectures renvoient des copies détachées et les identifiants de régions sont triés.

- **Invariants protégés :** `replace_clock()` et `replace_region()` revalident leur révision juste avant remplacement.

- **Résultat attendu et vérification :** Les recherches de commande permettent de rejouer un résultat déjà committé ou de détecter un conflit d’empreinte.

- **Limites et réserves :** Le dépôt ne choisit ni fréquence, ni formule écologique, ni autorisation de récolte.

- **Persistance et restauration :** `replace_all()` est réservé à une restauration complète préparée.

## 25. Modes de simulation

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/ecology_simulation_mode.gd`.**

```gdscript
class_name EcologySimulationMode
extends RefCounted

enum Value {
	ACTIVE,
	BACKGROUND,
	DORMANT,
}

static func interval_ticks(value: Value) -> int:
	match value:
		Value.ACTIVE:
			return 1
		Value.BACKGROUND:
			return 60
		Value.DORMANT:
			return 600
		_:
			return 600
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** `ACTIVE` met à jour une région à chaque tick logique échu.

- **Point d’explication complémentaire :** `BACKGROUND` et `DORMANT` agrègent davantage de temps pour réduire le coût.

- **Point d’explication complémentaire — complément 2 :** Les intervalles sont nominaux et changent de durée réelle si la fréquence physique change.

- **Limites et réserves — complément 2 :** Une région dormante conserve populations, ressources et révisions.

- **Point d’explication complémentaire — complément 3 :** Le mode contrôle le coût de simulation, jamais l’existence métier.

### 25.1 Sélection du mode par un port

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/ecology_region_mode_port.gd`.**

```gdscript
class_name EcologyRegionModePort
extends RefCounted

func mode_for(_region_id: StringName) -> EcologySimulationMode.Value:
	return EcologySimulationMode.Value.DORMANT

func phase_for(_region_id: StringName) -> int:
	return 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** Le port permet à la partition du monde de choisir un mode sans exposer ses scènes ou registres.

- **Limites et réserves :** Le mode par défaut est conservateur et limite le travail lorsqu’aucun adaptateur n’est configuré.

- **Point d’explication complémentaire :** La phase est dérivée de manière stable depuis l’identité régionale afin de répartir les échéances.

- **Limites et réserves — complément 2 :** Une présence de joueur peut influencer l’adaptateur, mais ne remplace jamais l’état écologique.

- **Dépendances et ports utilisés — complément 2 :** Le port ne fait avancer ni l’horloge ni une région.

## 26. Politique d’échéance

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/ecology_tick_policy.gd`.**

```gdscript
class_name EcologyTickPolicy
extends RefCounted

func is_due(
	current_tick: int,
	last_simulated_tick: int,
	mode: EcologySimulationMode.Value,
	phase: int,
) -> bool:
	var interval := EcologySimulationMode.interval_ticks(mode)
	if current_tick < 0 or last_simulated_tick >= current_tick:
		return false
	var normalized_phase := posmod(phase, interval)
	var remainder := posmod(last_simulated_tick + normalized_phase, interval)
	var next_due_tick := last_simulated_tick + interval - remainder
	return current_tick >= next_due_tick
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Point d’explication complémentaire :** La phase répartit les régions sur plusieurs ticks.

- **Point d’explication complémentaire — complément 2 :** `posmod()` conserve un reste positif même si la phase fournie est négative.

- **Limites et réserves :** Une région dépassant son créneau reste due grâce à `>=`.

- **Limites et réserves — complément 2 :** Les créneaux manqués ne sont pas rejoués un par un.

- **Point d’explication complémentaire — complément 3 :** Cette politique reprend le principe du chapitre 17 sans reprendre l’état des agents.

## 27. Ordonnanceur écologique borné

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/ecology_scheduler.gd`.**

```gdscript
class_name EcologyScheduler
extends Node

const MAX_REGIONS_PER_PHYSICS_TICK := 4
const WARNING_BUDGET_USEC := 2500

var _repository: EcologyRepository
var _simulator: RegionEcologySimulator
var _mode_port: EcologyRegionModePort
var _tick_policy := EcologyTickPolicy.new()
var _cursor: int = 0

func process_tick(clock: WorldClockState) -> Array[EcologyStepResult]:
	var results: Array[EcologyStepResult] = []
	if clock == null or clock.validate() != OK:
		return results
	if _repository == null or _simulator == null or _mode_port == null:
		return results
	var ids := _repository.all_region_ids_sorted()
	if ids.is_empty():
		_cursor = 0
		return results

	var started_usec := Time.get_ticks_usec()
	var visited := 0
	var processed := 0
	while visited < ids.size() and processed < MAX_REGIONS_PER_PHYSICS_TICK:
		var index := (_cursor + visited) % ids.size()
		var region_id := ids[index]
		var source := _repository.get_region(region_id)
		visited += 1
		if source == null:
			continue
		var mode := _mode_port.mode_for(region_id)
		var phase := _mode_port.phase_for(region_id)
		if not _tick_policy.is_due(
			clock.logical_tick, source.last_simulated_tick, mode, phase
		):
			continue
		var candidate := _simulator.prepare_step(
			source, clock.logical_tick, clock.ticks_per_day
		)
		results.append(_commit_candidate(source, candidate, clock.logical_tick))
		processed += 1

	_cursor = (_cursor + maxi(visited, 1)) % ids.size()
	var elapsed_usec := Time.get_ticks_usec() - started_usec
	if elapsed_usec > WARNING_BUDGET_USEC:
		push_warning("Ecologie: tick lent: %d µs" % elapsed_usec)
	return results

func _commit_candidate(
	source: RegionEcologyState,
	candidate: RegionEcologyState,
	current_tick: int,
) -> EcologyStepResult:
	if candidate == null:
		return _rejected_result(
			EcologyStepResult.Status.REJECTED_CONTEXT,
			source,
			current_tick,
			"candidat indisponible",
		)
	var result := _committed_result(source, candidate)
	if result.validate() != OK:
		return _rejected_result(
			EcologyStepResult.Status.REJECTED_INTERNAL,
			source,
			current_tick,
			"résultat candidat invalide",
		)
	var code := _repository.replace_region(candidate, source.revision)
	if code == ERR_BUSY:
		return _rejected_result(
			EcologyStepResult.Status.REJECTED_STALE_REVISION,
			source,
			current_tick,
			"révision obsolète",
		)
	if code != OK:
		return _rejected_result(
			EcologyStepResult.Status.REJECTED_INTERNAL,
			source,
			current_tick,
			error_string(code),
		)
	return result

func _committed_result(
	source: RegionEcologyState,
	candidate: RegionEcologyState,
) -> EcologyStepResult:
	var result := EcologyStepResult.new()
	result.status = EcologyStepResult.Status.COMMITTED
	result.region_id = source.region_id
	result.previous_tick = source.last_simulated_tick
	result.current_tick = candidate.last_simulated_tick
	result.previous_revision = source.revision
	result.current_revision = candidate.revision
	result.changed_population_ids = _changed_population_ids(source, candidate)
	result.changed_resource_ids = _changed_resource_ids(source, candidate)
	result.message = "étape écologique committée"
	return result

func _rejected_result(
	status: EcologyStepResult.Status,
	source: RegionEcologyState,
	current_tick: int,
	message: String,
) -> EcologyStepResult:
	var result := EcologyStepResult.new()
	result.status = status
	result.region_id = source.region_id
	result.previous_tick = source.last_simulated_tick
	result.current_tick = maxi(current_tick, source.last_simulated_tick)
	result.previous_revision = source.revision
	result.current_revision = source.revision
	result.message = message
	return result

func _changed_population_ids(
	source: RegionEcologyState,
	candidate: RegionEcologyState,
) -> Array[StringName]:
	var ids: Array[StringName] = []
	for species_id: StringName in candidate.populations:
		var before := source.populations.get(species_id) as PopulationState
		var after := candidate.populations[species_id] as PopulationState
		if before == null or before.revision != after.revision:
			ids.append(species_id)
	ids.sort()
	return ids

func _changed_resource_ids(
	source: RegionEcologyState,
	candidate: RegionEcologyState,
) -> Array[StringName]:
	var ids: Array[StringName] = []
	for resource_id: StringName in candidate.resources:
		var before := source.resources.get(resource_id) as ResourcePoolState
		var after := candidate.resources[resource_id] as ResourcePoolState
		if before == null or before.revision != after.revision:
			ids.append(resource_id)
	ids.sort()
	return ids
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Point d’explication complémentaire :** L’ordonnanceur parcourt des identifiants triés avec un curseur round-robin et un nombre maximal de régions par tick.

- **Limites et réserves :** `Time.get_ticks_usec()` mesure seulement le coût matériel ; il ne fait jamais avancer le monde.

- **Résultat attendu et vérification :** Le résultat committé est construit et validé avant le remplacement autoritaire.

- **Invariants protégés :** `ERR_BUSY` devient un refus de révision distinct d’une panne interne, et aucun événement n’est émis ici avant le commit.

- **Point d’explication complémentaire — complément 2 :** Les listes de populations et ressources modifiées sont calculées depuis leurs révisions puis triées pour rester reproductibles.

## 28. Rattrapage après une longue absence

Un chargement ne doit pas rejouer chaque tick depuis la sauvegarde. Le système calcule `elapsed_ticks`, applique une étape agrégée et limite le rattrapage maximal.

> **[LECTURE] Politique de rattrapage — Ne pas saisir.**

```text
saved_tick = 12 000
current_tick = 48 000
elapsed_ticks = 36 000

interdit :
- appeler 36 000 fois le simulateur ;
- instancier des scènes intermédiaires ;
- rejouer chaque animation ou apparition.

autorisé :
- une étape agrégée bornée ;
- calculs entiers avec résidus ;
- un résumé d’événements committés ;
- matérialisation depuis l’état final.
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** Le rattrapage porte sur l’état logique, jamais sur la présentation.

- **Limites et réserves :** Les résidus rendent les taux faibles cumulables sur une longue période.

- **Point d’explication complémentaire :** Les bornes protègent le temps CPU et les dépassements entiers.

- **Invariants protégés :** Un rattrapage supérieur à la politique autorisée produit un refus ou une stratégie de découpage explicitement bornée.

- **Point d’explication complémentaire — complément 2 :** L’état final devient la seule base de matérialisation.

- **Limites et réserves — complément 2 :** Le guide ne simule pas automatiquement le temps réel écoulé lorsque l’application était fermée. Une fonctionnalité d’« évolution hors connexion » exigerait une politique explicite, une horloge système non autoritaire et des bornes de sécurité supplémentaires.

## 29. Population logique et représentation en scène

Une population de `120` cervidés peut n’avoir que `8` acteurs visibles. Ces huit acteurs sont une projection de la population, pas une liste exhaustive.

> **[LECTURE] Séparation existence / représentation — Ne pas saisir.**

```text
PopulationState.count = 120

représentations actives : 8 CharacterId
représentations arrière-plan : 0 nœud
individus non matérialisés : 112

apparition d’un acteur : count reste 120
disparition de la scène : count reste 120
naissance écologique : count devient 121
mort validée : count devient 119 ou 120 selon les autres transitions
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** Une apparition ne crée pas un individu logique.

- **Limites et réserves — complément 2 :** Une dématérialisation ne constitue ni une mort ni une migration.

- **Point d’explication complémentaire :** Les personnages possèdent les identités matérialisées.

- **Point d’explication complémentaire — complément 2 :** L’écologie possède le nombre agrégé et les transitions de population.

- **Limites et réserves — complément 3 :** Une mort de combat devient une commande causale consommée une seule fois par l’écologie.

## 30. Port de matérialisation

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/ecology_materialization_port.gd`.**

```gdscript
class_name EcologyMaterializationPort
extends RefCounted

class Request:
	extends RefCounted

	var region_id: StringName
	var species_id: StringName
	var desired_visible_count: int = 0
	var region_revision: int = 0

	func validate() -> Error:
		if not StableId.is_valid(region_id) or not StableId.is_valid(species_id):
			return ERR_INVALID_DATA
		if desired_visible_count < 0 or desired_visible_count > 512:
			return ERR_INVALID_DATA
		return OK if region_revision >= 0 else ERR_INVALID_DATA

class PreparedMaterialization:
	extends RefCounted

	var authority_id: StringName = &"characters"
	var payload: Dictionary = {}

	func validate() -> Error:
		if authority_id != &"characters":
			return ERR_INVALID_DATA
		return OK if not payload.is_empty() else ERR_INVALID_DATA

func prepare(_request: Request) -> PreparedMaterialization:
	return null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** La demande exprime une densité visible souhaitée, pas une liste d’identités imposée.

- **Invariants protégés :** L’adaptateur des personnages choisit ou crée les représentations selon ses invariants.

- **Point d’explication complémentaire :** Le payload opaque n’est pas construit par l’écologie ni par l’interface.

- **Limites et réserves — complément 2 :** La révision régionale empêche d’appliquer une projection devenue obsolète.

- **Point d’explication complémentaire — complément 2 :** La matérialisation peut échouer sans annuler l’existence logique de la population.

## 31. Modifier une population par commande causale

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/domain/population_delta_command.gd`.**

```gdscript
class_name PopulationDeltaCommand
extends RefCounted

var command_id: StringName
var region_id: StringName
var species_id: StringName
var delta_count: int = 0
var expected_region_revision: int = 0
var expected_population_revision: int = 0
var cause_id: StringName
var source_system_id: StringName
var logical_tick: int = 0
var command_fingerprint: String = ""

func validate() -> Error:
	if not StableId.is_valid(command_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(region_id) or not StableId.is_valid(species_id):
		return ERR_INVALID_DATA
	if delta_count == 0 or delta_count < -1000000 or delta_count > 1000000:
		return ERR_INVALID_DATA
	if expected_region_revision < 0 or expected_population_revision < 0:
		return ERR_INVALID_DATA
	if not StableId.is_valid(cause_id) or not StableId.is_valid(source_system_id):
		return ERR_INVALID_DATA
	if logical_tick < 0 or command_fingerprint.is_empty():
		return ERR_INVALID_DATA
	if command_fingerprint.length() > 128:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Point d’explication complémentaire :** La commande sert aux naissances scénarisées, morts validées ou ajustements explicitement autorisés.

- **Limites et réserves :** Une cause et un système source rendent le changement traçable.

- **Point d’explication complémentaire — complément 2 :** Les deux révisions protègent la région et la population ciblée.

- **Point d’explication complémentaire — complément 3 :** L’empreinte bornée permet un traitement idempotent.

- **Dépendances et ports utilisés :** La commande ne transporte ni nœud, ni prix, ni objet d’inventaire.

### 31.1 Résultat d’une commande écologique

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/domain/ecology_command_result.gd`.**

```gdscript
class_name EcologyCommandResult
extends RefCounted

enum Status {
	COMMITTED,
	REPLAYED,
	REJECTED_INVALID_COMMAND,
	REJECTED_NOT_FOUND,
	REJECTED_UNAUTHORIZED,
	REJECTED_STALE_REVISION,
	REJECTED_INSUFFICIENT_RESOURCE,
	REJECTED_INVENTORY,
	REJECTED_IDEMPOTENCY_CONFLICT,
	REJECTED_INTERNAL,
}

var status: Status = Status.REJECTED_INTERNAL
var command_id: StringName
var region_id: StringName
var affected_units: int = 0
var message: String = ""

func is_success() -> bool:
	return status in [Status.COMMITTED, Status.REPLAYED]

func validate() -> Error:
	if status < Status.COMMITTED or status > Status.REJECTED_INTERNAL:
		return ERR_INVALID_DATA
	if is_success():
		if not StableId.is_valid(command_id) or not StableId.is_valid(region_id):
			return ERR_INVALID_DATA
	else:
		if not command_id.is_empty() and not StableId.is_valid(command_id):
			return ERR_INVALID_DATA
		if not region_id.is_empty() and not StableId.is_valid(region_id):
			return ERR_INVALID_DATA
	if affected_units < -1000000 or affected_units > 1000000:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** `REPLAYED` confirme qu’une commande identique était déjà committée sans seconde mutation.

- **Invariants protégés :** Les refus d’accès, de révision, de ressource et d’inventaire restent distincts.

- **Limites et réserves — complément 2 :** `affected_units` est signé pour une population et positif pour une récolte.

- **Résultat attendu et vérification :** Le résultat ne contient aucun état régional mutable.

- **Invariants protégés — complément 2 :** Un succès exige des identifiants valides ; seuls les refus antérieurs à une lecture sûre peuvent les laisser vides.

### 31.2 Autoriser sans muter

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/ecology_access_port.gd`.**

```gdscript
class_name EcologyAccessPort
extends RefCounted

func can_change_population(
	_command: PopulationDeltaCommand,
	_region: RegionEcologyState,
	_population: PopulationState,
) -> Error:
	return ERR_UNAVAILABLE

func can_harvest(
	_command: HarvestEcologyCommand,
	_region: RegionEcologyState,
	_pool: ResourcePoolState,
) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** Le port vérifie que l’acteur ou le système source peut demander l’opération.

- **Limites et réserves :** Il ne modifie ni population, ni réserve, ni inventaire.

- **Point d’explication complémentaire :** Les lois, permissions et territoires futurs pourront adapter cette frontière au chapitre 23.

- **Invariants protégés :** L’écologie revalide encore identités, quantités et révisions après l’autorisation.

- **Invariants protégés — complément 2 :** `ERR_UNAUTHORIZED` devient un refus métier ; les autres codes inattendus restent des pannes internes.

## 32. Frontière de récolte avec l’inventaire

Une récolte diminue une réserve écologique et crée éventuellement un lot d’inventaire. Ces deux effets doivent être préparés puis committés ensemble.

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/domain/harvest_ecology_command.gd`.**

```gdscript
class_name HarvestEcologyCommand
extends RefCounted

var command_id: StringName
var region_id: StringName
var resource_id: StringName
var requested_units: int = 0
var actor_character_id: StringName
var destination_container_id: StringName
var created_stack_id: StringName
var expected_region_revision: int = 0
var expected_resource_revision: int = 0
var expected_destination_revision: int = 0
var cause_id: StringName
var source_system_id: StringName
var logical_tick: int = 0
var command_fingerprint: String = ""

func validate() -> Error:
	if not StableId.is_valid(command_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(region_id) or not StableId.is_valid(resource_id):
		return ERR_INVALID_DATA
	if requested_units < 1 or requested_units > 1000000:
		return ERR_INVALID_DATA
	if not actor_character_id.is_empty() and not CharacterId.is_valid(actor_character_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(destination_container_id):
		return ERR_INVALID_DATA
	if not created_stack_id.is_empty() and not StableId.is_valid(created_stack_id):
		return ERR_INVALID_DATA
	if expected_region_revision < 0 or expected_resource_revision < 0:
		return ERR_INVALID_DATA
	if expected_destination_revision < 0:
		return ERR_INVALID_DATA
	if not StableId.is_valid(cause_id) or not StableId.is_valid(source_system_id):
		return ERR_INVALID_DATA
	if logical_tick < 0 or command_fingerprint.is_empty():
		return ERR_INVALID_DATA
	if command_fingerprint.length() > 128:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** La commande demande une quantité écologique et une destination d’inventaire.

- **Limites et réserves — complément 2 :** L’acteur est optionnel pour une cause système, mais validé lorsqu’il est présent.

- **Point d’explication complémentaire :** `created_stack_id` sert uniquement lorsque l’inventaire doit créer un nouveau lot.

- **Point d’explication complémentaire — complément 2 :** Les révisions couvrent la région, la réserve et la destination d’inventaire.

- **Point d’explication complémentaire — complément 3 :** Le service recalculera le rendement autorisé depuis les définitions.

## 33. Ports de rendement et de commit

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/ecology_inventory_yield_port.gd`.**

```gdscript
class_name EcologyInventoryYieldPort
extends RefCounted

class PreparedYield:
	extends RefCounted

	var authority_id: StringName = &"inventory"
	var payload: Dictionary = {}

	func validate() -> Error:
		if authority_id != &"inventory":
			return ERR_INVALID_DATA
		return OK if not payload.is_empty() else ERR_INVALID_DATA

func prepare_harvest_yield(
	_command: HarvestEcologyCommand,
	_item_definition_id: StringName,
	_quantity: int,
) -> PreparedYield:
	return null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Point d’explication complémentaire :** L’inventaire prépare lui-même l’objet, le lot, la provenance et la destination.

- **Limites et réserves :** L’écologie fournit seulement une définition d’objet validée et une quantité autorisée.

- **Frontières d’autorité :** Un payload vide ou une mauvaise autorité est refusé.

- **Dépendances et ports utilisés :** Le port ne modifie ni réserve ni conteneur.

- **Limites et réserves — complément 2 :** Une ressource sans rendement d’inventaire ne peut pas passer par la commande de récolte présentée ici.

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/ecology_transaction_commit_port.gd`.**

```gdscript
class_name EcologyTransactionCommitPort
extends RefCounted

func commit_population(
	_region_candidate: RegionEcologyState,
	_expected_region_revision: int,
	_result: EcologyCommandResult,
	_command_id: StringName,
	_command_fingerprint: String,
) -> Error:
	return ERR_UNAVAILABLE

func commit_harvest(
	_region_candidate: RegionEcologyState,
	_expected_region_revision: int,
	_inventory_candidate: EcologyInventoryYieldPort.PreparedYield,
	_result: EcologyCommandResult,
	_command_id: StringName,
	_command_fingerprint: String,
) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** Le point de composition coordonne les dépôts propriétaires et l’enregistrement idempotent du résultat.

- **Résultat attendu et vérification :** Une mutation de population committe région, identité, empreinte et résultat comme un même lot.

- **Limites et réserves :** Une récolte ajoute le candidat opaque de l’inventaire sans donner ses règles à l’écologie.

- **Limites et réserves — complément 2 :** Les révisions sont relues avant le premier remplacement et un échec ne laisse aucun état partiel observable.

- **Point d’explication complémentaire :** L’atomicité runtime devra être exécutée au chapitre 27.

### 33.1 Service de mutations écologiques

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/ecology_service.gd`.**

```gdscript
class_name EcologyService
extends RefCounted

signal population_delta_committed(result: EcologyCommandResult)
signal harvest_committed(result: EcologyCommandResult)

var _catalog: EcologyCatalog
var _repository: EcologyRepository
var _access: EcologyAccessPort
var _inventory: EcologyInventoryYieldPort
var _commit_port: EcologyTransactionCommitPort

func apply_population_delta(command: PopulationDeltaCommand) -> EcologyCommandResult:
	if command == null or command.validate() != OK:
		return _result(EcologyCommandResult.Status.REJECTED_INVALID_COMMAND, null, 0)
	if not _is_configured(false):
		return _result(EcologyCommandResult.Status.REJECTED_INTERNAL, command, 0)
	var replay := _find_replay(command.command_id, command.command_fingerprint)
	if replay != null:
		return replay
	if _repository.has_conflicting_fingerprint(
		command.command_id, command.command_fingerprint
	):
		return _result(EcologyCommandResult.Status.REJECTED_IDEMPOTENCY_CONFLICT, command, 0)

	var source := _repository.get_region(command.region_id)
	if source == null:
		return _result(EcologyCommandResult.Status.REJECTED_NOT_FOUND, command, 0)
	var population := source.populations.get(command.species_id) as PopulationState
	if population == null:
		return _result(EcologyCommandResult.Status.REJECTED_NOT_FOUND, command, 0)
	if source.revision != command.expected_region_revision:
		return _result(EcologyCommandResult.Status.REJECTED_STALE_REVISION, command, 0)
	if population.revision != command.expected_population_revision:
		return _result(EcologyCommandResult.Status.REJECTED_STALE_REVISION, command, 0)
	var access_code := _access.can_change_population(command, source, population)
	if access_code == ERR_UNAUTHORIZED:
		return _result(EcologyCommandResult.Status.REJECTED_UNAUTHORIZED, command, 0)
	if access_code != OK:
		return _result(EcologyCommandResult.Status.REJECTED_INTERNAL, command, 0)

	var candidate := source.duplicate_detached()
	var candidate_population := candidate.populations[command.species_id] as PopulationState
	var next_count: Variant = EcologyMath.checked_add(
		candidate_population.count, command.delta_count
	)
	if next_count == null or int(next_count) < 0 or int(next_count) > 1000000000:
		return _result(EcologyCommandResult.Status.REJECTED_INVALID_COMMAND, command, 0)
	candidate_population.count = int(next_count)
	candidate_population.revision += 1
	candidate.revision += 1
	if not _candidate_is_valid(candidate):
		return _result(EcologyCommandResult.Status.REJECTED_INTERNAL, command, 0)
	var result := _result(
		EcologyCommandResult.Status.COMMITTED, command, command.delta_count
	)
	var code := _commit_port.commit_population(
		candidate,
		command.expected_region_revision,
		result,
		command.command_id,
		command.command_fingerprint,
	)
	if code != OK:
		return _commit_failure(command, code)
	population_delta_committed.emit(result)
	return result

func harvest(command: HarvestEcologyCommand) -> EcologyCommandResult:
	if command == null or command.validate() != OK:
		return _result(EcologyCommandResult.Status.REJECTED_INVALID_COMMAND, null, 0)
	if not _is_configured(true):
		return _result(EcologyCommandResult.Status.REJECTED_INTERNAL, command, 0)
	var replay := _find_replay(command.command_id, command.command_fingerprint)
	if replay != null:
		return replay
	if _repository.has_conflicting_fingerprint(
		command.command_id, command.command_fingerprint
	):
		return _result(EcologyCommandResult.Status.REJECTED_IDEMPOTENCY_CONFLICT, command, 0)

	var source := _repository.get_region(command.region_id)
	if source == null:
		return _result(EcologyCommandResult.Status.REJECTED_NOT_FOUND, command, 0)
	var pool := source.resources.get(command.resource_id) as ResourcePoolState
	var definition := _catalog.get_resource(command.resource_id)
	if pool == null or definition == null:
		return _result(EcologyCommandResult.Status.REJECTED_NOT_FOUND, command, 0)
	if definition.inventory_item_definition_id.is_empty():
		return _result(EcologyCommandResult.Status.REJECTED_INVENTORY, command, 0)
	if source.revision != command.expected_region_revision:
		return _result(EcologyCommandResult.Status.REJECTED_STALE_REVISION, command, 0)
	if pool.revision != command.expected_resource_revision:
		return _result(EcologyCommandResult.Status.REJECTED_STALE_REVISION, command, 0)
	if pool.quantity_units < command.requested_units:
		return _result(EcologyCommandResult.Status.REJECTED_INSUFFICIENT_RESOURCE, command, 0)
	var access_code := _access.can_harvest(command, source, pool)
	if access_code == ERR_UNAUTHORIZED:
		return _result(EcologyCommandResult.Status.REJECTED_UNAUTHORIZED, command, 0)
	if access_code != OK:
		return _result(EcologyCommandResult.Status.REJECTED_INTERNAL, command, 0)

	var candidate := source.duplicate_detached()
	var candidate_pool := candidate.resources[command.resource_id] as ResourcePoolState
	candidate_pool.quantity_units -= command.requested_units
	candidate_pool.revision += 1
	candidate.revision += 1
	if not _candidate_is_valid(candidate):
		return _result(EcologyCommandResult.Status.REJECTED_INTERNAL, command, 0)
	var inventory_candidate := _inventory.prepare_harvest_yield(
		command,
		definition.inventory_item_definition_id,
		command.requested_units,
	)
	if inventory_candidate == null or inventory_candidate.validate() != OK:
		return _result(EcologyCommandResult.Status.REJECTED_INVENTORY, command, 0)
	var result := _result(
		EcologyCommandResult.Status.COMMITTED, command, command.requested_units
	)
	var code := _commit_port.commit_harvest(
		candidate,
		command.expected_region_revision,
		inventory_candidate,
		result,
		command.command_id,
		command.command_fingerprint,
	)
	if code != OK:
		return _commit_failure(command, code)
	harvest_committed.emit(result)
	return result
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Résultat attendu et vérification :** La configuration est vérifiée avant la lecture du registre d’idempotence.

- **Invariants protégés :** Un retry identique renvoie `REPLAYED`, tandis qu’une même identité associée à une autre empreinte est refusée.

- **Limites et réserves :** Les révisions de région et d’agrégat sont relues avant de préparer une copie candidate.

- **Point d’explication complémentaire :** La récolte prépare le rendement d’inventaire seulement après validation de la réserve candidate.

- **Résultat attendu et vérification — complément 2 :** Les signaux sont émis uniquement après le commit qui enregistre aussi le résultat durable.

### 33.2 Helpers du service

> **[LECTURE] Helpers internes — Suite de `ecology_service.gd`.**

```gdscript
func _find_replay(command_id: StringName, fingerprint: String) -> EcologyCommandResult:
	if _repository == null:
		return null
	var previous := _repository.find_command_result(command_id, fingerprint)
	if previous == null:
		return null
	previous.status = EcologyCommandResult.Status.REPLAYED
	return previous

func _candidate_is_valid(candidate: RegionEcologyState) -> bool:
	if candidate == null or _catalog == null or _repository == null:
		return false
	var clock := _repository.get_clock()
	if clock == null or clock.validate() != OK:
		return false
	return candidate.validate(_catalog, clock.ticks_per_day) == OK

func _is_configured(require_inventory: bool) -> bool:
	var ready := (
		_catalog != null
		and _repository != null
		and _access != null
		and _commit_port != null
	)
	return ready and (not require_inventory or _inventory != null)

func _result(
	status: EcologyCommandResult.Status,
	command: Variant,
	affected_units: int,
) -> EcologyCommandResult:
	var result := EcologyCommandResult.new()
	result.status = status
	result.affected_units = affected_units
	if command != null:
		result.command_id = command.command_id
		result.region_id = command.region_id
	result.message = EcologyCommandResult.Status.keys()[status]
	return result

func _commit_failure(command: Variant, code: Error) -> EcologyCommandResult:
	var status := EcologyCommandResult.Status.REJECTED_INTERNAL
	if code == ERR_BUSY:
		status = EcologyCommandResult.Status.REJECTED_STALE_REVISION
	elif code == ERR_UNAUTHORIZED:
		status = EcologyCommandResult.Status.REJECTED_UNAUTHORIZED
	return _result(status, command, 0)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Résultat attendu et vérification :** Le dépôt garantit que le résultat relu est une copie validée ; le service change seulement son statut d’affichage en `REPLAYED`.

- **Persistance et restauration :** `_candidate_is_valid()` relit l’horloge afin d’appliquer la convention temporelle persistée aux résidus.

- **Limites et réserves :** `_is_configured()` exige l’inventaire seulement pour une récolte.

- **Paramètres et types importants :** `_result()` accepte les deux types de commandes sans exposer leurs états mutables.

- **Limites et réserves — complément 2 :** Les codes `ERR_BUSY` et `ERR_UNAUTHORIZED` restent distingués d’une panne interne.

## 34. Publier des indices à l’économie

L’écologie ne calcule pas un prix. Elle peut produire un signal borné décrivant l’état d’une ressource dans une région.

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/ecology_market_signal_port.gd`.**

```gdscript
class_name EcologyMarketSignalPort
extends RefCounted

class SignalSnapshot:
	extends RefCounted

	var region_id: StringName
	var resource_id: StringName
	var scarcity_bp: int = 0
	var abundance_bp: int = 0
	var region_revision: int = 0
	var valid_until_tick: int = 0

	func validate() -> Error:
		if not StableId.is_valid(region_id) or not StableId.is_valid(resource_id):
			return ERR_INVALID_DATA
		if scarcity_bp < 0 or scarcity_bp > 10000:
			return ERR_INVALID_DATA
		if abundance_bp < 0 or abundance_bp > 10000:
			return ERR_INVALID_DATA
		if scarcity_bp + abundance_bp > 10000:
			return ERR_INVALID_DATA
		if region_revision < 0 or valid_until_tick < 0:
			return ERR_INVALID_DATA
		return OK

func snapshot_for(
	_region_id: StringName,
	_resource_id: StringName,
	_logical_tick: int,
) -> SignalSnapshot:
	return null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** Le signal transporte des indices et une révision, jamais un prix unitaire.

- **Limites et réserves :** Rareté et abondance sont bornées et ne peuvent pas dépasser ensemble `100 %`.

- **Point d’explication complémentaire :** L’économie décide comment intégrer ce contexte à sa politique de prix du chapitre 21.

- **Invariants protégés :** Un signal expiré est refusé au moment du devis.

- **Dépendances et ports utilisés — complément 2 :** L’écologie ne lit ni portefeuille ni offre commerciale.

## 35. Fournir des observations aux agents

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/application/ecology_agent_observation_port.gd`.**

```gdscript
class_name EcologyAgentObservationPort
extends RefCounted

class Observation:
	extends RefCounted

	var region_id: StringName
	var region_revision: int = 0
	var logical_tick: int = 0
	var population_counts: Dictionary[StringName, int] = {}
	var resource_levels_bp: Dictionary[StringName, int] = {}

	func validate() -> Error:
		if not StableId.is_valid(region_id):
			return ERR_INVALID_DATA
		if region_revision < 0 or logical_tick < 0:
			return ERR_INVALID_DATA
		if population_counts.size() > 128 or resource_levels_bp.size() > 128:
			return ERR_OUT_OF_MEMORY
		for species_id: StringName in population_counts:
			if not StableId.is_valid(species_id) or population_counts[species_id] < 0:
				return ERR_INVALID_DATA
		for resource_id: StringName in resource_levels_bp:
			var value: int = resource_levels_bp[resource_id]
			if not StableId.is_valid(resource_id) or value < 0 or value > 10000:
				return ERR_INVALID_DATA
		return OK

func snapshot_for(_region_id: StringName, _logical_tick: int) -> Observation:
	return null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Point d’explication complémentaire :** L’observation contient des valeurs simples, bornées et indexées par identifiants stables.

- **Point d’explication complémentaire — complément 2 :** Les agents transforment ces données en faits structurés selon le chapitre 17.

- **Frontières d’autorité :** Une décision d’agent reste une requête soumise au système propriétaire.

- **Valeur de retour ou code d’échec :** Le port ne retourne aucun dictionnaire interne du dépôt écologique.

- **Persistance et restauration :** Une sortie générative ne peut pas remplacer ce snapshot validé.

## 36. Événements et causalité

Les événements écologiques sont émis après commit et portent :

- un identifiant stable ;
- la région ;
- le tick logique ;
- la révision committée ;
- la cause et le système source lorsqu’ils proviennent d’une commande ;
- les deltas agrégés ;
- aucune référence de scène.

> **[LECTURE] Exemple d’événement committé — Structure de référence.**

```gdscript
class_name EcologyPopulationChangedEvent
extends RefCounted

var event_id: StringName
var region_id: StringName
var species_id: StringName
var previous_count: int = 0
var current_count: int = 0
var logical_tick: int = 0
var region_revision: int = 0
var cause_id: StringName
var source_system_id: StringName
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Point d’explication complémentaire :** L’événement décrit un fait déjà committé.

- **Persistance et restauration :** Les valeurs avant/après permettent un diagnostic sans relire un ancien snapshot.

- **Limites et réserves :** Cause et système source distinguent une transition naturelle d’une commande externe.

- **Limites et réserves — complément 2 :** Les consommateurs ne peuvent pas modifier la région à travers l’événement.

- **Limites et réserves — complément 3 :** Une présentation ou un agent peut ignorer un événement devenu ancien grâce à la révision.

## 37. Présentation et interaction

L’interface peut afficher :

- le jour logique et la phase du cycle ;
- la région active ;
- une estimation de population ;
- le niveau d’une ressource ;
- la tendance récente ;
- la rareté structurée ;
- le dernier tick simulé ;
- un avertissement de rattrapage borné.

Elle ne doit pas :

- avancer directement l’horloge ;
- écrire dans une population ou une réserve ;
- créer des acteurs pour augmenter un compteur ;
- calculer un prix depuis une rareté ;
- considérer un nœud absent comme un individu mort ;
- appliquer une récolte avant le commit multi-autorités.

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/presentation/ecology_presentation_bridge.gd`.**

```gdscript
class_name EcologyPresentationBridge
extends Node

signal region_feedback_requested(region_id: StringName, logical_tick: int)

var _latest_revision: Dictionary[StringName, int] = {}

func on_step_committed(result: EcologyStepResult) -> void:
	if result == null or result.validate() != OK or not result.is_success():
		return
	var known_revision: int = int(_latest_revision.get(result.region_id, -1))
	if result.current_revision <= known_revision:
		return
	_latest_revision[result.region_id] = result.current_revision
	region_feedback_requested.emit(result.region_id, result.current_tick)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Résultat attendu et vérification :** Le pont accepte uniquement un résultat validé et committé.

- **Limites et réserves :** La révision empêche de rejouer une présentation plus ancienne.

- **Frontières d’autorité :** Le cache local ne remplace pas l’autorité du dépôt.

- **Dépendances et ports utilisés :** Le signal transporte des identifiants et entiers simples.

- **Limites et réserves — complément 2 :** Aucun état écologique n’est modifié dans le nœud.

## 38. Persistance

Sont persistés :

- l’horloge logique, sa révision et `ticks_per_day` ;
- les régions vivantes et leur dernier tick simulé ;
- les populations, quantités, résidus et révisions ;
- les réserves de ressources, résidus et révisions ;
- les séquences d’événements ;
- les identités, empreintes et résultats récents nécessaires à l’idempotence ;
- la version de format.

Ne sont pas persistés :

- les définitions `.tres` ;
- les capacités d’accueil dérivées ;
- les contextes environnementaux ;
- les modes et phases de planification dérivés ;
- les nœuds matérialisés et listes de personnages actifs ;
- les signaux de marché et observations d’agents ;
- les commandes, candidats et demandes de matérialisation en attente ;
- les caches de présentation ;
- les prix, offres ou portefeuilles ;
- les objets déjà possédés par l’inventaire.

Le parcours Solo borne l’historique d’idempotence dans le snapshot. Le Mode Studio peut archiver des événements écologiques dans SQLite pour le diagnostic, sans faire de cette archive l’autorité du chargement.

## 39. Codec strict

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/infrastructure/ecology_snapshot_codec.gd`.**

```gdscript
class_name EcologySnapshotCodec
extends RefCounted

const FORMAT := "project-asteria-ecology"
const VERSION := 1
const ROOT_KEYS := [
	"format",
	"version",
	"clock",
	"regions",
	"idempotency",
]

class DecodeResult:
	extends RefCounted

	var code: Error = FAILED
	var prepared: Dictionary = {}
	var message: String = ""

	func is_success() -> bool:
		return code == OK

func decode(document: Dictionary, catalog: EcologyCatalog) -> DecodeResult:
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
	var prepared := _decode_all(document, catalog)
	if prepared == null:
		return _failure(ERR_INVALID_DATA, "état écologique invalide")
	if _validate_cross_references(prepared, catalog) != OK:
		return _failure(ERR_INVALID_DATA, "références croisées invalides")
	var result := DecodeResult.new()
	result.code = OK
	result.prepared = prepared
	return result
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Point d’explication complémentaire :** Le codec exige exactement les clés prévues.

- **Point d’explication complémentaire — complément 2 :** Les entiers suivent la règle JSON sûre du chapitre 9.

- **Invariants protégés :** `_decode_all()` décode d’abord l’horloge, puis valide chaque région avec son `ticks_per_day`, sans toucher au dépôt actif.

- **Résultat attendu et vérification :** Les références croisées vérifient espèces, ressources et régions contre le catalogue.

- **Invariants protégés — complément 2 :** `DecodeResult` distingue un document vide valide d’un échec.

## 40. Section de sauvegarde

> **[VSC] Visual Studio Code — Créer : `res://src/features/ecology/infrastructure/ecology_save_section.gd`.**

```gdscript
class_name EcologySaveSection
extends SaveSection

var _repository: EcologyRepository
var _catalog: EcologyCatalog
var _codec := EcologySnapshotCodec.new()
var _prepared: Dictionary = {}
var _is_prepared := false

func section_id() -> StringName:
	return &"ecology"

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

**Explication structurée du bloc :**

- **Point d’explication complémentaire :** La section prépare l’ensemble du monde vivant avant toute mutation.

- **Point d’explication complémentaire — complément 2 :** Les données sont copiées avant stockage et application.

- **Persistance et restauration :** Un échec d’une autre section permet d’annuler la restauration.

- **Point d’explication complémentaire — complément 3 :** L’horloge et les régions sont remplacées dans un même état préparé.

- **Persistance et restauration — complément 2 :** Les définitions doivent être chargées avant le snapshot vivant.

## 41. Scène pédagogique

La scène `ch22_living_world_demo.tscn` doit montrer :

1. une horloge logique et deux régions ;
2. une population et une ressource valides ;
3. une régénération sur plusieurs ticks ;
4. une consommation par population ;
5. une croissance sous la capacité ;
6. une décroissance en cas de pénurie ;
7. une région active et une région dormante ;
8. un rattrapage agrégé ;
9. une apparition de représentation sans changement de population ;
10. une dématérialisation sans décès ;
11. une récolte committée avec l’inventaire ;
12. un signal de rareté transmis à l’économie ;
13. une sauvegarde et restauration de l’horloge, des résidus et des révisions.

## 42. Modes Solo et Studio

### 42.1 Mode Solo

- quelques dizaines de régions ;
- définitions `.tres` locales ;
- simulation déterministe sur le thread principal ;
- quatre régions maximum par tick physique ;
- rattrapage agrégé borné ;
- contexte environnemental simple ;
- journaux récents ;
- matérialisation locale ;
- aucune dépendance à un service IA.

### 42.2 Mode Studio

- catalogues versionnés et revus ;
- scénarios écologiques de référence ;
- tests de propriété sur les bornes et résidus ;
- replays déterministes ;
- télémétrie des temps de simulation ;
- profils de régions ;
- outils de visualisation de populations et ressources ;
- migration de snapshots ;
- simulations massives hors runtime de production ;
- validation des contrats inter-systèmes.

Le Mode Studio renforce les outils et l’observabilité. Il ne crée pas un gestionnaire global capable de modifier directement tous les systèmes.

## 43. Budgets, sécurité et diagnostics

Bornes pédagogiques :

| Élément | Borne |
|---|---:|
| régions écologiques | 4 096 |
| populations par région | 128 |
| ressources par région | 128 |
| régions traitées par tick physique | 4 |
| rattrapage par étape | 1 000 000 ticks |
| représentations visibles par demande | 512 |
| commandes idempotentes récentes | 4 096 |
| événements récents par région | 512 |

Ces bornes devront être mesurées et ajustées au chapitre 27.

Journaliser :

- région, tick précédent et tick courant ;
- mode, phase et intervalle ;
- révisions attendues et constatées ;
- populations et ressources modifiées ;
- quantité récoltée ;
- cause et système source ;
- durée matérielle de l’étape ;
- refus de contexte, budget ou révision ;
- conflit d’idempotence.

Ne pas journaliser les snapshots complets, positions de tous les acteurs, données personnelles inutiles, sorties génératives brutes ou contenu d’inventaire non concerné.

## 44. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 44.1 Utiliser l’heure système comme temps du monde

**Symptôme ou risque :** changer l’horloge du système modifie la simulation ou fait régresser le monde.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var day_index := Time.get_unix_time_from_system() / 86400
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** l’heure système est modifiable et ne constitue pas une séquence logique reproductible.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var day_index := world_clock.logical_tick / world_clock.ticks_per_day
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le jour est dérivé d’un état autoritaire sauvegardé et non décroissant.

### 44.2 Utiliser des `float` pour les populations et ressources

**Symptôme ou risque :** les résultats varient selon l’ordre des calculs et les fractions sont perdues ou arrondies différemment.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
population += population * 0.015
resource_pool += 0.1 * delta
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** aucun contrat d’arrondi ni résidu persistable n’est défini.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var accrued := EcologyMath.accrue(
	units_per_day,
	elapsed_ticks,
	ticks_per_day,
	previous_residual,
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les unités entières et le résidu produisent une évolution déterministe et sérialisable.

### 44.3 Rejouer chaque tick manqué

**Symptôme ou risque :** un chargement après une longue absence bloque la boucle principale.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
for tick in range(saved_tick, current_tick):
	simulate_one_tick(tick)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le coût dépend sans borne de la durée écoulée et rejoue des états intermédiaires inutiles.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var elapsed_ticks := current_tick - saved_tick
var candidate := simulator.prepare_step(state, current_tick, ticks_per_day)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** une étape agrégée bornée calcule directement l’état final utile.

### 44.4 Confondre présence en scène et existence

**Symptôme ou risque :** quitter une zone supprime ses populations ou entrer dans une zone en crée de nouvelles.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
population.count = get_tree().get_nodes_in_group("wolves").size()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le nombre de nœuds actifs devient l’autorité d’une population qui existe hors écran.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var population := ecology_repository.get_region(region_id).populations[species_id]
var visible_count := character_registry.count_visible(region_id, species_id)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le nombre logique et le nombre visible sont lus séparément sans s’écraser.

### 44.5 Modifier la population lors d’une apparition

**Symptôme ou risque :** matérialiser puis dématérialiser plusieurs fois crée ou détruit des individus.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
spawn_character()
population.count += 1
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** l’instanciation d’une représentation est confondue avec une naissance écologique.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var prepared := materialization_port.prepare(request)
apply_character_projection(prepared)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la projection visuelle change sans mutation du nombre logique.

### 44.6 Laisser l’économie écrire une ressource écologique

**Symptôme ou risque :** une variation de prix ou une vente augmente directement une réserve naturelle.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if market_price > threshold:
	ecology_pool.quantity_units += 100
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** l’économie devient propriétaire d’un état écologique et introduit une boucle implicite.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var signal := ecology_market_signal.snapshot_for(
	region_id,
	resource_id,
	logical_tick,
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’économie lit un indice validé sans modifier la réserve source.

### 44.7 Laisser l’écologie fixer un prix

**Symptôme ou risque :** deux autorités calculent des prix incompatibles.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
item_price_minor = scarcity_bp * 50
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** un indice écologique devient directement un montant monétaire.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
pricing_context.supply_multiplier_bp = scarcity_policy.from_signal(signal)
var quote := economy_service.quote(command)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’économie transforme l’indice selon sa propre politique et reste l’unique autorité du prix.

### 44.8 Réduire une réserve avant de créer le rendement d’inventaire

**Symptôme ou risque :** une panne d’inventaire détruit la ressource sans remettre l’objet au récolteur.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
pool.quantity_units -= harvested
inventory.add_item(item_definition_id, harvested)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** les deux autorités sont modifiées séquentiellement et peuvent diverger.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var ecology_candidate := prepare_harvest(command)
var inventory_candidate := inventory_yield_port.prepare_harvest_yield(
	command,
	item_definition_id,
	harvested,
)
var code := transaction_commit_port.commit_harvest(
	ecology_candidate,
	command.expected_region_revision,
	inventory_candidate,
	command.command_id,
	command.command_fingerprint,
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la réserve et le lot sont préparés puis committés comme une seule opération.

### 44.9 Utiliser le RNG global sans état restaurable

**Symptôme ou risque :** deux replays identiques produisent des migrations ou apparitions différentes.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if randf() < migration_probability:
	migrate_population()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le tirage dépend d’un état global non corrélé à la région et non persisté par ce système.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var migration_units := deterministic_migration_policy.compute(
	region_state,
	species_definition,
	elapsed_ticks,
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la politique utilise uniquement l’état, les définitions, le tick et des résidus persistés.

### 44.10 Laisser une sortie IA modifier le monde vivant

**Symptôme ou risque :** un texte génératif crée une famine, une migration ou une ressource persistante sans règle métier.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
region.populations = ai_response["populations"]
region.resources = ai_response["resources"]
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une sortie non fiable remplace directement deux agrégats autoritaires.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var suggestion := ai_gateway.suggest_ecology_event(summary)
var command := ecology_suggestion_policy.to_validated_command(suggestion)
if command != null:
	ecology_service.apply_population_delta(command)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la suggestion est filtrée puis convertie en commande typée qui repasse par les validations et révisions.

## 45. Tests à préparer

### 45.1 Tests unitaires

- identifiants écologiques ;
- horloge non décroissante ;
- calcul du jour et du tick dans le jour ;
- validation des définitions ;
- capacités de ressources ;
- arithmétique bornée et résidus ;
- régénération ;
- consommation ;
- capacité d’accueil ;
- croissance et mortalité ;
- échéances par mode et phases régionales ;
- résultats idempotents ;
- codec strict.

### 45.2 Tests d’intégration

- étape complète d’une région ;
- région active, arrière-plan et dormante ;
- région reportée par le budget puis traitée ;
- rattrapage agrégé ;
- contexte environnemental expiré ;
- révision obsolète ;
- apparition sans changement de population ;
- dématérialisation sans décès ;
- mort de combat consommée une seule fois ;
- conflit d’empreinte et replay d’une commande ;
- récolte atomique avec l’inventaire ;
- signal écologique utilisé par l’économie sans prix direct ;
- observation d’agent ;
- sauvegarde et restauration des résidus.

### 45.3 Simulations

- 1, 64 et 4 096 régions ;
- 1, 32 et 128 populations par région ;
- 1, 32 et 128 ressources par région ;
- 1, 60 et 600 ticks entre étapes ;
- rattrapages de 1 000 à 1 000 000 ticks ;
- pénurie complète puis régénération ;
- population à zéro, sous capacité et à capacité ;
- 10 000 jours simulés avec comparaison de replays ;
- récoltes concurrentes sur la même réserve ;
- matérialisation répétée sans dérive du compteur.

## 46. Réserves runtime

Cette revue statique ne prouve pas :

- le passage de tous les extraits dans le parseur Godot 4.7.1 ;
- le comportement de tous les dictionnaires typés ;
- les contrôles de dépassement aux bornes ;
- l’équilibrage du modèle de croissance ;
- la stabilité des budgets avec 4 096 régions ;
- l’atomicité réelle entre écologie et inventaire ;
- l’adaptateur de matérialisation des personnages ;
- l’intégration d’un contexte météo futur ;
- les actions d’agents ;
- l’instanciation de la scène pédagogique ;
- l’exécution du codec et d’une migration future ;
- la reproductibilité entre plateformes ou versions ;
- la génération d’un PDF intermédiaire.

## 47. Sources techniques

- [Godot 4.7 — `Resource`](https://docs.godotengine.org/en/4.7/classes/class_resource.html)
- [Godot 4.7 — `RefCounted`](https://docs.godotengine.org/en/4.7/classes/class_refcounted.html)
- [Godot 4.7 — `Array`](https://docs.godotengine.org/en/4.7/classes/class_array.html)
- [Godot 4.7 — `Dictionary`](https://docs.godotengine.org/en/4.7/classes/class_dictionary.html)
- [Godot 4.7 — `StringName`](https://docs.godotengine.org/en/4.7/classes/class_stringname.html)
- [Godot 4.7 — `Time`](https://docs.godotengine.org/en/4.7/classes/class_time.html)
- [Godot 4.7 — bases de GDScript et entier 64 bits](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/gdscript_basics.html)
- [Godot 4.7 — génération de nombres aléatoires](https://docs.godotengine.org/en/4.7/tutorials/math/random_number_generation.html)
- [Chapitre 9 — Sauvegardes, chargements et compatibilité](CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md)
- [Chapitre 14 — Personnages](CHAPITRE-14-Personnages.md)
- [Chapitre 17 — Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md)
- [Chapitre 20 — Inventaire et réputation des objets](CHAPITRE-20-Inventaire-et-reputation-des-objets.md)
- [Chapitre 21 — Économie](CHAPITRE-21-Economie.md)

## 48. Synthèse opérationnelle pour Project Asteria

Le monde vivant de `Project Asteria` retient les décisions suivantes :

1. une horloge logique globale ordonne tous les systèmes ;
2. l’heure système et les timers de scène ne sont jamais autoritaires ;
3. les régions sont des unités logiques indépendantes des scènes ;
4. définitions et états vivants restent séparés ;
5. les populations existent sans représentation active ;
6. une apparition ou disparition de scène ne modifie pas le nombre logique ;
7. populations et ressources utilisent des entiers et des résidus persistés ;
8. les capacités d’accueil sont dérivées des régions, espèces et contextes ;
9. les étapes modifient des copies puis remplacent un candidat validé ;
10. les modes actif, arrière-plan et dormant contrôlent le coût, pas l’existence ;
11. un rattrapage utilise une étape agrégée bornée ;
12. les agents reçoivent des observations mais ne modifient pas directement l’écologie ;
13. une récolte coordonne réserve écologique et rendement d’inventaire ;
14. l’écologie publie des indices, jamais des prix ;
15. les commandes causales sont idempotentes et committent leur résultat avec la région ;
16. l’économie, l’inventaire, les personnages et les agents conservent leurs autorités ;
17. une sortie IA ne produit qu’une suggestion filtrée par des commandes validées ;
18. horloge, régions, populations, ressources, résidus, révisions et résultats idempotents sont persistés ;
19. définitions, capacités dérivées, nœuds, contextes, signaux et candidats restent hors du snapshot.
