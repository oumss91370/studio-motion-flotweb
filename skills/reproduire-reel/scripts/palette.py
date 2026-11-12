#!/usr/bin/env python3
"""Palette d'une image (ou d'une zone) : couleurs dominantes avec leur part, et le « look » global.

  python palette.py <image ou video.mp4@numéro> <sortie.json> [--k 6] [--boite x0,y0,x1,y1] [--nom "plein jour"]
Sert aux décors : une palette par ambiance (jour, soir, intérieur, nuit…), relevée sur une image nette de chaque ambiance.
Écrit <sortie>.json et <sortie>.png (les pastilles, à garder avec la fiche de la référence). Le « look » :
  luminance_moyenne   0 (noir) à 255 (blanc)
  contraste           écart type de la luminance, en niveaux (40 à 60 : image contrastée)
  saturation_moyenne  0 (gris) à 1 (couleurs pures)
  dominante_chaude    moyenne de (rouge − bleu), en niveaux : positif = image chaude, négatif = image froide
  nettete             énergie des contours (moyenne du laplacien, en niveaux). Elle n'a pas d'échelle absolue : elle ne se compare
                      qu'entre deux zones de la MÊME image (--boite). Un sujet 3 fois plus net que le fond = profondeur de champ courte.
Dépendances : Python 3.9+, numpy, Pillow, opencv-python. Écrit par Flot Web.
"""
import sys
sys.dont_write_bytecode = True
import argparse, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np
import cv2
from PIL import Image, ImageDraw
import mp_base as B

def palette(chemin, k=6, boite=None):
    rgb = B.lire(chemin)
    if boite:
        x0, y0, x1, y1 = [int(v) for v in boite]
        rgb = rgb[max(0, y0):y1, max(0, x0):x1]
    if rgb.shape[0] < 4 or rgb.shape[1] < 4:
        raise SystemExit(f"la boîte {boite} est vide ou hors de l'image : elle s'écrit x0,y0,x1,y1 en pixels de l'image")
    L = B.luma(rgb)
    pas = max(1, int(round((rgb.shape[0] * rgb.shape[1] / 60000) ** 0.5)))
    ech = rgb[::pas, ::pas].reshape(-1, 3)
    k = max(1, min(int(k), len(ech)))
    labs = B.lab(ech).astype(np.float32)
    cv2.setRNGSeed(7)
    _, et, _ = cv2.kmeans(labs, k, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 40, 0.1), 4, cv2.KMEANS_PP_CENTERS)
    et = et.ravel()
    coul = []
    for i in sorted(range(k), key=lambda i: -(et == i).sum()):
        z = et == i
        if z.sum() < 5:
            continue
        c = np.median(ech[z], 0)
        t, s, l = B.tsl(c)
        coul.append(dict(hex=B.hexa(c), part=round(float(z.mean()), 3), luminance=round(float(B.luma(c)), 1), teinte=round(t), saturation=round(s), luminosite=round(l)))
    mx, mn = rgb.max(-1), rgb.min(-1)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1), 0)
    lap = cv2.Laplacian(L, cv2.CV_32F, ksize=3)
    return dict(image=str(chemin), boite=boite, taille=[int(rgb.shape[1]), int(rgb.shape[0])], couleurs=coul,
                look=dict(luminance_moyenne=round(float(L.mean()), 1), contraste=round(float(L.std()), 1), saturation_moyenne=round(float(sat.mean()), 3),
                          dominante_chaude=round(float((rgb[..., 0] - rgb[..., 2]).mean()), 1), nettete=round(float(np.abs(lap).mean()), 2)))

def pastilles(res, sortie, nom=""):
    c = res["couleurs"]
    im = Image.new("RGB", (max(1, len(c)) * 150 + 10, 190), (255, 255, 255)); d = ImageDraw.Draw(im)
    d.text((8, 6), (nom + " · " if nom else "") + f"luminance {res['look']['luminance_moyenne']}, contraste {res['look']['contraste']}, saturation {res['look']['saturation_moyenne']}",
           fill=(0, 0, 0), font=B.police(14, True))
    for i, e in enumerate(c):
        x = 10 + i * 150
        d.rectangle((x, 30, x + 140, 140), fill=tuple(int(v) for v in B.de_hexa(e["hex"])), outline=(90, 90, 90))
        d.text((x, 146), e["hex"], fill=(0, 0, 0), font=B.police(15, True))
        d.text((x, 166), f"{100 * e['part']:.0f} % · lum. {e['luminance']:.0f}", fill=(60, 60, 60), font=B.police(13))
    im.save(sortie)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("image"); ap.add_argument("sortie"); ap.add_argument("--k", type=int, default=6); ap.add_argument("--boite"); ap.add_argument("--nom", default="")
    a = ap.parse_args()
    r = palette(a.image, a.k, [int(v) for v in a.boite.split(",")] if a.boite else None)
    r["nom"] = a.nom
    s = pathlib.Path(a.sortie); s.parent.mkdir(parents=True, exist_ok=True)
    s.write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
    pastilles(r, s.with_suffix(".png"), a.nom)
    print(a.nom or a.image, ":", " ".join(f"{c['hex']} ({100 * c['part']:.0f} %)" for c in r["couleurs"]), "|", r["look"])
