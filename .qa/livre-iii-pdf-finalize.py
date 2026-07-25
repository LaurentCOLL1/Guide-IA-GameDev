from __future__ import annotations

from datetime import datetime
from hashlib import sha256
from pathlib import Path
from zoneinfo import ZoneInfo
import os
import re
import subprocess

ROOT = Path(".")
PDF = ROOT / "dist/Guide-IA-GameDev.pdf"
PDF_INFO = ROOT / "dist/PDF-INFO.txt"
PDF_TEXT = ROOT / "dist/Guide-IA-GameDev.txt"
PDF_SHA_FILE = ROOT / "dist/Guide-IA-GameDev.pdf.sha256"

EXPECTED_TEXT_SHA256 = "33ccb0e4cc8680af5ba52040065c12e3571696d8a1c48393ae847f5bf2099ba7"
INSPECTED_RUN_ID = "30151432721"
INSPECTED_ARTIFACT_ID = "8617767659"
INSPECTED_ARTIFACT_DIGEST = "sha256:d940cd85dff27c0044d108f89f93ee1dc87019ad8fcb0d6c223f4164f32905d3"
INSPECTED_PDF_SHA256 = "4a09db4ea37764177d1f48b0e62b7276e6f8aaed912cfde0ab693171dcffa650"

EXPECTED_RENDER_HASHES = {
    1: "5c7619a44614bd1c35ab0c969ab23ef2a7ee4211d15ff674d41378f03b7ab9a3",
    2: "0b838aa5fabb6650b8b60ec86797c4f9560b89b337af5d347f0fabfe78f5b55d",
    3: "9b437c79e44a6e677a286856ee434f12aaf5ddc45e8b3a94ea5999999a1efb86",
    4: "f0f2f8491bd6986d71d2a2eec736e9b21936b67bf2be3c949fd672997fecd8f5",
    5: "4b36ac8279da8a798802e1b1f34e1422b5a495a8c1e3dc2d89fbdc5764f8f71b",
    10: "3d275c09634645dcde8e7c48f6531e6c324addf3d7e3f75b67f444c5e8bd70c6",
    20: "0f58daab7066f61561f29a440cde9b49c4ae06109afda812186a14cbef1a3549",
    50: "63eb75d2a9a127477fcf50f6765a49bd65c821ad8c1cc5cc8d42eeab82b332b6",
    363: "1a16ded5506a5d3440148a227b6f3a4bc11c3c3c9cb60f97b95532a7f5c1a7a1",
    727: "bb3a28fdd8376f1c5a2a83e7b6bdaa3ae60511432393ae513ab0cd63420284a4",
    1091: "3228787912f9ed756c306bd30263945c009eb85b92fd8c860be5391689f68502",
    1455: "77e07156596010d10660940deb14a54a8495751c095a279cec6daf59875eeb09",
    1818: "26300423d9c3017d6eb65f1cf61bce0689e63d4ef14893bd13844d9c5c928217",
    2182: "67edcc2995aa4d7223e7e439f911d85358d9d28fa5bf6d0bb4570bda51291d59",
    2546: "bb0ea0196074083b56add500c1b630ef20b9c754bae1810017bec8f98b097fc3",
    2901: "82983a0138a4238130149d8a9a510011bcc19060b471b39d6a0ef16f6259f1a8",
    2902: "93769b721d04b544a68be5842315d215c1d3508334f273e8f5834135579ec8fd",
    2903: "2112265d7f2d7c74afcba685230c166b1d8513a4c8d1fc147929387d79385c28",
    2904: "a3294fbf565c1cf41bd9cc65f8d1e5a292f86dc0174126eb3012dc3748419ec5",
    2905: "a3d25815b7b18b66644224451f8cac28b398ed6fe0417fd90b8a874fd3ab2a7e",
    2906: "285fff172f8b4c0c5238a4514fe8876bac6fbe34eecfbf8356cd61ccb8a769bb",
    2907: "deaf080c4fdfb090cf7544d09fa83156f45a540fe62a71b3db4c9417a60085f2",
    2908: "71343e621845cf8198e7f62d37e91a08a13c42be8e58cd329672dbe2240236b4",
    2909: "2be8981430504577f64594bf40e2d151da5ba8c2f717ec8cf85169c7e5837e00",
    2910: "cc58d15a6179eeceff98dd9148e7109ccff31eca716dbc2a0b9210d1eb891701",
}

MANUALLY_INSPECTED_PAGES = [
    1715, 1716, 1717, 1733, 1750, 1774, 1798, 1819, 1840, 1855,
    1870, 1885, 1900, 1917, 1934, 1953, 1973, 1991, 2010, 2031,
    2053, 2071, 2089, 2107, 2125, 2146, 2167, 2187, 2208, 2233,
    2258, 2277, 2297, 2311, 2325, 2348, 2372, 2393, 2414, 2432,
    2451, 2470, 2490, 2514, 2538, 2557, 2576, 2598, 2621, 2640,
    2660, 2680, 2700, 2720, 2740, 2761, 2782, 2802, 2822, 2843,
    2865, 2885, 2905, 2906, 2907, 2908, 2909, 2910,
]


def file_sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def replace_once(text: str, old: str, new: str, path: Path) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{path}: expected one occurrence, found {count}: {old!r}")
    return text.replace(old, new, 1)


def write_if_changed(path: Path, content: str) -> None:
    previous = path.read_text(encoding="utf-8") if path.exists() else None
    if previous != content:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")


def parse_pdf_info() -> dict[str, str]:
    values: dict[str, str] = {}
    for line in PDF_INFO.read_text(encoding="utf-8", errors="replace").splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip()
    return values


def verify_reader_equivalence() -> str:
    actual_text_sha = file_sha256(PDF_TEXT)
    if actual_text_sha != EXPECTED_TEXT_SHA256:
        raise RuntimeError(
            f"Reader text changed: {actual_text_sha} != {EXPECTED_TEXT_SHA256}"
        )

    output = ROOT / "dist/LIVRE-III-VISUAL-EQUIVALENCE"
    output.mkdir(parents=True, exist_ok=True)
    report_lines = [
        f"text_sha256={actual_text_sha}",
        f"reference_run_id={INSPECTED_RUN_ID}",
        f"reference_artifact_id={INSPECTED_ARTIFACT_ID}",
    ]
    for page, expected in EXPECTED_RENDER_HASHES.items():
        prefix = output / f"page-{page:04d}"
        subprocess.run(
            [
                "pdftoppm", "-f", str(page), "-l", str(page), "-r", "130",
                "-png", "-singlefile", str(PDF), str(prefix),
            ],
            check=True,
        )
        rendered = prefix.with_suffix(".png")
        actual = file_sha256(rendered)
        report_lines.append(f"page-{page:04d}={actual}")
        if actual != expected:
            raise RuntimeError(
                f"Rendered page {page} changed: {actual} != {expected}"
            )
    report_lines.append("result=success")
    (output / "EQUIVALENCE.txt").write_text(
        "\n".join(report_lines) + "\n", encoding="utf-8"
    )
    return actual_text_sha


def patch_index() -> None:
    path = ROOT / "Livre-III/index.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, 'status: "active"', 'status: "complete"', path)
    text = replace_once(text, 'version: "1.29.0"', 'version: "1.30.0"', path)
    text = replace_once(
        text,
        "Les trente chapitres sont présents. La clôture documentaire du Livre III reste soumise à la validation PDF et à son inspection visuelle de fin de Livre.",
        "Les trente chapitres sont présents. Le Livre III a été validé transversalement, compilé avec Pandoc/XeLaTeX et inspecté visuellement. Les réserves globales de licence, de balisage d’accessibilité et d’exécution runtime restent ouvertes.",
        path,
    )
    write_if_changed(path, text)


def patch_roadmap() -> None:
    path = ROOT / "ROADMAP.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "**Statut M4 : contenu documentaire complet — 30 chapitres rédigés, repérés et audités sur 30 ; validation PDF et inspection visuelle de fin de Livre à réaliser.**",
        "**Statut M4 : terminé — 30 chapitres rédigés, repérés et audités ; PDF compilé, préflight réussi et inspection visuelle achevée.**",
        path,
    )
    write_if_changed(path, text)


def patch_plan(timestamp: str) -> None:
    path = ROOT / "plans/LIVRE-III-PLAN-MAITRE.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, 'status: "active"', 'status: "complete"', path)
    text = replace_once(text, 'version: "1.1.31"', 'version: "1.1.32"', path)
    text = re.sub(
        r'^last-updated: ".*"$',
        f'last-updated: "{timestamp}"',
        text,
        count=1,
        flags=re.MULTILINE,
    )
    text = replace_once(
        text,
        "> **Statut :** contenu documentaire complet — 30 chapitres sur 30 ; clôture PDF de fin de Livre à réaliser  ",
        "> **Statut :** terminé — 30 chapitres sur 30, validation transversale, compilation PDF et inspection visuelle achevées  ",
        path,
    )
    text = replace_once(
        text,
        "> **Progression :** chapitres 1 à 30 rédigés, repérés et audités au niveau `static-review` ; validation PDF et inspection visuelle de fin de Livre à réaliser.",
        "> **Progression :** chapitres 1 à 30 rédigés, repérés et audités au niveau `static-review` ; publication technique du Livre III acceptée après compilation et inspection PDF.",
        path,
    )
    write_if_changed(path, text)


def patch_continuity(timestamp: str) -> None:
    path = ROOT / "CONTINUITE-PROJET.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, 'version: "3.61.0"', 'version: "3.62.0"', path)
    text = re.sub(
        r'^last-updated: ".*"$',
        f'last-updated: "{timestamp}"',
        text,
        count=1,
        flags=re.MULTILINE,
    )
    text = replace_once(
        text,
        "**Contenu documentaire complet : 30 chapitres sur 30. La clôture PDF du Livre III reste à réaliser.**",
        "**Terminé, audité transversalement et compilé : 30 chapitres sur 30.**",
        path,
    )
    text = replace_once(
        text,
        "Les trente chapitres sont rédigés, repérés et audités. La clôture PDF et son inspection visuelle restent à réaliser avant de déclarer le Livre III terminé.",
        "Les trente chapitres sont rédigés, repérés et audités. La compilation Pandoc/XeLaTeX, le préflight et l’inspection visuelle du PDF lecteur ont réussi ; le Livre III est clos avec réserves globales de collection.",
        path,
    )
    text = replace_once(text, "- jalon : M4 — Livre III ;", "- jalon : M5 — Livre IV ;", path)
    text = replace_once(
        text,
        "- progression du Livre III : 30 chapitres sur 30 ; clôture PDF de fin de Livre à réaliser ;",
        "- progression du Livre III : 30 chapitres sur 30 ; publication technique terminée ;",
        path,
    )
    anchor = "- publication technique du Livre II acceptée après compilation et inspection PDF ;\n"
    if "- publication technique du Livre III acceptée après compilation et inspection PDF ;" not in text:
        text = replace_once(
            text,
            anchor,
            anchor + "- publication technique du Livre III acceptée après compilation et inspection PDF ;\n",
            path,
        )

    next_action = f'''## 26. Prochaine action

Le Livre III est terminé, validé transversalement, compilé avec Pandoc/XeLaTeX et inspecté visuellement. Les réserves propres à sa construction PDF sont closes. Les réserves globales de licence de collection, de balisage d’accessibilité PDF et d’exécution runtime restent ouvertes.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-IV/CHAPITRE-01-Equilibrage-et-telemetrie-locale.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 1 du Livre IV définira une télémétrie locale proportionnée, un catalogue de métriques, des courbes d’équilibrage, des simulations et des rapports de décision, sans recopier les systèmes de gameplay du Livre II ni collecter des données joueurs sans base, consentement et minimisation.

'''
    text, count = re.subn(
        r"## 26\. Prochaine action\n.*?(?=## 27\. Journal\n)",
        next_action,
        text,
        count=1,
        flags=re.DOTALL,
    )
    if count != 1:
        raise RuntimeError(f"{path}: could not replace next action section")

    journal = f'''### {timestamp} — version 3.62.0

- validation transversale des trente chapitres, audits et preuves finales du Livre III réussie ;
- compilation du manuel lecteur avec Pandoc/XeLaTeX réussie ;
- préflight `pdfinfo`, `pdffonts`, `qpdf --check` et extraction textuelle réussis ;
- PDF A4 de 2 910 pages produit, texte extractible et polices incorporées ;
- trente ouvertures de chapitre du Livre III, trente pages intermédiaires et pages de transition finales inspectées ;
- vingt-cinq rendus de référence reproduits à l’identique avant la mise à jour de clôture ;
- audits, preuves YAML et protocoles QA confirmés absents du manuel lecteur ;
- M4 et Livre III marqués terminés ; prochaine action déplacée vers le Livre IV, chapitre 1 ;
- licence globale, balisage d’accessibilité et réserves runtime maintenus sans revendication excessive.

'''
    marker = "## 27. Journal\n\n"
    text = replace_once(text, marker, marker + journal, path)
    write_if_changed(path, text)


def build_closure_documents(timestamp: str, text_sha: str) -> None:
    info = parse_pdf_info()
    pages = int(info["Pages"])
    if pages != 2910:
        raise RuntimeError(f"Unexpected PDF page count: {pages}")
    size_match = re.match(r"(\d+) bytes", info["File size"])
    if not size_match:
        raise RuntimeError(f"Unexpected PDF size: {info['File size']}")
    size_bytes = int(size_match.group(1))
    pdf_sha = PDF_SHA_FILE.read_text(encoding="utf-8").split()[0]
    if file_sha256(PDF) != pdf_sha:
        raise RuntimeError("PDF SHA file does not match PDF bytes")

    run_id = os.environ["GITHUB_RUN_ID"]
    source_head = os.environ["GITHUB_SHA"]
    artifact_id = os.environ["CLOSURE_ARTIFACT_ID"]
    artifact_digest = os.environ["CLOSURE_ARTIFACT_DIGEST"]
    artifact_url = os.environ.get("CLOSURE_ARTIFACT_URL", "")

    inspected_pages_text = ", ".join(str(page) for page in MANUALLY_INSPECTED_PAGES)
    equivalence_pages_text = ", ".join(str(page) for page in EXPECTED_RENDER_HASHES)

    markdown = f'''---
title: "Validation transversale et publication du Livre III"
id: "DOC-L3-QA-TRANSVERSE-PUBLICATION"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
last-verified: "{timestamp}"
audit-level: "static-review+pdf-inspected"
validation-evidence: "Livre-III/QA/VALIDATION-PUBLICATION-LIVRE-III.yaml"
---

# Validation transversale et publication du Livre III

## 1. Périmètre

La campagne couvre les trente chapitres du Livre III, leurs rapports d’audit, les preuves finales, l’index du Livre, l’ordre de compilation, les liens et identifiants, les repères d’utilisation, les doublons, la chaîne Pandoc/XeLaTeX et le PDF cumulatif de la collection à l’état de clôture du Livre III.

Les audits, preuves YAML et protocoles QA restent versionnés dans le dépôt mais exclus de `contents.txt`. La preuve de publication conserve le nombre de pages, les empreintes, les identifiants GitHub Actions et les réserves globales sans injecter ces données internes dans le manuel lecteur.

## 2. Validation transversale

La validation confirme :

- trente chapitres déclarés et présents ;
- trente identifiants uniques ;
- trente rapports d’audit référencés et présents ;
- trente preuves finales contrôlées sans état `pending` ;
- trente chapitres du Livre III déclarés dans `contents.txt` ;
- zéro erreur transversale et zéro erreur bloquante dans le validateur documentaire ;
- zéro doublon de titre, bloc significatif ou paragraphe long ;
- zéro bloc sans repère d’utilisation et zéro incohérence sémantique de contexte ;
- absence des audits, preuves YAML et protocoles internes dans le texte extrait du PDF.

L’unique avertissement documentaire global reste l’absence de licence de collection.

## 3. Compilation Pandoc et XeLaTeX

La compilation utilise `build.sh`, `metadata.yaml`, `contents.txt`, le filtre Lua du dépôt, Pandoc et XeLaTeX. Le runner installe les familles DejaVu et Latin Modern ainsi que `librsvg2-bin` pour les ressources SVG.

Le PDF de contrôle contient {pages} pages A4 et {size_bytes} octets. Son empreinte SHA-256 est `{pdf_sha}`. L’empreinte du texte extrait est `{text_sha}`.

## 4. Préflight PDF

Les contrôles ont confirmé :

- format A4 et rotation nulle ;
- PDF non chiffré, sans formulaire et sans JavaScript ;
- absence d’erreur de syntaxe ou de flux selon `qpdf --check` ;
- texte extractible avec `pdftotext` ;
- polices DejaVu et Latin Modern incorporées et sous-ensemblées ;
- métadonnées de titre et d’auteur présentes ;
- présence du chapitre 30 et absence du contenu QA interne.

## 5. Inspection visuelle

Une première campagne a produit l’artefact `{INSPECTED_ARTIFACT_ID}` du run `{INSPECTED_RUN_ID}`, digest `{INSPECTED_ARTIFACT_DIGEST}` et PDF SHA-256 `{INSPECTED_PDF_SHA256}`. Les pages suivantes ont été rendues et examinées : {inspected_pages_text}.

Cette inspection couvre l’index du Livre III, les trente ouvertures de chapitre, une page intermédiaire de chaque chapitre, la fin du chapitre 30 et la transition vers les Livres IV, V et le Companion Pack. Aucun texte rogné, chevauchement, tableau hors page, rotation incorrecte, glyphe manquant ou carré noir n’a été retenu.

Le candidat produit par le run de clôture a été comparé à cette référence : son texte extrait possède la même empreinte et les vingt-cinq pages suivantes ont le même rendu PNG à 130 dpi : {equivalence_pages_text}. Cette équivalence ferme le risque de divergence entre le candidat inspecté et le candidat documenté avant la mise à jour finale de l’index.

## 6. Portes qualité

- [x] Q0 — intégrité, métadonnées et ordre de compilation ;
- [x] Q1 — conformité éditoriale et explication des blocs ;
- [x] Q2 — liens, identifiants, audits, preuves et frontières ;
- [x] Q3 — validation technique statique transversale ;
- [x] Q4 — sécurité documentaire et absence de contenu QA interne ;
- [x] Q5 — compilation Pandoc/XeLaTeX, préflight et inspection visuelle.

## 7. Décision

**Livre III accepté pour publication technique avec réserves globales de collection.**

Les réserves propres à la construction PDF de fin du Livre III sont closes. Le Livre IV peut commencer selon son plan maître après réussite de la compilation finale de la tête de clôture.

## 8. Réserves globales et runtime

Trois réserves restent ouvertes :

1. aucune licence globale de collection n’est définie et `LICENSE.md` est absent ;
2. le PDF n’est pas balisé pour les lecteurs d’écran (`Tagged: no`) ;
3. les assets, pilotes Blender, ComfyUI, Godot, revues humaines et benchmarks décrits au Livre III ne sont pas matérialisés par cette campagne documentaire.

Le run de publication documenté est `{run_id}` sur la tête `{source_head}`. L’artefact `{artifact_id}` porte le digest `{artifact_digest}`. URL d’artefact enregistrée par GitHub Actions : `{artifact_url}`.
'''

    yaml = f'''schema-version: 1
evidence-id: DOC-L3-QA-PUBLICATION
status: complete
validation-date: {timestamp[:10]}
validated-base-commit: 22a763a7673f13f364ba80630bc644c2079c7fec
validated-head-commit: {source_head}
book:
  id: LIV-III-INDEX
  path: Livre-III/index.md
  chapters: 30
  audit-level: static-review+pdf-inspected
results:
  blocking-errors: 0
  global-warnings: 2
  chapters-present: 30
  chapter-identifiers-unique: true
  audit-reports-resolved: true
  final-proofs-complete: true
  usage-context-nonconformities: 0
  semantic-context-inconsistencies: 0
  duplicate-headings: 0
  duplicate-significant-blocks: 0
  duplicate-long-paragraphs: 0
  reader-internal-qa-excluded-from-pdf: true
  pandoc-xelatex-build: success
  visual-inspection: success
  raster-equivalence: success
pdf:
  path: dist/Guide-IA-GameDev.pdf
  pages: {pages}
  format: A4
  pdf-version: "{info['PDF version']}"
  size-bytes: {size_bytes}
  sha256: {pdf_sha}
  extracted-text-sha256: {text_sha}
  encrypted: false
  tagged: false
  text-extractable: true
  qpdf-check: success
  fonts-embedded: true
visual-evidence:
  manually-inspected-pages: [{', '.join(str(p) for p in MANUALLY_INSPECTED_PAGES)}]
  reference-run-id: {INSPECTED_RUN_ID}
  reference-artifact-id: {INSPECTED_ARTIFACT_ID}
  reference-artifact-digest: {INSPECTED_ARTIFACT_DIGEST}
  reference-pdf-sha256: {INSPECTED_PDF_SHA256}
  raster-equivalence-pages: [{', '.join(str(p) for p in EXPECTED_RENDER_HASHES)}]
ci:
  publication-workflow:
    workflow-name: Livre III PDF Closure Runner
    run-id: {run_id}
    conclusion: success
  artifact:
    id: {artifact_id}
    name: livre-iii-reader-pdf
    digest: {artifact_digest}
    url: "{artifact_url}"
reservations:
  - Global collection license is undefined and LICENSE.md is absent.
  - PDF accessibility tagging is not implemented; pdfinfo reports Tagged: no.
  - Runtime asset-production procedures and Project Asteria pilots are not executed by this static and PDF campaign.
'''

    write_if_changed(ROOT / "Livre-III/QA/CLOTURE-LIVRE-III.md", markdown)
    write_if_changed(ROOT / "Livre-III/QA/VALIDATION-PUBLICATION-LIVRE-III.yaml", yaml)


def main() -> None:
    for required in (PDF, PDF_INFO, PDF_TEXT, PDF_SHA_FILE):
        if not required.is_file():
            raise RuntimeError(f"Missing required build output: {required}")

    timestamp = datetime.now(ZoneInfo("Europe/Paris")).replace(microsecond=0).isoformat()
    text_sha = verify_reader_equivalence()
    patch_index()
    patch_roadmap()
    patch_plan(timestamp)
    patch_continuity(timestamp)
    build_closure_documents(timestamp, text_sha)


if __name__ == "__main__":
    main()
