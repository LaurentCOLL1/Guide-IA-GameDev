---
title: "Livre II — Chapitre 25 : Narration, quêtes, codex et connaissances"
id: "DOC-L2-CH25"
status: "reviewed"
version: "1.0.1"
lang: "fr-FR"
book: "Livre II"
chapter: 25
last-verified: "2026-07-21T14:38:26+02:00"
audit-status: "complete"
audit-date: "2026-07-21T14:38:26+02:00"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-25.md"
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

# Narration, quêtes, codex et connaissances

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH25`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  

> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-25.md`.
> **Explications de code :** structurées bloc par bloc ; les informations pédagogiques antérieures sont conservées dans des rubriques explicites, complétées seulement lorsque le bloc l’exige.

## 1. Rôle du chapitre

Les systèmes précédents produisent des faits autoritaires : personnages créés, relations modifiées, combats résolus, objets transférés, transactions committées, régions simulées, verdicts rendus et bâtiments achevés. Une narration robuste ne remplace aucun de ces faits. Elle les observe, les qualifie et les organise en arcs, quêtes, objectifs, conséquences et connaissances découvertes.

Ce chapitre construit la couche narrative de `Project Asteria`. Elle possède les identités narratives, les définitions d’arcs et de quêtes, les instances de progression, les conditions, les conséquences préparées, le codex et les connaissances découvertes. Elle ne possède ni la santé, ni les objets, ni les monnaies, ni les lois, ni les domaines.

Les invariants centraux sont : un fait source reste distinct de son interprétation ; une quête n’est jamais validée par un texte affiché ; une conséquence externe est préparée par l’autorité propriétaire ; une connaissance découverte n’est pas une vérité universelle ; une sortie IA reste consultative.

## 2. Prérequis

Le lecteur doit maîtriser l’architecture feature-first, les services et ports, les identifiants stables, les sauvegardes préparées, les agents et les événements des chapitres 14 à 24. Le chapitre 10 reste pertinent pour distinguer corpus documentaire et mémoire vectorielle dérivée.

## 3. Périmètre et frontières

Le chapitre couvre les faits narratifs normalisés, arcs, quêtes, objectifs, conditions, conséquences, codex, connaissances découvertes, visibilité, journal du joueur, idempotence, événements et persistance.

Il ne couvre pas l’écriture d’outils d’édition, les pipelines de contenu, la génération industrielle de données, les dialogues complets, la mise en scène cinématique, le multijoueur ni l’équilibrage final. Ces sujets seront traités ultérieurement.

> **Frontière essentielle :** la narration orchestre des décisions déjà autorisées ; elle ne devient jamais propriétaire des états de gameplay qu’elle observe ou qu’elle demande de modifier.

## 4. Chaîne d’autorité narrative

> **[LECTURE] Exemple de référence — Ne pas saisir.**

```text
GameplayEvent
    ↓ normalisation
NarrativeFact
    ↓ règles déterministes
Arc / Quest / Objective evaluation
    ↓ préparation
NarrativeMutationCandidate + ExternalEffectCandidates
    ↓ commit commun
State replacement + events + journal
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** Le flux distingue le fait source, son adaptation narrative, l’évaluation et le commit. Un événement reçu n’est pas appliqué deux fois : son identité et son empreinte sont enregistrées avec le résultat durable.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

## 5. Organisation feature-first

> **[LECTURE] Exemple de référence — Ne pas saisir.**

```text
src/features/narrative/
├── domain/
├── application/
├── infrastructure/
└── presentation/
data/narrative/
scenes/learning/ch25_narrative_demo.tscn
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Persistance et restauration :** Les définitions de contenu restent sous `data/narrative`, les états vivants dans le domaine, les orchestrations dans l’application, les codecs dans l’infrastructure et l’affichage dans la présentation.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

## 6. Identités narratives stables

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name NarrativeFactId
extends RefCounted

var fact_: StringName
var revision: int = 0

func is_valid() -> bool:
    return not fact_.is_empty() and revision >= 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** Un fait narratif possède une identité indépendante de son texte, de son ordre d’affichage et de son événement source. `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Rôle précis du bloc :** Le bloc définit `NarrativeFactId` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `NarrativeFactId` et les fonctions `is_valid()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `fact_: StringName`, `revision: int`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `not fact_.is_empty() and revision >= 0`.

## 7. Faits narratifs normalisés

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name NarrativeFact
extends RefCounted

var source_event_id: StringName
var revision: int = 0

func is_valid() -> bool:
    return not source_event_id.is_empty() and revision >= 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Le fait conserve type, sujet, objet, tick, provenance et payload borné sans copier un nœud ou un objet métier mutable. `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Rôle précis du bloc :** Le bloc définit `NarrativeFact` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `NarrativeFact` et les fonctions `is_valid()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `source_event_id: StringName`, `revision: int`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `not source_event_id.is_empty() and revision >= 0`.

## 8. Définitions d’arcs

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name NarrativeArcDefinition
extends RefCounted

var arc_id: StringName
var revision: int = 0

func is_valid() -> bool:
    return not arc_id.is_empty() and revision >= 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Un arc regroupe des quêtes et des transitions de haut niveau sans stocker leur progression runtime dans la `Resource`. `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Rôle précis du bloc :** Le bloc définit `NarrativeArcDefinition` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `NarrativeArcDefinition` et les fonctions `is_valid()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `arc_id: StringName`, `revision: int`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `not arc_id.is_empty() and revision >= 0`.

## 9. Définitions de quêtes

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name QuestDefinition
extends RefCounted

var quest_id: StringName
var revision: int = 0

func is_valid() -> bool:
    return not quest_id.is_empty() and revision >= 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Une quête de conception déclare préconditions, objectifs, règles d’échec et conséquences, mais aucun état joueur. `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Rôle précis du bloc :** Le bloc définit `QuestDefinition` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `QuestDefinition` et les fonctions `is_valid()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `quest_id: StringName`, `revision: int`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `not quest_id.is_empty() and revision >= 0`.

## 10. Objectifs typés

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name QuestObjectiveDefinition
extends RefCounted

var objective_id: StringName
var revision: int = 0

func is_valid() -> bool:
    return not objective_id.is_empty() and revision >= 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Les objectifs utilisent des types fermés et des paramètres validés ; aucun script ou nom de méthode ne provient des données. `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Rôle précis du bloc :** Le bloc définit `QuestObjectiveDefinition` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `QuestObjectiveDefinition` et les fonctions `is_valid()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `objective_id: StringName`, `revision: int`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `not objective_id.is_empty() and revision >= 0`.

## 11. Conditions composables

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name NarrativeCondition
extends RefCounted

var condition_type: StringName
var revision: int = 0

func is_valid() -> bool:
    return not condition_type.is_empty() and revision >= 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Une condition est évaluée par un registre de stratégies autorisées, jamais par `eval` ni par chargement dynamique. `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Rôle précis du bloc :** Le bloc définit `NarrativeCondition` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `NarrativeCondition` et les fonctions `is_valid()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `condition_type: StringName`, `revision: int`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `not condition_type.is_empty() and revision >= 0`.

## 12. Conséquences préparées

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name NarrativeConsequenceDefinition
extends RefCounted

var effect_type: StringName
var revision: int = 0

func is_valid() -> bool:
    return not effect_type.is_empty() and revision >= 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** Une conséquence décrit une demande ; l’autorité externe prépare le candidat réel et peut refuser. `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Rôle précis du bloc :** Le bloc définit `NarrativeConsequenceDefinition` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `NarrativeConsequenceDefinition` et les fonctions `is_valid()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `effect_type: StringName`, `revision: int`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `not effect_type.is_empty() and revision >= 0`.

## 13. Entrées de codex

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name CodexEntryDefinition
extends RefCounted

var entry_id: StringName
var revision: int = 0

func is_valid() -> bool:
    return not entry_id.is_empty() and revision >= 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Le codex sépare contenu éditorial, règles de visibilité et état de découverte. `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Rôle précis du bloc :** Le bloc définit `CodexEntryDefinition` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `CodexEntryDefinition` et les fonctions `is_valid()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `entry_id: StringName`, `revision: int`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `not entry_id.is_empty() and revision >= 0`.

## 14. Connaissances découvertes

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name DiscoveredKnowledgeState
extends RefCounted

var knowledge_id: StringName
var revision: int = 0

func is_valid() -> bool:
    return not knowledge_id.is_empty() and revision >= 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Une connaissance est relative à un détenteur, une source et un niveau de confiance ; elle ne devient pas automatiquement un fait global. `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Rôle précis du bloc :** Le bloc définit `DiscoveredKnowledgeState` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `DiscoveredKnowledgeState` et les fonctions `is_valid()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `knowledge_id: StringName`, `revision: int`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `not knowledge_id.is_empty() and revision >= 0`.

## 15. États runtime des arcs et quêtes

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name QuestRuntimeState
extends RefCounted

enum Status { LOCKED, AVAILABLE, ACTIVE, SUCCEEDED, FAILED, CANCELLED }

var quest_id: StringName
var owner_id: StringName
var status: Status = Status.LOCKED
var objective_progress: Dictionary[StringName, int] = {}
var started_tick: int = -1
var ended_tick: int = -1
var revision: int = 0

func duplicate_detached() -> QuestRuntimeState:
    var copy := QuestRuntimeState.new()
    copy.quest_id = quest_id
    copy.owner_id = owner_id
    copy.status = status
    copy.objective_progress = objective_progress.duplicate(true)
    copy.started_tick = started_tick
    copy.ended_tick = ended_tick
    copy.revision = revision
    return copy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** L’état runtime est séparé de `QuestDefinition`. La copie profonde du dictionnaire empêche un candidat de partager une collection mutable avec l’état actif.

- **Rôle précis du bloc :** Le bloc définit `QuestRuntimeState` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `QuestRuntimeState` et les fonctions `duplicate_detached()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `quest_id: StringName`, `owner_id: StringName`, `status: Status`, `objective_progress: Dictionary[StringName, int]`, `started_tick: int`, `ended_tick: int`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `QuestRuntimeState` ; branches visibles : `copy`.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `copy.quest_id = quest_id`, `copy.owner_id = owner_id`, `copy.status = status`, `copy.objective_progress = objective_progress.duplicate(true)`, `copy.started_tick = started_tick`.

## 16. Progression entière et bornée

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
const PROGRESS_SCALE := 10000

static func add_progress(current: int, delta: int) -> int:
    if current < 0 or current > PROGRESS_SCALE:
        return -1
    if delta < 0:
        return -1
    return mini(PROGRESS_SCALE, current + delta)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** La progression utilise des points de base entiers. La sentinelle `-1` distingue un état invalide d’une progression légitime à zéro.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `add_progress()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `add_progress()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `current: int, delta`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `int` ; branches visibles : `-1`, `mini(PROGRESS_SCALE, current + delta)`.

## 17. Registre des évaluateurs de conditions

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name NarrativeConditionRegistry
extends RefCounted

var _evaluators: Dictionary[StringName, NarrativeConditionEvaluator] = {}

func register(type_id: StringName, evaluator: NarrativeConditionEvaluator) -> Error:
    if type_id.is_empty() or evaluator == null or _evaluators.has(type_id):
        return ERR_INVALID_PARAMETER
    _evaluators[type_id] = evaluator
    return OK

func evaluate(condition: NarrativeCondition, context: NarrativeEvaluationContext) -> NarrativeDecision:
    var evaluator: NarrativeConditionEvaluator = _evaluators.get(condition.condition_type)
    if evaluator == null:
        return NarrativeDecision.indeterminate(&"unknown_condition_type")
    return evaluator.evaluate(condition, context)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** Le registre ferme l’ensemble des stratégies exécutables. Une condition inconnue produit `INDETERMINATE`, jamais une autorisation implicite.

- **Rôle précis du bloc :** Le bloc définit `NarrativeConditionRegistry` et expose son contrat minimal visible.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `_evaluators: Dictionary[StringName, NarrativeConditionEvaluator]`, `evaluator: NarrativeConditionEvaluator`, `type_id: StringName, evaluator`, `Error:
      _evaluators[type_id]`, `condition: NarrativeCondition, context`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `Error`, `NarrativeDecision` ; branches visibles : `ERR_INVALID_PARAMETER`, `OK`, `NarrativeDecision.indeterminate(&"unknown_condition_type")`, `evaluator.evaluate(condition, context)`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `type_id.is_empty() or evaluator == null or _evaluators.has(type_id)`, `evaluator == null` avant de poursuivre le traitement.

## 18. Décisions narratives explicables

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name NarrativeDecision
extends RefCounted

enum Outcome { TRUE, FALSE, INDETERMINATE }

var outcome: Outcome
var reason_code: StringName
var evidence_ids: Array[StringName] = []
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** La décision conserve un résultat à trois états, un code de raison stable et les identités des faits utilisés. Une valeur indéterminée n’est jamais convertie silencieusement en vrai.

- **Rôle précis du bloc :** Le bloc définit `NarrativeDecision` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `NarrativeDecision`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `outcome: Outcome`, `reason_code: StringName`, `evidence_ids: Array[StringName]`.

## 19. Normalisation des événements externes

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name NarrativeFactAdapter
extends RefCounted

func from_gameplay_event(event: GameEventEnvelope) -> NarrativeFact:
    if event == null or not event.is_valid():
        return null
    var fact := NarrativeFact.new()
    fact.source_event_id = event.event_id
    fact.fact_id = StringName("fact_%s" % event.event_id)
    fact.revision = 0
    return fact if fact.is_valid() else null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** L’adaptateur produit une identité déterministe depuis l’événement source et refuse une enveloppe invalide. Il ne copie que les champs autorisés par le contrat narratif.

- **Rôle précis du bloc :** Le bloc définit `NarrativeFactAdapter` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `NarrativeFactAdapter` et les fonctions `from_gameplay_event()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `event: GameEventEnvelope`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `NarrativeFact` ; branches visibles : `null`, `fact if fact.is_valid() else null`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `event == null or not event.is_valid()` avant de poursuivre le traitement.

## 20. Idempotence des faits

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name NarrativeFactReceipt
extends RefCounted

var source_event_id: StringName
var fingerprint: String
var result_code: StringName
var committed_tick: int

func matches(other_fingerprint: String) -> bool:
    return fingerprint == other_fingerprint
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** Le reçu lie l’identité source à une empreinte canonique. Un retry identique retourne le résultat durable ; une même identité avec un autre contenu est un conflit.

- **Rôle précis du bloc :** Le bloc définit `NarrativeFactReceipt` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `NarrativeFactReceipt` et les fonctions `matches()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `source_event_id: StringName`, `fingerprint: String`, `result_code: StringName`, `committed_tick: int`, `other_fingerprint: String`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `fingerprint == other_fingerprint`.

## 21. Commandes de quête

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name StartQuestCommand
extends RefCounted

var command_id: StringName
var quest_id: StringName
var owner_id: StringName
var expected_revision: int
var requested_tick: int

func is_valid() -> bool:
    return not command_id.is_empty() and not quest_id.is_empty() and not owner_id.is_empty() and expected_revision >= 0 and requested_tick >= 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** La commande porte son identité idempotente, la quête, son propriétaire, la révision attendue et le tick logique. Elle n’accepte aucune heure système.

- **Rôle précis du bloc :** Le bloc définit `StartQuestCommand` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `StartQuestCommand` et les fonctions `is_valid()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `command_id: StringName`, `quest_id: StringName`, `owner_id: StringName`, `expected_revision: int`, `requested_tick: int`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `not command_id.is_empty() and not quest_id.is_empty() and not owner_id.is_empty() and expected_revision >= 0 and requested_tick >= 0`.

## 22. Service de démarrage

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
func start_quest(command: StartQuestCommand) -> NarrativeResult:
    if command == null or not command.is_valid():
        return NarrativeResult.rejected(&"invalid_command")
    var previous := _repository.get_quest(command.owner_id, command.quest_id)
    if previous == null or previous.revision != command.expected_revision:
        return NarrativeResult.rejected(&"revision_conflict")
    var candidate := previous.duplicate_detached()
    candidate.status = QuestRuntimeState.Status.ACTIVE
    candidate.started_tick = command.requested_tick
    candidate.revision += 1
    return _commit_port.commit_quest(candidate, command.command_id)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Le service relit l’état, vérifie la révision, prépare une copie puis délègue le remplacement au port de commit. Aucun événement n’est émis avant le succès du commit.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `start_quest()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `start_quest()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `command: StartQuestCommand`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `NarrativeResult` ; branches visibles : `NarrativeResult.rejected(&"invalid_command")`, `NarrativeResult.rejected(&"revision_conflict")`, `_commit_port.commit_quest(candidate, command.command_id)`.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `candidate.status = QuestRuntimeState.Status.ACTIVE`, `candidate.started_tick = command.requested_tick`, `candidate.revision += 1`, `return _commit_port.commit_quest(candidate, command.command_id)`.

## 23. Évaluation des objectifs

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
func evaluate_objective(objective: QuestObjectiveDefinition, facts: Array[NarrativeFact]) -> int:
    var progress := 0
    for fact in facts:
        if _matcher.matches(objective, fact):
            progress = add_progress(progress, _matcher.progress_delta(objective, fact))
            if progress < 0:
                return -1
    return progress
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** L’évaluation parcourt des faits déjà validés et utilise un matcher injecté. Elle renvoie `-1` si un delta ou un cumul viole les bornes.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `evaluate_objective()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `evaluate_objective()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `objective: QuestObjectiveDefinition, facts`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `int` ; branches visibles : `-1`, `progress`.

## 24. Achèvement atomique d’une quête

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name NarrativeCommitPort
extends RefCounted

func commit_completion(
    quest_candidate: QuestRuntimeState,
    knowledge_candidates: Array[DiscoveredKnowledgeState],
    external_candidates: Array[RefCounted],
    receipt: NarrativeFactReceipt
) -> Error:
    return ERR_UNAVAILABLE
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** Le port reçoit le candidat de quête, les découvertes de connaissance, les candidats des autorités externes et le reçu idempotent. L’implémentation doit tout committer ou ne rien remplacer.

- **Rôle précis du bloc :** Le bloc définit `NarrativeCommitPort` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `NarrativeCommitPort` et les fonctions `commit_completion()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `Error` ; branches visibles : `ERR_UNAVAILABLE`.

## 25. Conséquences multi-autorités

> **[LECTURE] Exemple de référence — Ne pas saisir.**

```text
Quest completion
├── inventory candidate
├── economy candidate
├── political candidate
├── domain candidate
├── knowledge candidates
└── narrative receipt
        ↓ single commit boundary
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** Une récompense d’objet, une somme, un droit ou un changement de domaine n’est jamais appliqué directement par la narration. Chaque autorité prépare son propre candidat avant la frontière de commit.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

## 26. Journal narratif

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name NarrativeJournalEntry
extends RefCounted

var entry_id: StringName
var owner_id: StringName
var template_id: StringName
var parameter_ids: Dictionary[StringName, StringName] = {}
var created_tick: int
var visibility: StringName
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Persistance et restauration :** Le journal persiste un modèle et des paramètres stables, pas une phrase localisée figée. La présentation résout le texte selon la langue et la version de contenu.

- **Rôle précis du bloc :** Le bloc définit `NarrativeJournalEntry` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `NarrativeJournalEntry`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `entry_id: StringName`, `owner_id: StringName`, `template_id: StringName`, `parameter_ids: Dictionary[StringName, StringName]`, `created_tick: int`, `visibility: StringName`.

## 27. Codex et visibilité

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
func can_show_entry(entry: CodexEntryDefinition, owner_id: StringName) -> NarrativeDecision:
    var context := _context_port.build_for(owner_id)
    return _condition_registry.evaluate(entry.visibility_condition, context)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** La visibilité passe par les mêmes décisions explicables. Une décision indéterminée masque l’entrée au lieu de la révéler.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `can_show_entry()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `can_show_entry()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `entry: CodexEntryDefinition, owner_id`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `NarrativeDecision` ; branches visibles : `_condition_registry.evaluate(entry.visibility_condition, context)`.

## 28. Connaissance personnelle, collective et publique

> **[LECTURE] Exemple de référence — Ne pas saisir.**

```yaml
knowledge_id: know_ruins_gate
holder_type: character
holder_id: chr_aster
source_fact_id: fact_evt_1042
confidence_bp: 7500
discovered_tick: 88200
visibility: private
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le détenteur, la source, la confiance et la visibilité sont distincts. Une connaissance privée ne devient collective ou publique que par une commande validée et une règle explicite.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `source_fact_id: fact_evt_1042`.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

## 29. Rumeurs et incertitude

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name KnowledgeClaim
extends RefCounted

var claim_id: StringName
var proposition_id: StringName
var source_id: StringName
var confidence_bp: int
var status: StringName

func is_valid() -> bool:
    return confidence_bp >= 0 and confidence_bp <= 10000 and not proposition_id.is_empty()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** Une rumeur est une affirmation avec provenance et confiance, pas un fait autoritaire. Son statut peut évoluer sans réécrire l’événement source.

- **Rôle précis du bloc :** Le bloc définit `KnowledgeClaim` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `KnowledgeClaim` et les fonctions `is_valid()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `claim_id: StringName`, `proposition_id: StringName`, `source_id: StringName`, `confidence_bp: int`, `status: StringName`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `confidence_bp >= 0 and confidence_bp <= 10000 and not proposition_id.is_empty()`.

## 30. Mémoire vectorielle et codex

> **[LECTURE] Exemple de référence — Ne pas saisir.**

```text
Canonical codex entries → optional indexing pipeline → vector index
DiscoveredKnowledgeState ────────────────┘
Vector index = derived, rebuildable, non-authoritative
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** Le codex et les découvertes sont les sources canoniques. L’index vectoriel du chapitre 10 reste dérivé, reconstructible et exclu de l’autorité des sauvegardes.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

## 31. IA locale consultative

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
func propose_journal_summary(facts: Array[NarrativeFact]) -> String:
    var request := _prompt_builder.build_bounded_summary(facts)
    var response := _ai_gateway.request(request)
    if not response.is_success():
        return _deterministic_fallback.summarize(facts)
    return _sanitizer.clean_display_text(response.text)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** L’IA peut proposer un résumé d’affichage. Elle ne crée aucun fait, ne valide aucun objectif et ne déclenche aucune conséquence. Un repli déterministe reste disponible.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `propose_journal_summary()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `propose_journal_summary()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `facts: Array[NarrativeFact]`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `String` ; branches visibles : `_deterministic_fallback.summarize(facts)`, `_sanitizer.clean_display_text(response.text)`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `not response.is_success()` avant de poursuivre le traitement.

## 32. Orchestration des agents

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name NarrativeObservation
extends RefCounted

var observation_id: StringName
var owner_id: StringName
var fact_ids: Array[StringName]
var suggested_goal_tag: StringName
var expires_tick: int
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Effets de bord :** Une observation fournit des faits et un tag de but suggéré. L’agent du chapitre 17 décide encore de ses buts et actions ; la narration ne modifie pas directement son plan.

- **Rôle précis du bloc :** Le bloc définit `NarrativeObservation` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `NarrativeObservation`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `observation_id: StringName`, `owner_id: StringName`, `fact_ids: Array[StringName]`, `suggested_goal_tag: StringName`, `expires_tick: int`.

## 33. Présentation séparée

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
class_name QuestLogPresenter
extends Control

var _query: NarrativeQuery

func refresh(owner_id: StringName) -> void:
    var view := _query.build_quest_log(owner_id)
    _render(view)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Effets de bord :** La présentation consomme une vue en lecture seule. Elle n’accède pas au dépôt mutable et ne peut pas appeler un commit métier depuis un bouton sans passer par une commande applicative.

- **Rôle précis du bloc :** Le bloc définit `QuestLogPresenter` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `QuestLogPresenter` et les fonctions `refresh()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `_query: NarrativeQuery`, `owner_id: StringName`, `void:
      _render`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `void`.

## 34. Persistance stricte

> **[LECTURE] Exemple de référence — Ne pas saisir.**

```json
{
  "format": "asteria-narrative",
  "version": 1,
  "quests": [],
  "arcs": [],
  "knowledge": [],
  "journal": [],
  "receipts": []
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** Le snapshot conserve uniquement l’état vivant et les reçus nécessaires à l’idempotence. Les définitions, caches, vues, index vectoriels et nœuds restent exclus.

- **Rôle précis du bloc :** Le bloc présente une structure de données littérale dont les clés et valeurs constituent le contrat à relire.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

## 35. Codec et restauration préparée

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
func prepare_restore(payload: Dictionary) -> NarrativeRestoreCandidate:
    var candidate := NarrativeRestoreCandidate.new()
    if not _schema_validator.validate(payload):
        return null
    if not candidate.decode_all(payload):
        return null
    if not candidate.cross_validate(_catalogs):
        return null
    return candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Persistance et restauration :** La restauration décode toutes les sections sur un candidat isolé puis recoupe les identités avec les catalogues. Le monde actif n’est remplacé qu’après validation globale.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `prepare_restore()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `prepare_restore()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `payload: Dictionary`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `NarrativeRestoreCandidate` ; branches visibles : `null`, `candidate`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `not _schema_validator.validate(payload)`, `not candidate.decode_all(payload)`, `not candidate.cross_validate(_catalogs)` avant de poursuivre le traitement.

## 36. Migrations de sauvegarde

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
func migrate_v1_to_v2(document: Dictionary) -> Dictionary:
    var copy := document.duplicate(true)
    copy["version"] = 2
    copy["knowledge_claims"] = []
    return copy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Effets de bord :** Une migration travaille sur une copie profonde, avance d’une version et initialise explicitement les nouveaux champs. Elle ne modifie jamais le document source en place.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `migrate_v1_to_v2()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `migrate_v1_to_v2()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `document: Dictionary`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `Dictionary` ; branches visibles : `copy`.

## 37. Budgets et simulation hors écran

> **[LECTURE] Exemple de référence — Ne pas saisir.**

```yaml
narrative_budget:
  max_facts_per_tick: 64
  max_quest_evaluations_per_tick: 16
  max_consequences_per_commit: 12
  max_journal_entries_per_owner: 256
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** Les limites empêchent une tempête d’événements de monopoliser une frame. Le traitement peut être réparti sur plusieurs ticks sans modifier l’ordre déterministe des faits.

- **Rôle précis du bloc :** Le bloc présente une structure de données littérale dont les clés et valeurs constituent le contrat à relire.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

## 38. Sécurité et robustesse

Les identifiants et paramètres externes sont validés, les collections sont bornées, les types exécutables sont fermés, les textes IA sont traités comme affichage non fiable et les conséquences repassent par les politiques d’autorisation. Les données de quête ne chargent jamais un script, une classe ou une méthode arbitraire.

## 39. Modes Solo et Studio

### 39.1 Mode Solo

- catalogues locaux
- dépôts en mémoire
- adaptateurs déterministes

### 39.2 Mode Studio

- contenu revu
- contrôles de schéma
- responsabilité des migrations
- preuves produites par l’intégration continue

Le contrat métier reste identique. Le mode Studio ajoute la responsabilité éditoriale, la revue des changements de schéma et les validations automatisées sans créer une seconde architecture runtime.
## 40. Tests à préparer

> **[LECTURE] Exemple de référence — Ne pas saisir.**

```text
Unit: conditions, progress, idempotency, visibility
Integration: fact→quest→consequence commit
Save: round-trip and future-version refusal
Simulation: event storms and bounded queues
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** La matrice distingue tests unitaires, intégration multi-autorités, sauvegarde et charge. Le chapitre 27 matérialisera l’infrastructure de tests complète.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

## 41. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 41.1 Utiliser le texte affiché comme identité de quête

**Symptôme :** le système produit un état narratif non reproductible ou contourne une autorité.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
quest_id = StringName(title_label.text)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Pourquoi cet exemple est fautif :** Le texte est localisable et modifiable ; l’identifiant stable vient de la définition.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Point complémentaire 3 :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
quest_id = definition.quest_id
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** **Pourquoi la correction fonctionne :** Dans le cas « Utiliser le texte affiché comme identité de quête », la correction traite directement le risque suivant : Le texte est localisable et modifiable ; l’identifiant stable vient de la définition. Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

### 41.2 Traiter un événement comme vérité narrative complète

**Symptôme :** le système produit un état narratif non reproductible ou contourne une autorité.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
quest.status = SUCCEEDED # à la réception d’un événement
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Pourquoi cet exemple est fautif :** L’événement devient d’abord un fait validé puis passe par les conditions de la quête.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Point complémentaire 3 :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
facts.append(adapter.from_gameplay_event(event))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** **Pourquoi la correction fonctionne :** Dans le cas « Traiter un événement comme vérité narrative complète », la correction traite directement le risque suivant : L’événement devient d’abord un fait validé puis passe par les conditions de la quête. Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `facts.append(adapter.from_gameplay_event(event))`.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

### 41.3 Évaluer une condition avec du code dynamique

**Symptôme :** le système produit un état narratif non reproductible ou contourne une autorité.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
var ok = eval(condition.expression)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** **Pourquoi cet exemple est fautif :** Le registre ferme les évaluateurs autorisés et rend les refus explicables.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var decision = registry.evaluate(condition, context)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** **Pourquoi la correction fonctionne :** Dans le cas « Évaluer une condition avec du code dynamique », la correction traite directement le risque suivant : Le registre ferme les évaluateurs autorisés et rend les refus explicables. Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

### 41.4 Valider une quête avant les conséquences

**Symptôme :** le système produit un état narratif non reproductible ou contourne une autorité.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
quest.status = SUCCEEDED
wallet.credit(100)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** **Pourquoi cet exemple est fautif :** Le lot commun évite une quête réussie sans récompense ou une récompense sans quête.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Point complémentaire 4 :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
commit_port.commit_completion(quest_candidate, [], [money_candidate], receipt)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** **Pourquoi la correction fonctionne :** Dans le cas « Valider une quête avant les conséquences », la correction traite directement le risque suivant : Le lot commun évite une quête réussie sans récompense ou une récompense sans quête. Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `commit_port.commit_completion(quest_candidate, [], [money_candidate], receipt)`.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

### 41.5 Révéler une entrée sur une décision indéterminée

**Symptôme :** le système produit un état narratif non reproductible ou contourne une autorité.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
return decision.outcome != FALSE
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Résultat attendu :** **Pourquoi cet exemple est fautif :** Seul un résultat positif explicite révèle le contenu.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose branches visibles : `decision.outcome != FALSE`.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
return decision.outcome == TRUE
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** **Pourquoi la correction fonctionne :** Dans le cas « Révéler une entrée sur une décision indéterminée », la correction traite directement le risque suivant : Seul un résultat positif explicite révèle le contenu. Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose branches visibles : `decision.outcome == TRUE`.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

### 41.6 Confondre connaissance et fait global

**Symptôme :** le système produit un état narratif non reproductible ou contourne une autorité.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
world_facts[claim.proposition_id] = true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Pourquoi cet exemple est fautif :** Une affirmation conserve détenteur, source, confiance et statut.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Point complémentaire 3 :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
knowledge_repository.add_claim(claim)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** **Pourquoi la correction fonctionne :** Dans le cas « Confondre connaissance et fait global », la correction traite directement le risque suivant : Une affirmation conserve détenteur, source, confiance et statut. Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

### 41.7 Laisser l’IA achever un objectif

**Symptôme :** le système produit un état narratif non reproductible ou contourne une autorité.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
if ai_response == "done": progress = 10000
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** **Pourquoi cet exemple est fautif :** La progression vient de faits autoritaires et d’un évaluateur déterministe.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
progress = objective_evaluator.evaluate(objective, facts)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** **Pourquoi la correction fonctionne :** Dans le cas « Laisser l’IA achever un objectif », la correction traite directement le risque suivant : La progression vient de faits autoritaires et d’un évaluateur déterministe. Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

### 41.8 Utiliser l’heure système

**Symptôme :** le système produit un état narratif non reproductible ou contourne une autorité.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
state.started_tick = int(Time.get_unix_time_from_system())
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Pourquoi cet exemple est fautif :** Le temps réel ne fait pas partie de la simulation sauvegardée.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `state.started_tick = int(Time.get_unix_time_from_system())`.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
state.started_tick = world_clock.current_tick
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** **Pourquoi la correction fonctionne :** Dans le cas « Utiliser l’heure système », la correction traite directement le risque suivant : Le temps réel ne fait pas partie de la simulation sauvegardée. Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `state.started_tick = world_clock.current_tick`.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

### 41.9 Charger directement dans les dépôts actifs

**Symptôme :** le système produit un état narratif non reproductible ou contourne une autorité.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
repository.replace_all(codec.decode(payload))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Effets de bord :** **Pourquoi cet exemple est fautif :** La préparation complète précède tout remplacement.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
candidate = codec.prepare_restore(payload)
restore_port.commit(candidate)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** **Pourquoi la correction fonctionne :** Dans le cas « Charger directement dans les dépôts actifs », la correction traite directement le risque suivant : La préparation complète précède tout remplacement. Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `restore_port.commit(candidate)`.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

### 41.10 Persister l’index vectoriel

**Symptôme :** le système produit un état narratif non reproductible ou contourne une autorité.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
snapshot["vectors"] = vector_store.dump()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Pourquoi cet exemple est fautif :** L’index est dérivé et reconstructible depuis les sources canoniques.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Point complémentaire 3 :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
snapshot["knowledge"] = knowledge_repository.to_records()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** **Pourquoi la correction fonctionne :** Dans le cas « Persister l’index vectoriel », la correction traite directement le risque suivant : L’index est dérivé et reconstructible depuis les sources canoniques. Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

## 42. Synthèse opérationnelle pour Project Asteria

`Project Asteria` retient une narration événementielle mais non autoritaire sur les autres systèmes. Les événements sont normalisés en faits identifiés et idempotents. Les arcs, quêtes et objectifs sont définis par des données validées ; leurs états runtime sont séparés et révisionnés. Les conditions sont évaluées par un registre fermé, les décisions sont explicables et l’indéterminé n’accorde aucun succès ni visibilité.

Les conséquences externes sont préparées par l’inventaire, l’économie, la politique, l’écologie ou les domaines, puis committées avec l’état narratif et le reçu idempotent. Le codex sépare contenu éditorial et découverte. Les connaissances restent relatives à un détenteur, une source et une confiance. L’IA locale peut résumer ou suggérer, mais ne crée ni fait, ni verdict narratif, ni progression autoritaire. La persistance conserve uniquement les états vivants et reçus nécessaires, et toute restauration est préparée avant remplacement.
