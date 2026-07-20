from pathlib import Path
import re

FILES = [
    Path('Livre-II/CHAPITRE-15-Relations-sociales.md'),
    Path('Livre-II/CHAPITRE-16-Famille-et-generations.md'),
]

out = []
for path in FILES:
    lines = path.read_text(encoding='utf-8').splitlines()
    headings = []
    current = None
    for idx, line in enumerate(lines, start=1):
        m = re.match(r'^(#{2,6})\s+(.+?)\s*$', line)
        if m:
            current = (len(m.group(1)), m.group(2), idx)
            headings.append(current)
        if current and 'Pourquoi cet exemple est fautif' in line and f'« {current[1]} »' in line:
            out.append(f'{path}:{idx}:SELF_REFERENCE:{current[1]}::{line.strip()}')
        if line.startswith('> **À relire :**'):
            link = re.search(r'\[([^\]]+)\]\((#[^)]+)\)', line)
            label = link.group(1) if link else '<missing>'
            target = link.group(2) if link else '<missing>'
            out.append(f'{path}:{idx}:REREAD:{current[1] if current else "<none>"}::{label}::{target}')
    out.append(f'HEADINGS::{path}')
    out.extend(f'{path}:{line_no}:HEADING:H{level}:{title}' for level, title, line_no in headings)

Path('tmp_section_paraphrases_links_audit.txt').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('\n'.join(out))
