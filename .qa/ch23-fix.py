from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import re

ROOT = Path('.')
CHAPTER = ROOT / 'Livre-II/CHAPITRE-23-Politique-factions-et-justice.md'

now = datetime.now(ZoneInfo('Europe/Paris')).replace(microsecond=0)
stamp = now.isoformat()
date = now.date().isoformat()


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8', newline='\n')


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected one occurrence, got {count}')
    return text.replace(old, new, 1)


chapter = read(CHAPTER)
if 'id: "DOC-L2-CH23"' not in chapter or 'version: "0.9.0"' not in chapter:
    raise RuntimeError('Unexpected chapter 23 source')
if chapter.count('<!-- qa:code-explanation -->') != 71:
    raise RuntimeError('Unexpected explanation marker count')
if len(re.findall(r'^### 48\.\d+ ', chapter, re.M)) != 10:
    raise RuntimeError('Unexpected detailed error case count')

chapter = replace_once(chapter, 'status: "draft"', 'status: "reviewed"', 'chapter status')
chapter = replace_once(chapter, 'version: "0.9.0"', 'version: "1.0.0"', 'chapter version')
chapter = re.sub(r'last-verified: "[^"]+"', f'last-verified: "{stamp}"', chapter, count=1)
chapter = replace_once(chapter, 'audit-status: "pending"', 'audit-status: "complete"', 'audit status')
chapter = re.sub(r'audit-date: "[^"]+"', f'audit-date: "{stamp}"', chapter, count=1)
chapter = replace_once(chapter, 'audit-level: "not-audited"', 'audit-level: "static-review"', 'audit level')
chapter = replace_once(
    chapter,
    '> **Audit post-création :** en attente — voir `Livre-II/QA/AUDIT-CHAPITRE-23.md`.',
    '> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-23.md`.',
    'visible audit status',
)

old_mandate = """\tif not holder_character_id.is_empty() and not CharacterId.is_valid(holder_character_id):
\t\treturn ERR_INVALID_DATA
\tif not jurisdiction_id.is_empty() and not StableId.is_valid(jurisdiction_id):
"""
new_mandate = """\tif status == Status.ACTIVE and not CharacterId.is_valid(holder_character_id):
\t\treturn ERR_INVALID_DATA
\tif status == Status.VACANT and not holder_character_id.is_empty():
\t\treturn ERR_INVALID_DATA
\tif status not in [Status.ACTIVE, Status.VACANT]:
\t\tif not holder_character_id.is_empty() and not CharacterId.is_valid(holder_character_id):
\t\t\treturn ERR_INVALID_DATA
\tif not jurisdiction_id.is_empty() and not StableId.is_valid(jurisdiction_id):
"""
chapter = replace_once(chapter, old_mandate, new_mandate, 'mandate holder invariants')
chapter = replace_once(
    chapter,
    '- Un siège vacant peut conserver la fonction et la juridiction sans titulaire.\n',
    '- Un mandat actif exige un titulaire valide ; un siège vacant conserve la fonction et la juridiction mais exige un titulaire vide.\n',
    'mandate explanation',
)

old_faction_start = """func validate(catalog: PoliticalCatalog) -> Error:
\tif catalog == null or catalog.get_faction(faction_id) == null:
\t\treturn ERR_DOES_NOT_EXIST
\tif revision < 0 or event_sequence < 0:
"""
new_faction_start = """func validate(catalog: PoliticalCatalog) -> Error:
\tif catalog == null:
\t\treturn ERR_UNCONFIGURED
\tvar definition := catalog.get_faction(faction_id)
\tif definition == null:
\t\treturn ERR_DOES_NOT_EXIST
\tif revision < 0 or event_sequence < 0:
"""
chapter = replace_once(chapter, old_faction_start, new_faction_start, 'faction definition lookup')
old_membership_check = """\t\tif membership.faction_id != faction_id or membership.validate() != OK:
\t\t\treturn ERR_INVALID_DATA
\t\tif membership.status in [MembershipState.Status.ACTIVE, MembershipState.Status.SUSPENDED]:
"""
new_membership_check = """\t\tif membership.faction_id != faction_id or membership.validate() != OK:
\t\t\treturn ERR_INVALID_DATA
\t\tif membership.rank_id not in definition.rank_ids:
\t\t\treturn ERR_INVALID_DATA
\t\tif membership.status in [MembershipState.Status.ACTIVE, MembershipState.Status.SUSPENDED]:
"""
chapter = replace_once(chapter, old_membership_check, new_membership_check, 'membership rank cross-reference')
old_mandate_check = """\t\tif mandate.faction_id != faction_id or mandate.validate() != OK:
\t\t\treturn ERR_INVALID_DATA
\treturn OK
"""
new_mandate_check = """\t\tif mandate.faction_id != faction_id or mandate.validate() != OK:
\t\t\treturn ERR_INVALID_DATA
\t\tif mandate.institution_id != definition.institution_id:
\t\t\treturn ERR_INVALID_DATA
\t\tif mandate.office_id not in definition.office_ids:
\t\t\treturn ERR_INVALID_DATA
\treturn OK
"""
chapter = replace_once(chapter, old_mandate_check, new_mandate_check, 'mandate cross-references')
chapter = replace_once(
    chapter,
    '- Les clés de mandats et d’adhésions sont recoupées avec les identifiants contenus dans les valeurs.\n',
    '- Les clés sont recoupées avec les identifiants des valeurs ; chaque adhésion utilise un rang autorisé et chaque mandat l’institution et une fonction déclarées par la faction.\n',
    'faction explanation',
)

chapter = replace_once(
    chapter,
    """func decode_sections(
\t_document: Dictionary,
\t_catalog: PoliticalCatalog,
) -> Dictionary:
\treturn {}
""",
    """func decode_sections(
\t_document: Dictionary,
\t_catalog: PoliticalCatalog,
) -> Variant:
\treturn null
""",
    'decoder failure sentinel',
)
chapter = replace_once(
    chapter,
    '- Un dictionnaire vide peut être un état préparé valide ; un échec de décodage est représenté par `null`, jamais par `{}`.\n',
    '- Le retour `Variant` permet de réserver `{}` à un état préparé vide mais valide et `null` à un échec de décodage.\n',
    'decoder explanation',
)

error_start = chapter.index('## 48. Erreurs fréquentes et corrections')
before = chapter[:error_start]
errors = chapter[error_start:]
pattern = '<!-- qa:code-explanation -->\n\n**Explication détaillée du bloc :**\n\n**Pourquoi'
removed = errors.count(pattern)
if removed != 20:
    raise RuntimeError(f'Expected 20 redundant error headings, got {removed}')
errors = errors.replace(pattern, '<!-- qa:code-explanation -->\n\n**Pourquoi')
chapter = before + errors

if 'Validate Chapters Without PDF' in chapter:
    raise RuntimeError('Reader chapter contains documentary validation commands')
if re.search(r'^## .*Prochaine étape', chapter, re.M):
    raise RuntimeError('Reader chapter contains a next-step section')
if not chapter.rstrip().endswith('21. définitions, droits dérivés, contextes, candidats, observations et présentation restent hors du snapshot.'):
    raise RuntimeError('Project Asteria synthesis is not the final content')

lines = len(chapter.splitlines())
headings = re.findall(r'^(#{1,6})\s+(.+?)\s*$', chapter, re.M)
heading_texts = [text for _, text in headings]
duplicates = sorted([text for text, count in Counter(heading_texts).items() if count > 1])
fences = len(re.findall(r'^```', chapter, re.M))
if fences % 2:
    raise RuntimeError('Unbalanced fenced blocks')
blocks = fences // 2
markers = chapter.count('<!-- qa:code-explanation -->')
error_cases = len(re.findall(r'^### 48\.\d+ ', chapter, re.M))
faulty = chapter.count('**Pourquoi cet exemple est fautif :**')
corrected = chapter.count('**Pourquoi la correction fonctionne :**')
if blocks != markers:
    raise RuntimeError(f'Block/marker mismatch: {blocks}/{markers}')
if error_cases != 10 or faulty != 10 or corrected != 10:
    raise RuntimeError('Error/correction gate failed')
if duplicates:
    raise RuntimeError(f'Duplicate headings: {duplicates}')

write(CHAPTER, chapter)

import json
Path('.qa/ch23-metrics.json').write_text(json.dumps({'stamp': stamp, 'date': date, 'lines': lines, 'headings': len(headings), 'blocks': blocks, 'markers': markers, 'error_cases': error_cases, 'faulty': faulty, 'corrected': corrected}, ensure_ascii=False), encoding='utf-8')
