from __future__ import annotations

import re
from pathlib import Path

T = "2026-07-22T23:35:44+02:00"


def rw(path: str, old: str, new: str) -> None:
    p = Path(path)
    s = p.read_text(encoding="utf-8")
    if s.count(old) != 1:
        raise RuntimeError(f"{path}: motif inattendu ({s.count(old)}): {old[:100]!r}")
    p.write_text(s.replace(old, new, 1), encoding="utf-8")


def main() -> None:
    chapter = Path("Livre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md").read_text(encoding="utf-8")
    for marker in ('id: "DOC-L3-CH05"', '## 44. Références institutionnelles et standards vérifiés', '<!-- qa:error-correction-section -->'):
        if marker not in chapter:
            raise RuntimeError(f"chapitre incomplet: {marker}")

    rw("Livre-III/index.md", 'version: "1.3.0"', 'version: "1.4.0"')
    rw(
        "Livre-III/index.md",
        "4. [Pipeline Blender et organisation des fichiers](CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md)\n\nLes chapitres 5 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`.",
        "4. [Pipeline Blender et organisation des fichiers](CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md)\n5. [Provenance, licences et validation des assets](CHAPITRE-05-Provenance-licences-et-validation-des-assets.md)\n\nLes chapitres 6 à 30 seront ajoutés progressivement selon `plans/LIVRE-III-PLAN-MAITRE.md`.",
    )

    rw(
        "ROADMAP.md",
        "- [x] Chapitre 4 — Pipeline Blender et organisation des fichiers.\n- [ ] Préproduction et direction artistique — 4 chapitres sur 5.",
        "- [x] Chapitre 4 — Pipeline Blender et organisation des fichiers.\n- [x] Chapitre 5 — Provenance, licences et validation des assets.\n- [x] Préproduction et direction artistique — 5 chapitres sur 5.",
    )
    rw(
        "ROADMAP.md",
        "**Statut M4 : en cours — 4 chapitres rédigés, repérés et audités sur 30.**",
        "**Statut M4 : en cours — 5 chapitres rédigés, repérés et audités sur 30.**",
    )

    rw(
        "contents.txt",
        "Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md\nLivre-IV/index.md",
        "Livre-III/CHAPITRE-04-Pipeline-Blender-et-organisation-des-fichiers.md\nLivre-III/CHAPITRE-05-Provenance-licences-et-validation-des-assets.md\nLivre-IV/index.md",
    )

    plan = Path("plans/LIVRE-III-PLAN-MAITRE.md")
    s = plan.read_text(encoding="utf-8")
    s = s.replace('version: "1.1.4"', 'version: "1.1.5"', 1)
    s = re.sub(r'last-updated: "[^"]+"', f'last-updated: "{T}"', s, count=1)
    s = s.replace("> **Statut :** en cours — 4 chapitres sur 30", "> **Statut :** en cours — 5 chapitres sur 30", 1)
    s = s.replace(
        "> **Progression :** chapitres 1 à 4 rédigés, repérés et audités au niveau `static-review` ; chapitres 5 à 30 à produire.",
        "> **Progression :** chapitres 1 à 5 rédigés, repérés et audités au niveau `static-review` ; chapitres 6 à 30 à produire.",
        1,
    )
    plan.write_text(s, encoding="utf-8")

    cp = Path("CONTINUITE-PROJET.md")
    c = cp.read_text(encoding="utf-8")
    c = c.replace('version: "3.34.1"', 'version: "3.35.0"', 1)
    c = re.sub(r'last-updated: "[^"]+"', f'last-updated: "{T}"', c, count=1)
    c = c.replace("**En cours : 4 chapitres sur 30.**", "**En cours : 5 chapitres sur 30.**")
    c = c.replace(
        "3. Références, concept art et ComfyUI — terminé au niveau `static-review`.\n4. Pipeline Blender et organisation des fichiers — terminé au niveau `static-review`.\n\nLes chapitres 5 à 30 restent définis",
        "3. Références, concept art et ComfyUI — terminé au niveau `static-review`.\n4. Pipeline Blender et organisation des fichiers — terminé au niveau `static-review`.\n5. Provenance, licences et validation des assets — terminé au niveau `static-review`.\n\nLes chapitres 6 à 30 restent définis",
        1,
    )

    architecture = '''### 11.30 Provenance, licences et validation des assets

- aucun fichier ne devient publiable par simple présence, achat, commande, gratuité ou génération ;
- chaque asset possède un identifiant stable, une version immuable, une fiche, un statut, des dépendances et un paquet de preuves ;
- auteur, titulaire de droits, fournisseur, acquéreur et responsable de publication restent des rôles distincts ;
- droit d’auteur, droits patrimoniaux, droit moral, droits voisins, consentement, données personnelles, image et marques ne sont pas fusionnés ;
- les licences standards utilisent un identifiant exact lorsque possible ; contrats, boutiques et consentements utilisent `LicenseRef-...` ;
- commercial, modification, redistributions, attribution, territoire, durée, sous-licence, entraînement et clonage restent séparés ;
- `unknown`, une contestation ou une dépendance non publiable bloquent la livraison ;
- les transformations sont append-only et relient entrées, outils, paramètres, sorties et empreintes ;
- les chaînes IA qualifient application, extensions, modèles, poids, datasets, entrées, workflow, sorties et sélection humaine ;
- voix, image, interprétation, scan et mocap utilisent des autorisations adaptées et un stockage restreint ;
- les contrôles automatiques vérifient la structure sans prononcer de conclusion juridique ;
- la publication exige une décision humaine et un paquet de preuves haché ;
- un retrait conserve l’historique, gèle les nouvelles livraisons et crée un remplacement versionné ;
- aucune fiche réelle, licence, contrat, consentement, revue juridique ou CI de provenance n’est revendiqué avant matérialisation.
'''
    anchor = "- aucune exécution Blender, export, import Godot, réouverture multi-poste ou mesure n’est revendiquée avant matérialisation.\n\n## 24. Erreurs à ne pas reproduire"
    if c.count(anchor) != 1:
        raise RuntimeError("ancre architecture absente")
    c = c.replace(anchor, anchor.split("\n\n## 24")[0] + "\n\n" + architecture + "\n## 24. Erreurs à ne pas reproduire", 1)

    errs = '''- ne pas considérer qu’un asset gratuit est libre ou redistribuable ;
- ne pas déduire l’étendue des droits d’une facture ou d’un paiement ;
- ne pas utiliser `royalty-free`, `free`, `open` ou `AI-generated` comme identifiant de licence ;
- ne pas fusionner auteur, titulaire, fournisseur et plateforme ;
- ne pas publier une sortie générée sans qualifier modèles, entrées, workflow et conditions ;
- ne pas déduire clonage vocal ou entraînement d’une autorisation générale d’enregistrement ;
- ne pas effacer un asset contesté avec ses preuves ;
- ne pas accepter un asset dont une dépendance reste bloquée ;
- ne pas stocker contrats, signatures ou données personnelles dans un dépôt public ;
- ne pas écraser une licence ancienne sans nouvelle version et requalification ;
- ne pas confondre empreinte et preuve de validité juridique ;
- ne pas laisser une décision automatique remplacer la revue humaine ;

'''
    c = c.replace("- ne pas oublier la mise à jour de ce fichier.", errs + "- ne pas oublier la mise à jour de ce fichier.", 1)
    c = c.replace("- progression du Livre III : 4 chapitres sur 30 ;", "- progression du Livre III : 5 chapitres sur 30 ;", 1)
    c = c.replace(
        "- chapitre 4 du Livre III : version `1.0.0`, niveau `static-review` ;\n- Livre II : 30 chapitres sur 30, publication technique terminée ;",
        "- chapitre 4 du Livre III : version `1.0.0`, niveau `static-review` ;\n- chapitre 5 du Livre III : version `1.0.0`, niveau `static-review` ;\n- Livre II : 30 chapitres sur 30, publication technique terminée ;",
        1,
    )

    next_section = '''## 26. Prochaine action

Le chapitre 5 du Livre III est rédigé, repéré et audité au niveau `static-review`. La politique de provenance distingue auteurs, titulaires, fournisseurs, licences, consentements, données personnelles, chaînes IA, transformations, dépendances, statuts de blocage, publication et retrait. Aucun registre réel, contrat, consentement, asset ou contrôle runtime n’est revendiqué comme matérialisé.

Action suivante :

> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**

```text
Livre-III/CHAPITRE-06-Creation-des-humains.md
Niveau GPT-5.6 Sol recommandé : Élevée
```

Le chapitre 6 produira une base humaine modulaire, crédible, animable et compatible avec les contraintes de personnalisation, de topologie, de matériaux, de LOD et de performance. Les visages, cheveux et vêtements resteront approfondis dans leurs chapitres spécialisés.

'''
    c, n = re.subn(r"## 26\. Prochaine action\n.*?(?=## 27\. Journal)", next_section, c, count=1, flags=re.S)
    if n != 1:
        raise RuntimeError("section prochaine action absente")

    journal = f'''### {T} — version 3.35.0

- chapitre 5 du Livre III créé, relu et audité au niveau `static-review` ;
- auteurs, titulaires, licences, consentements, données personnelles, image, droits voisins et marques distingués ;
- fiches, registre, preuves, transformations, restrictions, statuts et dépendances documentés ;
- chaînes IA, voix, scans, mocap, polices, audio, marques et contenus sensibles encadrés ;
- contrôles structurels, porte humaine de publication, retrait et remplacement définis ;
- sources institutionnelles françaises, européennes et standards de licences vérifiés au 22 juillet 2026 ;
- index, roadmap, ordre lecteur, plan maître, audit, preuve QA provisoire et continuité mis à jour ;
- prochaine action déplacée vers le chapitre 6 — Création des humains, niveau Élevée ;
- aucun registre réel, contrat, consentement, runtime ou PDF du Livre III produits.

'''
    c = c.replace("## 27. Journal\n\n", "## 27. Journal\n\n" + journal, 1)
    cp.write_text(c, encoding="utf-8")
    print("CH05_GOVERNANCE_APPLIED")


if __name__ == "__main__":
    main()
