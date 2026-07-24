---
title: "Audit post-création — Livre III, chapitre 21"
id: "DOC-L3-QA-AUDIT-CH21"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L3-CH21"
chapter-version: "1.0.0"
audit-date: "2026-07-24T13:38:11+02:00"
last-verified: "2026-07-24T13:38:11+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 21

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation, de droits privés, de capture, de retargeting, d’import Godot, de mesures et de PDF de fin de Livre.

Aucune session, donnée personnelle, animation, scène, GLB, bibliothèque, capture ou mesure runtime n’est revendiquée.

## 2. Périmètre comparé au plan maître

Le chapitre couvre les types de capture et leurs limites, provenance et consentement, trajectoires et contacts, mapping et poses de référence, proportions différentes, corrections des mains, pieds et centre de masse, direction artistique et intégration en bibliothèque.

Les livrables prévus sont documentés : session ou clip sourcé, profils de mapping, animations nettoyées, rapport de corrections et matrice multi-rigs. Leur matérialisation reste en réserve.

## 3. Frontières contrôlées

- le chapitre 19 conserve l’autorité sur le rig, le skinning, les axes, le roll et la rest pose ;
- le chapitre 20 conserve l’autorité sur le keyframing, les principes d’animation, root motion, événements et graphes ;
- le chapitre 22 conserve l’autorité sur les cinématiques, caméras et la mise en scène ;
- le chapitre 28 conserve l’intégration globale des assets ;
- aucune mutation gameplay n’est confiée aux pistes d’animation.

## 4. Contrôles pédagogiques

- procédure progressive depuis le choix de capture jusqu’à la porte d’acceptation ;
- fonctions, paramètres, types, opérateurs, retours et effets explicités dans les exemples Python et GDScript ;
- chaque bloc significatif possède un repère d’utilisation et un marqueur d’explication ;
- dix diagnostics suivent l’ordre symptôme, exemple fautif, raison, exemple corrigé, raison ;
- modes Solo et Studio, provenance, sécurité, automatisation et reprises documentés ;
- valeurs non exécutées marquées comme candidates ou en attente de mesure.

## 5. Contrôles documentaires

- lignes : 2850 ;
- titres : 86 ;
- blocs code ou données : 94 ;
- marqueurs d’explication : 94 ;
- explications structurées hors diagnostics : 74 ;
- diagnostics détaillés : 10 ;
- synthèse opérationnelle `Project Asteria` présente ;
- liens locaux limités à la convention des contextes ;
- absence de prochaine action et de recommandation GPT dans le texte lecteur ;
- PDF non produit.

## 6. Exactitude technique

La revue statique s’appuie sur la documentation officielle Godot relative au retargeting de squelettes 3D, à `SkeletonProfile`, `SkeletonProfileHumanoid`, `BoneMap` et `RetargetModifier3D`, ainsi que sur la documentation Blender relative aux poses d’armatures et contraintes.

Les formulations distinguent auto-mapping et approbation, pose de référence et rest pose, translation globale et mouvement local, retargeting hors ligne et variante runtime.

## 7. Réserves ouvertes

- méthode et matériel de capture non sélectionnés ;
- performeur, consentement et contrat réels absents du dépôt ;
- session, calibration, prises et clips non matérialisés ;
- seuils de filtrage, interpolation et réduction non mesurés ;
- contacts, glissements, collisions et équilibre non inspectés ;
- profils de mapping et poses de référence non créés dans les outils ;
- retargeting Blender et Godot non exécuté ;
- trois morphologies pilotes non matérialisées ou testées ;
- GLB, `BoneMap`, `AnimationLibrary` et scène Godot non produits ;
- CPU, mémoire, taille et temps de chargement non mesurés ;
- Starter Kit non matérialisé ;
- licence globale de la collection non définie ;
- PDF du Livre III différé à la fin du Livre.

## 8. Conclusion

Le chapitre satisfait le plan maître et peut entrer dans la validation légère sans PDF. La preuve finale sera fermée uniquement par le workflow dédié après réussite de tous les contrôles.
