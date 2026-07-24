---
title: "Livre III — Chapitre 25 : Expérience utilisateur et accessibilité visuelle"
id: "DOC-L3-CH25"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 25
last-verified: "2026-07-24T21:47:46+02:00"
audit-status: "complete"
audit-date: "2026-07-24T21:47:46+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-25.md"
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

# Expérience utilisateur et accessibilité visuelle

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH25`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+

## 1. Rôle du chapitre

Une expérience utilisateur accessible transforme les possibilités d’un système en parcours compréhensibles, prévisibles et récupérables. Elle ne se réduit ni à une palette « haute visibilité », ni à une checklist ajoutée après la production.

Le chapitre complète le système visuel du chapitre 24 par des critères de perception, des profils de réglages, des scénarios de tâches, des observations et une boucle de correction. Il n’accorde à l’interface aucune autorité sur les règles de combat, d’inventaire, de quête, de sauvegarde ou d’économie.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
chapter_role:
  input: themed_ui_components_and_authoritative_view_models
  transformation: measurable_ux_rules_accessibility_profiles_and_user_evaluation
  output: recoverable_task_flows_with_evidence_and_open_reservations
  authority: presentation_feedback_and_request_only
  evidence_level: static_review
  runtime_claims: none
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** le chapitre part des composants, écrans et modèles de vue déjà définis au chapitre 24.
- **Transformation :** les critères visuels deviennent des profils, scénarios, journaux d’observation et décisions révisables.
- **Autorité :** l’interface explique et transmet une intention ; elle ne valide jamais une transaction métier.
- **Sortie :** chaque parcours possède des critères observables, une méthode de test et des réserves explicites.
- **Preuve :** aucun profil, participant, test ou résultat runtime n’est revendiqué comme matérialisé.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura hiérarchiser l’information, réduire la charge cognitive, fixer des objectifs de contraste et de taille, rendre la couleur redondante, maintenir un focus visible et proposer des variantes de mouvement.

Il saura aussi préparer des messages d’erreur récupérables, des confirmations proportionnées au risque, des scénarios de test avec des personnes et un rapport qui distingue faits observés, interprétations, limites et décisions.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
learning_outcomes:
  perception: [hierarchy, contrast, typography, density, redundant_coding]
  navigation: [focus_visibility, logical_order, recovery, target_spacing]
  comfort: [motion_reduction, flash_review, persistent_information]
  safety: [error_prevention, confirmation, cancellation, undo]
  evaluation: [tasks, observations, severity, reporting, human_decision]
  governance: [consent, privacy, scope, evidence, reservations]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Perception :** la lisibilité est traitée comme un ensemble de conditions observables plutôt qu’une préférence esthétique.
- **Navigation :** le focus et l’ordre logique doivent rester détectables, prévisibles et récupérables.
- **Confort :** les mouvements et clignotements sont bornés, substituables ou désactivables selon le profil.
- **Évaluation :** les tests reposent sur des tâches et des observations plutôt que sur une approbation vague.
- **Gouvernance :** les données de participants restent minimales, consenties et hors du dépôt public.

## 3. Niveau de preuve et réserves

Le chapitre est accepté au niveau `static-review`. Les profils, fichiers, scènes et formulaires sont des modèles pédagogiques ; ils ne prouvent ni accessibilité effective, ni conformité à une norme, ni réussite d’un parcours par des personnes réelles.

Les critères issus de WCAG 2.2 servent de repères mesurables. WCAG vise le contenu web : leur reprise dans un jeu aide à formuler des objectifs, mais ne constitue pas une certification automatique de Project Asteria.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
evidence_level:
  chapter: static_review
  accessibility_profiles_created: false
  contrast_measurements_recorded: false
  focus_paths_executed: false
  reduced_motion_variant_inspected: false
  user_sessions_conducted: false
  participant_data_collected: false
  wcag_conformance_claimed: false
  runtime_measurements: false
  pdf_produced: false
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** la méthode est relue contre les sources officielles sans annoncer une implémentation terminée.
- **Profils :** aucune variante de contraste, taille, couleur ou mouvement n’est déclarée créée.
- **Participants :** aucune session, donnée personnelle, observation ou citation n’est inventée.
- **Normes :** les critères web sont utilisés comme références techniques, pas comme label de conformité du jeu.
- **Publication :** le PDF du Livre III demeure différé jusqu’à la fin du Livre.

## 4. Frontières avec les chapitres voisins

Le chapitre 24 conserve le design system, les thèmes Godot, les composants et les dispositions. Le chapitre 25 décide comment ces briques sont évaluées, configurées et corrigées pour la compréhension, la tolérance aux erreurs et l’accessibilité visuelle.

Le Livre II conserve les états et commandes autoritaires. Le Livre IV complétera l’accessibilité audio, la personnalisation des commandes et la validation globale de plateforme.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ownership:
  chapter_24: ui_design_system_theme_components_and_layout
  chapter_25: ux_rules_visual_accessibility_profiles_and_user_evaluation
  book_ii_chapter_06: input_intentions_and_remapping
  book_ii_domain_chapters: authoritative_state_commands_and_transactions
  book_iv: audio_input_and_platform_accessibility_completion
  invariant: evaluation_and_presentation_never_commit_domain_state
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Interface :** les composants existants sont qualifiés ; ils ne sont pas redessinés comme s’ils n’avaient pas de source.
- **UX :** les critères, profils, tâches et rapports appartiennent au présent chapitre.
- **Gameplay :** une observation peut déclencher une demande de correction, jamais une mutation métier directe.
- **Livre IV :** les dimensions audio, commandes et plateforme restent explicitement hors du périmètre.
- **Invariant :** la preuve d’utilisabilité n’accorde aucune autorité au rendu ou au testeur.

## 5. Pilote UX de Project Asteria

Le pilote `AST-UX-PILOT-CORE-SHELL-001` reprend le menu principal, le HUD d’exploration, l’inventaire, la pause et la modale de confirmation du chapitre 24. Il teste un ensemble cohérent de tâches sans multiplier les prototypes.

Les profils restent composables. Ils décrivent des réglages visuels et interactionnels ; ils ne diagnostiquent pas une personne et ne prétendent pas représenter tous les besoins possibles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asteria_ux_pilot:
  id: AST-UX-PILOT-CORE-SHELL-001
  ui_source: AST-UI-PILOT-CORE-SHELL-001
  task_flows:
    - start_or_continue_session
    - read_exploration_status
    - compare_and_move_inventory_item
    - pause_and_resume
    - confirm_or_cancel_destructive_action
  candidate_profiles:
    - AST-UX-PROFILE-REFERENCE-001
    - AST-UX-PROFILE-HIGH-CONTRAST-001
    - AST-UX-PROFILE-LARGE-TEXT-001
    - AST-UX-PROFILE-LOW-MOTION-001
    - AST-UX-PROFILE-REDUNDANT-COLOR-001
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pilote :** les cinq écrans partagent une même campagne et des identifiants stables.
- **Tâches :** chaque flux possède un début, une intention, un résultat attendu et une récupération possible.
- **Profils :** les variantes sont combinables et ne sont pas liées à une catégorie médicale.
- **Source :** le chapitre 24 reste propriétaire des scènes et composants que le pilote évalue.
- **Réserve :** aucun écran, profil ou parcours n’est déclaré exécuté.

## 6. Distinguer utilisabilité, accessibilité et préférence

L’utilisabilité décrit la capacité à accomplir une tâche avec compréhension et récupération. L’accessibilité cherche à éviter que la perception, la motricité, la cognition ou le contexte d’usage excluent une personne. Une préférence personnelle peut améliorer le confort sans constituer à elle seule une barrière.

Ces catégories se recouvrent mais ne sont pas interchangeables. Une option appréciée par beaucoup peut être essentielle pour certains joueurs.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
decision_vocabulary:
  usability_issue:
    test: task_is_possible_but_confusing_slow_or_error_prone
  accessibility_barrier:
    test: task_becomes_unavailable_or_unreasonably_difficult_for_a_need
  preference:
    test: alternative_changes_comfort_without_removing_a_barrier
  rule: classify_from_observed_effect_not_from_assumed_user_identity
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Utilisabilité :** le diagnostic part de la tâche et du comportement observé.
- **Barrière :** l’obstacle est décrit par son effet concret sans inférer un diagnostic.
- **Préférence :** un réglage de confort reste utile même lorsqu’il n’est pas indispensable.
- **Classification :** les catégories peuvent évoluer après une nouvelle observation.
- **Prudence :** l’identité supposée d’un participant ne remplace jamais l’analyse du parcours.

## 7. Hiérarchie de l’information

Un écran accessible ne donne pas le même poids à toutes les données. La hiérarchie distingue ce qui exige une action immédiate, ce qui soutient la décision courante, ce qui peut attendre et ce qui est purement décoratif.

Le test ne demande pas seulement « est-ce visible ? », mais « la bonne information est-elle découverte au bon moment et comprise sans exploration inutile ? ».

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
information_hierarchy:
  urgent:
    examples: [danger, failed_save, irreversible_confirmation]
    persistence: until_understood_or_resolved
  primary:
    examples: [current_goal, selected_item, health_state]
    placement: stable_and_predictable
  secondary:
    examples: [comparison_detail, recent_change, contextual_hint]
    disclosure: on_demand_or_contextual
  decorative:
    examples: [ornamental_frame, ambient_motion]
    removable: true
  invariant: urgent_information_is_never_encoded_by_color_alone
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Urgent :** le signal persiste assez longtemps pour être compris ou résolu.
- **Principal :** les données de décision gardent un emplacement et une forme prévisibles.
- **Secondaire :** le détail est disponible sans encombrer le parcours principal.
- **Décoratif :** l’ornement peut être réduit sans perte fonctionnelle.
- **Invariant :** un second canal — texte, forme, icône ou position — accompagne la couleur.

## 8. Réduire la charge cognitive

La charge cognitive augmente lorsque le joueur doit mémoriser des règles cachées, comparer trop d’options simultanément ou déduire l’état courant à partir d’indices dispersés. La solution n’est pas de supprimer toute complexité, mais de rendre la structure progressive et stable.

La divulgation progressive présente d’abord la décision utile, puis le détail, l’historique ou l’aide à la demande.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
cognitive_load_policy:
  visible_choices:
    target: task_relevant_subset
  memory_demand:
    reduce_with: [persistent_labels, summaries, recent_context]
  progressive_disclosure:
    first_layer: action_and_consequence
    second_layer: explanation_and_comparison
    third_layer: history_and_advanced_details
  consistency:
    same_action_same_label_same_location: required
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Choix :** l’écran montre d’abord les options nécessaires à la tâche courante.
- **Mémoire :** les labels et résumés évitent de retenir une information entre deux écrans.
- **Progression :** le détail reste accessible sans bloquer l’action principale.
- **Cohérence :** une action conserve son nom, son symbole et son emplacement logique.
- **Validation :** la réduction est confirmée par des tâches, pas par une impression de simplicité.

## 9. Regrouper et ordonner visuellement

La proximité, l’alignement et les séparateurs doivent rendre les groupes interprétables sans dépendre d’une bordure décorative. Les espaces ne sont pas des vides perdus : ils séparent des responsabilités et protègent la lecture.

Un groupe visuel doit également conserver un ordre logique pour le focus et la lecture séquentielle.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
visual_grouping:
  group_identity: title_or_accessible_label
  inside_spacing: compact_and_regular
  between_groups_spacing: larger_than_inside_spacing
  alignment: shared_axis
  separators: optional_not_sole_signal
  focus_order: follows_task_logic_not_visual_coordinates_only
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** un titre ou libellé explique la fonction du groupe.
- **Espacement :** la différence entre espace interne et externe rend la structure perceptible.
- **Alignement :** un axe partagé accélère le balayage et la comparaison.
- **Séparateur :** une ligne décorative ne remplace pas la structure sémantique.
- **Focus :** l’ordre de navigation suit la tâche même lorsque la composition change.

## 10. Densité, respiration et profils compacts

La densité ne se résume pas au nombre d’éléments. Elle dépend de la taille du texte, de la longueur des libellés, des cibles, du contraste, du mouvement et de la nécessité de comparer plusieurs données.

Un profil compact peut réduire des éléments secondaires, mais ne doit ni masquer une information critique ni réduire les cibles au point de rendre l’activation incertaine.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
density_profiles:
  reference:
    goal: balanced_reading_and_comparison
  compact:
    removes: [ornament, duplicate_secondary_detail]
    preserves: [critical_text, focus_indicator, target_spacing]
  spacious:
    increases: [line_spacing, group_spacing, target_size]
    reflows: true
  rejection: compact_profile_that_hides_required_state
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Référence :** le profil de base sert de comparaison, pas de vérité universelle.
- **Compact :** seules les couches secondaires et décoratives sont candidates à la réduction.
- **Spacieux :** l’augmentation de l’espace doit provoquer un reflow plutôt qu’un dépassement.
- **Cibles :** la densité ne sacrifie ni l’activation ni le focus visible.
- **Rejet :** un état requis disparu bloque le profil.

## 11. Contraste : objectifs et limites

Le contraste doit être mesuré entre les couleurs réellement affichées, y compris les états normal, survolé, focalisé, pressé, désactivé et les fonds semi-transparents. Une valeur de thème isolée ne suffit pas si le rendu final mélange plusieurs couches.

WCAG 2.2 fournit des repères utiles pour le texte et les composants. Le chapitre les traite comme objectifs documentés à vérifier dans les captures du jeu, sans revendiquer une conformité web globale.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
contrast_targets:
  text_regular:
    reference_ratio: "4.5:1"
    source: WCAG_2_2_SC_1_4_3
  text_large:
    reference_ratio: "3:1"
    source: WCAG_2_2_SC_1_4_3
  component_boundary_and_state:
    reference_ratio: "3:1"
    source: WCAG_2_2_SC_1_4_11
  focus_indicator:
    reference_ratio: "3:1_change"
    source: WCAG_2_2_SC_2_4_13_AAA
  scope: design_targets_not_game_certification
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Texte :** les rapports servent de cibles initiales et doivent être mesurés sur le rendu final.
- **Composants :** les limites et états nécessaires à l’usage doivent rester perceptibles.
- **Focus :** le changement entre état focalisé et non focalisé possède son propre objectif.
- **Portée :** la référence WCAG ne transforme pas le jeu en contenu web certifié.
- **Preuve :** chaque résultat doit citer couleur avant-plan, fond, capture et outil de mesure.

## 12. Mesurer les combinaisons réelles

Une bibliothèque de couleurs doit stocker les couples testés plutôt que seulement des couleurs indépendantes. Un même texte peut être lisible sur un panneau opaque et insuffisant sur une image ou un brouillard animé.

Les captures doivent couvrir les situations les plus défavorables : surbrillance, nuit, VFX, transparence, HDR et variation de plateforme.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
contrast_evidence:
  sample_id: AST-UX-CONTRAST-SAMPLE-001
  foreground_token: text.primary
  background_context: panel.reference_over_gameplay_worst_case
  state: focused
  measurement_tool: to_be_qualified
  measured_ratio: null
  target_ratio: "4.5:1"
  capture_id: null
  approval: pending
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** chaque mesure est reliée à un état et à un contexte de rendu.
- **Outil :** la méthode de mesure reste qualifiée et versionnée.
- **Résultat :** la valeur reste `null` tant qu’aucune capture n’a été analysée.
- **Cible :** le seuil documente l’intention indépendamment du résultat.
- **Approbation :** une mesure seule n’approuve ni le composant ni tout le profil.

## 13. Tailles de texte et échelle utilisateur

La taille nominale d’une police ne prouve pas la lisibilité. Le test doit considérer densité de pixels, distance d’affichage, graisse, contraste, interligne, longueur de ligne, langue et facteur d’échelle choisi.

L’échelle utilisateur doit agrandir les composants et provoquer un reflow. Un simple `scale` local peut flouter ou faire sortir le contenu sans recalculer les tailles minimales.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
text_scale_contract:
  profiles: [candidate_min, reference, candidate_large]
  affects: [font_sizes, icons, minimum_sizes, spacing, wrap]
  preserves: [information, focus_order, action_availability]
  forbids:
    - clipping_required_text
    - horizontal_overflow_without_alternative
    - scale_transform_as_only_strategy
  evidence: per_resolution_and_distance
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profils :** les valeurs restent candidates jusqu’aux mesures sur les appareils cibles.
- **Propagation :** texte, icônes, cibles et espacements évoluent ensemble.
- **Préservation :** aucune action ou information requise ne disparaît à grande échelle.
- **Interdits :** le clipping et le zoom local isolé ne sont pas des solutions d’accessibilité.
- **Preuve :** les résultats citent résolution, distance, langue et profil.

## 14. Typographie, longueur de ligne et espacement

Une police qualifiée doit conserver ses glyphes, accents, chiffres, ponctuation et styles utiles. La graisse et la casse ne remplacent pas une hiérarchie claire.

Les textes longs utilisent une largeur de lecture bornée, des paragraphes courts et un espacement configurable. Une ligne très longue ralentit le retour visuel ; une colonne trop étroite fragmente les mots et augmente les mouvements oculaires.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
typography_review:
  font_asset: AST-UI-FONT-BODY-001
  glyph_sets: [latin_extended, digits, punctuation, symbols_required_by_game]
  styles: [regular, semibold]
  line_length: measured_in_context
  line_spacing: profile_driven
  all_caps: short_labels_only
  fallback_chain: documented_and_tested
  licence_status: pending
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Glyphes :** le jeu de caractères réel est testé, y compris les traductions prévues.
- **Styles :** la hiérarchie repose sur un nombre limité de variantes cohérentes.
- **Lecture :** longueur de ligne et interligne sont évalués dans le panneau final.
- **Casse :** les textes longs évitent les capitales continues.
- **Licence :** la police reste bloquée tant que ses droits ne sont pas qualifiés.

## 15. Ne jamais coder une information par la couleur seule

La couleur peut renforcer un statut, mais une différence importante doit également être portée par un texte, une forme, une icône, une texture, une position ou un motif. Cette redondance aide aussi lorsque l’écran est terne, compressé ou observé en périphérie.

Les mots « rouge » et « vert » ne doivent pas être la seule instruction lorsque la tâche dépend de leur distinction.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
redundant_encoding:
  status_success:
    color: semantic.success
    icon: check
    label: action_completed
  status_warning:
    color: semantic.warning
    icon: triangle_exclamation
    label: attention_required
  status_error:
    color: semantic.error
    icon: octagon_cross
    label: action_failed
  invariant: meaning_survives_grayscale_review
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Succès :** la coche et le libellé conservent le sens sans la teinte.
- **Avertissement :** la forme et le texte distinguent l’état d’un simple accent décoratif.
- **Erreur :** le message décrit le problème et la prochaine action possible.
- **Gris :** une revue sans couleur vérifie la redondance du codage.
- **Invariant :** la couleur reste un renforcement, jamais l’unique canal.

## 16. Profils de perception des couleurs

Les profils de couleur ne doivent pas promettre de « corriger » la vision d’une personne. Ils modifient plutôt les palettes, motifs et contrastes pour rendre les catégories distinctes dans les tâches ciblées.

Une simulation logicielle peut révéler un risque, mais ne remplace pas les tests avec des personnes ni la vérification des codages redondants.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
color_profiles:
  reference:
    palette: AST-UI-PALETTE-REFERENCE-001
  high_separation:
    palette: AST-UI-PALETTE-SEPARATED-001
    adds: [patterns, labels, icon_shapes]
  grayscale_review:
    purpose: verify_non_color_channels
  simulations:
    status: diagnostic_only
    approval_authority: none
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Référence :** la palette principale reste un point de comparaison.
- **Séparation :** le profil renforce simultanément teintes, valeurs, motifs et formes.
- **Gris :** la perte volontaire de couleur révèle les informations non redondantes.
- **Simulation :** l’outil aide au diagnostic mais n’approuve pas un écran.
- **Autorité :** la décision combine mesures, tâches et retours humains.

## 17. Variantes de contraste

Une variante de contraste ne consiste pas à rendre chaque élément noir ou blanc. Elle doit préserver la hiérarchie, les états interactifs, les distinctions de profondeur et les informations non textuelles nécessaires.

Les arrière-plans animés ou détaillés peuvent recevoir un panneau opaque, un flou qualifié ou une zone de repos visuel plutôt qu’une simple augmentation de la luminosité du texte.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
contrast_profiles:
  reference:
    background_treatment: designed_per_screen
  high_contrast:
    panel_opacity: increased
    decorative_layers: reduced
    focus_indicator: reinforced
    critical_icons: outlined
  low_glare:
    peak_brightness: reduced_candidate
    large_white_areas: avoided
  review_states: [normal, hover, focus, pressed, disabled, error]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Référence :** le profil de base reste évalué avec les mêmes tâches.
- **Contraste élevé :** la variante agit sur fond, décor, focus et icônes, pas seulement sur le texte.
- **Éblouissement :** les valeurs restent candidates jusqu’aux tests d’affichage.
- **États :** chaque état interactif conserve une distinction mesurable.
- **Cohérence :** les variantes partagent la même signification sémantique.

## 18. Focus visible et état courant

Le focus doit être distinguable du survol, de la sélection persistante et de l’état pressé. Un halo subtil qui disparaît sur certains fonds ne constitue pas une indication fiable.

Le critère WCAG 2.4.13 propose une référence renforcée pour la surface et le contraste du focus. Dans Project Asteria, il sert d’objectif de conception à inspecter dans chaque profil et non de certification.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
focus_visual_contract:
  states:
    hover: pointer_location
    focus: keyboard_or_gamepad_navigation_target
    selected: persistent_choice
    pressed: current_activation
  focus_indicator:
    minimum_reference: equivalent_to_2_css_pixel_perimeter
    change_contrast_reference: "3:1"
    redundant_shape_change: required
  test_backgrounds: [light, dark, image, vfx_overlay]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **États :** chaque état possède une fonction distincte et ne réutilise pas un seul effet ambigu.
- **Périmètre :** la référence de surface évite un indicateur minuscule.
- **Contraste :** le changement est évalué entre l’état focalisé et l’état normal.
- **Redondance :** une bordure ou forme complète le changement de couleur.
- **Fonds :** le focus est inspecté sur les contextes les plus défavorables.

## 19. Ordre logique de navigation

L’ordre de focus suit l’intention de la tâche, pas seulement la position actuelle des contrôles. Un reflow, un profil compact ou une langue RTL peut modifier la géométrie sans devoir rendre la navigation incohérente.

Les groupes complexes définissent une entrée, une sortie et une règle locale. Les raccourcis ne doivent pas piéger le joueur dans une région.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
focus_order:
  screen_entry: first_required_action_or_heading
  groups:
    - id: primary_actions
      order: task_priority
    - id: inventory_grid
      order: row_or_column_documented
    - id: details_panel
      order: after_selected_item
  modal:
    traps_focus: true
    restores_previous_valid_target: true
  screen_exit: back_or_explicit_close
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrée :** la première cible correspond à l’action utile ou au début logique du contenu.
- **Groupes :** chaque zone possède une règle documentée et testable.
- **Inventaire :** l’ordre de grille reste stable et prévisible.
- **Modale :** le focus ne quitte pas la fenêtre active et revient sur une cible valide.
- **Sortie :** un moyen cohérent permet de revenir sans parcourir tout l’écran.

## 20. Taille et espacement des cibles

Les petites cibles rapprochées augmentent les activations involontaires. WCAG 2.2 propose une référence de 24 par 24 pixels CSS ou un espacement équivalent pour les entrées pointeur ; le jeu utilise cette valeur comme plancher de conception à adapter à la densité et à la distance d’affichage.

Les actions importantes visent une surface plus généreuse et ne reposent pas sur la seule zone visible de l’icône.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
target_review:
  minimum_reference: "24x24_css_px_or_equivalent_spacing"
  preferred_for_primary_actions: larger_than_minimum
  hit_area:
    includes: visible_component_and_documented_padding
    excludes: overlapping_neighbor_targets
  contexts: [mouse, touch_if_supported, virtual_pointer]
  evidence: screenshot_plus_hit_rect_overlay
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Référence :** le seuil sert de plancher mesurable et non d’optimum universel.
- **Actions principales :** une surface plus large réduit les erreurs de pointage.
- **Hitbox :** la zone active est documentée et ne chevauche pas une cible voisine.
- **Contextes :** chaque périphérique effectivement pris en charge est testé.
- **Preuve :** la capture superpose le rectangle visuel et la zone interactive.

## 21. Identifier les sources de mouvement

Le mouvement peut venir d’un tween, d’un shader, d’un VFX, d’une caméra, d’un défilement automatique, d’un curseur pulsant ou d’un fond vidéo. Un réglage global ne fonctionne que si ces sources sont inventoriées et classées.

Le mouvement informatif, le mouvement de transition et le mouvement décoratif n’ont pas la même priorité.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
motion_inventory:
  informative:
    examples: [incoming_damage_direction, focus_transition]
    alternative: static_or_stepwise_signal
  transitional:
    examples: [panel_enter, list_reorder]
    alternative: shortened_or_instant
  decorative:
    examples: [ambient_particles, parallax, pulse]
    alternative: disabled
  owner: visual_accessibility_profile
  gameplay_timing_authority: none
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Informatif :** une alternative statique conserve le sens lorsque l’animation est réduite.
- **Transition :** la durée peut être raccourcie ou supprimée sans perdre l’état final.
- **Décoratif :** la couche peut disparaître sans conséquence fonctionnelle.
- **Propriétaire :** le profil visuel orchestre les variantes sans éditer les assets sources.
- **Autorité :** le réglage ne modifie jamais le timing gameplay.

## 22. Profil de mouvement réduit

Un profil de mouvement réduit n’accélère pas aveuglément toutes les animations. Il remplace les déplacements importants par des fondus, des changements d’état ou des étapes courtes ; il peut désactiver parallaxe, tremblement et pulsation décorative.

L’état final et la disponibilité des actions doivent rester identiques au profil de référence.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
reduced_motion_profile:
  id: AST-UX-PROFILE-LOW-MOTION-001
  transitions:
    large_translation: replace_with_fade_or_instant
    small_state_change: shorten_candidate
  disable:
    - decorative_parallax
    - continuous_pulse
    - nonessential_camera_shake
  preserve:
    - final_state
    - critical_timing_information
    - input_availability
  values: pending_runtime_measurement
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le profil possède un ID stable et composable.
- **Remplacement :** les grands déplacements deviennent des signaux moins mobiles.
- **Désactivation :** les mouvements continus non essentiels sont supprimés.
- **Préservation :** les fonctions et informations restent identiques.
- **Mesure :** les durées numériques ne sont pas approuvées avant exécution.

## 23. Clignotements, pulsations et sécurité visuelle

Les effets rapides et répétés sont revus avant intégration. Le critère WCAG « Three Flashes or Below Threshold » fournit une référence de prudence pour les flashs ; le chapitre ne transforme pas cette revue documentaire en avis médical ni en garantie de sécurité.

La voie préférée consiste à éviter les flashs inutiles, à proposer une variante stable et à conserver le sens par un autre canal.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
flash_review:
  source_id: null
  frequency_measurement: pending
  screen_area_measurement: pending
  luminance_change_measurement: pending
  reference: WCAG_2_2_SC_2_3_1
  alternatives: [steady_highlight, icon_change, text_notice]
  approval: blocked_until_measured
  medical_claim: none
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Source :** chaque effet concerné est identifié séparément.
- **Mesures :** fréquence, surface et variation lumineuse restent à établir avec un outil qualifié.
- **Référence :** le critère W3C guide la revue sans constituer une expertise médicale.
- **Alternatives :** des signaux stables conservent l’information.
- **Blocage :** l’effet n’est pas approuvé tant que les mesures et variantes manquent.

## 24. Messages d’erreur compréhensibles

Un message d’erreur décrit ce qui s’est passé, ce qui a été conservé, ce que le joueur peut faire et, lorsque pertinent, comment obtenir plus de détails. Un code interne seul ne suffit pas.

Le message ne blâme pas la personne et ne prétend pas qu’une action a échoué lorsque le statut réel est indéterminé.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
error_message_contract:
  title: action_not_completed
  cause: known_cause_or_explicitly_unknown
  preserved_state: what_remains_unchanged
  next_actions:
    - retry_when_safe
    - change_input
    - cancel_and_return
  technical_details: optional_expandable
  correlation_id: optional_non_secret
  tone: factual_and_non_blame
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Titre :** le message annonce le résultat de l’action plutôt qu’un code technique.
- **Cause :** l’inconnu reste explicite au lieu d’être inventé.
- **État :** le joueur sait ce qui a été conservé ou annulé.
- **Actions :** les options proposées respectent l’idempotence et les capacités réelles.
- **Détails :** les informations techniques restent accessibles sans envahir le message principal.

## 25. Prévenir les erreurs avant la confirmation

La prévention commence avant le dialogue final : labels précis, aperçu des conséquences, contraintes visibles, valeurs par défaut prudentes et désactivation expliquée réduisent les erreurs.

Une confirmation répétée sur chaque action banale crée de l’habituation et masque les décisions réellement risquées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
error_prevention:
  before_action:
    - precise_label
    - visible_constraints
    - consequence_preview
    - safe_default
  confirmation_required_when:
    - irreversible_or_costly
    - large_scope
    - ambiguous_target
  confirmation_avoided_when:
    - frequent_low_risk_action
    - immediate_undo_available
  rejection: confirmation_as_substitute_for_clear_design
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Avant :** le contrôle explique la portée avant l’activation.
- **Risque :** la confirmation est proportionnée à l’irréversibilité et à l’étendue.
- **Habituation :** les actions fréquentes et récupérables évitent les dialogues systématiques.
- **Annulation :** un undo fiable peut remplacer une confirmation intrusive.
- **Rejet :** une modale ne corrige pas un libellé ambigu ou une cible mal identifiée.

## 26. Confirmations proportionnées au risque

Une confirmation utile nomme l’objet, l’étendue et la conséquence. Les boutons « Oui » et « Non » sont remplacés par des verbes explicites comme « Supprimer la sauvegarde » et « Conserver la sauvegarde ».

L’action la plus sûre reçoit le focus initial lorsque le choix est destructif, sauf raison documentée et testée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
confirmation_dialog:
  subject: selected_save_slot_name
  consequence: permanently_remove_local_save
  scope: one_slot
  primary_action:
    label: remove_save
    destructive: true
    focus_initial: false
  safe_action:
    label: keep_save
    focus_initial: true
  escape_action: keep_save
  details: timestamp_and_progress_summary
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sujet :** le joueur voit exactement l’objet concerné.
- **Conséquence :** la formulation décrit l’irréversibilité sans euphémisme.
- **Action destructive :** le bouton porte un verbe spécifique et un style cohérent.
- **Action sûre :** le focus initial et la touche retour conservent l’état.
- **Détails :** un résumé réduit le risque de supprimer le mauvais élément.

## 27. Annulation, retour et restauration

Chaque parcours possède un moyen de revenir sans perdre un travail non validé. L’annulation doit préciser si elle abandonne un brouillon, ferme seulement une fenêtre ou restaure l’état précédent.

Après une erreur ou une modale, le focus revient sur une cible valide associée à la tâche interrompue.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
recovery_contract:
  cancel:
    effect: discard_uncommitted_ui_draft_only
    domain_state: unchanged
  back:
    effect: return_to_previous_screen_context
  retry:
    precondition: operation_is_safe_or_idempotent
  undo:
    availability: when_committed_action_is_reversible
  focus_restore:
    checks: [exists, visible, enabled, focusable]
    fallback: first_valid_control_in_parent_context
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Annuler :** seul le brouillon de présentation non committé est abandonné.
- **Retour :** le contexte précédent est restauré sans réinitialiser la tâche.
- **Réessayer :** l’action n’est proposée que lorsque le contrat autorise une nouvelle tentative.
- **Annuler après commit :** un undo séparé traite les opérations réellement réversibles.
- **Focus :** la cible restaurée est vérifiée avant activation.

## 28. Informations persistantes et contraintes de temps

Une notification critique ne doit pas disparaître avant d’avoir été comprise. Les informations temporaires disposent d’un journal, d’une répétition contrôlée ou d’un panneau consultable.

Les contraintes de temps gameplay restent dans leurs systèmes propriétaires ; l’interface peut seulement les présenter et proposer des réglages autorisés.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
time_and_persistence:
  critical_message:
    dismissal: explicit_or_resolved
    history: retained_in_notification_log
  transient_feedback:
    duration: candidate
    repeat_access: available
  timed_task:
    authority: gameplay_system
    visual_warning: redundant
    accommodation: only_if_supported_by_authoritative_rule
  system_clock_dependency: none_for_task_order
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Critique :** le message persiste jusqu’à une action ou une résolution explicite.
- **Transitoire :** une voie permet de relire l’information après sa disparition.
- **Temps :** le gameplay conserve l’autorité sur toute contrainte temporelle.
- **Réglage :** l’interface n’invente pas une extension que le système n’accepte pas.
- **Ordre :** la séquence de tâche ne dépend pas de l’horloge système.

## 29. Notifications et interruptions

Les notifications sont classées par urgence, action requise et durée de pertinence. Une animation spectaculaire ne doit pas faire passer un message décoratif avant une erreur de sauvegarde.

Le regroupement réduit le bruit, mais ne fusionne pas des événements qui exigent des décisions distinctes.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
notification_policy:
  blocking:
    requires_action: true
    examples: [failed_save_needs_choice]
  urgent:
    requires_action: contextual
    examples: [critical_status_change]
  informative:
    requires_action: false
    examples: [item_added, objective_updated]
  ambient:
    requires_action: false
    examples: [world_flavor]
  queue:
    bounded: true
    deduplication: by_semantic_identity
    history: available
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Bloquante :** la notification arrête le flux uniquement lorsqu’une décision est nécessaire.
- **Urgente :** le signal reste visible sans masquer une action prioritaire.
- **Informative :** les événements proches peuvent être regroupés selon leur identité sémantique.
- **Ambiante :** le bruit décoratif est supprimé en premier dans les profils simplifiés.
- **File :** la capacité est bornée et l’historique permet une relecture.

## 30. Aide contextuelle et apprentissage progressif

L’aide apparaît au moment où une personne peut l’utiliser. Un tutoriel initial exhaustif surcharge la mémoire et devient obsolète avant que l’action correspondante ne soit disponible.

Les rappels restent consultables et ne bloquent pas les joueurs qui maîtrisent déjà le système.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
contextual_help:
  trigger: first_relevant_context_or_explicit_request
  content:
    - action_goal
    - input_or_control
    - immediate_consequence
  persistence:
    replayable: true
    dismissible: true
  adaptation:
    repeated_failure: offer_hint_without_forcing_action
  analytics:
    authority: descriptive_only
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Déclenchement :** l’aide correspond au contexte réellement actif.
- **Contenu :** la consigne relie intention, contrôle et conséquence.
- **Persistance :** le joueur peut fermer puis retrouver l’explication.
- **Échec :** un indice est proposé sans exécuter l’action à la place de la personne.
- **Analyse :** les données de consultation décrivent le parcours sans décider du gameplay.

## 31. Profils d’accessibilité composables

Un profil est un ensemble de valeurs initiales que le joueur peut ensuite modifier. Les options ne doivent pas être verrouillées derrière une étiquette médicale ou un questionnaire obligatoire.

Les profils partagent un schéma commun et enregistrent les overrides séparément, afin qu’une mise à jour du profil ne supprime pas les choix personnels.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
accessibility_profile_model:
  profile_id: AST-UX-PROFILE-REFERENCE-001
  schema_version: 1
  defaults:
    ui_scale: reference
    contrast: reference
    color_encoding: redundant
    motion: reference
    focus_strength: reference
  user_overrides: separate_map
  diagnosis_required: false
  composable: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le profil possède un ID stable et une version de schéma.
- **Défauts :** les valeurs initiales sont explicites et comparables.
- **Overrides :** les choix personnels restent séparés du preset.
- **Accès :** aucun diagnostic n’est requis pour activer une option.
- **Composition :** les réglages peuvent être combinés sans profils exclusifs.

## 32. Représenter les réglages visuels

La ressource de réglages transporte des préférences de présentation. Elle ne contient ni santé, ni inventaire, ni autorisation métier. Les plages numériques sont des candidats à valider dans la campagne de test.

Le code ci-dessous illustre un contrat typé ; il reste à créer, charger et exécuter dans le projet.

> **[VSC] Visual Studio Code — Créer : `src/ui/accessibility/visual_accessibility_settings.gd`.**

```gdscript
class_name VisualAccessibilitySettings
extends Resource

@export_range(0.75, 1.75, 0.05) var ui_scale: float = 1.0
@export var high_contrast: bool = false
@export var reduced_motion: bool = false
@export var redundant_color_coding: bool = true
@export var reinforced_focus: bool = false

func duplicate_for_edit() -> VisualAccessibilitySettings:
    return duplicate(true) as VisualAccessibilitySettings

func clamp_candidates() -> void:
    ui_scale = clampf(ui_scale, 0.75, 1.75)
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe :** `Resource` permet de transporter et sérialiser un ensemble de préférences visuelles.
- **Plage :** `@export_range` documente des candidats d’éditeur et ne prouve pas leur adéquation.
- **Booléens :** chaque option contrôle une responsabilité visuelle distincte.
- **Copie :** `duplicate(true)` crée un brouillon éditable sans modifier immédiatement la ressource active.
- **Borne :** `clampf` protège le format, tandis que la validation utilisateur reste une étape séparée.

## 33. Séparer brouillon, aperçu et application

Un menu de réglages doit permettre l’aperçu sans écrire immédiatement la configuration persistée. `Appliquer`, `Annuler` et `Rétablir` possèdent des effets distincts.

L’adaptateur de présentation applique seulement le rendu. La sauvegarde des préférences passe par le service prévu par l’architecture du Livre II.

> **[VSC] Visual Studio Code — Créer : `src/ui/accessibility/accessibility_settings_session.gd`.**

```gdscript
class_name AccessibilitySettingsSession
extends RefCounted

var committed: VisualAccessibilitySettings
var draft: VisualAccessibilitySettings

func begin(current: VisualAccessibilitySettings) -> void:
    committed = current
    draft = current.duplicate_for_edit()

func preview(adapter: VisualAccessibilityAdapter) -> void:
    draft.clamp_candidates()
    adapter.preview(draft)

func cancel(adapter: VisualAccessibilityAdapter) -> void:
    adapter.apply(committed)
    draft = committed.duplicate_for_edit()

func commit(adapter: VisualAccessibilityAdapter) -> VisualAccessibilitySettings:
    draft.clamp_candidates()
    committed = draft.duplicate_for_edit()
    adapter.apply(committed)
    return committed
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **États :** `committed` représente la préférence active et `draft` la modification non validée.
- **Début :** `begin` crée une copie profonde afin d’éviter une mutation partagée.
- **Aperçu :** l’adaptateur reçoit un brouillon borné sans persistance implicite.
- **Annulation :** le rendu et le brouillon reviennent aux valeurs validées.
- **Commit :** la fonction retourne une ressource à transmettre au service de sauvegarde, sans l’écrire elle-même.

## 34. Catalogue des réglages

Chaque réglage possède une fonction, une valeur de référence, une portée et une méthode de vérification. Une option sans effet observable ou sans écran couvert ne doit pas être publiée.

Le catalogue évite que deux menus exposent des libellés différents pour la même préférence.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
setting_catalog:
  - id: visual.ui_scale
    scope: all_ui
    verification: multi_resolution_reflow
  - id: visual.contrast_profile
    scope: theme_variation
    verification: measured_state_pairs
  - id: visual.color_redundancy
    scope: semantic_statuses_and_maps
    verification: grayscale_task_review
  - id: visual.motion_profile
    scope: ui_vfx_camera_presentation
    verification: motion_inventory_and_task_equivalence
  - id: visual.focus_profile
    scope: focusable_controls
    verification: keyboard_and_gamepad_path
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identifiant :** la clé reste stable indépendamment du libellé traduit.
- **Portée :** chaque option nomme les éléments qu’elle doit modifier.
- **Vérification :** une méthode observable accompagne chaque réglage.
- **Cohérence :** les écrans consomment le catalogue au lieu de recréer leurs propres options.
- **Publication :** une option incomplète reste masquée ou marquée expérimentale.

## 35. Compatibilité et migration des profils

Les réglages persistés portent une version. Lorsqu’un token ou une option disparaît, la migration conserve les choix encore valides et documente le repli appliqué.

Une valeur inconnue ne doit pas rendre le menu inaccessible ni réinitialiser silencieusement tous les réglages.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
profile_migration:
  source_schema: 1
  target_schema: 2
  mappings:
    visual.motion_reduction: visual.motion_profile
  removed_values:
    legacy_flash_mode: fallback_to_safe_default
  unknown_key:
    preserve_in_raw_snapshot: true
    apply_to_runtime: false
  migration_report: required
  silent_full_reset: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Versions :** la source et la cible sont explicites.
- **Mapping :** un renommage conserve l’intention lorsque les contrats restent compatibles.
- **Suppression :** la valeur obsolète reçoit un repli documenté.
- **Inconnu :** la donnée est conservée pour diagnostic mais non appliquée.
- **Rapport :** la migration laisse une trace sans réinitialisation globale silencieuse.

## 36. Scénarios de tâches prioritaires

Un test utilisateur porte sur une tâche concrète, pas sur la question générale « aimez-vous l’interface ? ». Chaque scénario précise le contexte, l’objectif, les données initiales, les résultats acceptables et les conditions d’arrêt.

Le facilitateur ne révèle pas le chemin attendu avant l’observation.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
task_scenario:
  id: AST-UX-TASK-INVENTORY-COMPARE-001
  context: player_has_two_tools_and_one_full_container
  goal: compare_tools_and_move_one_item_to_valid_container
  starting_screen: exploration_hud
  success:
    - correct_item_selected
    - comparison_understood
    - valid_transfer_requested
  recovery:
    - invalid_target_explained
    - player_can_return_without_loss
  stop_conditions: [participant_requests_stop, technical_blocker, consent_withdrawn]
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le scénario peut être rejoué et relié à ses observations.
- **Contexte :** les données initiales sont contrôlées pour comparer les sessions.
- **Succès :** plusieurs résultats observables remplacent une note subjective unique.
- **Récupération :** le traitement de l’erreur fait partie de la tâche.
- **Arrêt :** la session cesse immédiatement lorsque la personne le demande ou retire son consentement.

## 37. Recrutement et diversité des parcours

Un petit panel peut révéler des barrières importantes, mais ses résultats ne sont pas généralisables à toutes les personnes. Les participants sont sélectionnés selon les tâches, les périphériques, l’expérience de jeu et les besoins pertinents.

Le recrutement n’exige pas de diagnostic médical. Les informations sensibles ne sont collectées que lorsqu’elles sont nécessaires, consenties et protégées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
participant_sampling:
  goal: cover_relevant_interaction_strategies
  dimensions:
    - game_experience
    - input_device_experience
    - visual_preferences_and_needs_self_described
    - familiarity_with_target_genre
  avoid:
    - one_participant_represents_all
    - medical_diagnosis_as_entry_requirement
    - unnecessary_sensitive_data
  statistical_claim: none_for_small_qualitative_sample
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Objectif :** le recrutement couvre des stratégies d’usage liées aux tâches.
- **Dimensions :** l’expérience et les besoins sont décrits par les participants eux-mêmes.
- **Prudence :** une personne ne représente ni un handicap ni tout un public.
- **Données :** les informations non nécessaires ne sont pas demandées.
- **Conclusion :** un petit échantillon qualitatif ne produit pas de signification statistique.

## 38. Consentement, confidentialité et retrait

Avant la session, la personne sait ce qui sera observé, enregistré, conservé et partagé. Le consentement peut être retiré sans justification et sans affecter une relation future.

Les identités, enregistrements, coordonnées et données sensibles restent hors du dépôt public. Les rapports utilisent des identifiants pseudonymes et des citations approuvées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
participant_data_governance:
  participant_id: AST-UX-PARTICIPANT-PSEUDONYM-001
  consent:
    observation: required
    audio_recording: separate_optional
    screen_recording: separate_optional
    quotation: separate_optional
  withdrawal:
    available_any_time: true
    retention_action: documented
  public_repository:
    personal_data: forbidden
    raw_recordings: forbidden
  retention_period: defined_before_collection
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identifiant :** le rapport utilise un pseudonyme sans exposer l’identité.
- **Consentements :** observation, audio, écran et citation sont des autorisations séparées.
- **Retrait :** la conséquence sur les données déjà collectées est annoncée à l’avance.
- **Dépôt :** aucune donnée personnelle ni prise brute n’entre dans le dépôt public.
- **Conservation :** la durée est définie avant la première collecte.

## 39. Préparer une session reproductible

La session documente la build, le matériel, la résolution, le profil actif, la langue, le périphérique et les données de départ. Une différence de configuration peut expliquer un résultat et ne doit pas être confondue avec un problème d’interface.

Le scénario de secours prévoit les pannes d’enregistrement et les blocages techniques sans forcer la personne à continuer.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
session_setup:
  session_id: AST-UX-SESSION-001
  build_commit: null
  platform: pending
  display:
    resolution: pending
    physical_size: pending
    viewing_distance: pending
  input_profile: pending
  locale: pending
  accessibility_profile: pending
  fixture_version: AST-UX-FIXTURE-CORE-001
  recording_status: not_started
  fallback_notes_template: ready
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Session :** un identifiant relie configuration, tâches et observations.
- **Build :** le commit reste `null` tant qu’aucune version testable n’existe.
- **Affichage :** résolution, taille physique et distance sont distinguées.
- **Fixture :** les données initiales portent une version stable.
- **Secours :** un gabarit de notes permet de poursuivre seulement si le consentement et le confort le permettent.

## 40. Faciliter sans diriger

Le facilitateur rappelle que le produit est testé, pas la personne. Il demande de réaliser la tâche, observe, puis pose des questions neutres. Il évite de nommer le contrôle attendu ou de corriger immédiatement le parcours.

Une aide donnée est consignée, car elle modifie l’interprétation du résultat.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
facilitation_protocol:
  opening:
    - product_is_being_tested
    - participant_can_pause_or_stop
    - think_aloud_optional
  prompts:
    neutral: ["Que cherchez-vous maintenant ?", "Qu’attendez-vous de cette action ?"]
    forbidden: ["Cliquez sur le bouton bleu", "La réponse est dans le panneau droit"]
  assistance:
    record_time_and_content: true
    mark_task_as_assisted: true
  closing:
    - debrief
    - confirm_data_preferences
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Ouverture :** la personne connaît ses droits et le but de la session.
- **Verbalisation :** penser à voix haute reste optionnel.
- **Questions :** les formulations explorent l’intention sans révéler le chemin.
- **Aide :** toute intervention est horodatée et qualifie la tâche comme assistée.
- **Clôture :** le débrief et les préférences de données sont confirmés.

## 41. Consigner les observations brutes

Une observation décrit un comportement visible : cible cherchée, action tentée, message lu, retour arrière, pause ou demande d’aide. L’interprétation vient ensuite dans un champ séparé.

Les citations sont courtes, consenties et rattachées au contexte de tâche.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
observation_record:
  observation_id: AST-UX-OBS-001
  session_id: AST-UX-SESSION-001
  task_id: AST-UX-TASK-INVENTORY-COMPARE-001
  step: locate_comparison
  timestamp_from_session_start: pending
  observed_behavior: participant_scans_item_list_then_opens_unrelated_filter
  facilitator_assistance: none
  participant_quote: null
  interpretation: separate_pending
  media_reference: restricted_or_null
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Lien :** session, tâche et étape rendent l’observation traçable.
- **Temps :** la durée est mesurée depuis le début de session, pas avec l’horloge système comme ordre métier.
- **Comportement :** la description évite d’attribuer une intention non exprimée.
- **Interprétation :** l’hypothèse reste séparée et révisable.
- **Média :** la référence pointe vers un stockage restreint ou reste absente.

## 42. Mesures qualitatives et quantitatives

Les mesures servent à comparer des variantes et à détecter des problèmes, pas à réduire l’expérience à un score unique. Le temps, les erreurs, l’aide, les retours arrière et la confiance déclarée sont interprétés avec le contexte.

Une tâche accomplie avec une forte détresse, des essais répétés ou une aide importante n’est pas équivalente à un parcours fluide.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
task_metrics:
  completion:
    values: [unassisted, assisted, not_completed, stopped]
  navigation_errors:
    definition: action_leads_away_from_task_or_invalid_target
  recovery:
    values: [self_recovered, recovered_after_feedback, assisted, not_recovered]
  elapsed_duration:
    source: monotonic_session_timer
    interpretation: contextual_not_pass_fail_alone
  confidence:
    source: optional_self_report
  aggregation:
    preserve_individual_notes: true
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Achèvement :** le statut distingue autonomie, aide et arrêt.
- **Erreurs :** la définition dépend de la tâche et non d’un clic arbitraire.
- **Récupération :** le retour après erreur est mesuré séparément.
- **Durée :** un compteur monotone mesure l’intervalle sans devenir un seuil universel.
- **Agrégation :** les synthèses conservent les observations individuelles et leurs limites.

## 43. Qualifier la gravité d’un problème

La gravité combine l’impact sur la tâche, la fréquence observée, la disponibilité d’une récupération et l’étendue des profils touchés. Elle ne dépend pas seulement du nombre de participants.

Une barrière empêchant une tâche critique peut être prioritaire même si elle n’apparaît qu’une fois.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
issue_severity:
  impact:
    blocker: task_cannot_continue
    major: task_completed_only_with_assistance_or_loss
    moderate: delay_confusion_or_repeated_error
    minor: friction_without_task_risk
  recovery: [none, difficult, available, immediate]
  frequency: observed_count_with_sample_scope
  reach: profiles_and_screens_affected
  priority: human_decision
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Impact :** la classification part de la conséquence sur la tâche.
- **Récupération :** la présence et le coût d’un retour modifient la gravité.
- **Fréquence :** le compteur cite toujours la taille et la nature de l’échantillon.
- **Étendue :** les écrans, profils et plateformes concernés sont listés.
- **Priorité :** la décision finale combine risque, coût et calendrier humainement.

## 44. Transformer une observation en problème actionnable

Un ticket UX relie la preuve, le contexte, l’impact, l’hypothèse et le critère de fermeture. Il ne se contente pas de « rendre plus intuitif ».

La correction proposée reste une hypothèse tant qu’elle n’a pas été retestée.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
ux_issue:
  issue_id: AST-UX-ISSUE-001
  title: inventory_comparison_entry_is_not_discoverable
  evidence: [AST-UX-OBS-001, AST-UX-OBS-004]
  affected_tasks: [AST-UX-TASK-INVENTORY-COMPARE-001]
  affected_profiles: [reference, large_text]
  impact: major
  hypothesis: comparison_action_is_visually_grouped_with_filters
  proposed_change: separate_and_label_comparison_action
  closure_test: rerun_task_with_same_fixture_and_profiles
  status: open
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Titre :** la formulation décrit le comportement et la zone concernée.
- **Preuves :** les observations restent consultables et ne sont pas réécrites dans le ticket.
- **Impact :** la gravité est reliée à la tâche.
- **Hypothèse :** la cause supposée reste distincte du fait observé.
- **Fermeture :** la correction doit être retestée avec une fixture comparable.

## 45. Analyser sans sur-généraliser

Les résultats d’un petit nombre de sessions peuvent révéler des barrières et guider une correction, mais ils ne permettent pas d’affirmer que tous les joueurs réussiront. Le rapport précise le périmètre, le recrutement, les profils, les appareils et les limites.

Les tests avec des personnes complètent les contrôles techniques ; ils ne remplacent ni les mesures de contraste, ni l’inventaire du focus, ni les revues de code.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
analysis_scope:
  sessions_completed: 0
  sample_description: not_collected
  tasks_covered: planned_only
  platforms_covered: none
  findings:
    observed: []
    inferred: []
  generalization: forbidden_without_support
  combine_with:
    - technical_checks
    - contrast_measurements
    - focus_path_review
    - standards_based_review
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Sessions :** la valeur zéro empêche toute présentation fictive de résultats.
- **Échantillon :** la description reste absente tant qu’aucun recrutement n’a eu lieu.
- **Constats :** faits observés et inférences occupent des listes séparées.
- **Généralisation :** les conclusions restent limitées au périmètre réel.
- **Combinaison :** les tests utilisateurs et contrôles techniques se complètent.

## 46. Rapport utilisateur

Le rapport consolide configuration, tâches, observations, problèmes, citations consenties, décisions et réserves. Il ne publie pas les données brutes ni les identités.

Chaque conclusion indique son niveau de confiance et la preuve qui la soutient.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
user_evaluation_report:
  report_id: AST-UX-REPORT-001
  pilot_id: AST-UX-PILOT-CORE-SHELL-001
  scope:
    sessions: 0
    tasks: planned
    profiles: planned
  evidence:
    observation_ids: []
    restricted_media_refs: []
  findings: []
  decisions: []
  unresolved_questions: []
  privacy_review: pending
  approval: pending
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** le rapport est versionné et relié au pilote.
- **Périmètre :** l’absence de sessions est visible et non dissimulée.
- **Preuves :** les médias restreints sont référencés sans être publiés.
- **Décisions :** les choix et questions ouvertes sont séparés.
- **Approbation :** la revue confidentialité précède toute diffusion.

## 47. Porte d’acceptation UX et accessibilité visuelle

La porte exige des preuves indépendantes : structure d’information, perception, navigation, mouvement, récupération, profils, tests techniques, sessions utilisateurs et confidentialité. Un écran ne passe pas parce qu’il obtient une bonne moyenne globale.

Une réserve bloquante maintient le statut en cours même si les autres domaines sont satisfaits.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
acceptance_gate:
  information_hierarchy: pending
  text_and_contrast: pending
  redundant_color_coding: pending
  focus_and_navigation: pending
  target_size_and_spacing: pending
  reduced_motion_equivalence: pending
  error_recovery: pending
  user_task_evaluation: pending
  privacy_and_consent: pending
  runtime_performance: pending
  decision: blocked
  rule: all_blocking_domains_require_evidence
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Domaines :** chaque axe possède une preuve et une décision séparées.
- **Équivalence :** le profil de mouvement réduit conserve les mêmes tâches et informations.
- **Utilisateurs :** les sessions complètent les contrôles automatisables.
- **Confidentialité :** le consentement et le stockage sont des critères bloquants.
- **Décision :** l’absence de preuve maintient explicitement la porte fermée.

## 48. Matrice de test visuelle et interactionnelle

La matrice croise écrans, profils, ratios, langues, périphériques et situations de jeu. Elle évite de valider chaque dimension isolément tout en bornant le nombre de combinaisons par les risques.

Les profils critiques reçoivent une couverture prioritaire ; les combinaisons restantes utilisent un échantillonnage documenté.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
test_matrix:
  screens: [main_menu, exploration_hud, inventory, pause, confirmation_modal]
  visual_profiles: [reference, high_contrast, large_text, low_motion, redundant_color]
  aspect_profiles: ["16:9", "16:10", "21:9", "4:3"]
  locales: [reference, expanded_pseudo, pseudo_rtl]
  input_profiles: [mouse_keyboard, gamepad]
  contexts: [calm_background, high_detail_background, vfx_overlay]
  selection_strategy: risk_based_pairwise_plus_mandatory_critical_paths
  execution_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Écrans :** les cinq surfaces pilotes restent présentes dans la campagne.
- **Profils :** chaque réglage critique possède au moins un parcours complet.
- **Langues :** expansion et pseudo-RTL révèlent les ruptures de disposition.
- **Contextes :** les fonds défavorables testent contraste et focus.
- **Sélection :** la couverture est bornée par une stratégie documentée, sans prétendre tester toutes les combinaisons.

## 49. Automatisation et limites des captures

L’automatisation peut ouvrir une scène, appliquer un profil, régler une résolution et produire une capture. Elle peut aussi vérifier la présence de focus, l’absence d’erreur et certaines bornes géométriques.

Elle ne décide pas si la hiérarchie est comprise, si une animation est confortable ou si une personne sait récupérer d’une erreur.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
automation_boundary:
  can_check:
    - scene_loads
    - required_controls_exist
    - focus_target_exists
    - critical_rect_inside_safe_area
    - screenshot_generated
    - profile_id_applied
  cannot_approve:
    - comprehension
    - comfort
    - cognitive_load
    - visual_hierarchy
    - user_recovery
  final_decision: human_review_with_user_evidence
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Structure :** les contrôles et cibles peuvent être vérifiés automatiquement.
- **Géométrie :** les rectangles critiques sont comparés aux zones sûres.
- **Capture :** une image est un artefact, pas une décision.
- **Limites :** compréhension, confort et récupération exigent une évaluation humaine.
- **Décision :** l’automatisation prépare la preuve sans approuver l’expérience.

## 50. Budgets et performance des variantes

Les profils d’accessibilité ne doivent pas provoquer des allocations continues, une recompilation de thème à chaque image ou une duplication incontrôlée des textures. Les coûts sont mesurés lors de l’application et pendant l’usage stable.

Un profil visuel peut coûter davantage lorsqu’il ajoute des contours ou panneaux, mais la décision repose sur les mesures des plateformes ciblées.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
runtime_budget_plan:
  events:
    apply_profile:
      measure: [cpu_duration, allocations, frame_spike]
    steady_state:
      measure: [cpu_frame, gpu_frame, memory, draw_calls]
    screen_transition:
      measure: [latency, dropped_frames]
  profiles: [reference, high_contrast, large_text, low_motion]
  target_values: pending
  platform_results: []
  approval: pending
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Application :** le changement de profil est mesuré comme événement distinct.
- **Stable :** le coût continu est séparé du pic de configuration.
- **Transition :** la latence d’entrée et les images perdues sont observées.
- **Cibles :** aucune valeur n’est inventée avant le benchmark.
- **Approbation :** les résultats restent spécifiques à une plateforme et une build.

## 51. Provenance des polices, icônes et outils de mesure

Les profils peuvent nécessiter des polices, icônes, motifs ou outils externes. Chaque dépendance possède une provenance, une licence, une version et une autorisation de redistribution.

Un service web de mesure ne reçoit pas automatiquement des captures contenant des données personnelles ou confidentielles.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
accessibility_dependencies:
  fonts:
    manifest_required: true
    licence_required: true
    redistribution_review: true
  icons_and_patterns:
    source_and_author: required
    modifications: documented
  measurement_tools:
    version: required
    method: documented
    data_upload: reviewed
  participant_media:
    external_upload_without_consent: forbidden
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Polices :** les droits couvrent l’intégration et la redistribution prévues.
- **Icônes :** les transformations et auteurs restent traçables.
- **Outils :** la version et la méthode accompagnent chaque mesure.
- **Données :** un outil distant ne reçoit aucune capture sensible par défaut.
- **Consentement :** les médias participants suivent une autorisation séparée.

## 52. Livrables à conserver

Le chapitre prépare cinq livrables : checklist UX, profils d’accessibilité, variantes de contraste, scénarios de test et rapport utilisateur. Ils restent séparés des scènes UI et des données personnelles.

Chaque livrable possède une identité, une version, un propriétaire et un statut.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
deliverables:
  checklist:
    id: AST-UX-CHECKLIST-001
    status: specified_not_materialized
  profiles:
    root_id: AST-UX-PROFILES-001
    status: specified_not_materialized
  contrast_variants:
    id: AST-UX-CONTRAST-SET-001
    status: specified_not_materialized
  test_scenarios:
    id: AST-UX-SCENARIOS-001
    status: specified_not_materialized
  user_report:
    id: AST-UX-REPORT-001
    status: specified_not_materialized
  personal_data_storage: outside_public_repository
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Checklist :** les contrôles techniques et humains sont versionnés.
- **Profils :** les presets restent distincts des overrides personnels.
- **Contraste :** chaque variante cite ses mesures et contextes.
- **Scénarios :** les tâches et fixtures peuvent être rejouées.
- **Rapport :** la synthèse publique exclut les données personnelles et prises brutes.

## 53. Modes Solo et Studio

Le mode Solo et le mode Studio utilisent les mêmes critères. Ils diffèrent par l’ampleur du recrutement, la spécialisation des rôles et le niveau de formalisation, pas par le droit d’ignorer une barrière connue.

### 53.1 Mode Solo

- limiter le pilote aux cinq écrans prioritaires ;
- tester les tâches critiques avec quelques personnes volontaires et des configurations variées ;
- conserver les observations, corrections et réserves dans un rapport simple ;
- utiliser des profils composables plutôt qu’une multiplication d’écrans spécifiques ;
- effectuer une revue différée pour réduire le biais de l’auteur.

### 53.2 Mode Studio

- identifier une responsabilité accessibilité et une responsabilité recherche utilisateur ;
- recruter un panel adapté aux tâches et aux plateformes ;
- séparer facilitation, prise de notes, analyse et décision lorsque possible ;
- gérer consentements, stockage restreint, rétention et suppression ;
- suivre les problèmes jusqu’au retest et à la décision de fermeture.

## 54. Plan de campagne du pilote

La campagne commence par les contrôles techniques, corrige les blocages évidents, puis organise les sessions avec des personnes. Cette séquence évite de consommer du temps participant sur des défauts détectables automatiquement.

Les retests utilisent la même tâche et une fixture comparable, tout en notant les modifications de build et de profil.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
campaign_plan:
  phase_1_static_review:
    outputs: [checklist, profile_specifications, task_scripts]
  phase_2_technical_checks:
    outputs: [contrast_samples, focus_paths, safe_area_captures]
  phase_3_internal_walkthrough:
    outputs: [obvious_blocker_fixes]
  phase_4_user_sessions:
    outputs: [observations, assisted_statuses, debrief_notes]
  phase_5_analysis:
    outputs: [issues, severity, decisions]
  phase_6_retest:
    outputs: [closure_evidence, remaining_reservations]
  current_phase: phase_1_static_review
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statique :** les contrats et scénarios sont préparés avant l’exécution.
- **Technique :** les défauts mesurables sont corrigés avant le recrutement.
- **Interne :** un walkthrough élimine les blocages évidents sans se substituer aux utilisateurs.
- **Sessions :** les observations restent liées aux tâches et consentements.
- **Retest :** la fermeture exige une nouvelle preuve et conserve les réserves.

## 55. Diagnostics et corrections

<!-- qa:error-correction-section -->


### 55.1 Une alerte critique dépend uniquement du rouge

**Symptôme ou risque :** un joueur ne distingue pas l’état d’échec lorsque l’écran est désaturé ou que la teinte se confond avec le fond.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
status:
  success: green
  warning: yellow
  error: red
  labels: absent
  icons: identical_circle
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la couleur est l’unique canal. Lorsque la teinte n’est pas perçue ou que le contraste varie, les trois états deviennent indiscernables.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
status:
  success: {color: green, icon: check, label: completed}
  warning: {color: amber, icon: triangle, label: attention}
  error: {color: red, icon: octagon_cross, label: failed}
  grayscale_review: required
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les formes et libellés conservent le sens en niveaux de gris, tandis que la couleur renforce la lecture.

### 55.2 Le profil de texte agrandi utilise seulement `scale`

**Symptôme ou risque :** le texte paraît plus grand mais devient flou, chevauche les boutons et sort du panneau.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
large_text:
  root_scale: Vector2(1.5, 1.5)
  minimum_sizes: unchanged
  wrap: unchanged
  reflow: none
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une transformation locale agrandit le rendu sans recalculer les contraintes du layout. Les conteneurs continuent de réserver l’ancienne taille.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
large_text:
  font_tokens: increased_profile
  icon_tokens: increased_profile
  minimum_sizes: recomputed
  wrap: enabled
  reflow: tested
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le profil modifie les tokens qui alimentent les tailles minimales et le reflow, puis la campagne vérifie chaque ratio.

### 55.3 Le focus est indiqué par une lueur trop subtile

**Symptôme ou risque :** la cible clavier ou manette devient invisible sur un fond lumineux ou animé.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
focus_state:
  effect: soft_glow
  contrast_measurement: absent
  shape_change: none
  backgrounds_tested: [dark_panel]
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la lueur dépend du fond, n’a pas de surface ni de contraste mesurés et ne se distingue pas du survol.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
focus_state:
  effect: solid_outline_plus_shape_change
  change_contrast_target: "3:1"
  perimeter_reference: "2_css_px_equivalent"
  backgrounds_tested: [light, dark, image, vfx_overlay]
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la bordure et le changement de forme créent un signal redondant, mesuré sur plusieurs fonds défavorables.

### 55.4 Le profil de mouvement réduit accélère toutes les animations

**Symptôme ou risque :** les transitions deviennent brusques, les informations directionnelles disparaissent et certaines actions sont disponibles à un moment différent.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
reduced_motion:
  all_tween_durations: multiply_by_0_1
  camera_shake: unchanged
  parallax: unchanged
  final_state_timing: changed
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une réduction uniforme ne distingue pas mouvement informatif, transition et décor. Elle peut modifier le contrat de disponibilité.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
reduced_motion:
  large_translation: replace_with_fade_or_instant
  informative_motion: add_static_equivalent
  camera_shake: disable_nonessential
  parallax: disable
  final_state_and_input_timing: preserved
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** chaque famille reçoit une alternative adaptée et le profil conserve l’état final ainsi que le timing fonctionnel.

### 55.5 Le message d’erreur affiche seulement un code

**Symptôme ou risque :** le joueur ne sait pas si son action a été annulée, conservée ou peut être réessayée.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
error_dialog:
  title: ERR_4097
  body: operation_failed
  next_actions: [close]
  preserved_state: unknown
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le code interne ne décrit ni la cause, ni l’état conservé, ni les voies de récupération.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
error_dialog:
  title: save_not_completed
  body: explain_known_or_unknown_cause
  preserved_state: previous_save_is_unchanged
  next_actions: [retry_when_safe, change_slot, cancel]
  technical_details: expandable_with_correlation_id
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le message explique le résultat, protège l’état et propose uniquement des actions réellement sûres.

### 55.6 La confirmation destructive utilise Oui et Non

**Symptôme ou risque :** le joueur valide une suppression en croyant confirmer la conservation de l’élément.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
dialog:
  question: Are_you_sure
  buttons: [Yes, No]
  initial_focus: Yes
  subject_details: absent
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** les libellés ne rappellent pas la conséquence, le sujet est ambigu et le focus initial favorise l’action risquée.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
dialog:
  subject: named_save_slot
  consequence: permanent_local_deletion
  buttons: [remove_save, keep_save]
  initial_focus: keep_save
  escape_action: keep_save
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les verbes nomment les conséquences et le chemin par défaut conserve l’état.

### 55.7 Une notification critique disparaît automatiquement

**Symptôme ou risque :** une erreur de sauvegarde s’efface pendant que le joueur regarde une autre zone et ne peut plus être relue.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
notification:
  type: save_failure
  duration_seconds: 2
  dismissal: automatic
  history: none
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la durée arbitraire suppose que le message sera vu et compris immédiatement, sans voie de récupération.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
notification:
  type: save_failure
  dismissal: explicit_or_resolved
  history: notification_log
  actions: [review_details, retry_when_safe, cancel]
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le signal persiste jusqu’à résolution et le journal permet de le relire.

### 55.8 Le test demande seulement si l’écran plaît

**Symptôme ou risque :** les réponses positives ne révèlent pas que plusieurs personnes échouent à retrouver l’action de comparaison.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
user_test:
  prompt: Do_you_like_this_screen
  task: none
  fixture: uncontrolled
  observations: opinions_only
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la question mesure une préférence générale sans tâche, contexte ni comportement observable.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
user_test:
  task: compare_two_tools_and_move_one_item
  fixture: AST-UX-FIXTURE-CORE-001
  observe: [search_path, errors, recovery, assistance]
  debrief: [expectations, confusing_labels, confidence]
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la tâche produit des observations comparables, puis le débrief explore les attentes sans remplacer les faits.

### 55.9 Une citation de participant est publiée avec son identité

**Symptôme ou risque :** le dépôt public contient un nom, une vidéo et une information sensible qui n’étaient pas nécessaires à la correction.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
report:
  participant_name: full_identity
  quote: raw_unapproved_quote
  recording_url: public
  consent_scope: generic
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le rapport expose des données personnelles, confond les consentements et rend le retrait difficile.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
report:
  participant_id: pseudonym
  quote: approved_or_null
  restricted_media_reference: protected_or_null
  consent_scopes: [observation, recording_optional, quotation_optional]
  public_personal_data: none
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les autorisations sont séparées, les médias restent restreints et le rapport public ne contient aucune identité.

### 55.10 Une observation est présentée comme une vérité universelle

**Symptôme ou risque :** un problème rencontré par une personne est déclaré applicable à tous les joueurs et à toutes les plateformes.

> **[LECTURE] Exemple fautif — Ne pas saisir.**

```yaml
analysis:
  sessions: 1
  finding: all_players_cannot_use_inventory
  platform_scope: universal
  confidence: certain
```
<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la conclusion dépasse l’échantillon, les tâches et la plateforme réellement observés.

> **[LECTURE] Exemple corrigé — Ne pas saisir.**

```yaml
analysis:
  sessions: 1
  observed: participant_did_not_find_comparison_in_task_context
  scope: tested_build_profile_and_fixture
  hypothesis: comparison_action_grouping_is_unclear
  next_step: technical_review_and_additional_sessions
```
<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** le rapport limite le constat à son contexte, sépare l’hypothèse et demande des preuves supplémentaires.

## 56. Checklist de production et validation

La checklist est utilisée avant toute déclaration d’acceptation. Une case non vérifiée reste une réserve ; la présence d’un exemple dans ce chapitre ne la transforme pas en réussite.

- [ ] hiérarchie de l’information et groupes de lecture définis ;
- [ ] contraste du texte, des composants et du focus mesuré sur le rendu final ;
- [ ] tailles, reflow, longueur de ligne et profils d’échelle inspectés ;
- [ ] toute information portée par la couleur possède un canal redondant ;
- [ ] variantes de contraste et perception des couleurs qualifiées ;
- [ ] focus visible, ordre logique, entrée, sortie et restauration testés ;
- [ ] cibles et espacements vérifiés pour les périphériques pris en charge ;
- [ ] inventaire des mouvements et profil réduit validés par tâche ;
- [ ] flashs et pulsations revus avec une méthode qualifiée ;
- [ ] messages d’erreur décrivent cause, état et récupération ;
- [ ] confirmations nomment sujet, portée et conséquence ;
- [ ] annulation, retour, retry et undo respectent leurs contrats ;
- [ ] notifications critiques persistantes et historique disponibles ;
- [ ] profils composables et migrations de réglages testés ;
- [ ] scénarios, fixtures et conditions d’arrêt versionnés ;
- [ ] consentements, stockage, rétention et retrait documentés ;
- [ ] observations séparées des interprétations ;
- [ ] gravité et priorité reliées aux tâches et preuves ;
- [ ] retests effectués avant fermeture des problèmes ;
- [ ] mesures runtime enregistrées par profil et plateforme ;
- [ ] décision humaine et réserves consignées.

## 57. Références techniques officielles

Les pages suivantes fournissent les contrats Godot et les critères W3C utilisés comme références. Les critères WCAG concernent le contenu web ; ils servent ici à formuler des objectifs mesurables et ne certifient pas automatiquement un jeu.

- [Godot 4.7 — Control](https://docs.godotengine.org/en/4.7/classes/class_control.html)
- [Godot 4.7 — ProjectSettings et actions `ui_*`](https://docs.godotengine.org/en/4.7/classes/class_projectsettings.html)
- [Godot 4.7 — Navigation clavier/manette et focus](https://docs.godotengine.org/en/4.7/tutorials/ui/gui_navigation.html)
- [Godot 4.7 — Résolutions multiples](https://docs.godotengine.org/en/4.7/tutorials/rendering/multiple_resolutions.html)
- [Godot 4.7 — Pseudo-localisation](https://docs.godotengine.org/en/4.7/tutorials/i18n/pseudolocalization.html)
- [W3C — WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [W3C — Comprendre l’usage de la couleur, critère 1.4.1](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)
- [W3C — Comprendre le contraste minimal, critère 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- [W3C — Comprendre le contraste non textuel, critère 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)
- [W3C — Comprendre le reflow, critère 1.4.10](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- [W3C — Comprendre le focus visible, critère 2.4.7](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html)
- [W3C — Comprendre l’apparence du focus, critère 2.4.13](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html)
- [W3C — Comprendre la taille minimale des cibles, critère 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- [W3C — Comprendre l’animation déclenchée par les interactions, critère 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)
- [W3C — Comprendre trois flashs ou sous le seuil, critère 2.3.1](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html)
- [W3C — Comprendre l’identification des erreurs, critère 3.3.1](https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html)
- [W3C — Comprendre la suggestion après erreur, critère 3.3.3](https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html)
- [W3C — Impliquer les utilisateurs dans les projets d’accessibilité](https://www.w3.org/WAI/planning/involving-users/fr)
- [W3C — Impliquer les utilisateurs dans l’évaluation de l’accessibilité](https://www.w3.org/WAI/test-evaluate/involving-users/fr)
- [Livre III — Chapitre 24 : Interface utilisateur](CHAPITRE-24-Interface-utilisateur.md)

## 58. Synthèse opérationnelle pour Project Asteria

Project Asteria retient `AST-UX-PILOT-CORE-SHELL-001` comme campagne UX et accessibilité visuelle du noyau d’interface. Les cinq écrans du chapitre 24 sont évalués par tâches, profils composables, mesures de contraste, parcours de focus, variantes de mouvement, contrôles de récupération et sessions consenties. Les profils décrivent des réglages et ne diagnostiquent aucune personne.

La porte d’acceptation exige des preuves distinctes pour hiérarchie, texte, contraste, couleur redondante, focus, cibles, mouvement, erreurs, récupération, confidentialité, tests avec des personnes et coût runtime. Les observations restent séparées des interprétations, les petits échantillons ne sont pas généralisés et aucune donnée personnelle n’entre dans le dépôt public. Tant que les profils, scènes, sessions, mesures et retests ne sont pas matérialisés, le système reste au niveau `static-review`.

> **[LECTURE] Exemple ou structure de référence — Ne pas saisir.**

```yaml
asteria_ux_decisions:
  pilot_id: AST-UX-PILOT-CORE-SHELL-001
  ui_source: AST-UI-PILOT-CORE-SHELL-001
  profile_root: AST-UX-PROFILES-001
  checklist_id: AST-UX-CHECKLIST-001
  scenario_set_id: AST-UX-SCENARIOS-001
  report_id: AST-UX-REPORT-001
  evidence_model: observation_separate_from_interpretation
  privacy_rule: no_personal_data_in_public_repository
  wcag_usage: measurable_reference_not_game_certification
  acceptance: technical_plus_task_plus_user_plus_privacy_plus_runtime
  materialization_status: not_started
```
<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Pilote :** les décisions UX restent reliées aux cinq écrans du système UI existant.
- **Livrables :** profils, checklist, scénarios et rapport possèdent des identifiants séparés.
- **Preuve :** l’observation brute ne se confond jamais avec l’hypothèse d’analyse.
- **Confidentialité :** les données personnelles et enregistrements restent hors du dépôt public.
- **Porte :** l’acceptation combine contrôles techniques, tâches, utilisateurs, confidentialité et mesures runtime.
