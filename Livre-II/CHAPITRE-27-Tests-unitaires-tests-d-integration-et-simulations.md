---
title: "Livre II — Chapitre 27 : Tests unitaires, tests d’intégration et simulations"
id: "DOC-L2-CH27"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 27
last-verified: "2026-07-21T21:00:05+02:00"
audit-status: "complete"
audit-date: "2026-07-21T21:00:05+02:00"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-27.md"
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
---

# Tests unitaires, tests d’intégration et simulations

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH27`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-27.md`.  
> **Explications de code :** structurées bloc par bloc ; les sections d’erreurs conservent la séquence directe symptôme, exemple fautif, explication, exemple corrigé et explication de la correction.

## 1. Rôle du chapitre

Les chapitres 1 à 26 ont défini des contrats, des frontières d’autorité, des formats versionnés, des commandes, des résultats et des invariants. Le présent chapitre transforme ces décisions en vérifications répétables.

Un test utile ne démontre pas seulement qu’une fonction « marche ». Il précise une entrée, une observation et une règle qui doit rester vraie. Cette précision permet de détecter une régression, de localiser une responsabilité et de refuser un changement dont les conséquences ne sont pas maîtrisées.

Le chapitre construit quatre niveaux complémentaires :

- les tests unitaires des règles pures ou faiblement couplées ;
- les tests d’intégration des scènes, dépôts, codecs et adaptateurs ;
- les simulations déterministes de plusieurs ticks ou de plusieurs systèmes ;
- les campagnes de non-régression qui rejouent des scénarios et des graines connues.

## 2. Prérequis et frontières

Le lecteur doit connaître les fonctions, classes, `Resource`, scènes, signaux, dépôts, ports, commandes, résultats, horloges logiques, graines pseudo-aléatoires, sauvegardes et pipelines documentés précédemment.

Le chapitre utilise **GUT** comme framework de test GDScript pour le projet. Les tests intégrés au moteur Godot avec `--test` concernent le moteur compilé avec ses tests C++ ; la documentation officielle précise que le runner GDScript interne du moteur n’est pas destiné aux scripts utilisateur. Le projet adopte donc un framework installé sous `addons/gut`.

La version de GUT doit correspondre à la branche Godot utilisée. Pour Godot `4.7.x`, le dépôt officiel de GUT publie une branche `godot_4_7`. Le Starter Kit devra enregistrer le commit exact retenu et conserver la licence MIT fournie avec l’add-on. Le présent chapitre ne prétend pas avoir installé ou exécuté ce composant.

Le chapitre 28 approfondira journaux structurés, corrélation et reproductibilité opérationnelle. Le chapitre 29 automatisera les campagnes Python et la génération de données. Le chapitre 30 décidera l’organisation globale des parcours Solo et Studio. Ici, les suites et leurs contrats restent centrés sur Godot et GDScript.

## 3. Portfolio de tests
> **[LECTURE] Portfolio de vérification — Ne pas saisir.**

```text
Règle pure
    ↓ test unitaire
Service + ports en mémoire
    ↓ test de composant
Scène + SceneTree + signaux
    ↓ test d’intégration
Plusieurs systèmes + horloge + graines
    ↓ simulation déterministe
Scénarios et résultats approuvés
    ↓ campagne de non-régression
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le schéma classe les vérifications par quantité d’infrastructure réellement mobilisée, sans réduire la stratégie à une pyramide abstraite.
- **Déroulement ou instructions importantes :** Chaque flèche augmente la surface intégrée : règle, composant, scène, monde simulé puis corpus de scénarios.
- **Invariants protégés :** Un test ne change pas de catégorie parce qu’il est rapide ; sa catégorie dépend des frontières qu’il traverse.
- **Résultat attendu :** Le lecteur peut choisir la suite la plus petite capable d’observer l’invariant visé.

## 4. Définitions opérationnelles

### 4.1 Test unitaire

Un test unitaire exerce une règle ou un objet avec des dépendances remplacées par des valeurs ou des doubles contrôlés. Il ne lit pas un fichier réel, n’ouvre pas une base, ne dépend pas d’une scène globale et ne consulte pas l’heure système.

### 4.2 Test d’intégration

Un test d’intégration vérifie qu’au moins deux composants réels coopèrent selon leur contrat : codec et dépôt, scène et contrôleur, service et base temporaire, pipeline et système de fichiers de test.

### 4.3 Simulation déterministe

Une simulation applique une séquence de ticks, commandes ou événements à un état initial contrôlé. La même version, le même scénario, les mêmes graines et les mêmes entrées doivent produire le même résultat canonique.

### 4.4 Campagne de non-régression

Une campagne rejoue un ensemble versionné de cas connus. Elle n’affirme pas que tous les comportements possibles sont corrects ; elle garantit que les invariants et résultats approuvés du corpus ne changent pas silencieusement.

## 5. Choisir et gouverner GUT
> **[LECTURE] Décision de dépendance — Ne pas saisir.**

```text
Framework       GUT
Famille         9.x pour Godot 4.x
Branche cible   godot_4_7 pour Godot 4.7.x
Installation    addons/gut
Licence         MIT incluse dans l’add-on
Autorité        outil de test, jamais runtime
Verrouillage    commit source exact dans le registre des dépendances
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** La famille majeure, la branche moteur, le chemin d’installation et la licence sont des propriétés distinctes de la dépendance.
- **Frontières d’autorité :** `addons/gut` peut charger les scripts de test mais ne possède aucune règle de gameplay ni donnée de partie.
- **Sécurité et licences :** Le commit source exact et la licence doivent être conservés afin qu’une mise à jour du framework soit une décision relue.
- **Limites et réserves :** La branche `godot_4_7` doit être testée avec le binaire de référence avant matérialisation du Starter Kit.

### 5.1 Installer depuis une archive contrôlée

L’installation recommandée consiste à télécharger l’archive correspondant à la branche ou au commit approuvé, puis à copier uniquement `addons/gut` dans le projet. Le dépôt officiel indique que sa structure complète n’est pas conçue comme un sous-module placé directement sous `addons`.

> **[WEB] Navigateur — Ouvrir le dépôt officiel `bitwes/Gut`, sélectionner la branche `godot_4_7`, relever le commit choisi et télécharger son archive.**

> **[APP] Explorateur de fichiers — Copier le dossier `addons/gut` de l’archive vers `Project Asteria/addons/gut`, en conservant `LICENSE.md`.**

> **[APP] Godot Editor — Ouvrir `Project > Project Settings > Plugins`, activer `Gut`, puis vérifier l’apparition du panneau GUT.**

L’activation du plugin facilite l’exécution locale, mais la ligne de commande reste l’autorité des campagnes automatisées.

## 6. Arborescence des tests
> **[LECTURE] Arborescence de référence — Ne pas saisir.**

```text
test/
├── unit/
│   ├── characters/
│   ├── economy/
│   └── ecology/
├── integration/
│   ├── scenes/
│   ├── persistence/
│   └── content_pipeline/
├── simulation/
│   ├── scenarios/
│   └── expected/
└── support/
    ├── builders/
    ├── fakes/
    ├── fixtures/
    └── canonical/
test-results/
└── .gitkeep
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des fichiers :** `unit`, `integration` et `simulation` séparent les coûts et frontières ; `support` contient uniquement les aides partagées.
- **Dépendances et ports utilisés :** Les builders et fakes peuvent dépendre des contrats du projet, mais le code de production ne dépend jamais de `test/`.
- **Résultat attendu :** Un nom de fichier et son dossier indiquent immédiatement le niveau de vérification et le système concerné.
- **Limites et réserves :** `expected` ne doit pas devenir un dépôt d’instantanés opaques ; chaque résultat approuvé conserve un scénario et une version.

## 7. Créer les dossiers

> **[PS] PowerShell 7 — Exécuter depuis la racine du projet Godot.**
> **[PS] PowerShell 7 — Créer l’arborescence de tests.**

```powershell
$paths = @(
  "test/unit",
  "test/integration",
  "test/simulation/scenarios",
  "test/simulation/expected",
  "test/support/builders",
  "test/support/fakes",
  "test/support/fixtures",
  "test/support/canonical",
  "test-results"
)

$paths | ForEach-Object {
  New-Item -ItemType Directory -Force -Path $_ | Out-Null
}

New-Item -ItemType File -Force -Path "test-results/.gitkeep" |
  Out-Null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et options importants :** `-ItemType Directory` crée les dossiers ; `-Force` rend l’opération répétable lorsque le chemin existe déjà.
- **Déroulement ou instructions importantes :** La boucle crée chaque racine avant le fichier `.gitkeep` qui permet de versionner un répertoire de résultats vide.
- **Effets de bord :** La commande ne supprime aucun fichier et n’écrit pas de résultat de test.
- **Résultat attendu :** Les quatre catégories de support et les trois suites apparaissent sous `test/`.

## 8. Configuration GUT

> **[VSC] Visual Studio Code — Créer `Project Asteria/.gutconfig.json`.**
> **[VSC] Fichier `.gutconfig.json` — Ne pas saisir dans un terminal.**

```json
{
  "dirs": [
    "res://test/unit/",
    "res://test/integration/",
    "res://test/simulation/"
  ],
  "double_strategy": "SCRIPT_ONLY",
  "ignore_pause": false,
  "include_subdirs": true,
  "log_level": 1,
  "prefix": "test_",
  "should_exit": true,
  "suffix": ".gd",
  "tests": [],
  "junit_xml_file": "res://test-results/gut.xml",
  "junit_xml_timestamp": false
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** `dirs` contient les trois suites et `include_subdirs` autorise leurs sous-dossiers.
- **Paramètres et types importants :** `double_strategy` utilise `SCRIPT_ONLY`, la stratégie par défaut qui ne double que les méthodes définies par le projet ; `should_exit` est un booléen nécessaire aux exécutions non interactives.
- **Résultat attendu :** Les fichiers préfixés `test_` et suffixés `.gd` sont découverts, puis un résultat JUnit stable est écrit sous `test-results`.
- **Limites et réserves :** Les options exactes doivent être régénérées avec `-gprint_gutconfig_sample` après toute mise à jour majeure de GUT.

## 9. Vérifier la configuration effective
> **[PS] PowerShell 7 — Afficher les options GUT résolues.**

```powershell
godot --headless --path . -s addons/gut/gut_cmdln.gd `
  -gpo
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** `-gpo` affiche les valeurs effectives après fusion du fichier `.gutconfig.json` et des options de ligne de commande.
- **Paramètres et options importants :** `--headless` sélectionne les pilotes sans fenêtre ; `--path .` fixe la racine du projet ; `-s` exécute le script CLI de GUT.
- **Valeur de retour ou code d’échec :** L’appel doit terminer sans lancer les tests ; un script ou une configuration introuvable produit un code non nul.
- **Résultat attendu :** Le terminal montre les trois dossiers, le préfixe, le suffixe, la stratégie de doubles et le chemin JUnit attendus.

## 10. Première exécution ciblée
> **[PS] PowerShell 7 — Exécuter uniquement les tests unitaires.**

```powershell
godot --headless --path . -s addons/gut/gut_cmdln.gd `
  -gdir=res://test/unit `
  -ginclude_subdirs `
  -gexit `
  -gjunit_xml_file=res://test-results/unit.xml
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et options importants :** `-gdir` remplace la liste de dossiers pour cette exécution ; `-ginclude_subdirs` descend dans les modules ; `-gexit` ferme le runner.
- **Valeur de retour ou code d’échec :** GUT documente un code `0` lorsque tous les tests passent et `1` lorsqu’au moins un test échoue.
- **Effets de bord :** Le fichier `test-results/unit.xml` est remplacé par le résultat JUnit de la campagne.
- **Limites et réserves :** Cette commande reste une procédure à exécuter sur le projet matérialisé ; le présent audit documentaire ne la lance pas.

## 11. Convention de nommage

Les fichiers commencent par `test_`. Les fonctions de test commencent par `test_`. Le nom décrit une règle observable, pas le nom interne de la méthode appelée.

Exemples :

- `test_health_delta_is_bounded_at_zero` ;
- `test_trade_commit_rejects_stale_wallet_revision` ;
- `test_ecology_step_is_reproducible_for_same_seed` ;
- `test_character_scene_emits_spawned_after_registration`.

## 12. Structure Arrange, Act, Assert
> **[VSC] Test unitaire minimal — Ne pas saisir.**

```gdscript
extends GutTest

func test_health_delta_is_bounded_at_zero() -> void:
    # Arrange
    var state := CharacterRuntimeState.new()
    state.current_health = 5
    state.maximum_health = 100

    # Act
    var result := CharacterRules.apply_health_delta(
        state,
        -20
    )

    # Assert
    assert_eq(result, OK)
    assert_eq(state.current_health, 0)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le test vérifie le bornage inférieur de la santé avec une entrée qui dépasserait zéro.
- **Responsabilités des classes ou fonctions :** `CharacterRuntimeState` porte l’état du cas ; `CharacterRules.apply_health_delta()` applique la règle réellement testée.
- **Paramètres et types importants :** Le delta `-20` est un entier et l’état commence à `5` sur un maximum de `100`.
- **Valeur de retour ou code d’échec :** Le test exige `OK`, puis vérifie séparément la postcondition `current_health == 0`.
- **Invariants protégés :** Une mutation valide ne produit jamais une santé négative.

## 13. Comparer exactement ou approximativement

Les identifiants, ticks, unités mineures, révisions, statuts et quantités entières se comparent exactement. Les valeurs issues d’une physique, d’une interpolation ou d’un calcul flottant documenté utilisent une tolérance métier explicite.
> **[VSC] Assertions exactes et approximatives — Ne pas saisir.**

```gdscript
func test_price_quote_uses_exact_minor_units() -> void:
    var quote := MoneyAmount.new(&"currency.crown", 1250)

    assert_eq(quote.currency_id, &"currency.crown")
    assert_eq(quote.minor_units, 1250)

func test_camera_pitch_reaches_expected_angle() -> void:
    var actual_pitch := deg_to_rad(-34.9999)
    var expected_pitch := deg_to_rad(-35.0)

    assert_almost_eq(
        actual_pitch,
        expected_pitch,
        0.00001
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** `StringName` et `int` sont comparés avec `assert_eq`; les angles `float` utilisent `assert_almost_eq`.
- **Opérateurs et conversions non évidents :** `deg_to_rad()` convertit les degrés en radians avant la comparaison.
- **Invariants protégés :** La tolérance `0.00001` appartient au test et rend visible l’écart accepté.
- **Limites et réserves :** Une tolérance large ne doit pas masquer une erreur d’unité ou un calcul instable.

## 14. Tester les refus contrôlés
> **[VSC] Test d’un refus par révision — Ne pas saisir.**

```gdscript
func test_trade_rejects_stale_wallet_revision() -> void:
    var command := TradeCommand.new(
        &"cmd.trade.001",
        &"wallet.buyer",
        &"wallet.seller",
        &"item.instance.7c42a9",
        1250,
        3
    )
    var repository := FakeWalletRepository.new()
    repository.seed_wallet(&"wallet.buyer", 4, 5000)

    var result := TradeService.new(repository).execute(command)

    assert_eq(
        result.status,
        TradeResult.Status.REJECTED
    )
    assert_eq(
        result.reason_id,
        &"economy.reason.stale_wallet_revision"
    )
    assert_eq(repository.replace_count, 0)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le cas prouve qu’une commande préparée sur la révision `3` est refusée lorsque le dépôt expose la révision `4`.
- **Valeur de retour ou code d’échec :** Le statut métier `REJECTED` et le `reason_id` stable sont observés séparément.
- **Effets de bord :** `replace_count == 0` confirme qu’aucune écriture n’a eu lieu après le refus.
- **Invariants protégés :** Une révision périmée ne peut jamais produire un commit partiel.

## 15. Tests paramétrés
> **[VSC] Table de cas pour un ratio borné — Ne pas saisir.**

```gdscript
extends GutTest

var ratio_cases := [
    [0, 0, 0],
    [0, 10, 0],
    [5, 10, 5000],
    [10, 10, 10000],
    [15, 10, 10000],
]

func test_ratio_basis_points(
    values = use_parameters(ratio_cases)
) -> void:
    var actual := DomainMath.ratio_basis_points(
        values[0],
        values[1]
    )

    assert_eq(actual, values[2])
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Chaque entrée contient le numérateur, le dénominateur et le résultat attendu en points de base.
- **Paramètres et types importants :** GUT exige un unique paramètre de test dont la valeur par défaut appelle `use_parameters(array)`.
- **Déroulement ou instructions importantes :** Le runner exécute la fonction une fois par ligne de `ratio_cases`.
- **Invariants protégés :** Les bornes `0` et `10000`, le dénominateur nul et la valeur médiane sont vérifiés sans dupliquer le corps du test.

## 16. Fixtures et builders

Une fixture décrit un état de départ réutilisable. Un builder construit cet état avec des valeurs par défaut lisibles, puis permet au test de modifier uniquement ce qui compte pour son scénario.
> **[VSC] Builder de personnage — Ne pas saisir.**

```gdscript
class_name CharacterStateBuilder
extends RefCounted

var _character_id := &"chr_test"
var _health := 100
var _maximum_health := 100
var _revision := 0

func with_health(
    current: int,
    maximum: int
) -> CharacterStateBuilder:
    _health = current
    _maximum_health = maximum
    return self

func with_revision(value: int) -> CharacterStateBuilder:
    _revision = value
    return self

func build() -> CharacterRuntimeState:
    var state := CharacterRuntimeState.new()
    state.character_id = _character_id
    state.current_health = _health
    state.maximum_health = _maximum_health
    state.revision = _revision
    return state
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le builder centralise un état valide minimal et rend les variations du test explicites.
- **Paramètres et types importants :** `with_health()` reçoit deux entiers et renvoie le builder afin de chaîner les appels.
- **Valeur de retour ou code d’échec :** `build()` retourne une nouvelle instance détachée à chaque appel.
- **Effets de bord :** Les méthodes `with_*` modifient uniquement le builder ; aucun dépôt ou nœud n’est touché.
- **Limites et réserves :** Le builder ne doit pas reproduire les règles de validation du système testé.

## 17. Cycle de vie des fixtures
> **[VSC] Préparation et nettoyage par test — Ne pas saisir.**

```gdscript
extends GutTest

var _repository: FakeCharacterRepository

func before_each() -> void:
    _repository = FakeCharacterRepository.new()

func after_each() -> void:
    _repository.clear()

func test_first_case() -> void:
    _repository.seed(
        CharacterStateBuilder.new().build()
    )
    assert_eq(_repository.count(), 1)

func test_second_case_starts_empty() -> void:
    assert_eq(_repository.count(), 0)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** `before_each()` crée une fixture neuve ; `after_each()` réalise le nettoyage explicite.
- **Déroulement ou instructions importantes :** GUT appelle les deux hooks autour de chaque fonction `test_*`.
- **Invariants protégés :** Le second test ne dépend pas de l’ordre d’exécution ni des mutations du premier.
- **Limites et réserves :** `before_all()` convient uniquement aux objets réellement immuables et coûteux à construire.

## 18. Taxonomie des doubles

- **Fake** : implémentation simplifiée mais fonctionnelle, par exemple un dépôt en mémoire.
- **Stub** : dépendance configurée pour renvoyer une valeur précise.
- **Spy** : double qui enregistre les appels observables.
- **Mock** : double assorti d’attentes sur les interactions.

Le projet privilégie les fakes écrits à la main pour les ports stables. Les doubles générés par GUT restent utiles à la périphérie et pour les interactions ponctuelles.

## 19. Fake d’horloge logique
> **[VSC] Horloge contrôlée — Ne pas saisir.**

```gdscript
class_name FakeLogicalClock
extends LogicalClockPort

var current_tick: int = 0

func now_tick() -> int:
    return current_tick

func advance(ticks: int) -> void:
    assert(ticks >= 0)
    current_tick += ticks
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le fake remplace l’horloge du monde par une valeur entière contrôlée par le test.
- **Paramètres et types importants :** `advance()` reçoit un nombre de ticks non négatif ; `now_tick()` retourne un `int`.
- **Effets de bord :** L’avancement modifie uniquement `current_tick` dans l’instance de test.
- **Invariants protégés :** Aucun test métier ne dépend de l’heure réelle ou de la durée d’exécution sur la machine.

## 20. Fake de générateur pseudo-aléatoire
> **[VSC] Suite de tirages déterminée — Ne pas saisir.**

```gdscript
class_name SequenceRandom
extends RandomPort

var _values: Array[int] = []
var _index: int = 0

func _init(values: Array[int]) -> void:
    _values = values.duplicate()

func next_int(
    minimum: int,
    maximum: int
) -> int:
    assert(not _values.is_empty())
    var raw := _values[_index % _values.size()]
    _index += 1
    return clampi(raw, minimum, maximum)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le fake fournit une suite connue au lieu d’utiliser l’état global de `RandomNumberGenerator`.
- **Paramètres et types importants :** Le constructeur copie le tableau ; `next_int()` reçoit les bornes inclusives.
- **Déroulement ou instructions importantes :** L’opérateur `%` boucle dans la suite et `clampi()` respecte le contrat de plage.
- **Invariants protégés :** Deux exécutions avec le même tableau observent les mêmes décisions aléatoires.

## 21. Fake de dépôt versionné
> **[VSC] Dépôt en mémoire avec révision — Ne pas saisir.**

```gdscript
class_name FakeCharacterRepository
extends CharacterRepositoryPort

var _states: Dictionary[StringName, CharacterRuntimeState] = {}
var replace_count: int = 0

func seed(state: CharacterRuntimeState) -> void:
    _states[state.character_id] = state.duplicate_detached()

func read(character_id: StringName) -> CharacterRuntimeState:
    var state := _states.get(character_id)
    return null if state == null else state.duplicate_detached()

func replace(
    expected_revision: int,
    candidate: CharacterRuntimeState
) -> Error:
    var active := _states.get(candidate.character_id)
    if active == null:
        return ERR_DOES_NOT_EXIST
    if active.revision != expected_revision:
        return ERR_BUSY

    _states[candidate.character_id] = candidate.duplicate_detached()
    replace_count += 1
    return OK

func count() -> int:
    return _states.size()

func clear() -> void:
    _states.clear()
    replace_count = 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** `seed`, `read` et `replace` reproduisent le contrat public du dépôt sans accès disque.
- **Paramètres et types importants :** Le dictionnaire est indexé par `StringName`; les lectures et écritures utilisent des copies détachées.
- **Codes de retour :** `ERR_DOES_NOT_EXIST` distingue l’absence et `ERR_BUSY` une révision devenue obsolète.
- **Effets de bord :** Seul un remplacement accepté incrémente `replace_count`.
- **Invariants protégés :** Le fake conserve l’isolation des copies et l’optimistic concurrency du dépôt réel.

## 22. Fake d’un port IA local
> **[VSC] Port consultatif en mémoire — Ne pas saisir.**

```gdscript
class_name FakeLocalAiGateway
extends LocalAiGateway

var responses: Dictionary[StringName, LocalAiResponse] = {}
var requested_ids: Array[StringName] = []

func request(
    request_value: LocalAiRequest
) -> LocalAiResponse:
    requested_ids.append(request_value.request_id)
    return responses.get(
        request_value.request_id,
        LocalAiResponse.unavailable(
            request_value.request_id,
            &"test.no_response"
        )
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** Le fake remplace le transport et ne modifie aucun état autoritaire du gameplay.
- **Paramètres et types importants :** Les réponses sont indexées par `request_id`; les demandes reçues sont enregistrées dans l’ordre.
- **Valeur de retour ou code d’échec :** Une demande non configurée renvoie une indisponibilité typée au lieu de `null`.
- **Résultat attendu :** Les tests peuvent vérifier le repli déterministe sans lancer Python, HTTP, WebSocket ou modèle local.

## 23. Utiliser un double GUT avec prudence
> **[VSC] Double script-only — Ne pas saisir.**

```gdscript
extends GutTest

const PORT_SCRIPT := preload(
    "res://src/features/economy/application/tax_policy_port.gd"
)

func test_quote_uses_configured_tax_rate() -> void:
    var policy := double(PORT_SCRIPT).new()
    stub(policy, "rate_basis_points").to_return(750)

    var quote := PriceCalculator.new(policy).quote(10000)

    assert_eq(quote.tax_minor, 750)
    assert_eq(quote.total_minor, 10750)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** `double()` crée une classe de test depuis le script utilisateur ; `stub()` configure la méthode observée.
- **Paramètres et types importants :** Le taux `750` représente 7,5 % en points de base et le montant de base vaut `10000` unités mineures.
- **Valeur de retour ou code d’échec :** Les deux assertions contrôlent la taxe puis le total, pas l’implémentation interne du calculateur.
- **Limites et réserves :** Les méthodes natives Godot ne sont pas incluses par défaut et les paramètres par défaut des méthodes doublées exigent une attention particulière.

## 24. Espionner une interaction
> **[VSC] Vérifier un appel de port — Ne pas saisir.**

```gdscript
extends GutTest

func test_successful_completion_emits_one_commit() -> void:
    var commit_port := double(
        preload(
            "res://src/features/narration/application/"
            + "quest_commit_port.gd"
        )
    ).new()
    stub(commit_port, "commit_completion").to_return(OK)

    var service := QuestCompletionService.new(commit_port)
    var result := service.complete(
        QuestCompletionCommandBuilder.new().build()
    )

    assert_eq(result.status, QuestResult.Status.COMMITTED)
    assert_called_count(
        commit_port.commit_completion,
        1
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le test vérifie qu’une résolution acceptée produit exactement une tentative de commit.
- **Responsabilités des classes ou fonctions :** Le stub fixe le résultat du port ; le spy de GUT enregistre l’appel sur le double.
- **Valeur de retour ou code d’échec :** Le statut métier et `assert_called_count(commit_port.commit_completion, 1)` sont deux observations complémentaires.
- **Limites et réserves :** Le test ne doit pas spécifier chaque appel interne lorsque seul le commit unique appartient au contrat.

## 25. Tester les scènes dans un `SceneTree`

Les nœuds reçoivent leurs callbacks seulement après leur entrée dans l’arbre. Un test de scène doit donc instancier une `PackedScene`, l’ajouter avec un mécanisme de nettoyage automatique, puis attendre les frames nécessaires à l’observation.
> **[VSC] Instancier une scène sous test — Ne pas saisir.**

```gdscript
extends GutTest

const CHARACTER_SCENE := preload(
    "res://src/features/characters/presentation/"
    + "character_actor.tscn"
)

func test_character_actor_registers_after_ready() -> void:
    var actor := CHARACTER_SCENE.instantiate()
    add_child_autofree(actor)

    await wait_idle_frames(1)

    assert_true(actor.is_node_ready())
    assert_true(actor.has_runtime_binding())
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** `instantiate()` crée l’arbre local ; `add_child_autofree()` l’ajoute au runner et planifie son nettoyage.
- **Déroulement ou instructions importantes :** `wait_idle_frames(1)` laisse passer l’entrée dans l’arbre et les callbacks `_ready()`.
- **Valeur de retour ou code d’échec :** Les assertions observent l’état prêt et la liaison runtime publiée par la scène.
- **Limites et réserves :** Le nombre de frames doit provenir du contrat de la scène, pas d’une attente arbitraire destinée à masquer une course.

## 26. Tester un signal avec délai borné
> **[VSC] Attendre un signal sans bloquer indéfiniment — Ne pas saisir.**

```gdscript
extends GutTest

func test_actor_emits_despawned_after_request() -> void:
    var actor := CharacterActorFixture.create()
    add_child_autofree(actor)

    actor.request_despawn(&"test.cleanup")

    var emitted := await wait_for_signal(
        actor.despawned,
        0.5,
        "attente du signal despawned"
    )

    assert_true(emitted)
    assert_signal_emitted(actor, "despawned")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** `wait_for_signal()` reçoit le signal, un délai maximal en secondes et un message de diagnostic.
- **Valeur de retour ou code d’échec :** Le booléen `emitted` distingue l’émission du dépassement de délai.
- **Effets de bord :** La demande de disparition peut déclencher une libération différée ; le runner nettoie l’acteur à la fin du cas.
- **Invariants protégés :** Un signal absent échoue de manière bornée au lieu de suspendre toute la campagne.

## 27. Simuler des callbacks sans attendre le temps réel
> **[VSC] Appeler les callbacks sur plusieurs pas — Ne pas saisir.**

```gdscript
extends GutTest

func test_cooldown_reaches_zero_after_three_steps() -> void:
    var node := CooldownPresenter.new()
    node.remaining_seconds = 0.3

    simulate(
        node,
        3,
        0.1,
        true
    )

    assert_almost_eq(
        node.remaining_seconds,
        0.0,
        0.00001
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** `simulate()` appelle les callbacks de traitement sur l’objet sans attendre trois dixièmes de seconde réelles.
- **Paramètres et types importants :** Les arguments représentent l’objet, trois itérations, un delta de `0.1` et le respect de l’état `is_processing`.
- **Déroulement ou instructions importantes :** GUT appelle les méthodes de traitement visibles sur l’objet et ses descendants selon l’ordre documenté.
- **Limites et réserves :** Cette aide ne remplace pas une intégration réelle au `SceneTree` lorsque les signaux de frame, serveurs ou notifications moteur font partie du contrat.

## 28. Tester un codec et sa restauration
> **[VSC] Aller-retour d’un état versionné — Ne pas saisir.**

```gdscript
func test_character_snapshot_round_trip() -> void:
    var original := (
        CharacterStateBuilder.new()
        .with_health(42, 100)
        .with_revision(7)
        .build()
    )

    var encoded := CharacterSaveCodec.new().encode(original)
    var prepared := CharacterSaveCodec.new().prepare_restore(
        encoded
    )

    assert_true(prepared.is_valid())
    assert_eq(
        prepared.state.character_id,
        original.character_id
    )
    assert_eq(prepared.state.current_health, 42)
    assert_eq(prepared.state.revision, 7)
    assert_ne(prepared.state, original)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le test vérifie qu’un snapshot valide conserve les champs durables sans réutiliser l’instance active.
- **Déroulement ou instructions importantes :** L’état est construit, encodé, préparé pour restauration, puis comparé au modèle source.
- **Invariants protégés :** `assert_ne(prepared.state, original)` impose une copie détachée.
- **Limites et réserves :** Un aller-retour ne suffit pas ; les versions futures, données invalides et migrations exigent des cas séparés.


## 29. Produire des chemins temporaires uniques

> **[VSC] Aide `test/support/test_run_id.gd` — Ne pas saisir.**

```gdscript
class_name TestRunId
extends RefCounted

static var _counter: int = 0

static func next_string() -> String:
    _counter += 1
    return "%d-%06d" % [
        OS.get_process_id(),
        _counter,
    ]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** `TestRunId` fabrique un suffixe unique dans le processus de test sans lire l’heure système.
- **Paramètres et types importants :** `_counter` est un entier statique partagé par la campagne ; `OS.get_process_id()` distingue deux processus concurrents.
- **Valeur de retour ou code d’échec :** `next_string()` retourne une chaîne composée du processus et d’un compteur sur six chiffres.
- **Effets de bord :** Chaque appel incrémente uniquement le compteur du support de test.
- **Limites et réserves :** L’identifiant sert aux chemins temporaires ; il ne doit pas entrer dans un résultat canonique ou un scénario déterministe.

## 30. Intégrer SQLite dans une base temporaire
> **[VSC] Fixture de base isolée — Ne pas saisir.**

```gdscript
extends GutTest

var _database_path: String
var _connection: DatabaseConnection

func before_each() -> void:
    _database_path = "user://tests/%s.sqlite" %         TestRunId.next_string()
    _connection = SqliteConnection.new()
    assert_eq(_connection.open(_database_path), OK)
    assert_eq(TestMigrationSet.apply(_connection), OK)

func after_each() -> void:
    _connection.close()
    DirAccess.remove_absolute(
        ProjectSettings.globalize_path(_database_path)
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** Chaque test ouvre une base unique, applique les migrations approuvées, puis ferme et supprime le fichier.
- **Paramètres et types importants :** Le chemin `user://tests/<run-id>.sqlite` évite le partage entre cas ; `globalize_path()` produit le chemin absolu requis par la suppression.
- **Effets de bord :** Le test crée puis supprime un fichier sous le répertoire utilisateur de l’application.
- **Invariants protégés :** Aucune campagne ne modifie la base de développement ou une sauvegarde réelle.
- **Limites et réserves :** La création du dossier `user://tests` et le comportement exact du wrapper SQLite devront être vérifiés dans le Starter Kit.

## 31. Vérifier une transaction multi-autorités
> **[VSC] Intégration économie-inventaire — Ne pas saisir.**

```gdscript
func test_trade_commit_is_atomic() -> void:
    var fixture := TradeIntegrationFixture.new(
        _connection
    )
    fixture.seed_buyer_balance(5000)
    fixture.seed_item_owner(&"character.seller")

    fixture.commit_port.fail_after_wallet_prepare = true

    var result := fixture.trade_service.execute(
        fixture.valid_trade_command(1250)
    )

    assert_eq(result.status, TradeResult.Status.REJECTED)
    assert_eq(fixture.read_buyer_balance(), 5000)
    assert_eq(
        fixture.read_item_owner(),
        &"character.seller"
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le scénario injecte une panne entre préparation et commit pour vérifier l’absence de mutation partielle.
- **Effets de bord :** Les lectures finales interrogent les dépôts réels de la fixture d’intégration.
- **Invariants protégés :** Le solde et la propriété restent tous deux inchangés lorsque le lot est refusé.
- **Limites et réserves :** Le point de panne est une capacité de la fixture de test et ne doit pas être exposé dans l’API runtime.

## 32. Tester les fichiers de sauvegarde

Un test de sauvegarde écrit dans un dossier de test unique, vérifie le temporaire, le fichier final et la copie de secours, puis nettoie ses artefacts. Il ne réutilise jamais les slots du joueur.
> **[VSC] Sauvegarde et restauration isolées — Ne pas saisir.**

```gdscript
func test_save_then_load_preserves_snapshot() -> void:
    var root := "user://tests/saves/%s" % TestRunId.next_string()
    var store := FileSaveStore.new(root)
    var snapshot := WorldSnapshotFixture.small_world()

    var save_result := store.save(&"slot.test", snapshot)
    var load_result := store.load(&"slot.test")

    assert_eq(save_result.status, SaveResult.Status.COMMITTED)
    assert_eq(load_result.status, LoadResult.Status.LOADED)
    assert_eq(
        load_result.snapshot.canonical_digest(),
        snapshot.canonical_digest()
    )

    TestFiles.remove_tree(root)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** Le dossier unique et le slot `slot.test` séparent le cas des données utilisateur.
- **Déroulement ou instructions importantes :** Le test sauvegarde, recharge, compare les empreintes canoniques puis supprime le dossier.
- **Valeur de retour ou code d’échec :** Les statuts `COMMITTED` et `LOADED` sont vérifiés avant l’accès au snapshot.
- **Invariants protégés :** Le contenu durable restauré possède la même représentation canonique que l’état source.

## 33. Tester le pipeline de contenu
> **[VSC] Publication dans une racine temporaire — Ne pas saisir.**

```gdscript
func test_pipeline_promotes_only_validated_content() -> void:
    var workspace := ContentTestWorkspace.new()
    workspace.write_source(
        "quests/tutorial.json",
        QuestFixture.valid_source()
    )

    var pipeline := ContentPipeline.new(
        workspace.ports()
    )
    var preview := pipeline.prepare(
        PublishContentCommandBuilder.new().build()
    )
    var result := pipeline.publish(preview.receipt_id)

    assert_true(preview.is_publishable())
    assert_eq(result.status, PublishResult.Status.PROMOTED)
    assert_true(
        workspace.artifact_exists(
            "quests/tutorial.tres"
        )
    )
    workspace.cleanup()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** Le workspace redirige sources, staging et artefacts vers une racine temporaire ; aucun fichier canonique du projet n’est touché.
- **Déroulement ou instructions importantes :** La publication utilise le `receipt_id` produit par l’aperçu, comme le contrat du chapitre 26.
- **Valeur de retour ou code d’échec :** Le test exige un aperçu publiable puis un statut `PROMOTED`.
- **Invariants protégés :** L’artefact n’existe qu’après une préparation validée et une promotion acceptée.

## 34. Contrats d’adaptateurs externes

Les adaptateurs HTTP, WebSocket, processus compagnon ou OpenAI-compatible ne sont pas appelés dans la suite unitaire. Une suite de contrat leur fournit des enveloppes enregistrées, vérifie parsing, limites, statuts et corrélation, puis réserve les tests réseau réels à une campagne explicitement isolée.
> **[VSC] Cas de contrat HTTP enregistré — Ne pas saisir.**

```gdscript
func test_http_adapter_maps_429_to_overloaded() -> void:
    var transport := RecordedHttpTransport.new()
    transport.enqueue_response(
        429,
        {"Retry-After": "2"},
        "{\"error\":{\"code\":\"queue_full\"}}"
    )

    var result := OpenAiCompatibleAdapter.new(
        transport
    ).submit(LocalAiRequestBuilder.new().build())

    assert_eq(
        result.status,
        LocalAiResponse.Status.OVERLOADED
    )
    assert_eq(result.retry_after_ms, 2000)
    assert_eq(result.error_id, &"queue_full")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le test exerce le mapping de l’adaptateur avec une réponse enregistrée, sans ouvrir de socket.
- **Paramètres et types importants :** Le code HTTP `429`, l’en-tête `Retry-After` en secondes et le JSON d’erreur sont des entrées distinctes.
- **Valeur de retour ou code d’échec :** Le résultat expose un statut métier, un délai en millisecondes et un identifiant stable.
- **Invariants protégés :** La surcharge n’est ni transformée en succès ni confondue avec une panne de parsing.

## 35. Modèle d’une simulation déterministe
> **[LECTURE] Flux d’une simulation — Ne pas saisir.**

```text
ScenarioDefinition
  initial_snapshot
  commands_by_tick
  seeds_by_system
  maximum_ticks
        ↓
SimulationHarness.run()
        ↓
tick final
snapshot canonique
événements canoniques
compteurs d’invariants
digest de campagne
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Le scénario porte toutes les entrées nécessaires : état, commandes, graines et borne.
- **Déroulement ou instructions importantes :** Le harness exécute les ticks jusqu’à la borne ou une condition terminale, puis produit des sorties canoniques.
- **Invariants protégés :** Aucune entrée ne provient du temps réel, de l’ordre d’un dictionnaire non normalisé ou d’un RNG global.
- **Résultat attendu :** Une campagne peut comparer le digest et les compteurs sans sérialiser des objets de scène.

## 36. Définir un scénario
> **[VSC] Définition d’un scénario de simulation — Ne pas saisir.**

```gdscript
class_name SimulationScenario
extends Resource

@export var scenario_id: StringName
@export var schema_version: int = 1
@export var maximum_ticks: int = 1000
@export var initial_snapshot: Dictionary = {}
@export var commands_by_tick: Dictionary = {}
@export var seeds_by_system: Dictionary = {}

func validate() -> SimulationScenarioReport:
    var report := SimulationScenarioReport.new()
    if scenario_id == &"":
        report.add_error(&"empty_scenario_id")
    if maximum_ticks <= 0:
        report.add_error(&"invalid_maximum_ticks")
    if initial_snapshot.is_empty():
        report.add_error(&"empty_initial_snapshot")
    return report
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La `Resource` versionnée décrit les entrées persistantes d’une campagne.
- **Paramètres et types importants :** Les commandes sont indexées par tick entier et les graines par identifiant de système.
- **Valeur de retour ou code d’échec :** `validate()` retourne un rapport structuré plutôt qu’un booléen sans diagnostic.
- **Invariants protégés :** L’identité, la borne de ticks et l’état initial sont obligatoires avant exécution.
- **Limites et réserves :** Le dictionnaire initial doit passer ensuite par les codecs et validations propriétaires de chaque système.

## 37. Orchestrer les ticks
> **[VSC] Harness borné — Ne pas saisir.**

```gdscript
class_name SimulationHarness
extends RefCounted

var _world: SimulatedWorld
var _events: CanonicalEventRecorder

func run(
    scenario: SimulationScenario
) -> SimulationRunResult:
    var report := scenario.validate()
    if report.has_errors():
        return SimulationRunResult.invalid(report)

    _world = SimulatedWorld.restore(
        scenario.initial_snapshot,
        scenario.seeds_by_system
    )
    _events = CanonicalEventRecorder.new()

    for tick in range(
        1,
        scenario.maximum_ticks + 1
    ):
        _apply_commands(
            tick,
            scenario.commands_by_tick.get(tick, [])
        )
        _world.step(tick, _events)
        if _world.is_terminal():
            return _build_result(tick)

    return _build_result(scenario.maximum_ticks)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** `restore()` construit le monde contrôlé ; `_apply_commands()` injecte les entrées ; `step()` fait progresser les systèmes.
- **Déroulement ou instructions importantes :** La boucle commence au tick `1`, inclut `maximum_ticks` et peut se terminer plus tôt sur un état terminal.
- **Valeur de retour ou code d’échec :** Un scénario invalide produit `SimulationRunResult.invalid`; une exécution valide produit un résultat final borné.
- **Invariants protégés :** Le harness ne saute aucun tick, n’en ajoute aucun et n’attend aucune durée murale.

## 38. Enregistrer des événements canoniques
> **[VSC] Projection stable des événements — Ne pas saisir.**

```gdscript
class_name CanonicalEventRecorder
extends RefCounted

var records: Array[Dictionary] = []

func record(event_value: DomainEvent) -> void:
    records.append({
        "event_id": String(event_value.event_id),
        "event_type": String(event_value.event_type),
        "logical_tick": event_value.logical_tick,
        "source_id": String(event_value.source_id),
        "payload": CanonicalValue.normalize(
            event_value.to_payload()
        ),
    })

func digest() -> String:
    return CanonicalHash.sha256(records)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le recorder transforme les événements en valeurs sérialisables et ordonnées pour la comparaison.
- **Paramètres et types importants :** Les `StringName` sont convertis en `String`; le payload passe par la normalisation canonique.
- **Effets de bord :** `record()` ajoute une entrée au tableau dans l’ordre d’observation.
- **Valeur de retour ou code d’échec :** `digest()` retourne l’empreinte SHA-256 de la séquence complète.
- **Limites et réserves :** Les champs volatils, références de nœuds et messages localisés doivent être exclus de `to_payload()`.

## 39. Résultat d’une campagne
> **[LECTURE] Résultat versionné — Ne pas saisir.**

```json
{
  "schema_version": 1,
  "scenario_id": "sim.ecology.small_valley",
  "engine_contract": "asteria-sim-1",
  "final_tick": 720,
  "snapshot_digest": "sha256:...",
  "event_digest": "sha256:...",
  "invariants": {
    "negative_population_count": 0,
    "unbalanced_ledger_count": 0,
    "stale_commit_count": 0
  }
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Le résultat distingue version, identité, contrat de simulation, tick final, deux empreintes et compteurs.
- **Invariants protégés :** Les compteurs rendent visibles les violations même lorsque le digest final serait mis à jour.
- **Résultat attendu :** Une revue peut décider si un changement de digest est légitime sans perdre les métriques de sécurité.
- **Limites et réserves :** Une empreinte seule n’explique pas la différence ; les rapports détaillés restent nécessaires en cas d’échec.

## 40. Vérifier la reproductibilité
> **[VSC] Rejouer deux fois le même scénario — Ne pas saisir.**

```gdscript
func test_same_scenario_produces_same_digests() -> void:
    var scenario := preload(
        "res://test/simulation/scenarios/"
        + "small_valley.tres"
    )

    var first := SimulationHarness.new().run(scenario)
    var second := SimulationHarness.new().run(scenario)

    assert_eq(first.final_tick, second.final_tick)
    assert_eq(
        first.snapshot_digest,
        second.snapshot_digest
    )
    assert_eq(
        first.event_digest,
        second.event_digest
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le test détecte une dépendance cachée à l’ordre, au temps ou à un état global.
- **Déroulement ou instructions importantes :** Deux harness neufs exécutent la même `Resource` de scénario.
- **Invariants protégés :** Le tick final, l’état canonique et la séquence événementielle doivent être identiques.
- **Limites et réserves :** La comparaison sur une même machine ne remplace pas une campagne multiplateforme ultérieure.

## 41. Tester des propriétés et invariants
> **[VSC] Campagne de graines bornée — Ne pas saisir.**

```gdscript
func test_population_never_becomes_negative() -> void:
    for seed in range(0, 128):
        var scenario := (
            EcologyScenarioFactory.new()
            .with_seed(seed)
            .with_maximum_ticks(365)
            .build()
        )

        var result := SimulationHarness.new().run(
            scenario
        )

        assert_eq(
            result.invariants[
                "negative_population_count"
            ],
            0,
            "seed=%d" % seed
        )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** La campagne parcourt exactement 128 graines et borne chaque scénario à 365 ticks.
- **Déroulement ou instructions importantes :** Le message `seed=<n>` rend le cas reproductible lorsqu’une assertion échoue.
- **Invariants protégés :** Aucune population logique ne passe sous zéro quelle que soit la suite pseudo-aléatoire du corpus.
- **Limites et réserves :** Cette boucle est une exploration bornée, pas une preuve mathématique de toutes les graines possibles.

## 42. Conserver le premier cas défaillant
> **[VSC] Rapport de graine reproductible — Ne pas saisir.**

```gdscript
class_name SeedFailure
extends RefCounted

var scenario_id: StringName
var seed: int
var failed_invariant: StringName
var final_tick: int
var snapshot_digest: String

func to_dictionary() -> Dictionary:
    return {
        "scenario_id": String(scenario_id),
        "seed": seed,
        "failed_invariant": String(failed_invariant),
        "final_tick": final_tick,
        "snapshot_digest": snapshot_digest,
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** L’objet capture les données minimales nécessaires au replay d’une graine défaillante.
- **Paramètres et types importants :** L’identité du scénario et de l’invariant utilisent `StringName`; la sérialisation les convertit en chaînes.
- **Résultat attendu :** Le rapport peut être écrit comme artefact de campagne et transformé en fixture permanente.
- **Limites et réserves :** Le snapshot complet n’est pas dupliqué ici ; son digest doit pointer vers un artefact ou un scénario reconstructible.

## 43. Résultats approuvés et golden files

Un golden file contient une sortie canonique relue. Il est pertinent pour un manifeste, un snapshot réduit ou un rapport stable. Il est dangereux lorsqu’il capture des milliers de lignes volatiles que personne ne relit.
> **[VSC] Comparaison d’un résultat approuvé — Ne pas saisir.**

```gdscript
func test_small_valley_matches_approved_result() -> void:
    var scenario := SimulationScenarioLoader.load_checked(
        "res://test/simulation/scenarios/"
        + "small_valley.tres"
    )
    var expected := CanonicalJson.read_checked(
        "res://test/simulation/expected/"
        + "small_valley.v1.json"
    )

    var actual := SimulationHarness.new().run(
        scenario
    ).to_dictionary()

    assert_eq(
        CanonicalValue.normalize(actual),
        CanonicalValue.normalize(expected)
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le test compare deux documents canoniques après chargement validé.
- **Dépendances et ports utilisés :** `SimulationScenarioLoader` et `CanonicalJson` centralisent les diagnostics de lecture.
- **Invariants protégés :** L’ordre des clés ou une représentation JSON non canonique ne crée pas de faux échec.
- **Limites et réserves :** Toute mise à jour du fichier attendu exige une revue de la différence et une justification dans le commit.

## 44. Budgets de performance

Un test de performance mesure une enveloppe sur une machine et un profil connus. Il ne doit pas utiliser un seuil trop serré dans la suite de correction rapide. Le résultat principal reste un rapport de tendance ; les seuils bloquants sont réservés aux régressions importantes et reproductibles.
> **[VSC] Mesure bornée d’une campagne — Ne pas saisir.**

```gdscript
func test_small_world_stays_within_operation_budget() -> void:
    var scenario := PerformanceScenarioFactory.small_world()
    var result := InstrumentedSimulationHarness.new().run(
        scenario
    )

    assert_lte(result.expanded_plan_nodes, 20000)
    assert_lte(result.database_queries, 400)
    assert_lte(result.maximum_pending_events, 512)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le cas mesure des compteurs d’opérations déterministes plutôt qu’une durée CPU très sensible à la machine.
- **Paramètres et types importants :** Les trois seuils portent sur des nœuds de planification, requêtes et événements en attente.
- **Invariants protégés :** Une optimisation ne peut pas augmenter sans borne la recherche, les accès persistants ou la file.
- **Limites et réserves :** Le temps mur, la mémoire et le rendu exigent des benchmarks séparés sur la configuration de référence.

## 45. Catégoriser les suites
> **[LECTURE] Matrice de suites — Ne pas saisir.**

```text
Suite          Dépendances réelles              Fréquence
unit           règles + fakes                   chaque modification
integration    SceneTree, fichiers, SQLite       pull request
simulation     plusieurs systèmes, graines      pull request ciblée
regression     scénarios approuvés               avant fusion majeure
platform       export, GPU, pilotes, réseau      campagne dédiée
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des données :** Chaque ligne associe une surface technique à une fréquence minimale.
- **Frontières d’autorité :** La suite `platform` ne doit pas être présentée comme un test unitaire plus lent.
- **Résultat attendu :** Les développeurs savent quelles suites lancer localement et quelles campagnes déléguer à l’intégration continue.
- **Limites et réserves :** Le chapitre ne matérialise pas encore les workflows runtime du Starter Kit.

## 46. Commandes par suite
> **[PS] PowerShell 7 — Exécuter les tests d’intégration.**

```powershell
godot --headless --path . -s addons/gut/gut_cmdln.gd `
  -gdir=res://test/integration `
  -ginclude_subdirs `
  -gexit `
  -gjunit_xml_file=res://test-results/integration.xml
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et options importants :** Le dossier et le fichier JUnit sont propres à la suite d’intégration.
- **Valeur de retour ou code d’échec :** Un code non nul bloque la campagne appelante.
- **Effets de bord :** Les fixtures peuvent écrire sous leurs racines temporaires ; elles doivent les supprimer avant la fin du run.
- **Résultat attendu :** Le terminal et `integration.xml` distinguent les tests réussis, échoués et risqués.

> **[PS] PowerShell 7 — Exécuter les simulations.**

```powershell
godot --headless --path . -s addons/gut/gut_cmdln.gd `
  -gdir=res://test/simulation `
  -ginclude_subdirs `
  -gexit `
  -gjunit_xml_file=res://test-results/simulation.xml
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et options importants :** Le runner limite sa découverte à `res://test/simulation`.
- **Déroulement ou instructions importantes :** Les scénarios, graines et résultats approuvés restent chargés par les tests ; la commande ne les génère pas silencieusement.
- **Résultat attendu :** Le fichier JUnit permet à une CI d’afficher le scénario ou la graine ayant échoué.
- **Limites et réserves :** Les campagnes très longues devront être réparties au chapitre 29 sans modifier leur sémantique.

## 47. Wrapper PowerShell et codes de sortie
> **[VSC] Script `tools/test/run-gut.ps1` — Ne pas saisir dans Godot.**

```powershell
param(
  [ValidateSet("unit", "integration", "simulation")]
  [string]$Suite = "unit"
)

$ErrorActionPreference = "Stop"
$resultPath = "res://test-results/$Suite.xml"
$testDir = "res://test/$Suite"

& godot --headless --path . `
  -s addons/gut/gut_cmdln.gd `
  "-gdir=$testDir" `
  -ginclude_subdirs `
  -gexit `
  "-gjunit_xml_file=$resultPath"

$exitCode = $LASTEXITCODE
if ($exitCode -ne 0) {
  throw "Suite $Suite échouée avec le code $exitCode."
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** `ValidateSet` ferme les valeurs autorisées de `$Suite`; la valeur par défaut est `unit`.
- **Déroulement ou instructions importantes :** Le script dérive le dossier et le rapport, appelle Godot, puis lit immédiatement `$LASTEXITCODE`.
- **Valeur de retour ou code d’échec :** Tout code différent de zéro devient une exception PowerShell et échoue la tâche appelante.
- **Invariants protégés :** Le wrapper ne relance pas automatiquement une suite en échec et ne remplace pas son diagnostic.

## 48. Artefacts de campagne
> **[LECTURE] Artefacts à conserver — Ne pas saisir.**

```text
test-results/
├── unit.xml
├── integration.xml
├── simulation.xml
├── first-failing-seed.json
├── canonical-diff.json
└── campaign-summary.json
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des fichiers :** Les rapports JUnit, la première graine défaillante, la différence canonique et le résumé ont des responsabilités distinctes.
- **Résultat attendu :** Une personne peut reproduire l’échec sans relire tout le journal de console.
- **Sécurité et confidentialité :** Les artefacts ne contiennent ni secret, ni jeton, ni donnée de joueur réelle.
- **Limites et réserves :** La politique de rétention et les journaux structurés complets seront définis au chapitre 28.

## 49. Critères de passage

Une modification peut passer lorsque :

- les tests unitaires concernés sont verts ;
- les intégrations touchées sont vertes ;
- les scénarios déterministes gardent leurs invariants ;
- tout changement de résultat approuvé est expliqué et relu ;
- aucun test risqué, ignoré ou flaky n’est masqué ;
- les rapports sont produits avec un code de sortie cohérent ;
- les dépendances et fixtures sont isolées ;
- les réserves de plateforme sont déclarées.

## 50. Mode Solo

Le parcours Solo conserve une installation GUT épinglée, une configuration unique, les trois dossiers de suites et un wrapper PowerShell. La priorité est donnée aux règles pures, aux fakes écrits à la main, aux intégrations critiques de sauvegarde et à quelques simulations courtes.

Les campagnes longues restent manuelles mais versionnées. Une graine défaillante devient immédiatement un cas permanent lorsqu’elle révèle une régression réelle.

## 51. Mode Studio

Le parcours Studio ajoute des propriétaires de suites, une matrice par système, des revues de golden files, des campagnes par plateforme, des rapports JUnit centralisés, des quarantaines temporaires avec échéance, des budgets d’opérations et une politique de promotion des graines défaillantes.

La séparation des suites permet d’exécuter rapidement les unités à chaque changement, les intégrations sur chaque pull request et les campagnes longues selon le risque ou un calendrier défini.

## 52. Contrat commun Solo et Studio

Les deux parcours exigent des tests déterministes, des dépendances contrôlées, des fichiers temporaires isolés, des résultats actionnables, des codes de sortie non masqués et l’absence de données utilisateur réelles.

## 53. Frontières avec les chapitres précédents

- personnages : règles, état détaché, apparition et registre actif ;
- relations et famille : invariants orientés, cycles et vues dérivées ;
- agents : planification bornée, invalidation et graines ;
- combat et compétences : commandes, coûts, initiative, effets et commits ;
- inventaire et économie : transferts, écritures équilibrées et idempotence ;
- écologie : pas agrégés, résidus, populations et récoltes ;
- politique et domaines : autorisations, sanctions et transactions externes ;
- narration : faits, conditions, conséquences et connaissance relative ;
- outils de contenu : validation, reçus, staging et promotion.

Le chapitre ne change aucune de ces autorités. Il fournit les moyens de les vérifier.

## 54. Observations à ne pas confondre

- une assertion échouée décrit une différence observée ;
- un refus métier valide peut constituer le résultat attendu d’un test ;
- une exception du framework indique un problème de test ou d’environnement ;
- un code de sortie non nul bloque la campagne ;
- une différence de digest demande un diagnostic, pas une mise à jour automatique ;
- un test lent n’est pas nécessairement un test d’intégration ;
- un test avec un fake peut rester un test unitaire.

## 55. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

Les dix cas suivants enseignent des défauts qui rendent une suite trompeuse, instable ou incapable de localiser une régression.
### 55.1 Tester une méthode privée au lieu d’un contrat

**Symptôme :** Le test casse après un simple refactoring alors que le comportement public reste identique.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
var service := TradeService.new(repository)
assert_eq(service._compute_tax(1000), 75)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** `_compute_tax()` est un détail privé ; le test verrouille l’organisation interne et n’observe ni le devis ni le résultat public.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var quote := service.quote(
    TradeQuoteCommand.fixture(1000)
)
assert_eq(quote.tax_minor, 75)
assert_eq(quote.total_minor, 1075)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le test vérifie les valeurs publiques du devis ; la méthode interne peut être renommée ou remplacée sans modifier le contrat.

### 55.2 Utiliser l’heure réelle dans un test

**Symptôme :** Le même cas réussit ou échoue selon la vitesse de la machine et l’instant d’exécution.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
var started := Time.get_unix_time_from_system()
await get_tree().create_timer(0.2).timeout
assert_true(
    Time.get_unix_time_from_system() > started
)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le temps horloge et un délai réel introduisent une dépendance externe sans rapport avec la règle métier.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var clock := FakeLogicalClock.new()
clock.current_tick = 10
clock.advance(2)
assert_eq(clock.now_tick(), 12)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le test contrôle exactement l’état initial et l’avancement de l’horloge logique, sans attendre de durée murale.

### 55.3 Utiliser le RNG global

**Symptôme :** Une nouvelle utilisation aléatoire dans un autre test change le résultat du cas.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
var selected := variants.pick_random()
assert_eq(selected, &"variant.a")
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** `pick_random()` consomme l’état pseudo-aléatoire global, partagé et non restauré par la fixture.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var random := SequenceRandom.new([0])
var selected := VariantPolicy.choose(
    variants,
    random
)
assert_eq(selected, &"variant.a")
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le port aléatoire reçoit une suite locale connue ; l’ordre des autres tests ne peut pas modifier le choix.

### 55.4 Partager une fixture mutable

**Symptôme :** Un test passe seul mais échoue lorsqu’il est exécuté après un autre.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
var shared_state := CharacterStateBuilder.new().build()

func test_damage() -> void:
    shared_state.current_health -= 10

func test_full_health() -> void:
    assert_eq(shared_state.current_health, 100)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les deux tests utilisent la même instance et le premier modifie l’état observé par le second.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var state: CharacterRuntimeState

func before_each() -> void:
    state = CharacterStateBuilder.new().build()

func test_full_health() -> void:
    assert_eq(state.current_health, 100)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** `before_each()` crée une nouvelle instance avant chaque cas ; l’ordre d’exécution n’influence plus le résultat.

### 55.5 Comparer exactement un calcul flottant

**Symptôme :** Une différence numérique minuscule fait échouer une valeur pourtant dans la tolérance du contrat.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
var actual := deg_to_rad(-35.0)
assert_eq(actual, -0.610865)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La constante décimale tronquée n’est pas exactement égale à la représentation flottante calculée.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var actual := deg_to_rad(-35.0)
assert_almost_eq(
    actual,
    -0.610865,
    0.000001
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La tolérance explicite compare l’angle selon la précision réellement nécessaire au système.

### 55.6 Doubler toutes les dépendances

**Symptôme :** Le test répète les appels internes et devient plus long que la règle qu’il vérifie.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
var clock := double(CLOCK_SCRIPT).new()
var repository := double(REPOSITORY_SCRIPT).new()
var policy := double(POLICY_SCRIPT).new()
var bus := double(BUS_SCRIPT).new()
# dizaines de stubs et d’attentes
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le cas remplace même des valeurs et ports simples, puis spécifie l’implémentation au lieu de l’issue observable.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var clock := FakeLogicalClock.new()
var repository := FakeCharacterRepository.new()
var policy := FixedPolicyFixture.create()
var service := CharacterService.new(
    clock,
    repository,
    policy
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les fakes fonctionnels portent les contrats stables ; le test configure seulement les valeurs qui influencent le scénario.

### 55.7 Appeler un test d’intégration un test unitaire

**Symptôme :** Une modification de fichier, de scène ou de base ralentit et fragilise la suite rapide.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
func test_unit_save() -> void:
    var store := FileSaveStore.new("user://saves")
    store.save(&"slot.1", snapshot)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le cas écrit un fichier réel et traverse l’adaptateur de persistance ; il n’est pas isolé à une unité.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
func test_save_command_builds_valid_snapshot() -> void:
    var store := FakeSaveStore.new()
    var service := SaveService.new(store)
    var result := service.save(
        SaveCommandBuilder.new().build()
    )
    assert_eq(result.status, SaveResult.Status.COMMITTED)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le test unitaire utilise un port en mémoire ; l’écriture de fichier reste dans une suite d’intégration nommée et isolée.

### 55.8 Relancer automatiquement un test instable

**Symptôme :** Le pipeline devient vert après plusieurs tentatives sans corriger la cause.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
for attempt in range(3):
    if run_test():
        return OK
return FAILED
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le retry masque une course ou une dépendance au temps et détruit l’information sur la première défaillance.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var result := run_test_once()
if not result.passed:
    FailureArtifacts.write(result)
assert_true(result.passed)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Une seule exécution conserve l’échec, ses paramètres et ses artefacts ; la cause peut être reproduite et corrigée.

### 55.9 Mettre à jour un golden file automatiquement

**Symptôme :** Une régression devient la nouvelle référence sans examen humain.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
var actual := run_scenario()
FileAccess.open(
    expected_path,
    FileAccess.WRITE
).store_string(JSON.stringify(actual))
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le test remplace l’attendu par le résultat courant avant toute comparaison et ne peut donc jamais signaler une différence.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var actual := run_scenario()
var expected := CanonicalJson.read_checked(
    expected_path
)
assert_eq(
    CanonicalValue.normalize(actual),
    CanonicalValue.normalize(expected)
)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le résultat approuvé reste immuable pendant le test ; toute différence échoue et doit être examinée dans un commit distinct.

### 55.10 Appeler un service IA ou réseau réel dans la suite déterministe

**Symptôme :** Le test dépend de la disponibilité locale, du modèle chargé, du réseau ou d’une réponse non déterministe.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
var response := await real_gateway.request(prompt)
assert_true(response.text.contains("forêt"))
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le transport et la génération externes ne garantissent ni disponibilité, ni contenu exact, ni durée bornée identique.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var gateway := FakeLocalAiGateway.new()
gateway.responses[&"req.1"] =     LocalAiResponse.fixture_success(
        &"req.1",
        &"intent.describe_forest"
    )
var result := service.handle(
    LocalAiRequest.fixture(&"req.1"),
    gateway
)
assert_eq(result.intent_id, &"intent.describe_forest")
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le fake fournit une réponse typée et stable ; le test exerce le filtrage et le contrat applicatif sans dépendre du service externe.

## 56. Checklist d’acceptation

Avant d’accepter une suite de tests :

- chaque test nomme un comportement observable ;
- chaque fixture est isolée ou explicitement immuable ;
- les horloges et RNG sont injectés ;
- les écritures utilisent une racine temporaire ;
- les ports externes utilisent des fakes ou enregistrements contrôlés ;
- les refus métier sont distingués des erreurs de framework ;
- les assertions flottantes déclarent leur tolérance ;
- les tests de scène attendent des frames ou signaux avec une borne ;
- les simulations déclarent scénario, version, graines et maximum de ticks ;
- les golden files ne sont jamais régénérés pendant la vérification ;
- le premier cas défaillant reste reproductible ;
- les codes de sortie non nuls ne sont pas masqués ;
- les rapports JUnit sont conservés comme artefacts ;
- les réserves runtime et plateforme sont déclarées.

## 57. Références techniques officielles

- [Godot 4.7 — tests unitaires du moteur](https://docs.godotengine.org/en/4.7/engine_details/architecture/unit_testing.html) ;
- [Godot 4.7 — ligne de commande et mode headless](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html) ;
- [Godot 4.7 — `SceneTree`](https://docs.godotengine.org/en/4.7/classes/class_scenetree.html) ;
- [Godot 4.7 — utilisation du `SceneTree`](https://docs.godotengine.org/en/4.7/tutorials/scripting/scene_tree.html) ;
- [GUT — dépôt officiel et matrice des versions](https://github.com/bitwes/Gut) ;
- [GUT 9.7 — installation](https://gut.readthedocs.io/en/v9.7.0/Install.html) ;
- [GUT 9.7 — création des tests](https://gut.readthedocs.io/en/v9.7.0/Creating-Tests.html) ;
- [GUT 9.7 — ligne de commande](https://gut.readthedocs.io/en/v9.7.0/Command-Line.html) ;
- [GUT 9.7 — doubles](https://gut.readthedocs.io/en/v9.7.0/Doubles.html) ;
- [GUT 9.7 — résultats JUnit](https://gut.readthedocs.io/en/v9.7.0/Export-Test-Results.html).

La référence du projet reste Godot `4.7.1-stable`. La branche GUT destinée à Godot `4.7.x`, les scripts, scènes, bases temporaires et simulations devront être exécutés dans le Starter Kit avant de transformer l’audit en `runtime-tested`.

## 58. Décisions retenues pour Project Asteria

`Project Asteria` adopte GUT sous `addons/gut`, épinglé à un commit compatible avec Godot `4.7.x` et accompagné de sa licence. Les suites sont séparées en `unit`, `integration` et `simulation`, avec des supports partagés qui ne deviennent jamais des dépendances du code runtime.

Les règles pures utilisent des valeurs et fakes contrôlés. Les scènes entrent réellement dans un `SceneTree` lorsque leurs callbacks ou signaux font partie du contrat. Les fichiers, sauvegardes, bases SQLite et pipelines utilisent des espaces temporaires uniques puis nettoyés.

Les horloges logiques, graines et ports aléatoires rendent les simulations reproductibles. Chaque scénario déclare une borne de ticks et produit un snapshot, une séquence événementielle, des compteurs d’invariants et des empreintes canoniques. Une graine défaillante devient un cas permanent lorsqu’elle révèle une régression.

Les golden files restent approuvés et immuables pendant les tests. Les rapports JUnit, différences canoniques et premières graines défaillantes servent d’artefacts. Aucun retry automatique, appel IA réel ou mise à jour silencieuse d’un résultat attendu ne peut rendre une campagne verte.
