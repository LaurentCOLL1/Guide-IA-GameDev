---
title: "Audit documentaire et technique - Volume 0 et Livre I"
id: "DOC-QA-V0-L1-2026-07"
status: "in-progress"
version: "0.1.0"
date: "2026-07-18"
category: "quality-report"
audit-level: "static-review"
---

# Audit documentaire et technique - Volume 0 et Livre I

## 1. Périmètre

L’audit couvre :

- les onze chapitres du Volume 0 ;
- les annexes normatives du Volume 0 ;
- l’index et l’assurance qualité du Volume 0 ;
- les dix chapitres du Livre I ;
- l’index du Livre I ;
- les entrées correspondantes de `contents.txt`, `ROADMAP.md` et `STYLE_GUIDE.md` ;
- la chaîne de compilation Pandoc/XeLaTeX ;
- les liens, commandes, contenus de fichiers et procédures destinées aux débutants.

## 2. Objectifs

L’audit doit vérifier :

1. la complétude documentaire ;
2. la cohérence avec le sommaire maître ;
3. l’actualité des procédures et références techniques ;
4. la présence d’un contexte d’utilisation avant chaque commande ou contenu de fichier ;
5. l’identification des actions à effectuer dans un navigateur ou une interface graphique ;
6. la distinction entre commande, contenu à créer, résultat attendu et exemple de lecture ;
7. les métadonnées, identifiants, liens et index ;
8. la compilation et la mise en page PDF.

## 3. Non-conformité transversale confirmée

La règle historique du Volume 0 demandait déjà de « préciser le terminal concerné », mais elle ne définissait ni syntaxe obligatoire ni contrôle automatique.

Conséquences observées :

- des blocs PowerShell étaient présentés sans phrase indiquant d’ouvrir PowerShell ;
- des commandes Git ou WinGet pouvaient être prises pour des commandes génériques ;
- le contenu de `.vscode/settings.json` était affiché sans expliquer clairement qu’il fallait créer ce fichier dans Visual Studio Code ;
- des blocs de sortie pouvaient être confondus avec des commandes à saisir ;
- des liens de téléchargement procéduraux ne précisaient pas toujours qu’ils devaient être ouverts dans un navigateur ;
- les commandes Docker exécutées depuis l’hôte n’étaient pas toujours distinguées d’un shell ouvert dans un conteneur.

Cette non-conformité est classée **majeure** pour un guide destiné aux débutants.

## 4. Correction normative

La convention `DOC-V0-ANN-CONTEXTES` introduit les repères :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
[PS] [CMD] [WSL] [DCT] [DCK] [VSC] [WEB] [APP] [SORTIE] [LECTURE]
```

La migration automatique ajoute ces repères dans le Volume 0 et le Livre I. Un contrôle permanent de CI empêchera leur suppression involontaire.

## 5. Exemples corrigés

### 5.1 Installation avec WinGet

Avant correction, le lecteur devait déduire le terminal à utiliser.

Après correction :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
winget show --id Git.Git --exact --source winget
winget install --id Git.Git --exact --source winget
```

> **[PS] PowerShell 7 - Vérifier après réouverture :** fermer PowerShell, ouvrir une nouvelle fenêtre, puis exécuter les commandes.

```powershell
git --version
where.exe git
```

### 5.2 Paramètres du workspace VS Code

Après correction :

> **[VSC] Visual Studio Code - Créer :** `.vscode/settings.json` à la racine du projet. Ouvrir le dossier dans VS Code, créer `.vscode` si nécessaire, puis créer `settings.json`.

```json
{
  "files.encoding": "utf8",
  "files.eol": "\n",
  "editor.formatOnSave": false,
  "files.exclude": {
    "**/.venv": true,
    "**/__pycache__": true,
    "**/.godot": true
  }
}
```

## 6. Vérification technique en cours

Les domaines suivants sont vérifiés contre leurs sources officielles datées :

- Windows, WinGet, PowerShell et WSL ;
- Git et Visual Studio Code ;
- Python et environnements virtuels ;
- Docker Desktop et Docker Compose ;
- Open WebUI, Open Terminal et Vane ;
- ComfyUI et les voies AMD ;
- Ollama, llama.cpp, LocalAI et LibreChat ;
- outils audio locaux ;
- sécurité, sauvegarde et validation.

Les changements de versions ou de support détectés sont consignés avant clôture.

## 7. Résultats quantitatifs

À compléter après migration et exécution de la CI :

| Mesure | Résultat |
|---|---|
| Documents contrôlés | en cours |
| Blocs annotés | en cours |
| Liens procéduraux annotés | en cours |
| Non-conformités bloquantes ouvertes | en cours |
| Compilation PDF | en cours |
| Inspection visuelle | en cours |

## 8. Portes qualité

- [ ] Q0 - Intégrité et métadonnées
- [ ] Q1 - Conformité éditoriale
- [ ] Q2 - Cohérence documentaire
- [ ] Q3 - Vérification technique statique
- [ ] Q4 - Sécurité et licences
- [ ] Q5 - Compilation et inspection PDF

## 9. Réserve runtime

Cet audit vérifie statiquement les procédures, les commandes et les configurations. Il ne prétend pas que chaque logiciel tiers a été installé et exécuté sur une station physique dans cette campagne.

Les exemples qui nécessitent une station Windows, une RX 6750 XT, Docker Desktop, un modèle IA ou un périphérique audio conservent une réserve runtime explicite.
