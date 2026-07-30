from __future__ import annotations
import argparse, ast, json, re, sys
from pathlib import Path

FORBIDDEN_DIRS={'.godot','__pycache__','.venv','venv','node_modules'}
FORBIDDEN_SUFFIXES={'.exe','.dll','.so','.dylib','.bin','.zip','.7z','.tar','.gz','.pck'}
SECRET_PATTERNS=[r'BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY', r'ghp_[A-Za-z0-9]{20,}', r'sk-[A-Za-z0-9]{20,}']

def load(path: Path): return json.loads(path.read_text(encoding='utf-8'))

def python_symbols(path: Path) -> set[str]:
    tree=ast.parse(path.read_text(encoding='utf-8'), filename=str(path))
    return {node.name for node in tree.body if isinstance(node,(ast.ClassDef,ast.FunctionDef,ast.AsyncFunctionDef)) and not node.name.startswith('_')}

def gdscript_symbols(path: Path) -> set[str]:
    text=path.read_text(encoding='utf-8')
    symbols=set(re.findall(r'^class_name\s+([A-Za-z_][A-Za-z0-9_]*)', text, re.MULTILINE))
    symbols.update(re.findall(r'^static func\s+([A-Za-z_][A-Za-z0-9_]*)', text, re.MULTILINE))
    return symbols

def main() -> int:
    parser=argparse.ArgumentParser(); parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1]); parser.add_argument('--report', type=Path)
    args=parser.parse_args(); root=args.root.resolve(); errors=[]; warnings=[]
    required=['README.md','VERSION','manifest.json','catalog.json','duplicate-decisions.json','docs/API.md','docs/DUPLICATE-POLICY.md','python/src/asteria_code/__init__.py','godot-example/project.godot','godot-example/tests/run_tests.gd']
    for rel in required:
        if not (root/rel).is_file(): errors.append(f'missing:{rel}')
    version=(root/'VERSION').read_text(encoding='utf-8').strip()
    manifest=load(root/'manifest.json'); catalog=load(root/'catalog.json'); decisions=load(root/'duplicate-decisions.json')
    if manifest.get('version') != version: errors.append('manifest-version-mismatch')
    if catalog.get('pack_version') != version: errors.append('catalog-version-mismatch')
    components=catalog.get('components',[]); ids=set(); sources=set(); symbols=set(); concepts_by_language=set(); concept_languages={}
    api=(root/'docs/API.md').read_text(encoding='utf-8')
    reserved=set(decisions.get('reserved_external_concepts',{})); allowed=set(decisions.get('allowed_cross_language_ports',[]))
    for component in components:
        cid=component.get('component_id'); concept=component.get('concept_id'); language=component.get('language'); source=component.get('source')
        if cid in ids: errors.append(f'duplicate-component-id:{cid}')
        ids.add(cid)
        if source in sources: errors.append(f'duplicate-source:{source}')
        sources.add(source)
        if concept in reserved: errors.append(f'reserved-concept:{concept}')
        key=(language,concept)
        if key in concepts_by_language: errors.append(f'duplicate-concept-in-language:{language}:{concept}')
        concepts_by_language.add(key); concept_languages.setdefault(concept,set()).add(language)
        path=root/source
        if not path.is_file(): errors.append(f'missing-component-source:{source}'); continue
        available=python_symbols(path) if language=='python' else gdscript_symbols(path)
        for symbol in component.get('public_symbols',[]):
            skey=(language,symbol)
            if skey in symbols: errors.append(f'duplicate-public-symbol:{language}:{symbol}')
            symbols.add(skey)
            if symbol not in available: errors.append(f'undetected-public-symbol:{language}:{symbol}:{source}')
            if f'`{symbol}`' not in api: errors.append(f'undocumented-public-symbol:{symbol}')
    for concept,languages in concept_languages.items():
        if len(languages)>1 and concept not in allowed: errors.append(f'undeclared-cross-language-port:{concept}')
        if len(languages)>2: errors.append(f'too-many-language-ports:{concept}')
    source_files=[]
    for path in sorted(root.rglob('*')):
        rel=path.relative_to(root)
        if any(part in FORBIDDEN_DIRS for part in rel.parts): errors.append(f'forbidden-directory:{rel}'); continue
        if not path.is_file(): continue
        if path.suffix.lower() in FORBIDDEN_SUFFIXES: errors.append(f'forbidden-binary:{rel}')
        source_files.append(str(rel))
        try: text=path.read_text(encoding='utf-8')
        except UnicodeDecodeError: errors.append(f'non-utf8:{rel}'); continue
        for pattern in SECRET_PATTERNS:
            if re.search(pattern,text): errors.append(f'possible-secret:{rel}')
    report={'status':'success' if not errors else 'failure','pack_version':version,'source_files':len(source_files),'components':len(components),'public_symbols':len(symbols),'concepts':len(concept_languages),'errors':errors,'warnings':warnings}
    if args.report:
        args.report.parent.mkdir(parents=True,exist_ok=True); args.report.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False))
    if errors: return 1
    print(f'CODE_LIBRARY_STATIC: PASS ({len(source_files)} files, {len(components)} components)')
    return 0

if __name__=='__main__': raise SystemExit(main())
