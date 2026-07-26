  capacity_before: measured
  capacity_after: proposed
  eviction_policy: lru
  hit_rate: measured
  rebuild_cost_ms: measured
  memory_peak_mib: measured
  rollback: defined
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** mémoire, efficacité du cache et coût de reconstruction sont évalués ensemble.

### 40.4 Créer un pool sans limite

**Symptôme ou risque :** Le nombre d’objets inactifs augmente après chaque combat.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```gdscript
func release(projectile: Node) -> void:
    idle_projectiles.push_back(projectile)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le pool conserve indéfiniment chaque instance et ses ressources.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au contrat du projet.**

```gdscript
func release(projectile: Node) -> void:
    projectile.prepare_for_pool()
    if idle_projectiles.size() >= maximum_idle:
        projectile.queue_free()
        return
    idle_projectiles.push_back(projectile)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** la taille inactive est bornée et le surplus est libéré.

### 40.5 Supprimer un nœud de l’arbre sans le libérer

**Symptôme ou risque :** Le nœud disparaît visuellement mais le nombre d’objets continue de croître.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```gdscript
func retire(node: Node) -> void:
    remove_child(node)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** `remove_child()` ne détruit pas le nœud et aucune autre propriété n’est définie.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au contrat du projet.**

```gdscript
func retire(node: Node) -> void:
    if is_instance_valid(node):
        node.queue_free()
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** la fin de vie est explicite et compatible avec le cycle de l’arbre.

### 40.6 Dupliquer toutes les ressources runtime

**Symptôme ou risque :** Chaque instance de personnage possède ses propres matériaux et données immuables.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```gdscript
func spawn(template: Resource) -> Resource:
    return template.duplicate(true)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** la copie profonde est appliquée sans besoin de mutabilité ni mesure.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au contrat du projet.**

```gdscript
func spawn(template: Resource, needs_mutation: bool) -> Resource:
    if not needs_mutation:
        return template
    var copy := template.duplicate(true)
    copy.set_meta("copy_reason", "runtime_mutation")
    return copy
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** les ressources immuables sont partagées et les copies nécessaires sont traçables.

### 40.7 Mesurer la VRAM avec un seul compteur

**Symptôme ou risque :** Le compteur du moteur reste sous le budget, mais le pilote sature.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
vram:
  engine_video_mem_bytes: measured
  driver_view: absent
  other_processes: ignored
  decision: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** l’indicateur du moteur n’inventorie pas nécessairement le pilote et les autres processus.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au contrat du projet.**

```yaml
vram:
  engine_texture_mem_bytes: measured
  engine_buffer_mem_bytes: measured
  engine_video_mem_bytes: measured
  system_or_driver_view: recorded
  resolution_and_profile: recorded
  decision: pending_review
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** plusieurs vues compatibles et le contexte graphique soutiennent la décision.

### 40.8 Réduire la mémoire en cassant la qualité

**Symptôme ou risque :** Les textures sont réduites et le budget est respecté, mais les interfaces deviennent illisibles.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
candidate:
  vram_peak: lower
  texture_resolution: reduced_globally
  visual_review: absent
  accessibility_review: absent
  decision: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le gain mémoire ignore la qualité visuelle et l’accessibilité.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au contrat du projet.**

```yaml
candidate:
  vram_peak: measured
  texture_policy: per_asset_class
  reference_images: compared
  ui_legibility: passed
  accessibility_review: passed
  rollback: defined
  decision: pending_human_approval
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** le budget, les catégories d’assets et la qualité sont contrôlés ensemble.

### 40.9 Nettoyer seulement à la fermeture

**Symptôme ou risque :** La session courte semble stable, mais la mémoire croît entre les transitions.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```gdscript
func _notification(what: int) -> void:
    if what == NOTIFICATION_WM_CLOSE_REQUEST:
        cache.clear()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** le nettoyage final ne traite pas les échéances fonctionnelles pendant la session.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au contrat du projet.**

```yaml
lifetime_policy:
  encounter_cache: combat_exit
  preview_cache: lru_eviction
  chapter_resources: chapter_exit
  global_catalog: application_shutdown
  long_run_validation: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** chaque famille possède une échéance cohérente et vérifiable en longue durée.

### 40.10 Déclarer le succès après un pic plus bas

**Symptôme ou risque :** Le maximum baisse, mais le plateau et le nombre d’orphelins augmentent.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
result:
  ram_peak_mib: lower
  idle_plateau_slope: ignored
  orphan_nodes: ignored
  functional_suite: absent
  decision: accepted
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Erreur :** un seul maximum masque une dérive persistante et l’absence de garde fonctionnelle.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au contrat du projet.**

```yaml
result:
  ram_peak_mib: measured
  vram_peak_mib: measured
  idle_plateau_slope: measured
  orphan_nodes_end: measured
  long_run: passed
  functional_suite: passed
  visual_quality: passed
  decision: pending_human_approval
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Correction :** pics, dérive, objets, longue durée et régressions soutiennent la décision.

## 41. Modes Solo et Studio

### Mode Solo

- figer le scénario et les budgets avant mesure ;
- conserver les échantillons bruts et les captures ;
- écrire l’hypothèse avant de modifier cache ou durée de vie ;
- limiter le changement à une cause principale ;
- séparer profilage, correction et revue dans le temps ;
- exécuter un test de longue durée après le test court ;
- conserver un retour arrière simple ;
- vérifier fonctionnel et qualité avant acceptation.

### Mode Studio

- **QA performance :** possède scénarios, campagnes, budgets et artefacts ;
- **programmeur moteur :** attribue allocations, ressources et caches ;
- **programmeur gameplay :** corrige propriétaires, pools et temporaires ;
- **art technique :** qualifie textures, formats, mipmaps et qualité ;
- **référent plateforme :** documente RAM, VRAM, fichier d’échange et outils système ;
- **QA fonctionnelle :** vérifie transitions, sauvegardes et comportement ;
- **tech lead :** arbitre budget, dette et risque ;
- **release owner :** conserve l’autorité de promotion.

Une correction critique gagne à être reproduite par une seconde personne ou un scénario automatisé. La personne qui propose une limite de cache ne devrait pas être l’unique autorité de son acceptation.

## 42. Checklist d’acceptation

### Contrat

- [ ] plateforme, build, renderer, résolution et profil déclarés ;
- [ ] budgets souples et durs versionnés ;
- [ ] cycle, phases, warm-up, cadence et durée définis ;
- [ ] compteurs et unités documentés ;
- [ ] exclusions définies avant mesure.

### Mesure

- [ ] échantillons RAM, processus, objets et VRAM conservés ;
- [ ] pics, médiane, p95, p99 et plateaux calculés ;
- [ ] croissance par cycle analysée ;
- [ ] fenêtres de récupération observées ;
- [ ] coût du collecteur déclaré ;
- [ ] captures et inventaires liés au scénario.

### Changement

- [ ] hypothèse et propriétaire écrits ;
- [ ] variable principale isolée ;
- [ ] échéances de libération explicites ;
- [ ] cache ou pool borné ;
- [ ] duplication justifiée ;
- [ ] retour arrière défini.

### Produit

- [ ] test de longue durée réussi ;
- [ ] suite fonctionnelle réussie ;
- [ ] qualité visuelle et accessibilité préservées ;
- [ ] chargements et temps de frame non dégradés hors critères ;
- [ ] décision humaine enregistrée ;
- [ ] aucune valeur runtime inventée.

## 43. Critère d’acceptation du pilote

Le chapitre sera validé au niveau runtime lorsque `Project Asteria` disposera d’au moins une campagne mémoire matérialisée répondant simultanément aux conditions suivantes :

1. budgets RAM et VRAM qualifiés pour une plateforme ;
2. scénario cyclique et manifeste d’environnement versionnés ;
3. baseline avec échantillons moteur et système conservés ;
4. pic ou croissance attribué à une famille de propriétaires ;
5. hypothèse écrite avant modification ;
6. candidate mesurée avec le même contrat ;
7. réduction soutenue par pics, plateaux et pente ;
8. test de longue durée réussi ;
9. tests fonctionnels et qualité visuelle satisfaits ;
10. rapport, rollback et approbation humaine conservés.

## 44. Synthèse opérationnelle pour Project Asteria

- `config/performance/memory_budgets.yaml` pour les limites par plateforme ;
- `config/performance/memory_campaign.yaml` pour le scénario cyclique ;
- `config/performance/memory_environment.yaml` pour l’environnement ;
- `config/performance/memory_soak_test.yaml` pour la longue durée ;
- `res://src/core/performance/` pour sondes et échantillonnage borné ;
- `res://src/core/cache/` pour les caches versionnés et bornés ;
- `tools/performance/` pour l’analyse des séries ;
- `reports/performance/memory/` pour données brutes, résumés et comparaisons ;
- une porte humaine reliant budget, stabilité, fonctionnel et qualité.

Aucun de ces artefacts n’est présenté comme matérialisé. Le chapitre fournit des contrats prêts à être intégrés, exécutés et audités.

## 45. Références techniques

- [Godot 4.7 — Performance](https://docs.godotengine.org/en/4.7/classes/class_performance.html)
- [Godot 4.7 — OS](https://docs.godotengine.org/en/4.7/classes/class_os.html)
- [Godot 4.7 — RenderingServer](https://docs.godotengine.org/en/4.7/classes/class_renderingserver.html)
- [Godot — Optimisation générale](https://docs.godotengine.org/en/stable/tutorials/performance/general_optimization.html)
- [Godot 4.7 — WeakRef](https://docs.godotengine.org/en/4.7/classes/class_weakref.html)
- [Godot 4.7 — RefCounted](https://docs.godotengine.org/en/4.7/classes/class_refcounted.html)
- [Godot 4.7 — Resource](https://docs.godotengine.org/en/4.7/classes/class_resource.html)
- [Godot 4.7 — Node](https://docs.godotengine.org/en/4.7/classes/class_node.html)

## 46. Conclusion

L’optimisation mémoire est une discipline de durée de vie et de preuve. Les budgets orientent l’enquête ; les cycles, plateaux, propriétaires et séries temporelles montrent ce qui reste réellement en mémoire. Un cache, un pool ou une duplication n’est ni bon ni mauvais par nature : sa finalité, sa limite, son coût de reconstruction et son point de libération doivent être mesurés.

Pour `Project Asteria`, l’objectif est un produit qui reste sous ses budgets après des transitions répétées et une longue session, sans sacrifier stabilité, fonctionnalité, qualité visuelle ni maintenabilité.
