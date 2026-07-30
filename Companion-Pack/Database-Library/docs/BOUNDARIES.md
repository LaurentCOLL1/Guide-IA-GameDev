# Frontières et anti-doublon

| Sujet | Propriétaire | Décision du Pack 5 |
|---|---|---|
| données de conception | Livre II, chapitre 7 | non stockées par réflexe dans SQLite |
| connexion et migrations SQLite | Livre II, chapitre 8 | matérialisées en Python et SQL |
| sauvegarde complète de partie | Livre II, chapitre 9 | exclue |
| recherche vectorielle | Livre II, chapitre 10 | exclue |
| cache et file de fournisseur IA | AI Library | exclus |
| repository mémoire | Code Library | non recopié |
| scripts de lots génériques | Production Toolkit futur | exclus |
| tests et benchmarks transversaux | Test & Benchmark Library futur | seuls tests propres au Pack inclus |

## Décisions permanentes

1. Une migration publiée est immuable.
2. Une base étrangère n’est jamais adoptée automatiquement.
3. Une version future n’est jamais rétrogradée automatiquement.
4. Une sauvegarde n’est acceptée qu’après restauration et validation dans le périmètre testé.
5. Les valeurs SQL utilisent des paramètres liés.
6. Une donnée dérivée ne devient pas autoritaire par sa présence en base.
7. Aucune performance ou compatibilité concurrente n’est inférée des tests fonctionnels.
