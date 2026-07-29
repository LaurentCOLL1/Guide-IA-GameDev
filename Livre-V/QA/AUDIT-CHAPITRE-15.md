---
title: "Audit — Livre V, Fiche 15 : Bases vectorielles et recherche sémantique"
id: "DOC-L5-QA-AUDIT-CH15"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 15
last-verified: "2026-07-29T06:18:10+02:00"
audit-date: "2026-07-29T06:18:10+02:00"
audit-level: "static-review"
validation-authority: "livre-v-reference-profile"
---

# Audit — Fiche 15 : Bases vectorielles et recherche sémantique

## 1. Décision

La fiche est conforme au profil spécialisé du Livre V au niveau `static-review`. Elle fournit une référence non linéaire des espaces vectoriels, modèles d’embeddings, métriques, index exacts et approximatifs, filtres, collections, cycles de vie, solutions locales, corpus et mesures de récupération.

Une campagne temporaire a réellement exécuté 43 contrôles déterministes sur des vecteurs synthétiques avec la bibliothèque standard Python. Elle qualifie les formules, classements exacts, filtres, identités, remplacements, suppressions, générations et métriques d’évaluation exercés. Elle ne qualifie ni Qdrant, ni Faiss, ni Chroma, ni Sentence Transformers, ni un modèle d’embedding.

## 2. Périmètre contrôlé

| Domaine | Couverture | Propriétaire conservé |
|---|---|---|
| autorité | source canonique, index dérivé et reconstruction | Livre II, chapitre 10 |
| espace vectoriel | modèle, révision, préparation, dimension, métrique et normalisation | fournisseur d’embeddings |
| fragmentation | tokenizer, identités, hashes et stratégie versionnée | pipeline du Livre II |
| métadonnées | provenance, langue, visibilité, tenant, licence et rétention | politiques du projet |
| collections | espaces homogènes, vecteurs nommés, dense, sparse et hybride | backend qualifié |
| index | exact, Flat, HNSW, IVF, PQ, disque et sparse | fiche 21 pour les campagnes |
| filtres | payload, index structurés, sélectivité et droits | service d’autorisation |
| cycle de vie | upsert, remplacement, suppression, idempotence et purge | Companion Pack |
| migration | staging, bascule, observation et retour arrière | Livre IV |
| évaluation | hit@k, recall@k, MRR, nDCG, latence et ressources | corpus reproductible |
| solutions | exact, Faiss, Chroma, Qdrant et Sentence Transformers | fiche 23 pour le comparatif global |
| sécurité | droits, données sensibles, hors ligne et provenance | Livres I, II et IV |

## 3. Conformité Livre V

- `document-format: "reference-cards"` présent ;
- treize marqueurs `l5:card` et trois marqueurs `l5:matrix` ;
- index express placé avant les cartes ;
- tables de décision placées avant les paragraphes ;
- 28 renvois vers les Livres I à IV, dont 12 liens profonds ;
- 17 liens vers les documentations ou dépôts officiels ;
- aucun bloc de code ou de commande ;
- aucune installation, configuration Qdrant ou pipeline pédagogique recopié ;
- distinctions explicites entre distance, similarité, probabilité et vérité ;
- niveaux de preuve et limites visibles.

## 4. Couverture du plan maître

| Exigence | Réponse |
|---|---|
| concepts et métriques | VEC-01, VEC-02 et Matrice B |
| solutions locales | VEC-11 |
| index et stockage | VEC-05 et VEC-06 |
| filtres | VEC-04 et VEC-07 |
| embeddings | VEC-02 |
| paramètres et diagnostics | VEC-06, VEC-07 et VEC-12 |
| suppression et réindexation | VEC-08 et VEC-09 |
| fiches solutions | VEC-11 |
| matrice de choix | Matrice A |
| jeux de benchmark | Matrice C et VEC-10 |
| schéma de métadonnées | VEC-04 |
| corpus reproductible | protocole VEC-10 et campagne synthétique 43/43 |

## 5. Exactitude technique statique

Les sources officielles ont été revues le 29 juillet 2026 : Qdrant `1.18.2`, Faiss `1.14.3`, Chroma `1.5.9` et Sentence Transformers `5.5.1`. Ces versions sont des références documentaires, pas des versions installées ou exécutées dans le dépôt.

La fiche distingue notamment :

- source canonique, fragment, embedding, point, payload et résultat ;
- modèle, bibliothèque d’inférence et backend vectoriel ;
- dimension, métrique, normalisation et type numérique ;
- distance à minimiser et similarité à maximiser ;
- recherche exhaustive et voisinage approximatif ;
- dense, sparse, hybride et reranking ;
- identité stable, ordinal, révision et hash de contenu ;
- collection, génération, alias et espace incompatible ;
- filtre structuré, autorisation et post-filtrage ;
- suppression logique, purge et reconstruction ;
- hit-rate, rappel, MRR, nDCG et vérité du contenu.

## 6. Campagne temporaire vectorielle

Le run spécialisé `30422132646` a exécuté 43 cas, tous réussis, sur `Linux-6.17.0-1020-azure-x86_64-with-glibc2.39` avec :

- Python `3.12.3` ;
- implémentation `CPython` ;
- backend de fixture `python-stdlib-exact-synthetic` ;
- durée rapportée `5.677 ms` ;
- réseau désactivé ;
- aucun modèle chargé ;
- aucun backend vectoriel chargé ;
- aucune donnée utilisateur traitée.

Familles exercées :

- produit scalaire, norme, normalisation, cosine, L2 au carré et Manhattan ;
- vecteur nul, dimensions incompatibles et métrique inconnue ;
- classements cosine et L2, limite `top_k` et égalités stables ;
- filtres de visibilité, langue et tags ;
- provenance et identifiants déterministes ;
- upsert idempotent, remplacement et suppression par source ;
- détection des sources obsolètes ;
- staging, bascule d’alias et retour arrière ;
- hit@k, recall@k, reciprocal rank, MRR et nDCG ;
- fusion Reciprocal Rank Fusion ;
- hash de corpus, répertoire isolé et manifeste runtime.

## 7. Échecs préparatoires tracés

1. Le run `30421674690` s’est arrêté avant exécution : 43 cas étaient enregistrés pour un garde-fou réglé à 42. Le seuil a été aligné sans retirer de cas.
2. Le run `30421801067` s’est arrêté avant exécution : le wrapper d’import dynamique n’avait pas inscrit le module dans `sys.modules`, exigence visible de `dataclasses` sous Python 3.12. Le wrapper a été corrigé sans modifier les cas.
3. Le run `30421858796` a exécuté les 43 cas avec 43 réussites et zéro échec.
4. Le run `30422132646` a rejoué les 43 cas avec succès et a figé les métriques structurelles et l’empreinte du chapitre.

Aucun résultat partiel ou préparatoire n’est présenté comme une qualification réussie.

## 8. Métriques documentaires

| Mesure | Valeur |
|---|---:|
| lignes | 424 |
| titres | 19 |
| cartes | 13 |
| matrices | 3 |
| liens Markdown | 67 |
| renvois Livres I à IV | 28 |
| liens profonds | 12 |
| liens officiels | 17 |
| blocs clôturés | 0 |
| fixtures synthétiques | 43 |
| fixtures réussies | 43 |

## 9. Frontières préservées

- le pipeline complet, Qdrant local, le modèle E5 et le repli lexical restent au Livre II, chapitre 10 ;
- l’appel depuis Godot reste au chapitre 11 du Livre II ;
- HTTP, WebSocket et files de tâches restent au chapitre 12 ;
- le durcissement production/runtime reste au chapitre 13 ;
- les campagnes comparatives complètes restent à la fiche 21 ;
- les matrices de compatibilité restent à la fiche 22 ;
- les comparatifs globaux restent à la fiche 23 ;
- les licences et provenances restent à la fiche 25 ;
- les corpus, scripts, environnements verrouillés et backends exécutables restent au Companion Pack.

## 10. Réserves

- aucun paquet Qdrant, Faiss, Chroma ou Sentence Transformers installé ;
- aucun modèle d’embedding téléchargé ou chargé ;
- aucune collection, HNSW, IVF, PQ, quantification ou index de payload exécuté ;
- aucun corpus réel, utilisateur, secret, personnel ou Companion Pack traité ;
- aucun Godot, HTTP, WebSocket, conteneur, GPU, serveur ou service distant exécuté ;
- aucune campagne de charge, concurrence, consommation mémoire ou performance matérielle ;
- aucune migration entre backends ou formats binaires testée ;
- aucune supériorité de solution revendiquée ;
- aucune approbation juridique organisationnelle ;
- aucun PDF produit ; licence globale et accessibilité avancée restent ouvertes.

## 11. Décision finale

La fiche est acceptée en version `1.0.0` au niveau `static-review`, avec preuve runtime bornée aux 43 fixtures synthétiques de contrats vectoriels. Toute adoption de backend ou modèle dans le Companion Pack exigera sa propre qualification versionnée, licenciée et reproductible.
