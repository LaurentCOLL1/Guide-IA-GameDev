from pathlib import Path
import re

path = Path('Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md')
text = path.read_text(encoding='utf-8')
lines = text.splitlines()

inside_section_37 = False
matches = []
for line_no, line in enumerate(lines, 1):
    if line.startswith('## 37.'):
        inside_section_37 = True
    elif inside_section_37 and re.match(r'^##\s+38\.', line):
        inside_section_37 = False
    if not inside_section_37 and re.match(r'^- \*\*(Erreur|Erreurs|Erreur attendue|Erreur fréquente|Erreurs et retours|Retours et erreurs)\s*:', line):
        matches.append((line_no, line.strip()))

interval_line = next((line_no for line_no, line in enumerate(lines, 1) if '- **Intervalles :**' in line), None)

report = [
    '# Scan terminologique du chapitre 17',
    '',
    f'- ligne des intervalles : {interval_line}',
    f'- libellés ambigus hors section 37 : {len(matches)}',
    '',
]
report.extend(f'- ligne {line_no}: {line}' for line_no, line in matches)
Path('tmp_ch17_terminology_report.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
print('\n'.join(report))
