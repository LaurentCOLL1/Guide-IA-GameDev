---
title: "Fiche outil — Pandoc d’exemple"
id: "CARD-TOOL-099"
status: "validated"
version: "1.0.0"
lang: "fr-FR"
date: "2026-07-30"
card-type: "outil"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Fiche outil — Pandoc d’exemple

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à comparer et **[LECTURE]** contenu à étudier.

| Champ | Valeur |
|---|---|
| Nom | Pandoc |
| Version ou format | >= 3.0 |
| Source ou installation | paquet système ou distribution officielle |
| Licence | GPL-2.0-or-later |

## Usage retenu

Compiler les exemples Markdown du Pack vers HTML pendant la qualification.

## Limites et réserves

La compilation HTML ne prouve ni la qualité PDF ni l’accessibilité du rendu.

## Vérification

Exécuter `pandoc --version`, puis compiler un exemple avec `--standalone`.
