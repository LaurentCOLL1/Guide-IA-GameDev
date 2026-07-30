# Construire les publications

## Prérequis

### Obligatoires

- Git ;
- Python 3.12 ou version compatible ;
- Pandoc ;
- une distribution LaTeX avec XeLaTeX pour le PDF : MiKTeX sous Windows ou TeX Live sous Linux.

### Contrôles de qualification

La campagne CI ajoute également :

- `qpdf` et les outils Poppler pour le PDF ;
- Java et EPUBCheck 5.3.0 pour l’EPUB ;
- PyYAML pour les validations documentaires transversales.

## Vérifier les outils principaux

```bash
python3 --version
pandoc --version
xelatex --version
```

## Construire les trois formats

### Windows PowerShell

```powershell
./build.ps1
```

### Linux ou macOS

```bash
chmod +x build.sh
./build.sh
```

Les fichiers générés sont placés dans `dist/publication/` :

- `Guide-IA-GameDev.pdf` ;
- `Guide-IA-GameDev.html` ;
- `Guide-IA-GameDev.epub` ;
- `publication-manifest.json` ;
- `SHA256SUMS`.

## Construire un sous-ensemble de formats

```bash
./build.sh --formats html epub
./build.sh --formats pdf
```

Sous PowerShell, les mêmes options sont transmises au script Python :

```powershell
./build.ps1 --formats html epub
```

## Ordre et métadonnées des sources

`contents.txt` définit l’ordre officiel de compilation. Une ligne vide ou commençant par `#` est ignorée.

Les métadonnées sont fusionnées dans cet ordre :

1. `metadata.yaml` — collection et chaîne PDF ;
2. `publication/metadata.yaml` — identifiant, droits et description des exports.

Le filtre `filters/pdf-normalize.lua` applique la normalisation du document lecteur aux trois formats. La feuille `publication/style.css` est incorporée au HTML autonome et incluse dans l’EPUB.

## Construction directe

```bash
python3 tools/build_publications.py --root . --dist dist/publication
```

Le script :

- contrôle l’existence de toutes les sources ;
- produit PDF, HTML5 autonome et EPUB 3 depuis la même liste ;
- fixe `SOURCE_DATE_EPOCH` lorsqu’il n’est pas fourni ;
- enregistre la taille et le SHA-256 de chaque source et de chaque sortie.

## Validation technique

La validation complète est exécutée par `.github/workflows/build-publications.yml`. Elle vérifie notamment :

- le préflight et les polices du PDF ;
- le titre, la langue, la table des matières et les ancres HTML ;
- le conteneur EPUB et EPUBCheck ;
- la présence des mentions de licence ;
- l’absence des anciens marqueurs de licence en attente ;
- l’intégrité Git et les validations documentaires transversales.

## Dépannage

- **`pandoc` introuvable** : vérifier le `PATH` ;
- **`xelatex` introuvable** : installer MiKTeX ou TeX Live ;
- **police absente** : installer DejaVu et Latin Modern ou adapter `metadata.yaml` ;
- **lien ou image manquante** : vérifier les chemins relatifs depuis la racine ;
- **EPUBCheck échoue** : lire le rapport de validation contenu dans l’artefact CI.

## Règle de publication

Le Markdown est la source de vérité. Les PDF, pages HTML et EPUB sont des artefacts générés et ne doivent pas être modifiés manuellement. Leur présence dans un artefact CI ne constitue pas une release ni une publication officielle.
