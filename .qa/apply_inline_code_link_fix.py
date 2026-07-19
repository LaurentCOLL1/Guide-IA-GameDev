#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
validator_path = ROOT / "tools/validate_chapters.py"
audit_path = ROOT / "Livre-II/QA/AUDIT-CHAPITRE-07.md"
continuity_path = ROOT / "CONTINUITE-PROJET.md"

validator = validator_path.read_text(encoding="utf-8")
validator = validator.replace(
    'LINK_RE = re.compile(r"(?<!!)\\[[^\\]]*\\]\\(([^)]+)\\)")\n',
    'LINK_RE = re.compile(r"(?<!!)\\[[^\\]]*\\]\\(([^)]+)\\)")\nINLINE_CODE_RE = re.compile(r"(`+)([^\\n]*?)\\1")\n',
    1,
)
validator = validator.replace(
    '    markdown_text = text_without_fenced_code(text)\n    for raw_target in LINK_RE.findall(markdown_text):',
    '    markdown_text = text_without_fenced_code(text)\n    markdown_text = INLINE_CODE_RE.sub("", markdown_text)\n    for raw_target in LINK_RE.findall(markdown_text):',
    1,
)
validator_path.write_text(validator, encoding="utf-8")

audit = audit_path.read_text(encoding="utf-8")
audit = audit.replace(
'''### Risque 19 — exemples corrigés incompatibles avec les contrats déjà définis

**Correction :** seconde relecture des noms publics : utilisation de `cooldown_remaining`, `tick()`, `record_activation()`, du constructeur `BeaconRuntimeState.new(profile)`, de `BeaconJsonMapper.from_dictionary()` sur une instance et de `BeaconCatalog.register()`.''',
'''### Risque 19 — exemples corrigés incompatibles avec les contrats déjà définis

**Correction :** seconde relecture des noms publics : utilisation de `cooldown_remaining`, `tick()`, `record_activation()`, du constructeur `BeaconRuntimeState.new(profile)`, de `BeaconJsonMapper.from_dictionary()` sur une instance et de `BeaconCatalog.register()`.

### Risque 20 — code inline interprété comme lien Markdown

**Correction :** le validateur de liens ignore désormais les blocs clôturés et les expressions placées entre backticks, par exemple `Array[StringName](...)`.'''
)
audit_path.write_text(audit, encoding="utf-8")

continuity = continuity_path.read_text(encoding="utf-8")
continuity = continuity.replace(
    '- chapitre 7 porté en version `1.1.0`.',
    '- chapitre 7 porté en version `1.1.0` ;\n- validateur de liens renforcé pour ignorer le code inline entre backticks.',
    1,
)
continuity_path.write_text(continuity, encoding="utf-8")

print("Validateur de liens et preuves QA corrigés.")
