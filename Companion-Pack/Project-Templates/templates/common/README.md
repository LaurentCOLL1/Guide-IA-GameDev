# __PROJECT_NAME__

Projet Godot généré depuis le profil `__PROFILE_ID__` du Pack 2 — Project Templates.

## Identité

- identifiant : `__PROJECT_ID__`
- slug : `__PROJECT_SLUG__`
- profil : `__PROFILE_ID__`
- propriétaire déclaré : `__OWNER_HANDLE__`

## Démarrage

```powershell
godot --editor --path .
```

Test headless :

```powershell
godot --headless --rendering-method gl_compatibility --path . --quit-after 5
```

Tests GDScript :

```powershell
godot --headless --rendering-method gl_compatibility --path . --script res://tests/run_tests.gd
```

## Gouvernance

Lire `docs/governance/branch-policy.md`, `docs/governance/responsibilities.md` et `docs/adr/0001-project-profile.md`.

La présence de ces fichiers ne prouve pas que les règles GitHub sont appliquées. Les protections de branche, permissions, réviseurs et propriétaires doivent être configurés dans le dépôt cible.

## Architecture

Les fonctionnalités vivent sous `src/features/<module>/` avec les couches :

- `domain` ;
- `application` ;
- `infrastructure` ;
- `presentation` ;
- `tests`.

Le dossier `src/composition/` assemble les implémentations concrètes. Le domaine ne dépend pas de la présentation ni de l’infrastructure.
