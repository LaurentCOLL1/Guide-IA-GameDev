---
title: "Companion Pack — Documentation Library"
id: "CP-PACK-07-DOCUMENTATION-LIBRARY"
status: "candidate"
version: "1.0.0"
lang: "fr-FR"
validation-status: "candidate-runtime"
redistribution-status: "pending-global-license"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Documentation Library

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à comparer et **[LECTURE]** contenu à étudier.

Le Pack 7 fournit des patrons documentaires normalisés, des exemples fictifs remplis, des schémas et des scripts déterministes pour créer, contrôler et compiler de nouveaux documents sans dupliquer les chapitres propriétaires.

## État candidat

| Élément | État |
|---|---|
| patrons documentaires | 13 |
| exemples remplis | 10 |
| génération déterministe | à qualifier en CI |
| compilation Pandoc HTML | à qualifier en CI |
| PDF | non produit |
| licence globale | non décidée |

## Utilisation minimale

> **[PS] PowerShell — Exécuter depuis la racine du dépôt :**

```powershell
python .\Companion-Pack\Documentation-Library\scripts\generate_document.py `
  --root .\Companion-Pack\Documentation-Library `
  --template templates\chapters\tutorial.md `
  --data examples\data\chapter.json `
  --output dist\CHAPITRE-99.md
```

Le générateur refuse les tokens manquants, les valeurs inutilisées et les placeholders restants.

## Validation locale

```powershell
python .\Companion-Pack\Documentation-Library\scripts\validate_documentation_library.py

python -m unittest discover `
  -s .\Companion-Pack\Documentation-Library\tests `
  -v
```

## Compilation de contrôle

```powershell
pandoc .\dist\CHAPITRE-99.md --from markdown --to html --standalone `
  --output .\dist\CHAPITRE-99.html
```

Cette compilation vérifie la portabilité structurelle. Elle ne constitue pas une inspection PDF, HTML visuelle ou d’accessibilité.

## Frontières

Le Volume 0 demeure normatif. Les Livres demeurent propriétaires de leurs explications. Le Pack ne modifie aucun index ni `contents.txt` automatiquement.

## Réserves

Le candidat ne valide encore ni compilation CI, ni rendu visuel, ni PDF, DOCX ou EPUB, ni accessibilité, ni publication, ni redistribution autonome.
