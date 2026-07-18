---
title: "Annexe — Bibliographie"
id: "DOC-V0-ANN-BIBLIOGRAPHIE"
status: "in-progress"
version: "0.1.0"
---

# Bibliographie

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](CONVENTION-OUTILS-ET-CONTEXTES.md).

Cette annexe décrit le registre bibliographique de la collection. Elle privilégie les sources primaires, officielles, versionnées et consultables sans ambiguïté.

## Hiérarchie des sources

1. Documentation officielle d’un projet, d’un éditeur ou d’un standard.
2. Dépôt source officiel, notes de version et tickets maintenus par le projet.
3. Publication scientifique ou spécification technique primaire.
4. Documentation d’un distributeur ou intégrateur reconnu.
5. Article technique secondaire, uniquement lorsqu’aucune source primaire suffisante n’existe.
6. Forum, vidéo ou message communautaire, utilisé comme piste et jamais comme unique fondement d’une règle normative.

## Format d’une référence

Chaque référence stable doit contenir les champs suivants :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
id: REF-0001
title: "Titre de la ressource"
author_or_project: "Projet ou auteur"
source_type: "official-docs | repository | release-notes | paper | standard | secondary"
url: "https://..."
version: "version concernée ou rolling"
accessed: "AAAA-MM-JJ"
language: "fr | en | autre"
scope:
  - "chapitre ou domaine concerné"
notes: "Limites, archivage ou conditions particulières"
```

## Registre des sources de base

Les entrées ci-dessous identifient les familles de sources à maintenir. Les versions, dates d’accès et pages précises seront renseignées au moment de la rédaction technique des livres concernés.

| ID | Projet ou organisme | Source primaire attendue | Domaine couvert | Statut |
|---|---|---|---|---|
| REF-0001 | Godot Engine | Documentation officielle, dépôt et notes de version | Moteur de jeu, GDScript, export, performances | À compléter dans le Livre II |
| REF-0002 | Blender Foundation | Manuel officiel, API Python et notes de version | Modélisation, animation, rendu, automatisation | À compléter dans le Livre III |
| REF-0003 | ComfyUI | Dépôt officiel, documentation et registre des dépendances | Workflows visuels et exécution locale | À compléter dans le Livre I |
| REF-0004 | Open WebUI | Documentation, dépôt et notes de version | Interface locale, outils et administration | À compléter dans le Livre I |
| REF-0005 | Docker | Documentation officielle et spécification Compose | Conteneurs, réseaux et volumes | À compléter dans le Livre I |
| REF-0006 | Python | Documentation officielle et PEP applicables | Scripts, environnements et automatisation | À compléter transversalement |
| REF-0007 | Git | Documentation officielle | Versionnement et collaboration | À compléter transversalement |
| REF-0008 | Pandoc | Manuel officiel | Compilation Markdown, PDF, HTML et DOCX | Actif pour l’infrastructure documentaire |
| REF-0009 | FFmpeg | Documentation officielle | Traitement audio et vidéo | À compléter dans les Livres I et III |
| REF-0010 | Ollama | Documentation et dépôt officiels | Exécution de modèles de langage locaux | À compléter dans le Livre I |
| REF-0011 | llama.cpp | Dépôt, documentation et formats supportés | Inférence locale et quantification | À compléter dans le Livre I |
| REF-0012 | LocalAI | Documentation et dépôt officiels | API locale compatible avec plusieurs familles de modèles | À compléter dans le Livre I |
| REF-0013 | LibreChat | Documentation et dépôt officiels | Interface et orchestration alternatives | À compléter dans le Livre I |
| REF-0014 | Chatterbox, Kokoro et Piper | Dépôts et documentations officielles | Synthèse vocale locale | À compléter dans le Livre I |
| REF-0015 | Whisper et Faster-Whisper | Publications, dépôts et documentation | Transcription et traitement vocal | À compléter dans le Livre I |
| REF-0016 | MusicGen et AudioGen | Publication et dépôt officiels | Génération musicale et sonore | À compléter dans le Livre III |
| REF-0017 | AMD | Documentation pilotes et technologies GPU | Compatibilité matérielle et performances | À compléter dans le Livre I |
| REF-0018 | ZLUDA | Dépôt et documentation officiels | Couche de compatibilité GPU | À compléter dans le Livre I |
| REF-0019 | Khronos Group | Spécifications officielles | Vulkan, glTF et formats graphiques | À compléter selon les chapitres |
| REF-0020 | W3C, IETF et organismes de normalisation pertinents | Standards publiés | Web, réseau, formats et accessibilité | À compléter selon les chapitres |

## Citations dans les chapitres

Une affirmation dépendante d’une version, d’un comportement logiciel ou d’une règle juridique doit renvoyer vers une référence identifiable. La citation doit être placée au plus près de l’affirmation et préciser, lorsque nécessaire, la version testée.

Exemple :

> **[LECTURE] Exemple ou structure de référence - Ne pas saisir.**

```text
Cette procédure a été validée avec la version X.Y de l’outil [REF-0003].
```

## Archivage

Pour les publications stables :

- conserver la date d’accès ;
- indiquer la version ou le commit lorsque la documentation est évolutive ;
- privilégier une URL pérenne ou archivée ;
- conserver localement les licences nécessaires à la redistribution ;
- signaler les liens morts comme anomalies documentaires.

## Checklist de validation

- [ ] Chaque source normative possède un identifiant unique.
- [ ] La source primaire est privilégiée.
- [ ] La version ou la date d’accès est indiquée.
- [ ] Les affirmations sensibles sont reliées à une source.
- [ ] Les licences et conditions de redistribution sont contrôlées séparément.
- [ ] Les liens sont vérifiés avant publication stable.
