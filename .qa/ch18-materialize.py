from pathlib import Path

required = [
    Path('Livre-III/CHAPITRE-18-LOD-imposteurs-et-optimisation-geometrique.md'),
    Path('Livre-III/QA/AUDIT-CHAPITRE-18.md'),
    Path('Livre-III/QA/VALIDATION-FINALE-CHAPITRE-18.yaml'),
]
missing = [str(path) for path in required if not path.is_file()]
if missing:
    raise RuntimeError(f'Lot permanent chapitre 18 incomplet: {missing}')
print('Lot permanent chapitre 18 déjà matérialisé; reprise de clôture autorisée.')
