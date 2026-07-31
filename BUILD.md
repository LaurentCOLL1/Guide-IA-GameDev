---
title: "Construire les publications"
id: "DOC-BUILD-PUBLICATIONS"
status: "active"
version: "2.0.0"
lang: "fr-FR"
last-updated: "2026-07-30T23:04:00+02:00"
license: "CC-BY-SA-4.0"
---

# Construire les publications

## Sorties techniques

La chaîne commune génère dans `dist/publications/` :

- `Guide-IA-GameDev.pdf` — PDF A4 produit avec XeLaTeX ;
- `Guide-IA-GameDev.html` — document HTML autonome avec ressources embarquées ;
- `Guide-IA-GameDev.epub` — livre numérique EPUB 3 ;
- `publication-manifest.json` — tailles, empreintes SHA-256, ordre des sources et statut de diffusion.

Ces sorties sont des **builds techniques**, pas une publication officielle ni une release.

## Prérequis

- Python 3.12 ou version compatible ;
- Pandoc ;
- XeLaTeX pour le PDF ;
- `pdfinfo` et `pdftotext` pour la validation PDF.

Sous Ubuntu, le workflow installe Pandoc, TeX Live, les polices DejaVu et Poppler. Sous Windows, MiKTeX ou TeX Live peut fournir XeLaTeX.

## Construction complète

### Windows PowerShell

```powershell
./build.ps1
```

### Linux ou macOS

```bash
chmod +x build.sh
./build.sh
```

## Construction ciblée

```bash
python tools/build_publications.py --clean --formats html epub
python tools/validate_publications.py --report dist/publications/validation.json
```

Les valeurs autorisées pour `--formats` sont `pdf`, `html` et `epub`.

## Ordre et métadonnées

`contents.txt` définit l’ordre officiel des sources. `metadata.yaml` fournit le titre, l’auteur, la langue, les polices et la licence. Les scripts refusent toute source absente.

Les trois formats embarquent ou déclarent la licence éditoriale `CC-BY-SA-4.0`. Les scripts et outils de construction restent sous MIT conformément à `LICENSE.md` et à la matrice de licence.

## Contrôles automatiques

La validation vérifie notamment :

- l’existence et la taille minimale des trois sorties ;
- le nombre de pages et le texte des premières pages du PDF ;
- la structure autonome, le titre, la table des matières et la licence du HTML ;
- le conteneur ZIP, le mimetype, le paquet OPF et la licence de l’EPUB ;
- la concordance des SHA-256 avec le manifeste ;
- le statut `technical-build-not-official-release` ;
- les validations documentaires et de licence du dépôt ;
- l’absence de mutation des sources versionnées.

## Reproductibilité

Le workflow fixe `SOURCE_DATE_EPOCH` et enregistre les versions d’outils ainsi que les SHA-256. La chaîne vise une reconstruction traçable, mais ne revendique pas encore une identité byte pour byte entre systèmes, versions de Pandoc ou moteurs TeX différents.

## Dépannage

- **Pandoc absent** : vérifier son installation et le `PATH`.
- **XeLaTeX absent** : installer MiKTeX ou TeX Live.
- **Police absente** : installer DejaVu ou adapter `metadata.yaml`.
- **Ressource introuvable** : vérifier son chemin relatif depuis la racine.
- **EPUB invalide** : inspecter `validation.json` et le contenu ZIP.
- **PDF trop court ou texte absent** : consulter les journaux XeLaTeX et `pdfinfo`.

## Règle de publication

Le Markdown reste la source de vérité. Les PDF, HTML et EPUB sont générés, jamais modifiés manuellement. Une publication officielle ou une release doit faire l’objet d’un lot séparé avec contrôle d’accessibilité, attribution, archives et approbation explicite.
