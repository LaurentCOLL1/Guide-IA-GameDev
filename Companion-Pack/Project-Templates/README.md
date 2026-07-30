---
title: "Companion Pack — Project Templates"
id: "CP-PACK-02-PROJECT-TEMPLATES"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
last-verified: "2026-07-30T05:34:00+02:00"
validation-status: "runtime-tested-linux"
validation-report: "Companion-Pack/Project-Templates/qa/AUDIT-PROJECT-TEMPLATES.md"
redistribution-status: "pending-global-license"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
---

# Project Templates

Le Pack 2 fournit deux modèles composables de projet Godot : **Solo** et **Studio**. Les deux partagent le même cœur technique, les mêmes frontières de module, les mêmes tests minimaux et les mêmes conventions de nommage. Ils diffèrent par leur gouvernance, leur profondeur de revue et leurs responsabilités.

## État du lot

| Élément | État |
|---|---|
| modèle Solo | matérialisé |
| modèle Studio | matérialisé |
| générateur de projet | matérialisé |
| générateur de module Godot | matérialisé |
| conventions Git | matérialisées |
| modèles d’issues et de PR | matérialisés |
| ADR et responsabilités | matérialisés |
| paramètres VS Code et style | matérialisés |
| création de projets neufs | validée par le run `30511425269` |
| import et tests Godot | validés sur Linux x86_64 par le run `30511425269` |
| protection de branche réelle | non appliquée |
| CODEOWNERS effectif sur un dépôt cible | non vérifié |
| licence globale | non décidée |

Les fichiers de gouvernance sont des **modèles de départ**. Leur présence ne prouve ni une protection de branche active, ni une revue obligatoire, ni l’application d’un CODEOWNERS par GitHub.

## Qualification obtenue

Le run `30511425269` a instancié les profils Solo et Studio, créé un module en cinq couches dans chacun, initialisé leurs dépôts Git, importé les deux projets avec Godot `4.7.1.stable.official.a13da4feb`, exécuté les démarrages headless et Xvfb Compatibility, puis obtenu `PROJECT_TEMPLATE_TESTS: PASS` pour les deux profils. Les arbres Git sont restés propres après runtime.

La génération statique est déterministe pour des entrées identiques :

- projet Solo : `61f2286f90dbaad1375ac201eeecfff85f65eecd25967799a126e6d1cdbe2896` ;
- projet Studio : `43d49d1e9b06a16f2f822217111a7d1ca49a759b7390a2f7b86adfe604dd4f57` ;
- module Solo : `0662f720c8880a4726fb5139ca247f692ae7b283620d32a6f46c2ac6975d471a` ;
- module Studio : `6a48c5014cfffdbe8645a5959294ae90d408e6f81fba4584afa2e86da5328cf7`.

Cette qualification ne rend pas les politiques GitHub effectives et ne constitue pas une revue visuelle du rendu Xvfb.

## Prérequis

- Python `3.10` ou plus récent, sans paquet tiers ;
- Godot Engine Standard `4.7.1-stable` pour importer et exécuter les projets générés ;
- PowerShell 7 uniquement pour l’enveloppe Windows facultative ;
- Git pour initialiser le dépôt produit et appliquer les politiques choisies.

## Créer un projet Solo

Depuis `Companion-Pack/Project-Templates` :

```powershell
python .\tools\instantiate_project.py `
  --profile solo `
  --project-name "Mon Projet Solo" `
  --project-id mon_projet_solo `
  --owner-handle mon-compte `
  --output .\work\mon-projet-solo
```

Le profil Solo utilise des branches courtes, une auto-revue différée et une plateforme obligatoire initiale. Il ne crée pas de rôle d’équipe fictif.

## Créer un projet Studio

```powershell
python .\tools\instantiate_project.py `
  --profile studio `
  --project-name "Mon Projet Studio" `
  --project-id mon_projet_studio `
  --owner-handle mon-organisation `
  --output .\work\mon-projet-studio
```

Le profil Studio ajoute un fichier CODEOWNERS, des responsabilités distinctes, une revue indépendante recommandée et deux plateformes requises. Ces paramètres restent à appliquer dans le dépôt GitHub réel.

## Ajouter un module Godot

```powershell
python .\tools\create_module.py `
  --project .\work\mon-projet-solo `
  --module-id inventory `
  --display-name "Inventaire"
```

Le module produit les couches `domain`, `application`, `infrastructure`, `presentation` et `tests`, avec un README de frontière. Le générateur refuse un identifiant invalide ou un dossier déjà présent.

## Valider les sources du pack

```powershell
python .\tools\validate_templates.py --report .\qa\validation-static.json
```

## Nettoyage

Les projets générés dans `work/` sont des sorties reproductibles. Ils peuvent être supprimés puis recréés depuis les modèles :

```powershell
Remove-Item -Recurse -Force .\work -ErrorAction SilentlyContinue
```

Dans un projet produit, `.godot/`, journaux et rapports locaux sont régénérables. Les sources, ADR, politiques, fichiers `.gd.uid` fournis et manifestes de projet ne sont pas des caches.

## Provenance et redistribution

Tous les fichiers du pack sont originaux et textuels. Aucun binaire Godot, addon, modèle, asset tiers, secret ou donnée personnelle n’est inclus. Le moteur est téléchargé séparément depuis sa distribution officielle.

La licence globale du dépôt restant indécise, [LICENSE-STATUS.md](LICENSE-STATUS.md) bloque la redistribution autonome du pack.

## Références internes

- [Architecture modulaire](../../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md)
- [Services et injection](../../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md)
- [Outils d’édition et pipelines](../../Livre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md)
- [Architecture Solo et Studio](../../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md)
- [Starter Kit](../Starter-Kit/README.md)
