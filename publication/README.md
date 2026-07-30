---
title: "Publications PDF, HTML et EPUB"
id: "DOC-PUBLICATION-FORMATS"
status: "candidate"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-30T21:37:00+02:00"
validation-status: "awaiting-ci"
license: "CC-BY-SA-4.0"
---

# Publications PDF, HTML et EPUB

Ce dossier définit les métadonnées et le style communs aux trois formats techniques de la collection **Guide IA GameDev**.

## Source de vérité

- `contents.txt` fixe l’ordre officiel des sources destinées au lecteur ;
- les fichiers Markdown restent l’unique source éditoriale ;
- `metadata.yaml` fournit les métadonnées générales ;
- `publication/metadata.yaml` ajoute les métadonnées propres aux exports ;
- `filters/pdf-normalize.lua` applique la même normalisation éditoriale aux trois formats.

## Sorties techniques

`tools/build_publications.py` produit dans `dist/publication/` :

- `Guide-IA-GameDev.pdf` ;
- `Guide-IA-GameDev.html` — document HTML5 autonome avec ressources incorporées ;
- `Guide-IA-GameDev.epub` — publication EPUB 3 ;
- `publication-manifest.json` — inventaire des sources et empreintes ;
- `SHA256SUMS` — empreintes des trois artefacts.

Ces fichiers sont des artefacts CI. Leur génération ne constitue ni une release GitHub, ni une publication commerciale, ni une validation d’accessibilité avancée.

## Validation attendue

- PDF : compilation XeLaTeX, `qpdf --check`, informations Poppler, texte extractible, A4 et polices incorporées ;
- HTML : document autonome, langue française, titre, table des matières, identifiants uniques et liens internes résolus ;
- EPUB : conteneur valide, licence embarquée et EPUBCheck 5.3.0 sans erreur ;
- collection : aucune ancienne mention de licence globale en attente, sources inchangées et validations documentaires transversales réussies.

## Licence

Les contenus éditoriaux des trois exports relèvent de `CC-BY-SA-4.0`. Les scripts et la feuille de style technique relèvent de `MIT`, conformément à `LICENSE.md` et à `docs/licensing/LICENSE-MATRIX.yaml`.
