---
title: "Audit du Livre II — Chapitre 10"
id: "DOC-L2-QA-CH10"
status: "complete"
version: "1.0.0"
book: "Livre II"
chapter: 10
category: "quality-report"
audit-date: "2026-07-19"
audit-level: "static-review"
chapter-id: "DOC-L2-CH10"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du Livre II — Chapitre 10

> **Chapitre audité :** `Livre-II/CHAPITRE-10-Memoire-vectorielle-connaissances-et-recherche-semantique.md`  
> **Niveau GPT-5.6 Sol annoncé :** Élevée  
> **Décision :** accepté avec réserves runtime et PDF de fin de Livre.

## 1. Objet

L’audit vérifie que le chapitre introduit une mémoire vectorielle locale sans confondre :

- connaissance source ;
- index dérivé ;
- persistance SQLite ;
- sauvegarde de partie ;
- cache ;
- service accessible ultérieurement depuis Godot.

Il vérifie également que le parcours de référence reste utilisable sur Windows avec GPU AMD sans revendiquer une accélération non exécutée.

## 2. Couverture du périmètre officiel

| Exigence | Couverture |
|---|---|
| Rôle de la mémoire vectorielle dans `Project Asteria` | Complet |
| Embeddings locaux | Complet |
| Choix compatible avec la plateforme AMD | Complet avec CPU de référence |
| Découpage des documents | Complet |
| Taille des segments | Complet et mesurée en tokens |
| Métadonnées et provenance | Complet |
| Identifiants stables | Complet |
| Création de l’index | Complet |
| Mise à jour de l’index | Complet |
| Recherche par similarité | Complet |
| Filtres | Complet |
| Source, index et sauvegarde séparés | Complet |
| Suppressions et réindexations | Complet |
| Évaluation de récupération | Complet |
| Confidentialité et fonctionnement local | Complet |
| Chemin déterministe en cas d’indisponibilité | Complet |
| Parcours Solo | Complet |
| Parcours Studio | Complet |
| Audit statique sans PDF | Complet |

## 3. Frontières avec les chapitres voisins

### 3.1 Chapitre 7

Le chapitre 10 réutilise :

- validation JSON ;
- identifiants stables ;
- séparation entre donnée de conception et état runtime ;
- conversion vers des objets typés.

Il ne transforme pas les `Resource` de conception en mémoire vectorielle d’autorité.

### 3.2 Chapitre 8

SQLite reste la persistance relationnelle métier.

Qdrant ne remplace ni les contraintes relationnelles, ni les transactions des repositories.

### 3.3 Chapitre 9

Les sauvegardes restent des snapshots de reconstruction.

Le dossier Qdrant, les caches et les embeddings ne sont pas inclus comme autorité du slot.

### 3.4 Chapitre 11

Le chapitre 10 construit des outils Python locaux.

La communication depuis Godot, les contrats de disponibilité et le cycle de vie du service restent réservés au chapitre 11.

### 3.5 Chapitre 12

Aucun tutoriel HTTP, WebSocket ou API compatible OpenAI n’est introduit.

Le mode serveur Qdrant est seulement mentionné comme évolution, sans procédure d’intégration Godot.

### 3.6 Chapitre 13

Les principes de confidentialité sont présents, mais le durcissement réseau, les secrets, l’isolation production/runtime et la politique de déploiement restent réservés au chapitre 13.

## 4. Choix techniques vérifiés

### 4.1 Modèle `multilingual-e5-small`

Le modèle de référence :

- annonce 94 langues ;
- utilise une licence MIT ;
- possède une dimension cachée de `384` ;
- possède `512` positions maximales dans sa configuration ;
- documente les préfixes `query:` et `passage:` pour la récupération ;
- peut être utilisé avec Sentence Transformers.

Le chapitre conserve une marge avec :

- cible de `420` tokens ;
- overlap de `60` tokens ;
- maximum de `480` tokens.

### 4.2 Sentence Transformers

La documentation recommande, pour la recherche asymétrique, de distinguer requêtes et documents.

Le chapitre applique explicitement les rôles E5 et normalise les embeddings.

### 4.3 Qdrant Local Mode

Le client Python officiel documente :

> **[LECTURE] Formes de référence — Ne pas exécuter depuis le rapport.**

```python
QdrantClient(":memory:")
QdrantClient(path="path/to/db")
```

Le chapitre utilise le second chemin afin de persister un index dérivé sans démarrer de serveur. Qdrant et son client Python sont qualifiés comme composants Apache-2.0.

### 4.4 Collection

La collection impose :

- dimension `384` ;
- distance cosinus ;
- vecteur dense unique ;
- vérification avant usage ;
- nouvelle version en cas de dimension incompatible.

Qdrant documente qu’une collection regroupe des points de dimension homogène et que la distance dépend du modèle.

### 4.5 Points et payload

Chaque point possède :

- un UUID déterministe ;
- un vecteur ;
- un payload avec texte et provenance ;
- `source_id` ;
- révision ;
- hash du fragment ;
- modèle ;
- version de schéma ;
- visibilité ;
- langue ;
- tags.

### 4.6 Suppressions

La suppression est filtrée par `source_id`.

Le fichier source n’est jamais supprimé par l’adaptateur Qdrant.

### 4.7 Recherche filtrée

La recherche exige au moins une visibilité autorisée.

Elle filtre également :

- le modèle ;
- le schéma ;
- la langue optionnelle ;
- tous les tags obligatoires.

### 4.8 Repli lexical

Le chemin lexical :

- se construit avant le chargement du modèle ;
- lit les sources canoniques ;
- applique les mêmes contraintes de visibilité, langue et tags ;
- produit un ordre déterministe ;
- signale `retrieval_mode="lexical"` ;
- ne fabrique aucune réponse.

Cette construction corrige le risque d’un repli qui dépendrait lui-même du tokenizer indisponible.

## 5. Revue du découpage

### 5.1 Unité réelle

Le chapitre compte les tokens avec le tokenizer du modèle, pas les caractères.

### 5.2 Titres Markdown

Le chemin de titres est conservé dans le fragment et le payload.

### 5.3 Paragraphes hors limite

Une unité supérieure à la limite est divisée aux fins de phrase.

Une phrase toujours trop longue est refusée au lieu d’être tronquée.

### 5.4 Overlap

Le chevauchement conserve des paragraphes entiers.

Il n’est pas propagé lors d’un changement de titre.

Il est abandonné s’il ferait dépasser `max_tokens`.

### 5.5 Identité

Le `chunk_id` combine :

- namespace UUID stable ;
- `source_id` ;
- chemin de titres ;
- ordinal ;
- SHA-256 du contenu.

Le même contrat produit le même identifiant.

Un changement de découpage ou de contenu produit un nouveau point.

## 6. Revue des fonctions, paramètres et retours

Les extraits expliquent :

- `KnowledgeConfig` et ses valeurs par défaut ;
- `validate()` et ses erreurs ;
- `load_manifest()` ;
- `load_documents()` ;
- `safe_relative_path()` ;
- `ensure_inside_root()` ;
- `require_text()` ;
- `require_visibility()` ;
- `validate_tags()` ;
- `TokenChunker.split()` ;
- `_markdown_units()` ;
- `_split_oversized()` ;
- `_overlap_tail()` ;
- `_count()` ;
- `_build_chunk()` ;
- `embed_documents()` ;
- `embed_query()` ;
- le contrat `KnowledgeIndex` ;
- `_ensure_collection()` ;
- `_payload()` ;
- `replace_source()` ;
- `delete_source()` ;
- `list_source_ids()` ;
- `_search_filter()` ;
- `search()` ;
- le score lexical ;
- l’orchestrateur de récupération ;
- les interfaces de commande ;
- `reciprocal_rank()` ;
- `evaluate()`.

Pour chaque groupe, le chapitre précise les types, paramètres, retours, opérateurs et résultats concrets.

## 7. Revue statique du code

### 7.1 Python

Les extraits utilisent :

- `from __future__ import annotations` ;
- `dataclass` ;
- `Path` ;
- types paramétrés ;
- `Protocol` ;
- `Sequence` ;
- `uuid5` ;
- `hashlib.sha256` ;
- `argparse` ;
- `Counter` ;
- filtres Qdrant typés.

Aucune exécution runtime n’est revendiquée.

### 7.2 Qdrant

Les signatures relues correspondent aux concepts actuels du client :

- `QdrantClient(path=...)` ;
- `collection_exists()` ;
- `create_collection()` ;
- `get_collection()` ;
- `upsert()` ;
- `delete()` avec `FilterSelector` ;
- `scroll()` ;
- `query_points()` ;
- `PointStruct` ;
- `VectorParams` ;
- `Distance.COSINE` ;
- `Filter` ;
- `FieldCondition` ;
- `MatchValue` ;
- `MatchAny`.

La compatibilité exacte avec la version résolue par le futur verrou reste une réserve runtime.

### 7.3 Sentence Transformers

Les paramètres relus sont :

- `device="cpu"` ;
- `normalize_embeddings=True` ;
- `convert_to_numpy=True` ;
- `show_progress_bar=False`.

La conversion en `float32` est explicite.

## 8. Compatibilité AMD

### 8.1 Chemin garanti

Le CPU constitue la référence.

Aucune dépendance à CUDA n’est introduite.

### 8.2 DirectML et WinML

La documentation ONNX Runtime indique que DirectML :

- prend en charge du matériel DirectX 12 incluant AMD ;
- reste supporté ;
- se trouve en maintenance soutenue ;
- laisse les nouveaux développements Windows privilégier WinML.

Le chapitre présente donc cette voie comme optionnelle et à mesurer.

### 8.3 ROCm et MIGraphX

La documentation ONNX Runtime indique que le fournisseur ROCm est retiré à partir de la version 1.23 et oriente vers MIGraphX.

Le chapitre ne présente pas ROCm comme le chemin Windows de la RX 6750 XT.

## 9. Confidentialité et sécurité

Le chapitre vérifie :

- chemins relatifs seulement ;
- refus de `..` ;
- confinement sous la racine autorisée ;
- format et version du manifeste ;
- champs obligatoires ;
- visibilités sur liste autorisée ;
- tags normalisés ;
- visibilité calculée par une politique, pas accordée par la demande ;
- fonctionnement local ;
- absence de secret ;
- exclusion de l’index des sauvegardes de partie ;
- provenance de chaque résultat ;
- score non présenté comme vérité.

## 10. Évaluation de la récupération

Le chapitre fournit :

- format JSON versionné ;
- identifiants de cas ;
- questions ;
- filtres ;
- sources attendues ;
- `hit-rate@k` ;
- MRR ;
- code de retour ;
- règle interdisant de retirer les cas difficiles pour améliorer artificiellement les métriques.

Les sorties numériques restent explicitement illustratives.

## 11. Règle sémantique des erreurs

La section `Erreurs fréquentes, pièges et corrections` porte :

> **[LECTURE] Marqueur QA — Ne pas saisir.**

```html
<!-- qa:error-correction-section -->
```

Elle contient quatorze cas détaillés.

Chaque cas fournit :

- un symptôme ;
- un exemple fautif ;
- une correction ;
- un exemple corrigé ou un flux équivalent ;
- une différence explicite.

## 12. Non-conformités détectées et corrigées

| N° | Risque initial | Correction |
|---:|---|---|
| 1 | Repli lexical construit après le modèle | Construction directe depuis les documents avant toute initialisation vectorielle |
| 2 | Overlap propagé sous un autre titre | Overlap supprimé lors d’un changement de chemin de titres |
| 3 | Overlap pouvant dépasser `max_tokens` | Abandon du chevauchement lorsqu’il rendrait le fragment trop long |
| 4 | `ValueError` masquée par le repli | Les erreurs de contrat ne sont plus interceptées dans la recherche |
| 5 | Dimension modifiée silencieusement | Vérification de collection et nouvelle version obligatoire |
| 6 | Anciennes révisions conservées | Remplacement complet par `source_id` |
| 7 | Suppression d’une source non propagée | Différence d’ensembles entre manifeste et index |
| 8 | Filtres contrôlés par la requête | Visibilités obligatoires issues d’une politique d’autorisation |
| 9 | Score interprété comme probabilité | Formulation et erreur dédiée |
| 10 | Accélération AMD promise | CPU de référence, accélérations optionnelles et mesurées |
| 11 | Dossier Qdrant versionné | Sources, configuration et évaluations seulement dans Git |
| 12 | Évaluation auto-sélectionnée | Jeu stable et échecs conservés |
| 13 | Sauvegarde confondue avec l’index | Contrats d’autorité séparés |
| 14 | Passage tronqué silencieusement | Découpage préalable et refus explicite |

## 13. Contrôle des doublons

La revue locale du nouveau chapitre détecte :

- aucun titre dupliqué ;
- aucun bloc significatif dupliqué ;
- aucun paragraphe long dupliqué.

Le workflow permanent doit confirmer cette mesure sur l’ensemble du dépôt.

## 14. Repères d’utilisation

Les blocs utilisent :

- `[PS]` pour PowerShell ;
- `[VSC]` pour les fichiers ;
- `[SORTIE]` pour les résultats ;
- `[LECTURE]` pour les structures et exemples non exécutables.

Aucun bloc n’est présenté sans repère.

Les repères `[CMD]`, `[WSL]`, `[DCT]`, `[DCK]`, `[WEB]` et `[APP]` restent disponibles dans la légende, mais aucune procédure ne les emploie artificiellement lorsque le chapitre n’en a pas besoin.

## 15. Réserves runtime

Ne sont pas exécutés :

- création de l’environnement Python ;
- installation de `sentence-transformers` ;
- installation de `qdrant-client` ;
- téléchargement du modèle ;
- chargement CPU ;
- tokenisation ;
- vérification de dimension ;
- création de collection ;
- insertion ;
- recherche ;
- filtres ;
- suppression ;
- repli ;
- évaluation ;
- fonctionnement hors ligne ;
- verrou concurrent du stockage local ;
- mesure CPU, RAM, disque et latence ;
- DirectML ou WinML ;
- MIGraphX ;
- intégration Godot ;
- mode serveur ;
- export Windows.

## 16. PDF

Conformément à la politique du projet :

- aucun PDF intermédiaire n’est construit ;
- la compilation et l’inspection restent différées jusqu’à la fin du Livre II.

## 17. Sources officielles vérifiées

La revue statique s’appuie sur :

- [Sentence Transformers — Semantic Search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) ;
- [Hugging Face — intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) ;
- [Hugging Face — config.json](https://huggingface.co/intfloat/multilingual-e5-small/blob/main/config.json) ;
- [Qdrant Client — dépôt officiel](https://github.com/qdrant/qdrant-client) ;
- [Qdrant — Collections](https://qdrant.tech/documentation/manage-data/collections/) ;
- [Qdrant — Points](https://qdrant.tech/documentation/manage-data/points/) ;
- [Qdrant — Payload](https://qdrant.tech/documentation/concepts/payload/) ;
- [Qdrant — Filtering](https://qdrant.tech/documentation/search/filtering/) ;
- [ONNX Runtime — DirectML](https://onnxruntime.ai/docs/execution-providers/DirectML-ExecutionProvider.html) ;
- [ONNX Runtime — ROCm](https://onnxruntime.ai/docs/execution-providers/ROCm-ExecutionProvider.html) ;
- [ONNX Runtime — MIGraphX](https://onnxruntime.ai/docs/execution-providers/MIGraphX-ExecutionProvider.html).

## 18. Décision

**Accepté avec réserves runtime et PDF de fin de Livre.**

Le chapitre peut être déclaré **rédigé, repéré et audité au niveau `static-review`** après réussite des workflows légers :

- `Validate Chapters Without PDF` ;
- `Validate Usage Contexts`.

Cette décision ne revendique aucune exécution du modèle, de Qdrant, des scripts Python ou de l’accélération AMD.
