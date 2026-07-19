#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def case(
    number: str,
    title: str,
    symptom: str,
    bad_lang: str,
    bad_code: str,
    correction: str,
    good_marker: str,
    good_lang: str,
    good_code: str,
    difference: str,
) -> str:
    return f'''### {number} {title}

**Symptôme ou risque :** {symptom}

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```{bad_lang}
{bad_code.rstrip()}
```

**Correction :** {correction}

> **{good_marker}**

```{good_lang}
{good_code.rstrip()}
```

**Différence :** {difference}
'''


def section(heading: str, intro: str, cases: list[str]) -> str:
    return f'''{heading}

<!-- qa:error-correction-section -->

{intro}

''' + "\n".join(cases).rstrip() + "\n"


def replace_section(path: str, start_heading: str, next_heading: str, replacement: str) -> None:
    file_path = ROOT / path
    text = file_path.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"^{re.escape(start_heading)}\n.*?(?=^{re.escape(next_heading)}\n)",
        re.MULTILINE | re.DOTALL,
    )
    updated, count = pattern.subn(replacement + "\n", text, count=1)
    if count != 1:
        raise RuntimeError(f"Section introuvable ou ambiguë dans {path}: {start_heading}")
    file_path.write_text(updated, encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    file_path = ROOT / path
    text = file_path.read_text(encoding="utf-8")
    if old not in text:
        raise RuntimeError(f"Texte introuvable dans {path}: {old[:80]!r}")
    file_path.write_text(text.replace(old, new, 1), encoding="utf-8")


def add_supplemental_audit(path: str) -> None:
    file_path = ROOT / path
    text = file_path.read_text(encoding="utf-8")
    marker = 'supplemental-audit: "Livre-II/QA/AUDIT-RETROACTIF-EXEMPLES-ERREURS-CH01-CH06.md"'
    if marker in text:
        return
    needle = 'audit-report:'
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith(needle):
            lines.insert(index + 1, marker)
            file_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            return
    raise RuntimeError(f"audit-report absent dans {path}")


ch1 = section(
    "## 28. Erreurs fréquentes",
    "Chaque cas associe désormais une situation fautive, une correction observable et l’explication de la différence.",
    [
        case(
            "28.1", "Le projet n’apparaît pas dans le Project Manager",
            "le mauvais dossier est importé et `project.godot` se trouve un niveau plus bas.",
            "text", "C:\\IA-GameDev\\projects\\project-asteria\\project-asteria\\project.godot",
            "importer le dossier qui contient directement `project.godot` et vérifier son existence avant l’ouverture.",
            "[PS] PowerShell 7 — Exemple corrigé depuis le dossier supposé du projet.",
            "powershell", "Set-Location C:\\IA-GameDev\\projects\\project-asteria\nTest-Path .\\project.godot",
            "le premier exemple montre une extraction imbriquée ; le second vérifie la racine exacte attendue par Godot.",
        ),
        case(
            "28.2", "L’éditeur utilise une autre version",
            "un double-clic ouvre le projet avec l’association Windows, qui peut viser une version non approuvée.",
            "text", "Double-cliquer sur project.godot sans vérifier l’exécutable associé.",
            "lancer explicitement l’exécutable de référence et contrôler sa version.",
            "[PS] PowerShell 7 — Exemple corrigé avec l’exécutable approuvé.",
            "powershell", "$env:GODOT_EXE = 'C:\\IA-GameDev\\apps\\godot\\4.7.1-standard\\Godot_v4.7.1-stable_win64.exe'\n& $env:GODOT_EXE --version\n& $env:GODOT_EXE --editor --path .",
            "le lancement explicite rend la version reproductible, alors que l’association de fichiers reste implicite.",
        ),
        case(
            "28.3", "Écran vide au lancement",
            "la scène principale ne contient aucune caméra active ou la caméra ne regarde pas le marqueur.",
            "text", "Main\n└── Marker",
            "utiliser une scène minimale qui contient une caméra active, une lumière et le marqueur visible.",
            "[LECTURE] Structure corrigée à reproduire dans Godot.",
            "text", "Main\n├── Camera3D (Current = On)\n├── DirectionalLight3D\n└── Marker",
            "la scène corrigée fournit les éléments indispensables au rendu ; la scène fautive ne définit aucun point de vue.",
        ),
        case(
            "28.4", "La scène courante fonctionne, mais pas le projet",
            "`F6` valide une scène isolée alors que `F5` lance une autre scène principale ou aucune scène.",
            "text", "F6 → res://scenes/learning/bootstrap_test.tscn\nF5 → scène principale absente",
            "définir `main.tscn` comme scène principale et vérifier aussi le lancement du projet.",
            "[APP] Godot — Exemple corrigé dans Project > Project Settings > Run.",
            "text", "Main Scene = res://src/features/bootstrap/main.tscn\nF5 → main.tscn",
            "le test corrigé valide le vrai point d’entrée du jeu, pas seulement une scène ouverte dans l’éditeur.",
        ),
        case(
            "28.5", "Le script ne trouve pas `Marker`",
            "le chemin suppose un enfant direct alors que le nœud a été renommé ou déplacé.",
            "gdscript", "@onready var marker: MeshInstance3D = $Marker",
            "aligner l’arbre et le chemin, ou rendre la dépendance explicite avec un nœud exporté.",
            "[VSC] Visual Studio Code — Exemple corrigé avec une dépendance assignée dans l’Inspector.",
            "gdscript", "@export_node_path('MeshInstance3D') var marker_path: NodePath\n@onready var marker := get_node(marker_path) as MeshInstance3D",
            "le chemin fautif est caché dans le script ; la version corrigée expose le chemin et permet sa vérification dans l’Inspector.",
        ),
        case(
            "28.6", "Le rendu Forward+ ne démarre pas",
            "le projet est relancé sans journal et plusieurs paramètres sont modifiés simultanément.",
            "text", "Changer le pilote, le renderer et la scène en même temps, puis relancer sans --verbose.",
            "isoler le moteur de rendu avec un journal, puis tester un seul profil de secours à la fois.",
            "[PS] PowerShell 7 — Exemple corrigé de diagnostic contrôlé.",
            "powershell", "& $env:GODOT_EXE --verbose --editor --path . --rendering-method mobile --log-file .\\logs\\mobile-test.log",
            "le diagnostic corrigé conserve une trace et ne change qu’une variable, ce qui permet d’identifier la couche fautive.",
        ),
        case(
            "28.7", "Git suit `.godot/`",
            "le cache a été ajouté à l’index avant la création ou la correction de `.gitignore`.",
            "powershell", "git add .\ngit commit -m 'chore: add every generated file'",
            "ignorer le dossier et le retirer seulement de l’index Git, sans supprimer le cache local.",
            "[PS] PowerShell 7 — Exemple corrigé depuis la racine du projet.",
            "powershell", "Add-Content .gitignore '/.godot/'\ngit rm -r --cached .godot\ngit add .gitignore\ngit commit -m 'chore(git): stop tracking Godot cache'",
            "`--cached` cesse le suivi tout en conservant les fichiers sur le poste ; l’exemple fautif versionne des données régénérables.",
        ),
        case(
            "28.8", "Déplacement de fichier cassant une scène",
            "une scène ou Resource est déplacée dans l’Explorateur Windows sans mise à jour des références Godot.",
            "text", "Explorateur Windows : déplacer status_beacon.tscn vers un autre dossier pendant que Godot est fermé.",
            "effectuer le déplacement depuis le dock FileSystem, puis rechercher les anciens chemins et relancer l’import.",
            "[APP] Godot — Exemple corrigé à exécuter depuis le dock FileSystem.",
            "text", "FileSystem : Move To…\nPuis vérifier Output, les scènes dépendantes et git diff.",
            "Godot peut mettre à jour les références connues lors du déplacement corrigé ; l’Explorateur ne connaît pas ces dépendances.",
        ),
    ],
)
replace_section(
    "Livre-II/CHAPITRE-01-Decouvrir-Godot-et-creer-le-projet-fil-rouge.md",
    "## 28. Erreurs fréquentes",
    "## 29. Diagnostic par couches",
    ch1,
)

ch2 = section(
    "## 35. Erreurs fréquentes",
    "Le titre reste volontairement court. La règle s’applique à son contenu : chaque erreur possède une faute, une correction et une comparaison.",
    [
        case("35.1", "Confondre `=` et `==`", "une affectation est écrite à la place d’une comparaison dans une condition.", "gdscript", "if health = 0:\n\tqueue_free()", "utiliser `==` pour comparer et réserver `=` à l’affectation.", "[VSC] Visual Studio Code — Exemple corrigé dans une condition.", "gdscript", "if health == 0:\n\tqueue_free()", "`=` change une variable ; `==` produit un booléen utilisé par `if`."),
        case("35.2", "Mauvaise indentation", "une ligne destinée à la fonction se retrouve hors de son bloc ou au mauvais niveau.", "gdscript", "func can_act() -> bool:\nif stunned:\n\treturn false\nreturn true", "indenter chaque bloc avec les tabulations configurées par le projet.", "[VSC] Visual Studio Code — Exemple corrigé avec des blocs cohérents.", "gdscript", "func can_act() -> bool:\n\tif stunned:\n\t\treturn false\n\treturn true", "l’indentation corrigée détermine clairement quelles instructions appartiennent à la fonction et à la condition."),
        case("35.3", "Type trop vague", "une variable sans type accepte n’importe quelle valeur et reporte les erreurs à l’exécution.", "gdscript", "var data\ndata = 42\ndata = {'name': 'Aster'}", "déclarer le contrat réel ou créer une classe métier dédiée.", "[VSC] Visual Studio Code — Exemple corrigé avec un dictionnaire typé.", "gdscript", "var data: Dictionary[StringName, Variant] = {\n\t&'name': 'Aster',\n}", "la version corrigée limite la forme générale et permet à l’éditeur de détecter des usages incompatibles."),
        case("35.4", "Dépendance cachée à un nœud", "le script cherche un chemin absolu appartenant à une scène extérieure.", "gdscript", "var player := get_node('/root/Main/World/Player')", "recevoir la dépendance depuis la scène ou le point de composition.", "[VSC] Visual Studio Code — Exemple corrigé par configuration explicite.", "gdscript", "var _player: Node3D\n\nfunc configure(player: Node3D) -> void:\n\t_player = player", "la dépendance corrigée apparaît dans l’interface du composant et peut être remplacée dans une scène de test."),
        case("35.5", "Travail lourd dans `_process()`", "un fichier ou une Resource est chargé à chaque image.", "gdscript", "func _process(_delta: float) -> void:\n\tvar profile := load('res://data/profile.tres')", "charger une fois à l’initialisation ou utiliser un cache explicite.", "[VSC] Visual Studio Code — Exemple corrigé avec préchargement fixe.", "gdscript", "const PROFILE := preload('res://data/profile.tres')\n\nfunc _process(_delta: float) -> void:\n\tuse_profile(PROFILE)", "le chargement corrigé est réalisé une fois ; la boucle d’image ne répète plus une opération d’E/S ou de résolution."),
        case("35.6", "Utiliser `Variant` partout", "les paramètres et retours internes n’expriment plus aucun contrat.", "gdscript", "func add_score(value: Variant) -> Variant:\n\treturn value + 1", "conserver `Variant` aux frontières dynamiques et typer le cœur métier.", "[VSC] Visual Studio Code — Exemple corrigé avec un contrat numérique.", "gdscript", "func add_score(value: int) -> int:\n\treturn value + 1", "la fonction corrigée refuse immédiatement une chaîne ou un nœud au lieu de produire une erreur tardive."),
        case("35.7", "Modifier un tableau partagé sans le savoir", "deux variables référencent le même tableau et une modification affecte les deux.", "gdscript", "var copy := original\ncopy.append('nouveau')", "dupliquer la collection lorsqu’une copie indépendante est nécessaire.", "[VSC] Visual Studio Code — Exemple corrigé avec duplication explicite.", "gdscript", "var copy: Array[String] = original.duplicate()\ncopy.append('nouveau')", "l’affectation fautive partage la référence ; `duplicate()` crée un conteneur séparé."),
        case("35.8", "Masquer tous les avertissements", "une annotation globale désactive un contrôle sans corriger sa cause.", "gdscript", "@warning_ignore('unused_parameter')\nfunc _process(delta: float) -> void:\n\tpass", "exprimer l’intention locale, par exemple avec un nom de paramètre commençant par `_`.", "[VSC] Visual Studio Code — Exemple corrigé sans suppression globale.", "gdscript", "func _process(_delta: float) -> void:\n\tpass", "le nom `_delta` indique que le paramètre imposé par Godot est volontairement inutilisé ; le reste des avertissements demeure actif."),
        case("35.9", "Utiliser `@tool` trop tôt", "un script d’éditeur modifie une Resource dès son chargement, y compris pendant la conception.", "gdscript", "@tool\nextends Node\n\nfunc _process(_delta: float) -> void:\n\tprofile.cooldown_seconds -= 1.0", "rester en runtime normal ou protéger explicitement les effets d’éditeur.", "[VSC] Visual Studio Code — Exemple corrigé avec garde d’éditeur.", "gdscript", "@tool\nextends Node\n\nfunc refresh_preview() -> void:\n\tif not Engine.is_editor_hint():\n\t\treturn\n\tupdate_preview_without_saving_source_data()", "la version corrigée limite l’exécution à une action de prévisualisation et évite de muter silencieusement les données sources."),
    ],
)
replace_section("Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md", "## 35. Erreurs fréquentes", "## 36. Principes de conception retenus", ch2)

ch3 = section(
    "## 21. Erreurs fréquentes et diagnostics",
    "Le diagnostic reste associé à une correction concrète. Les exemples utilisent les contrats introduits dans le chapitre.",
    [
        case("21.1", "`Node not found`", "un chemin exige un enfant qui n’existe pas à cet emplacement.", "gdscript", "@onready var label: Label = $Panel/StatusLabel", "rendre le chemin cohérent avec la scène ou traiter explicitement une dépendance optionnelle.", "[VSC] Visual Studio Code — Exemple corrigé avec contrôle nullable.", "gdscript", "@onready var label := get_node_or_null('Panel/StatusLabel') as Label\n\nfunc _ready() -> void:\n\tif label == null:\n\t\tpush_error('StatusLabel est absent.')", "`$...` échoue immédiatement ; `get_node_or_null()` permet de produire un diagnostic adapté avant l’usage."),
        case("21.2", "`Invalid access to property` sur `null`", "le résultat d’un cast est utilisé sans vérifier qu’il a réussi.", "gdscript", "var beacon := node as StatusBeacon\nbeacon.activate(&'player')", "tester la référence avant d’accéder à ses propriétés ou méthodes.", "[VSC] Visual Studio Code — Exemple corrigé après le cast.", "gdscript", "var beacon := node as StatusBeacon\nif beacon == null:\n\tpush_error('La racine instanciée doit être un StatusBeacon.')\n\treturn\nbeacon.activate(&'player')", "la version corrigée traite le résultat nullable du cast et rapproche l’erreur de sa cause."),
        case("21.3", "Signal connecté deux fois", "la même connexion est créée à chaque réactivation de la scène.", "gdscript", "func enable() -> void:\n\tbeacon.activated.connect(_on_beacon_activated)", "vérifier la connexion avant de l’ajouter.", "[VSC] Visual Studio Code — Exemple corrigé idempotent.", "gdscript", "func enable() -> void:\n\tif not beacon.activated.is_connected(_on_beacon_activated):\n\t\tbeacon.activated.connect(_on_beacon_activated)", "le second appel corrigé ne crée pas une nouvelle liaison et ne duplique pas le callback."),
        case("21.4", "Signal émis avant la connexion", "l’action est lancée avant que l’abonné soit enregistré.", "gdscript", "beacon.activate(&'player')\nbeacon.activated.connect(_on_beacon_activated)", "connecter d’abord, puis déclencher l’action.", "[VSC] Visual Studio Code — Exemple corrigé dans l’ordre observable.", "gdscript", "beacon.activated.connect(_on_beacon_activated)\nbeacon.activate(&'player')", "un signal ne conserve pas l’historique ; seul l’ordre corrigé permet au récepteur d’observer cette émission."),
        case("21.5", "Signature incompatible", "le callback ne reçoit pas le même nombre de paramètres que le signal.", "gdscript", "signal activated(beacon_id: StringName, message: String)\n\nfunc _on_activated(beacon_id: StringName) -> void:\n\tprint(beacon_id)", "aligner la signature du callback sur la déclaration du signal.", "[VSC] Visual Studio Code — Exemple corrigé avec les deux paramètres.", "gdscript", "func _on_activated(beacon_id: StringName, message: String) -> void:\n\tprint('%s : %s' % [beacon_id, message])", "la version corrigée accepte exactement les valeurs envoyées par `emit()`."),
        case("21.6", "Resource partagée modifiée par erreur", "le cooldown courant est écrit dans la définition partagée.", "gdscript", "profile.cooldown_seconds -= delta", "conserver la configuration dans la Resource et l’état courant dans le nœud.", "[VSC] Visual Studio Code — Exemple corrigé avec une variable runtime.", "gdscript", "_remaining_cooldown = maxf(_remaining_cooldown - delta, 0.0)", "la Resource reste identique pour toutes les instances ; seule la variable propre au nœud évolue."),
        case("21.7", "Mauvaise scène exécutée", "`F6` lance l’onglet courant alors que le test attendu concerne la scène principale.", "text", "Onglet actif : status_beacon.tscn\nF6 → seule la balise est exécutée",
             "lancer explicitement la scène de démonstration ou utiliser `F5` pour la scène principale.", "[PS] PowerShell 7 — Exemple corrigé avec une cible explicite.", "powershell", "godot --headless --path . --scene 'res://scenes/learning/ch03_scene_signals_demo.tscn' --quit-after 180", "la commande corrigée nomme la scène testée et rend le résultat reproductible."),
        case("21.8", "Nœud ajouté mais absent après enregistrement", "un outil d’éditeur ajoute un enfant sans propriétaire de scène.", "gdscript", "var marker := Marker3D.new()\nscene_root.add_child(marker)\nResourceSaver.save(packed_scene, path)", "dans un outil d’éditeur, définir `owner` vers la racine enregistrée avant le conditionnement de la scène.", "[VSC] Visual Studio Code — Exemple corrigé réservé à un outil d’éditeur.", "gdscript", "var marker := Marker3D.new()\nscene_root.add_child(marker)\nmarker.owner = scene_root\nResourceSaver.save(packed_scene, path)", "`add_child()` suffit au runtime, mais `owner` indique au sérialiseur que l’enfant appartient à la scène enregistrée."),
    ],
)
replace_section("Livre-II/CHAPITRE-03-Scenes-noeuds-Resources-et-signaux.md", "## 21. Erreurs fréquentes et diagnostics", "## 22. Validation dans Godot", ch3)

ch4_antipatterns = section(
    "## 14. Éviter les anti-patterns",
    "Cette section est soumise à la même règle que les sections nommées « Erreurs fréquentes » : le titre diffère, mais la fonction pédagogique est identique.",
    [
        case("14.1", "Le dossier `managers/`", "un `GameManager` accumule des responsabilités sans frontière.", "gdscript", "class_name GameManager\nextends Node\n\nfunc save_game(): pass\nfunc play_music(): pass\nfunc complete_quest(): pass", "nommer et placer chaque capacité selon sa responsabilité réelle.", "[LECTURE] Exemple corrigé d’organisation — Ne pas créer tous les fichiers sans besoin.", "text", "features/quests/application/quest_service.gd\nfeatures/audio/presentation/voice_playback_manager.gd\nfeatures/saves/application/save_service.gd", "la structure corrigée révèle les propriétaires et évite un objet central qui change pour toutes les fonctionnalités."),
        case("14.2", "Le singleton omniprésent", "un module accède directement à un Autoload pour toutes ses dépendances.", "gdscript", "func buy(item_id: StringName) -> void:\n\tGlobal.inventory.remove_currency(10)\n\tGlobal.audio.play('buy')", "injecter seulement les contrats nécessaires depuis le point de composition.", "[VSC] Visual Studio Code — Exemple corrigé avec dépendance explicite.", "gdscript", "var _wallet: WalletService\n\nfunc configure(wallet: WalletService) -> void:\n\t_wallet = wallet", "le module corrigé déclare ce dont il dépend et peut recevoir un remplacement de test."),
        case("14.3", "La scène monolithique", "le script racine manipule directement des branches indépendantes.", "gdscript", "func _ready() -> void:\n\t$Player.setup()\n\t$Inventory.load_items()\n\t$Quests.start_all()\n\t$Weather.update_world()", "extraire des sous-scènes cohérentes et les assembler depuis un point d’entrée.", "[LECTURE] Structure corrigée de composition — Ne pas saisir.", "text", "Main\n├── PlayerFeature\n├── InventoryFeature\n├── QuestFeature\n└── WorldSimulation", "la scène corrigée conserve des interfaces de composants plutôt qu’un accès direct à tous leurs enfants internes."),
        case("14.4", "Le dossier `shared/` sans règle", "une classe spécifique à une fonctionnalité est placée dans un espace partagé par commodité.", "text", "src/shared/beacon_cooldown_calculator.gd",
             "laisser le code dans son module tant qu’un second usage réellement générique n’existe pas.", "[LECTURE] Chemin corrigé selon le propriétaire fonctionnel — Ne pas saisir.", "text", "src/features/beacons/domain/beacon_cooldown_calculator.gd", "le chemin corrigé indique le vocabulaire et le propriétaire ; un déplacement vers `core` exigera plus tard un contrat réellement transversal."),
        case("14.5", "Les couches qui se contournent", "la présentation ouvre directement une base ou un fichier d’infrastructure.", "gdscript", "func _on_refresh_pressed() -> void:\n\tvar db := SQLite.new()\n\tresult_label.text = str(db.query('SELECT * FROM quests'))", "la présentation demande une action à un service ou contrôleur d’application.", "[VSC] Visual Studio Code — Exemple corrigé avec une dépendance d’application.", "gdscript", "func _on_refresh_pressed() -> void:\n\tvar quests := _quest_query_service.list_active_quests()\n\t_render_quests(quests)", "l’interface corrigée ne connaît ni SQLite ni le format de stockage et peut fonctionner avec une autre implémentation."),
        case("14.6", "L’architecture spéculative", "des interfaces, fabriques et dossiers vides sont créés avant tout besoin concret.", "text", "src/features/future_system/\n├── factories/\n├── interfaces/\n├── adapters/\n└── implementations/",
             "commencer par la responsabilité actuelle et extraire une abstraction lorsqu’une variation observée la justifie.", "[LECTURE] Structure corrigée minimale — Ne pas saisir.", "text", "src/features/beacons/\n├── domain/\n├── presentation/\n└── README.md", "la structure corrigée correspond à des fichiers et frontières existants ; l’exemple fautif anticipe des besoins inconnus."),
    ],
)
replace_section("Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md", "## 14. Éviter les anti-patterns", "## 15. Architecture Decision Records", ch4_antipatterns)

ch4_errors = section(
    "## 22. Erreurs fréquentes et diagnostics",
    "Ces diagnostics portent sur le placement et les dépendances. Chaque correction montre une différence architecturale observable.",
    [
        case("22.1", "« Je ne sais pas où mettre ce fichier »", "un fichier spécifique aux balises est placé dans `core` parce que ce dossier semble central.", "text", "src/core/beacon_profile.gd", "identifier d’abord le vocabulaire et le propriétaire fonctionnel.", "[LECTURE] Chemin corrigé — Ne pas saisir.", "text", "src/features/beacons/domain/beacon_profile.gd", "le chemin corrigé limite la dépendance au module qui possède ce concept ; `core` reste indépendant des fonctionnalités."),
        case("22.2", "Dépendance circulaire", "deux modules chargent mutuellement leurs classes concrètes.", "text", "inventory → quests/quest_reward.gd\nquests → inventory/inventory_service.gd", "extraire un contrat stable ou déplacer l’orchestration dans `src/app`.", "[LECTURE] Dépendances corrigées — Ne pas saisir.", "text", "inventory → core/contracts/item_grant.gd\nquests → core/contracts/item_grant.gd\napp → assemble quests + inventory", "les modules corrigés convergent vers un contrat et ne se connaissent plus directement."),
        case("22.3", "Trop de petits fichiers", "une opération privée triviale devient une classe sans état ni réutilisation.", "gdscript", "class_name AddOne\nextends RefCounted\n\nfunc run(value: int) -> int:\n\treturn value + 1", "conserver la fonction privée dans la classe qui porte la responsabilité.", "[VSC] Visual Studio Code — Exemple corrigé dans le service concerné.", "gdscript", "func _increment_activation_count() -> void:\n\t_activation_count += 1", "la version corrigée réduit la navigation et garde ensemble ce qui change pour la même raison."),
        case("22.4", "Module trop gros", "un module `characters` contient apparence, locomotion, relations et sauvegarde avec un seul propriétaire.", "text", "features/characters/character_everything.gd", "séparer seulement les capacités qui possèdent des vocabulaires et cycles de vie indépendants.", "[LECTURE] Organisation corrigée lorsque le besoin est réel — Ne pas saisir.", "text", "features/characters/appearance/\nfeatures/characters/locomotion/\nfeatures/relationships/", "la séparation corrigée suit des responsabilités évoluant indépendamment au lieu d’un découpage arbitraire par taille."),
        case("22.5", "`core` dépend d’une fonctionnalité", "un utilitaire central importe un type `BeaconProfile`.", "gdscript", "# res://src/core/validation.gd\nfunc validate(profile: BeaconProfile) -> bool:\n\treturn not profile.id.is_empty()", "déplacer la règle dans le module ou reformuler un contrat réellement générique.", "[VSC] Visual Studio Code — Exemple corrigé dans le domaine des balises.", "gdscript", "# res://src/features/beacons/domain/beacon_profile.gd\nfunc validate() -> PackedStringArray:\n\tvar errors := PackedStringArray()\n\tif id.is_empty():\n\t\terrors.append('id est obligatoire')\n\treturn errors", "`core` ne connaît plus la fonctionnalité ; l’invariant reste auprès du modèle qui le définit."),
        case("22.6", "Documentation et code divergent", "un module est déplacé sans mettre à jour sa matrice ni son README.", "text", "Commit : déplacer beacons vers src/features/status/\nDocumentation : conserve src/features/beacons/", "modifier code, chemins et sources d’architecture dans la même pull request.", "[LECTURE] Lot corrigé — Ne pas saisir.", "text", "PR unique :\n- fichiers déplacés\n- README du module\n- dependency-matrix.md\n- ADR si la décision change\n- tests et scènes corrigés", "le lot corrigé maintient une seule source de vérité vérifiable ; le lot fautif laisse des instructions obsolètes."),
    ],
)
replace_section("Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md", "## 22. Erreurs fréquentes et diagnostics", "## 23. Checklist de fin de chapitre", ch4_errors)

ch5 = section(
    "## 15. Anti-patterns et corrections",
    "Le titre « Anti-patterns » désigne ici des erreurs de conception récurrentes. Chaque cas possède donc les mêmes preuves pédagogiques qu’une section « Erreurs fréquentes ».",
    [
        case("15.1", "Un Autoload par service", "chaque capacité devient globale et son ordre dépend de la liste Project Settings.", "text", "Autoloads :\n- AudioService\n- SaveService\n- QuestService\n- BeaconService\n- InventoryService", "conserver un composition root persistant et construire les services ordinaires sous son contrôle.", "[LECTURE] Organisation corrigée — Ne pas saisir.", "text", "Autoload : AppRuntime\nAppRuntime crée :\n- GameEventBus\n- BeaconActivationService\n- autres services nécessaires", "la version corrigée limite le point global et rend le cycle de vie des services explicite."),
        case("15.2", "Le registre injecté partout", "un objet métier recherche lui-même sa dépendance dans le registre.", "gdscript", "func activate() -> void:\n\tvar bus := registry.require_service(&'event_bus')\n\tbus.beacon_activated.emit(id)", "résoudre la dépendance dans le bootstrap puis injecter le type attendu.", "[VSC] Visual Studio Code — Exemple corrigé par constructeur.", "gdscript", "var _events: GameEventBus\n\nfunc _init(events: GameEventBus) -> void:\n\t_events = events", "la dépendance corrigée est visible et typée ; le registre reste un outil du point de composition."),
        case("15.3", "Un bus générique à dictionnaires", "un seul signal transporte un nom libre et un payload sans schéma.", "gdscript", "signal event_published(name: String, payload: Dictionary)\n\nevent_published.emit('becon_actvated', {'id': 42})", "déclarer des signaux nommés avec des paramètres typés.", "[VSC] Visual Studio Code — Exemple corrigé dans `GameEventBus`.", "gdscript", "signal beacon_activated(beacon_id: StringName)\n\nbeacon_activated.emit(&'beacon.training')", "le moteur peut vérifier le nom du signal et la forme de ses arguments ; la faute de frappe du bus générique reste invisible."),
        case("15.4", "Des événements pour chaque appel local", "un enfant demande à son parent une action simple par le bus global.", "gdscript", "_events.event_published.emit('label_text_requested', {'text': message})", "utiliser un appel direct ou un signal local lorsque les composants appartiennent à la même scène.", "[VSC] Visual Studio Code — Exemple corrigé dans la présentation locale.", "gdscript", "result_label.text = message", "la correction conserve un flux direct et traçable ; le bus reste réservé aux frontières transversales."),
        case("15.5", "Un service qui connaît l’interface graphique", "le service cherche et modifie un `Label`.", "gdscript", "func request_activation(id: StringName) -> void:\n\tget_node('/root/Main/UI/ResultLabel').text = 'Activation demandée'", "retourner une valeur ou émettre un événement que la présentation traduit en affichage.", "[VSC] Visual Studio Code — Exemple corrigé avec retour métier.", "gdscript", "func request_activation(id: StringName) -> bool:\n\tif id.is_empty():\n\t\treturn false\n\t_events.beacon_activation_requested.emit(id)\n\treturn true", "le service corrigé ne dépend plus de l’arbre d’interface et peut être testé sans scène graphique."),
        case("15.6", "Un démarrage non idempotent", "chaque appel recrée le bus et reconnecte les signaux.", "gdscript", "func start_application() -> void:\n\t_events = GameEventBus.new()\n\tadd_child(_events)", "refuser un second démarrage ou retourner l’état existant.", "[VSC] Visual Studio Code — Exemple corrigé avec garde.", "gdscript", "func start_application() -> Error:\n\tif _started:\n\t\treturn ERR_ALREADY_IN_USE\n\t_started = true\n\treturn OK", "la garde rend le cycle de vie déterministe et empêche les doublons de nœuds ou de connexions."),
        case("15.7", "Un arrêt dans le mauvais ordre", "le bus est supprimé avant les services susceptibles d’émettre pendant leur arrêt.", "gdscript", "func stop_application() -> void:\n\t_events.queue_free()\n\t_beacon_activation.stop()", "arrêter les consommateurs avant leurs dépendances.", "[VSC] Visual Studio Code — Exemple corrigé dans l’ordre inverse du démarrage.", "gdscript", "func stop_application() -> void:\n\t_beacon_activation.stop()\n\t_beacon_activation = null\n\t_events.queue_free()\n\t_events = null", "le service termine alors que le bus existe encore ; la version fautive peut émettre vers un objet déjà libéré."),
    ],
)
replace_section("Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md", "## 15. Anti-patterns et corrections", "## 16. Parcours Solo", ch5)

ch6 = section(
    "## 22. Anti-patterns et corrections",
    "La section 21.3 reste un index de symptômes. Les cas ci-dessous constituent les explications détaillées exigées par la règle pédagogique.",
    [
        case("22.1", "Touches codées en dur", "le gameplay dépend directement d’une touche physique et ne peut pas être remappé.", "gdscript", "if event is InputEventKey and event.keycode == KEY_E:\n\ttry_interact()", "interroger une action logique définie dans l’Input Map.", "[VSC] Visual Studio Code — Exemple corrigé dans `_unhandled_input()`.", "gdscript", "if event.is_action_pressed(&'interact'):\n\ttry_interact()", "l’action corrigée peut recevoir plusieurs touches ou boutons et être remappée sans modifier le gameplay."),
        case("22.2", "Déplacement dans `_input()`", "la position change une fois par événement reçu, donc selon le périphérique et sa fréquence.", "gdscript", "func _input(event: InputEvent) -> void:\n\tif event.is_action(&'move_forward'):\n\t\tposition.z -= speed", "lire l’intention puis appliquer le mouvement pendant le pas physique.", "[VSC] Visual Studio Code — Exemple corrigé avec séparation des responsabilités.", "gdscript", "func _physics_process(delta: float) -> void:\n\tvar frame := input_reader.sample(delta)\n\tmotor.apply_input(frame, delta)", "la version corrigée produit une vitesse stable à chaque tick physique au lieu de dépendre du nombre d’événements."),
        case("22.3", "Multiplier `velocity` par `delta`", "la vitesse finale est transformée en déplacement avant `move_and_slide()`.", "gdscript", "velocity = direction * speed * delta\nmove_and_slide()", "conserver une vitesse en unités par seconde et multiplier seulement les accélérations par `delta`.", "[VSC] Visual Studio Code — Exemple corrigé pour `CharacterBody3D`.", "gdscript", "velocity.x = direction.x * speed\nvelocity.z = direction.z * speed\nvelocity.y -= gravity * delta\nmove_and_slide()", "`move_and_slide()` utilise déjà le pas physique pour la vitesse ; seul le changement de vitesse dû à la gravité dépend ici de `delta`."),
        case("22.4", "Une classe qui lit les entrées et modifie tout", "un seul script interroge les touches, tourne la caméra, déplace le corps et déclenche les interactions.", "gdscript", "func _physics_process(delta: float) -> void:\n\tread_keyboard()\n\trotate_camera()\n\tmove_character(delta)\n\tcheck_interaction()\n\tupdate_ui()", "déléguer à des composants spécialisés reliés par un contrôleur.", "[VSC] Visual Studio Code — Exemple corrigé dans `PlayerController`.", "gdscript", "func _physics_process(delta: float) -> void:\n\tvar frame := input_reader.sample(delta)\n\tcamera_rig.apply_look(frame.look, delta)\n\tmotor.apply_input(frame, delta)\n\tinteractor.try_interact(frame.interact_pressed)", "le contrôleur corrigé orchestre des contrats séparés ; chaque composant peut évoluer et être testé indépendamment."),
        case("22.5", "Bus global pour une interaction locale", "une balise et son contrôleur de scène communiquent par un événement transversal.", "gdscript", "_events.event_published.emit('local_beacon_clicked', {'id': id})", "utiliser un signal direct ou un appel entre composants de la même fonctionnalité.", "[VSC] Visual Studio Code — Exemple corrigé avec signal local typé.", "gdscript", "interaction_target.accepted.connect(_on_beacon_interaction_accepted)", "la connexion corrigée rend l’émetteur et le récepteur visibles dans la scène ; le bus n’ajoute aucune valeur pour ce trajet local."),
        case("22.6", "Interaction par nom de méthode libre", "n’importe quel objet possédant une méthode du même nom est appelé sans contrat de signature.", "gdscript", "if collider.has_method('interact'):\n\tcollider.call('interact', player)", "utiliser un composant ou une classe typée représentant une cible interactive.", "[VSC] Visual Studio Code — Exemple corrigé avec cast.", "gdscript", "var target := collider as InteractionTarget\nif target != null:\n\ttarget.interact(player)", "le cast corrigé vérifie le type attendu et l’éditeur connaît la méthode publique et ses paramètres."),
        case("22.7", "Caméra enfant directe du personnage sans pivot", "le même transform mélange rotation horizontale, verticale et déplacement du corps.", "text", "PlayerCharacter\n└── Camera3D", "séparer le lacet, le tangage et l’évitement d’obstacles dans un rig.", "[LECTURE] Arbre corrigé de caméra — Ne pas saisir.", "text", "PlayerCharacter\n└── CameraYaw\n    └── CameraPitch\n        └── SpringArm3D\n            └── Camera3D", "chaque nœud corrigé porte un axe ou une responsabilité, ce qui permet de limiter le tangage sans incliner le personnage."),
        case("22.8", "Remappage destructif sans voie de secours", "les événements existants sont effacés avant de vérifier la nouvelle liste.", "gdscript", "InputMap.action_erase_events(action)\nfor event in events:\n\tInputMap.action_add_event(action, event)", "valider l’action et conserver au moins une liaison avant toute suppression.", "[VSC] Visual Studio Code — Exemple corrigé avec garde préalable.", "gdscript", "if not InputMap.has_action(action) or events.is_empty():\n\treturn false\n\nInputMap.action_erase_events(action)\nfor event: InputEvent in events:\n\tInputMap.action_add_event(action, event)\nreturn true", "la version corrigée ne détruit jamais la dernière commande lorsque la proposition est vide ou l’action inconnue."),
    ],
)
replace_section("Livre-II/CHAPITRE-06-Entrees-controleurs-cameras-et-interactions.md", "## 22. Anti-patterns et corrections", "## 23. Parcours Solo", ch6)

# Transformer le tableau de symptômes du chapitre 6 en index explicitement relié à la section détaillée.
replace_once(
    "Livre-II/CHAPITRE-06-Entrees-controleurs-cameras-et-interactions.md",
    "### 21.3 Symptômes fréquents\n\n| Symptôme | Cause probable | Vérification |",
    "### 21.3 Symptômes fréquents\n\n<!-- qa:error-correction-index -->\n\nCe tableau constitue un index de diagnostic rapide. Les exemples fautifs et corrigés détaillés se trouvent dans la section 22 ; les lignes propres au confort de caméra, aux couches physiques ou au matériel renvoient aussi aux sections techniques correspondantes du chapitre.\n\n| Symptôme | Cause probable | Vérification |",
)

# Marquer la section déjà conforme du chapitre 7.
replace_once(
    "Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md",
    "## 35. Erreurs fréquentes et corrections\n\nChaque erreur ci-dessous",
    "## 35. Erreurs fréquentes et corrections\n\n<!-- qa:error-correction-section -->\n\nChaque erreur ci-dessous",
)

versions = {
    "Livre-II/CHAPITRE-01-Decouvrir-Godot-et-creer-le-projet-fil-rouge.md": ("version: \"1.2.0\"", "version: \"1.3.0\""),
    "Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md": ("version: \"1.3.0\"", "version: \"1.4.0\""),
    "Livre-II/CHAPITRE-03-Scenes-noeuds-Resources-et-signaux.md": ("version: \"1.0.0\"", "version: \"1.1.0\""),
    "Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md": ("version: \"1.0.0\"", "version: \"1.1.0\""),
    "Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md": ("version: \"1.0.0\"", "version: \"1.1.0\""),
    "Livre-II/CHAPITRE-06-Entrees-controleurs-cameras-et-interactions.md": ("version: \"1.0.0\"", "version: \"1.1.0\""),
    "Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md": ("version: \"1.1.0\"", "version: \"1.1.1\""),
}
for path, (old, new) in versions.items():
    replace_once(path, old, new)
    add_supplemental_audit(path)

# Renforcer le protocole QA.
protocol = ROOT / "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
text = protocol.read_text(encoding="utf-8")
text = text.replace('version: "1.4.0"', 'version: "1.5.0"', 1)
needle = "- [ ] Une checklist et un critère d’acceptation sont fournis.\n"
addition = '''- [ ] Une checklist et un critère d’acceptation sont fournis.
- [ ] Toute section qui enseigne des erreurs, anti-patterns, pièges ou corrections fournit un exemple fautif, un exemple corrigé et leur différence pour chaque cas.

#### Q1.1 — Règle sémantique des erreurs et corrections

La règle dépend de la fonction pédagogique, jamais du titre exact. Elle couvre notamment les sections nommées :

- `Erreurs fréquentes` ;
- `Erreurs fréquentes et diagnostics` ;
- `Anti-patterns et corrections` ;
- `Éviter les anti-patterns` ;
- `Pièges`, `Mauvaises pratiques` ou toute formulation équivalente.

Une section détaillée porte le marqueur invisible suivant :

> **[LECTURE] Marqueur QA — Ne pas saisir dans un terminal.**

```html
<!-- qa:error-correction-section -->
```

Chaque sous-cas doit alors contenir :

1. un symptôme ou risque ;
2. un **exemple fautif** ;
3. une **correction** ;
4. un **exemple corrigé** ;
5. une explication explicite de la différence.

Un tableau servant uniquement d’index de diagnostic peut rester compact s’il porte `<!-- qa:error-correction-index -->` et renvoie clairement vers une section détaillée conforme. Il ne peut pas remplacer les exemples détaillés.
'''
if needle not in text:
    raise RuntimeError("Point Q1 introuvable dans le protocole")
text = text.replace(needle, addition, 1)
protocol.write_text(text, encoding="utf-8")

# Renforcer le validateur léger avec les marqueurs sémantiques.
validator = ROOT / "tools/validate_chapters.py"
text = validator.read_text(encoding="utf-8")
constant_needle = 'VALID_REASONING = {"GPT-5.6 Sol — Moyenne", "GPT-5.6 Sol — Élevée"}\n'
constant_add = constant_needle + 'ERROR_SECTION_MARKER = "<!-- qa:error-correction-section -->"\nERROR_INDEX_MARKER = "<!-- qa:error-correction-index -->"\nERROR_HEADING_RE = re.compile(r"(?:erreurs? fréquentes|anti[- ]patterns?|symptômes fréquents|pièges fréquents)", re.IGNORECASE)\n'
if constant_needle not in text:
    raise RuntimeError("Constante VALID_REASONING introuvable")
text = text.replace(constant_needle, constant_add, 1)
function_anchor = '\n\ndef inspect_duplicates(text: str, rel: str) -> ChapterStats:\n'
new_function = r'''

def validate_error_correction_sections(text: str, rel: str, errors: list[str]) -> None:
    """Valide les sections pédagogiques d'erreurs indépendamment de leur titre."""
    lines = text.splitlines()
    headings: list[tuple[int, int, str]] = []
    for index, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if match:
            headings.append((index, len(match.group(1)), match.group(2).strip()))

    for position, (start, level, title) in enumerate(headings):
        if level < 2 or not ERROR_HEADING_RE.search(title):
            continue
        end = len(lines)
        for next_start, next_level, _ in headings[position + 1:]:
            if next_level <= level:
                end = next_start
                break
        body = "\n".join(lines[start + 1:end])
        has_detail = ERROR_SECTION_MARKER in body
        has_index = ERROR_INDEX_MARKER in body
        if not has_detail and not has_index:
            errors.append(
                f"Section d’erreurs non qualifiée dans {rel} : {title}. "
                "Ajouter un marqueur détaillé ou d’index."
            )
            continue
        if has_index:
            normalized = body.casefold()
            if "exemples" not in normalized or "section" not in normalized:
                errors.append(f"Index de diagnostic sans renvoi explicite dans {rel} : {title}")
            continue

        children = [
            (child_start, child_title)
            for child_start, child_level, child_title in headings[position + 1:]
            if child_start < end and child_level == level + 1
        ]
        if not children:
            errors.append(f"Section détaillée sans sous-cas dans {rel} : {title}")
            continue
        for child_index, (child_start, child_title) in enumerate(children):
            child_end = children[child_index + 1][0] if child_index + 1 < len(children) else end
            child_body = "\n".join(lines[child_start + 1:child_end])
            missing: list[str] = []
            if "Exemple fautif" not in child_body:
                missing.append("exemple fautif")
            if "Exemple corrigé" not in child_body:
                missing.append("exemple corrigé")
            if "**Différence :**" not in child_body:
                missing.append("explication de la différence")
            if missing:
                errors.append(
                    f"Cas pédagogique incomplet dans {rel} — {child_title} : "
                    + ", ".join(missing)
                )
'''
if function_anchor not in text:
    raise RuntimeError("Ancre inspect_duplicates introuvable")
text = text.replace(function_anchor, new_function + function_anchor, 1)
call_needle = "                chapter_stats = inspect_duplicates(text, rel)\n"
call_add = "                validate_error_correction_sections(text, rel, errors)\n" + call_needle
if call_needle not in text:
    raise RuntimeError("Appel inspect_duplicates introuvable")
text = text.replace(call_needle, call_add, 1)
validator.write_text(text, encoding="utf-8")

# Créer la preuve d'audit rétroactif.
audit_path = ROOT / "Livre-II/QA/AUDIT-RETROACTIF-EXEMPLES-ERREURS-CH01-CH06.md"
audit_path.write_text('''---
title: "Audit rétroactif — exemples d’erreurs et corrections, chapitres 1 à 6"
id: "DOC-L2-QA-ERROR-EXAMPLES-CH01-CH06"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
audit-date: "2026-07-19"
audit-level: "static-review"
pdf-built: false
---

# Audit rétroactif — exemples d’erreurs et corrections, chapitres 1 à 6

## 1. Décision

Les sections pédagogiques consacrées aux erreurs, anti-patterns et diagnostics des chapitres 1 à 6 ont été révisées selon une règle sémantique indépendante de leur titre.

**Décision : accepté au niveau `static-review`, sous réserve de la validation automatique légère.**

## 2. Sections contrôlées

| Chapitre | Section | Cas détaillés |
|---:|---|---:|
| 1 | `Erreurs fréquentes` | 8 |
| 2 | `Erreurs fréquentes` | 9 |
| 3 | `Erreurs fréquentes et diagnostics` | 8 |
| 4 | `Éviter les anti-patterns` | 6 |
| 4 | `Erreurs fréquentes et diagnostics` | 6 |
| 5 | `Anti-patterns et corrections` | 7 |
| 6 | `Anti-patterns et corrections` | 8 |

Total : **52 cas détaillés**.

Le tableau `Symptômes fréquents` du chapitre 6 est conservé comme index rapide et renvoie explicitement vers la section détaillée.

## 3. Critères appliqués

Chaque cas détaillé contient maintenant :

1. un symptôme ou risque ;
2. un bloc marqué `Exemple fautif` ;
3. une correction formulée ;
4. un bloc marqué `Exemple corrigé` ;
5. un paragraphe `Différence` expliquant le changement de comportement ou d’architecture.

Les exemples utilisent les repères `[LECTURE]`, `[VSC]`, `[PS]`, `[APP]` ou `[SORTIE]` adaptés à leur nature.

## 4. Règle de titre

Aucun renommage artificiel n’est imposé. Les formulations suivantes sont équivalentes lorsqu’elles enseignent des fautes et leurs remèdes :

- erreurs fréquentes ;
- erreurs et diagnostics ;
- anti-patterns ;
- pièges ;
- mauvaises pratiques ;
- symptômes accompagnés de corrections.

Le marqueur `<!-- qa:error-correction-section -->` qualifie une section détaillée. Le marqueur `<!-- qa:error-correction-index -->` qualifie un index compact renvoyant vers les exemples.

## 5. Automatisation

`tools/validate_chapters.py` vérifie désormais :

- qu’une section reconnue possède un marqueur sémantique ;
- qu’une section détaillée possède des sous-cas ;
- que chaque sous-cas contient les deux exemples et l’explication de différence ;
- qu’un index compact renvoie vers des exemples détaillés.

## 6. Réserves

- les exemples restent audités statiquement ;
- les fichiers du Starter Kit ne sont pas encore matérialisés ;
- aucun PDF intermédiaire n’est construit ;
- les comportements seront qualifiés `runtime-tested` après exécution réelle.
''', encoding="utf-8")

# Index et ordre de compilation.
contents = ROOT / "contents.txt"
text = contents.read_text(encoding="utf-8")
needle = "Livre-II/QA/AUDIT-CHAPITRE-07.md\n"
if "AUDIT-RETROACTIF-EXEMPLES-ERREURS-CH01-CH06.md" not in text:
    text = text.replace(needle, needle + "Livre-II/QA/AUDIT-RETROACTIF-EXEMPLES-ERREURS-CH01-CH06.md\n", 1)
contents.write_text(text, encoding="utf-8")

index = ROOT / "Livre-II/index.md"
text = index.read_text(encoding="utf-8")
needle = "- [audit du chapitre 7](QA/AUDIT-CHAPITRE-07.md)."
replacement = needle + "\n- [audit rétroactif des exemples d’erreurs, chapitres 1 à 6](QA/AUDIT-RETROACTIF-EXEMPLES-ERREURS-CH01-CH06.md)."
if needle not in text:
    raise RuntimeError("Lien audit chapitre 7 introuvable dans l’index")
text = text.replace(needle, replacement, 1)
index.write_text(text, encoding="utf-8")

roadmap = ROOT / "ROADMAP.md"
text = roadmap.read_text(encoding="utf-8")
needle = "- [x] Chapitre 7 — Resources, JSON, catalogues et configurations — rédigé et audité au niveau `static-review`.\n"
addition = needle + "- [x] Audit rétroactif des sections d’erreurs, diagnostics et anti-patterns des chapitres 1 à 6 — 52 cas avec exemples fautifs et corrigés.\n"
if needle not in text:
    raise RuntimeError("Point chapitre 7 introuvable dans ROADMAP")
text = text.replace(needle, addition, 1)
roadmap.write_text(text, encoding="utf-8")

continuity = ROOT / "CONTINUITE-PROJET.md"
text = continuity.read_text(encoding="utf-8")
text = text.replace('version: "3.6.0"', 'version: "3.7.0"', 1)
old_rule = "Les rappels courts sont permis. Les duplications intégrales sont interdites. Toute section intitulée « Erreurs fréquentes et corrections » doit fournir, pour chaque erreur, au moins un exemple fautif, un exemple corrigé et l’explication de la différence."
new_rule = """Les rappels courts sont permis. Les duplications intégrales sont interdites.

La règle des erreurs et corrections est **sémantique**, pas nominale. Toute section dont la fonction est d’enseigner des erreurs fréquentes, diagnostics, anti-patterns, pièges ou mauvaises pratiques doit fournir, pour chaque cas détaillé : un symptôme, un exemple fautif, une correction, un exemple corrigé et l’explication de leur différence. Le titre peut être « Erreurs fréquentes », « Erreurs fréquentes et diagnostics », « Anti-patterns et corrections », « Éviter les anti-patterns » ou toute formulation équivalente.

Les sections détaillées portent `<!-- qa:error-correction-section -->`. Un index compact de symptômes peut porter `<!-- qa:error-correction-index -->` uniquement s’il renvoie vers des exemples détaillés conformes."""
if old_rule not in text:
    raise RuntimeError("Ancienne règle pédagogique introuvable dans la continuité")
text = text.replace(old_rule, new_rule, 1)
journal_heading = "## 16. Journal\n"
entry = '''## 16. Journal

### 2026-07-19 — version 3.7.0

- généralisation sémantique de la règle « erreur fautive / correction » ;
- audit rétroactif des chapitres 1 à 6 ;
- 52 cas détaillés enrichis ;
- ajout des marqueurs QA de section et d’index ;
- validation automatique renforcée ;
- aucun PDF intermédiaire construit.
'''
if journal_heading not in text:
    raise RuntimeError("Journal introuvable dans la continuité")
text = text.replace(journal_heading, entry, 1)
continuity.write_text(text, encoding="utf-8")

# Supprimer l'infrastructure temporaire avant le commit automatique.
for relative in (
    "tools/retrofit_error_examples.py",
    ".github/workflows/retrofit-error-examples.yml",
):
    target = ROOT / relative
    if target.exists():
        target.unlink()

print("Rétrofit pédagogique terminé : 52 cas détaillés, gouvernance et validateur mis à jour.")
