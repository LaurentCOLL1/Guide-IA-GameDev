---
title: "Livre IV — Chapitre 19 : Localisation et internationalisation"
id: "DOC-L4-CH19"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 19
last-verified: "2026-07-27T18:41:51+02:00"
audit-status: "complete"
audit-date: "2026-07-27T18:41:51+02:00"
audit-report: "Livre-IV/QA/AUDIT-CHAPITRE-19.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
reference-project:
  name: "Project Asteria"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Localisation et internationalisation

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes Windows, **[WSL]** terminal Linux ou WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir et **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).


## 1. Rôle du chapitre

Le chapitre 18 possède l’accessibilité du produit complet et ses parcours représentatifs. Le présent chapitre possède
l’internationalisation de l’architecture, la localisation des contenus, les formats culturels, les écritures, les polices,
la pseudo-localisation, la traduction, la relecture linguistique et les contrôles de régression associés.

Le chapitre 17 conserve les pages boutique et la publication initiale. Le chapitre 20 conservera les correctifs,
mises à jour distribuées et retours arrière. La création artistique des voix appartient au Livre III ; ici, les voix
localisées sont inventoriées, reliées aux sous-titres et contrôlées comme variantes linguistiques.

Le niveau de preuve reste `static-review`. Aucun catalogue Godot, fichier PO final, police qualifiée, doublage,
capture localisée, test de débordement runtime, relecture native ou build multilingue de `Project Asteria` n’est revendiqué.


> **[LECTURE] Carte de responsabilité — Ne pas saisir.**

```yaml
localization_scope:
  architecture_owner: chapter-19
  accessibility_owner: chapter-18
  initial_publication_owner: chapter-17
  updates_owner: chapter-20
  voice_asset_owner: livre-iii-chapter-26
evidence_level: static-review
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Autorités :** Chaque clé attribue un sujet à un chapitre propriétaire unique.
- **Frontière :** Le présent chapitre consomme l’accessibilité et les voix sans reprendre leur conception.
- **Niveau de preuve :** `static-review` interdit de présenter les exemples comme des fichiers exécutés.
- **Résultat attendu :** Une demande de traduction, de format culturel ou d’écriture est routée vers le chapitre 19.


## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur saura :

- distinguer internationalisation, localisation, traduction, transcréation et adaptation culturelle ;
- concevoir des identifiants stables indépendants du texte source ;
- externaliser chaînes, dialogues, métadonnées et contenus culturels ;
- traiter variables, pluriels, genres grammaticaux, dates, nombres, devises et unités ;
- préparer écritures latines et non latines, sens gauche-droite et droite-gauche, segmentation et saisie ;
- sélectionner des familles de polices et des stratégies de repli sans masquer les glyphes manquants ;
- organiser sous-titres, voix, lip-sync et variantes de médias par locale ;
- exécuter une pseudo-localisation, des contrôles de débordement et des audits de clés ;
- organiser traduction, relecture, validation en contexte et gestion des retours ;
- diagnostiquer dix erreurs fréquentes de localisation.


## 3. Vocabulaire opérationnel

L’**internationalisation**, souvent abrégée `i18n`, prépare le produit à plusieurs langues et conventions sans dupliquer
sa logique. La **localisation**, ou `l10n`, adapte le produit à une locale définie. Une **locale** combine généralement
langue, région et parfois écriture, par exemple `fr-FR`, `pt-BR` ou `sr-Latn-RS`.

La **traduction** transforme le contenu linguistique. La **transcréation** adapte une intention lorsque la formulation
littérale échoue. L’**adaptation culturelle** traite symboles, références, conventions, restrictions et attentes locales.
Une **clé** est un identifiant stable ; une **chaîne source** est un contenu éditorial qui peut changer sans modifier la clé.


> **[LECTURE] Glossaire minimal — Exemple de données.**

```json
{
  "key": "ui.inventory.capacity",
  "source_locale": "fr-FR",
  "target_locale": "en-GB",
  "status": "candidate",
  "context": "inventory_header",
  "max_visual_lines": 1
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `key` reste stable lorsque la formulation source évolue.
- **Locales :** `source_locale` et `target_locale` séparent langue d’auteur et langue livrée.
- **Contexte :** `context` aide le traducteur à choisir le sens correct.
- **Contrainte visuelle :** `max_visual_lines` décrit un budget d’interface à vérifier, pas une troncature automatique.
- **Résultat attendu :** Le catalogue peut être recherché, traduit et testé sans dépendre du texte affiché.


## 4. Périmètre et frontières

Le périmètre comprend menus, HUD, tutoriels, quêtes, dialogues, codex, sous-titres, captions, notifications, erreurs,
contenus système, pages d’aide, métadonnées internes et textes visibles avant achat lorsque la publication les consomme.

Le chapitre n’enseigne pas la linguistique générale, ne remplace pas une relecture native, ne garantit pas la conformité
légale d’un territoire et ne transforme pas une traduction automatique en contenu approuvé. Les exigences de chaque
plateforme restent volatiles et sont vérifiées dans le registre du chapitre 17.


## 5. Concevoir les locales prises en charge

Une locale ne se réduit pas à deux lettres. Le produit distingue la langue de texte, la langue audio, la région de format,
l’écriture et les préférences du joueur. Une politique de repli explicite évite qu’un contenu absent bascule silencieusement
vers une langue inattendue.

`Project Asteria` retient `fr-FR` comme locale source documentaire. Les locales candidates ne deviennent supportées
qu’après couverture des chaînes, revue linguistique, qualification des polices, validation en contexte et décision de publication.

Le registre éditorial conserve des balises BCP 47 avec traits d’union. À la frontière Godot,
`TranslationServer.standardize_locale()` normalise la valeur vers la forme reconnue par le moteur, par exemple `fr_FR`.
La valeur saisie par le joueur et la valeur normalisée sont distinguées dans les journaux de diagnostic.


> **[VSC] Fichier candidat `localization/locales.yaml`.**

```yaml
schema: asteria-locales-v1
source_locale: fr-FR
fallback_locale: fr-FR
candidates:
  - locale: en-GB
    text: planned
    audio: not_planned
    script: Latn
    direction: ltr
  - locale: ar
    text: research
    audio: not_planned
    script: Arab
    direction: rtl
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Schéma :** `schema` permet de faire évoluer le registre.
- **Repli :** `fallback_locale` est explicite et identique pour tous les environnements qualifiés.
- **Capacités :** `text` et `audio` sont séparés ; une langue de texte n’implique pas un doublage.
- **Écriture :** `script` et `direction` préparent polices, shaping et mise en page.
- **Résultat attendu :** L’équipe sait quelles combinaisons sont candidates, recherchées ou exclues.


## 6. Utiliser des clés stables

Une clé décrit une intention ou un emplacement fonctionnel, jamais la phrase actuelle. Elle évite les identifiants basés
sur le texte source, qui cassent dès qu’une correction éditoriale intervient. Les clés sont hiérarchiques, en minuscules,
séparées par des points et dépourvues de numéros de ligne ou de chemin de scène fragile.


> **[LECTURE] Convention de clés — Exemple de référence.**

```text
ui.main_menu.continue
ui.settings.language
quest.relay_intro.objective
dialogue.scout.relay_warning
system.save.incompatible_version
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Préfixes :** `ui`, `quest`, `dialogue` et `system` séparent les domaines.
- **Stabilité :** Les clés ne recopient pas le texte français.
- **Recherche :** La hiérarchie facilite les audits par fonctionnalité.
- **Limite :** Une clé ne contient ni ponctuation visible ni index de ligne.
- **Résultat attendu :** Une reformulation ne provoque pas de suppression et recréation artificielle de traduction.


## 7. Externaliser les chaînes dans Godot

Godot peut utiliser des ressources de traduction importées et des clés passées à `tr()`. Le texte visible ne doit pas être
concaténé dans le code métier. Les scènes peuvent porter des clés, tandis qu’un service de présentation résout la locale
courante. Les chaînes dynamiques utilisent des paramètres nommés afin que le traducteur puisse réordonner les éléments.


> **[VSC] Script candidat `src/core/localization/localized_text.gd`.**

```gdscript
class_name LocalizedText
extends RefCounted

static func format_key(key: StringName, values: Dictionary = {}) -> String:
    var template: String = String(TranslationServer.translate(key))
    if values.is_empty():
        return template
    return template.format(values)
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Classe :** `LocalizedText` regroupe une transformation de présentation sans devenir un Autoload ; l’appel au singleton `TranslationServer` reste valide depuis cette méthode statique.
- **Paramètre `key` :** `StringName` représente l’identifiant stable transmis à `TranslationServer.translate()` ; la conversion `String(...)` produit le type de retour explicite de la fonction.
- **Paramètre `values` :** Le dictionnaire associe des noms explicites à leurs valeurs ; `{}` évite d’imposer des variables.
- **Retour :** La fonction renvoie toujours un `String` prêt à afficher.
- **Branche :** `is_empty()` évite un formatage inutile et conserve les accolades littérales non destinées au moteur.
- **Limite :** La fonction ne choisit pas la locale et ne valide pas les pluriels.


## 8. Éviter la concaténation linguistique

L’ordre des mots varie selon les langues. Une construction comme `nom + " possède " + quantité + " objets"` impose
l’ordre français et fragmente la traduction. Une seule unité traduisible doit porter le message complet et ses variables.


> **[VSC] Message paramétré — Structure candidate.**

```json
{
  "key": "inventory.owner_count",
  "source": "{owner} possède {count} objets.",
  "variables": {
    "owner": "String",
    "count": "int"
  }
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Message complet :** Le traducteur peut déplacer `{owner}` et `{count}`.
- **Types :** Le contrat documente les valeurs fournies par le code.
- **Sécurité :** Les variables ne contiennent pas de balisage arbitraire.
- **Résultat attendu :** La phrase reste grammaticale lorsque l’ordre change.


## 9. Paramètres, balisage et sécurité

Les variables utilisent des noms sémantiques. Les contenus de joueur sont échappés avant insertion dans du RichText.
Les balises autorisées sont séparées du texte libre et revues comme une petite grammaire. Une traduction ne doit jamais
pouvoir appeler une commande, charger un fichier ou modifier l’état métier.


## 10. Pluriels et quantités

Le pluriel ne se limite pas à `un` contre `plusieurs`. Certaines langues possèdent davantage de catégories. Le catalogue
doit conserver les formes nécessaires et déléguer la sélection à une règle de locale qualifiée. Le code transmet la
quantité numérique ; il ne choisit pas une forme française avant traduction.


> **[LECTURE] Entrée de pluriel — Modèle conceptuel.**

```yaml
key: inventory.item_count
type: plural
variable: count
forms:
  one: "{count} objet"
  other: "{count} objets"
status: candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Type :** `plural` distingue cette entrée d’une chaîne simple.
- **Variable :** `count` reste numérique jusqu’au formatage.
- **Formes :** `one` et `other` suffisent pour le français, pas nécessairement pour toutes les locales.
- **Statut :** `candidate` réserve la validation à l’outil réellement adopté.
- **Résultat attendu :** Le catalogue expose les catégories manquantes au lieu de les inventer.


## 11. Genre grammatical et références

Le genre d’une personne, le genre grammatical d’un nom et la forme d’adresse sont des dimensions distinctes. Le produit
évite de dériver automatiquement une grammaire depuis une identité. Lorsque la langue exige plusieurs variantes, le contrat
déclare les dimensions utiles et prévoit une formulation neutre de repli validée éditorialement.


## 12. Dates, heures et calendriers

Les instants sont stockés dans un format stable, généralement UTC, puis rendus selon une locale et un fuseau choisis.
Une date affichée ne doit pas être reconstruite depuis une chaîne localisée. Les calendriers fictifs de `Project Asteria`
restent des données de gameplay et utilisent leurs propres règles, séparées des dates civiles de fichiers et de support.


> **[LECTURE] Contrat de format de date — Exemple.**

```json
{
  "instant_utc": "2026-07-27T15:35:44Z",
  "display_locale": "fr-FR",
  "time_zone": "Europe/Paris",
  "style": "medium",
  "status": "candidate"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Instant :** `instant_utc` identifie le moment sans ambiguïté locale.
- **Locale :** `display_locale` règle l’ordre et les noms visibles.
- **Fuseau :** `time_zone` détermine l’heure civile.
- **Style :** `medium` est une intention de présentation à mapper vers l’API retenue.
- **Résultat attendu :** Le même instant peut être affiché différemment sans modifier la donnée canonique.


## 13. Nombres, pourcentages et devises

Les séparateurs décimaux, groupements, signes et espaces varient. Les valeurs restent numériques jusqu’au rendu. Un prix
candidat français s’écrit par exemple `19,99 €` dans la prose, mais le contrat de données conserve séparément le montant
décimal et le code `EUR`. Le chapitre 17 reste propriétaire du prix commercial réel.


> **[LECTURE] Montant candidat — Ne pas publier.**

```yaml
amount:
  value: "19.99"
  currency: EUR
display_locale: fr-FR
authority: chapter-17
status: candidate
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Valeur :** La chaîne décimale évite une perte binaire pendant l’échange documentaire.
- **Devise :** `EUR` est séparé du symbole affiché.
- **Locale :** `fr-FR` produirait une présentation comme `19,99 €` dans un formateur qualifié.
- **Autorité :** Le chapitre 19 formate ; le chapitre 17 approuve la donnée commerciale.
- **Résultat attendu :** Une adaptation d’affichage ne change jamais le prix canonique.


## 14. Unités et mesures

Les unités ne sont pas concaténées après un nombre. Le système conserve une valeur canonique, une unité de stockage et une
préférence d’affichage. Toute conversion est explicite, testée et arrondie selon une règle documentée. Les unités de gameplay
fictionnelles restent dans le domaine concerné.


## 15. Écritures, direction et ordre visuel

Les interfaces doivent supporter le sens gauche-droite et droite-gauche sans miroir naïf. L’ordre logique du texte,
l’ordre visuel, l’alignement, les icônes directionnelles, les marges et les animations peuvent demander des adaptations
différentes. Les nombres, chemins, identifiants et fragments techniques peuvent conserver une direction locale au sein
d’un paragraphe opposé.


> **[VSC] Métadonnées de direction — Exemple candidat.**

```yaml
locale: ar
direction: rtl
mirror_layout: true
mirror_directional_icons: reviewed_only
preserve:
  - product_codes
  - file_paths
  - numeric_ids
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Direction :** `rtl` pilote la mise en page, pas la traduction.
- **Miroir :** `mirror_layout` autorise une réorganisation générale.
- **Icônes :** Les symboles directionnels sont revus ; un logo ou une icône non directionnelle ne doit pas être inversé.
- **Préservation :** Codes, chemins et identifiants gardent leur ordre utile.
- **Résultat attendu :** Le test distingue texte bidirectionnel et miroir d’interface.


## 16. Segmentation, shaping et saisie

Une chaîne Unicode n’est pas une suite simple de lettres visibles. Les graphèmes peuvent combiner plusieurs points de code.
Le shaping choisit les glyphes selon le contexte. La navigation du curseur, la sélection, la suppression et les limites de
longueur doivent respecter les graphèmes plutôt que les octets. Les méthodes de saisie complexes sont testées sur plateforme.


## 17. Polices, glyphes et repli

Une police candidate est qualifiée par écriture, licence, couverture, lisibilité, métriques, poids, hinting et coût mémoire.
Le repli de police est explicite. Un carré de remplacement ou une police système imprévisible n’est pas une stratégie.
Les icônes privées dans une police ne doivent pas entrer en collision avec des caractères Unicode.


> **[LECTURE] Registre de polices — Exemple candidat.**

```yaml
font_stack:
  role: ui_body
  primary: AsteriaSans
  fallbacks:
    - NotoSansArabic
    - NotoSansCJK
  required_scripts:
    - Latn
    - Arab
    - Hans
  licence_review: pending
  runtime_validation: not_run
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle :** `ui_body` sépare cette pile des titres ou du texte monospace.
- **Ordre :** Les fallbacks sont déterministes.
- **Couverture :** `required_scripts` permet un audit automatisé des glyphes.
- **Réserves :** Licence et validation runtime restent explicitement ouvertes.
- **Résultat attendu :** Une locale ne passe pas en publication tant que sa pile n’est pas qualifiée.


## 18. Mise en page flexible

La longueur d’une traduction varie. Les conteneurs, tailles minimales, retours à la ligne, ratios et zones sûres doivent
absorber l’expansion sans réduire automatiquement le texte sous un seuil lisible. Les boutons n’imposent pas une largeur
fixe calculée sur le français. Les chaînes critiques disposent de budgets visuels testables.


## 19. Pseudo-localisation

La pseudo-localisation transforme les chaînes source pour révéler les textes codés en dur, les débordements, les glyphes
manquants et les concaténations. Elle conserve les variables et balises autorisées. Une variante accentuée et allongée
teste l’expansion ; une variante bidirectionnelle teste l’ordre et les isolats.


> **[PS] Script candidat de pseudo-localisation — PowerShell 7.**

```powershell
param(
    [Parameter(Mandatory)]
    [string]$InputPath,
    [Parameter(Mandatory)]
    [string]$OutputPath
)

function Convert-NaturalText {
    param([Parameter(Mandatory)][string]$Text)

    $protected = '\{[A-Za-z_][A-Za-z0-9_]*\}|\[[^\]]+\]'
    $cursor = 0
    $builder = [System.Text.StringBuilder]::new()

    foreach ($match in [regex]::Matches($Text, $protected)) {
        $segment = $Text.Substring($cursor, $match.Index - $cursor)
        $segment = $segment.Replace('a', 'á').Replace('e', 'ë')
        [void]$builder.Append($segment)
        [void]$builder.Append($match.Value)
        $cursor = $match.Index + $match.Length
    }

    $tail = $Text.Substring($cursor).Replace('a', 'á').Replace('e', 'ë')
    [void]$builder.Append($tail)
    return "[!! $builder ～～ !!]"
}

$data = Get-Content -LiteralPath $InputPath -Raw | ConvertFrom-Json
foreach ($entry in $data.entries) {
    $entry.text = Convert-NaturalText -Text $entry.text
}
$data | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $OutputPath -Encoding utf8
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètres :** `InputPath` et `OutputPath` sont obligatoires et séparés pour préserver la source.
- **Lecture :** `-Raw` évite de traiter le JSON ligne par ligne.
- **Protection :** L’expression régulière isole les variables `{name}` et les balises `[tag]` avant toute transformation.
- **Parcours :** `cursor` et `Substring()` transforment uniquement les segments de langue naturelle entre les tokens protégés.
- **Transformation :** Les remplacements accentuent le texte et les délimiteurs rendent les omissions visibles.
- **Retour :** `Convert-NaturalText` renvoie une nouvelle chaîne ; la source reste lue depuis un fichier distinct.
- **Sérialisation :** `-Depth 8` conserve les objets imbriqués du catalogue.
- **Effet de bord :** Le script écrit un nouveau fichier ; il ne doit pas viser le catalogue source.
- **Limite :** Cette version pédagogique doit être enrichie pour protéger variables et balises avant usage réel.


## 20. Protéger variables et balises pendant la pseudo-localisation

Une transformation naïve peut altérer `{count}`, `%s`, des tags ou des codes. Le pipeline tokenize les éléments protégés,
transforme uniquement le texte naturel, puis restaure les tokens et vérifie leur identité. Toute variable perdue, ajoutée
ou renommée bloque le lot.


## 21. Catalogue de traduction

Le catalogue conserve clé, texte source, commentaire, capture ou contexte, variables, contraintes, propriétaire, statut,
version source et historique. Les doublons sémantiques sont signalés mais ne sont pas fusionnés automatiquement : deux
contextes identiques aujourd’hui peuvent diverger demain.


> **[VSC] Entrée de catalogue — Exemple candidat.**

```yaml
key: dialogue.scout.relay_warning
source: "Le relais n’est pas sûr."
context:
  speaker: scout
  scene: relay_entry
  intent: warning
variables: []
max_lines: 2
owner: narrative
source_revision: 4
translation_status: ready_for_translation
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contexte narratif :** Locuteur, scène et intention réduisent les ambiguïtés.
- **Contraintes :** `max_lines` doit être vérifié en contexte et ne justifie pas une traduction incorrecte.
- **Révision :** `source_revision` permet d’invalider une traduction après modification.
- **Statut :** `ready_for_translation` n’équivaut ni à traduit ni à approuvé.
- **Résultat attendu :** Le traducteur reçoit assez d’information pour produire une proposition traçable.


## 22. Formats CSV, PO et ressources Godot

Le format retenu dépend des outils et des besoins. CSV est simple mais fragile pour les retours à la ligne et métadonnées.
PO offre commentaires, contextes et pluriels. Les ressources Godot facilitent l’intégration moteur. Le dépôt conserve une
source canonique et génère les formats dérivés ; deux formats ne deviennent pas deux autorités concurrentes.


## 23. Extraction des chaînes

L’extraction automatise la découverte des clés mais ne comprend pas toutes les intentions. Les chaînes calculées, données
externes, dialogues et ressources doivent être inventoriés. Une clé supprimée passe par une période d’obsolescence avant
purge afin de ne pas perdre une traduction encore référencée par une branche ou une sauvegarde.


> **[WSL] Audit candidat des clés — Terminal Linux ou WSL.**

```bash
set -euo pipefail
python tools/localization/audit_keys.py   --catalog localization/catalog.yaml   --source-root src   --scene-root scenes   --report build/reports/localization-keys.json
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Mode strict :** `set -euo pipefail` arrête le script sur commande, variable ou pipeline défaillant.
- **Arguments :** Les chemins séparent catalogue, scripts, scènes et rapport.
- **Retour :** Le processus doit renvoyer un code non nul lorsque des clés manquent ou sont orphelines au-delà de la politique.
- **Effet de bord :** Seul le rapport sous `build/reports` est produit.
- **Résultat attendu :** La CI distingue clé absente, inutilisée, dupliquée et dynamique non vérifiable.


## 24. Traduction et statuts éditoriaux

Le workflow distingue brouillon, traduit, relu, validé en contexte, approuvé et publié. Une traduction automatique peut
alimenter un brouillon identifié, jamais un statut approuvé. Toute modification de la source invalide ou marque à revoir
les locales concernées selon la portée réelle du changement.


> **[LECTURE] Machine d’états linguistique — Exemple.**

```text
source_ready
  -> translated
  -> linguistic_reviewed
  -> in_context_reviewed
  -> approved
  -> published

source_changed -> needs_update
rejected -> translated
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Étapes :** La traduction et la validation en contexte sont séparées.
- **Retour :** `rejected` revient à une proposition traduite au lieu d’effacer l’historique.
- **Invalidation :** `source_changed` évite de conserver silencieusement une version périmée.
- **Résultat attendu :** Une locale publiée possède une chaîne de décisions consultable.


## 25. Relecture linguistique et validation en contexte

La relecture linguistique contrôle sens, grammaire, terminologie, ton et cohérence. La validation en contexte contrôle
débordement, locuteur, synchronisation, variables, interaction, lisibilité et cohérence avec l’image. Une capture aide,
mais une interaction réelle reste nécessaire pour les contenus dynamiques.


## 26. Terminologie et mémoire de traduction

Le glossaire définit termes interdits, préférés, variables, noms propres et formes flexibles. La mémoire de traduction
propose des correspondances ; elle ne remplace pas la décision contextuelle. Les droits, la confidentialité et la
provenance des corpus sont enregistrés avant utilisation par un outil local ou distant.


> **[VSC] Glossaire candidat `localization/glossary.yaml`.**

```yaml
terms:
  - id: relay
    source: relais
    domain: world
    do_not_translate: false
    notes: "Installation technique, pas une course."
  - id: asteria
    source: Asteria
    domain: product
    do_not_translate: true
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `id` permet de renommer la forme source sans perdre les décisions.
- **Domaine :** `domain` distingue un terme du monde d’un nom de produit.
- **Instruction :** `do_not_translate` est explicite et justifiée.
- **Contexte :** `notes` prévient un faux sens fréquent.
- **Résultat attendu :** Les contrôles terminologiques peuvent produire des alertes ciblées.


## 27. Noms propres, variables et contenu généré

Les noms propres peuvent être traduits, translittérés ou conservés selon une décision éditoriale. Les noms créés par le
joueur restent des données et ne passent pas dans le catalogue. Le contenu généré dynamiquement doit annoncer sa locale,
ses contraintes et son statut ; il ne reçoit pas automatiquement la qualité d’une traduction approuvée.


## 28. Sous-titres, captions et voix localisées

Le texte de sous-titre, les captions sonores et la transcription de voix sont des objets liés mais distincts. Les timecodes,
identifiants de locuteur, limites de lignes et variantes d’accessibilité doivent rester corrélés à l’asset audio. Une voix
localisée peut modifier la durée ; le montage et le lip-sync sont revalidés sans accélérer artificiellement la parole.


> **[LECTURE] Manifeste de dialogue localisé — Exemple candidat.**

```json
{
  "line_id": "AST-DLG-RELAY-0042",
  "locale": "en-GB",
  "subtitle_key": "dialogue.scout.relay_warning",
  "audio_asset": null,
  "timing_status": "not_run",
  "lip_sync_status": "not_run",
  "caption_review": "pending"
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Identité :** `line_id` relie texte, audio, timing et animation.
- **Locale :** La variante linguistique est explicite.
- **Absence d’audio :** `null` indique qu’aucun doublage n’est promis.
- **Statuts :** Timing, lip-sync et caption sont indépendants.
- **Résultat attendu :** Une langue texte seule ne crée pas une fausse revendication de voix localisée.


## 29. Images, textures et texte intégré

Le texte incrusté dans une image est évité. Lorsqu’il est indispensable, la source modifiable, les variantes, les droits,
les dimensions et le processus de régénération sont inventoriés. Les captures boutique appartiennent au dossier de
publication du chapitre 17 mais consomment les locales approuvées.


## 30. Contenus juridiques et réglementaires

Les textes juridiques, politiques de confidentialité, avertissements et classifications suivent une autorité dédiée.
Ils ne sont pas traduits comme une chaîne ordinaire lorsque la juridiction exige une validation spécialisée. Le catalogue
enregistre l’approbateur, la date, la portée territoriale et la version du texte.


## 31. Données culturelles et adaptation

Couleurs, symboles, gestes, nourriture, cartes, noms, références historiques et humour peuvent demander une adaptation.
L’équipe documente le risque et la décision sans essentialiser une population. Une adaptation culturelle ne masque pas
une mécanique ou un événement essentiel sans arbitrage de conception.


## 32. Recherche utilisateur et retours linguistiques

Les retours sont collectés avec consentement, finalité, minimisation et politique de rétention adaptées. Le signalement
d’une faute distingue locale, version, clé, capture, contexte et proposition. La fréquence d’un retour n’autorise pas une
modification automatique du texte publié.


## 33. Tests automatisés de catalogue

Les contrôles automatiques vérifient YAML ou JSON, unicité des clés, variables, balises, formes de pluriel, couverture,
chaînes vides, espaces, ponctuation, caractères interdits, longueurs candidates et références orphelines. Ils ne jugent
pas le naturel ou la justesse culturelle d’une traduction.


> **[PS] Commande candidate d’audit — PowerShell 7.**

```powershell
$python = ".venv\Scripts\python.exe"
& $python tools/localization/validate_catalog.py `
  --catalog localization/catalog.yaml `
  --locales localization/locales.yaml `
  --glossary localization/glossary.yaml `
  --report build/reports/localization-validation.json

if ($LASTEXITCODE -ne 0) {
    throw "La validation du catalogue a échoué avec le code $LASTEXITCODE."
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Interpréteur :** Le chemin vise l’environnement virtuel du projet.
- **Arguments :** Catalogue, locales, glossaire et rapport sont séparés.
- **Code de retour :** `$LASTEXITCODE` conserve le statut du processus Python.
- **Refus contrôlé :** `throw` bloque la tâche lorsque l’audit signale une non-conformité.
- **Résultat attendu :** Un rapport JSON est produit sans modifier les traductions.


### 33.1 Variante Windows `cmd.exe` et sortie attendue

> **[CMD] Invite de commandes — Lancer le même audit depuis la racine du dépôt.**

```bat
@echo off
.venv\Scripts\python.exe tools\localization\validate_catalog.py ^
  --catalog localization\catalog.yaml ^
  --locales localization\locales.yaml ^
  --report build\reports\localization-validation.json
exit /b %ERRORLEVEL%
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Contexte :** Le fichier utilise la syntaxe `cmd.exe`, distincte de PowerShell.
- **Continuation :** Le caret `^` prolonge la commande sur la ligne suivante.
- **Code de retour :** `%ERRORLEVEL%` est propagé avec `exit /b` afin que la CI ou l’appelant détecte un refus.
- **Chemins :** Les séparateurs Windows visent l’environnement virtuel et les fichiers candidats du dépôt.
- **Résultat attendu :** Le processus termine à zéro uniquement lorsque le validateur accepte le catalogue.

> **[SORTIE] Rapport console attendu — Lire sans le saisir.**

```text
localization-validation: PASS
keys: 248
missing: 0
placeholder_mismatches: 0
plural_rule_gaps: 0
report: build/reports/localization-validation.json
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Statut :** `PASS` représente un exemple de sortie, pas un résultat obtenu pour `Project Asteria`.
- **Compteurs :** Les valeurs montrent les catégories que le rapport doit rendre observables.
- **Chemin :** Le rapport persistant permet une comparaison et une revue indépendantes.
- **Limite :** Un catalogue structurellement valide peut encore contenir une traduction incorrecte.
- **Résultat attendu :** Le lecteur sait distinguer commande à exécuter et sortie à vérifier.

## 34. Tests de débordement et captures

Les scènes représentatives sont exécutées avec pseudo-locale longue, tailles de texte accessibles, ratios étroits et
chaînes bidirectionnelles. Les captures sont nommées par build, locale, scène, résolution et profil. Un diff d’image aide
au triage mais ne décide pas seul qu’une interface est correcte.


## 35. Tester les écritures non latines

Une simple substitution de glyphes ne teste ni shaping, ni ordre bidirectionnel, ni segmentation, ni saisie. Les campagnes
incluent texte mixte, nombres, ponctuation, noms propres, retours à la ligne, sélection, copier-coller et navigation au
clavier. Les scripts candidats sont choisis avec des relecteurs compétents.


## 36. Changement de langue et persistance

Le changement de langue doit définir quand l’interface se rafraîchit, quelles scènes sont reconstruites et comment la
préférence est sauvegardée. Les objets métier ne stockent pas le texte traduit. Une sauvegarde conserve identifiants et
valeurs ; l’affichage est recalculé dans la locale active.


> **[VSC] Contrat candidat de préférence linguistique.**

```gdscript
class_name LanguagePreference
extends RefCounted

var text_locale: StringName
var audio_locale: StringName

func _init(text_value: StringName, audio_value: StringName) -> void:
    text_locale = text_value
    audio_locale = audio_value

func to_dictionary() -> Dictionary:
    return {
        "text_locale": String(text_locale),
        "audio_locale": String(audio_locale),
    }
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **État :** Texte et audio sont indépendants.
- **Constructeur :** `_init()` exige les deux valeurs ; aucune locale implicite n’est inventée ici.
- **Sérialisation :** `to_dictionary()` renvoie un `Dictionary` de chaînes stables.
- **Effet de bord :** La classe ne change pas la locale de Godot et n’écrit pas de sauvegarde.
- **Résultat attendu :** La couche de configuration peut persister une préférence sans texte localisé.


## 37. Locale système, choix initial et repli

La locale système peut proposer une valeur initiale, jamais imposer un choix irréversible. Le premier démarrage doit rester
navigable lorsqu’une détection échoue. Le repli est visible dans les diagnostics et ne mélange pas aléatoirement plusieurs
langues dans une même interface.


## 38. Performances et mémoire

Charger toutes les langues, polices et voix peut augmenter RAM, VRAM, stockage et temps de démarrage. Le produit mesure
les coûts par plateforme et peut charger des ressources linguistiques à la demande. Une éviction ne doit pas supprimer
une ressource encore utilisée par une scène ou une voix active.


## 39. Sécurité et confidentialité des outils

Les catalogues peuvent contenir scénario non publié, données personnelles de test ou clauses contractuelles. Les outils
de traduction distante sont évalués avant envoi. Secrets, jetons et identifiants de portail restent hors des fichiers de
localisation et des journaux. Les fournisseurs et modèles IA ne reçoivent pas automatiquement le droit de réutiliser le corpus.


### 39.1 Contextes d’outillage complémentaires

> **[APP] Godot Editor — Ouvrir Project Settings > Localization pour inspecter les ressources déclarées.**

Cette inspection vérifie les traductions et remaps enregistrés sans modifier la locale active. Elle ne remplace pas un test
dans un build exporté. L’opérateur conserve une capture ou une note de revue liée à la révision du catalogue.

> **[WEB] Navigateur — Consulter uniquement les références officielles nommées à la section 46.**

La consultation web sert à vérifier les API, formats et règles susceptibles d’évoluer. Aucune valeur de portail, exigence
commerciale ou promesse de plateforme n’est recopiée sans date et sans source.

> **[DCK] Docker Desktop — Contrôler l’état d’un service linguistique local approuvé avant son utilisation.**

Docker Desktop reste une interface d’exploitation. Le chapitre ne démarre aucun service, n’importe aucune image et ne
présente aucun conteneur comme qualifié. Les versions, volumes, ports et licences restent dans le dossier Studio.

> **[DCT] Terminal dans un conteneur — Exécuter seulement les validateurs inclus dans une image épinglée et approuvée.**

Le terminal conteneurisé reçoit un catalogue minimisé et un répertoire de rapport monté en écriture. Il ne reçoit ni
secret de boutique, ni scénario non approuvé, ni accès au dépôt complet par défaut.

## 40. Organisation Solo et Studio

En mode Solo, une personne maintient un catalogue réduit, priorise les locales réellement soutenables, utilise la
pseudo-localisation tôt et demande une relecture externe ciblée avant publication.

En mode Studio, les rôles source, ingénierie i18n, gestion linguistique, traduction, relecture, QA en contexte,
accessibilité, juridique et publication sont séparés. Les droits d’approbation sont limités et les changements de source
sont gelés pendant les fenêtres de validation.


> **[LECTURE] Matrice RACI simplifiée — Exemple candidat.**

```yaml
activities:
  source_approval:
    responsible: narrative
    accountable: product
  catalog_build:
    responsible: localization_engineering
    accountable: technical_direction
  linguistic_review:
    responsible: native_reviewer
    accountable: localization_lead
  publication_gate:
    responsible: release
    accountable: product
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Responsable :** `responsible` réalise l’activité.
- **Redevable :** `accountable` possède la décision finale.
- **Séparation :** La construction technique ne vaut pas approbation linguistique.
- **Résultat attendu :** Une chaîne rejetée revient au bon rôle sans contourner la porte de publication.


## 41. Portes d’acceptation

Une locale candidate franchit successivement : couverture structurelle, variables et pluriels, terminologie, relecture
linguistique, validation en contexte, accessibilité, polices et écritures, performance, conformité spécialisée,
corrélation au build et décision de publication. Une porte non applicable est justifiée ; elle n’est pas supprimée.


> **[LECTURE] Go/no-go linguistique — Modèle.**

```yaml
locale: en-GB
build_id: candidate-not-materialized
gates:
  catalog_integrity: prepared
  linguistic_review: not_run
  in_context_review: not_run
  font_coverage: not_run
  accessibility_regression: not_run
  publication_approval: not_run
decision: no-go
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Corrélation :** `build_id` rappelle que la décision vise une version précise.
- **États :** `prepared` et `not_run` ne sont pas assimilés à un succès.
- **Décision :** `no-go` est la seule conclusion cohérente tant que les portes ne sont pas exécutées.
- **Résultat attendu :** Le document ne transforme pas une préparation statique en support linguistique réel.


## 42. Diagnostics : dix erreurs fréquentes

<!-- qa:error-correction-section -->

Les cas suivants enseignent des défauts reproductibles. Chaque contre-exemple est immédiatement suivi de sa correction.


### 42.1 Utiliser le texte français comme clé

**Symptôme :** Le produit semble fonctionner dans la locale source mais échoue dès qu’une autre langue ou écriture est activée.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
ui.continue: "Continuer"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Une correction de formulation change l’identité et orpheline les traductions.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
ui.main_menu.continue: "Continuer"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La clé fonctionnelle reste stable lorsque le texte source évolue.


### 42.2 Concaténer une phrase

**Symptôme :** Le produit semble fonctionner dans la locale source mais échoue dès qu’une autre langue ou écriture est activée.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
message = player_name + " possède " + str(count) + " objets"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** L’ordre français est imposé et les fragments perdent leur contexte.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
message = LocalizedText.format_key(&"inventory.owner_count", {"owner": player_name, "count": count})
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le message complet est traduisible et les variables peuvent être réordonnées.


### 42.3 Choisir le pluriel dans le code français

**Symptôme :** Le produit semble fonctionner dans la locale source mais échoue dès qu’une autre langue ou écriture est activée.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
key = "item.one" if count == 1 else "item.other"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le code suppose deux catégories et mélange logique de locale et gameplay.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
key = &"inventory.item_count"
quantity = count
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La quantité reste numérique et la locale choisit la catégorie appropriée.


### 42.4 Stocker une date déjà formatée

**Symptôme :** Le produit semble fonctionner dans la locale source mais échoue dès qu’une autre langue ou écriture est activée.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
saved_at = "27/07/2026 17:35"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La chaîne perd le fuseau, l’instant et la possibilité d’un autre rendu.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
saved_at_utc = "2026-07-27T15:35:00Z"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** L’instant canonique peut être rendu selon locale et fuseau.


### 42.5 Afficher un prix concaténé

**Symptôme :** Le produit semble fonctionner dans la locale source mais échoue dès qu’une autre langue ou écriture est activée.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
label.text = str(price) + " €"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le séparateur, l’espace et la position du symbole sont figés.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
label.text = money_formatter.format_decimal(price, "EUR", locale)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Montant, devise et locale sont transmis séparément à un formateur qualifié.


### 42.6 Inverser toute l’interface RTL

**Symptôme :** Le produit semble fonctionner dans la locale source mais échoue dès qu’une autre langue ou écriture est activée.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
node.scale.x = -1
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le miroir géométrique inverse aussi textes, logos et contenus non directionnels.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
apply_layout_direction(Control.LAYOUT_DIRECTION_RTL)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La direction de mise en page est appliquée sans déformer les éléments.


### 42.7 Accepter un fallback système implicite

**Symptôme :** Le produit semble fonctionner dans la locale source mais échoue dès qu’une autre langue ou écriture est activée.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
theme.default_font = null
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le rendu dépend de la machine et peut masquer des glyphes manquants.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
theme.default_font = qualified_font_stack
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** La pile de polices est explicite, versionnée et testable.


### 42.8 Pseudo-localiser les variables

**Symptôme :** Le produit semble fonctionner dans la locale source mais échoue dès qu’une autre langue ou écriture est activée.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
text = text.replace("a", "á")
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Les noms de variables et balises peuvent être corrompus.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
text = transform_only_natural_language(tokens)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Les tokens protégés sont extraits, vérifiés et restaurés.


### 42.9 Déclarer une langue supportée après traduction

**Symptôme :** Le produit semble fonctionner dans la locale source mais échoue dès qu’une autre langue ou écriture est activée.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
status = "supported"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** La traduction seule ne prouve ni polices, UI, accessibilité ni build.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
status = "in_context_review_pending"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le statut nomme la porte réellement atteinte.


### 42.10 Envoyer tout le scénario à un service distant

**Symptôme :** Le produit semble fonctionner dans la locale source mais échoue dès qu’une autre langue ou écriture est activée.

**Exemple fautif :**

> **[LECTURE] Contre-exemple à étudier — Ne pas saisir.**

```text
upload(project_dialogues, api_token)
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** Le corpus, les secrets et les contenus non publiés sont exposés sans gouvernance.

**Exemple corrigé :**

> **[LECTURE] Correction conceptuelle — Adapter au contrat retenu.**

```text
upload(approved_minimized_batch, scoped_credential)
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** Le lot est minimisé, approuvé et utilise un credential limité.


## 43. Checklist Solo

- [ ] définir locales source, candidates et de repli ;
- [ ] adopter une convention de clés stables ;
- [ ] externaliser chaque texte visible et chaque contenu dynamique ;
- [ ] documenter variables, pluriels, genres et contraintes ;
- [ ] qualifier polices, écritures et directions ;
- [ ] exécuter pseudo-localisation longue et bidirectionnelle ;
- [ ] contrôler débordements, focus, sous-titres et accessibilité ;
- [ ] obtenir une relecture linguistique indépendante ;
- [ ] valider les scènes représentatives en contexte ;
- [ ] conserver rapport, réserves et décision de publication.


## 44. Checklist Studio

- [ ] nommer propriétaires source, technique, linguistique, QA, juridique et release ;
- [ ] versionner catalogue, glossaire, mémoire et guide de style ;
- [ ] automatiser extraction, couverture, variables, pluriels et clés orphelines ;
- [ ] gérer statuts, retours, invalidations et gel de source ;
- [ ] protéger secrets, corpus et droits des fournisseurs ;
- [ ] qualifier outils, polices, scripts et plateformes ;
- [ ] corréler captures, rapports et approbations au build ;
- [ ] séparer validation linguistique, en contexte, accessibilité et publication ;
- [ ] prévoir capacité de correction et support après lancement ;
- [ ] archiver sources, dérivés, rapports et décisions.


## 45. Critères d’acceptation documentaire

Le chapitre passe au niveau documentaire lorsque le périmètre du plan maître est couvert, les frontières sont explicites,
les clés et formats sont expliqués, les dix diagnostics sont complets, les repères d’utilisation sont cohérents, les
doublons sont absents et les réserves runtime sont visibles.

Le niveau `runtime-tested` exigerait au minimum un catalogue matérialisé, plusieurs locales intégrées, pseudo-localisation,
tests de débordement, écritures non latines, polices qualifiées, validation linguistique et en contexte, rapports conservés
et corrélation à un build précis. Ces preuves ne sont pas produites ici.


## 46. Références techniques officielles

- [Internationalizing games — documentation Godot](https://docs.godotengine.org/en/latest/tutorials/i18n/internationalizing_games.html)
- [Locales — documentation Godot](https://docs.godotengine.org/en/latest/tutorials/i18n/locales.html)
- [Using gettext — documentation Godot](https://docs.godotengine.org/en/latest/tutorials/i18n/localization_using_gettext.html)
- [TranslationServer — documentation Godot](https://docs.godotengine.org/en/latest/classes/class_translationserver.html)
- [Internationalizing games — examples and CSV](https://docs.godotengine.org/en/latest/tutorials/i18n/localization_using_spreadsheets.html)
- [Unicode Bidirectional Algorithm — Unicode Standard Annex #9](https://www.unicode.org/reports/tr9/)
- [Unicode Locale Data Markup Language](https://unicode.org/reports/tr35/)
- [CLDR — Unicode Common Locale Data Repository](https://cldr.unicode.org/)
- [BCP 47 — Tags for Identifying Languages](https://www.rfc-editor.org/rfc/rfc5646)


## 47. Synthèse opérationnelle pour `Project Asteria`

`Project Asteria` retient `fr-FR` comme locale source documentaire et n’annonce aucune autre locale comme supportée avant
qualification complète. Les textes visibles utilisent des clés stables hiérarchiques ; les sauvegardes et le domaine
conservent identifiants et valeurs, jamais les traductions résolues.

Les contrats séparent langue de texte, langue audio, région de format, écriture et direction. Les nombres, dates, montants
et unités restent structurés jusqu’au rendu. Les variables sont nommées, les pluriels appartiennent aux règles de locale,
les polices utilisent des piles explicites et les interfaces sont testées par pseudo-localisation longue et bidirectionnelle.

Le catalogue, le glossaire, les statuts, les rapports et les captures sont versionnés. Traduction, relecture linguistique,
validation en contexte, accessibilité, conformité spécialisée et décision de publication restent des portes distinctes.
Les outils distants ne reçoivent aucun corpus sans revue de confidentialité, droits et minimisation.

Aucun catalogue Godot, fichier PO, traduction, police, doublage, pseudo-locale exécutée, capture, test d’écriture,
relecture native, validation en contexte, build multilingue, publication réelle ou PDF du Livre IV n’est revendiqué.
