from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: attendu 1 occurrence, trouvé {count}")
    return text.replace(old, new, 1)


chapter_path = Path("Livre-III/CHAPITRE-08-Creation-des-animaux.md")
chapter = chapter_path.read_text(encoding="utf-8")
chapter = replace_once(
    chapter,
    "## 36. Erreurs fréquentes et corrections\n\n\n### 36.1 Utiliser un squelette humain pour tous les animaux",
    "## 36. Erreurs fréquentes et corrections\n\n<!-- qa:error-correction-section -->\n\n### 36.1 Utiliser un squelette humain pour tous les animaux",
    "marqueur de section d'erreurs",
)
chapter_path.write_text(chapter, encoding="utf-8")


audit_path = Path("Livre-III/QA/AUDIT-CHAPITRE-08.md")
audit = audit_path.read_text(encoding="utf-8")
audit = replace_once(
    audit,
    'audit-date: "2026-07-23T04:29:27+02:00"\n',
    'last-verified: "2026-07-23T04:29:27+02:00"\n'
    'audit-date: "2026-07-23T04:29:27+02:00"\n',
    "last-verified de l'audit",
)
audit = replace_once(audit, "- lignes : 1928 ;", "- lignes : 1929 ;", "lignes audit")
audit = replace_once(
    audit,
    "- titres Markdown de niveau 2 à 6 : 66 ;",
    "- titres Markdown comptés par le validateur : 67 ;",
    "titres audit",
)
audit = replace_once(
    audit,
    "- blocs significatifs retenus : 39 ;",
    "- blocs significatifs retenus : 32 ;",
    "blocs significatifs audit",
)
audit_path.write_text(audit, encoding="utf-8")


proof_path = Path("Livre-III/QA/VALIDATION-FINALE-CHAPITRE-08.yaml")
proof = proof_path.read_text(encoding="utf-8")
proof = replace_once(proof, "  chapter-lines: 1928", "  chapter-lines: 1929", "lignes preuve")
proof = replace_once(proof, "  chapter-headings: 66", "  chapter-headings: 67", "titres preuve")
proof_path.write_text(proof, encoding="utf-8")

print("Corrections de validation du chapitre 8 appliquées.")
