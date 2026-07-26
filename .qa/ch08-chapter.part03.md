    while _order.size() > _capacity:
        var evicted_key := _order.pop_front()
        _values.erase(evicted_key)

func clear() -> void:
    _values.clear()
    _order.clear()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Capacité :** le nombre d’entrées possède une limite dure.
- **Récence :** chaque lecture déplace la clé en fin d’ordre.
- **Éviction :** les anciennes entrées perdent leur référence forte.
- **Limite :** une capacité en nombre d’objets ne remplace pas un budget en octets.

## 29. Cache pondéré par coût

Des entrées de tailles très différentes exigent un poids. L’estimation doit être cohérente et versionnée, même si elle n’égale pas exactement l’allocation réelle.

> **[VSC] Visual Studio Code — Étendre le cache avec un budget estimé.**

```gdscript
var _max_weight_bytes := 64 * 1024 * 1024
var _current_weight_bytes := 0
var _weights: Dictionary = {}

func put_weighted(key: Variant, value: Variant, weight_bytes: int) -> void:
    if weight_bytes < 0:
        push_error("Poids négatif interdit")
        return
    if _values.has(key):
        _current_weight_bytes -= int(_weights[key])
        _order.erase(key)
    _values[key] = value
    _weights[key] = weight_bytes
    _current_weight_bytes += weight_bytes
    _order.push_back(key)
    while _current_weight_bytes > _max_weight_bytes and not _order.is_empty():
        var evicted_key := _order.pop_front()
        _current_weight_bytes -= int(_weights[evicted_key])
        _weights.erase(evicted_key)
        _values.erase(evicted_key)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Poids :** chaque entrée déclare une estimation en octets.
- **Remplacement :** l’ancien poids est retiré avant mise à jour.
- **Budget :** l’éviction se poursuit jusqu’au retour sous la limite.
- **Prudence :** l’estimation doit être confrontée aux compteurs réels.

## 30. Cache négatif et expiration

Mémoriser indéfiniment les échecs peut empêcher une ressource corrigée d’être retrouvée. Un cache négatif doit posséder une expiration et une clé de version.

> **[LECTURE] Contrat de cache négatif — Ne pas saisir.**

```yaml
negative_cache:
  key:
    - resource_id
    - content_version
  entry:
    error_code: recorded
    created_at_monotonic_usec: recorded
    ttl_seconds: 30
  invalidation:
    - content_version_changed
    - manual_retry
    - ttl_expired
  maximum_entries: 512
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Version :** une correction de contenu produit une autre clé.
- **Expiration :** l’échec n’est pas conservé sans limite.
- **Capacité :** les erreurs sont elles aussi bornées.
- **Diagnostic :** le code d’erreur reste disponible pour le rapport.

## 31. Pooling : bénéfice et dette

Un pool peut réduire les créations fréquentes, mais il conserve volontairement des instances et leurs ressources. Sa taille doit être mesurée et sa remise à zéro testée.

> **[VSC] Visual Studio Code — Créer un pool borné de projectiles.**

```gdscript
class_name ProjectilePool
extends Node

@export var maximum_idle := 128
var _idle: Array[Node] = []

func acquire(factory: Callable) -> Node:
    if not _idle.is_empty():
        var projectile := _idle.pop_back()
        projectile.reset_for_reuse()
        return projectile
    return factory.call()

func release(projectile: Node) -> void:
    projectile.prepare_for_pool()
    if _idle.size() >= maximum_idle:
        projectile.queue_free()
        return
    _idle.push_back(projectile)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Réutilisation :** une instance inactive est remise à zéro avant emploi.
- **Capacité :** le pool ne conserve pas plus de 128 instances inactives.
- **Surplus :** les instances au-delà de la limite sont libérées.
- **Correction :** `reset_for_reuse()` et `prepare_for_pool()` doivent être couverts par des tests.

## 32. Allocations temporaires dans les boucles

Les tableaux, dictionnaires, chaînes et copies créés à chaque frame peuvent augmenter la pression mémoire et le coût CPU. Le premier levier est de réduire la fréquence et la quantité de données produites.

> **[VSC] Visual Studio Code — Réutiliser un tampon de candidats.**

```gdscript
var _nearby_candidates: Array[Node3D] = []

func collect_nearby_candidates(source: Array[Node3D],
        origin: Vector3, radius_squared: float) -> Array[Node3D]:
    _nearby_candidates.clear()
    for candidate in source:
        if candidate.global_position.distance_squared_to(origin) <= radius_squared:
            _nearby_candidates.push_back(candidate)
    return _nearby_candidates
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Tampon :** le tableau est conservé entre appels.
- **Calcul :** la distance au carré évite une racine carrée.
- **Fréquence :** la fonction doit rester appelée seulement lorsque nécessaire.
- **Contrat :** l’appelant ne doit pas conserver ou modifier le tampon retourné.

## 33. API sans propriété ambiguë

Retourner un tampon interne est rapide mais fragile. Une API sûre peut remplir un tableau fourni par l’appelant, qui en possède explicitement la durée de vie.

> **[VSC] Visual Studio Code — Préférer un tampon de sortie.**

```gdscript
func fill_nearby_candidates(
        source: Array[Node3D],
        origin: Vector3,
        radius_squared: float,
        output: Array[Node3D]) -> void:
    output.clear()
    for candidate in source:
        if candidate.global_position.distance_squared_to(origin) <= radius_squared:
            output.push_back(candidate)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Propriété :** l’appelant possède le tableau de sortie.
- **Réutilisation :** le même tampon peut servir à plusieurs cycles.
- **Absence de copie :** la fonction ne construit pas un nouveau tableau de résultat.
- **Documentation :** le contrat précise que le contenu précédent est effacé.

## 34. Structures compactes

Les `Packed*Array` conviennent aux séries homogènes et peuvent réduire le surcoût par élément par rapport à des conteneurs de `Variant`. Le choix dépend toutefois des opérations et conversions nécessaires.

> **[LECTURE] Choix de structure — Ne pas saisir.**

```yaml
data_layout:
  positions:
    preferred: PackedVector3Array
    reason: homogeneous_numeric_series
  entity_records:
    preferred: Array[Dictionary]
    reason: heterogeneous_debug_records
  binary_payload:
    preferred: PackedByteArray
    reason: serialized_bytes
  decision:
    benchmark_required: true
    conversion_cost_recorded: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Homogénéité :** les séries numériques utilisent un conteneur spécialisé.
- **Hétérogénéité :** les rapports de diagnostic privilégient la lisibilité.
- **Binaire :** les octets sérialisés évitent une liste de variants.
- **Mesure :** la conversion et les usages réels déterminent le choix final.

## 35. Chaînes et journaux

Construire de longues chaînes à chaque frame peut provoquer allocations et contention. Le chapitre 5 conserve la politique de journalisation ; ici, la règle est d’éviter la création du message lorsque l’événement n’est pas retenu.

> **[VSC] Visual Studio Code — Garder l’événement mémoire borné.**

```gdscript
func emit_budget_event(category: StringName, used_bytes: int,
        limit_bytes: int, should_emit: bool) -> void:
    if not should_emit:
        return
    var payload := {
        "category": String(category),
        "used_bytes": used_bytes,
        "limit_bytes": limit_bytes,
        "ratio": (
            float(used_bytes) / float(limit_bytes)
            if limit_bytes > 0 else null
        ),
    }
    MemoryEventBus.emit_structured(payload)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Garde :** aucun dictionnaire n’est créé lorsque l’événement est filtré.
- **Données :** les octets sources sont conservés.
- **Ratio :** la division par zéro est évitée.
- **Frontière :** la rétention et le débit restent gouvernés par le chapitre 5.

## 36. Images, textures et mipmaps

Une image CPU, une texture GPU et leurs variantes peuvent coexister. Le rapport identifie les copies, dimensions, formats, mipmaps et propriétaires au lieu d’estimer depuis le seul fichier source.

> **[LECTURE] Inventaire d’une texture — Ne pas saisir.**

```yaml
texture_inventory:
  resource_path: res://assets/environment/rock_albedo.ktx2
  dimensions: measured
  imported_format: recorded
  mipmaps: recorded
  cpu_image_retained: measured
  gpu_texture_present: measured
  duplicate_instances: measured
  owners:
    - material_library
    - preview_cache
  release_points:
    preview_cache: lru_eviction
    material_library: project_shutdown
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Étages :** source importée, image CPU et texture GPU sont distinguées.
- **Format :** dimensions, compression et mipmaps influencent l’empreinte.
- **Copies :** le nombre d’instances est mesuré.
- **Propriété :** chaque conservation possède un point de libération.

## 37. Scènes, sous-ressources et localité

Rendre une ressource locale à une scène ou dupliquer une sous-ressource peut être nécessaire pour l’état mutable, mais multiplie les instances. Le diagnostic compare les chemins, identifiants et raisons de localité.

> **[LECTURE] Rapport de duplication de sous-ressources — Ne pas saisir.**

```yaml
subresource_duplicates:
  source_scene: res://scenes/characters/guard.tscn
  resource_type: StandardMaterial3D
  expected_shared_instances: measured
  local_to_scene_instances: measured
  deep_duplicates: measured
  reasons:
    runtime_tint: explicit
    accidental_editor_duplicate: pending_review
  candidate_action:
    share_immutable_base: proposed
    isolate_mutable_parameters: proposed
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** la scène canonique est identifiée.
- **Catégories :** partage, localité et copie profonde sont séparés.
- **Raison :** une variation runtime ne justifie pas automatiquement une copie complète.
- **Action :** la proposition reste à mesurer et revoir.

## 38. Test de longue durée

> **[VSC] Visual Studio Code — Créer `config/performance/memory_soak_test.yaml`.**

```yaml
schema_version: 1
soak_test:
  id: AST-MEM-SOAK-001
  duration_minutes: 180
  warmup_minutes: 15
  cycle_count: 120
  sample_interval_seconds: 1
  checkpoints_minutes:
    - 15
    - 30
    - 60
    - 120
    - 180
  required_signals:
    - private_memory_bytes
    - working_set_bytes
    - static_memory_bytes
    - object_count
    - orphan_node_count
    - texture_mem_bytes
    - buffer_mem_bytes
    - video_mem_bytes
  failure:
    crash: blocking
    hard_budget_exceeded: blocking
    unrecovered_growth: review_required
    functional_error: blocking
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Durée :** la campagne couvre plusieurs heures et cycles.
- **Checkpoints :** des résumés intermédiaires facilitent l’attribution.
- **Signaux :** processus, moteur, objets et rendu sont rapprochés.
- **Porte :** crash, budget dur et régression fonctionnelle sont bloquants.

## 39. Rapport avant/après

> **[VSC] Visual Studio Code — Créer `reports/performance/memory/AST-MEM-001-comparison.yaml`.**

```yaml
schema_version: 1
comparison:
  baseline:
    commit: pending
    environment_manifest: pending
    raw_samples: pending
  candidate:
    commit: pending
    environment_manifest: pending
    raw_samples: pending
  change:
    hypothesis: pending
    primary_variable: pending
    rollback: pending
  metrics:
    ram_peak_mib:
      before: measured
      after: measured
    idle_plateau_slope_mib_per_cycle:
      before: measured
      after: measured
    vram_peak_mib:
      before: measured
      after: measured
    orphan_nodes_end:
      before: measured
      after: measured
  gates:
    memory_budget: pending
    long_run: pending
    functional_suite: pending
    visual_quality: pending
    human_approval: pending
  decision: pending
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Symétrie :** baseline et candidate possèdent environnement et échantillons.
- **Hypothèse :** la variable principale et le retour arrière sont écrits.
- **Métriques :** pics, pente et orphelins sont comparés séparément.
- **Porte :** la décision attend mémoire, durée, fonctionnel, visuel et approbation.

## 40. Diagnostics et anti-patterns

### 40.1 Conclure depuis une seule capture

**Symptôme ou risque :** Une capture montre une valeur élevée et l’équipe annonce une fuite.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
diagnosis:
  samples: 1
  phase: unknown
  warmup: ignored
  cycles: 0
  conclusion: leak_confirmed
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** une valeur isolée ne décrit ni tendance, ni récupération, ni phase.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au contrat du projet.**

```yaml
diagnosis:
  measured_cycles: 30
  phase: idle_plateau_end
  raw_series: retained
  recovery_window: observed
  slope: measured
  attribution: pending_review
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** la série cyclique, le plateau et la fenêtre de récupération soutiennent une enquête reproductible.

### 40.2 Confondre working set et mémoire privée

**Symptôme ou risque :** Deux outils affichent des nombres différents et l’un est déclaré faux.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
process_memory:
  working_set_bytes: 2400000000
  private_memory_bytes: 3100000000
  interpretation: counters_should_match
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** les compteurs décrivent des concepts différents et ne doivent pas coïncider.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au contrat du projet.**

```yaml
process_memory:
  working_set_bytes: measured
  private_memory_bytes: measured
  definitions: documented
  comparison: same_counter_across_runs
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** chaque série conserve sa définition et n’est comparée qu’à son équivalent.

### 40.3 Effacer un cache sans politique

**Symptôme ou risque :** La mémoire baisse, mais les temps de chargement et les saccades se dégradent.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```gdscript
func fix_memory() -> void:
    global_cache.clear()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** l’effacement total ignore finalité, fréquence, coût de reconstruction et budget.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au contrat du projet.**

```yaml
cache_change:
