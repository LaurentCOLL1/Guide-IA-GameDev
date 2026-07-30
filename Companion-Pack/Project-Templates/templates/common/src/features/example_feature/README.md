# Module example_feature

## Responsabilité

Démontrer la structure minimale d’une fonctionnalité sans imposer une règle métier au projet réel.

## Interface publique

- `ExampleRecord` ;
- `ExampleService.create_record()` ;
- `InMemoryExampleRepository`.

## Dépendances autorisées

- classes Godot standard ;
- types du module ;
- contrats de `src/core` réellement communs.

## Dépendances interdites

- chemin de scène absolu ;
- Autoload implicite ;
- accès direct à une base ou un service réseau depuis le domaine ;
- mutation interne d’un autre module.
