---
title: "Livre III — Chapitre 3 : Références, concept art et ComfyUI"
id: "DOC-L3-CH03"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 3
last-verified: "2026-07-22T20:42:28+02:00"
audit-status: "complete"
audit-date: "2026-07-22T20:42:28+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-03.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
reference-tools:
  comfyui:
    version: "0.28.0"
    qualification: "documentation-reviewed"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Références, concept art et ComfyUI

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH03`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** ComfyUI `0.28.0`, Godot `4.7.1-stable`, Windows 11

## 1. Rôle du chapitre

Le chapitre 2 a fixé la grammaire visuelle de `Project Asteria` : formes, silhouettes, proportions, palettes, matériaux, lumière, lisibilité, variations et procédure de dérogation. Le présent chapitre transforme cette grammaire en une **chaîne de recherche et de conception traçable**. Il explique comment chercher, enregistrer, annoter, comparer et sélectionner des références, puis comment utiliser ComfyUI pour produire des propositions reproductibles sans confondre une image persuasive avec un asset de jeu prêt à intégrer.

Le résultat attendu n’est pas un dossier rempli d’images. Il s’agit d’un système où chaque image retenue répond à une question, possède une provenance, un contexte d’usage, un statut juridique documenté, une relation explicite avec la bible visuelle et une décision humaine enregistrée.

ComfyUI intervient comme outil de génération et d’itération. Son graphe peut être enregistré en JSON et les images compatibles peuvent conserver le workflow dans leurs métadonnées. Cette capacité facilite la reprise, mais elle ne suffit pas à prouver les droits du modèle, des références, des custom nodes, des entrées ou des sorties. La traçabilité juridique et éditoriale reste un contrat du projet.

> **[LECTURE] Chaîne de transformation — Ne pas saisir.**



```text

Besoin de conception
    ↓
Question visuelle précise
    ↓
Références sourcées et annotées
    ↓
Règles extraites de la bible visuelle
    ↓
Workflow ComfyUI versionné
    ↓
Famille de propositions reproductibles
    ↓
Critique anatomique, matérielle, culturelle et fonctionnelle
    ↓
Sélection ou rejet humain documenté
    ↓
Dossier de concept consolidé
    ↓
Décisions de modélisation, jamais asset final automatique

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** La chaîne place la question de conception et la provenance avant la génération, puis impose une revue humaine avant toute décision de production.

- **Déroulement :** Chaque étape produit une information consommée par la suivante ; une image ne passe pas directement de la génération à la modélisation.

- **Invariant :** La conformité à la bible, la provenance et le statut d’usage doivent rester vérifiables même lorsque le workflow est réexécuté plusieurs mois plus tard.

- **Résultat attendu :** Un concept retenu peut être expliqué, reproduit approximativement et relié à des décisions de forme, de matière et de fonction.

## 2. Portée, niveau de preuve et réserves

Ce chapitre est accepté au niveau `static-review`. Il documente une organisation cible, des formats de manifestes, des commandes de contrôle et des procédures de revue. Il ne prétend pas qu’un environnement ComfyUI a été installé, qu’un modèle a été téléchargé, qu’un workflow a été exécuté, qu’une image a été générée ou qu’un droit d’exploitation a été validé par un juriste.

La version qualifiée pour la documentation est ComfyUI `0.28.0`, dernière version stable observée le 22 juillet 2026. La version du logiciel ne détermine pas celle des modèles, du front-end, des templates ou des custom nodes ; chacun possède son propre cycle et doit être enregistré séparément.

La machine de référence possède une Radeon RX 6750 XT, architecture RDNA2. La documentation officielle actuelle décrit l’accélération AMD Windows expérimentale pour des générations RDNA plus récentes et ne permet pas de qualifier cette carte sous Windows. Le chapitre n’invente donc aucun temps de génération, aucun niveau de mémoire disponible et aucune procédure accélérée garantie. Une exécution CPU ou une solution communautaire peut être explorée dans un environnement isolé, mais ne devient pas une référence de production sans test et décision documentés.

## 3. Distinguer inspiration, référence, concept, source et asset final

Ces cinq catégories ne sont pas interchangeables :

- une **inspiration** oriente une intention générale sans être nécessairement copiée dans le dossier de production ;
- une **référence** répond à une question observable : assemblage, proportion, matériau, mécanisme, climat, geste, vêtement ou organisation spatiale ;
- un **concept** combine et transforme des décisions pour explorer une solution propre au projet ;
- une **source de production** est un fichier modifiable utilisé pour fabriquer l’asset : dessin en calques, fichier Blender, texture source, masque ou document vectoriel ;
- un **asset final** est une ressource validée, versionnée, budgétée, importée et utilisable dans le jeu selon ses droits.

Une même image peut changer de statut au cours du projet, mais le changement doit être explicite. Une capture trouvée sur le Web ne devient pas une source de production parce qu’elle a été redimensionnée. Une sortie ComfyUI ne devient pas un concept retenu parce qu’elle paraît spectaculaire. Un concept retenu ne devient pas un asset final parce qu’il ressemble à un rendu 3D.

> **[VSC] Visual Studio Code — Créer : `docs/art/concepts/CONCEPT-STATUS.yaml` — Ne pas saisir.**



```yaml

status_definitions:
  inspiration:
    decision_authority: false
    redistribution_default: false
  reference:
    question_required: true
    provenance_required: true
  generated_proposal:
    workflow_required: true
    human_selection_required: true
  selected_concept:
    review_report_required: true
    production_ready: false
  production_source:
    editable_source_required: true
    rights_cleared: true
  final_asset:
    godot_validation_required: true
    budget_validation_required: true

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** Le fichier définit les portes minimales permettant de faire évoluer une image d’un statut exploratoire vers un statut de production.

- **Champs et types :** Chaque statut mappe des booléens ou exigences lisibles ; `decision_authority: false` interdit d’utiliser une inspiration comme décision autoritaire.

- **Effet de bord :** Changer un statut crée des obligations supplémentaires, notamment un rapport de revue, une source modifiable ou une validation dans Godot.

- **Invariant :** Aucun statut généré ou sélectionné ne possède implicitement les droits, la qualité technique ou le budget d’un asset final.

- **Résultat attendu :** Les dossiers, tableaux et revues utilisent un vocabulaire commun et évitent les promotions silencieuses.

## 4. Livrables cibles et arborescence

L’organisation doit séparer les éléments reçus, les documents internes, les workflows, les sorties dérivées et les décisions. Les images externes non redistribuables ne doivent pas être placées dans un dépôt public. Le registre peut conserver leur URL, leur empreinte locale et leurs annotations sans publier le fichier lui-même.

Les chemins suivants décrivent la cible de `Project Asteria` :

- `docs/art/references/REFERENCE-REGISTER.yaml` : registre de provenance et d’usage ;
- `docs/art/references/questions/` : questions visuelles et critères ;
- `docs/art/moodboards/` : moodboards annotés et manifestes ;
- `docs/art/concepts/CONCEPT-REGISTER.yaml` : propositions et décisions ;
- `docs/art/concepts/reviews/` : rapports de sélection ;
- `workflows/comfyui/` : graphes JSON versionnés ;
- `workflows/comfyui/manifests/` : modèles, nœuds, versions et licences ;
- `inputs/reference-images/` : entrées autorisées, hors dépôt public si nécessaire ;
- `outputs/comfyui/quarantine/` : sorties non revues ;
- `outputs/comfyui/selected/` : sorties retenues comme concepts, jamais comme assets finaux ;
- `outputs/comfyui/rejected/` : exemples rejetés utiles à la critique ;
- `hashes/` : empreintes des fichiers significatifs.

> **[LECTURE] Arborescence de travail — Ne pas saisir.**



```text

ProjectAsteria/
├── docs/
│   └── art/
│       ├── references/
│       │   ├── REFERENCE-REGISTER.yaml
│       │   └── questions/
│       ├── moodboards/
│       └── concepts/
│           ├── CONCEPT-REGISTER.yaml
│           └── reviews/
├── workflows/
│   └── comfyui/
│       ├── concept-environment-v001.json
│       └── manifests/
├── inputs/
│   └── reference-images/
├── outputs/
│   └── comfyui/
│       ├── quarantine/
│       ├── selected/
│       └── rejected/
└── hashes/

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** L’arbre sépare les décisions versionnées des fichiers reçus et des sorties non validées.

- **Dépendances :** Les registres sous `docs/` référencent les fichiers par identifiant et empreinte plutôt que par position implicite.

- **Sécurité :** Le dossier `quarantine` évite qu’une sortie nouvelle soit confondue avec une sélection approuvée.

- **Frontière :** Aucun chemin ne place directement une image ComfyUI dans les textures, modèles ou ressources importables par Godot.

- **Résultat attendu :** Une personne peut localiser la source d’une décision sans parcourir un dossier unique rempli de variantes.

## 5. Formuler une question visuelle avant de chercher

Une recherche utile commence par une question limitée. « Trouver des idées de ville » est trop vaste. « Comment signaler une réparation récente sur une maçonnerie ancienne sans employer une couleur saturée ? » produit des critères observables et permet de rejeter les images hors sujet.

Chaque question doit préciser :

- l’identifiant du besoin ou de l’asset concerné ;
- la décision attendue ;
- les dimensions à observer ;
- les dimensions à ignorer ;
- les contraintes de la bible visuelle ;
- le niveau de priorité ;
- la personne qui clôt la recherche ;
- la condition d’arrêt.

La condition d’arrêt protège contre la collecte infinie. Elle peut être quantitative, par exemple douze références qualifiées, et qualitative, par exemple trois mécanismes distincts suffisamment documentés.

> **[VSC] Visual Studio Code — Créer : `docs/art/references/questions/REFQ-ARCH-REPAIR-001.yaml` — Ne pas saisir.**



```yaml

id: "REFQ-ARCH-REPAIR-001"
asset_scope:
  - "AST-BLD-RUIN-001"
decision: "rendre lisible une réparation récente sur une structure ancienne"
observe:
  - "liaison entre matériaux d'âges différents"
  - "traces d'outils et fixations"
  - "zones de charge"
ignore:
  - "style photographique"
  - "mobilier environnant"
bible_rules:
  - "pillar.traces_and_repair"
  - "material.wear.causal"
priority: 80
owner: "art-direction-owner"
stop_condition:
  qualified_references: 12
  distinct_mechanisms: 3
status: "open"

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** La fiche transforme une recherche vague en décision bornée reliée à un asset et à deux règles de la bible.

- **Champs et types :** `observe` et `ignore` sont des listes ; `stop_condition` combine un nombre de références et une diversité minimale.

- **Déroulement :** Le propriétaire clôt la question lorsque les deux conditions sont satisfaites ou lorsqu’une décision de changement est enregistrée.

- **Invariant :** Une image intéressante mais étrangère aux dimensions observées ne doit pas entrer dans la sélection principale.

- **Résultat attendu :** Le moodboard ultérieur répond à une question vérifiable au lieu d’accumuler des préférences.

## 6. Construire le registre de provenance

Le registre doit exister avant le moodboard. Il ne constitue pas un avis juridique ; il empêche surtout l’oubli des informations nécessaires à une décision éclairée.

Pour chaque référence, enregistrer au minimum :

- identifiant stable ;
- titre descriptif interne ;
- type de source ;
- auteur, organisme ou fournisseur ;
- URL ou emplacement ;
- date et heure d’accès lorsque la source est en ligne ;
- licence, conditions contractuelles ou statut inconnu ;
- usages envisagés ;
- restrictions ;
- présence éventuelle de personnes, marques, œuvres, données personnelles ou informations sensibles ;
- fichier local et empreinte si une copie autorisée est conservée ;
- question visuelle servie ;
- statut de revue.

Une licence du site, une licence du modèle et une licence de l’image sont trois choses différentes. L’absence d’information ne signifie pas domaine public. Le statut `unknown` doit bloquer la redistribution et toute transformation destinée à la production jusqu’à résolution.

> **[VSC] Visual Studio Code — Créer : `docs/art/references/REFERENCE-REGISTER.yaml` — Ne pas saisir.**



```yaml

schema_version: 1
references:
  - id: "REF-ARCH-REPAIR-0001"
    question_id: "REFQ-ARCH-REPAIR-001"
    title: "liaison métallique sur maçonnerie réparée"
    source_type: "web_page"
    author: null
    provider: null
    url: null
    accessed_at: null
    license:
      identifier: "unknown"
      evidence_path: null
    intended_uses:
      - "internal_visual_analysis"
    restrictions:
      - "no_redistribution"
      - "no_generation_input"
    sensitive_elements: []
    local_file:
      path: null
      sha256: null
    annotation_status: "pending"
    rights_status: "blocked"

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** L’entrée montre une référence volontairement bloquée tant que l’auteur, la source et les droits ne sont pas documentés.

- **Valeurs nulles :** Les `null` sont des absences à résoudre, pas des valeurs par défaut autorisant l’usage.

- **Restrictions :** `no_generation_input` distingue la consultation visuelle d’un emploi comme condition d’un modèle génératif.

- **Traçabilité :** L’empreinte SHA-256 identifie une copie locale autorisée mais ne prouve ni l’auteur ni la licence.

- **Résultat attendu :** La référence peut être discutée en interne sans être publiée ni injectée dans un workflow avant qualification.

## 7. Définir le contexte d’usage

Une référence peut être autorisée pour un usage et interdite pour un autre. Le projet doit distinguer au moins :

- consultation interne ;
- inclusion dans un moodboard interne ;
- inclusion dans une documentation distribuée ;
- utilisation comme entrée image d’un modèle ;
- transformation ou adaptation ;
- entraînement ou ajustement d’un modèle ;
- intégration directe dans un asset ;
- communication publique ou marketing.

Le registre conserve l’usage prévu, pas seulement la licence nominale. Une licence ouverte peut imposer attribution, partage dans les mêmes conditions, interdiction commerciale ou absence de modification. Une autorisation contractuelle peut être limitée à une équipe, une durée ou un territoire. Toute ambiguïté doit être remontée à la personne responsable des droits.

> **[LECTURE] Matrice de décision des usages — Ne pas saisir.**



```yaml

usage_matrix:
  internal_analysis:
    requires_known_source: true
    requires_redistribution_right: false
  distributed_moodboard:
    requires_known_source: true
    requires_redistribution_right: true
    attribution_record_required: true
  generation_input:
    requires_known_source: true
    explicit_input_permission_required: true
  production_integration:
    direct_copy_allowed: false
    separate_clearance_required: true
  model_training:
    covered_by_this_chapter: false
    explicit_project_decision_required: true

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** La matrice empêche d’étendre automatiquement un droit de consultation à la redistribution ou à l’utilisation comme entrée générative.

- **Conditions :** Les booléens expriment des portes documentaires ; ils ne remplacent pas la lecture des conditions applicables.

- **Frontière :** L’entraînement de modèles reste hors du périmètre opérationnel et exige une décision spécifique.

- **Invariant :** La copie directe d’une référence dans un asset n’est jamais autorisée par le seul fait qu’elle a servi au moodboard.

- **Résultat attendu :** Le réviseur peut expliquer pourquoi une référence reste interne ou pourquoi elle est exclue du workflow.

## 8. Recevoir et mettre en quarantaine les fichiers externes

Les fichiers reçus par téléchargement, messagerie ou partage doivent être traités comme non fiables. Avant ouverture :

1. conserver le nom original dans le registre ;
2. calculer une empreinte ;
3. vérifier le type réel du fichier ;
4. analyser le fichier avec les protections disponibles ;
5. retirer les métadonnées sensibles seulement sur une copie dérivée ;
6. conserver l’original autorisé dans un emplacement à accès limité ;
7. créer une miniature de travail si les droits le permettent ;
8. ne jamais exécuter un fichier présenté comme image mais contenant du code ou une archive inattendue.

Les documents provenant d’une autre personne peuvent contenir des informations personnelles dans leurs métadonnées. Le nettoyage doit être documenté et ne doit pas détruire l’original lorsque celui-ci constitue la preuve de provenance.

> **[PS] PowerShell 7 — Exécuter depuis la racine du workspace : calculer l’empreinte d’une référence — Saisir.**



```powershell

$Path = "inputs/reference-images/REF-ARCH-REPAIR-0001.png"
if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
    throw "Fichier introuvable : $Path"
}

$Item = Get-Item -LiteralPath $Path
$Hash = Get-FileHash -LiteralPath $Path -Algorithm SHA256

[pscustomobject]@{
    Path = $Item.FullName
    Bytes = $Item.Length
    Sha256 = $Hash.Hash.ToLowerInvariant()
}

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** La commande vérifie l’existence du fichier, lit sa taille et calcule une empreinte SHA-256 destinée au registre.

- **Paramètres :** `-LiteralPath` évite d’interpréter des caractères du nom comme jokers ; `-Algorithm SHA256` fixe l’algorithme.

- **Retours :** La sortie contient le chemin absolu, le nombre d’octets et l’empreinte en minuscules.

- **Erreur :** L’absence du fichier arrête la commande au lieu d’enregistrer une empreinte vide.

- **Limite :** L’empreinte détecte un changement d’octets mais ne valide pas la sécurité, l’auteur ou les droits.

## 9. Organiser un moodboard comme document argumenté

Un moodboard utile ne se contente pas d’aligner des images. Il doit relier chaque zone à une question, une annotation et une conclusion provisoire. Les images non retenues peuvent rester dans le registre, mais le moodboard principal doit être limité aux références qui apportent une information distincte.

Pour chaque vignette, préciser :

- identifiant de référence ;
- détail observé ;
- relation avec une règle de la bible ;
- élément à conserver ;
- élément à ne pas reproduire ;
- échelle ou distance pertinente ;
- niveau de confiance ;
- statut des droits ;
- décision issue de la comparaison.

Un moodboard peut contenir des contradictions volontaires. Elles doivent être nommées : deux solutions de fermeture, deux rapports de proportions ou deux niveaux d’usure. La comparaison doit produire une décision ou une expérimentation, pas une moyenne visuelle implicite.

> **[VSC] Visual Studio Code — Créer : `docs/art/moodboards/MB-ARCH-REPAIR-001.yaml` — Ne pas saisir.**



```yaml

id: "MB-ARCH-REPAIR-001"
question_id: "REFQ-ARCH-REPAIR-001"
bible_version: "1.0.0"
entries:
  - reference_id: "REF-ARCH-REPAIR-0007"
    observe: "plaque de renfort suit les lignes de charge"
    keep: "fixations lisibles à moyenne distance"
    reject: "ornement central sans fonction"
    confidence: "medium"
  - reference_id: "REF-ARCH-REPAIR-0011"
    observe: "mortier récent distingue la réparation par texture"
    keep: "différence de rugosité"
    reject: "contraste coloré excessif"
    confidence: "high"
decision:
  rule: "associer renfort structurel et différence de rugosité"
  status: "candidate"
  requires_concept_test: true

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** Le manifeste relie deux références à une question et extrait une règle candidate à tester.

- **Comparaison :** Les champs `keep` et `reject` évitent de copier une image entière et isolent les propriétés pertinentes.

- **Dépendance :** `bible_version` indique quelle version des règles a guidé la sélection.

- **Effet de bord :** La décision crée une expérimentation de concept mais ne modifie pas encore la bible.

- **Résultat attendu :** Le concept art peut tester une combinaison explicitement argumentée.

## 10. Créer une planche de comparaison lisible

Une planche doit préserver l’identifiant des références et ne pas recadrer au point de supprimer le contexte nécessaire. Les légendes doivent rester lisibles sans ouvrir un fichier annexe. Les zones examinées peuvent être encadrées, mais les annotations ne doivent pas masquer l’information.

Pour les références dont la redistribution n’est pas autorisée, produire une version interne à accès contrôlé et une version distribuable contenant seulement les identifiants, les descriptions, les décisions et, si nécessaire, des schémas originaux créés pour expliquer les principes.

La planche n’est pas la source de vérité juridique. Elle cite le registre. Si une référence est retirée ou ses conditions changent, le manifeste du moodboard doit permettre de retrouver toutes les planches concernées.

## 11. Qualifier ComfyUI et figer le contexte d’exécution

ComfyUI est un moteur et une interface à graphes. Un workflow relie des nœuds qui chargent des modèles, encodent des conditions, échantillonnent, décodent et enregistrent des sorties. La version `0.28.0` est retenue comme référence documentaire du chapitre.

Le projet doit enregistrer séparément :

- version ou commit de ComfyUI ;
- version du front-end si elle est exposée ;
- version du Manager ;
- version de chaque custom node ;
- version et empreinte de chaque modèle ;
- version de Python ;
- version de PyTorch et backend matériel ;
- système d’exploitation ;
- arguments de lancement ;
- chemins de modèles externes ;
- état d’exécution : non testé, démarré, workflow chargé, génération réussie ou qualifié.

Une mise à jour ne doit pas écraser silencieusement l’environnement qualifié. L’environnement de recherche peut évoluer ; l’environnement utilisé pour reproduire une sélection doit rester reconstruisible.

> **[VSC] Visual Studio Code — Créer : `workflows/comfyui/manifests/ENVIRONMENT.yaml` — Ne pas saisir.**



```yaml

schema_version: 1
comfyui:
  version: "0.28.0"
  commit: null
  license: "GPL-3.0-or-later"
frontend:
  version: null
manager:
  version: null
python:
  version: null
pytorch:
  version: null
  backend: "not_qualified"
platform:
  os: "Windows 11"
  gpu: "AMD Radeon RX 6750 XT 12 GB"
  acceleration_status: "not_qualified_for_reference_gpu_on_windows"
launch:
  command: null
  arguments: []
validation:
  runtime_executed: false
  workflow_loaded: false
  generation_completed: false

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** Le manifeste distingue la version documentaire de ComfyUI des composants et paramètres qui restent à mesurer sur la machine réelle.

- **Valeurs nulles :** Les versions inconnues ne sont pas inventées ; elles doivent être renseignées depuis l’environnement exécuté.

- **Backend :** `not_qualified` indique que la présence d’une carte AMD ne constitue pas une preuve d’accélération compatible.

- **État :** Les trois booléens de validation empêchent de confondre lecture documentaire, démarrage de l’outil et génération réussie.

- **Résultat attendu :** Une future exécution peut compléter le manifeste sans réécrire l’historique de la qualification initiale.

## 12. Séparer environnement de recherche et environnement qualifié

L’environnement de recherche sert à essayer de nouveaux modèles ou nœuds. L’environnement qualifié sert à reproduire les concepts retenus. Les deux ne doivent pas partager des mises à jour automatiques incontrôlées.

En Mode Solo, deux dossiers ou deux environnements virtuels suffisent. En Mode Studio, employer des manifestes verrouillés et une procédure de promotion. Une extension testée en recherche ne passe en environnement qualifié qu’après :

- vérification de la source ;
- revue de la licence ;
- épinglage d’une version ou d’un commit ;
- lecture des dépendances ;
- test dans un environnement isolé ;
- reproduction d’un workflow témoin ;
- décision de promotion ;
- plan de retour arrière.

Les modèles téléchargés doivent être considérés comme des dépendances volumineuses et juridiquement distinctes. Un modèle portant le même nom sur deux sites peut avoir des octets, conditions ou auteurs différents.

> **[LECTURE] Profils d’environnement — Ne pas saisir.**



```yaml

profiles:
  research:
    updates: "manual_after_review"
    custom_nodes: "experimental_allowed"
    outputs: "quarantine_only"
    reproducibility_target: "best_effort"
  qualified:
    updates: "blocked_without_change_request"
    custom_nodes: "pinned_only"
    outputs: "eligible_for_human_selection"
    reproducibility_target: "documented_family"
promotion_gate:
  requires:
    - "source_review"
    - "license_review"
    - "version_pin"
    - "dependency_review"
    - "workflow_smoke_test"
    - "rollback_plan"

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** Les profils limitent l’impact des expérimentations sur les workflows qui soutiennent des décisions déjà approuvées.

- **Promotion :** La liste `requires` décrit les preuves minimales avant de déplacer un composant vers l’environnement qualifié.

- **Sorties :** Les résultats de recherche restent en quarantaine ; seuls les résultats d’un environnement qualifié peuvent entrer dans une revue de sélection.

- **Invariant :** Une mise à jour utile ne modifie pas rétroactivement la définition d’un workflow retenu.

- **Résultat attendu :** Le projet peut explorer sans perdre la capacité de reproduire les familles de concepts sélectionnées.

## 13. Commencer par les nœuds Core

Les templates officiels utilisant les nœuds Core réduisent les dépendances et constituent un meilleur point de départ pédagogique. Ajouter un custom node seulement lorsqu’une exigence précise ne peut pas être satisfaite raisonnablement avec les nœuds Core.

Un custom node est du code exécuté par le processus ComfyUI. Il peut installer des dépendances, lire des fichiers ou communiquer avec le réseau selon son implémentation. Il faut donc examiner sa source, sa licence, sa maintenance, ses dépendances et son comportement. Un workflow JSON provenant d’un tiers peut référencer des nœuds absents ou dangereux ; il ne doit pas provoquer une installation automatique non revue.

Pour un premier workflow de concept, limiter le graphe à :

- chargeur de checkpoint ;
- encodeurs de texte ;
- latent initial ;
- échantillonneur ;
- décodeur VAE ;
- enregistrement d’image ;
- éventuellement une entrée image autorisée et des nœuds Core de conditionnement.

## 14. Enregistrer le workflow JSON comme source canonique

ComfyUI peut conserver un workflow dans les métadonnées d’une image et dans un fichier JSON lisible. Le fichier JSON versionné doit rester la source canonique du graphe ; l’image est une sortie dérivée qui peut perdre ses métadonnées lors d’une conversion, d’un envoi ou d’une optimisation.

Après chaque changement significatif :

1. enregistrer le workflow JSON ;
2. incrémenter sa version ;
3. mettre à jour le manifeste de modèles et de nœuds ;
4. exécuter un test lorsque l’environnement est disponible ;
5. enregistrer les paramètres de la sélection ;
6. calculer l’empreinte du JSON ;
7. ne pas modifier manuellement les identifiants internes sans comprendre le schéma.

Le workflow JSON peut contenir des chemins, noms de modèles, textes ou métadonnées sensibles. Il doit être relu avant publication.

> **[VSC] Visual Studio Code — Créer : `workflows/comfyui/manifests/WF-CONCEPT-ENV-001.yaml` — Ne pas saisir.**



```yaml

id: "WF-CONCEPT-ENV-001"
workflow_file: "../concept-environment-v001.json"
workflow_sha256: null
comfyui_version: "0.28.0"
purpose: "explorer la silhouette d'un poste de veille Asteria"
source_question_ids:
  - "REFQ-ARCH-WATCHPOST-001"
bible_rules:
  - "shape.civilization.angular"
  - "silhouette.medium_distance"
models:
  - "MODEL-CHECKPOINT-001"
custom_nodes: []
inputs:
  reference_images: []
outputs:
  directory: "../../../outputs/comfyui/quarantine/WF-CONCEPT-ENV-001/"
execution:
  status: "not_executed"
  run_ids: []

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** Le manifeste relie le graphe à son but, aux questions de référence, aux règles de la bible et aux dépendances.

- **Empreinte :** `workflow_sha256` sera calculé sur le fichier JSON réellement enregistré ; il reste nul tant que le fichier n’existe pas.

- **Dépendances :** Les modèles sont référencés par identifiant de manifeste et la liste vide de custom nodes prouve l’intention de commencer avec le cœur.

- **Sortie :** Le répertoire cible reste en quarantaine jusqu’à la revue humaine.

- **Résultat attendu :** Une personne sait quel graphe reproduire et pourquoi il existe sans ouvrir d’abord ComfyUI.

## 15. Manifester les modèles et leurs droits

Le nom du fichier ne suffit pas à identifier un modèle. Le manifeste doit enregistrer :

- identifiant interne ;
- nom exact du fichier ;
- famille et rôle ;
- fournisseur et dépôt ;
- version ou révision ;
- empreinte ;
- taille ;
- page de licence ;
- identifiant de licence lorsque disponible ;
- restrictions d’usage ;
- date d’accès ;
- approbateur ;
- statut de qualification.

Les composants secondaires comptent aussi : VAE, encodeur de texte, ControlNet, LoRA, upscaler, modèle de détection ou modèle de profondeur. La licence de ComfyUI ne couvre pas automatiquement ces fichiers.

> **[VSC] Visual Studio Code — Créer : `workflows/comfyui/manifests/MODELS.yaml` — Ne pas saisir.**



```yaml

schema_version: 1
models:
  - id: "MODEL-CHECKPOINT-001"
    role: "checkpoint"
    filename: null
    provider: null
    repository: null
    revision: null
    sha256: null
    bytes: null
    license:
      identifier: "unknown"
      source_url: null
      evidence_path: null
    restrictions: []
    accessed_at: null
    approved_by: null
    qualification_status: "blocked_until_documented"

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** Le manifeste refuse de préremplir un modèle qui n’a pas encore été sélectionné et téléchargé.

- **Identité :** La combinaison fournisseur, dépôt, révision, nom de fichier, taille et empreinte distinguera deux fichiers portant un nom similaire.

- **Droits :** La licence possède sa propre source et une preuve archivable ; une simple étiquette saisie à la main est insuffisante.

- **Porte :** `blocked_until_documented` interdit d’utiliser le modèle dans un workflow qualifié.

- **Résultat attendu :** Le projet peut remplacer ou retirer un modèle en retrouvant tous les workflows concernés.

## 16. Manifester et épingler les custom nodes

Le registre officiel des nœuds améliore la découverte et applique des contrôles, mais il ne remplace pas la revue du projet. Pour chaque extension :

- enregistrer le dépôt canonique ;
- épingler une version immuable ou un commit ;
- enregistrer la licence ;
- lire le fichier de dépendances ;
- vérifier les téléchargements de modèles ou exécutables ;
- rechercher les appels système et communications réseau ;
- noter les répertoires lus et écrits ;
- vérifier la compatibilité avec la version de ComfyUI ;
- tester la désactivation ;
- conserver un workflow témoin ;
- documenter le remplacement par des nœuds Core lorsque possible.

Ne jamais installer automatiquement les nœuds manquants d’un workflow reçu. La documentation officielle rappelle que les custom nodes peuvent être malveillants et recommande de n’utiliser que des sources de confiance après examen.

> **[VSC] Visual Studio Code — Créer : `workflows/comfyui/manifests/CUSTOM-NODES.yaml` — Ne pas saisir.**



```yaml

schema_version: 1
custom_nodes:
  - id: "NODEPACK-EXAMPLE-001"
    repository: null
    commit: null
    package_version: null
    license:
      identifier: "unknown"
      source_url: null
    dependency_file_sha256: null
    network_access: "unknown"
    subprocess_usage: "unknown"
    writes_outside_workspace: "unknown"
    reviewed_by: null
    tested_with:
      comfyui_version: "0.28.0"
      workflow_id: null
    status: "not_approved"

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** La structure rend visibles les comportements qui peuvent introduire un risque de chaîne d’approvisionnement.

- **Version :** Le commit ou la version doit être immuable afin qu’une mise à jour amont ne change pas silencieusement le workflow.

- **Sécurité :** Les champs réseau, processus et écritures restent `unknown` jusqu’à lecture et test ; l’inconnu n’est pas assimilé à l’absence.

- **Compatibilité :** La version de ComfyUI et le workflow témoin lient l’approbation à un contexte concret.

- **Résultat attendu :** Une extension ne peut pas être promue sur la seule base de sa popularité ou d’une installation réussie.

## 17. Gérer les seeds et la reproductibilité réelle

Une seed fixe ne garantit pas une image identique dans tous les environnements. Le résultat dépend aussi du modèle exact, du VAE, du sampler, du scheduler, du nombre d’étapes, du CFG, des dimensions, des entrées, des nœuds, des versions logicielles, du backend matériel et parfois d’optimisations non déterministes.

Le contrat du chapitre vise deux niveaux :

- **reproduction exacte** : mêmes octets attendus dans un environnement qualifié, seulement si cela a été démontré ;
- **reproduction de famille** : variations visuellement comparables obtenues avec le même graphe et les paramètres enregistrés.

Par défaut, déclarer une reproduction de famille. Une promesse d’identité binaire exige un test et une preuve spécifiques.

> **[VSC] Visual Studio Code — Créer : `workflows/comfyui/manifests/RUN-WF-CONCEPT-ENV-001-0001.yaml` — Ne pas saisir.**



```yaml

run_id: "RUN-WF-CONCEPT-ENV-001-0001"
workflow_id: "WF-CONCEPT-ENV-001"
workflow_sha256: null
environment_profile: "qualified"
seed: 184467440737095516
sampler: null
scheduler: null
steps: null
cfg: null
width: null
height: null
batch_size: 1
input_hashes: []
output_hashes: []
reproducibility_claim: "not_tested"
started_at: null
completed_at: null
result: "not_executed"

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** Le manifeste de run sépare les paramètres d’une exécution du workflow et de l’environnement eux-mêmes.

- **Types :** La seed est un entier ; dimensions, sampler et valeurs de diffusion restent nuls avant lecture du graphe exécuté.

- **Empreintes :** Les entrées et sorties seront liées par SHA-256 sans que l’empreinte prétende établir leurs droits.

- **Allégation :** `not_tested` empêche de revendiquer une reproductibilité seulement supposée.

- **Résultat attendu :** Une sélection peut citer l’exécution exacte qui a produit chaque image.

## 18. Écrire un contrat de prompt

Le prompt ne doit pas être un long texte opaque dont chaque modification change plusieurs intentions. Le projet peut le décomposer en champs :

- sujet et fonction ;
- silhouette ;
- proportions ;
- matériaux ;
- état et usure ;
- environnement ;
- lumière ;
- cadrage ;
- contraintes de la bible ;
- exclusions ;
- éléments non négociables ;
- éléments ouverts à variation.

Les mots de style et noms d’artistes posent des problèmes de contrôle, de cohérence et parfois de droits ou de politique interne. Préférer des propriétés observables : angle de lumière, densité de détail, construction de silhouette, type de surface, période technique ou fonction.

> **[VSC] Visual Studio Code — Créer : `docs/art/concepts/prompts/PROMPT-WATCHPOST-001.yaml` — Ne pas saisir.**



```yaml

id: "PROMPT-WATCHPOST-001"
subject:
  function: "poste de veille démontable"
  occupants: 2
shape:
  primary: "tour étroite à base triangulée"
  secondary: "passerelle suspendue courte"
materials:
  - "bois réparé"
  - "attaches métalliques récentes"
wear:
  - "contact concentré sur échelle et garde-corps"
environment:
  biome: "lisière forestière humide"
lighting:
  purpose: "lecture de silhouette"
  direction: "latérale neutre"
bible_constraints:
  - "civilisation angulaire contre végétation souple"
  - "détail groupé autour des fonctions"
exclude:
  - "ornement sans fonction"
  - "contraste saturé sur toute la structure"
variation:
  allowed:
    - "forme du toit"
    - "distribution des réparations"

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** Le prompt structuré traduit les règles de la bible en propriétés modifiables séparément.

- **Paramètres :** Les listes de contraintes et d’exclusions sont indépendantes des éléments laissés à variation.

- **Déroulement :** Une itération peut changer le toit sans altérer la fonction, la silhouette principale ou les matériaux.

- **Invariant :** Les propriétés ouvertes ne doivent pas annuler les contraintes obligatoires.

- **Résultat attendu :** Le rapport de sélection peut identifier quelle dimension explique une amélioration ou un rejet.

## 19. Ne pas traiter le prompt négatif comme une garantie

Un prompt négatif influence certains modèles et workflows, mais ne constitue pas une validation. Écrire « pas de mains déformées » ne prouve pas l’anatomie. Écrire « culturellement cohérent » ne fournit ni source ni revue. Les exclusions importantes doivent être vérifiées après génération avec une grille.

Les contraintes qui concernent la production doivent être exprimées dans le prompt structuré, le workflow et la revue. Le prompt négatif peut réduire certains artefacts connus, mais il ne remplace pas :

- une silhouette contrôlée ;
- des références anatomiques autorisées ;
- une vérification matérielle ;
- une lecture culturelle ;
- une comparaison à la bible ;
- une décision humaine.

## 20. Construire une matrice d’expériences

Changer simultanément le modèle, la seed, le sampler, le nombre d’étapes, le prompt et la référence image rend la comparaison inutilisable. Une expérimentation doit définir :

- hypothèse ;
- variable modifiée ;
- variables maintenues ;
- plage de valeurs ;
- nombre maximum de variantes ;
- critère de comparaison ;
- condition d’arrêt ;
- résultat ;
- décision.

Les sorties non sélectionnées peuvent être supprimées après conservation des paramètres et de quelques exemples utiles. L’objectif est d’apprendre, pas d’accumuler.

> **[VSC] Visual Studio Code — Créer : `docs/art/concepts/experiments/EXP-WATCHPOST-SILHOUETTE-001.yaml` — Ne pas saisir.**



```yaml

id: "EXP-WATCHPOST-SILHOUETTE-001"
workflow_id: "WF-CONCEPT-ENV-001"
hypothesis: "une base triangulée améliore la lecture à moyenne distance"
independent_variable:
  field: "shape.primary"
  values:
    - "base_rectangulaire"
    - "base_triangulee"
controlled:
  seed: 4815162342
  model_id: "MODEL-CHECKPOINT-001"
  lighting: "lateral_neutral"
  output_size: "1024x1024"
sample_count_per_value: 4
comparison_criteria:
  - "silhouette"
  - "fonction_lisible"
  - "conformite_bible"
stop_condition:
  max_outputs: 8
  minimum_clear_preference: 2
result: "not_executed"
decision: null

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** L’expérience compare une variable de forme en conservant les autres paramètres annoncés.

- **Échantillonnage :** Quatre sorties par valeur limitent la conclusion tirée d’une seule seed tout en bornant le coût.

- **Critères :** La silhouette, la fonction et la conformité sont évaluées séparément.

- **État :** Le résultat reste `not_executed` et la décision nulle tant qu’aucune planche n’a été produite.

- **Résultat attendu :** La revue peut attribuer une préférence à la variable étudiée plutôt qu’à une modification cachée.

## 21. Utiliser une image de référence comme entrée

Une image peut conditionner un workflow par image-to-image, masque, pose, profondeur, contours, segmentation ou autre représentation. Avant de l’utiliser :

- vérifier que cet usage est autorisé ;
- enregistrer l’image et son empreinte ;
- noter les transformations préalables ;
- conserver les masques et cartes dérivées ;
- enregistrer la force de conditionnement ;
- vérifier les personnes et informations sensibles ;
- éviter les images dont le statut est inconnu ;
- documenter ce qui doit être repris et ce qui doit être transformé.

Une image de référence interne ne doit pas être intégrée par inadvertance dans les métadonnées ou archives distribuées.

> **[VSC] Visual Studio Code — Ajouter à : `workflows/comfyui/manifests/RUN-WF-CONCEPT-ENV-001-0001.yaml` — Ne pas saisir.**



```yaml

reference_inputs:
  - reference_id: "REF-ARCH-WATCHPOST-0004"
    file: "../../../inputs/reference-images/REF-ARCH-WATCHPOST-0004.png"
    sha256: null
    allowed_use: "generation_input"
    preprocessing:
      - operation: "crop"
        parameters:
          x: null
          y: null
          width: null
          height: null
      - operation: "edge_map"
        tool_version: null
    conditioning:
      role: "structural_outline"
      strength: null

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** La structure relie l’entrée au registre et détaille les dérivations utilisées par le workflow.

- **Prétraitement :** Le recadrage et la carte de contours possèdent leurs paramètres afin d’éviter une transformation implicite.

- **Droits :** `allowed_use` doit correspondre à une autorisation documentée, pas à une préférence du producteur.

- **Valeurs à mesurer :** La force, les coordonnées et la version d’outil restent nulles avant exécution.

- **Résultat attendu :** Une autre personne peut reconstruire le conditionnement ou identifier pourquoi il ne doit pas être distribué.

## 22. Nommer les sorties sans dépendre du nom généré par l’outil

Le nom de sortie doit contenir un identifiant de workflow, un identifiant de run et un index. Les informations longues restent dans le manifeste. Éviter les noms contenant le prompt complet, des noms de personnes, des secrets ou des chemins locaux.

Forme recommandée :

`CONCEPT_<sujet>_<workflow>_<run>_<index>.<extension>`

Exemple : `CONCEPT_watchpost_WF-CONCEPT-ENV-001_RUN-0001_0003.png`.

Le nom n’est pas l’identité unique. L’empreinte et le registre permettent de détecter un remplacement ou une copie.

## 23. Contrôler l’anatomie et les articulations

Pour les personnages et créatures, vérifier au minimum :

- nombre et connexion des membres ;
- axes articulaires ;
- continuité du squelette ;
- répartition des masses ;
- appuis et centre de gravité ;
- amplitude plausible ;
- cohérence entre vues ;
- interaction avec vêtements et équipement ;
- silhouette à distance de jeu ;
- éléments fonctionnels nécessaires à l’animation.

Une image peut être séduisante tout en étant impossible à riguer. Les incohérences doivent être annotées sur la planche, pas seulement mentionnées oralement.

> **[VSC] Visual Studio Code — Créer : `docs/art/concepts/reviews/ANATOMY-CHECK-001.yaml` — Ne pas saisir.**



```yaml

concept_id: "CONCEPT-CREATURE-001"
views_required:
  - "front"
  - "side"
  - "three_quarter"
checks:
  limb_count: "not_reviewed"
  joint_axes: "not_reviewed"
  mass_balance: "not_reviewed"
  ground_contact: "not_reviewed"
  cross_view_consistency: "not_reviewed"
  rig_feasibility: "not_reviewed"
issues: []
decision: "pending"
reviewer: null
reviewed_at: null

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** La grille empêche qu’une vue unique masque des incohérences qui bloqueraient la modélisation ou le rig.

- **États :** Chaque contrôle possède un état explicite ; l’absence d’issue ne vaut pas réussite tant que l’état reste `not_reviewed`.

- **Vues :** Les trois orientations imposent une comparaison minimale de volume et de connexion des membres.

- **Décision :** La sélection reste `pending` sans réviseur et sans date.

- **Résultat attendu :** Les corrections demandées peuvent être traduites en contraintes de concept ou en dessin manuel.

## 24. Contrôler les matériaux et la construction

Pour les objets et environnements, vérifier :

- rôle de chaque matériau ;
- épaisseur et assemblage ;
- mode de fixation ;
- comportement sous charge ;
- exposition à l’eau, au soleil, au sol et aux contacts ;
- causalité de l’usure ;
- cohérence d’échelle ;
- possibilité de produire des cartes PBR ;
- séparation entre décor et fonction ;
- continuité entre vues.

Une génération peut mélanger bois, métal, pierre et tissu sans assemblage plausible. Le concept retenu doit montrer comment les éléments tiennent ensemble, même si le détail final sera décidé en modélisation.

## 25. Contrôler les signes culturels et sociaux

Une variation culturelle ne doit pas être créée par addition aléatoire de motifs ou par imitation d’une culture réelle sans contexte. La revue doit demander :

- quelles contraintes environnementales expliquent les choix ;
- quelles ressources et techniques sont disponibles ;
- quelle fonction sociale possède l’objet ;
- quels éléments sont partagés avec les autres régions ;
- quelles références réelles ont été utilisées ;
- quels risques de stéréotype, mélange incohérent ou appropriation existent ;
- qui peut relire la proposition ;
- quelles parties doivent être remplacées par une invention propre au monde.

Lorsque la compétence interne manque, le projet doit signaler la réserve et prévoir une consultation adaptée avant publication.

> **[VSC] Visual Studio Code — Créer : `docs/art/concepts/reviews/CULTURAL-REVIEW-001.yaml` — Ne pas saisir.**



```yaml

concept_id: "CONCEPT-REGION-HIGHLANDS-001"
region_rule_ids:
  - "region.highlands.materials"
  - "region.highlands.weather"
real_world_reference_ids: []
review:
  environmental_causality: "not_reviewed"
  resource_plausibility: "not_reviewed"
  social_function: "not_reviewed"
  stereotype_risk: "not_reviewed"
  mixed_culture_risk: "not_reviewed"
  external_review_needed: true
issues: []
decision: "pending"

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** La grille exige des causes environnementales et sociales au lieu de valider une apparence seulement exotique.

- **Références :** La liste vide montre qu’aucune culture réelle n’est encore revendiquée comme source.

- **Risque :** Les risques de stéréotype et de mélange sont des contrôles distincts.

- **Escalade :** `external_review_needed: true` conserve une réserve lorsque l’équipe ne possède pas la compétence suffisante.

- **Résultat attendu :** La sélection peut être suspendue sans masquer la raison ni présenter une validation culturelle inexistante.

## 26. Comparer les concepts à la bible visuelle

La grille du chapitre 2 reste l’autorité artistique. Le rapport du présent chapitre doit citer les règles exactes et distinguer :

- conforme ;
- limite acceptable pour expérimentation ;
- non conforme ;
- impossible à évaluer ;
- dérogation proposée.

Une dérogation ne doit pas être ajoutée automatiquement parce qu’une image est appréciée. Elle suit le processus de la bible et identifie les conséquences sur les autres assets.

> **[VSC] Visual Studio Code — Créer : `docs/art/concepts/reviews/SELECT-WATCHPOST-001.yaml` — Ne pas saisir.**



```yaml

review_id: "SELECT-WATCHPOST-001"
question_id: "REFQ-ARCH-WATCHPOST-001"
candidates:
  - concept_id: "CONCEPT-WATCHPOST-0003"
    run_id: "RUN-WF-CONCEPT-ENV-001-0001"
    output_index: 3
    assessments:
      shape.civilization.angular: "conform"
      silhouette.medium_distance: "conform"
      material.wear.causal: "limit"
    issues:
      - "réparation métallique sans fixation lisible"
    decision: "revise"
  - concept_id: "CONCEPT-WATCHPOST-0006"
    run_id: "RUN-WF-CONCEPT-ENV-001-0002"
    output_index: 2
    assessments:
      shape.civilization.angular: "non_conform"
      silhouette.medium_distance: "conform"
      material.wear.causal: "unknown"
    issues:
      - "forme principale trop organique pour la famille"
    decision: "reject"
selected_concept: null
reviewer: "art-direction-owner"
reviewed_at: null

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** Le rapport compare deux candidats règle par règle et conserve les causes de révision ou de rejet.

- **États :** `limit`, `non_conform` et `unknown` distinguent un écart mesuré d’une information impossible à lire.

- **Décision :** Aucun concept n’est sélectionné tant que le candidat révisable n’a pas reçu de fixations lisibles.

- **Traçabilité :** Chaque candidat cite son run et son index de sortie.

- **Résultat attendu :** Une itération suivante répond à un problème précis au lieu de relancer arbitrairement le workflow.

## 27. Consolider un concept retenu

Une sortie retenue doit être transformée en dossier de concept. Selon l’asset, ce dossier peut inclure :

- vue principale annotée ;
- silhouette simplifiée ;
- vues orthogonales ou précisions manuelles ;
- proportions et échelle ;
- matériaux nommés ;
- assemblages et fonctions ;
- variantes autorisées ;
- éléments interdits ;
- points encore inconnus ;
- références utilisées ;
- workflow et run ;
- rapport de sélection ;
- conséquences pour la modélisation.

Les vues supplémentaires générées ne doivent pas être présentées comme cohérentes si elles ne le sont pas. Une correction dessinée ou une note technique peut être plus honnête qu’une nouvelle image qui invente un autre objet.

> **[VSC] Visual Studio Code — Créer : `docs/art/concepts/CONCEPT-REGISTER.yaml` — Ne pas saisir.**



```yaml

schema_version: 1
concepts:
  - id: "CONCEPT-WATCHPOST-001"
    question_id: "REFQ-ARCH-WATCHPOST-001"
    status: "selected_for_consolidation"
    primary_output:
      run_id: "RUN-WF-CONCEPT-ENV-001-0003"
      output_index: 1
      sha256: null
    workflow_id: "WF-CONCEPT-ENV-001"
    review_id: "SELECT-WATCHPOST-001"
    source_files:
      - "watchpost-001-annotations.svg"
      - "watchpost-001-proportions.md"
    unresolved:
      - "mécanisme de fixation de la passerelle"
    production_ready: false

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** Le registre promeut une proposition vers la consolidation tout en conservant une question technique non résolue.

- **Sources :** Les annotations vectorielles et la fiche de proportions deviennent des sources modifiables distinctes de l’image générée.

- **Empreinte :** Le hash de sortie sera ajouté depuis le fichier réel.

- **Porte :** `production_ready: false` interdit de transmettre le concept comme asset ou plan complet de fabrication.

- **Résultat attendu :** Le chapitre 4 et les chapitres de modélisation reçoivent un dossier explicite plutôt qu’une image isolée.

## 28. Préserver la couleur et les formats sans surpromesse

Les concepts servent à décider, pas à définir seuls les couleurs finales. Les captures, navigateurs, applications et conversions peuvent modifier l’apparence. Conserver :

- fichier source ou sortie originale ;
- profil colorimétrique lorsqu’il existe ;
- format et profondeur ;
- dimensions ;
- version annotée séparée ;
- miniature dérivée ;
- empreintes ;
- notes sur l’affichage de revue.

Éviter d’utiliser une compression destructive comme unique source. Ne pas déduire une couleur PBR ou UI définitive d’une image générée sans mesure et validation dans les outils appropriés.

## 29. Protéger les données, personnes et secrets

Les prompts, références et sorties peuvent contenir des informations confidentielles. Le workflow JSON peut inclure des chemins locaux, des noms de fichiers ou des textes internes. Les custom nodes peuvent effectuer des communications réseau. Le projet doit :

- exclure les secrets des prompts et fichiers ;
- utiliser des chemins relatifs ou neutralisés dans les exports ;
- ne pas envoyer de références confidentielles vers un service distant sans autorisation ;
- vérifier les journaux ;
- séparer les sorties destinées au partage ;
- retirer les métadonnées sensibles sur une copie ;
- conserver la provenance avant nettoyage ;
- limiter les accès aux références non redistribuables ;
- documenter toute utilisation d’un service externe.

Ce chapitre privilégie les workflows locaux, mais « local » ne signifie pas automatiquement sans réseau lorsque des extensions sont installées.

> **[VSC] Visual Studio Code — Créer : `workflows/comfyui/manifests/SHARING-CHECKLIST.yaml` — Ne pas saisir.**



```yaml

before_sharing:
  workflow_json:
    inspect_prompts: true
    inspect_paths: true
    inspect_model_names: true
    inspect_custom_node_parameters: true
  images:
    preserve_internal_original: true
    create_sanitized_copy: true
    inspect_embedded_workflow: true
    inspect_personal_metadata: true
  rights:
    references_redistributable: false
    model_output_terms_reviewed: false
    attribution_prepared: false
  decision:
    approved: false
    approved_by: null
    approved_at: null

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** La checklist sépare l’original interne de la copie distribuable et rend visible l’état des droits.

- **Métadonnées :** L’inspection du workflow embarqué évite de publier prompts, chemins et noms de modèles par inadvertance.

- **Droits :** Les trois valeurs fausses bloquent le partage tant que références, conditions du modèle et attribution ne sont pas traitées.

- **Autorité :** L’approbation exige une personne et une date.

- **Résultat attendu :** La publication devient une décision explicite et non un simple glisser-déposer d’une image générée.

## 30. Vérifier les fichiers et manifestes avec un script borné

Une vérification automatique peut confirmer que les chemins existent, que les empreintes correspondent et que les statuts bloqués ne sont pas présentés comme approuvés. Elle ne doit pas décider de la qualité artistique ou de la légalité.

Le script suivant illustre un contrôle local d’un manifeste de run. Il refuse les chemins absolus, les fichiers manquants et les empreintes incohérentes. Il ne télécharge rien et ne modifie aucun fichier.

> **[VSC] Visual Studio Code — Créer : `tools/verify_concept_run.py` — Ne pas saisir.**



```python

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_inside_workspace(raw: str) -> Path:
    candidate = (ROOT / raw).resolve()
    try:
        candidate.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError(f"chemin hors workspace : {raw}") from exc
    return candidate


def main(manifest_name: str) -> int:
    manifest_path = resolve_inside_workspace(manifest_name)
    data = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    if data.get("result") == "not_executed":
        print("Run non exécuté : aucune sortie à vérifier.")
        return 0

    failures: list[str] = []
    for item in data.get("outputs", []):
        path = resolve_inside_workspace(item["path"])
        if not path.is_file():
            failures.append(f"sortie absente : {item['path']}")
            continue
        actual = sha256(path)
        if actual != item["sha256"]:
            failures.append(f"empreinte incohérente : {item['path']}")

    for failure in failures:
        print(f"- {failure}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify_concept_run.py <manifest.yaml>")
    raise SystemExit(main(sys.argv[1]))

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** Le script lit un manifeste YAML, borne les chemins au workspace et compare les empreintes des sorties annoncées.

- **Fonctions :** `sha256` traite le fichier par blocs ; `resolve_inside_workspace` refuse une résolution en dehors de la racine.

- **Entrée et retour :** Un seul chemin de manifeste est exigé ; le programme retourne `1` si une sortie manque ou ne correspond pas.

- **Effets de bord :** Le script lit des fichiers et écrit seulement des messages sur les flux standard ; il ne corrige ni ne télécharge.

- **Limite :** Une empreinte valide ne prouve pas la qualité, la provenance ou les droits de la sortie.

- **Résultat attendu :** Une revue peut détecter un fichier remplacé ou un manifeste incomplet avant de discuter le concept.

## 31. Enregistrer les sorties d’un run sans masquer les rejets

Le manifeste de run doit lister chaque sortie conservée, son index, son empreinte et son statut. Il n’est pas nécessaire de conserver toutes les images à long terme, mais la suppression doit suivre la politique du projet :

- conserver les sorties sélectionnées ;
- conserver quelques rejets pédagogiques utiles ;
- conserver les paramètres et la matrice d’expérience ;
- supprimer les doublons et variantes sans information nouvelle ;
- ne pas supprimer une sortie faisant l’objet d’une décision, d’un litige ou d’une revue en cours ;
- mettre à jour le registre après suppression.

La sélection humaine peut être aveugle au nom du modèle ou de la seed lorsque cela réduit un biais de préférence, mais la traçabilité complète doit être rétablie après décision.

> **[VSC] Visual Studio Code — Ajouter à : `workflows/comfyui/manifests/RUN-WF-CONCEPT-ENV-001-0001.yaml` — Ne pas saisir.**



```yaml

outputs:
  - index: 1
    path: "../../../outputs/comfyui/quarantine/WF-CONCEPT-ENV-001/output-0001.png"
    sha256: null
    review_status: "pending"
  - index: 2
    path: "../../../outputs/comfyui/quarantine/WF-CONCEPT-ENV-001/output-0002.png"
    sha256: null
    review_status: "pending"
retention:
  keep_until: "selection_closed"
  deletion_allowed: false

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** La liste lie chaque fichier à un index stable et bloque sa suppression avant clôture de la sélection.

- **Chemins :** Les chemins relatifs facilitent le déplacement du workspace et peuvent être contrôlés par le script borné.

- **Empreintes :** Les valeurs restent nulles avant génération et calcul réel.

- **Cycle de vie :** `keep_until` et `deletion_allowed` rendent explicite la politique de rétention.

- **Résultat attendu :** Les rapports de revue ne pointent pas vers des fichiers susceptibles de disparaître silencieusement.

## 32. Préparer l’intégration dans Godot sans importer les concepts

Les concepts peuvent être affichés dans une scène ou un document de validation comme références de comparaison, mais ils ne doivent pas être placés dans les dossiers d’assets finaux. Une image de concept peut servir à :

- comparer une silhouette à la caméra de jeu ;
- vérifier une échelle approximative ;
- annoter une zone de fonction ;
- préparer une fiche de modélisation ;
- définir des questions pour un blockout.

Elle ne fournit pas directement :

- topologie ;
- UV ;
- cartes PBR ;
- collision ;
- LOD ;
- rig ;
- animation ;
- budget mémoire ;
- licence d’asset final.

Si une image est temporairement importée dans Godot pour une planche de référence, utiliser un chemin explicitement exclu de la livraison et un identifiant de contenu non autoritaire.

> **[LECTURE] Contrat de planche de référence Godot — Ne pas saisir.**



```yaml

reference_board:
  id: "REFBOARD-WATCHPOST-001"
  concept_id: "CONCEPT-WATCHPOST-001"
  source_image: "res://reference_only/watchpost-001.png"
  shipping_allowed: false
  gameplay_authority: false
  scale_claim: "approximate"
  material_claim: "concept_only"
  delete_before_release: true
validation:
  scene_materialized: false
  import_tested: false
  camera_compared: false

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** Le contrat permet une comparaison visuelle dans Godot sans promouvoir l’image vers les assets livrables.

- **Autorité :** `shipping_allowed` et `gameplay_authority` sont faux afin d’éviter qu’une référence devienne une ressource du jeu.

- **Allégations :** L’échelle reste approximative et les matériaux conceptuels.

- **Validation :** Les trois contrôles restent faux puisqu’aucune scène n’a été matérialisée.

- **Résultat attendu :** Le blockout futur peut citer le concept tout en conservant les exigences techniques des chapitres de production.

## 33. Budgets d’itération et règle d’arrêt

La génération peu coûteuse en apparence peut produire un coût élevé de tri, de stockage et de décision. Définir avant le run :

- nombre maximal de variantes ;
- résolution de travail ;
- nombre d’expériences simultanées ;
- temps maximal de revue ;
- espace disque ;
- nombre de concepts à consolider ;
- critères de rejet immédiat ;
- critères d’arrêt ;
- personne autorisée à prolonger l’expérience.

Les valeurs doivent être calibrées après exécution sur le matériel réel. Aucun temps de génération n’est fourni ici pour la RX 6750 XT.

> **[VSC] Visual Studio Code — Créer : `docs/art/concepts/ITERATION-BUDGETS.yaml` — Ne pas saisir.**



```yaml

budgets:
  solo:
    active_questions_max: 3
    variants_per_experiment_max: 12
    selected_concepts_per_asset_max: 2
    review_minutes_per_batch_max: 45
  studio:
    active_questions_max: 8
    variants_per_experiment_max: 24
    selected_concepts_per_asset_max: 3
    review_minutes_per_batch_max: 60
runtime_measurements:
  reference_gpu: "AMD Radeon RX 6750 XT 12 GB"
  seconds_per_output: null
  peak_vram_bytes: null
  disk_bytes_per_batch: null
  measured: false

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** Les plafonds limitent l’accumulation avant de connaître le coût réel de génération et de revue.

- **Parcours :** Le Studio autorise plus de questions et de variantes mais conserve une limite stricte de concepts consolidés.

- **Mesures :** Les coûts runtime restent nuls et `measured` reste faux sur la configuration de référence.

- **Effet de bord :** Dépasser un plafond exige une décision explicite au lieu d’une relance automatique.

- **Résultat attendu :** Le temps humain de critique devient une ressource planifiée au même titre que le calcul.

## 34. Mode Solo

En Mode Solo, réduire le nombre de systèmes à maintenir :

- un registre de références ;
- un moodboard par question importante ;
- un ou deux workflows Core stables ;
- un manifeste commun de modèles ;
- aucune extension sans besoin démontré ;
- une matrice d’expérience courte ;
- une revue différée après une pause ;
- deux concepts consolidés maximum par asset ;
- suppression régulière des variantes sans valeur ;
- journal de décisions concis.

La même personne peut rechercher, générer et sélectionner, mais elle doit séparer ces moments. Une revue immédiate favorise l’attachement à la dernière sortie obtenue. L’usage d’une grille et d’identifiants permet de comparer les concepts sans dépendre de la mémoire.

## 35. Mode Studio

En Mode Studio, séparer les responsabilités sans créer des silos :

- recherche et provenance ;
- direction artistique ;
- opérateur ComfyUI ;
- sécurité des extensions ;
- validation juridique ;
- spécialiste de domaine ou relecteur culturel ;
- revue anatomique ou technique ;
- décision de sélection ;
- préparation du dossier de production.

Le workflow et le modèle ne doivent pas être modifiés pendant une revue sans nouvelle version. Les commentaires citent un candidat, une règle et une action. La personne qui a généré les images peut défendre l’intention, mais la validation juridique et la promotion vers la production restent indépendantes.

## 36. Contrat commun entre Solo et Studio

Les deux parcours partagent les mêmes invariants :

- question visuelle avant collecte ;
- provenance avant moodboard ;
- droits liés à un usage précis ;
- workflow JSON versionné ;
- modèles et custom nodes manifestés ;
- paramètres et seeds enregistrés ;
- sorties en quarantaine avant revue ;
- critique humaine multidimensionnelle ;
- sélection reliée à la bible ;
- concept consolidé distinct de l’asset final ;
- aucune promesse runtime sans mesure ;
- aucune redistribution sans revue.

> **[LECTURE] Responsabilités comparées — Ne pas saisir.**



```markdown

| Responsabilité | Solo | Studio |
|---|---|---|
| recherche | créateur avec question bornée | documentaliste ou artiste assigné |
| provenance | registre unique | revue de registre et propriétaire |
| génération | workflows stables limités | opérateur sur environnement qualifié |
| sélection | revue différée avec grille | comité réduit avec autorité nommée |
| sécurité | revue avant extension | approbation technique séparée |
| droits | réserve explicite | validation juridique ou rôle désigné |
| consolidation | annotations personnelles versionnées | dossier transmis aux producteurs |
| invariant | aucun concept promu sans preuve | aucun concept promu sans preuve |

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** Le tableau adapte le nombre de rôles sans modifier les portes de provenance, sécurité, sélection et consolidation.

- **Différence :** Le Studio distribue les responsabilités ; le Solo sépare surtout les moments et les documents.

- **Autorité :** La promotion nécessite une preuve dans les deux parcours.

- **Transmission :** Le Studio formalise le passage vers les producteurs, tandis que le Solo conserve des annotations versionnées.

- **Résultat attendu :** La taille de l’équipe ne change pas la distinction entre proposition, concept et asset final.

## 37. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 37.1 Collecter des images sans question



**Symptôme :** Le moodboard grandit, mais personne ne sait quelle décision il doit permettre de prendre.



**Exemple fautif :**



> **[LECTURE] Contre-exemple — Ne pas saisir.**



```yaml

moodboard:
  - "belle image 1"
  - "belle image 2"
  - "belle image 3"
goal: "trouver le style"

```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** La formulation n’identifie ni asset, ni dimension observable, ni condition d’arrêt. Chaque participant peut interpréter le dossier selon ses préférences.



**Exemple corrigé :**



> **[LECTURE] Correction — Ne pas saisir.**



```yaml

question_id: "REFQ-ARCH-REPAIR-001"
decision: "montrer une réparation récente sans contraste saturé"
observe:
  - "assemblage"
  - "rugosité"
stop_condition:
  qualified_references: 12

```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction borne le sujet, nomme les propriétés examinées et définit quand la collecte peut s’arrêter.

### 37.2 Utiliser une référence dont les droits sont inconnus



**Symptôme :** Une image appréciée est publiée dans le dépôt et réutilisée comme entrée générative sans source vérifiée.



**Exemple fautif :**



> **[LECTURE] Contre-exemple — Ne pas saisir.**



```yaml

reference:
  url: null
  license: "probably_free"
  allowed_uses:
    - "everything"
  status: "approved"

```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** L’absence de source est remplacée par une supposition et l’usage universel n’est soutenu par aucune preuve.



**Exemple corrigé :**



> **[LECTURE] Correction — Ne pas saisir.**



```yaml

reference:
  url: null
  license: "unknown"
  allowed_uses:
    - "internal_visual_analysis"
  restrictions:
    - "no_redistribution"
    - "no_generation_input"
  status: "blocked"

```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction limite l’usage interne et bloque redistribution et conditionnement tant que la source et les droits ne sont pas documentés.

### 37.3 Installer automatiquement tous les custom nodes manquants



**Symptôme :** L’ouverture d’un workflow tiers entraîne l’exécution de code et l’installation de dépendances non examinées.



**Exemple fautif :**



> **[PS] PowerShell 7 — Exécuter : contre-exemple de sécurité — Ne pas saisir.**



```powershell

# À éviter
comfy node install-deps --all-missing
comfy launch

```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** La commande traite l’absence de nœuds comme une autorisation d’installer et d’exécuter du code provenant de sources inconnues.



**Exemple corrigé :**



> **[PS] PowerShell 7 — Exécuter : procédure de revue — Ne pas saisir.**



```powershell

# Procédure de revue
$Workflow = "incoming/workflow.json"
Write-Output "Inventorier les nœuds manquants : $Workflow"
Write-Output "Vérifier dépôt, version, licence et dépendances"
Write-Output "Installer uniquement après approbation explicite"

```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction sépare inventaire, revue et installation ; aucun paquet n’est exécuté par défaut.

### 37.4 Croire qu’une seed fixe garantit une image identique



**Symptôme :** Le même nombre est enregistré, mais le modèle et les versions changent entre deux exécutions.



**Exemple fautif :**



> **[LECTURE] Contre-exemple — Ne pas saisir.**



```yaml

reproducibility:
  seed: 42
  claim: "bit_exact_on_any_machine"

```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** La seed ne capture ni le modèle, ni le workflow, ni les versions, ni le backend matériel et ne justifie pas une identité binaire.



**Exemple corrigé :**



> **[LECTURE] Correction — Ne pas saisir.**



```yaml

reproducibility:
  seed: 42
  workflow_sha256: "to_be_computed"
  model_sha256: "to_be_computed"
  environment_profile: "qualified"
  claim: "family_reproduction_not_yet_tested"

```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction enregistre les dépendances nécessaires et réduit l’allégation au niveau qui peut réellement être testé.

### 37.5 Modifier plusieurs variables dans la même expérience



**Symptôme :** Une variante paraît meilleure, mais il est impossible de savoir si le résultat vient du modèle, du prompt, de la seed ou du sampler.



**Exemple fautif :**



> **[LECTURE] Contre-exemple — Ne pas saisir.**



```yaml

experiment:
  model: "new"
  prompt: "rewritten"
  seed: "random"
  sampler: "changed"
  steps: 60
  conclusion: "better"

```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** Toutes les causes potentielles changent simultanément et la conclusion n’est reliée à aucun critère.



**Exemple corrigé :**



> **[LECTURE] Correction — Ne pas saisir.**



```yaml

experiment:
  independent_variable:
    field: "shape.primary"
    values: ["rectangular", "triangular"]
  controlled:
    model_id: "MODEL-CHECKPOINT-001"
    seed: 4815162342
    sampler: "recorded_from_workflow"
  criteria: ["silhouette", "function_readability"]

```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction isole une variable, maintient le contexte et définit les critères avant la comparaison.

### 37.6 Sélectionner seulement l’image la plus spectaculaire



**Symptôme :** Le concept retenu fonctionne en illustration rapprochée mais ne respecte ni silhouette de jeu ni fonction de l’asset.



**Exemple fautif :**



> **[LECTURE] Contre-exemple — Ne pas saisir.**



```yaml

selection:
  candidate: "output-0042.png"
  reason: "most cinematic"
  bible_checks: []
  functional_checks: []

```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** Le motif de sélection décrit une préférence de présentation sans confronter l’image aux exigences de production.



**Exemple corrigé :**



> **[LECTURE] Correction — Ne pas saisir.**



```yaml

selection:
  candidate: "CONCEPT-WATCHPOST-0003"
  assessments:
    silhouette.medium_distance: "conform"
    function.watchpost: "conform"
    material.wear.causal: "limit"
  decision: "revise"
  issue: "ajouter des fixations lisibles"

```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction cite les règles, conserve un écart précis et demande une révision avant promotion.

### 37.7 Confondre une image générée avec un asset final



**Symptôme :** Une sortie PNG est placée dans le dossier de textures et déclarée prête pour Godot.



**Exemple fautif :**



> **[LECTURE] Contre-exemple — Ne pas saisir.**



```yaml

asset:
  source: "outputs/comfyui/image.png"
  status: "final"
  pbr_validated: true
  godot_validated: true

```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** Le statut et les validations sont inventés ; l’image ne fournit ni source de production, ni cartes PBR contrôlées, ni preuve moteur.



**Exemple corrigé :**



> **[LECTURE] Correction — Ne pas saisir.**



```yaml

concept:
  source: "outputs/comfyui/selected/image.png"
  status: "selected_for_consolidation"
  production_ready: false
  required_next_evidence:
    - "editable_source"
    - "modeling_decisions"
    - "godot_validation"

```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction conserve la sortie comme concept et énumère les preuves encore nécessaires avant un asset final.

### 37.8 Ignorer une incohérence anatomique entre vues



**Symptôme :** Une vue de face et une vue de profil représentent des articulations et des proportions différentes.



**Exemple fautif :**



> **[LECTURE] Contre-exemple — Ne pas saisir.**



```yaml

anatomy_review:
  views: ["front"]
  decision: "approved"
  issues: []

```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** Une seule vue ne permet pas de contrôler le volume, les axes articulaires ou la cohérence nécessaire au rig.



**Exemple corrigé :**



> **[LECTURE] Correction — Ne pas saisir.**



```yaml

anatomy_review:
  views: ["front", "side", "three_quarter"]
  cross_view_consistency: "failed"
  issues:
    - "position du genou incompatible entre face et profil"
  decision: "revise"

```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction exige plusieurs vues, nomme l’incohérence et empêche l’approbation avant reprise.

### 37.9 Publier une image contenant son workflow sensible



**Symptôme :** Une sortie est partagée publiquement avec des prompts internes, chemins locaux et noms de modèles dans ses métadonnées.



**Exemple fautif :**



> **[LECTURE] Contre-exemple — Ne pas saisir.**



```yaml

sharing:
  file: "original-output.png"
  inspect_metadata: false
  sanitized_copy: false
  approved: true

```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** L’original est diffusé sans inspection et l’approbation ne repose sur aucune vérification des métadonnées ou droits.



**Exemple corrigé :**



> **[LECTURE] Correction — Ne pas saisir.**



```yaml

sharing:
  internal_original: "original-output.png"
  public_copy: "public-output-sanitized.png"
  inspect_embedded_workflow: true
  inspect_personal_metadata: true
  rights_reviewed: true
  approved_by: "release-owner"

```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction préserve l’original interne, crée une copie dédiée et exige des contrôles et une autorité nommée.

### 37.10 Accumuler des variantes sans règle d’arrêt



**Symptôme :** Des centaines d’images sont générées, la revue est reportée et aucune décision n’est prise.



**Exemple fautif :**



> **[LECTURE] Contre-exemple — Ne pas saisir.**



```yaml

generation:
  batch_size: 100
  batches: "until_good"
  review_deadline: null
  stop_condition: null

```



<!-- qa:code-explanation -->



**Pourquoi cet exemple est fautif :** Le volume est illimité, la notion de résultat satisfaisant n’est pas définie et le coût humain de tri est ignoré.



**Exemple corrigé :**



> **[LECTURE] Correction — Ne pas saisir.**



```yaml

generation:
  variants_per_experiment_max: 12
  review_deadline: "same_work_session"
  stop_condition:
    clear_preference_found: true
    criteria_met:
      - "silhouette"
      - "function"
      - "bible_conformity"

```



<!-- qa:code-explanation -->



**Pourquoi la correction fonctionne :** La correction borne le lot, impose une revue et relie l’arrêt à des critères définis avant la génération.

## 38. Livrables à conserver

À la clôture documentaire de ce chapitre, le projet doit savoir produire ou préparer :

- registre de références avec provenance et usages ;
- fiches de questions visuelles ;
- moodboards annotés ;
- planches comparatives ;
- manifeste d’environnement ComfyUI ;
- workflows JSON versionnés ;
- manifestes de modèles et custom nodes ;
- manifestes de runs ;
- prompts structurés ;
- matrices d’expériences ;
- grilles anatomiques, matérielles et culturelles ;
- rapports de sélection ;
- registre des concepts ;
- dossiers consolidés ;
- checklist de partage ;
- budgets d’itération ;
- empreintes de fichiers significatifs.

Ces livrables restent des contrats proposés. Aucun fichier de `Project Asteria` n’est présenté comme matérialisé par le seul fait qu’un exemple apparaît dans le chapitre.

## 39. Application à Project Asteria

Pour le vertical slice, la première famille de concepts doit rester limitée :

1. un poste de veille architectural ;
2. un personnage ou costume pilote ;
3. une créature pilote ;
4. un objet d’interaction ;
5. une petite planche d’ambiance environnementale.

Chaque famille consomme les règles du chapitre 2 et produit un dossier de concept destiné aux chapitres de modélisation. Les références doivent être sourcées, les modèles et workflows manifestés, les sorties revues et les décisions consignées.

Les premières expériences doivent privilégier les nœuds Core et un seul modèle qualifié. Les custom nodes sont ajoutés seulement lorsqu’un manque précis est démontré. La configuration AMD Windows de référence reste une réserve runtime ; aucune cadence ni capacité de lot n’est supposée.

## 40. Contrôles avant transmission à la production

Avant de transmettre un concept :

- la question visuelle est fermée ou explicitement suspendue ;
- les références retenues possèdent provenance et contexte d’usage ;
- le moodboard cite les identifiants du registre ;
- le workflow JSON est enregistré et empreinté ;
- chaque modèle et custom node est manifesté ;
- le run sélectionné possède ses paramètres ;
- les entrées image sont autorisées ;
- les incohérences anatomiques, matérielles et culturelles sont traitées ou réservées ;
- le rapport de sélection cite les règles de la bible ;
- le concept consolidé contient des sources modifiables ;
- les inconnues sont listées ;
- `production_ready` reste faux tant que les chapitres de production n’ont pas fourni leurs preuves ;
- les copies destinées au partage sont revues séparément.

> **[LECTURE] Porte de transmission — Ne pas saisir.**



```yaml

concept_handoff:
  concept_id: "CONCEPT-WATCHPOST-001"
  provenance_complete: false
  workflow_manifest_complete: false
  model_manifest_complete: false
  custom_nodes_approved: false
  selection_review_complete: false
  technical_unknowns_closed: false
  editable_sources_present: false
  rights_cleared_for_intended_use: false
  production_ready: false
decision: "blocked"

```



<!-- qa:code-explanation -->



**Explication structurée du bloc :**



- **Rôle précis du bloc :** La porte regroupe les preuves nécessaires avant qu’un concept soit présenté comme dossier de production.

- **État initial :** Tous les contrôles restent faux parce que le chapitre ne matérialise pas le cas Asteria.

- **Autorité :** La décision `blocked` découle des preuves manquantes et non d’une appréciation de l’image.

- **Frontière :** Même une porte entièrement satisfaite ne crée pas automatiquement un asset Godot ; elle autorise la transmission aux chapitres de production.

- **Résultat attendu :** Les producteurs reçoivent un dossier traçable et une liste d’inconnues plutôt qu’une image ambiguë.

## 41. Sources officielles et points de vérification

Les points techniques du chapitre ont été comparés aux sources officielles suivantes, consultées le 22 juillet 2026 :

- [ComfyUI — version stable v0.28.0](https://github.com/Comfy-Org/ComfyUI/releases/tag/v0.28.0) ;
- [ComfyUI — concepts de workflow et sauvegarde JSON](https://docs.comfy.org/development/core-concepts/workflow) ;
- [ComfyUI — modèles](https://docs.comfy.org/development/core-concepts/models) ;
- [ComfyUI — installation manuelle](https://docs.comfy.org/installation/manual_install) ;
- [ComfyUI — exigences système](https://docs.comfy.org/installation/system_requirements) ;
- [ComfyUI — installation des custom nodes et avertissements de sécurité](https://docs.comfy.org/installation/install_custom_node) ;
- [ComfyUI Registry — standards de sécurité](https://docs.comfy.org/registry/standards) ;
- [ComfyUI — dépôt officiel et licence GPL-3.0](https://github.com/Comfy-Org/ComfyUI).

Les versions, pages de licence et conditions des modèles ou extensions réellement sélectionnés devront être vérifiées au moment de leur adoption. Les exemples du chapitre n’attribuent aucune licence à un modèle fictif.

## 42. Synthèse opérationnelle

Une chaîne de concept robuste commence par une question, pas par un bouton de génération. Les références sont qualifiées avant usage, les moodboards produisent des décisions, les workflows JSON restent versionnés, les modèles et extensions possèdent leurs manifestes, les seeds sont replacées dans leur environnement complet et les sorties restent en quarantaine jusqu’à une critique humaine.

ComfyUI accélère l’exploration mais ne décide ni des droits, ni de la cohérence culturelle, ni de la faisabilité anatomique, ni de la production. Le concept retenu devient un dossier consolidé comportant règles, paramètres, sources modifiables, inconnues et rapport de sélection. Il prépare la modélisation sans se substituer aux preuves techniques des chapitres suivants.
