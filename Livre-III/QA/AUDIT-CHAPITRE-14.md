---
title: "Audit du Livre III — Chapitre 14 : Terrains, paysages et mondes ouverts"
id: "DOC-L3-QA-AUDIT-CH14"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 14
last-verified: "2026-07-23T16:43:43+02:00"
audit-date: "2026-07-23T16:43:43+02:00"
audit-level: "static-review"
audited-document: "Livre-III/CHAPITRE-14-Terrains-paysages-et-mondes-ouverts.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit — Chapitre 14 : Terrains, paysages et mondes ouverts

## 1. Décision

Le chapitre est **accepté au niveau `static-review` avec réserves runtime**.

Le texte couvre le plan maître, les interfaces avec les chapitres 13, 15, 16, 17 et 28, les frontières avec le Livre II, les contrats de données, les scènes Godot, le chargement en arrière-plan et les campagnes de mesure. Aucun terrain, heightmap, tuile, route, rivière, lac, matériau, collision, navmesh, scène, LOD, HLOD, GLB ou résultat runtime n’est revendiqué comme produit.

## 2. Périmètre comparé au plan maître

| Exigence | Couverture | Décision |
|---|---|---|
| Heightmaps, sculpt et érosion contrôlée | Sections 14 à 18 | Conforme |
| Échelle du monde et découpage spatial | Sections 9 à 13 | Conforme |
| Routes, rivières et raccords aux bâtiments | Sections 21 à 25 | Conforme |
| Tuiles, streaming et voisinage | Sections 19, 20 et 32 à 42 | Conforme |
| Matériaux de terrain et mélange de couches | Sections 26 et 27 | Conforme comme contrat préparatoire |
| Eau, collisions et navigation | Sections 23 à 31 | Conforme |
| Benchmarks de parcours, mémoire et ruptures | Sections 52 à 55 | Conforme comme protocole non exécuté |
| Terrain pilote | Sections 7, 16 à 28 et 59 | Cible documentée, asset non produit |
| Découpage spatial | Sections 9 à 13 et 59 | Conforme |
| Profils de streaming | Sections 34 à 42 et 59 | Conforme |
| Matériaux de terrain | Sections 26, 27 et 59 | Identifiants et masques documentés, matériaux non produits |
| Scène de benchmark | Sections 52 à 55 et 59 | Contrat documenté, scène non matérialisée |
| Traversée sans rupture visuelle majeure | Sections 19, 20, 43 à 46 et 55 | Protocole documenté, traversée non exécutée |
| Streaming et mémoire dans les budgets | Sections 35 à 42 et 52 à 54 | Protocole documenté, budgets non mesurés |
| Collisions et navigation cohérentes | Sections 28 à 31 et 55 | Protocole documenté, tests non exécutés |
| Frontière avec le chapitre 13 | Sections 1, 4, 22 et 60 | Conforme |
| Frontière avec le chapitre 15 | Sections 4, 24, 26 et 60 | Conforme |
| Frontière avec le chapitre 16 | Sections 4, 26, 27 et 60 | Conforme |
| Frontière avec la simulation écologique du Livre II | Sections 1, 4, 24, 42 et 60 | Conforme |

## 3. Livrables permanents

Les cinq livrables du plan maître sont matérialisés comme contrats versionnés :

1. terrain pilote ;
2. découpage spatial ;
3. profils de streaming ;
4. matériaux de terrain ;
5. scène de benchmark.

La région pilote `AST-WORLD-REGION-DELTA-001` reste une cible de production. Aucun fichier Blender, EXR, HDR, texture, maillage, GLB, scène Godot ou rapport runtime n’est annoncé comme existant.

## 4. Cohérence technique

### 4.1 Échelle, coordonnées et partition

- le mètre reste l’unité commune aux personnages, bâtiments et terrain ;
- les grandes coordonnées ne sont pas activées sans preuve de précision et de coût ;
- origine, axes et coordonnées logiques sont documentés ;
- région, secteur, cellule, tuile et sous-tuile possèdent des rôles distincts ;
- la cellule est l’unité de streaming de référence ;
- les identifiants stables ne dépendent pas du chemin ou du nom affiché ;
- sources, exports, dérivés et preuves restent séparés.

### 4.2 Relief et continuité

- une heightmap est limitée à une hauteur par position horizontale ;
- grottes, ponts, arches et surplombs exigent des maillages séparés ;
- les sources 16 ou 32 bits sont privilégiées pour éviter la quantification visible ;
- étendue, résolution et pas horizontal sont reliés ;
- le sculpt progresse du macro vers le méso puis le micro ;
- l’érosion est expérimentale, masquée, traçable et réversible ;
- les tuiles partagent une autorité de bordure ;
- les marges de travail ne deviennent pas des chevauchements runtime.

### 4.3 Routes, eau et architecture

- les routes sont des corridors géométriques avant d’être des masques matériels ;
- les pads terrain-bâtiment consomment le contrat architectural sans le recopier ;
- les rivières respectent bassin versant, pente et exutoire ;
- les plans d’eau possèdent un niveau et une ligne de rive continus ;
- eau visuelle, collision, navigation et gameplay sont séparés ;
- les zones humides ne deviennent pas une simulation écologique.

### 4.4 Collision et navigation

- `HeightMapShape3D` est réservé aux surfaces à hauteur unique ;
- ponts, caves et surplombs possèdent des collisions dédiées ;
- les dimensions de `map_data`, `map_width` et `map_depth` sont documentées ;
- collision et rendu ne partagent pas automatiquement la même densité ;
- chaque cellule possède une région de navigation identifiable ;
- la superposition de navmeshes n’est pas considérée comme une connexion ;
- les tests de frontière sont bidirectionnels et attendent la synchronisation.

### 4.5 Streaming et performance

- les états `UNLOADED`, `REQUESTED`, `LOADING`, `READY`, `ACTIVE`, `RELEASING` et `FAILED` sont explicités ;
- `ResourceLoader.load_threaded_request()` est séparé du sondage et de l’instanciation ;
- `load_threaded_get()` n’est appelé qu’après le statut chargé ;
- le préchargement dépend du voisinage, de la vitesse et des temps mesurés ;
- l’hystérésis empêche les oscillations ;
- les épingles possèdent des propriétaires et des compteurs ;
- retrait, sauvegarde et état métier sont séparés ;
- LOD, HLOD, horizon et occlusion sont soumis à mesure ;
- les scènes ouvertes ne supposent pas un bénéfice automatique de l’occlusion ;
- temps de chargement, mémoire et pics de frame sont corrélés aux événements.

## 5. Revue pédagogique

Le chapitre explique notamment :

- la différence entre région, secteur, cellule, tuile et sous-tuile ;
- la différence entre heightmap maître et aperçu ;
- la différence entre domaine de travail et domaine publié ;
- la différence entre route visuelle et corridor praticable ;
- la différence entre eau visuelle et règles de nage ;
- la différence entre ressource prête et cellule active ;
- la différence entre préchargement, activation, épinglage et éviction ;
- la différence entre LOD de tuile et HLOD de secteur ;
- la différence entre contenu statique et état persistant ;
- les parcours Solo et Studio ;
- les statuts bloquants et réserves de preuve.

Les dix diagnostics suivent la séquence obligatoire : symptôme, exemple fautif, explication immédiate, exemple corrigé et explication de la correction.

## 6. Métriques statiques

- lignes : 2806 ;
- titres Markdown comptés : 74 ;
- blocs code ou données : 78 ;
- blocs significatifs retenus : 78 ;
- marqueurs `qa:code-explanation` : 78 ;
- explications structurées hors diagnostics : 58 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- corrections expliquées : 10 ;
- doublons de titres : 0 ;
- doublons de blocs : 0 ;
- doublons de paragraphes longs : 0.

## 7. Contrôles de frontières

Le chapitre ne contient pas :

- de nouvelle bibliothèque de bâtiments ;
- d’espèces, catalogues ou distributions végétales ;
- de simulation écologique ou hydrologique autoritaire ;
- de règle de nage, bateau, dégâts ou température ;
- de pipeline PBR transversal ;
- de cours complet sur UV, retopologie ou baking ;
- de VFX météorologique ou de destruction final ;
- d’importeur global de monde ;
- de mesure runtime inventée ;
- de prochaine action éditoriale ;
- de recommandation GPT dans le texte lecteur ;
- de procédure QA interne dans le chapitre lecteur.

## 8. Sources qualifiées

Le chapitre s’appuie sur les documentations officielles Godot 4.7 pour les grandes coordonnées, le chargement en arrière-plan, `ResourceLoader`, `HeightMapShape3D`, `NavigationRegion3D`, `GeometryInstance3D`, les plages de visibilité, le LOD et l’occlusion. Il s’appuie sur le manuel Blender pour le modificateur Displace, le sculpt et l’export glTF 2.0.

Les choix de dimensions, de découpage, de précision, de distances et de mémoire restent à qualifier dans `Project Asteria`.

## 9. Réserves

- brief de région non approuvé par une revue de production ;
- parcours, repères et lignes de vue non testés ;
- échelle, origine et stratégie de coordonnées non mesurées ;
- partition région-secteur-cellule-tuile non validée ;
- identifiants et manifestes non instanciés ;
- heightmaps haute précision non produites ;
- résolution, étendue et pas horizontal non qualifiés ;
- blockout et sculpt Blender non créés ;
- expériences d’érosion non exécutées ;
- bordures de tuiles non comparées ;
- routes et sections non produites ;
- pads architecturaux non raccordés ;
- rivière, lac, littoral et eau visuelle non produits ;
- matériaux et masques non produits ;
- collisions de terrain et géométries spéciales non produites ;
- navigation et raccords bidirectionnels non testés ;
- scènes de cellules et manifestes non matérialisés ;
- contrôleur GDScript non exécuté ;
- préchargement, hystérésis, épingles et retrait non testés ;
- intégration avec sauvegarde et autorités du Livre II non exécutée ;
- LOD et HLOD non produits ;
- horizon, brouillard et occlusion non qualifiés ;
- GLB non exportés ;
- scène de benchmark non créée ;
- temps froids et chauds non mesurés ;
- mémoire, pics de frame et nombre de cellules actives non mesurés ;
- matrice de frontières non exécutée ;
- Starter Kit non matérialisé ;
- licence globale non définie ;
- PDF du Livre III non construit.

## 10. Avertissement documentaire

Un avertissement demeure : résolutions, altitudes, pas d’échantillonnage, tailles de cellules, distances de préchargement, durées, budgets mémoire, erreurs géométriques et seuils LOD/HLOD sont provisoires. Ils ne doivent pas être repris comme objectifs définitifs sans campagne réelle sur les plateformes de référence.

## 11. Conclusion

Décision : **accepté au niveau `static-review`**, sous réserve de la réussite des validateurs légers et du maintien explicite de toutes les réserves runtime.
