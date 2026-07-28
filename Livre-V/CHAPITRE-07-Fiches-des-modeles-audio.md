---
title: "Livre V — Fiche 07 : Fiches des modèles audio"
id: "DOC-L5-CH07"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 7
last-verified: "2026-07-28T17:27:15+02:00"
audit-status: "complete"
audit-date: "2026-07-28T17:27:15+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-07.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "audio-model-families-voices-and-components"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Fiches des modèles audio

> **Type de document :** cartes de familles, cartes de voix et composants, matrices de compatibilité et protocole de test audio.
> **Lecture :** partir de la tâche, puis identifier séparément le modèle, le moteur, la voix, les dépendances, les droits et le niveau de preuve.
> **Principe :** un modèle audio n’est ni une voix, ni un moteur, ni un fichier prêt pour le jeu ; chacun possède sa version, sa licence, sa mémoire, ses formats et sa validation.

## Index express

| Besoin | Ouvrir |
|---|---|
| enregistrer un paquet audio exact | [AUDIO-00](#audio-00--contrat-dun-paquet-audio) |
| choisir selon tâche et enveloppe | [Matrice A](#matrice-a--sélection-par-tâche-et-enveloppe) |
| produire une voix légère | [AUDIO-01 — Kokoro](#audio-01--kokoro-82m) |
| produire une voix embarquable | [AUDIO-02 — Piper](#audio-02--piper-et-ses-voix) |
| produire une voix expressive autorisée | [AUDIO-03 — Chatterbox](#audio-03--chatterbox) |
| transcrire ou traduire un enregistrement | [AUDIO-04 — Whisper](#audio-04--whisper) |
| explorer une maquette musicale | [AUDIO-05 — MusicGen](#audio-05--musicgen) |
| explorer un bruitage généré | [AUDIO-06 — AudioGen](#audio-06--audiogen) |
| vérifier les composants obligatoires | [Matrice B](#matrice-b--compatibilité-du-paquet) |
| distinguer voix, locuteur et consentement | [AUDIO-07](#audio-07--voix-locuteur-et-consentement) |
| identifier phonémiseur, vocodeur et codec | [AUDIO-08](#audio-08--phonémiseur-tokenizer-vocodeur-et-codec) |
| préparer VAD, diarisation et nettoyage | [AUDIO-09](#audio-09--vad-diarisation-et-nettoyage) |
| qualifier français et localisation | [AUDIO-10](#audio-10--langues-prononciation-et-localisation) |
| qualifier une voix ou un dérivé tiers | [AUDIO-11](#audio-11--voix-et-dérivés-communautaires) |
| comparer sans inventer une qualité | [Matrice C](#matrice-c--workflow-de-test-reproductible) |
| accepter, limiter ou retirer un paquet | [AUDIO-12](#audio-12--manifeste-et-acceptation) |

---

<!-- l5:card -->
## AUDIO-00 — Contrat d’un paquet audio

| Champ | Règle |
|---|---|
| identité | organisation, dépôt, révision, nom exact de chaque fichier, taille et empreinte |
| fonction | TTS, STT, traduction, musique, effet, séparation, détection ou transformation |
| moteur | bibliothèque ou exécutable qui charge le modèle ; voir la [fiche 04](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#backend-06--faster-whisper-et-ctranslate2) |
| voix | locuteur synthétique, voix préentraînée ou référence consentie ; elle ne se confond pas avec le modèle |
| composants | tokenizer, phonémiseur, encodeur, vocodeur, codec, VAD, modèle principal et fichiers de configuration |
| formats | poids, audio d’entrée, audio de sortie, fréquence, profondeur, canaux et métadonnées |
| langues | langues annoncées, voix disponibles et langues réellement testées restent distinctes |
| licence | code, poids, voix, datasets, référence, sortie et redistribution sont qualifiés séparément |
| performance | temps de chargement, facteur temps réel, RAM, VRAM et stabilité seulement après mesure |
| preuve | source officielle, chargement, sortie produite, comparaison datée, écoute humaine et droits vérifiés |

**Réponse rapide :** l’unité acceptée est un **paquet audio exécutable, traçable et autorisé**, pas le nom d’un modèle. Le [registre audio du Livre I](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#18-gestion-des-modèles-et-licences) et la [chaîne de provenance du Livre III](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#14-génération-de-voix-sfx-ou-musique) restent les sources de production.

---

<!-- l5:matrix -->
## Matrice A — Sélection par tâche et enveloppe

| Besoin | Familles à examiner | Paquet minimal | Enveloppe et risque | Décision |
|---|---|---|---|---|
| voix utilitaire locale | Kokoro ou Piper | modèle, voix, phonémiseur, configuration et moteur | CPU privilégié ; français et licence de voix à vérifier | commencer par une phrase témoin courte |
| voix expressive multilingue | Chatterbox Multilingual | modèle, tokenizer, référence autorisée, vocodeur et moteur | plus lourd ; consentement et stabilité du locuteur obligatoires | environnement isolé et usage borné |
| voix rapide anglaise | Chatterbox Turbo ou Nano | variante exacte et voix autorisée | langue et fonctions différentes de la branche multilingue | ne pas transférer les capacités entre variantes |
| transcription française | Whisper small ou medium | checkpoint Whisper, tokenizer, moteur STT et VAD qualifié | CPU possible ; exactitude, timestamps et hallucinations à relire | small comme point de départ documentaire |
| transcription autonome | mêmes poids Whisper via whisper.cpp | modèle converti, binaire, VAD et options | CPU de référence ; Vulkan seulement après comparaison | conserver le même audio et les mêmes réglages |
| maquette musicale | MusicGen | modèle, codec audio, prompt et moteur AudioCraft | poids non commerciaux ; charge mémoire importante | recherche seulement jusqu’à clarification |
| maquette de bruitage | AudioGen | modèle, codec, prompt et moteur AudioCraft | poids non commerciaux ; sortie à monter et contrôler | prototype ou référence temporaire |
| publication d’un asset | paquet déjà accepté | source, master, licence, consentement, rapport et export | aucune sortie brute n’est un asset final | suivre le pipeline du Livre III |

Le [CPU reste la référence du Livre I](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#21-le-cpu-reste-la-référence). Cette matrice oriente une qualification ; elle ne prouve ni qualité, ni temps réel, ni compatibilité avec la RX 6750 XT.

---

<!-- l5:card -->
## AUDIO-01 — Kokoro-82M

| Champ | Référence datée |
|---|---|
| famille | Kokoro-82M, modèle TTS léger de 82 millions de paramètres |
| fonction | synthèse vocale rapide pour prototypes, voix système, accessibilité et prévisualisation |
| langues | plusieurs pipelines linguistiques ; la disponibilité d’une voix française ne prouve pas une couverture française large |
| composants | modèle Kokoro, tokenizer ou phonémiseur, fichier de voix et bibliothèque d’inférence |
| licence | poids annoncés sous Apache 2.0 ; vérifier la licence de chaque voix et dépendance |
| CPU | candidat léger, mais aucune vitesse n’est transférée à la machine de référence sans mesure |
| formats | sortie audio et fréquence dépendent de l’implémentation ; conserver les paramètres du run |
| limites | noms propres, nombres, sigles, accents, rythme et longues phrases doivent être écoutés |
| alternative | Piper pour un paquet embarquable ; Chatterbox pour une expressivité ou adaptation autorisée |
| sources officielles | [dépôt Kokoro](https://github.com/hexgrad/kokoro), [carte Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) |
| sources internes | [positionnement Kokoro](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#61-positionnement), [test minimal](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#63-test-minimal) |
| preuve | sources officielles revues le `2026-07-28` ; aucune phrase générée |

**Décision de consultation :** Kokoro est un candidat de prototype, pas une voix française validée. Une voix, son fichier, sa langue et ses droits doivent être enregistrés séparément.

---

<!-- l5:card -->
## AUDIO-02 — Piper et ses voix

| Champ | Référence datée |
|---|---|
| famille | Piper actuel maintenu dans `OHF-Voice/piper1-gpl` |
| version observée | release `v1.4.2` publiée le `2026-04-02` |
| fonction | TTS local, embarquable et orienté CPU |
| composants | code Piper, modèle ONNX, configuration JSON, phonémiseur `espeak-ng` et éventuels fichiers annexes |
| voix | chaque voix est un artefact distinct avec langue, locuteur, qualité, fichier et carte de modèle |
| licence | code actuel GPL-3.0 ; licence de la voix lue dans sa carte et non déduite du moteur |
| formats | paire `.onnx` et `.onnx.json` pour les voix courantes |
| limites | prononciation, vitesse, qualité et couverture linguistique varient par voix |
| alternative | Kokoro pour une autre baseline légère ; Chatterbox lorsque l’expressivité justifie un paquet plus lourd |
| sources officielles | [dépôt Piper actuel](https://github.com/OHF-Voice/piper1-gpl), [releases Piper](https://github.com/OHF-Voice/piper1-gpl/releases), [collection des voix](https://huggingface.co/rhasspy/piper-voices) |
| sources internes | [dépôt actuel de Piper](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#71-dépôt-actuel), [backend Piper](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#backend-08--piper) |
| preuve | dépôt et release revus le `2026-07-28` ; aucun modèle de voix téléchargé |

**Décision de consultation :** un changement de voix est un changement de dépendance. Le nom `Piper` ne suffit jamais à identifier le résultat attendu ou ses droits.

---

<!-- l5:card -->
## AUDIO-03 — Chatterbox

| Champ | Référence datée |
|---|---|
| famille | Chatterbox de Resemble AI, avec variantes Multilingual V3, Turbo et Nano |
| variantes observées | Multilingual V3 autour de 500M et plus de 23 langues annoncées ; Turbo 350M et Nano 110M orientés anglais |
| fonction | voix expressive, adaptation ou clonage contrôlé selon variante |
| langues | le français appartient à la branche multilingue annoncée ; ne pas l’inférer pour Turbo ou Nano |
| composants | modèle, tokenizer, référence vocale éventuelle, vocodeur, paramètres d’expressivité et moteur Python |
| licence | dépôt et cartes officielles annoncés sous MIT ; références vocales et sorties restent juridiquement séparées |
| consentement | toute adaptation d’une personne identifiable exige une autorisation préalable, explicite et archivée |
| performance | les vitesses publiées par l’éditeur ne sont pas des mesures du guide ni du Ryzen 7 2700 |
| limites | ressemblance, stabilité, prononciation, émotions, dérives et contenu sensible nécessitent une écoute humaine |
| alternative | Kokoro ou Piper lorsqu’aucune référence vocale ni forte expressivité n’est requise |
| sources officielles | [dépôt Chatterbox](https://github.com/resemble-ai/chatterbox), [carte Multilingual V3](https://huggingface.co/ResembleAI/chatterbox), [carte Turbo](https://huggingface.co/ResembleAI/chatterbox-turbo) |
| sources internes | [clonage contrôlé](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#8-chatterbox--voix-expressive-et-clonage-contrôlé), [consentement vocal](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#26-voix-et-artistes-interprètes) |
| preuve | sources Resemble AI revues le `2026-07-28` ; aucune référence vocale fournie ni sortie produite |

**Décision de consultation :** le clonage n’est jamais le mode par défaut. Sans consentement explicite et périmètre d’usage, le statut reste `blocked`.

---

<!-- l5:card -->
## AUDIO-04 — Whisper

| Champ | Référence datée |
|---|---|
| famille | OpenAI Whisper, famille STT multilingue et de traduction |
| tailles officielles | tiny 39M, base 74M, small 244M, medium 769M, large 1550M et turbo 809M |
| fonction | transcription, détection de langue et, selon modèle, traduction vers l’anglais |
| variante turbo | optimisée pour la transcription ; elle ne doit pas être utilisée comme équivalent de traduction |
| composants | checkpoint, tokenizer, prétraitement log-Mel, décodage, VAD optionnel et moteur |
| moteurs | OpenAI Whisper, faster-whisper/CTranslate2 ou whisper.cpp ; le moteur reste propriétaire de l’exécution |
| licence | code et poids officiels sous MIT ; audio d’entrée et transcription gardent leurs propres droits |
| local | `small` sert de point de départ documentaire pour le français ; aucune précision ou vitesse n’est présumée |
| limites | omissions, répétitions, hallucinations, langue erronée, noms propres et timestamps doivent être relus |
| alternative | modèle plus petit pour un test rapide, medium ou large pour comparaison hors temps réel |
| sources officielles | [dépôt OpenAI Whisper](https://github.com/openai/whisper), [carte Whisper large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo) |
| sources internes | [modèle de départ](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#94-modèle-de-départ), [faster-whisper](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#backend-06--faster-whisper-et-ctranslate2), [whisper.cpp](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#backend-07--whispercpp) |
| preuve | dépôt et cartes OpenAI revus le `2026-07-28` ; aucun audio transcrit |

**Décision de consultation :** comparer les checkpoints avec le même audio, la même langue et le même protocole. Une transcription n’est publiable qu’après relecture de l’audio original.

---

<!-- l5:card -->
## AUDIO-05 — MusicGen

| Champ | Référence datée |
|---|---|
| famille | MusicGen dans AudioCraft |
| tailles documentées | small 300M, medium et melody 1.5B, large 3.3B |
| fonction | génération de maquettes musicales à partir de texte et, pour certaines variantes, d’une mélodie |
| composants | modèle MusicGen, encodeur texte, codec EnCodec 32 kHz, moteur AudioCraft et paramètres de durée |
| licence | code AudioCraft MIT ; poids publiés sous CC-BY-NC 4.0 |
| usage | recherche d’ambiance, structure, rythme ou référence temporaire non commerciale |
| mémoire | l’éditeur recommande 16 Go de GPU pour medium ; cette valeur ne qualifie ni AMD Windows ni la RX 6750 XT |
| limites | structure longue, boucle, mix, droits, ressemblances et répétitions doivent être évalués |
| alternative | composition originale, prestataire, bibliothèque licenciée ou modèle aux droits compatibles |
| sources officielles | [dépôt AudioCraft](https://github.com/facebookresearch/audiocraft), [documentation MusicGen](https://facebookresearch.github.io/audiocraft/docs/MUSICGEN.html) |
| sources internes | [usage autorisé dans le guide](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#142-usage-autorisé-dans-le-guide), [droits des musiques et enregistrements](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#25-musiques-sons-et-enregistrements) |
| preuve | sources Meta revues le `2026-07-28` ; aucune musique générée |

**Décision de consultation :** les poids officiels servent uniquement aux maquettes non commerciales tant qu’aucune base juridique différente n’est approuvée.

---

<!-- l5:card -->
## AUDIO-06 — AudioGen

| Champ | Référence datée |
|---|---|
| famille | AudioGen dans AudioCraft |
| taille documentée | variante medium 1.5B dans la documentation officielle |
| fonction | génération de bruitages et scènes sonores depuis une description textuelle |
| composants | modèle AudioGen, encodeur texte, codec EnCodec 16 kHz, moteur AudioCraft et paramètres de durée |
| licence | code AudioCraft MIT ; poids publiés sous CC-BY-NC 4.0 |
| usage | idées d’impact, textures, créatures, ambiances et variations destinées au montage |
| mémoire | la documentation demande au moins 16 Go de GPU ; aucune exécution locale n’est déduite |
| limites | voix indésirable, musique parasite, continuité, perspective, bruit et détails inventés doivent être contrôlés |
| postproduction | toute sortie reste un brouillon à écouter, découper, nettoyer et documenter |
| alternative | enregistrement, synthèse procédurale, bibliothèque licenciée ou sound design manuel |
| sources officielles | [dépôt AudioCraft](https://github.com/facebookresearch/audiocraft), [documentation AudioGen](https://facebookresearch.github.io/audiocraft/docs/AUDIOGEN.html) |
| sources internes | [AudioGen dans le Livre I](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#15-génération-deffets-avec-audiogen), [nettoyage non destructif](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#15-nettoyage-non-destructif) |
| preuve | sources Meta revues le `2026-07-28` ; aucun bruitage généré |

**Décision de consultation :** AudioGen reste une source exploratoire. La sortie ne devient ni un master, ni un effet publiable par simple nettoyage.

---

<!-- l5:matrix -->
## Matrice B — Compatibilité du paquet

| Composant | Doit correspondre à | Symptôme d’incompatibilité | Preuve minimale |
|---|---|---|---|
| modèle principal | architecture, variante et chargeur | poids refusés, sortie vide ou erreur de forme | fichier exact chargé dans le moteur qualifié |
| tokenizer ou phonémiseur | langue, symboles et modèle | mots ignorés, noms déformés ou caractères rejetés | version, langue et phrase témoin enregistrées |
| voix | architecture TTS et configuration | timbre absent, hauteur incohérente ou échec de chargement | fichier, carte, licence et locuteur identifiés |
| vocodeur | représentation acoustique et fréquence | bruit, débit erroné ou audio inutilisable | vocodeur recommandé ou comparaison documentée |
| codec neuronal | modèle de génération et fréquence | artefacts, durée ou décodage incorrects | version et fréquence conformes au paquet |
| VAD | moteur STT et seuils | mots coupés, silences transcrits ou segments manquants | audio témoin, seuils et comparaison sans VAD |
| diarisation | nombre de locuteurs et pipeline | attribution erronée ou chevauchement perdu | échantillon autorisé et revue humaine |
| moteur | format des poids, API et backend | option absente, fallback ou résultat divergent | version, commit, options et journal |
| backend | opérations et précision réellement prises en charge | lenteur, erreur mémoire ou sortie différente | comparaison CPU et mesures sur le matériel |
| licence et consentement | chaque fichier, voix, entrée et usage | publication ou entraînement bloqués | textes archivés et décision humaine |

La [séparation des environnements audio](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#1-objet-du-chapitre) évite de traiter TTS, STT, musique et effets comme un seul runtime. La [source, le master et l’export](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#7-séparer-source-travail-master-et-export-runtime) gardent également des identités distinctes.

---

<!-- l5:card -->
## AUDIO-07 — Voix, locuteur et consentement

| Champ | Référence |
|---|---|
| besoin | rattacher une voix synthétique ou adaptée à une origine, un locuteur et des usages autorisés |
| réponse rapide | créer un identifiant de voix séparé du modèle et du fichier de référence |
| locuteur | personne réelle, voix construite, acteur, fournisseur ou statut inconnu |
| droits | fixation, reproduction, communication, adaptation, langues, plateformes, durée et promotion |
| synthèse | distinguer TTS générique, adaptation, clonage, conversion de voix et entraînement |
| consentement | explicite, préalable, vérifiable, limité et révocable selon le cadre retenu |
| données | prises brutes, références et documents de consentement restent hors dépôt public |
| retrait | bloquer les nouvelles générations, retrouver les dérivés, remplacer les assets et conserver les preuves |
| limites | une licence de modèle ou une ressemblance convaincante ne prouve aucun droit sur une personne |
| alternative | voix générique autorisée, acteur enregistré, nouvelle voix construite ou texte sans voix |
| sources internes | [aucun clonage sans consentement](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#23-aucun-clonage-sans-consentement-explicite), [registre de consentement](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#26-voix-et-artistes-interprètes) |
| preuve | règle de gouvernance ; aucun consentement ou enregistrement personnel traité dans cette fiche |

---

<!-- l5:card -->
## AUDIO-08 — Phonémiseur, tokenizer, vocodeur et codec

| Champ | Référence |
|---|---|
| besoin | identifier les composants qui transforment texte, représentations acoustiques et signal audio |
| réponse rapide | enregistrer chaque composant lorsque son remplacement peut modifier la sortie |
| tokenizer | découpe le texte ou les symboles attendus par le modèle |
| phonémiseur | convertit les mots en unités de prononciation selon langue, dictionnaire et règles |
| vocodeur | reconstruit le signal depuis une représentation acoustique |
| codec neuronal | encode et décode des tokens audio pour certaines familles de musique ou d’effets |
| fréquence | modèle, vocodeur et codec doivent partager les paramètres attendus |
| licence | espeak-ng, vocodeur, codec et modèles possèdent leurs propres textes |
| validation | même texte ou représentation, mêmes composants, puis écoute des consonnes, silences, artefacts et durée |
| alternative | paquet monolithique seulement lorsque ses composants restent identifiables et versionnés |
| sources internes | [formats et fréquences du projet](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#4-formats-audio-du-projet), [spécification des échantillons](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#21-fréquence-déchantillonnage-profondeur-et-canaux) |
| preuve | revue statique ; aucun composant audio chargé |

---

<!-- l5:card -->
## AUDIO-09 — VAD, diarisation et nettoyage

| Champ | Référence |
|---|---|
| besoin | préparer un enregistrement et séparer parole, silence ou locuteurs sans altérer la source |
| réponse rapide | conserver l’original, versionner le prétraitement et comparer chaque étape |
| VAD | détection d’activité vocale ; seuils, durée minimale et marges influencent les segments |
| diarisation | attribution de segments à des locuteurs ; ce n’est ni une identification légale ni une vérité automatique |
| nettoyage | conversion, réduction de bruit et normalisation restent non destructives et auditées |
| risques | consonnes coupées, silences inventés, chevauchements perdus, locuteurs fusionnés ou texte halluciné |
| données | enregistrements et transcriptions peuvent contenir des données personnelles |
| validation | audio propre, bruité, deux locuteurs, noms et nombres, silences et chevauchement |
| alternative | segmentation manuelle, transcription humaine ou pipeline sans diarisation |
| sources internes | [validation humaine STT](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#95-validation-humaine), [nettoyage non destructif](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#15-nettoyage-non-destructif) |
| preuve | protocole défini ; aucun fichier préparé ou segmenté |

---

<!-- l5:card -->
## AUDIO-10 — Langues, prononciation et localisation

| Champ | Référence |
|---|---|
| besoin | vérifier qu’un paquet traite la langue, la voix et le vocabulaire réellement utilisés par le jeu |
| réponse rapide | tester par locale, voix et tâche ; ne pas déduire le français d’une étiquette « multilingue » |
| français | accents, élisions, liaisons, nombres, dates, sigles, noms fictifs et ponctuation |
| variante régionale | `fr-FR`, autres locales francophones, accent et registre sont enregistrés séparément |
| TTS | intelligibilité, naturel, stabilité, rythme, émotions et dictionnaire de prononciation |
| STT | taux d’erreurs relu, noms propres, chiffres, ponctuation, timestamps et silences |
| musique et SFX | les mots du prompt ne garantissent ni genre, ni culture, ni absence de voix |
| accessibilité | sous-titres, descriptions sonores et synchronisation restent édités humainement |
| validation | corpus autorisé identique, grille fermée, plusieurs locuteurs ou voix et contexte de jeu |
| alternative | nouvelle voix, dictionnaire, découpage, réenregistrement ou relecture humaine |
| sources internes | [dictionnaire de prononciation](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#163-dictionnaire-de-prononciation), [sous-titres et accessibilité](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#17-sous-titres-et-accessibilité) |
| preuve | grille préparée ; aucune langue ou voix évaluée |

---

<!-- l5:card -->
## AUDIO-11 — Voix et dérivés communautaires

| Champ | Référence |
|---|---|
| besoin | qualifier une voix, conversion, fine-tune, checkpoint ou quantification publié par un tiers |
| réponse rapide | partir du fichier exact et reconstruire modèle de base, locuteur, données et conditions |
| identité | auteur, plateforme, page, version, fichier, taille, SHA-256 et configuration |
| locuteur | personne, pseudonyme, voix construite, origine inconnue ou mélange |
| dérivation | base, entraînement, conversion, quantification, phonémiseur, vocodeur et dataset déclaré |
| licence | licence propre, licences héritées, droit sur la prestation et consentement |
| démonstrations | échantillons promotionnels ne prouvent ni fichier, ni absence de traitement, ni autorisation |
| sécurité | archives, code distant et formats sérialisés restent non fiables avant revue |
| statut | `intake`, `quarantined`, `under_review`, `accepted_limited`, `accepted` ou `blocked` |
| alternative | voix officielle documentée, enregistrement interne autorisé ou synthèse générique |
| sources internes | [cycle de vie des assets](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#6-cycle-de-vie-et-statuts), [chaîne IA](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#20-modèles-ia-datasets-et-extensions) |
| preuve | règle de gouvernance ; aucune voix communautaire auditée |

---

<!-- l5:matrix -->
## Matrice C — Workflow de test reproductible

| Test | Variables fixes | Variable observée | Mesures ou revue | Sortie attendue |
|---|---|---|---|---|
| T1 — chargement | modèle, moteur et backend | capacité à charger chaque composant | journal, RAM, VRAM, fallback et durée | statut fonctionnel ou blocage précis |
| T2 — TTS court | texte, voix et paramètres | modèle ou variante | facteur temps réel, durée, coupures et intelligibilité | WAV témoin et rapport d’écoute |
| T3 — TTS long | voix, texte et format | segmentation ou longueur | stabilité du locuteur, respirations, dérive et mémoire | limite de segment retenue |
| T4 — français | paquet et paramètres | corpus français | accents, noms, nombres, rythme et erreurs | grille linguistique |
| T5 — consentement | modèle et workflow | référence vocale | périmètre, ressemblance, dérives et retraits | acceptation limitée ou blocage |
| T6 — STT propre | audio, langue et moteur | checkpoint Whisper | temps, erreurs relues, timestamps et omissions | transcription annotée |
| T7 — STT dégradé | même texte de référence | bruit, silence ou VAD | hallucinations, mots coupés et segments | réglage ou repli retenu |
| T8 — musique | prompt, durée et modèle | seed ou variante | structure, boucle, artefacts, mémoire et droits | maquette non commerciale |
| T9 — SFX | prompt, durée et modèle | variante | pertinence, perspective, voix parasite et montage requis | brouillon ou rejet |
| T10 — reproductibilité | paquet et entrées inchangés | répétition ou backend | octets, durée, contenu, erreurs et versions | allégation exacte ou comparable |
| T11 — postproduction | source générée | chaîne de nettoyage | artefacts, loudness, crête, silences et provenance | master candidat |
| T12 — revue humaine | sorties anonymisées et critères | candidat | qualité, fonction, culture, droits et accessibilité | sélection, rejet ou nouvelle expérience |

Le [plan de benchmarks audio](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#20-benchmarks) fournit les dimensions de mesure. Les résultats exécutés appartiendront au chapitre 21 du Livre V ; cette matrice ne contient aucune valeur préremplie.

---

<!-- l5:card -->
## AUDIO-12 — Manifeste et acceptation

| Champ | Valeur à enregistrer |
|---|---|
| paquet | identifiant, fonction, propriétaire, statut et date de décision |
| composants | rôle, fournisseur, dépôt, révision, fichier, taille, empreinte et format |
| voix | identifiant, langue, locuteur, source, carte, licence et consentement |
| compatibilité | moteur, backend, OS, matériel, précision et versions réellement testés |
| entrées | texte, audio, prompt, référence, droits, empreintes et politique de données |
| paramètres | langue, voix, seed, température, vitesse, expressivité, VAD, durée et fréquence |
| sorties | identifiants de runs, audio témoin, transcription, empreintes et rapport humain |
| performance | chargement, facteur temps réel, RAM, VRAM et stabilité sans valeur inventée |
| qualité | intelligibilité, prononciation, erreurs STT, artefacts, structure et fonction |
| droits | code, poids, voix, dataset, entrée, sortie, attribution et restrictions |
| décision | `accepted`, `accepted_limited`, `blocked`, `withdrawn` ou `superseded` |
| retrait | références, sorties, masters et exports affectés, remplacement et preuves conservées |

**Porte minimale :** aucun paquet n’est `accepted` sans identité complète, licences relues, voix et consentements qualifiés, sortie témoin, écoute humaine, mesures datées et repli documenté. Le [niveau de preuve du pipeline audio](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#3-niveau-de-preuve-et-réserves) interdit de confondre cette fiche avec une production matérialisée.

**Frontières :**

- la fiche 03 possède les applications et outils audio ;
- la fiche 04 possède moteurs, API et backends d’inférence ;
- la fiche 07 possède familles, voix et composants des modèles audio ;
- la fiche 08 possédera les workflows réutilisables ;
- le chapitre 19 possédera la référence audio transversale ;
- le chapitre 21 possédera les mesures exécutées ;
- le chapitre 22 possédera les compatibilités historiques ;
- le chapitre 25 possédera l’inventaire transversal des licences et consentements ;
- la prise, le montage, le mix et l’intégration Godot restent dans le Livre III.

**Niveau de preuve :** `static-review`. Aucun modèle, voix, référence, enregistrement ou échantillon n’a été téléchargé ; aucun moteur n’a chargé de poids ; aucune synthèse, transcription, musique, effet, mesure, écoute, approbation juridique ou production PDF n’a été réalisée.
