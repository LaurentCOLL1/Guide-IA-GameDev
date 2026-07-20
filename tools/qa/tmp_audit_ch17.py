from pathlib import Path
import re

path = Path('Livre-II/CHAPITRE-17-Agents-IA-et-comportements-autonomes.md')
text = path.read_text(encoding='utf-8')
lines = text.splitlines()

headings = []
anchors = set(re.findall(r'<a id="([^"]+)"></a>', text))
links = re.findall(r'\]\(#([^)]+)\)', text)
missing_anchors = sorted(set(links) - anchors)

for line_no, line in enumerate(lines, 1):
    if re.match(r'^#{2,6}\s+', line):
        headings.append((line_no, line.lstrip('#').strip()))

blocks = []
in_block = False
start = 0
lang = ''
for index, line in enumerate(lines):
    if line.startswith('```'):
        if not in_block:
            in_block = True
            start = index
            lang = line[3:].strip()
        else:
            end = index
            window = '\n'.join(lines[end + 1:end + 12])
            blocks.append({
                'start': start + 1,
                'end': end + 1,
                'lang': lang,
                'explained': '<!-- qa:code-explanation -->' in window and '**Explication détaillée du bloc :**' in window,
            })
            in_block = False

self_mentions = []
current = ''
for line_no, line in enumerate(lines, 1):
    match = re.match(r'^#{2,6}\s+(.+?)\s*$', line)
    if match:
        current = match.group(1)
        continue
    if current and line.lstrip().startswith('- **') and current in line:
        self_mentions.append((line_no, current, line.strip()))

risks = []
checks = {
    'codec-placeholder-encode': 'func encode(state: AgentState) -> Dictionary:\n\treturn {}',
    'codec-placeholder-decode': ') -> AgentState:\n\treturn null',
    'packed-stringname-conversion': 'PackedStringArray(action_ids)',
    'untyped-values-apply': 'return _repository.replace_all(_prepared_states.values())',
    'missing-prepare-guard': 'var _is_prepared: bool',
    'draft-reserve-text': 'Limite du brouillon',
}
for name, needle in checks.items():
    present = needle in text
    if name == 'missing-prepare-guard':
        if not present:
            risks.append(name)
    elif present:
        risks.append(name)

error_cases = len(re.findall(r'^### 37\.\d+\s+', text, flags=re.M))
faulty = text.count('**Pourquoi cet exemple est fautif :**')
corrected = text.count('**Pourquoi la correction fonctionne :**')
source_links = len(re.findall(r'^- \[Godot 4\.7', text, flags=re.M))

report = [
    '# Audit post-création du chapitre 17 — brouillon 0.9.0',
    '',
    f'- lignes : {len(lines)}',
    f'- titres : {len(headings)}',
    f'- blocs clôturés : {len(blocks)}',
    f'- blocs expliqués : {sum(1 for block in blocks if block["explained"])}',
    f'- blocs sans explication détectée : {sum(1 for block in blocks if not block["explained"])}',
    f'- cas d’erreurs : {error_cases}',
    f'- explications fautives : {faulty}',
    f'- explications corrigées : {corrected}',
    f'- sources Godot 4.7 nommées : {source_links}',
    f'- ancres explicites : {len(anchors)}',
    f'- fragments internes : {len(links)}',
    f'- fragments sans ancre : {len(missing_anchors)}',
    f'- auto-paraphrases détectées : {len(self_mentions)}',
    '',
    '## Fragments sans ancre',
]
report.extend(f'- {value}' for value in missing_anchors or ['aucun'])
report.extend(['', '## Risques techniques ciblés'])
report.extend(f'- {value}' for value in risks or ['aucun'])
report.extend(['', '## Blocs sans explication'])
report.extend(f'- lignes {block["start"]}-{block["end"]} ({block["lang"] or "text"})' for block in blocks if not block['explained'])
report.extend(['', '## Auto-paraphrases'])
report.extend(f'- ligne {line_no}: {title} :: {line}' for line_no, title, line in self_mentions or [])
report.extend(['', '## Décision de l’audit', '', 'Corrections obligatoires avant passage en `1.0.0` : compléter le codec, sécuriser la préparation de sauvegarde, corriger les conversions de collections, résoudre toutes les ancres, remplacer les ports seulement annoncés par des contrats explicites, puis relancer les contrôles documentaires.'])

Path('tmp_ch17_audit_report.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
print('\n'.join(report))
