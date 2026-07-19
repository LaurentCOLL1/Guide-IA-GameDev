from pathlib import Path

path = Path("tools/qa/tmp_refine_code_explanations_ch15_ch16.py")
text = path.read_text(encoding="utf-8")
text = text.replace(
    'return "\\n".join(lines[max(0, start - 18):start]).lower()',
    'return "\\n".join(lines[max(0, start - 8):start]).lower()',
    1,
)
text = text.replace(
    'faulty_words = ["exemple fautif", "mauvaise", "incorrect", "anti-pattern", "ne pas utiliser", "erreur"]',
    'faulty_words = ["exemple fautif", "mauvaise pratique", "mauvaise normalisation", "anti-pattern", "ne pas utiliser", "à éviter"]',
    1,
)
text = text.replace(
    'corrected_words = ["exemple corrig", "correction", "version correcte", "bonne pratique"]',
    'corrected_words = ["exemple corrig", "version corrigée", "correction appliquée", "bonne pratique"]',
    1,
)
path.write_text(text, encoding="utf-8")
