---
title: "Demande de validation du Volume 0"
id: "DOC-V0-QA-REQUEST"
status: "validation"
version: "1.0.5"
---

# Demande de validation du Volume 0

Ce document déclenche la validation automatisée du Volume 0 par GitHub Actions.

## Périmètre

- contrôle structurel des sources déclarées dans `contents.txt` ;
- validation des métadonnées et identifiants, y compris l’alias historique `identifier` ;
- contrôle des liens Markdown locaux ;
- compilation complète avec Pandoc et XeLaTeX ;
- normalisation du titre global et des glyphes PDF ;
- conversion des ressources SVG ;
- conservation du journal complet de compilation ;
- inspection technique du PDF généré ;
- publication du rapport QA et du PDF comme artefacts de workflow.

Cette révision valide l’état final de M1 après mise à jour de l’index, du rapport QA et de la roadmap.
