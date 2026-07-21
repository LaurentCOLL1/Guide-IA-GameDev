#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import re

ROOT = Path('.')
NOW = datetime.now(ZoneInfo('Europe/Paris')).replace(microsecond=0).isoformat()

chapter_paths = sorted((ROOT / 'Livre-II').glob('CHAPITRE-*.md'))
removed = 0
for path in chapter_paths:
    text = path.read_text(encoding='utf-8')
    updated, count = re.subn(
        r'^> \*\*Niveau de raisonnement conseillé :\*\* GPT-5\.6 Sol — (?:Moyenne|Élevée)\s*\n',
        '',
        text,
        flags=re.MULTILINE,
    )
    if count:
        path.write_text(updated, encoding='utf-8')
        removed += count

if removed < 10:
    raise SystemExit(f'Nombre inattendu de lignes lecteur retirées : {removed}')

validator_path = ROOT / 'tools/validate_chapters.py'
validator = validator_path.read_text(encoding='utf-8')
needle = '''            if book_code == "II":
                if metadata.get("audit-status") != "complete":
'''
replacement = '''            if book_code == "II":
                if "recommended-reasoning:" in text or "Niveau de raisonnement conseillé" in text:
                    errors.append(
                        f"Le niveau GPT-5.6 Sol appartient au processus de production, pas au chapitre publié : {rel}"
                    )
                if metadata.get("audit-status") != "complete":
'''
if needle not in validator:
    raise SystemExit('Point d’insertion du validateur introuvable.')
validator = validator.replace(needle, replacement, 1)
validator_path.write_text(validator, encoding='utf-8')

protocol_path = ROOT / 'Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md'
protocol = protocol_path.read_text(encoding='utf-8')
protocol = protocol.replace('version: "1.7.5"', 'version: "1.7.6"', 1)
protocol = re.sub(r'last-verified: "[^"]+"', f'last-verified: "{NOW}"', protocol, count=1)
protocol = protocol.replace(
    'Elle ne doit pas être inscrite dans le front matter du chapitre, dans son audit ou dans sa preuve QA comme si elle décrivait le contenu publié.',
    'Elle ne doit être inscrite ni dans le front matter ni dans l’en-tête ou le corps du chapitre, ni dans son audit ou sa preuve QA comme si elle décrivait le contenu publié.',
)
protocol = protocol.replace(
    '- [ ] Le niveau de raisonnement conseillé est annoncé avant la rédaction et reste hors des métadonnées du chapitre.',
    '- [ ] Le niveau de raisonnement conseillé est annoncé avant la rédaction et reste absent des métadonnées comme du texte destiné au lecteur.',
)
protocol_path.write_text(protocol, encoding='utf-8')

continuity_path = ROOT / 'CONTINUITE-PROJET.md'
continuity = continuity_path.read_text(encoding='utf-8')
continuity = continuity.replace('version: "3.25.1"', 'version: "3.25.2"', 1)
continuity = re.sub(r'last-updated: "[^"]+"', f'last-updated: "{NOW}"', continuity, count=1)
continuity = continuity.replace(
    'Elle ne décrit pas le chapitre lui-même et ne doit donc jamais apparaître sous la clé '
    '`recommended-reasoning` dans le front matter, l’audit ou la preuve QA du document publié.',
    'Elle ne décrit pas le chapitre lui-même et ne doit donc apparaître ni sous la clé '
    '`recommended-reasoning`, ni dans l’en-tête ou le corps destiné au lecteur, ni dans l’audit ou la preuve QA du document publié.',
)
journal_anchor = '## 27. Journal\n'
journal_entry = f'''## 27. Journal

### {NOW} — version 3.25.2

- lignes « Niveau de raisonnement conseillé » retirées des en-têtes lecteurs des chapitres du Livre II ;
- validateur renforcé pour refuser la clé YAML comme la mention visible dans un chapitre publié ;
- protocole QA clarifié : la recommandation reste exclusivement dans le processus de production ;
- prochaine action maintenue sur le chapitre 26 ;
- aucun test runtime revendiqué et aucun PDF construit.
'''
if journal_anchor not in continuity:
    raise SystemExit('Journal de continuité introuvable.')
continuity = continuity.replace(journal_anchor, journal_entry, 1)
continuity_path.write_text(continuity, encoding='utf-8')

roadmap_path = ROOT / 'ROADMAP.md'
roadmap = roadmap_path.read_text(encoding='utf-8')
roadmap = roadmap.replace(
    '- [x] Gouvernance GPT-5.6 Sol corrigée : recommandation conservée dans le processus, retirée des métadonnées des chapitres.',
    '- [x] Gouvernance GPT-5.6 Sol corrigée : recommandation conservée dans le processus, retirée des métadonnées et des en-têtes lecteurs des chapitres.',
)
roadmap_path.write_text(roadmap, encoding='utf-8')

for path in chapter_paths:
    text = path.read_text(encoding='utf-8')
    if 'recommended-reasoning:' in text or 'Niveau de raisonnement conseillé' in text:
        raise SystemExit(f'Reliquat de niveau GPT dans {path}')

Path('.qa/fix_reasoning_reader_header.py').unlink()
print(f'Lignes lecteur retirées : {removed}')
