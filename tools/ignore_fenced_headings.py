#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
validator = root / "tools/validate_chapters.py"
text = validator.read_text(encoding="utf-8")
old = '''    headings: list[tuple[int, int, str]] = []
    for index, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if match:
            headings.append((index, len(match.group(1)), match.group(2).strip()))
'''
new = '''    headings: list[tuple[int, int, str]] = []
    in_fence = False
    fence_char = ""
    fence_length = 0
    for index, line in enumerate(lines):
        fence_match = FENCE_RE.match(line.strip())
        if fence_match:
            fence = fence_match.group("fence")
            if not in_fence:
                in_fence = True
                fence_char = fence[0]
                fence_length = len(fence)
            elif fence[0] == fence_char and len(fence) >= fence_length:
                in_fence = False
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if match:
            headings.append((index, len(match.group(1)), match.group(2).strip()))
'''
if old not in text:
    raise SystemExit("Heading collection block not found")
text = text.replace(old, new, 1)
validator.write_text(text, encoding="utf-8")

for rel in ("tools/ignore_fenced_headings.py", ".github/workflows/ignore-fenced-headings.yml"):
    path = root / rel
    if path.exists():
        path.unlink()
print("Fenced code headings ignored.")
