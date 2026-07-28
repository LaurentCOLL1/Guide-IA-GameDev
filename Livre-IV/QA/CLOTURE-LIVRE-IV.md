---
title: "Clôture technique et PDF — Livre IV"
id: "DOC-L4-QA-CLOSURE"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-28T07:28:40+02:00"
audit-level: "static-review+pdf-inspected"
target-book: "Livre IV"
---

# Clôture technique et PDF — Livre IV

## 1. Décision

Le Livre IV — **Finalisation, optimisation, publication et maintenance** est accepté au niveau de publication technique documentaire `static-review+pdf-inspected`.

La décision couvre la présence et la cohérence des 22 chapitres, les métadonnées et audits, l’ordre lecteur, la compilation Pandoc/XeLaTeX, le préflight structurel, l’extraction textuelle, les polices incorporées et une inspection visuelle représentative. Elle ne qualifie aucune campagne runtime, plateforme, archive, restauration, build de jeu, service, procédure de support ou conformité juridique réelle.

## 2. Périmètre contrôlé

- `Livre-IV/index.md` et les 22 chapitres inscrits dans `contents.txt` ;
- les audits et preuves QA de chapitre, exclus du PDF lecteur ;
- les contrôles de structure, métadonnées, liens, doublons et repères d’utilisation ;
- `build.sh`, les métadonnées Pandoc, le modèle XeLaTeX et `filters/pdf-normalize.lua` ;
- le PDF cumulatif de la collection à l’état de fin du Livre IV ;
- la transition vers le Livre V et le Companion Pack.

## 3. Corrections découvertes pendant la campagne

Trois caractères de contrôle `BEL` invisibles empêchaient XeLaTeX de compiler des exemples de chemins Windows. Ils ont été remplacés par les séparateurs attendus dans les chapitres 16 et 18 :

- `platform-tools\adb.exe` ;
- `docs\accessibility\task-barriers.yaml` ;
- `docs\accessibility\public-statement.md`.

Le filtre PDF supprimait également le chapitre 2 entier parce que la chaîne générale `assurance qualité` était traitée comme un titre de fabrication. La règle est désormais exacte : une rubrique interne intitulée uniquement `Assurance qualité` peut être exclue, mais **Stratégie générale d’assurance qualité** reste un chapitre lecteur. Un garde-fou vérifie maintenant la présence des 22 titres du Livre IV dans le texte extrait.

## 4. Validation documentaire transversale

- 22 chapitres présents et inscrits dans l’ordre lecteur ;
- identifiants de documents uniques ;
- audits et preuves de chapitre résolus ;
- zéro erreur bloquante de structure, métadonnées, liens ou doublons ;
- zéro non-conformité de présence ou de cohérence sémantique des repères ;
- aucune preuve QA, audit de chapitre ou protocole interne dans le PDF lecteur ;
- les 22 titres de chapitre sont présents dans le texte extrait du PDF.

## 5. Compilation et préflight finaux

La tête lecteur `f6b2118daf23edf7595ce9d5e2b4d300c00b1d40` a été compilée par le workflow `Livre IV PDF Closure Runner`, run `30331869053`.

| Contrôle | Résultat |
|---|---|
| Pandoc/XeLaTeX | succès |
| `qpdf --check` | succès, aucune erreur de syntaxe ou de flux |
| Pages | 3 672 |
| Format | A4, 595,28 × 841,89 points |
| Version PDF | 1.5 |
| Taille | 9 428 292 octets |
| Chiffrement | non |
| Formulaires | aucun |
| JavaScript | absent |
| Texte extractible | oui |
| Polices | incorporées et sous-ensembles ; aucun Type 3 ou type inconnu |
| Balisage d’accessibilité | non |

Empreintes :

- PDF : `013f8d9bf800d74b408c806f5b5ea6e291e85568b152799feb2b75152de7f9fe` ;
- texte extrait avec mise en page : `4a11854f4ba541ca82948dec4acbec7046e0cf7e39ee3df9d0b69451604dc13d`.

## 6. Inspection visuelle

Le candidat complet a été rendu avec Poppler sur 49 pages réparties entre l’index du Livre IV, les 22 ouvertures de chapitre, un point intermédiaire de chaque chapitre, la fin du chapitre 22 et les transitions suivantes.

Pages inspectées : 2934, 2935, 2936, 2954, 2974, 2993, 3013, 3019, 3027, 3039, 3053, 3067, 3082, 3094, 3107, 3120, 3134, 3148, 3164, 3181, 3199, 3216, 3234, 3252, 3272, 3291, 3311, 3326, 3343, 3368, 3394, 3413, 3433, 3451, 3470, 3487, 3505, 3523, 3543, 3554, 3566, 3583, 3601, 3617, 3635, 3652, 3670, 3671 et 3672.

Un contrôle de parité Poppler/PDFium a porté sur les pages 2934, 2974, 3013, 3082, 3199, 3343, 3433, 3505, 3601, 3635, 3671 et 3672. Les différences observées se limitent à l’anticrénelage des contours de glyphes ; aucun déplacement, rognage, carré noir, glyphe absent ou changement de contenu n’a été observé.

Après passage de l’index à l’état `complete`, la tête finale a été réinspectée sur les pages 2934, 2935, 2974, 3433, 3505, 3635, 3670, 3671 et 3672. La pagination est restée à 3 672 pages et la différence textuelle avec le candidat se limite aux mentions de progression et de statut de l’index.

## 7. Artefacts de preuve

- candidat pré-clôture inspecté : run `30331157848`, artefact `8677476229`, digest `sha256:bc271ec2a2c6d4c4e8eda563139d19fc9c08d13208cc8ae97a59599e3722469c` ;
- tête lecteur définitive : run `30331869053`, artefact `8677727006`, digest `sha256:0109aa765694cee0c6cc2663e83a3310485e5915517e3c0c35fcb95b43ac59ce`.

Les artefacts contiennent le PDF, son texte extrait, les empreintes, les rapports `pdfinfo`, `pdffonts`, `qpdf`, le journal de build et le rapport transversal des chapitres.

## 8. Portes de qualité

| Porte | Résultat |
|---|---|
| 22 chapitres rédigés, repérés et audités | acceptée |
| ordre lecteur complet et QA interne exclue | acceptée |
| compilation PDF reproductible dans le runner documenté | acceptée |
| préflight structurel et polices | accepté |
| inspection visuelle représentative avec deux moteurs | acceptée |
| campagnes runtime, performance et plateformes | réservées |
| licence globale de collection | réservée |
| PDF balisé pour lecteurs d’écran | réservé |

## 9. Réserves

- la licence globale de la collection n’est pas définie et `LICENSE.md` reste absent ;
- `pdfinfo` indique `Tagged: no` : le PDF n’est pas présenté comme accessible aux lecteurs d’écran ;
- les exports, installations, plateformes, campagnes QA produit, performances, réseau, sauvegardes, restaurations, mises à jour et procédures de maintenance décrites par le Livre IV ne sont pas exécutés par cette campagne documentaire ;
- le PDF est un artefact de validation technique, pas une publication commerciale.

## 10. Conclusion

La rédaction, la validation documentaire, la compilation et l’inspection PDF du Livre IV sont closes. Le prochain jalon est le Livre V — **Encyclopédie technique et bibliothèque de référence**.
