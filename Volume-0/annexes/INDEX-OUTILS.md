---
title: "Annexe — Index des outils"
id: "DOC-V0-ANN-INDEX-OUTILS"
status: "in-progress"
version: "0.1.0"
---

# Index des outils

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](CONVENTION-OUTILS-ET-CONTEXTES.md).

Cet index répertorie les outils principaux, leurs rôles dans le guide et l’emplacement prévu de leur documentation détaillée.

## Outils principaux

| Outil | Rôle dans le projet | Priorité | Documentation principale prévue |
|---|---|---|---|
| Godot | Moteur de jeu, architecture, scripting, export et profilage | Obligatoire | Livre II, puis Livre IV |
| Blender | Modélisation, rig, animation, matériaux, préparation et automatisation des assets | Obligatoire | Livre III |
| ComfyUI | Workflows de génération et de traitement visuel local | Obligatoire pour le parcours image IA | Livre I et Livre III |
| Open WebUI | Interface centrale pour les modèles locaux et certains outils | Recommandé | Livre I et Livre II |
| Docker | Isolation et déploiement reproductible des services | Recommandé | Livre I |
| Docker Compose | Orchestration locale de plusieurs services | Recommandé | Livre I |
| Git | Versionnement du code et de la documentation | Obligatoire | Livre I et Livre IV |
| VS Code | Édition du code, du Markdown et des configurations | Recommandé | Livre I |
| Python | Automatisation, validation, conversion et intégration IA | Obligatoire pour les scripts compagnon | Livres I à IV |
| Pandoc | Compilation des sources Markdown en livrables | Obligatoire pour la documentation | Volume 0 et Livre IV |

## Modèles de langage et interfaces

| Outil | Usage | Statut dans le guide |
|---|---|---|
| Ollama | Exécution simplifiée de modèles locaux | Recommandé |
| llama.cpp | Inférence locale, quantification et contrôle avancé | Recommandé |
| LocalAI | Service local compatible avec plusieurs familles de modèles | Optionnel |
| LibreChat | Interface alternative ou complémentaire | Optionnel |
| Open Terminal | Accès encadré aux commandes depuis l’environnement central | Recommandé avec permissions limitées |
| Vane | Extension ou composant d’orchestration associé à Open WebUI | Optionnel selon compatibilité vérifiée |

## Audio et voix

| Outil | Usage | Statut dans le guide |
|---|---|---|
| Voicebox | Interface de gestion ou d’expérimentation vocale locale | Recommandé selon disponibilité |
| Chatterbox | Synthèse vocale locale | Optionnel |
| Kokoro | Synthèse vocale locale légère | Recommandé |
| Piper | Synthèse vocale locale rapide | Recommandé |
| Whisper | Reconnaissance et transcription vocale | Recommandé |
| Faster-Whisper | Variante optimisée de transcription | Recommandé |
| MusicGen | Génération musicale | Optionnel |
| AudioGen | Génération d’effets et ambiances sonores | Optionnel |
| Audacity | Édition audio simple | Recommandé |
| Ardour | Production audio multipiste | Optionnel |
| FFmpeg | Conversion, normalisation et automatisation audio/vidéo | Obligatoire pour plusieurs pipelines |

## Données, diagnostic et production

| Outil ou famille | Usage | Statut |
|---|---|---|
| SQLite | Données locales, prototypes et index | Recommandé |
| PostgreSQL | Données partagées ou services Studio | Optionnel |
| PowerShell | Installation et automatisation Windows | Obligatoire pour le parcours Windows |
| Bash | Automatisation Linux et environnements compatibles | Recommandé |
| Mermaid | Diagrammes intégrés au Markdown | Recommandé |
| GitHub | Hébergement, suivi, revue et publication du dépôt | Recommandé |

## Fiche d’outil obligatoire

Tout outil documenté en profondeur doit préciser :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
name: "Nom"
role: "Rôle principal"
priority: "required | recommended | optional"
license: "Licence ou référence du registre"
validated_versions:
  - "X.Y"
platforms:
  - "Windows"
hardware_profiles:
  - "H2"
installation: "Référence de procédure"
configuration: "Référence de configuration"
validation: "Test de bon fonctionnement"
fallbacks:
  - "Solution de repli"
```

## Règles de maintenance

- Ne pas présenter un outil comme obligatoire lorsqu’une alternative libre et maintenue remplit le même rôle.
- Distinguer l’outil principal des variantes et solutions de repli.
- Documenter la version réellement testée.
- Vérifier licence, activité du projet et compatibilité matérielle avant promotion.
- Signaler les outils abandonnés, non maintenus ou remplacés.

## Checklist

- [ ] Chaque outil cité dans les livres apparaît dans cet index.
- [ ] Son rôle et sa priorité sont explicites.
- [ ] Sa licence est reliée à l’index des licences.
- [ ] La version validée est enregistrée dans la matrice de compatibilité.
- [ ] Une solution de repli est proposée pour les composants critiques.
