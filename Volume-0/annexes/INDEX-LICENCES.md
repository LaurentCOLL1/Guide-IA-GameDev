---
title: "Annexe — Index des licences"
id: "DOC-V0-ANN-INDEX-LICENCES"
status: "in-progress"
version: "0.1.0"
---

# Index des licences

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](CONVENTION-OUTILS-ET-CONTEXTES.md).

Cet index organise la vérification des licences applicables aux logiciels, modèles, jeux de données, assets et livrables. Il ne constitue pas un avis juridique. Toute publication commerciale ou redistribution importante doit faire l’objet d’une vérification adaptée au territoire et au mode de diffusion.

## Principes obligatoires

- Aucun composant ne doit être redistribué sans licence identifiable.
- La licence du code ne couvre pas automatiquement les modèles, données, voix, images ou musiques associés.
- Une ressource gratuite n’est pas nécessairement libre, redistribuable ou exploitable commercialement.
- Les obligations d’attribution, de partage à l’identique, de publication du code source ou de conservation des notices doivent être enregistrées.
- Les conditions d’un service distant sont distinctes de la licence d’un logiciel local.
- Les restrictions d’usage propres aux modèles ou jeux de données doivent être conservées avec leur fiche.

## Catégories du registre

| Code | Catégorie | Exemples de composants | Vérifications minimales |
|---|---|---|---|
| LIC-CODE | Code logiciel | Moteur, bibliothèque, script, plugin | Copyleft, attribution, redistribution, liaison et modifications |
| LIC-MODEL | Modèle IA | LLM, modèle image, LoRA, TTS | Licence des poids, usages autorisés, redistribution, dérivés |
| LIC-DATA | Jeu de données | Corpus, embeddings, données d’entraînement | Provenance, consentement, droits sui generis, restrictions d’usage |
| LIC-ASSET | Asset artistique | Modèle 3D, texture, animation, police, icône | Usage commercial, modifications, attribution, redistribution |
| LIC-AUDIO | Audio et voix | Musique, bruitage, voix synthétique ou enregistrée | Droits voisins, consentement vocal, synchronisation, redistribution |
| LIC-DOC | Documentation | Texte, schéma, capture, tutoriel | Licence éditoriale, citations, captures et extraits |
| LIC-STANDARD | Format ou spécification | Codec, format, protocole | Brevets éventuels, implémentation et distribution |
| LIC-SERVICE | Service et conditions d’utilisation | API ou plateforme distante | Données envoyées, conservation, quotas, droits sur les sorties |

## Statuts de validation

| Statut | Signification |
|---|---|
| `unknown` | Licence absente ou non vérifiée ; composant bloqué pour publication |
| `review-needed` | Licence identifiée mais compatibilité avec le projet non validée |
| `approved-internal` | Utilisation interne autorisée, redistribution non validée |
| `approved-distribution` | Redistribution validée dans le périmètre documenté |
| `restricted` | Utilisation soumise à des conditions particulières |
| `prohibited` | Composant incompatible avec le projet ou sa distribution |
| `deprecated` | Composant retiré ou remplacé, conservé pour traçabilité |

## Fiche de licence

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
id: "LIC-0001"
component: "Nom et version du composant"
category: "LIC-CODE"
license_name: "Nom officiel"
license_identifier: "Identifiant SPDX lorsque disponible"
license_file: "chemin/vers/LICENSE"
source: "référence bibliographique"
status: "review-needed"
allowed_uses:
  - "usage interne"
  - "modification"
restricted_uses:
  - "redistribution non validée"
obligations:
  - "conserver la notice"
commercial_use: "yes | no | conditional | unknown"
redistribution: "yes | no | conditional | unknown"
derivative_works: "yes | no | conditional | unknown"
attribution_required: true
reviewed_on: "AAAA-MM-JJ"
reviewed_by: "personne ou rôle"
notes: "Périmètre et limites"
```

## Compatibilité entre catégories

Une publication doit vérifier au minimum :

1. la licence du dépôt et du code du jeu ;
2. les licences des dépendances distribuées ;
3. les licences des plugins Godot, Blender et ComfyUI ;
4. les licences des modèles et adaptations IA ;
5. les conditions des jeux de données utilisés ;
6. les droits applicables aux assets et aux polices ;
7. les droits musicaux, vocaux et sonores ;
8. les notices et attributions à inclure dans le produit ;
9. les restrictions propres aux plateformes de publication.

## Fichier de notices

Chaque version distribuée devra générer ou fournir un fichier de notices regroupant :

- le nom du composant ;
- sa version ;
- son auteur ou projet ;
- le texte ou la référence de sa licence ;
- l’attribution exigée ;
- l’emplacement du code source lorsque cela est requis ;
- les modifications apportées lorsque la licence l’impose.

## Modèles et contenus générés

Pour chaque modèle IA, conserver séparément :

- la licence du code d’inférence ;
- la licence des poids ;
- la licence des adaptations ou LoRA ;
- les conditions d’usage du jeu de données lorsqu’elles sont connues ;
- les restrictions de redistribution ;
- les obligations d’attribution ;
- les limites concernant les voix, visages ou identités réelles.

La possibilité technique de générer un contenu ne prouve pas que son exploitation est juridiquement autorisée.

## Parcours Solo et Studio

### Mode Solo

- conserver les fichiers de licence avec chaque ressource téléchargée ;
- refuser toute ressource sans origine identifiable ;
- utiliser une fiche simplifiée mais complète avant publication.

### Mode Studio

- centraliser le registre des licences ;
- définir un rôle responsable de la validation ;
- bloquer automatiquement les composants au statut `unknown` ou `prohibited` ;
- conserver les preuves d’achat, autorisations et versions des conditions ;
- inclure la revue des licences dans chaque jalon de publication.

## Checklist de publication

- [ ] Tous les composants distribués figurent dans le registre.
- [ ] Aucun statut `unknown` ne reste dans le périmètre publié.
- [ ] Les licences du code, des poids et des données sont distinguées.
- [ ] Les obligations d’attribution sont satisfaites.
- [ ] Les notices sont intégrées au livrable.
- [ ] Les restrictions commerciales sont compatibles avec la publication.
- [ ] Les voix, visages et données personnelles possèdent les autorisations nécessaires.
- [ ] Les décisions et exceptions sont archivées.
