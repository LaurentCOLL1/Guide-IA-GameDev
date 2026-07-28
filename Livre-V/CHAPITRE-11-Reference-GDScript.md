---
title: "Livre V — Fiche 11 : Référence GDScript"
id: "DOC-L5-CH11"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 11
last-verified: "2026-07-28T22:02:17+02:00"
audit-status: "complete"
audit-date: "2026-07-28T22:02:17+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-11.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "gdscript-4-7-language-reference"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Référence GDScript

> **Type de document :** aide-mémoire non linéaire, tables de syntaxe, index d’opérateurs et portes de qualification.
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript.
> **Principe :** une forme syntaxique relue n’est ni un script analysé par Godot, ni un comportement runtime validé, ni une garantie pour une autre version du moteur.

## Index express

| Besoin | Ouvrir |
|---|---|
| identifier la portée de cette référence | [GDS-00](#gds-00--contrat-de-la-référence) |
| trouver une notion par tâche | [Matrice A](#matrice-a--sélection-par-besoin) |
| ordonner un fichier et nommer ses membres | [GDS-01](#gds-01--fichier-classe-et-nommage) |
| déclarer une valeur et choisir son type | [GDS-02](#gds-02--déclarations-et-typage) |
| distinguer types valeur, collections et objets | [GDS-03](#gds-03--familles-de-types) |
| retrouver un opérateur ou sa priorité | [Matrice B](#matrice-b--opérateurs-et-priorité) |
| écrire une condition, un `match` ou une boucle | [GDS-04](#gds-04--contrôle-de-flux) |
| définir une fonction, un `Callable` ou un `await` | [GDS-05](#gds-05--fonctions-callables-et-attente) |
| choisir classe, héritage, composition ou propriété | [GDS-06](#gds-06--classes-et-propriétés) |
| choisir une annotation | [GDS-07](#gds-07--annotations-et-inspector) |
| manipuler tableaux et dictionnaires | [GDS-08](#gds-08--collections) |
| comprendre signaux, cycle de vie et validité | [GDS-09](#gds-09--signaux-cycle-de-vie-et-validité) |
| charger une ressource ou utiliser un chemin Godot | [GDS-10](#gds-10--ressources-et-chemins) |
| diagnostiquer erreurs et avertissements | [GDS-11](#gds-11--diagnostics-et-avertissements) |
| retrouver un mot-clé ou une fonction courante | [Matrice C](#matrice-c--index-alphabétique) |
| qualifier une migration de version | [GDS-12](#gds-12--compatibilité-et-acceptation) |

---

<!-- l5:card -->
## GDS-00 — Contrat de la référence

| Champ | Règle |
|---|---|
| autorité pédagogique | [Fondamentaux de GDScript](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#1-rôle-du-chapitre) |
| moteur cible | Godot `4.7.1-stable`, annoncé le 14 juillet 2026 par le projet Godot |
| unité de consultation | mot-clé, type, opérateur, annotation, fonction ou piège |
| preuve | revue statique des sources du dépôt et de la documentation officielle |
| exemples | formes minimales en code inline ; aucun fichier exécutable matérialisé |
| exclus | cours progressif, architecture de gameplay, API exhaustive des classes, benchmark et tutoriel de migration |
| sources externes | [référence GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html), [index GDScript](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/index.html) et [Godot 4.7.1](https://godotengine.org/article/maintenance-release-godot-4-7-1/) |
| état | `static-review` ; aucun parseur GDScript ni moteur lancé |

**Réponse rapide :** cette fiche sert à retrouver une forme et sa frontière. Elle ne remplace pas l’apprentissage détaillé, conformément à la [méthode de lecture des exemples](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#21-méthode-de-lecture-des-exemples) et à la [progression sans répétition](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#22-progression-sans-répétition).

---

<!-- l5:matrix -->
## Matrice A — Sélection par besoin

| Besoin | Forme de départ | Carte | Source propriétaire | Contrôle minimal |
|---|---|---|---|---|
| créer un type global | `class_name Nom` puis `extends Base` | GDS-01 et 06 | [un fichier est une classe](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#3-un-fichier-gdscript-est-une-classe) | unicité du nom et dépendance explicite |
| typer une variable | `var nom: Type = valeur` ou `var nom := valeur` | GDS-02 | [typage progressif](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#10-typage-progressif) | type non ambigu et avertissements relus |
| modéliser un identifiant répété | `StringName` et littéral `&"id"` | GDS-03 | [`StringName`](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#93-stringname) | ne pas convertir les textes destinés au joueur |
| choisir une collection | `Array[T]`, `Dictionary[K, V]` ou `Packed*Array` | GDS-08 | [dictionnaires](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#14-dictionnaires) | type, ordre, duplication et mutation |
| brancher une règle | `if`, `match` ou expression conditionnelle | GDS-04 | [conditions](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#15-conditions) | cas par défaut et comparaison de types |
| suspendre une fonction | `await signal_ou_coroutine` | GDS-05 | [`await` et fonctions suspendues](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#186-await-et-fonctions-suspendues) | annulation, durée de vie et ordre des effets |
| exposer un réglage | `@export var ...` ou annotation spécialisée | GDS-07 | [annotations principales](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#21-annotations-principales) | validation runtime indépendante de l’Inspector |
| réagir à un événement | `signal`, `.connect()` et `.emit()` | GDS-09 | [scènes, nœuds, Resources et signaux](../Livre-II/CHAPITRE-03-Scenes-noeuds-Resources-et-signaux.md) | propriétaire, connexion, déconnexion et durée de vie |
| charger une dépendance fixe | `preload("res://...")` | GDS-10 | [`preload()`](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#241-preload) | chemin connu à l’analyse et ressource attendue |
| signaler un défaut | `push_warning`, `push_error`, `Error` ou `assert` | GDS-11 | [code `Error`](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#282-code-error) | diagnostic distinct de la décision métier |

---

<!-- l5:card -->
## GDS-01 — Fichier, classe et nommage

| Élément | Forme rapide | Règle du guide | Source |
|---|---|---|---|
| fichier | `nom_de_classe.gd` | UTF-8 sans BOM, LF, tabulations | [indentation et format](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#4-indentation-et-format-des-fichiers) |
| type global | `class_name HealthPool` | `PascalCase`, nom global unique | [classes et `class_name`](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#19-classes-héritage-et-classname) |
| base | `extends RefCounted` | relation stable et explicite | [héritage](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#192-héritage) |
| fonction | `func apply_damage(...)` | `snake_case` | [identifiants et nommage](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#7-identifiants-et-conventions-de-nommage) |
| membre privé conventionnel | `_state` ou `_recalculate()` | préfixe `_`, sans protection d’accès réelle | [fonction privée conventionnelle](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#183-fonction-privée-conventionnelle) |
| constante | `MAX_HEALTH` | `CONSTANT_CASE` | [identifiants et nommage](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#7-identifiants-et-conventions-de-nommage) |
| signal | `health_changed` | événement accompli, `snake_case` | [guide de style officiel](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html) |
| documentation | `## Texte` | rôle, contrat et réserves, pas paraphrase du code | [commentaire de documentation](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#62-commentaire-de-documentation) |

**Ordre recommandé :** annotations de classe, `class_name`, `extends`, documentation, signaux, enums, constantes, variables, callbacks virtuels, méthodes publiques, méthodes privées et classes internes. La [section propriétaire](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#5-ordre-recommandé-dun-script) et le [guide officiel](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html#code-order) prévalent sur un ordre improvisé.

---

<!-- l5:card -->
## GDS-02 — Déclarations et typage

| Forme | Sens | Piège |
|---|---|---|
| `var health: int = 100` | variable typée explicitement | valeur incompatible refusée |
| `var origin := Vector3.ZERO` | type inféré depuis une expression claire | éviter lorsque le domaine reste ambigu |
| `const LIMIT: int = 32` | constante de classe | la valeur doit être constante |
| `var value: Variant` | valeur volontairement dynamique | réduit la détection statique |
| `func f(a: int) -> bool` | paramètre et retour typés | `void` signifie absence de valeur utile |
| `value as PlayerController` | conversion vers un type objet, sinon `null` | vérifier le résultat avant usage |
| `value is PlayerController` | test de type | ne transforme pas la valeur |
| `null` | absence de référence ou valeur vide compatible | distinguer objet absent et objet libéré |

Le dépôt privilégie un style typé cohérent. Les types statiques peuvent concerner variables, constantes, paramètres et retours ; ils améliorent l’analyse avant exécution et l’autocomplétion, sans supprimer les erreurs runtime. Voir la [documentation officielle du typage](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/static_typing.html) et la [justification du guide](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#105-pourquoi-typer-le-code-du-guide).

**Limite 4.7.1 :** les collections typées imbriquées telles que `Array[Array[int]]` ou `Dictionary[String, Dictionary[String, int]]` ne sont pas prises en charge directement ; employer une classe, une `Resource` ou une collection extérieure non imbriquée lorsque le contrat devient complexe.

---

<!-- l5:card -->
## GDS-03 — Familles de types

| Famille | Exemples | Sémantique utile | Vigilance |
|---|---|---|---|
| scalaires | `bool`, `int`, `float` | valeurs simples | conversions, division et précision |
| texte et identifiants | `String`, `StringName`, `NodePath` | texte, identifiant interné, chemin Godot | ne pas employer `StringName` pour le contenu utilisateur |
| mathématiques | `Vector2`, `Vector3`, `Quaternion`, `Basis`, `Transform3D`, `Color` | géométrie et rendu | unité, espace local/global et normalisation |
| collections générales | `Array`, `Dictionary` | structures mutables par référence | alias, ordre et duplication |
| collections compactes | `PackedByteArray`, `PackedVector3Array`, etc. | séries homogènes et interfaces moteur | moins de souplesse métier |
| fonctions et événements | `Callable`, `Signal` | comportement transmissible et notification | signature, cible libérée et arguments liés |
| objets | `Object`, `RefCounted`, `Resource`, `Node` | références vers des instances moteur ou script | durée de vie différente selon la base |
| dynamique | `Variant` | union runtime de types Godot | validation obligatoire à la frontière |
| absence de retour | `void` | fonction sans résultat exploitable | ne pas affecter son appel à une variable |

Les types intégrés détaillés restent dans la [table du chapitre pédagogique](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#9-types-de-base) et dans les [classes de référence Godot](https://docs.godotengine.org/en/stable/classes/). Une classe native, globale ou interne peut servir d’annotation de type ; un enum nommé reste représenté par un entier et exige néanmoins une validation du domaine.

---

<!-- l5:matrix -->
## Matrice B — Opérateurs et priorité

| Groupe, du plus prioritaire au moins prioritaire | Formes | Usage | Piège principal |
|---|---|---|---|
| groupement et accès | `()`, `x[i]`, `x.member`, `f()` | contrôler l’ordre et accéder aux valeurs | index hors limites ou membre absent |
| attente et type | `await`, `is`, `is not`, `as` | suspendre, tester ou convertir | `as` peut produire `null` |
| puissance et unaires | `**`, `~`, `+x`, `-x` | puissance, bits, signe | `**` est associatif à gauche en GDScript |
| multiplicatifs | `*`, `/`, `%` | produit, division, reste ou formatage de chaîne | `%` possède deux sens |
| additifs | `+`, `-` | nombres, vecteurs ou concaténation compatible | résultat dépend des types |
| décalages | `<<`, `>>` | bits | réserver aux contrats binaires explicites |
| bit à bit | `&`, `^`, `|` | masques | ne pas confondre avec `and` et `or` |
| comparaisons | `<`, `>`, `==`, `!=`, `<=`, `>=` | ordre ou égalité | `match` est plus strict que `==` pour certains types |
| appartenance | `in`, `not in` | collection, chaîne, dictionnaire ou groupe de nœuds | complexité selon la structure |
| booléens | `not`, `and`, `or` | logique | utiliser des parenthèses lorsque l’intention est ambiguë |
| conditionnel | `a if condition else b` | sélectionner une valeur simple | éviter l’imbrication illisible |
| affectation | `=`, `+=`, `-=`, `*=`, `/=`, `%=` | modifier une variable | ne pas confondre `=` et `==` |

La table résume la [référence officielle des opérateurs](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html#operators). Lorsque plusieurs familles apparaissent dans une expression métier, des variables intermédiaires ou des parenthèses explicites sont préférables à une dépendance implicite à la priorité.

---

<!-- l5:card -->
## GDS-04 — Contrôle de flux

| Forme | Usage | Réserve |
|---|---|---|
| `if` / `elif` / `else` | branches ordonnées | préférer les retours précoces aux imbrications profondes |
| `a if condition else b` | valeur conditionnelle courte | ne pas y cacher plusieurs décisions |
| `match value:` | motifs, enums et états fermés | premier motif correspondant ; `_` couvre le reste |
| `pattern when guard:` | motif avec garde | la garde ne s’évalue qu’après le motif |
| `for item in collection` | itération sur un itérable | un dictionnaire parcourt ses clés |
| `for i in range(n)` | indices bornés | `range(n)` s’arrête avant `n` |
| `while condition` | répétition conditionnelle | progression visible vers la sortie obligatoire |
| `break` | quitter la boucle | aucun élément suivant n’est traité |
| `continue` | passer au tour suivant | les instructions restantes du tour sont ignorées |
| `pass` | bloc volontairement vide | ne doit pas masquer une implémentation oubliée |
| `return` | terminer une fonction | le code suivant du même chemin n’est pas exécuté |

**Choix rapide :** `if` exprime une décision progressive ; `match` convient à une valeur fermée ou à des motifs ; `for` parcourt une collection connue ; `while` exige une condition d’arrêt explicitement maintenue. Voir [conditions](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#15-conditions), [`match`](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#16-match) et [boucles](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#17-boucles).

---

<!-- l5:card -->
## GDS-05 — Fonctions, callables et attente

| Élément | Forme | Contrat |
|---|---|---|
| fonction | `func add(a: int, b: int) -> int:` | paramètres, retour et effets explicites |
| valeur par défaut | `prefix: String = ""` | paramètres optionnels après les obligatoires |
| fonction statique | `static func validate(...)` | ne dépend pas des membres d’une instance |
| méthode parente | `super.reset()` | appelle l’implémentation héritée |
| lambda | `func(value): return value * 2` | crée un `Callable` local |
| référence de méthode | `object.method` | callable lié à l’objet |
| arguments liés | `callable.bind(value)` | ajoute des arguments à la fin de l’appel |
| appel différé | `callable.call_deferred()` | exécution en temps d’inactivité, pas immédiatement |
| attente | `await signal_ou_fonction` | suspend la fonction courante sans bloquer toute l’application |
| résultat suspendu | valeur après `await` | l’appelant ne doit pas supposer l’effet déjà terminé |

La distinction entre fonction, méthode, paramètre, argument et retour est définie dans le [vocabulaire propriétaire](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#180-vocabulaire-indispensable). `Callable` représente une méthode ou une fonction autonome et sert fréquemment aux callbacks de signaux ; consulter sa [classe officielle](https://docs.godotengine.org/en/stable/classes/class_callable.html).

**Limite :** une opération suspendue exige une politique de durée de vie, d’annulation et de résultat tardif. Le détail des signaux et de la scène appartient au chapitre 3, pas à cette référence syntaxique.

---

<!-- l5:card -->
## GDS-06 — Classes et propriétés

| Besoin | Forme | Décision |
|---|---|---|
| type global | `class_name ActorState` | disponible dans le projet sans `preload` |
| base moteur | `extends Node` | participe à l’arbre et à son cycle de vie |
| valeur partagée | `extends RefCounted` | libération par comptage de références |
| données éditables | `extends Resource` | sérialisation et Inspector selon le contrat |
| classe interne | `class Entry:` | détail local non réutilisé ailleurs |
| appel parent | `super.method()` | conserver le contrat hérité |
| propriété simple | `var health: int` | stockage direct |
| accesseur | `var health: int: set(value): ...` | invariant local et léger |
| dépendance | composition par membre typé | préférée à un héritage opportuniste |
| construction | `.new()` | crée une instance de script ou de classe compatible |

L’héritage exprime une relation « est un » stable ; la composition exprime une collaboration. Les accesseurs protègent un invariant court et ne doivent pas déclencher réseau, chargement lourd ou mutation transversale. Voir [classes et héritage](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#19-classes-héritage-et-classname) et [propriétés et accesseurs](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#20-propriétés-et-accesseurs).

---

<!-- l5:card -->
## GDS-07 — Annotations et Inspector

| Annotation | Cible | Effet | Vigilance |
|---|---|---|---|
| `@export` | variable membre | sérialise et expose dans l’Inspector | valider aussi au runtime |
| `@export_range(...)` | nombre | borne et pas d’édition | l’Inspector n’est pas une barrière de sécurité |
| `@export_enum(...)` | `int` ou `String` | choix fermé dans l’Inspector | stocker une identité stable si la liste évolue |
| `@export_file`, `@export_dir` | chemin | sélecteur d’éditeur | vérifier extension, racine et existence |
| `@export_group`, `@export_subgroup` | propriétés suivantes | organisation de l’Inspector | éviter une hiérarchie artificielle |
| `@onready` | variable membre | initialise juste avant `_ready()` | le chemin et le type doivent correspondre |
| `@tool` | script | autorise l’exécution dans l’éditeur | sauvegarde, garde et absence d’effet destructif |
| `@warning_ignore(...)` | déclaration ou ligne suivante | masque un avertissement précis | justification locale et code de l’avertissement exact |
| `@rpc(...)` | méthode | configure un appel réseau | autorité, canal et validation restent au Livre IV |
| `@icon(...)` | classe globale | icône dans l’éditeur | chemin de ressource valide |

Les propriétés exportées sont enregistrées avec la scène ou la `Resource` et deviennent éditables dans l’Inspector ; voir la [documentation officielle](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_exports.html). Le dépôt présente les formes essentielles dans les [annotations principales](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#21-annotations-principales).

**Règle :** une annotation modifie le traitement d’un script, d’une déclaration ou d’une ligne. Elle ne remplace ni validation métier, ni autorisation, ni test du comportement obtenu.

---

<!-- l5:card -->
## GDS-08 — Collections

| Structure | Forme | Usage | Piège |
|---|---|---|---|
| tableau dynamique | `Array` | série hétérogène ou contrat encore ouvert | retours souvent `Variant` |
| tableau typé | `Array[Item]` | série homogène et analysable | pas de type imbriqué direct |
| dictionnaire dynamique | `Dictionary` | métadonnées flexibles | clé absente et valeur `Variant` |
| dictionnaire typé | `Dictionary[StringName, float]` | clés et valeurs fermées | méthodes encore partiellement dynamiques |
| tableau compact | `PackedByteArray`, `PackedVector3Array`, etc. | buffers et grandes séries homogènes | API plus spécialisée |
| duplication | `duplicate(true)` | copie profonde compatible | coût et objets toujours référencés selon leur type |
| lecture sûre | `dict.get(key, fallback)` | valeur de repli | distinguer absence et valeur égale au repli |
| présence | `dict.has(key)` ou `value in array` | test explicite | coût dépend de la collection |
| modification | `append`, `erase`, `clear` | mutation en place | ne pas modifier arbitrairement pendant l’itération |
| tri | `sort`, `sort_custom` | ordre déterminé | définir locale et comparateur si pertinent |

Les tableaux et dictionnaires sont transmis par référence : une seconde variable peut viser la même collection. Une copie indépendante exige une duplication adaptée ; voir [références et duplication](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#134-références-et-duplication) et [dictionnaires typés](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#142-dictionnaire-typé).

**Choix métier :** lorsque les champs sont stables, typés et partagés entre plusieurs systèmes, une classe ou une `Resource` protège mieux les invariants qu’un dictionnaire ouvert.

---

<!-- l5:card -->
## GDS-09 — Signaux, cycle de vie et validité

| Élément | Forme | Moment ou rôle | Réserve |
|---|---|---|---|
| déclaration | `signal health_changed(value: int)` | contrat d’événement | nom d’événement accompli |
| connexion | `source.health_changed.connect(callback)` | associe un `Callable` | éviter les connexions multiples non voulues |
| émission | `health_changed.emit(value)` | notifie les abonnés | ne remplace pas la mutation propriétaire |
| construction | `_init()` | instance créée | enfants de scène pas forcément disponibles |
| entrée dans l’arbre | `_enter_tree()` | nœud attaché | ordre parent/enfant à vérifier |
| prêt | `_ready()` | nœud et enfants prêts | point habituel de `@onready` |
| rendu | `_process(delta)` | chaque image rendue active | fréquence variable |
| physique | `_physics_process(delta)` | pas physique fixe | logique physique uniquement |
| sortie | `_exit_tree()` | retrait de l’arbre | libérer abonnements ou ressources externes |
| validité | `is_instance_valid(object)` | objet natif encore valide | `object != null` ne suffit pas toujours |
| retrait différé | `queue_free()` | suppression de nœud en fin d’image | ne plus l’utiliser ensuite |

Le cycle simplifié appartient au [chapitre pédagogique](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#22-cycle-de-vie-dun-nœud), tandis que les connexions et la composition de scènes sont développées dans [Scènes, nœuds, Resources et signaux](../Livre-II/CHAPITRE-03-Scenes-noeuds-Resources-et-signaux.md). La référence syntaxique ne qualifie aucun ordre runtime complexe.

---

<!-- l5:card -->
## GDS-10 — Ressources et chemins

| Forme | Usage | Moment | Contrôle |
|---|---|---|---|
| `res://` | ressource du projet importée | édition et runtime selon export | chemin versionné et inclus dans le paquet |
| `user://` | données propres à l’utilisateur | runtime | format, quota, sauvegarde et permissions |
| `NodePath` | chemin de nœud ou propriété | scène | chemin stable ou référence typée préférée |
| `$Child/Node` | raccourci de `get_node()` | scène active | type attendu et présence |
| `%UniqueNode` | nœud à nom unique | scène propriétaire | unicité configurée |
| `preload(path_constant)` | dépendance fixe | analyse du script | chemin connu et ressource valide |
| `load(path)` | ressource choisie au runtime | exécution | type, erreur, provenance et taille |
| `ResourceLoader` | chargement avancé | exécution ou thread selon API | statut, cache et compatibilité |
| `FileAccess` | octets ou texte | runtime | encodage, limite et code `Error` |
| `DirAccess` | dossiers | runtime | racine autorisée et effets de bord |

Les chemins Godot ne sont pas des chemins Windows ou Linux ordinaires. `preload()` convient à une dépendance fixe ; `load()` demande validation du résultat et du type. Voir [chargement de ressources](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#24-chargement-de-ressources) et les contrats de données du [chapitre 7](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md).

---

<!-- l5:card -->
## GDS-11 — Diagnostics et avertissements

| Outil | Usage | Ne prouve pas |
|---|---|---|
| erreur de parse | syntaxe refusée avant exécution | comportement des autres fichiers non chargés |
| erreur de type statique | incompatibilité détectée par l’analyse | absence d’erreur runtime |
| `Error` et `OK` | résultat de nombreuses API moteur | détail métier sans traduction explicite |
| `error_string(code)` | texte associé à un code moteur | identité stable destinée à une API métier |
| `print()` | information de développement | journal structuré ou sévérité |
| `push_warning()` | anomalie récupérable | décision d’acceptation |
| `push_error()` | défaut nécessitant correction | exception générale |
| `printerr()` | sortie d’erreur basse couche | contexte suffisant à lui seul |
| `assert(condition, message)` | hypothèse de développement | validation d’entrée non fiable ou garde de production |
| avertissement GDScript | risque ou ambiguïté détecté | défaut certain dans tous les cas |
| `@warning_ignore` | suppression locale justifiée | permission de désactiver globalement le contrôle |

Le système d’avertissements complète le typage et peut être configuré dans les paramètres du projet ; consulter la [documentation stable](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/warning_system.html) et la politique du dépôt dans [Avertissements du langage](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#29-avertissements-du-langage).

**Validation :** un contrôle headless peut importer le projet et faire apparaître des erreurs de scripts chargés, mais ne remplace pas les tests du gameplay ; voir [Validation sans interface](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#33-validation-sans-interface).

---

<!-- l5:matrix -->
## Matrice C — Index alphabétique

| Entrée | Fonction rapide | Carte ou source |
|---|---|---|
| `and`, `or`, `not` | logique booléenne lisible | Matrice B |
| `Array[T]` | tableau typé | GDS-08 |
| `as`, `is` | conversion ou test de type | GDS-02 |
| `assert` | hypothèse de développement | GDS-11 |
| `await` | suspendre la fonction courante | GDS-05 |
| `break`, `continue` | arrêter ou sauter une itération | GDS-04 |
| `Callable` | fonction ou méthode transmissible | GDS-05 |
| `class`, `class_name` | classe interne ou globale | GDS-06 |
| `const`, `var` | constante ou variable | GDS-02 |
| `Dictionary[K, V]` | association typée clé/valeur | GDS-08 |
| `emit`, `connect` | publier ou écouter un signal | GDS-09 |
| `enum` | constantes nommées liées | GDS-01 et 03 |
| `extends`, `super` | héritage et parent | GDS-06 |
| `for`, `while`, `range` | boucles | GDS-04 |
| `func`, `return`, `void` | fonction et résultat | GDS-05 |
| `if`, `elif`, `else`, `match` | branchement | GDS-04 |
| `is_instance_valid` | validité d’un objet | GDS-09 |
| `load`, `preload` | chargement dynamique ou fixe | GDS-10 |
| `null`, `Variant` | absence ou type dynamique | GDS-02 et 03 |
| `pass` | bloc volontairement vide | GDS-04 |
| `push_error`, `push_warning` | diagnostics moteur | GDS-11 |
| `queue_free` | retrait différé d’un nœud | GDS-09 |
| `StringName`, `NodePath` | identifiant et chemin Godot | GDS-03 et 10 |
| `@export`, `@onready`, `@tool` | métadonnées de script ou membre | GDS-07 |
| `:=`, `->` | inférence et type de retour | GDS-02 et 05 |

Cet index n’énumère pas toutes les méthodes des classes natives. La [classe de référence Godot](https://docs.godotengine.org/en/stable/classes/) reste l’autorité pour signatures, propriétés et constantes d’API.

---

<!-- l5:card -->
## GDS-12 — Compatibilité et acceptation

| Porte | Preuve minimale | État de cette fiche |
|---|---|---|
| version du moteur | binaire exact et empreinte ou source de téléchargement | référence documentaire `4.7.1-stable` seulement |
| analyse syntaxique | import ou parse de tous les scripts concernés | non exécuté |
| avertissements | configuration enregistrée et rapport sans défaut bloquant | non exécuté |
| types | erreurs et lignes dangereuses relues | non exécuté |
| scène minimale | instanciation et cycle de vie observés | non exécuté |
| tests purs | fonctions déterministes et cas limites | non exécuté |
| intégration | signaux, ressources, fichiers et nœuds réels | non exécuté |
| migration | comparaison avant/après sur une branche dédiée | non exécuté |
| documentation | ancres internes et sources officielles vérifiées | effectué statiquement |
| publication | audit, preuve, licences et réserves | documenté, sans artefact du Companion Pack |

**Règle de version :** une page `latest` peut décrire une fonctionnalité instable. Pour une qualification, employer la documentation correspondant à la version de référence et enregistrer toute différence avec `4.7.1-stable`. La release de maintenance recommande sauvegarde ou contrôle de version avant mise à niveau.

**Acceptation documentaire :** la fiche est acceptée au niveau `static-review` lorsque structure, métadonnées, marqueurs, liens locaux, fragments propriétaires et absence de PDF passent. Une forme GDScript ne devient `syntax-checked`, `tested` ou `qualified` qu’après les portes correspondantes de la [bibliothèque de recettes](CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md#code-01--statut-et-niveau-de-preuve) et des [tests déterministes](../Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md#34-tests-déterministes).
