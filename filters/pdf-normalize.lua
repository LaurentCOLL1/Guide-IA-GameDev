-- Normalisation du livrable PDF destiné au lecteur.
-- Le filtre protège les métadonnées globales, retire quelques pictogrammes
-- absents des polices choisies et exclut les sections de gouvernance QA qui
-- appartiennent au dépôt de conception, pas au manuel commercial.

local function plain_text(block)
  return pandoc.utils.stringify(block):lower()
end

local function is_process_section(header, section_blocks)
  local heading = plain_text(header)
  local body_parts = {}
  for _, block in ipairs(section_blocks) do
    table.insert(body_parts, plain_text(block))
  end
  local body = table.concat(body_parts, " ")

  if heading:match("audit post") or heading:match("checklist d.audit") then
    return true
  end
  if heading:match("niveau de raisonnement") or heading:match("politique pdf") then
    return true
  end
  if body:match("livre%-ii/qa/audit%-chapitre") then
    return true
  end
  if body:match("protocole%-audit%-post%-creation") then
    return true
  end
  if body:match("validation transversale et publication du livre ii") then
    return true
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
  local blocks = document.blocks
  local index = 1

  while index <= #blocks do
    local block = blocks[index]
    if block.t == "Header" then
      local level = block.level
      local section = pandoc.List()
      local cursor = index + 1
      while cursor <= #blocks do
        local candidate = blocks[cursor]
        if candidate.t == "Header" and candidate.level <= level then
          break
        end
        section:insert(candidate)
        cursor = cursor + 1
      end

      if not is_process_section(block, section) then
        output:insert(block)
        output:extend(section)
      end
      index = cursor
    else
      local text = plain_text(block)
      if not text:match("livre%-ii/qa/audit%-chapitre")
         and not text:match("protocole%-audit%-post%-creation") then
        output:insert(block)
      end
      index = index + 1
    end
  end

  document.blocks = output
  return document
end
