---
title: "Livre V — Fiche 02 : Arbres de décision"
id: "DOC-L5-CH02"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 2
last-verified: "2026-07-28T13:00:32+02:00"
audit-status: "complete"
audit-date: "2026-07-28T13:00:32+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-02.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "conditional-decisions"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Arbres de décision

> **Type de document :** fiches d’aide à la décision, matrices de critères et scénarios.
> **Lecture :** partir du besoin, suivre les contraintes, puis ouvrir les sources indiquées.
> **Principe :** une décision valide nomme ses compromis, son repli et sa méthode de vérification. Aucun arbre ne désigne une solution universellement meilleure.

## Index express

| Je dois choisir… | Ouvrir |
|---|---|
| une voie d’accélération AMD ou CPU | [DEC-01](#dec-01--accélération-amd-cpu-ou-voie-expérimentale) |
| une exécution native, WSL ou Docker | [DEC-02](#dec-02--windows-natif-wsl-ou-docker) |
| une version et un environnement Python | [DEC-03](#dec-03--version-et-environnement-python) |
| une voie ComfyUI sur RX 6750 XT | [DEC-04](#dec-04--comfyui-sur-rx-6750-xt) |
| un moteur LLM, une interface ou une passerelle | [DEC-05](#dec-05--moteur-llm-interface-ou-passerelle) |
| un support de données ou de persistance | [DEC-06](#dec-06--resource-json-sqlite-sauvegarde-ou-index-vectoriel) |
| un transport pour un service IA local | [DEC-07](#dec-07--processus-compagnon-http-websocket-ou-file-de-tâches) |
| une étape de production d’asset | [DEC-08](#dec-08--production-intégration-et-validation-dun-asset) |
| le premier outil de diagnostic de performance | [DEC-09](#dec-09--diagnostiquer-avant-doptimiser) |
| une enveloppe Solo ou Studio | [DEC-10](#dec-10--enveloppe-solo-ou-studio) |
| une route de publication et de maintenance | [DEC-11](#dec-11--build-publication-correctif-ou-archivage) |
| entre plusieurs solutions encore plausibles | [DEC-12](#dec-12--aucune-solution-unique) |

---

<!-- l5:card -->
## DEC-00 — Lire un arbre sans transformer une préférence en fait

| Ordre | Question | Conséquence |
|---:|---|---|
| 1 | Quelle contrainte est non négociable ? | éliminer les options incompatibles avant de noter les préférences |
| 2 | Quelle preuve existe pour ce matériel, cette version et ce contexte ? | séparer support officiel, revue statique, test local et hypothèse |
| 3 | Quelle option est réversible ? | privilégier le choix dont le retour arrière est documenté |
| 4 | Quel repli conserve la fonction essentielle ? | éviter qu’une accélération, un service ou un outil facultatif devienne obligatoire |
| 5 | Quelle mesure départage les candidats restants ? | définir le test avant d’observer le résultat |
| 6 | Qui accepte la décision ? | auto-revue en Solo ou approbation indépendante en Studio selon le risque |

**Réponse rapide :** appliquer d’abord les portes éliminatoires, puis comparer les options restantes. Une pondération ne doit jamais réintroduire une option qui viole une contrainte obligatoire.

**Sources :** [politique de compatibilité](../Volume-0/CHAPITRE-09-Politique-de-compatibilite.md), [tests et simulations](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md), [architecture Solo et Studio](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#3-un-produit-deux-enveloppes-opérationnelles).

---

<!-- l5:matrix -->
## Matrice A — Pondérer sans masquer les portes éliminatoires

| Note | Interprétation |
|---:|---|
| 0 | incompatible ou preuve absente pour une contrainte obligatoire |
| 1 | possible avec réserve forte, repli ou maintenance manuelle |
| 2 | adapté au besoin avec limites connues |
| 3 | adapté, documenté et vérifiable dans le contexte retenu |

| Critère | Poids de départ Solo | Poids de départ Studio | Porte éliminatoire possible |
|---|---:|---:|---|
| compatibilité matérielle et système | 5 | 5 | oui |
| licence, provenance et redistribution | 5 | 5 | oui |
| fonction essentielle disponible sans service facultatif | 5 | 5 | oui |
| reproductibilité | 4 | 5 | oui pour une publication |
| coût de maintenance | 5 | 3 | non |
| automatisation | 2 | 5 | non |
| facilité de diagnostic | 4 | 4 | non |
| performance mesurée | 3 | 4 | non |
| réversibilité | 4 | 5 | oui pour une migration risquée |

**Usage :** adapter les poids avant le test. Conserver les notes, les sources et la raison d’une élimination. Le chapitre 23 possédera les comparatifs détaillés ; cette matrice fournit seulement une méthode commune.

---

<!-- l5:card -->
## DEC-01 — Accélération AMD, CPU ou voie expérimentale

| Question | Oui | Non |
|---|---|---|
| L’application documente-t-elle un backend compatible avec le GPU exact et la version retenue ? | utiliser ce backend, puis mesurer | continuer |
| Le modèle est-il disponible pour Windows ML, ONNX Runtime ou DirectML ? | tester la voie Windows adaptée, avec CPU comme référence | continuer |
| L’application exige-t-elle CUDA sans alternative maintenue ? | isoler un essai ZLUDA seulement si le risque est acceptable | préférer le backend natif ou le CPU |
| Le workflow fonctionne-t-il sur CPU ? | conserver ce chemin comme diagnostic et secours | réduire le workflow ou remplacer l’outil avant d’optimiser |
| Le gain a-t-il été mesuré sans perte de stabilité ? | conserver la voie accélérée avec version épinglée | revenir au chemin stable |

**Décision pour la configuration de référence :** la RX 6750 XT ne justifie pas de présenter ROCm/PyTorch Windows comme voie universelle. Le CPU reste obligatoire comme référence fonctionnelle ; ZLUDA reste un laboratoire isolé.

**Sources propriétaires :**
- [limites structurantes de la RX 6750 XT](../Livre-I/CHAPITRE-01-Materiel-Windows-pilotes-AMD-et-acceleration.md#32-limites-structurantes) ;
- [voie Windows ML, ONNX Runtime et DirectML](../Livre-I/CHAPITRE-01-Materiel-Windows-pilotes-AMD-et-acceleration.md#41-voie-a-windows-ml-onnx-runtime-et-directml) ;
- [backend natif de l’application](../Livre-I/CHAPITRE-01-Materiel-Windows-pilotes-AMD-et-acceleration.md#42-voie-b-backend-natif-spécifique-à-lapplication) ;
- [ZLUDA](../Livre-I/CHAPITRE-01-Materiel-Windows-pilotes-AMD-et-acceleration.md#43-voie-c-zluda) ;
- [CPU obligatoire](../Livre-I/CHAPITRE-01-Materiel-Windows-pilotes-AMD-et-acceleration.md#44-voie-d-cpu) ;
- [matrice de décision RX 6750 XT](../Livre-I/CHAPITRE-01-Materiel-Windows-pilotes-AMD-et-acceleration.md#5-matrice-de-décision-pour-la-rx-6750-xt).

---

<!-- l5:card -->
## DEC-02 — Windows natif, WSL ou Docker

| Besoin dominant | Choix initial | Pourquoi | Repli ou limite |
|---|---|---|---|
| accès direct au GPU AMD, à une interface graphique ou à un périphérique local | Windows natif | réduit les couches de compatibilité matérielle | isoler les dépendances par environnement et dossier |
| service web, API, base ou outil auxiliaire reproductible | Docker Desktop | sépare services, ports, volumes et dépendances | ne pas supposer un accès GPU AMD Linux équivalent |
| outil Linux en ligne de commande sans besoin GPU direct | WSL | apporte l’environnement Linux sans conteneur permanent | documenter les chemins Windows/WSL |
| service fourni et maintenu sous forme de conteneur | Docker | suit le mode de distribution prévu | vérifier volumes, secrets, ports et sauvegarde |
| doute sur la frontière | matériel et application en natif ; services auxiliaires en conteneurs | garde l’autorité près du matériel et l’infrastructure isolée | simplifier si le coût opérationnel dépasse le bénéfice |

**Sources :** [objet de Docker dans la collection](../Livre-I/CHAPITRE-05-Docker-et-Docker-Compose.md#1-objet-du-chapitre), [positionnement Windows et backend](../Livre-I/CHAPITRE-05-Docker-et-Docker-Compose.md#3-positionnement-officiel-au-18-juillet-2026), [architecture recommandée des LLM locaux](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#2-architecture-recommandée), [raison de conserver Ollama natif](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#22-pourquoi-ollama-reste-natif).

---

<!-- l5:card -->
## DEC-03 — Version et environnement Python

| Question | Décision |
|---|---|
| L’application impose-t-elle une version de Python ? | utiliser cette version dans un environnement dédié |
| Plusieurs outils imposent-ils des versions différentes ? | créer un environnement par outil ; ne pas chercher une version globale commune |
| Le projet fournit-il un fichier de verrouillage ou un manifeste ? | le traiter comme source de reconstruction |
| La commande `python` pointe-t-elle vers un interpréteur ambigu ? | utiliser un lanceur ou un chemin explicite avant toute installation |
| Une mise à niveau est-elle seulement « plus récente » ? | ne pas migrer sans compatibilité déclarée et test minimal |
| L’environnement est-il devenu difficile à expliquer ou restaurer ? | le reconstruire à partir des déclarations plutôt que le réparer indéfiniment |

**Invariant :** une application ou un projet Python possède son propre environnement, ses dépendances déclarées et une méthode de reconstruction.

**Sources :** [pourquoi isoler Python](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#1-pourquoi-isoler-python), [choisir une version](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#3-choisir-une-version-de-python), [automatisation Python du projet](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md).

---

<!-- l5:card -->
## DEC-04 — ComfyUI sur RX 6750 XT

| Porte | Décision |
|---|---|
| Besoin d’une référence fonctionnelle et diagnostiquable | installation manuelle CPU |
| Besoin de DirectML malgré ses limites connues | copie séparée, classée comme secours dégradé |
| Besoin d’essayer une application CUDA | copie ZLUDA isolée, version épinglée, retour CPU conservé |
| Tentation d’utiliser ComfyUI Desktop comme parcours AMD principal | refuser pour cette configuration de référence |
| Workflow non reproductible sur CPU | corriger le workflow avant de conclure sur le backend |
| Accélération instable après mise à jour | revenir à la copie stable et comparer les manifestes |

**Ordre conseillé :** CPU validé → workflow minimal → copie expérimentale → mesure → conservation seulement si stable.

**Sources :** [ComfyUI Desktop sous Windows](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#22-comfyui-desktop-sous-windows), [installation manuelle](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#24-installation-manuelle), [DirectML](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#25-directml), [ZLUDA](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#26-zluda), [matrice de décision ComfyUI](../Livre-I/CHAPITRE-07-ComfyUI-et-workflows-graphiques.md#3-matrice-de-décision), [provenance des références artistiques](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md).

---

<!-- l5:card -->
## DEC-05 — Moteur LLM, interface ou passerelle

| Besoin | Choix initial | Ne pas confondre |
|---|---|---|
| installation simple, gestion de modèles et API locale | Ollama natif | Ollama est un moteur, pas le modèle |
| contrôle fin d’un GGUF, CPU de référence ou benchmark | llama.cpp | un binaire Vulkan ou HIP doit être qualifié séparément |
| API unifiée pour plusieurs backends | LocalAI, seulement si cette orchestration est réellement nécessaire | la passerelle ajoute une couche à maintenir |
| interface conversationnelle principale | Open WebUI | l’interface peut répondre alors que le moteur ou le modèle échoue |
| interface agentique alternative | LibreChat | ne pas maintenir deux interfaces sans besoin distinct |
| intégration dans Godot | viser le port applicatif et le transport retenu, pas l’interface humaine | l’interface n’est pas le contrat du jeu |

**Sources :** [rôle des quatre composants](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#1-objet-du-chapitre), [parcours principal](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#21-parcours-principal), [pourquoi conserver llama.cpp](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#23-pourquoi-llamacpp-est-conservé), [interface et moteur](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#33-une-interface-nest-pas-un-moteur), [profils pour 12 Go de VRAM](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md#4-profils-de-modèles-pour-12-go-de-vram).

---

<!-- l5:card -->
## DEC-06 — Resource, JSON, SQLite, sauvegarde ou index vectoriel

| Question | Support propriétaire |
|---|---|
| La donnée est-elle une définition de conception éditée dans Godot ? | `Resource` ou configuration versionnée |
| La donnée doit-elle circuler entre outils ou représenter un document lisible ? | JSON avec schéma et version |
| Les relations, contraintes et transactions sont-elles centrales ? | SQLite derrière un contrat de persistance |
| Faut-il reconstruire une partie cohérente ? | sauvegarde versionnée distincte de la base et des caches |
| Faut-il retrouver des passages par similarité ? | index vectoriel dérivé de sources canoniques |
| La donnée peut-elle être régénérée intégralement ? | cache ou index dérivé, jamais autorité métier |
| Plusieurs catégories semblent nécessaires ? | séparer les responsabilités au lieu de choisir un stockage universel |

**Sources :** [Resources, JSON et configurations](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md), [SQLite et migrations](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md), [rôle de la sauvegarde](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#1-rôle-du-chapitre), [périmètre et frontières de la sauvegarde](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#3-périmètre-et-frontières), [mémoire vectorielle](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md), [reprise après incident](../Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md).

---

<!-- l5:card -->
## DEC-07 — Processus compagnon, HTTP, WebSocket ou file de tâches

| Situation | Choix initial | Contrôle |
|---|---|---|
| un seul processus local, démarré et arrêté avec l’application | processus compagnon et protocole borné | corrélation, délais, stderr séparé et arrêt contrôlé |
| requête courte avec réponse complète | HTTP | taille, délai, code de transport et résultat métier distincts |
| progression ou événements continus | WebSocket | files bornées, séquences et état final autoritaire |
| travail long, annulable ou limité en concurrence | file de tâches | idempotence, priorité, backpressure, expiration et polling |
| fonctionnalité essentielle du gameplay | aucun service IA obligatoire | repli déterministe local |
| exposition au réseau ou à plusieurs utilisateurs | ajouter le durcissement du chapitre sécurité | authentification, autorisation, TLS, limites et journaux |

**Sources :** [communication Godot avec les services IA](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md), [HTTP, WebSocket et files de tâches](../Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md), [séparation production/runtime et sécurité](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md), [observabilité locale](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md).

---

<!-- l5:card -->
## DEC-08 — Production, intégration et validation d’un asset

| État du besoin | Ouvrir et décider |
|---|---|
| style, usage ou budget encore flous | cadrer dans la [préproduction](../Livre-III/CHAPITRE-01-Preproduction-et-cahier-des-charges-artistique.md) avant de produire |
| besoin de références ou de concept art | utiliser le [chapitre ComfyUI artistique](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md) avec provenance |
| source 3D à construire ou maintenir | appliquer le [pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md) |
| dépendances, licences ou origine incertaines | arrêter la livraison et ouvrir la [validation de provenance](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md) |
| source approuvée prête pour le moteur | suivre le [rôle de l’importation Godot](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#1-rôle-du-chapitre) |
| personnalisation Godot à protéger d’une réimportation | respecter les [frontières d’intégration](../Livre-III/CHAPITRE-28-Importation-et-integration-dans-Godot.md#4-frontières-avec-les-chapitres-voisins) |
| premier exemplaire non encore accepté | valider manuellement avec le [chapitre 29](../Livre-III/CHAPITRE-29-Validation-technique-et-artistique-des-assets.md) |
| lot répétitif déjà qualifié | automatiser avec le [chapitre 30](../Livre-III/CHAPITRE-30-Automatisation-Blender-ComfyUI-et-production-en-lots.md) |

**Invariant :** automatiser après avoir accepté une unité représentative ; l’automatisation ne transforme pas une source incertaine en livrable valide.

---

<!-- l5:card -->
## DEC-09 — Diagnostiquer avant d’optimiser

| Signal observé | Première décision | Source |
|---|---|---|
| comportement fonctionnel incorrect | reproduire et réduire avant de profiler | [rôle du débogage](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#1-rôle-du-chapitre) |
| anomalie non reproductible | compléter environnement, état initial, étapes et preuves | [prérequis et frontières](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#4-prérequis-et-frontières) |
| absence de mesure fiable | instrumenter et journaliser | [observabilité](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md) |
| durée de frame dominée par le processeur | profiler le CPU | [profilage CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md) |
| coût de rendu, remplissage ou géométrie | profiler le GPU | [profilage GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md) |
| mémoire, VRAM ou allocations en hausse | mesurer mémoire et cycles de vie | [RAM, VRAM et allocations](../Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md) |
| saccades liées aux entrées/sorties ou changements de zone | analyser chargements et streaming | [chargements et ressources](../Livre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md) |
| script ou scène coûteux après localisation du goulot | appliquer une optimisation bornée | [scènes, scripts et systèmes](../Livre-IV/CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md) |

**Refus contrôlé :** ne pas modifier plusieurs systèmes avant d’avoir enregistré une mesure de référence et un critère d’amélioration.

---

<!-- l5:card -->
## DEC-10 — Enveloppe Solo ou Studio

| Contrainte | Solo suffit lorsque… | Studio devient pertinent lorsque… |
|---|---|---|
| propriétaires | une personne peut séparer conception, exécution et revue dans le temps | plusieurs personnes possèdent des domaines ou livrables distincts |
| revue | une auto-revue différée est proportionnée au risque | une approbation indépendante est requise |
| plateformes | une cible principale est qualifiée | plusieurs plateformes ou environnements doivent rester compatibles |
| secrets et publication | une personne peut séparer les étapes et conserver les preuves | les droits de build, signature et publication doivent être séparés |
| automatisation | les scripts locaux sont reproductibles et lisibles | les portes CI doivent être obligatoires et partagées |
| continuité | la documentation permet une reprise personnelle | le départ ou l’absence d’un membre ne doit pas bloquer le projet |

**Invariant :** le cœur métier, les formats, les identifiants et les règles de sécurité restent communs. Studio ajoute des contrôles ; il ne crée pas une seconde architecture du jeu.

**Sources :** [rôle du chapitre Solo/Studio](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#1-rôle-du-dernier-chapitre-du-livre-ii), [invariants non négociables](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#2-frontières-et-invariants-non-négociables), [deux enveloppes opérationnelles](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#3-un-produit-deux-enveloppes-opérationnelles), [Git et GitHub](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md), [DevOps](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md).

---

<!-- l5:card -->
## DEC-11 — Build, publication, correctif ou archivage

| Besoin réel | Route |
|---|---|
| vérifier chaque changement | [tests](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) → [DevOps et CI](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md) |
| produire les exécutables et paquets | [exports Godot et packaging](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md) |
| distribuer une version | [publication et distribution](../Livre-IV/CHAPITRE-17-Publication-et-distribution.md) |
| corriger une version déjà publiée | [correctifs, mises à jour et retour arrière](../Livre-IV/CHAPITRE-20-Correctifs-mises-a-jour-et-retour-arriere.md) |
| préserver sources, outils et preuves | [maintenance, archivage et pérennité](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md) |
| choisir entre publication interne et publique | qualifier licence, provenance, accessibilité, localisation, support et responsabilités avant diffusion |

**Décision :** ne pas appeler « publication » un simple export local. Chaque route possède une porte, des preuves et un retour arrière distincts.

---

<!-- l5:card -->
## DEC-12 — Aucune solution unique

| Situation | Décision correcte |
|---|---|
| deux options satisfont toutes les contraintes | conserver les deux jusqu’à une mesure discriminante |
| les mesures sont proches | choisir selon maintenance, réversibilité et compétence disponible |
| les sources officielles couvrent mal le matériel exact | classer le résultat comme non vérifié, pas comme incompatible |
| une option est plus rapide mais instable | conserver la voie stable et isoler l’expérimentation |
| une solution est meilleure seulement en Studio | ne pas imposer son coût au parcours Solo |
| une solution dépend d’un service facultatif | garantir un repli pour la fonction essentielle |
| aucune option ne passe une porte obligatoire | réduire le besoin, changer de format ou remplacer l’outil |

**Trace minimale :** besoin, contraintes, candidats écartés, sources, décision provisoire, repli, mesure à exécuter et date de révision.

**Sources :** [politique de compatibilité](../Volume-0/CHAPITRE-09-Politique-de-compatibilite.md), [matrices de compatibilité futures](index.md#chapitres), [comparatifs futurs](index.md#chapitres), [benchmarks futurs](index.md#chapitres).

---

<!-- l5:matrix -->
## Matrice B — Quatre scénarios de décision

| Scénario | Contraintes dominantes | Décision de départ | Repli | Preuve encore requise |
|---|---|---|---|---|
| artiste Solo, RX 6750 XT, images locales | AMD RDNA 2, maintenance limitée, reproductibilité | ComfyUI manuel CPU validé, puis ZLUDA isolé seulement pour comparaison | CPU | mesure sur un workflow et des modèles identifiés |
| assistant local relié à Godot | fonction essentielle sans IA, API locale, diagnostic | moteur natif documenté ; transport choisi selon requête courte, flux ou tâche | réponse déterministe locale | test de corrélation, délai, annulation et indisponibilité |
| petit jeu 3D avec assets réutilisables | source maintenable, provenance, réimportation | Blender comme source, scène d’intégration Godot, validation manuelle du premier exemplaire | dernière livraison acceptée | contrôle artistique, technique et budget runtime |
| publication Studio multiplateforme | revues indépendantes, secrets, plusieurs cibles | branche protégée, CI, exports par plateforme et approbation de publication | artefact précédent et procédure de retour arrière | campagne sur les plateformes réellement qualifiées |

**Limite :** ces scénarios montrent la méthode. Ils ne constituent ni benchmarks ni prescriptions pour un matériel différent.

---

<!-- l5:matrix -->
## Matrice C — Conséquences à enregistrer

| Dimension | Question à consigner |
|---|---|
| compatibilité | quelles versions, plateformes et architectures sont réellement couvertes ? |
| sécurité | quels privilèges, secrets, ports ou données nouvelles apparaissent ? |
| licence | quelles obligations d’usage, attribution ou redistribution s’ajoutent ? |
| performance | quelle mesure peut confirmer le bénéfice dans le contexte réel ? |
| maintenance | qui met à jour, diagnostique et restaure la solution ? |
| réversibilité | comment revenir au dernier état stable ? |
| Solo/Studio | le choix modifie-t-il seulement les contrôles ou aussi le cœur du produit ? |
| preuve | le résultat est-il une source officielle, une revue statique, un test local ou une hypothèse ? |

---

<!-- l5:card -->
## Critère d’acceptation d’une décision

Une décision issue de cette fiche est consultable lorsqu’elle contient :

1. le besoin et les contraintes obligatoires ;
2. les options considérées et les portes éliminatoires ;
3. les sources propriétaires ;
4. les compromis et conséquences ;
5. le choix initial et son repli ;
6. la validation ou la mesure encore nécessaire ;
7. le contexte Solo ou Studio lorsqu’il change la gouvernance ;
8. un niveau de preuve qui n’exagère pas ce qui a été exécuté.

Cette fiche ne remplace ni les installations détaillées du Livre I, ni les architectures du Livre II, ni les pipelines du Livre III, ni les méthodes de qualification du Livre IV. Les fiches outils du chapitre 3 décriront les logiciels ; les comparatifs du chapitre 23 approfondiront les pondérations entre solutions.
