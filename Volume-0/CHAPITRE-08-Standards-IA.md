---
title: "Chapitre 8 — Standards IA"
id: "DOC-V0-CH08"
status: "draft"
version: "0.5.0"
book: "Volume 0"
chapter: 8
language: "fr-FR"
tags:
  - intelligence-artificielle
  - reproductibilite
  - modeles-locaux
  - prompts
  - evaluation
  - securite
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Chapitre 8 — Standards IA

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## Objectif du chapitre

Ce chapitre définit les règles communes à toutes les fonctions d’intelligence artificielle utilisées dans le guide, dans le projet fil rouge et dans le Companion Pack.

Ces standards s’appliquent notamment aux domaines suivants :

- modèles de langage locaux ;
- génération et retouche d’images avec ComfyUI ;
- génération de voix, musique et bruitages ;
- transcription et sous-titrage ;
- assistance au code ;
- génération de données structurées ;
- recherche documentaire augmentée ;
- agents et automatisations ;
- génération ou préparation d’assets 2D et 3D ;
- évaluation automatique de contenu ;
- outils d’aide à la production, au test et au diagnostic.

L’objectif n’est pas de rendre chaque résultat identique au bit près sur toutes les machines. L’objectif est de rendre chaque processus :

1. compréhensible ;
2. traçable ;
3. reproductible dans des conditions comparables ;
4. mesurable ;
5. réversible ;
6. compatible avec une validation humaine ;
7. utilisable dans un environnement local maîtrisé.

> **Niveau : Obligatoire**  
> Toute fonctionnalité IA intégrée au projet doit respecter les règles minimales de provenance, de validation et de sécurité décrites dans ce chapitre.

## 1. Principes directeurs

### 1.1 Local d’abord

Le pipeline principal doit fonctionner localement sans dépendre d’un service distant obligatoire.

Une solution distante peut être présentée à titre comparatif ou utilisée comme solution secondaire, mais elle ne doit pas être nécessaire pour reproduire le parcours principal du guide.

Le fonctionnement local apporte plusieurs avantages :

- contrôle des données ;
- meilleure confidentialité ;
- coûts prévisibles ;
- fonctionnement hors ligne ;
- maîtrise des versions ;
- intégration plus simple aux outils de production ;
- réduction du risque de disparition d’une API ou d’un abonnement.

### 1.2 L’IA assiste, elle ne décide pas seule

Une sortie générée par IA est une proposition de travail, pas une vérité.

Aucune sortie critique ne doit être intégrée automatiquement sans validation lorsque cette sortie peut affecter :

- le code exécutable ;
- les sauvegardes ;
- l’économie du jeu ;
- les données personnelles ;
- la conformité légale ;
- les licences ;
- la sécurité du système ;
- la publication d’un contenu ;
- la cohérence narrative ;
- les limites applicables au contenu adulte.

### 1.3 Traçabilité avant automatisation

Une automatisation non traçable est considérée comme incomplète.

Avant d’automatiser une tâche IA, le projet doit pouvoir enregistrer au minimum :

- l’identifiant du modèle ;
- la version ou le hash du modèle lorsque disponible ;
- les paramètres principaux ;
- la date d’exécution ;
- le prompt ou l’instruction ;
- les fichiers d’entrée ;
- les fichiers de sortie ;
- le statut de validation ;
- les erreurs éventuelles.

### 1.4 Reproductibilité proportionnée

Toutes les tâches n’exigent pas le même niveau de reproductibilité.

Trois niveaux sont définis :

| Niveau | Usage | Exigence minimale |
|---|---|---|
| R1 — Exploratoire | Idéation, variantes, tests rapides | Modèle, prompt et paramètres principaux |
| R2 — Production | Asset, texte, voix ou donnée retenue | Modèle, prompt complet, seed, paramètres, provenance et validation |
| R3 — Critique | Code, migration, données sensibles, publication | Toutes les informations R2, revue humaine, test, journal et possibilité de retour arrière |

Le niveau requis doit être indiqué dans la fiche de la tâche ou du workflow.

## 2. Registre des modèles

### 2.1 Identité d’un modèle

Chaque modèle utilisé dans le projet doit posséder une fiche ou une entrée de registre.

Cette entrée doit contenir au minimum :

- un identifiant interne stable ;
- le nom public du modèle ;
- sa famille ;
- son format ;
- sa source ;
- sa licence ;
- sa taille ;
- sa quantification éventuelle ;
- son usage prévu ;
- ses limitations connues ;
- la mémoire requise ;
- la date d’ajout au projet ;
- le statut de validation.

Exemple d’identifiant :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
AI-MODEL-LLM-001
```

Exemple de registre simplifié :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
id: AI-MODEL-LLM-001
name: exemple-modele-local
family: llm
format: gguf
quantization: q4_k_m
source: local-cache
license: a-verifier
intended_use:
  - assistance-redactionnelle
  - generation-json
status: evaluation
validated_on:
  - windows-amd
```

### 2.2 Version et empreinte

Un nom de modèle seul n’est pas suffisant.

Lorsque le format le permet, le registre doit aussi conserver :

- le nom exact du fichier ;
- sa taille en octets ;
- une empreinte SHA-256 ;
- la date de téléchargement ;
- la source de téléchargement ;
- la révision ou le commit d’origine.

Cette règle évite de confondre deux fichiers portant un nom proche mais contenant des poids différents.

### 2.3 Licence et conditions d’usage

La licence doit être vérifiée avant l’intégration d’un modèle dans un pipeline de production.

La fiche doit distinguer :

- usage personnel ;
- usage commercial ;
- redistribution ;
- modification ;
- génération de contenu ;
- restrictions particulières ;
- obligations d’attribution.

Une licence inconnue ou ambiguë entraîne le statut :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
blocked-license-review
```

Un modèle dans cet état peut être testé localement, mais il ne doit pas être inclus dans une publication, une archive distribuée ou un produit commercial tant que sa licence n’a pas été clarifiée.

## 3. Gestion des prompts

### 3.1 Le prompt est une ressource versionnée

Un prompt de production ne doit pas être conservé uniquement dans une interface graphique ou dans un historique de conversation.

Il doit être enregistré dans un fichier versionné avec :

- un identifiant ;
- un objectif ;
- une version ;
- le modèle cible ;
- les variables attendues ;
- le format de sortie ;
- des exemples ;
- les critères de validation ;
- les limitations connues.

Exemple d’identifiant :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
AI-PROMPT-NPC-DIALOGUE-001
```

### 3.2 Séparer instruction et données

Les données injectées dans un prompt doivent être clairement séparées des instructions.

Exemple recommandé :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
[SYSTEME]
Tu produis uniquement un objet JSON conforme au schéma fourni.

[CONTEXTE]
{{context}}

[DONNEES]
{{input_data}}

[TACHE]
{{task}}

[FORMAT_DE_SORTIE]
{{schema}}
```

Cette séparation facilite :

- la lecture ;
- le débogage ;
- la détection d’injections ;
- le remplacement des variables ;
- les tests automatisés.

### 3.3 Variables explicites

Les variables d’un prompt doivent utiliser une syntaxe uniforme.

Convention recommandée :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
{{variable_name}}
```

Chaque variable doit être documentée avec :

- son type ;
- son caractère obligatoire ou facultatif ;
- sa valeur par défaut ;
- sa longueur maximale ;
- les caractères interdits ;
- un exemple valide.

### 3.4 Prompts négatifs

Pour les workflows qui les utilisent, les prompts négatifs doivent être versionnés séparément ou dans une section dédiée.

Ils ne doivent pas servir à masquer l’absence de contrôle qualité. Un prompt négatif très long peut indiquer :

- un mauvais modèle ;
- un mauvais dataset ;
- un mauvais conditionnement ;
- une résolution inadaptée ;
- un workflow instable ;
- des critères artistiques insuffisamment définis.

### 3.5 Langue des prompts

La langue choisie doit être adaptée au modèle et au résultat attendu.

Le guide peut expliquer en français tout en utilisant un prompt en anglais lorsque cela améliore réellement la compatibilité avec le modèle. Dans ce cas :

- le prompt original est conservé ;
- une explication française est fournie ;
- les termes techniques importants sont traduits ;
- les différences de résultat sont documentées.

## 4. Paramètres et seeds

### 4.1 Paramètres obligatoires

Une génération de production doit conserver tous les paramètres capables de modifier significativement le résultat.

Selon le type de modèle, cela peut inclure :

- seed ;
- température ;
- top-p ;
- top-k ;
- pénalité de répétition ;
- longueur maximale ;
- sampler ;
- scheduler ;
- nombre d’étapes ;
- CFG ;
- résolution ;
- durée ;
- fréquence d’échantillonnage ;
- modèle de voix ;
- vitesse et expressivité ;
- poids des adaptateurs ;
- paramètres de quantification ;
- taille de contexte ;
- nombre de threads ;
- options GPU.

### 4.2 Seed fixe et seed aléatoire

Une seed fixe est obligatoire pour :

- reproduire une anomalie ;
- comparer deux versions d’un workflow ;
- mesurer l’impact d’un paramètre ;
- valider une régression ;
- archiver un asset retenu.

Une seed aléatoire reste acceptable pour l’exploration, à condition que la seed effectivement utilisée soit enregistrée avec le résultat.

### 4.3 Comparaison contrôlée

Lors d’un benchmark, un seul facteur doit être modifié à la fois, sauf lorsque le test porte explicitement sur une configuration complète.

Une comparaison correcte conserve autant que possible :

- le même prompt ;
- la même seed ;
- la même entrée ;
- le même matériel ;
- la même résolution ;
- le même nombre d’étapes ;
- le même protocole de mesure.

## 5. Standards pour les modèles de langage

### 5.1 Sortie structurée

Lorsqu’un modèle alimente un système logiciel, la sortie libre doit être évitée.

Le format recommandé est un objet structuré validable, par exemple :

- JSON ;
- YAML lorsque le risque d’ambiguïté est maîtrisé ;
- CSV pour les tableaux simples ;
- Markdown strict pour la documentation ;
- appels d’outils avec schéma explicite.

Tout JSON de production doit être validé par un schéma ou par un parseur strict avant utilisation.

### 5.2 Défense contre les hallucinations

Un modèle de langage ne doit jamais être considéré comme une source primaire.

Pour les faits techniques, le pipeline doit privilégier :

1. la documentation officielle ;
2. les fichiers réels du projet ;
3. les tests exécutés ;
4. les journaux ;
5. les sources vérifiables ;
6. l’inférence du modèle en dernier recours.

Une réponse incertaine doit pouvoir utiliser un état explicite :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```json
{
  "status": "uncertain",
  "reason": "information insuffisante",
  "needs_review": true
}
```

### 5.3 Taille de contexte

La quantité de contexte envoyée au modèle doit être limitée au strict nécessaire.

Un contexte trop grand peut :

- augmenter la consommation mémoire ;
- ralentir l’inférence ;
- diluer les instructions ;
- augmenter les contradictions ;
- rendre le diagnostic plus difficile.

Le découpage doit préserver les unités logiques : fonctions, classes, scènes, chapitres ou enregistrements complets.

### 5.4 Génération de code

Le code généré doit être traité comme du code externe non vérifié.

Avant intégration :

- le code est relu ;
- les imports sont vérifiés ;
- les commandes dangereuses sont recherchées ;
- les chemins et secrets sont contrôlés ;
- les tests sont exécutés ;
- le style du projet est appliqué ;
- la licence de fragments inhabituels est examinée ;
- les performances sont mesurées si nécessaire.

Le modèle ne doit pas recevoir automatiquement un droit d’écriture global sur le dépôt, le système de fichiers ou la base de données.

## 6. Recherche documentaire augmentée

### 6.1 Sources contrôlées

Un système RAG doit indiquer clairement quelles sources sont indexées.

Chaque corpus doit posséder :

- un identifiant ;
- une origine ;
- une date d’import ;
- une licence ;
- une langue ;
- une stratégie de découpage ;
- une version d’embedding ;
- une politique de mise à jour ;
- une politique de suppression.

### 6.2 Citation des sources

Une réponse fondée sur un corpus doit conserver un lien vers les extraits ayant contribué au résultat.

Une citation doit permettre de retrouver :

- le fichier ;
- la section ou la plage ;
- la version du fichier ;
- le score ou le rang de récupération lorsque disponible.

### 6.3 Données sensibles

Les données suivantes ne doivent pas être indexées sans décision explicite :

- mots de passe ;
- clés privées ;
- jetons d’accès ;
- données personnelles ;
- contrats confidentiels ;
- journaux contenant des identifiants ;
- fichiers soumis à une licence incompatible.

## 7. Standards ComfyUI et génération visuelle

### 7.1 ComfyUI comme source du workflow

Pour le pipeline visuel principal, le workflow ComfyUI constitue la description exécutable de la génération.

Chaque workflow de production doit conserver :

- son JSON ;
- son identifiant ;
- sa version ;
- les modèles requis ;
- les nœuds personnalisés ;
- leurs versions ;
- les paramètres exposés ;
- un exemple d’entrée ;
- un exemple de sortie ;
- la consommation VRAM observée ;
- les limitations connues.

### 7.2 Nœuds personnalisés

Un nœud personnalisé doit être considéré comme une dépendance logicielle.

Son installation doit indiquer :

- le dépôt source ;
- le commit ou la version ;
- la licence ;
- les dépendances Python ;
- les risques de compatibilité ;
- la procédure de désinstallation ;
- une solution de remplacement lorsque possible.

### 7.3 Métadonnées des images

Lorsqu’un format permet de conserver les métadonnées de génération, celles-ci ne doivent pas être supprimées de l’archive de production.

Une copie destinée à la publication peut être nettoyée, mais l’original de production doit conserver :

- workflow ;
- prompt ;
- seed ;
- modèle ;
- dimensions ;
- paramètres ;
- date ;
- statut de validation.

### 7.4 Références et droits

Une image de référence ne doit être utilisée que si sa provenance et ses droits sont compatibles avec l’usage prévu.

Le projet doit éviter :

- les références dont l’auteur est inconnu ;
- l’imitation directe d’un artiste vivant comme objectif de production ;
- l’usage non autorisé de visages réels ;
- l’intégration d’éléments protégés identifiables ;
- les datasets personnels non documentés.

## 8. Standards audio et voix

### 8.1 Identité d’une voix

Une voix synthétique doit être identifiée par :

- le moteur ;
- le modèle ;
- la langue ;
- la variante ;
- les paramètres prosodiques ;
- la seed si disponible ;
- les conditions de licence ;
- l’origine des données de référence.

### 8.2 Consentement et imitation

Il est interdit d’utiliser la voix d’une personne réelle sans autorisation adaptée à l’usage prévu.

Le projet ne doit pas présenter une voix synthétique comme étant celle d’une personne réelle lorsqu’elle ne l’est pas.

### 8.3 Qualité audio

Toute sortie retenue doit être contrôlée pour :

- les clics ;
- les saturations ;
- les silences anormaux ;
- les erreurs de prononciation ;
- les variations de volume ;
- les bruits parasites ;
- le format et la fréquence d’échantillonnage ;
- la synchronisation avec les sous-titres ou animations.

## 9. Agents et appels d’outils

### 9.1 Principe du moindre privilège

Un agent ne doit disposer que des outils nécessaires à sa tâche.

Exemples :

- un agent de résumé n’a pas besoin d’écrire dans le dépôt ;
- un agent de génération d’assets n’a pas besoin d’accéder aux sauvegardes ;
- un agent de test ne doit pas publier une version ;
- un agent de documentation ne doit pas supprimer des fichiers.

### 9.2 Actions réversibles

Les actions automatiques doivent privilégier :

- la création d’un brouillon ;
- une branche dédiée ;
- une copie de sauvegarde ;
- un mode simulation ;
- une transaction ;
- une corbeille plutôt qu’une suppression définitive.

### 9.3 Confirmation humaine

Une confirmation humaine est obligatoire avant :

- suppression massive ;
- publication ;
- envoi de messages externes ;
- modification de données de production ;
- rotation de secrets ;
- achat ou appel payant ;
- changement de licence ;
- fusion d’une modification critique ;
- génération d’un contenu sensible destiné à diffusion.

### 9.4 Journal des outils

Chaque appel d’outil doit pouvoir enregistrer :

- l’agent ;
- la tâche ;
- l’outil ;
- les paramètres non sensibles ;
- l’heure ;
- le résultat ;
- le code d’erreur ;
- la durée ;
- l’action de validation.

Les secrets doivent être masqués dans les journaux.

## 10. Évaluation des sorties

### 10.1 Critères avant score

Un score global sans critères explicites est insuffisant.

Chaque évaluation doit définir des dimensions adaptées, par exemple :

- exactitude ;
- cohérence ;
- fidélité au brief ;
- qualité technique ;
- style ;
- stabilité ;
- performance ;
- absence d’artefacts ;
- conformité au format ;
- conformité aux limites de contenu ;
- coût mémoire ;
- temps de génération.

### 10.2 Jeu de tests fixe

Les comparaisons entre modèles ou versions doivent utiliser un jeu de tests stable et versionné.

Ce jeu peut inclure :

- prompts courts ;
- prompts longs ;
- cas normaux ;
- cas limites ;
- entrées invalides ;
- plusieurs langues ;
- sorties structurées ;
- tâches adaptées au projet fil rouge.

### 10.3 Évaluation humaine

L’évaluation automatique ne remplace pas l’évaluation humaine pour les aspects subjectifs ou critiques.

Une revue humaine doit notamment être conservée pour :

- direction artistique ;
- cohérence narrative ;
- qualité d’un dialogue ;
- crédibilité d’une voix ;
- contenu adulte ;
- conformité légale ;
- expérience utilisateur ;
- décision de publication.

### 10.4 Régression

Une mise à jour de modèle ou de workflow doit être comparée à la version précédente sur le même protocole.

La mise à jour est refusée si elle provoque une régression non acceptée sur :

- qualité ;
- stabilité ;
- consommation mémoire ;
- vitesse ;
- compatibilité matérielle ;
- licence ;
- sécurité ;
- reproductibilité.

## 11. Performance et configuration AMD

### 11.1 Budget VRAM

La configuration de référence dispose de 12 Go de VRAM. Les workflows principaux doivent donc proposer un profil compatible avec cette enveloppe.

Chaque workflow lourd doit préciser :

- VRAM minimale ;
- VRAM observée ;
- RAM système observée ;
- temps de génération ;
- résolution testée ;
- options de réduction mémoire ;
- impact de ces options sur la qualité.

### 11.2 Profils de fonctionnement

Trois profils sont recommandés :

| Profil | Objectif | Caractéristiques |
|---|---|---|
| Économie | Compatibilité et stabilité | Faible résolution, quantification, déchargement mémoire |
| Équilibré | Usage principal | Qualité et temps adaptés à la machine de référence |
| Qualité | Sortie finale | Temps plus long, traitement par lots réduit, contrôle renforcé |

### 11.3 Mesure réelle

Les affirmations de performance doivent provenir d’une mesure et non d’une estimation vague.

Le rapport doit préciser :

- matériel ;
- système ;
- versions ;
- paramètres ;
- nombre d’essais ;
- moyenne ;
- valeur minimale et maximale ;
- erreurs rencontrées.

## 12. Données, confidentialité et conservation

### 12.1 Minimisation des données

Un modèle ne doit recevoir que les données nécessaires à la tâche.

Avant traitement, il faut retirer lorsque possible :

- secrets ;
- identifiants personnels ;
- chemins inutiles ;
- journaux complets lorsque quelques lignes suffisent ;
- métadonnées sensibles ;
- fichiers hors périmètre.

### 12.2 Conservation

Le projet doit distinguer :

- données d’entrée temporaires ;
- cache de modèle ;
- résultats exploratoires ;
- résultats de production ;
- journaux ;
- données de validation ;
- sauvegardes.

Chaque catégorie doit posséder une règle de conservation et de suppression.

### 12.3 Télémétrie

Les outils locaux doivent être configurés pour désactiver la télémétrie non nécessaire lorsque cette option existe.

Toute télémétrie conservée doit être documentée avec :

- les données collectées ;
- la destination ;
- la durée ;
- la méthode de désactivation.

## 13. Contenus sensibles et destinés aux adultes

### 13.1 Cadre général

Le guide peut traiter de systèmes de jeu destinés à un public adulte dans un cadre technique, narratif, artistique ou de simulation.

Les workflows doivent néanmoins appliquer les règles suivantes :

- personnages explicitement adultes ;
- consentement clair dans les systèmes concernés ;
- absence de personnes réelles non consentantes ;
- absence de contenu impliquant des mineurs ;
- absence de confusion sur l’âge ;
- contrôle humain obligatoire avant publication ;
- classification et avertissements adaptés ;
- séparation des ressources sensibles dans le pipeline de production.

### 13.2 Données de référence

Les références sensibles doivent provenir de sources légales, documentées et autorisées.

Elles ne doivent pas être ajoutées automatiquement à un corpus RAG, un dataset, un dépôt public ou une archive de distribution.

### 13.3 Validation

Une sortie sensible doit être validée selon au moins quatre axes :

1. conformité au brief ;
2. conformité aux limites du projet ;
3. conformité légale et aux plateformes visées ;
4. absence d’éléments non consentis ou ambigus.

## 14. Gestion des erreurs IA

### 14.1 Types d’erreurs

Les erreurs doivent être classées pour faciliter le diagnostic :

- modèle introuvable ;
- dépendance manquante ;
- manque de mémoire ;
- sortie invalide ;
- timeout ;
- contenu incomplet ;
- incohérence ;
- violation de schéma ;
- ressource sans licence ;
- résultat refusé par la validation ;
- incompatibilité de version ;
- erreur d’outil ou d’agent.

### 14.2 Échec explicite

Un système ne doit pas transformer silencieusement une erreur en succès.

Une sortie invalide doit produire un état explicite, par exemple :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```json
{
  "status": "failed",
  "error_code": "AI_OUTPUT_SCHEMA_INVALID",
  "retryable": true,
  "needs_human_review": false
}
```

### 14.3 Reprise contrôlée

Les tentatives automatiques doivent être limitées.

Le système doit éviter :

- les boucles infinies ;
- la multiplication incontrôlée des fichiers ;
- les appels répétés à un outil défaillant ;
- le masquage de l’erreur originale ;
- la modification progressive du prompt sans journal.

## 15. Modes Solo et Studio

### 15.1 Mode Solo

En Mode Solo, les standards minimaux sont :

- registre simple des modèles ;
- prompts stockés dans le dépôt ;
- seeds et paramètres conservés pour les résultats retenus ;
- validation manuelle ;
- sauvegarde locale ;
- tests sur la machine de référence ;
- journal léger mais lisible.

### 15.2 Mode Studio

En Mode Studio, il faut ajouter :

- registre centralisé ;
- contrôle des accès ;
- revue par pair ;
- stockage partagé versionné ;
- validation de licence ;
- CI pour les sorties structurées ;
- jeux de tests de régression ;
- suivi des coûts et performances ;
- politiques de conservation ;
- séparation développement, validation et production ;
- procédure d’incident.

## 16. Fiche minimale d’un workflow IA

Chaque workflow de production doit pouvoir être résumé par la fiche suivante :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
id: AI-WORKFLOW-XXX-001
name: nom-du-workflow
version: 0.1.0
status: draft
reproducibility_level: R2
purpose: description-courte
models:
  - AI-MODEL-XXX-001
inputs:
  - name: input
    type: file
outputs:
  - name: output
    type: file
parameters:
  seed: 123456
hardware_profile: amd-12gb-balanced
validation:
  human_review: true
  automated_tests: []
licenses_checked: false
known_limitations: []
```

## 17. Checklist de conformité IA

Avant de déclarer un workflow prêt pour la production, vérifier les points suivants :

- [ ] Le besoin d’utiliser une IA est justifié.
- [ ] Le workflow principal fonctionne localement.
- [ ] Les modèles sont enregistrés avec leur provenance.
- [ ] Les licences ont été examinées.
- [ ] Les prompts sont versionnés.
- [ ] Les variables sont documentées.
- [ ] Les paramètres influents sont conservés.
- [ ] La seed est enregistrée lorsque pertinente.
- [ ] Les entrées et sorties sont traçables.
- [ ] Les sorties structurées sont validées.
- [ ] Les résultats critiques sont revus par une personne.
- [ ] Les secrets ne sont pas présents dans les prompts ou journaux.
- [ ] Les actions d’agent utilisent le moindre privilège.
- [ ] Les actions destructrices nécessitent une confirmation.
- [ ] La consommation RAM et VRAM a été mesurée.
- [ ] Les cas d’erreur sont explicites.
- [ ] Une procédure de retour arrière existe.
- [ ] Les contenus sensibles respectent les limites du projet.
- [ ] Un jeu de tests permet de détecter les régressions.
- [ ] Le workflow est documenté pour les modes Solo et Studio.

## Conclusion

Les standards IA du projet reposent sur une idée centrale : une génération utile doit rester maîtrisable.

Un résultat n’est pas prêt pour la production simplement parce qu’il paraît convaincant. Il devient exploitable lorsque son origine est connue, ses paramètres sont conservés, ses limites sont comprises, sa licence est vérifiée, sa qualité est mesurée et sa validation humaine est documentée.

Ces règles constituent la base des chapitres consacrés aux LLM locaux, à ComfyUI, aux voix, à la musique, aux agents, à l’automatisation et aux outils de production assistés par IA.
