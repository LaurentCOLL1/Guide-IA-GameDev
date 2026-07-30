---
title: "Companion Pack — Code Library"
id: "CP-PACK-04-CODE-LIBRARY"
status: "candidate"
version: "0.1.0"
lang: "fr-FR"
validation-status: "candidate"
redistribution-status: "pending-global-license"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  language: "GDScript"
---

# Code Library

Le Pack 4 fournit un catalogue resserré de composants réutilisables en Python et GDScript. Chaque composant possède un identifiant de concept, une API publique documentée, des tests et une décision explicite de non-duplication.

## Composants

| Domaine | Python | GDScript |
|---|---|---|
| collection ordonnée sans doublon | `StableUniqueList` | `StableUniqueList` |
| validation composée | `Validator`, `ValidationResult` | `Validator`, `ValidationResult` |
| sérialisation canonique | `canonical_json_dumps` | `CanonicalJson` |
| registre de services | `ServiceRegistry` | `ServiceRegistry` |
| repository mémoire | `InMemoryRepository` | `InMemoryRepository` |
| machine à états | `StateMachine` | `StateMachine` |
| routage d’interactions | `InteractionRouter` | `InteractionRouter` |
| conversions bornées | fonctions de conversion | `ValueConversions` |
| aides de test | `ManualClock`, `EventRecorder` | `TestProbe` |

## Principes

- aucune architecture globale imposée ;
- aucune dépendance Python tierce ;
- aucune copie de code issue des autres packs ;
- file bornée et cache TTL restent propriétaires de l’AI Library ;
- bootstrap et composition de projet restent propriétaires des Project Templates et du Starter Kit ;
- les implémentations Python et GDScript d’un même concept sont des ports parallèles déclarés, pas des doublons accidentels.

## Validation candidate

La PR doit exécuter la validation statique, les tests Python, l’import Godot, un démarrage headless, un démarrage Xvfb Compatibility, les tests GDScript et le contrôle d’un arbre Git propre. Aucun résultat n’est revendiqué avant les runs consultables.

Voir [API.md](docs/API.md), [DUPLICATE-POLICY.md](docs/DUPLICATE-POLICY.md) et [INTEGRATION.md](docs/INTEGRATION.md).
