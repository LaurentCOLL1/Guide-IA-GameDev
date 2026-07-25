---
title: "Livre III — Chapitre 30 : Automatisation Blender, ComfyUI et production en lots"
id: "DOC-L3-CH30"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 30
last-verified: "2026-07-25T09:40:18+02:00"
audit-status: "complete"
audit-date: "2026-07-25T09:40:18+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-30.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
reference-tools:
  blender:
    version: "5.2.0"
    qualification: "inherited-documentation-review"
  comfyui:
    version: "0.28.0"
    qualification: "inherited-documentation-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Automatisation Blender, ComfyUI et production en lots

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH30`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Versions de référence héritées :** Blender `5.2.0`, ComfyUI `0.28.0`, Godot `4.7.1-stable`, CPython selon la matrice qualifiée du Livre II
## 1. Rôle du chapitre

Ce dernier chapitre du Livre III transforme les contrats de production en une chaîne de lots observable. Il coordonne des scripts Blender, des workflows ComfyUI, des imports Godot et la porte qualité du chapitre 29 sans absorber l’autorité de ces outils.

L’automatisation réduit les gestes répétitifs, mais elle ne transforme ni une sortie générative en concept retenu, ni un export valide en asset accepté. Elle prépare des preuves, applique des refus mesurables et place chaque décision artistique devant une personne identifiée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
chapter_role:
  input: immutable_batch_plan
  orchestration: bounded_and_resumable
  blender: parameterized_background_jobs
  comfyui: queued_workflows_with_run_manifests
  godot: import_and_technical_gate
  human_authority: artistic_selection_and_release
  gameplay_authority: none
  runtime_claims: none
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** le lot part d’un plan figé, versionné et associé à une empreinte.
- **Outils :** Blender, ComfyUI et Godot restent propriétaires de leurs contrats techniques.
- **Orchestration :** la chaîne borne la concurrence, les tentatives, les délais et le stockage.
- **Autorité humaine :** sélection, dérogation et acceptation artistique ne sont jamais déduites d’un code de sortie.
- **Limite :** aucun job de production ne modifie un état gameplay.

## 2. Résultats d’apprentissage

Le lecteur saura identifier les tâches réellement automatisables, construire un manifeste de lot, modéliser un graphe de dépendances et exécuter des jobs isolés avec reprise vérifiée.

Il saura également intégrer une file ComfyUI, paramétrer Blender en arrière-plan, consolider les artefacts dans une CI et organiser un échantillonnage humain qui ne confond pas débit de production et qualité.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
learning_outcomes:
  plan:
    - classify_tasks
    - freeze_inputs
    - build_dependency_graph
  execute:
    - blender_background_job
    - comfyui_queue_job
    - godot_validation_job
  control:
    - bounded_concurrency
    - retry_policy
    - verified_checkpoint
    - staging_promotion
  review:
    - representative_sampling
    - human_comparison
    - independent_approval
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Planification :** les tâches sont classées avant leur passage en file.
- **Exécution :** chaque adaptateur reçoit un contrat fermé et retourne un résultat structuré.
- **Contrôle :** reprise, concurrence et promotion reposent sur des preuves d’intégrité.
- **Revue :** les échantillons sont choisis selon une règle documentée, puis évalués humainement.
- **Résultat attendu :** un autre opérateur peut relancer le même lot et comprendre chaque décision.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les scripts, manifestes, workflows et fichiers CI sont des modèles pédagogiques ; ils ne prouvent pas qu’un lot réel a été exécuté.

Aucun temps Blender, débit ComfyUI, consommation GPU, coût de stockage, taux d’échec ou gain de productivité n’est inventé. Ces valeurs doivent provenir d’une campagne matérialisée sur les profils cibles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
evidence_level:
  chapter: static_review
  batch_pilot_materialized: false
  blender_scripts_executed: false
  comfyui_queue_executed: false
  godot_batch_import_executed: false
  retry_recovery_demonstrated: false
  ci_pipeline_executed: false
  human_sampling_performed: false
  livre_iii_pdf_produced: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** la méthode est relue sans devenir une preuve d’exécution.
- **Outils :** aucun script Blender ou appel ComfyUI n’est déclaré lancé.
- **Reprise :** aucun incident réel n’est présenté comme démonstration de checkpoint.
- **Revue :** aucun échantillon ni lot de Project Asteria n’est déclaré approuvé.
- **Publication :** le PDF de fin de Livre reste une opération séparée après clôture documentaire.

## 4. Frontières avec les chapitres voisins

Le chapitre 3 conserve les questions visuelles, workflows, modèles, custom nodes, seeds et décisions de concept. Le chapitre 4 conserve les sources Blender, collections d’export et conventions de fichiers. Le chapitre 28 conserve les profils d’import et le chapitre 29 la décision finale d’asset.

Le Livre II, chapitre 29 fournit les primitives Python de planification, empreinte, concurrence, checkpoint, staging et publication. Le présent chapitre les spécialise pour la production artistique en lots.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ownership:
  livre_iii_ch03: comfyui_workflow_and_concept_decisions
  livre_iii_ch04: blender_sources_and_export_contracts
  livre_iii_ch28: godot_import_and_reimport_contracts
  livre_iii_ch29: individual_asset_quality_gate
  livre_iii_ch30: batch_orchestration_and_ci
  livre_ii_ch29: generic_python_automation_primitives
  invariant: orchestration_never_overrides_owner_decisions
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Amont :** les chapitres propriétaires définissent les entrées et leurs règles.
- **Spécialisation :** le chapitre 30 assemble les contrats sans les recopier.
- **Porte qualité :** un lot terminé n’est pas synonyme d’assets acceptés.
- **Python :** les primitives génériques sont réutilisées plutôt que réinventées.
- **Invariant :** l’orchestrateur conserve les codes de décision de chaque propriétaire.

## 5. Pilote de lot de Project Asteria

Le pilote `AST-PRODUCTION-BATCH-SCOUT-RELAY-001` réunit l’éclaireur et le module de relais déjà utilisés aux chapitres 28 et 29. Il ajoute un petit ensemble ComfyUI destiné à explorer des marquages du relais, sans promouvoir automatiquement les images produites.

Le lot reste volontairement réduit : deux exports Blender, une famille de propositions ComfyUI, une importation Godot et deux passages par la porte qualité. Cette taille permet d’expliquer la reprise sans masquer les relations.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asteria_batch_pilot:
  id: AST-PRODUCTION-BATCH-SCOUT-RELAY-001
  revision: 0.1.0-draft
  blender_candidates:
    - AST-CHAR-SCOUT-001
    - AST-PROP-RELAY-MODULE-001
  comfyui_experiment: AST-EXP-RELAY-MARKINGS-001
  import_dependency: AST-IMPORT-PILOT-SCOUT-RELAY-001
  quality_gate: AST-ASSET-GATE-SCOUT-RELAY-001
  materialization_status: not_started
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le pilote possède un identifiant distinct des assets individuels.
- **Blender :** chaque candidat conserve sa source et son profil d’export.
- **ComfyUI :** l’expérience produit des propositions en quarantaine.
- **Godot :** les résultats techniques passent par les contrats déjà documentés.
- **Réserve :** aucun lot, asset ou concept n’est déclaré exécuté ou accepté.

## 6. Modèle mental d’un lot

Un lot n’est pas un dossier de fichiers à traiter dans l’ordre où ils apparaissent. Il s’agit d’un plan immuable composé de tâches identifiées, de dépendances, de ressources, de préconditions et de résultats attendus.

La vitesse d’exécution peut varier sans changer le manifeste final. En revanche, une modification d’entrée, de version d’outil ou de configuration crée une nouvelle révision du plan.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
batch_model:
  plan: immutable
  tasks: identified_and_versioned
  dependencies: explicit_dag
  resources: declared
  execution_order: derived
  outputs: staged_and_hashed
  decisions: separated_from_execution
  resume: allowed_only_with_matching_plan_hash
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Plan :** la révision du lot fixe les entrées et paramètres.
- **Graphe :** l’ordre provient des dépendances, pas de la découverte du système de fichiers.
- **Ressources :** CPU, GPU, mémoire et accès exclusifs sont déclarés.
- **Sorties :** les artefacts restent en staging avant promotion.
- **Reprise :** un checkpoint d’un autre plan est rejeté.

## 7. Choisir les tâches réellement automatisables

Une tâche est automatisable lorsqu’elle possède des entrées structurées, un résultat vérifiable et un échec observable. Renommer selon une convention, exporter une collection, soumettre un workflow ou calculer une empreinte répond à ce contrat.

La qualité d’une silhouette, l’adéquation culturelle ou la préférence entre deux concepts ne deviennent pas automatiques parce qu’un formulaire peut enregistrer une note.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
automation_candidate:
  task: export_named_collection
  inputs:
    source_blend: art/blender/sources/props/relay.blend
    collection: AST_PROP_RELAY__EXPORT
    profile: AST-BLENDER-EXPORT-STATIC-001
  measurable_output:
    path: staging/relay.glb
    sha256_required: true
  human_judgment_required: false
  safe_to_retry: conditional
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Tâche :** l’action est limitée à une collection explicitement nommée.
- **Entrées :** source et profil sont déclarés avant l’exécution.
- **Sortie :** le chemin et l’empreinte rendent le résultat contrôlable.
- **Jugement :** aucune décision artistique n’est cachée dans le job.
- **Retry :** la relance dépend de l’idempotence et de l’état du staging.

## 8. Classer les tâches déterministes, génératives et humaines

Trois classes évitent d’appliquer une même promesse de reproductibilité à tous les outils. Une transformation déterministe vise une équivalence canonique ; une génération contrôlée vise une famille documentée ; une décision humaine produit une approbation signée.

Le classement influence les comparaisons, les checkpoints et les critères de reprise.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
task_classes:
  deterministic_transform:
    examples: [hash_manifest, validate_schema, copy_artifact]
    expected_equivalence: canonical
  controlled_generation:
    examples: [comfyui_sampling, procedural_variation]
    expected_equivalence: family_unless_proven_exact
  human_decision:
    examples: [art_selection, waiver_approval, final_release]
    expected_equivalence: not_applicable
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterministe :** la comparaison porte sur des octets ou une forme canonique.
- **Génératif :** la seed seule ne suffit pas à promettre une identité binaire.
- **Humain :** l’issue possède un auteur, une date et des références.
- **Checkpoint :** chaque classe définit ce qui peut être réutilisé.
- **Limite :** un score automatique ne change pas la classe d’une décision artistique.

## 9. Figer l’identité du lot et son plan

L’identité fonctionnelle du lot ne dépend pas de son heure de lancement. Elle combine un identifiant stable, une révision, la révision source et l’empreinte canonique du plan.

Relancer la même révision avec les mêmes entrées crée une nouvelle exécution, pas un nouveau lot.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class BatchIdentity:
    batch_id: str
    revision: str
    source_revision: str
    plan_sha256: str

@dataclass(frozen=True, slots=True)
class BatchRunIdentity:
    batch: BatchIdentity
    run_id: str
    attempt: int
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classes :** `BatchIdentity` décrit le plan ; `BatchRunIdentity` décrit une exécution.
- **Immutabilité :** `frozen=True` interdit les modifications accidentelles après construction.
- **Types :** les révisions et empreintes restent des chaînes canoniques.
- **Tentative :** `attempt` distingue les reprises d’un même run logique.
- **Invariant :** l’horodatage peut documenter l’exécution, mais ne définit pas l’identité du plan.

## 10. Organiser l’arborescence de production en lots

L’arborescence sépare les sources, la configuration versionnée, le travail jetable, les artefacts de preuve et les publications. Aucun adaptateur n’écrit directement dans les sources canoniques.

Les répertoires de runs sont isolés afin qu’un échec ne contamine pas une campagne suivante.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```text
automation/art-batches/
├── schemas/
├── profiles/
├── plans/
├── src/asteria_art_batches/
├── workflows/
│   ├── blender/
│   └── comfyui/
├── work/
│   ├── runs/<run_id>/staging/
│   ├── runs/<run_id>/checkpoints/
│   └── runs/<run_id>/logs/
├── artifacts/<run_id>/
└── published/
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Configuration :** schémas, profils et plans sont versionnés.
- **Adaptateurs :** les scripts Blender et ComfyUI restent séparés du cœur d’orchestration.
- **Runs :** chaque exécution possède son propre staging, checkpoint et journal.
- **Artefacts :** les preuves CI sont distinctes des publications approuvées.
- **Sécurité :** les sources artistiques ne sont jamais une racine de sortie.

## 11. Définir un manifeste de lot versionné

Le manifeste constitue l’entrée canonique du planificateur. Il ferme les champs attendus, référence les profils et refuse les chemins absolus propres à un poste.

Les secrets, jetons et données personnelles n’y figurent jamais.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
schema_version: 1
batch:
  id: AST-PRODUCTION-BATCH-SCOUT-RELAY-001
  revision: 0.1.0-draft
  source_revision: "<git-commit>"
  profile_set: AST-ART-BATCH-PROFILES-001
tasks:
  - id: export-scout
    kind: blender_export
    profile: AST-BLENDER-EXPORT-CHARACTER-001
  - id: generate-relay-markings
    kind: comfyui_workflow
    profile: AST-COMFYUI-CONCEPT-001
policy:
  max_parallel_cpu: 2
  max_parallel_gpu: 1
  maximum_attempts: 2
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Version :** `schema_version` permet de faire évoluer le format.
- **Source :** la révision Git relie le lot aux contrats consommés.
- **Tâches :** chaque entrée possède un identifiant et un profil.
- **Politique :** les limites de ressources sont explicites.
- **Secrets :** les identifiants d’accès restent fournis par un mécanisme externe.

## 12. Modéliser une tâche de lot

Une tâche porte sa classe, ses dépendances, ses ressources et ses conditions de réussite. Le planificateur n’infère pas ces données depuis le nom d’un script.

Les sorties attendues sont des chemins relatifs sous le staging du run.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
from dataclasses import dataclass
from enum import StrEnum

class TaskKind(StrEnum):
    BLENDER = "blender"
    COMFYUI = "comfyui"
    GODOT = "godot"
    HUMAN = "human"

@dataclass(frozen=True, slots=True)
class BatchTask:
    task_id: str
    kind: TaskKind
    depends_on: tuple[str, ...]
    resource_class: str
    output_paths: tuple[str, ...]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Enumération :** `TaskKind` ferme les familles connues du planificateur.
- **Dépendances :** `depends_on` contient des identifiants stables.
- **Ressource :** la classe choisit la capacité CPU, GPU ou humaine.
- **Sorties :** les chemins attendus permettent de vérifier la complétude.
- **Limite :** une tâche humaine peut bloquer le graphe sans être exécutée par un worker.

## 13. Construire un graphe de dépendances acyclique

Les tâches forment un graphe orienté : un export précède l’import, puis la validation technique précède la revue artistique. Un cycle signale un plan invalide, pas une situation à résoudre par des relances.

Le tri topologique doit être stable lorsque plusieurs tâches sont prêtes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
def ready_task_ids(
    tasks_by_id: dict[str, BatchTask],
    completed: frozenset[str],
) -> tuple[str, ...]:
    ready = []
    for task_id, task in tasks_by_id.items():
        if task_id in completed:
            continue
        if all(dep in completed for dep in task.depends_on):
            ready.append(task_id)
    return tuple(sorted(ready))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** le dictionnaire contient le plan validé et `completed` les succès vérifiés.
- **Condition :** toutes les dépendances doivent être terminées.
- **Retour :** le tri lexical stabilise la sélection des tâches prêtes.
- **Effet :** la fonction ne lance aucun job et ne modifie aucun état.
- **Précondition :** l’absence de cycle et de dépendance inconnue est validée séparément.

## 14. Définir la machine d’états d’une tâche

Un booléen `done` ne distingue pas une attente, une exécution, un échec retentable, un blocage définitif ou une validation humaine. Les états guident les actions autorisées.

Une tâche interrompue n’est pas réutilisable tant que ses sorties ne sont pas vérifiées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
task_states:
  PLANNED:
    next: [READY, BLOCKED]
  READY:
    next: [RUNNING, CANCELLED]
  RUNNING:
    next: [SUCCEEDED, RETRYABLE_FAILED, BLOCKED, INTERRUPTED]
  RETRYABLE_FAILED:
    next: [READY, BLOCKED]
  SUCCEEDED:
    next: [VERIFIED]
  VERIFIED:
    terminal: true
  BLOCKED:
    terminal: true
  CANCELLED:
    terminal: true
  INTERRUPTED:
    next: [READY, BLOCKED]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **États :** l’exécution et la vérification restent séparées.
- **Retry :** un échec retentable revient à `READY` seulement selon la politique.
- **Interruption :** la reprise exige une vérification des artefacts.
- **Terminaux :** `VERIFIED`, `BLOCKED` et `CANCELLED` ne sont pas confondus.
- **Rapport :** chaque transition conserve son auteur ou son processus.

## 15. Énoncer préconditions et postconditions

Un worker ne doit pas découvrir ses obligations pendant l’exécution. Les préconditions contrôlent les fichiers, versions et profils ; les postconditions contrôlent les sorties, rapports et empreintes.

Une commande qui retourne zéro sans produire son artefact attendu reste un échec de contrat.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
task_contract:
  id: export-relay
  preconditions:
    - source_hash_matches_manifest
    - blender_version_matches_profile
    - export_collection_exists_once
    - staging_directory_is_empty
  postconditions:
    - glb_exists
    - report_exists
    - artifact_hash_matches_report
    - source_hash_unchanged
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Préconditions :** elles empêchent une exécution sur une source ou un outil inattendu.
- **Staging :** un dossier propre évite de réutiliser une sortie ancienne.
- **Postconditions :** code de sortie, fichiers et empreintes sont tous nécessaires.
- **Source :** son empreinte doit rester inchangée après le job.
- **Décision :** l’échec d’une condition produit un diagnostic stable.

## 16. Rendre les opérations idempotentes

Une opération idempotente peut être répétée sans accumuler des nœuds, suffixes, fichiers ou métadonnées supplémentaires. Elle reconstruit un résultat depuis le contrat au lieu de modifier un état inconnu par petites touches.

Lorsque l’idempotence est impossible, le worker doit exiger un workspace neuf.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
def replace_generated_collection(
    collection_name: str,
    build_collection,
) -> None:
    existing = bpy.data.collections.get(collection_name)
    if existing is not None:
        bpy.data.collections.remove(existing, do_unlink=True)
    generated = build_collection()
    generated.name = collection_name
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Recherche :** la collection générée est identifiée par un nom réservé.
- **Remplacement :** l’ancienne sortie est retirée avant reconstruction.
- **Callback :** `build_collection` crée une structure complète, non un delta.
- **Effet de bord :** la scène ouverte est modifiée ; elle doit être une copie de travail.
- **Limite :** les données artistiques manuelles ne doivent jamais utiliser le préfixe réservé.

## 17. Paramétrer les scripts Blender

Les scripts Blender reçoivent un fichier de job validé plutôt que des constantes dispersées. Le job distingue source, collection d’export, profil, staging et rapport.

Les chemins sont résolus par l’orchestrateur avant le lancement et restent sous des racines autorisées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "task_id": "export-relay",
  "source_blend": "workspace/sources/relay.blend",
  "export_collection": "AST_PROP_RELAY__EXPORT",
  "export_profile": "AST-BLENDER-EXPORT-STATIC-001",
  "output_glb": "staging/relay/relay.glb",
  "report_json": "staging/relay/blender-report.json",
  "expected_source_sha256": "<sha256>"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schéma :** le format est versionné et fermé avant l’appel Blender.
- **Collection :** l’export ne dépend pas de la sélection interactive.
- **Profil :** les options d’export sont référencées par identité.
- **Empreinte :** la source copiée doit correspondre au manifeste.
- **Sorties :** GLB et rapport résident dans le staging du run.

## 18. Lancer Blender en arrière-plan

Le fichier `.blend` est chargé avant le script, car Blender applique les arguments dans l’ordre. `--python-exit-code` rend les exceptions Python visibles dans le code de sortie.

Les arguments propres au script suivent `--` afin de ne pas être interprétés comme des options Blender.

> **[PS] PowerShell 7 — Lancer un job Blender isolé — Ne pas saisir.**

```powershell
$blender = "C:\Tools\Blender\blender.exe"
& $blender `
  --background "workspace\sources\relay.blend" `
  --python-exit-code 23 `
  --python "automation\workflows\blender\run_job.py" `
  -- `
  --job "work\runs\RUN-001\jobs\export-relay.json"

if ($LASTEXITCODE -ne 0) {
  throw "Blender a échoué avec le code $LASTEXITCODE"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ordre :** le fichier source précède le script et ses arguments.
- **Arrière-plan :** `--background` retire la dépendance à l’interface.
- **Code Python :** `23` distingue une exception du script dans le rapport d’orchestration.
- **Séparateur :** les paramètres après `--` sont lus par `sys.argv`.
- **Effet :** la commande modifie uniquement la copie de workspace et le staging.

## 19. Limiter le contexte implicite de `bpy.ops`

Les opérateurs Blender dépendent souvent du contexte actif, de la sélection et du mode. Pour les transformations de données, l’accès direct à `bpy.data` et aux propriétés est plus prévisible.

Lorsqu’un opérateur est nécessaire, le script vérifie son `poll()` et prépare explicitement le contexte attendu.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
def set_all_objects_unselected() -> None:
    for obj in bpy.context.scene.objects:
        obj.select_set(False)

def export_operator_available() -> bool:
    return bool(bpy.ops.export_scene.gltf.poll())

if not export_operator_available():
    raise RuntimeError("BLENDER_EXPORT_CONTEXT_INVALID")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sélection :** elle est réinitialisée au lieu d’hériter de l’interface précédente.
- **Disponibilité :** `poll()` vérifie le contexte de l’opérateur.
- **Retour :** un booléen est converti explicitement.
- **Refus :** un code stable remplace une exception vague de contexte.
- **Limite :** la disponibilité de l’opérateur ne prouve pas la validité des options d’export.

## 20. Travailler sur une copie isolée des sources

L’orchestrateur copie la source canonique et ses dépendances autorisées dans le workspace du run. Blender n’ouvre jamais la source publiée avec permission d’écriture.

Après le job, l’empreinte de la source canonique est recalculée pour détecter toute mutation hors contrat.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
from shutil import copy2

def prepare_blender_workspace(
    source: Path,
    workspace_source: Path,
    expected_sha256: str,
) -> None:
    if sha256_file(source) != expected_sha256:
        raise ValueError("SOURCE_HASH_MISMATCH")
    workspace_source.parent.mkdir(parents=True, exist_ok=True)
    copy2(source, workspace_source)
    if sha256_file(workspace_source) != expected_sha256:
        raise ValueError("WORKSPACE_COPY_MISMATCH")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** source, destination et empreinte attendue sont obligatoires.
- **Contrôle initial :** une source divergente bloque le lot.
- **Copie :** les métadonnées ordinaires sont préservées sans déplacer l’autorité.
- **Contrôle final :** la copie doit être identique avant ouverture.
- **Effet :** seul le workspace reçoit un nouveau fichier.

## 21. Valider la scène Blender avant export

Le script contrôle les collections attendues, les objets cachés, les transforms, les références externes et les noms réservés. Les règles de famille proviennent des profils déjà établis dans le Livre III.

La validation produit tous les constats déterministes avant de décider si l’export peut commencer.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
@dataclass(frozen=True, slots=True)
class BlenderFinding:
    code: str
    object_name: str | None
    severity: str
    message: str

def validate_export_collection(name: str) -> tuple[BlenderFinding, ...]:
    collection = bpy.data.collections.get(name)
    if collection is None:
        return (BlenderFinding(
            "EXPORT_COLLECTION_MISSING", None, "BLOCKER", name
        ),)
    findings: list[BlenderFinding] = []
    if not collection.all_objects:
        findings.append(BlenderFinding(
            "EXPORT_COLLECTION_EMPTY", None, "BLOCKER", name
        ))
    return tuple(findings)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Modèle :** chaque constat possède code, cible, sévérité et message.
- **Recherche :** la collection est obtenue par son nom contractuel.
- **Retours :** une collection absente ou vide produit un blocker.
- **Accumulation :** la fonction peut être étendue par les profils de famille.
- **Limite :** cette validation technique ne juge pas la qualité artistique.

## 22. Produire un rapport Blender structuré

Le rapport conserve la version de Blender, la source, la collection, les constats et les sorties. Les messages de console restent complémentaires, pas autoritaires.

Un rapport peut exister pour une tâche bloquée sans prétendre qu’un GLB a été publié.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "task_id": "export-relay",
  "blender_version": "5.2.0",
  "background": true,
  "source_sha256": "<sha256>",
  "collection": "AST_PROP_RELAY__EXPORT",
  "status": "BLOCKED",
  "findings": [
    {
      "code": "EXPORT_COLLECTION_EMPTY",
      "severity": "BLOCKER",
      "object_name": null
    }
  ],
  "artifacts": []
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contexte :** version et mode de lancement expliquent l’environnement.
- **Source :** l’empreinte relie le rapport à la copie exacte.
- **Statut :** `BLOCKED` reste distinct d’une panne d’orchestrateur.
- **Constats :** les diagnostics sont exploitables sans analyser la console.
- **Artefacts :** une liste vide est valide lorsque l’export n’a pas eu lieu.

## 23. Exporter un GLB avec un profil fermé

Les options de l’exporteur ne sont pas assemblées depuis des valeurs implicites de l’interface. Un profil versionné fournit les propriétés et le script refuse les clés inconnues.

Le résultat est écrit dans le staging, puis contrôlé par empreinte et par les validations du chapitre 29.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
ALLOWED_GLTF_OPTIONS = {
    "export_format",
    "use_selection",
    "export_yup",
    "export_apply",
}

def export_glb(output_path: Path, options: dict[str, object]) -> None:
    unknown = set(options) - ALLOWED_GLTF_OPTIONS
    if unknown:
        raise ValueError(f"UNKNOWN_GLTF_OPTIONS:{sorted(unknown)}")
    result = bpy.ops.export_scene.gltf(
        filepath=str(output_path),
        **options,
    )
    if "FINISHED" not in result:
        raise RuntimeError(f"GLTF_EXPORT_NOT_FINISHED:{sorted(result)}")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Liste autorisée :** les options non qualifiées sont refusées.
- **Chemin :** `filepath` pointe vers le staging résolu.
- **Opérateur :** les propriétés sont passées par mots-clés.
- **Retour :** l’ensemble d’états doit contenir `FINISHED`.
- **Postcondition :** l’existence et l’empreinte du GLB sont vérifiées après cet appel.

## 24. Versionner les workflows ComfyUI au format API

Le workflow d’interface et le workflow API n’ont pas la même finalité. Le lot soumet un graphe au format API, avec identifiants de nœuds, `class_type` et entrées explicites.

Le fichier est versionné et son empreinte figure dans chaque manifeste d’exécution.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```json
{
  "3": {
    "class_type": "KSampler",
    "inputs": {
      "seed": 4815162342,
      "steps": 24,
      "cfg": 6.5,
      "sampler_name": "euler",
      "scheduler": "normal",
      "model": ["4", 0],
      "positive": ["6", 0],
      "negative": ["7", 0],
      "latent_image": ["5", 0]
    }
  }
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Nœud :** la clé `3` constitue une identité de graphe, pas un ordre d’exécution.
- **Type :** `class_type` doit exister dans l’environnement qualifié.
- **Entrées :** seed, sampler et dimensions sont fixés par le plan d’expérience.
- **Connexions :** les tableaux `[node_id, slot]` relient les sorties.
- **Limite :** l’extrait n’est pas un workflow complet ni exécuté.

## 25. Manifester modèles et custom nodes ComfyUI

Le batch refuse un workflow dont un modèle ou un paquet de nœuds n’est pas qualifié. Les versions, commits, licences, empreintes et permissions réseau appartiennent au manifeste d’environnement.

L’installation automatique d’une dépendance manquante est interdite pendant un run.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
comfyui_environment:
  profile_id: AST-COMFYUI-CONCEPT-001
  comfyui_version: 0.28.0
  workflow_sha256: "<sha256>"
  models:
    - id: MODEL-CHECKPOINT-001
      revision: "<immutable-revision>"
      sha256: "<sha256>"
      licence_status: approved
  custom_nodes:
    - id: NODEPACK-CONTROL-001
      commit: "<commit>"
      dependency_lock_sha256: "<sha256>"
      network_access: denied
      status: approved
  install_missing_dependencies: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil :** l’environnement possède une identité versionnée.
- **Modèles :** révision, empreinte et droits restent indépendants.
- **Nœuds :** le commit et le verrou empêchent une mise à jour silencieuse.
- **Réseau :** la permission est déclarée, pas déduite.
- **Porte :** une dépendance absente bloque l’exécution.

## 26. Soumettre une requête à la file ComfyUI

Le client local envoie le workflow complet à `/prompt` et récupère un `prompt_id`. Une erreur de validation du graphe reste un refus contrôlé, non une panne retentable par défaut.

Un identifiant client corrèle les messages WebSocket et le manifeste du run.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
import json
from urllib.request import Request, urlopen

def queue_prompt(
    base_url: str,
    workflow: dict[str, object],
    client_id: str,
    timeout_seconds: float,
) -> str:
    payload = json.dumps({
        "prompt": workflow,
        "client_id": client_id,
    }).encode("utf-8")
    request = Request(
        f"{base_url.rstrip('/')}/prompt",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=timeout_seconds) as response:
        body = json.load(response)
    return str(body["prompt_id"])
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** URL, workflow, client et délai sont fournis par le job.
- **Payload :** le graphe complet est sérialisé en JSON UTF-8.
- **Délai :** `urlopen` borne l’attente réseau initiale.
- **Retour :** le `prompt_id` devient l’identité serveur de l’exécution.
- **Erreurs :** HTTP, JSON ou clé absente sont convertis ensuite en diagnostics structurés.

## 27. Suivre l’exécution et récupérer les sorties

Le client écoute les messages WebSocket ou interroge l’historique selon le profil. Une reconnexion ne transforme pas une absence de message en succès.

La récupération finale utilise le `prompt_id`, puis copie uniquement les sorties déclarées dans le staging du run.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
comfyui_tracking:
  prompt_id: "<prompt-id>"
  client_id: "<uuid>"
  completion_signals:
    - execution_success
    - execution_error
    - execution_interrupted
  fallback:
    mode: history_polling
    interval_seconds: profile_value
    maximum_wait_seconds: profile_value
  output_policy:
    accept_only_declared_nodes: true
    copy_to_quarantine: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Signaux :** succès, erreur et interruption sont terminaux et distincts.
- **Repli :** le polling possède intervalle et durée maximale.
- **Sorties :** seuls les nœuds autorisés peuvent produire des artefacts du lot.
- **Quarantaine :** les fichiers générés ne rejoignent pas un dossier approuvé.
- **Limite :** un succès serveur ne vaut pas validation artistique.

## 28. Conserver seeds et niveaux de reproductibilité

La seed est enregistrée avec le workflow, les modèles, les nœuds, les entrées et le backend. Le manifeste distingue une identité binaire démontrée d’une simple reproduction de famille.

Une nouvelle tentative conserve la seed lorsque l’objectif est de reprendre la même expérience ; une variation volontaire crée un nouvel item.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
generation_run:
  item_id: relay-marking-a-0003
  workflow_sha256: "<sha256>"
  environment_profile: AST-COMFYUI-CONCEPT-001
  seed: 4815162342
  input_hashes:
    - "<sha256>"
  attempt: 2
  variation_reason: retry_same_item
  reproducibility_claim: family_only
  output_hashes: []
  review_status: quarantine
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Item :** l’identité de variante reste stable pendant les retries.
- **Environnement :** le profil complète la seed.
- **Tentative :** le compteur documente la reprise.
- **Allégation :** `family_only` évite une promesse binaire non démontrée.
- **Statut :** aucune sortie n’est sélectionnée automatiquement.

## 29. Mettre les sorties génératives en quarantaine

Les sorties ComfyUI arrivent dans un espace non approuvé. Leur copie vers une planche comparative ne change pas leur statut juridique ou artistique.

La promotion exige une décision humaine reliée à la question visuelle et aux critères du chapitre 3.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
quarantine_record:
  artifact_id: AST-GEN-RELAY-MARKING-0003
  run_item_id: relay-marking-a-0003
  relative_path: quarantine/relay/marking-a-0003.png
  sha256: "<sha256>"
  provenance_status: documented
  technical_status: generated
  artistic_status: NOT_REVIEWED
  allowed_transitions:
    - REJECTED
    - SELECTED_CONCEPT
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** chaque fichier généré possède un identifiant distinct.
- **Provenance :** elle peut être documentée sans valider la qualité.
- **Technique :** `generated` signifie seulement que le job a produit un fichier.
- **Art :** `NOT_REVIEWED` bloque toute utilisation comme décision.
- **Transitions :** seules une revue et ses preuves changent le statut.

## 30. Déclarer les classes de ressources

Le plan distingue les jobs CPU, Blender, GPU ComfyUI, Godot et humains. Une classe de ressource possède une capacité et éventuellement une exclusivité.

Cette déclaration évite qu’une file logique lance plusieurs tâches lourdes sur une même carte graphique.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
resource_classes:
  cpu_light:
    capacity: 4
  blender_process:
    capacity: 2
    memory_budget: profile_value
  gpu_comfyui:
    capacity: 1
    exclusive_key: gpu-0
  godot_import:
    capacity: 1
    exclusive_key: godot-import-cache
  human_art_review:
    capacity: manual
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Capacité :** le nombre de jobs simultanés est borné.
- **Mémoire :** les valeurs restent dans un profil à mesurer.
- **Exclusivité GPU :** une clé commune empêche le chevauchement.
- **Cache Godot :** l’import partagé est sérialisé lorsqu’il utilise le même workspace.
- **Humain :** la revue ne consomme pas un worker automatique.

## 31. Borner la concurrence

Le nombre de workers provient du profil, jamais du nombre de tâches. Les résultats sont triés par identité après exécution pour préserver un rapport stable.

Une exception bloque la promotion du lot même si d’autres futures terminent.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def run_cpu_tasks(
    tasks: tuple[BatchTask, ...],
    workers: int,
) -> tuple[tuple[str, str], ...]:
    if not 1 <= workers <= 8:
        raise ValueError("WORKER_COUNT_OUT_OF_RANGE")
    results: list[tuple[str, str]] = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        future_map = {
            pool.submit(run_task, task): task.task_id
            for task in tasks
        }
        for future in as_completed(future_map):
            results.append((future_map[future], future.result()))
    return tuple(sorted(results))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Borne :** `workers` est validé avant la création du pool.
- **Association :** chaque future conserve l’identité de la tâche.
- **Propagation :** `future.result()` relaie l’échec du worker.
- **Ordre :** le tri final neutralise l’ordre de terminaison.
- **Limite :** les jobs GPU exclusifs utilisent un ordonnanceur distinct.

## 32. Protéger une ressource GPU exclusive

Un sémaphore local suffit uniquement lorsque tous les workers résident dans le même processus. En CI distribuée, la ressource exige un runner dédié ou une primitive de verrouillage externe qualifiée.

Le verrou possède un délai afin qu’un worker mort ne laisse pas une attente infinie.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
from threading import BoundedSemaphore

GPU_SLOT = BoundedSemaphore(value=1)

def run_gpu_task(task: BatchTask, acquire_timeout: float) -> str:
    acquired = GPU_SLOT.acquire(timeout=acquire_timeout)
    if not acquired:
        raise TimeoutError("GPU_SLOT_TIMEOUT")
    try:
        return run_task(task)
    finally:
        GPU_SLOT.release()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sémaphore :** la valeur `1` impose l’exclusivité dans le processus.
- **Délai :** l’acquisition peut échouer de manière observable.
- **Libération :** `finally` rend le slot même après exception.
- **Retour :** le résultat du worker est propagé.
- **Frontière :** ce verrou ne coordonne pas plusieurs machines.

## 33. Appliquer la backpressure

La file d’admission doit refuser ou différer un lot lorsque sa capacité de staging, de GPU ou de revue est saturée. Ajouter toujours plus de jobs masque le problème et augmente le coût de reprise.

La capacité est exprimée en items et en octets estimés lorsque ces estimations sont qualifiées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
admission_policy:
  maximum_pending_items: 24
  maximum_staging_bytes: profile_value
  maximum_unreviewed_outputs: 40
  on_capacity_reached:
    action: refuse_new_batch
    code: BATCH_CAPACITY_REACHED
    retry_after_seconds: profile_value
  drop_policy: none
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Items :** la file pending possède une borne indépendante des workers.
- **Stockage :** le profil peut ajouter une limite en octets.
- **Revue :** trop de sorties non revues bloque de nouvelles générations.
- **Refus :** un code stable permet une reprise ultérieure.
- **Aucune perte :** les jobs existants ne sont pas supprimés silencieusement.

## 34. Définir délais et annulation

Chaque adaptateur possède un délai de connexion, d’exécution et d’arrêt. L’annulation demande d’abord un arrêt coopératif, puis marque les sorties partielles comme non réutilisables.

Tuer un processus ne prouve pas que ses enfants, verrous ou fichiers temporaires ont disparu.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
timeouts:
  blender:
    start_seconds: profile_value
    execution_seconds: profile_value
    terminate_grace_seconds: profile_value
  comfyui:
    submit_seconds: profile_value
    completion_seconds: profile_value
    interrupt_grace_seconds: profile_value
  godot:
    import_seconds: profile_value
cancellation:
  partial_outputs: quarantine
  checkpoint_status: invalid_until_verified
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Phases :** connexion, exécution et arrêt ont des délais distincts.
- **Profils :** aucune valeur réelle n’est inventée dans le chapitre.
- **Interruption :** ComfyUI et les processus externes utilisent leur contrat propre.
- **Partiels :** ils rejoignent la quarantaine, jamais la promotion.
- **Checkpoint :** il reste invalide jusqu’au contrôle d’intégrité.

## 35. Limiter les nouvelles tentatives

Une nouvelle tentative est réservée aux pannes transitoires identifiées : indisponibilité locale, délai réseau ou saturation temporaire. Une erreur de schéma, une dépendance inconnue ou un blocker artistique ne devient pas retentable.

Le nombre maximal inclut la première exécution.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
@dataclass(frozen=True, slots=True)
class RetryPolicy:
    maximum_attempts: int
    retryable_codes: frozenset[str]

    def allows(self, attempt: int, code: str) -> bool:
        if attempt < 1:
            raise ValueError("ATTEMPT_MUST_START_AT_ONE")
        return (
            attempt < self.maximum_attempts
            and code in self.retryable_codes
        )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Borne :** `maximum_attempts` inclut l’essai initial.
- **Codes :** l’ensemble immuable ferme les erreurs transitoires admises.
- **Validation :** une tentative commence à `1`.
- **Retour :** le booléen décide seulement de la relance.
- **Effets :** délai, backoff et création du nouvel essai restent à l’orchestrateur.

## 36. Classer les échecs sans les masquer

La taxonomie sépare une entrée invalide, une panne d’outil, une capacité saturée, un contrôle technique bloquant et une décision humaine négative. Chaque classe conduit à une action différente.

Le rapport conserve le premier échec causal et les conséquences annulées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
failure_classes:
  INPUT_INVALID:
    retryable: false
    action: correct_plan
  TOOL_UNAVAILABLE:
    retryable: conditional
    action: restore_qualified_environment
  CAPACITY_REACHED:
    retryable: true
    action: defer
  TECHNICAL_BLOCKER:
    retryable: false
    action: create_new_candidate_revision
  ART_REJECTED:
    retryable: false
    action: revise_art_direction_or_candidate
  EXECUTION_INTERRUPTED:
    retryable: conditional
    action: verify_checkpoint
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** un plan invalide est corrigé, pas relancé.
- **Outil :** la disponibilité ne suffit pas sans version qualifiée.
- **Capacité :** le report peut être retenté après libération.
- **Technique et art :** les corrections créent une nouvelle révision.
- **Interruption :** la reprise dépend des empreintes du checkpoint.

## 37. Écrire des checkpoints vérifiés

Un checkpoint enregistre les tâches vérifiées et les empreintes de leurs sorties. La présence d’un fichier ou d’un statut `succeeded` ne suffit pas.

Le checkpoint est écrit atomiquement après les postconditions, jamais pendant la production d’un artefact.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "run_id": "RUN-ASTERIA-BATCH-0001",
  "plan_sha256": "<sha256>",
  "verified_tasks": {
    "export-relay": {
      "attempt": 1,
      "artifacts": {
        "relay/relay.glb": "<sha256>",
        "relay/blender-report.json": "<sha256>"
      }
    }
  },
  "failed_tasks": {},
  "checkpoint_sequence": 4
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Plan :** son empreinte empêche une reprise croisée.
- **Tâches :** seules les sorties `VERIFIED` sont enregistrées.
- **Artefacts :** chaque chemin relatif possède une empreinte.
- **Séquence :** elle aide à sélectionner le dernier checkpoint complet.
- **Écriture :** le remplacement atomique est une postcondition de l’orchestrateur.

## 38. Reprendre après une interruption

La reprise recharge le plan, contrôle son empreinte et revalide chaque artefact avant de marquer une tâche réutilisable. Une divergence force la régénération de la tâche et de ses dépendants.

Les décisions humaines déjà signées restent valides uniquement pour le candidat et les preuves exactes qu’elles citent.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
def reusable_task_ids(
    checkpoint: dict[str, object],
    expected_plan_sha256: str,
    staging: Path,
) -> frozenset[str]:
    if checkpoint["plan_sha256"] != expected_plan_sha256:
        return frozenset()
    reusable: set[str] = set()
    for task_id, record in sorted(checkpoint["verified_tasks"].items()):
        artifacts = record["artifacts"]
        if all(
            sha256_file(resolve_inside(staging, path)) == digest
            for path, digest in artifacts.items()
        ):
            reusable.add(task_id)
    return frozenset(reusable)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Plan :** une divergence invalide tout le checkpoint.
- **Parcours :** les tâches sont examinées dans un ordre stable.
- **Contrôle :** chaque artefact doit encore exister avec la bonne empreinte.
- **Retour :** l’ensemble immuable alimente le planificateur.
- **Limite :** les dépendants d’une tâche régénérée sont invalidés par une étape séparée.

## 39. Promouvoir depuis un staging fermé

La publication commence seulement lorsque les tâches obligatoires sont vérifiées et que les approbations humaines exigées existent. Les artefacts sont copiés depuis un inventaire fermé.

Une promotion partielle ne doit pas laisser un mélange de deux révisions dans le dossier publié.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
promotion_gate:
  batch_id: AST-PRODUCTION-BATCH-SCOUT-RELAY-001
  required:
    - all_mandatory_tasks_verified
    - artifact_manifest_complete
    - technical_gate_complete
    - rights_gate_complete
    - artistic_approval_present
  strategy: versioned_directory_then_pointer_switch
  source: work/runs/<run_id>/staging
  destination: published/<batch_id>/<revision>
  overwrite_existing_revision: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Préconditions :** les dimensions technique, juridique et artistique restent séparées.
- **Stratégie :** une nouvelle version est préparée avant bascule.
- **Source :** le staging du run est l’unique origine.
- **Immutabilité :** une révision publiée n’est pas écrasée.
- **Limite :** la technique de bascule doit être adaptée au stockage réel.

## 40. Consolider manifestes d’artefacts et provenance

Le manifeste final relie chaque sortie à sa tâche, ses entrées, ses outils et son statut. Il n’enregistre pas seulement un chemin de fichier.

Les preuves restreintes restent dans une archive interne ; le dépôt public reçoit uniquement les métadonnées redistribuables.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
artifact:
  artifact_id: AST-ARTIFACT-RELAY-GLB-001
  relative_path: relay/relay.glb
  media_type: model/gltf-binary
  size_bytes: profile_measurement
  sha256: "<sha256>"
  produced_by:
    task_id: export-relay
    run_id: RUN-ASTERIA-BATCH-0001
    tool_profile: AST-BLENDER-5-2-001
  inputs:
    source_sha256: "<sha256>"
    export_profile_sha256: "<sha256>"
  decisions:
    technical: pending
    artistic: pending
    rights: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** l’artefact possède un identifiant indépendant du chemin.
- **Production :** tâche, run et profil expliquent son origine.
- **Entrées :** les empreintes rendent la transformation traçable.
- **Décisions :** les trois portes restent explicitement en attente.
- **Mesure :** la taille réelle n’est renseignée qu’après matérialisation.

## 41. Sérialiser canoniquement et calculer les empreintes

Les manifestes utilisent une sérialisation stable avant calcul SHA-256. Les clés sont triées, l’encodage est UTF-8 et les séparateurs ne dépendent pas d’un formateur.

L’empreinte établit l’intégrité relative aux octets, pas l’auteur, la licence ou la qualité.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
from hashlib import sha256
import json

def canonical_json_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    ).encode("utf-8")

def object_sha256(value: object) -> str:
    return sha256(canonical_json_bytes(value)).hexdigest()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Tri :** l’ordre d’insertion des dictionnaires ne change pas les octets.
- **Séparateurs :** les espaces de présentation sont supprimés.
- **Nombres :** NaN et infinis sont refusés.
- **Retour :** l’empreinte hexadécimale possède 64 caractères.
- **Limite :** une signature ou attestation reste un mécanisme distinct.

## 42. Journaliser avec corrélation

Chaque événement porte le lot, le run, la tâche et la tentative. Les journaux humains et machine lisibles dérivent du même événement structuré.

Les prompts complets, secrets et données personnelles ne sont pas copiés dans les journaux par défaut.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```json
{
  "timestamp_utc": "2026-07-25T07:40:00Z",
  "level": "ERROR",
  "event": "task_failed",
  "batch_id": "AST-PRODUCTION-BATCH-SCOUT-RELAY-001",
  "run_id": "RUN-ASTERIA-BATCH-0001",
  "task_id": "generate-relay-markings",
  "attempt": 2,
  "code": "COMFYUI_EXECUTION_INTERRUPTED",
  "retryable": false,
  "sensitive_fields_redacted": true
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Temps :** l’événement utilise UTC pour les échanges.
- **Corrélation :** quatre identifiants situent précisément l’échec.
- **Code :** la cause stable complète le message humain.
- **Retry :** la décision courante est visible.
- **Rédaction :** les champs sensibles ne sont pas sérialisés.

## 43. Produire un rapport de lot

Le rapport synthétise l’exécution sans remplacer les rapports Blender, ComfyUI, Godot et qualité. Il présente les statuts, diagnostics, artefacts et décisions restantes.

Un lot peut être techniquement complet tout en restant `HUMAN_REVIEW_REQUIRED`.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
batch_report:
  batch_id: AST-PRODUCTION-BATCH-SCOUT-RELAY-001
  run_id: RUN-ASTERIA-BATCH-0001
  execution_status: COMPLETED
  tasks:
    verified: 6
    blocked: 0
    cancelled: 0
  artifacts_manifest: artifacts/manifest.json
  technical_gate: PASSED
  rights_gate: PASSED
  artistic_gate: HUMAN_REVIEW_REQUIRED
  final_status: NOT_PROMOTABLE
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Exécution :** `COMPLETED` décrit le scheduler, pas la publication.
- **Tâches :** les comptes facilitent le diagnostic sans remplacer le détail.
- **Manifestes :** le rapport pointe vers les preuves.
- **Portes :** technique, droits et art restent indépendants.
- **Final :** l’absence de revue humaine bloque la promotion.

## 44. Échantillonner les résultats humainement

La revue de tous les artefacts peut être impossible pour un grand lot, mais un échantillon aléatoire naïf peut manquer les cas rares. La stratégie combine items obligatoires, frontières de profil, échecs réparés et sélection déterministe par hash.

Les éléments non échantillonnés ne deviennent pas artistiquement approuvés par extrapolation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
def deterministic_sample(
    item_ids: tuple[str, ...],
    mandatory: frozenset[str],
    sample_size: int,
    batch_seed: str,
) -> tuple[str, ...]:
    selected = set(mandatory)
    ranked = sorted(
        item_ids,
        key=lambda item_id: sha256(
            f"{batch_seed}:{item_id}".encode("utf-8")
        ).hexdigest(),
    )
    for item_id in ranked:
        if len(selected) >= sample_size:
            break
        selected.add(item_id)
    return tuple(sorted(selected))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Obligatoires :** les cas à risque entrent toujours dans l’échantillon.
- **Classement :** le hash produit un ordre stable à partir du lot.
- **Borne :** `sample_size` limite la revue automatique proposée.
- **Retour :** les identifiants sont triés pour la planche.
- **Limite :** la stratégie doit être complétée par des critères de couverture.

## 45. Construire une planche comparative

La planche associe chaque vignette à son item sans exposer des paramètres susceptibles de biaiser la première lecture lorsque le protocole prévoit une revue aveugle.

Une seconde passe révèle les paramètres, la provenance et les constats techniques pour justifier la décision.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
comparison_board:
  board_id: AST-BOARD-RELAY-MARKINGS-001
  batch_id: AST-PRODUCTION-BATCH-SCOUT-RELAY-001
  first_pass:
    blinded_fields: [seed, sampler, model_label]
    visible_fields: [candidate_code, image]
  second_pass:
    visible_fields:
      - workflow_revision
      - provenance_status
      - technical_findings
      - parameters
  decision_form: AST-ART-REVIEW-FORM-001
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Première passe :** la lecture visuelle peut être protégée de certains biais.
- **Code :** chaque candidat reste traçable sans afficher sa recette complète.
- **Seconde passe :** les preuves redeviennent visibles avant décision finale.
- **Formulaire :** les critères et commentaires sont structurés.
- **Limite :** l’aveuglement n’est utilisé que lorsqu’il sert réellement le protocole.

## 46. Exiger une validation humaine indépendante

La personne qui écrit le script ou règle le workflow ne doit pas être l’unique autorité d’approbation d’un lot Studio. En Solo, une revue différée et une checklist explicite réduisent le biais sans prétendre créer une indépendance organisationnelle.

La décision cite le lot, l’échantillon, les exceptions et la portée de l’approbation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
human_approval:
  approval_id: AST-APPROVAL-BATCH-0001
  batch_id: AST-PRODUCTION-BATCH-SCOUT-RELAY-001
  run_id: RUN-ASTERIA-BATCH-0001
  reviewer_role: art_lead
  reviewed_items:
    - relay-marking-a-0003
    - relay-marking-b-0001
  scope: sampled_outputs_only
  decision: CHANGES_REQUESTED
  findings:
    - AST-FINDING-RELAY-SYMBOL-READABILITY-001
  signature_status: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identités :** l’approbation vise un run exact.
- **Rôle :** le reviewer est enregistré par fonction.
- **Portée :** l’échantillon n’approuve pas implicitement le reste.
- **Décision :** une demande de changements reste distincte d’un rejet.
- **Signature :** le document n’est pas final tant que son statut reste pending.

## 47. Intégrer les contrôles techniques à la CI

La CI valide les manifestes, prépare les jobs et exécute uniquement les tâches adaptées à ses runners. Les opérations exigeant des modèles lourds, des droits restreints ou un GPU local peuvent rester manuelles avec artefacts importés.

La CI ne télécharge pas des modèles ou custom nodes non qualifiés pendant le workflow.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
name: Validate Art Batch

on:
  workflow_dispatch:
    inputs:
      plan:
        required: true
        type: string

jobs:
  validate-plan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python -m asteria_art_batches validate-plan "${{ inputs.plan }}"

  technical-gates:
    needs: validate-plan
    strategy:
      fail-fast: false
      matrix:
        profile: [blender-static, blender-character, godot-import]
    uses: ./.github/workflows/reusable-art-task.yml
    with:
      profile: "${{ matrix.profile }}"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déclenchement :** le plan est fourni explicitement.
- **Validation :** le schéma et les chemins sont contrôlés avant la matrice.
- **Dépendance :** les gates ne démarrent qu’après succès du plan.
- **Matrice :** les profils restent séparés et `fail-fast` conserve les diagnostics.
- **Frontière :** aucune étape ne signe l’acceptation artistique.

## 48. Définir une matrice CI et ses profils

La matrice couvre les outils et plateformes réellement qualifiés. Une combinaison non testée reste absente ou marquée expérimentale au lieu d’être supposée compatible.

Le nombre de jobs et leur parallélisme sont bornés pour éviter la saturation des runners et du stockage.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ci_matrix:
  include:
    - os: windows
      tool: blender
      profile: AST-BLENDER-5-2-WINDOWS-001
      qualified: false
    - os: windows
      tool: godot
      profile: AST-GODOT-4-7-WINDOWS-001
      qualified: false
    - os: self-hosted-gpu
      tool: comfyui
      profile: AST-COMFYUI-AMD-WINDOWS-001
      qualified: false
policy:
  max_parallel: 2
  fail_fast: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** chaque ligne associe système, outil et profil.
- **Qualification :** `false` reflète l’absence d’exécution réelle.
- **GPU :** un runner auto-hébergé nécessite sa propre sécurité.
- **Parallélisme :** la capacité est bornée au niveau de la stratégie.
- **Diagnostics :** `fail_fast: false` collecte les résultats indépendants.

## 49. Conserver les artefacts CI utiles

Les rapports, manifestes, journaux rédigés et échantillons autorisés sont publiés comme artefacts de workflow. Les sources restreintes, modèles, contrats et données personnelles en sont exclus.

La durée de conservation suit le risque, le coût et les obligations du projet.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ci_artifacts:
  public_safe:
    - batch-report.json
    - artifact-manifest.json
    - technical-findings.json
    - redacted-logs.jsonl
  restricted:
    - source-blend-files
    - licensed-reference-images
    - model-weights
    - consent-documents
  retention_days: project_policy
  digest_required: true
  promotion_from_ci_artifact: prohibited_without_gate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** les preuves redistribuables sont listées explicitement.
- **Restreints :** les sources et documents sensibles ne deviennent pas des artefacts publics.
- **Rétention :** la valeur réelle appartient à une politique approuvée.
- **Digest :** l’artefact téléchargé doit être vérifiable.
- **Promotion :** un ZIP CI ne contourne pas les portes du chapitre 29.

## 50. Sécuriser secrets, réseau et dépendances

Les tokens éventuels sont injectés par le gestionnaire de secrets et ne sont jamais écrits dans le plan, la console ou le manifeste public. Les jobs locaux utilisent le mode hors ligne lorsque le contrat le permet.

Les dépendances Blender, Python et ComfyUI sont épinglées et revues avant exécution.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
security_policy:
  secrets:
    source: ci_secret_store_or_local_provider
    allowed_in_manifest: false
    log_redaction: required
  network:
    default: denied
    allowlist: []
  dependencies:
    blender_addons: qualified_only
    comfyui_custom_nodes: pinned_and_reviewed
    python_lock: required
  generated_code_execution: prohibited
  untrusted_workflow_installation: prohibited
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Secrets :** ils restent hors des fichiers versionnés.
- **Réseau :** l’absence de liste autorisée signifie aucun accès.
- **Dépendances :** chaque écosystème conserve son verrou ou manifeste.
- **Code généré :** une sortie IA n’est jamais exécutée automatiquement.
- **Workflow reçu :** son ouverture ne déclenche aucune installation.

## 51. Borner coûts, stockage et volume de sorties

Un lot définit le nombre maximal d’items, la taille de staging, le nombre de variantes et la quantité de sorties en attente de revue. Les limites financières restent pertinentes lorsqu’un service externe est autorisé.

Une estimation dépassée bloque l’admission ; elle ne supprime pas les sorties existantes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
quota_profile:
  maximum_batch_items: 32
  maximum_variants_per_experiment: 8
  maximum_unreviewed_outputs: 40
  maximum_staging_bytes: profile_value
  external_service_budget_eur: null
  on_limit:
    status: BLOCKED
    code: QUOTA_EXCEEDED
    required_action: revise_plan_or_profile
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Items :** le lot et chaque expérience possèdent des bornes.
- **Revue :** l’accumulation de sorties non évaluées est limitée.
- **Stockage :** la valeur doit être mesurée sur l’infrastructure réelle.
- **Budget :** `null` signifie qu’aucun montant n’est qualifié ou autorisé.
- **Refus :** le plan est révisé plutôt que tronqué silencieusement.

## 52. Mode Solo

Le parcours Solo commence par des lots de deux à cinq tâches, exécutés localement depuis une commande lisible. La personne conserve les manifestes, inspecte chaque sortie et limite la génération ComfyUI à une expérience dont la condition d’arrêt est écrite avant le lancement.

La revue artistique est différée : fermer la session, revenir avec la grille du chapitre 3 et comparer les sorties sans modifier les paramètres pendant l’évaluation. Une correction crée un nouvel item ou une nouvelle révision ; elle ne remplace pas discrètement le fichier déjà examiné.

La reprise utilise un checkpoint local, mais le nettoyage reste manuel et vérifié. Aucun script Solo ne doit parcourir une racine large avec suppression récursive, installer un nœud manquant ou publier automatiquement dans le dossier du jeu.

## 53. Mode Studio

Le parcours Studio sépare le propriétaire du plan, les opérateurs d’outils, les responsables des profils, la QA technique, la direction artistique et la personne autorisée à promouvoir. Les files partagées possèdent quotas, SLA, priorités et journaux de corrélation.

Les runners Blender et Godot sont reproductibles ; les runners GPU sont isolés, inventoriés et réservés par une politique de capacité. Les artefacts de revue sont accessibles selon le rôle, tandis que les sources sous licence et consentements restent dans un stockage restreint.

L’approbation d’un lot est indépendante de son auteur lorsque l’organisation le permet. Une dérogation possède une portée, une expiration et un plan de correction ; une campagne urgente ne change pas silencieusement les profils communs.

## 54. Préparer les exemples du Companion Pack

Le Companion Pack recevra des modèles réutilisables, pas les sources ou modèles non redistribuables de Project Asteria. Chaque exemple doit fonctionner avec des placeholders et décrire les dépendances à fournir.

Les exemples restent séparés du Starter Kit tant que celui-ci n’est pas matérialisé et qualifié.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
companion_pack_candidates:
  - path: Companion-Pack/templates/art-batch-plan.schema.json
    status: planned
  - path: Companion-Pack/templates/blender-job.schema.json
    status: planned
  - path: Companion-Pack/templates/comfyui-run-manifest.yaml
    status: planned
  - path: Companion-Pack/examples/bounded-batch-runner/
    status: planned
  - path: Companion-Pack/examples/art-batch-ci.yml
    status: planned
redistributable_assets_included: false
starter_kit_materialized: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Candidats :** schémas, manifests et runner sont identifiés.
- **Statut :** `planned` ne prétend pas que les fichiers existent.
- **Exemples :** ils utiliseront des données fictives redistribuables.
- **Assets :** aucun modèle, image ou source Asteria n’est inclus.
- **Starter Kit :** sa matérialisation reste un chantier distinct.

## 55. Conserver, nettoyer et archiver les runs

Le nettoyage cible uniquement les sous-répertoires autorisés d’un run. Les rapports de décision et manifestes publiés suivent une politique de conservation distincte du cache ou des previews.

Une suppression est journalisée et ne réécrit pas l’historique d’acceptation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```python
from shutil import rmtree

CLEANABLE_RUN_DIRS = frozenset({
    "cache",
    "previews",
    "temporary",
})

def clean_run_subdir(run_root: Path, name: str) -> None:
    if name not in CLEANABLE_RUN_DIRS:
        raise ValueError("CLEAN_TARGET_FORBIDDEN")
    target = resolve_inside(run_root, name)
    if target.exists():
        rmtree(target)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Liste fermée :** seuls trois dossiers jetables sont autorisés.
- **Résolution :** le chemin reste sous la racine du run.
- **Suppression :** l’opération est récursive uniquement après validation.
- **Exclusions :** staging vérifié, manifestes, rapports et décisions ne sont pas concernés.
- **Journal :** l’appelant enregistre l’identité du run et l’opérateur.

## 56. Définir la clôture du lot et du Livre III

Un lot est clos lorsque ses tâches obligatoires possèdent un état terminal, ses artefacts sont inventoriés et ses décisions restantes sont explicites. Un lot non promotable peut être clos comme échec documenté.

La fin documentaire du Livre III exige en plus les trente chapitres, leurs audits et preuves, puis la compilation et l’inspection du PDF lecteur selon le protocole de publication. Cette exigence ne transforme pas les pilotes non matérialisés en résultats runtime.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
closure_contract:
  batch:
    terminal_tasks_accounted_for: true
    artifact_manifest_complete: true
    unresolved_findings_listed: true
    promotion_status_explicit: true
  livre_iii:
    chapters_expected: 30
    chapter_30_static_review: true
    end_of_book_pdf_required: true
    visual_pdf_inspection_required: true
    runtime_pilots_required_for_claims_only: true
    collection_licence_status: unresolved
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Lot :** succès et échec documenté peuvent tous deux être terminaux.
- **Artefacts :** l’inventaire permet une reprise et un archivage.
- **Livre :** la clôture éditoriale déclenche la chaîne PDF de fin de Livre.
- **Runtime :** les réserves restent ouvertes tant que les pilotes ne sont pas exécutés.
- **Licence :** la décision globale de collection demeure indépendante.

## 57. Diagnostics : erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

Les dix cas suivants montrent comment une automatisation apparemment efficace peut perdre l’identité, saturer les ressources ou contourner la validation humaine. Chaque correction rétablit un contrat mesurable.

### 57.1 Lancer un script Blender sur la source canonique

**Symptôme ou risque :** Le job modifie directement le `.blend` publié et rend impossible la comparaison avec l’entrée.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```python
source = Path("art/blender/sources/relay.blend")
subprocess.run(
    ["blender", "--background", str(source), "--python", "fix_and_export.py"],
    check=True,
)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le processus ouvre la source avec un script qui peut enregistrer ou modifier des données sans workspace ni contrôle d’empreinte.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```python
prepare_blender_workspace(source, workspace_source, expected_sha256)
subprocess.run([
    "blender", "--background", str(workspace_source),
    "--python-exit-code", "23",
    "--python", "run_job.py", "--", "--job", str(job_path),
], check=True)
assert sha256_file(source) == expected_sha256
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La source reste en lecture seule par contrat, le job travaille sur une copie vérifiée et l’empreinte finale détecte toute mutation hors périmètre.

### 57.2 Dépendre de la sélection interactive Blender

**Symptôme ou risque :** Le même fichier exporte des objets différents selon l’état laissé dans l’interface.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```python
bpy.ops.export_scene.gltf(
    filepath="relay.glb",
    use_selection=True,
)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** `use_selection=True` consomme un contexte implicite que le job n’a ni préparé ni enregistré.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```python
collection = bpy.data.collections["AST_PROP_RELAY__EXPORT"]
set_all_objects_unselected()
for obj in collection.all_objects:
    obj.select_set(True)
if not bpy.ops.export_scene.gltf.poll():
    raise RuntimeError("BLENDER_EXPORT_CONTEXT_INVALID")
export_glb(output_path, qualified_options)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La collection contractuelle détermine la sélection, le contexte est contrôlé et le profil ferme les options.

### 57.3 Installer automatiquement les custom nodes manquants

**Symptôme ou risque :** Un workflow reçu modifie l’environnement et exécute des dépendances non revues pendant le lot.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
comfyui_job:
  workflow: received.json
  install_missing_custom_nodes: true
  trust_registry_results: true
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** L’installation dynamique déplace la chaîne d’approvisionnement dans l’exécution et peut changer le code, les modèles, le réseau ou les sorties.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
comfyui_job:
  workflow: qualified-api.json
  environment_profile: AST-COMFYUI-CONCEPT-001
  install_missing_custom_nodes: false
  on_missing_dependency:
    status: BLOCKED
    code: COMFYUI_DEPENDENCY_UNQUALIFIED
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le profil épinglé devient la seule autorité ; toute dépendance absente produit un blocker avant la génération.

### 57.4 Utiliser une seed comme preuve d’identité binaire

**Symptôme ou risque :** Deux environnements différents sont considérés équivalents parce qu’ils utilisent le même entier.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
reproducibility:
  seed: 4815162342
  claim: exact
  environment_manifest: absent
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La sortie dépend aussi du workflow, des modèles, des nœuds, des versions, des entrées et du backend matériel.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
reproducibility:
  seed: 4815162342
  workflow_sha256: "<sha256>"
  environment_profile: AST-COMFYUI-CONCEPT-001
  input_hashes: ["<sha256>"]
  claim: family_only
  exact_reproduction_evidence: null
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La promesse reste limitée à une famille tant qu’une comparaison binaire qualifiée n’a pas été démontrée.

### 57.5 Relancer sans limite une erreur structurelle

**Symptôme ou risque :** Un workflow invalide remplit la file avec la même requête et masque la cause.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```python
while True:
    try:
        queue_prompt(base_url, workflow, client_id, 30.0)
        break
    except Exception:
        continue
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Toutes les erreurs deviennent retentables, aucune borne ni diagnostic n’est conservé et la boucle peut être infinie.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```python
code = classify_exception(error)
if not retry_policy.allows(attempt, code):
    raise BatchTaskBlocked(code) from error
schedule_retry(
    task_id,
    attempt + 1,
    bounded_backoff(attempt),
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Seuls les codes transitoires admis sont relancés, dans une limite explicite et avec conservation de la cause.

### 57.6 Réutiliser un checkpoint sur un plan modifié

**Symptôme ou risque :** Une sortie ancienne est promue après changement de profil ou de source.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
resume:
  checkpoint: latest.json
  compare_plan_hash: false
  trust_existing_files: true
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le nom du checkpoint et la présence des fichiers ne prouvent pas qu’ils appartiennent au plan courant.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
resume:
  checkpoint: checkpoint-0004.json
  required_plan_sha256: "<current-plan-sha256>"
  verify_each_artifact_sha256: true
  invalidate_dependents_on_mismatch: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le plan et chaque artefact sont vérifiés ; toute divergence entraîne une régénération cohérente.

### 57.7 Lancer plusieurs jobs GPU sur la même carte

**Symptôme ou risque :** Le scheduler traite la capacité logique comme si elle représentait la mémoire et l’exclusivité réelles.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
resource_class: gpu_comfyui
workers: 4
gpu_index: 0
exclusive: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Quatre workers peuvent saturer la VRAM, provoquer des OOM et rendre les délais non interprétables.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
resource_class: gpu_comfyui
capacity: 1
exclusive_key: gpu-0
acquire_timeout_seconds: profile_value
on_timeout: GPU_SLOT_TIMEOUT
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le profil impose un seul job, un verrou identifiable et un refus observable lorsque la ressource reste occupée.

### 57.8 Promouvoir parce que tous les jobs ont retourné zéro

**Symptôme ou risque :** Le scheduler confond exécution réussie, contrôle technique et acceptation artistique.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
batch:
  exit_codes: [0, 0, 0]
  final_status: PUBLISHED
  human_review: skipped
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les codes de sortie ne prouvent ni la conformité artistique, ni les droits, ni la portée d’une dérogation.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
batch:
  execution_status: COMPLETED
  technical_gate: PASSED
  rights_gate: PASSED
  artistic_gate: HUMAN_REVIEW_REQUIRED
  final_status: NOT_PROMOTABLE
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Chaque dimension conserve son statut et la promotion reste bloquée jusqu’à une approbation humaine valide.

### 57.9 Échantillonner uniquement les premiers fichiers

**Symptôme ou risque :** Les mêmes catégories et seeds sont toujours revues tandis que les cas tardifs ou rares échappent au contrôle.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```python
sample = sorted(item_ids)[:10]
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le tri lexical n’assure aucune couverture des profils, erreurs réparées, frontières ou variations.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```python
mandatory = boundary_items | repaired_items | rights_sensitive_items
sample = deterministic_sample(
    tuple(item_ids),
    frozenset(mandatory),
    sample_size=profile.sample_size,
    batch_seed=batch.plan_sha256,
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les cas à risque sont obligatoires et le complément est sélectionné de façon stable et reproductible.

### 57.10 Nettoyer une racine trop large après le lot

**Symptôme ou risque :** Une commande récursive peut supprimer des sources, rapports ou artefacts publiés.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```python
rmtree(project_root / "art")
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La cible n’est pas limitée au run et l’opération ne distingue pas cache, source ou publication.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```python
clean_run_subdir(run_root, "temporary")
append_cleanup_event(
    run_id=run_id,
    target="temporary",
    operator=operator_id,
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La liste autorisée et la résolution sous `run_root` bornent la suppression, puis l’événement reste traçable.

## 58. Checklist de production et d’acceptation

Cette checklist décrit les preuves nécessaires ; elle reste ouverte tant que le pilote n’est pas matérialisé. Une case n’est cochée que pour une révision exacte et un artefact consultable.

La fermeture documentaire du chapitre ne remplace aucune exécution Blender, ComfyUI, Godot ou humaine.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
checklist_status:
  pilot: AST-PRODUCTION-BATCH-SCOUT-RELAY-001
  plan_schema_documented: true
  batch_runner_materialized: false
  blender_jobs_executed: false
  comfyui_jobs_executed: false
  godot_jobs_executed: false
  checkpoint_recovery_demonstrated: false
  ci_executed: false
  human_sample_reviewed: false
  assets_promoted: false
  evidence_level: static_review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pilote :** la checklist vise un lot identifié.
- **Documentation :** les contrats sont décrits dans le chapitre.
- **Exécution :** tous les jobs réels restent à `false`.
- **Reprise :** aucune interruption n’est présentée comme démonstration.
- **Promotion :** aucun asset ou concept n’est déclaré publié.

- [ ] plan de lot figé avec identifiant, révision et empreinte ;
- [ ] tâches classées en déterministes, génératives ou humaines ;
- [ ] dépendances acycliques et sorties attendues validées ;
- [ ] profils Blender, ComfyUI, Godot et qualité qualifiés ;
- [ ] sources copiées dans un workspace isolé ;
- [ ] scripts Blender paramétrés, idempotents et contrôlés ;
- [ ] workflow ComfyUI API et environnement manifestés ;
- [ ] seeds, modèles, custom nodes, entrées et sorties enregistrés ;
- [ ] classes de ressources et capacités bornées ;
- [ ] timeouts, annulations et retries limités ;
- [ ] checkpoint écrit après vérification des artefacts ;
- [ ] reprise testée contre un plan et des empreintes identiques ;
- [ ] staging fermé et promotion transactionnelle ;
- [ ] journaux corrélés et données sensibles rédigées ;
- [ ] rapport et manifeste d’artefacts complets ;
- [ ] échantillon représentatif défini avant la revue ;
- [ ] approbation humaine avec portée explicite ;
- [ ] CI limitée aux tâches et runners qualifiés ;
- [ ] artefacts CI redistribuables et rétention définie ;
- [ ] aucune autorité artistique ou gameplay déléguée à l’automatisation ;

## 59. Références techniques officielles

Les références suivantes documentent les interfaces utilisées. Elles ne remplacent ni les profils du projet, ni la qualification des versions, ni les tests du pilote.

Les pages locales restent les autorités de périmètre pour les sources, droits, importations, portes qualité et automatisation Python.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
reference_scope:
  blender:
    - command_line_arguments
    - python_api_data_and_operators
    - gltf_export
  comfyui:
    - workflow_graph
    - local_server_routes
    - websocket_messages
  github_actions:
    - workflow_syntax
    - matrix
    - concurrency
    - artifacts
  godot:
    - command_line_headless_import
  python:
    - subprocess
    - concurrent_futures
    - hashlib_and_json
  runtime_evidence: separate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Blender :** la ligne de commande et l’API encadrent les jobs en arrière-plan.
- **ComfyUI :** workflow, routes et messages décrivent la file locale.
- **CI :** matrice, concurrence et artefacts sont contrôlés par les workflows.
- **Godot :** les imports headless restent ceux du chapitre 28.
- **Limite :** aucune page de documentation ne constitue une campagne exécutée.

- [Blender Manual 5.2 — Arguments de ligne de commande](https://docs.blender.org/manual/en/5.2/advanced/command_line/arguments.html)
- [Blender Python API — Accès aux données `bpy.data`](https://docs.blender.org/api/current/bpy.data.html)
- [Blender Python API — Opérateurs `bpy.ops`](https://docs.blender.org/api/current/bpy.ops.html)
- [Blender Python API — Export glTF 2.0](https://docs.blender.org/api/current/bpy.ops.export_scene.html)
- [ComfyUI — Concepts de workflow](https://docs.comfy.org/development/core-concepts/workflow)
- [ComfyUI Server — Vue d’ensemble des communications](https://docs.comfy.org/development/comfyui-server/comms_overview)
- [ComfyUI Server — Routes locales](https://docs.comfy.org/development/comfyui-server/comms_routes)
- [ComfyUI Server — Messages WebSocket](https://docs.comfy.org/development/comfyui-server/comms_messages)
- [GitHub Actions — Syntaxe des workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [GitHub Actions — Contrôler la concurrence](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency)
- [GitHub Actions — Stocker et partager des artefacts](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-what-your-workflow-does/storing-and-sharing-data-from-a-workflow)
- [Godot 4.7 — Tutoriel de ligne de commande](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html)
- [Python 3 — `subprocess`](https://docs.python.org/3/library/subprocess.html)
- [Python 3 — `concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html)
- [Python 3 — `hashlib`](https://docs.python.org/3/library/hashlib.html)
- [Python 3 — `json`](https://docs.python.org/3/library/json.html)
- [Livre II — Chapitre 29 : Automatisation Python et génération de données](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md)
- [Livre III — Chapitre 3 : Références, concept art et ComfyUI](CHAPITRE-03-References-concept-art-et-ComfyUI.md)
- [Livre III — Chapitre 4 : Pipeline Blender et organisation des fichiers](CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md)
- [Livre III — Chapitre 5 : Provenance, licences et validation des assets](CHAPITRE-05-Provenance-licences-et-validation-des-assets.md)
- [Livre III — Chapitre 28 : Importation et intégration dans Godot](CHAPITRE-28-Importation-et-integration-dans-Godot.md)
- [Livre III — Chapitre 29 : Validation technique et artistique des assets](CHAPITRE-29-Validation-technique-et-artistique-des-assets.md)

## 60. Synthèse opérationnelle pour Project Asteria

Project Asteria retient `AST-PRODUCTION-BATCH-SCOUT-RELAY-001` comme pilote d’orchestration du Livre III. Le plan réunira les exports de l’éclaireur et du module de relais, l’expérience ComfyUI `AST-EXP-RELAY-MARKINGS-001`, l’import du chapitre 28 et la porte qualité `AST-ASSET-GATE-SCOUT-RELAY-001`.

Les jobs Blender travailleront sur des copies isolées et des collections explicites. Les jobs ComfyUI utiliseront un workflow API, un environnement épinglé, des seeds et des sorties en quarantaine. Le scheduler bornera les ressources, les tentatives, les délais et le stockage, puis écrira manifestes, journaux, checkpoints et rapports.

La réussite technique conduira seulement à une revue humaine. Aucune image générée, source Blender, sortie GLB ou preuve CI ne sera promue sans droits qualifiés, validation Godot et approbation artistique de portée explicite. Tous les livrables restent non matérialisés au niveau de preuve actuel.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asteria_batch_decisions:
  pilot_id: AST-PRODUCTION-BATCH-SCOUT-RELAY-001
  plan_schema_id: AST-ART-BATCH-PLAN-001
  profile_set_id: AST-ART-BATCH-PROFILES-001
  comfyui_experiment_id: AST-EXP-RELAY-MARKINGS-001
  import_dependency: AST-IMPORT-PILOT-SCOUT-RELAY-001
  quality_gate_dependency: AST-ASSET-GATE-SCOUT-RELAY-001
  orchestration:
    bounded_concurrency: true
    verified_checkpoints: true
    staging_promotion: true
    automatic_dependency_installation: false
  promotion_requires:
    - technical_gate_complete
    - rights_gate_complete
    - godot_evidence_complete
    - human_artistic_approval
  automation_artistic_authority: none
  gameplay_authority: none
  materialization_status: not_started
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identifiants :** pilote, schéma, profils et expérience sont nommés durablement.
- **Dépendances :** import et qualité restent propriétaires de leurs décisions.
- **Orchestration :** concurrence, reprise et promotion utilisent des contrats vérifiables.
- **Sécurité :** aucune installation dynamique n’est admise pendant un run.
- **Porte :** technique, droits, preuve Godot et art sont tous nécessaires.
- **Autorité :** l’automatisation ne possède ni décision artistique ni état gameplay.
- **Réserve :** aucun lot, script, workflow, artefact, benchmark ou PDF n’est déclaré exécuté.
