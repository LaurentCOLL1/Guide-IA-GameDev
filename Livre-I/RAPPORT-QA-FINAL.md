---
title: "Rapport QA final du Livre I"
id: "DOC-L1-QA-FINAL"
status: "complete"
version: "2.0.0"
book: "Livre I"
category: "quality-report"
validation-date: "2026-07-18"
---

# Rapport QA final du Livre I

> **Repères d’utilisation :** **[PS]** PowerShell, **[VSC]** Visual Studio Code, **[WEB]** navigateur internet, **[APP]** interface graphique, **[SORTIE]** résultat à ne pas saisir. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

## 1. Décision

**Validation réussie.** La structure corrigée du Livre I contient dix chapitres et satisfait les contrôles documentaires, structurels et de compilation du milestone M2.

Le Livre I peut être considéré comme **terminé sur le plan documentaire et technique de compilation**.

Cette décision ne remplace pas :

- les essais matériels sur chaque poste utilisateur ;
- la vérification juridique des licences pour un projet commercial particulier ;
- la validation de la licence globale du guide avant publication officielle ;
- le chantier de balisage et d’accessibilité du PDF prévu dans M8.

## 2. Exécution de référence

| Élément | Valeur |
|---|---|
| Workflow | `Validate Documentation` |
| Exécution | `29639079721` |
| Résultat | `success` |
| Branche de contrôle | `docs/reopen-livre-i-foundations` |
| Commit contrôlé | `78ee0e432cf31a8282dd243125a0b4a70785afbb` |
| Pull request | `#3` |
| Date | 18 juillet 2026 |

Toutes les étapes ont réussi :

- installation de la chaîne documentaire ;
- contrôle structurel des sources ;
- contrôle de la séquence des chapitres 01 à 10 ;
- contrôle des identifiants nouveaux et historiques ;
- contrôle des métadonnées de renumérotation ;
- validation des liens locaux ;
- compilation Pandoc et XeLaTeX ;
- inspection technique du PDF ;
- extraction du texte ;
- publication des artefacts de validation.

## 3. Correction du périmètre

La première version du Livre I regroupait le contenu dans six chapitres. Elle couvrait les grands services IA, mais pas suffisamment les fondations nécessaires à un débutant complet.

Quatre chapitres ont été ajoutés :

1. terminal, PowerShell et outils Windows ;
2. Git, GitHub et Visual Studio Code ;
3. Python et environnements virtuels ;
4. sécurité, sauvegarde et validation de la plateforme.

Les chapitres historiques ont été déplacés :

| Sujet | Ancienne position | Position actuelle | Identifiant conservé |
|---|---:|---:|---|
| Docker et Docker Compose | 2 | 5 | `DOC-L1-CH02` |
| Open WebUI, Open Terminal et Vane | 3 | 6 | `DOC-L1-CH03` |
| ComfyUI et workflows graphiques | 4 | 7 | `DOC-L1-CH04` |
| LLM locaux | 5 | 8 | `DOC-L1-CH05` |
| Audio IA local | 6 | 9 | `DOC-L1-CH06` |

Les identifiants stables n’ont pas été réattribués. Les documents déplacés possèdent les métadonnées `legacy-chapter` et `canonical-order`.

## 4. Résultats du contrôle structurel

| Mesure | Résultat |
|---|---:|
| Sources déclarées dans `contents.txt` | 37 |
| Chapitres du Livre I détectés | 10 |
| Séquence attendue | 01 à 10 |
| Identifiants uniques détectés | 36 |
| Erreurs bloquantes | 0 |
| Avertissements automatisés | 1 |

Les contrôles n’ont détecté aucun :

- fichier source absent ;
- doublon dans `contents.txt` ;
- chapitre manquant ou hors ordre ;
- identifiant documentaire dupliqué ;
- identifiant stable incorrect dans le Livre I ;
- front matter YAML invalide ;
- métadonnée `book`, `chapter` ou `last-verified` manquante ;
- métadonnée de migration manquante dans les chapitres déplacés ;
- lien Markdown local cassé ;
- marqueur de conflit Git.

## 5. Périmètre des dix chapitres

1. matériel, Windows, pilotes AMD et accélération locale ;
2. terminal, PowerShell et outils Windows ;
3. Git, GitHub et Visual Studio Code ;
4. Python et environnements virtuels ;
5. Docker et Docker Compose ;
6. Open WebUI, Open Terminal et Vane ;
7. ComfyUI et workflows graphiques ;
8. LLM locaux avec Ollama, llama.cpp, LocalAI et LibreChat ;
9. audio IA local, voix, transcription, musique et effets ;
10. sécurité, sauvegarde et validation de la plateforme.

La nouvelle structure fournit une progression complète :

> **[LECTURE] Structure de référence - Ne pas saisir :** utiliser le bloc comme repère visuel.

```text
comprendre le poste
        ↓
maîtriser le terminal
        ↓
versionner les sources
        ↓
isoler Python
        ↓
installer les services
        ↓
installer les outils IA
        ↓
sauvegarder et restaurer
        ↓
valider la plateforme
```

## 6. Résultats de compilation

| Propriété | Résultat |
|---|---|
| Format | PDF 1.5 |
| Taille de page | A4 |
| Nombre de pages | 396 |
| Taille du fichier | 1 051 008 octets |
| Moteur | XeLaTeX via Pandoc |
| Producteur | `xdvipdfmx` |
| Titre PDF | Guide réaliste de création de jeux vidéo 3D avec IA locale |
| Auteur | Laurent Collin |
| Chiffrement | aucun |
| JavaScript embarqué | aucun |
| Texte extractible | oui |
| Pages suspectes signalées | aucune |
| Polices principales | DejaVu Serif, DejaVu Sans et DejaVu Sans Mono, incorporées |

Le journal Pandoc ne contient aucune erreur, aucun avertissement de glyphe manquant et aucun message de fichier introuvable.

## 7. Contrôle visuel

Un échantillon de **82 pages** a été rendu à 160 DPI et examiné :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
1-5
210-220
230-270
372-396
```

L’échantillon couvre :

- la couverture ;
- la table des matières ;
- la fin du Volume 0 ;
- l’index du Livre I ;
- le chapitre matériel ;
- l’intégralité visuelle ou de larges extraits des chapitres Terminal, Git et Python ;
- la transition Python vers Docker ;
- la fin du chapitre audio ;
- le chapitre sécurité et restauration ;
- la transition vers le Livre II ;
- les index des Livres III à V ;
- le Companion Pack.

Aucun des défauts suivants n’a été observé :

- texte rogné ;
- chevauchement majeur ;
- glyphe manquant visible ;
- carré noir ;
- rotation incorrecte ;
- changement inattendu de format de page ;
- titre global remplacé par un titre de chapitre ;
- tableau manifestement hors page ;
- bloc de code illisible dans l’échantillon ;
- rupture visuelle causée par la renumérotation.

La dernière page est partiellement vide, ce qui correspond à la fin du contenu actuel du Companion Pack.

## 8. Avertissements et réserves

### 8.1 Licence globale

La métadonnée globale conserve :

> **[LECTURE] Exemple de code - Ne pas exécuter directement :** utiliser selon l’instruction qui précède.

```yaml
license: "À définir avant publication"
```

Cette réserve ne bloque pas M2, mais reste **bloquante avant une publication officielle, une release stable ou une redistribution organisée**.

### 8.2 Licences des dépendances et ressources

La validation structurelle ne peut pas décider automatiquement si la licence d’un logiciel, modèle, poids, voix, jeu de données ou contenu généré convient à un usage commercial particulier.

Les chapitres imposent :

- une source et une date de récupération ;
- une distinction entre licence du code et licence des poids ;
- une empreinte pour les modèles et archives importants ;
- un registre de consentement pour les voix ;
- le blocage des ressources non commerciales dans un pipeline commercial ;
- une nouvelle vérification lors de chaque changement de version.

### 8.3 Accessibilité

Le PDF généré n’est pas balisé comme PDF structuré pour lecteur d’écran (`Tagged: no`). Ce point reste transféré à M8.

### 8.4 Validation matérielle

Le workflow prouve la cohérence et la compilabilité de la documentation. Il ne prouve pas que tous les backends fonctionnent sur chaque poste.

Les procédures conservent donc :

- un chemin CPU de référence ;
- des tests minimaux ;
- des critères d’acceptation observables ;
- des environnements expérimentaux isolés ;
- une méthode de retour arrière.

## 9. Artefacts produits

L’artefact GitHub Actions `documentation-validation` contient :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
Guide-IA-GameDev.pdf
Guide-IA-GameDev.txt
QA-DOCUMENTATION.md
PANDOC-BUILD.log
PDF-INFO.txt
```

L’archive de l’exécution porte l’empreinte :

> **[LECTURE] Exemple ou valeur de référence - Ne pas saisir.**

```text
sha256:37692ab31405d003fcbe7f6c9fb8ac2f4b9b4d8017e95af485ff9db473bdda98
```

Les artefacts sont conservés quatorze jours par le workflow. Le PDF reste un livrable généré et n’est pas versionné comme source dans Git.

## 10. Historique de validation

| Structure | Exécution | Résultat | Statut actuel |
|---|---:|---|---|
| Livre I à six chapitres | `29638120888` | succès | historique, remplacé |
| Livre I à dix chapitres | `29639079721` | succès | référence actuelle |

La validation à six chapitres reste une preuve historique correcte pour son ancien périmètre. Elle ne constitue plus la référence de clôture.

## 11. Critères de clôture M2

- [x] Dix chapitres rédigés.
- [x] Dix chapitres intégrés dans `contents.txt`.
- [x] Progression pédagogique adaptée aux débutants.
- [x] Identifiants historiques conservés.
- [x] Nouveaux identifiants sans collision.
- [x] Métadonnées spécifiques au Livre I vérifiées.
- [x] Liens Markdown locaux valides.
- [x] Compilation Pandoc/XeLaTeX réussie.
- [x] PDF A4 de 396 pages généré.
- [x] Texte du PDF extractible.
- [x] Métadonnées PDF globales correctes.
- [x] Polices incorporées.
- [x] Échantillon visuel de 82 pages contrôlé.
- [x] Rapport QA final rédigé.
- [ ] Licence globale définie avant publication officielle.
- [ ] PDF balisé pour l’accessibilité avant publication officielle.

## 12. Conclusion

Le milestone **M2 — Livre I : Préparer la plateforme** peut être clôturé sur sa structure corrigée à dix chapitres.

La prochaine phase active est **M3 — Livre II : Développement et architecture**, en commençant par Godot, GDScript et l’architecture du projet de jeu.
