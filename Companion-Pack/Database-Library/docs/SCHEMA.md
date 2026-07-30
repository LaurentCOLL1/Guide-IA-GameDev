# Schéma et diagrammes

## Vue relationnelle

```mermaid
erDiagram
    schema_migrations {
        INTEGER version PK
        TEXT name UK
        TEXT checksum
        TEXT applied_at_utc
    }
    beacon_state {
        TEXT beacon_id PK
        INTEGER is_enabled
        INTEGER activation_count
        REAL cooldown_remaining
        TEXT last_activated_at_utc
        TEXT updated_at_utc
    }
    beacon_activation_event {
        INTEGER event_id PK
        TEXT beacon_id FK
        TEXT actor_id
        TEXT occurred_at_utc
    }
    content_document {
        TEXT document_id PK
        TEXT title
        TEXT body
        TEXT language_code
        INTEGER content_version
        TEXT updated_at_utc
    }
    content_tag {
        TEXT tag_id PK
        TEXT label UK
    }
    content_document_tag {
        TEXT document_id PK,FK
        TEXT tag_id PK,FK
    }
    derived_cache_entry {
        TEXT cache_key PK
        TEXT source_checksum
        TEXT payload_json
        TEXT created_at_utc
        TEXT expires_at_utc
    }

    beacon_state ||--o{ beacon_activation_event : owns
    content_document ||--o{ content_document_tag : receives
    content_tag ||--o{ content_document_tag : classifies
```

## Cycle de migration

```mermaid
flowchart TD
    A[Ouvrir la base] --> B[Lire application_id]
    B -->|étranger| X[Refus sans écriture]
    B --> C[Lire user_version]
    C -->|future| X
    C --> D[Vérifier historique et checksums]
    D -->|divergent| X
    D --> E[BEGIN IMMEDIATE]
    E --> F[Exécuter le SQL]
    F --> G[Insérer schema_migrations]
    G --> H[Mettre à jour user_version]
    H --> I[COMMIT]
    F -->|échec| R[ROLLBACK]
    G -->|échec| R
    H -->|échec| R
```

## Autorités

- `beacon_state` : état relationnel persistant courant ;
- `beacon_activation_event` : historique dépendant ;
- `content_document` : contenu canonique synthétique de démonstration ;
- `derived_cache_entry` : donnée dérivée supprimable ;
- `schema_migrations` : preuve technique d’application, pas autorité métier.
