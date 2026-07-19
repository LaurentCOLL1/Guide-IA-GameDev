from pathlib import Path

path = Path("tools/patch_ch09_once.py")
lines = path.read_text(encoding="utf-8").splitlines()
result: list[str] = []
index = 0
removed = False

while index < len(lines):
    if (
        lines[index] == "replacements.append(("
        and index + 1 < len(lines)
        and lines[index + 1].startswith("'''Les limites :")
    ):
        removed = True
        index += 2
        while index < len(lines) and lines[index] != "'''))":
            index += 1
        if index >= len(lines):
            raise SystemExit("Unterminated obsolete replacement")
        index += 1
        continue

    result.append(lines[index])
    index += 1

if not removed:
    raise SystemExit("Obsolete replacement was not found")

path.write_text("\n".join(result) + "\n", encoding="utf-8")
