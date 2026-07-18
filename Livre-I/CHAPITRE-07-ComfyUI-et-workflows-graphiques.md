---
title: "Livre I — Chapitre 7 : ComfyUI et workflows graphiques"
id: "DOC-L1-CH04"
status: "draft-review"
version: "1.4.0"
lang: "fr-FR"
book: "Livre I"
chapter: 7
legacy-chapter: 4
canonical-order: 7
last-verified: "2026-07-18"
reference-hardware:
  gpu: "AMD Radeon RX 6750 XT 12 Go"
  cpu: "AMD Ryzen 7 2700"
  ram: "32 Go"
  os: "Windows 11 64 bits"
reference-software:
  comfyui: "v0.24.0"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# ComfyUI et workflows graphiques

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L1-CH04`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **État technique vérifié le :** 18 juillet 2026  
> **Résultat attendu :** disposer d’une installation ComfyUI locale, isolée, reproductible et adaptée à la RX 6750 XT, avec des workflows versionnés, des modèles traçables et un chemin CPU de secours.

## 1. Objet du chapitre

ComfyUI est le moteur graphique nodal principal du projet. Il permet de construire des chaînes de génération d’images, de traitement, d’animation, de vidéo, d’audio et de 3D sous forme de graphes explicites.

Le rôle de ComfyUI dans le guide est double :

1. fournir un environnement de création interactif ;
2. devenir un moteur automatisable par API pour les pipelines de production.

Le chapitre ne cherche pas à installer le plus grand nombre possible de modèles ou de nœuds. Il cherche à construire une base :

- stable ;
- mesurable ;
- réversible ;
- documentée ;
- compatible avec la configuration AMD de référence ;
- capable de reproduire un résultat à partir d’un workflow et d’un manifeste.

La règle centrale est :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Un workflow sans version, sans modèles identifiés et sans dépendances enregistrées
n’est pas un workflow reproductible.
```

## 2. État officiel au 18 juillet 2026

### 2.1 Version de référence

La version stable de référence utilisée pour la rédaction est :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
ComfyUI v0.24.0
```

Cette version doit être remplacée par un tag ou un commit explicitement testé lors d’une future mise à jour du guide. La mention `latest` ne doit jamais être utilisée comme preuve de compatibilité.

### 2.2 ComfyUI Desktop sous Windows

ComfyUI Desktop est l’installation la plus simple pour un poste compatible. Toutefois, la documentation officielle Windows la destine actuellement aux GPU NVIDIA.

Pour la RX 6750 XT :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
ComfyUI Desktop Windows
└── non retenu comme parcours principal
```

La sélection « configuration manuelle » du Desktop ne transforme pas cette édition en solution AMD officiellement validée. Elle doit être réservée à des utilisateurs capables de maintenir eux-mêmes l’environnement Python.

### 2.3 Portable Windows

Le portable officiel Windows fournit :

- un environnement Python embarqué ;
- des scripts de démarrage ;
- une procédure de mise à jour ;
- des variantes NVIDIA, CPU et AMD expérimentales.

La variante AMD officielle expérimentale vise actuellement les générations RDNA 3, RDNA 3.5 et RDNA 4. La RX 6750 XT appartient à RDNA 2 et ne doit donc pas être présentée comme compatible avec ce portable AMD officiel.

### 2.4 Installation manuelle

L’installation manuelle est la base retenue pour ce guide, car elle permet :

- de choisir la version de Python ;
- de séparer les environnements CPU, DirectML et ZLUDA ;
- de figer le code ComfyUI ;
- de contrôler les dépendances ;
- de sauvegarder les nœuds personnalisés ;
- de reproduire l’installation sur une autre machine.

### 2.5 DirectML

ComfyUI accepte encore l’argument :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
--directml
```

Cependant, le code officiel avertit actuellement que `torch-directml` fonctionne mal, reste très lent, n’a pas été mis à jour depuis longtemps et pourrait être supprimé.

DirectML est donc classé :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
secours dégradé
```

Il ne constitue ni le parcours principal ni la référence de performance.

### 2.6 ZLUDA

ZLUDA est une couche communautaire permettant à certaines applications CUDA de fonctionner sur des GPU non-NVIDIA. Ce projet est indépendant de ComfyUI.

Dans le guide :

- ZLUDA est optionnel ;
- son installation est isolée ;
- ses versions sont figées ;
- son fonctionnement n’est jamais garanti après une mise à jour ;
- un environnement CPU validé reste obligatoire ;
- les workflows produits doivent rester lisibles sans ZLUDA.

ZLUDA ne doit pas être copié dans l’installation stable CPU ni dans une installation officielle ComfyUI.

## 3. Matrice de décision

| Voie | RX 6750 XT | Statut dans le guide | Usage |
|---|---|---|---|
| Desktop Windows | non ciblé officiellement | écarté | NVIDIA principalement |
| Portable NVIDIA | incompatible | écarté | GPU NVIDIA |
| Portable AMD officiel | RDNA 3 et plus récent | non retenu pour RX 6750 XT | test sur matériel pris en charge |
| Manuel CPU | compatible | obligatoire | référence fonctionnelle et diagnostic |
| Manuel DirectML | possible mais très dégradé | secours | test ponctuel |
| Manuel ZLUDA | communautaire et variable | laboratoire | accélération expérimentale |
| Linux ROCm | RX 6750 XT non officiellement garantie | laboratoire séparé | utilisateurs avancés |

Le parcours de référence est :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Installation CPU validée
        ↓
Workflow minimal reproductible
        ↓
Copie isolée pour ZLUDA
        ↓
Mesure comparative
        ↓
Conservation du backend seulement s’il est stable
```

## 4. Architecture des dossiers

### 4.1 Principe

Le code, les environnements Python, les modèles et les productions ne doivent pas être mélangés.

Arborescence recommandée :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
D:\IA\ComfyUI\
├── installations\
│   ├── comfyui-cpu\
│   ├── comfyui-directml\
│   └── comfyui-zluda\
├── models\
│   ├── checkpoints\
│   ├── diffusion_models\
│   ├── clip\
│   ├── clip_vision\
│   ├── controlnet\
│   ├── loras\
│   ├── upscale_models\
│   ├── vae\
│   └── vae_approx\
├── workflows\
│   ├── source\
│   ├── accepted\
│   ├── tests\
│   └── archive\
├── input\
├── output\
├── temp\
├── manifests\
├── benchmarks\
├── backups\
└── logs\
```

### 4.2 Disque

Les modèles doivent être stockés sur un SSD. Un NVMe réduit surtout :

- le temps de chargement des checkpoints ;
- les changements de modèles ;
- les opérations de déchargement vers le disque ;
- les copies et sauvegardes.

Prévoir plusieurs centaines de gigaoctets lorsque plusieurs familles de modèles, ControlNet, LoRA, VAE, upscalers et modèles vidéo sont conservés.

### 4.3 Dépôt Git

Le dépôt documentaire peut contenir :

- les workflows JSON ;
- les manifestes YAML ;
- les scripts de lancement ;
- les fichiers de chemins d’exemple ;
- les captures légères nécessaires à la documentation ;
- les listes de dépendances.

Il ne doit pas contenir :

- les checkpoints ;
- les LoRA volumineuses ;
- les VAE ;
- les caches Hugging Face ;
- les fichiers de sortie ;
- les secrets d’API ;
- les environnements Python.

## 5. Installer l’environnement CPU de référence

### 5.1 Pourquoi commencer par le CPU

L’environnement CPU valide indépendamment :

- Python ;
- Git ;
- les dépendances ComfyUI ;
- le chargement du workflow ;
- la présence des modèles ;
- les nœuds ;
- les chemins ;
- l’interface web ;
- les sorties.

Il sera lent, mais il fournit une référence de diagnostic.

### 5.2 Version de Python

La documentation ComfyUI recommande actuellement Python 3.13. Python 3.12 reste un bon repli lorsque certains nœuds personnalisés échouent avec 3.13.

Pour un projet de production :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Python 3.13.x : choix initial
Python 3.12.x : repli de compatibilité
Python 3.14.x : laboratoire tant que les nœuds ne sont pas tous validés
```

Ne pas utiliser le Python global de Windows pour toutes les applications IA.

### 5.3 Cloner une version stable

Dans PowerShell :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Set-Location D:\IA\ComfyUI\installations
git clone https://github.com/Comfy-Org/ComfyUI.git comfyui-cpu
Set-Location comfyui-cpu
git checkout v0.24.0
```

Enregistrer :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git rev-parse HEAD
git status --short
```

Le résultat doit montrer un dépôt propre et un commit précis.

### 5.4 Créer l’environnement virtuel

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Vérifier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python --version
python -c "import sys; print(sys.executable)"
```

L’exécutable doit appartenir au dossier `.venv` de l’installation.

### 5.5 Installer les dépendances

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python -m pip install -r requirements.txt
```

Puis vérifier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python -m pip check
python -m pip freeze > ..\..\manifests\comfyui-cpu-pip-freeze.txt
```

### 5.6 Démarrer en CPU

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python main.py `
  --cpu `
  --listen 127.0.0.1 `
  --port 8188 `
  --output-directory D:\IA\ComfyUI\output `
  --input-directory D:\IA\ComfyUI\input `
  --user-directory D:\IA\ComfyUI\workflows
```

Ouvrir :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text

> **[WEB] Navigateur internet - Ouvrir :** utiliser la page officielle indiquée ci-dessous.

http://127.0.0.1:8188
```

Ne pas utiliser `--listen` sans adresse. Sans argument, cette option écoute sur toutes les interfaces IPv4 et IPv6.

## 6. Partager les modèles entre installations

### 6.1 Fichier de chemins

Créer dans chaque installation :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
extra_model_paths.yaml
```

Exemple :

> **[VSC] Visual Studio Code - Créer ou modifier :** `text extra_model_paths.yaml`.

```yaml
guide_ia_models:
  base_path: D:/IA/ComfyUI
  checkpoints: models/checkpoints
  diffusion_models: models/diffusion_models
  clip: models/clip
  clip_vision: models/clip_vision
  controlnet: models/controlnet
  loras: models/loras
  upscale_models: models/upscale_models
  vae: models/vae
  vae_approx: models/vae_approx
```

Utiliser des barres obliques `/` dans le YAML afin de limiter les problèmes d’échappement.

### 6.2 Avantages

Cette séparation permet :

- de tester plusieurs backends avec les mêmes modèles ;
- d’éviter les duplications ;
- de réinstaller ComfyUI sans déplacer les checkpoints ;
- de sauvegarder les modèles indépendamment du code ;
- d’identifier plus facilement les fichiers manquants.

### 6.3 Risque

Une mise à jour simultanée de plusieurs installations peut écrire dans les mêmes dossiers de cache ou de métadonnées. Les modèles peuvent être partagés, mais les dossiers `user`, `custom_nodes`, `temp` et environnements Python doivent rester séparés.

## 7. Modèles et provenance

### 7.1 Manifeste obligatoire

Chaque modèle accepté doit être enregistré avec :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
id: MODEL-IMAGE-001
name: "Nom du modèle"
filename: "modele.safetensors"
family: "famille"
revision: "tag-ou-commit"
source: "URL officielle"
license: "licence"
sha256: "empreinte"
size_bytes: 0
format: "safetensors"
backend_tested: "cpu|zluda|directml"
comfyui_version: "v0.24.0"
verified_date: "2026-07-18"
```

### 7.2 Format

Privilégier `safetensors` lorsque le modèle officiel le fournit.

Les formats capables d’exécuter du code arbitraire pendant le chargement doivent être traités comme non fiables jusqu’à validation.

### 7.3 Licences

Vérifier séparément :

- la licence du code ;
- la licence du modèle ;
- les restrictions commerciales ;
- les restrictions de redistribution ;
- les règles relatives aux contenus adultes ;
- les obligations d’attribution ;
- les éventuelles restrictions sur les personnes réelles.

« Open weights » ne signifie pas automatiquement « libre de toute restriction ».

### 7.4 Empreinte

PowerShell :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Get-FileHash .\modele.safetensors -Algorithm SHA256
```

La comparaison doit porter sur l’empreinte et non seulement sur le nom du fichier.

## 8. Premier workflow de validation

### 8.1 Objectif

Le premier workflow doit rester simple :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Checkpoint Loader
├── CLIP Text Encode positif
├── CLIP Text Encode négatif
├── Empty Latent Image
├── KSampler
├── VAE Decode
└── Save Image
```

Il ne doit utiliser aucun nœud personnalisé.

### 8.2 Paramètres de test

Point de départ :

| Paramètre | Valeur |
|---|---:|
| Largeur | 512 |
| Hauteur | 512 |
| Batch | 1 |
| Étapes | 8 à 12 |
| Seed | valeur fixe |
| CFG | valeur recommandée par le modèle |
| Sampler | sampler natif stable |
| Scheduler | scheduler documenté |

Le but est de vérifier le pipeline, pas de produire l’image finale du projet.

### 8.3 Prompts de test

Les prompts utilisés pour la validation doivent être neutres et répétables. Exemple :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
positif : studio photograph of a red ceramic mug on a wooden table, neutral light
négatif : blurry, duplicate, text, watermark
```

Les exemples de validation du guide n’utilisent aucun personnage d’âge ambigu et aucun acte sexuel explicite.

### 8.4 Résultat attendu

Le test réussit lorsque :

- le modèle est chargé ;
- tous les nœuds deviennent valides ;
- la file d’exécution se termine ;
- une image est enregistrée ;
- le PNG contient les métadonnées du workflow ;
- le même seed et les mêmes paramètres peuvent être relancés ;
- le journal ne contient pas d’erreur bloquante.

## 9. Versionner les workflows

### 9.1 Fichier source

Chaque workflow accepté doit être exporté en JSON :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
workflows/source/WF-IMG-0001-text-to-image.json
```

### 9.2 Manifeste de workflow

Créer un fichier associé :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
workflows/source/WF-IMG-0001-text-to-image.yaml
```

Exemple :

> **[VSC] Visual Studio Code - Créer ou modifier :** `text workflows/source/WF-IMG-0001-text-to-image.yaml`.

```yaml
id: WF-IMG-0001
name: "Validation text-to-image"
version: "1.0.0"
status: "accepted"
comfyui:
  version: "v0.24.0"
  commit: "f49bdb6"
backend:
  name: "cpu"
  version: "reference"
models:
  - id: MODEL-IMAGE-001
custom_nodes: []
inputs:
  width: 512
  height: 512
  steps: 10
  batch: 1
reproducibility:
  seed: 123456789
  deterministic_requested: false
verified_date: "2026-07-18"
```

### 9.3 États

| État | Signification |
|---|---|
| `draft` | expérimentation en cours |
| `review` | prêt pour contrôle |
| `accepted` | validé sur la configuration de référence |
| `deprecated` | remplacé, conservé pour migration |
| `archived` | historique non maintenu |

### 9.4 PNG avec métadonnées

Une image générée par ComfyUI peut contenir le workflow et les paramètres. Ce mécanisme est utile, mais le PNG ne remplace pas le JSON versionné.

Conserver :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
JSON source + manifeste + image de référence
```

### 9.5 Ne pas désactiver les métadonnées par défaut

L’argument :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
--disable-metadata
```

supprime les métadonnées des fichiers générés. Il ne doit être utilisé que pour une exportation publique ou une contrainte de confidentialité clairement identifiée.

Le pipeline interne conserve les métadonnées afin de faciliter l’audit et la reproduction.

## 10. Dépendances des nœuds personnalisés

### 10.1 Risque principal

Un nœud personnalisé est du code Python exécuté avec les droits du compte utilisateur. Il peut :

- lire et modifier des fichiers ;
- accéder au réseau ;
- installer des dépendances ;
- exécuter des commandes ;
- introduire une incompatibilité Python ;
- casser des workflows existants.

Un workflow trouvé en ligne ne doit jamais entraîner automatiquement l’installation aveugle de tous ses nœuds.

### 10.2 Règle d’installation

Avant d’installer un nœud :

1. identifier le dépôt d’origine ;
2. lire la licence ;
3. examiner l’activité et les issues ;
4. enregistrer le commit testé ;
5. examiner `requirements.txt` ;
6. vérifier les scripts d’installation ;
7. effectuer une sauvegarde ou un snapshot ;
8. tester sur une copie de l’installation ;
9. documenter les nœuds réellement utilisés.

### 10.3 ComfyUI-Manager

Le Manager officiel intégré peut être activé avec :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python -m pip install -r manager_requirements.txt
python main.py --enable-manager
```

Le niveau de sécurité recommandé est `normal`. Les niveaux plus permissifs ne doivent pas être utilisés pour une interface accessible à distance.

### 10.4 Snapshots

Avec `comfy-cli` :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell python -m pip install -r manager_requirements.txt python main.py --enable-manager`.

```powershell
comfy node save-snapshot
comfy node snapshot-list
comfy node restore-snapshot <snapshot>
```

Il est également possible de produire une liste de dépendances à partir d’un workflow :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
comfy node deps-in-workflow `
  --workflow .\workflows\source\WF-IMG-0001-text-to-image.json `
  --output .\manifests\WF-IMG-0001-deps.json
```

### 10.5 Conflits Python

Les nœuds peuvent exiger des versions incompatibles d’une même bibliothèque.

Pour le Mode Studio :

- utiliser un environnement test ;
- regrouper les dépendances ;
- employer la résolution unifiée lorsque disponible ;
- refuser une mise à jour si le solveur détecte un conflit ;
- conserver l’ancien environnement tant que la migration n’est pas validée.

## 11. Accélération ZLUDA isolée

### 11.1 Principe

Ne jamais transformer l’installation CPU en installation ZLUDA.

Créer :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
D:\IA\ComfyUI\installations\comfyui-zluda
```

à partir du même tag ComfyUI, mais avec :

- un environnement Python indépendant ;
- une version ZLUDA précise ;
- les bibliothèques AMD attendues ;
- des scripts de lancement dédiés ;
- un journal séparé ;
- aucun écrasement de DLL dans Windows ou l’installation CPU.

### 11.2 Ce que ZLUDA ne garantit pas

ZLUDA ne garantit pas :

- la compatibilité de toutes les opérations CUDA ;
- la compatibilité de tous les modèles ;
- la stabilité de tous les nœuds ;
- la reproductibilité entre versions ;
- la précision numérique identique à CUDA ;
- la réussite d’une mise à jour PyTorch.

### 11.3 Manifeste du backend

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
id: BACKEND-ZLUDA-001
status: experimental
comfyui_tag: "v0.24.0"
comfyui_commit: "f49bdb6"
python: "3.12.x"
torch: "version exacte"
zluda: "version exacte"
amd_driver: "version exacte"
gpu: "Radeon RX 6750 XT"
gpu_architecture: "gfx1031"
verified_workflows:
  - WF-IMG-0001
known_failures: []
```

### 11.4 Validation minimale

ZLUDA n’est accepté que si :

- ComfyUI démarre sans modifier l’installation CPU ;
- le GPU est détecté ;
- le workflow minimal termine ;
- deux exécutions successives ne plantent pas ;
- la mémoire est libérée après le workflow ;
- les images sont cohérentes ;
- le temps est inférieur au CPU ;
- les erreurs connues sont consignées.

### 11.5 Retour arrière

Le retour arrière consiste à :

1. arrêter l’installation ZLUDA ;
2. redémarrer l’installation CPU ;
3. charger le même workflow ;
4. vérifier le modèle et les entrées ;
5. produire une sortie de référence ;
6. archiver les journaux ZLUDA.

Aucune migration de workflow ne doit être nécessaire pour revenir au CPU.

## 12. DirectML en secours

### 12.1 Environnement distinct

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
D:\IA\ComfyUI\installations\comfyui-directml
```

Ne pas installer `torch-directml` dans les environnements CPU ou ZLUDA.

### 12.2 Installation de principe

> **[VSC] Visual Studio Code - Créer ou modifier :** `text D:\IA\ComfyUI\installations\comfyui-directml`.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install torch-directml
python -m pip install -r requirements.txt
```

Démarrage :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell python -m venv .venv .\.venv\Scripts\Activate.ps1 python -m pip install torch-directml python -m pip install -r requirements.txt`.

```powershell
python main.py --directml --listen 127.0.0.1 --port 8190
```

### 12.3 Limites

DirectML est utilisé uniquement pour déterminer si un workflow fonctionne mieux qu’en CPU sur un cas particulier.

Il ne doit pas être utilisé pour :

- définir les performances attendues ;
- valider tous les nœuds ;
- installer la plateforme Studio ;
- promettre la compatibilité d’un modèle ;
- produire sans journal de test.

## 13. Gestion de la VRAM sur 12 Go

### 13.1 Conserver la gestion dynamique

ComfyUI utilise une gestion dynamique de la VRAM. Ne pas la désactiver sans diagnostic précis.

L’argument :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
--disable-dynamic-vram
```

est à éviter. Le projet ComfyUI signale que cette option doit disparaître à terme.

### 13.2 Réserver de la VRAM

Point de départ :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
--reserve-vram 1.5
```

La valeur doit être mesurée. Augmenter la réserve lorsque :

- Windows manque de mémoire graphique ;
- le navigateur devient instable ;
- un écran haute résolution utilise beaucoup de VRAM ;
- d’autres applications GPU restent ouvertes.

### 13.3 Profils de lancement

#### Profil normal

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python main.py --reserve-vram 1.5
```

#### Profil prudent

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell python main.py --reserve-vram 1.5`.

```powershell
python main.py --lowvram --reserve-vram 2.0
```

#### Profil de secours

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell python main.py --lowvram --reserve-vram 2.0`.

```powershell
python main.py --novram --reserve-vram 2.0
```

Les arguments `--lowvram` et `--novram` peuvent ralentir fortement le workflow. Ils sont utilisés pour terminer une tâche qui dépasse la VRAM, pas pour améliorer la vitesse.

### 13.4 Réduire la charge

Dans cet ordre :

1. batch à 1 ;
2. résolution réduite ;
3. modèle plus léger ;
4. VAE tiled ;
5. ControlNet réduit ou désactivé ;
6. upscale séparé ;
7. encodage texte déchargé vers le CPU ;
8. fermeture de Blender, navigateur lourd et jeux ;
9. lancement prudent ;
10. CPU en dernier recours.

### 13.5 Ne pas forcer le FP8 sans preuve

Les options FP8 et `--fast` sont expérimentales et peuvent modifier la qualité, provoquer des erreurs ou ne pas être prises en charge par le backend AMD.

Elles ne doivent pas être activées dans le profil stable sans comparaison visuelle et test de régression.

## 14. Profils de workflows pour la RX 6750 XT

### 14.1 Niveau W0 — fumée

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
512 × 512
batch 1
8 à 12 étapes
aucun ControlNet
aucun upscale
```

Objectif : valider l’installation.

### 14.2 Niveau W1 — production légère

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
512 à 768 pixels
batch 1
15 à 25 étapes
une LoRA maximum
prévisualisation faible
```

Objectif : concept art, tests de style, textures simples.

### 14.3 Niveau W2 — production standard

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
768 à 1024 pixels
batch 1
20 à 35 étapes
une ou deux conditions
upscale séparé
```

Objectif : images de référence et assets 2D préparatoires.

### 14.4 Niveau W3 — lourd

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
haute résolution
plusieurs ControlNet
modèles vidéo
modèles 3D
upscale important
```

Objectif : expérimentation. Le workflow doit être fractionné, mesurer chaque étape et accepter le déchargement RAM ou disque.

## 15. Conception des graphes

### 15.1 Un graphe, une responsabilité

Éviter les graphes monolithiques de plusieurs centaines de nœuds sans structure.

Découper :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
01-load
02-conditioning
03-sampling
04-decode
05-postprocess
06-save
```

### 15.2 Nommage

Utiliser des groupes et notes :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
[INPUT] modèle et image
[STYLE] prompt et LoRA
[CONTROL] pose et profondeur
[SAMPLE] génération
[OUTPUT] conversion et sauvegarde
```

### 15.3 Valeurs exposées

Les paramètres fréquemment modifiés doivent être regroupés :

- seed ;
- résolution ;
- steps ;
- CFG ;
- sampler ;
- scheduler ;
- force des LoRA ;
- force des ControlNet ;
- préfixe de sortie.

### 15.4 App Mode

Lorsqu’un workflow est destiné à un utilisateur non technique, App Mode peut exposer seulement les paramètres nécessaires.

Le graphe source complet reste versionné et accessible aux mainteneurs.

### 15.5 Sous-graphes

Les sous-graphes ou composants réutilisables doivent rester simples et documentés. Ne pas cacher une logique critique dans un sous-graphe sans identifiant et version.

## 16. Nommage des sorties

Convention :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
<workflow-id>_<asset-id>_<version>_<seed>_<date>
```

Exemple :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
WF-IMG-0042_ENV-FOREST-003_v02_s123456_20260718.png
```

Les dossiers de sortie peuvent suivre :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
output/
├── concepts/
├── characters/
├── environments/
├── textures/
├── ui/
├── tests/
└── rejected/
```

Une sortie rejetée ne doit pas écraser une sortie acceptée.

## 17. API locale

### 17.1 Exposition

Par défaut :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
127.0.0.1:8188
```

Une application locale, Open WebUI ou un script peut envoyer un workflow à l’API ComfyUI.

### 17.2 Sécurité

Ne pas exposer ComfyUI directement à Internet.

Pour un accès distant :

- VPN ;
- proxy authentifié ;
- réseau privé ;
- filtrage des IP ;
- journalisation ;
- répertoire d’entrée contrôlé ;
- nœuds personnalisés approuvés.

### 17.3 API Nodes

Les API Nodes intégrés peuvent communiquer avec des services externes. Pour une instance strictement locale :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
--disable-api-nodes
```

Cette option empêche également le frontend de communiquer avec Internet par les API nodes.

### 17.4 Multi-utilisateur

L’option :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
--multi-user
```

sépare le stockage utilisateur, mais ne transforme pas à elle seule ComfyUI en service sécurisé pour Internet.

## 18. Mise à jour

### 18.1 Ne pas mettre à jour pendant une production critique

Avant mise à jour :

1. enregistrer le commit actuel ;
2. exporter les workflows ;
3. créer un snapshot des nœuds ;
4. sauvegarder le dossier `user` ;
5. enregistrer `pip freeze` ;
6. conserver les scripts de lancement ;
7. valider un workflow de référence.

### 18.2 Mise à jour du code

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git fetch --tags
git checkout <nouveau-tag>
python -m pip install -r requirements.txt
python -m pip check
```

Ne pas exécuter `git pull` aveuglément sur une installation de production modifiée.

### 18.3 Environnement parallèle

Méthode recommandée :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
comfyui-v0.24.0-stable
comfyui-v0.xx-test
```

Les deux installations partagent les modèles, mais pas les environnements Python ni les nœuds personnalisés.

### 18.4 Tests de régression

Après mise à jour, exécuter :

- workflow W0 ;
- workflow W1 ;
- un workflow avec LoRA ;
- un workflow avec ControlNet ;
- un workflow avec les nœuds personnalisés critiques ;
- un appel API ;
- une génération avec seed fixe.

Comparer :

- réussite ;
- durée ;
- mémoire ;
- image ;
- journaux ;
- métadonnées.

## 19. Sauvegarde

### 19.1 Sauvegarder

- workflows JSON ;
- manifestes ;
- dossiers `user` ;
- nœuds personnalisés et commits ;
- scripts de lancement ;
- `extra_model_paths.yaml` ;
- listes de modèles et empreintes ;
- profils de benchmark ;
- images de référence ;
- rapports de validation.

### 19.2 Modèles

Les modèles peuvent être re-téléchargés uniquement si :

- la source reste disponible ;
- la révision est connue ;
- la licence autorise toujours l’usage ;
- l’empreinte est enregistrée.

Pour une production importante, conserver une sauvegarde locale des modèles approuvés.

### 19.3 Ne pas sauvegarder les caches comme source

Les caches peuvent être supprimés et recréés. Ils ne doivent pas être la seule copie d’un modèle ou d’un workflow.

## 20. Benchmark

### 20.1 Fiche

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
id: BENCH-COMFY-001
date: "2026-07-18"
hardware:
  gpu: "RX 6750 XT 12 Go"
  cpu: "Ryzen 7 2700"
  ram: "32 Go"
software:
  comfyui: "v0.24.0"
  backend: "cpu|zluda|directml"
  driver: "version"
workflow: "WF-IMG-0001"
model_sha256: "empreinte"
settings:
  width: 512
  height: 512
  steps: 10
  batch: 1
results:
  cold_start_seconds: 0
  warm_run_seconds: 0
  peak_vram_gb: 0
  peak_ram_gb: 0
  success: true
notes: ""
```

### 20.2 Mesures

Séparer :

- démarrage ;
- chargement du modèle ;
- première génération ;
- génération à chaud ;
- sauvegarde ;
- pic VRAM ;
- pic RAM ;
- stabilité après plusieurs exécutions.

Une moyenne sans préciser le nombre d’exécutions n’est pas exploitable.

## 21. Diagnostic

### Couche 1 — Python

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python --version
python -c "import sys; print(sys.executable)"
python -m pip check
```

### Couche 2 — ComfyUI

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
git rev-parse HEAD
git status --short
python main.py --cpu --verbose DEBUG
```

### Couche 3 — modèles

- fichier présent ;
- taille cohérente ;
- empreinte correcte ;
- dossier correct ;
- licence enregistrée ;
- architecture compatible avec les nœuds.

### Couche 4 — workflow

- nœuds manquants ;
- entrées invalides ;
- modèle non trouvé ;
- dimensions excessives ;
- types incompatibles ;
- sortie absente.

### Couche 5 — nœuds personnalisés

Démarrer sans nœuds personnalisés :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python main.py --disable-all-custom-nodes
```

Puis autoriser seulement un dossier :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell python main.py --disable-all-custom-nodes`.

```powershell
python main.py `
  --disable-all-custom-nodes `
  --whitelist-custom-nodes nom_du_noeud
```

### Couche 6 — VRAM

Réduire :

- batch ;
- résolution ;
- nombre de modèles chargés ;
- ControlNet ;
- upscale ;
- prévisualisation.

Puis tester `--lowvram` et `--novram`.

### Couche 7 — backend

Comparer le même workflow :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
CPU → DirectML → ZLUDA
```

Si CPU réussit et ZLUDA échoue, le workflow n’est pas nécessairement en cause.

### Couche 8 — réseau

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Test-NetConnection 127.0.0.1 -Port 8188
```

Vérifier les arguments `--listen` et `--port`.

## 22. Erreurs fréquentes

### Torch not compiled with CUDA enabled

Cette erreur indique souvent qu’un workflow ou une dépendance attend CUDA alors que l’environnement installé est CPU, DirectML ou mal configuré.

Ne pas installer un paquet CUDA au hasard. Identifier d’abord le backend de l’environnement.

### Modèle introuvable

- vérifier `extra_model_paths.yaml` ;
- redémarrer ComfyUI ;
- vérifier le type de dossier ;
- vérifier le nom dans le workflow ;
- éviter deux fichiers différents portant le même nom.

### Nœud rouge après import

- identifier le paquet manquant ;
- vérifier sa licence ;
- installer le nœud dans une copie de test ;
- enregistrer son commit ;
- ne pas utiliser « install missing nodes » sans revue.

### Out of memory

- batch à 1 ;
- réduire la résolution ;
- fermer les autres applications GPU ;
- utiliser un VAE tiled ;
- séparer l’upscale ;
- utiliser `--lowvram` ;
- vérifier les modèles encore chargés.

### Interface accessible depuis le réseau

Vérifier que le lancement contient :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
--listen 127.0.0.1
```

Ne pas utiliser `--listen` seul.

### Mise à jour ayant cassé les workflows

- revenir au tag précédent ;
- restaurer le snapshot des nœuds ;
- réinstaller les dépendances figées ;
- comparer les journaux ;
- migrer les workflows dans une branche dédiée.

## 23. Mode Solo

Le Mode Solo applique :

- une installation CPU stable ;
- une installation ZLUDA optionnelle ;
- un seul backend actif à la fois ;
- peu de nœuds personnalisés ;
- des workflows courts et nommés ;
- une sauvegarde hebdomadaire des workflows ;
- un inventaire simple des modèles ;
- des profils W0 à W2 ;
- l’interface liée à `127.0.0.1` ;
- l’arrêt de ComfyUI après la session lorsqu’il n’est pas utilisé.

## 24. Mode Studio

Le Mode Studio ajoute :

- un registre central des modèles ;
- une liste de nœuds approuvés ;
- des tags ComfyUI validés ;
- un environnement d’intégration ;
- des workflows versionnés et revus ;
- des benchmarks comparables ;
- un stockage partagé en lecture seule pour les modèles ;
- une file d’exécution contrôlée ;
- un proxy authentifié pour l’accès réseau ;
- des journaux conservés ;
- une procédure d’incident ;
- un rôle de responsable de la compatibilité.

Un utilisateur ne doit pas pouvoir installer librement un nœud Python dans l’instance de production partagée.

## 25. Validation du chapitre

### 25.1 Checklist obligatoire

- [ ] Le code ComfyUI est figé sur un tag ou commit.
- [ ] L’environnement CPU est installé et démarre.
- [ ] Python appartient au bon environnement virtuel.
- [ ] L’interface écoute uniquement sur `127.0.0.1`.
- [ ] Les modèles sont stockés hors du code ComfyUI.
- [ ] `extra_model_paths.yaml` fonctionne.
- [ ] Un workflow sans nœud personnalisé termine.
- [ ] Le workflow JSON est versionné.
- [ ] Le modèle possède une source, une licence et une empreinte.
- [ ] Les sorties conservent leurs métadonnées internes.
- [ ] Les nœuds personnalisés sont inventoriés.
- [ ] Un snapshot des dépendances est disponible.
- [ ] Le profil de VRAM est documenté.
- [ ] Le backend ZLUDA, s’il existe, est isolé.
- [ ] Le CPU reste utilisable après installation de ZLUDA.
- [ ] Un benchmark minimal est enregistré.
- [ ] Une sauvegarde des workflows et manifestes existe.
- [ ] Une procédure de retour arrière est testée.

### 25.2 Critère d’acceptation

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
ComfyUI CPU              → démarrage réussi
Workflow W0              → image enregistrée
Workflow JSON            → exporté
Métadonnées PNG           → présentes
Modèle                    → hash et licence enregistrés
Custom nodes              → zéro ou liste approuvée
Accès réseau              → localhost uniquement
Backend expérimental      → isolé et réversible
```

## 26. Décisions retenues

| Décision | Statut |
|---|---|
| ComfyUI comme moteur graphique nodal principal | retenu |
| Desktop Windows pour RX 6750 XT | écarté |
| Portable AMD officiel pour RX 6750 XT | non présumé compatible |
| Installation manuelle versionnée | obligatoire |
| Environnement CPU de référence | obligatoire |
| ZLUDA dans un environnement séparé | optionnel |
| DirectML comme parcours principal | écarté |
| Modèles stockés hors du code | obligatoire |
| Nœuds personnalisés installés sans revue | interdit |
| Workflows JSON versionnés | obligatoire |
| Métadonnées internes conservées | recommandé |
| Exposition directe à Internet | interdite |
| Gestion dynamique de VRAM | conservée |
| `--fast` sans benchmark | interdit |

## 27. Sources officielles vérifiées

- [Documentation officielle ComfyUI](https://docs.comfy.org/)
- [Configuration requise](https://docs.comfy.org/installation/system_requirements)
- [ComfyUI Desktop Windows](https://docs.comfy.org/installation/desktop/windows)
- [ComfyUI Portable Windows](https://docs.comfy.org/installation/comfyui_portable_windows)
- [Installation manuelle](https://docs.comfy.org/installation/manual_install)
- [Mise à jour de ComfyUI](https://docs.comfy.org/installation/update_comfyui)
- [Première génération](https://docs.comfy.org/get_started/first_generation)
- [Dépôt ComfyUI](https://github.com/Comfy-Org/ComfyUI)
- [Versions ComfyUI](https://github.com/Comfy-Org/ComfyUI/releases)
- [Arguments de ligne de commande](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy/cli_args.py)
- [Gestion des périphériques et DirectML](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy/model_management.py)
- [ComfyUI Manager](https://github.com/Comfy-Org/ComfyUI-Manager)
- [comfy-cli](https://github.com/Comfy-Org/comfy-cli)
- [ZLUDA](https://github.com/vosen/ZLUDA)

## 28. Résumé

Pour la RX 6750 XT, ComfyUI doit être installé comme un environnement de production versionné plutôt que comme une application opaque mise à jour automatiquement.

Le socle retenu est :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
ComfyUI manuel CPU
├── tag stable
├── modèles partagés et manifestés
├── workflows JSON versionnés
├── nœuds personnalisés approuvés
├── accès localhost
└── tests de régression

Laboratoire ZLUDA
├── environnement séparé
├── versions figées
├── mêmes modèles et workflows
├── benchmarks comparatifs
└── retour CPU immédiat
```

Le chapitre suivant installe et compare les runtimes LLM locaux : Ollama, llama.cpp, LocalAI et LibreChat.
