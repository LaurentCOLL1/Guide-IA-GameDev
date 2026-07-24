#!/usr/bin/env python3
from __future__ import annotations

import base64
import json
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TIMESTAMP = '2026-07-24T15:16:59+02:00'

def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: attendu 1 occurrence, trouvé {count}")
    return text.replace(old, new, 1)

def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")

def write(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")

payload_text = "".join(
    path.read_text(encoding="utf-8").strip()
    for path in sorted((ROOT / ".qa").glob("ch22-payload-*.txt"))
)
payload = json.loads(zlib.decompress(base64.b64decode(payload_text)).decode("utf-8"))

for rel, content in payload.items():
    path = ROOT / rel
    if path.exists():
        raise RuntimeError(f"Fichier déjà existant, création refusée : {rel}")
    write(rel, content)

contents = read("contents.txt")
contents = replace_once(
    contents,
    "Livre-III/CHAPITRE-21-Capture-de-mouvement-et-retargeting.md\n",
    "Livre-III/CHAPITRE-21-Capture-de-mouvement-et-retargeting.md\n"
    "Livre-III/CHAPITRE-22-Cinematiques-cameras-et-mise-en-scene.md\n",
    "contents chapitre 22",
)
write("contents.txt", contents)

index = read("Livre-III/index.md")
index = replace_once(index, 'version: "1.20.0"', 'version: "1.21.0"', "version index")
index = replace_once(
    index,
    "21. [Capture de mouvement et retargeting](CHAPITRE-21-Capture-de-mouvement-et-retargeting.md)\n",
    "21. [Capture de mouvement et retargeting](CHAPITRE-21-Capture-de-mouvement-et-retargeting.md)\n"
    "22. [Cinématiques, caméras et mise en scène](CHAPITRE-22-Cinematiques-cameras-et-mise-en-scene.md)\n",
    "entrée index chapitre 22",
)
index = replace_once(
    index,
    "Les chapitres 22 à 30 seront ajoutés progressivement",
    "Les chapitres 23 à 30 seront ajoutés progressivement",
    "futurs chapitres index",
)
write("Livre-III/index.md", index)

roadmap = read("ROADMAP.md")
roadmap = replace_once(
    roadmap,
    "- [x] Chapitre 21 — Capture de mouvement et retargeting.\n",
    "- [x] Chapitre 21 — Capture de mouvement et retargeting.\n"
    "- [x] Chapitre 22 — Cinématiques, caméras et mise en scène.\n",
    "roadmap chapitre 22",
)
roadmap = replace_once(
    roadmap,
    "**Statut M4 : en cours — 21 chapitres rédigés, repérés et audités sur 30.**",
    "**Statut M4 : en cours — 22 chapitres rédigés, repérés et audités sur 30.**",
    "statut roadmap",
)
write("ROADMAP.md", roadmap)

plan = read("plans/LIVRE-III-PLAN-MAITRE.md")
plan = replace_once(plan, 'version: "1.1.22"', 'version: "1.1.23"', "version plan")
plan = replace_once(
    plan,
    'last-updated: "2026-07-24T13:38:11+02:00"',
    f'last-updated: "{TIMESTAMP}"',
    "horodatage plan",
)
plan = replace_once(
    plan,
    "> **Statut :** en cours — 21 chapitres sur 30",
    "> **Statut :** en cours — 22 chapitres sur 30",
    "statut plan",
)
plan = replace_once(
    plan,
    "> **Progression :** chapitres 1 à 21 rédigés, repérés et audités au niveau `static-review` ; chapitres 22 à 30 à produire.",
    "> **Progression :** chapitres 1 à 22 rédigés, repérés et audités au niveau `static-review` ; chapitres 23 à 30 à produire.",
    "progression plan",
)
write("plans/LIVRE-III-PLAN-MAITRE.md", plan)

continuity = read("CONTINUITE-PROJET.md")
continuity = replace_once(continuity, 'version: "3.52.0"', 'version: "3.53.0"', "version continuité")
continuity = replace_once(
    continuity,
    'last-updated: "2026-07-24T13:38:11+02:00"',
    f'last-updated: "{TIMESTAMP}"',
    "horodatage continuité",
)
continuity = replace_once(
    continuity,
    "**En cours : 20 chapitres sur 30.**",
    "**En cours : 22 chapitres sur 30.**",
    "synthèse Livre III",
)
continuity = replace_once(
    continuity,
    "20. Animation procédurale et animation par keyframes — terminé au niveau `static-review`.\n\n"
    "Les chapitres 21 à 30 restent définis",
    "20. Animation procédurale et animation par keyframes — terminé au niveau `static-review`.\n"
    "21. Capture de mouvement et retargeting — terminé au niveau `static-review`.\n"
    "22. Cinématiques, caméras et mise en scène — terminé au niveau `static-review`.\n\n"
    "Les chapitres 23 à 30 restent définis",
    "collection Livre III",
)
continuity = replace_once(
    continuity,
    "## 24. Erreurs à ne pas reproduire",
    '### 11.33 Cinématiques, caméras et mise en scène\n\n- `AST-CINE-PILOT-SCOUT-RELAY-001` constitue le pilote cinématique du chapitre 22 ;\n- l’intention dramatique, les beats, le storyboard, la liste de plans, le blocage, l’animatique et la séquence Godot restent des états distincts et versionnés ;\n- chaque plan possède un identifiant stable, une fonction narrative, une durée candidate, une caméra, des dépendances et un statut de revue ;\n- focales, FOV, projection, composition, profondeur, hauteur, direction écran, regards et raccords sont décidés selon l’information à transmettre ;\n- les trajectoires de caméra utilisent des chemins et interpolations inspectables ; le bruit éventuel reste borné, désactivable et subordonné au confort ;\n- la scène cinématique dérivée référence les personnages, décors et animations approuvés sans éditer directement les imports ;\n- `Camera3D`, `AnimationPlayer` et un directeur limité orchestrent la lecture visuelle sans acquérir d’autorité gameplay ;\n- animations, dialogue, lumière et VFX partagent une base temporelle documentée, mais leurs assets restent produits dans leurs chapitres propriétaires ;\n- l’entrée, la sortie, le saut, l’annulation et l’interruption restaurent explicitement caméra, entrées, état final et contrôle du joueur ;\n- les versions de revue conservent commentaires, plans concernés, décisions, responsables et historique des reprises ;\n- la porte exige lecture narrative claire, rythme maîtrisé, dépendances résolues, séquence fonctionnelle dans le build et retour gameplay contrôlé ;\n- aucun storyboard, animatique, asset, scène Godot, timeline, rendu, test de build, synchronisation ou mesure runtime n’est revendiqué avant matérialisation.\n\n' + "## 24. Erreurs à ne pas reproduire",
    "section décisions chapitre 22",
)
continuity = replace_once(
    continuity,
    "## 25. État courant",
    '- ne pas ajouter un plan dépourvu de fonction narrative vérifiable ;\n- ne pas franchir l’axe de mise en scène sans préparation ou nouveau plan d’établissement ;\n- ne pas utiliser une focale ou un FOV extrême pour masquer un mauvais placement ;\n- ne pas éditer directement une scène importée comme source de la cinématique ;\n- ne pas laisser une piste de méthode ou la timeline modifier directement l’état gameplay autoritaire ;\n- ne pas désactiver les entrées ou la caméra de gameplay sans restauration garantie ;\n- ne pas traiter un dialogue, une lumière ou un VFX placeholder comme un asset final approuvé ;\n- ne pas démarrer la séquence avant que ses dépendances obligatoires soient chargées et validées ;\n- ne pas valider une cinématique uniquement dans l’éditeur, sur un seul ratio d’image ou sans variante de confort ;\n- ne pas déclarer rythme, synchronisation, stabilité du build ou coût runtime sans exécution et mesures réelles ;\n\n' + "## 25. État courant",
    "erreurs chapitre 22",
)
continuity = replace_once(
    continuity,
    "- progression du Livre III : 21 chapitres sur 30 ;",
    "- progression du Livre III : 22 chapitres sur 30 ;",
    "état progression",
)
continuity = replace_once(
    continuity,
    "- chapitre 21 du Livre III : version `1.0.0`, niveau `static-review` ;\n",
    "- chapitre 21 du Livre III : version `1.0.0`, niveau `static-review` ;\n"
    "- chapitre 22 du Livre III : version `1.0.0`, niveau `static-review` ;\n",
    "état chapitre 22",
)
continuity = replace_once(continuity, 'Le chapitre 21 du Livre III est rédigé, repéré et audité au niveau `static-review`. Le pilote `AST-MOCAP-PILOT-SCOUT-001` couvre choix de capture, droits, calibration, ingestion, nettoyage, contacts, mapping, poses de référence, proportions, corrections, import Godot et validation multi-rigs. Aucune session, donnée personnelle, animation, bibliothèque, GLB, scène, capture, rapport runtime ou mesure n’est revendiqué comme matérialisé.\n\nAction suivante :\n\n> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n```text\nLivre-III/CHAPITRE-22-Cinematiques-cameras-et-mise-en-scene.md\nNiveau GPT-5.6 Sol recommandé : Élevée\n```\n\nLe chapitre 22 traitera storyboard, liste de plans, focales, composition, animatique, caméras Godot, timelines, synchronisation, versions et transitions vers le gameplay, sans refaire la production et le retargeting des animations du chapitre 21.\n', 'Le chapitre 22 du Livre III est rédigé, repéré et audité au niveau `static-review`. Le pilote `AST-CINE-PILOT-SCOUT-RELAY-001` couvre intention dramatique, storyboard, liste de plans, focales, composition, raccords, animatique, caméras Godot, timeline, synchronisation et transitions avec le gameplay. Aucun storyboard, animatique, asset, scène Godot, timeline, rendu, rapport runtime ou mesure n’est revendiqué comme matérialisé.\n\nAction suivante :\n\n> **[LECTURE] Chemin et niveau prévisionnels — Ne pas saisir.**\n\n```text\nLivre-III/CHAPITRE-23-Effets-visuels-particules-et-simulations.md\nNiveau GPT-5.6 Sol recommandé : Élevée\n```\n\nLe chapitre 23 traitera effets visuels, particules GPU et CPU, shaders, simulations précalculées, collisions, pooling, transparence, overdraw, LOD et budgets, sans refaire la mise en scène, les caméras ou la timeline du chapitre 22.\n', "prochaine action")
continuity = replace_once(
    continuity,
    "## 27. Journal\n\n",
    "## 27. Journal\n\n" + '### 2026-07-24T15:16:59+02:00 — version 3.53.0\n\n- chapitre 22 du Livre III créé, relu et audité au niveau `static-review` ;\n- pilote `AST-CINE-PILOT-SCOUT-RELAY-001` documenté pour une courte séquence d’éclaireur au relais abandonné ;\n- intention dramatique, beats, storyboard, liste de plans, blocage, animatique et base temporelle encadrés ;\n- focales, FOV, projection, composition, profondeur, axes, regards, raccords et mouvements de caméra documentés ;\n- architecture Godot avec scènes dérivées, `Camera3D`, `AnimationPlayer`, routeur et directeur de séquence préparée ;\n- synchronisation des animations, dialogues, lumières et VFX placeholders séparée de la production de leurs assets ;\n- entrée, sortie, saut, annulation, interruption, chargement et restauration du gameplay encadrés ;\n- versions de revue, commentaires, ratios d’image, confort visuel, sous-titres, budgets candidats et tests de build documentés ;\n- progression documentaire portée à 22 chapitres sur 30 et synthèse supérieure du Livre III alignée ;\n- prochaine action déplacée vers le chapitre 23 — Effets visuels, particules et simulations, niveau Élevée ;\n- aucun storyboard, animatique, asset, scène Godot, timeline, rendu, test runtime, benchmark ou PDF du Livre III produit.\n\n',
    "journal chapitre 22",
)
write("CONTINUITE-PROJET.md", continuity)

print("Chapitre 22 et gouvernance matérialisés.")
