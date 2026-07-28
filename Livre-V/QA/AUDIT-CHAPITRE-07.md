---
title: "Audit — Livre V, fiche 07"
id: "DOC-L5-QA-AUDIT-CH07"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 7
last-verified: "2026-07-28T17:27:15+02:00"
audit-date: "2026-07-28T17:27:15+02:00"
audit-level: "static-review"
audited-document: "Livre-V/CHAPITRE-07-Fiches-des-modeles-audio.md"
protocol: "Livre-V/QA/PROTOCOLE-FICHES-LIVRE-V.md"
---

# Audit de la fiche 07 — Fiches des modèles audio

## Décision

**Acceptée au niveau `static-review`.** La fiche respecte le profil du Livre V : index express, cartes de familles et de composants, matrices en premier, liens profonds vers les sources propriétaires et séparation explicite entre modèle, moteur, voix, consentement, exécution et asset publié.

## Couverture du plan maître

| Exigence | Résultat |
|---|---|
| TTS | Kokoro-82M, Piper et Chatterbox qualifiés |
| STT | famille Whisper et ses tailles qualifiées sans dupliquer les moteurs |
| musique | MusicGen qualifié comme outil de maquette non commerciale avec AudioCraft |
| effets | AudioGen qualifié comme source exploratoire non commerciale |
| langues | français, locales, prononciation et couverture annoncée séparés des tests |
| voix | modèle, fichier de voix, locuteur, référence et consentement distingués |
| licences | code, poids, voix, datasets, entrées, sorties et redistribution séparés |
| consentements | adaptation, clonage, conversion et entraînement nécessitent une autorisation explicite |
| vitesse et mémoire | variables et protocoles visibles sans résultat matériel inventé |
| qualité | intelligibilité, erreurs STT, stabilité, artefacts et fonction soumis à écoute humaine |
| échantillons | protocole et identifiants préparés ; aucun fichier audio matérialisé |
| benchmarks | matrice de douze tests sans valeur préremplie |
| formulaires de provenance | champs de manifeste, consentement et retrait présents |

## Frontières contrôlées

- La fiche 03 conserve les applications et outils audio.
- La fiche 04 conserve faster-whisper, whisper.cpp, Piper comme moteur, les API et les backends.
- La fiche 07 conserve les familles de modèles, voix et composants audio.
- La fiche 08 conservera les workflows réutilisables.
- Le chapitre 19 du Livre V conservera la référence audio transversale.
- Le chapitre 21 conservera les benchmarks exécutés.
- Le chapitre 22 conservera les compatibilités historiques.
- Le chapitre 25 conservera l’inventaire transversal des licences et consentements.
- Le Livre I conserve les installations.
- Le Livre III conserve prise, montage, mix, mastering et intégration Godot.

## Contrôles de forme

| Contrôle | Résultat |
|---|---:|
| lignes | 394 |
| titres Markdown | 18 |
| fiches `l5:card` | 13 |
| matrices `l5:matrix` | 3 |
| liens Markdown | 61 |
| renvois vers les Livres I à IV | 27 |
| liens profonds vers des sous-sections | 27 |
| liens web officiels | 14 |
| blocs clôturés | 0 |
| structure « Résultats d’apprentissage » importée | absente |
| synthèse finale `Project Asteria` importée | absente |
| installation audio complète recopiée | absente |
| échantillon audio intégré | absent |

## Sources officielles datées

Les pages et dépôts suivants ont été consultés le `2026-07-28` :

- dépôt et carte Kokoro-82M ;
- dépôt, releases et collection de voix Piper ;
- dépôt et cartes Chatterbox Multilingual V3 et Turbo ;
- dépôt et carte OpenAI Whisper ;
- dépôt AudioCraft et documentations MusicGen et AudioGen.

Les cartes reprennent seulement identité, taille, langues annoncées, composants, licences, formats et contraintes de qualification. Les démonstrations audio et affirmations promotionnelles de vitesse ou qualité ne sont pas importées comme résultats du guide.

## Qualification des faits volatils

- chaque famille porte une date de revue ;
- une langue annoncée n’est pas une prononciation qualifiée ;
- une voix disponible n’est pas un consentement ;
- une licence de code ne couvre pas les poids, voix, datasets ou sorties ;
- une vitesse éditeur n’est pas une mesure du Ryzen 7 2700 ;
- une quantité de mémoire éditeur n’est pas un pic sur la RX 6750 XT ;
- un modèle TTS n’est ni sa voix, ni son phonémiseur, ni son vocodeur ;
- Whisper est la famille de modèles ; faster-whisper et whisper.cpp restent des moteurs ;
- les poids AudioCraft publiés sous CC-BY-NC 4.0 ne sont pas une base commerciale par défaut ;
- une sortie ressemblante n’est ni autorisée, ni stable, ni publiable par elle-même.

## Consentement et données

La fiche exige de distinguer :

- locuteur et titulaire ;
- voix enregistrée et voix synthétique ;
- synthèse générique, adaptation, clonage, conversion et entraînement ;
- fixation, reproduction, communication, adaptation, langues, plateformes et promotion ;
- consentement préalable, périmètre d’usage, révocation et retrait ;
- stockage restreint des prises, références et documents.

Aucun enregistrement personnel, formulaire signé ou donnée biométrique n’est traité dans ce lot.

## Workflow de test

La matrice C couvre :

- chargement du paquet exact ;
- TTS court et long ;
- français, nombres, noms propres et rythme ;
- référence vocale consentie ;
- STT propre et dégradé ;
- VAD et hallucinations ;
- musique et bruitages exploratoires ;
- reproductibilité ;
- postproduction ;
- revue humaine.

Aucun résultat ni fichier audio n’est fourni. Les exécutions futures doivent conserver modèles, voix, entrées, paramètres, sorties, empreintes, consentements et rapports, puis enregistrer les mesures au chapitre 21.

## Liens et ancres

Les 27 renvois profonds visent les sections propriétaires consacrées aux modèles audio, voix, consentements, formats, CPU, TTS, STT, musique, effets, nettoyage, prononciation, sous-titres, benchmarks et provenance. Le validateur spécialisé du Livre V vérifie leur résolution sur la branche de PR.

Les 14 liens web sont nommés et visent des dépôts, cartes ou documentations officielles. Leur consultation qualifie l’état documentaire sans téléchargement de poids ni écoute d’échantillon.

## Doublons et densité

- aucun tutoriel d’installation recopié ;
- aucune commande de synthèse ou transcription reproduite ;
- aucun moteur de la fiche 04 dupliqué comme modèle ;
- aucune procédure de mix ou d’intégration Godot du Livre III reproduite ;
- chaque famille et chaque composant possède une carte distincte ;
- les paragraphes restent courts et les tables portent l’information principale.

## Réserves

- aucun modèle, checkpoint, voix, vocodeur, codec ou dérivé téléchargé ;
- aucun fichier de référence vocale ou consentement reçu ;
- aucun moteur audio chargé ou exécuté ;
- aucune synthèse, transcription, musique, effet ou échantillon produit ;
- aucune mesure de temps, facteur temps réel, RAM, VRAM, stabilité ou qualité produite ;
- aucune voie CPU, DirectML, Vulkan, ZLUDA ou ROCm qualifiée avec ces modèles ;
- aucune approbation juridique organisationnelle réalisée ;
- aucune voix communautaire ni cas de clonage audité ;
- aucun fichier ou manifeste du Companion Pack créé ;
- aucun PDF produit ;
- la licence globale et le balisage avancé de publication restent ouverts.

## Empreinte

L’empreinte du chapitre est enregistrée dans la preuve QA finale. Toute modification ultérieure exige une nouvelle empreinte et une nouvelle validation.
