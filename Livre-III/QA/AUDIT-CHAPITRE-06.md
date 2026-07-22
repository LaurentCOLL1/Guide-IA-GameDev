---
title: "Audit du Livre III — Chapitre 6"
id: "DOC-L3-QA-AUDIT-CH06"
status: "complete"
version: "1.0.0"
chapter-id: "DOC-L3-CH06"
chapter-version: "1.0.0"
audit-level: "static-review"
audit-date: "2026-07-23T00:42:11+02:00"
last-verified: "2026-07-23T00:42:11+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 6 — Création des humains

## 1. Porte de création

La création intervient après la fusion, la clôture QA et le nettoyage opérationnel du chapitre 5. `CONTINUITE-PROJET.md` version `3.35.1` désignait explicitement le chemin `Livre-III/CHAPITRE-06-Creation-des-humains.md` et recommandait un niveau élevé.

Avant rédaction, le dépôt ne contenait ni chapitre 6 du Livre III, ni audit, ni preuve finale, ni branche `ch06` ou `humain`, ni pull request ouverte concurrente. La branche `docs/livre-iii-ch06-creation-humains` a donc été créée depuis `main` sans écraser de travail existant.

Le chemin, l’intention, les quatre résultats d’apprentissage, les sept contenus obligatoires, les cinq livrables, les parcours Solo et Studio, les trois critères de validation et la frontière ont été comparés à `plans/LIVRE-III-PLAN-MAITRE.md`.

Le texte lecteur ne contient ni recommandation de raisonnement, ni protocole QA interne, ni chemin du chapitre suivant.

## 2. Résultats documentaires

- lignes finales : **1 755** ;
- titres Markdown contrôlés hors blocs : **68** ;
- sections principales numérotées : **44** ;
- blocs de code, données ou structures : **34** ;
- marqueurs d’explication : **34**, dont **14** explications structurées hors erreurs ;
- cas d’erreurs détaillés : **10** ;
- exemples fautifs expliqués : **10** ;
- corrections expliquées : **10** ;
- métadonnée de processus de raisonnement : **0** ;
- instruction de prochaine étape dans le texte lecteur : **0**.

Les métriques de doublons et de blocs significatifs seront fermées par les validations documentaires permanentes avant la preuve finale.

## 3. Complétude contre le plan maître

Le chapitre couvre :

- références anatomiques reliées à des questions de production et à leur provenance ;
- mesures métriques, tolérances et repères de proportions ;
- A-pose détendue comme pose documentaire de construction ;
- base neutre par grands volumes ;
- distinction entre symétrie de construction et asymétrie documentée ;
- topologie générale et flux de déformation ;
- épaules, omoplates, coudes, avant-bras, bassin, hanches, genoux, jambes, mains et pieds ;
- séparation corps, tête, mains et pieds ;
- contrat d’interface modulaire avec nombre et ordre des sommets ;
- variantes de stature, épaules, bassin, membres, muscle et volume adipeux ;
- séparation explicite entre morphologie et données de gameplay ;
- variations adultes et réserves pour les cas nécessitant un traitement spécialisé ;
- shape keys limitées aux topologies compatibles ;
- préparation UV et matériaux sans lookdev facial détaillé ;
- politique de topologie, poses et critères d’acceptation ;
- budgets provisoires de triangles, surfaces, textures et influences ;
- profils LOD0 à LOD4 et règles de mesure ;
- distinction entre LOD importés et LOD générés par Godot ;
- préparation du contrat de rig sans produire le rig ;
- export GLB de validation ;
- configuration d’import Godot ;
- scène Godot de poses, distances, éclairages et performances ;
- script GDScript de contrôle structurel ;
- manifeste de poses ;
- protocole de mesure sans résultat inventé ;
- provenance et identifiants ;
- arborescence Solo et Studio ;
- porte d’acceptation ;
- dix erreurs fréquentes avec contre-exemple et correction ;
- checklist complète ;
- synthèse opérationnelle pour `Project Asteria`.

Les cinq livrables du plan maître sont matérialisés sous forme de contrats et procédures : base humaine de référence, variantes morphologiques, guide de proportions, budgets et profils LOD, scène Godot de validation.

## 4. Frontières contrôlées

- le chapitre produit un contrat d’asset visuel, pas un personnage de gameplay ;
- il ne redéfinit pas `CharacterDefinition`, l’état runtime, la sauvegarde ou les contrôleurs du Livre II ;
- il ne crée pas les humanoïdes du chapitre 7 ;
- il ne crée pas les animaux ou créatures des chapitres 8 et 9 ;
- il ne finalise pas le visage, la peau, les yeux, les dents, les cheveux ou la pilosité du chapitre 10 ;
- il ne crée pas les vêtements, armures, accessoires ou simulations du chapitre 11 ;
- il ne produit pas le rig, le skinning ou les contraintes du chapitre 19 ;
- il ne produit pas les animations ou le retargeting de production du chapitre 20 ;
- il ne crée pas d’interface de personnalisation runtime ;
- il ne présente aucune proportion comme norme de valeur, de santé ou d’identité ;
- il ne déduit aucune statistique de gameplay depuis une morphologie ;
- il ne revendique aucun asset, export, scène, mesure ou test runtime réellement matérialisé ;
- il ne construit aucun PDF intermédiaire.

## 5. Vérification technique

La revue du 23 juillet 2026 a utilisé les références officielles suivantes :

- Blender Manual `5.0` pour les data-blocks, modificateurs, groupes de sommets, shape keys et armatures ;
- documentation Godot stable pour l’import avancé des scènes 3D, les LOD, les shadow meshes et les influences de skin ;
- classe `ImporterMesh` pour les surfaces, blend shapes et LOD produits pendant l’import ;
- classes `MeshInstance3D` et `Skeleton3D` pour le lien entre maillage, peau, squelette, pose et rest pose ;
- `SkeletonProfileHumanoid` et le guide de retargeting pour les profils d’os, rest poses, axes et limites de l’auto-mapping ;
- spécification glTF `2.0.1` du Khronos Group pour maillages, skins et morph targets.

Les formulations évitent de promettre qu’un LOD automatique, un `BoneMap`, une correction de silhouette ou une importation sans message d’erreur garantit la qualité des déformations.

## 6. Explications pédagogiques

Les **14** blocs hors erreurs possèdent **14** marqueurs structurés et les vingt exemples fautifs/corrigés possèdent leurs marqueurs directs `<!-- qa:code-explanation -->`. Les explications couvrent selon leur nature : rôle, champs, entrées, types, valeurs, invariants, effets de bord, limites et résultat attendu.

Les dix cas d’erreurs respectent la séquence directe :

1. symptôme ;
2. exemple fautif ;
3. `Pourquoi cet exemple est fautif` ;
4. exemple corrigé ;
5. `Pourquoi la correction fonctionne`.

Aucune rubrique `Explication structurée du bloc` ne s’intercale dans les séquences d’erreurs.

## 7. Contrôles particuliers

- chaque fichier à créer utilise `[VSC]` ou `[APP]` avec son chemin ;
- chaque structure non exécutable utilise `[LECTURE]` ;
- les sections Solo et Studio restent en Markdown ordinaire ;
- les budgets sont marqués `provisional` ;
- les mesures absentes restent `null` ou `not_executed` ;
- les interfaces modulaires possèdent nombre, ordre et révision ;
- le contrat de rig reste explicitement en attente du chapitre 19 ;
- les animations restent explicitement en attente du chapitre 20 ;
- les variantes morphologiques n’ajoutent aucune capacité de gameplay ;
- la scène Godot vérifie uniquement un contrat structurel et une hauteur visuelle ;
- le script ne modifie pas l’asset ;
- la mesure AABB est décrite comme une approximation de validation ;
- les LOD sont contrôlés en pose et selon la couverture écran ;
- les sources, exports et livraisons restent séparés ;
- aucune valeur runtime n’est inventée.

## 8. Réserves

- source Blender réelle non matérialisée ;
- base humaine réelle non modélisée ;
- références anatomiques réelles non collectées ni qualifiées ;
- variantes morphologiques réelles non produites ;
- interfaces modulaires non testées ;
- UV et matériaux non créés ;
- LOD réels non générés ;
- armature et skinning non produits ;
- poses de validation non exécutées ;
- export GLB non produit ;
- scène Godot non matérialisée ;
- script GDScript non exécuté ;
- hauteurs, triangles, surfaces, textures et mémoire non mesurés ;
- seuils de LOD non mesurés dans plusieurs résolutions et champs de vision ;
- comparaison quatre/huit influences non exécutée ;
- revue anatomique, artistique, rigging, animation et performance non exécutée ;
- Starter Kit non matérialisé ;
- licence globale de la collection non définie ;
- PDF du Livre III non construit conformément à la politique de fin de Livre.

## 9. Décision

Le chapitre 6 du Livre III est **accepté au niveau `static-review` sous réserve de réussite des validations documentaires permanentes**. Il définit une base humaine modulaire, des contrats de proportions, topologie, variantes, LOD et validation Godot conformes au plan maître, sans transformer les budgets en mesures ni les modèles documentaires en assets exécutés.
