---
title: "Audit du Livre III — Chapitre 13 : Architecture, bâtiments et kits modulaires"
id: "DOC-L3-QA-AUDIT-CH13"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 13
last-verified: "2026-07-23T14:35:47+02:00"
audit-date: "2026-07-23T14:35:47+02:00"
audit-level: "static-review"
audited-document: "Livre-III/CHAPITRE-13-Architecture-batiments-et-kits-modulaires.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit — Chapitre 13 : Architecture, bâtiments et kits modulaires

## 1. Décision

Le chapitre est **accepté au niveau `static-review` avec réserves runtime**.

Le chapitre original a été récupéré depuis le paquet de transport avec son empreinte SHA-256 attendue. Le conteneur temporaire présentait une corruption après le chapitre ; l’audit est donc reconstruit à partir du chapitre vérifié, du plan maître et du protocole QA. Aucun module, bâtiment, matériau, collision, navigation, occluder, LOD, HLOD, GLB, `MeshLibrary`, scène Godot ou résultat runtime n’est revendiqué comme produit.

## 2. Périmètre comparé au plan maître

| Exigence | Couverture | Décision |
|---|---|---|
| Grille métrique et dimensions humaines | Sections 9 à 11 | Conforme |
| Catégories de modules et règles d’assemblage | Sections 12 à 14 | Conforme |
| Coins, jonctions, ouvertures et transitions | Sections 19 à 23 | Conforme |
| Intérieurs, façades et variantes | Sections 24 et 25 | Conforme |
| Pivots, snapping et tolérances | Sections 15 à 17 | Conforme |
| Collisions, navigation et occlusion | Sections 28 à 30 | Conforme comme contrats non matérialisés |
| LOD, matériaux partagés et rupture de répétition | Sections 25, 26 et 37 | Conforme, budgets provisoires |
| Kit modulaire | Sections 7, 12 à 27 et 48 | Contrat documenté, kit non produit |
| Grille métrique | Sections 10, 11 et 48 | Conforme |
| Règles d’assemblage | Sections 14, 15, 41 et 48 | Conforme |
| Scènes de test | Sections 38 à 44 et 48 | Contrats documentés, scènes non matérialisées |
| Budgets et LOD | Sections 37, 44 et 48 | Profils documentés, mesures absentes |
| Trois bâtiments différents | Sections 7, 18, 41 et 46 | Porte de preuve documentée, assemblages non exécutés |
| Collisions et navigation cohérentes | Sections 28, 29, 42 et 46 | Protocole documenté, tests non exécutés |
| Répétition visuelle maîtrisée | Sections 25, 26, 43 et 46 | Protocole documenté, captures absentes |
| Frontière avec le chapitre 14 | Sections 4 et 49 | Conforme |
| Frontière avec la construction runtime | Sections 1, 4, 31 et 49 | Conforme |

## 3. Livrables permanents

Les cinq livrables du plan maître sont matérialisés comme contrats réutilisables :

1. kit modulaire ;
2. grille métrique ;
3. règles d’assemblage ;
4. scènes de test ;
5. budgets et LOD.

Le kit pilote `AST-ARCH-KIT-WAYSTATION-001` et ses trois bâtiments de preuve restent des cibles de production. Aucun fichier Blender, texture, GLB, `MeshLibrary` ou scène Godot n’est annoncé comme existant.

## 4. Cohérence technique

### 4.1 Métriques et assemblage

- usages et plans précèdent les façades détaillées ;
- grille principale, sous-grille, travées et dimensions humaines sont séparées ;
- modules et connecteurs possèdent des identifiants stables ;
- tolérances, joints, chevauchements et fuites de lumière sont contrôlés ;
- origines et pivots ne sont pas déplacés silencieusement après publication ;
- trois bâtiments doivent démontrer la réutilisation avant la finition.

### 4.2 Familles architecturales

- murs, ouvertures et linteaux forment une famille compatible ;
- coins, jonctions et transitions ne reposent pas sur des superpositions arbitraires ;
- sols, plafonds et ouvertures verticales partagent les mêmes métriques ;
- escaliers, paliers et garde-corps sont vérifiés contre les personnages ;
- toitures, rives et changements de pente disposent de pièces de raccord ;
- intérieurs et façades restent deux vues du même contrat.

### 4.3 Collisions, navigation et occlusion

- maillage de rendu, collision, source de navigation et occluder sont séparés ;
- les collisions simples sont privilégiées lorsque le contrat le permet ;
- les raccords entre régions de navigation sont explicitement testés ;
- la superposition de navmeshes n’est jamais considérée comme une connexion ;
- les occluders restent plus simples que la géométrie détaillée ;
- la destruction est limitée à des états, joints et proxies visuels sans autorité gameplay.

### 4.4 Godot, LOD et performance

- GLB reste le conteneur d’échange ;
- scène importée et scène dérivée sont séparées ;
- scènes modulaires, `GridMap` et approche hybride sont comparés ;
- `MeshLibrary` conserve des identités stables ;
- LOD de module et HLOD de bâtiment restent distincts ;
- les intérieurs ne disparaissent pas d’une représentation encore visitable ;
- le validateur GDScript est non destructif ;
- aucune distance, valeur CPU, GPU, VRAM, draw call ou mémoire n’est inventée.

## 5. Revue pédagogique

Le chapitre explique notamment :

- la différence entre module, variante, connecteur, pivot, cellule et bâtiment ;
- la différence entre grille principale et sous-incrément ;
- la différence entre joint contrôlé et chevauchement correctif ;
- la différence entre rendu, collision, navigation et occlusion ;
- la différence entre scène modulaire, `GridMap` et approche hybride ;
- la différence entre LOD de module et HLOD de bâtiment ;
- la différence entre préparation visuelle de destruction et destruction autoritaire ;
- les parcours Solo et Studio ;
- les statuts bloquants et réserves de preuve.

Les dix diagnostics suivent la séquence imposée : symptôme, exemple fautif, explication directe, exemple corrigé et explication de la correction.

## 6. Métriques statiques

- lignes : 2 381 ;
- titres Markdown comptés : 63 ;
- blocs code ou données : 69 ;
- blocs significatifs retenus : 69 ;
- marqueurs `qa:code-explanation` : 69 ;
- explications structurées hors diagnostics : 49 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- corrections expliquées : 10 ;
- doublons de titres : 0 ;
- doublons de blocs : 0 ;
- doublons de paragraphes longs : 0.

## 7. Contrôles de frontières

Le chapitre ne contient pas :

- de nouveau système d’objets individuels ;
- de terrain, route, rivière, tuile de monde ou système de streaming ;
- de règle runtime de construction, chantier, coût, propriété ou permission ;
- de destruction autoritaire, de dégâts ou de réparation ;
- de pipeline PBR transversal ;
- de cours générique complet sur UV, retopologie ou baking ;
- de système d’animation ou de VFX final ;
- de mesure runtime inventée ;
- de prochaine action éditoriale ;
- de recommandation GPT dans le texte lecteur ;
- de procédure QA interne dans le chapitre lecteur.

## 8. Sources qualifiées

Le chapitre relie les mécanismes techniques aux documentations officielles Blender et Godot. Les choix portent notamment sur transformations et origines, export glTF 2.0, scènes importées et dérivées, `GridMap`, `MeshLibrary`, collisions 3D, navigation et occlusion. Les valeurs de production restent à mesurer dans `Project Asteria`.

## 9. Réserves

- brief du kit pilote non approuvé par une revue de production ;
- références, droits et provenance non qualifiés ;
- modules et trois bâtiments de preuve non produits ;
- grille, travées, sous-incréments et tolérances non mesurés ;
- catalogue, connecteurs et matrice d’assemblage non validés ;
- blockouts Blender non créés ;
- familles de murs, ouvertures, coins, transitions, sols, escaliers et toitures non produites ;
- intérieurs, façades, variantes, trim sheets et atlas non produits ;
- origines, pivots et snapping non validés ;
- collisions architecturales non produites ;
- sources et raccords de navigation non produits ;
- occluders non produits ni testés ;
- états visuels de destruction non produits ;
- GLB non exportés ;
- scènes Godot, `GridMap` et `MeshLibrary` non matérialisés ;
- validateur GDScript non exécuté ;
- matrice d’assemblage et tests de caméra non exécutés ;
- LOD et HLOD non produits ni mesurés ;
- performances CPU, GPU, VRAM, draw calls, mémoire, navigation et occlusion non mesurées ;
- Starter Kit non matérialisé ;
- licence globale non définie ;
- PDF du Livre III non construit.

## 10. Avertissement documentaire

Un avertissement demeure : dimensions, cellules, tolérances, nombres de modules, matériaux, collisions, distances, budgets et profils LOD/HLOD sont provisoires. Ils ne doivent pas être repris comme objectifs définitifs sans campagne réelle dans `Project Asteria`.

## 11. Conclusion

Décision : **accepté au niveau `static-review`**, sous réserve de la réussite des validateurs légers et du maintien explicite de toutes les réserves runtime.
