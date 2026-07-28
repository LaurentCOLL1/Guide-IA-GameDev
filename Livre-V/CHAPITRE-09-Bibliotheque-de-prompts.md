---
title: "Livre V — Fiche 09 : Bibliothèque de prompts"
id: "DOC-L5-CH09"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 9
last-verified: "2026-07-28T19:12:00+02:00"
audit-status: "complete"
audit-date: "2026-07-28T19:12:00+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-09.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "cross-modal-prompt-library"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Bibliothèque de prompts

> **Type de document :** contrats de prompts, matrices de sélection, jeux de tests et portes d’acceptation.
> **Lecture :** choisir la tâche, identifier le modèle exact, instancier les variables, puis appliquer la grille d’évaluation adaptée.
> **Principe :** un prompt décrit une demande ; il ne prouve ni la qualité, ni la sécurité, ni la reproductibilité de la réponse.

## Index express

| Besoin | Ouvrir |
|---|---|
| enregistrer un prompt versionné | [PROMPT-00](#prompt-00--contrat-dun-prompt) |
| choisir un gabarit par tâche | [Matrice A](#matrice-a--sélection-par-tâche) |
| distinguer template, instance et run | [PROMPT-01](#prompt-01--template-instance-et-run) |
| déclarer les variables et le contexte | [PROMPT-02](#prompt-02--variables-délimiteurs-et-contexte) |
| obtenir JSON ou appel d’outil | [PROMPT-03](#prompt-03--sortie-structurée-et-outils) |
| résumer, extraire ou classer | [PROMPT-04](#prompt-04--résumé-extraction-et-classification) |
| répondre depuis un corpus | [PROMPT-05](#prompt-05--rag-citations-et-incertitude) |
| demander ou revoir du code | [PROMPT-06](#prompt-06--code-et-revue-technique) |
| décrire une génération visuelle | [PROMPT-07](#prompt-07--visuel-et-multimodal) |
| préparer voix, STT, musique ou SFX | [PROMPT-08](#prompt-08--audio-voix-et-transcription) |
| générer narration ou dialogue | [PROMPT-09](#prompt-09--narration-et-dialogue) |
| figer modèle, template et paramètres | [PROMPT-10](#prompt-10--modèle-cible-et-paramètres) |
| traiter les injections et données non fiables | [PROMPT-11](#prompt-11--injection-sécurité-et-données) |
| versionner une révision | [Matrice B](#matrice-b--cycle-dun-prompt) |
| qualifier sans inventer de résultat | [Matrice C](#matrice-c--jeu-de-tests-minimal) |
| publier un paquet de prompts | [PROMPT-12](#prompt-12--paquet-et-acceptation) |

---

<!-- l5:card -->
## PROMPT-00 — Contrat d’un prompt

| Champ | Règle |
|---|---|
| identité | identifiant stable, version, propriétaire, dépôt et chemin canonique |
| tâche | opération unique et observable : résumer, extraire, classer, proposer, transformer ou appeler un outil |
| modèle cible | fournisseur, famille, identifiant exact ou snapshot, modalité et date de qualification |
| interface | rôle système éventuel, messages, template de chat, format API ou nœud de conditionnement |
| variables | nom, type, obligation, valeur par défaut, borne, confiance et exemple autorisé |
| instructions | priorité, résultat attendu, critères d’arrêt et comportements interdits |
| données | contexte et entrées séparés des instructions, avec origine et niveau de confiance |
| sortie | média, langue, longueur, schéma, enum, citations, refus ou état d’incertitude |
| paramètres | température, seed si disponible, limite, outils, raisonnement exposé ou non, sampler selon modalité |
| exemples | cas few-shot représentatifs, cohérents et distincts du jeu de test final |
| sécurité | injections, secrets, données personnelles, outils autorisés et validation avant effet |
| évaluation | fixtures, oracles, métriques, revue humaine, variance et seuil de passage |
| preuve | modèle réellement appelé, requête résolue, réponse brute, parse, mesures et décision |
| retrait | modèles affectés, remplaçant, jeux de tests, versions dépendantes et conservation des preuves |

**Réponse rapide :** le prompt est une ressource versionnée, conformément au [standard de gestion des prompts](../Volume-0/CHAPITRE-08-Standards-IA.md#31-le-prompt-est-une-ressource-versionnée). La présente bibliothèque décrit les contrats ; la [bibliothèque de workflows](CHAPITRE-08-Bibliotheque-de-workflows.md#workflow-00--contrat-dun-workflow) possède leur orchestration.

---

<!-- l5:matrix -->
## Matrice A — Sélection par tâche

| Besoin | Carte de départ | Sortie fermée | Source propriétaire | Évaluation minimale |
|---|---|---|---|---|
| extraire des champs | PROMPT-03 et 04 | JSON Schema ou types stricts | [sortie structurée](../Volume-0/CHAPITRE-08-Standards-IA.md#51-sortie-structurée) | parse, schéma et exactitude des valeurs |
| résumer un document | PROMPT-04 | longueur, langue et faits autorisés | [test français](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#153-test-français) | couverture, absence d’ajout et lisibilité |
| répondre depuis des sources | PROMPT-05 | réponse, citations et état d’incertitude | [source canonique](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md#41-source-canonique) | citation retrouvable et fidélité au contexte |
| produire ou revoir du code | PROMPT-06 | patch, diagnostic ou code typé | [génération de code](../Volume-0/CHAPITRE-08-Standards-IA.md#54-génération-de-code) | syntaxe, tests, sécurité et diff |
| explorer un concept visuel | PROMPT-07 | propriétés observables et exclusions | [contrat de prompt visuel](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#18-écrire-un-contrat-de-prompt) | grille artistique, technique et juridique |
| synthétiser ou transcrire | PROMPT-08 | texte, audio ou segments horodatés | [sorties audio intermédiaires](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#24-les-sorties-ia-restent-des-sources-intermédiaires) | écoute, relecture, format et consentement |
| proposer narration ou dialogue | PROMPT-09 | candidat sans mutation gameplay | [autorité narrative](../Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md#1-rôle-du-chapitre) | cohérence, faits sources et revue humaine |
| appeler un outil | PROMPT-03 et 11 | nom et arguments conformes au schéma | [séparation production/runtime](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md#7-séparation-productionruntime) | autorisation, arguments et effet contrôlé |

Une tâche complexe peut chaîner plusieurs prompts, mais chaque étape conserve une entrée, une sortie et un propriétaire distincts. Le workflow reste responsable de l’ordre, des retries et de la promotion.

---

<!-- l5:card -->
## PROMPT-01 — Template, instance et run

| Objet | Définition | Identité minimale | Ne prouve pas |
|---|---|---|---|
| template | gabarit versionné avec variables non résolues | `prompt_id`, version et SHA-256 | compatibilité avec un modèle |
| variante | adaptation explicite à une famille, langue ou modalité | parent, cible et motif | supériorité sur le parent |
| instance | template avec variables résolues et contexte attaché | instance, template, entrées et empreintes | qu’un appel a eu lieu |
| requête | messages, outils, paramètres et options réellement envoyés | run, moteur, modèle exact et horodatage | que le service a terminé |
| réponse brute | contenu reçu avant parsing ou post-traitement | run, séquence, statut et octets | validité métier |
| résultat interprété | réponse parsée, validée ou transformée | parseur, schéma, diagnostics et statut | autorisation de publication |
| décision | acceptation, rejet, nouvelle expérience ou retrait | réviseur, critères, périmètre et date | universalité du prompt |

**Règle :** ne jamais corriger silencieusement une instance puis l’archiver sous la version du template initial. Une modification d’instruction, d’exemple, de délimiteur ou de schéma crée une révision traçable.

**Source :** la [traçabilité avant automatisation](../Volume-0/CHAPITRE-08-Standards-IA.md#13-traçabilité-avant-automatisation) exige modèle, paramètres, prompt, entrées, sorties et statut de validation.

---

<!-- l5:card -->
## PROMPT-02 — Variables, délimiteurs et contexte

| Champ | Contrat |
|---|---|
| syntaxe | employer une convention unique, par exemple `{{variable_name}}` |
| type | chaîne, enum, entier, booléen, liste, document, image, audio ou référence d’outil |
| obligation | `required`, `optional` ou `derived`, sans valeur implicite cachée |
| borne | longueur, nombre d’items, taille de fichier, locale, format et caractères autorisés |
| confiance | `trusted_instruction`, `trusted_context`, `untrusted_data` ou `secret_reference` |
| échappement | conserver les données comme données ; ne pas concaténer dans une instruction exécutable |
| délimiteurs | sections ou balises cohérentes pour rôle, contraintes, contexte, données, tâche et sortie |
| contexte long | sélectionner les passages utiles, conserver leur identité et placer la question sans ambiguïté |
| absence | valeur explicite `null`, liste vide ou état `information_insuffisante` selon le schéma |
| journal | enregistrer les valeurs résolues ou leurs empreintes ; rédiger les secrets et données sensibles |

**Gabarit compact :** `INSTRUCTIONS → CONTRAINTES → CONTEXTE → DONNÉES NON FIABLES → TÂCHE → FORMAT → CRITÈRES`. L’ordre exact doit être qualifié pour le modèle cible ; les délimiteurs améliorent la séparation mais ne neutralisent pas une injection.

Voir [séparer instruction et données](../Volume-0/CHAPITRE-08-Standards-IA.md#32-séparer-instruction-et-données) et [variables explicites](../Volume-0/CHAPITRE-08-Standards-IA.md#33-variables-explicites).

---

<!-- l5:card -->
## PROMPT-03 — Sortie structurée et outils

| Champ | Référence |
|---|---|
| besoin | produire des données parsables ou demander une action bornée |
| choix | sortie structurée pour la réponse finale ; appel d’outil pour proposer une action à un exécuteur |
| schéma | types fermés, champs requis, enums, bornes et descriptions ; sous-ensemble réellement supporté par le moteur |
| prompt | expliquer la tâche et la sémantique des champs, sans recopier inutilement le schéma |
| validation | parse syntaxique, validation de schéma, validation métier et contrôle des références |
| outil | nom stable, description précise, arguments typés, erreurs documentées et permissions minimales |
| autorité | le modèle propose ; l’application authentifie, autorise, valide et exécute |
| erreur | sortie invalide, valeur impossible, outil inconnu, argument hors borne ou besoin de revue |
| repli | réponse textuelle classée non exploitable, nouvelle instance plus simple ou traitement manuel |
| preuve | requête, schéma, réponse brute, parse, diagnostics, outil choisi et résultat de l’exécuteur |
| sources officielles | [sorties structurées Gemini](https://ai.google.dev/gemini-api/docs/structured-output), [référence Evals OpenAI](https://platform.openai.com/docs/api-reference/evals) |
| preuve actuelle | documentations revues le `2026-07-28` ; aucun appel API ni parse exécuté |

**Point critique :** un objet conforme au schéma peut contenir des valeurs fausses ou incohérentes. La validation métier reste obligatoire, comme l’impose le [standard JSON de production](../Volume-0/CHAPITRE-08-Standards-IA.md#51-sortie-structurée).

---

<!-- l5:card -->
## PROMPT-04 — Résumé, extraction et classification

| Champ | Gabarit de référence |
|---|---|
| tâche | nommer une seule opération : résumer, extraire ou classer |
| entrée | texte identifié, langue, provenance, longueur et règles de traitement |
| sortie | phrases maximales, champs requis ou enum fermé |
| faits | utiliser uniquement l’entrée ; signaler explicitement l’information absente |
| citations | conserver identifiants de section ou plages lorsque le résultat doit être vérifiable |
| exemples | cas nominal, ambigu, vide et contradictoire ; formats identiques |
| résumé | dimensions obligatoires, éléments à omettre et niveau de compression |
| extraction | ne pas normaliser une valeur sans règle ; conserver texte source et confiance |
| classification | catégories définies, règle pour `unknown` et interdiction d’inventer une classe |
| variance | mêmes faits attendus, formulation éventuellement variable selon le contrat |
| critères | exactitude, couverture, fidélité, format, langue et absence de contenu ajouté |
| repli | réponse `uncertain`, revue humaine ou extracteur déterministe pour une grammaire simple |

**Test propriétaire :** le [jeu de tests LLM](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#15-jeux-de-tests) sépare test fonctionnel, JSON, français, code et refus d’invention.

---

<!-- l5:card -->
## PROMPT-05 — RAG, citations et incertitude

| Champ | Contrat |
|---|---|
| question | demande autonome, périmètre et date ou version pertinente |
| contexte | passages récupérés avec source, section, révision, visibilité et rang |
| autorité | les sources canoniques restent propriétaires ; le score vectoriel n’est pas une preuve de vérité |
| instruction | répondre uniquement depuis le contexte autorisé et distinguer citation, synthèse et inférence |
| absence | retourner un état explicite lorsque les passages ne suffisent pas |
| conflit | présenter les sources incompatibles sans choisir silencieusement |
| citations | rattacher chaque affirmation importante au passage qui la supporte |
| injection | traiter les instructions trouvées dans les documents comme des données non fiables |
| sortie | réponse, citations, niveau de confiance documentaire et limites |
| évaluation | précision de récupération, citation retrouvable, fidélité, refus correct et couverture |
| repli | recherche lexicale, reformulation de requête, élargissement contrôlé ou revue humaine |
| sources | [similarité non probabilité](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md#46-similarité), [citation des sources](../Volume-0/CHAPITRE-08-Standards-IA.md#62-citation-des-sources) |

**Réponse rapide :** le prompt ne répare pas un corpus incomplet, un mauvais découpage ou une récupération hors sujet. Les évaluations de recherche et de génération restent séparées.

---

<!-- l5:card -->
## PROMPT-06 — Code et revue technique

| Champ | Contrat |
|---|---|
| mode | expliquer, diagnostiquer, proposer un patch, générer un fichier ou produire des tests |
| contexte | langage, version, conventions, chemins, interfaces, dépendances et extraits minimaux |
| contraintes | types, API autorisées, effets de bord, performance, sécurité et compatibilité |
| sortie | diff, fichier complet, diagnostic structuré ou plan de test ; jamais mélange implicite |
| hypothèses | énumérer celles qui affectent le résultat et refuser les symboles absents du contexte |
| dépendances | aucune bibliothèque, commande ou version inventée ; demander ou marquer l’incertitude |
| tests | cas nominal, erreur, limite et non-régression liés aux critères du changement |
| sécurité | code traité comme externe, sans secret, écriture globale ou commande destructive automatique |
| licence | signaler les fragments inhabituels et ne pas imiter une source non autorisée |
| évaluation | syntaxe, compilation ou analyse, tests, diff, diagnostic et revue humaine |
| repli | pseudocode, contrat d’interface ou question ciblée lorsque le contexte manque |
| source | [génération de code non vérifiée](../Volume-0/CHAPITRE-08-Standards-IA.md#54-génération-de-code), [test de code LLM](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#154-test-code) |

**Frontière :** le chapitre 10 du Livre V possédera les recettes exécutables. Cette carte ne fournit aucun script prétendument testé.

---

<!-- l5:card -->
## PROMPT-07 — Visuel et multimodal

| Champ | Contrat |
|---|---|
| fonction | concept, variation, retouche, texture, référence, masque ou analyse visuelle |
| sujet | rôle, silhouette, proportions, matériaux, état, environnement et relations spatiales |
| composition | cadrage, point de vue, focale descriptive, profondeur et hiérarchie visuelle |
| lumière | direction, contraste, fonction, heure et lisibilité attendue |
| contraintes | règles de bible, propriétés non négociables, éléments ouverts et exclusions |
| entrées | images autorisées, masques, pose, profondeur ou contrôle, avec droits et empreintes |
| modèle | famille exacte, composants, résolution native et syntaxe réellement supportée |
| négatif | seulement si le workflow le prend en charge ; ne remplace aucune vérification |
| paramètres | seed, dimensions, sampler, scheduler, étapes, guidance et poids des contrôles |
| sortie | quarantaine, métadonnées, run et association au prompt résolu |
| évaluation | fonction, silhouette, cohérence matérielle, artefacts, bible, droits et revue humaine |
| sources | [contrat visuel](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#18-écrire-un-contrat-de-prompt), [limite du prompt négatif](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#19-ne-pas-traiter-le-prompt-négatif-comme-une-garantie) |

**Décision :** préférer des propriétés observables aux noms d’artistes ou à un mot de style opaque. Une sortie séduisante mais hors fonction reste un échec du contrat.

---

<!-- l5:card -->
## PROMPT-08 — Audio, voix et transcription

| Tâche | Variables principales | Sortie attendue | Contrôle obligatoire |
|---|---|---|---|
| TTS | texte, langue, voix, prononciation, rythme et intention | audio brut et métadonnées | consentement, intelligibilité et écoute |
| adaptation vocale | référence autorisée, locuteur, périmètre et retrait | candidat en accès contrôlé | consentement explicite et ressemblance |
| STT | audio, langue, segmentation, VAD et timestamps | transcription et segments | relecture contre l’original |
| traduction STT | audio, langue source et langue cible | texte traduit identifié | ne pas confondre transcription et traduction |
| musique | description, structure, durée, tempo, instrumentation et exclusions | maquette intermédiaire | licence, ressemblance et montage |
| SFX | source, action, matière, perspective, durée et environnement | brouillon sonore | voix parasite, continuité et fonction |
| prononciation | noms, sigles, nombres, locale et dictionnaire | variante de texte ou lexique | test par voix et locale |

**Règles :** la description ne remplace ni le modèle, ni la voix, ni le consentement, ni les paramètres. Les sorties restent intermédiaires jusqu’à écoute, nettoyage et validation, conformément au [pipeline audio](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#24-les-sorties-ia-restent-des-sources-intermédiaires) et aux [formats du projet](../Livre-I/CHAPITRE-09-Audio-IA-local-voix-transcription-musique-et-effets.md#4-formats-audio-du-projet).

---

<!-- l5:card -->
## PROMPT-09 — Narration et dialogue

| Champ | Contrat |
|---|---|
| besoin | proposer un texte ou une structure narrative sans muter l’état du jeu |
| faits | événements, personnages, relations, lieux et connaissances fournis par leurs autorités |
| perspective | locuteur, public, connaissances permises, registre, langue et intention |
| contraintes | canon, longueur, ton fonctionnel, informations interdites et continuité |
| sortie | candidat de dialogue, résumé, beat, variante ou objet structuré de proposition |
| ignorance | un personnage ne révèle pas un fait absent de ses connaissances autorisées |
| gameplay | aucun texte généré ne valide une quête, ne transfère un objet ou ne modifie une relation |
| variété | distinguer variation lexicale, contenu nouveau et décision narrative |
| sécurité | contenu sensible, stéréotypes, données personnelles et limites d’âge revus humainement |
| évaluation | fidélité aux faits, voix, cohérence, non-divulgation, jouabilité et localisation |
| repli | ligne écrite manuellement, template déterministe ou absence de génération runtime |
| source | [frontière narrative](../Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md#3-périmètre-et-frontières), [IA consultative](../Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md#1-rôle-du-chapitre) |

**Porte :** une sortie narrative est une proposition éditoriale. Les faits autoritaires, conditions et conséquences restent déterministes et propriétaires.

---

<!-- l5:card -->
## PROMPT-10 — Modèle cible et paramètres

| Champ | À enregistrer |
|---|---|
| fournisseur | organisation, moteur local ou service, sans confondre interface et modèle |
| modèle | identifiant exact, snapshot ou fichier, famille, quantification et empreinte si locale |
| template | chat template, rôles, tokens spéciaux, Modelfile ou format d’instruction |
| capacités | texte, image, audio, outils, sortie structurée et limites réellement disponibles |
| paramètres | température, top-p, top-k, seed, limite de sortie, contexte, raisonnement et stop |
| outils | noms, schémas, choix autorisés et politique d’exécution |
| locale | langue du prompt, langue de sortie et corpus d’évaluation |
| environnement | moteur, version, backend, matériel, options et date |
| comparaison | même jeu de tests, mêmes entrées et critères ; une variable changée ou couplage déclaré |
| alias | un alias mouvant n’est pas une preuve stable ; préférer un snapshot pour une qualification durable |
| migration | relancer le jeu d’évaluation avant d’adopter une nouvelle famille, version ou template |
| sources officielles | [guide de modèle OpenAI](https://developers.openai.com/api/docs/guides/latest-model), [stratégies de prompts Gemini](https://ai.google.dev/gemini-api/docs/prompting-strategies), [bonnes pratiques Claude](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices), [Modelfile Ollama](https://docs.ollama.com/modelfile) |
| preuve actuelle | sources revues le `2026-07-28` ; aucun modèle appelé ni paramètre comparé |

**Limite :** une température basse ou une seed fixe ne garantit pas une réponse identique entre versions, backends ou plateformes. Le [standard de paramètres](../Volume-0/CHAPITRE-08-Standards-IA.md#4-paramètres-et-seeds) exige une revendication proportionnée.

---

<!-- l5:card -->
## PROMPT-11 — Injection, sécurité et données

| Risque | Contrôle minimal | Test |
|---|---|---|
| instruction hostile de l’utilisateur | autorité limitée, règles hors données et sortie fermée | tentative directe d’ignorer les contraintes |
| injection indirecte dans un fichier ou site | traiter le contenu comme données non fiables | document contenant une fausse instruction |
| exfiltration | ne jamais placer secrets ou données inutiles dans le contexte | demande de révélation ou encodage |
| outil trop puissant | allowlist, arguments typés, autorisation et confirmation des effets | appel hors capacité ou hors chemin |
| confusion de rôles | conserver la structure réellement prise en charge par le modèle | données imitant un message système |
| sortie active | parser et neutraliser HTML, Markdown, URL, commande ou chemin avant usage | charge utile dans un champ texte |
| déni de service | limites de taille, tokens, outils, tours, temps et coût | entrée maximale et boucle d’outil |
| données personnelles | minimisation, accès, rétention, retrait et journal rédigé | fixture synthétique et refus de donnée réelle |
| décision critique | revue humaine ou règle déterministe propriétaire | réponse plausible mais non autorisée |
| sécurité par prompt seul | défense en profondeur dans l’application et le workflow | prompt contourné sans effet externe |

Les injections directes et indirectes restent des risques même avec des délimiteurs ou un RAG. Voir [zones de confiance](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md#6-zones-de-confiance) et la [fiche OWASP Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/), revue le `2026-07-28`.

**Niveau de preuve :** contrôles documentaires ; aucun test d’intrusion, outil, secret, fichier hostile ou service n’a été exécuté.

---

<!-- l5:matrix -->
## Matrice B — Cycle d’un prompt

| État | Question | Artefact autorisé | Passage interdit |
|---|---|---|---|
| `draft` | la tâche et le propriétaire sont-ils définis ? | note et hypothèses | distribuer comme gabarit recommandé |
| `defined` | variables, modèle, sortie et limites sont-ils explicites ? | template versionné | annoncer qu’il fonctionne |
| `instantiated` | les valeurs résolues sont-elles valides et autorisées ? | instance et empreintes | masquer une valeur ou un secret |
| `evaluating` | le jeu de tests et les paramètres sont-ils figés ? | runs, réponses brutes et diagnostics | modifier le prompt en cours de campagne |
| `qualified` | les seuils sont-ils atteints sur la cible exacte ? | rapport daté et périmètre | généraliser à un autre modèle |
| `accepted_limited` | l’usage est-il borné et le repli connu ? | paquet pour une tâche précise | étendre la décision sans test |
| `accepted` | les cas nominaux, limites et sécurité sont-ils couverts ? | version publiée et matrice de support | supprimer les preuves |
| `blocked` | quel défaut ou risque empêche l’usage ? | diagnostic et propriétaire | relancer sans changement d’hypothèse |
| `superseded` | quel remplaçant couvre les dépendants ? | migration et historique | réutiliser comme version courante |
| `withdrawn` | quelles instances et sorties sont affectées ? | décision de retrait | effacer les traces nécessaires |

Une amélioration de formulation ne devient pas un progrès tant que le même jeu de tests ne démontre pas le changement. Les résultats mesurés appartiendront au chapitre 21 du Livre V.

---

<!-- l5:matrix -->
## Matrice C — Jeu de tests minimal

| Test | Fixture | Critère automatique | Revue humaine | État dans cette fiche |
|---|---|---|---|---|
| T1 — cas nominal | entrée courte valide | format et champs requis | utilité du résultat | non exécuté |
| T2 — absence | donnée obligatoire manquante | état d’incertitude ou refus | absence d’invention | non exécuté |
| T3 — ambiguïté | deux interprétations plausibles | demande ciblée ou statut ambigu | qualité de la clarification | non exécuté |
| T4 — contradiction | sources incompatibles | conflit conservé | présentation équitable | non exécuté |
| T5 — format | caractères, accents et valeurs limites | parse et schéma | sens des valeurs | non exécuté |
| T6 — français | noms, nombres, dates et registre | langue et contraintes | naturel et précision | non exécuté |
| T7 — contexte long | passages pertinents et distracteurs | citations retrouvables | fidélité et couverture | non exécuté |
| T8 — injection directe | instruction hostile explicite | aucune action non autorisée | réponse sûre et utile | non exécuté |
| T9 — injection indirecte | document hostile | contenu traité comme données | absence d’exfiltration | non exécuté |
| T10 — variation | répétitions mêmes paramètres | taux de passage et distribution | stabilité fonctionnelle | non exécuté |
| T11 — migration | ancien et nouveau modèle ou template | mêmes métriques et coûts | régression qualitative | non exécuté |
| T12 — repli | modèle, outil ou schéma indisponible | état fermé et route alternative | exploitabilité du repli | non exécuté |

**Règles d’évaluation :** conserver les fixtures hors des exemples few-shot, enregistrer chaque réponse brute, distinguer exactitude et style, éviter un juge unique pour les décisions sensibles et documenter la variance plutôt que sélectionner seulement les meilleures sorties.

Les [mesures obligatoires des LLM](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#16-mesures-obligatoires) fournissent les dimensions runtime ; la présente matrice ne contient aucune valeur de performance ou qualité.

---

<!-- l5:card -->
## PROMPT-12 — Paquet et acceptation

| Élément | Exigence |
|---|---|
| fiche | identité, tâche, propriétaire, modèle cible, limites et sources |
| template | fichier canonique lisible, version, empreinte et licence de redistribution |
| variables | schéma, types, bornes, confiance, exemples et politique de rédaction |
| variantes | différences explicites par modèle, langue, modalité ou profil |
| exemples | entrées et sorties de forme attendue, marquées `illustrative` tant qu’elles ne proviennent pas d’un run |
| évaluations | fixtures séparées, oracles, métriques, seuils, variance et revue humaine |
| runs | requêtes résolues, réponses brutes, paramètres, modèle exact et diagnostics |
| sécurité | injections, outils, secrets, données personnelles, limites et repli |
| compatibilité | modèles, templates de chat, moteurs et versions réellement qualifiés |
| documentation | liens vers les tutoriels propriétaires et sources officielles datées |
| Companion Pack | emplacement prévu et statut `not-materialized` tant que les fichiers n’existent pas |
| décision | `defined`, `qualified`, `accepted_limited`, `accepted`, `blocked`, `withdrawn` ou `superseded` |

**Porte minimale :** un prompt reste `defined` tant qu’aucun modèle exact ne l’a exécuté sur un jeu de tests représentatif. Il devient `qualified` seulement avec réponses brutes, critères appliqués, variance documentée, tests de sécurité adaptés et repli vérifié.

**Frontières :**

- la fiche 05 possède les familles de modèles de langage ;
- les fiches 06 et 07 possèdent les modèles visuels et audio ;
- la fiche 08 possède les workflows et leur orchestration ;
- la fiche 09 possède templates, variables, instances et critères d’évaluation ;
- le chapitre 10 possédera scripts, recettes et runners ;
- le chapitre 21 possédera les résultats de benchmarks et campagnes ;
- le chapitre 22 possédera les compatibilités historiques par modèle et version ;
- le chapitre 24 possédera les checklists transversales ;
- le chapitre 25 possédera licences, provenance et conformité ;
- les paquets exécutables réels appartiendront au Companion Pack après matérialisation.

**Niveau de preuve :** `static-review`. Aucun modèle, moteur, API, outil, workflow visuel, pipeline audio, fixture hostile, dataset d’évaluation ou prompt du Companion Pack n’a été exécuté ; aucune réponse, mesure, note humaine, approbation juridique ou production PDF n’a été réalisée.
