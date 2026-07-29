---
title: "Audit — Livre V, Fiche 19 : Référence audio"
id: "DOC-L5-QA-AUDIT-CH19"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 19
audit-date: "2026-07-29T15:46:00+02:00"
last-verified: "2026-07-29T15:46:00+02:00"
audit-level: "static-review"
document-format: "reference-cards"
protocol: "Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md"
---

# Audit — Fiche 19 : Référence audio

## 1. Décision

**Décision : accepté au niveau `static-review`, sans revendication de production audio, d’écoute ou de runtime.**

La fiche respecte le profil spécialisé du Livre V : index express, cartes techniques, matrices de choix, paragraphes courts, liens profonds vers les méthodes propriétaires et absence de tutoriel complet recopié.

Les valeurs numériques restent des conventions de référence déjà décidées dans le dépôt, des exemples de signal ou des champs de profil. Aucun objectif de loudness, bitrate, mémoire, latence, concurrence, ducking ou spatialisation n’est présenté comme universel ou mesuré.

## 2. Périmètre du plan maître

Le plan maître demande :

- formats ;
- fréquences ;
- loudness ;
- boucles ;
- spatialisation ;
- TTS et STT ;
- licences ;
- bus et intégration Godot ;
- diagnostics ;
- tables, presets, exemples et checklists ;
- validation par fichiers de test et mesures.

La fiche couvre les dix premiers éléments sous forme de treize cartes, trois matrices et diagrammes compacts. Les presets restent décrits comme contrats versionnés et non comme fichiers exécutables. Les fichiers de test, écoutes et mesures n’ont pas été exécutés, car aucun asset, preset ou scène audio du Companion Pack n’a été matérialisé.

## 3. Comparaison avec les fiches et chapitres voisins

### Fiche 07 — Fiches des modèles audio

La fiche 07 possède les familles de modèles, moteurs, voix, composants, variantes, licences et protocoles de qualification des paquets TTS, STT, musique et SFX. La fiche 19 traite le signal, les assets, le runtime, le mix et les preuves sans recopier les cartes de modèles.

### Fiche 18 — Référence graphique et 3D

La fiche 18 possède unités, axes, formats graphiques, PBR, UV, géométrie, LOD, rigs et import 3D. La fiche 19 utilise la même discipline de source, dérivé, import, profil et preuve, mais reste limitée à l’audio.

### Fiche 20 — Catalogue des erreurs et diagnostics

La fiche 19 contient un index compact de symptômes audio relié aux corrections propriétaires. Elle ne remplace pas le catalogue transversal par outil, message, cause et version prévu à la fiche 20.

### Fiche 21 — Benchmarks et méthodes de mesure

La fiche 19 nomme les dimensions à mesurer et les champs de protocole. La fiche 21 possédera répétitions, environnement, dispersion, comparaison et interprétation des résultats.

### Livre I — Outils audio locaux

Le Livre I conserve l’installation, les environnements, les moteurs locaux, la configuration CPU de référence et les commandes de test.

### Livre III — Production propriétaire

Les méthodes complètes restent dans :

- chapitre 5 pour provenance, licences, consentements et voix ;
- chapitre 26 pour sources, prises, génération, montage, formats, loudness, boucles, spatialisation, bus, mix, mesures et intégration Godot ;
- chapitre 27 pour phonèmes, visèmes, timings et animation faciale ;
- chapitre 28 pour les contrats d’import et de réimportation communs ;
- chapitre 29 pour la porte technique et artistique des assets.

### Livre IV — Produit complet

Le Livre IV conserve :

- chapitre 18 pour captions, signaux redondants, réglages audio accessibles, narration et TTS système ;
- chapitre 19 pour langues de texte et audio, sous-titres, doublages, repli et validation linguistique ;
- chapitres 6, 8 et 9 pour profilage CPU, mémoire et ressources ;
- chapitres 2 et 3 pour stratégie QA et non-régression.

## 4. Forme documentaire

Mesures calculées sur le contenu final :

| Mesure | Valeur |
|---|---:|
| lignes | 468 |
| titres | 20 |
| cartes `<!-- l5:card -->` | 13 |
| matrices `<!-- l5:matrix -->` | 3 |
| liens Markdown | 95 |
| renvois vers les Livres I à IV | 49 |
| liens profonds vers les Livres I à IV | 49 |
| diagrammes compacts | 7 |
| blocs clôturés | 0 |
| titres dupliqués | 0 |

L’index express ouvre chaque carte ou matrice. Les identifiants `AUDR-00` à `AUDR-12` restent uniques et distincts des cartes `AUDIO-00` à `AUDIO-12` de la fiche 07.

## 5. Couverture des cartes

| Unité | Couverture |
|---|---|
| AUDR-00 | contrat : famille, source, signal, format, lecture, routage, langue, droits et preuve |
| Matrice A | entrée par problème, carte et chapitre propriétaire |
| AUDR-01 | fréquence, profondeur PCM, canaux, durée, resampling et downmix |
| AUDR-02 | dBFS, sample peak, true peak, RMS, LUFS, dynamique et headroom |
| AUDR-03 | source, travail, revue, master, export, import, publication et provenance |
| Matrice B | WAV, FLAC, Ogg Vorbis, MP3, Opus, TTS et STT |
| AUDR-04 | profils d’import, compression, loop, trim, normalisation, mono et réimportation |
| AUDR-05 | boucles, régions, crossfades, intro, outro, stingers, stems et variantes |
| AUDR-06 | voix, SFX, ambiances, musique, UI, narration et signaux critiques |
| AUDR-07 | lecture 2D/3D, auditeur, atténuation, directivité, Doppler, filtres et zones |
| AUDR-08 | bus, sous-bus, effets, snapshots, ducking et restauration |
| AUDR-09 | modèles TTS, voix, STT, transcription, doublage, dictionnaire, timings et lip-sync |
| AUDR-10 | sous-titres, captions, redondance, mono, description audio, narration et TTS système |
| AUDR-11 | stockage, mémoire, décodage, démarrage, concurrence, mix, localisation et profils |
| Matrice C | niveaux de preuve et portes de promotion |
| AUDR-12 | symptômes, premières vérifications, causes possibles, checklist et pilote futur |

## 6. Exactitude des conventions

La fiche conserve les décisions de `Project Asteria` :

- la fréquence d’échantillonnage, la profondeur et les canaux sont des dimensions distinctes ;
- `48 kHz` et le PCM 24 bits restent des repères de production candidats, pas des obligations universelles ;
- un fichier mono est privilégié pour une source 3D ponctuelle lorsque le contexte le confirme ;
- gain, dBFS, sample peak, true peak, RMS, LUFS et plage dynamique ne sont pas interchangeables ;
- source brute, session, master, export runtime, cache importé et asset publié ont des autorités différentes ;
- FLAC reste un format d’archive ou d’échange, sans supposer un import runtime canonique ;
- WAV, Ogg Vorbis et MP3 sont choisis selon durée, boucle, latence, mémoire et profil mesurés ;
- les limites de boucle sont conservées en échantillons et vérifiées après encodage et import ;
- la variation audio ne modifie jamais le résultat gameplay ;
- la distance audible ne constitue pas une portée d’interaction ;
- l’auditeur, les zones et les bus restent des représentations ;
- les voix, modèles, moteurs, langues, consentements et sorties sont qualifiés séparément ;
- langue de texte et langue audio restent des capacités distinctes ;
- captions, signaux visuels, mono et narration sont des mécanismes à tester, pas un mode universel ;
- tout budget ou preset est lié à une famille, un build, une plateforme, une scène et un protocole.

## 7. Diagnostics et règle sémantique des erreurs

`AUDR-12` est un index compact de symptômes, vérifications, causes possibles et sources propriétaires. Il porte `<!-- qa:error-correction-index -->` et ne contient aucun faux couple exemple fautif/corrigé incomplet.

Les exemples détaillés restent dans les sections conformes des chapitres propriétaires. La future fiche 20 conservera le catalogue transversal des messages, outils, versions et procédures de diagnostic.

## 8. Validation documentaire légère

Workflow temporaire : `Temporary Livre V Chapter 19 Script Runner`.

Run final : `30458855819`.

Tête source : `4268161da585e900479aeea1e2c94fa5d5bd88af`.

Commandes exécutées sans PDF :

- `python tools/validate_chapters.py --root . --report dist/QA-CHAPTERS.md` ;
- `python tools/validate_livre_v_references.py --check` ;
- `python tools/check_code_explanation_structure.py --check` ;
- `python tools/check_context_markers.py --check` ;
- `python tools/audit_contextes_semantiques.py --check`.

Les validations doivent réussir sur le lot final avant commit. Aucun workflow PDF, Pandoc, XeLaTeX, qpdf ou rendu visuel ne doit être lancé.

## 9. Doublons, liens et repères

- aucun titre dupliqué ;
- aucun bloc clôturé à expliquer ;
- aucun paragraphe long recopié depuis les chapitres propriétaires ;
- ordre continu du Livre V maintenu dans `contents.txt` ;
- chemin canonique et identifiant `DOC-L5-CH19` conformes ;
- densité de renvois vers les Livres I à IV supérieure au minimum du protocole ;
- plusieurs liens profonds visent des sous-sections réellement présentes ;
- aucune structure tutoriel interdite ;
- aucune commande à exécuter dans la fiche ;
- aucune URL externe ou brute ;
- aucun PDF intermédiaire.

## 10. Niveau de preuve

Les assertions techniques sont limitées aux contrats déjà consignés dans le dépôt. La fiche ne revendique pas :

- l’exécution d’un moteur TTS, STT, générateur musical ou outil audio ;
- l’enregistrement ou le traitement d’une voix ;
- la création d’un WAV, FLAC, Ogg, MP3, Opus, master ou export runtime ;
- une écoute critique ou une comparaison AB ;
- un import ou une réimportation Godot ;
- la création d’un bus, effet, snapshot, zone ou lecteur ;
- une boucle, transition, variation ou synchronisation produite ;
- une mesure de loudness, true peak, mémoire, latence ou concurrence ;
- une campagne d’accessibilité, de localisation ou de plateforme ;
- une approbation artistique, linguistique ou juridique ;
- une donnée utilisateur, personnelle ou de production.

Le niveau reste `static-review`.

## 11. Intégrité

Empreinte SHA-256 du chapitre :

`721d462541534bc3f701ae5fc7e35f54b710a60a921fc3c7758f5ac195bcd1c9`

L’empreinte de cet audit est enregistrée dans la preuve finale.

## 12. Réserves

- aucun fichier audio de test matérialisé ou mesuré malgré le critère futur du plan maître ;
- aucun preset, checklist exécutable ou fixture permanente du Companion Pack créé ;
- aucune importation, réimportation, lecture ou comparaison exécutée ;
- aucune mesure de niveau, mémoire, concurrence, streaming ou latence ;
- aucune qualification Mobile, Web, console, casque, haut-parleur ou autre dispositif ;
- aucune revue artistique, accessible, linguistique ou juridique organisationnelle ;
- aucun PDF produit ;
- licence globale et accessibilité avancée du PDF toujours ouvertes.

## 13. Critère d’acceptation

La fiche est acceptée parce qu’un lecteur peut :

1. trouver immédiatement la convention ou le symptôme audio recherché ;
2. distinguer fréquence, profondeur, canaux, durée et conversion ;
3. distinguer dBFS, crête, RMS, LUFS, dynamique et headroom ;
4. séparer source, session, master, export et cache importé ;
5. choisir un chemin de format selon l’usage et la preuve ;
6. relier boucles, régions, transitions et variantes aux méthodes propriétaires ;
7. distinguer lecture 2D, source 3D, auditeur, zone et portée gameplay ;
8. organiser bus, effets, snapshots et ducking sans déplacer l’autorité métier ;
9. relier modèles, voix, TTS, STT, localisation et lip-sync ;
10. préparer captions, redondance, mono, narration et TTS système ;
11. traiter budgets et presets comme contextuels et versionnés ;
12. distinguer revue statique, écoute, mesure, test build et décision humaine ;
13. comprendre qu’aucun fichier, mesure ou runtime n’a été exécuté.