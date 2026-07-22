---
title: "Livre II — Chapitre 29 : Automatisation Python et génération de données"
id: "DOC-L2-CH29"
status: "reviewed"
version: "1.0.1"
lang: "fr-FR"
book: "Livre II"
chapter: 29
last-verified: "2026-07-22T07:05:00+02:00"
audit-status: "complete"
audit-date: "2026-07-22T07:05:00+02:00"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-29.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-python:
  implementation: "CPython"
  version: "3.14.6"
  fallback-version: "3.13.14"
  qualification-status: "provisional"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Automatisation Python et génération de données

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH29`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence :** Godot `4.7.1-stable`, cible principale CPython `3.14.6`, repli CPython `3.13.14`, édition Standard, GDScript, Forward+  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-29.md`.  
> **Explications de code :** structurées bloc par bloc ; les sections d’erreurs conservent la séquence directe symptôme, exemple fautif, explication, exemple corrigé et explication de la correction.

## 1. Rôle du chapitre

Python sert ici d’outil de production, d’orchestration et de transformation. Il prépare des entrées, appelle des validateurs, consolide des résultats et construit des artefacts reproductibles. Il ne devient jamais l’autorité métier du jeu : les règles de personnages, d’économie, de politique, de narration ou de sauvegarde restent dans leurs systèmes propriétaires.

Le chapitre met en place une chaîne locale capable de fonctionner hors ligne. Elle doit produire le même résultat à partir des mêmes sources, versions, paramètres et graines, indépendamment de l’ordre de découverte des fichiers ou de la vitesse relative des tâches.

## 2. Prérequis et frontières

Le lecteur doit connaître les pipelines de contenu du chapitre 26, les suites et simulations du chapitre 27, ainsi que les journaux, manifestes et paquets de diagnostic du chapitre 28.

Le chapitre automatise ces contrats sans les redéfinir. Un script Python peut demander une validation de contenu, lancer une simulation ou empaqueter un diagnostic ; il ne peut pas décider qu’un contenu invalide devient valide, qu’un test échoué devient réussi ou qu’une donnée générée est promue sans contrôle.

Le chapitre 30 restera responsable de l’architecture finale des parcours Solo et Studio.

CPython `3.14.6` est une **cible principale de qualification**, pas encore un environnement universellement garanti. CPython `3.13.14` reste le repli documenté tant que l’ensemble réel des dépendances du Starter Kit n’a pas passé la matrice de qualification. Cette distinction interdit de déduire la compatibilité de futures bibliothèques à partir des seules dépendances minimales de ce chapitre.

## 3. Définitions opérationnelles

### 3.1 Automatisation

Une automatisation est une commande répétable dont les entrées, sorties, codes d’échec et effets de bord sont explicites. Elle doit être exécutable par une personne, une tâche locale ou une intégration continue sans modifier sa signification.

### 3.2 Génération déterministe

Une génération est déterministe lorsque les mêmes sources canoniques, la même version d’outil, la même configuration et la même graine produisent des octets identiques ou un ensemble d’artefacts canoniquement équivalent.

### 3.3 Orchestration

L’orchestration coordonne plusieurs outils sans absorber leur autorité. Elle collecte les codes de sortie, impose des délais, ordonne les artefacts et arrête la promotion lorsque l’un des contrats obligatoires échoue.

### 3.4 Reprise sur erreur

La reprise sur erreur consiste à reprendre une campagne depuis un point de contrôle valide. Elle ne signifie pas ignorer l’échec, relancer sans limite ni réutiliser une sortie partielle dont l’intégrité n’est pas établie.

## 4. Architecture cible

La chaîne comporte cinq couches : interface de commande, configuration, planification, exécution et publication. Les fonctions pures transforment des valeurs ; les adaptateurs accèdent au système de fichiers, lancent Godot ou créent une archive. Les manifestes relient chaque sortie aux entrées et versions qui l’ont produite.

## 5. Organiser l’arborescence d’automatisation
> **[LECTURE] Exemple du chapitre — Ne pas saisir.**

```text
automation/
├── pyproject.toml
├── pylock.toml
├── schemas/
│   ├── generation-job.schema.json
│   └── artifact-manifest.schema.json
├── src/asteria_tools/
│   ├── cli.py
│   ├── config.py
│   ├── planning.py
│   ├── execution.py
│   ├── generation.py
│   └── publication.py
├── tests/
└── work/
    ├── staging/
    ├── checkpoints/
    └── reports/
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** L’arborescence sépare le paquet Python, les schémas versionnés, les tests et les répertoires de travail jetables.
- **Responsabilités des dossiers :** `src/asteria_tools` contient le code versionné ; `schemas` décrit les échanges ; `work` reçoit uniquement des sorties régénérables.
- **Invariants protégés :** Aucun artefact temporaire n’est confondu avec une source canonique et aucun script n’écrit directement dans les données publiées.
- **Résultat attendu :** Une revue peut identifier immédiatement l’origine d’un fichier et le moment où il devient publiable.
- **Limites et réserves :** Le Starter Kit n’est pas matérialisé dans ce chapitre ; l’arborescence décrit le contrat à appliquer lors de sa création.

## 6. Créer un environnement virtuel sous Windows
> **[PS] Exemple du chapitre — Ne pas saisir.**

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip --version
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Les commandes créent un environnement isolé lié à la cible principale CPython 3.14 puis mettent à niveau `pip` dans cet environnement uniquement.
- **Paramètres importants :** `-3.14` sélectionne la cible principale ; le repli utilise `-3.13` dans un environnement distinct ; `.venv` est un répertoire local non versionné.
- **Valeur de retour ou code d’échec :** Chaque commande doit retourner `0`; une absence d’interpréteur ou un échec d’installation bloque la préparation.
- **Effets de bord :** Le dossier `.venv` est créé ou réutilisé et reçoit les paquets installés.
- **Invariants protégés :** Les dépendances du projet ne polluent pas l’installation Python globale de Windows.

## 7. Créer un environnement virtuel sous WSL
> **[WSL] Exemple du chapitre — Ne pas saisir.**

```bash
python3.14 -m venv .venv
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip --version
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La procédure WSL crée un environnement distinct de celui de Windows et utilise toujours l’exécutable interne.
- **Déroulement important :** La création précède toute installation ; les commandes suivantes ciblent explicitement `.venv/bin/python`.
- **Code d’échec :** Une commande non nulle signale un interpréteur manquant, un module `venv` absent ou un problème d’installation.
- **Effets de bord :** Un environnement Linux local est créé sans partager ses binaires avec `.venv` Windows.
- **Limites et réserves :** Un même dossier `.venv` ne doit pas être monté alternativement par Windows et WSL.

## 8. Déclarer le projet dans pyproject.toml
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```toml
[build-system]
requires = ["hatchling==1.31.0"]
build-backend = "hatchling.build"

[project]
name = "asteria-tools"
version = "0.1.0"
requires-python = ">=3.13.14,<3.15"
dependencies = [
  "jsonschema==4.26.0",
]

[project.scripts]
asteria-tools = "asteria_tools.cli:main"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le fichier déclare le backend de construction, la compatibilité Python, la dépendance de validation et le point d’entrée CLI.
- **Paramètres et types importants :** `requires-python` est une contrainte de version ; `dependencies` est une liste de spécifications épinglées ; `project.scripts` associe un nom exécutable à une fonction.
- **Effets de bord :** Les outils d’installation utilisent ces métadonnées pour construire et exposer la commande `asteria-tools`.
- **Invariants protégés :** Une exécution avec une série Python non prévue ou une dépendance non résolue doit échouer avant la génération.
- **Limites et réserves :** `hatchling 1.31.0` et `jsonschema 4.26.0` déclarent Python 3.14, mais leur présence ne garantit ni les futures dépendances ni les intégrations propres au Starter Kit.

## 9. Produire un fichier de verrouillage
> **[PS] Exemple du chapitre — Ne pas saisir.**

```powershell
.\.venv\Scripts\python.exe -m pip lock -e . -o pylock.windows.toml
.\.venv\Scripts\python.exe -m pip check
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La première commande demande un verrou pour le projet local ; la seconde vérifie la cohérence des dépendances installées.
- **Paramètres importants :** `-e .` cible le projet courant et `-o` choisit un verrou nommé pour la plateforme Windows.
- **Valeur de retour :** `pip check` retourne `0` si les dépendances installées sont compatibles et `1` lorsqu’une exigence manque ou possède une mauvaise version.
- **Invariants protégés :** Le verrou est distinct par environnement lorsque les roues ou marqueurs de plateforme diffèrent.
- **Limites et réserves :** `pip lock` est expérimental ; son format de sortie et son intégration doivent être validés avant d’en faire une dépendance de publication.

**Statut de qualification de l’interpréteur et des dépendances.**

La cible principale est CPython `3.14.6`. CPython `3.13.14` constitue le repli tant que la matrice complète du Starter Kit n’est pas validée. Le paquet d’automatisation reste volontairement minimal : les environnements de ComfyUI, de génération vocale, de LLM, de bases vectorielles ou d’autres services spécialisés conservent leurs propres interpréteurs et verrous.

Les dépendances minimales vérifiées par la matrice sont `hatchling==1.31.0` et `jsonschema==4.26.0`, ainsi que les dépendances transitives résolues par `pip`. L’installation doit utiliser `--only-binary=:all:` pendant la qualification afin qu’une roue native manquante provoque un échec visible au lieu d’une compilation implicite.

**État de qualification CI :** en attente de la matrice GitHub Actions.

| Environnement de qualification | Interpréteur | Rôle | État |
|---|---:|---|---|
| Windows hébergé x86-64 | CPython 3.14.6 | cible principale | à vérifier par la matrice CI |
| Linux hébergé x86-64 | CPython 3.14.6 | proxy de compatibilité pour WSL | à vérifier par la matrice CI |
| Windows hébergé x86-64 | CPython 3.13.14 | repli | à vérifier par la matrice CI |
| Linux hébergé x86-64 | CPython 3.13.14 | proxy de compatibilité pour WSL | à vérifier par la matrice CI |

Linux hébergé vérifie la disponibilité des distributions et les imports sous Linux, mais ne valide pas à lui seul les chemins montés, permissions, interactions Windows/WSL ou performances d’un WSL réel.

**Critères avant de déclarer un environnement validé.**

1. résolution complète sans conflit ;
2. installation avec roues binaires uniquement pour tout paquet natif ;
3. `pip check` sans erreur ;
4. import et lecture de version de chaque dépendance directe ;
5. exécution des tests et commandes du Starter Kit ;
6. verrous distincts pour chaque version de Python et chaque plateforme ;
7. reconstruction réussie dans un environnement vierge ;
8. validation séparée sur un WSL réel avant toute promesse spécifique à WSL.

## 10. Décrire la configuration de campagne
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```toml
schema_version = 1
campaign_id = "nightly-small-world"
workspace = "work/nightly-small-world"
maximum_workers = 4
fail_fast = true

[generation]
seed = 84217
source_root = "content/source"
output_root = "work/nightly-small-world/staging"

[validation]
json_schema_root = "automation/schemas"
maximum_file_bytes = 4194304
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La configuration regroupe l’identité de campagne, les limites de concurrence et les racines de génération et de validation.
- **Paramètres et types importants :** Les versions, limites et graines sont des entiers ; les chemins sont relatifs à la racine du dépôt ; `fail_fast` est un booléen explicite.
- **Effets de bord :** Aucun : le fichier décrit une intention et ne lance pas la campagne.
- **Invariants protégés :** La campagne ne dépend ni du répertoire courant implicite ni d’un nombre de workers choisi automatiquement.
- **Résultat attendu :** Deux opérateurs lisent la même configuration et construisent un plan identique.

## 11. Charger un TOML avec une taille bornée
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from pathlib import Path
import tomllib

MAX_CONFIG_BYTES = 1_048_576

def load_toml(path: Path) -> dict[str, object]:
    size = path.stat().st_size
    if size > MAX_CONFIG_BYTES:
        raise ValueError(f"configuration trop volumineuse: {size}")
    with path.open("rb") as stream:
        return tomllib.load(stream)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** `load_toml` refuse les configurations anormalement volumineuses puis délègue le décodage TOML à la bibliothèque standard.
- **Paramètres et types importants :** `path` est un `Path`; la fonction retourne un dictionnaire générique qui doit encore être validé sémantiquement.
- **Valeur de retour ou code d’échec :** Une structure TOML décodée est retournée ; une taille excessive, un fichier absent ou un TOML invalide lève une exception.
- **Effets de bord :** Le fichier est lu sans modification.
- **Limites et réserves :** `tomllib` ne valide pas les clés métier et ne sait pas écrire du TOML.

## 12. Convertir la configuration en types explicites
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True, slots=True)
class CampaignSettings:
    campaign_id: str
    workspace: Path
    maximum_workers: int
    fail_fast: bool
    seed: int

    def validate(self) -> None:
        if not self.campaign_id or "/" in self.campaign_id:
            raise ValueError("campaign_id invalide")
        if not 1 <= self.maximum_workers <= 16:
            raise ValueError("maximum_workers hors limites")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La dataclass transforme une configuration libre en valeur immuable avec des contraintes locales.
- **Responsabilités de la classe :** `CampaignSettings` conserve les paramètres validés ; `validate()` refuse les identités ambiguës et la concurrence excessive.
- **Paramètres et types importants :** `workspace` est un chemin ; `maximum_workers` et `seed` sont des entiers ; `fail_fast` reste un booléen.
- **Valeur de retour ou code d’échec :** `validate()` ne retourne rien en cas de succès et lève `ValueError` à la première violation.
- **Invariants protégés :** Une campagne planifiée ne peut plus changer silencieusement de configuration pendant son exécution.

## 13. Définir des codes de sortie stables
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from enum import IntEnum

class ExitCode(IntEnum):
    OK = 0
    INVALID_ARGUMENTS = 2
    INVALID_CONFIGURATION = 3
    VALIDATION_FAILED = 4
    EXECUTION_FAILED = 5
    INTEGRITY_FAILED = 6
    INTERNAL_ERROR = 10
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** L’énumération fournit une interface stable entre la CLI, PowerShell, WSL et l’intégration continue.
- **Responsabilités :** Chaque valeur distingue une famille d’échec actionnable sans analyser un message humain.
- **Valeur de retour :** Les membres sont convertibles en entiers et utilisés comme code de fin du processus.
- **Invariants protégés :** Une validation métier échouée n’est pas confondue avec une exception interne de l’outil.
- **Limites et réserves :** Les codes ne remplacent pas le rapport détaillé associé à la campagne.

## 14. Construire une CLI typée avec argparse
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
import argparse
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="asteria-tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate = subparsers.add_parser("generate")
    generate.add_argument("--config", type=Path, required=True)
    generate.add_argument("--resume", action="store_true")

    validate = subparsers.add_parser("validate")
    validate.add_argument("--manifest", type=Path, required=True)
    return parser
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** `build_parser` définit deux sous-commandes et convertit immédiatement les chemins en objets `Path`.
- **Paramètres et types importants :** `dest=command` rend le choix accessible ; `required=True` interdit une invocation sans action ; `--resume` produit un booléen.
- **Valeur de retour ou code d’échec :** La fonction retourne le parser ; `argparse` termine avec le code `2` lorsque la syntaxe est invalide.
- **Effets de bord :** Aucun tant que `parse_args()` n’est pas appelé.
- **Invariants protégés :** La commande sélectionnée et ses paramètres obligatoires sont connus avant l’accès au système de fichiers.

## 15. Router la commande principale
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "generate":
            return int(run_generation(args.config, args.resume))
        if args.command == "validate":
            return int(run_validation(args.manifest))
        return int(ExitCode.INVALID_ARGUMENTS)
    except ValueError as exc:
        print(f"configuration invalide: {exc}")
        return int(ExitCode.INVALID_CONFIGURATION)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** `main` adapte les arguments de processus aux fonctions applicatives et traduit les erreurs de configuration en code stable.
- **Paramètres et types importants :** `argv` permet les tests unitaires sans modifier `sys.argv`; les fonctions appelées retournent un `ExitCode`.
- **Valeur de retour :** Un entier est toujours retourné au lanceur.
- **Effets de bord :** Le message d’erreur est écrit sur la sortie standard dans cet exemple minimal.
- **Limites et réserves :** Les erreurs internes inattendues doivent être journalisées et mappées séparément à `INTERNAL_ERROR` dans l’implémentation complète.

## 16. Résoudre la racine du dépôt
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from pathlib import Path

MARKER = "CONTINUITE-PROJET.md"

def find_repository_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in (current, *current.parents):
        if (candidate / MARKER).is_file():
            return candidate
    raise FileNotFoundError(f"racine introuvable depuis {start}")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction localise la racine à partir d’un marqueur versionné au lieu de supposer le répertoire courant.
- **Paramètres et types importants :** `start` peut désigner un fichier ou dossier de travail ; `resolve()` normalise le chemin local.
- **Valeur de retour ou code d’échec :** La première racine contenant le marqueur est retournée ; sinon `FileNotFoundError` est levée.
- **Effets de bord :** Seules des vérifications d’existence sont effectuées.
- **Invariants protégés :** Tous les chemins relatifs d’une campagne partagent la même base explicite.

## 17. Interdire les sorties hors du workspace
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
def resolve_inside(root: Path, relative: str) -> Path:
    if Path(relative).is_absolute():
        raise ValueError("chemin absolu interdit")
    candidate = (root / relative).resolve()
    if not candidate.is_relative_to(root.resolve()):
        raise ValueError("sortie hors workspace")
    return candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** `resolve_inside` protège les écritures contre les chemins absolus et les remontées `..`.
- **Paramètres et types importants :** `root` est la frontière autorisée ; `relative` provient d’une configuration validée.
- **Valeur de retour ou code d’échec :** Un chemin canonique interne est retourné ou `ValueError` bloque l’opération.
- **Effets de bord :** Aucun fichier n’est créé.
- **Invariants protégés :** Une campagne ne peut pas écraser une source du dépôt ni un fichier extérieur au workspace.

## 18. Écrire un fichier par remplacement contrôlé
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
import os
from pathlib import Path


def atomic_write_bytes(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("wb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction écrit d’abord un fichier temporaire voisin puis remplace la destination après vidage du tampon.
- **Paramètres et types importants :** `payload` contient les octets finaux ; la destination est un `Path` déjà validé.
- **Valeur de retour ou code d’échec :** Aucune valeur n’est retournée ; les erreurs d’E/S restent visibles à l’appelant.
- **Effets de bord :** Le dossier parent peut être créé et la destination est remplacée.
- **Limites et réserves :** Le remplacement contrôlé ne constitue pas une promesse d’atomicité universelle sur tous les systèmes de fichiers.

## 19. Sérialiser du JSON canonique
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
import json
from typing import Any


def canonical_json_bytes(value: Any) -> bytes:
    text = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )
    return (text + "\n").encode("utf-8")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction impose l’ordre des clés, des séparateurs sans espaces, UTF-8 et l’interdiction des valeurs non finies.
- **Paramètres et types importants :** `value` doit être composé de types JSON ; le retour est une séquence d’octets prête à hacher ou écrire.
- **Valeur de retour ou code d’échec :** Les octets canoniques sont retournés ; un type non sérialisable ou `NaN` provoque une exception.
- **Invariants protégés :** Deux structures JSON égales produisent la même représentation indépendamment de l’ordre d’insertion des dictionnaires.
- **Résultat attendu :** Les empreintes et golden files ne changent pas pour une simple variation de mise en forme.

## 20. Calculer une empreinte SHA-256
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from hashlib import sha256
from pathlib import Path


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    digest = sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(chunk_size):
            digest.update(chunk)
    return digest.hexdigest()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction calcule l’empreinte d’un fichier sans le charger entièrement en mémoire.
- **Paramètres et types importants :** `chunk_size` borne la mémoire de lecture ; le retour est une chaîne hexadécimale de 64 caractères.
- **Valeur de retour ou code d’échec :** L’empreinte est retournée ; une erreur d’ouverture ou de lecture est propagée.
- **Effets de bord :** Le fichier est lu sans modification.
- **Limites et réserves :** Une empreinte prouve l’intégrité relative aux octets attendus, pas l’identité de l’auteur ni l’origine du fichier.

## 21. Définir un manifeste d’artefact
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ArtifactRecord:
    relative_path: str
    media_type: str
    size_bytes: int
    sha256: str

@dataclass(frozen=True, slots=True)
class CampaignManifest:
    schema_version: int
    campaign_id: str
    tool_version: str
    python_version: str
    source_revision: str
    seed: int
    artifacts: tuple[ArtifactRecord, ...]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Les deux dataclasses décrivent les preuves minimales nécessaires pour relier une campagne à ses sorties.
- **Responsabilités des classes :** `ArtifactRecord` décrit un fichier ; `CampaignManifest` décrit l’ensemble ordonné de la campagne.
- **Paramètres et types importants :** Les chemins restent relatifs ; les tailles sont entières ; la collection d’artefacts est un tuple immuable.
- **Invariants protégés :** Le manifeste ne contient ni chemin absolu, ni objet mutable, ni date utilisée comme identité de sortie.
- **Limites et réserves :** La signature cryptographique et l’attestation de provenance restent des couches distinctes.

## 22. Créer un générateur pseudo-aléatoire local
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from random import Random


def build_rng(master_seed: int, namespace: str) -> Random:
    material = canonical_json_bytes({
        "master_seed": str(master_seed),
        "namespace": namespace,
    })
    derived_seed = int.from_bytes(sha256(material).digest()[:16], "big")
    return Random(derived_seed)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction dérive une graine indépendante par espace de noms et construit un RNG local.
- **Paramètres et types importants :** `master_seed` est sérialisé en chaîne pour éviter les limites JSON des grands entiers ; `namespace` identifie un flux de génération.
- **Valeur de retour :** Un objet `Random` isolé est retourné.
- **Effets de bord :** Aucun état aléatoire global n’est modifié.
- **Invariants protégés :** Ajouter une nouvelle famille de données ne décale pas les tirages des familles existantes si leurs namespaces restent stables.

## 23. Trier les sources avant génération
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
def discover_json_sources(root: Path) -> tuple[Path, ...]:
    candidates = (
        path for path in root.rglob("*.json")
        if path.is_file() and not path.name.startswith(".")
    )
    return tuple(sorted(candidates, key=lambda p: p.relative_to(root).as_posix()))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La découverte collecte les fichiers JSON puis impose un ordre lexical sur les chemins relatifs POSIX.
- **Paramètres et types importants :** `root` est une racine validée ; le retour est un tuple de `Path`.
- **Valeur de retour :** Une séquence stable, éventuellement vide, est retournée.
- **Effets de bord :** Le système de fichiers est parcouru en lecture seule.
- **Invariants protégés :** L’ordre de génération ne dépend pas de l’ordre fourni par le système de fichiers.

## 24. Construire des identifiants dérivés stables
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from uuid import UUID, uuid5

ASTERIA_NAMESPACE = UUID("6c8a8d40-9863-5ac8-b8d4-4f4b76716ef2")

def stable_content_id(kind: str, source_key: str) -> str:
    normalized = f"{kind.strip().lower()}:{source_key.strip().lower()}"
    return str(uuid5(ASTERIA_NAMESPACE, normalized))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction dérive un UUID reproductible depuis une catégorie et une clé source normalisées.
- **Paramètres et types importants :** `kind` et `source_key` sont des identifiants techniques, jamais des noms affichés localisés.
- **Valeur de retour :** Une chaîne UUID canonique est retournée.
- **Effets de bord :** Aucun registre global n’est modifié.
- **Limites et réserves :** Changer la normalisation ou le namespace constitue une migration d’identité et doit être versionné explicitement.

## 25. Modéliser une définition générée
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from dataclasses import asdict, dataclass

@dataclass(frozen=True, slots=True)
class GeneratedBiome:
    biome_id: str
    display_name_key: str
    moisture_permille: int
    temperature_milli_celsius: int
    resource_ids: tuple[str, ...]

    def to_json(self) -> dict[str, object]:
        return asdict(self)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La dataclass représente une sortie de génération avant sérialisation.
- **Responsabilités :** Elle regroupe l’identité stable, la clé de traduction et des unités entières explicites.
- **Paramètres et types importants :** L’humidité est en millièmes et la température en milli-degrés Celsius ; les ressources sont ordonnées dans un tuple.
- **Valeur de retour :** `to_json()` produit un dictionnaire composé de types sérialisables.
- **Invariants protégés :** Les unités et identités ne sont pas déduites d’un texte affiché ou d’un nombre flottant implicite.

## 26. Générer une collection de biomes
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
def generate_biomes(seed: int, count: int) -> tuple[GeneratedBiome, ...]:
    if not 1 <= count <= 256:
        raise ValueError("count hors limites")
    rng = build_rng(seed, "biomes-v1")
    generated: list[GeneratedBiome] = []
    for index in range(count):
        source_key = f"generated-{index:04d}"
        generated.append(GeneratedBiome(
            biome_id=stable_content_id("biome", source_key),
            display_name_key=f"biome.{source_key}.name",
            moisture_permille=rng.randrange(0, 1001),
            temperature_milli_celsius=rng.randrange(-30_000, 50_001),
            resource_ids=(),
        ))
    return tuple(generated)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction construit une série bornée de définitions à partir d’une graine et d’un namespace versionné.
- **Paramètres et types importants :** `count` est limité à 256 ; les bornes des grandeurs sont inclusives selon les appels `randrange`.
- **Valeur de retour ou code d’échec :** Un tuple ordonné est retourné ; une quantité invalide lève `ValueError`.
- **Effets de bord :** Aucun fichier n’est écrit pendant la génération pure.
- **Invariants protégés :** La position d’un biome, son identité et ses valeurs sont reproductibles pour une même graine et une même version d’algorithme.

## 27. Déclarer un schéma JSON versionné
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://asteria.invalid/schemas/generated-biome-v1.json",
  "type": "object",
  "required": [
    "biome_id",
    "display_name_key",
    "moisture_permille",
    "temperature_milli_celsius",
    "resource_ids"
  ],
  "additionalProperties": false,
  "properties": {
    "biome_id": {"type": "string", "format": "uuid"},
    "display_name_key": {"type": "string", "minLength": 1},
    "moisture_permille": {"type": "integer", "minimum": 0, "maximum": 1000},
    "temperature_milli_celsius": {"type": "integer", "minimum": -30000, "maximum": 50000},
    "resource_ids": {"type": "array", "items": {"type": "string"}, "uniqueItems": true}
  }
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le schéma décrit la forme externe attendue pour une définition de biome générée.
- **Paramètres et types importants :** `$schema` fixe le dialecte 2020-12 ; `$id` identifie le schéma ; `additionalProperties: false` ferme le contrat.
- **Valeur de retour ou code d’échec :** Le schéma n’exécute rien seul ; un validateur compatible produit ensuite une liste d’erreurs ou un succès.
- **Invariants protégés :** Les bornes, types et clés obligatoires sont vérifiables indépendamment du code Python.
- **Limites et réserves :** Le mot-clé `default` ne remplit pas automatiquement les propriétés absentes.

## 28. Valider une instance avec JSON Schema
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from jsonschema import Draft202012Validator, FormatChecker


def validate_instance(schema: dict[str, object], instance: object) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(instance), key=lambda e: tuple(e.absolute_path))
    return [
        f"/{'/'.join(map(str, error.absolute_path))}: {error.message}"
        for error in errors
    ]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction exécute le dialecte choisi, active les formats et retourne toutes les violations dans un ordre stable.
- **Paramètres et types importants :** `schema` est un dictionnaire décodé ; `instance` peut être toute valeur JSON ; le retour est une liste de messages.
- **Valeur de retour :** Une liste vide signifie que le validateur n’a trouvé aucune violation ; elle ne signifie pas que la donnée est correcte métier.
- **Effets de bord :** Aucun fichier n’est modifié.
- **Invariants protégés :** L’ordre des diagnostics ne dépend pas de l’ordre interne du validateur.

## 29. Accumuler des diagnostics structurés
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Diagnostic:
    code: str
    source: str
    pointer: str
    message: str


def schema_diagnostics(source: Path, messages: list[str]) -> tuple[Diagnostic, ...]:
    return tuple(
        Diagnostic("SCHEMA_INVALID", source.as_posix(), message.split(":", 1)[0], message)
        for message in messages
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le modèle remplace les chaînes isolées par des diagnostics dotés d’un code, d’une source et d’un pointeur.
- **Responsabilités :** `Diagnostic` porte une observation ; `schema_diagnostics` adapte les messages du validateur au format de campagne.
- **Valeur de retour :** Un tuple stable de diagnostics est retourné.
- **Effets de bord :** Aucun journal n’est écrit par cette fonction pure.
- **Limites et réserves :** Le découpage de message illustré doit être remplacé par les propriétés structurées de l’erreur dans l’implémentation complète.

## 30. Planifier des tâches immuables
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkItem:
    item_id: str
    source_path: str
    output_path: str
    seed: int


def build_plan(
    sources: tuple[Path, ...],
    source_root: Path,
    output_root: Path,
    master_seed: int,
) -> tuple[WorkItem, ...]:
    plan = []
    for source in sources:
        relative = source.relative_to(source_root).as_posix()
        output = output_root / Path(relative).with_suffix(".generated.json")
        plan.append(WorkItem(
            item_id=stable_content_id("work-item", relative),
            source_path=relative,
            output_path=output.as_posix(),
            seed=int.from_bytes(sha256(relative.encode()).digest()[:8], "big") ^ master_seed,
        ))
    return tuple(sorted(plan, key=lambda item: item.item_id))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** `build_plan` transforme une liste de sources en unités de travail indépendantes et ordonnées.
- **Paramètres et types importants :** Chaque tâche contient des chemins sérialisables, une identité stable et une graine dérivée.
- **Valeur de retour :** Un tuple trié par `item_id` est retourné.
- **Effets de bord :** La planification ne crée aucune sortie.
- **Invariants protégés :** Une reprise peut comparer le plan courant au plan enregistré avant de réutiliser un checkpoint.

## 31. Lancer Godot sans shell intermédiaire
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
import subprocess


def run_godot(project_root: Path, script: Path, report: Path, timeout_seconds: int) -> subprocess.CompletedProcess[str]:
    command = [
        "godot",
        "--headless",
        "--path", str(project_root),
        "--script", str(script),
        "--", "--report", str(report),
    ]
    return subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
        shell=False,
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction lance un script Godot headless avec une liste d’arguments et capture ses sorties.
- **Paramètres et types importants :** Les chemins sont passés comme éléments distincts ; `timeout_seconds` borne l’attente du processus externe.
- **Valeur de retour ou code d’échec :** Un `CompletedProcess` expose `returncode`, `stdout` et `stderr`; un dépassement lève `TimeoutExpired`.
- **Effets de bord :** Godot peut lire le projet et écrire le rapport explicitement demandé.
- **Invariants protégés :** Aucune chaîne de commande n’est interprétée par un shell et aucune entrée utilisateur ne devient une option implicite.

## 32. Normaliser le résultat d’un processus
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
@dataclass(frozen=True, slots=True)
class ProcessResult:
    command: tuple[str, ...]
    return_code: int
    stdout_tail: str
    stderr_tail: str


def normalize_process(result: subprocess.CompletedProcess[str], command: list[str]) -> ProcessResult:
    return ProcessResult(
        command=tuple(command),
        return_code=result.returncode,
        stdout_tail=result.stdout[-8192:],
        stderr_tail=result.stderr[-8192:],
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le modèle conserve les informations utiles d’un processus tout en bornant les sorties intégrées au rapport.
- **Paramètres et types importants :** La commande devient un tuple ; les extraits sont limités à 8192 caractères chacun.
- **Valeur de retour :** Un `ProcessResult` immuable est retourné.
- **Effets de bord :** Aucun fichier n’est écrit.
- **Limites et réserves :** Les journaux complets peuvent être conservés comme artefacts séparés lorsque la politique de confidentialité l’autorise.

## 33. Orchestrer les validateurs documentaires
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
@dataclass(frozen=True, slots=True)
class ToolCommand:
    name: str
    argv: tuple[str, ...]
    required: bool = True

VALIDATION_COMMANDS = (
    ToolCommand("chapters", ("python", "tools/validate_chapters.py", "--report", "work/reports/chapters.md")),
    ToolCommand("contexts", ("python", "tools/check_context_markers.py", "--check")),
    ToolCommand("semantic-contexts", ("python", "tools/audit_contextes_semantiques.py", "--check")),
)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La table de commandes rend l’orchestration déclarative et associe un nom stable à chaque outil obligatoire.
- **Paramètres et types importants :** `argv` est un tuple déjà séparé ; `required` distingue un contrôle bloquant d’une information facultative.
- **Valeur de retour :** Le bloc définit des valeurs ; l’exécuteur décidera ensuite du code global.
- **Invariants protégés :** Le script Python ne recopie pas les règles des validateurs et ne transforme pas un échec en succès.
- **Limites et réserves :** L’exécutable `python` doit être remplacé par `sys.executable` dans une implémentation portable complète.

## 34. Calculer le résultat global d’une campagne
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
def campaign_exit(results: tuple[ProcessResult, ...], commands: tuple[ToolCommand, ...]) -> ExitCode:
    required_by_name = {command.name: command.required for command in commands}
    for result in results:
        name = Path(result.command[1]).stem if len(result.command) > 1 else result.command[0]
        if result.return_code != 0 and required_by_name.get(name, True):
            return ExitCode.VALIDATION_FAILED
    return ExitCode.OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction réduit plusieurs résultats à un code de campagne sans masquer les échecs obligatoires.
- **Paramètres et types importants :** Les résultats et commandes sont des tuples ; la correspondance par nom doit être stabilisée dans l’implémentation finale.
- **Valeur de retour :** `VALIDATION_FAILED` est retourné dès qu’un contrôle requis échoue, sinon `OK`.
- **Effets de bord :** Aucun.
- **Limites et réserves :** L’exemple illustre la politique ; un identifiant de commande explicite doit éviter de déduire le nom depuis le chemin.

## 35. Lire un flux JSONL borné
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
import json
from collections.abc import Iterator

MAX_LINE_BYTES = 1_048_576

def read_jsonl(path: Path) -> Iterator[dict[str, object]]:
    with path.open("rb") as stream:
        for line_number, raw in enumerate(stream, start=1):
            if len(raw) > MAX_LINE_BYTES:
                raise ValueError(f"ligne {line_number} trop volumineuse")
            value = json.loads(raw)
            if not isinstance(value, dict):
                raise ValueError(f"ligne {line_number}: objet attendu")
            yield value
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le lecteur traite le fichier ligne par ligne et refuse les enregistrements trop volumineux ou non objets.
- **Paramètres et types importants :** Le chemin est lu en binaire ; chaque valeur produite est un dictionnaire JSON.
- **Valeur de retour ou code d’échec :** La fonction est un itérateur ; une ligne invalide arrête la lecture avec `ValueError`.
- **Effets de bord :** Lecture seule du journal.
- **Invariants protégés :** Une entrée malveillante ne provoque pas le chargement intégral du fichier ni l’acceptation silencieuse d’un tableau ou scalaire.

## 36. Créer un checkpoint vérifiable
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
@dataclass(frozen=True, slots=True)
class Checkpoint:
    schema_version: int
    campaign_id: str
    plan_sha256: str
    completed_item_ids: tuple[str, ...]
    artifact_sha256_by_path: dict[str, str]


def write_checkpoint(path: Path, checkpoint: Checkpoint) -> None:
    payload = canonical_json_bytes(asdict(checkpoint))
    atomic_write_bytes(path, payload)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le checkpoint enregistre l’identité du plan, les tâches terminées et les empreintes des sorties réutilisables.
- **Responsabilités :** `Checkpoint` décrit l’état de reprise ; `write_checkpoint` sérialise et remplace le fichier de contrôle.
- **Valeur de retour ou code d’échec :** Aucune valeur n’est retournée ; une erreur de sérialisation ou d’écriture bloque la reprise.
- **Effets de bord :** Le checkpoint est écrit dans le workspace.
- **Invariants protégés :** Une sortie n’est considérée terminée que si son identité et son empreinte sont enregistrées ensemble.

## 37. Valider un checkpoint avant reprise
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
def reusable_items(checkpoint: Checkpoint, expected_plan_sha256: str, workspace: Path) -> set[str]:
    if checkpoint.plan_sha256 != expected_plan_sha256:
        return set()
    reusable: set[str] = set()
    for relative, expected_sha in sorted(checkpoint.artifact_sha256_by_path.items()):
        artifact = resolve_inside(workspace, relative)
        if artifact.is_file() and sha256_file(artifact) == expected_sha:
            reusable.add(relative)
    return reusable
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction refuse toute reprise si le plan a changé puis vérifie chaque artefact par son empreinte.
- **Paramètres et types importants :** Le retour est un ensemble de chemins réutilisables ; les chemins du checkpoint sont revalidés dans le workspace.
- **Valeur de retour :** Un ensemble vide force une régénération complète lorsque le plan diverge.
- **Effets de bord :** Les artefacts sont lus pour calculer leurs empreintes.
- **Invariants protégés :** La présence d’un fichier ou d’un identifiant de tâche ne suffit jamais à déclarer une étape terminée.

## 38. Publier depuis un staging fermé
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from shutil import copy2


def promote_artifacts(records: tuple[ArtifactRecord, ...], staging: Path, published: Path) -> None:
    for record in sorted(records, key=lambda item: item.relative_path):
        source = resolve_inside(staging, record.relative_path)
        if sha256_file(source) != record.sha256:
            raise ValueError(f"empreinte invalide: {record.relative_path}")
        destination = resolve_inside(published, record.relative_path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        copy2(source, destination)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La promotion copie uniquement les artefacts déclarés après vérification de leur empreinte.
- **Paramètres et types importants :** Les records sont triés par chemin ; staging et publication sont deux racines distinctes.
- **Valeur de retour ou code d’échec :** Aucune valeur n’est retournée ; une empreinte incorrecte arrête la promotion.
- **Effets de bord :** Les dossiers de destination sont créés et les fichiers publiés sont remplacés individuellement.
- **Limites et réserves :** Une promotion multi-fichiers exige une stratégie de transaction ou de bascule de répertoire adaptée au système de fichiers cible.

## 39. Exécuter des tâches avec un pool borné
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from concurrent.futures import ThreadPoolExecutor, as_completed


def execute_bounded(items: tuple[WorkItem, ...], workers: int) -> tuple[tuple[str, str], ...]:
    if not 1 <= workers <= 16:
        raise ValueError("workers hors limites")
    outputs: list[tuple[str, str]] = []
    with ThreadPoolExecutor(max_workers=workers, thread_name_prefix="asteria") as pool:
        future_by_id = {pool.submit(run_item, item): item.item_id for item in items}
        for future in as_completed(future_by_id):
            item_id = future_by_id[future]
            outputs.append((item_id, future.result()))
    return tuple(sorted(outputs, key=lambda pair: pair[0]))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction borne le nombre de threads, associe chaque future à une identité stable et trie les résultats après exécution.
- **Paramètres et types importants :** `workers` est limité à 16 ; `items` est un plan immuable ; le retour associe identités et chemins.
- **Valeur de retour ou code d’échec :** Un tuple trié est retourné ; l’exception d’une tâche est propagée par `future.result()`.
- **Effets de bord :** `run_item` peut produire des artefacts dans des emplacements indépendants.
- **Invariants protégés :** L’ordre de fin des threads ne change pas l’ordre canonique du rapport ou du manifeste.

## 40. Réserver ProcessPoolExecutor aux calculs adaptés
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from concurrent.futures import ProcessPoolExecutor


def compute_heavy_batches(batches: tuple[tuple[int, ...], ...], workers: int) -> tuple[int, ...]:
    with ProcessPoolExecutor(max_workers=workers) as pool:
        results = pool.map(score_batch, batches, chunksize=1)
        return tuple(results)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le pool de processus exécute des calculs CPU indépendants et sérialisables.
- **Paramètres et types importants :** Les lots et résultats doivent être picklables ; `workers` reste explicitement borné par la configuration.
- **Valeur de retour ou code d’échec :** Un tuple dans l’ordre des entrées est retourné ; un worker brisé ou une fonction non sérialisable provoque un échec.
- **Effets de bord :** Des processus enfants sont créés.
- **Limites et réserves :** Les lambdas, fonctions interactives et appels imbriqués aux méthodes d’Executor sont exclus ; l’entrée `__main__` doit être importable.

## 41. Annuler proprement après un échec bloquant
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
def cancel_pending(futures: dict[object, str]) -> None:
    for future in futures:
        if not future.done():
            future.cancel()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction demande l’annulation des tâches qui n’ont pas encore commencé après un échec bloquant.
- **Paramètres et types importants :** Les clés doivent fournir `done()` et `cancel()` comme les objets `Future`.
- **Valeur de retour :** Aucune valeur n’est retournée.
- **Effets de bord :** Les tâches en attente peuvent être annulées ; une tâche déjà en cours continue selon son propre contrat.
- **Limites et réserves :** `cancel()` ne constitue pas une interruption garantie d’une opération déjà lancée.

## 42. Définir une politique de nouvelle tentative bornée
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
@dataclass(frozen=True, slots=True)
class RetryPolicy:
    maximum_attempts: int
    retryable_codes: frozenset[str]

    def should_retry(self, attempt: int, error_code: str) -> bool:
        return attempt < self.maximum_attempts and error_code in self.retryable_codes
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La politique décide explicitement quelles erreurs transitoires peuvent être retentées et combien de fois.
- **Paramètres et types importants :** `attempt` commence à 1 ; les codes retentables forment un ensemble immuable.
- **Valeur de retour :** Un booléen indique si une nouvelle tentative est autorisée.
- **Effets de bord :** Aucun délai ni relance n’est effectué par cette classe.
- **Invariants protégés :** Une erreur de schéma, d’intégrité ou de règle métier ne devient pas retentable par défaut.

## 43. Écrire un rapport de campagne
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
@dataclass(frozen=True, slots=True)
class CampaignReport:
    campaign_id: str
    exit_code: int
    completed: int
    failed: int
    diagnostics: tuple[Diagnostic, ...]
    manifest_path: str | None


def write_report(path: Path, report: CampaignReport) -> None:
    atomic_write_bytes(path, canonical_json_bytes(asdict(report)))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le rapport résume l’issue de campagne dans un format machine lisible distinct du manifeste d’artefacts.
- **Responsabilités :** `CampaignReport` décrit le résultat ; `write_report` le sérialise canoniquement.
- **Valeur de retour ou code d’échec :** Aucune valeur n’est retournée ; l’écriture échouée doit influencer le code final de la CLI.
- **Effets de bord :** Un fichier de rapport est créé ou remplacé.
- **Invariants protégés :** Une campagne échouée peut produire un rapport sans produire de manifeste de publication.

## 44. Conserver une provenance minimale
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
import platform


def build_provenance(root: Path, tool_version: str) -> dict[str, object]:
    return {
        "schema_version": 1,
        "tool_version": tool_version,
        "python_version": platform.python_version(),
        "platform": platform.system().lower(),
        "source_revision": read_git_revision(root),
        "configuration_sha256": sha256_file(root / "automation/campaign.toml"),
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction rassemble les versions et empreintes nécessaires pour expliquer comment une campagne a été préparée.
- **Paramètres et types importants :** `tool_version` provient du paquet ; la révision et l’empreinte sont des chaînes stables.
- **Valeur de retour :** Un dictionnaire JSON sérialisable est retourné.
- **Effets de bord :** La configuration et les métadonnées Git sont lues.
- **Limites et réserves :** Le nom de plateforme seul ne décrit pas toutes les différences de roues ou de processeur ; le verrou d’environnement complète cette provenance.

## 45. Construire une archive déterministe
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ZIP_EPOCH = (1980, 1, 1, 0, 0, 0)

def write_deterministic_zip(destination: Path, root: Path, records: tuple[ArtifactRecord, ...]) -> None:
    with ZipFile(destination, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for record in sorted(records, key=lambda item: item.relative_path):
            source = resolve_inside(root, record.relative_path)
            info = ZipInfo(record.relative_path, date_time=ZIP_EPOCH)
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction fixe l’ordre, l’horodatage ZIP et les permissions pour réduire les variations d’archive.
- **Paramètres et types importants :** Les chemins sont relatifs et triés ; le niveau de compression est fixé à 9.
- **Valeur de retour ou code d’échec :** Aucune valeur n’est retournée ; toute lecture ou écriture impossible lève une exception.
- **Effets de bord :** Une archive ZIP est créée ou remplacée.
- **Limites et réserves :** ZIP fournit un conteneur et une compression ; il ne chiffre ni ne signe les fichiers.

## 46. Vérifier une archive avant diffusion
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from zipfile import ZipFile


def verify_zip(path: Path, expected: dict[str, str]) -> None:
    with ZipFile(path, "r") as archive:
        names = sorted(archive.namelist())
        if names != sorted(expected):
            raise ValueError("contenu ZIP inattendu")
        for name in names:
            payload = archive.read(name)
            if sha256(payload).hexdigest() != expected[name]:
                raise ValueError(f"empreinte ZIP invalide: {name}")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La vérification compare la liste fermée des membres puis l’empreinte de chaque contenu décompressé.
- **Paramètres et types importants :** `expected` associe chemins relatifs et empreintes SHA-256.
- **Valeur de retour ou code d’échec :** Le succès ne retourne rien ; tout membre absent, supplémentaire ou altéré lève `ValueError`.
- **Effets de bord :** L’archive est lue sans extraction sur disque.
- **Invariants protégés :** La diffusion ne repose pas uniquement sur la capacité de la bibliothèque à ouvrir le fichier ZIP.

## 47. Nettoyer uniquement les répertoires autorisés
> **[VSC] Exemple du chapitre — Ne pas saisir.**

```python
from shutil import rmtree

ALLOWED_CLEAN_ROOTS = {"staging", "reports", "checkpoints"}

def clean_workspace_subdir(workspace: Path, name: str) -> None:
    if name not in ALLOWED_CLEAN_ROOTS:
        raise ValueError("répertoire de nettoyage interdit")
    target = resolve_inside(workspace, name)
    if target.exists():
        rmtree(target)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La fonction limite la suppression à trois sous-répertoires jetables connus.
- **Paramètres et types importants :** `name` est comparé à une liste fermée avant résolution du chemin.
- **Valeur de retour ou code d’échec :** Aucune valeur n’est retournée ; un nom non autorisé lève `ValueError`.
- **Effets de bord :** Le sous-répertoire choisi et son contenu sont supprimés.
- **Invariants protégés :** Une configuration ne peut pas demander la suppression de la racine du dépôt, des sources ou d’un chemin arbitraire.

## 48. Produire un résumé lisible par l’intégration continue
> **[SORTIE] Exemple du chapitre — Ne pas saisir.**

```text
campaign=nightly-small-world
status=failed
exit_code=4
completed=127
failed=3
report=work/nightly-small-world/reports/campaign.json
manifest=
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La sortie courte expose des paires clé-valeur stables pour une console ou une étape d’intégration continue.
- **Paramètres importants :** Une valeur vide de `manifest` indique qu’aucun lot publiable n’a été produit.
- **Valeur de retour ou code d’échec :** Le processus associé doit terminer avec le code `4`, cohérent avec `VALIDATION_FAILED`.
- **Effets de bord :** Aucun ; il s’agit d’une sortie à lire.
- **Limites et réserves :** Le rapport JSON reste la source détaillée ; cette sortie ne doit pas être analysée comme un journal métier.

## 49. Décrire le pipeline complet
> **[LECTURE] Exemple du chapitre — Ne pas saisir.**

```text
configuration
    ↓ validation TOML et types
plan immuable
    ↓ génération dans staging
validation JSON Schema
    ↓ tests et simulations existants
consolidation des diagnostics
    ↓ manifeste et empreintes
promotion contrôlée
    ↓ archive et rapport
publication ou échec explicite
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le flux montre les portes successives entre configuration, exécution, validation et publication.
- **Déroulement important :** Chaque flèche suppose la réussite de l’étape précédente ; le staging précède toujours la promotion.
- **Invariants protégés :** Ni la génération, ni l’orchestrateur Python ne peuvent court-circuiter les validateurs propriétaires.
- **Résultat attendu :** Une campagne réussie produit un rapport, un manifeste et des artefacts vérifiés ; une campagne échouée produit un rapport sans promotion.
- **Limites et réserves :** Le diagramme ne décrit pas l’interface utilisateur du Mode Studio, réservée au chapitre 30.

## 50. Mode Solo

En Mode Solo, une seule personne maintient le paquet Python et privilégie une chaîne courte : un environnement virtuel local, une configuration de campagne, un staging, un rapport et un manifeste. Les commandes doivent rester exécutables depuis PowerShell ou WSL sans service distant obligatoire.

Le développeur Solo limite le nombre de variantes de plateforme, conserve des campagnes petites et explicites, puis élargit la génération seulement après avoir obtenu des sorties identiques sur plusieurs exécutions locales.

## 51. Mode Studio

En Mode Studio, les responsabilités sont séparées entre propriétaires de schémas, mainteneurs des générateurs, responsables des pipelines et personnes autorisées à promouvoir les artefacts. Les changements de schéma, d’algorithme de génération, de graine maîtresse ou de normalisation d’identité passent par revue.

Les campagnes de grande taille publient leurs plans, checkpoints, rapports et manifestes. Les permissions d’écriture sur les sources, le staging et les sorties publiées sont distinctes. Une intégration continue peut orchestrer les outils, mais ne modifie pas leurs critères de succès.

## 52. Contrat commun Solo et Studio

Dans les deux modes :

- l’environnement Python et ses dépendances sont versionnés ;
- les entrées et sorties possèdent des schémas explicites ;
- les chemins sont relatifs et confinés ;
- les générateurs utilisent des graines et ordres stables ;
- le parallélisme ne modifie pas l’ordre canonique des résultats ;
- chaque sortie publiée possède une empreinte et une provenance ;
- un échec obligatoire interdit la promotion ;
- les scripts Python n’acquièrent aucune autorité métier.

## 53. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 53.1 Utiliser le RNG global

**Symptôme :** Une nouvelle fonction change toutes les données générées après son insertion.

**Exemple fautif :**

> **[VSC] Contre-exemple — Ne pas saisir.**

```python
import random

def generate_value() -> int:
    return random.randint(0, 1000)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le module global partage un état implicite. L’ordre des appels devient une dépendance cachée de toute la campagne.

**Exemple corrigé :**

> **[VSC] Correction — Ne pas saisir.**

```python
def generate_value(seed: int, namespace: str) -> int:
    rng = build_rng(seed, namespace)
    return rng.randrange(0, 1001)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Chaque famille obtient un flux local dérivé d’une graine et d’un namespace stables ; l’ajout d’un autre générateur ne décale pas ses tirages.

### 53.2 Faire confiance à l’ordre du système de fichiers

**Symptôme :** Deux machines produisent des manifestes dans un ordre différent.

**Exemple fautif :**

> **[VSC] Contre-exemple — Ne pas saisir.**

```python
sources = tuple(root.rglob('*.json'))
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** L’ordre retourné par le parcours n’est pas un contrat portable et peut varier selon le système de fichiers.

**Exemple corrigé :**

> **[VSC] Correction — Ne pas saisir.**

```python
sources = tuple(sorted(root.rglob('*.json'), key=lambda p: p.relative_to(root).as_posix()))
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le tri sur le chemin relatif POSIX fixe l’ordre indépendamment de la plateforme.

### 53.3 Exécuter une commande avec shell=True

**Symptôme :** Un chemin contenant des caractères spéciaux modifie la commande réellement exécutée.

**Exemple fautif :**

> **[VSC] Contre-exemple — Ne pas saisir.**

```python
subprocess.run(f'godot --path {project} --script {script}', shell=True)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La chaîne est réinterprétée par un shell ; une valeur dynamique peut devenir une option ou une commande supplémentaire.

**Exemple corrigé :**

> **[VSC] Correction — Ne pas saisir.**

```python
subprocess.run(['godot', '--path', str(project), '--script', str(script)], shell=False, check=False)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Chaque argument est transmis séparément au processus sans interprétation intermédiaire du shell.

### 53.4 Écrire directement dans les sources publiées

**Symptôme :** Une campagne interrompue laisse un catalogue à moitié régénéré.

**Exemple fautif :**

> **[VSC] Contre-exemple — Ne pas saisir.**

```python
for item in generated:
    (published / item.name).write_bytes(item.payload)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les fichiers deviennent visibles avant validation globale et aucune porte ne distingue sortie partielle et lot accepté.

**Exemple corrigé :**

> **[VSC] Correction — Ne pas saisir.**

```python
write_to_staging(generated, staging)
records = validate_staging(staging)
promote_artifacts(records, staging, published)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le lot reste isolé jusqu’à la validation et la promotion ne copie que les artefacts déclarés et vérifiés.

### 53.5 Reprendre sur la seule présence d’un fichier

**Symptôme :** Une sortie ancienne est réutilisée après modification de la configuration.

**Exemple fautif :**

> **[VSC] Contre-exemple — Ne pas saisir.**

```python
if output.exists():
    return output
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** L’existence ne prouve ni que le plan est identique, ni que le fichier est complet, ni que ses octets correspondent au checkpoint.

**Exemple corrigé :**

> **[VSC] Correction — Ne pas saisir.**

```python
if checkpoint.plan_sha256 == plan_sha and sha256_file(output) == expected_sha:
    return output
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La reprise exige simultanément le même plan et la même empreinte d’artefact.

### 53.6 Utiliser hash() pour une graine persistante

**Symptôme :** Les données changent entre deux processus malgré les mêmes entrées.

**Exemple fautif :**

> **[VSC] Contre-exemple — Ne pas saisir.**

```python
seed = hash(source_key)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** `hash()` n’est pas une fonction d’empreinte de format et sa valeur n’est pas un contrat reproductible entre processus ou versions.

**Exemple corrigé :**

> **[VSC] Correction — Ne pas saisir.**

```python
seed = int.from_bytes(sha256(source_key.encode('utf-8')).digest()[:8], 'big')
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** SHA-256 produit les mêmes octets pour la même clé encodée et la conversion est définie explicitement.

### 53.7 Ajouter les résultats dans l’ordre de fin

**Symptôme :** Le manifeste varie selon la charge du processeur.

**Exemple fautif :**

> **[VSC] Contre-exemple — Ne pas saisir.**

```python
for future in as_completed(futures):
    records.append(future.result())
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** L’ordre de fin dépend de la vitesse relative des tâches et devient un détail non déterministe du manifeste.

**Exemple corrigé :**

> **[VSC] Correction — Ne pas saisir.**

```python
for future in as_completed(futures):
    records.append(future.result())
records.sort(key=lambda record: record.relative_path)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le parallélisme reste libre, mais la représentation finale est réordonnée par une clé canonique.

### 53.8 Retenter toutes les erreurs

**Symptôme :** Un schéma invalide est relancé plusieurs fois et masque la vraie cause.

**Exemple fautif :**

> **[VSC] Contre-exemple — Ne pas saisir.**

```python
for attempt in range(10):
    try:
        return run_job()
    except Exception:
        continue
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La boucle capture aussi les erreurs permanentes, perd leur code et peut répéter des effets de bord partiels.

**Exemple corrigé :**

> **[VSC] Correction — Ne pas saisir.**

```python
if policy.should_retry(attempt, result.error_code):
    cleanup_partial_output(item)
    continue
return result
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La politique autorise seulement des codes transitoires connus et nettoie la sortie partielle avant une nouvelle tentative bornée.

### 53.9 Considérer pip freeze comme un verrou résolu

**Symptôme :** La reconstruction de l’environnement dépend de l’état accidentel d’une machine.

**Exemple fautif :**

> **[PS] Contre-exemple — Ne pas saisir.**

```powershell
python -m pip freeze > requirements.txt
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** `pip freeze` décrit les paquets installés ; il ne calcule pas un verrou à partir des dépendances du projet et ne garantit pas un environnement portable.

**Exemple corrigé :**

> **[PS] Correction — Ne pas saisir.**

```powershell
python -m pip lock -e . -o pylock.windows.toml
python -m pip check
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le projet demande un verrou explicite puis vérifie la cohérence de l’environnement ; le caractère expérimental de `pip lock` reste documenté.

### 53.10 Donner au script une autorité métier

**Symptôme :** Un générateur modifie directement les soldes et valide lui-même l’opération.

**Exemple fautif :**

> **[VSC] Contre-exemple — Ne pas saisir.**

```python
wallet.balance += generated_reward
save_wallet(wallet)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le script contourne l’autorité économique, les écritures équilibrées, l’idempotence et le commit multi-autorités.

**Exemple corrigé :**

> **[VSC] Correction — Ne pas saisir.**

```python
command = RewardProposal(actor_id, amount_minor, provenance)
write_proposal(staging / 'reward-proposals.json', command)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Python produit une proposition typée et traçable ; le système économique reste seul responsable de sa validation et de son commit.

## 54. Checklist de revue

Avant d’accepter une automatisation Python :

- la version Python et les dépendances sont-elles explicites ;
- les configurations possèdent-elles une version et des limites ;
- les entrées sont-elles triées et validées ;
- les graines sont-elles locales et dérivées de façon stable ;
- les chemins sont-ils confinés à des racines autorisées ;
- les écritures passent-elles par un staging ;
- les codes de sortie distinguent-ils configuration, validation, exécution et intégrité ;
- le parallélisme est-il borné ;
- les résultats sont-ils réordonnés canoniquement ;
- les reprises vérifient-elles plan et empreintes ;
- les nouvelles tentatives sont-elles limitées aux erreurs transitoires ;
- chaque publication possède-t-elle manifeste, empreintes et provenance ;
- l’automatisation respecte-t-elle l’autorité des chapitres 26 à 28 ;
- les journaux et rapports évitent-ils secrets et données inutiles.

## 55. Décisions retenues pour Project Asteria

`Project Asteria` retient CPython `3.14.6` comme référence documentaire du chapitre et un paquet `asteria-tools` isolé du runtime Godot. L’environnement utilise `venv`, `pyproject.toml` et des verrous nommés par plateforme lorsque les résolutions diffèrent. `pip lock` reste signalé comme expérimental jusqu’à validation dans le Starter Kit.

Les CLI utilisent `argparse`, des codes de sortie stables et des chemins `Path` confinés. Les configurations TOML, instances JSON et manifestes déclarent une version. JSON Schema Draft 2020-12 vérifie les contrats externes, sans remplacer les validations métier.

Les générateurs sont purs autant que possible. Ils reçoivent leurs sources, versions et graines ; ils trient les entrées, utilisent des RNG locaux et produisent d’abord dans un staging. Les identités dérivées reposent sur un namespace versionné, jamais sur un nom affiché ou `hash()`.

L’orchestrateur lance les validateurs et Godot avec des listes d’arguments, `shell=False`, des délais bornés et des codes non nuls conservés. Le parallélisme est explicitement limité ; l’ordre de fin ne devient jamais l’ordre du manifeste.

La reprise exige un plan identique et des empreintes valides. Les nouvelles tentatives ne concernent que des erreurs transitoires cataloguées. Toute erreur de schéma, d’intégrité ou d’autorité bloque la promotion.

Chaque lot publiable possède un manifeste, des empreintes SHA-256, une provenance et un rapport. Une archive ZIP est décrite comme un conteneur compressé, jamais comme un chiffrement ou une signature. Python produit des propositions ou artefacts ; les systèmes Godot restent responsables des décisions et commits métier.

## 56. Références officielles

- Python `3.14.6`, notes de version et documentation de la bibliothèque standard ;
- documentation Python de `venv`, `argparse`, `tomllib`, `pathlib`, `subprocess`, `hashlib`, `random`, `concurrent.futures` et `zipfile` ;
- Python Packaging User Guide pour `pyproject.toml`, les environnements reproductibles et la spécification `pylock.toml` ;
- documentation `pip lock` et `pip check`, avec mention explicite du statut expérimental du verrouillage ;
- JSON Schema Draft 2020-12 et documentation officielle des mots-clés de validation.
