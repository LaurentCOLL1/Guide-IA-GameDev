---
title: "Audit post-création — Livre III, chapitre 27"
id: "DOC-L3-QA-AUDIT-CH27"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L3-CH27"
chapter-version: "1.0.0"
audit-date: "2026-07-24T23:50:00+02:00"
last-verified: "2026-07-24T23:50:00+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 27

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation du jeu de visèmes, du rig facial, des profils linguistiques, des timings, des animations, des scènes Godot, des campagnes multi-distance, des mesures runtime, des droits et du PDF de fin de Livre.

Aucun blendshape, alignement, TextGrid, animation faciale, profil de langue, scène Godot, capture, benchmark, consentement ou PDF n’est revendiqué comme produit ou exécuté.

## 2. Périmètre comparé au plan maître

Le chapitre couvre graphèmes, phonèmes, allophones, visèmes, différences linguistiques, jeu minimal de formes, mâchoire, lèvres, langue, yeux, sourcils, timings manuels ou alignés, TextGrid, mapping, coarticulation, transitions, regard, clignements, gestes, langues, profils de qualité et LOD facial.

Les livrables prévus sont préparés comme contrats : jeu de visèmes, profil de rig, profils linguistiques, pipeline de timing, animation pilote et campagne de tests en gros plan, à distance et en foule. Leur matérialisation reste en réserve.

## 3. Frontières contrôlées

- le chapitre 10 conserve l’anatomie, les formes et les dépendances du visage ;
- le chapitre 19 conserve le rig, le skinning et les contrôleurs ;
- le chapitre 20 conserve la bibliothèque d’animation corporelle ;
- le chapitre 26 conserve voix, montage, mix, provenance et consentements vocaux ;
- le chapitre 27 conserve mapping linguistique, timings, courbes et performance faciale ;
- le chapitre 28 conservera presets d’import, scripts post-import et réimportation ;
- le Livre II conserve les décisions narratives et gameplay ;
- aucune piste, fin d’animation, analyse audio ou sortie automatique n’applique une règle métier.

## 4. Contrôles pédagogiques

- procédure progressive depuis la voix approuvée jusqu’à la porte d’acceptation ;
- distinction graphème, phonème, allophone, visème et silence ;
- jeu minimal de visèmes, blendshapes, mâchoire, correctifs et pose neutre expliqués ;
- annotation manuelle, alignement forcé, TextGrid, lexique et validation des timings documentés ;
- coarticulation, enveloppes, mélange, interpolation, lissage et latence séparés ;
- regard, clignements, saccades, tête, gestes, émotion et asymétrie encadrés ;
- intégration Godot par pistes, `AnimationPlayer`, `AnimationTree` et driver runtime préparée ;
- profils de langue, qualité, gros plan, gameplay et foule documentés ;
- fonctions, paramètres, types, retours et effets de bord explicités ;
- chaque bloc significatif possède un repère d’utilisation et une explication structurée ;
- dix diagnostics suivent l’ordre symptôme, exemple fautif, raison, exemple corrigé, raison ;
- modes Solo et Studio documentés en Markdown ordinaire ;
- sources officielles Godot, Blender, Praat et Montreal Forced Aligner fournies sous forme de liens cliquables.

## 5. Contrôles documentaires

- lignes : 2345 ;
- titres : 76 ;
- blocs code ou données : 82 ;
- marqueurs d’explication : 82 ;
- explications structurées hors diagnostics : 62 ;
- diagnostics détaillés : 10 ;
- titres dupliqués : 0 ;
- blocs significatifs dupliqués : 0 ;
- paragraphes longs dupliqués : 0 ;
- synthèse opérationnelle `Project Asteria` présente ;
- références techniques officielles sous forme de liens Markdown cliquables ;
- absence de prochaine action et de recommandation GPT dans le texte lecteur ;
- PDF non produit.

## 6. Exactitude technique

La revue statique s’appuie sur la documentation officielle Godot 4.7 pour les pistes de blend shapes, `AnimationPlayer`, `AnimationTree`, `Animation` et `Mesh`, ainsi que sur le manuel Blender pour les Shape Keys et Drivers.

Praat est cité pour la structure et les formats TextGrid. Montreal Forced Aligner est présenté comme outil d’alignement forcé produisant un brouillon à revoir, jamais comme autorité automatique de publication.

Les formulations distinguent prononciation, phone, visème, pose, courbe, profil linguistique, LOD, coût et autorité. Les nombres de millisecondes, poids, distances, fréquences et budgets restent explicitement candidats ou en attente de mesure.

## 7. Réserves ouvertes

- pilote `AST-FACE-PILOT-RELAY-DIALOGUE-001` non matérialisé ;
- aucun jeu de visèmes, blendshape, correctif ou profil de rig créé ;
- aucune transcription, lexique, annotation ou sortie TextGrid produite ;
- aucun alignement forcé exécuté ou revu ;
- aucune courbe, animation ou scène Godot créée ;
- aucun profil linguistique ou de qualité qualifié ;
- aucun test gros plan, distance, foule ou multi-voix exécuté ;
- CPU, mémoire, allocations, fréquence de mise à jour et nombre de visages non mesurés ;
- droits vidéo, capture faciale, scan et entraînement non qualifiés ;
- Starter Kit non matérialisé ;
- licence globale de la collection non définie ;
- PDF du Livre III différé à la fin du Livre.

## 8. Conclusion

Le chapitre satisfait le plan maître et peut entrer dans la validation légère sans PDF. La preuve finale restera `pending` jusqu’à la réussite des workflows permanents sur la branche matérialisée.
