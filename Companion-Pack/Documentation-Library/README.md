---
title: "Companion Pack — Documentation Library"
id: "CP-PACK-07-DOCUMENTATION-LIBRARY"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-30T12:34:03+02:00"
validation-status: "runtime-tested-linux"
redistribution-status: "global-policy-defined"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Documentation Library

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à comparer et **[LECTURE]** contenu à étudier.

Le Pack 7 fournit des patrons documentaires normalisés, des exemples fictifs remplis, des schémas et des scripts déterministes pour créer, contrôler et compiler de nouveaux documents sans dupliquer les chapitres propriétaires.

## État qualifié

| Élément | État |
|---|---|
| patrons documentaires | 13 validés |
| exemples remplis | 10 régénérés octet pour octet |
| schémas documentaires | 3 matérialisés |
| tests Python | 18 réussis |
| compilation Pandoc HTML | 9 documents réussis |
| preuve YAML générée | analysée avec PyYAML |
| validations transversales | réussies sans PDF |
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

Cette compilation vérifie la portabilité structurelle. Elle ne constitue pas une inspection visuelle ou d’accessibilité.

## Qualification obtenue

Le run `30535138371` a validé 57 fichiers du Pack, 13 patrons, 10 exemples remplis et 18 tests Python. Les dix exemples ont été régénérés octet pour octet ; les neuf documents Markdown ont été compilés vers HTML et la preuve YAML a été analysée.

Environnement : Ubuntu 24.04, CPython `3.12.13`, PyYAML `6.0.3` et Pandoc `3.1.3`. Artefact `8756322426`, digest `sha256:7d17cbbc5897f74130ef20420c33d5f68a9d483381027b549b2f558e14806933`.

L’arbre Git est resté propre. Aucun PDF, DOCX ou EPUB n’a été produit.

## Frontières

Le Volume 0 demeure normatif. Les Livres demeurent propriétaires de leurs explications. Le Pack ne modifie aucun index ni `contents.txt` automatiquement et ne transforme jamais un exemple rempli en preuve d’un document réel.

## Réserves

La qualification ne valide aucun rendu visuel, contrôle d’accessibilité, PDF, DOCX, EPUB, publication, licence globale ou redistribution autonome.
