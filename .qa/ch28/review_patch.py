#!/usr/bin/env python3
from pathlib import Path

STAMP = "2026-07-22T03:26:36+02:00"
CHAPTER = Path("Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md")
AUDIT = Path("Livre-II/QA/AUDIT-CHAPITRE-28.md")
PROOF = Path("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-28.yaml")
CONTINUITY = Path("CONTINUITE-PROJET.md")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


chapter = CHAPTER.read_text(encoding="utf-8")
chapter = replace_once(chapter, 'version: "1.0.0"', 'version: "1.0.1"', "chapter version")
chapter = replace_once(chapter, 'last-verified: "2026-07-22T03:02:36+02:00"', f'last-verified: "{STAMP}"', "chapter verified")
chapter = replace_once(chapter, 'audit-date: "2026-07-22T03:02:36+02:00"', f'audit-date: "{STAMP}"', "chapter audit date")

old_context = '''func child(
    child_correlation_id: String = correlation_id,
    child_causation_id: StringName = causation_id
) -> TelemetryContext:
    var value := TelemetryContext.new()
    value.run_id = run_id
    value.correlation_id = child_correlation_id
    value.causation_id = child_causation_id
    value.logical_tick = logical_tick
    return value'''
new_context = '''func child(
    child_correlation_id: String = "",
    child_causation_id: StringName = &""
) -> TelemetryContext:
    var value := TelemetryContext.new()
    value.run_id = run_id
    value.correlation_id = (
        correlation_id
        if child_correlation_id.is_empty()
        else child_correlation_id
    )
    value.causation_id = (
        causation_id
        if child_causation_id == &""
        else child_causation_id
    )
    value.logical_tick = logical_tick
    return value'''
chapter = replace_once(chapter, old_context, new_context, "telemetry context defaults")
chapter = replace_once(
    chapter,
    "- **Paramètres et types importants :** Un tick négatif signifie qu’aucun tick logique n’appartient à l’opération.\n- **Valeur de retour ou code d’échec :** `child()` crée une copie détachée et conserve le `run_id`.",
    "- **Paramètres et types importants :** Un tick négatif signifie qu’aucun tick logique n’appartient à l’opération ; les chaînes vides demandent de conserver la corrélation et la cause du parent.\n- **Valeur de retour ou code d’échec :** `child()` crée une copie détachée, conserve le `run_id` et remplace uniquement les identifiants explicitement fournis.",
    "telemetry context explanation",
)

chapter = replace_once(
    chapter,
    "var _policy: TelemetryPolicy\n\nfunc build(event_value: TelemetryEvent) -> Dictionary:",
    "var _policy: TelemetryPolicy\n\nfunc _init(policy: TelemetryPolicy) -> void:\n    _policy = policy\n\nfunc build(event_value: TelemetryEvent) -> Dictionary:",
    "record builder injection",
)
chapter = replace_once(
    chapter,
    "- **Responsabilités des classes ou fonctions :** Le builder rassemble les champs communs et délègue la minimisation à la politique.",
    "- **Responsabilités des classes ou fonctions :** Le builder reçoit sa politique obligatoire à la construction, rassemble les champs communs et lui délègue la minimisation.",
    "record builder explanation",
)

chapter = replace_once(
    chapter,
    "var _builder: TelemetryRecordBuilder\nvar _file: FileAccess\nvar _pending_since_flush := 0\n\nfunc open(run_id: String) -> Error:",
    "var _builder: TelemetryRecordBuilder\nvar _file: FileAccess\nvar _pending_since_flush := 0\n\nfunc _init(builder: TelemetryRecordBuilder) -> void:\n    _builder = builder\n\nfunc open(run_id: String) -> Error:",
    "jsonl sink injection",
)
chapter = replace_once(
    chapter,
    "- **Déroulement ou instructions importantes :** Le dossier est créé, le fichier existant est ouvert sans troncature, puis le curseur est placé à la fin.",
    "- **Déroulement ou instructions importantes :** Le builder obligatoire est injecté à la construction ; le dossier est créé, le fichier existant est ouvert sans troncature, puis le curseur est placé à la fin.",
    "jsonl sink explanation",
)

old_logger = '''class_name ThreadedEngineLogger
extends Logger

var _mutex := Mutex.new()
var _pending: Array[Dictionary] = []

func _log_message(message: String, error: bool) -> void:
    var record := {
        "kind": "engine_message",
        "stderr": error,
        "message": message.left(512),
    }
    _mutex.lock()
    _pending.append(record)
    _mutex.unlock()

func drain() -> Array[Dictionary]:
    _mutex.lock()
    var result := _pending.duplicate(true)
    _pending.clear()
    _mutex.unlock()
    return result

func pending_count() -> int:
    _mutex.lock()
    var result := _pending.size()
    _mutex.unlock()
    return result'''
new_logger = '''class_name ThreadedEngineLogger
extends Logger

const MAX_PENDING_RECORDS := 4096

var _mutex := Mutex.new()
var _pending: Array[Dictionary] = []
var _dropped_records := 0

func _enqueue(record: Dictionary) -> void:
    _mutex.lock()
    if _pending.size() >= MAX_PENDING_RECORDS:
        _pending.pop_front()
        _dropped_records += 1
    _pending.append(record)
    _mutex.unlock()

func _log_message(message: String, error: bool) -> void:
    _enqueue({
        "kind": "engine_message",
        "stderr": error,
        "message": message.left(512),
    })

func drain() -> Array[Dictionary]:
    _mutex.lock()
    var result := _pending.duplicate(true)
    _pending.clear()
    _mutex.unlock()
    return result

func pending_count() -> int:
    _mutex.lock()
    var result := _pending.size()
    _mutex.unlock()
    return result

func dropped_count() -> int:
    _mutex.lock()
    var result := _dropped_records
    _mutex.unlock()
    return result'''
chapter = replace_once(chapter, old_logger, new_logger, "bounded engine logger")
chapter = replace_once(
    chapter,
    "- **Responsabilités des classes ou fonctions :** Les callbacks se contentent d’enfiler ; `drain()` transfère les données au thread principal.\n- **Sécurité des threads :** Le mutex protège le tableau pendant la copie et la remise à zéro.\n- **Effets de bord :** Aucun appel à `print`, `push_error` ou au sink n’a lieu depuis le logger, ce qui évite la récursion.\n- **Limites et réserves :** La file doit recevoir une capacité maximale afin qu’un flot moteur anormal ne consomme pas toute la mémoire.",
    "- **Responsabilités des classes ou fonctions :** Les callbacks se contentent d’enfiler ; `drain()` transfère les données au thread principal et `dropped_count()` expose les pertes cumulées.\n- **Sécurité des threads :** Le mutex protège la capacité, la file, la copie, la remise à zéro et le compteur de pertes.\n- **Effets de bord :** Lorsque la capacité de `4096` est atteinte, le plus ancien enregistrement est remplacé et le compteur augmente ; aucun appel à `print`, `push_error` ou au sink n’a lieu depuis le logger.\n- **Invariants protégés :** Un flot moteur anormal ne peut pas faire croître la file sans borne et la saturation reste observable.",
    "bounded logger explanation",
)
chapter = replace_once(
    chapter,
    "    _mutex.lock()\n    _pending.append(record)\n    _mutex.unlock()\n```\n\n<!-- qa:code-explanation -->\n\n**Explication structurée du bloc :**\n\n- **Paramètres et types importants :** Le moteur fournit emplacement, code, justification, type et piles de scripts.",
    "    _enqueue(record)\n```\n\n<!-- qa:code-explanation -->\n\n**Explication structurée du bloc :**\n\n- **Paramètres et types importants :** Le moteur fournit emplacement, code, justification, type et piles de scripts.",
    "engine error enqueue",
)
chapter = replace_once(
    chapter,
    '        "telemetry_queue_depth": _engine_logger.pending_count(),\n',
    '        "telemetry_queue_depth": _engine_logger.pending_count(),\n        "telemetry_dropped_records": _engine_logger.dropped_count(),\n',
    "health saturation metric",
)
chapter = replace_once(
    chapter,
    "- **Organisation des données :** Le snapshot réunit des compteurs déjà possédés par leurs systèmes.",
    "- **Organisation des données :** Le snapshot réunit des compteurs déjà possédés par leurs systèmes et rend visible la saturation cumulée du logger.",
    "health snapshot explanation",
)

CHAPTER.write_text(chapter, encoding="utf-8")
chapter_lines = len(chapter.splitlines())

# Update audit and document the second technical reading.
audit = AUDIT.read_text(encoding="utf-8")
audit = replace_once(audit, 'version: "1.0.0"', 'version: "1.0.1"', "audit version")
audit = replace_once(audit, 'chapter-version: "1.0.0"', 'chapter-version: "1.0.1"', "audit chapter version")
audit = replace_once(audit, 'audit-date: "2026-07-22T03:02:36+02:00"', f'audit-date: "{STAMP}"', "audit date")
audit = replace_once(audit, 'last-verified: "2026-07-22T03:02:36+02:00"', f'last-verified: "{STAMP}"', "audit verified")
audit = replace_once(audit, "- lignes finales : **2091** ;", f"- lignes finales : **{chapter_lines}** ;", "audit line count")
audit = replace_once(
    audit,
    "- aucun des calques terminologiques interdits par le validateur n’est présent.",
    "- aucun des calques terminologiques interdits par le validateur n’est présent ;\n- les dépendances de `TelemetryRecordBuilder` et `JsonlTelemetrySink` sont injectées par leurs constructeurs ;\n- `TelemetryContext.child()` utilise des sentinelles constantes et ne dépend pas d’une valeur membre dans sa signature ;\n- la file du `Logger` est bornée à `4096` entrées et expose un compteur de pertes ;\n- le snapshot de santé rend la saturation du logger observable.",
    "audit second reading controls",
)
AUDIT.write_text(audit, encoding="utf-8")

# Reset evidence until the corrected head is validated.
proof = PROOF.read_text(encoding="utf-8")
proof = replace_once(proof, "status: complete", "status: pending", "proof status")
proof = replace_once(proof, "validated-head-commit: da0524e373f48c8b9ef7495399bac229918fa7f8", "validated-head-commit: pending", "proof head")
proof = replace_once(proof, "  version: 1.0.0", "  version: 1.0.1", "proof chapter version")
proof = replace_once(proof, "  blocking-errors: 0", "  blocking-errors: pending", "proof errors")
proof = replace_once(proof, "  warnings: 1", "  warnings: pending", "proof warnings")
proof = replace_once(proof, "  chapter-lines: 2091", f"  chapter-lines: {chapter_lines}", "proof line count")
proof = replace_once(proof, "    run-id: 29882825771", "    run-id: pending", "proof chapter run")
proof = replace_once(proof, "    conclusion: success", "    conclusion: pending", "proof chapter conclusion")
proof = replace_once(proof, "    run-id: 29882825815", "    run-id: pending", "proof context run")
proof = replace_once(proof, "    conclusion: success", "    conclusion: pending", "proof context conclusion")
proof = replace_once(proof, "    id: 8515408912", "    id: pending", "proof artifact id")
proof = replace_once(proof, "    digest: sha256:a23b5c03cda7db7868130dc66ecfe123a4229b46347d3a2aac57f331d00713be", "    digest: pending", "proof artifact digest")
proof = replace_once(proof, "  commit: e4d4b4a961abf9fde94082237b6ff1b0507d428a", "  commit: pending", "proof closure")
PROOF.write_text(proof, encoding="utf-8")

continuity = CONTINUITY.read_text(encoding="utf-8")
continuity = replace_once(continuity, 'version: "3.28.0"', 'version: "3.28.1"', "continuity version")
continuity = replace_once(continuity, 'last-updated: "2026-07-22T03:13:32+02:00"', f'last-updated: "{STAMP}"', "continuity timestamp")
continuity = replace_once(continuity, '- chapitre 28 : version `1.0.0` ;', '- chapitre 28 : version `1.0.1` ;', "continuity chapter version")
journal = f'''### {STAMP} — version 3.28.1

- seconde lecture technique du chapitre 28 effectuée avant fusion ;
- dépendances de construction rendues explicites pour le builder et le sink JSONL ;
- paramètres par défaut de `TelemetryContext.child()` remplacés par des sentinelles constantes ;
- file du logger moteur bornée à `4096` entrées avec compteur de pertes exposé dans l’état de santé ;
- chapitre porté à `1.0.1`, audit à `1.0.1` et preuve QA remise en attente ;
- aucun test runtime revendiqué et aucun PDF construit.

'''
continuity = replace_once(continuity, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "continuity journal")
CONTINUITY.write_text(continuity, encoding="utf-8")

print(f"Chapter 28 technical review patch prepared: {chapter_lines} lines.")
