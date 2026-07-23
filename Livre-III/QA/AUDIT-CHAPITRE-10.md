---
title: "Audit du Livre III — Chapitre 10 : Visages, peau, yeux, cheveux et pilosité"
id: "DOC-L3-QA-AUDIT-CH10"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 10
last-verified: "2026-07-23T10:56:17+02:00"
audit-date: "2026-07-23T10:56:17+02:00"
audit-level: "static-review"
audited-document: "Livre-III/CHAPITRE-10-Visages-peau-yeux-cheveux-et-pilosite.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit — Chapitre 10 : Visages, peau, yeux, cheveux et pilosité

## 1. Décision

Le chapitre est **accepté au niveau `static-review` avec réserves runtime**.

Il couvre le périmètre du plan maître sans revendiquer de tête finale, sculpture, retopologie, texture, matériau, œil, dentition, groom, hair card, blendshape, export, scène Godot ou mesure réellement exécutés. Les frontières avec les bases humaines et humanoïdes des chapitres 6 et 7, les créatures du chapitre 9, les vêtements du chapitre 11, le pipeline PBR du chapitre 16, les UV et le baking du chapitre 17, le rig facial du chapitre 19 et la synchronisation labiale du chapitre 27 sont explicites.

## 2. Périmètre comparé au plan maître

| Exigence | Couverture | Décision |
|---|---|---|
| Topologie du visage et zones de déformation | Sections 8 à 12 | Conforme |
| Sculpture, asymétrie et variation | Sections 10 et 11 | Conforme |
| Shader de peau et gestion des détails | Sections 13 à 15 | Conforme, sans paramètres runtime revendiqués |
| Œil, cornée, iris, humidité et reflets | Sections 16 et 17 | Conforme |
| Dents, bouche et intersections | Section 18 | Conforme |
| Cheveux, barbe, fourrure et transparence | Sections 19 à 22 | Conforme |
| Blendshapes et expressions de test | Section 12 | Préparation documentée, visèmes exclus |
| LOD facial | Section 23 | Conforme |
| Tête de référence | Sections 6 à 12 et 33 | Contrat documenté, asset non matérialisé |
| Matériaux peau et yeux | Sections 13 à 17 et 33 | Profils documentés, matériaux non matérialisés |
| Bibliothèque cheveux et pilosité | Sections 19 à 22 et 33 | Profils documentés, bibliothèque non matérialisée |
| Système facial de préparation | Sections 12, 25 et 26 | Conforme, système final non produit |
| Profils LOD | Sections 23, 28 et 33 | Conforme |
| Gros plans sous plusieurs éclairages | Sections 15, 20 et 27 | Protocole documenté, captures non produites |
| Absence d'artefacts de transparence/intersection | Sections 17 à 22 et 32 | Contrôles documentés, tests non exécutés |
| LOD facial stable | Sections 23, 28 et 32 | Protocole documenté, stabilité non mesurée |
| Frontière avec le chapitre 27 | Sections 4, 12, 25, 30 et 34 | Conforme |

## 3. Livrables permanents

Les cinq livrables exigés sont matérialisés comme contrats réutilisables :

1. tête de référence ;
2. matériaux peau et yeux ;
3. bibliothèque de cheveux et pilosité ;
4. blendshapes ou système facial de préparation ;
5. profils LOD.

La scène `FaceValidationLab` est documentée comme environnement commun de preuve. Aucun fichier Blender, texture, GLB ou scène Godot n'est annoncé comme existant.

## 4. Cohérence technique

### 4.1 Anatomie, sculpture et topologie

- repères artistiques distingués d'une norme médicale ;
- construction par formes primaires, secondaires et tertiaires ;
- détail tertiaire interdit comme correction d'une erreur primaire ;
- boucles de paupières et de lèvres explicitement prioritaires ;
- densité guidée par la déformation ;
- symétrie de construction séparée de l'asymétrie contrôlée ;
- formes de test limitées à la validation de déformation ;
- visèmes, timings et acting exclus.

### 4.2 Peau, yeux et bouche

- couleur sRGB séparée des cartes de données linéaires ;
- couleur de base sans ombres directionnelles peintes ;
- roughness régionale ;
- normal et detail normal séparées ;
- diffusion sous-surface qualifiée comme profil à mesurer ;
- sclère, cornée, iris et film humide distingués ;
- paupières préparées pour envelopper le globe ;
- sac buccal, dents, gencives et langue documentés ;
- intersections et fuites lumineuses bloquantes.

### 4.3 Cheveux et pilosité

- volumes sculptés, mèches, hair cards, courbes et grooms comparés ;
- overdraw distingué du nombre de triangles ;
- conversion non destructive depuis une source canonique ;
- sourcils, cils, barbe et duvet possèdent parents et tests ;
- transparence, contre-jour, mipmaps et transitions LOD réservés à des preuves distinctes ;
- aucune conversion Blender-Godot annoncée comme réussie.

### 4.4 Godot, LOD et performance

- export GLB séparé de la source Blender ;
- scène dérivée et rig d'éclairage de référence ;
- caméras gros plan, dialogue et gameplay ;
- validateur GDScript non destructif ;
- fonctions, paramètres, types, retours et opérateurs expliqués ;
- rapports JSON structurés ;
- scénarios de performance séparés ;
- aucune valeur CPU, GPU, VRAM, draw call ou overdraw inventée.

## 5. Revue pédagogique

Le chapitre explique :

- le rôle de chaque fichier et profil ;
- les types YAML, JSON, PowerShell et GDScript significatifs ;
- les paramètres, valeurs, retours et opérateurs du validateur ;
- la différence entre volume, détail et bruit ;
- la différence entre couleur et éclairage ;
- la différence entre géométrie d'œil et matériau ;
- la différence entre triangles et overdraw ;
- la différence entre formes de test et visèmes ;
- la différence entre budget et mesure ;
- les parcours Solo et Studio ;
- les réserves et statuts bloquants.

Les dix diagnostics suivent la séquence imposée :

1. symptôme ;
2. exemple fautif ;
3. `Pourquoi cet exemple est fautif` ;
4. exemple corrigé ;
5. `Pourquoi la correction fonctionne`.

## 6. Métriques statiques

- lignes : 1 978 ;
- titres Markdown comptés : 49 ;
- blocs code ou données : 52 ;
- blocs significatifs retenus : 52 ;
- marqueurs `qa:code-explanation` : 52 ;
- explications structurées hors diagnostics : 32 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- corrections expliquées : 10 ;
- doublons de titres : 0 ;
- doublons de blocs : 0 ;
- doublons de paragraphes longs : 0.

## 7. Contrôles de frontières

Le chapitre ne contient pas :

- de nouvelle base corporelle humaine ou humanoïde ;
- de nouvelle anatomie de créature ;
- de système de vêtements ou d'accessoires ;
- de pipeline PBR transversal ;
- de cours générique complet sur UV, retopologie ou baking ;
- de rig facial de production final ;
- de contrôleurs d'animation ;
- de visèmes linguistiques finalisés ;
- de timings de dialogue ;
- de coarticulation ;
- de règles d'intelligence artificielle ou de gameplay ;
- de mesure runtime inventée ;
- de prochaine action éditoriale ;
- de recommandation GPT dans le texte lecteur ;
- de procédure QA interne dans le chapitre lecteur.

## 8. Sources qualifiées

Les fonctions techniques sont reliées aux documentations officielles Blender et Godot. Les pages `latest` ou `stable` sont signalées lorsqu'aucune page versionnée équivalente n'est exposée. Aucune source commerciale ou tutoriel tiers n'est nécessaire à la décision statique.

## 9. Réserves

- brief artistique réel non approuvé ;
- références, consentements et droits non qualifiés ;
- diversité et biais des références non revus ;
- tête pilote non produite ;
- repères et volumes non relus ;
- topologie et déformations non testées ;
- asymétrie non validée ;
- sculpture primaire, secondaire et tertiaire non réalisée ;
- textures de peau non produites ;
- matériau de peau non créé ;
- diffusion sous-surface non mesurée ;
- œil, cornée, iris et film humide non produits ;
- clignement et contact paupière-globe non testés ;
- bouche, dents, gencives et langue non produites ;
- intersections et fuites lumineuses non testées ;
- solution de cheveux non choisie ;
- hair cards et overdraw non mesurés ;
- conversion de groom non testée ;
- sourcils, cils, barbe et duvet non produits ;
- formes faciales de test non produites ;
- LOD non produits ni mesurés ;
- export GLB non exécuté ;
- scène Godot non matérialisée ;
- validateur GDScript non exécuté ;
- éclairages et captures non produits ;
- performances CPU, GPU, VRAM, draw calls et overdraw non mesurées ;
- Starter Kit non matérialisé ;
- licence globale non définie ;
- PDF du Livre III non construit.

## 10. Avertissement documentaire

Un avertissement demeure : distances de caméra, nombres de LOD, résolutions, densités, nombres de cartes, intensités, rayons et profils matériels sont provisoires. Ils ne doivent pas être repris comme objectifs définitifs sans campagne réelle dans `Project Asteria`.

## 11. Conclusion

Décision : **accepté au niveau `static-review`**, sous réserve de la réussite des validateurs légers et du maintien explicite de toutes les réserves runtime.
