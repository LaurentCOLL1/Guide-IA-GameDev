---
title: "Livre II — Chapitre 23 : Politique, factions et justice"
id: "DOC-L2-CH23"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 23
last-verified: "2026-07-21T04:38:43+02:00"
audit-status: "complete"
audit-date: "2026-07-21T04:38:43+02:00"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-23.md"
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

# Politique, factions et justice

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH23`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  

> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-23.md`.

## 1. Rôle du chapitre

Les systèmes précédents savent représenter des individus, des relations, des familles, des agents, des combats, des objets, une économie et un monde vivant. Ils ne possèdent cependant aucune autorité institutionnelle capable de dire qui appartient à une faction, qui exerce un mandat, quelle loi est applicable, quel droit autorise une action, comment une infraction est instruite ou quelle sanction a été décidée.

Ce chapitre construit la couche **politique et judiciaire** de `Project Asteria`. Il définit :

- des institutions et factions identifiées ;
- des rangs, fonctions et mandats datés en ticks logiques ;
- des adhésions et statuts institutionnels séparés des relations sociales ;
- un recueil de lois versionnées et immuables après promulgation ;
- des demandes d’autorisation produisant une décision explicable ;
- des infractions, dossiers, preuves, enquêtes et décisions ;
- des sanctions préparées avec les systèmes propriétaires concernés ;
- une persistance stricte et une restauration préparée.

Le système doit garantir que :

- une faction ne modifie pas directement un personnage, une relation, un portefeuille, un objet ou une région ;
- une loi promulguée conserve sa version, sa période d’effet et sa provenance ;
- une autorisation ne dépend jamais d’un nom affiché ou d’un nœud actif ;
- une accusation n’est pas un verdict ;
- une preuve reste distincte du fait qu’elle prétend soutenir ;
- une sanction multi-systèmes est préparée puis committée comme un lot ;
- une sortie IA peut suggérer une enquête ou un texte, mais ne peut ni promulguer une loi ni condamner un personnage.

## 2. Prérequis

Le lecteur doit avoir parcouru :

- le chapitre 4 pour l’architecture feature-first ;
- le chapitre 5 pour les services, ports et unités de travail ;
- le chapitre 7 pour les `Resource`, catalogues et identifiants stables ;
- le chapitre 9 pour les snapshots et restaurations préparées ;
- le chapitre 14 pour les identités de personnages ;
- le chapitre 15 pour les relations sociales orientées ;
- le chapitre 16 pour les liens familiaux ;
- le chapitre 17 pour les agents et commandes validées ;
- le chapitre 20 pour la propriété et la garde des objets ;
- le chapitre 21 pour les portefeuilles, paiements et amendes ;
- le chapitre 22 pour les régions logiques et l’horloge globale.

## 3. Périmètre et frontières

Ce chapitre couvre :

- les définitions d’institutions, factions, rangs et fonctions ;
- les adhésions, rangs détenus et états institutionnels ;
- les mandats, nominations, révocations et fins de mandat ;
- les lois versionnées, périodes d’effet et juridictions ;
- les droits, permissions, interdictions et décisions d’accès ;
- les infractions déclarées et leurs identités causales ;
- les preuves structurées avec provenance et chaîne de garde logique ;
- les dossiers judiciaires, enquêtes, audiences et verdicts ;
- les sanctions institutionnelles et leur coordination ;
- les événements politiques et judiciaires ;
- les observations destinées aux agents et à la narration ;
- la persistance.

Il ne couvre pas :

- les perceptions personnelles, l’affinité ou la confiance ;
- la parenté, l’héritage familial ou la succession biologique ;
- les décisions internes des agents ;
- les dégâts, états de combat ou décès ;
- la propriété et le transfert des objets ;
- les prix, portefeuilles ou écritures comptables ;
- les populations et ressources écologiques ;
- la propriété foncière, les bâtiments et chaînes de production ;
- les quêtes, scènes narratives ou conséquences scénarisées ;
- le multijoueur et l’autorité réseau ;
- l’équilibrage final des institutions et peines.

> **Frontière essentielle :** la politique possède institutions, adhésions, mandats, lois, dossiers et décisions. Les autres systèmes restent propriétaires des identités, perceptions, parentés, objets, monnaies, régions, bâtiments et récits.

## 4. Chaîne d’autorité

> **[LECTURE] Flux politique et judiciaire — Ne pas saisir.**

```text
PoliticalCommand
    ↓ validation de forme et d'identité
PoliticalService / JusticeService
    ├── relit les agrégats et révisions
    ├── demande les autorisations externes
    ├── prépare des copies détachées
    ├── produit une décision explicable
    └── prépare les effets externes
            ↓
PoliticalJusticeCommitPort
    ├── revalide toutes les révisions
    ├── committe les agrégats propriétaires
    └── enregistre identité, empreinte et résultat
            ↓
événements typés après commit
            ↓
agents, présentation et narration
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Une commande exprime une intention sans imposer le résultat.
- Les services relisent les autorités concernées et ne travaillent que sur des copies.
- Les ports externes préparent leurs propres candidats sans céder leurs invariants.
- Le commit coordonné empêche une sanction partiellement appliquée.
- Les événements décrivent uniquement un fait déjà committé.

## 5. Architecture retenue

> **[LECTURE] Arborescence cible — Ne pas créer depuis un terminal.**

```text
res://src/features/politics/
├── domain/
│   ├── political_id.gd
│   ├── institution_definition.gd
│   ├── faction_definition.gd
│   ├── rank_definition.gd
│   ├── office_definition.gd
│   ├── law_definition.gd
│   ├── membership_state.gd
│   ├── mandate_state.gd
│   ├── faction_state.gd
│   ├── law_book_state.gd
│   ├── political_command_result.gd
│   ├── infraction_report_command.gd
│   ├── evidence_record.gd
│   ├── justice_case_state.gd
│   ├── verdict_decision.gd
│   └── sanction_plan.gd
├── application/
│   ├── political_catalog.gd
│   ├── political_repository.gd
│   ├── political_identity_port.gd
│   ├── political_region_port.gd
│   ├── membership_service.gd
│   ├── mandate_service.gd
│   ├── legislative_service.gd
│   ├── authorization_context.gd
│   ├── political_authorization_service.gd
│   ├── justice_repository.gd
│   ├── political_causal_event_port.gd
│   ├── justice_intake_service.gd
│   ├── evidence_source_port.gd
│   ├── investigation_service.gd
│   ├── justice_service.gd
│   ├── sanction_economy_port.gd
│   ├── sanction_inventory_port.gd
│   ├── sanction_character_port.gd
│   ├── sanction_domain_port.gd
│   ├── political_justice_commit_port.gd
│   ├── political_agent_observation_port.gd
│   └── political_narrative_event_port.gd
├── infrastructure/
│   ├── political_snapshot_section_decoder.gd
│   ├── political_snapshot_codec.gd
│   ├── political_restore_commit_port.gd
│   └── political_save_section.gd
└── presentation/
    └── political_presentation_bridge.gd

res://data/politics/
├── institutions/
├── factions/
├── ranks/
├── offices/
├── laws/
└── sanctions/

res://scenes/learning/
├── ch23_politics_justice_demo.tscn
└── ch23_politics_justice_demo.gd
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `domain` contient les définitions, états, commandes et décisions indépendants des scènes.
- `application` orchestre les politiques et les ports vers les autres autorités.
- `infrastructure` encode seulement les données durables.
- `presentation` transforme les résultats committés en retour visuel.
- Les données de conception restent séparées des adhésions, mandats et dossiers vivants.

## 6. Vocabulaire

Une **institution** est une organisation politique ou judiciaire durable : conseil, cité, ordre, tribunal ou administration.

Une **faction** est un groupe institutionnel auquel des personnages peuvent appartenir. Elle peut dépendre d’une institution sans se confondre avec elle.

Un **rang** exprime une position durable dans une faction. Une **fonction** décrit un rôle institutionnel susceptible d’être exercé pendant un mandat.

Un **mandat** relie un titulaire, une fonction, une juridiction et un intervalle logique.

Une **loi** est une règle de conception versionnée, promulguée dans un recueil vivant avec une période d’effet.

Une **autorisation** est une décision calculée à partir d’une action, d’un acteur, d’une juridiction, des lois applicables et des droits institutionnels.

Une **infraction rapportée** est une allégation structurée. Elle ne prouve ni la matérialité des faits ni la culpabilité.

Une **preuve** est un élément identifié, sourcé et daté, dont la recevabilité et le poids sont évalués par le système judiciaire.

Un **dossier** agrège les allégations, preuves, participants, étapes et décisions d’une affaire.

Une **sanction** est une conséquence institutionnelle décidée. Les effets sur monnaie, objets, personnages ou domaines restent exécutés par leurs systèmes propriétaires.

## 7. Identifiants politiques

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/political_id.gd`.**

```gdscript
class_name PoliticalId
extends RefCounted

const INSTITUTION_PREFIX := "politics.institution."
const FACTION_PREFIX := "politics.faction."
const RANK_PREFIX := "politics.rank."
const OFFICE_PREFIX := "politics.office."
const LAW_PREFIX := "politics.law."
const MEMBERSHIP_PREFIX := "politics.membership."
const MANDATE_PREFIX := "politics.mandate."
const CASE_PREFIX := "justice.case."
const EVIDENCE_PREFIX := "justice.evidence."
const DECISION_PREFIX := "justice.decision."
const COMMAND_PREFIX := "politics.command."

static func institution(slug: String) -> StringName:
	return _from_slug(INSTITUTION_PREFIX, slug)

static func faction(slug: String) -> StringName:
	return _from_slug(FACTION_PREFIX, slug)

static func rank(slug: String) -> StringName:
	return _from_slug(RANK_PREFIX, slug)

static func office(slug: String) -> StringName:
	return _from_slug(OFFICE_PREFIX, slug)

static func law(slug: String) -> StringName:
	return _from_slug(LAW_PREFIX, slug)

static func membership(uuid_text: String) -> StringName:
	return _from_slug(MEMBERSHIP_PREFIX, uuid_text)

static func mandate(uuid_text: String) -> StringName:
	return _from_slug(MANDATE_PREFIX, uuid_text)

static func justice_case(uuid_text: String) -> StringName:
	return _from_slug(CASE_PREFIX, uuid_text)

static func evidence(uuid_text: String) -> StringName:
	return _from_slug(EVIDENCE_PREFIX, uuid_text)

static func decision(uuid_text: String) -> StringName:
	return _from_slug(DECISION_PREFIX, uuid_text)

static func command(uuid_text: String) -> StringName:
	return _from_slug(COMMAND_PREFIX, uuid_text)

static func _from_slug(prefix: String, value: String) -> StringName:
	var normalized := value.strip_edges().to_lower().replace("-", "_")
	if normalized.is_empty():
		return &""
	for character: String in normalized:
		var letter := character >= "a" and character <= "z"
		var digit := character >= "0" and character <= "9"
		if not letter and not digit and character != "_":
			return &""
	return StringName(prefix + normalized)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Chaque famille possède un préfixe afin d’éviter les collisions entre concepts.
- Les méthodes couvrent aussi les identités vivantes : adhésions, mandats, dossiers, preuves et décisions.
- Les identifiants sont indépendants des noms traduits et des chemins de fichiers.
- La normalisation refuse tout caractère non prévu plutôt que de le supprimer silencieusement.
- Les identités de personnages continuent d’utiliser `CharacterId`, tandis que les commandes possèdent leur propre espace pour l’idempotence.

## 8. Définition d’une institution

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/institution_definition.gd`.**

```gdscript
class_name InstitutionDefinition
extends Resource

@export var institution_id: StringName
@export var display_name_key: StringName
@export var institution_kind: StringName
@export var default_jurisdiction_ids: Array[StringName] = []
@export var enabled_faction_ids: Array[StringName] = []

func validate() -> Error:
	if not StableId.is_valid(institution_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(display_name_key):
		return ERR_INVALID_DATA
	if not StableId.is_valid(institution_kind):
		return ERR_INVALID_DATA
	if default_jurisdiction_ids.size() > 256:
		return ERR_OUT_OF_MEMORY
	if enabled_faction_ids.is_empty() or enabled_faction_ids.size() > 128:
		return ERR_INVALID_DATA
	if _validate_unique_ids(default_jurisdiction_ids) != OK:
		return ERR_INVALID_DATA
	return _validate_unique_ids(enabled_faction_ids)

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

- L’institution est une `Resource` de conception partagée et immuable pendant le gameplay.
- Les juridictions sont des références logiques ; elles ne donnent aucune propriété sur les régions.
- Les factions autorisées sont déclarées explicitement et sans doublon.
- `institution_kind` permet de distinguer conseil, tribunal ou administration sans charger un script depuis les données.
- Aucun membre, mandat ou dossier vivant n’est stocké dans la définition.

## 9. Définition d’une faction

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/faction_definition.gd`.**

```gdscript
class_name FactionDefinition
extends Resource

@export var faction_id: StringName
@export var institution_id: StringName
@export var display_name_key: StringName
@export var rank_ids: Array[StringName] = []
@export var office_ids: Array[StringName] = []
@export var maximum_members: int = 1000000

func validate() -> Error:
	if not StableId.is_valid(faction_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(institution_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(display_name_key):
		return ERR_INVALID_DATA
	if maximum_members < 1 or maximum_members > 1000000:
		return ERR_INVALID_DATA
	if rank_ids.is_empty() or rank_ids.size() > 64:
		return ERR_INVALID_DATA
	if office_ids.size() > 64:
		return ERR_OUT_OF_MEMORY
	if _validate_unique_ids(rank_ids) != OK:
		return ERR_INVALID_DATA
	return _validate_unique_ids(office_ids)

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

- Une faction dépend d’une institution par identifiant, jamais par référence mutable.
- Les rangs et fonctions autorisés sont bornés.
- La capacité maximale protège les scénarios et les snapshots pathologiques.
- L’ordre politique n’est pas déduit d’une relation sociale ou d’un nom.
- Les adhésions vivantes restent dans `FactionState`.

## 10. Rangs et fonctions

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/rank_definition.gd`.**

```gdscript
class_name RankDefinition
extends Resource

@export var rank_id: StringName
@export var display_name_key: StringName
@export var authority_level: int = 0
@export var granted_right_ids: Array[StringName] = []

func validate() -> Error:
	if not StableId.is_valid(rank_id) or not StableId.is_valid(display_name_key):
		return ERR_INVALID_DATA
	if authority_level < 0 or authority_level > 100:
		return ERR_INVALID_DATA
	var seen: Dictionary[StringName, bool] = {}
	for right_id: StringName in granted_right_ids:
		if not StableId.is_valid(right_id) or seen.has(right_id):
			return ERR_INVALID_DATA
		seen[right_id] = true
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `authority_level` sert uniquement à comparer des rangs au sein de politiques qui le demandent.
- Les droits sont des identifiants déclaratifs, pas des appels de méthodes.
- Les doublons sont refusés afin qu’une décision d’accès reste explicable.
- Un rang ne modifie ni relation sociale ni statistiques de personnage.
- La définition ne contient aucun titulaire.

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/office_definition.gd`.**

```gdscript
class_name OfficeDefinition
extends Resource

@export var office_id: StringName
@export var display_name_key: StringName
@export var required_rank_ids: Array[StringName] = []
@export var granted_right_ids: Array[StringName] = []
@export var maximum_simultaneous_holders: int = 1
@export var mandate_duration_ticks: int = 0

func validate() -> Error:
	if not StableId.is_valid(office_id) or not StableId.is_valid(display_name_key):
		return ERR_INVALID_DATA
	if required_rank_ids.size() > 32 or granted_right_ids.size() > 64:
		return ERR_OUT_OF_MEMORY
	if maximum_simultaneous_holders < 1 or maximum_simultaneous_holders > 64:
		return ERR_INVALID_DATA
	if mandate_duration_ticks < 0 or mandate_duration_ticks > 9007199254740991:
		return ERR_INVALID_DATA
	if _validate_unique_ids(required_rank_ids) != OK:
		return ERR_INVALID_DATA
	return _validate_unique_ids(granted_right_ids)

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

- Une fonction décrit les conditions et droits d’un mandat sans désigner son titulaire.
- Une durée nulle signifie une fin explicite et non un mandat sans contrôle.
- Les titulaires simultanés sont bornés.
- Les droits de fonction s’ajoutent aux droits de rang seulement lors du calcul d’autorisation.
- La nomination demeure une commande validée.

## 11. Lois versionnées

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/law_definition.gd`.**

```gdscript
class_name LawDefinition
extends Resource

enum Effect {
	ALLOW,
	DENY,
	REQUIRE_RIGHT,
	REPORT_INFRACTION,
}

@export var law_id: StringName
@export var version: int = 1
@export var display_name_key: StringName
@export var action_id: StringName
@export var effect: Effect = Effect.DENY
@export var required_right_id: StringName
@export var infraction_type_id: StringName
@export var priority: int = 0

func validate() -> Error:
	if not StableId.is_valid(law_id) or not StableId.is_valid(display_name_key):
		return ERR_INVALID_DATA
	if version < 1 or version > 1000000:
		return ERR_INVALID_DATA
	if not StableId.is_valid(action_id):
		return ERR_INVALID_DATA
	if effect < Effect.ALLOW or effect > Effect.REPORT_INFRACTION:
		return ERR_INVALID_DATA
	if effect == Effect.REQUIRE_RIGHT and not StableId.is_valid(required_right_id):
		return ERR_INVALID_DATA
	if effect == Effect.REPORT_INFRACTION and not StableId.is_valid(infraction_type_id):
		return ERR_INVALID_DATA
	if priority < -10000 or priority > 10000:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Une loi possède une identité stable et un numéro de version distinct.
- `effect` limite les comportements à une énumération connue.
- Les champs conditionnels sont obligatoires seulement pour l’effet qui les utilise.
- La priorité est bornée et ne remplace pas l’ordre de promulgation.
- Une version promulguée ne sera jamais modifiée en place.

## 12. Catalogue politique

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/political_catalog.gd`.**

```gdscript
class_name PoliticalCatalog
extends RefCounted

var _institutions: Dictionary[StringName, InstitutionDefinition] = {}
var _factions: Dictionary[StringName, FactionDefinition] = {}
var _ranks: Dictionary[StringName, RankDefinition] = {}
var _offices: Dictionary[StringName, OfficeDefinition] = {}
var _laws: Dictionary[StringName, Dictionary] = {}

func register_institution(definition: InstitutionDefinition) -> Error:
	return _register_resource(_institutions, definition, definition.institution_id if definition != null else &"")

func register_faction(definition: FactionDefinition) -> Error:
	return _register_resource(_factions, definition, definition.faction_id if definition != null else &"")

func register_rank(definition: RankDefinition) -> Error:
	return _register_resource(_ranks, definition, definition.rank_id if definition != null else &"")

func register_office(definition: OfficeDefinition) -> Error:
	return _register_resource(_offices, definition, definition.office_id if definition != null else &"")

func register_law(definition: LawDefinition) -> Error:
	if definition == null or definition.validate() != OK:
		return ERR_INVALID_DATA
	var versions: Dictionary = _laws.get_or_add(definition.law_id, {})
	if versions.has(definition.version):
		return ERR_ALREADY_EXISTS
	versions[definition.version] = definition.duplicate(true)
	return OK

func validate_cross_references() -> Error:
	for faction: FactionDefinition in _factions.values():
		var institution := get_institution(faction.institution_id)
		if institution == null or faction.faction_id not in institution.enabled_faction_ids:
			return ERR_DOES_NOT_EXIST
		for rank_id: StringName in faction.rank_ids:
			if not _ranks.has(rank_id):
				return ERR_DOES_NOT_EXIST
		for office_id: StringName in faction.office_ids:
			if not _offices.has(office_id):
				return ERR_DOES_NOT_EXIST
	for office: OfficeDefinition in _offices.values():
		for rank_id: StringName in office.required_rank_ids:
			if not _ranks.has(rank_id):
				return ERR_DOES_NOT_EXIST
	return OK

func get_institution(institution_id: StringName) -> InstitutionDefinition:
	return _copy_resource(_institutions.get(institution_id)) as InstitutionDefinition

func get_faction(faction_id: StringName) -> FactionDefinition:
	return _copy_resource(_factions.get(faction_id)) as FactionDefinition

func get_rank(rank_id: StringName) -> RankDefinition:
	return _copy_resource(_ranks.get(rank_id)) as RankDefinition

func get_office(office_id: StringName) -> OfficeDefinition:
	return _copy_resource(_offices.get(office_id)) as OfficeDefinition

func get_law(law_id: StringName, version: int) -> LawDefinition:
	var versions := _laws.get(law_id) as Dictionary
	if versions == null:
		return null
	return _copy_resource(versions.get(version)) as LawDefinition

func latest_law_version(law_id: StringName) -> int:
	var versions := _laws.get(law_id) as Dictionary
	if versions == null or versions.is_empty():
		return 0
	var keys: Array = versions.keys()
	keys.sort()
	return int(keys.back())

func _register_resource(target: Dictionary, definition: Variant, stable_id: StringName) -> Error:
	if definition == null or definition.validate() != OK:
		return ERR_INVALID_DATA
	if not StableId.is_valid(stable_id):
		return ERR_INVALID_DATA
	if target.has(stable_id):
		return ERR_ALREADY_EXISTS
	target[stable_id] = definition.duplicate(true)
	return OK

func _copy_resource(value: Variant) -> Resource:
	var resource := value as Resource
	return null if resource == null else resource.duplicate(true)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les cinq familles de définitions sont enregistrées par des méthodes explicites et refusent les doublons.
- `_register_resource()` centralise la validation, l’identité stable et la copie profonde sans devenir un registre de services.
- `validate_cross_references()` s’exécute après le chargement complet et vérifie institution, factions, rangs et fonctions.
- Chaque lecture retourne une copie afin de préserver l’immuabilité pendant le gameplay.
- Les versions de loi restent groupées par identité ; `latest_law_version()` les trie avant de choisir la plus récente.

## 13. État d’adhésion

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/membership_state.gd`.**

```gdscript
class_name MembershipState
extends RefCounted

enum Status {
	ACTIVE,
	SUSPENDED,
	RESIGNED,
	EXPELLED,
}

var membership_id: StringName
var faction_id: StringName
var character_id: StringName
var rank_id: StringName
var status: Status = Status.ACTIVE
var joined_tick: int = 0
var ended_tick: int = -1
var revision: int = 0
var cause_id: StringName

func validate() -> Error:
	if not StableId.is_valid(membership_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(faction_id) or not CharacterId.is_valid(character_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(rank_id) or not StableId.is_valid(cause_id):
		return ERR_INVALID_DATA
	if status < Status.ACTIVE or status > Status.EXPELLED:
		return ERR_INVALID_DATA
	if joined_tick < 0 or revision < 0:
		return ERR_INVALID_DATA
	if status == Status.ACTIVE or status == Status.SUSPENDED:
		if ended_tick != -1:
			return ERR_INVALID_DATA
	elif ended_tick < joined_tick:
		return ERR_INVALID_DATA
	return OK

func duplicate_detached() -> MembershipState:
	var copy := MembershipState.new()
	for property_name: StringName in [
		&"membership_id", &"faction_id", &"character_id", &"rank_id",
		&"status", &"joined_tick", &"ended_tick", &"revision", &"cause_id",
	]:
		copy.set(property_name, get(property_name))
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Une adhésion est identifiée indépendamment du personnage et de la faction.
- La suspension conserve l’adhésion ouverte mais retire ses droits selon la politique.
- Une adhésion terminée possède un tick de fin qui ne précède pas l’entrée.
- `cause_id` rend l’entrée ou la dernière transition traçable.
- La copie détachée prépare un changement sans modifier l’état actif.

## 14. État d’un mandat

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/mandate_state.gd`.**

```gdscript
class_name MandateState
extends RefCounted

enum Status {
	ACTIVE,
	COMPLETED,
	REVOKED,
	VACANT,
}

var mandate_id: StringName
var institution_id: StringName
var faction_id: StringName
var office_id: StringName
var holder_character_id: StringName
var jurisdiction_id: StringName
var status: Status = Status.ACTIVE
var started_tick: int = 0
var scheduled_end_tick: int = -1
var actual_end_tick: int = -1
var revision: int = 0
var appointment_cause_id: StringName

func validate() -> Error:
	for value: StringName in [mandate_id, institution_id, faction_id, office_id]:
		if not StableId.is_valid(value):
			return ERR_INVALID_DATA
	if status == Status.ACTIVE and not CharacterId.is_valid(holder_character_id):
		return ERR_INVALID_DATA
	if status == Status.VACANT and not holder_character_id.is_empty():
		return ERR_INVALID_DATA
	if status not in [Status.ACTIVE, Status.VACANT]:
		if not holder_character_id.is_empty() and not CharacterId.is_valid(holder_character_id):
			return ERR_INVALID_DATA
	if not jurisdiction_id.is_empty() and not StableId.is_valid(jurisdiction_id):
		return ERR_INVALID_DATA
	if started_tick < 0 or revision < 0:
		return ERR_INVALID_DATA
	if scheduled_end_tick != -1 and scheduled_end_tick < started_tick:
		return ERR_INVALID_DATA
	if status == Status.ACTIVE and actual_end_tick != -1:
		return ERR_INVALID_DATA
	if status != Status.ACTIVE and actual_end_tick < started_tick:
		return ERR_INVALID_DATA
	return OK

func duplicate_detached() -> MandateState:
	var copy := MandateState.new()
	for property_name: StringName in [
		&"mandate_id", &"institution_id", &"faction_id", &"office_id",
		&"holder_character_id", &"jurisdiction_id", &"status", &"started_tick",
		&"scheduled_end_tick", &"actual_end_tick", &"revision",
		&"appointment_cause_id",
	]:
		copy.set(property_name, get(property_name))
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le mandat distingue une fin planifiée de sa fin réelle.
- Un mandat actif exige un titulaire valide ; un siège vacant conserve la fonction et la juridiction mais exige un titulaire vide.
- La juridiction est une référence logique validée par un port.
- La révocation ne supprime pas l’historique du mandat.
- Les droits sont dérivés de la fonction, du rang et de la période active.

## 15. Agrégat de faction

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/faction_state.gd`.**

```gdscript
class_name FactionState
extends RefCounted

const MAX_MEMBERSHIPS := 100000
const MAX_MANDATES := 4096

var faction_id: StringName
var revision: int = 0
var event_sequence: int = 0
var memberships: Dictionary[StringName, MembershipState] = {}
var active_membership_by_character: Dictionary[StringName, StringName] = {}
var mandates: Dictionary[StringName, MandateState] = {}

func validate(catalog: PoliticalCatalog) -> Error:
	if catalog == null:
		return ERR_UNCONFIGURED
	var definition := catalog.get_faction(faction_id)
	if definition == null:
		return ERR_DOES_NOT_EXIST
	if revision < 0 or event_sequence < 0:
		return ERR_INVALID_DATA
	if memberships.size() > MAX_MEMBERSHIPS or mandates.size() > MAX_MANDATES:
		return ERR_OUT_OF_MEMORY
	var active_seen: Dictionary[StringName, StringName] = {}
	for membership_id: StringName in memberships:
		var membership := memberships[membership_id] as MembershipState
		if membership == null or membership.membership_id != membership_id:
			return ERR_INVALID_DATA
		if membership.faction_id != faction_id or membership.validate() != OK:
			return ERR_INVALID_DATA
		if membership.rank_id not in definition.rank_ids:
			return ERR_INVALID_DATA
		if membership.status in [MembershipState.Status.ACTIVE, MembershipState.Status.SUSPENDED]:
			if active_seen.has(membership.character_id):
				return ERR_ALREADY_EXISTS
			active_seen[membership.character_id] = membership_id
	if not _same_index(active_seen, active_membership_by_character):
		return ERR_INVALID_DATA
	for mandate_id: StringName in mandates:
		var mandate := mandates[mandate_id] as MandateState
		if mandate == null or mandate.mandate_id != mandate_id:
			return ERR_INVALID_DATA
		if mandate.faction_id != faction_id or mandate.validate() != OK:
			return ERR_INVALID_DATA
		if mandate.institution_id != definition.institution_id:
			return ERR_INVALID_DATA
		if mandate.office_id not in definition.office_ids:
			return ERR_INVALID_DATA
	return OK

func duplicate_detached() -> FactionState:
	var copy := FactionState.new()
	copy.faction_id = faction_id
	copy.revision = revision
	copy.event_sequence = event_sequence
	for membership_id: StringName in memberships:
		copy.memberships[membership_id] = memberships[membership_id].duplicate_detached()
	copy.active_membership_by_character = active_membership_by_character.duplicate(true)
	for mandate_id: StringName in mandates:
		copy.mandates[mandate_id] = mandates[mandate_id].duplicate_detached()
	return copy

func _same_index(
	left: Dictionary[StringName, StringName],
	right: Dictionary[StringName, StringName],
) -> bool:
	if left.size() != right.size():
		return false
	for character_id: StringName in left:
		if right.get(character_id, &"") != left[character_id]:
			return false
	return true
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’agrégat vérifie d’abord que sa définition de faction existe dans le catalogue.
- Il garantit au plus une adhésion ouverte par personnage et recalcule l’index secondaire avant de le comparer clé par clé.
- Les clés sont recoupées avec les identifiants des valeurs ; chaque adhésion utilise un rang autorisé et chaque mandat l’institution et une fonction déclarées par la faction.
- `duplicate_detached()` copie profondément chaque état vivant et l’index, ce qui évite tout partage mutable avec l’agrégat actif.
- Les tailles et révisions sont validées avant chaque remplacement.

## 16. Recueil de lois vivant

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/law_book_state.gd`.**

```gdscript
class_name LawBookState
extends RefCounted

const MAX_ENACTMENTS := 100000

class Enactment:
	extends RefCounted
	var law_id: StringName
	var law_version: int = 1
	var institution_id: StringName
	var jurisdiction_id: StringName
	var enacted_tick: int = 0
	var effective_from_tick: int = 0
	var effective_until_tick: int = -1
	var promulgation_cause_id: StringName

	func validate() -> Error:
		if not StableId.is_valid(law_id) or law_version < 1:
			return ERR_INVALID_DATA
		if not StableId.is_valid(institution_id):
			return ERR_INVALID_DATA
		if not jurisdiction_id.is_empty() and not StableId.is_valid(jurisdiction_id):
			return ERR_INVALID_DATA
		if enacted_tick < 0 or effective_from_tick < enacted_tick:
			return ERR_INVALID_DATA
		if effective_until_tick != -1 and effective_until_tick < effective_from_tick:
			return ERR_INVALID_DATA
		if not StableId.is_valid(promulgation_cause_id):
			return ERR_INVALID_DATA
		return OK

	func duplicate_detached() -> Enactment:
		var copy := Enactment.new()
		copy.law_id = law_id
		copy.law_version = law_version
		copy.institution_id = institution_id
		copy.jurisdiction_id = jurisdiction_id
		copy.enacted_tick = enacted_tick
		copy.effective_from_tick = effective_from_tick
		copy.effective_until_tick = effective_until_tick
		copy.promulgation_cause_id = promulgation_cause_id
		return copy

var revision: int = 0
var enactments: Array[Enactment] = []

func validate(catalog: PoliticalCatalog) -> Error:
	if catalog == null or revision < 0:
		return ERR_INVALID_DATA
	if enactments.size() > MAX_ENACTMENTS:
		return ERR_OUT_OF_MEMORY
	var seen: Dictionary[String, bool] = {}
	for enactment: Enactment in enactments:
		if enactment == null or enactment.validate() != OK:
			return ERR_INVALID_DATA
		if catalog.get_institution(enactment.institution_id) == null:
			return ERR_DOES_NOT_EXIST
		if catalog.get_law(enactment.law_id, enactment.law_version) == null:
			return ERR_DOES_NOT_EXIST
		var key := "%s|%d|%s|%s|%d" % [
			enactment.law_id,
			enactment.law_version,
			enactment.institution_id,
			enactment.jurisdiction_id,
			enactment.effective_from_tick,
		]
		if seen.has(key):
			return ERR_ALREADY_EXISTS
		seen[key] = true
	return OK

func active_at(jurisdiction_id: StringName, logical_tick: int) -> Array[Enactment]:
	var result: Array[Enactment] = []
	if logical_tick < 0:
		return result
	for enactment: Enactment in enactments:
		if enactment.jurisdiction_id not in [&"", jurisdiction_id]:
			continue
		if logical_tick < enactment.effective_from_tick:
			continue
		if enactment.effective_until_tick != -1 and logical_tick > enactment.effective_until_tick:
			continue
		result.append(enactment.duplicate_detached())
	result.sort_custom(_sort_enactments)
	return result

func duplicate_detached() -> LawBookState:
	var copy := LawBookState.new()
	copy.revision = revision
	for enactment: Enactment in enactments:
		copy.enactments.append(enactment.duplicate_detached())
	return copy

func _sort_enactments(left: Enactment, right: Enactment) -> bool:
	if left.law_id != right.law_id:
		return String(left.law_id) < String(right.law_id)
	if left.law_version != right.law_version:
		return left.law_version < right.law_version
	return left.effective_from_tick < right.effective_from_tick
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Une promulgation référence une version de définition déjà enregistrée et exige une cause stable.
- `validate()` recoupe institution et version de loi, borne le nombre d’entrées et refuse les doublons métier.
- Les périodes d’effet utilisent l’horloge logique du chapitre 22 ; une juridiction vide représente une portée globale explicitement prévue.
- `active_at()` retourne des copies dans un ordre déterministe, sans exposer les promulgations internes.
- `duplicate_detached()` permet au service législatif de préparer une nouvelle promulgation sans réécrire l’historique actif.

## 17. Dépôt politique

> **[LECTURE] Contrat du dépôt politique — Structure de référence.**

```gdscript
class_name PoliticalRepository
extends RefCounted

func get_faction(_faction_id: StringName) -> FactionState:
	return null

func get_law_book() -> LawBookState:
	return null

func all_faction_ids_sorted() -> Array[StringName]:
	return []

func find_command_result(
	_command_id: StringName,
	_fingerprint: String,
) -> PoliticalCommandResult:
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

- Les lectures doivent retourner des copies détachées.
- Les identifiants de factions sont triés pour les traitements reproductibles.
- Les résultats de commandes sont persistés pour l’idempotence.
- Le dépôt ne décide ni adhésion, ni autorisation, ni verdict.
- `replace_all()` est réservé à une restauration complète déjà validée.

## 18. Ports d’identité et de juridiction

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/political_identity_port.gd`.**

```gdscript
class_name PoliticalIdentityPort
extends RefCounted

func character_exists(_character_id: StringName) -> bool:
	return false

func character_is_eligible(
	_character_id: StringName,
	_requirement_id: StringName,
	_logical_tick: int,
) -> bool:
	return false
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le système politique valide une identité sans lire un registre de nœuds actifs.
- L’éligibilité reste un contrat explicite et borné.
- Le port ne retourne ni état runtime ni relations sociales.
- Une absence de scène ne rend pas un personnage inexistant.
- Une sortie IA ne peut pas répondre à la place de ce port.

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/political_region_port.gd`.**

```gdscript
class_name PoliticalRegionPort
extends RefCounted

func jurisdiction_exists(_jurisdiction_id: StringName) -> bool:
	return false

func contains_region(
	_jurisdiction_id: StringName,
	_region_id: StringName,
	_logical_tick: int,
) -> bool:
	return false
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le port traduit une juridiction vers les régions logiques sans donner accès aux populations ou ressources.
- Les frontières peuvent évoluer par tick logique.
- Le chapitre 22 reste propriétaire des régions écologiques.
- Le chapitre 24 pourra adapter les domaines et bâtiments sans déplacer cette frontière.
- Une juridiction inconnue est refusée avant toute décision.

## 19. Résultat d’une commande politique

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/political_command_result.gd`.**

```gdscript
class_name PoliticalCommandResult
extends RefCounted

enum Status {
	COMMITTED,
	REPLAYED,
	REJECTED_INVALID_COMMAND,
	REJECTED_NOT_FOUND,
	REJECTED_UNAUTHORIZED,
	REJECTED_STALE_REVISION,
	REJECTED_CONFLICT,
	REJECTED_CAPACITY,
	REJECTED_EXTERNAL_PREPARATION,
	REJECTED_IDEMPOTENCY_CONFLICT,
	REJECTED_INTERNAL,
}

var status: Status = Status.REJECTED_INTERNAL
var command_id: StringName
var aggregate_id: StringName
var decision_id: StringName
var message: String = ""

func is_success() -> bool:
	return status in [Status.COMMITTED, Status.REPLAYED]

func validate() -> Error:
	if status < Status.COMMITTED or status > Status.REJECTED_INTERNAL:
		return ERR_INVALID_DATA
	if is_success():
		if not StableId.is_valid(command_id) or not StableId.is_valid(aggregate_id):
			return ERR_INVALID_DATA
	else:
		if not command_id.is_empty() and not StableId.is_valid(command_id):
			return ERR_INVALID_DATA
		if not aggregate_id.is_empty() and not StableId.is_valid(aggregate_id):
			return ERR_INVALID_DATA
	if not decision_id.is_empty() and not StableId.is_valid(decision_id):
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le résultat distingue refus métier, conflit de révision, capacité et panne externe.
- `REPLAYED` confirme une commande déjà committée sans seconde mutation.
- Un succès exige la commande et l’agrégat ; `decision_id` devient obligatoire seulement pour une décision qui en produit une.
- Le résultat ne transporte aucun agrégat mutable.
- Le message reste descriptif et n’est pas utilisé comme code métier.

## 20. Commande d’adhésion

> **[LECTURE] Commande de référence — `membership_command.gd`.**

```gdscript
class_name MembershipCommand
extends RefCounted

enum Operation {
	JOIN,
	CHANGE_RANK,
	SUSPEND,
	RESIGN,
	EXPEL,
}

var command_id: StringName
var operation: Operation = Operation.JOIN
var faction_id: StringName
var membership_id: StringName
var character_id: StringName
var target_rank_id: StringName
var expected_faction_revision: int = 0
var expected_membership_revision: int = -1
var cause_id: StringName
var source_system_id: StringName
var logical_tick: int = 0
var command_fingerprint: String = ""

func validate() -> Error:
	if not StableId.is_valid(command_id) or not StableId.is_valid(faction_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(membership_id) or not CharacterId.is_valid(character_id):
		return ERR_INVALID_DATA
	if operation < Operation.JOIN or operation > Operation.EXPEL:
		return ERR_INVALID_DATA
	if not target_rank_id.is_empty() and not StableId.is_valid(target_rank_id):
		return ERR_INVALID_DATA
	if expected_faction_revision < 0 or expected_membership_revision < -1:
		return ERR_INVALID_DATA
	if not StableId.is_valid(cause_id) or not StableId.is_valid(source_system_id):
		return ERR_INVALID_DATA
	if logical_tick < 0 or command_fingerprint.is_empty():
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Une énumération limite les transitions possibles.
- L’identité d’adhésion est fournie pour rendre les retries déterministes.
- `expected_membership_revision = -1` est réservé à une création.
- La commande porte cause, système source, tick et empreinte.
- Elle ne contient aucune relation sociale ou donnée d’interface.

## 21. Service d’adhésion

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/membership_service.gd`.**

```gdscript
class_name MembershipService
extends RefCounted

var _catalog: PoliticalCatalog
var _repository: PoliticalRepository
var _identities: PoliticalIdentityPort
var _commit: PoliticalJusticeCommitPort

signal membership_committed(result: PoliticalCommandResult)

func execute(command: MembershipCommand) -> PoliticalCommandResult:
	if command == null or command.validate() != OK:
		return _command_result(PoliticalCommandResult.Status.REJECTED_INVALID_COMMAND, command)
	if _repository == null or _commit == null:
		return _command_result(PoliticalCommandResult.Status.REJECTED_INTERNAL, command)
	var replay := _repository.find_command_result(command.command_id, command.command_fingerprint)
	if replay != null:
		replay.status = PoliticalCommandResult.Status.REPLAYED
		return replay
	if _repository.has_conflicting_fingerprint(
		command.command_id,
		command.command_fingerprint,
	):
		return _command_result(
			PoliticalCommandResult.Status.REJECTED_IDEMPOTENCY_CONFLICT,
			command,
		)
	var candidate := prepare(command)
	if candidate == null:
		return _command_result(PoliticalCommandResult.Status.REJECTED_CONFLICT, command)
	var result := _command_result(PoliticalCommandResult.Status.COMMITTED, command)
	var code := _commit.commit_political(
		candidate,
		command.expected_faction_revision,
		result,
		command.command_id,
		command.command_fingerprint,
	)
	if code != OK:
		return _command_result(
			PoliticalCommandResult.Status.REJECTED_STALE_REVISION
			if code == ERR_BUSY
			else PoliticalCommandResult.Status.REJECTED_INTERNAL,
			command,
		)
	membership_committed.emit(result)
	return result

func prepare(command: MembershipCommand) -> FactionState:
	if command == null or command.validate() != OK:
		return null
	if _catalog == null or _repository == null or _identities == null:
		return null
	if not _identities.character_exists(command.character_id):
		return null
	var source := _repository.get_faction(command.faction_id)
	if source == null or source.revision != command.expected_faction_revision:
		return null
	var candidate := source.duplicate_detached()
	match command.operation:
		MembershipCommand.Operation.JOIN:
			if not _prepare_join(candidate, command):
				return null
		MembershipCommand.Operation.CHANGE_RANK:
			if not _prepare_rank(candidate, command):
				return null
		_:
			if not _prepare_end_or_suspend(candidate, command):
				return null
	candidate.revision += 1
	return candidate if candidate.validate(_catalog) == OK else null

func _command_result(
	status: PoliticalCommandResult.Status,
	command: MembershipCommand,
) -> PoliticalCommandResult:
	var result := PoliticalCommandResult.new()
	result.status = status
	if command != null:
		result.command_id = command.command_id
		result.aggregate_id = command.faction_id
	result.message = PoliticalCommandResult.Status.keys()[status]
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `execute()` traite replay et conflit d’empreinte avant la préparation, puis émet le signal seulement après le commit.
- Le service valide l’identité logique avant de lire l’agrégat.
- La révision de faction protège toutes les transitions.
- Chaque opération modifie une copie détachée par un helper spécialisé.
- Une adhésion n’est jamais créée à partir d’une relation sociale supposée.
- `commit_political()` enregistre ensemble le candidat, l’identité, l’empreinte et le résultat idempotent.

### 21.1 Invariants des transitions d’adhésion

Pour `JOIN`, le personnage ne possède aucune adhésion ouverte dans la faction, le rang appartient à la définition et la capacité n’est pas dépassée. Pour `CHANGE_RANK`, l’adhésion est active, sa révision correspond et le nouveau rang est autorisé. Pour `SUSPEND`, `RESIGN` ou `EXPEL`, le statut et le tick de fin sont calculés sans supprimer l’historique.

Une suspension ne produit aucun droit actif. Une démission et une expulsion ferment l’adhésion. Une réintégration future crée une nouvelle identité d’adhésion afin que l’historique ne soit pas réécrit.

### 21.2 Helpers de transition

> **[LECTURE] Helpers internes — Suite de `membership_service.gd`.**

```gdscript
func _prepare_join(candidate: FactionState, command: MembershipCommand) -> bool:
	if command.expected_membership_revision != -1:
		return false
	if candidate.memberships.has(command.membership_id):
		return false
	if candidate.active_membership_by_character.has(command.character_id):
		return false
	var definition := _catalog.get_faction(command.faction_id)
	if definition == null or command.target_rank_id not in definition.rank_ids:
		return false
	if candidate.active_membership_by_character.size() >= definition.maximum_members:
		return false
	var membership := MembershipState.new()
	membership.membership_id = command.membership_id
	membership.faction_id = command.faction_id
	membership.character_id = command.character_id
	membership.rank_id = command.target_rank_id
	membership.status = MembershipState.Status.ACTIVE
	membership.joined_tick = command.logical_tick
	membership.revision = 0
	membership.cause_id = command.cause_id
	candidate.memberships[membership.membership_id] = membership
	candidate.active_membership_by_character[membership.character_id] = membership.membership_id
	return true

func _prepare_rank(candidate: FactionState, command: MembershipCommand) -> bool:
	var membership := candidate.memberships.get(command.membership_id) as MembershipState
	if membership == null or membership.character_id != command.character_id:
		return false
	if membership.status != MembershipState.Status.ACTIVE:
		return false
	if membership.revision != command.expected_membership_revision:
		return false
	var definition := _catalog.get_faction(command.faction_id)
	if definition == null or command.target_rank_id not in definition.rank_ids:
		return false
	membership.rank_id = command.target_rank_id
	membership.cause_id = command.cause_id
	membership.revision += 1
	return true

func _prepare_end_or_suspend(
	candidate: FactionState,
	command: MembershipCommand,
) -> bool:
	var membership := candidate.memberships.get(command.membership_id) as MembershipState
	if membership == null or membership.character_id != command.character_id:
		return false
	if membership.revision != command.expected_membership_revision:
		return false
	if membership.status not in [MembershipState.Status.ACTIVE, MembershipState.Status.SUSPENDED]:
		return false
	match command.operation:
		MembershipCommand.Operation.SUSPEND:
			membership.status = MembershipState.Status.SUSPENDED
			membership.ended_tick = -1
		MembershipCommand.Operation.RESIGN:
			membership.status = MembershipState.Status.RESIGNED
			membership.ended_tick = command.logical_tick
			candidate.active_membership_by_character.erase(membership.character_id)
		MembershipCommand.Operation.EXPEL:
			membership.status = MembershipState.Status.EXPELLED
			membership.ended_tick = command.logical_tick
			candidate.active_membership_by_character.erase(membership.character_id)
		_:
			return false
	membership.cause_id = command.cause_id
	membership.revision += 1
	return true
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Une entrée exige une identité nouvelle, l’absence d’adhésion ouverte et un rang autorisé par la définition.
- Le changement de rang relit l’adhésion, son personnage, son statut et sa révision avant mutation.
- Une suspension conserve l’index de l’adhésion ouverte mais retire ses droits lors du calcul d’autorisation.
- Une démission ou expulsion ferme l’intervalle logique puis retire uniquement l’index secondaire.
- Tous les helpers modifient exclusivement la copie candidate reçue par le service.

## 22. Commande de mandat

> **[LECTURE] Commande de référence — `mandate_command.gd`.**

```gdscript
class_name MandateCommand
extends RefCounted

enum Operation {
	APPOINT,
	REVOKE,
	COMPLETE,
	MARK_VACANT,
}

var command_id: StringName
var operation: Operation = Operation.APPOINT
var faction_id: StringName
var mandate_id: StringName
var office_id: StringName
var holder_character_id: StringName
var jurisdiction_id: StringName
var expected_faction_revision: int = 0
var expected_mandate_revision: int = -1
var cause_id: StringName
var source_system_id: StringName
var logical_tick: int = 0
var command_fingerprint: String = ""

func validate() -> Error:
	for value: StringName in [
		command_id, faction_id, mandate_id, office_id, cause_id, source_system_id,
	]:
		if not StableId.is_valid(value):
			return ERR_INVALID_DATA
	if operation < Operation.APPOINT or operation > Operation.MARK_VACANT:
		return ERR_INVALID_DATA
	if operation == Operation.APPOINT and not CharacterId.is_valid(holder_character_id):
		return ERR_INVALID_DATA
	if operation != Operation.APPOINT and not holder_character_id.is_empty():
		if not CharacterId.is_valid(holder_character_id):
			return ERR_INVALID_DATA
	if not jurisdiction_id.is_empty() and not StableId.is_valid(jurisdiction_id):
		return ERR_INVALID_DATA
	if expected_faction_revision < 0 or expected_mandate_revision < -1:
		return ERR_INVALID_DATA
	if operation == Operation.APPOINT and expected_mandate_revision != -1:
		return ERR_INVALID_DATA
	if operation != Operation.APPOINT and expected_mandate_revision < 0:
		return ERR_INVALID_DATA
	if logical_tick < 0 or command_fingerprint.is_empty():
		return ERR_INVALID_DATA
	if command_fingerprint.length() > 128:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La nomination et les fins de mandat partagent une structure causale unique.
- Une création exige `expected_mandate_revision = -1`, tandis qu’une modification exige une révision existante.
- Le titulaire est obligatoire pour une nomination et reste validé lorsqu’une opération de fin le mentionne.
- Cause, système source, tick et empreinte rendent la commande traçable et idempotente.
- La juridiction reste une référence validée par le port régional, jamais un accès à l’état écologique.

## 23. Service de mandats

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/mandate_service.gd`.**

```gdscript
class_name MandateService
extends RefCounted

var _catalog: PoliticalCatalog
var _repository: PoliticalRepository
var _identities: PoliticalIdentityPort
var _regions: PoliticalRegionPort
var _commit: PoliticalJusticeCommitPort

signal mandate_committed(result: PoliticalCommandResult)

func execute(command: MandateCommand) -> PoliticalCommandResult:
	if command == null or command.validate() != OK:
		return _command_result(PoliticalCommandResult.Status.REJECTED_INVALID_COMMAND, command)
	if _repository == null or _commit == null:
		return _command_result(PoliticalCommandResult.Status.REJECTED_INTERNAL, command)
	var replay := _repository.find_command_result(command.command_id, command.command_fingerprint)
	if replay != null:
		replay.status = PoliticalCommandResult.Status.REPLAYED
		return replay
	if _repository.has_conflicting_fingerprint(
		command.command_id,
		command.command_fingerprint,
	):
		return _command_result(
			PoliticalCommandResult.Status.REJECTED_IDEMPOTENCY_CONFLICT,
			command,
		)
	var candidate := prepare(command)
	if candidate == null:
		return _command_result(PoliticalCommandResult.Status.REJECTED_CONFLICT, command)
	var result := _command_result(PoliticalCommandResult.Status.COMMITTED, command)
	var code := _commit.commit_political(
		candidate,
		command.expected_faction_revision,
		result,
		command.command_id,
		command.command_fingerprint,
	)
	if code != OK:
		return _command_result(
			PoliticalCommandResult.Status.REJECTED_STALE_REVISION
			if code == ERR_BUSY
			else PoliticalCommandResult.Status.REJECTED_INTERNAL,
			command,
		)
	mandate_committed.emit(result)
	return result

func prepare(command: MandateCommand) -> FactionState:
	if command == null or command.validate() != OK:
		return null
	if _catalog == null or _repository == null or _identities == null or _regions == null:
		return null
	var source := _repository.get_faction(command.faction_id)
	if source == null or source.revision != command.expected_faction_revision:
		return null
	var candidate := source.duplicate_detached()
	if command.operation == MandateCommand.Operation.APPOINT:
		if not _prepare_appointment(candidate, command):
			return null
	else:
		if not _prepare_end(candidate, command):
			return null
	candidate.revision += 1
	return candidate if candidate.validate(_catalog) == OK else null

func _prepare_appointment(candidate: FactionState, command: MandateCommand) -> bool:
	if candidate.mandates.has(command.mandate_id):
		return false
	if not _identities.character_exists(command.holder_character_id):
		return false
	if not command.jurisdiction_id.is_empty():
		if not _regions.jurisdiction_exists(command.jurisdiction_id):
			return false
	var definition := _catalog.get_faction(command.faction_id)
	var office := _catalog.get_office(command.office_id)
	if definition == null or office == null or command.office_id not in definition.office_ids:
		return false
	if not _holder_meets_rank(candidate, command.holder_character_id, office):
		return false
	if _active_holders(candidate, command.office_id) >= office.maximum_simultaneous_holders:
		return false
	var mandate := MandateState.new()
	mandate.mandate_id = command.mandate_id
	mandate.institution_id = definition.institution_id
	mandate.faction_id = command.faction_id
	mandate.office_id = command.office_id
	mandate.holder_character_id = command.holder_character_id
	mandate.jurisdiction_id = command.jurisdiction_id
	mandate.status = MandateState.Status.ACTIVE
	mandate.started_tick = command.logical_tick
	mandate.scheduled_end_tick = _scheduled_end(command.logical_tick, office.mandate_duration_ticks)
	if mandate.scheduled_end_tick < -1:
		return false
	mandate.revision = 0
	mandate.appointment_cause_id = command.cause_id
	candidate.mandates[mandate.mandate_id] = mandate
	return true

func _prepare_end(candidate: FactionState, command: MandateCommand) -> bool:
	var mandate := candidate.mandates.get(command.mandate_id) as MandateState
	if mandate == null or mandate.office_id != command.office_id:
		return false
	if mandate.revision != command.expected_mandate_revision:
		return false
	if mandate.status != MandateState.Status.ACTIVE:
		return false
	match command.operation:
		MandateCommand.Operation.REVOKE:
			mandate.status = MandateState.Status.REVOKED
		MandateCommand.Operation.COMPLETE:
			mandate.status = MandateState.Status.COMPLETED
		MandateCommand.Operation.MARK_VACANT:
			mandate.status = MandateState.Status.VACANT
			mandate.holder_character_id = &""
		_:
			return false
	mandate.actual_end_tick = command.logical_tick
	mandate.revision += 1
	return true

func _holder_meets_rank(
	faction: FactionState,
	character_id: StringName,
	office: OfficeDefinition,
) -> bool:
	var membership_id: StringName = faction.active_membership_by_character.get(character_id, &"")
	var membership := faction.memberships.get(membership_id) as MembershipState
	return (
		membership != null
		and membership.status == MembershipState.Status.ACTIVE
		and membership.rank_id in office.required_rank_ids
	)

func _active_holders(faction: FactionState, office_id: StringName) -> int:
	var count := 0
	for mandate: MandateState in faction.mandates.values():
		if mandate.office_id == office_id and mandate.status == MandateState.Status.ACTIVE:
			count += 1
	return count

func _scheduled_end(start_tick: int, duration_ticks: int) -> int:
	if duration_ticks == 0:
		return -1
	if start_tick > 9007199254740991 - duration_ticks:
		return -2
	return start_tick + duration_ticks

func _command_result(
	status: PoliticalCommandResult.Status,
	command: MandateCommand,
) -> PoliticalCommandResult:
	var result := PoliticalCommandResult.new()
	result.status = status
	if command != null:
		result.command_id = command.command_id
		result.aggregate_id = command.faction_id
	result.message = PoliticalCommandResult.Status.keys()[status]
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `execute()` protège l’idempotence, committe le candidat et n’émet son événement qu’après succès.
- `prepare()` traite création et fin de mandat sur une copie détachée, puis revalide l’agrégat complet.
- Une nomination recoupe identité, juridiction, définition de faction, fonction autorisée, rang requis et capacité simultanée.
- Une opération de fin exige le mandat actif et sa révision exacte ; elle conserve l’historique au lieu de supprimer l’entrée.
- `_scheduled_end()` distingue un mandat sans échéance (`-1`) d’un dépassement entier (`-2`).
- Les droits ne sont pas copiés dans le mandat : ils restent dérivés des définitions et de la période active.

## 24. Promulguer une loi

> **[LECTURE] Commande de promulgation — `enact_law_command.gd`.**

```gdscript
class_name EnactLawCommand
extends RefCounted

var command_id: StringName
var law_id: StringName
var law_version: int = 1
var institution_id: StringName
var jurisdiction_id: StringName
var effective_from_tick: int = 0
var effective_until_tick: int = -1
var proposer_character_id: StringName
var expected_law_book_revision: int = 0
var cause_id: StringName
var source_system_id: StringName
var logical_tick: int = 0
var command_fingerprint: String = ""

func validate() -> Error:
	for value: StringName in [
		command_id, law_id, institution_id, cause_id, source_system_id,
	]:
		if not StableId.is_valid(value):
			return ERR_INVALID_DATA
	if law_version < 1 or expected_law_book_revision < 0:
		return ERR_INVALID_DATA
	if not jurisdiction_id.is_empty() and not StableId.is_valid(jurisdiction_id):
		return ERR_INVALID_DATA
	if not CharacterId.is_valid(proposer_character_id):
		return ERR_INVALID_DATA
	if logical_tick < 0 or effective_from_tick < logical_tick:
		return ERR_INVALID_DATA
	if effective_until_tick != -1 and effective_until_tick < effective_from_tick:
		return ERR_INVALID_DATA
	if command_fingerprint.is_empty() or command_fingerprint.length() > 128:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La commande référence une définition de loi déjà versionnée et ne transporte aucun code exécutable.
- La date d’effet ne peut pas précéder la promulgation, et la date de fin ne peut pas précéder le début.
- Le proposant est identifié, mais son autorité est recalculée depuis les lois et mandats actifs.
- Cause, système source et empreinte permettent d’auditer puis de rejouer la commande sans double effet.
- La révision protège le recueil contre deux promulgations concurrentes.

## 25. Service législatif

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/legislative_service.gd`.**

```gdscript
class_name LegislativeService
extends RefCounted

var _catalog: PoliticalCatalog
var _repository: PoliticalRepository
var _authorization: PoliticalAuthorizationService
var _regions: PoliticalRegionPort
var _commit: PoliticalJusticeCommitPort

signal law_enacted(result: PoliticalCommandResult)

func execute(command: EnactLawCommand) -> PoliticalCommandResult:
	if command == null or command.validate() != OK:
		return _command_result(PoliticalCommandResult.Status.REJECTED_INVALID_COMMAND, command)
	if _repository == null or _commit == null:
		return _command_result(PoliticalCommandResult.Status.REJECTED_INTERNAL, command)
	var replay := _repository.find_command_result(command.command_id, command.command_fingerprint)
	if replay != null:
		replay.status = PoliticalCommandResult.Status.REPLAYED
		return replay
	if _repository.has_conflicting_fingerprint(
		command.command_id,
		command.command_fingerprint,
	):
		return _command_result(
			PoliticalCommandResult.Status.REJECTED_IDEMPOTENCY_CONFLICT,
			command,
		)
	var candidate := prepare(command)
	if candidate == null:
		return _command_result(PoliticalCommandResult.Status.REJECTED_CONFLICT, command)
	var result := _command_result(PoliticalCommandResult.Status.COMMITTED, command)
	var code := _commit.commit_political(
		candidate,
		command.expected_law_book_revision,
		result,
		command.command_id,
		command.command_fingerprint,
	)
	if code != OK:
		return _command_result(
			PoliticalCommandResult.Status.REJECTED_STALE_REVISION
			if code == ERR_BUSY
			else PoliticalCommandResult.Status.REJECTED_INTERNAL,
			command,
		)
	law_enacted.emit(result)
	return result

func prepare(command: EnactLawCommand) -> LawBookState:
	if command == null or command.validate() != OK:
		return null
	if _catalog == null or _repository == null or _authorization == null or _regions == null:
		return null
	var definition := _catalog.get_law(command.law_id, command.law_version)
	if definition == null:
		return null
	if _catalog.get_institution(command.institution_id) == null:
		return null
	if not command.jurisdiction_id.is_empty():
		if not _regions.jurisdiction_exists(command.jurisdiction_id):
			return null
	var context := AuthorizationContext.for_action(
		&"politics.action.enact_law",
		command.proposer_character_id,
		command.institution_id,
		command.jurisdiction_id,
		command.logical_tick,
	)
	var decision := _authorization.decide(context)
	if decision == null or not decision.is_allowed():
		return null
	var source := _repository.get_law_book()
	if source == null or source.revision != command.expected_law_book_revision:
		return null
	if _overlaps_existing_enactment(source, command):
		return null
	var candidate := source.duplicate_detached()
	candidate.enactments.append(_new_enactment(command))
	candidate.revision += 1
	return candidate if candidate.validate(_catalog) == OK else null

func _overlaps_existing_enactment(
	source: LawBookState,
	command: EnactLawCommand,
) -> bool:
	for enactment: LawBookState.Enactment in source.enactments:
		if enactment.law_id != command.law_id:
			continue
		if enactment.law_version != command.law_version:
			continue
		if enactment.institution_id != command.institution_id:
			continue
		if enactment.jurisdiction_id != command.jurisdiction_id:
			continue
		if _intervals_overlap(
			enactment.effective_from_tick,
			enactment.effective_until_tick,
			command.effective_from_tick,
			command.effective_until_tick,
		):
			return true
	return false

func _intervals_overlap(left_start: int, left_end: int, right_start: int, right_end: int) -> bool:
	var left_after_right := right_end != -1 and left_start > right_end
	var right_after_left := left_end != -1 and right_start > left_end
	return not left_after_right and not right_after_left

func _new_enactment(command: EnactLawCommand) -> LawBookState.Enactment:
	var enactment := LawBookState.Enactment.new()
	enactment.law_id = command.law_id
	enactment.law_version = command.law_version
	enactment.institution_id = command.institution_id
	enactment.jurisdiction_id = command.jurisdiction_id
	enactment.enacted_tick = command.logical_tick
	enactment.effective_from_tick = command.effective_from_tick
	enactment.effective_until_tick = command.effective_until_tick
	enactment.promulgation_cause_id = command.cause_id
	return enactment

func _command_result(
	status: PoliticalCommandResult.Status,
	command: EnactLawCommand,
) -> PoliticalCommandResult:
	var result := PoliticalCommandResult.new()
	result.status = status
	if command != null:
		result.command_id = command.command_id
		result.aggregate_id = &"politics.law_book"
	result.message = PoliticalCommandResult.Status.keys()[status]
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `execute()` applique les règles d’idempotence avant préparation et émet la promulgation seulement après le commit.
- La définition, l’institution, la juridiction et l’autorisation sont relues avant l’agrégat vivant.
- Le droit de promulguer est calculé au tick demandé ; la commande ne peut pas se déclarer elle-même autorisée.
- `_overlaps_existing_enactment()` refuse deux périodes qui se chevauchent pour la même version et la même portée.
- Les intervalles ouverts utilisent `-1` et sont comparés sans consulter l’heure système.
- Le recueil candidat conserve les anciennes promulgations et est intégralement revalidé avant retour.

## 26. Contexte d’autorisation

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/authorization_context.gd`.**

```gdscript
class_name AuthorizationContext
extends RefCounted

var action_id: StringName
var actor_character_id: StringName
var institution_id: StringName
var faction_id: StringName
var jurisdiction_id: StringName
var target_character_id: StringName
var target_object_id: StringName
var logical_tick: int = 0
var facts: Dictionary[StringName, Variant] = {}

static func for_action(
	p_action_id: StringName,
	p_actor_id: StringName,
	p_institution_id: StringName,
	p_jurisdiction_id: StringName,
	p_tick: int,
) -> AuthorizationContext:
	var context := AuthorizationContext.new()
	context.action_id = p_action_id
	context.actor_character_id = p_actor_id
	context.institution_id = p_institution_id
	context.jurisdiction_id = p_jurisdiction_id
	context.logical_tick = p_tick
	return context

func validate() -> Error:
	if not StableId.is_valid(action_id):
		return ERR_INVALID_DATA
	if not CharacterId.is_valid(actor_character_id):
		return ERR_INVALID_DATA
	for value: StringName in [institution_id, faction_id, jurisdiction_id]:
		if not value.is_empty() and not StableId.is_valid(value):
			return ERR_INVALID_DATA
	if not target_character_id.is_empty() and not CharacterId.is_valid(target_character_id):
		return ERR_INVALID_DATA
	if not target_object_id.is_empty() and not StableId.is_valid(target_object_id):
		return ERR_INVALID_DATA
	if logical_tick < 0 or facts.size() > 32:
		return ERR_INVALID_DATA
	for fact_id: StringName in facts:
		if not StableId.is_valid(fact_id):
			return ERR_INVALID_DATA
		if typeof(facts[fact_id]) not in [TYPE_BOOL, TYPE_INT, TYPE_STRING, TYPE_STRING_NAME]:
			return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le contexte rassemble des identifiants et faits bornés, jamais des nœuds.
- Les cibles optionnelles restent explicitement séparées par type.
- La fabrique initialise le cas courant sans empêcher des contextes plus riches.
- Les faits supplémentaires doivent provenir de ports validés.
- Le contexte est transitoire et n’est pas persisté.

## 27. Décision d’autorisation

> **[LECTURE] Décision explicable — `authorization_decision.gd`.**

```gdscript
class_name AuthorizationDecision
extends RefCounted

enum Outcome {
	ALLOW,
	DENY,
	NOT_APPLICABLE,
	INDETERMINATE,
}

var outcome: Outcome = Outcome.INDETERMINATE
var action_id: StringName
var actor_character_id: StringName
var matched_law_refs: Array[String] = []
var granted_right_ids: Array[StringName] = []
var denied_reason_id: StringName
var evaluated_tick: int = 0
var law_book_revision: int = 0

func is_allowed() -> bool:
	return outcome == Outcome.ALLOW

func validate() -> Error:
	if outcome < Outcome.ALLOW or outcome > Outcome.INDETERMINATE:
		return ERR_INVALID_DATA
	if outcome == Outcome.INDETERMINATE:
		if not action_id.is_empty() and not StableId.is_valid(action_id):
			return ERR_INVALID_DATA
		if not actor_character_id.is_empty() and not CharacterId.is_valid(actor_character_id):
			return ERR_INVALID_DATA
	else:
		if not StableId.is_valid(action_id) or not CharacterId.is_valid(actor_character_id):
			return ERR_INVALID_DATA
	if evaluated_tick < 0 or law_book_revision < 0:
		return ERR_INVALID_DATA
	if matched_law_refs.size() > 128 or granted_right_ids.size() > 128:
		return ERR_OUT_OF_MEMORY
	if _validate_unique_rights(granted_right_ids) != OK:
		return ERR_INVALID_DATA
	if outcome in [Outcome.DENY, Outcome.INDETERMINATE]:
		if not StableId.is_valid(denied_reason_id):
			return ERR_INVALID_DATA
	return OK

func _validate_unique_rights(values: Array[StringName]) -> Error:
	var seen: Dictionary[StringName, bool] = {}
	for value: StringName in values:
		if not StableId.is_valid(value) or seen.has(value):
			return ERR_INVALID_DATA
		seen[value] = true
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La décision distingue refus, absence de loi et impossibilité d’évaluer.
- Les références de lois expliquent la conclusion sans exposer les définitions mutables.
- Les droits accordés sont listés et bornés.
- Un refus ou une impossibilité d’évaluer exige une raison stable.
- Une décision d’autorisation est un résultat transitoire, pas une loi persistée.

## 28. Calculer une autorisation

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/political_authorization_service.gd`.**

```gdscript
class_name PoliticalAuthorizationService
extends RefCounted

var _catalog: PoliticalCatalog
var _repository: PoliticalRepository

func decide(context: AuthorizationContext) -> AuthorizationDecision:
	if context == null or context.validate() != OK:
		return _indeterminate(context, &"politics.reason.invalid_context")
	if _catalog == null or _repository == null:
		return _indeterminate(context, &"politics.reason.unconfigured")
	var law_book := _repository.get_law_book()
	if law_book == null or law_book.validate(_catalog) != OK:
		return _indeterminate(context, &"politics.reason.missing_law_book")
	var rights := _collect_active_rights(context)
	var enactments := law_book.active_at(context.jurisdiction_id, context.logical_tick)
	var matching: Array[LawDefinition] = []
	for enactment: LawBookState.Enactment in enactments:
		var law := _catalog.get_law(enactment.law_id, enactment.law_version)
		if law == null:
			return _indeterminate(context, &"politics.reason.missing_law_definition")
		if law.action_id == context.action_id:
			matching.append(law)
	matching.sort_custom(_sort_laws)
	return _evaluate(context, rights, matching, law_book.revision)

func _collect_active_rights(context: AuthorizationContext) -> Array[StringName]:
	var seen: Dictionary[StringName, bool] = {}
	for faction_id: StringName in _repository.all_faction_ids_sorted():
		var faction := _repository.get_faction(faction_id)
		var definition := _catalog.get_faction(faction_id)
		if faction == null or definition == null:
			continue
		if not context.institution_id.is_empty():
			if definition.institution_id != context.institution_id:
				continue
		var membership_id: StringName = faction.active_membership_by_character.get(
			context.actor_character_id,
			&"",
		)
		var membership := faction.memberships.get(membership_id) as MembershipState
		if membership == null or membership.status != MembershipState.Status.ACTIVE:
			continue
		var rank := _catalog.get_rank(membership.rank_id)
		if rank != null:
			for right_id: StringName in rank.granted_right_ids:
				seen[right_id] = true
		for mandate: MandateState in faction.mandates.values():
			if mandate.status != MandateState.Status.ACTIVE:
				continue
			if mandate.holder_character_id != context.actor_character_id:
				continue
			if not context.jurisdiction_id.is_empty():
				if mandate.jurisdiction_id not in [&"", context.jurisdiction_id]:
					continue
			var office := _catalog.get_office(mandate.office_id)
			if office == null:
				continue
			for right_id: StringName in office.granted_right_ids:
				seen[right_id] = true
	var result: Array[StringName] = []
	result.assign(seen.keys())
	result.sort()
	return result

func _evaluate(
	context: AuthorizationContext,
	rights: Array[StringName],
	laws: Array[LawDefinition],
	law_book_revision: int,
) -> AuthorizationDecision:
	if laws.is_empty():
		return _decision(
			AuthorizationDecision.Outcome.NOT_APPLICABLE,
			context,
			rights,
			[],
			&"",
			law_book_revision,
		)
	var matched_refs: Array[String] = []
	for law: LawDefinition in laws:
		matched_refs.append("%s@%d" % [law.law_id, law.version])
		match law.effect:
			LawDefinition.Effect.DENY:
				return _decision(
					AuthorizationDecision.Outcome.DENY,
					context,
					rights,
					matched_refs,
					&"politics.reason.explicit_deny",
					law_book_revision,
				)
			LawDefinition.Effect.REQUIRE_RIGHT:
				if law.required_right_id in rights:
					return _decision(
						AuthorizationDecision.Outcome.ALLOW,
						context,
						rights,
						matched_refs,
						&"",
						law_book_revision,
					)
				return _decision(
					AuthorizationDecision.Outcome.DENY,
					context,
					rights,
					matched_refs,
					&"politics.reason.missing_right",
					law_book_revision,
				)
			LawDefinition.Effect.ALLOW:
				return _decision(
					AuthorizationDecision.Outcome.ALLOW,
					context,
					rights,
					matched_refs,
					&"",
					law_book_revision,
				)
			LawDefinition.Effect.REPORT_INFRACTION:
				return _decision(
					AuthorizationDecision.Outcome.DENY,
					context,
					rights,
					matched_refs,
					&"politics.reason.reportable_infraction",
					law_book_revision,
				)
	return _indeterminate(context, &"politics.reason.unhandled_law_effect")

func _decision(
	outcome: AuthorizationDecision.Outcome,
	context: AuthorizationContext,
	rights: Array[StringName],
	matched_refs: Array[String],
	reason_id: StringName,
	law_book_revision: int,
) -> AuthorizationDecision:
	var decision := AuthorizationDecision.new()
	decision.outcome = outcome
	decision.action_id = context.action_id
	decision.actor_character_id = context.actor_character_id
	decision.matched_law_refs = matched_refs.duplicate()
	decision.granted_right_ids = rights.duplicate()
	decision.denied_reason_id = reason_id
	decision.evaluated_tick = context.logical_tick
	decision.law_book_revision = law_book_revision
	return decision if decision.validate() == OK else null

func _indeterminate(
	context: AuthorizationContext,
	reason_id: StringName,
) -> AuthorizationDecision:
	var decision := AuthorizationDecision.new()
	decision.outcome = AuthorizationDecision.Outcome.INDETERMINATE
	decision.denied_reason_id = reason_id
	if context != null:
		decision.action_id = context.action_id
		decision.actor_character_id = context.actor_character_id
		decision.evaluated_tick = maxi(context.logical_tick, 0)
	return decision if decision.validate() == OK else null

func _sort_laws(left: LawDefinition, right: LawDefinition) -> bool:
	if left.priority != right.priority:
		return left.priority > right.priority
	if left.law_id != right.law_id:
		return String(left.law_id) < String(right.law_id)
	return left.version < right.version
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les droits actifs sont reconstruits depuis les adhésions `ACTIVE` et les mandats `ACTIVE`, jamais depuis la proximité, l’affinité ou un nœud.
- Les lois actives sont relues depuis le recueil au tick et dans la juridiction demandés ; une définition manquante rend l’évaluation indéterminée.
- La priorité décroissante est départagée lexicalement puis par version, ce qui rend l’ordre reproductible.
- `_evaluate()` traite la première règle prioritaire applicable : interdiction, droit requis, permission ou infraction rapportable.
- Chaque décision conserve les références de lois, les droits observés, la révision du recueil et une raison stable sans exposer les agrégats mutables.

### 28.1 Politique de décision

`Project Asteria` utilise une politique **deny-by-default** pour les actions protégées. Une loi `DENY` prioritaire refuse. Une loi `REQUIRE_RIGHT` autorise seulement si le droit est actif. Une loi `ALLOW` peut autoriser lorsque aucune interdiction prioritaire ne s’applique. Une loi `REPORT_INFRACTION` refuse l’action protégée et fournit une raison stable qui peut être transformée en rapport par un service séparé.

`NOT_APPLICABLE` signifie qu’aucune loi ne correspond à l’action. L’appelant ne le confond pas avec `ALLOW` : il applique alors la politique générale déclarée pour cette famille d’actions. `INDETERMINATE` signale une entrée invalide, une configuration absente ou une référence incohérente et produit toujours un échec fermé.

## 29. Rapporter une infraction

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/infraction_report_command.gd`.**

```gdscript
class_name InfractionReportCommand
extends RefCounted

var command_id: StringName
var case_id: StringName
var infraction_type_id: StringName
var institution_id: StringName
var jurisdiction_id: StringName
var accused_character_id: StringName
var reporter_character_id: StringName
var alleged_tick: int = 0
var reported_tick: int = 0
var source_event_id: StringName
var cause_id: StringName
var source_system_id: StringName
var expected_case_revision: int = -1
var command_fingerprint: String = ""

func validate() -> Error:
	for value: StringName in [
		command_id,
		case_id,
		infraction_type_id,
		institution_id,
		source_event_id,
		cause_id,
		source_system_id,
	]:
		if not StableId.is_valid(value):
			return ERR_INVALID_DATA
	if not jurisdiction_id.is_empty() and not StableId.is_valid(jurisdiction_id):
		return ERR_INVALID_DATA
	if not CharacterId.is_valid(accused_character_id):
		return ERR_INVALID_DATA
	if not reporter_character_id.is_empty():
		if not CharacterId.is_valid(reporter_character_id):
			return ERR_INVALID_DATA
	if alleged_tick < 0 or reported_tick < alleged_tick:
		return ERR_INVALID_DATA
	if expected_case_revision != -1:
		return ERR_INVALID_DATA
	if command_fingerprint.is_empty() or command_fingerprint.length() > 128:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le dossier et la commande possèdent des identités distinctes.
- L’accusé est obligatoire ; le rapporteur peut rester vide pour une cause système authentifiée par `source_system_id`.
- Le fait allégué ne peut pas être daté après son rapport.
- `source_event_id`, `cause_id` et le système source relient l’allégation à un fait committé sans conclure à la culpabilité.
- `expected_case_revision = -1` indique explicitement une création idempotente.

### 29.1 Ouvrir un dossier sans préjuger du verdict

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/political_causal_event_port.gd`.**

```gdscript
class_name PoliticalCausalEventPort
extends RefCounted

func event_exists(
	_source_system_id: StringName,
	_event_id: StringName,
) -> bool:
	return false
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le port confirme qu’un événement causal a réellement été committé par le système source annoncé.
- Il ne retourne ni payload mutable, ni conclusion judiciaire.
- L’adaptateur peut router vers combat, économie, inventaire, écologie ou un système institutionnel.
- Une identité inconnue ou associée à un autre système est refusée.
- La vérification du fait source ne transforme pas l’allégation en preuve recevable ni en verdict.

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/justice_intake_service.gd`.**

```gdscript
class_name JusticeIntakeService
extends RefCounted

signal case_opened(result: PoliticalCommandResult)

var _political_repository: PoliticalRepository
var _justice_repository: JusticeRepository
var _identities: PoliticalIdentityPort
var _regions: PoliticalRegionPort
var _events: PoliticalCausalEventPort
var _commit: PoliticalJusticeCommitPort

func open_case(command: InfractionReportCommand) -> PoliticalCommandResult:
	if command == null or command.validate() != OK:
		return _result(PoliticalCommandResult.Status.REJECTED_INVALID_COMMAND, command)
	if not _is_configured():
		return _result(PoliticalCommandResult.Status.REJECTED_INTERNAL, command)
	var replay := _political_repository.find_command_result(
		command.command_id,
		command.command_fingerprint,
	)
	if replay != null:
		replay.status = PoliticalCommandResult.Status.REPLAYED
		return replay
	if _political_repository.has_conflicting_fingerprint(
		command.command_id,
		command.command_fingerprint,
	):
		return _result(PoliticalCommandResult.Status.REJECTED_IDEMPOTENCY_CONFLICT, command)
	if _justice_repository.get_case(command.case_id) != null:
		return _result(PoliticalCommandResult.Status.REJECTED_CONFLICT, command)
	if not _events.event_exists(command.source_system_id, command.source_event_id):
		return _result(PoliticalCommandResult.Status.REJECTED_NOT_FOUND, command)
	if not _identities.character_exists(command.accused_character_id):
		return _result(PoliticalCommandResult.Status.REJECTED_NOT_FOUND, command)
	if not command.reporter_character_id.is_empty():
		if not _identities.character_exists(command.reporter_character_id):
			return _result(PoliticalCommandResult.Status.REJECTED_NOT_FOUND, command)
	if not command.jurisdiction_id.is_empty():
		if not _regions.jurisdiction_exists(command.jurisdiction_id):
			return _result(PoliticalCommandResult.Status.REJECTED_NOT_FOUND, command)

	var candidate := JusticeCaseState.new()
	candidate.case_id = command.case_id
	candidate.institution_id = command.institution_id
	candidate.jurisdiction_id = command.jurisdiction_id
	candidate.infraction_type_id = command.infraction_type_id
	candidate.accused_character_id = command.accused_character_id
	candidate.reporter_character_id = command.reporter_character_id
	candidate.source_event_id = command.source_event_id
	candidate.opening_cause_id = command.cause_id
	candidate.status = JusticeCaseState.Status.OPEN
	candidate.opened_tick = command.reported_tick
	candidate.revision = 0
	if candidate.validate() != OK:
		return _result(PoliticalCommandResult.Status.REJECTED_INVALID_COMMAND, command)
	var result := _result(PoliticalCommandResult.Status.COMMITTED, command)
	var code := _commit.commit_case(
		candidate,
		-1,
		result,
		command.command_id,
		command.command_fingerprint,
	)
	if code != OK:
		return _result(
			PoliticalCommandResult.Status.REJECTED_CONFLICT
			if code == ERR_ALREADY_EXISTS
			else PoliticalCommandResult.Status.REJECTED_INTERNAL,
			command,
		)
	case_opened.emit(result)
	return result

func _result(
	status: PoliticalCommandResult.Status,
	command: InfractionReportCommand,
) -> PoliticalCommandResult:
	var result := PoliticalCommandResult.new()
	result.status = status
	if command != null:
		result.command_id = command.command_id
		result.aggregate_id = command.case_id
	result.message = PoliticalCommandResult.Status.keys()[status]
	return result

func _is_configured() -> bool:
	return (
		_political_repository != null
		and _justice_repository != null
		and _identities != null
		and _regions != null
		and _events != null
		and _commit != null
	)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le service traite replay et conflit d’empreinte avant de créer le dossier.
- Il vérifie l’événement causal, les identités logiques et la juridiction sans consulter les scènes actives.
- L’allégation devient un dossier `OPEN` contenant sa provenance, mais aucune conclusion ni sanction.
- `commit_case()` enregistre ensemble le dossier, l’identité de commande, l’empreinte et le résultat durable.
- Le signal est émis seulement après le commit ; un retry identique renvoie `REPLAYED` sans ouvrir un second dossier.

## 30. Preuve structurée

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/evidence_record.gd`.**

```gdscript
class_name EvidenceRecord
extends RefCounted

enum Kind {
	TESTIMONY,
	OBJECT_REFERENCE,
	TRANSACTION_REFERENCE,
	COMBAT_EVENT_REFERENCE,
	ECOLOGY_EVENT_REFERENCE,
	DOCUMENT_REFERENCE,
}

var evidence_id: StringName
var case_id: StringName
var kind: Kind = Kind.DOCUMENT_REFERENCE
var source_id: StringName
var submitted_by_character_id: StringName
var collected_tick: int = 0
var chain_sequence: int = 0
var integrity_digest: String = ""
var admissibility_status_id: StringName
var weight_bp: int = 0

func validate() -> Error:
	if not StableId.is_valid(evidence_id) or not StableId.is_valid(case_id):
		return ERR_INVALID_DATA
	if kind < Kind.TESTIMONY or kind > Kind.DOCUMENT_REFERENCE:
		return ERR_INVALID_DATA
	if not StableId.is_valid(source_id):
		return ERR_INVALID_DATA
	if not submitted_by_character_id.is_empty():
		if not CharacterId.is_valid(submitted_by_character_id):
			return ERR_INVALID_DATA
	if collected_tick < 0 or chain_sequence < 0:
		return ERR_INVALID_DATA
	if integrity_digest.is_empty() or integrity_digest.length() > 128:
		return ERR_INVALID_DATA
	if not StableId.is_valid(admissibility_status_id):
		return ERR_INVALID_DATA
	if weight_bp < 0 or weight_bp > 10000:
		return ERR_INVALID_DATA
	return OK

func duplicate_detached() -> EvidenceRecord:
	var copy := EvidenceRecord.new()
	copy.evidence_id = evidence_id
	copy.case_id = case_id
	copy.kind = kind
	copy.source_id = source_id
	copy.submitted_by_character_id = submitted_by_character_id
	copy.collected_tick = collected_tick
	copy.chain_sequence = chain_sequence
	copy.integrity_digest = integrity_digest
	copy.admissibility_status_id = admissibility_status_id
	copy.weight_bp = weight_bp
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La preuve référence un fait ou objet possédé par un autre système au lieu de le copier.
- La séquence de chaîne de garde rend l’ordre des remises vérifiable.
- Le digest détecte une substitution du payload référencé sans prétendre prouver sa véracité.
- Recevabilité et poids sont distincts ; un témoignage reste une preuve possible, pas une vérité automatique.
- `duplicate_detached()` évite qu’un dossier candidat partage une preuve mutable avec le dossier actif.

### 30.1 Vérifier une référence sans prendre son autorité

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/evidence_source_port.gd`.**

```gdscript
class_name EvidenceSourcePort
extends RefCounted

func reference_exists(
	_kind: EvidenceRecord.Kind,
	_source_id: StringName,
) -> bool:
	return false

func integrity_digest_for(
	_kind: EvidenceRecord.Kind,
	_source_id: StringName,
) -> String:
	return ""
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’adaptateur route la vérification vers l’autorité concernée : inventaire, économie, combat, écologie ou documents.
- `reference_exists()` ne retourne jamais l’objet, la transaction ou l’événement mutable.
- `integrity_digest_for()` fournit une empreinte canonique calculée par le système source.
- Une référence supprimée, inconnue ou dont l’empreinte diffère est refusée avant l’ajout au dossier.
- Le port n’évalue ni recevabilité, ni poids, ni culpabilité.

## 31. Dossier judiciaire

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/justice_case_state.gd`.**

```gdscript
class_name JusticeCaseState
extends RefCounted

enum Status {
	OPEN,
	INVESTIGATING,
	READY_FOR_HEARING,
	DECIDED,
	APPEALED,
	CLOSED,
	DISMISSED,
}

const MAX_EVIDENCE := 512
const MAX_PARTICIPANTS := 128
const MAX_DECISIONS := 64

var case_id: StringName
var institution_id: StringName
var jurisdiction_id: StringName
var infraction_type_id: StringName
var accused_character_id: StringName
var reporter_character_id: StringName
var source_event_id: StringName
var opening_cause_id: StringName
var status: Status = Status.OPEN
var opened_tick: int = 0
var revision: int = 0
var evidence: Dictionary[StringName, EvidenceRecord] = {}
var investigator_character_ids: Array[StringName] = []
var decisions: Dictionary[StringName, VerdictDecision] = {}

func validate() -> Error:
	for value: StringName in [
		case_id,
		institution_id,
		infraction_type_id,
		source_event_id,
		opening_cause_id,
	]:
		if not StableId.is_valid(value):
			return ERR_INVALID_DATA
	if not jurisdiction_id.is_empty() and not StableId.is_valid(jurisdiction_id):
		return ERR_INVALID_DATA
	if not CharacterId.is_valid(accused_character_id):
		return ERR_INVALID_DATA
	if not reporter_character_id.is_empty():
		if not CharacterId.is_valid(reporter_character_id):
			return ERR_INVALID_DATA
	if status < Status.OPEN or status > Status.DISMISSED:
		return ERR_INVALID_DATA
	if opened_tick < 0 or revision < 0:
		return ERR_INVALID_DATA
	if evidence.size() > MAX_EVIDENCE:
		return ERR_OUT_OF_MEMORY
	if investigator_character_ids.size() > MAX_PARTICIPANTS:
		return ERR_OUT_OF_MEMORY
	if decisions.size() > MAX_DECISIONS:
		return ERR_OUT_OF_MEMORY
	for evidence_id: StringName in evidence:
		var record := evidence[evidence_id] as EvidenceRecord
		if record == null or record.evidence_id != evidence_id:
			return ERR_INVALID_DATA
		if record.case_id != case_id or record.validate() != OK:
			return ERR_INVALID_DATA
	if _validate_unique_characters(investigator_character_ids) != OK:
		return ERR_INVALID_DATA
	for decision_id: StringName in decisions:
		var decision := decisions[decision_id] as VerdictDecision
		if decision == null or decision.decision_id != decision_id:
			return ERR_INVALID_DATA
		if decision.case_id != case_id or decision.validate() != OK:
			return ERR_INVALID_DATA
	return OK

func duplicate_detached() -> JusticeCaseState:
	var copy := JusticeCaseState.new()
	copy.case_id = case_id
	copy.institution_id = institution_id
	copy.jurisdiction_id = jurisdiction_id
	copy.infraction_type_id = infraction_type_id
	copy.accused_character_id = accused_character_id
	copy.reporter_character_id = reporter_character_id
	copy.source_event_id = source_event_id
	copy.opening_cause_id = opening_cause_id
	copy.status = status
	copy.opened_tick = opened_tick
	copy.revision = revision
	for evidence_id: StringName in evidence:
		copy.evidence[evidence_id] = evidence[evidence_id].duplicate_detached()
	copy.investigator_character_ids = investigator_character_ids.duplicate()
	for decision_id: StringName in decisions:
		copy.decisions[decision_id] = decisions[decision_id].duplicate_detached()
	return copy

func _validate_unique_characters(values: Array[StringName]) -> Error:
	var seen: Dictionary[StringName, bool] = {}
	for value: StringName in values:
		if not CharacterId.is_valid(value) or seen.has(value):
			return ERR_INVALID_DATA
		seen[value] = true
	return OK

```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le dossier conserve l’allégation, sa provenance, les participants, les preuves et les verdicts complets sans préjuger de leur issue.
- Les clés de preuves sont recoupées avec les identifiants des valeurs et les collections sont bornées puis dédupliquées.
- La juridiction et le rapporteur peuvent être absents seulement selon les règles explicites de la commande d’ouverture.
- `duplicate_detached()` copie profondément toutes les preuves et listes avant une enquête ou une audience.
- Les références externes restent dans leurs systèmes propriétaires ; le dossier ne conserve que leurs identités et empreintes.

## 32. Dépôt judiciaire

> **[LECTURE] Contrat du dépôt judiciaire — Structure de référence.**

```gdscript
class_name JusticeRepository
extends RefCounted

func get_case(_case_id: StringName) -> JusticeCaseState:
	return null

func all_open_case_ids_sorted() -> Array[StringName]:
	return []

func replace_case(
	_candidate: JusticeCaseState,
	_expected_revision: int,
) -> Error:
	return ERR_UNAVAILABLE

func replace_all(_prepared: Dictionary) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les lectures retournent des copies détachées.
- Les dossiers ouverts sont triés pour un ordonnanceur reproductible.
- Le remplacement revalide la révision au dernier instant.
- Le dépôt ne décide ni recevabilité, ni culpabilité, ni sanction.
- Une restauration complète utilise un candidat global déjà validé.

## 33. Service d’enquête

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/investigation_service.gd`.**

```gdscript
class_name InvestigationService
extends RefCounted

var _repository: JusticeRepository
var _authorization: PoliticalAuthorizationService
var _evidence_sources: EvidenceSourcePort

func prepare_add_evidence(
	case_id: StringName,
	expected_revision: int,
	record: EvidenceRecord,
	actor_character_id: StringName,
	logical_tick: int,
) -> JusticeCaseState:
	if _repository == null or _authorization == null or _evidence_sources == null:
		return null
	if record == null or record.validate() != OK or record.case_id != case_id:
		return null
	var source := _repository.get_case(case_id)
	if source == null or source.revision != expected_revision:
		return null
	if source.status not in [JusticeCaseState.Status.OPEN, JusticeCaseState.Status.INVESTIGATING]:
		return null
	var context := AuthorizationContext.for_action(
		&"politics.action.collect_evidence",
		actor_character_id,
		source.institution_id,
		source.jurisdiction_id,
		logical_tick,
	)
	var decision := _authorization.decide(context)
	if decision == null or not decision.is_allowed():
		return null
	if record.chain_sequence != source.evidence.size():
		return null
	if not _evidence_sources.reference_exists(record.kind, record.source_id):
		return null
	var current_digest := _evidence_sources.integrity_digest_for(record.kind, record.source_id)
	if current_digest.is_empty() or current_digest != record.integrity_digest:
		return null
	var candidate := source.duplicate_detached()
	if candidate.evidence.has(record.evidence_id):
		return null
	candidate.evidence[record.evidence_id] = record.duplicate_detached()
	candidate.status = JusticeCaseState.Status.INVESTIGATING
	candidate.revision += 1
	return candidate if candidate.validate() == OK else null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le dossier, sa révision et son statut sont relus avant l’ajout.
- L’enquêteur doit posséder le droit actif au tick demandé.
- Le port de sources confirme l’existence puis recalcule l’empreinte canonique de la référence externe.
- Une séquence de chaîne de garde non contiguë, une identité déjà présente ou une empreinte différente est refusée sans mutation du dossier actif.
- La preuve est copiée dans le candidat, qui passe ensuite toute la validation du dossier.

## 34. Décision de verdict

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/verdict_decision.gd`.**

```gdscript
class_name VerdictDecision
extends RefCounted

enum Outcome {
	NOT_GUILTY,
	GUILTY,
	DISMISSED,
	MISTRIAL,
}

var decision_id: StringName
var case_id: StringName
var outcome: Outcome = Outcome.MISTRIAL
var decided_by_character_id: StringName
var decided_tick: int = 0
var applied_law_refs: Array[String] = []
var accepted_evidence_ids: Array[StringName] = []
var rejected_evidence_ids: Array[StringName] = []
var reasoning_code_ids: Array[StringName] = []
var case_revision: int = 0

func validate() -> Error:
	if not StableId.is_valid(decision_id) or not StableId.is_valid(case_id):
		return ERR_INVALID_DATA
	if outcome < Outcome.NOT_GUILTY or outcome > Outcome.MISTRIAL:
		return ERR_INVALID_DATA
	if not CharacterId.is_valid(decided_by_character_id):
		return ERR_INVALID_DATA
	if decided_tick < 0 or case_revision < 0:
		return ERR_INVALID_DATA
	if applied_law_refs.is_empty() and outcome == Outcome.GUILTY:
		return ERR_INVALID_DATA
	if accepted_evidence_ids.size() + rejected_evidence_ids.size() > 512:
		return ERR_OUT_OF_MEMORY
	if _validate_disjoint_evidence() != OK:
		return ERR_INVALID_DATA
	return _validate_reason_ids()

func _validate_disjoint_evidence() -> Error:
	var seen: Dictionary[StringName, bool] = {}
	for evidence_id: StringName in accepted_evidence_ids:
		if not StableId.is_valid(evidence_id) or seen.has(evidence_id):
			return ERR_INVALID_DATA
		seen[evidence_id] = true
	for evidence_id: StringName in rejected_evidence_ids:
		if not StableId.is_valid(evidence_id) or seen.has(evidence_id):
			return ERR_INVALID_DATA
		seen[evidence_id] = true
	return OK

func _validate_reason_ids() -> Error:
	var seen: Dictionary[StringName, bool] = {}
	for reason_id: StringName in reasoning_code_ids:
		if not StableId.is_valid(reason_id) or seen.has(reason_id):
			return ERR_INVALID_DATA
		seen[reason_id] = true
	return OK

func duplicate_detached() -> VerdictDecision:
	var copy := VerdictDecision.new()
	copy.decision_id = decision_id
	copy.case_id = case_id
	copy.outcome = outcome
	copy.decided_by_character_id = decided_by_character_id
	copy.decided_tick = decided_tick
	copy.applied_law_refs = applied_law_refs.duplicate()
	copy.accepted_evidence_ids = accepted_evidence_ids.duplicate()
	copy.rejected_evidence_ids = rejected_evidence_ids.duplicate()
	copy.reasoning_code_ids = reasoning_code_ids.duplicate()
	copy.case_revision = case_revision
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le verdict distingue culpabilité, acquittement, classement et impossibilité de juger.
- Une condamnation exige au moins une référence de loi applicable.
- Les preuves acceptées et rejetées restent identifiées séparément.
- Les codes de raisonnement sont stables et localisables.
- Le verdict ne contient encore aucun effet monétaire, matériel ou corporel.

## 35. Plan de sanction

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/domain/sanction_plan.gd`.**

```gdscript
class_name SanctionPlan
extends RefCounted

var decision_id: StringName
var case_id: StringName
var target_character_id: StringName
var fine_currency_id: StringName
var fine_amount_minor: int = 0
var confiscated_entry_ids: Array[StringName] = []
var restriction_ids: Array[StringName] = []
var affected_domain_ids: Array[StringName] = []
var duration_ticks: int = 0

func validate() -> Error:
	if not StableId.is_valid(decision_id) or not StableId.is_valid(case_id):
		return ERR_INVALID_DATA
	if not CharacterId.is_valid(target_character_id):
		return ERR_INVALID_DATA
	if fine_amount_minor < 0 or fine_amount_minor > 9007199254740991:
		return ERR_INVALID_DATA
	if fine_amount_minor > 0 and not StableId.is_valid(fine_currency_id):
		return ERR_INVALID_DATA
	if fine_amount_minor == 0 and not fine_currency_id.is_empty():
		if not StableId.is_valid(fine_currency_id):
			return ERR_INVALID_DATA
	if duration_ticks < 0 or duration_ticks > 9007199254740991:
		return ERR_INVALID_DATA
	if confiscated_entry_ids.size() > 256:
		return ERR_OUT_OF_MEMORY
	if restriction_ids.size() > 64 or affected_domain_ids.size() > 64:
		return ERR_OUT_OF_MEMORY
	if _validate_unique_ids(confiscated_entry_ids) != OK:
		return ERR_INVALID_DATA
	if _validate_unique_ids(restriction_ids) != OK:
		return ERR_INVALID_DATA
	return _validate_unique_ids(affected_domain_ids)

func has_effects() -> bool:
	return (
		fine_amount_minor > 0
		or not confiscated_entry_ids.is_empty()
		or not restriction_ids.is_empty()
		or not affected_domain_ids.is_empty()
	)

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

- Le plan décrit les effets décidés sans les appliquer.
- Les amendes utilisent les unités mineures du chapitre 21.
- Les confiscations référencent des entrées possédées par l’inventaire.
- Les restrictions institutionnelles restent distinctes des dégâts ou états de combat.
- Les domaines sont seulement référencés pour un adaptateur futur.

## 36. Ports de préparation des sanctions

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/sanction_economy_port.gd`.**

```gdscript
class_name SanctionEconomyPort
extends RefCounted

class PreparedFine:
	extends RefCounted
	var authority_id: StringName = &"economy"
	var payload: Dictionary = {}

	func validate() -> Error:
		return OK if authority_id == &"economy" and not payload.is_empty() else ERR_INVALID_DATA

func prepare_fine(
	_plan: SanctionPlan,
	_expected_wallet_revision: int,
) -> PreparedFine:
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’économie prépare elle-même les écritures équilibrées de l’amende.
- Le système judiciaire fournit un montant décidé et une cible, jamais un solde.
- Le payload opaque empêche la politique de contourner les règles de portefeuille.
- Une absence de fonds produit un résultat métier défini par la politique économique.
- Aucun portefeuille n’est modifié pendant la préparation.

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/sanction_inventory_port.gd`.**

```gdscript
class_name SanctionInventoryPort
extends RefCounted

class PreparedConfiscation:
	extends RefCounted
	var authority_id: StringName = &"inventory"
	var payload: Dictionary = {}

	func validate() -> Error:
		return OK if authority_id == &"inventory" and not payload.is_empty() else ERR_INVALID_DATA

func prepare_confiscation(
	_plan: SanctionPlan,
	_expected_container_revisions: Dictionary[StringName, int],
) -> PreparedConfiscation:
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’inventaire vérifie propriété, garde, équipement et révisions.
- Le plan judiciaire ne retire aucun objet directement.
- Le candidat peut transférer vers un conteneur institutionnel défini par composition.
- Les objets équipés suivent encore les invariants du chapitre 20.
- Un échec laisse tous les conteneurs inchangés.

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/sanction_character_port.gd`.**

```gdscript
class_name SanctionCharacterPort
extends RefCounted

class PreparedRestriction:
	extends RefCounted
	var authority_id: StringName = &"characters"
	var payload: Dictionary = {}

	func validate() -> Error:
		return OK if authority_id == &"characters" and not payload.is_empty() else ERR_INVALID_DATA

func prepare_restrictions(
	_plan: SanctionPlan,
	_expected_character_revision: int,
) -> PreparedRestriction:
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le port prépare seulement les restrictions appartenant aux personnages ou à leur présence.
- Une sanction ne modifie jamais directement santé, endurance ou état de vie.
- L’adaptateur peut refuser une restriction incompatible avec l’état courant.
- Les restrictions durables portent des identifiants et ticks logiques.
- Les animations et cellules physiques restent de la présentation.

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/sanction_domain_port.gd`.**

```gdscript
class_name SanctionDomainPort
extends RefCounted

class PreparedDomainChange:
	extends RefCounted
	var authority_id: StringName = &"domains"
	var payload: Dictionary = {}

	func validate() -> Error:
		return OK if authority_id == &"domains" and not payload.is_empty() else ERR_INVALID_DATA

func prepare_domain_changes(
	_plan: SanctionPlan,
	_expected_domain_revisions: Dictionary[StringName, int],
) -> PreparedDomainChange:
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Ce port réserve la frontière avec les domaines et bâtiments sans les implémenter dans le système judiciaire.
- L’adaptateur propriétaire vérifiera les identités de domaine, les droits et les révisions.
- Une destitution territoriale ou saisie foncière reste un candidat opaque.
- Le chapitre politique ne crée ni bâtiment, ni chaîne de production, ni propriété foncière.
- Tant que l’adaptateur n’existe pas, toute sanction comportant un domaine est refusée de façon fermée.

## 37. Commit coordonné

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/political_justice_commit_port.gd`.**

```gdscript
class_name PoliticalJusticeCommitPort
extends RefCounted

func commit_political(
	_aggregate_candidate: RefCounted,
	_expected_revision: int,
	_result: PoliticalCommandResult,
	_command_id: StringName,
	_command_fingerprint: String,
) -> Error:
	return ERR_UNAVAILABLE

func commit_case(
	_case_candidate: JusticeCaseState,
	_expected_case_revision: int,
	_result: PoliticalCommandResult,
	_command_id: StringName,
	_command_fingerprint: String,
) -> Error:
	return ERR_UNAVAILABLE

func commit_verdict_and_sanctions(
	_case_candidate: JusticeCaseState,
	_expected_case_revision: int,
	_verdict: VerdictDecision,
	_fine_candidate: SanctionEconomyPort.PreparedFine,
	_confiscation_candidate: SanctionInventoryPort.PreparedConfiscation,
	_restriction_candidate: SanctionCharacterPort.PreparedRestriction,
	_domain_candidate: SanctionDomainPort.PreparedDomainChange,
	_result: PoliticalCommandResult,
	_command_id: StringName,
	_command_fingerprint: String,
) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `commit_political()` couvre les adhésions, mandats et promulgations déjà préparés.
- `commit_case()` ouvre ou fait évoluer un dossier tout en enregistrant son résultat idempotent.
- Le commit de verdict revalide les révisions de toutes les autorités et accepte des candidats externes nuls seulement lorsque l’effet correspondant est absent.
- Verdict, dossier, sanctions, identité de commande, empreinte et résultat sont enregistrés comme un lot.
- Un échec ne laisse ni amende, ni confiscation, ni restriction, ni changement de domaine partiel ; l’atomicité réelle reste une réserve runtime.

## 38. Service judiciaire

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/justice_service.gd`.**

```gdscript
class_name JusticeService
extends RefCounted

signal verdict_committed(result: PoliticalCommandResult)

var _political_repository: PoliticalRepository
var _repository: JusticeRepository
var _authorization: PoliticalAuthorizationService
var _economy: SanctionEconomyPort
var _inventory: SanctionInventoryPort
var _characters: SanctionCharacterPort
var _domains: SanctionDomainPort
var _commit: PoliticalJusticeCommitPort

func issue_verdict(
	command_id: StringName,
	fingerprint: String,
	case_id: StringName,
	expected_case_revision: int,
	verdict: VerdictDecision,
	plan: SanctionPlan,
	judge_character_id: StringName,
	logical_tick: int,
	expected_wallet_revision: int,
	expected_container_revisions: Dictionary[StringName, int],
	expected_character_revision: int,
	expected_domain_revisions: Dictionary[StringName, int],
) -> PoliticalCommandResult:
	if not _basic_input_is_valid(
		command_id, fingerprint, case_id, expected_case_revision,
		judge_character_id, logical_tick,
	):
		return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_INVALID_COMMAND)
	if not _is_configured():
		return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_INTERNAL)
	var replay := _political_repository.find_command_result(command_id, fingerprint)
	if replay != null:
		replay.status = PoliticalCommandResult.Status.REPLAYED
		return replay
	if _political_repository.has_conflicting_fingerprint(command_id, fingerprint):
		return _rejected(
			command_id,
			case_id,
			PoliticalCommandResult.Status.REJECTED_IDEMPOTENCY_CONFLICT,
		)

	var source := _repository.get_case(case_id)
	if source == null:
		return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_NOT_FOUND)
	if source.revision != expected_case_revision:
		return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_STALE_REVISION)
	if verdict == null or verdict.validate() != OK:
		return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_INVALID_COMMAND)
	if verdict.case_id != case_id or verdict.case_revision != source.revision:
		return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_STALE_REVISION)
	if verdict.decided_by_character_id != judge_character_id or verdict.decided_tick != logical_tick:
		return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_INVALID_COMMAND)
	if not _plan_matches(source, verdict, plan):
		return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_INVALID_COMMAND)

	var context := AuthorizationContext.for_action(
		&"politics.action.issue_verdict",
		judge_character_id,
		source.institution_id,
		source.jurisdiction_id,
		logical_tick,
	)
	var access := _authorization.decide(context)
	if access == null or not access.is_allowed():
		return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_UNAUTHORIZED)
	var candidate := _prepare_decided_case(source, verdict)
	if candidate == null:
		return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_CONFLICT)

	var fine_candidate: SanctionEconomyPort.PreparedFine = null
	var confiscation_candidate: SanctionInventoryPort.PreparedConfiscation = null
	var restriction_candidate: SanctionCharacterPort.PreparedRestriction = null
	var domain_candidate: SanctionDomainPort.PreparedDomainChange = null
	if plan != null:
		if plan.fine_amount_minor > 0:
			if _economy == null:
				return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_EXTERNAL_PREPARATION)
			fine_candidate = _economy.prepare_fine(plan, expected_wallet_revision)
			if fine_candidate == null or fine_candidate.validate() != OK:
				return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_EXTERNAL_PREPARATION)
		if not plan.confiscated_entry_ids.is_empty():
			if _inventory == null:
				return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_EXTERNAL_PREPARATION)
			confiscation_candidate = _inventory.prepare_confiscation(
				plan,
				expected_container_revisions,
			)
			if confiscation_candidate == null or confiscation_candidate.validate() != OK:
				return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_EXTERNAL_PREPARATION)
		if not plan.restriction_ids.is_empty():
			if _characters == null:
				return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_EXTERNAL_PREPARATION)
			restriction_candidate = _characters.prepare_restrictions(
				plan,
				expected_character_revision,
			)
			if restriction_candidate == null or restriction_candidate.validate() != OK:
				return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_EXTERNAL_PREPARATION)
		if not plan.affected_domain_ids.is_empty():
			if _domains == null:
				return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_EXTERNAL_PREPARATION)
			domain_candidate = _domains.prepare_domain_changes(
				plan,
				expected_domain_revisions,
			)
			if domain_candidate == null or domain_candidate.validate() != OK:
				return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_EXTERNAL_PREPARATION)

	var result := PoliticalCommandResult.new()
	result.status = PoliticalCommandResult.Status.COMMITTED
	result.command_id = command_id
	result.aggregate_id = case_id
	result.decision_id = verdict.decision_id
	result.message = "verdict et sanctions committés"
	if result.validate() != OK:
		return _rejected(command_id, case_id, PoliticalCommandResult.Status.REJECTED_INTERNAL)
	var code := _commit.commit_verdict_and_sanctions(
		candidate,
		expected_case_revision,
		verdict,
		fine_candidate,
		confiscation_candidate,
		restriction_candidate,
		domain_candidate,
		result,
		command_id,
		fingerprint,
	)
	if code != OK:
		return _rejected(
			command_id,
			case_id,
			PoliticalCommandResult.Status.REJECTED_STALE_REVISION
			if code == ERR_BUSY
			else PoliticalCommandResult.Status.REJECTED_INTERNAL,
		)
	verdict_committed.emit(result)
	return result

func _prepare_decided_case(
	source: JusticeCaseState,
	verdict: VerdictDecision,
) -> JusticeCaseState:
	if source.status not in [
		JusticeCaseState.Status.READY_FOR_HEARING,
		JusticeCaseState.Status.APPEALED,
	]:
		return null
	if source.decisions.has(verdict.decision_id):
		return null
	var candidate := source.duplicate_detached()
	candidate.decisions[verdict.decision_id] = verdict.duplicate_detached()
	match verdict.outcome:
		VerdictDecision.Outcome.DISMISSED:
			candidate.status = JusticeCaseState.Status.DISMISSED
		VerdictDecision.Outcome.MISTRIAL:
			candidate.status = JusticeCaseState.Status.READY_FOR_HEARING
		_:
			candidate.status = JusticeCaseState.Status.DECIDED
	candidate.revision += 1
	return candidate if candidate.validate() == OK else null

func _plan_matches(
	source: JusticeCaseState,
	verdict: VerdictDecision,
	plan: SanctionPlan,
) -> bool:
	if verdict.outcome != VerdictDecision.Outcome.GUILTY:
		return plan == null
	if plan == null or plan.validate() != OK or not plan.has_effects():
		return false
	return (
		plan.case_id == source.case_id
		and plan.decision_id == verdict.decision_id
		and plan.target_character_id == source.accused_character_id
	)

func _basic_input_is_valid(
	command_id: StringName,
	fingerprint: String,
	case_id: StringName,
	expected_case_revision: int,
	judge_character_id: StringName,
	logical_tick: int,
) -> bool:
	return (
		StableId.is_valid(command_id)
		and StableId.is_valid(case_id)
		and CharacterId.is_valid(judge_character_id)
		and expected_case_revision >= 0
		and logical_tick >= 0
		and not fingerprint.is_empty()
		and fingerprint.length() <= 128
	)

func _is_configured() -> bool:
	return (
		_political_repository != null
		and _repository != null
		and _authorization != null
		and _commit != null
	)

func _rejected(
	command_id: StringName,
	case_id: StringName,
	status: PoliticalCommandResult.Status,
) -> PoliticalCommandResult:
	var result := PoliticalCommandResult.new()
	result.status = status
	if StableId.is_valid(command_id):
		result.command_id = command_id
	if StableId.is_valid(case_id):
		result.aggregate_id = case_id
	result.message = PoliticalCommandResult.Status.keys()[status]
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Replay et conflit d’empreinte sont traités avant toute préparation afin qu’un retry ne répète jamais une sanction.
- Le dossier, le verdict, le juge, le tick et la révision sont recoupés ; une condamnation exige un plan valide ciblant l’accusé.
- Les quatre autorités externes sont facultatives seulement lorsque le plan ne demande aucun effet de leur famille.
- Chaque candidat est préparé et validé avant la création du résultat committé.
- Le signal est émis uniquement après le commit coordonné qui enregistre aussi le verdict et l’idempotence.

### 38.1 Ordre de préparation d’un verdict

L’ordre retenu est :

1. valider la commande, l’identité et l’empreinte ;
2. rechercher un replay ou un conflit d’idempotence ;
3. relire le dossier et sa révision ;
4. valider le verdict, son juge, son tick et sa corrélation au dossier ;
5. recalculer l’autorisation du juge ;
6. préparer le dossier candidat ;
7. préparer l’amende, la confiscation, les restrictions et les domaines nécessaires ;
8. revalider chaque candidat ;
9. committer le lot ;
10. émettre les événements.

Aucun effet n’est appliqué entre les étapes 1 et 8.

## 39. Événements politiques et judiciaires

> **[LECTURE] Événement committé — Structure de référence.**

```gdscript
class_name JusticeVerdictCommittedEvent
extends RefCounted

var event_id: StringName
var decision_id: StringName
var case_id: StringName
var institution_id: StringName
var jurisdiction_id: StringName
var accused_character_id: StringName
var outcome: VerdictDecision.Outcome
var decided_tick: int = 0
var case_revision: int = 0
var applied_law_refs: Array[String] = []
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’événement décrit un verdict déjà committé.
- Les identifiants permettent aux consommateurs de relire leurs propres données.
- Les lois appliquées sont référencées par identité et version.
- Aucun payload de portefeuille, d’inventaire ou de personnage n’est exposé.
- La révision permet d’ignorer un événement devenu ancien.

## 40. Observations pour les agents et la narration

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/political_agent_observation_port.gd`.**

```gdscript
class_name PoliticalAgentObservationPort
extends RefCounted

class Observation:
	extends RefCounted
	var character_id: StringName
	var logical_tick: int = 0
	var membership_ids: Array[StringName] = []
	var active_mandate_ids: Array[StringName] = []
	var applicable_right_ids: Array[StringName] = []
	var open_case_ids: Array[StringName] = []

	func validate() -> Error:
		if not CharacterId.is_valid(character_id) or logical_tick < 0:
			return ERR_INVALID_DATA
		if membership_ids.size() > 128 or active_mandate_ids.size() > 64:
			return ERR_OUT_OF_MEMORY
		if applicable_right_ids.size() > 256 or open_case_ids.size() > 128:
			return ERR_OUT_OF_MEMORY
		var all_lists: Array = [
			membership_ids,
			active_mandate_ids,
			applicable_right_ids,
			open_case_ids,
		]
		for values: Array in all_lists:
			var seen: Dictionary[StringName, bool] = {}
			for stable_id: StringName in values:
				if not StableId.is_valid(stable_id) or seen.has(stable_id):
					return ERR_INVALID_DATA
				seen[stable_id] = true
		return OK

func snapshot_for(_character_id: StringName, _logical_tick: int) -> Observation:
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’observation contient des identifiants et droits calculés, pas les agrégats internes.
- Les agents transforment ces données en faits selon le chapitre 17.
- Une intention d’agent repasse par une commande politique ou judiciaire.
- Les dossiers ouverts sont bornés et filtrés par visibilité.
- Une sortie générative ne peut pas remplacer ce snapshot.

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/application/political_narrative_event_port.gd`.**

```gdscript
class_name PoliticalNarrativeEventPort
extends RefCounted

func publish_committed_event(
	_event_id: StringName,
	_event_kind_id: StringName,
	_subject_ids: Array[StringName],
	_logical_tick: int,
	_payload: Dictionary,
) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le port transmet à la narration uniquement des événements déjà committés.
- Le chapitre 25 choisira quêtes, scènes et conséquences sans modifier le verdict source.
- Les sujets sont identifiés et le payload est borné par l’adaptateur.
- Une indisponibilité narrative n’annule pas un commit politique.
- Le port ne sert jamais à demander une décision judiciaire.

## 41. Présentation

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/presentation/political_presentation_bridge.gd`.**

```gdscript
class_name PoliticalPresentationBridge
extends Node

signal political_feedback_requested(
	aggregate_id: StringName,
	feedback_id: StringName,
)

var _latest_feedback_by_aggregate: Dictionary[StringName, StringName] = {}

func on_command_committed(result: PoliticalCommandResult) -> void:
	if result == null or result.validate() != OK or not result.is_success():
		return
	var feedback_id := result.decision_id
	if feedback_id.is_empty():
		feedback_id = result.command_id
	if not StableId.is_valid(feedback_id):
		return
	if _latest_feedback_by_aggregate.get(result.aggregate_id, &"") == feedback_id:
		return
	_latest_feedback_by_aggregate[result.aggregate_id] = feedback_id
	political_feedback_requested.emit(result.aggregate_id, feedback_id)
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le pont accepte seulement un résultat validé et réussi.
- Un verdict utilise `decision_id` ; une adhésion, nomination, promulgation ou ouverture de dossier utilise l’identité de commande.
- Le cache évite de rejouer le même retour pour un agrégat et reste non persistant.
- Les identifiants permettent à la vue de relire un modèle adapté sans exposer d’état mutable.
- Aucun rang, loi, dossier ou sanction n’est modifié depuis le nœud.

L’interface peut afficher les adhésions, rangs, mandats, lois applicables, droits actifs, étapes d’un dossier, preuves recevables et verdicts. Elle ne doit pas changer directement un statut, promulguer une loi, marquer une preuve recevable, calculer une culpabilité ou appliquer une sanction.

## 42. Persistance

Sont persistés :

- les adhésions, rangs détenus, statuts, ticks et révisions ;
- les mandats, titulaires, juridictions, périodes et causes ;
- le recueil de promulgations et ses révisions ;
- les dossiers, allégations, preuves, participants, statuts et verdicts ;
- les séquences d’événements ;
- les identités, empreintes et résultats récents d’idempotence ;
- la version de format.

Ne sont pas persistés :

- les définitions `.tres` ;
- les droits dérivés ;
- les décisions d’autorisation transitoires ;
- les index secondaires reconstructibles ;
- les contextes d’évaluation ;
- les commandes et candidats en attente ;
- les observations d’agents et événements narratifs dérivés ;
- les vues, filtres, tris et caches de présentation ;
- les portefeuilles, objets, états de personnage, régions ou domaines possédés par d’autres systèmes.

## 43. Codec strict

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/infrastructure/political_snapshot_section_decoder.gd`.**

```gdscript
class_name PoliticalSnapshotSectionDecoder
extends RefCounted

func decode_sections(
	_document: Dictionary,
	_catalog: PoliticalCatalog,
) -> Variant:
	return null

func validate_prepared(
	_prepared: Dictionary,
	_catalog: PoliticalCatalog,
) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le décodeur de sections possède une responsabilité bornée : construire factions, recueil, dossiers et registre d’idempotence hors des dépôts actifs.
- Son implémentation exige les clés exactes de chaque objet, les types JSON attendus, les bornes et les références croisées.
- Le retour `Variant` permet de réserver `{}` à un état préparé vide mais valide et `null` à un échec de décodage.
- `validate_prepared()` revalide l’ensemble après décodage afin de détecter les références entre sections.
- Ce contrat sépare la lecture volumineuse des entités de la validation du format racine sans rendre les contrôles facultatifs.

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/infrastructure/political_snapshot_codec.gd`.**

```gdscript
class_name PoliticalSnapshotCodec
extends RefCounted

const FORMAT := "project-asteria-politics-justice"
const VERSION := 1
const ROOT_KEYS := [
	"format",
	"version",
	"factions",
	"law_book",
	"cases",
	"idempotency",
]

class DecodeResult:
	extends RefCounted
	var code: Error = FAILED
	var prepared: Dictionary = {}
	var message: String = ""

	func is_success() -> bool:
		return code == OK

var _sections: PoliticalSnapshotSectionDecoder

func decode(document: Dictionary, catalog: PoliticalCatalog) -> DecodeResult:
	if catalog == null or _sections == null:
		return _failure(ERR_UNCONFIGURED, "dépendance absente")
	if not _has_exact_keys(document, ROOT_KEYS):
		return _failure(ERR_INVALID_DATA, "clés racine invalides")
	if typeof(document.get("format")) != TYPE_STRING:
		return _failure(ERR_INVALID_DATA, "format non textuel")
	if String(document.get("format")) != FORMAT:
		return _failure(ERR_FILE_UNRECOGNIZED, "format inconnu")
	var version_value := _read_int(document.get("version"), 1, VERSION)
	if version_value == null or int(version_value) != VERSION:
		return _failure(ERR_FILE_UNRECOGNIZED, "version inconnue")
	var prepared: Variant = _sections.decode_sections(document, catalog)
	if prepared == null or typeof(prepared) != TYPE_DICTIONARY:
		return _failure(ERR_INVALID_DATA, "sections invalides")
	if _sections.validate_prepared(prepared, catalog) != OK:
		return _failure(ERR_INVALID_DATA, "état politique invalide")
	var result := DecodeResult.new()
	result.code = OK
	result.prepared = (prepared as Dictionary).duplicate(true)
	return result

func _has_exact_keys(document: Dictionary, expected: Array[String]) -> bool:
	if document.size() != expected.size():
		return false
	for key: String in expected:
		if not document.has(key):
			return false
	return true

func _read_int(value: Variant, minimum: int, maximum: int) -> Variant:
	if typeof(value) != TYPE_INT:
		return null
	var parsed := int(value)
	return parsed if parsed >= minimum and parsed <= maximum else null

func _failure(code: Error, message: String) -> DecodeResult:
	var result := DecodeResult.new()
	result.code = code
	result.message = message
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le codec exige exactement les clés prévues et vérifie séparément type, format et version.
- `_read_int()` refuse les nombres flottants et les entiers hors de la plage demandée.
- Le décodeur de sections doit retourner `null` lors d’un échec ; `{}` reste disponible pour un monde politique vide mais valide.
- Le candidat complet est revalidé contre le catalogue avant d’être copié dans `DecodeResult`.
- Aucune faction, loi ou affaire n’est appliquée aux dépôts pendant le décodage.

## 44. Section de sauvegarde

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/infrastructure/political_restore_commit_port.gd`.**

```gdscript
class_name PoliticalRestoreCommitPort
extends RefCounted

func replace_all(_prepared: Dictionary) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le port appartient au point de composition qui connaît les deux dépôts et leur transaction de restauration.
- Il reçoit uniquement un candidat déjà décodé, recoupé et copié.
- L’implémentation remplace politique, justice et idempotence comme un lot ou ne remplace rien.
- Elle ne relance ni enquête, ni sanction, ni événement de gameplay pendant le chargement.
- Un échec laisse les dépôts actifs inchangés.

> **[VSC] Visual Studio Code — Créer : `res://src/features/politics/infrastructure/political_save_section.gd`.**

```gdscript
class_name PoliticalSaveSection
extends SaveSection

var _catalog: PoliticalCatalog
var _codec := PoliticalSnapshotCodec.new()
var _restore_commit: PoliticalRestoreCommitPort
var _prepared: Dictionary = {}
var _is_prepared := false

func section_id() -> StringName:
	return &"politics_justice"

func prepare_restore(payload: Dictionary) -> Error:
	_prepared.clear()
	_is_prepared = false
	if _catalog == null or _restore_commit == null:
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
	var code := _restore_commit.replace_all(_prepared.duplicate(true))
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

- La section prépare la totalité de la politique et de la justice avant toute application.
- Le codec et le port de commit sont configurés avant la lecture du payload.
- Les données sont copiées avant stockage puis avant transmission au point de composition.
- Une autre section peut provoquer `cancel_restore()` sans mutation partielle.
- L’application remplace les deux dépôts et l’idempotence par une seule opération, sans émettre les événements historiques comme des faits nouveaux.

## 45. Scène pédagogique

La scène `ch23_politics_justice_demo.tscn` doit montrer :

1. une institution, deux factions et plusieurs rangs ;
2. une adhésion valide et un refus de doublon ;
3. une nomination avec fonction, titulaire et juridiction ;
4. une loi promulguée avec date d’effet future ;
5. une autorisation refusée avant l’effet puis accordée après ;
6. une infraction rapportée sans verdict automatique ;
7. deux preuves avec provenance et recevabilité distinctes ;
8. un enquêteur autorisé et un autre refusé ;
9. un verdict d’acquittement ;
10. un verdict de culpabilité avec plan de sanction ;
11. un échec de préparation d’inventaire sans effet partiel ;
12. un retry idempotent renvoyant `REPLAYED` ;
13. une sauvegarde et restauration des adhésions, mandats, lois et dossiers.

## 46. Modes Solo et Studio

### 46.1 Mode Solo

- quelques institutions et factions ;
- définitions `.tres` locales ;
- un recueil de lois versionné ;
- dossiers bornés ;
- décisions synchrones et déterministes ;
- adaptateurs locaux pour amendes et confiscations ;
- événements récents ;
- aucune dépendance obligatoire à un service IA.

### 46.2 Mode Studio

- catalogues revus et versionnés ;
- matrices de droits et juridictions ;
- scénarios judiciaires de référence ;
- tests de propriété sur les transitions ;
- replays déterministes ;
- outils de visualisation des lois applicables ;
- audit de chaîne de garde ;
- séparation des responsabilités de conception ;
- simulations massives hors runtime ;
- validation des commits multi-autorités.

Le Mode Studio améliore l’outillage et la revue. Il ne crée pas une autorité globale capable de modifier directement tous les systèmes.

## 47. Budgets, sécurité et diagnostics

Bornes pédagogiques :

| Élément | Borne |
|---|---:|
| institutions | 1 024 |
| factions | 4 096 |
| adhésions par faction | 100 000 |
| mandats par faction | 4 096 |
| versions par loi | 1 000 |
| promulgations | 100 000 |
| dossiers ouverts | 10 000 |
| preuves par dossier | 512 |
| participants par dossier | 128 |
| résultats idempotents récents | 4 096 |

Ces bornes devront être mesurées et ajustées au chapitre 27.

Journaliser :

- identité de commande et empreinte non sensible ;
- agrégat, révision attendue et constatée ;
- institution, faction et juridiction ;
- loi, version et période d’effet ;
- statut du dossier et décision ;
- identités des candidats externes ;
- refus d’autorisation, conflit et idempotence ;
- durée matérielle des évaluations.

Ne pas journaliser les témoignages complets, conversations privées, secrets, inventaires non concernés, soldes complets, sorties génératives brutes ou informations personnelles inutiles.

## 48. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 48.1 Utiliser le nom affiché comme identité de faction

**Symptôme ou risque :** changer la langue ou renommer la faction casse adhésions et lois.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var faction_key := faction_display_name
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le texte localisé n’est pas une identité stable.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var faction_id := PoliticalId.faction("river_council")
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’identité reste stable indépendamment de l’affichage.

### 48.2 Déduire une adhésion depuis l’affinité

**Symptôme ou risque :** un ami d’un membre devient automatiquement membre sans décision institutionnelle.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if social_view.affinity > 80:
	membership.status = MembershipState.Status.ACTIVE
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une perception sociale n’est ni une admission ni un droit.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var result := membership_service.execute(join_command)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** une commande causale repasse par capacité, rang, révision et autorisation.

### 48.3 Modifier une loi promulguée en place

**Symptôme ou risque :** les décisions passées changent lorsque la ressource est éditée.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
law.effect = LawDefinition.Effect.ALLOW
law.version = 2
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la même instance réécrit l’historique applicable.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
catalog.register_law(new_version)
legislative_service.enact(enact_command)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** une nouvelle version est enregistrée puis promulguée avec sa propre période.

### 48.4 Autoriser par absence de règle

**Symptôme ou risque :** une panne de catalogue ou une loi manquante devient une permission.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if matching_laws.is_empty():
	return true
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** absence de règle et autorisation explicite sont confondues.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var decision := authorization_service.decide(context)
if decision.outcome == AuthorizationDecision.Outcome.ALLOW:
	perform_action()
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** seul le résultat `ALLOW` autorise l’action protégée.

### 48.5 Traiter une accusation comme un verdict

**Symptôme ou risque :** un rapport applique immédiatement une sanction.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
report_infraction(command)
apply_fine(accused_id, 500)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le rapport n’a ni enquête, ni preuve, ni décision.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var case_result := justice_service.open_case(command)
# Les sanctions attendent un verdict committé.
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le dossier est ouvert sans présumer de la culpabilité.

### 48.6 Copier un objet comme preuve

**Symptôme ou risque :** la justice devient propriétaire d’une copie divergente de l’inventaire.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
evidence.payload = inventory_entry.duplicate(true)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** l’objet copié peut diverger de l’autorité et contourner sa garde.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
evidence.source_id = inventory_entry.entry_id
evidence.integrity_digest = inventory_reference_digest
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la preuve référence l’objet et vérifie son intégrité sans le posséder.

### 48.7 Laisser une sortie IA condamner

**Symptôme ou risque :** un texte génératif devient une décision autoritaire.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
verdict.outcome = ai_response["outcome"]
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la sortie non fiable contourne lois, preuves, juge et révisions.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var suggestion := ai_gateway.suggest_case_summary(case_view)
var draft := verdict_draft_policy.filter(suggestion)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la sortie reste un brouillon non autoritaire soumis à une décision validée.

### 48.8 Débiter une amende directement

**Symptôme ou risque :** un échec ultérieur de confiscation laisse une sanction partielle.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
wallet.balance_minor -= fine
inventory.remove(confiscated_id)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** les autorités sont modifiées séquentiellement sans rollback commun.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var fine_candidate := economy_port.prepare_fine(plan, wallet_revision)
var item_candidate := inventory_port.prepare_confiscation(plan, revisions)
commit_port.commit_verdict_and_sanctions(case_candidate, case_revision, verdict, fine_candidate, item_candidate, restriction_candidate, result, command_id, fingerprint)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** tous les candidats sont préparés puis committés comme un lot.

### 48.9 Dater un mandat avec l’heure système

**Symptôme ou risque :** modifier l’horloge de la machine change la durée institutionnelle.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
mandate.started_tick = int(Time.get_unix_time_from_system())
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le temps réel (temps horloge) ne fait pas partie de la simulation sauvegardée.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
mandate.started_tick = world_clock.logical_tick
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le mandat utilise l’horloge logique persistée du monde.

### 48.10 Émettre un événement avant le commit

**Symptôme ou risque :** l’interface ou la narration réagit à une décision ensuite refusée.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
verdict_committed.emit(result)
var code := commit_port.commit_verdict_and_sanctions(...)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** les consommateurs observent un fait qui n’existe peut-être pas.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var code := commit_port.commit_verdict_and_sanctions(...)
if code == OK:
	verdict_committed.emit(result)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’événement décrit uniquement un lot déjà committé.

## 49. Tests à préparer

### 49.1 Tests unitaires

- identifiants politiques ;
- validation des définitions ;
- versions de lois immuables ;
- intervalles d’adhésion et de mandat ;
- index d’adhésions ouvertes ;
- tri déterministe des lois ;
- collecte de droits actifs ;
- politique deny-by-default ;
- cycle de vie des dossiers ;
- validation des preuves ;
- décisions de verdict ;
- plans de sanction ;
- codec strict.

### 49.2 Tests d’intégration

- admission, changement de rang, suspension et fin d’adhésion ;
- nomination, vacance, révocation et fin planifiée ;
- promulgation et entrée en vigueur ;
- juridictions globales et locales ;
- autorisation par rang et mandat ;
- conflit de lois et priorité ;
- rapport d’infraction sans sanction ;
- ajout de preuve autorisé et refusé ;
- verdict avec révision obsolète ;
- verdict acquitté sans candidat de sanction ;
- condamnation avec amende, confiscation et restriction ;
- échec d’un candidat externe sans effet partiel ;
- replay et conflit d’empreinte ;
- sauvegarde et restauration.

### 49.3 Simulations

- 1, 64 et 4 096 factions ;
- 1, 10 000 et 100 000 adhésions ;
- 1 à 1 000 versions d’une loi ;
- 1 à 10 000 dossiers ouverts ;
- 1, 64 et 512 preuves par dossier ;
- changements de juridiction sur plusieurs milliers de ticks ;
- 100 000 décisions d’autorisation comparées entre replays ;
- sanctions concurrentes sur le même portefeuille ou objet ;
- sauvegarde pendant un dossier en enquête puis reprise.

## 50. Réserves runtime

Cette revue statique ne prouve pas :

- le passage de tous les extraits dans le parseur Godot 4.7.1 ;
- le comportement de toutes les collections typées ;
- l’atomicité réelle entre politique, justice, économie, inventaire et personnages ;
- la stabilité avec 100 000 adhésions ou 10 000 dossiers ;
- la performance du calcul des lois applicables ;
- l’exactitude d’adaptateurs de juridiction futurs ;
- la matérialisation d’une audience ou d’une détention ;
- la coordination avec les domaines et bâtiments ;
- les conséquences narratives ;
- l’équilibrage des droits, preuves et sanctions ;
- la reproductibilité interplateforme ;
- l’instanciation de la scène pédagogique ;
- l’exécution du codec et d’une migration future ;
- la génération d’un PDF intermédiaire.

## 51. Sources techniques

- [Godot 4.7 — `Resource`](https://docs.godotengine.org/en/4.7/classes/class_resource.html)
- [Godot 4.7 — `RefCounted`](https://docs.godotengine.org/en/4.7/classes/class_refcounted.html)
- [Godot 4.7 — `Array`](https://docs.godotengine.org/en/4.7/classes/class_array.html)
- [Godot 4.7 — `Dictionary`](https://docs.godotengine.org/en/4.7/classes/class_dictionary.html)
- [Godot 4.7 — `StringName`](https://docs.godotengine.org/en/4.7/classes/class_stringname.html)
- [Godot 4.7 — `Time`](https://docs.godotengine.org/en/4.7/classes/class_time.html)
- [Godot 4.7 — bases de GDScript et entier 64 bits](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/gdscript_basics.html)
- [Chapitre 9 — Sauvegardes, chargements et compatibilité](CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md)
- [Chapitre 14 — Personnages](CHAPITRE-14-Personnages.md)
- [Chapitre 15 — Relations sociales](CHAPITRE-15-Relations-sociales.md)
- [Chapitre 16 — Famille et générations](CHAPITRE-16-Famille-et-generations.md)
- [Chapitre 17 — Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md)
- [Chapitre 20 — Inventaire et réputation des objets](CHAPITRE-20-Inventaire-et-reputation-des-objets.md)
- [Chapitre 21 — Économie](CHAPITRE-21-Economie.md)
- [Chapitre 22 — Monde vivant et simulation écologique](CHAPITRE-22-Monde-vivant-et-simulation-ecologique.md)

## 52. Synthèse opérationnelle pour Project Asteria

La politique et la justice de `Project Asteria` retiennent les décisions suivantes :

1. institutions, factions, rangs et fonctions utilisent des identifiants stables ;
2. les définitions de conception restent immuables pendant le gameplay ;
3. les adhésions et mandats sont des états vivants révisionnés ;
4. une relation sociale ou familiale ne crée aucun droit institutionnel implicite ;
5. les périodes utilisent l’horloge logique globale ;
6. une version de loi promulguée n’est jamais modifiée en place ;
7. les lois applicables sont sélectionnées par juridiction, période, action et priorité ;
8. les actions protégées suivent une politique deny-by-default ;
9. une accusation ouvre un dossier sans produire de verdict ;
10. les preuves sont identifiées, sourcées, bornées et distinctes des faits ;
11. les dossiers possèdent un cycle de vie explicite ;
12. un verdict référence les lois et preuves retenues ;
13. les sanctions sont décrites par un plan avant tout effet ;
14. l’économie, l’inventaire, les personnages, l’écologie et les domaines conservent leurs autorités ;
15. les effets externes sont préparés puis committés avec le dossier et le verdict ;
16. les commandes et décisions sont idempotentes et révisionnées ;
17. les événements sont émis uniquement après commit ;
18. les agents et la narration reçoivent des observations ou événements committés ;
19. une sortie IA reste consultative et ne peut ni promulguer ni condamner ;
20. adhésions, mandats, promulgations, dossiers, preuves, décisions, révisions et résultats idempotents sont persistés ;
21. définitions, droits dérivés, contextes, candidats, observations et présentation restent hors du snapshot.
