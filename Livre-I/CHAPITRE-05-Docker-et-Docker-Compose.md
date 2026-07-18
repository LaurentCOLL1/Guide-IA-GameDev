---
title: "Livre I — Chapitre 5 : Docker et Docker Compose"
id: "DOC-L1-CH02"
status: "draft-review"
version: "1.2.0"
lang: "fr-FR"
book: "Livre I"
chapter: 5
legacy-chapter: 2
canonical-order: 5
last-verified: "2026-07-18"
reference-platform:
  os: "Windows 11 64 bits"
  backend: "Docker Desktop avec WSL 2"
  cpu: "AMD Ryzen 7 2700"
  ram: "32 Go"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Docker et Docker Compose

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L1-CH02`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **État technique vérifié le :** 18 juillet 2026  
> **Résultat attendu :** disposer d’un environnement Docker Desktop et Docker Compose stable, sécurisé, sauvegardable et prêt à héberger les services locaux du guide.

## 1. Objet du chapitre

Ce chapitre installe la couche de services de la plateforme locale.

Docker sera utilisé pour isoler et orchestrer notamment :

- Open WebUI et ses services associés ;
- les bases de données ;
- les bases vectorielles ;
- les interfaces d’administration ;
- les API locales ;
- les outils documentaires ;
- les services de journalisation et de diagnostic ;
- certains runtimes de modèles lorsqu’ils sont réellement compatibles avec le matériel.

Docker ne remplace pas Windows, Godot, Blender ou ComfyUI. Il fournit une couche reproductible pour les composants qui gagnent à être exécutés comme services.

La stratégie retenue est :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Windows 11
├── applications natives
│   ├── Godot
│   ├── Blender
│   ├── ComfyUI et backends AMD compatibles
│   └── outils audio nécessitant le matériel local
└── Docker Desktop avec WSL 2
    ├── interfaces web
    ├── API
    ├── bases de données
    ├── bases vectorielles
    ├── outils documentaires
    └── services auxiliaires
```

Pour la RX 6750 XT de référence, le GPU ne doit pas être considéré comme automatiquement accessible aux conteneurs Linux de Docker Desktop. La documentation officielle de Docker Desktop pour Windows décrit actuellement le calcul GPU conteneurisé avec GPU-PV pour les cartes NVIDIA. Les charges AMD accélérées restent donc, par défaut, exécutées directement sur l’hôte Windows.

## 2. Résultat final attendu

À la fin du chapitre, les commandes suivantes doivent fonctionner :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
wsl --version
docker version
docker info
docker compose version
docker run --rm hello-world
```

Le lecteur doit également disposer :

- d’un backend WSL 2 à jour ;
- d’un emplacement de données Docker choisi explicitement ;
- d’une convention commune pour les projets Compose ;
- d’un premier projet de validation ;
- d’une politique de secrets ;
- d’une stratégie de sauvegarde des volumes ;
- d’une procédure de diagnostic ;
- d’une méthode propre d’arrêt et de redémarrage.

## 3. Positionnement officiel au 18 juillet 2026

### 3.1 Plateforme Windows

La documentation Docker Desktop exige notamment :

- Windows 10 ou Windows 11 64 bits pris en charge ;
- WSL 2.1.5 ou une version ultérieure pour le backend WSL 2 ;
- la virtualisation matérielle activée ;
- un processeur 64 bits compatible SLAT ;
- au moins 8 Go de RAM.

La configuration de référence du guide satisfait les exigences de mémoire avec 32 Go de RAM, sous réserve que la virtualisation et WSL 2 fonctionnent correctement.

### 3.2 Backend retenu

Le backend principal est :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Docker Desktop
└── moteur Linux basé sur WSL 2
```

Ce choix est adapté au projet parce qu’il fournit :

- les conteneurs Linux attendus par la majorité des outils IA locaux ;
- une intégration directe avec PowerShell, Windows Terminal et WSL ;
- une allocation dynamique de la mémoire ;
- la possibilité de travailler avec VS Code côté Windows ou WSL ;
- Docker Compose intégré.

Les conteneurs Windows ne sont pas nécessaires au parcours principal.

### 3.3 Licence Docker Desktop

Docker Desktop est gratuit pour :

- l’usage personnel ;
- l’éducation ;
- les petits organismes répondant aux seuils du contrat Docker ;
- les projets open source non commerciaux.

Une souscription payante est requise dans certaines grandes organisations, administrations et situations commerciales. Les conditions doivent être vérifiées par l’organisation avant déploiement.

Cette question concerne Docker Desktop. Les composants open source Docker Engine et Moby ont leurs propres licences.

## 4. Préparer WSL 2

### 4.1 Vérifier l’état

Ouvrir PowerShell puis exécuter :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
wsl --version
wsl --status
wsl --list --verbose
```

Résultat attendu :

- une version de WSL est affichée ;
- la version par défaut est `2` ;
- les distributions installées utilisent WSL 2 ;
- aucune erreur de virtualisation n’apparaît.

### 4.2 Installer ou mettre à jour WSL

Dans un terminal administrateur :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
wsl --install
wsl --update
wsl --set-default-version 2
```

Redémarrer Windows lorsque le système le demande.

Ne pas installer manuellement un ancien moteur Docker dans une distribution WSL utilisée avec Docker Desktop. Cela crée deux moteurs concurrents, deux ensembles d’images et des erreurs de contexte difficiles à diagnostiquer.

### 4.3 Vérifier la virtualisation

Dans le Gestionnaire des tâches :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Performances
└── Processeur
    └── Virtualisation : Activée
```

En cas d’échec WSL :

1. vérifier la virtualisation dans l’UEFI ;
2. vérifier les fonctions Windows `Plateforme de machine virtuelle` et `Sous-système Windows pour Linux` ;
3. exécuter `wsl --update` ;
4. redémarrer complètement Windows ;
5. tester à nouveau `wsl --list --verbose`.

## 5. Installer Docker Desktop

### 5.1 Télécharger depuis la source officielle

Télécharger Docker Desktop uniquement depuis le site officiel Docker.

Enregistrer avant installation :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Docker Desktop : version téléchargée
Date : AAAA-MM-JJ
Source : site officiel Docker
Mode d’installation : par utilisateur ou tous les utilisateurs
Backend choisi : WSL 2
```

### 5.2 Choisir le mode d’installation

Pour une station personnelle ou un petit poste de production, préférer l’installation par utilisateur lorsqu’elle est proposée et compatible avec les politiques du poste.

L’installation pour tous les utilisateurs reste pertinente lorsque :

- plusieurs comptes Windows utilisent la machine ;
- l’administration centralisée l’exige ;
- les conteneurs Windows sont nécessaires ;
- certaines opérations doivent être gérées par un service privilégié.

Le parcours principal du guide n’exige pas les conteneurs Windows.

### 5.3 Paramètres initiaux

Dans Docker Desktop :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Settings
├── General
│   └── Use the WSL 2 based engine : activé
├── Resources
│   ├── WSL Integration : distribution choisie uniquement
│   └── Advanced : emplacement des données vérifié
└── Kubernetes
    └── désactivé tant qu’il n’est pas explicitement nécessaire
```

Ne pas activer toutes les distributions WSL sans raison. Chaque intégration supplémentaire élargit la surface de diagnostic et d’accès au moteur.

### 5.4 Vérifier l’installation

Dans PowerShell :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker version
docker info
docker compose version
docker context ls
```

Contrôler :

- la présence du client et du serveur ;
- l’utilisation de conteneurs Linux ;
- l’absence d’erreur de connexion au daemon ;
- la disponibilité de la commande `docker compose`.

La syntaxe officielle utilisée dans le guide est :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose
```

La forme historique `docker-compose` ne doit pas être introduite dans les nouveaux scripts.

## 6. Tester le moteur

### 6.1 Test minimal

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker run --rm hello-world
```

Ce test valide :

- le téléchargement d’une image ;
- la création d’un conteneur ;
- son exécution ;
- la communication entre le client et le moteur ;
- sa suppression après exécution.

### 6.2 Test Linux

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker run --rm alpine:3.22 uname -a
```

Résultat attendu : une ligne décrivant un noyau Linux.

### 6.3 Inventaire initial

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker system info
docker image ls
docker container ls --all
docker volume ls
docker network ls
```

Conserver la sortie de `docker version` et `docker info` dans le dossier de diagnostic du projet lors de chaque mise à jour majeure.

## 7. Ressources adaptées au poste de référence

Docker Desktop avec WSL 2 utilise une allocation dynamique. Il reste cependant nécessaire d’éviter qu’un service conteneurisé monopolise les 32 Go de RAM pendant que ComfyUI, Blender ou Godot fonctionnent sur l’hôte.

### 7.1 Point de départ recommandé

Pour le Mode Solo :

| Ressource WSL 2 | Valeur de départ recommandée |
|---|---:|
| Mémoire maximale | 10 Go |
| Processeurs logiques | 6 |
| Swap | 8 Go |

Pour un poste Studio dédié aux services :

| Ressource WSL 2 | Valeur de départ recommandée |
|---|---:|
| Mémoire maximale | 16 Go |
| Processeurs logiques | 8 |
| Swap | 8 à 12 Go |

Ces valeurs ne sont pas des minima universels. Elles servent de point de départ pour la configuration Ryzen 7 2700 et 32 Go de RAM.

### 7.2 Exemple de `.wslconfig`

Créer ou modifier :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
%USERPROFILE%\.wslconfig
```

Exemple Mode Solo :

> **[VSC] Visual Studio Code - Créer ou modifier :** `text %USERPROFILE%\.wslconfig`.

```ini
[wsl2]
memory=10GB
processors=6
swap=8GB
localhostForwarding=true
```

Appliquer les changements :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
wsl --shutdown
```

Relancer ensuite Docker Desktop.

### 7.3 Surveiller les ressources

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker stats
docker compose stats
```

Dans le Gestionnaire des tâches, surveiller également :

- `Docker Desktop` ;
- `com.docker.backend.exe` ;
- `vmmemWSL` ;
- la mémoire système totale ;
- le disque hébergeant le fichier virtuel WSL.

## 8. Organisation des fichiers

### 8.1 Arborescence recommandée

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
plateforme-locale/
├── compose.yaml
├── compose.override.yaml.example
├── .env.example
├── config/
│   ├── open-webui/
│   ├── proxy/
│   └── observabilite/
├── secrets/
│   └── README.md
├── exports/
├── backups/
├── scripts/
└── README.md
```

Ne pas versionner :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
.env
secrets/*
backups/*
exports/*
data/*
*.log
```

### 8.2 Choisir entre bind mount et volume nommé

Utiliser un **bind mount** pour :

- les fichiers de configuration lisibles ;
- les scripts ;
- les fichiers sources modifiés depuis VS Code ;
- les exports destinés à Windows.

Utiliser un **volume nommé** pour :

- les bases de données ;
- les index vectoriels ;
- les données internes d’une application ;
- les caches dont le format appartient au service ;
- les données qui ne doivent pas dépendre d’un chemin Windows précis.

### 8.3 Performance des bind mounts

Docker recommande de conserver les sources fréquemment bind-montées dans le système de fichiers Linux de WSL pour de meilleures performances et pour recevoir correctement les événements de fichiers Linux.

Pour les projets à forte activité disque :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
\\wsl$\Ubuntu\home\<utilisateur>\projects\<projet>
```

ou, depuis WSL :

> **[WSL] Terminal WSL/Bash - Exécuter :** utiliser la distribution Linux indiquée.

```bash
~/projects/<projet>
```

Les documents peu modifiés, sauvegardes et exports peuvent rester sur un volume Windows. Les bases de données ne doivent pas être exécutées directement sur un bind mount Windows sans validation explicite de leurs performances et garanties de cohérence.

## 9. Standards Docker Compose du guide

### 9.1 Nom des fichiers

Le fichier principal est :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
compose.yaml
```

Fichiers complémentaires possibles :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
compose.override.yaml
compose.dev.yaml
compose.studio.yaml
compose.production.yaml
```

Ne pas ajouter la clé historique `version:` au début d’un nouveau fichier Compose.

### 9.2 Règles obligatoires

Chaque service durable doit préciser autant que possible :

- une image versionnée ;
- un nom de service stable ;
- un `healthcheck` ;
- une politique de redémarrage ;
- les volumes persistants ;
- les réseaux autorisés ;
- les ports réellement nécessaires ;
- les limites de ressources pertinentes ;
- le traitement des secrets ;
- le niveau de privilège minimal.

### 9.3 Ports locaux

Une interface destinée uniquement à la machine locale doit être liée à l’adresse de boucle :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
ports:
  - "127.0.0.1:8080:8080"
```

Éviter :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
ports:
  - "8080:8080"
```

La deuxième forme peut rendre le service accessible depuis d’autres interfaces réseau selon la configuration du poste et du pare-feu.

### 9.4 Réseaux

Créer des réseaux fonctionnels lorsque l’architecture le justifie :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
networks:
  frontend:
  backend:
    internal: true
```

Une base de données n’a généralement pas besoin d’être publiée vers Windows. Elle doit être accessible par son nom de service sur le réseau Compose.

### 9.5 Ordre de démarrage

`depends_on` contrôle l’ordre de création, mais un service en cours d’exécution n’est pas nécessairement prêt.

Utiliser :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
depends_on:
  database:
    condition: service_healthy
```

Le service dépendant ne démarre alors qu’après réussite du `healthcheck` de la dépendance.

### 9.6 Profils

Les outils optionnels doivent utiliser des profils :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
services:
  adminer:
    image: adminer:latest
    profiles: ["debug"]
```

Démarrage :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose --profile debug up -d
```

Le Mode Solo peut ainsi laisser les outils d’administration, d’observabilité ou de debug arrêtés tant qu’ils ne sont pas utiles.

## 10. Projet Compose de validation

Créer un dossier temporaire :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
New-Item -ItemType Directory -Force "$HOME\docker-check" | Out-Null
Set-Location "$HOME\docker-check"
```

Créer `compose.yaml` :

> **[VSC] Visual Studio Code - Créer ou modifier :** `compose.yaml`.

```yaml
name: guide-ia-docker-check

services:
  web:
    image: busybox:1.37.0
    command:
      - sh
      - -c
      - |
        mkdir -p /www
        printf 'Docker Compose OK\n' > /www/index.html
        httpd -f -p 8080 -h /www
    ports:
      - "127.0.0.1:18080:8080"
    healthcheck:
      test: ["CMD", "wget", "-q", "-O", "-", "http://127.0.0.1:8080/"]
      interval: 5s
      timeout: 3s
      retries: 10
      start_period: 2s
    restart: "no"
    read_only: true
    tmpfs:
      - /www:size=16m
      - /tmp:size=16m
    cap_drop:
      - ALL
    security_opt:
      - no-new-privileges:true
    mem_limit: 64m
    cpus: 0.50
```

Valider la configuration :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose config
```

Démarrer :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose up -d
docker compose ps
docker compose logs --tail=100
```

Tester :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Invoke-WebRequest http://127.0.0.1:18080
```

Résultat attendu :

> **[SORTIE] Résultat attendu - Ne pas saisir :** comparer avec la sortie obtenue.

```text
Docker Compose OK
```

Arrêter et nettoyer :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell Invoke-WebRequest http://127.0.0.1:18080`.

```powershell
docker compose down
```

## 11. Variables d’environnement et secrets

### 11.1 Fichier `.env.example`

Le dépôt peut contenir :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```dotenv
APP_PORT=8080
APP_LOG_LEVEL=info
```

Le fichier réel `.env` ne doit pas être versionné lorsqu’il contient une information locale ou sensible.

### 11.2 Ne pas confondre interpolation et secret

Les variables d’environnement sont pratiques pour la configuration, mais elles peuvent être visibles :

- dans les processus ;
- dans les diagnostics ;
- dans les journaux ;
- dans l’inspection du conteneur ;
- dans l’historique d’un terminal.

Un mot de passe, une clé d’API ou un certificat doit utiliser les secrets Compose lorsque l’image le permet.

### 11.3 Exemple de secret

> **[VSC] Visual Studio Code - Créer ou modifier :** `.env`.

```yaml
services:
  application:
    image: exemple/application:1.0
    secrets:
      - api_key

secrets:
  api_key:
    file: ./secrets/api_key.txt
```

Dans le conteneur, le secret est monté sous :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
/run/secrets/api_key
```

Le service doit recevoir uniquement les secrets dont il a besoin.

## 12. Sécurité minimale

### 12.1 Interdictions par défaut

Ne pas utiliser sans justification écrite :

> **[VSC] Visual Studio Code - Créer ou modifier :** `text /run/secrets/api_key`.

```yaml
privileged: true
network_mode: host
pid: host
ipc: host
```

Ne pas monter le socket Docker dans un conteneur ordinaire :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
volumes:
  - /var/run/docker.sock:/var/run/docker.sock
```

L’accès au socket Docker équivaut généralement à un contrôle très étendu de l’hôte Docker.

### 12.2 Réduire les privilèges

Lorsque l’image le permet :

> **[VSC] Visual Studio Code - Créer ou modifier :** `yaml volumes: - /var/run/docker.sock:/var/run/docker.sock`.

```yaml
read_only: true
cap_drop:
  - ALL
security_opt:
  - no-new-privileges:true
```

Ajouter uniquement les capacités nécessaires.

### 12.3 Images

Pour un environnement reproductible :

- éviter `latest` dans les services durables ;
- enregistrer la version de l’image ;
- utiliser un digest pour une release figée ;
- lire les notes de version avant mise à jour ;
- tester la mise à jour sur une copie ou une branche dédiée ;
- conserver une procédure de retour arrière.

### 12.4 Interfaces d’administration

Les interfaces de base de données, tableaux de bord et consoles de debug doivent :

- rester désactivées hors besoin ;
- être liées à `127.0.0.1` ;
- utiliser un profil Compose ;
- ne pas être exposées directement à Internet ;
- exiger une authentification lorsqu’elles accèdent à des données sensibles.

## 13. Communication avec les services Windows

Un conteneur Docker Desktop peut joindre un service exécuté sur Windows avec :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
host.docker.internal
```

Exemple : un service Windows écoute sur le port `11434` :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
http://host.docker.internal:11434
```

Cette adresse sera utilisée plus tard pour permettre à une interface conteneurisée de joindre un runtime IA lancé directement sur Windows.

Ne pas remplacer cette adresse par une IP hôte codée en dur, car l’adresse interne peut changer.

## 14. Stratégie GPU AMD

### 14.1 Règle du projet

Pour la RX 6750 XT :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
GPU AMD
├── ComfyUI natif Windows : voie principale selon backend compatible
├── applications Windows ML ou DirectML : selon prise en charge
├── ZLUDA isolé : option expérimentale
└── Docker Desktop Linux GPU : non requis et non présumé compatible
```

Les conteneurs hébergent en priorité les services qui n’ont pas besoin d’un accès direct au GPU AMD.

### 14.2 Séparer orchestration et calcul

Exemple :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Open WebUI dans Docker
        │
        ├── HTTP vers Ollama Windows
        ├── HTTP vers LocalAI Windows si nécessaire
        └── HTTP vers une API ComfyUI Windows
```

Cette architecture évite de rendre toute la plateforme dépendante d’une prise en charge GPU conteneurisée absente ou expérimentale.

## 15. Sauvegarde et restauration

### 15.1 Ce qui doit être sauvegardé

- `compose.yaml` et ses variantes ;
- `.env.example` ;
- les configurations ;
- les fichiers de secrets dans un coffre séparé ;
- les exports des bases ;
- les volumes nommés importants ;
- la liste des images et versions ;
- les scripts de restauration.

### 15.2 Inventaire

> **[VSC] Visual Studio Code - Créer ou modifier :** `.env.example`.

```powershell
docker compose config > exports\compose-resolved.yaml
docker image ls --digests > exports\docker-images.txt
docker volume ls > exports\docker-volumes.txt
docker version > exports\docker-version.txt
```

Le fichier `compose-resolved.yaml` peut contenir des valeurs interpolées. Vérifier qu’il ne contient aucun secret avant de le partager ou de le versionner.

### 15.3 Sauvegarde d’un volume

Exemple générique :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker run --rm `
  --mount source=mon_volume,target=/data,readonly `
  --mount type=bind,source="$PWD\backups",target=/backup `
  alpine:3.22 `
  tar -czf /backup/mon_volume.tar.gz -C /data .
```

### 15.4 Restauration d’un volume

> **[VSC] Visual Studio Code - Créer ou modifier :** `tar -czf /backup/mon_volume.tar.gz -C /data .`.

```powershell
docker volume create mon_volume

docker run --rm `
  --mount source=mon_volume,target=/data `
  --mount type=bind,source="$PWD\backups",target=/backup,readonly `
  alpine:3.22 `
  tar -xzf /backup/mon_volume.tar.gz -C /data
```

Pour une base de données, préférer également ses outils d’export logique : `pg_dump`, `mysqldump` ou équivalent. Une archive brute du volume ne remplace pas toujours une sauvegarde cohérente de l’application.

### 15.5 Avant une réinstallation

Docker précise que la désinstallation de Docker Desktop détruit les conteneurs, images, volumes et autres données locales. Sauvegarder avant :

- une désinstallation ;
- un retour à une ancienne version ;
- une réinitialisation d’usine ;
- un déplacement du disque WSL ;
- une migration vers une autre machine.

## 16. Commandes opérationnelles

### 16.1 Vérifier la configuration

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose config
docker compose config --services
docker compose config --volumes
docker compose config --networks
```

### 16.2 Télécharger les images

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose pull
```

Sur une connexion limitée ou un disque lent :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose --parallel 1 pull
```

### 16.3 Démarrer

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose up -d
docker compose ps
```

### 16.4 Consulter les journaux

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose logs --tail=200
docker compose logs --follow nom_du_service
```

### 16.5 Redémarrer un service

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose restart nom_du_service
```

### 16.6 Recréer après modification

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose up -d --force-recreate nom_du_service
```

### 16.7 Arrêter sans détruire les données

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose down
```

### 16.8 Commande destructive

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose down --volumes
```

> **Avertissement :** `--volumes` supprime les volumes déclarés par le projet. Cette commande exige une sauvegarde vérifiée ou la certitude que les données sont jetables.

## 17. Diagnostic par couches

### Couche 1 — Windows et WSL

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
wsl --status
wsl --version
wsl --list --verbose
```

### Couche 2 — Docker Desktop

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker version
docker info
docker context show
```

### Couche 3 — Compose

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose version
docker compose config
```

### Couche 4 — Projet

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose ps
docker compose logs --tail=200
docker compose events
```

### Couche 5 — Ressources

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker stats
docker system df
```

### Couche 6 — Réseau

Tester depuis Windows :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Test-NetConnection 127.0.0.1 -Port 8080
```

Tester depuis un conteneur vers Windows :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker run --rm alpine:3.22 sh -c "wget -q -O - http://host.docker.internal:8000"
```

### Couche 7 — Réinitialisation contrôlée

Avant toute réinitialisation :

1. exporter les bases ;
2. sauvegarder les volumes ;
3. enregistrer les versions ;
4. arrêter les services ;
5. conserver les journaux utiles ;
6. vérifier que les sauvegardes sont lisibles.

Ne pas utiliser immédiatement la réinitialisation d’usine comme première méthode de diagnostic.

## 18. Mode Solo

Le Mode Solo applique les règles suivantes :

- démarrer uniquement les services utilisés pendant la session ;
- laisser Kubernetes désactivé ;
- utiliser des profils pour les outils optionnels ;
- limiter la mémoire WSL afin de préserver ComfyUI, Blender et Godot ;
- utiliser des volumes nommés pour les bases ;
- effectuer une sauvegarde avant chaque mise à jour majeure ;
- conserver une commande unique pour démarrer et arrêter la plateforme.

Exemple :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose up -d
docker compose down
```

## 19. Mode Studio

Le Mode Studio ajoute :

- une liste de versions Docker Desktop approuvées ;
- un registre des images et digests autorisés ;
- des fichiers Compose séparés par environnement ;
- une gestion centralisée des secrets ;
- des sauvegardes automatisées et testées ;
- un réseau de développement documenté ;
- un contrôle des licences Docker Desktop ;
- une validation en préproduction avant mise à jour ;
- une procédure de restauration chronométrée ;
- une politique de rétention des journaux.

Les fichiers locaux ne doivent pas être la seule copie de la configuration d’un service partagé.

## 20. Erreurs fréquentes

### Docker Desktop ne démarre pas

Causes probables :

- virtualisation désactivée ;
- WSL trop ancien ;
- fonctions Windows manquantes ;
- hyperviseur désactivé au démarrage ;
- disque système saturé ;
- corruption du disque virtuel Docker.

### Le client ne trouve pas le daemon

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
error during connect
Cannot connect to the Docker daemon
```

Vérifier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker context ls
docker context use desktop-linux
docker version
```

Le nom du contexte peut varier. Sélectionner le contexte Docker Desktop réellement présent sur le poste.

### Un service démarre avant sa base

Ajouter :

- un `healthcheck` à la base ;
- `condition: service_healthy` dans `depends_on` ;
- une logique de reconnexion dans l’application.

### Les fichiers sont très lents

- déplacer les sources à forte activité dans le système de fichiers WSL ;
- utiliser un volume nommé pour les données internes ;
- réduire les bind mounts massifs depuis `C:\` ;
- exclure seulement les dossiers justifiés des analyses en temps réel, après évaluation de sécurité ;
- mesurer avant et après chaque changement.

### Le disque Docker grossit

> **[VSC] Visual Studio Code - Créer ou modifier :** `C:\`.

```powershell
docker system df
docker image prune
docker builder prune
```

Ne pas exécuter `docker system prune --all --volumes` sans inventaire et sauvegarde. Cette commande peut supprimer images, caches et volumes utiles.

## 21. Validation du chapitre

### 21.1 Checklist obligatoire

- [ ] La virtualisation matérielle est activée.
- [ ] WSL 2 est installé et à jour.
- [ ] Docker Desktop utilise le backend WSL 2.
- [ ] `docker version` affiche un client et un serveur.
- [ ] `docker compose version` fonctionne.
- [ ] `hello-world` s’exécute correctement.
- [ ] Le projet Compose de validation devient `healthy`.
- [ ] L’interface de validation répond uniquement sur `127.0.0.1:18080`.
- [ ] Les limites WSL sont adaptées au poste.
- [ ] L’emplacement des données Docker est connu.
- [ ] Les volumes persistants ont une stratégie de sauvegarde.
- [ ] Les secrets ne sont pas versionnés.
- [ ] Les services GPU AMD restent sur l’hôte sauf preuve de compatibilité.
- [ ] La licence Docker Desktop est compatible avec le contexte d’utilisation.
- [ ] La procédure d’arrêt et de restauration est documentée.

### 21.2 Critère d’acceptation

Le chapitre est validé lorsque :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
wsl --version             → succès
docker version            → client et serveur disponibles
docker compose version    → succès
hello-world               → succès
compose de validation     → healthy
requête HTTP locale       → Docker Compose OK
arrêt du projet            → aucune donnée importante perdue
```

## 22. Décisions retenues

| Décision | Statut |
|---|---|
| Docker Desktop avec WSL 2 comme parcours Windows principal | retenu |
| Conteneurs Linux pour les services locaux | retenu |
| Conteneurs Windows dans le parcours principal | écarté |
| Commande `docker compose` | obligatoire |
| GPU AMD requis dans Docker Desktop | écarté |
| Calcul AMD lourd exécuté sur l’hôte Windows | retenu |
| Volumes nommés pour les bases et états internes | retenu |
| Ports locaux liés à `127.0.0.1` | obligatoire |
| Secrets stockés dans Git | interdit |
| Kubernetes activé par défaut | écarté |
| Sauvegarde avant mise à jour ou réinitialisation | obligatoire |

## 23. Sources officielles vérifiées

- [Installation de Docker Desktop sur Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
- [Backend WSL 2 de Docker Desktop](https://docs.docker.com/desktop/features/wsl/)
- [Bonnes pratiques WSL 2](https://docs.docker.com/desktop/features/wsl/best-practices/)
- [Exigences de permissions sous Windows](https://docs.docker.com/desktop/setup/install/windows-permission-requirements/)
- [Référence Docker Compose](https://docs.docker.com/reference/compose-file/)
- [Ordre de démarrage et healthchecks](https://docs.docker.com/compose/how-tos/startup-order/)
- [Gestion des secrets Compose](https://docs.docker.com/compose/how-tos/use-secrets/)
- [Variables d’environnement Compose](https://docs.docker.com/compose/how-tos/environment-variables/)
- [Réseau Docker Desktop](https://docs.docker.com/desktop/features/networking/networking-how-tos/)
- [Sauvegarde et restauration Docker Desktop](https://docs.docker.com/desktop/settings-and-maintenance/backup-and-restore/)
- [Volumes Docker](https://docs.docker.com/engine/storage/volumes/)
- [Prise en charge GPU Docker Desktop pour Windows](https://docs.docker.com/desktop/features/gpu/)
- [Licence Docker Desktop](https://docs.docker.com/subscription/desktop-license/)

## 24. Résumé

Docker Desktop et Docker Compose constituent la couche de services reproductible du projet. Sur la configuration Windows et AMD de référence, Docker héberge les interfaces, bases, API et outils auxiliaires tandis que les charges GPU AMD restent par défaut sur l’hôte.

Une installation correcte doit être :

- fondée sur WSL 2 à jour ;
- limitée en ressources ;
- organisée avec Compose ;
- protégée par des réseaux et ports minimaux ;
- dépourvue de secrets versionnés ;
- sauvegardable ;
- testable ;
- réversible.

Le chapitre suivant installe Open WebUI, Open Terminal et Vane sur cette base.
