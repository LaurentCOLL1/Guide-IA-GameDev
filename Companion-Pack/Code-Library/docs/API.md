# API publique

Le registre canonique est `catalog.json`. Les signatures ci-dessous sont stables pour la version 1.x ; les extensions doivent rester additives ou passer par une nouvelle version majeure.

## Collections

### Python — `StableUniqueList`

- `add(key, value) -> bool` : ajoute une valeur si la clé est absente ;
- `replace(key, value) -> bool` : remplace une valeur existante sans déplacer sa position ;
- `remove(key) -> bool` ;
- `values() -> list` : copie défensive de l’ordre courant.

### GDScript — `StableUniqueList`

Contrat équivalent avec `add`, `replace`, `remove`, `values` et `size`.

## Validation

### Python — `ValidationIssue`, `ValidationResult`, `Validator`

Une règle reçoit une valeur et retourne `None`, une `ValidationIssue` ou une séquence d’issues. `ValidationResult.is_valid` est vrai lorsqu’aucune erreur n’est présente.

### GDScript — `ValidationIssue`, `ValidationResult`, `Validator`

Les règles sont des `Callable`. Une règle retourne `null`, une issue ou un tableau d’issues.

## Sérialisation

### Python — `to_primitive`, `canonical_json_dumps`

Convertit dataclasses, mappings, séquences et ensembles vers des primitives JSON. Les clés sont triées ; les valeurs non finies sont refusées.

### GDScript — `CanonicalJson`

`CanonicalJson.encode(value)` trie récursivement les dictionnaires avant `JSON.stringify`.

## Services

### Python et GDScript — `ServiceRegistry`

`register`, `resolve`, `contains`, `remove`. Le remplacement exige `replace=true`; aucun singleton global n’est créé.

## Repositories

### Python et GDScript — `InMemoryRepository`

`save`, `get_by_id`, `contains`, `remove`, `list_ids`, `clear`. Les tableaux et dictionnaires sont copiés afin d’éviter une mutation externe silencieuse.

## Machines à états

### Python et GDScript — `StateMachine`

`add_transition`, `can_trigger`, `trigger`, `current_state`. Une transition inconnue échoue sans modifier l’état.

## Interactions

### Python et GDScript — `InteractionRouter`

`register`, `dispatch`, `contains`. Le résultat est explicite : succès avec valeur, ou échec avec code d’erreur.

## Conversions

### Python

`clamp_float`, `seconds_to_milliseconds`, `milliseconds_to_seconds`, `parse_bool`.

### GDScript — `ValueConversions`

Méthodes statiques équivalentes. Les conversions de temps rejettent les valeurs négatives.

## Aides de test

### Python — `ManualClock`, `EventRecorder`

Horloge contrôlable et enregistreur d’événements sans attente réelle.

### GDScript — `TestProbe`

`record`, `count`, `last`, `clear` pour les assertions de tests Godot.
