---
title: "Volume 0 — Chapitre 2 : Les 21 règles fondamentales"
id: "DOC-V0-CH02"
status: "draft"
version: "0.3.0"
language: "fr-FR"
audit-status: "complete"
audit-date: "2026-07-18"
audit-report: "Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md"
audit-level: "static-review"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Volume 0 — Chapitre 2

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).
# Les 21 règles fondamentales du projet

## 1. Objet du chapitre

Ce chapitre formalise les règles normatives applicables à l’ensemble de la collection **Guide IA GameDev**, aux cinq livres, au Volume 0 et au Companion Pack.

Ces règles servent à préserver :

- la cohérence pédagogique ;
- la reproductibilité technique ;
- la maintenabilité documentaire ;
- la compatibilité avec une chaîne de production locale ;
- la lisibilité pour les débutants ;
- l’évolutivité du projet sur plusieurs années.

Toute dérogation devra être documentée dans un **Architecture Decision Record** (ADR) et justifiée par un besoin concret.

---

## 2. Règle 1 — Le guide doit être accessible aux débutants

Le guide doit pouvoir être suivi par une personne disposant de peu ou pas d’expérience en informatique, en développement de jeux ou en intelligence artificielle.

Conséquences :

- chaque terme technique est défini avant sa première utilisation ;
- aucune étape essentielle n’est supposée connue ;
- les commandes sont expliquées ligne par ligne lorsqu’elles sont introduites ;
- les captures, diagrammes et exemples suivent une progression simple vers complexe ;
- les erreurs courantes sont traitées explicitement.

---

## 3. Règle 2 — Le guide adopte une progression strictement pas à pas

Chaque notion doit être introduite dans un ordre logique :

1. contexte ;
2. objectif ;
3. prérequis ;
4. théorie minimale ;
5. procédure ;
6. exemple simple ;
7. exemple avancé ;
8. vérification ;
9. dépannage ;
10. optimisation.

Le lecteur ne doit jamais être renvoyé vers une notion qui n’a pas encore été présentée.

---

## 4. Règle 3 — Le projet fil rouge est unique

Les exemples principaux s’appuient sur un même projet de référence :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Guide-IA-GameDev/
```

Ce projet évolue tout au long des cinq livres. Les exemples isolés restent autorisés, mais ils doivent toujours préciser leur relation avec le projet fil rouge.

---

## 5. Règle 4 — Le pipeline principal doit fonctionner localement

Les composants essentiels doivent pouvoir fonctionner sans dépendre obligatoirement d’un service cloud.

Le fonctionnement local concerne notamment :

- les modèles de langage ;
- la génération d’images ;
- la génération vocale ;
- les bases de données ;
- la production documentaire ;
- le moteur de jeu ;
- les outils d’automatisation.

Les services distants peuvent être présentés uniquement comme alternatives optionnelles.

---

## 6. Règle 5 — Les outils principaux doivent être gratuits

Le parcours principal ne doit exiger aucun abonnement payant.

Lorsqu’un outil gratuit possède aussi une offre commerciale, le guide doit distinguer clairement :

- les fonctions gratuites ;
- les fonctions payantes ;
- les restrictions éventuelles ;
- les alternatives entièrement libres.

---

## 7. Règle 6 — L’open source est privilégié et les exceptions sont signalées

Le guide privilégie les logiciels et modèles open source.

Pour chaque composant, une fiche doit indiquer :

- la licence ;
- le dépôt officiel ;
- les droits d’utilisation ;
- les limitations de redistribution ;
- la possibilité d’usage commercial ;
- le statut open source, source-available ou propriétaire.

Un outil non open source ne peut intégrer le pipeline principal que si aucune alternative viable n’existe et si son statut est explicitement signalé.

---

## 8. Règle 7 — ComfyUI est l’interface graphique principale pour l’image

ComfyUI constitue l’interface officielle du pipeline de génération graphique.

Les autres interfaces sont présentées dans un chapitre comparatif, mais elles ne doivent pas créer de doublons dans le parcours principal.

Le guide doit couvrir :

- workflows ;
- modèles ;
- LoRA ;
- ControlNet et équivalents ;
- upscale ;
- cohérence de personnages ;
- génération de textures et références 3D ;
- optimisation AMD et ZLUDA.

---

## 9. Règle 8 — Open WebUI est la plateforme centrale des LLM

Open WebUI est présenté comme l’interface et la plateforme d’orchestration principale pour :

- Ollama ;
- llama.cpp ;
- LocalAI ;
- les modèles compatibles avec une API de type OpenAI ;
- Knowledge et RAG ;
- Workspaces ;
- Pipelines ;
- Open Terminal ;
- Vane ;
- outils et fonctions locales.

LibreChat reste une interface alternative et comparative.

---

## 10. Règle 9 — Godot est le moteur de jeu principal

Tous les systèmes de gameplay, l’intégration des assets, les interfaces, le réseau, la sauvegarde et l’export sont développés prioritairement avec Godot.

Unity et Unreal peuvent apparaître dans des comparatifs, mais ils ne doivent pas fragmenter le pipeline pédagogique principal.

---

## 11. Règle 10 — Blender est l’outil 3D principal

Blender est utilisé pour :

- modélisation ;
- sculpture ;
- UV ;
- matériaux ;
- rigging ;
- animation ;
- retopologie ;
- baking ;
- LOD ;
- export glTF/GLB vers Godot.

Les outils spécialisés externes sont classés comme recommandés ou optionnels selon leur rôle.

---

## 12. Règle 11 — La configuration matérielle de référence doit être respectée

Le guide est optimisé en priorité pour :

| Composant | Référence |
|---|---|
| GPU | AMD Radeon RX 6750 XT |
| VRAM | 12 Go |
| CPU | AMD Ryzen 7 2700, 8 cœurs |
| RAM | 32 Go |
| Système principal | Windows |
| Accélération ComfyUI | ZLUDA lorsque compatible |
| Conteneurisation | Docker Desktop |

Chaque chapitre technique doit préciser :

- la consommation CPU, RAM et VRAM ;
- les réglages adaptés ;
- les limites observables ;
- les solutions de repli CPU ;
- les variantes pour d’autres configurations lorsqu’elles sont pertinentes.

---

## 13. Règle 12 — Les architectures doivent être modulaires

Chaque système doit limiter son couplage aux autres systèmes.

Le guide privilégie :

- la composition ;
- les scènes autonomes ;
- les signaux ;
- les services clairement définis ;
- les données séparées de la logique ;
- les interfaces stables ;
- les dépendances explicites.

Les architectures excessivement complexes doivent être signalées et justifiées.

---

## 14. Règle 13 — Les douze grands systèmes utilisent une fiche standardisée

Les douze systèmes sont :

1. Personnages ;
2. Relations sociales ;
3. Famille ;
4. Agents IA ;
5. Combat ;
6. Compétences et pouvoirs ;
7. Inventaire et réputation des objets ;
8. Économie ;
9. Monde vivant et simulation écologique ;
10. Politique, factions et justice ;
11. Construction et colonies ;
12. Narration, quêtes, codex et encyclopédie.

Chaque fiche doit contenir au minimum :

- objectif ;
- architecture logicielle ;
- architecture Godot ;
- JSON ;
- SQLite ;
- ressources Godot ;
- intégration IA ;
- arborescence ;
- scripts GDScript ;
- UML ;
- flux de données ;
- exemples ;
- erreurs fréquentes ;
- bonnes pratiques ;
- optimisation matérielle ;
- tests ;
- checklist.

---

## 15. Règle 14 — Une seule source de vérité doit exister

Le Markdown est la source documentaire officielle.

Les formats suivants sont générés à partir de cette source :

- PDF ;
- HTML ;
- DOCX ;
- EPUB lorsque prévu.

Les informations techniques ne doivent pas être maintenues séparément dans plusieurs fichiers sans mécanisme automatique de synchronisation.

---

## 16. Règle 15 — Aucun doublon documentaire non justifié

Une notion complexe doit posséder un chapitre de référence unique.

Les autres chapitres utilisent :

- une synthèse courte ;
- un identifiant stable ;
- une référence croisée ;
- un lien relatif.

Les répétitions utiles à la pédagogie restent possibles lorsqu’elles sont explicitement présentées comme rappel.

---

## 17. Règle 16 — Tous les exemples doivent être reproductibles

Un exemple technique doit fournir :

- les prérequis ;
- les versions des outils ;
- les fichiers nécessaires ;
- les commandes exactes ;
- le résultat attendu ;
- une procédure de vérification ;
- les erreurs possibles.

Un exemple non testé doit être marqué comme expérimental.

---

## 18. Règle 17 — Chaque ressource possède un identifiant stable

Les identifiants ne dépendent pas des numéros de page.

Exemples :

- `DOC-V0-CH02` : chapitre documentaire ;
- `GDS-001` : script GDScript ;
- `PY-001` : script Python ;
- `SQL-001` : schéma ou script SQL ;
- `JSON-001` : structure JSON ;
- `WF-CFY-001` : workflow ComfyUI ;
- `UML-001` : diagramme UML ;
- `CHK-001` : checklist ;
- `TMP-001` : modèle de document.

Les identifiants restent inchangés lors des réorganisations éditoriales.

---

## 19. Règle 18 — Les modes Solo et Studio sont transversaux

Chaque chapitre doit préciser les différences entre :

### Mode Solo

- automatisation maximale ;
- périmètre réduit ;
- compromis réalistes ;
- procédures simplifiées ;
- priorités pour un développeur indépendant.

### Mode Studio

- travail collaboratif ;
- branches Git ;
- revues ;
- responsabilités ;
- validation des assets ;
- CI/CD ;
- documentation partagée.

Ces modes ne constituent pas deux guides séparés.

---

## 20. Règle 19 — Chaque procédure est classée par priorité

Le guide doit distinguer explicitement :

| Niveau | Signification |
|---|---|
| **Obligatoire** | Indispensable pour suivre le pipeline principal. |
| **Recommandé** | Améliore fortement la qualité, la sécurité ou la productivité. |
| **Optionnel** | Répond à un besoin avancé, spécialisé ou alternatif. |

Le statut doit être visible au début des sections importantes.

---

## 21. Règle 20 — Les performances sont mesurées avant optimisation

Le guide ne doit pas recommander une optimisation uniquement sur la base d’une intuition.

La méthode officielle est :

1. mesurer ;
2. identifier le goulet d’étranglement ;
3. modifier un paramètre ;
4. mesurer à nouveau ;
5. documenter le résultat ;
6. conserver ou annuler le changement.

Les benchmarks doivent préciser leur environnement matériel et logiciel.

---

## 22. Règle 21 — La qualité, la sécurité et la conformité sont intégrées dès la conception

Chaque partie du guide doit tenir compte, selon le contexte, de :

- la validation des entrées ;
- la sécurité des services locaux ;
- les permissions Docker ;
- la protection des sauvegardes ;
- la gestion des secrets ;
- les licences des modèles et assets ;
- la confidentialité ;
- les tests ;
- l’accessibilité ;
- la compatibilité des versions ;
- les procédures de restauration.

La qualité n’est pas une étape ajoutée à la fin du projet : elle accompagne tout le cycle de production.

---

## 23. Application des règles aux contenus destinés aux adultes

Le guide peut traiter des contraintes techniques propres à un jeu destiné exclusivement à des adultes, par exemple :

- classification et signalement du contenu ;
- consentement entre personnages adultes ;
- personnalisation des corps adultes ;
- animation, rigging, collisions et effets visuels ;
- interfaces de configuration et filtres de contenu ;
- sauvegarde des préférences ;
- séparation des assets explicites ;
- contrôle de l’âge et avertissements ;
- conformité aux licences et aux plateformes de distribution.

Ces contenus doivent rester clairement limités à des personnages adultes et respecter les exigences légales, éthiques et de distribution applicables.

---

## 24. Gestion des exceptions

Une exception à une règle doit indiquer :

- la règle concernée ;
- le problème rencontré ;
- les solutions alternatives étudiées ;
- la décision retenue ;
- ses conséquences ;
- sa date ;
- son auteur ;
- la version concernée.

Les exceptions durables sont enregistrées dans un ADR.

---

## 25. Checklist de validation du chapitre

- [x] Les 21 règles sont formalisées.
- [x] Les statuts Obligatoire, Recommandé et Optionnel sont définis.
- [x] Les modes Solo et Studio sont intégrés.
- [x] La configuration AMD de référence est fixée.
- [x] Les outils principaux du pipeline sont fixés.
- [x] Les exigences de reproductibilité et de qualité sont définies.
- [x] Le traitement des contenus destinés aux adultes est encadré.
- [x] Une procédure d’exception est prévue.

---

## 26. Références croisées

- `DOC-V0-CH01` — Vision générale du projet.
- `DOC-V0-CH03` — Architecture documentaire.
- `DOC-V0-CH04` — Convention des identifiants.
- `DOC-V0-CH05` — Conventions Markdown et Pandoc.
- `DOC-V0-ADR` — Historique des décisions d’architecture.

---

## 27. Ressources du Companion Pack associées

- `TMP-DOC-001` — Modèle universel de chapitre.
- `TMP-ADR-001` — Modèle d’Architecture Decision Record.
- `CHK-DOC-001` — Checklist documentaire générale.
- `CHK-LIC-001` — Checklist des licences.

---

**Fin de `DOC-V0-CH02`.**
