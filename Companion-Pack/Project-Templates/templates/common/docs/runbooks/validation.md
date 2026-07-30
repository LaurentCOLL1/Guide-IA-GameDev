# Runbook de validation

## Contrôles locaux

1. exécuter `python tools/validate_project.py` ;
2. importer avec Godot en headless ;
3. exécuter le bootstrap borné ;
4. exécuter `res://tests/run_tests.gd` ;
5. vérifier `git status --short`.

## Contrôles non couverts automatiquement

- qualité visuelle ;
- performance GPU ;
- export ;
- signature ;
- protections GitHub effectives ;
- permissions organisationnelles.
