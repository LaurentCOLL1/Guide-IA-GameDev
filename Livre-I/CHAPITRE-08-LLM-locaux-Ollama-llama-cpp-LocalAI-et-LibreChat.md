---
title: "Livre I — Chapitre 8 : LLM locaux avec Ollama, llama.cpp, LocalAI et LibreChat"
id: "DOC-L1-CH05"
status: "draft-review"
version: "1.1.0"
lang: "fr-FR"
book: "Livre I"
chapter: 8
legacy-chapter: 5
canonical-order: 8
last-verified: "2026-07-18"
reference-hardware:
  gpu: "AMD Radeon RX 6750 XT 12 Go"
  cpu: "AMD Ryzen 7 2700"
  ram: "32 Go"
  os: "Windows 11 64 bits"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# LLM locaux avec Ollama, llama.cpp, LocalAI et LibreChat

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L1-CH05`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **État technique vérifié le :** 18 juillet 2026  
> **Résultat attendu :** disposer d’au moins un moteur LLM local reproductible, relié à Open WebUI ou LibreChat, avec une stratégie CPU et GPU AMD mesurée.

## 1. Objet du chapitre

Ce chapitre installe et organise les moteurs de modèles de langage locaux.

Quatre composants sont distingués :

| Composant | Rôle principal | Statut dans le guide |
|---|---|---|
| Ollama | installation simple, gestion des modèles et API locale | parcours principal |
| llama.cpp | moteur de référence GGUF, benchmark et contrôle fin | obligatoire comme outil de diagnostic |
| LocalAI | passerelle multi-backends compatible avec des API courantes | optionnel |
| LibreChat | interface conversationnelle et agentique alternative | optionnel |

Aucun de ces composants ne doit être présenté comme un modèle. Ils chargent et servent des modèles obtenus séparément.

Le pipeline retenu est :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Modèle et licence vérifiés
        ↓
Format et quantification choisis
        ↓
Ollama ou llama.cpp
        ↓
API locale liée à 127.0.0.1
        ↓
Open WebUI, LibreChat ou application du projet
        ↓
Mesures, validation et journal de décision
```

## 2. Architecture recommandée

### 2.1 Parcours principal

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
Windows 11
├── Ollama natif
│   ├── API : http://127.0.0.1:11434
│   ├── modèles gérés par Ollama
│   └── accélération AMD testée puis mesurée
├── llama.cpp natif
│   ├── binaire CPU de référence
│   ├── binaire Vulkan expérimental contrôlé
│   └── modèles GGUF versionnés par manifeste
└── Docker Desktop
    ├── Open WebUI
    ├── LibreChat, uniquement lorsqu’il remplace Open WebUI
    └── LocalAI CPU, si une passerelle unifiée est nécessaire
```

### 2.2 Pourquoi Ollama reste natif

L’exécution native Windows simplifie :

- l’accès au pilote Radeon ;
- la détection du GPU ;
- l’accès aux modèles stockés sur un disque local ;
- les mises à jour ;
- les journaux ;
- la connexion depuis les interfaces Docker avec `host.docker.internal`.

Le conteneur Ollama n’est pas le parcours principal sur cette machine AMD, car Docker Desktop ne fournit pas un accès GPU AMD Windows équivalent au passthrough Linux natif.

### 2.3 Pourquoi llama.cpp est conservé

llama.cpp fournit :

- une exécution CPU sans service permanent ;
- des binaires Windows CPU, Vulkan et HIP ;
- des modèles GGUF directement inspectables ;
- le contrôle des couches envoyées au GPU ;
- un serveur compatible avec une partie de l’API OpenAI ;
- un outil de benchmark séparé ;
- une référence utile lorsque l’orchestration d’Ollama masque un détail.

## 3. Principes obligatoires

### 3.1 Local ne signifie pas autorisé

Avant tout téléchargement, vérifier :

- la licence du modèle ;
- les usages commerciaux autorisés ou interdits ;
- les obligations d’attribution ;
- les restrictions de redistribution ;
- les restrictions de contenu ;
- la provenance de la quantification ;
- la compatibilité du format avec le moteur choisi.

Le fichier du modèle et le code du moteur ont des licences distinctes.

### 3.2 Un modèle doit être identifiable

Chaque modèle accepté possède une fiche :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
id: LLM-EXEMPLE-001
name: nom-affiche
source: https://source-officielle.example/model
publisher: organisation
base_model: nom-du-modele-de-base
revision: commit-ou-tag
format: GGUF
quantization: Q4_K_M
filename: modele-q4_k_m.gguf
sha256: empreinte
parameter_count: 8B
context_tested: 4096
license: licence-verifiee
runtime_tested:
  - ollama
  - llama.cpp-vulkan
hardware_tested: RX-6750-XT-12GB
status: review
```

Les modèles ne sont pas versionnés dans Git. Le manifeste, la licence, la source et l’empreinte le sont.

### 3.3 Une interface n’est pas un moteur

Open WebUI et LibreChat ne doivent pas être confondus avec Ollama, llama.cpp ou LocalAI.

Une interface peut continuer à répondre alors que :

- le moteur est arrêté ;
- le modèle n’est pas chargé ;
- l’API pointe vers une mauvaise adresse ;
- l’inférence est retombée sur le CPU ;
- le contexte dépasse la mémoire disponible.

Le diagnostic commence toujours par le moteur.

## 4. Profils de modèles pour 12 Go de VRAM

Les valeurs suivantes sont des profils de départ, pas des garanties universelles.

| Profil | Taille indicative | Quantification de départ | Usage |
|---|---:|---|---|
| S | 1 à 4 milliards de paramètres | Q4 ou Q5 | classification, résumé court, outils légers |
| M | 7 à 9 milliards | Q4_K_M ou équivalent | assistant général principal |
| L | 12 à 14 milliards | Q4 avec contexte limité | qualité supérieure, exécution hybride possible |
| XL | plus de 20 milliards | quantification forte | CPU ou hybride lent, usage exceptionnel |

Le besoin mémoire dépend également :

- du contexte ;
- du cache KV ;
- du nombre de requêtes parallèles ;
- de l’architecture du modèle ;
- des couches offloadées ;
- du type de cache ;
- des composants multimodaux.

### 4.1 Configuration prudente initiale

Pour la RX 6750 XT et 32 Go de RAM :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
contexte initial : 4096 jetons
modèles simultanés : 1
requêtes parallèles : 1
profil de départ : 7B à 9B en Q4_K_M
```

Augmenter une seule variable à la fois après mesure.

### 4.2 Choisir une quantification

Point de départ recommandé :

- `Q4_K_M` pour un compromis mémoire et qualité ;
- `Q5_K_M` lorsque la mémoire le permet et que la qualité progresse réellement ;
- `Q8_0` pour les petits modèles ou les tests de référence ;
- quantification plus forte uniquement après comparaison sur les tâches du projet.

Le nom exact des quantifications dépend du format et de l’outil.

## 5. Installer Ollama sous Windows

### 5.1 Installation

Télécharger l’installateur Windows depuis le site officiel Ollama.

L’installation standard :

- s’effectue dans le compte utilisateur ;
- ajoute la commande `ollama` au PATH ;
- démarre une application en arrière-plan ;
- expose l’API sur `http://localhost:11434`.

Vérifier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
ollama --version
Get-Command ollama
Invoke-RestMethod http://127.0.0.1:11434/api/tags
```

### 5.2 Déplacer le stockage des modèles

Les modèles peuvent occuper plusieurs dizaines ou centaines de gigaoctets.

Créer un dossier dédié :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
New-Item -ItemType Directory -Force "D:\IA\ollama-models" | Out-Null
```

Créer la variable utilisateur :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell New-Item -ItemType Directory -Force "D:\IA\ollama-models" | Out-Null`.

```powershell
[Environment]::SetEnvironmentVariable(
  "OLLAMA_MODELS",
  "D:\IA\ollama-models",
  "User"
)
```

Quitter complètement Ollama depuis la zone de notification puis le relancer.

Vérifier que les nouveaux téléchargements utilisent le dossier choisi.

### 5.3 Paramètres prudents

Variables utilisateur de départ :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
[Environment]::SetEnvironmentVariable("OLLAMA_HOST", "127.0.0.1:11434", "User")
[Environment]::SetEnvironmentVariable("OLLAMA_CONTEXT_LENGTH", "4096", "User")
[Environment]::SetEnvironmentVariable("OLLAMA_NUM_PARALLEL", "1", "User")
[Environment]::SetEnvironmentVariable("OLLAMA_MAX_LOADED_MODELS", "1", "User")
```

Redémarrer Ollama après toute modification.

Ne pas utiliser `0.0.0.0` sans pare-feu, authentification ajoutée par un proxy et besoin réseau documenté.

## 6. Premier modèle Ollama

### 6.1 Choisir un petit modèle de validation

Le premier test doit utiliser un modèle léger dont :

- la licence est lisible ;
- la source est officielle ;
- le format est pris en charge ;
- la taille permet un diagnostic rapide ;
- le nom exact est enregistré dans le manifeste.

Télécharger :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
ollama pull <modele-de-validation>
```

Exécuter :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
ollama run <modele-de-validation>
```

Prompt de validation :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Réponds uniquement avec : OLLAMA_OK
```

### 6.2 Commandes essentielles

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
ollama list
ollama show <modele>
ollama ps
ollama stop <modele>
ollama rm <modele>
```

`ollama ps` doit être exécuté pendant que le modèle est chargé.

La colonne `PROCESSOR` permet d’observer :

- `100% GPU` ;
- `100% CPU` ;
- une répartition CPU/GPU.

Ne pas conclure à une accélération uniquement parce que l’application répond.

### 6.3 Tester l’API native

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
$body = @{
  model = "<modele-de-validation>"
  prompt = "Réponds uniquement avec API_OK"
  stream = $false
} | ConvertTo-Json

Invoke-RestMethod `
  -Uri "http://127.0.0.1:11434/api/generate" `
  -Method Post `
  -ContentType "application/json" `
  -Body $body
```

### 6.4 Tester l’API compatible OpenAI

> **[VSC] Visual Studio Code - Créer ou modifier :** `-ContentType "application/json"`.

```powershell
$body = @{
  model = "<modele-de-validation>"
  messages = @(
    @{
      role = "user"
      content = "Réponds uniquement avec OPENAI_API_OK"
    }
  )
} | ConvertTo-Json -Depth 5

Invoke-RestMethod `
  -Uri "http://127.0.0.1:11434/v1/chat/completions" `
  -Method Post `
  -Headers @{ Authorization = "Bearer ollama" } `
  -ContentType "application/json" `
  -Body $body
```

La compatibilité OpenAI est partielle. Une application doit être testée avec les endpoints réellement utilisés.

## 7. Accélération AMD dans Ollama

### 7.1 Essai standard

Ollama Windows annonce la prise en charge des GPU Radeon, mais la liste ROCm Windows officielle ne contient pas toutes les cartes AMD.

Procédure :

1. démarrer Ollama sans variable expérimentale ;
2. charger un modèle ;
3. exécuter `ollama ps` ;
4. enregistrer la colonne `PROCESSOR` ;
5. relever le temps de chargement et les jetons par seconde ;
6. conserver les journaux en cas de retour CPU.

### 7.2 Vulkan expérimental

Ollama propose un backend Vulkan expérimental pour élargir la prise en charge GPU.

Créer un laboratoire séparé :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
[Environment]::SetEnvironmentVariable("OLLAMA_VULKAN", "1", "User")
```

Quitter et relancer Ollama, puis refaire exactement le même benchmark.

Pour désactiver le test :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
[Environment]::SetEnvironmentVariable("OLLAMA_VULKAN", $null, "User")
```

Le backend Vulkan ne devient pas le parcours stable avant :

- trois exécutions réussies ;
- absence de sortie corrompue ;
- absence de crash pilote ;
- gain mesurable ;
- résultat de qualité comparable ;
- possibilité de revenir au CPU.

### 7.3 Diagnostic Ollama

Journaux Windows :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
%LOCALAPPDATA%\Ollama\app.log
%LOCALAPPDATA%\Ollama\server.log
%LOCALAPPDATA%\Ollama\upgrade.log
```

Collecte :

> **[VSC] Visual Studio Code - Créer ou modifier :** `text %LOCALAPPDATA%\Ollama\app.log %LOCALAPPDATA%\Ollama\server.log %LOCALAPPDATA%\Ollama\upgrade.log`.

```powershell
ollama --version
ollama list
ollama ps
Get-Content "$env:LOCALAPPDATA\Ollama\server.log" -Tail 200
```

## 8. Installer llama.cpp

### 8.1 Binaires officiels

Télécharger depuis les releases officielles :

- le paquet Windows x64 CPU ;
- le paquet Windows x64 Vulkan pour le laboratoire AMD ;
- éventuellement le paquet HIP uniquement pour un test explicitement compatible.

Ne pas mélanger les DLL de plusieurs paquets dans le même dossier.

Arborescence :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
D:\IA\llama.cpp\
├── cpu\
│   └── <build-id>\
├── vulkan\
│   └── <build-id>\
├── hip\
│   └── <build-id>\
├── models\
├── benchmarks\
└── manifests\
```

Enregistrer le numéro de build ou le commit de chaque paquet.

### 8.2 Vérification CPU

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Set-Location "D:\IA\llama.cpp\cpu\<build-id>"
.\llama-cli.exe --version
```

Test :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell Set-Location "D:\IA\llama.cpp\cpu\<build-id>" .\llama-cli.exe --version`.

```powershell
.\llama-cli.exe `
  -m "D:\IA\llama.cpp\models\modele.gguf" `
  -p "Réponds uniquement avec LLAMA_CPP_CPU_OK" `
  -n 32 `
  -c 4096 `
  -t 8
```

### 8.3 Vérification Vulkan

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell .\llama-cli.exe`.

```powershell
Set-Location "D:\IA\llama.cpp\vulkan\<build-id>"
.\llama-cli.exe --version
```

Test avec offload progressif :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell Set-Location "D:\IA\llama.cpp\vulkan\<build-id>" .\llama-cli.exe --version`.

```powershell
.\llama-cli.exe `
  -m "D:\IA\llama.cpp\models\modele.gguf" `
  -p "Réponds uniquement avec LLAMA_CPP_VULKAN_OK" `
  -n 32 `
  -c 4096 `
  -ngl 20
```

Augmenter `-ngl` progressivement. Ne pas commencer par un offload maximal sur un modèle non testé.

### 8.4 Benchmark

CPU :

> **[VSC] Visual Studio Code - Créer ou modifier :** `-m "D:\IA\llama.cpp\models\modele.gguf"`.

```powershell
.\llama-bench.exe `
  -m "D:\IA\llama.cpp\models\modele.gguf" `
  -t 8 `
  -ngl 0
```

Vulkan :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell .\llama-bench.exe`.

```powershell
.\llama-bench.exe `
  -m "D:\IA\llama.cpp\models\modele.gguf" `
  -t 8 `
  -ngl 999
```

Conserver la sortie brute avec :

- build llama.cpp ;
- pilote AMD ;
- modèle et empreinte ;
- quantification ;
- contexte ;
- nombre de threads ;
- nombre de couches GPU ;
- température du système ;
- date.

## 9. Serveur llama.cpp

### 9.1 Démarrer localement

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
.\llama-server.exe `
  -m "D:\IA\llama.cpp\models\modele.gguf" `
  --host 127.0.0.1 `
  --port 8081 `
  -c 4096 `
  -t 8 `
  -ngl 20
```

Vérifier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Invoke-RestMethod http://127.0.0.1:8081/health
```

### 9.2 Connexion depuis Docker

Depuis Open WebUI ou LibreChat :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
http://host.docker.internal:8081/v1
```

Ne pas publier simultanément plusieurs moteurs sur le même port.

## 10. Installer LocalAI

### 10.1 Positionnement

LocalAI est utilisé lorsque le projet a besoin :

- d’une passerelle compatible avec plusieurs familles d’API ;
- de plusieurs backends spécialisés ;
- d’une configuration de modèles en YAML ;
- d’une administration centralisée ;
- d’un environnement Studio partagé.

Il n’est pas requis pour un Mode Solo déjà satisfait par Ollama.

### 10.2 Parcours Windows sûr

Sur Docker Desktop Windows avec la RX 6750 XT, le parcours par défaut est CPU.

Créer `.env` :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```dotenv
LOCALAI_IMAGE=localai/localai:vX.Y.Z
LOCALAI_PORT=8080
```

Le tag doit être remplacé par une version testée et figée.

Créer `compose.yaml` :

> **[VSC] Visual Studio Code - Créer ou modifier :** `compose.yaml`.

```yaml
name: guide-ia-localai

services:
  localai:
    image: ${LOCALAI_IMAGE:?Définir LOCALAI_IMAGE}
    ports:
      - "127.0.0.1:${LOCALAI_PORT:-8080}:8080"
    volumes:
      - localai_models:/models
      - ./config:/config:ro
    environment:
      MODELS_PATH: /models
      THREADS: "8"
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-fsS", "http://127.0.0.1:8080/readyz"]
      interval: 15s
      timeout: 5s
      retries: 20
      start_period: 60s

volumes:
  localai_models:
```

Valider et démarrer :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose config
docker compose up -d
docker compose ps
docker compose logs --tail=200
```

### 10.3 Vulkan LocalAI

LocalAI publie des images Vulkan. Elles nécessitent que le conteneur accède aux périphériques GPU de l’hôte.

Cette voie est adaptée en priorité à un hôte Linux natif correctement configuré.

Elle n’est pas présumée fonctionnelle avec le GPU AMD depuis Docker Desktop Windows. Toute exception doit être démontrée et documentée.

## 11. Installer LibreChat

### 11.1 Rôle

LibreChat est une interface alternative à Open WebUI.

Elle apporte notamment :

- plusieurs endpoints ;
- agents et outils ;
- RAG ;
- MCP ;
- MongoDB ;
- MeiliSearch ;
- services vectoriels selon la configuration.

Elle utilise plus de services qu’une interface minimale.

### 11.2 Installation Docker

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git clone https://github.com/danny-avila/LibreChat.git
Set-Location LibreChat
Copy-Item .env.example .env
docker compose up -d
```

Ouvrir :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text

> **[WEB] Navigateur internet - Ouvrir :** utiliser la page officielle indiquée ci-dessous.

http://127.0.0.1:3080
```

Le premier compte créé devient administrateur selon le parcours Docker documenté. Vérifier immédiatement les paramètres d’inscription, d’authentification et d’accès réseau.

### 11.3 Relier LibreChat à Ollama

Dans `librechat.yaml`, ajouter un endpoint personnalisé :

> **[VSC] Visual Studio Code - Créer ou modifier :** `librechat.yaml`.

```yaml
version: 1.2.1

endpoints:
  custom:
    - name: Ollama
      apiKey: ollama
      baseURL: http://host.docker.internal:11434/v1/
      models:
        fetch: true
      titleConvo: true
      titleModel: <modele-de-titre>
```

Monter `librechat.yaml` dans le conteneur puis redémarrer :

> **[VSC] Visual Studio Code - Créer ou modifier :** `librechat.yaml`.

```powershell
docker compose down
docker compose up -d
```

Le modèle de titre doit être léger ou désactivé si cette fonction augmente inutilement la mémoire.

### 11.4 Règle Mode Solo

Ne pas exécuter en permanence Open WebUI et LibreChat sur la même station sans besoin réel.

Choisir une interface principale :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Open WebUI : parcours recommandé du guide
LibreChat : alternative pour tests ou besoins spécifiques
```

## 12. Connexions entre composants

| Client | Moteur sur Windows | Adresse depuis Docker |
|---|---|---|
| Open WebUI | Ollama | `http://host.docker.internal:11434` |
| LibreChat | Ollama compatible OpenAI | `http://host.docker.internal:11434/v1/` |
| Open WebUI | llama-server | `http://host.docker.internal:8081/v1` |
| LibreChat | llama-server | `http://host.docker.internal:8081/v1` |
| Open WebUI | LocalAI | `http://localai:8080/v1` ou adresse du projet |
| LibreChat | LocalAI | endpoint personnalisé compatible |

Les adresses `localhost` dans un conteneur désignent le conteneur lui-même, pas Windows.

## 13. Sécurité des API locales

### 13.1 Lier à la boucle locale

Utiliser :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
127.0.0.1
```

et non :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
0.0.0.0
```

sauf décision réseau documentée.

### 13.2 Ne pas supposer une authentification

Une API locale peut accepter les requêtes sans authentification forte.

Avant toute exposition réseau :

- ajouter un reverse proxy ;
- activer TLS ;
- exiger une authentification ;
- limiter les origines ;
- appliquer le pare-feu ;
- séparer les comptes ;
- enregistrer les accès ;
- limiter les modèles et outils disponibles.

### 13.3 Prompts et données sensibles

Ne pas envoyer automatiquement :

- secrets ;
- fichiers privés complets ;
- données personnelles inutiles ;
- clés d’API ;
- sauvegardes ;
- bases de données brutes.

Les journaux d’inférence doivent être soumis à une politique de rétention.

## 14. Paramètres de génération

Les paramètres doivent être enregistrés avec les tests :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
temperature: 0.7
top_p: 0.9
top_k: 40
repeat_penalty: 1.1
seed: 42
context: 4096
max_tokens: 512
```

Les noms et valeurs acceptés varient selon le moteur.

Pour un test de régression :

- température faible ou nulle ;
- seed fixée lorsque prise en charge ;
- prompt stable ;
- même modèle et même quantification ;
- même contexte ;
- même backend.

## 15. Jeux de tests

### 15.1 Test fonctionnel

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Réponds uniquement avec : TEST_LLM_OK
```

### 15.2 Test JSON

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Retourne uniquement un objet JSON valide contenant les clés status et value.
status doit valoir ok et value doit valoir 42.
```

### 15.3 Test français

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Résume en trois phrases un paragraphe technique en français sans inventer de fait.
```

### 15.4 Test code

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Écris une fonction GDScript typée qui additionne deux entiers, puis un test minimal.
```

Le code produit doit être exécuté ou analysé. Une réponse plausible ne constitue pas une validation.

### 15.5 Test de refus d’invention

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Lorsque l’information manque, réponds exactement : INFORMATION_INSUFFISANTE
```

## 16. Mesures obligatoires

Pour chaque couple modèle-moteur :

| Mesure | Description |
|---|---|
| temps de chargement | démarrage jusqu’au modèle prêt |
| premier jeton | délai avant la première sortie |
| débit | jetons générés par seconde |
| RAM maximale | pic système observé |
| VRAM maximale | pic GPU observé |
| répartition | CPU, GPU ou hybride |
| contexte testé | nombre de jetons |
| stabilité | réussite sur trois essais |
| qualité | grille liée aux tâches du projet |

Fiche :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
runtime: ollama
runtime_version: version
model_id: LLM-EXEMPLE-001
backend: vulkan
context: 4096
parallel_requests: 1
load_time_seconds: 0
first_token_seconds: 0
tokens_per_second: 0
peak_ram_gb: 0
peak_vram_gb: 0
processor_split: "CPU/GPU"
result: pass
```

## 17. Sauvegarde et restauration

### 17.1 Sauvegarder les informations, pas nécessairement tous les poids

Conserver dans Git :

- manifestes ;
- empreintes ;
- licences ;
- sources ;
- Modelfiles ;
- configurations YAML ;
- scripts de lancement ;
- benchmarks ;
- jeux de tests.

Les poids peuvent être retéléchargés si :

- la source est durable ;
- l’empreinte est connue ;
- la version reste disponible ;
- la licence autorise l’usage.

Conserver une copie locale ou une archive hors ligne pour les modèles critiques ou difficiles à reproduire.

### 17.2 Inventaire Ollama

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
ollama list | Out-File .\exports\ollama-models.txt
ollama --version | Out-File .\exports\ollama-version.txt
```

### 17.3 Inventaire llama.cpp

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell ollama list | Out-File .\exports\ollama-models.txt ollama --version | Out-File .\exports\ollama-version.txt`.

```powershell
Get-FileHash .\models\*.gguf -Algorithm SHA256 |
  Export-Csv .\exports\gguf-hashes.csv -NoTypeInformation
```

## 18. Mises à jour

### 18.1 Ne pas mettre à jour tous les composants simultanément

Ordre recommandé :

1. sauvegarder ;
2. enregistrer les versions actuelles ;
3. mettre à jour un moteur ;
4. relancer les tests de référence ;
5. comparer les performances et sorties ;
6. valider ou revenir en arrière ;
7. seulement ensuite mettre à jour l’interface.

### 18.2 Ollama

L’application Windows peut proposer automatiquement une mise à jour.

Avant redémarrage :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
ollama --version
ollama list
```

Après redémarrage :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
ollama --version
ollama run <modele-de-validation>
ollama ps
```

### 18.3 llama.cpp

Chaque build est installé dans un nouveau dossier.

Ne jamais remplacer le seul binaire fonctionnel.

### 18.4 LocalAI et LibreChat

Mettre à jour sur une branche ou une copie :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
docker compose pull
docker compose up -d
docker compose ps
docker compose logs --tail=200
```

Vérifier les migrations de données avant tout retour arrière.

## 19. Diagnostic par couches

### Couche 1 — Modèle

- fichier présent ;
- empreinte correcte ;
- licence enregistrée ;
- quantification attendue ;
- template compatible.

### Couche 2 — Moteur

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
ollama --version
ollama ps
```

ou :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
.\llama-cli.exe --version
```

### Couche 3 — API

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell .\llama-cli.exe --version`.

```powershell
Test-NetConnection 127.0.0.1 -Port 11434
Invoke-RestMethod http://127.0.0.1:11434/api/tags
```

### Couche 4 — Conteneur

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell Test-NetConnection 127.0.0.1 -Port 11434 Invoke-RestMethod http://127.0.0.1:11434/api/tags`.

```powershell
docker compose ps
docker compose logs --tail=200
```

### Couche 5 — Interface

- endpoint correct ;
- modèle sélectionné ;
- clé fictive ou réelle selon l’API ;
- contexte compatible ;
- outils désactivés pendant le diagnostic.

### Couche 6 — Performance

- `ollama ps` ;
- Gestionnaire des tâches ;
- mémoire et VRAM ;
- nombre de modèles chargés ;
- contexte ;
- parallélisme ;
- autres applications GPU actives.

## 20. Mode Solo

Le Mode Solo utilise :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Ollama natif
+ Open WebUI
+ llama.cpp pour benchmark et dépannage
```

Règles :

- un modèle principal chargé ;
- contexte initial de 4096 ;
- une seule requête parallèle ;
- LibreChat arrêté sauf test ;
- LocalAI arrêté sauf besoin d’API spécifique ;
- fermeture de ComfyUI pendant les benchmarks LLM GPU ;
- catalogue de modèles limité et documenté.

## 21. Mode Studio

Le Mode Studio ajoute :

- registre approuvé des modèles ;
- cache partagé ou miroir interne ;
- validation juridique ;
- benchmarks reproductibles ;
- environnements développement, validation et production ;
- quotas et authentification ;
- passerelle LocalAI ou autre routeur lorsque justifié ;
- LibreChat pour certains groupes si ses fonctions sont nécessaires ;
- supervision des API ;
- stratégie de retour arrière ;
- tests de charge et de concurrence.

Un modèle ne doit pas être ajouté directement en production par simple téléchargement depuis une interface.

## 22. Erreurs fréquentes

### Le modèle répond mais le GPU reste inactif

- exécuter `ollama ps` ;
- vérifier la colonne `PROCESSOR` ;
- contrôler les journaux ;
- réduire le modèle et le contexte ;
- fermer les autres applications GPU ;
- comparer le backend standard et Vulkan expérimental.

### L’interface Docker ne trouve pas Ollama

Utiliser :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
http://host.docker.internal:11434
```

et non :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
http://localhost:11434
```

### La mémoire augmente avec plusieurs conversations

- limiter le parallélisme ;
- limiter les modèles chargés ;
- réduire le contexte ;
- arrêter les modèles inutilisés ;
- vérifier les fonctions de titre, résumé et embeddings automatiques.

### Les sorties changent après une mise à jour

Comparer :

- moteur ;
- modèle ;
- quantification ;
- template de chat ;
- paramètres ;
- contexte ;
- seed ;
- backend.

### Le JSON est invalide

- utiliser les sorties structurées si le moteur et le modèle les prennent en charge ;
- valider avec un parseur ;
- relancer avec une température plus faible ;
- ne jamais injecter directement un JSON non validé dans le jeu.

## 23. Checklist obligatoire

- [ ] Ollama est installé sous Windows.
- [ ] `ollama --version` fonctionne.
- [ ] Le stockage des modèles est placé sur un disque adapté.
- [ ] L’API écoute uniquement sur la boucle locale.
- [ ] Un modèle de validation est enregistré dans le manifeste.
- [ ] La licence du modèle est vérifiée.
- [ ] `ollama ps` indique la répartition CPU/GPU.
- [ ] Le test API natif réussit.
- [ ] Le test compatible OpenAI réussit.
- [ ] llama.cpp CPU fonctionne avec le même GGUF de référence.
- [ ] llama.cpp Vulkan est testé séparément ou explicitement écarté.
- [ ] Les benchmarks sont conservés.
- [ ] Open WebUI peut joindre le moteur Windows.
- [ ] LibreChat est arrêté lorsqu’il n’est pas utilisé.
- [ ] LocalAI est installé uniquement si son rôle est justifié.
- [ ] Aucun moteur n’est exposé publiquement sans proxy sécurisé.
- [ ] Les manifestes contiennent les empreintes SHA-256.
- [ ] Les paramètres de contexte et parallélisme sont documentés.
- [ ] Une stratégie CPU de secours est validée.

## 24. Critère d’acceptation

Le chapitre est validé lorsque :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Ollama Windows              → API disponible
modèle de validation        → réponse correcte
ollama ps                   → répartition enregistrée
llama.cpp CPU               → test réussi
backend AMD retenu          → mesuré ou explicitement écarté
Open WebUI                  → connexion réussie
LibreChat ou LocalAI        → option documentée, active ou écartée
manifeste et licence        → présents
benchmark                   → reproductible
retour CPU                  → fonctionnel
```

## 25. Décisions retenues

| Décision | Statut |
|---|---|
| Ollama natif Windows comme moteur principal | retenu |
| llama.cpp CPU comme référence | obligatoire |
| llama.cpp Vulkan comme laboratoire AMD | retenu |
| LocalAI obligatoire en Mode Solo | écarté |
| LocalAI comme passerelle Studio | optionnel |
| LibreChat exécuté avec Open WebUI en permanence | écarté |
| API liée à `127.0.0.1` | obligatoire |
| Contexte initial de 4096 | retenu |
| Une requête parallèle sur le poste de référence | retenu |
| Un modèle chargé à la fois | retenu |
| Modèle sans licence enregistrée | interdit |
| Sortie IA injectée sans validation | interdit |

## 26. Sources officielles vérifiées

- [Ollama pour Windows](https://docs.ollama.com/windows)
- [Prise en charge matérielle Ollama](https://docs.ollama.com/gpu)
- [FAQ et configuration Ollama](https://docs.ollama.com/faq)
- [API Ollama](https://docs.ollama.com/api/introduction)
- [Compatibilité OpenAI d’Ollama](https://docs.ollama.com/api/openai-compatibility)
- [Référence CLI Ollama](https://docs.ollama.com/cli)
- [Dépôt officiel llama.cpp](https://github.com/ggml-org/llama.cpp)
- [Compilation Vulkan de llama.cpp](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md)
- [Releases llama.cpp](https://github.com/ggml-org/llama.cpp/releases)
- [Documentation LocalAI](https://localai.io/docs/overview/)
- [Installation LocalAI](https://localai.io/installation/)
- [Accélération GPU LocalAI](https://localai.io/features/gpu-acceleration/)
- [Installation locale LibreChat](https://www.librechat.ai/docs/local)
- [LibreChat avec Docker](https://www.librechat.ai/docs/local/docker)
- [Endpoint Ollama de LibreChat](https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/ollama)

## 27. Résumé

La plateforme LLM locale repose sur une séparation nette des responsabilités :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Ollama      → simplicité et service principal
llama.cpp   → référence, benchmark et contrôle fin
LocalAI     → passerelle multi-backends optionnelle
LibreChat   → interface alternative optionnelle
```

Pour la RX 6750 XT, aucune accélération ne doit être supposée. Elle est observée avec `ollama ps`, comparée à llama.cpp CPU, puis validée par benchmark. Le modèle, sa licence, son empreinte, sa quantification et ses paramètres restent traçables.

Le chapitre suivant installe la chaîne audio IA locale : synthèse vocale, transcription, génération musicale et effets sonores.
