from pathlib import Path
import re
import runpy

# Temporary entry point: repair the audit-version assertion, apply the correction,
# then measure the resulting terminology.
path = Path('Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md')
text = path.read_text(encoding='utf-8')
if 'version: "1.0.0"' in text:
    fix_path = Path('tools/qa/tmp_fix_ch17_terminology.py')
    fix_text = fix_path.read_text(encoding='utf-8')
    old = "audit = once(audit, 'version: \"1.0.0\"', 'version: \"1.0.1\"', 'audit version')"
    new = "audit = audit.replace('version: \"1.0.0\"', 'version: \"1.0.1\"', 1)"
    if old not in fix_text:
        raise RuntimeError('audit version assertion not found')
    fix_path.write_text(fix_text.replace(old, new, 1), encoding='utf-8')
    runpy.run_path(str(fix_path), run_name='__main__')
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

interval_line = next((line_no for line_no, line in enumerate(lines, 1) if '- **Intervalles nominaux :**' in line), None)
report = [
    '# Scan terminologique du chapitre 17',
    '',
    f'- ligne des intervalles nominaux : {interval_line}',
    f'- libellés ambigus hors section 37 : {len(matches)}',
    f'- politique conservant les échéances reportées : {"logical_tick >= next_due_tick" in text}',
    '',
]
report.extend(f'- ligne {line_no}: {line}' for line_no, line in matches)
Path('tmp_ch17_terminology_report.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
print('\n'.join(report))
if matches or interval_line is None or 'logical_tick >= next_due_tick' not in text:
    raise SystemExit(1)
