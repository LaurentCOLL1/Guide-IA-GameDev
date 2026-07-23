---
title: "Audit du Livre III — Chapitre 7"
id: "DOC-L3-QA-AUDIT-CH07"
status: "complete"
version: "1.0.0"
chapter-id: "DOC-L3-CH07"
chapter-version: "1.0.0"
audit-level: "static-review"
audit-date: "2026-07-23T01:49:34+02:00"
last-verified: "2026-07-23T01:49:34+02:00"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 7 — Création des humanoïdes

## 1. Porte de création

La création intervient après la fusion, la fermeture QA et le nettoyage opérationnel du chapitre 6. `CONTINUITE-PROJET.md` version `3.36.2` désigne explicitement `Livre-III/CHAPITRE-07-Creation-des-humanoides.md` comme prochaine action.

Avant rédaction, le dépôt ne contenait ni chapitre 7, ni audit, ni preuve finale, ni branche `ch07` ou `humano`, ni pull request ouverte concurrente. La branche `docs/livre-iii-ch07-creation-humanoides` a été créée depuis `main`.

Le titre, l’intention, les quatre résultats d’apprentissage, les sept contenus obligatoires, les cinq livrables, les dépendances, les parcours Solo et Studio, les trois critères de validation et la frontière ont été comparés à `plans/LIVRE-III-PLAN-MAITRE.md`.

Le texte lecteur ne contient ni procédure QA interne, ni recommandation de raisonnement, ni chemin du chapitre suivant.

## 2. Résultats documentaires

- lignes finales : **2015** ;
- titres Markdown contrôlés hors blocs : **72** ;
- blocs de code, données ou structures : **42** ;
- blocs significatifs selon le validateur : **39** ;
- marqueurs d’explication : **42** ;
- explications structurées hors section d’erreurs : **22** ;
- cas d’erreurs détaillés : **10** ;
- exemples fautifs expliqués : **10** ;
- corrections expliquées : **10** ;
- titres dupliqués : **0** ;
- blocs significatifs dupliqués : **0** ;
- paragraphes longs dupliqués : **0** ;
- instruction de prochaine étape dans le texte lecteur : **0** ;
- métadonnée de processus de raisonnement : **0**.

Les métriques CI, les identifiants d’artefacts et les empreintes finales sont consignés dans `Livre-III/QA/VALIDATION-FINALE-CHAPITRE-07.yaml`.

## 3. Complétude contre le plan maître

Le chapitre couvre :

- définition technique d’un humanoïde et distinction avec humain stylisé, animal anthropomorphe et créature non humanoïde ;
- fiche d’espèce reliée au monde, aux interactions, aux distances de caméra et aux objectifs de réutilisation ;
- registre des écarts anatomiques comparé à la base humaine du chapitre 6 ;
- classes d’impact des écarts et décision variante, module ou nouvelle base ;
- proportions, posture, centre de masse, colonne, thorax, ceintures, tête et cou ;
- membres, mains, pieds, queues, oreilles, cornes et membranes ;
- tests de silhouette primaire, secondaire et tertiaire ;
- adaptation fonctionnelle de la topologie ;
- interfaces modulaires versionnées ;
- profils de rig avec os communs, renommés, absents, supplémentaires, de contrôle et de déformation ;
- `SkeletonProfileHumanoid`, `BoneMap`, poses de repos et axes ;
- retargeting local, global et partiel ;
- poids, influences et profil quatre ou huit influences ;
- vêtements, armures, masques corporels et variantes ;
- sockets, orientations et volumes libres ;
- variations culturelles sans inférence depuis l’anatomie ;
- matériaux préparatoires et traits de surface ;
- LOD préservant les traits distinctifs ;
- budgets géométriques, squelettiques, matériels et de variantes ;
- organisation Blender, export GLB et manifeste ;
- import Godot, scène de validation et GDScript structurel ;
- batterie de poses, mouvements, équipements et mesures ;
- responsabilités de revue ;
- parcours Solo et Studio ;
- porte d’acceptation ;
- dix diagnostics avec exemples fautifs et corrections ;
- décisions retenues pour `Project Asteria`.

Les cinq livrables du plan maître sont matérialisés : bases humanoïdes, règles d’adaptation anatomique, profils de rig, matrice de compatibilité des équipements et scènes de test.

## 4. Frontières contrôlées

- le chapitre part de la base humaine du chapitre 6 sans la réécrire ;
- il ne produit pas les animaux du chapitre 8 ;
- il ne produit pas les créatures réellement non humanoïdes du chapitre 9 ;
- il prépare sans approfondir les visages, peaux, yeux, cheveux et pilosités du chapitre 10 ;
- il prépare sans fabriquer les vêtements et armures du chapitre 11 ;
- il documente les profils nécessaires au rig et à l’animation sans réaliser les chapitres 19 et 20 ;
- il ne crée aucun système de statistiques, capacités, interactions ou comportement du Livre II ;
- il ne transforme pas une anatomie en personnalité, culture, profession ou moralité ;
- il ne présente pas une compatibilité de retargeting comme universelle ;
- il ne présente aucune valeur runtime comme mesurée ;
- il ne construit aucun PDF intermédiaire.

## 5. Vérification technique

La revue du 23 juillet 2026 utilise des sources officielles :

- Godot documente `SkeletonProfile` comme profil virtuel utilisé pour le retargeting et `SkeletonProfileHumanoid` comme profil standardisé ;
- Godot indique que le profil humanoïde contient 56 os et plusieurs groupes ;
- le tutoriel de retargeting exige de traiter les noms et les poses de repos ;
- `RetargetModifier3D` distingue les conséquences des poses locales et globales lorsque les longueurs ou nombres d’os diffèrent ;
- l’import de scènes Godot propose quatre influences compatibles ou toutes les influences, jusqu’à huit, avec une réserve de compatibilité ;
- Blender documente les hiérarchies d’armature, groupes de sommets, poids symétriques et shape keys relatives ;
- glTF 2.0 transporte les skins, hiérarchies de joints et attributs `JOINTS_n` et `WEIGHTS_n`.

Les références exactes sont conservées dans la dernière section du chapitre. Les formulations propres à `Project Asteria`, notamment les budgets et statuts, sont identifiées comme décisions ou hypothèses du projet.

## 6. Explications pédagogiques

Les **42** blocs possèdent **42** marqueurs. Les **22** blocs hors erreurs utilisent une rubrique `Explication structurée du bloc` comportant au moins quatre points spécifiques.

Les dix cas d’erreurs respectent la séquence :

1. symptôme ou risque ;
2. exemple fautif ;
3. `Pourquoi cet exemple est fautif` ;
4. exemple corrigé ;
5. `Pourquoi la correction fonctionne`.

Aucune rubrique structurée ne s’intercale dans les séquences d’erreurs.

## 7. Contrôles particuliers

- chaque bloc clôturé possède un repère d’utilisation ;
- les fichiers à créer utilisent `[VSC]` et un chemin ;
- les structures de référence utilisent `[LECTURE]` ;
- les modes Solo et Studio restent en Markdown ordinaire ;
- les identifiants d’espèce, profil, module, export et mesure sont distincts ;
- les valeurs provisoires et nulles sont visibles ;
- les incompatibilités restent des statuts normaux ;
- `SkeletonProfileHumanoid` n’est pas imposé aux anatomies incompatibles ;
- les os supplémentaires restent séparés du profil humain ;
- les équipements sont qualifiés par région ;
- les sockets possèdent transformation, axes, volume et test ;
- les cultures restent séparées de l’anatomie ;
- les LOD conservent des traits obligatoires ;
- le GDScript ne prétend pas valider la qualité artistique ;
- aucune exécution Blender ou Godot n’est revendiquée.

## 8. Réserves

- fiche d’espèce réelle non matérialisée ;
- références anatomiques réelles non collectées ni qualifiées ;
- base humanoïde non modélisée ;
- écarts anatomiques non mesurés ;
- topologie et modules non produits ;
- interfaces modulaires non vérifiées ;
- rig et poses de repos non créés ;
- BoneMap et profils Godot non configurés ;
- retargeting local, global ou partiel non exécuté ;
- poids et comparaisons quatre/huit influences non mesurés ;
- vêtements, armures, masques et sockets non fabriqués ;
- variations culturelles non revues ;
- LOD non générés ;
- export GLB non produit ;
- scène Godot non matérialisée ;
- validateur GDScript non exécuté ;
- campagnes de poses, mouvement, équipement et coût non réalisées ;
- Starter Kit non matérialisé ;
- licence globale de la collection non définie ;
- PDF du Livre III non construit conformément à la politique de fin de Livre.

## 9. Décision

Le chapitre 7 du Livre III est **accepté au niveau `static-review` sous réserve de réussite des validations documentaires permanentes**. Il définit un système d’adaptation des humanoïdes conforme au plan maître, en conservant explicitement les incompatibilités anatomiques, de rig, d’animation et d’équipement.
