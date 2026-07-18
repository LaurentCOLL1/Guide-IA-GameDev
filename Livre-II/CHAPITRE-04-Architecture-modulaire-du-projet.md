---
title: "Livre II — Chapitre 4 : Architecture modulaire du projet"
id: "DOC-L2-CH04"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 4
last-verified: "2026-07-18"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-04.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
recommended-reasoning: "GPT-5.6 Sol — Élevée"
---

# Architecture modulaire du projet

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir, **[LECTURE]** exemple à étudier. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH04`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Niveau de raisonnement conseillé pour produire ou réviser ce chapitre :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-04.md`.

## 1. Rôle du chapitre

Les trois premiers chapitres ont créé le projet, introduit GDScript et construit une première fonctionnalité réutilisable avec des scènes, des Resources et des signaux.

Le projet reste encore suffisamment petit pour que presque tous les fichiers puissent être retrouvés de mémoire. Cette situation ne durera pas. Lorsque les personnages, la sauvegarde, l’économie, les quêtes, l’IA locale et les outils de production seront ajoutés, une organisation improvisée produira rapidement :

- des scripts qui connaissent trop de systèmes ;
- des scènes monolithiques ;
- des dépendances circulaires ;
- des fichiers difficiles à localiser ;
- des modifications risquées ;
- des tests impossibles à isoler ;
- des responsabilités ambiguës entre personnes ou équipes.

Ce chapitre définit l’architecture modulaire de `Project Asteria` avant que ces problèmes apparaissent.

À la fin du chapitre, le lecteur doit savoir :

- distinguer architecture, module, couche, dépendance, contrat, couplage et cohésion ;
- organiser le projet par fonctionnalités plutôt que par type de fichier global ;
- séparer domaine, application, présentation, données, infrastructure et outils ;
- appliquer une direction de dépendance explicite ;
- choisir entre scène, script, Resource et objet `RefCounted` ;
- concevoir une interface publique limitée pour chaque module ;
- comprendre les contrats explicites, les classes abstraites et le duck typing ;
- documenter une décision avec une ADR ;
- lire et maintenir une matrice de dépendances ;
- migrer progressivement le module `beacons` sans casser le chapitre précédent ;
- différencier l’architecture minimale Solo et les contrôles supplémentaires Studio.

## 2. Prérequis

Le lecteur doit avoir terminé :

- le chapitre 1 pour disposer de `Project Asteria` ;
- le chapitre 2 pour comprendre classes, types, fonctions et héritage ;
- le chapitre 3 pour comprendre scènes, Resources, signaux, `Callable` et frontières d’instances.

Ce chapitre réutilise `BeaconProfile` et `StatusBeacon`. Il ne réexplique pas entièrement leur code.

## 3. Périmètre et frontières

Ce chapitre définit :

- la structure physique des dossiers ;
- les couches conceptuelles ;
- les modules fonctionnels ;
- les dépendances autorisées ;
- les règles d’interface et d’encapsulation ;
- la documentation des décisions ;
- le point de composition principal.

Il ne définit pas encore :

- un registre de services complet ;
- les Autoloads définitifs ;
- un bus d’événements global ;
- l’injection de dépendances runtime détaillée ;
- les repositories et adaptateurs concrets ;
- les catalogues JSON et stratégies de données ;
- les tests automatisés complets de l’architecture.

Ces sujets appartiennent principalement aux chapitres 5, 7, 8, 27 et 29.

> **Frontière essentielle :** le chapitre 4 définit où les responsabilités vivent et dans quelle direction elles peuvent dépendre. Le chapitre 5 expliquera comment les objets concrets sont créés et reliés à l’exécution.

## 4. Vocabulaire architectural

### 4.1 Architecture

L’architecture est l’ensemble des décisions qui déterminent :

- où se trouve chaque responsabilité ;
- quelles parties peuvent communiquer ;
- quelles dépendances sont autorisées ;
- comment une fonctionnalité peut évoluer sans obliger tout le projet à changer.

Une arborescence de dossiers n’est pas, à elle seule, une architecture. Elle devient utile lorsqu’elle matérialise des règles de responsabilité et de dépendance.

### 4.2 Module

Un module est un ensemble cohérent de fichiers qui réalise une capacité identifiable du jeu.

Exemples futurs :

- `beacons` ;
- `characters` ;
- `inventory` ;
- `economy` ;
- `quests` ;
- `local_ai`.

Un module possède :

- un objectif ;
- des données qu’il contrôle ;
- une interface publique ;
- des détails internes ;
- des dépendances déclarées ;
- des tests ou critères d’acceptation.

### 4.3 Couche

Une couche regroupe des responsabilités de même nature.

Dans ce guide, les couches principales sont :

1. **domaine** — règles et concepts métier du jeu ;
2. **application** — orchestration d’un cas d’usage ;
3. **présentation** — scènes, nœuds, interface et feedback ;
4. **données** — Resources, configurations et contenus de conception ;
5. **infrastructure** — fichiers, réseau, SQLite, services externes et adaptateurs ;
6. **outils** — scripts d’éditeur, génération, import et validation.

Une couche n’est pas obligatoirement un dossier dans chaque petit module. Elle devient un dossier lorsque la séparation améliore réellement la compréhension.

### 4.4 Dépendance

Le fichier A dépend du fichier B lorsque A doit connaître B pour fonctionner ou être analysé.

Exemples :

- une annotation `var profile: BeaconProfile` crée une dépendance vers `BeaconProfile` ;
- `preload("res://.../status_beacon.tscn")` crée une dépendance vers cette scène ;
- un appel à une méthode publique dépend du contrat de cette méthode ;
- une scène qui contient une autre scène dépend de son interface et de sa structure sérialisée.

### 4.5 Couplage

Le couplage mesure à quel point deux parties se connaissent.

Un couplage fort apparaît lorsque :

- un module connaît les chemins internes d’un autre ;
- plusieurs modules modifient directement les mêmes données ;
- une scène suppose des noms précis dans une scène extérieure ;
- une modification locale exige de modifier beaucoup de fichiers éloignés.

Un couplage faible signifie que les parties communiquent à travers une petite interface stable.

### 4.6 Cohésion

La cohésion mesure à quel point les éléments d’un module servent le même objectif.

Un module `inventory` contenant inventaire, météo, dialogue et musique possède une faible cohésion.

Un module `beacons` contenant profil, scène de balise, interface publique et tests de balise possède une meilleure cohésion.

### 4.7 Contrat

Un contrat décrit ce qu’une partie promet aux autres :

- une fonction et sa signature ;
- un signal et ses arguments ;
- une classe abstraite ;
- un format de Resource ;
- un schéma JSON ;
- une convention documentée et contrôlée.

Un contrat décrit **ce qui est disponible**, pas tous les détails de l’implémentation.

### 4.8 Frontière

Une frontière sépare l’interface publique des détails internes.

Pour `StatusBeacon` :

- `activate()` et les signaux constituent l’interface publique ;
- `StatusLabel`, `CooldownTimer` et `_refresh_label()` sont internes ;
- une scène extérieure ne doit pas manipuler ces détails directement.

## 5. Principes retenus pour `Project Asteria`

### 5.1 Organiser d’abord par fonctionnalité

Godot recommande de conserver les ressources proches des scènes qui les utilisent lorsque cela améliore la maintenance. `Project Asteria` adopte donc une organisation **feature-first** : les fichiers propres à une fonctionnalité restent dans le même module.

> **[LECTURE] Comparaison conceptuelle - Ne pas créer ces dossiers tels quels.**

```text
Organisation uniquement par type             Organisation par fonctionnalité
scripts/                                      src/features/beacons/
├── beacon.gd                                 ├── presentation/status_beacon.gd
├── inventory.gd                              ├── presentation/status_beacon.tscn
└── quest.gd                                  ├── domain/beacon_profile.gd
scenes/                                       ├── data/default_beacon.tres
├── beacon.tscn                               └── README.md
├── inventory.tscn
└── quest.tscn
```

Avec une organisation uniquement par type, une fonctionnalité est dispersée dans plusieurs grandes arborescences. Avec une organisation par fonctionnalité, son code, ses scènes et ses données proches peuvent être découverts ensemble.

### 5.2 Utiliser des couches locales seulement lorsque nécessaire

Un module de trois fichiers n’a pas besoin de six dossiers vides.

Règle :

- commencer avec un module simple et cohérent ;
- créer une sous-couche lorsqu’au moins deux responsabilités différentes deviennent visibles ;
- ne jamais créer une couche uniquement pour imiter un diagramme théorique.

Le module `beacons` possède déjà une Resource de domaine et une scène de présentation. Deux sous-dossiers deviennent donc justifiés.

### 5.3 Dépendre vers les règles, pas vers les détails

La direction principale est :

> **[LECTURE] Direction de dépendance - Ne pas saisir.**

```text
Présentation ───────┐
                    ├──> Application ───> Domaine / contrats stables
Infrastructure ─────┘

Données de conception ───> types du domaine

App / Bootstrap ───> assemble les implémentations concrètes
Outils ─────────────> observent ou génèrent, sans devenir obligatoires au runtime
```

Les flèches signifient « peut dépendre de ».

Le domaine ne doit pas importer une scène, une interface graphique, un client HTTP ou une base SQLite.

### 5.4 Préférer la composition

Godot repose naturellement sur la composition de scènes et de nœuds.

Préférer :

- plusieurs petites scènes spécialisées ;
- une racine qui expose une interface claire ;
- des Resources pour les données ;
- des objets `RefCounted` pour une logique sans présence dans le `SceneTree` ;
- une classe abstraite seulement lorsqu’une famille partage réellement un contrat et une base.

Éviter les hiérarchies d’héritage profondes où chaque nouvelle variante dépend de tous les choix de ses ancêtres.

### 5.5 Garder les dépendances visibles

Une dépendance visible est :

- un paramètre ;
- une propriété exportée ;
- un constructeur ou une fonction de configuration ;
- une scène enfant explicite ;
- un contrat nommé.

Une dépendance cachée est :

- un chemin absolu recherché n’importe où dans l’arbre ;
- un Autoload supposé sans déclaration ;
- un nom de groupe non documenté ;
- un fichier chargé depuis une chaîne construite sans validation.

Le chapitre 5 montrera comment fournir ces dépendances concrètes.

## 6. Arborescence canonique

### 6.1 Structure cible

La structure canonique à ce stade est :

> **[LECTURE] Arborescence cible - Ne pas créer en recopiant le bloc ; suivre les étapes suivantes.**

```text
Project Asteria/
├── project.godot
├── addons/                         # plugins et composants tiers contrôlés
├── docs/
│   ├── .gdignore
│   └── architecture/
│       ├── README.md
│       ├── ADR-0001-feature-first.md
│       └── dependency-matrix.md
├── scenes/
│   ├── app/
│   └── learning/
├── src/
│   ├── app/                        # point d’entrée et composition
│   ├── core/
│   │   ├── contracts/              # contrats réellement partagés
│   │   ├── types/                  # petits types stables
│   │   └── utilities/              # utilitaires purs et limités
│   ├── features/
│   │   └── beacons/
│   │       ├── domain/
│   │       │   └── beacon_profile.gd
│   │       ├── presentation/
│   │       │   ├── status_beacon.gd
│   │       │   └── status_beacon.tscn
│   │       ├── data/
│   │       │   └── default_beacon.tres
│   │       ├── tests/
│   │       └── README.md
│   └── infrastructure/             # adaptateurs concrets futurs
├── tests/                          # tests transversaux et intégration
└── tools/
    └── .gdignore                   # scripts externes non importés par Godot
```

### 6.2 Rôle de chaque zone

| Zone | Responsabilité | Peut connaître |
|---|---|---|
| `src/app` | démarrage, scènes racines, composition | tous les modules concrets nécessaires au démarrage |
| `src/core` | contrats et types réellement communs | aucun module fonctionnel |
| `src/features` | capacités métier du jeu | `core`, ses propres couches, contrats explicitement autorisés |
| `src/infrastructure` | fichiers, réseau, bases et adaptateurs | contrats du domaine ou de l’application |
| `scenes/app` | scènes d’assemblage principales | présentations publiques des modules |
| `tests` | tests transversaux | modules soumis aux tests |
| `tools` | scripts externes et automatisation | fichiers du dépôt, jamais requis par un export runtime |
| `docs` | décisions et diagrammes | aucune dépendance runtime |
| `addons` | plugins ou ressources tierces | API du plugin et licence déclarée |

### 6.3 Pourquoi `.gdignore`

Godot utilise le système de fichiers du projet directement. Un fichier vide `.gdignore` empêche l’éditeur d’importer et d’afficher le contenu du dossier concerné.

Utiliser `.gdignore` pour :

- la documentation non chargée au runtime ;
- les scripts Python ou outils externes ;
- des fichiers de travail que Godot ne doit pas indexer.

Ne pas placer `.gdignore` dans un dossier contenant une Resource chargée avec `load()` ou `preload()`, car Godot ne pourra plus charger ce contenu.

## 7. Créer les dossiers d’architecture

Depuis la racine du projet :

> **[PS] PowerShell 7 - Créer les dossiers de l’architecture depuis la racine de `Project Asteria`.**

```powershell
$paths = @(
  "docs/architecture",
  "scenes/app",
  "src/app",
  "src/core/contracts",
  "src/core/types",
  "src/core/utilities",
  "src/features/beacons/domain",
  "src/features/beacons/presentation",
  "src/features/beacons/data",
  "src/features/beacons/tests",
  "src/infrastructure",
  "tests",
  "tools"
)

foreach ($path in $paths) {
  New-Item -ItemType Directory -Force -Path $path | Out-Null
}
```

Décomposition :

- `$paths` contient un tableau de chemins ;
- `@(...)` crée ce tableau sur plusieurs lignes ;
- `foreach` parcourt chaque chemin ;
- `$path` contient le chemin courant ;
- `New-Item` crée le dossier ;
- `-Force` accepte qu’un dossier existe déjà ;
- `| Out-Null` masque la sortie répétitive de PowerShell.

Créer les fichiers `.gdignore` :

> **[PS] PowerShell 7 - Créer les fichiers vides :** `docs/.gdignore` et `tools/.gdignore`.

```powershell
New-Item -ItemType File -Force -Path "docs/.gdignore" | Out-Null
New-Item -ItemType File -Force -Path "tools/.gdignore" | Out-Null
```

Vérifier :

> **[PS] PowerShell 7 - Afficher les dossiers créés.**

```powershell
Get-ChildItem -Directory -Recurse -Depth 3 |
  Select-Object -ExpandProperty FullName
```

## 8. Migrer le module `beacons`

### 8.1 Pourquoi utiliser le dock FileSystem de Godot

Les fichiers du chapitre 3 sont déjà référencés par des scènes et des Resources. Déplacer un fichier depuis l’Explorateur Windows ou PowerShell peut laisser des chemins obsolètes dans les fichiers Godot.

Pour cette migration, utiliser le dock **FileSystem** de Godot. L’éditeur peut mettre à jour les dépendances connues lors du déplacement.

### 8.2 Déplacements à effectuer

> **[APP] Godot Editor - Déplacer dans le dock FileSystem :** déplacer `src/features/beacons/beacon_profile.gd` vers `src/features/beacons/domain/beacon_profile.gd`.

> **[APP] Godot Editor - Déplacer dans le dock FileSystem :** déplacer `src/features/beacons/status_beacon.gd` et `src/features/beacons/status_beacon.tscn` vers `src/features/beacons/presentation/`.

> **[APP] Godot Editor - Déplacer dans le dock FileSystem :** déplacer `data/beacons/default_beacon.tres` vers `src/features/beacons/data/default_beacon.tres`.

Lorsque Godot demande de mettre à jour les dépendances, accepter la mise à jour.

Chemins cibles :

> **[SORTIE] Chemins attendus après migration - Ne pas saisir.**

```text
res://src/features/beacons/domain/beacon_profile.gd
res://src/features/beacons/presentation/status_beacon.gd
res://src/features/beacons/presentation/status_beacon.tscn
res://src/features/beacons/data/default_beacon.tres
```

### 8.3 Vérifier les références

Ouvrir :

- `status_beacon.tscn` ;
- `ch03_scene_signals_demo.tscn` ;
- `chapter03_demo.gd`.

Vérifier que les chemins ne sont pas marqués comme manquants.

> **[PS] PowerShell 7 - Rechercher les anciens chemins depuis la racine du projet.**

```powershell
$oldPaths = @(
  "src/features/beacons/beacon_profile.gd",
  "src/features/beacons/status_beacon.gd",
  "src/features/beacons/status_beacon.tscn",
  "data/beacons/default_beacon.tres"
)

foreach ($oldPath in $oldPaths) {
  Get-ChildItem -Recurse -File |
    Select-String -SimpleMatch $oldPath
}
```

Aucune occurrence active ne doit rester dans les fichiers du projet. Les mentions historiques dans une documentation peuvent être conservées si elles expliquent la migration.

### 8.4 Ne pas déplacer automatiquement tout le projet

Une migration architecturale doit rester progressive.

Ne pas :

- déplacer plusieurs centaines de fichiers en une seule opération non vérifiée ;
- renommer simultanément dossiers, classes et scènes ;
- mélanger la migration avec une nouvelle fonctionnalité importante ;
- supprimer les anciens chemins avant d’avoir validé les références.

## 9. Documenter le module `beacons`

Créer un README local :

> **[VSC] Visual Studio Code - Créer :** `src/features/beacons/README.md`.

```markdown
# Module beacons

## Responsabilité

Afficher et publier l’activation locale d’une balise de statut.

## Interface publique

- classe `StatusBeacon` ;
- fonction `activate(actor_name: StringName) -> bool` ;
- signal `activated(beacon_id: StringName, message: String)` ;
- signal `availability_changed(is_available: bool)` ;
- Resource `BeaconProfile`.

## Données contrôlées

- identité et texte d’une balise ;
- durée de cooldown de conception ;
- disponibilité runtime de chaque instance.

## Dépendances autorisées

- classes Godot standard ;
- contrats stables de `src/core` lorsqu’ils existeront.

## Dépendances interdites

- Autoload global non déclaré ;
- base SQLite ;
- service réseau ;
- interface interne d’un autre module.

## Frontière

Les autres modules appellent l’interface publique de `StatusBeacon` ou écoutent ses signaux. Ils ne manipulent pas `StatusLabel` ni `CooldownTimer`.

## Validation

La scène de démonstration du chapitre 3 reste exécutable après chaque modification du module.
```

### 9.1 Pourquoi ce README est utile

Il permet de répondre rapidement à cinq questions :

1. que possède le module ?
2. que peut appeler un autre module ?
3. de quoi dépend-il ?
4. que ne doit-il pas connaître ?
5. comment vérifier qu’il fonctionne encore ?

## 10. Définir les couches

### 10.1 Domaine

Le domaine contient les concepts et règles propres au jeu.

Exemples :

- identifiant de balise ;
- règle de cooldown ;
- état d’une quête ;
- montant d’une transaction ;
- relation entre personnages.

Le domaine doit rester aussi indépendant que raisonnablement possible de l’interface graphique, du réseau et du stockage.

Dans le module `beacons`, `BeaconProfile` représente actuellement une donnée de conception proche du domaine.

### 10.2 Application

La couche application orchestre une intention :

- activer une balise ;
- démarrer une quête ;
- transférer un objet ;
- sauvegarder une partie.

Elle décide dans quel ordre appeler les règles et contrats, sans connaître les détails d’affichage ou de stockage.

Ce chapitre ne crée pas encore de service d’application complet. Le chapitre 5 introduira leur construction et leurs dépendances.

### 10.3 Présentation

La présentation contient :

- scènes ;
- nœuds ;
- UI ;
- animations de feedback ;
- sons directement liés à la vue ;
- adaptation des entrées utilisateur vers une intention.

`StatusBeacon` appartient à cette couche, car elle est une scène 3D et affiche un label.

### 10.4 Données

La couche données contient les contenus de conception :

- Resources `.tres` ;
- catalogues ;
- tables de configuration ;
- données de localisation ;
- valeurs équilibrées par les designers.

Elle ne doit pas devenir un emplacement fourre-tout pour toutes les variables runtime.

### 10.5 Infrastructure

L’infrastructure contient les détails techniques externes :

- système de fichiers ;
- SQLite ;
- HTTP et WebSocket ;
- appels vers les services IA ;
- télémétrie ;
- intégration de plateforme.

L’infrastructure doit fournir des implémentations de contrats définis plus près du domaine ou de l’application.

### 10.6 Outils

Les outils assistent la production mais ne sont pas requis par le jeu exporté :

- scripts Python ;
- validateurs ;
- importateurs ;
- génération de données ;
- scripts Blender ;
- rapports de build.

Le dossier `tools/` possède `.gdignore` lorsqu’il contient des fichiers que Godot ne doit pas importer.

## 11. Matrice des dépendances

Créer la matrice :

> **[VSC] Visual Studio Code - Créer :** `docs/architecture/dependency-matrix.md`.

```markdown
# Matrice des dépendances

| Couche source | Couches cibles autorisées |
|---|---|
| Domaine | Domaine, Core |
| Application | Domaine, Application, Données*, Core |
| Présentation | Domaine, Application, Présentation, Données, Core |
| Données | Domaine, Données, Core |
| Infrastructure | Domaine, Application, Données, Infrastructure, Core |
| Core | Core |
| App / Bootstrap | Toutes les couches nécessaires à l’assemblage |

* L’application lit des types de données stables. Elle ne choisit pas
  directement un chemin de fichier ou une base concrète.

L’application dépend d’un contrat. Le point `App / Bootstrap` fournit
l’implémentation d’infrastructure correspondante.
```

### 11.1 Lire la matrice

La ligne **Domaine** ne possède aucune dépendance vers présentation ou infrastructure.

La ligne **Présentation** peut appeler l’application ou afficher des types du domaine. Elle ne doit pas ouvrir directement une base SQLite.

La ligne **Infrastructure** peut implémenter un contrat d’application et convertir les données externes vers les types du domaine.

La ligne **App / Bootstrap** est la seule autorisée à connaître de nombreux éléments concrets, car sa responsabilité est précisément de les assembler.

### 11.2 Les dépendances entre modules

Deux modules fonctionnels ne doivent pas importer librement leurs détails internes.

Préférer :

- un contrat dans `core/contracts` lorsque plusieurs modules en ont réellement besoin ;
- une fonction publique du module propriétaire ;
- un signal local ;
- une orchestration dans la couche application ;
- un adaptateur dans l’infrastructure.

Éviter :

> **[LECTURE] Exemple de dépendance interdite - Ne pas recopier.**

```gdscript
# Le module inventory atteint un enfant interne du module characters.
var label: Label3D = get_node("/root/Main/World/Player/Status/NameLabel")
label.text = "Chargé"
```

Cette ligne dépend de toute la structure de scène du personnage.

Préférer une API publique :

> **[LECTURE] Exemple de contrat public - Étudier la différence.**

```gdscript
player_status.set_state_text("Chargé")
```

Le module appelant dépend encore d’une fonction, mais ne connaît plus l’arbre interne.

## 12. Contrats dans GDScript

### 12.1 Contrat par signature publique

La forme la plus simple est une classe concrète dont la petite API est documentée et typée.

> **[LECTURE] Contrat public existant - Ne pas recopier isolément.**

```gdscript
func activate(actor_name: StringName) -> bool:
```

Ce contrat promet :

- un paramètre `actor_name` de type `StringName` ;
- un résultat `bool` ;
- `true` si l’action est acceptée ;
- `false` si elle est refusée.

### 12.2 Classe abstraite

Godot 4.7 permet de déclarer des classes et méthodes abstraites avec `@abstract`.

Une classe abstraite est utile lorsqu’une famille d’objets partage une base et doit obligatoirement fournir certaines méthodes.

> **[VSC] Visual Studio Code - Exemple à créer seulement lorsqu’un second composant activable justifie le contrat :** `src/core/contracts/activatable.gd`.

```gdscript
@abstract
class_name Activatable
extends RefCounted
## Contrat minimal pour une opération d’activation sans présence dans le SceneTree.


@abstract func activate(actor_name: StringName) -> bool
```

Décomposition :

- `@abstract` empêche l’instanciation directe ;
- `class_name Activatable` crée un type global ;
- `extends RefCounted` indique que le contrat décrit un objet léger sans nœud ;
- la méthode abstraite ne possède pas de corps ;
- une classe concrète qui hérite de ce contrat doit fournir une signature compatible.

Limite : GDScript utilise un héritage de classe unique. Une scène dont la racine étend déjà `Node3D` ne peut pas également hériter de `Activatable`.

Ne pas forcer une classe abstraite lorsque la composition ou une petite API publique suffit.

### 12.3 Duck typing et `has_method()`

GDScript permet d’appeler une méthode selon sa présence plutôt que selon une interface formelle.

> **[LECTURE] Exemple flexible - Étudier les contrôles.**

```gdscript
func try_activate(candidate: Object, actor_name: StringName) -> bool:
	if not candidate.has_method("activate"):
		push_warning("L’objet ne respecte pas le contrat activate().")
		return false

	var result: Variant = candidate.call("activate", actor_name)
	if result is not bool:
		push_warning("activate() doit renvoyer un booléen.")
		return false

	return result
```

Décomposition :

- `candidate: Object` accepte tout objet Godot ;
- `has_method("activate")` vérifie la présence de la méthode ;
- `call()` réalise un appel dynamique ;
- le résultat est d’abord un `Variant` ;
- `result is not bool` détecte un retour incompatible ;
- `return result` renvoie la valeur après cette vérification.

Cette approche est flexible mais moins sûre qu’un type statique. L’utiliser pour une frontière dynamique clairement documentée, pas pour éviter toute conception.

### 12.4 Contrat par signal

Un signal est un contrat d’événement.

> **[LECTURE] Contrat d’événement existant - Ne pas recopier isolément.**

```gdscript
signal activated(beacon_id: StringName, message: String)
```

Le module promet que chaque émission fournit l’identifiant puis le message, dans cet ordre.

### 12.5 Contrat par Resource

Une Resource typée peut décrire un format de données éditable.

`BeaconProfile` promet actuellement :

- un identifiant ;
- un nom affiché ;
- un message ;
- une durée de cooldown.

Le chapitre 7 ajoutera validation, versions et migrations des données.

## 13. Composition et point d’entrée

### 13.1 Composition root

Le **composition root** est l’endroit où les implémentations concrètes sont créées et reliées.

Dans `Project Asteria`, ce rôle appartient progressivement à `src/app` et aux scènes de `scenes/app`.

Il peut :

- instancier les modules ;
- leur fournir des dépendances ;
- connecter les signaux entre grandes parties ;
- choisir une implémentation locale ou simulée ;
- démarrer le flux principal.

Les modules ne doivent pas tous devenir des enfants directs d’un gigantesque `Main` avec des références croisées. Le point d’entrée assemble des sous-arbres cohérents.

### 13.2 Structure de scène de départ

> **[LECTURE] Structure de composition proposée - Ne pas saisir.**

```text
Main
├── World
│   ├── GameplayModules
│   └── CurrentLevel
├── Interface
└── Diagnostics
```

Cette structure décrit des responsabilités, pas uniquement des positions spatiales.

- `World` contient le monde 3D ;
- `GameplayModules` accueille les systèmes liés au monde ;
- `CurrentLevel` contient la scène de niveau active ;
- `Interface` reste séparée du monde ;
- `Diagnostics` rassemble les informations de développement.

Le chapitre 5 décidera quels systèmes doivent être des nœuds persistants, des services injectés ou des Autoloads.

## 14. Éviter les anti-patterns

### 14.1 Le dossier `managers/`

Un dossier rempli de `SomethingManager.gd` cache souvent des responsabilités imprécises.

Avant de créer un manager, préciser :

- quelles données il possède ;
- quelle action unique il réalise ;
- pourquoi cette action ne vit pas dans un module existant ;
- qui le crée ;
- qui peut l’appeler ;
- comment le tester.

### 14.2 Le singleton omniprésent

Un Autoload est accessible depuis tout le projet. Cette facilité peut créer :

- un état global ;
- des appels impossibles à tracer ;
- des tests dépendants de l’ordre de démarrage ;
- une responsabilité excessive.

Le chapitre 5 expliquera les cas où un Autoload reste justifié.

Dans ce chapitre, la règle est :

> ne pas choisir un Autoload uniquement pour éviter de transmettre une dépendance.

### 14.3 La scène monolithique

Une scène devient monolithique lorsque :

- elle contient de nombreux sous-systèmes indépendants ;
- son script racine modifie directement des dizaines d’enfants ;
- elle ne peut pas être testée partiellement ;
- toute modification produit des conflits de fusion.

Extraire une branche en sous-scène lorsque cette branche :

- possède une responsabilité ;
- peut exposer une interface ;
- peut être testée ou prévisualisée seule ;
- est réutilisable ou maintenue séparément.

### 14.4 Le dossier `shared/` sans règle

Un dossier partagé devient facilement une décharge.

Une classe ne rejoint `core` ou un espace partagé que si :

- au moins deux modules réels l’utilisent ;
- son sens est identique dans ces modules ;
- elle ne dépend pas d’un module particulier ;
- son contrat est stable ;
- son propriétaire est identifié.

### 14.5 Les couches qui se contournent

Exemple interdit : la présentation ouvre directement SQLite parce que cela semble plus rapide.

Ce raccourci lie l’interface à la base, rend les tests difficiles et empêche une autre source de données.

La présentation doit demander une action à l’application ; l’infrastructure fournit l’accès concret.

### 14.6 L’architecture spéculative

Créer immédiatement :

- vingt interfaces ;
- un bus global ;
- plusieurs fabriques ;
- une hiérarchie abstraite profonde ;
- des dossiers vides pour tous les systèmes futurs ;

n’est pas une preuve de qualité.

Appliquer YAGNI : créer une abstraction lorsque deux besoins concrets révèlent une variation ou une frontière utile.

## 15. Architecture Decision Records

### 15.1 Rôle d’une ADR

Une ADR conserve une décision d’architecture importante avec son contexte et ses conséquences.

Elle évite de perdre la réponse à la question : « Pourquoi avons-nous choisi cette organisation ? »

Une ADR n’est pas un journal quotidien. Elle documente une décision qui influence durablement la structure ou les contraintes du projet.

### 15.2 Créer l’ADR initiale

> **[VSC] Visual Studio Code - Créer :** `docs/architecture/ADR-0001-feature-first.md`.

```markdown
# ADR-0001 — Organisation feature-first

- Statut : accepté
- Date : 2026-07-18
- Décideur : propriétaire du projet

## Contexte

Project Asteria doit accueillir de nombreux systèmes de gameplay,
des données persistantes, des services IA et deux parcours.

Une organisation uniquement par type de fichier disperserait
chaque fonctionnalité.

## Décision

Le projet utilise une organisation feature-first.

Chaque module regroupe ses scènes, scripts et données proches.
Les sous-couches sont créées uniquement lorsqu’une responsabilité
réelle existe.

Les dépendances vont vers le domaine et les contrats stables.
`src/app` constitue le point de composition.

## Conséquences positives

- localisation plus rapide des fichiers ;
- meilleure cohésion ;
- frontières de responsabilité visibles ;
- réduction des conflits entre fonctionnalités ;
- migration progressive possible ;
- Companion Pack organisé par modules réutilisables.

## Conséquences négatives

- les types de fichiers sont répartis dans plusieurs modules ;
- les règles doivent être documentées et contrôlées ;
- une fonction transversale exige un contrat explicite ;
- déplacer un fichier partagé exige une décision.

## Alternatives considérées

1. dossiers globaux par type de fichier ;
2. couches globales strictes ;
3. aucune règle formelle avant les premiers problèmes.

## Révision

Réévaluer après les chapitres 9, 13 et 25, ou lorsque trois
modules contournent la matrice de dépendances.
```

### 15.3 Statuts d’une ADR

Statuts recommandés :

- `proposé` ;
- `accepté` ;
- `rejeté` ;
- `déprécié` ;
- `remplacé par ADR-XXXX`.

Ne pas effacer une ancienne ADR acceptée. Une nouvelle ADR peut la remplacer tout en conservant l’historique.

## 16. Document d’architecture principal

Créer :

> **[VSC] Visual Studio Code - Créer :** `docs/architecture/README.md`.

```markdown
# Architecture de Project Asteria

## Principes

1. Organisation par fonctionnalité.
2. Couches locales uniquement lorsqu’elles sont utiles.
3. Dépendances dirigées vers le domaine et les contrats.
4. Composition de petites scènes et objets spécialisés.
5. Point d’assemblage dans `src/app`.
6. Infrastructure remplaçable derrière des contrats.
7. Outils absents du runtime exporté.
8. Aucune dépendance globale implicite.

## Sources de vérité

- `dependency-matrix.md` ;
- ADR acceptées ;
- README de chaque module ;
- tests et validations d’architecture.

## Modules actifs

| Module | Responsabilité | État |
|---|---|---|
| `beacons` | balise de statut locale | démonstration pédagogique |

## Règle de modification

Toute nouvelle dépendance entre modules doit être ajoutée à la matrice ou justifiée par une ADR.
```

## 17. Règles de nommage et ownership

### 17.1 Fichiers et dossiers

Utiliser :

- `snake_case` pour fichiers et dossiers ;
- `PascalCase` pour les noms de nœuds ;
- `PascalCase` pour les classes `class_name` ;
- `snake_case` pour fonctions et variables ;
- `UPPER_SNAKE_CASE` pour constantes.

Ces règles évitent également des erreurs de casse lors des exports vers des systèmes sensibles à la casse.

### 17.2 Propriétaire fonctionnel

Chaque module possède ses fichiers.

« Posséder » signifie :

- décider de son interface ;
- valider ses changements ;
- maintenir ses données ;
- fournir sa documentation ;
- corriger ses régressions.

Le terme ne doit pas être confondu avec la propriété Godot `Node.owner` expliquée au chapitre 3.

### 17.3 Interface publique et interne

Convention :

- les méthodes publiques nécessaires aux autres modules ne commencent pas par `_` ;
- les méthodes internes commencent par `_` ;
- les enfants internes ne sont pas exposés sans besoin ;
- le README liste l’API publique ;
- une modification incompatible exige une migration ou une décision explicite.

Le préfixe `_` est une convention, pas un mécanisme de sécurité absolu.

## 18. Règles d’import et de chargement

### 18.1 Chemins stables

Un chemin `res://` fait partie du contrat lorsqu’il est chargé directement par d’autres modules.

Limiter les chemins publics. Préférer :

- une classe `class_name` ;
- une Resource assignée dans l’Inspector ;
- un catalogue ;
- un point de création centralisé ;
- une constante publique du module lorsque le chemin doit être exposé.

### 18.2 Déplacements de fichiers

Déplacer les Resources et scènes depuis le dock FileSystem de Godot lorsque des dépendances existent.

Après déplacement :

1. ouvrir les scènes concernées ;
2. rechercher les anciens chemins ;
3. exécuter l’import headless ;
4. lancer les scènes de démonstration ;
5. vérifier `git diff`.

### 18.3 Ressources tierces

Conserver les plugins dans `addons/` lorsqu’ils utilisent cette convention Godot.

Pour chaque dépendance tierce, enregistrer :

- nom ;
- version ;
- source ;
- licence ;
- fichiers modifiés ;
- procédure de mise à jour ;
- procédure de suppression.

## 19. Validation de l’architecture

### 19.1 Vérification manuelle

Pour chaque nouveau fichier, demander :

1. quelle responsabilité possède-t-il ?
2. quel module le possède ?
3. quelle couche représente-t-il ?
4. de quoi dépend-il ?
5. cette dépendance est-elle autorisée ?
6. l’interface est-elle plus petite que l’implémentation ?
7. peut-il être testé ou démontré isolément ?
8. faut-il une ADR ?

### 19.2 Recherche de chemins absolus fragiles

> **[PS] PowerShell 7 - Rechercher les accès absolus à `/root` dans les scripts GDScript.**

```powershell
Get-ChildItem -Path "src" -Recurse -Filter "*.gd" |
  Select-String -Pattern 'get_node\("/root/'
```

Une occurrence n’est pas automatiquement une erreur, mais elle doit être justifiée. Les Autoloads futurs apparaîtront probablement sous `/root`.

### 19.3 Rechercher les imports entre modules

> **[PS] PowerShell 7 - Rechercher les chemins vers d’autres modules fonctionnels.**

```powershell
Get-ChildItem -Path "src/features" -Recurse -Filter "*.gd" |
  Select-String -Pattern 'res://src/features/'
```

Examiner chaque résultat. Un fichier peut charger un autre fichier de son propre module. Une dépendance vers un module différent doit respecter la matrice.

### 19.4 Import headless

> **[PS] PowerShell 7 - Valider les chemins et imports depuis la racine de `Project Asteria`.**

```powershell
godot --headless --path . --import
```

Cette commande détecte notamment certains chemins de Resources ou scripts devenus invalides.

### 19.5 Relancer la scène du chapitre 3

> **[PS] PowerShell 7 - Exécuter la démonstration après migration.**

```powershell
godot --headless --path . --scene "res://scenes/learning/ch03_scene_signals_demo.tscn" --quit-after 180
```

La démonstration doit produire les mêmes événements qu’avant la migration.

## 20. Exemple de revue d’une dépendance

Demande : le module `quests` veut afficher une notification.

### Solution fragile

`quests` cherche directement un label dans la scène principale.

Problèmes :

- dépendance au chemin ;
- dépendance à l’UI ;
- impossible à tester sans la scène complète ;
- modification de l’UI susceptible de casser les quêtes.

### Solution transitoire acceptable

Le point de composition fournit au module de quêtes un `Callable` de notification.

> **[LECTURE] Exemple architectural simplifié - Ne pas intégrer avant le chapitre 5.**

```gdscript
var notify: Callable


func complete_quest() -> void:
	# Met à jour les règles du module.
	if notify.is_valid():
		notify.call("Quête terminée")
```

Le module connaît uniquement un `Callable`.

### Solution à long terme

Le chapitre 5 pourra introduire un contrat de notification et fournir une implémentation concrète depuis le point de composition.

L’architecture ne cherche pas la solution la plus abstraite immédiatement. Elle cherche une dépendance visible, limitée et remplaçable.

## 21. Mode Solo et Mode Studio

### 21.1 Mode Solo

Le parcours Solo applique un minimum rigoureux :

- organisation feature-first ;
- README pour les modules importants ;
- une matrice de dépendances ;
- ADR seulement pour les décisions durables ;
- revue architecturale lors d’un nouveau module ;
- migration progressive ;
- aucune abstraction sans besoin concret.

Le développeur Solo peut conserver une couche à la racine du module tant que les responsabilités restent évidentes.

### 21.2 Mode Studio

Le parcours Studio ajoute :

- propriétaires de modules ou équipes responsables ;
- revue obligatoire des nouvelles dépendances ;
- ADR discutées dans les pull requests ;
- contrôle CI des imports interdits ;
- conventions de compatibilité des interfaces ;
- politique de dépréciation ;
- tests de contrats ;
- diagrammes mis à jour ;
- CODEOWNERS lorsque l’organisation GitHub le justifie.

Une équipe Studio ne doit pas utiliser la matrice comme justification bureaucratique. Elle doit automatiser les règles stables et réserver les revues humaines aux décisions réelles.

## 22. Erreurs fréquentes et diagnostics

### 22.1 « Je ne sais pas où mettre ce fichier »

Demander d’abord sa responsabilité et son propriétaire fonctionnel.

- spécifique à une fonctionnalité : module de cette fonctionnalité ;
- contrat stable partagé : `core/contracts` ;
- détail de stockage ou réseau : `infrastructure` ;
- scène d’assemblage : `scenes/app` ou `src/app` ;
- outil absent du runtime : `tools`.

### 22.2 Dépendance circulaire

Symptômes :

- module A charge B ;
- B charge A ;
- ordre d’analyse ou d’initialisation fragile ;
- responsabilité impossible à attribuer.

Corrections :

- extraire un contrat stable ;
- déplacer l’orchestration dans `app` ou application ;
- utiliser un signal pour une réaction ;
- fusionner les modules si leur séparation est artificielle.

### 22.3 Trop de petits fichiers

Une fonction privée de trois lignes n’a pas besoin de sa propre classe.

Regrouper ce qui change ensemble et possède la même responsabilité.

### 22.4 Module trop gros

Un module qui possède plusieurs vocabulaires et plusieurs cycles de vie peut cacher plusieurs capacités.

Exemple : un module `characters` pourra plus tard séparer apparence, locomotion et relations si ces parties évoluent indépendamment.

### 22.5 `core` dépend d’une fonctionnalité

`core` ne doit pas importer `beacons`, `inventory` ou `quests`.

Déplacer le type vers son module ou reformuler un contrat réellement générique.

### 22.6 Documentation et code divergent

Mettre à jour dans la même pull request :

- README du module ;
- matrice ;
- ADR si décision modifiée ;
- diagramme ;
- fichiers déplacés ;
- tests et scènes de démonstration.

## 23. Checklist de fin de chapitre

- [ ] Je peux définir module, couche, dépendance, couplage, cohésion et contrat.
- [ ] Je comprends l’organisation feature-first.
- [ ] Je n’ajoute pas des couches vides sans responsabilité réelle.
- [ ] Je connais la direction générale des dépendances.
- [ ] Le domaine n’importe pas présentation ou infrastructure.
- [ ] Je sais pourquoi `src/app` est un point de composition.
- [ ] Je distingue contrat public, classe abstraite, signal et duck typing.
- [ ] Je sais qu’une classe abstraite ne remplace pas la composition.
- [ ] Je peux lire la matrice de dépendances.
- [ ] Je sais quand créer une ADR.
- [ ] Le module `beacons` possède un README et une frontière documentée.
- [ ] Les fichiers du module sont déplacés depuis le dock FileSystem de Godot.
- [ ] Les anciens chemins ne restent pas dans les fichiers actifs.
- [ ] La démonstration du chapitre 3 fonctionne après migration.
- [ ] Les dossiers `docs` et `tools` utilisent `.gdignore` sans masquer de Resources runtime.
- [ ] Chaque commande et contenu de fichier indique son outil et son chemin.

## 24. Critères d’acceptation

Le chapitre est réussi lorsque :

1. l’arborescence canonique est créée sans dossiers spéculatifs inutiles ;
2. les fichiers `beacons` sont regroupés dans leur module avec couches `domain`, `presentation` et `data` ;
3. Godot ne signale aucune dépendance manquante après déplacement ;
4. `src/features/beacons/README.md` décrit responsabilité, interface et dépendances ;
5. `docs/architecture/dependency-matrix.md` existe ;
6. `docs/architecture/ADR-0001-feature-first.md` existe et possède un statut ;
7. `docs/architecture/README.md` indique les principes et modules actifs ;
8. les anciens chemins ne sont plus utilisés par les scènes ou scripts actifs ;
9. l’import headless réussit ;
10. la démonstration du chapitre 3 reste fonctionnelle ;
11. aucune dépendance circulaire n’est introduite ;
12. la réserve runtime reste déclarée tant que le Starter Kit ne contient pas et n’exécute pas ces fichiers.

## 25. Ce que le chapitre suivant ajoutera

Le chapitre 5 définira :

- service, manager, repository, controller et système ;
- Autoloads et leurs limites ;
- registre de services ;
- injection de dépendances ;
- bus d’événements typé et limité ;
- initialisation et arrêt ;
- variantes Solo et Studio.

Il utilisera la structure et la matrice du présent chapitre pour assembler les implémentations sans créer de dépendances globales implicites.

## 26. Sources vérifiées

- [Godot 4.7 — Project organization](https://docs.godotengine.org/en/4.7/tutorials/best_practices/project_organization.html)
- [Godot 4.7 — Scene organization](https://docs.godotengine.org/en/4.7/tutorials/best_practices/scene_organization.html)
- [Godot 4.7 — Applying object-oriented principles](https://docs.godotengine.org/en/4.7/tutorials/best_practices/what_are_godot_classes.html)
- [Godot 4.7 — When to use scenes versus scripts](https://docs.godotengine.org/en/4.7/tutorials/best_practices/scenes_versus_scripts.html)
- [Godot 4.7 — Autoloads versus regular nodes](https://docs.godotengine.org/en/4.7/tutorials/best_practices/autoloads_versus_regular_nodes.html)
- [Godot 4.7 — Godot interfaces](https://docs.godotengine.org/en/4.7/tutorials/best_practices/godot_interfaces.html)
- [Godot 4.7 — GDScript abstract classes and methods](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/gdscript_basics.html)
- [Architectural Decision Records — ADR community](https://adr.github.io/)

## 27. Résumé

`Project Asteria` adopte une architecture feature-first : chaque capacité regroupe ses scènes, scripts et données proches, puis ajoute des couches locales uniquement lorsqu’elles correspondent à des responsabilités réelles.

La direction de dépendance protège le domaine des détails de présentation et d’infrastructure. `src/app` assemble les implémentations concrètes. Les modules exposent une petite interface publique, documentent leurs dépendances et conservent leurs détails internes.

L’architecture n’est pas un ensemble de dossiers décoratifs. Elle constitue une série de décisions vérifiables, conservées par une matrice, des README, des ADR et des critères de validation.