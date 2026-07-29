---
title: "Livre V — Fiche 16 : Patrons d’architecture"
id: "DOC-L5-CH16"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 16
last-verified: "2026-07-29T06:49:56+02:00"
audit-status: "complete"
audit-date: "2026-07-29T06:49:56+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-16.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "architecture-patterns-reference"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Patrons d’architecture

> **Type de document :** cartes de patrons, matrices de décision, diagrammes compacts, anti-patterns et portes de validation.
> **Référence projet :** Godot `4.7.1-stable`, édition Standard, GDScript et architecture feature-first de `Project Asteria`.
> **Principe :** un patron nomme un compromis récurrent. Il ne remplace ni le problème concret, ni la mesure, ni la propriété d’état, ni une décision documentée.

## Index express

| Besoin | Ouvrir |
|---|---|
| définir le contrat architectural | [ARC-00](#arc-00--contrat-dun-patron-architectural) |
| choisir un patron selon le problème | [Matrice A](#matrice-a--sélection-par-problème) |
| poser modules, couches et dépendances | [ARC-01](#arc-01--frontières-modules-et-direction-des-dépendances) |
| assembler les implémentations | [ARC-02](#arc-02--composition-root-et-injection-explicite) |
| choisir scène, `Node`, `RefCounted`, `Resource` ou Autoload | [Matrice B](#matrice-b--support-et-durée-de-vie) |
| préférer composition ou héritage | [ARC-03](#arc-03--composition-avant-héritage) |
| orchestrer un cas d’usage | [ARC-04](#arc-04--service-dapplication-commandes-et-requêtes) |
| isoler l’accès aux données | [ARC-05](#arc-05--repository-et-unité-de-travail) |
| isoler moteur, addon ou service externe | [ARC-06](#arc-06--ports-adaptateurs-et-couche-anti-corruption) |
| choisir appel, signal ou bus | [ARC-07](#arc-07--appels-signaux-événements-et-médiation) |
| attribuer état et cycle de vie | [ARC-08](#arc-08--propriété-détat-et-cycle-de-vie) |
| réduire une interface publique | [ARC-09](#arc-09--façade-de-module-et-contrat-public) |
| varier un comportement | [ARC-10](#arc-10--stratégie-fabrique-et-registre-borné) |
| tester les frontières | [ARC-11](#arc-11--coutures-de-test-et-tests-de-contrat) |
| comparer conséquences et preuves | [Matrice C](#matrice-c--conséquences-et-portes-de-validation) |
| diagnostiquer et accepter | [ARC-12](#arc-12--anti-patterns-diagnostics-et-acceptation) |

---

<!-- l5:card -->
## ARC-00 — Contrat d’un patron architectural

| Champ | Question obligatoire |
|---|---|
| problème | quelle difficulté répétée doit être résolue |
| contexte | quelles contraintes rendent le patron pertinent |
| forces | simplicité, testabilité, performance, autonomie, sécurité ou exploitation |
| structure | quelles responsabilités et relations sont introduites |
| autorité | quel composant peut accepter ou refuser une mutation |
| dépendances | qui connaît quel contrat ou détail concret |
| état | où vit l’état mutable et qui contrôle son cycle |
| communication | appel, retour, signal, événement, message ou stockage |
| erreurs | comment l’échec est signalé, compensé ou journalisé |
| preuve | quel test, graphe, fixture ou mesure confirme la propriété recherchée |
| conséquences | coût cognitif, indirection, fichiers, latence et maintenance |
| alternatives | option plus simple ou plus spécialisée |
| sortie | condition de retrait ou de remplacement du patron |

**Réponse rapide :** partir du [vocabulaire architectural](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#4-vocabulaire-architectural), puis vérifier le [périmètre des services et dépendances](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md#3-périmètre-et-frontières). Une carte ne doit pas convertir un nom célèbre en dépendance obligatoire.

**Diagramme compact :** `problème observé → forces explicites → patron minimal → conséquences mesurées → décision conservée ou retirée`.

---

<!-- l5:matrix -->
## Matrice A — Sélection par problème

| Problème dominant | Patron de départ | À éviter | Source propriétaire |
|---|---|---|---|
| objets concrets dispersés | composition root | création cachée dans chaque scène | [point de composition](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md#10-construire-le-point-de-composition) |
| dépendance difficile à remplacer | injection explicite | accès global ou recherche arbitraire | [formes d’injection](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md#6-les-trois-formes-dinjection-de-dépendances) |
| variante de comportement | stratégie ou objet composé | hiérarchie profonde | [préférer la composition](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#54-préférer-la-composition) |
| cas d’usage multi-étapes | service d’application | logique métier dans l’UI | [couche application](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#102-application) |
| stockage concret envahissant | repository | SQL, chemin ou API dans le domaine | [repository](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md#45-repository) |
| dépendance technique remplaçable | port et adaptateur | type tiers dans tous les modules | [direction des dépendances](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#53-dépendre-vers-les-règles-pas-vers-les-détails) |
| notification locale | signal direct | bus global | [bus limité](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md#7-créer-un-bus-dévénements-limité-et-typé) |
| événement transversal rare | médiateur ou bus typé | dictionnaire générique d’événements | [événement, commande et état](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md#72-événement-commande-et-état) |
| interface de module trop large | façade | accès aux chemins internes | [frontière](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#48-frontière) |
| état dupliqué | propriétaire unique + vues dérivées | synchronisation bidirectionnelle implicite | [carte des autorités](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#4-carte-des-autorités-de-project-asteria) |
| changement atomique multi-autorités | unité de travail bornée | « transaction universelle » | [invariants non négociables](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#2-frontières-et-invariants-non-négociables) |
| intégration tierce instable | couche anti-corruption | vocabulaire externe dans le domaine | [séparation production/runtime](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md) |

**Décision :** commencer par l’appel direct, la composition locale et une interface courte. Ajouter une indirection uniquement lorsqu’elle protège une frontière, une variante, une durée de vie ou une preuve de test.

---

<!-- l5:card -->
## ARC-01 — Frontières, modules et direction des dépendances

| Élément | Contrat |
|---|---|
| module | capacité cohérente, données contrôlées, interface publique et validation |
| domaine | règles et décisions métier, sans scène, stockage concret ou protocole |
| application | orchestre une intention et les autorités concernées |
| présentation | adapte entrée, scène, UI et feedback |
| données | contenus de conception validés et versionnés |
| infrastructure | fichiers, SQLite, réseau, IA et adaptateurs concrets |
| outils | génération, import, audit et opérations hors runtime |
| composition | connaît les implémentations concrètes et les relie |
| dépendance | pointe vers une règle ou un contrat plus stable |

**Diagramme compact :** `Présentation → Application → Domaine ← Port ← Infrastructure`; `Composition → toutes les implémentations nécessaires au démarrage`.

La [structure feature-first](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#51-organiser-dabord-par-fonctionnalité) rapproche les fichiers d’une capacité. Les [règles de dépendances Solo/Studio](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#6-règles-de-dépendances) gardent `core` indépendant des fonctionnalités et réservent la connaissance des détails à la composition.

**Limite :** un module de trois fichiers n’a pas besoin de six couches physiques. La séparation conceptuelle précède la création de dossiers.

---

<!-- l5:card -->
## ARC-02 — Composition root et injection explicite

| Responsabilité du point de composition | Contrôle |
|---|---|
| créer | instancier les adaptateurs et services concrets |
| configurer | fournir chaque dépendance obligatoire |
| relier | connecter les événements transversaux documentés |
| démarrer | respecter l’ordre topologique des dépendances |
| exposer | transmettre des façades ou contrats, pas le conteneur entier |
| arrêter | suivre l’ordre inverse et libérer les ressources |
| diagnostiquer | refuser doublon, type inattendu et dépendance absente |

**Diagramme compact :** `AppBootstrap → crée RepositorySQLite + EventBus → injecte InventoryService → configure InventoryPanel`.

L’injection peut passer par constructeur, méthode de configuration ou propriété explicite. Le [registre minimal](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md#8-construire-un-registre-de-services-minimal) reste limité au bootstrap ; s’il est injecté partout, il devient un Service Locator et cache à nouveau les dépendances. Martin Fowler distingue également [Dependency Injection et Service Locator](https://martinfowler.com/articles/injection.html).

**Exemple Asteria :** `AppBootstrap` choisit `SQLiteInventoryRepository` pour l’application réelle et `InMemoryInventoryRepository` pour une fixture. `InventoryService` ne change pas.

---

<!-- l5:matrix -->
## Matrice B — Support et durée de vie

| Support | Choisir lorsque | Éviter lorsque | Propriétaire naturel |
|---|---|---|---|
| scène composée | structure visuelle ou ensemble réutilisable de nœuds | logique sans présence dans l’arbre | parent ou scène racine |
| `Node` | notifications, enfants, `_process`, arbre distant ou durée de scène | simple calcul pur | parent, scène ou Autoload |
| `RefCounted` | logique injectée sans présence dans le `SceneTree` | durée liée à un parent visuel | références explicites |
| `Resource` | donnée sérialisable, profil ou configuration | service global mutable | fichier, scène ou propriétaire de contenu |
| Autoload | état ou service réellement global à toute la session | commodité d’accès | racine du `SceneTree` |
| objet Python | outil, conversion ou automatisation hors export Godot | boucle gameplay autoritaire | processus d’outil |
| processus compagnon | dépendance native ou IA isolée | appel local trivial | superviseur applicatif |
| service réseau | partage entre processus ou machines | besoin hors ligne essentiel | plateforme et exploitation |

La [sélection de type Godot](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md#5-choisir-le-bon-type-godot) rappelle que `Resource` porte d’abord des données. La documentation Godot distingue aussi [Nodes et Resources](https://docs.godotengine.org/en/4.7/tutorials/scripting/resources.html) et expose les coûts de l’[accès global par Autoload](https://docs.godotengine.org/en/4.7/tutorials/best_practices/autoloads_versus_regular_nodes.html).

---

<!-- l5:card -->
## ARC-03 — Composition avant héritage

| Question | Composition | Héritage |
|---|---|---|
| relation | « possède/utilise » | « est une spécialisation de » |
| variation | remplacer un collaborateur | redéfinir un comportement hérité |
| dépendances | visibles par propriétés ou constructeur | souvent dispersées dans la hiérarchie |
| test | double injecté localement | sous-classe ou état ancestral à préparer |
| risque | trop de petits objets | profondeur, fragile base class et effets latéraux |

**Patron :** une scène racine compose mouvement, santé, interaction et présentation ; chaque composant garde une responsabilité et une durée de vie claire. Une classe de base reste pertinente lorsqu’elle définit réellement une famille substituable et un invariant partagé.

**Diagnostic :** si une variante doit désactiver la moitié de son parent, tester le type concret à plusieurs endroits ou connaître cinq niveaux d’ancêtres, préférer une stratégie ou un composant.

Godot présente la [composition de scènes et les relations faiblement couplées](https://docs.godotengine.org/en/4.7/tutorials/best_practices/scene_organization.html). La fiche 17 possède les patrons de gameplay spécialisés ; cette carte ne définit pas leurs machines à états ou capacités.

---

<!-- l5:card -->
## ARC-04 — Service d’application, commandes et requêtes

| Notion | Rôle | Retour attendu |
|---|---|---|
| commande | demande une mutation | succès, refus ou erreur typée |
| requête | demande une vue sans mutation | résultat ou absence explicite |
| service d’application | orchestre règles, ports et transaction | résultat du cas d’usage |
| événement | annonce un fait déjà accepté | identité, révision et données minimales |
| contrôleur | traduit entrée ou UI en commande/requête | aucune décision métier nouvelle |

**Diagramme compact :** `Entrée → Contrôleur → Commande → Service applicatif → Autorité → Commit → Événement → Présentation`.

**Exemple Asteria :** `TransferItemCommand` contient les identifiants source, destination, item et quantité. `InventoryTransferService` valide les inventaires, prépare le transfert, committe, puis publie `item_transferred`. L’interface n’écrit jamais directement dans un tableau d’objets.

**Limite :** séparer commandes et requêtes ne signifie pas déployer deux bases ou adopter CQRS complet. La complexité doit répondre à un besoin mesuré.

---

<!-- l5:card -->
## ARC-05 — Repository et unité de travail

| Élément | Contrat |
|---|---|
| repository | charger, rechercher et persister selon le vocabulaire du domaine |
| implémentation | SQLite, fichier, mémoire, API ou cache |
| mapping | convertir types persistés et objets du domaine |
| transaction | borner l’écriture d’une autorité |
| unité de travail | coordonner plusieurs écritures explicitement compatibles |
| fixture mémoire | substitut de test respectant le même contrat observable |
| erreur | distinguer absence, conflit, corruption et panne technique |

Le repository crée une séparation entre domaine et stockage ; la définition historique est résumée par [Martin Fowler — Repository](https://martinfowler.com/eaaCatalog/repository.html). Les schémas, transactions et migrations restent propriétaires de la [fiche SQLite](CHAPITRE-14-Schemas-SQLite-et-migrations.md#sql-00--contrat-dune-base) et du [chapitre d’intégration SQLite](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md).

**Anti-pattern :** un repository générique `save(anything)` détruit le vocabulaire, les invariants et les erreurs utiles. Préférer des opérations nommées selon l’autorité.

**Réserve :** une unité de travail ne promet pas une atomicité magique entre SQLite, fichier, réseau et service distant. Elle documente préparation, ordre, compensation et preuve de chaque frontière.

---

<!-- l5:card -->
## ARC-06 — Ports, adaptateurs et couche anti-corruption

| Élément | Position |
|---|---|
| port entrant | commande ou cas d’usage offert à la présentation |
| port sortant | besoin du domaine ou de l’application envers une technologie |
| adaptateur entrant | scène, UI, CLI, HTTP ou message converti en intention |
| adaptateur sortant | SQLite, fichier, Qdrant, service IA ou addon Godot |
| anti-corruption | traduction de vocabulaire, types, erreurs et versions externes |
| contrat de capacité | fonctions disponibles, limites, version et repli |

**Diagramme compact :** `Godot/UI → port entrant → application → port sortant ← adaptateur SQLite/IA/addon`.

Les [protocoles Godot–service](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md) et les [contrats HTTP/WebSocket](../Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md) sont des exemples de frontières où l’adaptateur absorbe transport, délais et codes d’erreur. La [fiche vectorielle](CHAPITRE-15-Bases-vectorielles-et-recherche-semantique.md#vec-00--contrat-dun-index-vectoriel) conserve Qdrant, Faiss ou Chroma hors du domaine.

**Exemple Asteria :** un adaptateur transforme la réponse d’un modèle local en `KnowledgeSuggestion`; le domaine décide encore si cette suggestion peut devenir une action.

---

<!-- l5:card -->
## ARC-07 — Appels, signaux, événements et médiation

| Forme | Usage | Couplage | Risque |
|---|---|---|---|
| appel direct | demander une action locale et obtenir un retour | explicite | chaîne synchrone longue |
| signal direct | notifier parent ou collaborateur connu | faible et local | connexion oubliée |
| médiateur | relier plusieurs pairs dans un contexte borné | centralisé localement | médiateur trop intelligent |
| bus typé | événement transversal rare | émetteur découplé des observateurs | flux invisible et ordre implicite |
| file durable | travail différé, reprise ou autre processus | contrat de message | duplication et cohérence |

**Règle :** une commande demande ; un événement constate ; un état dure. Un bus ne remplace ni un retour de fonction, ni un service d’application, ni une base de données.

**Diagramme compact :** `Service → commit réussi → EventBus.emit(fait) → observateurs`; jamais `UI → événement générique → mutation inconnue`.

La documentation du [bus limité et typé](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md#7-créer-un-bus-dévénements-limité-et-typé) distingue signal local et événement transversal. Martin Fowler distingue plusieurs sens d’« event-driven » dans [What do you mean by “Event-Driven”?](https://martinfowler.com/articles/201701-event-driven.html).

---

<!-- l5:card -->
## ARC-08 — Propriété d’état et cycle de vie

| Question | Décision |
|---|---|
| propriétaire | un seul composant accepte les mutations de l’état |
| vues | copies dérivées, snapshots ou projections en lecture |
| durée | frame, scène, session, partie, installation ou service |
| création | valeurs initiales et dépendances obligatoires |
| démarrage | ressources ouvertes et abonnements actifs |
| arrêt | abonnements retirés, écritures terminées et ressources libérées |
| persistance | format, version, migration et restauration |
| invalidation | événement, révision ou expiration explicite |

**Diagramme compact :** `CREATED → CONFIGURED → STARTED → STOPPED`; une branche `FAILED` doit conserver cause et état nettoyable.

Le [cycle de vie des services](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md#9-définir-le-cycle-de-vie-des-services) démarre les dépendances avant leurs consommateurs et les arrête en ordre inverse. Les sauvegardes restent au [chapitre 9](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md), pas dans un singleton d’état global.

**Frontière avec la fiche 17 :** cette carte attribue la propriété et la durée de l’état ; elle ne définit pas la machine à états d’un personnage ou d’un système de gameplay.

---

<!-- l5:card -->
## ARC-09 — Façade de module et contrat public

| Interface publique | Détail interne |
|---|---|
| commandes et requêtes stables | nœuds enfants et chemins de scène |
| événements documentés | signaux de travail internes |
| types et identifiants du domaine | tables, fichiers et payloads techniques |
| résultat et erreurs nommées | exceptions ou codes tiers bruts |
| version et capacités | ordre d’initialisation interne |

Une façade publie le minimum nécessaire à un consommateur. Elle ne devient pas un « super service » qui centralise toutes les décisions du module.

**Exemple Asteria :** `InventoryModule` expose `transfer_item()`, `get_container_view()` et `item_transferred`; il ne publie ni le chemin de sa table SQLite, ni sa scène de panneau, ni son dictionnaire mutable.

Le README local décrit responsabilité, données contrôlées, dépendances autorisées et validation. Les [frontières du chapitre 4](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#48-frontière) et la [visibilité des dépendances](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#55-garder-les-dépendances-visibles) restent propriétaires du tutoriel complet.

---

<!-- l5:card -->
## ARC-10 — Stratégie, fabrique et registre borné

| Patron | Problème | Garde-fou |
|---|---|---|
| stratégie | plusieurs algorithmes derrière le même rôle | contrat observable commun |
| fabrique | création complexe ou dépendante d’une configuration | rester au bord ou à la composition |
| registre borné | ensemble nommé de handlers ou capacités | propriétaires, doublons et fermeture documentés |
| table de dispatch | choix déterministe par type ou identifiant | aucune exécution arbitraire par chaîne externe |
| plugin | extension activable sans modifier le cœur | manifeste, version, licence et permissions |

**Exemple Asteria :** une stratégie de recherche choisit `LexicalSearch` ou `VectorSearch` derrière `KnowledgeSearch`; la fabrique lit une configuration validée ; le domaine ne connaît ni Qdrant ni le modèle.

**Anti-pattern :** un registre global d’objets hétérogènes accessible depuis tout le projet recrée un Service Locator. Un plugin chargé dynamiquement n’obtient pas automatiquement les droits de modifier chaque autorité.

Les dépendances tierces restent soumises aux contrats de [sécurité et séparation runtime](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md) et aux décisions Solo/Studio du [chapitre 30](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md).

---

<!-- l5:card -->
## ARC-11 — Coutures de test et tests de contrat

| Preuve | Propriété vérifiée |
|---|---|
| test unitaire | règle pure ou stratégie isolée |
| fixture mémoire | service indépendant du stockage concret |
| test de contrat | plusieurs adaptateurs respectent la même interface observable |
| test de composant | module réel avec adaptateurs bornés |
| test d’intégration | frontière SQLite, fichier, réseau ou addon |
| graphe de dépendances | absence de cycle et direction autorisée |
| test de cycle de vie | ordre de démarrage, échec et arrêt inverse |
| test d’événement | publication après commit et payload minimal |
| test de sécurité | droits dérivés d’une politique fiable |
| snapshot de diagnostic | structure du bootstrap sans devenir oracle métier |

**Patron :** tester d’abord le domaine sans Godot, puis le service avec doubles, ensuite l’adaptateur réel, enfin le point de composition. Une substitution n’est valide que si elle respecte les erreurs, l’ordre et les effets observables du contrat.

Les suites exécutables restent au [chapitre 27](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md), les journaux au [chapitre 28](../Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md) et les campagnes comparatives à la fiche 21. Le Livre V indexe les coutures ; il ne duplique pas les procédures.

---

<!-- l5:matrix -->
## Matrice C — Conséquences et portes de validation

| Patron | Gain attendu | Coût accepté | Porte minimale | Signal de retrait |
|---|---|---|---|---|
| module feature-first | cohésion et découverte | arborescence locale | dépendances autorisées lisibles | module sans responsabilité propre |
| composition root | création et cycle visibles | bootstrap plus explicite | démarrage/arrêt déterministes | logique métier dans le bootstrap |
| injection | substitution et test | paramètres supplémentaires | dépendance absente refusée | objet n’a aucune variante ni test |
| composition | variantes locales | plus d’objets | composant remplaçable | délégation sans bénéfice |
| service d’application | orchestration hors UI | type par cas d’usage | règle métier toujours propriétaire | service devenu « manager » global |
| repository | stockage remplaçable | mapping et contrat | fixture + adaptateur réel conformes | simple lecture de fichier sans domaine |
| port/adaptateur | technologie isolée | traduction supplémentaire | erreur tierce convertie | contrat copie exactement l’API tierce |
| bus typé | observateurs indépendants | traçage et ordre | événement après succès | un seul récepteur local stable |
| façade | interface courte | couche supplémentaire | aucun accès interne externe | façade retransmet tout sans filtrer |
| stratégie | variation contrôlée | protocole commun | mêmes fixtures sur chaque stratégie | une seule implémentation durable |
| unité de travail | coordination explicite | préparation/compensation | aucun succès partiel silencieux | ressources sans transaction compatible |
| anti-corruption | domaine protégé | mapping et version | tests de traduction | vocabulaire externe déjà canonique |

Le critère n’est pas le nombre de patrons. Une architecture acceptable minimise les concepts tout en rendant visibles autorité, dépendances, état, durée de vie, erreurs et preuves.

---

<!-- l5:card -->
## ARC-12 — Anti-patterns, diagnostics et acceptation

| Symptôme | Anti-pattern probable | Vérification | Correction minimale |
|---|---|---|---|
| tout appelle `Global` | état global / Service Locator | rechercher accès implicites | injecter un contrat depuis la composition |
| `GameManager` connaît tous les systèmes | God object | compter responsabilités et autorités | scinder par capacités propriétaires |
| domaine importe scène ou SQLite | dépendance inversée | graphe d’imports | introduire un port sortant |
| bus contient commandes, état et dictionnaires | bus universel | inventorier événements et consommateurs | appel direct, service ou signaux typés |
| même état mutable dans UI et domaine | double autorité | tracer chaque écriture | propriétaire unique + vue dérivée |
| repository expose tables et SQL | fuite d’infrastructure | lire l’interface publique | opérations nommées selon le domaine |
| chaque classe possède une interface vide | abstraction spéculative | compter implémentations et substitutions | retirer jusqu’au besoin réel |
| hiérarchie nécessite des tests de type | héritage fragile | relever branches `is`/casts | composer stratégies ou composants |
| bootstrap décide les règles métier | composition envahissante | comparer orchestration et validation | déplacer la règle dans l’autorité |
| plugin peut modifier tout le jeu | frontière absente | inspecter permissions et ports | capacités minimales et validation |
| test ne fonctionne qu’avec la scène principale | dépendance cachée | exécuter fixture isolée | fournir doubles et point de composition de test |
| architecture décrite seulement dans un diagramme | documentation non exécutable | comparer graphe réel et document | ajouter contrôles de dépendances et contrats |

**Portes d’acceptation :**

1. chaque mutation possède une autorité nommée ;
2. le graphe de dépendances respecte la direction déclarée ;
3. les dépendances obligatoires sont visibles au point de création ;
4. le domaine ne connaît aucun stockage, scène, addon ou protocole concret ;
5. l’état mutable possède un propriétaire et une durée de vie ;
6. les événements sont typés, rares et publiés après succès ;
7. les adaptateurs convertissent types et erreurs externes ;
8. au moins une fixture remplace chaque dépendance réellement variable ;
9. la solution Solo reste plus simple que la solution Studio lorsque les contraintes le permettent ;
10. toute indirection sans preuve, variante ou frontière peut être supprimée.

La stratégie QA relève du [Livre IV, chapitre 2](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md), le diagnostic du [Livre IV, chapitre 4](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md), l’observabilité du [Livre IV, chapitre 5](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md) et la CI du [Livre IV, chapitre 14](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md).

## Sources et frontières

- [Godot 4.7 — Project organization](https://docs.godotengine.org/en/4.7/tutorials/best_practices/project_organization.html)
- [Godot 4.7 — Scene organization](https://docs.godotengine.org/en/4.7/tutorials/best_practices/scene_organization.html)
- [Godot 4.7 — Autoloads versus regular nodes](https://docs.godotengine.org/en/4.7/tutorials/best_practices/autoloads_versus_regular_nodes.html)
- [Godot 4.7 — Resources](https://docs.godotengine.org/en/4.7/tutorials/scripting/resources.html)
- [Martin Fowler — Dependency Injection](https://martinfowler.com/articles/injection.html)
- [Martin Fowler — Repository](https://martinfowler.com/eaaCatalog/repository.html)
- [Martin Fowler — What do you mean by “Event-Driven”?](https://martinfowler.com/articles/201701-event-driven.html)

Les patrons de gameplay restent à la fiche 17. Les exemples exécutables permanents, graphes de dépendances, doubles, adaptateurs, scènes de bootstrap et tests de contrat appartiennent au Companion Pack. Aucun runtime Godot, addon, base, service réseau ou système de gameplay n’est prétendu exécuté par cette fiche.