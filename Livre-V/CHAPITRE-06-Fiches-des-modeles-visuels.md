---
title: "Livre V — Fiche 06 : Fiches des modèles visuels"
id: "DOC-L5-CH06"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 6
last-verified: "2026-07-28T16:17:52+02:00"
audit-status: "complete"
audit-date: "2026-07-28T16:17:52+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-06.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "visual-model-families-and-components"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Fiches des modèles visuels

> **Type de document :** cartes de familles, cartes de composants, matrices de compatibilité et protocole de test visuel.
> **Lecture :** identifier la tâche, puis le paquet exact de modèles et enfin le workflow, la licence, la mémoire et le niveau de preuve.
> **Principe :** un checkpoint n’est pas un workflow complet ; un VAE, un encodeur, un ControlNet, une LoRA ou un upscaler peut posséder sa propre compatibilité, sa propre licence et sa propre empreinte.

## Index express

| Besoin | Ouvrir |
|---|---|
| enregistrer un paquet visuel exact | [VISUEL-00](#visuel-00--contrat-dun-paquet-visuel) |
| choisir selon tâche et enveloppe | [Matrice A](#matrice-a--sélection-par-tâche-et-enveloppe) |
| utiliser l’écosystème Stable Diffusion | [VISUEL-01](#visuel-01--stable-diffusion-xl-et-35) |
| comparer la famille FLUX actuelle | [VISUEL-02](#visuel-02--flux2-et-flux1) |
| privilégier texte rendu et édition | [VISUEL-03](#visuel-03--qwen-image) |
| examiner un modèle MoE très lourd | [VISUEL-04](#visuel-04--hunyuanimage-30) |
| examiner une famille 17B ouverte | [VISUEL-05](#visuel-05--hidream-i1) |
| vérifier les composants obligatoires | [Matrice B](#matrice-b--compatibilité-du-paquet) |
| choisir ou remplacer un VAE | [VISUEL-06](#visuel-06--vae-et-autoencodeur) |
| identifier les encodeurs de texte | [VISUEL-07](#visuel-07--encodeurs-de-texte) |
| ajouter un contrôle structurel | [VISUEL-08](#visuel-08--controlnet-et-adaptateurs-de-contrôle) |
| ajouter une adaptation légère | [VISUEL-09](#visuel-09--lora-et-adaptations) |
| agrandir ou restaurer une image | [VISUEL-10](#visuel-10--upscalers-et-restauration) |
| qualifier un dérivé communautaire | [VISUEL-11](#visuel-11--checkpoints-communautaires-et-dérivés) |
| comparer sans inventer une qualité | [Matrice C](#matrice-c--workflow-de-test-reproductible) |
| accepter, limiter ou bloquer un paquet | [VISUEL-12](#visuel-12--manifeste-et-acceptation) |

---

<!-- l5:card -->
## VISUEL-00 — Contrat d’un paquet visuel

| Champ | Règle |
|---|---|
| identité | organisation, dépôt, révision, nom exact de chaque fichier, taille et empreinte |
| rôle | diffusion ou transformer, checkpoint monolithique, encodeur, VAE, contrôle, adaptation ou restauration |
| architecture | famille exacte ; deux composants portant le même rôle ne sont pas automatiquement interchangeables |
| format | `safetensors`, paquet Diffusers ou autre format explicitement nommé ; le format ne prouve pas la licence |
| résolution | dimensions natives ou recommandées, ratios admis et résolution réellement testée |
| échantillonnage | sampler, scheduler, nombre d’étapes, CFG ou guidance et paramètres propres à la famille |
| conditionnement | texte, image, masque, profondeur, contours, pose, références multiples ou autre entrée |
| licence | texte exact de chaque composant, conditions commerciales, redistribution et dérivés |
| runtime | version de ComfyUI, nœuds Core ou extensions, backend et niveau de compatibilité observé |
| preuve | source officielle, workflow chargé, génération réussie, comparaison datée ou validation humaine |

**Réponse rapide :** l’unité acceptée est le **paquet exécutable et documenté**, pas le seul fichier principal. Le [manifeste des modèles du Livre III](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#15-manifester-les-modèles-et-leurs-droits) reste la source de production, tandis que la [fiche 04](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#moteur-04--comfyui-comme-moteur-de-workflow) possède le moteur et les backends.

---

<!-- l5:matrix -->
## Matrice A — Sélection par tâche et enveloppe

| Besoin | Familles à examiner | Paquet minimal | Enveloppe et risque | Décision |
|---|---|---|---|---|
| concept local mature | SDXL ou dérivé documenté | checkpoint, encodeurs intégrés ou séparés, VAE | écosystème large ; qualité et licence du dérivé variables | établir une base témoin avant toute extension |
| contrôle structurel | SD3.5 avec ControlNet, FLUX avec contrôle compatible, Qwen-Image avec adaptateur qualifié | base exacte, contrôle, préprocesseur, VAE | mémoire et dépendances supplémentaires | vérifier l’architecture et le type de condition |
| génération et édition compactes | FLUX.2 Klein 4B | modèle, encodeur, autoencodeur, workflow officiel | exemples éditeur surtout NVIDIA ; aucune équivalence AMD présumée | laboratoire prioritaire seulement après démarrage CPU ou backend qualifié |
| texte dans l’image | Qwen-Image ou variante 2512 | diffusion, encodeur Qwen, VAE, éventuelle LoRA rapide | paquet volumineux ; lisibilité du français à tester | utiliser une grille typographique dédiée |
| recherche lourde | HunyuanImage-3.0, HiDream-I1 Full ou autres grands modèles | plusieurs fichiers, encodeurs et runtime spécialisé | hors enveloppe locale de référence probable | machine distincte ou service qualifié |
| adaptation de style ou sujet | LoRA compatible avec une base retenue | base exacte, LoRA, poids d’application, prompt témoin | interactions entre adaptations et droits des données | une variable par expérience |
| restauration ou agrandissement | Real-ESRGAN ou upscaler identifié | modèle de restauration, facteur, tuilage, entrée témoin | peut inventer des détails et modifier les matières | comparer à l’original, jamais remplacer la source |
| publication d’un concept | paquet déjà accepté et workflow verrouillé | manifestes, empreintes, run et rapport humain | aucune sortie n’est automatiquement un asset final | suivre le statut du Livre III |

La [chaîne de conception du Livre III](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#1-rôle-du-chapitre) conserve la décision artistique. Cette matrice aide à choisir une expérience ; elle ne remplace ni une génération, ni une revue, ni un benchmark.

---

<!-- l5:card -->
## VISUEL-01 — Stable Diffusion XL et 3.5

| Champ | Référence datée |
|---|---|
| famille | SDXL reste une base d’écosystème ; Stable Diffusion 3.5 comprend Large, Large Turbo et Medium |
| architecture | la famille 3.5 n’est pas compatible par simple nom avec les composants SDXL ou SD 1.x |
| contrôle officiel | trois ControlNets SD3.5 Large publiés pour Blur, Canny et Depth |
| licence | Stability AI Community License pour les modèles couverts ; seuil et conditions commerciales à relire avant publication |
| formats | poids et code disponibles depuis les pages officielles ; enregistrer le fichier exact et sa révision |
| résolution | utiliser les dimensions du modèle ou du template exact ; ne pas transférer une résolution SDXL vers SD3.5 |
| local AMD | des variantes ONNX optimisées AMD existent, mais elles ne prouvent pas un workflow ComfyUI sur RX 6750 XT |
| alternatives | SDXL pour l’écosystème mature ; FLUX.2 Klein ou Qwen-Image selon édition, texte et enveloppe |
| sources officielles | [présentation Stable Diffusion 3.5](https://stability.ai/news/introducing-stable-diffusion-3-5), [licences Stability AI](https://stability.ai/license), [ControlNets SD3.5 Large](https://stability.ai/news-updates/sd3-5-large-controlnets), [variantes AMD](https://stability.ai/news-updates/stable-diffusion-now-optimized-for-amd-radeon-gpus) |
| sources internes | [état et voies ComfyUI](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#2-état-officiel-au-18-juillet-2026), [matrice des backends](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#matrice-b--api-formats-accélération-et-mémoire) |
| preuve | sources éditeur revues le `2026-07-28` ; aucun fichier chargé ni résultat produit |

**Décision de consultation :** séparer SDXL, SD3.5 Medium et SD3.5 Large comme trois paquets de test. Une LoRA ou un ControlNet n’est accepté qu’après confirmation explicite de sa base.

---

<!-- l5:card -->
## VISUEL-02 — FLUX.2 et FLUX.1

| Champ | Référence datée |
|---|---|
| famille actuelle | FLUX.2 couvre génération et édition ; la branche Klein propose des variantes 4B et 9B, distillées ou Base |
| variantes locales | Klein 4B et 4B Base sous Apache 2.0 ; Klein 9B, 9B Base et FLUX.2 Dev sous licence non commerciale FLUX |
| génération et édition | texte-vers-image, édition à une ou plusieurs références selon variante |
| composants | modèle de flux, encodeur de texte et autoencodeur FLUX.2 séparé ; les fichiers FLUX.1 ne sont pas présumés compatibles |
| personnalisation | variantes Base pour adaptation ; modèles distillés pour peu d’étapes, sans transférer leurs réglages |
| mémoire | les chiffres officiels dépendent de précision, quantification et GPU NVIDIA ; aucune compatibilité RX 6750 XT n’est déduite |
| FLUX.1 | Schnell sous Apache 2.0 ; Dev et outils associés sous licence non commerciale dédiée |
| ComfyUI | workflows officiels disponibles, mais la présence d’un template peut exiger une version récente des nœuds Core |
| sources officielles | [dépôt FLUX.2](https://github.com/black-forest-labs/flux2), [présentation FLUX.2 Klein](https://bfl.ai/blog/flux2-klein-towards-interactive-visual-intelligence), [dépôt FLUX.1](https://github.com/black-forest-labs/flux), [workflow ComfyUI FLUX.2 Klein](https://docs.comfy.org/tutorials/flux/flux-2-klein) |
| sources internes | [environnement qualifié](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#12-séparer-environnement-de-recherche-et-environnement-qualifié), [ZLUDA et repli CPU](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#backend-04--zluda) |
| preuve | état officiel consulté le `2026-07-28` ; aucune variante exécutée |

**Décision de consultation :** Klein 4B est le premier candidat FLUX.2 à étudier pour un poste local, mais son positionnement « grand public » ne vaut pas qualification AMD ou promesse de tenir entièrement dans 12 Go.

---

<!-- l5:card -->
## VISUEL-03 — Qwen-Image

| Champ | Référence datée |
|---|---|
| famille | Qwen-Image, modèle MMDiT 20B orienté génération, rendu de texte et édition |
| état courant | ComfyUI documente Qwen-Image-2512 comme mise à jour de décembre et des variantes d’édition séparées |
| composants | modèle de diffusion, encodeur Qwen 2.5 VL, VAE et éventuelle LoRA d’accélération |
| licence | Apache 2.0 annoncé pour la base ouverte ; vérifier chaque mise à jour, contrôle et LoRA séparément |
| texte | capacités annoncées en plusieurs langues ; le français, les accents et les petites tailles doivent être testés |
| résolution | suivre les ratios et dimensions du template exact ; ne pas forcer une taille arbitraire comme baseline |
| contrôle | ControlNets, patches ou LoRA de contrôle existent, avec compatibilités et préprocesseurs propres |
| mémoire | 20B et plusieurs composants ; ne pas présumer un chargement local complet sur 12 Go de VRAM |
| sources officielles | [annonce Qwen-Image](https://qwenlm.github.io/blog/qwen-image/), [workflow ComfyUI Qwen-Image](https://docs.comfy.org/tutorials/image/qwen/qwen-image), [workflow Qwen-Image-2512](https://docs.comfy.org/tutorials/image/qwen/qwen-image-2512) |
| sources internes | [prompt structuré et contrôle humain](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#18-écrire-un-contrat-de-prompt), [fiche des modèles de langage](CHAPITRE-05-Fiches-des-modeles-de-langage.md#modèle-00--contrat-dune-fiche) |
| preuve | pages officielles revues le `2026-07-28` ; aucun test typographique exécuté |

**Décision de consultation :** réserver une planche dédiée au texte français, aux signes diacritiques, aux alignements et aux petits corps. Une démonstration anglaise ou chinoise ne valide pas cette tâche.

---

<!-- l5:card -->
## VISUEL-04 — HunyuanImage-3.0

| Champ | Référence datée |
|---|---|
| famille | HunyuanImage-3.0, modèle multimodal autorégressif de génération et d’édition |
| architecture annoncée | mélange de 64 experts, 80B paramètres totaux et 13B actifs |
| variantes | base texte-vers-image, Instruct pour édition et raisonnement, Instruct-Distil à moins d’étapes |
| composants | checkpoint, tokenizer, code distant et dépendances d’inférence ; plusieurs licences peuvent intervenir |
| mémoire | modèle de recherche lourd, non présumé compatible avec le poste local de référence |
| runtime | exemples officiels CUDA et vLLM ; aucun support AMD Windows ou ComfyUI Core n’est inféré |
| licence | lire le fichier de licence du dépôt et les conditions du checkpoint exact avant tout téléchargement |
| usage | comparaison hors ligne, édition complexe ou service spécialisé après qualification |
| source officielle | [dépôt HunyuanImage-3.0](https://github.com/Tencent-Hunyuan/HunyuanImage-3.0) |
| sources internes | [séparer moteur et modèle](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md#moteur-00--contrat-et-vocabulaire), [niveau de preuve du pipeline visuel](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#2-portée-niveau-de-preuve-et-réserves) |
| preuve | dépôt officiel revu le `2026-07-28` ; aucune installation ni exécution |

**Décision de consultation :** conserver HunyuanImage-3.0 comme référence de modèle lourd. Il ne doit pas déplacer les baselines locales avant disponibilité d’un environnement matériel et juridique approprié.

---

<!-- l5:card -->
## VISUEL-05 — HiDream-I1

| Champ | Référence datée |
|---|---|
| famille | HiDream-I1, modèle de génération d’images 17B |
| variantes | Full, Dev et Fast avec nombres d’étapes de référence distincts |
| licence | dépôt et modèles annoncés sous MIT ; l’encodeur Llama 3.1 8B possède ses propres conditions |
| composants | modèle HiDream, tokenizers, plusieurs encodeurs dont Llama, VAE et pipeline |
| runtime | implémentation officielle centrée CUDA et Flash Attention |
| mémoire | aucune adaptation AMD Windows ou exécution 12 Go n’est présumée |
| avantage documentaire | illustre pourquoi une licence permissive du modèle principal ne couvre pas toute la chaîne |
| alternative | FLUX.2 Klein pour un paquet plus compact ; SDXL pour un écosystème plus ancien et large |
| source officielle | [dépôt HiDream-I1](https://github.com/HiDream-ai/HiDream-I1) |
| sources internes | [licences de chaque dépendance](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#4-vocabulaire-opérationnel), [manifester les composants](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#15-manifester-les-modèles-et-leurs-droits) |
| preuve | dépôt officiel revu le `2026-07-28` ; aucun modèle téléchargé |

**Décision de consultation :** ne pas étiqueter le paquet entier « MIT » sans enregistrer séparément l’encodeur Llama, ses fichiers et ses conditions.

---

<!-- l5:matrix -->
## Matrice B — Compatibilité du paquet

| Composant | Doit correspondre à | Symptôme d’incompatibilité | Preuve minimale |
|---|---|---|---|
| diffusion ou transformer | architecture, précision et chargeur | nœud absent, forme de tenseur invalide, sortie incohérente | modèle exact chargé par un workflow officiel ou qualifié |
| encodeur de texte | tokenizer et architecture attendus | prompt ignoré, erreur de dimensions, langue dégradée | fichier, révision, tokenizer et test de prompt témoin |
| VAE ou autoencodeur | espace latent et échelle du modèle | couleurs, contraste, détails ou décodage incorrects | VAE recommandé ou comparaison documentée |
| ControlNet | famille de base et type de condition | contrôle inactif, erreur de forme ou composition instable | base, contrôle, préprocesseur et entrée témoin identifiés |
| LoRA | architecture, modules ciblés et convention de poids | aucun effet, artefacts ou sur-contrainte | base exacte, poids, déclencheurs et intensité enregistrés |
| upscaler | domaine d’image et facteur | textures plastifiées, halos, lignes inventées | modèle, facteur, tuilage et comparaison à 100 % |
| sampler et scheduler | famille et variante distillée ou non | bruit résiduel, surcuisson ou résultat non comparable | paramètres issus du template ou de la carte du modèle |
| nœuds ComfyUI | version Core ou commit de l’extension | workflow incomplet ou comportement modifié | version de ComfyUI, nœuds et dépendances épinglés |
| backend | opérations réellement prises en charge | fallback CPU, erreur mémoire ou résultat différent | journal, mémoire et génération témoin sur le matériel |
| licence | chaque fichier et dérivé | usage ou redistribution bloqués | texte de licence archivé et décision humaine |

La [documentation ComfyUI sur les modèles](https://docs.comfy.org/development/core-concepts/models) confirme que checkpoints, VAE, LoRA, ControlNet et upscalers sont des poids distincts. Le [workflow JSON canonique](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#14-enregistrer-le-workflow-json-comme-source-canonique) doit citer chacun d’eux.

---

<!-- l5:card -->
## VISUEL-06 — VAE et autoencodeur

| Champ | Référence |
|---|---|
| besoin | encoder une image vers l’espace latent et décoder le latent vers l’image |
| réponse rapide | employer le VAE ou autoencodeur explicitement recommandé par la famille ou le checkpoint |
| identité | fichier, architecture, révision, empreinte, précision et licence |
| compatibilité | l’espace latent, l’échelle et les canaux doivent correspondre au modèle |
| comparaison | même latent ou même workflow, sans modifier sampler, prompt ou seed |
| contrôles | couleurs, noirs, hautes lumières, gradients, détails fins, bandes et saturation |
| mémoire | peut être chargé, déchargé ou tuilé selon le runtime ; mesurer au lieu de supposer |
| risque | un VAE « plus net » peut modifier la matière ou masquer des défauts plutôt qu’améliorer la fidélité |
| alternative | VAE intégré au checkpoint seulement si son identité est connue et acceptée |
| source officielle | [modèles et répertoires ComfyUI](https://docs.comfy.org/development/core-concepts/models) |
| source interne | [composants secondaires du manifeste](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#15-manifester-les-modèles-et-leurs-droits) |
| preuve | revue statique ; aucun décodage comparatif exécuté |

---

<!-- l5:card -->
## VISUEL-07 — Encodeurs de texte

| Champ | Référence |
|---|---|
| besoin | transformer le texte en conditionnement consommé par le modèle visuel |
| réponse rapide | enregistrer tokenizer, encodeur, précision et révision comme dépendances du paquet |
| familles | CLIP, T5, Qwen VL, Llama ou autres selon l’architecture |
| compatibilité | une version voisine ou quantifiée peut changer mémoire, longueur et sémantique |
| langues | tester le français, les accents, la négation, les noms propres et le vocabulaire du projet |
| mémoire | certains grands modèles visuels déplacent une part importante de la mémoire vers l’encodeur |
| sécurité | `trust_remote_code` ou code de tokenizer impose une revue séparée |
| licence | l’encodeur peut avoir des conditions différentes du générateur principal |
| validation | comparer un jeu de prompts identique et conserver les tokenizers exacts |
| source officielle | [paquet Qwen-Image-2512 dans ComfyUI](https://docs.comfy.org/tutorials/image/qwen/qwen-image-2512) |
| sources internes | [contrat de prompt](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#18-écrire-un-contrat-de-prompt), [tests multilingues](CHAPITRE-05-Fiches-des-modeles-de-langage.md#modèle-11--français-et-multilingue) |
| preuve | revue statique ; aucun tokenizer ni encodeur chargé |

---

<!-- l5:card -->
## VISUEL-08 — ControlNet et adaptateurs de contrôle

| Champ | Référence |
|---|---|
| besoin | imposer contours, profondeur, pose, masque, flou ou autre structure à une génération |
| réponse rapide | choisir un contrôle explicitement entraîné ou adapté pour la base exacte |
| paquet | modèle de contrôle, préprocesseur, image condition, VAE éventuel et nœuds d’application |
| paramètres | force, début et fin d’application, résolution du préprocesseur et éventuel mode de devinette |
| compatibilité | SD 1.x, SDXL, SD3.5, FLUX et Qwen-Image ne partagent pas automatiquement les contrôles |
| limites | le contrôle influence une condition ; il ne garantit ni anatomie, ni matériaux, ni droits |
| sécurité | un préprocesseur ou custom node reste du code tiers à qualifier |
| alternatives | masque et image-vers-image, LoRA de contrôle, modèle natif d’édition |
| sources officielles | [implémentation ControlNet](https://github.com/lllyasviel/ControlNet), [exemple ControlNet ComfyUI](https://docs.comfy.org/tutorials/controlnet/controlnet), [ControlNets SD3.5](https://stability.ai/news-updates/sd3-5-large-controlnets) |
| sources internes | [nœuds Core avant extensions](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#13-commencer-par-les-nœuds-core), [workflow de contrôle FLUX](https://docs.comfy.org/tutorials/flux/flux-1-controlnet) |
| preuve | revue documentaire ; aucun contrôle appliqué |

---

<!-- l5:card -->
## VISUEL-09 — LoRA et adaptations

| Champ | Référence |
|---|---|
| besoin | adapter une base à un sujet, une apparence, un mouvement ou une fonction sans remplacer tous ses poids |
| réponse rapide | enregistrer base exacte, modules ciblés, rang, fichier, déclencheurs et poids d’application |
| compatibilité | une LoRA SDXL, SD3, FLUX ou Qwen ne se transfère pas par extension de fichier |
| combinaison | plusieurs LoRA peuvent interagir ; ajouter une seule adaptation par expérience initiale |
| licence | conditions du fichier, de la base, des données d’entraînement et des sorties restent séparées |
| provenance | auteur, dépôt, révision, dataset déclaré, images d’exemple et empreinte |
| validation | prompts positifs, négatifs et hors domaine ; comparaison avec base seule |
| risque | reproduire une identité, une marque ou une apparence protégée peut être indésirable même si le fichier est techniquement compatible |
| alternative | checkpoint spécialisé, contrôle structurel ou édition par référence |
| sources officielles | [guide LoRA Diffusers](https://github.com/huggingface/diffusers/blob/main/docs/source/en/training/lora.md), [chargeurs LoRA Diffusers](https://github.com/huggingface/diffusers/blob/main/docs/source/en/api/loaders/lora.md) |
| sources internes | [matrice d’expériences](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#20-construire-une-matrice-dexpériences), [provenance des transformations](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#4-vocabulaire-opérationnel) |
| preuve | revue statique ; aucune LoRA entraînée ou chargée |

---

<!-- l5:card -->
## VISUEL-10 — Upscalers et restauration

| Champ | Référence |
|---|---|
| besoin | augmenter les dimensions ou restaurer certains défauts d’une image dérivée |
| réponse rapide | traiter l’upscaler comme un modèle de transformation, pas comme une récupération fidèle de détails absents |
| familles | Real-ESRGAN, ESRGAN, SwinIR ou modèle spécialisé explicitement identifié |
| paramètres | facteur, tuilage, recouvrement, réduction de bruit, espace colorimétrique et traitement alpha |
| domaine | photographie, illustration, anime, textures ou vidéo ; un modèle général n’est pas universel |
| contrôle | comparer à 100 %, vérifier halos, répétitions, coutures, texte, lignes, grain et micro-détails inventés |
| source | conserver l’image originale ; l’upscale est un dérivé remplaçable |
| licence | code et poids peuvent avoir des licences ou provenances différentes |
| alternative | génération haute résolution, latent upscale, tiled diffusion ou réexport depuis une source vectorielle |
| source officielle | [dépôt Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) |
| sources internes | [architecture des modèles ComfyUI](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#4-architecture-des-dossiers), [validation des assets](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md) |
| preuve | revue documentaire ; aucune image restaurée ou agrandie |

---

<!-- l5:card -->
## VISUEL-11 — Checkpoints communautaires et dérivés

| Champ | Référence |
|---|---|
| besoin | qualifier un fine-tune, un merge, une conversion ou une quantification publié par un tiers |
| réponse rapide | partir de l’artefact exact et reconstruire sa chaîne vers les bases et composants |
| identité | auteur, plateforme, page, version, date, fichier, taille, SHA-256 et format |
| dérivation | base, recette de merge, entraînement, dataset déclaré, VAE, encodeurs et adaptations intégrées |
| licence | licence propre, licences héritées et restrictions de la base ; absence ou ambiguïté bloque |
| sécurité | préférer un format de poids sans exécution Python, sans confondre ce choix avec une garantie juridique ou fonctionnelle |
| exemples | images de démonstration et prompts ne prouvent ni fichier utilisé, ni seed, ni absence de retouche |
| compatibilité | vérifier chargeur, architecture, résolution, prediction type et composants inclus |
| statut | `intake`, `quarantined`, `under_review`, `accepted_limited`, `accepted` ou `blocked` |
| alternative | modèle éditeur ou paquet déjà qualifié |
| sources internes | [cycle de vie des assets](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#6-cycle-de-vie-et-statuts), [identifiant stable](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#7-identifiant-stable-et-versions) |
| preuve | règle de gouvernance ; aucun dépôt communautaire audité dans cette fiche |

---

<!-- l5:matrix -->
## Matrice C — Workflow de test reproductible

| Test | Variables fixes | Variable observée | Mesures ou revue | Sortie attendue |
|---|---|---|---|---|
| T1 — chargement | paquet, workflow et backend | capacité à charger chaque composant | journal, RAM, VRAM, fallback et durée de chargement | statut fonctionnel ou blocage précis |
| T2 — baseline | prompt, seed, dimensions et sampler | modèle ou variante | durée, pic mémoire, erreur, image et empreinte | témoin conservé sans jugement global |
| T3 — résolution | prompt, seed et modèle | dimensions ou ratio | stabilité, composition, artefacts et mémoire | plage retenue, pas maximum théorique |
| T4 — sampler | modèle, prompt, seed et taille | sampler, scheduler ou étapes | cohérence, défauts et coût | réglage retenu pour ce workflow |
| T5 — français | paquet et paramètres | prompts français et texte rendu | accents, casse, petits corps, sens et mise en page | rapport typographique |
| T6 — contrôle | base, prompt et seed | type, force, début et fin du contrôle | fidélité structurelle et artefacts | contrôle accepté ou rejeté |
| T7 — adaptation | base et workflow | LoRA et poids | effet utile, sur-apprentissage, collisions et hors domaine | plage de poids et restrictions |
| T8 — restauration | image source | upscaler et paramètres | halos, coutures, détails inventés, couleur et alpha | dérivé comparé à l’original |
| T9 — reproductibilité | paquet et workflow inchangés | répétition sur même puis autre backend | octets, famille visuelle, erreurs et versions | allégation exacte ou de famille |
| T10 — revue humaine | sorties anonymisées et critères | candidat | anatomie, matière, fonction, culture, droits et bible | sélection, rejet ou nouvelle expérience |

Le [contrat des seeds](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#17-gérer-les-seeds-et-la-reproductibilité-réelle) interdit de promettre une identité universelle. Les résultats chiffrés appartiendront au chapitre 21 du Livre V ; cette matrice définit seulement le protocole.

---

<!-- l5:card -->
## VISUEL-12 — Manifeste et acceptation

| Champ | Valeur à enregistrer |
|---|---|
| paquet | identifiant, but, propriétaire, statut et date de décision |
| composants | rôle, fournisseur, dépôt, révision, fichier, taille, empreinte et format |
| compatibilité | architecture, ComfyUI, nœuds, backend, OS et matériel réellement testés |
| workflow | fichier JSON, empreinte, template d’origine et modifications |
| paramètres | dimensions, sampler, scheduler, étapes, guidance, seed et entrées |
| droits | licence de chaque composant, preuves, restrictions, attribution et périmètre accepté |
| résultats | identifiants de runs, images témoins, empreintes et rapport de revue |
| performance | durée, mémoire, backend et niveau de preuve, sans valeur préremplie |
| reproductibilité | non testée, famille reproduite ou octets reproduits dans un environnement défini |
| décision | `accepted`, `accepted_limited`, `blocked`, `withdrawn` ou `superseded` avec approbateur |
| retrait | dépendances et workflows affectés, remplacement, date et conservation des preuves |

**Porte minimale :** aucun paquet n’est `accepted` sans identité complète, licence relue, workflow versionné, génération témoin, revue humaine et repli documenté. Une image persuasive reste une proposition tant qu’elle n’a pas franchi les portes décrites dans [les statuts de concept](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md#3-distinguer-inspiration-référence-concept-source-et-asset-final).

**Frontières :**

- la fiche 03 possède l’application ComfyUI et les outils ;
- la fiche 04 possède le moteur, les API et les backends ;
- la fiche 06 possède les familles visuelles et leurs composants ;
- la fiche 08 possédera les workflows réutilisables ;
- le chapitre 21 possédera les mesures exécutées ;
- le chapitre 22 possédera les compatibilités historiques ;
- le chapitre 25 possédera l’inventaire transversal des licences ;
- la création et la sélection artistiques restent dans le Livre III.

**Niveau de preuve :** `static-review`. Aucun checkpoint, VAE, encodeur, ControlNet, LoRA ou upscaler n’a été téléchargé ; aucun workflow n’a été chargé ; aucune image, mesure RAM/VRAM, comparaison ou approbation juridique n’a été produite.
