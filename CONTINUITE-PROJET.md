---
title: "Continuité du projet Guide IA GameDev"
id: "DOC-PROJECT-CONTINUITY"
status: "active"
version: "1.0.0"
lang: "fr-FR"
last-updated: "2026-07-18"
update-policy: "mandatory-on-every-project-change"
---

# Continuité du projet Guide IA GameDev

> **Document de reprise prioritaire.** Ce fichier résume les décisions, l’historique, l’état du dépôt, les règles permanentes et la prochaine action. Il doit permettre de reprendre le projet dans une nouvelle conversation sans recommencer la conception depuis zéro.

> **Règle obligatoire :** toute modification fonctionnelle, documentaire, structurelle, éditoriale, technique ou QA du projet doit mettre à jour ce fichier dans le même lot de commits ou la même pull request.

## 1. Mode d’emploi lors d’une reprise

Lorsqu’une nouvelle conversation commence :

1. lire entièrement `CONTINUITE-PROJET.md` ;
2. lire `ROADMAP.md`, `contents.txt` et l’index du Livre actif ;
3. vérifier les derniers commits et pull requests fusionnés ;
4. ne pas recréer un chapitre ou une décision déjà présente ;
5. continuer depuis la section **Prochaine action** ;
6. actualiser ce fichier avant de déclarer le nouveau lot terminé.

Ce document est un résumé opérationnel de la conversation. Il ne reproduit pas mot pour mot tous les dialogues, mais conserve les informations nécessaires pour poursuivre le travail fidèlement.

## 2. Demande et vision du projet

Laurent Collin souhaite produire un guide français très complet permettant à un débutant de concevoir et développer un jeu vidéo 3D réaliste avec :

- Godot et GDScript ;
- Blender ;
- Python, JSON, SQLite et mémoire vectorielle ;
- IA locale pour les textes, images, voix, sons et musiques ;
- outils gratuits, locaux et majoritairement open source ;
- procédures reproductibles et adaptées à une station Windows avec GPU AMD ;
- deux parcours : développeur Solo et équipe/Studio ;
- un projet fil rouge nommé `Project Asteria` ;
- une collection comprenant un Volume 0, cinq Livres et un Companion Pack.

Le guide ne doit pas seulement donner des commandes ou du code. Il doit expliquer clairement :

- quel programme ouvrir ;
- où créer ou modifier un fichier ;
- où exécuter une commande ;
- ce que signifie chaque élément important du code ;
- le résultat attendu ;
- comment vérifier et corriger les erreurs.

## 3. Configuration matérielle de référence

- Système : Windows.
- GPU : AMD Radeon RX 6750 XT, 12 Go de VRAM, architecture RDNA2.
- CPU : AMD Ryzen 7 2700, 8 cœurs, 3,2 GHz.
- RAM : 32 Go.
- ComfyUI : installation Windows avec voie ZLUDA expérimentale lorsque pertinente.
- Docker Desktop : utilisé pour les services CPU et les interfaces ; les charges GPU AMD restent principalement natives sur Windows.
- Éditeur principal : Visual Studio Code.
- Terminal Windows principal : PowerShell 7.

## 4. Architecture de la collection

### Volume 0 — Fondation documentaire

Terminé et audité. Il contient notamment :

1. Vision générale du projet.
2. Les 21 règles fondamentales.
3. Architecture documentaire.
4. Convention des identifiants.
5. Conventions Markdown et Pandoc.
6. Style rédactionnel.
7. Standards techniques.
8. Standards IA.
9. Politique de compatibilité.
10. Production, validation et publication.
11. Glossaire, bibliographie et index.

Annexes et QA importantes :

- `Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md` ;
- `Volume-0/QA/AUDIT-VOLUME-0-LIVRE-I.md` ;
- `Volume-0/QA/VALIDATION-FINALE-V0-L1.yaml`.

### Livre I — Préparer la plateforme de développement IA

Terminé, corrigé, repéré et audité avec dix chapitres :

1. Matériel, Windows, pilotes AMD et accélération locale.
2. Terminal, PowerShell et outils Windows.
3. Git, GitHub et Visual Studio Code.
4. Python et environnements virtuels.
5. Docker et Docker Compose.
6. Open WebUI, Open Terminal et Vane.
7. ComfyUI et workflows graphiques.
8. LLM locaux : Ollama, llama.cpp, LocalAI et LibreChat.
9. Audio IA local : voix, transcription, musique et effets.
10. Sécurité, sauvegarde et validation de la plateforme.

Décision historique importante : le Livre I avait d’abord été condensé en six chapitres. Après vérification du plan initial, quatre chapitres de fondation ont été ajoutés. Les cinq chapitres historiques déplacés ont conservé leurs identifiants stables grâce aux métadonnées de migration.

### Livre II — Développement du jeu et plateforme IA

En cours. Plan maître : 30 chapitres répartis entre :

- 9 chapitres de fondations Godot, architecture et données ;
- 4 chapitres de plateforme IA locale ;
- 12 grands systèmes de gameplay ;
- 5 chapitres d’industrialisation.

Chapitres actuellement rédigés :

1. `Livre-II/CHAPITRE-01-Decouvrir-Godot-et-creer-le-projet-fil-rouge.md`
2. `Livre-II/CHAPITRE-02-Fondamentaux-de-GDScript.md`

Le chapitre 2 est actuellement en version `1.3.0`, avec explications détaillées des symboles, types, fonctions, paramètres, arguments, retours, collections et boucles.

### Livres III à V et Companion Pack

Leurs domaines sont définis dans `ROADMAP.md` et les index correspondants. Ils ne sont pas encore rédigés.

## 5. Système obligatoire des contextes d’utilisation

Chaque bloc de commande, code, configuration, sortie ou structure doit indiquer le programme et l’action à effectuer.

Repères normatifs :

| Repère | Contexte |
|---|---|
| `[PS]` | PowerShell 7 sur Windows |
| `[CMD]` | Invite de commandes Windows |
| `[WSL]` | Terminal WSL/Bash |
| `[DCT]` | Terminal dans un conteneur Docker |
| `[DCK]` | Interface Docker Desktop |
| `[VSC]` | Visual Studio Code |
| `[WEB]` | Navigateur internet |
| `[APP]` | Interface graphique du logiciel nommé |
| `[SORTIE]` | Résultat à lire, ne pas saisir |
| `[LECTURE]` | Exemple ou structure de référence |

Forme attendue :

```text
[CODE] Outil - Action : chemin, cible ou précision utile
```

Exemples :

```text
[PS] PowerShell 7 - Exécuter
winget install --id Git.Git --exact --source winget
```

```text
[VSC] Visual Studio Code - Créer : .vscode/settings.json
{
  "files.encoding": "utf8"
}
```

La CI contrôle la présence et la cohérence sémantique de ces repères.

## 6. Règle permanente d’audit après création

Aucun chapitre ne doit être déclaré terminé immédiatement après sa rédaction.

Séquence obligatoire :

1. rédaction ;
2. comparaison au sommaire maître ;
3. audit de complétude pédagogique ;
4. contrôle des doublons ;
5. vérification technique des commandes et exemples ;
6. ajout des contextes d’utilisation ;
7. correction des omissions ;
8. mise à jour de `contents.txt`, de l’index et de `ROADMAP.md` ;
9. compilation Pandoc/XeLaTeX ;
10. inspection du PDF ;
11. rapport QA et preuve indépendante ;
12. mise à jour de `CONTINUITE-PROJET.md` ;
13. seulement ensuite : chapitre déclaré rédigé, repéré et audité.

Les métadonnées attendues comprennent notamment :

```yaml
status: "reviewed"
audit-status: "complete"
audit-date: "YYYY-MM-DD"
audit-level: "static-review"
audit-report: "chemin/du/rapport.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
```

Le niveau `runtime-tested` ne doit être utilisé qu’après exécution réelle des exemples dans un projet matérialisé.

## 7. Règle pédagogique pour le code

Lors de la première apparition d’une syntaxe ou d’un concept, expliquer chaque élément important :

- mot-clé ;
- nom de variable ou fonction ;
- type ;
- opérateur ;
- paramètre et argument ;
- valeur par défaut ;
- valeur et type de retour ;
- portée ;
- accès par index ou clé ;
- appel de méthode ;
- résultat concret.

Exemple traité dans le chapitre 2 :

```gdscript
for key: StringName in metrics:
	print("%s = %s" % [key, metrics[key]])
```

Le texte explique désormais `for`, `key`, `StringName`, `metrics`, `metrics[key]`, les deux `%s`, l’opérateur `%`, le tableau de valeurs et un résultat concret.

Autre exemple traité :

```gdscript
var target: Node3D
var camera: Camera3D
var report: BootstrapReport
```

Le texte explique `var`, les noms choisis, l’annotation `:`, les classes natives, la classe personnalisée, l’héritage et la valeur initiale `null`.

Les rappels pédagogiques sont autorisés lorsqu’un nouvel exemple combine les concepts différemment. Les duplications intégrales involontaires de titres, paragraphes longs ou blocs significatifs sont interdites.

## 8. Audit actuel du chapitre 2 GDScript

La dernière campagne fusionnée est la PR n°11 :

- titre : `docs(livre-ii): audit duplicates and deepen GDScript functions` ;
- commit de référence : `e40da615bdc922f0296ef34f51dc6e226f0782dd` ;
- 152 titres contrôlés ;
- 57 blocs de code significatifs contrôlés ;
- 22 paragraphes longs contrôlés ;
- zéro titre dupliqué ;
- zéro bloc significatif dupliqué ;
- zéro paragraphe long dupliqué ;
- zéro explication pédagogique obligatoire manquante ;
- 829 blocs sur 829 repérés ;
- zéro incohérence sémantique ;
- PDF A4 1.5 de 512 pages ;
- réserve runtime maintenue jusqu’à la matérialisation de `Project Asteria`.

La PR n°12 a été fermée sans fusion, car son mécanisme temporaire n’avait pas appliqué les changements et était devenu redondant après la fusion de la PR n°11.

## 9. QA, compilation et preuves

Principes :

- Markdown = source unique ;
- compilation avec Pandoc et XeLaTeX ;
- vérification structurelle, métadonnées, identifiants et liens ;
- extraction du texte du PDF ;
- contrôle des polices et caractéristiques techniques ;
- inspection visuelle d’un échantillon de pages ;
- preuves finales externalisées en YAML pour éviter l’auto-référence des rapports compilés.

Les rapports ne doivent pas revendiquer une exécution runtime qui n’a pas eu lieu.

## 10. Décisions techniques importantes

### Windows et AMD

- Le guide est local-first et Windows-first pour la configuration de référence.
- Les chemins GPU AMD expérimentaux sont isolés et clairement qualifiés.
- Le CPU constitue toujours une voie de référence ou de diagnostic.
- Docker Desktop sous Windows n’est pas présenté comme une solution universelle pour les charges GPU AMD.

### ComfyUI

- Installation manuelle de référence.
- CPU obligatoire comme voie de secours.
- ZLUDA isolé comme laboratoire expérimental.
- DirectML uniquement comme solution dégradée lorsque nécessaire.
- Workflows JSON, manifestes YAML, modèles, licences et empreintes doivent être versionnés.

### LLM locaux

- Ollama natif Windows pour le parcours simple.
- llama.cpp CPU/Vulkan comme moteur de référence et de mesure.
- LocalAI comme passerelle optionnelle.
- LibreChat comme interface alternative à Open WebUI.
- Services locaux liés à `127.0.0.1` sauf justification et sécurisation explicites.

### Audio local

- Kokoro et Piper pour les voix légères.
- Chatterbox pour la voix expressive et le clonage autorisé.
- faster-whisper et whisper.cpp pour la transcription.
- AudioCraft réservé aux usages compatibles avec les licences des poids.
- Aucun clonage vocal sans consentement explicite.

## 11. Historique condensé des jalons

- M0 : infrastructure documentaire terminée.
- M1 : Volume 0 terminé et audité.
- M2 : Livre I terminé à dix chapitres, après réouverture pour ajouter les fondations manquantes.
- Audit transversal Volume 0/Livre I : contextes d’utilisation appliqués et validés.
- M3 : Livre II en cours.
- Chapitre 1 : Godot et projet fil rouge, rédigé, repéré et audité.
- Chapitre 2 : fondamentaux de GDScript, rédigé, repéré, enrichi et audité contre les doublons.

Pull requests importantes :

- PR 3 : restauration du Livre I complet à dix chapitres ;
- PR 5 : audit initial des chapitres 1 et 2 du Livre II ;
- PR 6 et 7 : audit des contextes Volume 0/Livre I et stabilisation des preuves ;
- PR 8 : application des repères aux chapitres 1 et 2 du Livre II ;
- PR 10 : explications GDScript ligne par ligne ;
- PR 11 : audit anti-doublon et approfondissement des fonctions ;
- PR 12 : fermée sans fusion, workflow temporaire non appliqué.

## 12. Erreurs à ne pas reproduire

- Ne pas déclarer un Livre complet uniquement parce que ses grands domaines sont couverts.
- Ne pas condenser des fondations nécessaires à un débutant en simples prérequis.
- Ne pas donner une commande sans préciser le terminal.
- Ne pas donner un contenu de fichier sans préciser l’éditeur et le chemin.
- Ne pas présenter une sortie comme une commande.
- Ne pas affirmer qu’un exemple a été exécuté lorsqu’il a seulement été relu statiquement.
- Ne pas conserver des workflows temporaires dans `main`.
- Ne pas publier des mesures d’une exécution intermédiaire comme preuve finale.
- Ne pas laisser une fonction, un paramètre, un opérateur ou un type sans explication suffisante lors de sa première apparition.
- Ne pas dupliquer intégralement une explication déjà donnée ; utiliser un rappel bref et un renvoi.
- Ne pas oublier de mettre à jour ce fichier de continuité.

## 13. État courant du dépôt

- Branche principale : `main`.
- Dernier jalon actif : M3 — Livre II.
- Livre II : 2 chapitres sur 30 rédigés, repérés et audités.
- Chapitre 2 : version `1.3.0`.
- Dernier commit métier important : `e40da615bdc922f0296ef34f51dc6e226f0782dd`.
- Licence globale : encore à définir.
- Accessibilité PDF avancée : encore à traiter avant publication.
- Tests runtime de `Project Asteria` : en attente de matérialisation du projet exécutable.

## 14. Prochaine action

Créer puis auditer :

```text
Livre-II/CHAPITRE-03-Scenes-noeuds-resources-et-signaux.md
```

Le chapitre devra notamment expliquer en détail :

- la différence entre scène et nœud ;
- l’arbre de scène ;
- instanciation et propriété ;
- chemins de nœuds et références typées ;
- signaux intégrés et personnalisés ;
- connexion par l’éditeur et par code ;
- découplage émetteur/récepteur ;
- Resources natives et personnalisées ;
- cycle de vie et ordre d’initialisation ;
- erreurs fréquentes ;
- exercice intégré à `Project Asteria` ;
- repères d’utilisation ;
- explications ligne par ligne des nouveaux concepts ;
- audit des doublons, QA, compilation et inspection PDF.

## 15. Journal des mises à jour de continuité

### 2026-07-18 — version 1.0.0

- création du document de continuité ;
- reprise de la vision, du matériel, de l’architecture et des jalons ;
- enregistrement des règles d’audit et de contextes d’utilisation ;
- enregistrement de l’état des Livres I et II ;
- enregistrement de l’audit anti-doublon du chapitre 2 ;
- définition de la prochaine action.
