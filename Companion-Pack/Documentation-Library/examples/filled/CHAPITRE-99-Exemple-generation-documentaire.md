---
title: "Chapitre 99 — Générer une fiche documentaire reproductible"
id: "DOC-L2-CH99"
status: "validated"
version: "1.0.0"
lang: "fr-FR"
date: "2026-07-30"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Chapitre 99 — Générer une fiche documentaire reproductible

> **Repères d’utilisation :** **[PS]** PowerShell, **[CMD]** Invite de commandes, **[WSL]** terminal Linux sous Windows, **[DCT]** terminal d’un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à comparer et **[LECTURE]** contenu à étudier.

## 1. Objectif

Créer un document Markdown identifié, vérifiable et compilable à partir d’un patron versionné.

## 2. Public et prérequis

**Public :** auteur technique débutant à intermédiaire

**Prérequis :**

- Python 3.10 ou supérieur ;
- accès en lecture au Pack 7 ;
- Pandoc pour la compilation de contrôle.

## 3. Priorité et modes

- priorité : **Recommandé** ;
- Mode Solo : génération locale d’un document ;
- Mode Studio : génération intégrée à une revue de branche.

## 4. Concepts essentiels

Le patron définit la structure. Le profil JSON fournit uniquement les valeurs propres au document. La génération refuse tout placeholder non résolu.

## 5. Procédure

1. copier un profil d’exemple ;
2. remplacer l’identifiant et les contenus ;
3. lancer le générateur ;
4. exécuter le validateur ;
5. compiler le Markdown vers HTML avec Pandoc.

## 6. Exemple minimal

> **[PS] PowerShell — Exécuter depuis la racine du dépôt :**

```powershell
python .\Companion-Pack\Documentation-Library\scripts\generate_document.py `
  --template .\Companion-Pack\Documentation-Library\templates\chapters\tutorial.md `
  --data .\Companion-Pack\Documentation-Library\examples\data\chapter.json `
  --output .\dist\documentation\CHAPITRE-99.md
```

## 7. Résultat attendu et vérification

Le fichier généré ne contient aucun token `{{...}}`, possède un seul titre de niveau 1 et peut être converti vers HTML.

## 8. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

**Erreur :** modifier directement le patron pour un seul chapitre.

**Correction :** conserver le patron générique et placer les valeurs spécifiques dans le profil JSON.

## 9. Checklist

- [x] identifiant conforme ;
- [x] repères d’utilisation présents ;
- [x] exemple et résultat attendus ;
- [x] aucune information propriétaire copiée.

## 10. Références croisées

- `DOC-V0-CH03` — architecture documentaire ;
- `DOC-V0-CH04` — identifiants ;
- `DOC-V0-CH05` — Markdown et Pandoc.

## 11. Historique

- 2026-07-30 — version 1.0.0 : création de l’exemple.
