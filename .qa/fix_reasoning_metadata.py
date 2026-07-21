#!/usr/bin/env python3
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import re

ROOT = Path('.')
NOW = datetime.now(ZoneInfo('Europe/Paris')).replace(microsecond=0).isoformat()

# 1. Retirer la métadonnée de tous les chapitres publiés du Livre II.
chapter_paths = sorted((ROOT / 'Livre-II').glob('CHAPITRE-*.md'))
removed = 0
for path in chapter_paths:
    text = path.read_text(encoding='utf-8')
    updated, count = re.subn(
        r'^recommended-reasoning:\s*"[^"]+"\s*\n',
        '',
        text,
        flags=re.MULTILINE,
    )
    if count:
        path.write_text(updated, encoding='utf-8')
        removed += count

if removed < 20:
    raise SystemExit(f'Nombre inattendu de métadonnées retirées : {removed}')

# 2. Corriger le validateur : le niveau de raisonnement n'est pas une propriété documentaire.
validator_path = ROOT / 'tools/validate_chapters.py'
validator = validator_path.read_text(encoding='utf-8')
validator = validator.replace(
    'VALID_REASONING = {"GPT-5.6 Sol — Moyenne", "GPT-5.6 Sol — Élevée"}\n',
    '',
)
validator = validator.replace(
    '                if number >= 3 and metadata.get("recommended-reasoning") not in VALID_REASONING:\n'
    '                    errors.append(f"Niveau GPT-5.6 Sol absent ou invalide : {rel}")\n',
    '',
)
if 'recommended-reasoning' in validator or 'VALID_REASONING' in validator:
    raise SystemExit('Le validateur contient encore une exigence de niveau de raisonnement.')
validator_path.write_text(validator, encoding='utf-8')

# 3. Corriger le protocole QA.
protocol_path = ROOT / 'Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md'
protocol = protocol_path.read_text(encoding='utf-8')
protocol = protocol.replace('version: "1.7.4"', 'version: "1.7.5"')
protocol = re.sub(
    r'last-verified: "[^"]+"',
    f'last-verified: "{NOW}"',
    protocol,
    count=1,
)
old_section = '''La recommandation est enregistrée dans le front matter :

> **[LECTURE] Exemple YAML — Ne pas créer de fichier sans chemin explicitement indiqué.**

```yaml
recommended-reasoning: "GPT-5.6 Sol — Élevée"
```
'''
new_section = '''La recommandation appartient au **processus de production**, pas au document produit. Elle est annoncée avant la rédaction et peut être consignée dans `CONTINUITE-PROJET.md`, la branche ou la pull request. Elle ne doit pas être inscrite dans le front matter du chapitre, dans son audit ou dans sa preuve QA comme si elle décrivait le contenu publié.
'''
if old_section not in protocol:
    raise SystemExit('Section historique du protocole introuvable.')
protocol = protocol.replace(old_section, new_section)
protocol = protocol.replace(
    'usage-context-standard: "DOC-V0-ANN-CONTEXTES"\nrecommended-reasoning: "GPT-5.6 Sol — Moyenne ou Élevée"\n',
    'usage-context-standard: "DOC-V0-ANN-CONTEXTES"\n',
)
protocol = protocol.replace(
    '- [ ] Le niveau de raisonnement conseillé est annoncé et enregistré.',
    '- [ ] Le niveau de raisonnement conseillé est annoncé avant la rédaction et reste hors des métadonnées du chapitre.',
)
if 'recommended-reasoning:' in protocol:
    raise SystemExit('Le protocole contient encore la clé interdite.')
protocol_path.write_text(protocol, encoding='utf-8')

# 4. Corriger la continuité du projet.
continuity_path = ROOT / 'CONTINUITE-PROJET.md'
continuity = continuity_path.read_text(encoding='utf-8')
continuity = continuity.replace('version: "3.25.0"', 'version: "3.25.1"', 1)
continuity = re.sub(
    r'last-updated: "[^"]+"',
    f'last-updated: "{NOW}"',
    continuity,
    count=1,
)
continuity = continuity.replace(
    'usage-context-standard: "DOC-V0-ANN-CONTEXTES"\nrecommended-reasoning: "GPT-5.6 Sol — Moyenne ou Élevée"\n',
    'usage-context-standard: "DOC-V0-ANN-CONTEXTES"\n',
)
anchor = ('À chaque clôture de chapitre, la section **Prochaine action** de `CONTINUITE-PROJET.md` doit contenir '
          'dans le même bloc de texte le chemin canonique et la ligne `Niveau GPT-5.6 Sol recommandé : Moyenne ou '
          'Élevée`. Le chapitre publié ne contient ni section `Prochaine étape`, ni chemin ou niveau du chapitre suivant '
          ': ces informations restent exclusivement dans la continuité du projet.')
addition = (anchor + '\n\nLa recommandation GPT-5.6 Sol décrit l’effort de raisonnement conseillé pour **produire** un chapitre. '
            'Elle ne décrit pas le chapitre lui-même et ne doit donc jamais apparaître sous la clé '
            '`recommended-reasoning` dans le front matter, l’audit ou la preuve QA du document publié.')
if anchor not in continuity:
    raise SystemExit('Ancre de gouvernance GPT introuvable dans la continuité.')
continuity = continuity.replace(anchor, addition, 1)
journal_anchor = '## 27. Journal\n'
journal_entry = f'''## 27. Journal

### {NOW} — version 3.25.1

- correction de gouvernance : le niveau GPT-5.6 Sol est une donnée du processus de production, pas une métadonnée du chapitre ;
- clé `recommended-reasoning` retirée des chapitres publiés du Livre II ;
- protocole QA et validateur léger corrigés pour ne plus exiger cette clé ;
- doublon de l’audit du chapitre 24 retiré de l’index ;
- prochaine action maintenue sur le chapitre 26 ;
- aucun test runtime revendiqué et aucun PDF construit.
'''
if journal_anchor not in continuity:
    raise SystemExit('Journal de continuité introuvable.')
continuity = continuity.replace(journal_anchor, journal_entry, 1)
if 'recommended-reasoning:' in continuity:
    raise SystemExit('La continuité contient encore la clé YAML interdite.')
continuity_path.write_text(continuity, encoding='utf-8')

# 5. Corriger l'index du Livre II.
index_path = ROOT / 'Livre-II/index.md'
index = index_path.read_text(encoding='utf-8')
index = index.replace('version: "1.17.0"', 'version: "1.17.1"', 1)
index = index.replace(
    'Les chapitres 3 à 24 utilisent **Élevée**. La recommandation doit être justifiée avant le début du travail et enregistrée dans les métadonnées du chapitre.',
    'Les chapitres 3 à 25 ont utilisé **Élevée**. La recommandation doit être justifiée avant le début du travail et reste une donnée de gouvernance du processus, jamais une métadonnée du chapitre publié.',
)
audit24 = '- [audit du chapitre 24](QA/AUDIT-CHAPITRE-24.md) ;\n'
if index.count(audit24) != 2:
    raise SystemExit(f'Nombre inattendu de lignes audit 24 : {index.count(audit24)}')
first = index.find(audit24)
second = index.find(audit24, first + len(audit24))
index = index[:second] + index[second + len(audit24):]
index_path.write_text(index, encoding='utf-8')

# 6. Tracer la correction dans la roadmap.
roadmap_path = ROOT / 'ROADMAP.md'
roadmap = roadmap_path.read_text(encoding='utf-8')
roadmap_anchor = '- [x] Protocole QA adapté à la construction PDF différée.\n'
roadmap_line = '- [x] Gouvernance GPT-5.6 Sol corrigée : recommandation conservée dans le processus, retirée des métadonnées des chapitres.\n'
if roadmap_line not in roadmap:
    if roadmap_anchor not in roadmap:
        raise SystemExit('Ancre roadmap introuvable.')
    roadmap = roadmap.replace(roadmap_anchor, roadmap_anchor + roadmap_line, 1)
roadmap_path.write_text(roadmap, encoding='utf-8')

# Contrôles finaux ciblés.
for path in chapter_paths:
    if 'recommended-reasoning:' in path.read_text(encoding='utf-8'):
        raise SystemExit(f'Clé interdite encore présente : {path}')

Path('.qa/fix_reasoning_metadata.py').unlink()
print(f'Métadonnées retirées : {removed}')
