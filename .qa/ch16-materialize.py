from pathlib import Path
import hashlib

checks = {
    Path("Livre-III/CHAPITRE-16-Textures-materiaux-et-pipeline-PBR.md"): "2c5d9182ff27921ee14905e5a516a73a054e3657a6d8e7394347c957044e105b",
    Path("Livre-III/QA/AUDIT-CHAPITRE-16.md"): "55eb5d449c8fc79ecbda55ef66b2ed76de1c6a5fa3bf78d87efa3cf218d8d3e8",
}

for path, expected in checks.items():
    if not path.is_file():
        raise RuntimeError(f"Fichier permanent absent: {path}")
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError(f"Empreinte inattendue pour {path}: {actual}")
