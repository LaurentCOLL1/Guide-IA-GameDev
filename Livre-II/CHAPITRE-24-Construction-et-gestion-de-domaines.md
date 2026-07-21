---
title: "Livre II — Chapitre 24 : Construction et gestion de domaines"
id: "DOC-L2-CH24"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 24
last-verified: "2026-07-21T09:05:12+02:00"
audit-status: "complete"
audit-date: "2026-07-21T09:05:12+02:00"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-24.md"
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

# Construction et gestion de domaines

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH24`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Niveau de raisonnement conseillé :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-24.md`.

## 1. Rôle du chapitre

Les chapitres précédents savent identifier les personnages, protéger les objets, calculer des coûts, simuler les régions et décider des droits politiques. Il manque encore une autorité capable de représenter un domaine, ses parcelles, ses bâtiments, ses chantiers et ses cycles de production sans confondre ces actifs avec une scène Godot.

Ce chapitre construit le système de **construction et gestion de domaines** de `Project Asteria`. Il définit :

- des domaines et parcelles identifiés indépendamment des scènes ;
- des liens de tenure vers les droits du chapitre 23 ;
- des définitions de bâtiments, recettes de construction et recettes de production ;
- des bâtiments, chantiers et états d’entretien persistants ;
- des livraisons de matériaux préparées par l’inventaire ;
- des coûts préparés par l’économie ;
- des contraintes de site fournies par l’écologie ;
- des permissions d’accès calculées depuis les droits politiques ;
- des commits multi-autorités idempotents ;
- une persistance stricte et une restauration préparée.

Le système doit garantir que :

- une scène ne devient jamais l’autorité d’un bâtiment ;
- le chapitre 24 ne crée ni droit politique, ni monnaie, ni objet, ni ressource écologique ;
- un chantier ne consomme rien avant la préparation complète des candidats ;
- la progression est entière, bornée et fondée sur le tick logique ;
- achever un bâtiment exige tous les matériaux et tous les travaux requis ;
- une production consomme ses intrants et produit ses extrants dans un même lot ;
- une sortie IA ne peut ni attribuer une parcelle, ni achever un chantier, ni produire des objets.

## 2. Prérequis

Le lecteur doit avoir parcouru :

- le chapitre 4 pour l’architecture feature-first ;
- le chapitre 5 pour les services, ports et unités de travail ;
- le chapitre 7 pour les `Resource`, catalogues et identifiants stables ;
- le chapitre 9 pour les snapshots et restaurations préparées ;
- le chapitre 17 pour les agents et demandes validées ;
- le chapitre 20 pour les objets, lots, conteneurs et transferts ;
- le chapitre 21 pour les coûts et transactions économiques ;
- le chapitre 22 pour les régions, ressources et ticks logiques ;
- le chapitre 23 pour les juridictions, droits et autorisations.

## 3. Périmètre et frontières

Ce chapitre couvre :

- les définitions de domaines, parcelles et bâtiments ;
- les liens de tenure et droits d’usage externes ;
- les emplacements logiques ;
- les plans et recettes de construction ;
- les chantiers, matériaux livrés et travail accompli ;
- l’achèvement et l’état d’un bâtiment ;
- la production, l’entretien et l’indisponibilité ;
- les permissions d’accès et d’exploitation ;
- les événements committés ;
- les observations destinées aux agents ;
- la persistance.

Il ne couvre pas :

- la promulgation d’un droit, d’une loi ou d’une sanction ;
- la propriété et les transferts d’objets ;
- les prix, soldes ou écritures comptables ;
- les populations et réserves écologiques ;
- les quêtes, objectifs narratifs ou dialogues ;
- l’édition 3D détaillée des bâtiments ;
- le multijoueur et l’autorité réseau ;
- l’équilibrage final des coûts et durées.

> **Frontière essentielle :** le domaine possède les actifs fonciers, bâtiments, chantiers, production et entretien. La politique possède les droits ; l’inventaire possède les matériaux et produits ; l’économie possède les paiements ; l’écologie possède les régions et ressources ; la narration possède les conséquences scénarisées.

> **[LECTURE] Chaîne d’autorité d’une construction — Ne pas saisir.**

```text
BuildCommand
    ↓ validation, identité et empreinte
DomainConstructionService
    ├── relit domaine, parcelle et révisions
    ├── demande une décision de droit au chapitre 23
    ├── demande un contexte de site au chapitre 22
    ├── prépare matériaux auprès du chapitre 20
    ├── prépare coût éventuel auprès du chapitre 21
    └── construit un candidat de domaine détaché
            ↓
DomainTransactionCommitPort
    ├── revalide toutes les révisions
    ├── committe domaine + inventaire + économie
    └── enregistre identité, empreinte et résultat
            ↓
événements typés après commit
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le service de domaine orchestre sans écrire directement les dépôts propriétaires des autres systèmes.

- La décision politique et le contexte écologique sont des snapshots validés, pas des références de scène.

- Les matériaux et le coût restent candidats jusqu’au commit commun.

- L’identité et l’empreinte rendent le retry idempotent.

- Les événements ne décrivent qu’un état déjà committé.

## 4. Architecture retenue

> **[LECTURE] Arborescence cible — Ne pas créer depuis un terminal.**

```text
res://src/features/domains/
├── domain/
│   ├── domain_id.gd
│   ├── domain_definition.gd
│   ├── parcel_definition.gd
│   ├── building_definition.gd
│   ├── construction_recipe_definition.gd
│   ├── production_recipe_definition.gd
│   ├── domain_tenure_link.gd
│   ├── parcel_state.gd
│   ├── building_state.gd
│   ├── worksite_state.gd
│   ├── domain_state.gd
│   └── domain_command_result.gd
├── application/
│   ├── domain_catalog.gd
│   ├── domain_repository.gd
│   ├── domain_rights_port.gd
│   ├── domain_ecology_port.gd
│   ├── domain_inventory_port.gd
│   ├── domain_economy_port.gd
│   ├── domain_transaction_commit_port.gd
│   ├── domain_access_policy.gd
│   ├── domain_construction_service.gd
│   ├── domain_production_service.gd
│   └── domain_agent_observation_port.gd
├── infrastructure/
│   ├── domain_snapshot_codec.gd
│   └── domain_save_section.gd
└── presentation/
    └── domain_presentation_bridge.gd

res://data/domains/
├── domains/
├── parcels/
├── buildings/
├── construction_recipes/
└── production_recipes/

res://scenes/learning/
├── ch24_domains_demo.tscn
└── ch24_domains_demo.gd
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `domain` contient les données et invariants qui ne dépendent d’aucun nœud.

- `application` coordonne les ports vers politique, écologie, inventaire et économie.

- `infrastructure` sérialise seulement les données durables.

- `presentation` traduit les événements committés en demandes visuelles.

- Les définitions de conception restent séparées des états sauvegardés.

## 5. Vocabulaire

Un **domaine** est un agrégat logique regroupant des parcelles, bâtiments et chantiers sous une même identité de gestion.

Une **parcelle** est un emplacement logique rattaché à une région écologique. Elle n’est ni un `Node3D`, ni un polygone de collision autoritaire.

Un **lien de tenure** référence un droit politique valide : propriété, usage, administration ou exploitation. Il ne crée pas ce droit.

Un **bâtiment** est un actif logique issu d’une définition de conception. Sa représentation 3D est dérivée.

Un **chantier** conserve la recette, les matériaux livrés, le travail accompli et les révisions nécessaires à l’achèvement.

Une **recette de production** décrit des intrants, extrants, travail et contraintes. Elle ne déplace aucun objet par elle-même.

L’**entretien** représente l’état fonctionnel d’un bâtiment. Il ne remplace ni la durabilité d’un objet, ni les dégâts de combat.

## 6. Identifiants stables

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/domain_id.gd`.**

```gdscript
class_name DomainId
extends RefCounted

const DOMAIN_PREFIX := "domain.instance."
const PARCEL_PREFIX := "domain.parcel."
const BUILDING_PREFIX := "domain.building."
const WORKSITE_PREFIX := "domain.worksite."
const COMMAND_PREFIX := "domain.command."

static func domain(uuid_text: String) -> StringName:
    return _from_slug(DOMAIN_PREFIX, uuid_text)

static func parcel(uuid_text: String) -> StringName:
    return _from_slug(PARCEL_PREFIX, uuid_text)

static func building(uuid_text: String) -> StringName:
    return _from_slug(BUILDING_PREFIX, uuid_text)

static func worksite(uuid_text: String) -> StringName:
    return _from_slug(WORKSITE_PREFIX, uuid_text)

static func command(uuid_text: String) -> StringName:
    return _from_slug(COMMAND_PREFIX, uuid_text)

static func _from_slug(prefix: String, value: String) -> StringName:
    var normalized := value.strip_edges().to_lower().replace("-", "_")
    if normalized.is_empty():
        return &""
    for character: String in normalized:
        var allowed := (
            (character >= "a" and character <= "z")
            or (character >= "0" and character <= "9")
            or character == "_"
        )
        if not allowed:
            return &""
    return StringName(prefix + normalized)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Chaque famille possède un espace de noms distinct afin d’éviter les collisions entre domaine, parcelle, bâtiment et chantier.

- Les identifiants ne dépendent ni d’un nom affiché, ni d’un chemin de scène.

- La normalisation accepte uniquement lettres ASCII minuscules, chiffres et soulignement.

- Une entrée invalide renvoie `&""` et doit être refusée par la fabrique appelante.

- Les commandes possèdent leur propre identité pour l’idempotence.

## 7. Définitions de conception

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/domain_definition.gd`.**

```gdscript
class_name DomainDefinition
extends Resource

@export var definition_id: StringName
@export var display_name_key: StringName
@export var maximum_parcels: int = 16
@export var maximum_buildings: int = 64
@export var permitted_region_tags: Array[StringName] = []

func validate() -> Error:
    if not StableId.is_valid(definition_id):
        return ERR_INVALID_DATA
    if not StableId.is_valid(display_name_key):
        return ERR_INVALID_DATA
    if maximum_parcels < 1 or maximum_parcels > 4096:
        return ERR_INVALID_DATA
    if maximum_buildings < 0 or maximum_buildings > 16384:
        return ERR_INVALID_DATA
    return _validate_unique_ids(permitted_region_tags)

func _validate_unique_ids(values: Array[StringName]) -> Error:
    var seen: Dictionary[StringName, bool] = {}
    for value: StringName in values:
        if not StableId.is_valid(value) or seen.has(value):
            return ERR_INVALID_DATA
        seen[value] = true
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La `Resource` décrit les limites de conception et reste immuable pendant le gameplay.

- `maximum_parcels` et `maximum_buildings` bornent l’agrégat avant toute allocation.

- Les tags de région sont des identifiants stables et sans doublon.

- Aucun propriétaire, bâtiment vivant ou révision n’est stocké dans cette définition.

- Le résultat `Error` permet au catalogue de refuser une ressource invalide.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/parcel_definition.gd`.**

```gdscript
class_name ParcelDefinition
extends Resource

@export var definition_id: StringName
@export var display_name_key: StringName
@export var footprint_units: int = 1
@export var allowed_building_tags: Array[StringName] = []
@export var required_site_tags: Array[StringName] = []

func validate() -> Error:
    if not StableId.is_valid(definition_id):
        return ERR_INVALID_DATA
    if not StableId.is_valid(display_name_key):
        return ERR_INVALID_DATA
    if footprint_units < 1 or footprint_units > 1000000000:
        return ERR_INVALID_DATA
    if allowed_building_tags.is_empty():
        return ERR_INVALID_DATA
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `footprint_units` utilise une unité logique documentée, pas des mètres obtenus depuis une collision.

- Les tags de bâtiment et de site servent à valider la compatibilité sans charger de scène.

- Une parcelle de conception n’enregistre aucune occupation runtime.

- La région réelle appartient à l’état de parcelle, car deux instances peuvent utiliser la même définition.

- Le catalogue complétera la validation des références croisées.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/building_definition.gd`.**

```gdscript
class_name BuildingDefinition
extends Resource

@export var definition_id: StringName
@export var display_name_key: StringName
@export var building_tags: Array[StringName] = []
@export var required_parcel_units: int = 1
@export var maximum_condition_bp: int = 10000
@export var construction_recipe_id: StringName
@export var production_recipe_ids: Array[StringName] = []

func validate() -> Error:
    if not StableId.is_valid(definition_id):
        return ERR_INVALID_DATA
    if not StableId.is_valid(display_name_key):
        return ERR_INVALID_DATA
    if building_tags.is_empty() or building_tags.size() > 32:
        return ERR_INVALID_DATA
    if required_parcel_units < 1 or required_parcel_units > 1000000000:
        return ERR_INVALID_DATA
    if maximum_condition_bp < 1 or maximum_condition_bp > 10000:
        return ERR_INVALID_DATA
    if not StableId.is_valid(construction_recipe_id):
        return ERR_INVALID_DATA
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La définition fixe les capacités du type de bâtiment sans contenir son état vivant.

- La condition maximale est exprimée en points de base pour éviter un `float` autoritaire.

- La recette de construction est référencée par identité et validée dans le catalogue.

- Les recettes de production restent des définitions séparées et réutilisables.

- La scène 3D éventuelle appartient à la présentation, pas à ce contrat.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/construction_recipe_definition.gd`.**

```gdscript
class_name ConstructionRecipeDefinition
extends Resource

@export var recipe_id: StringName
@export var material_units: Dictionary[StringName, int] = {}
@export var required_work_units: int = 1
@export var optional_currency_id: StringName
@export var optional_cost_minor: int = 0

func validate() -> Error:
    if not StableId.is_valid(recipe_id):
        return ERR_INVALID_DATA
    if material_units.is_empty() or material_units.size() > 64:
        return ERR_INVALID_DATA
    for item_id: StringName in material_units:
        var quantity: int = material_units[item_id]
        if not StableId.is_valid(item_id) or quantity < 1 or quantity > 1000000000:
            return ERR_INVALID_DATA
    if required_work_units < 1 or required_work_units > 1000000000:
        return ERR_INVALID_DATA
    if optional_cost_minor < 0 or optional_cost_minor > 9007199254740991:
        return ERR_INVALID_DATA
    if optional_cost_minor > 0 and not StableId.is_valid(optional_currency_id):
        return ERR_INVALID_DATA
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les matériaux sont indexés par définition d’objet et quantités entières.

- Le travail requis est distinct des matériaux afin de ne pas transformer automatiquement une livraison en achèvement.

- Le coût monétaire reste optionnel et utilise les unités mineures du chapitre 21.

- La recette ne choisit ni conteneur source, ni portefeuille payeur.

- Les limites empêchent une définition de contenu de produire un chantier démesuré.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/production_recipe_definition.gd`.**

```gdscript
class_name ProductionRecipeDefinition
extends Resource

@export var recipe_id: StringName
@export var required_building_tags: Array[StringName] = []
@export var input_units: Dictionary[StringName, int] = {}
@export var output_units: Dictionary[StringName, int] = {}
@export var work_units: int = 1
@export var minimum_condition_bp: int = 5000

func validate() -> Error:
    if not StableId.is_valid(recipe_id):
        return ERR_INVALID_DATA
    if required_building_tags.is_empty():
        return ERR_INVALID_DATA
    if input_units.is_empty() or output_units.is_empty():
        return ERR_INVALID_DATA
    if input_units.size() > 64 or output_units.size() > 64:
        return ERR_OUT_OF_MEMORY
    if work_units < 1 or work_units > 1000000000:
        return ERR_INVALID_DATA
    if minimum_condition_bp < 0 or minimum_condition_bp > 10000:
        return ERR_INVALID_DATA
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Une recette exige au moins un intrant et un extrant pour éviter les productions gratuites implicites.

- Les tags expriment la capacité requise sans référencer un bâtiment précis.

- La condition minimale empêche un bâtiment trop dégradé de produire.

- Les quantités détaillées seront recoupées par le catalogue et l’inventaire.

- Le temps de travail est un entier logique, indépendant d’une animation.

## 8. Liens de tenure et états vivants

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/domain_tenure_link.gd`.**

```gdscript
class_name DomainTenureLink
extends RefCounted

var political_right_id: StringName
var right_revision: int = 0
var valid_from_tick: int = 0
var valid_until_tick: int = -1
var purpose_id: StringName

func validate() -> Error:
    if not StableId.is_valid(political_right_id):
        return ERR_INVALID_DATA
    if right_revision < 0 or valid_from_tick < 0:
        return ERR_INVALID_DATA
    if valid_until_tick != -1 and valid_until_tick < valid_from_tick:
        return ERR_INVALID_DATA
    if not StableId.is_valid(purpose_id):
        return ERR_INVALID_DATA
    return OK

func is_active_at(logical_tick: int) -> bool:
    return (
        logical_tick >= valid_from_tick
        and (valid_until_tick == -1 or logical_tick <= valid_until_tick)
    )
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le lien référence un droit du chapitre 23 sans le recréer dans le domaine.

- `right_revision` permet de détecter une autorisation politique devenue obsolète.

- La fin `-1` représente un intervalle ouvert et reste distincte du tick zéro.

- `purpose_id` indique propriété, usage, construction ou exploitation selon le vocabulaire politique.

- La validité temporelle utilise le tick logique sauvegardé.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/parcel_state.gd`.**

```gdscript
class_name ParcelState
extends RefCounted

var parcel_id: StringName
var definition_id: StringName
var region_id: StringName
var site_slot_id: StringName
var occupied_units: int = 0
var building_ids: Array[StringName] = []
var revision: int = 0

func validate(definition: ParcelDefinition) -> Error:
    if definition == null or definition.validate() != OK:
        return ERR_UNCONFIGURED
    if not StableId.is_valid(parcel_id):
        return ERR_INVALID_DATA
    if definition_id != definition.definition_id:
        return ERR_INVALID_DATA
    if not StableId.is_valid(region_id) or not StableId.is_valid(site_slot_id):
        return ERR_INVALID_DATA
    if occupied_units < 0 or occupied_units > definition.footprint_units:
        return ERR_INVALID_DATA
    if building_ids.size() > 1024 or revision < 0:
        return ERR_INVALID_DATA
    var seen: Dictionary[StringName, bool] = {}
    for building_id: StringName in building_ids:
        if not StableId.is_valid(building_id) or seen.has(building_id):
            return ERR_INVALID_DATA
        seen[building_id] = true
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La parcelle conserve un emplacement logique et une région, jamais un transform de scène autoritaire.

- `occupied_units` est recoupé avec la capacité de la définition.

- La liste de bâtiments contient seulement des identifiants uniques.

- La révision protège les constructions concurrentes sur la même parcelle.

- Les droits d’accès restent vérifiés par un port séparé.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/building_state.gd`.**

```gdscript
class_name BuildingState
extends RefCounted

enum Status { OPERATIONAL, DISABLED, RUINED }

var building_id: StringName
var definition_id: StringName
var parcel_id: StringName
var status: Status = Status.OPERATIONAL
var condition_bp: int = 10000
var completed_tick: int = 0
var last_maintenance_tick: int = 0
var revision: int = 0

func validate(definition: BuildingDefinition) -> Error:
    if definition == null or definition.validate() != OK:
        return ERR_UNCONFIGURED
    if not StableId.is_valid(building_id) or not StableId.is_valid(parcel_id):
        return ERR_INVALID_DATA
    if definition_id != definition.definition_id:
        return ERR_INVALID_DATA
    if status < Status.OPERATIONAL or status > Status.RUINED:
        return ERR_INVALID_DATA
    if condition_bp < 0 or condition_bp > definition.maximum_condition_bp:
        return ERR_INVALID_DATA
    if completed_tick < 0 or last_maintenance_tick < 0 or revision < 0:
        return ERR_INVALID_DATA
    if status == Status.RUINED and condition_bp != 0:
        return ERR_INVALID_DATA
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le statut distingue un arrêt temporaire d’une ruine définitive selon la politique retenue.

- La condition est entière et bornée par la définition du bâtiment.

- Les ticks d’achèvement et d’entretien utilisent l’horloge du monde.

- L’état ne contient ni `Node3D`, ni mesh, ni animation.

- La révision protège production, entretien et changement de statut.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/worksite_state.gd`.**

```gdscript
class_name WorksiteState
extends RefCounted

enum Status { OPEN, READY_TO_COMPLETE, COMPLETED, CANCELLED }

var worksite_id: StringName
var parcel_id: StringName
var building_id: StringName
var building_definition_id: StringName
var recipe_id: StringName
var delivered_materials: Dictionary[StringName, int] = {}
var completed_work_units: int = 0
var started_tick: int = 0
var last_progress_tick: int = 0
var status: Status = Status.OPEN
var revision: int = 0

func validate(recipe: ConstructionRecipeDefinition) -> Error:
    if recipe == null or recipe.validate() != OK:
        return ERR_UNCONFIGURED
    if not StableId.is_valid(worksite_id) or not StableId.is_valid(parcel_id):
        return ERR_INVALID_DATA
    if not StableId.is_valid(building_id) or not StableId.is_valid(building_definition_id):
        return ERR_INVALID_DATA
    if recipe_id != recipe.recipe_id:
        return ERR_INVALID_DATA
    if completed_work_units < 0 or completed_work_units > recipe.required_work_units:
        return ERR_INVALID_DATA
    if started_tick < 0 or last_progress_tick < started_tick or revision < 0:
        return ERR_INVALID_DATA
    for item_id: StringName in delivered_materials:
        var delivered: int = delivered_materials[item_id]
        var required: int = int(recipe.material_units.get(item_id, -1))
        if required < 0 or delivered < 0 or delivered > required:
            return ERR_INVALID_DATA
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le chantier conserve des quantités livrées, jamais les objets ou lots eux-mêmes.

- Chaque quantité est recoupée avec la recette afin d’interdire les surlivraisons.

- Le travail accompli est borné séparément des matériaux.

- Le bâtiment reçoit déjà une identité stable avant l’achèvement, ce qui facilite l’idempotence.

- Les ticks et la révision rendent la progression diagnosticable.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/domain_state.gd`.**

```gdscript
class_name DomainState
extends RefCounted

const MAX_TENURE_LINKS := 64

var domain_id: StringName
var definition_id: StringName
var governing_institution_id: StringName
var tenure_links: Array[DomainTenureLink] = []
var parcels: Dictionary[StringName, ParcelState] = {}
var buildings: Dictionary[StringName, BuildingState] = {}
var worksites: Dictionary[StringName, WorksiteState] = {}
var revision: int = 0
var event_sequence: int = 0

func duplicate_detached() -> DomainState:
    var copy := DomainState.new()
    copy.domain_id = domain_id
    copy.definition_id = definition_id
    copy.governing_institution_id = governing_institution_id
    copy.revision = revision
    copy.event_sequence = event_sequence
    for link: DomainTenureLink in tenure_links:
        var cloned := DomainTenureLink.new()
        cloned.political_right_id = link.political_right_id
        cloned.right_revision = link.right_revision
        cloned.valid_from_tick = link.valid_from_tick
        cloned.valid_until_tick = link.valid_until_tick
        cloned.purpose_id = link.purpose_id
        copy.tenure_links.append(cloned)
    for parcel_id: StringName in parcels:
        copy.parcels[parcel_id] = parcels[parcel_id].duplicate(true)
    for building_id: StringName in buildings:
        copy.buildings[building_id] = buildings[building_id].duplicate(true)
    for worksite_id: StringName in worksites:
        copy.worksites[worksite_id] = worksites[worksite_id].duplicate(true)
    return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’agrégat regroupe les états qui doivent rester cohérents au moment d’un commit.

- Les liens de tenure sont copiés champ par champ afin de ne partager aucun objet mutable.

- Parcelles, bâtiments et chantiers sont copiés avant mutation.

- La révision protège l’ensemble du domaine tandis que les sous-agrégats conservent leurs propres révisions.

- Les index dérivés et représentations de scène restent absents.

## 9. Catalogue et validation croisée

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/application/domain_catalog.gd`.**

```gdscript
class_name DomainCatalog
extends RefCounted

var _domains: Dictionary[StringName, DomainDefinition] = {}
var _parcels: Dictionary[StringName, ParcelDefinition] = {}
var _buildings: Dictionary[StringName, BuildingDefinition] = {}
var _construction: Dictionary[StringName, ConstructionRecipeDefinition] = {}
var _production: Dictionary[StringName, ProductionRecipeDefinition] = {}

func validate_cross_references() -> Error:
    for building: BuildingDefinition in _buildings.values():
        if not _construction.has(building.construction_recipe_id):
            return ERR_DOES_NOT_EXIST
        for recipe_id: StringName in building.production_recipe_ids:
            if not _production.has(recipe_id):
                return ERR_DOES_NOT_EXIST
    return OK

func get_building(definition_id: StringName) -> BuildingDefinition:
    var value := _buildings.get(definition_id) as BuildingDefinition
    return null if value == null else value.duplicate(true) as BuildingDefinition

func get_construction(recipe_id: StringName) -> ConstructionRecipeDefinition:
    var value := _construction.get(recipe_id) as ConstructionRecipeDefinition
    return null if value == null else value.duplicate(true) as ConstructionRecipeDefinition

func get_production(recipe_id: StringName) -> ProductionRecipeDefinition:
    var value := _production.get(recipe_id) as ProductionRecipeDefinition
    return null if value == null else value.duplicate(true) as ProductionRecipeDefinition
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le catalogue centralise les définitions mais ne conserve aucun état de joueur.

- Les bâtiments sont recoupés avec leurs recettes après le chargement complet.

- Les lectures retournent des copies profondes pour maintenir l’immuabilité de conception.

- Une référence manquante bloque le bootstrap avant le gameplay.

- Les méthodes d’enregistrement suivent le modèle validé du chapitre 22 et refusent les doublons.

## 10. Arithmétique de progression

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/application/domain_math.gd`.**

```gdscript
class_name DomainMath
extends RefCounted

const MAX_SAFE_INTEGER := 9007199254740991
const BASIS_POINT_SCALE := 10000

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

static func ratio_basis_points(value: int, maximum: int) -> int:
    if value < 0 or maximum < 1 or value > maximum:
        return -1
    if value > MAX_SAFE_INTEGER / BASIS_POINT_SCALE:
        return -1
    return (value * BASIS_POINT_SCALE) / maximum
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’addition vérifie la plage entière sûre avant d’effectuer l’opération.

- `ratio_basis_points()` produit une progression de `0` à `10000` sans nombre flottant.

- La multiplication est vérifiée avant le calcul du ratio.

- La sentinelle `-1` distingue un calcul invalide d’une progression nulle.

- Cette arithmétique peut être sérialisée et rejouée de manière déterministe.

## 11. Dépôt et idempotence

> **[LECTURE] Contrat du dépôt — Structure de référence.**

```gdscript
class_name DomainRepository
extends RefCounted

func get_domain(_domain_id: StringName) -> DomainState:
    return null

func all_domain_ids_sorted() -> Array[StringName]:
    return []

func replace_domain(
    _candidate: DomainState,
    _expected_revision: int,
) -> Error:
    return ERR_UNAVAILABLE

func find_command_result(
    _command_id: StringName,
    _fingerprint: String,
) -> DomainCommandResult:
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

**Explication détaillée du bloc :**

- Les lectures doivent renvoyer des copies détachées et les identifiants triés.

- `replace_domain()` revalide la révision au dernier instant.

- Le registre d’idempotence distingue replay identique et conflit d’empreinte.

- Le dépôt ne décide ni des droits, ni des coûts, ni des recettes.

- `replace_all()` est réservé à une restauration complète déjà validée.

## 12. Ports vers les autorités externes

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/application/domain_rights_port.gd`.**

```gdscript
class_name DomainRightsPort
extends RefCounted

class Decision:
    extends RefCounted

    enum Status { ALLOW, DENY, NOT_APPLICABLE, INDETERMINATE }

    var status: Status = Status.INDETERMINATE
    var right_id: StringName
    var right_revision: int = 0
    var valid_until_tick: int = 0
    var reason_code: StringName

    func validate() -> Error:
        if status < Status.ALLOW or status > Status.INDETERMINATE:
            return ERR_INVALID_DATA
        if right_revision < 0 or valid_until_tick < 0:
            return ERR_INVALID_DATA
        if not StableId.is_valid(reason_code):
            return ERR_INVALID_DATA
        if status == Status.ALLOW and not StableId.is_valid(right_id):
            return ERR_INVALID_DATA
        return OK

func decide(
    _actor_character_id: StringName,
    _domain_id: StringName,
    _action_id: StringName,
    _logical_tick: int,
) -> Decision:
    return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le port consomme une décision du chapitre 23 sans reproduire son moteur de lois.

- Seul `ALLOW` autorise une action protégée ; les autres statuts restent des refus conservateurs.

- La révision et l’échéance permettent de rejeter une décision devenue ancienne.

- Le code de raison rend le refus explicable.

- Le port ne modifie ni droit politique ni domaine.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/application/domain_ecology_port.gd`.**

```gdscript
class_name DomainEcologyPort
extends RefCounted

class SiteSnapshot:
    extends RefCounted

    var region_id: StringName
    var site_slot_id: StringName
    var region_revision: int = 0
    var valid_until_tick: int = 0
    var site_tags: Array[StringName] = []
    var capacity_units: int = 0

    func validate() -> Error:
        if not StableId.is_valid(region_id) or not StableId.is_valid(site_slot_id):
            return ERR_INVALID_DATA
        if region_revision < 0 or valid_until_tick < 0 or capacity_units < 0:
            return ERR_INVALID_DATA
        if site_tags.size() > 64:
            return ERR_OUT_OF_MEMORY
        return OK

func snapshot_for(
    _region_id: StringName,
    _site_slot_id: StringName,
    _logical_tick: int,
) -> SiteSnapshot:
    return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’écologie fournit la capacité et les tags d’un site sans céder sa région au domaine.

- Le snapshot porte une révision et une échéance.

- La parcelle conserve seulement l’identité du site choisi.

- La construction refuse un contexte absent, expiré ou incompatible.

- Aucune réserve écologique n’est consommée par ce port.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/application/domain_inventory_port.gd`.**

```gdscript
class_name DomainInventoryPort
extends RefCounted

class PreparedMutation:
    extends RefCounted

    var authority_id: StringName = &"inventory"
    var payload: Dictionary = {}
    var expected_revisions: Dictionary[StringName, int] = {}

    func validate() -> Error:
        if authority_id != &"inventory":
            return ERR_INVALID_DATA
        if payload.is_empty() or expected_revisions.is_empty():
            return ERR_INVALID_DATA
        return OK

func prepare_material_delivery(
    _command: DeliverMaterialsCommand,
    _remaining_requirements: Dictionary[StringName, int],
) -> PreparedMutation:
    return null

func prepare_production_exchange(
    _command: RunProductionCommand,
    _inputs: Dictionary[StringName, int],
    _outputs: Dictionary[StringName, int],
) -> PreparedMutation:
    return null

func prepare_maintenance_materials(
    _command: MaintainBuildingCommand,
    _requirements: Dictionary[StringName, int],
) -> PreparedMutation:
    return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’inventaire sélectionne les lots, vérifie leur provenance et prépare les quantités consommées ou produites.

- Le domaine fournit des besoins, jamais des mutations internes de conteneur.

- Les révisions attendues accompagnent le candidat opaque.

- Un payload vide est refusé avant le commit.

- Les trois opérations restent distinctes pour conserver des diagnostics précis.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/application/domain_economy_port.gd`.**

```gdscript
class_name DomainEconomyPort
extends RefCounted

class PreparedCost:
    extends RefCounted

    var authority_id: StringName = &"economy"
    var payload: Dictionary = {}
    var expected_wallet_revision: int = 0

    func validate() -> Error:
        if authority_id != &"economy":
            return ERR_INVALID_DATA
        if payload.is_empty() or expected_wallet_revision < 0:
            return ERR_INVALID_DATA
        return OK

func prepare_construction_cost(
    _command: StartWorksiteCommand,
    _currency_id: StringName,
    _amount_minor: int,
) -> PreparedCost:
    return null

func prepare_maintenance_cost(
    _command: MaintainBuildingCommand,
    _currency_id: StringName,
    _amount_minor: int,
) -> PreparedCost:
    return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’économie prépare les écritures et relit le portefeuille payeur.

- Le domaine ne calcule jamais un solde et ne modifie aucune écriture.

- Les montants viennent d’une recette validée ou d’une politique injectée.

- Une révision de portefeuille obsolète bloque le commit.

- Un coût nul n’exige pas de candidat économique.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/application/domain_transaction_commit_port.gd`.**

```gdscript
class_name DomainTransactionCommitPort
extends RefCounted

func commit_domain_only(
    _domain_candidate: DomainState,
    _expected_domain_revision: int,
    _result: DomainCommandResult,
    _command_id: StringName,
    _fingerprint: String,
) -> Error:
    return ERR_UNAVAILABLE

func commit_with_external_candidates(
    _domain_candidate: DomainState,
    _expected_domain_revision: int,
    _inventory_candidate: DomainInventoryPort.PreparedMutation,
    _economy_candidate: DomainEconomyPort.PreparedCost,
    _result: DomainCommandResult,
    _command_id: StringName,
    _fingerprint: String,
) -> Error:
    return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le point de composition revalide toutes les révisions avant le premier remplacement.

- Le résultat idempotent est enregistré dans le même lot que les états mutés.

- Un candidat économique peut être nul lorsque la recette ne porte aucun coût.

- Un candidat d’inventaire est obligatoire dès qu’un matériau ou produit change.

- Aucun événement n’est émis par le port avant le succès complet.

## 13. Résultats et commandes

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/domain_command_result.gd`.**

```gdscript
class_name DomainCommandResult
extends RefCounted

enum Status {
    COMMITTED,
    REPLAYED,
    REJECTED_INVALID_COMMAND,
    REJECTED_NOT_FOUND,
    REJECTED_UNAUTHORIZED,
    REJECTED_STALE_REVISION,
    REJECTED_SITE,
    REJECTED_MATERIALS,
    REJECTED_ECONOMY,
    REJECTED_NOT_READY,
    REJECTED_IDEMPOTENCY_CONFLICT,
    REJECTED_INTERNAL,
}

var status: Status = Status.REJECTED_INTERNAL
var command_id: StringName
var domain_id: StringName
var target_id: StringName
var message: String = ""

func is_success() -> bool:
    return status in [Status.COMMITTED, Status.REPLAYED]

func validate() -> Error:
    if status < Status.COMMITTED or status > Status.REJECTED_INTERNAL:
        return ERR_INVALID_DATA
    if is_success():
        if not StableId.is_valid(command_id) or not StableId.is_valid(domain_id):
            return ERR_INVALID_DATA
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le résultat distingue les refus de droit, site, matériaux, économie et préparation.

- `REPLAYED` confirme un succès antérieur sans seconde mutation.

- Un succès exige les identifiants nécessaires au diagnostic.

- Le résultat ne contient aucun état mutable.

- Les services convertissent les codes techniques du commit vers ces statuts métier.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/start_worksite_command.gd`.**

```gdscript
class_name StartWorksiteCommand
extends RefCounted

var command_id: StringName
var domain_id: StringName
var parcel_id: StringName
var worksite_id: StringName
var building_id: StringName
var building_definition_id: StringName
var actor_character_id: StringName
var payer_wallet_id: StringName
var expected_domain_revision: int = 0
var expected_parcel_revision: int = 0
var logical_tick: int = 0
var fingerprint: String = ""

func validate() -> Error:
    if not StableId.is_valid(command_id) or not StableId.is_valid(domain_id):
        return ERR_INVALID_DATA
    if expected_domain_revision < 0 or logical_tick < 0:
        return ERR_INVALID_DATA
    if fingerprint.is_empty() or fingerprint.length() > 128:
        return ERR_INVALID_DATA
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’ouverture d’un chantier fixe à l’avance les identités du chantier et du futur bâtiment.

- La commande transporte une identité et une empreinte pour l’idempotence.

- Les révisions attendues empêchent d’écraser un état plus récent.

- Le tick logique ordonne l’opération sans consulter l’heure réelle.

- Les validations spécifiques supplémentaires sont appliquées par le service avant préparation.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/deliver_materials_command.gd`.**

```gdscript
class_name DeliverMaterialsCommand
extends RefCounted

var command_id: StringName
var domain_id: StringName
var worksite_id: StringName
var actor_character_id: StringName
var source_container_id: StringName
var requested_units: Dictionary[StringName, int] = {}
var expected_domain_revision: int = 0
var expected_worksite_revision: int = 0
var logical_tick: int = 0
var fingerprint: String = ""

func validate() -> Error:
    if not StableId.is_valid(command_id) or not StableId.is_valid(domain_id):
        return ERR_INVALID_DATA
    if expected_domain_revision < 0 or logical_tick < 0:
        return ERR_INVALID_DATA
    if fingerprint.is_empty() or fingerprint.length() > 128:
        return ERR_INVALID_DATA
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La livraison demande des quantités par définition, mais laisse l’inventaire choisir les lots.

- La commande transporte une identité et une empreinte pour l’idempotence.

- Les révisions attendues empêchent d’écraser un état plus récent.

- Le tick logique ordonne l’opération sans consulter l’heure réelle.

- Les validations spécifiques supplémentaires sont appliquées par le service avant préparation.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/advance_worksite_command.gd`.**

```gdscript
class_name AdvanceWorksiteCommand
extends RefCounted

var command_id: StringName
var domain_id: StringName
var worksite_id: StringName
var actor_character_id: StringName
var requested_work_units: int = 0
var expected_domain_revision: int = 0
var expected_worksite_revision: int = 0
var logical_tick: int = 0
var fingerprint: String = ""

func validate() -> Error:
    if not StableId.is_valid(command_id) or not StableId.is_valid(domain_id):
        return ERR_INVALID_DATA
    if expected_domain_revision < 0 or logical_tick < 0:
        return ERR_INVALID_DATA
    if fingerprint.is_empty() or fingerprint.length() > 128:
        return ERR_INVALID_DATA
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La progression porte une quantité de travail explicite et ne dépend pas d’une animation.

- La commande transporte une identité et une empreinte pour l’idempotence.

- Les révisions attendues empêchent d’écraser un état plus récent.

- Le tick logique ordonne l’opération sans consulter l’heure réelle.

- Les validations spécifiques supplémentaires sont appliquées par le service avant préparation.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/run_production_command.gd`.**

```gdscript
class_name RunProductionCommand
extends RefCounted

var command_id: StringName
var domain_id: StringName
var building_id: StringName
var recipe_id: StringName
var actor_character_id: StringName
var input_container_id: StringName
var output_container_id: StringName
var cycles: int = 1
var expected_domain_revision: int = 0
var expected_building_revision: int = 0
var logical_tick: int = 0
var fingerprint: String = ""

func validate() -> Error:
    if not StableId.is_valid(command_id) or not StableId.is_valid(domain_id):
        return ERR_INVALID_DATA
    if expected_domain_revision < 0 or logical_tick < 0:
        return ERR_INVALID_DATA
    if fingerprint.is_empty() or fingerprint.length() > 128:
        return ERR_INVALID_DATA
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La production nomme les conteneurs d’entrée et de sortie sans exposer leur contenu.

- La commande transporte une identité et une empreinte pour l’idempotence.

- Les révisions attendues empêchent d’écraser un état plus récent.

- Le tick logique ordonne l’opération sans consulter l’heure réelle.

- Les validations spécifiques supplémentaires sont appliquées par le service avant préparation.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/domain/maintain_building_command.gd`.**

```gdscript
class_name MaintainBuildingCommand
extends RefCounted

var command_id: StringName
var domain_id: StringName
var building_id: StringName
var actor_character_id: StringName
var source_container_id: StringName
var payer_wallet_id: StringName
var restore_condition_bp: int = 0
var expected_domain_revision: int = 0
var expected_building_revision: int = 0
var logical_tick: int = 0
var fingerprint: String = ""

func validate() -> Error:
    if not StableId.is_valid(command_id) or not StableId.is_valid(domain_id):
        return ERR_INVALID_DATA
    if expected_domain_revision < 0 or logical_tick < 0:
        return ERR_INVALID_DATA
    if fingerprint.is_empty() or fingerprint.length() > 128:
        return ERR_INVALID_DATA
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’entretien demande une restauration bornée et peut préparer matériaux et coût.

- La commande transporte une identité et une empreinte pour l’idempotence.

- Les révisions attendues empêchent d’écraser un état plus récent.

- Le tick logique ordonne l’opération sans consulter l’heure réelle.

- Les validations spécifiques supplémentaires sont appliquées par le service avant préparation.

## 14. Politique d’accès au domaine

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/application/domain_access_policy.gd`.**

```gdscript
class_name DomainAccessPolicy
extends RefCounted

var _rights: DomainRightsPort

func authorize(
    actor_character_id: StringName,
    domain: DomainState,
    action_id: StringName,
    logical_tick: int,
) -> DomainRightsPort.Decision:
    if _rights == null or domain == null:
        return null
    var decision := _rights.decide(
        actor_character_id,
        domain.domain_id,
        action_id,
        logical_tick,
    )
    if decision == null or decision.validate() != OK:
        return null
    if logical_tick > decision.valid_until_tick:
        return null
    return decision

func is_allowed(decision: DomainRightsPort.Decision) -> bool:
    return decision != null and decision.status == DomainRightsPort.Decision.Status.ALLOW
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La politique délègue la loi et la juridiction au chapitre 23.

- Une décision absente, invalide ou expirée ne devient jamais une autorisation implicite.

- `is_allowed()` accepte exclusivement le statut `ALLOW`.

- Le domaine reste libre d’appliquer ensuite ses invariants de capacité et de révision.

- Cette séparation permet de remplacer l’adaptateur politique sans modifier les états fonciers.

## 15. Ouvrir un chantier

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/application/domain_construction_service.gd`.**

```gdscript
class_name DomainConstructionService
extends RefCounted

signal worksite_started(result: DomainCommandResult)
signal materials_delivered(result: DomainCommandResult)
signal worksite_advanced(result: DomainCommandResult)
signal building_completed(result: DomainCommandResult)

var _catalog: DomainCatalog
var _repository: DomainRepository
var _access := DomainAccessPolicy.new()
var _ecology: DomainEcologyPort
var _inventory: DomainInventoryPort
var _economy: DomainEconomyPort
var _commit: DomainTransactionCommitPort

func start_worksite(command: StartWorksiteCommand) -> DomainCommandResult:
    if command == null or command.validate() != OK:
        return _result(DomainCommandResult.Status.REJECTED_INVALID_COMMAND, null)
    var replay := _replay_or_conflict(command.command_id, command.fingerprint)
    if replay != null:
        return replay
    var source := _repository.get_domain(command.domain_id)
    if source == null:
        return _result(DomainCommandResult.Status.REJECTED_NOT_FOUND, command)
    if source.revision != command.expected_domain_revision:
        return _result(DomainCommandResult.Status.REJECTED_STALE_REVISION, command)
    var parcel := source.parcels.get(command.parcel_id) as ParcelState
    var building_definition := _catalog.get_building(command.building_definition_id)
    if parcel == null or building_definition == null:
        return _result(DomainCommandResult.Status.REJECTED_NOT_FOUND, command)
    if parcel.revision != command.expected_parcel_revision:
        return _result(DomainCommandResult.Status.REJECTED_STALE_REVISION, command)
    var decision := _access.authorize(
        command.actor_character_id, source, &"domain.action.build", command.logical_tick
    )
    if not _access.is_allowed(decision):
        return _result(DomainCommandResult.Status.REJECTED_UNAUTHORIZED, command)
    var site := _ecology.snapshot_for(parcel.region_id, parcel.site_slot_id, command.logical_tick)
    if not _site_accepts(site, parcel, building_definition, command.logical_tick):
        return _result(DomainCommandResult.Status.REJECTED_SITE, command)
    return _prepare_and_commit_start(command, source, parcel, building_definition)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La méthode refuse d’abord forme invalide, replay conflictuel, absence et révisions obsolètes.

- Le droit de construire est demandé avant de préparer un coût ou modifier un candidat.

- Le contexte de site est relu avec son échéance et ses tags.

- La parcelle et le domaine restent inchangés jusqu’au helper de préparation.

- Le résultat final sera émis uniquement après le commit commun.

> **[LECTURE] Préparation interne — Suite de `domain_construction_service.gd`.**

```gdscript
func _prepare_and_commit_start(
    command: StartWorksiteCommand,
    source: DomainState,
    parcel: ParcelState,
    building_definition: BuildingDefinition,
) -> DomainCommandResult:
    var recipe := _catalog.get_construction(building_definition.construction_recipe_id)
    if recipe == null:
        return _result(DomainCommandResult.Status.REJECTED_INTERNAL, command)
    var candidate := source.duplicate_detached()
    var candidate_parcel := candidate.parcels[parcel.parcel_id] as ParcelState
    if candidate.worksites.has(command.worksite_id) or candidate.buildings.has(command.building_id):
        return _result(DomainCommandResult.Status.REJECTED_INVALID_COMMAND, command)
    if candidate_parcel.occupied_units + building_definition.required_parcel_units > _parcel_capacity(candidate_parcel):
        return _result(DomainCommandResult.Status.REJECTED_SITE, command)

    var worksite := WorksiteState.new()
    worksite.worksite_id = command.worksite_id
    worksite.parcel_id = command.parcel_id
    worksite.building_id = command.building_id
    worksite.building_definition_id = building_definition.definition_id
    worksite.recipe_id = recipe.recipe_id
    worksite.started_tick = command.logical_tick
    worksite.last_progress_tick = command.logical_tick
    candidate.worksites[worksite.worksite_id] = worksite
    candidate_parcel.occupied_units += building_definition.required_parcel_units
    candidate_parcel.revision += 1
    candidate.revision += 1

    var cost_candidate: DomainEconomyPort.PreparedCost = null
    if recipe.optional_cost_minor > 0:
        cost_candidate = _economy.prepare_construction_cost(
            command, recipe.optional_currency_id, recipe.optional_cost_minor
        )
        if cost_candidate == null or cost_candidate.validate() != OK:
            return _result(DomainCommandResult.Status.REJECTED_ECONOMY, command)
    var result := _result(DomainCommandResult.Status.COMMITTED, command)
    var code := _commit.commit_with_external_candidates(
        candidate, source.revision, null, cost_candidate,
        result, command.command_id, command.fingerprint
    )
    if code != OK:
        return _commit_failure(command, code)
    worksite_started.emit(result)
    return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le chantier et le futur bâtiment reçoivent leurs identités avant le commit.

- L’occupation de la parcelle est réservée dans le candidat afin d’empêcher deux chantiers concurrents.

- Le coût est préparé seulement après la validation complète du candidat de domaine.

- Le commit accepte un candidat d’inventaire nul car l’ouverture ne consomme encore aucun matériau.

- Le signal est émis après le succès du lot.

## 16. Livrer des matériaux

> **[LECTURE] Livraison idempotente — Méthode de `DomainConstructionService`.**

```gdscript
func deliver_materials(command: DeliverMaterialsCommand) -> DomainCommandResult:
    if command == null or command.validate() != OK or command.requested_units.is_empty():
        return _result(DomainCommandResult.Status.REJECTED_INVALID_COMMAND, command)
    var replay := _replay_or_conflict(command.command_id, command.fingerprint)
    if replay != null:
        return replay
    var source := _repository.get_domain(command.domain_id)
    if source == null or source.revision != command.expected_domain_revision:
        return _result(DomainCommandResult.Status.REJECTED_STALE_REVISION, command)
    var worksite := source.worksites.get(command.worksite_id) as WorksiteState
    if worksite == null:
        return _result(DomainCommandResult.Status.REJECTED_NOT_FOUND, command)
    if worksite.revision != command.expected_worksite_revision:
        return _result(DomainCommandResult.Status.REJECTED_STALE_REVISION, command)
    var decision := _access.authorize(
        command.actor_character_id, source, &"domain.action.deliver", command.logical_tick
    )
    if not _access.is_allowed(decision):
        return _result(DomainCommandResult.Status.REJECTED_UNAUTHORIZED, command)
    var recipe := _catalog.get_construction(worksite.recipe_id)
    var remaining := _remaining_materials(worksite, recipe)
    if not _request_fits(command.requested_units, remaining):
        return _result(DomainCommandResult.Status.REJECTED_MATERIALS, command)
    var inventory_candidate := _inventory.prepare_material_delivery(command, remaining)
    if inventory_candidate == null or inventory_candidate.validate() != OK:
        return _result(DomainCommandResult.Status.REJECTED_MATERIALS, command)
    var candidate := source.duplicate_detached()
    var candidate_worksite := candidate.worksites[command.worksite_id] as WorksiteState
    for item_id: StringName in command.requested_units:
        candidate_worksite.delivered_materials[item_id] = (
            int(candidate_worksite.delivered_materials.get(item_id, 0))
            + command.requested_units[item_id]
        )
    candidate_worksite.revision += 1
    candidate.revision += 1
    return _commit_delivery(command, source, candidate, inventory_candidate)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La demande est comparée aux besoins restants avant d’interroger l’inventaire.

- L’inventaire prépare les lots à consommer et leurs révisions.

- Le chantier candidat additionne uniquement les quantités demandées et validées.

- Aucune quantité n’est retirée du conteneur avant le commit.

- Le helper de commit enregistre aussi l’identité et l’empreinte de la commande.

## 17. Faire progresser et achever le chantier

> **[LECTURE] Progression de travail — Méthode de `DomainConstructionService`.**

```gdscript
func advance_worksite(command: AdvanceWorksiteCommand) -> DomainCommandResult:
    if command == null or command.validate() != OK:
        return _result(DomainCommandResult.Status.REJECTED_INVALID_COMMAND, command)
    if command.requested_work_units < 1 or command.requested_work_units > 1000000:
        return _result(DomainCommandResult.Status.REJECTED_INVALID_COMMAND, command)
    var source := _repository.get_domain(command.domain_id)
    var worksite := null if source == null else source.worksites.get(command.worksite_id) as WorksiteState
    if worksite == null:
        return _result(DomainCommandResult.Status.REJECTED_NOT_FOUND, command)
    if source.revision != command.expected_domain_revision or worksite.revision != command.expected_worksite_revision:
        return _result(DomainCommandResult.Status.REJECTED_STALE_REVISION, command)
    var recipe := _catalog.get_construction(worksite.recipe_id)
    var next_value: Variant = DomainMath.checked_add(
        worksite.completed_work_units, command.requested_work_units
    )
    if next_value == null:
        return _result(DomainCommandResult.Status.REJECTED_INTERNAL, command)
    var candidate := source.duplicate_detached()
    var target := candidate.worksites[command.worksite_id] as WorksiteState
    target.completed_work_units = mini(int(next_value), recipe.required_work_units)
    target.last_progress_tick = command.logical_tick
    target.revision += 1
    if _materials_complete(target, recipe) and target.completed_work_units == recipe.required_work_units:
        target.status = WorksiteState.Status.READY_TO_COMPLETE
    candidate.revision += 1
    return _commit_domain_only(command, source, candidate, &"worksite_advanced")
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le travail demandé est borné avant l’addition.

- La valeur finale est limitée au travail total de la recette.

- Le statut prêt exige simultanément travail et matériaux complets.

- Le tick logique remplace toute durée d’animation ou horloge réelle.

- La progression ne crée pas encore le bâtiment opérationnel.

> **[LECTURE] Achèvement atomique — Méthode de `DomainConstructionService`.**

```gdscript
func complete_building(command: AdvanceWorksiteCommand) -> DomainCommandResult:
    var source := _repository.get_domain(command.domain_id)
    var worksite := null if source == null else source.worksites.get(command.worksite_id) as WorksiteState
    if worksite == null or worksite.status != WorksiteState.Status.READY_TO_COMPLETE:
        return _result(DomainCommandResult.Status.REJECTED_NOT_READY, command)
    if source.revision != command.expected_domain_revision or worksite.revision != command.expected_worksite_revision:
        return _result(DomainCommandResult.Status.REJECTED_STALE_REVISION, command)
    var definition := _catalog.get_building(worksite.building_definition_id)
    var candidate := source.duplicate_detached()
    var target_worksite := candidate.worksites[worksite.worksite_id] as WorksiteState
    var building := BuildingState.new()
    building.building_id = worksite.building_id
    building.definition_id = worksite.building_definition_id
    building.parcel_id = worksite.parcel_id
    building.condition_bp = definition.maximum_condition_bp
    building.completed_tick = command.logical_tick
    building.last_maintenance_tick = command.logical_tick
    candidate.buildings[building.building_id] = building
    var parcel := candidate.parcels[building.parcel_id] as ParcelState
    parcel.building_ids.append(building.building_id)
    parcel.building_ids.sort()
    parcel.revision += 1
    target_worksite.status = WorksiteState.Status.COMPLETED
    target_worksite.revision += 1
    candidate.revision += 1
    return _commit_domain_only(command, source, candidate, &"building_completed")
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La méthode exige le statut prêt et les deux révisions attendues.

- Le bâtiment est créé dans le candidat avec une condition initiale issue de sa définition.

- La parcelle référence ensuite le bâtiment par identité stable.

- Le chantier est conservé comme historique terminé plutôt que supprimé silencieusement.

- Le lot ne modifie aucun objet ni portefeuille, car ils ont déjà été traités lors des étapes précédentes.

## 18. Production

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/application/domain_production_service.gd`.**

```gdscript
class_name DomainProductionService
extends RefCounted

signal production_committed(result: DomainCommandResult)

var _catalog: DomainCatalog
var _repository: DomainRepository
var _access := DomainAccessPolicy.new()
var _inventory: DomainInventoryPort
var _commit: DomainTransactionCommitPort

func run(command: RunProductionCommand) -> DomainCommandResult:
    if command == null or command.validate() != OK or command.cycles < 1 or command.cycles > 1000:
        return _result(DomainCommandResult.Status.REJECTED_INVALID_COMMAND, command)
    var source := _repository.get_domain(command.domain_id)
    var building := null if source == null else source.buildings.get(command.building_id) as BuildingState
    var recipe := _catalog.get_production(command.recipe_id)
    if building == null or recipe == null:
        return _result(DomainCommandResult.Status.REJECTED_NOT_FOUND, command)
    if source.revision != command.expected_domain_revision or building.revision != command.expected_building_revision:
        return _result(DomainCommandResult.Status.REJECTED_STALE_REVISION, command)
    if building.status != BuildingState.Status.OPERATIONAL or building.condition_bp < recipe.minimum_condition_bp:
        return _result(DomainCommandResult.Status.REJECTED_NOT_READY, command)
    var definition := _catalog.get_building(building.definition_id)
    if command.recipe_id not in definition.production_recipe_ids:
        return _result(DomainCommandResult.Status.REJECTED_UNAUTHORIZED, command)
    var decision := _access.authorize(
        command.actor_character_id, source, &"domain.action.produce", command.logical_tick
    )
    if not _access.is_allowed(decision):
        return _result(DomainCommandResult.Status.REJECTED_UNAUTHORIZED, command)
    var inputs := _scaled_units(recipe.input_units, command.cycles)
    var outputs := _scaled_units(recipe.output_units, command.cycles)
    if inputs == null or outputs == null:
        return _result(DomainCommandResult.Status.REJECTED_INTERNAL, command)
    var inventory_candidate := _inventory.prepare_production_exchange(command, inputs, outputs)
    if inventory_candidate == null or inventory_candidate.validate() != OK:
        return _result(DomainCommandResult.Status.REJECTED_MATERIALS, command)
    return _commit_production(command, source, building, inventory_candidate)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La production vérifie bâtiment, recette, révisions, statut et condition avant de préparer les objets.

- La définition du bâtiment doit explicitement autoriser la recette.

- Les quantités sont multipliées avec contrôle de dépassement.

- L’inventaire prépare simultanément consommation des intrants et création des extrants.

- Le domaine committe ensuite sa révision avec le candidat d’inventaire et le résultat idempotent.

## 19. Entretien et dégradation

> **[LECTURE] Dégradation agrégée — Politique déterministe.**

```gdscript
func degrade_building(
    building: BuildingState,
    elapsed_ticks: int,
    loss_bp_per_day: int,
    ticks_per_day: int,
) -> Error:
    if building == null or elapsed_ticks < 0 or ticks_per_day < 1:
        return ERR_INVALID_PARAMETER
    if loss_bp_per_day < 0 or loss_bp_per_day > 10000:
        return ERR_INVALID_PARAMETER
    if elapsed_ticks > DomainMath.MAX_SAFE_INTEGER / loss_bp_per_day:
        return ERR_INVALID_DATA
    var loss := (elapsed_ticks * loss_bp_per_day) / ticks_per_day
    building.condition_bp = maxi(0, building.condition_bp - loss)
    if building.condition_bp == 0:
        building.status = BuildingState.Status.RUINED
    elif building.condition_bp < 2500:
        building.status = BuildingState.Status.DISABLED
    building.revision += 1
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La dégradation utilise le tick logique et une perte en points de base par jour.

- La multiplication est protégée avant la division.

- La condition ne devient jamais négative.

- Les seuils de statut sont une politique pédagogique remplaçable.

- Cette opération travaille sur un candidat de bâtiment, jamais sur une scène.

> **[LECTURE] Entretien coordonné — Service applicatif.**

```gdscript
func maintain(command: MaintainBuildingCommand) -> DomainCommandResult:
    if command == null or command.validate() != OK:
        return _result(DomainCommandResult.Status.REJECTED_INVALID_COMMAND, command)
    if command.restore_condition_bp < 1 or command.restore_condition_bp > 10000:
        return _result(DomainCommandResult.Status.REJECTED_INVALID_COMMAND, command)
    var source := _repository.get_domain(command.domain_id)
    var building := null if source == null else source.buildings.get(command.building_id) as BuildingState
    if building == null:
        return _result(DomainCommandResult.Status.REJECTED_NOT_FOUND, command)
    if source.revision != command.expected_domain_revision or building.revision != command.expected_building_revision:
        return _result(DomainCommandResult.Status.REJECTED_STALE_REVISION, command)
    var requirements := _maintenance_requirements(building, command.restore_condition_bp)
    var inventory_candidate := _inventory.prepare_maintenance_materials(command, requirements)
    if inventory_candidate == null or inventory_candidate.validate() != OK:
        return _result(DomainCommandResult.Status.REJECTED_MATERIALS, command)
    var candidate := source.duplicate_detached()
    var target := candidate.buildings[building.building_id] as BuildingState
    var definition := _catalog.get_building(target.definition_id)
    target.condition_bp = mini(
        definition.maximum_condition_bp,
        target.condition_bp + command.restore_condition_bp,
    )
    target.status = BuildingState.Status.OPERATIONAL
    target.last_maintenance_tick = command.logical_tick
    target.revision += 1
    candidate.revision += 1
    return _commit_maintenance(command, source, candidate, inventory_candidate)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’entretien prépare les matériaux avant de relever la condition du candidat.

- La condition restaurée reste bornée par la définition.

- Le statut opérationnel n’est rétabli qu’avec un candidat d’inventaire valide.

- Le tick d’entretien est sauvegardé pour les diagnostics et politiques futures.

- Le commit commun empêche une réparation gratuite en cas de panne d’inventaire.

## 20. Événements et observations

> **[LECTURE] Événement committé — Structure de référence.**

```gdscript
class_name DomainChangedEvent
extends RefCounted

var event_id: StringName
var domain_id: StringName
var target_id: StringName
var event_kind: StringName
var logical_tick: int = 0
var domain_revision: int = 0
var cause_id: StringName
var source_system_id: StringName

func validate() -> Error:
    if not StableId.is_valid(event_id) or not StableId.is_valid(domain_id):
        return ERR_INVALID_DATA
    if not StableId.is_valid(event_kind) or not StableId.is_valid(cause_id):
        return ERR_INVALID_DATA
    if not StableId.is_valid(source_system_id):
        return ERR_INVALID_DATA
    if logical_tick < 0 or domain_revision < 0:
        return ERR_INVALID_DATA
    return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’événement décrit un fait déjà committé et ne transporte aucun candidat.

- La cible peut être une parcelle, un chantier ou un bâtiment.

- Le tick et la révision permettent d’ignorer une notification ancienne.

- Cause et système source assurent la traçabilité.

- Les scènes et agents ne peuvent pas modifier le domaine à travers l’événement.

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/application/domain_agent_observation_port.gd`.**

```gdscript
class_name DomainAgentObservationPort
extends RefCounted

class Observation:
    extends RefCounted

    var domain_id: StringName
    var domain_revision: int = 0
    var logical_tick: int = 0
    var open_worksite_ids: Array[StringName] = []
    var operational_building_ids: Array[StringName] = []
    var disabled_building_ids: Array[StringName] = []
    var available_actions: Array[StringName] = []

    func validate() -> Error:
        if not StableId.is_valid(domain_id):
            return ERR_INVALID_DATA
        if domain_revision < 0 or logical_tick < 0:
            return ERR_INVALID_DATA
        if open_worksite_ids.size() > 1024 or operational_building_ids.size() > 16384:
            return ERR_OUT_OF_MEMORY
        return OK

func snapshot_for(
    _actor_character_id: StringName,
    _domain_id: StringName,
    _logical_tick: int,
) -> Observation:
    return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’observation contient des identifiants et actions déjà filtrées, jamais les collections internes du dépôt.

- Les actions disponibles tiennent compte des droits sans exposer les règles politiques.

- Les agents transforment ces données en faits et requêtes selon le chapitre 17.

- Une décision d’agent repasse toujours par une commande validée.

- La taille des collections est bornée.

## 21. Présentation

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/presentation/domain_presentation_bridge.gd`.**

```gdscript
class_name DomainPresentationBridge
extends Node

signal refresh_domain_requested(domain_id: StringName, revision: int)

var _latest_revision: Dictionary[StringName, int] = {}

func on_domain_changed(event: DomainChangedEvent) -> void:
    if event == null or event.validate() != OK:
        return
    var known: int = int(_latest_revision.get(event.domain_id, -1))
    if event.domain_revision <= known:
        return
    _latest_revision[event.domain_id] = event.domain_revision
    refresh_domain_requested.emit(event.domain_id, event.domain_revision)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le pont accepte seulement un événement validé et postérieur à la dernière révision affichée.

- Le cache local sert à éviter les rafraîchissements anciens, pas à sauvegarder le domaine.

- Le signal demande une reconstruction visuelle depuis une lecture autorisée.

- Aucun bâtiment logique n’est créé ou supprimé par le nœud.

- La représentation peut être absente sans modifier l’existence des actifs.

## 22. Persistance

Sont persistés :

- les identités de domaines, parcelles, bâtiments et chantiers ;
- les liens de tenure et révisions de droits observées ;
- les régions et emplacements logiques des parcelles ;
- les occupations, états de bâtiments et conditions ;
- les matériaux livrés et le travail accompli ;
- les ticks, révisions et séquences d’événements ;
- les résultats idempotents récents ;
- la version du format.

Ne sont pas persistés :

- les définitions `.tres` ;
- les décisions politiques dérivées ;
- les snapshots écologiques ;
- les candidats d’inventaire ou d’économie ;
- les commandes en attente ;
- les transforms, meshes, collisions ou animations ;
- les observations d’agents ;
- les caches de présentation ;
- les recettes et ratios dérivés.

## 23. Codec strict

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/infrastructure/domain_snapshot_codec.gd`.**

```gdscript
class_name DomainSnapshotCodec
extends RefCounted

const FORMAT := "project-asteria-domains"
const VERSION := 1
const ROOT_KEYS := ["format", "version", "domains", "idempotency"]

class DecodeResult:
    extends RefCounted

    var code: Error = FAILED
    var prepared: Dictionary = {}
    var message: String = ""

    func is_success() -> bool:
        return code == OK

func decode(document: Dictionary, catalog: DomainCatalog) -> DecodeResult:
    if catalog == null:
        return _failure(ERR_UNCONFIGURED, "catalogue absent")
    if not _has_exact_keys(document, ROOT_KEYS):
        return _failure(ERR_INVALID_DATA, "clés racine invalides")
    if typeof(document.get("format")) != TYPE_STRING or String(document["format"]) != FORMAT:
        return _failure(ERR_FILE_UNRECOGNIZED, "format inconnu")
    if typeof(document.get("version")) != TYPE_INT or int(document["version"]) != VERSION:
        return _failure(ERR_FILE_UNRECOGNIZED, "version inconnue")
    var prepared := _decode_all(document, catalog)
    if prepared == null or _validate_cross_references(prepared, catalog) != OK:
        return _failure(ERR_INVALID_DATA, "snapshot de domaines invalide")
    var result := DecodeResult.new()
    result.code = OK
    result.prepared = prepared
    return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le codec exige le format, la version et exactement les clés prévues.

- Toutes les sections sont décodées dans une structure candidate avant mutation.

- Les références vers définitions, parcelles, bâtiments et chantiers sont recoupées.

- Les entiers suivent la plage JSON sûre du chapitre 9.

- `DecodeResult` distingue un document vide valide d’un échec.

## 24. Section de sauvegarde

> **[VSC] Visual Studio Code — Créer : `res://src/features/domains/infrastructure/domain_save_section.gd`.**

```gdscript
class_name DomainSaveSection
extends SaveSection

var _repository: DomainRepository
var _catalog: DomainCatalog
var _codec := DomainSnapshotCodec.new()
var _prepared: Dictionary = {}
var _is_prepared := false

func section_id() -> StringName:
    return &"domains"

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
    cancel_restore()
    return OK

func cancel_restore() -> void:
    _prepared.clear()
    _is_prepared = false
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La section prépare tous les domaines avant de toucher au dépôt actif.

- Les données sont copiées à la préparation puis à l’application.

- Un échec d’une autre section permet d’annuler sans mutation partielle.

- Les définitions doivent être chargées avant les états vivants.

- Les droits politiques seront revalidés par leurs ports après restauration.

## 25. Scène pédagogique

La scène `ch24_domains_demo.tscn` doit montrer :

1. un domaine comportant deux parcelles ;
2. un lien de tenure valide et un droit refusé ;
3. un site compatible et un site incompatible ;
4. l’ouverture d’un chantier avec coût préparé ;
5. une livraison partielle de matériaux ;
6. une surlivraison refusée ;
7. une progression de travail avant matériaux complets ;
8. un chantier prêt puis un bâtiment achevé ;
9. une production atomique avec l’inventaire ;
10. une production refusée par condition insuffisante ;
11. une dégradation puis un entretien ;
12. une dématérialisation visuelle sans suppression du bâtiment ;
13. une sauvegarde et restauration des révisions et résultats idempotents.

## 26. Modes Solo et Studio

### 26.1 Mode Solo

- quelques dizaines de domaines ;
- définitions `.tres` locales ;
- services sur le thread principal ;
- commits multi-autorités orchestrés par le point de composition ;
- historique idempotent borné ;
- scène pédagogique unique ;
- aucun service IA obligatoire.

### 26.2 Mode Studio

- catalogues versionnés et revus ;
- outils de visualisation des parcelles et occupations ;
- simulateurs de chantiers et productions ;
- tests de propriété sur capacités, quantités et révisions ;
- migrations de snapshots ;
- télémétrie des commits et refus ;
- scénarios de concurrence ;
- séparation des responsabilités de conception, économie et gameplay.

Le Mode Studio renforce les outils, les validations et l’observabilité. Il ne crée pas un gestionnaire global capable d’écrire tous les systèmes.

## 27. Budgets, sécurité et diagnostics

| Élément | Borne pédagogique |
|---|---:|
| domaines | 4 096 |
| parcelles par domaine | 4 096 |
| bâtiments par domaine | 16 384 |
| chantiers ouverts par domaine | 1 024 |
| matériaux par recette | 64 |
| recettes de production par bâtiment | 64 |
| cycles de production par commande | 1 000 |
| résultats idempotents récents | 4 096 |

Journaliser les identités, ticks, révisions attendues et constatées, décisions d’accès, site utilisé, quantités agrégées, progression, condition, durée matérielle du commit et statut final. Ne pas journaliser le contenu complet des inventaires, les payloads de paiement, les snapshots politiques ou les sorties génératives brutes.

## 28. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 28.1 Utiliser un nœud comme autorité du bâtiment

**Symptôme ou risque :** Supprimer la scène détruit le bâtiment sauvegardé.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
building_exists = is_instance_valid(building_node)
if not building_exists:
    repository.delete(building_id)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi cet exemple est fautif : Le nœud actif devient l’autorité d’un actif qui doit exister hors écran.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var building := domain_repository.get_domain(domain_id).buildings.get(building_id)
var visible := presentation_registry.has(building_id)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi la correction fonctionne : L’état logique et la représentation sont lus séparément ; masquer la scène ne supprime rien.

### 28.2 Déduire un droit depuis la relation sociale

**Symptôme ou risque :** Une forte confiance accorde implicitement un droit de construire.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if social.trust > 80:
    start_worksite(command)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi cet exemple est fautif : Une perception sociale remplace une décision juridique versionnée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var decision := rights_port.decide(actor_id, domain_id, action_id, logical_tick)
if decision.status == DomainRightsPort.Decision.Status.ALLOW:
    start_worksite(command)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi la correction fonctionne : Le chapitre 23 reste l’unique autorité de l’autorisation.

### 28.3 Consommer les matériaux avant le candidat de domaine

**Symptôme ou risque :** Une panne après retrait laisse le chantier incomplet et les matériaux perdus.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
inventory.consume(materials)
worksite.delivered_materials = materials
repository.replace_domain(candidate)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi cet exemple est fautif : Les autorités sont mutées séquentiellement sans rollback garanti.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var inventory_candidate := inventory_port.prepare_material_delivery(command, remaining)
var domain_candidate := prepare_delivery(command)
commit_port.commit_with_external_candidates(domain_candidate, revision, inventory_candidate, null, result, command_id, fingerprint)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi la correction fonctionne : Les deux candidats sont préparés puis committés comme un seul lot.

### 28.4 Confondre livraison et progression de travail

**Symptôme ou risque :** Livrer les derniers matériaux achève immédiatement le bâtiment.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if all_materials_delivered:
    complete_building()
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi cet exemple est fautif : La recette distingue pourtant matériaux et travail requis.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if all_materials_delivered and completed_work_units == required_work_units:
    worksite.status = WorksiteState.Status.READY_TO_COMPLETE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi la correction fonctionne : L’état prêt exige les deux conditions avant une commande d’achèvement séparée.

### 28.5 Utiliser un nombre flottant pour la progression

**Symptôme ou risque :** Deux replays peuvent arrondir différemment la progression.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
progress += delta * worker_speed
if progress >= 1.0:
    complete_building()
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi cet exemple est fautif : Le contrat d’arrondi et la valeur persistée sont implicites.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
worksite.completed_work_units += granted_work_units
var progress_bp := DomainMath.ratio_basis_points(worksite.completed_work_units, recipe.required_work_units)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi la correction fonctionne : Le travail et le ratio sont entiers, bornés et sérialisables.

### 28.6 Fixer un coût dans le bâtiment vivant

**Symptôme ou risque :** Le prix devient une propriété persistante de l’actif.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
building.construction_price = 1250
wallet.balance -= building.construction_price
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi cet exemple est fautif : Le domaine reprend l’autorité monétaire et mélange conception, état et économie.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var recipe := catalog.get_construction(building_definition.construction_recipe_id)
var cost_candidate := economy_port.prepare_construction_cost(command, recipe.optional_currency_id, recipe.optional_cost_minor)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi la correction fonctionne : La recette fournit une donnée validée et l’économie prépare les écritures.

### 28.7 Produire les extrants avant de consommer les intrants

**Symptôme ou risque :** Une panne intermédiaire duplique les objets produits.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
inventory.add_outputs(outputs)
inventory.remove_inputs(inputs)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi cet exemple est fautif : Les deux effets sont appliqués dans un ordre observable et non atomique.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var mutation := inventory_port.prepare_production_exchange(command, inputs, outputs)
commit_port.commit_with_external_candidates(domain_candidate, revision, mutation, null, result, command_id, fingerprint)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi la correction fonctionne : Un seul candidat d’inventaire porte consommation et production.

### 28.8 Utiliser le temps réel pour l’entretien

**Symptôme ou risque :** Changer l’horloge de l’ordinateur modifie l’état du bâtiment.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
building.last_maintenance_tick = int(Time.get_unix_time_from_system())
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi cet exemple est fautif : Le temps réel ne fait pas partie de la simulation sauvegardée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
building.last_maintenance_tick = world_clock.logical_tick
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi la correction fonctionne : Le tick logique est persisté, non décroissant et commun aux systèmes.

### 28.9 Autoriser une action en absence de décision

**Symptôme ou risque :** Une panne du service politique ouvre l’accès au domaine.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var decision := rights_port.decide(actor_id, domain_id, action_id, tick)
if decision == null or decision.status != DENY:
    run_production(command)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi cet exemple est fautif : Tous les états autres que refus explicite deviennent autorisés.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var decision := rights_port.decide(actor_id, domain_id, action_id, tick)
if decision != null and decision.status == DomainRightsPort.Decision.Status.ALLOW:
    run_production(command)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi la correction fonctionne : Seul `ALLOW` ouvre l’action ; absence et indétermination restent fermées.

### 28.10 Laisser une sortie IA achever un chantier

**Symptôme ou risque :** Un texte génératif modifie directement le domaine persistant.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if ai_response["worksite_complete"]:
    worksite.status = WorksiteState.Status.COMPLETED
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi cet exemple est fautif : La sortie non fiable contourne matériaux, travail, droits, révisions et idempotence.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var suggestion := ai_gateway.suggest_domain_action(summary)
var command := domain_suggestion_policy.to_validated_command(suggestion)
if command != null:
    construction_service.advance_worksite(command)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Pourquoi la correction fonctionne : La suggestion devient au mieux une commande typée qui repasse par toutes les validations.

## 29. Tests à préparer

### 29.1 Tests unitaires

- identifiants de domaine ;
- validation des définitions ;
- liens de tenure ouverts et fermés ;
- capacité de parcelle ;
- progression en points de base ;
- besoins restants en matériaux ;
- état prêt à achever ;
- condition et statuts du bâtiment ;
- multiplication des recettes ;
- codec strict et références croisées.

### 29.2 Tests d’intégration

- ouverture de chantier autorisée ;
- refus de droit et décision expirée ;
- site incompatible ;
- coût économique indisponible ;
- livraison partielle puis complète ;
- deux livraisons concurrentes ;
- travail complet avant matériaux ;
- matériaux complets avant travail ;
- achèvement unique et retry idempotent ;
- production atomique ;
- entretien atomique ;
- sauvegarde et restauration.

### 29.3 Simulations

- 1, 64 et 4 096 domaines ;
- 1, 256 et 4 096 parcelles par domaine ;
- 1, 1 024 et 16 384 bâtiments ;
- 1 à 1 000 cycles de production ;
- chantiers concurrents sur une même parcelle ;
- 10 000 jours de dégradation et entretien ;
- replays avec comparaison des snapshots ;
- pannes injectées à chaque étape d’un commit multi-autorités.

## 30. Réserves runtime

Cette revue statique ne prouve pas :

- le passage de tous les extraits dans le parseur Godot 4.7.1 ;
- le comportement de toutes les collections typées ;
- l’atomicité réelle entre domaine, inventaire et économie ;
- l’adaptateur politique de droits ;
- l’adaptateur écologique de site ;
- les performances aux bornes maximales ;
- l’équilibrage des coûts, travaux, productions et entretiens ;
- l’instanciation de la scène pédagogique ;
- l’exécution du codec et de la restauration ;
- la reproductibilité interplateforme ;
- la génération d’un PDF intermédiaire.

## 31. Sources techniques

- [Godot 4.7 — `Resource`](https://docs.godotengine.org/en/4.7/classes/class_resource.html)
- [Godot 4.7 — `RefCounted`](https://docs.godotengine.org/en/4.7/classes/class_refcounted.html)
- [Godot 4.7 — `Dictionary`](https://docs.godotengine.org/en/4.7/classes/class_dictionary.html)
- [Godot 4.7 — `Array`](https://docs.godotengine.org/en/4.7/classes/class_array.html)
- [Godot 4.7 — `StringName`](https://docs.godotengine.org/en/4.7/classes/class_stringname.html)
- [Godot 4.7 — `Time`](https://docs.godotengine.org/en/4.7/classes/class_time.html)
- [Godot 4.7 — bases de GDScript](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/gdscript_basics.html)
- [Chapitre 9 — Sauvegardes, chargements et compatibilité](CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md)
- [Chapitre 17 — Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md)
- [Chapitre 20 — Inventaire et réputation des objets](CHAPITRE-20-Inventaire-et-reputation-des-objets.md)
- [Chapitre 21 — Économie](CHAPITRE-21-Economie.md)
- [Chapitre 22 — Monde vivant et simulation écologique](CHAPITRE-22-Monde-vivant-et-simulation-ecologique.md)
- [Chapitre 23 — Politique, factions et justice](CHAPITRE-23-Politique-factions-et-justice.md)

## 32. Synthèse opérationnelle pour Project Asteria

Le système de domaines de `Project Asteria` retient les décisions suivantes :

1. domaines, parcelles, bâtiments et chantiers utilisent des identifiants stables ;
2. définitions de conception et états vivants restent séparés ;
3. les parcelles sont logiques et indépendantes des scènes ;
4. les droits politiques sont référencés et revalidés, jamais recréés ;
5. seul un statut politique `ALLOW` autorise une action protégée ;
6. les contraintes de site proviennent de snapshots écologiques validés ;
7. la parcelle réserve une capacité lors de l’ouverture du chantier ;
8. matériaux livrés et travail accompli restent deux dimensions distinctes ;
9. la progression utilise des entiers et des points de base ;
10. un bâtiment n’existe qu’après un achèvement committé ;
11. l’absence de représentation 3D ne supprime aucun actif ;
12. l’inventaire prépare consommation de matériaux, intrants et extrants ;
13. l’économie prépare les coûts et conserve les écritures ;
14. les commits multi-autorités revalident toutes les révisions ;
15. les commandes sont idempotentes et lient identité, empreinte et résultat ;
16. production et entretien exigent un bâtiment compatible et suffisamment fonctionnel ;
17. la dégradation utilise le tick logique et une arithmétique entière ;
18. les événements sont émis uniquement après commit ;
19. les agents reçoivent des observations et soumettent des commandes ;
20. une sortie IA reste consultative ;
21. le snapshot conserve actifs, chantiers, conditions, révisions et résultats idempotents ;
22. définitions, décisions dérivées, candidats, scènes et caches restent hors de la sauvegarde.
