---
title: "Audit du Livre III — Chapitre 9 : Création des créatures"
id: "DOC-L3-QA-AUDIT-CH09"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 9
last-verified: "2026-07-23T09:06:37+02:00"
audit-date: "2026-07-23T09:06:37+02:00"
audit-level: "static-review"
audited-document: "Livre-III/CHAPITRE-09-Creation-des-creatures.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit — Chapitre 9 : Création des créatures

## 1. Décision

Le chapitre est **accepté au niveau `static-review` avec réserves runtime**.

Il couvre le périmètre du plan maître sans revendiquer de concept final, planche anatomique, modèle, rig, collision, socket, export, scène ou mesure réellement exécutés. La frontière avec les animaux réels du chapitre 8, le lookdev détaillé du chapitre 10, le rigging du chapitre 19, l'animation du chapitre 20 et les systèmes de gameplay du Livre II est explicite.

## 2. Périmètre comparé au plan maître

| Exigence | Couverture | Décision |
|---|---|---|
| Fonction narrative et gameplay de la créature | Sections 7 et 8 | Conforme, sans valeurs métier |
| Anatomie spéculative cohérente | Sections 9 à 12 et 16 | Conforme |
| Silhouette primaire, secondaire et détails | Sections 13 et 14 | Conforme |
| Points de contact, locomotion et centre de masse | Sections 11, 12, 22 et 23 | Conforme |
| Volumes de collision, zones d'impact et sockets | Sections 19 à 21 et 30 | Conforme |
| Rig, contraintes et animations possibles | Sections 17, 18, 22 et 23 | Contrats préparatoires documentés |
| Variantes, LOD et lisibilité en combat | Sections 25, 26 et 31 | Conforme |
| Fiches de créatures | Sections 7, 8 et 38 | Conforme |
| Planches anatomiques | Sections 9 à 17 et 38 | Conforme |
| Modèles pilotes | Sections 15 à 17 et 38 | Contrat documenté, modèle non matérialisé |
| Rigs et volumes de collision | Sections 18 à 20 et 38 | Profils documentés, assets non matérialisés |
| Tests de lisibilité gameplay | Sections 22, 26, 31 et 36 | Protocole documenté, test non exécuté |
| Frontière avec le chapitre 8 | Sections 1, 4 et 39 | Conforme |
| Frontière avec le chapitre 10 | Sections 4, 24 et 39 | Conforme |
| Frontière avec le Livre II | Sections 4, 20, 21, 22 et 39 | Conforme |

## 3. Livrables permanents

Les cinq livrables exigés sont matérialisés comme contrats réutilisables :

1. fiches de créatures ;
2. planches anatomiques ;
3. modèles pilotes ;
4. rigs et volumes de collision ;
5. tests de lisibilité gameplay.

La scène `CreatureValidationLab` est documentée comme environnement commun de preuve. Aucun fichier Blender, GLB ou Godot n'est annoncé comme existant.

## 4. Cohérence technique

### 4.1 Anatomie et conception

- fonctions, formes, coûts et limites sont reliés par une matrice ;
- analogues réels limités à une question et à une portée ;
- niveaux observé, extrapolé, fantastique contraint et non résolu distingués ;
- centre de masse artistique explicitement séparé d'une masse physique ;
- appuis et stabilité examinés sans prétendre simuler la biomécanique ;
- silhouette primaire protégée avant les détails ;
- structures non résolues bloquantes.

### 4.2 Blender et rig

- unités et axes hérités du chapitre 4 ;
- blockout fonctionnel séparé de la sculpture ;
- topologie organisée autour des six membres, de la crête, du cou et de la queue ;
- profil de rig propre à la créature ;
- os de déformation séparés des contrôleurs futurs ;
- sockets exprimés dans l'espace local d'un os ;
- poses extrêmes et dérive de socket préparées ;
- aucune compatibilité animale ou humanoïde supposée.

### 4.3 Godot et collisions

- import GLB et scène dérivée ;
- `Skeleton3D`, `BoneAttachment3D`, `CollisionShape3D` et AABB qualifiés ;
- proxies simples séparés du maillage de rendu ;
- absence de valeurs de combat dans les zones de lecture ;
- validateur structurel non destructif ;
- réimport, sockets, collisions et LOD réservés à des preuves distinctes ;
- aucune collision runtime ou mesure inventée.

## 5. Revue pédagogique

Le chapitre explique :

- chaque format YAML, JSON, texte et GDScript significatif ;
- types, paramètres, valeurs par défaut, retours et opérateurs du validateur ;
- différence entre analogie, extrapolation et invention ;
- différence entre maillage, proxy et zone de lecture ;
- différence entre socket et autorité gameplay ;
- différence entre budget et mesure ;
- responsabilités Solo et Studio ;
- réserves et statuts bloquants.

Les dix diagnostics suivent la séquence imposée :

1. symptôme ;
2. exemple fautif ;
3. `Pourquoi cet exemple est fautif` ;
4. exemple corrigé ;
5. `Pourquoi la correction fonctionne`.

## 6. Métriques statiques

- lignes : 2332 ;
- titres Markdown comptés par le validateur : 66 ;
- blocs code ou données : 50 ;
- blocs significatifs retenus : 45 ;
- marqueurs `qa:code-explanation` : 50 ;
- explications structurées hors diagnostics : 30 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- corrections expliquées : 10 ;
- doublons de titres : 0 ;
- doublons de blocs : 0 ;
- doublons de paragraphes longs : 0.

## 7. Contrôles de frontières

Le chapitre ne contient pas :

- d'animal réel présenté comme créature fantastique ;
- de lookdev détaillé de peau, yeux, dents, cheveux ou pelage ;
- de rig de production final ;
- de contrôleurs IK ou outils d'animation ;
- de bibliothèque d'animations finale ;
- de règles d'intelligence artificielle ;
- de navigation ou d'évitement ;
- de dégâts, multiplicateurs, statistiques ou fenêtres actives ;
- de mesure runtime inventée ;
- de prochaine action éditoriale ;
- de recommandation GPT dans le texte lecteur ;
- de procédure QA interne dans le chapitre lecteur.

## 8. Sources qualifiées

Les fonctions techniques sont reliées aux documentations officielles Blender et Godot. Les pages `latest` ou `stable` sont signalées lorsqu'aucune page versionnée équivalente n'est exposée. Aucune source commerciale ou tutoriel tiers n'est nécessaire à la décision statique.

## 9. Réserves

- brief artistique réel non approuvé ;
- analogues et droits non qualifiés ;
- anatomie spéculative non relue par spécialité ;
- planches anatomiques non produites ;
- blockout et modèle non créés ;
- topologie et poses non testées ;
- armature, poids et contraintes non produits ;
- sockets non créés ;
- proxies de collision non créés ;
- zones de lecture non testées ;
- animations et transitions non produites ;
- matériaux détaillés laissés au chapitre 10 ;
- variantes non produites ;
- LOD non produits ;
- export GLB non exécuté ;
- scène Godot non matérialisée ;
- validateur GDScript non exécuté ;
- collisions, AABB, sockets et réimport non testés ;
- lisibilité gameplay non mesurée ;
- performances CPU, GPU et mémoire non mesurées ;
- Starter Kit non matérialisé ;
- licence globale non définie ;
- PDF du Livre III non construit.

## 10. Avertissement documentaire

Un avertissement demeure : dimensions, ratios de masse artistique, nombres d'os, budgets de triangles, slots de matériaux et scénarios de densité sont provisoires. Ils ne doivent pas être repris comme objectifs définitifs sans campagne réelle dans `Project Asteria`.

## 11. Conclusion

Décision : **accepté au niveau `static-review`**, sous réserve de la réussite des validateurs légers et du maintien explicite de toutes les réserves runtime.
