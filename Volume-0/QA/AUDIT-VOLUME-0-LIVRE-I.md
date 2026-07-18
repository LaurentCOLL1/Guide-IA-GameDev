---
title: "Audit documentaire et technique - Volume 0 et Livre I"
id: "DOC-QA-V0-L1-2026-07"
status: "reviewed"
version: "0.9.0"
date: "2026-07-18"
category: "quality-report"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit documentaire et technique - Volume 0 et Livre I

## 1. Périmètre

L’audit couvre :

- les onze chapitres du Volume 0 ;
- les huit annexes normatives du Volume 0 ;
- l’index et les documents d’assurance qualité du Volume 0 ;
- les dix chapitres du Livre I ;
- l’index et le rapport QA du Livre I ;
- les entrées correspondantes de `contents.txt`, `ROADMAP.md` et `STYLE_GUIDE.md` ;
- la chaîne de compilation Pandoc/XeLaTeX ;
- les liens, commandes, contenus de fichiers et procédures destinées aux débutants.

## 2. Objectifs et méthode

L’audit vérifie :

1. la complétude documentaire ;
2. la cohérence avec le sommaire maître ;
3. l’actualité des procédures et références techniques au 18 juillet 2026 ;
4. la présence d’un contexte d’utilisation avant chaque commande ou contenu de fichier ;
5. l’identification des actions à effectuer dans un navigateur ou une interface graphique ;
6. la distinction entre commande, contenu à créer, résultat attendu et exemple de lecture ;
7. les métadonnées, identifiants, liens et index ;
8. la compilation et la mise en page PDF.

La vérification technique utilise en priorité les documentations officielles, les pages de téléchargement des éditeurs et les dépôts principaux des projets.

## 3. Non-conformité transversale confirmée

La règle historique du Volume 0 demandait déjà de « préciser le terminal concerné », mais elle ne définissait ni syntaxe obligatoire ni contrôle automatique.

Conséquences observées :

- des blocs PowerShell étaient présentés sans phrase indiquant d’ouvrir PowerShell ;
- des commandes Git ou WinGet pouvaient être prises pour des commandes génériques ;
- le contenu de `.vscode/settings.json` était affiché sans expliquer clairement qu’il fallait créer ce fichier dans Visual Studio Code ;
- certains fichiers `.env`, YAML ou JSON pouvaient être confondus avec des exemples à lire ;
- des blocs de sortie pouvaient être confondus avec des commandes à saisir ;
- des liens de téléchargement procéduraux ne précisaient pas toujours qu’ils devaient être ouverts dans un navigateur ;
- les commandes Docker exécutées depuis l’hôte n’étaient pas toujours distinguées d’un shell ouvert dans un conteneur.

Cette non-conformité est classée **majeure** pour un guide destiné aux débutants.

## 4. Correction normative

La convention `DOC-V0-ANN-CONTEXTES` introduit les repères suivants.

> **[LECTURE] Liste normative - Ne pas saisir.**

```text
[PS]      PowerShell 7 sur l’hôte Windows
[CMD]     Invite de commandes Windows
[WSL]     Terminal WSL ou Bash Linux
[DCT]     Terminal ouvert dans un conteneur Docker
[DCK]     Interface Docker Desktop
[VSC]     Visual Studio Code pour créer ou modifier un fichier
[WEB]     Navigateur internet
[APP]     Interface graphique de l’application nommée
[SORTIE]  Résultat attendu, à ne pas saisir
[LECTURE] Exemple, structure ou valeur non directement exécutable
```

Deux contrôles permanents sont ajoutés :

- présence d’un repère avant chaque bloc procédural ;
- cohérence sémantique entre le repère, le langage du bloc et l’action annoncée.

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

### 5.3 Docker : hôte et conteneur

> **[PS] PowerShell 7 - Exécuter :** lancer Docker Compose depuis le dossier contenant `compose.yaml`.

```powershell
docker compose up -d
```

> **[DCT] Terminal du conteneur - Exécuter :** utiliser le shell du conteneur concerné.

```bash
python --version
```

## 6. Résultats de la vérification technique

### 6.1 Windows, WinGet, PowerShell, Git et VS Code

- Les commandes WinGet utilisent les identifiants exacts et la source `winget`.
- PowerShell 7 reste le shell principal du parcours Windows.
- Git for Windows `2.55.0` était la version officielle courante le 18 juillet 2026 ; la procédure conserve néanmoins la version réellement installée comme source de vérité locale.
- Les paramètres de workspace VS Code sont bien stockés dans `.vscode/settings.json` et peuvent être édités dans l’interface ou dans le fichier JSON.
- Les étapes qui nécessitent une réouverture de terminal indiquent désormais explicitement quel programme fermer et quel shell rouvrir.

### 6.2 Python

- Python `3.14.6` et `3.13.14` étaient les versions publiées courantes lors de l’audit.
- Le Livre I conserve Python 3.13 comme exemple de compatibilité pour plusieurs applications IA.
- Le texte précise désormais qu’une version plus récente n’est pas automatiquement prise en charge par les dépendances du projet.
- Les commandes `pip` ont été reclassées en **[PS]** et ne sont plus présentées comme du contenu à créer dans VS Code.

### 6.3 Docker, Open WebUI, Open Terminal et Vane

- Docker Compose v2 utilise la forme `docker compose`, exécutée depuis PowerShell dans le parcours Windows principal.
- Open WebUI recommande officiellement Docker pour la majorité des utilisateurs et documente `v0.10.1` comme exemple de release épinglée.
- Open Terminal `v0.11.34` et Vane `v1.12.2` correspondent aux releases observées pendant l’audit.
- Les commandes Docker exécutées sur l’hôte utilisent **[PS]** ; les commandes réellement exécutées dans un conteneur utilisent **[DCT]**.
- `.env`, `.env.example` et `compose.yaml` indiquent désormais Visual Studio Code et leur emplacement cible.

### 6.4 ComfyUI et AMD

- La version de référence a été corrigée de `v0.24.0` vers `v0.28.0`, release stable observée le 15 juillet 2026.
- ComfyUI Desktop Windows reste principalement destiné aux GPU NVIDIA.
- Un portable AMD expérimental existe désormais, mais le support Windows AMD officiel vise RDNA 3, RDNA 3.5 et RDNA 4.
- La Radeon RX 6750 XT étant RDNA 2, ce portable expérimental n’est pas présenté comme compatible avec la configuration de référence.
- Python 3.13 reste recommandé par ComfyUI ; Python 3.12 constitue un repli et Python 3.14 peut encore poser problème à certains nœuds personnalisés.

### 6.5 Ollama et LLM locaux

- Ollama `v0.32.0` était la release courante observée pendant l’audit.
- L’application Windows prend officiellement en charge les GPU AMD Radeon et expose l’API locale sur le port `11434`.
- `OLLAMA_MODELS` reste la variable officielle pour déplacer les modèles.
- Les chapitres conservent une exécution native Windows comme parcours principal pour la machine AMD de référence.

### 6.6 Volume 0

Les onze chapitres et les annexes ont été relus pour vérifier :

- les identifiants et conventions documentaires ;
- les structures Markdown et Pandoc ;
- les exemples de métadonnées et de rapports ;
- les distinctions entre contenu à créer, commande et résultat ;
- la sécurité, les licences et la reproductibilité ;
- la cohérence des index et de la chaîne de compilation.

Aucune non-conformité bloquante supplémentaire n’a été conservée après correction.

## 7. Non-conformités corrigées

| ID | Gravité | Constat | Résolution |
|---|---|---|---|
| V0L1-AUD-001 | majeure | Aucun repère normalisé pour les programmes et terminaux. | Création de `DOC-V0-ANN-CONTEXTES`. |
| V0L1-AUD-002 | majeure | Blocs PowerShell sans indication explicite du shell. | Ajout de **[PS]** et du contexte hôte Windows. |
| V0L1-AUD-003 | majeure | Contenus JSON/YAML/.env sans éditeur ni chemin systématiques. | Ajout de **[VSC]** et du chemin cible. |
| V0L1-AUD-004 | majeure | Commandes Docker hôte et conteneur insuffisamment distinguées. | Séparation **[PS]**, **[DCK]** et **[DCT]**. |
| V0L1-AUD-005 | mineure | Sorties et exemples susceptibles d’être recopiés. | Ajout de **[SORTIE]** et **[LECTURE]**. |
| V0L1-AUD-006 | mineure | Liens procéduraux sans instruction de navigateur. | Ajout de **[WEB]** lorsque le lien fait partie d’une procédure. |
| V0L1-AUD-007 | majeure | Le premier linter validait la présence, mais pas le sens du repère. | Ajout d’un audit sémantique distinct. |
| V0L1-AUD-008 | mineure | Python 3.13 pouvait sembler être la dernière version disponible. | Distinction entre actualité et compatibilité. |
| V0L1-AUD-009 | majeure | Version ComfyUI de référence devenue obsolète. | Mise à jour vers `v0.28.0`. |
| V0L1-AUD-010 | mineure | Les dix chapitres du Livre I restaient en `draft-review`. | Passage au statut `reviewed` après audit. |

## 8. Résultats quantitatifs

Les valeurs exactes sont produites par `tools/report_contextes_utilisation.py` et seront recopiées après l’exécution finale de la CI.

| Mesure | Résultat provisoire |
|---|---|
| Documents contrôlés par le linter | 42 |
| Chapitres audités | 21 |
| Blocs précédés d’un repère | validation automatique requise |
| Cohérence sémantique | validation automatique requise |
| Non-conformités bloquantes ouvertes | 0 après corrections |
| Compilation PDF | en attente du passage final |
| Inspection visuelle | en attente du passage final |

## 9. Portes qualité

- [x] Q0 - Intégrité et métadonnées
- [x] Q1 - Conformité éditoriale
- [x] Q2 - Cohérence documentaire
- [x] Q3 - Vérification technique statique
- [x] Q4 - Sécurité et licences
- [ ] Q5 - Compilation et inspection PDF

## 10. Réserve runtime

Cet audit vérifie statiquement les procédures, les commandes et les configurations. Il ne prétend pas que chaque logiciel tiers a été installé et exécuté sur une station physique dans cette campagne.

Les exemples qui nécessitent une station Windows, une RX 6750 XT, Docker Desktop, un modèle IA ou un périphérique audio conservent une réserve runtime explicite. Le niveau `runtime-tested` ne pourra être attribué qu’après exécution sur la station de référence et conservation des journaux correspondants.
