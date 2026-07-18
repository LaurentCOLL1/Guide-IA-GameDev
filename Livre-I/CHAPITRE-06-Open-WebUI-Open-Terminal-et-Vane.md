---
title: "Livre I — Chapitre 6 : Open WebUI, Open Terminal et Vane"
id: "DOC-L1-CH03"
status: "draft-review"
version: "1.3.0"
lang: "fr-FR"
book: "Livre I"
chapter: 6
legacy-chapter: 3
canonical-order: 6
last-verified: "2026-07-18"
reference-platform:
  os: "Windows 11 64 bits"
  containers: "Docker Desktop avec WSL 2"
  gpu: "AMD Radeon RX 6750 XT 12 Go"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Open WebUI, Open Terminal et Vane

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L1-CH03`  
> **Priorité :** Open WebUI obligatoire · Open Terminal recommandé · Vane optionnel  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **État technique vérifié le :** 18 juillet 2026  
> **Résultat attendu :** disposer d’une interface IA locale persistante, d’un terminal contrôlé pour les agents et, si nécessaire, d’un moteur de recherche IA autonome avec citations.

## 1. Objet du chapitre

Ce chapitre installe la couche d’interaction humaine de la plateforme locale.

Les trois composants n’ont pas le même rôle :

| Composant | Rôle | Statut dans le guide |
|---|---|---|
| Open WebUI | interface centrale pour les modèles, conversations, connaissances, outils et agents | obligatoire |
| Open Terminal | environnement d’exécution de commandes et de gestion de fichiers accessible depuis Open WebUI | recommandé, à activer avec prudence |
| Vane | moteur de recherche et de réponse avec sources, indépendant d’Open WebUI | optionnel |

Ils ne doivent pas être confondus :

- Open Terminal est un projet de l’organisation Open WebUI et possède une intégration native dans Open WebUI ;
- Vane est un projet tiers distinct ;
- aucune dépendance fonctionnelle n’impose d’installer Vane pour utiliser Open WebUI ;
- aucune installation de terminal ne doit donner à un modèle un accès illimité au poste Windows.

## 2. Architecture retenue

La configuration principale sépare l’interface, le terminal et la recherche :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
Navigateur Windows
├── http://127.0.0.1:3000 → Open WebUI
└── http://127.0.0.1:3001 → Vane, optionnel

Docker Desktop / WSL 2
├── open-webui
│   ├── volume persistant
│   ├── accès aux fournisseurs de modèles
│   └── accès interne à Open Terminal
├── open-terminal
│   ├── réseau interne uniquement
│   ├── clé API obligatoire
│   └── espace de travail dédié
└── vane, profil optionnel
    ├── volume persistant
    └── moteur SearxNG inclus dans l’image standard

Hôte Windows
├── Ollama, llama.cpp ou autre serveur compatible
├── ComfyUI
└── fichiers de projet explicitement partagés
```

La règle essentielle est la suivante :

> Une interface web peut être facilement réinstallée. Les données, secrets, conversations et fichiers manipulés par les agents doivent en revanche être persistants, sauvegardés et limités par une frontière de confiance explicite.

## 3. État des projets au 18 juillet 2026

### 3.1 Open WebUI

Open WebUI est une plateforme auto-hébergée compatible avec :

- Ollama ;
- les API compatibles OpenAI ;
- les fournisseurs Open Responses ;
- les bases de connaissances ;
- les outils et serveurs MCP ;
- Open Terminal ;
- différents agents locaux ou distants.

L’installation Docker est la voie officiellement recommandée pour la majorité des utilisateurs.

Les images officielles sont publiées sur :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
ghcr.io/open-webui/open-webui
openwebui/open-webui
```

Le guide utilise GitHub Container Registry comme référence principale.

### 3.2 Open Terminal

Open Terminal fournit une API permettant à un assistant de :

- exécuter des commandes ;
- lire et écrire des fichiers ;
- lancer des scripts ;
- parcourir un espace de travail ;
- exposer certains services locaux ;
- fonctionner comme serveur MCP.

Il peut fonctionner :

- dans Docker, avec une isolation par conteneur ;
- directement sur Windows, Linux ou macOS ;
- au sein d’un environnement multi-utilisateur limité ;
- derrière un orchestrateur de terminaux distinct.

Le parcours principal utilise Docker. Le mode natif Windows n’est utilisé que lorsqu’un accès réel aux outils Windows est indispensable et après validation du risque.

### 3.3 Vane

Vane est un moteur de recherche IA auto-hébergé, axé sur :

- la recherche web ;
- les réponses avec citations ;
- les discussions et sources académiques ;
- les fichiers téléversés ;
- l’utilisation de modèles locaux ou de fournisseurs cloud ;
- SearxNG comme métamoteur de recherche.

Vane reste optionnel, car Open WebUI possède déjà ses propres fonctions de recherche, RAG, outils et agents. Vane est pertinent lorsque le projet souhaite une interface spécialisée de type moteur de réponse.

La présence d’un moteur auto-hébergé ne signifie pas que la recherche web devient hors ligne ou anonyme par magie. Les requêtes quittent la machine lorsqu’elles interrogent des moteurs, sites ou API externes.

## 4. Décisions de sécurité

### 4.1 Open WebUI

Le guide impose :

- une authentification active ;
- un `WEBUI_SECRET_KEY` persistant ;
- une liaison à `127.0.0.1` tant qu’un accès réseau n’est pas nécessaire ;
- une sauvegarde avant mise à jour ;
- une image versionnée ou un digest enregistré ;
- un compte administrateur distinct des usages ordinaires en Mode Studio ;
- aucun volume de données partagé entre une instance stable et une instance `dev`.

Le mode `WEBUI_AUTH=False` n’est pas utilisé dans le parcours principal. La documentation officielle avertit qu’une instance passée en mode mono-utilisateur sans authentification ne peut pas ensuite être convertie simplement en instance multi-comptes.

### 4.2 Open Terminal

Open Terminal constitue une frontière de confiance critique.

Un agent pouvant exécuter des commandes peut notamment :

- supprimer ou modifier des fichiers ;
- télécharger et exécuter du code ;
- consommer toute la mémoire ou le CPU disponibles ;
- exfiltrer des données si le réseau sortant est ouvert ;
- lire les secrets accessibles dans son environnement ;
- lancer un serveur local ;
- produire des résultats techniquement valides mais indésirables.

Le parcours principal applique donc :

- aucun port publié vers Windows pour Open Terminal ;
- accès uniquement depuis Open WebUI sur un réseau Docker interne ;
- clé API longue et aléatoire ;
- montage d’un dossier de travail dédié uniquement ;
- interdiction de monter le profil Windows complet ;
- interdiction de monter le socket Docker ;
- interdiction de monter les dossiers contenant les clés SSH, mots de passe ou données privées ;
- sauvegarde Git ou copie préalable avant toute action agentique ;
- validation humaine pour les commandes destructives.

### 4.3 Vane

Vane est lié à `127.0.0.1` par défaut.

Les clés de fournisseurs éventuelles :

- ne doivent pas apparaître dans `compose.yaml` ;
- ne doivent pas être partagées avec Open Terminal ;
- doivent être limitées au fournisseur nécessaire ;
- doivent être révoquées si elles apparaissent dans un journal ou une capture ;
- doivent être évitées lorsque le parcours local avec Ollama suffit.

## 5. Versions et reproductibilité

Les exemples officiels de documentation utilisent parfois des balises flottantes telles que :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
:main
:latest
```

Elles sont pratiques pour un essai, mais ne garantissent pas qu’une réinstallation future récupère le même logiciel.

Le projet applique deux niveaux :

### Niveau d’exploration

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```dotenv
OPEN_WEBUI_IMAGE=ghcr.io/open-webui/open-webui:main
OPEN_TERMINAL_IMAGE=ghcr.io/open-webui/open-terminal
VANE_IMAGE=itzcrazykns1337/vane:latest
```

### Niveau stable

Après validation :

1. choisir une version de release lorsqu’elle existe dans le registre ;
2. télécharger l’image ;
3. relever son digest ;
4. enregistrer le digest dans le manifeste de compatibilité ;
5. tester la sauvegarde et la restauration ;
6. mettre à jour une seule instance de test avant la production.

Commande d’inventaire :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker image inspect `
  --format '{{json .RepoDigests}}' `
  ghcr.io/open-webui/open-webui:main
```

Lors de la vérification de ce chapitre :

- la documentation Open WebUI citait notamment une image de release `v0.10.1` comme exemple de version épinglée ;
- la dernière release GitHub observée d’Open Terminal était `v0.11.34` ;
- la dernière release GitHub observée de Vane était `v1.12.2`.

Ces valeurs constituent un relevé daté, pas une invitation à supposer qu’elles restent les dernières versions après le 18 juillet 2026.

## 6. Préparer le dossier de déploiement

Créer :

> **[VSC] Visual Studio Code - Créer ou modifier :** `ghcr.io/open-webui/open-webui:main`.

```powershell
New-Item -ItemType Directory -Force "$HOME\Guide-IA-Services" | Out-Null
Set-Location "$HOME\Guide-IA-Services"
New-Item -ItemType Directory -Force "workspace" | Out-Null
New-Item -ItemType Directory -Force "backups" | Out-Null
```

Arborescence :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
Guide-IA-Services/
├── compose.yaml
├── .env
├── .env.example
├── workspace/
├── backups/
└── README.md
```

Le dossier `workspace` est le seul dossier de projet partagé avec Open Terminal dans le parcours initial.

## 7. Préparer les secrets

### 7.1 Générer les clés

Avec PowerShell :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
$bytes = New-Object byte[] 32
[System.Security.Cryptography.RandomNumberGenerator]::Fill($bytes)
[Convert]::ToHexString($bytes).ToLower()
```

Exécuter deux fois la commande pour obtenir :

- `WEBUI_SECRET_KEY` ;
- `OPEN_TERMINAL_API_KEY`.

### 7.2 Créer `.env.example`

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```dotenv
OPEN_WEBUI_IMAGE=ghcr.io/open-webui/open-webui:main
OPEN_TERMINAL_IMAGE=ghcr.io/open-webui/open-terminal
VANE_IMAGE=itzcrazykns1337/vane:latest
OPEN_WEBUI_PORT=3000
VANE_PORT=3001
WEBUI_SECRET_KEY=replace-me
OPEN_TERMINAL_API_KEY=replace-me
```

### 7.3 Créer `.env`

Copier le fichier puis remplacer les secrets :

> **[VSC] Visual Studio Code - Créer ou modifier :** `.env`.

```powershell
Copy-Item .env.example .env
notepad .env
```

Ajouter au `.gitignore` du projet local :

> **[VSC] Visual Studio Code - Créer ou modifier :** `.gitignore`.

```gitignore
.env
backups/
workspace/.secrets/
```

Le fichier `.env` reste une solution simple adaptée au Mode Solo. Pour un déploiement Studio, utiliser un gestionnaire de secrets ou un mécanisme d’injection protégé.

## 8. Fichier Compose de référence

Créer `compose.yaml` :

> **[VSC] Visual Studio Code - Créer ou modifier :** `compose.yaml`.

```yaml
name: guide-ia-interface

services:
  open-webui:
    image: ${OPEN_WEBUI_IMAGE:?OPEN_WEBUI_IMAGE absent}
    container_name: guide-ia-open-webui
    ports:
      - "127.0.0.1:${OPEN_WEBUI_PORT:-3000}:8080"
    extra_hosts:
      - "host.docker.internal:host-gateway"
    environment:
      WEBUI_SECRET_KEY: ${WEBUI_SECRET_KEY:?WEBUI_SECRET_KEY absent}
    volumes:
      - open-webui-data:/app/backend/data
    networks:
      - application
      - terminal
    restart: unless-stopped
    healthcheck:
      test:
        - CMD
        - python
        - -c
        - "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health', timeout=5)"
      interval: 15s
      timeout: 8s
      retries: 20
      start_period: 30s

  open-terminal:
    image: ${OPEN_TERMINAL_IMAGE:?OPEN_TERMINAL_IMAGE absent}
    container_name: guide-ia-open-terminal
    environment:
      OPEN_TERMINAL_API_KEY: ${OPEN_TERMINAL_API_KEY:?OPEN_TERMINAL_API_KEY absent}
    volumes:
      - open-terminal-home:/home/user
      - ./workspace:/workspace
    working_dir: /workspace
    expose:
      - "8000"
    networks:
      - terminal
    restart: unless-stopped
    security_opt:
      - no-new-privileges:true
    healthcheck:
      test:
        - CMD
        - python
        - -c
        - "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/docs', timeout=5)"
      interval: 15s
      timeout: 8s
      retries: 20
      start_period: 20s

  vane:
    image: ${VANE_IMAGE:?VANE_IMAGE absent}
    container_name: guide-ia-vane
    profiles:
      - research
    ports:
      - "127.0.0.1:${VANE_PORT:-3001}:3000"
    extra_hosts:
      - "host.docker.internal:host-gateway"
    volumes:
      - vane-data:/home/vane/data
    networks:
      - application
    restart: unless-stopped

networks:
  application:
  terminal:
    internal: true

volumes:
  open-webui-data:
    name: guide-ia-open-webui-data
  open-terminal-home:
    name: guide-ia-open-terminal-home
  vane-data:
    name: guide-ia-vane-data
```

### 8.1 Pourquoi Open Terminal ne publie aucun port

Open WebUI et Open Terminal partagent le réseau interne `terminal`.

Open WebUI peut joindre :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
http://open-terminal:8000
```

Le navigateur Windows ne peut pas joindre directement ce service. Cette architecture évite d’exposer une API capable d’exécuter des commandes.

### 8.2 Pourquoi Vane utilise un profil

Vane est optionnel. Il ne doit pas consommer des ressources ni multiplier les services lorsqu’il n’est pas utilisé.

Démarrage standard :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose up -d open-webui open-terminal
```

Démarrage avec Vane :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose --profile research up -d
```

## 9. Valider la configuration Compose

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose config
```

Cette commande doit échouer si une variable obligatoire manque.

Afficher les services :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose config --services
```

Afficher les volumes :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose config --volumes
```

Ne pas poursuivre tant que `docker compose config` signale une erreur.

## 10. Démarrer Open WebUI et Open Terminal

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose pull open-webui open-terminal
docker compose up -d open-webui open-terminal
docker compose ps
docker compose logs --tail=100 open-webui open-terminal
```

Attendre que les deux services soient `healthy`.

Ouvrir :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text

> **[WEB] Navigateur internet - Ouvrir :** utiliser la page officielle indiquée ci-dessous.

http://127.0.0.1:3000
```

Le premier compte créé devient administrateur. Utiliser un mot de passe unique et conserver les informations de récupération dans un coffre de mots de passe.

## 11. Connecter Open Terminal à Open WebUI

### 11.1 Connexion système recommandée

Dans Open WebUI :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Admin Settings
└── Integrations
    └── Open Terminal
```

Ajouter :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Nom : Terminal Guide IA
URL : http://open-terminal:8000
API key : valeur de OPEN_TERMINAL_API_KEY
```

La connexion administrateur est recommandée lorsque les deux conteneurs partagent le même réseau Docker. La configuration système est proxifiée par le backend Open WebUI ; l’URL et la clé du terminal ne sont pas exposées directement au navigateur.

### 11.2 Ne pas utiliser `localhost`

Depuis le conteneur Open WebUI :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
localhost = conteneur Open WebUI
```

La bonne adresse est le nom de service Compose :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
http://open-terminal:8000
```

### 11.3 Tester la liaison interne

> **[VSC] Visual Studio Code - Créer ou modifier :** `text http://open-terminal:8000`.

```powershell
docker compose exec open-webui python -c "import urllib.request; print(urllib.request.urlopen('http://open-terminal:8000/docs').status)"
```

Résultat attendu :

> **[SORTIE] Résultat attendu - Ne pas saisir :** comparer avec la sortie obtenue.

```text
200
```

### 11.4 Premier test fonctionnel

Créer dans `workspace` un fichier sans importance :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Set-Content -Path .\workspace\test-agent.txt -Value "Avant test"
```

Demander ensuite à l’assistant, avec confirmation humaine :

> **[SORTIE] Résultat attendu - Ne pas saisir :** comparer avec la sortie obtenue.

```text
Lis /workspace/test-agent.txt et ajoute une ligne contenant "Open Terminal validé".
Ne modifie aucun autre fichier.
```

Vérifier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Get-Content .\workspace\test-agent.txt
```

Ne pas commencer par une tâche portant sur un dépôt important ou un dossier personnel.

## 12. Limiter l’espace de travail du terminal

### 12.1 Arborescence conseillée

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
workspace/
├── sandbox/
├── imports/
├── exports/
└── projects/
    └── copie-de-travail/
```

L’agent ne reçoit que les fichiers nécessaires à sa tâche.

### 12.2 Interdictions

Ne pas monter :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
C:\Users\<utilisateur>
C:\
%USERPROFILE%\.ssh
%APPDATA%
%LOCALAPPDATA%
Docker Desktop data
/var/run/docker.sock
```

Ne pas transmettre au terminal :

- la clé privée Git ;
- les mots de passe de publication ;
- les jetons administrateur ;
- le portefeuille de certificats ;
- les bases contenant des données personnelles réelles ;
- les fichiers de licence non destinés au projet.

### 12.3 Git comme filet de sécurité

Avant une tâche agentique :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git status
git add -A
git commit -m "checkpoint before agent task"
```

Ou travailler dans une branche dédiée :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git switch -c agent/tache-limitee
```

Open Terminal ne remplace ni la revue de code ni la sauvegarde.

## 13. Open Terminal natif Windows

Open Terminal prend en charge Windows avec `pywinpty` et peut exécuter PowerShell et des programmes interactifs.

Le mode natif est utile lorsque l’agent doit réellement accéder :

- à Godot installé sur Windows ;
- à Blender installé sur Windows ;
- à un SDK Windows ;
- à des scripts PowerShell locaux ;
- à un environnement Python ou Node natif ;
- à des fichiers non accessibles depuis Docker.

Exemple limité :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Set-Location C:\Projets\Sandbox-Agent
uvx open-terminal run `
  --cwd C:\Projets\Sandbox-Agent `
  --host 127.0.0.1 `
  --port 8000 `
  --api-key "une-cle-longue"
```

Ce mode donne à l’agent les permissions du compte Windows qui lance le processus. Il ne doit jamais être considéré comme plus sûr que le conteneur.

Lier le service à `127.0.0.1`, utiliser un dossier dédié et arrêter le processus dès la fin de la tâche.

## 14. Mode MCP

Open Terminal peut fonctionner comme serveur MCP.

Installation ponctuelle :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
uvx --from "open-terminal[mcp]" open-terminal mcp
```

Transport HTTP local :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
uvx --from "open-terminal[mcp]" open-terminal mcp `
  --transport streamable-http `
  --host 127.0.0.1 `
  --port 8000 `
  --cwd C:\Projets\Sandbox-Agent
```

Ne pas activer simultanément plusieurs voies d’accès au même terminal sans documenter :

- les clients autorisés ;
- les clés utilisées ;
- les ports ;
- les répertoires accessibles ;
- les journaux ;
- la méthode d’arrêt.

## 15. Installer Vane

### 15.1 Démarrer le profil

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose --profile research pull vane
docker compose --profile research up -d vane
docker compose ps
docker compose logs --tail=200 vane
```

Ouvrir :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text

> **[WEB] Navigateur internet - Ouvrir :** utiliser la page officielle indiquée ci-dessous.

http://127.0.0.1:3001
```

L’image standard de Vane inclut SearxNG. Le volume persistant conserve les paramètres et données applicatives sous :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
/home/vane/data
```

### 15.2 Configuration initiale

L’assistant de configuration permet de choisir :

- un fournisseur de modèle ;
- le modèle de conversation ;
- le modèle d’embedding ;
- les sources de recherche ;
- les éventuelles clés d’API ;
- les préférences de recherche.

Le parcours local utilisera plus tard Ollama ou une API compatible OpenAI exécutée sur Windows.

Depuis un conteneur, l’adresse de l’hôte est :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
host.docker.internal
```

Exemple d’URL future :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
http://host.docker.internal:11434
```

La configuration détaillée du fournisseur est traitée dans le chapitre consacré aux LLM locaux.

### 15.3 Version allégée avec SearxNG externe

Vane publie également une image `slim-latest` destinée à un SearxNG existant :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
itzcrazykns1337/vane:slim-latest
```

Cette variante n’est retenue que lorsque :

- un SearxNG central existe déjà ;
- son format JSON est activé ;
- son URL interne est stable ;
- la responsabilité de sa mise à jour est définie ;
- sa politique réseau est documentée.

Pour le Mode Solo, l’image standard réduit le nombre de composants à configurer.

## 16. Choisir entre recherche Open WebUI et Vane

| Besoin | Choix conseillé |
|---|---|
| conversation générale avec modèles locaux | Open WebUI |
| connaissances privées et RAG | Open WebUI |
| agents et outils | Open WebUI |
| exécution de commandes | Open WebUI + Open Terminal |
| moteur de recherche spécialisé avec interface dédiée | Vane |
| recherche occasionnelle | outils de recherche Open WebUI |
| séparation nette entre chat et recherche documentaire | Open WebUI + Vane |
| poste peu puissant ou services minimaux | Open WebUI seul |

Installer deux interfaces qui fournissent des fonctions similaires augmente :

- la consommation de RAM ;
- les mises à jour ;
- les volumes à sauvegarder ;
- les comptes et secrets ;
- les risques de divergence des paramètres ;
- la surface d’exposition réseau.

Vane doit donc répondre à un besoin réel, pas uniquement à une volonté d’accumuler les outils.

## 17. Open WebUI Computer

Open WebUI propose également **Open WebUI Computer**, une application capable de travailler sur des fichiers, un terminal, Git et des projets depuis le navigateur.

Elle peut remplacer plusieurs usages d’Open Terminal dans certaines configurations.

Le parcours principal ne l’installe pas simultanément par défaut, car :

- ses fonctions recouvrent celles d’Open Terminal ;
- elle possède sa propre base, ses comptes et ses espaces de travail ;
- elle élargit la frontière de confiance ;
- le guide privilégie d’abord une architecture simple et mesurable.

Elle sera évaluée comme variante dans le Livre V ou le Companion Pack lorsque les besoins d’agent complet sur la machine seront définis.

## 18. Sauvegarder les données

### 18.1 Arrêter les écritures

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose stop open-webui open-terminal vane
```

L’arrêt de Vane peut signaler que le profil n’est pas actif ; ce n’est pas une erreur si Vane n’a jamais été démarré.

### 18.2 Sauvegarder Open WebUI

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker run --rm `
  --mount source=guide-ia-open-webui-data,target=/data,readonly `
  --mount type=bind,source="$PWD\backups",target=/backup `
  alpine:3.22 `
  tar -czf /backup/open-webui-data.tar.gz -C /data .
```

Le volume contient notamment :

- les utilisateurs ;
- les conversations ;
- les paramètres administrateur ;
- les fichiers téléversés ;
- les données de connaissances ;
- la base SQLite ;
- certains caches et journaux.

### 18.3 Sauvegarder Open Terminal

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker run --rm `
  --mount source=guide-ia-open-terminal-home,target=/data,readonly `
  --mount type=bind,source="$PWD\backups",target=/backup `
  alpine:3.22 `
  tar -czf /backup/open-terminal-home.tar.gz -C /data .
```

Le dossier `workspace` étant un bind mount, il doit être sauvegardé par Git ou par le système de sauvegarde Windows.

### 18.4 Sauvegarder Vane

> **[VSC] Visual Studio Code - Créer ou modifier :** `tar -czf /backup/open-terminal-home.tar.gz -C /data .`.

```powershell
docker run --rm `
  --mount source=guide-ia-vane-data,target=/data,readonly `
  --mount type=bind,source="$PWD\backups",target=/backup `
  alpine:3.22 `
  tar -czf /backup/vane-data.tar.gz -C /data .
```

### 18.5 Redémarrer

> **[VSC] Visual Studio Code - Créer ou modifier :** `tar -czf /backup/vane-data.tar.gz -C /data .`.

```powershell
docker compose up -d open-webui open-terminal
docker compose --profile research up -d vane
```

Ne pas démarrer Vane si le profil n’est pas utilisé.

## 19. Mettre à jour sans perdre les données

### 19.1 Procédure

1. lire les notes de version ;
2. sauvegarder les volumes ;
3. noter les images et digests actuels ;
4. mettre à jour `.env` vers la version testée ;
5. télécharger les nouvelles images ;
6. recréer les conteneurs ;
7. vérifier les migrations ;
8. tester les connexions ;
9. conserver l’ancienne sauvegarde jusqu’à validation.

Commandes :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose pull open-webui open-terminal
docker compose --profile research pull vane
docker compose up -d open-webui open-terminal
docker compose --profile research up -d vane
docker compose logs --tail=200
```

Open WebUI exécute ses migrations au démarrage. Une mise à jour interrompue ou une tentative de retour arrière après migration peut nécessiter une restauration du volume complet.

### 19.2 Instance de développement

Ne pas utiliser le même volume pour :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
open-webui:dev
open-webui:main
open-webui:vX.Y.Z
```

Créer un volume distinct :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
volumes:
  open-webui-dev-data:
```

Les versions de développement peuvent introduire des migrations incompatibles avec un retour arrière.

## 20. Journaux et diagnostic

### 20.1 État général

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose ps
docker compose top
docker stats --no-stream
```

### 20.2 Open WebUI

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose logs --tail=300 open-webui
```

Vérifier :

- migrations terminées ;
- absence de boucle de redémarrage ;
- volume accessible ;
- clé secrète persistante ;
- connexion au fournisseur de modèles ;
- WebSocket fonctionnel dans le navigateur.

### 20.3 Open Terminal

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose logs --tail=300 open-terminal
```

Vérifier :

- API démarrée sur le port interne 8000 ;
- clé API chargée ;
- dossier `/workspace` visible ;
- droits d’écriture limités au dossier prévu ;
- absence de port publié vers Windows.

### 20.4 Vane

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose --profile research logs --tail=300 vane
```

Vérifier :

- SearxNG démarré ;
- modèle configuré ;
- aucune clé affichée dans les journaux ;
- accès au fournisseur local ;
- recherche web fonctionnelle ;
- citations présentes dans les réponses de test.

## 21. Problèmes fréquents

### Open WebUI ne joint pas un service Windows

Utiliser :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
host.docker.internal
```

et non :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
localhost
127.0.0.1
```

Depuis le conteneur, ces deux dernières adresses désignent le conteneur lui-même.

### Déconnexion après recréation

Cause probable : `WEBUI_SECRET_KEY` a changé.

Solution :

- restaurer la clé précédente ;
- vérifier le chargement du fichier `.env` ;
- ne pas générer la clé automatiquement à chaque démarrage.

### Open Terminal répond depuis Windows alors qu’il ne devrait pas

Vérifier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose config
```

Le service `open-terminal` ne doit contenir aucune section `ports:` dans la configuration de base.

### Open Terminal ne voit pas les fichiers

Vérifier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose exec open-terminal pwd
docker compose exec open-terminal ls -la /workspace
```

Contrôler ensuite les permissions du bind mount Windows.

### Vane ne trouve aucun modèle local

Vérifier :

- le serveur de modèle est démarré ;
- l’URL utilise `host.docker.internal` ;
- le modèle demandé existe réellement ;
- la clé API n’est pas vide lorsque le fournisseur attend une valeur ;
- le pare-feu autorise le trafic local nécessaire ;
- le serveur écoute sur une interface accessible depuis Docker Desktop.

### Recherche web lente

Causes possibles :

- moteurs SearxNG indisponibles ;
- latence du réseau ;
- modèle trop lent ;
- mode de recherche approfondie ;
- extraction de pages complexes ;
- contexte du modèle insuffisant ;
- nombre de sources trop élevé.

Mesurer séparément :

1. la recherche ;
2. le téléchargement des pages ;
3. l’embedding ;
4. l’inférence ;
5. le rendu de la réponse.

## 22. Mode Solo

Le Mode Solo privilégie :

- une seule instance Open WebUI ;
- Open Terminal arrêté lorsqu’il n’est pas utilisé ;
- Vane lancé uniquement avec le profil `research` ;
- les ports liés à `127.0.0.1` ;
- un seul compte administrateur protégé ;
- un dossier `workspace` jetable ou versionné ;
- une sauvegarde avant chaque mise à jour ;
- aucun accès distant permanent.

Commandes quotidiennes :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose up -d open-webui
```

Avec terminal :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose up -d open-webui open-terminal
```

Avec recherche Vane :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose --profile research up -d
```

## 23. Mode Studio

Le Mode Studio ajoute :

- des comptes individuels ;
- des groupes et permissions Open WebUI ;
- une instance de test séparée ;
- des versions d’images approuvées ;
- un reverse proxy TLS ;
- une authentification centralisée lorsque justifiée ;
- des journaux d’audit ;
- une politique de rétention ;
- un terminal par équipe ou frontière de confiance ;
- aucune confiance dans le mode multi-utilisateur léger comme isolation de production ;
- une revue juridique des licences et marques ;
- une procédure de révocation des clés ;
- un test de restauration périodique.

Le mode multi-utilisateur d’Open Terminal dans un seul conteneur repose sur des comptes et permissions Unix mais ne constitue pas une séparation forte du noyau, du réseau et des ressources. Pour des utilisateurs non mutuellement fiables, préférer des conteneurs distincts ou un orchestrateur adapté.

## 24. Licences

### Open WebUI

Open WebUI utilise une licence propre comprenant notamment une condition relative à la conservation de la marque Open WebUI au-delà de certains contextes d’utilisation. Le dépôt contient également un historique de licences pour les contributions antérieures.

Avant distribution, personnalisation de marque ou déploiement à grande échelle :

- lire `LICENSE` ;
- lire `LICENSE_HISTORY` ;
- vérifier le nombre d’utilisateurs ;
- documenter les modifications ;
- demander un avis juridique si nécessaire.

### Open Terminal

Open Terminal est publié sous licence MIT au moment de la vérification.

### Vane

Vane est publié sous licence MIT au moment de la vérification.

Les images Docker, dépendances, modèles et moteurs de recherche utilisés par ces applications peuvent posséder des licences supplémentaires.

## 25. Checklist de validation

### 25.1 Open WebUI

- [ ] L’image utilisée est enregistrée avec sa version ou son digest.
- [ ] Le volume `guide-ia-open-webui-data` existe.
- [ ] `WEBUI_SECRET_KEY` est long, persistant et non versionné.
- [ ] Le service est accessible sur `http://127.0.0.1:3000`.
- [ ] L’authentification est active.
- [ ] Le compte administrateur est protégé.
- [ ] Le service devient `healthy`.
- [ ] Une sauvegarde du volume a été créée et vérifiée.

### 25.2 Open Terminal

- [ ] La clé API est définie et non versionnée.
- [ ] Aucun port n’est publié vers l’hôte.
- [ ] Open WebUI le joint par `http://open-terminal:8000`.
- [ ] Seul `workspace` est monté comme dossier de projet.
- [ ] Le socket Docker n’est pas monté.
- [ ] Un test sur un fichier jetable réussit.
- [ ] Les commandes destructives exigent une confirmation humaine.
- [ ] Le terminal est arrêté lorsqu’il n’est pas nécessaire.

### 25.3 Vane

- [ ] Vane répond sur `http://127.0.0.1:3001` lorsque le profil est actif.
- [ ] Le volume `guide-ia-vane-data` existe.
- [ ] Le fournisseur de modèle est documenté.
- [ ] Les clés éventuelles ne sont pas versionnées.
- [ ] Une recherche de test produit des sources vérifiables.
- [ ] Vane reste arrêté lorsque sa fonction spécialisée n’est pas utile.

### 25.4 Critère d’acceptation

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Open WebUI              → interface locale accessible et persistante
Open Terminal           → accessible seulement depuis Open WebUI
Test fichier terminal   → modification limitée et vérifiée
Vane optionnel          → recherche avec citations fonctionnelle
Sauvegardes             → archives lisibles créées
Secrets                 → absents du dépôt Git
Ports                    → uniquement 127.0.0.1 pour les interfaces
```

## 26. Décisions retenues

| Décision | Statut |
|---|---|
| Open WebUI comme interface principale | retenu |
| Open WebUI exposé sur toutes les interfaces | écarté par défaut |
| Authentification désactivée | écarté |
| Open Terminal intégré à Open WebUI | retenu |
| Port Open Terminal publié sur Windows | interdit par défaut |
| Profil Windows complet monté dans Open Terminal | interdit |
| Socket Docker monté dans Open Terminal | interdit |
| Vane obligatoire | écarté |
| Vane comme moteur de recherche optionnel | retenu |
| Vane et Open WebUI considérés comme un seul produit | écarté |
| Versions ou digests enregistrés | obligatoire |
| Sauvegarde avant mise à jour | obligatoire |
| Instance `dev` partageant le volume stable | interdit |

## 27. Sources officielles et primaires vérifiées

### Open WebUI

- [Documentation Open WebUI](https://docs.openwebui.com/)
- [Démarrage rapide Docker](https://docs.openwebui.com/getting-started/quick-start/)
- [Mise à jour et sauvegarde](https://docs.openwebui.com/getting-started/updating/)
- [Variables d’environnement](https://docs.openwebui.com/reference/env-configuration/)
- [Rôles et authentification](https://docs.openwebui.com/features/authentication-access/rbac/roles/)
- [Dépôt GitHub Open WebUI](https://github.com/open-webui/open-webui)
- [Licence Open WebUI](https://github.com/open-webui/open-webui/blob/main/LICENSE)

### Open Terminal

- [Installation Open Terminal](https://docs.openwebui.com/features/open-terminal/setup/installation/)
- [Dépôt GitHub Open Terminal](https://github.com/open-webui/open-terminal)
- [Releases Open Terminal](https://github.com/open-webui/open-terminal/releases)

### Vane

- [Dépôt GitHub Vane](https://github.com/ItzCrazyKns/Vane)
- [Releases Vane](https://github.com/ItzCrazyKns/Vane/releases)

## 28. Résumé

Open WebUI fournit l’interface centrale de la plateforme. Open Terminal lui ajoute une capacité d’action qui doit être traitée comme un privilège sensible. Vane complète éventuellement l’ensemble par une interface spécialisée de recherche et de synthèse avec sources.

La configuration recommandée :

- conserve les interfaces sur la boucle locale ;
- isole Open Terminal sur un réseau Docker interne ;
- ne partage qu’un espace de travail dédié ;
- protège les secrets ;
- sépare les fonctions redondantes ;
- rend Vane optionnel par profil ;
- persiste et sauvegarde chaque volume ;
- prépare la connexion future aux LLM locaux.

Le chapitre suivant installe ComfyUI et définit les workflows graphiques adaptés à la RX 6750 XT.
