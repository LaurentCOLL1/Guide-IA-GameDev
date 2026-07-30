-- Normalise les liens internes après le traitement multifichier de Pandoc.
-- La réparation est conservatrice : un fragment n'est remplacé que si la
-- cible exacte est absente et qu'une variante à tirets normalisés existe.

function Pandoc(doc)
  local identifiers = {}

  doc:walk({
    Header = function(element)
      if element.identifier and element.identifier ~= "" then
        identifiers[element.identifier] = true
      end
    end,
    Div = function(element)
      if element.identifier and element.identifier ~= "" then
        identifiers[element.identifier] = true
      end
    end,
    Span = function(element)
      if element.identifier and element.identifier ~= "" then
        identifiers[element.identifier] = true
      end
    end,
  })

  return doc:walk({
    Link = function(element)
      local target = element.target or ""
      if target:sub(1, 1) ~= "#" then
        return nil
      end

      local identifier = target:sub(2)
      if identifiers[identifier] then
        return nil
      end

      local collapsed = identifier:gsub("%-%-+", "-")
      if collapsed ~= identifier and identifiers[collapsed] then
        element.target = "#" .. collapsed
        return element
      end

      return nil
    end,
  })
end
