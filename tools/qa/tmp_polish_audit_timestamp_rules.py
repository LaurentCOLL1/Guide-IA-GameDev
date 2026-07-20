from pathlib import Path

ROOT = Path('.')


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding='utf-8')


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding='utf-8')


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new, 1)


continuity_path = 'CONTINUITE-PROJET.md'
continuity = read(continuity_path)
old_code_rule = '''Tout bloc de code significatif doit être expliqué avec un niveau de détail proportionné à sa complexité. L’explication couvre au minimum son rôle, son emplacement, ses entrées et types, ses paramètres, ses retours et erreurs, ses effets de bord, les instructions non évidentes, les invariants protégés, le résultat attendu et les erreurs fréquentes. Une phrase générique ne suffit pas lorsqu’un lecteur débutant doit encore deviner le fonctionnement d’une ligne importante.\n\nCette règle est une porte d’audit bloquante. Elle s’applique aux nouveaux chapitres et aux corrections rétroactives. Les chapitres 15 et 16 doivent recevoir un enrichissement pédagogique de leurs blocs de code avant le démarrage du chapitre 17.\n'''
new_code_rule = '''Tout bloc de code significatif doit recevoir une explication proportionnée à sa complexité et limitée aux informations réellement utiles : entrées et types, paramètres, valeurs de retour, effets de bord, instructions non évidentes, invariants, résultat attendu et limites pertinentes. `Rôle` est conservé seulement lorsqu’il nomme un contrat, une fonction, une transformation ou une responsabilité concrète. `Emplacement` est omis lorsque le chemin est déjà donné par le contexte adjacent. Les règles générales de syntaxe déjà expliquées ne sont pas répétées.\n\nCette règle est une porte d’audit bloquante pour les nouveaux chapitres comme pour les corrections rétroactives. Les chapitres 15 et 16 ont été corrigés selon cette règle ; le chapitre 17 applique en plus la nomenclature précise des retours, refus et statuts.\n'''
continuity = replace_once(continuity, old_code_rule, new_code_rule, 'continuity code rule')
old_metadata = '''```yaml\nstatus: "reviewed"\naudit-status: "complete"\naudit-date: "YYYY-MM-DD"\naudit-level: "static-review"\naudit-report: "Livre-II/QA/..."\nusage-context-standard: "DOC-V0-ANN-CONTEXTES"\nrecommended-reasoning: "GPT-5.6 Sol — Moyenne ou Élevée"\n```\n'''
new_metadata = '''```yaml\nstatus: "reviewed"\nlast-verified: "YYYY-MM-DDTHH:MM:SS±HH:MM"\naudit-status: "complete"\naudit-date: "YYYY-MM-DDTHH:MM:SS±HH:MM"\naudit-level: "static-review"\naudit-report: "Livre-II/QA/..."\nusage-context-standard: "DOC-V0-ANN-CONTEXTES"\nrecommended-reasoning: "GPT-5.6 Sol — Moyenne ou Élevée"\n```\n'''
continuity = replace_once(continuity, old_metadata, new_metadata, 'continuity metadata example')
continuity = replace_once(
    continuity,
    'Le protocole officiel est `Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md`, version `1.7.1`.',
    'Le protocole officiel est `Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md`, version `1.7.3`.',
    'continuity protocol version',
)
write(continuity_path, continuity)

protocol_path = 'Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md'
protocol = read(protocol_path)
old_protocol_metadata = '''```yaml\naudit-status: "complete"\naudit-date: "AAAA-MM-JJ"\naudit-report: "Livre-II/QA/<rapport>.md"\naudit-level: "static-review"\nusage-context-standard: "DOC-V0-ANN-CONTEXTES"\nrecommended-reasoning: "GPT-5.6 Sol — Moyenne ou Élevée"\n```\n'''
new_protocol_metadata = '''```yaml\nlast-verified: "AAAA-MM-JJTHH:MM:SS±HH:MM"\naudit-status: "complete"\naudit-date: "AAAA-MM-JJTHH:MM:SS±HH:MM"\naudit-report: "Livre-II/QA/<rapport>.md"\naudit-level: "static-review"\nusage-context-standard: "DOC-V0-ANN-CONTEXTES"\nrecommended-reasoning: "GPT-5.6 Sol — Moyenne ou Élevée"\n```\n'''
protocol = replace_once(protocol, old_protocol_metadata, new_protocol_metadata, 'protocol metadata example')
protocol = replace_once(
    protocol,
    '`static-review` signifie que les explications, commandes et extraits ont été relus contre les références officielles, sans prétendre qu’ils ont tous été exécutés.',
    'Les champs `last-verified` et `audit-date` sont des chaînes ISO 8601 entre guillemets et incluent obligatoirement les secondes ainsi qu’un décalage UTC explicite. `static-review` signifie que les explications, commandes et extraits ont été relus contre les références officielles, sans prétendre qu’ils ont tous été exécutés.',
    'protocol metadata explanation',
)
write(protocol_path, protocol)

validator_path = 'tools/validate_chapters.py'
validator = read(validator_path)
validator = replace_once(
    validator,
    'VALID_REASONING = {"GPT-5.6 Sol — Moyenne", "GPT-5.6 Sol — Élevée"}\n',
    'VALID_REASONING = {"GPT-5.6 Sol — Moyenne", "GPT-5.6 Sol — Élevée"}\nISO_TIMESTAMP_RE = re.compile(r"^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(?:Z|[+-]\\d{2}:\\d{2})$")\n',
    'validator timestamp regex',
)
old_helper = '''def validate_timestamp(value: object, field_name: str, rel: str, errors: list[str]) -> None:\n    if not isinstance(value, str):\n        errors.append(f"Métadonnée {field_name} non textuelle ou non horodatée : {rel}")\n        return\n    try:\n        parsed = datetime.fromisoformat(value)\n    except ValueError:\n        errors.append(f"Métadonnée {field_name} hors format ISO 8601 : {rel} — {value}")\n        return\n    if parsed.tzinfo is None or parsed.utcoffset() is None:\n        errors.append(f"Métadonnée {field_name} sans décalage UTC : {rel} — {value}")\n    if 'T' not in value or parsed.second is None:\n        errors.append(f"Métadonnée {field_name} sans heure complète : {rel} — {value}")\n'''
new_helper = '''def validate_timestamp(value: object, field_name: str, rel: str, errors: list[str]) -> None:\n    if not isinstance(value, str) or ISO_TIMESTAMP_RE.fullmatch(value) is None:\n        errors.append(\n            f"Métadonnée {field_name} hors format ISO 8601 horodaté "\n            f"(secondes et décalage UTC obligatoires) : {rel} — {value}"\n        )\n        return\n    try:\n        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))\n    except ValueError:\n        errors.append(f"Métadonnée {field_name} invalide : {rel} — {value}")\n        return\n    if parsed.tzinfo is None or parsed.utcoffset() is None:\n        errors.append(f"Métadonnée {field_name} sans décalage UTC : {rel} — {value}")\n'''
validator = replace_once(validator, old_helper, new_helper, 'validator helper precision')
write(validator_path, validator)

assert 'audit-date: "YYYY-MM-DDTHH:MM:SS±HH:MM"' in continuity
assert 'version `1.7.3`' in continuity
assert 'audit-date: "AAAA-MM-JJTHH:MM:SS±HH:MM"' in protocol
assert 'ISO_TIMESTAMP_RE.fullmatch' in validator
print('timestamp consistency polished')
