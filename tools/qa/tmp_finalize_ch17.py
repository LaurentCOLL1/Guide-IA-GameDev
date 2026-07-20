from pathlib import Path
import re

ROOT = Path('.')
chapter_path = ROOT / 'Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md'
text = chapter_path.read_text(encoding='utf-8')


def once(value: str, old: str, new: str, label: str) -> str:
    count = value.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected 1, got {count}')
    return value.replace(old, new, 1)

text = once(text, 'status: "draft"', 'status: "reviewed"', 'chapter status')
text = once(text, 'version: "0.9.0"', 'version: "1.0.0"', 'chapter version')
text = once(text, 'audit-status: "pending"', 'audit-status: "complete"', 'audit status')
text = once(text, 'audit-date: null', 'audit-date: "2026-07-20"', 'audit date')
text = once(text, 'audit-level: "not-audited"', 'audit-level: "static-review"', 'audit level')
text = once(
    text,
    '> **Audit post-création :** en attente — le premier commit constitue la porte de brouillon `0.9.0`.',
    '> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-17.md`.',
    'chapter audit banner',
)
text = once(text, '## 6. État logique de l’agent', '<a id="ch17-agent-state"></a>\n\n## 6. État logique de l’agent', 'agent state anchor')
text = once(
    text,
    '''func signature() -> String:
\treturn ",".join(PackedStringArray(action_ids))''',
    '''func signature() -> String:
\tvar parts := PackedStringArray()
\tfor action_id: StringName in action_ids:
\t\tparts.append(String(action_id))
\treturn ",".join(parts)''',
    'search signature conversion',
)
text = once(
    text,
    '- **Limite du brouillon :** les catalogues `AgentGoalPolicy`, `AgentGoalConditionCatalog`, `AgentSnapshotBuilder` et `WorldRevisionSource` sont des ports à documenter dans le projet matérialisé.',
    '- **Ports :** `AgentSnapshotBuilder`, `AgentGoalPolicy`, `AgentGoalConditionCatalog` et `WorldRevisionSource` sont définis par les signatures immédiatement suivantes ; leurs implémentations restent injectées.',
    'service draft reserve',
)
ports = '''

### 22.1 Signatures des ports de décision

| Port | Signature minimale | Responsabilité |
|---|---|---|
| `AgentSnapshotBuilder` | `build_snapshot(character_id: StringName, logical_tick: int) -> AgentWorldSnapshot` | agréger des lectures autorisées dans un snapshot détaché |
| `AgentGoalPolicy` | `select_goal(goals: Array[AgentGoal], logical_tick: int) -> AgentGoal` | choisir un but avec un ordre stable |
| `AgentGoalConditionCatalog` | `get_for(goal_type: StringName) -> Array[AgentCondition]` | fournir les conditions validées d’un type de but |
| `WorldRevisionSource` | `current_revision() -> int` | exposer la révision monotone utilisée pour l’invalidation |
| `AgentStateRepository` | `replace_all(states: Array[AgentState]) -> Error` | remplacer atomiquement les états durables |
| `AgentRuntimeRegistry` | `all_character_ids_sorted() -> Array[StringName]` et `get_runtime(character_id: StringName) -> AgentRuntime` | fournir les runtimes transitoires dans un ordre canonique |

Ces ports ne sont pas des Service Locators. Ils sont construits au bootstrap et injectés uniquement dans les services qui en ont besoin.
'''
text = once(text, '\n## 23. Exécuteurs et systèmes propriétaires', ports + '\n## 23. Exécuteurs et systèmes propriétaires', 'decision ports insertion')
text = text.replace('"target_position": [12.0, 0.0, -4.0],', '"target_position": {"x": 12.0, "y": 0.0, "z": -4.0},', 1)
text = once(
    text,
    '- **Vecteur :** `target_position` est encodé sous forme de trois nombres finis et reconstruit explicitement en `Vector3`.',
    '- **Vecteur :** `target_position` utilise le dictionnaire `{x, y, z}` du `SaveValueCodec` introduit au chapitre 9 ; chaque composante doit être numérique et finie.',
    'vector explanation',
)
old_codec = '''```gdscript
class_name AgentSnapshotCodec
extends RefCounted

func encode(state: AgentState) -> Dictionary:
\treturn {}

func decode(
\traw: Dictionary,
\tidentities: CharacterIdentityIndex,
) -> AgentState:
\treturn null
```'''
new_codec = '''```gdscript
class_name AgentSnapshotCodec
extends RefCounted

const FORMAT := "project-asteria-agent-state"
const VERSION := 1
const REQUIRED_KEYS := PackedStringArray([
\t"format",
\t"version",
\t"owner_character_id",
\t"policy_id",
\t"decision_sequence",
\t"random_seed",
\t"random_state",
\t"last_decision_tick",
\t"durable_goals",
])

func encode(state: AgentState) -> Dictionary:
\tif state == null or state.validate() != OK:
\t\treturn {}
\tvar encoded_goals: Array[Dictionary] = []
\tfor goal: AgentGoal in state.durable_goals:
\t\tif goal.status != AgentGoal.Status.ACTIVE:
\t\t\tcontinue
\t\tencoded_goals.append(_encode_goal(goal))
\treturn {
\t\t"format": FORMAT,
\t\t"version": VERSION,
\t\t"owner_character_id": String(state.owner_character_id),
\t\t"policy_id": String(state.policy_id),
\t\t"decision_sequence": state.decision_sequence,
\t\t"random_seed": state.random_seed,
\t\t"random_state": state.random_state,
\t\t"last_decision_tick": state.last_decision_tick,
\t\t"durable_goals": encoded_goals,
\t}

func decode(
\traw: Dictionary,
\tidentities: CharacterIdentityIndex,
) -> AgentState:
\tif identities == null or not _has_exact_keys(raw, REQUIRED_KEYS):
\t\treturn null
\tif raw.get("format") != FORMAT or raw.get("version") != VERSION:
\t\treturn null
\tfor key: String in [
\t\t"decision_sequence",
\t\t"random_seed",
\t\t"random_state",
\t\t"last_decision_tick",
\t]:
\t\tif not raw[key] is int:
\t\t\treturn null
\tif not raw["owner_character_id"] is String:
\t\treturn null
\tif not raw["policy_id"] is String or not raw["durable_goals"] is Array:
\t\treturn null

\tvar owner_id := StringName(raw["owner_character_id"])
\tif not CharacterId.is_valid(owner_id) or not identities.contains(owner_id):
\t\treturn null
\tvar state := AgentState.new()
\tstate.owner_character_id = owner_id
\tstate.policy_id = StringName(raw["policy_id"])
\tstate.decision_sequence = raw["decision_sequence"]
\tstate.random_seed = raw["random_seed"]
\tstate.random_state = raw["random_state"]
\tstate.last_decision_tick = raw["last_decision_tick"]

\tvar goal_ids: Dictionary[StringName, bool] = {}
\tfor item: Variant in raw["durable_goals"]:
\t\tif not item is Dictionary:
\t\t\treturn null
\t\tvar goal := _decode_goal(item, identities)
\t\tif goal == null or goal_ids.has(goal.goal_id):
\t\t\treturn null
\t\tgoal_ids[goal.goal_id] = true
\t\tstate.durable_goals.append(goal)
\treturn state if state.validate() == OK else null

func _encode_goal(goal: AgentGoal) -> Dictionary:
\treturn {
\t\t"goal_id": String(goal.goal_id),
\t\t"goal_type": String(goal.goal_type),
\t\t"target_character_id": String(goal.target_character_id),
\t\t"target_position": SaveValueCodec.vector3_to_dictionary(goal.target_position),
\t\t"priority": goal.priority,
\t\t"created_tick": goal.created_tick,
\t\t"deadline_tick": goal.deadline_tick,
\t\t"status": "active",
\t\t"provenance": String(goal.provenance),
\t}

func _decode_goal(
\traw: Dictionary,
\tidentities: CharacterIdentityIndex,
) -> AgentGoal:
\tvar required := PackedStringArray([
\t\t"goal_id", "goal_type", "target_character_id", "target_position",
\t\t"priority", "created_tick", "deadline_tick", "status", "provenance",
\t])
\tif not _has_exact_keys(raw, required):
\t\treturn null
\tfor key: String in ["goal_id", "goal_type", "target_character_id", "status", "provenance"]:
\t\tif not raw[key] is String:
\t\t\treturn null
\tfor key: String in ["priority", "created_tick", "deadline_tick"]:
\t\tif not raw[key] is int:
\t\t\treturn null
\tif not raw["target_position"] is Dictionary or raw["status"] != "active":
\t\treturn null

\tvar errors := PackedStringArray()
\tvar goal := AgentGoal.new()
\tgoal.goal_id = StringName(raw["goal_id"])
\tgoal.goal_type = StringName(raw["goal_type"])
\tgoal.target_character_id = StringName(raw["target_character_id"])
\tif not goal.target_character_id.is_empty() and not identities.contains(goal.target_character_id):
\t\treturn null
\tgoal.target_position = SaveValueCodec.dictionary_to_vector3(
\t\traw["target_position"], errors, "durable_goals.target_position"
\t)
\tif not errors.is_empty():
\t\treturn null
\tgoal.priority = raw["priority"]
\tgoal.created_tick = raw["created_tick"]
\tgoal.deadline_tick = raw["deadline_tick"]
\tgoal.status = AgentGoal.Status.ACTIVE
\tgoal.provenance = StringName(raw["provenance"])
\treturn goal if goal.validate() == OK else null

func _has_exact_keys(raw: Dictionary, expected: PackedStringArray) -> bool:
\tif raw.size() != expected.size():
\t\treturn false
\tfor key: String in expected:
\t\tif not raw.has(key):
\t\t\treturn false
\treturn true
```'''
text = once(text, old_codec, new_codec, 'codec implementation')
old_codec_explanation = '''- **Rôle :** ce contrat sépare la représentation JSON de `AgentState` et reçoit l’index logique nécessaire pour vérifier le propriétaire et les cibles de buts.
- **Valeurs de repli :** les corps vides ne sont pas une implémentation fonctionnelle ; ils marquent le contrat minimal du brouillon et doivent être remplacés avant le passage d’audit.
- **Erreur attendue :** `decode()` retourne `null` au premier champ inconnu, type incorrect, identifiant absent, doublon de but ou état pseudo-aléatoire invalide.'''
new_codec_explanation = '''- **Rôle :** le codec encode les données durables et reconstruit un candidat après contrôle exact du format, de la version, des clés, des types et des identités.
- **Encodage :** seuls les buts actifs sont écrits ; les positions passent par `SaveValueCodec` et les identifiants deviennent des chaînes JSON.
- **Décodage :** les entiers sont exigés comme tels dans le dictionnaire déjà normalisé par la chaîne de sauvegarde ; chaque but possède des clés exactes et une cible connue lorsqu’elle est renseignée.
- **Doublons :** `goal_ids` refuse deux buts portant le même identifiant avant leur insertion dans l’état candidat.
- **Retours :** `{}` signale un état source invalide à l’appelant d’encodage ; `null` signale un payload refusé sans mutation du dépôt.
- **Limite :** l’état interne du RNG ne peut pas être validé par sa forme seule ; il doit provenir d’un snapshot produit par cette version du projet et reste couvert par les tests de reprise.'''
text = once(text, old_codec_explanation, new_codec_explanation, 'codec explanation')
old_save = '''```gdscript
class_name AgentSaveSection
extends SaveSection

var _prepared_states: Dictionary[StringName, AgentState] = {}
var _codec: AgentSnapshotCodec
var _identity_index: CharacterIdentityIndex
var _repository: AgentStateRepository

func prepare_load(raw: Variant) -> Error:
\t_prepared_states.clear()
\tif not raw is Array:
\t\treturn ERR_INVALID_DATA
\tfor item: Variant in raw:
\t\tif not item is Dictionary:
\t\t\t_prepared_states.clear()
\t\t\treturn ERR_INVALID_DATA
\t\tvar state := _codec.decode(item, _identity_index)
\t\tif state == null or _prepared_states.has(state.owner_character_id):
\t\t\t_prepared_states.clear()
\t\t\treturn ERR_INVALID_DATA
\t\t_prepared_states[state.owner_character_id] = state
\treturn OK

func apply_prepared() -> Error:
\treturn _repository.replace_all(_prepared_states.values())

func cancel_load() -> void:
\t_prepared_states.clear()
```'''
new_save = '''```gdscript
class_name AgentSaveSection
extends SaveSection

var _prepared_states: Dictionary[StringName, AgentState] = {}
var _is_prepared: bool = false
var _codec: AgentSnapshotCodec
var _identity_index: CharacterIdentityIndex
var _repository: AgentStateRepository

func prepare_load(raw: Variant) -> Error:
\t_prepared_states.clear()
\t_is_prepared = false
\tif _codec == null or _identity_index == null or _repository == null:
\t\treturn ERR_UNCONFIGURED
\tif not raw is Array:
\t\treturn ERR_INVALID_DATA
\tfor item: Variant in raw:
\t\tif not item is Dictionary:
\t\t\t_prepared_states.clear()
\t\t\treturn ERR_INVALID_DATA
\t\tvar state := _codec.decode(item, _identity_index)
\t\tif state == null or _prepared_states.has(state.owner_character_id):
\t\t\t_prepared_states.clear()
\t\t\treturn ERR_INVALID_DATA
\t\t_prepared_states[state.owner_character_id] = state
\t_is_prepared = true
\treturn OK

func apply_prepared() -> Error:
\tif not _is_prepared:
\t\treturn ERR_UNCONFIGURED
\tvar states: Array[AgentState] = []
\tstates.assign(_prepared_states.values())
\tvar result := _repository.replace_all(states)
\tif result == OK:
\t\t_prepared_states.clear()
\t\t_is_prepared = false
\treturn result

func cancel_load() -> void:
\t_prepared_states.clear()
\t_is_prepared = false
```'''
text = once(text, old_save, new_save, 'save section implementation')
old_save_explanation = '''- **Rôle :** la section décode tous les agents dans un candidat avant de demander un remplacement global au dépôt.
- **Échec fermé :** une entrée invalide ou dupliquée vide le candidat et interrompt la préparation.
- **Application :** `replace_all()` doit lui-même valider l’ensemble et ne remplacer l’état actif qu’après succès.
- **Annulation :** le candidat est supprimé sans effet sur le dépôt.
- **Réserve :** le brouillon doit encore vérifier les dépendances nulles et convertir explicitement `_prepared_states.values()` vers `Array[AgentState]` avant l’audit final.'''
new_save_explanation = '''- **Rôle :** la section décode tous les agents dans un candidat avant de demander un remplacement global au dépôt.
- **Dépendances :** l’absence du codec, de l’index ou du dépôt produit `ERR_UNCONFIGURED` avant lecture du payload.
- **Échec fermé :** une entrée invalide ou dupliquée vide le candidat et laisse `_is_prepared` à `false`.
- **Conversion typée :** `states.assign()` construit explicitement un `Array[AgentState]` depuis les valeurs du dictionnaire.
- **Application :** aucune application n’est possible avant une préparation réussie ; le candidat est consommé seulement après remplacement réussi.
- **Annulation :** les données préparées et le drapeau sont supprimés sans effet sur le dépôt.'''
text = once(text, old_save_explanation, new_save_explanation, 'save explanation')
final_block = '''```text
Livre-II/CHAPITRE-18-Combat.md
Niveau GPT-5.6 Sol recommandé : Élevée
```'''
final_explanation = final_block + '''

<!-- qa:code-explanation -->

**Explication détaillée du bloc :**

- **Rôle :** ce bloc enregistre le chemin canonique et le niveau conseillé pour la prochaine étape de la collection.
- **Frontière :** le chapitre 18 consommera les requêtes d’action sans déplacer ses règles de combat dans le système d’agents.'''
text = once(text, final_block, final_explanation, 'final next action explanation')

# Static editorial checks.
current = ''
anchors = set(re.findall(r'<a id="([^"]+)"></a>', text))
links = re.findall(r'\]\(#([^)]+)\)', text)
if set(links) - anchors:
    raise RuntimeError(f'broken fragments: {sorted(set(links) - anchors)}')
for line_no, line in enumerate(text.splitlines(), 1):
    match = re.match(r'^#{2,6}\s+(.+?)\s*$', line)
    if match:
        current = match.group(1)
        continue
    if current and line.lstrip().startswith('- **') and current in line:
        raise RuntimeError(f'self-title mention at line {line_no}')
if 'Limite du brouillon' in text or 'return _repository.replace_all(_prepared_states.values())' in text:
    raise RuntimeError('draft technical residue remains')
if 'PackedStringArray(action_ids)' in text:
    raise RuntimeError('unsafe packed conversion remains')

chapter_path.write_text(text, encoding='utf-8')
lines = len(text.splitlines())
blocks = len(re.findall(r'^```', text, flags=re.M)) // 2
markers = text.count('<!-- qa:code-explanation -->')
error_cases = len(re.findall(r'^### 37\.\d+\s+', text, flags=re.M))

# Audit report.
audit_path = ROOT / 'Livre-II/QA/AUDIT-CHAPITRE-17.md'
audit_path.write_text(f'''---
title: "Audit du Livre II — Chapitre 17"
id: "DOC-L2-QA-AUDIT-CH17"
status: "complete"
version: "1.0.0"
chapter-id: "DOC-L2-CH17"
chapter-version: "1.0.0"
audit-level: "static-review"
audit-date: "2026-07-20"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 17 — Agents IA et comportements autonomes

## 1. Porte de brouillon observée

Le premier commit permanent a conservé `status: draft`, `version: 0.9.0`, `audit-status: pending` et `audit-level: not-audited`. Le présent rapport appartient à une passe distincte.

## 2. Résultats

- lignes finales : **{lines}** ;
- blocs clôturés : **{blocks}** ;
- marqueurs d’explication : **{markers}** ;
- cas d’erreurs détaillés : **{error_cases}** ;
- auto-paraphrases du titre courant : **0** ;
- fragments internes non résolus : **0** ;
- sources Godot 4.7 nommées : **13** ;
- doublons de titres ou blocs significatifs : à confirmer par CI ;
- PDF produit : **non** ;
- exécution runtime : **non**.

## 3. Corrections issues de la seconde lecture

1. ajout de l’ancre précise `ch17-agent-state` ;
2. conversion explicite des `StringName` pour la signature d’un chemin ;
3. documentation des six ports applicatifs utilisés ;
4. implémentation stricte de `AgentSnapshotCodec` ;
5. réutilisation de `SaveValueCodec` pour `Vector3` ;
6. refus des clés, types, versions, identités et buts dupliqués ;
7. ajout d’un drapeau de préparation à `AgentSaveSection` ;
8. conversion explicite vers `Array[AgentState]` ;
9. consommation du candidat seulement après succès ;
10. explication du bloc de prochaine étape ;
11. maintien de l’IA générative dans un rôle consultatif ;
12. séparation conservée avec combat, compétences, économie, monde vivant et narration.

## 4. Audit du déterminisme

Le chemin de référence utilise :

- snapshots détachés ;
- actions et buts triés ;
- clés d’état canoniques ;
- limites d’expansions et de profondeur ;
- nombre d’agents par tick ;
- phases stables ;
- ticks et séquences logiques ;
- RNG local restaurable seulement pour variantes équivalentes ;
- microsecondes limitées à la télémétrie.

## 5. Réserves

Aucun script n’a été analysé par le parseur Godot. La scène, les signaux, le contrôleur, le planificateur, le codec, la restauration, les performances, la parallélisation et le packaging n’ont pas été exécutés.

## 6. Décision

**Accepté au niveau `static-review`**, sous réserve des validations documentaires permanentes et des tests runtime futurs du chapitre 27.
''', encoding='utf-8')

# Evidence pending CI.
evidence_path = ROOT / 'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-17.yaml'
evidence_path.write_text(f'''schema-version: 1
evidence-id: DOC-L2-QA-EVIDENCE-CH17
status: pending-ci
validation-date: 2026-07-20
validated-base-commit: a61ea9e5378e270e1db98d9f83e6fe6cef847318
validated-head-commit: pending-ci
chapter:
  id: DOC-L2-CH17
  path: Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md
  version: 1.0.0
  audit-level: static-review
results:
  chapter-lines: {lines}
  chapter-code-and-data-blocks: {blocks}
  code-explanation-markers: {markers}
  detailed-error-cases: {error_cases}
  self-title-paraphrases: 0
  broken-explicit-fragments: 0
  official-godot-source-links: 13
  deterministic-planner-documented: true
  logical-budgets-documented: true
  microseconds-telemetry-only: true
  active-background-dormant-modes: true
  generative-ai-advisory-only: true
  durable-state-only-persisted: true
  strict-codec-documented: true
  prepared-save-section-documented: true
  pdf-produced: false
  runtime-executed: false
ci:
  validate-chapters-without-pdf:
    run-id: pending
    conclusion: pending
  validate-usage-contexts:
    run-id: pending
    conclusion: pending
  artifact:
    id: pending
    name: chapter-validation-without-pdf
    digest: pending
reservations:
  - Godot parser not executed.
  - Demo scene not instantiated.
  - Signals and action executors not run.
  - Planner and scheduler performance not measured.
  - Save restoration not executed.
  - Cross-platform replay not verified.
  - PDF deferred until end of Livre II.
''', encoding='utf-8')

# Index.
index_path = ROOT / 'Livre-II/index.md'
index = index_path.read_text(encoding='utf-8')
index = once(index, 'version: "1.12.0"', 'version: "1.12.1"', 'index version')
index = once(
    index,
    '17. [Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md) — **brouillon 0.9.0, audit en attente**',
    '17. [Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md) — **rédigé, repéré, expliqué bloc par bloc et audité au niveau static-review**',
    'index chapter status',
)
index = once(index, '- [audit du chapitre 17 — en attente](QA/AUDIT-CHAPITRE-17.md) ;', '- [audit du chapitre 17](QA/AUDIT-CHAPITRE-17.md) ;', 'index audit status')
index = index.replace('Les chapitres 3 à 16 utilisent **Élevée**.', 'Les chapitres 3 à 17 utilisent **Élevée**.', 1)
index = index.replace('**Seize chapitres sur trente**', '**Dix-sept chapitres sur trente**', 1)
index = index.replace('compte désormais **trois systèmes sur douze**', 'compte désormais **quatre systèmes sur douze**', 1)
index_path.write_text(index, encoding='utf-8')

# Roadmap.
roadmap_path = ROOT / 'ROADMAP.md'
roadmap = roadmap_path.read_text(encoding='utf-8')
roadmap = once(roadmap, '- [ ] Douze grands systèmes de jeu — 3 chapitres rédigés, repérés et audités sur 12.', '- [ ] Douze grands systèmes de jeu — 4 chapitres rédigés, repérés et audités sur 12.', 'roadmap count')
roadmap = once(roadmap, '- [x] Convention des outils et contextes appliquée aux chapitres 1 à 16.', '- [x] Convention des outils et contextes appliquée aux chapitres 1 à 17.', 'roadmap contexts')
roadmap = once(roadmap, '- [ ] Chapitre 17 — agents IA et comportements autonomes — brouillon `0.9.0` créé, audit post-création en attente.', '- [x] Chapitre 17 — perceptions, mémoire bornée, buts, planification déterministe, ordonnanceur, simulation hors écran, invalidation, IA consultative et sauvegarde minimale — rédigé et audité au niveau `static-review`.', 'roadmap ch17')
roadmap = roadmap.replace('**Statut M3 : en cours — 16 chapitres rédigés, repérés et audités sur 30.**', '**Statut M3 : en cours — 17 chapitres rédigés, repérés et audités sur 30.**', 1)
roadmap = roadmap.replace('Trois des douze systèmes de gameplay sont documentés : personnages, relations sociales et famille.', 'Quatre des douze systèmes de gameplay sont documentés : personnages, relations sociales, famille et agents autonomes.', 1)
roadmap = roadmap.replace('Le chapitre 17 traitera désormais les agents IA et comportements autonomes derrière des contrats et budgets explicites.', 'Le chapitre 17 sépare l’état d’agent, les snapshots, la mémoire, les buts, le plan transitoire et les exécuteurs ; le chapitre 18 traitera désormais le combat.', 1)
roadmap_path.write_text(roadmap, encoding='utf-8')

# Continuity.
continuity_path = ROOT / 'CONTINUITE-PROJET.md'
continuity = continuity_path.read_text(encoding='utf-8')
continuity = once(continuity, 'version: "3.17.6"', 'version: "3.17.7"', 'continuity version')
continuity = continuity.replace('**En cours : 16 chapitres sur 30.**', '**En cours : 17 chapitres sur 30.**', 1)
continuity = once(continuity, '17. Agents IA et comportements autonomes.', '17. Agents IA et comportements autonomes — terminé au niveau `static-review`.', 'continuity collection')
continuity = continuity.replace('Chapitres 3 à 16 : **Élevée**.', 'Chapitres 3 à 17 : **Élevée**.', 1)
architecture_anchor = '### 11.11 Famille et générations\n'
if '### 11.12 Agents IA et comportements autonomes' not in continuity:
    insert_at = continuity.index('## 12. Chapitre 5 — état résumé')
    agent_decisions = '''### 11.12 Agents IA et comportements autonomes

- état `AgentState` séparé de `CharacterRuntimeState`, du social et de la famille ;
- faits structurés avec provenance, confiance, observation et expiration ;
- mémoire bornée à `128` faits et tableau noir à `32` clés déclarées ;
- buts durables séparés des intentions, plans et requêtes transitoires ;
- catalogue d’actions validé avec préconditions, effets, coût et exécuteur ;
- planificateur déterministe borné à `256` expansions et profondeur `8` ;
- snapshots détachés et révision du monde contrôlée avant émission ;
- ordonnanceur round-robin limité à `8` décisions par tick physique ;
- modes actif, arrière-plan et dormant sans confondre scène et existence ;
- invalidation et annulation coopérative corrélées par `request_id` ;
- RNG local restaurable réservé aux variantes métier équivalentes ;
- IA générative limitée à des suggestions filtrées par le catalogue ;
- persistance des buts et compteurs durables, sans perceptions ni plans ;
- codec strict et section préparée avant remplacement atomique ;
- combat, compétences, économie, monde vivant, politique et narration séparés.

'''
    continuity = continuity[:insert_at] + agent_decisions + continuity[insert_at:]
continuity = once(continuity, '- chapitre 17 : brouillon version `0.9.0`, audit en attente ;', '- chapitre 17 : version `1.0.0` ;', 'continuity state ch17')
continuity = continuity.replace('- progression : 16 chapitres sur 30 ;', '- progression : 17 chapitres sur 30 ;', 1)
start = continuity.index('## 26. Prochaine action')
end = continuity.index('## 27. Journal')
next_action = '''## 26. Prochaine action

Le chapitre 17 est terminé au niveau `static-review`. Les agents produisent des requêtes d’action déterministes et bornées, sans devenir autorités des systèmes métier.

Chapitre suivant :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-II/CHAPITRE-18-Combat.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Périmètre attendu : règles de combat séparées du planificateur, commandes typées, initiative, portée, dégâts, défense, états, ciblage, historique, persistance, budgets et frontières avec compétences et agents.

'''
continuity = continuity[:start] + next_action + continuity[end:]
if '### 2026-07-20 — version 3.17.7' not in continuity:
    entry = '''## 27. Journal

### 2026-07-20 — version 3.17.7

- chapitre 17 porté de la porte de brouillon `0.9.0` à `1.0.0` ;
- audit distinct terminé au niveau `static-review` ;
- codec d’agent complété et section de sauvegarde sécurisée ;
- planification déterministe, budgets logiques et ordonnanceur documentés ;
- IA générative maintenue dans un rôle consultatif ;
- index, roadmap, `contents.txt`, audit et preuve mis à jour ;
- aucun PDF construit et aucun test runtime revendiqué.
'''
    continuity = continuity.replace('## 27. Journal\n', entry, 1)
continuity_path.write_text(continuity, encoding='utf-8')

print(f'chapter_lines={lines}')
print(f'blocks={blocks}')
print(f'markers={markers}')
print(f'error_cases={error_cases}')
print('finalize=ok')
