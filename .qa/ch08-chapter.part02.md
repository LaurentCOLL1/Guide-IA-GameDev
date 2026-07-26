        "video_mem_bytes": RenderingServer.get_rendering_info(
            RenderingServer.RENDERING_INFO_VIDEO_MEM_USED
        ),
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Textures :** le compteur isole les ressources de texture suivies par le renderer.
- **Buffers :** les buffers sont suivis séparément.
- **Total :** la mémoire vidéo agrège les éléments connus du moteur.
- **Limite :** pilote, outils et autres processus peuvent consommer de la VRAM hors de cet inventaire.

## 15. Échantillon structuré

> **[VSC] Visual Studio Code — Créer `res://src/core/performance/memory_sample.gd`.**

```gdscript
class_name MemorySample
extends RefCounted

static func capture(phase: StringName, cycle: int) -> Dictionary:
    var sample := {
        "schema_version": 1,
        "timestamp_usec": Time.get_ticks_usec(),
        "phase": String(phase),
        "cycle": cycle,
    }
    sample.merge(MemoryProbe.snapshot())
    sample.merge(MemoryProbe.process_snapshot())
    sample.merge(MemoryProbe.rendering_memory_snapshot())
    return sample
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Horloge :** les ticks monotones ordonnent les échantillons dans une exécution.
- **Contexte :** phase et cycle permettent de comparer les mêmes moments.
- **Fusion :** les trois familles de compteurs restent nommées.
- **Schéma :** la version protège les analyses futures.

## 16. Collecteur borné

Échantillonner trop vite peut lui-même allouer, perturber les caches et gonfler les journaux. Le collecteur utilise une cadence explicite et une capacité maximale.

> **[VSC] Visual Studio Code — Créer `res://src/core/performance/memory_sampler.gd`.**

```gdscript
class_name MemorySampler
extends Node

@export var interval_seconds := 0.5
@export var max_samples := 20_000

var _elapsed := 0.0
var _phase: StringName = &"unknown"
var _cycle := 0
var _samples: Array[Dictionary] = []

func _process(delta: float) -> void:
    _elapsed += delta
    if _elapsed < interval_seconds:
        return
    _elapsed = 0.0
    if _samples.size() >= max_samples:
        return
    _samples.append(MemorySample.capture(_phase, _cycle))

func set_context(phase: StringName, cycle: int) -> void:
    _phase = phase
    _cycle = cycle
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cadence :** l’intervalle limite le coût de collecte.
- **Capacité :** le tableau cesse de croître après la limite.
- **Contexte :** la phase est modifiée par le scénario de campagne.
- **Réserve :** le coût propre du collecteur devra être mesuré avant usage prolongé.

## 17. Export JSONL déterministe

> **[VSC] Visual Studio Code — Ajouter l’export au collecteur.**

```gdscript
func export_jsonl(path: String) -> Error:
    var file := FileAccess.open(path, FileAccess.WRITE)
    if file == null:
        return FileAccess.get_open_error()
    for sample in _samples:
        file.store_line(JSON.stringify(sample, "", false, true))
    file.close()
    return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Format :** une ligne JSON représente un échantillon.
- **Ordre :** l’ordre d’insertion est conservé.
- **Erreur :** l’échec d’ouverture est renvoyé au scénario.
- **Mémoire :** l’exemple garde les échantillons en RAM ; un collecteur de très longue durée devra écrire par lots bornés.

## 18. Vue système sous Windows

La mémoire du processus vue par Windows complète les compteurs internes. La série doit viser le PID du build mesuré, pas un processus portant seulement un nom similaire.

> **[PS] PowerShell 7 — Échantillonner le processus ciblé.**

```powershell
$ProcessId = 12345
$Samples = 120
$IntervalSeconds = 1

1..$Samples | ForEach-Object {
    $p = Get-Process -Id $ProcessId -ErrorAction Stop
    [pscustomobject]@{
        TimestampUtc       = [DateTimeOffset]::UtcNow.ToString("O")
        ProcessId          = $p.Id
        WorkingSet64       = $p.WorkingSet64
        PrivateMemory64    = $p.PrivateMemorySize64
        VirtualMemory64    = $p.VirtualMemorySize64
        HandleCount        = $p.HandleCount
        ThreadCount        = $p.Threads.Count
    }
    Start-Sleep -Seconds $IntervalSeconds
} | Export-Csv -NoTypeInformation -Encoding utf8 `
    reports/performance/memory/process_samples.csv
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cible :** le PID évite de mélanger plusieurs exécutions.
- **Compteurs :** working set, mémoire privée et mémoire virtuelle restent distincts.
- **Contexte :** handles et threads peuvent révéler une autre croissance de ressources.
- **Cadence :** la fenêtre est bornée par nombre d’échantillons et intervalle.

## 19. Phases et plateaux

Chaque cycle doit laisser un temps de stabilisation après la sortie d’une zone. Une baisse différée peut être normale ; une croissance du plateau après chaque cycle mérite une attribution.

> **[LECTURE] Contrat de phases — Ne pas exécuter.**

```yaml
cycle:
  - phase: hub_enter
    settle_seconds: 5
  - phase: combat_enter
    settle_seconds: 3
  - phase: combat_play
    duration_seconds: 60
  - phase: combat_exit
    settle_seconds: 5
  - phase: hub_return
    settle_seconds: 10
  - phase: idle_plateau
    duration_seconds: 30
comparison_points:
  - combat_enter_peak
  - combat_play_p95
  - idle_plateau_median
  - idle_plateau_end
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Stabilisation :** les délais empêchent de mesurer uniquement une transition.
- **Pic :** l’entrée en combat possède un point de comparaison dédié.
- **Plateau :** la médiane et la fin de repos détectent une dérive.
- **Répétition :** les mêmes points sont extraits à chaque cycle.

## 20. Analyser une croissance par cycle

> **[VSC] Visual Studio Code — Créer `tools/performance/analyze_memory_cycles.py`.**

```python
from __future__ import annotations

import csv
import math
from collections import defaultdict
from pathlib import Path

SOURCE = Path("reports/performance/memory/process_samples.csv")

def linear_slope(values: list[float]) -> float:
    if len(values) < 2:
        raise ValueError("Au moins deux cycles sont requis")
    n = len(values)
    xs = list(range(n))
    mean_x = sum(xs) / n
    mean_y = sum(values) / n
    numerator = sum((x - mean_x) * (y - mean_y)
                    for x, y in zip(xs, values))
    denominator = sum((x - mean_x) ** 2 for x in xs)
    if denominator == 0:
        raise ValueError("Cycles non distincts")
    return numerator / denominator

def ensure_finite(values: list[float]) -> None:
    if not values or not all(math.isfinite(value) for value in values):
        raise ValueError("Série vide ou non finie")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pente :** la régression simple quantifie une tendance par cycle.
- **Minimum :** deux cycles sont insuffisants pour une conclusion robuste mais évitent un calcul impossible.
- **Validation :** les valeurs non finies sont refusées.
- **Unité :** la pente conserve l’unité de la série, à documenter dans le rapport.

## 21. Comparer pics et plateaux

> **[VSC] Visual Studio Code — Compléter l’analyse Python.**

```python
def percentile(values: list[float], ratio: float) -> float:
    ordered = sorted(values)
    if not ordered:
        raise ValueError("Série vide")
    index = min(len(ordered) - 1,
                max(0, math.ceil(ratio * len(ordered)) - 1))
    return ordered[index]

def summarize(values: list[float]) -> dict[str, float]:
    ensure_finite(values)
    ordered = sorted(values)
    middle = len(ordered) // 2
    median = (
        ordered[middle]
        if len(ordered) % 2
        else (ordered[middle - 1] + ordered[middle]) / 2
    )
    return {
        "median": median,
        "p95": percentile(ordered, 0.95),
        "p99": percentile(ordered, 0.99),
        "maximum": max(ordered),
        "minimum": min(ordered),
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Distribution :** médiane, p95, p99 et maximum décrivent centre et queue.
- **Méthode :** le percentile nearest-rank est explicite.
- **Reproductibilité :** la même fonction analyse baseline et candidate.
- **Limite :** les statistiques n’attribuent pas la cause de la croissance.

## 22. Définir un critère de fuite

Une fuite ne se déclare pas au seul fait qu’un maximum augmente. Le critère combine croissance de plateau, répétition, absence de récupération et attribution.

> **[LECTURE] Porte de suspicion de fuite — Ne pas interpréter comme mesure.**

```yaml
leak_suspicion:
  minimum_measured_cycles: 20
  compare_phase: idle_plateau_end
  signals:
    private_memory_slope_mib_per_cycle: measured
    static_memory_slope_mib_per_cycle: measured
    object_count_slope_per_cycle: measured
    orphan_node_count_slope_per_cycle: measured
    video_memory_slope_mib_per_cycle: measured
  gates:
    repeated_positive_growth: required
    recovery_window_observed: required
    scenario_errors_absent: required
    attribution_started: required
  decision: pending_human_review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Durée :** un nombre minimal de cycles évite une conclusion depuis une courte chauffe.
- **Phase :** les fins de plateau sont comparées entre elles.
- **Signaux :** mémoire et objets sont rapprochés sans être confondus.
- **Décision :** la suspicion reste soumise à revue et attribution.

## 23. Durée de vie des nœuds

Un nœud retiré de l’arbre n’est pas nécessairement détruit. `queue_free()` programme sa libération sûre ; une référence conservée par un gestionnaire peut maintenir d’autres objets accessibles.

> **[VSC] Visual Studio Code — Libérer une instance de gameplay.**

```gdscript
func retire_enemy(enemy: Node) -> void:
    if not is_instance_valid(enemy):
        return
    enemy.set_process(false)
    enemy.set_physics_process(false)
    enemy.queue_free()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Validation :** la fonction ignore une instance déjà invalide.
- **Arrêt :** les traitements sont coupés avant la libération différée.
- **Libération :** `queue_free()` respecte le cycle de l’arbre.
- **Références :** les collections externes doivent aussi retirer l’ennemi.

## 24. Registre sans rétention involontaire

> **[VSC] Visual Studio Code — Utiliser des références faibles dans un registre d’observation.**

```gdscript
class_name WeakNodeRegistry
extends RefCounted

var _entries: Dictionary[int, WeakRef] = {}

func track(node: Node) -> void:
    _entries[node.get_instance_id()] = weakref(node)

func resolve(instance_id: int) -> Node:
    var ref: WeakRef = _entries.get(instance_id)
    if ref == null:
        return null
    var value := ref.get_ref()
    if value == null:
        _entries.erase(instance_id)
        return null
    return value as Node

func prune() -> void:
    for instance_id in _entries.keys():
        resolve(instance_id)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Clé :** l’identifiant sert à retrouver l’entrée sans référence forte directe.
- **Faible :** `WeakRef` ne prolonge pas volontairement la durée de vie.
- **Nettoyage :** les références mortes sont supprimées lors de la résolution ou de l’élagage.
- **Usage :** ce modèle convient à l’observation, pas à un propriétaire fonctionnel.

## 25. Connexions de signaux et propriétaires

Une connexion peut prolonger ou compliquer la durée de vie si le propriétaire fonctionnel reste global. Le diagnostic documente qui connecte, qui déconnecte et quel objet possède l’abonnement.

> **[VSC] Visual Studio Code — Encadrer un abonnement.**

```gdscript
var _subscribed := false

func activate(bus: Node) -> void:
    if _subscribed:
        return
    bus.event_emitted.connect(_on_event_emitted)
    _subscribed = true

func deactivate(bus: Node) -> void:
    if not _subscribed:
        return
    if bus.event_emitted.is_connected(_on_event_emitted):
        bus.event_emitted.disconnect(_on_event_emitted)
    _subscribed = false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Idempotence :** l’activation ne crée pas plusieurs connexions.
- **Déconnexion :** la sortie retire explicitement l’abonnement.
- **État :** le booléen rend le contrat observable.
- **Responsabilité :** l’appelant doit garantir que `deactivate()` accompagne la fin de vie logique.

## 26. Ressources RefCounted

Les ressources dérivées de `RefCounted` sont libérées lorsque plus aucune référence forte ne les conserve. Les singletons, dictionnaires, callbacks et caches sont donc des suspects naturels.

> **[LECTURE] Carte de propriété d’une ressource — Ne pas saisir.**

```yaml
resource_lifetime:
  path: res://data/items/sword.tres
  owners:
    - inventory_catalog
    - equipped_item
    - ui_preview_cache
  expected_release:
    inventory_catalog: application_shutdown
    equipped_item: unequip
    ui_preview_cache: lru_eviction
  duplicate_policy:
    shared_read_only: preferred
    mutable_runtime_copy: explicit
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Propriétaires :** chaque référence forte attendue est nommée.
- **Échéance :** la fin de vie diffère selon le rôle.
- **Cache :** l’éviction devient un événement attendu.
- **Duplication :** une copie mutable doit être explicite.

## 27. Duplications explicites

Une copie profonde de ressources, tableaux ou dictionnaires peut multiplier l’empreinte. Le rapport doit distinguer partage intentionnel, copie de configuration et état runtime mutable.

> **[VSC] Visual Studio Code — Déclarer une copie runtime.**

```gdscript
func create_runtime_state(template: Resource) -> Resource:
    var runtime_state := template.duplicate(true)
    runtime_state.set_meta("source_path", template.resource_path)
    runtime_state.set_meta("copy_reason", "mutable_runtime_state")
    return runtime_state
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Copie :** `duplicate(true)` produit une copie profonde volontaire.
- **Provenance :** le chemin source reste attaché à la copie.
- **Justification :** la raison distingue copie nécessaire et duplication accidentelle.
- **Contrôle :** le nombre de copies doit être mesuré dans la campagne.

## 28. Cache borné LRU

> **[VSC] Visual Studio Code — Créer `res://src/core/cache/bounded_lru_cache.gd`.**

```gdscript
class_name BoundedLruCache
extends RefCounted

var _capacity: int
var _values: Dictionary = {}
var _order: Array[Variant] = []

func _init(capacity: int) -> void:
    _capacity = maxi(1, capacity)

func get_value(key: Variant) -> Variant:
    if not _values.has(key):
        return null
    _order.erase(key)
    _order.push_back(key)
    return _values[key]

func put(key: Variant, value: Variant) -> void:
    if _values.has(key):
        _order.erase(key)
    _values[key] = value
    _order.push_back(key)
