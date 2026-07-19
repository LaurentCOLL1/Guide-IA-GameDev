from pathlib import Path

path = Path("tools/qa/tmp_enrich_code_explanations_ch15_ch16.py")
text = path.read_text(encoding="utf-8")
text = text.replace(
    "Correction pédagogique prioritaire avant tout nouveau chapitre:",
    "Correction pédagogique prioritaire avant tout nouveau chapitre :",
)
text = text.replace(
    "Chapitre suivant, bloqué jusqu’à la fermeture de cette correction:",
    "Chapitre suivant, bloqué jusqu’à la fermeture de cette correction :",
)
old = '''    pending = "- [ ] Correction pédagogique des blocs de code des chapitres 15 et 16 avant le chapitre 17."
    done = "- [x] Correction pédagogique des blocs de code des chapitres 15 et 16 — explications détaillées, audits et preuves QA révisés."
    roadmap = replace_once(roadmap, pending, done, "roadmap correction")
'''
new = '''    pending = """- [ ] Correction pédagogique du chapitre 15 — expliquer chaque bloc de code significatif avec rôle, types, paramètres, retours, effets, invariants et résultat attendu.
- [ ] Correction pédagogique du chapitre 16 — expliquer chaque bloc de code significatif avec rôle, types, paramètres, retours, effets, invariants et résultat attendu.
- [ ] Fermer les audits et preuves QA corrigés des chapitres 15 et 16 avant de commencer le chapitre 17."""
    done = """- [x] Correction pédagogique du chapitre 15 — blocs de code expliqués selon QA Q1.1.
- [x] Correction pédagogique du chapitre 16 — blocs de code expliqués selon QA Q1.1.
- [x] Audits et preuves QA corrigés des chapitres 15 et 16 fermés avant le chapitre 17."""
    roadmap = replace_once(roadmap, pending, done, "roadmap correction")
    roadmap = roadmap.replace(
        "Avant le chapitre 17, une correction pédagogique bloquante doit enrichir les explications des blocs de code des chapitres 15 et 16, puis fermer leurs audits et preuves QA mis à jour. Le chapitre 17 traitera ensuite",
        "La correction pédagogique des chapitres 15 et 16 est terminée et leurs audits et preuves QA sont révisés. Le chapitre 17 traitera désormais",
    )
'''
if old not in text:
    raise RuntimeError("roadmap source anchor not found")
path.write_text(text.replace(old, new, 1), encoding="utf-8")
