# Audit post-création du chapitre 17 — brouillon 0.9.0

- lignes : 2389
- titres : 65
- blocs clôturés : 69
- blocs expliqués : 68
- blocs sans explication détectée : 1
- cas d’erreurs : 16
- explications fautives : 16
- explications corrigées : 16
- sources Godot 4.7 nommées : 13
- ancres explicites : 2
- fragments internes : 2
- fragments sans ancre : 1
- auto-paraphrases détectées : 0

## Fragments sans ancre
- ch17-agent-state

## Risques techniques ciblés
- codec-placeholder-encode
- codec-placeholder-decode
- packed-stringname-conversion
- untyped-values-apply
- missing-prepare-guard
- draft-reserve-text

## Blocs sans explication
- lignes 2386-2389 (text)

## Auto-paraphrases

## Décision de l’audit

Corrections obligatoires avant passage en `1.0.0` : compléter le codec, sécuriser la préparation de sauvegarde, corriger les conversions de collections, résoudre toutes les ancres, remplacer les ports seulement annoncés par des contrats explicites, puis relancer les contrôles documentaires.
