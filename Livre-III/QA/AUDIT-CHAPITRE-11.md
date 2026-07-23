---
title: "Audit du Livre III — Chapitre 11 : Vêtements, armures et accessoires"
id: "DOC-L3-QA-AUDIT-CH11"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 11
last-verified: "2026-07-23T11:50:40+02:00"
audit-date: "2026-07-23T11:50:40+02:00"
audit-level: "static-review"
audited-document: "Livre-III/CHAPITRE-11-Vetements-armures-et-accessoires.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit — Chapitre 11 : Vêtements, armures et accessoires

## 1. Décision

Le chapitre est **accepté au niveau `static-review` avec réserves runtime**.

Il couvre le périmètre du plan maître sans revendiquer de vêtement, armure, accessoire, patron, skinning, simulation, collision, masque, atlas, LOD, export ou scène Godot réellement produits. Les frontières avec les bases humaines et humanoïdes des chapitres 6 et 7, le lookdev facial du chapitre 10, les objets tenus et armes du chapitre 12, le pipeline PBR du chapitre 16, les UV et le baking du chapitre 17, le rig du chapitre 19, l'animation du chapitre 20 et les règles métier du Livre II sont explicites.

## 2. Périmètre comparé au plan maître

| Exigence | Couverture | Décision |
|---|---|---|
| Layering et ordre des couches | Sections 8 et 9 | Conforme |
| Patrons, volumes et marges de mouvement | Sections 10 à 13 | Conforme |
| Skinning aux rigs de référence | Sections 14 à 16 | Conforme, sans poids exécutés |
| Simulation de tissu | Sections 18 à 21 | Conforme, limitée à Blender et à une conversion qualifiée |
| Collisions simplifiées | Sections 19 et 20 | Conforme, séparées du gameplay |
| Attaches et points de fixation | Sections 17 et 18 | Conforme |
| Masquage de géométrie | Sections 22 et 23 | Conforme, réversible et conditionnel |
| LOD, atlas et réduction des matériaux | Sections 24 à 26 | Conforme, budgets provisoires |
| Kits vestimentaires | Sections 6, 27 et 39 | Contrat documenté, kit non matérialisé |
| Règles de layering | Sections 8, 9 et 39 | Conforme |
| Profils de skinning | Sections 14 à 16 et 39 | Conforme |
| Collisions de simulation | Sections 19 à 21 et 39 | Conforme |
| Matrice de compatibilité | Sections 9, 27 et 39 | Conforme |
| Absence de clipping majeur | Sections 22, 23, 32 et 38 | Protocole documenté, tests non exécutés |
| Combinaisons autorisées identifiées | Sections 8, 9, 27 et 37 | Conforme |
| Simulation stable et coût maîtrisé | Sections 20, 21, 33 et 37 | Protocole documenté, stabilité non mesurée |
| Frontière avec le chapitre 12 | Sections 1, 4, 18, 38 et 40 | Conforme |

## 3. Livrables permanents

Les cinq livrables exigés sont matérialisés comme contrats réutilisables :

1. kits vestimentaires ;
2. règles de layering ;
3. profils de skinning ;
4. collisions de simulation ;
5. matrice de compatibilité.

La scène `WearableValidationLab` est documentée comme environnement commun de preuve. Aucun fichier Blender, texture, GLB ou scène Godot n'est annoncé comme existant.

## 4. Cohérence technique

### 4.1 Layering, morphologies et patrons

- ordre des couches séparé des conflits explicites ;
- compatibilité fermée par défaut ;
- statuts `supported`, `conditional`, `blocked`, `untested` et `not_applicable` distingués ;
- profils morphologiques limités aux bases testées ;
- patrons, panneaux, coutures, marges et directions de déformation documentés ;
- `Shrinkwrap` limité au blockout ;
- pose neutre interdite comme preuve unique.

### 4.2 Skinning, rigidité et attaches

- transfert de poids présenté comme première passe ;
- normalisation, sommets sans poids et influences excessives contrôlés ;
- textile, rembourrage, plaque et sangle peuvent employer des comportements différents ;
- demandes d'os auxiliaires présentées comme candidates ;
- attaches exprimées dans l'espace local de l'os ;
- `BoneAttachment3D`, parentage et skinning distingués ;
- objets tenus et armes exclus.

### 4.3 Simulation, collisions et clipping

- simulation Blender qualifiée comme étape de fabrication ;
- cache Blender explicitement non canonique et non présumé compatible avec Godot ;
- conversion vers maillage skinné, animation bakée, os secondaires ou forme statique documentée ;
- proxies simples distingués des collisions gameplay ;
- correction du patron et du skinning prioritaire sur le masquage ;
- masques réversibles et protégés aux ouvertures ;
- tests de régression entre combinaisons prévus.

### 4.4 Godot, LOD et performance

- GLB conservé comme conteneur d'échange ;
- scène importée séparée de la scène dérivée ;
- `MeshInstance3D`, `Skeleton3D`, `Skin` et attaches vérifiés structurellement ;
- validateur GDScript non destructif ;
- fonctions, paramètres, types, retours et opérateurs expliqués ;
- LOD géométriques, matériels, accessoires et mouvement secondaire distingués ;
- cohérence des masques pendant les transitions exigée ;
- aucune valeur CPU, GPU, VRAM, draw call ou overdraw inventée.

## 5. Revue pédagogique

Le chapitre explique :

- la différence entre couche et compatibilité ;
- la différence entre taille commerciale et profil morphologique ;
- la différence entre patron, volume et marge de mouvement ;
- la différence entre textile skinné et plaque rigide ;
- la différence entre collision de simulation et collision gameplay ;
- la différence entre cache Blender et représentation runtime ;
- la différence entre correction de clipping et masquage ;
- la différence entre variante visuelle et statistique d'objet ;
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

- lignes : 1 973 ;
- titres Markdown comptés : 52 ;
- blocs code ou données : 56 ;
- blocs significatifs retenus : 56 ;
- marqueurs `qa:code-explanation` : 56 ;
- explications structurées hors diagnostics : 36 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- corrections expliquées : 10 ;
- doublons de titres : 0 ;
- doublons de blocs : 0 ;
- doublons de paragraphes longs : 0.

## 7. Contrôles de frontières

Le chapitre ne contient pas :

- de nouvelle base humaine ou humanoïde ;
- de nouveau lookdev facial ou capillaire ;
- d'objet tenu, d'arme ou de projectile ;
- de règle d'inventaire, d'équipement ou de combat ;
- de pipeline PBR transversal ;
- de cours générique complet sur UV, retopologie ou baking ;
- de rig de production final ;
- de contrôleur d'animation ;
- de simulation runtime déclarée compatible sans preuve ;
- de mesure runtime inventée ;
- de prochaine action éditoriale ;
- de recommandation GPT dans le texte lecteur ;
- de procédure QA interne dans le chapitre lecteur.

## 8. Sources qualifiées

Les fonctions techniques sont reliées aux documentations officielles Blender et Godot. Les pages `latest` ou `stable` sont signalées lorsqu'aucune page versionnée équivalente n'est exposée. La documentation Godot confirme le triplet `MeshInstance3D`, `Skeleton3D` et `Skin`, l'import glTF 2.0 recommandé et la nécessité d'une scène dérivée pour l'intégration. Aucune capacité de simulation vestimentaire runtime n'est présumée.

## 9. Réserves

- brief du kit pilote non approuvé ;
- références, droits et provenance non qualifiés ;
- kit du Gardien non produit ;
- profils morphologiques non mesurés ;
- patrons et marges non créés ;
- blockouts non revus ;
- topologies non réalisées ;
- skinning et transfert de poids non exécutés ;
- zones rigides non testées ;
- attaches non matérialisées ;
- proxies de collision non produits ;
- simulation Blender non exécutée ;
- conversion ou baking non testés ;
- clipping et poses extrêmes non testés ;
- masques corporels non produits ;
- matériaux et atlas non créés ;
- variantes non produites ;
- LOD non produits ni mesurés ;
- matrice de compatibilité non validée ;
- export GLB non exécuté ;
- scène Godot non matérialisée ;
- validateur GDScript non exécuté ;
- performances CPU, GPU, VRAM, draw calls, skinning et overdraw non mesurées ;
- Starter Kit non matérialisé ;
- licence globale non définie ;
- PDF du Livre III non construit.

## 10. Avertissement documentaire

Un avertissement demeure : indices de couches, nombres de profils, limites d'influences, surfaces, matériaux, collisions, LOD et distances sont provisoires. Ils ne doivent pas être repris comme objectifs définitifs sans campagne réelle dans `Project Asteria`.

## 11. Conclusion

Décision : **accepté au niveau `static-review`**, sous réserve de la réussite des validateurs légers et du maintien explicite de toutes les réserves runtime.
