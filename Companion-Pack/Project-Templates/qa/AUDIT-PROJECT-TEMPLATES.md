---
title: "Audit — Companion Pack, Pack 2 : Project Templates"
id: "CP-PACK-02-AUDIT"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-30T05:34:00+02:00"
audit-date: "2026-07-30T05:34:00+02:00"
audit-level: "runtime-tested"
target: "Companion-Pack/Project-Templates/README.md"
---

# Audit du Pack 2 — Project Templates

## Décision

Le pack matérialise deux profils distincts autour d’un cœur technique commun. La validation statique locale confirme la génération déterministe des projets Solo et Studio, la résolution des jetons, la création d’un module en couches et l’absence de dépendance Python tierce.

Le pack est accepté au niveau `runtime-tested` pour Linux x86_64. Le run `30511425269` a validé la génération, les deux imports, les deux démarrages headless, les deux démarrages Xvfb Compatibility, les deux suites GDScript et les arbres Git propres.

## Couverture statique

- fichiers de pack, manifestes et provenance ;
- modèles communs et overlays Solo/Studio ;
- conventions de branches ;
- modèles d’issues et de pull requests ;
- ADR, responsabilités et CODEOWNERS Studio ;
- paramètres VS Code et règles de style ;
- générateur de projet ;
- générateur de module ;
- validation des chemins et des jetons ;
- génération déterministe de deux exemplaires par profil ;
- distinction explicite entre fichier de politique et réglage GitHub réellement appliqué.

## Frontières

Le pack ne prétend pas :

- activer une protection de branche ;
- créer des comptes, équipes ou permissions GitHub ;
- rendre CODEOWNERS effectif sur un dépôt cible ;
- produire un export ou une release ;
- valider Windows graphique ou Forward+ sur GPU réel ;
- décider la licence globale.

## Porte runtime

La campagne CI doit :

1. instancier les profils Solo et Studio dans des dossiers neufs ;
2. créer un module dans chaque projet ;
3. valider les sources générées ;
4. importer les deux projets avec Godot officiel ;
5. exécuter un démarrage headless et graphique virtuel borné ;
6. exécuter les tests GDScript, y compris le module généré ;
7. vérifier l’arbre Git propre après runtime ;
8. publier les journaux et manifestes comme artefact.


## Résultats runtime

- Godot : `4.7.1.stable.official.a13da4feb` ;
- archive Linux SHA-256 : `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba` ;
- profil Solo : import, bootstrap, Xvfb et tests réussis ;
- profil Studio : import, bootstrap, Xvfb et tests réussis ;
- module généré `inventory_demo` chargé et testé dans les deux profils ;
- arbres Git propres après import et tests ;
- run : `30511425269` ;
- commit qualifié : `488697292d3dd82804c80d6bbc56629b45cb6a79` ;
- artefact : `8747249256` ;
- digest : `sha256:a285b4880527d0aa36bfe1f1ed67d3e950b4668601709ce5aadb04e73bd04473`.

## Réserves maintenues

- les avertissements Xvfb relatifs à V-Sync et à l’absence de périphérique audio sur le runner ne constituent pas une revue de qualité visuelle ou audio ;
- aucune protection de branche n’est appliquée à un dépôt cible ;
- l’efficacité de CODEOWNERS n’est pas vérifiée sur un dépôt cible ;
- Windows graphique et Forward+ sur GPU réel ne sont pas exécutés ;
- aucun export, paquet de release ou licence globale n’est produit ou décidé.
