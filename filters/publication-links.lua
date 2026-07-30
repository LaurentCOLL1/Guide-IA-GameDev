-- Résolution des liens pour les publications multifichiers.
-- Le filtre exploite les enveloppes créées par --file-scope, résout les liens
-- vers les sources incluses, externalise les ressources techniques absentes,
-- répare les anciens fragments lorsque la cible est identifiable, puis retire
-- les enveloppes afin de restaurer la structure normale du livre et de l'EPUB.

local repository_blob_base = "https://github.com/LaurentCOLL1/Guide-IA-GameDev/blob/main/"

local function decode_url(value)
  return (value:gsub("%%(%x%x)", function(hex)
    return string.char(tonumber(hex, 16))
  end))
end

local function normalize_path(value)
  local path = decode_url(tostring(value or "")):gsub("\\", "/")
  path = path:gsub("^%./", "")
  local parts = {}
  for part in path:gmatch("[^/]+") do
    if part == ".." then
      if #parts > 0 then
        table.remove(parts)
      end
    elseif part ~= "." and part ~= "" then
      table.insert(parts, part)
    end
  end
  return table.concat(parts, "/")
end

local function dirname(path)
  return path:match("^(.*)/[^/]+$") or ""
end

local function file_scope_id(path)
  return normalize_path(path):lower():gsub("/", "__")
end

local function canonical_identifier(value)
  local result = tostring(value or ""):lower()
  result = result:gsub("’", "")
  result = result:gsub("'", "")
  result = result:gsub("[%s%-%._:/]", "")
  return result
end

local function split_target(target)
  local path, fragment = target:match("^(.-)#(.*)$")
  if path == nil then
    return target, nil
  end
  return path, fragment
end

local function is_external(target)
  return target:match("^[%a][%w+%.%-]*:") ~= nil or target:sub(1, 2) == "//" or target:sub(1, 1) == "/"
end

local function is_document_path(path)
  local lower = path:lower()
  return lower:match("%.md$") ~= nil
      or lower:match("%.txt$") ~= nil
      or lower:match("%.ya?ml$") ~= nil
      or lower:match("%.json$") ~= nil
      or lower:match("%.csv$") ~= nil
end

local function root_like(path)
  return path:match("^Volume%-0/") ~= nil
      or path:match("^Livre%-[IVX]+/") ~= nil
      or path:match("^Companion%-Pack/") ~= nil
      or path:match("^docs/") ~= nil
      or path:match("^QA/") ~= nil
      or path:match("^LICENSE") ~= nil
      or path:match("^NOTICE") ~= nil
      or path:match("^README") ~= nil
      or path:match("^ROADMAP") ~= nil
      or path:match("^BUILD") ~= nil
      or path:match("^STYLE_GUIDE") ~= nil
      or path:match("^CONTRIBUTING") ~= nil
end

function Pandoc(doc)
  local publication_root = normalize_path(os.getenv("PUBLICATION_ROOT") or "")
  local input_paths = {}
  local input_ids = {}
  local path_by_id = {}

  for _, raw_input in ipairs(PANDOC_STATE.input_files or {}) do
    local path = normalize_path(raw_input)
    if publication_root ~= "" and path:sub(1, #publication_root + 1) == publication_root .. "/" then
      path = path:sub(#publication_root + 2)
    end
    local identifier = file_scope_id(path)
    table.insert(input_paths, path)
    input_ids[path] = identifier
    path_by_id[identifier] = path
  end

  local identifiers = {}
  local canonical_index = {}
  local primary_by_file_id = {}

  local function register_identifier(identifier)
    if identifier == nil or identifier == "" then
      return
    end
    identifiers[identifier] = true
    local key = canonical_identifier(identifier)
    if canonical_index[key] == nil then
      canonical_index[key] = identifier
    elseif canonical_index[key] ~= identifier then
      canonical_index[key] = false
    end
  end

  doc:walk({
    Header = function(element)
      register_identifier(element.identifier)
    end,
    Div = function(element)
      register_identifier(element.identifier)
    end,
    Span = function(element)
      register_identifier(element.identifier)
    end,
    CodeBlock = function(element)
      register_identifier(element.identifier)
    end,
  })

  for _, block in ipairs(doc.blocks) do
    if block.t == "Div" and path_by_id[block.identifier] ~= nil then
      local first_header = nil
      block:walk({
        Header = function(element)
          if first_header == nil and element.identifier ~= "" then
            first_header = element.identifier
          end
        end,
      })
      primary_by_file_id[block.identifier] = first_header
    end
  end

  local function identifier_candidate(identifier, current_file_id)
    if identifier == nil or identifier == "" then
      return current_file_id and primary_by_file_id[current_file_id] or nil
    end

    if primary_by_file_id[identifier] ~= nil then
      return primary_by_file_id[identifier]
    end

    local candidates = {}
    local seen = {}
    local function add(value)
      if value ~= nil and value ~= "" and not seen[value] then
        seen[value] = true
        table.insert(candidates, value)
      end
    end

    add(identifier)
    add(identifier:gsub("%-%-+", "-"))

    local prefix, suffix = identifier:match("^(.*)__(.+)$")
    if suffix ~= nil then
      add(suffix)
      add(suffix:gsub("%-%-+", "-"))
      if primary_by_file_id[prefix] ~= nil then
        add(primary_by_file_id[prefix])
      end
    elseif current_file_id ~= nil then
      add(current_file_id .. "__" .. identifier)
      add((current_file_id .. "__" .. identifier):gsub("%-%-+", "-"))
    end

    for _, candidate in ipairs(candidates) do
      if identifiers[candidate] then
        return candidate
      end
    end

    for _, candidate in ipairs(candidates) do
      local indexed = canonical_index[canonical_identifier(candidate)]
      if indexed and indexed ~= false then
        return indexed
      end
    end

    if prefix ~= nil and primary_by_file_id[prefix] ~= nil then
      return primary_by_file_id[prefix]
    end
    if current_file_id ~= nil then
      return primary_by_file_id[current_file_id]
    end
    return nil
  end

  local function find_input_path(raw_path, current_path)
    local root_candidate = normalize_path(raw_path)
    local current_dir = dirname(current_path or "")
    local relative_candidate = normalize_path((current_dir ~= "" and current_dir .. "/" or "") .. raw_path)

    if input_ids[relative_candidate] ~= nil then
      return relative_candidate
    end
    if input_ids[root_candidate] ~= nil then
      return root_candidate
    end

    local suffix_match = nil
    for _, input_path in ipairs(input_paths) do
      if input_path == root_candidate or input_path:sub(-#root_candidate - 1) == "/" .. root_candidate then
        if suffix_match ~= nil and suffix_match ~= input_path then
          return nil
        end
        suffix_match = input_path
      end
    end
    return suffix_match
  end

  local function repository_path(raw_path, current_path)
    local root_candidate = normalize_path(raw_path)
    if root_like(root_candidate) then
      return root_candidate
    end
    local current_dir = dirname(current_path or "")
    return normalize_path((current_dir ~= "" and current_dir .. "/" or "") .. raw_path)
  end

  local function rewrite_link(element, current_path, current_file_id)
    local target = element.target or ""
    if target == "" or is_external(target) then
      return nil
    end

    if target:sub(1, 1) == "#" then
      local resolved = identifier_candidate(target:sub(2), current_file_id)
      if resolved ~= nil and resolved ~= target:sub(2) then
        element.target = "#" .. resolved
        return element
      end
      return nil
    end

    local path, fragment = split_target(target)
    if not is_document_path(path) then
      return nil
    end

    local input_path = find_input_path(path, current_path)
    if input_path ~= nil then
      local file_id = input_ids[input_path]
      local resolved = nil
      if fragment ~= nil and fragment ~= "" then
        resolved = identifier_candidate(file_id .. "__" .. fragment, file_id)
      else
        resolved = primary_by_file_id[file_id]
      end
      if resolved ~= nil then
        element.target = "#" .. resolved
        return element
      end
    end

    local repo_path = repository_path(path, current_path):gsub(" ", "%%20")
    local external_target = repository_blob_base .. repo_path
    if fragment ~= nil and fragment ~= "" then
      external_target = external_target .. "#" .. fragment
    end
    element.target = external_target
    return element
  end

  local flattened = pandoc.List()
  for _, block in ipairs(doc.blocks) do
    if block.t == "Div" and path_by_id[block.identifier] ~= nil then
      local current_path = path_by_id[block.identifier]
      local current_file_id = block.identifier
      local walked = block:walk({
        Link = function(element)
          return rewrite_link(element, current_path, current_file_id)
        end,
      })
      for _, child in ipairs(walked.content) do
        flattened:insert(child)
      end
    else
      flattened:insert(block:walk({
        Link = function(element)
          return rewrite_link(element, nil, nil)
        end,
      }))
    end
  end

  doc.blocks = flattened
  return doc
end
