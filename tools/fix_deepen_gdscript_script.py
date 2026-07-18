from pathlib import Path

path = Path(__file__).resolve().parent / "deepen_gdscript_chapter.py"
text = path.read_text(encoding="utf-8")
old = "### 18.3 Paramètres nommés"
new = "### 18.3 Fonction privée conventionnelle"
if old not in text:
    raise RuntimeError("Ancienne ancre absente du script de migration")
path.write_text(text.replace(old, new), encoding="utf-8", newline="\n")
print("Ancre du chapitre 18.3 corrigée.")

# Relance finale pour appliquer et committer le contenu pédagogique validé.
