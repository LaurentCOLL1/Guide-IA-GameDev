from pathlib import Path
import re

path = Path(__file__).resolve().parent / "deepen_gdscript_chapter.py"
text = path.read_text(encoding="utf-8")
text = text.replace("### 18.3 Paramètres nommés", "### 18.3 Fonction privée conventionnelle")

new_anchor = '''anchor2 = """\treturn "%s %s" % [prefix, actor_name]
```

Les paramètres possédant une valeur par défaut sont placés après les paramètres obligatoires."""'''
text, count = re.subn(
    r'anchor2 = """.*?"""\ninsert2 = ',
    new_anchor + '\ninsert2 = ',
    text,
    count=1,
    flags=re.DOTALL,
)
if count != 1:
    raise RuntimeError("Bloc anchor2 introuvable")

old_end = '### 18.3 Fonction privée conventionnelle"""\ntext = replace_once(text, anchor2, insert2)'
new_end = 'Les paramètres possédant une valeur par défaut sont placés après les paramètres obligatoires."""\ntext = replace_once(text, anchor2, insert2)'
if old_end not in text:
    raise RuntimeError("Fin du bloc insert2 introuvable")
text = text.replace(old_end, new_end, 1)

path.write_text(text, encoding="utf-8", newline="\n")
print("Ancres du chapitre 18.2 corrigées structurellement.")
