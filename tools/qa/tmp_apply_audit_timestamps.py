from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path('.')
STAMP = datetime.now(ZoneInfo('Europe/Paris')).replace(microsecond=0).isoformat()


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding='utf-8')


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding='utf-8')


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new, 1)


# Chapter 17 metadata.
chapter_path = 'Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md'
chapter = read(chapter_path)
chapter = replace_once(chapter, 'version: "1.0.1"', 'version: "1.0.2"', 'chapter version')
chapter = replace_once(chapter, 'last-verified: "2026-07-20"', f'last-verified: "{STAMP}"', 'chapter last-verified')
chapter = replace_once(chapter, 'audit-date: "2026-07-20"', f'audit-date: "{STAMP}"', 'chapter audit-date')
write(chapter_path, chapter)

# Audit report metadata and addendum.
audit_path = 'Livre-II/QA/AUDIT-CHAPITRE-17.md'
audit = read(audit_path)
audit = audit.replace('version: "1.0.1"', 'version: "1.0.2"', 1)
audit = replace_once(audit, 'chapter-version: "1.0.1"', 'chapter-version: "1.0.2"', 'audit chapter version')
audit = replace_once(audit, 'audit-date: "2026-07-20"', f'audit-date: "{STAMP}"\nlast-verified: "{STAMP}"', 'audit timestamp')
audit_addendum = f'''\n\n## 8. Addendum d’horodatage — version 1.0.2\n\nLa vérification corrective est horodatée en heure locale `Europe/Paris` avec le format ISO 8601 et son décalage UTC : `{STAMP}`. Les métadonnées `audit-date` et `last-verified` portent désormais l’heure, les minutes, les secondes et l’offset.\n\nLes anciens audits qui ne disposent que d’une date ne reçoivent pas d’heure reconstruite artificiellement. Ils adopteront ce format lors de leur prochaine modification auditée.\n'''
if '## 8. Addendum d’horodatage' not in audit:
    audit = audit.rstrip() + audit_addendum
write(audit_path, audit)

# QA protocol: timestamp convention and terminology permanence.
protocol_path = 'Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md'
protocol = read(protocol_path)
protocol = replace_once(protocol, 'version: "1.7.2"', 'version: "1.7.3"', 'protocol version')
protocol = replace_once(protocol, 'last-verified: "2026-07-20"', f'last-verified: "{STAMP}"', 'protocol last-verified')
protocol_anchor = '''Le libellé `Erreur fréquente` est réservé à un véritable piège que le lecteur pourrait reproduire. S’il apparaît, il relève de Q1.2 et doit être accompagné d’un exemple fautif et d’une correction, ou être reformulé avec l’un des libellés précis ci-dessus.\n'''
protocol_rule = f'''\n### Q1.1.1 — Horodatage des vérifications et audits\n\nÀ partir du chapitre 17 version `1.0.2`, et pour tout nouveau chapitre ou document d’audit, `last-verified` et `audit-date` utilisent une chaîne ISO 8601 complète et entre guillemets : date, heure, minutes, secondes et décalage UTC. Le fuseau de référence du projet est `Europe/Paris` ; l’offset enregistré suit donc l’heure légale applicable, par exemple `+01:00` ou `+02:00`.\n\nUne heure ne doit jamais être inventée rétroactivement. Les documents historiques qui portent seulement `YYYY-MM-DD` conservent cette valeur jusqu’à leur prochaine révision réellement vérifiée. Dès qu’un chapitre ou son audit est modifié et revalidé, les deux champs sont actualisés avec l’heure effective de cette nouvelle vérification.\n\nLe validateur impose ce format au chapitre 17 et aux chapitres suivants, ainsi qu’à leurs rapports d’audit.\n'''
if '### Q1.1.1 — Horodatage des vérifications et audits' not in protocol:
    protocol = replace_once(protocol, protocol_anchor, protocol_anchor + protocol_rule, 'protocol timestamp insertion')
write(protocol_path, protocol)

# Continuity: record the complete terminology and timestamp rules.
continuity_path = 'CONTINUITE-PROJET.md'
continuity = read(continuity_path)
continuity = replace_once(continuity, 'version: "3.17.8"', 'version: "3.17.9"', 'continuity version')
continuity = replace_once(continuity, 'last-updated: "2026-07-20"', f'last-updated: "{STAMP}"', 'continuity last-updated')
continuity_anchor = '''Les sections détaillées portent `<!-- qa:error-correction-section -->`. Un index compact de symptômes peut porter `<!-- qa:error-correction-index -->` uniquement s’il renvoie vers des exemples détaillés conformes.\n'''
continuity_rules = f'''\nHors d’une section pédagogique d’erreurs ou de corrections, le mot `erreur` ne sert pas de libellé générique. Employer `Valeurs de retour` pour des résultats ou sentinelles, `Codes de retour` pour les valeurs `Error`, `Refus contrôlé` pour un rejet normal par contrat, `Statuts à distinguer` pour comparer des états métier, et `Traitement du résultat` lorsque l’appelant doit consommer ou journaliser le retour. `Erreur fréquente` est réservé à un piège reproductible accompagné d’un exemple fautif et d’une correction.\n\nÀ partir du chapitre 17 version `1.0.2`, `last-verified` et `audit-date` sont des chaînes ISO 8601 complètes avec heure, secondes et décalage UTC, dans le fuseau `Europe/Paris`. Une heure historique inconnue n’est jamais reconstruite : les documents antérieurs passent au format horodaté seulement lors de leur prochaine révision réellement auditée.\n'''
if 'Hors d’une section pédagogique d’erreurs ou de corrections' not in continuity:
    continuity = replace_once(continuity, continuity_anchor, continuity_anchor + continuity_rules, 'continuity rules insertion')
continuity = replace_once(continuity, '- chapitre 17 : version `1.0.1` ;', '- chapitre 17 : version `1.0.2` ;', 'continuity chapter state')
journal = f'''### {STAMP} — version 3.17.9\n\n- nomenclature des résultats négatifs ajoutée explicitement à la continuité du projet ;\n- `Valeurs de retour`, `Codes de retour`, `Refus contrôlé`, `Statuts à distinguer` et `Traitement du résultat` deviennent les libellés permanents hors sections pédagogiques d’erreurs ;\n- `Erreur fréquente` reste réservé aux pièges accompagnés d’un exemple fautif et d’une correction ;\n- `last-verified` et `audit-date` adoptent le format ISO 8601 horodaté avec offset à partir du chapitre 17 ;\n- chapitre et audit 17 portés en version `1.0.2`, protocole QA en version `1.7.3` ;\n- aucune heure rétroactive inconnue n’est inventée.\n\n'''
if 'version 3.17.9' not in continuity:
    continuity = replace_once(continuity, '## 27. Journal\n\n', '## 27. Journal\n\n' + journal, 'continuity journal')
write(continuity_path, continuity)

# Index and roadmap.
index_path = 'Livre-II/index.md'
index_text = read(index_path)
index_text = replace_once(index_text, 'version: "1.12.2"', 'version: "1.12.3"', 'index version')
index_text = replace_once(
    index_text,
    'terminologie des retours clarifiée et audité au niveau static-review',
    'terminologie des retours clarifiée, métadonnées d’audit horodatées et audité au niveau static-review',
    'index chapter 17 status',
)
write(index_path, index_text)

roadmap_path = 'ROADMAP.md'
roadmap = read(roadmap_path)
roadmap_anchor = '- [x] Clarification du chapitre 17 — intervalles nominaux explicités, codes de retour distingués des erreurs pédagogiques et échéances reportées conservées.\n'
roadmap_line = '- [x] Horodatage des audits — `last-verified` et `audit-date` utilisent ISO 8601 avec heure et offset à partir du chapitre 17, sans heure rétroactive inventée.\n'
if roadmap_line not in roadmap:
    roadmap = replace_once(roadmap, roadmap_anchor, roadmap_anchor + roadmap_line, 'roadmap timestamp line')
write(roadmap_path, roadmap)

# Evidence returns to pending until CI validates this revision.
evidence_path = 'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-17.yaml'
evidence = read(evidence_path)
evidence = replace_once(evidence, 'status: complete', 'status: pending-ci', 'evidence status')
evidence = replace_once(evidence, 'validated-head-commit: 58f090584911a5f30a585334a66a40e477a88955', 'validated-head-commit: pending-ci', 'evidence head')
evidence = replace_once(evidence, '  version: 1.0.1', '  version: 1.0.2', 'evidence chapter version')
evidence = replace_once(evidence, '  ambiguous-error-labels-outside-section-37: 0', '  ambiguous-error-labels-outside-section-37: 0\n  audit-timestamps-with-offset: true', 'evidence timestamp result')
evidence = replace_once(evidence, '    run-id: 29725806307\n    conclusion: success', '    run-id: pending\n    conclusion: pending', 'evidence chapter CI')
evidence = replace_once(evidence, '    run-id: 29725806301\n    conclusion: success', '    run-id: pending\n    conclusion: pending', 'evidence context CI')
evidence = replace_once(evidence, '    id: 8454174626', '    id: pending', 'evidence artifact id')
evidence = replace_once(evidence, '    digest: sha256:c98e63b798fbcd999252353724165cb956dd0f28b5d1e65e5811b21f03fcf5f0', '    digest: pending', 'evidence artifact digest')
write(evidence_path, evidence)

# Validator: require ISO 8601 timestamps with an offset for chapter 17+ and audit reports.
validator_path = 'tools/validate_chapters.py'
validator = read(validator_path)
validator = replace_once(validator, 'import argparse\nimport re\nimport sys', 'import argparse\nfrom datetime import datetime\nimport re\nimport sys', 'validator datetime import')
helper_anchor = '''def normalize_heading(value: str) -> str:\n'''
helper = '''def validate_timestamp(value: object, field_name: str, rel: str, errors: list[str]) -> None:\n    if not isinstance(value, str):\n        errors.append(f"Métadonnée {field_name} non textuelle ou non horodatée : {rel}")\n        return\n    try:\n        parsed = datetime.fromisoformat(value)\n    except ValueError:\n        errors.append(f"Métadonnée {field_name} hors format ISO 8601 : {rel} — {value}")\n        return\n    if parsed.tzinfo is None or parsed.utcoffset() is None:\n        errors.append(f"Métadonnée {field_name} sans décalage UTC : {rel} — {value}")\n    if 'T' not in value or parsed.second is None:\n        errors.append(f"Métadonnée {field_name} sans heure complète : {rel} — {value}")\n\n\n'''
if 'def validate_timestamp(' not in validator:
    validator = replace_once(validator, helper_anchor, helper + helper_anchor, 'validator helper')
validation_anchor = '''                if not metadata.get("audit-date"):\n                    errors.append(f"Métadonnée audit-date absente : {rel}")\n'''
validation_block = '''                if number >= 17:\n                    validate_timestamp(metadata.get("last-verified"), "last-verified", rel, errors)\n                    validate_timestamp(metadata.get("audit-date"), "audit-date", rel, errors)\n'''
if 'validate_timestamp(metadata.get("last-verified")' not in validator:
    validator = replace_once(validator, validation_anchor, validation_anchor + validation_block, 'validator chapter timestamp check')
audit_anchor = '''                elif not (root / str(audit_report)).is_file():\n                    errors.append(f"Rapport d’audit absent pour {rel} : {audit_report}")\n'''
audit_validation = '''                elif number >= 17:\n                    audit_path = root / str(audit_report)\n                    audit_text = audit_path.read_text(encoding="utf-8")\n                    audit_metadata = parse_front_matter(audit_text, str(audit_report), errors)\n                    validate_timestamp(audit_metadata.get("last-verified"), "last-verified", str(audit_report), errors)\n                    validate_timestamp(audit_metadata.get("audit-date"), "audit-date", str(audit_report), errors)\n'''
if 'audit_metadata = parse_front_matter' not in validator:
    validator = replace_once(validator, audit_anchor, audit_anchor + audit_validation, 'validator audit timestamp check')
write(validator_path, validator)

# Final assertions.
assert f'last-verified: "{STAMP}"' in chapter
assert f'audit-date: "{STAMP}"' in chapter
assert 'version: "3.17.9"' in continuity
assert 'Codes de retour' in continuity and 'Refus contrôlé' in continuity
assert 'def validate_timestamp' in validator
print(STAMP)
