---
title: "Clôture technique et PDF — Livre V"
id: "DOC-L5-QA-CLOSURE"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-30T03:00:00+02:00"
audit-level: "static-review+pdf-inspected"
target-book: "Livre V"
---

# Clôture technique et PDF — Livre V

## 1. Décision

La publication technique du Livre V est **acceptée au niveau `static-review+pdf-inspected`**. Les 26 fiches sont présentes dans le PDF cumulatif, les validations documentaires sont vertes, le préflight structurel est réussi et l’échantillon visuel ne révèle ni texte coupé, ni chevauchement, ni glyphe cassé, ni page anormalement vide.

Cette décision porte sur le document lecteur et sa chaîne de publication. Elle ne constitue ni une validation runtime du projet, ni une décision de licence globale, ni une publication commerciale.

## 2. Corpus et chaîne

- corpus lecteur : 145 sources déclarées par `contents.txt` ;
- Livre V : `Livre-V/index.md` et 26 fiches ;
- construction : `build.sh` → Pandoc → XeLaTeX → `dist/Guide-IA-GameDev.pdf` ;
- préflight : `qpdf`, `pdfinfo`, `pdffonts` et `pdftotext` ;
- inspection : Poppler et PDFium ;
- QA internes, audits, preuves et protocoles : exclus du PDF lecteur.

## 3. Corrections nécessaires à la compilation

Deux défauts de chaîne ont été corrigés sans modifier le contenu sémantique :

1. dans la fiche 05, deux séparateurs `---` immédiatement suivis d’un marqueur `l5:card` ont reçu la ligne vide attendue afin que Pandoc ne les interprète pas comme des blocs YAML ;
2. le runner de compilation a installé explicitement le paquet `lmodern`, requis par la chaîne XeLaTeX.

Le diagnostic Pandoc par source a ensuite confirmé que les 145 documents lecteur sont parsables indépendamment.

## 4. Validations automatisées

| Contrôle | Résultat |
|---|---|
| structure, métadonnées, liens et doublons | réussi |
| cartes et liens profonds du Livre V | réussi |
| explications structurées du code | réussi |
| repères d’utilisation et cohérence sémantique | réussi |
| couverture des contextes | mesurée sans erreur bloquante |
| compilation Pandoc/XeLaTeX | réussie |
| présence de l’index et des 26 titres du Livre V | réussie |
| exclusion des contenus QA internes | réussie |
| `qpdf --check` | aucune erreur de syntaxe ou de flux |
| polices | incorporées et sous-ensemblées ; aucun Type 3 ou type inconnu |
| texte extractible | oui |

## 5. Caractéristiques du PDF

| Propriété | Valeur |
|---|---|
| fichier | `dist/Guide-IA-GameDev.pdf` |
| pages | 4063 |
| taille | 10462788 octets |
| format | A4, 595,28 × 841,89 points |
| version PDF | 1.5 |
| chiffrement | non |
| linéarisation | non |
| texte extractible | oui |
| PDF balisé | non |
| champs de formulaire | 0 |
| pièces jointes | 0 |
| éléments de plan | 7 204 |
| annotations et liens | 11 060 |

## 6. Cartographie du Livre V

- index du Livre V : page 3 681 ;
- fiche 01 : page 3 683 ;
- fiche 26 : page 4 048 ;
- dernière page du Livre V : page 4 062 ;
- entrée du Companion Pack : page 4 063.

Le fichier `LIVRE-V-PAGE-MAP.json` de l’artefact conserve les ouvertures des 26 fiches, leurs occurrences textuelles, les 82 pages d’échantillon et les pages de parité.

## 7. Inspection visuelle

### Poppler

**82 pages** ont été rendues et inspectées : index, ouverture, deuxième page et page intermédiaire de chaque fiche lorsque disponible, dernière page du Livre V et première page du Companion Pack.

### PDFium

**8 pages** ont été rendues avec PDFium et comparées à Poppler : 3 681, 3 683, 3 758, 3 862, 3 967, 4 048, 4 062 et 4 063.

### Conclusion visuelle

- hiérarchie des titres cohérente ;
- tableaux contenus dans la page ;
- liens et code lisibles ;
- aucun chevauchement ou rognage observé ;
- aucun carré noir, glyphe absent ou corruption de police observé ;
- mêmes contenus, sauts de ligne et limites de pages avec les deux moteurs ;
- seules les différences normales d’anticrénelage raster subsistent.

## 8. Intégrité et artefact

- workflow : `Livre V PDF Closure Runner V2` ;
- run : `30503741584` ;
- commit source : `28ff5ad6e952d45b5cfebb53237197e7177d1e94` ;
- artefact : `8744567647` ;
- digest de l’artefact : `sha256:b8300a8a449b89606f9a1b80551454d17f3205bb8f1131451676fc514a4ff221` ;
- SHA-256 du PDF : `008ae82f759f562178b810e87abbd08c0e00bf6dd6eba4afeb5334748feda8a3` ;
- SHA-256 du texte extrait : `6734cb86d214264e55b0f2ef188be73c55ccfed050c9374d43cde37ad6e58df5` ;
- finalisation de gouvernance : run `30504686403`.

## 9. Réserves

- la licence globale de la collection reste indécise ;
- le PDF n’est pas qualifié comme document balisé pour lecteurs d’écran ;
- les formats HTML et EPUB ne sont pas produits par cette campagne ;
- aucune procédure runtime, plateforme, performance, sécurité produit, restauration ou publication commerciale n’est validée ici ;
- le Starter Kit et les autres ressources du Companion Pack ne sont pas encore matérialisés.

## 10. Porte suivante

M6 — Livre V est terminé. Le jalon actif devient **M7 — Companion Pack**, avec le **Pack 1 — Starter Kit** comme prochaine action. Son point d’entrée canonique à créer est `Companion-Pack/Starter-Kit/README.md`.
