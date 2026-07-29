---
title: "Livre V — Fiche 21 : Benchmarks et méthodes de mesure"
id: "DOC-L5-CH21"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 21
last-verified: "2026-07-29T18:11:00+02:00"
audit-status: "complete"
audit-date: "2026-07-29T18:11:00+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-21.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "reproducible-benchmarks-measurement-statistics-and-comparison"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-python:
  implementation: "CPython"
  version: "3.14.6"
  fallback-version: "3.13.14"
  qualification-status: "inherited-provisional"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Benchmarks et méthodes de mesure

> **Type de document :** contrats de benchmark, matrices de contrôle, formats de résultats et portes d’interprétation.
> **Lecture :** partir de la décision à prendre, figer le protocole avant la campagne, conserver les observations brutes, puis séparer calcul, interprétation et décision.
> **Principe :** une mesure est vraie pour un objet, un scénario, un environnement, une période et une méthode identifiés ; elle ne devient pas une propriété universelle du produit ou de l’outil.

## Index express

| Besoin | Ouvrir |
|---|---|
| définir un benchmark complet | [BMK-00](#bmk-00--contrat-minimal-dun-benchmark) |
| choisir la méthode propriétaire | [Matrice A](#matrice-a--routage-par-famille-de-mesure) |
| formuler la question et la décision | [BMK-01](#bmk-01--question-hypothèse-et-décision) |
| figer matériel, logiciel et build | [BMK-02](#bmk-02--empreinte-denvironnement-et-dobjet) |
| stabiliser scénario, charge et fixtures | [BMK-03](#bmk-03--scénario-charge-et-fixtures) |
| distinguer froid, chaud, cache et warm-up | [BMK-04](#bmk-04--warm-up-caches-et-états-froid-chaud) |
| contrôler, randomiser ou rapporter les facteurs | [Matrice B](#matrice-b--facteurs-à-contrôler-randomiser-ou-rapporter) |
| organiser répétitions et ordre des variantes | [BMK-05](#bmk-05--runs-répétitions-ordre-et-arrêt) |
| choisir horloge, unité et cadence | [BMK-06](#bmk-06--unités-horloges-précision-et-instrumentation) |
| conserver les observations brutes | [BMK-07](#bmk-07--format-des-données-brutes-et-nullabilité) |
| résumer une distribution | [BMK-08](#bmk-08--statistiques-dispersion-et-incertitude) |
| traiter valeurs aberrantes et données manquantes | [BMK-09](#bmk-09--valeurs-aberrantes-données-manquantes-et-exclusions) |
| comparer baseline et candidate | [BMK-10](#bmk-10--comparaison-effet-et-signification-pratique) |
| produire un rapport lisible et vérifiable | [BMK-11](#bmk-11--visualisation-rapport-et-séparation-des-couches) |
| savoir ce que la preuve autorise | [Matrice C](#matrice-c--niveaux-de-preuve-et-déclarations-permises) |
| répéter, maintenir et retirer un benchmark | [BMK-12](#bmk-12--répétition-indépendante-maintenance-et-retrait) |

---

<!-- l5:card -->
## BMK-00 — Contrat minimal d’un benchmark

| Champ | Règle |
|---|---|
| identité | identifiant stable, version du protocole, propriétaire et date |
| décision | question à résoudre et action possible selon le résultat |
| objet | build, outil, modèle, asset, scène, service, configuration ou algorithme mesuré |
| variantes | baseline, candidate et changements autorisés entre elles |
| métriques | grandeur, direction favorable, unité, source, cadence et agrégation |
| scénario | charge, fixtures, entrées, durée, seed, parcours et préconditions |
| environnement | matériel, OS, pilotes, versions, build, profil d’alimentation et processus concurrents |
| états | warm-up, caches, froid/chaud, initialisation, stabilisation et nettoyage |
| plan d’exécution | runs, répétitions, ordre, randomisation, pauses et conditions d’arrêt |
| données | observations brutes, statuts, nullabilité, empreintes et artefacts |
| analyse | statistiques prévues, exclusions, comparaisons, graphiques et incertitude |
| portes | critères fonctionnels, qualité, sécurité, confidentialité et décision humaine |
| limites | population, plateformes, versions et situations auxquelles le résultat ne s’applique pas |

**Réponse rapide :** le [contrat CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md#9-contrat-de-benchmark), le [contrat GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md#9-contrat-de-benchmark-gpu), la [campagne mémoire](../Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md#10-contrat-de-campagne-mémoire) et le [benchmark de scène](../Livre-IV/CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md#8-contrat-de-benchmark-de-scène) restent propriétaires de leurs domaines. La présente fiche normalise ce qui permet de les comparer et de les auditer.

**Diagramme compact :** `décision → protocole figé → runs bruts → contrôles → analyse prévue → interprétation bornée → décision et réserves`.

**Niveau de preuve :** `static-review`. Aucun protocole n’est exécuté, aucune série n’est mesurée et aucune performance de `Project Asteria` n’est revendiquée.

---

<!-- l5:matrix -->
## Matrice A — Routage par famille de mesure

| Question dominante | Métrique ou artefact principal | Source propriétaire | Contrôle indispensable |
|---|---|---|---|
| coût CPU d’une frame ou fonction | temps propre/inclusif, médiane, p95, p99, dépassements | [profilage CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md#8-mesurer-plusieurs-distributions-pas-un-seul-nombre) | même scénario, profiler déclaré, suite fonctionnelle |
| coût GPU et qualité visuelle | temps GPU, passes, draw calls, capture et profil visuel | [profilage GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md#7-distinguer-cpu-de-rendu-gpu-et-attente) | résolution, V-Sync, pilote, caméra et comparaison d’image |
| RAM, VRAM ou allocations | série temporelle, pic, plateau, croissance par cycle | [mémoire](../Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md#7-les-quatre-questions-dune-enquête-mémoire) | cycles, durée, compteur exact et test prolongé |
| chargement ou streaming | froid/chaud, premier retour, prêt interactif, blocage principal | [chargements](../Livre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md#8-budgets-de-chargement) | stockage, cache, phases et activation séparés |
| scènes, scripts et systèmes | coût × fréquence × multiplicité, pics d’activation | [optimisation des systèmes](../Livre-IV/CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md#7-classer-le-coût-avant-de-modifier) | une cause principale, population et fréquence figées |
| équilibrage ou simulation | compteur, ratio, distribution, intervalle et scénario | [télémétrie locale](../Livre-IV/CHAPITRE-01-Equilibrage-et-telemetrie-locale.md#7-formuler-une-question-mesurable) | question préalable, seed, dénominateur et absence de donnée personnelle |
| comportement fonctionnel | résultat attendu/observé et statut de cas | [tests fonctionnels](../Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md#6-contrat-dun-cas) | oracle indépendant de la métrique de performance |
| incident intermittent | fréquence, environnement et archive de reproduction | [reproduction des anomalies](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#16-fréquence-et-tentatives) | tentatives, conditions et statuts `BLOCKED`/`NOT_REPRODUCED` |
| événement, métrique ou trace | faits structurés, agrégats et chemin corrélé | [observabilité locale](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md#8-distinguer-événements-métriques-et-traces) | cardinalité, rétention, coût et absence de causalité supposée |
| réseau et synchronisation | latence, gigue, perte, débit, désynchronisation | [autorité et prédiction](../Livre-IV/CHAPITRE-12-Synchronisation-autorite-et-prediction.md#1-rôle-du-chapitre) | topologie, horloges, conditions réseau et autorité |
| CI, build ou livraison | durée de job, taux d’échec, taille, installation et reprise | [DevOps](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#1-rôle-du-chapitre) | runner, cache, artefact, permissions et révision |
| asset graphique ou audio | qualité, import, mémoire, temps et limites de famille | [référence graphique](CHAPITRE-18-Reference-graphique-et-3D.md#g3d-11--presets-checklists-et-comparaison-des-pilotes) et [référence audio](CHAPITRE-19-Reference-audio.md#audr-11--budgets-profils-presets-et-mesures) | source, preset, scène, dispositif et revue humaine |
| modèle IA local | latence, débit, mémoire, qualité et taux d’échec | [modèles de langage](CHAPITRE-05-Fiches-des-modeles-de-langage.md) et [modèles audio](CHAPITRE-07-Fiches-des-modeles-audio.md) | modèle exact, quantification, backend, prompt ou échantillon et licence |

**Décision :** choisir d’abord le chapitre propriétaire de la grandeur, puis appliquer le contrat transversal. Une même session peut produire plusieurs métriques, mais chaque conclusion conserve son propriétaire et sa porte.

---

<!-- l5:card -->
## BMK-01 — Question, hypothèse et décision

| Élément | Formulation utile | Formulation à éviter |
|---|---|---|
| question | « sur le scénario S et la plateforme P, la candidate réduit-elle le p95 de X sans dépasser Y ? » | « est-ce plus rapide ? » |
| hypothèse | relation testable entre un changement et une métrique | justification écrite après lecture des résultats |
| métrique primaire | unique grandeur qui décide la comparaison principale | sélection de la meilleure valeur après la campagne |
| métriques secondaires | contexte, qualité, sécurité et mécanismes possibles | liste illimitée utilisée pour chercher un résultat favorable |
| direction | inférieur, supérieur, proche d’une cible ou dans une plage | « meilleur » sans convention |
| seuil pratique | écart minimal qui change réellement une décision | différence numériquement visible mais sans effet produit |
| arrêt | nombre prévu de runs ou condition de sécurité | arrêt dès qu’une tendance plaît |
| décision | adopter, conserver, rejeter, répéter ou déclarer indéterminé | forcer une conclusion binaire |

**Réponse rapide :** la question précède la collecte, comme dans la [boucle d’équilibrage](../Livre-IV/CHAPITRE-01-Equilibrage-et-telemetrie-locale.md#1-rôle-du-chapitre). La métrique primaire et le seuil pratique sont figés avant d’ouvrir les résultats ; les métriques secondaires peuvent expliquer, jamais remplacer silencieusement l’objectif initial.

**Diagramme compact :** `question → hypothèse → métrique primaire → seuil pratique → plan d’arrêt → données → décision`.

**Limite :** une campagne exploratoire peut découvrir de nouvelles hypothèses, mais ses constats doivent être étiquetés exploratoires et confirmés par une campagne séparée.

---

<!-- l5:card -->
## BMK-02 — Empreinte d’environnement et d’objet

| Famille | Champs minimaux |
|---|---|
| identité temporelle | date UTC, fuseau d’affichage, durée et identifiant de campagne |
| objet | commit ou build, mode debug/release, options, hash des fichiers et configuration |
| moteur et outils | versions exactes, édition, backend, plugins, extensions et paramètres |
| système | OS, version, architecture, locale, virtualisation et correctifs pertinents |
| CPU | modèle, cœurs/logiques, fréquence gouvernée, affinité si imposée |
| GPU | modèle, VRAM, pilote, API, renderer, résolution, fréquence écran et V-Sync |
| mémoire et stockage | RAM installée, type de stockage, espace libre et emplacement des données |
| énergie et thermique | profil d’alimentation, secteur/batterie, température ou état de stabilisation |
| concurrence | processus de fond, antivirus, indexation, téléchargements et services actifs |
| réseau | interface, topologie, latence injectée, perte, débit et serveur |
| contenu | scène, assets, modèle IA, quantification, seed, prompts et empreintes |
| instrumentation | profiler, capture, logs, sampling et coût connu de l’outil |

**Réponse rapide :** utiliser les manifests spécialisés du [CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md#10-manifeste-denvironnement), du [GPU](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md#10-manifeste-denvironnement-amd) ou du [chargement](../Livre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md#9-manifeste-denvironnement). Un champ inconnu reste `unknown` ou `not_recorded`, jamais une valeur supposée.

**Invalidation :** changement de build, pilote, renderer, résolution, modèle, preset, scène, dépendance ou profil d’alimentation peut empêcher une comparaison directe. L’invalidation est une règle du protocole, pas une impression après coup.

**Limite :** deux machines portant le même nom commercial peuvent différer par firmware, mémoire, refroidissement, alimentation ou charge de fond.

---

<!-- l5:card -->
## BMK-03 — Scénario, charge et fixtures

| Dimension | Contrat |
|---|---|
| état initial | sauvegarde synthétique, scène, base, cache, inventaire et paramètres reconstruisibles |
| entrées | trajet caméra, commandes, requêtes, prompt, fichier, seed ou trace rejouable |
| charge | nombre d’entités, taille des données, résolution, durée, concurrence et cadence |
| phases | initialisation, warm-up, mesure, transition, plateau, nettoyage et fin |
| oracle | résultat fonctionnel ou qualité attendue distinct de la métrique mesurée |
| stabilité | horloge, aléatoire, réseau, tâches de fond et dépendances déclarés |
| sortie | artefacts bruts, captures, statuts, erreurs et identifiant du run |
| nettoyage | état restauré ou nouvelle fixture ; aucune contamination silencieuse du run suivant |

**Réponse rapide :** une charge est une donnée versionnée, pas « refaire la même chose ». Les scénarios CPU séparent les familles de coût dans la [matrice dédiée](../Livre-IV/CHAPITRE-06-Profilage-CPU.md#11-matrice-des-scénarios), tandis que le [benchmark de scène](../Livre-IV/CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md#8-contrat-de-benchmark-de-scène) fixe population, trajet et événements.

**Diagramme compact :** `fixture → entrées rejouables → charge contrôlée → phases nommées → métrique + oracle → nettoyage`.

**Porte :** si l’oracle fonctionnel échoue, le run peut rester utile au diagnostic, mais il ne participe pas à la comparaison de performance prévue sans règle explicite.

---

<!-- l5:card -->
## BMK-04 — Warm-up, caches et états froid/chaud

| État | Définition | Usage |
|---|---|---|
| démarrage froid | aucune présence préalable supposée dans les caches du protocole | mesurer première utilisation ou installation |
| démarrage chaud | données ou pipelines déjà amorcés selon une procédure déclarée | mesurer usage répété |
| warm-up | période exécutée avant la fenêtre principale afin de stabiliser compilations, caches et allocations | exclue du résumé principal, conservée séparément |
| cache applicatif | état contrôlé par l’application ou le service | vider seulement par mécanisme supporté |
| cache système | pages, fichiers, pilotes ou services gérés par l’OS | ne pas prétendre l’effacer sans procédure vérifiée |
| cache distant | proxy, CDN, modèle, base ou service | identité, TTL et invalidation enregistrés |
| compilation différée | shader, pipeline, JIT ou graphe construit à la première utilisation | mesurer séparément si visible par le joueur |
| plateau thermique | régime où température et fréquence ne dérivent plus fortement | documenter plutôt que supposer |

**Réponse rapide :** le [warm-up et l’ordre des runs](../Livre-IV/CHAPITRE-06-Profilage-CPU.md#12-warm-up-répétitions-et-ordre-des-runs) absorbent les effets d’amorçage sans les supprimer de l’histoire. Le [chargement](../Livre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md#5-vocabulaire-opérationnel) distingue explicitement froid et chaud.

**Diagramme compact :** `état initial déclaré → warm-up observé → fenêtre mesurée → nettoyage → état suivant déclaré`.

**Limite :** un redémarrage n’est pas automatiquement un cache froid ; une suppression de cache ou un changement système peut être destructif et doit rester dans la procédure propriétaire.

---

<!-- l5:matrix -->
## Matrice B — Facteurs à contrôler, randomiser ou rapporter

| Facteur | Contrôler lorsque possible | Randomiser ou contrebalancer | Toujours rapporter |
|---|---|---|---|
| version et build | même révision hors changement étudié | non | commit, hash et mode |
| matériel | même machine pour une comparaison locale | ordre des machines dans une campagne multi-postes | modèles et capacités |
| température et fréquence | phase de stabilisation et pauses | ordre A/B si dérive attendue | état observé et politique |
| ordre des variantes | mêmes préconditions | `A-B-B-A`, blocs ou ordre aléatoire pré-déclaré | séquence réelle |
| cache | procédure froid/chaud explicite | alterner les états si la question le demande | état avant chaque run |
| scène et données | mêmes fixtures et empreintes | ordre des scénarios | identifiants et tailles |
| aléatoire | seeds enregistrées | ensemble ou ordre des seeds | seed de chaque run |
| réseau | profil injecté ou topologie stable | ordre des profils | latence, perte, débit et serveur |
| outils de capture | même instrumentation | run témoin avec/sans capture si nécessaire | outil, version et réglages |
| charge de fond | politique et fenêtre dédiées | non par défaut | écarts, interruptions et anomalies |
| opérateur | procédure écrite | opérateurs distincts pour répétition indépendante | rôle et intervention |
| heure et durée | fenêtre comparable | blocs répartis si dérive journalière | date, début, fin et pauses |

**Décision :** contrôler réduit la variabilité, randomiser réduit certains biais d’ordre, rapporter rend l’écart interprétable. Aucun choix ne garantit à lui seul une causalité.

---

<!-- l5:card -->
## BMK-05 — Runs, répétitions, ordre et arrêt

| Élément | Règle |
|---|---|
| run | exécution complète possédant un identifiant, un état initial et une sortie |
| observation | mesure élémentaire à l’intérieur d’un run ; elle ne remplace pas le nombre de runs |
| répétition | nouveau run conforme au même protocole, pas duplication d’une ligne |
| nombre | défini avant la campagne selon variabilité, coût et risque ; aucun nombre universel |
| ordre | alterné, bloqué ou randomisé selon le biais attendu |
| pause | durée et condition de reprise déclarées lorsque température, mémoire ou service dérivent |
| échec | conservé avec statut et cause connue/inconnue ; jamais remplacé par zéro |
| arrêt sécurité | température, corruption, perte de données, dépassement de quota ou erreur critique |
| arrêt statistique | seulement si méthode séquentielle pré-définie ; jamais parce que le résultat devient favorable |
| reprise | nouvelle campagne ou version de protocole si les conditions changent |

**Réponse rapide :** un appel unique est trop sensible au bruit ; le [pilote de répétitions](../Livre-IV/CHAPITRE-06-Profilage-CPU.md#18-pilote-de-répétitions) conserve les échantillons bruts et sépare warm-up et mesure. Le nombre de frames n’est pas le nombre de répétitions indépendantes.

**Limite :** augmenter artificiellement les observations d’un même run peut donner une précision trompeuse lorsque toutes partagent le même état thermique, cache ou dérive.

---

<!-- l5:card -->
## BMK-06 — Unités, horloges, précision et instrumentation

| Sujet | Règle |
|---|---|
| unité | incluse dans le nom ou le schéma : `ms`, `µs`, `bytes`, `MiB`, `GiB`, `fps`, `items/s` |
| multiples | distinguer SI et binaire ; conserver la valeur source avant conversion |
| durée | horloge monotone pour les intervalles ; horloge civile seulement pour dater |
| résolution | précision de l’outil et arrondi documentés ; ne pas afficher plus de décimales que la mesure |
| débit | numérateur, dénominateur et fenêtre explicites |
| ratio | dénominateur conservé ; division par zéro traitée comme non définie |
| FPS | convertir en temps de frame pour comparer les latences ; ne pas moyenner naïvement des FPS hétérogènes |
| mémoire | nommer compteur, portée et instant ; deux outils peuvent mesurer des périmètres différents |
| énergie | dispositif, cadence, intégration et calibration documentés |
| instrumentation | mesurer ou estimer le coût du profiler, des logs, captures et overlays |
| synchronisation | V-Sync, limite de cadence, attente CPU/GPU et sommeil déclarés |
| arrondi | appliqué à la présentation, jamais aux données brutes |

**Réponse rapide :** les [unités mémoire](../Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md#9-unités-et-conversions) rappellent qu’une conversion correcte ne rend pas deux compteurs équivalents. Pour le CPU, `16,667 ms` est un plafond théorique à 60 FPS, non une mesure du projet.

**Diagramme compact :** `source → compteur et horloge → unité native → conversion tracée → valeur brute → présentation arrondie`.

**Limite :** une mesure plus précise numériquement peut être moins exacte si l’instrumentation perturbe le système ou si la grandeur est mal définie.

---

<!-- l5:card -->
## BMK-07 — Format des données brutes et nullabilité

| Colonne ou champ | Fonction |
|---|---|
| `campaign_id` | relie protocole, environnement et décision |
| `run_id` | distingue les répétitions |
| `variant_id` | baseline, candidate ou contrôle |
| `scenario_id` | charge et fixture |
| `observation_index` | ordre dans le run |
| `phase` | warm-up, mesure, transition, plateau ou nettoyage |
| `metric_id` | identité stable de la grandeur |
| `value` | nombre brut ou valeur absente |
| `unit` | unité native |
| `status` | `measured`, `blocked`, `invalid`, `missing` ou `not_applicable` |
| `timestamp_relative` | position monotone dans le run |
| `artifact_ref` | capture, log, profiler, rapport ou fichier source |
| `notes_code` | code contrôlé ; pas de texte libre sensible par défaut |

**Réponse rapide :** le [schéma CSV CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md#19-exporter-des-échantillons-de-frame) conserve une ligne par observation et laisse les valeurs bloquées absentes. Zéro signifie une mesure égale à zéro ; il ne signifie jamais « manquant ».

**Intégrité :** schéma versionné, encodage explicite, ordre déterministe lorsque nécessaire, empreinte du fichier et manifeste des artefacts. Les corrections produisent une nouvelle version au lieu d’écraser la source.

**Limite :** un fichier bien formé peut contenir une campagne invalide ; le validateur structurel ne remplace pas les contrôles du protocole.

---

<!-- l5:card -->
## BMK-08 — Statistiques, dispersion et incertitude

| Statistique | Usage | Réserve |
|---|---|---|
| nombre `n` | taille réelle de la série analysée | distinguer observations et runs indépendants |
| moyenne | centre lorsque l’addition et la distribution la rendent pertinente | sensible aux valeurs extrêmes |
| médiane | centre robuste pour latences et distributions asymétriques | masque la largeur de la distribution |
| minimum/maximum | bornes observées | très sensibles au nombre d’observations |
| quartiles et IQR | dispersion robuste | ne décrivent pas entièrement les queues |
| écart-type | dispersion autour de la moyenne | interprétation fragile si distribution très asymétrique |
| p90/p95/p99 | queues et expérience des cas lents | définition et méthode d’interpolation nécessaires |
| taux de dépassement | fréquence au-dessus d’un budget | conserver numérateur et dénominateur |
| intervalle d’incertitude | variabilité de l’estimation selon une méthode déclarée | ne transforme pas l’échantillon en population universelle |
| distribution par run | variabilité entre répétitions | ne pas agréger toutes les frames comme indépendantes |
| tendance temporelle | dérive, chauffe, fuite ou cache | exige ordre et temps conservés |

**Réponse rapide :** conserver plusieurs distributions, comme l’exige le [profilage CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md#8-mesurer-plusieurs-distributions-pas-un-seul-nombre). Le script propriétaire d’[analyse des distributions](../Livre-IV/CHAPITRE-06-Profilage-CPU.md#20-analyser-les-distributions) illustre médiane, p95, p99 et dépassements sans supprimer les pics.

**Diagramme compact :** `observations par run → résumé de chaque run → comparaison entre runs → incertitude → conclusion bornée`.

**Limite :** aucune statistique unique n’est obligatoire pour toutes les grandeurs. Le choix dépend de la décision, de la distribution, du coût des queues et de l’unité d’indépendance.

---

<!-- l5:card -->
## BMK-09 — Valeurs aberrantes, données manquantes et exclusions

| Situation | Traitement |
|---|---|
| run interrompu | conserver le run et le statut ; exclure seulement selon la règle pré-définie |
| valeur impossible | marquer `invalid`, conserver la source et enquêter sur le compteur |
| valeur absente | `missing` ou `blocked`, jamais zéro |
| pic valide | conserver dans la distribution et l’analyser comme expérience réelle |
| violation de protocole | documenter le facteur, exclure de la comparaison principale et garder en annexe |
| erreur d’instrumentation | conserver l’artefact, qualifier l’impact et répéter |
| résultat extrême sans cause connue | ne pas supprimer ; comparer analyses inclusive et justifiée si prévu |
| changement d’environnement | séparer la campagne ou introduire un bloc explicite |
| données dupliquées | retirer seulement après preuve d’identité et conserver le journal de correction |
| sélection postérieure | étiqueter exploratoire et lancer une confirmation indépendante |

**Réponse rapide :** une valeur aberrante est une observation à expliquer, pas un nombre gênant. L’exclusion doit être fondée sur le protocole ou une erreur démontrée, puis signalée avec le nombre de lignes concernées et l’effet sur le résultat.

**Porte :** publier au minimum le résumé avec toutes les observations valides, les exclusions motivées, le décompte des statuts et la sensibilité de la conclusion.

**Limite :** une méthode automatique d’outlier peut retirer précisément les pics qui constituent le risque produit ; elle n’a pas d’autorité décisionnelle seule.

---

<!-- l5:card -->
## BMK-10 — Comparaison, effet et signification pratique

| Calcul | Définition | Condition |
|---|---|---|
| différence absolue | `candidate − baseline` dans l’unité native | direction favorable explicitée |
| variation relative | `(candidate − baseline) / baseline × 100 %` | baseline non nulle et ratio pertinent |
| speedup | `baseline / candidate` pour une durée où plus petit est meilleur | mêmes unités et travail équivalent |
| écart au budget | valeur moins seuil ou taux de dépassement | budget qualifié pour la plateforme |
| effet par run | paire candidate/baseline selon bloc ou seed | appariement défini avant analyse |
| effet pratique | écart comparé au seuil qui change le produit | seuil décidé avant lecture |
| qualité | différence visuelle, sonore, fonctionnelle ou métier | oracle ou revue séparée |
| coût total | performance, mémoire, complexité, maintenance et réversibilité | aucune dimension masquée |

**Réponse rapide :** une baisse numérique n’est pas suffisante. La boucle CPU exige une [baseline et une candidate comparables](../Livre-IV/CHAPITRE-06-Profilage-CPU.md#14-capturer-une-baseline), la boucle GPU ajoute un contrôle visuel, et les systèmes exigent tests fonctionnels et revue de lisibilité.

**Diagramme compact :** `effet mesuré + incertitude + seuil pratique + portes qualité → adopter / conserver / répéter / indéterminé`.

**Interdictions :** ne pas comparer des moyennes provenant de scénarios différents ; ne pas annoncer `x % plus rapide` lorsque la baseline est nulle ou change de travail ; ne pas confondre absence de différence détectée et équivalence.

---

<!-- l5:card -->
## BMK-11 — Visualisation, rapport et séparation des couches

| Couche | Contenu | Autorité |
|---|---|---|
| protocole | question, métriques, environnement, plan et portes | définit la campagne |
| données brutes | observations, statuts, ordre, artefacts et empreintes | preuve consultable |
| transformation | filtres, conversions, agrégations et version du script | calcul reproductible |
| tableaux | nombres avec unités, `n`, dispersion et exclusions | résumé |
| graphiques | distribution, série temporelle, comparaison et budget | aide à la lecture |
| interprétation | mécanismes possibles, limites et hypothèses restantes | analyse humaine |
| décision | accepter, rejeter, répéter, déroger ou retirer | propriétaire nommé |
| archivage | versions, durée de validité, dépendances et invalidation | maintenance |

**Réponse rapide :** un graphique ne remplace ni les données ni la méthode. Axe tronqué, échelle logarithmique, lissage, agrégation et plage doivent être visibles ; la légende nomme unités, variantes, nombre de runs et environnement.

**Rapport minimal :** résumé exécutif borné, question, protocole, écarts au protocole, résultats bruts accessibles, statistiques prévues, contrôles fonctionnels/qualité, décision, réserves et prochaine mesure.

**Limite :** une visualisation peut révéler une tendance exploratoire ; elle ne modifie pas rétroactivement la métrique primaire.

---

<!-- l5:matrix -->
## Matrice C — Niveaux de preuve et déclarations permises

| Niveau | Preuve disponible | Déclaration permise | Déclaration interdite |
|---|---|---|---|
| protocole revu | contrat, schéma et sources relus | méthode prête à matérialiser | performance réelle |
| outil qualifié statiquement | interface, version et sortie attendue | capacité documentaire | précision ou coût runtime |
| run isolé | un environnement et des données brutes | observation de ce run | tendance stable |
| série locale | répétitions conformes sur un poste | distribution locale datée | généralisation matérielle |
| comparaison locale | baseline/candidate comparables et portes satisfaites | effet sur ce protocole | causalité universelle |
| campagne multi-scénarios | scénarios et populations déclarés | portée élargie aux cas testés | couverture des cas absents |
| répétition indépendante | autre opérateur ou environnement selon le contrat | reproductibilité observée et hétérogénéité | identité parfaite attendue |
| qualification plateforme | matériel, build, qualité et seuils approuvés | budget pour la plateforme nommée | support d’une autre plateforme |
| décision produit | preuves, risques, réserves et propriétaire | adoption dans le périmètre décidé | vérité permanente |
| résultat déprécié | dépendance, version ou protocole changé | usage historique et comparaison prudente | recommandation actuelle |

**Décision :** le niveau le plus faible encore ouvert borne l’affirmation. `Non mesuré`, `indéterminé` et `non comparable` sont des résultats honnêtes, non des échecs à maquiller.

---

<!-- l5:card -->
## BMK-12 — Répétition indépendante, maintenance et retrait

| Événement | Action |
|---|---|
| nouvelle version d’outil ou moteur | répéter ou marquer le résultat historique |
| changement matériel, pilote ou OS | créer un environnement distinct |
| modification du scénario ou des fixtures | versionner le protocole et ne pas fusionner silencieusement les séries |
| changement de métrique ou méthode de percentile | recalcul versionné ou nouvelle campagne |
| correction du script d’analyse | conserver ancien résultat, diff et motif |
| nouvelle plateforme | qualifier séparément |
| dérive thermique, réseau ou service | ajouter bloc, répéter et rapporter l’hétérogénéité |
| répétition indépendante divergente | comparer environnements avant de choisir un « bon » résultat |
| artefact manquant ou empreinte invalide | retirer la déclaration jusqu’à restauration de la preuve |
| résultat dépassé | marquer `superseded` avec successeur |
| risque ou coût excessif | arrêter la campagne et conserver le statut |
| retrait | conserver identité, date, raison et dernière portée autorisée |

**Réponse rapide :** la répétition indépendante suit le même protocole sans dépendre d’une explication orale cachée. Elle cherche une conclusion compatible, pas des nombres identiques. Les écarts entre postes ou opérateurs deviennent des données de portée.

**Diagramme compact :** `résultat daté → changement détecté → validité réévaluée → répéter / déprécier / remplacer / retirer`.

**Profil Solo :** un poste, peu de scénarios, données brutes lisibles, protocole court et répétition différée suffisent pour une décision locale honnête.

**Profil Studio :** registre de campagnes, environnements nommés, scripts verrouillés, artefacts, revues indépendantes, campagnes multi-plateformes, dérogations et dates d’expiration.

**Limite :** les scripts exécutables, fixtures et jeux de données permanents appartiennent au Companion Pack. Cette fiche définit leurs contrats sans prétendre les matérialiser.

---

## Sources propriétaires et limites

- [Livre IV, chapitre 1 — Équilibrage et télémétrie locale](../Livre-IV/CHAPITRE-01-Equilibrage-et-telemetrie-locale.md)
- [Livre IV, chapitre 2 — Stratégie générale d’assurance qualité](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md)
- [Livre IV, chapitre 3 — Tests fonctionnels et tests de régression](../Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md)
- [Livre IV, chapitre 4 — Débogage et reproduction des anomalies](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md)
- [Livre IV, chapitre 5 — Journalisation et observabilité locale](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md)
- [Livre IV, chapitre 6 — Profilage CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md)
- [Livre IV, chapitre 7 — Profilage GPU et optimisation du rendu](../Livre-IV/CHAPITRE-07-Profilage-GPU-et-optimisation-du-rendu.md)
- [Livre IV, chapitre 8 — Optimisation RAM, VRAM et allocations](../Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md)
- [Livre IV, chapitre 9 — Chargements, streaming et gestion des ressources](../Livre-IV/CHAPITRE-09-Chargements-streaming-et-gestion-des-ressources.md)
- [Livre IV, chapitre 10 — Optimisation des scènes, scripts et systèmes de jeu](../Livre-IV/CHAPITRE-10-Optimisation-des-scenes-scripts-et-systemes-de-jeu.md)
- [Livre IV, chapitre 12 — Synchronisation, autorité et prédiction](../Livre-IV/CHAPITRE-12-Synchronisation-autorite-et-prediction.md)
- [Livre IV, chapitre 14 — DevOps et intégration continue](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md)
- [Livre V, fiche 18 — Référence graphique et 3D](CHAPITRE-18-Reference-graphique-et-3D.md)
- [Livre V, fiche 19 — Référence audio](CHAPITRE-19-Reference-audio.md)
- [Livre V, fiche 20 — Catalogue des erreurs et diagnostics](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md)

**Niveau de preuve de cette fiche :** `static-review`. Les contrats et liens sont relus contre les sources du dépôt. Aucun benchmark CPU, GPU, RAM, VRAM, chargement, gameplay, réseau, CI, asset, audio ou modèle IA n’a été exécuté ; aucun script, fixture, profiler, capture, série, statistique, comparaison, décision produit, donnée utilisateur ou PDF n’a été produit.

## Synthèse de consultation

Commencer par la décision et la métrique primaire ; figer ensuite l’objet, l’environnement, le scénario, les états de cache et le plan de répétitions ; conserver chaque observation brute avec son statut ; calculer des résumés adaptés à la distribution ; comparer l’effet au seuil pratique et aux portes fonctionnelles ou qualitatives ; enfin dater, borner, répéter et retirer le résultat lorsque son contexte change.
