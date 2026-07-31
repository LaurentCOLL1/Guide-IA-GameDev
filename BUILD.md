---
title: "Construire les publications"
id: "DOC-BUILD-PUBLICATIONS"
status: "active"
version: "2.1.0"
lang: "fr-FR"
last-updated: "2026-07-31T16:34:00+02:00"
license: "CC-BY-SA-4.0"
---

# Construire les publications

## Sorties techniques

### Chaîne multiformat

La chaîne commune génère dans `dist/publications/` :

- `Guide-IA-GameDev.pdf` — PDF A4 produit avec XeLaTeX ;
- `Guide-IA-GameDev.html` — document HTML autonome avec ressources embarquées ;
- `Guide-IA-GameDev.epub` — livre numérique EPUB 3 ;
- `publication-manifest.json` — tailles, empreintes SHA-256, ordre des sources et statut de diffusion.

### Chaîne PDF balisé

La chaîne d’accessibilité génère séparément dans `dist/accessible-pdf/` :

- `Guide-IA-GameDev-tagged.pdf` — candidat technique balisé produit avec LuaLaTeX ;
- `accessible-pdf-manifest.json` — taille, empreinte SHA-256, cible PDF/UA-1 et revendication bornée ;
- `validation.json` — contrôles de structure, métadonnées, intégrité, sources et diagnostic veraPDF ;
- `verapdf-ua1.xml` et `verapdf.log` — diagnostic machine PDF/UA-1 conservé sans transformation ;
- les versions d’outils, digests d’images et sommes de contrôle nécessaires à la traçabilité.

Ces sorties sont des **builds techniques**, pas une publication officielle, une certification d’accessibilité ni une release.

## Source et ordre de lecture

`contents.txt` définit l’ordre officiel des 162 sources. `metadata.yaml` fournit le titre, l’auteur, la langue, les polices et la licence. Les scripts refusent toute source absente.

Les formats embarquent ou déclarent la licence éditoriale `CC-BY-SA-4.0`. Les scripts et outils de construction restent sous MIT conformément à `LICENSE.md` et à la matrice de licence.

## Chaîne multiformat

### Prérequis

- Python 3.12 ou version compatible ;
- Pandoc ;
- XeLaTeX pour le PDF ;
- `pdfinfo` et `pdftotext` pour la validation PDF.

Sous Ubuntu, le workflow installe Pandoc, TeX Live, les polices DejaVu et Poppler. Sous Windows, MiKTeX ou TeX Live peut fournir XeLaTeX.

### Construction complète

#### Windows PowerShell

```powershell
./build.ps1
```

#### Linux ou macOS

```bash
chmod +x build.sh
./build.sh
```

### Construction ciblée

```bash
python tools/build_publications.py --clean --formats html epub
python tools/validate_publications.py --report dist/publications/validation.json
```

Les valeurs autorisées pour `--formats` sont `pdf`, `html` et `epub`.

### Contrôles automatiques

La validation vérifie notamment :

- l’existence et la taille minimale des trois sorties ;
- le nombre de pages et le texte des premières pages du PDF ;
- la structure autonome, le titre, la table des matières et la licence du HTML ;
- le conteneur ZIP, le mimetype, le paquet OPF et la licence de l’EPUB ;
- la concordance des SHA-256 avec le manifeste ;
- le statut `technical-build-not-official-release` ;
- les validations documentaires et de licence du dépôt ;
- l’absence de mutation des sources versionnées.

## Chaîne PDF balisé

### Environnement de référence

La qualification de référence s’exécute dans GitHub Actions avec :

- Ubuntu 24.04 ;
- une image TeX Live 2026 épinglée par digest ;
- Pandoc 3.10 dans cette image ;
- LuaLaTeX et l’interface `\DocumentMetadata` du projet LaTeX Tagged PDF ;
- `qpdf`, `pdfinfo` et `pdftotext` sur l’hôte ;
- veraPDF 1.30.2 dans une image épinglée par digest.

L’image TeX complète est volumineuse et le document dépasse 4 000 pages. La construction locale n’est donc pas présentée comme équivalente tant que les versions et digests ne correspondent pas à ceux enregistrés par le workflow.

### Construction technique

Dans un environnement possédant Pandoc, LuaLaTeX, les polices et paquets TeX nécessaires :

```bash
python tools/build_accessible_pdf.py --clean
```

Le script :

1. lit les 162 chemins de `contents.txt` ;
2. place `\DocumentMetadata` avant `\documentclass` ;
3. déclare la langue `fr-FR` et la cible PDF/UA-1 ;
4. applique le filtre de normalisation de publication ;
5. construit le PDF avec LuaLaTeX ;
6. écrit un manifeste incluant taille et SHA-256.

La commande ne certifie pas le résultat. Elle produit un candidat qui doit ensuite franchir les portes de validation.

### Diagnostic veraPDF

Le workflow exécute le profil `ua1` de veraPDF dans un conteneur sans réseau et conserve le XML intégral. Le validateur du dépôt reçoit ensuite ce rapport :

```bash
python tools/validate_accessible_pdf.py \
  --report dist/accessible-pdf/validation.json \
  --verapdf-report dist/accessible-pdf/verapdf-ua1.xml
```

Une absence ou une impossibilité d’analyser le rapport est bloquante. Une non-conformité veraPDF est enregistrée comme réserve à corriger ou à justifier ; elle n’est jamais transformée en réussite PDF/UA.

### Contrôles automatiques

La porte machine vérifie notamment :

- l’intégrité syntaxique avec `qpdf` ;
- `Tagged: yes` dans `pdfinfo` ;
- `/MarkInfo`, `/Marked true`, `/StructTreeRoot` et `/Lang` dans le catalogue ;
- le titre, l’auteur et une pagination plausible ;
- la concordance de la taille et du SHA-256 avec le manifeste ;
- les 162 sources et l’ordre `contents.txt` ;
- l’absence d’image Markdown ou HTML sans alternative textuelle dans les sources destinées au lecteur ;
- la présence et l’analyse du rapport veraPDF ;
- les validations documentaires et de licence ;
- l’absence de sortie générée suivie par Git.

### Revendication bornée

Le manifeste et le rapport utilisent :

```text
tagged-pdf-machine-checked-not-full-pdfua-conformance
```

Cette formulation signifie uniquement que le PDF possède une structure balisée contrôlée par la machine et qu’un diagnostic PDF/UA a été exécuté. Elle ne signifie pas :

- certification PDF/UA ;
- conformité exhaustive au protocole Matterhorn ;
- compatibilité garantie avec tous les lecteurs d’écran ;
- validation humaine de chaque page, tableau, lien, note, bloc de code ou formule.

### Contrôles humains

Avant toute publication officielle, un échantillon représentatif doit couvrir :

- ordre de lecture et navigation par titres ;
- listes, tableaux, liens et notes ;
- code, sorties terminal et formules ;
- pertinence des alternatives textuelles ;
- comparaison visuelle avec le PDF classique ;
- comportement avec au moins un lecteur d’écran réel.

Les contrôles réellement exécutés sont consignés dans `QA/AUDIT-ACCESSIBLE-PDF.md` et `QA/VALIDATION-ACCESSIBLE-PDF.yaml`. Les contrôles non exécutés restent des réserves explicites.

## Reproductibilité

Les workflows fixent `SOURCE_DATE_EPOCH` et enregistrent versions, digests et SHA-256. Les images de construction du PDF balisé sont épinglées par digest.

La chaîne vise une reconstruction traçable, mais ne revendique pas une identité byte pour byte entre systèmes, images de runner, versions de Pandoc ou moteurs TeX différents. La stabilité utile se contrôle séparément par pagination, extraction textuelle, échantillons visuels et manifestes.

## Dépannage

- **Pandoc absent** : vérifier son installation et le `PATH`.
- **XeLaTeX absent** : installer MiKTeX ou TeX Live pour la chaîne multiformat.
- **LuaLaTeX ou paquet de balisage absent** : utiliser l’image TeX Live épinglée par le workflow accessible.
- **Capacité TeX dépassée** : conserver les options Web2C bornées du script accessible ; ne pas modifier globalement l’installation.
- **Police absente** : installer DejaVu ou adapter `metadata.yaml`.
- **Ressource introuvable** : vérifier son chemin relatif depuis la racine.
- **EPUB invalide** : inspecter `validation.json` et le contenu ZIP.
- **PDF trop court ou texte absent** : consulter les journaux TeX, `pdfinfo` et `pdftotext`.
- **veraPDF absent ou mutable** : utiliser l’image et le digest enregistrés dans le workflow.
- **veraPDF non conforme** : lire `verapdf-ua1.xml`, qualifier chaque échec et conserver la réserve tant qu’elle n’est pas corrigée.
- **Ordre de lecture incorrect** : ne pas corriger seulement l’apparence ; inspecter l’arbre de structure et la source correspondante.

## Règle de publication

Le Markdown reste la source de vérité. Les PDF, HTML et EPUB sont générés, jamais modifiés manuellement.

Une publication officielle ou une release doit faire l’objet d’un lot séparé avec contrôle humain d’accessibilité, attribution, archives, décision sur les réserves et approbation explicite.
