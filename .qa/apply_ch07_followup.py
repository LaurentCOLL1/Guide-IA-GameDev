#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
chapter_path = ROOT / "Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md"
audit_path = ROOT / "Livre-II/QA/AUDIT-CHAPITRE-07.md"

chapter = chapter_path.read_text(encoding="utf-8")
chapter = chapter.replace(
'''func update_cooldown(delta: float) -> void:
	runtime_state.remaining_cooldown = maxf(
		runtime_state.remaining_cooldown - delta,
		0.0
	)
```

`delta` représente le temps écoulé. `maxf(..., 0.0)` empêche une durée négative. La Resource reste inchangée.''',
'''func update_cooldown(delta: float) -> void:
	runtime_state.tick(delta)
```

`delta` représente le temps écoulé. La méthode `tick()` soustrait cette durée de `cooldown_remaining` et utilise `maxf()` pour empêcher une valeur négative. La Resource reste inchangée.'''
)
chapter = chapter.replace(
'''profile.is_active = true
ResourceSaver.save(profile, "res://data/beacons/beacon_training.tres")''',
'''profile.enabled_by_default = false
ResourceSaver.save(profile, "res://data/beacons/beacon_training.tres")'''
)
chapter = chapter.replace(
'''var runtime_state := BeaconRuntimeState.new()
runtime_state.is_active = true
runtime_state.remaining_cooldown = profile.cooldown_seconds''',
'''var runtime_state := BeaconRuntimeState.new(profile)
runtime_state.record_activation(profile.cooldown_seconds)'''
)
chapter = chapter.replace(
'''var profile := BeaconJsonMapper.to_profile(data)
if profile == null:
	return

catalog.add_profile(profile)
activation_service.configure(event_bus, catalog)''',
'''var mapper := BeaconJsonMapper.new()
var profile := mapper.from_dictionary(data)
if profile == null:
	return

catalog.register(profile)
activation_service.configure(event_bus, catalog)'''
)
chapter = chapter.replace(
'if not raw_radius is float and not raw_radius is int:',
'if not (raw_radius is float or raw_radius is int):'
)
chapter_path.write_text(chapter, encoding="utf-8")

audit = audit_path.read_text(encoding="utf-8")
audit = audit.replace(
'''### Risque 18 — erreurs fréquentes sans exemples concrets

**Correction :** chaque erreur de la section 35 possède maintenant un exemple fautif, un exemple corrigé et une explication de la différence.''',
'''### Risque 18 — erreurs fréquentes sans exemples concrets

**Correction :** chaque erreur de la section 35 possède maintenant un exemple fautif, un exemple corrigé et une explication de la différence.

### Risque 19 — exemples corrigés incompatibles avec les contrats déjà définis

**Correction :** seconde relecture des noms publics : utilisation de `cooldown_remaining`, `tick()`, `record_activation()`, du constructeur `BeaconRuntimeState.new(profile)`, de `BeaconJsonMapper.from_dictionary()` sur une instance et de `BeaconCatalog.register()`.'''
)
audit_path.write_text(audit, encoding="utf-8")
print("Corrections de cohérence du chapitre 7 appliquées.")
