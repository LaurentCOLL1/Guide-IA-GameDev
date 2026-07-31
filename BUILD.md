---
title: "Construire les publications"
id: "DOC-BUILD-PUBLICATIONS"
status: "active"
version: "2.1.0"
lang: "fr-FR"
last-updated: "2026-07-31T03:40:00+02:00"
license: "CC-BY-SA-4.0"
---

# Construire les publications

## Sorties techniques

La chaîne commune génère dans `dist/publications/` :

- `Guide-IA-GameDev.pdf` — PDF A4 visuel produit avec XeLaTeX ;
- `Guide-IA-GameDev.html` — document HTML autonome avec ressources embarquées ;
- `Guide-IA-GameDev.epub` — livre numérique EPUB 3 ;
- `publication-manifest.json` — tailles, empreintes SHA-256, ordre des sources et statut de diffusion.

Une chaîne séparée génère :

- `Guide-IA-GameDev-accessible.pdf` — candidat PDF balisé PDF/UA-2 produit avec LuaLaTeX ;
- `accessible-pdf-manifest.json` — outil conteneurisé, taille, empreinte, langue et profil candidat ;
- `accessible-pdf-validation.json` et `verapdf-ua2-report.json` — contrôles structurels et rapport PDF/UA vérifiable par machine.

Ces sorties sont des **builds techniques**, pas une publication officielle ni une release. Le PDF balisé ne remplace pas le PDF visuel historique.

## Prérequis de la chaîne visuelle et numérique

- Python 3.12 ou version compatible ;
- Pandoc ;
- XeLaTeX pour le PDF visuel ;
- `pdfinfo` et `pdftotext` pour la validation PDF.

Sous Ubuntu, le workflow installe Pandoc, TeX Live, les polices DejaVu et Poppler. Sous Windows, MiKTeX ou TeX Live peut fournir XeLaTeX.

## Prérequis du PDF balisé

- Python 3.12 ou version compatible ;
- Docker ;
- Poppler (`pdfinfo`, `pdftotext`) ;
- qpdf.

La construction utilise l’image versionnée `pandoc/latex:3.10.0.0-ubuntu`, associée à TeX Live 2026, et la validation utilise `verapdf/cli:v1.30.2`. Le build est exécuté sans réseau après téléchargement des images. Les tags et digests effectifs sont enregistrés dans les preuves CI.

## Construction complète classique

### Windows PowerShell

```powershell
./build.ps1
```

### Linux ou macOS

```bash
chmod +x build.sh
./build.sh
```

## Construction ciblée classique

```bash
python tools/build_publications.py --clean --formats html epub
python tools/validate_publications.py --report dist/publications/validation.json
```

Les valeurs autorisées pour `--formats` restent `pdf`, `html` et `epub`.

## Construction du PDF balisé

### Windows PowerShell

```powershell
./build-accessible.ps1
```

### Linux ou macOS

```bash
chmod +x build-accessible.sh
./build-accessible.sh
```

Commandes détaillées :

```bash
python tools/build_accessible_pdf.py --clean --pull
python tools/validate_accessible_pdf.py \
  --report dist/publications/accessible-pdf-validation.json
```

`metadata-accessible-pdf.yaml` isole les métadonnées nécessaires au PDF balisé et évite les personnalisations de table des matières qui ne sont pas encore qualifiées avec le balisage LaTeX.

## Ordre et métadonnées

`contents.txt` définit l’ordre officiel des sources. `metadata.yaml` fournit les métadonnées de la chaîne classique ; `metadata-accessible-pdf.yaml` fournit le titre, l’auteur, la langue française et le profil `ua-2` de la chaîne balisée. Les scripts refusent toute source absente.

Tous les formats embarquent ou déclarent la licence éditoriale `CC-BY-SA-4.0`. Les scripts et outils de construction restent sous MIT conformément à `LICENSE.md` et à la matrice de licence.

## Contrôles automatiques classiques

La validation vérifie notamment :

- l’existence et la taille minimale des trois sorties ;
- le nombre de pages et le texte des premières pages du PDF visuel ;
- la structure autonome, le titre, la table des matières et la licence du HTML ;
- le conteneur ZIP, le mimetype, le paquet OPF et la licence de l’EPUB ;
- la concordance des SHA-256 avec le manifeste ;
- le statut `technical-build-not-official-release` ;
- les validations documentaires et de licence du dépôt ;
- l’absence de mutation des sources versionnées.

## Contrôles automatiques du PDF balisé

La validation dédiée vérifie notamment :

- la déclaration `Tagged: yes` de Poppler ;
- le nombre de pages, le titre et le texte extractible ;
- `StructTreeRoot`, `MarkInfo`, `Marked true`, la langue `fr-FR`, l’affichage du titre et l’identifiant PDF/UA ;
- l’intégrité qpdf ;
- les alternatives textuelles non vides pour les images Markdown et HTML du corpus ;
- la concordance du manifeste et du SHA-256 ;
- le profil PDF/UA-2 avec veraPDF ;
- l’état Git propre après génération.

veraPDF couvre les exigences PDF/UA vérifiables par machine. L’ordre de lecture complet, la pertinence des alternatives, la navigation dans les structures complexes et l’interopérabilité avec les lecteurs d’écran restent des contrôles humains distincts avant toute revendication complète.

## Reproductibilité

Les workflows fixent `SOURCE_DATE_EPOCH`, utilisent des images versionnées et enregistrent les versions, digests d’images et SHA-256. La chaîne vise une reconstruction traçable, mais ne revendique pas une identité byte pour byte entre systèmes, versions d’outils ou architectures.

## Dépannage

- **Pandoc absent** : vérifier son installation et le `PATH`.
- **XeLaTeX absent** : installer MiKTeX ou TeX Live.
- **Docker absent** : installer Docker avant d’utiliser la chaîne balisée.
- **Image conteneur indisponible** : exécuter le wrapper avec accès réseau afin de télécharger les deux images versionnées.
- **Police absente** : installer DejaVu ou adapter le fichier de métadonnées concerné.
- **Ressource introuvable** : vérifier son chemin relatif depuis la racine.
- **EPUB invalide** : inspecter `validation.json` et le contenu ZIP.
- **PDF visuel trop court ou texte absent** : consulter les journaux XeLaTeX et `pdfinfo`.
- **PDF balisé refusé** : inspecter `accessible-pdf-validation.json`, `verapdf-ua2-report.json` et la structure qpdf avant toute correction.

## Règle de publication

Le Markdown reste la source de vérité. Les PDF, HTML et EPUB sont générés, jamais modifiés manuellement. Une publication officielle ou une release doit faire l’objet d’un lot séparé avec attribution, archives, contrôle humain d’accessibilité et approbation explicite.
