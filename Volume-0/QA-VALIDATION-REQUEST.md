---
title: "Demande de validation du Volume 0"
id: "DOC-V0-QA-REQUEST"
status: "validation"
version: "1.0.0"
---

# Demande de validation du Volume 0

Ce document déclenche la validation automatisée du Volume 0 par GitHub Actions.

## Périmètre

- contrôle structurel des sources déclarées dans `contents.txt` ;
- validation des métadonnées et identifiants ;
- contrôle des liens Markdown locaux ;
- compilation complète avec Pandoc et XeLaTeX ;
- inspection technique du PDF généré ;
- publication du rapport QA et du PDF comme artefacts de workflow.

Ce fichier pourra être supprimé ou archivé après clôture de la validation.
