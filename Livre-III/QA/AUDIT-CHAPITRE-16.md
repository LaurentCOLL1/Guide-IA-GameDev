---
title: "Audit du Livre III — Chapitre 16 : Textures, matériaux et pipeline PBR"
id: "DOC-L3-QA-AUDIT-CH16"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 16
last-verified: "2026-07-23T21:15:00+02:00"
audit-date: "2026-07-23T21:15:00+02:00"
audit-level: "static-review"
audited-document: "Livre-III/CHAPITRE-16-Textures-materiaux-et-pipeline-PBR.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit — Chapitre 16 : Textures, matériaux et pipeline PBR

## 1. Décision

Le chapitre est **accepté au niveau `static-review` avec réserves runtime**.

Le document établit une chaîne PBR depuis la source et la provenance jusqu’aux matériaux Godot, à la scène d’éclairage comparative et au budget mémoire. Il ne revendique comme produits ni textures, ni matériaux Blender ou Godot, ni presets, ni captures, ni mesures.

## 2. Périmètre comparé au plan maître

| Exigence | Couverture | Décision |
|---|---|---|
| Rôle et interprétation de chaque carte PBR | Sections 7 à 15 | Conforme |
| sRGB, données linéaires et erreurs de colorimétrie | Sections 16 et 47.1 | Conforme |
| Résolution, mipmaps, compression et mémoire | Sections 18 à 21 et 41 | Conforme comme protocole non exécuté |
| Densité de texels et cohérence inter-assets | Section 23 | Conforme, cibles réservées |
| Matériaux tilables | Section 25 | Conforme |
| Trim sheets | Section 26 | Conforme, affectation UV laissée au chapitre 17 |
| Atlas | Section 27 | Conforme, marges laissées au chapitre 17 |
| Configuration des matériaux Godot | Sections 33 à 36 | Conforme comme exemples non exécutés |
| Scène d’éclairage de référence | Sections 37 à 40 | Conforme comme contrat non matérialisé |
| Guide PBR | Sections 6 à 23 et 49 | Contrat documenté |
| Presets d’export et d’import | Sections 32 et 33 et 49 | Contrat documenté |
| Bibliothèque de matériaux | Sections 24, 42 et 49 | Contrat documenté |
| Profils de compression | Sections 20 à 22 et 49 | Contrat documenté |
| Scène d’éclairage comparative | Sections 37 à 40 et 49 | Contrat documenté |
| Cohérence sous plusieurs éclairages | Sections 37 à 40, 44 et 48 | Porte de validation documentée |
| Canaux et espaces correctement configurés | Sections 7 à 22, 34 et 35 | Porte de validation documentée |
| Mémoire et résolution conformes | Sections 18 à 23, 41, 44 et 48 | Protocole documenté, mesures absentes |
| Frontière avec terrains et végétation | Sections 1, 4 et 50 | Conforme |
| Frontière avec UV et baking | Sections 4, 12, 13, 26, 27 et 32 | Conforme |
| Frontière avec optimisation globale | Sections 4 et 48 | Conforme |

## 3. Livrables permanents

Les cinq livrables du plan maître sont matérialisés comme contrats versionnés :

1. guide PBR ;
2. presets d’export et d’import ;
3. bibliothèque de matériaux ;
4. profils de compression ;
5. scène d’éclairage de référence.

Le laboratoire `AST-MAT-LAB-PBR-001` et les identifiants associés restent des cibles de production. Aucun fichier Blender, texture, ressource `.tres`, GLB, preset d’import, capture ou rapport de VRAM n’est annoncé comme existant.

## 4. Cohérence technique

### 4.1 Canaux PBR

- la base color est séparée des ombres et reflets capturés ;
- metallic décrit la nature conductrice et non la brillance ;
- roughness est reliée aux causes microscopiques ;
- les normales tangentielles sont traitées comme données ;
- AO, height, emissive et opacity possèdent des contrats distincts ;
- les fonctions VFX ou baking restent sous l’autorité des chapitres propriétaires.

### 4.2 Colorimétrie, formats et mémoire

- base color et couleur emissive utilisent sRGB ;
- roughness, metallic, normal, AO, height et masques restent linéaires ;
- PNG, EXR et JPEG sont qualifiés par usage ;
- stockage disque, format importé et VRAM sont séparés ;
- la chaîne complète de mipmaps est incluse dans l’estimation ;
- les limites d’import ne détruisent pas les sources.

### 4.3 Compression et packing

- les profils VRAM sont des candidats à mesurer ;
- les normales reçoivent un profil adapté ;
- le packing ORM suit R=AO, G=roughness, B=metallic ;
- les canaux packés sont prévisualisés séparément ;
- aucun format GPU définitif n’est inventé.

### 4.4 Densité et réutilisation

- la densité de texels relie pixels et dimensions réelles ;
- les classes d’usage restent à mesurer ;
- les matériaux maîtres demeurent spécialisés ;
- les matériaux tilables possèdent une échelle physique ;
- les trim sheets et atlas sont versionnés ;
- les détails et décalcomanies répondent à des causes lisibles.

### 4.5 Blender, glTF et Godot

- Blender reste une référence de lookdev ;
- le Principled BSDF connecte les canaux selon leur sémantique ;
- glTF transporte le sous-ensemble metallic-roughness ;
- Godot reste l’autorité de la ressource runtime dérivée ;
- `StandardMaterial3D` et `ORMMaterial3D` sont séparés ;
- filtre, répétition et anisotropie sont documentés ;
- les exemples GDScript n’ont pas été exécutés.

### 4.6 Validation

- le laboratoire contient géométries, étalons et caméras verrouillées ;
- quatre profils d’éclairage sont distingués ;
- les captures conservent commit, scène, matériau et import ;
- les campagnes varient une famille de paramètres à la fois ;
- CPU, GPU, VRAM et défauts visuels sont enregistrés séparément ;
- aucune valeur runtime n’est inventée.

## 5. Revue pédagogique

Le chapitre explique notamment :

- la différence entre couleur sRGB et donnée linéaire ;
- la différence entre metallic et brillance ;
- la différence entre roughness et luminance de la base color ;
- la différence entre normale, height et géométrie ;
- la différence entre poids disque et mémoire GPU ;
- la différence entre matériau tilable, trim sheet, atlas et décalcomanie ;
- la différence entre matériau Blender, sous-ensemble glTF et ressource Godot ;
- la différence entre estimation mémoire et mesure ;
- les parcours Solo et Studio ;
- les portes de preuve et réserves runtime.

Les dix diagnostics respectent la séquence imposée : symptôme, exemple fautif, explication directe, exemple corrigé et explication de la correction.

## 6. Métriques statiques

- lignes : 1654 ;
- titres Markdown : 63 ;
- blocs code ou données significatifs : 68 ;
- marqueurs `qa:code-explanation` : 68 ;
- explications structurées hors diagnostics : 48 ;
- diagnostics détaillés : 10 ;
- exemples fautifs expliqués : 10 ;
- corrections expliquées : 10 ;
- doublons de titres : 0 ;
- doublons de blocs : 0 ;
- doublons de paragraphes longs : 0.

## 7. Contrôles de frontières

Le chapitre ne contient pas :

- de nouveau système de terrain ou de végétation ;
- de découpe UV détaillée ;
- de création de cage ou de baking approfondi ;
- de chaîne LOD générale ;
- de système VFX complet ;
- d’intégration globale du pipeline artistique ;
- de résultat Blender ou Godot inventé ;
- de budget mémoire présenté comme mesuré ;
- de prochaine action éditoriale ;
- de recommandation GPT dans le texte lecteur ;
- de procédure QA interne dans le chapitre lecteur.

## 8. Sources qualifiées

Le chapitre s’appuie sur les documentations officielles de Godot pour l’import des images, le processus d’import, `BaseMaterial3D`, `StandardMaterial3D` et `ORMMaterial3D`, sur le manuel Blender pour le Principled BSDF et la gestion des couleurs, ainsi que sur la spécification glTF 2.0.

La documentation stable de Godot décrit la compression VRAM comme le profil courant pour les textures 3D, recommande les mipmaps en 3D et indique que les réglages de filtre et de répétition des matériaux 3D ne relèvent plus des options d’import générales. Le chapitre conserve ces réglages comme candidats à valider sur Godot `4.7.1-stable`.

## 9. Réserves

- laboratoire PBR non créé ;
- géométries de calibration non produites ;
- environnements neutre, chaud, froid et contrasté non configurés ;
- textures sources non produites ;
- provenance et droits non qualifiés ;
- canaux PBR non peints ni bakés ;
- espaces colorimétriques non contrôlés dans les applications ;
- résolutions et densités non mesurées ;
- mipmaps non inspectés ;
- profils de compression non appliqués ;
- packing ORM non produit ;
- matériaux tilables, trim sheets et atlas non produits ;
- Principled BSDF Blender non construit ;
- export GLB non réalisé ;
- profils d’import Godot non matérialisés ;
- `StandardMaterial3D` et `ORMMaterial3D` non créés ;
- filtres, répétition et anisotropie non testés ;
- captures comparatives non produites ;
- validateur GDScript non exécuté ;
- CPU, GPU et VRAM non mesurés ;
- Starter Kit non matérialisé ;
- licence globale non définie ;
- PDF du Livre III non construit.

## 10. Avertissement documentaire

Un avertissement demeure : résolutions, densités de texels, tailles de cycle, paramètres de roughness, intensités emissives, profils de compression, limites d’import, anisotropie, budgets et mesures sont provisoires. Ils ne doivent pas être repris comme objectifs définitifs sans campagne réelle dans `Project Asteria`.

## 11. Conclusion

Décision : **accepté au niveau `static-review`**, sous réserve de la réussite des validateurs légers et du maintien explicite de toutes les réserves runtime.
