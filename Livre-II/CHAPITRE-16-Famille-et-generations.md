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

- **Rôle :** ce bloc définit le contrat `FamilyLinkId` et l’appuie sur `RefCounted`.
- **Emplacement :** place ce code dans `src/features/families/domain/family_link_id.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `create_random(aucun paramètre) -> StringName` est une méthode statique qui valide puis ajoute ou applique une mutation métier ; `is_valid(value: StringName) -> bool` est une méthode statique qui vérifie les préconditions et signale toute donnée invalide. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** constantes `PREFIX := "fam_"`, `HEX_LENGTH := 32` ; variables `bytes := Crypto.new().generate_random_bytes(16)`, `text := String(value)`, `suffix := text.substr(PREFIX.length())`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** mémorise une erreur consultable. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Résultat attendu et vérification :** obtenir `true` uniquement lorsque toutes les conditions décrites sont satisfaites et `false` pour les cas limites. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc définit le contrat `FamilyLinkKind` et l’appuie sur `RefCounted`.
- **Emplacement :** place ce code dans `src/features/families/domain/family_link_kind.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `is_parent_kind(value: Value) -> bool` est une méthode statique qui répond à une question sans modifier l’état ; `is_known(value: int) -> bool` est une méthode statique qui répond à une question sans modifier l’état. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** énumérations `Value = BIOLOGICAL_PARENT, ADOPTIVE_PARENT, GUARDIANSHIP, UNION`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc définit le contrat `LogicalInterval` et l’appuie sur `RefCounted`.
- **Emplacement :** place ce code dans `src/features/families/domain/logical_interval.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `_init(start_tick: int, end_tick: int = OPEN_END) -> void` est une méthode qui initialise l’objet et copie les arguments dans son état interne ; `is_valid(aucun paramètre) -> bool` est une méthode qui vérifie les préconditions et signale toute donnée invalide ; `is_active_at(tick: int) -> bool` est une méthode qui répond à une question sans modifier l’état ; `close_at(tick: int) -> Error` est une méthode qui termine ou retire un élément en refusant les transitions incohérentes ; `duplicate_value(aucun paramètre) -> LogicalInterval` est une méthode qui produit une copie défensive indépendante de l’original. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** constantes `OPEN_END := -1` ; variables `started_at_tick: int`, `ended_at_tick: int`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** modifie un état temporel ou une révision ; crée une copie défensive. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les transitions utilisent des ticks logiques cohérents ; les lectures ne doivent pas exposer directement un objet interne mutable.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc définit le contrat `ParentChildLink` et l’appuie sur `RefCounted`.
- **Emplacement :** place ce code dans `src/features/families/domain/parent_child_link.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `_init(new_link_id: StringName, new_parent_id: StringName, new_child_id: StringName, new_kind: FamilyLinkKind.Value, new_tick: int, new_provenance: StringName,) -> void` est une méthode qui initialise l’objet et copie les arguments dans son état interne ; `validate(aucun paramètre) -> PackedStringArray` est une méthode qui vérifie les préconditions et signale toute donnée invalide ; `duplicate_value(aucun paramètre) -> ParentChildLink` est une méthode qui produit une copie défensive indépendante de l’original. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `link_id: StringName`, `parent_id: StringName`, `child_id: StringName`, `kind: FamilyLinkKind.Value`, `established_at_tick: int`, `provenance: StringName` et 1 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique ; crée une copie défensive. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** une identité ne peut pas former un lien avec elle-même ; chaque référence doit correspondre à une identité logique connue, même hors scène ; les lectures ne doivent pas exposer directement un objet interne mutable.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc définit le contrat `GuardianshipLink` et l’appuie sur `RefCounted`.
- **Emplacement :** place ce code dans `src/features/families/domain/guardianship_link.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `validate(aucun paramètre) -> PackedStringArray` est une méthode qui vérifie les préconditions et signale toute donnée invalide ; `duplicate_value(aucun paramètre) -> GuardianshipLink` est une méthode qui produit une copie défensive indépendante de l’original. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `link_id: StringName`, `guardian_id: StringName`, `ward_id: StringName`, `interval: LogicalInterval`, `provenance: StringName`, `errors := PackedStringArray()` et 1 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique ; crée une copie défensive. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** chaque référence doit correspondre à une identité logique connue, même hors scène ; les lectures ne doivent pas exposer directement un objet interne mutable.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc définit le contrat `CharacterPair` et l’appuie sur `RefCounted`.
- **Emplacement :** place ce code dans `src/features/families/domain/character_pair.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `create(left_id: StringName, right_id: StringName) -> CharacterPair` est une méthode statique qui encapsule l’opération métier indiquée par son nom ; `key(aucun paramètre) -> StringName` est une méthode qui encapsule l’opération métier indiquée par son nom. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `first_id: StringName`, `second_id: StringName`, `pair := CharacterPair.new()`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** chaque référence doit correspondre à une identité logique connue, même hors scène.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc définit le contrat `UnionLink` et l’appuie sur `RefCounted`.
- **Emplacement :** place ce code dans `src/features/families/domain/union_link.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `validate(aucun paramètre) -> PackedStringArray` est une méthode qui vérifie les préconditions et signale toute donnée invalide ; `duplicate_value(aucun paramètre) -> UnionLink` est une méthode qui produit une copie défensive indépendante de l’original. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `link_id: StringName`, `pair: CharacterPair`, `interval: LogicalInterval`, `union_type: StringName`, `provenance: StringName`, `errors := PackedStringArray()` et 1 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique ; crée une copie défensive. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les lectures ne doivent pas exposer directement un objet interne mutable.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc illustre la règle technique de « 10. Contrat de l’index logique des personnages ».
- **Emplacement :** place ce code dans `src/features/characters/application/character_identity_index.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** chaque référence doit correspondre à une identité logique connue, même hors scène.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc définit le contrat `FamilyGraph` et l’appuie sur `RefCounted`.
- **Emplacement :** place ce code dans `src/features/families/domain/family_graph.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** constantes `MAX_TRAVERSAL_NODES := 4096` ; variables `_parent_links: Dictionary[StringName, ParentChildLink] = {}`, `_guardian_links: Dictionary[StringName, GuardianshipLink] = {}`, `_union_links: Dictionary[StringName, UnionLink] = {}`, `_parents_by_child: Dictionary[StringName, Array] = {}`, `_children_by_parent: Dictionary[StringName, Array] = {}`, `_unions_by_pair: Dictionary[StringName, Array] = {}`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les parcours et historiques sont bornés ; les valeurs numériques restent dans leurs bornes métier.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 11.2 Ajouter une filiation ».
- **Emplacement :** place ce code dans `src/features/families/domain/family_graph.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `add_parent_link(link: ParentChildLink) -> Error` est une méthode qui valide puis ajoute ou applique une mutation métier. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** crée une copie défensive. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** aucun cycle d’ascendance ne peut être introduit ; les lectures ne doivent pas exposer directement un objet interne mutable.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 11.3 Cycle d’ascendance ».
- **Emplacement :** place ce code dans `src/features/families/domain/family_graph.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `_would_create_ancestry_cycle(parent_id: StringName, child_id: StringName,) -> bool` est une méthode qui encapsule l’opération métier indiquée par son nom. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `pending: Array[StringName] = [child_id]`, `visited: Dictionary[StringName, bool] = {}`, `current: StringName = pending.pop_back()`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; la boucle `while` poursuit un parcours dont le budget doit rester borné ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique ; mémorise une erreur consultable. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** une identité ne peut pas former un lien avec elle-même ; les parcours et historiques sont bornés ; aucun cycle d’ascendance ne peut être introduit ; les valeurs numériques restent dans leurs bornes métier.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 11.4 Helpers d’index ».
- **Emplacement :** place ce code dans `src/features/families/domain/family_graph.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `_append_index(index: Dictionary[StringName, Array], character_id: StringName, link_id: StringName,) -> void` est une méthode qui encapsule l’opération métier indiquée par son nom ; `_has_parent_edge(parent_id: StringName, child_id: StringName,) -> bool` est une méthode qui encapsule l’opération métier indiquée par son nom ; `get_parent_links(aucun paramètre) -> Array[ParentChildLink]` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes ; `get_guardianship_links(aucun paramètre) -> Array[GuardianshipLink]` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes ; `get_union_links(aucun paramètre) -> Array[UnionLink]` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `ids: Array = index.get(character_id, [])`, `link := _parent_links.get(link_id) as ParentChildLink`, `result: Array[ParentChildLink] = []`, `result: Array[GuardianshipLink] = []`, `result: Array[UnionLink] = []`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique ; crée une copie défensive. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les lectures ne doivent pas exposer directement un objet interne mutable.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc illustre volontairement une normalisation incorrecte qui détruit l’ordre métier.
- **Emplacement :** place ce code dans `src/features/families/domain/family_graph.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `get_parents(child_id: StringName) -> Array[StringName]` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes ; `get_children(parent_id: StringName) -> Array[StringName]` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `result: Array[StringName] = []`, `link := _parent_links.get(link_id) as ParentChildLink`, `result: Array[StringName] = []`, `link := _parent_links.get(link_id) as ParentChildLink`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** l’ordre des identifiants conserve la direction de la relation.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** constater que deux relations opposées produisent la même paire triée, ce qui prouve la perte d’orientation ; ce bloc ne doit pas être intégré au projet. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc illustre volontairement une normalisation incorrecte qui détruit l’ordre métier.
- **Emplacement :** place ce code dans `src/features/families/domain/family_graph.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `get_siblings(character_id: StringName) -> Array[StringName]` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `siblings: Dictionary[StringName, bool] = {}`, `result: Array[StringName] = []`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les clés et types externes sont contrôlés strictement ; l’ordre des identifiants conserve la direction de la relation.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** constater que deux relations opposées produisent la même paire triée, ce qui prouve la perte d’orientation ; ce bloc ne doit pas être intégré au projet. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 12.3 Ancêtres bornés ».
- **Emplacement :** place ce code dans `src/features/families/domain/family_graph.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `get_ancestors(character_id: StringName, max_depth: int = 32,) -> Dictionary[StringName, int]` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `distances: Dictionary[StringName, int] = {}`, `pending: Array[Dictionary] = [`, `visited_nodes := 0`, `entry: Dictionary = pending.pop_front()`, `current: StringName = entry["id"]`, `depth: int = entry["depth"]` et 1 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; la boucle `while` poursuit un parcours dont le budget doit rester borné ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique ; mémorise une erreur consultable. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les parcours et historiques sont bornés ; aucun cycle d’ascendance ne peut être introduit ; les valeurs numériques restent dans leurs bornes métier.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 12.4 Descendants bornés ».
- **Emplacement :** place ce code dans `src/features/families/domain/family_graph.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `get_descendants(character_id: StringName, max_depth: int = 32,) -> Dictionary[StringName, int]` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `distances: Dictionary[StringName, int] = {}`, `pending: Array[Dictionary] = [`, `visited_nodes := 0`, `entry: Dictionary = pending.pop_front()`, `current: StringName = entry["id"]`, `depth: int = entry["depth"]` et 1 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; la boucle `while` poursuit un parcours dont le budget doit rester borné ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique ; mémorise une erreur consultable. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les parcours et historiques sont bornés ; aucun cycle d’ascendance ne peut être introduit ; les valeurs numériques restent dans leurs bornes métier.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 13.2 Distance générationnelle ».
- **Emplacement :** place ce code dans `src/features/families/domain/family_graph.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `get_generation_distance(ancestor_id: StringName, descendant_id: StringName, max_depth: int = 32,) -> int` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `descendants := get_descendants(ancestor_id, max_depth)`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les parcours et historiques sont bornés ; aucun cycle d’ascendance ne peut être introduit ; les valeurs numériques restent dans leurs bornes métier.
- **Résultat attendu et vérification :** observer le comportement décrit par la section sans modifier de donnée autoritaire non concernée. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 14.1 Ajouter une tutelle ».
- **Emplacement :** place ce code dans `src/features/families/domain/family_graph.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `add_guardianship(link: GuardianshipLink) -> Error` est une méthode qui valide puis ajoute ou applique une mutation métier. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** crée une copie défensive. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les lectures ne doivent pas exposer directement un objet interne mutable.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 14.2 Ajouter une union ».
- **Emplacement :** place ce code dans `src/features/families/domain/family_graph.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `add_union(link: UnionLink) -> Error` est une méthode qui valide puis ajoute ou applique une mutation métier. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `pair_key := link.pair.key()`, `existing := _union_links.get(existing_id) as UnionLink`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** crée une copie défensive. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les lectures ne doivent pas exposer directement un objet interne mutable.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 14.3 Chevauchement d’intervalles ».
- **Emplacement :** place ce code dans `src/features/families/domain/family_graph.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `_intervals_overlap(left: LogicalInterval, right: LogicalInterval,) -> bool` est une méthode qui encapsule l’opération métier indiquée par son nom ; `replace_all_from(source: FamilyGraph) -> Error` est une méthode qui remplace l’état autoritaire à partir d’un candidat déjà validé. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `left_end := (`, `right_end := (`, `candidate := FamilyGraph.new()`, `parent_result := candidate.add_parent_link(link)`, `guardian_result := candidate.add_guardianship(link)`, `union_result := candidate.add_union(link)`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** remplace l’état autoritaire ; modifie un état temporel ou une révision. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les transitions utilisent des ticks logiques cohérents ; un candidat complet est validé avant mutation de l’état actif.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc définit le contrat `AddParentLinkCommand` et l’appuie sur `RefCounted`.
- **Emplacement :** place ce code dans `src/features/families/application/add_parent_link_command.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `validate(aucun paramètre) -> PackedStringArray` est une méthode qui vérifie les préconditions et signale toute donnée invalide. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `parent_id: StringName`, `child_id: StringName`, `kind: FamilyLinkKind.Value`, `tick: int`, `provenance: StringName`, `errors := PackedStringArray()`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** une identité ne peut pas former un lien avec elle-même ; chaque référence doit correspondre à une identité logique connue, même hors scène.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc définit le contrat `FamilyLinkAddedEvent` et l’appuie sur `RefCounted`.
- **Emplacement :** place ce code dans `src/features/families/application/family_link_added_event.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** variables `link_id: StringName`, `kind: FamilyLinkKind.Value`, `first_character_id: StringName`, `second_character_id: StringName`, `tick: int`, `provenance: StringName`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc définit le contrat `FamilyGraphService` et l’appuie sur `RefCounted`.
- **Emplacement :** place ce code dans `src/features/families/application/family_graph_service.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `_init(graph: FamilyGraph, identities: CharacterIdentityIndex,) -> void` est une méthode qui initialise l’objet et copie les arguments dans son état interne ; `add_parent_link(command: AddParentLinkCommand) -> Error` est une méthode qui valide puis ajoute ou applique une mutation métier. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `_graph: FamilyGraph`, `_identities: CharacterIdentityIndex`, `link := ParentChildLink.new(`, `result := _graph.add_parent_link(link)`, `event := FamilyLinkAddedEvent.new()` ; signaux `family_link_added(event: FamilyLinkAddedEvent)`, `family_link_closed(`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** émet un événement observable après succès. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc définit le contrat `FamilyHistoryRecord` et l’appuie sur `RefCounted`.
- **Emplacement :** place ce code dans `src/features/families/domain/family_history_record.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `validate(aucun paramètre) -> bool` est une méthode qui vérifie les préconditions et signale toute donnée invalide ; `duplicate_value(aucun paramètre) -> FamilyHistoryRecord` est une méthode qui produit une copie défensive indépendante de l’original. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `sequence: int`, `event_type: StringName`, `link_id: StringName`, `tick: int`, `provenance: StringName`, `copy := FamilyHistoryRecord.new()`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** crée une copie défensive. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les lectures ne doivent pas exposer directement un objet interne mutable.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc définit le contrat `FamilyEventLog` et l’appuie sur `RefCounted`.
- **Emplacement :** place ce code dans `src/features/families/domain/family_history_record.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `append(event_type: StringName, link_id: StringName, tick: int, provenance: StringName,) -> Error` est une méthode qui encapsule l’opération métier indiquée par son nom ; `snapshot(aucun paramètre) -> Array[FamilyHistoryRecord]` est une méthode qui encapsule l’opération métier indiquée par son nom ; `restore(records: Array[FamilyHistoryRecord]) -> Error` est une méthode qui remplace l’état autoritaire à partir d’un candidat déjà validé. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** constantes `MAX_RECORDS := 256` ; variables `_records: Array[FamilyHistoryRecord] = []`, `_next_sequence := 0`, `record := FamilyHistoryRecord.new()`, `result: Array[FamilyHistoryRecord] = []`, `candidate: Array[FamilyHistoryRecord] = []`, `previous_sequence := -1`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; la boucle `while` poursuit un parcours dont le budget doit rester borné ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique ; modifie un état temporel ou une révision ; crée une copie défensive. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les parcours et historiques sont bornés ; un candidat complet est validé avant mutation de l’état actif ; les lectures ne doivent pas exposer directement un objet interne mutable ; les valeurs numériques restent dans leurs bornes métier.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc définit le contrat `FamilyGraphValidator` et l’appuie sur `RefCounted`.
- **Emplacement :** place ce code dans `src/features/families/application/family_graph_validator.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `validate(graph: FamilyGraph, identities: CharacterIdentityIndex,) -> PackedStringArray` est une méthode qui vérifie les préconditions et signale toute donnée invalide. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `errors := PackedStringArray()`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Résultat attendu et vérification :** pouvoir instancier ou appeler ce contrat depuis la couche prévue, avec un état valide et des lectures défensives. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc montre la forme JSON attendue par « 18.1 Structure JSON ».
- **Emplacement :** place ce code dans `src/features/families/application/family_graph_validator.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc définit le contrat `FamilySnapshotCodec` et l’appuie sur `RefCounted`.
- **Emplacement :** place ce code dans `src/features/families/application/family_graph_validator.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** constantes `FORMAT_VERSION := 1`, `MAX_PARENT_LINKS := 8192`, `MAX_GUARDIANSHIPS := 4096`, `MAX_UNIONS := 4096`, `MAX_HISTORY_RECORDS := 256`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les parcours et historiques sont bornés ; les valeurs numériques restent dans leurs bornes métier.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 18.3 Encodeurs ».
- **Emplacement :** place ce code dans `src/features/families/infrastructure/family_snapshot_codec.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `encode_graph(graph: FamilyGraph, history: FamilyEventLog,) -> Dictionary` est une méthode qui convertit l’objet vers une représentation de transport ou de stockage ; `_encode_parent_link(link: ParentChildLink) -> Dictionary` est une méthode qui encapsule l’opération métier indiquée par son nom ; `_encode_interval(interval: LogicalInterval) -> Dictionary` est une méthode qui encapsule l’opération métier indiquée par son nom ; `_encode_guardianship(link: GuardianshipLink) -> Dictionary` est une méthode qui encapsule l’opération métier indiquée par son nom ; `_encode_union(link: UnionLink) -> Dictionary` est une méthode qui encapsule l’opération métier indiquée par son nom ; `_encode_history(record: FamilyHistoryRecord) -> Dictionary` est une méthode qui encapsule l’opération métier indiquée par son nom. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `parent_links: Array[Dictionary] = []`, `guardianships: Array[Dictionary] = []`, `unions: Array[Dictionary] = []`, `history_records: Array[Dictionary] = []`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les transitions utilisent des ticks logiques cohérents.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 18.4 Décodage strict d’une filiation ».
- **Emplacement :** place ce code dans `src/features/families/infrastructure/family_snapshot_codec.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `_decode_parent_link(value: Variant, identities: CharacterIdentityIndex,) -> ParentChildLink` est une méthode qui encapsule l’opération métier indiquée par son nom. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `data := value as Dictionary`, `required := [`, `parent_id := StringName(data["parent_id"])`, `child_id := StringName(data["child_id"])`, `kind_value: int = data["kind"]`, `link := ParentChildLink.new(`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les clés et types externes sont contrôlés strictement.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 18.5 Intervalles, tutelles et unions ».
- **Emplacement :** place ce code dans `src/features/families/infrastructure/family_snapshot_codec.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `_decode_interval(value: Variant) -> LogicalInterval` est une méthode qui encapsule l’opération métier indiquée par son nom ; `_decode_guardianship(value: Variant, identities: CharacterIdentityIndex,) -> GuardianshipLink` est une méthode qui encapsule l’opération métier indiquée par son nom ; `_decode_union(value: Variant, identities: CharacterIdentityIndex,) -> UnionLink` est une méthode qui encapsule l’opération métier indiquée par son nom. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `data := value as Dictionary`, `interval := LogicalInterval.new(`, `data := value as Dictionary`, `required := [`, `guardian_id := StringName(data["guardian_id"])`, `ward_id := StringName(data["ward_id"])` et 9 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les transitions utilisent des ticks logiques cohérents.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 18.6 Historique et utilitaires ».
- **Emplacement :** place ce code dans `src/features/families/infrastructure/family_snapshot_codec.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `_decode_history(value: Variant) -> FamilyHistoryRecord` est une méthode qui encapsule l’opération métier indiquée par son nom ; `_has_exact_keys(data: Dictionary, required: Array) -> bool` est une méthode qui encapsule l’opération métier indiquée par son nom ; `_types_match(data: Dictionary, expected: Dictionary,) -> bool` est une méthode qui encapsule l’opération métier indiquée par son nom. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `data := value as Dictionary`, `required := [`, `record := FamilyHistoryRecord.new()`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 19. Construction atomique du graphe candidat ».
- **Emplacement :** place ce code dans `src/features/families/infrastructure/family_snapshot_codec.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `decode_snapshot(payload: Variant, identities: CharacterIdentityIndex,) -> Dictionary` est une méthode qui reconstruit une valeur typée après validation de la représentation externe. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `data := payload as Dictionary`, `root_keys := [`, `candidate := FamilyGraph.new()`, `parent_link := _decode_parent_link(raw_link, identities)`, `guardianship := _decode_guardianship(raw_link, identities)`, `union_link := _decode_union(raw_link, identities)` et 3 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les parcours et historiques sont bornés ; un candidat complet est validé avant mutation de l’état actif ; les valeurs numériques restent dans leurs bornes métier.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc définit le contrat `FamilySaveSection` et l’appuie sur `SaveSection`.
- **Emplacement :** place ce code dans `src/features/families/infrastructure/family_save_section.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `_init(graph: FamilyGraph, history: FamilyEventLog, codec: FamilySnapshotCodec, identities: CharacterIdentityIndex,) -> void` est une méthode qui initialise l’objet et copie les arguments dans son état interne ; `get_section_id(aucun paramètre) -> StringName` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes ; `capture(aucun paramètre) -> Dictionary` est une méthode qui encapsule l’opération métier indiquée par son nom ; `prepare_apply(payload: Variant) -> Error` est une méthode qui encapsule l’opération métier indiquée par son nom ; `apply_prepared(aucun paramètre) -> Error` est une méthode qui valide puis ajoute ou applique une mutation métier ; `cancel_prepared(aucun paramètre) -> void` est une méthode qui encapsule l’opération métier indiquée par son nom. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** constantes `SECTION_ID := &"families"` ; variables `_graph: FamilyGraph`, `_history: FamilyEventLog`, `_codec: FamilySnapshotCodec`, `_identities: CharacterIdentityIndex`, `_prepared_graph: FamilyGraph`, `_prepared_history: FamilyEventLog` et 6 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** remplace l’état autoritaire ; mémorise une erreur consultable. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** un candidat complet est validé avant mutation de l’état actif.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 22.2 Script de démonstration ».
- **Emplacement :** place ce code dans `scenes/learning/ch16_family_demo.gd`. Ce fichier appartient à la couche indiquée par le chemin ; le déplacer vers une scène ou un état de personnage rendrait les responsabilités moins nettes.
- **Fonctions, paramètres et retours :** `_ready(aucun paramètre) -> void` est une méthode qui encapsule l’opération métier indiquée par son nom ; `demonstrate_cycle_refusal(grandparent_id: StringName, parent_id: StringName, child_id: StringName,) -> void` est une méthode qui encapsule l’opération métier indiquée par son nom ; `_add_parent(parent_id: StringName, child_id: StringName, tick: int,) -> Error` est une méthode qui encapsule l’opération métier indiquée par son nom. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** variables `output: RichTextLabel = %Output`, `graph := FamilyGraph.new()`, `result := _add_parent(child_id, grandparent_id, 30)`, `link := ParentChildLink.new(`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** aucun cycle d’ascendance ne peut être introduit.
- **Résultat attendu et vérification :** obtenir `OK` pour le cas valide et un code `Error` documenté pour chaque refus, sans mutation partielle. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.1 Utiliser le nom affiché comme identité ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Correction :** utiliser les `CharacterId`.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
parents_by_child[child_id] = [parent_id]
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.1 Utiliser le nom affiché comme identité ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Différence :** l’identité reste stable et indépendante de l’affichage.

### 28.2 Stocker la famille dans le nœud actif

**Symptôme ou risque :** les liens disparaissent lors du déchargement.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
player_node.children_ids.append(child_id)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.2 Stocker la famille dans le nœud actif ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Correction :** conserver les liens dans `FamilyGraph`.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
family_graph.add_parent_link(link)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.2 Stocker la famille dans le nœud actif ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


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

- **Rôle :** ce bloc illustre la règle technique de « 28.3 Déduire la filiation depuis l’affinité ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

**Correction :** créer une commande familiale explicite.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
family_service.add_parent_link(command)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.3 Déduire la filiation depuis l’affinité ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Différence :** la structure et la perception restent séparées.

### 28.4 Persister la fratrie

**Symptôme ou risque :** les données deviennent contradictoires après ajout d’un parent.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
snapshot["siblings"] = sibling_ids
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.4 Persister la fratrie ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Correction :** calculer la fratrie depuis les parents partagés.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var sibling_ids := graph.get_siblings(character_id)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.4 Persister la fratrie ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** variables `sibling_ids := graph.get_siblings(character_id)`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Différence :** une seule autorité est persistée.

### 28.5 Persister un numéro de génération absolu

**Symptôme ou risque :** plusieurs lignées produisent des numéros incompatibles.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
character.generation = 4
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.5 Persister un numéro de génération absolu ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Correction :** calculer une distance relative à un ancêtre.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var distance := graph.get_generation_distance(founder_id, character_id)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.5 Persister un numéro de génération absolu ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** variables `distance := graph.get_generation_distance(founder_id, character_id)`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Différence :** la valeur dépend explicitement du point de référence.

### 28.6 Oublier la détection de cycle

**Symptôme ou risque :** un personnage devient son propre ancêtre.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
_parent_links[link.link_id] = link
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.6 Oublier la détection de cycle ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** aucun cycle d’ascendance ne peut être introduit.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Correction :** rechercher si le parent est déjà descendant de l’enfant.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if _would_create_ancestry_cycle(link.parent_id, link.child_id):
	return ERR_CYCLIC_LINK
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.6 Oublier la détection de cycle ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** aucun cycle d’ascendance ne peut être introduit.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

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

- **Rôle :** ce bloc illustre la règle technique de « 28.7 Traiter un dépassement de budget comme une absence de cycle ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** aucun cycle d’ascendance ne peut être introduit.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

**Correction :** refuser conservativement.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if visited.size() >= MAX_TRAVERSAL_NODES:
	return true
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.7 Traiter un dépassement de budget comme une absence de cycle ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les parcours et historiques sont bornés ; aucun cycle d’ascendance ne peut être introduit ; les valeurs numériques restent dans leurs bornes métier.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

**Différence :** l’incertitude n’autorise pas la mutation.

### 28.8 Orienter une union

**Symptôme ou risque :** `{A, B}` et `{B, A}` deviennent deux unions.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
var key := "%s>%s" % [left_id, right_id]
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.8 Orienter une union ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** variables `key := "%s>%s" % [left_id, right_id]`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Correction :** canoniser la paire.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var key := CharacterPair.create(left_id, right_id).key()
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.8 Orienter une union ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** variables `key := CharacterPair.create(left_id, right_id).key()`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Différence :** l’ordre des partenaires ne change pas l’identité métier.

### 28.9 Utiliser l’heure système

**Symptôme ou risque :** les sauvegardes et simulations ne sont pas reproductibles.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
started_at_tick = Time.get_unix_time_from_system()
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.9 Utiliser l’heure système ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les transitions utilisent des ticks logiques cohérents.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Correction :** utiliser le tick logique.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
started_at_tick = simulation_clock.current_tick
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.9 Utiliser l’heure système ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les transitions utilisent des ticks logiques cohérents.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Différence :** l’ordre dépend de la simulation.

### 28.10 Accepter un intervalle inversé

**Symptôme ou risque :** un lien se termine avant de commencer.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
interval.ended_at_tick = 10
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.10 Accepter un intervalle inversé ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** modifie un état temporel ou une révision. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les transitions utilisent des ticks logiques cohérents.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Correction :** passer par `close_at()`.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var result := interval.close_at(current_tick)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.10 Accepter un intervalle inversé ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** variables `result := interval.close_at(current_tick)`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


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

- **Rôle :** ce bloc illustre la règle technique de « 28.11 Valider uniquement contre les personnages actifs ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

**Correction :** utiliser l’index logique.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
if not identity_index.contains(parent_id):
	return ERR_DOES_NOT_EXIST
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.11 Valider uniquement contre les personnages actifs ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** chaque référence doit correspondre à une identité logique connue, même hors scène.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

**Différence :** la présence en scène n’est pas l’existence métier.

### 28.12 Retourner une collection interne mutable

**Symptôme ou risque :** l’appelant désynchronise les index.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
return _children_by_parent[parent_id]
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.12 Retourner une collection interne mutable ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Correction :** construire un nouveau tableau.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
return result
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.12 Retourner une collection interne mutable ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


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

- **Rôle :** ce bloc illustre la règle technique de « 28.13 Charger directement dans le graphe actif ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les boucles `for` parcourent explicitement les collections. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

**Correction :** construire un candidat complet.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var candidate := codec.decode_graph(payload, identities)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.13 Charger directement dans le graphe actif ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** variables `candidate := codec.decode_graph(payload, identities)`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** un candidat complet est validé avant mutation de l’état actif.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Différence :** aucun état actif n’est modifié avant succès global.

### 28.14 Sauvegarder les index secondaires

**Symptôme ou risque :** liens et index divergent.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
snapshot["parents_by_child"] = _parents_by_child
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.14 Sauvegarder les index secondaires ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Correction :** persister uniquement les liens autoritaires.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
snapshot["parent_links"] = encoded_links
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.14 Sauvegarder les index secondaires ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Différence :** les index sont reconstruits.

### 28.15 Laisser une sortie IA créer un lien directement

**Symptôme ou risque :** un texte généré contourne les invariants.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
family_graph.add_parent_link(ai_response)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.15 Laisser une sortie IA créer un lien directement ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


**Correction :** mapper vers une commande validée et soumise à l’autorité du jeu.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
var result := family_service.add_parent_link(validated_command)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.15 Laisser une sortie IA créer un lien directement ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** variables `result := family_service.add_parent_link(validated_command)`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


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

- **Rôle :** ce bloc regroupe les opérations nécessaires à « 28.16 Mélanger succession et famille ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Fonctions, paramètres et retours :** `add_child(child_id) -> Variant implicite` est une méthode qui valide puis ajoute ou applique une mutation métier. Les annotations après `:` typent les paramètres ; l’annotation après `->` impose le résultat que l’appelant doit gérer.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

**Correction :** publier un événement familial consommable par le chapitre 23.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de référence.**

```gdscript
family_link_added.emit(event)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc illustre la règle technique de « 28.16 Mélanger succession et famille ».
- **Emplacement :** ce bloc est un exemple à lire dans le contexte pédagogique indiqué juste avant le bloc ; il ne faut pas créer un fichier supplémentaire tant qu’aucun chemin `[VSC]` n’est fourni.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** émet un événement observable après succès. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Pourquoi cet exemple est fautif :** il est volontairement présenté comme contre-exemple. La ligne problématique supprime une information métier, contourne une validation ou écrit dans la mauvaise couche ; elle ne doit pas être copiée dans le projet.
- **Résultat attendu et vérification :** identifier précisément l’invariant violé, puis vérifier que l’exemple corrigé refuse ou encadre le même cas. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.


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
