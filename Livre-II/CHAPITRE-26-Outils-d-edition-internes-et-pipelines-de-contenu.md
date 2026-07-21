---
title: "Livre II — Chapitre 26 : Outils d’édition internes et pipelines de contenu"
id: "DOC-L2-CH26"
status: "reviewed"
version: "1.0.1"
lang: "fr-FR"
book: "Livre II"
chapter: 26
last-verified: "2026-07-21T14:38:26+02:00"
audit-status: "complete"
audit-date: "2026-07-21T14:38:26+02:00"
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

- **Rôle précis du bloc :** Les sources auteur sont modifiables et revues. Les artefacts canoniques sont les définitions approuvées que le runtime peut charger. Les caches peuvent être supprimés puis reconstruits ; ils ne doivent jamais devenir l’unique détenteur d’une information métier.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Responsabilités des classes ou fonctions :** Le fichier `plugin.gd` orchestre uniquement le cycle de vie de l’extension. La validation et la publication sont réutilisables sans interface. Les accès disque restent dans l’infrastructure, tandis que les contrôles Godot résident dans la présentation.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Dépendances et ports utilisés :** La section `plugin` rend l’extension détectable. Le champ `script` pointe vers l’`EditorPlugin` chargé à l’activation. La version appartient à l’outil de production et doit figurer dans les reçus lorsque son comportement influence les artefacts.

- **Rôle précis du bloc :** Le bloc présente une structure de données littérale dont les clés et valeurs constituent le contrat à relire.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Frontières d’autorité :** `@tool` autorise l’exécution dans l’éditeur. `Engine.is_editor_hint()` isole le chemin éditorial si le script peut aussi être instancié ailleurs. Une méthode outil ne doit jamais muter une partie ni appeler directement une autorité runtime.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `refresh_preview()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `refresh_preview()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `void` ; branches visibles : `queue_redraw()`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `not Engine.is_editor_hint()` avant de poursuivre le traitement.

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

- **Frontières d’autorité :** Chaque enregistrement possède son retrait miroir. L’exemple utilise l’API de dock historique encore disponible ; une implémentation strictement alignée sur `EditorDock` emploie `add_dock()` et `remove_dock()` avec le même invariant de nettoyage.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `_enter_tree()`, `_exit_tree()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `_enter_tree()`, `_exit_tree()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `_dock: Control`, `_inspector_plugin: EditorInspectorPlugin`, `_import_plugin: EditorImportPlugin`, `void:
      _dock`, `void:
          _dock.queue_free`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `void`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `_import_plugin != null`, `_inspector_plugin != null`, `_dock != null` avant de poursuivre le traitement.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `_dock.queue_free()`.

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

- **Dépendances et ports utilisés :** La garde échoue explicitement si le module est chargé hors éditeur. Le package runtime ne doit dépendre ni de ce plugin, ni de ses scènes d’interface, ni de ses adaptateurs de fichiers. Les artefacts publiés restent utilisables sans l’extension.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `_ready()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `_ready()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `void:
      _connect_editor_signals`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `void` ; branches visibles : `_connect_editor_signals()`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `not Engine.is_editor_hint()` avant de poursuivre le traitement.

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

- **Effets de bord :** Le dock émet des intentions et ne réalise aucun accès disque. Le service applicatif calcule l’aperçu et le reçu. Le bouton de publication ne peut donc pas construire arbitrairement une liste de fichiers à écrire.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `_ready()`, `_on_preview_pressed()`, `_on_publish_pressed()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `_ready()`, `_on_preview_pressed()`, `_on_publish_pressed()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `void:
  func _on_preview_pressed`, `void:
  func _on_publish_pressed`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `void`.

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

- **Dépendances et ports utilisés :** `READY_TO_PUBLISH` est la seule porte d’activation du bouton. Une validation échouée, un aperçu obsolète ou une opération en cours ne peut pas lancer la promotion. L’interface reflète une décision applicative plutôt qu’une déduction visuelle.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `can_publish()`, `set_state()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `can_publish()`, `set_state()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `state: DockState`, `bool:
  func set_state`, `next_state: DockState`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool`, `void` ; branches visibles : `state == DockState.READY_TO_PUBLISH`.

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

- **Paramètres et types importants :** `_can_handle()` ferme le périmètre à un type connu. `_parse_begin()` ajoute un contrôle sans remplacer les propriétés natives. L’action transmet un chemin de ressource au service applicatif et ne corrige jamais silencieusement l’objet sélectionné.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `_can_handle()`, `_parse_begin()`, `_request_validation()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `_can_handle()`, `_parse_begin()`, `_request_validation()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool`, `void` ; branches visibles : `object is QuestDefinition`.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `ContentToolBus.validation_requested.emit(resource_path)`.

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

- **Effets de bord :** L’action conserve l’ancienne et la nouvelle valeur dans l’historique approprié. La ressource fournie comme contexte aide l’éditeur à sélectionner l’historique. `commit_action()` exécute l’opération et marque normalement le document comme modifié.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `rename_entry()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `rename_entry()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `previous_id: StringName`, `resource: Resource, next_id`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `void`.

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

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `update_generated_preview()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `update_generated_preview()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `node: Node3D, mesh`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `void`.

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

- **Frontières d’autorité :** Un diagnostic possède un code stable, un fichier et un pointeur interne. Le texte aide l’auteur ; `code` sert au filtrage et à l’automatisation. Seule la sévérité `BLOCKING` interdit mécaniquement la publication.

- **Rôle précis du bloc :** Le bloc définit `ContentIssue` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `ContentIssue` et les fonctions `blocks_publication()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `severity: Severity`, `code: StringName`, `path: String`, `pointer: String`, `message: String`, `suggestion: String`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `severity == Severity.BLOCKING`.

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

- **Déterminisme et idempotence :** Le rapport est une photographie du contrôle. Son empreinte relie la décision aux sources exactes. La copie profonde empêche le panneau d’interface de modifier une collection réutilisée par la commande de publication.

- **Rôle précis du bloc :** Le bloc définit `ContentValidationReport` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `ContentValidationReport` et les fonctions `is_publishable()`, `duplicate_detached()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `source_fingerprint: String`, `issues: Array[ContentIssue]`, `checked_paths: PackedStringArray`, `bool:
  func duplicate_detached`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool`, `ContentValidationReport` ; branches visibles : `false`, `not source_fingerprint.is_empty()`, `copy`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `issue.blocks_publication()` avant de poursuivre le traitement.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `copy.source_fingerprint = source_fingerprint`, `copy.issues = issues.duplicate(true)`, `copy.checked_paths = checked_paths.duplicate()`.

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

- **Paramètres et types importants :** La donnée ne fournit ni chemin de script, ni classe, ni nom de méthode. Elle choisit uniquement un identifiant présent dans un registre construit par le code. Un type inconnu produit un blocage explicite.

- **Rôle précis du bloc :** Le bloc définit `ContentValidatorRegistry` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `ContentValidatorRegistry` et les fonctions `register()`, `validate()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `Error`, `Array[ContentIssue]` ; branches visibles : `ERR_INVALID_PARAMETER`, `ERR_ALREADY_EXISTS`, `OK`, `[`, `validator.validate(document)`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `type_id.is_empty() or validator == null`, `_validators.has(type_id)`, `validator == null` avant de poursuivre le traitement.

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

- **Invariants protégés :** Chaque couche suppose la précédente valide. Une référence n’est pas résolue avant que son champ soit reconnu comme chaîne. Cet ordre limite les cascades de diagnostics secondaires et localise mieux la cause initiale.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Invariants protégés :** Le chemin reste dans la racine source et la taille est bornée avant analyse. Le résultat distingue un refus de politique d’un échec d’entrée-sortie. Une implémentation optimisée pourra lire la taille sans charger tout le fichier.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `read_source()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `read_source()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `path: String`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `ContentReadResult` ; branches visibles : `ContentReadResult.rejected(`, `ContentReadResult.rejected(&"source_too_large")`, `ContentReadResult.failed(`, `ContentReadResult.accepted(`.

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

- **Invariants protégés :** Les migrations travaillent sur une copie détachée. Une version future est refusée afin qu’un ancien outil ne réécrive pas un document qu’il ne comprend pas. Le candidat final est entièrement validé avant toute promotion.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `prepare_document()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `prepare_document()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `ContentPreparationResult` ; branches visibles : `ContentPreparationResult.rejected(`, `_validate_candidate(candidate)`.

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

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `validate_reference()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `validate_reference()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `source_path: String,`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `Array[ContentIssue]` ; branches visibles : `[`, `[]`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `target_id.is_empty()`, `not catalog.contains(target_id)` avant de poursuivre le traitement.

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

- **Effets de bord :** Le graphe décrit les dépendances logiques entre définitions. Les nœuds autonomes existent même sans arête. Les collections internes restent privées afin qu’une étape de présentation ne puisse pas altérer le plan de compilation.

- **Rôle précis du bloc :** Le bloc définit `ContentDependencyGraph` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `ContentDependencyGraph` et les fonctions `add_node()`, `add_dependency()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `_edges: Dictionary[StringName, Array]`, `content_id: StringName`, `void:
          _edges[content_id]`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `void`, `Error` ; branches visibles : `ERR_ALREADY_EXISTS`, `OK`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `not _edges.has(content_id)`, `depends_on in _edges[content_id]` avant de poursuivre le traitement.

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

- **Responsabilités des classes ou fonctions :** Rencontrer un nœud `ACTIVE` révèle une arête de retour. Le chemin retourné rend le diagnostic actionnable. Le pipeline n’invente jamais un ordre lorsque le graphe contient une boucle.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `find_cycle()`.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `state: VisitState`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `Array[StringName]` ; branches visibles : `stack.slice(start) + [dependency]`, `nested`, `[]`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `state == VisitState.ACTIVE`, `state == VisitState.UNSEEN`, `not nested.is_empty()` avant de poursuivre le traitement.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `stack.append(node)`.

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

- **Invariants protégés :** Le tri des candidats prêts fixe un ordre reproductible lorsque plusieurs solutions sont valides. Un tableau vide signale un cycle ou une incohérence. Cette stabilité évite des artefacts différents entre deux machines.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `topological_order()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `topological_order()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `ready: Array[StringName]`, `result: Array[StringName]`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `Array[StringName]` ; branches visibles : `result if result.size() == remaining.size() else []`.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `ready.append(content_id)`, `result.append(current)`, `ready.append(dependent)`.

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

- **Rôle précis du bloc :** Les clés de dictionnaire sont ordonnées, tandis que les tableaux conservent leur ordre métier. La sérialisation finale doit imposer UTF-8 et une convention stable pour les nombres. Une date de build ne participe jamais à la valeur canonique.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `CanonicalValue` et les fonctions `normalize()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `keys: Array`, `items: Array`, `value: Variant`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `Variant`, `bool` ; branches visibles : `str(a) < str(b)`, `ordered`, `items`, `value`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `value is Dictionary`, `value is Array` avant de poursuivre le traitement.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `items.append(normalize(item))`.

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

- **Déterminisme et idempotence :** L’empreinte dépend uniquement du document normalisé. Elle permet de vérifier qu’un aperçu correspond encore aux sources. Elle ne constitue ni une signature d’auteur ni une preuve suffisante de provenance.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `fingerprint()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `fingerprint()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `document: Dictionary`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `String` ; branches visibles : `context.finish().hex_encode()`.

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

- **Déterminisme et idempotence :** Le manifeste relie identité, source, artefact et empreintes. Ses entrées sont triées avant sérialisation. La version de l’outil explique quel compilateur a produit le lot sans rendre ce compilateur nécessaire à l’exécution du jeu.

- **Rôle précis du bloc :** Le bloc présente une structure de données littérale dont les clés et valeurs constituent le contrat à relire.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Déterminisme et idempotence :** La provenance décrit la génération et l’approbation. Elle ne remplace ni le schéma ni la revue. Le manifeste ne copie aucun secret, jeton ou échange complet ; l’approbation porte sur l’empreinte exacte de la source examinée.

- **Rôle précis du bloc :** Le bloc présente une structure de données littérale dont les clés et valeurs constituent le contrat à relire.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Déterminisme et idempotence :** Le reçu relie validation, compilation et publication. `matches()` empêche de publier avec un rapport devenu obsolète. Un horodatage peut être ajouté pour le suivi, mais reste hors de l’empreinte déterministe.

- **Rôle précis du bloc :** Le bloc définit `PipelineReceipt` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `PipelineReceipt` et les fonctions `matches()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `receipt_id: StringName`, `source_fingerprint: String`, `artifact_fingerprint: String`, `tool_version: String`, `issue_counts: Dictionary[StringName, int]`, `published_paths: PackedStringArray`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `source_fingerprint == report.source_fingerprint`.

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

- **Invariants protégés :** `prepare()` ne touche pas aux artefacts canoniques. Il découvre, lit, valide et planifie. Les phases de staging, vérification et promotion commencent seulement après une confirmation explicite.

- **Rôle précis du bloc :** Le bloc définit `ContentPipeline` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `ContentPipeline` et les fonctions `prepare()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `ContentBuildPlan` ; branches visibles : `ContentBuildPlan.rejected(report)`, `_compiler.prepare_plan(`.

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

- **Valeur de retour ou code d’échec :** Le compilateur reçoit un document déjà validé et retourne une nouvelle définition. Il ne consulte ni singleton, ni horloge, ni système de fichiers. Cette pureté simplifie la comparaison des sorties et prépare les tests du chapitre 27.

- **Rôle précis du bloc :** Le bloc définit `QuestContentCompiler` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `QuestContentCompiler` et les fonctions `compile()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `source: Dictionary`, `QuestDefinition:
          source[`.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `result.quest_id = StringName(source["quest_id"])`, `result.title_key = StringName(source["title_key"])`, `result.objectives = _compile_objectives(`, `result.consequences = _compile_consequences(`.

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

- **Persistance et restauration :** Le staging reste hors du chemin canonique. L’ancien artefact reçoit une sauvegarde ciblée avant remplacement. La documentation décrit les garanties réelles du système de fichiers et ne promet pas une atomicité universelle.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Déterminisme et idempotence :** La transaction décrit toutes les écritures et suppressions avant le commit. Deux opérations ne peuvent pas viser le même chemin. Le committer revérifiera les empreintes et préparera les sauvegardes avant la première promotion.

- **Rôle précis du bloc :** Le bloc définit `StagedFileTransaction` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `StagedFileTransaction` et les fonctions `validate()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `writes: Array[StagedWrite]`, `deletes: PackedStringArray`, `source_fingerprint: String`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `Error` ; branches visibles : `ERR_INVALID_DATA`, `ERR_ALREADY_EXISTS`, `OK`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `source_fingerprint.is_empty()`, `targets.has(write.target_path)` avant de poursuivre le traitement.

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

- **Valeur de retour ou code d’échec :** `ResourceSaver.save()` retourne un code `Error` qui doit être consommé. Le chemin est borné à la zone de staging. La simple existence ne suffit pas : l’étape suivante recharge et contrôle l’artefact.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `save_staged()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `save_staged()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `error != OK`, `not FileAccess.file_exists(staging_path)` avant de poursuivre le traitement.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `var error := ResourceSaver.save(`.

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

- **Déterminisme et idempotence :** L’artefact est rouvert par Godot, son type est contrôlé et son empreinte calculée. Une source valide peut encore révéler une erreur de compilateur ou de sérialisation ; cette vérification protège la promotion.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `verify_staged()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `verify_staged()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `path: String,`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `ContentArtifactResult` ; branches visibles : `ContentArtifactResult.failed(`, `ContentArtifactResult.accepted(`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `loaded == null`, `not loaded.is_class(expected_type)`, `digest.is_empty()` avant de poursuivre le traitement.

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

- **Invariants protégés :** Le service refuse un nouveau scan ou import pendant une opération active. `update_file()` actualise les informations de fichier ; `reimport_files()` traite ensuite les sources ciblées. L’appelant programme une nouvelle tentative après `ERR_BUSY`.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `refresh_editor_paths()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `refresh_editor_paths()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `paths: PackedStringArray`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `Error` ; branches visibles : `ERR_BUSY`, `OK`.

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

- **Dépendances et ports utilisés :** L’identité technique de l’importeur est stable et distincte du nom visible. La version de format augmente lors d’un changement incompatible des artefacts importés. Les extensions reconnues sont fermées.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `_get_importer_name()`, `_get_visible_name()`, `_get_recognized_extensions()`, `_get_save_extension()`, `_get_resource_type()`, `_get_format_version()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `_get_importer_name()`, `_get_visible_name()`, `_get_recognized_extensions()`, `_get_save_extension()`, `_get_resource_type()`, `_get_format_version()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `String:
  func _get_visible_name`, `String:
  func _get_recognized_extensions`, `PackedStringArray:
  func _get_save_extension`, `String:
  func _get_resource_type`, `String:
  func _get_format_version`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `String`, `PackedStringArray`, `int` ; branches visibles : `"asteria.quest_source"`, `"Asteria Quest Source"`, `PackedStringArray(["aquest"])`, `"tres"`, `"QuestDefinition"`.

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

- **Valeur de retour ou code d’échec :** L’importeur délègue aux mêmes règles que le dock et retourne un code `Error`. Il produit une définition de conception vers le chemin fourni par l’éditeur ; il ne touche ni à une quête active ni au dépôt narratif runtime.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `_import()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `_import()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `artifact: QuestDefinition`, `source_file: String,`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `not preparation.is_publishable()` avant de poursuivre le traitement.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `return ResourceSaver.save(`.

## 39. Import parallèle prudent

> **[VSC] Déclaration de sûreté — Ne pas saisir.**

```gdscript
func _can_import_threaded() -> bool:
    return false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** `false` est le défaut sûr si le pipeline utilise un cache mutable, une bibliothèque non thread-safe ou l’interface d’éditeur. Passer à `true` exige que toute la chaîne d’import supporte des appels concurrents et indépendants.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `_can_import_threaded()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `_can_import_threaded()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `false`.

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

- **Rôle précis du bloc :** Le contenu est reconstruit si la source, l’outil ou l’artefact diffère du manifeste. La date de modification n’est pas une preuve suffisante, car elle varie selon les copies et certains outils la préservent.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `needs_rebuild()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `true`, `FileAccess.get_sha256(`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `entry.source_sha256 != current_source_hash`, `entry.tool_version != tool_version`, `not FileAccess.file_exists(entry.artifact_path)` avant de poursuivre le traitement.

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

- **Invariants protégés :** Un changement invalide les artefacts qui en dépendent directement ou indirectement. Le dictionnaire sert d’ensemble de visite, puis le tri garantit le même ordre de reconstruction pour un graphe identique.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `expand_dirty_set()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `expand_dirty_set()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `queue: Array[StringName]`, `result: Array[StringName]`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `Array[StringName]` ; branches visibles : `result`.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `queue.append(dependent)`.

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

- **Déterminisme et idempotence :** L’aperçu liste les ajouts, changements et suppressions sans les appliquer. Une empreinte source et l’absence de blocage sont nécessaires. La commande finale revérifie cette empreinte avant le commit.

- **Rôle précis du bloc :** Le bloc définit `ContentPreview` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `ContentPreview` et les fonctions `can_be_confirmed()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `receipt_id: StringName`, `source_fingerprint: String`, `added: PackedStringArray`, `changed: PackedStringArray`, `removed: PackedStringArray`, `blocking_issues: Array[ContentIssue]`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `bool` ; branches visibles : `(`.

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

- **Déterminisme et idempotence :** Le reçu identifie un aperçu contrôlé, mais une seconde empreinte protège la fenêtre entre prévisualisation et confirmation. Une source modifiée force un nouvel aperçu. Le committer reçoit une transaction complète.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `publish()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `publish()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `command: PublishContentCommand`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `PublishResult` ; branches visibles : `PublishResult.rejected(`, `_transaction_committer.commit(`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `preview == null or not preview.can_be_confirmed()`, `current_fingerprint != preview.source_fingerprint` avant de poursuivre le traitement.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `return _transaction_committer.commit(`.

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

- **Déterminisme et idempotence :** La migration produit des candidats liés aux empreintes originales. Aucun fichier n’est écrasé pendant la préparation. La publication vérifie que chaque source est restée identique et conserve une restauration.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `prepare_migration()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `prepare_migration()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `paths: PackedStringArray,`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `SourceMigrationPlan` ; branches visibles : `plan`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `not read.is_ok()`, `not migrated.is_ok()` avant de poursuivre le traitement.

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

- **Persistance et restauration :** La définition référence une clé de localisation et une identité d’asset, pas un chemin fragile. La politique peut distinguer une clé indispensable d’une icône optionnelle. Les catalogues utilisés sont des snapshots de validation.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `validate_presentation_refs()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `validate_presentation_refs()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `issues: Array[ContentIssue]`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `Array[ContentIssue]` ; branches visibles : `issues`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `not locales.has_key(title_key)`, `not icon_id.is_empty() and not assets.has_id(icon_id)` avant de poursuivre le traitement.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `issues.append(`.

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

- **Invariants protégés :** Le pipeline refuse les chemins absolus, les segments parents et les extensions hors liste. La normalisation ne remplace pas la politique de racine. L’appelant ne peut pas viser `addons`, `project.godot` ou un dossier utilisateur arbitraire.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `resolve_target()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `resolve_target()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `ContentPathResult` ; branches visibles : `ContentPathResult.rejected(`, `ContentPathResult.accepted(`.

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

- **Valeur de retour ou code d’échec :** Le port retourne un brouillon et ne connaît aucune commande de publication. La destination est une racine dédiée hors du contenu canonique. Les contraintes sont validées avant l’appel.

- **Rôle précis du bloc :** Le bloc définit `ContentDraftGeneratorPort`, `GenerateQuestDraftCommand` et expose son contrat minimal visible.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les classes `ContentDraftGeneratorPort`, `GenerateQuestDraftCommand` et les fonctions `generate_draft()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `template_id: StringName`, `constraints: Dictionary`, `destination: String`.

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

- **Invariants protégés :** La taille est bornée avant l’analyse. Une sortie syntaxiquement valide reste en état `review_required`, même si aucun blocage n’est détecté. L’IA ne reçoit ni accès au dossier canonique ni port de commit.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `accept_generated_text()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `accept_generated_text()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `ContentDraftResult` ; branches visibles : `ContentDraftResult.rejected(`, `ContentDraftResult.review_required(`.

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

- **Rôle précis du bloc :** `--headless` évite l’ouverture d’une fenêtre, `--path .` fixe le projet et `--script` lance un script compatible avec la ligne de commande. Le séparateur `--` transmet les arguments suivants au code utilisateur.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

## 52. Attendre les imports

> **[PS] Import du projet — Ne pas saisir.**

```powershell
godot --headless --path . --import
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Effets de bord :** `--import` démarre l’éditeur, attend la fin des imports puis quitte. Cette étape est utile avant un contrôle qui dépend d’artefacts importés. Elle ne remplace pas la validation des sources.

- **Rôle précis du bloc :** Le bloc présente une commande complète et l’ordre exact de ses arguments.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

## 53. Analyse syntaxique seule

> **[PS] Vérification du script — Ne pas saisir.**

```powershell
godot --headless --path . --script res://tools/content/validate_content.gd --check-only
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limites et réserves :** `--check-only` demande l’analyse du script sans exécuter son traitement normal. La commande reste une réserve documentaire tant qu’elle n’est pas lancée avec le binaire de référence sur le projet matérialisé.

- **Rôle précis du bloc :** Le bloc présente une commande complète et l’ordre exact de ses arguments.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Point complémentaire 4 :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

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

- **Dépendances et ports utilisés :** Le script hérite de `SceneTree`, lit les arguments utilisateur et termine avec un code explicite. `0` signifie publiable, `1` signale un contenu non publiable et `2` une invocation incorrecte. Le rapport contient les détails.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `_init()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `_init()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `void` ; branches visibles : `var result := ContentBatchValidator.new().run(options)`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `not options.is_valid()` avant de poursuivre le traitement.

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

- **Résultat attendu :** Le dépôt conserve ce qui permet de reproduire et revoir le contenu. Les caches internes de Godot et le staging ne sont pas des sources. Un artefact lourd exige une politique explicite, par exemple Git LFS, sans devenir une définition métier.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Frontières d’autorité :** Le pipeline produit des définitions et catalogues. Il ne crée pas de personnage vivant, ne crédite pas une monnaie, ne rend pas de verdict et n’achève pas de quête. Toute mutation runtime passe encore par les commandes propriétaires.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Résultat attendu :** Le lecteur doit retrouver la structure, les clés ou la commande dans l’ordre montré, sans interpréter ce bloc de référence comme une preuve d’exécution runtime.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `_on_publish_pressed()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `_on_publish_pressed()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `void`.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `var file := FileAccess.open(`.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
func _on_publish_pressed() -> void:
    publish_requested.emit(&"current_preview")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Effets de bord :** **Pourquoi la correction fonctionne :** Le bouton corrigé émet une intention liée à un aperçu déjà calculé. Le service applicatif reste seul responsable de la transaction.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `_on_publish_pressed()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `_on_publish_pressed()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `void`.

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

- **Rôle précis du bloc :** **Pourquoi cet exemple est fautif :** Le nœud est ajouté hors de l’historique de l’éditeur et peut être perdu ou impossible à retirer proprement.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `add_marker()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `root: Node`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `void`.

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

- **Responsabilités des classes ou fonctions :** **Pourquoi la correction fonctionne :** La correction enregistre l’ajout, le retrait et la référence dans l’historique associé à la scène.

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `add_marker()`.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `root: Node`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `void`.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `undo_redo.commit_action()`.

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

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Point complémentaire 3 :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var quest_id := StringName(document["quest_id"])

if not StableIdPolicy.is_valid(quest_id):
    return ERR_INVALID_DATA
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Dépendances et ports utilisés :** **Pourquoi la correction fonctionne :** Le champ corrigé est un identifiant stable soumis à une politique de forme indépendante du chemin et du titre.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose branches visibles : `ERR_INVALID_DATA`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `not StableIdPolicy.is_valid(quest_id)` avant de poursuivre le traitement.

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

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `method_name: StringName`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose branches visibles : `call(method_name, document)`.

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

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose branches visibles : `_validator_registry.validate(`.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

### 58.5 Mélanger sources, artefacts et caches

**Symptôme :** Un cache dérivé peut être révisé comme une source ou versionné par erreur.

**Exemple fautif :**

> **[LECTURE] Contre-exemple — Ne pas saisir.**

```gdscript
const OUTPUT_ROOT := "res://data_src/generated_and_cache/"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis du bloc :** **Pourquoi cet exemple est fautif :** Une seule racine efface la différence entre ce qui est édité, publié et reconstructible.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Point complémentaire 3 :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose branches visibles : `str(document.hash())`.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

**Exemple corrigé :**

> **[LECTURE] Correction — Ne pas saisir.**

```gdscript
var normalized := CanonicalValue.normalize(document)
return fingerprint(normalized)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsabilités des classes ou fonctions :** **Pourquoi la correction fonctionne :** La correction retire les données volatiles et calcule SHA-256 sur une sérialisation ordonnée.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose branches visibles : `fingerprint(normalized)`.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose branches visibles : `ResourceSaver.save(`.

- **Effets de bord :** Les mutations ou appels observables montrés par l’extrait incluent `return ResourceSaver.save(`.

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

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose branches visibles : `PublishResult.failed(`, `_transaction_committer.promote(staged)`.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `not staged.is_verified()` avant de poursuivre le traitement.

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

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose branches visibles : `_review_queue.enqueue(`.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Déroulement ou instructions importantes :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Point complémentaire 3 :** Le traitement suit l’ordre écrit dans le bloc ; aucune étape implicite ne doit être ajoutée entre les gardes, la préparation et le résultat montré.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Valeur de retour ou code d’échec :** **Pourquoi la correction fonctionne :** La correction retourne `ERR_BUSY` et permet une nouvelle tentative après la fin de l’opération active.

- **Rôle précis du bloc :** Le bloc présente une structure de référence et les relations explicites entre ses éléments.

- **Invariants protégés :** Les gardes visibles contrôlent notamment `fs.is_importing() or fs.is_scanning()` avant de poursuivre le traitement.

- **Limites et réserves :** L’extrait reste une structure pédagogique relue statiquement ; son intégration doit encore respecter les réserves runtime déclarées dans le chapitre.

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

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `grant_reward()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `grant_reward()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `void`.

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

- **Rôle précis du bloc :** Le bloc montre le traitement porté par `compile_reward_definition()`.

- **Responsabilités des classes ou fonctions :** Le bloc déclare les fonctions `compile_reward_definition()`; leurs responsabilités restent limitées aux opérations explicitement visibles dans l’extrait.

- **Paramètres et types importants :** Les déclarations typées visibles comprennent `source: Dictionary`.

- **Valeur de retour ou code d’échec :** Le contrat de sortie expose types annoncés : `RewardDefinition` ; branches visibles : `RewardDefinitionCompiler.new().compile(`.

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
