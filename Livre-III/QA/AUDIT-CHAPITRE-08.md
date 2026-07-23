---
title: "Audit du Livre III — Chapitre 8 : Création des animaux"
id: "DOC-L3-QA-AUDIT-CH08"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 8
audit-date: "2026-07-23T04:29:27+02:00"
audit-level: "static-review"
audited-document: "Livre-III/CHAPITRE-08-Creation-des-animaux.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit — Chapitre 8 : Création des animaux

## 1. Décision

Le chapitre est **accepté au niveau `static-review` avec réserves runtime**.

Il couvre le périmètre du plan maître sans revendiquer de modèles, rigs, cycles, surfaces, exports, scènes ou mesures réellement exécutés. La frontière avec les créatures fantastiques du chapitre 9 et avec les comportements animaux du Livre II est explicite.

## 2. Périmètre comparé au plan maître

| Exigence | Couverture | Décision |
|---|---|---|
| Quadrupèdes, oiseaux, poissons, reptiles et morphologies particulières | Sections 7 à 10 | Conforme |
| Répartition des masses, articulations et contacts | Sections 9 à 13 | Conforme |
| Marche, course, vol, nage et repos | Sections 16 à 20 | Conforme |
| Pelage, plumes, écailles et rendu | Sections 21 à 23 | Conforme |
| Variantes pertinentes | Section 24 | Conforme |
| LOD, instancing et densité de groupe | Sections 25 et 26 | Conforme |
| Scènes de validation de locomotion et coût | Sections 28 à 31 | Conforme |
| Bases animales pilotes | Sections 7, 12 et 37 | Contrat documenté, asset non matérialisé |
| Fiches anatomiques | Sections 8 à 11 | Conforme |
| Rigs de base | Sections 14 et 15 | Profil documenté, rig non matérialisé |
| Cycles de locomotion | Sections 16 à 20 | Manifestes documentés, cycles non matérialisés |
| Budgets par distance et densité | Sections 25, 26 et 31 | Budgets provisoires documentés |
| Frontière avec le Livre II | Sections 4, 20 et 38 | Conforme |
| Frontière avec le chapitre 9 | Sections 4 et 38 | Conforme |

## 3. Livrables permanents

Les cinq livrables exigés sont matérialisés comme contrats réutilisables :

1. bases animales pilotes ;
2. fiches anatomiques ;
3. profils de rig de base ;
4. cycles de locomotion pilotes ;
5. budgets par distance et densité.

La scène `AnimalValidationLab` est documentée comme environnement commun de preuve. Aucun fichier Blender, GLB ou Godot n’est annoncé comme existant.

## 4. Cohérence technique

### 4.1 Blender

- unités et axes hérités du chapitre 4 ;
- topologie organisée autour des volumes et zones de déformation ;
- poids automatiques présentés comme point de départ ;
- profils de rig propres aux familles animales ;
- courbes de cheveux séparées de la représentation livrée ;
- plumes, écailles et pelage traités selon silhouette, distance et coût ;
- sources procédurales exclues de l’export tant que leur conversion n’est pas testée.

### 4.2 Godot

- import GLB et scène dérivée ;
- `Skeleton3D`, `AnimationPlayer` et `AnimationTree` qualifiés ;
- LOD automatique distingué des LOD manuels skinnés ;
- plages de visibilité documentées ;
- `MultiMesh` limité aux représentations compatibles ;
- AABB, éclairage, blend shapes et culling cités comme limites à mesurer ;
- validateur structurel non destructif ;
- performance comparée à une scène témoin.

### 4.3 Mouvement

- contacts ou phases versionnés par cycle ;
- aucune séquence de pas présentée comme universelle ;
- racine en place et mouvement auteur distingués ;
- transitions séparées des boucles ;
- glissement, pénétration, boucle et dérive réservés à la mesure ;
- locomotion de gameplay laissée au Livre II.

## 5. Revue pédagogique

Le chapitre explique :

- chaque format YAML, JSON, texte et GDScript significatif ;
- les entrées, retours, invariants et limites du validateur ;
- la différence entre source, export et représentation moteur ;
- la différence entre budget et mesure ;
- la différence entre scène proche, LOD skinné et groupe distant ;
- les responsabilités Solo et Studio ;
- les réserves et statuts bloquants.

Les dix diagnostics suivent la séquence imposée :

1. symptôme ;
2. exemple fautif ;
3. `Pourquoi cet exemple est fautif` ;
4. correction ;
5. `Pourquoi la correction fonctionne`.

## 6. Métriques statiques

- lignes : 1928 ;
- titres Markdown de niveau 2 à 6 : 66 ;
- blocs de code ou de données : 43 ;
- blocs significatifs retenus : 39 ;
- marqueurs `qa:code-explanation` : 43 ;
- explications structurées hors diagnostics : 23 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- corrections expliquées : 10 ;
- doublons de titres : 0 ;
- doublons de blocs : 0 ;
- doublons de paragraphes longs : 0.

## 7. Contrôles de frontières

Le chapitre ne contient pas :

- de système d’IA animale ;
- de simulation écologique ;
- de navigation ou d’évitement ;
- de règles de combat ou de statistiques ;
- de créature fantastique ;
- de rig final ou d’outil d’animation complet ;
- de comportement de groupe autoritaire ;
- de mesures runtime inventées ;
- de prochaine action éditoriale ;
- de recommandation GPT dans le texte lecteur ;
- de procédure QA interne dans le chapitre lecteur.

## 8. Sources qualifiées

Les fonctions techniques sont reliées à des documentations officielles Blender et Godot. Les pages `latest` ou `dev` sont signalées lorsqu’aucune page versionnée équivalente n’est disponible. Aucune source commerciale ou tutoriel tiers n’est nécessaire à la décision statique.

## 9. Réserves

- références zoologiques réelles non collectées ;
- provenance et droits non qualifiés ;
- bases animales non modélisées ;
- topologies non testées ;
- armatures et poids non produits ;
- cycles et transitions non animés ;
- pelage, plumes et écailles non matérialisés ;
- conversion des courbes Blender non testée ;
- exports GLB non produits ;
- imports Godot non exécutés ;
- AABB, LOD, culling et éclairage non mesurés ;
- représentation `MultiMesh` non éprouvée ;
- glissement et contacts non mesurés ;
- performances CPU, GPU et mémoire non mesurées ;
- variantes non produites ;
- Starter Kit non matérialisé ;
- licence globale non définie ;
- PDF du Livre III non construit.

## 10. Avertissement documentaire

Un avertissement demeure : les budgets de triangles, d’os, de matériaux, de textures, de densité et de distance sont provisoires. Ils ne doivent pas être repris comme objectifs définitifs sans campagne dans `Project Asteria`.

## 11. Conclusion

Décision : **accepté au niveau `static-review`**, sous réserve de la réussite des validateurs légers et du maintien explicite de toutes les réserves runtime.
