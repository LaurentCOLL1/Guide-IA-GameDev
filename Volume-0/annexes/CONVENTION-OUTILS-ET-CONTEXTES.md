---
title: "Convention des outils et contextes d’utilisation"
id: "DOC-V0-ANN-CONTEXTES"
status: "validated"
version: "1.0.0"
date: "2026-07-18"
category: "normative"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
---

# Convention des outils et contextes d’utilisation

## 1. Objectif

Une commande, un contenu de fichier ou une adresse internet ne doit jamais obliger le lecteur à deviner quel programme ouvrir.

Tout élément destiné à être exécuté, créé, modifié, ouvert ou seulement observé reçoit un repère explicite immédiatement avant l’élément concerné.

La forme normative est :

> **[CODE] Outil - Action :** emplacement, fichier ou précision utile.

Le repère doit répondre au minimum à deux questions :

1. **Quel programme faut-il ouvrir ?**
2. **Que faut-il faire avec le bloc ou le lien ?**

## 2. Repères autorisés

| Repère | Programme ou contexte | Usage principal |
|---|---|---|
| **[PS]** | PowerShell 7 sur l’hôte Windows | Exécuter des commandes Windows, Git, WinGet, Python, Docker CLI ou scripts `.ps1`. |
| **[CMD]** | Invite de commandes `cmd.exe` | Exécuter une commande qui dépend réellement de `cmd.exe` ou d’un fichier `.bat`/`.cmd`. |
| **[WSL]** | Terminal WSL ou Bash Linux | Exécuter des commandes Linux dans une distribution WSL. |
| **[DCT]** | Terminal ouvert à l’intérieur d’un conteneur Docker | Exécuter une commande dans le système de fichiers et l’environnement du conteneur. |
| **[DCK]** | Interface Docker Desktop | Modifier une option graphique, consulter l’état du moteur ou gérer une ressource depuis l’application. |
| **[VSC]** | Visual Studio Code | Créer ou modifier un fichier source, un script ou une configuration. |
| **[WEB]** | Navigateur internet | Ouvrir une page officielle, télécharger un outil ou consulter une documentation procédurale. |
| **[APP]** | Interface graphique nommée dans le texte | Effectuer une action dans Godot, Blender, ComfyUI, Open WebUI ou une autre application. |
| **[SORTIE]** | Résultat attendu | Lire et comparer ; ne pas saisir le contenu. |
| **[LECTURE]** | Exemple, structure ou valeur de référence | Comprendre le document ; ne pas exécuter ni recopier sans instruction complémentaire. |

## 3. Commandes PowerShell

Le repère **[PS]** signifie que les commandes sont saisies dans **PowerShell 7** ouvert sur l’hôte Windows.

> **[PS] PowerShell 7 - Exécuter :** ouvrir PowerShell sur Windows, sans privilèges administrateur sauf indication contraire.

```powershell
winget show --id Git.Git --exact --source winget
winget install --id Git.Git --exact --source winget
```

Après une installation qui modifie le `PATH`, la procédure doit préciser qu’il faut fermer puis rouvrir PowerShell.

> **[PS] PowerShell 7 - Vérifier après réouverture :** fermer toutes les fenêtres PowerShell, ouvrir une nouvelle fenêtre, puis exécuter les commandes.

```powershell
git --version
where.exe git
```

Une commande `git`, `python`, `winget` ou `docker compose` n’obtient pas automatiquement un repère spécifique : le repère décrit le **terminal utilisé**. Dans le parcours Windows principal, ces commandes utilisent donc généralement **[PS]**.

## 4. Création ou modification d’un fichier

Un bloc contenant le contenu d’un fichier indique l’éditeur et le chemin cible.

> **[VSC] Visual Studio Code - Créer :** `.vscode/settings.json` à la racine du projet. Dans VS Code, ouvrir le dossier du projet, créer le dossier `.vscode` s’il n’existe pas, puis créer `settings.json`.

```json
{
  "files.encoding": "utf8",
  "files.eol": "\n",
  "editor.formatOnSave": false
}
```

Le mot **Créer** est utilisé lorsque le fichier n’existe pas. Le mot **Modifier** est utilisé lorsqu’une procédure complète ou remplace un fichier existant.

Le chemin doit être donné avant le bloc, et non seulement dans un paragraphe éloigné.

## 5. Navigateur internet

Une adresse utilisée dans une procédure indique explicitement qu’elle doit être ouverte dans un navigateur.

> **[WEB] Navigateur internet - Ouvrir :** utiliser la page officielle de téléchargement indiquée ci-dessous.

[Page officielle de téléchargement de Git](https://git-scm.com/download/win)

Les listes bibliographiques et les sections intitulées **Sources**, **Références** ou **Documentation officielle** peuvent regrouper plusieurs liens sous un seul repère **[WEB]**. Elles ne nécessitent pas un repère répété devant chaque entrée lorsque l’usage est évident.

## 6. Docker : hôte, interface et conteneur

Les contextes Docker ne doivent pas être confondus.

### 6.1 Commande Docker lancée depuis Windows

> **[PS] PowerShell 7 - Exécuter depuis le dossier contenant `compose.yaml` :** la commande pilote Docker Desktop depuis l’hôte Windows.

```powershell
docker compose up -d
```

### 6.2 Action dans Docker Desktop

> **[DCK] Docker Desktop - Interface :** ouvrir **Settings > Resources** et contrôler les ressources attribuées au moteur WSL 2.

### 6.3 Commande dans un conteneur

> **[DCT] Terminal du conteneur - Exécuter :** après ouverture d’un shell dans le conteneur concerné.

```bash
python --version
ls -la /app
```

Une commande Bash n’est marquée **[DCT]** que si le texte établit clairement que le shell se trouve dans un conteneur. Une commande Bash exécutée dans Ubuntu sous WSL utilise **[WSL]**.

## 7. Interfaces graphiques

Le repère **[APP]** nomme toujours l’application.

> **[APP] Visual Studio Code - Interface :** ouvrir la palette de commandes avec `Ctrl+Shift+P`, puis choisir **Preferences: Open Workspace Settings (JSON)**.

> **[APP] Godot - Interface :** sélectionner le nœud `Camera3D` dans l’arbre de scène, puis modifier la propriété **Current** dans l’Inspector.

> **[APP] ComfyUI - Interface :** importer le workflow JSON depuis le menu de chargement.

Le repère générique **[APP]** ne doit jamais être écrit sans le nom de l’application.

## 8. Sorties et exemples non exécutables

Une sortie de commande ne doit pas être confondue avec une commande.

> **[SORTIE] Résultat attendu - Ne pas saisir :** la version exacte peut varier.

```text
Git version 2.x.y
```

Une arborescence, une valeur indicative, un diagramme textuel ou un pseudocode utilise **[LECTURE]**.

> **[LECTURE] Structure de référence - Ne pas saisir :** exemple d’organisation d’un projet.

```text
project/
├── src/
├── tests/
└── README.md
```

## 9. Règles de placement

Le repère :

- se place immédiatement avant le bloc, le lien ou le groupe de liens concerné ;
- reste séparé du bloc par une seule ligne vide ;
- indique le programme exact lorsque plusieurs possibilités existent ;
- précise le chemin du fichier pour tout contenu destiné à être créé ou modifié ;
- précise le dossier de travail lorsque la commande en dépend ;
- indique si des droits administrateur sont nécessaires ;
- distingue une commande d’un résultat attendu ;
- ne repose pas uniquement sur une icône ou une couleur.

## 10. Exceptions

Un repère n’est pas obligatoire pour :

- un nom de commande cité en code en ligne sans instruction d’exécution ;
- une référence bibliographique clairement située dans une section de sources ;
- une syntaxe présentée uniquement comme objet d’étude, à condition qu’un repère **[LECTURE]** couvre le groupe d’exemples ;
- le front matter YAML du document.

En cas de doute, ajouter le repère. Une répétition courte est préférable à une procédure ambiguë.

## 11. Contrôle automatique

La CI vérifie les documents du Volume 0 et du Livre I. Tout bloc de code procédural doit être précédé d’un repère reconnu.

Les repères reconnus sont :

> **[LECTURE] Liste normative - Ne pas saisir.**

```text
[PS] [CMD] [WSL] [DCT] [DCK] [VSC] [WEB] [APP] [SORTIE] [LECTURE]
```

Un chapitre ne peut être déclaré audité si des blocs procéduraux restent sans contexte d’utilisation.