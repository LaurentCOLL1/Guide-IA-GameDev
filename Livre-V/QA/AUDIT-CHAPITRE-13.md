---
title: "Audit — Livre V, Fiche 13 : Structures JSON et formats d’échange"
id: "DOC-L5-QA-AUDIT-CH13"
status: "complete"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 13
last-verified: "2026-07-28T23:25:14+02:00"
audit-date: "2026-07-28T23:25:14+02:00"
audit-level: "static-review"
validation-authority: "livre-v-reference-profile"
---

# Audit — Fiche 13 : Structures JSON et formats d’échange

## 1. Décision

La fiche est conforme au profil spécialisé du Livre V au niveau `static-review`. Elle fournit une référence non linéaire des formats d’échange, complétée par une campagne temporaire de 24 contrôles locaux en mémoire. Aucun convertisseur permanent, fichier Godot ou artefact du Companion Pack n’est matérialisé.

## 2. Périmètre contrôlé

| Domaine | Couverture | Propriétaire conservé |
|---|---|---|
| contrat de format | identité, modèle, syntaxe, encodage, schéma, évolution et preuve | systèmes propriétaires des Livres I à IV |
| couches | métier, modèle, représentation, document, flux, sérialisation, transport et stockage | chapitres 11 et 12 du Livre II pour les transports |
| encodage et média | UTF-8, BOM, fins de ligne, extensions et types média | RFC et registres officiels |
| JSON | profil strict, doublons, nombres finis, ordre et nullabilité | RFC 8259 et codecs propriétaires |
| JSON Schema | dialecte 2020-12, `$schema`, `$id`, types et champs | schémas futurs du Companion Pack |
| versionnement | `format`, `format_version`, métadonnées, payload et migrations | Livre II, chapitre 9 |
| JSONL | une valeur compacte par ligne | Livre II, chapitre 11 |
| JSON Text Sequences | séparateur `0x1E` et `application/json-seq` | RFC 7464 |
| CSV | dialecte, en-tête, types, multiline, `null` et formules | contrats d’import et d’export futurs |
| YAML | profil 1.2.2, document unique, chargeur sûr, tags et aliases | configurations humaines bornées |
| formats Godot | `.tres`, `.res`, `.tscn`, `.scn`, `.escn` et caches | Godot et Livre II, chapitre 7 |
| configurations | `res://`, `user://`, `ConfigFile`, sauvegardes, caches et logs | Livres II, chapitres 7 et 9 |
| conversions | correspondances, pertes, round-trip, staging et rapport | Companion Pack futur |
| canonicalisation | pretty-print, convention interne, JCS, hash et signature | Livre II, chapitre 29 et publication future |
| sécurité | limites, données non fiables, formules, tags, archives et chemins | Livre IV et chapitre 25 du Livre V |

## 3. Conformité Livre V

- `document-format: "reference-cards"` présent ;
- treize marqueurs `l5:card` et trois marqueurs `l5:matrix` ;
- index express avant les cartes ;
- tables de décision avant les paragraphes ;
- paragraphes courts et accès non linéaire ;
- liens profonds vers les tutoriels propriétaires ;
- exemples valides et invalides compacts, sans procédure dupliquée ;
- aucun résultat d’apprentissage ni synthèse `Project Asteria` importé du profil tutoriel ;
- aucun bloc de code clôturé ;
- niveau de preuve et limites visibles.

## 4. Couverture du plan maître

| Exigence | Réponse |
|---|---|
| JSON | FMT-02 à FMT-05 |
| JSONL | FMT-05 |
| CSV | FMT-06 |
| YAML | FMT-07 |
| formats Godot | FMT-08 et FMT-09 |
| encodage | FMT-02 |
| schémas | FMT-04 et Matrice B |
| version | FMT-04 |
| validation | Matrice B et FMT-12 |
| avantages et limites | Matrice A et chaque carte de format |
| sécurité | FMT-06, FMT-07 et FMT-12 |
| structures canoniques | FMT-04 et FMT-10 |
| fiches formats | FMT-03, 05, 06, 07, 08 et 09 |
| exemples valides et invalides | FMT-03, 05, 06 et 07 |
| convertisseurs | contrat FMT-11 ; fichiers permanents réservés au Companion Pack |
| validateurs automatiques | campagne temporaire de 24 cas et portes permanentes |

## 5. Frontières

- les données de conception, Resources, JSON et configurations restent au Livre II, chapitre 7 ;
- les sauvegardes, migrations de documents et slots restent au Livre II, chapitre 9 ;
- le protocole JSONL du processus compagnon reste au Livre II, chapitre 11 ;
- HTTP, WebSocket et enveloppes réseau restent au Livre II, chapitre 12 ;
- les codecs Python et pipelines de conversion restent au Livre II, chapitre 29 et au Companion Pack ;
- SQLite et ses migrations restent au chapitre 14 ;
- les diagnostics transversaux restent au chapitre 20 ;
- les benchmarks restent au chapitre 21 ;
- les compatibilités restent au chapitre 22 ;
- les licences, provenance et conformité restent au chapitre 25.

## 6. Exactitude technique statique

Les références officielles ont été revues le 28 juillet 2026 : RFC 8259, RFC 4180, RFC 7464, RFC 8785, RFC 9512, YAML 1.2.2, JSON Schema 2020-12, Python 3.14, PyYAML, OWASP CSV Injection et Godot `4.7.1-stable`.

La fiche distingue correctement :

- JSONL et JSON Text Sequences ;
- modèle logique, représentation, document, flux, transport et stockage ;
- syntaxe JSON, profil strict, schéma et invariants métier ;
- champ absent et valeur `null` ;
- `format_version`, `schema_version`, `$schema`, `$id` et version du producteur ;
- dialecte CSV et type média `text/csv` ;
- YAML 1.2.2, chargeur sûr et profil de sécurité ;
- formats texte et binaires de Godot ;
- pretty-print, canonicalisation interne et JCS RFC 8785 ;
- empreinte, signature, chiffrement et compression ;
- round-trip par octets, modèle, normalisation ou perte.

## 7. Campagne temporaire de fixtures

La CI installe PyYAML et `jsonschema`, puis exécute `tools/tmp_l5_ch13_validate_formats.py`. Les 24 cas couvrent JSON strict, JSON Schema 2020-12, JSONL, CSV, YAML et canonicalisation. Le rapport `dist/QA-LIVRE-V-CH13-FORMATS.json` conserve versions, résultats et réserves.

Cette campagne ne qualifie pas Godot, les autres bibliothèques de parsing, un convertisseur permanent, une plateforme complète ou des données réelles.

## 8. Métriques

| Mesure | Valeur |
|---|---:|
| lignes | 419 |
| titres | 18 |
| cartes | 13 |
| matrices | 3 |
| liens Markdown | 53 |
| renvois vers les Livres I à IV | 18 |
| liens profonds propriétaires | 18 |
| liens officiels | 19 |
| blocs clôturés | 0 |
| fixtures temporaires | 24 |

## 9. Contrôles et réserves

- structure, métadonnées, liens locaux et doublons : validateur permanent ;
- marqueurs et fragments du Livre V : validateur spécialisé ;
- repères de contexte : aucun bloc procédural dans la fiche ;
- fixtures : chaînes et flux en mémoire seulement ;
- PDF : interdit pour ce lot léger ;
- aucun binaire Godot ou projet Godot chargé ;
- aucune Resource ou scène parsée, importée ou sauvegardée ;
- aucun fichier utilisateur, secret, réseau ou archive traité ;
- aucun convertisseur permanent créé ;
- aucun fichier du Companion Pack matérialisé ;
- aucune matrice inter-parseurs, OS ou architecture exécutée ;
- aucune campagne de performance ou de sécurité offensive ;
- aucune approbation juridique organisationnelle.

## 10. Décision finale

Accepté au niveau `static-review` après réussite des validateurs permanents et des 24 fixtures temporaires. Les formats et convertisseurs réels restent non qualifiés hors de l’environnement et du périmètre enregistrés.
