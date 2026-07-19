#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]

validator = root / "tools/validate_chapters.py"
text = validator.read_text(encoding="utf-8")
text = text.replace(
    'ERROR_HEADING_RE = re.compile(r"(?:erreurs? fréquentes|anti[- ]patterns?|symptômes fréquents|pièges fréquents)", re.IGNORECASE)',
    'ERROR_HEADING_RE = re.compile(r"(?:erreurs? fréquentes|anti[- ]patterns?|symptômes fréquents|pièges(?: fréquents)?|mauvaises pratiques|problèmes fréquents|diagnostics et corrections)", re.IGNORECASE)',
    1,
)
old = '''            if "**Différence :**" not in child_body:
                missing.append("explication de la différence")
'''
new = '''            has_labeled_difference = "**Différence :**" in child_body
            trailing_prose = ""
            if "Exemple corrigé" in child_body:
                corrected_part = child_body.split("Exemple corrigé", 1)[1]
                outside_fence: list[str] = []
                current_after_fence: list[str] = []
                in_fence = False
                saw_closed_fence = False
                fence_char = ""
                fence_length = 0
                for line in corrected_part.splitlines():
                    fence_match = FENCE_RE.match(line.strip())
                    if fence_match:
                        fence = fence_match.group("fence")
                        if not in_fence:
                            in_fence = True
                            fence_char = fence[0]
                            fence_length = len(fence)
                        elif fence[0] == fence_char and len(fence) >= fence_length:
                            in_fence = False
                            saw_closed_fence = True
                            current_after_fence = []
                        continue
                    if saw_closed_fence and not in_fence:
                        current_after_fence.append(line)
                outside_fence = [
                    line.strip()
                    for line in current_after_fence
                    if line.strip() and not line.lstrip().startswith((">", "<!--"))
                ]
                trailing_prose = normalize_paragraph(" ".join(outside_fence))
            if not has_labeled_difference and len(trailing_prose) < 45:
                missing.append("explication de la différence")
'''
if old not in text:
    raise SystemExit("Validator difference check not found")
text = text.replace(old, new, 1)
validator.write_text(text, encoding="utf-8")

chapter7 = root / "Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md"
text = chapter7.read_text(encoding="utf-8")
old = '''		continue
	catalog.add_profile(profile)
```

Le chapitre privilégie malgré tout'''
new = '''		continue
	var register_error := catalog.register(profile)
	if register_error != OK:
		push_error("Profil refusé : %s" % error_string(register_error))
```

Le chargeur corrigé utilise la méthode publique `register()` du catalogue et contrôle son code `Error` au lieu d’appeler une méthode inexistante.

Le chapitre privilégie malgré tout'''
if old not in text:
    raise SystemExit("Chapter 7 add_profile corrected example not found")
text = text.replace(old, new, 1)
chapter7.write_text(text, encoding="utf-8")

continuity = root / "CONTINUITE-PROJET.md"
text = continuity.read_text(encoding="utf-8")
old = '''- chapitre 2 : version `1.3.0` ;
- chapitres 3 à 7 : version `1.0.0` ;'''
new = '''- chapitre 1 : version `1.3.0` ;
- chapitre 2 : version `1.5.0` ;
- chapitres 3 à 6 : version `1.1.0` ;
- chapitre 7 : version `1.1.1` ;'''
if old not in text:
    raise SystemExit("Continuity version summary not found")
text = text.replace(old, new, 1)
continuity.write_text(text, encoding="utf-8")

for rel in ("tools/finalize_error_rule.py", ".github/workflows/finalize-error-rule.yml"):
    path = root / rel
    if path.exists():
        path.unlink()

print("Final semantic rule patch applied.")
