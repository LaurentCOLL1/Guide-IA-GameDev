---
title: "Livre V — Fiche 19 : Référence audio"
id: "DOC-L5-CH19"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 19
last-verified: "2026-07-29T15:46:00+02:00"
audit-status: "complete"
audit-date: "2026-07-29T15:46:00+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-19.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "audio-signal-assets-and-runtime-reference"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Référence audio

> **Type de document :** tables techniques, cartes de convention, matrices de choix, diagrammes compacts et index de diagnostic audio.
> **Référence projet :** Godot `4.7.1-stable`, édition Standard, `Project Asteria`, chaîne de production locale documentée dans les Livres I et III.
> **Principe :** un fichier audible n’est pas automatiquement une source autorisée, un master, un export runtime, un mix validé ou une preuve de qualité.

## Index express

| Besoin | Ouvrir |
|---|---|
| définir le contrat d’une référence audio | [AUDR-00](#audr-00--contrat-dune-référence-audio) |
| trouver la méthode propriétaire | [Matrice A](#matrice-a--entrée-par-problème-ou-livrable) |
| vérifier fréquence, profondeur et canaux | [AUDR-01](#audr-01--signal-fréquence-profondeur-et-canaux) |
| distinguer dBFS, RMS, LUFS et crête vraie | [AUDR-02](#audr-02--niveaux-loudness-crête-vraie-et-dynamique) |
| séparer source, master et export | [AUDR-03](#audr-03--cycle-de-vie-identité-et-provenance) |
| choisir WAV, FLAC, Ogg, MP3 ou Opus | [Matrice B](#matrice-b--formats-et-chemins-dusage) |
| préparer import et réimportation Godot | [AUDR-04](#audr-04--formats-import-et-réimportation-godot) |
| préparer une boucle ou une transition | [AUDR-05](#audr-05--boucles-régions-transitions-et-variantes) |
| classer voix, SFX, ambiance, musique et UI | [AUDR-06](#audr-06--familles-audio-événements-et-variantes) |
| configurer une source audio 3D | [AUDR-07](#audr-07--spatialisation-auditeur-atténuation-et-doppler) |
| organiser les bus et états de mix | [AUDR-08](#audr-08--bus-effets-snapshots-et-ducking) |
| relier voix, TTS, STT et lip-sync | [AUDR-09](#audr-09--voix-tts-stt-localisation-et-synchronisation) |
| préparer captions et alternatives sonores | [AUDR-10](#audr-10--accessibilité-audio-captions-et-redondance) |
| encadrer mémoire, concurrence et latence | [AUDR-11](#audr-11--budgets-profils-presets-et-mesures) |
| distinguer les niveaux de preuve | [Matrice C](#matrice-c--preuves-et-portes-de-promotion) |
| diagnostiquer un défaut audio | [AUDR-12](#audr-12--symptômes-diagnostics-et-acceptation) |

---

<!-- l5:card -->
## AUDR-00 — Contrat d’une référence audio

| Champ | Question obligatoire |
|---|---|
| besoin | quelle information ou sensation le son doit-il représenter |
| famille | voix, SFX, ambiance, musique, UI, narration ou signal accessible |
| source | prise, génération, bibliothèque licenciée, synthèse système ou dérivé |
| identité | quel identifiant stable relie source, master, export, import et événement |
| signal | fréquence, profondeur, canaux, durée et éventuelles régions temporelles |
| niveau | quelle métrique, quelle fenêtre, quelle unité et quel contexte de mix |
| format | quel conteneur ou codec sert au travail, à l’archive, au runtime ou à l’échange |
| lecture | 2D, 3D, boucle, one-shot, stream, stem, transition ou narration |
| routage | quel bus, quelle priorité, quels effets et quelle politique de concurrence |
| langue | quelle locale, quel locuteur, quelle transcription et quel repli |
| droits | quelles licences, autorisations, consentements, attributions et restrictions |
| preuve | revue statique, écoute, mesure, import, test build ou acceptation humaine |
| réserve | quelle étape n’a pas été exécutée, mesurée ou juridiquement qualifiée |
| retrait | quel changement de source, voix, licence, profil ou plateforme invalide le résultat |

**Réponse rapide :** partir du [contrat de paquet audio de la fiche 07](CHAPITRE-07-Fiches-des-modeles-audio.md#audio-00--contrat-dun-paquet-audio), puis rejoindre la [chaîne de production audio propriétaire](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#1-rôle-du-chapitre). Le présent document indexe les conventions ; il ne remplace ni l’installation du [Livre I](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#1-objet-du-chapitre), ni la production, ni le mix.

**Diagramme compact :** `intention → source autorisée → travail non destructif → master → export runtime → import → lecture et mix → mesure → décision`.

**Limite :** une valeur de niveau, de débit ou de mémoire sans fichier, méthode, build, plateforme et scène de test n’est pas une cible approuvée.

---

<!-- l5:matrix -->
## Matrice A — Entrée par problème ou livrable

| Problème ou livrable | Carte | Source propriétaire |
|---|---|---|
| fichier lu trop vite, trop lentement ou avec hauteur incorrecte | [AUDR-01](#audr-01--signal-fréquence-profondeur-et-canaux) | [fréquence, profondeur et canaux](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#21-fréquence-déchantillonnage-profondeur-et-canaux) |
| saturation, volume incohérent ou mix trompeur | [AUDR-02](#audr-02--niveaux-loudness-crête-vraie-et-dynamique) | [crête, RMS et loudness](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#17-comprendre-niveau-de-crête-rms-et-loudness) |
| source, master et fichier Godot confondus | [AUDR-03](#audr-03--cycle-de-vie-identité-et-provenance) | [cycle de vie audio](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#7-séparer-source-travail-master-et-export-runtime) |
| choix de format pour un son court ou long | [Matrice B](#matrice-b--formats-et-chemins-dusage) | [WAV, Ogg Vorbis et MP3 dans Godot](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#20-choisir-wav-ogg-vorbis-ou-mp3-dans-godot) |
| silence supprimé ou timing cassé après import | [AUDR-04](#audr-04--formats-import-et-réimportation-godot) | [import des échantillons](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#22-importer-les-échantillons-dans-godot) |
| clic ou rupture à la répétition | [AUDR-05](#audr-05--boucles-régions-transitions-et-variantes) | [boucle sans clic](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#23-préparer-une-boucle-sans-clic) |
| répétition audible d’un même SFX | [AUDR-06](#audr-06--familles-audio-événements-et-variantes) | [variantes et anti-répétition](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#25-variantes-et-anti-répétition) |
| source 3D large, imprécise ou inaudible | [AUDR-07](#audr-07--spatialisation-auditeur-atténuation-et-doppler) | [`AudioStreamPlayer3D`](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#30-utiliser-audiostreamplayer3d-pour-une-source-localisée) |
| dialogue masqué par musique ou ambiance | [AUDR-08](#audr-08--bus-effets-snapshots-et-ducking) | [ducking et priorité de la voix](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#36-ducking-et-priorité-de-la-voix) |
| voix, modèle TTS et consentement confondus | [AUDR-09](#audr-09--voix-tts-stt-localisation-et-synchronisation) | [voix, locuteur et consentement](CHAPITRE-07-Fiches-des-modeles-audio.md#audio-07--voix-locuteur-et-consentement) |
| doublage et texte d’une locale désalignés | [AUDR-09](#audr-09--voix-tts-stt-localisation-et-synchronisation) | [locales prises en charge](../Livre-IV/CHAPITRE-19-Localisation-et-internationalisation.md#5-concevoir-les-locales-prises-en-charge) |
| information critique portée seulement par le son | [AUDR-10](#audr-10--accessibilité-audio-captions-et-redondance) | [redondance des signaux](../Livre-IV/CHAPITRE-18-Accessibilite.md#7-redonder-linformation-critique) |
| trop de voix simultanées ou coût supposé | [AUDR-11](#audr-11--budgets-profils-presets-et-mesures) | [polyphonie et concurrence](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#38-polyphonie-concurrence-et-voix-simultanées) |
| décision de publication d’un asset audio | [AUDR-12](#audr-12--symptômes-diagnostics-et-acceptation) | [pilote audio Asteria](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#5-pilote-audio-de-project-asteria) |

**Décision :** partir du symptôme ou du livrable, vérifier d’abord la source et le signal, puis seulement l’import, le mix et le runtime. Un même défaut audible peut provenir de la prise, du montage, du codec, du routage, de la scène ou du dispositif d’écoute.

---

<!-- l5:card -->
## AUDR-01 — Signal, fréquence, profondeur et canaux

| Élément | Signification | Convention de référence |
|---|---|---|
| fréquence d’échantillonnage | nombre d’échantillons par seconde | master candidat à `48 kHz` ; conserver la fréquence native pendant la génération |
| profondeur PCM | résolution d’amplitude d’un échantillon | prise candidate en `24 bits`, travail possible en flottant selon l’outil |
| canaux | organisation mono, stéréo ou multicanal | mono privilégié pour une source 3D ponctuelle |
| durée | nombre d’échantillons divisé par la fréquence | conserver aussi les positions de boucle en échantillons |
| interleaving | ordre des échantillons entre canaux | dépend du format et de l’outil ; ne pas le déduire du nom |
| resampling | conversion de fréquence | une étape contrôlée plutôt que plusieurs conversions successives |
| downmix | réduction du nombre de canaux | écouter les annulations de phase et la perte d’information |
| upmix | création de canaux supplémentaires | ne crée aucune information spatiale absente de la source |
| normalisation | changement de gain selon une règle | ne répare ni une prise saturée ni un mix incohérent |

**Réponse rapide :** les repères historiques du projet sont détaillés dans les [formats audio du Livre I](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#4-formats-audio-du-projet) et la [spécification du signal du Livre III](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#21-fréquence-déchantillonnage-profondeur-et-canaux). Ils constituent un point de départ, pas une obligation universelle pour chaque source.

**Diagramme compact :** `durée = nombre d’échantillons ÷ fréquence ; mono/stéréo décrit les canaux, pas la position gameplay`.

**Validation minimale :** fréquence déclarée, durée attendue, absence de changement de hauteur, canaux conformes à l’usage, un seul rééchantillonnage documenté et downmix écouté.

**Limite :** une fréquence plus élevée ou une profondeur supérieure ne garantit pas une meilleure qualité lorsque la source, le microphone, le codec ou l’écoute sont limitants.

---

<!-- l5:card -->
## AUDR-02 — Niveaux, loudness, crête vraie et dynamique

| Mesure | Question répondue | Réserve |
|---|---|---|
| gain | quelle multiplication est appliquée au signal | dépend du point de la chaîne |
| dBFS | où se situe un niveau numérique par rapport au maximum pleine échelle | zéro dBFS n’est pas une cible de mix |
| sample peak | quel échantillon atteint le maximum | ignore les crêtes inter-échantillons |
| true peak | quelles crêtes peuvent apparaître à la reconstruction | dépend de l’algorithme et du suréchantillonnage |
| RMS | quelle énergie moyenne existe sur une fenêtre | fenêtre et canaux doivent être consignés |
| LUFS intégrés | quel loudness moyen pondéré couvre un programme | peu adapté seul à un one-shot très court |
| loudness court terme | comment évolue le niveau perçu sur une fenêtre courte | méthode et durée restent obligatoires |
| plage dynamique | quel écart existe entre passages faibles et forts | ne se résume pas à un compresseur activé |
| headroom | quelle marge reste avant un plafond défini | la compression avec perte peut recréer des crêtes |

**Réponse rapide :** ne jamais remplacer une métrique par une autre. Le [chapitre 26 distingue crête, RMS et loudness](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#17-comprendre-niveau-de-crête-rms-et-loudness) et réserve les [objectifs de loudness](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#18-objectifs-candidats-de-loudness) à des profils mesurés dans le mix réel.

**Contrat de mesure :** enregistrer fichier, version, famille, métrique, unité, fenêtre, canaux, outil, réglages, encodage, dispositif d’écoute, scène, build et date.

**Alternative :** pour un SFX court, comparer crête vraie, forme temporelle et lisibilité dans le mix ; pour une musique longue, compléter par loudness intégré, sections et transitions.

**Limite :** aucun nombre de LUFS, de dBFS ou de réduction de gain n’est universel pour tous les jeux, plateformes, modes d’écoute et fonctions sonores.

---

<!-- l5:card -->
## AUDR-03 — Cycle de vie, identité et provenance

| État | Autorité et usage | Interdit |
|---|---|---|
| source brute | prise, génération ou fichier licencié conservé avec empreinte | écrasement par le nettoyage |
| session de travail | montage, traitements et décisions révisables | confusion avec le master publié |
| rendu de revue | dérivé temporaire pour écoute et commentaires | intégration silencieuse au jeu |
| master édité | autorité haute qualité pour futurs exports | compression destructrice unique sans source |
| export runtime | dérivé par profil de plateforme et famille | remplacement du master |
| ressource importée | dérivé du moteur et de ses options | modification manuelle comme source canonique |
| asset publié | identité, manifeste, droits, master, export et preuve approuvés | publication sans retrait ni propriétaire |

**Réponse rapide :** appliquer la séparation [source, travail, master et export runtime](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#7-séparer-source-travail-master-et-export-runtime). Pour une génération IA, conserver en plus moteur, modèle, révision, paramètres, entrées et droits selon la [chaîne de génération propriétaire](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#14-génération-de-voix-sfx-ou-musique).

**Diagramme compact :** `source immuable → session révisable → master versionné → exports par profil → cache importé régénérable`.

**Provenance minimale :** `asset_id`, source ou session, empreinte, auteur ou fournisseur, licences, consentement éventuel, transformations, versions d’outils, master, exports, propriétaire de décision et procédure de retrait.

**Limite :** le dépôt public ne contient ni contrats signés, ni références vocales restreintes, ni prises personnelles non autorisées.

---

<!-- l5:matrix -->
## Matrice B — Formats et chemins d’usage

| Format ou famille | Usage pertinent | Atout | Vigilance | Statut dans le projet |
|---|---|---|---|---|
| WAV PCM | prise, travail, master ou SFX court sensible à la latence | simple, sans perte, repères d’échantillons précis | taille et mémoire | référence de production selon profil |
| WAV compressé sans perte | import spécifique lorsque qualifié | intégrité avec coût réduit | support et décodage à vérifier | candidat par preset Godot |
| FLAC | archive ou échange sans perte | compression sans perte et métadonnées | ne pas supposer l’import runtime Godot | archive, pas format runtime par défaut |
| Ogg Vorbis | musique, ambiance ou voix longues | compression adaptée aux longs flux | artefacts, décodage et boucles à tester | candidat runtime principal pour flux longs |
| MP3 | compatibilité ou source reçue | diffusion courante | délai d’encodage, padding, génération avec perte | usage spécifique, non choix automatique |
| Opus | prévisualisation, communication ou outil compatible | efficace à bas débit | support direct, conteneur et latence à qualifier | hors preset runtime canonique tant que non testé |
| audio d’un modèle TTS | sortie intermédiaire selon moteur | conserve la fréquence native du modèle | voix, langue, droits et postproduction | brouillon jusqu’à qualification |
| audio STT | entrée de transcription | mono et fréquence contrôlée facilitent la répétition | conversion et VAD peuvent modifier les timings | dérivé de traitement, pas master artistique |

**Décision :** le [Livre I sépare formats de source, archive, échange et export](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#4-formats-audio-du-projet). Pour Godot, suivre le choix [WAV, Ogg Vorbis ou MP3](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#20-choisir-wav-ogg-vorbis-ou-mp3-dans-godot) en fonction de la durée, de la boucle, de la latence, de la mémoire et de la plateforme mesurées.

**Refus contrôlé :** ne pas transcoder une source déjà compressée avec perte vers un autre codec avec perte sans conserver l’original et documenter l’impact.

---

<!-- l5:card -->
## AUDR-04 — Formats, import et réimportation Godot

| Élément | Règle | Contrôle |
|---|---|---|
| source importée | provient d’un export runtime versionné | empreinte et manifeste présents |
| preset | dépend de la famille, durée, boucle, canaux et plateforme | identifiant et version explicites |
| compression | choisie après écoute et mesure | comparer source, encode et décodage |
| loop | activé seulement pour une région conçue comme boucle | répétitions après import |
| trim | désactivé lorsque le silence ou le pré-roll appartient au timing | comparer durée et marqueurs |
| normalize | ne remplace pas le mastering ou la politique de mix | mesurer avant et après |
| force mono | dépend d’une source ponctuelle et d’un contrôle de phase | écouter source et downmix |
| cache importé | dérivé régénérable | ne pas le traiter comme master |
| réimportation | nouvelle transformation à valider | diff de durée, codec, boucle, niveau et canaux |

**Réponse rapide :** versionner un profil par famille, puis appliquer la [procédure d’import audio du chapitre 26](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#22-importer-les-échantillons-dans-godot). La réimportation ne constitue jamais une approbation automatique.

**Validation minimale :** durée, fréquence, canaux, région de boucle, attaque, queue, niveau, artefacts, mémoire candidate, temps de démarrage et routage vers le bon bus.

**Alternative :** un SFX très court peut privilégier un profil différent d’une musique longue ; une voix synchronisée peut conserver un pré-roll qu’un son d’interface n’exige pas.

**Limite :** les options exactes de l’inspecteur dépendent du format et de la version du moteur ; la présente fiche n’enregistre pas un preset exécutable.

---

<!-- l5:card -->
## AUDR-05 — Boucles, régions, transitions et variantes

| Élément | Contrat | Vérification |
|---|---|---|
| loop start et end | positions conservées en échantillons | pas d’arrondi temporel ambigu |
| continuité | niveau, pente, spectre et modulation compatibles | plusieurs répétitions après encodage |
| crossfade | durée et courbe écoutées | absence de phasing ou respiration |
| intro | région jouée une fois avant la boucle | transition sans saut |
| outro | sortie dédiée ou queue séparée | ne pas couper une réverbération utile |
| stinger | événement musical court superposé ou quantifié | priorité et timing explicites |
| grille | temps, battement ou mesure vérifiés | tempo et signature versionnés |
| stems | même origine d’échantillon, durée, tempo et phase | démarrage synchrone |
| variantes | plusieurs prises et choix borné | historique anti-répétition |

**Réponse rapide :** préparer la boucle selon les [contrôles de continuité](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#23-préparer-une-boucle-sans-clic), puis enregistrer les [régions et transitions](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#24-métadonnées-de-boucle-et-transitions). Pour la musique, les [stems et états](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#28-organiser-la-musique-en-stems-et-états) restent une méthode propriétaire.

**Diagramme compact :** `intro → boucle N fois → transition quantifiée ou crossfade → outro ; les limites restent des données versionnées`.

**Refus contrôlé :** un passage par zéro unique, un fade automatique ou un nom contenant `loop` ne prouvent pas une boucle transparente.

**Limite :** les valeurs de pitch, de gain, de durée de crossfade et de taille d’historique sont contextuelles et doivent être écoutées dans la scène réelle.

---

<!-- l5:card -->
## AUDR-06 — Familles audio, événements et variantes

| Famille | Fonction dominante | Lecture habituelle | Vigilance |
|---|---|---|---|
| voix | contenu sémantique et interprétation | 2D, radio, 3D ou cinématique | consentement, langue, intelligibilité, captions |
| SFX | retour d’action, matière ou événement | one-shot, localisé ou non | concurrence, répétition, priorité |
| ambiance | continuité de lieu et climat | lit stéréo, émetteurs mono, événements rares | boucles, mémoire, masquage |
| musique | structure émotionnelle et transition | flux long, stems, intro, loop, outro | synchronisation, ducking, licence |
| UI | confirmation et navigation | non positionnelle et courte | lisibilité, répétition, accessibilité |
| narration | description, tutoriel ou lecture d’interface | bus séparé, interruptible | langue, interruption, débit |
| signal critique | alerte fonctionnelle | priorité élevée et canal redondant | ne pas dépendre du son seul |

**Réponse rapide :** classer par fonction avant de choisir le format. La [typologie fonctionnelle du chapitre 26](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#6-typologie-fonctionnelle-des-ressources-audio) relie chaque famille à ses contraintes, tandis que les [variantes anti-répétition](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#25-variantes-et-anti-répétition) restent des représentations d’un événement déjà validé.

**Contrat d’événement :** l’événement gameplay porte une identité et des données autorisées ; le système audio choisit cue, variante, bus et spatialisation sans modifier le résultat métier.

**Alternative :** une ambiance crédible combine [lit, émetteurs et événements rares](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#27-construire-une-ambiance-en-couches) plutôt qu’un unique fichier stéréo très dense.

**Limite :** la fin de lecture, la détection d’un pic ou la présence d’un fichier ne constituent jamais une preuve de succès gameplay.

---

<!-- l5:card -->
## AUDR-07 — Spatialisation, auditeur, atténuation et Doppler

| Élément | Question | Invariant |
|---|---|---|
| lecteur 2D | le son doit-il rester indépendant de la position | UI et musique généralement non positionnelles |
| lecteur 3D | la source possède-t-elle une position audible | source ponctuelle mono privilégiée |
| auditeur | quel point d’écoute est actif | caméra ou listener de présentation, jamais position métier |
| échelle | quelle unité alimente la courbe | mètres cohérents avec la référence 3D |
| atténuation | comment le niveau évolue avec la distance | courbe écoutée et mesurée dans la scène |
| distance maximale | quand la source cesse-t-elle d’être calculée ou audible | ne définit pas la portée gameplay |
| directionnalité | la source rayonne-t-elle dans un axe | angle cohérent avec l’objet sonore |
| Doppler | le mouvement relatif justifie-t-il une variation de hauteur | désactivé si inutile ou inconfortable |
| filtre de distance | le timbre change-t-il avec l’éloignement | ne masque pas un mauvais mix |
| zone | quel envoi de réverbération représente l’espace | volume acoustique distinct des collisions gameplay |

**Réponse rapide :** utiliser le [lecteur 3D pour une source localisée](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#30-utiliser-audiostreamplayer3d-pour-une-source-localisée), puis qualifier [atténuation, directionnalité et Doppler](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#31-atténuation-directionnalité-et-doppler) avec l’auditeur réellement retenu.

**Diagramme compact :** `événement autorisé → source mono 3D → courbe et zone → auditeur actif → bus → sortie ; aucun maillon ne décide le gameplay`.

**Validation minimale :** proximité, distance moyenne, limite, arrière de la source, passage de zone, mouvement rapide, changement de caméra et écoute mono/stéréo.

**Limite :** le split-screen, la VR, les casques multicanaux et les profils HRTF exigent des conceptions et qualifications distinctes non supposées par cette fiche.

---

<!-- l5:card -->
## AUDR-08 — Bus, effets, snapshots et ducking

| Élément | Rôle | Contrôle |
|---|---|---|
| `Master` | sortie finale | traitements globaux minimaux et justifiés |
| `Music` | musique et stems | transitions, loudness et ducking |
| `Voice` | dialogues et narration | intelligibilité, langue et traitements spécialisés |
| `SFX` | actions, monde et foley | priorité, concurrence et masquage |
| `Ambience` | lits et émetteurs | densité, zones et mémoire |
| `UI` | interface non positionnelle | lisibilité et répétition |
| sous-bus critiques | alertes et signaux indispensables | protégés du vol de voix et du ducking global |
| chaîne d’effets | traitement ordonné | objectif, ordre, bypass et niveau comparables |
| snapshot | offsets relatifs de plusieurs bus | transition bornée et restauration |
| ducking | réduction temporaire par déclencheur | attaque, release, profondeur et absence de pompage |

**Réponse rapide :** partir de l’[architecture des bus Godot](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#33-architecture-des-bus-godot), puis versionner les [presets et états de mix](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#35-presets-et-états-de-mix). Le ducking suit la [priorité de la voix](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#36-ducking-et-priorité-de-la-voix) sans réduire les signaux critiques.

**Diagramme compact :** `lecteurs → bus de famille → sous-bus spécialisés → effets ordonnés → Master → dispositif d’écoute`.

**Alternative :** un snapshot manuel peut être plus prévisible qu’un sidechain lorsqu’une cinématique ou un dialogue possède des bornes temporelles connues.

**Limite :** les offsets en décibels, temps d’attaque, release, seuils, ratios et effets restent candidats jusqu’à écoute et mesure du mix réel.

---

<!-- l5:card -->
## AUDR-09 — Voix, TTS, STT, localisation et synchronisation

| Objet | Autorité | Contrôle indispensable |
|---|---|---|
| modèle TTS | produit un signal selon un paquet identifié | modèle, moteur, voix, phonémiseur, langue et licence séparés |
| voix | locuteur synthétique ou référence autorisée | identité, consentement, usages, durée et retrait |
| texte | contenu source ou localisé | clé stable, version, langue et contexte |
| STT | produit une transcription candidate | timestamps, hallucinations, VAD, langue et revue humaine |
| transcription | texte aligné à une source audio | ne remplace pas le script approuvé sans décision |
| doublage | variante audio d’une locale | couverture séparée de la couverture texte |
| dictionnaire | prononciations et noms propres | versionné par langue et moteur |
| timing | événements temporels pour sous-titres ou visèmes | dérivé de média, pas horloge gameplay |
| lip-sync | mapping phonème-visème et animation | consomme une voix approuvée sans rouvrir ses droits |

**Réponse rapide :** identifier le paquet selon la [fiche des modèles audio](CHAPITRE-07-Fiches-des-modeles-audio.md#audio-00--contrat-dun-paquet-audio), appliquer la règle [aucun clonage sans consentement explicite](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#23-aucun-clonage-sans-consentement-explicite), puis traiter la sortie IA comme une [source intermédiaire](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#24-les-sorties-ia-restent-des-sources-intermédiaires).

**Localisation :** la langue de texte et la langue audio restent des capacités séparées dans le [registre des locales](../Livre-IV/CHAPITRE-19-Localisation-et-internationalisation.md#5-concevoir-les-locales-prises-en-charge). Une voix française validée ne prouve ni sous-titres complets, ni lip-sync d’une autre langue.

**Synchronisation :** le chapitre 27 conserve le [mapping phonème-visème](../Livre-III/CHAPITRE-27-Synchronisation-labiale-et-animation-faciale.md#6-graphème-phonème-allophone-et-visème) et les [variantes de prononciation](../Livre-III/CHAPITRE-27-Synchronisation-labiale-et-animation-faciale.md#7-différences-linguistiques-et-variantes-de-prononciation).

**Limite :** aucune voix, transcription, traduction, prononciation ou synchronisation n’est acceptée sans écoute et revue humaine adaptées à la langue et au contexte.

---

<!-- l5:card -->
## AUDR-10 — Accessibilité audio, captions et redondance

| Besoin | Mécanisme | Porte de validation |
|---|---|---|
| dialogue inaccessible sans son | sous-titres avec locuteur et timing | exactitude, durée de lecture et synchronisation |
| information non verbale utile | captions de sons et musique | catégorie, formulation, direction et priorité |
| menace directionnelle | indicateur visuel ou haptique cohérent | même information, sans révélation supplémentaire |
| voix masquée | volumes séparés, ducking et dynamique réduite | intelligibilité sans destruction du mix |
| écoute sur un seul canal | sortie mono qualifiée | absence d’annulation ou de signal perdu |
| description d’une cinématique | piste de description audio distincte | langue, mix, timing et interruptions |
| interface sans vision | narration ou TTS système | capacité, voix, débit, interruption et plateforme |
| environnement bruyant | captions, réglages de catégories et répétition | parcours sans dépendance exclusive à l’audio |

**Réponse rapide :** une information critique suit la règle de [redondance multimodale](../Livre-IV/CHAPITRE-18-Accessibilite.md#7-redonder-linformation-critique). Les [catégories audio réglables](../Livre-IV/CHAPITRE-18-Accessibilite.md#27-séparer-les-catégories-audio) et les [représentations visuelles des sons utiles](../Livre-IV/CHAPITRE-18-Accessibilite.md#28-représenter-les-sons-utiles-visuellement) complètent le mix sans devenir des capteurs gameplay.

**Captions :** personnaliser taille, fond, locuteur, indices sonores et zones sûres selon la [politique d’affichage](../Livre-IV/CHAPITRE-18-Accessibilite.md#26-personnaliser-laffichage-des-captions).

**Narration :** distinguer piste de description, narration d’interface et [TTS du système](../Livre-IV/CHAPITRE-18-Accessibilite.md#30-encadrer-tts-et-lecteur-décran-dans-godot).

**Limite :** un profil nommé « accessible », « mono » ou « dynamique réduite » ne prouve aucune barrière supprimée tant que les parcours représentatifs ne sont pas exécutés.

---

<!-- l5:card -->
## AUDR-11 — Budgets, profils, presets et mesures

| Dimension | Mesure candidate | Contexte obligatoire |
|---|---|---|
| stockage | octets par export et par lot | codec, qualité, langue et plateforme |
| mémoire | flux chargés, décompressés ou streamés | import, durée, canaux et simultanéité |
| décodage | temps CPU et stabilité | codec, nombre de voix et matériel |
| démarrage | latence entre demande et premier son | cache, stockage, streaming et build |
| concurrence | voix simultanées par famille | scène de saturation et priorités |
| vol de voix | événements coupés ou remplacés | âge, distance, importance et répétition |
| mix | loudness, true peak et intelligibilité | snapshot, bus, écoute et fenêtre |
| spatialisation | coût et lisibilité des sources 3D | nombre, distances, zones et auditeur |
| localisation | taille et couverture par langue audio | locale, doublage, captions et fallback |
| accessibilité | parcours avec audio absent, mono ou bruit ambiant | options, persistance et non-régression |

**Réponse rapide :** les limites de [polyphonie et concurrence](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#38-polyphonie-concurrence-et-voix-simultanées) sont des champs de profil, pas des constantes universelles. La future [fiche 21 — Benchmarks et méthodes de mesure](#limite-de-périmètre) possédera les protocoles transversaux ; ici, chaque budget nomme seulement ce qui doit être mesuré.

**Preset minimal :** famille, source et export, options d’import, mode de lecture, bus, concurrence, spatialisation, plateforme, date, propriétaire, critères et procédure de retrait.

**Profil Solo :** limiter le nombre de variantes et de plateformes, conserver des presets lisibles et mesurer un pilote réduit.

**Profil Studio :** versionner presets, manifests, rapports, responsables, dérogations et campagnes multi-plateformes sans déclarer l’automatisation artistique souveraine.

**Limite de périmètre :** aucun budget chiffré de mémoire, voix, latence, bitrate ou loudness n’est approuvé dans cette fiche.

---

<!-- l5:matrix -->
## Matrice C — Preuves et portes de promotion

| Niveau | Preuve disponible | Déclaration permise | Déclaration interdite |
|---|---|---|---|
| source revue | documentation ou fichier identifié | format ou capacité documentée | qualité audible ou compatibilité runtime |
| manifeste complet | identité, droits, versions et empreintes | traçabilité préparée | publication juridiquement autorisée |
| écoute de source | audition sur un dispositif documenté | défauts observés sur ce fichier | qualité sur tous les appareils |
| mesure de fichier | méthode, unité, fenêtre et outil enregistrés | valeur pour ce fichier et ce protocole | cible universelle de mix |
| import Godot | ressource importée et options conservées | import réussi pour cette version | lecture correcte en build |
| test de scène | lecture, bus, boucle et spatialisation observés | comportement dans ce scénario | performance globale du jeu |
| campagne build | scènes, plateformes et répétitions définies | résultat daté et borné | généralisation à une plateforme non testée |
| revue artistique | écoute humaine responsable et réserves | acceptation artistique de la version | licence ou accessibilité automatiquement validée |
| revue juridique | décision organisationnelle conservée | usage autorisé dans le périmètre décidé | avis juridique général |
| asset publié | toutes les portes requises sont satisfaites | diffusion du dérivé approuvé | réutilisation hors périmètre ou après retrait |

**Décision :** le niveau `static-review` de cette fiche correspond aux deux premières lignes et à la cohérence documentaire. Aucun fichier audio, import, écoute, mesure, test de scène, revue artistique ou décision juridique n’est revendiqué.

---

<!-- l5:card -->
## AUDR-12 — Symptômes, diagnostics et acceptation

<!-- qa:error-correction-index -->

| Symptôme | Première vérification | Causes possibles | Source de correction |
|---|---|---|---|
| hauteur ou vitesse incorrecte | fréquence déclarée et interprétée | métadonnée, resampling, import | [AUDR-01](#audr-01--signal-fréquence-profondeur-et-canaux) |
| saturation ou claquement | forme d’onde, sample peak et true peak | prise saturée, limiteur, encode | [AUDR-02](#audr-02--niveaux-loudness-crête-vraie-et-dynamique) |
| souffle métallique | comparer bypass à niveau égal | réduction de bruit excessive | [nettoyage non destructif](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#15-nettoyage-non-destructif) |
| clic de boucle | limites en échantillons et décodage | discontinuité, padding, phase | [AUDR-05](#audr-05--boucles-régions-transitions-et-variantes) |
| attaque ou fin coupée | durée, trim et pré-roll | import, montage, fade | [AUDR-04](#audr-04--formats-import-et-réimportation-godot) |
| source 3D trop large | nombre de canaux | stéréo intégrée, auditeur, courbe | [AUDR-07](#audr-07--spatialisation-auditeur-atténuation-et-doppler) |
| son inaudible à proximité | stream, bus, gain et distance | bus muet, priorité, atténuation | [AUDR-08](#audr-08--bus-effets-snapshots-et-ducking) |
| dialogue masqué | bus, snapshot et spectre concurrent | musique, ambiance, ducking | [AUDR-08](#audr-08--bus-effets-snapshots-et-ducking) |
| répétition fatigante | historique et ensemble de variantes | trop peu de prises, pitch extrême | [AUDR-06](#audr-06--familles-audio-événements-et-variantes) |
| voix incohérente ou mal prononcée | paquet, voix, langue et dictionnaire | variante de modèle, texte, accent | [AUDR-09](#audr-09--voix-tts-stt-localisation-et-synchronisation) |
| sous-titre désynchronisé | horloge média et version audio | export changé, timing obsolète | [AUDR-10](#audr-10--accessibilité-audio-captions-et-redondance) |
| information perdue en mono | comparer canaux et corrélation | opposition de phase, signal latéral | [AUDR-10](#audr-10--accessibilité-audio-captions-et-redondance) |
| coupures en saturation | journal des voix et priorités | limite, vol de voix, streaming | [AUDR-11](#audr-11--budgets-profils-presets-et-mesures) |
| fichier accepté mais non publiable | registre de droits et consentement | licence, retrait, attribution | [provenance audio](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#4-frontières-avec-les-chapitres-voisins) |

**Diagramme compact :** `symptôme → source et signal → export → import → lecteur et bus → scène et dispositif → preuve ; corriger le premier maillon confirmé`.

**Checklist d’acceptation :** identité stable, provenance et droits, source et master conservés, signal documenté, export et preset versionnés, boucle et timing contrôlés, routage et priorité définis, accessibilité reliée, mesures contextualisées, réserves explicites et propriétaire de décision nommé.

**Pilote :** le lot `AST-AUDIO-PILOT-RELAY-STORM-001` du [chapitre 26](../Livre-III/CHAPITRE-26-Voix-bruitages-ambiances-et-musique.md#5-pilote-audio-de-project-asteria) fournit le périmètre de comparaison futur. Aucun de ses fichiers, bus, captures ou mesures n’est matérialisé ici.

**Limite :** la future fiche 20 possédera le catalogue transversal des erreurs par outil, message et version ; la présente carte reste un index audio compact relié aux méthodes détaillées.

---

## Limites générales

- aucune prise, voix, transcription, musique, ambiance ou SFX n’a été créé ;
- aucun modèle TTS ou STT n’a été exécuté ;
- aucun fichier WAV, FLAC, Ogg, MP3 ou Opus n’a été encodé, importé ou écouté ;
- aucun bus, effet, snapshot, zone, lecteur ou preset Godot n’a été matérialisé ;
- aucune mesure de loudness, true peak, mémoire, latence ou concurrence n’a été enregistrée ;
- aucune revue artistique, linguistique, accessible ou juridique n’a été réalisée ;
- aucune donnée utilisateur, voix personnelle, consentement ou contrat n’a été traité ;
- aucun PDF n’a été produit.

## Synthèse de consultation

Pour une décision audio, identifier d’abord la famille, la source et les droits ; vérifier ensuite le signal et le cycle de vie ; choisir format, import et lecture selon l’usage ; organiser bus, spatialisation, accessibilité et priorités ; enfin mesurer dans une scène et un build définis. Toute valeur, voix ou validation reste bornée à sa preuve.