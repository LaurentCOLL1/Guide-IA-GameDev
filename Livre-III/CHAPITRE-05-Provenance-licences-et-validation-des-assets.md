---
title: "Livre III — Chapitre 5 : Provenance, licences et validation des assets"
id: "DOC-L3-CH05"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre III"
chapter: 5
last-verified: "2026-07-22T23:35:44+02:00"
audit-status: "complete"
audit-date: "2026-07-22T23:35:44+02:00"
audit-report: "Livre-III/QA/AUDIT-CHAPITRE-05.md"
audit-level: "static-review"
reference-jurisdiction:
  production-base: "France"
  market-context: "European Union"
  verification-date: "2026-07-22"
reference-project:
  name: "Project Asteria"
  renderer: "Forward+"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Provenance, licences et validation des assets

> **Repères d’utilisation :** **[PS]** PowerShell 7, **[CMD]** Invite de commandes, **[WSL]** terminal WSL, **[DCT]** terminal dans un conteneur, **[DCK]** Docker Desktop, **[VSC]** Visual Studio Code, **[WEB]** navigateur, **[APP]** application graphique nommée, **[SORTIE]** résultat à lire sans le saisir, **[LECTURE]** exemple ou structure de référence. Voir la [convention complète](../Volume-0/annexes/CONVENTION-OUTILS-ET-CONTEXTES.md).

> **Identifiant stable :** `DOC-L3-CH05`  
> **Priorité :** Obligatoire  
> **Parcours :** Mode Solo · Mode Studio  
> **Public :** débutant à avancé  
> **Cadre de référence :** production basée en France, diffusion potentielle dans l’Union européenne

## 1. Rôle du chapitre

Un asset techniquement parfait peut rester inutilisable lorsque son origine, son auteur, ses droits, son consentement ou ses restrictions ne sont pas démontrables. Le présent chapitre transforme donc la provenance en **contrat de production** : aucun fichier ne devient publiable par simple présence dans le dépôt.

La politique couvre les modèles 3D, textures, images, concepts, polices, musiques, sons, voix, animations, captures de mouvement, données de scan, modèles IA, datasets, extensions, scripts et livrables fournis par des tiers. Elle s’applique aussi aux créations internes et générées.

Le chapitre ne fournit pas d’avis juridique personnalisé. Il organise les informations, les preuves et les portes de décision nécessaires pour qu’une personne compétente puisse vérifier un asset. Lorsqu’un contrat, une juridiction, une personne, une marque ou une exploitation inhabituelle soulève un doute, le statut reste bloqué jusqu’à revue adaptée.

> **[LECTURE] Chaîne de décision — Ne pas saisir.**

```text
Source ou création
    ↓
Identité stable de l’asset
    ↓
Fiche d’asset et preuves brutes
    ↓
Licence, contrat, consentement et restrictions
    ↓
Chaîne de transformations et dépendances
    ↓
Contrôles automatiques minimaux
    ↓
Revue humaine responsable
    ↓
Statut : accepté, limité, bloqué ou retiré
    ↓
Publication immuable ou remplacement versionné
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis :** la chaîne interdit de sauter directement d’un téléchargement ou d’une génération à une publication.
- **Décisions :** l’automatisation contrôle la présence et la cohérence des données ; la décision d’usage reste humaine.
- **Invariant :** un fichier sans preuve suffisante reste identifiable et conservé en quarantaine, mais n’entre pas dans une livraison.
- **Résultat attendu :** chaque asset publié peut être relié à une source, une autorité, des restrictions et une décision enregistrée.

## 2. Résultats d’apprentissage

À la fin du chapitre, le lecteur sait :

- distinguer droit d’auteur, droits patrimoniaux, droit moral, droits voisins, licence, cession, consentement, marque, droit à l’image et données personnelles ;
- ne pas déduire un droit d’usage depuis un achat, un téléchargement, une commande ou une génération ;
- attribuer un identifiant stable à chaque asset et à chaque version publiée ;
- remplir une fiche d’asset et un registre de provenance ;
- enregistrer auteurs, titulaires, sources, outils, licences, contrats, transformations et dépendances ;
- qualifier les assets internes, commandés, achetés, ouverts, libres, publics, générés et mixtes ;
- traiter séparément modèles IA, datasets, entrées, sorties, extensions et services ;
- encadrer voix, image, interprétation, scan et capture de mouvement ;
- appliquer des statuts de blocage, d’acceptation limitée, de retrait et de remplacement ;
- automatiser des contrôles de structure sans présenter le script comme une validation juridique ;
- conserver l’historique et retirer un asset contesté sans effacer les preuves.

## 3. Niveau de preuve et frontière juridique

Le chapitre est accepté au niveau `static-review`. Les règles de production, schémas, statuts et scripts ont été relus contre les sources institutionnelles citées à la fin du chapitre. Aucun contrat de `Project Asteria`, aucune licence commerciale, aucun consentement, aucun registre réel et aucun audit juridique individualisé ne sont revendiqués comme matérialisés.

Dans le cadre français, le droit d’auteur naît du seul fait de la création. Une commande ou un contrat de service ne transfère donc pas automatiquement tous les droits nécessaires au projet. Lorsqu’une transmission de droits est requise, le projet exige une preuve écrite et une délimitation suffisamment précise des droits, usages, territoires et durées concernés.

La voix et l’image peuvent identifier une personne physique. Une interprétation enregistrée peut aussi mobiliser des droits propres à l’artiste-interprète. Le pipeline sépare donc :

- l’autorisation de traiter ou conserver une donnée personnelle ;
- l’autorisation d’enregistrer une personne ;
- les droits d’exploiter sa prestation ;
- les droits sur le texte, la musique, l’image ou le personnage interprété ;
- les restrictions contractuelles et éditoriales du projet.

Aucun statut automatisé ne remplace la revue d’une personne compétente. `accepted` signifie seulement que la porte définie par le projet a été franchie avec les preuves disponibles à une date donnée.

## 4. Vocabulaire opérationnel

### 4.1 Asset

Élément consommé par la production ou la livraison : fichier source, export, texture, son, police, modèle, rig, animation, script, dataset, modèle IA, documentation ou paquet de preuves.

### 4.2 Source

Origine identifiable de l’asset ou de l’un de ses composants : auteur interne, prestataire, boutique, dépôt, archive, capture, séance, service ou génération.

### 4.3 Auteur et titulaire de droits

L’auteur est la personne à l’origine d’une création protégeable. Le titulaire des droits exploitables peut être l’auteur ou une autre personne selon la loi et les actes applicables. Le registre ne fusionne pas ces deux rôles.

### 4.4 Licence

Autorisation d’utiliser un élément selon des conditions données. Une licence ne signifie pas nécessairement transfert de propriété, exclusivité, autorisation de sous-licencier ou droit de redistribuer le fichier source.

### 4.5 Cession

Transmission de droits déterminés. Le registre conserve l’acte, les droits concernés, l’étendue, la destination, le territoire, la durée et les limites.

### 4.6 Consentement

Manifestation enregistrée d’une autorisation liée à une personne, une prestation ou une donnée. Son objet, sa portée, sa durée, les usages et les possibilités de retrait doivent rester distinguables.

### 4.7 Transformation

Opération qui modifie, combine, convertit ou dérive un asset : retouche, crop, retopologie, bake, remix, montage, entraînement, génération, conversion, compression ou export.

### 4.8 Preuve

Document ou empreinte permettant de vérifier une affirmation : contrat signé, facture, reçu, capture horodatée des conditions, fichier de licence, page archivée, consentement, journal de génération, manifeste ou SHA-256.

## 5. Typologie des assets

Le registre utilise une catégorie de provenance principale :

- `internal-original` : création réalisée en interne ;
- `commissioned` : création commandée à un tiers ;
- `purchased` : asset acquis auprès d’une boutique ou d’un fournisseur ;
- `open-licensed` : asset sous licence ouverte identifiée ;
- `public-domain-claimed` : élément annoncé comme relevant du domaine public, à confirmer selon l’usage et la juridiction ;
- `generated` : sortie d’un système génératif ;
- `captured` : photo, scan, audio, vidéo ou mocap produit pendant une séance ;
- `user-submitted` : contenu fourni par un utilisateur ou une communauté ;
- `mixed` : combinaison de plusieurs catégories ;
- `unknown` : origine insuffisante, statut bloqué.

La catégorie n’accorde aucun droit. Elle détermine seulement les questions et preuves à réunir.

## 6. Cycle de vie et statuts

> **[VSC] Visual Studio Code — Créer : `art/provenance/ASSET-STATUS-POLICY.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
statuses:
  intake:
    publishable: false
    meaning: "Asset reçu, informations encore incomplètes."
  quarantined:
    publishable: false
    meaning: "Origine ou sécurité à examiner avant ouverture ou transformation."
  under_review:
    publishable: false
    meaning: "Preuves présentes, décision humaine non terminée."
  blocked:
    publishable: false
    meaning: "Condition obligatoire absente, incompatible ou contestée."
  accepted_limited:
    publishable: true
    meaning: "Usage autorisé uniquement dans le périmètre déclaré."
  accepted:
    publishable: true
    meaning: "Porte de publication du projet franchie."
  withdrawn:
    publishable: false
    meaning: "Asset retiré des nouvelles livraisons, historique conservé."
  superseded:
    publishable: false
    meaning: "Remplacé par une autre version ou un autre asset."
terminal_statuses:
  - withdrawn
  - superseded
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Champs importants :** `publishable` répond à la porte technique, tandis que `meaning` documente le sens métier.
- **Invariant :** `accepted_limited` ne devient jamais un synonyme de `accepted` ; son périmètre d’usage doit être contrôlé au moment de la livraison.
- **Frontière :** un statut décrit la décision du projet à une date donnée, pas une garantie universelle de licéité.
- **Résultat attendu :** les outils de build peuvent refuser les statuts non publiables sans interpréter eux-mêmes un contrat.

## 7. Identifiant stable et versions

L’identifiant de provenance ne dépend pas du nom de fichier. `Project Asteria` utilise :

- `AST-ASSET-<DOMAINE>-<NOM>-<NNN>` pour l’asset logique ;
- `vNNN` pour une version source ou publiée ;
- un identifiant distinct pour chaque dépendance significative ;
- une relation explicite entre remplacement et élément remplacé.

Exemple : `AST-ASSET-TEX-STONEWALL-001` reste stable lorsque la texture passe de `v001` à `v002`. Une nouvelle photographie sans continuité de provenance reçoit un nouvel identifiant.

> **[VSC] Visual Studio Code — Créer : `art/provenance/ASSET-ID-POLICY.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
asset_id_pattern: '^AST-ASSET-(CONCEPT|MESH|TEX|MAT|FONT|MUSIC|SFX|VOICE|MOCAP|MODEL|DATA|SCRIPT)-[A-Z0-9]+-[0-9]{3}$'
version_pattern: '^v[0-9]{3}$'
immutable_after_acceptance: true
replacement_requires:
  - replacement_asset_id
  - reason
  - decision_date
  - approver
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Motifs :** les expressions régulières imposent une catégorie, un nom ASCII et un numéro stable.
- **Invariant :** une version acceptée n’est pas réécrite ; toute correction crée une nouvelle version ou un remplacement.
- **Dépendances :** le remplacement conserve un lien vers l’asset retiré au lieu de supprimer son existence historique.
- **Résultat attendu :** une scène, un rapport et une livraison peuvent citer la même identité sans dépendre du chemin actuel.

## 8. Fiche d’asset obligatoire

> **[VSC] Visual Studio Code — Créer : `art/provenance/assets/AST-ASSET-TEX-STONEWALL-001.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
asset_id: "AST-ASSET-TEX-STONEWALL-001"
version: "v001"
title: "Stone wall material"
category: "mixed"
status: "under_review"
owner_team: "environment-art"
source:
  origin_type: "purchased"
  provider: "Example Marketplace"
  source_url: "https://example.invalid/item/stone-wall"
  acquired_on: "2026-07-22"
  receipt_evidence: "../../evidence/AST-ASSET-TEX-STONEWALL-001/receipt.pdf"
creators:
  - name: "Provider account name"
    role: "original creator"
rights:
  licence_id: "LicenseRef-EXAMPLE-MARKETPLACE-2026"
  commercial_use: "reviewed"
  modification: "reviewed"
  redistribution_source: "forbidden"
  redistribution_embedded: "reviewed"
  attribution: "required"
  territory: "contract_defined"
  duration: "contract_defined"
  sublicensing: "unknown"
  ai_training: "unknown"
transformations:
  manifest: "../../transformations/AST-ASSET-TEX-STONEWALL-001-v001.yaml"
dependencies: []
personal_data:
  present: false
publication_scope:
  products:
    - "Project Asteria game builds"
  excluded:
    - "standalone source pack"
review:
  automated_checks: "pending"
  human_decision: "pending"
  reviewer: null
  reviewed_on: null
proof_sha256: null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation des rôles :** `source`, `creators`, `rights`, `transformations` et `review` répondent à des questions différentes.
- **Statuts :** `reviewed`, `unknown` et `pending` évitent d’inventer une autorisation lorsque le contrat n’a pas encore été lu.
- **Périmètre :** `publication_scope` distingue l’intégration dans le jeu de la redistribution autonome des sources.
- **Preuve :** `proof_sha256` relie la fiche à un paquet de preuves immuable une fois la décision fermée.
- **Résultat attendu :** la fiche peut être validée automatiquement sans réduire le contrat à un simple nom de licence.

## 9. Registre central de provenance

Le registre central permet de chercher rapidement les assets, mais ne remplace pas leur fiche détaillée.

> **[VSC] Visual Studio Code — Créer : `art/provenance/ASSET-REGISTER.csv` — Ne pas saisir.**

```csv
asset_id,version,category,status,licence_id,owner_team,source_ref,replacement_asset_id
AST-ASSET-TEX-STONEWALL-001,v001,mixed,under_review,LicenseRef-EXAMPLE-MARKETPLACE-2026,environment-art,assets/AST-ASSET-TEX-STONEWALL-001.yaml,
AST-ASSET-SFX-DOOR-001,v001,internal-original,accepted,LicenseRef-ASTERIA-INTERNAL,sound,sources/AST-ASSET-SFX-DOOR-001.yaml,
AST-ASSET-VOICE-NARRATOR-001,v001,captured,blocked,LicenseRef-ASTERIA-PERFORMANCE-2026,audio,assets/AST-ASSET-VOICE-NARRATOR-001.yaml,
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Clé :** le couple `asset_id` et `version` identifie une ligne ; un validateur refuse les doublons.
- **Référence :** `source_ref` pointe vers la fiche détaillée et non vers le média brut.
- **Décision :** la voix reste `blocked` tant que les autorisations nécessaires ne sont pas fermées, même si le fichier audio existe.
- **Résultat attendu :** un responsable peut filtrer immédiatement les assets non publiables ou les licences personnalisées.

## 10. Chaîne de transformations

Chaque transformation significative devient un événement append-only. Le projet enregistre l’entrée, l’opérateur, l’outil, la version, les paramètres pertinents, la sortie et les empreintes.

> **[VSC] Visual Studio Code — Créer : `art/provenance/transformations/AST-ASSET-TEX-STONEWALL-001-v001.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
asset_id: "AST-ASSET-TEX-STONEWALL-001"
source_version: "v001"
events:
  - event_id: "EVT-0001"
    operation: "download"
    performed_on: "2026-07-22T20:00:00+02:00"
    operator: "user:art-lead"
    tool: "web-browser"
    input_sha256: null
    output_sha256: "REPLACE_WITH_REAL_SHA256"
    notes: "Archive originale conservée sans modification."
  - event_id: "EVT-0002"
    operation: "normal-map-conversion"
    performed_on: "2026-07-22T20:30:00+02:00"
    operator: "user:environment-artist"
    tool: "Material Tool 1.0"
    input_sha256: "REPLACE_WITH_REAL_SHA256"
    output_sha256: "REPLACE_WITH_REAL_SHA256"
    parameters:
      convention_from: "OpenGL"
      convention_to: "DirectX"
    notes: "Exemple documentaire non exécuté."
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Événements :** chaque entrée décrit une opération et ne modifie pas rétroactivement l’événement précédent.
- **Empreintes :** les SHA-256 distinguent la source acquise de la sortie transformée.
- **Paramètres :** seuls ceux nécessaires à la reproductibilité et à la compréhension juridique ou technique sont conservés.
- **Réserve :** les valeurs factices sont explicitement marquées et ne peuvent pas fermer une preuve réelle.

## 11. Paquet de preuves

> **[LECTURE] Arborescence de preuve — Ne pas saisir.**

```text
art/provenance/evidence/AST-ASSET-TEX-STONEWALL-001/
├── README.md
├── source-page.pdf
├── licence.txt
├── terms-snapshot.pdf
├── receipt.pdf
├── creator-statement.pdf
├── consent/
├── correspondence/
├── checksums.sha256
└── review-decision.yaml
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Rôle précis :** le paquet rassemble les éléments qui justifient la fiche sans les mélanger aux fichiers de production.
- **Conservation :** une capture ou un reçu ne remplace pas le texte contractuel applicable ; plusieurs preuves peuvent être nécessaires.
- **Confidentialité :** les contrats, identités et consentements sensibles suivent des droits d’accès plus stricts que le registre public du projet.
- **Résultat attendu :** le paquet peut être exporté pour une revue ou un incident sans rechercher des messages dispersés.

## 12. Carte des droits et autorisations

Une même production peut exiger plusieurs couches :

- droit d’auteur sur l’œuvre source ;
- droits patrimoniaux nécessaires à la reproduction, adaptation, représentation ou distribution ;
- droit moral, attribution et respect de l’intégrité ;
- droits voisins d’un artiste-interprète ou d’un producteur ;
- droit à l’image, respect de la vie privée et protection des données ;
- droit des marques, logos et signes distinctifs ;
- droits contractuels d’une boutique, plateforme, API ou service ;
- droits sur les modèles, poids, code, datasets et extensions d’une chaîne IA ;
- restrictions sectorielles, culturelles, territoriales ou de plateforme.

La présence d’une couche valide ne ferme pas les autres. Une musique originale peut appartenir au studio tandis que l’interprétation, l’enregistrement, un sample et le nom de l’artiste restent soumis à des droits distincts.

## 13. Matrice des licences

> **[VSC] Visual Studio Code — Créer : `art/provenance/LICENCE-MATRIX.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
fields:
  commercial_use:
    allowed_values: [allowed, forbidden, conditional, unknown]
  modification:
    allowed_values: [allowed, forbidden, conditional, unknown]
  source_redistribution:
    allowed_values: [allowed, forbidden, conditional, unknown]
  embedded_redistribution:
    allowed_values: [allowed, forbidden, conditional, unknown]
  attribution:
    allowed_values: [required, optional, forbidden_claim, unknown]
  share_alike:
    allowed_values: [required, not_required, unknown]
  territory:
    allowed_values: [worldwide, listed, unknown]
  duration:
    allowed_values: [perpetual, dated, revocable, unknown]
  sublicensing:
    allowed_values: [allowed, forbidden, conditional, unknown]
  ai_training:
    allowed_values: [allowed, forbidden, conditional, unknown]
  biometric_or_voice_cloning:
    allowed_values: [allowed, forbidden, conditional, unknown]
blocking_values:
  - forbidden
  - unknown
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Valeurs fermées :** `unknown` est une information utile et bloque l’usage concerné ; il ne doit pas être converti silencieusement en `allowed`.
- **Distinction :** redistribution intégrée et redistribution du fichier source sont séparées, car une licence peut autoriser l’une et interdire l’autre.
- **Contexte IA :** entraînement et clonage vocal restent des champs propres, même lorsque la licence générale autorise la modification.
- **Résultat attendu :** la matrice révèle immédiatement les questions à transmettre à la revue humaine.

## 14. Identifiants SPDX et licences personnalisées

SPDX fournit des identifiants courts normalisés pour de nombreuses licences et exceptions. Le registre utilise un identifiant SPDX seulement lorsque le texte applicable correspond réellement à l’entrée choisie.

Une licence commerciale, un contrat de commande, des conditions de boutique ou un consentement interne reçoivent un identifiant local :

`LicenseRef-ASTERIA-<NOM>-<ANNEE>`

> **[LECTURE] Expressions de licence — Ne pas saisir.**

```text
MIT
CC-BY-4.0
Apache-2.0 OR MIT
GPL-3.0-only WITH Classpath-exception-2.0
LicenseRef-ASTERIA-INTERNAL
LicenseRef-EXAMPLE-MARKETPLACE-2026
NOASSERTION
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Expressions :** `OR`, `AND` et `WITH` ont un sens formel ; ils ne sont pas des commentaires libres.
- **Licence locale :** `LicenseRef-...` conserve une identité stable lorsqu’aucun identifiant standard ne représente le texte.
- **Refus contrôlé :** `NOASSERTION` signale une incapacité à conclure et ne permet pas la publication.
- **Résultat attendu :** la chaîne évite les libellés vagues comme `free`, `royalty-free` ou `open` sans texte associé.

## 15. Licences Creative Commons

Les licences Creative Commons reposent notamment sur les conditions Attribution, Partage dans les mêmes conditions, Pas d’utilisation commerciale et Pas de modification. Le projet ne déduit jamais la compatibilité depuis le seul pictogramme.

Règles de production :

- conserver la version exacte de la licence et son lien ;
- enregistrer le titre, l’auteur, la source et les modifications ;
- vérifier si l’usage commercial est autorisé ;
- vérifier si les adaptations sont autorisées ;
- traiter `ShareAlike` comme une obligation de compatibilité à examiner ;
- ne pas appliquer une licence CC à une œuvre que le projet ne possède pas ou ne contrôle pas ;
- ne pas supposer qu’une licence couvre marques, vie privée, image, données ou droits de tiers ;
- conserver la preuve même lorsque le contenu disparaît du site source.

La dédicace CC0 et une revendication de domaine public ne sont pas interchangeables. Une revue vérifie le statut, l’autorité de la personne qui publie et les droits connexes éventuels.

## 16. Créations internes

Une création interne reçoit également une fiche. Le projet documente :

- la personne ou l’équipe créatrice ;
- le contexte de création ;
- les fichiers sources ;
- le contrat ou régime applicable ;
- les éléments tiers incorporés ;
- les outils, modèles et extensions utilisés ;
- l’autorité de publication ;
- les restrictions de confidentialité, d’attribution ou de portfolio.

Le simple fait qu’un fichier ait été créé sur un ordinateur du studio ne prouve pas que tous ses composants sont exploitables. Une police, un brush, une texture de référence, un sample ou un modèle IA peut introduire une dépendance distincte.

## 17. Commandes et prestataires

Avant la production, le bon de commande ou contrat décrit au minimum :

- livrables et formats sources ;
- auteurs et sous-traitants autorisés ;
- garanties de provenance ;
- droits transmis ou concédés ;
- usages, supports, versions, produits et modes de diffusion ;
- étendue territoriale et durée ;
- droit d’adaptation, de traduction et d’intégration ;
- autorisation ou interdiction de réutilisation et de portfolio ;
- règles relatives aux outils génératifs et aux datasets ;
- attribution ;
- confidentialité et données personnelles ;
- procédure de correction, retrait et remplacement ;
- conservation des sources et preuves.

Une facture prouve un paiement, pas nécessairement l’étendue des droits. Le projet relie donc facture, contrat, livrables, correspondance de clarification et décision de revue.

## 18. Assets achetés et services en ligne

Pour une boutique ou un service :

1. enregistrer le fournisseur et le compte acheteur ;
2. conserver la page de l’asset et la version des conditions ;
3. archiver le reçu ;
4. vérifier commercial, modification, nombre de sièges, redistribution et produits autorisés ;
5. vérifier les limitations par plateforme, moteur, chiffre d’affaires ou type de projet ;
6. vérifier l’usage dans un produit modifiable, un mod kit ou un Starter Kit ;
7. vérifier les droits sur les composants inclus ;
8. calculer l’empreinte de l’archive reçue ;
9. conserver une copie originale en lecture seule ;
10. attribuer un statut et un périmètre de publication.

`Royalty-free` ne signifie ni gratuit, ni libre, ni sans conditions, ni redistribuable comme source.

## 19. Assets ouverts, libres et domaine public

Le pipeline distingue :

- licence ouverte identifiée ;
- licence libre reconnue ;
- contenu gratuit sous conditions ;
- contenu sans licence visible ;
- œuvre annoncée comme domaine public ;
- reproduction numérique d’une œuvre ancienne ;
- données publiques soumises à des conditions propres.

L’absence de mention ne vaut pas autorisation. Une œuvre ancienne peut avoir des reproductions, traductions, restaurations, photographies, interprétations, éditions ou marques encore soumises à des droits.

## 20. Modèles IA, datasets et extensions

La chaîne IA contient plusieurs objets juridiques et techniques :

- code de l’application ;
- extensions ou custom nodes ;
- modèle ou architecture ;
- poids ;
- VAE, LoRA, embeddings et contrôles ;
- dataset déclaré ou documentation du fournisseur ;
- licence ou conditions du service ;
- entrées et références fournies par le projet ;
- prompts, paramètres, seeds et workflow ;
- sorties brutes ;
- sélection, correction et intégration humaines.

> **[VSC] Visual Studio Code — Créer : `art/provenance/ai/AI-CHAIN-MANIFEST.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
chain_id: "AST-AI-CHAIN-CONCEPT-001"
application:
  name: "ComfyUI"
  version: "0.28.0"
  licence_id: "GPL-3.0-only"
models:
  - asset_id: "AST-ASSET-MODEL-CONCEPT-001"
    file_sha256: null
    licence_id: "NOASSERTION"
    status: "blocked"
extensions: []
inputs:
  - asset_id: "AST-ASSET-CONCEPT-BRIEF-001"
    allowed_for_generation: "reviewed"
workflow:
  path: "../../../concept/workflows/AST-CONCEPT-001.json"
  sha256: null
outputs:
  - asset_id: "AST-ASSET-CONCEPT-GENERATED-001"
    status: "under_review"
human_review:
  selection: "pending"
  authorship_and_rights_review: "pending"
runtime_status: "not_executed"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Séparation :** application, modèles, extensions, entrées, workflow et sorties possèdent leurs propres statuts.
- **Blocage :** un modèle sans licence qualifiée bloque la chaîne, même lorsque l’application principale possède une licence connue.
- **Entrées :** `allowed_for_generation` ne se déduit pas du simple accès au fichier.
- **Réserve :** `runtime_status` empêche de présenter le manifeste documentaire comme une exécution réelle.

## 21. Sorties générées et contribution humaine

Le libellé `généré par IA` ne résout pas :

- les droits sur les entrées ;
- les conditions du modèle ou du service ;
- la similarité avec des œuvres ou personnes identifiables ;
- les marques et éléments protégés ;
- le niveau de contribution humaine ;
- la capacité à prouver la chaîne ;
- les règles du marché et des plateformes de distribution.

Chaque sortie conserve son workflow, les modèles, les paramètres, la seed, les entrées, la date, l’opérateur, les transformations et la décision humaine. Une sortie non sélectionnée peut être supprimée selon la politique de rétention, mais les sorties utilisées ou contestées gardent un paquet de preuves.

## 22. Entrées des systèmes génératifs

Une référence visuelle ne devient pas automatiquement une entrée autorisée. Le registre distingue :

- inspiration consultée sans ingestion ;
- référence interne autorisée ;
- photo ou scan capturé par le projet ;
- asset sous licence autorisant l’usage prévu ;
- contenu fourni avec consentement ;
- contenu inconnu ou interdit ;
- nom de personne, marque, franchise ou artiste vivant utilisé dans une instruction.

Les entrées `unknown`, `forbidden` ou `contested` ne passent pas la porte de génération de production.

## 23. Photos, textures, scans et photogrammétrie

Une capture réalisée par l’équipe peut encore contenir :

- une personne identifiable ;
- une œuvre exposée ;
- une propriété privée ;
- une marque ou un logo ;
- une plaque, une adresse ou une donnée personnelle ;
- un objet soumis à une restriction contractuelle ;
- un lieu dont l’accès ou la captation était conditionné.

La fiche de séance enregistre lieu, date, opérateur, matériel, autorisations, personnes, œuvres visibles, restrictions, fichiers bruts et empreintes. Les données brutes sensibles restent dans un stockage contrôlé et ne sont pas copiées dans un dépôt public.

## 24. Polices et typographies

La licence d’une police peut distinguer :

- usage sur poste de travail ;
- intégration dans une image rasterisée ;
- inclusion dans un document ;
- embarquement dans une application ;
- distribution du fichier de police ;
- modification ou création de sous-ensemble ;
- usage web ;
- nombre d’utilisateurs ;
- utilisation dans un logo ou une marque.

Le projet conserve le fichier de licence, l’origine, la version de la police et la liste des sorties qui l’embarquent. Une police installée sur Windows ne devient pas automatiquement distribuable avec le jeu.

## 25. Musiques, sons et enregistrements

Le registre sépare au minimum :

- composition ;
- paroles ;
- arrangement ;
- interprétation ;
- enregistrement maître ;
- samples ;
- bruitages individuels ;
- bibliothèque source ;
- montage final ;
- droits de synchronisation, reproduction et distribution selon le contexte.

Un seul fichier `.wav` peut donc dépendre de plusieurs titulaires et contrats. Les crédits et organismes de gestion éventuels restent enregistrés sans présumer qu’un paiement unique couvre toutes les exploitations.

## 26. Voix et artistes-interprètes

Pour une voix enregistrée, le projet demande une autorisation écrite adaptée à :

- la fixation de la prestation ;
- la reproduction ;
- la communication au public ;
- le montage et l’adaptation ;
- les langues et versions ;
- les plateformes et territoires ;
- la durée ;
- le nom ou pseudonyme ;
- les usages promotionnels ;
- la synthèse, le clonage, l’entraînement ou les transformations vocales, traités séparément ;
- la conservation et la sécurité des prises brutes ;
- la procédure en cas de retrait, litige ou remplacement.

> **[VSC] Visual Studio Code — Créer : `art/provenance/consent/VOICE-CONSENT-REGISTER.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
records:
  - consent_id: "AST-CONSENT-VOICE-001"
    performer_ref: "PERSON-RESTRICTED-001"
    asset_ids:
      - "AST-ASSET-VOICE-NARRATOR-001"
    signed_document: "restricted://contracts/voice/AST-CONSENT-VOICE-001.pdf"
    fixation: "granted"
    reproduction: "granted"
    public_communication: "granted"
    game_and_marketing: "granted"
    voice_cloning: "forbidden"
    model_training: "forbidden"
    territory: "contract_defined"
    duration: "contract_defined"
    status: "under_review"
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Confidentialité :** `performer_ref` évite de placer l’identité complète dans le registre général ; le document signé réside dans un stockage restreint.
- **Granularité :** clonage et entraînement sont séparés des usages classiques du jeu et du marketing.
- **Décision :** même avec plusieurs autorisations `granted`, le statut reste `under_review` tant que la revue globale n’est pas fermée.
- **Résultat attendu :** le build peut vérifier la présence d’un consentement sans exposer le contrat.

## 27. Image, visage, mocap et données personnelles

L’image et la voix d’une personne peuvent constituer des données personnelles lorsqu’elles permettent une identification directe ou indirecte. Les scans faciaux, données corporelles, enregistrements de mouvement et métadonnées de séance exigent donc une politique de minimisation, d’accès, de durée de conservation et de suppression adaptée.

Le projet distingue :

- autorisation de capture ;
- finalité du traitement ;
- exploitation artistique ;
- droits de l’interprète ;
- utilisation promotionnelle ;
- création de doublure numérique ;
- entraînement ou adaptation de modèle ;
- partage avec prestataires ;
- conservation des données brutes ;
- retrait de la livraison et traitement des sauvegardes.

Les mineurs, données sensibles, personnes vulnérables et usages biométriques reçoivent une revue renforcée.

## 28. Marques, logos et signes distinctifs

Une référence réaliste peut inclure une marque, un logo, un emballage, un uniforme, une interface, un produit ou une architecture commerciale identifiable. La revue vérifie :

- si l’élément est nécessaire ;
- s’il est présenté comme origine, partenariat ou approbation ;
- si une licence ou autorisation existe ;
- si le contexte crée un risque de confusion ;
- si une marque fictive ou un remplacement est préférable ;
- si la communication marketing modifie le risque ;
- si les magasins de distribution imposent des règles supplémentaires.

Le pipeline ne transforme pas cette checklist en conclusion juridique automatique. Tout doute significatif reste `blocked`.

## 29. Patrimoine, cultures et contenus sensibles

Une autorisation juridique minimale n’épuise pas les questions de représentation. Le registre peut demander :

- source culturelle ou historique ;
- communauté concernée ;
- caractère sacré, funéraire ou confidentiel ;
- restrictions de captation ou de reproduction ;
- contexte colonial ou de collecte ;
- personne consultée ;
- correction demandée ;
- règle d’attribution ou de partage ;
- décision éditoriale.

La revue culturelle ne remplace pas la revue juridique, et inversement.

## 30. Dépendances transitives

Un asset accepté devient bloqué lorsqu’une dépendance nécessaire ne l’est pas. La fiche déclare donc :

- textures ;
- polices ;
- samples ;
- rigs ;
- modèles IA ;
- plugins ;
- bibliothèques ;
- données de scan ;
- documents de consentement ;
- licences personnalisées.

> **[LECTURE] Graphe de décision — Ne pas saisir.**

```text
AST-ASSET-MESH-CHARACTER-001 [under_review]
├── AST-ASSET-TEX-SKIN-001 [accepted]
├── AST-ASSET-TEX-CLOTH-001 [blocked]
├── AST-ASSET-RIG-HUMAN-001 [accepted]
└── AST-ASSET-MODEL-FACE-001 [unknown]

Décision calculée : blocked
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Propagation :** une dépendance `blocked` ou `unknown` rend la livraison dépendante non publiable.
- **Lisibilité :** le graphe révèle la cause sans modifier les statuts sources.
- **Limite :** la décision calculée ne remplace pas une éventuelle exception humaine documentée, qui doit posséder un périmètre et une date d’expiration.
- **Résultat attendu :** une texture problématique peut être remplacée sans perdre la fiche du personnage ni son historique.

## 31. Contrôles automatiques minimaux

Le script suivant valide la structure des fiches, les statuts, les identifiants, les références et les dépendances. Il ne lit pas les contrats et ne prononce aucune conclusion juridique.

> **[VSC] Visual Studio Code — Créer : `tools/validate_asset_provenance.py` — Ne pas saisir.**

```python
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ASSET_ID = re.compile(
    r"^AST-ASSET-(CONCEPT|MESH|TEX|MAT|FONT|MUSIC|SFX|VOICE|MOCAP|MODEL|DATA|SCRIPT)-[A-Z0-9]+-[0-9]{3}$"
)
PUBLISHABLE = {"accepted", "accepted_limited"}
BLOCKING_DEPENDENCY = {"intake", "quarantined", "under_review", "blocked", "withdrawn", "superseded"}


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("La racine YAML doit être un objet.")
    return data


def validate_card(path: Path, data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    asset_id = data.get("asset_id")
    if not isinstance(asset_id, str) or ASSET_ID.fullmatch(asset_id) is None:
        errors.append(f"{path}: asset_id invalide")

    status = data.get("status")
    if not isinstance(status, str):
        errors.append(f"{path}: status absent")

    rights = data.get("rights")
    if not isinstance(rights, dict) or not rights.get("licence_id"):
        errors.append(f"{path}: rights.licence_id absent")

    review = data.get("review")
    if status in PUBLISHABLE:
        if not isinstance(review, dict) or review.get("human_decision") != "accepted":
            errors.append(f"{path}: statut publiable sans décision humaine acceptée")
        if not data.get("proof_sha256"):
            errors.append(f"{path}: statut publiable sans empreinte de preuve")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    args = parser.parse_args()

    cards: dict[str, dict[str, Any]] = {}
    errors: list[str] = []
    for path in sorted(args.root.glob("*.yaml")):
        try:
            data = load_yaml(path)
        except (OSError, UnicodeError, yaml.YAMLError, ValueError) as exc:
            errors.append(f"{path}: lecture impossible: {exc}")
            continue
        errors.extend(validate_card(path, data))
        asset_id = data.get("asset_id")
        if isinstance(asset_id, str):
            if asset_id in cards:
                errors.append(f"{path}: asset_id dupliqué: {asset_id}")
            cards[asset_id] = data

    for asset_id, card in cards.items():
        for dependency in card.get("dependencies", []):
            target = cards.get(dependency)
            if target is None:
                errors.append(f"{asset_id}: dépendance absente: {dependency}")
            elif card.get("status") in PUBLISHABLE and target.get("status") in BLOCKING_DEPENDENCY:
                errors.append(
                    f"{asset_id}: dépendance non publiable: {dependency} ({target.get('status')})"
                )

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1

    print(f"Fiches valides: {len(cards)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Entrées :** le script reçoit un dossier contenant des fiches YAML et charge chaque objet avec `safe_load`.
- **Contrôles :** il vérifie l’identifiant, le statut, la licence, la décision humaine, l’empreinte de preuve et les dépendances.
- **Codes de retour :** `0` signifie que les contrôles structurels réussissent ; `1` indique au moins une non-conformité.
- **Refus contrôlé :** une fiche publiable sans décision humaine ou preuve est rejetée.
- **Limite :** le script ne détermine pas si une licence, une cession ou un consentement est juridiquement suffisant.

> **[PS] PowerShell 7 — Exécuter le validateur depuis la racine du dépôt.**

```powershell
python tools/validate_asset_provenance.py art/provenance/assets
if ($LASTEXITCODE -ne 0) {
  throw "Le registre de provenance ne franchit pas les contrôles structurels."
}
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Paramètre :** le dossier transmis doit contenir uniquement les fiches individuelles attendues par le validateur.
- **Valeur de retour :** PowerShell lit le code du script dans `$LASTEXITCODE`.
- **Effet de bord :** la commande ne modifie aucune fiche ; elle produit seulement des diagnostics.
- **Résultat attendu :** la chaîne de livraison s’arrête avant publication lorsqu’une preuve ou une dépendance structurelle manque.

## 32. Règles de blocage

Un asset reste `blocked` lorsque l’un des points suivants est vrai :

- source inconnue ;
- auteur ou titulaire non identifiable lorsque nécessaire ;
- texte de licence absent ;
- conditions contradictoires ;
- usage commercial inconnu ;
- modification interdite alors que le pipeline transforme l’asset ;
- redistribution incompatible avec la livraison ;
- attribution impossible à respecter ;
- territoire ou durée insuffisants ;
- consentement absent ou hors périmètre ;
- dépendance bloquée ;
- modèle IA, dataset ou entrée non qualifié ;
- contestation active ;
- document de preuve altéré ou non relié à l’asset ;
- exception humaine expirée.

Un asset `accepted_limited` exige un contrôle de périmètre à chaque build concerné.

## 33. Porte de publication

> **[VSC] Visual Studio Code — Créer : `art/provenance/PUBLISH-GATE.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
required_for_publish:
  - stable_asset_id
  - immutable_version
  - source_recorded
  - creator_or_provider_recorded
  - licence_or_contract_recorded
  - restrictions_visible
  - transformation_chain_recorded
  - dependencies_resolved
  - automated_checks_passed
  - human_decision_accepted
  - proof_package_hashed
conditional_checks:
  personal_data:
    - lawful_basis_or_documented_authority
    - minimisation
    - restricted_storage
    - retention_defined
  performance_or_voice:
    - written_authorisation
    - permitted_uses
    - territory
    - duration
  generated:
    - model_chain_qualified
    - inputs_qualified
    - workflow_recorded
    - similarity_reviewed
refuse_statuses:
  - intake
  - quarantined
  - under_review
  - blocked
  - withdrawn
  - superseded
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Préconditions :** la liste commune s’applique à tous les assets, puis des contrôles conditionnels complètent la porte.
- **Décision humaine :** la présence d’une revue acceptée reste obligatoire après les contrôles automatiques.
- **Refus :** les statuts non publiables sont explicitement listés afin d’éviter une valeur par défaut permissive.
- **Résultat attendu :** le pipeline de build peut appliquer une politique déterministe sans lire de données personnelles sensibles.

## 34. Procédure de retrait et remplacement

Lorsqu’un asset est contesté ou devient incompatible :

1. ouvrir un incident et geler les nouvelles publications ;
2. identifier toutes les versions, dépendances, scènes, builds et supports marketing concernés ;
3. conserver les preuves et communications dans un espace restreint ;
4. passer l’asset à `blocked` ou `withdrawn` ;
5. désigner un responsable ;
6. décider suppression, remplacement, nouvelle licence ou limitation de périmètre ;
7. produire un asset de remplacement avec une nouvelle fiche ;
8. relier `replacement_asset_id` et `replaces_asset_id` ;
9. reconstruire les livraisons concernées ;
10. vérifier les caches, CDN, stores, sauvegardes et branches ;
11. enregistrer ce qui ne peut pas être retiré immédiatement et pourquoi ;
12. clore l’incident sans effacer l’historique.

> **[VSC] Visual Studio Code — Créer : `art/provenance/incidents/INC-ASSET-0001.yaml` — Ne pas saisir.**

```yaml
schema_version: 1
incident_id: "INC-ASSET-0001"
opened_on: "2026-07-22T23:00:00+02:00"
asset_id: "AST-ASSET-TEX-STONEWALL-001"
status: "open"
trigger: "licence_scope_contested"
publication_hold: true
affected:
  asset_versions: ["v001"]
  builds: []
  marketing: []
decision:
  action: "replace"
  replacement_asset_id: "AST-ASSET-TEX-STONEWALL-002"
  approver: null
  decided_on: null
retention:
  evidence_preserved: true
  public_source_removed: false
closure:
  completed_on: null
  notes: null
```

<!-- qa:code-explanation -->

**Explication structurée du bloc :**

- **Gel :** `publication_hold` empêche une nouvelle diffusion pendant l’analyse.
- **Portée :** `affected` sépare les assets, builds et contenus marketing à corriger.
- **Remplacement :** l’identifiant du nouvel asset ne modifie pas l’identité de l’élément contesté.
- **Conservation :** la preuve reste préservée même lorsque la source publique disparaît.
- **Résultat attendu :** l’incident peut être audité et repris sans reconstituer les faits depuis la mémoire d’une personne.

## 35. Conservation et accès aux preuves

La politique de rétention distingue :

- fichiers publics de licence ;
- contrats confidentiels ;
- données personnelles ;
- captures et enregistrements bruts ;
- factures et informations financières ;
- sorties générées non retenues ;
- preuves d’assets publiés ;
- preuves d’incidents et contestations ;
- sauvegardes et journaux techniques.

Les durées sont définies par finalité et obligation, pas par une valeur universelle. Les droits d’accès suivent le principe du besoin d’en connaître. Le registre général conserve des références opaques vers les documents restreints.

Les empreintes prouvent l’identité d’un fichier conservé, pas sa validité juridique ni l’identité de son signataire. Une signature électronique ou une chaîne de conservation peut être nécessaire selon le risque.

## 36. Mode Solo

Le parcours Solo maintient une fiche légère pour chaque source externe, générée ou capturée. Il conserve au minimum :

- identifiant ;
- origine ;
- lien ou fournisseur ;
- licence ou contrat ;
- auteur ou compte source ;
- date d’acquisition ;
- restrictions majeures ;
- transformations ;
- dépendances ;
- statut ;
- paquet de preuves.

Le créateur Solo ne remplace pas la revue par sa mémoire. Les éléments inconnus sont retirés ou remplacés avant publication. Une consultation professionnelle est réservée aux enjeux significatifs : voix, personnes, marques, contrats personnalisés, contenus culturels sensibles, diffusion importante ou contestation.

## 37. Mode Studio

Le parcours Studio ajoute :

- registre central ;
- propriétaires et responsables de revue ;
- séparation des rôles entre acquisition, création, validation et publication ;
- stockage restreint des contrats et données personnelles ;
- modèles contractuels validés ;
- revue juridique ou responsable désigné ;
- exceptions datées et approuvées ;
- contrôles CI des fiches et dépendances ;
- inventaire des modèles IA et services ;
- procédure d’incident ;
- audit périodique ;
- export de notices, crédits et attributions ;
- interdiction de publier un statut implicite.

## 38. Mesures à consigner

Le projet mesure :

- nombre d’assets par catégorie et statut ;
- fiches incomplètes ;
- licences personnalisées ;
- assets avec données personnelles ;
- consentements arrivant à échéance ;
- dépendances bloquées ;
- exceptions actives ;
- délais de revue ;
- retraits et remplacements ;
- builds contenant des assets `accepted_limited` ;
- modèles IA et services non requalifiés après changement de conditions ;
- écarts entre registre et fichiers livrés.

Ces mesures servent à prioriser le travail. Elles ne deviennent pas un score juridique automatique.

## 39. Sécurité et confidentialité

Les contrats, reçus, données personnelles et preuves peuvent contenir noms, adresses, signatures, coordonnées bancaires, voix, images ou informations commerciales. Les règles minimales sont :

- ne pas committer de secrets ou documents sensibles dans un dépôt public ;
- utiliser des références opaques ;
- chiffrer les stockages adaptés ;
- limiter les accès ;
- journaliser les consultations sensibles lorsque nécessaire ;
- vérifier les pièces jointes et archives avant ouverture ;
- désactiver les scripts automatiques de formats non qualifiés ;
- minimiser les données ;
- définir rétention, sauvegarde et suppression ;
- traiter les demandes et incidents selon la procédure du projet.

## 40. Erreurs fréquentes et corrections

<!-- qa:error-correction-section -->

### 40.1 Considérer qu’un asset gratuit est libre

**Symptôme :** le fichier est intégré sans licence parce que son prix était nul.

**Exemple fautif**

> **[LECTURE] Fiche fautive — Ne pas saisir.**

```yaml
asset_id: "AST-ASSET-TEX-FOREST-001"
price: 0
status: "accepted"
licence_id: null
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le prix ne décrit ni l’autorisation commerciale, ni la modification, ni la redistribution, ni l’attribution.

**Exemple corrigé**

> **[LECTURE] Fiche corrigée — Ne pas saisir.**

```yaml
asset_id: "AST-ASSET-TEX-FOREST-001"
category: "open-licensed"
status: "under_review"
licence_id: "CC-BY-4.0"
proof_ref: "evidence/AST-ASSET-TEX-FOREST-001/"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la licence exacte et la preuve sont enregistrées, tandis que la revue reste ouverte avant publication.

### 40.2 Déduire les droits d’une facture

**Symptôme :** un prestataire a été payé et le studio suppose posséder tous les droits mondiaux et perpétuels.

**Exemple fautif**

> **[LECTURE] Décision fautive — Ne pas saisir.**

```text
Facture payée = tous droits acquis
Contrat détaillé = absent
Territoire et durée = non vérifiés
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le paiement prouve une transaction, pas le contenu précis d’une licence ou d’une cession.

**Exemple corrigé**

> **[LECTURE] Décision corrigée — Ne pas saisir.**

```text
Facture = preuve de paiement
Contrat écrit = droits, usages, territoire et durée
Fiche d’asset = lien vers contrat et décision de revue
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** chaque document conserve son rôle et la portée des droits peut être vérifiée séparément.

### 40.3 Utiliser `royalty-free` comme licence

**Symptôme :** le registre contient seulement `royalty-free`.

**Exemple fautif**

> **[LECTURE] Champ fautif — Ne pas saisir.**

```yaml
licence_id: "royalty-free"
redistribution_source: "allowed"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** le terme ne fournit ni texte contractuel ni autorisation de redistribuer les sources.

**Exemple corrigé**

> **[LECTURE] Champ corrigé — Ne pas saisir.**

```yaml
licence_id: "LicenseRef-MARKETPLACE-PRO-2026"
licence_text: "evidence/licence.txt"
redistribution_source: "forbidden"
redistribution_embedded: "reviewed"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** un identifiant local pointe vers le texte applicable et sépare les formes de redistribution.

### 40.4 Fusionner auteur, fournisseur et titulaire

**Symptôme :** le nom de la boutique est enregistré comme auteur et propriétaire de tous les droits.

**Exemple fautif**

> **[LECTURE] Attribution fautive — Ne pas saisir.**

```yaml
creator: "Marketplace X"
rights_holder: "Marketplace X"
provider: "Marketplace X"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** une plateforme peut distribuer un asset sans en être l’auteur ni le titulaire de tous les droits.

**Exemple corrigé**

> **[LECTURE] Attribution corrigée — Ne pas saisir.**

```yaml
provider: "Marketplace X"
creators:
  - name: "Studio Y"
    role: "author_claimed_by_listing"
rights_holder: "review_against_contract"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les rôles restent distincts et l’incertitude est visible jusqu’à la lecture du contrat.

### 40.5 Considérer une sortie IA comme libre de droits

**Symptôme :** la sortie est publiée sans enregistrer modèle, entrées ou conditions du service.

**Exemple fautif**

> **[LECTURE] Manifeste fautif — Ne pas saisir.**

```yaml
origin_type: "generated"
licence_id: "none_needed"
inputs: []
model: null
status: "accepted"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la génération ne supprime pas les questions relatives aux entrées, modèles, conditions, personnes, marques ou similarités.

**Exemple corrigé**

> **[LECTURE] Manifeste corrigé — Ne pas saisir.**

```yaml
origin_type: "generated"
model_chain: "ai/AI-CHAIN-MANIFEST.yaml"
inputs:
  - "AST-ASSET-CONCEPT-BRIEF-001"
workflow_sha256: "REPLACE_WITH_REAL_SHA256"
status: "under_review"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la chaîne générative est traçable et la décision humaine n’est pas anticipée.

### 40.6 Autoriser une voix sans traiter le clonage

**Symptôme :** une autorisation générale d’enregistrement est interprétée comme permission d’entraîner un modèle vocal.

**Exemple fautif**

> **[LECTURE] Consentement fautif — Ne pas saisir.**

```yaml
recording: "granted"
voice_cloning: "assumed"
model_training: "assumed"
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** des usages substantiellement différents sont déduits d’une autorisation générique.

**Exemple corrigé**

> **[LECTURE] Consentement corrigé — Ne pas saisir.**

```yaml
recording: "granted"
game_use: "granted"
voice_cloning: "forbidden"
model_training: "forbidden"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** chaque usage sensible possède une décision explicite et vérifiable.

### 40.7 Effacer un asset contesté et ses preuves

**Symptôme :** l’équipe supprime tous les fichiers pour faire disparaître le problème.

**Exemple fautif**

> **[LECTURE] Retrait fautif — Ne pas saisir.**

```text
Supprimer la fiche
Supprimer les reçus et contrats
Réutiliser le même identifiant pour le remplacement
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** l’historique, la portée des builds concernés et la justification du remplacement deviennent impossibles à établir.

**Exemple corrigé**

> **[LECTURE] Retrait corrigé — Ne pas saisir.**

```text
Passer l’asset à withdrawn
Conserver les preuves sous accès restreint
Créer un nouvel identifiant de remplacement
Relier incident, ancien asset et nouvel asset
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la livraison est corrigée sans détruire la traçabilité nécessaire à l’audit.

### 40.8 Oublier les dépendances transitives

**Symptôme :** un modèle 3D est accepté alors qu’une texture requise reste sans licence.

**Exemple fautif**

> **[LECTURE] Dépendance fautive — Ne pas saisir.**

```yaml
asset_id: "AST-ASSET-MESH-HOUSE-001"
status: "accepted"
dependencies: []
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** la fiche présente l’asset comme autonome alors que son rendu dépend d’éléments non déclarés.

**Exemple corrigé**

> **[LECTURE] Dépendance corrigée — Ne pas saisir.**

```yaml
asset_id: "AST-ASSET-MESH-HOUSE-001"
status: "blocked"
dependencies:
  - "AST-ASSET-TEX-WOOD-001"
  - "AST-ASSET-TEX-ROOF-001"
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les causes du blocage sont explicites et peuvent être remplacées séparément.

### 40.9 Stocker un contrat personnel dans un dépôt public

**Symptôme :** signatures, adresses et rémunérations sont committées avec le jeu.

**Exemple fautif**

> **[LECTURE] Stockage fautif — Ne pas saisir.**

```text
repo-public/art/contracts/voice_actor_signed.pdf
repo-public/art/consent/passport-scan.jpg
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** des données personnelles et contractuelles sensibles deviennent accessibles au-delà du besoin de production.

**Exemple corrigé**

> **[LECTURE] Stockage corrigé — Ne pas saisir.**

```text
Registre public : restricted://contracts/voice/AST-CONSENT-VOICE-001.pdf
Stockage restreint : document chiffré et accès limité
Dépôt : identifiant, statut et empreinte seulement
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** la production peut vérifier l’existence et l’identité de la preuve sans exposer son contenu sensible.

### 40.10 Remplacer une licence sans nouvelle revue

**Symptôme :** les conditions d’un fournisseur changent et l’équipe écrase le champ de licence existant.

**Exemple fautif**

> **[LECTURE] Historique fautif — Ne pas saisir.**

```yaml
version: "v001"
licence_id: "LicenseRef-NEW-TERMS"
previous_terms: null
```

<!-- qa:code-explanation -->

**Pourquoi cet exemple est fautif :** l’équipe ne peut plus déterminer quelles conditions s’appliquaient lors d’un ancien build ou d’une acquisition antérieure.

**Exemple corrigé**

> **[LECTURE] Historique corrigé — Ne pas saisir.**

```yaml
version: "v002"
licence_id: "LicenseRef-NEW-TERMS"
previous_version: "v001"
requalification_required: true
acquisition_basis_preserved: true
```

<!-- qa:code-explanation -->

**Pourquoi la correction fonctionne :** les conditions anciennes restent reliées aux livraisons antérieures et la nouvelle version repasse par la porte de revue.

## 41. Critères d’acceptation

Le chapitre est appliqué lorsque :

- chaque asset publié possède un identifiant stable et une version immuable ;
- la source, l’auteur ou le fournisseur et la date d’acquisition sont enregistrés ;
- le texte de licence, contrat ou consentement est conservé ;
- commercial, modification, redistribution, attribution, territoire et durée sont visibles ;
- les chaînes IA séparent modèles, poids, code, extensions, entrées, workflow et sorties ;
- les personnes, voix, scans et interprétations possèdent les autorisations adaptées ;
- les données sensibles utilisent un stockage restreint ;
- les transformations et dépendances sont traçables ;
- l’automatisation refuse les fiches structurellement incomplètes ;
- une décision humaine ferme chaque publication ;
- un asset contesté peut être retiré et remplacé sans perdre l’historique ;
- aucune conclusion juridique personnalisée n’est déduite du guide.

## 42. Livrables permanents

Les livrables du chapitre sont :

- registre central de provenance ;
- modèle de fiche d’asset ;
- matrice des licences et restrictions ;
- manifeste de chaîne de transformations ;
- registre des consentements ;
- politique de statuts et blocages ;
- porte de publication ;
- validateur structurel proposé ;
- procédure de retrait et remplacement ;
- modèle d’incident ;
- politique de conservation et d’accès.

## 43. Synthèse opérationnelle pour Project Asteria

`Project Asteria` ne publie aucun asset sur la base d’un nom de fichier, d’un prix nul, d’un achat, d’une commande ou d’une génération. Chaque élément reçoit une identité stable, une fiche, un statut, une chaîne de transformations, des dépendances et un paquet de preuves.

Les licences ouvertes utilisent un identifiant exact lorsque possible ; les contrats, boutiques et consentements utilisent `LicenseRef-...`. Les restrictions de commercialisation, modification, attribution, redistribution, territoire, durée, sous-licence, entraînement et clonage restent séparées.

Les modèles IA, datasets, custom nodes, entrées, workflows et sorties sont qualifiés individuellement. Les voix, images, interprétations, scans et captures de mouvement utilisent des registres restreints et des autorisations explicites selon l’usage.

La CI contrôle la structure et la cohérence, mais la publication exige une décision humaine. Les statuts inconnus ou contestés bloquent la livraison. Un retrait conserve la preuve, relie les builds concernés et crée un remplacement versionné.

À ce stade, les modèles de fichiers et scripts sont documentaires. Aucun registre réel, contrat, consentement, asset, paquet de preuves ou contrôle runtime de `Project Asteria` n’est revendiqué comme matérialisé.

## 44. Références institutionnelles et standards vérifiés

- [Légifrance — Code de la propriété intellectuelle, droit d’auteur](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069414/LEGISCTA000006133323/)
- [Légifrance — dispositions générales relatives à l’exploitation des droits](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069414/LEGISCTA000006161639/)
- [Légifrance — droits des artistes-interprètes](https://www.legifrance.gouv.fr/codes/id/LEGIARTI000006279034/2026-05-15)
- [Légifrance — Code civil, article 9](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006419288/)
- [CNIL — définition d’une donnée personnelle](https://www.cnil.fr/fr/definition/donnee-personnelle)
- [SPDX — License List](https://spdx.org/licenses/)
- [Creative Commons — licences et conditions](https://creativecommons.org/share-your-work/use-remix/cc-licenses/)
- [Creative Commons — considérations avant d’appliquer ou réutiliser une licence](https://creativecommons.org/share-your-work/licensing-considerations/version4/)
- [OMPI — licences de droit d’auteur dans l’environnement numérique](https://www.wipo.int/en/web/copyright/activities/copyright_licensing)
- [Commission européenne — cadre européen de l’intelligence artificielle](https://commission.europa.eu/topics/artificial-intelligence_en)
