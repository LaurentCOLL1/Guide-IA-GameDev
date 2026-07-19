#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]

audit = root / "Livre-II/QA/AUDIT-CHAPITRE-08.md"
text = audit.read_text(encoding="utf-8")
text = text.replace('version: "1.0.0"', 'version: "1.1.0"', 1)
old = "Aucun PDF intermédiaire n’a été construit, conformément à la politique du Livre II.\n"
new = '''Aucun PDF intermédiaire n’a été construit, conformément à la politique du Livre II.

La validation finale légère a réussi :

- `Validate Chapters Without PDF`, run `29684886165` ;
- `Validate Usage Contexts`, run `29684886159` ;
- 56 sources déclarées ;
- 55 identifiants uniques ;
- 8 chapitres du Livre II continus ;
- 0 erreur bloquante ;
- 0 incohérence sémantique ;
- 1 143 blocs sur 1 143 précédés d’un repère ;
- aucun titre, bloc significatif ou paragraphe long dupliqué dans le Livre II.
'''
if text.count(old) != 1:
    raise SystemExit("Audit validation insertion point missing")
text = text.replace(old, new, 1)
old = "Il peut être déclaré **rédigé, repéré et audité au niveau `static-review`**, sous réserve de la réussite du workflow léger et des tests runtime différés.\n"
new = "Les portes documentaires et statiques ont réussi. Il est déclaré **rédigé, repéré et audité au niveau `static-review`**, sous réserve des seuls tests runtime différés et du PDF de fin de Livre.\n"
if text.count(old) != 1:
    raise SystemExit("Audit conclusion point missing")
audit.write_text(text.replace(old, new, 1), encoding="utf-8")

evidence = root / "Livre-II/QA/VALIDATION-FINALE-CHAPITRE-08.yaml"
text = evidence.read_text(encoding="utf-8")
text = text.replace("status: awaiting-ci", "status: complete", 1)
old = '''ci:
  validate-chapters-without-pdf: pending
  validate-usage-contexts: pending
'''
new = '''ci:
  validate-chapters-without-pdf:
    run-id: 29684886165
    conclusion: success
  validate-usage-contexts:
    run-id: 29684886159
    conclusion: success
  artifact:
    id: 8441749891
    name: chapter-validation-without-pdf
    digest: sha256:f3a6caa0688c6171906f35f181abceace5b3b1115d29b1ffe0945280d0851d0c
  metrics:
    sources: 56
    unique-identifiers: 55
    livre-i-chapters: 10
    livre-ii-chapters: 8
    chapter-08-lines: 2334
    chapter-08-headings: 102
    chapter-08-significant-code-blocks: 28
    total-context-blocks: 1143
    marked-context-blocks: 1143
    semantic-inconsistencies: 0
    blocking-errors: 0
    warnings: 1
    duplicate-headings: 0
    duplicate-significant-blocks: 0
    duplicate-long-paragraphs: 0
'''
if text.count(old) != 1:
    raise SystemExit("Evidence CI block missing")
evidence.write_text(text.replace(old, new, 1), encoding="utf-8")

continuity = root / "CONTINUITE-PROJET.md"
text = continuity.read_text(encoding="utf-8")
old = "- validateur sémantique étendu aux libellés « Architecture corrigée » et « Flux corrigé » ;\n"
new = '''- validateur sémantique étendu aux libellés « Architecture corrigée » et « Flux corrigé » ;
- validations finales `29684886165` et `29684886159` réussies ;
- 56 sources, 55 identifiants uniques et 1 143 blocs sur 1 143 repérés ;
'''
if text.count(old) != 1:
    raise SystemExit("Continuity final validation insertion missing")
continuity.write_text(text.replace(old, new, 1), encoding="utf-8")

for rel in (
    "tools/finalize_chapter08_evidence.py",
    ".github/workflows/finalize-chapter08-evidence.yml",
):
    file_path = root / rel
    if file_path.exists():
        file_path.unlink()

print("Chapter 8 evidence finalized.")
