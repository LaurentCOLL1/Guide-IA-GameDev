---
title: "Livre II — Chapitre 10 : Mémoire vectorielle, connaissances et recherche sémantique"
id: "DOC-L2-CH10"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre II"
chapter: 10
last-verified: "2026-07-19"
audit-status: "complete"
audit-date: "2026-07-19"
audit-report: "Livre-II/QA/AUDIT-CHAPITRE-10.md"
audit-level: "static-review"
reference-engine:
  name: "Godot Engine"
  version: "4.7.1-stable"
  edition: "Standard"
  language: "GDScript"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Mémoire vectorielle, connaissances et recherche sémantique

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L2-CH10`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Version de référence :** Godot `4.7.1-stable`, édition Standard, GDScript, Forward+  
> **Niveau de raisonnement conseillé :** GPT-5.6 Sol — Élevée  
> **Audit post-création :** terminé au niveau `static-review` — voir `Livre-II/QA/AUDIT-CHAPITRE-10.md`.

## 1. Rôle du chapitre

Les chapitres 7 à 9 ont séparé les données de conception, la configuration, la persistance SQLite et les snapshots de sauvegarde. Ce chapitre ajoute une cinquième catégorie : **l’index de recherche dérivé**.

Une mémoire vectorielle transforme des fragments de connaissance en tableaux de nombres, appelés embeddings, afin de retrouver les passages dont le sens est proche d’une question. Elle ne remplace ni les fichiers sources, ni SQLite, ni les sauvegardes.

À la fin du chapitre, le lecteur doit savoir :

- distinguer source canonique, fragment, embedding, point vectoriel et résultat ;
- choisir un modèle local multilingue ;
- découper les documents selon le tokenizer réel ;
- attribuer des identifiants stables ;
- conserver la provenance ;
- construire un index Qdrant local et dérivable ;
- mettre à jour et supprimer les points obsolètes ;
- rechercher avec similarité et filtres ;
- utiliser un repli lexical déterministe ;
- évaluer la récupération ;
- préserver les frontières des chapitres 11 à 13.

## 2. Prérequis

Le lecteur doit connaître :

- Python et les environnements virtuels du Livre I ;
- les classes, fonctions, types et collections du chapitre 2 ;
- l’architecture feature-first du chapitre 4 ;
- les contrats et l’injection du chapitre 5 ;
- les identifiants stables et la validation JSON du chapitre 7 ;
- SQLite du chapitre 8 ;
- les sauvegardes du chapitre 9.

Docker n’est pas requis. Qdrant fonctionne ici en **mode local Python**, dans le même processus que l’outil d’indexation.

## 3. Périmètre et frontières

Ce chapitre définit une chaîne Python locale : lecture, validation, découpage, embeddings, indexation, recherche, repli et évaluation.

Il ne définit pas encore :

- l’appel depuis Godot, réservé au chapitre 11 ;
- HTTP, WebSocket, API compatibles OpenAI et files de tâches, réservés au chapitre 12 ;
- le durcissement production/runtime, réservé au chapitre 13 ;
- la mémoire personnelle des agents, réservée au chapitre 17 ;
- le codex narratif, réservé au chapitre 25 ;
- les campagnes industrialisées, réservées au chapitre 27.

> **Frontière essentielle :** Godot ne lit jamais directement le répertoire interne de Qdrant.

## 4. Vocabulaire

### 4.1 Source canonique

Une source canonique est un document d’autorité lisible, validé et versionnable. L’index peut être reconstruit depuis elle.

### 4.2 Fragment

Un fragment, ou *chunk*, est une portion autonome d’un document. Il doit être assez court pour le modèle et assez complet pour rester compréhensible.

### 4.3 Token

Un token est une unité produite par le tokenizer. Il ne correspond pas toujours à un mot : ponctuation et morceaux de mots peuvent former des tokens distincts.

### 4.4 Embedding

Un embedding est un tableau de nombres à virgule flottante. Le modèle retenu produit ici `384` composantes.

### 4.5 Point et payload

Un point Qdrant contient un identifiant, un vecteur et un payload. Le payload conserve texte, source, langue, visibilité, tags, révision et version de schéma.

### 4.6 Similarité

La similarité classe les vecteurs proches. Un score élevé n’est ni une probabilité, ni une preuve de vérité.

## 5. Matrice d’autorité

> **[LECTURE] Séparation des responsabilités — Ne pas saisir.**

```text
Élément                         Autorité ?  Versionné Git ?  Reconstructible ?
------------------------------  ----------  --------------  ----------------
knowledge/sources/*.md          oui         oui             source primaire
knowledge/manifest.json         oui         oui             décrit le corpus
var/knowledge/qdrant/           non         non             oui
cache d’embeddings              non         non             oui
SQLite sous user://             oui métier  non             non depuis l’index
user://saves/*.json             oui partie  non             non depuis l’index
résultat de recherche           non         non             oui
```

La mémoire vectorielle peut enrichir une fonction. Elle ne décide jamais seule d’un état durable de gameplay.

## 6. Architecture de référence

> **[LECTURE] Flux de connaissance — Ne pas saisir.**

```text
sources canoniques
       ↓
lecture + validation
       ↓
découpage déterministe ───────→ index lexical de repli
       ↓
embeddings locaux
       ↓
Qdrant Local Mode
       ↓
recherche + filtres + provenance
```

Les sources ne connaissent pas Qdrant. Le domaine dépend d’un contrat. L’adaptateur Qdrant reste dans l’infrastructure. L’intégration Godot viendra au chapitre 11.

## 7. Choix de référence

### 7.1 Modèle d’embeddings

Le modèle pédagogique retenu est :

> **[LECTURE] Identité du modèle — Ne pas saisir.**

```text
intfloat/multilingual-e5-small
```

Raisons : couverture multilingue incluant le français, licence MIT, dimension `384`, configuration à `512` positions et préfixes documentés `query:` et `passage:`.

Le chemin de référence utilise le CPU. Le premier téléchargement doit être réalisé avant un fonctionnement totalement hors ligne.

### 7.2 Stockage vectoriel

Qdrant est utilisé avec `qdrant-client` en mode local persistant :

> **[LECTURE] Initialisation conceptuelle — Ne pas saisir.**

```python
client = QdrantClient(path="var/knowledge/qdrant")
```

Ce mode ne démarre aucun serveur et ne demande pas Docker. Le moteur Qdrant et son client Python sont distribués sous licence Apache-2.0. Le modèle et le stockage doivent figurer dans l’inventaire des composants tiers.

### 7.3 Compatibilité AMD

La RX 6750 XT n’est pas présentée comme automatiquement accélérée. La référence est :

> **[LECTURE] Ordre de priorité — Ne pas saisir.**

```text
1. CPU local validé
2. mesure du besoin
3. export ONNX séparé
4. essai WinML ou DirectML sous Windows
5. essai MIGraphX sur plateforme compatible
```

DirectML reste une voie DirectX 12 incluant AMD, mais les nouveaux développements Windows privilégient WinML. Le fournisseur ROCm d’ONNX Runtime a été retiré à partir de la version 1.23 au profit de MIGraphX. Aucune de ces accélérations n’est exécutée dans ce chapitre.

## 8. Préparer l’environnement

> **[PS] PowerShell 7 — Créer l’environnement depuis la racine du projet :**

```powershell
py -3.12 -m venv .venv-knowledge
.\.venv-knowledge\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install sentence-transformers qdrant-client
```

`-m venv` exécute le module standard `venv`. `Activate.ps1` modifie la session courante. `python -m pip` garantit que `pip` appartient à l’interpréteur actif.

> **[SORTIE] PowerShell — Exemple de contrôle attendu :**

```text
(.venv-knowledge) PS C:\...\ProjectAsteria>
```

Aucune version exacte n’est prétendue installée ici. Le futur Starter Kit devra produire un verrou après exécution réelle.

## 9. Arborescence

> **[VSC] Visual Studio Code — Créer les dossiers et fichiers suivants :**

```text
ProjectAsteria/
├── knowledge/
│   ├── manifest.json
│   ├── sources/
│   └── evaluation/
├── tools/knowledge/
│   ├── knowledge_config.py
│   ├── knowledge_models.py
│   ├── source_loader.py
│   ├── chunker.py
│   ├── embedding_provider.py
│   ├── knowledge_index.py
│   ├── qdrant_index.py
│   ├── lexical_index.py
│   ├── retrieval_service.py
│   ├── index_knowledge.py
│   ├── search_knowledge.py
│   └── evaluate_retrieval.py
└── var/knowledge/qdrant/       # dérivé, ignoré par Git
```

`knowledge/` contient l’autorité. `tools/knowledge/` contient le pipeline. `var/` contient des données reconstructibles.

## 10. Configuration typée

> **[VSC] Visual Studio Code — Créer :** `tools/knowledge/knowledge_config.py`.

```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class KnowledgeConfig:
    project_root: Path
    model_name: str = "intfloat/multilingual-e5-small"
    collection_name: str = "asteria_knowledge_v1"
    vector_size: int = 384
    target_tokens: int = 420
    overlap_tokens: int = 60
    max_tokens: int = 480
    default_limit: int = 5
    index_schema_version: int = 1

    @property
    def source_root(self) -> Path:
        return self.project_root / "knowledge" / "sources"

    @property
    def manifest_path(self) -> Path:
        return self.project_root / "knowledge" / "manifest.json"

    @property
    def qdrant_path(self) -> Path:
        return self.project_root / "var" / "knowledge" / "qdrant"

    def validate(self) -> None:
        if self.vector_size <= 0:
            raise ValueError("vector_size doit être positif.")
        if not 1 <= self.overlap_tokens < self.target_tokens:
            raise ValueError("overlap_tokens doit être inférieur à target_tokens.")
        if not self.target_tokens <= self.max_tokens <= 500:
            raise ValueError("target_tokens <= max_tokens <= 500 est obligatoire.")
        if not 1 <= self.default_limit <= 50:
            raise ValueError("default_limit doit rester entre 1 et 50.")
```

`@dataclass` génère notamment le constructeur. `frozen=True` interdit la réaffectation des champs. `slots=True` limite les attributs. `Path` représente un chemin. L’opérateur `/` assemble ses segments.

`validate()` retourne implicitement `None`. `raise ValueError` arrête l’appel lorsque le contrat est violé. L’expression `1 <= x < y` combine deux comparaisons.

## 11. Modèles du domaine

> **[VSC] Visual Studio Code — Créer :** `tools/knowledge/knowledge_models.py`.

```python
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True, slots=True)
class KnowledgeDocument:
    source_id: str
    source_path: Path
    title: str
    language: str
    visibility: str
    tags: tuple[str, ...]
    revision: str
    body: str


@dataclass(frozen=True, slots=True)
class KnowledgeChunk:
    chunk_id: str
    source_id: str
    source_path: str
    title: str
    heading_path: tuple[str, ...]
    ordinal: int
    language: str
    visibility: str
    tags: tuple[str, ...]
    revision: str
    content_sha256: str
    text: str


@dataclass(frozen=True, slots=True)
class KnowledgeHit:
    chunk_id: str
    source_id: str
    source_path: str
    text: str
    score: float
    metadata: dict[str, Any]
    retrieval_mode: str
```

`tuple[str, ...]` contient zéro ou plusieurs chaînes immuables. `dict[str, Any]` possède des clés textuelles ; ses valeurs restent validées à la frontière. `KnowledgeHit` indique explicitement si le résultat vient du chemin `vector` ou `lexical`.

## 12. Manifeste et source canonique

> **[VSC] Visual Studio Code — Créer :** `knowledge/manifest.json`.

```json
{
  "format": "project-asteria-knowledge-manifest",
  "format_version": 1,
  "sources": [
    {
      "source_id": "knowledge.beacons.north-gate",
      "path": "beacons/beacon-north-gate.md",
      "title": "Balise de la porte nord",
      "language": "fr",
      "visibility": "internal",
      "tags": ["beacon", "north-gate"]
    }
  ]
}
```

> **[VSC] Visual Studio Code — Créer :** `knowledge/sources/beacons/beacon-north-gate.md`.

```markdown
# Balise de la porte nord

## Fonction

La balise signale l’ouverture du passage vers la Réserve du Nord.

## Activation

Elle s’active lorsque le joueur possède l’autorisation des Veilleurs.

## Défaillance

Si le relais local est hors service, la porte reste fermée et un signal orange apparaît.
```

Le manifeste fournit l’identité et la politique. Le Markdown fournit le contenu d’autorité. Le chemin reste relatif à `knowledge/sources/`.

## 13. Charger et valider les sources

> **[VSC] Visual Studio Code — Créer :** `tools/knowledge/source_loader.py`.

```python
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from knowledge_models import KnowledgeDocument


def load_manifest(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("La racine du manifeste doit être un objet.")
    if data.get("format") != "project-asteria-knowledge-manifest":
        raise ValueError("Format de manifeste inconnu.")
    if data.get("format_version") != 1:
        raise ValueError("Version de manifeste non prise en charge.")
    if not isinstance(data.get("sources"), list):
        raise ValueError("sources doit être un tableau.")
    return data


def safe_relative_path(value: str) -> Path:
    path = Path(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise ValueError(f"Chemin interdit : {value}")
    if path.suffix.lower() != ".md":
        raise ValueError("Seules les sources Markdown sont acceptées.")
    return path


def require_text(entry: dict[str, Any], key: str) -> str:
    value = entry.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{key} doit être une chaîne non vide.")
    return value.strip()


def validate_tags(value: Any) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise ValueError("tags doit être un tableau.")
    result: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise ValueError("Chaque tag doit être une chaîne non vide.")
        result.append(item.strip().lower())
    return tuple(sorted(set(result)))


def load_documents(root: Path, manifest: dict[str, Any]) -> list[KnowledgeDocument]:
    documents: list[KnowledgeDocument] = []
    seen: set[str] = set()
    root = root.resolve()

    for index, raw in enumerate(manifest["sources"]):
        if not isinstance(raw, dict):
            raise ValueError(f"sources[{index}] doit être un objet.")
        source_id = require_text(raw, "source_id")
        if source_id in seen:
            raise ValueError(f"source_id dupliqué : {source_id}")
        seen.add(source_id)

        relative = safe_relative_path(require_text(raw, "path"))
        absolute = (root / relative).resolve()
        try:
            absolute.relative_to(root)
        except ValueError as exc:
            raise ValueError(f"Source hors racine : {relative}") from exc

        body = absolute.read_text(encoding="utf-8")
        if not body.strip():
            raise ValueError(f"Source vide : {relative}")
        visibility = require_text(raw, "visibility")
        if visibility not in {"public", "internal", "restricted"}:
            raise ValueError(f"Visibilité invalide : {visibility}")

        documents.append(KnowledgeDocument(
            source_id=source_id,
            source_path=relative,
            title=require_text(raw, "title"),
            language=require_text(raw, "language"),
            visibility=visibility,
            tags=validate_tags(raw.get("tags", [])),
            revision=hashlib.sha256(body.encode("utf-8")).hexdigest(),
            body=body,
        ))
    return documents
```

`json.loads()` analyse le texte. `isinstance()` vérifie un type au runtime. `enumerate()` produit l’index et la valeur. `set` détecte les doublons. `resolve()` normalise un chemin ; `relative_to()` vérifie son confinement. `sha256().hexdigest()` retourne une empreinte hexadécimale de 64 caractères.

## 14. Découpage déterministe

Le modèle accepte au plus 512 positions. Le projet vise 420 tokens, autorise un chevauchement de 60 et refuse tout fragment supérieur à 480.

> **[VSC] Visual Studio Code — Créer :** `tools/knowledge/chunker.py`.

```python
from __future__ import annotations

import hashlib
import re
from uuid import UUID, uuid5

from knowledge_models import KnowledgeChunk, KnowledgeDocument

CHUNK_NAMESPACE = UUID("f6fe48a6-48d4-4fa8-b2f8-4d1dd122d36c")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")


class TokenChunker:
    def __init__(self, tokenizer, target: int, overlap: int, maximum: int):
        self._tokenizer = tokenizer
        self._target = target
        self._overlap = overlap
        self._maximum = maximum

    def _count(self, text: str) -> int:
        return len(self._tokenizer.encode(text, add_special_tokens=False))

    def _units(self, body: str) -> list[tuple[tuple[str, ...], str]]:
        headings: list[str] = []
        units: list[tuple[tuple[str, ...], str]] = []
        paragraph: list[str] = []

        def flush() -> None:
            if paragraph:
                units.append((tuple(headings), " ".join(paragraph).strip()))
                paragraph.clear()

        for line in body.splitlines():
            match = HEADING_RE.match(line)
            if match:
                flush()
                level = len(match.group(1))
                headings[:] = headings[: level - 1]
                headings.append(match.group(2).strip())
            elif line.strip():
                paragraph.append(line.strip())
            else:
                flush()
        flush()
        return units

    def _split_oversized(self, text: str) -> list[str]:
        if self._count(text) <= self._maximum:
            return [text]
        parts: list[str] = []
        current: list[str] = []
        for sentence in SENTENCE_RE.split(text):
            candidate = " ".join([*current, sentence]).strip()
            if current and self._count(candidate) > self._maximum:
                parts.append(" ".join(current))
                current = [sentence]
            else:
                current.append(sentence)
        if current:
            value = " ".join(current)
            if self._count(value) > self._maximum:
                raise ValueError("Une phrase dépasse max_tokens ; source à corriger.")
            parts.append(value)
        return parts

    def split(self, document: KnowledgeDocument) -> list[KnowledgeChunk]:
        chunks: list[KnowledgeChunk] = []
        current: list[str] = []
        current_heading: tuple[str, ...] = ()

        def emit() -> None:
            nonlocal current
            if not current:
                return
            text = "\n\n".join(current)
            ordinal = len(chunks)
            digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
            identity = f"{document.source_id}|{'/'.join(current_heading)}|{ordinal}|{digest}"
            chunks.append(KnowledgeChunk(
                chunk_id=str(uuid5(CHUNK_NAMESPACE, identity)),
                source_id=document.source_id,
                source_path=document.source_path.as_posix(),
                title=document.title,
                heading_path=current_heading,
                ordinal=ordinal,
                language=document.language,
                visibility=document.visibility,
                tags=document.tags,
                revision=document.revision,
                content_sha256=digest,
                text=text,
            ))
            overlap: list[str] = []
            total = 0
            for paragraph in reversed(current):
                count = self._count(paragraph)
                if total + count > self._overlap:
                    break
                overlap.insert(0, paragraph)
                total += count
            current = overlap

        for heading, paragraph in self._units(document.body):
            if heading != current_heading:
                emit()
                current = []
                current_heading = heading
            for part in self._split_oversized(paragraph):
                candidate = "\n\n".join([*current, part])
                if current and self._count(candidate) > self._target:
                    emit()
                    candidate = "\n\n".join([*current, part])
                    if self._count(candidate) > self._maximum:
                        current = []
                current.append(part)
        emit()
        return chunks
```

Le constructeur reçoit le tokenizer et trois entiers. `_count()` retourne un `int`. `_units()` retourne le chemin des titres avec chaque paragraphe. Le chevauchement conserve des paragraphes entiers, ne traverse pas un changement de titre et est abandonné s’il ferait dépasser la limite.

`uuid5()` produit le même UUID pour la même identité. Une modification du texte change le hash, donc l’identifiant. L’ordinal reste local à la source.

## 15. Fournisseur d’embeddings

> **[VSC] Visual Studio Code — Créer :** `tools/knowledge/embedding_provider.py`.

```python
from __future__ import annotations

import numpy as np
from sentence_transformers import SentenceTransformer


class E5EmbeddingProvider:
    def __init__(self, model_name: str, expected_size: int):
        self._model = SentenceTransformer(model_name, device="cpu")
        self._expected_size = expected_size
        probe = self.embed_query("contrôle de dimension")
        if len(probe) != expected_size:
            raise ValueError(
                f"Dimension reçue {len(probe)}, attendue {expected_size}."
            )

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        values = [f"passage: {text}" for text in texts]
        vectors = self._model.encode(
            values,
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=False,
        )
        return np.asarray(vectors, dtype=np.float32).tolist()

    def embed_query(self, text: str) -> list[float]:
        if not text.strip():
            raise ValueError("La requête ne peut pas être vide.")
        vector = self._model.encode(
            f"query: {text.strip()}",
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=False,
        )
        return np.asarray(vector, dtype=np.float32).tolist()
```

`model_name` identifie le modèle. `expected_size` protège le contrat de collection. `encode()` retourne un tableau NumPy. `normalize_embeddings=True` produit des vecteurs normalisés. `tolist()` convertit le tableau vers des listes Python sérialisables.

Les préfixes `query:` et `passage:` appartiennent au contrat E5. Ils ne sont pas décoratifs.

## 16. Contrat de l’index

> **[VSC] Visual Studio Code — Créer :** `tools/knowledge/knowledge_index.py`.

```python
from __future__ import annotations

from typing import Protocol, Sequence

from knowledge_models import KnowledgeChunk, KnowledgeHit


class KnowledgeIndex(Protocol):
    def replace_source(
        self,
        source_id: str,
        chunks: Sequence[KnowledgeChunk],
        vectors: Sequence[Sequence[float]],
    ) -> None: ...

    def delete_source(self, source_id: str) -> None: ...

    def list_source_ids(self) -> set[str]: ...

    def search(
        self,
        query_vector: Sequence[float],
        allowed_visibility: set[str],
        language: str | None,
        required_tags: set[str],
        limit: int,
    ) -> list[KnowledgeHit]: ...
```

`Protocol` décrit une forme attendue sans imposer d’héritage. `Sequence` accepte plusieurs collections ordonnées. `str | None` signifie chaîne ou absence de valeur. Les points de suspension représentent une méthode contractuelle.

## 17. Adaptateur Qdrant

> **[VSC] Visual Studio Code — Créer :** `tools/knowledge/qdrant_index.py`.

```python
from __future__ import annotations

from collections.abc import Sequence

from qdrant_client import QdrantClient, models

from knowledge_models import KnowledgeChunk, KnowledgeHit


class QdrantKnowledgeIndex:
    def __init__(self, path: str, collection: str, vector_size: int,
                 model_name: str, schema_version: int):
        self._client = QdrantClient(path=path)
        self._collection = collection
        self._vector_size = vector_size
        self._model_name = model_name
        self._schema_version = schema_version
        self._ensure_collection()

    def _ensure_collection(self) -> None:
        if not self._client.collection_exists(self._collection):
            self._client.create_collection(
                collection_name=self._collection,
                vectors_config=models.VectorParams(
                    size=self._vector_size,
                    distance=models.Distance.COSINE,
                ),
            )
            return
        info = self._client.get_collection(self._collection)
        vectors = info.config.params.vectors
        if not isinstance(vectors, models.VectorParams):
            raise ValueError("Une collection dense simple est attendue.")
        if vectors.size != self._vector_size:
            raise ValueError("Dimension incompatible ; créer une nouvelle collection.")

    def _payload(self, chunk: KnowledgeChunk) -> dict[str, object]:
        return {
            "source_id": chunk.source_id,
            "source_path": chunk.source_path,
            "title": chunk.title,
            "heading_path": list(chunk.heading_path),
            "ordinal": chunk.ordinal,
            "language": chunk.language,
            "visibility": chunk.visibility,
            "tags": list(chunk.tags),
            "revision": chunk.revision,
            "content_sha256": chunk.content_sha256,
            "text": chunk.text,
            "embedding_model": self._model_name,
            "index_schema_version": self._schema_version,
        }

    def delete_source(self, source_id: str) -> None:
        self._client.delete(
            collection_name=self._collection,
            points_selector=models.FilterSelector(filter=models.Filter(must=[
                models.FieldCondition(
                    key="source_id", match=models.MatchValue(value=source_id)
                )
            ])),
            wait=True,
        )

    def replace_source(self, source_id: str,
                       chunks: Sequence[KnowledgeChunk],
                       vectors: Sequence[Sequence[float]]) -> None:
        if len(chunks) != len(vectors):
            raise ValueError("Un vecteur est requis pour chaque fragment.")
        for vector in vectors:
            if len(vector) != self._vector_size:
                raise ValueError("Dimension de vecteur incorrecte.")
        self.delete_source(source_id)
        points = [
            models.PointStruct(id=chunk.chunk_id, vector=list(vector),
                               payload=self._payload(chunk))
            for chunk, vector in zip(chunks, vectors, strict=True)
        ]
        if points:
            self._client.upsert(
                collection_name=self._collection,
                points=points,
                wait=True,
            )

    def list_source_ids(self) -> set[str]:
        result: set[str] = set()
        offset = None
        while True:
            points, offset = self._client.scroll(
                collection_name=self._collection,
                limit=256,
                offset=offset,
                with_payload=["source_id"],
                with_vectors=False,
            )
            for point in points:
                if point.payload and isinstance(point.payload.get("source_id"), str):
                    result.add(point.payload["source_id"])
            if offset is None:
                return result

    def search(self, query_vector: Sequence[float],
               allowed_visibility: set[str], language: str | None,
               required_tags: set[str], limit: int) -> list[KnowledgeHit]:
        if not allowed_visibility:
            raise ValueError("Une visibilité autorisée est obligatoire.")
        must: list[models.Condition] = [
            models.FieldCondition(
                key="visibility",
                match=models.MatchAny(any=sorted(allowed_visibility)),
            ),
            models.FieldCondition(
                key="embedding_model",
                match=models.MatchValue(value=self._model_name),
            ),
            models.FieldCondition(
                key="index_schema_version",
                match=models.MatchValue(value=self._schema_version),
            ),
        ]
        if language:
            must.append(models.FieldCondition(
                key="language", match=models.MatchValue(value=language)
            ))
        for tag in sorted(required_tags):
            must.append(models.FieldCondition(
                key="tags", match=models.MatchValue(value=tag)
            ))
        response = self._client.query_points(
            collection_name=self._collection,
            query=list(query_vector),
            query_filter=models.Filter(must=must),
            limit=limit,
            with_payload=True,
            with_vectors=False,
        )
        hits: list[KnowledgeHit] = []
        for point in response.points:
            payload = point.payload or {}
            hits.append(KnowledgeHit(
                chunk_id=str(point.id),
                source_id=str(payload.get("source_id", "")),
                source_path=str(payload.get("source_path", "")),
                text=str(payload.get("text", "")),
                score=float(point.score),
                metadata=dict(payload),
                retrieval_mode="vector",
            ))
        return hits
```

`collection_exists()` évite de recréer la collection. `VectorParams` fixe dimension et distance. `wait=True` attend la fin de l’écriture. `zip(..., strict=True)` refuse des longueurs différentes. `scroll()` parcourt tous les points sans charger les vecteurs. `query_points()` retourne les points classés.

Le remplacement supprime d’abord les points de la source, puis insère la nouvelle révision. Une application de production préparera une collection de staging pour éviter une fenêtre intermédiaire vide.

## 18. Synchroniser créations, modifications et suppressions

> **[VSC] Visual Studio Code — Créer :** `tools/knowledge/index_knowledge.py`.

```python
from __future__ import annotations

from pathlib import Path

from chunker import TokenChunker
from embedding_provider import E5EmbeddingProvider
from knowledge_config import KnowledgeConfig
from qdrant_index import QdrantKnowledgeIndex
from source_loader import load_documents, load_manifest


def rebuild(project_root: Path) -> None:
    config = KnowledgeConfig(project_root.resolve())
    config.validate()
    manifest = load_manifest(config.manifest_path)
    documents = load_documents(config.source_root, manifest)

    embeddings = E5EmbeddingProvider(config.model_name, config.vector_size)
    chunker = TokenChunker(
        embeddings._model.tokenizer,
        config.target_tokens,
        config.overlap_tokens,
        config.max_tokens,
    )
    index = QdrantKnowledgeIndex(
        str(config.qdrant_path), config.collection_name,
        config.vector_size, config.model_name, config.index_schema_version,
    )

    declared = {document.source_id for document in documents}
    for stale in index.list_source_ids() - declared:
        index.delete_source(stale)

    for document in documents:
        chunks = chunker.split(document)
        vectors = embeddings.embed_documents([chunk.text for chunk in chunks])
        index.replace_source(document.source_id, chunks, vectors)
```

`rebuild()` retourne `None`. La différence d’ensembles `indexés - déclarés` identifie les sources retirées. La compréhension de liste extrait le texte de chaque fragment.

L’accès pédagogique au tokenizer montre la dépendance réelle ; le Starter Kit exposera une propriété publique afin de ne pas utiliser `_model` hors de l’adaptateur.

> **[PS] PowerShell 7 — Lancer depuis la racine :**

```powershell
.\.venv-knowledge\Scripts\python.exe .\tools\knowledge\index_knowledge.py
```

> **[SORTIE] PowerShell — Résultat attendu après matérialisation :**

```text
Index construit : nombre de sources et fragments affiché par le futur journal.
```

Cette sortie est une cible documentaire ; elle n’a pas été obtenue dans cet audit.

## 19. Repli lexical déterministe

Le repli doit fonctionner même si le modèle ne se charge pas. Il est donc construit directement depuis les documents canoniques, avant l’initialisation vectorielle.

> **[VSC] Visual Studio Code — Créer :** `tools/knowledge/lexical_index.py`.

```python
from __future__ import annotations

import re
from collections import Counter

from knowledge_models import KnowledgeDocument, KnowledgeHit

WORD_RE = re.compile(r"[\wÀ-ÿ'-]+", re.UNICODE)


def words(text: str) -> list[str]:
    return [value.casefold() for value in WORD_RE.findall(text)]


class LexicalIndex:
    def __init__(self, documents: list[KnowledgeDocument]):
        self._documents = documents

    def search(self, query: str, allowed_visibility: set[str],
               language: str | None, required_tags: set[str],
               limit: int) -> list[KnowledgeHit]:
        query_counts = Counter(words(query))
        ranked: list[KnowledgeHit] = []
        for document in self._documents:
            if document.visibility not in allowed_visibility:
                continue
            if language and document.language != language:
                continue
            if not required_tags.issubset(set(document.tags)):
                continue
            body_counts = Counter(words(document.body))
            score = float(sum(
                min(count, body_counts[word])
                for word, count in query_counts.items()
            ))
            if score <= 0:
                continue
            ranked.append(KnowledgeHit(
                chunk_id=f"lexical:{document.source_id}",
                source_id=document.source_id,
                source_path=document.source_path.as_posix(),
                text=document.body,
                score=score,
                metadata={"title": document.title, "tags": list(document.tags)},
                retrieval_mode="lexical",
            ))
        ranked.sort(key=lambda hit: (-hit.score, hit.source_id))
        return ranked[:limit]
```

`casefold()` normalise la casse de manière plus large que `lower()`. `Counter` compte les termes. `issubset()` impose tous les tags. La clé de tri négative classe les scores décroissants, puis l’identifiant garantit un ordre stable.

Ce repli ne prétend pas être sémantique. Il restitue des sources et leur provenance ; il ne fabrique aucune réponse.

## 20. Orchestrateur de récupération

> **[VSC] Visual Studio Code — Créer :** `tools/knowledge/retrieval_service.py`.

```python
from __future__ import annotations

from embedding_provider import E5EmbeddingProvider
from knowledge_index import KnowledgeIndex
from knowledge_models import KnowledgeHit
from lexical_index import LexicalIndex


class RetrievalService:
    def __init__(self, lexical: LexicalIndex,
                 embeddings: E5EmbeddingProvider | None,
                 vector_index: KnowledgeIndex | None):
        self._lexical = lexical
        self._embeddings = embeddings
        self._vector_index = vector_index

    def search(self, query: str, allowed_visibility: set[str],
               language: str | None = None,
               required_tags: set[str] | None = None,
               limit: int = 5) -> list[KnowledgeHit]:
        query = query.strip()
        if not query:
            raise ValueError("La requête ne peut pas être vide.")
        if not allowed_visibility:
            raise ValueError("Aucune visibilité autorisée.")
        tags = required_tags or set()

        if self._embeddings is not None and self._vector_index is not None:
            try:
                vector = self._embeddings.embed_query(query)
                return self._vector_index.search(
                    vector, allowed_visibility, language, tags, limit
                )
            except (OSError, RuntimeError) as exc:
                print(f"Recherche vectorielle indisponible : {exc}")

        return self._lexical.search(
            query, allowed_visibility, language, tags, limit
        )
```

Les dépendances vectorielles sont optionnelles. Les erreurs de contrat comme `ValueError` ne sont pas masquées : elles doivent être corrigées. Seules des indisponibilités techniques ciblées déclenchent le repli.

`required_tags or set()` fournit un ensemble vide quand le paramètre vaut `None`. Le retour reste `list[KnowledgeHit]` dans les deux modes.

## 21. Interface de recherche locale

> **[VSC] Visual Studio Code — Créer :** `tools/knowledge/search_knowledge.py`.

```python
from __future__ import annotations

import argparse
from pathlib import Path

from knowledge_config import KnowledgeConfig
from lexical_index import LexicalIndex
from retrieval_service import RetrievalService
from source_loader import load_documents, load_manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--visibility", action="append", required=True)
    parser.add_argument("--language")
    parser.add_argument("--tag", action="append", default=[])
    parser.add_argument("--limit", type=int, default=5)
    args = parser.parse_args()

    root = Path.cwd().resolve()
    config = KnowledgeConfig(root)
    config.validate()
    documents = load_documents(
        config.source_root, load_manifest(config.manifest_path)
    )
    service = RetrievalService(LexicalIndex(documents), None, None)
    hits = service.search(
        args.query,
        set(args.visibility),
        args.language,
        set(args.tag),
        args.limit,
    )
    for hit in hits:
        print(f"[{hit.retrieval_mode}] {hit.score:.4f} {hit.source_id}")
        print(hit.text[:400].replace("\n", " "))
    return 0 if hits else 2


if __name__ == "__main__":
    raise SystemExit(main())
```

`argparse` convertit les arguments. `action="append"` autorise plusieurs occurrences. `required=True` impose une visibilité issue de la politique appelante. `type=int` convertit la limite. Le code `0` signifie résultat ; `2` signifie aucun résultat dans cette convention d’outil.

> **[PS] PowerShell 7 — Tester le repli lexical après matérialisation :**

```powershell
.\.venv-knowledge\Scripts\python.exe .\tools\knowledge\search_knowledge.py `
  "Comment ouvrir la porte nord ?" `
  --visibility internal `
  --language fr `
  --tag beacon
```

> **[SORTIE] PowerShell — Exemple illustratif :**

```text
[lexical] 2.0000 knowledge.beacons.north-gate
# Balise de la porte nord ...
```

Le nombre est illustratif. Il ne provient pas d’une exécution conservée.

## 22. Évaluer la récupération

Une démonstration réussie ne suffit pas. Il faut des questions stables et des sources attendues.

> **[VSC] Visual Studio Code — Créer :** `knowledge/evaluation/retrieval-cases.json`.

```json
{
  "format": "project-asteria-retrieval-evaluation",
  "format_version": 1,
  "cases": [
    {
      "case_id": "north-gate-opening",
      "query": "Comment ouvrir la porte nord ?",
      "allowed_visibility": ["internal"],
      "language": "fr",
      "required_tags": ["beacon"],
      "expected_source_ids": ["knowledge.beacons.north-gate"]
    }
  ]
}
```

> **[VSC] Visual Studio Code — Créer :** `tools/knowledge/evaluate_retrieval.py`.

```python
from __future__ import annotations

import json
from pathlib import Path


def reciprocal_rank(found: list[str], expected: set[str]) -> float:
    for rank, source_id in enumerate(found, start=1):
        if source_id in expected:
            return 1.0 / rank
    return 0.0


def evaluate(service, path: Path, limit: int = 5) -> tuple[float, float]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("format") != "project-asteria-retrieval-evaluation":
        raise ValueError("Format d’évaluation inconnu.")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("Une liste de cas non vide est obligatoire.")

    hits_at_k = 0
    rr_total = 0.0
    for case in cases:
        expected = set(case["expected_source_ids"])
        hits = service.search(
            case["query"],
            set(case["allowed_visibility"]),
            case.get("language"),
            set(case.get("required_tags", [])),
            limit,
        )
        found = [hit.source_id for hit in hits]
        if expected.intersection(found):
            hits_at_k += 1
        rr_total += reciprocal_rank(found, expected)

    count = len(cases)
    return hits_at_k / count, rr_total / count
```

`reciprocal_rank()` retourne `1/rang` pour le premier résultat attendu. `hit-rate@k` mesure la proportion de cas où une source attendue apparaît dans les `k` premiers. MRR récompense un rang plus élevé.

Le jeu d’évaluation doit être indépendant du corpus d’exemples et conserver les échecs. Retirer un cas difficile pour améliorer la métrique invalide la comparaison.

## 23. Mise à jour et réindexation

Une source doit être remplacée lorsque changent :

- son contenu ;
- son titre ou chemin ;
- sa langue, visibilité ou ses tags ;
- le modèle ;
- la stratégie de découpage ;
- la dimension ;
- le schéma de payload.

Une évolution incompatible crée une nouvelle collection, par exemple `asteria_knowledge_v2`. Le mode Studio construit une collection de staging, l’évalue, puis bascule un alias. Le mode Solo peut reconstruire l’index hors session de jeu.

Le dossier `var/knowledge/qdrant/` est exclu de Git et des slots de sauvegarde. Il peut être effacé puis régénéré.

## 24. Confidentialité et autorisations

La visibilité du manifeste décrit une classification. Elle ne constitue pas une autorisation accordée à l’utilisateur.

La couche appelante doit calculer `allowed_visibility` depuis une politique fiable. Une requête ne peut pas demander elle-même `restricted`.

Chaque résultat conserve :

- `source_id` ;
- chemin ;
- révision ;
- hash ;
- modèle ;
- schéma ;
- mode de récupération.

Une donnée personnelle, un secret, une clé d’API ou un document non autorisé ne doit jamais entrer dans le corpus par défaut.

## 25. Parcours Solo

Le parcours Solo retient :

- un seul corpus local ;
- CPU de référence ;
- Qdrant Local Mode ;
- reconstruction manuelle ;
- repli lexical ;
- une petite campagne d’évaluation ;
- aucun service réseau obligatoire au runtime.

Critère : supprimer `var/knowledge/qdrant/` ne détruit aucune connaissance d’autorité.

## 26. Parcours Studio

Le parcours Studio ajoute :

- propriétaire du corpus et du schéma ;
- revue des sources et licences ;
- collection de staging ;
- alias et rollback ;
- jeu d’évaluation versionné ;
- seuils de régression ;
- mesures CPU, RAM, disque et latence ;
- procédure de suppression ;
- inventaire des copies dérivées ;
- fonctionnement hors ligne qualifié.

## 27. Erreurs fréquentes, pièges et corrections

<!-- qa:error-correction-section -->

### 27.1 Traiter l’index comme la source d’autorité

**Symptôme :** supprimer Qdrant détruit la seule copie du texte.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```text
Les textes n’existent que dans le payload Qdrant.
```

**Correction :** conserver les documents canoniques.

> **[LECTURE] Architecture corrigée — Référence.**

```text
sources versionnées → découpage → embeddings → index dérivé
```

**Différence :** l’index peut être migré ou supprimé sans perte d’autorité.

### 27.2 Copier une sauvegarde dans l’index

**Symptôme :** le chargement dépend d’un modèle ou d’un index absent.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
payload["save_game"] = complete_save_document
```

**Correction :** garder le snapshot dans le contrat du chapitre 9.

> **[LECTURE] Flux corrigé — Référence.**

```text
sauvegarde → SaveCoordinator
connaissance → KnowledgeIndex
```

**Différence :** reconstruction de partie et recherche restent indépendantes.

### 27.3 Compter les caractères au lieu des tokens

**Symptôme :** certains fragments dépassent la fenêtre du modèle.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
if len(text) <= 480:
    accept(text)
```

**Correction :** compter avec le tokenizer réel.

> **[LECTURE] Exemple corrigé — Référence.**

```python
count = len(tokenizer.encode(text, add_special_tokens=False))
```

**Différence :** la limite correspond à l’unité réellement consommée.

### 27.4 Tronquer silencieusement un passage

**Symptôme :** la conclusion utile disparaît sans diagnostic.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
encoded = encoded[:480]
```

**Correction :** découper aux phrases et refuser une phrase toujours excessive.

> **[LECTURE] Flux corrigé — Référence.**

```text
paragraphe → phrases → fragments validés ou erreur explicite
```

**Différence :** aucune information n’est perdue silencieusement.

### 27.5 Mélanger les préfixes E5

**Symptôme :** la qualité chute malgré des vecteurs valides.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
model.encode([document, query])
```

**Correction :** distinguer documents et requêtes.

> **[LECTURE] Exemple corrigé — Référence.**

```python
model.encode("passage: " + document)
model.encode("query: " + query)
```

**Différence :** chaque texte reçoit le rôle attendu par le modèle.

### 27.6 Changer la dimension en silence

**Symptôme :** l’insertion échoue ou mélange des espaces incompatibles.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
vector_size = len(first_vector)
reuse_existing_collection()
```

**Correction :** vérifier le contrat et créer une nouvelle collection.

> **[LECTURE] Architecture corrigée — Référence.**

```text
modèle ou dimension modifié → asteria_knowledge_v2 → réindexation
```

**Différence :** deux espaces vectoriels incompatibles ne sont jamais confondus.

### 27.7 Insérer sans retirer l’ancienne révision

**Symptôme :** la recherche retourne plusieurs versions contradictoires.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
client.upsert(points=new_points)
```

**Correction :** remplacer par `source_id`.

> **[LECTURE] Flux corrigé — Référence.**

```text
filtrer source_id → supprimer → insérer nouvelle révision
```

**Différence :** une seule révision active reste interrogeable.

### 27.8 Oublier une source supprimée

**Symptôme :** un document retiré reste trouvable.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
for document in manifest:
    index(document)
```

**Correction :** comparer déclarés et indexés.

> **[LECTURE] Exemple corrigé — Référence.**

```python
for stale in indexed_ids - declared_ids:
    delete_source(stale)
```

**Différence :** la suppression canonique est propagée à l’index dérivé.

### 27.9 Laisser la requête choisir ses droits

**Symptôme :** un appelant demande une visibilité restreinte.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
allowed_visibility = set(request.json["visibility"])
```

**Correction :** calculer les droits depuis une politique fiable.

> **[LECTURE] Architecture corrigée — Référence.**

```text
identité authentifiée → politique → visibilités autorisées → filtre
```

**Différence :** les droits ne viennent plus d’une valeur contrôlée par la requête.

### 27.10 Interpréter le score comme une probabilité

**Symptôme :** l’interface affiche « réponse vraie à 82 % ».

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
score 0,82 = 82 % de vérité
```

**Correction :** présenter le score comme un signal de classement.

> **[LECTURE] Formulation corrigée — Référence.**

```text
Score de similarité interne ; vérifier le passage et sa provenance.
```

**Différence :** la propriété réelle du score est respectée.

### 27.11 Promettre une accélération AMD

**Symptôme :** le guide affirme utiliser le GPU sans journal d’exécution.

> **[LECTURE] Exemple fautif — Ne pas recopier.**

```text
La RX 6750 XT accélère automatiquement Sentence Transformers.
```

**Correction :** conserver le CPU et qualifier chaque backend.

> **[LECTURE] Formulation corrigée — Référence.**

```text
CPU validé d’abord ; WinML, DirectML ou MIGraphX seulement après mesure.
```

**Différence :** aucune capacité matérielle non testée n’est revendiquée.

### 27.12 Construire le repli après le modèle

**Symptôme :** le téléchargement échoue et aucun repli n’existe.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
model = SentenceTransformer(name)
lexical = LexicalIndex(load_sources())
```

**Correction :** charger les sources et le repli avant les dépendances vectorielles.

> **[LECTURE] Ordre corrigé — Référence.**

```text
sources → lexical → tentative modèle et Qdrant → service
```

**Différence :** l’indisponibilité vectorielle ne supprime plus la recherche minimale.

### 27.13 Masquer une erreur de contrat par le repli

**Symptôme :** une dimension invalide devient un résultat lexical sans alerte.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```python
except Exception:
    return lexical.search(query)
```

**Correction :** intercepter uniquement les indisponibilités prévues.

> **[LECTURE] Exemple corrigé — Référence.**

```python
except (OSError, RuntimeError):
    return lexical.search(query)
```

**Différence :** les erreurs de configuration restent visibles et corrigibles.

### 27.14 Versionner le dossier Qdrant

**Symptôme :** Git contient des fichiers binaires volumineux et dépendants d’une version.

> **[LECTURE] Exemple fautif — Ne pas utiliser.**

```text
git add var/knowledge/qdrant/
```

**Correction :** versionner sources, manifeste et évaluations seulement.

> **[LECTURE] Organisation corrigée — Référence.**

```text
Git : knowledge/ + outils + évaluations
Ignoré : var/knowledge/qdrant/ + caches
```

**Différence :** le dépôt conserve l’autorité et non un artefact reconstructible.

## 28. Diagnostic

### 28.1 Le modèle ne se charge pas

Vérifier l’environnement actif, l’espace disque, le cache local et la disponibilité du modèle. Le service doit rester capable de construire le repli lexical.

### 28.2 Dimension incompatible

Ne pas modifier la collection existante silencieusement. Créer une nouvelle collection, reconstruire puis évaluer.

### 28.3 Aucun résultat

Contrôler la visibilité, la langue, les tags, le corpus déclaré et le mode de récupération. Un filtre trop strict est différent d’une panne.

### 28.4 Résultats anciens

Comparer la révision du payload à l’empreinte de la source. Vérifier la suppression des points avant le remplacement.

## 29. Critères d’acceptation

Le chapitre est compris lorsque le lecteur peut montrer que :

- les sources survivent à la suppression de l’index ;
- les fragments respectent le tokenizer et `max_tokens` ;
- chaque point possède une provenance ;
- le modèle, la dimension et le schéma sont vérifiés ;
- une source modifiée remplace l’ancienne révision ;
- une source retirée disparaît ;
- la visibilité est imposée par une politique ;
- le repli lexical fonctionne sans modèle ;
- l’évaluation calcule hit-rate et MRR ;
- aucun test runtime ou GPU non exécuté n’est revendiqué.

## 30. Checklist Solo

- [ ] Créer l’environnement Python.
- [ ] Créer le manifeste et les sources.
- [ ] Valider les chemins et identifiants.
- [ ] Découper avec le tokenizer.
- [ ] Construire les embeddings CPU.
- [ ] Créer la collection locale.
- [ ] Synchroniser suppressions et remplacements.
- [ ] Construire le repli lexical.
- [ ] Ajouter des cas d’évaluation.
- [ ] Exclure `var/` de Git et des sauvegardes.

## 31. Checklist Studio

- [ ] Nommer un propriétaire du corpus.
- [ ] Inventorier modèles et licences.
- [ ] Versionner schéma et stratégie de découpage.
- [ ] Utiliser staging, alias et rollback.
- [ ] Définir des seuils de régression.
- [ ] Mesurer CPU, RAM, disque et latence.
- [ ] Auditer les visibilités et suppressions.
- [ ] Qualifier le fonctionnement hors ligne.
- [ ] Préparer la migration vers le mode serveur.

## 32. Sources techniques

Sources principales vérifiées le 19 juillet 2026 :

- [Sentence Transformers — Semantic Search](https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html) ;
- [Hugging Face — intfloat/multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small) ;
- [Hugging Face — configuration du modèle](https://huggingface.co/intfloat/multilingual-e5-small/blob/main/config.json) ;
- [Qdrant Client — dépôt officiel et Local Mode](https://github.com/qdrant/qdrant-client) ;
- [Qdrant — Collections](https://qdrant.tech/documentation/manage-data/collections/) ;
- [Qdrant — Points](https://qdrant.tech/documentation/manage-data/points/) ;
- [Qdrant — Payload](https://qdrant.tech/documentation/concepts/payload/) ;
- [Qdrant — Filtering](https://qdrant.tech/documentation/search/filtering/) ;
- [ONNX Runtime — DirectML](https://onnxruntime.ai/docs/execution-providers/DirectML-ExecutionProvider.html) ;
- [ONNX Runtime — ROCm](https://onnxruntime.ai/docs/execution-providers/ROCm-ExecutionProvider.html) ;
- [ONNX Runtime — MIGraphX](https://onnxruntime.ai/docs/execution-providers/MIGraphX-ExecutionProvider.html).

## 33. Réserves de validation

Le chapitre reste au niveau `static-review`.

Ne sont pas exécutés : installation des dépendances, téléchargement du modèle, tokenisation réelle, vérification runtime de la dimension, création et interrogation Qdrant, filtres, remplacements, suppressions, campagne d’évaluation, fonctionnement hors ligne, WinML, DirectML, MIGraphX, intégration Godot et export Windows.

Les extraits Python ont seulement fait l’objet d’une compilation syntaxique locale. Cette compilation ne charge aucune dépendance et ne valide aucun comportement.

Aucun PDF intermédiaire n’est construit.

## 34. Résultat attendu

`Project Asteria` possède désormais un contrat de connaissance locale : sources d’autorité, fragments déterministes, embeddings multilingues, index dérivé, provenance, filtres, synchronisation, repli lexical et évaluation.

Le chapitre 11 pourra introduire la communication depuis Godot sans déplacer ces responsabilités dans les scènes de gameplay.
