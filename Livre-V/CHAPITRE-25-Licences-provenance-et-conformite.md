---
title: "Livre V — Fiche 25 : Licences, provenance et conformité"
id: "DOC-L5-CH25"
status: "reviewed"
version: "1.0.0"
lang: "fr-FR"
book: "Livre V"
chapter: 25
last-verified: "2026-07-30T00:17:00+02:00"
audit-status: "complete"
audit-date: "2026-07-30T00:17:00+02:00"
audit-report: "Livre-V/QA/AUDIT-CHAPITRE-25.md"
audit-level: "static-review"
document-format: "reference-cards"
reference-scope: "licenses-provenance-consent-redistribution-attribution-regulatory-routing-and-compliance-decisions"
reference-jurisdiction:
  production-base: "France"
  market-context: "European Union"
  verification-date: "2026-07-30"
usage-context-standard: "DOC-V0-ANN-CONTEXTES"
---

# Licences, provenance et conformité

> **Type de document :** cartes de qualification, matrices de droits et obligations, registres de provenance, routage réglementaire et portes de publication.
> **Lecture :** identifier l’objet exact, retrouver le texte applicable et sa preuve, qualifier l’usage prévu, puis enregistrer une décision limitée au périmètre examiné.
> **Principe :** une licence connue n’autorise pas automatiquement tous les usages ; une provenance connue ne prouve pas tous les droits ; une checklist réussie ne constitue pas un avis juridique.

## Règles de lecture

| Règle | Conséquence |
|---|---|
| un objet juridique par ligne | code, poids, dataset, asset, prestation, sortie et service ne partagent pas automatiquement le même régime |
| le texte applicable prévaut sur le surnom | `open`, `free`, `royalty-free` ou `commercial-friendly` ne suffisent pas |
| l’usage prévu fait partie de la décision | utiliser, modifier, entraîner, intégrer, redistribuer et publier sont des opérations distinctes |
| l’inconnu reste bloquant | `unknown` ou `NOASSERTION` ne devient jamais `allowed` par défaut |
| la preuve reste consultable | page, fichier, contrat, consentement, reçu, archive et empreinte sont reliés au registre |
| la décision est bornée | produit, version, canal, territoire, durée, public et restrictions restent visibles |
| l’automatisation contrôle la structure | elle ne lit pas un contrat à la place d’une personne compétente |
| la réglementation est routée | la fiche signale une revue nécessaire sans conclure seule à l’applicabilité ou à la conformité |

**Réponse rapide :** la politique détaillée des assets appartient au [Livre III, chapitre 5](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#1-rôle-du-chapitre). La [production et publication](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#8-validation-juridique-et-des-licences) impose une revue avant diffusion ; la présente fiche fournit la vue transversale de consultation.

## Index express

| Besoin | Ouvrir |
|---|---|
| qualifier un objet et un usage | [LIC-00](#lic-00--contrat-de-qualification) |
| séparer les couches juridiques | [Matrice A](#matrice-a--objets-couches-et-propriétaires) |
| inventorier une dépendance ou un asset | [LIC-01](#lic-01--identité-inventaire-et-périmètre) |
| enregistrer SPDX, `LicenseRef` et expressions | [LIC-02](#lic-02--texte-identifiant-et-expression-de-licence) |
| lire droits, obligations et restrictions | [Matrice B](#matrice-b--droits-obligations-et-questions-bloquantes) |
| router code, contenu, modèles et services | [LIC-03](#lic-03--familles-dobjets-et-sources-propriétaires) |
| conserver provenance et preuves | [LIC-04](#lic-04--chaîne-de-provenance-et-paquet-de-preuves) |
| traiter voix, image et données personnelles | [LIC-05](#lic-05--personnes-consentements-et-données) |
| qualifier une chaîne IA | [LIC-06](#lic-06--modèles-datasets-entrées-sorties-et-services-ia) |
| vérifier redistribution et compatibilité | [LIC-07](#lic-07--redistribution-compatibilité-et-dépendances-transitives) |
| savoir quelle décision est permise | [Matrice C](#matrice-c--statuts-décisions-et-déclarations-permises) |
| produire notices, crédits et offres de source | [LIC-08](#lic-08--notices-attributions-sbom-et-paquet-de-publication) |
| adapter le registre en Solo ou Studio | [LIC-09](#lic-09--gouvernance-solo-studio-et-séparation-des-rôles) |
| escalader vers un avis professionnel | [LIC-10](#lic-10--revue-réglementaire-exceptions-et-escalade) |
| retirer ou requalifier un objet | [LIC-11](#lic-11--changements-expiration-incidents-et-retrait) |
| décider la licence globale de la collection | [LIC-12](#lic-12--licence-de-collection-frontières-et-sources-officielles) |

---

<!-- l5:card -->
## LIC-00 — Contrat de qualification

| Champ | Règle |
|---|---|
| identité | objet, version, fichier, composant logique ou prestation clairement identifié |
| catégorie | code, documentation, modèle, poids, adaptation, dataset, asset, audio, police, service, personne ou sortie |
| source | auteur, titulaire, fournisseur, dépôt, boutique, séance, service ou chaîne générative |
| texte applicable | licence, contrat, conditions, consentement, politique ou acte archivé |
| identifiant | SPDX lorsque le texte correspond, sinon `LicenseRef-...` stable |
| opération | consulter, exécuter, modifier, entraîner, intégrer, distribuer, sous-licencier, promouvoir ou archiver |
| périmètre | produit, version, canal, plateforme, territoire, durée, public et environnement |
| droits | autorisations nécessaires pour l’opération exacte |
| obligations | attribution, notice, partage à l’identique, offre de source, marquage, information ou conservation |
| restrictions | commercial, redistribution source, dérivés, personnes, marques, IA, territoire ou plateforme |
| dépendances | composants dont le statut conditionne la décision |
| preuve | texte, capture datée, reçu, contrat, consentement, manifeste, hash et décision |
| propriétaire | rôle qui maintient la fiche et répond aux changements |
| approbateur | rôle autorisé à accepter le périmètre ou à demander une revue spécialisée |
| statut | état courant séparé de la licence déclarée |
| expiration | date, version, changement de conditions, retrait, incident ou nouvelle diffusion |
| réserves | limites connues et questions non résolues |
| décision | usage autorisé, limité, bloqué, retiré ou à requalifier dans le périmètre nommé |

**Réponse rapide :** la [fiche d’asset](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#8-fiche-dasset-obligatoire) et le [registre central](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#9-registre-central-de-provenance) fournissent les détails de production. Le contrat ci-dessus s’applique aussi au code, aux modèles, aux données, aux services et à la documentation.

**Diagramme compact :** `objet exact → texte applicable → opération prévue → droits + obligations + restrictions → preuves → décision bornée`.

**Niveau de preuve :** `static-review`. Aucun objet réel de la collection ou de `Project Asteria` n’est qualifié par cette fiche.

---

<!-- l5:matrix -->
## Matrice A — Objets, couches et propriétaires

| Objet | Couches à distinguer | Source propriétaire |
|---|---|---|
| dépôt et scripts | copyright, licence du projet, dépendances, notices, contributions | [Index des licences](../Volume-0/annexes/INDEX-LICENCES.md#catégories-du-registre) et [sécurité de production](../Livre-II/CHAPITRE-13-Securite-et-separation-entre-production-et-runtime-de-l-IA.md) |
| documentation | texte, schémas, captures, extraits, marques, polices, médias | [Validation juridique](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#8-validation-juridique-et-des-licences) |
| asset artistique | source, auteur, titulaire, licence, transformations, dépendances | [Provenance des assets](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#12-carte-des-droits-et-autorisations) |
| musique et son | composition, paroles, arrangement, interprétation, master, samples, synchronisation | [Musiques et enregistrements](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#25-musiques-sons-et-enregistrements) |
| voix, visage et mocap | capture, prestation, exploitation, image, données, clonage, entraînement | [Voix](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#26-voix-et-artistes-interprètes) et [données personnelles](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#27-image-visage-mocap-et-données-personnelles) |
| chaîne IA | application, extension, architecture, poids, adaptation, dataset, entrées, sorties, service | [Modèles IA et datasets](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#20-modèles-ia-datasets-et-extensions) |
| package et build | fichiers inclus, licences, notices, source requise, manifestes et signatures | [Exports et packaging](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md#6-distinguer-export-packaging-et-publication) |
| page et canal | déclarations, médias, classification, territoires, conditions de plateforme | [Publication et distribution](../Livre-IV/CHAPITRE-17-Publication-et-distribution.md#1-rôle-du-chapitre) |
| mod et contenu communautaire | API, code exécutable, asset, attribution, consentement, modération et retrait | [Modding et contenu communautaire](../Livre-IV/CHAPITRE-21-Modding-et-contenu-communautaire.md) |
| archive | licences, droits de redistribution, preuves, secrets, formats et succession | [Maintenance et archivage](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md#4-modèle-mental-conserver-un-système-pas-seulement-un-zip) |

**Décision :** une couche validée ne ferme pas les autres. Un code sous licence connue peut charger des poids, données, polices ou sons dont les droits restent indépendants.

---

<!-- l5:card -->
## LIC-01 — Identité, inventaire et périmètre

| Question | Réponse attendue |
|---|---|
| qu’est-ce qui est qualifié ? | objet logique et octets exacts, avec version ou empreinte |
| où vient-il ? | source officielle, auteur, titulaire, fournisseur ou séance |
| comment est-il entré ? | création, commande, achat, téléchargement, contribution, capture ou génération |
| où est le texte ? | fichier de licence, contrat, conditions archivées ou consentement |
| pour quel usage ? | opération et produit précis, pas « usage général » |
| dans quelle livraison ? | build, archive, dépôt, document, page ou Companion Pack |
| pour qui et où ? | public, territoire, plateforme et canal |
| jusqu’à quand ? | durée, date de revue ou événement d’expiration |
| avec quoi ? | dépendances directes et transitives |
| qui décide ? | propriétaire, relecteur et approbateur nommés |

**Méthode :** le registre utilise un identifiant stable indépendant du nom de fichier. Chaque nouvelle licence, version de conditions, source substantiellement différente ou périmètre de publication peut exiger une nouvelle révision.

**Réponse rapide :** la [typologie des assets](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#5-typologie-des-assets) classe l’origine sans accorder de droit. L’[index des licences](../Volume-0/annexes/INDEX-LICENCES.md#fiche-de-licence) fournit une fiche minimale à étendre.

**Diagramme compact :** `inventaire de fichiers → regroupement en objets → versions et empreintes → usages prévus → dépendances → registre de qualification`.

**Limite :** l’inventaire prouve ce qui a été déclaré et scanné ; il ne garantit pas l’absence de composant incorporé, de sample, de police ou de code généré non déclaré.

---

<!-- l5:card -->
## LIC-02 — Texte, identifiant et expression de licence

| Valeur | Usage |
|---|---|
| identifiant SPDX | texte correspondant à une entrée de la liste SPDX |
| expression SPDX | combinaison formelle avec `AND`, `OR` et `WITH` |
| `LicenseRef-...` | licence personnalisée, contrat, conditions de boutique ou consentement non représenté par SPDX |
| `NOASSERTION` | impossibilité documentée de conclure ; jamais une autorisation |
| fichier `LICENSE` ou `COPYING` | texte livré par le composant, à conserver avec sa version |
| notice ou en-tête | attribution et informations par fichier ou groupe de fichiers |
| capture de conditions | preuve complémentaire datée, pas substitut au texte applicable |
| référence de contrat | pointeur opaque vers un stockage protégé |

**Règles :**

- comparer le texte réellement reçu, pas seulement le nom affiché ;
- conserver la version exacte et la date de récupération ;
- ne pas appliquer un identifiant SPDX à un texte modifié sans vérifier la correspondance ;
- ne pas transformer `OR` en préférence interne après distribution ;
- ne pas utiliser `AND` lorsque le projet voulait exprimer une alternative ;
- relier chaque `LicenseRef` à son texte ou à une référence de preuve ;
- distinguer l’identifiant de licence de la décision de compatibilité avec le projet.

**Réponse rapide :** les [identifiants SPDX et licences personnalisées](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#14-identifiants-spdx-et-licences-personnalisées) montrent la syntaxe. La spécification officielle [SPDX 3.0](https://spdx.dev/use/specifications/) et la [SPDX License List](https://spdx.org/licenses/) sont les autorités de format vérifiées le 30 juillet 2026.

**Diagramme compact :** `nom annoncé ≠ texte applicable → texte archivé → identifiant ou LicenseRef → expression → obligations calculables → revue humaine`.

**Limite :** SPDX standardise des déclarations ; il ne rend pas deux licences compatibles et ne décide pas si une œuvre ou un modèle peut recevoir la licence déclarée.

---

<!-- l5:matrix -->
## Matrice B — Droits, obligations et questions bloquantes

| Axe | Valeurs de registre | Question avant décision |
|---|---|---|
| exécution ou consultation | `allowed`, `conditional`, `forbidden`, `unknown` | l’usage interne ou runtime est-il couvert ? |
| modification ou adaptation | mêmes valeurs | le pipeline retouche-t-il, traduit-il, fine-tune-t-il ou convertit-il ? |
| intégration | mêmes valeurs | l’objet est-il incorporé, lié, embarqué ou seulement appelé ? |
| redistribution source | mêmes valeurs | les octets sources sont-ils remis tels quels ou modifiés ? |
| redistribution intégrée | mêmes valeurs | l’objet est-il seulement inclus dans un produit fermé ou transformé ? |
| usage commercial | mêmes valeurs | le produit, la promotion, le financement ou le service relève-t-il du périmètre autorisé ? |
| attribution | `required`, `optional`, `forbidden_claim`, `unknown` | où, comment et sous quel nom le crédit doit-il apparaître ? |
| partage à l’identique | `required`, `not_required`, `unknown` | quelle partie dérivée ou adaptée reçoit les mêmes termes ? |
| source et notices | `required`, `not_required`, `conditional`, `unknown` | faut-il fournir texte, code source, modifications ou offre écrite ? |
| sous-licence | `allowed`, `conditional`, `forbidden`, `unknown` | le distributeur ou l’utilisateur final reçoit-il des droits supplémentaires ? |
| territoire et durée | valeurs exactes ou `unknown` | le canal et la période de diffusion sont-ils couverts ? |
| données et personnes | base, finalité, consentement ou autre autorité documentée | la conservation et l’exploitation artistique sont-elles séparées ? |
| entraînement et génération | `allowed`, `conditional`, `forbidden`, `unknown` | entrée, modèle, adaptation, sortie et service ont-ils chacun une base ? |
| marques et approbation | `cleared`, `limited`, `blocked`, `unknown` | l’usage crée-t-il une confusion ou une revendication d’affiliation ? |
| conditions de plateforme | version et date | la boutique ou le service ajoute-t-il des restrictions ou déclarations ? |

**Porte :** toute valeur `forbidden` incompatible avec l’usage ou toute valeur `unknown` sur un axe obligatoire produit `HOLD` ou `REJECT`, jamais une moyenne ou un score compensatoire.

---

<!-- l5:card -->
## LIC-03 — Familles d’objets et sources propriétaires

### Code et dépendances

Vérifier licence du code, exceptions, forme de liaison ou d’incorporation, modifications, distribution binaire, notices et éventuelle mise à disposition du source. Une licence approuvée par l’OSI satisfait la définition Open Source ; un dépôt visible ou un modèle téléchargeable ne devient pas « open source » par accessibilité seule. Voir la [définition OSI](https://opensource.org/osd) et les [licences approuvées](https://opensource.org/licenses/).

### Documentation et médias

Séparer texte original, citations, captures, logos, polices, images et extraits. La licence du dépôt ne s’étend pas silencieusement aux médias tiers ni aux captures d’interfaces.

### Assets, polices et audio

Consommer les fiches du [Livre III, chapitre 5](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#12-carte-des-droits-et-autorisations), notamment les [polices](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#24-polices-et-typographies) et les [enregistrements](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#25-musiques-sons-et-enregistrements).

### Données, modèles et services

Séparer licences du code d’inférence, des poids, des adaptations, du dataset, des entrées, des sorties et conditions du service. Une API distante ajoute confidentialité, rétention, transferts, comptes et conditions évolutives.

### Contenu communautaire

Conserver auteur déclaré, licence, source, version, droits sur les composants, consentements et procédure de retrait. Le fait qu’un utilisateur soumette un fichier ne prouve pas qu’il peut le concéder.

**Diagramme compact :** `famille → propriétaire documentaire → questions spécialisées → fiche de registre → décision de publication`.

**Limite :** cette carte route les questions ; elle ne remplace ni le contrat, ni le texte de licence, ni la revue spécialisée.

---

<!-- l5:card -->
## LIC-04 — Chaîne de provenance et paquet de preuves

| Étape | Preuve attendue |
|---|---|
| acquisition ou création | source, date, opérateur, auteur ou fournisseur |
| texte applicable | licence, contrat, conditions ou consentement versionné |
| original reçu | archive ou fichier conservé avec empreinte |
| transformation | entrée, outil, version, paramètres pertinents, sortie et empreintes |
| dépendances | identifiants et versions de chaque composant requis |
| revue | questions, constats, responsable, date et réserves |
| décision | périmètre autorisé ou refusé, approbateur et expiration |
| publication | build, package, notices, crédits et manifeste corrélés |
| incident | contestation, gel, éléments affectés, retrait et remplacement |
| conservation | classe, accès, durée, copies et vérification de fixité |

**Réponse rapide :** la [chaîne de transformations](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#10-chaîne-de-transformations) et le [paquet de preuves](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#11-paquet-de-preuves) restent les procédures propriétaires.

**Règles :**

- conserver l’original et les dérivés comme objets distincts ;
- ne pas placer contrats, signatures ou données personnelles dans un dépôt public ;
- utiliser une référence opaque vers le stockage restreint ;
- calculer les empreintes sur les octets réellement conservés ;
- ne pas présenter un hash comme preuve d’authenticité, de signature ou de validité juridique ;
- conserver la page et les conditions même si la source disparaît ;
- protéger l’historique append-only des transformations et décisions.

**Diagramme compact :** `source + texte + original → événements de transformation → dépendances → revue → preuve scellée → publication corrélée`.

**Limite :** une preuve peut être authentique mais insuffisante pour l’usage prévu ; plusieurs couches peuvent nécessiter des documents différents.

---

<!-- l5:card -->
## LIC-05 — Personnes, consentements et données

| Sujet | Question distincte |
|---|---|
| donnée personnelle | quelle finalité, quelle base, quelle minimisation et quelle durée ? |
| capture | la personne autorise-t-elle l’enregistrement ou le scan ? |
| prestation | les droits de l’artiste-interprète sont-ils traités ? |
| image et voix | quels usages, supports, territoires, durées et promotions ? |
| montage et adaptation | quelles transformations sont permises ? |
| doublure numérique | la création et les usages sont-ils expressément couverts ? |
| entraînement ou clonage | autorisation séparée, jamais déduite de l’enregistrement initial |
| prestataire | quelles données sont envoyées, conservées, transférées ou réutilisées ? |
| retrait ou incident | quelles nouvelles diffusions cessent et quelles preuves restent conservées ? |
| mineurs ou données sensibles | quelle revue renforcée et quelle autorité compétente ? |

**Réponse rapide :** la procédure détaillée se trouve dans [Voix et artistes-interprètes](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#26-voix-et-artistes-interprètes) et [Image, visage, mocap et données personnelles](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#27-image-visage-mocap-et-données-personnelles).

Les principes officiels de la CNIL imposent notamment finalité, minimisation, durée limitée, sécurité et droits des personnes ; le registre cite la base et le périmètre réels plutôt que d’utiliser « consentement » comme réponse universelle. Voir les [six grands principes du RGPD](https://www.cnil.fr/fr/comprendre-le-rgpd/les-six-grands-principes-du-rgpd).

**Diagramme compact :** `personne → finalité et base → capture → prestation → exploitation → usages sensibles séparés → rétention et retrait`.

**Porte :** un document général ou un accord de jeu n’autorise pas automatiquement clonage vocal, entraînement, publicité, traduction, doublure numérique ou conservation illimitée.

---

<!-- l5:card -->
## LIC-06 — Modèles, datasets, entrées, sorties et services IA

| Objet | Champs minimaux |
|---|---|
| application | nom, version, licence, source et rôle |
| extension ou custom node | commit, licence, dépendances et code exécuté |
| architecture ou modèle | identité, fournisseur, documentation et restrictions |
| poids | fichier, version, hash, licence et redistribution |
| adaptation | base, méthode, licence, données et relation au modèle parent |
| dataset | origine, documentation, droits déclarés, personnes, restrictions et rétention |
| entrée | source, autorisation pour l’opération, personnes, marques et confidentialité |
| workflow | outils, versions, paramètres, seeds et empreinte |
| service | conditions, compte, données envoyées, rétention, territoire et droits sur les sorties |
| sortie brute | identité, date, chaîne, similarités ou risques à revoir |
| sélection humaine | responsable, transformations, contribution et décision |
| sortie publiée | dépendances, attribution, version, package et preuve corrélés |

**Réponse rapide :** le [manifeste de chaîne IA](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#20-modèles-ia-datasets-et-extensions), la [revue des sorties](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#21-sorties-générées-et-contribution-humaine) et la [qualification des entrées](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#22-entrées-des-systèmes-génératifs) sont propriétaires.

**Règles non négociables :**

- la licence de l’application ne couvre pas les poids ;
- la licence des poids ne prouve pas les droits sur le dataset ;
- les conditions d’un service ne deviennent pas une licence open source ;
- un droit d’utiliser une entrée ne prouve pas le droit de l’entraîner ;
- une sortie générée ne reçoit pas automatiquement le statut `public-domain`, `original` ou `free` ;
- le registre conserve la contribution et la revue humaines sans inventer une conclusion d’auteur ;
- une chaîne avec une dépendance `unknown`, `blocked` ou contestée ne passe pas la porte.

Le [règlement européen sur l’intelligence artificielle](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/fra) et son [calendrier officiel de mise en œuvre](https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline) sont des sources réglementaires volatiles à revérifier selon le rôle, l’usage et la date. La fiche ne conclut pas à leur applicabilité pour `Project Asteria`.

**Diagramme compact :** `code + extensions + poids + données + entrées + service → workflow → sortie → revue → périmètre publiable`.

---

<!-- l5:card -->
## LIC-07 — Redistribution, compatibilité et dépendances transitives

### Distinguer les opérations

| Opération | Exemple de question |
|---|---|
| usage interne | peut-on installer et tester l’outil dans l’équipe ? |
| exécution runtime | le composant est-il distribué ou seulement utilisé côté production ? |
| intégration | le fichier devient-il une partie du produit ou une dépendance séparée ? |
| modification | le projet change-t-il le code, le média, les poids ou le format ? |
| redistribution binaire | quelles notices, sources ou conditions accompagnent le package ? |
| redistribution source | le Companion Pack remet-il les fichiers modifiables ? |
| service | le produit appelle-t-il un système tiers sans en distribuer les octets ? |
| mod kit | les utilisateurs peuvent-ils extraire ou réutiliser des composants ? |
| documentation | une capture, un extrait ou un exemple redistribue-t-il un contenu tiers ? |
| archive | le dépôt historique peut-il conserver et transmettre l’objet ? |

### Compatibilité

Une matrice de compatibilité de licences est une **analyse par scénario**. Elle enregistre textes, versions, type de combinaison, éléments modifiés, forme de distribution, obligations et conclusion humaine. Elle ne se réduit pas à une table universelle « compatible/incompatible ».

La [matrice des licences](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#13-matrice-des-licences) sépare redistribution source et intégrée. Les [dépendances transitives](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#30-dépendances-transitives) propagent les blocages sans réécrire les décisions sources.

**Porte :** aucune note, popularité, gratuité ou avantage technique ne compense une obligation impossible à satisfaire.

**Limite :** une exception de licence, une liaison, une adaptation, un asset incorporé ou un modèle distribué exigent une analyse contextuelle ; la fiche route vers une personne compétente lorsqu’un doute matériel subsiste.

---

<!-- l5:matrix -->
## Matrice C — Statuts, décisions et déclarations permises

| Statut | Sens | Déclaration permise |
|---|---|---|
| `not_inventoried` | objet détecté mais non enregistré | « inventaire requis » |
| `unknown` | texte, source ou droit nécessaire absent | « publication bloquée » |
| `under_review` | dossier ouvert, décision non fermée | « revue en cours » |
| `approved_internal` | usage interne qualifié | « usage interne dans le périmètre X » |
| `approved_distribution` | diffusion qualifiée | « redistribution autorisée pour X, sous obligations Y » |
| `approved_limited` | usage restreint | « autorisé uniquement pour X jusqu’à Y » |
| `blocked` | condition incompatible ou preuve insuffisante | « ne pas utiliser ou publier dans X » |
| `contested` | revendication ou contradiction active | « gel des nouvelles diffusions » |
| `withdrawn` | retiré des nouvelles livraisons | « historique conservé, remplacement en cours ou terminé » |
| `superseded` | remplacé par une révision identifiée | « suivre la décision successeure » |
| `stale` | preuve ou revue expirée | « requalification obligatoire » |
| `not_applicable` | axe sans sens dans le périmètre | « non applicable, justification et approbateur enregistrés » |

**Interdictions de formulation :**

- « juridiquement sûr » sans périmètre ni autorité ;
- « libre de droits » comme statut global ;
- « open source » pour un objet non logiciel ou une licence non approuvée sans définition explicite ;
- « conforme RGPD » ou « conforme AI Act » sur la seule base d’une checklist ;
- « domaine public » sans source, juridiction et revue ;
- « tous droits acquis » déduit d’un paiement ;
- « généré par IA donc libre » ;
- « aucune attribution » sans texte qualifié.

**Décision :** l’automatisation peut produire `HOLD` à partir d’un champ manquant. Seule l’autorité désignée ferme `approved_*`, `not_applicable`, une exception ou un retrait.

---

<!-- l5:card -->
## LIC-08 — Notices, attributions, SBOM et paquet de publication

| Livrable | Contenu minimal |
|---|---|
| inventaire distribué | objets, versions, hashes, catégories et chemins de package |
| notices tierces | nom, version, auteur ou projet, licence, copyright et modifications exigées |
| textes de licence | copies ou références requises par les textes applicables |
| crédits | formulation, emplacement, langue et ordre validés |
| offre ou accès au source | méthode, version, durée et destinataires lorsque requis |
| SBOM | composants logiciels et relations dans un format déclaré |
| manifeste d’assets | identités, versions, statuts et preuves de publication |
| manifeste IA | application, extensions, poids, adaptations et conditions |
| consentements | références opaques et présence vérifiée, jamais documents privés dans le package |
| rapport de porte | build, canal, contrôles, réserves, approbateurs et date |
| archive de preuve | sources, textes, décisions, checksums et procédure de reconstruction |

**Réponse rapide :** le [contenu minimal d’une publication](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#13-préparation-dune-publication) et le [packaging](../Livre-IV/CHAPITRE-16-Exports-Godot-et-packaging.md#6-distinguer-export-packaging-et-publication) possèdent la fabrication des livrables. La [checklist de la fiche 24](CHAPITRE-24-Checklists-de-production-et-de-publication.md#chk-08--publication-distribution-et-support) consomme les preuves sans les créer.

La spécification [REUSE 3.3](https://reuse.software/spec/) fournit une méthode de déclaration copyright/licence par fichier fondée sur les expressions SPDX. Elle peut soutenir le dépôt de code, mais ne remplace pas les registres des modèles, datasets, contrats, personnes ou assets.

**Diagramme compact :** `registre qualifié + package fermé → inventaire réel → notices + crédits + sources requises → rapport de porte → archive corrélée`.

**Porte :** les notices sont générées depuis les objets réellement distribués, puis inspectées ; une liste de dépendances de développement ne prouve pas le contenu du package final.

---

<!-- l5:card -->
## LIC-09 — Gouvernance Solo, Studio et séparation des rôles

| Fonction | Solo | Studio |
|---|---|---|
| inventaire | registre unique lisible, maintenu à chaque acquisition | registre central, propriétaires par domaine et intégration aux pipelines |
| acquisition | conserver source, texte et reçu immédiatement | fournisseur approuvé, contrat, responsable et stockage contrôlé |
| qualification | revue différée séparée de la création | relecteur technique, juridique ou conformité selon risque |
| publication | auto-revue datée après pause et checklist | approbateur indépendant pour les objets critiques |
| preuves | arborescence simple hors dépôt public pour les documents sensibles | coffre, accès par rôle, journal et politique de rétention |
| exceptions | rares, bornées, justifiées et expirantes | autorité explicite, compensation, revue et suivi |
| changements | revue manuelle des versions et conditions | veille, alertes, tickets, CI structurelle et campagnes périodiques |
| incident | gel, recherche des usages, remplacement et conservation | coordination produit, juridique, sécurité, support et distribution |
| conseil professionnel | voix, personnes, marques, contrat atypique, diffusion importante ou contestation | critères d’escalade et budget de revue définis avant le jalon |

**Réponse rapide :** les parcours [Solo](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#36-mode-solo) et [Studio](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#37-mode-studio) restent les procédures détaillées. Les responsabilités d’archive sont définies dans [Maintenance et pérennité](../Livre-IV/CHAPITRE-22-Maintenance-archivage-et-perennite.md#6-établir-les-responsabilités).

**Limite :** le cumul de rôles en Solo ne fusionne pas création, qualification et décision. Les étapes et preuves restent séparées dans le temps.

---

<!-- l5:card -->
## LIC-10 — Revue réglementaire, exceptions et escalade

### Signaux d’escalade

| Signal | Action |
|---|---|
| texte absent, contradictoire ou modifié | bloquer et obtenir le texte applicable |
| cession, contrat ou licence personnalisée | revue professionnelle proportionnée |
| personne identifiable, voix, scan ou biométrie | revue droits, données, sécurité et consentements |
| mineur, donnée sensible ou personne vulnérable | revue renforcée avant collecte ou usage |
| marque, personnage, franchise ou confusion d’affiliation | revue marque et communication |
| dataset ou entraînement d’origine incertaine | bloquer la chaîne concernée |
| copyleft, exception, liaison ou distribution complexe | analyse de compatibilité contextualisée |
| diffusion internationale ou plateforme nouvelle | requalifier territoire, canal et obligations |
| service distant ou conditions modifiées | requalifier données, sorties, rétention et droits |
| contestation, retrait ou menace de litige | gel, conservation des preuves et conseil compétent |
| nouvelle obligation réglementaire potentielle | identifier rôle, système, date et source officielle |
| licence globale de collection | décision séparée par catégories d’œuvres et composants |

### Exceptions

Une exception contient : règle écartée, objet, usage, risque, justification, autorité, mesures compensatoires, date, expiration, versions concernées et plan de sortie. Elle ne peut pas autoriser ce que le texte applicable interdit clairement.

**Réponse rapide :** les [règles de blocage](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#32-règles-de-blocage) et les [critères de blocage d’une publication](../Volume-0/CHAPITRE-10-Production-validation-et-publication.md#20-critères-de-blocage-dune-publication) prévalent sur la pression de calendrier.

En France, l’article [L131-3 du Code de la propriété intellectuelle](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000006278958/2026-02-28) encadre notamment la délimitation des droits cédés. Cette référence ne suffit pas à analyser un contrat ou une situation particulière.

**Limite :** la fiche ne détermine ni juridiction compétente, ni titularité, ni validité contractuelle, ni conformité réglementaire individualisée.

---

<!-- l5:card -->
## LIC-11 — Changements, expiration, incidents et retrait

### Déclencheurs de requalification

- nouvelle version du composant, du modèle ou des poids ;
- changement de texte de licence ou de conditions ;
- nouvelle source, adaptation ou dépendance ;
- modification du package ou de la forme de redistribution ;
- nouveau canal, territoire, langue, public ou modèle économique ;
- ajout d’un mod kit, d’un Starter Kit ou de sources modifiables ;
- utilisation d’une personne, d’une voix ou d’une donnée pour un nouvel usage ;
- changement de service, fournisseur, compte ou politique de rétention ;
- échéance d’un contrat, consentement, autorisation ou exception ;
- alerte de sécurité, contestation, demande de retrait ou source disparue ;
- évolution réglementaire ou décision officielle pertinente.

### Réponse

1. geler les nouvelles diffusions si le risque le justifie ;
2. identifier objets, versions, builds, pages, archives et utilisateurs affectés ;
3. préserver textes, contrats, preuves et communications sous accès adapté ;
4. passer le statut à `stale`, `contested`, `blocked` ou `withdrawn` ;
5. désigner le propriétaire et l’autorité de décision ;
6. corriger, obtenir une nouvelle autorisation, limiter, remplacer ou retirer ;
7. reconstruire les livraisons concernées ;
8. corréler notes, support et communications ;
9. conserver l’historique et l’identité de remplacement ;
10. fermer seulement après preuve des actions exigées.

**Réponse rapide :** la [procédure de retrait et remplacement](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#34-procédure-de-retrait-et-remplacement), la [conservation des preuves](../Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md#35-conservation-et-accès-aux-preuves) et les [correctifs et retours arrière](../Livre-IV/CHAPITRE-20-Correctifs-mises-a-jour-et-retour-arriere.md) possèdent l’exécution.

**Diagramme compact :** `changement ou contestation → gel ciblé → impact → décision → remplacement ou retrait → rebuild → communication → archive`.

**Limite :** arrêter une nouvelle publication ne retire pas automatiquement les copies déjà distribuées, les forks, les caches ou les sauvegardes.

---

<!-- l5:card -->
## LIC-12 — Licence de collection, frontières et sources officielles

### Décision de licence globale

Le dépôt ne possède pas encore de licence globale. La décision future doit traiter séparément :

| Couche de la collection | Décision à prendre |
|---|---|
| texte original des Livres | droits accordés pour lecture, copie, adaptation, traduction et redistribution |
| code et scripts originaux | licence logicielle, contributions, brevets éventuels et notices |
| exemples et configurations | relation avec le texte, le code et les dépendances |
| schémas, tableaux et illustrations | licence éditoriale et composants tiers |
| captures, logos et extraits | exceptions, autorisations et marques |
| Companion Pack | contenu de chaque archive, sources, modèles, assets et notices |
| `Project Asteria` | séparation entre exemple documentaire, code, assets et produit |
| contributions futures | accord, certification d’origine ou politique d’acceptation |
| marques et identité du projet | licence de contenu distincte des autorisations de marque |
| données personnelles et contrats | exclus du périmètre public, gouvernés séparément |

**Règles :**

- ne pas annoncer une licence avant de vérifier que le projet contrôle les droits nécessaires ;
- éviter une licence unique lorsque code, documentation et médias exigent des régimes distincts ;
- publier clairement les exclusions et contenus tiers ;
- définir le traitement des contributions et traductions ;
- tester la compatibilité avec les objectifs de diffusion et le Companion Pack ;
- conserver les versions historiques des notices et décisions ;
- faire relire la décision avant publication officielle de la collection.

### Sources officielles vérifiées le 30 juillet 2026

- [SPDX Specifications](https://spdx.dev/use/specifications/) — standard et formats de déclaration ;
- [SPDX License List](https://spdx.org/licenses/) — identifiants et textes référencés ;
- [REUSE Specification 3.3](https://reuse.software/spec/) — déclarations copyright/licence par fichier ;
- [Open Source Definition](https://opensource.org/osd) et [OSI Approved Licenses](https://opensource.org/licenses/) — qualification « open source » pour le logiciel ;
- [Creative Commons Licenses](https://creativecommons.org/share-your-work/cclicenses/) — conditions et six licences principales pour les œuvres ;
- [Code de la propriété intellectuelle, article L131-3](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000006278958/2026-02-28) — source officielle française à relire selon le contrat ;
- [Principes du RGPD présentés par la CNIL](https://www.cnil.fr/fr/comprendre-le-rgpd/les-six-grands-principes-du-rgpd) — finalité, minimisation, durée, sécurité et droits ;
- [Règlement (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/fra) et [calendrier officiel](https://ai-act-service-desk.ec.europa.eu/en/ai-act/eu-ai-act-implementation-timeline) — sources à revérifier pour une chaîne IA entrant réellement dans leur champ.

**Frontières :**

- la fiche 24 possède les checklists et signatures de porte ;
- la future fiche 26 possédera les index croisés, synonymes et navigation globale ;
- le Companion Pack possédera les registres exécutables, validateurs, générateurs de notices et rapports ;
- la décision de licence globale relève d’une action de publication distincte ;
- aucune source officielle citée ne remplace une analyse professionnelle adaptée au produit, au territoire et au contrat.

**Réponse rapide :** la publication reste bloquée tant que la licence globale de la collection n’est pas décidée et que les éléments tiers ne sont pas qualifiés. La présente fiche définit les questions, statuts et preuves ; elle ne choisit aucune licence pour le projet.

## Règles non négociables

- ne jamais déduire un droit d’un prix, d’un téléchargement, d’une visibilité publique ou d’une génération ;
- ne jamais fusionner auteur, titulaire, fournisseur, opérateur et approbateur ;
- ne jamais étendre la licence du code aux modèles, données, médias ou personnes ;
- ne jamais présenter `unknown`, `NOASSERTION`, `under_review` ou une preuve expirée comme autorisation ;
- ne jamais publier un objet dont une dépendance obligatoire reste bloquée ;
- ne jamais exposer un contrat, consentement, signature, secret ou donnée personnelle dans un registre public ;
- ne jamais confondre intégrité cryptographique, signature, authenticité et validité juridique ;
- ne jamais automatiser une conclusion juridique ou réglementaire ;
- ne jamais appliquer une exception au-delà de son objet, sa version, son canal ou son expiration ;
- ne jamais effacer l’historique d’un objet contesté ou retiré ;
- ne jamais annoncer une licence globale avant une décision documentée sur les différentes couches de la collection.

## Limites de preuve

Cette fiche est acceptée au niveau `static-review`. Elle ne :

- qualifie aucune licence, cession, consentement, dataset, modèle, sortie, asset, marque, contrat ou service réel ;
- décide aucune compatibilité de licences ;
- détermine aucune titularité ou applicabilité réglementaire ;
- crée aucun registre de production, SBOM, notice, offre de source ou paquet de preuves ;
- traite aucune donnée personnelle ou confidentielle ;
- produit aucune approbation, exception, signature ou avis juridique ;
- choisit aucune licence globale pour la collection ;
- produit aucun PDF.
