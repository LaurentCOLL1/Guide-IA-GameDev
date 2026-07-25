---
title: "Audit post-création — Livre III, chapitre 28"
id: "DOC-L3-QA-AUDIT-CH28"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
chapter-id: "DOC-L3-CH28"
chapter-version: "1.0.0"
audit-date: "2026-07-25T06:23:53+02:00"
last-verified: "2026-07-25T06:23:53+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit post-création — Chapitre 28

## 1. Décision

Le chapitre est accepté au niveau `static-review` avec réserves de matérialisation des livraisons, profils, sidecars, scènes importées, scènes d’intégration, remaps, scripts post-import, campagnes de réimportation, mesures runtime et PDF de fin de Livre.

Aucun GLB, glTF, `.blend`, FBX, OBJ, texture, audio, preset, scène Godot, matériau externe, animation, collision, socket, import headless, capture, benchmark ou PDF n’est revendiqué comme produit ou exécuté.

## 2. Périmètre comparé au plan maître

Le chapitre couvre les formats d’échange, les presets par famille, les scènes importées, héritées et composées, les matériaux externes ou remappés, les textures, l’audio, les animations, squelettes, blendshapes, collisions, sockets, LOD, métadonnées, scripts post-import et réimportation.

Les livrables prévus sont préparés comme contrats : matrice format-usage, profils d’import, scènes d’intégration, script post-import, manifeste d’import, diff et checklist de réimportation. Leur matérialisation reste en réserve.

## 3. Frontières contrôlées

- les chapitres 4 à 27 conservent les sources, conventions et livraisons artistiques ;
- le chapitre 28 conserve les profils, remaps, scènes d’intégration et contrats de réimportation ;
- le chapitre 29 conservera l’acceptation technique et artistique finale ;
- le chapitre 30 conservera l’orchestration en lots et la CI artistique ;
- le Livre II conserve les outils génériques et toute autorité métier ;
- aucun importeur, suffixe, socket, animation ou métadonnée n’applique une règle gameplay.

## 4. Contrôles pédagogiques

- séparation source, livraison, sidecar `.import`, cache `.godot` et scène d’intégration ;
- matrice GLB, glTF séparé, `.blend`, FBX, OBJ et DAE ;
- profils pour assets statiques, personnages, animations, textures et audio ;
- héritage et composition expliqués avec protection des personnalisations ;
- externalisation et remapping des matériaux documentés ;
- squelettes, skins, blendshapes, LOD, collisions et sockets encadrés ;
- `EditorScenePostImport`, idempotence, limites de chemin et absence de réimportation récursive expliqués ;
- diff, baseline, campagnes propres, profils de plateforme et budgets préparés ;
- fonctions, paramètres, types, retours et effets de bord explicités ;
- chaque bloc significatif possède un repère d’utilisation et une explication structurée ;
- dix diagnostics suivent l’ordre symptôme, exemple fautif, raison, exemple corrigé, raison ;
- modes Solo et Studio documentés en Markdown ordinaire ;
- sources officielles Godot, Khronos et Blender fournies sous forme de liens cliquables.

## 5. Contrôles documentaires

- lignes : 2237 ;
- titres : 71 ;
- blocs code ou données : 79 ;
- marqueurs d’explication : 79 ;
- explications structurées hors diagnostics : 59 ;
- diagnostics détaillés : 10 ;
- titres dupliqués : 0 ;
- blocs significatifs dupliqués : 0 ;
- paragraphes longs dupliqués : 0 ;
- synthèse opérationnelle `Project Asteria` présente ;
- références techniques officielles sous forme de liens Markdown cliquables ;
- absence de prochaine action et de recommandation GPT dans le texte lecteur ;
- PDF non produit.

## 6. Exactitude technique

La revue statique s’appuie sur la documentation Godot 4.7 pour le processus d’import, les scènes 3D, les formats disponibles, les configurations, les suffixes, `ResourceImporterScene`, `EditorScenePostImport`, `EditorImportPlugin`, les images, l’audio et l’organisation du projet.

La documentation officielle confirme la distinction entre fichiers `<asset>.import` à versionner et cache `.godot/imported` à régénérer. glTF 2.0 reste le format 3D recommandé ; l’import direct `.blend` ajoute une conversion Blender vers glTF et une dépendance d’outil.

Les formulations distinguent configuration, cache, ressource importée, scène héritée, composition, ressource externe, remap, post-import et preuve runtime. Les durées, tailles, tolérances et budgets restent explicitement candidats ou en attente de mesure.

## 7. Réserves ouvertes

- pilote `AST-IMPORT-PILOT-SCOUT-RELAY-001` non matérialisé ;
- aucune livraison ni manifeste réel produit ;
- aucun profil ou sidecar `.import` créé ;
- aucune scène importée, héritée ou d’intégration créée ;
- aucun matériau externe, remap, texture ou audio importé ;
- aucun squelette, skin, blendshape, animation, collision, socket ou LOD contrôlé ;
- aucun script post-import exécuté ;
- aucun import propre, réimportation ou diff exécuté ;
- aucune capture ou revue artistique produite ;
- durées d’import, cache, mémoire, chargement et coûts runtime non mesurés ;
- droits et dépendances réels non qualifiés ;
- Starter Kit non matérialisé ;
- licence globale de la collection non définie ;
- PDF du Livre III différé à la fin du Livre.

## 8. Conclusion

Le chapitre satisfait le plan maître et peut entrer dans la validation légère sans PDF. La preuve finale restera `pending` jusqu’à la réussite des workflows permanents sur la branche documentaire.
