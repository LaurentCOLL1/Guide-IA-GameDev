---
title: "Companion Pack — Project Templates"
id: "CP-PACK-02-PROJECT-TEMPLATES"
status: "candidate"
version: "0.1.0"
lang: "fr-FR"
last-verified: "2026-07-30T05:06:00+02:00"
validation-status: "pending-runtime"
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
| création de projets neufs | en attente de la preuve CI |
| import et tests Godot | en attente de la preuve CI |
| protection de branche réelle | non appliquée |
| CODEOWNERS effectif sur un dépôt cible | non vérifié |
| licence globale | non décidée |

Les fichiers de gouvernance sont des **modèles de départ**. Leur présence ne prouve ni une protection de branche active, ni une revue obligatoire, ni l’application d’un CODEOWNERS par GitHub.

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
