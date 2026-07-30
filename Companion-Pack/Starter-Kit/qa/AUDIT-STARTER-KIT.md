---
title: "Audit — Companion Pack, Starter Kit"
id: "CP-QA-PACK-01-AUDIT"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-30T04:19:00+02:00"
audit-date: "2026-07-30T04:19:00+02:00"
audit-level: "runtime-tested"
target: "Companion-Pack/Starter-Kit"
---

# Audit du Starter Kit

## Décision

Le Starter Kit est accepté en version `1.0.0` au niveau `runtime-tested` pour le périmètre Linux x86_64 de la campagne CI. Le projet s’importe, démarre en headless, démarre sous affichage virtuel Xvfb avec le moteur Compatibility, exécute ses tests GDScript et se reproduit depuis un clone Git neuf.

## Preuves exécutées

- validateur Python sans paquet tiers : réussi ;
- enveloppe PowerShell : réussie ;
- Godot `4.7.1.stable.official.a13da4feb` : version vérifiée ;
- archive Godot SHA-256 `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba` ;
- import Linux headless : réussi ;
- démarrage headless borné : réussi ;
- démarrage graphique virtuel Xvfb avec Compatibility : réussi ;
- `BootstrapReport` valide et identifiant `CP-SK-BOOTSTRAP-001` observé ;
- tests GDScript : `STARTER_KIT_TESTS: PASS` ;
- clone Git neuf : validation statique, import et tests réussis ;
- arbre Git : propre après import, grâce aux UID versionnés et aux caches ignorés.

## Traçabilité

- workflow : `Validate Starter Kit` ;
- run : `30508086899` ;
- commit : `f310701c9ad41f0ca9a75a66a80fb75b089def03` ;
- artefact : `8746081670` ;
- digest : `sha256:5429fcc7001d4a28d7475908d8660e859b4aafd86b4febd42629b66e5310e2ed`.

## Réserves

- Windows graphique n’a pas été exécuté ;
- Forward+ sur GPU réel n’a pas été exécuté ;
- le lancement Xvfb utilise Compatibility et ne constitue pas une validation visuelle ;
- aucun preset d’export, paquet ou test d’installation n’est produit ;
- aucune restauration ou migration n’est exercée ;
- la licence globale reste indécise et bloque la redistribution autonome.
