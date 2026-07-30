#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path.cwd()
STAMP = "2026-07-30T23:04:00+02:00"
RUN_ID = "30582855712"
ARTIFACT_ID = "8775425907"
DIGEST = "sha256:d5d3d548b133e1e6cc12e7d2809e27c3e7166f5dfb131e0e817c4de39426e9e6"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, name: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{name}: expected 1 occurrence, got {count}")
    return text.replace(old, new, 1)


proof = f"""schema-version: 1
evidence-id: QA-PUBLICATION-FORMATS-M8
status: complete
validation-status: runtime-tested-linux
formats:
  pdf:
    bytes: 10571878
    pages: 4108
    sha256: ca360a66a820a4dbd9951acd4c45e16c5bb8560fd5a0323620455307b1e9dcd4
  html:
    bytes: 18721066
    standalone: true
    sha256: 411671facba03ac6b194e42b664a67d55eb459a34cdd37fb73ea363a99a274ee
  epub3:
    bytes: 3864620
    entries: 173
    sha256: a6db51c39e37b848cefb63d2a80926c1f35ed89169f6f32bd67859fdf6c31b96
source-count: 162
source-order: contents.txt
license: CC-BY-SA-4.0
publication-status: technical-build-not-official-release
environment:
  os: ubuntu-24.04
  python: 3.12.13
  pandoc: 3.1.3
ci:
  workflow: Build Publication Formats
  run-id: {RUN_ID}
  artifact-id: {ARTIFACT_ID}
  artifact-digest: {DIGEST}
visual-inspection:
  rendered-pages: [1, 2]
  result: readable-no-overlap-no-broken-glyphs
reservations:
  - No tagged accessible PDF is produced.
  - No byte-identical cross-platform claim.
  - No official release or public publication.
  - No exhaustive visual inspection of all 4108 PDF pages or EPUB readers.
"""
write("QA/VALIDATION-PUBLICATION-FORMATS.yaml", proof)

audit = read("QA/AUDIT-PUBLICATION-FORMATS.md")
audit = audit.replace('status: "candidate"', 'status: "reviewed"', 1)
audit = audit.replace('audit-level: "runtime-candidate-linux"', 'audit-level: "runtime-tested-linux"', 1)
audit += f"""

## Résultat qualifié

Le run `{RUN_ID}` a construit et validé 162 sources sous Ubuntu 24.04 avec Python 3.12.13 et Pandoc 3.1.3 : PDF de 4 108 pages, HTML autonome et EPUB 3. L'artefact `{ARTIFACT_ID}` porte le digest `{DIGEST}`. Les pages PDF 1 et 2 ont été rendues et inspectées visuellement : couverture et table des matières lisibles, sans chevauchement ni glyphe cassé.
"""
write("QA/AUDIT-PUBLICATION-FORMATS.md", audit)

roadmap = read("ROADMAP.md")
roadmap = replace_once(
    roadmap,
    "- [ ] Produire les versions PDF, HTML et EPUB.",
    "- [x] Produire les versions PDF, HTML et EPUB — 162 sources, PDF de 4 108 pages, HTML autonome et EPUB 3 validés sous Linux.",
    "ROADMAP publication formats",
)
write("ROADMAP.md", roadmap)

continuity = read("CONTINUITE-PROJET.md")
continuity = replace_once(continuity, 'version: "4.25.0"', 'version: "4.26.0"', "continuity version")
continuity = replace_once(continuity, 'last-updated: "2026-07-30T18:26:37+02:00"', f'last-updated: "{STAMP}"', "continuity timestamp")
old_action = """M8 — Publications est actif. La licence globale est définie par catégories de droits et de fichiers : documentation sous `CC-BY-SA-4.0`, logiciel et ressources techniques sous `MIT`, métadonnées factuelles explicitement classées sous `CC0-1.0`. Les composants tiers conservent leur licence d’origine et sont exclus de toute relicence automatique.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
M8 — Publications
Produire les versions PDF, HTML et EPUB.
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le prochain lot doit générer les formats de collection à partir des sources maîtrisées, embarquer les attributions et notices de licence, vérifier les liens et métadonnées, et ne pas confondre génération technique avec publication officielle.
"""
new_action = """M8 — Publications est actif. La chaîne commune génère désormais depuis 162 sources un PDF A4, un HTML autonome et un EPUB 3, avec manifeste SHA-256, licence éditoriale et statut explicite de build technique. La génération a été qualifiée sur Linux ; aucune release officielle n'a été créée.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
M8 — Publications
Produire un PDF balisé pour les lecteurs d’écran.
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le prochain lot doit traiter la structure logique, les titres, la langue, l'ordre de lecture, les alternatives textuelles et la vérification avec des outils d'accessibilité, sans dégrader le PDF visuel existant ni revendiquer une conformité non testée.
"""
continuity = replace_once(continuity, old_action, new_action, "continuity next action")
journal = f"""### {STAMP} — version 4.26.0

- chaîne commune PDF, HTML autonome et EPUB 3 ajoutée ;
- wrappers Bash et PowerShell alignés sur `tools/build_publications.py` ;
- 162 sources compilées dans l'ordre de `contents.txt` ;
- PDF de 4 108 pages, 10 571 878 octets, SHA-256 `ca360a66a820a4dbd9951acd4c45e16c5bb8560fd5a0323620455307b1e9dcd4` ;
- HTML autonome de 18 721 066 octets, SHA-256 `411671facba03ac6b194e42b664a67d55eb459a34cdd37fb73ea363a99a274ee` ;
- EPUB 3 de 3 864 620 octets et 173 entrées, SHA-256 `a6db51c39e37b848cefb63d2a80926c1f35ed89169f6f32bd67859fdf6c31b96` ;
- manifeste, contrôles PDF/HTML/EPUB, licences et état Git propre validés ;
- pages PDF 1 et 2 rendues et inspectées sans chevauchement ni glyphe cassé ;
- run `{RUN_ID}`, artefact `{ARTIFACT_ID}`, digest `{DIGEST}` ;
- tâche M8 « produire les versions PDF, HTML et EPUB » clôturée ;
- prochaine action : produire un PDF balisé pour les lecteurs d'écran, niveau Élevée ;
- aucune release, publication publique, conformité EPUBCheck complète, PDF balisé ou identité byte pour byte inter-plateformes revendiquée.

"""
continuity = replace_once(continuity, "## 27. Journal\n\n", "## 27. Journal\n\n" + journal, "continuity journal")
write("CONTINUITE-PROJET.md", continuity)

subprocess.run(["python", "tools/validate_chapters.py"], check=True)
subprocess.run(["python", "tools/validate_licenses.py", "--report", "/tmp/licensing.json"], check=True)
subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
subprocess.run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], check=True)
subprocess.run(["git", "add", "QA/AUDIT-PUBLICATION-FORMATS.md", "QA/VALIDATION-PUBLICATION-FORMATS.yaml", "ROADMAP.md", "CONTINUITE-PROJET.md"], check=True)
subprocess.run(["git", "commit", "-m", "docs(publications): qualifier les formats et poursuivre M8"], check=True)
subprocess.run(["git", "push", "origin", "HEAD:feat/publication-formats-pdf-html-epub"], check=True)
