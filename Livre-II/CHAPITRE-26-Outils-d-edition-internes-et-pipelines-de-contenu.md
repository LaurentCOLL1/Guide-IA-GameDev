---
title: "Livre II — Chapitre 26 : Outils d’édition internes et pipelines de contenu"
id: "DOC-L2-CH26"
status: "reviewed"
version: "1.0.1"
lang: "fr-FR"
book: "Livre II"
chapter: 26
last-verified: "2026-07-21T15:28:42+02:00"
audit-status: "complete"
audit-date: "2026-07-21T15:28:42+02:00"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-26.md"
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

# Outils d’édition internes et pipelines de contenu

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH26`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-26.md`.
> **Explications de code :** structurées bloc par bloc ; les informations pédagogiques antérieures sont conservées dans des rubriques explicites, complétées seulement lorsque le bloc l’exige.
## 1. Rôle du chapitre

Les chapitres 14 à 25 ont défini des systèmes runtime propriétaires de leurs états. Le présent chapitre ne leur ajoute aucune nouvelle autorité : il construit une couche de production destinée aux auteurs, aux designers et aux intégrateurs de contenu.

Un outil d’édition réduit les manipulations répétitives, mais augmente le rayon d’impact d’une mauvaise action. Un clic peut modifier une scène ouverte, réécrire un catalogue ou déclencher une importation de masse. Le principe directeur est donc : **préparer, valider, prévisualiser, puis promouvoir**.

Le résultat attendu est un pipeline unique dont les règles peuvent être appelées depuis un dock Godot, l’Inspector, un importeur, un script headless ou une intégration continue, sans dupliquer la logique métier.

## 2. Prérequis et frontières

Le lecteur doit maîtriser les `Resource`, les documents JSON versionnés, les identifiants stables, les migrations et les frontières d’autorité définies précédemment.

Le chapitre couvre les plugins d’éditeur, les docks, les extensions d’Inspector, les importeurs, les manifestes, la validation multicouche, les graphes de dépendances, les empreintes, le staging, la publication, la provenance et la génération assistée.

Le chapitre 27 traitera les tests ; le chapitre 28, la journalisation et la reproductibilité détaillées ; le chapitre 29, l’automatisation Python à grande échelle ; le chapitre 30, l’architecture globale Solo et Studio. Ici, on établit les contrats qu’ils pourront exercer.

## 3. Sources, artefacts et caches

> **[LECTURE] Modèle de séparation — Ne pas saisir.**

```text
Sources auteur
  data_src/**/*.json
  prompts/**/*.md
  assets_src/**/*
        ↓ validation et compilation
Artefacts canoniques
  data/**/*.tres
  data/**/*.json
  manifests/content-manifest.json
        ↓ import et indexation
Caches dérivés
  .godot/imported/**
  .godot/asteria_cache/**
  dist/reports/**
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Les sources auteur sont modifiables et revues. Les artefacts canoniques sont les définitions approuvées que le runtime peut charger. Les caches peuvent être supprimés puis reconstruits ; ils ne doivent jamais devenir l’unique détenteur d’une information métier. Le schéma fait circuler le traitement de `Sources auteur` vers `dist/reports/**`.

- **Déroulement ou instructions importantes :** Les transitions visibles sont `↓ validation et compilation`, `↓ import et indexation`.

- **Résultat attendu :** La lecture doit conserver l’ordre et les correspondances explicites entre les éléments listés, sans inventer de relation absente du schéma.

- **Limites du contrat visible :** Le bloc décrit uniquement les éléments littéraux affichés ; il ne définit aucune étape supplémentaire hors de cette structure.

## 4. Arborescence feature-first

> **[LECTURE] Organisation du plugin — Ne pas saisir.**

```text
addons/asteria_content_tools/
├── plugin.cfg
├── plugin.gd
├── application/
│   ├── content_pipeline.gd
│   └── publish_content_command.gd
├── domain/
│   ├── content_issue.gd
│   ├── content_manifest.gd
│   └── pipeline_receipt.gd
├── infrastructure/
│   ├── canonical_json_writer.gd
│   ├── content_import_plugin.gd
│   └── staged_file_transaction.gd
└── presentation/
    ├── content_dock.tscn
    ├── content_dock.gd
    └── content_inspector_plugin.gd
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des fichiers :** Le fichier `plugin.gd` orchestre uniquement le cycle de vie de l’extension. Les chemins restent séparés selon leur responsabilité ; les fichiers listés ne sont pas interchangeables entre domaine, application, infrastructure et présentation.

- **Limites et réserves :** La validation et la publication sont réutilisables sans interface. Les accès disque restent dans l’infrastructure, tandis que les contrôles Godot résident dans la présentation.

- **Rôle précis du bloc :** L’arborescence répartit les éléments entre `plugin.cfg`, `plugin.gd`, `application`, `content_pipeline.gd`, `publish_content_command.gd`, `domain`, `content_issue.gd`, `content_manifest.gd`.

- **Résultat attendu :** La lecture doit conserver l’ordre et les correspondances explicites entre les éléments listés, sans inventer de relation absente du schéma.

## 5. Déclarer le plugin

> **[VSC] Fichier `addons/asteria_content_tools/plugin.cfg` — Ne pas saisir.**

```ini
[plugin]
name="Asteria Content Tools"
description="Validation et publication contrôlée du contenu de Project Asteria"
author="Project Asteria"
version="1.0.0"
script="plugin.gd"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** La section `plugin` rend l’extension détectable.

- **Paramètres et types importants :** Le champ `script` pointe vers l’`EditorPlugin` chargé à l’activation. Les clés visibles comprennent `name`, `description`, `author`, `version`, `script`.

- **Dépendances et ports utilisés :** La version appartient à l’outil de production et doit figurer dans les reçus lorsque son comportement influence les artefacts.

- **Rôle précis du bloc :** Le bloc matérialise le format de données annoncé par `> **[VSC] Fichier `addons/asteria_content_tools/plugin.cfg` — Ne pas saisir.**`.

- **Organisation des données :** La configuration est organisée dans `[plugin]`.

- **Résultat attendu :** Une lecture conforme doit retrouver les mêmes clés, leurs relations et les valeurs obligatoires avant toute promotion ou consommation.

## 6. Exécuter du code dans l’éditeur

> **[VSC] Script `@tool` minimal — Ne pas saisir.**

```gdscript
@tool
extends Node

func refresh_preview() -> void:
    if not Engine.is_editor_hint():
        return
    queue_redraw()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** `@tool` autorise l’exécution dans l’éditeur. `Engine.is_editor_hint()` isole le chemin éditorial si le script peut aussi être instancié ailleurs. Le bloc expose `refresh_preview()` et montre son traitement complet ou son squelette contractuel.

- **Frontières d’autorité :** Une méthode outil ne doit jamais muter une partie ni appeler directement une autorité runtime.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `refresh_preview() -> void`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `queue_redraw()`.

- **Invariants protégés :** Les gardes explicites contrôlent `not Engine.is_editor_hint()`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 7. Limiter le rayon d’impact

Un script `@tool` s’exécute dans le processus de l’éditeur. Une boucle de sauvegarde, une libération de nœud mal placée ou un accès non borné peut bloquer l’outil de production.

La politique retenue interdit les actions destructives dans `_process()`, les scans complets à chaque changement d’Inspector, les chemins externes non validés et toute promotion automatique après une génération IA. Une opération multi-fichiers exige un aperçu lisible et un moyen de restauration adapté au support modifié.

## 8. Cycle de vie symétrique d’un EditorPlugin

> **[VSC] Plugin racine — Ne pas saisir.**

```gdscript
@tool
extends EditorPlugin

var _dock: Control
var _inspector_plugin: EditorInspectorPlugin
var _import_plugin: EditorImportPlugin

func _enter_tree() -> void:
    _dock = preload(
        "res://addons/asteria_content_tools/presentation/content_dock.tscn"
    ).instantiate()
    add_control_to_dock(DOCK_SLOT_RIGHT_UL, _dock)

    _inspector_plugin = preload(
        "res://addons/asteria_content_tools/presentation/content_inspector_plugin.gd"
    ).new()
    add_inspector_plugin(_inspector_plugin)

    _import_plugin = preload(
        "res://addons/asteria_content_tools/infrastructure/content_import_plugin.gd"
    ).new()
    add_import_plugin(_import_plugin)

func _exit_tree() -> void:
    if _import_plugin != null:
        remove_import_plugin(_import_plugin)
    if _inspector_plugin != null:
        remove_inspector_plugin(_inspector_plugin)
    if _dock != null:
        remove_control_from_docks(_dock)
        _dock.queue_free()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** Chaque enregistrement possède son retrait miroir. L’exemple utilise l’API de dock historique encore disponible ; une implémentation strictement alignée sur `EditorDock` emploie `add_dock()` et `remove_dock()` avec le même invariant de nettoyage. Les signatures documentées sont `_enter_tree() -> void`, `_exit_tree() -> void`.

- **Rôle précis du bloc :** Le bloc expose `_enter_tree()`, `_exit_tree()` et montre son traitement complet ou son squelette contractuel.

- **Paramètres et types importants :** Les déclarations visibles sont `_dock: Control`, `_inspector_plugin: EditorInspectorPlugin`, `_import_plugin: EditorImportPlugin`.

- **Invariants protégés :** Les gardes explicites contrôlent `_import_plugin != null`, `_inspector_plugin != null`, `_dock != null`.

- **Effets de bord :** Les effets visibles sont `_dock.queue_free()`.

## 9. Empêcher une dépendance runtime

> **[VSC] Garde d’environnement — Ne pas saisir.**

```gdscript
func _ready() -> void:
    if not Engine.is_editor_hint():
        push_error("Asteria Content Tools ne doit pas être chargé au runtime.")
        set_process(false)
        return
    _connect_editor_signals()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La garde échoue explicitement si le module est chargé hors éditeur. Le bloc expose `_ready()` et montre son traitement complet ou son squelette contractuel.

- **Dépendances et ports utilisés :** Le package runtime ne doit dépendre ni de ce plugin, ni de ses scènes d’interface, ni de ses adaptateurs de fichiers.

- **Limites et réserves :** Les artefacts publiés restent utilisables sans l’extension.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `_ready() -> void`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `_connect_editor_signals()`.

- **Invariants protégés :** Les gardes explicites contrôlent `not Engine.is_editor_hint()`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 10. Dock orienté commande

> **[VSC] Contrôleur du dock — Ne pas saisir.**

```gdscript
@tool
extends VBoxContainer

signal preview_requested(selection: PackedStringArray)
signal publish_requested(receipt_id: StringName)

@onready var preview_button: Button = %PreviewButton
@onready var publish_button: Button = %PublishButton

func _ready() -> void:
    preview_button.pressed.connect(_on_preview_pressed)
    publish_button.pressed.connect(_on_publish_pressed)

func _on_preview_pressed() -> void:
    preview_requested.emit(_collect_selected_paths())

func _on_publish_pressed() -> void:
    publish_requested.emit(&"current_preview")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Effets de bord :** Le dock émet des intentions et ne réalise aucun accès disque. Les effets visibles sont `preview_requested.emit(_collect_selected_paths())`, `publish_requested.emit(&"current_preview")`.

- **Responsabilités des classes ou fonctions :** Le service applicatif calcule l’aperçu et le reçu. Les signatures documentées sont `_ready() -> void`, `_on_preview_pressed() -> void`, `_on_publish_pressed() -> void`.

- **Limites et réserves :** Le bouton de publication ne peut donc pas construire arbitrairement une liste de fichiers à écrire.

- **Rôle précis du bloc :** Le bloc expose `_ready()`, `_on_preview_pressed()`, `_on_publish_pressed()` et montre son traitement complet ou son squelette contractuel.

- **Paramètres et types importants :** Les déclarations visibles sont `signal preview_requested`, `signal publish_requested`.

## 11. États explicites de l’interface

> **[VSC] Machine d’état du dock — Ne pas saisir.**

```gdscript
enum DockState {
    IDLE,
    SCANNING,
    INVALID,
    READY_TO_PUBLISH,
    PUBLISHING,
    FAILED
}

var state: DockState = DockState.IDLE

func can_publish() -> bool:
    return state == DockState.READY_TO_PUBLISH

func set_state(next_state: DockState) -> void:
    state = next_state
    %PublishButton.disabled = not can_publish()
    %ProgressBar.visible = state in [
        DockState.SCANNING,
        DockState.PUBLISHING
    ]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** `READY_TO_PUBLISH` est la seule porte d’activation du bouton.

- **Limites et réserves :** Une validation échouée, un aperçu obsolète ou une opération en cours ne peut pas lancer la promotion.

- **Rôle précis du bloc :** L’interface reflète une décision applicative plutôt qu’une déduction visuelle. Le bloc expose `can_publish()`, `set_state()` et montre son traitement complet ou son squelette contractuel.

- **Paramètres et types importants :** Les déclarations visibles sont `state: DockState`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `can_publish() -> bool`, `set_state(next_state: DockState) -> void`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `state == DockState.READY_TO_PUBLISH`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 12. Étendre l’Inspector

> **[VSC] Inspector ciblé — Ne pas saisir.**

```gdscript
@tool
extends EditorInspectorPlugin

func _can_handle(object: Object) -> bool:
    return object is QuestDefinition

func _parse_begin(object: Object) -> void:
    var button := Button.new()
    button.text = "Valider cette définition"
    button.pressed.connect(
        _request_validation.bind(object.resource_path)
    )
    add_custom_control(button)

func _request_validation(resource_path: String) -> void:
    ContentToolBus.validation_requested.emit(resource_path)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** `_can_handle()` ferme le périmètre à un type connu.

- **Effets de bord :** `_parse_begin()` ajoute un contrôle sans remplacer les propriétés natives. Les effets visibles sont `ContentToolBus.validation_requested.emit(resource_path)`.

- **Responsabilités des classes ou fonctions :** L’action transmet un chemin de ressource au service applicatif et ne corrige jamais silencieusement l’objet sélectionné. Les signatures documentées sont `_can_handle(object: Object) -> bool`, `_parse_begin(object: Object) -> void`, `_request_validation(resource_path: String) -> void`.

- **Rôle précis du bloc :** Le bloc expose `_can_handle()`, `_parse_begin()`, `_request_validation()` et montre son traitement complet ou son squelette contractuel.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `object is QuestDefinition`.

## 13. Mutations annulables

> **[VSC] Modification via `EditorUndoRedoManager` — Ne pas saisir.**

```gdscript
func rename_entry(resource: Resource, next_id: StringName) -> void:
    var undo_redo := EditorInterface.get_editor_undo_redo()
    var previous_id: StringName = resource.entry_id

    undo_redo.create_action(
        "Renommer l’identifiant de contenu",
        UndoRedo.MERGE_DISABLE,
        resource
    )
    undo_redo.add_do_property(resource, "entry_id", next_id)
    undo_redo.add_undo_property(resource, "entry_id", previous_id)
    undo_redo.commit_action()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** L’action conserve l’ancienne et la nouvelle valeur dans l’historique approprié. La ressource fournie comme contexte aide l’éditeur à sélectionner l’historique. Le bloc expose `rename_entry()` et montre son traitement complet ou son squelette contractuel.

- **Effets de bord :** `commit_action()` exécute l’opération et marque normalement le document comme modifié. Les effets visibles sont `undo_redo.add_do_property(resource, "entry_id", next_id)`, `undo_redo.add_undo_property(resource, "entry_id", previous_id)`, `undo_redo.commit_action()`.

- **Paramètres et types importants :** Les déclarations visibles sont `previous_id: StringName`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `rename_entry(resource: Resource, next_id: StringName) -> void`.

## 14. Scène non enregistrée

> **[VSC] Marquage explicite — Ne pas saisir.**

```gdscript
func update_generated_preview(node: Node3D, mesh: Mesh) -> void:
    node.set_meta(&"preview_mesh", mesh)
    EditorInterface.mark_scene_as_unsaved()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** Une opération qui ne peut raisonnablement pas être modélisée par undo/redo doit au minimum marquer la scène comme non enregistrée. Cette voie reste secondaire : les mutations structurelles doivent préférer l’historique de l’éditeur.

- **Rôle précis du bloc :** Le bloc expose `update_generated_preview()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `update_generated_preview(node: Node3D, mesh: Mesh) -> void`.

- **Déroulement ou instructions importantes :** L’extrait commence par `func update_generated_preview(node: Node3D, mesh: Mesh) -> void:` et se termine par `EditorInterface.mark_scene_as_unsaved()` ; les lignes intermédiaires doivent être lues dans cet ordre.

## 15. Diagnostic de contenu

> **[VSC] Objet `ContentIssue` — Ne pas saisir.**

```gdscript
class_name ContentIssue
extends RefCounted

enum Severity { INFO, WARNING, ERROR, BLOCKING }

var severity: Severity
var code: StringName
var path: String
var pointer: String
var message: String
var suggestion: String

func blocks_publication() -> bool:
    return severity == Severity.BLOCKING
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Un diagnostic possède un code stable, un fichier et un pointeur interne. Le texte aide l’auteur ; `code` sert au filtrage et à l’automatisation. Le bloc définit `ContentIssue` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Invariants protégés :** Seule la sévérité `BLOCKING` interdit mécaniquement la publication.

- **Paramètres et types importants :** Les déclarations visibles sont `severity: Severity`, `code: StringName`, `path: String`, `pointer: String`, `message: String`, `suggestion: String`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `blocks_publication() -> bool`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `severity == Severity.BLOCKING`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 16. Rapport détaché

> **[VSC] Résultat de validation — Ne pas saisir.**

```gdscript
class_name ContentValidationReport
extends RefCounted

var source_fingerprint: String
var issues: Array[ContentIssue] = []
var checked_paths: PackedStringArray = []

func is_publishable() -> bool:
    for issue in issues:
        if issue.blocks_publication():
            return false
    return not source_fingerprint.is_empty()

func duplicate_detached() -> ContentValidationReport:
    var copy := ContentValidationReport.new()
    copy.source_fingerprint = source_fingerprint
    copy.issues = issues.duplicate(true)
    copy.checked_paths = checked_paths.duplicate()
    return copy
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** Le rapport est une photographie du contrôle.

- **Déterminisme et idempotence :** Son empreinte relie la décision aux sources exactes.

- **Effets de bord :** La copie profonde empêche le panneau d’interface de modifier une collection réutilisée par la commande de publication. Les effets visibles sont `copy.source_fingerprint = source_fingerprint`, `copy.issues = issues.duplicate(true)`, `copy.checked_paths = checked_paths.duplicate()`.

- **Rôle précis du bloc :** Le bloc définit `ContentValidationReport` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Paramètres et types importants :** Les déclarations visibles sont `source_fingerprint: String`, `issues: Array[ContentIssue]`, `checked_paths: PackedStringArray`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `is_publishable() -> bool`, `duplicate_detached() -> ContentValidationReport`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `false`, `not source_fingerprint.is_empty()`, `copy`.

- **Invariants protégés :** Les gardes explicites contrôlent `issue.blocks_publication()`.

## 17. Registre fermé des validateurs

> **[VSC] Sélection de stratégie — Ne pas saisir.**

```gdscript
class_name ContentValidatorRegistry
extends RefCounted

var _validators: Dictionary[StringName, ContentValidator] = {}

func register(
    type_id: StringName,
    validator: ContentValidator
) -> Error:
    if type_id.is_empty() or validator == null:
        return ERR_INVALID_PARAMETER
    if _validators.has(type_id):
        return ERR_ALREADY_EXISTS
    _validators[type_id] = validator
    return OK

func validate(
    type_id: StringName,
    document: Dictionary
) -> Array[ContentIssue]:
    var validator: ContentValidator = _validators.get(type_id)
    if validator == null:
        return [
            ContentIssueFactory.blocking(
                &"unknown_content_type",
                "Type de contenu non enregistré."
            )
        ]
    return validator.validate(document)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** La donnée ne fournit ni chemin de script, ni classe, ni nom de méthode. Les signatures documentées sont `register(type_id: StringName, validator: ContentValidator) -> Error`, `validate(type_id: StringName, document: Dictionary) -> Array[ContentIssue]`.

- **Invariants protégés :** Elle choisit uniquement un identifiant présent dans un registre construit par le code. Les gardes explicites contrôlent `type_id.is_empty() or validator == null`, `_validators.has(type_id)`, `validator == null`.

- **Paramètres et types importants :** Un type inconnu produit un blocage explicite. Les déclarations visibles sont `_validators: Dictionary[StringName, ContentValidator]`, `validator: ContentValidator`.

- **Rôle précis du bloc :** Le bloc définit `ContentValidatorRegistry` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ERR_INVALID_PARAMETER`, `ERR_ALREADY_EXISTS`, `OK`, `[`, `validator.validate(document)`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 18. Couches de validation

> **[LECTURE] Ordre des contrôles — Ne pas saisir.**

```text
1. Lecture bornée et encodage
2. Syntaxe JSON ou ressource
3. Version de schéma
4. Forme et types des champs
5. Identifiants et références
6. Invariants sémantiques
7. Compatibilité inter-systèmes
8. Assets et localisations
9. Politique de publication
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Chaque couche suppose la précédente valide.

- **Paramètres et types importants :** Une référence n’est pas résolue avant que son champ soit reconnu comme chaîne.

- **Limites et réserves :** Cet ordre limite les cascades de diagnostics secondaires et localise mieux la cause initiale.

- **Rôle précis du bloc :** Le bloc compare ou énumère `1. Lecture bornée et encodage`, `2. Syntaxe JSON ou ressource`, `3. Version de schéma`, `4. Forme et types des champs`, `5. Identifiants et références`, `6. Invariants sémantiques`.

- **Résultat attendu :** La lecture doit conserver l’ordre et les correspondances explicites entre les éléments listés, sans inventer de relation absente du schéma.

## 19. Lecture bornée

> **[VSC] Chargeur défensif — Ne pas saisir.**

```gdscript
const MAX_SOURCE_BYTES := 4 * 1024 * 1024

func read_source(path: String) -> ContentReadResult:
    if not path.begins_with("res://data_src/"):
        return ContentReadResult.rejected(
            &"path_outside_source_root"
        )

    var bytes := FileAccess.get_file_as_bytes(path)
    if bytes.size() > MAX_SOURCE_BYTES:
        return ContentReadResult.rejected(&"source_too_large")

    if bytes.is_empty() and FileAccess.get_open_error() != OK:
        return ContentReadResult.failed(
            FileAccess.get_open_error()
        )

    return ContentReadResult.accepted(
        bytes.get_string_from_utf8()
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des fichiers :** Le chemin reste dans la racine source et la taille est bornée avant analyse.

- **Rôle précis du bloc :** Le résultat distingue un refus de politique d’un échec d’entrée-sortie. Le bloc expose `read_source()` et montre son traitement complet ou son squelette contractuel.

- **Limites et réserves :** Une implémentation optimisée pourra lire la taille sans charger tout le fichier.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `read_source(path: String) -> ContentReadResult`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ContentReadResult.rejected(`, `ContentReadResult.rejected(&"source_too_large")`, `ContentReadResult.failed(`, `ContentReadResult.accepted(`.

- **Invariants protégés :** Les gardes explicites contrôlent `not path.begins_with("res://data_src/")`, `bytes.size() > MAX_SOURCE_BYTES`, `bytes.is_empty() and FileAccess.get_open_error() != OK`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 20. Schéma versionné

> **[VSC] Préparation et migration — Ne pas saisir.**

```gdscript
const CURRENT_SCHEMA := 3

func prepare_document(
    raw: Dictionary
) -> ContentPreparationResult:
    var version := int(raw.get("schema_version", -1))

    if version < 0:
        return ContentPreparationResult.rejected(
            &"missing_schema_version"
        )
    if version > CURRENT_SCHEMA:
        return ContentPreparationResult.rejected(
            &"future_schema"
        )

    var candidate := raw.duplicate(true)
    while version < CURRENT_SCHEMA:
        candidate = _migrations[version].migrate(candidate)
        version += 1

    return _validate_candidate(candidate)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Les migrations travaillent sur une copie détachée. Le candidat final est entièrement validé avant toute promotion. Le bloc expose `prepare_document()` et montre son traitement complet ou son squelette contractuel.

- **Résultat attendu :** Une version future est refusée afin qu’un ancien outil ne réécrive pas un document qu’il ne comprend pas.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `prepare_document(raw: Dictionary) -> ContentPreparationResult`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ContentPreparationResult.rejected(`, `_validate_candidate(candidate)`.

- **Invariants protégés :** Les gardes explicites contrôlent `version < 0`, `version > CURRENT_SCHEMA`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 21. Références stables

> **[VSC] Contrôle de catalogue — Ne pas saisir.**

```gdscript
func validate_reference(
    source_path: String,
    field_name: StringName,
    target_id: StringName,
    catalog: ContentIdCatalog
) -> Array[ContentIssue]:
    if target_id.is_empty():
        return [
            ContentIssueFactory.blocking(
                &"empty_reference",
                source_path,
                field_name
            )
        ]

    if not catalog.contains(target_id):
        return [
            ContentIssueFactory.blocking(
                &"missing_reference",
                source_path,
                field_name
            )
        ]

    return []
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** La validation consulte un catalogue d’identifiants, jamais un titre affiché ou un chemin comme identité métier. Le diagnostic conserve le fichier et le champ qui portent la référence manquante.

- **Rôle précis du bloc :** Le bloc expose `validate_reference()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `validate_reference(source_path: String, field_name: StringName, target_id: StringName, catalog: ContentIdCatalog) -> Array[ContentIssue]`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `[`, `[]`.

- **Invariants protégés :** Les gardes explicites contrôlent `target_id.is_empty()`, `not catalog.contains(target_id)`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 22. Graphe de dépendances

> **[VSC] Construction du graphe — Ne pas saisir.**

```gdscript
class_name ContentDependencyGraph
extends RefCounted

var _edges: Dictionary[StringName, Array] = {}

func add_node(content_id: StringName) -> void:
    if not _edges.has(content_id):
        _edges[content_id] = []

func add_dependency(
    content_id: StringName,
    depends_on: StringName
) -> Error:
    add_node(content_id)
    add_node(depends_on)

    if depends_on in _edges[content_id]:
        return ERR_ALREADY_EXISTS

    _edges[content_id].append(depends_on)
    return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Effets de bord :** Le graphe décrit les dépendances logiques entre définitions. Les effets visibles sont `_edges[content_id].append(depends_on)`.

- **Limites et réserves :** Les nœuds autonomes existent même sans arête. Les collections internes restent privées afin qu’une étape de présentation ne puisse pas altérer le plan de compilation.

- **Rôle précis du bloc :** Le bloc définit `ContentDependencyGraph` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Paramètres et types importants :** Les déclarations visibles sont `_edges: Dictionary[StringName, Array]`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `add_node(content_id: StringName) -> void`, `add_dependency(content_id: StringName, depends_on: StringName) -> Error`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ERR_ALREADY_EXISTS`, `OK`.

- **Invariants protégés :** Les gardes explicites contrôlent `not _edges.has(content_id)`, `depends_on in _edges[content_id]`.

## 23. Rejeter les cycles

> **[VSC] Parcours tricolore — Ne pas saisir.**

```gdscript
enum VisitState { UNSEEN, ACTIVE, DONE }

func find_cycle(
    node: StringName,
    states: Dictionary,
    stack: Array[StringName]
) -> Array[StringName]:
    states[node] = VisitState.ACTIVE
    stack.append(node)

    for dependency: StringName in _edges[node]:
        var state: VisitState = states.get(
            dependency,
            VisitState.UNSEEN
        )

        if state == VisitState.ACTIVE:
            var start := stack.find(dependency)
            return stack.slice(start) + [dependency]

        if state == VisitState.UNSEEN:
            var nested := find_cycle(
                dependency,
                states,
                stack
            )
            if not nested.is_empty():
                return nested

    stack.pop_back()
    states[node] = VisitState.DONE
    return []
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Rencontrer un nœud `ACTIVE` révèle une arête de retour. Le bloc expose `find_cycle()` et montre son traitement complet ou son squelette contractuel.

- **Résultat attendu :** Le chemin retourné rend le diagnostic actionnable.

- **Responsabilités des classes ou fonctions :** Le pipeline n’invente jamais un ordre lorsque le graphe contient une boucle. Les signatures documentées sont `find_cycle(node: StringName, states: Dictionary, stack: Array[StringName]) -> Array[StringName]`.

- **Paramètres et types importants :** Les déclarations visibles sont `state: VisitState`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `stack.slice(start) + [dependency]`, `nested`, `[]`.

- **Invariants protégés :** Les gardes explicites contrôlent `state == VisitState.ACTIVE`, `state == VisitState.UNSEEN`, `not nested.is_empty()`.

- **Effets de bord :** Les effets visibles sont `stack.append(node)`.

## 24. Ordre topologique déterministe

> **[VSC] Tri stable des définitions — Ne pas saisir.**

```gdscript
func topological_order() -> Array[StringName]:
    var remaining := _compute_in_degrees()
    var ready: Array[StringName] = []

    for content_id: StringName in remaining.keys():
        if remaining[content_id] == 0:
            ready.append(content_id)

    ready.sort()
    var result: Array[StringName] = []

    while not ready.is_empty():
        var current := ready.pop_front()
        result.append(current)

        for dependent: StringName in _dependents_of(current):
            remaining[dependent] -= 1
            if remaining[dependent] == 0:
                ready.append(dependent)
                ready.sort()

    return result if result.size() == remaining.size() else []
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Le tri des candidats prêts fixe un ordre reproductible lorsque plusieurs solutions sont valides. Les gardes explicites contrôlent `remaining[content_id] == 0`, `remaining[dependent] == 0`.

- **Rôle précis du bloc :** Un tableau vide signale un cycle ou une incohérence. Cette stabilité évite des artefacts différents entre deux machines. Le bloc expose `topological_order()` et montre son traitement complet ou son squelette contractuel.

- **Paramètres et types importants :** Les déclarations visibles sont `ready: Array[StringName]`, `result: Array[StringName]`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `topological_order() -> Array[StringName]`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `result if result.size() == remaining.size() else []`.

- **Effets de bord :** Les effets visibles sont `ready.append(content_id)`, `result.append(current)`, `ready.append(dependent)`.

## 25. Sérialisation canonique

> **[VSC] Normalisation récursive — Ne pas saisir.**

```gdscript
class_name CanonicalValue
extends RefCounted

static func normalize(value: Variant) -> Variant:
    if value is Dictionary:
        var ordered := {}
        var keys: Array = value.keys()
        keys.sort_custom(
            func(a: Variant, b: Variant) -> bool:
                return str(a) < str(b)
        )
        for key: Variant in keys:
            ordered[str(key)] = normalize(value[key])
        return ordered

    if value is Array:
        var items: Array = []
        for item: Variant in value:
            items.append(normalize(item))
        return items

    return value
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Les clés de dictionnaire sont ordonnées, tandis que les tableaux conservent leur ordre métier. Une date de build ne participe jamais à la valeur canonique. Le bloc définit `CanonicalValue` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Persistance et restauration :** La sérialisation finale doit imposer UTF-8 et une convention stable pour les nombres.

- **Paramètres et types importants :** Les déclarations visibles sont `keys: Array`, `items: Array`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `normalize(value: Variant) -> Variant`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `str(a) < str(b)`, `ordered`, `items`, `value`.

- **Invariants protégés :** Les gardes explicites contrôlent `value is Dictionary`, `value is Array`.

- **Effets de bord :** Les effets visibles sont `items.append(normalize(item))`.

## 26. Empreinte SHA-256

> **[VSC] Hachage du JSON canonique — Ne pas saisir.**

```gdscript
func fingerprint(document: Dictionary) -> String:
    var normalized := CanonicalValue.normalize(document)
    var canonical_json := JSON.stringify(
        normalized,
        "",
        false,
        true
    )

    var context := HashingContext.new()
    context.start(HashingContext.HASH_SHA256)
    context.update(canonical_json.to_utf8_buffer())
    return context.finish().hex_encode()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** L’empreinte dépend uniquement du document normalisé.

- **Invariants protégés :** Elle permet de vérifier qu’un aperçu correspond encore aux sources.

- **Rôle précis du bloc :** Elle ne constitue ni une signature d’auteur ni une preuve suffisante de provenance. Le bloc expose `fingerprint()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `fingerprint(document: Dictionary) -> String`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `context.finish().hex_encode()`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 27. Manifeste de contenu

> **[LECTURE] Exemple de manifeste — Ne pas saisir.**

```json
{
  "manifest_version": 1,
  "tool_version": "1.0.0",
  "content_schema": 3,
  "entries": [
    {
      "content_id": "quest_asteria_first_signal",
      "source_path": "res://data_src/narrative/first_signal.json",
      "artifact_path": "res://data/narrative/first_signal.tres",
      "source_sha256": "sha256:…",
      "artifact_sha256": "sha256:…"
    }
  ]
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** Le manifeste relie identité, source, artefact et empreintes.

- **Persistance et restauration :** Ses entrées sont triées avant sérialisation.

- **Responsabilités des classes ou fonctions :** La version de l’outil explique quel compilateur a produit le lot sans rendre ce compilateur nécessaire à l’exécution du jeu.

- **Rôle précis du bloc :** Le bloc matérialise le format de données annoncé par `> **[LECTURE] Exemple de manifeste — Ne pas saisir.**`.

- **Paramètres et types importants :** Les clés visibles comprennent `manifest_version`, `tool_version`, `content_schema`, `entries`, `content_id`, `source_path`, `artifact_path`, `source_sha256`, `artifact_sha256`.

- **Résultat attendu :** Une lecture conforme doit retrouver les mêmes clés, leurs relations et les valeurs obligatoires avant toute promotion ou consommation.

## 28. Provenance de génération assistée

> **[LECTURE] Métadonnées de provenance — Ne pas saisir.**

```json
{
  "generator": {
    "kind": "local_text_model",
    "model_id": "model-local-example",
    "prompt_template_id": "quest-draft-v2",
    "parameters_digest": "sha256:…"
  },
  "review": {
    "status": "approved",
    "reviewer_id": "author_local_01",
    "approved_source_sha256": "sha256:…"
  }
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Effets de bord :** La provenance décrit la génération et l’approbation. Elle ne remplace ni le schéma ni la revue.

- **Déterminisme et idempotence :** Le manifeste ne copie aucun secret, jeton ou échange complet ; l’approbation porte sur l’empreinte exacte de la source examinée.

- **Rôle précis du bloc :** Le bloc matérialise le format de données annoncé par `> **[LECTURE] Métadonnées de provenance — Ne pas saisir.**`.

- **Paramètres et types importants :** Les clés visibles comprennent `generator`, `kind`, `model_id`, `prompt_template_id`, `parameters_digest`, `review`, `status`, `reviewer_id`, `approved_source_sha256`.

- **Résultat attendu :** Une lecture conforme doit retrouver les mêmes clés, leurs relations et les valeurs obligatoires avant toute promotion ou consommation.

## 29. Reçu du pipeline

> **[VSC] Objet `PipelineReceipt` — Ne pas saisir.**

```gdscript
class_name PipelineReceipt
extends RefCounted

var receipt_id: StringName
var source_fingerprint: String
var artifact_fingerprint: String
var tool_version: String
var issue_counts: Dictionary[StringName, int] = {}
var published_paths: PackedStringArray = []

func matches(
    report: ContentValidationReport
) -> bool:
    return source_fingerprint == report.source_fingerprint
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le reçu relie validation, compilation et publication. Le bloc définit `PipelineReceipt` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Dépendances et ports utilisés :** `matches()` empêche de publier avec un rapport devenu obsolète.

- **Déterminisme et idempotence :** Un horodatage peut être ajouté pour le suivi, mais reste hors de l’empreinte déterministe.

- **Paramètres et types importants :** Les déclarations visibles sont `receipt_id: StringName`, `source_fingerprint: String`, `artifact_fingerprint: String`, `tool_version: String`, `issue_counts: Dictionary[StringName, int]`, `published_paths: PackedStringArray`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `matches(report: ContentValidationReport) -> bool`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `source_fingerprint == report.source_fingerprint`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 30. Pipeline en étapes fermées

> **[VSC] Orchestrateur de préparation — Ne pas saisir.**

```gdscript
class_name ContentPipeline
extends RefCounted

enum Stage {
    DISCOVER,
    READ,
    VALIDATE,
    PLAN,
    COMPILE,
    STAGE,
    VERIFY,
    PROMOTE
}

func prepare(
    request: ContentBuildRequest
) -> ContentBuildPlan:
    var discovered := _discovery.discover(request.roots)
    var documents := _reader.read_all(discovered)
    var report := _validator.validate_all(documents)

    if not report.is_publishable():
        return ContentBuildPlan.rejected(report)

    var order := _dependency_planner.plan(documents)
    return _compiler.prepare_plan(
        documents,
        order,
        report
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** `prepare()` ne touche pas aux artefacts canoniques. Le bloc définit `ContentPipeline` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Invariants protégés :** Il découvre, lit, valide et planifie. Les phases de staging, vérification et promotion commencent seulement après une confirmation explicite. Les gardes explicites contrôlent `not report.is_publishable()`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `prepare(request: ContentBuildRequest) -> ContentBuildPlan`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ContentBuildPlan.rejected(report)`, `_compiler.prepare_plan(`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 31. Compilation pure

> **[VSC] Compilateur de quête — Ne pas saisir.**

```gdscript
class_name QuestContentCompiler
extends RefCounted

func compile(source: Dictionary) -> QuestDefinition:
    var result := QuestDefinition.new()
    result.quest_id = StringName(source["quest_id"])
    result.title_key = StringName(source["title_key"])
    result.objectives = _compile_objectives(
        source["objectives"]
    )
    result.consequences = _compile_consequences(
        source["consequences"]
    )
    return result
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Valeur de retour ou code d’échec :** Le compilateur reçoit un document déjà validé et retourne une nouvelle définition. Les branches de sortie visibles renvoient `result`.

- **Dépendances et ports utilisés :** Il ne consulte ni singleton, ni horloge, ni système de fichiers.

- **Rôle précis du bloc :** Cette pureté simplifie la comparaison des sorties et prépare les tests du chapitre 27. Le bloc définit `QuestContentCompiler` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `compile(source: Dictionary) -> QuestDefinition`.

- **Effets de bord :** Les effets visibles sont `result.quest_id = StringName(source["quest_id"])`, `result.title_key = StringName(source["title_key"])`, `result.objectives = _compile_objectives(`, `result.consequences = _compile_consequences(`.

## 32. Staging avant promotion

> **[LECTURE] Cycle de fichiers — Ne pas saisir.**

```text
res://data_src/narrative/first_signal.json
        ↓ compilation
user://content_staging/build-<receipt>/first_signal.tres
        ↓ relecture et empreinte
res://data/narrative/first_signal.tres.tmp
        ↓ sauvegarde de l’ancien artefact
res://data/narrative/first_signal.tres.bak
        ↓ remplacement contrôlé
res://data/narrative/first_signal.tres
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** Le staging reste hors du chemin canonique.

- **Persistance et restauration :** L’ancien artefact reçoit une sauvegarde ciblée avant remplacement.

- **Effets de bord :** La documentation décrit les garanties réelles du système de fichiers et ne promet pas une atomicité universelle.

- **Rôle précis du bloc :** Le schéma fait circuler le traitement de `res://data_src/narrative/first_signal.json` vers `res://data/narrative/first_signal.tres`.

- **Déroulement ou instructions importantes :** Les transitions visibles sont `↓ compilation`, `↓ relecture et empreinte`, `↓ sauvegarde de l’ancien artefact`, `↓ remplacement contrôlé`.

- **Résultat attendu :** La lecture doit conserver l’ordre et les correspondances explicites entre les éléments listés, sans inventer de relation absente du schéma.

## 33. Transaction préparée

> **[VSC] Plan de promotion — Ne pas saisir.**

```gdscript
class_name StagedFileTransaction
extends RefCounted

var writes: Array[StagedWrite] = []
var deletes: PackedStringArray = []
var source_fingerprint: String

func validate() -> Error:
    if source_fingerprint.is_empty():
        return ERR_INVALID_DATA

    var targets := {}
    for write: StagedWrite in writes:
        if targets.has(write.target_path):
            return ERR_ALREADY_EXISTS
        targets[write.target_path] = true

    return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Effets de bord :** La transaction décrit toutes les écritures et suppressions avant le commit. Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

- **Rôle précis du bloc :** Deux opérations ne peuvent pas viser le même chemin. Le bloc définit `StagedFileTransaction` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Déterminisme et idempotence :** Le committer revérifiera les empreintes et préparera les sauvegardes avant la première promotion.

- **Paramètres et types importants :** Les déclarations visibles sont `writes: Array[StagedWrite]`, `deletes: PackedStringArray`, `source_fingerprint: String`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `validate() -> Error`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ERR_INVALID_DATA`, `ERR_ALREADY_EXISTS`, `OK`.

- **Invariants protégés :** Les gardes explicites contrôlent `source_fingerprint.is_empty()`, `targets.has(write.target_path)`.

## 34. Sauvegarder une Resource

> **[VSC] Écriture dans le staging — Ne pas saisir.**

```gdscript
func save_staged(
    resource: Resource,
    staging_path: String
) -> Error:
    if not staging_path.begins_with(
        "user://content_staging/"
    ):
        return ERR_INVALID_PARAMETER

    var error := ResourceSaver.save(
        resource,
        staging_path
    )
    if error != OK:
        return error

    if not FileAccess.file_exists(staging_path):
        return ERR_CANT_CREATE

    return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Valeur de retour ou code d’échec :** `ResourceSaver.save()` retourne un code `Error` qui doit être consommé. Les branches de sortie visibles renvoient `ERR_INVALID_PARAMETER`, `error`, `ERR_CANT_CREATE`, `OK`.

- **Rôle précis du bloc :** Le chemin est borné à la zone de staging. La simple existence ne suffit pas : l’étape suivante recharge et contrôle l’artefact. Le bloc expose `save_staged()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `save_staged(resource: Resource, staging_path: String) -> Error`.

- **Invariants protégés :** Les gardes explicites contrôlent `error != OK`, `not FileAccess.file_exists(staging_path)`.

- **Effets de bord :** Les effets visibles sont `var error := ResourceSaver.save(`.

## 35. Vérifier l’artefact staged

> **[VSC] Relecture typée — Ne pas saisir.**

```gdscript
func verify_staged(
    path: String,
    expected_type: StringName
) -> ContentArtifactResult:
    var loaded := ResourceLoader.load(path)

    if loaded == null:
        return ContentArtifactResult.failed(
            &"staged_resource_unreadable"
        )

    if not loaded.is_class(expected_type):
        return ContentArtifactResult.failed(
            &"unexpected_resource_type"
        )

    var digest := FileAccess.get_sha256(path)
    if digest.is_empty():
        return ContentArtifactResult.failed(
            &"artifact_digest_failed"
        )

    return ContentArtifactResult.accepted(
        loaded,
        digest
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** L’artefact est rouvert par Godot, son type est contrôlé et son empreinte calculée.

- **Persistance et restauration :** Une source valide peut encore révéler une erreur de compilateur ou de sérialisation ; cette vérification protège la promotion.

- **Rôle précis du bloc :** Le bloc expose `verify_staged()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `verify_staged(path: String, expected_type: StringName) -> ContentArtifactResult`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ContentArtifactResult.failed(`, `ContentArtifactResult.accepted(`.

- **Invariants protégés :** Les gardes explicites contrôlent `loaded == null`, `not loaded.is_class(expected_type)`, `digest.is_empty()`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 36. Synchroniser EditorFileSystem

> **[VSC] Rafraîchissement différé — Ne pas saisir.**

```gdscript
func refresh_editor_paths(
    paths: PackedStringArray
) -> Error:
    var editor_fs := EditorInterface.get_resource_filesystem()

    if editor_fs.is_importing() or editor_fs.is_scanning():
        return ERR_BUSY

    for path: String in paths:
        editor_fs.update_file(path)

    editor_fs.reimport_files(paths)
    return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** Le service refuse un nouveau scan ou import pendant une opération active. `reimport_files()` traite ensuite les sources ciblées.

- **Rôle précis du bloc :** `update_file()` actualise les informations de fichier ; L’appelant programme une nouvelle tentative après `ERR_BUSY`. Le bloc expose `refresh_editor_paths()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `refresh_editor_paths(paths: PackedStringArray) -> Error`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ERR_BUSY`, `OK`.

- **Invariants protégés :** Les gardes explicites contrôlent `editor_fs.is_importing() or editor_fs.is_scanning()`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 37. Importeur personnalisé

> **[VSC] Squelette `EditorImportPlugin` — Ne pas saisir.**

```gdscript
@tool
extends EditorImportPlugin

func _get_importer_name() -> String:
    return "asteria.quest_source"

func _get_visible_name() -> String:
    return "Asteria Quest Source"

func _get_recognized_extensions() -> PackedStringArray:
    return PackedStringArray(["aquest"])

func _get_save_extension() -> String:
    return "tres"

func _get_resource_type() -> String:
    return "QuestDefinition"

func _get_format_version() -> int:
    return 1
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** L’identité technique de l’importeur est stable et distincte du nom visible. La version de format augmente lors d’un changement incompatible des artefacts importés.

- **Rôle précis du bloc :** Les extensions reconnues sont fermées. Le bloc expose `_get_importer_name()`, `_get_visible_name()`, `_get_recognized_extensions()`, `_get_save_extension()`, `_get_resource_type()`, `_get_format_version()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `_get_importer_name() -> String`, `_get_visible_name() -> String`, `_get_recognized_extensions() -> PackedStringArray`, `_get_save_extension() -> String`, `_get_resource_type() -> String`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `"asteria.quest_source"`, `"Asteria Quest Source"`, `PackedStringArray(["aquest"])`, `"tres"`, `"QuestDefinition"`, `1`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 38. Implémenter `_import()`

> **[VSC] Import contrôlé — Ne pas saisir.**

```gdscript
func _import(
    source_file: String,
    save_path: String,
    options: Dictionary,
    platform_variants: Array[String],
    gen_files: Array[String]
) -> Error:
    var preparation := _pipeline.prepare_single(
        source_file,
        options
    )

    if not preparation.is_publishable():
        _write_import_report(
            source_file,
            preparation.report
        )
        return ERR_INVALID_DATA

    var artifact: QuestDefinition = preparation.artifact
    return ResourceSaver.save(
        artifact,
        save_path + "." + _get_save_extension()
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** L’importeur délègue aux mêmes règles que le dock et retourne un code `Error`.

- **Résultat attendu :** Il produit une définition de conception vers le chemin fourni par l’éditeur ; il ne touche ni à une quête active ni au dépôt narratif runtime.

- **Rôle précis du bloc :** Le bloc expose `_import()` et montre son traitement complet ou son squelette contractuel.

- **Paramètres et types importants :** Les déclarations visibles sont `artifact: QuestDefinition`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `_import(source_file: String, save_path: String, options: Dictionary, platform_variants: Array[String], gen_files: Array[String]) -> Error`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ERR_INVALID_DATA`, `ResourceSaver.save(`.

- **Invariants protégés :** Les gardes explicites contrôlent `not preparation.is_publishable()`.

- **Effets de bord :** Les effets visibles sont `return ResourceSaver.save(`.

## 39. Import parallèle prudent

> **[VSC] Déclaration de sûreté — Ne pas saisir.**

```gdscript
func _can_import_threaded() -> bool:
    return false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** `false` est le défaut sûr si le pipeline utilise un cache mutable, une bibliothèque non thread-safe ou l’interface d’éditeur. Les signatures documentées sont `_can_import_threaded() -> bool`.

- **Dépendances et ports utilisés :** Passer à `true` exige que toute la chaîne d’import supporte des appels concurrents et indépendants.

- **Rôle précis du bloc :** Le bloc expose `_can_import_threaded()` et montre son traitement complet ou son squelette contractuel.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `false`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 40. Reconstruction incrémentale

> **[VSC] Décision par empreinte — Ne pas saisir.**

```gdscript
func needs_rebuild(
    entry: ContentManifestEntry,
    current_source_hash: String,
    tool_version: String
) -> bool:
    if entry.source_sha256 != current_source_hash:
        return true
    if entry.tool_version != tool_version:
        return true
    if not FileAccess.file_exists(entry.artifact_path):
        return true

    return FileAccess.get_sha256(
        entry.artifact_path
    ) != entry.artifact_sha256
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le contenu est reconstruit si la source, l’outil ou l’artefact diffère du manifeste. La date de modification n’est pas une preuve suffisante, car elle varie selon les copies et certains outils la préservent. Le bloc expose `needs_rebuild()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `needs_rebuild(entry: ContentManifestEntry, current_source_hash: String, tool_version: String) -> bool`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `true`, `FileAccess.get_sha256(`.

- **Invariants protégés :** Les gardes explicites contrôlent `entry.source_sha256 != current_source_hash`, `entry.tool_version != tool_version`, `not FileAccess.file_exists(entry.artifact_path)`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 41. Invalidation transitive

> **[VSC] Propagation des changements — Ne pas saisir.**

```gdscript
func expand_dirty_set(
    initial: Array[StringName],
    graph: ContentDependencyGraph
) -> Array[StringName]:
    var dirty := {}
    var queue: Array[StringName] = initial.duplicate()

    while not queue.is_empty():
        var current := queue.pop_front()
        if dirty.has(current):
            continue

        dirty[current] = true
        for dependent: StringName in graph.dependents_of(current):
            queue.append(dependent)

    var result: Array[StringName] = []
    result.assign(dirty.keys())
    result.sort()
    return result
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Un changement invalide les artefacts qui en dépendent directement ou indirectement. Les gardes explicites contrôlent `dirty.has(current)`.

- **Rôle précis du bloc :** Le dictionnaire sert d’ensemble de visite, puis le tri garantit le même ordre de reconstruction pour un graphe identique. Le bloc expose `expand_dirty_set()` et montre son traitement complet ou son squelette contractuel.

- **Paramètres et types importants :** Les déclarations visibles sont `queue: Array[StringName]`, `result: Array[StringName]`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `expand_dirty_set(initial: Array[StringName], graph: ContentDependencyGraph) -> Array[StringName]`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `result`.

- **Effets de bord :** Les effets visibles sont `queue.append(dependent)`.

## 42. Aperçu sans publication

> **[VSC] Résumé des effets — Ne pas saisir.**

```gdscript
class_name ContentPreview
extends RefCounted

var receipt_id: StringName
var source_fingerprint: String
var added: PackedStringArray
var changed: PackedStringArray
var removed: PackedStringArray
var blocking_issues: Array[ContentIssue]

func can_be_confirmed() -> bool:
    return (
        blocking_issues.is_empty()
        and not source_fingerprint.is_empty()
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** L’aperçu liste les ajouts, changements et suppressions sans les appliquer.

- **Déterminisme et idempotence :** Une empreinte source et l’absence de blocage sont nécessaires. La commande finale revérifie cette empreinte avant le commit.

- **Rôle précis du bloc :** Le bloc définit `ContentPreview` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Paramètres et types importants :** Les déclarations visibles sont `receipt_id: StringName`, `source_fingerprint: String`, `added: PackedStringArray`, `changed: PackedStringArray`, `removed: PackedStringArray`, `blocking_issues: Array[ContentIssue]`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `can_be_confirmed() -> bool`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `(`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 43. Confirmation avec empreinte fraîche

> **[VSC] Commande de publication — Ne pas saisir.**

```gdscript
func publish(
    command: PublishContentCommand
) -> PublishResult:
    var preview := _preview_store.get(
        command.receipt_id
    )

    if preview == null or not preview.can_be_confirmed():
        return PublishResult.rejected(
            &"preview_not_publishable"
        )

    var current_fingerprint := _fingerprints.for_paths(
        command.source_paths
    )

    if current_fingerprint != preview.source_fingerprint:
        return PublishResult.rejected(
            &"sources_changed_after_preview"
        )

    return _transaction_committer.commit(
        preview.transaction
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** Le reçu identifie un aperçu contrôlé, mais une seconde empreinte protège la fenêtre entre prévisualisation et confirmation.

- **Rôle précis du bloc :** Une source modifiée force un nouvel aperçu. Le bloc expose `publish()` et montre son traitement complet ou son squelette contractuel.

- **Effets de bord :** Le committer reçoit une transaction complète. Les effets visibles sont `return _transaction_committer.commit(`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `publish(command: PublishContentCommand) -> PublishResult`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `PublishResult.rejected(`, `_transaction_committer.commit(`.

- **Invariants protégés :** Les gardes explicites contrôlent `preview == null or not preview.can_be_confirmed()`, `current_fingerprint != preview.source_fingerprint`.

## 44. Undo/redo ou transaction de fichiers

`EditorUndoRedoManager` convient aux propriétés de ressources et aux nœuds connus de l’éditeur. Il ne constitue pas une transaction générale pour des fichiers externes, des suppressions multiples ou un manifeste.

La règle pratique est : objet édité dans une scène ou une ressource ouverte, undo/redo ; lot de fichiers canoniques, transaction préparée ; cache dérivé, reconstruction ; source auteur, modification explicite et revue Git avant migration.

## 45. Migration de sources en lot

> **[VSC] Préparation sans écrasement — Ne pas saisir.**

```gdscript
func prepare_migration(
    paths: PackedStringArray,
    target_version: int
) -> SourceMigrationPlan:
    var plan := SourceMigrationPlan.new()

    for path: String in paths:
        var read := _reader.read_json(path)
        if not read.is_ok():
            plan.add_issue(
                path,
                &"source_unreadable"
            )
            continue

        var migrated := _migrator.migrate(
            read.document,
            target_version
        )
        if not migrated.is_ok():
            plan.add_issue(path, migrated.reason)
            continue

        plan.add_candidate(
            path,
            migrated.document,
            read.sha256
        )

    return plan
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** La migration produit des candidats liés aux empreintes originales.

- **Limites et réserves :** Aucun fichier n’est écrasé pendant la préparation.

- **Persistance et restauration :** La publication vérifie que chaque source est restée identique et conserve une restauration.

- **Rôle précis du bloc :** Le bloc expose `prepare_migration()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `prepare_migration(paths: PackedStringArray, target_version: int) -> SourceMigrationPlan`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `plan`.

- **Invariants protégés :** Les gardes explicites contrôlent `not read.is_ok()`, `not migrated.is_ok()`.

- **Effets de bord :** Les effets visibles sont `plan.add_issue(`, `plan.add_issue(path, migrated.reason)`, `plan.add_candidate(`.

## 46. Localisation et assets

> **[VSC] Validation croisée — Ne pas saisir.**

```gdscript
func validate_presentation_refs(
    document: Dictionary,
    locales: LocaleCatalog,
    assets: AssetCatalog
) -> Array[ContentIssue]:
    var issues: Array[ContentIssue] = []

    var title_key := StringName(
        document.get("title_key", "")
    )
    if not locales.has_key(title_key):
        issues.append(
            ContentIssueFactory.blocking(
                &"missing_locale_key",
                str(title_key)
            )
        )

    var icon_id := StringName(
        document.get("icon_id", "")
    )
    if not icon_id.is_empty() and not assets.has_id(icon_id):
        issues.append(
            ContentIssueFactory.error(
                &"missing_asset_id",
                str(icon_id)
            )
        )

    return issues
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La définition référence une clé de localisation et une identité d’asset, pas un chemin fragile. La politique peut distinguer une clé indispensable d’une icône optionnelle. Le bloc expose `validate_presentation_refs()` et montre son traitement complet ou son squelette contractuel.

- **Persistance et restauration :** Les catalogues utilisés sont des snapshots de validation.

- **Paramètres et types importants :** Les déclarations visibles sont `issues: Array[ContentIssue]`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `validate_presentation_refs(document: Dictionary, locales: LocaleCatalog, assets: AssetCatalog) -> Array[ContentIssue]`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `issues`.

- **Invariants protégés :** Les gardes explicites contrôlent `not locales.has_key(title_key)`, `not icon_id.is_empty() and not assets.has_id(icon_id)`.

- **Effets de bord :** Les effets visibles sont `issues.append(`.

## 47. Sécurité des chemins

> **[VSC] Résolution dans une racine — Ne pas saisir.**

```gdscript
func resolve_target(
    relative_path: String
) -> ContentPathResult:
    if relative_path.is_absolute_path():
        return ContentPathResult.rejected(
            &"absolute_path_forbidden"
        )

    if ".." in relative_path.split("/"):
        return ContentPathResult.rejected(
            &"parent_segment_forbidden"
        )

    var normalized := relative_path.simplify_path()
    var extension := normalized.get_extension().to_lower()

    if extension not in ["json", "tres", "res"]:
        return ContentPathResult.rejected(
            &"extension_not_allowed"
        )

    return ContentPathResult.accepted(
        "res://data/" + normalized
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Invariants protégés :** Le pipeline refuse les chemins absolus, les segments parents et les extensions hors liste. Les gardes explicites contrôlent `relative_path.is_absolute_path()`, `".." in relative_path.split("/")`, `extension not in ["json", "tres", "res"]`.

- **Organisation des fichiers :** La normalisation ne remplace pas la politique de racine. L’appelant ne peut pas viser `addons`, `project.godot` ou un dossier utilisateur arbitraire.

- **Rôle précis du bloc :** Le bloc expose `resolve_target()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `resolve_target(relative_path: String) -> ContentPathResult`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ContentPathResult.rejected(`, `ContentPathResult.accepted(`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 48. IA limitée aux brouillons

> **[VSC] Port de génération — Ne pas saisir.**

```gdscript
class_name ContentDraftGeneratorPort
extends RefCounted

func generate_draft(
    request: ContentDraftRequest
) -> ContentDraftResult:
    return ContentDraftResult.failed(
        &"not_implemented"
    )

class_name GenerateQuestDraftCommand
extends RefCounted

var template_id: StringName
var constraints: Dictionary
var destination: String = "res://data_src/drafts/"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** Le port retourne un brouillon et ne connaît aucune commande de publication.

- **Organisation des fichiers :** La destination est une racine dédiée hors du contenu canonique.

- **Rôle précis du bloc :** Les contraintes sont validées avant l’appel. Le bloc définit `ContentDraftGeneratorPort`, `GenerateQuestDraftCommand` dérivé de `RefCounted` et rend visibles les données et opérations qui composent son contrat.

- **Paramètres et types importants :** Les déclarations visibles sont `template_id: StringName`, `constraints: Dictionary`, `destination: String`.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `generate_draft(request: ContentDraftRequest) -> ContentDraftResult`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ContentDraftResult.failed(`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 49. Contrôler une sortie générée

> **[VSC] Passerelle de brouillon — Ne pas saisir.**

```gdscript
func accept_generated_text(
    raw_text: String,
    request: ContentDraftRequest
) -> ContentDraftResult:
    if raw_text.to_utf8_buffer().size() > request.max_output_bytes:
        return ContentDraftResult.rejected(
            &"generated_output_too_large"
        )

    var parser := JSON.new()
    if parser.parse(raw_text) != OK:
        return ContentDraftResult.rejected(
            &"generated_output_invalid_json"
        )

    if not parser.data is Dictionary:
        return ContentDraftResult.rejected(
            &"generated_output_not_object"
        )

    var issues := _registry.validate(
        request.content_type,
        parser.data
    )

    return ContentDraftResult.review_required(
        parser.data,
        issues
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** La taille est bornée avant l’analyse. Le bloc expose `accept_generated_text()` et montre son traitement complet ou son squelette contractuel.

- **Invariants protégés :** Une sortie syntaxiquement valide reste en état `review_required`, même si aucun blocage n’est détecté. Les gardes explicites contrôlent `raw_text.to_utf8_buffer().size() > request.max_output_bytes`, `parser.parse(raw_text) != OK`, `not parser.data is Dictionary`.

- **Organisation des fichiers :** L’IA ne reçoit ni accès au dossier canonique ni port de commit.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `accept_generated_text(raw_text: String, request: ContentDraftRequest) -> ContentDraftResult`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ContentDraftResult.rejected(`, `ContentDraftResult.review_required(`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 50. Modes Solo et Studio

### 50.1 Mode Solo

- aperçu local obligatoire
- commit Git avant migration large
- approbation par l’auteur
- rapport temporaire conservé localement

### 50.2 Mode Studio

- revue par une autre personne pour les lots sensibles
- règles de branche et pull request
- artefacts QA joints à la CI
- propriété explicite des catalogues
- promotion par un rôle autorisé

Les deux modes partagent les mêmes validateurs et formats. Le Studio ajoute séparation des responsabilités et contrôle d’accès ; il ne crée pas un second modèle de données. Le chapitre 30 détaillera l’organisation complète.
## 51. Validation headless

> **[PS] Commande depuis la racine du projet — Ne pas saisir.**

```powershell
godot --headless --path . --script res://tools/content/validate_content.gd -- --report dist/content-report.json
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** `--headless` évite l’ouverture d’une fenêtre, `--path .` fixe le projet et `--script` lance un script compatible avec la ligne de commande. Le séparateur `--` transmet les arguments suivants au code utilisateur. La commande invoque `godot` pour exécuter l’opération indiquée par le bloc.

- **Paramètres et options importants :** Les options visibles sont `--headless`, `--path`, `--script`, `--`, `--report`.

- **Résultat attendu :** L’appel doit terminer avec le code de sortie prévu par le script ou l’outil appelé ; tout code non nul reste un échec à diagnostiquer.

- **Limites du contrat visible :** Le bloc décrit uniquement les éléments littéraux affichés ; il ne définit aucune étape supplémentaire hors de cette structure.

## 52. Attendre les imports

> **[PS] Import du projet — Ne pas saisir.**

```powershell
godot --headless --path . --import
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** `--import` démarre l’éditeur, attend la fin des imports puis quitte. Cette étape est utile avant un contrôle qui dépend d’artefacts importés.

- **Effets de bord :** Elle ne remplace pas la validation des sources.

- **Rôle précis du bloc :** La commande invoque `godot` pour exécuter l’opération indiquée par le bloc.

- **Paramètres et options importants :** Les options visibles sont `--headless`, `--path`, `--import`.

- **Résultat attendu :** L’appel doit terminer avec le code de sortie prévu par le script ou l’outil appelé ; tout code non nul reste un échec à diagnostiquer.

## 53. Analyse syntaxique seule

> **[PS] Vérification du script — Ne pas saisir.**

```powershell
godot --headless --path . --script res://tools/content/validate_content.gd --check-only
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** `--check-only` demande l’analyse du script sans exécuter son traitement normal. La commande reste une réserve documentaire tant qu’elle n’est pas lancée avec le binaire de référence sur le projet matérialisé.

- **Rôle précis du bloc :** La commande invoque `godot` pour exécuter l’opération indiquée par le bloc.

- **Paramètres et options importants :** Les options visibles sont `--headless`, `--path`, `--script`, `--check-only`.

- **Résultat attendu :** L’appel doit terminer avec le code de sortie prévu par le script ou l’outil appelé ; tout code non nul reste un échec à diagnostiquer.

## 54. Contrat du script headless

> **[VSC] Entrée de ligne de commande — Ne pas saisir.**

```gdscript
extends SceneTree

func _init() -> void:
    var args := OS.get_cmdline_user_args()
    var options := ContentCliOptions.parse(args)

    if not options.is_valid():
        printerr("Arguments de validation invalides")
        quit(2)
        return

    var result := ContentBatchValidator.new().run(options)
    quit(0 if result.is_publishable() else 1)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** Le script hérite de `SceneTree`, lit les arguments utilisateur et termine avec un code explicite. Le bloc expose `_init()` et montre son traitement complet ou son squelette contractuel.

- **Limites et réserves :** `0` signifie publiable, `1` signale un contenu non publiable et `2` une invocation incorrecte.

- **Dépendances et ports utilisés :** Le rapport contient les détails.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `_init() -> void`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `var result := ContentBatchValidator.new().run(options)`.

- **Invariants protégés :** Les gardes explicites contrôlent `not options.is_valid()`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 55. Politique Git

> **[LECTURE] Règles de versionnement — Ne pas saisir.**

```text
À versionner
- data_src/**
- data/** canoniques
- manifests/**
- migrations/**
- addons/asteria_content_tools/**

À reconstruire ou ignorer
- .godot/imported/**
- .godot/asteria_cache/**
- user://content_staging/**
- rapports locaux temporaires
- réponses brutes contenant des secrets
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Résultat attendu :** Le dépôt conserve ce qui permet de reproduire et revoir le contenu. La lecture doit conserver l’ordre et les correspondances explicites entre les éléments listés, sans inventer de relation absente du schéma.

- **Rôle précis du bloc :** Les caches internes de Godot et le staging ne sont pas des sources. Le bloc compare ou énumère `À versionner`, `- data_src/**`, `- data/** canoniques`, `- manifests/**`, `- migrations/**`, `- addons/asteria_content_tools/**`.

- **Invariants protégés :** Un artefact lourd exige une politique explicite, par exemple Git LFS, sans devenir une définition métier.

- **Déroulement ou instructions importantes :** L’extrait commence par `À versionner` et se termine par `- réponses brutes contenant des secrets` ; les lignes intermédiaires doivent être lues dans cet ordre.

## 56. Observabilité minimale

Chaque exécution produit au minimum un identifiant de reçu, l’empreinte des sources, la version de l’outil, le nombre de documents, les problèmes par sévérité, les chemins staged, les chemins promus et le résultat final.

Les messages du dock restent actionnables : code stable, fichier, pointeur, raison et suggestion. Le chapitre 28 définira les corrélations, journaux structurés et mécanismes de reproductibilité détaillés.

## 57. Frontières avec le runtime

> **[LECTURE] Matrice d’autorité — Ne pas saisir.**

```text
Outil de contenu          Autorité runtime
----------------------    --------------------------------
compile QuestDefinition → narration possède QuestRuntimeState
compile ItemDefinition  → inventaire possède ItemInstance
compile LawDefinition   → politique possède les lois promulguées
compile BuildingData    → domaines possèdent BuildingState
compile SpeciesProfile  → écologie possède populations et réserves
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** Le pipeline produit des définitions et catalogues.

- **Résultat attendu :** Il ne crée pas de personnage vivant, ne crédite pas une monnaie, ne rend pas de verdict et n’achève pas de quête. La lecture doit conserver l’ordre et les correspondances explicites entre les éléments listés, sans inventer de relation absente du schéma.

- **Frontières d’autorité :** Toute mutation runtime passe encore par les commandes propriétaires.

- **Rôle précis du bloc :** Le schéma fait circuler le traitement de `Outil de contenu          Autorité runtime` vers `compile SpeciesProfile  → écologie possède populations et réserves`.

- **Déroulement ou instructions importantes :** Les transitions visibles sont `compile QuestDefinition → narration possède QuestRuntimeState`, `compile ItemDefinition  → inventaire possède ItemInstance`, `compile LawDefinition   → politique possède les lois promulguées`, `compile BuildingData    → domaines possèdent BuildingState`, `compile SpeciesProfile  → écologie possède populations et réserves`.

## 58. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

Les dix cas suivants sont bloquants pour un outil ou un pipeline destiné à la publication.

### 58.1 Écrire le contenu canonique directement depuis un bouton

**Symptôme :** Le clic contourne l’aperçu, la validation globale et la transaction de fichiers.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
func _on_publish_pressed() -> void:
    var file := FileAccess.open(
        "res://data/quests.json",
        FileAccess.WRITE
    )
    file.store_string(%Editor.text)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** **Pourquoi cet exemple est fautif :** L’interface écrit dans le fichier final sans reçu, sans sauvegarde et sans contrôle d’empreinte.

- **Rôle précis du bloc :** Le bloc expose `_on_publish_pressed()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `_on_publish_pressed() -> void`.

- **Effets de bord :** Les effets visibles sont `var file := FileAccess.open(`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
func _on_publish_pressed() -> void:
    publish_requested.emit(&"current_preview")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Effets de bord :** **Pourquoi la correction fonctionne :** Le bouton corrigé émet une intention liée à un aperçu déjà calculé. Les effets visibles sont `publish_requested.emit(&"current_preview")`.

- **Invariants protégés :** Le service applicatif reste seul responsable de la transaction.

- **Rôle précis du bloc :** Le bloc expose `_on_publish_pressed()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `_on_publish_pressed() -> void`.

### 58.2 Modifier une scène sans undo/redo

**Symptôme :** La scène paraît enregistrée et l’auteur ne peut pas annuler la mutation.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
func add_marker(root: Node) -> void:
    root.add_child(Marker3D.new())
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Pourquoi cet exemple est fautif :** Le nœud est ajouté hors de l’historique de l’éditeur et peut être perdu ou impossible à retirer proprement. Le bloc expose `add_marker()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `add_marker(root: Node) -> void`.

- **Effets de bord :** Les effets visibles sont `root.add_child(Marker3D.new())`.

- **Déroulement ou instructions importantes :** L’extrait commence par `func add_marker(root: Node) -> void:` et se termine par `root.add_child(Marker3D.new())` ; les lignes intermédiaires doivent être lues dans cet ordre.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
func add_marker(root: Node) -> void:
    var marker := Marker3D.new()
    var undo_redo := EditorInterface.get_editor_undo_redo()

    undo_redo.create_action(
        "Ajouter un marqueur",
        UndoRedo.MERGE_DISABLE,
        root
    )
    undo_redo.add_do_method(root, "add_child", marker)
    undo_redo.add_undo_method(root, "remove_child", marker)
    undo_redo.add_do_reference(marker)
    undo_redo.commit_action()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** **Pourquoi la correction fonctionne :** La correction enregistre l’ajout, le retrait et la référence dans l’historique associé à la scène. Les signatures documentées sont `add_marker(root: Node) -> void`.

- **Rôle précis du bloc :** Le bloc expose `add_marker()` et montre son traitement complet ou son squelette contractuel.

- **Effets de bord :** Les effets visibles sont `undo_redo.add_do_method(root, "add_child", marker)`, `undo_redo.add_undo_method(root, "remove_child", marker)`, `undo_redo.add_do_reference(marker)`, `undo_redo.commit_action()`.

- **Déroulement ou instructions importantes :** L’extrait commence par `func add_marker(root: Node) -> void:` et se termine par `undo_redo.commit_action()` ; les lignes intermédiaires doivent être lues dans cet ordre.

### 58.3 Utiliser le chemin comme identité

**Symptôme :** Un déplacement de fichier change l’identité logique et casse les références.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
var quest_id := StringName(
    source_file.get_file().get_basename()
)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Pourquoi cet exemple est fautif :** Le nom du fichier est une information d’organisation, pas une identité métier permanente.

- **Déroulement ou instructions importantes :** L’extrait commence par `var quest_id := StringName(` et se termine par `)` ; les lignes intermédiaires doivent être lues dans cet ordre.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `var quest_id := StringName(`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var quest_id := StringName(document["quest_id"])

if not StableIdPolicy.is_valid(quest_id):
    return ERR_INVALID_DATA
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** **Pourquoi la correction fonctionne :** Le champ corrigé est un identifiant stable soumis à une politique de forme indépendante du chemin et du titre.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ERR_INVALID_DATA`.

- **Invariants protégés :** Les gardes explicites contrôlent `not StableIdPolicy.is_valid(quest_id)`.

- **Déroulement ou instructions importantes :** L’extrait commence par `var quest_id := StringName(document["quest_id"])` et se termine par `return ERR_INVALID_DATA` ; les lignes intermédiaires doivent être lues dans cet ordre.

### 58.4 Exécuter une méthode fournie par les données

**Symptôme :** Le document externe devient du code arbitraire et contourne les stratégies autorisées.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
var method_name: StringName = document["validator"]
return call(method_name, document)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** **Pourquoi cet exemple est fautif :** Un auteur ou un fichier compromis peut choisir une méthode inattendue dans le processus d’édition.

- **Paramètres et types importants :** Les déclarations visibles sont `method_name: StringName`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `call(method_name, document)`.

- **Déroulement ou instructions importantes :** L’extrait commence par `var method_name: StringName = document["validator"]` et se termine par `return call(method_name, document)` ; les lignes intermédiaires doivent être lues dans cet ordre.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var type_id := StringName(document["content_type"])
return _validator_registry.validate(
    type_id,
    document
)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** **Pourquoi la correction fonctionne :** Le type corrigé sélectionne uniquement un validateur déjà enregistré ; un type inconnu produit un problème bloquant.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `_validator_registry.validate(`.

- **Déroulement ou instructions importantes :** L’extrait commence par `var type_id := StringName(document["content_type"])` et se termine par `)` ; les lignes intermédiaires doivent être lues dans cet ordre.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

### 58.5 Mélanger sources, artefacts et caches

**Symptôme :** Un cache dérivé peut être révisé comme une source ou versionné par erreur.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
const OUTPUT_ROOT := "res://data_src/generated_and_cache/"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Organisation des fichiers :** **Pourquoi cet exemple est fautif :** Une seule racine efface la différence entre ce qui est édité, publié et reconstructible.

- **Rôle précis du bloc :** Le bloc fixe les identifiants et valeurs nommées `OUTPUT_ROOT`.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `const OUTPUT_ROOT := "res://data_src/generated_and_cache/"`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
const SOURCE_ROOT := "res://data_src/"
const ARTIFACT_ROOT := "res://data/"
const CACHE_ROOT := "res://.godot/asteria_cache/"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** **Pourquoi la correction fonctionne :** Les trois constantes expriment des responsabilités séparées et empêchent le cache de devenir une autorité.

- **Rôle précis du bloc :** Le bloc fixe les identifiants et valeurs nommées `SOURCE_ROOT`, `ARTIFACT_ROOT`, `CACHE_ROOT`.

- **Déroulement ou instructions importantes :** L’extrait commence par `const SOURCE_ROOT := "res://data_src/"` et se termine par `const CACHE_ROOT := "res://.godot/asteria_cache/"` ; les lignes intermédiaires doivent être lues dans cet ordre.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

### 58.6 Introduire l’heure dans l’empreinte

**Symptôme :** Deux machines produisent des résultats différents pour une source identique.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
document["built_at"] = Time.get_datetime_string_from_system()
return str(document.hash())
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres et types importants :** **Pourquoi cet exemple est fautif :** L’heure et `Dictionary.hash()` ne constituent pas une représentation canonique reproductible du contenu.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `str(document.hash())`.

- **Déroulement ou instructions importantes :** L’extrait commence par `document["built_at"] = Time.get_datetime_string_from_system()` et se termine par `return str(document.hash())` ; les lignes intermédiaires doivent être lues dans cet ordre.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var normalized := CanonicalValue.normalize(document)
return fingerprint(normalized)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Persistance et restauration :** **Pourquoi la correction fonctionne :** La correction retire les données volatiles et calcule SHA-256 sur une sérialisation ordonnée.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `fingerprint(normalized)`.

- **Déroulement ou instructions importantes :** L’extrait commence par `var normalized := CanonicalValue.normalize(document)` et se termine par `return fingerprint(normalized)` ; les lignes intermédiaires doivent être lues dans cet ordre.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

### 58.7 Écrire directement dans le fichier final

**Symptôme :** Une interruption peut laisser un artefact partiel sans restauration fiable.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
return ResourceSaver.save(
    resource,
    target_path
)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** **Pourquoi cet exemple est fautif :** La sauvegarde remplace l’artefact canonique avant relecture, empreinte ou copie de secours.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `ResourceSaver.save(`.

- **Effets de bord :** Les effets visibles sont `return ResourceSaver.save(`.

- **Déroulement ou instructions importantes :** L’extrait commence par `return ResourceSaver.save(` et se termine par `)` ; les lignes intermédiaires doivent être lues dans cet ordre.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var staged := _stage_writer.save(
    resource,
    receipt_id
)

if not staged.is_verified():
    return PublishResult.failed(
        &"staging_verification_failed"
    )

return _transaction_committer.promote(staged)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Persistance et restauration :** **Pourquoi la correction fonctionne :** La correction sauvegarde, recharge et vérifie le staged avant une promotion contrôlée.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `PublishResult.failed(`, `_transaction_committer.promote(staged)`.

- **Invariants protégés :** Les gardes explicites contrôlent `not staged.is_verified()`.

- **Déroulement ou instructions importantes :** L’extrait commence par `var staged := _stage_writer.save(` et se termine par `return _transaction_committer.promote(staged)` ; les lignes intermédiaires doivent être lues dans cet ordre.

### 58.8 Promouvoir automatiquement une sortie IA

**Symptôme :** Une réponse plausible devient une définition canonique sans approbation.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
var draft := await _ai.generate(prompt)
_publish_json(draft)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** **Pourquoi cet exemple est fautif :** La sortie générée contourne le schéma, le rapport de validation et la décision humaine.

- **Déroulement ou instructions importantes :** L’extrait commence par `var draft := await _ai.generate(prompt)` et se termine par `_publish_json(draft)` ; les lignes intermédiaires doivent être lues dans cet ordre.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `var draft := await _ai.generate(prompt)`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var draft := await _draft_port.generate_draft(
    request
)

return _review_queue.enqueue(
    draft,
    validation_report
)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déterminisme et idempotence :** **Pourquoi la correction fonctionne :** La sortie corrigée entre dans une file de revue et ne peut être publiée sans approbation liée à son empreinte.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `_review_queue.enqueue(`.

- **Déroulement ou instructions importantes :** L’extrait commence par `var draft := await _draft_port.generate_draft(` et se termine par `)` ; les lignes intermédiaires doivent être lues dans cet ordre.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

### 58.9 Relancer un scan pendant une importation

**Symptôme :** Un appel réentrant peut bloquer le flux d’import ou produire des callbacks imbriqués.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
EditorInterface.get_resource_filesystem().scan()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Pourquoi cet exemple est fautif :** Le code ignore l’état courant du système de fichiers éditorial.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

- **Instruction principale :** L’instruction exacte est `EditorInterface.get_resource_filesystem().scan()`.

- **Symboles manipulés :** Les symboles visibles sont `EditorInterface`, `get_resource_filesystem`, `scan`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var fs := EditorInterface.get_resource_filesystem()

if fs.is_importing() or fs.is_scanning():
    return ERR_BUSY

fs.scan()
return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Valeur de retour ou code d’échec :** **Pourquoi la correction fonctionne :** La correction retourne `ERR_BUSY` et permet une nouvelle tentative après la fin de l’opération active. Les branches de sortie visibles renvoient `ERR_BUSY`, `OK`.

- **Invariants protégés :** Les gardes explicites contrôlent `fs.is_importing() or fs.is_scanning()`.

- **Déroulement ou instructions importantes :** L’extrait commence par `var fs := EditorInterface.get_resource_filesystem()` et se termine par `return OK` ; les lignes intermédiaires doivent être lues dans cet ordre.

- **Limites du contrat visible :** Le contrat documenté se limite aux classes, champs, fonctions, gardes et appels présents dans l’extrait ; aucun comportement non écrit n’est supposé.

### 58.10 Faire du plugin une autorité runtime

**Symptôme :** Le jeu dépend de l’éditeur et une action de production peut modifier une partie.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
func grant_reward(
    wallet_id: StringName,
    amount: int
) -> void:
    EconomyService.credit(wallet_id, amount)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Effets de bord :** **Pourquoi cet exemple est fautif :** Le plugin écrit directement dans le système économique au lieu de produire une définition.

- **Rôle précis du bloc :** Le bloc expose `grant_reward()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `grant_reward(wallet_id: StringName, amount: int) -> void`.

- **Déroulement ou instructions importantes :** L’extrait commence par `func grant_reward(` et se termine par `EconomyService.credit(wallet_id, amount)` ; les lignes intermédiaires doivent être lues dans cet ordre.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
func compile_reward_definition(
    source: Dictionary
) -> RewardDefinition:
    return RewardDefinitionCompiler.new().compile(
        source
    )
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Frontières d’autorité :** **Pourquoi la correction fonctionne :** Le compilateur corrigé ne crée qu’un artefact de conception ; l’économie reste propriétaire de toute écriture runtime.

- **Rôle précis du bloc :** Le bloc expose `compile_reward_definition()` et montre son traitement complet ou son squelette contractuel.

- **Responsabilités des classes ou fonctions :** Les signatures documentées sont `compile_reward_definition(source: Dictionary) -> RewardDefinition`.

- **Valeur de retour ou code d’échec :** Les branches de sortie visibles renvoient `RewardDefinitionCompiler.new().compile(`.

- **Effets de bord :** Aucune écriture, émission de signal ou mutation externe n’apparaît dans l’extrait ; le résultat est calculé puis retourné.

## 59. Checklist d’acceptation

Avant d’accepter un outil ou un pipeline :

- le plugin se charge et se décharge symétriquement ;
- aucun module runtime ne dépend de `addons/asteria_content_tools` ;
- les mutations de scène ou ressource utilisent undo/redo ou marquent le document ;
- les sources, artefacts et caches possèdent des racines distinctes ;
- les identifiants, références et versions de schéma sont validés ;
- les stratégies exécutables proviennent d’un registre fermé ;
- le graphe de dépendances est acyclique et ordonné déterministement ;
- les empreintes reposent sur une sérialisation canonique ;
- l’aperçu et le reçu correspondent aux sources actuelles ;
- les écritures passent par staging, relecture, sauvegarde et promotion ;
- le système de fichiers n’est pas rescanné pendant un import actif ;
- les sorties IA restent des brouillons soumis à revue ;
- la même logique est appelable depuis l’éditeur et le mode headless ;
- les limites runtime et plateforme restent explicitement déclarées.

## 60. Références techniques officielles

Les contrats de ce chapitre s’appuient sur la documentation stable de Godot :

- [`@tool` et exécution dans l’éditeur](https://docs.godotengine.org/en/stable/tutorials/plugins/running_code_in_the_editor.html) ;
- [`EditorPlugin`](https://docs.godotengine.org/en/stable/classes/class_editorplugin.html) ;
- [`EditorInspectorPlugin`](https://docs.godotengine.org/en/stable/classes/class_editorinspectorplugin.html) ;
- [`EditorImportPlugin`](https://docs.godotengine.org/en/stable/classes/class_editorimportplugin.html) ;
- [`EditorUndoRedoManager`](https://docs.godotengine.org/en/stable/classes/class_editorundoredomanager.html) ;
- [`ResourceSaver`](https://docs.godotengine.org/en/stable/classes/class_resourcesaver.html) ;
- [`EditorFileSystem`](https://docs.godotengine.org/en/stable/classes/class_editorfilesystem.html) ;
- [Godot en ligne de commande](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html).

La référence du projet reste Godot `4.7.1-stable`. Les exemples éditoriaux devront être confirmés avec ce binaire avant intégration dans un Starter Kit exécutable.

## 61. Décisions retenues pour Project Asteria

`Project Asteria` adopte un plugin de production isolé sous `addons/asteria_content_tools`, sans dépendance depuis le runtime. Le dock, l’Inspector et les importeurs appellent un noyau commun de préparation et de validation.

Les sources auteur, artefacts canoniques et caches dérivés sont séparés. Les identifiants stables, versions de schéma, graphes acycliques, sérialisation canonique et empreintes SHA-256 rendent les lots comparables. Un aperçu validé produit un reçu ; la publication revérifie l’empreinte avant une transaction staged.

Les mutations de scènes et ressources ouvertes utilisent l’annulation de l’éditeur. Les lots de fichiers utilisent sauvegardes et promotion contrôlée. Une sortie IA ne dépasse jamais le statut de brouillon avant validation et approbation humaine.

Les chapitres 14 à 25 restent propriétaires de tous les états runtime. Le pipeline ne produit que les définitions, catalogues, manifestes et reçus qu’ils consomment.
