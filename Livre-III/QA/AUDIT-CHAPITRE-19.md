---
title: "Audit du Livre III — Chapitre 19 : Rigging et skinning"
id: "DOC-L3-QA-AUDIT-CH19"
status: "complete"
version: "1.0.1"
lang: "fr-FR"
book: "Livre III"
chapter: 19
last-verified: "2026-07-24T11:13:52+02:00"
audit-date: "2026-07-24T11:13:52+02:00"
audit-level: "static-review"
audited-document: "Livre-III/CHAPITRE-19-Rigging-et-skinning.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit — Chapitre 19 : Rigging et skinning

## 1. Décision

Le chapitre est **accepté au niveau `static-review` avec réserves de production et runtime**.

Il documente une chaîne complète depuis le maillage final jusqu’au squelette de déformation, rig de contrôle, skinning, correctifs, sockets, export glTF, import Godot et retargeting. Aucun rig, poids, GLB, scène, capture ou résultat runtime n’est présenté comme produit.

## 2. Couverture du plan maître

| Exigence | Couverture | Décision |
|---|---|---|
| Squelette de déformation et rig de contrôle | Sections 10 à 16 | Conforme |
| Orientation, roll et hiérarchie | Sections 9 à 18 | Conforme |
| Contraintes et limites articulaires | Sections 26 à 32 | Conforme |
| Poids, influences et volumes | Sections 37 à 49 | Conforme |
| Twist bones, correctifs et poses extrêmes | Sections 33 à 35 et 50 à 53 | Conforme |
| Sockets et os accessoires | Sections 22, 24, 36 et 59 | Conforme |
| Export, rest pose et compatibilité Godot | Sections 10, 54 à 60 | Conforme comme protocole non exécuté |
| Rigs de référence | Sections 5, 14 à 16 et 61 | Contrat documenté, fichiers absents |
| Conventions d’os | Sections 7, 11 à 18 | Conforme |
| Profils de skinning | Sections 37 à 49 | Contrats documentés, mesures absentes |
| Poses de test | Sections 44, 51 et 52 | Conforme, captures absentes |
| Fichiers d’export | Sections 54 à 56 | Structure documentée, GLB absent |
| Frontière avec le chapitre 18 | Sections 1 et 4 | Conforme |
| Frontière avec le chapitre 20 | Sections 4, 13, 20, 30, 31, 51 et 65 | Conforme |
| Frontière avec le chapitre 28 | Sections 4 et 56 à 60 | Conforme |

## 3. Cohérence technique

- squelette de déformation, contrôles, mécanismes, correctifs et sockets ont des rôles distincts ;
- axes, unités, transforms, rest pose, roll et hiérarchie sont traités avant les contraintes ;
- bassin, colonne, épaules, membres, mains et pieds disposent de contrats séparés ;
- IK, FK, pole targets, commutation et espaces sont documentés sans animation finale ;
- twist bones, correctifs osseux et shape keys restent justifiés par des poses ;
- bind automatique, normalisation, verrous, miroir et limites d’influences sont encadrés ;
- la grille de poses et le rapport relient défauts, corrections et régressions ;
- l’export filtre contrôleurs et mécanismes, puis conserve squelette, skin et sockets ;
- `Skeleton3D`, `SkeletonProfile`, `BoneMap`, retargeting et `BoneAttachment3D` ont des responsabilités distinctes ;
- le validateur Godot contrôle la structure sans prononcer de jugement esthétique.

## 4. Revue pédagogique

Les 81 blocs significatifs possèdent chacun un marqueur d’explication. Les 61 blocs hors diagnostics disposent d’au moins quatre rubriques structurées. Les dix diagnostics respectent la séquence symptôme, exemple fautif, explication directe, exemple corrigé et justification.

## 5. Métriques statiques

- lignes : 2255 ;
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
- squelette de déformation, contrôleurs, mécanismes et correctifs non créés ;
- roll, axes, rest pose, contraintes, IK/FK et espaces non testés ;
- bind, poids, normalisation, miroir et limites d’influences non exécutés ;
- poses extrêmes, volumes, intersections et dérives de sockets non mesurés ;
- GLB, manifeste, scène Godot et rapports de validation absents ;
- `Skeleton3D`, `BoneMap`, retargeting et `BoneAttachment3D` non testés ;
- performances de skinning et budgets d’os non mesurés ;
- provenance et droits du pilote non qualifiés ;
- Starter Kit non matérialisé ;
- licence globale non définie ;
- PDF du Livre III non construit.

## 7. Avertissement documentaire

Les nombres d’os, angles, influences maximales, seuils de nettoyage, facteurs de twist et limites articulaires restent des valeurs candidates. Ils ne doivent pas devenir des valeurs de production sans rig réel, poses réelles, export réel et tests sur les plateformes de référence.

## 8. Conclusion

Décision : **accepté au niveau `static-review`**, sous réserve de la réussite des validateurs légers et du maintien explicite de toutes les réserves de production et runtime.

## Correctif transversal — Synthèse opérationnelle Project Asteria

La section de clôture propre à Project Asteria a été restaurée dans le chapitre 19. Elle transforme la conclusion générale en décisions de pipeline, identifiants, dépendances, portes d’acceptation et réserves directement applicables au projet fil rouge. Ce correctif ne modifie pas le périmètre technique ni le niveau de preuve `static-review` ; il restaure une exigence éditoriale transversale et rend sa présence contrôlable automatiquement.
