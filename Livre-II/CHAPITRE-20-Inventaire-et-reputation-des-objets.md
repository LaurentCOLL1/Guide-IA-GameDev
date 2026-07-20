---
title: "Livre II — Chapitre 20 : Inventaire et réputation des objets"
id: "DOC-L2-CH20"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 20
last-verified: "2026-07-20T17:32:42+02:00"
audit-status: "complete"
audit-date: "2026-07-20T17:32:42+02:00"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-20.md"
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

# Inventaire et réputation des objets

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH20`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Niveau de raisonnement conseillé :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-20.md`.

## 1. Rôle du chapitre

Le chapitre 19 a séparé les définitions de compétences, leur progression et leur état runtime. Il a aussi établi qu’un objet peut accorder une compétence sans devenir propriétaire de ses coûts, effets, charges ou recharges.

Ce chapitre construit l’autorité des **objets possédés** : définitions de conception, instances uniques, lots empilables, conteneurs, équipement, durabilité, propriété, provenance et réputation propre aux objets remarquables.

Le système doit garantir que :

- une `Resource` partagée reste une définition immuable ;
- une épée usée et une épée neuve ne deviennent jamais le même état ;
- un objet célèbre conserve une identité indépendante de son nom affiché ;
- une pile ne fusionne que des quantités réellement fongibles ;
- une mutation de transfert valide source et destination avant tout remplacement ;
- un objet équipé peut accorder une compétence sans modifier directement le système de compétences ;
- le combat demande une perte de durabilité sans écrire l’inventaire ;
- la réputation d’un objet provient d’événements métier validés, pas d’un texte génératif ;
- le chargement prépare l’ensemble des objets et conteneurs avant de remplacer l’état actif.

## 2. Prérequis

Le lecteur doit avoir parcouru :

- le chapitre 4 pour l’architecture feature-first ;
- le chapitre 5 pour les services injectés et le point de composition ;
- le chapitre 7 pour les `Resource`, catalogues et identifiants stables ;
- le chapitre 9 pour les sections de sauvegarde préparées avant application ;
- le chapitre 14 pour les identités de personnages ;
- le chapitre 17 pour les actions d’agents ;
- le chapitre 18 pour l’autorité du combat ;
- le chapitre 19 pour les compétences accordées par une source externe.

## 3. Périmètre et frontières

Ce chapitre couvre :

- définitions d’objets ;
- instances uniques ;
- lots et empilement ;
- conteneurs et capacités ;
- transfert, division et fusion ;
- équipement par emplacements explicites ;
- durabilité et état brisé ;
- propriété légale et garde matérielle ;
- provenance bornée et traçable ;
- réputation globale d’un objet identifié ;
- intégration avec les agents, le combat et les compétences ;
- persistance stricte et restauration préparée.

Il ne couvre pas :

- les prix, monnaies, achats, ventes, taxes et récompenses économiques ;
- les formules finales de dégâts, portée, défense ou pénétration ;
- les coûts, charges, recharges et effets des compétences ;
- la connaissance subjective d’un objet par chaque personnage ;
- les lois de propriété, vols et sanctions ;
- les récompenses de quête et conséquences narratives ;
- la fabrication et les bâtiments de production ;
- les outils d’édition de masse ;
- le multijoueur.

> **Frontière essentielle :** l’inventaire possède l’identité, l’emplacement, la quantité, l’équipement, la durabilité, la propriété, la provenance et la réputation des objets. Il ne recalcule jamais les règles propriétaires des systèmes voisins.

## 4. Chaîne d’autorité

> **[LECTURE] Flux d’une mutation d’inventaire — Ne pas saisir.**

```text
joueur / agent / combat / scénario / économie future
    ↓ commande typée ou demande de candidat
InventoryService
    ├── relit définitions, entrées, conteneurs et révisions
    ├── prépare les états source et destination
    ├── prépare propriété, provenance et réputation éventuelle
    └── demande les candidats externes requis
            ↓
InventoryMutationUnitOfWork
    ├── revalide toutes les révisions
    ├── valide l’ensemble des candidats
    ├── remplace les agrégats comme un lot
    └── refuse avant tout événement si une précondition échoue
            ↓
InventoryResult + événements typés
            ↓
présentation, agents, combat, compétences, narration
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Une commande exprime une intention ; elle ne contient pas le résultat final.
- Les conteneurs source et destination sont préparés sur des copies détachées.
- Les systèmes voisins préparent leurs propres candidats lorsque leurs autorités sont concernées.
- L’unité de travail revalide les révisions immédiatement avant le commit.
- Les événements et animations sont déclenchés seulement après réussite.

## 5. Architecture retenue

> **[LECTURE] Arborescence cible — Ne pas créer depuis un terminal.**

```text
res://src/features/inventory/
├── domain/
│   ├── item_id.gd
│   ├── item_owner_ref.gd
│   ├── inventory_entry_ref.gd
│   ├── item_definition.gd
│   ├── item_instance_state.gd
│   ├── item_stack_state.gd
│   ├── item_provenance_record.gd
│   ├── item_reputation_state.gd
│   ├── inventory_container_state.gd
│   ├── equipment_loadout_state.gd
│   ├── inventory_transfer_command.gd
│   └── inventory_result.gd
├── application/
│   ├── item_catalog.gd
│   ├── inventory_repository.gd
│   ├── inventory_mutation_candidate.gd
│   ├── inventory_mutation_unit_of_work.gd
│   ├── inventory_ability_grant_port.gd
│   ├── inventory_durability_port.gd
│   ├── item_reputation_policy.gd
│   ├── inventory_service.gd
│   └── inventory_agent_action_executor.gd
├── infrastructure/
│   ├── inventory_snapshot_codec.gd
│   └── inventory_save_section.gd
└── presentation/
    └── inventory_presentation_bridge.gd

res://data/items/
├── ashwood_staff.tres
├── field_ration.tres
└── starforged_blade.tres

res://scenes/learning/
├── ch20_inventory_demo.tscn
└── ch20_inventory_demo.gd
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `domain` contient les identités, états et invariants indépendants des scènes.
- `application` orchestre les mutations et les frontières avec les autres systèmes.
- `infrastructure` encode uniquement la persistance.
- `presentation` observe des résultats déjà committés.
- Les définitions `.tres` restent séparées des instances vivantes.

## 6. Vocabulaire

Une **définition d’objet** décrit une catégorie de contenu partagée : nom localisé, masse, politique de pile, emplacements d’équipement, durabilité maximale et compétences accordées.

Une **instance** est un objet individuel doté d’un identifiant propre. Elle peut porter une durabilité, une provenance et une réputation.

Un **lot** représente une quantité fongible d’une même définition et d’une même origine de lot. Il n’a ni durabilité individuelle, ni équipement, ni réputation propre.

Un **conteneur** possède une capacité et référence des instances ou lots.

La **propriété** désigne le titulaire métier de l’objet. La **garde** désigne le conteneur qui le détient matériellement.

La **provenance** conserve l’origine et des événements significatifs validés.

La **réputation d’objet** est une renommée globale attachée à une instance identifiable. La connaissance subjective de cette renommée par un personnage appartient aux systèmes de connaissances et de narration.

## 7. Identifiants et références de propriétaire

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/domain/item_id.gd`.**

```gdscript
class_name ItemId
extends RefCounted

const DEFINITION_PREFIX := "item.definition."
const INSTANCE_PREFIX := "item.instance."
const STACK_PREFIX := "item.stack."
const CONTAINER_PREFIX := "inventory.container."
const EVENT_PREFIX := "item.event."

static func definition(slug: String) -> StringName:
	return _from_slug(DEFINITION_PREFIX, slug)

static func instance(uuid_text: String) -> StringName:
	return _from_slug(INSTANCE_PREFIX, uuid_text)

static func stack(uuid_text: String) -> StringName:
	return _from_slug(STACK_PREFIX, uuid_text)

static func container(slug: String) -> StringName:
	return _from_slug(CONTAINER_PREFIX, slug)

static func event(entry_id: StringName, sequence: int) -> StringName:
	if not StableId.is_valid(entry_id) or sequence <= 0:
		return &""
	return StringName("%s%s.%d" % [EVENT_PREFIX, String(entry_id), sequence])

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

**Explication détaillée du bloc :**

- Chaque espace d’identité possède un préfixe distinct.
- `_from_slug()` normalise les tirets et refuse les caractères inattendus.
- `event()` corrèle un événement à une entrée et à une séquence positive.
- Une entrée invalide renvoie `&""`, jamais un identifiant partiel.
- Le nom affiché et le chemin du fichier ne participent pas à l’identité.

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/domain/item_owner_ref.gd`.**

```gdscript
class_name ItemOwnerRef
extends RefCounted

enum Kind {
	NONE,
	CHARACTER,
	WORLD,
	ORGANIZATION,
}

var kind: Kind = Kind.NONE
var owner_id: StringName

func validate() -> Error:
	if kind < Kind.NONE or kind > Kind.ORGANIZATION:
		return ERR_INVALID_DATA
	if kind == Kind.NONE:
		return OK if owner_id.is_empty() else ERR_INVALID_DATA
	return OK if StableId.is_valid(owner_id) else ERR_INVALID_DATA

func duplicate_detached() -> ItemOwnerRef:
	var copy := ItemOwnerRef.new()
	copy.kind = kind
	copy.owner_id = owner_id
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `kind` évite de confondre un personnage, le monde et une organisation future.
- `NONE` exige un identifiant vide.
- Les organisations peuvent être référencées sans définir ici leurs règles politiques.
- La copie détachée empêche un appelant de modifier la référence interne.

## 8. Référence d’entrée

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/domain/inventory_entry_ref.gd`.**

```gdscript
class_name InventoryEntryRef
extends RefCounted

enum Kind {
	INSTANCE,
	STACK,
}

var kind: Kind = Kind.INSTANCE
var entry_id: StringName

func validate() -> Error:
	if kind < Kind.INSTANCE or kind > Kind.STACK:
		return ERR_INVALID_DATA
	if not StableId.is_valid(entry_id):
		return ERR_INVALID_DATA
	return OK

func duplicate_detached() -> InventoryEntryRef:
	var copy := InventoryEntryRef.new()
	copy.kind = kind
	copy.entry_id = entry_id
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Une entrée est soit une instance unique, soit un lot.
- `entry_id` reste stable indépendamment de sa position dans l’interface.
- Le type explicite évite de rechercher le même identifiant dans plusieurs tables.
- Une référence ne contient ni quantité ni état mutable.

## 9. Définition d’objet

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/domain/item_definition.gd`.**

```gdscript
class_name ItemDefinition
extends Resource

enum Category {
	MATERIAL,
	CONSUMABLE,
	WEAPON,
	ARMOR,
	TOOL,
	QUEST,
	MISCELLANEOUS,
}

@export var item_id: StringName
@export var display_name_key: StringName
@export var description_key: StringName
@export var category: Category = Category.MISCELLANEOUS
@export_range(0, 1000000000, 1) var mass_mg: int = 0
@export_range(1, 1000000, 1) var maximum_stack_size: int = 1
@export_range(0, 100000000, 1) var maximum_durability: int = 0
@export var equipment_slot_ids: Array[StringName] = []
@export var granted_ability_ids: Array[StringName] = []
@export var reputation_enabled := false
@export var tags: Array[StringName] = []

func is_stackable() -> bool:
	return (
		maximum_stack_size > 1
		and maximum_durability == 0
		and equipment_slot_ids.is_empty()
		and granted_ability_ids.is_empty()
		and not reputation_enabled
	)

func validate() -> Error:
	if not StableId.is_valid(item_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(display_name_key):
		return ERR_INVALID_DATA
	if not StableId.is_valid(description_key):
		return ERR_INVALID_DATA
	if category < Category.MATERIAL or category > Category.MISCELLANEOUS:
		return ERR_INVALID_DATA
	if mass_mg < 0 or maximum_stack_size < 1:
		return ERR_INVALID_DATA
	if maximum_durability < 0:
		return ERR_INVALID_DATA
	if maximum_stack_size > 1 and not is_stackable():
		return ERR_INVALID_DATA
	if _validate_unique_ids(equipment_slot_ids) != OK:
		return ERR_INVALID_DATA
	if _validate_unique_ids(granted_ability_ids) != OK:
		return ERR_INVALID_DATA
	if _validate_unique_ids(tags) != OK:
		return ERR_INVALID_DATA
	return OK

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

- `mass_mg` utilise un entier en milligrammes pour éviter les erreurs d’arrondi cumulées.
- Une définition empilable ne peut porter aucune donnée qui exige une identité individuelle.
- `maximum_durability == 0` signifie que la durabilité ne s’applique pas.
- Les emplacements, compétences et tags sont des identifiants stables uniques.
- La définition ne contient ni quantité, ni propriétaire, ni durabilité courante.

## 10. Instance unique

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/domain/item_instance_state.gd`.**

```gdscript
class_name ItemInstanceState
extends RefCounted

var instance_id: StringName
var definition_id: StringName
var container_id: StringName
var owner: ItemOwnerRef
var current_durability: int = 0
var equipped_by_character_id: StringName
var provenance_sequence: int = 0
var revision: int = 0

func validate(definition: ItemDefinition) -> Error:
	if definition == null or definition.validate() != OK:
		return ERR_UNCONFIGURED
	if not StableId.is_valid(instance_id):
		return ERR_INVALID_DATA
	if definition_id != definition.item_id:
		return ERR_INVALID_DATA
	if not StableId.is_valid(container_id):
		return ERR_INVALID_DATA
	if owner == null or owner.validate() != OK:
		return ERR_INVALID_DATA
	if definition.maximum_durability == 0:
		if current_durability != 0:
			return ERR_INVALID_DATA
	elif current_durability < 0 or current_durability > definition.maximum_durability:
		return ERR_INVALID_DATA
	if not equipped_by_character_id.is_empty():
		if not CharacterId.is_valid(equipped_by_character_id):
			return ERR_INVALID_DATA
		if definition.equipment_slot_ids.is_empty():
			return ERR_INVALID_DATA
	if provenance_sequence < 0 or revision < 0:
		return ERR_INVALID_DATA
	return OK

func is_broken(definition: ItemDefinition) -> bool:
	return definition.maximum_durability > 0 and current_durability == 0

func duplicate_detached() -> ItemInstanceState:
	var copy := ItemInstanceState.new()
	copy.instance_id = instance_id
	copy.definition_id = definition_id
	copy.container_id = container_id
	copy.owner = owner.duplicate_detached() if owner != null else null
	copy.current_durability = current_durability
	copy.equipped_by_character_id = equipped_by_character_id
	copy.provenance_sequence = provenance_sequence
	copy.revision = revision
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’instance référence une définition, mais conserve son propre état vivant.
- `container_id` décrit la garde matérielle ; `owner` décrit la propriété métier.
- L’état brisé est dérivé de la durabilité courante.
- Un objet non équipable ne peut porter de personnage équipé.
- `revision` permet de refuser une commande construite depuis un état obsolète.

## 11. Lot empilable

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/domain/item_stack_state.gd`.**

```gdscript
class_name ItemStackState
extends RefCounted

var stack_id: StringName
var definition_id: StringName
var container_id: StringName
var owner: ItemOwnerRef
var lot_id: StringName
var quantity: int = 0
var revision: int = 0

func validate(definition: ItemDefinition) -> Error:
	if definition == null or definition.validate() != OK:
		return ERR_UNCONFIGURED
	if not definition.is_stackable():
		return ERR_INVALID_DATA
	if not StableId.is_valid(stack_id):
		return ERR_INVALID_DATA
	if definition_id != definition.item_id:
		return ERR_INVALID_DATA
	if not StableId.is_valid(container_id) or not StableId.is_valid(lot_id):
		return ERR_INVALID_DATA
	if owner == null or owner.validate() != OK:
		return ERR_INVALID_DATA
	if quantity < 1 or quantity > definition.maximum_stack_size:
		return ERR_INVALID_DATA
	if revision < 0:
		return ERR_INVALID_DATA
	return OK

func can_merge_with(other: ItemStackState) -> bool:
	if other == null:
		return false
	return (
		definition_id == other.definition_id
		and lot_id == other.lot_id
		and owner.kind == other.owner.kind
		and owner.owner_id == other.owner.owner_id
	)

func duplicate_detached() -> ItemStackState:
	var copy := ItemStackState.new()
	copy.stack_id = stack_id
	copy.definition_id = definition_id
	copy.container_id = container_id
	copy.owner = owner.duplicate_detached() if owner != null else null
	copy.lot_id = lot_id
	copy.quantity = quantity
	copy.revision = revision
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Un lot n’existe que pour une définition explicitement fongible.
- `lot_id` conserve une origine commune sans prétendre suivre chaque unité.
- Deux piles ne fusionnent que si définition, lot et propriétaire correspondent.
- La capacité maximale reste celle de la définition.
- Une division crée un nouvel identifiant de pile mais conserve le même `lot_id`.

## 12. Provenance

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/domain/item_provenance_record.gd`.**

```gdscript
class_name ItemProvenanceRecord
extends RefCounted

enum Kind {
	CREATED,
	ACQUIRED,
	TRANSFERRED,
	EQUIPPED,
	UNEQUIPPED,
	DAMAGED,
	REPAIRED,
	RENOWN_CHANGED,
}

var event_id: StringName
var instance_id: StringName
var kind: Kind = Kind.CREATED
var logical_tick: int = 0
var cause_id: StringName
var source_system_id: StringName
var actor_character_id: StringName
var previous_owner: ItemOwnerRef
var next_owner: ItemOwnerRef

func validate() -> Error:
	if not StableId.is_valid(event_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(instance_id):
		return ERR_INVALID_DATA
	if kind < Kind.CREATED or kind > Kind.RENOWN_CHANGED:
		return ERR_INVALID_DATA
	if logical_tick < 0:
		return ERR_INVALID_DATA
	if not StableId.is_valid(cause_id) or not StableId.is_valid(source_system_id):
		return ERR_INVALID_DATA
	if not actor_character_id.is_empty() and not CharacterId.is_valid(actor_character_id):
		return ERR_INVALID_DATA
	if previous_owner != null and previous_owner.validate() != OK:
		return ERR_INVALID_DATA
	if next_owner != null and next_owner.validate() != OK:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La provenance est fondée sur un événement métier corrélé et un tick logique.
- `cause_id` indique pourquoi la mutation existe ; `source_system_id` indique qui l’a autorisée.
- Les propriétaires précédent et suivant sont optionnels selon le type d’événement.
- Le record ne contient ni texte libre non filtré ni référence de scène.
- Le dépôt conserve l’origine et au plus `64` événements significatifs récents par instance.

## 13. Réputation d’un objet

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/domain/item_reputation_state.gd`.**

```gdscript
class_name ItemReputationState
extends RefCounted

const MAX_RENOWN := 10000
const MAX_RECENT_CAUSES := 32

var instance_id: StringName
var renown: int = 0
var significant_event_count: int = 0
var last_event_tick: int = 0
var recent_cause_ids: Array[StringName] = []
var revision: int = 0

func validate(definition: ItemDefinition) -> Error:
	if definition == null or definition.validate() != OK:
		return ERR_UNCONFIGURED
	if not definition.reputation_enabled:
		return ERR_UNAVAILABLE
	if not StableId.is_valid(instance_id):
		return ERR_INVALID_DATA
	if renown < 0 or renown > MAX_RENOWN:
		return ERR_INVALID_DATA
	if significant_event_count < 0 or last_event_tick < 0 or revision < 0:
		return ERR_INVALID_DATA
	if recent_cause_ids.size() > MAX_RECENT_CAUSES:
		return ERR_INVALID_DATA
	for cause_id: StringName in recent_cause_ids:
		if not StableId.is_valid(cause_id):
			return ERR_INVALID_DATA
	return OK

func apply_delta(cause_id: StringName, delta: int, logical_tick: int) -> Error:
	if not StableId.is_valid(cause_id) or delta == 0 or logical_tick < last_event_tick:
		return ERR_INVALID_PARAMETER
	renown = clampi(renown + delta, 0, MAX_RENOWN)
	significant_event_count += 1
	last_event_tick = logical_tick
	recent_cause_ids.append(cause_id)
	while recent_cause_ids.size() > MAX_RECENT_CAUSES:
		recent_cause_ids.pop_front()
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La réputation est bornée et globale à l’instance.
- `significant_event_count` conserve le nombre total même lorsque la liste récente est élaguée.
- Un événement plus ancien que le dernier événement appliqué est refusé.
- La connaissance de cette réputation par un observateur n’est pas stockée ici.
- La politique applicative décide quels événements peuvent produire un delta.

## 14. Conteneur d’inventaire

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/domain/inventory_container_state.gd`.**

```gdscript
class_name InventoryContainerState
extends RefCounted

var container_id: StringName
var custodian: ItemOwnerRef
var maximum_entries: int = 0
var maximum_mass_mg: int = 0
var entries: Array[InventoryEntryRef] = []
var revision: int = 0

func validate() -> Error:
	if not StableId.is_valid(container_id):
		return ERR_INVALID_DATA
	if custodian == null or custodian.validate() != OK:
		return ERR_INVALID_DATA
	if maximum_entries < 0 or maximum_mass_mg < 0 or revision < 0:
		return ERR_INVALID_DATA
	if maximum_entries > 0 and entries.size() > maximum_entries:
		return ERR_OUT_OF_MEMORY
	var seen: Dictionary[StringName, bool] = {}
	for entry: InventoryEntryRef in entries:
		if entry == null or entry.validate() != OK:
			return ERR_INVALID_DATA
		if seen.has(entry.entry_id):
			return ERR_ALREADY_EXISTS
		seen[entry.entry_id] = true
	return OK

func contains(entry_id: StringName) -> bool:
	for entry: InventoryEntryRef in entries:
		if entry.entry_id == entry_id:
			return true
	return false

func duplicate_detached() -> InventoryContainerState:
	var copy := InventoryContainerState.new()
	copy.container_id = container_id
	copy.custodian = custodian.duplicate_detached()
	copy.maximum_entries = maximum_entries
	copy.maximum_mass_mg = maximum_mass_mg
	copy.revision = revision
	for entry: InventoryEntryRef in entries:
		copy.entries.append(entry.duplicate_detached())
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- `maximum_entries == 0` ou `maximum_mass_mg == 0` signifie que la borne correspondante est désactivée.
- Le conteneur refuse les références invalides et les doublons.
- La masse courante reste dérivée depuis le catalogue et les états d’entrées.
- L’ordre de l’interface n’est pas une identité ; un tri de présentation peut être recalculé.
- La copie profonde protège le dépôt pendant une préparation.

## 15. Calculer la masse sans la persister

> **[LECTURE] Fonction de requête — À placer dans le service de lecture d’inventaire.**

```gdscript
func calculate_mass_mg(container: InventoryContainerState) -> Variant:
	if container == null or container.validate() != OK:
		return null
	var total: int = 0
	for entry: InventoryEntryRef in container.entries:
		var definition := _definition_for_entry(entry)
		if definition == null:
			return null
		var quantity := _quantity_for_entry(entry)
		if quantity < 1:
			return null
		if definition.mass_mg > 0 and quantity > 9007199254740991 / definition.mass_mg:
			return null
		total += definition.mass_mg * quantity
		if total > 9007199254740991:
			return null
	return total
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La fonction renvoie `Variant` afin de distinguer une masse valide de `null`.
- Chaque quantité est relue depuis l’état autoritaire.
- Les contrôles évitent un dépassement et conservent la plage entière JSON sûre.
- La masse totale n’est pas persistée : elle est recalculée depuis les données sources.
- Une définition ou une entrée absente invalide la requête au lieu de produire une estimation silencieuse.

## 16. Équipement

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/domain/equipment_loadout_state.gd`.**

```gdscript
class_name EquipmentLoadoutState
extends RefCounted

var character_id: StringName
var slots: Dictionary[StringName, StringName] = {}
var revision: int = 0

func validate(
	instances: Dictionary[StringName, ItemInstanceState],
	catalog: ItemCatalog,
) -> Error:
	if not CharacterId.is_valid(character_id) or revision < 0:
		return ERR_INVALID_DATA
	var used_instances: Dictionary[StringName, bool] = {}
	for slot_id: StringName in slots:
		var instance_id: StringName = slots[slot_id]
		if not StableId.is_valid(slot_id) or not StableId.is_valid(instance_id):
			return ERR_INVALID_DATA
		if used_instances.has(instance_id):
			return ERR_ALREADY_EXISTS
		var instance := instances.get(instance_id) as ItemInstanceState
		if instance == null:
			return ERR_DOES_NOT_EXIST
		var definition := catalog.get_definition(instance.definition_id)
		if definition == null or slot_id not in definition.equipment_slot_ids:
			return ERR_INVALID_DATA
		if instance.is_broken(definition):
			return ERR_UNAVAILABLE
		if instance.equipped_by_character_id != character_id:
			return ERR_INVALID_DATA
		used_instances[instance_id] = true
	return OK

func duplicate_detached() -> EquipmentLoadoutState:
	var copy := EquipmentLoadoutState.new()
	copy.character_id = character_id
	copy.slots = slots.duplicate(true)
	copy.revision = revision
	return copy
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Un emplacement et une instance ne peuvent apparaître qu’une fois.
- La définition déclare les emplacements compatibles.
- Un objet brisé est refusé par la politique pédagogique retenue.
- L’état d’instance et le loadout doivent se confirmer mutuellement.
- Les bonus de combat ou de personnage restent des vues dérivées consommées par leurs propriétaires.

## 17. Catalogue et dépôt

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/application/item_catalog.gd`.**

```gdscript
class_name ItemCatalog
extends RefCounted

var _definitions: Dictionary[StringName, ItemDefinition] = {}

func register(definition: ItemDefinition) -> Error:
	if definition == null or definition.validate() != OK:
		return ERR_INVALID_DATA
	if _definitions.has(definition.item_id):
		return ERR_ALREADY_EXISTS
	_definitions[definition.item_id] = definition.duplicate(true) as ItemDefinition
	return OK

func get_definition(item_id: StringName) -> ItemDefinition:
	var stored := _definitions.get(item_id) as ItemDefinition
	return null if stored == null else stored.duplicate(true) as ItemDefinition

func all_ids_sorted() -> Array[StringName]:
	var ids: Array[StringName] = []
	ids.assign(_definitions.keys())
	ids.sort()
	return ids
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le catalogue valide une définition avant enregistrement.
- Il conserve et renvoie des copies profondes.
- Les identifiants triés donnent un ordre déterministe.
- Le catalogue ne contient aucune instance, quantité ou propriété.

> **[LECTURE] Contrat du dépôt — Structure de référence.**

```gdscript
class_name InventoryRepository
extends RefCounted

func get_container(_container_id: StringName) -> InventoryContainerState:
	return null

func get_instance(_instance_id: StringName) -> ItemInstanceState:
	return null

func get_stack(_stack_id: StringName) -> ItemStackState:
	return null

func get_loadout(_character_id: StringName) -> EquipmentLoadoutState:
	return null

func get_reputation(_instance_id: StringName) -> ItemReputationState:
	return null

func revision_for_container(_container_id: StringName) -> int:
	return -1

func replace_prepared(_candidate: InventoryMutationCandidate) -> Error:
	return ERR_UNAVAILABLE

func replace_all(_prepared: Dictionary) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les méthodes de lecture doivent renvoyer des copies détachées.
- Les révisions sont relues au moment de préparer et de committer.
- Le dépôt ne décide ni prix, ni dégâts, ni compétences.
- `replace_prepared()` applique un candidat déjà validé.
- `replace_all()` est réservé à une restauration complète préparée.

## 18. Commande de transfert

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/domain/inventory_transfer_command.gd`.**

```gdscript
class_name InventoryTransferCommand
extends RefCounted

var command_id: StringName
var entry: InventoryEntryRef
var quantity: int = 1
var source_container_id: StringName
var destination_container_id: StringName
var requested_owner: ItemOwnerRef
var cause_id: StringName
var source_system_id: StringName
var actor_character_id: StringName
var logical_tick: int = 0
var expected_source_revision: int = 0
var expected_destination_revision: int = 0
var expected_entry_revision: int = 0

func validate() -> Error:
	if not StableId.is_valid(command_id):
		return ERR_INVALID_DATA
	if entry == null or entry.validate() != OK:
		return ERR_INVALID_DATA
	if quantity < 1:
		return ERR_INVALID_DATA
	if not StableId.is_valid(source_container_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(destination_container_id):
		return ERR_INVALID_DATA
	if source_container_id == destination_container_id:
		return ERR_INVALID_PARAMETER
	if requested_owner == null or requested_owner.validate() != OK:
		return ERR_INVALID_DATA
	if not StableId.is_valid(cause_id) or not StableId.is_valid(source_system_id):
		return ERR_INVALID_DATA
	if not actor_character_id.is_empty() and not CharacterId.is_valid(actor_character_id):
		return ERR_INVALID_DATA
	if logical_tick < 0:
		return ERR_INVALID_DATA
	if expected_source_revision < 0:
		return ERR_INVALID_DATA
	if expected_destination_revision < 0 or expected_entry_revision < 0:
		return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La commande identifie explicitement source, destination, entrée et quantité.
- Trois révisions protègent les deux conteneurs et l’entrée.
- `requested_owner` permet un don ou un transfert autorisé sans définir le paiement.
- La cause et le système source alimentent la provenance.
- Le transfert au sein du même conteneur relève d’une commande de réorganisation de présentation, pas de cette mutation métier.

## 19. Résultat métier

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/domain/inventory_result.gd`.**

```gdscript
class_name InventoryResult
extends RefCounted

enum Status {
	COMMITTED,
	REJECTED_INVALID_COMMAND,
	REJECTED_NOT_FOUND,
	REJECTED_STALE_REVISION,
	REJECTED_CAPACITY,
	REJECTED_STACK_RULE,
	REJECTED_OWNERSHIP,
	REJECTED_EQUIPMENT,
	REJECTED_EXTERNAL_AUTHORITY,
	REJECTED_INTERNAL,
}

var status: Status = Status.REJECTED_INTERNAL
var command_id: StringName
var affected_entry_ids: Array[StringName] = []
var message: String = ""

func is_success() -> bool:
	return status == Status.COMMITTED

func validate() -> Error:
	if status < Status.COMMITTED or status > Status.REJECTED_INTERNAL:
		return ERR_INVALID_DATA
	if not command_id.is_empty() and not StableId.is_valid(command_id):
		return ERR_INVALID_DATA
	for entry_id: StringName in affected_entry_ids:
		if not StableId.is_valid(entry_id):
			return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les refus normaux sont distingués d’une panne interne.
- `affected_entry_ids` contient uniquement les identifiants committés.
- `is_success()` n’accepte qu’un commit réel.
- Le résultat ne conserve ni commande mutable ni snapshot complet.

## 20. Candidat de mutation

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/application/inventory_mutation_candidate.gd`.**

```gdscript
class_name InventoryMutationCandidate
extends RefCounted

var command_id: StringName
var containers: Dictionary[StringName, InventoryContainerState] = {}
var instances: Dictionary[StringName, ItemInstanceState] = {}
var stacks: Dictionary[StringName, ItemStackState] = {}
var loadouts: Dictionary[StringName, EquipmentLoadoutState] = {}
var reputations: Dictionary[StringName, ItemReputationState] = {}
var provenance_records: Array[ItemProvenanceRecord] = []
var expected_revisions: Dictionary[StringName, int] = {}

func validate(catalog: ItemCatalog) -> Error:
	if not StableId.is_valid(command_id) or catalog == null:
		return ERR_INVALID_DATA
	for container: InventoryContainerState in containers.values():
		if container == null or container.validate() != OK:
			return ERR_INVALID_DATA
	for instance: ItemInstanceState in instances.values():
		var definition := catalog.get_definition(instance.definition_id)
		if instance == null or instance.validate(definition) != OK:
			return ERR_INVALID_DATA
	for stack: ItemStackState in stacks.values():
		var definition := catalog.get_definition(stack.definition_id)
		if stack == null or stack.validate(definition) != OK:
			return ERR_INVALID_DATA
	for record: ItemProvenanceRecord in provenance_records:
		if record == null or record.validate() != OK:
			return ERR_INVALID_DATA
	for aggregate_id: StringName in expected_revisions:
		if not StableId.is_valid(aggregate_id) or expected_revisions[aggregate_id] < 0:
			return ERR_INVALID_DATA
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le candidat regroupe tous les agrégats que la commande veut remplacer.
- Les collections contiennent des copies détachées.
- Chaque instance ou pile est revalidée contre sa définition.
- Les révisions attendues sont associées à des identifiants d’agrégats.
- Un candidat invalide ne peut atteindre l’unité de travail.

## 21. Préparer un transfert

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/application/inventory_service.gd`.**

```gdscript
class_name InventoryService
extends RefCounted

signal inventory_committed(result: InventoryResult)

var _catalog: ItemCatalog
var _repository: InventoryRepository
var _unit_of_work: InventoryMutationUnitOfWork

func transfer(command: InventoryTransferCommand) -> InventoryResult:
	if command == null or command.validate() != OK:
		return _result(
			InventoryResult.Status.REJECTED_INVALID_COMMAND,
			command,
			"commande invalide",
		)
	if _catalog == null or _repository == null or _unit_of_work == null:
		return _result(
			InventoryResult.Status.REJECTED_INTERNAL,
			command,
			"services obligatoires indisponibles",
		)
	var candidate := _prepare_transfer(command)
	if candidate == null:
		return _result(
			InventoryResult.Status.REJECTED_NOT_FOUND,
			command,
			"entrée ou conteneur absent",
		)
	if candidate.validate(_catalog) != OK:
		return _result(
			InventoryResult.Status.REJECTED_INTERNAL,
			command,
			"candidat invalide",
		)
	var commit_code := _unit_of_work.commit(candidate)
	if commit_code != OK:
		var status := InventoryResult.Status.REJECTED_INTERNAL
		if commit_code == ERR_BUSY:
			status = InventoryResult.Status.REJECTED_STALE_REVISION
		elif commit_code == ERR_OUT_OF_MEMORY:
			status = InventoryResult.Status.REJECTED_CAPACITY
		return _result(status, command, error_string(commit_code))
	var result := _result(
		InventoryResult.Status.COMMITTED,
		command,
		"transfert committé",
	)
	result.affected_entry_ids.assign(_affected_ids(candidate))
	inventory_committed.emit(result)
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Les validations générales précèdent toute lecture détaillée.
- `_prepare_transfer()` construit des copies de source, destination et entrée.
- Le candidat est validé avant le commit.
- `ERR_BUSY` représente une révision devenue obsolète.
- Le signal est émis seulement après le remplacement réussi.

> **[LECTURE] Préparation interne d’une instance — Suite de `inventory_service.gd`.**

```gdscript
func _prepare_instance_transfer(
	command: InventoryTransferCommand,
	source: InventoryContainerState,
	destination: InventoryContainerState,
) -> InventoryMutationCandidate:
	if command.quantity != 1:
		return null
	var instance := _repository.get_instance(command.entry.entry_id)
	if instance == null or instance.container_id != source.container_id:
		return null
	if instance.revision != command.expected_entry_revision:
		return null
	if not source.contains(instance.instance_id):
		return null

	var source_candidate := source.duplicate_detached()
	var destination_candidate := destination.duplicate_detached()
	if not _remove_entry(source_candidate, instance.instance_id):
		return null
	if not _append_instance(destination_candidate, instance):
		return null

	var instance_candidate := instance.duplicate_detached()
	var previous_owner := instance_candidate.owner.duplicate_detached()
	instance_candidate.container_id = destination.container_id
	instance_candidate.owner = command.requested_owner.duplicate_detached()
	instance_candidate.revision += 1
	instance_candidate.provenance_sequence += 1

	var candidate := InventoryMutationCandidate.new()
	candidate.command_id = command.command_id
	candidate.containers[source.container_id] = source_candidate
	candidate.containers[destination.container_id] = destination_candidate
	candidate.instances[instance.instance_id] = instance_candidate
	candidate.expected_revisions[source.container_id] = command.expected_source_revision
	candidate.expected_revisions[destination.container_id] = command.expected_destination_revision
	candidate.expected_revisions[instance.instance_id] = command.expected_entry_revision
	candidate.provenance_records.append(
		_build_transfer_record(command, instance_candidate, previous_owner)
	)
	return candidate
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Une instance se transfère toujours avec une quantité égale à `1`.
- La source est vérifiée à la fois dans l’instance et dans le conteneur.
- La destination est validée avant de modifier l’instance candidate.
- Propriété, garde, révision et séquence de provenance changent dans le même candidat.
- Aucun état actif n’est modifié par cette fonction.

## 22. Diviser et fusionner un lot

> **[LECTURE] Règles de quantité — Fonctions internes du service.**

```gdscript
func _split_stack(
	stack: ItemStackState,
	quantity: int,
	new_stack_id: StringName,
) -> ItemStackState:
	if stack == null or quantity < 1 or quantity >= stack.quantity:
		return null
	if not StableId.is_valid(new_stack_id):
		return null
	var created := stack.duplicate_detached()
	created.stack_id = new_stack_id
	created.quantity = quantity
	created.revision = 0
	return created

func _merge_quantity(
	destination: ItemStackState,
	source: ItemStackState,
	definition: ItemDefinition,
	quantity: int,
) -> Error:
	if destination == null or source == null or definition == null:
		return ERR_INVALID_PARAMETER
	if not destination.can_merge_with(source):
		return ERR_INVALID_DATA
	if quantity < 1 or quantity > source.quantity:
		return ERR_INVALID_PARAMETER
	if destination.quantity + quantity > definition.maximum_stack_size:
		return ERR_OUT_OF_MEMORY
	destination.quantity += quantity
	source.quantity -= quantity
	destination.revision += 1
	source.revision += 1
	return OK
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Une division partielle crée une nouvelle pile avec le même `lot_id`.
- La pile source réelle n’est modifiée que sur une copie préparée par l’appelant.
- La fusion exige une compatibilité stricte et une capacité suffisante.
- Une quantité source ramenée à zéro entraîne la suppression préparée de sa référence et de son état.
- Les prix ou valeurs monétaires ne participent jamais à la règle de pile.

## 23. Unité de travail

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/application/inventory_mutation_unit_of_work.gd`.**

```gdscript
class_name InventoryMutationUnitOfWork
extends RefCounted

class ExternalCandidate:
	extends RefCounted

	var authority_id: StringName
	var payload: Dictionary = {}

	func validate() -> Error:
		if not StableId.is_valid(authority_id):
			return ERR_INVALID_DATA
		return OK if not payload.is_empty() else ERR_INVALID_DATA

func commit(
	inventory_candidate: InventoryMutationCandidate,
	external_candidates: Array[ExternalCandidate] = [],
) -> Error:
	return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le contrat reçoit le candidat d’inventaire et les candidats des autorités externes.
- L’implémentation réelle doit revalider toutes les révisions et tous les candidats avant le premier remplacement.
- `authority_id` identifie le propriétaire de chaque payload.
- Une capacité transactionnelle réelle doit être matérialisée et testée ; le stub ne revendique aucune atomicité exécutée.
- Les événements restent hors du commit et sont émis après réussite.

## 24. Équiper et accorder une compétence

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/application/inventory_ability_grant_port.gd`.**

```gdscript
class_name InventoryAbilityGrantPort
extends RefCounted

func prepare_grant_set(
	character_id: StringName,
	source_instance_id: StringName,
	ability_ids: Array[StringName],
	enabled: bool,
	expected_ability_revision: int,
) -> InventoryMutationUnitOfWork.ExternalCandidate:
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le port appartient à la frontière du système de compétences.
- L’inventaire indique une source, une liste d’identifiants et l’activation demandée.
- Le système de compétences valide les définitions et construit son candidat.
- L’inventaire ne modifie ni progression, ni charges, ni recharge.
- Le grant temporaire est recalculable depuis l’équipement restauré.

> **[LECTURE] Préparation d’un équipement — Structure de référence.**

```gdscript
func prepare_equip(
	character_id: StringName,
	slot_id: StringName,
	instance_id: StringName,
	expected_inventory_revision: int,
	expected_ability_revision: int,
) -> Dictionary:
	var instance := _repository.get_instance(instance_id)
	if instance == null:
		return {}
	var definition := _catalog.get_definition(instance.definition_id)
	if definition == null or slot_id not in definition.equipment_slot_ids:
		return {}
	if instance.is_broken(definition):
		return {}
	var loadout := _repository.get_loadout(character_id)
	if loadout == null or loadout.revision != expected_inventory_revision:
		return {}

	var instance_candidate := instance.duplicate_detached()
	var loadout_candidate := loadout.duplicate_detached()
	instance_candidate.equipped_by_character_id = character_id
	instance_candidate.revision += 1
	loadout_candidate.slots[slot_id] = instance_id
	loadout_candidate.revision += 1

	var grant_candidate := _ability_grant_port.prepare_grant_set(
		character_id,
		instance_id,
		definition.granted_ability_ids,
		true,
		expected_ability_revision,
	)
	if not definition.granted_ability_ids.is_empty() and grant_candidate == null:
		return {}
	return {
		"instance": instance_candidate,
		"loadout": loadout_candidate,
		"grant": grant_candidate,
	}
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’instance, la définition et le loadout sont relus avant préparation.
- Un objet brisé ou incompatible est refusé.
- L’état d’équipement est modifié sur des copies.
- Une compétence accordée produit un candidat appartenant au système de compétences.
- Le commit final doit réunir le candidat d’inventaire et le candidat externe.

## 25. Durabilité demandée par le combat

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/application/inventory_durability_port.gd`.**

```gdscript
class_name InventoryDurabilityPort
extends RefCounted

func prepare_loss(
	instance_id: StringName,
	amount: int,
	cause_id: StringName,
	logical_tick: int,
	expected_instance_revision: int,
) -> InventoryMutationCandidate:
	return null

func prepare_repair(
	instance_id: StringName,
	amount: int,
	cause_id: StringName,
	logical_tick: int,
	expected_instance_revision: int,
) -> InventoryMutationCandidate:
	return null
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le combat peut demander une perte après avoir résolu son action autoritaire.
- L’inventaire borne la durabilité entre zéro et le maximum de la définition.
- Une réparation suit la même autorité et exige une cause validée.
- Les méthodes renvoient un candidat, jamais une mutation déjà appliquée.
- Le système qui orchestre le commit décide si la perte appartient au même lot que l’action source.

## 26. Politique de réputation

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/application/item_reputation_policy.gd`.**

```gdscript
class_name ItemReputationPolicy
extends RefCounted

const ALLOWED_CAUSES: Dictionary[StringName, int] = {
	&"item.reputation.defeated_major_threat": 250,
	&"item.reputation.saved_settlement": 400,
	&"item.reputation.carried_by_renowned_owner": 100,
	&"item.reputation.public_failure": -75,
	&"item.reputation.forged_legend": 800,
}

func delta_for(cause_id: StringName) -> Variant:
	if not ALLOWED_CAUSES.has(cause_id):
		return null
	return ALLOWED_CAUSES[cause_id]

func prepare_change(
	state: ItemReputationState,
	definition: ItemDefinition,
	cause_id: StringName,
	logical_tick: int,
) -> ItemReputationState:
	if state == null or state.validate(definition) != OK:
		return null
	var delta_value: Variant = delta_for(cause_id)
	if delta_value == null:
		return null
	var candidate := state.duplicate(true) as ItemReputationState
	if candidate.apply_delta(cause_id, int(delta_value), logical_tick) != OK:
		return null
	candidate.revision += 1
	return candidate
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- La liste autorisée ferme les causes et leurs deltas.
- `Variant` distingue un delta absent d’un delta numérique.
- La politique travaille sur une copie candidate.
- Un texte, un score IA ou un nom célèbre ne modifie pas directement la réputation.
- Les valeurs sont pédagogiques et devront être équilibrées par des données versionnées si elles deviennent du contenu de production.

## 27. Adapter une action d’agent

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/application/inventory_agent_action_executor.gd`.**

```gdscript
class_name InventoryAgentActionExecutor
extends AgentActionExecutor

const EXECUTOR_KEY := &"agent.executor.inventory_transfer"

var _inventory_service: InventoryService
var _context_port: InventoryAgentContextPort

func can_execute(request: AgentActionRequest) -> Error:
	if request == null or request.validate() != OK:
		return ERR_INVALID_DATA
	if request.executor_key != EXECUTOR_KEY:
		return ERR_UNAVAILABLE
	if _inventory_service == null or _context_port == null:
		return ERR_UNCONFIGURED
	return OK

func start(request: AgentActionRequest) -> Error:
	var check := can_execute(request)
	if check != OK:
		return check
	var context := _context_port.snapshot_for(request.owner_character_id)
	if context == null or context.validate() != OK:
		return ERR_DOES_NOT_EXIST
	var command := context.build_transfer_command(request)
	if command == null:
		return ERR_INVALID_DATA
	var result := _inventory_service.transfer(command)
	return OK if result.is_success() else ERR_CANT_RESOLVE
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- L’agent choisit une intention depuis un snapshot, pas un remplacement de dépôt.
- Le contexte fournit les conteneurs, l’entrée et les révisions autorisées.
- Le même service traite ensuite joueur et agent.
- Un refus provoque une nouvelle décision sur un snapshot frais.
- L’agent ne choisit ni prix, ni dégâts, ni delta de réputation.

## 28. Présentation et interaction du joueur

L’interface peut afficher :

- icône et nom localisé ;
- quantité ;
- masse et capacité ;
- durabilité courante ;
- propriétaire et gardien autorisés ;
- emplacement d’équipement ;
- compétences accordées ;
- niveau de renommée ;
- provenance significative accessible au joueur.

Elle ne doit pas :

- déplacer directement une entrée dans les collections internes ;
- fusionner deux piles sans revalidation ;
- déduire la propriété depuis la scène ;
- appliquer un bonus ou une compétence ;
- considérer un glisser-déposer comme un commit.

> **[LECTURE] Séparation interface / autorité — Ne pas saisir.**

```text
interface :
- affiche un snapshot détaché ;
- propose source, destination et quantité ;
- construit une commande typée ;
- attend InventoryResult.

service :
- relit définitions, états et révisions ;
- prépare source, destination, propriété et provenance ;
- demande les candidats externes ;
- commit le lot ;
- émet le résultat.
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le glisser-déposer reste une intention de présentation.
- Une destination peut devenir pleine avant le commit.
- La même commande peut être soumise par une interface, un agent ou un scénario.
- Les règles métier ne sont pas dupliquées dans les widgets.

## 29. Persistance

Sont persistés :

- conteneurs, capacités et révisions ;
- références d’entrées ;
- instances, définitions référencées, garde et propriété ;
- durabilité courante ;
- équipement et révisions de loadout ;
- lots, quantités et `lot_id` ;
- origine et événements de provenance retenus ;
- réputation, compteurs, causes récentes et révisions.

Ne sont pas persistés :

- définitions `.tres` ;
- masse totale dérivée ;
- clés de tri, filtres et sélection de l’interface ;
- candidats et commandes en attente ;
- références de nœuds ;
- icônes, meshes, animations et VFX ;
- caches de catalogue ;
- compétences accordées dérivées de l’équipement ;
- prix, offres ou paniers économiques ;
- cibles et résultats de combat.

## 30. Codec strict

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/infrastructure/inventory_snapshot_codec.gd`.**

```gdscript
class_name InventorySnapshotCodec
extends RefCounted

const FORMAT := "project-asteria-inventory"
const VERSION := 1
const ROOT_KEYS := [
	"format",
	"version",
	"containers",
	"instances",
	"stacks",
	"loadouts",
	"provenance",
	"reputations",
]

class DecodeResult:
	extends RefCounted

	var code: Error = FAILED
	var prepared: Dictionary = {}
	var message: String = ""

	func is_success() -> bool:
		return code == OK

func decode(document: Dictionary, catalog: ItemCatalog) -> DecodeResult:
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

	var prepared := _decode_all_sections(document, catalog)
	if prepared == null:
		return _failure(ERR_INVALID_DATA, "inventaire invalide")
	if _validate_cross_references(prepared, catalog) != OK:
		return _failure(ERR_INVALID_DATA, "références croisées invalides")
	var result := DecodeResult.new()
	result.code = OK
	result.prepared = prepared
	return result
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le format, la version et les clés exactes sont obligatoires.
- Les sections sont décodées avant la validation croisée.
- La validation croisée vérifie notamment que chaque entrée appartient à un seul conteneur et que chaque loadout vise une instance existante.
- Les définitions absentes rendent la restauration invalide.
- Aucun dépôt actif n’est modifié pendant le décodage.

## 31. Section de sauvegarde

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/infrastructure/inventory_save_section.gd`.**

```gdscript
class_name InventorySaveSection
extends SaveSection

var _repository: InventoryRepository
var _catalog: ItemCatalog
var _codec := InventorySnapshotCodec.new()
var _prepared: Dictionary = {}
var _is_prepared := false

func section_id() -> StringName:
	return &"inventory"

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
- Les données sont copiées avant stockage et avant application.
- La préparation reste disponible après un échec d’application.
- Le coordinateur peut annuler si une autre section de sauvegarde échoue.
- Les compétences accordées sont recalculées après restauration de l’équipement par le bootstrap applicatif.

## 32. Présentation et scène pédagogique

> **[VSC] Visual Studio Code — Créer : `res://src/features/inventory/presentation/inventory_presentation_bridge.gd`.**

```gdscript
class_name InventoryPresentationBridge
extends Node

var _actor_registry: ActiveCharacterRegistry

func on_inventory_committed(result: InventoryResult) -> void:
	if result == null or result.validate() != OK:
		return
	if not result.is_success():
		return
	for entry_id: StringName in result.affected_entry_ids:
		request_inventory_refresh(entry_id)

func request_inventory_refresh(_entry_id: StringName) -> void:
	pass
```

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- Le pont reçoit seulement un résultat committé.
- Il demande un rafraîchissement par identifiant stable.
- Il ne déplace aucune entrée et ne recalcule aucune règle.
- Un objet hors scène reste valide sans représentation visuelle.

La scène `ch20_inventory_demo.tscn` doit montrer :

1. une instance unique transférée entre deux conteneurs ;
2. une destination pleine refusant le transfert sans perte côté source ;
3. une pile divisée puis fusionnée avec le même lot ;
4. deux lots incompatibles refusant la fusion ;
5. un objet équipé accordant temporairement une compétence ;
6. un objet brisé refusé à l’équipement ;
7. une perte et une réparation de durabilité préparées ;
8. une provenance enrichie par un transfert ;
9. une réputation modifiée par une cause autorisée ;
10. une sauvegarde restaurant conteneurs, équipement et réputation.

## 33. Modes Solo et Studio

### 33.1 Mode Solo

- catalogue local de `.tres` ;
- dépôt en mémoire ;
- un conteneur principal par personnage ;
- équipement simple ;
- provenance limitée à l’origine et aux événements significatifs ;
- réputation globale déterministe ;
- diagnostics lisibles ;
- aucune classe chargée depuis les données.

### 33.2 Mode Studio

- catalogues et schémas versionnés ;
- import de données contrôlé ;
- tests de propriété sur divisions et fusions ;
- revue des capacités et masses ;
- migrations explicites ;
- télémétrie agrégée des refus ;
- validation éditoriale des causes de réputation ;
- transaction partagée avec l’économie lorsque celle-ci sera matérialisée ;
- séparation entre équilibrage, domaine et présentation.

Le Mode Studio renforce les contrôles. Il n’ajoute ni Service Locator ni Autoload universel.

## 34. Budgets, sécurité et diagnostics

Bornes pédagogiques :

| Élément | Borne |
|---|---:|
| conteneurs par propriétaire | 64 |
| entrées par conteneur | 512 |
| quantité maximale par pile | 1 000 000 |
| événements de provenance récents par instance | 64 |
| causes de réputation récentes | 32 |
| emplacements d’équipement par personnage | 64 |
| compétences accordées par objet | 16 |

Ces valeurs devront être mesurées lors des campagnes exécutées.

Une définition ou un import externe doit :

- être limité avant parsing ;
- utiliser un schéma versionné ;
- référencer uniquement des catégories et emplacements autorisés ;
- refuser chemins, scripts et méthodes dynamiques ;
- borner masse, durabilité, quantité, historique et renommée ;
- être validé avant le catalogue.

Journaliser :

- identifiant de commande ;
- entrée, source, destination et quantité ;
- révisions attendues et observées ;
- cause et système source ;
- code de commit ;
- identifiants de candidats externes ;
- changements de durabilité ou de réputation.

Ne pas journaliser snapshots complets, inventaires privés non nécessaires, secrets, textes génératifs bruts ou références de nœuds.

## 35. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 35.1 Modifier la définition partagée

**Symptôme ou risque :** plusieurs objets changent simultanément de durabilité ou de propriétaire.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
item_definition.current_durability -= 1
item_definition.owner_id = character_id
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une `Resource` partagée devient l’état vivant de toutes ses instances.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var instance_candidate := instance.duplicate_detached()
instance_candidate.current_durability -= 1
instance_candidate.owner = new_owner.duplicate_detached()
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** seule la copie de l’instance concernée porte la mutation préparée.

### 35.2 Utiliser le nom affiché comme identité

**Symptôme ou risque :** traduction, renommage ou doublon de libellé casse les sauvegardes.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
inventory["Lame des étoiles"] = sword
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le texte localisé n’est ni unique ni stable.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
instances[&"item.instance.7c42a9"] = sword_state
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’instance conserve une identité métier indépendante de l’affichage.

### 35.3 Empiler des objets individualisés

**Symptôme ou risque :** durabilité, provenance, équipement ou réputation disparaît pendant la fusion.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if first.definition_id == second.definition_id:
	first.quantity += second.quantity
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** l’identité de définition ne prouve pas la fongibilité des états.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if definition.is_stackable() and first.can_merge_with(second):
	return _merge_quantity(first, second, definition, quantity)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la définition et le lot imposent une compatibilité stricte avant fusion.

### 35.4 Stocker l’inventaire dans le personnage actif

**Symptôme ou risque :** la disparition de la scène supprime ou désynchronise les objets logiques.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
character_node.inventory.append(item_node)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** des nœuds de scène deviennent la source de vérité persistante.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var result := inventory_service.transfer(command)
if result.is_success():
	refresh_inventory_view()
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le dépôt logique survit à la disparition des représentations actives.

### 35.5 Retirer la source avant de valider la destination

**Symptôme ou risque :** un objet disparaît lorsque la destination est pleine ou invalide.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
source.entries.erase(entry)
if destination.entries.size() >= destination.maximum_entries:
	return ERR_OUT_OF_MEMORY
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la mutation active précède la dernière précondition.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var candidate := prepare_transfer(source, destination, entry)
if candidate == null:
	return ERR_OUT_OF_MEMORY
return unit_of_work.commit(candidate)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** source et destination sont validées sur des copies avant le commit commun.

### 35.6 Équiper une pile

**Symptôme ou risque :** un emplacement référence une quantité sans identité ni durabilité propre.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
loadout.slots[slot_id] = ration_stack.stack_id
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** un lot fongible ne possède pas les invariants d’une instance équipable.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var instance := repository.get_instance(instance_id)
var definition := catalog.get_definition(instance.definition_id)
if slot_id in definition.equipment_slot_ids:
	prepare_equip(character_id, slot_id, instance_id, inventory_revision, ability_revision)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’équipement exige une instance unique et une compatibilité déclarée.

### 35.7 Laisser le combat écrire la durabilité

**Symptôme ou risque :** l’état d’objet contourne révisions, provenance et commit partagé.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
weapon.current_durability -= damage_amount
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le combat modifie une autorité appartenant à l’inventaire.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var durability_candidate := inventory_durability_port.prepare_loss(
	weapon_id,
	loss,
	cause_id,
	logical_tick,
	instance_revision,
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’inventaire borne et prépare sa propre mutation pour le commit orchestré.

### 35.8 Débloquer directement une compétence depuis l’objet

**Symptôme ou risque :** l’équipement écrase une progression durable ou une recharge existante.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
ability_progression.unlocked = true
ability_runtime.available_charges = 1
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** l’inventaire écrit dans les états propriétaires du chapitre 19.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var grant_candidate := ability_grant_port.prepare_grant_set(
	character_id,
	item_instance_id,
	definition.granted_ability_ids,
	true,
	ability_revision,
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le système de compétences valide et prépare un grant lié à une source externe.

### 35.9 Persister une valeur dérivée ou une sélection d’interface

**Symptôme ou risque :** la sauvegarde contient des valeurs contradictoires après changement de définition.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
payload["total_mass"] = cached_mass
payload["selected_slot"] = selected_index
payload["sorted_entries"] = ui_entries
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** caches, index visuels et ordre d’interface deviennent des autorités concurrentes.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
payload["entries"] = encode_entry_refs(container.entries)
payload["instances"] = encode_instances(instances)
payload["stacks"] = encode_stacks(stacks)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les valeurs dérivées sont recalculées depuis les états durables.

### 35.10 Laisser une sortie IA créer la réputation

**Symptôme ou risque :** un texte inventé transforme immédiatement un objet en relique célèbre.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
reputation.renown += int(ai_response["legend_score"])
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une sortie non autoritaire choisit directement un état persistant.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var candidate := reputation_policy.prepare_change(
	state,
	definition,
	validated_cause_id,
	logical_tick,
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** seule une cause fermée et validée produit un delta déterministe.

## 36. Tests à préparer

### 36.1 Tests unitaires

- identifiants et références ;
- validation des définitions ;
- fongibilité et `is_stackable()` ;
- masse dérivée et dépassements ;
- division et fusion de lots ;
- durabilité et état brisé ;
- loadout et emplacements ;
- propriété et garde ;
- provenance bornée ;
- politique de réputation ;
- codec strict.

### 36.2 Tests d’intégration

- transfert entre deux conteneurs ;
- destination pleine sans perte côté source ;
- changement simultané de propriété et de garde ;
- équipement avec grant de compétence ;
- déséquipement retirant uniquement le grant source ;
- perte de durabilité préparée depuis le combat ;
- transfert autorisé depuis une transaction économique future ;
- action d’agent ;
- sauvegarde et restauration ;
- recalcul des grants après chargement.

### 36.3 Simulations

- 1, 64 et 512 entrées par conteneur ;
- 1, 16 et 64 conteneurs par propriétaire ;
- divisions et fusions répétées ;
- transferts concurrents sur les mêmes révisions ;
- 10 000 objets uniques hors scène ;
- 64 événements de provenance par objet ;
- équipement de plusieurs personnages partageant une définition ;
- évolution de réputation jusqu’aux deux bornes.

## 37. Réserves runtime

Cette revue statique ne prouve pas :

- le passage de tous les extraits dans le parseur Godot 4.7.1 ;
- le comportement des dictionnaires typés dans toutes les signatures présentées ;
- l’atomicité réelle de `InventoryMutationUnitOfWork` ;
- l’intégration runtime du grant de compétences ;
- l’intégration combat-durabilité ;
- l’instanciation de la scène pédagogique ;
- la tenue des budgets avec de grands inventaires ;
- l’exécution du codec et d’une migration future ;
- le replay entre plateformes ou versions ;
- la génération d’un PDF intermédiaire.

## 38. Sources techniques

- [Godot 4.7 — `Resource`](https://docs.godotengine.org/en/4.7/classes/class_resource.html)
- [Godot 4.7 — `RefCounted`](https://docs.godotengine.org/en/4.7/classes/class_refcounted.html)
- [Godot 4.7 — `Array`](https://docs.godotengine.org/en/4.7/classes/class_array.html)
- [Godot 4.7 — `Dictionary`](https://docs.godotengine.org/en/4.7/classes/class_dictionary.html)
- [Godot 4.7 — `StringName`](https://docs.godotengine.org/en/4.7/classes/class_stringname.html)
- [Godot 4.7 — `Variant`](https://docs.godotengine.org/en/4.7/classes/class_variant.html)
- [Godot 4.7 — signaux](https://docs.godotengine.org/en/4.7/getting_started/step_by_step/signals.html)
- [Chapitre 7 — Données avec Resources, JSON et configurations](CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md)
- [Chapitre 9 — Sauvegardes, chargements et compatibilité](CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md)
- [Chapitre 14 — Personnages](CHAPITRE-14-Personnages.md)
- [Chapitre 17 — Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md)
- [Chapitre 18 — Combat](CHAPITRE-18-Combat.md)
- [Chapitre 19 — Compétences et pouvoirs](CHAPITRE-19-Competences-et-pouvoirs.md)

## 39. Synthèse opérationnelle pour Project Asteria

Le système d’inventaire et de réputation des objets de `Project Asteria` retient les décisions suivantes :

1. `ItemDefinition` est une donnée de conception partagée et immuable ;
2. les instances uniques sont séparées des lots fongibles ;
3. une définition empilable ne possède ni durabilité, ni équipement, ni compétence accordée, ni réputation individuelle ;
4. propriété et garde sont distinctes ;
5. les conteneurs référencent des entrées par identifiants stables ;
6. masse et autres vues dérivées sont recalculées ;
7. source, destination et entrée sont préparées avant tout transfert ;
8. division et fusion conservent le `lot_id` et respectent la capacité maximale ;
9. seul un objet unique compatible peut être équipé ;
10. les compétences accordées restent sous l’autorité du système de compétences ;
11. le combat prépare une demande de durabilité sans écrire l’inventaire ;
12. provenance et réputation utilisent des causes validées et des ticks logiques ;
13. une sortie IA ne modifie jamais directement la réputation ;
14. conteneurs, états, équipement et candidats externes sont committés comme un lot ;
15. définitions, caches, présentation, commandes et valeurs dérivées sont exclus de la persistance.
