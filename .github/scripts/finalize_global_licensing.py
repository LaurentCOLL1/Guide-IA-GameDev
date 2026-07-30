#!/usr/bin/env python3
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
STAMP = "2026-07-30T18:08:00+02:00"
PACKS = [
    "Starter-Kit", "Project-Templates", "AI-Library", "Code-Library",
    "Database-Library", "ComfyUI-Library", "Documentation-Library",
    "Test-Benchmark-Library", "Production-Toolkit", "Knowledge-Base",
]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    (ROOT / rel).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, name: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{name}: expected 1 occurrence, got {count}")
    return text.replace(old, new, 1)


def run(*args: str) -> None:
    subprocess.run(list(args), check=True)


# README
path = "README.md"
text = read(path)
old = """## Licence

La licence du texte, du code d’exemple et des ressources du Companion Pack sera précisée dans `LICENSE.md`. Les composants tiers conserveront leurs propres licences, qui devront être recensées et respectées individuellement.
"""
new = """## Licence

Le dépôt applique une politique de licences multiples définie dans [`LICENSE.md`](LICENSE.md) :

- documentation et contenus éditoriaux : `CC-BY-SA-4.0` ;
- code, scripts et ressources techniques réutilisables : `MIT` ;
- métadonnées factuelles explicitement classées : `CC0-1.0` ;
- composants tiers : licence d’origine, sans relicence automatique.

La matrice machine-readable se trouve dans [`docs/licensing/LICENSE-MATRIX.yaml`](docs/licensing/LICENSE-MATRIX.yaml). Les exports et archives doivent conserver les notices de copyright, d’attribution et de licence.
"""
write(path, replace_once(text, old, new, "README licence"))

# CONTRIBUTING
path = "CONTRIBUTING.md"
text = read(path)
anchor = "## Contenu sensible et adulte\n"
section = """## Licence des contributions

En proposant une contribution, son auteur confirme qu’il dispose des droits nécessaires et accepte que la contribution soit distribuée selon la licence applicable au fichier ou à sa catégorie dans `LICENSE.md` et `docs/licensing/LICENSE-MATRIX.yaml`.

- les contributions éditoriales sont reçues sous `CC-BY-SA-4.0` ;
- les contributions logicielles et techniques sont reçues sous `MIT` ;
- `CC0-1.0` ne s’applique qu’aux métadonnées explicitement classées ;
- tout composant tiers doit rester sous sa licence d’origine et être accompagné de sa provenance.

Une contribution ne doit pas incorporer un contenu incompatible avec la licence de destination.

"""
if "## Licence des contributions" not in text:
    text = replace_once(text, anchor, section + anchor, "CONTRIBUTING section")
write(path, text)

# metadata
path = "metadata.yaml"
text = read(path)
text = replace_once(
    text,
    'license: "À définir avant publication"',
    'license: "CC-BY-SA-4.0 (documentation); MIT (software); CC0-1.0 (explicit factual metadata)"',
    "metadata license",
)
write(path, text)

# ROADMAP
path = "ROADMAP.md"
text = read(path)
text = replace_once(
    text,
    "- [ ] Définir la licence globale du projet.",
    "- [x] Définir la licence globale du projet — politique multiple `CC-BY-SA-4.0` / `MIT` / `CC0-1.0`, matrice et validation CI.",
    "roadmap license",
)
write(path, text)

# Companion Pack index
path = "Companion-Pack/index.md"
text = read(path)
text = text.replace(
    "publication et licence globale restent ouvertes. La prochaine action relève de M8 — Publications : définir la licence globale du projet.",
    "publication et préparation des exports restent ouvertes. La licence globale multiple est définie ; la prochaine action de M8 est de produire les versions PDF, HTML et EPUB.",
)
write(path, text)

# Pack statuses and front matter token
status = """# Statut de licence

Ce Pack suit la politique globale décrite dans [`../../LICENSE.md`](../../LICENSE.md) et la matrice [`../../docs/licensing/LICENSE-MATRIX.yaml`](../../docs/licensing/LICENSE-MATRIX.yaml).

- documentation et contenus éditoriaux : `CC-BY-SA-4.0` ;
- code, scripts, schémas techniques, configurations et fixtures de test : `MIT` ;
- métadonnées factuelles explicitement classées : `CC0-1.0` ;
- composants tiers : licence d’origine, provenance obligatoire et aucune relicence automatique.

Le Pack peut être inclus dans une archive redistribuable si l’archive conserve `LICENSE.md`, `NOTICE.md`, le dossier `LICENSES/` et la matrice de licence.
"""
for pack in PACKS:
    write(f"Companion-Pack/{pack}/LICENSE-STATUS.md", status)
for file_path in (ROOT / "Companion-Pack").rglob("*"):
    if file_path.is_file() and file_path.suffix.lower() in {".md", ".yaml", ".yml", ".json", ".txt"}:
        value = file_path.read_text(encoding="utf-8")
        if "pending-global-license" in value:
            file_path.write_text(value.replace("pending-global-license", "global-policy-defined"), encoding="utf-8")

# contents
path = "contents.txt"
text = read(path)
entries = [
    "LICENSE.md", "NOTICE.md", "LICENSES/README.md",
    "docs/licensing/README.md", "docs/licensing/LICENSE-MATRIX.yaml",
    "QA/AUDIT-LICENSING.md", "QA/VALIDATION-LICENSING.yaml",
]
for entry in entries:
    if entry not in text.splitlines():
        text += ("\n" if not text.endswith("\n") else "") + entry + "\n"
write(path, text)

# CHANGELOG
path = "CHANGELOG.md"
text = read(path)
entry = """
## 2026-07-30 — Politique de licence globale

- documentation sous `CC-BY-SA-4.0` ;
- logiciel et ressources techniques sous `MIT` ;
- métadonnées factuelles explicitement classées sous `CC0-1.0` ;
- matrice de chemins, notices, règles de contribution et validation CI ajoutées.
"""
if "## 2026-07-30 — Politique de licence globale" not in text:
    lines = text.splitlines()
    if lines and lines[0].startswith("#"):
        text = lines[0] + "\n" + entry + "\n" + "\n".join(lines[1:]).lstrip("\n")
    else:
        text = entry.lstrip() + text
write(path, text)

# Continuity
path = "CONTINUITE-PROJET.md"
text = read(path)
text = replace_once(text, 'version: "4.24.0"', 'version: "4.25.0"', "continuity version")
text = replace_once(
    text,
    'last-updated: "2026-07-30T16:44:55+02:00"',
    f'last-updated: "{STAMP}"',
    "continuity time",
)
marker = "- progression du Companion Pack : 10 packs validés sur 10, M7 terminé ;\n"
if "- politique de licence globale :" not in text:
    text = replace_once(
        text,
        marker,
        marker + "- politique de licence globale : `CC-BY-SA-4.0` pour l’éditorial, `MIT` pour le logiciel et `CC0-1.0` pour les métadonnées explicitement classées ;\n",
        "continuity state",
    )
start = text.index("## 26. Prochaine action")
end = text.index("## 27. Journal", start)
next_block = """## 26. Prochaine action

M8 — Publications est actif. La licence globale est définie par catégories de droits et de fichiers : documentation sous `CC-BY-SA-4.0`, logiciel et ressources techniques sous `MIT`, métadonnées factuelles explicitement classées sous `CC0-1.0`. Les composants tiers conservent leur licence d’origine et sont exclus de toute relicence automatique.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
M8 — Publications
Produire les versions PDF, HTML et EPUB.
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le prochain lot doit générer les formats de collection à partir des sources maîtrisées, embarquer les attributions et notices de licence, vérifier les liens et métadonnées, et ne pas confondre génération technique avec publication officielle.

"""
text = text[:start] + next_block + text[end:]
journal = """### 2026-07-30T18:08:00+02:00 — version 4.25.0

- définition de la politique de licence globale multiple du projet ;
- documentation, chapitres, contenus narratifs et exports éditoriaux placés sous `CC-BY-SA-4.0` ;
- code, scripts, workflows, schémas techniques, configurations et fixtures de test placés sous `MIT` ;
- métadonnées factuelles explicitement classées placées sous `CC0-1.0` ;
- composants tiers, marques, modèles et assets externes exclus de toute relicence automatique ;
- `LICENSE.md`, `NOTICE.md`, trois notices de licence et une matrice machine-readable ajoutés ;
- règles de contribution et métadonnées Pandoc alignées ;
- dix fichiers `LICENSE-STATUS.md` du Companion Pack rendus redistribuables sous la politique globale ;
- validation CI dédiée ajoutée ;
- tâche M8 « définir la licence globale » clôturée ;
- prochaine action : produire les versions PDF, HTML et EPUB, niveau Élevée ;
- aucune publication, release, archive publique ou validation juridique individualisée réalisée.

"""
text = text.replace("## 27. Journal\n\n", "## 27. Journal\n\n" + journal, 1)
write(path, text)

# Candidate QA state
path = "QA/AUDIT-LICENSING.md"
text = read(path).replace("**Statut :** candidate", "**Statut :** reviewed")
text += "\n## Résultat\n\nLa politique est structurée, les dix Packs sont reliés à la matrice et les anciens marqueurs de licence globale en attente sont retirés. La qualification runtime Linux reste à inscrire dans la preuve YAML après le workflow permanent.\n"
write(path, text)
path = "QA/VALIDATION-LICENSING.yaml"
text = read(path)
text = text.replace("status: pending", "status: qualified-candidate", 1)
text = text.replace("validation-status: candidate", "validation-status: awaiting-permanent-workflow", 1)
write(path, text)

run(sys.executable, "tools/validate_licenses.py", "--report", "dist/licensing/finalizer-validation.json")
run(sys.executable, "tools/validate_chapters.py")
run("git", "diff", "--check")
run("git", "config", "user.name", "github-actions[bot]")
run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
run(
    "git", "add", "README.md", "CONTRIBUTING.md", "metadata.yaml", "ROADMAP.md",
    "Companion-Pack/index.md", "Companion-Pack", "contents.txt", "CHANGELOG.md",
    "CONTINUITE-PROJET.md", "QA/AUDIT-LICENSING.md", "QA/VALIDATION-LICENSING.yaml",
)
run("git", "commit", "-m", "docs(license): aligner la gouvernance et les dix Packs")
run("git", "push", "origin", "HEAD:feat/global-licensing-policy")
