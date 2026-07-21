from __future__ import annotations

import base64
import gzip
import hashlib
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARTS = [HERE / f"refine_payload_{index}.txt" for index in range(1, 4)]
payload = "".join(path.read_text(encoding="utf-8").strip() for path in PARTS)
source_bytes = gzip.decompress(base64.b64decode(payload))
expected = "2236fdd3c995a3e89260fd7c91c659ca446f75bad80a61f3eb9254bf840a6cec"
actual = hashlib.sha256(source_bytes).hexdigest()
if actual != expected:
    raise RuntimeError(f"empreinte du script invalide: {actual}")
for path in PARTS:
    path.unlink()
SOURCE = source_bytes.decode("utf-8")

validator_boundary = '''def end_of_explanation(lines: list[str], start: int) -> int:
    structured_seen = False
    for index in range(start, len(lines)):
        line = lines[index]
        stripped = line.strip()
        if not stripped:
            continue
        if stripped == STRUCTURED:
            structured_seen = True
            continue
        if structured_seen and (line.startswith("- **") or line.startswith("  ")):
            continue
        if structured_seen:
            return index
    return len(lines)
'''
SOURCE, count = re.subn(
    r'def end_of_explanation\(lines: list\[str\], start: int\) -> int:\n.*?\n\ndef check\(',
    validator_boundary + '\n\ndef check(',
    SOURCE,
    count=1,
    flags=re.S,
)
if count != 1:
    raise RuntimeError("fonction de frontière du validateur introuvable")
SOURCE = SOURCE.replace(
    'end = end_of_explanation(lines, start + 1)',
    'end = end_of_explanation(lines, start)',
    1,
)

refinement_boundary = '''def explanation_end(lines: list[str], start: int) -> int:
    wrapper_seen = False
    for index in range(start, len(lines)):
        line = lines[index]
        stripped = line.strip()
        if not stripped:
            continue
        if stripped == WRAPPER:
            wrapper_seen = True
            continue
        if wrapper_seen and (line.startswith("- **") or line.startswith("  ")):
            continue
        if wrapper_seen:
            return index
    return len(lines)
'''
SOURCE, count = re.subn(
    r'def explanation_end\(lines: list\[str\], start: int\) -> int:\n.*?\n\ndef parse_bullets\(',
    refinement_boundary + '\n\ndef parse_bullets(',
    SOURCE,
    count=1,
    flags=re.S,
)
if count != 1:
    raise RuntimeError("fonction de frontière du raffinement introuvable")

SOURCE = SOURCE.replace(
    '        block = lines[start:end]\n        bullets = parse_bullets(block)',
    '        block = lines[start:end]\n        anchors = [line.strip() for line in block if re.match(r\'^\\s*<a id="[^"]+"></a>\\s*$\', line)]\n        block = [line for line in block if not re.match(r\'^\\s*<a id="[^"]+"></a>\\s*$\', line)]\n        bullets = parse_bullets(block)',
    1,
)
SOURCE = SOURCE.replace(
    '        replacement = format_points(points)\n        lines[start:end] = replacement',
    '        replacement = format_points(points)\n        for anchor in anchors:\n            replacement.extend([anchor, ""])\n        lines[start:end] = replacement',
    1,
)
SOURCE = SOURCE.replace(
    '        for segment in preserved_texts:\n            if segment not in rendered:\n                raise RuntimeError(f"chapitre {chapter}: segment antérieur perdu: {segment}")',
    '        normalized_rendered = re.sub(r"\\s+", " ", rendered).strip()\n        for segment in preserved_texts:\n            normalized_segment = re.sub(r"\\s+", " ", segment).strip()\n            if normalized_segment not in normalized_rendered:\n                raise RuntimeError(f"chapitre {chapter}: segment antérieur perdu: {segment}")',
    1,
)
SOURCE = SOURCE.replace(
    '            if len(points) < 4:\n                raise RuntimeError(f"chapitre {chapter}: moins de quatre rubriques spécifiques ligne {marker + 1}")',
    '''            if len(points) < 4 and code.strip():
                first_line = meaningful[0]
                last_line = meaningful[-1]
                identifiers = uniq(re.findall(r"[A-Za-z_][A-Za-z0-9_]*", code))
                micro_points = [
                    ("Instruction principale", f"L’instruction exacte est `{first_line}`."),
                    ("Symboles manipulés", "Les symboles visibles sont " + ", ".join(f"`{name}`" for name in identifiers[:8]) + "." if identifiers else f"Le littéral visible est `{first_line}`."),
                    ("Opération visible", f"La syntaxe de `{first_line}` montre l’opération locale réalisée par ce micro-extrait."),
                    ("Portée de l’extrait", f"Le bloc `{language or 'text'}` contient {len(meaningful)} ligne(s) significative(s) et se termine par `{last_line}`."),
                ]
                existing_labels = {label for label, _ in points}
                for label, value in micro_points:
                    if label not in existing_labels and len(points) < 4:
                        points.append((label, value))
                        existing_labels.add(label)
                points = group_points(points)
            if len(points) < 4:
                raise RuntimeError(f"chapitre {chapter}: moins de quatre rubriques spécifiques ligne {marker + 1}")''',
    1,
)

exec(compile(SOURCE, __file__, "exec"))
