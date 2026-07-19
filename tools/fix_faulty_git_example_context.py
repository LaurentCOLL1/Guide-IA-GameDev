#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
chapter = root / "Livre-II/CHAPITRE-01-Decouvrir-Godot-et-creer-le-projet-fil-rouge.md"
text = chapter.read_text(encoding="utf-8")
old = '''> **[LECTURE] Exemple fautif — Ne pas recopier.**

```powershell
git add .
git commit -m 'chore: add every generated file'
```'''
new = '''> **[LECTURE] Exemple fautif — Ne pas recopier ni exécuter.**

```text
git add .
git commit -m 'chore: add every generated file'
```'''
if old not in text:
    raise SystemExit("Faulty Git example not found")
chapter.write_text(text.replace(old, new, 1), encoding="utf-8")

for rel in ("tools/fix_faulty_git_example_context.py", ".github/workflows/fix-faulty-git-example-context.yml"):
    path = root / rel
    if path.exists():
        path.unlink()
print("Faulty Git example converted to literal text.")
