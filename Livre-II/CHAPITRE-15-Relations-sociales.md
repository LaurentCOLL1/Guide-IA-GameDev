---
title: "Livre II — Chapitre 15 : Relations sociales"
id: "DOC-L2-CH15"
status: "reviewed"
version: "1.2.0"
lang: "fr-FR"
book: "Livre II"
chapter: 15
last-verified: "2026-07-20"
audit-status: "complete"
audit-date: "2026-07-20"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-15.md"
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

# Relations sociales

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH15`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Niveau de raisonnement conseillé :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-15.md`.
> **Explications de code :** contextualisées bloc par bloc selon la porte QA Q1.1, sans répéter le chemin ou les rappels généraux de syntaxe.
> **Convention de lecture :** la consigne `[VSC]` placée avant un bloc porte déjà son chemin canonique ; l’explication ne le répète pas. Les annotations GDScript `:` et `->` sont présentées au [chapitre 2](CHAPITRE-02-Fondamentaux-de-GDScript.md) et ne sont rappelées ici que lorsqu’un choix de type ou de retour demande une attention particulière.

## 1. Rôle du chapitre

Le chapitre 14 a défini le personnage comme une identité stable, une définition de conception, un état runtime, une représentation éventuelle dans la scène et un snapshot persistant.

Le présent chapitre ajoute un système social sans transformer `CharacterRuntimeState` en objet universel.

Une relation sociale doit continuer d’exister lorsque :

- aucun des deux personnages n’est chargé dans la scène ;
- un personnage change de nom affiché ;
- une zone est déchargée ;
- un contrôleur humain devient autonome ;
- une sauvegarde est fermée puis rechargée ;
- l’interface sociale n’est pas ouverte ;
- le service IA local est indisponible.

La règle centrale est :

> **Une relation sociale appartient aux données du monde, pas aux nœuds visibles.**

À la fin du chapitre, le lecteur doit savoir :

- distinguer une relation dirigée d’une vue mutuelle ;
- identifier une relation par deux identifiants de personnages ;
- représenter plusieurs axes sociaux bornés ;
- appliquer un changement avec cause, provenance et horodatage logique ;
- conserver un historique borné ;
- émettre des événements typés ;
- interroger les voisins sociaux sans parcourir les scènes ;
- persister le système dans une section indépendante ;
- refuser les références invalides avant toute mutation ;
- garder les liens familiaux, factions, réputation et narration dans leurs chapitres propres.

## 2. Prérequis

Le chapitre réutilise :

- `CharacterId` du chapitre 14 ;
- les identifiants stables du chapitre 7 ;
- les événements typés du chapitre 5 ;
- la sauvegarde préparée avant application du chapitre 9 ;
- les limites et principes d’échec fermé du chapitre 13.

Le lecteur doit comprendre :

- `RefCounted` ;
- `Resource` ;
- `Dictionary` et `Array` typés ;
- les signaux ;
- les codes `Error` ;
- les snapshots JSON versionnés.

## 3. Périmètre et frontières

Ce chapitre définit :

- l’identité d’une relation dirigée ;
- quatre axes sociaux : affinité, confiance, respect et peur ;
- les changements sociaux causaux ;
- un historique récent borné ;
- un dépôt en mémoire indépendant des nœuds ;
- les requêtes de voisinage ;
- les vues mutuelles ;
- les événements typés ;
- la persistance et la restauration atomique.

Il ne définit pas encore :

- les liens de parenté du chapitre 16 ;
- les décisions des agents autonomes du chapitre 17 ;
- l’hostilité tactique et les dégâts du chapitre 18 ;
- les compétences sociales du chapitre 19 ;
- les factions et la justice du chapitre 23 ;
- la réputation des objets du chapitre 20 ;
- les quêtes et conséquences narratives du chapitre 25 ;
- le multijoueur du Livre IV.

> **Frontière essentielle :** une relation sociale influence potentiellement une décision future, mais elle ne décide pas elle-même d’une action.

## 4. Modèle conceptuel

### 4.1 Une relation est dirigée

La perception d’Aster envers Brann n’est pas nécessairement la perception de Brann envers Aster.

> **[LECTURE] Deux relations distinctes — Ne pas saisir.**

```text
Aster → Brann : confiance 70, respect 20
Brann → Aster : confiance 15, respect 65
```

Le système conserve donc deux états :

> **[LECTURE] Deux clés orientées — Ne pas saisir.**

```text
(source = Aster, cible = Brann)
(source = Brann, cible = Aster)
```

### 4.2 Une vue mutuelle est calculée

Une amitié réciproque peut être calculée à partir des deux directions.

Le chapitre ne stocke pas un booléen `is_friend` indépendant, car il pourrait contredire les axes.

> **[LECTURE] Exemple de vue mutuelle — Ne pas saisir.**

```text
affinité mutuelle = minimum(affinité A→B, affinité B→A)
confiance mutuelle = minimum(confiance A→B, confiance B→A)
```

Le minimum est conservateur : une relation mutuelle forte exige que les deux directions soient fortes.

### 4.3 Les axes ne sont pas des vérités absolues

Les valeurs représentent l’état du modèle de jeu, pas une mesure psychologique universelle.

Les bornes retenues sont :

| Axe | Minimum | Maximum | Interprétation |
|---|---:|---:|---|
| affinité | `-100` | `100` | aversion à attachement |
| confiance | `-100` | `100` | suspicion à confiance |
| respect | `-100` | `100` | mépris à respect |
| peur | `0` | `100` | absence de peur à peur maximale |

Ces axes restent indépendants :

- un personnage peut respecter un rival qu’il n’apprécie pas ;
- il peut craindre une personne en qui il a confiance ;
- une forte affinité ne garantit pas une confiance élevée.

## 5. Architecture retenue

> **[LECTURE] Architecture du système social — Ne pas saisir.**

```text
CharacterId
    ↓
SocialRelationshipKey
    ↓
SocialRelationshipState
    ├── SocialAxes
    └── historique borné de SocialChangeRecord
             ↓
SocialRelationshipRepository
             ↓
SocialRelationshipService
    ├── commandes validées
    ├── événements typés
    └── requêtes de voisinage
             ↓
SocialRelationshipSaveSection
```

Répartition des responsabilités :

| Élément | Responsabilité |
|---|---|
| `SocialRelationshipKey` | identifier `source → cible` |
| `SocialAxes` | contenir les valeurs courantes bornées |
| `SocialChangeCause` | identifier une cause stable |
| `SocialChangeRecord` | expliquer un changement passé |
| `SocialRelationshipState` | porter axes, révision et historique |
| `SocialRelationshipRepository` | conserver et indexer les états |
| `SocialRelationshipService` | valider et appliquer les changements |
| `SocialRelationshipQuery` | produire voisins et vues mutuelles |
| `SocialRelationshipSaveSection` | sérialiser et restaurer atomiquement |

## 6. Identifier une relation dirigée

### 6.1 Clé de relation

> **[VSC] Visual Studio Code — Créer : `res://src/features/social/domain/social_relationship_key.gd`.**

```gdscript
class_name SocialRelationshipKey
extends RefCounted

var source_id: StringName
var target_id: StringName

func _init(
	p_source_id: StringName,
	p_target_id: StringName,
) -> void:
	source_id = p_source_id
	target_id = p_target_id

func validate() -> Error:
	if source_id.is_empty() or target_id.is_empty():
		return ERR_INVALID_DATA

	if source_id == target_id:
		return ERR_INVALID_DATA

	if not CharacterId.is_valid(source_id):
		return ERR_INVALID_DATA

	if not CharacterId.is_valid(target_id):
		return ERR_INVALID_DATA

	return OK

func to_storage_key() -> String:
	return "%s->%s" % [String(source_id), String(target_id)]
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc définit le contrat `SocialRelationshipKey` et l’appuie sur `RefCounted`.
- **Fonctions, paramètres et retours :** `_init(p_source_id: StringName, p_target_id: StringName,) -> void` est une méthode qui initialise l’objet et copie les arguments dans son état interne ; `validate(aucun paramètre) -> Error` est une méthode qui vérifie les préconditions et signale toute donnée invalide ; `to_storage_key(aucun paramètre) -> String` est une méthode qui convertit l’objet vers une représentation de transport ou de stockage.
- **Données et types :** variables `source_id: StringName`, `target_id: StringName`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** une identité ne peut pas former un lien avec elle-même ; chaque référence doit correspondre à une identité logique connue, même hors scène.
- **Résultat attendu et vérification :** obtenir `OK` pour le cas valide et un code `Error` documenté pour chaque refus, sans mutation partielle. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

Explication :

- `source_id` est le personnage qui porte la perception ;
- `target_id` est le personnage perçu ;
- une relation avec soi-même est refusée ;
- `to_storage_key()` fabrique une clé technique déterministe ;
- la flèche rend l’orientation visible ;
- la clé technique n’est jamais affichée au joueur.

### 6.2 Pourquoi ne pas trier les identifiants

Trier les identifiants détruirait l’orientation.

> **[LECTURE] Mauvaise normalisation — Ne pas utiliser.**

```gdscript
var ids := [source_id, target_id]
ids.sort()
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** l’extrait viole la règle métier rappelée dans « 6.2 Pourquoi ne pas trier les identifiants ».

Cette approche convient uniquement à une paire réellement non orientée. Elle ne convient pas à une perception sociale.

## 7. Représenter les axes sociaux

> **[VSC] Visual Studio Code — Créer : `res://src/features/social/domain/social_axes.gd`.**

```gdscript
class_name SocialAxes
extends RefCounted

const MIN_SIGNED := -100
const MAX_SIGNED := 100
const MIN_FEAR := 0
const MAX_FEAR := 100

var affinity: int = 0
var trust: int = 0
var respect: int = 0
var fear: int = 0

func duplicate_axes() -> SocialAxes:
	var copy := SocialAxes.new()
	copy.affinity = affinity
	copy.trust = trust
	copy.respect = respect
	copy.fear = fear
	return copy

func validate() -> Error:
	if affinity < MIN_SIGNED or affinity > MAX_SIGNED:
		return ERR_INVALID_DATA
	if trust < MIN_SIGNED or trust > MAX_SIGNED:
		return ERR_INVALID_DATA
	if respect < MIN_SIGNED or respect > MAX_SIGNED:
		return ERR_INVALID_DATA
	if fear < MIN_FEAR or fear > MAX_FEAR:
		return ERR_INVALID_DATA
	return OK

func apply_delta(
	affinity_delta: int,
	trust_delta: int,
	respect_delta: int,
	fear_delta: int,
) -> void:
	affinity = clampi(
		affinity + affinity_delta,
		MIN_SIGNED,
		MAX_SIGNED,
	)
	trust = clampi(
		trust + trust_delta,
		MIN_SIGNED,
		MAX_SIGNED,
	)
	respect = clampi(
		respect + respect_delta,
		MIN_SIGNED,
		MAX_SIGNED,
	)
	fear = clampi(
		fear + fear_delta,
		MIN_FEAR,
		MAX_FEAR,
	)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc définit le contrat `SocialAxes` et l’appuie sur `RefCounted`.
- **Fonctions, paramètres et retours :** `duplicate_axes(aucun paramètre) -> SocialAxes` est une méthode qui produit une copie défensive indépendante de l’original ; `validate(aucun paramètre) -> Error` est une méthode qui vérifie les préconditions et signale toute donnée invalide ; `apply_delta(affinity_delta: int, trust_delta: int, respect_delta: int, fear_delta: int,) -> void` est une méthode qui valide puis ajoute ou applique une mutation métier.
- **Données et types :** constantes `MIN_SIGNED := -100`, `MAX_SIGNED := 100`, `MIN_FEAR := 0`, `MAX_FEAR := 100` ; variables `affinity: int = 0`, `trust: int = 0`, `respect: int = 0`, `fear: int = 0`, `copy := SocialAxes.new()`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** crée une copie défensive. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les parcours et historiques sont bornés ; les lectures ne doivent pas exposer directement un objet interne mutable ; les valeurs numériques restent dans leurs bornes métier.
- **Résultat attendu et vérification :** obtenir `OK` pour le cas valide et un code `Error` documenté pour chaque refus, sans mutation partielle. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

`duplicate_axes()` évite de partager le même objet mutable entre un état courant, un événement et une vue d’interface.

`apply_delta()` borne chaque résultat après addition. Un changement de `500` ne crée donc pas une valeur hors contrat.

## 8. Décrire la cause d’un changement

### 8.1 Identifiant de cause

Une cause est un identifiant stable, par exemple :

> **[LECTURE] Exemples de causes — Ne pas saisir.**

```text
social.cause.conversation.kind
social.cause.promise.kept
social.cause.promise.broken
social.cause.rescue
social.cause.public_insult
```

Une cause ne contient pas le texte affiché. La localisation reste séparée.

### 8.2 Type de cause

> **[VSC] Visual Studio Code — Créer : `res://src/features/social/domain/social_change_cause.gd`.**

```gdscript
class_name SocialChangeCause
extends RefCounted

var cause_id: StringName
var source_system: StringName
var context_id: StringName

func _init(
	p_cause_id: StringName,
	p_source_system: StringName,
	p_context_id: StringName = &"",
) -> void:
	cause_id = p_cause_id
	source_system = p_source_system
	context_id = p_context_id

func validate() -> Error:
	if not StableId.is_valid(cause_id):
		return ERR_INVALID_DATA

	if not StableId.is_valid(source_system):
		return ERR_INVALID_DATA

	if not context_id.is_empty() and not StableId.is_valid(context_id):
		return ERR_INVALID_DATA

	return OK
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc définit le contrat `SocialChangeCause` et l’appuie sur `RefCounted`.
- **Fonctions, paramètres et retours :** `_init(p_cause_id: StringName, p_source_system: StringName, p_context_id: StringName = &"",) -> void` est une méthode qui initialise l’objet et copie les arguments dans son état interne ; `validate(aucun paramètre) -> Error` est une méthode qui vérifie les préconditions et signale toute donnée invalide.
- **Données et types :** variables `cause_id: StringName`, `source_system: StringName`, `context_id: StringName`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Résultat attendu et vérification :** obtenir `OK` pour le cas valide et un code `Error` documenté pour chaque refus, sans mutation partielle. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

`source_system` indique la provenance applicative, par exemple :

> **[LECTURE] Exemples de systèmes sources — Ne pas saisir.**

```text
system.social.dialogue
system.quest
system.world.event
```

Le chapitre 15 n’implémente pas ces systèmes. Il prépare seulement une provenance vérifiable.

## 9. Commander un changement social

> **[VSC] Visual Studio Code — Créer : `res://src/features/social/application/change_social_relationship_command.gd`.**

```gdscript
class_name ChangeSocialRelationshipCommand
extends RefCounted

const MAX_ABSOLUTE_DELTA := 100

var relationship_key: SocialRelationshipKey
var cause: SocialChangeCause
var affinity_delta: int = 0
var trust_delta: int = 0
var respect_delta: int = 0
var fear_delta: int = 0
var logical_tick: int = 0

func validate() -> Error:
	if relationship_key == null:
		return ERR_INVALID_PARAMETER
	if relationship_key.validate() != OK:
		return ERR_INVALID_DATA

	if cause == null:
		return ERR_INVALID_PARAMETER
	if cause.validate() != OK:
		return ERR_INVALID_DATA

	if logical_tick < 0:
		return ERR_INVALID_DATA

	var deltas: Array[int] = [
		affinity_delta,
		trust_delta,
		respect_delta,
		fear_delta,
	]
	for delta: int in deltas:
		if absi(delta) > MAX_ABSOLUTE_DELTA:
			return ERR_INVALID_DATA

	if (
		affinity_delta == 0
		and trust_delta == 0
		and respect_delta == 0
		and fear_delta == 0
	):
		return ERR_INVALID_DATA

	return OK
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc définit le contrat `ChangeSocialRelationshipCommand` et l’appuie sur `RefCounted`.
- **Fonctions, paramètres et retours :** `validate(aucun paramètre) -> Error` est une méthode qui vérifie les préconditions et signale toute donnée invalide.
- **Données et types :** constantes `MAX_ABSOLUTE_DELTA := 100` ; variables `relationship_key: SocialRelationshipKey`, `cause: SocialChangeCause`, `affinity_delta: int = 0`, `trust_delta: int = 0`, `respect_delta: int = 0`, `fear_delta: int = 0` et 2 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les parcours et historiques sont bornés ; les transitions utilisent des ticks logiques cohérents ; les valeurs numériques restent dans leurs bornes métier.
- **Résultat attendu et vérification :** obtenir `OK` pour le cas valide et un code `Error` documenté pour chaque refus, sans mutation partielle. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

La commande :

- ne contient aucun nœud ;
- ne contient aucun nom affiché ;
- impose une cause ;
- impose un tick logique non négatif ;
- refuse les commandes sans effet ;
- limite l’amplitude d’une seule opération.

Le tick logique appartient à la simulation ou au coordinateur de partie. Il ne dépend pas de l’horloge murale du système.

## 10. Conserver un historique borné

### 10.1 Enregistrement de changement

> **[VSC] Visual Studio Code — Créer : `res://src/features/social/domain/social_change_record.gd`.**

```gdscript
class_name SocialChangeRecord
extends RefCounted

const MAX_ABSOLUTE_DELTA := 100

var revision: int
var logical_tick: int
var cause_id: StringName
var source_system: StringName
var context_id: StringName
var affinity_delta: int
var trust_delta: int
var respect_delta: int
var fear_delta: int

func validate() -> Error:
	if revision <= 0:
		return ERR_INVALID_DATA
	if logical_tick < 0:
		return ERR_INVALID_DATA
	if not StableId.is_valid(cause_id):
		return ERR_INVALID_DATA
	if not StableId.is_valid(source_system):
		return ERR_INVALID_DATA
	if not context_id.is_empty() and not StableId.is_valid(context_id):
		return ERR_INVALID_DATA

	var deltas: Array[int] = [
		affinity_delta,
		trust_delta,
		respect_delta,
		fear_delta,
	]
	var has_effect := false
	for delta: int in deltas:
		if absi(delta) > MAX_ABSOLUTE_DELTA:
			return ERR_INVALID_DATA
		has_effect = has_effect or delta != 0

	if not has_effect:
		return ERR_INVALID_DATA

	return OK

func duplicate_record() -> SocialChangeRecord:
	var copy := SocialChangeRecord.new()
	copy.revision = revision
	copy.logical_tick = logical_tick
	copy.cause_id = cause_id
	copy.source_system = source_system
	copy.context_id = context_id
	copy.affinity_delta = affinity_delta
	copy.trust_delta = trust_delta
	copy.respect_delta = respect_delta
	copy.fear_delta = fear_delta
	return copy
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc définit le contrat `SocialChangeRecord` et l’appuie sur `RefCounted`.
- **Fonctions, paramètres et retours :** `validate(aucun paramètre) -> Error` est une méthode qui vérifie les préconditions et signale toute donnée invalide ; `duplicate_record(aucun paramètre) -> SocialChangeRecord` est une méthode qui produit une copie défensive indépendante de l’original.
- **Données et types :** constantes `MAX_ABSOLUTE_DELTA := 100` ; variables `revision: int`, `logical_tick: int`, `cause_id: StringName`, `source_system: StringName`, `context_id: StringName`, `affinity_delta: int` et 6 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** crée une copie défensive. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les parcours et historiques sont bornés ; les transitions utilisent des ticks logiques cohérents ; les lectures ne doivent pas exposer directement un objet interne mutable ; les valeurs numériques restent dans leurs bornes métier.
- **Résultat attendu et vérification :** obtenir `OK` pour le cas valide et un code `Error` documenté pour chaque refus, sans mutation partielle. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

### 10.2 Pourquoi l’historique reste borné

Un historique illimité :

- augmente chaque sauvegarde ;
- ralentit les requêtes ;
- conserve des détails sans politique ;
- complique les migrations ;
- peut révéler des données inutiles dans les journaux.

La valeur pédagogique retenue est `32` changements récents par direction.

Un historique analytique plus long appartiendrait à une infrastructure spécialisée du chapitre 28.

## 11. État d’une relation

> **[VSC] Visual Studio Code — Créer : `res://src/features/social/domain/social_relationship_state.gd`.**

```gdscript
class_name SocialRelationshipState
extends RefCounted

const MAX_HISTORY := 32

var key: SocialRelationshipKey
var axes := SocialAxes.new()
var revision: int = 0
var last_changed_tick: int = 0
var _history: Array[SocialChangeRecord] = []

func _init(p_key: SocialRelationshipKey) -> void:
	key = p_key

func validate() -> Error:
	if key == null or key.validate() != OK:
		return ERR_INVALID_DATA
	if axes == null or axes.validate() != OK:
		return ERR_INVALID_DATA
	if revision < 0 or last_changed_tick < 0:
		return ERR_INVALID_DATA
	if _history.size() > MAX_HISTORY:
		return ERR_INVALID_DATA

	var previous_revision := 0
	var previous_tick := 0

	for record: SocialChangeRecord in _history:
		if record == null or record.validate() != OK:
			return ERR_INVALID_DATA
		if record.revision <= previous_revision:
			return ERR_INVALID_DATA
		if record.logical_tick < previous_tick:
			return ERR_INVALID_DATA
		previous_revision = record.revision
		previous_tick = record.logical_tick

	if revision == 0:
		if last_changed_tick != 0 or not _history.is_empty():
			return ERR_INVALID_DATA
	elif _history.is_empty():
		return ERR_INVALID_DATA
	else:
		if _history.back().revision != revision:
			return ERR_INVALID_DATA
		if _history.back().logical_tick != last_changed_tick:
			return ERR_INVALID_DATA

	return OK

func get_history_copy() -> Array[SocialChangeRecord]:
	var copy: Array[SocialChangeRecord] = []
	for record: SocialChangeRecord in _history:
		copy.append(record.duplicate_record())
	return copy

func apply_validated(
	command: ChangeSocialRelationshipCommand,
) -> SocialChangeRecord:
	axes.apply_delta(
		command.affinity_delta,
		command.trust_delta,
		command.respect_delta,
		command.fear_delta,
	)

	revision += 1
	last_changed_tick = command.logical_tick

	var record := SocialChangeRecord.new()
	record.revision = revision
	record.logical_tick = command.logical_tick
	record.cause_id = command.cause.cause_id
	record.source_system = command.cause.source_system
	record.context_id = command.cause.context_id
	record.affinity_delta = command.affinity_delta
	record.trust_delta = command.trust_delta
	record.respect_delta = command.respect_delta
	record.fear_delta = command.fear_delta

	_history.append(record)
	while _history.size() > MAX_HISTORY:
		_history.pop_front()

	return record
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc définit le contrat `SocialRelationshipState` et l’appuie sur `RefCounted`.
- **Fonctions, paramètres et retours :** `_init(p_key: SocialRelationshipKey) -> void` est une méthode qui initialise l’objet et copie les arguments dans son état interne ; `validate(aucun paramètre) -> Error` est une méthode qui vérifie les préconditions et signale toute donnée invalide ; `get_history_copy(aucun paramètre) -> Array[SocialChangeRecord]` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes ; `apply_validated(command: ChangeSocialRelationshipCommand,) -> SocialChangeRecord` est une méthode qui valide puis ajoute ou applique une mutation métier.
- **Données et types :** constantes `MAX_HISTORY := 32` ; variables `key: SocialRelationshipKey`, `axes := SocialAxes.new()`, `revision: int = 0`, `last_changed_tick: int = 0`, `_history: Array[SocialChangeRecord] = []`, `previous_revision := 0` et 3 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; la boucle `while` poursuit un parcours dont le budget doit rester borné ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique ; modifie un état temporel ou une révision ; crée une copie défensive. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les parcours et historiques sont bornés ; les transitions utilisent des ticks logiques cohérents ; les lectures ne doivent pas exposer directement un objet interne mutable ; les valeurs numériques restent dans leurs bornes métier.
- **Résultat attendu et vérification :** obtenir `OK` pour le cas valide et un code `Error` documenté pour chaque refus, sans mutation partielle. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

`apply_validated()` suppose que la commande a déjà réussi `validate()`. Cette précondition est assurée par le service applicatif.

Le tableau retourné par `get_history_copy()` empêche un appelant de supprimer directement les éléments du tableau interne.

## 12. Dépôt de relations

### 12.1 Contrat

> **[VSC] Visual Studio Code — Créer : `res://src/features/social/application/social_relationship_repository.gd`.**

```gdscript
class_name SocialRelationshipRepository
extends RefCounted

func get_state(
	source_id: StringName,
	target_id: StringName,
) -> SocialRelationshipState:
	push_error("get_state() doit être implémentée.")
	return null

func replace_one(
	state: SocialRelationshipState,
) -> Error:
	push_error("replace_one() doit être implémentée.")
	return ERR_UNAVAILABLE

func replace_all(
	states: Array[SocialRelationshipState],
) -> Error:
	push_error("replace_all() doit être implémentée.")
	return ERR_UNAVAILABLE

func get_outgoing(
	source_id: StringName,
) -> Array[SocialRelationshipState]:
	push_error("get_outgoing() doit être implémentée.")
	return []

func get_all() -> Array[SocialRelationshipState]:
	push_error("get_all() doit être implémentée.")
	return []
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc définit le contrat `SocialRelationshipRepository` et l’appuie sur `RefCounted`.
- **Fonctions, paramètres et retours :** `get_state(source_id: StringName, target_id: StringName,) -> SocialRelationshipState` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes ; `replace_one(state: SocialRelationshipState,) -> Error` est une méthode qui remplace l’état autoritaire à partir d’un candidat déjà validé ; `replace_all(states: Array[SocialRelationshipState],) -> Error` est une méthode qui remplace l’état autoritaire à partir d’un candidat déjà validé ; `get_outgoing(source_id: StringName,) -> Array[SocialRelationshipState]` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes ; `get_all(aucun paramètre) -> Array[SocialRelationshipState]` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** remplace l’état autoritaire ; mémorise une erreur consultable. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Résultat attendu et vérification :** obtenir `OK` pour le cas valide et un code `Error` documenté pour chaque refus, sans mutation partielle. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

### 12.2 Implémentation en mémoire

> **[VSC] Visual Studio Code — Créer : `res://src/features/social/infrastructure/in_memory_social_relationship_repository.gd`.**

```gdscript
class_name InMemorySocialRelationshipRepository
extends SocialRelationshipRepository

var _states: Dictionary[String, SocialRelationshipState] = {}
var _outgoing_keys: Dictionary[StringName, Array] = {}

func get_state(
	source_id: StringName,
	target_id: StringName,
) -> SocialRelationshipState:
	var key := SocialRelationshipKey.new(source_id, target_id)
	if key.validate() != OK:
		return null
	return _states.get(key.to_storage_key()) as SocialRelationshipState

func replace_one(
	state: SocialRelationshipState,
) -> Error:
	if state == null or state.validate() != OK:
		return ERR_INVALID_DATA

	var storage_key := state.key.to_storage_key()
	var is_new := not _states.has(storage_key)
	_states[storage_key] = state

	if is_new:
		_index_outgoing(state.key.source_id, storage_key)

	return OK

func replace_all(
	states: Array[SocialRelationshipState],
) -> Error:
	var candidate_states: Dictionary[String, SocialRelationshipState] = {}
	var candidate_outgoing: Dictionary[StringName, Array] = {}

	for state: SocialRelationshipState in states:
		if state == null or state.validate() != OK:
			return ERR_INVALID_DATA

		var storage_key := state.key.to_storage_key()
		if candidate_states.has(storage_key):
			return ERR_ALREADY_EXISTS

		candidate_states[storage_key] = state

		if not candidate_outgoing.has(state.key.source_id):
			candidate_outgoing[state.key.source_id] = []
		candidate_outgoing[state.key.source_id].append(storage_key)

	_states = candidate_states
	_outgoing_keys = candidate_outgoing
	return OK

func get_outgoing(
	source_id: StringName,
) -> Array[SocialRelationshipState]:
	var result: Array[SocialRelationshipState] = []
	var keys := _outgoing_keys.get(source_id, []) as Array

	for storage_key: String in keys:
		var state := _states.get(storage_key) as SocialRelationshipState
		if state != null:
			result.append(state)

	result.sort_custom(
		func(left: SocialRelationshipState, right: SocialRelationshipState) -> bool:
			return String(left.key.target_id) < String(right.key.target_id)
	)
	return result

func get_all() -> Array[SocialRelationshipState]:
	var result: Array[SocialRelationshipState] = []
	result.assign(_states.values())
	result.sort_custom(
		func(left: SocialRelationshipState, right: SocialRelationshipState) -> bool:
			return left.key.to_storage_key() < right.key.to_storage_key()
	)
	return result

func _index_outgoing(
	source_id: StringName,
	storage_key: String,
) -> void:
	if not _outgoing_keys.has(source_id):
		_outgoing_keys[source_id] = []
	_outgoing_keys[source_id].append(storage_key)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc définit le contrat `InMemorySocialRelationshipRepository` et l’appuie sur `SocialRelationshipRepository`.
- **Fonctions, paramètres et retours :** `get_state(source_id: StringName, target_id: StringName,) -> SocialRelationshipState` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes ; `replace_one(state: SocialRelationshipState,) -> Error` est une méthode qui remplace l’état autoritaire à partir d’un candidat déjà validé ; `replace_all(states: Array[SocialRelationshipState],) -> Error` est une méthode qui remplace l’état autoritaire à partir d’un candidat déjà validé ; `get_outgoing(source_id: StringName,) -> Array[SocialRelationshipState]` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes ; `get_all(aucun paramètre) -> Array[SocialRelationshipState]` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes ; `_index_outgoing(source_id: StringName, storage_key: String,) -> void` est une méthode qui encapsule l’opération métier indiquée par son nom.
- **Données et types :** variables `_states: Dictionary[String, SocialRelationshipState] = {}`, `_outgoing_keys: Dictionary[StringName, Array] = {}`, `key := SocialRelationshipKey.new(source_id, target_id)`, `storage_key := state.key.to_storage_key()`, `is_new := not _states.has(storage_key)`, `candidate_states: Dictionary[String, SocialRelationshipState] = {}` et 6 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** remplace l’état autoritaire ; ajoute une entrée à une collection ou à un historique. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** un candidat complet est validé avant mutation de l’état actif.
- **Résultat attendu et vérification :** obtenir `OK` pour le cas valide et un code `Error` documenté pour chaque refus, sans mutation partielle. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

`replace_all()` prépare deux dictionnaires candidats. Les données courantes ne sont remplacées qu’après validation complète.

Le second index évite de parcourir toutes les relations pour obtenir les perceptions sortantes d’un personnage.

## 13. Vérifier les personnages référencés

Le dépôt de relations ne doit pas dépendre des nœuds actifs.

Il dépend d’un contrat de lecture des identités connues.

> **[VSC] Visual Studio Code — Créer : `res://src/features/characters/application/character_identity_index.gd`.**

```gdscript
class_name CharacterIdentityIndex
extends RefCounted

func contains(character_id: StringName) -> bool:
	push_error("contains() doit être implémentée.")
	return false
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc définit le contrat `CharacterIdentityIndex` et l’appuie sur `RefCounted`.
- **Fonctions, paramètres et retours :** `contains(character_id: StringName) -> bool` est une méthode qui encapsule l’opération métier indiquée par son nom.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** mémorise une erreur consultable. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Résultat attendu et vérification :** obtenir `true` uniquement lorsque toutes les conditions décrites sont satisfaites et `false` pour les cas limites. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

Une implémentation peut agréger :

- les personnages présents dans la sauvegarde ;
- les personnages prédéfinis ;
- les personnages créés dynamiquement ;
- les identités archivées encore référencées.

Elle ne doit pas limiter la réponse aux personnages visibles.

## 14. Événement social typé

> **[VSC] Visual Studio Code — Créer : `res://src/features/social/application/social_relationship_changed_event.gd`.**

```gdscript
class_name SocialRelationshipChangedEvent
extends RefCounted

var source_id: StringName
var target_id: StringName
var revision: int
var logical_tick: int
var cause_id: StringName
var before_axes: SocialAxes
var after_axes: SocialAxes

func validate() -> Error:
	if not CharacterId.is_valid(source_id):
		return ERR_INVALID_DATA
	if not CharacterId.is_valid(target_id):
		return ERR_INVALID_DATA
	if source_id == target_id:
		return ERR_INVALID_DATA
	if revision <= 0 or logical_tick < 0:
		return ERR_INVALID_DATA
	if not StableId.is_valid(cause_id):
		return ERR_INVALID_DATA
	if before_axes == null or before_axes.validate() != OK:
		return ERR_INVALID_DATA
	if after_axes == null or after_axes.validate() != OK:
		return ERR_INVALID_DATA
	return OK
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc définit le contrat `SocialRelationshipChangedEvent` et l’appuie sur `RefCounted`.
- **Fonctions, paramètres et retours :** `validate(aucun paramètre) -> Error` est une méthode qui vérifie les préconditions et signale toute donnée invalide.
- **Données et types :** variables `source_id: StringName`, `target_id: StringName`, `revision: int`, `logical_tick: int`, `cause_id: StringName`, `before_axes: SocialAxes` et 1 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** une identité ne peut pas former un lien avec elle-même ; chaque référence doit correspondre à une identité logique connue, même hors scène ; les transitions utilisent des ticks logiques cohérents.
- **Résultat attendu et vérification :** obtenir `OK` pour le cas valide et un code `Error` documenté pour chaque refus, sans mutation partielle. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

L’événement transporte des copies des axes avant et après. Un observateur ne peut donc pas modifier l’état interne du dépôt.

## 15. Service applicatif

> **[VSC] Visual Studio Code — Créer : `res://src/features/social/application/social_relationship_service.gd`.**

```gdscript
class_name SocialRelationshipService
extends RefCounted

signal relationship_changed(
	event: SocialRelationshipChangedEvent,
)

var _repository: SocialRelationshipRepository
var _character_index: CharacterIdentityIndex

func _init(
	repository: SocialRelationshipRepository,
	character_index: CharacterIdentityIndex,
) -> void:
	_repository = repository
	_character_index = character_index

func apply_change(
	command: ChangeSocialRelationshipCommand,
) -> Error:
	if command == null or command.validate() != OK:
		return ERR_INVALID_DATA

	if _repository == null or _character_index == null:
		return ERR_UNCONFIGURED

	var key := command.relationship_key

	if not _character_index.contains(key.source_id):
		return ERR_DOES_NOT_EXIST
	if not _character_index.contains(key.target_id):
		return ERR_DOES_NOT_EXIST

	var current := _repository.get_state(
		key.source_id,
		key.target_id,
	)
	if current == null:
		current = SocialRelationshipState.new(
			SocialRelationshipKey.new(
				key.source_id,
				key.target_id,
			)
		)

	if command.logical_tick < current.last_changed_tick:
		return ERR_INVALID_DATA

	var candidate := current.duplicate_state()
	var before := candidate.axes.duplicate_axes()
	var record := candidate.apply_validated(command)

	if candidate.validate() != OK:
		return ERR_INVALID_DATA

	var event := SocialRelationshipChangedEvent.new()
	event.source_id = key.source_id
	event.target_id = key.target_id
	event.revision = record.revision
	event.logical_tick = record.logical_tick
	event.cause_id = record.cause_id
	event.before_axes = before
	event.after_axes = candidate.axes.duplicate_axes()

	if event.validate() != OK:
		return ERR_INVALID_DATA

	var replace_error := _repository.replace_one(candidate)
	if replace_error != OK:
		return replace_error

	relationship_changed.emit(event)
	return OK
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc définit le contrat `SocialRelationshipService` et l’appuie sur `RefCounted`.
- **Fonctions, paramètres et retours :** `_init(repository: SocialRelationshipRepository, character_index: CharacterIdentityIndex,) -> void` est une méthode qui initialise l’objet et copie les arguments dans son état interne ; `apply_change(command: ChangeSocialRelationshipCommand,) -> Error` est une méthode qui valide puis ajoute ou applique une mutation métier.
- **Données et types :** variables `_repository: SocialRelationshipRepository`, `_character_index: CharacterIdentityIndex`, `key := command.relationship_key`, `current := _repository.get_state(`, `candidate := current.duplicate_state()`, `before := candidate.axes.duplicate_axes()` et 3 autre(s) ; signaux `relationship_changed(`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** émet un événement observable après succès ; remplace l’état autoritaire ; crée une copie défensive. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les transitions utilisent des ticks logiques cohérents ; un candidat complet est validé avant mutation de l’état actif ; les lectures ne doivent pas exposer directement un objet interne mutable.
- **Résultat attendu et vérification :** obtenir `OK` pour le cas valide et un code `Error` documenté pour chaque refus, sans mutation partielle. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

Le service vérifie :

1. la commande ;
2. ses dépendances ;
3. l’existence logique des deux personnages ;
4. l’ordre du tick ;
5. l’état final ;
6. l’événement avant émission.

L’absence d’un personnage dans la scène n’est jamais une erreur. Seule l’absence de son identité logique l’est.

## 16. Éviter une mutation partielle

Le service ne modifie jamais directement l’objet conservé dans le dépôt.

Il calcule un candidat, le valide, prépare l’événement, puis demande au dépôt de remplacer une seule relation.

> **[VSC] Visual Studio Code — Ajouter à `social_relationship_state.gd`.**

```gdscript
func duplicate_state() -> SocialRelationshipState:
	var copy := SocialRelationshipState.new(
		SocialRelationshipKey.new(
			key.source_id,
			key.target_id,
		)
	)
	copy.axes = axes.duplicate_axes()
	copy.revision = revision
	copy.last_changed_tick = last_changed_tick

	var history_copy: Array[SocialChangeRecord] = []
	for record: SocialChangeRecord in _history:
		history_copy.append(record.duplicate_record())
	copy._history = history_copy

	return copy
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Fonctions, paramètres et retours :** `duplicate_state(aucun paramètre) -> SocialRelationshipState` est une méthode qui produit une copie défensive indépendante de l’original.
- **Données et types :** variables `copy := SocialRelationshipState.new(`, `history_copy: Array[SocialChangeRecord] = []`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique ; crée une copie défensive. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les lectures ne doivent pas exposer directement un objet interne mutable.
- **Résultat attendu et vérification :** observer le comportement décrit par la section sans modifier de donnée autoritaire non concernée. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

`duplicate_state()` duplique aussi chaque enregistrement. Une simple duplication du tableau aurait conservé les mêmes objets mutables.

Le service applique ensuite la commande au candidat :

> **[LECTURE] Ordre atomique d’une mutation — Ne pas saisir.**

```text
lire l’état courant
    ↓
dupliquer l’état et son historique
    ↓
appliquer la commande au candidat
    ↓
valider le candidat et l’événement
    ↓
replace_one(candidat)
    ↓
émettre l’événement
```

Si la validation échoue, l’état courant n’a pas été modifié. Si `replace_one()` échoue, aucun événement n’est émis.

## 17. Requêtes de voisinage

> **[VSC] Visual Studio Code — Créer : `res://src/features/social/application/social_relationship_query.gd`.**

```gdscript
class_name SocialRelationshipQuery
extends RefCounted

var _repository: SocialRelationshipRepository

func _init(repository: SocialRelationshipRepository) -> void:
	_repository = repository

func get_outgoing(
	source_id: StringName,
) -> Array[SocialRelationshipState]:
	if _repository == null:
		return []
	if not CharacterId.is_valid(source_id):
		return []
	return _repository.get_outgoing(source_id)

func get_targets_above_affinity(
	source_id: StringName,
	minimum_affinity: int,
) -> Array[StringName]:
	var threshold := clampi(
		minimum_affinity,
		SocialAxes.MIN_SIGNED,
		SocialAxes.MAX_SIGNED,
	)

	var result: Array[StringName] = []
	for state: SocialRelationshipState in get_outgoing(source_id):
		if state.axes.affinity >= threshold:
			result.append(state.key.target_id)

	result.sort()
	return result
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc définit le contrat `SocialRelationshipQuery` et l’appuie sur `RefCounted`.
- **Fonctions, paramètres et retours :** `_init(repository: SocialRelationshipRepository) -> void` est une méthode qui initialise l’objet et copie les arguments dans son état interne ; `get_outgoing(source_id: StringName,) -> Array[SocialRelationshipState]` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes ; `get_targets_above_affinity(source_id: StringName, minimum_affinity: int,) -> Array[StringName]` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes.
- **Données et types :** variables `_repository: SocialRelationshipRepository`, `threshold := clampi(`, `result: Array[StringName] = []`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** chaque référence doit correspondre à une identité logique connue, même hors scène ; les parcours et historiques sont bornés ; les valeurs numériques restent dans leurs bornes métier ; l’ordre des identifiants conserve la direction de la relation.
- **Résultat attendu et vérification :** pouvoir instancier ou appeler ce contrat depuis la couche prévue, avec un état valide et des lectures défensives. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

La requête retourne des identifiants, pas des nœuds.

L’interface ou un autre système peut ensuite demander séparément :

- le nom affiché ;
- le portrait ;
- la présence dans la scène ;
- la localisation actuelle.

## 18. Vue mutuelle

> **[VSC] Visual Studio Code — Créer : `res://src/features/social/application/mutual_social_view.gd`.**

```gdscript
class_name MutualSocialView
extends RefCounted

var first_id: StringName
var second_id: StringName
var mutual_affinity: int
var mutual_trust: int
var mutual_respect: int
var maximum_fear: int
var complete: bool = false
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc définit le contrat `MutualSocialView` et l’appuie sur `RefCounted`.
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** variables `first_id: StringName`, `second_id: StringName`, `mutual_affinity: int`, `mutual_trust: int`, `mutual_respect: int`, `maximum_fear: int` et 1 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Résultat attendu et vérification :** pouvoir instancier ou appeler ce contrat depuis la couche prévue, avec un état valide et des lectures défensives. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

> **[VSC] Visual Studio Code — Ajouter à `social_relationship_query.gd`.**

```gdscript
func get_mutual_view(
	first_id: StringName,
	second_id: StringName,
) -> MutualSocialView:
	var view := MutualSocialView.new()
	view.first_id = first_id
	view.second_id = second_id

	if _repository == null:
		return view
	if not CharacterId.is_valid(first_id):
		return view
	if not CharacterId.is_valid(second_id):
		return view
	if first_id == second_id:
		return view

	var forward := _repository.get_state(first_id, second_id)
	var reverse := _repository.get_state(second_id, first_id)

	if forward == null or reverse == null:
		return view

	view.mutual_affinity = mini(
		forward.axes.affinity,
		reverse.axes.affinity,
	)
	view.mutual_trust = mini(
		forward.axes.trust,
		reverse.axes.trust,
	)
	view.mutual_respect = mini(
		forward.axes.respect,
		reverse.axes.respect,
	)
	view.maximum_fear = maxi(
		forward.axes.fear,
		reverse.axes.fear,
	)
	view.complete = true
	return view
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Fonctions, paramètres et retours :** `get_mutual_view(first_id: StringName, second_id: StringName,) -> MutualSocialView` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes.
- **Données et types :** variables `view := MutualSocialView.new()`, `forward := _repository.get_state(first_id, second_id)`, `reverse := _repository.get_state(second_id, first_id)`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** une identité ne peut pas former un lien avec elle-même ; chaque référence doit correspondre à une identité logique connue, même hors scène.
- **Résultat attendu et vérification :** observer le comportement décrit par la section sans modifier de donnée autoritaire non concernée. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

Une vue incomplète ne remplace pas une direction absente par des zéros. Zéro pourrait signifier une neutralité connue, alors que l’absence signifie « aucune relation enregistrée ».

## 19. Relations symétriques explicites

Certains concepts futurs sont réellement symétriques :

- un mariage reconnu ;
- une fratrie ;
- une appartenance commune à une maison ;
- un pacte formel.

Ils ne doivent pas être stockés dans `SocialRelationshipState`.

Le chapitre 16 introduira les relations familiales avec leurs propres invariants. Le chapitre 23 introduira les affiliations politiques et juridiques.

Le système social peut lire ces informations comme contexte, mais ne les possède pas.

## 20. Modificateurs et événements du monde

Une explosion, une rumeur ou une quête peut affecter plusieurs relations.

Le système appelant doit produire plusieurs commandes explicites.

> **[LECTURE] Propagation contrôlée — Ne pas saisir.**

```text
événement de monde
    ↓
sélection des personnages concernés
    ↓
une commande validée par direction
    ↓
une cause et un context_id communs
```

Le service social ne parcourt pas spontanément tous les personnages. Cette séparation évite les mutations globales cachées.

## 21. Snapshot persistant

### 21.1 Forme JSON

> **[LECTURE] Exemple de relation sauvegardée — Ne pas saisir.**

```json
{
  "source_id": "chr_01jz8r5d2w4f8m1k3n6p9q0s7t",
  "target_id": "chr_01jz8r6ab8d1e4g7h2k5m9p3qr",
  "revision": 4,
  "last_changed_tick": 8120,
  "axes": {
    "affinity": 35,
    "trust": 20,
    "respect": 48,
    "fear": 0
  },
  "history": [
    {
      "revision": 4,
      "logical_tick": 8120,
      "cause_id": "social.cause.promise.kept",
      "source_system": "system.quest",
      "context_id": "quest.village.water",
      "deltas": {
        "affinity": 8,
        "trust": 12,
        "respect": 5,
        "fear": 0
      }
    }
  ]
}
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc montre la forme JSON attendue par « 21.1 Forme JSON ».
- **Entrées et résultat :** le bloc ne définit pas de fonction. Il utilise les variables déjà présentes dans le contexte ou décrit une structure de données ; aucune valeur de retour implicite ne doit être supposée.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les transitions utilisent des ticks logiques cohérents.
- **Résultat attendu et vérification :** obtenir un document décodable avec exactement les clés, types et identifiants attendus, sans cache ni valeur dérivée persistée. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

Le snapshot ne contient :

- aucun nom affiché ;
- aucun nœud ;
- aucune référence de scène ;
- aucun objet `Resource` ;
- aucune vue mutuelle calculée ;
- aucun portrait ;
- aucune décision d’agent.

## 22. Codec strict

> **[VSC] Visual Studio Code — Créer : `res://src/features/social/infrastructure/social_relationship_snapshot_codec.gd`.**

```gdscript
class_name SocialRelationshipSnapshotCodec
extends RefCounted

const REQUIRED_KEYS: Array[String] = [
	"source_id",
	"target_id",
	"revision",
	"last_changed_tick",
	"axes",
	"history",
]

func encode(
	state: SocialRelationshipState,
) -> Dictionary:
	if state == null or state.validate() != OK:
		return {}

	var history_payload: Array[Dictionary] = []
	for record: SocialChangeRecord in state.get_history_copy():
		history_payload.append(_encode_record(record))

	return {
		"source_id": String(state.key.source_id),
		"target_id": String(state.key.target_id),
		"revision": state.revision,
		"last_changed_tick": state.last_changed_tick,
		"axes": {
			"affinity": state.axes.affinity,
			"trust": state.axes.trust,
			"respect": state.axes.respect,
			"fear": state.axes.fear,
		},
		"history": history_payload,
	}

func decode(payload: Variant) -> SocialRelationshipState:
	if not payload is Dictionary:
		return null

	var data := payload as Dictionary
	if not _has_exact_keys(data, REQUIRED_KEYS):
		return null

	if not data["source_id"] is String:
		return null
	if not data["target_id"] is String:
		return null
	if not data["revision"] is int:
		return null
	if not data["last_changed_tick"] is int:
		return null
	if not data["axes"] is Dictionary:
		return null
	if not data["history"] is Array:
		return null

	var key := SocialRelationshipKey.new(
		StringName(data["source_id"]),
		StringName(data["target_id"]),
	)
	if key.validate() != OK:
		return null

	var axes := _decode_axes(data["axes"])
	if axes == null:
		return null

	var state := SocialRelationshipState.new(key)
	state.axes = axes
	state.revision = data["revision"]
	state.last_changed_tick = data["last_changed_tick"]

	var records: Array[SocialChangeRecord] = []
	for record_payload: Variant in data["history"]:
		var record := _decode_record(record_payload)
		if record == null:
			return null
		records.append(record)

	var history_error := state.set_history_for_restore(records)
	if history_error != OK:
		return null
	if state.validate() != OK:
		return null
	return state

func _has_exact_keys(
	data: Dictionary,
	required: Array[String],
) -> bool:
	if data.size() != required.size():
		return false
	for key: String in required:
		if not data.has(key):
			return false
	return true
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc définit le contrat `SocialRelationshipSnapshotCodec` et l’appuie sur `RefCounted`.
- **Fonctions, paramètres et retours :** `encode(state: SocialRelationshipState,) -> Dictionary` est une méthode qui convertit l’objet vers une représentation de transport ou de stockage ; `decode(payload: Variant) -> SocialRelationshipState` est une méthode qui reconstruit une valeur typée après validation de la représentation externe ; `_has_exact_keys(data: Dictionary, required: Array[String],) -> bool` est une méthode qui encapsule l’opération métier indiquée par son nom.
- **Données et types :** constantes `REQUIRED_KEYS: Array[String] = [` ; variables `history_payload: Array[Dictionary] = []`, `data := payload as Dictionary`, `key := SocialRelationshipKey.new(`, `axes := _decode_axes(data["axes"])`, `state := SocialRelationshipState.new(key)`, `records: Array[SocialChangeRecord] = []` et 2 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les lectures ne doivent pas exposer directement un objet interne mutable.
- **Résultat attendu et vérification :** obtenir `true` uniquement lorsque toutes les conditions décrites sont satisfaites et `false` pour les cas limites. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

Le codec montre les contrôles principaux. Les méthodes `_encode_record()`, `_decode_axes()`, `_decode_record()` et `set_history_for_restore()` sont détaillées dans la section suivante.

## 23. Restaurer l’historique sans exposer la collection

> **[VSC] Visual Studio Code — Ajouter à `social_relationship_state.gd`.**

```gdscript
func set_history_for_restore(
	records: Array[SocialChangeRecord],
) -> Error:
	if records.size() > MAX_HISTORY:
		return ERR_INVALID_DATA

	var candidate: Array[SocialChangeRecord] = []
	for record: SocialChangeRecord in records:
		if record == null or record.validate() != OK:
			return ERR_INVALID_DATA
		candidate.append(record)

	_history = candidate
	return validate()
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Fonctions, paramètres et retours :** `set_history_for_restore(records: Array[SocialChangeRecord],) -> Error` est une méthode qui encapsule l’opération métier indiquée par son nom.
- **Données et types :** variables `candidate: Array[SocialChangeRecord] = []`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** les parcours et historiques sont bornés ; un candidat complet est validé avant mutation de l’état actif ; les valeurs numériques restent dans leurs bornes métier.
- **Résultat attendu et vérification :** obtenir `OK` pour le cas valide et un code `Error` documenté pour chaque refus, sans mutation partielle. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

Cette méthode n’est utilisée que par l’infrastructure de restauration.

Le domaine n’expose pas un setter générique de l’historique.

## 24. Encoder et décoder les axes

> **[VSC] Visual Studio Code — Ajouter à `social_relationship_snapshot_codec.gd`.**

```gdscript
func _decode_axes(payload: Variant) -> SocialAxes:
	if not payload is Dictionary:
		return null

	var data := payload as Dictionary
	var keys: Array[String] = [
		"affinity",
		"trust",
		"respect",
		"fear",
	]
	if not _has_exact_keys(data, keys):
		return null

	for key: String in keys:
		if not data[key] is int:
			return null

	var axes := SocialAxes.new()
	axes.affinity = data["affinity"]
	axes.trust = data["trust"]
	axes.respect = data["respect"]
	axes.fear = data["fear"]

	if axes.validate() != OK:
		return null
	return axes
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Fonctions, paramètres et retours :** `_decode_axes(payload: Variant) -> SocialAxes` est une méthode qui encapsule l’opération métier indiquée par son nom.
- **Données et types :** variables `data := payload as Dictionary`, `keys: Array[String] = [`, `axes := SocialAxes.new()`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les types annoncés doivent être respectés, les références doivent rester valides et aucune donnée interne mutable ne doit être exposée sans copie.
- **Résultat attendu et vérification :** observer le comportement décrit par la section sans modifier de donnée autoritaire non concernée. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

Les nombres décimaux sont refusés même s’ils pourraient être convertis vers des entiers. La sauvegarde doit respecter le contrat exact.

## 25. Encoder un enregistrement

> **[VSC] Visual Studio Code — Ajouter à `social_relationship_snapshot_codec.gd`.**

```gdscript
func _encode_record(
	record: SocialChangeRecord,
) -> Dictionary:
	return {
		"revision": record.revision,
		"logical_tick": record.logical_tick,
		"cause_id": String(record.cause_id),
		"source_system": String(record.source_system),
		"context_id": String(record.context_id),
		"deltas": {
			"affinity": record.affinity_delta,
			"trust": record.trust_delta,
			"respect": record.respect_delta,
			"fear": record.fear_delta,
		},
	}
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Fonctions, paramètres et retours :** `_encode_record(record: SocialChangeRecord,) -> Dictionary` est une méthode qui encapsule l’opération métier indiquée par son nom.
- **Données et types :** l’extrait ne crée pas d’état durable. Les types proviennent des paramètres, des valeurs locales ou du schéma externe montré par le bloc.
- **Déroulement :** les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les transitions utilisent des ticks logiques cohérents.
- **Résultat attendu et vérification :** observer le comportement décrit par la section sans modifier de donnée autoritaire non concernée. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

Le décodage applique les mêmes validations strictes :

- clés exactes ;
- types exacts ;
- identifiants stables ;
- révision positive ;
- tick non négatif ;
- deltas dans les bornes d’une commande.

> **[VSC] Visual Studio Code — Ajouter à `social_relationship_snapshot_codec.gd`.**

```gdscript
func _decode_record(payload: Variant) -> SocialChangeRecord:
	if not payload is Dictionary:
		return null

	var data := payload as Dictionary
	var required: Array[String] = [
		"revision",
		"logical_tick",
		"cause_id",
		"source_system",
		"context_id",
		"deltas",
	]
	if not _has_exact_keys(data, required):
		return null

	if not data["revision"] is int:
		return null
	if not data["logical_tick"] is int:
		return null
	if not data["cause_id"] is String:
		return null
	if not data["source_system"] is String:
		return null
	if not data["context_id"] is String:
		return null
	if not data["deltas"] is Dictionary:
		return null

	var deltas := _decode_delta_dictionary(data["deltas"])
	if deltas.is_empty():
		return null

	var record := SocialChangeRecord.new()
	record.revision = data["revision"]
	record.logical_tick = data["logical_tick"]
	record.cause_id = StringName(data["cause_id"])
	record.source_system = StringName(data["source_system"])
	record.context_id = StringName(data["context_id"])
	record.affinity_delta = deltas["affinity"]
	record.trust_delta = deltas["trust"]
	record.respect_delta = deltas["respect"]
	record.fear_delta = deltas["fear"]

	if record.validate() != OK:
		return null
	return record

func _decode_delta_dictionary(payload: Variant) -> Dictionary:
	if not payload is Dictionary:
		return {}

	var data := payload as Dictionary
	var keys: Array[String] = [
		"affinity",
		"trust",
		"respect",
		"fear",
	]
	if not _has_exact_keys(data, keys):
		return {}

	for key: String in keys:
		if not data[key] is int:
			return {}

	return {
		"affinity": data["affinity"],
		"trust": data["trust"],
		"respect": data["respect"],
		"fear": data["fear"],
	}
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Fonctions, paramètres et retours :** `_decode_record(payload: Variant) -> SocialChangeRecord` est une méthode qui encapsule l’opération métier indiquée par son nom ; `_decode_delta_dictionary(payload: Variant) -> Dictionary` est une méthode qui encapsule l’opération métier indiquée par son nom.
- **Données et types :** variables `data := payload as Dictionary`, `required: Array[String] = [`, `deltas := _decode_delta_dictionary(data["deltas"])`, `record := SocialChangeRecord.new()`, `data := payload as Dictionary`, `keys: Array[String] = [`. Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les transitions utilisent des ticks logiques cohérents.
- **Résultat attendu et vérification :** observer le comportement décrit par la section sans modifier de donnée autoritaire non concernée. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

## 26. Section de sauvegarde indépendante

> **[VSC] Visual Studio Code — Créer : `res://src/features/social/infrastructure/social_relationship_save_section.gd`.**

```gdscript
class_name SocialRelationshipSaveSection
extends SaveSection

const SECTION_ID: StringName = &"social_relationships"
const FORMAT_VERSION := 1

var _repository: SocialRelationshipRepository
var _character_index: CharacterIdentityIndex
var _codec := SocialRelationshipSnapshotCodec.new()
var _prepared_states: Array[SocialRelationshipState] = []
var _has_prepared_load := false

func _init(
	repository: SocialRelationshipRepository,
	character_index: CharacterIdentityIndex,
) -> void:
	_repository = repository
	_character_index = character_index

func get_section_id() -> StringName:
	return SECTION_ID

func capture() -> Dictionary:
	if _repository == null:
		return {}

	var entries: Array[Dictionary] = []
	for state: SocialRelationshipState in _repository.get_all():
		var payload := _codec.encode(state)
		if payload.is_empty():
			return {}
		entries.append(payload)

	return {
		"format_version": FORMAT_VERSION,
		"entries": entries,
	}

func prepare_load(payload: Variant) -> Error:
	_prepared_states.clear()
	_has_prepared_load = false

	if _character_index == null:
		return ERR_UNCONFIGURED

	if not payload is Dictionary:
		return ERR_INVALID_DATA

	var data := payload as Dictionary
	if data.size() != 2:
		return ERR_INVALID_DATA
	if not data.has("format_version") or not data.has("entries"):
		return ERR_INVALID_DATA
	if not data["format_version"] is int:
		return ERR_INVALID_DATA
	if data["format_version"] != FORMAT_VERSION:
		return ERR_INVALID_DATA
	if not data["entries"] is Array:
		return ERR_INVALID_DATA

	var candidate: Array[SocialRelationshipState] = []
	var seen: Dictionary[String, bool] = {}

	for entry: Variant in data["entries"]:
		var state := _codec.decode(entry)
		if state == null:
			return ERR_INVALID_DATA

		if not _character_index.contains(state.key.source_id):
			return ERR_DOES_NOT_EXIST
		if not _character_index.contains(state.key.target_id):
			return ERR_DOES_NOT_EXIST

		var storage_key := state.key.to_storage_key()
		if seen.has(storage_key):
			return ERR_ALREADY_EXISTS

		seen[storage_key] = true
		candidate.append(state)

	_prepared_states = candidate
	_has_prepared_load = true
	return OK

func apply_prepared() -> Error:
	if _repository == null:
		return ERR_UNCONFIGURED
	if not _has_prepared_load:
		return ERR_INVALID_DATA

	var result := _repository.replace_all(_prepared_states)
	if result == OK:
		_prepared_states.clear()
		_has_prepared_load = false
	return result

func cancel_load() -> void:
	_prepared_states.clear()
	_has_prepared_load = false
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc définit le contrat `SocialRelationshipSaveSection` et l’appuie sur `SaveSection`.
- **Fonctions, paramètres et retours :** `_init(repository: SocialRelationshipRepository, character_index: CharacterIdentityIndex,) -> void` est une méthode qui initialise l’objet et copie les arguments dans son état interne ; `get_section_id(aucun paramètre) -> StringName` est une méthode qui lit ou calcule une vue des données sans exposer directement les collections internes ; `capture(aucun paramètre) -> Dictionary` est une méthode qui encapsule l’opération métier indiquée par son nom ; `prepare_load(payload: Variant) -> Error` est une méthode qui encapsule l’opération métier indiquée par son nom ; `apply_prepared(aucun paramètre) -> Error` est une méthode qui valide puis ajoute ou applique une mutation métier ; `cancel_load(aucun paramètre) -> void` est une méthode qui encapsule l’opération métier indiquée par son nom.
- **Données et types :** constantes `SECTION_ID: StringName = &"social_relationships"`, `FORMAT_VERSION := 1` ; variables `_repository: SocialRelationshipRepository`, `_character_index: CharacterIdentityIndex`, `_codec := SocialRelationshipSnapshotCodec.new()`, `_prepared_states: Array[SocialRelationshipState] = []`, `_has_prepared_load := false`, `entries: Array[Dictionary] = []` et 7 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les branches `if` traitent d’abord les refus et cas limites ; les boucles `for` parcourent explicitement les collections ; les retours anticipés empêchent la suite du traitement après une erreur. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** ajoute une entrée à une collection ou à un historique ; retire ou réinitialise des données en mémoire. L’appelant ne doit considérer l’opération réussie qu’après le retour de succès.
- **Invariants protégés :** un candidat complet est validé avant mutation de l’état actif.
- **Résultat attendu et vérification :** obtenir `OK` pour le cas valide et un code `Error` documenté pour chaque refus, sans mutation partielle. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

La section sociale est indépendante de la section des personnages.

Le coordinateur de sauvegarde doit préparer toutes les sections avant d’en appliquer une seule. La section des personnages doit être préparée avant la section sociale afin que l’index d’identités candidat puisse valider les références.

L’assemblage transactionnel entre sections reste une responsabilité du coordinateur du chapitre 9.

## 27. Ordre de restauration

> **[LECTURE] Ordre logique de préparation — Ne pas saisir.**

```text
1. décoder les personnages
2. construire l’index candidat des identités
3. décoder les relations sociales contre cet index
4. préparer les autres systèmes
5. appliquer toutes les sections
```

Le dépôt social courant n’est pas consulté pour valider une sauvegarde future. La validation doit utiliser les identités du snapshot en cours de préparation.

## 28. Démonstration pédagogique

> **[APP] Godot — Créer la scène `res://scenes/learning/ch15_social_relationships_demo.tscn`.**

Arbre minimal :

> **[SORTIE] Arbre attendu dans le dock Scene — Ne pas saisir.**

```text
Ch15SocialRelationshipsDemo (Node)
└── DemoOutput (RichTextLabel)
```

> **[VSC] Visual Studio Code — Créer : `res://scenes/learning/ch15_social_relationships_demo.gd`.**

```gdscript
extends Node

@onready var _output: RichTextLabel = %DemoOutput

var _repository := InMemorySocialRelationshipRepository.new()
var _character_index := DemoCharacterIdentityIndex.new()
var _service := SocialRelationshipService.new(
	_repository,
	_character_index,
)
var _query := SocialRelationshipQuery.new(_repository)

func _ready() -> void:
	_service.relationship_changed.connect(_on_relationship_changed)

	var command := ChangeSocialRelationshipCommand.new()
	command.relationship_key = SocialRelationshipKey.new(
		&"chr_01jz8r5d2w4f8m1k3n6p9q0s7t",
		&"chr_01jz8r6ab8d1e4g7h2k5m9p3qr",
	)
	command.cause = SocialChangeCause.new(
		&"social.cause.promise.kept",
		&"system.social.demo",
	)
	command.affinity_delta = 10
	command.trust_delta = 15
	command.respect_delta = 5
	command.logical_tick = 120

	var result := _service.apply_change(command)
	_output.append_text("Résultat : %s\n" % error_string(result))

func _on_relationship_changed(
	event: SocialRelationshipChangedEvent,
) -> void:
	_output.append_text(
		"%s → %s | confiance %d → %d\n"
		% [
			event.source_id,
			event.target_id,
			event.before_axes.trust,
			event.after_axes.trust,
		]
	)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Fonctions, paramètres et retours :** `_ready(aucun paramètre) -> void` est une méthode qui encapsule l’opération métier indiquée par son nom ; `_on_relationship_changed(event: SocialRelationshipChangedEvent,) -> void` est une méthode qui encapsule l’opération métier indiquée par son nom.
- **Données et types :** variables `_output: RichTextLabel = %DemoOutput`, `_repository := InMemorySocialRelationshipRepository.new()`, `_character_index := DemoCharacterIdentityIndex.new()`, `_service := SocialRelationshipService.new(`, `_query := SocialRelationshipQuery.new(_repository)`, `command := ChangeSocialRelationshipCommand.new()` et 1 autre(s). Une valeur d’énumération ferme le vocabulaire autorisé ; une constante documente une borne ou une sentinelle ; une variable porte l’état courant.
- **Déroulement :** les instructions s’exécutent de haut en bas et construisent ou transforment une valeur locale. L’ordre est important : les validations doivent précéder toute écriture ou émission d’événement.
- **Effets de bord :** le bloc est déclaratif ou calculatoire ; il ne doit pas altérer une collection appartenant à l’appelant, un nœud actif ou une `Resource` partagée.
- **Invariants protégés :** les transitions utilisent des ticks logiques cohérents.
- **Résultat attendu et vérification :** observer le comportement décrit par la section sans modifier de donnée autoritaire non concernée. Vérifie au minimum un cas nominal, une limite et un refus, puis confirme que l’état reste inchangé après l’échec.

La démonstration vérifie seulement le flux applicatif. Elle ne constitue pas un test de sauvegarde, de migration ou de charge.

## 29. Mode Solo et Mode Studio

### 29.1 Mode Solo

Le parcours Solo peut utiliser :

- un dépôt en mémoire ;
- quatre axes fixes ;
- un historique de `32` entrées ;
- une section JSON ;
- une vue mutuelle calculée à la demande ;
- une validation au chargement.

### 29.2 Mode Studio

Le parcours Studio ajoute :

- un catalogue versionné de causes ;
- une revue des conventions d’axes ;
- des budgets par zone ou par personnage ;
- des outils de visualisation du graphe social ;
- des tests de migrations ;
- des métriques de distribution ;
- une politique de conservation des historiques ;
- des contrôles de cohérence entre systèmes ;
- une documentation des sources de chaque mutation.

Le Studio ne doit pas introduire une base de données uniquement parce que le système porte le mot « graphe ». Le choix dépend des volumes et des requêtes mesurés.

## 30. Budgets et complexité

Avec `N` personnages, toutes les paires possibles produisent `N × (N - 1)` directions.

Pour `1 000` personnages, cela représente `999 000` relations possibles.

Le système ne crée donc une relation qu’au premier changement pertinent ou lorsqu’une définition de départ l’exige.

Les budgets recommandés pour le prototype sont :

| Élément | Budget pédagogique |
|---|---:|
| historique par direction | `32` |
| deltas par commande | `-100` à `100` |
| axes persistés | `4` |
| relations initialisées | uniquement celles qui existent |
| résultats d’interface | pagination ou limite explicite |
| mutations par événement mondial | lot borné et observé |

## 31. Déterminisme

Le système social utilise :

- un tick logique ;
- des deltas entiers ;
- un ordre de sauvegarde déterministe ;
- des clés orientées stables ;
- des tris explicites pour les listes.

Il n’utilise pas directement :

- `Time.get_unix_time_from_system()` comme autorité ;
- un nombre aléatoire pendant l’application d’une commande ;
- l’ordre non documenté des nœuds dans la scène ;
- le nom affiché d’un personnage.

Une règle de décroissance temporelle, si elle est ajoutée plus tard, doit consommer le temps de simulation et non l’horloge du poste.

## 32. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 32.1 Stocker la relation sur le nœud du personnage

**Symptôme ou risque :** la relation disparaît lorsque le nœud est déchargé.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
extends CharacterBody3D
var affinity_by_node: Dictionary[Node, int] = {}
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** la relation disparaît lorsque le nœud est déchargé.

**Correction :** utiliser des identifiants stables dans un dépôt indépendant.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
var key := SocialRelationshipKey.new(source_id, target_id)
var state := repository.get_state(source_id, target_id)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** utiliser des identifiants stables dans un dépôt indépendant. le second exemple survit au déchargement des scènes.

**Différence :** le second exemple survit au déchargement des scènes.

### 32.2 Utiliser le nom affiché comme clé

> **À relire :** [§ 6. Identifier une relation dirigée](#6-identifier-une-relation-dirigee).

**Symptôme ou risque :** un renommage ou une traduction casse la relation.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
relations["Aster->Brann"] = 50
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** un renommage ou une traduction casse la relation.

**Correction :** employer deux `CharacterId`.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
var key := SocialRelationshipKey.new(aster_id, brann_id)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** employer deux `CharacterId`. l’identité n’est plus liée au texte affiché.

**Différence :** l’identité n’est plus liée au texte affiché.

### 32.3 Forcer une relation symétrique

> **À relire :** [§ 4.1 Une relation est dirigée](#41-une-relation-est-dirigee).

**Symptôme ou risque :** les perceptions divergentes sont écrasées.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
set_affinity(a, b, value)
set_affinity(b, a, value)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** les perceptions divergentes sont écrasées.

**Correction :** appliquer une commande distincte par direction.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
service.apply_change(command_a_to_b)
service.apply_change(command_b_to_a)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** appliquer une commande distincte par direction. chaque direction conserve sa cause et sa valeur.

**Différence :** chaque direction conserve sa cause et sa valeur.

### 32.4 Stocker `is_friend` séparément

**Symptôme ou risque :** le booléen contredit les axes.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
state.is_friend = true
state.axes.affinity = -80
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** le booléen contredit les axes.

**Correction :** calculer une vue selon une règle documentée.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
var view := query.get_mutual_view(first_id, second_id)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** calculer une vue selon une règle documentée. la vue reste dérivée des données d’autorité.

**Différence :** la vue reste dérivée des données d’autorité.

### 32.5 Laisser les axes hors limites

> **À relire :** [§ 7. Représenter les axes sociaux](#7-representer-les-axes-sociaux).

**Symptôme ou risque :** l’équilibrage et l’interface reçoivent des valeurs imprévues.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
state.axes.trust += 500
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** l’équilibrage et l’interface reçoivent des valeurs imprévues.

**Correction :** passer par `apply_delta()`.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
state.axes.apply_delta(0, 500, 0, 0)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** passer par `apply_delta()`. la confiance est bornée à `100`.

**Différence :** la confiance est bornée à `100`.

### 32.6 Accepter une commande sans cause

> **À relire :** [§ 9. Commander un changement social](#9-commander-un-changement-social).

**Symptôme ou risque :** le changement devient impossible à expliquer.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
command.cause = null
service.apply_change(command)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** le changement devient impossible à expliquer.

**Correction :** fournir une cause stable et une provenance.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
command.cause = SocialChangeCause.new(
	&"social.cause.rescue",
	&"system.world.event",
)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** fournir une cause stable et une provenance. l’historique possède une origine vérifiable.

**Différence :** l’historique possède une origine vérifiable.

### 32.7 Utiliser l’heure système comme ordre de simulation

**Symptôme ou risque :** deux machines ou relectures produisent un ordre différent.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
command.logical_tick = int(Time.get_unix_time_from_system())
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** deux machines ou relectures produisent un ordre différent.

**Correction :** injecter le tick logique de la simulation.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
command.logical_tick = simulation_clock.current_tick
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** injecter le tick logique de la simulation. l’ordre dépend de la partie, pas de l’ordinateur.

**Différence :** l’ordre dépend de la partie, pas de l’ordinateur.

### 32.8 Conserver un historique illimité

> **À relire :** [§ 23. Restaurer l’historique sans exposer la collection](#23-restaurer-lhistorique-sans-exposer-la-collection).

**Symptôme ou risque :** la sauvegarde grossit sans borne.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
_history.append(record)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** la sauvegarde grossit sans borne.

**Correction :** retirer les entrées les plus anciennes.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
_history.append(record)
while _history.size() > MAX_HISTORY:
	_history.pop_front()
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** retirer les entrées les plus anciennes. la taille maximale est explicite.

**Différence :** la taille maximale est explicite.

### 32.9 Retourner le tableau interne

> **À relire :** [§ 12. Dépôt de relations](#12-depot-de-relations).

**Symptôme ou risque :** un appelant modifie l’historique sans validation.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
func get_history() -> Array:
	return _history
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** un appelant modifie l’historique sans validation.

**Correction :** retourner une copie.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
func get_history_copy() -> Array[SocialChangeRecord]:
	return _history.duplicate()
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** retourner une copie. le tableau interne reste encapsulé.

**Différence :** le tableau interne reste encapsulé.

### 32.10 Parcourir tous les nœuds pour trouver les voisins

> **À relire :** [§ 17. Requêtes de voisinage](#17-requetes-de-voisinage).

**Symptôme ou risque :** les personnages hors scène sont ignorés.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
for node in get_tree().get_nodes_in_group("characters"):
	find_relationship(node)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** les personnages hors scène sont ignorés.

**Correction :** interroger l’index du dépôt.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
var outgoing := repository.get_outgoing(source_id)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** interroger l’index du dépôt. la requête porte sur les données du monde.

**Différence :** la requête porte sur les données du monde.

### 32.11 Créer toutes les paires possibles

**Symptôme ou risque :** la mémoire croît en `N²` sans utilité.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
for source in all_characters:
	for target in all_characters:
		create_relation(source, target)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** la mémoire croît en `N²` sans utilité.

**Correction :** créer une relation au premier événement pertinent.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
var state := repository.get_state(source_id, target_id)
if state == null:
	state = SocialRelationshipState.new(command.relationship_key)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** créer une relation au premier événement pertinent. seules les relations existantes occupent de la mémoire.

**Différence :** seules les relations existantes occupent de la mémoire.

### 32.12 Décoder avec des conversions silencieuses

> **À relire :** [§ 24. Encoder et décoder les axes](#24-encoder-et-decoder-les-axes).

**Symptôme ou risque :** une chaîne `"20"` devient un entier sans contrat clair.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
axes.trust = int(data["trust"])
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** une chaîne `"20"` devient un entier sans contrat clair.

**Correction :** vérifier le type exact avant affectation.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
if not data["trust"] is int:
	return null
axes.trust = data["trust"]
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** vérifier le type exact avant affectation. une sauvegarde invalide est refusée.

**Différence :** une sauvegarde invalide est refusée.

### 32.13 Appliquer avant validation complète

> **À relire :** [§ 27. Ordre de restauration](#27-ordre-de-restauration).

**Symptôme ou risque :** une relation valide est remplacée avant la découverte d’une entrée corrompue.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
for entry in entries:
	repository.add(codec.decode(entry))
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** une relation valide est remplacée avant la découverte d’une entrée corrompue.

**Correction :** préparer un tableau candidat puis appeler `replace_all()`.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
var prepare_error := section.prepare_load(payload)
if prepare_error == OK:
	section.apply_prepared()
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** préparer un tableau candidat puis appeler `replace_all()`. aucune mutation ne précède la validation globale de la section.

**Différence :** aucune mutation ne précède la validation globale de la section.

### 32.14 Valider contre les seuls personnages actifs

**Symptôme ou risque :** une relation vers un personnage hors zone est supprimée.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
if active_registry.get_actor(target_id) == null:
	return ERR_DOES_NOT_EXIST
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** une relation vers un personnage hors zone est supprimée.

**Correction :** consulter l’index logique des identités.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
if not character_identity_index.contains(target_id):
	return ERR_DOES_NOT_EXIST
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** consulter l’index logique des identités. la présence visuelle n’est pas confondue avec l’existence.

**Différence :** la présence visuelle n’est pas confondue avec l’existence.

### 32.15 Mélanger famille et relation sociale

> **À relire :** [§ 14. Événement social typé](#14-evenement-social-type).

**Symptôme ou risque :** une baisse d’affinité efface un lien de parenté.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
state.is_parent = state.axes.affinity > 50
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** une baisse d’affinité efface un lien de parenté.

**Correction :** garder la parenté dans le système du chapitre 16.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
var kinship := family_query.get_relationship(first_id, second_id)
var social := social_query.get_mutual_view(first_id, second_id)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** garder la parenté dans le système du chapitre 16. le fait familial et la perception sociale restent indépendants.

**Différence :** le fait familial et la perception sociale restent indépendants.

### 32.16 Utiliser l’IA comme autorité de la relation

> **À relire :** [§ 14. Événement social typé](#14-evenement-social-type).

**Symptôme ou risque :** une réponse non déterministe modifie directement l’état persistant.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```gdscript
state.axes.trust = ai_response["trust"]
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi cet exemple est fautif :** une réponse non déterministe modifie directement l’état persistant.

**Correction :** convertir une décision autorisée en commande bornée et traçable.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
var command := policy.map_suggestion_to_command(ai_suggestion)
var result := social_service.apply_change(command)
```
<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Pourquoi la correction fonctionne :** convertir une décision autorisée en commande bornée et traçable. le domaine valide la mutation et peut refuser la suggestion.

**Différence :** le domaine valide la mutation et peut refuser la suggestion.

## 33. Checklist de réalisation

- [ ] `SocialRelationshipKey` refuse l’auto-relation.
- [ ] Les deux identifiants utilisent `CharacterId`.
- [ ] Les axes respectent leurs bornes.
- [ ] Une commande sans effet est refusée.
- [ ] Chaque changement possède cause et provenance.
- [ ] Le tick logique ne recule pas.
- [ ] L’historique est borné.
- [ ] Le dépôt indexe les relations sortantes.
- [ ] Les personnages hors scène restent valides.
- [ ] Les événements transportent des copies.
- [ ] Une vue mutuelle exige les deux directions.
- [ ] Le snapshot refuse les types approximatifs.
- [ ] Les clés JSON sont contrôlées.
- [ ] Les références de personnages sont validées.
- [ ] La section prépare toutes les entrées avant application.
- [ ] Les liens familiaux restent hors du système.
- [ ] Aucun PDF intermédiaire n’est produit.

## 34. Critères d’acceptation

Le chapitre est acceptable au niveau documentaire lorsque :

1. une relation dirigée peut être identifiée sans nom affiché ;
2. deux directions divergentes peuvent coexister ;
3. les quatre axes restent bornés ;
4. chaque mutation possède une cause ;
5. l’historique ne dépasse jamais sa limite ;
6. une relation persiste sans nœud actif ;
7. les requêtes retournent des identifiants stables ;
8. la vue mutuelle distingue absence et neutralité ;
9. le snapshot ne contient ni nœud ni ressource ;
10. une entrée invalide empêche toute application ;
11. les frontières avec les chapitres 16, 17, 20, 23 et 25 restent explicites ;
12. le rapport d’audit post-création documente les réserves runtime.

## 35. Tests à préparer

Le chapitre 27 devra notamment couvrir :

- deux directions indépendantes ;
- refus d’une auto-relation ;
- refus d’un personnage inconnu ;
- bornage de chaque axe ;
- commande sans effet ;
- delta excessif ;
- tick décroissant ;
- ordre des révisions ;
- historique limité à `32` ;
- vue mutuelle complète et incomplète ;
- création paresseuse ;
- remplacement atomique du dépôt ;
- snapshot avec type invalide ;
- snapshot avec clé inconnue ;
- doublon de relation ;
- référence vers un personnage absent du snapshot ;
- déterminisme de l’ordre sérialisé ;
- restauration après sauvegarde.

## 36. Réserves runtime

Ce chapitre reste au niveau `static-review`.

Ne sont pas exécutés ici :

- le parseur GDScript de Godot `4.7.1-stable` ;
- l’instanciation de la scène de démonstration ;
- les signaux en runtime ;
- le coordinateur transactionnel de sauvegarde ;
- une migration depuis une ancienne section sociale ;
- les performances avec plusieurs centaines de milliers de relations ;
- les lots d’événements mondiaux ;
- la concurrence ou le multijoueur ;
- le packaging multi-plateforme ;
- la compilation PDF de fin de Livre.

## 37. Résumé

Le système social de `Project Asteria` repose sur des relations dirigées entre identifiants stables.

Chaque relation contient :

- quatre axes bornés ;
- une révision ;
- un tick logique ;
- un historique causal borné.

Le dépôt :

- ne dépend pas des scènes ;
- indexe les relations sortantes ;
- crée un candidat lors du premier changement pertinent ;
- remplace les données après validation.

Les vues mutuelles sont calculées. Les relations familiales, factions et réputations restent dans leurs systèmes propres.

## 38. Sources techniques

- [Godot 4.7 — `StringName`](https://docs.godotengine.org/en/4.7/classes/class_stringname.html)
- [Godot 4.7 — `Dictionary`](https://docs.godotengine.org/en/4.7/classes/class_dictionary.html)
- [Godot 4.7 — `Array`](https://docs.godotengine.org/en/4.7/classes/class_array.html)
- [Godot 4.7 — `Signal`](https://docs.godotengine.org/en/4.7/classes/class_signal.html)
- [Godot 4.7 — utilisation des signaux](https://docs.godotengine.org/en/4.7/getting_started/step_by_step/signals.html)
- [Godot 4.7 — `RefCounted`](https://docs.godotengine.org/en/4.7/classes/class_refcounted.html)
- [Godot 4.7 — `Resource`](https://docs.godotengine.org/en/4.7/classes/class_resource.html)
- [Godot 4.7 — `JSON`](https://docs.godotengine.org/en/4.7/classes/class_json.html)
- [Godot 4.7 — `Variant`](https://docs.godotengine.org/en/4.7/classes/class_variant.html)
- [Godot 4.7 — codes `Error`](https://docs.godotengine.org/en/4.7/classes/class_@globalscope.html#enum-globalscope-error)
- [Godot 4.7 — fonctions `clampi`, `mini` et `maxi`](https://docs.godotengine.org/en/4.7/classes/class_@globalscope.html)
- [Godot 4.7 — `Time`](https://docs.godotengine.org/en/4.7/classes/class_time.html)
- [Godot 4.7 — types fondamentaux du moteur](https://docs.godotengine.org/en/4.7/engine_details/architecture/core_types.html)
- [Godot 4.7 — classes, scènes et responsabilités](https://docs.godotengine.org/en/4.7/tutorials/best_practices/what_are_godot_classes.html)
- [Chapitre 14 — Personnages](CHAPITRE-14-Personnages.md)
