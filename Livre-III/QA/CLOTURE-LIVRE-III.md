---
title: "Validation transversale et publication du Livre III"
id: "DOC-L3-QA-TRANSVERSE-PUBLICATION"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-25T14:46:00+02:00"
audit-level: "static-review+pdf-inspected"
validation-evidence: "Livre-III/QA/VALIDATION-PUBLICATION-LIVRE-III.yaml"
---

# Validation transversale et publication du Livre III

## 1. Périmètre

La campagne couvre les trente chapitres du Livre III, leurs rapports d’audit, les preuves finales, l’index du Livre, l’ordre de compilation, les liens et identifiants, les repères d’utilisation, les doublons, la chaîne Pandoc/XeLaTeX et le PDF cumulatif de la collection à l’état de clôture du Livre III.

Les audits, preuves YAML et protocoles QA restent versionnés dans le dépôt mais exclus de `contents.txt`. La preuve de publication conserve le nombre de pages, les empreintes, les identifiants GitHub Actions et les réserves globales sans injecter ces données internes dans le manuel lecteur.

## 2. Validation transversale

La validation confirme :

- trente chapitres déclarés et présents ;
- trente identifiants uniques ;
- trente rapports d’audit référencés et présents ;
- trente preuves finales contrôlées sans état `pending` ;
- trente chapitres du Livre III déclarés dans `contents.txt` ;
- zéro erreur transversale et zéro erreur bloquante dans le validateur documentaire ;
- zéro doublon de titre, bloc significatif ou paragraphe long ;
- zéro bloc sans repère d’utilisation et zéro incohérence sémantique de contexte ;
- absence des audits, preuves YAML et protocoles internes dans le texte extrait du PDF.

L’unique avertissement documentaire global reste l’absence de licence de collection.

## 3. Compilation Pandoc et XeLaTeX

La compilation utilise `build.sh`, `metadata.yaml`, `contents.txt`, le filtre Lua du dépôt, Pandoc et XeLaTeX. Le runner installe les familles DejaVu et Latin Modern ainsi que `librsvg2-bin` pour les ressources SVG.

Le PDF de contrôle contient 2910 pages A4 et 7384734 octets. Son empreinte SHA-256 est `7feb46d7c1d016c0377be1e9ed31735bf525ea35589ea07678417f03b90ea9a5`. L’empreinte du texte extrait est `33ccb0e4cc8680af5ba52040065c12e3571696d8a1c48393ae847f5bf2099ba7`.

## 4. Préflight PDF

Les contrôles ont confirmé :

- format A4 et rotation nulle ;
- PDF non chiffré, sans formulaire et sans JavaScript ;
- absence d’erreur de syntaxe ou de flux selon `qpdf --check` ;
- texte extractible avec `pdftotext` ;
- polices DejaVu et Latin Modern incorporées et sous-ensemblées ;
- métadonnées de titre et d’auteur présentes ;
- présence du chapitre 30 et absence du contenu QA interne.

## 5. Inspection visuelle

Une première campagne a produit l’artefact `8617767659` du run `30151432721`, digest `sha256:d940cd85dff27c0044d108f89f93ee1dc87019ad8fcb0d6c223f4164f32905d3` et PDF SHA-256 `4a09db4ea37764177d1f48b0e62b7276e6f8aaed912cfde0ab693171dcffa650`. Les pages suivantes ont été rendues et examinées : 1715, 1716, 1717, 1733, 1750, 1774, 1798, 1819, 1840, 1855, 1870, 1885, 1900, 1917, 1934, 1953, 1973, 1991, 2010, 2031, 2053, 2071, 2089, 2107, 2125, 2146, 2167, 2187, 2208, 2233, 2258, 2277, 2297, 2311, 2325, 2348, 2372, 2393, 2414, 2432, 2451, 2470, 2490, 2514, 2538, 2557, 2576, 2598, 2621, 2640, 2660, 2680, 2700, 2720, 2740, 2761, 2782, 2802, 2822, 2843, 2865, 2885, 2905, 2906, 2907, 2908, 2909, 2910.

Cette inspection couvre l’index du Livre III, les trente ouvertures de chapitre, une page intermédiaire de chaque chapitre, la fin du chapitre 30 et la transition vers les Livres IV, V et le Companion Pack. Aucun texte rogné, chevauchement, tableau hors page, rotation incorrecte, glyphe manquant ou carré noir n’a été retenu.

Le candidat produit par le run de clôture a été comparé à cette référence : son texte extrait possède la même empreinte et les vingt-cinq pages suivantes ont le même rendu PNG à 130 dpi : 1, 2, 3, 4, 5, 10, 20, 50, 363, 727, 1091, 1455, 1818, 2182, 2546, 2901, 2902, 2903, 2904, 2905, 2906, 2907, 2908, 2909, 2910. Cette équivalence ferme le risque de divergence entre le candidat inspecté et le candidat documenté avant la mise à jour finale de l’index.

## 6. Portes qualité

- [x] Q0 — intégrité, métadonnées et ordre de compilation ;
- [x] Q1 — conformité éditoriale et explication des blocs ;
- [x] Q2 — liens, identifiants, audits, preuves et frontières ;
- [x] Q3 — validation technique statique transversale ;
- [x] Q4 — sécurité documentaire et absence de contenu QA interne ;
- [x] Q5 — compilation Pandoc/XeLaTeX, préflight et inspection visuelle.

## 7. Décision

**Livre III accepté pour publication technique avec réserves globales de collection.**

Les réserves propres à la construction PDF de fin du Livre III sont closes. Le Livre IV peut commencer selon son plan maître après réussite de la compilation finale de la tête de clôture.

## 8. Réserves globales et runtime

Trois réserves restent ouvertes :

1. aucune licence globale de collection n’est définie et `LICENSE.md` est absent ;
2. le PDF n’est pas balisé pour les lecteurs d’écran (`Tagged: no`) ;
3. les assets, pilotes Blender, ComfyUI, Godot, revues humaines et benchmarks décrits au Livre III ne sont pas matérialisés par cette campagne documentaire.

Le run de publication documenté est `30158411470` sur la tête `6eedc5c89876f7e8781487168d5c78c8f33b4979`. L’artefact `8619594813` porte le digest `8ae34f6e2b6ed7b41e33c8bce7155f03c6d739b1450e8dd7027965d95b6abdbc`. URL d’artefact enregistrée par GitHub Actions : `https://github.com/LaurentCOLL1/Guide-IA-GameDev/actions/runs/30158411470/artifacts/8619594813`.
