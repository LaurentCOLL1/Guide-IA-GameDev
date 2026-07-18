---
title: "Rapport QA final du Livre I"
id: "DOC-L1-QA-FINAL"
status: "complete"
version: "1.0.1"
book: "Livre I"
category: "quality-report"
validation-date: "2026-07-18"
---

# Rapport QA final du Livre I

## 1. Décision

**Validation réussie.** Les six chapitres du Livre I, leurs métadonnées, leurs liens et la chaîne de compilation documentaire satisfont les critères de clôture du milestone M2.

Le Livre I peut être considéré comme **terminé sur le plan documentaire**. Cette décision ne remplace pas les essais matériels réels sur chaque poste utilisateur et ne vaut pas autorisation de publication officielle tant que la licence globale du projet reste indéterminée.

## 2. Exécution de référence

| Élément | Valeur |
|---|---|
| Workflow | `Validate Documentation` |
| Exécution | `29638120888` |
| Résultat | `success` |
| Branche de contrôle | `qa/validate-livre-i` |
| Commit contrôlé | `75316cb1b1a51b10194343dcd7bd325d953876f1` |
| Date | 18 juillet 2026 |

Cette exécution finale inclut l’index du Livre I marqué `complete`, la clôture de M2 dans la roadmap et le lien vers le présent rapport QA.

Toutes les étapes ont réussi :

- installation de la chaîne documentaire ;
- contrôle structurel des sources ;
- contrôles spécifiques des six chapitres du Livre I ;
- compilation Pandoc et XeLaTeX ;
- inspection technique du PDF ;
- extraction du texte ;
- publication des artefacts de validation.

## 3. Résultats du contrôle structurel

| Mesure | Résultat |
|---|---:|
| Sources déclarées dans `contents.txt` | 33 |
| Chapitres du Livre I détectés | 6 |
| Identifiants uniques détectés | 32 |
| Erreurs bloquantes | 0 |
| Avertissements automatisés | 1 |

Les contrôles n’ont détecté aucun :

- fichier source absent ;
- doublon dans `contents.txt` ;
- identifiant documentaire dupliqué ;
- front matter YAML invalide ;
- métadonnée obligatoire manquante dans les chapitres du Livre I ;
- incohérence entre le numéro du fichier et la métadonnée `chapter` ;
- lien Markdown local cassé ;
- marqueur de conflit Git.

## 4. Avertissements et réserves

### 4.1 Licence globale

La métadonnée globale conserve :

```yaml
license: "À définir avant publication"
```

Cette réserve ne bloque pas M2, mais reste **bloquante avant une publication officielle, une release stable ou une redistribution organisée**.

### 4.2 Licences des composants et modèles

La validation structurelle ne peut pas décider automatiquement si une licence de modèle, de poids, de voix, de jeu de données ou de contenu généré convient à un projet commercial particulier.

Les chapitres du Livre I imposent donc :

- un manifeste par modèle ;
- une distinction entre licence du code et licence des poids ;
- la conservation de la source et de la date de téléchargement ;
- la vérification séparée des voix et données d’entraînement ;
- le blocage des ressources non commerciales dans un pipeline destiné à la publication commerciale.

### 4.3 Accessibilité du PDF

Le PDF généré n’est pas balisé comme PDF structuré pour lecteur d’écran (`Tagged: no`). Cela ne bloque pas le milestone documentaire M2, mais devra être traité dans le chantier de publication et d’accessibilité de M8.

## 5. Résultats de compilation

| Propriété | Résultat |
|---|---|
| Format | PDF 1.5 |
| Taille de page | A4 |
| Nombre de pages | 348 |
| Taille du fichier | 939 388 octets |
| Moteur | XeLaTeX via Pandoc |
| Producteur | `xdvipdfmx` |
| Titre PDF | Guide réaliste de création de jeux vidéo 3D avec IA locale |
| Auteur | Laurent Collin |
| Chiffrement | aucun |
| JavaScript embarqué | aucun |
| Texte extractible | oui |
| Polices principales | DejaVu Serif, DejaVu Sans et DejaVu Sans Mono, incorporées |

Le journal Pandoc ne contient aucune erreur, aucun avertissement de glyphe manquant et aucun message de fichier introuvable.

## 6. Contrôle visuel

Un échantillon de **46 pages** a été rendu à 160 DPI et examiné :

```text
1-5
210-220
228-232
246-250
270-274
294-298
316-320
344-348
```

Cet échantillon couvre :

- la couverture ;
- la table des matières ;
- la transition entre le Volume 0 et le Livre I ;
- l’index du Livre I ;
- le début, le milieu et la fin de chacun des six chapitres ;
- des tableaux ;
- des blocs de code ;
- des listes et arborescences ;
- la transition vers les livres suivants et le Companion Pack.

Après la clôture de M2, les pages 213 à 215 ont été rendues de nouveau à 180 DPI. Le lien vers le rapport QA, les réserves de publication et le statut final restent lisibles sans débordement.

Aucun des défauts suivants n’a été observé :

- texte rogné ;
- chevauchement majeur ;
- glyphe manquant visible ;
- carré noir ;
- rotation incorrecte ;
- changement inattendu de format de page ;
- titre global remplacé par un titre de chapitre ;
- tableau manifestement hors page ;
- bloc de code illisible dans l’échantillon.

La dernière page est partiellement vide, ce qui correspond à la fin du contenu actuel du Companion Pack et ne constitue pas une anomalie de mise en page.

## 7. Périmètre fonctionnel validé

Les six domaines documentaires de M2 sont présents :

1. matériel, Windows, pilotes AMD et voies d’accélération ;
2. Docker et Docker Compose ;
3. Open WebUI, Open Terminal et Vane ;
4. ComfyUI et workflows graphiques ;
5. LLM locaux avec Ollama, llama.cpp, LocalAI et LibreChat ;
6. audio IA local, voix, transcription, musique et effets.

La validation confirme la cohérence documentaire, pas la disponibilité universelle de tous les backends sur toutes les machines. Les chapitres conservent systématiquement :

- un chemin CPU de référence ;
- une séparation entre parcours officiellement documenté et solution expérimentale ;
- des procédures de diagnostic ;
- des critères d’acceptation observables ;
- des règles de sauvegarde et de retour arrière ;
- des contraintes de licence et de consentement.

## 8. Artefacts produits

L’artefact GitHub Actions `documentation-validation` contient :

```text
Guide-IA-GameDev.pdf
Guide-IA-GameDev.txt
QA-DOCUMENTATION.md
PANDOC-BUILD.log
PDF-INFO.txt
```

Les artefacts sont conservés quatorze jours par le workflow. Le PDF reste un livrable généré et n’est pas versionné comme source dans Git.

## 9. Critères de clôture M2

- [x] Six chapitres rédigés.
- [x] Six chapitres intégrés dans `contents.txt`.
- [x] Métadonnées spécifiques au Livre I vérifiées.
- [x] Identifiants sans doublon.
- [x] Liens Markdown locaux valides.
- [x] Compilation Pandoc/XeLaTeX réussie.
- [x] PDF A4 de 348 pages généré.
- [x] Texte du PDF extractible.
- [x] Métadonnées PDF globales correctes.
- [x] Polices incorporées.
- [x] Échantillon visuel de 46 pages contrôlé.
- [x] État clôturé de M2 recompilé et vérifié.
- [x] Rapport QA final rédigé.
- [ ] Licence globale définie avant publication officielle.
- [ ] PDF balisé pour l’accessibilité avant publication officielle.

## 10. Conclusion

Le milestone **M2 — Livre I : Préparer la plateforme** est clôturé sur le plan documentaire et technique de compilation.

La prochaine phase active est **M3 — Livre II : Développement et architecture**, en commençant par Godot, GDScript et l’architecture du projet de jeu.