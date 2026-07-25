---
title: "Validation transversale et publication du Livre III"
id: "DOC-L3-QA-TRANSVERSE-PUBLICATION"
status: "complete"
version: "1.0.1"
lang: "fr-FR"
last-verified: "2026-07-25T14:52:59+02:00"
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

Le PDF final de la tête de clôture contient 2 910 pages A4 et 7 384 815 octets. Son empreinte SHA-256 est `bc1bd50e9d63be7d65d792043354adaa750d7a5f9f9c86a3d0320c6a64f3f055`. L’empreinte du texte extrait avec conservation de la mise en page est `78e4455db1618b1ff402a71c65e309805927f4d334464b851589c719451535f4`.

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

Une première campagne a produit l’artefact `8617767659` du run `30151432721`, digest `sha256:d940cd85dff27c0044d108f89f93ee1dc87019ad8fcb0d6c223f4164f32905d3` et PDF SHA-256 `4a09db4ea37764177d1f48b0e62b7276e6f8aaed912cfde0ab693171dcffa650`. Soixante-huit pages ont été rendues et examinées : l’index du Livre III, les trente ouvertures de chapitre, une page intermédiaire de chaque chapitre, la fin du chapitre 30 et la transition vers les Livres IV, V et le Companion Pack.

Le candidat de préclôture a reproduit à l’identique le texte extrait et vingt-cinq rendus PNG de référence à 130 dpi. Après passage de l’index et de la gouvernance à l’état terminé, la tête `4ed21f950f9c29f16c63d6527c0528a8d86ef184` a été recompilée par le run `30158547181`. Les pages 1715, 1716, 1717, 1733, 1819, 2187, 2865 et 2905 à 2910 ont été rendues et examinées sur cet artefact final.

Aucun texte rogné, chevauchement, tableau hors page, rotation incorrecte, glyphe manquant ou carré noir n’a été retenu. Les titres longs se replient dans les marges et les blocs de code observés restent lisibles.

## 6. Portes qualité

- [x] Q0 — intégrité, métadonnées et ordre de compilation ;
- [x] Q1 — conformité éditoriale et explication des blocs ;
- [x] Q2 — liens, identifiants, audits, preuves et frontières ;
- [x] Q3 — validation technique statique transversale ;
- [x] Q4 — sécurité documentaire et absence de contenu QA interne ;
- [x] Q5 — compilation Pandoc/XeLaTeX, préflight et inspection visuelle de la tête finale.

## 7. Décision

**Livre III accepté pour publication technique avec réserves globales de collection.**

Les réserves propres à la construction PDF de fin du Livre III sont closes. Le Livre IV peut commencer selon son plan maître.

## 8. Réserves globales et runtime

Trois réserves restent ouvertes :

1. aucune licence globale de collection n’est définie et `LICENSE.md` est absent ;
2. le PDF n’est pas balisé pour les lecteurs d’écran (`Tagged: no`) ;
3. les assets, pilotes Blender, ComfyUI, Godot, revues humaines et benchmarks décrits au Livre III ne sont pas matérialisés par cette campagne documentaire.

Le run final de publication est `30158547181` sur la tête `4ed21f950f9c29f16c63d6527c0528a8d86ef184`. L’artefact `8619626083` porte le digest `sha256:c47950160abcaca333915fbe25de3f96384259f4542dae85e7cedaf740053ce7`. La validation permanente sans PDF a réussi dans le run `30158547192`.
