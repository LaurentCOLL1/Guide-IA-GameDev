from pathlib import Path

source_path = Path('tools/qa/tmp_fix_ch17_closure.py')
source = source_path.read_text(encoding='utf-8')
lines = source.splitlines()

needle = "    'index chapter status',"
try:
    marker_index = lines.index(needle)
except ValueError as exc:
    raise RuntimeError('index replacement marker missing') from exc

start = marker_index
while start >= 0 and lines[start] != 'index = replace_once(':
    start -= 1
if start < 0:
    raise RuntimeError('index replacement block start missing')

end = marker_index + 1
while end < len(lines) and lines[end] != ')':
    end += 1
if end >= len(lines):
    raise RuntimeError('index replacement block end missing')

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

patched = '\n'.join(lines[:start] + replacement + lines[end + 1:]) + '\n'
exec(compile(patched, str(source_path), 'exec'), {'__name__': '__main__'})
