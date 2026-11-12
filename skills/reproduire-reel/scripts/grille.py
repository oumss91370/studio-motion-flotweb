#!/usr/bin/env python3
"""Recadrage d'une image avec une grille de coordonnées (en pixels de l'image d'origine), pour poser les cibles à la main.

  python grille.py <image ou video.mp4@numéro> <sortie.jpg> [x0 y0 x1 y1] [--k 2] [--pas 50]
      sans boîte : l'image entière ; --k : agrandissement (au plus proche voisin, on voit les pixels) ; --pas : pas de la grille
On lit les coordonnées sur la grille, on les écrit dans le fichier de cibles (references/fichier-de-cibles.md).
Dépendances : Python 3.9+, Pillow, numpy, FFmpeg (seulement pour video@numéro). Écrit par Flot Web.
"""
import sys
sys.dont_write_bytecode = True
import argparse, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from PIL import Image, ImageDraw
import mp_base as B

def grille(chemin, sortie, boite=None, k=1.0, pas=50):
    im = B.ouvrir(chemin)
    x0, y0, x1, y1 = boite or (0, 0, im.width, im.height)
    x0, y0, x1, y1 = max(0, int(x0)), max(0, int(y0)), min(im.width, int(x1)), min(im.height, int(y1))
    im = im.crop((x0, y0, x1, y1))
    if k != 1:
        im = im.resize((int(im.width * k), int(im.height * k)), Image.NEAREST if k > 1 else Image.LANCZOS)
    d = ImageDraw.Draw(im, "RGBA"); f = B.police(13, True)
    for x in range((x0 // pas + 1) * pas, x1, pas):
        d.line(((x - x0) * k, 0, (x - x0) * k, im.height), fill=(255, 255, 0, 110))
        d.text(((x - x0) * k + 2, 2), str(x), fill=(255, 255, 0), font=f, stroke_width=2, stroke_fill=(0, 0, 0))
    for y in range((y0 // pas + 1) * pas, y1, pas):
        d.line((0, (y - y0) * k, im.width, (y - y0) * k), fill=(0, 255, 255, 110))
        d.text((2, (y - y0) * k + 2), str(y), fill=(0, 255, 255), font=f, stroke_width=2, stroke_fill=(0, 0, 0))
    pathlib.Path(sortie).parent.mkdir(parents=True, exist_ok=True)
    im.save(sortie, quality=90)
    return im.size

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("image"); p.add_argument("sortie"); p.add_argument("boite", nargs="*", type=int)
    p.add_argument("--k", type=float, default=1.0); p.add_argument("--pas", type=int, default=50)
    a = p.parse_args()
    if a.boite and len(a.boite) != 4:
        p.error("la boîte se donne par quatre nombres : x0 y0 x1 y1")
    print(a.sortie, grille(a.image, a.sortie, a.boite or None, a.k, a.pas))
