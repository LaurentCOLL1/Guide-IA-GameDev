---
title: "Livre V — Fiche 13 : Structures JSON et formats d’échange"
id: "DOC-L5-CH13"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 13
last-verified: "2026-07-28T23:25:14+02:00"
audit-status: "complete"
audit-date: "2026-07-28T23:25:14+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-13.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "structured-data-exchange-formats"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Structures JSON et formats d’échange

> **Type de document :** cartes de formats, matrices de conversion, profils stricts et portes de validation.
> **Référence :** JSON RFC 8259, JSON Schema 2020-12, YAML 1.2.2, CSV profil RFC 4180 et formats Godot `4.7.1-stable`.
> **Principe :** un texte parsable n’est ni un document conforme au schéma, ni une donnée métier valide, ni un échange sans perte, ni un artefact authentifié.

## Index express

| Besoin | Ouvrir |
|---|---|
| définir le périmètre d’un format | [FMT-00](#fmt-00--contrat-dun-format) |
| choisir JSON, JSONL, CSV, YAML ou Godot | [Matrice A](#matrice-a--sélection-par-besoin) |
| distinguer modèle, document, transport et stockage | [FMT-01](#fmt-01--couches-et-vocabulaire) |
| fixer encodage, extension et type média | [FMT-02](#fmt-02--encodage-identité-et-média) |
| appliquer un profil JSON strict | [FMT-03](#fmt-03--json-strict) |
| séparer schéma, enveloppe et versions | [FMT-04](#fmt-04--schémas-enveloppes-et-versions) |
| ordonner les contrôles | [Matrice B](#matrice-b--couches-de-validation) |
| traiter un flux JSON par lignes | [FMT-05](#fmt-05--jsonl-et-séquences-json) |
| définir un dialecte CSV | [FMT-06](#fmt-06--csv-et-contrat-tabulaire) |
| borner un document YAML | [FMT-07](#fmt-07--yaml-sûr-et-prévisible) |
| choisir un format Godot | [FMT-08](#fmt-08--ressources-scènes-et-formats-godot) |
| utiliser `ConfigFile` ou un fichier runtime | [FMT-09](#fmt-09--configurations-et-fichiers-runtime) |
| convertir les types sans perte cachée | [Matrice C](#matrice-c--correspondances-et-pertes) |
| obtenir des octets reproductibles | [FMT-10](#fmt-10--canonicalisation-et-intégrité) |
| qualifier un convertisseur | [FMT-11](#fmt-11--conversion-et-round-trip) |
| accepter un format en production | [FMT-12](#fmt-12--sécurité-limites-et-acceptation) |

---

<!-- l5:card -->
## FMT-00 — Contrat d’un format

| Champ | Règle |
|---|---|
| identité | nom stable, version, extension, type média et propriétaire |
| modèle | objets représentables, types, cardinalités, ordre et nullabilité |
| syntaxe | grammaire ou format moteur précisément nommé |
| encodage | jeu de caractères, BOM, fins de ligne et normalisation |
| enveloppe | famille, version, identifiant, métadonnées et payload |
| schéma | dialecte, identifiant, règles structurelles et politique de références |
| sémantique | identifiants, unités, plages, relations et invariants métier |
| évolution | compatibilité, migration, champs inconnus et retrait |
| limites | octets, profondeur, éléments, longueur, nombres et temps de traitement |
| sécurité | données non fiables, tags, formules, archives, chemins et secrets |
| conversion | source, cible, pertes, ordre, précision, erreurs et rapport |
| preuve | fixtures, commandes, versions, résultats, empreintes et réserves |

**Réponse rapide :** le format décrit une représentation ; le schéma en décrit une structure ; le codec transforme des valeurs ; le transport déplace des octets ; le stockage les conserve. Le chapitre propriétaire des [données de conception et configurations](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md#3-périmètre-et-frontières) et celui des [sauvegardes versionnées](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#3-périmètre-et-frontières) décident de la sémantique, pas cette fiche.

---

<!-- l5:matrix -->
## Matrice A — Sélection par besoin

| Besoin principal | Format de départ | Pourquoi | Source propriétaire | Repli ou limite |
|---|---|---|---|---|
| échange structuré inter-outils | JSON strict | petit modèle commun, schémas et APIs | [échange avec un outil externe](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md#5-matrice-de-décision) | conversions explicites pour les types Godot |
| messages ou enregistrements incrémentaux | JSONL déclaré | une valeur JSON par ligne | [protocole JSON par lignes](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md#9-protocole-json-par-lignes) | pas de mise en forme multilignes |
| séquence normalisée avec séparateur de contrôle | JSON Text Sequences | format IETF `application/json-seq` | [RFC 7464](https://www.rfc-editor.org/rfc/rfc7464.html) | distinct de JSONL |
| données tabulaires plates | CSV avec dialecte déclaré | table simple et outils bureautiques | [module CSV Python](https://docs.python.org/3.14/library/csv.html) | aucun type imbriqué ni `null` natif |
| configuration humaine commentée | YAML 1.2.2 borné | lisibilité et commentaires | [spécification YAML 1.2.2](https://yaml.org/spec/1.2.2/) | chargeur sûr et profil réduit obligatoires |
| donnée Godot éditable et versionnée | `.tres` | Resource texte et Inspector | [Resource personnalisée](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md#6-pourquoi-utiliser-une-resource-personnalisée) | format propriétaire du moteur |
| scène Godot versionnée | `.tscn` | arbre de scène texte | [format TSCN Godot 4.7](https://docs.godotengine.org/en/4.7/engine_details/file_formats/tscn.html) | laisser Godot gérer UID et références |
| ressource ou scène compacte | `.res` ou `.scn` | variante binaire Godot | [ResourceSaver](https://docs.godotengine.org/en/4.7/classes/class_resourcesaver.html) | diff Git et inspection moins pratiques |
| configuration locale Godot | `ConfigFile` / `.cfg` | valeurs Variant en forme INI | [catégories de données](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md#4-quatre-catégories-de-données) | pas un format INI universel |
| sauvegarde pédagogique | enveloppe JSON versionnée | validation et migration explicites | [choix du format de sauvegarde](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#6-choisir-le-format-de-référence) | mesurer avant compression ou binaire |

**Décision :** choisir d’abord le modèle et l’autorité, puis le format. L’extension la plus familière n’est pas automatiquement la plus sûre ni la plus compatible.

---

<!-- l5:card -->
## FMT-01 — Couches et vocabulaire

| Couche | Question | Exemple | Erreur fréquente |
|---|---|---|---|
| donnée métier | que signifie la valeur ? | identifiant d’objet, unité, état | faire porter l’autorité au fichier |
| modèle logique | quelles structures existent ? | objet, liste, table, graphe | forcer un graphe dans une table plate |
| représentation | comment les valeurs sont-elles exprimées ? | objet JSON, mapping YAML, Resource | confondre type runtime et type sérialisé |
| document | où commence et finit une unité ? | un JSON, un document YAML | concaténer deux JSON sans framing |
| flux | comment plusieurs unités sont-elles délimitées ? | JSONL, JSON Text Sequences | appeler tout flux « JSON streaming » |
| schéma | quelles formes sont admises ? | JSON Schema 2020-12 | croire que le schéma porte toutes les règles métier |
| sérialisation | comment produire le texte ou les octets ? | codec JSON, ResourceSaver | confondre sérialisation et stockage |
| transport | comment les octets voyagent-ils ? | stdio, HTTP, WebSocket | inclure les URL dans le domaine |
| stockage | où les octets restent-ils ? | `res://`, `user://`, archive | traiter un cache comme source canonique |
| conteneur | compression, paquet ou archive | gzip, ZIP | attribuer chiffrement ou signature au conteneur |

Le [port applicatif indépendant du transport](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md#51-port-applicatif) et l’[enveloppe réseau versionnée](../Livre-II/CHAPITRE-12-HTTP-WebSocket-API-compatibles-OpenAI-et-files-de-taches.md#9-enveloppe-réseau) illustrent cette séparation. Un changement de transport ne doit pas redéfinir la signification du payload.

---

<!-- l5:card -->
## FMT-02 — Encodage, identité et média

| Élément | Profil de référence | Validation |
|---|---|---|
| JSON échangé | UTF-8, sans BOM produit | décodage strict puis parse |
| JSONL | UTF-8, une valeur par ligne, terminaison LF recommandée | ligne vide refusée, numéro de ligne conservé |
| JSON Text Sequences | UTF-8, `RS 0x1E` avant chaque JSON et LF après | type `application/json-seq` |
| CSV | encodage et dialecte déclarés ; UTF-8 préféré | séparateur, guillemet, échappement et fin de ligne |
| YAML | Unicode ; profil du projet en UTF-8 | version et nombre de documents contrôlés |
| JSON média | `application/json` | ne pas ajouter un paramètre `charset` au contrat |
| CSV média | `text/csv` | dialecte non déduit du média seul |
| YAML média | `application/yaml` | anciens alias non retenus comme canonique |
| JSONL média | aucun type média standardisé | déclarer le choix local sans le présenter comme IANA |
| extension | indice de routage | ne remplace ni sniffing contrôlé ni validation |
| compression | couche extérieure nommée | limite décompressée et empreinte des octets définie |
| fins de ligne | convention enregistrée | ne pas modifier silencieusement des données signées |

Le [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259.html) définit JSON et `application/json`; le [RFC 4180](https://www.rfc-editor.org/rfc/rfc4180.html) documente un profil CSV sans rendre tous les CSV identiques; le [RFC 9512](https://www.rfc-editor.org/rfc/rfc9512.html) enregistre `application/yaml` et `+yaml`.

---

<!-- l5:card -->
## FMT-03 — JSON strict

| Notion | Admis | Refus ou réserve |
|---|---|---|
| valeur racine | objet, tableau, chaîne, nombre, booléen ou `null` | le contrat applicatif peut exiger un objet |
| objet | noms de membres uniques | doublons refusés même si un parseur garde le dernier |
| tableau | ordre significatif | homogénéité seulement si le schéma l’impose |
| chaîne | Unicode valide, échappements JSON | commentaires et chaînes entre apostrophes |
| nombre | syntaxe décimale JSON | `NaN`, `Infinity`, virgule décimale et zéro initial |
| entier interopérable | de `-9007199254740991` à `9007199254740991` par défaut | plage supérieure seulement avec contrat spécialisé |
| booléen | `true`, `false` | `True`, `False`, `yes`, `no` |
| absence | `null` lorsque prévu | champ absent et `null` ne sont pas synonymes |
| espace | autour des jetons | aucune signification métier |
| ordre des membres | non autoritaire | ne pas utiliser comme oracle métier |

| Exemple compact | Statut | Motif |
|---|---|---|
| `{"format":"asteria-item","format_version":1,"id":"item.iron"}` | JSON et contrat minimal plausibles | objet, noms uniques et types attendus |
| `{format:'asteria-item',}` | JSON invalide | nom non cité, apostrophes et virgule finale |
| `{"format":"asteria-item","format_version":"1"}` | JSON valide, contrat invalide | version encodée comme chaîne |
| `{"id":"a","id":"b"}` | rejet du profil strict | membre dupliqué et comportement de parseur variable |
| `{"weight":NaN}` | rejet du profil strict | valeur non définie par le RFC 8259 |

La classe [JSON de Godot](https://docs.godotengine.org/en/4.7/classes/class_json.html) et le [module `json` Python](https://docs.python.org/3.14/library/json.html) ne remplacent pas les contrôles du contrat. Python accepte notamment des valeurs non finies et des noms répétés avec ses options par défaut ; le profil strict doit les refuser explicitement.

---

<!-- l5:card -->
## FMT-04 — Schémas, enveloppes et versions

| Élément | Rôle | Exemple de décision |
|---|---|---|
| `format` | identifie la famille du document | `project-asteria-save` |
| `format_version` | versionne la structure de l’enveloppe | entier positif |
| `schema_version` | versionne un schéma métier lorsque distinct | ne pas le dupliquer sans besoin |
| `$schema` | sélectionne le dialecte JSON Schema | URI 2020-12 exacte |
| `$id` | identité canonique du schéma | URI stable et versionnée |
| `game_version` | indique le producteur | diagnostic, pas substitut de format |
| `minimum_reader_version` | annonce un lecteur minimal | politique appliquée explicitement |
| `payload` | porte les données autoritaires | validé avant toute mutation |
| `metadata` | aide affichage, tri ou diagnostic | jamais utilisée comme autorité métier |
| `integrity` | décrit empreinte et portée | champ exclu de son propre calcul |
| champs inconnus | `reject`, `ignore` ou `preserve` | politique choisie par version |
| migration | ancien document vers modèle courant | en mémoire avant application |

La [version du format](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#43-version-du-format), la [validation](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#46-validation) et le [contrat du document](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#10-contrat-du-document) restent les modèles propriétaires. La fiche utilise [JSON Schema 2020-12](https://json-schema.org/draft/2020-12) comme dialecte de référence, sans prétendre qu’un schéma remplace les invariants métier.

---

<!-- l5:matrix -->
## Matrice B — Couches de validation

| Ordre | Porte | Question | Refus typique | Preuve |
|---:|---|---|---|---|
| 1 | octets | taille, compression et encodage sont-ils admis ? | BOM interdit, archive excessive | compteur avant parse |
| 2 | framing | le document ou l’enregistrement est-il complet ? | ligne JSONL vide, séquence tronquée | position et numéro de record |
| 3 | syntaxe | le parseur accepte-t-il le texte ? | virgule finale, guillemet non fermé | erreur et position |
| 4 | profil strict | les divergences de parseurs sont-elles fermées ? | doublon, nombre non fini | options strictes |
| 5 | identité | famille et version sont-elles reconnues ? | `format` inconnu, version future | code stable |
| 6 | schéma | types, champs et cardinalités conviennent-ils ? | champ requis absent | rapport JSON Schema |
| 7 | sémantique | identifiants, unités et relations sont-ils valides ? | référence inconnue | validateur propriétaire |
| 8 | sécurité | données, chemins et actions restent-ils autorisés ? | tag YAML, formule CSV | politique de refus |
| 9 | migration | le modèle courant est-il obtenu sans perte cachée ? | saut de version absent | rapport de migration |
| 10 | intégrité | les octets ou le payload correspondent-ils ? | empreinte différente | hash recalculé |
| 11 | application | tous les candidats sont-ils prêts ? | section partiellement valide | commit atomique |
| 12 | observation | résultat et réserves sont-ils enregistrés ? | succès sans preuve | rapport et artefacts |

**Règle :** aucune porte tardive ne répare silencieusement une porte antérieure. Un parse réussi ne transforme pas une donnée inconnue en donnée autorisée.

---

<!-- l5:card -->
## FMT-05 — JSONL et séquences JSON

| Format | Délimitation | Média | Usage | Réserve |
|---|---|---|---|---|
| JSONL / NDJSON | une valeur JSON par ligne LF | non standardisé | logs, lots, stdio, datasets | pas de JSON pretty-print multilignes |
| JSON Text Sequences | `RS 0x1E`, JSON, puis LF | `application/json-seq` | séquence IETF récupérable | octets de contrôle distincts |
| tableau JSON | un document contenant un tableau | `application/json` | lot borné chargé ensemble | mémoire et clôture nécessaires |
| concaténation brute | aucune | aucune | aucun | ambiguë et interdite |

| Exemple compact | Statut |
|---|---|
| `{"id":"a"}` puis LF puis `{"id":"b"}` | deux enregistrements JSONL valides |
| objet JSON mis en forme sur plusieurs lignes | invalide pour le profil JSONL du projet |
| ligne vide entre deux valeurs | refusée, même si certains outils l’ignorent |
| `RS {"id":"a"} LF` | élément JSON Text Sequence, pas JSONL |

Le [protocole local du chapitre 11](../Livre-II/CHAPITRE-11-Communication-Godot-avec-les-services-IA-locaux.md#9-protocole-json-par-lignes) choisit JSONL : une enveloppe compacte par ligne, identifiant de corrélation obligatoire et limite de taille. Le site [JSON Lines](https://jsonlines.org/) documente la convention courante ; le [RFC 7464](https://www.rfc-editor.org/rfc/rfc7464.html) décrit un autre framing. Chaque record reçoit numéro, taille et résultat de validation ; une ligne invalide n’est jamais appliquée partiellement.

---

<!-- l5:card -->
## FMT-06 — CSV et contrat tabulaire

| Paramètre | Doit être déclaré |
|---|---|
| encodage | UTF-8 dans le profil du guide |
| séparateur | virgule, point-virgule, tabulation ou autre caractère unique |
| guillemet | caractère et règle de doublement ou d’échappement |
| fin de record | LF ou CRLF |
| en-tête | présent, noms, ordre et casse |
| types | chaîne, entier, décimal, booléen, date et identifiant |
| `null` | interdit, jeton explicite ou colonne auxiliaire |
| chaîne vide | distinguée de `null` si les deux existent |
| décimal | point dans le profil machine, jamais convention locale implicite |
| date et heure | chaîne ISO 8601/RFC 3339 avec fuseau lorsque nécessaire |
| colonnes inconnues | rejet, préservation ou ignorance explicite |
| formule | mode sûr pour les exports ouverts dans un tableur |

| Exemple compact | Lecture |
|---|---|
| `id,name` | en-tête de deux colonnes |
| `item.iron,"Marteau, fer"` | virgule contenue protégée par guillemets |
| `item.note,"ligne 1\nligne 2"` | un record peut couvrir plusieurs lignes physiques selon le dialecte |
| cellule commençant par `=`, `+`, `-` ou `@` | donnée potentiellement interprétée comme formule par un tableur |

Le RFC 4180 est **informatif** et ne couvre pas tous les dialectes. Le lecteur Python doit ouvrir les fichiers avec `newline=""` et un dialecte explicite ; Godot expose `get_csv_line()` et `store_csv_line()` dans [FileAccess](https://docs.godotengine.org/en/4.7/classes/class_fileaccess.html). Une table CSV ne possède ni objet imbriqué, ni type `null`, ni schéma universel. Les exports bureautiques contenant des données non fiables appliquent une politique contre la [CSV Formula Injection](https://owasp.org/www-community/attacks/CSV_Injection) et conservent la transformation dans le rapport.

---

<!-- l5:card -->
## FMT-07 — YAML sûr et prévisible

| Capacité YAML | Profil du guide | Motif |
|---|---|---|
| version | YAML 1.2.2 déclarée par contrat | résolution différente des anciens profils |
| documents | un seul par fichier sauf besoin explicite | un lecteur ne doit pas ignorer les suivants |
| mappings | clés uniques exigées | comportement de doublons dépendant du parseur |
| séquences | admises et bornées | taille et profondeur contrôlées |
| scalaires | chaînes ambiguës citées | éviter interprétation implicite inattendue |
| commentaires | admis pour configuration humaine | perdus dans beaucoup de round-trips |
| anchors et aliases | interdits par défaut ou budget très faible | graphe, cycles et amplification |
| merge keys | interdits dans le profil portable | extension et comportements variables |
| tags standards | sous-ensemble nécessaire seulement | types implicites à contrôler |
| tags personnalisés | interdits pour les entrées non fiables | construction d’objets ou code selon bibliothèque |
| chargeur | API sûre et version enregistrée | `safe_load` ne remplace pas les limites |
| média | `application/yaml` | `text/yaml` et `application/x-yaml` non canoniques |

| Exemple compact | Statut |
|---|---|
| `enabled: true` | booléen YAML 1.2 |
| `enabled: "yes"` | chaîne explicite et portable |
| `value: !!python/object:module.Class {}` | interdit pour une entrée non fiable |
| `---` suivi de deux documents | refus si le contrat attend un document unique |

YAML est un langage de sérialisation plus riche que JSON, pas un simple JSON avec commentaires. Le [RFC 9512](https://www.rfc-editor.org/rfc/rfc9512.html) souligne les risques d’exécution arbitraire, d’épuisement de ressources et de streams multiples. PyYAML précise que [`safe_load`](https://pyyaml.org/wiki/PyYAMLDocumentation) limite les constructions aux types simples ; le projet ajoute encore des limites d’octets, profondeur, alias, clés et documents.

---

<!-- l5:card -->
## FMT-08 — Ressources, scènes et formats Godot

| Extension | Nature | Outil propriétaire | Usage | Réserve |
|---|---|---|---|---|
| `.tres` | Resource texte | `ResourceLoader` / `ResourceSaver` | donnée éditable, diff Git | format Godot, UID et références internes |
| `.res` | Resource binaire | mêmes singletons | chargement compact | inspection et fusion moins pratiques |
| `.tscn` | scène texte | éditeur et Resource API | arbre de scène versionné | ne pas traiter comme YAML ou INI générique |
| `.scn` | scène binaire | éditeur et Resource API | distribution ou chargement | pas de diff lisible |
| `.escn` | scène texte exportée | pipeline d’import | échange depuis un autre outil | importée vers une scène binaire dérivée |
| `.cfg` | configuration Godot de style INI | `ConfigFile` | réglages locaux non secrets | format non standardisé |
| `.godot/imported/` | cache d’import dérivé | importeurs Godot | accélération et artefacts | non source canonique |
| fichier texte externe | données ordinaires | `FileAccess` | JSON, CSV, texte | export explicite nécessaire selon projet |

Les formats texte Godot 4 utilisent `format=3`; cette valeur appartient au format moteur et ne remplace pas la version métier du contenu. Le [format TSCN](https://docs.godotengine.org/en/4.7/engine_details/file_formats/tscn.html) décrit scènes, ressources externes, sous-ressources, nœuds et connexions. `ResourceLoader` charge les ressources reconnues ; les fichiers texte ordinaires passent par `FileAccess`. Les fichiers `.tres` doivent être générés ou sauvegardés par Godot lorsque des UID et références internes interviennent, conformément à la [forme textuelle indicative du chapitre 7](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md#82-forme-textuelle-indicative).

**Frontière :** `StringName`, `Vector3`, `Color`, `NodePath`, références de Resources et sous-ressources n’ont pas de représentation JSON native. Le codec métier doit les convertir en structures simples et versionnées.

---

<!-- l5:card -->
## FMT-09 — Configurations et fichiers runtime

| Besoin | Support | Racine | Politique |
|---|---|---|---|
| définition de conception | `.tres` | `res://` | versionnée, relue et immuable au runtime |
| configuration livrée | `.cfg`, JSON ou Resource | `res://` | défauts non secrets |
| préférence utilisateur | `ConfigFile` ou document versionné | `user://` | validation et remplacement contrôlé |
| sauvegarde | enveloppe versionnée | `user://saves/` | snapshot cohérent, migration et secours |
| cache | format régénérable | `user://cache/` ou cache outil | supprimable sans perte de source |
| journal | JSONL ou texte structuré | `user://logs/` | rétention et rédaction des secrets |
| échange avec Python | JSON/JSONL/CSV/YAML selon contrat | workspace borné | staging, validation et promotion |
| secret | mécanisme dédié hors dépôt | hors `res://` | jamais dans un format de confort |

`ConfigFile` stocke des valeurs Variant en syntaxe de style INI, mais `.cfg` et `.ini` ne définissent pas un standard universel commun à tous les outils. Les couches défaut, locale et runtime restent séparées. Le chapitre 7 demeure propriétaire de la [configuration technique](../Livre-II/CHAPITRE-07-Donnees-avec-Resources-JSON-et-configurations.md#42-configuration-technique) ; le chapitre 9 demeure propriétaire des fichiers de sauvegarde et de leur [intégrité](../Livre-II/CHAPITRE-09-Sauvegardes-chargements-et-compatibilite-des-versions.md#47-intégrité).

---

<!-- l5:matrix -->
## Matrice C — Correspondances et pertes

| Valeur logique | JSON | Python | Godot | CSV | YAML | Décision |
|---|---|---|---|---|---|---|
| absence | `null` | `None` | `null` | aucune forme native | `null` | distinguer champ absent et valeur nulle |
| booléen | `true` / `false` | `bool` | `bool` | texte convenu | booléen | ne pas accepter `yes/no` comme convention transverse |
| entier | nombre | `int` | `int` 64 bits | texte décimal | entier | borner la plage interopérable |
| décimal | nombre | `float` ou `Decimal` | `float` | texte avec point | flottant | unité, précision et arrondi explicites |
| chaîne | chaîne Unicode | `str` | `String` | cellule | scalaire | encodage et normalisation définis |
| tableau | array | `list` / `tuple` | `Array` | plusieurs records ou cellule encodée | sequence | aucune cellule JSON cachée sans contrat |
| objet | object | `dict` / modèle | `Dictionary` / classe | colonnes plates | mapping | clés uniques et champs inconnus |
| identifiant | chaîne | type ou chaîne | `StringName` | chaîne | chaîne | syntaxe stable, jamais nom affiché |
| date-heure | chaîne | `datetime` | chaîne ou objet dédié | chaîne | timestamp ou chaîne | RFC 3339, fuseau et précision |
| octets | Base64 ou référence | `bytes` | `PackedByteArray` | Base64 | `!!binary` possible | taille, média et empreinte obligatoires |
| vecteur 3D | objet ou tableau explicite | dataclass/tuple | `Vector3` | trois colonnes | mapping/sequence | axes, unités et ordre versionnés |
| enum | code chaîne stable | `Enum` | `StringName`/enum | chaîne | chaîne | ne pas sérialiser un ordinal fragile |
| ressource | identifiant ou chemin autorisé | modèle | `Resource` | identifiant | mapping | jamais objet moteur brut dans un échange |
| graphe | nœuds et arêtes explicites | objets liés | objets/références | tables liées | anchors possibles | préférer identité explicite aux alias YAML |

**Règle :** une conversion réussie au niveau des types peut rester sémantiquement perdante. Le rapport indique chaque normalisation, arrondi, valeur par défaut, champ abandonné et ordre reconstruit.

---

<!-- l5:card -->
## FMT-10 — Canonicalisation et intégrité

| Notion | Signification | Ne prouve pas |
|---|---|---|
| pretty-print | présentation lisible | octets stables |
| minification | retrait d’espaces non significatifs | ordre ou nombres canoniques |
| normalisation métier | identifiants, unités ou casse transformés | conformité au format source |
| JSON canonique du projet | UTF-8, clés triées, séparateurs fixes, LF final, nombres finis | conformité au RFC 8785 |
| JCS RFC 8785 | schéma précis de canonicalisation JSON | sémantique métier ou authenticité |
| empreinte SHA-256 | identité relative des octets choisis | auteur, confiance ou absence de malveillance |
| signature | liaison cryptographique à une clé | droit de publier ou qualité du contenu |
| MAC | intégrité et authenticité partagées | non-répudiation publique |
| chiffrement | confidentialité selon algorithme et clés | intégrité si le mode ne l’apporte pas |
| compression | réduction de taille | chiffrement, signature ou innocuité |

Le [JSON canonique du chapitre 29](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#19-sérialiser-du-json-canonique) est une convention interne utile aux empreintes et golden files. Elle ne doit être appelée [JSON Canonicalization Scheme RFC 8785](https://www.rfc-editor.org/rfc/rfc8785.html) que si toutes les règles du RFC sont appliquées. La portée du hash précise si elle couvre le payload, l’enveloppe sans `integrity`, le fichier compressé ou l’archive finale.

---

<!-- l5:card -->
## FMT-11 — Conversion et round-trip

| Champ du convertisseur | Exigence |
|---|---|
| identité | nom, version, propriétaire et commit |
| source | format, version, encodage, schéma et limites |
| cible | format, version, dialecte et structure attendue |
| mapping | type par type, champ par champ et unité par unité |
| inconnus | rejet, préservation ou journalisation |
| valeurs par défaut | origine et condition d’application |
| ordre | conservé, trié ou non significatif |
| nombres | plage, précision, arrondi et valeurs non finies |
| texte | Unicode, normalisation, fins de ligne et espaces |
| dates | fuseau, précision et calendrier |
| effets | fichiers lus, staging écrit et destination remplacée |
| erreurs | codes stables, record, chemin JSON et message |
| rapport | compteurs, avertissements, pertes et empreintes |
| tests | nominal, invalide, limite, inconnus, répétition et rollback |

| Classe de round-trip | Critère |
|---|---|
| octets identiques | décodage puis encodage reproduit les mêmes octets |
| modèle identique | octets différents, valeurs logiques égales |
| normalisé | représentation volontairement réordonnée ou reformattée |
| avec pertes | information abandonnée ou précision réduite |
| aller simple | retour non défini ou source non reconstructible |

Pipeline minimal : **lire en zone bornée → parser strictement → valider schéma et sémantique → convertir vers un modèle intermédiaire → écrire en staging → repars­er la cible → comparer selon la classe annoncée → promouvoir**. Les écritures utilisent le [remplacement contrôlé](../Livre-II/CHAPITRE-29-Automatisation-Python-et-generation-de-donnees.md#18-écrire-un-fichier-par-remplacement-contrôlé). Les convertisseurs permanents, leurs fixtures et rapports appartiennent au Companion Pack.

---

<!-- l5:card -->
## FMT-12 — Sécurité, limites et acceptation

| Porte | Contrôle minimal | État de cette fiche |
|---|---|---|
| octets | taille brute et décompressée, encodage et BOM | contrat documenté |
| parse | profondeur, longueur, nombres et durée | fixtures temporaires seulement |
| JSON | doublons, valeurs non finies et version | fixtures temporaires prévues |
| JSON Schema | dialecte exact, références locales et format policy | fixture 2020-12 prévue |
| JSONL | ligne vide, taille par record et numéro | fixture temporaire prévue |
| CSV | dialecte, colonnes, multiline et formules | fixture temporaire prévue |
| YAML | chargeur sûr, documents, tags et alias | fixture temporaire prévue |
| Godot | extensions, UID, cache et API propriétaire | revue statique uniquement |
| conversion | pertes, champs inconnus et round-trip | aucun convertisseur permanent |
| chemins | racine autorisée et staging | aucun fichier utilisateur traité |
| secrets | rédaction et exclusion des formats publics | aucun secret manipulé |
| intégrité | portée, algorithme et recalcul | empreintes documentaires seulement |
| compatibilité | versions d’outils et plateformes | non qualifiée globalement |
| publication | licence, provenance et retrait | réservés aux chapitres 22 et 25 |

**Risques prioritaires :** document surdimensionné ou profondément imbriqué ; clés JSON dupliquées ; nombres hors plage ; références JSON Schema distantes non contrôlées ; ligne JSONL tronquée ; formule CSV ; archive ou compression explosive ; tags YAML constructeurs ; aliases YAML amplifiés ou cycliques ; stream YAML multidocument inattendu ; désérialisation d’objets ; chemin sortant du workspace ; secret copié dans une fixture ; cache Godot promu comme source.

**Acceptation :** la fiche reste `static-review`. Les fixtures locales temporaires peuvent confirmer des comportements bornés de Python, PyYAML et JSON Schema, mais ne qualifient ni tous les parseurs, ni Godot runtime, ni un convertisseur du Companion Pack. Une structure devient `qualified` seulement après une campagne conservant versions, commandes, fixtures, résultats, artefacts et réserves.
