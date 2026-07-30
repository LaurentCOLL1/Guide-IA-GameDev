---
title: "Companion Pack — Code Library"
id: "CP-PACK-04-CODE-LIBRARY"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
validation-status: "runtime-tested-linux"
redistribution-status: "global-policy-defined"
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

## Qualification obtenue

Le run `30517143131` a validé 64 fichiers sources du pack, 18 composants et 9 concepts, puis exécuté 16 tests Python. Godot `4.7.1.stable.official.a13da4feb` a importé l’exemple, exécuté les démarrages headless et Xvfb Compatibility, puis obtenu `CODE_LIBRARY_GODOT_TESTS: PASS`. L’arbre Git est resté propre après runtime.

La CI refuse explicitement tout journal contenant `SCRIPT ERROR`, même lorsque le processus Godot retourne un code de succès.

Archive Godot Linux SHA-256 : `c7ff14fd28472c8d4f193043de30278dcf7e5241a1dcf7566b02e27addaa33ba`.

La qualification ne mesure ni performance ni charge et ne couvre pas Windows graphique, Forward+ sur GPU réel, export ou redistribution autonome.

Voir [API.md](docs/API.md), [DUPLICATE-POLICY.md](docs/DUPLICATE-POLICY.md) et [INTEGRATION.md](docs/INTEGRATION.md).
