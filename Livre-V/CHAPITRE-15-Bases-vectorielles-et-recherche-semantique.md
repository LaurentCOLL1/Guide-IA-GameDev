---
title: "Livre V — Fiche 15 : Bases vectorielles et recherche sémantique"
id: "DOC-L5-CH15"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 15
last-verified: "2026-07-29T06:05:55+02:00"
audit-status: "complete"
audit-date: "2026-07-29T06:05:55+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-15.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "vector-search-and-semantic-retrieval-reference"
reference-ecosystem:
  qdrant: "1.18.2"
  faiss: "1.14.3"
  chroma: "1.5.9"
  sentence-transformers: "5.5.1"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Bases vectorielles et recherche sémantique

> **Type de document :** cartes de décision, contrats d’espace vectoriel, fiches de solutions, schémas de métadonnées, diagnostics et portes d’évaluation.
> **Référence documentaire :** Qdrant `1.18.2`, Faiss `1.14.3`, Chroma `1.5.9` et Sentence Transformers `5.5.1`, vérifiés le 29 juillet 2026.
> **Principe :** un index vectoriel est un artefact dérivé. Il ne remplace ni la source canonique, ni la politique d’accès, ni la preuve de pertinence, ni la sauvegarde métier.

## Index express

| Besoin | Ouvrir |
|---|---|
| définir le contrat d’un index | [VEC-00](#vec-00--contrat-dun-index-vectoriel) |
| choisir une famille de solution | [Matrice A](#matrice-a--sélection-par-besoin) |
| distinguer vecteur, espace, score et résultat | [VEC-01](#vec-01--vocabulaire-et-espace-vectoriel) |
| choisir modèle, dimensions et prétraitement | [VEC-02](#vec-02--embeddings-et-contrat-du-modèle) |
| choisir distance et normalisation | [Matrice B](#matrice-b--métriques-et-normalisation) |
| définir fragments, identifiants et révisions | [VEC-03](#vec-03--fragments-identifiants-et-révisions) |
| définir le payload et les droits | [VEC-04](#vec-04--métadonnées-provenance-et-visibilité) |
| organiser collections et vecteurs nommés | [VEC-05](#vec-05--collections-et-familles-de-vecteurs) |
| choisir recherche exacte ou ANN | [VEC-06](#vec-06--index-exacts-et-approximatifs) |
| appliquer les filtres sans perdre le contrat | [VEC-07](#vec-07--filtres-index-de-payload-et-sélectivité) |
| synchroniser ajouts, remplacements et suppressions | [VEC-08](#vec-08--ingestion-remplacement-et-suppression) |
| migrer ou réindexer sans rupture | [VEC-09](#vec-09--réindexation-staging-et-retour-arrière) |
| définir le corpus et les métriques | [Matrice C](#matrice-c--portes-de-benchmark-et-dacceptation) |
| évaluer la récupération | [VEC-10](#vec-10--corpus-évaluation-et-mesures) |
| comparer exact, Faiss, Chroma et Qdrant | [VEC-11](#vec-11--fiches-des-solutions-locales) |
| diagnostiquer et accepter | [VEC-12](#vec-12--diagnostics-sécurité-et-acceptation) |

---

<!-- l5:card -->
## VEC-00 — Contrat d’un index vectoriel

| Élément | Décision obligatoire |
|---|---|
| autorité | sources canoniques conservées hors de l’index |
| unité | document, fragment, image, audio ou objet métier encodé |
| modèle | identifiant, révision, licence, tokenizer, préfixes et dimensions |
| espace | dense, sparse, binaire ou multi-vecteurs |
| métrique | cosine, produit scalaire, distance euclidienne ou autre contrat explicite |
| stockage | mémoire, disque, processus local, serveur ou service distant |
| index | exact, HNSW, IVF, quantification ou combinaison qualifiée |
| métadonnées | provenance, langue, visibilité, tags, révision et version de schéma |
| identité | identifiant stable de source et identifiant de fragment |
| synchronisation | ajout, remplacement, suppression, reprise et idempotence |
| recherche | requête, filtres, limite, score, mode et provenance retournée |
| repli | lexical ou exact, construit indépendamment du modèle vectoriel |
| évaluation | corpus, vérité attendue, hit-rate, MRR, rappel, latence et ressources |
| sécurité | politique d’accès, confinement, données sensibles et journalisation |
| cycle de vie | staging, alias, réindexation, retour arrière et purge |
| preuve | versions réellement exécutées, paramètres, résultats, artefacts et réserves |

**Réponse rapide :** la [matrice d’autorité du chapitre propriétaire](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md#5-matrice-dautorité) place les sources et le manifeste du côté canonique, puis l’index, les embeddings et les résultats du côté reconstructible. La [fiche SQLite](CHAPITRE-14-Schemas-SQLite-et-migrations.md#sql-00--contrat-dune-base) reste propriétaire des données relationnelles ; la [fiche des formats](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#fmt-00--contrat-dun-format) conserve les enveloppes d’échange.

---

<!-- l5:matrix -->
## Matrice A — Sélection par besoin

| Besoin | Point de départ | Atout | Limite structurante | Source propriétaire |
|---|---|---|---|---|
| petit corpus, oracle exact | balayage exact en mémoire | résultat déterministe et référence de vérité | coût linéaire | [évaluer la récupération](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md#22-évaluer-la-récupération) |
| bibliothèque bas niveau et index spécialisés | Faiss | large choix d’index denses, exacts et ANN | métadonnées et persistance à composer | [contrat de l’index](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md#16-contrat-de-lindex) |
| prototype applicatif local avec documents | Chroma | collection, embeddings, documents et filtres dans une API intégrée | contrat de stockage et migrations à qualifier | [architecture de référence](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md#6-architecture-de-référence) |
| recherche filtrée, payloads, dense et sparse | Qdrant | collections, HNSW filtrable, payloads et modes local/serveur | exploitation et compatibilité à versionner | [choix de référence](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md#7-choix-de-référence) |
| état métier transactionnel | SQLite | contraintes, jointures et transactions | pas un moteur sémantique par défaut | [fiche SQLite](CHAPITRE-14-Schemas-SQLite-et-migrations.md#matrice-a--sélection-par-besoin) |
| échange ou corpus versionné | JSON, JSONL ou Markdown validé | autorité lisible et diffable | index à reconstruire | [formats d’échange](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#matrice-a--sélection-par-besoin) |
| appel depuis Godot | service sous contrat | séparation moteur, politique et runtime | latence et panne réseau à traiter | [communication Godot–IA](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md) |
| API ou file de tâches | service HTTP, WebSocket ou worker | isolation et observabilité | sécurité et reprise obligatoires | [protocoles et files](../Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md) |

**Décision :** commencer par l’oracle exact et le corpus d’évaluation. Choisir ensuite un backend selon filtres, volume, mises à jour, mémoire, disque, plateforme et exploitation ; ne jamais choisir uniquement sur un benchmark public ou une popularité.

---

<!-- l5:card -->
## VEC-01 — Vocabulaire et espace vectoriel

| Notion | Définition de référence | Piège |
|---|---|---|
| source canonique | contenu d’autorité versionné et validé | stocker l’unique copie dans le payload |
| fragment | unité autonome produite par une stratégie de découpage | confondre longueur en caractères et tokens |
| embedding | représentation numérique produite par un modèle | le traiter comme une signification universelle |
| dimension | nombre de composantes du vecteur | réutiliser une collection de dimension différente |
| espace vectoriel | modèle, révision, prétraitement, dimension et métrique réunis | ne versionner que le nom du modèle |
| point | identifiant, vecteur et métadonnées | utiliser un ordinal instable comme identité métier |
| distance | mesure géométrique à minimiser | l’afficher comme probabilité |
| similarité | score à maximiser selon un contrat | comparer des scores issus de métriques différentes |
| voisin exact | meilleur résultat après comparaison exhaustive | supposer qu’un ANN le retourne toujours |
| voisin approximatif | candidat trouvé avec compromis vitesse–rappel | omettre le rappel face à l’oracle exact |
| dense | presque toutes les dimensions portent une valeur | supposer qu’il capture chaque attribut structuré |
| sparse | peu de dimensions non nulles | le traiter comme un dense compressé |
| hybride | combinaison de signaux dense, sparse ou lexical | fusionner des rangs sans protocole |
| reranking | seconde passe plus coûteuse sur un petit ensemble | l’utiliser sans conserver le classement initial |

Le [vocabulaire propriétaire](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md#4-vocabulaire) rappelle qu’un score élevé n’est ni une probabilité ni une preuve de vérité. Le [repli lexical](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md#19-repli-lexical-déterministe) reste un mode distinct, pas une recherche sémantique déguisée.

---

<!-- l5:card -->
## VEC-02 — Embeddings et contrat du modèle

| Champ | Valeur à enregistrer |
|---|---|
| fournisseur | projet, organisation ou dépôt d’origine |
| identifiant | nom exact du modèle ou chemin local |
| révision | tag, commit, hash ou digest réellement chargé |
| licence | modèle, poids, code et éventuelles restrictions |
| modalité | texte, image, audio ou multi-modal |
| langues | langues revendiquées et langues réellement évaluées |
| tokenizer | identité, révision et limite de positions |
| préparation | préfixes, gabarit, casse, normalisation et troncature |
| pooling | stratégie de réduction des représentations |
| dimension | dimension brute ou dimension tronquée qualifiée |
| type numérique | `float32`, `float16`, `int8`, binaire ou autre |
| normalisation | aucune, L2 ou traitement spécifique |
| métrique attendue | cosine, produit scalaire ou distance entraînée |
| runtime | bibliothèque, version, backend CPU/GPU et plateforme |
| empreinte | hash des fichiers et du manifeste de modèle |

**Réponse rapide :** changer le modèle, sa révision, ses préfixes, son tokenizer, sa dimension ou sa normalisation change potentiellement l’espace. La [configuration typée du chapitre 10](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md#10-configuration-typée) et son [fournisseur d’embeddings](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md#15-fournisseur-dembeddings) montrent le contrat E5 de référence sans en faire une règle universelle. Les environnements restent gouvernés par le [chapitre Python du Livre I](../Livre-I/CHAPITRE-04-Python-et-environnements-virtuels.md) et la [référence Python](CHAPITRE-12-Reference-Python.md#py-01--interpréteur-environnement-et-projet).

**Versions repères :** Sentence Transformers `5.5.1` est une bibliothèque d’inférence et d’évaluation, pas l’identité du modèle. Sa documentation distingue cosine, produit scalaire, euclidienne, Manhattan et MaxSim ; le modèle doit indiquer la fonction pertinente.

---

<!-- l5:matrix -->
## Matrice B — Métriques et normalisation

| Contrat | Classement | Précondition | Usage fréquent | Contrôle minimal |
|---|---|---|---|---|
| cosine | similarité décroissante | normes non nulles ; normalisation explicite ou gérée par le backend | orientation sémantique | vecteurs colinéaires classés ensemble |
| produit scalaire | score décroissant | norme porte éventuellement de l’information | modèles entraînés pour IP ou vecteurs normalisés | vérifier l’effet de la norme |
| L2 | distance croissante | unités et échelle cohérentes | géométrie euclidienne, Faiss `FlatL2` | identité à distance nulle |
| L2 au carré | distance croissante | même classement que L2 positif | sorties de plusieurs bibliothèques | ne pas comparer la valeur à L2 non carrée |
| Manhattan | distance croissante | contrat explicitement supporté | cas spécialisés et diagnostics | somme des écarts absolus |
| cosine sur vecteurs L2-normalisés | équivalent de classement au produit scalaire | normalisation identique des documents et requêtes | optimisation de recherche | normes proches de `1` |
| distance backend | sens dépendant de l’API | documentation et version enregistrées | résultat natif | nommer `distance` ou `similarity`, jamais `confidence` |

**Pièges :** zéro vector interdit pour cosine ; mélange `float32`/quantifié à qualifier ; score non comparable entre collections, modèles, métriques ou versions ; seuil absolu à calibrer sur le corpus, pas à copier d’un exemple.

---

<!-- l5:card -->
## VEC-03 — Fragments, identifiants et révisions

| Élément | Contrat recommandé |
|---|---|
| `source_id` | identifiant stable de la source canonique |
| `source_path` | chemin relatif validé et confiné |
| `chunk_id` | identifiant déterministe dérivé de source, structure, ordinal et contenu |
| `heading_path` | chemin de titres ou contexte local |
| `ordinal` | position dans la révision, jamais identité unique isolée |
| `content_sha256` | empreinte du texte exact encodé |
| `source_revision` | empreinte ou version de la source entière |
| `chunker_version` | stratégie, paramètres et tokenizer |
| `token_count` | nombre produit par le tokenizer réel |
| `created_at` | horodatage informatif, non substitut d’identité |
| `tombstone` | état explicite si le backend ou la réplication l’exige |

Le [découpage déterministe](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md#14-découpage-déterministe) conserve les titres, compte avec le tokenizer et refuse la perte silencieuse. Les identifiants et schémas d’échange restent alignés sur les [contrats JSON](CHAPITRE-13-Structures-JSON-et-formats-d-echange.md#fmt-04--identité-versions-et-évolution).

**Décision :** une modification de stratégie de découpage exige un nouvel identifiant de stratégie et généralement une réindexation complète. Une simple mise à jour de payload ne doit pas masquer un vecteur calculé depuis un texte ancien.

---

<!-- l5:card -->
## VEC-04 — Métadonnées, provenance et visibilité

| Champ de payload | Type logique | Obligatoire | Rôle |
|---|---|---:|---|
| `source_id` | texte stable | oui | remplacement et suppression par source |
| `source_path` | texte relatif | oui | retour à l’autorité |
| `chunk_id` | UUID ou texte stable | oui | identité du point |
| `text` ou référence | texte ou pointeur | selon architecture | passage présenté au lecteur |
| `title` | texte | oui | contexte lisible |
| `heading_path` | tableau de textes | recommandé | localisation dans la source |
| `language` | code de langue | oui | filtre et évaluation |
| `visibility` | enum fermée | oui | politique minimale d’accès |
| `tenant_id` | identifiant stable | si multi-tenant | partition logique ou physique |
| `tags` | ensemble de textes | optionnel | filtres métier contrôlés |
| `source_revision` | hash ou version | oui | détection d’obsolescence |
| `content_sha256` | hash | oui | intégrité du fragment |
| `embedding_model` | identifiant + révision | oui | compatibilité de l’espace |
| `vector_size` | entier | oui | diagnostic de collection |
| `distance` | enum | oui | interprétation du score |
| `index_schema_version` | entier ou semver | oui | migration du payload |
| `license_id` | identifiant | selon corpus | provenance et redistribution |
| `retention_class` | enum | si données gouvernées | purge et conservation |

La visibilité vient d’une politique fiable, jamais d’une valeur libre de la requête. Le [chapitre de sécurité IA](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md) conserve les frontières production/runtime ; la [sécurité de la plateforme](../Livre-I/CHAPITRE-10-Securite-sauvegarde-et-validation-de-la-plateforme.md) conserve secrets, provenance et validation. L’index ne rend pas une donnée licite, exacte ou redistribuable.

---

<!-- l5:card -->
## VEC-05 — Collections et familles de vecteurs

| Choix | Quand l’utiliser | Réserve |
|---|---|---|
| une collection par espace | modèle, dimension et métrique homogènes | solution par défaut lisible |
| vecteurs nommés | plusieurs modalités ou représentations par point | contrat et disponibilité propres à chaque nom |
| collection par version | migration incompatible ou comparaison A/B | coût de stockage et synchronisation |
| partition par payload | nombreux groupes partageant le même espace | indexer le champ de filtre et auditer l’isolation |
| collection par tenant | faible nombre de tenants nécessitant isolation | surcharge de collections |
| dense + sparse | récupération hybride | fusion, pondération et évaluation obligatoires |
| collection sans vecteur | payload ou orchestration spécifique | ne pas la présenter comme recherche dense |

Qdrant impose une dimension et une métrique par vecteur d’une collection et permet des vecteurs nommés. Chroma exige que la dimension de la requête corresponde à celle de la collection. Faiss construit chaque index pour une dimension fixe. Ces ressemblances ne garantissent ni format de fichier commun, ni migration directe, ni équivalence de score.

**Convention :** nommer la collection avec domaine, modalité, modèle ou génération, par exemple `asteria_knowledge_text_v2`; conserver le détail complet dans un manifeste, pas seulement dans le nom.

---

<!-- l5:card -->
## VEC-06 — Index exacts et approximatifs

| Famille | Exactitude | Construction | Mémoire | Paramètres clés | Usage |
|---|---:|---:|---:|---|---|
| balayage exact | exacte | nulle | vecteurs bruts | batch, métrique | oracle et petits corpus |
| Flat Faiss | exacte | faible | élevée | L2 ou IP, type `float32` | référence CPU et batch |
| HNSW | approximative | progressive | graphe en plus des vecteurs | `m`, `ef_construct`, `ef` | faible latence et mises à jour |
| IVF | approximative | entraînement requis | listes inversées | nombre de listes, `nprobe` | gros corpus et lots |
| PQ / quantification | approximative | entraînement ou calibration | réduite | sous-vecteurs, bits, rescore | mémoire ou disque contraints |
| index disque | selon famille | plus coûteuse | RAM réduite | cache, mmap, IO | corpus dépassant la RAM |
| sparse inversé | exact ou spécifique au backend | index lexical/sparse | dépend de la sparsité | tokenizer, IDF | termes rares et hybridation |

Faiss rappelle que seul un index `Flat` garantit le résultat exact ; ses autres familles échangent vitesse, mémoire, entraînement et qualité. Qdrant utilise HNSW pour le dense et peut effectuer une recherche exacte sur demande. Chroma expose des espaces L2, cosine ou produit interne selon sa configuration ; le backend concret et ses paramètres restent à épingler.

**Décision :** conserver un oracle exact sur un sous-corpus ou un corpus de validation. Mesurer le rappel de l’ANN face à cet oracle avant d’optimiser la latence.

---

<!-- l5:card -->
## VEC-07 — Filtres, index de payload et sélectivité

| Question | Contrôle |
|---|---|
| le filtre exprime-t-il une règle non encodable ? | langue, tenant, visibilité, date, tag ou état restent structurés |
| le champ est-il indexé ? | créer l’index de payload avant l’ingestion lorsque le backend le recommande |
| la cardinalité est-elle connue ? | mesurer valeurs uniques et distribution |
| le filtre est-il très strict ? | comparer ANN filtré, exact filtré et stratégie dédiée |
| plusieurs filtres se combinent-ils ? | mesurer rappel et latence de la combinaison réelle |
| le filtre vient-il de l’appelant ? | dériver les droits depuis identité et politique |
| le champ est-il absent ou nul ? | définir sémantique et requêtes de diagnostic |
| le résultat est-il vide ? | distinguer aucun voisin, filtre trop strict et panne |

Qdrant combine index vectoriel et index de payload ; sa documentation recommande de créer les index de payload avant l’ingestion afin que le graphe filtrable soit construit avec eux. Chroma fournit des filtres de métadonnées avec comparaisons, inclusion et opérateurs logiques. Faiss peut restreindre des identifiants selon certains index, mais n’est pas une base de métadonnées complète.

**Piège :** post-filtrer un petit `top_k` peut supprimer tous les résultats pertinents ; pré-filtrer peut réduire le graphe ; filtrer pendant la recherche dépend du backend. La stratégie appartient au benchmark du corpus réel.

---

<!-- l5:card -->
## VEC-08 — Ingestion, remplacement et suppression

| Opération | Contrat |
|---|---|
| validation | refuser source, chemin, schéma, visibilité ou dimension invalides avant écriture |
| découpage | produire des fragments déterministes et bornés |
| embedding | calculer par lots, conserver modèle et révision |
| upsert | idempotent pour un même `chunk_id` et même contenu |
| remplacement | retirer ou désactiver tous les points de l’ancienne révision de la source |
| suppression | propager toute source retirée du manifeste |
| contrôle | comparer sources déclarées, points indexés et révisions |
| journal | enregistrer compteurs, durée, erreurs et version du pipeline |
| reprise | définir frontière de lot, répétition sûre et état partiel |
| purge | traiter tombstones, segments, caches et rétention selon le backend |

Le [chapitre propriétaire synchronise créations, modifications et suppressions](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md#18-synchroniser-créations-modifications-et-suppressions) en comparant identifiants déclarés et indexés. Les outils réels appartiennent au [chapitre d’automatisation Python](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md) et au Companion Pack.

**Réserve :** supprimer puis insérer peut créer une fenêtre vide. Pour une disponibilité continue, construire une génération de staging, la vérifier, basculer un alias ou pointeur, puis conserver temporairement la génération précédente.

---

<!-- l5:card -->
## VEC-09 — Réindexation, staging et retour arrière

| Déclencheur | Action minimale |
|---|---|
| modèle ou révision changé | nouvelle génération complète |
| dimension ou métrique changée | nouvelle collection ou nouvel index |
| tokenizer ou chunker changé | redécoupage et réembedding complets |
| payload compatible enrichi | migration ou backfill qualifié |
| index ANN paramétré différemment | reconstruction et comparaison face à l’oracle |
| licence ou source retirée | purge des points, caches, snapshots et dérivés concernés |
| faille ou corruption | isoler, restaurer les sources, reconstruire et réévaluer |
| régression de qualité | revenir à l’alias précédent et conserver les preuves |

**Patron :** `sources validées → génération de staging → contrôles de comptes et schéma → corpus d’évaluation → mesures de ressources → bascule atomique → observation → purge différée`.

Le retour arrière et les correctifs restent gouvernés par [Livre IV, chapitre 20](../Livre-IV/CHAPITRE-20-Correctifs-mises-a-jour-et-retour-arriere.md). Les sauvegardes et restaurations appartiennent à [Livre IV, chapitre 15](../Livre-IV/CHAPITRE-15-Sauvegardes-migrations-et-reprise-apres-incident.md). Sauvegarder seulement l’index n’est pas un substitut à la conservation des sources, manifestes, versions et recettes de reconstruction.

---

<!-- l5:matrix -->
## Matrice C — Portes de benchmark et d’acceptation

| Porte | Mesure | Condition à déclarer | Échec typique |
|---|---|---|---|
| corpus | nombre de sources, fragments, langues et distributions | version et hash | corpus modifié entre deux essais |
| vérité | résultats pertinents par requête | méthode d’annotation | un seul positif incomplet |
| exactitude | hit-rate@k, recall@k, MRR, nDCG selon besoin | oracle exact et gestion des égalités | score moyen sans rang |
| filtres | rappel et faux accès par politique | combinaisons réelles | filtre testé séparément seulement |
| ingestion | points/s, durée, erreurs et idempotence | batch, threads et disque | cache chaud non déclaré |
| construction | temps et mémoire de l’index | paramètres ANN | temps exclu du comparatif |
| requête | médiane, p95, p99 et débit | concurrence, warm-up, top-k | une seule moyenne |
| ressources | RAM, VRAM, disque, CPU et IO | plateforme et versions | mémoire du processus ignorée |
| fraîcheur | délai modification → résultat visible | frontière de cohérence | ancienne révision toujours trouvable |
| suppression | délai et exhaustivité de purge | caches et snapshots inclus | tombstone encore accessible |
| reprise | temps de reconstruction et de bascule | panne simulée et point de départ | copie non restaurée |
| hors ligne | démarrage et recherche sans réseau | caches préchargés déclarés | téléchargement implicite |
| sécurité | visibilité, tenant et données sensibles | identité et politique | droits fournis par la requête |
| reproductibilité | graines, versions, commandes et artefacts | environnement figé | conclusion sans données brutes |

Le protocole de campagne relève de la [stratégie QA](../Livre-IV/CHAPITRE-02-Strategie-generale-d-assurance-qualite.md), des [tests de régression](../Livre-IV/CHAPITRE-03-Tests-fonctionnels-et-tests-de-regression.md), de l’[observabilité locale](../Livre-IV/CHAPITRE-05-Journalisation-et-observabilite-locale.md), du [profilage CPU](../Livre-IV/CHAPITRE-06-Profilage-CPU.md) et du [profilage mémoire](../Livre-IV/CHAPITRE-08-Optimisation-RAM-VRAM-et-allocations.md).

---

<!-- l5:card -->
## VEC-10 — Corpus, évaluation et mesures

| Artefact | Contenu minimal |
|---|---|
| manifeste de corpus | format, version, sources, langues, licences et hashes |
| cas de recherche | identifiant, requête, filtres et résultats attendus |
| jugements | pertinent, partiellement pertinent ou non pertinent selon protocole |
| oracle exact | classement exhaustif sur les mêmes vecteurs et filtres |
| run manifest | backend, version, paramètres, plateforme, date et graine |
| résultats bruts | rangs, identifiants, scores, durées et erreurs par requête |
| agrégats | hit-rate, recall, MRR, nDCG, percentiles et intervalles si pertinents |
| ressources | mémoire maximale, disque, CPU, durée de construction et ingestion |
| comparaison | delta face à la baseline, réserves et décision |

**Formules de lecture :** `hit@k` vérifie au moins un résultat attendu dans les `k` premiers ; `recall@k` mesure la part des pertinents retrouvés ; `MRR` utilise l’inverse du rang du premier pertinent ; `nDCG` accepte plusieurs degrés de pertinence. Aucun de ces nombres ne mesure la vérité du contenu.

Le [chapitre 10 exige hit-rate et MRR](../Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md#29-critères-dacceptation). Le [chapitre 27 du Livre II](../Livre-II/CHAPITRE-27-Tests-unitaires-tests-d-integration-et-simulations.md) conserve les suites exécutables et le [chapitre 28](../Livre-II/CHAPITRE-28-Journalisation-diagnostic-et-reproductibilite.md) conserve les journaux et la reproductibilité. La fiche 21 du Livre V possédera les campagnes comparatives complètes.

---

<!-- l5:card -->
## VEC-11 — Fiches des solutions locales

| Solution | Profil | Index et métriques | Métadonnées et filtres | Persistance | Licence | Quand l’évaluer |
|---|---|---|---|---|---|---|
| exact Python/NumPy | oracle de petite taille | comparaison exhaustive | à implémenter explicitement | fichier ou mémoire au choix | dépend du code et de NumPy | baseline, tests et diagnostic |
| Faiss `1.14.3` | bibliothèque C++/Python spécialisée | Flat exact, HNSW, IVF, PQ et autres | filtrage et stockage applicatifs à composer | sérialisation d’index selon famille | MIT | contrôle fin, lots, index spécialisés |
| Chroma `1.5.9` | infrastructure de recherche applicative | dense, espaces L2/cosine/IP selon configuration | documents, métadonnées, filtres et recherche textuelle | local ou service selon déploiement | Apache-2.0 | prototype intégré et API de collection |
| Qdrant `1.18.2` | moteur de recherche vectorielle | dense HNSW, exact, sparse, hybridation et quantification | payloads, index de payload, filtres et multi-tenancy | local, Edge ou serveur selon composant | Apache-2.0 | filtres riches, lifecycle et évolution vers service |
| Sentence Transformers `5.5.1` | bibliothèque d’embeddings et d’évaluation | produit des vecteurs ; plusieurs similarités | aucune base durable par elle-même | cache de modèles à gouverner | Apache-2.0 | génération, reranking et évaluateurs |

**Faiss :** vecteurs de dimension fixe, matrices `float32` dans l’API de référence, contrôle fin mais contrat de payload externe. **Chroma :** collection, fonction d’embedding optionnelle, documents et filtres intégrés ; épingler configuration et version. **Qdrant :** une collection associe points, vecteurs et payloads ; indexer les champs filtrés avant ingestion lorsque possible. **Sentence Transformers :** la version de bibliothèque ne remplace jamais le nom, la révision et la licence du modèle.

Sources officielles : [Qdrant — collections](https://qdrant.tech/documentation/manage-data/collections/), [indexation](https://qdrant.tech/documentation/manage-data/indexing/), [filtres](https://qdrant.tech/documentation/search/filtering/), [recherche](https://qdrant.tech/documentation/search/search/) et [quantification](https://qdrant.tech/documentation/quantization/) ; [Faiss — présentation](https://github.com/facebookresearch/faiss/wiki), [démarrage](https://github.com/facebookresearch/faiss/wiki/getting-started) et [choix d’index](https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index) ; [Chroma — collections](https://docs.trychroma.com/docs/collections/manage-collections), [configuration](https://docs.trychroma.com/docs/collections/configure), [requêtes](https://docs.trychroma.com/docs/querying-collections/query-and-get) et [filtres](https://docs.trychroma.com/docs/querying-collections/metadata-filtering) ; [Sentence Transformers — fonctions de similarité](https://www.sbert.net/docs/package_reference/util/similarity.html).

Versions et licences vérifiées sur les dépôts officiels : [Qdrant](https://github.com/qdrant/qdrant/releases), [Faiss](https://github.com/facebookresearch/faiss/releases), [Chroma](https://github.com/chroma-core/chroma/releases) et [Sentence Transformers](https://github.com/huggingface/sentence-transformers/releases). La fiche ne qualifie pas leur installation, leur stockage sur disque, leur API binaire ou leur performance sur Project Asteria.

---

<!-- l5:card -->
## VEC-12 — Diagnostics, sécurité et acceptation

| Symptôme | Vérification | Cause possible | Action |
|---|---|---|---|
| dimension refusée | modèle, révision, collection et taille | espace incompatible | nouvelle collection et réindexation |
| scores inversés | métrique, sens et API | distance lue comme similarité | normaliser le contrat de sortie |
| résultats anciens | `source_revision`, `content_sha256`, compteurs | remplacement incomplet | purger la source puis reconstruire |
| source supprimée retrouvée | manifeste contre points indexés | suppression non propagée | supprimer par `source_id`, caches inclus |
| aucun résultat | filtres, langue, tags, top-k et corpus | filtre trop strict ou corpus absent | tester exact sans filtre puis réintroduire |
| baisse de rappel ANN | oracle exact et paramètres | `ef`, `nprobe`, quantification ou filtre | restaurer baseline et retuner |
| latence instable | p95/p99, IO, optimisations et concurrence | index en reconstruction ou cache froid | séparer phases et enregistrer l’état |
| mémoire excessive | vecteurs, graphe, payload et cache | dimension ou index surdimensionné | mesurer avant on-disk ou quantification |
| fuite de données | identité, visibilité et tenant | droits contrôlés par l’appelant | imposer la politique côté service |
| panne hors ligne | cache modèle et dépendances | téléchargement implicite | précharger, inventorier et tester sans réseau |
| score présenté comme vérité | UI et contrat de résultat | confusion similarité/confiance | afficher passage, source et réserve |
| index impossible à restaurer | manifeste, sources, versions et recette | seul l’artefact dérivé a été conservé | restaurer l’autorité puis reconstruire |

**Porte d’acceptation de la fiche :**

| Contrôle | Statut requis |
|---|---|
| sources canoniques distinctes de l’index | documenté |
| modèle, dimension, métrique et normalisation | enregistrés |
| schéma de métadonnées et politique d’accès | définis |
| exact contre ANN | protocole prévu |
| ajouts, remplacements et suppressions | idempotents et vérifiables |
| staging, bascule et retour arrière | définis pour une migration incompatible |
| corpus reproductible et métriques | versionnés |
| versions et licences des composants | inventoriées |
| runtime réellement exécuté | séparé de la revue documentaire |
| Godot, réseau, GPU et production non exécutés | réserves visibles |

La maintenance à long terme relève de [Livre IV, chapitre 22](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md). Les diagnostics détaillés rejoindront la fiche 20, les benchmarks la fiche 21, les matrices de compatibilité la fiche 22 et les licences la fiche 25. Le Companion Pack conservera les corpus, scripts, manifests, environnements verrouillés et backends réellement qualifiés.

## Réserves de preuve

- revue documentaire effectuée le 29 juillet 2026 ;
- aucune installation de Qdrant, Faiss, Chroma, Sentence Transformers ou modèle d’embedding revendiquée dans la fiche ;
- aucune collection réelle, index ANN, quantification, payload index ou migration backend exécuté ;
- aucun corpus utilisateur, secret, donnée personnelle ou fichier du Companion Pack traité ;
- aucun appel Godot, HTTP, WebSocket, conteneur, GPU, serveur ou service distant exécuté ;
- la campagne temporaire associée peut seulement qualifier des contrats mathématiques et de lifecycle sur vecteurs synthétiques ;
- aucune performance matérielle ou supériorité de solution n’est revendiquée ;
- aucun PDF produit ; licence globale et accessibilité avancée de la collection restent ouvertes.
