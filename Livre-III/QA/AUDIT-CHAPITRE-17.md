---
title: "Audit du Livre III — Chapitre 17 : UV, retopologie et baking"
id: "DOC-L3-QA-AUDIT-CH17"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 17
last-verified: "2026-07-23T23:15:00+02:00"
audit-date: "2026-07-23T23:15:00+02:00"
audit-level: "static-review"
audited-document: "Livre-III/CHAPITRE-17-UV-retopologie-et-baking.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit — Chapitre 17 : UV, retopologie et baking

## 1. Décision

Le chapitre est **accepté au niveau `static-review` avec réserves de production et runtime**.

Le document définit une chaîne complète depuis le modèle haute résolution jusqu’au contrôle Blender–Godot du low poly et de ses textures bakées. Il ne revendique comme produits ni high poly, ni low poly, ni UV, ni cage, ni texture, ni GLB, ni scène Godot, ni capture, ni mesure.

## 2. Périmètre comparé au plan maître

| Exigence | Couverture | Décision |
|---|---|---|
| Objectifs statiques ou déformables | Sections 7, 16 et 17 | Conforme |
| Edge flow et densité locale | Sections 15 à 19 | Conforme |
| Découpe UV, îlots, marges et overlaps | Sections 24 à 34 | Conforme |
| Cages, ray distance et correspondance | Sections 35 à 40 | Conforme |
| Normales, AO, curvature et autres cartes | Sections 41 à 47 | Conforme |
| Tangent space Blender–Godot | Sections 41, 42, 51 et 55 à 59 | Conforme comme procédure non exécutée |
| Contrôle visuel et corrections | Sections 54, 58 à 60, 65 et 66 | Conforme |
| Maillage haute résolution | Sections 8, 53 et 67 | Contrat documenté, asset absent |
| Maillage basse résolution | Sections 9, 15 à 23, 53 et 67 | Contrat documenté, asset absent |
| UV et cages | Sections 24 à 40 et 67 | Contrats documentés, fichiers absents |
| Textures bakées | Sections 36, 41 à 53 et 67 | Contrats documentés, fichiers absents |
| Rapport de contrôle | Sections 59, 60, 66 et 67 | Structure documentée |
| Absence d’artefacts majeurs | Sections 31, 47 à 51, 54, 58 et 66 | Porte documentée, résultat absent |
| Densité UV cohérente | Sections 27 à 31 | Procédure documentée, mesure absente |
| Comparaison high/low sous éclairage | Sections 54, 58 et 59 | Scènes préparées, captures absentes |
| Frontière avec le chapitre 16 | Sections 1, 4, 29, 43, 45, 46 et 52 | Conforme |
| Frontière avec le chapitre 18 | Sections 1, 4, 19, 62 et 66 | Conforme |
| Frontière avec les chapitres 19 et 20 | Sections 4, 7, 16 et 24 | Conforme |

## 3. Livrables permanents

Les cinq livrables du plan maître sont matérialisés comme contrats versionnés :

1. maillage haute résolution ;
2. maillage basse résolution ;
3. UV et cages ;
4. textures bakées ;
5. rapport de contrôle.

Le pilote `AST-BAKE-PILOT-RELAY-001` reste une cible de production. Aucun `.blend`, EXR, PNG, GLB, `.tscn`, `.import`, manifeste de capture ou rapport d’exécution n’est annoncé comme existant.

## 4. Cohérence technique

### 4.1 Retopologie

- la coque statique et la sangle souple reçoivent des profils distincts ;
- la silhouette, les contacts et les biseaux majeurs précèdent la densité interne ;
- quads, triangles, n-gons et pôles sont qualifiés selon leur fonction ;
- Poly Build, snapping et Shrinkwrap restent des aides contrôlées ;
- le low poly possède l’autorité sur la silhouette, les UV, normales, tangentes et triangles ;
- la triangulation est figée avant le bake final.

### 4.2 UV

- la carte principale et l’éventuelle carte secondaire ont des responsabilités séparées ;
- seams, îlots et orientations sont liés à visibilité, peinture et distorsion ;
- checker, Average Island Scale et Minimize Stretch sont utilisés avec revue humaine ;
- la densité de texels hérite des profils du chapitre 16 ;
- la marge UV et la dilation de bake sont coordonnées avec mipmaps et compression ;
- chaque overlap intentionnel est enregistré avec les cartes compatibles ;
- UDIM reste une exception qualifiée et non un défaut de pipeline.

### 4.3 Projection et baking

- high, low et cage utilisent des suffixes et bake sets déterministes ;
- Selected to Active vérifie sources, cible active et image ;
- cage automatique, cage manuelle et Max Ray Distance sont distingués ;
- la cage manuelle conserve topologie et ordre des faces du low ;
- la normale est bakée en tangent space après gel des UV, normales et triangles ;
- AO, curvature et cartes auxiliaires conservent des rôles limités ;
- marges, échantillonnage, skew et géométries fines possèdent des diagnostics dédiés.

### 4.4 Blender, glTF et Godot

- glTF 2.0 et GLB restent l’échange de référence ;
- normales, UV et tangentes sont exportées ;
- `Ensure Tangents` Godot reste un fallback MikkTSpace, l’export DCC étant préféré ;
- la normale canonique est OpenGL `X+`, `Y+`, `Z+` ;
- `Normal Map Invert Y` est réservé à la conversion de cartes DirectX ;
- les `.import` sont versionnés, le dossier `.godot` ne l’est pas ;
- le validateur GDScript contrôle structure et présence des arrays sans prétendre juger les pixels ;
- la scène comparative sépare low avec et sans normale.

## 5. Revue pédagogique

Le chapitre explique notamment :

- pourquoi la retopologie statique et déformable diffèrent ;
- pourquoi les quads ne sont pas une règle absolue ;
- pourquoi la silhouette précède le transfert de détail ;
- pourquoi hard edge et UV seam ne sont pas synonymes ;
- pourquoi la triangulation doit être gelée avant le bake ;
- comment relier marge UV, dilation, mipmaps et compression ;
- quand un overlap est autorisé ou interdit ;
- comment choisir entre cage et Max Ray Distance ;
- pourquoi une normale tangentielle dépend du low final ;
- comment reconnaître une carte DirectX dans Godot ;
- comment distinguer contrôle structurel et validation visuelle ;
- comment adapter le workflow aux modes Solo et Studio.

Les dix diagnostics respectent la séquence imposée : symptôme, exemple fautif, explication directe, exemple corrigé et explication de la correction.

## 6. Métriques statiques

- lignes : 2890 ;
- titres Markdown : 82 ;
- blocs code ou données significatifs : 84 ;
- marqueurs `qa:code-explanation` : 84 ;
- explications structurées hors diagnostics : 64 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- corrections expliquées : 10 ;
- doublons de titres : 0 ;
- doublons de blocs : 0 ;
- doublons de paragraphes longs : 0.

## 7. Contrôles de frontières

Le chapitre ne contient pas :

- de redéfinition complète des cartes PBR, profils de compression ou matériaux maîtres ;
- de création de LOD, imposteurs, distances ou benchmark avant/après ;
- de rig, skinning ou poids de déformation ;
- de cours général d’animation ;
- de système autonome de lightmapping ;
- de production effective du pilote ;
- de mesure runtime inventée ;
- de prochaine action éditoriale ;
- de recommandation GPT dans le texte lecteur ;
- de procédure QA interne dans le chapitre lecteur.

## 8. Sources qualifiées

Le chapitre relie ses mécanismes aux documentations officielles Blender pour la retopologie, Poly Build, les UV, Pack Islands, Average Island Scale, Minimize Stretch et le baking, ainsi qu’aux documentations officielles Godot 4.7 pour glTF, les tangentes MikkTSpace, l’import d’images, la compression RGTC et l’orientation OpenGL des normales.

La documentation Godot précise que les tangentes sont nécessaires aux normales et height maps, que MikkTSpace peut être généré à l’import si elles manquent et que l’export depuis le DCC est préférable lorsque possible. Elle précise aussi que Godot attend des normales OpenGL et propose l’inversion Y pour les cartes DirectX.

## 9. Réserves

- asset pilote non approuvé par une revue de production ;
- high poly, low poly et cages non créés ;
- transformations, silhouette, edge flow et densité géométrique non mesurés ;
- UV, seams, îlots, overlaps, marges et densité de texels non produits ni mesurés ;
- triangulation et normales non gelées sur un asset réel ;
- images cibles et bake sets non matérialisés ;
- normales, AO, curvature et cartes auxiliaires non bakées ;
- cages, distances et skew non testés ;
- texture OpenGL non importée ;
- tangentes Blender et fallback Godot non comparées ;
- GLB et scènes de contrôle non produits ;
- validateur GDScript non exécuté ;
- captures et rapport de contrôle non produits ;
- triangles, sommets exportés, mémoire et draw calls non mesurés ;
- sources, brushes, alphas et droits non qualifiés ;
- Starter Kit non matérialisé ;
- licence globale non définie ;
- PDF du Livre III non construit.

## 10. Avertissement documentaire

Un avertissement demeure : densités, marges, résolutions, distances de rayons, extrusions de cage, budgets géométriques, facteurs de suréchantillonnage et tolérances restent des paramètres candidats. Ils ne doivent pas être repris comme valeurs définitives sans asset réel, captures Blender–Godot et mesures sur le matériel de référence.

## 11. Conclusion

Décision : **accepté au niveau `static-review`**, sous réserve de la réussite des validateurs légers et du maintien explicite de toutes les réserves de production et runtime.
