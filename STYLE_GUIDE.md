# Guide de style éditorial

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## Langue

Le contenu principal est rédigé en français. Les noms officiels d'outils, d'API, de classes et de paramètres restent dans leur forme d'origine.

## Public

Le guide s'adresse d'abord aux débutants. Toute notion technique doit être définie avant sa première utilisation.

## Ton

- Direct, pédagogique et précis.
- Pas de promesse non vérifiable.
- Pas de jargon sans définition.
- Les limites, risques et incertitudes sont signalés clairement.

## Hiérarchie Markdown

- Un seul titre `#` par fichier.
- Les sections principales utilisent `##`.
- Les sous-sections utilisent `###` puis `####`.
- Éviter de dépasser quatre niveaux de titres.

## Fiches de chapitre

Chaque chapitre doit indiquer, lorsque pertinent :

- son objectif ;
- ses prérequis ;
- son niveau de priorité : **Obligatoire**, **Recommandé** ou **Optionnel** ;
- les particularités **Mode Solo** et **Mode Studio** ;
- les outils et versions concernés ;
- des exemples progressifs ;
- les erreurs fréquentes ;
- les optimisations pour la configuration AMD de référence ;
- une checklist et des références croisées.

## Code

- Toujours préciser le langage après les trois accents graves.
- Les exemples doivent être exécutables ou explicitement identifiés comme pseudocode.
- Utiliser quatre espaces d'indentation dans Python, GDScript, JSON et YAML.
- Ne jamais inclure de secrets réels, de jetons ou d'identifiants privés.

## Contextes d’utilisation

Chaque commande, contenu de fichier ou lien procédural indique le programme à utiliser. La convention normative est définie par `DOC-V0-ANN-CONTEXTES`.

Repères principaux :

- **[PS]** : exécuter dans PowerShell 7 sur l’hôte Windows ;
- **[VSC]** : créer ou modifier le fichier dans Visual Studio Code, avec son chemin ;
- **[WEB]** : ouvrir la page dans un navigateur internet ;
- **[DCK]** : effectuer l’action dans l’interface Docker Desktop ;
- **[DCT]** : exécuter dans le terminal d’un conteneur ;
- **[WSL]** : exécuter dans un terminal WSL/Bash ;
- **[APP]** : effectuer l’action dans l’application nommée ;
- **[SORTIE]** : résultat à lire, jamais à saisir ;
- **[LECTURE]** : exemple ou structure non directement exécutable.

Le repère se place immédiatement avant le bloc ou le lien. Un contenu JSON, YAML, Python, GDScript ou autre destiné à un fichier doit indiquer **Visual Studio Code** et le chemin cible.

## Noms et chemins

- Fichiers Markdown : `CHAPITRE-XX-Titre-en-kebab-case.md`.
- Ressources techniques : identifiants stables définis dans le Volume 0.
- Chemins dans le texte : entre accents graves.

## Tableaux

Les tableaux servent aux comparaisons compactes. Les procédures détaillées restent sous forme de sections ou d'étapes numérotées.

## Liens et sources

- Privilégier les documentations officielles et sources primaires.
- Donner la date de vérification pour les informations susceptibles d'évoluer.
- Éviter les liens promotionnels et les sources non fiables.
- Respecter les licences et les limites de citation.
- Dans une section de sources ou de références techniques, toute page web citée utilise un lien Markdown nommé et directement cliquable, par exemple `[Documentation officielle — Fonction](https://exemple.invalid/page)`. Une URL brute, une URL entre accents graves ou une URL placée dans un bloc de code ne constitue pas une référence lecteur conforme.

## Illustrations

Chaque illustration doit comporter :

- un nom de fichier explicite ;
- un texte alternatif utile ;
- une légende lorsque nécessaire ;
- sa source et sa licence si elle n'a pas été créée pour le guide.

## Contenu adulte

Les sections destinées à un public adulte sont clairement identifiées et séparées. Elles doivent rappeler que tous les personnages concernés sont adultes, que les interactions reposent sur le consentement et qu'aucun contenu impliquant des mineurs n'est admis.

## Références croisées

Les références utilisent des identifiants stables plutôt que des numéros de page, car la pagination change selon le format de sortie.
