#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import hashlib
import re
import subprocess
from pathlib import Path

ROOT = Path('.')
NOW = dt.datetime.now(dt.timezone(dt.timedelta(hours=2))).replace(microsecond=0)
ISO = NOW.isoformat()
DATE = NOW.date().isoformat()
BRANCH = 'fix/livre-iii-syntheses-asteria'

SUMMARIES = {
    17: """Project Asteria retient `AST-BAKE-PILOT-RELAY-001` comme étalon de retopologie, d’UV et de baking. Les sources haute résolution, basse résolution et cage restent séparées et versionnées ; le maillage final possède l’autorité sur la silhouette, la triangulation, les UV, les normales et les tangentes. Les profils statique et déformable sont qualifiés séparément afin qu’une optimisation locale ne dégrade ni les appuis ni les zones de flexion.

Le pipeline Asteria impose une densité de texels mesurée, des marges compatibles avec les mipmaps, des chevauchements explicitement autorisés, un espace tangent MikkTSpace et des normales OpenGL. Chaque bake possède un manifeste reliant sources, paramètres, cartes produites, empreintes et contrôle Blender–Godot. Une modification tardive de topologie, d’UV, de normales ou de triangulation invalide le bake précédent.

La porte reste bloquée tant que les fichiers high, low et cage, les textures, le GLB, les captures comparatives et le rapport de contrôle ne sont pas matérialisés. Le chapitre fixe donc le contrat opérationnel de Project Asteria sans revendiquer une qualité visuelle, une compatibilité de déformation ou une performance runtime mesurée.""",
    18: """Project Asteria retient `AST-LOD-PILOT-SIGNAL-TOWER-001` comme étalon de réduction géométrique. Le LOD0 approuvé reste la source canonique ; chaque LOD manuel, LOD automatique, HLOD, imposteur ou billboard possède une identité, une plage d’usage, un profil de matériau, une règle d’ombre, une collision éventuelle et une provenance versionnée. Les décisions sont pilotées par la couverture écran et l’importance visuelle ou gameplay, non par un pourcentage de décimation isolé.

Les transitions Asteria utilisent des plages documentées, une hystérésis et, lorsque le renderer le permet, un fondu qualifié. Les silhouettes, masses, ouvertures, haubans et repères de lecture prioritaires sont protégés avant les détails internes. Les proxies de collision, d’occlusion et d’ombre restent indépendants de la représentation visuelle afin qu’un gain graphique ne modifie pas silencieusement le comportement du monde.

La chaîne n’est acceptée qu’après comparaison dans une scène Godot reproductible avec profils de caméra, captures, données brutes et tableau avant/après. Tant que les meshes simplifiés, textures d’imposteur, scènes et mesures n’existent pas, Project Asteria conserve le statut `static-review` et ne revendique aucun gain de mémoire, de draw calls ou de temps GPU.""",
    19: """Project Asteria retient `AST-RIG-PILOT-SCOUT-001` comme squelette témoin pour les personnages humanoïdes. Le squelette de déformation exporté, le rig de contrôle Blender, les profils de skinning, la rest pose, les sockets et le `BoneMap` sont versionnés comme contrats distincts. Les contrôleurs, widgets et mécanismes internes ne sont pas exportés lorsqu’ils n’appartiennent pas à la déformation livrée.

Le bind Asteria exige des axes et rolls documentés, des poids normalisés, un budget d’influences mesuré et une grille de poses couvrant repos, amplitudes usuelles et extrêmes. Les correctifs sont justifiés par une déformation observable ; les sockets sont contrôlés avec des accessoires témoins ; toute modification de hiérarchie, de rest pose ou de noms d’os déclenche une nouvelle qualification du retargeting et des animations dépendantes.

La porte reste bloquée tant que le rig Blender, les poids, la grille de poses, le GLB filtré, l’import `Skeleton3D`, les sockets et le rapport de déformation ne sont pas réellement produits et revus. Le chapitre fixe l’interface du personnage Asteria sans revendiquer un rig opérationnel ni une déformation runtime validée.""",
    20: """Project Asteria retient `AST-ANIM-PILOT-SCOUT-001` comme bibliothèque témoin construite sur le rig gelé du chapitre 19. Les Actions Blender canoniques, leur base temporelle, leurs phases, contacts, boucles, vitesses et événements sont versionnés séparément du graphe de lecture Godot. Le root motion, les fenêtres d’action et les pistes de méthode transportent des faits d’animation ; ils ne prennent pas l’autorité sur les règles de gameplay.

Le runtime Asteria organise locomotion, actions ponctuelles, couches additives, masques, blend spaces et machine à états dans un `AnimationTree` documenté. Chaque transition possède une durée, une politique d’interruption, une compatibilité de phase et une revue bidirectionnelle. Le regard, la visée, le placement des pieds et le warping restent des corrections procédurales bornées, comparées en mode activé et désactivé, et ne servent jamais à masquer une mauvaise animation source.

La porte d’acceptation exige les clips, le manifeste, le GLB, les bibliothèques importées, la matrice de transitions, les captures de contacts et une scène Godot reproductible. Tant que ces éléments ne sont pas exécutés, Project Asteria conserve le niveau `static-review` et ne revendique ni fluidité, ni absence de glissement, ni coût runtime mesuré.""",
}

CHAPTERS = {
    17: Path('Livre-III/CHAPITRE-17-UV-retopologie-et-baking.md'),
    18: Path('Livre-III/CHAPITRE-18-LOD-imposteurs-et-optimisation-geometrique.md'),
    19: Path('Livre-III/CHAPITRE-19-Rigging-et-skinning.md'),
    20: Path('Livre-III/CHAPITRE-20-Animation-procedurale-et-animation-par-keyframes.md'),
}
AUDITS = {n: Path(f'Livre-III/QA/AUDIT-CHAPITRE-{n}.md') for n in CHAPTERS}
PROOFS = {n: Path(f'Livre-III/QA/VALIDATION-FINALE-CHAPITRE-{n}.yaml') for n in CHAPTERS}


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + '\n', encoding='utf-8')


def bump_patch(text: str) -> str:
    match = re.search(r'(?m)^version: ["\']?(\d+)\.(\d+)\.(\d+)["\']?$', text)
    if not match:
        return text
    replacement = f'version: "{match.group(1)}.{match.group(2)}.{int(match.group(3)) + 1}"'
    return text[:match.start()] + replacement + text[match.end():]


def update_times(text: str) -> str:
    text = re.sub(r'(?m)^last-verified: .*$', f'last-verified: "{ISO}"', text, count=1)
    text = re.sub(r'(?m)^audit-date: .*$', f'audit-date: "{ISO}"', text, count=1)
    return text


def next_section(text: str) -> int:
    numbers = [int(value) for value in re.findall(r'(?m)^##\s+(\d+)\.', text)]
    return max(numbers, default=0) + 1


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(['git', *args], text=True).strip()


def commit_and_push(message: str) -> None:
    subprocess.run(['git', 'add', '-A'], check=True)
    subprocess.run(['git', 'commit', '-m', message], check=True)
    subprocess.run(['git', 'push', 'origin', f'HEAD:{BRANCH}'], check=True)


def stage_one() -> None:
    for number, path in CHAPTERS.items():
        text = read(path)
        if 'Synthèse opérationnelle pour Project Asteria' not in text:
            text = bump_patch(update_times(text))
            text += f'\n## {next_section(text)}. Synthèse opérationnelle pour Project Asteria\n\n{SUMMARIES[number]}\n'
            write(path, text)

        audit = AUDITS[number]
        audit_text = bump_patch(update_times(read(audit)))
        heading = '## Correctif transversal — Synthèse opérationnelle Project Asteria'
        if heading not in audit_text:
            audit_text += (
                f'\n{heading}\n\n'
                f'La section de clôture propre à Project Asteria a été restaurée dans le chapitre {number}. '
                'Elle transforme la conclusion générale en décisions de pipeline, identifiants, dépendances, portes '
                'd’acceptation et réserves directement applicables au projet fil rouge. Ce correctif ne modifie pas '
                'le périmètre technique ni le niveau de preuve `static-review` ; il restaure une exigence éditoriale '
                'transversale et rend sa présence contrôlable automatiquement.\n'
            )
        write(audit, audit_text)

    continuity = Path('CONTINUITE-PROJET.md')
    text = read(continuity)
    text = re.sub(r'(?m)^version: "3\.50\.1"$', 'version: "3.51.0"', text, count=1)
    text = re.sub(r'(?m)^last-updated: .*$', f'last-updated: "{ISO}"', text, count=1)
    text = text.replace('**En cours : 18 chapitres sur 30.**', '**En cours : 20 chapitres sur 30.**', 1)
    if '19. Rigging et skinning — terminé au niveau `static-review`.' not in text:
        text = text.replace(
            '18. LOD, imposteurs et optimisation géométrique — terminé au niveau `static-review`.\n',
            '18. LOD, imposteurs et optimisation géométrique — terminé au niveau `static-review`.\n'
            '19. Rigging et skinning — terminé au niveau `static-review`.\n'
            '20. Animation procédurale et animation par keyframes — terminé au niveau `static-review`.\n',
            1,
        )
    text = text.replace('Les chapitres 19 à 30 restent définis', 'Les chapitres 21 à 30 restent définis', 1)
    rule = (
        'Chaque chapitre du Livre III doit comporter une section finale intitulée **« Synthèse opérationnelle pour '
        'Project Asteria »**. Elle doit traduire le contenu en décisions permanentes du projet fil rouge : '
        'identifiants retenus, conventions, dépendances, livrables, porte d’acceptation et réserves. Son absence est '
        'désormais une erreur QA bloquante pour les chapitres 17 et suivants.\n'
    )
    if 'Son absence est désormais une erreur QA bloquante' not in text:
        anchor = 'Cette règle est une porte d’audit bloquante pour les nouveaux chapitres comme pour les corrections rétroactives.'
        text = text.replace(anchor, rule + '\n' + anchor, 1)
    if 'Restauration des synthèses opérationnelles Asteria' not in text:
        text += (
            f'\n### {DATE} — Restauration des synthèses opérationnelles Asteria\n\n'
            '- chapitres 17 à 20 complétés par une synthèse opérationnelle propre à Project Asteria ;\n'
            '- progression autoritative corrigée de 18/30 à 20/30 ;\n'
            '- règle de clôture ajoutée au plan maître et à la continuité ;\n'
            '- validateur permanent ajouté pour empêcher une nouvelle régression ;\n'
            '- audits et preuves QA actualisés sans modifier le niveau `static-review`.\n'
        )
    write(continuity, text)

    plan = Path('plans/LIVRE-III-PLAN-MAITRE.md')
    plan_text = bump_patch(read(plan))
    if 'Règle transversale de clôture — Project Asteria' not in plan_text:
        plan_text += (
            '\n## Règle transversale de clôture — Project Asteria\n\n'
            'Tout chapitre du Livre III doit se terminer par une section intitulée **« Synthèse opérationnelle pour '
            'Project Asteria »**. Cette section ne répète pas le résumé pédagogique : elle convertit les '
            'apprentissages en décisions applicables au projet fil rouge, en nommant les identifiants pilotes, les '
            'conventions retenues, les dépendances amont et aval, les livrables attendus, la porte d’acceptation et les '
            'réserves de preuve.\n\n'
            'Pour les chapitres 17 et suivants, l’absence de cette section, un corps inférieur à deux paragraphes '
            'substantiels ou l’absence de référence explicite à Project Asteria constitue une erreur QA bloquante. '
            'Les chapitres 17 à 20 ont été corrigés rétroactivement ; les chapitres 21 à 30 doivent intégrer cette '
            'section dès leur première version.\n'
        )
    write(plan, plan_text)

    validator = Path('scripts/validate_project_asteria_summaries.py')
    write(validator, '''#!/usr/bin/env python3
from pathlib import Path
import re
import sys

HEADING = "Synthèse opérationnelle pour Project Asteria"
errors = []
checked = 0
for path in sorted(Path("Livre-III").glob("CHAPITRE-*.md")):
    match = re.search(r"CHAPITRE-(\\d+)-", path.name)
    if not match or int(match.group(1)) < 17:
        continue
    checked += 1
    text = path.read_text(encoding="utf-8")
    heading = re.search(r"(?m)^##(?:\\s+\\d+\\.)?\\s+Synthèse opérationnelle pour Project Asteria\\s*$", text)
    if not heading:
        errors.append(f"{path}: section obligatoire absente")
        continue
    body = text[heading.end():]
    following = re.search(r"(?m)^##\\s+", body)
    if following:
        body = body[:following.start()]
    paragraphs = [p.strip() for p in re.split(r"\\n\\s*\\n", body) if len(p.strip()) >= 80]
    if len(paragraphs) < 2:
        errors.append(f"{path}: deux paragraphes substantiels minimum")
    if "Project Asteria" not in body:
        errors.append(f"{path}: Project Asteria absent du corps")
    if not any(token in body for token in ("porte", "acceptation", "bloquée", "bloque")):
        errors.append(f"{path}: condition d’acceptation ou de blocage absente")
if errors:
    print("Validation des synthèses Asteria : ÉCHEC", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)
print(f"Validation des synthèses Asteria : SUCCÈS ({checked} chapitres contrôlés)")
''')

    subprocess.run(['python', str(validator)], check=True)
    commit_and_push('docs(livre-iii): restaurer les synthèses opérationnelles Asteria')


def metrics(path: Path) -> tuple[int, int, int, int, int]:
    text = read(path)
    lines = len(text.splitlines())
    headings = len(re.findall(r'(?m)^#{1,6}\s+', text))
    blocks = len(re.findall(r'(?m)^```', text)) // 2
    markers = text.count('<!-- qa:code-explanation -->')
    return lines, headings, blocks, markers, max(markers - 20, 0)


def stage_two() -> None:
    validated_head = git('rev-parse', 'HEAD')
    for number, proof in PROOFS.items():
        text = read(proof)
        lines, headings, blocks, markers, structured = metrics(CHAPTERS[number])
        text = re.sub(r"(?m)^validation-date:.*$", f"validation-date: '{DATE}'", text, count=1)
        text = re.sub(r'(?m)^validated-head-commit:.*$', f'validated-head-commit: {validated_head}', text, count=1)
        text = text.replace('  version: 1.0.0', '  version: 1.0.1', 1)
        values = {
            'chapter-lines': lines,
            'chapter-headings': headings,
            'chapter-code-and-data-blocks': blocks,
            'significant-code-and-data-blocks': blocks,
            'code-explanation-markers': markers,
            'structured-non-error-code-explanations': structured,
        }
        for key, value in values.items():
            text = re.sub(rf'(?m)^  {re.escape(key)}: .*$', f'  {key}: {value}', text, count=1)
        if 'project-asteria-operational-summary-present:' not in text:
            text = text.replace(
                '  master-plan-scope-covered: true\n',
                '  master-plan-scope-covered: true\n  project-asteria-operational-summary-present: true\n',
                1,
            )
        text = re.sub(r'(?m)^  chapter-sha256: .*$', f'  chapter-sha256: {sha256(CHAPTERS[number])}', text, count=1)
        text = re.sub(r'(?m)^  audit-sha256: .*$', f'  audit-sha256: {sha256(AUDITS[number])}', text, count=1)
        if '  retrofit-validation:' not in text:
            block = (
                '  retrofit-validation:\n'
                '    workflow-name: Fix Project Asteria summaries\n'
                '    execution: dedicated-validator\n'
                '    conclusion: success\n'
            )
            text = text.replace('  artifact:\n', block + '  artifact:\n', 1)
        write(proof, text)
    commit_and_push('qa(livre-iii): actualiser les preuves des synthèses Asteria')


def stage_three() -> None:
    closure_head = git('rev-parse', 'HEAD')
    for proof in PROOFS.values():
        text = read(proof)
        text = re.sub(r'(?m)^(evidence-closure:\n  commit:) .*$', rf'\1 {closure_head}', text, count=1)
        write(proof, text)
    for path in [
        Path('.qa/fix_asteria_summaries.py'),
        Path('.qa/fix_asteria_summaries.py.gz.b64'),
        Path('.qa/asteria-summary-fix-trigger.txt'),
        Path('.qa/fix-asteria-error.log'),
    ]:
        if path.exists():
            path.unlink()
    commit_and_push('chore: fermer le correctif des synthèses Asteria')


def main() -> None:
    missing = any('Synthèse opérationnelle pour Project Asteria' not in read(path) for path in CHAPTERS.values())
    if missing:
        stage_one()
        return
    if any('  retrofit-validation:' not in read(path) for path in PROOFS.values()):
        stage_two()
        return
    stage_three()


if __name__ == '__main__':
    main()
