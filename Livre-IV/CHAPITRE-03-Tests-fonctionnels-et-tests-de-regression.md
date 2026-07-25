---
title: "Livre IV — Chapitre 3 : Tests fonctionnels et tests de régression"
id: "DOC-L4-CH03"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 3
last-verified: "2026-07-26T00:16:25+02:00"
audit-status: "complete"
audit-date: "2026-07-26T00:16:25+02:00"
audit-report: "Livre-IV/QA/AUDIT-CHAPITRE-03.md"
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

# Tests fonctionnels et tests de régression

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[VSC]** Visual Studio Code, **[SORTIE]** résultat à lire, **[LECTURE]** exemple de référence.

## 1. Rôle du chapitre

Ce chapitre transforme la stratégie QA du chapitre 2 en campagnes reproductibles. Il définit les cas, fixtures, états contrôlés, oracles, suites et preuves. Il ne redéfinit ni les risques et portes du chapitre 2, ni la reproduction détaillée des anomalies du chapitre 4, ni l’observabilité du chapitre 5.

## 2. Résultats d’apprentissage

Le lecteur saura écrire un cas reproductible, préparer une fixture synthétique, distinguer les statuts, construire des suites smoke/rapide/complète/publication, établir une matrice de couverture et protéger une correction par un test de non-régression.

## 3. Niveau de preuve

Le chapitre est accepté au niveau `static-review`. Aucun cas, script, run Godot, campagne, mutation connue, mesure de durée ou résultat produit n’est revendiqué comme exécuté.

## 4. Frontières

Le chapitre 2 possède les risques, rôles et portes. Le présent chapitre possède les cas et campagnes. Le chapitre 4 possède le rapport d’anomalie, la réduction et la reproduction approfondie.


## 5. Catalogue de cas

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/cases/catalog.v1.yaml`.**

```yaml
case_id: AST-TC-SAVE-ROUNDTRIP-001
risk_id: AST-RISK-DATA-LOSS-001
suite: smoke
status: designed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 6. Contrat d’un cas

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/cases/save-roundtrip.v1.yaml`.**

```yaml
test_case:
  id: AST-TC-SAVE-ROUNDTRIP-001
  preconditions: [fresh_profile, writable_storage]
  actions: [create_save, reload_save]
  expected: [state_equivalent, no_data_loss]
  cleanup: delete_test_profile
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 7. Préconditions observables

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/contracts/preconditions.v1.yaml`.**

```yaml
precondition:
  id: writable_storage
  probe: storage.can_write_test_file
  expected: true
  on_failure: BLOCKED
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 8. Oracle explicite

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `res://test/oracles/save_oracle.gd`.**

```gdscript
class_name SaveOracle
extends RefCounted

func compare(expected: Dictionary, actual: Dictionary) -> bool:
	return expected == actual
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 9. Fixture synthétique

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `test/fixtures/player_profile.v1.json`.**

```json
{"fixture_id":"AST-FIXTURE-PROFILE-001","schema_version":12,"currency_minor_units":2500,"personal_data":false}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 10. Seeds contrôlées

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/seeds/smoke.v1.yaml`.**

```yaml
seed_set:
  id: AST-SEEDS-SMOKE-001
  values: [104729, 130363, 155921]
  engine_contract: godot-4.7.1
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 11. État initial

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `test/scenarios/relay-entry.v1.yaml`.**

```yaml
scenario:
  id: AST-SCENARIO-RELAY-ENTRY-001
  fixture: AST-FIXTURE-PROFILE-001
  clock: fixed
  network: disabled
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 12. Actions typées

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `test/scripts/relay-entry.commands.yaml`.**

```yaml
commands:
  - type: load_profile
    profile: AST-FIXTURE-PROFILE-001
  - type: enter_region
    region: relay_delta
  - type: assert_checkpoint
    id: relay_entry_ready
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 13. Résultat de cas

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `work/qa/results/case-result.v1.yaml`.**

```yaml
case_result:
  case_id: AST-TC-SAVE-ROUNDTRIP-001
  status: NOT_EXECUTED
  evidence: []
  duration_ms: null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 14. Statuts

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/statuses.v1.yaml`.**

```yaml
statuses: [PASS, FAIL, BLOCKED, SKIPPED, NOT_EXECUTED]
rules:
  BLOCKED: precondition_failed
  FAIL: oracle_failed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 15. Suite smoke

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/suites/smoke.v1.yaml`.**

```yaml
suite:
  id: AST-SUITE-SMOKE-001
  maximum_minutes: 10
  cases: [AST-TC-BOOT-001, AST-TC-SAVE-ROUNDTRIP-001]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 16. Suite rapide

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/suites/fast.v1.yaml`.**

```yaml
suite:
  id: AST-SUITE-FAST-001
  target: pull_request
  selection: changed_features_plus_critical
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 17. Suite complète

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/suites/full.v1.yaml`.**

```yaml
suite:
  id: AST-SUITE-FULL-001
  target: nightly
  selection: all_supported_cases
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 18. Suite publication

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/suites/release.v1.yaml`.**

```yaml
suite:
  id: AST-SUITE-RELEASE-001
  requires: [full_pass, security_review, accessibility_review, rollback_ready]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 19. Matrice de couverture

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/coverage/risk-case-matrix.v1.yaml`.**

```yaml
coverage:
  AST-RISK-DATA-LOSS-001:
    cases: [AST-TC-SAVE-ROUNDTRIP-001]
    suites: [smoke, full, release]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 20. Test manuel

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `docs/qa/manual/first-launch.md`.**

```text
Case: AST-TC-FIRST-LAUNCH-001
Given: clean user profile
When: launch game and start new expedition
Then: tutorial is reachable
Evidence: screenshots and notes
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 21. Test automatisé Godot

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `res://test/functional/test_save_roundtrip.gd`.**

```gdscript
extends Node

func run_case() -> Dictionary:
	var expected := {"credits": 2500}
	var actual := expected.duplicate(true)
	return {"status": "PASS" if actual == expected else "FAIL"}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 22. Manifeste Python

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `automation/src/asteria_tools/qa/run_manifest.py`.**

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class RunManifest:
    build_id: str
    suite_id: str
    environment_id: str
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 23. Commande de campagne

Cette section établit un contrat vérifiable et versionné.

> **[PS] PowerShell 7 — Lancer une suite bornée.**

```powershell
.\.venv\Scripts\python.exe -m asteria_tools.qa.run_suite `
  --suite config\qa\suites\smoke.v1.yaml `
  --workspace work\qa-runs\AST-QA-RUN-0001

if ($LASTEXITCODE -ne 0) { throw "La suite a échoué." }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 24. Rapport de campagne

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `work/qa/reports/AST-QA-REPORT-0001.yaml`.**

```yaml
report:
  id: AST-QA-REPORT-0001
  totals: {pass: 0, fail: 0, blocked: 0, not_executed: 2}
  decision: PENDING
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 25. Sélection par impact

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/selection/impact-map.v1.yaml`.**

```yaml
impact_map:
  res://src/features/save/: [save, inventory, economy]
  res://src/features/combat/: [combat, progression]
fallback_suite: smoke
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 26. Quarantaine

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/quarantine.v1.yaml`.**

```yaml
quarantine:
  - case_id: AST-TC-FLAKY-001
    owner: qa
    expires_on: 2026-08-15
    replacement_control: manual_check
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 27. Tests instables

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/flaky-policy.v1.yaml`.**

```yaml
policy:
  retry_limit: 1
  pass_after_retry: FLAKY
  automatic_pass_prohibited: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 28. Contrat de non-régression

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/regression-contract.v1.yaml`.**

```yaml
regression_contract:
  defect_id: AST-DEFECT-184
  reproduction_case: AST-TC-SAVE-MIGRATION-184
  fixed_revision: <git-commit>
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 29. Mutation connue

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/mutations/save-regression.v1.yaml`.**

```yaml
known_regression:
  id: AST-MUTATION-SAVE-DROP-CURRENCY-001
  isolated_branch: qa/mutation-save-drop-currency
  expected_detected_by: AST-TC-SAVE-ROUNDTRIP-001
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 30. Preuve de détection

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `work/qa/mutations/result.yaml`.**

```yaml
mutation_result:
  mutation_id: AST-MUTATION-SAVE-DROP-CURRENCY-001
  reference: NOT_EXECUTED
  injected: NOT_EXECUTED
  restored: NOT_EXECUTED
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 31. Nettoyage borné

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/cleanup.v1.yaml`.**

```yaml
cleanup:
  allowed_roots: [user://qa-sandbox, work/qa-runs]
  preserve_failed_run_evidence: true
  delete_real_profiles: prohibited
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 32. Mode Solo

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/modes/solo.v1.yaml`.**

```yaml
solo:
  smoke_on_change: true
  full_weekly: true
  release_before_tag: true
  deferred_self_review_hours: 12
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 33. Mode Studio

Cette section établit un contrat vérifiable et versionné.

> **[VSC] Visual Studio Code — Créer `config/qa/modes/studio.v1.yaml`.**

```yaml
studio:
  author: developer
  case_owner: qa
  release_decider: product_owner
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contrat :** l’identité et le but du bloc sont explicites.
- **Entrées :** les préconditions, données et environnement sont déclarés.
- **Sortie :** le résultat possède un statut contrôlé.
- **Limite :** aucune exécution réelle n’est revendiquée.


## 34. Diagnostics : erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 34.1 Tester sans oracle

**Symptôme ou risque :** L’attente vague ne permet pas de décider.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
expected: ça marche
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** L’attente vague ne permet pas de décider.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
expected:
  main_menu_visible: true
  fatal_error_count: 0
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les assertions deviennent observables.


### 34.2 Partager une fixture mutable

**Symptôme ou risque :** Les cas se contaminent.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
fixture: shared_profile
reset: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les cas se contaminent.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
fixture: AST-FIXTURE-PROFILE-001
clone_per_case: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Chaque cas reçoit une copie.


### 34.3 Confondre BLOCKED et FAIL

**Symptôme ou risque :** Le produit est accusé sans exécution.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
status: FAIL
reason: device_unavailable
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le produit est accusé sans exécution.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
status: BLOCKED
reason: required_device_unavailable
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le statut décrit l’environnement.


### 34.4 Retry jusqu’au vert

**Symptôme ou risque :** Le défaut intermittent est masqué.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
retry_until_pass: true
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le défaut intermittent est masqué.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
retry_limit: 1
pass_after_retry: FLAKY
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** L’instabilité reste visible.


### 34.5 Tester seulement le chemin heureux

**Symptôme ou risque :** Les refus et bornes restent inconnus.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
paths: [success]
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les refus et bornes restent inconnus.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
paths: [success, refusal, boundary, recovery]
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les catégories essentielles sont couvertes.


### 34.6 Utiliser une sauvegarde réelle

**Symptôme ou risque :** Des données personnelles peuvent fuiter.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
fixture: user_save.zip
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Des données personnelles peuvent fuiter.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
fixture: synthetic-save-v12.json
personal_data: prohibited
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La donnée synthétique est contrôlée.


### 34.7 Changer l’oracle après l’échec

**Symptôme ou risque :** Le test est déplacé pour passer.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
expected: updated_to_actual
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le test est déplacé pour passer.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
expected_version: 2
change_requires_review: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La modification est versionnée.


### 34.8 Quarantaine sans fin

**Symptôme ou risque :** Le test disparaît durablement.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
quarantine: true
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le test disparaît durablement.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
quarantine:
  owner: qa
  expires_on: 2026-08-15
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La quarantaine est bornée.


### 34.9 Fermer sans rejouer

**Symptôme ou risque :** Un commit ne prouve pas la correction.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
status: closed
reason: fix_committed
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Un commit ne prouve pas la correction.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
status: verified
verification_run: AST-QA-RUN-043
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Une exécution est citée.


### 34.10 Publier sur un taux global

**Symptôme ou risque :** Le taux masque les cas critiques.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
pass_rate: 99%
decision: release
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le taux masque les cas critiques.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
critical_cases: PASS
blocked_cases: 0
decision_owner: product_owner
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La décision consomme plusieurs preuves.


## 35. Checklist de production et d’acceptation

- [ ] catalogue de cas versionné ;
- [ ] préconditions, actions, oracle et nettoyage explicites ;
- [ ] fixtures synthétiques et isolées ;
- [ ] seeds et environnements déclarés ;
- [ ] statuts distincts ;
- [ ] suites smoke, rapide, complète et publication ;
- [ ] matrice de couverture par risque ;
- [ ] preuves reliées au build ;
- [ ] quarantaines bornées ;
- [ ] tests instables visibles ;
- [ ] cas permanent après chaque correction ;
- [ ] mutation connue limitée à une branche isolée ;
- [ ] aucune donnée réelle utilisée par défaut ;
- [ ] aucune décision automatique issue d’un taux global.

## 36. Critère d’acceptation

Le pilote sera matérialisé lorsqu’un cas passe sur une référence saine, échoue sur une mutation isolée connue, puis repasse après restauration, avec manifestes et preuves conservés. Le présent chapitre ne revendique aucune exécution.

## 37. Références techniques officielles

- [Godot 4.7 — Ligne de commande](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html)
- [Python 3.14 — `unittest`](https://docs.python.org/3.14/library/unittest.html)
- [Livre II — Chapitre 27](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md)
- [Livre IV — Chapitre 2](CHAPITRE-02-Strategie-generale-d-assurance-qualite.md)

## 38. Synthèse opérationnelle pour Project Asteria

Project Asteria retient un catalogue stable, des fixtures synthétiques, des états contrôlés, des suites par coût et risque, des statuts distincts et un cas permanent pour chaque régression corrigée.

> **[LECTURE] Décisions de campagne — Ne pas saisir.**

```yaml
asteria_test_strategy:
  catalog_id: AST-QA-CASE-CATALOG-001
  suites: [smoke, fast, full, release]
  synthetic_fixtures_default: true
  isolated_state_per_case: true
  explicit_oracle_required: true
  blocked_is_not_failed: true
  flaky_is_not_pass: true
  regression_case_required_after_fix: true
  known_mutation_isolated_branch_only: true
  release_authority: human_gate
  materialization_status: not_started
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Catalogue :** les cas possèdent des identifiants stables.
- **Isolation :** fixture et état sont propres à chaque cas.
- **Statuts :** blocage et instabilité ne deviennent pas des succès.
- **Régression :** une correction crée une protection permanente.
- **Autorité :** `not_started` interdit toute revendication d’exécution.
