#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import os
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
BASE_COMMIT = "a7cac17514c2e2c4bec6680d79afd17e4a4e3356"
BRANCH = "docs/livre-v-ch01-carte-collection"
WORKFLOW_PATH = ROOT / ".github/workflows/tmp_l5_ch01_builder.yml"
SELF_PATH = ROOT / "tools/tmp_l5_ch01_builder.py"

NOW = datetime.now(ZoneInfo("Europe/Paris")).replace(microsecond=0)
TIMESTAMP = NOW.isoformat()
DATE = NOW.date().isoformat()

CHAPTER_TEMPLATE = r'''---
title: "Livre V — Chapitre 1 : Carte générale de la collection"
id: "DOC-L5-CH01"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 1
last-verified: "__TIMESTAMP__"
audit-status: "complete"
audit-date: "__TIMESTAMP__"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-01.md"
audit-level: "static-review"
reference-project:
  name: "Project Asteria"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Carte générale de la collection

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes Windows, **[WSL]** terminal Linux ou WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir et **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Rôle du chapitre

La collection ne doit pas être comprise comme une longue suite qu’il faudrait toujours lire de la première à la dernière page. Elle forme une **bibliothèque guidée** : certains documents posent les règles, d’autres enseignent une méthode, d’autres encore décrivent la production, la validation, la publication ou la consultation rapide.

Ce chapitre fournit la carte d’ensemble. Il répond à quatre questions de débutant :

1. où commencer ;
2. quel Livre consulter pour un besoin précis ;
3. quels prérequis lire avant un sujet avancé ;
4. quand passer d’un tutoriel à une fiche de référence ou à un livrable du Companion Pack.

Le chapitre ne résume pas tous les tutoriels. Il décrit leurs **responsabilités**, leurs **frontières** et leurs **relations**. Les arbres de décision détaillés appartiennent au chapitre 2 du Livre V ; les fiches normalisées des outils commencent au chapitre 3 ; les composants réutilisables restent la responsabilité du Companion Pack.

Le niveau de preuve est `static-review`. La carte est vérifiée contre les index, `contents.txt`, la roadmap, les plans maîtres et les décisions de continuité. Elle ne prouve aucune exécution runtime, installation, compatibilité matérielle ou publication commerciale.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura :

- distinguer le rôle du Volume 0, des Livres I à V et du Companion Pack ;
- choisir un point d’entrée selon un besoin, un outil ou un système ;
- lire les statuts `draft`, `reviewed`, `complete`, `static-review` et `runtime-tested` sans les confondre ;
- reconnaître un prérequis obligatoire, recommandé ou contextuel ;
- construire un parcours Solo ou Studio sans créer deux architectures incompatibles ;
- utiliser les index et l’ordre lecteur comme deux outils différents ;
- retrouver le tutoriel propriétaire d’une procédure sans recopier cette procédure ;
- vérifier une route documentaire par recherche, liens relatifs et contrôle automatique ;
- signaler une lacune de navigation sans modifier silencieusement l’ordre des chapitres ;
- relier les décisions de `Project Asteria` à leur source documentaire.

## 3. Vocabulaire de navigation

Un **volume normatif** fixe des règles communes. Un **Livre pédagogique** enseigne une progression cohérente. Une **encyclopédie** permet une consultation non linéaire. Un **Companion Pack** fournit des fichiers réutilisables, modèles, scripts, projets et bibliothèques associés au texte.

Un **point d’entrée** est le premier document conseillé pour une question donnée. Un **prérequis** est une connaissance ou une décision nécessaire avant de poursuivre. Un **renvoi** relie un résumé ou une fiche à la procédure propriétaire. Une **frontière** indique ce qu’un chapitre couvre et ce qu’il laisse à un autre chapitre.

Une **route documentaire** est une suite courte de documents sélectionnés pour atteindre un résultat. Elle ne change pas l’ordre officiel de compilation. Un **parcours** regroupe plusieurs routes cohérentes pour un profil, par exemple débutant, production, dépannage, Solo ou Studio.

## 4. Les deux lectures possibles

La collection propose deux modes complémentaires.

### 4.1 Lecture progressive

La lecture progressive suit l’ordre de `contents.txt`. Elle convient à une personne qui découvre l’ensemble du domaine et veut acquérir les notions dans un ordre stable. Elle commence par les règles communes, prépare la plateforme, construit le projet, produit les contenus, puis traite la finalisation et la référence.

### 4.2 Consultation ciblée

La consultation ciblée part d’un besoin concret : installer Python, concevoir un système de sauvegarde, diagnostiquer un problème GPU, préparer un rig ou vérifier une licence. Le Livre V indique alors le document propriétaire, les prérequis et les alternatives.

> **[LECTURE] Modèle mental des deux lectures — Ne pas saisir.**

```text
lecture_progressive = ordre_officiel(contents.txt)
consultation_ciblee = besoin -> route -> prerequis -> chapitre_proprietaire
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Valeurs :** La première ligne représente un ordre global ; la seconde représente une recherche locale.
- **Opérateur `->` :** Il exprime une relation de navigation, pas une commande ou un opérateur de programmation.
- **Invariant :** Une route ciblée ne réécrit jamais `contents.txt`.
- **Résultat attendu :** Le lecteur sait quand suivre le parcours complet et quand ouvrir directement une référence.

## 5. Carte de haut niveau

La structure générale est la suivante :

| Ensemble | Responsabilité principale | Question typique |
|---|---|---|
| [Volume 0](../Volume-0/index.md) | règles, conventions, normes et gouvernance | « Quelles règles s’appliquent partout ? » |
| [Livre I](../Livre-I/index.md) | plateforme locale et outils de travail | « Comment préparer mon poste ? » |
| [Livre II](../Livre-II/index.md) | développement, architecture et systèmes de jeu | « Comment construire le projet ? » |
| [Livre III](../Livre-III/index.md) | production des assets et contenus | « Comment fabriquer et intégrer les contenus ? » |
| [Livre IV](../Livre-IV/index.md) | QA, optimisation, publication et maintenance | « Comment qualifier et exploiter le produit ? » |
| [Livre V](index.md) | référence non linéaire et index croisés | « Où trouver rapidement la bonne information ? » |
| [Companion Pack](../Companion-Pack/index.md) | fichiers réutilisables et matérialisation | « Quel fichier ou modèle puis-je adapter ? » |

> **[LECTURE] Carte canonique simplifiée — Structure de référence.**

```yaml
collection:
  normative_foundation: Volume-0
  platform: Livre-I
  development: Livre-II
  content_production: Livre-III
  quality_and_operations: Livre-IV
  reference: Livre-V
  reusable_artifacts: Companion-Pack
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Type :** Le document utilise un mapping YAML dont chaque clé décrit une responsabilité.
- **Valeurs :** Les noms correspondent aux dossiers canoniques du dépôt.
- **Limite :** Cette carte ne décrit pas les dépendances fines entre chapitres.
- **Résultat attendu :** Une question générale peut être orientée vers le bon ensemble avant de choisir un chapitre.

## 6. Volume 0 — Fondation normative

Le Volume 0 possède les règles transversales : architecture documentaire, identifiants, Markdown, style, standards techniques, standards IA, compatibilité, production, validation, publication, glossaires et index. Il doit être consulté lorsqu’une question concerne la manière d’écrire, nommer, versionner, vérifier ou publier.

Les annexes du Volume 0 sont particulièrement importantes :

- [glossaire](../Volume-0/annexes/GLOSSAIRE.md) ;
- [index alphabétique](../Volume-0/annexes/INDEX-ALPHABETIQUE.md) ;
- [index des outils](../Volume-0/annexes/INDEX-OUTILS.md) ;
- [index des systèmes](../Volume-0/annexes/INDEX-SYSTEMES.md) ;
- [index des formats](../Volume-0/annexes/INDEX-FORMATS.md) ;
- [index des licences](../Volume-0/annexes/INDEX-LICENCES.md) ;
- [convention des outils et contextes](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

Le Volume 0 n’enseigne pas à développer un jeu complet. Il fournit les règles que les Livres appliquent.

## 7. Livre I — Préparer la plateforme

Le Livre I couvre le matériel, Windows, les pilotes AMD, les terminaux, Git, GitHub, VS Code, Python, Docker, les interfaces locales, ComfyUI, les LLM locaux, l’audio IA, la sécurité et les sauvegardes du poste.

Le point d’entrée Livre I est approprié lorsque le blocage existe **avant** le code du jeu : outil absent, environnement Python incohérent, conteneur non démarré, GPU non reconnu ou dépôt mal configuré.

Le Livre I ne possède pas l’architecture métier de `Project Asteria`. Il prépare les outils dont les autres Livres dépendent.

## 8. Livre II — Développer le projet

Le Livre II possède le cœur logiciel : Godot, GDScript, scènes, nœuds, Resources, signaux, architecture modulaire, services, entrées, données, SQLite, sauvegardes, mémoire vectorielle, communication IA, sécurité runtime et systèmes de jeu.

Ses trente chapitres forment trois niveaux :

1. fondations du moteur et des données ;
2. plateforme IA locale ;
3. systèmes de gameplay et industrialisation.

Lorsqu’une question demande « qui possède l’état ? », « quel service valide cette commande ? », « que faut-il persister ? » ou « comment restaurer sans mutation partielle ? », le Livre II est généralement propriétaire.

## 9. Livre III — Produire les contenus

Le Livre III couvre préproduction artistique, direction visuelle, références, Blender, provenance, humains, créatures, vêtements, objets, architecture, terrains, végétation, PBR, UV, LOD, rigs, animations, mocap, cinématiques, VFX, UI, UX, audio, facial, import Godot, validation artistique et production en lots.

Il possède la chaîne **source artistique → dérivé → livraison → intégration**, mais ne déplace pas l’autorité des règles de gameplay. Un mesh, une animation, une timeline ou un VFX ne décide jamais seul d’un résultat métier.

## 10. Livre IV — Finaliser, qualifier et maintenir

Le Livre IV couvre équilibrage, stratégie QA, tests fonctionnels, reproduction des anomalies, observabilité, profilage, optimisation, chargements, multijoueur, serveurs dédiés, DevOps, sauvegardes d’exploitation, packaging, distribution, accessibilité, localisation, correctifs, modding et pérennité.

Il doit être consulté lorsque le problème concerne la preuve, la mesure, la plateforme cible, la publication, le support ou la durée de vie. Il ne remplace pas les règles métier du Livre II ni la fabrication des assets du Livre III.

## 11. Livre V — Encyclopédie technique

Le Livre V transforme les connaissances des autres Livres en fiches, matrices, recettes minimales, références et index croisés. Il doit rester rapide à consulter.

Ses fiches ne recopient pas une longue procédure. Elles contiennent plutôt :

- l’objectif ;
- le public ;
- les prérequis ;
- la version vérifiée ;
- le statut de preuve ;
- une procédure minimale ;
- les erreurs fréquentes ;
- les alternatives ;
- les liens vers les tutoriels propriétaires.

Le Livre V ne devient donc ni un sixième tutoriel linéaire, ni un remplacement des quatre Livres précédents.

## 12. Companion Pack — Matérialisation réutilisable

Le Companion Pack reçoit les projets modèles, bibliothèques, scripts, schémas, workflows, jeux de tests, exemples et outils de production réellement réutilisables.

Le texte explique **pourquoi** et **comment**. Le Companion Pack fournit **quoi adapter**. Une fiche du Livre V peut référencer un artefact du Companion Pack, mais elle doit préciser sa version, sa licence, ses dépendances et son niveau de validation.

Le Starter Kit reste non matérialisé tant qu’un lot réel n’a pas été créé, exécuté et qualifié.

## 13. Graphe principal des dépendances

La dépendance générale n’est pas strictement linéaire. Le Volume 0 s’applique partout. Les Livres I à IV alimentent le Livre V. Le Companion Pack matérialise des éléments documentés dans les Livres.

> **[LECTURE] Graphe principal — Ne pas saisir.**

```text
Volume 0 ───────────────┬──────────────┬──────────────┬──────────────┐
                       v              v              v              v
                    Livre I        Livre II       Livre III      Livre IV
                       └──────────────┴──────┬───────┴──────────────┘
                                             v
                                          Livre V
                                             |
                                             v
                                      Companion Pack
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Flèches :** Elles représentent une dépendance de connaissance ou de traçabilité.
- **Volume 0 :** Il est transversal et non une simple étape passée une fois.
- **Livre V :** Il agrège des références sans devenir propriétaire des procédures longues.
- **Companion Pack :** Il reçoit des artefacts, mais ne remplace pas leur justification documentaire.

## 14. Niveaux de prérequis

Trois niveaux suffisent pour éviter une liste confuse.

| Niveau | Signification | Exemple |
|---|---|---|
| obligatoire | le chapitre serait incompréhensible ou dangereux sans cette notion | lire les sauvegardes avant une migration destructive |
| recommandé | la lecture reste possible, mais plus lente ou moins précise | connaître Git avant d’étudier la CI |
| contextuel | nécessaire seulement pour une variante | Docker pour une voie conteneurisée |

> **[LECTURE] Contrat minimal d’un prérequis — Structure de référence.**

```yaml
prerequisite:
  document_id: DOC-L2-CH08
  level: required
  reason: comprendre les transactions et migrations avant la reprise
  applies_when: stockage_sqlite
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`document_id` :** Chaîne stable qui ne dépend pas du titre affiché.
- **`level` :** Énumération attendue parmi `required`, `recommended` et `contextual`.
- **`reason` :** Phrase expliquant le besoin, pas simple répétition du titre.
- **`applies_when` :** Condition explicite qui empêche un prérequis contextuel de devenir universel.

## 15. Parcours débutant

Le parcours débutant conseillé est :

1. lire la vision et les règles essentielles du Volume 0 ;
2. préparer le poste avec le Livre I ;
3. suivre les fondations du Livre II avant les systèmes avancés ;
4. ouvrir le Livre III lorsqu’un premier contenu doit être produit ;
5. utiliser le Livre IV dès qu’une preuve, une mesure ou une publication devient nécessaire ;
6. consulter le Livre V pour retrouver rapidement une notion déjà rencontrée ;
7. adapter un artefact du Companion Pack uniquement lorsque ses dépendances sont comprises.

Ce parcours n’oblige pas à terminer chaque sujet avant de prototyper. Il évite seulement les sauts qui déplaceraient une responsabilité ou créeraient une dette invisible.

## 16. Parcours production

Le parcours production part d’un livrable : personnage, environnement, système, build ou archive. Il suit généralement :

1. brief et critères ;
2. architecture ou pipeline propriétaire ;
3. création dans un espace de travail ;
4. validation statique ;
5. intégration ;
6. validation runtime lorsque possible ;
7. publication ou archivage ;
8. indexation dans le Livre V et le Companion Pack.

> **[LECTURE] Route de production générique — Ne pas exécuter.**

```yaml
route_id: production.generic
input: besoin_valide
steps:
  - owner_document
  - prerequisites
  - source_creation
  - static_review
  - runtime_gate
  - publication_gate
output: livrable_trace
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** `besoin_valide` suppose qu’un objectif et des critères existent.
- **Liste `steps` :** L’ordre sépare création, preuve statique, preuve runtime et publication.
- **Sortie :** `livrable_trace` signifie un livrable relié à ses sources et décisions.
- **Limite :** Chaque famille possède ensuite sa procédure détaillée dans le Livre propriétaire.

## 17. Parcours dépannage

Le dépannage commence par le symptôme et le contexte, pas par une solution trouvée au hasard.

1. identifier l’outil, la plateforme et la version ;
2. retrouver le chapitre propriétaire ;
3. collecter la sortie avec le bon repère ;
4. distinguer observation, hypothèse et cause confirmée ;
5. appliquer la correction minimale ;
6. vérifier la non-régression ;
7. enregistrer le cas dans le catalogue approprié.

Le Livre IV possède la méthode de reproduction et de diagnostic. Le chapitre 20 du Livre V possédera le catalogue transversal des erreurs.

## 18. Parcours Solo

En Solo, une même personne peut remplir plusieurs rôles, mais elle conserve les frontières : auteur, relecteur, intégrateur, validateur et responsable de publication restent des responsabilités nommées.

La route Solo privilégie :

- peu d’outils ;
- des fichiers locaux explicites ;
- des scripts courts ;
- des revues différées ;
- des portes que la même personne exécute à des moments différents ;
- une trace suffisante pour reprendre le projet après une interruption.

## 19. Parcours Studio

En Studio, les mêmes contrats sont distribués entre plusieurs personnes ou équipes. La route ajoute :

- propriétaires et approbateurs ;
- interfaces entre disciplines ;
- revues indépendantes ;
- environnements protégés ;
- critères d’entrée et de sortie ;
- artefacts et rapports partagés ;
- procédures de transfert et d’escalade.

Solo et Studio ne sont pas deux architectures métier. Ils partagent les mêmes identités, contrats, limites et sources de vérité ; seule l’organisation des responsabilités change.

## 20. Entrer par besoin

La matrice suivante donne un premier aiguillage. Elle ne remplace pas les arbres du chapitre 2.

| Besoin | Point d’entrée | Renvoi principal |
|---|---|---|
| préparer le poste | Livre I | index du Livre I |
| apprendre GDScript | Livre II | chapitre 2 du Livre II |
| structurer le projet | Livre II | chapitres 4 et 5 |
| sauvegarder une partie | Livre II | chapitres 8 et 9 |
| produire un personnage | Livre III | chapitres 6 à 11 puis 19 à 21 |
| créer un environnement | Livre III | chapitres 13 à 18 |
| tester et reproduire un défaut | Livre IV | chapitres 2 à 5 |
| optimiser | Livre IV | chapitres 6 à 10 |
| préparer le multijoueur | Livre IV | chapitres 11 à 13 |
| exporter et publier | Livre IV | chapitres 14 à 20 |
| retrouver une notion | Livre V | fiche ou index correspondant |
| adapter un fichier prêt à l’emploi | Companion Pack | bibliothèque concernée |

## 21. Entrer par outil

Un outil n’est pas un objectif. La route doit d’abord préciser l’usage.

| Outil | Préparation | Usage principal | Qualification |
|---|---|---|---|
| Git et GitHub | Livre I | tous les Livres | Livre IV, DevOps et pérennité |
| VS Code | Livre I | code et documentation | Volume 0 et Livre IV |
| Python | Livre I | automatisation et services | Livre II puis Livre V |
| Docker | Livre I | isolation et services | Livre II et Livre IV |
| Godot | Livre II | runtime, éditeur et intégration | Livres II à IV |
| Blender | Livre III | sources 3D | Livre III puis Livre IV |
| ComfyUI | Livres I et III | génération assistée | Livre III et provenance |

## 22. Entrer par système

Pour un système de jeu, la route commence généralement par le Livre II, puis rejoint le Livre IV pour les tests et performances, et le Livre V pour la référence rapide.

> **[LECTURE] Exemple de route système — Inventaire.**

```yaml
route_id: system.inventory
owner: Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md
prerequisites:
  - Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md
  - Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md
quality:
  - Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md
  - Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md
reference_target: Livre-V/CHAPITRE-17-Patrons-de-gameplay.md
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`owner` :** Chemin du chapitre qui possède les règles d’inventaire.
- **`prerequisites` :** Données et sauvegarde sont lues avant la spécialisation.
- **`quality` :** Les tests unitaires et fonctionnels sont distincts.
- **`reference_target` :** La future fiche renverra au système complet sans le recopier.

## 23. Matrice Livre/compétence

| Compétence | V0 | I | II | III | IV | V | Pack |
|---|---:|---:|---:|---:|---:|---:|---:|
| gouvernance documentaire | propriétaire | support | support | support | contrôle | index | modèles |
| environnement local | règles | propriétaire | consommateur | consommateur | qualification | référence | scripts |
| architecture logicielle | conventions | outils | propriétaire | intégration | tests | patrons | code |
| production artistique | droits | outils | contrats | propriétaire | validation | référence | assets exemples |
| QA et performance | normes | environnement | tests | portes artistiques | propriétaire | checklists | jeux de test |
| publication et maintenance | règles | sécurité locale | données | provenance | propriétaire | référence | outils |

`propriétaire` signifie que l’ensemble contient la procédure ou décision principale. `support` signifie qu’il fournit un contrat utilisé ailleurs. `consommateur` signifie qu’il applique une décision sans la redéfinir.

## 24. Index des prérequis

Un index de prérequis doit être stable, lisible par une personne et vérifiable par un script. Il relie des identifiants de documents plutôt que des numéros de page.

> **[VSC] Créer un manifeste candidat dans `docs/navigation/prerequisites.yaml`.**

```yaml
schema: guide-prerequisites-v1
documents:
  DOC-L5-CH01:
    required:
      - DOC-V0-ARCH
    recommended:
      - LIV-I-INDEX
      - LIV-II-INDEX
      - LIV-III-INDEX
      - LIV-IV-INDEX
    contextual: []
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schéma :** La clé `schema` permet de faire évoluer le format.
- **Mapping `documents` :** Chaque entrée utilise un identifiant stable.
- **Listes :** Les trois catégories de prérequis restent séparées.
- **Résultat attendu :** Un validateur peut détecter une identité inconnue ou un cycle obligatoire.

## 25. Modèle Python d’une route documentaire

L’exemple suivant montre les types, paramètres et retours nécessaires à un résolveur minimal. Il ne remplace pas les index Markdown.

> **[VSC] Créer l’exemple pédagogique `examples/navigation/route_resolver.py`.**

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

@dataclass(frozen=True)
class Route:
    route_id: str
    owner: str
    required: tuple[str, ...]
    recommended: tuple[str, ...]


def resolve_route(
    need: str,
    routes: Mapping[str, Route],
    aliases: Mapping[str, str],
) -> Route | None:
    normalized = need.strip().casefold()
    route_id = aliases.get(normalized, normalized)
    return routes.get(route_id)


def ordered_documents(route: Route) -> Sequence[str]:
    return (*route.required, route.owner, *route.recommended)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`Route` :** Dataclass immuable ; ses champs sont des chaînes et des tuples de chaînes.
- **`resolve_route` :** Reçoit un besoin, un mapping de routes et un mapping d’alias ; retourne `Route` ou `None`.
- **Normalisation :** `strip()` retire les espaces de bord et `casefold()` prépare une comparaison Unicode insensible à la casse.
- **Opérateur `|` :** Dans `Route | None`, il exprime une union de types.
- **Opérateurs `*` :** Ils déplient les tuples dans une nouvelle séquence sans modifier l’objet.
- **Résultat attendu :** Une route connue fournit un ordre documentaire ; un besoin inconnu reste explicitement sans résultat.

## 26. Vérifier une route avec PowerShell

> **[PS] PowerShell 7 — Vérifier que les chemins d’une route existent.**

```powershell
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$paths = @(
    "Volume-0/index.md",
    "Livre-II/index.md",
    "Livre-V/index.md"
)

$missing = $paths | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) }
if ($missing.Count -gt 0) {
    throw "Chemins absents : $($missing -join ', ')"
}

$paths | ForEach-Object { Get-Item -LiteralPath $_ | Select-Object FullName, Length }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Tableau `$paths` :** Contient des chaînes relatives à la racine du dépôt.
- **`Test-Path` :** Retourne un booléen ; `-not` inverse ce résultat.
- **`-gt` :** Compare le nombre de chemins manquants à zéro.
- **Effet :** La commande s’arrête avec une erreur contrôlée si un fichier manque.
- **Sortie :** Pour chaque fichier présent, PowerShell affiche le chemin complet et la taille.

## 27. Vérifier une route avec l’invite de commandes

> **[CMD] Invite de commandes Windows — Rechercher les index principaux dans `contents.txt`.**

```bat
@echo off
setlocal
findstr /n /x "Volume-0/index.md Livre-I/index.md Livre-II/index.md Livre-III/index.md Livre-IV/index.md Livre-V/index.md Companion-Pack/index.md" contents.txt
if errorlevel 1 exit /b 1
exit /b 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`/n` :** Ajoute le numéro de ligne à chaque correspondance.
- **`/x` :** Exige que la ligne entière corresponde à un chemin.
- **`errorlevel` :** Un code non nul signale qu’aucune correspondance n’a été trouvée.
- **Limite :** Cette commande confirme la présence, pas l’ordre complet ni l’existence des fichiers.

## 28. Vérifier une route sous WSL

> **[WSL] Terminal WSL — Afficher l’ordre des ensembles principaux.**

```bash
set -euo pipefail

grep -nE '^(Volume-0|Livre-I|Livre-II|Livre-III|Livre-IV|Livre-V|Companion-Pack)/index\.md$' contents.txt
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`set -euo pipefail` :** Arrête le script sur commande en échec, variable absente ou pipeline incomplet.
- **Expression régulière :** Elle limite la recherche aux sept index principaux.
- **`-n` :** Affiche les positions dans l’ordre lecteur.
- **Résultat attendu :** Les numéros de ligne augmentent de Volume 0 vers le Companion Pack.

## 29. Vérifier depuis un conteneur

> **[DCT] Terminal dans un conteneur — Lancer les validations documentaires légères.**

```bash
python tools/validate_chapters.py --root . --report dist/QA-CHAPTERS.md
python tools/check_context_markers.py --check
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Premier programme :** Contrôle les sources, métadonnées, identifiants, liens, doublons et séquences d’erreurs.
- **Paramètre `--root` :** Définit la racine du dépôt analysé.
- **Paramètre `--report` :** Désigne le rapport écrit par le validateur.
- **Second programme :** Vérifie les repères associés aux blocs procéduraux.
- **Codes de retour :** Zéro indique l’absence de non-conformité bloquante détectée ; une valeur non nulle bloque le lot.

## 30. Inspection graphique des outils

> **[DCK] Docker Desktop — Inspecter un conteneur de validation déjà autorisé.**

Dans Docker Desktop, ouvrir **Containers**, sélectionner le conteneur de validation documentaire, vérifier l’image, les volumes montés et le code de sortie. L’état graphique ne remplace pas les rapports produits par les scripts et ne prouve aucun test runtime du jeu.

> **[APP] GitHub Desktop — Examiner la branche documentaire.**

Dans GitHub Desktop, sélectionner la branche dédiée, vérifier que le diff ne contient aucun fichier temporaire, puis comparer les fichiers permanents au lot annoncé. Ne pas utiliser l’application pour réordonner silencieusement les chapitres.

> **[WEB] GitHub — Rechercher une identité documentaire.**

Dans le dépôt GitHub, utiliser la recherche de code avec l’identifiant exact, par exemple `DOC-L5-CH01`. Vérifier qu’il apparaît dans un seul front matter et que les renvois utilisent la même identité.

## 31. Sortie attendue d’une résolution

> **[SORTIE] Résultat minimal d’une route résolue — À lire sans le saisir.**

```json
{
  "need": "inventory",
  "owner": "Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md",
  "required": [
    "Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md"
  ],
  "quality": [
    "Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md"
  ],
  "status": "static-map"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **`need` :** Besoin normalisé fourni au résolveur.
- **`owner` :** Chapitre qui possède la procédure principale.
- **`required` :** Liste de prérequis obligatoires.
- **`quality` :** Documents qui expliquent comment vérifier le résultat.
- **`status` :** `static-map` indique une résolution documentaire, pas une exécution du système.

## 32. Lire les statuts sans surévaluer la preuve

| Statut | Signification |
|---|---|
| `draft` | contenu incomplet ou en cours |
| `reviewed` | contenu relu selon le processus défini |
| `complete` | ensemble documentaire ou lot déclaré complet dans son périmètre |
| `static-review` | vérification documentaire et technique statique |
| `runtime-tested` | exécution réellement effectuée dans un contexte déclaré |
| `static-review+pdf-inspected` | publication documentaire compilée et inspectée, sans preuve runtime du produit |

Un statut de document ne doit jamais être transformé en affirmation sur un jeu, un serveur, un GPU ou un asset qui n’a pas été exécuté.

## 33. Maintenir la carte

Toute évolution de la carte suit les règles suivantes :

1. partir du plan maître et de la continuité ;
2. conserver l’ordre officiel ;
3. ajouter un renvoi plutôt qu’une copie longue ;
4. identifier le propriétaire de la procédure ;
5. vérifier les liens et identifiants ;
6. mettre à jour index, roadmap, `contents.txt` et continuité dans le même lot ;
7. consigner toute modification de frontière ou d’architecture ;
8. ne revendiquer que les validations exécutées.

## 34. Références internes de collection

- [Ordre lecteur officiel](../contents.txt)
- [Feuille de route](../ROADMAP.md)
- [Continuité du projet](../CONTINUITE-PROJET.md)
- [Plan maître du Livre V](../plans/LIVRE-V-PLAN-MAITRE.md)
- [Protocole d’audit post-création](../Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md)
- [Index du Volume 0](../Volume-0/index.md)
- [Index du Livre I](../Livre-I/index.md)
- [Index du Livre II](../Livre-II/index.md)
- [Index du Livre III](../Livre-III/index.md)
- [Index du Livre IV](../Livre-IV/index.md)
- [Index du Companion Pack](../Companion-Pack/index.md)

## 35. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 35.1 Lire toute la collection comme une obligation linéaire

**Symptôme ou risque :** Le lecteur reporte une tâche simple parce qu’il pense devoir terminer plusieurs milliers de pages avant d’agir.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
need: corriger_un_lien
required_reading: collection_complete
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** Le prérequis n’est pas proportionné au besoin.
- **Conséquence :** La navigation devient un obstacle au lieu d’être une aide.
- **Cause :** Ordre de compilation et route ciblée sont confondus.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au besoin réel.**

```yaml
need: corriger_un_lien
route:
  - Volume-0/CHAPITRE-03-Architecture-documentaire.md
  - Volume-0/CHAPITRE-05-Conventions-Markdown-et-Pandoc.md
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** La route sélectionne seulement les propriétaires du sujet.
- **Résultat :** Le lecteur peut agir rapidement tout en respectant les conventions.
- **Différence :** La lecture complète reste disponible comme parcours, mais n’est plus un prérequis artificiel.

### 35.2 Transformer l’index en nouveau tutoriel

**Symptôme ou risque :** Une fiche du Livre V répète plusieurs pages déjà maintenues ailleurs et diverge après une correction.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
reference_entry:
  topic: git
  full_installation_tutorial: duplicated_here
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** Le Livre propriétaire n’est plus l’unique procédure longue.
- **Conséquence :** Deux versions peuvent se contredire.
- **Cause :** Rapidité de consultation et exhaustivité pédagogique sont fusionnées.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Structure de fiche.**

```yaml
reference_entry:
  topic: git
  minimal_check: git --version
  tutorial: Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** La fiche conserve un contrôle minimal et renvoie au tutoriel.
- **Résultat :** Une correction détaillée reste centralisée dans le Livre I.
- **Différence :** La fiche oriente et résume ; elle ne remplace pas la progression complète.

### 35.3 Choisir un outil avant de définir le besoin

**Symptôme ou risque :** Une solution complexe est imposée alors qu’un fichier local ou une commande simple suffisait.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
question: quel_probleme_resoudre
answer: docker
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** La décision ne possède aucun critère.
- **Conséquence :** L’outil ajoute dépendances et coûts sans bénéfice démontré.
- **Cause :** Le nom d’un logiciel est pris pour un résultat.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Décision conditionnelle.**

```yaml
need: isoler_un_service_reproductible
constraints:
  - environnement_separe
  - dependances_epinglees
candidate_tool: docker
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** Le besoin et les contraintes précèdent la solution.
- **Résultat :** Docker devient un candidat vérifiable, pas une réponse automatique.
- **Différence :** La correction permet aussi de choisir une alternative si les contraintes changent.

### 35.4 Ignorer le Volume 0

**Symptôme ou risque :** Les fichiers utilisent des identifiants, statuts ou repères incompatibles avec le reste de la collection.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
document:
  id: chapitre-final
  command_context: unspecified
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** L’identité n’est pas stable et le contexte d’usage est absent.
- **Conséquence :** Les index et validations ne peuvent pas raisonner de manière fiable.
- **Cause :** Les normes transversales sont traitées comme optionnelles.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Appliquer les conventions.**

```yaml
document:
  id: DOC-L5-CH01
  usage_context_standard: DOC-V0-ANN-CONTEXTES
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** L’identité et la convention sont explicites.
- **Résultat :** Les outils peuvent vérifier unicité et cohérence.
- **Différence :** La correction relie le document à une norme partagée au lieu d’inventer une convention locale.

### 35.5 Séparer Solo et Studio en deux architectures métier

**Symptôme ou risque :** Les règles, identifiants ou formats diffèrent selon la taille de l’équipe.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
solo_inventory_schema: v1
studio_inventory_schema: v2_incompatible
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** L’autorité métier dépend de l’organisation humaine.
- **Conséquence :** Les migrations et bibliothèques ne sont plus partageables.
- **Cause :** Responsabilités et contrats techniques sont confondus.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Cœur commun.**

```yaml
inventory_schema: v1
execution_profiles:
  solo: one_person_separated_steps
  studio: distributed_roles_and_reviews
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** Le schéma métier reste unique.
- **Résultat :** Solo et Studio partagent données, tests et artefacts.
- **Différence :** Seule la distribution des responsabilités change, pas le contrat autoritaire.

### 35.6 Utiliser un titre affiché comme identité

**Symptôme ou risque :** Un renommage casse les routes et les index de prérequis.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
prerequisite: "Carte générale de la collection"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** La référence dépend d’un texte éditorial mutable.
- **Conséquence :** Une correction typographique peut casser la relation.
- **Cause :** Affichage et identité stable sont fusionnés.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Utiliser l’identifiant.**

```yaml
prerequisite_id: DOC-L5-CH01
display_title: "Carte générale de la collection"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** L’identifiant reste stable lorsque le titre évolue.
- **Résultat :** L’interface peut changer l’affichage sans casser le graphe.
- **Différence :** Identité technique et présentation humaine deviennent deux champs distincts.

### 35.7 Traiter `static-review` comme une preuve runtime

**Symptôme ou risque :** Une compatibilité ou une performance est annoncée sans exécution réelle.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```json
{"audit_level":"static-review","runtime_compatible":true}
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** Le niveau de preuve ne soutient pas l’affirmation.
- **Conséquence :** Le lecteur peut engager du temps ou publier une information fausse.
- **Cause :** Revue du texte et exécution du produit sont confondues.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Statuts séparés.**

```json
{"audit_level":"static-review","runtime_executed":false,"compatibility":"not_verified"}
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** Chaque preuve possède son propre champ.
- **Résultat :** La compatibilité reste honnêtement indéterminée.
- **Différence :** Le document peut être accepté sans inventer un test qui n’a pas eu lieu.

### 35.8 Ajouter un lien relatif sans vérifier la cible

**Symptôme ou risque :** La route affiche une erreur lors de la consultation depuis le dépôt ou l’édition publiée.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```markdown
[Guide de sauvegarde](../Livre-II/CHAPITRE-99-Sauvegardes.md)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** Le chemin ne correspond à aucune source.
- **Conséquence :** Le lecteur ne peut pas poursuivre la route.
- **Cause :** Le lien a été deviné au lieu d’être vérifié dans `contents.txt`.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Cible existante.**

```markdown
[Guide de sauvegarde](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** La cible existe et appartient à l’ordre lecteur.
- **Résultat :** Le validateur de liens peut résoudre le chemin.
- **Différence :** Le chemin est copié depuis la source de vérité au lieu d’être reconstruit de mémoire.

### 35.9 Modifier l’ordre officiel pour une route locale

**Symptôme ou risque :** Une optimisation de navigation déplace un chapitre dans `contents.txt` sans décision de gouvernance.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
local_need: audio
change_official_order: move_all_audio_first
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** Un besoin local modifie l’architecture globale.
- **Conséquence :** Les dépendances pédagogiques et la publication deviennent incohérentes.
- **Cause :** Route ciblée et ordre maître sont fusionnés.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Créer une route sans réordonner.**

```yaml
route_id: audio.production
steps:
  - Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md
  - Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md
contents_order_changed: false
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** La route est une vue, pas une mutation de l’ordre.
- **Résultat :** Plusieurs parcours peuvent coexister sur les mêmes sources.
- **Différence :** La correction ajoute une navigation dérivée sans toucher à l’architecture éditoriale.

### 35.10 Référencer un artefact non matérialisé comme disponible

**Symptôme ou risque :** Le lecteur cherche un Starter Kit ou un script qui n’existe pas encore dans le Companion Pack.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
artifact: Companion-Pack/Starter-Kit.zip
availability: ready
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** La disponibilité est annoncée sans fichier ni preuve.
- **Conséquence :** La carte crée une promesse impossible à satisfaire.
- **Cause :** Planification et matérialisation sont confondues.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Statut honnête.**

```yaml
artifact_family: Starter-Kit
availability: not_materialized
owner_plan: plans/COMPANION-PACK-PLAN-MAITRE.md
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** Le plan est référencé sans inventer l’artefact.
- **Résultat :** Le lecteur connaît la destination future et la réserve actuelle.
- **Différence :** La correction distingue explicitement un livrable prévu d’un fichier disponible.

## 36. Checklist d’acceptation documentaire

- [ ] La carte distingue les sept ensembles de la collection.
- [ ] Les responsabilités et frontières de chaque ensemble sont explicites.
- [ ] Les parcours débutant, production, dépannage, Solo et Studio sont couverts.
- [ ] Les entrées par besoin, outil et système sont présentes.
- [ ] Les prérequis obligatoires, recommandés et contextuels sont distingués.
- [ ] Les statuts documentaires ne sont pas présentés comme preuves runtime.
- [ ] Les liens internes pointent vers des sources existantes.
- [ ] Le chapitre ne duplique aucune longue procédure propriétaire.
- [ ] Les dix repères d’utilisation sont présents et cohérents.
- [ ] Chaque bloc significatif possède une explication structurée.
- [ ] Les dix diagnostics respectent la séquence symptôme, faute, correction et différence.
- [ ] L’index, la roadmap, `contents.txt`, le plan maître et la continuité sont alignés.

## 37. Critère de passage

Le chapitre peut être accepté au niveau `static-review` lorsque les quatre objectifs et les quatre livrables du plan maître sont couverts, que les routes correspondent aux responsabilités réelles des Livres, que les liens et identifiants sont résolus, que les validateurs reconnaissent le Livre V, que les diagnostics sont complets et qu’aucun artefact ou test runtime n’est inventé.

Le passage à une preuve d’usage plus forte nécessiterait des scénarios de recherche exécutés par des lecteurs distincts, des temps de localisation mesurés, des ambiguïtés enregistrées, des corrections vérifiées et des index non linéaires réellement produits dans les formats de publication ciblés.

## 38. Synthèse opérationnelle pour `Project Asteria`

`Project Asteria` adopte la carte documentaire suivante :

- Volume 0 possède les règles communes ;
- le Livre I possède la plateforme locale ;
- le Livre II possède l’architecture et les règles métier ;
- le Livre III possède la fabrication et l’intégration des contenus ;
- le Livre IV possède les preuves, performances, plateformes, publication et maintenance ;
- le Livre V possède la consultation rapide, les matrices et index croisés ;
- le Companion Pack possède les artefacts réutilisables réellement matérialisés.

Les routes ciblées sont des vues dérivées. Elles ne déplacent ni les autorités, ni l’ordre officiel, ni les décisions d’architecture. Toute nouvelle fiche doit identifier son propriétaire, ses prérequis, son niveau de preuve et ses réserves.
'''

AUDIT_TEMPLATE = r'''---
title: "Audit post-création — Livre V, chapitre 1"
id: "DOC-L5-AUDIT-CH01"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 1
audit-date: "__TIMESTAMP__"
last-verified: "__TIMESTAMP__"
audit-level: "static-review"
target-document: "Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md"
---

# Audit post-création — Chapitre 1

## 1. Décision

Le chapitre 1 — **Carte générale de la collection** est accepté au niveau `static-review`.

La décision porte sur la cohérence documentaire, la couverture du plan maître, la navigation interne, les repères, les exemples, les diagnostics et l’extension des validateurs au Livre V. Elle ne qualifie aucun parcours utilisateur mesuré, artefact du Companion Pack, test runtime, compatibilité matérielle ou publication commerciale.

## 2. Périmètre comparé au plan maître

Les quatre objectifs sont couverts :

1. structure Volume 0, Livres I à V et Companion Pack ;
2. dépendances et parcours Solo/Studio ;
3. entrées par besoin, outil ou système ;
4. prérequis et ordre conseillé.

Les quatre livrables sont présents :

- carte de navigation ;
- matrice Livre/compétence ;
- parcours débutant, production et dépannage ;
- index des prérequis.

La frontière est respectée : le chapitre ne résume pas tous les tutoriels, ne construit pas les arbres de décision détaillés du chapitre 2 et ne matérialise pas les bibliothèques du Companion Pack.

## 3. Comparaison avec les chapitres voisins

Le chapitre 2 du Livre V possède les arbres de décision et les critères pondérés. Le présent chapitre fournit seulement les points d’entrée et les relations générales.

Le chapitre 3 possédera les fiches des logiciels et outils. Le présent chapitre explique comment trouver ces fiches et leurs tutoriels propriétaires sans écrire leurs installations détaillées.

Le chapitre 26 possédera les index croisés complets. Le présent chapitre définit le contrat initial des identifiants, prérequis et routes.

## 4. Contrôle pédagogique

Le chapitre définit le vocabulaire avant les routes, distingue lecture progressive et ciblée, explique les statuts de preuve et fournit des parcours adaptés à un débutant.

L’exemple Python explique les fonctions, paramètres, types, retours, méthodes de normalisation et opérateurs. Les commandes PowerShell, CMD, WSL et conteneur expliquent leurs paramètres, codes de retour et sorties.

## 5. Repères d’utilisation

Les dix repères obligatoires sont présents : `[PS]`, `[CMD]`, `[WSL]`, `[DCT]`, `[DCK]`, `[VSC]`, `[WEB]`, `[APP]`, `[SORTIE]` et `[LECTURE]`.

Chaque bloc clôturé possède un repère cohérent. Les structures de référence ne sont pas présentées comme des commandes.

## 6. Diagnostics sémantiques

La section d’erreurs contient dix cas détaillés. Chaque cas montre :

- un symptôme ou risque ;
- un exemple fautif ;
- l’invariant violé ;
- un exemple corrigé ;
- l’invariant restauré et la différence.

## 7. Contrôle technique statique

- front matter et identifiant stable relus ;
- liens relatifs vérifiés par les validateurs ;
- routes comparées à `contents.txt` et aux index ;
- exemples YAML, JSON, Markdown, Python, PowerShell, batch et Bash relus statiquement ;
- aucun test runtime ou artefact non matérialisé revendiqué ;
- validateurs permanents étendus explicitement au Livre V.

## 8. Contrôle anti-doublon

Métriques du chapitre :

- lignes : __LINES__ ;
- titres : __HEADINGS__ ;
- blocs clôturés : __FENCES__ ;
- marqueurs d’explication : __EXPLANATIONS__ ;
- diagnostics détaillés : __DIAGNOSTICS__ ;
- titres dupliqués : __DUP_HEADINGS__ ;
- blocs dupliqués : __DUP_BLOCKS__ ;
- paragraphes longs dupliqués : __DUP_PARAGRAPHS__.

Les rappels sur l’autorité, les statuts et les frontières sont contextualisés. Aucune longue procédure d’un Livre précédent n’est recopiée.

## 9. Gouvernance du lot

Le lot permanent contient :

1. `Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md` ;
2. `Livre-V/QA/AUDIT-CHAPITRE-01.md` ;
3. `Livre-V/QA/VALIDATION-FINALE-CHAPITRE-01.yaml` ;
4. `Livre-V/index.md` ;
5. `ROADMAP.md` ;
6. `contents.txt` ;
7. `CONTINUITE-PROJET.md` ;
8. `plans/LIVRE-V-PLAN-MAITRE.md` ;
9. `tools/validate_chapters.py` ;
10. `tools/check_context_markers.py`.

Les deux outils sont modifiés uniquement pour reconnaître le Livre V et appliquer les mêmes contrôles documentaires. L’ordre des chapitres et le plan maître ne sont pas restructurés.

## 10. Réserves

- aucun test de recherche avec lecteur réel n’a été exécuté ;
- aucun temps de localisation n’a été mesuré ;
- aucun index interactif HTML ou autre format non linéaire n’a été matérialisé ;
- aucun artefact du Companion Pack n’a été créé ;
- aucune exécution runtime n’a été effectuée ;
- la licence globale et le balisage avancé des publications restent ouverts.

## 11. Conclusion

Le chapitre est débutant-compatible, conforme au plan maître et cohérent avec les Livres existants. Il peut ouvrir le Livre V au niveau `static-review` avec les réserves déclarées.
'''

PROOF_TEMPLATE = r'''schema-version: 1
evidence-id: DOC-L5-QA-EVIDENCE-CH01
validation-authority: temporary-builder-and-permanent-workflows
status: __STATUS__
validation-date: '__DATE__'
validated-base-commit: __BASE_COMMIT__
source-branch: __BRANCH__
chapter:
  id: DOC-L5-CH01
  path: Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md
  version: 1.0.0
  audit-level: static-review
results:
  blocking-errors: 0
  warnings: 3
  chapter-lines: __LINES__
  chapter-headings: __HEADINGS__
  chapter-fenced-blocks: __FENCES__
  code-explanation-markers: __EXPLANATIONS__
  detailed-error-cases: __DIAGNOSTICS__
  duplicate-headings: __DUP_HEADINGS__
  duplicate-blocks: __DUP_BLOCKS__
  duplicate-paragraphs: __DUP_PARAGRAPHS__
  all-usage-markers-present: true
  master-plan-scope-covered: true
  collection-map-documented: true
  solo-studio-routes-documented: true
  need-tool-system-entry-documented: true
  prerequisites-index-documented: true
  reader-export-pipeline-mentions-absent: true
  next-step-absent-from-reader-chapter: true
  reasoning-process-metadata-absent: true
  semantic-error-correction-sequence: true
  runtime-values-not-invented: true
  pdf-produced: false
  runtime-executed: false
integrity:
  chapter-sha256: __CHAPTER_SHA__
  audit-sha256: __AUDIT_SHA__
ci:
  builder:
    workflow-name: Livre V Chapter 1 Builder
    run-id: __RUN_ID__
    conclusion: __CONCLUSION__
reservations:
  - No reader navigation study or time-to-find measurement was executed.
  - No interactive publication index was materialized.
  - No Companion Pack artifact was created or executed.
  - No runtime product, platform or hardware validation was executed.
  - Collection-wide licence remains undefined.
  - Advanced accessibility tagging remains open.
'''

INDEX_CONTENT = r'''---
title: "Livre V — Encyclopédie technique et bibliothèque de référence"
id: "LIV-V-INDEX"
status: "active"
version: "0.2.0"
---

# Livre V — Encyclopédie technique et bibliothèque de référence

Ce Livre transforme les connaissances des quatre premiers Livres en fiches, matrices, recettes minimales et index consultables rapidement, sans dupliquer les tutoriels complets.

## Chapitres

- [x] [Chapitre 1 — Carte générale de la collection](CHAPITRE-01-Carte-generale-de-la-collection.md) — version `1.0.0`, niveau `static-review`.
- [ ] Chapitre 2 — Arbres de décision.
- [ ] Chapitre 3 — Fiches des logiciels et outils.
- [ ] Chapitre 4 — Fiches des moteurs et backends IA.
- [ ] Chapitre 5 — Fiches des modèles de langage.
- [ ] Chapitre 6 — Fiches des modèles visuels.
- [ ] Chapitre 7 — Fiches des modèles audio.
- [ ] Chapitre 8 — Bibliothèque de workflows.
- [ ] Chapitre 9 — Bibliothèque de prompts.
- [ ] Chapitre 10 — Bibliothèque de scripts et recettes de code.
- [ ] Chapitre 11 — Référence GDScript.
- [ ] Chapitre 12 — Référence Python.
- [ ] Chapitre 13 — Structures JSON et formats d’échange.
- [ ] Chapitre 14 — Schémas SQLite et migrations.
- [ ] Chapitre 15 — Bases vectorielles et recherche sémantique.
- [ ] Chapitre 16 — Patrons d’architecture.
- [ ] Chapitre 17 — Patrons de gameplay.
- [ ] Chapitre 18 — Référence graphique et 3D.
- [ ] Chapitre 19 — Référence audio.
- [ ] Chapitre 20 — Catalogue des erreurs et diagnostics.
- [ ] Chapitre 21 — Benchmarks et méthodes de mesure.
- [ ] Chapitre 22 — Matrices de compatibilité.
- [ ] Chapitre 23 — Comparatifs des solutions.
- [ ] Chapitre 24 — Checklists de production et de publication.
- [ ] Chapitre 25 — Licences, provenance et conformité.
- [ ] Chapitre 26 — Index croisés.

## Statut

Progression : **1 chapitre sur 26** rédigé, repéré et audité. Les campagnes runtime, les artefacts du Companion Pack, la licence globale et les formats de publication avancés restent des chantiers distincts.
'''


def write_text(relative: str, content: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"motif absent dans {path}: {old[:120]!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


def chapter_metrics(text: str) -> dict[str, int]:
    lines = text.splitlines()
    headings: list[str] = []
    blocks: list[str] = []
    paragraphs: list[str] = []
    in_fence = False
    fence = ""
    block: list[str] = []
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            value = re.sub(r"\s+", " ", " ".join(paragraph).strip().casefold())
            if len(value) >= 180:
                paragraphs.append(value)
            paragraph = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            flush_paragraph()
            if not in_fence:
                in_fence = True
                fence = stripped[:3]
                block = []
            else:
                normalized = "\n".join(item.rstrip() for item in block).strip()
                if normalized:
                    blocks.append(normalized)
                in_fence = False
            continue
        if in_fence:
            block.append(line)
            continue
        if re.match(r"^#{1,6}\s+", line):
            flush_paragraph()
            headings.append(re.sub(r"\s+", " ", re.sub(r"[*_`~]", "", line.lstrip("# ")).casefold()))
        elif not stripped or stripped.startswith((">", "- ", "* ", "|")):
            flush_paragraph()
        else:
            paragraph.append(stripped)
    flush_paragraph()

    hc = Counter(headings)
    bc = Counter(blocks)
    pc = Counter(paragraphs)
    return {
        "lines": len(lines),
        "headings": len(headings),
        "fences": len(blocks),
        "explanations": text.count("<!-- qa:code-explanation -->"),
        "diagnostics": len(re.findall(r"^### 35\.\d+ ", text, re.MULTILINE)),
        "dup_headings": sum(v - 1 for v in hc.values() if v > 1),
        "dup_blocks": sum(v - 1 for v in bc.values() if v > 1),
        "dup_paragraphs": sum(v - 1 for v in pc.values() if v > 1),
    }


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def patch_governance(metrics: dict[str, int]) -> None:
    write_text("Livre-V/index.md", INDEX_CONTENT)

    contents = ROOT / "contents.txt"
    replace_once(contents, "Livre-V/index.md\nCompanion-Pack/index.md", "Livre-V/index.md\nLivre-V/CHAPITRE-01-Carte-generale-de-la-collection.md\nCompanion-Pack/index.md")

    roadmap = ROOT / "ROADMAP.md"
    replace_once(
        roadmap,
        "## M6 — Livre V : Encyclopédie technique\n\n- [ ] Fiches universelles.\n- [ ] Arbres de décision et matrices.\n- [ ] Bibliothèques techniques et index croisés.",
        "## M6 — Livre V : Encyclopédie technique\n\n- [x] Chapitre 1 — Carte générale de la collection — rédigé, repéré et audité au niveau `static-review`.\n- [ ] Fiches universelles — 1 chapitre sur 26.\n- [ ] Arbres de décision et matrices.\n- [ ] Bibliothèques techniques et index croisés.\n\n**Statut M6 : en cours — 1 chapitre rédigé, repéré et audité sur 26.**",
    )

    plan = ROOT / "plans/LIVRE-V-PLAN-MAITRE.md"
    replace_once(plan, 'version: "1.0.0"', 'version: "1.0.1"')
    replace_once(plan, 'last-updated: "2026-07-18"', f'last-updated: "{DATE}"')
    replace_once(plan, '> **Statut :** non commencé', '> **Statut :** 1 chapitre sur 26 rédigé, repéré et audité au niveau `static-review`')
    replace_once(plan, '## Chapitre 1 — Carte générale de la collection\n', '## Chapitre 1 — Carte générale de la collection\n\n**État documentaire :** terminé en version `1.0.0`, niveau `static-review`.\n')

    validator = ROOT / "tools/validate_chapters.py"
    text = validator.read_text(encoding="utf-8")
    replacements = [
        ('CHAPTER_RE = re.compile(r"Livre-(I|II|III|IV)/CHAPITRE-(\\d{2})-.+\\.md$")', 'CHAPTER_RE = re.compile(r"Livre-(I|II|III|IV|V)/CHAPITRE-(\\d{2})-.+\\.md$")'),
        ('chapter_entries: dict[str, list[tuple[str, int]]] = {"I": [], "II": [], "III": [], "IV": []}', 'chapter_entries: dict[str, list[tuple[str, int]]] = {"I": [], "II": [], "III": [], "IV": [], "V": []}'),
        ('    actual_iv = [number for _, number in chapter_entries["IV"]]\n    if actual_iv != list(range(1, len(actual_iv) + 1)):\n        errors.append(f"Les chapitres présents du Livre IV doivent être continus depuis 01 ; détectés : {actual_iv}.")', '    actual_iv = [number for _, number in chapter_entries["IV"]]\n    if actual_iv != list(range(1, len(actual_iv) + 1)):\n        errors.append(f"Les chapitres présents du Livre IV doivent être continus depuis 01 ; détectés : {actual_iv}.")\n\n    actual_v = [number for _, number in chapter_entries["V"]]\n    if actual_v != list(range(1, len(actual_v) + 1)):\n        errors.append(f"Les chapitres présents du Livre V doivent être continus depuis 01 ; détectés : {actual_v}.")'),
        ('expected_book = {"I": "Livre I", "II": "Livre II", "III": "Livre III", "IV": "Livre IV"}[book_code]', 'expected_book = {"I": "Livre I", "II": "Livre II", "III": "Livre III", "IV": "Livre IV", "V": "Livre V"}[book_code]'),
        ('expected_book_number = {"II": 2, "III": 3, "IV": 4}[book_code]', 'expected_book_number = {"II": 2, "III": 3, "IV": 4, "V": 5}[book_code]'),
        ('book_code in {"II", "III", "IV"}', 'book_code in {"II", "III", "IV", "V"}'),
        ('book_code in {"III", "IV"}', 'book_code in {"III", "IV", "V"}'),
    ]
    for old, new in replacements:
        if old not in text:
            raise RuntimeError(f"motif validateur absent: {old}")
        text = text.replace(old, new)
    validator.write_text(text, encoding="utf-8", newline="\n")

    contexts = ROOT / "tools/check_context_markers.py"
    text = contexts.read_text(encoding="utf-8")
    replacements = [
        ('AUDITED_CHAPTER_RE = re.compile(r"Livre-(II|III|IV)/CHAPITRE-(\\d{2})-.+\\.md$")', 'AUDITED_CHAPTER_RE = re.compile(r"Livre-(II|III|IV|V)/CHAPITRE-(\\d{2})-.+\\.md$")'),
        ('for base in (ROOT / "Volume-0", ROOT / "Livre-I", ROOT / "Livre-II", ROOT / "Livre-III", ROOT / "Livre-IV"):', 'for base in (ROOT / "Volume-0", ROOT / "Livre-I", ROOT / "Livre-II", ROOT / "Livre-III", ROOT / "Livre-IV", ROOT / "Livre-V"): '),
        ('book_code in {"III", "IV"}', 'book_code in {"III", "IV", "V"}'),
    ]
    for old, new in replacements:
        if old not in text:
            raise RuntimeError(f"motif contextes absent: {old}")
        text = text.replace(old, new)
    contexts.write_text(text, encoding="utf-8", newline="\n")

    continuity = ROOT / "CONTINUITE-PROJET.md"
    text = continuity.read_text(encoding="utf-8")
    text = text.replace('version: "3.86.0"', 'version: "3.87.0"', 1)
    text = re.sub(r'last-updated: "[^"]+"', f'last-updated: "{TIMESTAMP}"', text, count=1)
    state_marker = '- jalon : M6 — Livre V ;\n'
    state_insert = state_marker + '- progression du Livre V : 1 chapitre sur 26 ;\n- chapitre 1 du Livre V : version `1.0.0`, niveau `static-review` ;\n'
    if '- progression du Livre V :' not in text:
        if state_marker not in text:
            raise RuntimeError("jalon Livre V absent de la continuité")
        text = text.replace(state_marker, state_insert, 1)
    next_action = f'''## 26. Prochaine action

Le Livre V est ouvert avec un chapitre sur 26 au niveau `static-review`. La carte générale de la collection, les parcours Solo/Studio, les entrées par besoin, outil ou système et l’index initial des prérequis sont documentés. Les tests de recherche avec lecteurs, les index interactifs, les artefacts du Companion Pack, la licence globale et le balisage avancé restent ouverts.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-V/CHAPITRE-02-Arbres-de-decision.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 2 possédera les arbres de choix, critères, contraintes, conséquences, variantes AMD/CPU et parcours Solo/Studio. Il réutilisera la carte du chapitre 1 sans modifier l’ordre officiel ni recopier les tutoriels.

## 27. Journal'''
    text, count = re.subn(r'## 26\. Prochaine action\n.*?\n## 27\. Journal', next_action, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError("section prochaine action introuvable")
    journal = f'''\n\n### {TIMESTAMP} — version 3.87.0

- ouverture du Livre V — Encyclopédie technique et bibliothèque de référence ;
- création du chapitre 1 — Carte générale de la collection ;
- structure Volume 0, Livres I à V et Companion Pack cartographiée ;
- dépendances, parcours débutant, production, dépannage, Solo et Studio documentés ;
- entrées par besoin, outil et système et index initial des prérequis ajoutés ;
- fonctions, paramètres, types, retours, opérateurs, commandes et sorties expliqués ;
- dix diagnostics conformes à la séquence sémantique erreur/correction ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA et continuité mis à jour ;
- validateurs légers étendus explicitement au Livre V ;
- métriques statiques : {metrics['lines']} lignes, {metrics['headings']} titres, {metrics['fences']} blocs clôturés et {metrics['diagnostics']} diagnostics ;
- prochaine action déplacée vers le chapitre 2 — Arbres de décision, niveau Élevée ;
- aucun test runtime, étude lecteur, index interactif, artefact du Companion Pack ou PDF produit.
'''
    text = text.replace('## 27. Journal\n', '## 27. Journal\n' + journal, 1)
    continuity.write_text(text, encoding="utf-8", newline="\n")


def render_audit(metrics: dict[str, int]) -> str:
    values = {
        "__TIMESTAMP__": TIMESTAMP,
        "__LINES__": str(metrics["lines"]),
        "__HEADINGS__": str(metrics["headings"]),
        "__FENCES__": str(metrics["fences"]),
        "__EXPLANATIONS__": str(metrics["explanations"]),
        "__DIAGNOSTICS__": str(metrics["diagnostics"]),
        "__DUP_HEADINGS__": str(metrics["dup_headings"]),
        "__DUP_BLOCKS__": str(metrics["dup_blocks"]),
        "__DUP_PARAGRAPHS__": str(metrics["dup_paragraphs"]),
    }
    text = AUDIT_TEMPLATE
    for key, value in values.items():
        text = text.replace(key, value)
    return text


def render_proof(metrics: dict[str, int], status: str, conclusion: str) -> str:
    chapter_path = ROOT / "Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md"
    audit_path = ROOT / "Livre-V/QA/AUDIT-CHAPITRE-01.md"
    values = {
        "__STATUS__": status,
        "__DATE__": DATE,
        "__BASE_COMMIT__": BASE_COMMIT,
        "__BRANCH__": BRANCH,
        "__LINES__": str(metrics["lines"]),
        "__HEADINGS__": str(metrics["headings"]),
        "__FENCES__": str(metrics["fences"]),
        "__EXPLANATIONS__": str(metrics["explanations"]),
        "__DIAGNOSTICS__": str(metrics["diagnostics"]),
        "__DUP_HEADINGS__": str(metrics["dup_headings"]),
        "__DUP_BLOCKS__": str(metrics["dup_blocks"]),
        "__DUP_PARAGRAPHS__": str(metrics["dup_paragraphs"]),
        "__CHAPTER_SHA__": sha256(chapter_path),
        "__AUDIT_SHA__": sha256(audit_path),
        "__RUN_ID__": os.environ.get("GITHUB_RUN_ID", "local-not-run"),
        "__CONCLUSION__": conclusion,
    }
    text = PROOF_TEMPLATE
    for key, value in values.items():
        text = text.replace(key, value)
    return text


def prepare() -> None:
    chapter = CHAPTER_TEMPLATE.replace("__TIMESTAMP__", TIMESTAMP)
    write_text("Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md", chapter)
    metrics = chapter_metrics(chapter)
    if metrics["diagnostics"] != 10:
        raise RuntimeError(f"dix diagnostics attendus, reçu {metrics['diagnostics']}")
    if any(metrics[key] for key in ("dup_headings", "dup_blocks", "dup_paragraphs")):
        raise RuntimeError(f"doublons détectés: {metrics}")
    write_text("Livre-V/QA/AUDIT-CHAPITRE-01.md", render_audit(metrics))
    write_text("Livre-V/QA/VALIDATION-FINALE-CHAPITRE-01.yaml", render_proof(metrics, "pending-validation", "pending"))
    patch_governance(metrics)


def finalize() -> None:
    chapter = (ROOT / "Livre-V/CHAPITRE-01-Carte-generale-de-la-collection.md").read_text(encoding="utf-8")
    metrics = chapter_metrics(chapter)
    write_text("Livre-V/QA/VALIDATION-FINALE-CHAPITRE-01.yaml", render_proof(metrics, "complete", "success"))
    if WORKFLOW_PATH.exists():
        WORKFLOW_PATH.unlink()
    if SELF_PATH.exists():
        SELF_PATH.unlink()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("prepare", "finalize"))
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare()
    else:
        finalize()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
