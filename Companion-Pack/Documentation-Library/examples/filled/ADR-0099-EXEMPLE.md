---
title: "Séparer patrons et documents propriétaires"
id: "ADR-0099"
status: "validated"
version: "1.0.0"
date: "2026-07-30"
decision-status: "accepted"
lang: "fr-FR"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# ADR-0099 — Séparer patrons et documents propriétaires

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à comparer et **[LECTURE]** contenu à étudier.

## Contexte

Le Pack doit aider à créer des documents sans recopier les chapitres du guide.

## Options étudiées

1. copier des chapitres complets ;
2. fournir des patrons abstraits ;
3. ne fournir aucun exemple.

## Décision

Fournir des patrons abstraits accompagnés d’exemples fictifs et remplis.

## Conséquences

La source normative reste dans le Volume 0. Les exemples du Pack restent courts, remplaçables et sans décision propriétaire.

## Validation et révision

Le validateur refuse les placeholders non résolus, vérifie les identifiants et compare les exemples régénérés.
