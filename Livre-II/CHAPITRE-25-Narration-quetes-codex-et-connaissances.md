---
title: "Livre II — Chapitre 25 : Narration, quêtes, codex et connaissances"
id: "DOC-L2-CH25"
status: "reviewed"
version: "1.0.1"
lang: "fr-FR"
book: "Livre II"
chapter: 25
last-verified: "2026-07-21T15:28:42+02:00"
audit-status: "complete"
audit-date: "2026-07-21T15:28:42+02:00"
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

- **Effets de bord :** Le flux distingue le fait source, son adaptation narrative, l’évaluation et le commit.

- **Déterminisme et idempotence :** Un événement reçu n’est pas appliqué deux fois : son identité et son empreinte sont enregistrées avec le résultat durable.

- **Rôle précis du bloc :** Le schéma fait circuler le traitement de `GameplayEvent` vers `State replacement + events + journal`.

- **Déroulement ou instructions importantes :** Les transitions visibles sont `↓ normalisation`, `↓ règles déterministes`, `↓ préparation`, `↓ commit commun`.

- **Résultat attendu :** La lecture doit conserver l’ordre et les correspondances explicites entre les éléments listés, sans inventer de relation absente du schéma.

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

- **Rôle précis du bloc :** L’arborescence répartit les éléments entre `domain`, `application`, `infrastructure`, `presentation`.

- **Organisation des fichiers :** Les chemins restent séparés selon leur responsabilité ; les fichiers listés ne sont pas interchangeables entre domaine, application, infrastructure et présentation.

- **Résultat attendu :** La lecture doit conserver l’ordre et les correspondances explicites entre les éléments listés, sans inventer de relation absente du schéma.

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

- **Rôle précis du bloc :** Un fait narratif possède une identité indépendante de son texte, de son ordre d’affichage et de son événement source. Le bloc définit `NarrativeFactId` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Invariants protégés :** `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Paramètres et types importants :** Les déclarations visibles sont `fact_: StringName`, `revision: int`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `is_valid() -> bool`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `not fact_.is_empty() and revision >= 0`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Paramètres et types importants :** Le fait conserve type, sujet, objet, tick, provenance et payload borné sans copier un nœud ou un objet métier mutable. Les déclarations visibles sont `source_event_id: StringName`, `revision: int`.

- **Invariants protégés :** `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Rôle précis du bloc :** Le bloc définit `NarrativeFact` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `is_valid() -> bool`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `not source_event_id.is_empty() and revision >= 0`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Limites et réserves :** Un arc regroupe des quêtes et des transitions de haut niveau sans stocker leur progression runtime dans la `Resource`.

- **Invariants protégés :** `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Rôle précis du bloc :** Le bloc définit `NarrativeArcDefinition` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Paramètres et types importants :** Les déclarations visibles sont `arc_id: StringName`, `revision: int`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `is_valid() -> bool`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `not arc_id.is_empty() and revision >= 0`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Limites et réserves :** Une quête de conception déclare préconditions, objectifs, règles d’échec et conséquences, mais aucun état joueur.

- **Invariants protégés :** `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Rôle précis du bloc :** Le bloc définit `QuestDefinition` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Paramètres et types importants :** Les déclarations visibles sont `quest_id: StringName`, `revision: int`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `is_valid() -> bool`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `not quest_id.is_empty() and revision >= 0`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Paramètres et types importants :** Les objectifs utilisent des types fermés et des paramètres validés ; aucun script ou nom de méthode ne provient des données. Les déclarations visibles sont `objective_id: StringName`, `revision: int`.

- **Invariants protégés :** `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Rôle précis du bloc :** Le bloc définit `QuestObjectiveDefinition` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `is_valid() -> bool`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `not objective_id.is_empty() and revision >= 0`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Responsabilités des classes ou fonctions :** Une condition est évaluée par un registre de stratégies autorisées, jamais par `eval` ni par chargement dynamique. Les signatures documentées sont `is_valid() -> bool`.

- **Invariants protégés :** `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Rôle précis du bloc :** Le bloc définit `NarrativeCondition` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Paramètres et types importants :** Les déclarations visibles sont `condition_type: StringName`, `revision: int`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `not condition_type.is_empty() and revision >= 0`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Frontières d’autorité :** Une conséquence décrit une demande ; l’autorité externe prépare le candidat réel et peut refuser.

- **Invariants protégés :** `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Rôle précis du bloc :** Le bloc définit `NarrativeConsequenceDefinition` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Paramètres et types importants :** Les déclarations visibles sont `effect_type: StringName`, `revision: int`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `is_valid() -> bool`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `not effect_type.is_empty() and revision >= 0`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Rôle précis du bloc :** Le codex sépare contenu éditorial, règles de visibilité et état de découverte. Le bloc définit `CodexEntryDefinition` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Invariants protégés :** `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Paramètres et types importants :** Les déclarations visibles sont `entry_id: StringName`, `revision: int`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `is_valid() -> bool`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `not entry_id.is_empty() and revision >= 0`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Rôle précis du bloc :** Une connaissance est relative à un détenteur, une source et un niveau de confiance ; elle ne devient pas automatiquement un fait global. Le bloc définit `DiscoveredKnowledgeState` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Invariants protégés :** `is_valid()` protège l’identité vide et les révisions négatives avant toute insertion dans un dépôt.

- **Paramètres et types importants :** Les déclarations visibles sont `knowledge_id: StringName`, `revision: int`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `is_valid() -> bool`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `not knowledge_id.is_empty() and revision >= 0`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Rôle précis du bloc :** L’état runtime est séparé de `QuestDefinition`. Le bloc définit `QuestRuntimeState` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Invariants protégés :** La copie profonde du dictionnaire empêche un candidat de partager une collection mutable avec l’état actif.

- **Paramètres et types importants :** Les déclarations visibles sont `quest_id: StringName`, `owner_id: StringName`, `status: Status`, `objective_progress: Dictionary[StringName, int]`, `started_tick: int`, `ended_tick: int`, `revision: int`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `duplicate_detached() -> QuestRuntimeState`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `copy`.

- **Effets de bord :** Les effets visibles sont `copy.quest_id = quest_id`, `copy.owner_id = owner_id`, `copy.status = status`, `copy.objective_progress = objective_progress.duplicate(true)`, `copy.started_tick = started_tick`, `copy.ended_tick = ended_tick`.

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

- **Paramètres et types importants :** La progression utilise des points de base entiers.

- **Valeur de retour ou code d’échec :** La sentinelle `-1` distingue un état invalide d’une progression légitime à zéro. Les branches de sortie visibles renvoient `-1`, `mini(PROGRESS_SCALE, current + delta)`.

- **Rôle précis du bloc :** Le bloc expose `add_progress()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `add_progress(current: int, delta: int) -> int`.

- **Invariants protégés :** Les gardes explicites contrôlent `current < 0 or current > PROGRESS_SCALE`, `delta < 0`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Responsabilités des classes ou fonctions :** Le registre ferme l’ensemble des stratégies exécutables. Les signatures documentées sont `register(type_id: StringName, evaluator: NarrativeConditionEvaluator) -> Error`, `evaluate(condition: NarrativeCondition, context: NarrativeEvaluationContext) -> NarrativeDecision`.

- **Résultat attendu :** Une condition inconnue produit `INDETERMINATE`, jamais une autorisation implicite.

- **Rôle précis du bloc :** Le bloc définit `NarrativeConditionRegistry` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Paramètres et types importants :** Les déclarations visibles sont `_evaluators: Dictionary[StringName, NarrativeConditionEvaluator]`, `evaluator: NarrativeConditionEvaluator`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ERR_INVALID_PARAMETER`, `OK`, `NarrativeDecision.indeterminate(&"unknown_condition_type")`, `evaluator.evaluate(condition, context)`.

- **Invariants protégés :** Les gardes explicites contrôlent `type_id.is_empty() or evaluator == null or _evaluators.has(type_id)`, `evaluator == null`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Rôle précis du bloc :** La décision conserve un résultat à trois états, un code de raison stable et les identités des faits utilisés. Le bloc définit `NarrativeDecision` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Déterminisme et idempotence :** Une valeur indéterminée n’est jamais convertie silencieusement en vrai.

- **Paramètres et types importants :** Les déclarations visibles sont `outcome: Outcome`, `reason_code: StringName`, `evidence_ids: Array[StringName]`.

- **Déroulement ou instructions importantes :** L’extrait commence par `class_name NarrativeDecision` et se termine par `var evidence_ids: Array[StringName] = []` ; les lignes intermédiaires doivent être lues dans cet ordre.

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

- **Déterminisme et idempotence :** L’adaptateur produit une identité déterministe depuis l’événement source et refuse une enveloppe invalide.

- **Paramètres et types importants :** Il ne copie que les champs autorisés par le contrat narratif.

- **Rôle précis du bloc :** Le bloc définit `NarrativeFactAdapter` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `from_gameplay_event(event: GameEventEnvelope) -> NarrativeFact`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `null`, `fact if fact.is_valid() else null`.

- **Invariants protégés :** Les gardes explicites contrôlent `event == null or not event.is_valid()`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Déterminisme et idempotence :** Le reçu lie l’identité source à une empreinte canonique.

- **Valeur de retour ou code d’échec :** Un retry identique retourne le résultat durable ; une même identité avec un autre contenu est un conflit. Les branches de sortie visibles renvoient `fingerprint == other_fingerprint`.

- **Rôle précis du bloc :** Le bloc définit `NarrativeFactReceipt` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Paramètres et types importants :** Les déclarations visibles sont `source_event_id: StringName`, `fingerprint: String`, `result_code: StringName`, `committed_tick: int`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `matches(other_fingerprint: String) -> bool`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Frontières d’autorité :** La commande porte son identité idempotente, la quête, son propriétaire, la révision attendue et le tick logique.

- **Limites et réserves :** Elle n’accepte aucune heure système.

- **Rôle précis du bloc :** Le bloc définit `StartQuestCommand` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Paramètres et types importants :** Les déclarations visibles sont `command_id: StringName`, `quest_id: StringName`, `owner_id: StringName`, `expected_revision: int`, `requested_tick: int`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `is_valid() -> bool`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `not command_id.is_empty() and not quest_id.is_empty() and not owner_id.is_empty() and expected_revision >= 0 and requested_tick >= 0`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Dépendances et ports utilisés :** Le service relit l’état, vérifie la révision, prépare une copie puis délègue le remplacement au port de commit.

- **Effets de bord :** Aucun événement n’est émis avant le succès du commit. Les effets visibles sont `candidate.status = QuestRuntimeState.Status.ACTIVE`, `candidate.started_tick = command.requested_tick`, `candidate.revision += 1`, `return _commit_port.commit_quest(candidate, command.command_id)`.

- **Rôle précis du bloc :** Le bloc expose `start_quest()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `start_quest(command: StartQuestCommand) -> NarrativeResult`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `NarrativeResult.rejected(&"invalid_command")`, `NarrativeResult.rejected(&"revision_conflict")`, `_commit_port.commit_quest(candidate, command.command_id)`.

- **Invariants protégés :** Les gardes explicites contrôlent `command == null or not command.is_valid()`, `previous == null or previous.revision != command.expected_revision`.

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

- **Dépendances et ports utilisés :** L’évaluation parcourt des faits déjà validés et utilise un matcher injecté.

- **Valeur de retour ou code d’échec :** Elle renvoie `-1` si un delta ou un cumul viole les bornes. Les branches de sortie visibles renvoient `-1`, `progress`.

- **Rôle précis du bloc :** Le bloc expose `evaluate_objective()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `evaluate_objective(objective: QuestObjectiveDefinition, facts: Array[NarrativeFact]) -> int`.

- **Invariants protégés :** Les gardes explicites contrôlent `_matcher.matches(objective, fact)`, `progress < 0`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Frontières d’autorité :** Le port reçoit le candidat de quête, les découvertes de connaissance, les candidats des autorités externes et le reçu idempotent.

- **Effets de bord :** L’implémentation doit tout committer ou ne rien remplacer. Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

- **Rôle précis du bloc :** Le bloc définit `NarrativeCommitPort` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `commit_completion(quest_candidate: QuestRuntimeState, knowledge_candidates: Array[DiscoveredKnowledgeState], external_candidates: Array[RefCounted], receipt: NarrativeFactReceipt) -> Error`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ERR_UNAVAILABLE`.

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

- **Rôle précis du bloc :** Une récompense d’objet, une somme, un droit ou un changement de domaine n’est jamais appliqué directement par la narration. L’arborescence répartit les éléments entre `inventory candidate`, `economy candidate`, `political candidate`, `domain candidate`, `knowledge candidates`, `narrative receipt`.

- **Frontières d’autorité :** Chaque autorité prépare son propre candidat avant la frontière de commit.

- **Organisation des fichiers :** Les chemins restent séparés selon leur responsabilité ; les fichiers listés ne sont pas interchangeables entre domaine, application, infrastructure et présentation.

- **Résultat attendu :** La lecture doit conserver l’ordre et les correspondances explicites entre les éléments listés, sans inventer de relation absente du schéma.

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

- **Persistance et restauration :** Le journal persiste un modèle et des paramètres stables, pas une phrase localisée figée.

- **Rôle précis du bloc :** La présentation résout le texte selon la langue et la version de contenu. Le bloc définit `NarrativeJournalEntry` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Paramètres et types importants :** Les déclarations visibles sont `entry_id: StringName`, `owner_id: StringName`, `template_id: StringName`, `parameter_ids: Dictionary[StringName, StringName]`, `created_tick: int`, `visibility: StringName`.

- **Déroulement ou instructions importantes :** L’extrait commence par `class_name NarrativeJournalEntry` et se termine par `var visibility: StringName` ; les lignes intermédiaires doivent être lues dans cet ordre.

## 27. Codex et visibilité

> **[VSC] Exemple de référence — Ne pas saisir.**

```gdscript
func can_show_entry(entry: CodexEntryDefinition, owner_id: StringName) -> NarrativeDecision:
    var context := _context_port.build_for(owner_id)
    return _condition_registry.evaluate(entry.visibility_condition, context)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La visibilité passe par les mêmes décisions explicables. Le bloc expose `can_show_entry()` et montre son traitement complet ou son squelette contractuel.

- **Déterminisme et idempotence :** Une décision indéterminée masque l’entrée au lieu de la révéler.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `can_show_entry(entry: CodexEntryDefinition, owner_id: StringName) -> NarrativeDecision`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `_condition_registry.evaluate(entry.visibility_condition, context)`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Rôle précis du bloc :** Le détenteur, la source, la confiance et la visibilité sont distincts. Une connaissance privée ne devient collective ou publique que par une commande validée et une règle explicite. Le bloc matérialise le format de données annoncé par `> **[LECTURE] Exemple de référence — Ne pas saisir.**`.

- **Paramètres et types importants :** Les clés visibles comprennent `knowledge_id`, `holder_type`, `holder_id`, `source_fact_id`, `confidence_bp`, `discovered_tick`, `visibility`.

- **Résultat attendu :** Une lecture conforme doit retrouver les mêmes clés, leurs relations et les valeurs obligatoires avant toute promotion ou consommation.

- **Déroulement ou instructions importantes :** L’extrait commence par `knowledge_id: know_ruins_gate` et se termine par `visibility: private` ; les lignes intermédiaires doivent être lues dans cet ordre.

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

- **Rôle précis du bloc :** Une rumeur est une affirmation avec provenance et confiance, pas un fait autoritaire. Le bloc définit `KnowledgeClaim` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Limites et réserves :** Son statut peut évoluer sans réécrire l’événement source.

- **Paramètres et types importants :** Les déclarations visibles sont `claim_id: StringName`, `proposition_id: StringName`, `source_id: StringName`, `confidence_bp: int`, `status: StringName`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `is_valid() -> bool`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `confidence_bp >= 0 and confidence_bp <= 10000 and not proposition_id.is_empty()`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 30. Mémoire vectorielle et codex

> **[LECTURE] Exemple de référence — Ne pas saisir.**

```text
Canonical codex entries → optional indexing pipeline → vector index
DiscoveredKnowledgeState ────────────────┘
Vector index = derived, rebuildable, non-authoritative
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le codex et les découvertes sont les sources canoniques. Le schéma fait circuler le traitement de `Canonical codex entries → optional indexing pipeline → vector index` vers `Vector index = derived, rebuildable, non-authoritative`.

- **Frontières d’autorité :** L’index vectoriel du chapitre 10 reste dérivé, reconstructible et exclu de l’autorité des sauvegardes.

- **Déroulement ou instructions importantes :** Les transitions visibles sont `Canonical codex entries → optional indexing pipeline → vector index`.

- **Résultat attendu :** La lecture doit conserver l’ordre et les correspondances explicites entre les éléments listés, sans inventer de relation absente du schéma.

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

- **Rôle précis du bloc :** L’IA peut proposer un résumé d’affichage. Le bloc expose `propose_journal_summary()` et montre son traitement complet ou son squelette contractuel.

- **Invariants protégés :** Elle ne crée aucun fait, ne valide aucun objectif et ne déclenche aucune conséquence. Les gardes explicites contrôlent `not response.is_success()`.

- **Déterminisme et idempotence :** Un repli déterministe reste disponible.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `propose_journal_summary(facts: Array[NarrativeFact]) -> String`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `_deterministic_fallback.summarize(facts)`, `_sanitizer.clean_display_text(response.text)`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Rôle précis du bloc :** Une observation fournit des faits et un tag de but suggéré. Le bloc définit `NarrativeObservation` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Effets de bord :** L’agent du chapitre 17 décide encore de ses buts et actions ; la narration ne modifie pas directement son plan.

- **Paramètres et types importants :** Les déclarations visibles sont `observation_id: StringName`, `owner_id: StringName`, `fact_ids: Array[StringName]`, `suggested_goal_tag: StringName`, `expires_tick: int`.

- **Déroulement ou instructions importantes :** L’extrait commence par `class_name NarrativeObservation` et se termine par `var expires_tick: int` ; les lignes intermédiaires doivent être lues dans cet ordre.

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

- **Invariants protégés :** La présentation consomme une vue en lecture seule.

- **Effets de bord :** Elle n’accède pas au dépôt mutable et ne peut pas appeler un commit métier depuis un bouton sans passer par une commande applicative.

- **Rôle précis du bloc :** Le bloc définit `QuestLogPresenter` dérivé de `Control` et rend visibles les données et opérations qui composent son contrat.

- **Paramètres et types importants :** Les déclarations visibles sont `_query: NarrativeQuery`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `refresh(owner_id: StringName) -> void`.

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

- **Déterminisme et idempotence :** Le snapshot conserve uniquement l’état vivant et les reçus nécessaires à l’idempotence.

- **Limites et réserves :** Les définitions, caches, vues, index vectoriels et nœuds restent exclus.

- **Rôle précis du bloc :** Le bloc matérialise le format de données annoncé par `> **[LECTURE] Exemple de référence — Ne pas saisir.**`.

- **Paramètres et types importants :** Les clés visibles comprennent `format`, `version`, `quests`, `arcs`, `knowledge`, `journal`, `receipts`.

- **Résultat attendu :** Une lecture conforme doit retrouver les mêmes clés, leurs relations et les valeurs obligatoires avant toute promotion ou consommation.

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

- **Persistance et restauration :** La restauration décode toutes les sections sur un candidat isolé puis recoupe les identités avec les catalogues.

- **Rôle précis du bloc :** Le monde actif n’est remplacé qu’après validation globale. Le bloc expose `prepare_restore()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `prepare_restore(payload: Dictionary) -> NarrativeRestoreCandidate`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `null`, `candidate`.

- **Invariants protégés :** Les gardes explicites contrôlent `not _schema_validator.validate(payload)`, `not candidate.decode_all(payload)`, `not candidate.cross_validate(_catalogs)`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

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

- **Paramètres et types importants :** Une migration travaille sur une copie profonde, avance d’une version et initialise explicitement les nouveaux champs.

- **Effets de bord :** Elle ne modifie jamais le document source en place. Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

- **Rôle précis du bloc :** Le bloc expose `migrate_v1_to_v2()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `migrate_v1_to_v2(document: Dictionary) -> Dictionary`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `copy`.

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

- **Invariants protégés :** Les limites empêchent une tempête d’événements de monopoliser une frame.

- **Déterminisme et idempotence :** Le traitement peut être réparti sur plusieurs ticks sans modifier l’ordre déterministe des faits.

- **Rôle précis du bloc :** Le bloc matérialise le format de données annoncé par `> **[LECTURE] Exemple de référence — Ne pas saisir.**`.

- **Paramètres et types importants :** Les clés visibles comprennent `narrative_budget`, `max_facts_per_tick`, `max_quest_evaluations_per_tick`, `max_consequences_per_commit`, `max_journal_entries_per_owner`.

- **Résultat attendu :** Une lecture conforme doit retrouver les mêmes clés, leurs relations et les valeurs obligatoires avant toute promotion ou consommation.

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

- **Frontières d’autorité :** La matrice distingue tests unitaires, intégration multi-autorités, sauvegarde et charge.

- **Rôle précis du bloc :** Le chapitre 27 matérialisera l’infrastructure de tests complète. Le schéma fait circuler le traitement de `Unit: conditions, progress, idempotency, visibility` vers `Simulation: event storms and bounded queues`.

- **Déroulement ou instructions importantes :** Les transitions visibles sont `Integration: fact→quest→consequence commit`.

- **Résultat attendu :** La lecture doit conserver l’ordre et les correspondances explicites entre les éléments listés, sans inventer de relation absente du schéma.

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

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `quest_id = StringName(title_label.text)`.

- **Symboles manipulés :** Les symboles visibles sont `quest_id`, `StringName`, `title_label`, `text`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
quest_id = definition.quest_id
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** **Pourquoi la correction fonctionne :** Dans le cas « Utiliser le texte affiché comme identité de quête », la correction traite directement le risque suivant : Le texte est localisable et modifiable ; l’identifiant stable vient de la définition.

- **Frontières d’autorité :** Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `quest_id = definition.quest_id`.

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

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `quest.status = SUCCEEDED # à la réception d’un événement`.

- **Symboles manipulés :** Les symboles visibles sont `quest`, `status`, `SUCCEEDED`, `la`, `r`, `ception`, `d`, `un`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
facts.append(adapter.from_gameplay_event(event))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** **Pourquoi la correction fonctionne :** Dans le cas « Traiter un événement comme vérité narrative complète », la correction traite directement le risque suivant : L’événement devient d’abord un fait validé puis passe par les conditions de la quête.

- **Frontières d’autorité :** Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Effets de bord :** Les effets visibles sont `facts.append(adapter.from_gameplay_event(event))`.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

### 41.3 Évaluer une condition avec du code dynamique

**Symptôme :** le système produit un état narratif non reproductible ou contourne une autorité.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
var ok = eval(condition.expression)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** **Pourquoi cet exemple est fautif :** Le registre ferme les évaluateurs autorisés et rend les refus explicables.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `var ok = eval(condition.expression)`.

- **Symboles manipulés :** Les symboles visibles sont `var`, `ok`, `eval`, `condition`, `expression`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var decision = registry.evaluate(condition, context)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** **Pourquoi la correction fonctionne :** Dans le cas « Évaluer une condition avec du code dynamique », la correction traite directement le risque suivant : Le registre ferme les évaluateurs autorisés et rend les refus explicables.

- **Frontières d’autorité :** Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `var decision = registry.evaluate(condition, context)`.

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

- **Déroulement ou instructions importantes :** L’extrait commence par `quest.status = SUCCEEDED` et se termine par `wallet.credit(100)` ; les lignes intermédiaires doivent être lues dans cet ordre.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `quest.status = SUCCEEDED`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
commit_port.commit_completion(quest_candidate, [], [money_candidate], receipt)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** **Pourquoi la correction fonctionne :** Dans le cas « Valider une quête avant les conséquences », la correction traite directement le risque suivant : Le lot commun évite une quête réussie sans récompense ou une récompense sans quête.

- **Frontières d’autorité :** Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Effets de bord :** Les effets visibles sont `commit_port.commit_completion(quest_candidate, [], [money_candidate], receipt)`.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

### 41.5 Révéler une entrée sur une décision indéterminée

**Symptôme :** le système produit un état narratif non reproductible ou contourne une autorité.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
return decision.outcome != FALSE
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** **Pourquoi cet exemple est fautif :** Seul un résultat positif explicite révèle le contenu.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `decision.outcome != FALSE`.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `return decision.outcome != FALSE`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
return decision.outcome == TRUE
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** **Pourquoi la correction fonctionne :** Dans le cas « Révéler une entrée sur une décision indéterminée », la correction traite directement le risque suivant : Seul un résultat positif explicite révèle le contenu.

- **Frontières d’autorité :** Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `decision.outcome == TRUE`.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

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

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `world_facts[claim.proposition_id] = true`.

- **Symboles manipulés :** Les symboles visibles sont `world_facts`, `claim`, `proposition_id`, `true`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
knowledge_repository.add_claim(claim)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** **Pourquoi la correction fonctionne :** Dans le cas « Confondre connaissance et fait global », la correction traite directement le risque suivant : Une affirmation conserve détenteur, source, confiance et statut.

- **Frontières d’autorité :** Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Effets de bord :** Les effets visibles sont `knowledge_repository.add_claim(claim)`.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

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

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `if ai_response == "done": progress = 10000`.

- **Symboles manipulés :** Les symboles visibles sont `if`, `ai_response`, `done`, `progress`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
progress = objective_evaluator.evaluate(objective, facts)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** **Pourquoi la correction fonctionne :** Dans le cas « Laisser l’IA achever un objectif », la correction traite directement le risque suivant : La progression vient de faits autoritaires et d’un évaluateur déterministe.

- **Frontières d’autorité :** Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `progress = objective_evaluator.evaluate(objective, facts)`.

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

- **Effets de bord :** Les effets visibles sont `state.started_tick = int(Time.get_unix_time_from_system())`.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `state.started_tick = int(Time.get_unix_time_from_system())`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
state.started_tick = world_clock.current_tick
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** **Pourquoi la correction fonctionne :** Dans le cas « Utiliser l’heure système », la correction traite directement le risque suivant : Le temps réel ne fait pas partie de la simulation sauvegardée.

- **Frontières d’autorité :** Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Effets de bord :** Les effets visibles sont `state.started_tick = world_clock.current_tick`.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

### 41.9 Charger directement dans les dépôts actifs

**Symptôme :** le système produit un état narratif non reproductible ou contourne une autorité.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
repository.replace_all(codec.decode(payload))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Effets de bord :** **Pourquoi cet exemple est fautif :** La préparation complète précède tout remplacement. Les effets visibles sont `repository.replace_all(codec.decode(payload))`.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `repository.replace_all(codec.decode(payload))`.

- **Symboles manipulés :** Les symboles visibles sont `repository`, `replace_all`, `codec`, `decode`, `payload`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
candidate = codec.prepare_restore(payload)
restore_port.commit(candidate)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Effets de bord :** **Pourquoi la correction fonctionne :** Dans le cas « Charger directement dans les dépôts actifs », la correction traite directement le risque suivant : La préparation complète précède tout remplacement. Les effets visibles sont `restore_port.commit(candidate)`.

- **Frontières d’autorité :** Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Déroulement ou instructions importantes :** L’extrait commence par `candidate = codec.prepare_restore(payload)` et se termine par `restore_port.commit(candidate)` ; les lignes intermédiaires doivent être lues dans cet ordre.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

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

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `snapshot["vectors"] = vector_store.dump()`.

- **Symboles manipulés :** Les symboles visibles sont `snapshot`, `vectors`, `vector_store`, `dump`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
snapshot["knowledge"] = knowledge_repository.to_records()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Persistance et restauration :** **Pourquoi la correction fonctionne :** Dans le cas « Persister l’index vectoriel », la correction traite directement le risque suivant : L’index est dérivé et reconstructible depuis les sources canoniques.

- **Frontières d’autorité :** Elle rétablit ensuite la frontière d’autorité, la décision explicite ou l’identité stable attendue.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `snapshot["knowledge"] = knowledge_repository.to_records()`.

## 42. Synthèse opérationnelle pour Project Asteria

`Project Asteria` retient une narration événementielle mais non autoritaire sur les autres systèmes. Les événements sont normalisés en faits identifiés et idempotents. Les arcs, quêtes et objectifs sont définis par des données validées ; leurs états runtime sont séparés et révisionnés. Les conditions sont évaluées par un registre fermé, les décisions sont explicables et l’indéterminé n’accorde aucun succès ni visibilité.

Les conséquences externes sont préparées par l’inventaire, l’économie, la politique, l’écologie ou les domaines, puis committées avec l’état narratif et le reçu idempotent. Le codex sépare contenu éditorial et découverte. Les connaissances restent relatives à un détenteur, une source et une confiance. L’IA locale peut résumer ou suggérer, mais ne crée ni fait, ni verdict narratif, ni progression autoritaire. La persistance conserve uniquement les états vivants et reçus nécessaires, et toute restauration est préparée avant remplacement.
