---
title: "Audit — Companion Pack, Pack 2 : Project Templates"
id: "CP-PACK-02-AUDIT"
status: "candidate"
version: "0.1.0"
lang: "fr-FR"
last-verified: "2026-07-30T05:06:00+02:00"
audit-date: "2026-07-30T05:06:00+02:00"
audit-level: "static-review"
target: "Companion-Pack/Project-Templates/README.md"
---

# Audit du Pack 2 — Project Templates

## Décision candidate

Le pack matérialise deux profils distincts autour d’un cœur technique commun. La validation statique locale confirme la génération déterministe des projets Solo et Studio, la résolution des jetons, la création d’un module en couches et l’absence de dépendance Python tierce.

La décision finale reste suspendue à l’exécution CI avec Godot `4.7.1-stable`.

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
