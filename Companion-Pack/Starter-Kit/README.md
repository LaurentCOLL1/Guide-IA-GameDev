---
title: "Companion Pack — Starter Kit"
id: "CP-PACK-01-STARTER-KIT"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-30T04:19:00+02:00"
validation-status: "runtime-tested-linux"
validation-report: "Companion-Pack/Starter-Kit/qa/AUDIT-STARTER-KIT.md"
redistribution-status: "pending-global-license"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
---

# Starter Kit

Le Starter Kit matérialise la base minimale de `Project Asteria`. Il fournit un projet Godot 3D sans extension tierce, une scène de bootstrap, un rapport structuré, deux profils d’environnement et des validations reproductibles.

## État du lot

| Élément | État |
|---|---|
| projet Godot et scène principale | matérialisés |
| validation statique Python | matérialisée |
| enveloppe PowerShell | matérialisée |
| test GDScript autonome | matérialisé |
| exécution Linux headless | validée par le run `30508086899` |
| lancement graphique virtuel Linux | validé sous Xvfb avec Compatibility |
| ouverture Windows graphique | non exécutée |
| rendu Forward+ graphique | non exécuté |
| export Windows ou Linux | non produit |
| clone neuf indépendant | validé par le run `30508086899` |
| licence globale | non décidée |

Une validation headless réussie ne prouvera pas la qualité visuelle, la compatibilité GPU AMD, l’export ni l’expérience d’édition sous Windows.

## Arborescence

```text
Starter-Kit/
├── godot-project/
│   ├── project.godot
│   ├── src/core/bootstrap_report.gd
│   ├── src/features/bootstrap/main.gd
│   ├── src/features/bootstrap/main.tscn
│   ├── tests/run_tests.gd
│   └── tools/
├── environments/
│   ├── solo/profile.json
│   └── studio/profile.json
├── qa/
├── DEPENDENCIES.json
├── LICENSE-STATUS.md
├── PROVENANCE.json
└── manifest.json
```

Le projet reste volontairement petit. Les bibliothèques IA, bases de données, systèmes de gameplay, exports et contenus lourds appartiennent aux packs suivants.

## Prérequis

- Godot Engine Standard `4.7.1-stable` pour ouvrir et exécuter le projet ;
- Python `3.10` ou plus récent pour le validateur statique, sans paquet tiers ;
- PowerShell 7 uniquement pour l’enveloppe Windows facultative ;
- Git pour conserver les changements et vérifier les fichiers ignorés.

Godot `4.7.1-stable` est l’unique dépendance runtime de ce lot. Aucun addon, modèle, service réseau ou secret n’est requis.

## Validation statique

Depuis `Companion-Pack/Starter-Kit/godot-project` :

```powershell
python .\tools\validate_project.py --report .\validation-static.json
```

Le validateur contrôle les fichiers obligatoires, les profils JSON, la scène principale, les chemins GDScript, les exclusions Git et l’absence d’artefacts interdits.

## Import headless

```powershell
& $env:GODOT_EXE --headless --path . --import
```

Cette commande importe et analyse les ressources. Elle ne valide ni Forward+ graphique ni les exports.

## Démarrage headless

```powershell
& $env:GODOT_EXE `
  --headless `
  --path . `
  --quit-after 5 `
  --log-file .\bootstrap-smoke.log
```

La sortie attendue contient l’identifiant `CP-SK-BOOTSTRAP-001` et un objet JSON produit par `BootstrapReport`.

## Tests GDScript

```powershell
& $env:GODOT_EXE `
  --headless `
  --path . `
  --script res://tests/run_tests.gd `
  --log-file .\starter-kit-tests.log
```

Le run `30508086899` a retourné `0` et affiché `STARTER_KIT_TESTS: PASS`. Cette preuve couvre Godot Linux x86_64 en mode Compatibility, pas Forward+ sur GPU réel.

## Profils Solo et Studio

Les fichiers `environments/solo/profile.json` et `environments/studio/profile.json` modifient la gouvernance, les plateformes exigées et l’approbation de release. Ils ne créent pas deux domaines métier différents.

Le profil Solo conserve Windows comme plateforme obligatoire initiale et autorise l’auto-revue. Le profil Studio ajoute Linux, une revue indépendante et des responsabilités séparées. Dans les deux cas, l’IA locale reste facultative.

## Contrat `BootstrapReport`

Le rapport expose un dictionnaire stable avec :

- `schema_version` ;
- `validation_id` ;
- `project_id` ;
- `profile_id` ;
- `engine_version` ;
- `renderer` ;
- `checks`.

Il décrit le démarrage observé. Il n’est pas une source d’autorité gameplay et ne modifie aucun état persistant.

## Nettoyage

Les éléments suivants peuvent être supprimés sans perdre les sources :

```powershell
Remove-Item -Recurse -Force .\.godot -ErrorAction SilentlyContinue
Remove-Item -Force .\*.log, .\validation-static.json -ErrorAction SilentlyContinue
```

La suppression de `.godot/` force un nouvel import. Les fichiers sous `src/`, `tests/`, `data/`, `docs/` et `environments/` ne sont pas des caches.

## Provenance et redistribution

Tous les fichiers du Starter Kit sont originaux et textuels. Aucun binaire Godot, asset tiers, modèle, voix, donnée personnelle ou secret n’est distribué. Le moteur doit être récupéré depuis la [publication officielle Godot 4.7.1](https://godotengine.org/article/maintenance-release-godot-4-7-1/).

La licence globale du dépôt n’étant pas encore décidée, [LICENSE-STATUS.md](LICENSE-STATUS.md) n’accorde pas de droit de redistribution autonome. Cette réserve doit être fermée avant une archive publique du Companion Pack.

## Références internes

- [Créer le projet fil rouge](../../Livre-II/CHAPITRE-01-Decouvrir-Godot-et-creer-le-projet-fil-rouge.md)
- [Architecture modulaire](../../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md)
- [Services et composition](../../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md)
- [Données et configurations](../../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md)
- [Tests et simulations](../../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md)
- [Architecture Solo et Studio](../../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md)
