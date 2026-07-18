from pathlib import Path

path = Path(__file__).resolve().parent / "deepen_gdscript_chapter.py"
text = path.read_text(encoding="utf-8")
text = text.replace("### 18.3 Paramètres nommés", "### 18.3 Fonction privée conventionnelle")
old_anchor = '''anchor2 = """\treturn "%s %s" % [prefix, actor_name]
```

### 18.3 Fonction privée conventionnelle"""'''
new_anchor = '''anchor2 = """\treturn "%s %s" % [prefix, actor_name]
```

Les paramètres possédant une valeur par défaut sont placés après les paramètres obligatoires."""'''
old_insert_end = '''- `format_actor_name("Aster", "Capitaine")` renvoie `Capitaine Aster`.

### 18.3 Fonction privée conventionnelle"""'''
new_insert_end = '''- `format_actor_name("Aster", "Capitaine")` renvoie `Capitaine Aster`.

Les paramètres possédant une valeur par défaut sont placés après les paramètres obligatoires."""'''
if old_anchor not in text:
    raise RuntimeError("Ancre du paramètre par défaut absente")
if old_insert_end not in text:
    raise RuntimeError("Fin d’insertion du paramètre par défaut absente")
text = text.replace(old_anchor, new_anchor, 1)
text = text.replace(old_insert_end, new_insert_end, 1)
path.write_text(text, encoding="utf-8", newline="\n")
print("Ancres du chapitre 18.2 corrigées.")
