---
title: "Livre V — Fiche 04 : Fiches des moteurs et backends IA"
id: "DOC-L5-CH04"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 4
last-verified: "2026-07-28T14:25:00+02:00"
audit-status: "complete"
audit-date: "2026-07-28T14:25:00+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-04.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "ai-engines-and-backends"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Fiches des moteurs et backends IA

> **Type de document :** cartes de moteurs, cartes de backends, matrices API/accélération et diagnostic compact.
> **Lecture :** identifier d’abord la couche en cause, puis ouvrir la carte correspondante et le tutoriel propriétaire.
> **Principe :** un moteur charge ou sert un modèle ; un backend exécute les calculs ; une interface pilote le moteur ; une orchestration coordonne plusieurs services. Ces rôles ne sont pas interchangeables.

## Index express

| Besoin | Ouvrir |
|---|---|
| distinguer moteur, backend, modèle et interface | [MOTEUR-00](#moteur-00--contrat-et-vocabulaire) |
| servir simplement un LLM local sous Windows | [MOTEUR-01](#moteur-01--ollama) |
| contrôler précisément GGUF, CPU et offload GPU | [MOTEUR-02](#moteur-02--llamacpp) |
| exposer plusieurs backends derrière une passerelle | [MOTEUR-03](#moteur-03--localai) |
| exécuter des graphes visuels | [MOTEUR-04](#moteur-04--comfyui-comme-moteur-de-workflow) |
| conserver une référence fonctionnelle universelle | [BACKEND-01](#backend-01--cpu) |
| tester une accélération AMD transversale | [BACKEND-02](#backend-02--vulkan) |
| utiliser un repli Windows compatible DirectX | [BACKEND-03](#backend-03--directml) |
| tester une couche CUDA communautaire sur AMD | [BACKEND-04](#backend-04--zluda) |
| qualifier ROCm ou HIP | [BACKEND-05](#backend-05--rocm-et-hip) |
| transcrire avec Python sur CPU | [BACKEND-06](#backend-06--faster-whisper-et-ctranslate2) |
| transcrire avec un moteur autonome | [BACKEND-07](#backend-07--whispercpp) |
| synthétiser une voix légère et embarquable | [BACKEND-08](#backend-08--piper) |
| comparer API, formats et accélérations | [Matrice B](#matrice-b--api-formats-accélération-et-mémoire) |
| partir d’un symptôme | [Matrice C](#matrice-c--diagnostic-par-couches) |

---

<!-- l5:card -->
## MOTEUR-00 — Contrat et vocabulaire

| Terme | Réponse rapide | Exemple | Autorité |
|---|---|---|---|
| moteur | programme qui charge, exécute ou sert un modèle | Ollama, llama.cpp, LocalAI, ComfyUI | version du moteur et journaux |
| backend | implémentation de calcul choisie par le moteur | CPU, Vulkan, DirectML, ZLUDA, ROCm/HIP | détection matérielle et mesure |
| modèle | poids, architecture, tokenizer, voix ou graphe appris | GGUF, modèle Whisper, voix Piper | manifeste, licence, empreinte |
| interface | application utilisée par l’humain | Open WebUI, LibreChat, navigateur ComfyUI | configuration d’endpoint |
| orchestration | coordination de moteurs, files, tâches et politiques | LocalAI, processus compagnon, worker | configuration versionnée |
| API | contrat d’échange, non preuve de compatibilité complète | Ollama native, sous-ensemble OpenAI | endpoints réellement testés |

**Réponse rapide :** diagnostiquer dans l’ordre modèle → moteur → backend → API → interface. Une interface qui affiche une réponse ne prouve ni le backend utilisé ni la conformité du modèle.

**Sources propriétaires :** [objet et distinction des composants](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#1-objet-du-chapitre), [une interface n’est pas un moteur](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#33-une-interface-nest-pas-un-moteur), [frontière de service dans Godot](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md#3-périmètre-et-frontières).

---

<!-- l5:matrix -->
## Matrice A — Couche, responsabilité et preuve

| Couche | Question à poser | Preuve minimale | Ne prouve pas |
|---|---|---|---|
| modèle | quel artefact exact est chargé ? | identifiant, révision, format, quantification, empreinte, licence | que le moteur l’exécute correctement |
| moteur | quel binaire ou service répond ? | version, build ou commit, journal de démarrage | que le GPU travaille |
| backend | où les calculs sont-ils exécutés ? | détection CPU/GPU, mémoire, journal et mesure comparative | que la qualité est identique |
| API | quel endpoint et quel sous-ensemble sont utilisés ? | requête de santé puis appel réel du client | une compatibilité OpenAI universelle |
| interface | vers quelle adresse pointe-t-elle ? | endpoint, modèle sélectionné et réponse corrélée | que le moteur local est sûr |
| orchestration | quelles files, limites et reprises existent ? | configuration, healthcheck, quotas et arrêt contrôlé | qu’une tâche longue est idempotente |

**Règle :** la [fiche 02](CHAPITRE-02-Arbres-de-decision.md#dec-00--lire-un-arbre-sans-transformer-une-préférence-en-fait) décide entre les voies ; cette fiche décrit ce que chaque voie implique. Les modèles et leurs licences détaillées appartiennent aux chapitres 5 à 7.

---

<!-- l5:matrix -->
## Matrice B — API, formats, accélération et mémoire

| Moteur ou backend | API ou interface principale | Format ou artefact | Voie CPU | Voie AMD Windows | Mémoire à surveiller | Statut dans la collection |
|---|---|---|---|---|---|---|
| Ollama | API native et sous-ensemble compatible OpenAI | catalogue géré, Modelfile, modèles servis | oui | support standard à mesurer, Vulkan expérimental | RAM, VRAM, contexte, modèles chargés | moteur LLM principal |
| llama.cpp | CLI, serveur local, benchmark | GGUF | référence obligatoire | Vulkan à mesurer ; HIP seulement si qualifié | RAM, VRAM, cache KV, couches offloadées | référence et diagnostic |
| LocalAI | API compatible et passerelle multi-backends | YAML, modèles et images conteneur | parcours Docker Windows | GPU non présumé dans Docker Desktop Windows | RAM, volumes, workers, files | option Studio ou besoin multi-backend |
| ComfyUI | interface nodale et API de workflow | workflow JSON, modèles, nœuds | référence fonctionnelle | ZLUDA laboratoire ; DirectML secours ; ROCm séparé | VRAM, RAM, VAE, modèles et nœuds | moteur visuel |
| Vulkan | interface graphique ou calcul selon moteur | backend compilé avec le moteur | repli disponible hors Vulkan | voie AMD expérimentale ou qualifiée par moteur | VRAM et stabilité pilote | laboratoire mesuré |
| DirectML | backend Windows via DirectX | environnement Python séparé | repli obligatoire | possible mais dégradé selon outil | VRAM, copies mémoire, latence | secours |
| ZLUDA | couche de traduction communautaire | DLL et environnement isolé | repli obligatoire | expérimental | VRAM, compatibilité pilote et bibliothèques | laboratoire |
| ROCm/HIP | pile AMD native ou backend compilé | runtime, build et bibliothèques | repli obligatoire | support dépendant du GPU, OS et version | VRAM, runtime et pilotes | uniquement si support explicite |
| faster-whisper | API Python CTranslate2 | modèles Whisper convertis | CPU INT8 principal | non requis pour le chemin de référence | RAM, modèle, batch et VAD | transcription principale |
| whisper.cpp | CLI et serveur local | modèles ggml/gguf selon version | oui | Vulkan ou ROCm à mesurer | RAM, VRAM et facteur temps réel | référence autonome |
| Piper | CLI, API Python ou serveur web | voix et configuration | oui | non nécessaire | RAM et débit audio | TTS léger |

**Lecture :** « oui » signifie qu’une voie existe dans le tutoriel source, pas qu’elle a été exécutée dans cette fiche. Les profils de mémoire des modèles appartiendront au chapitre 5 du Livre V ; ici, seules les variables à mesurer sont indiquées.

---

<!-- l5:card -->
## MOTEUR-01 — Ollama

| Champ | Référence |
|---|---|
| besoin | servir rapidement un ou plusieurs LLM locaux avec gestion de catalogue et API locale |
| réponse rapide | parcours principal natif Windows, lié à `127.0.0.1:11434`, avec un seul modèle chargé et un contexte initial prudent |
| format et API | catalogue Ollama, Modelfile, API native `/api/*`, sous-ensemble `/v1/*` compatible OpenAI |
| accélération | CPU disponible ; GPU Radeon annoncé mais à vérifier ; `OLLAMA_VULKAN=1` reste un laboratoire séparé |
| mémoire | contexte, cache KV, parallélisme et nombre de modèles simultanés influencent RAM et VRAM |
| sécurité | boucle locale par défaut ; ne pas exposer `0.0.0.0` sans proxy, authentification, TLS et pare-feu |
| alternative | llama.cpp pour contrôler le GGUF, les couches GPU et le benchmark ; LocalAI si une passerelle multi-backends est justifiée |
| provenance | moteur et modèles ont des licences distinctes ; enregistrer version du moteur, source, modèle et licence |
| validation minimale | `[PS] ollama --version`, appel `/api/tags`, chargement d’un modèle, puis `[PS] ollama ps` pendant l’inférence |
| source propriétaire | [architecture recommandée](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#2-architecture-recommandée), [tester les API](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#63-tester-lapi-native), [accélération AMD](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#7-accélération-amd-dans-ollama) |
| lien officiel | [documentation Ollama](https://docs.ollama.com/) |
| preuve | `static-review` datée du `2026-07-18` ; aucune inférence exécutée dans cette fiche |

---

<!-- l5:card -->
## MOTEUR-02 — llama.cpp

| Champ | Référence |
|---|---|
| besoin | exécuter directement un GGUF, comparer CPU et GPU, contrôler l’offload et disposer d’un benchmark séparé |
| réponse rapide | conserver un binaire CPU comme référence ; installer CPU, Vulkan et HIP dans des dossiers distincts avec leur build ou commit |
| format et API | GGUF, CLI, `llama-server` et sous-ensemble compatible OpenAI |
| accélération | CPU obligatoire ; Vulkan pertinent pour AMD Windows ; HIP seulement après qualification explicite |
| mémoire | taille du GGUF, quantification, contexte, cache KV, threads et nombre de couches GPU |
| sécurité | lier le serveur à `127.0.0.1` et traiter tout endpoint compatible comme une API à borner |
| alternative | Ollama pour une expérience gérée ; LocalAI pour une passerelle partagée |
| provenance | code du moteur, build, modèle GGUF et quantification ont des provenances distinctes |
| validation minimale | `[PS] llama-cli.exe --version`, même GGUF en CPU puis Vulkan, sortie brute de `llama-bench`, santé de `llama-server` |
| source propriétaire | [pourquoi llama.cpp est conservé](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#23-pourquoi-llamacpp-est-conservé), [binaires officiels](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#81-binaires-officiels), [benchmark](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#84-benchmark), [serveur local](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#9-serveur-llamacpp) |
| lien officiel | [dépôt llama.cpp](https://github.com/ggml-org/llama.cpp) |
| preuve | `static-review` ; aucun binaire ni modèle exécuté dans cette fiche |

---

<!-- l5:card -->
## MOTEUR-03 — LocalAI

| Champ | Référence |
|---|---|
| besoin | réunir plusieurs familles de modèles ou backends derrière une passerelle et une configuration centralisée |
| réponse rapide | optionnel en Solo ; pertinent en Studio lorsqu’une API commune, plusieurs backends ou une administration partagée réduisent réellement la complexité |
| format et API | API compatibles, configuration YAML, images de conteneur, volumes de modèles et healthcheck |
| accélération | CPU constitue le parcours Docker Desktop Windows ; les images Vulkan visent d’abord un hôte Linux correctement configuré |
| mémoire | workers, modèles chargés, files, volumes et limites de conteneur |
| sécurité | tag ou digest figé, boucle locale, configuration en lecture seule, secrets hors YAML versionné |
| alternative | Ollama pour un poste individuel ; llama.cpp pour un moteur unique et contrôlé |
| provenance | image, version, configuration de modèles et backend doivent être enregistrés séparément |
| validation minimale | `[PS] docker compose config`, état du conteneur, endpoint `/readyz`, puis appel réel du client |
| source propriétaire | [positionnement LocalAI](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#101-positionnement), [parcours Windows sûr](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#102-parcours-windows-sûr), [Vulkan LocalAI](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#103-vulkan-localai) |
| lien officiel | [documentation LocalAI](https://localai.io/) |
| preuve | `static-review` ; aucun conteneur LocalAI exécuté dans cette fiche |

---

<!-- l5:card -->
## MOTEUR-04 — ComfyUI comme moteur de workflow

| Champ | Référence |
|---|---|
| besoin | exécuter des graphes visuels reproductibles et automatisables par API |
| réponse rapide | considérer ComfyUI comme moteur de workflow ; le modèle, les nœuds et le backend d’exécution restent des dépendances distinctes |
| format et API | workflow JSON, prompt API, modèles, VAE, nœuds personnalisés, sorties et manifeste |
| accélération | CPU référence ; DirectML secours ; ZLUDA laboratoire ; ROCm Linux séparé ; portable AMD officiel non retenu pour la RX 6750 XT |
| mémoire | modèles simultanés, résolution, batch, VAE, ControlNet, VRAM réservée et autres applications GPU |
| sécurité | n’installer qu’un nœud qualifié ; enregistrer source, commit, licence, permissions et procédure de retrait |
| alternative | pipeline Python spécialisé ou outil visuel différent, après qualification des formats et licences |
| provenance | tag ou commit ComfyUI, versions Python et bibliothèques, modèles et nœuds enregistrés séparément |
| validation minimale | démarrage CPU, workflow minimal, deux exécutions successives, manifeste complet, puis test du backend candidat |
| source propriétaire | [objet du chapitre ComfyUI](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#1-objet-du-chapitre), [état officiel](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#2-état-officiel-au-18-juillet-2026), [matrice de décision](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#3-matrice-de-décision) |
| lien officiel | [documentation ComfyUI](https://docs.comfy.org/) |
| preuve | ComfyUI `v0.28.0` est la référence documentaire du `2026-07-18` ; aucun workflow exécuté ici |

---

<!-- l5:card -->
## BACKEND-01 — CPU

| Champ | Référence |
|---|---|
| besoin | disposer d’une voie reproductible lorsque l’accélération est absente, instable ou non prise en charge |
| réponse rapide | le CPU est la référence fonctionnelle minimale pour les moteurs LLM, visuels et audio retenus |
| avantages | disponibilité large, diagnostic plus simple, absence de dépendance à un pilote GPU spécifique |
| limites | débit inférieur, latence et consommation RAM parfois élevées, modèles ou résolutions à réduire |
| mémoire | RAM système, threads, contexte, quantification, batch et processus concurrents |
| validation | exécuter le même artefact, le même prompt ou le même fichier avec paramètres enregistrés |
| alternative | backend GPU seulement après preuve de stabilité et gain mesuré |
| source propriétaire | [référence CPU LLM](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#82-vérification-cpu), [CPU audio obligatoire](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#21-le-cpu-reste-la-référence), [ComfyUI manuel CPU](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#3-matrice-de-décision) |
| preuve | principe documentaire ; aucun benchmark CPU produit dans cette fiche |

---

<!-- l5:card -->
## BACKEND-02 — Vulkan

| Champ | Référence |
|---|---|
| besoin | tester une accélération portable sur GPU AMD lorsque le moteur la fournit explicitement |
| réponse rapide | Vulkan est un backend par moteur, pas une garantie globale ; compiler ou télécharger le bon build puis comparer au CPU |
| moteurs concernés | Ollama expérimental, llama.cpp, whisper.cpp et certains pipelines graphiques |
| limites | couverture d’opérateurs, stabilité, pilotes, qualité et mémoire diffèrent selon le moteur |
| mémoire | VRAM, copies entre RAM et VRAM, couches offloadées, contexte ou durée audio |
| validation | même artefact, mêmes paramètres, trois essais, sorties comparées, journaux et retour CPU |
| alternative | CPU ; ROCm/HIP uniquement si la combinaison matérielle et logicielle est explicitement prise en charge |
| source propriétaire | [Vulkan Ollama](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#72-vulkan-expérimental), [llama.cpp Vulkan](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#83-vérification-vulkan), [whisper.cpp](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#10-transcription-avec-whispercpp) |
| preuve | laboratoire à mesurer ; aucune accélération Vulkan revendiquée ici |

---

<!-- l5:card -->
## BACKEND-03 — DirectML

| Champ | Référence |
|---|---|
| besoin | disposer d’un backend Windows accessible via DirectX lorsqu’aucune voie mieux qualifiée n’est disponible |
| réponse rapide | utiliser un environnement séparé et classer DirectML comme secours, non comme référence de performance |
| moteurs concernés | ComfyUI via `torch-directml` et certains outils audio proposant explicitement cette option |
| limites | performances souvent dégradées, maintenance variable, compatibilité d’opérateurs incomplète |
| mémoire | VRAM, copies mémoire, résolution ou durée, latence et stabilité de l’environnement Python |
| validation | démarrage isolé, tâche minimale, comparaison CPU, journaux et retrait sans modifier la référence |
| alternative | CPU stable ; Vulkan ou backend officiel lorsque disponible |
| source propriétaire | [DirectML dans ComfyUI](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#25-directml), [DirectML en secours](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#12-directml-en-secours), [Voicebox CPU et DirectML](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#52-parcours-retenu) |
| preuve | secours documentaire ; aucun environnement DirectML exécuté |

---

<!-- l5:card -->
## BACKEND-04 — ZLUDA

| Champ | Référence |
|---|---|
| besoin | tester une couche communautaire permettant à certaines charges CUDA de fonctionner sur un GPU non-NVIDIA |
| réponse rapide | isoler ZLUDA dans une copie dédiée ; ne jamais contaminer l’environnement CPU stable |
| moteurs concernés | principalement ComfyUI et bibliothèques CUDA compatibles avec la version testée |
| limites | dépendance forte aux versions du pilote, de Python, de PyTorch et des bibliothèques ; support non garanti après mise à jour |
| mémoire | VRAM, bibliothèques chargées, modèle, résolution et libération après tâche |
| validation | GPU détecté, workflow minimal terminé deux fois, mémoire libérée, sortie cohérente, gain face au CPU et rollback immédiat |
| alternative | CPU ; DirectML comme secours ponctuel ; ROCm lorsque officiellement compatible |
| provenance | dépôt et version ZLUDA, DLL, pilote AMD, moteur et workflow doivent être enregistrés ensemble |
| source propriétaire | [positionnement ZLUDA](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#26-zluda), [validation minimale](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#114-validation-minimale), [retour arrière](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#115-retour-arrière) |
| lien officiel | [dépôt ZLUDA](https://github.com/vosen/ZLUDA) |
| preuve | laboratoire communautaire ; aucune exécution ZLUDA revendiquée |

---

<!-- l5:card -->
## BACKEND-05 — ROCm et HIP

| Champ | Référence |
|---|---|
| besoin | utiliser la pile de calcul AMD officiellement prise en charge par un moteur et une combinaison GPU/OS donnée |
| réponse rapide | ne pas déduire la compatibilité d’une autre carte ou de Linux vers Windows ; vérifier la matrice officielle du runtime et du moteur |
| moteurs concernés | builds HIP de llama.cpp, whisper.cpp, PyTorch/ComfyUI et outils audio selon leur documentation |
| limites | support matériel et système étroit, versions couplées, installation et diagnostic plus complexes |
| mémoire | VRAM, runtime, pilotes, bibliothèques et taille de l’artefact |
| validation | support officiel identifié, versions figées, test CPU conservé, tâche minimale puis mesure répétée |
| alternative | Vulkan lorsque le moteur le qualifie ; CPU comme repli universel |
| source propriétaire | [binaires llama.cpp](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#81-binaires-officiels), [matrice ComfyUI](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#3-matrice-de-décision), [whisper.cpp](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#101-positionnement) |
| lien officiel | [documentation ROCm](https://rocm.docs.amd.com/) |
| preuve | support à qualifier par combinaison ; aucun runtime ROCm/HIP exécuté |

---

<!-- l5:card -->
## BACKEND-06 — faster-whisper et CTranslate2

| Champ | Référence |
|---|---|
| besoin | transcrire localement depuis Python avec une voie CPU efficace et intégrable |
| réponse rapide | utiliser `faster-whisper` avec CTranslate2 en CPU INT8 comme parcours principal de transcription |
| format et interface | modèles Whisper convertis, API Python, segments horodatés, VAD et traitement par lots |
| accélération | CPU INT8 retenu ; tout autre device doit être qualifié dans un environnement séparé |
| mémoire | taille du modèle, type de calcul, batch, VAD et durée audio |
| sécurité | fichiers audio et transcriptions peuvent contenir des données personnelles ; définir accès, rétention et suppression |
| alternative | whisper.cpp pour un moteur autonome ; OpenAI Whisper comme témoin de comparaison |
| validation | même audio, langue fixée, timestamps, facteur temps réel, relecture humaine et journal des omissions |
| source propriétaire | [parcours faster-whisper](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#91-parcours-principal), [modèle de départ](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#94-modèle-de-départ), [validation humaine](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#95-validation-humaine) |
| lien officiel | [dépôt faster-whisper](https://github.com/SYSTRAN/faster-whisper) |
| preuve | `static-review` ; aucun audio transcrit |

---

<!-- l5:card -->
## BACKEND-07 — whisper.cpp

| Champ | Référence |
|---|---|
| besoin | disposer d’un moteur de transcription C/C++ autonome, quantifiable et utilisable en CLI ou serveur |
| réponse rapide | conserver le CPU comme référence et tester Vulkan avec le même modèle, le même audio et les mêmes options |
| format et interface | modèles Whisper convertis, CLI, sorties texte ou SRT, VAD et serveur local |
| accélération | CPU, Vulkan ou ROCm selon build ; la RX 6750 XT rend Vulkan intéressant mais non garanti |
| mémoire | modèle, quantification, threads, VAD, durée audio et backend |
| sécurité | ne pas publier le serveur sans authentification et politique de données ; conserver les entrées originales |
| alternative | faster-whisper pour l’intégration Python ; OpenAI Whisper pour une comparaison de référence |
| validation | facteur temps réel, qualité relue, mêmes paramètres CPU/Vulkan, journaux et retour CPU |
| source propriétaire | [positionnement whisper.cpp](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#101-positionnement), [référence CPU](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#102-référence-cpu), [benchmark CPU contre Vulkan](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#104-benchmark-cpu-contre-vulkan) |
| lien officiel | [dépôt whisper.cpp](https://github.com/ggml-org/whisper.cpp) |
| preuve | `static-review` ; aucun binaire ni fichier audio exécuté |

---

<!-- l5:card -->
## BACKEND-08 — Piper

| Champ | Référence |
|---|---|
| besoin | synthétiser rapidement des voix utilitaires sur CPU, dans un pipeline local ou embarquable |
| réponse rapide | utiliser le paquet et le dépôt actuels, puis traiter chaque voix comme un artefact avec sa propre licence |
| format et interface | CLI, API Python, serveur web, modèle de voix et configuration phonétique |
| accélération | CPU suffit au parcours principal |
| mémoire | modèle de voix, nombre de requêtes, longueur du texte et files de synthèse |
| sécurité et droits | une voix n’est pas libre parce que le moteur l’est ; enregistrer origine, licence, langue et restrictions |
| alternative | Kokoro pour des prototypes rapides ; moteur expressif séparé avec consentement documenté |
| validation | phrase courte, nombres, noms propres, durée, absence de coupure et vérification humaine |
| source propriétaire | [dépôt actuel de Piper](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#71-dépôt-actuel), [usage recommandé](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#74-usage-recommandé), [règles de consentement](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#23-aucun-clonage-sans-consentement-explicite) |
| lien officiel | [dépôt Piper actuel](https://github.com/OHF-Voice/piper1-gpl) |
| preuve | code actuel indiqué GPL-3.0 dans la source propriétaire ; aucune voix générée |

---

<!-- l5:matrix -->
## Matrice C — Diagnostic par couches

| Symptôme | Première vérification | Cause possible | Source |
|---|---|---|---|
| l’interface ne voit aucun modèle | tester l’API du moteur hors interface | mauvais endpoint, moteur arrêté ou `localhost` utilisé depuis un conteneur | [connexions entre composants](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#12-connexions-entre-composants) |
| le modèle répond mais le GPU reste inactif | journal du moteur et indicateur CPU/GPU | backend non chargé, carte non prise en charge ou retour CPU | [diagnostic par couches](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#19-diagnostic-par-couches) |
| erreur après mise à jour | comparer moteur, modèle, backend et paramètres | versions couplées, template ou bibliothèque modifiée | [mises à jour](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#18-mises-à-jour) |
| API « compatible OpenAI » incomplète | appeler l’endpoint réellement consommé | sous-ensemble différent ou champ non pris en charge | [tester l’API compatible](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#64-tester-lapi-compatible-openai) |
| mémoire croissante | relever contexte, modèles chargés, files et batch | cache KV, modèles simultanés, fuite ou file non bornée | [mesures obligatoires](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#16-mesures-obligatoires) |
| ComfyUI termine en CPU | vérifier environnement et journal de démarrage | backend absent, dépendance incompatible ou repli silencieux | [matrice ComfyUI](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#3-matrice-de-décision) |
| ZLUDA casse après mise à jour | redémarrer l’installation CPU inchangée | couplage pilote, PyTorch, bibliothèques ou DLL | [retour arrière ZLUDA](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#115-retour-arrière) |
| transcription invente ou omet | réécouter l’audio et comparer les segments | silence, bruit, langue ou modèle inadapté | [validation humaine](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#95-validation-humaine) |
| le service répond mais la capacité manque | lire l’état et la liste de capacités | service dégradé ou opération non autorisée | [états du service](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md#8-états-du-service) |
| une tâche longue sature le jeu | contrôler file, limites et backpressure | travail traité comme requête instantanée | [choisir le transport](../Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md#5-choisir-le-transport) |
| un moteur est joignable depuis le réseau | vérifier adresse d’écoute et pare-feu | liaison à `0.0.0.0` ou publication de port | [sécurité des API locales](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#13-sécurité-des-api-locales) |
| le runtime reçoit trop de privilèges | comparer profils production et développement | outil de production embarqué par erreur | [séparation production/runtime](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md#7-séparation-productionruntime) |

## Frontières avec les fiches voisines

- La [fiche 03](CHAPITRE-03-Fiches-des-logiciels-et-outils.md) reste propriétaire des applications, installations minimales et outils d’environnement.
- La présente fiche possède les moteurs, backends, API d’inférence, accélérations et diagnostics de couche.
- La fiche 05 possédera les familles de modèles de langage, tailles, quantifications, contextes et licences.
- Les fiches 06 et 07 posséderont respectivement les modèles visuels et audio.
- Le chapitre 21 possédera les protocoles et résultats de benchmarks datés.
- Le chapitre 22 possédera les matrices historiques de compatibilité par version.
- Les déploiements complets restent dans les [LLM locaux du Livre I](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md) et l’[audio local](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md).
- L’intégration applicative reste dans les chapitres [11](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md), [12](../Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md) et [13](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md) du Livre II.

## Réserves

- Aucun moteur, modèle, workflow, conteneur, serveur ou fichier audio n’a été exécuté.
- Aucun débit, temps de chargement, facteur temps réel, consommation RAM ou VRAM n’est revendiqué.
- Aucun support AMD n’est extrapolé d’un autre GPU, système ou moteur.
- Aucun lien officiel n’a été ouvert depuis un navigateur dans ce lot.
- Les compatibilités, licences et versions doivent être revérifiées avant installation ou publication.
- Aucun artefact du Companion Pack ni PDF n’a été produit.
