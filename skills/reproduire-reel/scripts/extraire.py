#!/usr/bin/env python3
"""Extrait des images d'une vidéo en PNG pleine résolution, sans aucun redimensionnement, et note leur netteté.

  python extraire.py <video> <dossier> <numéros> [préfixe]
      numéros : 345,990,1300 ou 100-110 (plage) ou un mélange ; numérotation à partir de 0, celle de decouper.py et bandes.py
      préfixe : début du nom des fichiers (défaut « ref ») → ref_0345.png

Pour chaque image, l'écart moyen avec l'image précédente et la suivante est écrit dans <préfixe>_nettete.json :
proche de 0 = plan figé (aucun flou de mouvement possible) ; au-dessus de 10 = quelque chose bouge, mesurer avec prudence.
Dépendances : Python 3.9+, numpy, Pillow, FFmpeg. Écrit par Flot Web.
"""
import sys
sys.dont_write_bytecode = True
import json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np
from PIL import Image
import mp_base as B

def numeros(texte):
    out = []
    for bout in str(texte).split(","):
        bout = bout.strip()
        if "-" in bout:
            a, b = bout.split("-", 1)
            out += list(range(int(a), int(b) + 1))
        elif bout:
            out.append(int(bout))
    return out

def extraire(video, dossier, nums, prefixe="ref"):
    dossier = pathlib.Path(dossier); dossier.mkdir(parents=True, exist_ok=True)
    veux = sorted(set(n + d for n in nums for d in (-1, 0, 1) if n + d >= 0))
    ims = {n: np.asarray(im, dtype=np.int16) for n, im in B.lire_images(video, veux).items()}
    f = dossier / f"{prefixe}_nettete.json"
    rapport = json.loads(f.read_text(encoding="utf-8-sig")) if f.exists() else {}
    for n in nums:
        if n not in ims:
            print(f"image {n} : absente de la vidéo")
            continue
        Image.fromarray(ims[n].astype(np.uint8)).save(dossier / f"{prefixe}_{n:04d}.png")
        e = {m: float(np.abs(ims[n] - ims[m]).mean()) for m in (n - 1, n + 1) if m in ims}
        pire = max(e.values(), default=0.0)
        rapport[str(n)] = dict(ecart_precedente=round(e[n - 1], 2) if n - 1 in e else None, ecart_suivante=round(e[n + 1], 2) if n + 1 in e else None,
                               taille=list(ims[n].shape[1::-1]),
                               verdict="figé" if pire < 4 else ("mouvement léger" if pire < 10 else "en mouvement : à mesurer avec prudence"))
    f.write_text(json.dumps(rapport, indent=1, ensure_ascii=False), encoding="utf-8")
    return rapport

if __name__ == "__main__":
    if len(sys.argv) < 4 or sys.argv[1] in ("-h", "--help"):
        print(__doc__); sys.exit(0 if len(sys.argv) > 1 else 2)
    nums = numeros(sys.argv[3])
    r = extraire(sys.argv[1], sys.argv[2], nums, sys.argv[4] if len(sys.argv) > 4 else "ref")
    for n in nums:
        print(n, r.get(str(n)))
