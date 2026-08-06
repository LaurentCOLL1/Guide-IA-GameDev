# Sécurité, âge et périmètre anatomique

## Principe

L’éditeur prend en charge toutes les étapes de vie pour la silhouette, le visage, la peau, la posture et les proportions générales. Il ne doit jamais transformer la représentation d’un mineur en contenu sexuel ou explicite.

## Règles obligatoires

### Personnage de moins de 18 ans

- `adult_anatomy_profile` est forcé à `unavailable_for_minor` ;
- `privacy_garment_enabled` est forcé à `true` ;
- la liste des modules anatomiques adultes est désactivée ;
- aucun asset génital explicite ne doit être chargé, prévisualisé, exporté ou sauvegardé ;
- les miniatures et captures restent habillées ou couvertes ;
- les presets ne peuvent pas contourner ces règles.

### Personnage adulte

- les modules externes détaillés restent optionnels et masqués par défaut ;
- le mannequin de base demeure neutre ;
- les modules sont des assets séparés avec provenance, licence et version ;
- l’interface doit permettre de réactiver immédiatement le vêtement de confidentialité ;
- les exports sensibles doivent être opt-in et ne pas être produits automatiquement.

## Séparation technique

```text
CharacterDefinition
    ├── âge et morphologie générale
    ├── apparence
    └── métadonnées de module adulte

Avatar principal
    ├── corps canonique
    ├── vêtements
    └── AdultAnatomySlot
            └── module externe adulte, absent de ce dépôt
```

Le corps canonique et les sauvegardes restent utilisables sans module adulte.

## Validation minimale

Avant publication, automatiser les vérifications suivantes :

1. charger chaque preset d’âge ;
2. confirmer que tous les presets mineurs forcent le vêtement de confidentialité ;
3. tenter de sélectionner chaque module adulte sur un preset mineur ;
4. confirmer que la valeur sauvegardée reste `unavailable_for_minor` ;
5. charger une sauvegarde adulte sur un personnage dont l’âge est ensuite abaissé ;
6. confirmer le retrait immédiat du module adulte ;
7. inspecter les miniatures, captures et exports automatiques ;
8. vérifier que les assets adultes ne sont jamais préchargés dans un contexte destiné aux mineurs.

## Hors périmètre de ce prototype

- modèles génitaux explicites ;
- simulation sexuelle ;
- nudité de mineurs ;
- détails médicaux internes ;
- classification biométrique de personnes réelles ;
- reconstruction d’une personne réelle sans consentement et droits appropriés.
