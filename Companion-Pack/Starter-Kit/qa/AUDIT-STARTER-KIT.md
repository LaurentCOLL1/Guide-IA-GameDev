---
title: "Audit — Companion Pack, Starter Kit"
id: "CP-QA-PACK-01-AUDIT"
status: "in-progress"
version: "0.1.0"
lang: "fr-FR"
last-verified: "2026-07-30T03:39:00+02:00"
audit-date: "2026-07-30T03:39:00+02:00"
audit-level: "static-review"
target: "Companion-Pack/Starter-Kit"
---

# Audit du Starter Kit

## Périmètre

L’audit couvre le projet Godot minimal, les profils Solo et Studio, les scripts de validation, la provenance, les dépendances et le statut de redistribution.

## Contrôles statiques préparés

- présence des fichiers obligatoires ;
- cohérence de `project.godot` et de la scène principale ;
- contrat `BootstrapReport` ;
- profil Solo sans infrastructure distribuée obligatoire ;
- profil Studio sans réécriture du domaine ;
- absence d’addon, binaire, modèle, secret et donnée personnelle ;
- exclusion des caches Godot et des états runtime ;
- validateur Python sans dépendance tierce ;
- test GDScript autonome et borné.

## Exécutions encore attendues

- téléchargement officiel de Godot `4.7.1-stable` pour Linux x86_64 ;
- enregistrement de l’empreinte du binaire téléchargé ;
- import headless ;
- démarrage headless borné ;
- test GDScript ;
- exécution de l’enveloppe PowerShell ;
- validation documentaire générale du dépôt.

## Réserves

Windows, Forward+ graphique, export, clone neuf indépendant, restauration et publication ne sont pas validés par la campagne Linux headless. La licence globale reste indécise.

## Décision provisoire

Le lot reste candidat jusqu’à obtention et enregistrement d’une preuve CI consultable.
