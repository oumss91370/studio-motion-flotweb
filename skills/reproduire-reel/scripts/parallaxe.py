#!/usr/bin/env python3
"""Ce qui est en volume et ce qui est peint : parallaxe entre deux images d'un même plan pendant un mouvement de caméra.

  python parallaxe.py <video> <dossier de sortie> 150:156,684:690 [--bande y0,y1]
      paires a:b : deux images du MÊME plan, prises pendant un déplacement de caméra, écartées de 1 à 10 images
                   (choisir a et b pour que le décor ait bougé de 10 à 50 px ; pas de coupe ni de fondu entre les deux)
      --bande : bande horizontale ignorée (les sous-titres), en pixels

Pour chaque paire : flot optique dense, puis ajustement d'UNE homographie (RANSAC) sur tout le flot.
- Un décor plat (toile peinte), ou une caméra qui ne fait que tourner ou zoomer, est entièrement expliqué par l'homographie :
  le résidu est proche de 0 partout.
- Un décor en volumes vu par une caméra qui se déplace laisse un résidu qui dépend de la profondeur : c'est la parallaxe.
Lecture : résidu médian sous 1 px et 90e centile sous 3 px = plat ou caméra qui pivote (non concluant si le flot médian est
sous 3 px) ; résidu de plusieurs pixels, différent d'une zone à l'autre = volumes à des profondeurs différentes. Les zones
qui bougent ensemble et très peu (ciel, lointain) sont les plans peints.
Les personnages qui bougent entre les deux images laissent eux aussi un résidu : lire la planche, pas seulement le chiffre.
Sorties : <a>_<b>_parallaxe.jpg (image, norme du flot, résidu) et parallaxe.json (résidu global, par bandes et par tuiles).
Dépendances : Python 3.9+, numpy, Pillow, opencv-python, FFmpeg. Écrit par Flot Web.
"""
import sys
sys.dont_write_bytecode = True
import argparse, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np
import cv2
from PIL import Image, ImageDraw
import mp_base as B

def _couleur(v, vmax):
    u = np.clip(v / vmax, 0, 1)
    return cv2.cvtColor(cv2.applyColorMap((u * 255).astype(np.uint8), cv2.COLORMAP_TURBO), cv2.COLOR_BGR2RGB)

def paire(A, Bi, bande=None):
    if A.shape != Bi.shape:
        raise ValueError("les deux images n'ont pas la même taille")
    ga, gb = B.luma(A).astype(np.uint8), B.luma(Bi).astype(np.uint8)
    dis = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM)
    flot = dis.calc(ga, gb, None)
    h, w = ga.shape
    # on ne garde que les points texturés (le flot n'a pas de sens dans un aplat), hors de la bande exclue
    g = cv2.GaussianBlur(np.hypot(cv2.Sobel(ga, cv2.CV_32F, 1, 0), cv2.Sobel(ga, cv2.CV_32F, 0, 1)), (0, 0), 6)
    fiable = g > 12
    if bande:
        fiable[max(0, int(bande[0])):max(0, int(bande[1]))] = False
    ys, xs = np.mgrid[8:h - 8:12, 8:w - 8:12]
    ok = fiable[ys, xs]
    if ok.sum() < 50:
        raise ValueError("trop peu de points texturés pour suivre le mouvement (image trop plate ou trop floue)")
    src = np.stack([xs[ok], ys[ok]], -1).astype(np.float32)
    dst = src + flot[ys[ok], xs[ok]]
    Hm, inl = cv2.findHomography(src, dst, cv2.RANSAC, 1.5)
    if Hm is None:
        raise ValueError("aucune homographie ajustable sur ce flot")
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    pts = cv2.perspectiveTransform(np.stack([xx, yy], -1).reshape(-1, 1, 2), Hm).reshape(h, w, 2)
    res = np.hypot(flot[..., 0] - (pts[..., 0] - xx), flot[..., 1] - (pts[..., 1] - yy))
    norme = np.hypot(flot[..., 0], flot[..., 1])
    def stat(m):
        m = m & fiable
        return None if m.sum() < 400 else dict(flot_median_px=round(float(np.median(norme[m])), 2), residu_median_px=round(float(np.median(res[m])), 2),
                                               residu_p90_px=round(float(np.percentile(res[m], 90)), 2), dx=round(float(np.median(flot[..., 0][m])), 2), dy=round(float(np.median(flot[..., 1][m])), 2))
    bandes = []
    for i in range(8):
        m = np.zeros((h, w), bool); m[i * h // 8:(i + 1) * h // 8] = True
        bandes.append(stat(m))
    tuiles = []
    for j in range(8):
        ligne = []
        for i in range(4):
            m = np.zeros((h, w), bool); m[j * h // 8:(j + 1) * h // 8, i * w // 4:(i + 1) * w // 4] = True
            s = stat(m)
            ligne.append(None if s is None else s["residu_median_px"])
        tuiles.append(ligne)
    g_ = stat(np.ones((h, w), bool))
    if g_ is None:
        raise ValueError("trop peu de points texturés pour une statistique")
    lecture = ("non concluant : la caméra bouge trop peu entre ces deux images (prendre des images plus écartées, pendant un déplacement)" if g_["flot_median_px"] < 3
               else "plat, ou caméra qui ne fait que tourner ou zoomer : une seule homographie explique tout" if g_["residu_median_px"] < 1 and g_["residu_p90_px"] < 3
               else "parallaxe : des éléments à des profondeurs différentes (volumes) ; regarder sur la planche lesquels")
    return dict(global_=g_, lecture=lecture, part_expliquee_par_homographie_pct=round(100 * float(inl.mean()), 1), bandes_haut_vers_bas=bandes, residu_par_tuile=tuiles), norme, res, fiable

def planche(A, norme, res, fiable, chemin, titre, r):
    h, w = A.shape[:2]
    vmax = max(4.0, float(np.percentile(norme[fiable], 98)))
    rmax = max(2.0, float(np.percentile(res[fiable], 98)))
    n = _couleur(norme, vmax); n[~fiable] = (n[~fiable] * 0.25).astype(np.uint8)
    q = _couleur(res, rmax); q[~fiable] = (q[~fiable] * 0.25).astype(np.uint8)
    toile = Image.new("RGB", (3 * (w // 2), h // 2 + 70), (20, 20, 24))
    for i, im in enumerate((np.clip(A, 0, 255).astype(np.uint8), n, q)):
        toile.paste(Image.fromarray(im).resize((w // 2, h // 2), Image.LANCZOS), (i * (w // 2), 70))
    d = ImageDraw.Draw(toile)
    f = B.police(20, True)
    g = r["global_"]
    d.text((8, 6), titre, font=f, fill=(255, 255, 255))
    d.text((8, 34), f"flot médian {g['flot_median_px']} px | résidu après homographie : médiane {g['residu_median_px']} px, 90e centile {g['residu_p90_px']} px", font=f, fill=(200, 220, 255))
    d.text((w // 2 + 8, 74), f"norme du flot (0 à {vmax:.0f} px)", font=f, fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))
    d.text((2 * (w // 2) + 8, 74), f"résidu = parallaxe (0 à {rmax:.0f} px)", font=f, fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))
    toile.save(chemin, quality=88)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video"); ap.add_argument("sortie"); ap.add_argument("paires", help="a:b,c:d …"); ap.add_argument("--bande")
    a = ap.parse_args()
    bande = [int(v) for v in a.bande.split(",")] if a.bande else None
    try:
        paires = [tuple(int(x) for x in p.split(":")) for p in a.paires.split(",") if p.strip()]
        assert paires and all(len(p) == 2 and p[0] != p[1] for p in paires)
    except (ValueError, AssertionError):
        raise SystemExit("paires : « a:b,c:d », deux numéros d'image différents par paire (numérotation à partir de 0)")
    sortie = pathlib.Path(a.sortie); sortie.mkdir(parents=True, exist_ok=True)
    ims = {n: np.asarray(im, dtype=np.float32) for n, im in B.lire_images(a.video, [n for p in paires for n in p]).items()}
    out = {}
    for x, y in paires:
        if x not in ims or y not in ims:
            print(f"  ! paire {x}:{y} : image absente de la vidéo"); out[f"{x}-{y}"] = dict(erreur="image absente de la vidéo"); continue
        try:
            r, norme, res, fiable = paire(ims[x], ims[y], bande)
        except (ValueError, cv2.error) as e:
            print(f"  ! paire {x}:{y} : {e}"); out[f"{x}-{y}"] = dict(erreur=str(e)); continue
        out[f"{x}-{y}"] = r
        planche(ims[x], norme, res, fiable, sortie / f"{x:04d}_{y:04d}_parallaxe.jpg", f"images {x} → {y}", r)
        g = r["global_"]
        print(f"{x} → {y} : flot médian {g['flot_median_px']} px, résidu médian {g['residu_median_px']} px, 90e centile {g['residu_p90_px']} px ; "
              f"résidu par bande (haut → bas) {[None if b is None else b['residu_median_px'] for b in r['bandes_haut_vers_bas']]}")
        print(f"    {r['lecture']}")
    (sortie / "parallaxe.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"écrit : {sortie / 'parallaxe.json'} et une planche par paire")

if __name__ == "__main__":
    main()
