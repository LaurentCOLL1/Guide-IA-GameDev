---
title: "Audit post-création — Livre IV, chapitre 20"
id: "DOC-L4-QA-AUDIT-CH20"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre IV"
chapter: 20
chapter-id: "DOC-L4-CH20"
chapter-version: "1.0.0"
last-verified: "2026-07-27T19:11:44+02:00"
audit-status: "complete"
audit-date: "2026-07-27T19:11:44+02:00"
audit-level: "static-review"
protocol: "Livre-II/QA/PROTOCOLE-AUDIT-POST-CREATION.md"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Audit du chapitre 20 — Correctifs, mises à jour et retour arrière

## 1. Décision

Décision : **accepté avec réserves runtime, plateformes, données, sécurité, support, communication et PDF de fin de Livre**.

Le chapitre satisfait le plan maître au niveau documentaire. Il définit les canaux interne, bêta et stable, les identités de versions, les packages complets et différentiels, les migrations, l’intégrité, la reprise, les déploiements progressifs, l’interruption, le rollback, le roll-forward et les communications associées sans revendiquer d’opération réelle.

## 2. Périmètre contrôlé

- frontière avec le chapitre 14 pour CI/CD et promotion d’artefacts ;
- frontière avec le chapitre 15 pour sauvegardes indépendantes et restauration ;
- frontière avec le chapitre 16 pour export, package et manifestes fermés ;
- frontière avec le chapitre 17 pour publication initiale et portails ;
- frontière avec le chapitre 19 pour chaînes localisées et formats culturels ;
- frontière avec le chapitre 21 pour compatibilité des mods ;
- frontière avec le chapitre 22 pour archivage de long terme ;
- séparation produit, build, contenu, sauvegarde et protocole ;
- canaux, promotion du même candidat et versions sources supportées ;
- packages complets, patches différentiels, staging et activation ;
- intégrité, préflight, reprise et génération précédente ;
- migrations versionnées, copies pré-migration et réversibilité ;
- compatibilité client-serveur, contenu, accessibilité et localisation ;
- déploiement progressif, observation, interruption et portes d’arrêt ;
- rollback binaire, restauration de données, roll-forward et hotfix ;
- notes de version, messages d’incident, support et minimisation ;
- modèles Steam, itch.io, Google Play, Apple et launcher auto-hébergé ;
- tests depuis plusieurs versions, injection de fautes et exercice de rollback ;
- procédures Solo/Studio et dix diagnostics complets.

## 3. Contrôle du plan maître

Les cinq objectifs sont couverts : canaux stable, bêta et interne ; patches compatibles ; migrations de données ; intégrité et reprise ; rollback et communication. Les cinq livrables sont représentés par la stratégie de version, les manifestes de patch, le registre de migrations, les procédures de rollback et les notes de version.

La validation future depuis plusieurs versions antérieures et par retour arrière contrôlé est préparée sans être présentée comme exécutée.

## 4. Contrôle pédagogique

- les termes fondamentaux sont définis avant usage ;
- l’invariant « interruption ne signifie pas rétrogradation » est répété dans les sections décisionnelles ;
- les exemples GDScript expliquent classes, paramètres, retours et limites ;
- les scripts PowerShell, Batch, Bash et Python décrivent entrées, échecs et résultats ;
- les formats YAML, JSON, Markdown et texte expliquent leurs champs ;
- chaque fence possède un repère immédiatement avant et un marqueur d’explication après ;
- les dix contextes d’utilisation apparaissent dans le corps ;
- les dix diagnostics comportent symptôme, exemple fautif, justification, correction et justification ;
- les valeurs de rollout, seuils et durées restent candidates lorsque non qualifiées ;
- les limites de preuve sont visibles dans l’ouverture, les critères et la synthèse.

## 5. Contrôle technique

- `FileAccess.get_sha256()` est utilisé comme vérification d’intégrité et non comme signature ;
- les patches différentiels exigent une base identifiée et une empreinte cible ;
- le staging et la génération active sont séparés ;
- les retries sont bornés et réservés aux erreurs transitoires ;
- les sauvegardes portent un schéma indépendant de la version produit ;
- les migrations publiées sont immuables ;
- les retours binaires sont bloqués lorsque le schéma courant est incompatible ;
- la restauration de données expose la perte potentielle et exige une décision distincte ;
- les plateformes gérées sont décrites comme modèles à revérifier dans leurs portails ;
- la télémétrie ne déclenche pas directement un rollback ou une suppression.

## 6. Métriques statiques

| Mesure | Valeur |
|---|---:|
| Lignes | 1857 |
| Titres | 68 |
| Blocs de code ou données | 64 |
| Blocs significatifs | 43 |
| Marqueurs d’explication | 64 |
| Explications structurées hors diagnostics | 44 |
| Cas fautifs expliqués | 10 |
| Corrections expliquées | 10 |
| Titres dupliqués | 0 |
| Blocs significatifs dupliqués | 0 |
| Paragraphes longs dupliqués | 0 |

## 7. Contrôle des références

- documentation stable de Godot pour `FileAccess`, `DirAccess`, entrées/sorties et politique de versions ;
- documentation Steamworks pour branches et activation d’un build ;
- documentation officielle itch.io pour canaux et patches `butler` ;
- aide Google Play Console pour tracks et déploiements par étapes ;
- aide Apple Developer pour publication progressive d’une mise à jour ;
- liens Markdown nommés, sans URL brute dans le corps explicatif ;
- comportements de portails qualifiés comme volatils et à vérifier.

## 8. Contrôle des doublons et frontières

Aucun titre dupliqué, aucun bloc significatif dupliqué et aucun paragraphe long dupliqué n’est détecté par le contrôle local. Le chapitre ne recrée ni le packaging, ni les sauvegardes indépendantes, ni la publication initiale, ni la localisation, ni l’archivage patrimonial.

## 9. Contrôle des revendications

- aucun package complet ou différentiel n’est matérialisé ;
- aucun canal interne, bêta ou stable n’est configuré ;
- aucune sauvegarde n’est copiée ou migrée ;
- aucun test depuis une version antérieure n’est exécuté ;
- aucun déploiement progressif n’est lancé, interrompu ou repris ;
- aucun build n’est activé, rétrogradé ou corrigé ;
- aucun hotfix, rollback, roll-forward ou restauration n’est exécuté ;
- aucun compte, credential, portail ou launcher réel n’est configuré ;
- aucune métrique, télémétrie, communication publique ou opération support n’est produite ;
- aucun PDF du Livre IV n’est produit.

## 10. Réserves

- les versions sources réellement supportées doivent être qualifiées ;
- les packages, deltas et manifestes doivent être matérialisés à partir des artefacts du chapitre 16 ;
- les migrations doivent être exécutées sur des fixtures et copies représentatives ;
- les stratégies de copie pré-migration et de restauration doivent être reliées au chapitre 15 ;
- les plateformes et portails doivent être vérifiés avec les comptes autorisés ;
- les règles de progression, seuils et fenêtres doivent être mesurées ou approuvées ;
- les builds précédents doivent être retenus, vérifiés et compatibles ;
- le rollback doit être exercé avec des schémas réversibles et irréversibles ;
- les messages publics et procédures support doivent être revus ;
- la sécurité du launcher ou de l’updater doit être évaluée si une solution propriétaire est retenue ;
- la licence globale de la collection reste indéfinie ;
- le balisage final d’accessibilité du PDF de collection reste ouvert.

## 11. Preuves d’intégrité

- empreinte SHA-256 du chapitre : `f75c45f6b456abd7aeb0d3373e6d0d8b474e6f1204ea6d1741f459481f74b8e0` ;
- empreinte SHA-256 de l’audit : calculée après fermeture de ce rapport et enregistrée dans la preuve YAML ;
- validation permanente légère : en attente du commit final de la branche ;
- niveau d’audit : `static-review`.

## 12. Conclusion

Le chapitre 20 est accepté au niveau documentaire avec zéro erreur bloquante dans les contrôles locaux. La seule alerte globale attendue reste la licence de collection non définie. Toutes les preuves de patch, migration, plateforme, déploiement, rollback, support, communication et runtime demeurent réservées.
