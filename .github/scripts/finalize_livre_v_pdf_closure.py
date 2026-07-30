from __future__ import annotations

import os
import re
from pathlib import Path

TIMESTAMP = "2026-07-30T03:00:00+02:00"
DATE = "2026-07-30"
PDF_RUN_ID = 30503741584
PDF_HEAD_COMMIT = "28ff5ad6e952d45b5cfebb53237197e7177d1e94"
PDF_ARTIFACT_ID = 8744567647
PDF_ARTIFACT_DIGEST = "sha256:b8300a8a449b89606f9a1b80551454d17f3205bb8f1131451676fc514a4ff221"
PDF_SHA256 = "008ae82f759f562178b810e87abbd08c0e00bf6dd6eba4afeb5334748feda8a3"
TEXT_SHA256 = "6734cb86d214264e55b0f2ef188be73c55ccfed050c9374d43cde37ad6e58df5"
PDF_PAGES = 4063
PDF_SIZE = 10462788
FINALIZER_RUN_ID = os.environ.get("FINALIZER_RUN_ID", "unknown")


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, content: str) -> None:
    Path(path).write_text(content, encoding="utf-8", newline="\n")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one occurrence, found {count}")
    return text.replace(old, new, 1)


report = f'''---
title: "Clôture technique et PDF — Livre V"
id: "DOC-L5-QA-CLOSURE"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
last-verified: "{TIMESTAMP}"
audit-level: "static-review+pdf-inspected"
target-book: "Livre V"
---

# Clôture technique et PDF — Livre V

## 1. Décision

La publication technique du Livre V est **acceptée au niveau `static-review+pdf-inspected`**. Les 26 fiches sont présentes dans le PDF cumulatif, les validations documentaires sont vertes, le préflight structurel est réussi et l’échantillon visuel ne révèle ni texte coupé, ni chevauchement, ni glyphe cassé, ni page anormalement vide.

Cette décision porte sur le document lecteur et sa chaîne de publication. Elle ne constitue ni une validation runtime du projet, ni une décision de licence globale, ni une publication commerciale.

## 2. Corpus et chaîne

- corpus lecteur : 145 sources déclarées par `contents.txt` ;
- Livre V : `Livre-V/index.md` et 26 fiches ;
- construction : `build.sh` → Pandoc → XeLaTeX → `dist/Guide-IA-GameDev.pdf` ;
- préflight : `qpdf`, `pdfinfo`, `pdffonts` et `pdftotext` ;
- inspection : Poppler et PDFium ;
- QA internes, audits, preuves et protocoles : exclus du PDF lecteur.

## 3. Corrections nécessaires à la compilation

Deux défauts de chaîne ont été corrigés sans modifier le contenu sémantique :

1. dans la fiche 05, deux séparateurs `---` immédiatement suivis d’un marqueur `l5:card` ont reçu la ligne vide attendue afin que Pandoc ne les interprète pas comme des blocs YAML ;
2. le runner de compilation a installé explicitement le paquet `lmodern`, requis par la chaîne XeLaTeX.

Le diagnostic Pandoc par source a ensuite confirmé que les 145 documents lecteur sont parsables indépendamment.

## 4. Validations automatisées

| Contrôle | Résultat |
|---|---|
| structure, métadonnées, liens et doublons | réussi |
| cartes et liens profonds du Livre V | réussi |
| explications structurées du code | réussi |
| repères d’utilisation et cohérence sémantique | réussi |
| couverture des contextes | mesurée sans erreur bloquante |
| compilation Pandoc/XeLaTeX | réussie |
| présence de l’index et des 26 titres du Livre V | réussie |
| exclusion des contenus QA internes | réussie |
| `qpdf --check` | aucune erreur de syntaxe ou de flux |
| polices | incorporées et sous-ensemblées ; aucun Type 3 ou type inconnu |
| texte extractible | oui |

## 5. Caractéristiques du PDF

| Propriété | Valeur |
|---|---|
| fichier | `dist/Guide-IA-GameDev.pdf` |
| pages | {PDF_PAGES} |
| taille | {PDF_SIZE} octets |
| format | A4, 595,28 × 841,89 points |
| version PDF | 1.5 |
| chiffrement | non |
| linéarisation | non |
| texte extractible | oui |
| PDF balisé | non |
| champs de formulaire | 0 |
| pièces jointes | 0 |
| éléments de plan | 7 204 |
| annotations et liens | 11 060 |

## 6. Cartographie du Livre V

- index du Livre V : page 3 681 ;
- fiche 01 : page 3 683 ;
- fiche 26 : page 4 048 ;
- dernière page du Livre V : page 4 062 ;
- entrée du Companion Pack : page 4 063.

Le fichier `LIVRE-V-PAGE-MAP.json` de l’artefact conserve les ouvertures des 26 fiches, leurs occurrences textuelles, les 82 pages d’échantillon et les pages de parité.

## 7. Inspection visuelle

### Poppler

**82 pages** ont été rendues et inspectées : index, ouverture, deuxième page et page intermédiaire de chaque fiche lorsque disponible, dernière page du Livre V et première page du Companion Pack.

### PDFium

**8 pages** ont été rendues avec PDFium et comparées à Poppler : 3 681, 3 683, 3 758, 3 862, 3 967, 4 048, 4 062 et 4 063.

### Conclusion visuelle

- hiérarchie des titres cohérente ;
- tableaux contenus dans la page ;
- liens et code lisibles ;
- aucun chevauchement ou rognage observé ;
- aucun carré noir, glyphe absent ou corruption de police observé ;
- mêmes contenus, sauts de ligne et limites de pages avec les deux moteurs ;
- seules les différences normales d’anticrénelage raster subsistent.

## 8. Intégrité et artefact

- workflow : `Livre V PDF Closure Runner V2` ;
- run : `{PDF_RUN_ID}` ;
- commit source : `{PDF_HEAD_COMMIT}` ;
- artefact : `{PDF_ARTIFACT_ID}` ;
- digest de l’artefact : `{PDF_ARTIFACT_DIGEST}` ;
- SHA-256 du PDF : `{PDF_SHA256}` ;
- SHA-256 du texte extrait : `{TEXT_SHA256}` ;
- finalisation de gouvernance : run `{FINALIZER_RUN_ID}`.

## 9. Réserves

- la licence globale de la collection reste indécise ;
- le PDF n’est pas qualifié comme document balisé pour lecteurs d’écran ;
- les formats HTML et EPUB ne sont pas produits par cette campagne ;
- aucune procédure runtime, plateforme, performance, sécurité produit, restauration ou publication commerciale n’est validée ici ;
- le Starter Kit et les autres ressources du Companion Pack ne sont pas encore matérialisés.

## 10. Porte suivante

M6 — Livre V est terminé. Le jalon actif devient **M7 — Companion Pack**, avec le **Pack 1 — Starter Kit** comme prochaine action. Son point d’entrée canonique à créer est `Companion-Pack/Starter-Kit/README.md`.
'''
write("Livre-V/QA/CLOTURE-LIVRE-V.md", report)

proof = f'''schema-version: 2
evidence-id: DOC-L5-QA-PUBLICATION
validation-authority: livre-v-publication-profile
status: complete
validation-date: '{DATE}'
validated-base-commit: 7f530fa47512768d543dba936fcae540c2a06de7
source-branch: qa/livre-v-pdf-closure
book:
  id: LIV-V-INDEX
  path: Livre-V/index.md
  chapters: 26
  audit-level: static-review+pdf-inspected
results:
  blocking-errors: 0
  reader-sources: 145
  livre-v-chapters: 26
  all-reader-sources-parse-with-pandoc: true
  all-chapter-titles-present-in-pdf: true
  reader-internal-qa-excluded-from-pdf: true
  pandoc-xelatex-build: success
  qpdf-check: success
  fonts-embedded: true
  type3-or-unknown-fonts: false
  text-extractable: true
  visual-inspection: success
  renderer-parity: success
  runtime-tests: 0
  global-license-selected: false
pdf:
  path: dist/Guide-IA-GameDev.pdf
  pages: {PDF_PAGES}
  size-bytes: {PDF_SIZE}
  page-size: A4
  page-size-points: 595.28 x 841.89
  format-version: '1.5'
  encrypted: false
  linearized: false
  tagged: false
  text-extractable: true
  outline-items: 7204
  form-fields: 0
  attachments: 0
  annotations: 11060
  sha256: {PDF_SHA256}
  extracted-text-sha256: {TEXT_SHA256}
page-map:
  livre-v-index-page: 3681
  first-card-page: 3683
  chapter-26-page: 4048
  livre-v-last-page: 4062
  companion-pack-first-page: 4063
visual-inspection:
  poppler:
    sample-pages: 82
    dpi: 100
    conclusion: pass
  pdfium:
    sample-pages: 8
    pages:
      - 3681
      - 3683
      - 3758
      - 3862
      - 3967
      - 4048
      - 4062
      - 4063
    dpi: 120
    conclusion: pass
  observed-defects:
    clipping: 0
    overlaps: 0
    broken-glyphs: 0
    black-boxes: 0
    abnormally-empty-pages: 0
ci:
  final-reader-build:
    workflow: Livre V PDF Closure Runner V2
    run-id: {PDF_RUN_ID}
    head-commit: {PDF_HEAD_COMMIT}
    conclusion: success
    artifact-id: {PDF_ARTIFACT_ID}
    artifact-digest: {PDF_ARTIFACT_DIGEST}
  governance-finalization:
    workflow: Temporary Livre V PDF Closure Finalizer
    run-id: {FINALIZER_RUN_ID}
    conclusion: success
reservations:
  - The global collection license is undefined and LICENSE.md is absent.
  - The PDF is not qualified as tagged for screen readers.
  - HTML and EPUB were not produced in this campaign.
  - No runtime, platform, performance, security-product, recovery or commercial-publication procedure was validated.
  - The Starter Kit and other Companion Pack resources are not materialized.
'''
write("Livre-V/QA/VALIDATION-PUBLICATION-LIVRE-V.yaml", proof)

index_path = "Livre-V/index.md"
index = read(index_path)
index = replace_once(index, 'status: "active"', 'status: "complete"', "Livre V index status")
index = replace_once(index, 'version: "1.18.0"', 'version: "1.19.0"\nlast-updated: "2026-07-30T03:00:00+02:00"', "Livre V index version")
old_status = "Progression : **26 chapitres sur 26** rédigés et audités au niveau `static-review`. La fiche 26 clôt la couverture documentaire par identités canoniques, index alphabétiques et thématiques, synonymes, relations typées, routes par domaine, navigation multiformat et contrôles d’intégrité. La construction, le préflight et l’inspection du PDF complet du Livre V, les formats HTML/EPUB, l’accessibilité avancée, la licence globale et les outils exécutables du Companion Pack restent des portes séparées."
new_status = f"Progression : **26 chapitres sur 26** rédigés et audités. La publication technique est acceptée au niveau `static-review+pdf-inspected` : PDF cumulatif de {PDF_PAGES} pages, préflight réussi, 26 titres présents, QA internes exclues et inspection visuelle Poppler/PDFium achevée. Voir le [rapport de clôture](QA/CLOTURE-LIVRE-V.md). La licence globale, les formats HTML/EPUB, le balisage avancé d’accessibilité et les outils du Companion Pack restent des portes séparées."
index = replace_once(index, old_status, new_status, "Livre V index status paragraph")
write(index_path, index)

roadmap_path = "ROADMAP.md"
roadmap = read(roadmap_path)
roadmap = replace_once(
    roadmap,
    "**Statut M6 : en cours — 26 chapitres rédigés, repérés et audités sur 26 ; la construction, le préflight et l’inspection du PDF complet du Livre V restent la porte de clôture technique.**",
    "**Statut M6 : terminé — 26 chapitres rédigés, repérés et audités ; PDF cumulatif construit, préflighté et inspecté au niveau `static-review+pdf-inspected`.**",
    "ROADMAP M6 status",
)
roadmap = replace_once(
    roadmap,
    "## M7 — Companion Pack\n\n- [ ] Starter Kit.",
    "## M7 — Companion Pack\n\n**Statut M7 : actif — Pack 1, Starter Kit, à matérialiser.**\n\n- [ ] Starter Kit.",
    "ROADMAP M7 status",
)
roadmap = replace_once(
    roadmap,
    "- [ ] Produire, préflighter et inspecter le PDF complet de fin du Livre V.",
    "- [x] Produire, préflighter et inspecter le PDF complet de fin du Livre V.",
    "ROADMAP Livre V PDF",
)
write(roadmap_path, roadmap)

plan_path = "plans/LIVRE-V-PLAN-MAITRE.md"
plan = read(plan_path)
plan = replace_once(plan, 'status: "active"', 'status: "complete"', "Livre V plan status")
plan = replace_once(plan, 'version: "1.26.0"', 'version: "1.27.0"', "Livre V plan version")
plan = replace_once(
    plan,
    "> **Statut :** 26 chapitres sur 26 rédigés et audités au niveau `static-review` ; clôture PDF du Livre V encore requise",
    "> **Statut :** terminé — 26 chapitres sur 26 et publication technique acceptée au niveau `static-review+pdf-inspected`",
    "Livre V plan summary",
)
old_closure = "**État de clôture :** la couverture documentaire des 26 fiches est complète ; la génération et l’inspection des formats de publication restent à exécuter séparément."
new_closure = f'''**État de clôture :** accepté au niveau `static-review+pdf-inspected`. Le PDF cumulatif contient {PDF_PAGES} pages ; l’index et les 26 fiches du Livre V occupent les pages 3 681 à 4 062. La compilation, le préflight, l’extraction textuelle, l’exclusion des QA internes et l’inspection Poppler/PDFium sont réussis. Voir le [rapport de clôture](../Livre-V/QA/CLOTURE-LIVRE-V.md) et la [preuve structurée](../Livre-V/QA/VALIDATION-PUBLICATION-LIVRE-V.yaml).

Les formats HTML/EPUB, le balisage avancé d’accessibilité, la licence globale et le Companion Pack restent hors de cette décision.'''
plan = replace_once(plan, old_closure, new_closure, "Livre V plan closure")
write(plan_path, plan)

continuity_path = "CONTINUITE-PROJET.md"
continuity = read(continuity_path)
continuity = replace_once(continuity, 'version: "4.13.0"', 'version: "4.14.0"', "continuity version")
continuity = replace_once(continuity, 'last-updated: "2026-07-30T01:18:00+02:00"', f'last-updated: "{TIMESTAMP}"', "continuity timestamp")
continuity = replace_once(continuity, "- jalon : M6 — Livre V ;", "- jalon : M7 — Companion Pack ;", "continuity milestone")
continuity = replace_once(
    continuity,
    "- clôture documentaire du Livre V : 26 fiches sur 26 ; construction, préflight et inspection du PDF complet encore requis ;",
    f"- publication technique du Livre V : acceptée au niveau `static-review+pdf-inspected` ; PDF cumulatif de {PDF_PAGES} pages, préflight réussi et inspection Poppler/PDFium achevée ;",
    "continuity Livre V closure",
)
next_section_pattern = re.compile(r"## 26\. Prochaine action\n.*?(?=## 27\. Journal)", re.S)
next_section = '''## 26. Prochaine action

M6 — Livre V est terminé au niveau `static-review+pdf-inspected`. Les 26 fiches sont rédigées et auditées ; le PDF cumulatif est construit, préflighté et inspecté. Le jalon actif est M7 — Companion Pack. Aucun Starter Kit, projet Godot, test, lancement ou artefact exécutable n’est encore matérialisé.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Companion-Pack/Starter-Kit/README.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le Pack 1 doit matérialiser un projet Godot minimal de référence avec `project.godot`, scène de bootstrap, structure canonique, profils d’environnement, scripts de validation, README, licence ou statut de redistribution et provenance. Aucune ouverture, exécution graphique ou headless, reproductibilité de clone ou réussite de test ne devra être annoncée sans exécution et preuve consultable.
'''
continuity, count = next_section_pattern.subn(next_section, continuity, count=1)
if count != 1:
    raise RuntimeError(f"continuity next action: expected one section, found {count}")
journal_anchor = "## 27. Journal\n\n"
journal_entry = f'''### {TIMESTAMP} — version 4.14.0

- clôture technique et PDF du Livre V — Encyclopédie technique et bibliothèque de référence ;
- 145 sources lecteur validées et parsables avec Pandoc ;
- deux séparateurs de la fiche 05 normalisés pour empêcher une interprétation YAML erronée ;
- dépendance Latin Modern ajoutée à la chaîne temporaire XeLaTeX ;
- PDF cumulatif final : {PDF_PAGES} pages A4, {PDF_SIZE} octets, version 1.5, non chiffré et texte extractible ;
- empreinte PDF `{PDF_SHA256}` et empreinte du texte extrait `{TEXT_SHA256}` ;
- `qpdf --check`, polices incorporées, 26 titres du Livre V et exclusion des contenus QA internes validés ;
- Livre V cartographié des pages 3 681 à 4 062 ; Companion Pack à partir de la page 4 063 ;
- 82 pages inspectées avec Poppler et 8 pages comparées avec PDFium, sans défaut visuel bloquant observé ;
- run final `{PDF_RUN_ID}`, artefact `{PDF_ARTIFACT_ID}`, digest `{PDF_ARTIFACT_DIGEST}` ;
- publication technique du Livre V acceptée au niveau `static-review+pdf-inspected` ;
- jalon actif déplacé vers M7 — Companion Pack ;
- prochaine action : `Companion-Pack/Starter-Kit/README.md`, niveau Élevée ;
- aucune licence globale, aucun PDF balisé, HTML, EPUB, Starter Kit, projet Godot exécutable, test runtime ou publication commerciale produit.

'''
continuity = replace_once(continuity, journal_anchor, journal_anchor + journal_entry, "continuity journal")
write(continuity_path, continuity)

print("Livre V PDF closure governance finalized.")
