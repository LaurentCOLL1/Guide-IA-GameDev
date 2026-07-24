from pathlib import Path

continuity = Path('CONTINUITE-PROJET.md').read_text(encoding='utf-8')
if 'version: "3.48.0"' not in continuity:
    raise RuntimeError('Gouvernance chapitre 18 absente ou déjà fermée.')
print('Gouvernance chapitre 18 déjà appliquée; aucune mutation supplémentaire.')
