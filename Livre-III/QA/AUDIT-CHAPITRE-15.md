---
title: "Audit du Livre III — Chapitre 15 : Végétation et biomes"
id: "DOC-L3-QA-AUDIT-CH15"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 15
last-verified: "2026-07-23T17:45:00+02:00"
audit-date: "2026-07-23T17:45:00+02:00"
audit-level: "static-review"
audited-document: "Livre-III/CHAPITRE-15-Vegetation-et-biomes.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit — Chapitre 15 : Végétation et biomes

## 1. Décision

Le chapitre est **accepté au niveau `static-review` avec réserves runtime**.

Le document définit une chaîne complète depuis le brief de biome jusqu’au benchmark de densité. Il ne revendique comme produits ni assets végétaux, ni matériaux, ni shaders, ni cartes de distribution, ni `MultiMesh`, ni scènes Godot, ni mesures.

## 2. Périmètre comparé au plan maître

| Exigence | Couverture | Décision |
|---|---|---|
| Profil visuel et écologique d’un biome | Sections 5 à 10 | Conforme comme profil artistique non autoritaire |
| Arbres, arbustes, herbes, fleurs et débris | Sections 13 à 16 | Conforme |
| Variantes de taille, saison et santé | Sections 21 et 22 | Conforme |
| Cartes et règles de distribution | Sections 28 à 31 | Conforme |
| Instancing, `MultiMesh` et regroupement | Sections 32 à 38 | Conforme comme architecture non exécutée |
| Shaders de vent et interaction locale | Sections 23 à 25 | Conforme comme exemples non compilés |
| LOD, imposteurs et benchmark de densité | Sections 26, 27 et 42 à 45 | Conforme, seuils et résultats réservés |
| Bibliothèque végétale | Sections 8 à 22 et 48 | Contrat documenté |
| Profils de biome | Sections 5, 6, 28 à 31 et 48 | Contrat documenté |
| Cartes de distribution | Sections 28 à 31 et 48 | Contrat documenté |
| Shaders de vent | Sections 23 à 25 et 48 | Contrat documenté |
| Benchmark de densité | Sections 43 à 45 et 48 | Contrat documenté |
| Diversité sans bruit visuel | Sections 5, 6, 14, 15, 21 et 49 | Porte de validation documentée |
| Coût acceptable aux densités prévues | Sections 17, 30, 37, 43 à 45 et 49 | Protocole documenté, mesures absentes |
| Transitions et distance crédibles | Sections 26, 27, 42 et 49 | Protocole documenté, tests absents |
| Frontière avec le chapitre 14 | Sections 1, 4 et 38 | Conforme |
| Frontière avec le chapitre 16 | Sections 4, 18 et 19 | Conforme |
| Frontière avec le Livre II | Sections 1, 4, 22, 25, 38 et 50 | Conforme |

## 3. Livrables permanents

Les cinq livrables du plan maître sont matérialisés comme contrats versionnés :

1. bibliothèque végétale ;
2. profils de biome ;
3. cartes de distribution ;
4. shaders de vent ;
5. benchmark de densité.

Le biome pilote `AST-VEG-BIOME-DELTA-001` reste une cible de production. Aucun fichier Blender, atlas, texture, shader compilé, GLB, `MultiMesh`, scène de biome ou capture de benchmark n’est annoncé comme existant.

## 4. Cohérence technique

### 4.1 Catalogue et sources

- les fonctions visuelles précèdent le catalogue ;
- espèce, morphotype, variante, état et instance sont séparés ;
- les références d’observation, textures, scans et contenus générés sont qualifiés séparément ;
- l’échelle est comparée aux personnages, bâtiments et cellules ;
- l’origine correspond à l’ancrage au sol ;
- les collections Blender séparent source, collision, LOD, export et prévisualisation.

### 4.2 Géométrie, feuillage et matériaux

- tronc, branches et couronne sont construits par niveaux ;
- les arbustes et strates basses possèdent des fonctions distinctes ;
- le coût géométrique est relié au nombre d’instances et à la transparence ;
- l’alpha blend généralisé est refusé comme défaut ;
- atlas et familles de matériaux restent préparatoires ;
- le pipeline PBR transversal demeure au chapitre 16.

### 4.3 Vent, interaction et états

- le vent suit une hiérarchie tronc-branches-rameaux-feuilles ;
- une phase par instance évite la synchronisation rigide ;
- l’interaction locale de masse reste visuelle ;
- les objets uniques peuvent recevoir une scène dédiée ;
- saison et santé sont des états visuels préparés ;
- la sélection autoritaire et la simulation restent dans le Livre II.

### 4.4 Distribution, instancing et culling

- cartes, canaux, repères et bordures sont versionnés ;
- exclusions et contraintes précèdent la randomisation ;
- les graines incluent identifiants et version d’algorithme ;
- Geometry Nodes sert à la prévisualisation sans constituer une preuve runtime ;
- `MultiMesh` est réservé aux grands groupes identiques ;
- les lots sont découpés par cellule, espèce, LOD et famille matérielle ;
- la boîte englobante prend en compte instances et vent ;
- le cycle de vie suit l’autorité des cellules du chapitre 14.

### 4.5 Collisions, navigation et performance

- seules les plantes réellement bloquantes reçoivent des collisions simples ;
- herbes, fleurs et cartes de feuillage restent sans collision ;
- dégagements physiques et visuels sont séparés ;
- ombres, overdraw, LOD, HLOD et imposteurs sont mesurés ;
- le benchmark conserve matériel, versions, scène, parcours et profils ;
- aucune valeur CPU, GPU, mémoire, distance ou densité n’est inventée.

## 5. Revue pédagogique

Le chapitre explique notamment :

- la différence entre espèce, morphotype, variante et instance ;
- la différence entre prototype et lot de rendu ;
- la différence entre prévisualisation Blender et instancing Godot ;
- la différence entre scène individuelle et `MultiMeshInstance3D` ;
- la limite de culling d’un `MultiMesh` ;
- la différence entre géométrie, cartes alpha et imposteurs ;
- la différence entre état visuel et simulation écologique ;
- la différence entre collision physique et exclusion de placement ;
- les parcours Solo et Studio ;
- les portes de preuve et réserves runtime.

Les dix diagnostics respectent la séquence imposée : symptôme, exemple fautif, explication directe, exemple corrigé et explication de la correction.

## 6. Métriques statiques

- lignes : 2236 ;
- titres Markdown : 64 ;
- blocs code ou données significatifs : 66 ;
- marqueurs `qa:code-explanation` : 66 ;
- explications structurées hors diagnostics : 46 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- corrections expliquées : 10 ;
- doublons de titres : 0 ;
- doublons de blocs : 0 ;
- doublons de paragraphes longs : 0.

## 7. Contrôles de frontières

Le chapitre ne contient pas :

- de nouvelle infrastructure de terrain, tuile ou streaming général ;
- de pipeline PBR complet ;
- de cours générique complet sur UV ou baking ;
- de système général d’animation ;
- de météo ou VFX final ;
- de système écologique dynamique ;
- de croissance, reproduction, mortalité ou régénération autoritaire ;
- de règle gameplay de récolte, dégâts ou ressources ;
- de mesure runtime inventée ;
- de prochaine action éditoriale ;
- de recommandation GPT dans le texte lecteur ;
- de procédure QA interne dans le chapitre lecteur.

## 8. Sources qualifiées

Le chapitre relie ses mécanismes aux documentations officielles de Godot pour `MultiMesh`, `MultiMeshInstance3D`, `GeometryInstance3D`, `MeshInstance3D` et les plages de visibilité, ainsi qu’au manuel Blender pour `Instance on Points` et à la spécification glTF 2.0.

La documentation stable de Godot indique qu’un `MultiMesh` peut dessiner un très grand nombre d’objets efficacement, mais que les instances ne sont pas cullées individuellement. Le chapitre en déduit un découpage par lots spatiaux, à confirmer par benchmark.

## 9. Réserves

- brief du biome pilote non approuvé par une revue de production ;
- références, droits et provenance non qualifiés ;
- catalogue et fiches d’espèces non approuvés ;
- dimensions, silhouettes et pivots non mesurés ;
- arbres, arbustes, herbes, fleurs, couvre-sols et débris non produits ;
- sources Blender et collections d’export non créées ;
- feuillage, atlas et matériaux non produits ;
- shaders de vent non compilés ;
- interaction locale non exécutée ;
- variantes de saison et santé non produites ;
- LOD et imposteurs non produits ;
- cartes de distribution non produites ;
- contraintes de pente, altitude, humidité et exclusions non testées ;
- placement déterministe non exécuté ;
- prévisualisation Geometry Nodes non créée ;
- ressources `MultiMesh` non générées ;
- tailles de lots et boîtes englobantes non mesurées ;
- cycle de chargement/retrait avec les cellules non testé ;
- collisions et navigation non produites ni validées ;
- ombres et overdraw non mesurés ;
- scènes Godot et GLB non matérialisés ;
- benchmark de densité non exécuté ;
- valeurs CPU, GPU, VRAM, mémoire, draw calls, distances et densités non mesurées ;
- Starter Kit non matérialisé ;
- licence globale non définie ;
- PDF du Livre III non construit.

## 10. Avertissement documentaire

Un avertissement demeure : tailles, densités, résolutions, amplitudes de vent, fréquences, distances, tailles de lots, budgets, niveaux LOD et profils d’imposteurs sont provisoires. Ils ne doivent pas être repris comme objectifs définitifs sans campagne réelle dans `Project Asteria`.

## 11. Conclusion

Décision : **accepté au niveau `static-review`**, sous réserve de la réussite des validateurs légers et du maintien explicite de toutes les réserves runtime.
