---
title: "Audit du Livre III — Chapitre 18 : LOD, imposteurs et optimisation géométrique"
id: "DOC-L3-QA-AUDIT-CH18"
status: "complete"
version: "1.0.1"
lang: "fr-FR"
book: "Livre III"
chapter: 18
last-verified: "2026-07-24T11:13:52+02:00"
audit-date: "2026-07-24T11:13:52+02:00"
audit-level: "static-review"
audited-document: "Livre-III/CHAPITRE-18-LOD-imposteurs-et-optimisation-geometrique.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit — Chapitre 18 : LOD, imposteurs et optimisation géométrique

## 1. Décision

Le chapitre est **accepté au niveau `static-review` avec réserves de production et runtime**.

Il documente une chaîne complète depuis le LOD0 approuvé jusqu’aux LOD manuels ou automatiques, imposteurs, billboards, proxies, profils de distance et benchmark. Aucun mesh, atlas, GLB, scène, capture ou résultat runtime n’est présenté comme produit.

## 2. Couverture du plan maître

| Exigence | Couverture | Décision |
|---|---|---|
| Budget par taille écran et importance gameplay | Sections 7 à 12 et 39 à 40 | Conforme |
| Décimation et silhouette | Sections 20 à 26 | Conforme |
| Simplification matériaux et textures | Sections 27 à 29 | Conforme |
| Imposteurs, billboards et orientation | Sections 41 à 47 | Conforme |
| Seuils, hystérésis et transitions | Sections 34 à 40 | Conforme |
| Popping, ombres et collisions | Sections 30, 31, 36, 37, 47 et 61 | Conforme |
| Benchmark avant/après | Sections 11, 52 à 58 et 62 | Conforme comme protocole non exécuté |
| Chaîne LOD | Sections 16 à 40 et 63 | Contrat documenté, fichiers absents |
| Imposteurs | Sections 41 à 47 et 63 | Contrat documenté, atlas absent |
| Profils de distance | Sections 8 à 12, 35 à 40 et 63 | Contrats documentés, mesures absentes |
| Scène de benchmark | Sections 52 à 55 et 63 | Structure documentée, scène absente |
| Tableau comparatif | Sections 54 à 56 et 63 | Structure documentée, données absentes |
| Frontière avec le chapitre 17 | Sections 1, 4, 19, 26 à 29 et 58 | Conforme |
| Frontière avec le chapitre 19 | Sections 4 et 48 | Conforme |
| Frontière avec le chapitre 28 | Sections 4, 33 et 51 | Conforme |
| Frontière avec le Livre IV | Sections 1, 4 et 51 | Conforme |

## 3. Cohérence technique

- la taille écran, le FOV, la résolution, l’échelle et l’importance gameplay sont distingués ;
- triangles Blender, sommets exportés, surfaces, draw calls et mémoire restent des métriques séparées ;
- Collapse, Planar et Un-Subdivide sont employés selon leur topologie cible ;
- silhouette, normales, tangentes, triangulation et UV sont revus par niveau ;
- LOD manuel, LOD automatique Godot, HLOD, imposteur et billboard ont des rôles distincts ;
- `lod_bias`, plages de visibilité, hystérésis et limites des fades par renderer sont documentés ;
- collisions et ombres utilisent des proxies sans donner au visuel une autorité gameplay ;
- alpha, padding, normales et profondeur d’imposteur sont qualifiés ;
- MultiMesh, AABB, culling et occlusion sont traités sans glissement de périmètre ;
- baseline, variantes, répétitions, données brutes, captures et non-régression sont explicités.

## 4. Revue pédagogique

Les 81 blocs significatifs possèdent chacun un marqueur d’explication. Les 61 blocs hors diagnostics disposent d’au moins quatre rubriques structurées. Les dix diagnostics respectent la séquence symptôme, exemple fautif, explication directe, exemple corrigé et justification.

## 5. Métriques statiques

- lignes : 3904 ;
- titres Markdown : 76 ;
- blocs code ou données significatifs : 81 ;
- marqueurs `qa:code-explanation` : 81 ;
- explications structurées hors diagnostics : 61 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- corrections expliquées : 10 ;
- doublons de titres : 0 ;
- doublons de blocs : 0 ;
- doublons de paragraphes longs : 0.

## 6. Réserves

- pilote non matérialisé ni approuvé en production ;
- LOD0, LOD1, LOD2, proxies et imposteur non créés ;
- ratios, triangles, sommets, surfaces, draw calls et mémoire non mesurés ;
- tailles écran, FOV, distances, marges et hystérésis non testés ;
- génération automatique Godot non comparée aux LOD manuels ;
- atlas, alpha, padding, normales et profondeur d’imposteur non produits ;
- ombres, collisions, AABB, culling, MultiMesh et occlusion non testés ;
- GLB, scène Godot, parcours caméra, captures et données brutes absents ;
- benchmark CPU/GPU non exécuté ;
- provenance et droits du pilote non qualifiés ;
- Starter Kit non matérialisé ;
- licence globale non définie ;
- PDF du Livre III non construit.

## 7. Avertissement documentaire

Les ratios, budgets, résolutions d’atlas, nombres de vues, seuils de distance, marges, durées et répétitions restent des valeurs candidates. Elles ne doivent pas devenir des valeurs de production sans assets réels, caméras réelles et mesures sur les plateformes de référence.

## 8. Conclusion

Décision : **accepté au niveau `static-review`**, sous réserve de la réussite des validateurs légers et du maintien explicite de toutes les réserves de production et runtime.

## Correctif transversal — Synthèse opérationnelle Project Asteria

La section de clôture propre à Project Asteria a été restaurée dans le chapitre 18. Elle transforme la conclusion générale en décisions de pipeline, identifiants, dépendances, portes d’acceptation et réserves directement applicables au projet fil rouge. Ce correctif ne modifie pas le périmètre technique ni le niveau de preuve `static-review` ; il restaure une exigence éditoriale transversale et rend sa présence contrôlable automatiquement.
