---
title: "Livre V — Fiche 17 : Patrons de gameplay"
id: "DOC-L5-CH17"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 17
last-verified: "2026-07-29T10:21:00+02:00"
audit-status: "complete"
audit-date: "2026-07-29T10:21:00+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-17.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "gameplay-patterns-reference"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Patrons de gameplay

> **Type de document :** cartes de patrons, matrices de décision, diagrammes compacts, diagnostics et portes de validation.
> **Référence projet :** Godot `4.7.1-stable`, GDScript et systèmes propriétaires de `Project Asteria`.
> **Principe :** un patron de gameplay organise une famille de décisions répétées. Il ne transfère jamais l’autorité d’un système vers l’interface, l’animation, l’agent, la scène ou une définition de contenu.

## Index express

| Besoin | Ouvrir |
|---|---|
| définir le contrat d’un patron | [GP-00](#gp-00--contrat-dun-patron-de-gameplay) |
| choisir selon le problème | [Matrice A](#matrice-a--sélection-par-problème) |
| séparer données, règles et présentation | [GP-01](#gp-01--données-règles-état-et-présentation) |
| modéliser un comportement exclusif | [GP-02](#gp-02--machine-à-états-finie) |
| choisir une variante simple ou avancée | [Matrice B](#matrice-b--variante-simple-ou-avancée) |
| combiner plusieurs dimensions de comportement | [GP-03](#gp-03--hiérarchie-régions-parallèles-et-sélecteurs) |
| définir une capacité ou compétence | [GP-04](#gp-04--capacités-compétences-et-effets-composables) |
| faire passer une intention vers une autorité | [GP-05](#gp-05--commande-action-résultat-et-événement) |
| organiser objets, conteneurs et équipement | [GP-06](#gp-06--inventaire-conteneurs-équipement-et-provenance) |
| suivre quêtes, objectifs et connaissances | [GP-07](#gp-07--faits-quêtes-objectifs-et-conséquences) |
| simuler un monde avec un temps logique | [GP-08](#gp-08--simulation-déterministe-ticks-et-budgets) |
| séparer existence logique et représentation | [GP-09](#gp-09--matérialisation-active-arrière-plan-et-dormante) |
| coordonner plusieurs autorités | [GP-10](#gp-10--préparation-commit-et-compensation) |
| composer les patrons et les tester | [GP-11](#gp-11--composition-extensibilité-et-coutures-de-test) |
| comparer preuves et signaux de retrait | [Matrice C](#matrice-c--preuves-coûts-et-signaux-de-retrait) |
| diagnostiquer les anti-patterns | [GP-12](#gp-12--anti-patterns-diagnostics-et-acceptation) |

---

<!-- l5:card -->
## GP-00 — Contrat d’un patron de gameplay

| Champ | Question obligatoire |
|---|---|
| problème | quelle décision ou transition se répète |
| autorité | quel système peut accepter ou refuser la mutation |
| données | quelles définitions immuables décrivent les possibilités |
| état | quelles valeurs vivantes évoluent pendant la partie |
| intention | qui demande l’action et avec quels identifiants |
| validation | quelles préconditions sont relues avant l’effet |
| transition | quel état initial peut devenir quel état final |
| temps | frame, tick logique, tour, échéance ou durée de session |
| ordre | quelles règles départagent deux demandes concurrentes |
| résultat | succès, refus contrôlé, absence ou erreur technique |
| événement | quel fait minimal est publié après réussite |
| persistance | quelles données durables sont sauvegardées |
| preuve | quel test ou scénario observe l’invariant |
| limite | quand une solution plus simple suffit |

**Réponse rapide :** commencer par la [carte des autorités de `Project Asteria`](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#4-carte-des-autorités-de-project-asteria), puis appliquer le [contrat architectural de la fiche 16](CHAPITRE-16-Patrons-d-architecture.md#arc-00--contrat-dun-patron-architectural). Un patron de gameplay ne vaut que si son propriétaire, son état et sa preuve sont nommés.

**Diagramme compact :** `intention → validation propriétaire → candidat → commit → résultat → événement → présentation`.

---

<!-- l5:matrix -->
## Matrice A — Sélection par problème

| Problème dominant | Patron de départ | Variante avancée seulement si nécessaire | Source propriétaire |
|---|---|---|---|
| un seul mode actif parmi plusieurs | machine à états finie | hiérarchie ou régions parallèles | [personnages](../Livre-II/CHAPITRE-14-Personnages.md) |
| plusieurs actions choisies selon un contexte | catalogue + sélecteur déterministe | planificateur borné | [agents](../Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md#4-chaîne-dautorité) |
| action avec coûts, cibles et effets | définition + commande + pipeline d’effets | unité de travail multi-autorités | [compétences](../Livre-II/CHAPITRE-19-Competences-et-pouvoirs.md) |
| objets possédés et transférables | conteneurs + entrées + commandes de transfert | lots, équipement et provenance | [inventaire](../Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md) |
| progression narrative observable | faits + objectifs + conséquences préparées | arcs, visibilité et codex | [narration](../Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md) |
| évolution hors écran | état agrégé + ticks logiques | rattrapage agrégé borné | [écologie](../Livre-II/CHAPITRE-22-Monde-vivant-et-simulation-ecologique.md) |
| résolution ordonnée de demandes | commandes typées + ordre déterministe | file bornée ou phases | [combat](../Livre-II/CHAPITRE-18-Combat.md) |
| plusieurs systèmes doivent réussir ensemble | préparation + revalidation + commit | compensation documentée | [invariants non négociables](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#2-frontières-et-invariants-non-négociables) |
| afficher sans déplacer l’autorité | projection ou vue dérivée | modèle de vue mis en cache | [interface utilisateur](../Livre-III/CHAPITRE-24-Interface-utilisateur.md) |
| vérifier une règle ou une simulation | fixture minimale | simulation déterministe multi-systèmes | [tests](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) |

**Décision :** choisir le patron le plus petit qui rend explicites l’autorité, le temps, l’ordre et le résultat. Une hiérarchie, un planificateur ou une transaction coordonnée ne sont pas des valeurs par défaut.

---

<!-- l5:card -->
## GP-01 — Données, règles, état et présentation

| Couche | Contenu | Ne doit pas posséder |
|---|---|---|
| définition | identifiant, paramètres, tags, coûts candidats, limites | progression vivante ou références de scène |
| état runtime | valeurs mutables, révision, échéances, compteurs | textures, nœuds ou règles cachées |
| règles | validation, calcul, transition et résultat | accès direct à l’interface |
| application | orchestration des autorités et des ports | nouvelle règle métier implicite |
| présentation | animation, son, VFX, HUD et feedback | décision autoritaire |
| persistance | snapshot versionné, migration et restauration | cache, sélection ou projection reconstruisible |

Une `Resource` partagée décrit une possibilité ; elle ne devient pas l’état d’une instance. Cette séparation prolonge la [propriété d’état](CHAPITRE-16-Patrons-d-architecture.md#arc-08--propriété-détat-et-cycle-de-vie) et les catalogues du [chapitre 7](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md).

**Exemple Asteria :** `AbilityDefinition` décrit une compétence. `AbilityRuntimeState` conserve charges et échéances. `AbilityService` valide l’utilisation. `AbilityPresentationBridge` joue l’animation après le résultat accepté.

**Limite :** un prototype local peut regrouper plusieurs responsabilités dans un seul fichier, mais les quatre rôles restent distingués conceptuellement afin de pouvoir être séparés sans changer les règles.

---

<!-- l5:card -->
## GP-02 — Machine à états finie

| Élément | Contrat |
|---|---|
| état | nom stable représentant un mode exclusif |
| événement ou intention | donnée qui demande une transition |
| garde | prédicat sans effet de bord |
| transition | couple source, demande, destination et priorité |
| entrée | effets déclenchés après acceptation de la transition |
| sortie | nettoyage exécuté avant l’activation suivante |
| état initial | valeur explicite et valide |
| état terminal | état sans sortie normale, lorsqu’il existe |
| refus | transition absente ou garde fausse |
| trace | source, demande, destination, tick et résultat |

**Variante simple :** un `match` ou une table de transitions suffit lorsque le nombre d’états est petit et qu’une seule dimension varie.

**Variante avancée :** une classe par état devient utile lorsque chaque état possède des dépendances, des données temporaires ou des tests propres. La [composition avant héritage](CHAPITRE-16-Patrons-d-architecture.md#arc-03--composition-avant-héritage) reste le garde-fou contre une hiérarchie profonde.

**Diagramme compact :** `IDLE --move_requested--> MOVING --target_reached--> IDLE`; `MOVING --stun_accepted--> STUNNED`.

**À éviter :** faire de l’animation l’autorité de la transition. Une piste peut refléter `STUNNED`, mais elle ne décide ni l’acceptation du stun ni sa durée logique.

---

<!-- l5:matrix -->
## Matrice B — Variante simple ou avancée

| Besoin observé | Solution simple | Solution avancée | Porte avant complexification |
|---|---|---|---|
| trois à six modes exclusifs | enum + table | objets d’état composés | logique spécifique réellement répétée |
| comportements combinables | drapeaux ou tags validés | régions parallèles | conflits et synchronisation mesurés |
| choix d’une action | priorité triée | utility scoring ou planificateur | scénarios où la priorité fixe échoue |
| effets d’une compétence | liste ordonnée d’effets | graphe acyclique préparé | dépendances entre effets prouvées |
| inventaire local | liste d’entrées | conteneurs imbriqués bornés | besoin réel de capacité ou délégation |
| quête linéaire | index d’étape | graphe d’objectifs | branches, retours ou objectifs parallèles |
| simulation proche | un pas par échéance | niveaux actif/arrière-plan/dormant | coût mesuré ou monde hors écran |
| coordination | service unique | unité de travail multi-autorités | succès partiel réellement dangereux |
| test | cas unitaires | simulation de scénario | invariant traversant plusieurs systèmes |

**Règle :** la variante avancée doit résoudre un cas observé et posséder un signal de retrait. Elle n’est pas adoptée pour rendre le diagramme plus impressionnant.

---

<!-- l5:card -->
## GP-03 — Hiérarchie, régions parallèles et sélecteurs

| Forme | Usage pertinent | Risque principal |
|---|---|---|
| état hiérarchique | partager des transitions entre sous-états | héritage implicite de comportements |
| régions parallèles | représenter locomotion, posture ou interaction indépendantes | combinaisons impossibles non validées |
| pile d’états | pause, menu, dialogue ou interruption temporaire | retour vers un état devenu invalide |
| sélecteur prioritaire | première règle valide dans un ordre stable | priorité cachée dans l’ordre du code |
| score d’utilité | comparer plusieurs actions avec critères explicites | score présenté comme vérité absolue |
| planificateur | construire une suite d’actions bornée | explosion combinatoire et plan périmé |
| tableau noir | partager des faits de travail bornés | devenir un dictionnaire global mutable |

L’agent du [chapitre 17](../Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md) observe, choisit et propose une action ; il ne remplace pas la machine à états propriétaire du personnage, du combat ou d’une quête.

**Diagramme compact :** `perception → snapshot immuable → sélecteur/plan → requête d’action → validation propriétaire`.

**Limite :** des régions parallèles ne doivent pas servir à contourner les invariants. Si `DEAD` interdit toute interaction, cette règle reste centralisée et ne dépend pas d’une combinaison de drapeaux dispersés.

---

<!-- l5:card -->
## GP-04 — Capacités, compétences et effets composables

| Élément | Responsabilité |
|---|---|
| définition | identité, conditions, coûts, ciblage et effets demandés |
| état de progression | rang, expérience et déblocages durables |
| état runtime | charges, recharge et compteurs temporaires |
| commande | utilisateur, capacité, cibles proposées, tick et révisions |
| plan d’exécution | coûts et effets candidats préparés |
| effet | demande typée vers l’autorité propriétaire |
| résultat | succès, refus nommé ou erreur technique |
| événement | fait minimal publié après commit |

Le patron complet appartient au [chapitre 19](../Livre-II/CHAPITRE-19-Competences-et-pouvoirs.md). La fiche retient trois frontières : une définition ne stocke pas les charges ; un effet ne modifie pas directement la santé ou l’inventaire ; une prévisualisation n’est pas un résultat.

**Variante simple :** une capacité contient une liste ordonnée d’effets indépendants.

**Variante avancée :** un graphe d’effets est acceptable uniquement s’il est acyclique, validé avant exécution, borné en taille et incapable de charger une méthode depuis les données.

**Exemple Asteria :** une compétence de soin prépare un coût d’endurance et une demande de ressource positive. Le système de personnage revalide la cible ; l’animation reçoit ensuite le résultat committé.

---

<!-- l5:card -->
## GP-05 — Commande, action, résultat et événement

| Notion | Question | Moment |
|---|---|---|
| intention | que souhaite le joueur, l’agent ou le scénario | avant validation |
| commande | quelles données typées sont soumises | entrée du cas d’usage |
| candidat | quel nouvel état serait valide | préparation |
| résultat | qu’a décidé l’autorité | après validation ou commit |
| événement | quel fait accepté intéresse les observateurs | après réussite |
| feedback | que doit voir ou entendre le joueur | après résultat |

**Règle :** une commande demande ; un résultat répond ; un événement constate. Le [service d’application](CHAPITRE-16-Patrons-d-architecture.md#arc-04--service-dapplication-commandes-et-requêtes) orchestre ce flux, tandis que le [bus typé](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md#7-créer-un-bus-dévénements-limité-et-typé) ne remplace pas le retour direct.

**Diagramme compact :** `Input/AI/Quest → Command → Owner.validate() → Candidate → Commit → Result → Event → UI/VFX/Audio`.

**À éviter :** envoyer `use_item` dans un bus générique et laisser un observateur inconnu décider de la mutation. Le propriétaire doit être appelé par un contrat explicite et retourner un résultat nommé.

---

<!-- l5:card -->
## GP-06 — Inventaire, conteneurs, équipement et provenance

| Élément | Contrat minimal |
|---|---|
| définition d’objet | données de conception immuables |
| instance | identité unique et état individualisé |
| lot | quantité fongible partageant définition et origine compatibles |
| entrée | référence vers une instance ou un lot |
| conteneur | capacité, politique d’accès, révision et entrées |
| équipement | emplacements et contraintes explicites |
| transfert | source, destination, quantité et révisions attendues |
| provenance | événements bornés expliquant l’origine |
| propriété | droit métier distinct de la garde matérielle |
| durabilité | état possédé par l’inventaire, modifié sur demande validée |

Le [chapitre 20](../Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md) possède les règles complètes. Le patron de conteneur exige une préparation de la source et de la destination avant retrait, puis un remplacement commun.

**Variante simple :** un inventaire plat de petites entrées suffit pour un prototype sans poids, équipement ni transferts complexes.

**Variante avancée :** conteneurs imbriqués, lots, équipement et provenance sont ajoutés séparément, chacun avec capacité, profondeur, cycle et règles de fusion bornés.

**À éviter :** stocker le prix dans l’objet, déduire la propriété depuis le personnage qui garde l’objet, ou laisser l’interface modifier directement une quantité.

---

<!-- l5:card -->
## GP-07 — Faits, quêtes, objectifs et conséquences

| Élément | Fonction |
|---|---|
| événement source | fait accepté par un système propriétaire |
| fait narratif | représentation normalisée et versionnée |
| définition de quête | objectifs, conditions et conséquences déclaratives |
| instance de quête | progression durable du joueur ou du groupe |
| objectif | règle déterministe observant des faits ou des vues |
| conséquence | demande préparée vers une autorité externe |
| connaissance | information découverte par un sujet |
| codex | présentation durable de connaissances autorisées |
| journal | projection lisible, jamais autorité de progression |

La narration du [chapitre 25](../Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md) observe les faits sans les remplacer. Une chaîne fiable suit : `GameplayEvent → NarrativeFact → évaluation → candidats → commit commun`.

**Variante simple :** une quête linéaire conserve un index d’étape et des objectifs indépendants.

**Variante avancée :** un graphe d’objectifs explicite dépendances, alternatives et objectifs parallèles. Les conditions restent des données interprétées par un catalogue fermé ; elles ne contiennent ni code, ni nom de méthode exécutable.

**À éviter :** valider une quête depuis un texte d’interface, une sortie IA ou la simple réception d’un événement sans vérifier son identité et son contexte.

---

<!-- l5:card -->
## GP-08 — Simulation déterministe, ticks et budgets

| Élément | Contrat |
|---|---|
| horloge logique | entier autoritaire, indépendant de l’horloge système |
| fréquence | politique nominale, pas garantie de durée réelle |
| échéance | prochain tick auquel une entité devient éligible |
| pas de simulation | fonction déterministe sur état et contexte |
| budget | nombre maximal d’entités ou d’opérations par cycle |
| ordre | tri stable par échéance puis identifiant |
| résidu | reste borné conservant les fractions discrètes |
| rattrapage | agrégation bornée d’un intervalle |
| graine | état pseudo-aléatoire local et persistable |
| résultat | nouvel état candidat et événements dérivés |

Le monde vivant du [chapitre 22](../Livre-II/CHAPITRE-22-Monde-vivant-et-simulation-ecologique.md) possède l’horloge globale, les régions, populations et ressources. Les agents du chapitre 17 possèdent leurs propres échéances de décision, sans créer une seconde horloge autoritaire du monde.

**Diagramme compact :** `clock.advance() → scheduler.select_due(budget) → simulate(copy, elapsed_ticks) → validate → replace → events`.

**À éviter :** utiliser un `Timer`, l’heure système, l’ordre d’un dictionnaire ou le nombre de nœuds visibles comme vérité de simulation.

---

<!-- l5:card -->
## GP-09 — Matérialisation active, arrière-plan et dormante

| Niveau | État logique | Représentation | Fréquence |
|---|---|---|---|
| actif | complet ou détaillé | scène et contrôleurs présents | fréquente et bornée |
| arrière-plan | complet mais agrégé | aucune scène obligatoire | espacée |
| dormant | durable minimal | aucune représentation | reprise agrégée |
| matérialisé | identité logique reliée à un acteur | nœud temporaire | selon visibilité et intérêt |
| dématérialisé | identité toujours existante | nœud retiré | simulation logique maintenue |

**Règle :** matérialiser ne crée pas l’entité métier ; dématérialiser ne la détruit pas. Le [registre des personnages actifs](../Livre-II/CHAPITRE-14-Personnages.md) suit seulement les instances présentes, tandis que les dépôts logiques conservent les identités absentes.

**Exemple Asteria :** une population écologique reste agrégée. Lorsqu’une zone devient active, un échantillon d’acteurs reçoit des identités ou références autorisées ; leur retrait visuel ne modifie pas automatiquement la population.

**Limite :** le passage entre niveaux doit conserver une révision, une échéance et une politique de conflit. Une réponse tardive d’un ancien acteur ne peut pas muter l’état après dématérialisation.

---

<!-- l5:card -->
## GP-10 — Préparation, commit et compensation

| Phase | Action autorisée |
|---|---|
| lecture | obtenir snapshots et révisions |
| validation | vérifier identités, droits, ressources et contexte |
| préparation | produire des copies ou candidats détachés |
| revalidation | confirmer les révisions juste avant mutation |
| commit | remplacer les états compatibles dans l’ordre déclaré |
| publication | émettre les événements après réussite |
| compensation | réparer une frontière non transactionnelle selon un plan explicite |
| diagnostic | conserver cause initiale, candidats et décision |

Ce patron est requis lorsqu’une action concerne plusieurs autorités : achat et transfert d’objet, compétence et ressources, récolte et inventaire, quête et récompense, sanction et confiscation.

**Diagramme compact :** `prepare A + prepare B → revalidate A/B → commit commun → events`; en cas d’impossibilité transactionnelle : `commit A → échec B → compensation documentée`, jamais « succès partiel silencieux ».

La fiche 16 décrit l’[unité de travail bornée](CHAPITRE-16-Patrons-d-architecture.md#arc-05--repository-et-unité-de-travail). Les règles économiques, écologiques, narratives ou d’inventaire restent propriétaires de leurs candidats.

**À éviter :** consommer un coût avant de savoir si l’effet est valide, retirer l’objet avant de valider la destination ou publier un événement avant le commit.

---

<!-- l5:card -->
## GP-11 — Composition, extensibilité et coutures de test

| Besoin | Couture minimale |
|---|---|
| nouvelle stratégie de choix | interface observable + mêmes scénarios |
| nouvel effet | type fermé ou registre borné validé |
| nouveau conteneur | politique injectée sans accès global |
| nouvelle condition de quête | interpréteur fermé et données versionnées |
| nouveau mode de simulation | même état canonique et échéances explicites |
| nouvelle présentation | vue dérivée et événements après commit |
| nouvel adaptateur | test de contrat commun |
| nouvelle extension communautaire | manifeste, capacités et refus par défaut |

Un patron extensible ne charge pas une classe, une méthode ou un script depuis les données. La [stratégie et le registre borné](CHAPITRE-16-Patrons-d-architecture.md#arc-10--stratégie-fabrique-et-registre-borné) limitent les variantes connues ; les extensions exécutables restent soumises au chapitre de [modding](../Livre-IV/CHAPITRE-21-Modding-et-contenu-communautaire.md).

**Ordre de preuve :** règle pure → service avec doubles → adaptateur réel → composition → simulation. Les [coutures de test](CHAPITRE-16-Patrons-d-architecture.md#arc-11--coutures-de-test-et-tests-de-contrat) et le [portfolio de tests](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) empêchent de confondre une fixture synthétique avec un runtime complet.

**Limite :** une interface n’est utile que lorsqu’une substitution, une frontière ou une preuve existe. Une abstraction vide par classe augmente le coût sans rendre le gameplay plus extensible.

---

<!-- l5:matrix -->
## Matrice C — Preuves, coûts et signaux de retrait

| Patron | Preuve minimale | Coût accepté | Signal de retrait |
|---|---|---|---|
| machine à états | transitions autorisées et refusées | table ou objets d’état | un booléen suffit |
| régions parallèles | combinaisons et exclusions | synchronisation supplémentaire | conflits plus nombreux que les états |
| sélecteur prioritaire | ordre stable et scénario limite | règles de priorité | une seule action durable |
| score d’utilité | critères, bornes et départage | calcul et diagnostic | score non interprétable |
| planificateur | borne, invalidation et replanning | recherche et mémoire | plan toujours d’une action |
| capacité composable | coûts et effets préparés | catalogue d’effets | effet unique sans variante |
| conteneurs | conservation quantité/identité | révisions et capacités | inventaire plat suffisant |
| graphe de quête | dépendances et cycles refusés | versionnement du graphe | progression strictement linéaire |
| simulation agrégée | même résultat pour mêmes entrées | résidus et rattrapage | aucune évolution hors écran |
| matérialisation | identité conservée sans nœud | registre et synchronisation | toutes les entités toujours actives |
| unité de travail | absence de succès partiel | préparation et compensation | une seule autorité concernée |
| bus d’événements | publication après commit | traçage et ordre | un seul consommateur local |

Le critère d’acceptation n’est pas le nombre de patrons. Une solution est meilleure lorsqu’elle réduit les états impossibles, garde les mutations propriétaires et produit une preuve plus petite.

---

<!-- l5:card -->
## GP-12 — Anti-patterns, diagnostics et acceptation

<!-- qa:error-correction-index -->

Cette section est un index de diagnostics. Les exemples fautifs et corrigés détaillés restent dans les sections propriétaires des Livres II à IV ; les liens ci-dessous permettent de rejoindre leur contexte complet sans le recopier.

| Symptôme | Anti-pattern probable | Vérification | Correction minimale |
|---|---|---|---|
| l’animation applique les dégâts | présentation autoritaire | tracer l’écriture de santé | commander le combat puis refléter le résultat |
| chaque état connaît tous les autres | machine à états couplée | compter transitions dispersées | table ou coordinateur de transitions |
| vingt booléens se contredisent | états implicites | lister combinaisons impossibles | état exclusif ou régions validées |
| une `Resource` perd des charges pour tous | définition utilisée comme runtime | inspecter le propriétaire du fichier | état d’instance séparé |
| l’agent écrit directement l’inventaire | frontière d’autorité absente | suivre la requête d’action | commande typée vers `InventoryService` |
| une quête se termine sur un libellé | texte utilisé comme identité | inspecter clé et fait source | identifiant stable + condition déterministe |
| un `Timer` fait avancer le monde | temps de scène autoritaire | comparer pause, reprise et sauvegarde | horloge logique persistable |
| retirer un nœud supprime l’entité | scène confondue avec état logique | charger la zone hors écran | dépôt logique + matérialisation |
| un coût est consommé avant l’effet | commit fractionné | injecter un refus tardif | préparation puis commit commun |
| un bus contient commandes et états | bus universel | inventorier producteurs et consommateurs | appels directs et événements après succès |
| le test exige la scène principale | dépendance cachée | lancer une fixture isolée | ports, doubles et composition de test |
| le patron avancé n’a aucun scénario | abstraction spéculative | chercher la preuve de besoin | revenir à la variante simple |

**Portes d’acceptation :**

1. chaque mutation possède une autorité nommée ;
2. définitions, état runtime et présentation sont séparés ;
3. commandes, résultats et événements ne sont pas confondus ;
4. transitions et ordres sont déterministes ou explicitement arbitrés ;
5. le temps autoritaire utilise des ticks logiques ;
6. une représentation peut disparaître sans supprimer l’état métier ;
7. les effets multi-systèmes sont préparés avant commit ;
8. aucune donnée ne nomme une méthode ou un script à exécuter ;
9. chaque variante avancée possède une preuve et un signal de retrait ;
10. les tests distinguent règle pure, composant, intégration et simulation.

La QA générale relève du [Livre IV, chapitre 2](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md), le diagnostic du [Livre IV, chapitre 4](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md), l’observabilité du [Livre IV, chapitre 5](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md) et les campagnes de tests du [Livre II, chapitre 27](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md).

## Sources et frontières internes

- [Livre II, chapitre 14 — Personnages](../Livre-II/CHAPITRE-14-Personnages.md)
- [Livre II, chapitre 17 — Agents IA et comportements autonomes](../Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md)
- [Livre II, chapitre 18 — Combat](../Livre-II/CHAPITRE-18-Combat.md)
- [Livre II, chapitre 19 — Compétences et pouvoirs](../Livre-II/CHAPITRE-19-Competences-et-pouvoirs.md)
- [Livre II, chapitre 20 — Inventaire et réputation des objets](../Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md)
- [Livre II, chapitre 22 — Monde vivant et simulation écologique](../Livre-II/CHAPITRE-22-Monde-vivant-et-simulation-ecologique.md)
- [Livre II, chapitre 25 — Narration, quêtes, codex et connaissances](../Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md)
- [Livre II, chapitre 27 — Tests unitaires, tests d’intégration et simulations](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md)
- [Livre V, fiche 16 — Patrons d’architecture](CHAPITRE-16-Patrons-d-architecture.md)

Les systèmes complets, leurs structures de données, leurs services et leurs exemples exécutables restent dans les chapitres propriétaires. La fiche 18 possédera la référence graphique et 3D. Les scènes, scripts, fixtures et assets permanents appartiennent au Companion Pack. Aucun runtime Godot, GDScript, scène, addon, base, réseau, service IA, simulation de production ou PDF n’est prétendu exécuté par cette fiche.
