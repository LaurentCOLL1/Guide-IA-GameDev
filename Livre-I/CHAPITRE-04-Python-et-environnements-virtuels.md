---
title: "Livre I — Chapitre 4 : Python et environnements virtuels"
id: "DOC-L1-ENV-PYTHON"
status: "reviewed"
version: "1.4.0"
lang: "fr-FR"
book: "Livre I"
chapter: 4
last-verified: "2026-07-18"
reference-platform:
  os: "Windows 11 64 bits"
  python-management: "Python Launcher et uv"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Python et environnements virtuels

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L1-ENV-PYTHON`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Résultat attendu :** installer plusieurs versions de Python sans conflit, créer un environnement isolé par outil et reproduire les dépendances à partir de fichiers versionnés.

## 1. Pourquoi isoler Python

La plateforme utilise Python pour :

- ComfyUI et ses nœuds ;
- transcription et synthèse vocale ;
- scripts d’automatisation ;
- conversion de modèles ;
- validation JSON, YAML et Markdown ;
- outils de données ;
- tests et génération du Companion Pack.

Ces usages n’exigent pas toujours la même version de Python ni les mêmes bibliothèques.

Installer toutes les dépendances dans un Python global provoque tôt ou tard :

- conflits de versions ;
- mises à jour qui cassent un autre outil ;
- difficulté à reproduire l’environnement ;
- commandes `python` et `pip` pointant vers des installations différentes ;
- impossibilité de revenir à un état connu.

La règle principale est :

> Une application ou un projet Python possède son propre environnement, ses dépendances déclarées et une méthode de reconstruction documentée.

## 2. Les composants à distinguer

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Interpréteur Python
├── version 3.x précise
├── bibliothèque standard
└── exécutable python.exe

Environnement virtuel
├── interpréteur sélectionné
├── paquets du projet
└── scripts et exécutables locaux

Gestionnaire de paquets
├── pip
└── uv

Déclaration du projet
├── pyproject.toml
├── uv.lock ou autre fichier de verrouillage
└── requirements.txt pour compatibilité
```

## 3. Choisir une version de Python

Il n’existe pas une version universelle pour tous les outils IA.

Ordre de décision :

1. lire les exigences officielles de l’application ;
2. vérifier les roues disponibles pour Windows et l’architecture utilisée ;
3. vérifier les contraintes de PyTorch ou du backend ;
4. utiliser la version explicitement validée par le projet ;
5. créer un environnement séparé ;
6. conserver un repli documenté.

Le guide peut utiliser plusieurs versions côte à côte. Une version récente n’est pas automatiquement compatible avec une extension ancienne.

## 4. Installer Python sous Windows

### 4.1 Vérifier les installations existantes

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
py --list
py --list-paths
where.exe python
where.exe pip
```

Si `python` ouvre le Microsoft Store ou pointe vers une installation inattendue, vérifier les alias d’exécution dans les paramètres Windows et utiliser le lanceur `py` avec une version explicite.

### 4.2 Installer depuis la source officielle

Pour un environnement contrôlé, utiliser les installateurs officiels Python ou un gestionnaire documenté comme `uv`.

Exemple WinGet :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
winget search Python.Python
winget show --id Python.Python.3.13 --exact --source winget
winget install --id Python.Python.3.13 --exact --source winget
```

Au 18 juillet 2026, les versions courantes publiées par Python sont `3.14.6` et `3.13.14`. Les commandes du guide conservent Python 3.13 comme exemple de compatibilité pour plusieurs outils IA ; la version la plus récente n’est pas automatiquement la version prise en charge par une application. Le numéro doit toujours être remplacé par la version exigée et testée par le projet concerné.

Vérifier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
py -3.13 --version
py -3.13 -c "import sys; print(sys.executable)"
```

### 4.3 Ne pas dépendre du `PATH` global

Une commande explicite est plus fiable :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
py -3.13 -m venv .venv
```

plutôt que :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python -m venv .venv
```

lorsque plusieurs installations existent.

## 5. Créer un environnement avec `venv`

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
New-Item -ItemType Directory -Force C:\IA-GameDev\workspaces\python-check | Out-Null
Set-Location C:\IA-GameDev\workspaces\python-check
py -3.13 -m venv .venv
```

Activer :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
.\.venv\Scripts\Activate.ps1
```

Vérifier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python --version
python -c "import sys; print(sys.executable)"
python -m pip --version
```

Désactiver :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
deactivate
```

Ne pas versionner `.venv/`.

## 6. Utiliser `pip` correctement

Toujours rattacher `pip` à l’interpréteur actif :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python -m pip install --upgrade pip
python -m pip install paquet
```

Éviter :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
pip install paquet
```

lorsque l’origine de `pip.exe` n’est pas certaine.

Inventaire :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python -m pip list
python -m pip show paquet
python -m pip check
```

Exporter un état diagnostique :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python -m pip freeze | Out-File requirements-diagnostic.txt -Encoding utf8
```

`pip freeze` décrit l’environnement courant, mais ne remplace pas nécessairement une stratégie de dépendances maintenable.

## 7. Installer `uv`

`uv` fournit la gestion des versions Python, environnements, dépendances, outils et fichiers de verrouillage.

Installation WinGet :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
winget show --id astral-sh.uv --exact --source winget
winget install --id astral-sh.uv --exact --source winget
```

Vérifier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
uv --version
uv python list
```

Le script d’installation officiel peut aussi être utilisé après inspection, mais WinGet évite un pipeline direct téléchargement-exécution dans le parcours débutant.

## 8. Créer un projet avec `uv`

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
New-Item -ItemType Directory -Force C:\IA-GameDev\workspaces\uv-check | Out-Null
Set-Location C:\IA-GameDev\workspaces\uv-check
uv init
```

Structure attendue :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
uv-check/
├── .gitignore
├── .python-version
├── README.md
├── main.py
└── pyproject.toml
```

Créer ou synchroniser l’environnement :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
uv sync
```

`uv` crée généralement :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
.venv/
uv.lock
```

Le fichier `uv.lock` doit être versionné. Le dossier `.venv/` ne doit pas l’être.

## 9. Ajouter et retirer des dépendances

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
uv add requests
uv add --dev pytest ruff
uv remove requests
```

Afficher l’arbre :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
uv tree
```

Exécuter dans l’environnement :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
uv run python main.py
uv run pytest
```

Vérifier que le verrouillage est à jour sans le modifier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
uv lock --check
```

Reproduire exactement l’environnement :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
uv sync --locked
```

Mettre à jour volontairement :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
uv lock --upgrade-package nom-du-paquet
```

Ne pas lancer une mise à jour générale au milieu d’une phase de production sans benchmark et point de retour.

## 10. `pyproject.toml`

Exemple minimal :

> **[VSC] Visual Studio Code - Créer ou modifier :** `pyproject.toml`.

```toml
[project]
name = "ia-gamedev-tools"
version = "0.1.0"
requires-python = ">=3.12,<3.14"
dependencies = [
  "pyyaml>=6,<7",
]

[dependency-groups]
dev = [
  "pytest>=8,<9",
  "ruff>=0.12,<1",
]
```

Les bornes doivent refléter les versions testées, pas une préférence arbitraire.

Le fichier de verrouillage enregistre la résolution exacte. `pyproject.toml` exprime les contraintes et l’intention du projet.

## 11. Compatibilité avec `requirements.txt`

Certains projets existants utilisent encore :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
requirements.txt
requirements-dev.txt
constraints.txt
```

Installer avec `pip` :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python -m pip install -r requirements.txt
```

Avec `uv` :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
uv pip sync requirements.txt
```

Exporter depuis un projet `uv` :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
uv export --format requirements.txt --output-file requirements.txt
```

Ne pas modifier manuellement un fichier généré sans modifier également sa source de vérité.

## 12. Organisation recommandée

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
C:\IA-GameDev\
├── apps\
│   ├── comfyui-cpu\
│   │   └── .venv\
│   ├── comfyui-zluda\
│   │   └── .venv\
│   └── audio-tools\
│       └── .venv\
├── workspaces\
│   └── automation\
│       ├── pyproject.toml
│       ├── uv.lock
│       └── .venv\
├── caches\
└── logs\
```

Les environnements CPU, DirectML, Vulkan, HIP ou ZLUDA ne doivent pas partager le même dossier lorsqu’ils imposent des dépendances incompatibles.

## 13. Variables et caches

Afficher les emplacements :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python -c "import site, sys; print(sys.executable); print(site.getsitepackages())"
uv cache dir
```

Les caches peuvent être déplacés vers un disque adapté, mais leur emplacement doit rester documenté.

Exemples de variables rencontrées :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
HF_HOME
TORCH_HOME
XDG_CACHE_HOME
UV_CACHE_DIR
```

Ne pas définir une variable globale pour résoudre un problème propre à une seule application si une configuration locale suffit.

## 14. Scripts et modules

Exécuter un fichier :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python .\script.py
```

Exécuter un module :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python -m pytest
```

La forme `python -m ...` garantit que le module appartient à l’interpréteur actif.

Exemple robuste :

> **[VSC] Visual Studio Code - Créer ou modifier :** `powershell python .\script.py`.

```python
from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    workspace = Path.cwd()
    print(f"Python : {sys.version}")
    print(f"Exécutable : {sys.executable}")
    print(f"Dossier : {workspace}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## 15. Diagnostic d’un environnement

Collecter :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python --version
python -c "import sys, platform; print(sys.executable); print(platform.platform())"
python -m pip --version
python -m pip list
python -m pip check
uv --version
uv tree
```

Pour un paquet :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
python -c "import NOM; print(NOM.__file__)"
```

Ordre de diagnostic :

1. vérifier l’interpréteur ;
2. vérifier l’environnement actif ;
3. vérifier la version du paquet ;
4. vérifier les dépendances ;
5. reproduire dans un environnement neuf ;
6. tester sans backend GPU ;
7. comparer avec le fichier de verrouillage.

## 16. Recréer plutôt que réparer indéfiniment

Lorsque `.venv` est corrompu ou incohérent :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Remove-Item .\.venv -Recurse -Force
uv sync --locked
```

Avec `venv` et `requirements.txt` :

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
Remove-Item .\.venv -Recurse -Force
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Cette opération est sûre uniquement si les dépendances et configurations nécessaires sont déclarées hors de `.venv`.

## 17. Sécurité de la chaîne Python

- installer depuis les index et dépôts officiels attendus ;
- examiner les noms proches de paquets connus ;
- conserver le fichier de verrouillage ;
- éviter `--trusted-host` et les hôtes non vérifiés ;
- ne pas désactiver TLS pour contourner une erreur ;
- vérifier les licences ;
- examiner les scripts d’installation de dépendances sensibles ;
- ne pas exécuter un notebook ou un script inconnu sur les données du projet ;
- traiter les modèles sérialisés exécutables avec prudence.

Les formats comme `pickle` peuvent exécuter du code lors du chargement. Préférer les formats de modèles et de données conçus pour limiter ce risque lorsque l’écosystème le permet.

## 18. Mode Solo

Le Mode Solo utilise :

- `uv` pour les nouveaux scripts et outils internes ;
- un environnement séparé par application tierce ;
- un fichier de verrouillage versionné ;
- des mises à jour manuelles et testées ;
- la reconstruction de `.venv` plutôt que sa sauvegarde complète.

## 19. Mode Studio

Le Mode Studio ajoute :

- versions Python approuvées ;
- miroir ou cache de paquets contrôlé ;
- analyse des dépendances ;
- SBOM lorsque nécessaire ;
- CI avec `uv sync --locked` ;
- tests sur plusieurs versions de Python ;
- procédure d’approbation des nouveaux paquets ;
- conservation des artefacts nécessaires à une reconstruction hors ligne.

## 20. Test de validation

> **[PS] PowerShell 7 - Exécuter :** utiliser PowerShell sur l’hôte Windows.

```powershell
$root = Join-Path $HOME "ia-gamedev-python-check"
New-Item -ItemType Directory -Force $root | Out-Null
Set-Location $root

uv init
uv add pyyaml
@"
import sys
import yaml

print(sys.executable)
print(yaml.safe_load("status: ok"))
"@ | Out-File .\main.py -Encoding utf8

uv run python .\main.py
uv lock --check
uv tree
```

Critères :

- [ ] `py --list` affiche les versions installées.
- [ ] `uv --version` fonctionne.
- [ ] Un environnement `.venv` est créé.
- [ ] `.venv/` est ignoré par Git.
- [ ] `pyproject.toml` déclare les dépendances.
- [ ] `uv.lock` est présent et versionné.
- [ ] `uv sync --locked` reconstruit l’environnement.
- [ ] `python`, `pip` et les paquets pointent vers le même environnement.
- [ ] Le lecteur sait recréer l’environnement depuis zéro.
- [ ] Aucun paquet n’est installé globalement sans justification.

## 21. Sources officielles vérifiées

- [Utilisation de Python sous Windows](https://docs.python.org/3/using/windows.html)
- [Module `venv`](https://docs.python.org/3/library/venv.html)
- [Guide officiel du packaging Python](https://packaging.python.org/)
- [Installation de `uv`](https://docs.astral.sh/uv/getting-started/installation/)
- [Projets `uv`](https://docs.astral.sh/uv/concepts/projects/)
- [Verrouillage et synchronisation `uv`](https://docs.astral.sh/uv/concepts/projects/sync/)
- [Structure d’un projet `uv`](https://docs.astral.sh/uv/concepts/projects/layout/)

## 22. Résumé

Python doit être géré comme une dépendance de projet, non comme une installation globale unique.

Le lecteur doit pouvoir :

- sélectionner une version explicite ;
- créer un environnement isolé ;
- déclarer les dépendances ;
- verrouiller leur résolution ;
- reconstruire l’environnement ;
- diagnostiquer l’interpréteur réellement utilisé ;
- séparer les backends incompatibles.

Le chapitre suivant installe Docker sur ce socle Windows, Git et Python.
