---
title: "Livre V — Fiche 26 : Index croisés"
id: "DOC-L5-CH26"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 26
last-verified: "2026-07-30T01:18:00+02:00"
audit-status: "complete"
audit-date: "2026-07-30T01:18:00+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-26.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "cross-indexes-synonyms-aliases-navigation-integrity-and-orphan-detection"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Index croisés

> **Type de document :** index alphabétiques et thématiques, tables de synonymes, relations croisées, routes par scénario et portes d’intégrité.
> **Lecture :** partir d’un mot, d’un besoin, d’un symptôme ou d’un ancien nom, suivre l’entrée canonique, puis ouvrir la fiche du Livre V et la procédure propriétaire.
> **Principe :** l’index relie des autorités ; il ne les remplace pas, ne réécrit pas leur contenu et ne transforme pas une occurrence textuelle en relation sémantique certaine.

## Règles de lecture

| Règle | Conséquence |
|---|---|
| une entrée canonique possède une identité stable | le libellé affiché peut évoluer sans casser les relations |
| un alias pointe vers une cible | un synonyme, acronyme ou ancien nom ne devient pas une seconde définition |
| chaque relation possède un type | `owner`, `prerequisite`, `validates`, `alternative`, `diagnoses`, `supersedes` et `related` ne sont pas interchangeables |
| la source propriétaire reste prioritaire | l’index résume seulement la destination et la raison du lien |
| une absence n’est pas une conclusion | un terme non indexé peut être nouveau, local, trop général ou réellement orphelin |
| les versions et statuts restent visibles | une ancienne appellation ne doit pas diriger silencieusement vers une procédure obsolète |
| le support de publication compte | un lien Markdown valide ne prouve pas encore la navigation PDF, HTML ou EPUB finale |
| l’intégrité est rejouable | chaque contrôle nomme son corpus, sa date, son outil et ses limites |

**Réponse rapide :** la [carte générale](CHAPITRE-01-Carte-generale-de-la-collection.md#index-express) oriente par besoin ; les [arbres de décision](CHAPITRE-02-Arbres-de-decision.md) orientent par contraintes ; la présente fiche relie les termes, concepts, formats, symptômes, licences et anciennes appellations à leurs autorités.

## Index express

| Besoin | Ouvrir |
|---|---|
| définir une entrée d’index complète | [IDX-00](#idx-00--contrat-dune-entrée-dindex) |
| choisir le propriétaire d’un type d’entrée | [Matrice A](#matrice-a--types-dentrées-et-autorités) |
| séparer identité, libellé et destination | [IDX-01](#idx-01--identité-canonique-et-cible) |
| ordonner un index alphabétique | [IDX-02](#idx-02--index-alphabétique-et-règles-de-tri) |
| construire des facettes thématiques | [IDX-03](#idx-03--index-thématique-et-facettes) |
| traiter synonymes, acronymes et anciens noms | [IDX-04](#idx-04--synonymes-alias-et-appellations-retirées) |
| comprendre le comportement d’une relation | [Matrice B](#matrice-b--relations-statuts-et-navigation) |
| retrouver un outil ou un environnement | [IDX-05](#idx-05--outils-environnements-et-services) |
| retrouver un système ou un patron | [IDX-06](#idx-06--systèmes-architecture-données-et-gameplay) |
| retrouver un format, fichier ou protocole | [IDX-07](#idx-07--formats-fichiers-protocoles-et-interfaces) |
| partir d’un symptôme ou d’un message | [IDX-08](#idx-08--symptômes-erreurs-preuves-et-diagnostics) |
| retrouver une licence ou une obligation | [IDX-09](#idx-09--licences-provenance-conformité-et-publication) |
| suivre une route par scénario | [IDX-10](#idx-10--routes-par-besoin-et-parcours-solo-studio) |
| préparer PDF, HTML et EPUB | [IDX-11](#idx-11--navigation-multiformat-et-accessibilité) |
| détecter liens cassés, doublons et orphelins | [Matrice C](#matrice-c--contrôles-dintégrité-et-actions) |
| maintenir et clôturer l’encyclopédie | [IDX-12](#idx-12--maintenance-rapports-dintégrité-et-clôture) |

---

<!-- l5:card -->
## IDX-00 — Contrat d’une entrée d’index

| Champ | Règle |
|---|---|
| identifiant | stable, unique et indépendant du titre affiché |
| terme canonique | forme retenue par la collection pour la recherche et les renvois |
| variantes | pluriel, accentuation, casse, acronyme, traduction, ancien nom ou faute fréquente documentée |
| type | outil, système, concept, format, erreur, licence, procédure, rôle, artefact ou statut |
| portée | collection, Livre, domaine, version, plateforme ou scénario concerné |
| destination | fichier et fragment existants, ou statut explicite si la cible n’est pas encore matérialisée |
| relation | nature du lien vers la destination et direction de lecture |
| résumé | une phrase expliquant pourquoi ouvrir cette cible |
| propriétaire | document qui définit le terme ou la procédure |
| compléments | prérequis, validation, alternative, diagnostic ou publication |
| statut | `canonical`, `alias`, `deprecated`, `planned`, `unresolved` ou `retired` |
| version | première version, dernière revue et éventuelle version de retrait |
| preuve | contrôle de lien, source documentaire, rapport d’intégrité ou décision éditoriale |
| confidentialité | aucune donnée personnelle, secret ou chemin restreint exposé dans l’index public |
| historique | prédécesseur, successeur, motif et date de modification |

**Réponse rapide :** l’entrée d’index répond à « quel terme conduit vers quelle autorité, pourquoi et avec quel statut ? ». Elle ne copie ni la définition complète ni la procédure.

**Diagramme compact :** `requête → normalisation → entrée canonique → relation typée → destination propriétaire → complément ou validation`.

**Niveau de preuve :** `static-review`. Aucun moteur de recherche, index généré, PDF, HTML, EPUB ou rapport d’orphelins complet n’est matérialisé dans cette fiche.

---

<!-- l5:matrix -->
## Matrice A — Types d’entrées et autorités

| Type recherché | Autorité de référence | Complément transversal | Exemple d’entrée |
|---|---|---|---|
| ensemble ou parcours | [carte générale](CHAPITRE-01-Carte-generale-de-la-collection.md#nav-01--rôle-des-sept-ensembles) | [routes par scénario](#idx-10--routes-par-besoin-et-parcours-solo-studio) | Livre II, Solo, Studio |
| décision | [arbres de décision](CHAPITRE-02-Arbres-de-decision.md) | [comparatifs](CHAPITRE-23-Comparatifs-des-solutions.md#cmp-00--contrat-minimal-dun-comparatif) | backend local, stockage |
| logiciel ou outil | [fiches d’outils](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#index-express) | [compatibilités](CHAPITRE-22-Matrices-de-compatibilite.md) | Godot, Blender, Python |
| moteur ou modèle IA | [moteurs](CHAPITRE-04-Fiches-des-moteurs-et-backends-IA.md), [LLM](CHAPITRE-05-Fiches-des-modeles-de-langage.md), [visuel](CHAPITRE-06-Fiches-des-modeles-visuels.md), [audio](CHAPITRE-07-Fiches-des-modeles-audio.md) | [licences](CHAPITRE-25-Licences-provenance-et-conformite.md#lic-06--modèles-datasets-entrées-sorties-et-services-ia) | llama.cpp, LoRA, TTS |
| workflow, prompt ou script | [workflows](CHAPITRE-08-Bibliotheque-de-workflows.md), [prompts](CHAPITRE-09-Bibliotheque-de-prompts.md), [scripts](CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md) | [checklists](CHAPITRE-24-Checklists-de-production-et-de-publication.md) | import, génération, validation |
| langage | [GDScript](CHAPITRE-11-Reference-GDScript.md), [Python](CHAPITRE-12-Reference-Python.md) | [diagnostics](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md) | signal, type, exception |
| format ou stockage | [formats](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#index-express), [SQLite](CHAPITRE-14-Schemas-SQLite-et-migrations.md), [vecteurs](CHAPITRE-15-Bases-vectorielles-et-recherche-semantique.md) | [compatibilités](CHAPITRE-22-Matrices-de-compatibilite.md) | JSONL, TSCN, WAL |
| patron ou système | [architecture](CHAPITRE-16-Patrons-d-architecture.md#index-express), [gameplay](CHAPITRE-17-Patrons-de-gameplay.md) | chapitres propriétaires du [Livre II](../Livre-II/index.md) | repository, quête, inventaire |
| média | [graphique et 3D](CHAPITRE-18-Reference-graphique-et-3D.md), [audio](CHAPITRE-19-Reference-audio.md) | production du [Livre III](../Livre-III/index.md) | PBR, rig, loudness |
| symptôme ou erreur | [catalogue diagnostique](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md#index-express) | QA et exploitation du [Livre IV](../Livre-IV/index.md) | crash, lenteur, artefact |
| mesure ou support | [benchmarks](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md), [compatibilité](CHAPITRE-22-Matrices-de-compatibilite.md) | [comparatifs](CHAPITRE-23-Comparatifs-des-solutions.md) | p95, officiellement supporté |
| porte ou publication | [checklists](CHAPITRE-24-Checklists-de-production-et-de-publication.md#index-express) | [licences](CHAPITRE-25-Licences-provenance-et-conformite.md#index-express) | release, attribution |
| gouvernance | [Volume 0](../Volume-0/index.md) | continuité et plans maîtres | version, preuve, licence globale |

**Décision :** l’index dirige d’abord vers l’autorité la plus spécialisée, puis vers la validation ou l’alternative. Un terme présent dans plusieurs domaines reçoit plusieurs relations, pas une définition fusionnée.

---

<!-- l5:card -->
## IDX-01 — Identité canonique et cible

| Élément | Contrat |
|---|---|
| identifiant | clé immuable de l’entrée, par exemple `IDX-CONCEPT-0042` |
| libellé | forme lisible actuelle, modifiable sans changer l’identité |
| clé normalisée | forme de recherche en minuscules, espaces réduits et ponctuation contrôlée |
| cible primaire | unique pour `owner`, sauf concept réellement partagé et explicitement gouverné |
| cibles secondaires | validation, alternative, diagnostic, migration ou historique |
| fragment | sous-section stable lorsque la destination précise est connue |
| titre observé | texte de la destination lors de la dernière vérification |
| statut de cible | présente, déplacée, remplacée, planifiée, retirée ou inconnue |
| redirection | ancienne cible vers nouvelle cible, sans boucle |
| cycle | date de vérification, événement de réouverture et propriétaire |

**Réponse rapide :** le couple `identifiant + relation` survit aux renommages. Le chemin seul n’est pas une identité métier ; le titre seul n’est pas une garantie de destination.

**Diagramme compact :** `ID stable → libellé courant → clé normalisée → cible primaire → cibles secondaires → historique`.

**Limite :** une ancre Markdown peut changer après renommage de titre. Les fragments critiques doivent être vérifiés par le validateur et remplacés par une ancre explicite lorsque la stabilité l’exige.

---

<!-- l5:card -->
## IDX-02 — Index alphabétique et règles de tri

| Dimension | Règle |
|---|---|
| casse | recherche insensible à la casse ; affichage selon l’orthographe canonique |
| accents | conserver à l’affichage ; permettre une clé de recherche sans accent |
| articles | trier selon le terme métier, pas automatiquement selon « le », « la » ou « un » |
| chiffres | utiliser un tri naturel déclaré pour `Livre 2`, `Livre 10` ou `v2`, `v10` |
| acronymes | indexer l’acronyme et la forme développée avec une cible commune |
| noms de produit | respecter la graphie officielle dans le libellé canonique |
| code | conserver symboles, classe, méthode ou extension exacts comme variante littérale |
| homonymes | ajouter un qualificateur de domaine : `signal (Godot)` ou `signal (diagnostic)` |
| pluriels | rediriger vers la forme canonique sans dupliquer la définition |
| langues | relier une traduction à la forme canonique française ou technique retenue |
| caractères spéciaux | fournir une variante de recherche lorsqu’ils sont difficiles à saisir |
| ordre publié | produire une table déterministe pour éviter des différences entre formats |

**Réponse rapide :** l’index alphabétique sert à retrouver un terme déjà connu. L’[index thématique](#idx-03--index-thématique-et-facettes) sert à explorer un domaine ou un objectif.

**Diagramme compact :** `forme saisie → normalisation déclarée → homonyme qualifié → terme canonique → ordre déterministe`.

**Exemples de renvoi :** `Web Socket` → `WebSocket` ; `VRAM` → `mémoire vidéo` ; `glTF` et `GLB` restent deux entrées reliées mais non synonymes.

---

<!-- l5:card -->
## IDX-03 — Index thématique et facettes

| Facette | Valeurs de départ | Source de vérité |
|---|---|---|
| ensemble | Volume 0, Livres I à V, Companion Pack | [carte générale](CHAPITRE-01-Carte-generale-de-la-collection.md) |
| domaine | plateforme, architecture, données, IA, gameplay, art, audio, QA, exploitation | plans maîtres |
| action | installer, créer, convertir, mesurer, diagnostiquer, publier, maintenir | fiches et procédures |
| objet | outil, fichier, asset, modèle, build, service, sauvegarde, preuve | propriétaires spécialisés |
| phase | cadrage, production, intégration, QA, build, publication, maintenance | [checklists](CHAPITRE-24-Checklists-de-production-et-de-publication.md#chk-01--phase-lot-portée-et-porte) |
| plateforme | Windows, CPU, GPU AMD, conteneur, serveur, Web | [matrices de compatibilité](CHAPITRE-22-Matrices-de-compatibilite.md) |
| organisation | Solo, Studio, propriétaire, approbateur | [architecture Solo/Studio](../Livre-II/CHAPITRE-30-Architecture-Solo-et-architecture-Studio.md#4-carte-des-autorités-de-project-asteria) |
| preuve | statique, officielle, mesurée, reproduite, approuvée | [benchmarks](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md) et [diagnostics](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md#diag-01--vocabulaire-et-niveaux-de-certitude) |
| risque | sécurité, confidentialité, licence, accessibilité, perte, verrouillage | chapitres propriétaires |
| statut | actuel, expérimental, inconnu, retiré, remplacé, planifié | entrée et source propriétaire |

**Réponse rapide :** une facette est un axe de filtrage, pas une nouvelle taxonomie propriétaire. Elle pointe vers les documents qui portent les définitions.

**Diagramme compact :** `besoin large → facettes domaine/action/objet/phase → petit ensemble de candidats → source propriétaire`.

**Limite :** les facettes ne doivent pas conclure qu’un terme absent d’une catégorie est incompatible avec celle-ci. L’absence peut provenir d’un index incomplet.

---

<!-- l5:card -->
## IDX-04 — Synonymes, alias et appellations retirées

| Relation | Exemple | Comportement |
|---|---|---|
| acronyme | `LLM` → modèle de langage | afficher les deux formes et partager la cible |
| nom développé | `interface de programmation` → API | rediriger vers le terme technique canonique |
| graphie | `Web Socket` → `WebSocket` | corriger sans créer une seconde entrée |
| traduction | `fallback` → repli | conserver la forme rencontrée dans les sources |
| terme voisin | `sauvegarde` ↔ snapshot | relier comme `related`, pas comme synonyme |
| ancien nom | nom de fichier ou outil remplacé | marquer `deprecated` et pointer vers le successeur |
| version retirée | API ou format obsolète | conserver la portée historique et l’alternative |
| erreur fréquente | orthographe réellement observée | rediriger sans propager la faute dans les titres |
| collision | même mot dans deux domaines | demander ou afficher un qualificateur |
| terme interdit | libellé trompeur comme `gratuit = libre` | renvoyer vers la correction et la source |

**Réponse rapide :** `alias` aide la recherche ; `deprecated` conserve l’histoire ; `related` signale une proximité ; `supersedes` décrit un remplacement. Ces relations ne sont jamais converties silencieusement les unes dans les autres.

**Diagramme compact :** `variante rencontrée → relation qualifiée → terme canonique → avertissement éventuel → destination actuelle`.

**Routage utile :** les confusions de licence rejoignent [LIC-02](CHAPITRE-25-Licences-provenance-et-conformite.md#lic-02--texte-identifiant-et-expression-de-licence) ; les confusions diagnostiques rejoignent [DIAG-01](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md#diag-01--vocabulaire-et-niveaux-de-certitude).

---

<!-- l5:matrix -->
## Matrice B — Relations, statuts et navigation

| Relation ou statut | Sens | Navigation affichée | Interdiction |
|---|---|---|---|
| `owner` | la cible définit le terme ou la procédure | « définition/procédure principale » | plusieurs propriétaires implicites |
| `prerequisite` | la cible doit être comprise ou réalisée avant | « commencer par » | présenter comme simple complément |
| `validates` | la cible fournit test, mesure ou porte | « vérifier avec » | confondre preuve et explication |
| `diagnoses` | la cible part du signal vers une cause | « diagnostiquer avec » | promettre une cause unique |
| `alternative` | autre voie raisonnable | « autre option » | la présenter comme équivalente sans limites |
| `supersedes` | la cible remplace l’entrée historique | « remplacé par » | effacer le prédécesseur |
| `related` | proximité utile mais non obligatoire | « voir aussi » | créer une dépendance |
| `canonical` | entrée active de référence | ouvrir normalement | dupliquer sous un autre ID |
| `alias` | variante de recherche | rediriger et afficher le canonique | contenir une définition divergente |
| `deprecated` | terme encore rencontré mais déconseillé | avertir puis rediriger | l’utiliser comme entrée principale |
| `planned` | cible prévue mais non matérialisée | afficher « planifié » sans faux lien | prétendre qu’elle existe |
| `unresolved` | relation ou cible non conclue | ouvrir une tâche de revue | choisir arbitrairement |
| `retired` | entrée retirée sans successeur direct | conserver l’historique | la proposer dans les routes actives |

**Décision :** une interface peut masquer les détails secondaires, mais elle ne doit jamais masquer le statut `deprecated`, `planned`, `unresolved` ou `retired`.

---

<!-- l5:card -->
## IDX-05 — Outils, environnements et services

| Terme ou variante | Entrée canonique | Première destination | Procédure propriétaire |
|---|---|---|---|
| terminal, shell, console | PowerShell 7 et Windows Terminal | [OUTIL-01](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-01--windows-terminal-et-powershell-7) | [terminaux Windows](../Livre-I/CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md#2-terminal-console-et-shell) |
| gestionnaire de paquets Windows | WinGet | [OUTIL-02](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-02--winget) | [vérifier WinGet](../Livre-I/CHAPITRE-02-Terminal-PowerShell-et-outils-Windows.md#31-vérifier-winget) |
| dépôt, commit, branche | Git | [OUTIL-03](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-03--git-for-windows) | [Git et VS Code](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#3-installer-git-for-windows) |
| PR, Actions, CI | GitHub | [OUTIL-04](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-04--github-et-github-actions) | [DevOps](../Livre-IV/CHAPITRE-14-DevOps-et-integration-continue.md#1-rôle-du-chapitre) |
| éditeur | Visual Studio Code | [OUTIL-05](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-05--visual-studio-code) | [installer VS Code](../Livre-I/CHAPITRE-03-Git-GitHub-et-VS-Code.md#5-installer-visual-studio-code) |
| interpréteur, `py`, `uv` | Python | [OUTIL-06](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-06--python-lanceur-py-et-uv) | [isoler Python](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md#1-pourquoi-isoler-python) |
| conteneur, Compose, WSL 2 | Docker Desktop | [OUTIL-07](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-07--docker-desktop-wsl-2-et-compose) | [objet de Docker](../Livre-I/CHAPITRE-05-Docker-et-Docker-Compose.md#1-objet-du-chapitre) |
| moteur de jeu | Godot Engine | [OUTIL-08](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-08--godot-engine) | [découvrir Godot](../Livre-II/CHAPITRE-01-Decouvrir-Godot-et-creer-le-projet-fil-rouge.md) |
| DCC, modélisation 3D | Blender | [OUTIL-09](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-09--blender) | [pipeline Blender](../Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md) |
| workflow nodal visuel | ComfyUI | [OUTIL-10](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-10--comfyui) | [références et concept art](../Livre-III/CHAPITRE-03-References-concept-art-et-ComfyUI.md) |
| interface LLM | Open WebUI | [OUTIL-11](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-11--open-webui) | [LLM locaux](../Livre-I/CHAPITRE-08-LLM-locaux-Ollama-llama-cpp-LocalAI-et-LibreChat.md) |
| exécution agentique | Open Terminal | [OUTIL-12](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#outil-12--open-terminal) | [sécurité et validation](../Livre-I/CHAPITRE-10-Securite-sauvegarde-et-validation.md) |

**Réponse rapide :** la carte d’outil indique la référence datée et les limites ; la procédure propriétaire indique l’installation ou l’usage ; la matrice de compatibilité indique le statut de la combinaison exacte.

**Limite :** cet index ne vérifie pas les versions installées et ne remplace pas [Matrice C — commandes minimales](CHAPITRE-03-Fiches-des-logiciels-et-outils.md#matrice-c--commandes-minimales-de-vérification).

---

<!-- l5:card -->
## IDX-06 — Systèmes, architecture, données et gameplay

| Requête | Destination de référence | Propriétaire détaillé |
|---|---|---|
| module, couche, frontière | [ARC-01](CHAPITRE-16-Patrons-d-architecture.md#arc-01--frontières-modules-et-direction-des-dépendances) | [architecture modulaire](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#3-périmètre-et-frontières) |
| composition root, injection | [ARC-02](CHAPITRE-16-Patrons-d-architecture.md#arc-02--composition-root-et-injection-explicite) | [services et injection](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md#10-construire-le-point-de-composition) |
| repository, unité de travail | [ARC-05](CHAPITRE-16-Patrons-d-architecture.md#arc-05--repository-et-unité-de-travail) | [repository](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md#45-repository) |
| ports et adaptateurs | [ARC-06](CHAPITRE-16-Patrons-d-architecture.md#arc-06--ports-adaptateurs-et-couche-anti-corruption) | [direction des dépendances](../Livre-II/CHAPITRE-04-Architecture-modulaire-du-projet.md#53-dépendre-vers-les-règles-pas-vers-les-détails) |
| Resource, JSON, configuration | [formats](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md) | [données de conception](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md#5-matrice-de-décision) |
| SQLite, migration, WAL | [schémas SQLite](CHAPITRE-14-Schemas-SQLite-et-migrations.md) | [persistance relationnelle](../Livre-II/CHAPITRE-08-SQLite-migrations-et-donnees-persistantes.md) |
| sauvegarde, snapshot, reprise | [formats et migrations](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#fmt-04--schémas-enveloppes-et-versions) | [sauvegardes](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#6-choisir-le-format-de-référence) |
| embeddings, vecteurs, recherche | [bases vectorielles](CHAPITRE-15-Bases-vectorielles-et-recherche-semantique.md) | [mémoire sémantique](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md) |
| personnage, combat, inventaire | [patrons de gameplay](CHAPITRE-17-Patrons-de-gameplay.md) | [systèmes du Livre II](../Livre-II/index.md) |
| commande, signal, événement | [ARC-07](CHAPITRE-16-Patrons-d-architecture.md#arc-07--appels-signaux-événements-et-médiation) | [bus limité et typé](../Livre-II/CHAPITRE-05-Services-gestionnaires-bus-evenements-et-injection-de-dependances.md#7-créer-un-bus-dévénements-limité-et-typé) |
| test, fixture, oracle | [coutures de test](CHAPITRE-16-Patrons-d-architecture.md#arc-11--coutures-de-test-et-tests-de-contrat) | [tests unitaires et simulations](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) |
| automatisation de données | [scripts et recettes](CHAPITRE-10-Bibliotheque-de-scripts-et-recettes-de-code.md) | [automatisation Python](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md) |

**Réponse rapide :** rechercher le concept dans le patron transversal, puis ouvrir le système propriétaire. Le patron décrit une structure réutilisable ; le chapitre métier possède les règles, l’état et les invariants.

---

<!-- l5:card -->
## IDX-07 — Formats, fichiers, protocoles et interfaces

| Terme | Distinction à conserver | Première destination |
|---|---|---|
| JSON | document structuré, pas schéma ni transport | [FMT-03](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#fmt-03--json-strict) |
| JSONL | une valeur JSON par ligne | [FMT-05](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#fmt-05--jsonl-et-séquences-json) |
| JSON Text Sequences | séparateur `RS`, distinct de JSONL | [FMT-05](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#fmt-05--jsonl-et-séquences-json) |
| CSV | dialecte tabulaire déclaré | [FMT-06](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#fmt-06--csv-et-contrat-tabulaire) |
| YAML | profil borné et chargeur sûr | [FMT-07](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#fmt-07--yaml-sûr-et-prévisible) |
| `.tres`, `.res` | Resource Godot texte ou binaire | [FMT-08](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#fmt-08--ressources-scènes-et-formats-godot) |
| `.tscn`, `.scn` | scène Godot texte ou binaire | [FMT-08](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#fmt-08--ressources-scènes-et-formats-godot) |
| `.cfg`, `ConfigFile` | configuration Godot, pas INI universel | [FMT-09](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#fmt-09--configurations-et-fichiers-runtime) |
| SQLite | stockage relationnel transactionnel | [fiche 14](CHAPITRE-14-Schemas-SQLite-et-migrations.md) |
| stdio | transport local d’octets | [protocole JSON par lignes](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md#9-protocole-json-par-lignes) |
| HTTP | échange requête/réponse borné | [enveloppe réseau](../Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md#9-enveloppe-réseau) |
| WebSocket | flux de paquets et événements | [HTTP, WebSocket et tâches](../Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md) |
| glTF, GLB | format logique et conteneur binaire associé | [référence graphique](CHAPITRE-18-Reference-graphique-et-3D.md) |
| WAV, OGG, Opus | source, livraison et codec à distinguer | [référence audio](CHAPITRE-19-Reference-audio.md) |
| ZIP, package, archive | conteneur, livraison et conservation distincts | [exports et packaging](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md#6-distinguer-export-packaging-et-publication) |

**Réponse rapide :** commencer par [FMT-01 — couches et vocabulaire](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#fmt-01--couches-et-vocabulaire) lorsque deux termes semblent interchangeables.

**Limite :** une extension identique ne garantit ni le même profil, ni la même version, ni la même sémantique. L’index ne déduit pas la compatibilité depuis le nom du format.

---

<!-- l5:card -->
## IDX-08 — Symptômes, erreurs, preuves et diagnostics

| Requête initiale | Route recommandée | Qualification suivante |
|---|---|---|
| « ça ne marche pas » | [contrat diagnostique](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md#diag-00--contrat-dune-entrée-diagnostique) | préciser attendu, observé et contexte |
| message ou code exact | [messages et signatures](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md#diag-06--messages-codes-et-signatures) | conserver version et sortie complète |
| anomalie reproductible | [reproduction](../Livre-IV/CHAPITRE-04-Debogage-et-reproduction-des-anomalies.md#13-étapes-de-reproduction) | joindre oracle et fixture |
| log ou trace ambiguë | [observabilité](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md#8-distinguer-événements-métriques-et-traces) | corrélation et fenêtre bornée |
| lenteur | [profilage CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md#1-rôle-du-chapitre) | séparer CPU, GPU, mémoire et chargement |
| défaut visuel | [diagnostics 3D](CHAPITRE-18-Reference-graphique-et-3D.md#g3d-12--symptômes-visuels-diagnostics-et-acceptation) | source, export, import, scène ou rendu |
| défaut audio | [diagnostics audio](CHAPITRE-19-Reference-audio.md#audr-12--symptômes-diagnostics-et-acceptation) | source, encodage, bus, scène ou dispositif |
| perte ou corruption | [sauvegardes et reprise](../Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md#1-rôle-du-chapitre) | version, migration et empreinte |
| CI en échec | [index outils et CI](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md#diag-09--index-outils-dépendances-et-ci) | job minimal et artefact |
| export incorrect | [index livraison](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md#diag-11--index-performance-réseau-et-livraison) | preset, contenu et installation |
| doute de cause | [niveaux de certitude](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md#diag-01--vocabulaire-et-niveaux-de-certitude) | expérience contrôlée |
| correction supposée | [cause et vérification](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md#diag-08--cause-confirmée-contournement-correction-et-vérification) | test de non-régression |

**Réponse rapide :** indexer le signal exact et le contexte avant le composant supposé coupable. Une recherche par message doit aussi accepter une signature normalisée qui retire chemins, identifiants éphémères et valeurs sensibles.

**Diagramme compact :** `signal → terme diagnostique canonique → contexte/version → propriétaire → preuve suivante → conclusion bornée`.

**Confidentialité :** aucune entrée publique ne doit incorporer secret, jeton, nom de joueur, contrat, voix, image ou chemin restreint.

---

<!-- l5:card -->
## IDX-09 — Licences, provenance, conformité et publication

| Requête | Destination | Ce que l’index ne conclut pas |
|---|---|---|
| licence du code | [objets et couches](CHAPITRE-25-Licences-provenance-et-conformite.md#matrice-a--objets-couches-et-propriétaires) | compatibilité avec toute distribution |
| identifiant SPDX | [texte et expression](CHAPITRE-25-Licences-provenance-et-conformite.md#lic-02--texte-identifiant-et-expression-de-licence) | correspondance sans lecture du texte |
| `LicenseRef` | [licence personnalisée](CHAPITRE-25-Licences-provenance-et-conformite.md#lic-02--texte-identifiant-et-expression-de-licence) | autorisation générale |
| provenance d’asset | [chaîne de provenance](CHAPITRE-25-Licences-provenance-et-conformite.md#lic-04--chaîne-de-provenance-et-paquet-de-preuves) | titularité complète |
| voix ou image | [personnes et consentements](CHAPITRE-25-Licences-provenance-et-conformite.md#lic-05--personnes-consentements-et-données) | consentement pour tout usage |
| modèle ou dataset | [chaîne IA](CHAPITRE-25-Licences-provenance-et-conformite.md#lic-06--modèles-datasets-entrées-sorties-et-services-ia) | droits sur les sorties |
| attribution | [notices et paquet](CHAPITRE-25-Licences-provenance-et-conformite.md#lic-08--notices-attributions-sbom-et-paquet-de-publication) | conformité de la notice produite |
| publication | [porte de publication](CHAPITRE-24-Checklists-de-production-et-de-publication.md#chk-08--publication-distribution-et-support) | approbation réelle |
| accessibilité | [Livre IV, chapitre 18](../Livre-IV/CHAPITRE-18-Accessibilite.md) | certification |
| localisation | [Livre IV, chapitre 19](../Livre-IV/CHAPITRE-19-Localisation-et-internationalisation.md) | conformité de toutes les locales |
| modding | [Livre IV, chapitre 21](../Livre-IV/CHAPITRE-21-Modding-et-contenu-communautaire.md) | droit de redistribuer les sources |
| archivage | [Livre IV, chapitre 22](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md#4-modèle-mental-conserver-un-système-pas-seulement-un-zip) | durée légale universelle |
| licence globale | [LIC-12](CHAPITRE-25-Licences-provenance-et-conformite.md#lic-12--licence-de-collection-frontières-et-sources-officielles) | décision déjà prise |

**Réponse rapide :** l’index peut retrouver un texte ou une obligation ; seul le registre qualifié et son approbateur peuvent décider l’usage dans un périmètre donné.

**Limite :** `gratuit`, `open`, `royalty-free`, `public` et `généré` sont des termes de recherche, pas des statuts d’autorisation.

---

<!-- l5:card -->
## IDX-10 — Routes par besoin et parcours Solo/Studio

| Je veux… | Première étape | Puis | Porte finale |
|---|---|---|---|
| installer un outil | [fiche d’outil](CHAPITRE-03-Fiches-des-logiciels-et-outils.md) | tutoriel du Livre I | version et commande vérifiées |
| choisir une solution | [arbre de décision](CHAPITRE-02-Arbres-de-decision.md) | [compatibilité](CHAPITRE-22-Matrices-de-compatibilite.md) et [comparatif](CHAPITRE-23-Comparatifs-des-solutions.md) | décision conditionnelle |
| concevoir un système | [patron d’architecture](CHAPITRE-16-Patrons-d-architecture.md) | chapitre métier du Livre II | tests et propriété d’état |
| produire un asset | [route artistique](CHAPITRE-01-Carte-generale-de-la-collection.md) | production du Livre III | validation technique, artistique et provenance |
| intégrer un format | [fiche de format](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md) | propriétaire des données ou de l’asset | conversion et round-trip |
| mesurer | [méthode de benchmark](CHAPITRE-21-Benchmarks-et-methodes-de-mesure.md) | propriétaire du système | rapport daté et réserves |
| diagnostiquer | [catalogue](CHAPITRE-20-Catalogue-des-erreurs-et-diagnostics.md) | chapitre du Livre IV | cause ou statut d’incertitude |
| publier | [checklist](CHAPITRE-24-Checklists-de-production-et-de-publication.md) | [licences](CHAPITRE-25-Licences-provenance-et-conformite.md) | décision de porte |
| maintenir | [correctifs](../Livre-IV/CHAPITRE-20-Correctifs-mises-a-jour-et-retour-arriere.md) | [archivage](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md) | reprise et historique |
| travailler en Solo | route minimale, propriétaires regroupés | preuves explicites malgré les rôles cumulés | aucune mémoire personnelle comme preuve |
| travailler en Studio | registre central et RACI | séparation préparation, revue et approbation | décisions signées et réouvrables |

**Réponse rapide :** Solo et Studio partagent les mêmes autorités et oracles. Seuls les rôles, la séparation des responsabilités, la granularité du registre et l’automatisation diffèrent.

**Diagramme compact :** `besoin → route Livre V → procédure propriétaire → validation → preuve → décision → maintenance`.

**Frontière :** les formulaires exécutables, moteurs de recherche, bases d’index, exports et tableaux de bord appartiennent au [Companion Pack](../Companion-Pack/index.md).

---

<!-- l5:card -->
## IDX-11 — Navigation multiformat et accessibilité

| Support | Exigence de navigation | Contrôle spécifique |
|---|---|---|
| Markdown | chemins relatifs et fragments résolus | validateur de liens du dépôt |
| HTML | identifiants uniques, liens profonds, retour au contexte et recherche | génération puis test dans le navigateur |
| PDF | signets, table des matières, liens internes et externes, ordre de lecture | compilation, préflight et inspection |
| EPUB | table de navigation, ancres, chapitres et métadonnées | validation EPUB et lecture sur plusieurs moteurs |
| lecteur d’écran | titres hiérarchiques, libellés explicites et ordre logique | audit d’accessibilité du format produit |
| impression | destination compréhensible sans dépendre uniquement d’un survol | inspection des libellés et références |
| hors ligne | liens locaux complets et ressources incluses ou signalées | test depuis l’archive distribuée |
| recherche | terme canonique, variantes et contexte | scénarios de recherche connus |

**Réponse rapide :** un lien Markdown vert est une précondition, pas une preuve de navigation finale. Les publications PDF, HTML et EPUB restent dans [M8 — Publications](../ROADMAP.md#m8--publications).

**Diagramme compact :** `graphe Markdown validé → génération du format → contrôles propres au support → inspection assistive → publication`.

**Réserve :** aucun PDF, HTML ou EPUB du Livre V n’est produit ou inspecté dans ce lot. Le statut de cette carte reste documentaire jusqu’aux campagnes de publication.

---

<!-- l5:matrix -->
## Matrice C — Contrôles d’intégrité et actions

| Contrôle | Signal | Conclusion permise | Action |
|---|---|---|---|
| chemin local absent | fichier cible introuvable | lien cassé | corriger ou retirer avant fusion |
| fragment absent | titre ou ancre non résolu | lien profond cassé | viser une section existante ou une ancre stable |
| identifiant dupliqué | même ID pour deux entrées | collision d’identité | bloquer et renommer selon gouvernance |
| terme canonique dupliqué | deux autorités concurrentes | conflit à arbitrer | désigner propriétaire ou qualifier l’homonyme |
| alias en boucle | A → B → A | redirection invalide | pointer directement vers le canonique |
| cible `planned` liée comme présente | lien vers fichier absent | promesse trompeuse | afficher le statut sans faux lien |
| entrée sans propriétaire | aucune autorité nommée | candidat orphelin | rechercher, créer une tâche ou retirer |
| document sans lien entrant | aucun index ou parcours ne le référence | candidat orphelin seulement | vérifier rôle racine, annexe ou artefact volontaire |
| document sans lien sortant | aucune source, validation ou complément | isolation potentielle | revoir la frontière et les renvois |
| cible retirée encore active | route vers `deprecated` ou `retired` | navigation obsolète | rediriger vers successeur avec avertissement |
| différence de libellé | titre indexé différent de la cible | changement possible | confirmer renommage ou corriger la fiche |
| support non testé | Markdown seul validé | aucune conclusion PDF/HTML/EPUB | planifier la campagne du format |
| résultat contradictoire | outils ou corpus différents | indéterminé | conserver rapports et harmoniser le protocole |

**Décision :** « orphelin » est un statut d’investigation, pas une suppression automatique. Les racines, index, annexes, audits et artefacts peuvent légitimement avoir des degrés entrants différents.

---

<!-- l5:card -->
## IDX-12 — Maintenance, rapports d’intégrité et clôture

| Élément | Contrat de maintenance |
|---|---|
| corpus | chemins inclus, exclus et version du dépôt |
| générateur | outil, version, configuration et ordre déterministe |
| inventaire | fichiers, titres, identifiants, ancres, liens, termes et statuts |
| rapport | erreurs bloquantes, avertissements, candidats orphelins et exceptions |
| scénario | requête connue, résultat attendu, route réellement obtenue |
| responsable | propriétaire de l’index et propriétaires des sources |
| fréquence | à chaque renommage, déplacement, retrait, ajout de fiche ou publication |
| réouverture | lien cassé, nouvel homonyme, alias ambigu, cible retirée ou format changé |
| version | numéro de l’index, date, commit et prédécesseur |
| conservation | rapports utiles et décisions gardés sans accumuler les sorties temporaires |
| clôture | toutes les entrées bloquantes résolues ou explicitement reportées |
| publication | campagne séparée pour chaque format final |

**Réponse rapide :** le rapport d’intégrité doit permettre de reproduire le contrôle et de retrouver la source de chaque anomalie. Un compteur seul n’explique ni le corpus ni la gravité.

**Diagramme compact :** `inventaire → graphe de liens → contrôles → candidats orphelins → revue humaine → corrections → rapport versionné`.

**Critère documentaire de la fiche :** les 26 chapitres du Livre V sont rédigés, repérés et audités lorsque cette fiche et sa preuve QA sont fusionnées. La clôture éditoriale du Livre V ne vaut pas licence globale, publication multiformat, accessibilité avancée, validation runtime ou achèvement du Companion Pack.

## Sources propriétaires et frontières

- [Volume 0 — Architecture documentaire](../Volume-0/CHAPITRE-03-Architecture-documentaire.md) pour les autorités, identifiants et hiérarchies ;
- [Volume 0 — Production, validation et publication](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md) pour les portes et la définition de terminé ;
- [Livre I](../Livre-I/index.md) pour l’installation et la plateforme locale ;
- [Livre II](../Livre-II/index.md) pour l’architecture, les données, l’IA intégrée et les systèmes ;
- [Livre III](../Livre-III/index.md) pour les assets, médias et pipelines ;
- [Livre IV](../Livre-IV/index.md) pour la QA, le diagnostic, les performances, la publication et la maintenance ;
- [Livre V](index.md) pour les fiches de consultation ;
- [Companion Pack](../Companion-Pack/index.md) pour les outils, bases et exports exécutables.

## Réserves de validation

- aucune recherche utilisateur, campagne de scénarios ou mesure de temps de recherche n’a été exécutée ;
- aucun générateur d’index, moteur de recherche, graphe de connaissances ou base d’alias n’a été produit ;
- aucun rapport exhaustif de documents orphelins ou de couverture sémantique n’a été calculé ;
- la validation automatique du lot contrôle les chemins et fragments Markdown, pas la pertinence de chaque relation ;
- aucun PDF, HTML ou EPUB du Livre V n’a été généré, préflighté ou inspecté ;
- aucun contrôle d’accessibilité avancée du format final n’a été réalisé ;
- aucune licence globale de la collection n’a été décidée ;
- aucune donnée personnelle, contenu restreint, secret ou artefact confidentiel n’a été indexé.
