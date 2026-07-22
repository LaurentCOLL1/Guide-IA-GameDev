#!/usr/bin/env python3
from pathlib import Path

path = Path(".qa/ch28/review_patch.py")
text = path.read_text(encoding="utf-8")
old = '''proof = replace_once(proof, "    run-id: 29882825771", "    run-id: pending", "proof chapter run")
proof = replace_once(proof, "    conclusion: success", "    conclusion: pending", "proof chapter conclusion")
proof = replace_once(proof, "    run-id: 29882825815", "    run-id: pending", "proof context run")
proof = replace_once(proof, "    conclusion: success", "    conclusion: pending", "proof context conclusion")
proof = replace_once(proof, "    id: 8515408912", "    id: pending", "proof artifact id")
proof = replace_once(proof, "    digest: sha256:a23b5c03cda7db7868130dc66ecfe123a4229b46347d3a2aac57f331d00713be", "    digest: pending", "proof artifact digest")
proof = replace_once(proof, "  commit: e4d4b4a961abf9fde94082237b6ff1b0507d428a", "  commit: pending", "proof closure")'''
new = '''proof = replace_once(
    proof,
    "  validate-chapters-without-pdf:\\n    run-id: 29882825771\\n    conclusion: success",
    "  validate-chapters-without-pdf:\\n    run-id: pending\\n    conclusion: pending",
    "proof chapter workflow",
)
proof = replace_once(
    proof,
    "  validate-usage-contexts:\\n    run-id: 29882825815\\n    conclusion: success",
    "  validate-usage-contexts:\\n    run-id: pending\\n    conclusion: pending",
    "proof context workflow",
)
proof = replace_once(
    proof,
    "  artifact:\\n    id: 8515408912\\n    name: chapter-validation-without-pdf\\n    digest: sha256:a23b5c03cda7db7868130dc66ecfe123a4229b46347d3a2aac57f331d00713be",
    "  artifact:\\n    id: pending\\n    name: chapter-validation-without-pdf\\n    digest: pending",
    "proof artifact",
)
proof = replace_once(
    proof,
    "evidence-closure:\\n  commit: e4d4b4a961abf9fde94082237b6ff1b0507d428a\\n  conclusion: success",
    "evidence-closure:\\n  commit: pending\\n  conclusion: pending",
    "proof closure",
)'''
if text.count(old) != 1:
    raise RuntimeError(f"Expected one vulnerable proof block, found {text.count(old)}")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
print("Review patch proof targeting hardened.")
