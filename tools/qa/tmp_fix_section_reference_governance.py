from pathlib import Path
import re


def once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected 1, got {count}')
    return text.replace(old, new, 1)


def version(text, old, new, label):
    pattern = rf'(?m)^version: "{re.escape(old)}"$'
    count = len(re.findall(pattern, text))
    if count != 1:
        raise RuntimeError(f'{label}: expected 1 exact version line, got {count}')
    return re.sub(pattern, f'version: "{new}"', text, count=1)

metrics = {}
for line in Path('tmp_precise_section_references_metrics.txt').read_text(encoding='utf-8').splitlines():
    chapter = int(re.search(r'chapter (\d+)', line).group(1))
    metrics[chapter] = {key: int(value) for key, value in re.findall(r'(\w+)=([0-9]+)', line)}

protocol_path = Path('Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md')
protocol = protocol_path.read_text(encoding='utf-8')
protocol = version(protocol, '1.7.0', '1.7.1', 'protocol version')
protocol = once(protocol, '- [ ] Les liens locaux sont résolus.',
    '- [ ] Les liens locaux sont résolus.\n- [ ] Chaque fragment interne vise une ancre existante et la sous-section la plus précise pertinente.', 'protocol fragment checklist')
old = 'Une explication peut être placée avant ou après le bloc, mais elle doit être immédiatement identifiable. Elle ne répète ni le chemin déjà affiché avant le code, ni une règle générale de syntaxe déjà présentée dans un chapitre de référence. Une rubrique `Rôle` qui reformule seulement le titre de la section est supprimée ; elle est conservée lorsqu’elle nomme un contrat, une fonction, une transformation ou une responsabilité concrète.'
new = old + ' Cette interdiction vaut pour toutes les rubriques : `Rôle`, `Pourquoi cet exemple est fautif`, `Pourquoi la correction fonctionne`, `Résultat attendu` ou toute formulation équivalente. Une explication ne peut jamais justifier un bloc en citant le titre de la section qui le contient ; elle énonce directement le fait technique, le risque ou l’invariant.'
protocol = once(protocol, old, new, 'protocol self-title rule')
old = 'Dans une section d’erreurs, d’anti-patterns, de pièges ou de corrections, le format privilégié est plus court : `Pourquoi cet exemple est fautif` sous le contre-exemple et `Pourquoi la correction fonctionne` sous la version corrigée. Un renvoi vers une section ou un chapitre antérieur peut être placé avant le code fautif lorsqu’il évite de répéter une règle déjà établie.'
new = old + ' Ce renvoi vise la sous-section exacte qui porte la règle ; une section parente n’est acceptable qu’en l’absence de cible plus précise. Son fragment doit être vérifié. Une ancre explicite et stable est privilégiée lorsque le fragment automatique du titre peut être ambigu, fragile ou dépendre du moteur Markdown.'
protocol = once(protocol, old, new, 'protocol precise link rule')
protocol_path.write_text(protocol, encoding='utf-8')

for chapter in (15, 16):
    m = metrics[chapter]
    audit_path = Path(f'Livre-II/QA/AUDIT-CHAPITRE-{chapter}.md')
    audit = audit_path.read_text(encoding='utf-8')
    audit = version(audit, '1.2.0', '1.2.1', f'audit {chapter} version')
    audit = once(audit, 'chapter-version: "1.2.0"', 'chapter-version: "1.2.1"', f'audit {chapter} chapter version')
    heading = '## Addendum 2026-07-20 — titres de section et renvois précis'
    if heading not in audit:
        audit = audit.rstrip() + f'''\n\n{heading}\n\nLa seconde lecture a vérifié toutes les rubriques d’explication et tous les renvois `À relire`.\n\n- auto-paraphrases du titre courant supprimées : **{m['self_title_removed']}** ;\n- descriptions de rôle factuellement erronées corrigées : **{m['roles_fixed']}** ;\n- renvois recâblés vers la sous-section exacte : **{m['links_fixed']}** ;\n- ancres explicites et stables ajoutées : **{m['anchors_added']}** ;\n- fragments vérifiés contre une ancre réellement présente ;\n- aucune modification du comportement GDScript revendiquée.\n\n**Décision révisée :** accepté au niveau `static-review` après correction éditoriale et navigationnelle.\n'''
    audit_path.write_text(audit, encoding='utf-8')

    evidence_path = Path(f'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-{chapter}.yaml')
    evidence = evidence_path.read_text(encoding='utf-8')
    evidence = re.sub(r'(?m)^status: (?:complete|pending-ci)$', 'status: pending-ci', evidence, count=1)
    evidence = re.sub(r'(?m)^validated-head-commit: .+$', 'validated-head-commit: pending-ci', evidence, count=1)
    evidence = once(evidence, '  version: 1.2.0', '  version: 1.2.1', f'evidence {chapter} version')
    evidence = re.sub(r'(?m)^  chapter-lines: \d+$', f"  chapter-lines: {m['lines']}", evidence, count=1)
    if 'section-reference-refinement:' not in evidence:
        evidence = evidence.rstrip() + f'''\n\nsection-reference-refinement:\n  policy: QA-Q1.1-precise-references\n  chapter: {chapter}\n  self-title-paraphrases-removed: {m['self_title_removed']}\n  incorrect-role-descriptions-corrected: {m['roles_fixed']}\n  reread-links-corrected: {m['links_fixed']}\n  explicit-target-anchors-added: {m['anchors_added']}\n  fragment-targets-verified: true\n  runtime-executed: false\n  ci-status: pending\n'''
    evidence_path.write_text(evidence, encoding='utf-8')

index_path = Path('Livre-II/index.md')
index = index_path.read_text(encoding='utf-8')
index = version(index, '1.11.0', '1.11.1', 'index version')
index = once(index,
    '15. [Relations sociales](CHAPITRE-15-Relations-sociales.md) — **rédigé, repéré, expliqué bloc par bloc sans répétitions éditoriales et audité au niveau static-review**',
    '15. [Relations sociales](CHAPITRE-15-Relations-sociales.md) — **rédigé, repéré, expliqué bloc par bloc sans répétitions éditoriales, avec renvois internes précis, et audité au niveau static-review**', 'index ch15')
index = once(index,
    '16. [Famille et générations](CHAPITRE-16-Famille-et-generations.md) — **rédigé, repéré, expliqué bloc par bloc sans répétitions éditoriales et audité au niveau static-review**',
    '16. [Famille et générations](CHAPITRE-16-Famille-et-generations.md) — **rédigé, repéré, expliqué bloc par bloc sans répétitions éditoriales, avec renvois internes précis, et audité au niveau static-review**', 'index ch16')
index_path.write_text(index, encoding='utf-8')

roadmap_path = Path('ROADMAP.md')
roadmap = roadmap_path.read_text(encoding='utf-8')
line = '- [x] Auto-paraphrases supprimées et renvois internes des chapitres 15 et 16 recâblés vers des ancres explicites de sous-sections.'
if line not in roadmap:
    roadmap = once(roadmap,
        '- [x] Explications des chapitres 15 et 16 rendues concises : chemins et syntaxe non répétés, rôles spécifiques, erreurs au format fautif/correction.',
        '- [x] Explications des chapitres 15 et 16 rendues concises : chemins et syntaxe non répétés, rôles spécifiques, erreurs au format fautif/correction.\n' + line, 'roadmap line')
roadmap_path.write_text(roadmap, encoding='utf-8')

continuity_path = Path('CONTINUITE-PROJET.md')
continuity = continuity_path.read_text(encoding='utf-8')
continuity = version(continuity, '3.17.4', '3.17.5', 'continuity version')
continuity = once(continuity, 'last-updated: "2026-07-19"', 'last-updated: "2026-07-20"', 'continuity date')
continuity = once(continuity, 'version `1.5.0`', 'version `1.7.1`', 'continuity protocol version')
continuity = once(continuity, 'Les rappels courts sont permis. Les duplications intégrales sont interdites.',
    'Les rappels courts sont permis. Les duplications intégrales sont interdites.\n\nAucune rubrique d’explication ne justifie un bloc en citant le titre de la section courante. Elle énonce directement le fait technique, le risque ou l’invariant. Les renvois internes visent la sous-section exacte et utilisent un fragment vérifié ou une ancre explicite stable.', 'continuity self-title rule')
continuity = once(continuity,
    'La règle des erreurs et corrections est **sémantique**, pas nominale. Toute section dont la fonction est d’enseigner des erreurs fréquentes, diagnostics, anti-patterns, pièges ou mauvaises pratiques doit fournir, pour chaque cas détaillé : un symptôme, un exemple fautif, une correction, un exemple corrigé et l’explication de leur différence.',
    'La règle des erreurs et corrections est **sémantique**, pas nominale. Toute section dont la fonction est d’enseigner des erreurs fréquentes, diagnostics, anti-patterns, pièges ou mauvaises pratiques doit fournir, pour chaque cas détaillé : un symptôme, un exemple fautif suivi de `Pourquoi cet exemple est fautif`, puis un exemple corrigé suivi de `Pourquoi la correction fonctionne`.', 'continuity error format')
continuity = once(continuity, '- chapitre 15 : version `1.2.0` ;', '- chapitre 15 : version `1.2.1` ;', 'continuity ch15')
continuity = once(continuity, '- chapitre 16 : version `1.2.0` ;', '- chapitre 16 : version `1.2.1` ;', 'continuity ch16')
if '### 2026-07-20 — version 3.17.5' not in continuity:
    entry = '''## 27. Journal\n\n### 2026-07-20 — version 3.17.5\n\n- suppression des auto-paraphrases du titre de section dans toutes les rubriques d’explication ;\n- correction de deux rôles factuellement incompatibles avec les requêtes familiales présentées ;\n- recâblage de 23 renvois `À relire` vers les sous-sections exactes ;\n- ajout de 21 ancres explicites et stables dans les chapitres 15 et 16 ;\n- protocole QA porté en version `1.7.1` ;\n- chapitres et audits 15 et 16 portés en version `1.2.1` ;\n- aucun PDF construit et aucun test runtime revendiqué.\n'''
    continuity = once(continuity, '## 27. Journal\n', entry, 'continuity journal')
continuity_path.write_text(continuity, encoding='utf-8')

contents = Path('contents.txt').read_text(encoding='utf-8')
for required in ('Livre-II/CHAPITRE-15-Relations-sociales.md', 'Livre-II/CHAPITRE-16-Famille-et-generations.md', 'Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md'):
    if required not in contents:
        raise RuntimeError(f'contents.txt missing {required}')
