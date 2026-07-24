---
title: "Livre III — Chapitre 24 : Interface utilisateur"
id: "DOC-L3-CH24"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 24
last-verified: "2026-07-24T20:12:01+02:00"
audit-status: "complete"
audit-date: "2026-07-24T20:12:01+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-24.md"
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

# Interface utilisateur

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH24`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+

## 1. Rôle du chapitre

Une interface utilisateur transforme des données et des possibilités d’action en éléments visibles, ordonnés et manipulables. Elle doit indiquer ce que le joueur peut comprendre ou demander sans décider elle-même des règles de combat, d’inventaire, de quête, de sauvegarde ou d’économie.

Le chapitre construit un système visuel réutilisable : design tokens, thèmes Godot, composants, écrans, navigation clavier-souris-manette, adaptation aux ratios, échelle d’interface, localisation et campagne de tests multi-résolution. Il ne prétend pas que ces scènes ou captures existent déjà.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
chapter_role:
  input: typed_domain_state_and_user_intent
  transformation: reusable_ui_components_and_screen_composition
  output: themed_screens_with_test_matrix
  authority: presentation_and_request_only
  evidence_level: static_review
  runtime_claims: none
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** les systèmes du Livre II fournissent un état déjà validé et des commandes autorisées.
- **Transformation :** la couche UI compose les données en contrôles, panneaux, listes, modales et indications.
- **Autorité :** un clic ou une activation émet une demande ; il ne modifie jamais directement l’état métier.
- **Sortie :** chaque écran repose sur un thème, des composants et des contrats de navigation versionnés.
- **Preuve :** les exemples sont relus statiquement sans revendiquer rendu, focus ou performance exécutés.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura définir un design system, organiser les tokens, créer un `Theme`, construire des composants réutilisables et assembler des menus, HUD, inventaires et fenêtres avec les nœuds `Control` et `Container`.

Il saura également configurer le focus, restaurer la navigation après une modale, adapter l’interface aux ratios et zones sûres, préparer la pseudo-localisation, tester plusieurs périphériques et enregistrer des résultats reproductibles sans confondre structure documentaire et preuve runtime.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
learning_outcomes:
  system: [tokens, theme, type_variations, components]
  layout: [anchors, offsets, containers, minimum_size]
  screens: [main_menu, hud, inventory, pause, modal]
  input: [mouse, keyboard, gamepad, focus, prompts]
  adaptation: [content_scale, aspect_ratios, safe_area, localization]
  validation: [test_matrix, visual_regression, acceptance_gate]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Système :** les décisions visuelles communes sont centralisées au lieu d’être copiées dans chaque scène.
- **Disposition :** ancres, offsets, tailles minimales et conteneurs répondent à des besoins distincts.
- **Écrans :** les scènes pilotes couvrent les structures fréquentes sans créer une scène unique par cas.
- **Entrées :** la même intention reste accessible avec souris, clavier et manette.
- **Validation :** les matrices et captures restent des livrables à matérialiser dans le build.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les fichiers `.tres`, `.tscn`, scripts et manifests sont des modèles pédagogiques : ils ne prouvent ni la lisibilité, ni la navigation complète, ni l’absence d’élément hors écran.

Aucun thème, composant, écran, police, jeu d’icônes, capture, test de périphérique ou benchmark n’est déclaré produit. Les tailles, durées, marges et seuils numériques restent des candidats à confirmer sur les résolutions et matériels ciblés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
evidence_level:
  chapter: static_review
  design_system_materialized: false
  godot_theme_created: false
  reusable_components_created: false
  pilot_screens_created: false
  keyboard_gamepad_navigation_tested: false
  multi_resolution_campaign_executed: false
  localization_and_rtl_tested: false
  runtime_measurements: false
  pdf_produced: false
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** la méthode, les contrats et les extraits sont contrôlés comme documentation.
- **Design :** aucun fichier de tokens, thème ou bibliothèque de composants n’est déclaré existant.
- **Navigation :** focus initial, voisins, retour et restauration restent à exécuter.
- **Adaptation :** ratios, zones sûres, pseudo-localisation et RTL restent à inspecter.
- **Publication :** le PDF du Livre III demeure différé jusqu’à la fin du Livre.

## 4. Frontières avec les chapitres voisins

Le chapitre 23 conserve la production des VFX. Le chapitre 25 approfondira l’expérience utilisateur, les profils d’accessibilité visuelle, la charge cognitive et les tests avec des personnes. Le chapitre 27 conservera les animations faciales et le chapitre 28 l’import universel des assets.

Le Livre II reste propriétaire des entrées gameplay, des données, des commandes, des inventaires, des quêtes et de la sauvegarde. Le présent chapitre affiche ces systèmes et leur transmet des requêtes typées ; il ne duplique ni leurs invariants ni leurs transactions.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
ownership:
  chapter_23: vfx_assets_and_visual_feedback
  chapter_24: ui_visual_system_components_and_screen_layouts
  chapter_25: ux_accessibility_profiles_and_user_testing
  chapter_28: global_asset_import_and_reimport
  book_ii_chapter_06: input_intentions_and_remapping
  book_ii_domain_chapters: authoritative_state_and_commands
  invariant: ui_never_commits_domain_state_directly
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **VFX :** un effet peut accompagner un bouton ou une notification sans définir le composant.
- **Interface :** le chapitre possède le thème, les composants et la composition des écrans.
- **UX :** les protocoles d’évaluation humaine et profils avancés restent au chapitre suivant.
- **Gameplay :** l’interface consomme des ports de lecture et de commande définis par les systèmes.
- **Invariant :** aucun callback visuel n’écrit directement dans une agrégation métier.

## 5. Pilote UI de Project Asteria

Le pilote `AST-UI-PILOT-CORE-SHELL-001` regroupe un menu principal, un HUD d’exploration, un écran d’inventaire, une pause et une modale de confirmation. Ce lot couvre assez de structures pour qualifier le design system sans disperser la production.

Le pilote s’appuie sur des données simulées ou des adaptateurs de lecture. Les valeurs montrées n’attestent pas que le combat, l’inventaire ou la sauvegarde ont été connectés dans un projet exécutable.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
asteria_ui_pilot:
  id: AST-UI-PILOT-CORE-SHELL-001
  theme_id: AST-UI-THEME-CORE-001
  screens:
    - AST-UI-SCREEN-MAIN-MENU-001
    - AST-UI-SCREEN-HUD-EXPLORATION-001
    - AST-UI-SCREEN-INVENTORY-001
    - AST-UI-SCREEN-PAUSE-001
    - AST-UI-MODAL-CONFIRM-001
  input_profiles: [mouse_keyboard, gamepad]
  aspect_profiles: ["16:9", "16:10", "21:9", "4:3"]
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pilote :** un identifiant stable regroupe la campagne sans confondre les écrans individuels.
- **Thème :** les scènes partagent une ressource commune plutôt que des overrides locaux.
- **Entrées :** souris-clavier et manette constituent les profils initiaux obligatoires.
- **Ratios :** la matrice inclut des formes larges et compactes, pas seulement le 16:9.
- **Réserve :** aucun écran ni test n’est annoncé comme créé.

## 6. Partir de la fonction de chaque information

Avant de dessiner un panneau, il faut écrire ce que le joueur doit savoir, décider ou confirmer. La position, le contraste et la persistance dépendent de cette fonction.

Une donnée purement décorative peut disparaître en profil compact ; une alerte critique conserve une forme textuelle ou iconographique redondante.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
information_hierarchy:
  critical: [danger, validation_required, irreversible_action]
  primary: [current_goal, health_state, selected_item]
  secondary: [context_hint, comparison, recent_change]
  decorative: [ambient_frame, ornamental_divider]
  rule: critical_information_survives_compact_profiles
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Critique :** une information qui modifie immédiatement la décision du joueur reste visible.
- **Primaire :** l’état utilisé fréquemment occupe une zone stable et identifiable.
- **Secondaire :** les détails contextuels peuvent être repliés ou retardés.
- **Décoratif :** les ornements sont les premiers supprimés en espace ou budget contraint.
- **Règle :** le profil compact ne retire jamais le signal nécessaire à une action sûre.

## 7. Construire les design tokens

Les tokens nomment les décisions répétées : espacements, tailles, rayons, durées, couleurs fonctionnelles et niveaux typographiques. Ils évitent les valeurs copiées sans intention.

Un token n’est pas un pixel magique universel. Sa valeur appartient à une version et peut évoluer après les tests multi-résolution.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
ui_tokens:
  spacing: {xs: 4, sm: 8, md: 16, lg: 24, xl: 32}
  radius: {control: 6, panel: 10, modal: 14}
  typography: {caption: 14, body: 18, title: 28, display: 40}
  timing_ms: {instant: 0, quick: 120, standard: 220}
  semantic_colors: [surface, text, muted, accent, warning, danger, success]
  status: candidate_until_runtime_review
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Espacement :** une échelle courte favorise des rythmes cohérents.
- **Rayons :** les formes sont nommées par usage plutôt que recopiées par contrôle.
- **Typographie :** les niveaux expriment une hiérarchie et non une liste de tailles arbitraires.
- **Durées :** les transitions partagent des catégories, mais restent désactivables.
- **Statut :** toutes les valeurs restent candidates avant inspection réelle.

## 8. Nommer, identifier et versionner les éléments UI

Une bibliothèque maintenable distingue le nom lecteur, l’identifiant stable, le type de composant et la version. Les noms de nœuds ne remplacent pas un catalogue.

Les identifiants survivent aux renommages visuels et facilitent les captures, les journaux et les demandes de correction.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
ui_asset_identity:
  component_id: AST-UI-COMP-BUTTON-PRIMARY-001
  display_name: Bouton principal
  component_type: action_button
  version: 1.0.0
  owner: ui_team
  source_scene: res://ui/components/buttons/primary_button.tscn
  theme_variation: AsteriaPrimaryButton
  approval: pending
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identifiant :** la clé stable relie scène, audit, capture et historique.
- **Nom lecteur :** le libellé français peut évoluer sans casser les références internes.
- **Type :** la famille décrit le comportement attendu.
- **Source :** le chemin canonique sépare la scène de ses instances.
- **Approbation :** la présence du fichier ne vaut pas validation.

## 9. Séparer sources, ressources et écrans

Les fichiers de conception, polices sources, icônes et captures de revue restent distincts des ressources importées par Godot. Les scènes d’écran consomment des composants, elles ne deviennent pas leur source.

Cette séparation permet de régénérer les dérivés et d’exclure les données lourdes ou privées du build.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
ui_roots:
  production:
    tokens: docs/ui/tokens/
    sources: art/ui/sources/
    fonts: art/ui/fonts/
    icons: art/ui/icons/
    reviews: docs/ui/reviews/
  runtime:
    themes: res://ui/themes/
    components: res://ui/components/
    screens: res://ui/screens/
    presenters: res://ui/presentation/
    tests: res://ui/tests/
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Production :** les sources modifiables et décisions restent hors des scènes runtime.
- **Runtime :** les ressources importables sont organisées par responsabilité.
- **Composants :** les briques réutilisables ne sont pas enfouies dans un écran.
- **Présentation :** les adaptateurs et modèles de vue restent séparés des contrôles.
- **Tests :** les scènes de qualification disposent d’une racine explicite.

## 10. Comprendre le contrat de Control

`Control` représente un rectangle d’interface dont la taille et la position dépendent du parent, des ancres, des offsets ou du conteneur. Il reçoit aussi thème, focus et événements GUI.

Une scène UI doit rester dans une chaîne continue de `Control` lorsqu’elle attend l’héritage du thème et du layout.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
control_contract:
  geometry: rectangle
  parent_dependency: control_or_viewport
  layout_sources: [anchors, offsets, container]
  interaction: [mouse_filter, focus_mode, gui_input]
  appearance: [theme, theme_type_variation, overrides]
  invariant: layout_and_interaction_are_explicit
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Géométrie :** la zone rectangulaire détermine affichage, hitbox et disposition.
- **Parent :** le comportement change selon que le parent est un `Control` ou un `Viewport`.
- **Layout :** ancres, offsets et conteneurs ne doivent pas être combinés au hasard.
- **Interaction :** souris et focus possèdent des politiques distinctes.
- **Apparence :** le thème est hérité tant que la chaîne de contrôles n’est pas interrompue.

## 11. Choisir entre ancres et offsets

Les ancres expriment une position relative au parent ; les offsets décrivent l’écart local par rapport à ces ancres. Ils conviennent aux HUD simples attachés aux coins ou au centre.

Une ancre ne garantit pas une taille minimale et ne remplace pas un conteneur pour des listes ou formulaires complexes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
anchor_recipe:
  element: hud_status_cluster
  anchors: {left: 0.0, top: 0.0, right: 0.0, bottom: 0.0}
  offsets: {left: 24, top: 24, right: 344, bottom: 164}
  safe_area_margin: required
  minimum_size: Vector2(280, 120)
  container_parent: false
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Élément :** le groupe HUD possède une fonction et une boîte mesurable.
- **Ancres :** les quatre valeurs l’attachent au coin supérieur gauche.
- **Offsets :** les écarts définissent la taille candidate et la marge locale.
- **Zone sûre :** la marge système doit encore être ajoutée sur les plateformes concernées.
- **Limite :** une taille minimale protège le contenu sans rendre le layout universel.

## 12. Utiliser les conteneurs pour les structures complexes

Un `Container` reprend la responsabilité de placer ses enfants. Les positions manuelles des contrôles enfants seront ignorées ou recalculées lors du redimensionnement.

Les `HBoxContainer`, `VBoxContainer`, `GridContainer`, `MarginContainer`, `PanelContainer`, `ScrollContainer` et `TabContainer` couvrent la majorité des écrans de jeu.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
container_tree:
  InventoryScreen:
    MarginContainer:
      VBoxContainer:
        HeaderRow: HBoxContainer
        BodySplit: HSplitContainer
        FooterActions: HBoxContainer
  child_layout:
    horizontal: [fill, expand]
    vertical: [fill]
    stretch_ratio: candidate
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Arbre :** les responsabilités de marges, empilement et séparation restent visibles.
- **Enfants :** chaque contrôle renonce au positionnement manuel sous un conteneur.
- **Remplissage :** `fill` utilise l’espace attribué sans demander plus d’espace.
- **Expansion :** `expand` participe au partage de l’espace restant.
- **Ratio :** le partage relatif reste à vérifier avec les contenus réels.

## 13. Définir les tailles minimales et les ratios d’étirement

La taille minimale protège le contenu contre l’écrasement. Elle peut provenir du contrôle, du thème, du texte ou de `custom_minimum_size`.

Un grand minimum fixe peut toutefois empêcher l’adaptation. Les valeurs doivent être réservées aux besoins réels du composant.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
sizing_policy:
  button:
    custom_minimum_size: Vector2(180, 52)
    horizontal: fill_expand
    vertical: fill
  item_list:
    minimum_width: content_driven
    horizontal: fill_expand
    stretch_ratio: 2.0
  details_panel:
    horizontal: fill_expand
    stretch_ratio: 3.0
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Bouton :** la hauteur protège la cible et le texte sans fixer tout l’écran.
- **Liste :** la largeur minimale dépend du contenu et peut devenir scrollable.
- **Expansion :** les deux panneaux reçoivent l’espace disponible.
- **Ratio :** le détail reçoit davantage d’espace que la liste.
- **Validation :** les nombres restent candidats jusqu’aux tests de texte et de résolution.

## 14. Créer un Theme de projet

Une ressource `Theme` centralise couleurs, constantes, polices, tailles de police, icônes et `StyleBox`. Elle peut s’appliquer au projet entier ou à une branche de contrôles.

Les overrides locaux restent réservés aux exceptions documentées ; ils ne doivent pas remplacer la bibliothèque de thème.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
theme_manifest:
  id: AST-UI-THEME-CORE-001
  resource: res://ui/themes/asteria_core_theme.tres
  scope: project
  types:
    - Button
    - Label
    - PanelContainer
    - LineEdit
    - ScrollBar
  custom_project_setting: gui/theme/custom
  approval: pending
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ressource :** le fichier `.tres` devient la source runtime du style.
- **Portée :** un thème de projet réduit les divergences entre écrans.
- **Types :** les familles natives reçoivent des items cohérents.
- **Réglage :** le manifeste note le point d’application global.
- **Approbation :** le thème reste candidat tant qu’il n’est pas inspecté.

## 15. Employer les variations de type

Une variation de thème permet de créer des familles comme bouton principal, bouton dangereux ou panneau de statut sans copier toutes les propriétés.

Le nom de variation décrit une intention sémantique. `RedButton` est moins robuste que `AsteriaDangerButton`, car la couleur peut changer sans changer le rôle.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
theme_variations:
  AsteriaPrimaryButton:
    base_type: Button
    intent: main_action
  AsteriaSecondaryButton:
    base_type: Button
    intent: alternative_action
  AsteriaDangerButton:
    base_type: Button
    intent: destructive_or_irreversible_action
  AsteriaHudPanel:
    base_type: PanelContainer
    intent: persistent_status
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Base :** chaque variation hérite d’un type connu du moteur.
- **Principal :** l’action dominante reste identifiable indépendamment de la couleur.
- **Secondaire :** les choix alternatifs partagent le même contrat.
- **Danger :** les actions risquées disposent d’un style et d’une confirmation distincts.
- **HUD :** les panneaux persistants se différencient des fenêtres modales.

## 16. Organiser la typographie

La typographie doit couvrir niveaux, graisse, chiffres, caractères accentués, ponctuation et langues ciblées. Une seule police décorative ne suffit pas aux textes longs ou données numériques.

Les tailles sont liées aux tokens et à l’échelle utilisateur. Les polices et leurs licences restent qualifiées comme des assets.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
typography_roles:
  display: {token: display, use: major_screen_title}
  title: {token: title, use: panel_heading}
  body: {token: body, use: readable_content}
  caption: {token: caption, use: secondary_metadata}
  numeric: {token: body, use: aligned_values, tabular_digits: evaluate}
  fallback: [latin_extended, symbols, target_locales]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Display :** le grand titre est rare et ne remplace pas la hiérarchie complète.
- **Corps :** le texte courant privilégie la lecture plutôt que le caractère décoratif.
- **Légende :** les métadonnées secondaires restent lisibles dans les profils compacts.
- **Numérique :** les valeurs alignées peuvent nécessiter des chiffres tabulaires.
- **Repli :** les glyphes manquants et langues cibles doivent être testés.

## 17. Traiter couleurs, contrastes et états sans dépendre de la couleur seule

Le chapitre 25 approfondira les profils d’accessibilité, mais le composant doit déjà éviter une information portée uniquement par la teinte. Icône, texte, forme ou position fournissent un second canal.

Les couleurs sont nommées par fonction et testées dans les états normal, survol, focus, pressé et désactivé.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
semantic_palette:
  surface: ui_surface
  text: ui_text_primary
  accent: ui_action_primary
  warning: ui_warning
  danger: ui_danger
  success: ui_success
  redundancy:
    danger: [color, icon, label]
    selected: [color, border, state_marker]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Palette :** les noms fonctionnels survivent aux changements de direction artistique.
- **Surface :** les couches distinguent fond, panneau et contrôle.
- **Danger :** la teinte s’accompagne d’une icône et d’un libellé.
- **Sélection :** la bordure et le marqueur d’état complètent la couleur.
- **Frontière :** les seuils et profils avancés seront validés au chapitre 25.

## 18. Construire une taxonomie de composants

Les composants sont classés par responsabilité : action, saisie, information, navigation, conteneur, statut ou superposition. Cette taxonomie évite les scènes nommées seulement selon un écran.

Un composant possède des états, des entrées, des signaux et une variation de thème documentés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
component_families:
  action: [primary_button, secondary_button, icon_button]
  input: [text_field, slider, toggle, remap_row]
  information: [label_value, badge, tooltip, progress_display]
  navigation: [tab, breadcrumb, list_row]
  container: [card, panel, split_view]
  overlay: [modal, toast, context_menu]
  status: [health_bar, objective_tracker, resource_counter]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Action :** les boutons expriment une intention et un signal.
- **Saisie :** les contrôles de réglage exposent valeur, plage et validation.
- **Information :** les composants de lecture ne deviennent pas interactifs par défaut.
- **Superposition :** modales et notifications ont un cycle de vie explicite.
- **Statut :** les indicateurs persistants consomment un modèle de vue borné.

## 19. Créer un bouton d’action réutilisable

Un bouton réutilisable expose son intention et son état, puis émet un signal. Il ne connaît ni l’inventaire ni le combat.

Le texte, l’icône et le raccourci sont fournis par l’écran ou un modèle de vue. La variation de thème encode la priorité visuelle.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```gdscript
class_name AsteriaActionButton
extends Button

signal action_requested(action_id: StringName)

@export var action_id: StringName = &""
@export var require_non_empty_id: bool = true

func _ready() -> void:
    pressed.connect(_on_pressed)

func _on_pressed() -> void:
    if require_non_empty_id and action_id.is_empty():
        push_warning("AsteriaActionButton sans action_id")
        return
    action_requested.emit(action_id)
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe :** le composant reste un `Button` compatible avec thème, focus et signaux.
- **Signal :** l’écran reçoit une intention nommée plutôt qu’un effet métier direct.
- **Identifiant :** `StringName` limite les chaînes répétées et rend le contrat explicite.
- **Garde :** un identifiant obligatoire absent produit un avertissement contrôlé.
- **Effet :** le bouton n’écrit aucune donnée de domaine.

## 20. Créer une carte ou un panneau réutilisable

Une carte regroupe un titre, un contenu et des actions avec une variation de thème. Elle ne suppose pas la nature du contenu.

`PanelContainer` fournit le fond et les marges du `StyleBox`, tandis que les conteneurs internes gèrent l’organisation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
component:
  id: AST-UI-COMP-CARD-001
  root: PanelContainer
  theme_type_variation: AsteriaCard
  slots:
    header: Control
    body: Control
    footer: Control
  states: [default, selected, disabled]
  data_contract: external
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racine :** `PanelContainer` dessine le style puis dimensionne son enfant.
- **Variation :** la carte partage les marges et surfaces du thème.
- **Slots :** les zones restent génériques et remplaçables.
- **États :** la sélection et la désactivation possèdent des représentations distinctes.
- **Contrat :** les données sont fournies par le parent.

## 21. Créer une ligne de liste recyclable

Les inventaires et codex peuvent contenir de nombreuses lignes. Une ligne de liste doit pouvoir être réinitialisée, recevoir un modèle simple et signaler sélection ou activation.

Une ligne recyclée ne conserve ni focus, ni tooltip, ni état de sélection provenant de l’élément précédent.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```gdscript
class_name AsteriaListRow
extends Button

var item_id: StringName = &""

func bind(model: Dictionary) -> void:
    item_id = model.get("id", &"")
    text = str(model.get("label", ""))
    disabled = not bool(model.get("enabled", true))
    tooltip_text = str(model.get("tooltip", ""))

func reset() -> void:
    item_id = &""
    text = ""
    disabled = false
    tooltip_text = ""
    button_pressed = false
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Liaison :** le modèle reste une vue simple et non une entité métier mutable.
- **Identifiant :** la ligne conserve seulement la clé nécessaire à la requête.
- **Désactivation :** l’état interactif vient explicitement du modèle.
- **Réinitialisation :** toutes les propriétés susceptibles de fuir entre usages sont nettoyées.
- **Limite :** un pool ou une virtualisation réelle reste à matérialiser et mesurer.

## 22. Construire une modale avec un contrat clair

Une modale interrompt la navigation visuelle mais ne doit pas inventer la pause du monde. Elle reçoit un texte, des actions et une politique de fermeture.

À l’ouverture, le focus va vers une action sûre. À la fermeture, il revient au contrôle précédent si celui-ci existe encore et reste visible.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
modal_contract:
  id: AST-UI-MODAL-CONFIRM-001
  initial_focus: cancel_button
  close_paths: [confirm, cancel, back]
  outside_click: disabled
  escape_or_back: cancel
  restore_previous_focus: true
  gameplay_pause_request: external
  destructive_default: false
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Focus :** l’action sûre reçoit le focus initial pour réduire les activations accidentelles.
- **Fermeture :** toutes les sorties sont nommées et testables.
- **Clic extérieur :** une confirmation importante ne disparaît pas sans intention explicite.
- **Pause :** la modale demande un état au système de pause sans l’imposer.
- **Destruction :** l’action irréversible n’est jamais le choix par défaut.

## 23. Gérer notifications et toasts

Une notification temporaire possède une priorité, une durée, une politique de file et une alternative persistante pour les informations importantes.

Les toasts ne remplacent pas un journal, un objectif ou une modale lorsqu’une information doit être relue ou confirmée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
notification_policy:
  queue_limit: candidate
  priorities: [info, success, warning, critical]
  info:
    lifetime_ms: candidate
    persistence: optional
  critical:
    lifetime_ms: until_acknowledged
    persistence: required
  duplicate_policy: coalesce_by_message_id
  animation_profile: user_setting
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Limite :** la file reste bornée pour éviter une accumulation illisible.
- **Priorité :** la durée et le canal dépendent de l’importance.
- **Critique :** une information essentielle ne disparaît pas sans accusé.
- **Doublons :** les répétitions peuvent être regroupées par identifiant.
- **Mouvement :** l’animation respecte le profil utilisateur futur.

## 24. Composer le HUD sans capturer toute l’entrée

Le HUD affiche des états persistants et des invites contextuelles. Ses couches décoratives doivent ignorer la souris afin de ne pas bloquer le monde ou les contrôles interactifs.

Les zones interactives restent explicites et limitées ; la plupart des indicateurs sont en lecture seule.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
hud_layers:
  root: Control
  status_layer:
    interactive: false
    mouse_filter: ignore
  objective_layer:
    interactive: false
    mouse_filter: ignore
  prompt_layer:
    interactive: false
    mouse_filter: ignore
  quick_action_layer:
    interactive: conditional
    mouse_filter: stop
  debug_layer:
    exported_in_release: false
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racine :** le HUD occupe le viewport mais ne doit pas absorber tous les événements.
- **Statut :** les indicateurs non interactifs utilisent `MOUSE_FILTER_IGNORE`.
- **Invite :** les glyphes de commande restent informatifs.
- **Actions :** seules les zones cliquables arrêtent l’événement.
- **Debug :** les aides de développement sont exclues des builds de livraison.

## 25. Structurer le menu principal

Le menu principal définit un ordre de focus stable, un bouton de reprise conditionnel et une sortie adaptée à la plateforme. Les options indisponibles sont désactivées avec une raison compréhensible.

Les commandes de chargement, de création de partie ou de fermeture passent par des ports applicatifs, pas par le contrôle lui-même.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
main_menu:
  focus_order: [continue, new_game, load, settings, credits, quit]
  continue:
    enabled_when: compatible_save_exists
  load:
    enabled_when: visible_slot_exists
  quit:
    platform_policy: conditional
  first_focus: first_enabled_control
  commands: application_ports
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ordre :** la navigation suit la hiérarchie visuelle.
- **Reprise :** l’état vient du système de sauvegarde.
- **Chargement :** l’interface ne déduit pas seule la compatibilité.
- **Sortie :** certaines plateformes masquent ou remplacent cette action.
- **Focus :** le premier contrôle réellement actif est sélectionné.

## 26. Structurer l’écran d’inventaire

L’écran d’inventaire présente filtres, liste, détails et actions. Il consomme des définitions et instances préparées par le système d’inventaire du Livre II.

Le tri visuel ne déplace aucun objet. Équiper, déplacer ou jeter déclenche une commande et attend un résultat autoritaire.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
inventory_screen:
  regions:
    filters: AST-UI-COMP-FILTER-BAR-001
    list: AST-UI-COMP-ITEM-LIST-001
    details: AST-UI-COMP-ITEM-DETAILS-001
    actions: AST-UI-COMP-ACTION-BAR-001
  view_model:
    immutable_snapshot: true
    selected_item_id: StringName
  commands: [equip, move, split, drop]
  result_handling: refresh_from_authoritative_state
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Régions :** les responsabilités restent séparées et réutilisables.
- **Snapshot :** l’écran lit une vue cohérente au lieu de modifier l’inventaire.
- **Sélection :** l’identifiant est distinct de la position visuelle.
- **Commandes :** chaque action passe par un port typé.
- **Résultat :** un refus ou succès entraîne une nouvelle lecture de l’état.

## 27. Construire des fenêtres et panneaux complexes

Les écrans denses utilisent des séparations, onglets, zones scrollables et actions persistantes. Une fenêtre ne doit pas devenir une scène monolithique avec des centaines de chemins de nœuds.

Chaque sous-panneau peut devenir un composant autonome avec son propre contrat et ses tests.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
complex_panel:
  root: PanelContainer
  layout:
    header: fixed
    tabs: TabContainer
    content: ScrollContainer
    actions: persistent_footer
  decomposition:
    maximum_responsibilities_per_component: reviewed
    direct_node_paths: bounded
    cross_panel_signals: typed
  resize_test: required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Racine :** la surface et les marges restent centralisées.
- **Onglets :** un seul contenu est visible à la fois.
- **Défilement :** les données longues n’agrandissent pas la fenêtre hors écran.
- **Décomposition :** les composants limitent les dépendances internes.
- **Test :** le redimensionnement reste une condition de validation.

## 28. Définir les profils de périphérique

L’interface ne doit pas changer de logique métier selon le périphérique. Elle adapte les glyphes, la présence du pointeur et la stratégie de focus.

Le profil actif peut suivre le dernier périphérique utilisé, mais les changements rapides doivent être stabilisés pour éviter un clignotement de prompts.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
input_profiles:
  mouse_keyboard:
    pointer_visible: true
    focus_visible: on_keyboard_navigation
    prompts: keyboard_layout_aware
  gamepad:
    pointer_visible: false
    focus_visible: always
    prompts: controller_family_aware
  switching:
    source: last_meaningful_input
    debounce_ms: candidate
    gameplay_actions_unchanged: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Souris :** le pointeur reste disponible et le focus peut apparaître lors de la navigation clavier.
- **Manette :** le focus est indispensable car il remplace le pointeur.
- **Prompts :** les glyphes dépendent de la disposition ou de la famille.
- **Bascule :** seules les entrées significatives changent le profil.
- **Invariant :** les actions nommées du gameplay ne changent pas.

## 29. Configurer le focus clavier et manette

Chaque écran définit un focus initial, un ordre logique et des voisins explicites pour les dispositions non linéaires. Le moteur peut deviner un voisin, mais cette approximation devient fragile dans une interface complexe.

Les actions `ui_up`, `ui_down`, `ui_left`, `ui_right`, `ui_focus_next`, `ui_focus_prev`, `ui_accept` et `ui_cancel` restent dédiées à l’interface.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
focus_contract:
  screen: AST-UI-SCREEN-INVENTORY-001
  initial: filter_all
  directional_neighbors:
    filter_all: {down: first_item, right: filter_weapons}
    first_item: {up: filter_all, right: details_primary_action}
  tab_order: explicit
  hidden_control_policy: choose_next_visible
  ui_actions_reserved_for_gui: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Initial :** l’écran devient navigable sans clic préalable.
- **Voisins :** les transitions spatiales suivent le layout visible.
- **Tabulation :** l’ordre séquentiel est documenté séparément.
- **Masquage :** un contrôle caché ne reste pas une cible fantôme.
- **Réservation :** les actions `ui_*` ne servent pas au gameplay.

## 30. Attribuer le focus au bon moment

Appeler `grab_focus()` trop tôt peut échouer si la scène n’est pas prête ou si le contrôle est invisible. Un appel différé après affichage est généralement plus robuste.

Le code doit vérifier que la cible est visible, active et configurée pour recevoir le focus.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```gdscript
func focus_first_available(candidates: Array[Control]) -> bool:
    for candidate in candidates:
        if candidate == null:
            continue
        if not candidate.is_visible_in_tree():
            continue
        if candidate.focus_mode == Control.FOCUS_NONE:
            continue
        candidate.grab_focus.call_deferred()
        return true
    return false
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** le tableau ordonné décrit les cibles préférées.
- **Nullité :** une scène optionnelle peut produire une référence absente.
- **Visibilité :** un contrôle caché ne reçoit pas le focus utile.
- **Mode :** `FOCUS_NONE` exclut explicitement la navigation.
- **Retour :** le booléen indique si une cible a été planifiée.

## 31. Gérer souris et tactile sans bloquer les parents

`mouse_filter` décide si un `Control` arrête, transmet ou ignore les événements. Les icônes et labels placés au-dessus d’un bouton doivent souvent ignorer la souris.

Un contrôle qui appelle `accept_event()` empêche le traitement ultérieur, y compris `_unhandled_input()` du gameplay. Cette décision doit être limitée aux interactions réellement consommées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
pointer_policy:
  interactive_control: stop
  decorative_child: ignore
  scroll_region: pass_or_stop_by_design
  fullscreen_overlay:
    default: ignore
    modal_backdrop: stop
  accepted_events:
    only_when_action_consumed: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Interactif :** un bouton arrête normalement le clic qu’il traite.
- **Décoratif :** une icône ne crée pas une hitbox concurrente.
- **Défilement :** la propagation dépend de la composition et doit être testée.
- **Overlay :** le HUD plein écran ignore la souris sauf modale.
- **Acceptation :** un événement n’est marqué traité que lorsqu’une action UI l’utilise.

## 32. Gérer la manette et les actions UI

La manette utilise le focus et les actions UI intégrées. Les sticks analogiques peuvent demander un seuil et un rythme de répétition pour les listes longues.

Les actions de navigation ne doivent pas déclencher simultanément le déplacement du personnage lorsque le menu est ouvert.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
gamepad_navigation:
  actions: [ui_up, ui_down, ui_left, ui_right, ui_accept, ui_cancel]
  repeat:
    initial_delay_ms: candidate
    interval_ms: candidate
  analog_threshold: candidate
  menu_context:
    gameplay_input_enabled: false
    ui_input_enabled: true
  validation: two_controller_families_minimum
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Actions :** les noms intégrés restent réservés au focus et à l’activation.
- **Répétition :** délai et cadence doivent être mesurés avec les listes.
- **Seuil :** le stick ne doit pas produire des déplacements involontaires.
- **Contexte :** l’ouverture du menu sépare les flux d’entrée.
- **Validation :** plusieurs familles de manettes réduisent les suppositions de glyphes.

## 33. Afficher des prompts et glyphes de commande

Un prompt lie une action nommée à un libellé et à un glyphe qualifié. Il ne stocke pas une touche en dur.

Lorsque plusieurs événements sont liés à la même action, le service choisit une représentation selon le profil actif et la préférence du joueur.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
prompt_model:
  action_id: interact
  localized_label_key: ui.action.interact
  input_profile: gamepad
  preferred_event: resolved_from_input_map
  glyph_id: AST-UI-GLYPH-GAMEPAD-FACE-LEFT
  fallback_text: E
  provenance: qualified_glyph_pack
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Action :** le prompt dépend de l’intention et non d’une touche fixe.
- **Libellé :** le texte passe par une clé localisée.
- **Événement :** la liaison effective est lue depuis l’Input Map.
- **Glyphe :** la ressource appartient à un pack identifié.
- **Repli :** un texte reste disponible si l’image manque.

## 34. Séparer événements GUI et gameplay

L’interface reçoit d’abord les événements GUI. Les événements non consommés peuvent ensuite atteindre `_unhandled_input()` du gameplay.

Cette chaîne permet qu’un clic sur un bouton ne tire pas une arme et qu’une touche non utilisée par le menu conserve son sens lorsque le contexte l’autorise.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
input_flow:
  physical_event:
    - gui_input_on_target_control
    - accept_event_if_consumed
    - shortcut_and_ui_actions
    - unhandled_input_for_gameplay
  menu_open:
    gameplay_context: suspended
  menu_closed:
    gameplay_context: restored
  invariant: one_event_one_authoritative_intent
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Cible :** le contrôle sous le pointeur ou focalisé traite l’événement pertinent.
- **Acceptation :** l’événement consommé ne descend plus vers le gameplay.
- **Raccourci :** les actions UI suivent le contexte du menu.
- **Suspension :** les entrées gameplay sont désactivées par un contrat externe.
- **Invariant :** un événement physique ne crée pas deux intentions concurrentes.

## 35. Définir tous les états interactifs

Un composant interactif possède au minimum les états normal, survol, focus, pressé et désactivé. La sélection, le chargement ou l’erreur de saisie ajoutent des états lorsque le contrat l’exige.

Le focus ne doit pas être seulement une variation de survol, car la manette et le clavier n’utilisent pas forcément le pointeur.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
interactive_states:
  normal: readable
  hover: pointer_feedback
  focus: keyboard_gamepad_indicator
  pressed: activation_feedback
  disabled: unavailable_with_reason
  selected: persistent_choice
  loading: action_temporarily_locked
  validation_error: field_specific_message
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Normal :** le contrôle reste identifiable sans interaction.
- **Survol :** le pointeur reçoit un retour immédiat mais non exclusif.
- **Focus :** une bordure ou forme dédiée signale la cible active.
- **Désactivé :** la raison est disponible sans laisser croire à un bug.
- **Extension :** sélection, chargement et validation répondent à des contrats spécifiques.

## 36. Animer transitions et feedback avec modération

Les transitions expliquent un changement d’état ou de hiérarchie ; elles ne doivent pas retarder toutes les actions. Leur durée et leur possibilité de réduction sont tokenisées.

Un contrôle ne devient pas interactif avant d’être lisible et ne reste pas cliquable après sa sortie visuelle.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
transition_contract:
  enter:
    duration_token: quick
    interaction_enabled_after: visible_threshold
  exit:
    duration_token: quick
    interaction_disabled_before: animation
  state_change:
    duration_token: instant_or_quick
  reduced_motion:
    duration_token: instant
    spatial_movement: removed
  concurrent_transition_policy: replace_previous
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** l’interaction attend que le contrôle soit perceptible.
- **Sortie :** la hitbox disparaît avant l’animation de retrait.
- **État :** les changements fréquents restent courts.
- **Réduction :** le profil sans mouvement garde le changement d’information.
- **Concurrence :** un nouveau tween remplace l’ancien au lieu de s’empiler.

## 37. Choisir une taille de base et un mode d’échelle

Godot 4.7 utilise pour les nouveaux projets des valeurs par défaut `canvas_items` et `expand`, mais un projet existant doit documenter explicitement ses réglages. La taille de base sert de cadre logique, pas de résolution unique de test.

`content_scale_mode`, `content_scale_aspect`, `content_scale_size` et `content_scale_factor` contrôlent la transformation du contenu.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
display_policy:
  base_size: Vector2i(1920, 1080)
  content_scale_mode: canvas_items
  content_scale_aspect: expand
  content_scale_factor: 1.0
  ui_scale_user_range: candidate
  project_defaults_recorded: true
  validation: multi_resolution_required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Base :** le cadre logique facilite la composition sans limiter les tests.
- **Mode :** `canvas_items` redimensionne les éléments 2D et UI.
- **Aspect :** `expand` expose plus d’espace selon la forme de fenêtre.
- **Facteur :** l’échelle utilisateur reste distincte de la résolution physique.
- **Validation :** les réglages ne sont acceptés qu’après campagne multi-résolution.

## 38. Adapter les ratios et les zones sûres

Un écran large, compact ou presque carré ne doit ni couper les actions ni étirer les composants de manière non uniforme. Les éléments essentiels restent dans une zone sûre.

`DisplayServer.get_display_safe_area()` fournit une zone non obstruée sur les plateformes prises en charge et un repli sur d’autres plateformes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
safe_layout:
  aspect_profiles: ["16:9", "16:10", "21:9", "4:3"]
  safe_area_source: DisplayServer.get_display_safe_area
  content_strategy:
    wide: increase_gutters_and_optional_context
    compact: collapse_secondary_panels
    tall: reflow_vertical_regions
  critical_controls_inside_safe_area: true
  notch_and_system_bar_test: required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profils :** la matrice couvre des formes réellement différentes.
- **Source :** la zone sûre vient du serveur d’affichage lorsque disponible.
- **Large :** l’espace supplémentaire ne dilue pas les groupes principaux.
- **Compact :** les panneaux secondaires se replient avant les actions critiques.
- **Test :** encoches et barres système restent des réserves à exécuter.

## 39. Proposer une échelle d’interface contrôlée

Une option d’échelle améliore la lisibilité sans imposer une résolution différente au rendu 3D. Elle agit sur le facteur de contenu ou une stratégie documentée, pas sur des `scale` arbitraires dispersés.

Le changement doit préserver les tailles minimales, les scrolls et les zones sûres.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```gdscript
class_name UiScaleService
extends RefCounted

const MIN_FACTOR: float = 0.75
const MAX_FACTOR: float = 1.50

func apply_factor(window: Window, requested: float) -> float:
    var accepted := clampf(requested, MIN_FACTOR, MAX_FACTOR)
    window.content_scale_factor = accepted
    return accepted
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe :** le service isole la politique d’échelle des écrans.
- **Bornes :** les limites candidates évitent les valeurs extrêmes non testées.
- **Entrée :** le facteur demandé peut venir des préférences du joueur.
- **Application :** la propriété du `Window` centralise l’échelle du contenu.
- **Retour :** la valeur réellement acceptée peut être affichée et persistée.

## 40. Gérer les contenus longs et le défilement

Une liste, un codex ou une description localisée peut dépasser l’espace disponible. `ScrollContainer` protège le layout, mais il faut aussi rendre le focus visible lors de la navigation.

Les barres, l’inertie et le défilement automatique doivent être testés à la souris, au clavier et à la manette.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
scroll_policy:
  viewport: ScrollContainer
  content: VBoxContainer
  focus_follow:
    ensure_focused_control_visible: true
  axes:
    horizontal: disabled_unless_required
    vertical: automatic
  input:
    mouse_wheel: true
    gamepad_navigation: true
    drag_or_touch: platform_specific
  long_content_test: required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Viewport :** le conteneur limite la zone visible.
- **Contenu :** la pile verticale fournit une taille minimale cumulée.
- **Focus :** la cible active doit entrer dans la zone visible.
- **Axes :** le défilement horizontal n’est pas activé par défaut.
- **Test :** les méthodes d’entrée sont vérifiées séparément.

## 41. Préparer localisation et expansion du texte

Les libellés visibles utilisent des clés, et les composants acceptent une expansion de longueur sans chevauchement. La pseudo-localisation permet de simuler des chaînes plus longues avant la traduction réelle.

Les concaténations de fragments sont évitées lorsque l’ordre grammatical peut changer.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
localization_contract:
  label_key: ui.inventory.capacity
  parameters: {used: 12, maximum: 30}
  pseudolocalization:
    expansion_ratio: 0.30
    fake_bidi: true
  layout:
    wrap_mode: semantic
    truncation: only_with_full_text_access
  concatenation_fragments: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Clé :** le texte visible n’est pas codé en dur dans la scène.
- **Paramètres :** les valeurs sont injectées dans une phrase complète.
- **Expansion :** un ratio candidat simule les langues plus longues.
- **Bidi :** la simulation repère les hypothèses gauche-droite.
- **Troncature :** le texte complet reste accessible lorsqu’une coupe est nécessaire.

## 42. Préparer les langues de droite à gauche

La direction du texte et du layout peut être héritée ou forcée selon le composant. Les icônes directionnelles, l’ordre des colonnes et les marges doivent être revus.

Tous les symboles ne se retournent pas : une icône de lecture temporelle ou un logo peut conserver son orientation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
rtl_review:
  layout_direction: inherited
  text_direction: automatic
  mirrored:
    - navigation_arrows
    - ordered_horizontal_groups
  not_automatically_mirrored:
    - brand_marks
    - media_play_symbol
    - world_compass
  pseudolocalization_fake_bidi: enabled_for_test
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Héritage :** la direction suit la langue et le parent sauf exception.
- **Texte :** la détection automatique gère les chaînes mixtes.
- **Miroir :** les directions spatiales et ordres de lecture sont revus.
- **Exceptions :** les symboles sémantiques ne changent pas mécaniquement.
- **Test :** la pseudo-localisation fournit une première détection, pas une validation humaine.

## 43. Séparer modèle de vue et état métier

Un modèle de vue transforme les données autoritaires en texte, icônes, statuts et actions disponibles. Il peut calculer une représentation, mais ne possède pas l’entité métier.

Le modèle de vue est remplacé après chaque résultat de commande ou événement pertinent.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```gdscript
class_name InventoryItemViewModel
extends RefCounted

var item_id: StringName
var title: String
var quantity_text: String
var icon_id: StringName
var action_ids: Array[StringName]
var is_enabled: bool

func _init(
    p_item_id: StringName,
    p_title: String,
    p_quantity_text: String,
    p_icon_id: StringName,
    p_action_ids: Array[StringName],
    p_is_enabled: bool
) -> void:
    item_id = p_item_id
    title = p_title
    quantity_text = p_quantity_text
    icon_id = p_icon_id
    action_ids = p_action_ids
    is_enabled = p_is_enabled
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe :** le modèle transporte seulement les données nécessaires à la vue.
- **Identifiant :** l’action ultérieure vise l’objet stable, pas l’index d’une ligne.
- **Texte :** la quantité est déjà formatée pour le contexte de lecture.
- **Actions :** la disponibilité vient du système métier.
- **Mutation :** le constructeur fixe un snapshot remplaçable plutôt qu’une entité partagée.

## 44. Définir le contrat de requête UI

Une action UI produit une requête avec identifiant, source et paramètres bornés. Le routeur applicatif valide ensuite l’autorisation et appelle le système propriétaire.

Le retour distingue succès, refus contrôlé et erreur technique ; la vue ne déduit pas le résultat à partir de l’animation du bouton.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
ui_request:
  request_id: generated
  action_id: inventory.equip
  source_screen: AST-UI-SCREEN-INVENTORY-001
  payload:
    item_id: ITEM-IRON-SWORD-001
  expected_result:
    statuses: [accepted, refused, failed]
    authoritative_refresh: required
  visual_feedback: derived_from_result
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Corrélation :** l’identifiant relie demande, résultat et journal.
- **Action :** le nom exprime une intention applicative.
- **Source :** l’écran facilite le diagnostic sans devenir propriétaire.
- **Statuts :** un refus métier est distinct d’une panne.
- **Rafraîchissement :** la vue relit l’état autoritaire avant d’afficher le résultat final.

## 45. Gérer une pile d’écrans

Un routeur UI ouvre, ferme et remplace les écrans selon une politique explicite. Les écrans ne s’instancient pas mutuellement par chemins codés en dur.

La pile conserve le contexte de focus et distingue superposition modale, écran exclusif et HUD persistant.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
screen_stack:
  persistent:
    - AST-UI-SCREEN-HUD-EXPLORATION-001
  stack:
    - AST-UI-SCREEN-INVENTORY-001
    - AST-UI-MODAL-CONFIRM-001
  operations: [push, pop, replace, clear_to_root]
  focus_snapshot: per_stack_entry
  modal_input_capture: top_only
  lifecycle: [entering, active, leaving, hidden]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Persistant :** le HUD peut rester monté tout en étant masqué ou désactivé.
- **Pile :** l’ordre détermine la superposition et la priorité d’entrée.
- **Opérations :** les transitions sont limitées à un vocabulaire testable.
- **Focus :** chaque entrée conserve la cible à restaurer.
- **Cycle :** les états empêchent les interactions pendant une transition incohérente.

## 46. Restaurer le focus après fermeture

La fermeture d’un panneau ou d’une modale doit revenir à une cible encore valide. Si elle a disparu, le routeur choisit un repli de l’écran parent.

Une simple référence forte peut garder un nœud supprimé ; un chemin, un identifiant ou une référence faible doit être vérifié avant usage.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
focus_restore:
  previous_control_path: NodePath
  fallback_paths:
    - ^"PrimaryAction"
    - ^"FirstEnabledControl"
  checks:
    - node_exists
    - visible_in_tree
    - focus_mode_not_none
    - not_disabled_when_base_button
  action: deferred_grab_focus
  failure: log_and_continue_without_crash
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Chemin :** la cible est relative à l’écran qui la possède.
- **Replis :** plusieurs choix ordonnés évitent un focus perdu.
- **Vérifications :** visibilité, focus et désactivation sont contrôlés.
- **Différé :** la restauration attend la fin de la modification de scène.
- **Échec :** l’absence de cible reste diagnostiquée sans bloquer le jeu.

## 47. Coordonner pause, menus et temps du jeu

Un menu de pause demande au système de pause de suspendre les domaines appropriés. L’interface peut continuer à traiter les entrées selon son `process_mode` sans décider seule quelles simulations s’arrêtent.

Les écrans non pausants, comme un inventaire temps réel, utilisent une politique différente et documentée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
pause_contract:
  screen: AST-UI-SCREEN-PAUSE-001
  request: app.pause.open
  authoritative_owner: pause_service
  ui_process_mode: when_paused
  gameplay_input: disabled_after_acceptance
  close_request: app.pause.close
  restoration: confirmed_by_service
  multiplayer_policy: deferred_to_book_iv
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Écran :** la scène décrit sa demande sans modifier directement l’arbre.
- **Propriétaire :** le service décide ce qui peut être suspendu.
- **Traitement :** l’interface reste active pendant la pause acceptée.
- **Entrées :** le gameplay est désactivé après confirmation.
- **Frontière :** le multijoueur reste hors du Livre III.

## 48. Charger thèmes, polices et icônes sans dépendances perdues

Les ressources obligatoires sont préchargées ou vérifiées avant l’affichage. Un fallback visuel permet de conserver un libellé lorsque l’icône manque.

Le chapitre 28 consolidera l’import universel ; ici, la scène documente ses dépendances directes et son comportement de repli.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
ui_dependencies:
  theme: res://ui/themes/asteria_core_theme.tres
  fonts:
    primary: res://ui/fonts/asteria_primary_font.tres
    fallback: res://ui/fonts/asteria_fallback_font.tres
  icons:
    atlas: res://ui/icons/asteria_ui_icons.tres
    missing_icon_policy: text_fallback
  loading:
    mandatory_before_screen_activation: true
    unresolved_dependency: block_screen_and_report
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Thème :** la ressource commune est une dépendance obligatoire.
- **Polices :** un repli couvre les glyphes absents.
- **Icônes :** le texte évite une commande invisible.
- **Activation :** l’écran ne devient pas interactif avant ses ressources critiques.
- **Refus :** une dépendance manquante produit un blocage explicite et un diagnostic.

## 49. Préparer une scène de test multi-résolution

La scène de test instancie les composants et écrans avec des données longues, courtes, vides et saturées. Elle permet de changer taille de fenêtre, ratio, échelle et profil d’entrée.

Cette scène est un outil de qualification ; elle n’est pas intégrée au build de livraison.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
ui_test_scene:
  path: res://ui/tests/test_ui_system.tscn
  fixtures:
    - short_text
    - expanded_text
    - empty_state
    - maximum_inventory
    - disabled_actions
    - missing_optional_icon
  controls:
    - resolution_selector
    - aspect_selector
    - ui_scale_selector
    - input_profile_selector
    - locale_selector
  release_exported: false
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Chemin :** la scène de qualification reste distincte des écrans de production.
- **Fixtures :** les états limites sont préparés à l’avance.
- **Résolution :** la fenêtre change sans recréer manuellement la scène.
- **Locale :** la pseudo-localisation fait partie de la campagne.
- **Livraison :** l’outil n’est pas exporté avec le jeu final.

## 50. Définir une matrice de résolutions et ratios

Une campagne utile combine résolution, ratio, mode fenêtre, échelle UI et langue. Tester seulement 1920×1080 ne révèle ni l’espace compact ni l’ultralarge.

Les valeurs exactes sont des scénarios candidats à ajuster selon les plateformes réellement ciblées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
ui_test_matrix:
  - {size: [1280, 720], aspect: "16:9", scale: 1.00, locale: fr}
  - {size: [1920, 1200], aspect: "16:10", scale: 1.25, locale: en}
  - {size: [2560, 1080], aspect: "21:9", scale: 1.00, locale: pseudo}
  - {size: [1024, 768], aspect: "4:3", scale: 1.25, locale: pseudo_rtl}
  window_modes: [windowed, borderless, exclusive_fullscreen]
  input_profiles: [mouse_keyboard, gamepad]
  evidence: capture_plus_checklist_plus_log
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Tailles :** la matrice couvre compact, standard, large et presque carré.
- **Échelle :** plusieurs facteurs révèlent les minima et scrolls.
- **Locales :** pseudo et pseudo-RTL stressent le layout.
- **Fenêtres :** les modes peuvent modifier l’espace réellement utilisable.
- **Preuve :** capture, checklist et journal sont conservés ensemble.

## 51. Automatiser des captures sans prétendre juger l’esthétique

Une automatisation peut ouvrir une scène, appliquer une configuration et capturer une image. Elle peut aussi détecter des contrôles hors bounds ou des erreurs de chargement.

Elle ne décide pas seule de la hiérarchie, de la lisibilité ou de la qualité artistique. Ces décisions restent humaines.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
visual_regression_job:
  inputs:
    scene: res://ui/tests/test_ui_system.tscn
    profile: ui_test_matrix_entry
    fixture: expanded_text
  outputs:
    screenshot: artifacts/ui/24/inventory_4x3_pseudo.png
    structure_log: artifacts/ui/24/inventory_4x3_pseudo.json
  automated_checks:
    - no_control_outside_safe_rect
    - no_missing_resource
    - no_unhandled_error
  human_review: required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** la scène, le profil et la fixture rendent le cas reproductible.
- **Capture :** le nom encode l’écran et le scénario.
- **Journal :** les bounds et dépendances complètent l’image.
- **Automatique :** les vérifications portent sur des faits mesurables.
- **Humain :** la cohérence visuelle ne se réduit pas à un seuil.

## 52. Mesurer le coût et la stabilité de l’interface

Les interfaces peuvent coûter du CPU, du GPU, de la mémoire et des allocations, surtout avec de longues listes, du texte riche, des icônes nombreuses ou des animations.

Les budgets doivent être mesurés dans des scénarios réalistes : ouverture, navigation soutenue, liste maximale, changement de langue et redimensionnement.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
ui_budget:
  scenarios:
    open_inventory: pending
    navigate_maximum_list: pending
    resize_window_continuously: pending
    switch_locale: pending
    open_close_modal_repeatedly: pending
  metrics:
    cpu_frame_time_ms: pending
    gpu_frame_time_ms: pending
    memory_delta_mb: pending
    allocation_spikes: pending
    input_latency_ms: pending
  decision: no_budget_claim_without_capture
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Scénarios :** les transitions et états denses sont mesurés séparément.
- **CPU :** layout, texte et scripts peuvent dominer certaines vues.
- **GPU :** transparence, flous et effets de panneau peuvent coûter.
- **Mémoire :** icônes, polices et listes doivent être observées.
- **Décision :** aucun budget n’est déclaré sans capture reproductible.

## 53. Qualifier polices, icônes et licences

Chaque police, atlas, icône ou illustration possède une source, une licence, une attribution et des droits de redistribution. Une ressource gratuite n’est pas automatiquement redistribuable.

Les fichiers sources, dérivés et versions embarquées peuvent avoir des obligations différentes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
ui_provenance:
  asset_id: AST-UI-FONT-PRIMARY-001
  source_type: authored_or_qualified_third_party
  author_or_provider: pending
  license_id: pending
  attribution: pending
  redistribution:
    source_files: pending
    derived_font_resource: pending
    runtime_build: pending
  glyph_coverage: pending
  approval: pending
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Asset :** la police reçoit une identité stable.
- **Source :** l’auteur ou fournisseur reste vérifiable.
- **Licence :** un identifiant remplace les formulations vagues.
- **Redistribution :** source, dérivé et build sont évalués séparément.
- **Couverture :** les glyphes requis font partie de la qualification.

## 54. Mode Solo et Mode Studio

En mode Solo, la priorité est une bibliothèque courte : un thème, quelques composants solides et cinq écrans pilotes. Les exceptions locales sont refusées lorsqu’un token ou une variation suffit.

- un seul thème de projet ;
- cinq écrans pilotes ;
- un catalogue minimal de composants ;
- une revue par checklist et captures ciblées ;
- les mêmes contrats de requête, focus et navigation que le parcours Studio.

En mode Studio, design, développement, localisation, QA et accessibilité partagent des propriétaires, une revue de composants et des tests de régression visuelle versionnés.

- propriétaires séparés pour design UI, ingénierie UI, localisation et QA ;
- composants partagés avec versions et historique ;
- matrice de captures commune ;
- approbation croisée design-développement-QA ;
- aucune divergence des contrats runtime entre les deux parcours.

## 55. Préparer le paquet de livraison et la porte d’acceptation

Le paquet UI contient thème, composants, écrans, ressources dérivées, manifests et résultats de tests. Les sources de conception et documents privés restent dans l’espace de production.

Un écran est accepté seulement si son contenu est cohérent, sa navigation complète, ses éléments dans les bounds, ses états compréhensibles et ses dépendances qualifiées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
acceptance_gate:
  artistic:
    theme_and_hierarchy_consistent: pending
  interaction:
    mouse_keyboard_gamepad_navigation_complete: pending
    focus_restore_and_modal_paths: pending
  adaptation:
    multi_resolution_and_safe_area_pass: pending
    localization_expansion_pass: pending
  technical:
    no_missing_dependency: pending
    runtime_budget_measured: pending
  legal:
    fonts_icons_and_images_approved: pending
  decision: blocked_until_all_required_checks_pass
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Artistique :** le thème et la hiérarchie sont jugés ensemble.
- **Interaction :** tous les parcours de focus et fermeture demandent une preuve.
- **Adaptation :** ratios, zones sûres et textes longs sont obligatoires.
- **Technique :** dépendances et budgets restent séparés de la revue visuelle.
- **Décision :** aucune catégorie ne compense l’échec d’une autre.

## 56. Diagnostics et corrections

<!-- qa:error-correction-section -->

### 56.1 Le bouton modifie directement l’inventaire

**Symptôme ou risque :** un clic sur « Équiper » retire l’objet de la liste locale avant que le système d’inventaire accepte la commande ; un refus serveur ou métier laisse l’écran incohérent.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
func _on_equip_pressed() -> void:
    selected_item.equipped = true
    inventory_items.erase(selected_item)
    refresh_list()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le contrôle modifie une entité et une collection locales sans transaction, autorisation ni résultat autoritaire. La vue peut diverger de la sauvegarde et des autres systèmes.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
func _on_equip_pressed() -> void:
    ui_requests.request_action(
        &"inventory.equip",
        {"item_id": selected_item_id}
    )
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le bouton émet une requête typée. Le système propriétaire décide puis publie un nouvel état que l’interface relit.

### 56.2 Les contrôles enfants d’un Container sont positionnés manuellement

**Symptôme ou risque :** un bouton revient à une ancienne position après redimensionnement ou changement de texte.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
layout:
  parent: VBoxContainer
  child_button:
    position: Vector2(640, 120)
    size: Vector2(240, 48)
    container_flags: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le conteneur reprend automatiquement le placement de ses enfants. Les coordonnées manuelles sont ignorées ou écrasées au prochain recalcul.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
layout:
  parent: VBoxContainer
  child_button:
    custom_minimum_size: Vector2(240, 48)
    horizontal_size_flags: [fill, expand]
    vertical_size_flags: [fill]
    position_owned_by_container: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le bouton exprime seulement ses besoins de taille et de partage. Le parent calcule sa position pour chaque taille disponible.

### 56.3 Chaque écran copie ses propres overrides de thème

**Symptôme ou risque :** deux boutons principaux ont des marges, couleurs ou états de focus différents après une correction.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
screens:
  inventory:
    primary_button_overrides: local_copy_a
  pause:
    primary_button_overrides: local_copy_b
  main_menu:
    primary_button_overrides: local_copy_c
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** les copies locales n’ont pas de source commune et dérivent silencieusement. Une correction doit être répétée dans chaque scène.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
theme:
  resource: res://ui/themes/asteria_core_theme.tres
  variation: AsteriaPrimaryButton
screens:
  inventory: uses_variation
  pause: uses_variation
  main_menu: uses_variation
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la variation de thème centralise les propriétés et tous les écrans reçoivent la même correction versionnée.

### 56.4 L’écran s’ouvre sans focus initial

**Symptôme ou risque :** la manette ne peut rien activer après l’ouverture du menu tant que le joueur n’utilise pas la souris.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
func open_screen() -> void:
    visible = true
    play_enter_animation()
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** aucun contrôle ne devient la cible active. Les actions de navigation n’ont donc pas de point de départ fiable.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
func open_screen() -> void:
    visible = true
    play_enter_animation()
    focus_first_available([continue_button, new_game_button, settings_button])
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** l’ouverture planifie un focus sur le premier contrôle visible et actif, ce qui rend immédiatement la navigation clavier/manette possible.

### 56.5 Les actions ui_* servent aussi au déplacement gameplay

**Symptôme ou risque :** appuyer sur le D-pad dans un menu déplace à la fois le focus et le personnage.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
input_actions:
  ui_up: [keyboard_up, gamepad_dpad_up]
  move_forward: aliases_ui_up
menu_context:
  gameplay_input_enabled: true
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** les actions internes de focus sont partagées avec une intention gameplay et les deux contextes restent actifs.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
input_actions:
  ui_up: [keyboard_up, gamepad_dpad_up]
  move_forward: [keyboard_w, keyboard_z, gamepad_left_stick_up]
menu_context:
  gameplay_input_enabled: false
  ui_input_enabled: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les actions de navigation et de déplacement sont distinctes, puis le contexte de menu suspend explicitement le gameplay.

### 56.6 Le HUD est validé uniquement en 16:9

**Symptôme ou risque :** sur un écran 4:3 ou ultralarge, une barre sort de l’écran et une action se trouve sous une zone système.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
validation:
  resolution: [1920, 1080]
  aspect: "16:9"
  safe_area: ignored
  ui_scale: 1.0
  result: approved_for_all_devices
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** un seul ratio ne prouve ni le reflow, ni les zones sûres, ni les facteurs d’échelle. La conclusion universelle dépasse les preuves.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
validation:
  matrix: ["16:9", "16:10", "21:9", "4:3"]
  safe_area: required
  ui_scales: [candidate_min, reference, candidate_max]
  result_scope: measured_profiles_only
  approval: pending
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la campagne couvre plusieurs formes et limite la décision aux profils réellement mesurés.

### 56.7 Le texte localisé est coupé par une largeur fixe

**Symptôme ou risque :** une traduction longue chevauche l’icône ou disparaît sans moyen de lire la phrase complète.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
label:
  width: 180
  wrap_mode: off
  clip_text: true
  tooltip: none
  localization_test: skipped
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la largeur fixe et l’absence de reflow supposent une longueur de texte unique. La coupure détruit l’information.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
label:
  horizontal_size_flags: [fill, expand]
  wrap_mode: word_smart
  clip_text: conditional
  full_text_access: tooltip_or_details
  pseudolocalization_test: required
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le conteneur distribue l’espace, le texte peut revenir à la ligne et une voie d’accès conserve le contenu complet.

### 56.8 Un overlay décoratif bloque tous les clics

**Symptôme ou risque :** les boutons visibles sous un effet plein écran ne reçoivent plus la souris, alors que l’overlay ne possède aucune action.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
overlay:
  root: Control
  anchors: full_rect
  mouse_filter: stop
  interactive_children: none
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le contrôle plein écran intercepte les événements avant les boutons et les marque comme traités.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
overlay:
  root: Control
  anchors: full_rect
  mouse_filter: ignore
  interactive_children: none
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** `MOUSE_FILTER_IGNORE` retire l’overlay de la chaîne de hit test et laisse les contrôles utiles recevoir les clics.

### 56.9 La modale ne restaure pas le focus

**Symptôme ou risque :** après fermeture d’une confirmation, le focus disparaît ou revient sur un contrôle masqué.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
modal:
  previous_focus: not_recorded
  close:
    hide_modal: true
    restore_focus: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la pile perd la cible précédente et ne vérifie pas si une cible de repli existe encore.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
modal:
  previous_focus: recorded_per_stack_entry
  close:
    hide_modal: true
    restore_focus:
      checks: [exists, visible, focusable, enabled]
      fallback: first_enabled_parent_control
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le routeur restaure une cible valide ou choisit un repli ordonné après la fermeture.

### 56.10 Les transitions s’empilent et laissent des hitboxes actives

**Symptôme ou risque :** ouvrir et fermer rapidement un panneau crée plusieurs tweens ; un contrôle invisible reste cliquable.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```gdscript
func show_panel() -> void:
    create_tween().tween_property(self, "modulate:a", 1.0, 0.5)

func hide_panel() -> void:
    create_tween().tween_property(self, "modulate:a", 0.0, 0.5)
    visible = false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** chaque appel crée une animation indépendante et la désactivation intervient trop tard ou sans cohérence avec l’état courant.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```gdscript
var transition: Tween

func show_panel() -> void:
    if transition:
        transition.kill()
    visible = true
    mouse_filter = Control.MOUSE_FILTER_STOP
    transition = create_tween()
    transition.tween_property(self, "modulate:a", 1.0, 0.12)

func hide_panel() -> void:
    if transition:
        transition.kill()
    mouse_filter = Control.MOUSE_FILTER_IGNORE
    transition = create_tween()
    transition.tween_property(self, "modulate:a", 0.0, 0.12)
    transition.tween_callback(hide)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** une transition remplace la précédente, la hitbox est désactivée avant la sortie et le nœud est masqué après l’animation.

## 57. Checklist de production et validation

La checklist est utilisée avant toute déclaration d’acceptation. Une case non vérifiée reste une réserve ; la présence d’un exemple dans ce chapitre ne la transforme pas en réussite.

- [ ] fonctions et priorités d’information définies ;
- [ ] tokens, thème et variations versionnés ;
- [ ] composants réutilisables séparés des écrans ;
- [ ] tailles minimales, conteneurs et ancres revus ;
- [ ] états normal, survol, focus, pressé et désactivé visibles ;
- [ ] navigation souris, clavier et manette complète ;
- [ ] focus initial et restauration après modale testés ;
- [ ] événements UI séparés des actions gameplay ;
- [ ] profils 16:9, 16:10, 21:9 et 4:3 inspectés ;
- [ ] zones sûres et échelles utilisateur validées ;
- [ ] textes longs, pseudo-localisation et pseudo-RTL testés ;
- [ ] polices, icônes et licences qualifiées ;
- [ ] scène de test et fixtures matérialisées ;
- [ ] captures, journaux et résultats conservés ;
- [ ] CPU, GPU, mémoire, allocations et latence mesurés ;
- [ ] aucune règle métier appliquée par un contrôle ;
- [ ] décision humaine et réserves consignées ;

## 58. Références techniques officielles

Les liens suivants sont les références primaires utilisées pour les contrôles, thèmes, conteneurs, navigation, mise à l’échelle, zones sûres et localisation. Ils doivent être relus lors d’une mise à jour de Godot ou du projet.

Les pages de classe décrivent les contrats disponibles ; elles ne prouvent pas qu’un écran, un thème ou une campagne particulière fonctionne dans Project Asteria.

- [Godot 4.7 — Control](https://docs.godotengine.org/en/4.7/classes/class_control.html)
- [Godot 4.7 — Theme](https://docs.godotengine.org/en/4.7/classes/class_theme.html)
- [Godot 4.7 — Window](https://docs.godotengine.org/en/4.7/classes/class_window.html)
- [Godot 4.7 — DisplayServer](https://docs.godotengine.org/en/4.7/classes/class_displayserver.html)
- [Godot 4.7 — Taille et ancres des interfaces](https://docs.godotengine.org/en/4.7/tutorials/ui/size_and_anchors.html)
- [Godot 4.7 — Utiliser les conteneurs](https://docs.godotengine.org/en/4.7/tutorials/ui/gui_containers.html)
- [Godot 4.7 — Navigation clavier/manette et focus](https://docs.godotengine.org/en/4.7/tutorials/ui/gui_navigation.html)
- [Godot 4.7 — Introduction aux thèmes GUI](https://docs.godotengine.org/en/4.7/tutorials/ui/gui_skinning.html)
- [Godot 4.7 — Utiliser l’éditeur de thème](https://docs.godotengine.org/en/4.7/tutorials/ui/gui_using_theme_editor.html)
- [Godot 4.7 — Variations de type de thème](https://docs.godotengine.org/en/4.7/tutorials/ui/gui_theme_type_variations.html)
- [Godot 4.7 — Utiliser les polices](https://docs.godotengine.org/en/4.7/tutorials/ui/gui_using_fonts.html)
- [Godot 4.7 — Contrôles GUI personnalisés](https://docs.godotengine.org/en/4.7/tutorials/ui/custom_gui_controls.html)
- [Godot 4.7 — Résolutions multiples](https://docs.godotengine.org/en/4.7/tutorials/rendering/multiple_resolutions.html)
- [Godot 4.7 — Internationaliser les jeux](https://docs.godotengine.org/en/4.7/tutorials/i18n/internationalizing_games.html)
- [Godot 4.7 — Pseudo-localisation](https://docs.godotengine.org/en/4.7/tutorials/i18n/pseudolocalization.html)
- [Livre II — Chapitre 6 : Entrées, contrôleurs, caméras et interactions](../Livre-II/CHAPITRE-06-Entrees-controleurs-cameras-et-interactions.md)
- [Livre III — Chapitre 23 : Effets visuels, particules et simulations](CHAPITRE-23-Effets-visuels-particules-et-simulations.md)

## 59. Synthèse opérationnelle pour Project Asteria

Project Asteria retient `AST-UI-PILOT-CORE-SHELL-001` comme pilote commun : menu principal, HUD d’exploration, inventaire, pause et modale de confirmation. Ces écrans utilisent `AST-UI-THEME-CORE-001`, un catalogue minimal de composants, des variations sémantiques, des modèles de vue immuables et une pile d’écrans qui conserve le focus. Toutes les actions visibles produisent des requêtes typées après lecture d’un état autoritaire ; aucun bouton, slider, panneau ou animation ne modifie directement le domaine.

La porte d’acceptation de Project Asteria exige une navigation complète à la souris, au clavier et à la manette, un focus initial et restauré, des états interactifs distincts, des textes extensibles, des ratios 16:9, 16:10, 21:9 et 4:3 sans élément critique hors zone sûre, ainsi que des polices et icônes juridiquement qualifiées. Les mesures CPU, GPU, mémoire, allocations et latence doivent être enregistrées dans la scène de test. Tant que ces preuves n’existent pas, le système reste bloqué au niveau `static-review` et ne revendique ni lisibilité finale, ni accessibilité complète, ni budget runtime.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**
```yaml
asteria_ui_decisions:
  pilot_id: AST-UI-PILOT-CORE-SHELL-001
  theme_id: AST-UI-THEME-CORE-001
  component_root: res://ui/components/
  screen_root: res://ui/screens/
  presentation_root: res://ui/presentation/
  test_scene: res://ui/tests/test_ui_system.tscn
  input_profiles: [mouse_keyboard, gamepad]
  aspect_profiles: ["16:9", "16:10", "21:9", "4:3"]
  request_contract: presentation_only_then_typed_application_request
  acceptance: artistic_plus_interaction_plus_adaptation_plus_technical_plus_legal
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pilote :** les cinq écrans constituent la référence de qualification commune.
- **Racines :** composants, écrans et présentation restent séparés.
- **Entrées :** les deux profils initiaux doivent réussir tous les parcours.
- **Ratios :** la campagne inclut plusieurs formes et zones sûres.
- **Porte :** les domaines d’acceptation restent indépendants et bloquants.
