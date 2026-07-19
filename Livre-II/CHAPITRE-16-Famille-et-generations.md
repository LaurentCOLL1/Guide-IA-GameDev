---
title: "Livre II — Chapitre 16 : Famille et générations"
id: "DOC-L2-CH16"
status: "reviewed"
version: "1.1.0"
lang: "fr-FR"
book: "Livre II"
chapter: 16
last-verified: "2026-07-20"
audit-status: "complete"
audit-date: "2026-07-20"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-16.md"
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

# Famille et générations

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH16`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Niveau de raisonnement conseillé :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-16.md`.
> **Explications de code :** enrichies bloc par bloc selon la porte QA Q1.1.

## 1. Rôle du chapitre

Le chapitre 14 a défini l’identité stable des personnages. Le chapitre 15 a ajouté des perceptions sociales orientées et mutables.

La famille forme un système différent. Une filiation ne se déduit ni de l’affinité ni de la confiance. Une adoption ne disparaît pas parce que deux personnes se disputent. Une union peut se terminer sans effacer les enfants, la tutelle passée ni l’histoire.

Ce chapitre construit donc un **graphe familial logique et temporel**, indépendant des nœuds actifs.

À la fin, le lecteur saura :

- représenter une filiation dirigée parent vers enfant ;
- distinguer lien biologique, adoption, tutelle et union ;
- refuser auto-liens, doublons, références inconnues et cycles d’ascendance ;
- canoniser une paire pour les unions non orientées ;
- dater le début et la fin d’un lien avec des ticks de simulation ;
- calculer parents, enfants, fratries, ancêtres, descendants et distances générationnelles ;
- conserver les personnages décédés, archivés ou absents des scènes ;
- produire des événements familiaux typés ;
- sérialiser le graphe dans une section de sauvegarde indépendante ;
- préparer la restauration complète avant toute mutation ;
- préserver les frontières avec relations sociales, succession, politique et narration.

## 2. Prérequis

Le chapitre réutilise :

- `CharacterId` du chapitre 14 ;
- l’index logique des personnages utilisé au chapitre 15 ;
- `SaveSection` et le coordinateur de sauvegarde du chapitre 9 ;
- les événements typés du chapitre 5 ;
- les dictionnaires et tableaux typés du chapitre 2 ;
- la règle de séparation domaine, application, infrastructure et présentation du chapitre 4.

Il ne dépend pas :

- des nœuds actuellement présents dans la scène ;
- de `ActiveCharacterRegistry` ;
- des valeurs sociales du chapitre 15 ;
- d’un service IA ;
- d’une base SQLite ouverte au moment de la simulation.

## 3. Périmètre et frontières

Ce chapitre définit :

- un identifiant de lien familial ;
- une filiation orientée ;
- une tutelle orientée et temporelle ;
- une union non orientée et temporelle ;
- un graphe familial validé ;
- des requêtes bornées ;
- un historique d’événements familiaux ;
- un codec strict ;
- une section de sauvegarde indépendante.

Il ne définit pas encore :

- les règles de succession politique du chapitre 23 ;
- les héritages d’objets et d’économie des chapitres 20 et 21 ;
- les comportements d’agents du chapitre 17 ;
- les quêtes familiales et révélations narratives du chapitre 25 ;
- la génétique, la reproduction biologique ou la simulation démographique avancée ;
- le multijoueur du Livre IV.

> **Frontière essentielle :** une relation sociale décrit une perception mutable. Un lien familial décrit une structure déclarée et validée du monde.

## 4. Modèle conceptuel

### 4.1 Trois familles de liens

| Type | Orientation | Temporalité | Exemple |
|---|---|---|---|
| filiation | parent → enfant | permanente dans ce chapitre | biologique ou adoption |
| tutelle | tuteur → protégé | début et fin possibles | protection légale |
| union | paire canonique | début et fin possibles | mariage ou partenariat |

La fratrie n’est pas persistée. Elle est calculée depuis les parents partagés.

La génération n’est pas persistée. Elle est calculée depuis les chemins de filiation.

### 4.2 Pourquoi ne pas utiliser un booléen `is_parent`

Un booléen placé dans le personnage :

- ne nomme pas l’autre personnage ;
- ne permet pas plusieurs parents ;
- ne distingue pas biologique et adoption ;
- ne détecte pas les cycles ;
- ne conserve pas la provenance ;
- ne permet pas une validation globale.

Le graphe est donc une autorité séparée.

### 4.3 Architecture retenue

> **[LECTURE] Architecture familiale — Ne pas saisir.**

```text
CharacterIdentityIndex
        ↓ validation des références
FamilyGraphService
        ↓
FamilyGraph
 ├── ParentChildLink
 ├── GuardianshipLink
 ├── UnionLink
 └── FamilyEventLog
        ↓
FamilySnapshotCodec
        ↓
FamilySaveSection
```

## 5. Identifiants et types de liens

### 5.1 Identifiant stable du lien

> **[VSC] Visual Studio Code — Créer : `src/features/families/domain/family_link_id.gd`.**

```gdscript
class_name FamilyLinkId
extends RefCounted

const PREFIX := "fam_"
const HEX_LENGTH := 32

static func create_random() -> StringName:
	var bytes := Crypto.new().generate_random_bytes(16)
	if bytes.size() != 16:
		push_error("Impossible de générer un identifiant familial.")
		return StringName()
	return StringName(PREFIX + bytes.hex_encode())

static func is_valid(value: StringName) -> bool:
	var text := String(value)
	if not text.begins_with(PREFIX):
		return false
	var suffix := text.substr(PREFIX.length())
	if suffix.length() != HEX_LENGTH:
		return false
	for character in suffix:
		if not character in "0123456789abcdef":
			return false
	return true
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `FamilyLinkId`, dérivée de `RefCounted`.
- **Emplacement :** il appartient à `src/features/families/domain/family_link_id.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** ce bloc ne déclare pas de fonction publique ; ses données sont consommées par le code qui l’instancie ou le décode. Les types visibles dans les déclarations constituent néanmoins le contrat à respecter.
- **État et dépendances :** le bloc déclare constantes `PREFIX := "fam_"`, `HEX_LENGTH := 32` ; état `bytes := Crypto.new().generate_random_bytes(16)`, `text := String(value)`, `suffix := text.substr(PREFIX.length())`. Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les boucles `for` parcourent les collections de façon explicite ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** enregistre une erreur exploitable par l’appelant. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

L’identifiant :

- n’utilise ni nom affiché ni index de tableau ;
- reste stable dans les sauvegardes ;
- ne transporte pas le type de lien ;
- n’est jamais recyclé.

### 5.2 Types explicites

> **[VSC] Visual Studio Code — Créer : `src/features/families/domain/family_link_kind.gd`.**

```gdscript
class_name FamilyLinkKind
extends RefCounted

enum Value {
	BIOLOGICAL_PARENT,
	ADOPTIVE_PARENT,
	GUARDIANSHIP,
	UNION,
}

static func is_parent_kind(value: Value) -> bool:
	return value in [
		Value.BIOLOGICAL_PARENT,
		Value.ADOPTIVE_PARENT,
	]

static func is_known(value: int) -> bool:
	return value in [
		int(Value.BIOLOGICAL_PARENT),
		int(Value.ADOPTIVE_PARENT),
		int(Value.GUARDIANSHIP),
		int(Value.UNION),
	]
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `FamilyLinkKind`, dérivée de `RefCounted`.
- **Emplacement :** il appartient à `src/features/families/domain/family_link_kind.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** ce bloc ne déclare pas de fonction publique ; ses données sont consommées par le code qui l’instancie ou le décode. Les types visibles dans les déclarations constituent néanmoins le contrat à respecter.
- **État et dépendances :** aucune donnée mutable durable n’est déclarée ici ; l’extrait dépend surtout des objets reçus en paramètres et des contrats cités dans les annotations de type.
- **Déroulement :** les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les identifiants et types reçus doivent déjà être valides, et le résultat ne doit pas exposer directement une collection interne mutable.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

Une tutelle ne devient pas automatiquement une adoption. Une union ne crée pas automatiquement une filiation.

## 6. Valeur temporelle commune

### 6.1 Intervalle logique

> **[VSC] Visual Studio Code — Créer : `src/features/families/domain/logical_interval.gd`.**

```gdscript
class_name LogicalInterval
extends RefCounted

const OPEN_END := -1

var started_at_tick: int
var ended_at_tick: int

func _init(start_tick: int, end_tick: int = OPEN_END) -> void:
	started_at_tick = start_tick
	ended_at_tick = end_tick

func is_valid() -> bool:
	if started_at_tick < 0:
		return false
	if ended_at_tick == OPEN_END:
		return true
	return ended_at_tick >= started_at_tick

func is_active_at(tick: int) -> bool:
	if tick < started_at_tick:
		return false
	return ended_at_tick == OPEN_END or tick <= ended_at_tick

func close_at(tick: int) -> Error:
	if ended_at_tick != OPEN_END:
		return ERR_ALREADY_EXISTS
	if tick < started_at_tick:
		return ERR_INVALID_PARAMETER
	ended_at_tick = tick
	return OK

func duplicate_value() -> LogicalInterval:
	return LogicalInterval.new(started_at_tick, ended_at_tick)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `LogicalInterval`, dérivée de `RefCounted`.
- **Emplacement :** il appartient à `src/features/families/domain/logical_interval.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `_init(start_tick: int, end_tick: int = OPEN_END) -> void`, `is_valid(aucun paramètre) -> bool`, `is_active_at(tick: int) -> bool`, `close_at(tick: int) -> Error`, `duplicate_value(aucun paramètre) -> LogicalInterval`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare constantes `OPEN_END := -1` ; état `started_at_tick: int`, `ended_at_tick: int`. Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** retourne un code `Error` explicite. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application ; l’ordre temporel repose sur des ticks logiques et non sur l’heure système.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

Les ticks proviennent de l’horloge logique de la simulation, jamais de l’heure système de l’ordinateur. L’intervalle est inclusif : `[started_at_tick, ended_at_tick]`. `OPEN_END` signifie qu’aucune fin n’est encore connue.

## 7. Filiation dirigée

### 7.1 Modèle de lien

> **[VSC] Visual Studio Code — Créer : `src/features/families/domain/parent_child_link.gd`.**

```gdscript
class_name ParentChildLink
extends RefCounted

var link_id: StringName
var parent_id: StringName
var child_id: StringName
var kind: FamilyLinkKind.Value
var established_at_tick: int
var provenance: StringName

func _init(
	new_link_id: StringName,
	new_parent_id: StringName,
	new_child_id: StringName,
	new_kind: FamilyLinkKind.Value,
	new_tick: int,
	new_provenance: StringName,
) -> void:
	link_id = new_link_id
	parent_id = new_parent_id
	child_id = new_child_id
	kind = new_kind
	established_at_tick = new_tick
	provenance = new_provenance

func validate() -> PackedStringArray:
	var errors := PackedStringArray()
	if not FamilyLinkId.is_valid(link_id):
		errors.append("link_id invalide")
	if not CharacterId.is_valid(parent_id):
		errors.append("parent_id invalide")
	if not CharacterId.is_valid(child_id):
		errors.append("child_id invalide")
	if parent_id == child_id:
		errors.append("auto-filiation interdite")
	if not FamilyLinkKind.is_parent_kind(kind):
		errors.append("type de filiation invalide")
	if established_at_tick < 0:
		errors.append("tick négatif")
	if provenance.is_empty():
		errors.append("provenance obligatoire")
	return errors

func duplicate_value() -> ParentChildLink:
	return ParentChildLink.new(
		link_id,
		parent_id,
		child_id,
		kind,
		established_at_tick,
		provenance,
	)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `ParentChildLink`, dérivée de `RefCounted`.
- **Emplacement :** il appartient à `src/features/families/domain/parent_child_link.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `_init(new_link_id: StringName, new_parent_id: StringName, new_child_id: StringName, new_kind: FamilyLinkKind.Value, new_tick: int, new_provenance: StringName,) -> void`, `validate(aucun paramètre) -> PackedStringArray`, `duplicate_value(aucun paramètre) -> ParentChildLink`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `link_id: StringName`, `parent_id: StringName`, `child_id: StringName`, `kind: FamilyLinkKind.Value`, `established_at_tick: int` et 2 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** ajoute des éléments à une collection ou à un historique borné. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application ; un auto-lien entre une identité et elle-même est refusé.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

### 7.2 Identité métier de la filiation

Deux liens avec les mêmes `parent_id`, `child_id` et `kind` constituent un doublon métier, même si leurs `link_id` diffèrent.

Une filiation biologique et une adoption entre la même paire ne doivent pas être créées silencieusement en parallèle. La politique applicative doit décider si une transition explicite est autorisée.

## 8. Tutelle temporelle

> **[VSC] Visual Studio Code — Créer : `src/features/families/domain/guardianship_link.gd`.**

```gdscript
class_name GuardianshipLink
extends RefCounted

var link_id: StringName
var guardian_id: StringName
var ward_id: StringName
var interval: LogicalInterval
var provenance: StringName

func validate() -> PackedStringArray:
	var errors := PackedStringArray()
	if not FamilyLinkId.is_valid(link_id):
		errors.append("link_id invalide")
	if not CharacterId.is_valid(guardian_id):
		errors.append("guardian_id invalide")
	if not CharacterId.is_valid(ward_id):
		errors.append("ward_id invalide")
	if guardian_id == ward_id:
		errors.append("auto-tutelle interdite")
	if interval == null or not interval.is_valid():
		errors.append("intervalle invalide")
	if provenance.is_empty():
		errors.append("provenance obligatoire")
	return errors

func duplicate_value() -> GuardianshipLink:
	var copy := GuardianshipLink.new()
	copy.link_id = link_id
	copy.guardian_id = guardian_id
	copy.ward_id = ward_id
	copy.interval = interval.duplicate_value()
	copy.provenance = provenance
	return copy
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `GuardianshipLink`, dérivée de `RefCounted`.
- **Emplacement :** il appartient à `src/features/families/domain/guardianship_link.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `validate(aucun paramètre) -> PackedStringArray`, `duplicate_value(aucun paramètre) -> GuardianshipLink`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `link_id: StringName`, `guardian_id: StringName`, `ward_id: StringName`, `interval: LogicalInterval`, `provenance: StringName` et 2 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** ajoute des éléments à une collection ou à un historique borné. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

Deux tutelles historiques peuvent exister entre la même paire si leurs intervalles ne se chevauchent pas. Deux tutelles actives identiques sont refusées.

## 9. Union canonique

### 9.1 Paire non orientée

> **[VSC] Visual Studio Code — Créer : `src/features/families/domain/character_pair.gd`.**

```gdscript
class_name CharacterPair
extends RefCounted

var first_id: StringName
var second_id: StringName

static func create(left_id: StringName, right_id: StringName) -> CharacterPair:
	if not CharacterId.is_valid(left_id):
		return null
	if not CharacterId.is_valid(right_id):
		return null
	if left_id == right_id:
		return null

	var pair := CharacterPair.new()
	if String(left_id) < String(right_id):
		pair.first_id = left_id
		pair.second_id = right_id
	else:
		pair.first_id = right_id
		pair.second_id = left_id
	return pair

func key() -> StringName:
	return StringName("%s|%s" % [first_id, second_id])
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `CharacterPair`, dérivée de `RefCounted`.
- **Emplacement :** il appartient à `src/features/families/domain/character_pair.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `key(aucun paramètre) -> StringName`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `first_id: StringName`, `second_id: StringName`, `pair := CharacterPair.new()`. Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

La paire `{A, B}` produit la même clé que `{B, A}`.

### 9.2 Lien d’union

> **[VSC] Visual Studio Code — Créer : `src/features/families/domain/union_link.gd`.**

```gdscript
class_name UnionLink
extends RefCounted

var link_id: StringName
var pair: CharacterPair
var interval: LogicalInterval
var union_type: StringName
var provenance: StringName

func validate() -> PackedStringArray:
	var errors := PackedStringArray()
	if not FamilyLinkId.is_valid(link_id):
		errors.append("link_id invalide")
	if pair == null:
		errors.append("paire invalide")
	if interval == null or not interval.is_valid():
		errors.append("intervalle invalide")
	if union_type.is_empty():
		errors.append("union_type obligatoire")
	if provenance.is_empty():
		errors.append("provenance obligatoire")
	return errors

func duplicate_value() -> UnionLink:
	var copy := UnionLink.new()
	copy.link_id = link_id
	copy.pair = CharacterPair.create(pair.first_id, pair.second_id)
	copy.interval = interval.duplicate_value()
	copy.union_type = union_type
	copy.provenance = provenance
	return copy
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `UnionLink`, dérivée de `RefCounted`.
- **Emplacement :** il appartient à `src/features/families/domain/union_link.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `validate(aucun paramètre) -> PackedStringArray`, `duplicate_value(aucun paramètre) -> UnionLink`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `link_id: StringName`, `pair: CharacterPair`, `interval: LogicalInterval`, `union_type: StringName`, `provenance: StringName` et 2 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** ajoute des éléments à une collection ou à un historique borné. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

Le chapitre n’impose ni exclusivité, ni monogamie, ni règles culturelles universelles. Ces politiques appartiennent à des données ou règles de monde explicites.

## 10. Contrat de l’index logique des personnages

> **[VSC] Visual Studio Code — Réutiliser : `src/features/characters/application/character_identity_index.gd`, introduit au chapitre 15.**

Le chapitre 16 ne redéfinit pas cette classe. Il consomme le même contrat logique :

> **[LECTURE] Exemple d’appel — Ne pas créer une seconde classe.**

```gdscript
if not identity_index.contains(character_id):
	return ERR_DOES_NOT_EXIST
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à illustrer concrètement la règle présentée dans « ce passage ».
- **Emplacement :** il appartient à `src/features/characters/application/character_identity_index.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** ce bloc ne déclare pas de fonction publique ; ses données sont consommées par le code qui l’instancie ou le décode. Les types visibles dans les déclarations constituent néanmoins le contrat à respecter.
- **État et dépendances :** aucune donnée mutable durable n’est déclarée ici ; l’extrait dépend surtout des objets reçus en paramètres et des contrats cités dans les annotations de type.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** retourne un code `Error` explicite. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les doublons et références déjà connues sont détectés.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

L’index contient les identités logiques :

- actives ;
- déchargées ;
- décédées ;
- archivées mais encore référencées.

Le graphe familial ne consulte jamais uniquement `ActiveCharacterRegistry`.

## 11. Graphe familial

### 11.1 Stockages internes

> **[VSC] Visual Studio Code — Créer : `src/features/families/domain/family_graph.gd`.**

```gdscript
class_name FamilyGraph
extends RefCounted

const MAX_TRAVERSAL_NODES := 4096

var _parent_links: Dictionary[StringName, ParentChildLink] = {}
var _guardian_links: Dictionary[StringName, GuardianshipLink] = {}
var _union_links: Dictionary[StringName, UnionLink] = {}

var _parents_by_child: Dictionary[StringName, Array] = {}
var _children_by_parent: Dictionary[StringName, Array] = {}
var _unions_by_pair: Dictionary[StringName, Array] = {}
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `FamilyGraph`, dérivée de `RefCounted`.
- **Emplacement :** il appartient à `src/features/families/domain/family_graph.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** ce bloc ne déclare pas de fonction publique ; ses données sont consommées par le code qui l’instancie ou le décode. Les types visibles dans les déclarations constituent néanmoins le contrat à respecter.
- **État et dépendances :** le bloc déclare constantes `MAX_TRAVERSAL_NODES := 4096` ; état `_parent_links: Dictionary[StringName, ParentChildLink] = {}`, `_guardian_links: Dictionary[StringName, GuardianshipLink] = {}`, `_union_links: Dictionary[StringName, UnionLink] = {}`, `_parents_by_child: Dictionary[StringName, Array] = {}`, `_children_by_parent: Dictionary[StringName, Array] = {}` et 1 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les instructions sont exécutées dans l’ordre, de la construction des données vers leur validation puis leur exposition.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les parcours ou historiques restent bornés.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

Les index secondaires contiennent des identifiants de liens, pas des copies d’objets.

### 11.2 Ajouter une filiation

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
func add_parent_link(link: ParentChildLink) -> Error:
	if link == null:
		return ERR_INVALID_PARAMETER
	if not link.validate().is_empty():
		return ERR_INVALID_DATA
	if _parent_links.has(link.link_id):
		return ERR_ALREADY_EXISTS
	if _has_parent_edge(link.parent_id, link.child_id):
		return ERR_ALREADY_EXISTS
	if _would_create_ancestry_cycle(link.parent_id, link.child_id):
		return ERR_CYCLIC_LINK

	_parent_links[link.link_id] = link.duplicate_value()
	_append_index(_parents_by_child, link.child_id, link.link_id)
	_append_index(_children_by_parent, link.parent_id, link.link_id)
	return OK
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `add_parent_link()` utilisées dans « 11.2 Ajouter une filiation ».
- **Emplacement :** il appartient à `src/features/families/domain/family_graph.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `add_parent_link(link: ParentChildLink) -> Error`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** aucune donnée mutable durable n’est déclarée ici ; l’extrait dépend surtout des objets reçus en paramètres et des contrats cités dans les annotations de type.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** retourne un code `Error` explicite. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application ; les doublons et références déjà connues sont détectés ; la structure hiérarchique ne peut pas introduire de cycle d’ascendance.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

L’ordre est important :

1. validation locale ;
2. doublon d’identifiant ;
3. doublon métier ;
4. cycle global ;
5. mutation des trois structures.

### 11.3 Cycle d’ascendance

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
func _would_create_ancestry_cycle(
	parent_id: StringName,
	child_id: StringName,
) -> bool:
	if parent_id == child_id:
		return true

	var pending: Array[StringName] = [child_id]
	var visited: Dictionary[StringName, bool] = {}

	while not pending.is_empty():
		if visited.size() >= MAX_TRAVERSAL_NODES:
			push_error("Parcours familial au-delà de la limite.")
			return true

		var current: StringName = pending.pop_back()
		if current == parent_id:
			return true
		if visited.has(current):
			continue
		visited[current] = true

		for descendant_id: StringName in get_children(current):
			if not visited.has(descendant_id):
				pending.append(descendant_id)

	return false
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `_would_create_ancestry_cycle()` utilisées dans « 11.3 Cycle d’ascendance ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `_would_create_ancestry_cycle(parent_id: StringName, child_id: StringName,) -> bool`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `pending: Array[StringName] = [child_id]`, `visited: Dictionary[StringName, bool] = {}`, `current: StringName = pending.pop_back()`. Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les boucles `for` parcourent les collections de façon explicite ; la boucle `while` poursuit un parcours borné jusqu’à épuisement de la file ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** ajoute des éléments à une collection ou à un historique borné ; enregistre une erreur exploitable par l’appelant. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** un auto-lien entre une identité et elle-même est refusé ; les doublons et références déjà connues sont détectés ; les parcours ou historiques restent bornés ; la structure hiérarchique ne peut pas introduire de cycle d’ascendance.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

Ajouter `parent → enfant` crée un cycle si `parent` est déjà descendant de `enfant`.

Le dépassement de budget est traité comme un refus conservateur, pas comme une absence de cycle.

### 11.4 Helpers d’index

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
func _append_index(
	index: Dictionary[StringName, Array],
	character_id: StringName,
	link_id: StringName,
) -> void:
	var ids: Array = index.get(character_id, [])
	if not ids.has(link_id):
		ids.append(link_id)
		index[character_id] = ids

func _has_parent_edge(
	parent_id: StringName,
	child_id: StringName,
) -> bool:
	for link_id: StringName in _children_by_parent.get(parent_id, []):
		var link := _parent_links.get(link_id) as ParentChildLink
		if link != null and link.child_id == child_id:
			return true
	return false

func get_parent_links() -> Array[ParentChildLink]:
	var result: Array[ParentChildLink] = []
	for link: ParentChildLink in _parent_links.values():
		result.append(link.duplicate_value())
	return result

func get_guardianship_links() -> Array[GuardianshipLink]:
	var result: Array[GuardianshipLink] = []
	for link: GuardianshipLink in _guardian_links.values():
		result.append(link.duplicate_value())
	return result

func get_union_links() -> Array[UnionLink]:
	var result: Array[UnionLink] = []
	for link: UnionLink in _union_links.values():
		result.append(link.duplicate_value())
	return result
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `_append_index()`, `_has_parent_edge()`, `get_parent_links()`, `get_guardianship_links()` utilisées dans « 11.4 Helpers d’index ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `_append_index(index: Dictionary[StringName, Array], character_id: StringName, link_id: StringName,) -> void`, `_has_parent_edge(parent_id: StringName, child_id: StringName,) -> bool`, `get_parent_links(aucun paramètre) -> Array[ParentChildLink]`, `get_guardianship_links(aucun paramètre) -> Array[GuardianshipLink]`, `get_union_links(aucun paramètre) -> Array[UnionLink]`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `ids: Array = index.get(character_id, [])`, `link := _parent_links.get(link_id) as ParentChildLink`, `result: Array[ParentChildLink] = []`, `result: Array[GuardianshipLink] = []`, `result: Array[UnionLink] = []`. Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les boucles `for` parcourent les collections de façon explicite ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** ajoute des éléments à une collection ou à un historique borné. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** un auto-lien entre une identité et elle-même est refusé ; les doublons et références déjà connues sont détectés.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

## 12. Requêtes de filiation

### 12.1 Parents et enfants directs

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
func get_parents(child_id: StringName) -> Array[StringName]:
	var result: Array[StringName] = []
	for link_id: StringName in _parents_by_child.get(child_id, []):
		var link := _parent_links.get(link_id) as ParentChildLink
		if link != null and not result.has(link.parent_id):
			result.append(link.parent_id)
	result.sort()
	return result

func get_children(parent_id: StringName) -> Array[StringName]:
	var result: Array[StringName] = []
	for link_id: StringName in _children_by_parent.get(parent_id, []):
		var link := _parent_links.get(link_id) as ParentChildLink
		if link != null and not result.has(link.child_id):
			result.append(link.child_id)
	result.sort()
	return result
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `get_parents()`, `get_children()` utilisées dans « 12.1 Parents et enfants directs ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `get_parents(child_id: StringName) -> Array[StringName]`, `get_children(parent_id: StringName) -> Array[StringName]`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `result: Array[StringName] = []`, `link := _parent_links.get(link_id) as ParentChildLink`, `result: Array[StringName] = []`, `link := _parent_links.get(link_id) as ParentChildLink`. Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les boucles `for` parcourent les collections de façon explicite ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** ajoute des éléments à une collection ou à un historique borné. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les doublons et références déjà connues sont détectés.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

Les tableaux retournés sont nouveaux. L’appelant ne reçoit jamais les collections internes mutables.

### 12.2 Fratrie calculée

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
func get_siblings(character_id: StringName) -> Array[StringName]:
	var siblings: Dictionary[StringName, bool] = {}

	for parent_id: StringName in get_parents(character_id):
		for child_id: StringName in get_children(parent_id):
			if child_id != character_id:
				siblings[child_id] = true

	var result: Array[StringName] = []
	result.assign(siblings.keys())
	result.sort()
	return result
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `get_siblings()` utilisées dans « 12.2 Fratrie calculée ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `get_siblings(character_id: StringName) -> Array[StringName]`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `siblings: Dictionary[StringName, bool] = {}`, `result: Array[StringName] = []`. Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les boucles `for` parcourent les collections de façon explicite ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les clés ou types inattendus sont refusés au lieu d’être convertis silencieusement.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

Cette définition retourne les demi-frères et demi-sœurs dès qu’au moins un parent est partagé.

Une politique plus stricte peut comparer l’ensemble complet des parents, mais elle doit être explicitement nommée.

### 12.3 Ancêtres bornés

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
func get_ancestors(
	character_id: StringName,
	max_depth: int = 32,
) -> Dictionary[StringName, int]:
	var distances: Dictionary[StringName, int] = {}
	if max_depth < 0 or max_depth > 32:
		push_error("Profondeur d’ancêtres hors limites.")
		return distances

	var pending: Array[Dictionary] = [
		{"id": character_id, "depth": 0},
	]
	var visited_nodes := 0

	while not pending.is_empty():
		if visited_nodes >= MAX_TRAVERSAL_NODES:
			push_error("Parcours d’ancêtres interrompu par le budget.")
			return {}
		visited_nodes += 1

		var entry: Dictionary = pending.pop_front()
		var current: StringName = entry["id"]
		var depth: int = entry["depth"]

		if depth >= max_depth:
			continue

		for parent_id: StringName in get_parents(current):
			var next_depth := depth + 1
			if distances.has(parent_id):
				if distances[parent_id] <= next_depth:
					continue
			distances[parent_id] = next_depth
			pending.append({"id": parent_id, "depth": next_depth})

	return distances
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `get_ancestors()` utilisées dans « 12.3 Ancêtres bornés ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `get_ancestors(character_id: StringName, max_depth: int = 32,) -> Dictionary[StringName, int]`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `distances: Dictionary[StringName, int] = {}`, `pending: Array[Dictionary] = [`, `visited_nodes := 0`, `entry: Dictionary = pending.pop_front()`, `current: StringName = entry["id"]` et 2 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les boucles `for` parcourent les collections de façon explicite ; la boucle `while` poursuit un parcours borné jusqu’à épuisement de la file ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** ajoute des éléments à une collection ou à un historique borné ; enregistre une erreur exploitable par l’appelant. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les doublons et références déjà connues sont détectés ; les parcours ou historiques restent bornés ; la structure hiérarchique ne peut pas introduire de cycle d’ascendance.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

La valeur associée est la distance minimale :

- `1` : parent ;
- `2` : grand-parent ;
- `3` : arrière-grand-parent.

### 12.4 Descendants bornés

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
func get_descendants(
	character_id: StringName,
	max_depth: int = 32,
) -> Dictionary[StringName, int]:
	var distances: Dictionary[StringName, int] = {}
	if max_depth < 0 or max_depth > 32:
		push_error("Profondeur de descendants hors limites.")
		return distances

	var pending: Array[Dictionary] = [
		{"id": character_id, "depth": 0},
	]
	var visited_nodes := 0

	while not pending.is_empty():
		if visited_nodes >= MAX_TRAVERSAL_NODES:
			push_error("Parcours de descendants interrompu par le budget.")
			return {}
		visited_nodes += 1

		var entry: Dictionary = pending.pop_front()
		var current: StringName = entry["id"]
		var depth: int = entry["depth"]

		if depth >= max_depth:
			continue

		for child_id: StringName in get_children(current):
			var next_depth := depth + 1
			if distances.has(child_id):
				if distances[child_id] <= next_depth:
					continue
			distances[child_id] = next_depth
			pending.append({"id": child_id, "depth": next_depth})

	return distances
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `get_descendants()` utilisées dans « 12.4 Descendants bornés ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `get_descendants(character_id: StringName, max_depth: int = 32,) -> Dictionary[StringName, int]`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `distances: Dictionary[StringName, int] = {}`, `pending: Array[Dictionary] = [`, `visited_nodes := 0`, `entry: Dictionary = pending.pop_front()`, `current: StringName = entry["id"]` et 2 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les boucles `for` parcourent les collections de façon explicite ; la boucle `while` poursuit un parcours borné jusqu’à épuisement de la file ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** ajoute des éléments à une collection ou à un historique borné ; enregistre une erreur exploitable par l’appelant. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les doublons et références déjà connues sont détectés ; les parcours ou historiques restent bornés ; la structure hiérarchique ne peut pas introduire de cycle d’ascendance.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

## 13. Générations dérivées

### 13.1 Pourquoi ne pas persister `generation_number`

Un numéro absolu dépend du point de référence. Dans un monde comportant plusieurs lignées et unions, « génération 4 » n’a pas de sens universel.

On calcule plutôt :

- distance à un ancêtre choisi ;
- profondeur maximale connue ;
- cohorte de descendants d’un fondateur ;
- niveau relatif entre deux personnages.

### 13.2 Distance générationnelle

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
func get_generation_distance(
	ancestor_id: StringName,
	descendant_id: StringName,
	max_depth: int = 32,
) -> int:
	var descendants := get_descendants(ancestor_id, max_depth)
	return int(descendants.get(descendant_id, -1))
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `get_generation_distance()` utilisées dans « 13.2 Distance générationnelle ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `get_generation_distance(ancestor_id: StringName, descendant_id: StringName, max_depth: int = 32,) -> int`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `descendants := get_descendants(ancestor_id, max_depth)`. Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les parcours ou historiques restent bornés ; la structure hiérarchique ne peut pas introduire de cycle d’ascendance.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

`-1` signifie qu’aucun chemin n’a été trouvé dans la profondeur autorisée.

## 14. Tutelles et unions actives

### 14.1 Ajouter une tutelle

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
func add_guardianship(link: GuardianshipLink) -> Error:
	if link == null or not link.validate().is_empty():
		return ERR_INVALID_DATA
	if _guardian_links.has(link.link_id):
		return ERR_ALREADY_EXISTS

	for existing: GuardianshipLink in _guardian_links.values():
		if (
			existing.guardian_id == link.guardian_id
			and existing.ward_id == link.ward_id
			and _intervals_overlap(existing.interval, link.interval)
		):
			return ERR_ALREADY_EXISTS

	_guardian_links[link.link_id] = link.duplicate_value()
	return OK
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `add_guardianship()` utilisées dans « 14.1 Ajouter une tutelle ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `add_guardianship(link: GuardianshipLink) -> Error`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** aucune donnée mutable durable n’est déclarée ici ; l’extrait dépend surtout des objets reçus en paramètres et des contrats cités dans les annotations de type.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les boucles `for` parcourent les collections de façon explicite ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** retourne un code `Error` explicite. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application ; les doublons et références déjà connues sont détectés.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

### 14.2 Ajouter une union

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
func add_union(link: UnionLink) -> Error:
	if link == null or not link.validate().is_empty():
		return ERR_INVALID_DATA
	if _union_links.has(link.link_id):
		return ERR_ALREADY_EXISTS

	var pair_key := link.pair.key()
	for existing_id: StringName in _unions_by_pair.get(pair_key, []):
		var existing := _union_links.get(existing_id) as UnionLink
		if existing != null and _intervals_overlap(
			existing.interval,
			link.interval,
		):
			return ERR_ALREADY_EXISTS

	_union_links[link.link_id] = link.duplicate_value()
	_append_index(_unions_by_pair, pair_key, link.link_id)
	return OK
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `add_union()` utilisées dans « 14.2 Ajouter une union ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `add_union(link: UnionLink) -> Error`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `pair_key := link.pair.key()`, `existing := _union_links.get(existing_id) as UnionLink`. Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les boucles `for` parcourent les collections de façon explicite ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** retourne un code `Error` explicite. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application ; les doublons et références déjà connues sont détectés.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

### 14.3 Chevauchement d’intervalles

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
func _intervals_overlap(
	left: LogicalInterval,
	right: LogicalInterval,
) -> bool:
	var left_end := (
		9223372036854775807
		if left.ended_at_tick == LogicalInterval.OPEN_END
		else left.ended_at_tick
	)
	var right_end := (
		9223372036854775807
		if right.ended_at_tick == LogicalInterval.OPEN_END
		else right.ended_at_tick
	)
	return (
		left.started_at_tick <= right_end
		and right.started_at_tick <= left_end
	)

func replace_all_from(source: FamilyGraph) -> Error:
	if source == null:
		return ERR_INVALID_PARAMETER

	var candidate := FamilyGraph.new()
	for link: ParentChildLink in source.get_parent_links():
		var parent_result := candidate.add_parent_link(link)
		if parent_result != OK:
			return parent_result
	for link: GuardianshipLink in source.get_guardianship_links():
		var guardian_result := candidate.add_guardianship(link)
		if guardian_result != OK:
			return guardian_result
	for link: UnionLink in source.get_union_links():
		var union_result := candidate.add_union(link)
		if union_result != OK:
			return union_result

	_parent_links = candidate._parent_links
	_guardian_links = candidate._guardian_links
	_union_links = candidate._union_links
	_parents_by_child = candidate._parents_by_child
	_children_by_parent = candidate._children_by_parent
	_unions_by_pair = candidate._unions_by_pair
	return OK
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `_intervals_overlap()`, `replace_all_from()` utilisées dans « 14.3 Chevauchement d’intervalles ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `_intervals_overlap(left: LogicalInterval, right: LogicalInterval,) -> bool`, `replace_all_from(source: FamilyGraph) -> Error`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `left_end := (`, `right_end := (`, `candidate := FamilyGraph.new()`, `parent_result := candidate.add_parent_link(link)`, `guardian_result := candidate.add_guardianship(link)` et 1 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les boucles `for` parcourent les collections de façon explicite ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** remplace l’état autoritaire seulement après validation du candidat ; retourne un code `Error` explicite. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** un auto-lien entre une identité et elle-même est refusé ; la donnée candidate est préparée entièrement avant toute mutation de l’état actif.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

## 15. Service applicatif

### 15.1 Commande de filiation

> **[VSC] Visual Studio Code — Créer : `src/features/families/application/add_parent_link_command.gd`.**

```gdscript
class_name AddParentLinkCommand
extends RefCounted

var parent_id: StringName
var child_id: StringName
var kind: FamilyLinkKind.Value
var tick: int
var provenance: StringName

func validate() -> PackedStringArray:
	var errors := PackedStringArray()
	if not CharacterId.is_valid(parent_id):
		errors.append("parent_id invalide")
	if not CharacterId.is_valid(child_id):
		errors.append("child_id invalide")
	if parent_id == child_id:
		errors.append("auto-filiation interdite")
	if not FamilyLinkKind.is_parent_kind(kind):
		errors.append("kind invalide")
	if tick < 0:
		errors.append("tick négatif")
	if provenance.is_empty():
		errors.append("provenance obligatoire")
	return errors
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `AddParentLinkCommand`, dérivée de `RefCounted`.
- **Emplacement :** il appartient à `src/features/families/application/add_parent_link_command.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `validate(aucun paramètre) -> PackedStringArray`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `parent_id: StringName`, `child_id: StringName`, `kind: FamilyLinkKind.Value`, `tick: int`, `provenance: StringName` et 1 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** ajoute des éléments à une collection ou à un historique borné. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application ; un auto-lien entre une identité et elle-même est refusé.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

### 15.2 Événement typé

> **[VSC] Visual Studio Code — Créer : `src/features/families/application/family_link_added_event.gd`.**

```gdscript
class_name FamilyLinkAddedEvent
extends RefCounted

var link_id: StringName
var kind: FamilyLinkKind.Value
var first_character_id: StringName
var second_character_id: StringName
var tick: int
var provenance: StringName
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `FamilyLinkAddedEvent`, dérivée de `RefCounted`.
- **Emplacement :** il appartient à `src/features/families/application/family_link_added_event.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** ce bloc ne déclare pas de fonction publique ; ses données sont consommées par le code qui l’instancie ou le décode. Les types visibles dans les déclarations constituent néanmoins le contrat à respecter.
- **État et dépendances :** le bloc déclare état `link_id: StringName`, `kind: FamilyLinkKind.Value`, `first_character_id: StringName`, `second_character_id: StringName`, `tick: int` et 1 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les instructions sont exécutées dans l’ordre, de la construction des données vers leur validation puis leur exposition.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les identifiants et types reçus doivent déjà être valides, et le résultat ne doit pas exposer directement une collection interne mutable.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

### 15.3 Orchestration

> **[VSC] Visual Studio Code — Créer : `src/features/families/application/family_graph_service.gd`.**

```gdscript
class_name FamilyGraphService
extends RefCounted

signal family_link_added(event: FamilyLinkAddedEvent)
signal family_link_closed(
	link_id: StringName,
	closed_at_tick: int,
	provenance: StringName,
)

var _graph: FamilyGraph
var _identities: CharacterIdentityIndex

func _init(
	graph: FamilyGraph,
	identities: CharacterIdentityIndex,
) -> void:
	_graph = graph
	_identities = identities

func add_parent_link(command: AddParentLinkCommand) -> Error:
	if command == null or not command.validate().is_empty():
		return ERR_INVALID_DATA
	if not _identities.contains(command.parent_id):
		return ERR_DOES_NOT_EXIST
	if not _identities.contains(command.child_id):
		return ERR_DOES_NOT_EXIST

	var link := ParentChildLink.new(
		FamilyLinkId.create_random(),
		command.parent_id,
		command.child_id,
		command.kind,
		command.tick,
		command.provenance,
	)
	var result := _graph.add_parent_link(link)
	if result != OK:
		return result

	var event := FamilyLinkAddedEvent.new()
	event.link_id = link.link_id
	event.kind = link.kind
	event.first_character_id = link.parent_id
	event.second_character_id = link.child_id
	event.tick = link.established_at_tick
	event.provenance = link.provenance
	family_link_added.emit(event)
	return OK
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `FamilyGraphService`, dérivée de `RefCounted`.
- **Emplacement :** il appartient à `src/features/families/application/family_graph_service.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `_init(graph: FamilyGraph, identities: CharacterIdentityIndex,) -> void`, `add_parent_link(command: AddParentLinkCommand) -> Error`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `_graph: FamilyGraph`, `_identities: CharacterIdentityIndex`, `link := ParentChildLink.new(`, `result := _graph.add_parent_link(link)`, `event := FamilyLinkAddedEvent.new()` ; signaux `family_link_added(event: FamilyLinkAddedEvent)`, `family_link_closed(`. Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** émet un signal ou un événement après la mutation ; retourne un code `Error` explicite. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application ; les doublons et références déjà connues sont détectés.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

Le service vérifie les identités logiques avant le graphe. Le graphe conserve néanmoins ses propres invariants structurels.

## 16. Historique familial

### 16.1 Événement persistant minimal

> **[VSC] Visual Studio Code — Créer : `src/features/families/domain/family_history_record.gd`.**

```gdscript
class_name FamilyHistoryRecord
extends RefCounted

var sequence: int
var event_type: StringName
var link_id: StringName
var tick: int
var provenance: StringName

func validate() -> bool:
	return (
		sequence >= 0
		and not event_type.is_empty()
		and FamilyLinkId.is_valid(link_id)
		and tick >= 0
		and not provenance.is_empty()
	)

func duplicate_value() -> FamilyHistoryRecord:
	var copy := FamilyHistoryRecord.new()
	copy.sequence = sequence
	copy.event_type = event_type
	copy.link_id = link_id
	copy.tick = tick
	copy.provenance = provenance
	return copy
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `FamilyHistoryRecord`, dérivée de `RefCounted`.
- **Emplacement :** il appartient à `src/features/families/domain/family_history_record.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `validate(aucun paramètre) -> bool`, `duplicate_value(aucun paramètre) -> FamilyHistoryRecord`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `sequence: int`, `event_type: StringName`, `link_id: StringName`, `tick: int`, `provenance: StringName` et 1 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application ; les parcours ou historiques restent bornés.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

### 16.2 Journal borné

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
class_name FamilyEventLog
extends RefCounted

const MAX_RECORDS := 256

var _records: Array[FamilyHistoryRecord] = []
var _next_sequence := 0

func append(
	event_type: StringName,
	link_id: StringName,
	tick: int,
	provenance: StringName,
) -> Error:
	var record := FamilyHistoryRecord.new()
	record.sequence = _next_sequence
	record.event_type = event_type
	record.link_id = link_id
	record.tick = tick
	record.provenance = provenance
	if not record.validate():
		return ERR_INVALID_DATA

	_next_sequence += 1
	_records.append(record)
	while _records.size() > MAX_RECORDS:
		_records.pop_front()
	return OK

func snapshot() -> Array[FamilyHistoryRecord]:
	var result: Array[FamilyHistoryRecord] = []
	for record: FamilyHistoryRecord in _records:
		result.append(record.duplicate_value())
	return result

func restore(records: Array[FamilyHistoryRecord]) -> Error:
	if records.size() > MAX_RECORDS:
		return ERR_OUT_OF_MEMORY

	var candidate: Array[FamilyHistoryRecord] = []
	var previous_sequence := -1

	for record: FamilyHistoryRecord in records:
		if record == null or not record.validate():
			return ERR_INVALID_DATA
		if record.sequence <= previous_sequence:
			return ERR_INVALID_DATA
		previous_sequence = record.sequence
		candidate.append(record.duplicate_value())

	_records = candidate
	_next_sequence = previous_sequence + 1
	return OK
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `FamilyEventLog`, dérivée de `RefCounted`.
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `append(event_type: StringName, link_id: StringName, tick: int, provenance: StringName,) -> Error`, `snapshot(aucun paramètre) -> Array[FamilyHistoryRecord]`, `restore(records: Array[FamilyHistoryRecord]) -> Error`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare constantes `MAX_RECORDS := 256` ; état `_records: Array[FamilyHistoryRecord] = []`, `_next_sequence := 0`, `record := FamilyHistoryRecord.new()`, `result: Array[FamilyHistoryRecord] = []`, `candidate: Array[FamilyHistoryRecord] = []` et 1 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les boucles `for` parcourent les collections de façon explicite ; la boucle `while` poursuit un parcours borné jusqu’à épuisement de la file ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** ajoute des éléments à une collection ou à un historique borné ; retourne un code `Error` explicite. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application ; les parcours ou historiques restent bornés ; la donnée candidate est préparée entièrement avant toute mutation de l’état actif.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

Le journal n’est pas un journal légal exhaustif. Il fournit un historique borné utile au gameplay et au diagnostic.

## 17. Validation globale

### 17.1 Pourquoi valider le graphe entier

Une série de liens localement valides peut contenir :

- un cycle ;
- un index secondaire désynchronisé ;
- un lien vers une identité inconnue ;
- deux unions chevauchantes identiques ;
- une tutelle terminée avant son début ;
- un doublon métier.

### 17.2 Validateur

> **[VSC] Visual Studio Code — Créer : `src/features/families/application/family_graph_validator.gd`.**

```gdscript
class_name FamilyGraphValidator
extends RefCounted

func validate(
	graph: FamilyGraph,
	identities: CharacterIdentityIndex,
) -> PackedStringArray:
	var errors := PackedStringArray()

	for link: ParentChildLink in graph.get_parent_links():
		if not identities.contains(link.parent_id):
			errors.append("Parent inconnu : %s" % link.parent_id)
		if not identities.contains(link.child_id):
			errors.append("Enfant inconnu : %s" % link.child_id)
		errors.append_array(link.validate())

	for link: GuardianshipLink in graph.get_guardianship_links():
		if not identities.contains(link.guardian_id):
			errors.append("Tuteur inconnu : %s" % link.guardian_id)
		if not identities.contains(link.ward_id):
			errors.append("Protégé inconnu : %s" % link.ward_id)
		errors.append_array(link.validate())

	for link: UnionLink in graph.get_union_links():
		if link.pair != null:
			if not identities.contains(link.pair.first_id):
				errors.append("Partenaire inconnu : %s" % link.pair.first_id)
			if not identities.contains(link.pair.second_id):
				errors.append("Partenaire inconnu : %s" % link.pair.second_id)
		errors.append_array(link.validate())

	return errors
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `FamilyGraphValidator`, dérivée de `RefCounted`.
- **Emplacement :** il appartient à `src/features/families/application/family_graph_validator.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `validate(graph: FamilyGraph, identities: CharacterIdentityIndex,) -> PackedStringArray`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `errors := PackedStringArray()`. Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les boucles `for` parcourent les collections de façon explicite ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** ajoute des éléments à une collection ou à un historique borné. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application ; les doublons et références déjà connues sont détectés.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

Le validateur de restauration sera exécuté sur un graphe candidat complet avant remplacement de l’état courant.

## 18. Snapshot persistant

### 18.1 Structure JSON

> **[LECTURE] Exemple de snapshot familial — Ne pas créer manuellement.**

```json
{
  "format_version": 1,
  "parent_links": [],
  "guardianships": [],
  "unions": [],
  "history": []
}
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à montrer la structure de données sérialisée attendue dans « 18.1 Structure JSON ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** ce bloc ne déclare pas de fonction publique ; ses données sont consommées par le code qui l’instancie ou le décode. Les types visibles dans les déclarations constituent néanmoins le contrat à respecter.
- **État et dépendances :** aucune donnée mutable durable n’est déclarée ici ; l’extrait dépend surtout des objets reçus en paramètres et des contrats cités dans les annotations de type.
- **Déroulement :** les instructions sont exécutées dans l’ordre, de la construction des données vers leur validation puis leur exposition.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les parcours ou historiques restent bornés.
- **Résultat attendu :** le document peut être décodé strictement, avec les clés et types attendus et sans valeur dérivée persistée. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

Le snapshot ne contient pas :

- les générations calculées ;
- les fratries calculées ;
- les index secondaires ;
- les nœuds actifs ;
- les noms affichés ;
- les vues sociales ;
- les caches d’ancêtres.

### 18.2 Limites du codec

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
class_name FamilySnapshotCodec
extends RefCounted

const FORMAT_VERSION := 1
const MAX_PARENT_LINKS := 8192
const MAX_GUARDIANSHIPS := 4096
const MAX_UNIONS := 4096
const MAX_HISTORY_RECORDS := 256
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `FamilySnapshotCodec`, dérivée de `RefCounted`.
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** ce bloc ne déclare pas de fonction publique ; ses données sont consommées par le code qui l’instancie ou le décode. Les types visibles dans les déclarations constituent néanmoins le contrat à respecter.
- **État et dépendances :** le bloc déclare constantes `FORMAT_VERSION := 1`, `MAX_PARENT_LINKS := 8192`, `MAX_GUARDIANSHIPS := 4096`, `MAX_UNIONS := 4096` et 1 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les instructions sont exécutées dans l’ordre, de la construction des données vers leur validation puis leur exposition.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les parcours ou historiques restent bornés.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

### 18.3 Encodeurs

> **[VSC] Visual Studio Code — Créer : `src/features/families/infrastructure/family_snapshot_codec.gd`.**

```gdscript
func encode_graph(
	graph: FamilyGraph,
	history: FamilyEventLog,
) -> Dictionary:
	var parent_links: Array[Dictionary] = []
	for link: ParentChildLink in graph.get_parent_links():
		parent_links.append(_encode_parent_link(link))

	var guardianships: Array[Dictionary] = []
	for link: GuardianshipLink in graph.get_guardianship_links():
		guardianships.append(_encode_guardianship(link))

	var unions: Array[Dictionary] = []
	for link: UnionLink in graph.get_union_links():
		unions.append(_encode_union(link))

	var history_records: Array[Dictionary] = []
	for record: FamilyHistoryRecord in history.snapshot():
		history_records.append(_encode_history(record))

	return {
		"format_version": FORMAT_VERSION,
		"parent_links": parent_links,
		"guardianships": guardianships,
		"unions": unions,
		"history": history_records,
	}

func _encode_parent_link(link: ParentChildLink) -> Dictionary:
	return {
		"link_id": String(link.link_id),
		"parent_id": String(link.parent_id),
		"child_id": String(link.child_id),
		"kind": int(link.kind),
		"established_at_tick": link.established_at_tick,
		"provenance": String(link.provenance),
	}

func _encode_interval(interval: LogicalInterval) -> Dictionary:
	return {
		"started_at_tick": interval.started_at_tick,
		"ended_at_tick": interval.ended_at_tick,
	}

func _encode_guardianship(link: GuardianshipLink) -> Dictionary:
	return {
		"link_id": String(link.link_id),
		"guardian_id": String(link.guardian_id),
		"ward_id": String(link.ward_id),
		"interval": _encode_interval(link.interval),
		"provenance": String(link.provenance),
	}

func _encode_union(link: UnionLink) -> Dictionary:
	return {
		"link_id": String(link.link_id),
		"first_id": String(link.pair.first_id),
		"second_id": String(link.pair.second_id),
		"interval": _encode_interval(link.interval),
		"union_type": String(link.union_type),
		"provenance": String(link.provenance),
	}

func _encode_history(record: FamilyHistoryRecord) -> Dictionary:
	return {
		"sequence": record.sequence,
		"event_type": String(record.event_type),
		"link_id": String(record.link_id),
		"tick": record.tick,
		"provenance": String(record.provenance),
	}
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `encode_graph()`, `_encode_parent_link()`, `_encode_interval()`, `_encode_guardianship()` utilisées dans « ce passage ».
- **Emplacement :** il appartient à `src/features/families/infrastructure/family_snapshot_codec.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `encode_graph(graph: FamilyGraph, history: FamilyEventLog,) -> Dictionary`, `_encode_parent_link(link: ParentChildLink) -> Dictionary`, `_encode_interval(interval: LogicalInterval) -> Dictionary`, `_encode_guardianship(link: GuardianshipLink) -> Dictionary`, `_encode_union(link: UnionLink) -> Dictionary`, `_encode_history(record: FamilyHistoryRecord) -> Dictionary`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `parent_links: Array[Dictionary] = []`, `guardianships: Array[Dictionary] = []`, `unions: Array[Dictionary] = []`, `history_records: Array[Dictionary] = []`. Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les boucles `for` parcourent les collections de façon explicite ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** ajoute des éléments à une collection ou à un historique borné. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les parcours ou historiques restent bornés.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

### 18.4 Décodage strict d’une filiation

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
func _decode_parent_link(
	value: Variant,
	identities: CharacterIdentityIndex,
) -> ParentChildLink:
	if not value is Dictionary:
		return null
	var data := value as Dictionary
	var required := [
		"link_id",
		"parent_id",
		"child_id",
		"kind",
		"established_at_tick",
		"provenance",
	]
	if not _has_exact_keys(data, required):
		return null
	if not _types_match(
		data,
		{
			"link_id": TYPE_STRING,
			"parent_id": TYPE_STRING,
			"child_id": TYPE_STRING,
			"kind": TYPE_INT,
			"established_at_tick": TYPE_INT,
			"provenance": TYPE_STRING,
		},
	):
		return null

	var parent_id := StringName(data["parent_id"])
	var child_id := StringName(data["child_id"])
	if not identities.contains(parent_id):
		return null
	if not identities.contains(child_id):
		return null

	var kind_value: int = data["kind"]
	if not FamilyLinkKind.is_known(kind_value):
		return null

	var link := ParentChildLink.new(
		StringName(data["link_id"]),
		parent_id,
		child_id,
		kind_value,
		data["established_at_tick"],
		StringName(data["provenance"]),
	)
	if not link.validate().is_empty():
		return null
	return link
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `_decode_parent_link()` utilisées dans « 18.4 Décodage strict d’une filiation ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `_decode_parent_link(value: Variant, identities: CharacterIdentityIndex,) -> ParentChildLink`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `data := value as Dictionary`, `required := [`, `parent_id := StringName(data["parent_id"])`, `child_id := StringName(data["child_id"])`, `kind_value: int = data["kind"]` et 1 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application ; les doublons et références déjà connues sont détectés ; les clés ou types inattendus sont refusés au lieu d’être convertis silencieusement.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

### 18.5 Intervalles, tutelles et unions

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
func _decode_interval(value: Variant) -> LogicalInterval:
	if not value is Dictionary:
		return null
	var data := value as Dictionary
	if not _has_exact_keys(
		data,
		["started_at_tick", "ended_at_tick"],
	):
		return null
	if not data["started_at_tick"] is int:
		return null
	if not data["ended_at_tick"] is int:
		return null

	var interval := LogicalInterval.new(
		data["started_at_tick"],
		data["ended_at_tick"],
	)
	return interval if interval.is_valid() else null

func _decode_guardianship(
	value: Variant,
	identities: CharacterIdentityIndex,
) -> GuardianshipLink:
	if not value is Dictionary:
		return null
	var data := value as Dictionary
	var required := [
		"link_id",
		"guardian_id",
		"ward_id",
		"interval",
		"provenance",
	]
	if not _has_exact_keys(data, required):
		return null
	if not data["link_id"] is String:
		return null
	if not data["guardian_id"] is String:
		return null
	if not data["ward_id"] is String:
		return null
	if not data["provenance"] is String:
		return null

	var guardian_id := StringName(data["guardian_id"])
	var ward_id := StringName(data["ward_id"])
	if not identities.contains(guardian_id):
		return null
	if not identities.contains(ward_id):
		return null

	var interval := _decode_interval(data["interval"])
	if interval == null:
		return null

	var link := GuardianshipLink.new()
	link.link_id = StringName(data["link_id"])
	link.guardian_id = guardian_id
	link.ward_id = ward_id
	link.interval = interval
	link.provenance = StringName(data["provenance"])
	return link if link.validate().is_empty() else null

func _decode_union(
	value: Variant,
	identities: CharacterIdentityIndex,
) -> UnionLink:
	if not value is Dictionary:
		return null
	var data := value as Dictionary
	var required := [
		"link_id",
		"first_id",
		"second_id",
		"interval",
		"union_type",
		"provenance",
	]
	if not _has_exact_keys(data, required):
		return null
	for key: String in [
		"link_id",
		"first_id",
		"second_id",
		"union_type",
		"provenance",
	]:
		if not data[key] is String:
			return null

	var first_id := StringName(data["first_id"])
	var second_id := StringName(data["second_id"])
	if not identities.contains(first_id):
		return null
	if not identities.contains(second_id):
		return null

	var pair := CharacterPair.create(first_id, second_id)
	var interval := _decode_interval(data["interval"])
	if pair == null or interval == null:
		return null

	var link := UnionLink.new()
	link.link_id = StringName(data["link_id"])
	link.pair = pair
	link.interval = interval
	link.union_type = StringName(data["union_type"])
	link.provenance = StringName(data["provenance"])
	return link if link.validate().is_empty() else null
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `_decode_interval()`, `_decode_guardianship()`, `_decode_union()` utilisées dans « 18.5 Intervalles, tutelles et unions ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `_decode_interval(value: Variant) -> LogicalInterval`, `_decode_guardianship(value: Variant, identities: CharacterIdentityIndex,) -> GuardianshipLink`, `_decode_union(value: Variant, identities: CharacterIdentityIndex,) -> UnionLink`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `data := value as Dictionary`, `interval := LogicalInterval.new(`, `data := value as Dictionary`, `required := [`, `guardian_id := StringName(data["guardian_id"])` et 10 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les boucles `for` parcourent les collections de façon explicite ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application ; les doublons et références déjà connues sont détectés ; les clés ou types inattendus sont refusés au lieu d’être convertis silencieusement.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

### 18.6 Historique et utilitaires

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
func _decode_history(value: Variant) -> FamilyHistoryRecord:
	if not value is Dictionary:
		return null
	var data := value as Dictionary
	var required := [
		"sequence",
		"event_type",
		"link_id",
		"tick",
		"provenance",
	]
	if not _has_exact_keys(data, required):
		return null
	if not data["sequence"] is int:
		return null
	if not data["event_type"] is String:
		return null
	if not data["link_id"] is String:
		return null
	if not data["tick"] is int:
		return null
	if not data["provenance"] is String:
		return null

	var record := FamilyHistoryRecord.new()
	record.sequence = data["sequence"]
	record.event_type = StringName(data["event_type"])
	record.link_id = StringName(data["link_id"])
	record.tick = data["tick"]
	record.provenance = StringName(data["provenance"])
	return record if record.validate() else null

func _has_exact_keys(data: Dictionary, required: Array) -> bool:
	if data.size() != required.size():
		return false
	for key: String in required:
		if not data.has(key):
			return false
	return true

func _types_match(
	data: Dictionary,
	expected: Dictionary,
) -> bool:
	for key: String in expected:
		if typeof(data[key]) != expected[key]:
			return false
	return true
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `_decode_history()`, `_has_exact_keys()`, `_types_match()` utilisées dans « 18.6 Historique et utilitaires ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `_decode_history(value: Variant) -> FamilyHistoryRecord`, `_has_exact_keys(data: Dictionary, required: Array) -> bool`, `_types_match(data: Dictionary, expected: Dictionary,) -> bool`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `data := value as Dictionary`, `required := [`, `record := FamilyHistoryRecord.new()`. Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les boucles `for` parcourent les collections de façon explicite ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application ; les doublons et références déjà connues sont détectés ; les parcours ou historiques restent bornés ; les clés ou types inattendus sont refusés au lieu d’être convertis silencieusement.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

## 19. Construction atomique du graphe candidat

> **[LECTURE] Extrait GDScript — Ne pas saisir directement.**

```gdscript
func decode_snapshot(
	payload: Variant,
	identities: CharacterIdentityIndex,
) -> Dictionary:
	if not payload is Dictionary:
		return {}
	var data := payload as Dictionary
	var root_keys := [
		"format_version",
		"parent_links",
		"guardianships",
		"unions",
		"history",
	]
	if not _has_exact_keys(data, root_keys):
		return {}
	if not data["format_version"] is int:
		return {}
	if data["format_version"] != FORMAT_VERSION:
		return {}
	for key: String in [
		"parent_links",
		"guardianships",
		"unions",
		"history",
	]:
		if not data[key] is Array:
			return {}

	if data["parent_links"].size() > MAX_PARENT_LINKS:
		return {}
	if data["guardianships"].size() > MAX_GUARDIANSHIPS:
		return {}
	if data["unions"].size() > MAX_UNIONS:
		return {}
	if data["history"].size() > MAX_HISTORY_RECORDS:
		return {}

	var candidate := FamilyGraph.new()
	for raw_link: Variant in data["parent_links"]:
		var parent_link := _decode_parent_link(raw_link, identities)
		if parent_link == null:
			return {}
		if candidate.add_parent_link(parent_link) != OK:
			return {}

	for raw_link: Variant in data["guardianships"]:
		var guardianship := _decode_guardianship(raw_link, identities)
		if guardianship == null:
			return {}
		if candidate.add_guardianship(guardianship) != OK:
			return {}

	for raw_link: Variant in data["unions"]:
		var union_link := _decode_union(raw_link, identities)
		if union_link == null:
			return {}
		if candidate.add_union(union_link) != OK:
			return {}

	var records: Array[FamilyHistoryRecord] = []
	for raw_record: Variant in data["history"]:
		var record := _decode_history(raw_record)
		if record == null:
			return {}
		records.append(record)

	var history := FamilyEventLog.new()
	if history.restore(records) != OK:
		return {}

	return {
		"graph": candidate,
		"history": history,
	}
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `decode_snapshot()` utilisées dans « 19. Construction atomique du graphe candidat ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `decode_snapshot(payload: Variant, identities: CharacterIdentityIndex,) -> Dictionary`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `data := payload as Dictionary`, `root_keys := [`, `candidate := FamilyGraph.new()`, `parent_link := _decode_parent_link(raw_link, identities)`, `guardianship := _decode_guardianship(raw_link, identities)` et 4 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les boucles `for` parcourent les collections de façon explicite ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** ajoute des éléments à une collection ou à un historique borné. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** un auto-lien entre une identité et elle-même est refusé ; les parcours ou historiques restent bornés ; la donnée candidate est préparée entièrement avant toute mutation de l’état actif ; les clés ou types inattendus sont refusés au lieu d’être convertis silencieusement.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

La fonction ne modifie jamais le graphe actif. Tout échec retourne un dictionnaire vide et abandonne le candidat.

## 20. Section de sauvegarde

> **[VSC] Visual Studio Code — Créer : `src/features/families/infrastructure/family_save_section.gd`.**

```gdscript
class_name FamilySaveSection
extends SaveSection

const SECTION_ID := &"families"

var _graph: FamilyGraph
var _history: FamilyEventLog
var _codec: FamilySnapshotCodec
var _identities: CharacterIdentityIndex
var _prepared_graph: FamilyGraph
var _prepared_history: FamilyEventLog

func _init(
	graph: FamilyGraph,
	history: FamilyEventLog,
	codec: FamilySnapshotCodec,
	identities: CharacterIdentityIndex,
) -> void:
	_graph = graph
	_history = history
	_codec = codec
	_identities = identities

func get_section_id() -> StringName:
	return SECTION_ID

func capture() -> Dictionary:
	if (
		_graph == null
		or _history == null
		or _codec == null
	):
		push_error("FamilySaveSection non configurée.")
		return {}
	return _codec.encode_graph(_graph, _history)

func prepare_apply(payload: Variant) -> Error:
	_prepared_graph = null
	_prepared_history = null
	if _codec == null or _identities == null:
		return ERR_UNCONFIGURED

	var decoded := _codec.decode_snapshot(payload, _identities)
	if decoded.is_empty():
		return ERR_INVALID_DATA

	var candidate := decoded["graph"] as FamilyGraph
	var candidate_history := decoded["history"] as FamilyEventLog
	if candidate == null or candidate_history == null:
		return ERR_INVALID_DATA

	var validator := FamilyGraphValidator.new()
	if not validator.validate(candidate, _identities).is_empty():
		return ERR_INVALID_DATA

	_prepared_graph = candidate
	_prepared_history = candidate_history
	return OK

func apply_prepared() -> Error:
	if _prepared_graph == null or _prepared_history == null:
		return ERR_UNCONFIGURED

	var graph_result := _graph.replace_all_from(_prepared_graph)
	if graph_result != OK:
		return graph_result

	var history_result := _history.restore(
		_prepared_history.snapshot(),
	)
	if history_result != OK:
		return history_result

	_prepared_graph = null
	_prepared_history = null
	return OK

func cancel_prepared() -> void:
	_prepared_graph = null
	_prepared_history = null
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à définir la classe `FamilySaveSection`, dérivée de `SaveSection`.
- **Emplacement :** il appartient à `src/features/families/infrastructure/family_save_section.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `_init(graph: FamilyGraph, history: FamilyEventLog, codec: FamilySnapshotCodec, identities: CharacterIdentityIndex,) -> void`, `get_section_id(aucun paramètre) -> StringName`, `capture(aucun paramètre) -> Dictionary`, `prepare_apply(payload: Variant) -> Error`, `apply_prepared(aucun paramètre) -> Error`, `cancel_prepared(aucun paramètre) -> void`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare constantes `SECTION_ID := &"families"` ; état `_graph: FamilyGraph`, `_history: FamilyEventLog`, `_codec: FamilySnapshotCodec`, `_identities: CharacterIdentityIndex`, `_prepared_graph: FamilyGraph` et 7 autre(s). Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** remplace l’état autoritaire seulement après validation du candidat ; enregistre une erreur exploitable par l’appelant ; retourne un code `Error` explicite. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les objets sont validés avant leur insertion ou leur application ; les parcours ou historiques restent bornés ; la donnée candidate est préparée entièrement avant toute mutation de l’état actif.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

`replace_all_from()` reconstruit les index secondaires à partir des liens du candidat. La section propage son retour `Error` et ne considère la préparation terminée qu’après remplacement du graphe et restauration de l’historique.

## 21. Personnages décédés, absents ou archivés

Un personnage décédé peut rester :

- parent ;
- enfant ;
- ancien partenaire ;
- tuteur historique ;
- ancêtre d’une lignée.

Le lien ne dépend pas de la présence en scène.

L’archivage physique d’une identité doit respecter une politique de référence :

- conserver un enregistrement minimal tant qu’un lien la référence ;
- refuser sa suppression définitive ;
- ou migrer explicitement les références vers une identité d’archive.

Le chapitre ne supprime jamais automatiquement une identité référencée.

## 22. Démonstration pédagogique

### 22.1 Scène

> **[APP] Godot — Créer `scenes/learning/ch16_family_demo.tscn`.**

> **[SORTIE] Arbre attendu dans le dock Scene — Ne pas saisir.**

```text
Ch16FamilyDemo (Node)
├── Output (RichTextLabel)
├── AddBiologicalParent (Button)
├── AddAdoptiveParent (Button)
├── TryCycle (Button)
├── ShowAncestors (Button)
└── SaveRoundTrip (Button)
```

### 22.2 Script de démonstration

> **[VSC] Visual Studio Code — Créer : `scenes/learning/ch16_family_demo.gd`.**

```gdscript
extends Node

@onready var output: RichTextLabel = %Output

var graph := FamilyGraph.new()

func _ready() -> void:
	output.text = "Chapitre 16 prêt."

func demonstrate_cycle_refusal(
	grandparent_id: StringName,
	parent_id: StringName,
	child_id: StringName,
) -> void:
	_add_parent(grandparent_id, parent_id, 10)
	_add_parent(parent_id, child_id, 20)
	var result := _add_parent(child_id, grandparent_id, 30)
	output.append_text("\nCycle refusé : %s" % (result == ERR_CYCLIC_LINK))

func _add_parent(
	parent_id: StringName,
	child_id: StringName,
	tick: int,
) -> Error:
	var link := ParentChildLink.new(
		FamilyLinkId.create_random(),
		parent_id,
		child_id,
		FamilyLinkKind.Value.BIOLOGICAL_PARENT,
		tick,
		&"demo",
	)
	return graph.add_parent_link(link)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `_ready()`, `demonstrate_cycle_refusal()`, `_add_parent()` utilisées dans « ce passage ».
- **Emplacement :** il appartient à `scenes/learning/ch16_family_demo.gd`. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `_ready(aucun paramètre) -> void`, `demonstrate_cycle_refusal(grandparent_id: StringName, parent_id: StringName, child_id: StringName,) -> void`, `_add_parent(parent_id: StringName, child_id: StringName, tick: int,) -> Error`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** le bloc déclare état `output: RichTextLabel = %Output`, `graph := FamilyGraph.new()`, `result := _add_parent(child_id, grandparent_id, 30)`, `link := ParentChildLink.new(`. Les champs préfixés par `_` sont internes et ne doivent pas devenir une API implicite.
- **Déroulement :** les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** la structure hiérarchique ne peut pas introduire de cycle d’ascendance.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

La démonstration n’est pas un test runtime tant que la scène n’a pas été matérialisée et exécutée.

## 23. Parcours Solo

Le parcours Solo privilégie :

- un `FamilyGraph` en mémoire ;
- un seul index logique de personnages ;
- une section de sauvegarde JSON ;
- un historique borné à 256 événements ;
- des requêtes à profondeur maximale 32 ;
- aucune création de toutes les paires possibles ;
- aucune base ou service réseau spécifique au système familial.

Cette architecture suffit pour un projet individuel ou une simulation de taille modérée.

## 24. Parcours Studio

Le parcours Studio ajoute :

- une ADR sur les types de liens et politiques culturelles ;
- des fixtures de grands graphes ;
- des tests de propriété sur l’absence de cycles ;
- des migrations de format versionnées ;
- une revue narrative des provenances ;
- une politique d’archivage des identités ;
- des métriques de profondeur et de coût des requêtes ;
- une responsabilité claire pour les règles de succession ;
- une revue d’accessibilité et de sensibilité du vocabulaire familial ;
- une validation de compatibilité des sauvegardes anciennes.

Le Studio ne remplace pas le graphe par un « manager global » accessible partout.

## 25. Complexité et budgets

Pour `V` personnages et `E` filiations :

- parents et enfants directs utilisent les index et coûtent approximativement le degré local ;
- ancêtres et descendants coûtent `O(V + E)` dans le sous-graphe parcouru ;
- la détection de cycle utilise un parcours borné ;
- la fratrie dépend du nombre de parents puis de leurs enfants ;
- les unions sont indexées par paire canonique.

Budgets de référence :

| Élément | Limite pédagogique |
|---|---:|
| profondeur de requête | 32 |
| nœuds d’un parcours | 4 096 |
| historique familial | 256 |
| liens par personnage avant alerte | 128 |
| format de snapshot | version 1 |

Ces limites doivent être mesurées et ajustées sur le projet matérialisé.

## 26. Tests à préparer

### 26.1 Tests unitaires

- `FamilyLinkId` accepte uniquement son format canonique ;
- une paire d’union est identique quel que soit l’ordre ;
- un auto-lien est refusé ;
- un doublon de filiation est refusé ;
- un cycle direct est refusé ;
- un cycle long est refusé ;
- parents et enfants directs sont exacts ;
- la fratrie exclut le personnage lui-même ;
- les ancêtres retournent la distance minimale ;
- une tutelle terminée avant son début est refusée ;
- deux tutelles identiques chevauchantes sont refusées ;
- deux unions identiques chevauchantes sont refusées ;
- une identité inconnue est refusée au décodage ;
- une clé JSON inconnue est refusée ;
- la génération n’apparaît pas dans le snapshot ;
- `prepare_apply()` n’altère pas le graphe actif.

### 26.2 Tests d’intégration

- création de trois générations ;
- sauvegarde puis chargement ;
- conservation des liens d’un personnage déchargé ;
- conservation des liens d’un personnage décédé ;
- annulation d’un chargement invalide ;
- restauration coordonnée avec la section des personnages ;
- migration d’un ancien format ;
- reconstruction des index secondaires.

### 26.3 Tests de charge

- lignée de profondeur 32 ;
- arbre large de plusieurs milliers de personnages ;
- requêtes répétées d’ancêtres ;
- import d’un snapshot proche de la limite ;
- tentative de cycle sur un grand graphe ;
- historique au-delà de 256 entrées.

## 27. Critères d’acceptation

Le chapitre est accepté au niveau documentaire et statique si :

- [ ] la famille reste hors de `CharacterRuntimeState` ;
- [ ] les identités utilisent `CharacterId` ;
- [ ] filiation, tutelle et union sont distinctes ;
- [ ] la filiation est orientée ;
- [ ] l’union utilise une paire canonique ;
- [ ] auto-liens et doublons sont refusés ;
- [ ] les cycles d’ascendance sont refusés ;
- [ ] les parcours sont bornés ;
- [ ] fratries et générations sont dérivées ;
- [ ] les intervalles temporels sont validés ;
- [ ] les personnages absents ou décédés restent référencés ;
- [ ] les événements sont typés ;
- [ ] le snapshot exclut caches et index ;
- [ ] la restauration prépare un candidat complet ;
- [ ] les frontières avec les chapitres futurs sont explicites ;
- [ ] les modes Solo et Studio sont présents.

## 28. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 28.1 Utiliser le nom affiché comme identité

**Symptôme ou risque :** un renommage casse les liens.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
parents_by_name["Aster"] = ["Mira"]
```

**Correction :** utiliser les `CharacterId`.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
parents_by_child[child_id] = [parent_id]
```

**Différence :** l’identité reste stable et indépendante de l’affichage.

### 28.2 Stocker la famille dans le nœud actif

**Symptôme ou risque :** les liens disparaissent lors du déchargement.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
player_node.children_ids.append(child_id)
```

**Correction :** conserver les liens dans `FamilyGraph`.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
family_graph.add_parent_link(link)
```

**Différence :** le graphe survit à la scène.

### 28.3 Déduire la filiation depuis l’affinité

**Symptôme ou risque :** une valeur sociale devient une autorité familiale.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if affinity > 80:
	is_parent = true
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à illustrer concrètement la règle présentée dans « 28.3 Déduire la filiation depuis l’affinité ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** ce bloc ne déclare pas de fonction publique ; ses données sont consommées par le code qui l’instancie ou le décode. Les types visibles dans les déclarations constituent néanmoins le contrat à respecter.
- **État et dépendances :** aucune donnée mutable durable n’est déclarée ici ; l’extrait dépend surtout des objets reçus en paramètres et des contrats cités dans les annotations de type.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les identifiants et types reçus doivent déjà être valides, et le résultat ne doit pas exposer directement une collection interne mutable.
- **Pourquoi cet exemple est fautif :** il montre volontairement une violation de contrat. Il ne doit pas être copié tel quel ; la section corrigée qui suit rétablit la validation, le bornage ou la séparation des responsabilités manquante.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

**Correction :** créer une commande familiale explicite.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
family_service.add_parent_link(command)
```

**Différence :** la structure et la perception restent séparées.

### 28.4 Persister la fratrie

**Symptôme ou risque :** les données deviennent contradictoires après ajout d’un parent.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
snapshot["siblings"] = sibling_ids
```

**Correction :** calculer la fratrie depuis les parents partagés.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var sibling_ids := graph.get_siblings(character_id)
```

**Différence :** une seule autorité est persistée.

### 28.5 Persister un numéro de génération absolu

**Symptôme ou risque :** plusieurs lignées produisent des numéros incompatibles.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
character.generation = 4
```

**Correction :** calculer une distance relative à un ancêtre.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var distance := graph.get_generation_distance(founder_id, character_id)
```

**Différence :** la valeur dépend explicitement du point de référence.

### 28.6 Oublier la détection de cycle

**Symptôme ou risque :** un personnage devient son propre ancêtre.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
_parent_links[link.link_id] = link
```

**Correction :** rechercher si le parent est déjà descendant de l’enfant.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if _would_create_ancestry_cycle(link.parent_id, link.child_id):
	return ERR_CYCLIC_LINK
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à illustrer concrètement la règle présentée dans « 28.6 Oublier la détection de cycle ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** ce bloc ne déclare pas de fonction publique ; ses données sont consommées par le code qui l’instancie ou le décode. Les types visibles dans les déclarations constituent néanmoins le contrat à respecter.
- **État et dépendances :** aucune donnée mutable durable n’est déclarée ici ; l’extrait dépend surtout des objets reçus en paramètres et des contrats cités dans les annotations de type.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** retourne un code `Error` explicite. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** la structure hiérarchique ne peut pas introduire de cycle d’ascendance.
- **Pourquoi cet exemple est fautif :** il montre volontairement une violation de contrat. Il ne doit pas être copié tel quel ; la section corrigée qui suit rétablit la validation, le bornage ou la séparation des responsabilités manquante.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

**Différence :** le graphe reste acyclique.

### 28.7 Traiter un dépassement de budget comme une absence de cycle

**Symptôme ou risque :** un grand graphe contourne la sécurité structurelle.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if visited.size() > limit:
	return false
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à illustrer concrètement la règle présentée dans « 28.7 Traiter un dépassement de budget comme une absence de cycle ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** ce bloc ne déclare pas de fonction publique ; ses données sont consommées par le code qui l’instancie ou le décode. Les types visibles dans les déclarations constituent néanmoins le contrat à respecter.
- **État et dépendances :** aucune donnée mutable durable n’est déclarée ici ; l’extrait dépend surtout des objets reçus en paramètres et des contrats cités dans les annotations de type.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les identifiants et types reçus doivent déjà être valides, et le résultat ne doit pas exposer directement une collection interne mutable.
- **Pourquoi cet exemple est fautif :** il montre volontairement une violation de contrat. Il ne doit pas être copié tel quel ; la section corrigée qui suit rétablit la validation, le bornage ou la séparation des responsabilités manquante.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

**Correction :** refuser conservativement.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if visited.size() >= MAX_TRAVERSAL_NODES:
	return true
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à illustrer concrètement la règle présentée dans « 28.7 Traiter un dépassement de budget comme une absence de cycle ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** ce bloc ne déclare pas de fonction publique ; ses données sont consommées par le code qui l’instancie ou le décode. Les types visibles dans les déclarations constituent néanmoins le contrat à respecter.
- **État et dépendances :** aucune donnée mutable durable n’est déclarée ici ; l’extrait dépend surtout des objets reçus en paramètres et des contrats cités dans les annotations de type.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les parcours ou historiques restent bornés.
- **Pourquoi la correction fonctionne :** elle déplace la décision vers le bon contrat, valide les données avant mutation et rend l’échec observable par l’appelant.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

**Différence :** l’incertitude n’autorise pas la mutation.

### 28.8 Orienter une union

**Symptôme ou risque :** `{A, B}` et `{B, A}` deviennent deux unions.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var key := "%s>%s" % [left_id, right_id]
```

**Correction :** canoniser la paire.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var key := CharacterPair.create(left_id, right_id).key()
```

**Différence :** l’ordre des partenaires ne change pas l’identité métier.

### 28.9 Utiliser l’heure système

**Symptôme ou risque :** les sauvegardes et simulations ne sont pas reproductibles.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
started_at_tick = Time.get_unix_time_from_system()
```

**Correction :** utiliser le tick logique.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
started_at_tick = simulation_clock.current_tick
```

**Différence :** l’ordre dépend de la simulation.

### 28.10 Accepter un intervalle inversé

**Symptôme ou risque :** un lien se termine avant de commencer.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
interval.ended_at_tick = 10
```

**Correction :** passer par `close_at()`.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var result := interval.close_at(current_tick)
```

**Différence :** l’invariant temporel est contrôlé.

### 28.11 Valider uniquement contre les personnages actifs

**Symptôme ou risque :** un parent déchargé devient « inconnu ».

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if not active_registry.has(parent_id):
	return ERR_DOES_NOT_EXIST
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à illustrer concrètement la règle présentée dans « 28.11 Valider uniquement contre les personnages actifs ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** ce bloc ne déclare pas de fonction publique ; ses données sont consommées par le code qui l’instancie ou le décode. Les types visibles dans les déclarations constituent néanmoins le contrat à respecter.
- **État et dépendances :** aucune donnée mutable durable n’est déclarée ici ; l’extrait dépend surtout des objets reçus en paramètres et des contrats cités dans les annotations de type.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** retourne un code `Error` explicite. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les doublons et références déjà connues sont détectés.
- **Pourquoi cet exemple est fautif :** il montre volontairement une violation de contrat. Il ne doit pas être copié tel quel ; la section corrigée qui suit rétablit la validation, le bornage ou la séparation des responsabilités manquante.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

**Correction :** utiliser l’index logique.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if not identity_index.contains(parent_id):
	return ERR_DOES_NOT_EXIST
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à illustrer concrètement la règle présentée dans « 28.11 Valider uniquement contre les personnages actifs ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** ce bloc ne déclare pas de fonction publique ; ses données sont consommées par le code qui l’instancie ou le décode. Les types visibles dans les déclarations constituent néanmoins le contrat à respecter.
- **État et dépendances :** aucune donnée mutable durable n’est déclarée ici ; l’extrait dépend surtout des objets reçus en paramètres et des contrats cités dans les annotations de type.
- **Déroulement :** les conditions `if` refusent les entrées invalides avant la mutation ; les retours anticipés réduisent le risque de modifier un état après une erreur.
- **Effets de bord :** retourne un code `Error` explicite. Ces effets ne doivent survenir qu’après le succès des validations précédentes.
- **Invariants protégés :** les doublons et références déjà connues sont détectés.
- **Pourquoi la correction fonctionne :** elle déplace la décision vers le bon contrat, valide les données avant mutation et rend l’échec observable par l’appelant.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

**Différence :** la présence en scène n’est pas l’existence métier.

### 28.12 Retourner une collection interne mutable

**Symptôme ou risque :** l’appelant désynchronise les index.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
return _children_by_parent[parent_id]
```

**Correction :** construire un nouveau tableau.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
return result
```

**Différence :** le graphe garde le contrôle de ses structures.

### 28.13 Charger directement dans le graphe actif

**Symptôme ou risque :** une erreur tardive laisse une restauration partielle.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
for raw_link in payload.parent_links:
	_graph.add_parent_link(decode(raw_link))
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à illustrer concrètement la règle présentée dans « 28.13 Charger directement dans le graphe actif ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** ce bloc ne déclare pas de fonction publique ; ses données sont consommées par le code qui l’instancie ou le décode. Les types visibles dans les déclarations constituent néanmoins le contrat à respecter.
- **État et dépendances :** aucune donnée mutable durable n’est déclarée ici ; l’extrait dépend surtout des objets reçus en paramètres et des contrats cités dans les annotations de type.
- **Déroulement :** les boucles `for` parcourent les collections de façon explicite.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les identifiants et types reçus doivent déjà être valides, et le résultat ne doit pas exposer directement une collection interne mutable.
- **Pourquoi cet exemple est fautif :** il montre volontairement une violation de contrat. Il ne doit pas être copié tel quel ; la section corrigée qui suit rétablit la validation, le bornage ou la séparation des responsabilités manquante.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

**Correction :** construire un candidat complet.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var candidate := codec.decode_graph(payload, identities)
```

**Différence :** aucun état actif n’est modifié avant succès global.

### 28.14 Sauvegarder les index secondaires

**Symptôme ou risque :** liens et index divergent.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
snapshot["parents_by_child"] = _parents_by_child
```

**Correction :** persister uniquement les liens autoritaires.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
snapshot["parent_links"] = encoded_links
```

**Différence :** les index sont reconstruits.

### 28.15 Laisser une sortie IA créer un lien directement

**Symptôme ou risque :** un texte généré contourne les invariants.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
family_graph.add_parent_link(ai_response)
```

**Correction :** mapper vers une commande validée et soumise à l’autorité du jeu.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var result := family_service.add_parent_link(validated_command)
```

**Différence :** l’IA ne devient pas autorité métier.

### 28.16 Mélanger succession et famille

**Symptôme ou risque :** le graphe impose prématurément des règles politiques.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
func add_child(child_id):
	next_ruler_id = child_id
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc sert à implémenter les opérations `add_child()` utilisées dans « 28.16 Mélanger succession et famille ».
- **Emplacement :** il appartient à le fichier indiqué juste avant le bloc. Le chemin est une partie du contrat pédagogique : déplacer ce code dans une autre couche peut créer un couplage non prévu.
- **Entrées et retours :** `add_child(child_id) -> Variant implicite`. Les paramètres typés limitent les appels ambigus ; le type placé après `->` décrit ce que l’appelant doit traiter.
- **État et dépendances :** aucune donnée mutable durable n’est déclarée ici ; l’extrait dépend surtout des objets reçus en paramètres et des contrats cités dans les annotations de type.
- **Déroulement :** les instructions sont exécutées dans l’ordre, de la construction des données vers leur validation puis leur exposition.
- **Effets de bord :** l’extrait est principalement déclaratif ou calculatoire ; il ne doit pas modifier un nœud actif, une ressource partagée ou une collection appartenant à l’appelant sans copie explicite.
- **Invariants protégés :** les identifiants et types reçus doivent déjà être valides, et le résultat ne doit pas exposer directement une collection interne mutable.
- **Pourquoi cet exemple est fautif :** il montre volontairement une violation de contrat. Il ne doit pas être copié tel quel ; la section corrigée qui suit rétablit la validation, le bornage ou la séparation des responsabilités manquante.
- **Résultat attendu :** l’appelant obtient un résultat typé ou un code d’erreur explicite, sans état partiellement appliqué. La vérification minimale consiste à tester un cas valide, un cas limite et un cas refusé, puis à confirmer que l’état actif reste inchangé après l’échec.

**Correction :** publier un événement familial consommable par le chapitre 23.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
family_link_added.emit(event)
```

**Différence :** la famille décrit le lien ; la politique décide de la succession.

## 29. Sources techniques

- [Godot 4.7 — Documentation officielle](https://docs.godotengine.org/en/4.7/)
- [Godot 4.7 — Référence GDScript](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/gdscript_basics.html)
- [Godot 4.7 — Typage statique GDScript](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/static_typing.html)
- [Godot 4.7 — Bonnes pratiques des classes](https://docs.godotengine.org/en/4.7/tutorials/best_practices/what_are_godot_classes.html)
- [Godot 4.7 — RefCounted](https://docs.godotengine.org/en/4.7/classes/class_refcounted.html)
- [Godot 4.7 — Dictionary](https://docs.godotengine.org/en/4.7/classes/class_dictionary.html)
- [Godot 4.7 — Array](https://docs.godotengine.org/en/4.7/classes/class_array.html)
- [Godot 4.7 — StringName](https://docs.godotengine.org/en/4.7/classes/class_stringname.html)
- [Godot 4.7 — JSON](https://docs.godotengine.org/en/4.7/classes/class_json.html)
- [Godot 4.7 — Variant](https://docs.godotengine.org/en/4.7/classes/class_variant.html)
- [Godot 4.7 — Object et signaux](https://docs.godotengine.org/en/4.7/classes/class_object.html)
- [Godot 4.7 — Error](https://docs.godotengine.org/en/4.7/classes/class_%40globalscope.html#enum-globalscope-error)
- [Godot 4.7 — Crypto](https://docs.godotengine.org/en/4.7/classes/class_crypto.html)
- [Godot 4.7 — FileAccess](https://docs.godotengine.org/en/4.7/classes/class_fileaccess.html)
- [RFC 8259 — The JavaScript Object Notation Data Interchange Format](https://www.rfc-editor.org/rfc/rfc8259)

## 30. Limites de l’audit statique

À ce stade :

- les scripts n’ont pas été analysés par le parseur Godot ;
- les classes du chapitre ne sont pas matérialisées dans le Starter Kit ;
- les signaux ne sont pas exécutés ;
- la détection de cycles n’est pas testée sur un grand graphe réel ;
- les limites de 4 096 nœuds et profondeur 32 ne sont pas mesurées ;
- la restauration coordonnée avec les personnages n’est pas exécutée ;
- les migrations de format ne sont pas implémentées ;
- les politiques culturelles d’union ne sont pas définies ;
- le multijoueur n’est pas traité ;
- aucun PDF intermédiaire n’est produit.

## 31. Résumé opérationnel

Le système familial de `Project Asteria` repose sur les décisions suivantes :

1. la famille est séparée du personnage et des relations sociales ;
2. la filiation est dirigée parent vers enfant ;
3. les unions utilisent une paire canonique ;
4. les tutelles et unions portent des intervalles logiques ;
5. les cycles d’ascendance sont refusés avant mutation ;
6. les parcours sont bornés ;
7. fratries, ancêtres et générations sont calculés ;
8. les personnages absents, décédés ou archivés restent référencés ;
9. les événements sont typés ;
10. le snapshot persiste uniquement les liens autoritaires ;
11. un graphe candidat complet est validé avant application ;
12. succession, politique et narration restent hors périmètre.
