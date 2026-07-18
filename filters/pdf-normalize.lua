-- Normalisation du livrable PDF.
-- Ce filtre empêche les métadonnées YAML des chapitres et index de remplacer
-- les métadonnées globales du guide, puis retire trois pictogrammes absents
-- des polices DejaVu utilisées par XeLaTeX.

function Meta(meta)
  meta.title = pandoc.MetaString("Guide réaliste de création de jeux vidéo 3D avec IA locale")
  meta.subtitle = pandoc.MetaString("Godot, Blender, ComfyUI, Open WebUI et outils open source locaux")
  meta.author = pandoc.MetaList({ pandoc.MetaString("Laurent Collin") })
  return meta
end

function Str(element)
  element.text = element.text:gsub("🟢", "")
  element.text = element.text:gsub("👤", "")
  element.text = element.text:gsub("👥", "")
  return element
end
