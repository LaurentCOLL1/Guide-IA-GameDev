---
title: "Audit du Livre III — Chapitre 12 : Objets, équipements et armes"
id: "DOC-L3-QA-AUDIT-CH12"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 12
last-verified: "2026-07-23T13:30:28+02:00"
audit-date: "2026-07-23T13:30:28+02:00"
audit-level: "static-review"
audited-document: "Livre-III/CHAPITRE-12-Objets-equipements-et-armes.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit — Chapitre 12 : Objets, équipements et armes

## 1. Décision

Le chapitre est **accepté au niveau `static-review` avec réserves runtime**.

Il couvre le périmètre du plan maître sans revendiquer d’objet, d’outil, d’arme, de pivot, de socket, de collision, de matériau, d’atlas, de LOD, d’export ou de scène Godot réellement produits. Les frontières avec les vêtements portés du chapitre 11, les kits architecturaux du chapitre 13, le pipeline PBR du chapitre 16, les UV et le baking du chapitre 17, le rig du chapitre 19, l’animation du chapitre 20, les VFX du chapitre 23 et les règles métier du Livre II sont explicites.

## 2. Périmètre comparé au plan maître

| Exigence | Couverture | Décision |
|---|---|---|
| Références dimensionnelles et ergonomie | Sections 8 à 11 | Conforme |
| Pivot, origine et orientation | Sections 12 et 13 | Conforme |
| Sockets de main, dos, ceinture ou environnement | Sections 14 à 16 | Conforme |
| Collisions de prise et d’interaction | Sections 23 et 24 | Conforme |
| Collision ou origine de projectile si nécessaire | Section 25 | Conforme comme proxy visuel, sans projectile autoritaire |
| États visuels, variantes et dégradation | Sections 27 et 28 | Conforme |
| Matériaux, LOD et atlas | Sections 22 et 29 à 30 | Conforme, budgets provisoires |
| Séparation asset, données de contenu et gameplay | Sections 4, 25, 27, 28 et 41 | Conforme |
| Bibliothèque d’objets pilotes | Sections 6, 8 et 42 | Contrat documenté, bibliothèque non matérialisée |
| Conventions de pivots et sockets | Sections 12 à 16 et 42 | Conforme |
| Collisions | Sections 23 à 25 et 42 | Profils documentés, collisions non produites |
| LOD | Sections 29, 30 et 42 | Profils documentés, LOD non produits |
| Scènes Godot d’équipement | Sections 32 à 37 et 42 | Contrat documenté, scènes non matérialisées |
| Alignement dans les animations | Sections 15, 26 et 36 | Protocole documenté, animations non exécutées |
| Collisions adaptées à l’usage | Sections 23 à 25 et 37 | Protocole documenté, tests non exécutés |
| Échelle cohérente | Sections 9 à 11 et 36 | Protocole documenté, mesures non réalisées |
| Frontière avec le chapitre 13 | Sections 4 et 43 | Conforme |

## 3. Livrables permanents

Les cinq livrables exigés sont matérialisés comme contrats réutilisables :

1. bibliothèque d’objets pilotes ;
2. conventions de pivots et sockets ;
3. collisions ;
4. LOD ;
5. scènes Godot d’équipement.

La scène `PropValidationLab` est documentée comme environnement commun de preuve. Aucun fichier Blender, texture, GLB ou scène Godot n’est annoncé comme existant.

## 4. Cohérence technique

### 4.1 Fonction, dimensions et ergonomie

- fonction observable séparée des statistiques métier ;
- dimensions croisées depuis plusieurs références ;
- incertitudes et hypothèses conservées ;
- prise, dégagement des doigts et centre de masse visuel documentés ;
- gabarits métriques distincts de la géométrie finale ;
- échelle vérifiée avec la main, le personnage et l’environnement ;
- aucune masse physique réelle inventée.

### 4.2 Origines, pivots et sockets

- origine canonique distinguée des ajustements locaux ;
- axes et orientation documentés avant export ;
- pivots de prise, rotation, pose et suspension distingués ;
- prises principale et secondaire séparées ;
- sockets de rangement et d’environnement séparés des prises ;
- point d’émission documenté par position et orientation ;
- `Marker3D` et `BoneAttachment3D` utilisés selon leur responsabilité ;
- aucun pivot n’est déplacé silencieusement après publication.

### 4.3 Collisions et interactions

- maillage de rendu séparé du volume d’interaction ;
- collision physique séparée du proxy d’impact ;
- primitives privilégiées lorsque le contrat le permet ;
- génération automatique depuis le maillage limitée au diagnostic ;
- échelle non uniforme de `CollisionShape3D` explicitement bloquée ;
- volumes de projectile limités à des repères et proxies visuels ;
- aucune logique de dégâts, portée, cadence ou munition ajoutée.

### 4.4 Godot, LOD et performance

- GLB conservé comme conteneur d’échange ;
- scène importée séparée de la scène dérivée ;
- nœuds fonctionnels ajoutés dans la scène dérivée ;
- validateur GDScript non destructif ;
- fonctions, paramètres, types, retours et opérateurs expliqués ;
- sockets nécessaires conservés selon l’usage de chaque LOD ;
- collisions et états qualifiés par représentation ;
- aucune valeur CPU, GPU, VRAM, draw call ou mémoire inventée.

## 5. Revue pédagogique

Le chapitre explique :

- la différence entre origine, pivot et socket ;
- la différence entre prise et rangement ;
- la différence entre maillage de rendu, interaction, physique et impact ;
- la différence entre objet visuel et définition métier ;
- la différence entre état visuel et durabilité autoritaire ;
- la différence entre variante esthétique et nouvelle identité d’objet ;
- la différence entre LOD distant et représentation encore équipable ;
- la différence entre scène importée et scène dérivée ;
- la différence entre budget provisoire et mesure ;
- les parcours Solo et Studio ;
- les réserves et statuts bloquants.

Les dix diagnostics suivent la séquence imposée :

1. symptôme ;
2. exemple fautif ;
3. `Pourquoi cet exemple est fautif` ;
4. exemple corrigé ;
5. `Pourquoi la correction fonctionne`.

## 6. Métriques statiques

- lignes : 2 312 ;
- titres Markdown comptés : 57 ;
- blocs code ou données : 61 ;
- blocs significatifs retenus : 61 ;
- marqueurs `qa:code-explanation` : 61 ;
- explications structurées hors diagnostics : 41 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- corrections expliquées : 10 ;
- doublons de titres : 0 ;
- doublons de blocs : 0 ;
- doublons de paragraphes longs : 0.

## 7. Contrôles de frontières

Le chapitre ne contient pas :

- de nouveau système de vêtements ou de layering ;
- de grille ou de kit architectural ;
- de règle d’inventaire, d’équipement, de durabilité ou de combat ;
- de valeur de dégâts, portée, cadence ou munition ;
- de projectile autoritaire ;
- de procédé de fabrication d’arme réelle ;
- de calcul balistique ;
- de pipeline PBR transversal ;
- de cours générique complet sur UV, retopologie ou baking ;
- de rig de production final ;
- de contrôleur d’animation ;
- de VFX d’impact final ;
- de mesure runtime inventée ;
- de prochaine action éditoriale ;
- de recommandation GPT dans le texte lecteur ;
- de procédure QA interne dans le chapitre lecteur.

## 8. Sources qualifiées

Les fonctions techniques sont reliées aux documentations officielles Blender et Godot. La documentation Godot confirme l’import glTF 2.0 recommandé, la séparation entre scène importée et scène dérivée, le rôle de `BoneAttachment3D`, `Marker3D`, `Area3D`, `CollisionShape3D` et des formes de collision. La documentation Blender qualifie les origines, transformations, objets vides et propriétés personnalisées exportables. Aucune source commerciale ou tutoriel tiers n’est nécessaire à la décision statique.

## 9. Réserves

- brief de la bibliothèque pilote non approuvé ;
- références, droits et provenance non qualifiés ;
- objets pilotes non produits ;
- dimensions et ergonomie non mesurées ;
- gabarits et blockouts non créés ;
- origines, axes et pivots non validés ;
- sockets de prise, rangement, environnement et émission non matérialisés ;
- topologies et pièces mobiles non produites ;
- matériaux et atlas non créés ;
- collisions d’interaction, physiques et d’impact non produites ;
- alignement aux mains et au squelette non testé ;
- états visuels et dégradations non produits ;
- variantes non produites ;
- LOD non produits ni mesurés ;
- export GLB non exécuté ;
- scènes Godot non matérialisées ;
- validateur GDScript non exécuté ;
- grille de poses et tests d’environnement non exécutés ;
- performances CPU, GPU, VRAM, draw calls, mémoire et collisions non mesurées ;
- Starter Kit non matérialisé ;
- licence globale non définie ;
- PDF du Livre III non construit.

## 10. Avertissement documentaire

Un avertissement demeure : dimensions, masses apparentes, surfaces, nombres de triangles, matériaux, collisions, distances, seuils et profils LOD sont provisoires. Ils ne doivent pas être repris comme objectifs définitifs sans campagne réelle dans `Project Asteria`.

## 11. Conclusion

Décision : **accepté au niveau `static-review`**, sous réserve de la réussite des validateurs légers et du maintien explicite de toutes les réserves runtime.
