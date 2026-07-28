---
title: "Livre IV — Chapitre 18 : Accessibilité"
id: "DOC-L4-CH18"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 18
last-verified: "2026-07-27T13:24:17+02:00"
audit-status: "complete"
audit-date: "2026-07-27T13:24:17+02:00"
audit-report: "Livre-IV/QA/AUDIT-CHAPITRE-18.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
reference-project:
  name: "Project Asteria"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Accessibilité

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes Windows, **[WSL]** terminal Linux ou WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir et **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Rôle du chapitre

Le chapitre 17 possède la publication initiale, les pages boutique et la documentation publique du produit. Le présent
chapitre possède les exigences d’accessibilité du produit complet : commandes, perception visuelle, information sonore,
charge cognitive, motricité, réglages, parcours de test, limites connues et déclaration publique.

L’accessibilité ne consiste pas à ajouter un unique « mode accessible ». Elle réduit des barrières concrètes en donnant
plusieurs moyens de percevoir une information, d’agir, de comprendre une conséquence et de récupérer après une erreur.
Les options doivent être disponibles avant qu’un obstacle ne bloque le joueur.

Le chapitre 25 du Livre III conserve l’accessibilité visuelle des assets et de l’expérience utilisateur. Le chapitre 19
du présent Livre conservera les chaînes, pluriels, écritures, polices et processus de traduction. Le chapitre 18
assemble ces apports au niveau du produit sans les réécrire.

> **[LECTURE] Carte de responsabilité — Ne pas saisir.**

```yaml
accessibility_scope:
  product_owner: chapter-18
  visual_asset_foundations: livre-iii-chapter-25
  localization_pipeline: chapter-19
  initial_publication: chapter-17
  patches_and_rollback: chapter-20
evidence_level: static-review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Portée :** `product_owner` attribue au chapitre 18 les parcours et options du produit complet.
- **Frontières :** Les fondations visuelles, la localisation, la publication et les correctifs restent chez leurs chapitres propriétaires.
- **Niveau de preuve :** `static-review` interdit de présenter les options comme exécutées dans un build réel.
- **Résultat attendu :** Une demande d’accessibilité est routée vers le bon propriétaire au lieu d’être dupliquée.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura :

- distinguer accessibilité, utilisabilité, préférence, assistance et conformité ;
- construire une matrice de barrières fondée sur des tâches observables plutôt que sur des diagnostics supposés ;
- organiser remapping, alternatives aux maintiens, sensibilités, zones mortes et contrôles numériques ;
- préparer sous-titres, captions, mixage, signaux redondants, narration et descriptions audio ;
- encadrer contraste, taille du texte, focus, mouvement, caméra et photosensibilité ;
- composer des profils sans enfermer le joueur dans un préréglage rigide ;
- préparer des parcours représentatifs, des sessions avec utilisateurs et une campagne de non-régression ;
- publier une déclaration d’accessibilité précise, datée et limitée aux fonctions réellement vérifiées ;
- diagnostiquer dix erreurs fréquentes d’accessibilité.

## 3. Niveau de preuve et réserves

Le niveau `static-review` signifie que les contrats, exemples, matrices et scénarios ont été relus statiquement. Il ne
signifie pas qu’une personne a utilisé une manette adaptée, qu’un lecteur d’écran a parcouru l’interface, qu’un test de
photosensibilité a été exécuté ou qu’un build de `Project Asteria` satisfait une norme.

Les références WCAG 2.2 servent ici de réservoir d’objectifs mesurables pour le texte, le contraste, le clavier, le
temps, le focus et les mouvements. Elles ne transforment pas automatiquement un jeu natif en contenu web conforme. Les
Xbox Accessibility Guidelines fournissent des bonnes pratiques de jeu ; elles ne constituent ni certification ni avis
juridique.

Une option documentée reste candidate tant que son interface, sa persistance, son comportement, ses interactions avec
les autres options et ses parcours représentatifs n’ont pas été testés sur le build qualifié.

> **[LECTURE] Registre de preuve — Structure candidate.**

```yaml
accessibility_evidence:
  design_review: prepared
  static_code_review: prepared
  automated_checks: not_run
  representative_journeys: not_run
  user_sessions: not_run
  platform_assistive_technology: not_run
  public_statement: draft_only
claim_policy: verified_features_only
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **États :** `prepared`, `not_run` et `draft_only` distinguent la préparation de l’exécution.
- **Politique de déclaration :** `verified_features_only` empêche d’annoncer une fonction sur la seule base de sa conception.
- **Effet de bord :** Le registre n’active aucune option et ne collecte aucune donnée.
- **Résultat attendu :** La communication publique reste alignée sur les preuves disponibles.

## 4. Prérequis et frontières

Le lecteur doit connaître l’Input Map, les nœuds `Control`, les thèmes, les bus audio, les sauvegardes de réglages et
les campagnes de test. Les chapitres antérieurs restent les références pour leur implémentation détaillée.

La portée inclut les menus, le gameplay, les cinématiques, les tutoriels, les erreurs, les communications système et les
réglages initiaux. Elle exclut le diagnostic médical, la promesse d’absence de risque, la certification automatique et
l’affirmation qu’un même réglage convient à toutes les personnes partageant une déficience.

| Sujet | Propriétaire principal | Consommation par le chapitre 18 |
|---|---|---|
| Actions et périphériques | Livre II, chapitre 6 | Contrats de remapping et alternatives d’activation |
| UI, thèmes et focus | Livre III, chapitres 24 et 25 | Parcours produit, réglages et portes de régression |
| Audio et voix | Livre III, chapitres 26 et 27 | Mixage, captions, description et narration |
| Tests produit | Livre IV, chapitres 2 et 3 | Scénarios, oracles, rapports et non-régression |
| Publication | Livre IV, chapitre 17 | Déclaration publique et preuves visibles avant achat |
| Localisation | Livre IV, chapitre 19 | Chaînes traduisibles, polices, sens d’écriture et relecture |

## 5. Vocabulaire opérationnel

Une **barrière** est une propriété du produit ou de son contexte qui empêche ou renchérit une tâche. Une **fonction
d’accessibilité** est un mécanisme qui supprime ou réduit cette barrière. Une **préférence** peut améliorer le confort
sans répondre à une barrière précise ; elle peut néanmoins devenir essentielle dans une situation donnée.

Une **modalité** désigne une manière de percevoir ou d’agir : vision, audition, toucher, mouvement, texte, parole ou
combinaison. Une information critique ne dépend pas d’une seule modalité lorsqu’une alternative raisonnable peut être
fournie.

Un **profil** est un ensemble réversible de réglages. Il n’est ni diagnostic ni identité de la personne. Une
**déclaration publique** décrit les fonctions et limites observées sur une version définie ; elle ne promet pas une
jouabilité universelle.

> **[LECTURE] Glossaire minimal — Exemple de données.**

```json
{
  "barrier_id": "AST-A11Y-BARRIER-INPUT-001",
  "task": "ouvrir le menu de pause",
  "demand": "pression simultanée de deux boutons",
  "alternative": "action unique remappable",
  "status": "candidate"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `barrier_id` reste stable même si le texte affiché change.
- **Tâche :** `task` décrit ce que le joueur cherche à accomplir, sans supposer une condition médicale.
- **Demande :** `demand` nomme la contrainte observable imposée par le produit.
- **Alternative :** `alternative` indique la transformation à vérifier.
- **Statut :** `candidate` réserve la conclusion jusqu’aux tests.

## 6. Partir des tâches, pas des diagnostics

Deux personnes portant le même diagnostic peuvent rencontrer des barrières différentes, tandis qu’une personne sans
handicap déclaré peut bénéficier des mêmes options dans un environnement bruyant, lumineux, fatigant ou temporairement
contraignant. L’équipe décrit donc la tâche, la demande sensorielle ou motrice, le point de blocage et l’alternative.

Les profils de test combinent des contraintes fonctionnelles sans prétendre représenter toute une population. Par
exemple : absence d’audio, vision à faible contraste, utilisation d’une seule main, impossibilité de maintenir un
bouton, temps de lecture prolongé ou navigation numérique uniquement.

> **[VSC] Fichier candidat `docs/accessibility/task-barriers.yaml`.**

```yaml
schema: asteria-accessibility-task-barriers-v1
barriers:
  - id: AST-A11Y-TASK-PAUSE-001
    journey: first_mission
    task: pause_game
    required_modalities: [vision, motor]
    observed_demand: simultaneous_buttons
    candidate_mitigation: single_remappable_action
    evidence_required: [input_review, journey_test]
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schéma :** La version permet de migrer le registre sans ambiguïté.
- **Tableau `barriers` :** Chaque entrée relie une tâche à une demande observable.
- **Modalités :** `required_modalities` aide à repérer une dépendance exclusive, mais ne remplace pas l’observation.
- **Preuves :** `evidence_required` transforme une idée en porte vérifiable.
- **Résultat attendu :** Le registre fournit un backlog priorisable et traçable.

## 7. Redonder l’information critique

Une alerte indispensable ne doit pas être portée uniquement par la couleur, uniquement par un son ou uniquement par une
vibration. La redondance combine au moins deux canaux compatibles avec le contexte : forme et texte, son et indicateur
directionnel, vibration et icône, dialogue et caption.

Redonder ne signifie pas saturer l’écran. Chaque canal doit préserver la même signification, arriver au bon moment et
pouvoir être réglé. Une flèche qui indique seulement qu’un danger existe n’est pas équivalente à un son qui précise sa
direction et son urgence.

> **[LECTURE] Contrat de signal critique — Exemple.**

```yaml
signal:
  id: AST-SIGNAL-INCOMING-PROJECTILE
  meaning: imminent_directional_threat
  channels:
    - audio_spatial
    - visual_directional_indicator
    - optional_haptic_pulse
  configurable:
    visual_intensity: true
    haptic_intensity: true
  gameplay_authority: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Signification :** `meaning` est la source commune des trois représentations.
- **Canaux :** La liste évite qu’une seule perception soit obligatoire.
- **Configuration :** Les intensités sont réglables sans changer la règle de collision.
- **Autorité :** `gameplay_authority: false` interdit aux signaux accessibles de décider du résultat métier.
- **Résultat attendu :** Une alerte manquée sur un canal reste perceptible sur un autre.

## 8. Construire la matrice d’accessibilité

La matrice croise parcours, tâches, barrières, options, preuves, propriétaires, plateformes et limites. Elle devient la
source de vérité du chapitre : un réglage sans tâche reliée est suspect ; une tâche critique sans alternative ou sans
justification devient un risque.

Les priorités ne sont pas dérivées d’un nombre de personnes supposé. Elles combinent sévérité du blocage, fréquence de
la tâche, absence d’alternative, exposition avant les réglages et coût de correction tardive.

> **[LECTURE] Matrice candidate — Extrait CSV à lire.**

```text
barrier_id;journey;task;severity;option_id;owner;evidence;status
AST-A11Y-001;first_boot;reach_settings;blocker;AST-OPT-NARRATION;ui;journey+screen_reader;candidate
AST-A11Y-002;combat;track_threat;major;AST-OPT-DIRECTIONAL-CUES;audio_vfx;journey+review;candidate
AST-A11Y-003;dialogue;read_caption;major;AST-OPT-CAPTION-STYLE;ui_audio;journey+user_session;candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparateur :** Le point-virgule évite de confondre les virgules présentes dans un texte localisé.
- **Sévérité :** `blocker` signifie qu’un parcours ne peut pas commencer ou continuer.
- **Option :** `option_id` relie la barrière à un réglage stable.
- **Preuve :** La colonne `evidence` exige plusieurs méthodes lorsque le risque le justifie.
- **Résultat attendu :** La matrice permet de détecter les trous de couverture avant publication.

## 9. Concevoir une architecture de réglages composables

Les réglages d’accessibilité appartiennent à un profil utilisateur, pas aux règles métier. Le gameplay consulte des
valeurs validées par des ports dédiés ; il ne lit pas directement des widgets. Un profil peut être prévisualisé,
appliqué, annulé et restauré.

Les options sont composables : activer les captions ne doit pas imposer une palette, et réduire le mouvement ne doit pas
modifier la difficulté du combat sauf choix explicite. Les dépendances rares sont déclarées et expliquées.

> **[VSC] Fichier candidat `src/features/accessibility/domain/accessibility_profile.gd`.**

```gdscript
class_name AccessibilityProfile
extends Resource

@export var profile_id: StringName = &"default"
@export var text_scale: float = 1.0
@export var captions_enabled: bool = true
@export var caption_background_opacity: float = 0.75
@export var reduce_motion: bool = false
@export var hold_actions_as_toggle: bool = false
@export var game_speed_scale: float = 1.0

func validate() -> Error:
    if profile_id.is_empty():
        return ERR_INVALID_DATA
    if text_scale < 0.8 or text_scale > 2.0:
        return ERR_INVALID_PARAMETER
    if caption_background_opacity < 0.0 or caption_background_opacity > 1.0:
        return ERR_INVALID_PARAMETER
    if game_speed_scale < 0.5 or game_speed_scale > 1.0:
        return ERR_INVALID_PARAMETER
    return OK
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe et héritage :** `Resource` rend le profil sérialisable et inspectable sans lui donner d’autorité sur le gameplay.
- **Types :** `StringName`, `float` et `bool` limitent les formes d’entrée.
- **Valeurs par défaut :** Les valeurs fournissent un démarrage utilisable, mais restent candidates tant qu’elles ne sont pas testées.
- **Validation :** `validate()` renvoie un code `Error`; elle ne corrige pas silencieusement une valeur incohérente.
- **Bornes :** Les bornes protègent l’interface et empêchent une vitesse nulle ou une opacité hors intervalle.
- **Résultat attendu :** `OK` autorise la prévisualisation ou l’application atomique du profil.

## 10. Appliquer, annuler et migrer un profil

Une prévisualisation peut rendre une interface illisible ou désorienter le joueur. Le système conserve donc le profil
précédent, applique un candidat, démarre un compte à rebours accessible et restaure automatiquement l’état antérieur si
la confirmation n’arrive pas.

Une migration ne déduit jamais une nouvelle préférence. Elle conserve les réglages connus, ajoute les nouvelles options
avec des valeurs sûres et journalise les champs abandonnés. Une version future inconnue est refusée plutôt
qu’interprétée.

> **[VSC] Fichier candidat `src/features/accessibility/application/accessibility_profile_service.gd`.**

```gdscript
class_name AccessibilityProfileService
extends RefCounted

var _active: AccessibilityProfile
var _preview_previous: AccessibilityProfile

func preview(candidate: AccessibilityProfile) -> Error:
    var validation := candidate.validate()
    if validation != OK:
        return validation
    _preview_previous = _active.duplicate(true)
    _active = candidate.duplicate(true)
    return OK

func confirm_preview() -> void:
    _preview_previous = null

func cancel_preview() -> void:
    if _preview_previous != null:
        _active = _preview_previous
        _preview_previous = null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Copies profondes :** `duplicate(true)` évite qu’un widget modifie le profil actif par référence partagée.
- **Valeur de retour :** `preview()` transmet le code de validation à l’appelant.
- **Prévisualisation :** Le profil précédent existe tant que le joueur n’a pas confirmé.
- **Annulation :** `cancel_preview()` restaure atomiquement l’état antérieur.
- **Limite :** Le compte à rebours, la persistance et l’application aux adaptateurs restent des responsabilités séparées.
- **Résultat attendu :** Un réglage risqué peut être essayé sans enfermer le joueur.

## 11. Rendre les réglages accessibles dès le premier démarrage

Le chemin vers les options d’accessibilité doit être utilisable avant les logos prolongés, le tutoriel et la première
séquence exigeant une perception particulière. Un raccourci visible et annoncé peut ouvrir le panneau depuis le premier
écran.

Le premier démarrage propose un petit nombre d’options à fort impact : narration ou TTS disponible, captions, taille du
texte, contraste du focus, réduction du mouvement, maintien-vers-bascule et vitesse du jeu. Le reste demeure accessible
dans le menu complet.

> **[APP] Godot Editor — Scène candidate du premier démarrage.**

```text
FirstBootAccessibilityPanel
├── Title
├── NarrationToggle
├── CaptionsToggle
├── TextScaleSelector
├── ReduceMotionToggle
├── HoldAsToggleOption
├── OpenFullAccessibilitySettings
└── ContinueButton
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Hiérarchie :** Le panneau place les réglages avant l’action de continuation.
- **Ordre :** Les options à fort impact précèdent le lien vers le menu complet.
- **Focus :** Chaque contrôle doit recevoir un nom, un état, une aide et un ordre cohérent.
- **Limite :** Cette arborescence ne prouve ni narration réelle ni compatibilité avec un lecteur d’écran.
- **Résultat attendu :** Le joueur peut adapter le produit avant le premier obstacle.

## 12. Séparer actions et périphériques

Le code métier dépend d’actions nommées comme `pause_game`, `interact` ou `open_inventory`, jamais d’une touche
physique. L’Input Map de Godot permet d’associer plusieurs événements à une action et de les modifier en code.

Le catalogue d’actions précise celles qui sont indispensables dans les menus, dans le gameplay et pour quitter
proprement. Une action système non remappable doit être rare, justifiée et accompagnée d’une alternative.

> **[VSC] Fichier candidat `src/features/accessibility/infrastructure/input_binding_service.gd`.**

```gdscript
class_name InputBindingService
extends RefCounted

func replace_binding(action: StringName, old_event: InputEvent, new_event: InputEvent) -> Error:
    if not InputMap.has_action(action):
        return ERR_DOES_NOT_EXIST
    if new_event == null:
        return ERR_INVALID_PARAMETER
    if old_event != null and InputMap.action_has_event(action, old_event):
        InputMap.action_erase_event(action, old_event)
    InputMap.action_add_event(action, new_event)
    return OK

func bindings_for(action: StringName) -> Array[InputEvent]:
    if not InputMap.has_action(action):
        return []
    return InputMap.action_get_events(action).duplicate()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** `action` est l’identité stable; les deux `InputEvent` représentent l’ancien et le nouvel événement.
- **Préconditions :** L’action doit exister et le nouvel événement ne peut pas être nul.
- **Mutation :** L’ancien événement n’est effacé que s’il est réellement associé à l’action.
- **Retour :** `OK`, `ERR_DOES_NOT_EXIST` ou `ERR_INVALID_PARAMETER` permettent une erreur d’interface précise.
- **Copie :** `bindings_for()` renvoie un tableau détaché afin que l’appelant ne traite pas la collection comme mutable.
- **Résultat attendu :** Un périphérique peut changer sans modifier les règles métier.

## 13. Détecter les conflits sans bloquer les choix légitimes

Deux actions peuvent partager un événement lorsque leurs contextes sont exclusifs, par exemple navigation de menu et
déplacement. Le système ne doit donc pas refuser tous les doublons ; il affiche les conflits actifs dans un même
contexte et propose remplacer, conserver ou annuler.

Les invites, tutoriels et cartes de commandes consomment le binding actif. Une icône figée dans une texture devient
obsolète après remapping et doit être remplacée par une représentation dynamique ou un texte générique.

> **[LECTURE] Résultat de détection de conflit — Exemple.**

```json
{
  "event": "Key:Space",
  "requested_action": "interact",
  "conflicts": [
    {"action": "jump", "context": "gameplay", "severity": "active"},
    {"action": "confirm", "context": "menu", "severity": "exclusive_context"}
  ],
  "choices": ["replace_active", "keep_all", "cancel"]
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Événement :** La représentation est destinée au diagnostic; la sérialisation réelle doit conserver le type et ses champs.
- **Contexte :** La sévérité distingue un conflit simultané d’un partage acceptable.
- **Choix :** Le joueur garde la décision finale; aucun remplacement silencieux n’est effectué.
- **Résultat attendu :** Le remapping reste flexible sans rendre deux actions gameplay indistinguables.

## 14. Remplacer les maintiens, répétitions rapides et combinaisons

Une action qui exige un maintien prolongé peut offrir une bascule, une durée réduite ou une activation automatique. Une
séquence de frappes rapides peut devenir une pression unique, un rythme configurable ou une réussite automatique. Une
combinaison simultanée peut devenir une action unique remappable.

Ces alternatives doivent couvrir les menus autant que le gameplay. Un curseur qui demande de maintenir un bouton tout en
déplaçant un stick conserve une barrière même si l’action principale est remappable.

> **[LECTURE] Contrat d’activation — Exemple.**

```yaml
action_activation:
  action: aim
  default_mode: hold
  available_modes: [hold, toggle]
  hold_duration_seconds: 0.0
  repeated_press_requirement: none
  simultaneous_inputs_required: false
  prompts_follow_active_mode: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Mode :** `available_modes` sépare la préférence du comportement par défaut.
- **Durée :** Une durée nulle signifie que l’action répond dès l’activation; elle n’impose pas un maintien caché.
- **Répétition :** `none` exclut une cadence implicite.
- **Invites :** Les textes et icônes suivent le mode réellement actif.
- **Résultat attendu :** La même intention peut être exprimée avec une demande motrice moindre.

## 15. Régler zones mortes, sensibilité et inversion

Les axes analogiques varient selon le périphérique, l’usure et la capacité motrice. Le joueur doit pouvoir régler les
zones mortes, la sensibilité et l’inversion par axe lorsque ces paramètres affectent une tâche. Les valeurs sont
prévisualisées sur un indicateur brut et filtré.

Une zone morte trop grande supprime les petits mouvements ; une zone trop faible crée une dérive. La courbe de réponse
ne doit pas être confondue avec la vitesse de caméra, et les réglages de souris ne doivent pas écraser ceux d’une
manette.

> **[VSC] Fichier candidat `src/features/accessibility/domain/analog_axis_profile.gd`.**

```gdscript
class_name AnalogAxisProfile
extends Resource

@export_range(0.0, 0.95, 0.01) var inner_deadzone: float = 0.2
@export_range(0.05, 1.0, 0.01) var outer_deadzone: float = 1.0
@export_range(0.25, 2.0, 0.05) var sensitivity: float = 1.0
@export var invert: bool = false

func transform_axis(raw_value: float) -> float:
    var magnitude := absf(raw_value)
    if magnitude <= inner_deadzone:
        return 0.0
    var normalized := inverse_lerp(inner_deadzone, outer_deadzone, magnitude)
    var signed_value := minf(normalized * sensitivity, 1.0) * signf(raw_value)
    return -signed_value if invert else signed_value
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Annotations :** `@export_range` rend les bornes visibles et empêche des valeurs arbitraires dans l’inspecteur.
- **Entrée :** `raw_value` est l’axe normalisé reçu du périphérique.
- **Zone interne :** Les petites dérives sont ramenées à zéro.
- **Normalisation :** `inverse_lerp()` remappe l’intervalle utile vers une progression de zéro à un.
- **Sensibilité et inversion :** Le résultat est borné puis éventuellement inversé.
- **Limite :** La courbe doit être testée sur les périphériques cibles; ce calcul n’est pas une qualification matérielle.

## 16. Offrir des alternatives numériques aux gestes analogiques

Une fonction contrôlée par un chemin précis — glisser-déposer, rotation libre, visée au stick — peut souvent proposer
une alternative fondée sur les points de départ et d’arrivée : boutons de déplacement, listes, pas discrets,
verrouillage de cible ou commande « déplacer vers ».

L’alternative doit atteindre la même fonction, même si l’expérience diffère. Elle ne doit pas être limitée à un
sous-ensemble qui empêche la progression.

> **[LECTURE] Matrice analogique-numérique — Exemple.**

```markdown
| Fonction | Entrée principale | Alternative numérique | Vérification |
|---|---|---|---|
| Naviguer une carte | stick libre | croix directionnelle par pas | atteindre chaque point d’intérêt |
| Déplacer un objet | glisser-déposer | sélectionner puis choisir la destination | même liste de destinations valides |
| Viser | souris ou stick | verrouillage et cycle de cibles | sélectionner toute cible autorisée |
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Fonction :** La comparaison porte sur le résultat recherché, pas sur le périphérique.
- **Alternative :** Chaque solution utilise des pressions simples et séquentielles.
- **Vérification :** L’oracle compare les destinations ou cibles atteignables.
- **Résultat attendu :** Une tâche essentielle ne dépend plus d’un mouvement continu précis.

## 17. Décomposer la difficulté et le rythme

Un choix global « Facile, Normal, Difficile » mélange souvent précision, temps de réaction, dégâts, ressources, énigmes
et pénalités. Des réglages séparés permettent au joueur de réduire une barrière sans supprimer le défi qu’il souhaite
conserver.

Le ralentissement du jeu, la pause pendant les menus, les fenêtres de timing élargies, l’aide à la visée, la répétition
d’un tutoriel, le passage d’une séquence et la conservation des ressources sont des axes distincts. Leur disponibilité
et leurs conséquences sont expliquées sans jugement.

> **[LECTURE] Profil de rythme candidat — Exemple.**

```yaml
pace_options:
  game_speed_scale: 0.75
  pause_during_radial_menu: true
  qte_mode: single_press
  timing_window_multiplier: 1.5
  puzzle_hints: on_request
  combat_damage_received_multiplier: 1.0
  achievements_affected: false
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Indépendance :** La vitesse, les QTE, les indices et les dégâts sont réglés séparément.
- **Multiplicateurs :** Les nombres sont des candidats de conception et non des valeurs équilibrées par mesure.
- **Transparence :** `achievements_affected` rend visible une conséquence produit; le projet ne doit pas pénaliser sans justification.
- **Résultat attendu :** Le joueur adapte la demande temporelle sans modifier automatiquement tous les autres défis.

## 18. Gérer les limites de temps

Un délai non essentiel peut être supprimé, prolongé ou suspendu. Lorsque le temps appartient à la fiction ou au
multijoueur réel, l’équipe cherche une alternative : file séparée, mode entraînement, confirmation anticipée, option de
lecture après l’événement ou action simplifiée.

Les comptes à rebours affichent leur durée, leur état et leur conséquence. Ils ne commencent pas avant que l’information
nécessaire soit perceptible.

> **[SORTIE] Rapport attendu d’un scénario temporel.**

```text
scenario=AST-A11Y-TIME-003
time_limit_visible=true
pause_option_available=true
caption_reading_time_preserved=true
unexpected_timeout=false
result=pass_candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Scénario :** L’identité permet de relier la sortie au parcours et au build.
- **Observables :** Chaque ligne décrit un comportement vérifiable plutôt qu’une impression globale.
- **Résultat :** `pass_candidate` n’est définitif qu’après conservation des preuves de la campagne.
- **Résultat attendu :** Un échec de lecture ou de motricité ne provient pas d’un délai caché.

## 19. Ne pas dépendre de la couleur seule

Une couleur peut renforcer un état, mais la forme, le texte, l’icône, la position ou le motif portent aussi la
signification. Les palettes candidates sont évaluées sur les écrans réels, y compris avec transparence, post-traitement,
daltonisation de test et conditions d’affichage variées.

Le contraste du texte et des composants utilise des objectifs mesurables. Les ratios WCAG peuvent guider l’évaluation,
mais leur application à un rendu de jeu exige une définition stable des couleurs, des arrière-plans et des états.

> **[LECTURE] Jetons d’état redondants — Exemple.**

```yaml
status_tokens:
  danger:
    color: "#D43C3C"
    icon: "triangle_exclamation"
    label: "Danger"
    pattern: "diagonal_stripes"
  safe:
    color: "#2F8F5B"
    icon: "shield_check"
    label: "Sûr"
    pattern: "solid"
color_only_encoding: forbidden
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Jetons :** Chaque état possède quatre canaux cohérents.
- **Libellé :** Le texte reste traduisible au chapitre 19.
- **Interdiction :** `color_only_encoding` rend la règle contrôlable par revue.
- **Limite :** Les codes hexadécimaux sont illustratifs; leur contraste dépend du contexte réel.
- **Résultat attendu :** La perte ou la confusion d’une couleur ne supprime pas le sens.

## 20. Agrandir le texte sans perdre le contenu

Le facteur de texte ne doit pas simplement étirer un bitmap. Les conteneurs recalculent leurs tailles, les lignes se
replient, les panneaux défilent si nécessaire et les informations ne sont pas coupées. Les textes essentiels évitent les
images de texte.

Le test couvre les écrans étroits, les écrans éloignés, les longues chaînes et les valeurs dynamiques. Le chapitre 19
ajoutera pseudo-localisation, scripts non latins et sens d’écriture ; le présent chapitre prépare les conteneurs et les
seuils de lisibilité.

> **[VSC] Fichier candidat `src/features/accessibility/presentation/text_scale_applier.gd`.**

```gdscript
class_name TextScaleApplier
extends RefCounted

const MIN_SCALE := 0.8
const MAX_SCALE := 2.0

func apply_to_theme(base_theme: Theme, requested_scale: float) -> Theme:
    var scale := clampf(requested_scale, MIN_SCALE, MAX_SCALE)
    var derived := base_theme.duplicate(true) as Theme
    for theme_type in derived.get_font_size_type_list():
        for font_size_name in derived.get_font_size_list(theme_type):
            var base_size := derived.get_font_size(font_size_name, theme_type)
            derived.set_font_size(font_size_name, theme_type, maxi(1, roundi(base_size * scale)))
    return derived
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Constantes :** Les bornes sont nommées pour rester cohérentes avec le profil.
- **Paramètres :** `base_theme` est la source; `requested_scale` vient du profil validé.
- **Copie profonde :** Le thème source n’est pas modifié pendant la prévisualisation.
- **Boucle :** Chaque propriété de taille est recalculée; le nom exact de l’API doit être confirmé contre le thème réel du projet.
- **Retour :** La fonction renvoie un thème dérivé à appliquer par la couche de présentation.
- **Réserve :** Cet extrait est une architecture candidate et nécessite une revue syntaxique contre les méthodes réellement utilisées par le projet.

## 21. Stabiliser le focus et la navigation

Un focus visible, non masqué et ordonné permet la navigation au clavier, à la manette et avec des dispositifs qui
émettent des entrées numériques. À l’ouverture d’un écran, le focus arrive sur un contrôle utile ; à la fermeture d’une
modale, il revient à l’élément déclencheur.

Les changements de focus ne déclenchent pas une action destructive. Les groupes répétés gardent un ordre relatif
cohérent et les contrôles désactivés expliquent leur état.

> **[VSC] Fichier candidat `src/features/accessibility/presentation/focus_restore.gd`.**

```gdscript
class_name FocusRestore
extends RefCounted

var _previous_focus: WeakRef

func remember(control: Control) -> void:
    _previous_focus = weakref(control) if is_instance_valid(control) else null

func restore(fallback: Control) -> void:
    var target: Control = null
    if _previous_focus != null:
        target = _previous_focus.get_ref() as Control
    if not is_instance_valid(target) or not target.is_visible_in_tree():
        target = fallback
    if is_instance_valid(target):
        target.call_deferred("grab_focus")
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Référence faible :** `WeakRef` n’empêche pas la libération de l’ancien contrôle.
- **Fallback :** Un contrôle de repli évite de laisser l’utilisateur sans point de navigation.
- **Visibilité :** Le focus n’est pas restauré sur un élément masqué.
- **Appel différé :** La demande intervient après la mise à jour de l’arbre de scène.
- **Résultat attendu :** La fermeture d’une modale ramène le joueur dans un contexte prévisible.

## 22. Dimensionner les cibles et éviter les gestes fragiles

Les cibles interactives doivent être assez grandes et assez espacées pour les écrans tactiles, les souris imprécises, le
regard ou les dispositifs alternatifs. Une petite icône peut conserver son apparence tout en disposant d’une zone
interactive plus grande.

Le glissement possède une alternative par sélection et activation. Une action déclenchée au relâchement permet
l’annulation lorsque le pointeur quitte la cible avant la fin du geste.

> **[LECTURE] Contrat de cible interactive — Exemple.**

```yaml
interactive_target:
  visual_size_px: [24, 24]
  hit_area_px: [48, 48]
  spacing_px: 8
  activation: release_inside
  drag_alternative: select_then_move
  keyboard_reachable: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Taille visuelle :** L’icône peut rester compacte.
- **Zone active :** `hit_area_px` agrandit la surface sans modifier le dessin.
- **Activation :** `release_inside` donne une possibilité d’annulation.
- **Alternative :** Le déplacement n’exige pas un trajet continu.
- **Réserve :** Les dimensions sont candidates et doivent être évaluées par plateforme et distance d’usage.

## 23. Réduire mouvement, caméra et distractions

Le profil de mouvement réduit peut désactiver le head bob, limiter le tremblement, supprimer le flou cinétique, réduire
les zooms brusques, stabiliser les arrière-plans et remplacer certaines transitions. Le champ de vision et la
sensibilité restent réglables séparément.

Un réglage réduit ne doit pas supprimer une information gameplay. Lorsqu’un effet visuel transmet un danger, une version
statique, textuelle ou sonore conserve la signification.

> **[LECTURE] Profil de mouvement candidat.**

```yaml
motion_profile:
  camera_shake_intensity: 0.0
  head_bob_enabled: false
  motion_blur_enabled: false
  rapid_zoom_enabled: false
  animated_backgrounds: reduced
  transition_duration_scale: 0.5
  field_of_view: 85
  preserves_gameplay_cues: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Indépendance :** Chaque cause de mouvement possède son réglage.
- **Échelle :** Une transition raccourcie n’est pas forcément supprimée; le comportement doit être prévisualisé.
- **Champ de vision :** La valeur est illustrative et dépend de la caméra et de la plateforme.
- **Invariant :** `preserves_gameplay_cues` impose une alternative lorsque l’effet transmet une information.
- **Résultat attendu :** Le confort visuel s’améliore sans perte de règle.

## 24. Traiter la photosensitivité comme une porte de sécurité

L’élimination ou la réduction des flashs dangereux est préférable à un simple avertissement. La revue couvre le
gameplay, les menus, les transitions, les vidéos, les VFX procéduraux et les combinaisons imprévues d’effets.

Un outil automatique peut signaler des séquences, mais il ne remplace ni la configuration correcte de la capture ni
l’interprétation spécialisée. Toute modification d’un effet lumineux critique rouvre la porte de revue.

> **[LECTURE] Registre de revue photosensibilité — Exemple.**

```yaml
photosensitivity_review:
  build_id: AST-BUILD-CANDIDATE
  capture_profile: full_screen_reference
  gameplay_routes: [combat, storm, low_health, menu_transitions]
  automated_analysis: not_run
  specialist_review: not_run
  known_flashing_content: unknown
  release_gate: blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Build :** La revue est reliée à une version précise.
- **Parcours :** Les situations à effets intenses sont nommées au lieu d’être supposées couvertes.
- **États :** `not_run` et `unknown` empêchent une conclusion prématurée.
- **Porte :** `blocked` reste la décision conservatrice tant que les preuves manquent.
- **Résultat attendu :** Un avertissement ne masque pas l’absence de contrôle.

## 25. Distinguer sous-titres et captions

Les sous-titres transcrivent la parole. Les captions couvrent aussi les sons non verbaux utiles : source, direction,
identité du locuteur, musique, interruption ou tonalité pertinente. Une caption n’invente pas une information absente du
son original.

Chaque entrée possède un identifiant stable, un intervalle, un locuteur éventuel, un texte localisable et des indices
sonores structurés. Les timings et textes traduits appartiendront au pipeline linguistique du chapitre 19.

> **[VSC] Fichier candidat `data/accessibility/caption_track.example.json`.**

```json
{
  "schema": "asteria-caption-track-v1",
  "track_id": "AST-CAPTION-RELAY-INTRO-FR",
  "language": "fr-FR",
  "entries": [
    {
      "id": "cap-001",
      "start_ms": 1240,
      "end_ms": 4380,
      "speaker_id": "scout",
      "text_key": "caption.relay_intro.scout_001",
      "sound_cues": ["radio_static"],
      "direction": "front_left"
    }
  ]
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schéma :** La version permet l’évolution du format.
- **Intervalle :** `start_ms` et `end_ms` sont des temps de média, pas l’horloge du gameplay.
- **Texte :** `text_key` prépare la localisation sans mettre la phrase française dans le format canonique.
- **Indices :** `sound_cues` et `direction` complètent le dialogue lorsque le son porte une information.
- **Résultat attendu :** Une piste peut être validée, traduite et rendue indépendamment.

## 26. Personnaliser l’affichage des captions

Le joueur peut régler taille, police compatible, arrière-plan, opacité, couleur du locuteur, nombre de lignes et
position sûre. Un aperçu utilise de vraies longueurs de phrase et plusieurs locuteurs.

Le texte ne doit pas masquer des objectifs, invites ou informations critiques. Un gestionnaire de zones arbitre les
collisions entre captions, HUD et notifications au lieu de superposer aveuglément les éléments.

> **[LECTURE] Style de captions candidat.**

```yaml
caption_style:
  text_scale: 1.25
  background_enabled: true
  background_opacity: 0.85
  speaker_labels: names
  sound_cues_enabled: true
  max_lines: 3
  safe_area: lower_center
  avoid_hud_regions: true
  preview_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Échelle :** La taille se compose avec l’échelle globale de texte selon une règle explicite.
- **Arrière-plan :** L’opacité améliore la séparation sans supposer un contraste suffisant dans tous les plans.
- **Locuteurs :** Les noms complètent la couleur et restent utilisables sans perception chromatique.
- **Zones :** `avoid_hud_regions` exige une coordination avec le layout réel.
- **Prévisualisation :** Le joueur voit le résultat avant confirmation.

## 27. Séparer les catégories audio

Les volumes de dialogue, effets, musique, interface, ambiance, narration et chat sont réglés séparément lorsque ces
catégories existent. Un mode de dynamique réduite rapproche les niveaux faibles et forts sans promettre une correction
universelle.

Le mix mono, l’atténuation de la musique pendant les dialogues et les signaux visuels complètent les réglages. Le mode
mono est vérifié pour éviter l’annulation de phase et la disparition d’un signal uniquement présent dans un canal.

> **[LECTURE] Profil audio accessible — Exemple.**

```yaml
audio_accessibility:
  master_db: 0.0
  dialogue_db: 2.0
  effects_db: -3.0
  music_db: -8.0
  ui_db: 0.0
  narration_db: 1.0
  dynamic_range: reduced
  mono_output: false
  dialogue_ducking: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Décibels :** Les valeurs sont des gains candidats; elles ne représentent pas des mesures de loudness.
- **Catégories :** Le joueur peut rendre la parole intelligible sans couper tous les effets.
- **Dynamique :** `reduced` désigne un profil à qualifier, pas un algorithme défini par ce seul mot.
- **Mono :** Le choix reste explicite et doit être testé sur le mix final.
- **Résultat attendu :** Les informations sonores essentielles deviennent ajustables.

## 28. Représenter les sons utiles visuellement

Un indicateur sonore directionnel décrit la catégorie, la direction et éventuellement la distance sans transformer tous
les sons en bruit visuel. Le joueur choisit les catégories : menace, interaction, allié, objectif ou environnement.

Le système ne révèle pas une information que l’audio normal ne transmet pas et ne devient pas une autorité de détection.
Il consomme les mêmes événements de présentation que le mixage.

> **[VSC] Fichier candidat `src/features/accessibility/presentation/audio_cue_presenter.gd`.**

```gdscript
class_name AudioCuePresenter
extends Node

signal cue_requested(category: StringName, direction: Vector2, intensity: float)

func present(category: StringName, world_direction: Vector3, strength: float) -> void:
    if category.is_empty():
        return
    var planar := Vector2(world_direction.x, world_direction.z)
    var direction := planar.normalized() if planar.length_squared() > 0.0 else Vector2.ZERO
    cue_requested.emit(category, direction, clampf(strength, 0.0, 1.0))
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Signal :** `cue_requested` transmet des données de présentation sans créer l’icône lui-même.
- **Paramètres :** La catégorie, la direction monde et la force viennent d’un événement déjà autorisé.
- **Projection :** Le vecteur 3D devient une direction plane pour l’interface.
- **Bornage :** L’intensité est limitée entre zéro et un.
- **Autorité :** La fonction ne cherche pas les ennemis et ne décide pas qu’un son existe.
- **Résultat attendu :** L’UI peut produire une représentation directionnelle cohérente avec l’audio.

## 29. Préparer description audio et narration

La description audio ajoute les informations visuelles essentielles d’une cinématique lorsque le dialogue et les sons ne
suffisent pas. Elle possède une piste, une langue, un mix et des points de synchronisation distincts.

La narration d’interface lit noms, rôles, valeurs, états et changements importants. Elle ne se limite pas au texte
visible : un curseur doit annoncer son libellé, sa valeur et son unité ; une option désactivée doit annoncer la raison
si elle est utile.

> **[LECTURE] Contrat de narration d’un contrôle.**

```json
{
  "control_id": "text_scale_slider",
  "accessible_name_key": "settings.accessibility.text_scale",
  "role": "slider",
  "value": 125,
  "unit_key": "unit.percent",
  "minimum": 80,
  "maximum": 200,
  "step": 5,
  "help_key": "settings.accessibility.text_scale.help"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Nom :** La clé localisable décrit la fonction plutôt que l’apparence.
- **Rôle :** `slider` permet à la couche de narration d’annoncer le comportement attendu.
- **Valeur et bornes :** Le joueur connaît l’état actuel et l’espace de réglage.
- **Aide :** Une description séparée évite de surcharger le nom.
- **Résultat attendu :** Le contrôle est compréhensible sans dépendre de sa position visuelle.

## 30. Encadrer TTS et lecteur d’écran dans Godot

Godot 4.7 expose du text-to-speech via `DisplayServer` et des API d’accessibilité de bas niveau. Le TTS dépend des voix
et bibliothèques du système ; sa disponibilité, sa langue, sa latence et son interruption varient selon la plateforme.

La documentation Godot précise que le TTS intégré n’offre pas à lui seul l’intégration riche d’un lecteur d’écran. Le
projet doit donc détecter les capacités réelles, permettre le choix de la voix et du débit, persister ces choix et
publier les limites par plateforme.

> **[VSC] Fichier candidat `src/features/accessibility/infrastructure/tts_adapter.gd`.**

```gdscript
class_name TtsAdapter
extends RefCounted

func voices_for(language: String) -> PackedStringArray:
    return DisplayServer.tts_get_voices_for_language(language)

func speak(text: String, voice_id: String, volume: int = 50, pitch: float = 1.0, rate: float = 1.0) -> Error:
    if text.is_empty() or voice_id.is_empty():
        return ERR_INVALID_PARAMETER
    DisplayServer.tts_speak(text, voice_id, volume, pitch, rate)
    return OK

func stop() -> void:
    DisplayServer.tts_stop()
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Capacités :** `voices_for()` interroge les voix du système pour une langue au lieu d’inventer un identifiant.
- **Collection :** Les identifiants sont copiés dans un `PackedStringArray` simple pour la couche de réglages.
- **Paramètres :** Le volume, la hauteur et le débit possèdent des valeurs par défaut explicites.
- **Retour :** `speak()` refuse texte ou voix vides et renvoie `OK` après l’envoi asynchrone.
- **Arrêt :** `stop()` demande l’interruption, dont la latence dépend du système.
- **Réserve :** Les signatures exactes et plages doivent être revérifiées lors de la matérialisation sur Godot 4.7.1.

## 31. Réduire la charge cognitive

Une tâche est plus accessible lorsque l’objectif, l’état, les choix et les conséquences sont visibles. Les écrans
utilisent des libellés cohérents, une hiérarchie stable, des étapes courtes, la divulgation progressive et des aides
disponibles à la demande.

Les tutoriels peuvent être répétés, ralentis ou consultés hors pression. Les objectifs conservent un historique et les
marqueurs expliquent pourquoi ils sont actifs. Les textes évitent les formulations ambiguës, sans appauvrir les
informations nécessaires.

> **[LECTURE] Contrat d’objectif compréhensible.**

```yaml
objective:
  id: AST-OBJ-RELAY-RESTORE
  title_key: objective.relay_restore.title
  summary_key: objective.relay_restore.summary
  current_step_key: objective.relay_restore.step.connect_power
  reason_key: objective.relay_restore.reason
  optional_hint_keys:
    - objective.relay_restore.hint.route
    - objective.relay_restore.hint.panel
  history_available: true
  time_pressure: none
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** L’objectif reste stable pendant les changements de texte.
- **Clés :** Titre, résumé, étape et raison sont séparés pour éviter un bloc opaque.
- **Indices :** Les aides sont optionnelles et demandées par le joueur.
- **Historique :** Le contexte peut être retrouvé après une interruption.
- **Temps :** `none` exclut une pression non nécessaire pendant la lecture.

## 32. Prévenir et réparer les erreurs

Une erreur est identifiée en langage clair, reliée au contrôle concerné et accompagnée d’une action de correction. Les
opérations destructives offrent confirmation, annulation ou undo proportionné au risque.

Le focus est envoyé vers le message ou le premier champ invalide sans enfermer la navigation. Une notification
temporaire importante possède un historique ou reste affichée jusqu’à acquittement.

> **[LECTURE] Résultat d’une validation de réglage.**

```json
{
  "status": "rejected",
  "field": "caption_background_opacity",
  "code": "value_out_of_range",
  "message_key": "settings.error.opacity_range",
  "minimum": 0.0,
  "maximum": 1.0,
  "recovery_action": "return_to_field"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** `rejected` décrit un refus contrôlé, pas une exception.
- **Champ et code :** L’interface peut cibler le contrôle et choisir le message localisé.
- **Bornes :** La correction proposée contient les valeurs acceptées.
- **Récupération :** Le focus revient au champ sans perdre les autres modifications.
- **Résultat attendu :** Le joueur comprend ce qui a échoué et comment continuer.

## 33. Préparer les aides motrices

Les aides motrices peuvent inclure visée assistée, verrouillage, conduite assistée, collecte automatique,
maintien-vers-bascule, sensibilité réduite, zone morte réglable, actions séquentielles, pause tactique et vitesse
réduite.

Chaque aide déclare ce qu’elle change, ce qu’elle ne change pas et si elle affecte le multijoueur compétitif. Une aide
locale ne doit pas être désactivée arbitrairement dans les menus ou les séquences secondaires.

> **[LECTURE] Fiche d’aide motrice — Exemple.**

```yaml
assist_feature:
  id: AST-A11Y-AIM-LOCK
  task: select_combat_target
  changes:
    - target_acquisition
    - target_retention
  does_not_change:
    - damage
    - enemy_health
  available_modes: [off, soft, strong]
  competitive_multiplayer_policy: requires_separate_review
  player_visible_description: required
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Tâche :** La fonction est reliée au besoin plutôt qu’à une catégorie de joueur.
- **Changements :** La portée évite qu’une aide modifie silencieusement les dégâts.
- **Modes :** L’intensité reste choisie par le joueur.
- **Multijoueur :** Une revue séparée traite équité, sécurité et architecture réseau.
- **Description :** Le comportement doit être compris avant activation.

## 34. Utiliser l’haptique comme canal optionnel

La vibration peut renforcer une confirmation, une direction ou un rythme, mais elle ne doit pas être le seul canal.
Intensité, catégories et désactivation globale sont réglables.

Les motifs trop longs, douloureux ou constants sont évités. Un périphérique sans haptique reçoit la même information par
les autres canaux.

> **[LECTURE] Motif haptique candidat.**

```yaml
haptic_pattern:
  id: AST-HAPTIC-CONFIRM
  purpose: confirm_success
  pulses:
    - duration_ms: 80
      weak: 0.35
      strong: 0.0
  required_for_gameplay: false
  visual_alternative: confirmation_icon
  audio_alternative: ui_confirm
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **But :** `purpose` empêche la réutilisation ambiguë du motif.
- **Impulsion :** La durée et les intensités sont candidates et doivent être testées sur matériel.
- **Optionnalité :** `required_for_gameplay: false` interdit une dépendance exclusive.
- **Alternatives :** L’icône et le son portent la même confirmation.
- **Résultat attendu :** La vibration améliore le retour sans devenir une barrière.

## 35. Préserver sauvegarde, checkpoints et reprise

Des checkpoints prévisibles, la sauvegarde manuelle lorsque compatible, la reprise après interruption et le retry rapide
réduisent la répétition imposée. L’accessibilité ne doit pas rendre les sauvegardes incompatibles ou effacer les choix
de difficulté.

Le profil d’accessibilité est chargé avant le premier écran interactif. En cas de profil corrompu, un profil sûr est
proposé sans supprimer le fichier source avant diagnostic.

> **[LECTURE] Section de sauvegarde candidate.**

```json
{
  "section": "accessibility_profile",
  "schema_version": 1,
  "profile_id": "custom-01",
  "settings_digest": "sha256:placeholder",
  "settings": {
    "captions_enabled": true,
    "text_scale": 1.25,
    "reduce_motion": true,
    "hold_actions_as_toggle": true
  }
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Section :** Le profil est séparé de l’état gameplay.
- **Version :** La migration peut être contrôlée.
- **Empreinte :** Le placeholder indique le champ attendu; aucune empreinte réelle n’est revendiquée.
- **Réglages :** Seules les préférences durables sont persistées.
- **Résultat attendu :** Les options restent disponibles après relance et peuvent être restaurées indépendamment.

## 36. Composer des profils sans enfermer le joueur

Des préréglages comme « texte renforcé », « mouvement réduit » ou « contrôles simplifiés » accélèrent le premier
réglage, mais chaque option reste modifiable. Le nom décrit l’effet, pas une déficience.

Une modification après application transforme le préréglage en profil personnalisé au lieu de revenir silencieusement à
une configuration figée. La comparaison montre les différences avant confirmation.

> **[LECTURE] Composition de profil — Exemple.**

```yaml
profile:
  id: custom-01
  based_on: reduced_motion
  overrides:
    captions_enabled: true
    text_scale: 1.35
    camera_shake_intensity: 0.1
  locked_fields: []
  reversible: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Base :** `based_on` garde la provenance du préréglage.
- **Surcharges :** Seules les différences sont listées.
- **Verrouillage :** Une liste vide signifie que le joueur peut encore tout adapter.
- **Réversibilité :** Le profil peut être annulé ou remplacé.
- **Résultat attendu :** Le préréglage sert de point de départ et non de diagnostic.

## 37. Définir des parcours représentatifs

Un parcours représentatif traverse les points où une barrière peut apparaître : premier démarrage, réglages, création ou
chargement de partie, tutoriel, exploration, combat, dialogue, inventaire, pause, cinématique, sauvegarde, erreur et
sortie.

Chaque scénario déclare le profil fonctionnel, les périphériques, les options actives, le build, les étapes, les
observables et les preuves. Un test isolé du menu n’établit pas la jouabilité du produit.

> **[VSC] Fichier candidat `tests/accessibility/journeys/first_mission.yaml`.**

```yaml
schema: asteria-accessibility-journey-v1
id: AST-A11Y-JOURNEY-FIRST-MISSION
build_id: candidate
functional_profile:
  audio_available: false
  input_mode: digital_single_press
  reading_pace: extended
settings:
  captions_enabled: true
  hold_actions_as_toggle: true
steps:
  - open_accessibility_from_first_boot
  - start_new_game
  - complete_tutorial
  - identify_directional_threat
  - pause_and_resume
oracles:
  - no_audio_only_blocker
  - no_simultaneous_input_required
  - critical_text_waits_for_player
evidence: not_run
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Profil fonctionnel :** Les contraintes sont observables et ne prétendent pas diagnostiquer une personne.
- **Réglages :** Le scénario précise l’état du produit.
- **Étapes :** Le parcours traverse plusieurs systèmes.
- **Oracles :** Les critères sont formulés comme absence de barrière critique.
- **Preuve :** `not_run` conserve la réserve tant que le build n’est pas exécuté.

## 38. Tester avec des utilisateurs de manière responsable

Les sessions avec utilisateurs complètent les revues et outils. Le recrutement décrit les tâches et technologies
utilisées, sans demander plus de données personnelles que nécessaire. Consentement, retrait, confidentialité,
accessibilité de la session, pauses et compensation sont préparés avant l’invitation.

Un participant n’est pas chargé de certifier le produit ni de représenter toutes les personnes. Les constats sont reliés
à un parcours, une version, une observation et une gravité ; les préférences individuelles ne sont pas transformées
automatiquement en règle universelle.

> **[LECTURE] Plan de session candidat.**

```yaml
user_session:
  id: AST-A11Y-SESSION-PLAN-001
  purpose: evaluate_first_boot_and_caption_controls
  consent_materials: prepared
  data_minimization: required
  recording: opt_in_only
  pause_any_time: true
  withdrawal_process: documented
  compensation_terms: communicated_before_session
  participant_count: not_scheduled
  build_id: not_selected
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Finalité :** La session vise des tâches précises.
- **Consentement :** Les matériaux sont préparés avant la collecte.
- **Enregistrement :** `opt_in_only` exclut l’enregistrement implicite.
- **Retrait :** Le processus existe avant le recrutement.
- **Réserves :** Aucun participant ni build n’est inventé.
- **Résultat attendu :** Les preuves humaines sont recueillies sans transférer le risque au participant.

## 39. Combiner automatisation, revue experte et observation

Les contrôles automatiques peuvent détecter champs absents, conflits de bindings, textes débordés, contrastes
calculables, focus orphelins ou captions sans intervalle. Ils ne peuvent pas décider seuls qu’un parcours est
compréhensible, qu’une narration est agréable ou qu’un effet ne provoque aucune gêne.

La porte combine donc lint, tests de composant, captures, parcours manuels, revue spécialisée et sessions utilisateurs.
Un résultat vert d’un seul outil ne ferme pas la matrice.

> **[PS] PowerShell 7 — Préparer un rapport statique sans exécuter le jeu.**

```powershell
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path '.').Path
$matrix = Join-Path $root 'docs/accessibility/task-barriers.yaml'
$journeys = Join-Path $root 'tests/accessibility/journeys'
$report = Join-Path $root 'dist/accessibility-static-inventory.txt'

@(
    "matrix_exists=$([IO.File]::Exists($matrix))"
    "journeys_exist=$([IO.Directory]::Exists($journeys))"
    "runtime_executed=false"
) | Set-Content -LiteralPath $report -Encoding utf8

Get-Content -LiteralPath $report
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Politique d’échec :** `Stop` transforme une erreur PowerShell en arrêt contrôlé.
- **Chemins :** `Join-Path` construit des chemins sous la racine résolue.
- **Inventaire :** Le script vérifie seulement la présence des sources préparées.
- **Écriture :** `Set-Content` crée un rapport textuel UTF-8.
- **Sortie :** `runtime_executed=false` empêche de confondre inventaire et campagne.
- **Résultat attendu :** Le rapport décrit les préconditions documentaires, pas la qualité du build.

> **[WSL] Terminal Linux ou WSL — Inventorier les sources préparées.**

```bash
set -eu
test -f docs/accessibility/task-barriers.yaml
test -d tests/accessibility/journeys
printf 'accessibility_sources_present=true\n'
printf 'runtime_executed=false\n'
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Politique d’échec :** `set -eu` arrête le script sur une commande en échec ou une variable absente.
- **Préconditions :** `test -f` et `test -d` contrôlent uniquement les sources documentaires attendues.
- **Sortie :** Les deux lignes distinguent l’inventaire réussi d’une exécution du produit.
- **Résultat attendu :** Une campagne Linux ou WSL ne commence pas avec un registre ou des parcours absents.

> **[DCK] Docker Desktop — Inspecter le conteneur de validation préparé.**

```text
Conteneur : asteria-doc-validation
Montage attendu : dépôt en lecture seule
Sortie autorisée : dist/accessibility/
Accès réseau : désactivé pour la validation locale
Jeu exécuté : non
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Conteneur :** Le nom identifie l’environnement documentaire dans Docker Desktop.
- **Montage :** La lecture seule protège les sources pendant l’inventaire.
- **Sortie :** Le rapport est confiné dans le répertoire prévu.
- **Réseau :** La validation locale ne télécharge ni modèle ni donnée.
- **Limite :** L’inspection du conteneur ne lance pas `Project Asteria`.

## 40. Protéger la non-régression

Chaque changement de contrôles, UI, caméra, audio, cinématique ou tutoriel sélectionne les scénarios d’accessibilité
touchés. La campagne de publication inclut un échantillon complet et des tests ciblés par diff.

Les réglages sont testés seuls puis en combinaison, car deux options valides peuvent interagir : texte agrandi et
captions, mouvement réduit et indicateurs de danger, TTS et ducking, maintien-vers-bascule et pause.

> **[CMD] Invite de commandes Windows — Vérifier l’inventaire préparé.**

```bat
@echo off
setlocal
set "MATRIX=docs\accessibility\task-barriers.yaml"
set "STATEMENT=docs\accessibility\public-statement.md"
if not exist "%MATRIX%" exit /b 2
if not exist "%STATEMENT%" exit /b 3
echo accessibility_sources_present=true
echo runtime_executed=false
exit /b 0
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Variables :** Les chemins sont nommés une seule fois.
- **Codes de retour :** `2` et `3` distinguent les sources absentes.
- **Sortie :** Le script confirme seulement l’inventaire.
- **Portée :** Aucun lancement du jeu, périphérique ou technologie d’assistance n’est exécuté.
- **Résultat attendu :** La CI peut bloquer un lot qui oublie une source obligatoire.

## 41. Tenir un registre des limites connues

Une limite connue décrit le parcours, la plateforme, l’impact, le contournement éventuel, le propriétaire, la version
observée et l’état de correction. Elle n’est ni cachée dans un ticket interne ni formulée comme une promesse vague.

Une fonction partielle est décrite précisément : par exemple « narration des menus principaux sous Windows » plutôt que
« compatible lecteur d’écran ». Les différences de plateformes et de périphériques restent visibles.

> **[LECTURE] Limite connue — Exemple.**

```yaml
known_limitation:
  id: AST-A11Y-LIMIT-TTS-WEB-001
  build_id: candidate
  platform: web
  journey: first_boot
  impact: system_voice_may_require_network_and_start_late
  workaround: captions_and_keyboard_navigation
  owner: accessibility_platform
  status: unverified
  public_disclosure_required: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Plateforme :** La limite n’est pas généralisée aux autres cibles.
- **Impact :** Le comportement observable est décrit sans promettre sa fréquence.
- **Contournement :** Une alternative disponible est indiquée honnêtement.
- **Statut :** `unverified` conserve l’incertitude.
- **Publication :** La déclaration publique doit reprendre la limite si elle subsiste.

## 42. Préparer la déclaration publique d’accessibilité

La déclaration permet au joueur d’évaluer le produit avant achat. Elle porte une version, une date, les plateformes
vérifiées, les fonctions disponibles, leur emplacement, les limites connues, les technologies d’assistance testées et un
canal de support accessible.

Elle évite les termes absolus comme « entièrement accessible ». Une fonction non vérifiée n’est pas listée comme
présente. Une mise à jour qui modifie une fonction rouvre sa preuve et la déclaration.

> **[VSC] Fichier candidat `docs/accessibility/public-statement.md`.**

```markdown
# Accessibilité de Project Asteria

Version du produit : à renseigner après qualification
Date de vérification : à renseigner après campagne
Plateformes vérifiées : aucune à ce stade

## Fonctions vérifiées

Aucune fonction n’est encore déclarée comme vérifiée.

## Fonctions préparées

- remapping des actions ;
- captions configurables ;
- réduction du mouvement ;
- réglages séparés du mixage audio ;
- alternatives aux maintiens et pressions répétées.

## Limites connues

Voir le registre de limites relié au build candidat.

## Assistance

Le canal accessible et ses délais seront publiés avec la version qualifiée.
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Version et date :** La déclaration est liée à un produit concret.
- **Plateformes :** L’absence de qualification reste explicite.
- **Fonctions vérifiées :** La liste vide évite toute revendication anticipée.
- **Fonctions préparées :** La conception est distinguée de l’exécution.
- **Support :** Le canal n’est pas inventé avant la publication.
- **Résultat attendu :** La page peut évoluer vers une déclaration factuelle après campagne.

## 43. Relier la déclaration à la publication

Le chapitre 17 publie la déclaration avec la fiche produit ; le chapitre 18 fournit les faits et limites. Le même
identifiant de build relie rapport, matrice, captures, résultats de parcours et texte public.

Une modification de dernière minute après validation invalide la corrélation. La publication utilise les mêmes octets
qualifiés et conserve le reçu de la déclaration affichée.

> **[WSL] Terminal Linux ou WSL — Vérifier la corrélation des identifiants.**

```bash
set -eu
BUILD_ID="${BUILD_ID:-candidate}"
MATRIX_BUILD_ID="${MATRIX_BUILD_ID:-candidate}"
STATEMENT_BUILD_ID="${STATEMENT_BUILD_ID:-candidate}"

test "$BUILD_ID" = "$MATRIX_BUILD_ID"
test "$BUILD_ID" = "$STATEMENT_BUILD_ID"
printf 'build_correlation=consistent
'
printf 'runtime_executed=false
'
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Variables :** Les trois sources reçoivent un identifiant candidat explicite.
- **Comparaisons :** `test` refuse une déclaration et une matrice portant sur des builds différents.
- **Sortie :** La cohérence documentaire ne prétend pas exécuter le produit.
- **Conteneur :** Le repère `[DCT]` réserve cette commande à un terminal de conteneur configuré.
- **Résultat attendu :** Une déclaration ne peut pas être promue avec des preuves d’une autre version.

## 44. Organiser le support et les retours

Le canal de support accepte le clavier, le copier-coller et un format textuel simple. Le formulaire ne rend pas
obligatoires des données médicales. Il demande version, plateforme, parcours, option, comportement attendu, comportement
observé et moyen de réponse choisi.

Les retours sont classés par barrière et tâche. Une urgence de sécurité, comme un risque photosensible, suit une
procédure accélérée sans promettre un diagnostic ou une prise en charge médicale.

> **[WEB] Navigateur internet — Consulter les références officielles de la section 49.**

La revue web vérifie la date, la version, la portée et le caractère normatif ou informatif de chaque source. Le registre
conserve la source, la date de consultation et l’impact sur la matrice. Cette lecture ne conclut ni à une conformité
globale ni à une absence de risque.

## 45. Mode Solo et Mode Studio

En mode Solo, une même personne peut cumuler conception, implémentation et test, mais sépare les moments de décision.
Elle utilise une matrice courte, des profils fonctionnels réutilisables, des parcours prioritaires et une revue externe
ciblée sur les risques qu’elle ne peut pas évaluer seule.

En mode Studio, un propriétaire accessibilité coordonne design, UI, audio, QA, production, localisation, support et
publication. Les équipes de fonctionnalité restent responsables de leurs barrières ; le spécialiste n’est pas un guichet
chargé de corriger seul toutes les omissions.

| Responsabilité | Mode Solo | Mode Studio |
|---|---|---|
| Matrice | Backlog unique et priorisé | Registre partagé avec propriétaires par fonctionnalité |
| Revue | Auto-revue différée puis pair externe | Revue croisée design, développement et QA |
| Tests utilisateurs | Sessions limitées mais préparées correctement | Programme récurrent avec recrutement accessible |
| Plateformes | Cibles prioritaires déclarées | Matrice par plateforme, périphérique et build |
| Déclaration | Page courte et factuelle | Publication coordonnée avec juridique, support et release |
| Régression | Parcours essentiels | Suites ciblées et campagne produit complète |

## 46. Critère d’acceptation documentaire

Le chapitre est acceptable lorsque chaque objectif du plan maître possède un contrat, une frontière et une méthode de
preuve ; lorsque les options ne déplacent pas l’autorité métier ; lorsque les limites sont explicites ; et lorsque les
diagnostics couvrent les échecs les plus probables.

La porte documentaire ne ferme pas les réserves de build, de matériel, de technologies d’assistance, de sessions
utilisateurs, de photosensibilité, de publication ou de support.

> **[SORTIE] Décision documentaire attendue.**

```text
chapter=18
scope=whole_product_accessibility
blocking_documentary_errors=0
runtime_executed=false
user_sessions_executed=false
photosensitivity_review_executed=false
public_claims_verified=false
decision=accepted_with_runtime_reservations
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Portée :** La décision concerne l’accessibilité du produit complet au niveau documentaire.
- **Zéro erreur :** Le compteur vise les non-conformités de rédaction et de structure.
- **Réserves :** Les quatre valeurs `false` empêchent toute surinterprétation.
- **Décision :** L’acceptation avec réserves autorise le chapitre, pas une promesse produit.

## 47. Checklist opérationnelle

- les réglages sont atteignables au premier démarrage et au clavier ou à la manette ;
- toutes les actions essentielles sont nommées, remappables ou justifiées ;
- les maintiens, répétitions rapides et combinaisons possèdent des alternatives ;
- zones mortes, sensibilités et inversions sont séparées par périphérique ;
- les informations critiques utilisent plusieurs canaux ;
- la couleur ne porte jamais seule un état essentiel ;
- le texte agrandi ne coupe ni contrôle ni information ;
- le focus initial, l’ordre, le retour et la visibilité sont vérifiés ;
- les mouvements, tremblements, zooms et flashs possèdent une porte dédiée ;
- les captions couvrent dialogue, locuteur et sons utiles ;
- les catégories audio, le ducking, le mono et la dynamique sont documentés ;
- le TTS et les API d’accessibilité sont qualifiés par plateforme ;
- les aides de rythme et de motricité décrivent leurs effets exacts ;
- les profils restent composables, réversibles et non diagnostiques ;
- les parcours représentatifs couvrent menus, gameplay, cinématiques et reprise ;
- les sessions utilisateurs préparent consentement, retrait, confidentialité et accessibilité ;
- les limites connues sont reliées à un build et publiables ;
- la déclaration publique ne liste que les fonctions réellement vérifiées ;
- le support n’exige aucune donnée médicale non nécessaire ;
- la campagne de publication réutilise exactement les octets qualifiés.

## 48. Diagnostics et corrections

<!-- qa:error-correction-section -->

Les dix cas suivants enseignent des échecs reproductibles. Chaque correction restaure un invariant précis sans prétendre
qu’un exemple statique a été exécuté.

### 48.1 Cacher les réglages derrière le premier obstacle

**Symptôme ou risque :** Le joueur doit terminer une cinématique non sous-titrée avant d’atteindre les options.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
first_boot:
  accessibility_entry: after_intro
  intro_requires_audio: true
  skip_available: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** Le chemin impose exactement la modalité qui devrait pouvoir être adaptée et bloque l’accès à la correction.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
first_boot:
  accessibility_entry: before_intro
  intro_requires_audio: false
  captions_default: true
  skip_available: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** Les réglages et l’alternative apparaissent avant le contenu qui pourrait exclure le joueur.

### 48.2 Traiter un préréglage comme un diagnostic

**Symptôme ou risque :** Le produit active un ensemble figé dès qu’une déficience est sélectionnée.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
profile_name: vision_impairment
locked_options: true
assumed_needs: universal
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** Le produit suppose des besoins uniformes, demande une identité sensible et empêche les ajustements individuels.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
profile_name: enhanced_text_and_contrast
locked_options: false
individual_overrides: allowed
medical_data_required: false
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** Le nom décrit les effets, les options restent libres et aucune donnée médicale n’est nécessaire.

### 48.3 Remapper une action sans mettre à jour les invites

**Symptôme ou risque :** Le tutoriel continue d’afficher l’ancienne touche et rend la consigne fausse.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
action: interact
active_binding: Key:E
tutorial_prompt: Key:F
prompt_source: static_texture
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** L’invite statique diverge de la source de vérité et peut bloquer le tutoriel.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
action: interact
active_binding: Key:E
tutorial_prompt_source: input_binding_service
prompt_refresh: on_binding_changed
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** La présentation consomme le binding actif et se rafraîchit après chaque changement.

### 48.4 Dépendre uniquement de la couleur

**Symptôme ou risque :** Les états sûr et dangereux utilisent la même forme et aucun libellé.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
safe: {color: green, icon: circle}
danger: {color: red, icon: circle}
labels: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** La signification disparaît lorsque les couleurs sont confondues, absentes ou altérées.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
safe: {color: green, icon: shield, label: Sûr}
danger: {color: red, icon: warning_triangle, label: Danger}
color_only_encoding: false
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** Forme et texte conservent l’état tandis que la couleur reste un renforcement.

### 48.5 Fournir des sous-titres sans captions

**Symptôme ou risque :** Les dialogues sont transcrits, mais un danger sonore hors champ reste invisible.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
dialogue_subtitles: true
non_speech_captions: false
directional_audio_cues: audio_only
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** Le joueur reçoit les paroles mais manque une information sonore nécessaire au gameplay.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
dialogue_subtitles: true
non_speech_captions: true
directional_audio_cues: visual_and_audio
caption_categories: configurable
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** Les sons utiles disposent d’une représentation réglable et d’un indicateur directionnel cohérent.

### 48.6 Ajouter un avertissement sans réduire les flashs

**Symptôme ou risque :** Le produit affiche un écran de prudence puis conserve des séquences non évaluées.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
warning_screen: true
flash_review: not_run
known_flashes: unknown
release_gate: open
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** L’avertissement transfère le risque au joueur et remplace à tort l’élimination ou l’évaluation.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
warning_screen: informational
flash_review: required
known_flashes: inventoried
release_gate: blocked_until_evidence
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** La porte reste bloquée jusqu’à l’inventaire, l’analyse et la revue appropriée.

### 48.7 Imposer plusieurs boutons simultanés

**Symptôme ou risque :** Un menu radial exige un maintien pendant le déplacement du stick.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
open_radial: hold_LB
select_item: analog_stick_while_holding
single_press_alternative: false
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** La combinaison exige force, portée et coordination continues malgré le remapping.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
open_radial: toggle_LB
select_item: dpad_or_analog
confirm_item: single_press
single_press_alternative: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** La bascule et les entrées séquentielles permettent la même sélection sans maintien simultané.

### 48.8 Présenter un test automatisé comme preuve universelle

**Symptôme ou risque :** Un lint vert est utilisé pour déclarer le jeu entièrement accessible.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
automated_lint: pass
user_journeys: not_run
platform_checks: not_run
public_claim: fully_accessible
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** Le lint ne mesure ni compréhension, confort, technologies d’assistance ni interactions entre options.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
automated_lint: pass
user_journeys: not_run
platform_checks: not_run
public_claim: prepared_features_only
known_limits: published
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** La déclaration reste limitée aux faits vérifiés et expose les réserves restantes.

### 48.9 Enregistrer un profil invalide sans retour arrière

**Symptôme ou risque :** Une échelle extrême rend le menu inutilisable et devient la valeur persistée.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
text_scale: 5.0
preview: false
auto_revert: false
persist_before_validation: true
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** La valeur non bornée est persistée avant que le joueur puisse confirmer ou restaurer l’interface.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
text_scale: 1.5
preview: true
auto_revert_seconds: 20
persist_after_confirmation: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** La prévisualisation bornée conserve l’ancien profil et n’écrit qu’après confirmation.

### 48.10 Publier une déclaration d’une autre version

**Symptôme ou risque :** La fiche boutique décrit les fonctions testées sur un ancien build.

**Exemple fautif :**

> **[LECTURE] Exemple fautif — Ne pas appliquer.**

```yaml
statement_build: AST-BUILD-017
release_build: AST-BUILD-018
digest_match: false
publish: true
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :**

- **Invariant violé :** La déclaration et les octets publiés ne partagent plus la même preuve.

**Exemple corrigé :**

> **[LECTURE] Exemple corrigé — Adapter au projet réel.**

```yaml
statement_build: AST-BUILD-018
release_build: AST-BUILD-018
digest_match: true
publish: candidate_after_review
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :**

- **Invariant restauré :** La corrélation d’identité et d’empreinte est rétablie avant la revue de publication.

## 49. Références techniques officielles

- [W3C — Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/)
- [W3C WAI — Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/Understanding/)
- [Microsoft — Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/)
- [Microsoft — XAG 101 : Text display](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/101)
- [Microsoft — XAG 103 : Additional channels for visual and audio cues](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/103)
- [Microsoft — XAG 104 : Subtitles and captions](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/104)
- [Microsoft — XAG 105 : Audio accessibility](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/105)
- [Microsoft — XAG 107 : Input](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/107)
- [Microsoft — XAG 108 : Game difficulty options](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/108)
- [Microsoft — XAG 112 : UI navigation](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/112)
- [Microsoft — XAG 116 : Time limits](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/116)
- [Microsoft — XAG 117 : Visual distractions and motion settings](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/117)
- [Microsoft — XAG 118 : Photosensitivity](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/118)
- [Microsoft — XAG 121 : Accessible feature documentation](https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/121)
- [Godot Engine 4.7 — Input examples and InputMap](https://docs.godotengine.org/en/4.7/tutorials/inputs/input_examples.html)
- [Godot Engine 4.7 — InputMap](https://docs.godotengine.org/en/4.7/classes/class_inputmap.html)
- [Godot Engine 4.7 — DisplayServer](https://docs.godotengine.org/en/4.7/classes/class_displayserver.html)
- [Godot Engine 4.7 — Text to speech](https://docs.godotengine.org/en/4.7/tutorials/audio/text_to_speech.html)

WCAG 2.2 est une norme destinée au contenu web. Le chapitre en réutilise certains critères comme objectifs mesurables
lorsque leur intention se transpose utilement à une interface de jeu, sans déclarer automatiquement une conformité WCAG
du produit natif.

Les Xbox Accessibility Guidelines sont des bonnes pratiques de conception et de test, pas une certification ni un
catalogue d’obligations légales. Les pages sont revérifiées au moment de la matérialisation, car leur contenu et leur
organisation peuvent évoluer.

Les API Godot dépendent de la plateforme et du moteur réellement utilisé. Les signatures, capacités TTS, voix, latences,
rôles accessibles et intégrations de lecteurs d’écran doivent être qualifiés sur chaque cible avant publication.

## 50. Synthèse opérationnelle pour `Project Asteria`

`Project Asteria` adopte une matrice d’accessibilité centrée sur des tâches observables. Chaque barrière relie un
parcours, une demande sensorielle, cognitive, temporelle ou motrice, une option candidate, un propriétaire, une
plateforme, une limite et les preuves requises.

Les réglages forment des profils composables, réversibles et indépendants des diagnostics. Ils sont disponibles dès le
premier démarrage, persistés séparément de l’état gameplay et appliqués par des ports de présentation. Le remapping
repose sur des actions nommées ; les maintiens, répétitions et combinaisons possèdent des alternatives.

Les informations critiques utilisent plusieurs canaux. Couleur, son et vibration ne deviennent jamais des autorités
exclusives. Texte, focus, captions, mixage, mouvement, caméra, photosensibilité, TTS, aide motrice, rythme et
récupération possèdent des portes distinctes et des limites publiables.

La validation future combinera contrôles automatiques, revues spécialisées, parcours représentatifs, technologies
d’assistance et sessions utilisateurs préparées avec consentement et minimisation. Une méthode isolée ne suffira pas à
déclarer le produit accessible.

La déclaration publique sera liée au même build que la matrice et les rapports. Tant que les options, plateformes,
périphériques, technologies d’assistance, parcours, sessions et revues de sécurité n’ont pas été exécutés et conservés,
aucune conformité globale ni accessibilité complète de `Project Asteria` n’est revendiquée.
