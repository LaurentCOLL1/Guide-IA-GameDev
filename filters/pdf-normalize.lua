-- Normalisation du livrable PDF destiné au lecteur.
-- Le filtre protège les métadonnées globales, retire quelques pictogrammes
-- absents des polices choisies et exclut les éléments de fabrication éditoriale
-- qui appartiennent au dépôt de conception, pas au manuel commercial.

local function plain_text(block)
  local text = pandoc.utils.stringify(block):lower()
  text = text:gsub("’", "'")
  text = text:gsub("‘", "'")
  return text
end

local process_headings = {
  "audit post",
  "audit transversal des contextes d'utilisation",
  "assurance qualité",
  "checklist d'audit",
  "limites de l'audit statique",
  "niveau de raisonnement",
  "politique pdf",
  "tests à préparer",
}

local process_block_phrases = {
  "rapport d'audit post-création",
  "rapport d'audit post-creation",
  "sources principales relues pour l'audit statique",
  "présent audit documentaire",
  "present audit documentaire",
  "cette sortie est une cible documentaire ; elle n'a pas été obtenue dans cet audit",
  "reste donc au niveau static-review",
  "reste au niveau static-review",
  "accepté au niveau static-review",
  "accepte au niveau static-review",
  "instructions concernant le chapitre suivant restent exclusivement dans continuite-projet.md",
  "validation transversale, les réserves runtime et le pdf complet restent à traiter",
  "un chapitre ne peut être déclaré audité",
  "un chapitre ne peut etre declare audite",
  "rapport qa final",
  "validation transversale et publication du livre ii",
}

local function is_process_heading(header)
  local heading = plain_text(header)
  for _, phrase in ipairs(process_headings) do
    if heading:find(phrase, 1, true) then
      return true
    end
  end
  return false
end

local function is_process_block(block)
  local text = plain_text(block)
  if text:match("/qa/")
     or text:match("audit%-chapitre")
     or text:match("protocole%-audit%-post%-creation") then
    return true
  end
  for _, phrase in ipairs(process_block_phrases) do
    if text:find(phrase, 1, true) then
      return true
    end
  end
  return false
end

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

function Pandoc(document)
  local output = pandoc.List()
  local skipped_level = nil

  for _, block in ipairs(document.blocks) do
    if block.t == "Header" then
      if skipped_level ~= nil and block.level <= skipped_level then
        skipped_level = nil
      end
      if skipped_level == nil and is_process_heading(block) then
        skipped_level = block.level
      elseif skipped_level == nil then
        output:insert(block)
      end
    elseif skipped_level == nil and not is_process_block(block) then
      output:insert(block)
    end
  end

  document.blocks = output
  return document
end
