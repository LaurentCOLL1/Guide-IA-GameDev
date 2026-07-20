from pathlib import Path

source_path = Path('tools/qa/tmp_fix_ch17_closure.py')
source = source_path.read_text(encoding='utf-8')
lines = source.splitlines()

matches = [index for index, line in enumerate(lines) if "'index chapter status'" in line]
if len(matches) != 1:
    raise RuntimeError(f'index replacement line: expected one occurrence, found {len(matches)}')
line_index = matches[0]

replacement = [
    "index, replacements = re.subn(",
    "    r'^17\\. \\[Agents IA et comportements autonomes\\]\\(CHAPITRE-17-Agents-IA-et-comportements-autonomes\\.md\\).+$',",
    "    '17. [Agents IA et comportements autonomes](CHAPITRE-17-Agents-IA-et-comportements-autonomes.md) — **rédigé, repéré, expliqué bloc par bloc, terminologie des retours clarifiée, métadonnées d’audit horodatées, clôturé par les décisions Project Asteria et audité au niveau static-review**',",
    "    index,",
    "    count=1,",
    "    flags=re.M,",
    ")",
    "if replacements != 1:",
    "    raise RuntimeError(f'index chapter status: expected one line, found {replacements}')",
]

patched = '\n'.join(lines[:line_index] + replacement + lines[line_index + 1:]) + '\n'
exec(compile(patched, str(source_path), 'exec'), {'__name__': '__main__'})
