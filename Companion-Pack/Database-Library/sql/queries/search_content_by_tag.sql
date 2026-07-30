SELECT
    d.document_id,
    d.title,
    d.language_code,
    d.content_version,
    d.updated_at_utc
FROM content_document AS d
JOIN content_document_tag AS dt
    ON dt.document_id = d.document_id
WHERE dt.tag_id = ?
ORDER BY d.updated_at_utc DESC, d.document_id ASC;
