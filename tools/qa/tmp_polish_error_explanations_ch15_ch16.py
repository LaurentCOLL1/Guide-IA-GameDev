from pathlib import Path
import re

CHAPTERS = {
    15: Path("Livre-II/CHAPITRE-15-Relations-sociales.md"),
    16: Path("Livre-II/CHAPITRE-16-Famille-et-generations.md"),
}
EVIDENCE = {
    15: Path("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-15.yaml"),
    16: Path("Livre-II/QA/VALIDATION-FINALE-CHAPITRE-16.yaml"),
}
AUDITS = {
    15: Path("Livre-II/QA/AUDIT-CHAPITRE-15.md"),
    16: Path("Livre-II/QA/AUDIT-CHAPITRE-16.md"),
}


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, got {count}")
    return text.replace(old, new, 1)


def capitalize_sentences(line: str) -> str:
    return re.sub(
        r"(?<=\.\s)([a-zà-ÿ])",
        lambda match: match.group(1).upper(),
        line,
    )


metrics = {}
for chapter, path in CHAPTERS.items():
    text = path.read_text(encoding="utf-8")
    heading = re.search(r"(?m)^##\s+.*(?:Erreurs fréquentes|Anti-patterns|Pièges).*$", text, re.IGNORECASE)
    if not heading:
        raise RuntimeError(f"chapter {chapter}: error section not found")
    prefix = text[: heading.start()]
    tail = text[heading.start() :]
    corrections = len(re.findall(r"(?m)^\*\*Correction :\*\*[^\n]*\n", tail))
    differences = len(re.findall(r"(?m)^\*\*Différence :\*\*[^\n]*\n", tail))
    tail = re.sub(r"(?m)^\*\*Correction :\*\*[^\n]*\n\n?", "", tail)
    tail = re.sub(r"(?m)^\*\*Différence :\*\*[^\n]*\n\n?", "", tail)
    lines = []
    for line in tail.splitlines():
        if line.startswith("- **Pourquoi la correction fonctionne :**"):
            line = capitalize_sentences(line)
        lines.append(line)
    text = prefix + "\n".join(lines) + "\n"
    if re.search(r"(?m)^\*\*(?:Correction|Différence) :\*\*", text[heading.start() :]):
        raise RuntimeError(f"chapter {chapter}: standalone correction/difference remains")
    path.write_text(text, encoding="utf-8")
    metrics[chapter] = {
        "standalone_corrections_removed": corrections,
        "standalone_differences_removed": differences,
        "lines": len(text.splitlines()),
    }

protocol_path = Path("Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md")
protocol = protocol_path.read_text(encoding="utf-8")
old = """Chaque sous-cas doit alors contenir :

1. un symptôme ou risque ;
2. un **exemple fautif** ;
3. une **correction** ;
4. un **exemple corrigé** ;
5. une explication explicite de la différence.
"""
new = """Chaque sous-cas doit alors contenir :

1. un symptôme ou risque ;
2. un **exemple fautif** suivi de `Pourquoi cet exemple est fautif` ;
3. un **exemple corrigé** suivi de `Pourquoi la correction fonctionne`.

Une ligne autonome `Correction` ou `Différence` n’est pas exigée lorsque son contenu est déjà intégré à ces deux explications. Le but est d’éviter la répétition sans supprimer l’analyse de l’invariant violé puis rétabli.
"""
if new not in protocol:
    protocol = replace_once(protocol, old, new, "protocol Q1.2 concise structure")
protocol_path.write_text(protocol, encoding="utf-8")

for chapter in CHAPTERS:
    audit_path = AUDITS[chapter]
    audit = audit_path.read_text(encoding="utf-8")
    addition = "- suppression des lignes autonomes `Correction` et `Différence` lorsque leur contenu est déjà intégré aux deux justifications ;"
    if addition not in audit:
        audit = audit.rstrip() + "\n\n" + addition + "\n"
    audit_path.write_text(audit, encoding="utf-8")

    evidence_path = EVIDENCE[chapter]
    evidence = evidence_path.read_text(encoding="utf-8")
    evidence = re.sub(r"(?m)^  chapter-lines: \d+$", f"  chapter-lines: {metrics[chapter]['lines']}", evidence, count=1)
    if "  standalone-correction-lines-removed:" not in evidence:
        anchor_line = "  corrected-explanations-simplified:"
        lines = evidence.splitlines()
        output = []
        inserted = False
        for line in lines:
            output.append(line)
            if line.startswith(anchor_line) and not inserted:
                output.append(f"  standalone-correction-lines-removed: {metrics[chapter]['standalone_corrections_removed']}")
                output.append(f"  standalone-difference-lines-removed: {metrics[chapter]['standalone_differences_removed']}")
                inserted = True
        evidence = "\n".join(output) + "\n"
    evidence_path.write_text(evidence, encoding="utf-8")

continuity_path = Path("CONTINUITE-PROJET.md")
continuity = continuity_path.read_text(encoding="utf-8")
needle = "- simplification des exemples fautifs et corrigés ;"
addition = "- suppression des lignes autonomes `Correction` et `Différence` lorsqu’elles répètent déjà les deux justifications ;"
if addition not in continuity:
    continuity = replace_once(continuity, needle, needle + "\n" + addition, "continuity concise error format")
continuity_path.write_text(continuity, encoding="utf-8")

metrics_path = Path("tmp_ch15_ch16_explanation_style_metrics.txt")
base = metrics_path.read_text(encoding="utf-8").rstrip()
if "chapter 15 polish:" not in base:
    base += "\n" + "\n".join(
        f"chapter {chapter} polish: " + ", ".join(f"{key}={value}" for key, value in values.items())
        for chapter, values in metrics.items()
    )
metrics_path.write_text(base + "\n", encoding="utf-8")
