CREATE TABLE content_document (
    document_id TEXT PRIMARY KEY,
    title TEXT NOT NULL CHECK (length(title) BETWEEN 1 AND 200),
    body TEXT NOT NULL,
    language_code TEXT NOT NULL CHECK (length(language_code) BETWEEN 2 AND 16),
    content_version INTEGER NOT NULL DEFAULT 1 CHECK (content_version >= 1),
    updated_at_utc TEXT NOT NULL
) STRICT;

CREATE TABLE content_tag (
    tag_id TEXT PRIMARY KEY,
    label TEXT NOT NULL UNIQUE CHECK (length(label) BETWEEN 1 AND 80)
) STRICT;

CREATE TABLE content_document_tag (
    document_id TEXT NOT NULL,
    tag_id TEXT NOT NULL,
    PRIMARY KEY (document_id, tag_id),
    FOREIGN KEY (document_id)
        REFERENCES content_document(document_id)
        ON DELETE CASCADE,
    FOREIGN KEY (tag_id)
        REFERENCES content_tag(tag_id)
        ON DELETE CASCADE
) WITHOUT ROWID;

CREATE INDEX idx_content_document_language_updated
    ON content_document(language_code, updated_at_utc);
