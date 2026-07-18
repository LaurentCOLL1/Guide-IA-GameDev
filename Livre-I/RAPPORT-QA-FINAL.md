---
title: "Rapport QA du Livre I — validation historique à six chapitres"
id: "DOC-L1-QA-FINAL"
status: "superseded"
version: "1.1.0"
book: "Livre I"
category: "quality-report"
validation-date: "2026-07-18"
superseded-date: "2026-07-18"
---

# Rapport QA du Livre I — validation historique à six chapitres

## Statut

Ce rapport est **superseded** depuis la réouverture de M2 et le passage du Livre I de six à dix chapitres.

Il reste conservé comme preuve de l’état documentaire antérieur, mais il ne peut plus être utilisé pour déclarer le Livre I terminé.

## Exécution historique

| Élément | Valeur |
|---|---|
| Workflow | `Validate Documentation` |
| Exécution | `29638120888` |
| Résultat | `success` |
| Branche de contrôle | `qa/validate-livre-i` |
| Commit contrôlé | `75316cb1b1a51b10194343dcd7bd325d953876f1` |
| Sources déclarées | 33 |
| Chapitres du Livre I | 6 |
| Identifiants uniques | 32 |
| Erreurs bloquantes | 0 |
| PDF généré | A4, 348 pages |
| Pages contrôlées visuellement | 46 |

## Motif de la réouverture

La structure à six chapitres couvrait les grands services IA, mais ne développait pas suffisamment les fondations nécessaires au public débutant annoncé par le guide.

Quatre chapitres ont donc été ajoutés :

1. Terminal, PowerShell et outils Windows ;
2. Git, GitHub et Visual Studio Code ;
3. Python et environnements virtuels ;
4. Sécurité, sauvegarde et validation de la plateforme.

Les chapitres Docker, Open WebUI, ComfyUI, LLM et audio ont été déplacés aux positions 5 à 9. Leurs identifiants stables historiques ont été conservés.

## Validation requise

Une nouvelle clôture de M2 exige :

- [ ] dix chapitres détectés dans `contents.txt` ;
- [ ] dix valeurs `chapter` cohérentes avec les chemins ;
- [ ] identifiants nouveaux et historiques sans doublon ;
- [ ] liens locaux valides après renumérotation ;
- [ ] compilation Pandoc/XeLaTeX réussie ;
- [ ] PDF inspecté techniquement ;
- [ ] contrôle visuel couvrant les quatre nouveaux chapitres ;
- [ ] nouveau rapport QA final ;
- [ ] index et roadmap remis au statut `complete` uniquement après succès.

## Réserves de publication conservées

- la licence globale du projet doit encore être définie ;
- le PDF final devra être balisé et contrôlé pour l’accessibilité ;
- les licences des modèles, poids, voix et données restent à vérifier par ressource.

## Conclusion

La validation historique à six chapitres reste valide pour le périmètre qu’elle avait contrôlé. Elle ne couvre pas la nouvelle structure du Livre I et ne clôt plus M2.