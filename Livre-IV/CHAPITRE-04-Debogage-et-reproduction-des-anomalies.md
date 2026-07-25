---
title: "Livre IV — Chapitre 4 : Débogage et reproduction des anomalies"
id: "DOC-L4-CH04"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 4
last-verified: "2026-07-26T00:30:21+02:00"
audit-status: "complete"
audit-date: "2026-07-26T00:30:21+02:00"
audit-report: "Livre-IV/QA/AUDIT-CHAPITRE-04.md"
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
  qualification-status: "inherited-provisional"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Débogage et reproduction des anomalies

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[VSC]** Visual Studio Code, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Rôle du chapitre

Une anomalie exploitable n’est pas une impression vague. Elle relie un comportement observé à un environnement, une version, un état initial, une séquence d’actions, un résultat attendu et des preuves consultables.

Ce chapitre organise la capture, la reproduction, la réduction et le triage des anomalies de `Project Asteria`. Il transforme un signal joueur, testeur ou outil en dossier diagnostique que deux personnes différentes peuvent comprendre et reproduire sans dépendre d’informations tacites.

Il ne redéfinit pas les campagnes du chapitre 3. Il ne définit pas non plus la collecte systématique des journaux, métriques et traces du chapitre 5. Il consomme seulement les preuves disponibles et précise comment les joindre à un rapport.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura :

- rédiger un rapport d’anomalie reproductible ;
- capturer build, plateforme, configuration et état initial ;
- séparer résultat attendu, résultat observé et interprétation ;
- produire une archive diagnostique minimale et expurgée ;
- mesurer la reproductibilité sans inventer de précision ;
- réduire un défaut à un scénario minimal ;
- distinguer gravité, fréquence, priorité et impact ;
- détecter et fusionner les doublons ;
- définir des conditions de réouverture ;
- organiser le triage en modes Solo et Studio ;
- préparer une reproduction indépendante humaine ou scriptée ;
- relier une correction à un test de non-régression du chapitre 3.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les modèles, commandes et scripts sont relus statiquement. Aucun défaut réel de `Project Asteria`, aucune archive diagnostique, aucun dump, aucune sauvegarde, aucune vidéo, aucune reproduction indépendante et aucune mesure runtime ne sont revendiqués comme produits.

> **[LECTURE] État de preuve du chapitre — Ne pas saisir.**

```yaml
evidence_level:
  chapter: static_review
  bug_report_materialized: false
  diagnostic_archive_created: false
  independent_reproduction_executed: false
  minimal_reproduction_executed: false
  runtime_measurements: none
  player_data_used: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** `static_review` décrit une revue documentaire, pas une exécution produit.
- **Séparation :** chaque artefact possède son propre indicateur de matérialisation.
- **Confidentialité :** `player_data_used: false` interdit d’inférer l’usage de données réelles.
- **Limite :** une future preuve devra citer l’environnement, le build, l’auteur et le résultat.

## 4. Prérequis et frontières

Le lecteur doit connaître :

- la stratégie QA et les portes du chapitre 2 ;
- les cas, fixtures, suites et statuts du chapitre 3 ;
- les concepts de journalisation et de reproductibilité du Livre II, chapitre 28 ;
- les versions et frontières d’autorité de `Project Asteria`.

Le présent chapitre possède :

- le modèle de rapport ;
- la procédure de reproduction ;
- l’archive diagnostique ;
- la réduction ;
- le triage ;
- les doublons ;
- les réouvertures.

Le chapitre 3 conserve les campagnes et tests de non-régression. Le chapitre 5 conservera la politique systématique de collecte, rotation, confidentialité et export des journaux.

> **Frontière essentielle :** ce chapitre explique comment transformer une anomalie observée en dossier reproductible. Il ne remplace ni la conception des tests ni l’observabilité continue.

## 5. Vocabulaire opérationnel

Une **anomalie** est un écart observé entre un comportement attendu et un comportement réel.

Un **défaut** est une cause confirmée dans un artefact : code, donnée, scène, configuration, asset ou procédure.

Un **symptôme** est ce qui devient visible : crash, blocage, valeur incorrecte, corruption, désynchronisation ou dégradation.

Une **reproduction** rejoue un scénario et retrouve le même symptôme selon des conditions déclarées.

Une **reproduction indépendante** est effectuée par une autre personne ou un script qui n’utilise pas d’informations tacites du rapporteur.

Une **réduction** retire des actions, données ou dépendances sans faire disparaître le symptôme.

Un **doublon** est un rapport rattaché à la même cause ou au même défaut canonique ; deux symptômes proches ne sont pas automatiquement des doublons.

Une **réouverture** remet un défaut vérifié dans un état actif lorsque le symptôme réapparaît ou que la correction ne couvre pas le périmètre déclaré.

## 6. Cycle de vie d’une anomalie

> **[LECTURE] Cycle de vie de référence — Ne pas saisir.**

```text
signal
  ↓
rapport initial
  ↓
qualification
  ↓
reproduction
  ↓
réduction
  ↓
diagnostic
  ↓
correction
  ↓
vérification
  ├── fermeture
  └── réouverture
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Signal :** une observation peut être incomplète sans être ignorée.
- **Qualification :** le triage décide si le dossier contient assez d’éléments.
- **Reproduction :** elle vérifie le symptôme avant d’attribuer une cause.
- **Réduction :** elle diminue le bruit sans réécrire l’histoire du défaut.
- **Fermeture :** elle intervient après vérification, pas au seul commit du correctif.

## 7. Identifiant stable du rapport

Chaque anomalie reçoit un identifiant indépendant du titre humain et de l’outil de suivi.

> **[VSC] Visual Studio Code — Créer `config/qa/defects/AST-DEFECT-000184.yaml`.**

```yaml
defect:
  id: AST-DEFECT-000184
  schema_version: 1
  status: reported
  canonical_issue: null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** l’identifiant reste stable même si le titre ou la priorité changent.
- **Schéma :** `schema_version` permet de faire évoluer le format.
- **Statut :** `reported` décrit l’entrée dans le cycle.
- **Doublons :** `canonical_issue` reste nul tant qu’aucun rattachement n’est confirmé.

## 8. Titre précis et observable

Le titre nomme le sous-système, l’action et le symptôme sans proposer prématurément une cause.

> **[VSC] Visual Studio Code — Compléter `config/qa/defects/AST-DEFECT-000184.yaml`.**

```yaml
summary:
  subsystem: save
  action: reload_slot
  symptom: inventory_missing_after_reload
  title: "Sauvegarde — l’inventaire disparaît après rechargement du slot 2"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Structure :** les trois champs rendent le titre recherchable.
- **Observation :** le symptôme est décrit sans affirmer que le sérialiseur est fautif.
- **Portée :** le slot concerné est nommé.
- **Recherche :** un titre stable facilite la détection de doublons.

## 9. Manifeste d’environnement

Une reproduction utile sépare système d’exploitation, moteur, rendu, architecture et langue.

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/environment.v1.json`.**

```json
{
  "os": "Windows 11",
  "architecture": "x86_64",
  "godot": "4.7.1-stable",
  "renderer": "Forward+",
  "locale": "fr-FR"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** chaque dimension peut expliquer un écart de comportement.
- **Version :** le moteur est épinglé au contrat du projet.
- **Locale :** elle peut modifier formatage, tri ou parsing.
- **Limite :** le bloc est un modèle et ne décrit pas une machine réellement inspectée.

## 10. Build et révision

Le rapport cite la révision source et l’identité du build, car deux exécutables proches peuvent contenir des contenus différents.

> **[VSC] Visual Studio Code — Ajouter `diagnostics/AST-DEFECT-000184/build.v1.yaml`.**

```yaml
build:
  build_id: AST-WIN-DEV-000731
  source_revision: "<git-commit>"
  content_manifest: "<sha256>"
  configuration: development
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Build :** `build_id` identifie l’exécutable testé.
- **Révision :** le commit relie le symptôme aux sources.
- **Contenu :** l’empreinte distingue les données et assets.
- **Configuration :** `development` évite de confondre un build de diagnostic avec une livraison.

## 11. Configuration active

Les drapeaux, options et mods actifs appartiennent au dossier lorsqu’ils peuvent modifier le comportement.

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/configuration.v1.yaml`.**

```yaml
configuration:
  difficulty: normal
  autosave: true
  language: fr-FR
  mods: []
  feature_flags:
    new_inventory_pipeline: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Options :** les valeurs visibles sont enregistrées.
- **Mods :** une liste vide vaut mieux qu’une omission ambiguë.
- **Feature flag :** le pipeline actif peut changer le chemin d’exécution.
- **Reproductibilité :** le second reproduisant peut reconstruire le même contexte.

## 12. État initial

Le scénario commence par un état observable et reconstructible, jamais par « utiliser ma sauvegarde habituelle ».

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/initial-state.v1.yaml`.**

```yaml
initial_state:
  fixture_id: AST-FIXTURE-PROFILE-001
  save_schema: 12
  scene: relay_hub
  player_inventory:
    iron_shard: 3
    field_ration: 1
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Fixture :** l’état se rattache à une donnée synthétique.
- **Schéma :** la version de sauvegarde est explicite.
- **Scène :** le point de départ spatial est nommé.
- **Inventaire :** les quantités attendues rendent le symptôme mesurable.

## 13. Étapes de reproduction

Chaque étape décrit une action unique, ordonnée et vérifiable.

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/reproduction.v1.yaml`.**

```yaml
steps:
  - id: 1
    action: launch_fixture
  - id: 2
    action: save_to_slot
    slot: 2
  - id: 3
    action: return_to_title
  - id: 4
    action: reload_slot
    slot: 2
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ordre :** les identifiants empêchent les inversions.
- **Atomicité :** une étape contient une action principale.
- **Paramètres :** le slot est répété aux points sensibles.
- **Scriptabilité :** les verbes peuvent être mappés vers un pilote automatisé.

## 14. Résultat attendu

L’attendu provient d’une exigence, d’un contrat ou d’un test, pas de l’intuition du rapporteur.

> **[VSC] Visual Studio Code — Ajouter `diagnostics/AST-DEFECT-000184/expected.v1.yaml`.**

```yaml
expected:
  source: AST-TC-SAVE-ROUNDTRIP-001
  invariant: inventory_roundtrip_equivalent
  iron_shard: 3
  field_ration: 1
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** le cas du chapitre 3 constitue l’oracle.
- **Invariant :** l’équivalence de round-trip est nommée.
- **Valeurs :** les quantités rendent la comparaison objective.
- **Frontière :** le présent chapitre consomme le test sans le redéfinir.

## 15. Résultat observé

L’observation décrit les faits, les valeurs et le moment où l’écart devient visible.

> **[VSC] Visual Studio Code — Ajouter `diagnostics/AST-DEFECT-000184/observed.v1.yaml`.**

```yaml
observed:
  after_step: 4
  inventory:
    iron_shard: 0
    field_ration: 0
  ui_message: null
  crash: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Moment :** `after_step` localise la première observation.
- **Valeurs :** les zéros montrent l’écart exact.
- **Absence :** `null` distingue l’absence de message d’un champ oublié.
- **Symptôme :** aucun crash n’est inventé.

## 16. Fréquence et tentatives

La fréquence est rapportée comme un couple succès/tentatives avec conditions, jamais comme un pourcentage isolé.

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/frequency.v1.yaml`.**

```yaml
reproduction_frequency:
  reproduced: 4
  attempts: 5
  environment_id: AST-WIN-DEV-000731
  seed_set: AST-SEEDS-SMOKE-001
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Numérateur :** `reproduced` compte les occurrences retrouvées.
- **Dénominateur :** `attempts` rend la proportion interprétable.
- **Environnement :** les essais restent rattachés au contexte.
- **Seeds :** les variations aléatoires sont contrôlées.

## 17. Gravité, priorité et impact

La gravité décrit l’effet ; la priorité décrit l’ordre de travail ; l’impact décrit les personnes ou données concernées.

> **[VSC] Visual Studio Code — Compléter `config/qa/defects/AST-DEFECT-000184.yaml`.**

```yaml
classification:
  severity: critical
  priority: P0
  impact:
    data_loss: true
    main_path_blocked: false
    workaround: none
  owner: save_system_owner
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Gravité :** la perte de données justifie `critical`.
- **Priorité :** `P0` est une décision de traitement, pas un synonyme de gravité.
- **Impact :** les dimensions sont explicites.
- **Propriété :** un responsable est nommé sans attribuer automatiquement la faute.

## 18. Archive diagnostique

L’archive réunit uniquement les artefacts nécessaires à la reproduction et au diagnostic.

> **[LECTURE] Arborescence d’une archive diagnostique — Ne pas saisir.**

```text
AST-DEFECT-000184/
├── manifest.json
├── environment.json
├── build.yaml
├── reproduction.yaml
├── expected.yaml
├── observed.yaml
├── logs/
│   └── relevant-window.log
└── evidence/
    └── inventory-after-reload.png
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racine :** l’identifiant du défaut nomme l’archive.
- **Manifeste :** il inventorie les fichiers et empreintes.
- **Fenêtre :** les journaux sont limités à la période pertinente.
- **Preuve :** la capture illustre le symptôme sans remplacer les données structurées.

## 19. Manifeste d’intégrité

Chaque fichier de l’archive reçoit une taille et une empreinte avant transmission.

> **[VSC] Visual Studio Code — Créer `tools/qa/build_diagnostic_manifest.py`.**

```python
from __future__ import annotations

import hashlib
import json
from pathlib import Path

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def build_manifest(root: Path) -> dict[str, object]:
    files = []
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        files.append({
            "path": path.relative_to(root).as_posix(),
            "size": path.stat().st_size,
            "sha256": digest(path),
        })
    return {"schema_version": 1, "files": files}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** `root` désigne une archive déjà préparée.
- **Parcours :** `rglob` collecte les fichiers sans suivre une liste implicite.
- **Déterminisme :** le tri stabilise l’ordre du manifeste.
- **Intégrité :** SHA-256 détecte une modification accidentelle ; il ne signe pas l’identité de l’auteur.

## 20. Expurgation des données

Avant partage, l’archive supprime secrets, chemins personnels, identifiants directs et textes libres non nécessaires.

> **[VSC] Visual Studio Code — Créer `config/qa/redaction.v1.yaml`.**

```yaml
redaction:
  remove:
    - access_tokens
    - email_addresses
    - home_directory
    - player_free_text
  replace:
    player_id: pseudonymous_case_id
  review_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Suppression :** les secrets et données directes ne quittent pas la machine.
- **Pseudonymisation :** un identifiant de cas remplace l’identité joueur.
- **Texte libre :** il est exclu par défaut car difficile à assainir.
- **Revue :** l’automatisation ne remplace pas une inspection humaine.

## 21. Fenêtre de journal pertinente

Le rapport joint un extrait borné autour du symptôme et conserve les horodatages et identifiants de corrélation disponibles.

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/log-window.v1.yaml`.**

```yaml
log_window:
  start: "2031-04-12T14:22:10Z"
  end: "2031-04-12T14:22:40Z"
  correlation_id: AST-SESSION-000731
  categories: [save, inventory]
  redacted: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Bornes :** la fenêtre évite d’exporter toute une session.
- **Corrélation :** l’identifiant relie plusieurs événements.
- **Catégories :** la sélection reste ciblée.
- **Frontière :** la politique générale de logs appartient au chapitre 5.

## 22. Sauvegarde synthétique de reproduction

Une sauvegarde jointe doit être synthétique, minimale, versionnée et dépourvue de données personnelles.

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/save-fixture.v1.yaml`.**

```yaml
save_fixture:
  fixture_id: AST-FIXTURE-DEFECT-000184
  schema_version: 12
  generated: true
  personal_data: false
  minimal_state: true
  sha256: "<sha256>"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Origine :** `generated: true` distingue la fixture d’une sauvegarde joueur.
- **Confidentialité :** `personal_data: false` est une condition d’acceptation.
- **Réduction :** `minimal_state` indique que les données non nécessaires ont été retirées.
- **Intégrité :** l’empreinte accompagne le fichier transmis.

## 23. Capture d’écran annotée

Une capture précise l’étape, la zone pertinente et l’absence éventuelle d’autres symptômes.

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/evidence/capture.v1.yaml`.**

```yaml
capture:
  file: inventory-after-reload.png
  after_step: 4
  focus: inventory_panel
  annotation: "Les deux compteurs sont à zéro."
  contains_personal_data: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contexte :** la capture est reliée à une étape.
- **Focus :** la zone observée est nommée.
- **Annotation :** le texte décrit le fait visible.
- **Confidentialité :** l’absence de données personnelles est explicitement vérifiée.

## 24. Vidéo de reproduction

Une vidéo complète les étapes lorsqu’un timing ou une interaction visuelle est difficile à décrire ; elle ne remplace pas le rapport structuré.

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/evidence/video.v1.yaml`.**

```yaml
video:
  file: reproduction.webm
  starts_before_step: 1
  ends_after_step: 4
  input_overlay: enabled
  audio: disabled
  redaction_review: complete
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Périmètre :** la vidéo couvre tout le scénario.
- **Entrées :** l’overlay rend les actions observables.
- **Audio :** il est désactivé pour éviter une collecte inutile.
- **Revue :** la vidéo est contrôlée avant partage.

## 25. Informations de crash

Lorsqu’un crash existe, le rapport conserve le code de sortie, le contexte et les symboles disponibles sans copier des secrets.

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/crash.v1.yaml`.**

```yaml
crash:
  occurred: false
  exit_code: null
  dump_file: null
  symbols_build_id: null
  sensitive_data_reviewed: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **État :** `occurred: false` évite de fabriquer un crash.
- **Nullabilité :** les champs restent présents mais non applicables.
- **Symboles :** un futur dump devra citer le build correspondant.
- **Confidentialité :** aucune revue n’est revendiquée lorsqu’aucun dump n’existe.

## 26. Première reproduction contrôlée

La première reproduction est enregistrée comme une exécution distincte avec résultat et réserves.

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/runs/first.v1.yaml`.**

```yaml
reproduction_run:
  run_id: AST-REPRO-000184-01
  executor: reporter
  environment_id: AST-WIN-DEV-000731
  result: NOT_EXECUTED
  evidence: []
  notes: "Modèle non exécuté."
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** chaque tentative possède un identifiant.
- **Exécuteur :** le rôle du rapporteur est enregistré.
- **Statut :** `NOT_EXECUTED` respecte le niveau de preuve du chapitre.
- **Preuves :** la liste vide évite de suggérer des artefacts inexistants.

## 27. Reproduction indépendante

La seconde reproduction doit utiliser le rapport et les artefacts, sans explication orale indispensable.

> **[VSC] Visual Studio Code — Créer `config/qa/reproduction-policy.v1.yaml`.**

```yaml
independent_reproduction:
  required_for:
    - critical_defect
    - intermittent_defect
    - release_blocker
  executor_must_differ: true
  hidden_context_prohibited: true
  result_values: [REPRODUCED, NOT_REPRODUCED, BLOCKED]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Portée :** les défauts à fort risque exigent une seconde lecture.
- **Indépendance :** l’exécuteur diffère du rapporteur initial.
- **Contexte :** les informations indispensables doivent être dans le dossier.
- **Résultats :** les trois statuts séparent absence de reproduction et impossibilité d’essayer.

## 28. Pilote scripté de reproduction

Un script peut rejouer des actions déterministes et produire un code de sortie sans décider de la cause.

> **[VSC] Visual Studio Code — Créer `tools/qa/reproduce_defect.py`.**

```python
from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum

class ExitCode(IntEnum):
    REPRODUCED = 0
    NOT_REPRODUCED = 1
    BLOCKED = 2

@dataclass(frozen=True)
class ReproductionResult:
    code: ExitCode
    observed_inventory_count: int
    evidence_path: str | None

def classify(observed_inventory_count: int) -> ReproductionResult:
    reproduced = observed_inventory_count == 0
    return ReproductionResult(
        code=ExitCode.REPRODUCED if reproduced else ExitCode.NOT_REPRODUCED,
        observed_inventory_count=observed_inventory_count,
        evidence_path=None,
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Codes :** les sorties distinguent reproduction, absence et blocage.
- **Immutabilité :** le résultat est figé après création.
- **Oracle :** le zéro représente le symptôme défini par le scénario.
- **Autorité :** le script classe une observation ; il ne localise pas la cause.

## 29. Commande bornée de reproduction

La commande reçoit un dossier de cas et écrit ses sorties dans un workspace déclaré.

> **[PS] PowerShell 7 — Lancer le pilote sur une fixture synthétique.**

```powershell
$Case = "diagnostics/AST-DEFECT-000184"
$Out = ".work/qa/reproduction/AST-DEFECT-000184"
New-Item -ItemType Directory -Force -Path $Out | Out-Null
python tools/qa/reproduce_defect.py --case $Case --output $Out
if ($LASTEXITCODE -notin 0,1,2) {
    throw "Code de sortie inattendu : $LASTEXITCODE"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** le cas et le workspace sont explicites.
- **Confinement :** les sorties restent sous `.work/qa/reproduction`.
- **Codes :** seuls les statuts documentés sont acceptés.
- **Limite :** la commande est un modèle ; aucun run n’est revendiqué.

## 30. Réduction par suppression d’étapes

La réduction teste si une sous-séquence conserve le symptôme, sans modifier les données historiques du rapport original.

> **[VSC] Visual Studio Code — Créer `tools/qa/reduce_steps.py`.**

```python
from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TypeVar

T = TypeVar("T")

def greedy_reduce(
    steps: Sequence[T],
    still_reproduces: Callable[[list[T]], bool],
) -> list[T]:
    current = list(steps)
    index = 0
    while index < len(current):
        candidate = current[:index] + current[index + 1:]
        if candidate and still_reproduces(candidate):
            current = candidate
        else:
            index += 1
    return current
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** la séquence et l’oracle sont injectés.
- **Méthode :** chaque étape est retirée puis testée.
- **Invariant :** la séquence vide n’est pas acceptée.
- **Limite :** l’algorithme produit un minimum local, pas la preuve d’un minimum global.

## 31. Journal de réduction

Chaque suppression tentée reste consultable afin de comprendre ce qui a été conservé ou rejeté.

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/reduction-log.v1.yaml`.**

```yaml
reduction:
  source_steps: [1, 2, 3, 4]
  attempts:
    - removed: 3
      reproduced: true
    - removed: 2
      reproduced: false
  retained_steps: [1, 2, 4]
  execution_status: NOT_EXECUTED
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** la séquence originale reste visible.
- **Tentatives :** chaque suppression indique son résultat attendu.
- **Résultat :** les étapes retenues forment le candidat minimal.
- **Preuve :** `NOT_EXECUTED` interdit de présenter l’exemple comme une réduction réelle.

## 32. Réduction de l’état

Les données sont réduites séparément des actions pour éviter de confondre deux variables.

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/state-reduction.v1.yaml`.**

```yaml
state_reduction:
  original_entities: 14
  retained_entities:
    - player
    - inventory
    - save_slot
  removed_domains:
    - quests
    - factions
    - weather
  result: NOT_EXECUTED
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** l’état est réduit après stabilisation des étapes.
- **Entités :** le noyau nécessaire est déclaré.
- **Domaines :** les suppressions candidates sont visibles.
- **Statut :** aucun résultat réel n’est inventé.

## 33. Réduction des entrées

Les entrées analogiques, séquences clavier ou données réseau sont normalisées avant comparaison.

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/input-reduction.v1.yaml`.**

```yaml
input_reduction:
  original_events: 37
  normalized_events: 6
  retained:
    - open_pause
    - select_save
    - confirm_slot_2
    - return_title
    - select_load
    - confirm_slot_2
  timing_contract: event_order_only
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Normalisation :** les événements redondants sont retirés.
- **Liste :** la séquence restante est lisible.
- **Timing :** seul l’ordre est requis dans ce contrat.
- **Frontière :** un défaut dépendant du temps devrait conserver des bornes explicites.

## 34. Temps, horloge et aléatoire

Une reproduction signale les sources non déterministes et les valeurs injectées.

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/determinism.v1.yaml`.**

```yaml
determinism:
  clock:
    mode: fixed
    value: "2031-04-12T14:22:00Z"
  rng:
    seed: 104729
  network:
    mode: disabled
  background_jobs:
    mode: drained_before_step_1
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Horloge :** la date fixe évite les branches temporelles.
- **Aléatoire :** la seed rend la tentative rejouable.
- **Réseau :** il est désactivé pour ce scénario local.
- **Tâches :** l’état asynchrone est stabilisé avant l’action.

## 35. Signature de doublon

Une signature combine sous-système, symptôme normalisé, version et point de rupture ; elle sert à chercher, pas à fusionner automatiquement.

> **[VSC] Visual Studio Code — Créer `tools/qa/duplicate_signature.py`.**

```python
from __future__ import annotations

import hashlib
import json

def signature(
    subsystem: str,
    normalized_symptom: str,
    save_schema: int,
    break_step: int,
) -> str:
    payload = {
        "subsystem": subsystem,
        "symptom": normalized_symptom,
        "save_schema": save_schema,
        "break_step": break_step,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** quatre dimensions stables décrivent le symptôme.
- **Canonisation :** le JSON trié produit une représentation déterministe.
- **Empreinte :** SHA-256 facilite la recherche exacte.
- **Décision :** une signature identique reste un indice, pas une preuve de cause commune.

## 36. Rattachement à un défaut canonique

Le rapport secondaire conserve son auteur et ses preuves même lorsqu’il devient doublon.

> **[VSC] Visual Studio Code — Compléter `config/qa/defects/AST-DEFECT-000219.yaml`.**

```yaml
duplicate:
  report_id: AST-DEFECT-000219
  canonical_id: AST-DEFECT-000184
  relation: same_confirmed_cause
  evidence_preserved: true
  decision_owner: qa_triage_owner
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Traçabilité :** les deux identifiants restent consultables.
- **Relation :** la cause commune est explicitement confirmée.
- **Preuves :** les environnements supplémentaires ne sont pas supprimés.
- **Autorité :** le triage, pas l’algorithme, décide du rattachement.

## 37. Conditions de réouverture

Une fermeture définit les événements qui justifient une réouverture sans débat improvisé.

> **[VSC] Visual Studio Code — Créer `config/qa/reopen-policy.v1.yaml`.**

```yaml
reopen_policy:
  reopen_when:
    - symptom_reappears_in_supported_build
    - verification_was_incomplete
    - fix_scope_excludes_reproduced_environment
    - regression_test_fails
  do_not_reopen_for:
    - unrelated_symptom
    - unsupported_environment_without_new_risk
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Réapparition :** le même symptôme dans un build pris en charge suffit.
- **Vérification :** une preuve incomplète peut être corrigée.
- **Portée :** un environnement exclu doit être explicitement comparé.
- **Séparation :** un symptôme sans relation ouvre un nouveau rapport.

## 38. Lien avec la non-régression

Après confirmation, le défaut cite le cas qui échoue avant correction et réussit après correction.

> **[VSC] Visual Studio Code — Compléter `config/qa/defects/AST-DEFECT-000184.yaml`.**

```yaml
regression_contract:
  defect_id: AST-DEFECT-000184
  test_case_id: AST-TC-SAVE-ROUNDTRIP-001
  fails_before_fix: required
  passes_after_fix: required
  suite: smoke
  verification_status: NOT_EXECUTED
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Lien :** le défaut et le cas restent bidirectionnels.
- **Avant :** l’échec prouve que le test détecte le symptôme.
- **Après :** le passage vérifie la correction.
- **Statut :** la preuve runtime reste ouverte.

## 39. Politique de triage

Le triage vérifie la qualité du dossier, le risque et l’autorité de décision sans confondre priorité et culpabilité.

> **[VSC] Visual Studio Code — Créer `config/qa/triage-policy.v1.yaml`.**

```yaml
triage:
  required_fields:
    - environment
    - build
    - steps
    - expected
    - observed
  decisions:
    - ACCEPT_FOR_REPRODUCTION
    - REQUEST_INFORMATION
    - LINK_DUPLICATE
    - REJECT_OUT_OF_SCOPE
  critical_escalation: immediate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Complétude :** les cinq champs rendent une tentative possible.
- **Décisions :** le triage distingue manque d’information, doublon et hors-périmètre.
- **Escalade :** un défaut critique n’attend pas la réunion suivante.
- **Frontière :** la priorité reste décidée selon la stratégie QA.

## 40. Sévérité et fréquence sans score magique

La matrice garde les dimensions séparées et impose une justification humaine.

> **[LECTURE] Matrice de triage — Ne pas saisir.**

```yaml
triage_matrix:
  - severity: critical
    frequency: any
    action: escalate
  - severity: major
    frequency: frequent
    action: prioritize
  - severity: minor
    frequency: rare
    action: schedule
  decision_requires_context: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dimensions :** gravité et fréquence restent distinctes.
- **Action :** la matrice propose une réaction initiale.
- **Contexte :** la dernière ligne interdit une décision mécanique.
- **Limite :** la priorité réelle dépend aussi du contournement et du périmètre.

## 41. Propriété et escalade

Le rapport distingue rapporteur, reproduisant, propriétaire du sous-système et décideur de priorité.

> **[VSC] Visual Studio Code — Créer `config/qa/defect-roles.v1.yaml`.**

```yaml
roles:
  reporter: records_observation
  reproducer: verifies_scenario
  subsystem_owner: investigates_cause
  qa_triage_owner: manages_workflow
  product_owner: decides_priority
  security_owner: handles_security_exception
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rapporteur :** il décrit ce qui a été vu.
- **Reproduisant :** il contrôle l’indépendance.
- **Propriétaire :** il enquête sans être présumé responsable du défaut.
- **Décision :** la priorité appartient au produit, avec escalade spécialisée si nécessaire.

## 42. Mode Solo

Une personne seule sépare les rôles dans le temps et conserve des preuves pour limiter l’auto-confirmation.

> **[LECTURE] Séparation temporelle en mode Solo — Ne pas saisir.**

```yaml
solo_workflow:
  report_phase: capture_without_diagnosis
  pause_before_reproduction: required
  reproduction_phase: follow_written_steps_only
  reduction_phase: preserve_original_report
  closure_phase: require_regression_evidence
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Capture :** le premier rapport évite d’inventer une cause.
- **Pause :** une séparation temporelle réduit le biais de mémoire.
- **Reproduction :** les étapes écrites sont suivies comme par une autre personne.
- **Fermeture :** un test de non-régression protège la décision.

## 43. Mode Studio

Une équipe attribue les responsabilités sans perdre l’historique du rapport.

> **[LECTURE] Responsabilités en mode Studio — Ne pas saisir.**

```yaml
studio_workflow:
  reporter: qa_analyst
  independent_reproducer: qa_peer
  triage_owner: qa_lead
  subsystem_owner: save_team
  priority_owner: product_owner
  closure_verifier: qa_peer
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Indépendance :** le reproduisant diffère du rapporteur.
- **Triage :** un propriétaire coordonne les statuts.
- **Investigation :** l’équipe sauvegarde reçoit le dossier qualifié.
- **Fermeture :** la vérification revient à un pair QA.

## 44. Rapport de synthèse

Le rapport de triage conserve faits, décisions, preuves et réserves dans des champs séparés.

> **[VSC] Visual Studio Code — Créer `diagnostics/AST-DEFECT-000184/report.v1.yaml`.**

```yaml
report:
  defect_id: AST-DEFECT-000184
  status: READY_FOR_REPRODUCTION
  facts:
    reproduced: 0
    attempts: 0
  decision:
    priority: P0
    owner: product_owner
  evidence: []
  reservations:
    - runtime_reproduction_pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Faits :** les compteurs à zéro reflètent l’absence d’exécution.
- **Décision :** la priorité et son propriétaire sont séparés.
- **Preuves :** aucun artefact inexistant n’est listé.
- **Réserves :** le travail runtime restant est explicite.

## 45. Checklist de production et d’acceptation

- [ ] identifiant stable attribué ;
- [ ] titre observable et recherchable ;
- [ ] build, révision, plateforme et configuration capturés ;
- [ ] état initial reconstructible ;
- [ ] étapes atomiques et ordonnées ;
- [ ] attendu sourcé ;
- [ ] observé factuel ;
- [ ] fréquence accompagnée de son nombre de tentatives ;
- [ ] gravité, priorité et impact séparés ;
- [ ] archive minimale et manifestée ;
- [ ] données sensibles expurgées ;
- [ ] journaux bornés à la fenêtre pertinente ;
- [ ] fixture synthétique utilisée par défaut ;
- [ ] reproduction indépendante préparée ;
- [ ] original préservé pendant la réduction ;
- [ ] doublon décidé par une autorité humaine ;
- [ ] conditions de réouverture définies ;
- [ ] lien de non-régression préparé ;
- [ ] réserves runtime visibles ;
- [ ] aucune instruction de pilotage éditorial dans le texte lecteur.

## 46. Diagnostics : erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

Les dix cas suivants montrent des rapports qui semblent plausibles mais détruisent la reproductibilité ou la traçabilité.

### 46.1 Écrire « ça ne marche pas »

**Symptôme ou risque :** Le rapport ne permet ni de localiser l’action ni de comparer attendu et observé.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
title: "La sauvegarde ne marche pas"
steps: "Jouer puis charger."
observed: "Bug."
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le titre, les étapes et l’observation sont trop vagues. Aucun second lecteur ne peut reconstruire l’état ou savoir quel symptôme chercher.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
title: "Sauvegarde — inventaire vide après rechargement du slot 2"
steps: [launch_fixture, save_slot_2, return_title, reload_slot_2]
expected: {iron_shard: 3}
observed: {iron_shard: 0}
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction nomme le sous-système, l’action, le slot et la différence mesurable.

### 46.2 Confondre hypothèse et fait

**Symptôme ou risque :** Le rapport accuse un composant avant toute investigation.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
observed: "Le sérialiseur InventoryCodec supprime les objets."
root_cause: confirmed
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le sérialiseur est présenté comme cause confirmée alors que seul le symptôme est connu.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
observed: "Après l’étape 4, les deux quantités d’inventaire valent zéro."
hypotheses:
  - inventory_deserialization
  - fixture_mismatch
root_cause: unknown
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction sépare le fait observable des hypothèses et conserve la cause à `unknown`.

### 46.3 Omettre le build

**Symptôme ou risque :** Le défaut peut être recherché dans des sources qui ne correspondent pas à l’exécutable.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
environment:
  os: Windows 11
build: "la dernière version"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** « La dernière version » change avec le temps et ne relie pas l’anomalie à une révision précise.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
environment:
  os: Windows 11
build_id: AST-WIN-DEV-000731
source_revision: "<git-commit>"
content_manifest: "<sha256>"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction identifie le build, les sources et le contenu chargés.

### 46.4 Utiliser une sauvegarde joueur brute

**Symptôme ou risque :** Le dossier expose des données inutiles et reste difficile à réduire.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
attachment:
  file: "save-laurent-complete.zip"
  personal_data_reviewed: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La sauvegarde réelle peut contenir identité, texte libre, historique et secrets de services.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
attachment:
  fixture_id: AST-FIXTURE-DEFECT-000184
  generated: true
  personal_data: false
  minimal_state: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction utilise une fixture synthétique et minimale.

### 46.5 Publier un taux sans tentatives

**Symptôme ou risque :** La fréquence paraît précise mais ne peut pas être évaluée.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
frequency: "80 %"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le pourcentage ne dit ni combien d’essais ont été conduits ni dans quel environnement.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
reproduction_frequency:
  reproduced: 4
  attempts: 5
  environment_id: AST-WIN-DEV-000731
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve numérateur, dénominateur et environnement.

### 46.6 Réduire en écrasant le rapport original

**Symptôme ou risque :** Les étapes historiques disparaissent et la comparaison devient impossible.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
reproduction_steps: [1, 2, 4]
original_steps_preserved: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le rapport ne permet plus de savoir ce qui a été supprimé ni pourquoi.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
original_steps: [1, 2, 3, 4]
reduced_candidate: [1, 2, 4]
reduction_log: reduction-log.v1.yaml
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction conserve la source, le candidat et le journal de réduction.

### 46.7 Fusionner des doublons sur le titre

**Symptôme ou risque :** Deux symptômes proches peuvent avoir des causes, versions ou environnements différents.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
duplicate_detection:
  rule: same_title
  action: auto_close
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le titre est une formulation humaine instable et ne démontre pas une cause commune.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
duplicate_detection:
  signals: [signature, break_step, build_range, confirmed_cause]
  action: propose_link
  decision_owner: qa_triage_owner
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction agrège plusieurs indices et réserve la décision au triage.

### 46.8 Fermer au commit du correctif

**Symptôme ou risque :** Une modification de code n’atteste pas que le symptôme a disparu.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
status: closed
reason: "Correctif committé."
verification_run: null
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le rapport ne cite ni reproduction après correction ni test de non-régression.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
status: ready_for_verification
fix_revision: "<git-commit>"
verification_case: AST-TC-SAVE-ROUNDTRIP-001
verification_run: NOT_EXECUTED
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction place le défaut avant vérification et rend la preuve manquante explicite.

### 46.9 Interpréter NOT_REPRODUCED comme inexistant

**Symptôme ou risque :** Une tentative négative peut venir d’un environnement différent ou d’un défaut intermittent.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
result: NOT_REPRODUCED
decision: REJECT_DEFECT
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** L’absence de reproduction lors d’un essai ne réfute pas automatiquement l’observation initiale.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
result: NOT_REPRODUCED
next_actions:
  - compare_environment
  - verify_build
  - increase_controlled_attempts
decision: HOLD
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction maintient le dossier en attente et cherche les variables divergentes.

### 46.10 Exporter tous les journaux

**Symptôme ou risque :** Le dossier devient volumineux, bruité et potentiellement sensible.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
logs:
  scope: entire_user_session
  redaction: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** L’export global collecte des événements sans lien avec le symptôme et peut exposer des données personnelles.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
logs:
  start: "2031-04-12T14:22:10Z"
  end: "2031-04-12T14:22:40Z"
  categories: [save, inventory]
  redacted: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La correction borne la fenêtre, filtre les catégories et impose l’expurgation.

## 47. Critère d’acceptation du protocole

Le protocole de `Project Asteria` pourra être déclaré matérialisé lorsque :

- le modèle de rapport existe dans le projet ;
- une fixture synthétique permet de reconstruire l’état initial ;
- le manifeste d’environnement et de build est produit ;
- l’archive diagnostique passe une revue de confidentialité ;
- une seconde personne ou un script reproduit indépendamment le symptôme ;
- la réduction conserve l’original et son journal ;
- le triage attribue propriétaire, gravité et priorité ;
- le défaut est relié à un cas de non-régression ;
- les conditions de fermeture et de réouverture sont vérifiables.

Le présent chapitre ne revendique aucune de ces matérialisations ni exécutions.

## 48. Références techniques officielles

- [Godot 4.7 — Présentation des outils de débogage](https://docs.godotengine.org/en/4.7/tutorials/scripting/debug/overview_of_debugging_tools.html)
- [Godot 4.7 — Utilisation en ligne de commande](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html)
- [Godot 4.7 — Classe `OS`](https://docs.godotengine.org/en/4.7/classes/class_os.html)
- [Python 3.14 — `hashlib`](https://docs.python.org/3.14/library/hashlib.html)
- [Python 3.14 — `json`](https://docs.python.org/3.14/library/json.html)
- [Python 3.14 — `pathlib`](https://docs.python.org/3.14/library/pathlib.html)
- [GitHub Docs — Syntaxe des formulaires d’issue](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)
- [Livre II — Chapitre 28 : Journalisation, diagnostic et reproductibilité](../Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md)
- [Livre IV — Chapitre 2 : Stratégie générale d’assurance qualité](CHAPITRE-02-Strategie-generale-d-assurance-qualite.md)
- [Livre IV — Chapitre 3 : Tests fonctionnels et tests de régression](CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md)

## 49. Synthèse opérationnelle pour Project Asteria

`Project Asteria` retient les décisions suivantes :

- chaque anomalie possède un identifiant stable ;
- un titre décrit sous-système, action et symptôme sans attribuer une cause ;
- build, révision, contenu, plateforme et configuration sont capturés ;
- l’état initial utilise une fixture synthétique et versionnée ;
- les étapes sont atomiques, ordonnées et scriptables ;
- attendu et observé restent séparés ;
- la fréquence conserve le nombre de reproductions et de tentatives ;
- gravité, priorité et impact restent des dimensions distinctes ;
- l’archive diagnostique est minimale, manifestée et expurgée ;
- une fenêtre de journaux ciblée est préférée à un export global ;
- une reproduction indépendante est exigée pour les risques élevés ;
- le rapport original est conservé pendant toute réduction ;
- une réduction gloutonne est reconnue comme minimum local seulement ;
- une signature de doublon propose une recherche sans fermer automatiquement ;
- les preuves des rapports doublons restent consultables ;
- la fermeture exige une vérification et un test de non-régression ;
- `NOT_REPRODUCED` ne signifie pas « défaut inexistant » ;
- les conditions de réouverture sont écrites avant fermeture ;
- les modes Solo et Studio conservent une séparation des rôles adaptée ;
- aucune exécution runtime n’est revendiquée sans preuve conservée.

> **[LECTURE] Décisions du protocole de débogage — Ne pas saisir.**

```yaml
asteria_defect_protocol:
  schema_version: 1
  stable_defect_id: required
  environment_manifest: required
  build_identity: required
  synthetic_fixture_default: true
  expected_observed_separated: true
  attempts_denominator_required: true
  diagnostic_archive_manifested: true
  redaction_review_required: true
  independent_reproduction_for_critical: true
  original_report_preserved_during_reduction: true
  automatic_duplicate_closure: prohibited
  verification_before_closure: required
  regression_case_link: required
  runtime_materialization_status: not_started
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le défaut, le build et l’environnement restent reliés.
- **Confidentialité :** fixtures synthétiques et revue d’expurgation sont obligatoires.
- **Indépendance :** les défauts critiques reçoivent une seconde reproduction.
- **Autorité :** aucun algorithme ne ferme seul un doublon.
- **Preuve :** `not_started` interdit toute revendication d’exécution.
