---
title: "Livre V — Fiche 12 : Référence Python"
id: "DOC-L5-CH12"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 12
last-verified: "2026-07-28T22:48:26+02:00"
audit-status: "complete"
audit-date: "2026-07-28T22:48:26+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-12.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "python-3-14-automation-reference"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Référence Python

> **Type de document :** aide-mémoire non linéaire pour les outils, scripts et chaînes d’automatisation du guide.
> **Versions de référence :** CPython `3.14.6` comme cible principale et CPython `3.13.14` comme repli provisoire.
> **Principe :** une forme Python relue n’est ni un module compilé, ni un test réussi, ni une distribution construite, ni une compatibilité de dépendances démontrée.

## Index express

| Besoin | Ouvrir |
|---|---|
| identifier le périmètre de la référence | [PY-00](#py-00--contrat-de-la-référence) |
| choisir la bonne famille d’outil | [Matrice A](#matrice-a--sélection-par-besoin) |
| distinguer interpréteur, environnement et commande | [PY-01](#py-01--interpréteur-et-environnement) |
| retrouver types et annotations | [PY-02](#py-02--valeurs-types-et-annotations) |
| choisir une collection ou un modèle de données | [PY-03](#py-03--collections-et-modèles-de-données) |
| comparer retour, exception et gestion de ressource | [Matrice B](#matrice-b--flux-erreurs-et-ressources) |
| écrire une condition, une boucle ou un `match` | [PY-04](#py-04--contrôle-de-flux) |
| définir une fonction, un générateur ou un callable | [PY-05](#py-05--fonctions-et-itération) |
| organiser modules, paquets et imports | [PY-06](#py-06--modules-paquets-et-imports) |
| lire ou écrire des fichiers de manière bornée | [PY-07](#py-07--fichiers-chemins-et-sérialisation) |
| construire une CLI et appeler un processus | [PY-08](#py-08--cli-processus-et-codes) |
| définir tests, fixtures et déterminisme | [PY-09](#py-09--tests-et-déterminisme) |
| déclarer et verrouiller les dépendances | [PY-10](#py-10--dépendances-et-verrouillage) |
| construire une distribution ou un point d’entrée | [PY-11](#py-11--packaging-et-points-dentrée) |
| comparer Python et GDScript | [Matrice C](#matrice-c--correspondances-python-et-gdscript) |
| qualifier sécurité et compatibilité | [PY-12](#py-12--sécurité-compatibilité-et-acceptation) |

---

<!-- l5:card -->
## PY-00 — Contrat de la référence

| Champ | Règle |
|---|---|
| autorité plateforme | [Python et environnements virtuels](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#1-pourquoi-isoler-python) |
| autorité automatisation | [Automatisation Python et génération de données](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#1-rôle-du-chapitre) |
| cible | CPython `3.14.6` ; repli CPython `3.13.14`, tous deux provisoires pour le futur Companion Pack |
| unité de consultation | syntaxe, type, module standard, contrat CLI, dépendance, test ou artefact de packaging |
| exemples | formes minimales en code inline ; aucun fichier `.py` matérialisé par cette fiche |
| preuve | revue statique du dépôt et des documentations officielles Python et PyPA |
| exclus | cours général, tutoriel d’installation, framework web, notebook, data science et API exhaustive |
| sources externes | [référence Python 3.14](https://docs.python.org/3.14/reference/), [bibliothèque standard](https://docs.python.org/3.14/library/) et [CPython 3.14.6](https://www.python.org/downloads/release/python-3146/) |
| état | `static-review` ; aucun interpréteur, compilateur, test runner ou outil de build lancé |

**Réponse rapide :** Python sert ici à transformer des fichiers, orchestrer des outils, valider des schémas et produire des artefacts. Il ne devient pas l’autorité métier du jeu, conformément au [rôle du chapitre d’automatisation](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#1-rôle-du-chapitre).

---

<!-- l5:matrix -->
## Matrice A — Sélection par besoin

| Besoin | Point de départ | Carte | Source propriétaire | Contrôle minimal |
|---|---|---|---|---|
| isoler un outil | interpréteur explicite et environnement `.venv` | PY-01 | [composants à distinguer](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#2-les-composants-à-distinguer) | version, exécutable et reconstruction |
| typer une interface interne | annotations, `Protocol`, `TypedDict` ou dataclass | PY-02 et 03 | [architecture cible](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#4-architecture-cible) | analyse statique distincte du runtime |
| transformer des fichiers | fonctions pures, `Path`, encodage explicite | PY-05 et 07 | [résoudre la racine](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#16-résoudre-la-racine-du-dépôt) | chemins bornés et sortie en staging |
| exposer une commande | `argparse`, `main(argv) -> int` et codes stables | PY-08 | [router la commande principale](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#15-router-la-commande-principale) | aide, stderr, code et effets |
| tester une règle | test isolé, fixture synthétique et oracle | PY-09 | [définitions des tests](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md#4-définitions-opérationnelles) | nominal, refus, limite et répétition |
| reproduire un environnement | `pyproject.toml`, verrou et synchronisation stricte | PY-10 | [`pyproject.toml`](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#10-pyprojecttoml) | interpréteur, plateforme et verrou cohérents |
| publier un outil | paquet installable, wheel et point d’entrée | PY-11 | [déclarer le projet](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#8-déclarer-le-projet-dans-pyprojecttoml) | build propre, installation neuve et licence |
| écrire une règle gameplay | GDScript propriétaire, pas Python par défaut | Matrice C | [Référence GDScript](CHAPITRE-11-Reference-GDScript.md#gds-00--contrat-de-la-référence) | autorité du système et frontière de processus |

---

<!-- l5:card -->
## PY-01 — Interpréteur et environnement

| Élément | Forme ou preuve | Règle |
|---|---|---|
| implémentation | `CPython` | ne pas confondre langage Python et implémentation |
| version | `3.14.6` ou repli `3.13.14` | enregistrer série, patch et architecture |
| exécutable | `sys.executable` | prouve le processus courant, pas la reconstruction |
| environnement | `sys.prefix != sys.base_prefix` | indique généralement un environnement virtuel actif |
| création | `python -m venv .venv` | environnement jetable, local et non versionné |
| activation | commodité du shell | non requise lorsque l’exécutable interne est appelé directement |
| module | `python -m module` | lie le module à l’interpréteur choisi |
| projet `uv` | `uv sync --locked` | reconstruit selon le verrou compatible et l’outil installé |
| cache | accélération régénérable | ne constitue ni source canonique ni sauvegarde |
| matrice | OS, architecture, version Python et dépendances | une combinaison réussie n’en qualifie pas une autre |

Un environnement virtuel possède ses propres paquets et doit pouvoir être supprimé puis recréé. Il n’est pas portable par copie ; voir la [documentation `venv`](https://docs.python.org/3.14/library/venv.html) et la règle du guide [recréer plutôt que réparer indéfiniment](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#16-recréer-plutôt-que-réparer-indéfiniment).

**Limite :** la présence de CPython `3.14.6` sur Windows ou Linux ne prouve pas que les bibliothèques natives, backends GPU ou outils IA du projet proposent une roue compatible.

---

<!-- l5:card -->
## PY-02 — Valeurs, types et annotations

| Notion | Forme rapide | Sémantique utile | Vigilance |
|---|---|---|---|
| absence | `None` | valeur singleton | ne pas confondre avec chaîne vide, zéro ou collection vide |
| booléens | `bool` | `True` ou `False` | la vérité implicite peut masquer une intention |
| nombres | `int`, `float` | entier arbitraire et flottant binaire | unités, arrondis et valeurs non finies |
| texte | `str` | Unicode | encodage requis lors des E/S |
| octets | `bytes`, `bytearray` | données binaires | distinguer immuable et mutable |
| annotation | `name: Type` | contrat pour outils et lecteurs | ne valide pas automatiquement au runtime |
| union | `A | B` | valeur de plusieurs types admis | éviter les unions trop larges |
| option | `T | None` | absence explicitement prévue | tester avant usage |
| alias | `type Name = ...` | nomme un contrat | versionner les changements de sens |
| garde | `isinstance(value, Type)` | validation runtime partielle | les génériques paramétrés ne sont pas tous testables ainsi |
| dynamique | `Any` | désactive largement le contrôle statique | réserver aux frontières réellement dynamiques |

La référence officielle du [module `typing`](https://docs.python.org/3.14/library/typing.html) décrit les annotations destinées aux outils. Une annotation ne remplace ni parseur de schéma, ni validation métier, ni test. Les scripts du guide peuvent conserver `from __future__ import annotations` lorsque leur politique de compatibilité l’exige, sans supposer que toutes les bibliothèques introspectent les annotations de la même manière.

---

<!-- l5:card -->
## PY-03 — Collections et modèles de données

| Structure | Usage | Propriété | Piège |
|---|---|---|---|
| `list[T]` | séquence mutable | ordre conservé | alias et mutation partagée |
| `tuple[T, ...]` | séquence immuable | hachable si ses éléments le sont | ne rend pas les objets contenus immuables |
| `dict[K, V]` | association clé-valeur | ordre d’insertion conservé | égalité métier distincte de l’ordre |
| `set[T]` | ensemble unique | ordre non contractuel | sortie à trier avant sérialisation déterministe |
| `frozenset[T]` | ensemble immuable | hachable selon éléments | ordre toujours non contractuel |
| dataclass | données structurées avec comportement léger | champs déclarés | validation à ajouter explicitement |
| dataclass gelée | `@dataclass(frozen=True, slots=True)` | intention d’immuabilité et empreinte mémoire bornée | objets imbriqués encore mutables |
| `TypedDict` | dictionnaire à clés connues pour analyse statique | compatible avec un `dict` runtime | aucune validation automatique |
| `NamedTuple` | enregistrement positionnel immuable | index et noms | moins adapté aux invariants complexes |
| `Enum` / `IntEnum` | identités fermées | membres nommés | valeur sérialisée à stabiliser |
| `Protocol` | interface structurelle | dépendance sur capacités | ne crée pas d’adaptateur runtime |

Pour un manifeste stable, une dataclass ou un modèle validé est préférable à un dictionnaire ouvert. Le [manifeste d’artefact du chapitre 29](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#21-définir-un-manifeste-dartefact) illustre cette séparation entre enregistrement de fichier et campagne.

---

<!-- l5:matrix -->
## Matrice B — Flux, erreurs et ressources

| Situation | Forme Python | Résultat | À éviter |
|---|---|---|---|
| résultat nominal | `return value` | transmet une valeur à l’appelant | code d’erreur caché dans une chaîne libre |
| absence attendue | `T | None` ou résultat typé | oblige à traiter l’absence | exception utilisée comme branche habituelle |
| entrée invalide | `raise ValueError(...)` | interrompt le chemin courant | exception avalée sans contexte |
| fichier absent | `FileNotFoundError` | cause précise issue des E/S | remplacer par `None` sans diagnostic |
| erreur applicative | classe d’exception dédiée | catégorie stable | hiérarchie excessive sans appelants |
| frontière CLI | capturer, diagnostiquer, retourner un code | contrat de processus stable | laisser une traceback comme seule interface |
| ressource | `with resource:` | fermeture même en cas d’exception | fermeture manuelle dispersée |
| nettoyage multiple | `contextlib.ExitStack` | ressources composées | pile de `try/finally` incohérente |
| reprise | checkpoint validé et idempotence | continuation bornée | relance infinie ou sortie partielle promue |
| arrêt | `KeyboardInterrupt`, signal ou délai traduit | état final explicite | confondre annulation et succès |

Les [exceptions intégrées](https://docs.python.org/3.14/library/exceptions.html) et les [utilitaires de contexte](https://docs.python.org/3.14/library/contextlib.html) fournissent les mécanismes ; le contrat métier décide lesquelles traversent une couche. Contrairement à Python, GDScript ne possède pas un mécanisme général d’exceptions équivalent.

---

<!-- l5:card -->
## PY-04 — Contrôle de flux

| Forme | Usage | Réserve |
|---|---|---|
| `if` / `elif` / `else` | branches ordonnées | conditions explicites lorsque la vérité implicite est ambiguë |
| expression conditionnelle | valeur courte | éviter les imbrications |
| `for item in iterable` | parcours d’un itérable | ne pas dépendre d’un ordre non contractuel |
| `enumerate(values)` | index et valeur | préférer à une gestion manuelle de compteur |
| `zip(a, b, strict=True)` | parcours parallèle | `strict=True` révèle les longueurs incompatibles |
| `while condition` | répétition conditionnelle | progression et limite visibles |
| `break` / `continue` | sortie ou saut d’itération | effets précédents du tour déjà réalisés |
| `match` / `case` | motifs structurels | sémantique différente du `match` GDScript |
| compréhension | transformation simple | éviter effets de bord et logique complexe |
| `all` / `any` | agrégation booléenne paresseuse | itérable consommé une seule fois |
| clause `else` de boucle | exécutée sans `break` | utiliser seulement lorsque l’intention est claire |

Pour une génération reproductible, trier les entrées avant la boucle lorsque leur source ne garantit pas l’ordre. Le chapitre 29 applique cette règle dans [Trier les sources avant génération](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#23-trier-les-sources-avant-génération).

---

<!-- l5:card -->
## PY-05 — Fonctions et itération

| Élément | Forme | Contrat |
|---|---|---|
| fonction | `def name(arg: T) -> R:` | paramètres, retour et effets documentés |
| paramètres nommés | `*, option=False` | interdit les appels positionnels fragiles |
| valeur par défaut | objet immuable ou `None` | éviter liste ou dictionnaire mutable partagé |
| fonction pure | mêmes entrées, même résultat | sans E/S ni état global |
| callable | `Callable[[T], R]` | fonction ou objet appelable |
| lambda | expression courte | pas de logique métier complexe |
| générateur | `yield value` | itération paresseuse et état suspendu |
| itérateur | `iter()` / `next()` | consommation progressive | une seconde lecture peut être vide |
| décorateur | transforme fonction ou classe | ordre et métadonnées à vérifier |
| fermeture | capture des noms environnants | attention aux variables de boucle liées tardivement |
| fonction asynchrone | `async def` / `await` | dépend d’une boucle d’événements et d’une politique d’annulation |

Les fonctions pures facilitent tests et déterminisme ; les adaptateurs concentrent fichiers, processus et réseau. Cette séparation reprend l’[architecture cible de l’automatisation](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#4-architecture-cible). La documentation des [fonctions](https://docs.python.org/3.14/tutorial/controlflow.html#defining-functions) et des [générateurs](https://docs.python.org/3.14/reference/expressions.html#yield-expressions) précise la syntaxe, sans qualifier les effets métier.

---

<!-- l5:card -->
## PY-06 — Modules, paquets et imports

| Élément | Rôle | Décision |
|---|---|---|
| module | fichier importable | nom `snake_case`, responsabilité bornée |
| paquet | espace de modules | structure installable préférée aux modifications de `sys.path` |
| `__init__.py` | initialise ou déclare le paquet classique | garder les effets d’import minimaux |
| import absolu | dépendance lisible depuis le paquet | forme privilégiée hors voisinage interne clair |
| import relatif | relation locale au paquet | ne pas remonter au-delà de l’architecture prévue |
| `__all__` | surface d’export déclarée | ne sécurise pas les membres internes |
| garde principale | `if __name__ == "__main__":` | sépare import et exécution directe |
| point d’entrée | fonction `main()` installée | meilleure interface qu’un import avec effet |
| métadonnées | `importlib.metadata` | version de distribution installée | nom de distribution parfois différent du nom importé |
| ressources | `importlib.resources` | fichiers embarqués dans le paquet | ne pas supposer un chemin physique ordinaire |
| import dynamique | `importlib` ou entry points | plugins contrôlés | provenance et conflits à qualifier |

Un import exécute le corps supérieur du module une fois par processus et peut donc avoir des effets de bord. Le guide privilégie des modules importables sans écriture, réseau ou lancement de processus. L’arborescence `src/` du [chapitre 29](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#5-organiser-larborescence-dautomatisation) sépare le paquet versionné des workspaces régénérables.

---

<!-- l5:card -->
## PY-07 — Fichiers, chemins et sérialisation

| Besoin | Forme | Contrôle |
|---|---|---|
| chemin local | `Path` | racine explicite, résolution et plateforme |
| joindre un chemin | `root / "child"` | ne pas concaténer des séparateurs à la main |
| borner une sortie | `candidate.is_relative_to(root)` après résolution | liens symboliques et course temporelle à considérer |
| ouvrir du texte | `path.open("r", encoding="utf-8")` | encodage, taille et erreurs |
| ouvrir des octets | `path.open("rb")` | type et limite de lecture |
| remplacement contrôlé | fichier temporaire voisin puis `os.replace` | ne garantit pas une atomicité universelle |
| JSON | `json.load` / `json.dump` | schéma, profondeur, taille et nombres non finis |
| JSON canonique | clés triées, séparateurs stables, UTF-8 | convention propriétaire à versionner |
| CSV | module `csv` avec `newline=""` | dialecte, séparateur et en-têtes |
| TOML | `tomllib` en lecture | écriture confiée à un outil adapté |
| archive | `zipfile` / `tarfile` | chemins internes, bombes et extraction bornée |
| empreinte | lecture par blocs et SHA-256 | intégrité des octets, pas provenance |

`pathlib` fournit des [chemins orientés objet](https://docs.python.org/3.14/library/pathlib.html), mais la politique de sécurité reste applicative. Voir [Interdire les sorties hors du workspace](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#17-interdire-les-sorties-hors-du-workspace), [Écrire un fichier par remplacement contrôlé](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#18-écrire-un-fichier-par-remplacement-contrôlé) et [Sérialiser du JSON canonique](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#19-sérialiser-du-json-canonique).

**Frontière :** les formats d’échange et leurs schémas appartiennent au chapitre 13 ; cette carte couvre seulement les primitives Python qui les manipulent.

---

<!-- l5:card -->
## PY-08 — CLI, processus et codes

| Élément | Contrat |
|---|---|
| parser | `argparse.ArgumentParser` avec aide, types et sous-commandes |
| arguments | liste explicite `argv` pour permettre les tests |
| fonction principale | `main(argv: list[str] | None = None) -> int` |
| succès | code `0` et sortie nominale stable |
| usage invalide | code distinct, généralement `2` avec `argparse` |
| erreur métier | code non nul documenté et diagnostic sur stderr |
| arrêt | `raise SystemExit(main())` à la garde principale |
| stdout | résultat nominal ou format machine convenu |
| stderr | diagnostic actionnable sans secret |
| processus natif | `subprocess.run([...], shell=False, check=False, timeout=...)` |
| environnement | dictionnaire minimal hérité ou construit explicitement |
| sortie partielle | staging, statut d’échec et nettoyage ou reprise |
| journal | corrélation, versions et chemins relatifs utiles |

La bibliothèque standard documente [`argparse`](https://docs.python.org/3.14/library/argparse.html), [`sys.exit`](https://docs.python.org/3.14/library/sys.html#sys.exit) et [`subprocess`](https://docs.python.org/3.14/library/subprocess.html). Une liste d’arguments est préférable à une chaîne de shell ; aucune donnée non fiable ne doit devenir du code de commande.

Le contrat complet reste celui de la [CLI du chapitre 29](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#15-router-la-commande-principale) et de la [bibliothèque de recettes](CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md#code-02--interface-et-codes-de-sortie).

---

<!-- l5:card -->
## PY-09 — Tests et déterminisme

| Élément | Définition | Preuve attendue |
|---|---|---|
| cas | entrée, préconditions, action et oracle | identifiant stable |
| test unitaire | règle isolée | doubles minimaux et aucun service réel |
| test d’intégration | frontière réelle ciblée | fichiers, processus ou base enregistrés |
| fixture | état contrôlé avant le test | source synthétique et nettoyage |
| répertoire temporaire | espace isolé par cas | aucun chemin utilisateur réel |
| oracle | résultat attendu observable | calcul indépendant ou golden file revu |
| paramétrage | même contrat sur plusieurs cas | cas lisibles et identifiés |
| graine | état pseudo-aléatoire local | générateur local et namespace stable |
| horloge | valeur injectée ou figée | aucun `now()` caché dans une règle |
| ordre | tri explicite | pas de dépendance à l’ordre du système de fichiers |
| locale et fuseau | configuration enregistrée | formats non dépendants de la machine |
| propriété | invariant sur de nombreuses entrées | stratégie, version et exemple réduit conservés |
| couverture | zones exercées | ne prouve pas la qualité des assertions |
| instabilité | échec intermittent analysé | pas de relance silencieuse jusqu’au vert |

`unittest` appartient à la [bibliothèque standard](https://docs.python.org/3.14/library/unittest.html) ; un autre runner peut être adopté après qualification. Le chapitre 27 possède la stratégie de tests et le chapitre 29 les fonctions déterministes. Cette fiche n’exécute aucun test et ne présente aucune couverture.

---

<!-- l5:card -->
## PY-10 — Dépendances et verrouillage

| Artefact ou notion | Rôle | Ne pas confondre |
|---|---|---|
| interpréteur | exécute le langage et la bibliothèque standard | environnement du projet |
| environnement virtuel | installe les distributions d’un projet | source versionnée |
| distribution | paquet publié et installé | nom de module importé |
| dépendance directe | exigence déclarée par le projet | paquet transitif résolu |
| `pyproject.toml` | métadonnées, contraintes et configuration d’outils | résolution exacte |
| `dependencies` | exigences runtime distribuées | groupes de développement |
| `dependency-groups` | tests, lint, documentation ou scripts internes | extras publiés |
| fichier de verrouillage | résolution exacte pour un outil et un contexte | preuve de compatibilité runtime |
| `requirements.txt` | entrée ou export compatible avec certains workflows | source universelle du projet |
| marqueur d’environnement | dépendance conditionnelle | test réellement passé sur la plateforme |
| index de paquets | source de distributions | dépôt de code source |
| cache | copie accélérant l’installation | registre d’intégrité ou sauvegarde |
| SBOM | inventaire des composants | validation de licence ou absence de vulnérabilité |

Le [chapitre d’environnement](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#9-ajouter-et-retirer-des-dépendances) distingue intention, verrou et environnement. La spécification [`pyproject.toml`](https://packaging.python.org/en/latest/specifications/pyproject-toml/) définit notamment `[build-system]`, `[project]`, `[project.scripts]` et `[tool]`; les [groupes de dépendances](https://packaging.python.org/en/latest/specifications/dependency-groups/) servent aux besoins internes sans devenir les métadonnées de la distribution.

**Règle :** une mise à jour de dépendance est une modification contrôlée avec environnement neuf, tests, rapports et point de retour. `pip freeze` décrit un état ; il ne remplace pas nécessairement une politique de dépendances maintenable.

---

<!-- l5:card -->
## PY-11 — Packaging et points d’entrée

| Élément | Rôle | Porte |
|---|---|---|
| arbre source | code et métadonnées versionnés | dépôt propre et fichiers attendus |
| backend de build | construit selon `[build-system]` | version et dépendances de build qualifiées |
| sdist | archive de sources | contenu, licence et reconstruction vérifiés |
| wheel | distribution construite | tags Python, ABI et plateforme contrôlés |
| build isolé | environnement temporaire de construction | aucune dépendance implicite locale |
| installation éditable | boucle de développement | ne représente pas l’artefact publié |
| `[project.scripts]` | commande console vers une fonction | `main()` stable et import sans effet |
| entry point | composant découvrable | groupe, nom et conflit documentés |
| version | identité de distribution | stratégie de version et source unique |
| métadonnées | nom, licence, Python requis et dépendances | cohérence avec les fichiers publiés |
| `RECORD` / empreintes | inventaire d’une wheel installable | pas une signature d’auteur |
| signature ou attestation | provenance supplémentaire | infrastructure et politique distinctes |
| dépôt de paquets | canal de publication | authentification, retrait et rétention |

La PyPA décrit les [métadonnées de projet](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/), les [points d’entrée](https://packaging.python.org/en/latest/specifications/entry-points/) et les [distributions sources](https://packaging.python.org/en/latest/specifications/source-distribution-format/). Le chapitre 29 définit un point d’entrée CLI dans `pyproject.toml`, mais cette fiche ne construit ni sdist ni wheel.

**Frontière :** un script interne peut rester un module non publié. Le packaging devient utile lorsqu’il faut installer, versionner, découvrir ou distribuer l’outil de façon reproductible.

---

<!-- l5:matrix -->
## Matrice C — Correspondances Python et GDScript

| Besoin | Python | GDScript | Différence décisive |
|---|---|---|---|
| variable typée | `name: Type = value` | `var name: Type = value` | annotation Python non imposée automatiquement au runtime |
| inférence | type déduit par l’outil ou le runtime | `:=` donne un type statique inféré | modèles de typage distincts |
| absence | `None` | `null` | validité d’un objet Godot libéré exige un contrôle supplémentaire |
| séquence | `list[T]`, `tuple[T, ...]` | `Array[T]`, `Packed*Array` | tuple immuable et PackedArrays spécifiques au moteur |
| association | `dict[K, V]` | `Dictionary[K, V]` | API et limites des génériques différentes |
| enregistrement | dataclass, `TypedDict`, modèle validé | classe, `RefCounted` ou `Resource` | aucune équivalence automatique avec l’Inspector |
| fonction | `def` | `func` | exceptions et paramètres possèdent des contrats différents |
| classe | `class Child(Base)` | `extends Base` | Python permet héritage multiple ; le guide privilégie la composition |
| branchement | `if`, `match/case` | `if`, `match` | motifs et égalités ne sont pas interchangeables |
| attente | `async def` et `await` | fonction suspendue avec `await` | boucle d’événements et cycle moteur différents |
| erreur | exceptions et retours typés | retours, codes `Error` et diagnostics | pas d’exception générale GDScript |
| événement | callback, file ou bibliothèque | `signal` natif | pas de signal Python universel |
| exposition éditeur | métadonnées ou framework dédié | `@export`, `@tool` | aucune annotation Python standard équivalente |
| fichier projet | `Path` du système | `res://`, `user://`, `FileAccess` | espaces de chemins et export Godot distincts |
| outil CLI | `argparse`, `sys.exit` | `SceneTree`, arguments OS et `quit()` | processus Python séparé du moteur |
| autorité | automatisation et transformation | runtime et logique Godot | ne pas traduire mécaniquement une responsabilité |

La [Référence GDScript](CHAPITRE-11-Reference-GDScript.md#matrice-b--opérateurs-et-priorité) reste propriétaire de la syntaxe du moteur. Une ressemblance de mots-clés ne prouve ni équivalence de type, ni compatibilité d’API, ni pertinence architecturale.

---

<!-- l5:card -->
## PY-12 — Sécurité, compatibilité et acceptation

| Porte | Preuve minimale | État de cette fiche |
|---|---|---|
| version Python | binaire exact, architecture et empreinte ou provenance | référence documentaire `3.14.6` et repli `3.13.14` |
| environnement | reconstruction neuve depuis les déclarations | non exécutée |
| syntaxe | compilation de tous les modules ciblés | non exécutée |
| imports | import propre sans effet non prévu | non exécuté |
| typage | analyseur, configuration et rapport | non exécutés |
| tests | suites unitaires et d’intégration | non exécutées |
| CLI | aide, codes, stdout, stderr, délai et annulation | non exécutés |
| fichiers | limites, chemins, encodages et remplacement contrôlé | non exécutés |
| dépendances | verrou, roues, licences et vulnérabilités | non qualifiés pour la fiche |
| packaging | sdist, wheel, installation neuve et point d’entrée | non construits |
| sécurité | données non fiables, archives, sérialisations et processus | contrôles documentés seulement |
| compatibilité | Windows, WSL/Linux, Solo et Studio | non qualifiée par cette fiche |
| documentation | ancres, sources et frontières | effectuée statiquement |
| publication | audit, preuve et réserves | documentée sans artefact du Companion Pack |

**Risques prioritaires :** ne jamais charger un `pickle` ou objet sérialisé exécutable non fiable ; ne pas extraire une archive sans contrôler ses chemins et limites ; ne pas passer une entrée non fiable à `shell=True`, `eval` ou `exec` ; ne pas journaliser secrets ou données personnelles ; ne pas supposer qu’une wheel disponible sur une plateforme existe sur une autre ; ne pas confondre verrouillage, provenance et innocuité.

La [sécurité de la chaîne Python](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#17-sécurité-de-la-chaîne-python), les [frontières d’effets de la bibliothèque de recettes](CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md#code-09--frontières-deffets) et les politiques du Livre IV prévalent sur un raccourci de commodité.

**Acceptation documentaire :** la fiche est acceptée au niveau `static-review` lorsque métadonnées, cartes, matrices, liens locaux, fragments propriétaires et absence de PDF passent. Un module ne devient `syntax-checked`, `tested`, `qualified` ou publiable qu’après une campagne enregistrée avec versions, commandes, codes, rapports, artefacts et réserves.
