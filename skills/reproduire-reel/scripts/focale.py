#!/usr/bin/env python3
"""Focale apparente d'une image par ses points de fuite.

  python focale.py <image> [<image> ...] [--bande y0,y1] [--sortie focale.json]
      image : un fichier, ou « video.mp4@1650 » (image 1650 de la vidéo)
      --bande : bande horizontale ignorée (les sous-titres), en pixels

Méthode : segments droits (Canny puis Hough), point de fuite des verticales et point de fuite d'une famille d'horizontales
(RANSAC), puis f² = −(v1 − c)·(v2 − c), c = centre de l'image.
Sort pour chaque image : points de fuite, focale en px et en mm pour un capteur de 36 mm sur la HAUTEUR de l'image (la
convention d'une caméra 3D en format vertical), champ vertical, tangage de la caméra, convergence des verticales en degrés
entre les deux bords de l'image.

Limite : il faut que les verticales CONVERGENT (caméra levée ou baissée de quelques degrés) et qu'une famille de fuyantes
soit visible (une façade, un plancher). Caméra tenue à l'horizontale : focale non calculable, on ne lit que la convergence
(moins de 2° = caméra à l'horizontale). Vérifier que « verticales_accordees » et « horizontales_accordees » dépassent 15
segments avant de croire le chiffre, et le refaire sur une deuxième image.
Dépendances : Python 3.9+, numpy, Pillow, opencv-python. Écrit par Flot Web.
"""
import sys
sys.dont_write_bytecode = True
import argparse, json, math, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np
import cv2
import mp_base as B

def segments(img, bande=None):
    h, w = img.shape[:2]
    e = w / 1080                                        # seuils réglés sur une image de 1 080 px de large
    g = cv2.GaussianBlur(B.luma(img), (0, 0), 1.2).astype(np.uint8)
    c = cv2.Canny(g, 30, 90)
    if bande:
        c[max(0, int(bande[0])):max(0, int(bande[1]))] = 0
    s = cv2.HoughLinesP(c, 1, np.pi / 360, max(20, int(round(60 * e))), minLineLength=max(30, int(round(90 * e))), maxLineGap=max(3, int(round(6 * e))))
    return np.zeros((0, 4)) if s is None else s[:, 0, :].astype(np.float64)

def _droites(seg):
    p = np.c_[seg[:, :2], np.ones(len(seg))]; q = np.c_[seg[:, 2:], np.ones(len(seg))]
    L = np.cross(p, q)
    return L / np.linalg.norm(L[:, :2], axis=1, keepdims=True)

def point_de_fuite(seg, essais=3000, tol=2.0, graine=1):
    """RANSAC : point où passent le plus de segments (écart angulaire entre le segment et la direction du point, en degrés)."""
    if len(seg) < 4:
        return None, 0
    rng = np.random.default_rng(graine)
    L = _droites(seg)
    mil = (seg[:, :2] + seg[:, 2:]) / 2
    dirs = seg[:, 2:] - seg[:, :2]; dirs /= np.linalg.norm(dirs, axis=1, keepdims=True)
    lon = np.linalg.norm(seg[:, 2:] - seg[:, :2], axis=1)
    def ecart(v):
        d = v[None] - mil; d /= np.linalg.norm(d, axis=1, keepdims=True) + 1e-9
        return np.degrees(np.arcsin(np.clip(np.abs(dirs[:, 0] * d[:, 1] - dirs[:, 1] * d[:, 0]), 0, 1)))
    best, bs = None, -1
    for _ in range(essais):
        i, j = rng.choice(len(seg), 2, replace=False)
        v = np.cross(L[i], L[j])
        if abs(v[2]) < 1e-9:
            continue
        v = v[:2] / v[2]
        sc = lon[ecart(v) < tol].sum()
        if sc > bs:
            best, bs = v, sc
    if best is None:
        return None, 0
    return best, int((ecart(best) < tol).sum())

def analyser(chemin, bande=None):
    img = B.lire(chemin)
    h, w = img.shape[:2]
    seg = segments(img, bande)
    out = dict(image=pathlib.Path(str(chemin)).name, taille=[w, h], segments=int(len(seg)))
    if not len(seg):
        out["focale"] = "non calculable (aucun segment droit trouvé)"
        return out
    ang = np.degrees(np.arctan2(seg[:, 2] - seg[:, 0], seg[:, 3] - seg[:, 1]))        # 0 = vertical
    ang = (ang + 90) % 180 - 90
    vert = seg[np.abs(ang) < 22]
    hori = seg[np.abs(ang) > 35]
    out.update(verticales=int(len(vert)), autres=int(len(hori)))
    pv, nv = point_de_fuite(vert)
    ph, nh = point_de_fuite(hori)
    c = np.array([w / 2, h / 2])
    if pv is not None:
        out["fuite_verticales"] = [round(float(pv[0])), round(float(pv[1]))]; out["verticales_accordees"] = nv
        a = [math.degrees(math.atan2(pv[0] - x, pv[1] - h / 2)) for x in (0, w)]     # verticales du bord gauche et du bord droit, à mi-hauteur
        d = abs(a[0] - a[1]) % 180
        out["convergence_bord_a_bord_deg"] = round(min(d, 180 - d), 2)
    if ph is not None:
        out["fuite_horizontales"] = [round(float(ph[0])), round(float(ph[1]))]; out["horizontales_accordees"] = nh
    if pv is not None and ph is not None:
        f2 = -float((pv - c) @ (ph - c))
        if f2 > 0:
            f = math.sqrt(f2)
            out.update(focale_px=round(f), focale_mm_capteur36_vertical=round(f * 36 / h, 1), champ_vertical_deg=round(2 * math.degrees(math.atan(h / 2 / f)), 1),
                       tangage_deg=round(math.degrees(math.atan2(f, abs(pv[1] - c[1]))) * (1 if pv[1] > c[1] else -1), 1))
            if min(nv, nh) < 15:
                out["avertissement"] = "moins de 15 segments accordés sur un des deux points de fuite : chiffre fragile, à confirmer sur une autre image"
        else:
            out["focale"] = "non calculable (points de fuite du même côté du centre : caméra à l'horizontale, ou segments mal accordés)"
    else:
        out.setdefault("focale", "non calculable (un point de fuite manque)")
    return out

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("images", nargs="+"); ap.add_argument("--bande"); ap.add_argument("--sortie")
    a = ap.parse_args()
    bande = [int(v) for v in a.bande.split(",")] if a.bande else None
    res = []
    for p in a.images:
        try:
            r = analyser(p, bande)
        except (OSError, ValueError) as e:
            r = dict(image=str(p), erreur=str(e))
        res.append(r); print(json.dumps(r, ensure_ascii=False))
    if a.sortie:
        pathlib.Path(a.sortie).parent.mkdir(parents=True, exist_ok=True)
        pathlib.Path(a.sortie).write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")

if __name__ == "__main__":
    main()
