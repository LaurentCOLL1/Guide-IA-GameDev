from pathlib import Path
import re

ROOT = Path('.')
chapter_path = ROOT / 'Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md'
parts = [ROOT / f'tmp/ch17-part-{index}.md' for index in (1, 2, 3)]
chapter = ''.join(path.read_text(encoding='utf-8') for path in parts)
if chapter.count('```') % 2 != 0:
    raise RuntimeError('unbalanced code fences')
if 'status: "draft"' not in chapter or 'version: "0.9.0"' not in chapter:
    raise RuntimeError('draft metadata missing')
if 'audit-status: "pending"' not in chapter or 'audit-level: "not-audited"' not in chapter:
    raise RuntimeError('draft audit gate missing')
chapter_path.write_text(chapter, encoding='utf-8')

index_path = ROOT / 'Livre-II/index.md'
index = index_path.read_text(encoding='utf-8')
index = index.replace('version: "1.11.1"', 'version: "1.12.0"', 1)
old = '17. Agents IA et comportements autonomes — à rédiger'
new = '17. [Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md) — **brouillon 0.9.0, audit en attente**'
if index.count(old) != 1:
    raise RuntimeError('index chapter 17 anchor missing')
index = index.replace(old, new, 1)
anchor = '- [audit du chapitre 16](QA/AUDIT-CHAPITRE-16.md) ;'
addition = anchor + '\n- [audit du chapitre 17 — en attente](QA/AUDIT-CHAPITRE-17.md) ;'
if index.count(anchor) != 1:
    raise RuntimeError('index audit anchor missing')
index = index.replace(anchor, addition, 1)
index_path.write_text(index, encoding='utf-8')

roadmap_path = ROOT / 'ROADMAP.md'
roadmap = roadmap_path.read_text(encoding='utf-8')
anchor = '- [x] Chapitre 16 — filiation dirigée, adoption, tutelle, unions canoniques, cycles, générations dérivées et sauvegarde familiale — rédigé et audité au niveau `static-review`.'
line = '- [ ] Chapitre 17 — agents IA et comportements autonomes — brouillon `0.9.0` créé, audit post-création en attente.'
if line not in roadmap:
    if roadmap.count(anchor) != 1:
        raise RuntimeError('roadmap anchor missing')
    roadmap = roadmap.replace(anchor, anchor + '\n' + line, 1)
roadmap_path.write_text(roadmap, encoding='utf-8')

contents_path = ROOT / 'contents.txt'
contents = contents_path.read_text(encoding='utf-8')
chapter_line = 'Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md'
if chapter_line not in contents:
    anchor = 'Livre-II/CHAPITRE-16-Famille-et-generations.md'
    if contents.count(anchor) != 1:
        raise RuntimeError('contents chapter anchor missing')
    contents = contents.replace(anchor, anchor + '\n' + chapter_line, 1)
audit_line = 'Livre-II/QA/AUDIT-CHAPITRE-17.md'
if audit_line not in contents:
    anchor = 'Livre-II/QA/AUDIT-CHAPITRE-16.md'
    contents = contents.replace(anchor, anchor + '\n' + audit_line, 1)
evidence_line = 'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-17.yaml'
if evidence_line not in contents:
    anchor = 'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-16.yaml'
    contents = contents.replace(anchor, anchor + '\n' + evidence_line, 1)
contents_path.write_text(contents, encoding='utf-8')

audit_path = ROOT / 'Livre-II/QA/AUDIT-CHAPITRE-17.md'
audit_path.write_text('''---
title: "Audit du Livre II — Chapitre 17"
id: "DOC-L2-QA-AUDIT-CH17"
status: "pending"
version: "0.9.0"
chapter-id: "DOC-L2-CH17"
chapter-version: "0.9.0"
audit-level: "not-audited"
audit-date: null
---

# Audit du chapitre 17 — en attente

Le chapitre existe au jalon de brouillon `0.9.0`. Cet audit doit être réalisé dans une passe distincte après la création initiale.

## Porte de brouillon

- chemin canonique créé ;
- métadonnées `draft`, `pending` et `not-audited` présentes ;
- périmètre comparé aux chapitres 14 à 18 ;
- index, roadmap, `contents.txt` et continuité mis à jour ;
- aucune revendication de test runtime ;
- aucun PDF produit.

## Points à contrôler

- complétude des ports et contrats annoncés ;
- validité statique des extraits GDScript ;
- déterminisme du planificateur et de l’ordonnanceur ;
- autorité strictement consultative de l’IA générative ;
- persistance minimale et restauration atomique ;
- explication spécifique de chaque bloc ;
- conformité des 16 cas d’erreurs ;
- sources officielles Godot 4.7.1 ;
- absence de doublons avec les chapitres voisins.
''', encoding='utf-8')

evidence_path = ROOT / 'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-17.yaml'
evidence_path.write_text('''schema-version: 1
evidence-id: DOC-L2-QA-EVIDENCE-CH17
status: draft-gate
validation-date: 2026-07-20
validated-base-commit: a61ea9e5378e270e1db98d9f83e6fe6cef847318
validated-head-commit: pending-audit
chapter:
  id: DOC-L2-CH17
  path: Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md
  version: 0.9.0
  audit-level: not-audited
process:
  draft-gate-recorded: true
  distinct-audit-required: true
  pdf-produced: false
  runtime-executed: false
ci:
  validate-chapters-without-pdf:
    run-id: pending
    conclusion: pending
  validate-usage-contexts:
    run-id: pending
    conclusion: pending
''', encoding='utf-8')

continuity_path = ROOT / 'CONTINUITE-PROJET.md'
continuity = continuity_path.read_text(encoding='utf-8')
if continuity.count('version: "3.17.5"') != 1:
    raise RuntimeError('continuity version anchor missing')
continuity = continuity.replace('version: "3.17.5"', 'version: "3.17.6"', 1)
state_anchor = '- chapitre 16 : version `1.2.1` ;'
state_line = '- chapitre 17 : brouillon version `0.9.0`, audit en attente ;'
if state_line not in continuity:
    continuity = continuity.replace(state_anchor, state_anchor + '\n' + state_line, 1)
start = continuity.index('## 26. Prochaine action')
end = continuity.index('## 27. Journal')
next_action = '''## 26. Prochaine action

Le brouillon du chapitre 17 est créé au jalon `0.9.0`. La prochaine opération obligatoire est une passe d’audit distincte, sans modifier silencieusement le périmètre.

Points prioritaires :

- vérifier chaque bloc GDScript contre Godot `4.7.1-stable` ;
- remplacer les contrats incomplets du codec et de la section de sauvegarde ;
- vérifier les conversions de collections typées ;
- contrôler les ports annoncés par le service de décision ;
- auditer le déterminisme, les budgets et les invalidations ;
- vérifier les 16 cas d’erreurs et leurs renvois ;
- fermer les preuves QA et lancer les workflows légers ;
- ne produire aucun PDF.

Chapitre en cours :

> **[LECTURE] Chemin et niveau — Ne pas saisir.**

```text
Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

'''
continuity = continuity[:start] + next_action + continuity[end:]
journal_anchor = '## 27. Journal\n'
entry = '''## 27. Journal

### 2026-07-20 — version 3.17.6

- création du brouillon `0.9.0` du chapitre 17 ;
- état `draft`, audit `pending`, niveau `not-audited` ;
- périmètre agents autonomes séparé des personnages, relations, famille et combat ;
- porte de brouillon et preuve initiale enregistrées ;
- index, roadmap et `contents.txt` mis à jour ;
- aucun PDF construit et aucun test runtime revendiqué.
'''
if '### 2026-07-20 — version 3.17.6' not in continuity:
    continuity = continuity.replace(journal_anchor, entry, 1)
continuity_path.write_text(continuity, encoding='utf-8')

print(f'chapter_lines={len(chapter.splitlines())}')
print(f'code_fences={chapter.count("```") // 2}')
print('draft_gate=ok')
