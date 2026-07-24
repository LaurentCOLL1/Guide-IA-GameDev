---
title: "Audit du Livre III — Chapitre 20 : Animation procédurale et animation par keyframes"
id: "DOC-L3-QA-AUDIT-CH20"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 20
last-verified: "2026-07-24T05:10:00+02:00"
audit-date: "2026-07-24T05:10:00+02:00"
audit-level: "static-review"
audited-document: "Livre-III/CHAPITRE-20-Animation-procedurale-et-animation-par-keyframes.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit — Chapitre 20 : Animation procédurale et animation par keyframes

## 1. Décision

Le chapitre est **accepté au niveau `static-review` avec réserves de production et runtime**.

Il documente une chaîne complète depuis le rig validé jusqu’aux Actions Blender, cycles, courbes, root motion, événements, couches, blend spaces, machine à états, corrections procédurales et scène de validation Godot. Aucune animation, bibliothèque, GLB, scène, capture ou mesure runtime n’est présentée comme produite.

## 2. Couverture du plan maître

| Exigence | Couverture | Décision |
|---|---|---|
| Principes de pose, timing, spacing et arcs | Sections 13 à 29 | Conforme |
| Cycles de locomotion et variations | Sections 30 à 38 | Conforme |
| Courbes, tangentes et nettoyage | Sections 23 à 29 | Conforme |
| Root motion et vitesse gameplay | Sections 36 à 38 et 49 | Conforme comme contrat |
| Événements, contacts et fenêtres d’action | Sections 35, 39 et 40 | Conforme |
| Blend trees, couches additives et masques | Sections 41 à 48 | Conforme |
| IK, ajustements procéduraux et tests Godot | Sections 50 à 58 | Conforme |
| Cycles de base | Sections 30 à 34 | Contrats documentés, fichiers absents |
| Bibliothèque d’animations | Sections 6 à 10 et 48 | Structure documentée, bibliothèque absente |
| Blend tree pilote | Sections 41 à 49 et 54 | Structure documentée, ressource absente |
| Profils d’export | Sections 6 à 10 et 48 | Contrats documentés, GLB absent |
| Scène Godot animée | Sections 54 à 58 | Structure documentée, scène absente |
| Frontière avec le chapitre 19 | Sections 1, 4, 5 et 6 | Conforme |
| Frontière avec le chapitre 21 | Sections 4, 7, 29, 50 et 65 | Conforme |
| Frontière avec le chapitre 28 | Sections 4, 7, 48, 54 et 58 | Conforme |

## 3. Cohérence technique

- la source Blender, le GLB d’échange et les bibliothèques Godot restent séparés ;
- poses, timing, spacing, arcs, silhouettes et équilibre sont traités avant le graphe runtime ;
- Dope Sheet, Action Editor, Graph Editor, interpolation et poignées possèdent des responsabilités distinctes ;
- idle, marche, course, démarrages, arrêts, demi-tours et interactions disposent de contrats de phase ;
- les contacts de pieds sont corrigés dans la source avant toute IK terrain ;
- root motion, in-place et vitesse gameplay sont documentés sans transférer l’autorité au graphe ;
- les événements visuels sont filtrés et ne mutent pas directement les systèmes métier ;
- couches additives, masques, blend spaces, synchronisation, machines à états et OneShot sont encadrés ;
- regard, visée, placement des pieds et ajustement de portée sont bornés et désactivables ;
- le validateur Godot contrôle la structure sans juger la qualité artistique.

## 4. Revue pédagogique

Les 81 blocs significatifs possèdent chacun un marqueur d’explication. Les 61 blocs hors diagnostics disposent d’au moins quatre rubriques structurées. Les dix diagnostics respectent la séquence symptôme, exemple fautif, explication directe, exemple corrigé et justification.

## 5. Métriques statiques

- lignes : 2452 ;
- titres Markdown : 76 ;
- blocs code ou données significatifs : 81 ;
- marqueurs `qa:code-explanation` : 81 ;
- explications structurées hors diagnostics : 61 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- corrections expliquées : 10 ;
- doublons de titres : 0 ;
- doublons de blocs : 0 ;
- doublons de paragraphes longs : 0.

## 6. Réserves

- pilote non matérialisé ni approuvé en production ;
- Actions, cycles, transitions, courbes et poses non créés dans Blender ;
- contacts, arcs, timing, spacing et root motion non inspectés ;
- export GLB, manifeste et bibliothèques Godot absents ;
- `AnimationPlayer`, `AnimationTree`, blend spaces et machine à états non exécutés ;
- événements, pistes de méthode et fenêtres non testés ;
- couches additives, masques et OneShot non validés ;
- regard, visée, IK de pieds et warping non mesurés ;
- coût CPU, GPU, mémoire et nombre de personnages non mesurés ;
- provenance et droits du pilote non qualifiés ;
- Starter Kit non matérialisé ;
- licence globale non définie ;
- PDF du Livre III non construit.

## 7. Avertissement documentaire

Les FPS, durées, vitesses, amplitudes, facteurs temporels, angles, fondus, tolérances de glissement et budgets restent des valeurs candidates. Ils ne doivent pas devenir des valeurs de production sans Actions réelles, export réel, scène Godot réelle et tests sur les plateformes de référence.

## 8. Conclusion

Décision : **accepté au niveau `static-review`**, sous réserve de la réussite des validateurs légers et du maintien explicite de toutes les réserves de production et runtime.
