from __future__ import annotations

import re
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path.cwd()
MARKER = '<!-- qa:code-explanation -->'
WRAPPER = '**Explication structurée du bloc :**'
CHAPTERS = {
    17: 'Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md',
    18: 'Livre-II/CHAPITRE-18-Combat.md',
    19: 'Livre-II/CHAPITRE-19-Competences-et-pouvoirs.md',
    20: 'Livre-II/CHAPITRE-20-Inventaire-et-reputation-des-objets.md',
    21: 'Livre-II/CHAPITRE-21-Economie.md',
    22: 'Livre-II/CHAPITRE-22-Monde-vivant-et-simulation-ecologique.md',
    23: 'Livre-II/CHAPITRE-23-Politique-factions-et-justice.md',
    24: 'Livre-II/CHAPITRE-24-Construction-et-gestion-de-domaines.md',
}
NOW = datetime.now(ZoneInfo('Europe/Paris')).replace(microsecond=0).isoformat()

LABEL_MAP = {
    'rôle': 'Rôle précis du bloc',
    'responsabilité': 'Responsabilités des classes ou fonctions',
    'responsabilités': 'Responsabilités des classes ou fonctions',
    'entrées': 'Paramètres et types importants',
    'entrée': 'Paramètres et types importants',
    'entrées et sorties': 'Paramètres, sorties et types importants',
    'données importantes': 'Paramètres et types importants',
    'types et sentinelle': 'Paramètres et types importants',
    'types': 'Paramètres et types importants',
    'paramètres': 'Paramètres et types importants',
    'valeurs de retour': 'Valeur de retour ou code d’échec',
    'codes de retour': 'Valeur de retour ou code d’échec',
    'retours': 'Valeur de retour ou code d’échec',
    'traitement du résultat': 'Valeur de retour ou traitement du résultat',
    'effets de bord': 'Effets de bord',
    'invariant protégé': 'Invariants protégés',
    'invariants protégés': 'Invariants protégés',
    'validation': 'Invariants protégés',
    'préconditions': 'Invariants protégés',
    'refus contrôlé': 'Refus contrôlé',
    'ordre': 'Déroulement ou instructions importantes',
    'déroulement': 'Déroulement ou instructions importantes',
    'phase': 'Déroulement ou instructions importantes',
    'rattrapage borné': 'Déroulement ou instructions importantes',
    'résultat attendu': 'Résultat attendu',
    'conséquence': 'Résultat attendu et conséquences',
    'vérification': 'Résultat attendu et vérification',
    'limite': 'Limites et réserves',
    'limites': 'Limites et réserves',
    'frontière': 'Frontières d’autorité',
    'dépendances': 'Dépendances et ports utilisés',
    'ports': 'Dépendances et ports utilisés',
    'lien moteur': 'Lien avec le moteur',
    'ordre déterministe': 'Déterminisme et ordre',
    'budget': 'Budgets et limites',
    'temps': 'Temps logique et mesure',
    'corrélation': 'Corrélation et révisions',
    'cibles': 'Cibles et données optionnelles',
    'annulation': 'Annulation',
    'disponibilité': 'Disponibilité et limites',
    'intervalles nominaux': 'Intervalles et cadence',
    'mode dormant': 'Persistance et mode dormant',
    'report conservé': 'Déterminisme et échéances',
    'copie défensive': 'Copies et mutabilité',
    'sémantique temporelle': 'Temps logique et expiration',
}


def git_main(path: str) -> str:
    return subprocess.check_output(['git', 'show', f'origin/main:{path}'], text=True, encoding='utf-8')


def boundary(line: str, seen: bool) -> bool:
    if not seen:
        return False
    return bool(
        re.match(r'^#{1,6}\s+', line)
        or line.startswith('> **[')
        or line.startswith('<!-- qa:')
        or line.startswith('<a id=')
        or line.startswith('**Exemple fautif')
        or line.startswith('**Exemple corrigé')
        or line.startswith('**Symptôme')
    )


def explanation_end(lines: list[str], start: int) -> int:
    seen = False
    for i in range(start, len(lines)):
        if lines[i].strip():
            if boundary(lines[i], seen):
                return i
            seen = True
    return len(lines)


def extract_units(block: list[str]) -> list[str]:
    lines = list(block)
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and lines[0].strip() in {'**Explication détaillée du bloc :**', WRAPPER}:
        lines.pop(0)
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    units: list[str] = []
    current: list[str] = []
    mode = None
    for line in lines:
        if line.startswith('- '):
            if current:
                units.append('\n'.join(current).strip())
            current = [line[2:]]
            mode = 'bullet'
        elif mode == 'bullet' and (line.startswith('  ') or not line.strip()):
            current.append(line[2:] if line.startswith('  ') else '')
        else:
            if current:
                units.append('\n'.join(current).strip())
                current = []
            if line.strip():
                units.append(line.strip())
            mode = 'prose'
    if current:
        units.append('\n'.join(current).strip())
    return [u for u in units if u]


def label_for(unit: str) -> str:
    m = re.match(r'^\*\*([^*]+?)\s*:\*\*', unit)
    if m:
        key = m.group(1).strip().casefold()
        if key in LABEL_MAP:
            return LABEL_MAP[key]
        return m.group(1).strip()
    low = unit.casefold()
    if 'autorité' in low or 'propriétaire' in low:
        return 'Frontières d’autorité'
    if 'persist' in low or 'snapshot' in low or 'restaur' in low:
        return 'Persistance et restauration'
    if 'retour' in low or 'sentinelle' in low:
        return 'Valeur de retour ou code d’échec'
    if 'paramètre' in low or 'type' in low or 'champ' in low:
        return 'Paramètres et types importants'
    if 'invariant' in low or 'valide' in low or 'refus' in low:
        return 'Invariants protégés'
    if 'dépend' in low or 'port' in low:
        return 'Dépendances et ports utilisés'
    if 'résultat' in low or 'vérifi' in low:
        return 'Résultat attendu et vérification'
    if 'limite' in low or 'aucun' in low or 'ne ' in low:
        return 'Limites et réserves'
    return 'Point d’explication complémentaire'


def unique_labels(items: list[tuple[str, str]]) -> list[tuple[str, str]]:
    counts: dict[str, int] = {}
    out = []
    for label, unit in items:
        counts[label] = counts.get(label, 0) + 1
        final = label if counts[label] == 1 else f'{label} — complément {counts[label]}'
        out.append((final, unit))
    return out


def render(items: list[tuple[str, str]]) -> list[str]:
    out = ['', WRAPPER, '']
    for idx, (label, unit) in enumerate(items):
        parts = unit.splitlines()
        out.append(f'- **{label} :** {parts[0]}')
        out.extend(f'  {line}' for line in parts[1:])
        if idx != len(items) - 1:
            out.append('')
    out.append('')
    return out


def transform(original: str) -> tuple[str, int]:
    lines = original.splitlines()
    markers = [i for i, line in enumerate(lines) if line.strip() == MARKER]
    preserved = 0
    for marker in reversed(markers):
        start = marker + 1
        end = explanation_end(lines, start)
        units = extract_units(lines[start:end])
        if not units:
            raise RuntimeError(f'explication vide après ligne {marker + 1}')
        preserved += len(units)
        items = unique_labels([(label_for(unit), unit) for unit in units])
        replacement = render(items)
        lines[start:end] = replacement
        rendered = '\n'.join(replacement)
        for unit in units:
            if unit not in rendered:
                raise RuntimeError(f'unité perdue: {unit}')
    return '\n'.join(lines) + '\n', preserved


def update_time(text: str) -> str:
    text = re.sub(r'^last-verified:\s*"[^"]+"\s*$', f'last-verified: "{NOW}"', text, count=1, flags=re.M)
    text = re.sub(r'^audit-date:\s*"[^"]+"\s*$', f'audit-date: "{NOW}"', text, count=1, flags=re.M)
    return text


def main() -> None:
    counts: dict[int, int] = {}
    for chapter, path in CHAPTERS.items():
        transformed, preserved = transform(git_main(path))
        current = (ROOT / path).read_text(encoding='utf-8')
        version = re.search(r'^version:\s*"([^"]+)"', current, re.M).group(1)
        transformed = re.sub(r'^version:\s*"[^"]+"', f'version: "{version}"', transformed, count=1, flags=re.M)
        transformed = update_time(transformed)
        note = '> **Explications de code :** structurées bloc par bloc ; les informations pédagogiques antérieures sont conservées dans des rubriques explicites, complétées seulement lorsque le bloc l’exige.'
        if note not in transformed:
            m = re.search(r'^(> \*\*Audit post-création :\*\*.*)$', transformed, re.M)
            transformed = transformed[:m.end()] + '\n' + note + transformed[m.end():]
        (ROOT / path).write_text(transformed, encoding='utf-8')
        counts[chapter] = preserved

        audit_path = ROOT / f'Livre-II/QA/AUDIT-CHAPITRE-{chapter:02d}.md'
        audit = update_time(audit_path.read_text(encoding='utf-8'))
        audit = re.sub(r'- (?:unités|segments) d’explication antérieur(?:es|s) conservé(?:es|s) : \*\*\d+\*\* ;', f'- unités d’explication antérieures conservées : **{preserved}** ;', audit)
        audit_path.write_text(audit, encoding='utf-8')

        proof_path = ROOT / f'Livre-II/QA/VALIDATION-FINALE-CHAPITRE-{chapter:02d}.yaml'
        proof = proof_path.read_text(encoding='utf-8')
        proof = re.sub(r'^(\s+prior-explanation-units-preserved:)\s*\d+', rf'\1 {preserved}', proof, flags=re.M)
        proof_path.write_text(proof, encoding='utf-8')

    for path in [ROOT / 'Livre-II/CHAPITRE-25-Narration-quetes-codex-et-connaissances.md', ROOT / 'Livre-II/CHAPITRE-26-Outils-d-edition-internes-et-pipelines-de-contenu.md']:
        text = path.read_text(encoding='utf-8').replace('et montre leur traitement complet ou leur squelette contractuel.', 'et montre son traitement complet ou son squelette contractuel.')
        path.write_text(text, encoding='utf-8')

    report_path = ROOT / 'Livre-II/QA/AUDIT-RESTRUCTURATION-EXPLICATIONS-CH17-CH26.md'
    report = update_time(report_path.read_text(encoding='utf-8'))
    for chapter, count in counts.items():
        report = re.sub(rf'(^\| {chapter} \| `[^`]+` \| \d+ \| \d+ \| )\d+( \| 0 \| \d+ \|$)', rf'\g<1>{count}\2', report, flags=re.M)
    total_17_24 = sum(counts.values())
    m25 = re.search(r'^\| 25 \| `[^`]+` \| \d+ \| \d+ \| (\d+)', report, re.M)
    m26 = re.search(r'^\| 26 \| `[^`]+` \| \d+ \| \d+ \| (\d+)', report, re.M)
    total = total_17_24 + int(m25.group(1)) + int(m26.group(1))
    report = re.sub(r'Totaux : \*\*\d+\*\* segments antérieurs conservés', f'Totaux : **{total}** segments antérieurs conservés', report)
    report_path.write_text(report, encoding='utf-8')

    continuity = ROOT / 'CONTINUITE-PROJET.md'
    text = continuity.read_text(encoding='utf-8')
    text = re.sub(r'^last-updated:\s*"[^"]+"', f'last-updated: "{NOW}"', text, count=1, flags=re.M)
    entry = f'''### {NOW} — reclassement fidèle des explications historiques\n\n- chapitres 17 à 24 reconstruits depuis leurs explications présentes sur `main` ;\n- libellés historiques utilisés comme autorité de classement ;\n- **{total_17_24}** unités conservées mot pour mot et **0** perdue ;\n- aucune modification des exemples de code ;\n- aucun test runtime revendiqué et aucun PDF construit.\n\n'''
    anchor = text.find('## 27. Journal')
    line_end = text.find('\n', anchor)
    text = text[:line_end + 1] + '\n' + entry + text[line_end + 1:]
    continuity.write_text(text, encoding='utf-8')

    Path(__file__).unlink()
    print('Unités conservées chapitres 17 à 24:', total_17_24)

if __name__ == '__main__':
    main()
