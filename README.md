# Guide IA GameDev

> Guide open source de développement de jeux 3D réalistes avec intelligence artificielle locale.

[![Statut](https://img.shields.io/badge/statut-en%20construction-orange)](#état-du-projet)
[![Documentation](https://img.shields.io/badge/source-Markdown-000000?logo=markdown)](#formats-de-publication)
[![Moteur](https://img.shields.io/badge/moteur-Godot-478CBF?logo=godot-engine&logoColor=white)](#pile-technologique-principale)
[![3D](https://img.shields.io/badge/3D-Blender-F5792A?logo=blender&logoColor=white)](#pile-technologique-principale)
[![IA locale](https://img.shields.io/badge/IA-locale-4C8BF5)](#principes-fondamentaux)

## Présentation

**Guide IA GameDev** est un projet documentaire en français consacré à la conception, au développement, à la production, aux tests, à l’optimisation, à la publication et à la maintenance d’un jeu vidéo 3D réaliste au moyen d’outils gratuits, locaux et majoritairement open source.

La documentation est destinée en priorité aux personnes disposant de peu ou pas d’expérience en informatique ou en développement de jeux. Elle suit une progression pas à pas, tout en proposant une architecture suffisamment structurée pour accompagner un projet indépendant de grande ampleur.

Le guide est rédigé en Markdown. Les versions PDF, HTML et autres formats de diffusion sont générées à partir de cette source unique.

## Objectifs

Le projet doit permettre au lecteur de :

- préparer une plateforme locale de création assistée par IA ;
- apprendre les bases de Godot, GDScript, Blender, Python, JSON et SQLite ;
- produire des images, textures, modèles 3D, animations, voix, bruitages et musiques ;
- concevoir des personnages, des mondes vivants et des systèmes de gameplay modulaires ;
- connecter Godot à des services IA locaux ;
- tester, optimiser, versionner et publier le jeu ;
- maintenir le projet et ses données sur le long terme.

## Principes fondamentaux

Le dépôt applique les principes suivants :

1. **Local par défaut** : le pipeline principal doit fonctionner sans service cloud obligatoire.
2. **Gratuit et open source autant que possible** : toute exception doit être identifiée et justifiée.
3. **Source unique en Markdown** : le PDF est un format de publication, non la source éditoriale.
4. **Projet fil rouge** : les chapitres participent à la construction progressive d’un même projet.
5. **Architecture modulaire** : les composants doivent rester compréhensibles, remplaçables et faiblement couplés.
6. **Reproductibilité** : les procédures, versions et paramètres doivent être documentés.
7. **Priorités explicites** : chaque élément est classé comme obligatoire, recommandé ou optionnel.
8. **Deux parcours de lecture** : un parcours pour développeur solo et un parcours pour équipe ou studio.
9. **Compatibilité matérielle documentée** : les limites et réglages sont adaptés à la configuration de référence.
10. **Contrôle qualité continu** : chaque procédure doit être vérifiée sous les angles technique, documentaire et pratique.

Les règles complètes seront définies dans le Volume 0.

## Configuration matérielle de référence

| Composant | Référence principale |
|---|---|
| Système | Windows, avec compléments Linux lorsque pertinents |
| GPU | AMD Radeon RX 6750 XT |
| VRAM | 12 Go |
| CPU | AMD Ryzen 7 2700, 8 cœurs |
| RAM | 32 Go |
| ComfyUI | Exécution AMD avec ZLUDA lorsque nécessaire |
| Conteneurs | Docker Desktop et Docker Compose |

Cette configuration sert de référence aux tests et aux optimisations. Le guide intégrera également des profils matériels alternatifs.

## Pile technologique principale

| Domaine | Outils principaux |
|---|---|
| Moteur de jeu | Godot Engine, GDScript |
| Modélisation 3D | Blender |
| Génération visuelle | ComfyUI |
| Interface LLM | Open WebUI |
| Exécution LLM | Ollama, llama.cpp, LocalAI |
| Interface alternative LLM | LibreChat |
| Production vocale | Voicebox, Chatterbox, Kokoro, Piper |
| Transcription | Whisper, Faster-Whisper |
| Musique et sons génératifs | MusicGen, AudioGen |
| Données | JSON, SQLite, base vectorielle locale |
| Infrastructure | Docker, Docker Compose, Git, Python, VS Code |
| Automatisation interactive | Open Terminal et Vane dans l’écosystème Open WebUI |

La présence d’un outil dans cette liste ne signifie pas qu’il est obligatoire. Le Volume 0 et chaque chapitre distingueront les éléments obligatoires, recommandés et optionnels.

## Organisation de la collection

La collection se compose d’un volume normatif, de cinq livres et d’un Companion Pack.

### Volume 0 — Fondation documentaire

Définit les règles éditoriales et techniques communes : conventions, identifiants, arborescence, compatibilité, formats, qualité et génération des publications.

### Livre I — Préparer la plateforme de développement IA

Installation et configuration du matériel, de Docker, des services IA locaux, de ComfyUI et des outils audio.

### Livre II — Développement du jeu et plateforme IA

Godot, architecture logicielle, systèmes de gameplay, bases de données, communication avec les IA locales et industrialisation du projet.

### Livre III — Production des contenus et des assets

Préproduction, personnages, humanoïdes, animaux, créatures, environnements, objets, matériaux, animations, effets visuels, interfaces, audio et intégration dans Godot.

### Livre IV — Finalisation, optimisation, publication et maintenance

Équilibrage, assurance qualité, tests, diagnostic, performances, multijoueur, DevOps, export, distribution, accessibilité et maintenance à long terme.

### Livre V — Encyclopédie technique et bibliothèque de référence

Fiches normalisées, arbres de décision, workflows, prompts, scripts, données, architectures, erreurs fréquentes, comparatifs, checklists et index croisés.

### Companion Pack

Projets modèles, scripts, schémas de bases, structures JSON, Docker Compose, workflows ComfyUI, modèles documentaires, tests et autres ressources directement réutilisables.

## Arborescence cible

```text
Guide-IA-GameDev/
├── README.md
├── LICENSE.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── STYLE_GUIDE.md
├── BUILD.md
├── ROADMAP.md
├── metadata.yaml
├── contents.txt
├── build.ps1
├── build.sh
├── Volume-0/
├── Livre-I/
├── Livre-II/
├── Livre-III/
├── Livre-IV/
├── Livre-V/
├── Companion-Pack/
├── assets/
├── templates/
└── output/
```

Les dossiers seront ajoutés progressivement. Git ne versionnant pas les dossiers vides, chaque dossier documentaire contiendra un fichier `index.md`.

## Parcours de lecture

### Mode Solo

Le parcours Solo identifie les raccourcis, les automatisations prioritaires et les éléments qui peuvent être reportés ou simplifiés par un développeur indépendant.

### Mode Studio

Le parcours Studio ajoute les pratiques collaboratives : branches, revues, responsabilités, validation des contenus, CI/CD, documentation partagée et conventions d’équipe.

## Formats de publication

Les sources seront maintenues en Markdown UTF-8. Les formats de diffusion prévus sont :

- PDF ;
- HTML ;
- EPUB ;
- DOCX, lorsque nécessaire ;
- archives du Companion Pack.

La génération sera automatisée avec Pandoc et des scripts PowerShell et Bash.

## État du projet

Le projet est en phase d’amorçage documentaire.

| Jalon | État |
|---|---|
| M0 — Infrastructure documentaire | En cours |
| M1 — Volume 0 | À faire |
| M2 — Livre I | À faire |
| M3 — Livre II | À faire |
| M4 — Livre III | À faire |
| M5 — Livre IV | À faire |
| M6 — Livre V | À faire |
| M7 — Companion Pack | À faire |
| M8 — Publications PDF/HTML/EPUB | À faire |
| M9 — Version 1.0 | À faire |

## Contributions

Le dépôt sera ouvert aux contributions après stabilisation du Volume 0. Les règles de contribution seront précisées dans `CONTRIBUTING.md` et `STYLE_GUIDE.md`.

## Licence

La licence du texte, du code d’exemple et des ressources du Companion Pack sera précisée dans `LICENSE.md`. Les composants tiers conserveront leurs propres licences, qui devront être recensées et respectées individuellement.

## Avertissement sur les informations évolutives

Les logiciels, modèles et pilotes évoluent rapidement. Les chapitres devront indiquer les versions vérifiées, la date de validation et les éventuelles incompatibilités connues. Une procédure de mise à jour et de révision régulière sera définie dans le Volume 0 et le Livre IV.
