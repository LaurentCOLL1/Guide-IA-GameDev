---
title: "Livre V — Fiche 05 : Fiches des modèles de langage"
id: "DOC-L5-CH05"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 5
last-verified: "2026-07-28T15:09:18+02:00"
audit-status: "complete"
audit-date: "2026-07-28T15:09:18+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-05.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "language-model-families"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Fiches des modèles de langage

> **Type de document :** cartes de familles, matrices de sélection, estimation mémoire et protocole de test reproductible.
> **Lecture :** choisir d’abord une tâche et une enveloppe de ressources, puis vérifier le modèle exact, sa licence, son format et son runtime.
> **Principe :** une famille n’est pas un fichier, un nombre de paramètres n’est pas une mesure de qualité, et une fenêtre de contexte annoncée n’est pas une capacité pratique garantie.

## Index express

| Besoin | Ouvrir |
|---|---|
| enregistrer un modèle exact | [MODÈLE-00](#modèle-00--contrat-dune-fiche) |
| partir de l’usage et des ressources | [Matrice A](#matrice-a--sélection-par-usage-et-enveloppe) |
| famille multilingue dense ou MoE | [MODÈLE-01 — Qwen3](#modèle-01--qwen3) |
| famille légère et multimodale Google | [MODÈLE-02 — Gemma 4](#modèle-02--gemma-4) |
| petit modèle Microsoft | [MODÈLE-03 — Phi-4](#modèle-03--phi-4) |
| famille IBM orientée efficacité et gouvernance | [MODÈLE-04 — Granite 4](#modèle-04--granite-4) |
| modèle hybride multimodal et raisonnement | [MODÈLE-05 — Mistral Small 4](#modèle-05--mistral-small-4) |
| famille Meta, du mobile au MoE serveur | [MODÈLE-06 — Llama](#modèle-06--llama) |
| raisonnement et distillations | [MODÈLE-07 — DeepSeek-R1](#modèle-07--deepseek-r1) |
| estimer les poids avant téléchargement | [Matrice B](#matrice-b--poids-théoriques-et-quantification) |
| comprendre Q4, Q5, Q8 et FP16 | [MODÈLE-08 — Quantification](#modèle-08--quantification) |
| borner le contexte et le cache KV | [MODÈLE-09 — Contexte](#modèle-09--contexte-et-cache-kv) |
| qualifier licence et provenance | [MODÈLE-10 — Licence](#modèle-10--licence-provenance-et-dérivés) |
| valider le français et les langues utiles | [MODÈLE-11 — Langues](#modèle-11--français-et-multilingue) |
| comparer sans inventer de benchmark | [Matrice C](#matrice-c--tests-reproductibles-sans-résultat-inventé) |
| conserver le manifeste de décision | [MODÈLE-12 — Manifeste](#modèle-12--manifeste-et-acceptation) |

---

<!-- l5:card -->
## MODÈLE-00 — Contrat d’une fiche

| Champ | Règle |
|---|---|
| identité | organisation, dépôt ou catalogue, nom exact, révision, fichier, format et empreinte |
| famille | lignée générale ; elle ne remplace jamais l’identité du checkpoint |
| variante | base, instruct, raisonnement, code, garde-fou ou autre spécialisation explicitement nommée |
| architecture | dense ou mélange d’experts ; paramètres totaux et actifs restent distincts |
| taille | nombre de paramètres déclaré par l’éditeur, sans en déduire seul la qualité |
| contexte | maximum annoncé, contexte réellement testé et valeur retenue par le projet |
| langues | langues annoncées puis langues effectivement évaluées par le projet |
| licence | texte exact du checkpoint, obligations de redistribution, attribution et usages restreints |
| runtime | moteur et backend testés ; voir la [fiche 04](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#moteur-00--contrat-et-vocabulaire) |
| preuve | source officielle, revue statique, test fonctionnel ou benchmark matériel daté |

**Réponse rapide :** le modèle accepté est un artefact précis, pas le nom d’une famille. Le [manifeste propriétaire du Livre I](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#32-un-modèle-doit-être-identifiable) reste la source d’exécution.

---

<!-- l5:matrix -->
## Matrice A — Sélection par usage et enveloppe

| Profil | Candidats de départ | Usage visé | Enveloppe prudente | Décision |
|---|---|---|---|---|
| très léger | Qwen3 0.6B–4B, Gemma 4 E2B/E4B, Phi-4-mini, Granite Micro/Tiny | classification, extraction, résumé court, outils simples | CPU ou faible VRAM ; contexte borné | mesurer qualité avant de privilégier la vitesse |
| local général | Qwen3 8B, Gemma 4 12B, Llama 3.1 8B, dérivé R1 7B/8B | assistant, français, JSON, code courant | Q4/Q5 comme point de départ ; un modèle chargé | profil principal à comparer sur les tâches du jeu |
| local ambitieux | Qwen3 14B, Phi-4 14B, variantes Granite Small | raisonnement, code ou rédaction plus exigeante | Q4 avec contexte réduit, offload ou CPU hybride | accepter seulement si le gain justifie latence et mémoire |
| lourd dense | Qwen3 32B, dérivé R1 32B | comparaison de qualité, tâche hors ligne | RAM importante ; GPU 12 Go insuffisant pour un chargement complet courant | laboratoire ou machine distincte |
| MoE spécialisé | Qwen3-30B-A3B, Gemma 4 26B-A4B, Mistral Small 4, Llama 4 | haut débit, multimodalité, raisonnement ou serveur | stockage selon paramètres totaux ; runtime et matériel spécialisés | ne pas confondre paramètres actifs et empreinte complète |
| service externe | modèles trop lourds pour la station | génération ponctuelle ou validation comparative | données, contrat, coût et confidentialité à qualifier | hors parcours local par défaut |

La configuration de référence conserve le [profil initial 7B–9B en Q4 et contexte 4096](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#41-configuration-prudente-initiale). Cette ligne est un **point de départ documentaire**, pas un benchmark de la RX 6750 XT.

---

<!-- l5:card -->
## MODÈLE-01 — Qwen3

| Champ | Référence datée |
|---|---|
| famille | Qwen3, publiée par l’équipe Qwen ; modèles denses et mélanges d’experts |
| tailles ouvertes annoncées | denses 0.6B, 1.7B, 4B, 8B, 14B et 32B ; MoE 30B-A3B et 235B-A22B |
| contexte annoncé | 32K pour les plus petites variantes ; jusqu’à 128K pour plusieurs variantes supérieures |
| langues | 119 langues et dialectes annoncés, dont le français |
| licence | Apache 2.0 pour les modèles ouverts listés dans l’annonce Qwen3 |
| usages | conversation, code, mathématiques, agents ; modes de raisonnement et de réponse directe selon variante |
| local | 4B ou 8B à tester en premier ; 14B seulement après mesure ; MoE non présumé adapté à 12 Go de VRAM |
| risques | format de chat, mode de raisonnement, tokenizer, quantification et dérivé communautaire peuvent changer le comportement |
| source officielle | [annonce Qwen3](https://qwenlm.github.io/blog/qwen3/) |
| sources internes | [choisir une quantification](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#42-choisir-une-quantification), [moteurs Ollama et llama.cpp](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#moteur-01--ollama) |
| preuve | revue de la source officielle le `2026-07-28` ; aucun checkpoint exécuté |

**Décision de consultation :** Qwen3 est une famille prioritaire à comparer pour le français, le code et les petits profils, mais aucun membre n’est déclaré gagnant sans exécuter la matrice C.

---

<!-- l5:card -->
## MODÈLE-02 — Gemma 4

| Champ | Référence datée |
|---|---|
| famille | Gemma 4, modèles à poids ouverts de Google |
| architectures annoncées | petites variantes effectives 2B et 4B, dense 31B, MoE 26B-A4B et variante unifiée 12B |
| contexte annoncé | 128K et jusqu’à 256K selon architecture |
| modalités | texte ; certaines variantes acceptent également image et audio |
| langues | plus de 140 langues annoncées au niveau de la famille |
| licence | conditions Gemma propres au modèle ; ne pas remplacer leur lecture par le terme « open source » |
| local | E2B/E4B pour machines contraintes ; 12B à mesurer ; 26B/31B comme profils plus lourds |
| risques | les paramètres « effectifs », actifs et totaux ne doivent pas être mélangés ; vérifier le modèle exact et ses conditions |
| sources officielles | [présentation Gemma](https://ai.google.dev/gemma/docs), [présentation Gemma 4](https://ai.google.dev/gemma/docs/core), [versions Gemma](https://ai.google.dev/gemma/docs/releases) |
| sources internes | [licence du modèle distincte du moteur](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#31-local-ne-signifie-pas-autorisé), [variables mémoire](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#matrice-b--api-formats-accélération-et-mémoire) |
| preuve | état officiel consulté le `2026-07-28` ; aucune variante téléchargée |

**Décision de consultation :** Gemma 4 apporte plusieurs enveloppes matérielles, mais son long contexte et sa multimodalité ne dispensent ni du test français ni de la vérification de la licence exacte.

---

<!-- l5:card -->
## MODÈLE-03 — Phi-4

| Champ | Référence datée |
|---|---|
| famille | Phi-4, famille de petits modèles Microsoft |
| variantes de référence | Phi-4 14B ; Phi-4-mini-instruct 3.8B ; variantes multimodales ou de raisonnement séparées |
| contexte annoncé | 128K pour Phi-4-mini-instruct |
| langues | 24 langues annoncées pour Phi-4-mini-instruct, dont le français |
| licence | MIT pour Phi-4-mini-instruct ; vérifier chaque variante séparément |
| usages | raisonnement compact, mathématiques, logique, code, outils et environnements contraints |
| local | Phi-4-mini est le candidat prioritaire ; Phi-4 14B demande une qualification mémoire plus prudente |
| risques | petit nombre de paramètres ne garantit ni français naturel, ni JSON stable, ni sécurité ; `trust_remote_code` exige une revue |
| sources officielles | [carte Microsoft Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct), [rapport technique Phi-4](https://www.microsoft.com/en-us/research/publication/phi-4-technical-report/) |
| sources internes | [jeux de tests du Livre I](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#15-jeux-de-tests), [sécurité production/runtime](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md#7-séparation-productionruntime) |
| preuve | sources Microsoft revues le `2026-07-28` ; aucune inférence exécutée |

**Décision de consultation :** Phi-4-mini est un candidat de faible empreinte, à condition de mesurer ses tâches réelles plutôt que de transférer les résultats de benchmarks éditeur.

---

<!-- l5:card -->
## MODÈLE-04 — Granite 4

| Champ | Référence datée |
|---|---|
| famille | IBM Granite 4, modèles hybrides orientés efficacité et usages d’entreprise |
| variantes annoncées | Base et Instruct en tailles Micro, Tiny et Small ; architecture hybride Mamba/transformer |
| licence | Apache 2.0 pour Granite 4.0 annoncé |
| provenance | IBM annonce signature cryptographique de checkpoints Granite 4 disponibles sur Hugging Face |
| usages | outils, RAG, workflows d’entreprise, instruction et déploiements gouvernés |
| local | Micro et Tiny à comparer pour les fonctions contraintes ; Small à mesurer selon sa variante exacte |
| langues | ne retenir que les langues déclarées dans la carte du checkpoint puis tester le français |
| risques | certification d’un processus ou signature d’un fichier ne prouve pas l’adéquation fonctionnelle au jeu |
| source officielle | [annonce IBM Granite 4.0](https://www.ibm.com/new/announcements/ibm-granite-4-0-hyper-efficient-high-performance-hybrid-models) |
| sources internes | [provenance et signature](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md#7-séparation-productionruntime), [sauvegarder manifestes et empreintes](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#17-sauvegarde-et-restauration) |
| preuve | annonce officielle revue le `2026-07-28` ; aucun checkpoint ni signature vérifiés localement |

**Décision de consultation :** Granite 4 mérite une place dans les comparaisons lorsque licence permissive, provenance et faible empreinte comptent, sans présumer sa supériorité sur les tâches créatives.

---

<!-- l5:card -->
## MODÈLE-05 — Mistral Small 4

| Champ | Référence datée |
|---|---|
| famille | Mistral Small 4, modèle hybride multimodal et de raisonnement |
| architecture annoncée | MoE, 119B paramètres totaux, 6B actifs par token, 8B avec embeddings et sortie |
| contexte annoncé | 256K |
| modalités | texte et image |
| licence | Apache 2.0 pour Mistral Small 4 |
| usages | conversation, code agentique, raisonnement configurable et analyse multimodale |
| local | paramètres actifs réduisent le calcul par token mais pas automatiquement le stockage ni toute la mémoire ; station 12 Go non présumée suffisante |
| risques | « Small » est un nom de gamme, pas une garantie d’exécution légère ; vérifier format, quantification et runtime |
| sources officielles | [annonce Mistral Small 4](https://mistral.ai/news/mistral-small-4/), [politique de licence des modèles ouverts Mistral](https://help.mistral.ai/en/articles/347393-under-which-license-are-mistral-s-open-models-available) |
| sources internes | [LocalAI pour une passerelle multi-backends](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#moteur-03--localai), [mesures obligatoires](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#16-mesures-obligatoires) |
| preuve | sources Mistral revues le `2026-07-28` ; aucun déploiement exécuté |

**Décision de consultation :** Mistral Small 4 est une référence MoE moderne pour serveur ou laboratoire, pas le choix local implicite de la configuration de référence.

---

<!-- l5:card -->
## MODÈLE-06 — Llama

| Champ | Référence datée |
|---|---|
| famille | Llama 3.x et Llama 4 de Meta |
| profils locaux encore utiles | Llama 3.2 1B/3B et Llama 3.1 8B, contexte annoncé 128K |
| génération Llama 4 | Scout 17B actifs/109B totaux et Maverick 17B actifs/400B totaux |
| contexte Llama 4 | 10M pour Scout et 1M pour Maverick annoncés dans la carte officielle |
| langues Llama 4 | douze langues prises en charge annoncées, dont le français |
| licence | licence communautaire Llama propre à la génération, obligations d’attribution et politique d’usage |
| local | privilégier les petites variantes 3.x pour la station ; Llama 4 exige un déploiement spécialisé |
| risques | ne pas traiter la licence Llama comme Apache 2.0 ou MIT ; contexte maximal et multimodalité nécessitent un runtime compatible |
| sources officielles | [catalogue officiel des modèles Llama](https://github.com/meta-llama/llama-models), [carte Llama 4](https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md), [licence Llama 4](https://github.com/meta-llama/llama-models/blob/main/models/llama4/LICENSE) |
| sources internes | [llama.cpp comme référence GGUF](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#moteur-02--llamacpp), [licences et provenance](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#31-local-ne-signifie-pas-autorisé) |
| preuve | sources Meta revues le `2026-07-28` ; aucun poids téléchargé |

**Décision de consultation :** séparer les petits modèles Llama 3.x réellement testables du nom de famille Llama 4, dont les paramètres totaux et les exigences ne correspondent pas au profil local principal.

---

<!-- l5:card -->
## MODÈLE-07 — DeepSeek-R1

| Champ | Référence datée |
|---|---|
| famille | DeepSeek-R1, modèle de raisonnement lourd, et checkpoints distillés plus petits |
| modèle principal annoncé | 671B paramètres totaux, 37B actifs, contexte 128K |
| distillations annoncées | 1.5B, 7B, 8B, 14B, 32B et 70B, dérivées de familles Qwen ou Llama |
| licence | dépôt et poids R1 sous MIT ; les distillations conservent aussi les obligations de leur famille de base |
| usages | raisonnement, mathématiques, code et comparaison de méthodes |
| local | 7B/8B comme candidats réalistes ; 14B après mesure ; modèle principal hors enveloppe de la station |
| risques | sorties longues, mélange de langues, format de raisonnement et coût en contexte ; un dérivé n’hérite pas d’une seule licence simplifiée |
| source officielle | [dépôt DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) |
| sources internes | [paramètres de génération](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#14-paramètres-de-génération), [diagnostic par couches](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#matrice-c--diagnostic-par-couches) |
| preuve | dépôt officiel revu le `2026-07-28` ; aucune distillation exécutée |

**Décision de consultation :** comparer les distillations comme modèles distincts, avec leur base, leur licence et leur template ; ne pas leur attribuer automatiquement les propriétés du modèle R1 complet.

---

<!-- l5:matrix -->
## Matrice B — Poids théoriques et quantification

| Paramètres | Q4, poids seuls | Q5, poids seuls | Q8, poids seuls | FP16, poids seuls | Lecture |
|---:|---:|---:|---:|---:|---|
| 2B | ≈ 1 Go | ≈ 1,25 Go | ≈ 2 Go | ≈ 4 Go | marge généralement importante pour contexte et runtime |
| 4B | ≈ 2 Go | ≈ 2,5 Go | ≈ 4 Go | ≈ 8 Go | profil léger courant |
| 8B | ≈ 4 Go | ≈ 5 Go | ≈ 8 Go | ≈ 16 Go | profil Q4/Q5 compatible avec une VRAM 12 Go selon runtime et contexte |
| 14B | ≈ 7 Go | ≈ 8,75 Go | ≈ 14 Go | ≈ 28 Go | marge VRAM étroite ; hybride ou contexte réduit probable |
| 32B | ≈ 16 Go | ≈ 20 Go | ≈ 32 Go | ≈ 64 Go | hors chargement complet courant en 12 Go |
| 70B | ≈ 35 Go | ≈ 43,75 Go | ≈ 70 Go | ≈ 140 Go | CPU/RAM importante ou serveur |

Ces valeurs sont des calculs **poids seuls** : `paramètres × bits ÷ 8`. Elles excluent métadonnées, tensors auxiliaires, runtime, cache KV, buffers GPU, vision, experts non chargés à la demande et copies mémoire. Pour un MoE, le stockage dépend des paramètres totaux même si le calcul par token n’active qu’une partie des experts.

---

<!-- l5:card -->
## MODÈLE-08 — Quantification

| Question | Réponse rapide |
|---|---|
| Q4 | point de départ mémoire fréquent ; la qualité dépend de la méthode et du modèle |
| Q5 | plus lourd, parfois meilleur ; valider le gain sur les tâches du projet |
| Q8 | proche d’un poids 8 bits, utile comme référence pour petits modèles |
| FP16/BF16 | référence haute précision mais souvent hors enveloppe locale |
| suffixe exact | `Q4_K_M`, `Q5_K_M`, `IQ*`, `GPTQ`, `AWQ` ou autre ne sont pas interchangeables |
| provenance | une quantification communautaire est un nouvel artefact avec auteur, fichier, révision et empreinte |
| validation | comparer même modèle, même prompt, même contexte et mêmes paramètres |

La [fiche 04](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#moteur-02--llamacpp) possède le runtime GGUF ; le [Livre I](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#42-choisir-une-quantification) possède la procédure. Cette carte ne transforme pas Q4 en recommandation universelle.

---

<!-- l5:card -->
## MODÈLE-09 — Contexte et cache KV

| Champ | Règle |
|---|---|
| contexte annoncé | limite architecturale ou commerciale publiée par l’éditeur |
| contexte du fichier | limite ou adaptation du checkpoint exact |
| contexte du runtime | valeur réellement acceptée par le moteur et le backend |
| contexte testé | valeur utilisée dans la campagne du projet |
| contexte retenu | valeur de production après qualité, mémoire et latence |
| cache KV | mémoire croissant avec contexte, couches, architecture, batch et précision |
| long contexte | ne prouve ni rappel fidèle, ni absence de dilution, ni coût acceptable |
| test | placer plusieurs faits contrôlés, demander leur restitution et mesurer erreurs et latence |

Le parcours principal démarre à `4096` jetons puis augmente **une variable à la fois**, conformément au [profil prudent du Livre I](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#41-configuration-prudente-initiale). Les 128K, 256K, 1M ou 10M annoncés restent des maxima de famille, pas des objectifs locaux.

---

<!-- l5:card -->
## MODÈLE-10 — Licence, provenance et dérivés

| Contrôle | Refus si absent |
|---|---|
| éditeur et source canonique | dépôt, organisation ou carte impossible à attribuer |
| nom et révision | alias mouvant sans commit, tag ou fichier exact |
| licence du modèle | seulement « gratuit », « open » ou « local » |
| licence de la base | dérivé ou distillation sans famille et conditions d’origine |
| licence de la quantification | auteur et redistribution inconnus |
| restrictions d’usage | politique acceptable-use ignorée |
| attribution | notices ou mentions obligatoires non conservées |
| empreinte | fichier impossible à distinguer d’une mise à jour silencieuse |
| données sensibles | modèle non qualifié promu directement au runtime |

La règle normative reste : [local ne signifie pas autorisé](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#31-local-ne-signifie-pas-autorisé). Les exigences de [provenance, SBOM et séparation production/runtime](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md#7-séparation-productionruntime) s’appliquent aussi aux modèles.

---

<!-- l5:card -->
## MODÈLE-11 — Français et multilingue

| Test | Critère |
|---|---|
| compréhension | suit une consigne française sans la traduire ni changer de langue |
| rédaction | phrases naturelles, accords, ponctuation et registre cohérents |
| extraction | conserve accents, noms propres et valeurs exactes |
| JSON | produit les clés imposées sans commentaire parasite |
| code | commentaires et identifiants selon la convention du projet |
| terminologie | respecte les noms de systèmes, factions, lieux et objets |
| refus d’invention | signale une information absente au lieu de compléter plausiblement |
| mélange de langues | aucun basculement non demandé dans les réponses longues |
| localisation | ne traite pas le français comme une simple traduction littérale de l’anglais |

Une langue annoncée dans une carte éditeur signifie **prise en charge déclarée**, pas qualité validée pour le projet. Réutiliser le [test français](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#153-test-français) et conserver les sorties brutes avant notation.

---

<!-- l5:matrix -->
## Matrice C — Tests reproductibles sans résultat inventé

| ID | Entrée stable | Mesure | Échec |
|---|---|---|---|
| TST-01 | « Réponds uniquement avec `MODELE_OK`. » | conformité exacte et latence | texte supplémentaire ou absence de réponse |
| TST-02 | résumé français d’un paragraphe technique fourni | fidélité, omissions, inventions | fait absent ajouté ou contrainte de longueur ignorée |
| TST-03 | objet JSON avec `status="ok"` et `value=42` | JSON parseable, schéma et types | Markdown, commentaire ou type incorrect |
| TST-04 | fonction GDScript typée additionnant deux entiers | syntaxe, types, retour et test minimal | code plausible mais invalide ou non typé |
| TST-05 | question dont l’information manque, réponse imposée `INFORMATION_INSUFFISANTE` | refus d’invention | réponse spéculative |
| TST-06 | trois faits repérés dans un contexte croissant | exactitude par position et taille | oubli, confusion ou citation fabriquée |
| TST-07 | même prompt avec paramètres fixés | stabilité, longueur et variance | paramètres non enregistrés |
| TST-08 | appel d’outil fictif avec schéma fermé | nom, arguments et absence d’exécution parasite | outil inventé ou argument hors schéma |

Chaque ligne est exécutée avec le **même fichier**, runtime, backend, template, contexte, température, seed si disponible et nombre d’essais. Les [mesures obligatoires](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#16-mesures-obligatoires) et la [reproductibilité](../Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md#1-rôle-du-chapitre) restent propriétaires des chapitres sources. La présente fiche ne contient aucun score.

---

<!-- l5:card -->
## MODÈLE-12 — Manifeste et acceptation

| Champ | Valeur attendue |
|---|---|
| `model_id` | identifiant stable interne |
| `family` | Qwen3, Gemma 4, Phi-4, Granite 4, Mistral, Llama, DeepSeek ou autre |
| `publisher` | organisation responsable |
| `source` | lien canonique nommé |
| `revision` | commit, tag ou révision de carte |
| `filename` | fichier réellement conservé |
| `sha256` | empreinte calculée |
| `format` | GGUF, Safetensors ou autre |
| `quantization` | valeur exacte, pas seulement « 4 bits » |
| `variant` | base, instruct, reasoning, code ou garde-fou |
| `license` | identifiant et copie du texte applicable |
| `languages_tested` | langues réellement évaluées |
| `runtime_tested` | moteur, version et backend |
| `context_tested` | valeur exécutée |
| `test_suite` | révision de la matrice C |
| `result` | candidat, accepté, refusé ou remplacé |
| `replacement` | modèle successeur lorsque pertinent |

**Porte d’acceptation :** une famille peut entrer dans la bibliothèque sans être adoptée. Un modèle n’entre dans le parcours principal que si son artefact, sa licence, son runtime, son repli CPU et ses résultats datés sont enregistrés. Les mises à jour suivent la règle [un composant à la fois](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#18-mises-à-jour).

## Frontières finales

- La [fiche 04](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md) conserve les moteurs, backends, API et diagnostics d’exécution.
- La fiche 05 conserve les familles de modèles textuels, leur sélection, licence, mémoire théorique et protocole de comparaison.
- La fiche 06 conservera checkpoints, VAE, ControlNet, LoRA et upscalers visuels.
- La fiche 07 conservera voix, transcription, musique et effets audio.
- Le chapitre 21 conservera les benchmarks réellement exécutés.
- Le chapitre 22 conservera les matrices historiques de compatibilité.
- Le chapitre 25 conservera l’inventaire transversal des licences et obligations.

## Critères d’acceptation documentaire

- au moins une famille légère, une famille dense, une famille MoE et une famille de raisonnement sont distinguées ;
- le modèle exact reste séparé de sa famille, de son moteur et de son backend ;
- les valeurs mémoire sont qualifiées comme poids théoriques ;
- les contextes annoncés ne sont pas présentés comme contextes validés ;
- les licences personnalisées, permissives et héritées des dérivés restent visibles ;
- la matrice de tests ne contient aucun résultat inventé ;
- les sources officielles et les tutoriels propriétaires sont directement accessibles ;
- aucun modèle n’est présenté comme meilleur universellement.
