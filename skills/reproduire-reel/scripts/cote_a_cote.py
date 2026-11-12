#!/usr/bin/env python3
"""Planche de comparaison côte à côte, avec recadrages agrandis au plus proche voisin (on voit les pixels d'origine).

Deux usages.
  1. Rapide, un seul élément, deux colonnes :
     python cote_a_cote.py --ref <image> --nous <image> -o planche.jpg [--zoom-ref cx,cy,demi] [--zoom-nous cx,cy,demi] [--k 4]
  2. Planche complète décrite dans un fichier (deux ou trois colonnes, une ligne par plan ou par détail) :
     python cote_a_cote.py <planche.json>
     { "sortie": "revue/comparaison.jpg",
       "colonnes": ["RÉFÉRENCE", "AVANT", "APRÈS"],
       "hauteur_vignette": 768, "cote_zoom": 220, "agrandissement": 3,
       "lignes": [ { "titre": "Plan 3 : le personnage se retourne",
                     "images": ["reference.mp4@395", "rendu_v1/f_0233.jpg", "rendu_v2/f_0233.jpg"],
                     "zooms":  [[515, 890], [540, 700], [540, 700]],          centre du recadrage dans chaque image ; null = pas de zoom
                     "notes":  ["réf. i395", "avant", "après"] } ] }
Une image s'écrit « fichier.png » ou « video.mp4@numéro d'image ». Les chemins sont relatifs au dossier du fichier .json.
La planche à trois colonnes « référence / avant / après » est celle qu'on montre au critique indépendant et au client.
Dépendances : Python 3.9+, Pillow, numpy, FFmpeg (pour video@numéro). Écrit par Flot Web.
"""
import sys
sys.dont_write_bytecode = True
import argparse, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from PIL import Image, ImageDraw
import mp_base as B

FOND = (24, 22, 28)

def _ouvrir(chemin, base):
    c = str(chemin)
    f, suite = (c.rsplit("@", 1)[0], "@" + c.rsplit("@", 1)[1]) if "@" in c and c.rsplit("@", 1)[1].isdigit() else (c, "")
    p = pathlib.Path(f)
    if not p.is_absolute():
        p = pathlib.Path(base) / p
    return B.ouvrir(str(p) + suite)

def _zoom(im, centre, cote, k):
    cx, cy = centre[:2]
    demi = (centre[2] if len(centre) > 2 else cote / 2)
    x0 = int(max(0, min(im.width - 2 * demi, cx - demi))); y0 = int(max(0, min(im.height - 2 * demi, cy - demi)))
    c = im.crop((x0, y0, int(x0 + 2 * demi), int(y0 + 2 * demi)))
    return c.resize((c.width * k, c.height * k), Image.NEAREST), (x0, y0, int(x0 + 2 * demi), int(y0 + 2 * demi))

def planche(spec, base="."):
    cols = spec.get("colonnes") or ["RÉFÉRENCE", "NOUS"]
    hv = int(spec.get("hauteur_vignette", 768)); cote = int(spec.get("cote_zoom", 220)); k = int(spec.get("agrandissement", 3))
    pad, tit = 14, 46
    gras, fin = B.police(26, True), B.police(18)
    rangs = []
    for li in spec["lignes"]:
        cases = []
        zooms = li.get("zooms") or [None] * len(li["images"])
        notes = li.get("notes") or [""] * len(li["images"])
        for i, ch in enumerate(li["images"]):
            if ch is None:
                cases.append(Image.new("RGB", (10, hv + 30), FOND)); continue
            im = _ouvrir(ch, base)
            lv = int(round(im.width * hv / im.height))
            vign = im.resize((lv, hv), Image.LANCZOS)
            z = zooms[i] if i < len(zooms) else None
            if z:
                zi, (x0, y0, x1, y1) = _zoom(im, z, cote, li.get("agrandissement", k))
                e = hv / im.height
                ImageDraw.Draw(vign).rectangle((x0 * e, y0 * e, x1 * e, y1 * e), outline=(255, 230, 0), width=2)
                case = Image.new("RGB", (lv + pad + zi.width, max(hv, zi.height) + 30), FOND)
                case.paste(vign, (0, 0)); case.paste(zi, (lv + pad, 0))
                note = (notes[i] if i < len(notes) else "") + f" · recadrage ×{li.get('agrandissement', k)} (pixels d'origine)"
            else:
                case = Image.new("RGB", (lv, hv + 30), FOND); case.paste(vign, (0, 0)); note = notes[i] if i < len(notes) else ""
            ImageDraw.Draw(case).text((4, case.height - 26), note, fill=(200, 200, 205), font=fin)
            cases.append(case)
        rangs.append((li.get("titre", ""), cases))
    larg = [max(r[1][i].width for r in rangs if i < len(r[1])) for i in range(len(cols))]
    W = sum(larg) + pad * (len(cols) + 1)
    H = 70 + sum(tit + max(c.height for c in r[1]) + pad for r in rangs)
    pl = Image.new("RGB", (W, H), FOND); d = ImageDraw.Draw(pl)
    x = pad
    for i, t in enumerate(cols):
        d.text((x + larg[i] / 2, 22), t, fill=(255, 255, 255), font=gras, anchor="ma"); x += larg[i] + pad
    y = 70
    for titre, cases in rangs:
        d.text((pad, y + 8), titre, fill=(255, 214, 110), font=gras)
        x = pad
        for i, c in enumerate(cases):
            pl.paste(c, (x, y + tit)); x += larg[i] + pad
        y += tit + max(c.height for c in cases) + pad
    sortie = pathlib.Path(spec["sortie"])
    if not sortie.is_absolute():
        sortie = pathlib.Path(base) / sortie
    sortie.parent.mkdir(parents=True, exist_ok=True)
    pl.save(sortie, quality=90)
    return sortie, pl.size

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", nargs="?"); ap.add_argument("--ref"); ap.add_argument("--nous"); ap.add_argument("-o", "--sortie")
    ap.add_argument("--zoom-ref"); ap.add_argument("--zoom-nous"); ap.add_argument("--k", type=int, default=4); ap.add_argument("--titre", default="")
    a = ap.parse_args()
    if a.spec:
        f = pathlib.Path(a.spec)
        s, t = planche(json.loads(f.read_text(encoding="utf-8-sig")), f.parent)
    elif a.ref and a.nous and a.sortie:
        z = lambda v: [float(x) for x in v.split(",")] if v else None
        s, t = planche(dict(sortie=a.sortie, colonnes=["RÉFÉRENCE", "NOUS"], agrandissement=a.k,
                            lignes=[dict(titre=a.titre, images=[a.ref, a.nous], zooms=[z(a.zoom_ref), z(a.zoom_nous)], notes=[a.ref, a.nous])]))
    else:
        ap.error("donner un fichier de planche, ou --ref, --nous et -o")
    print(s, t)

if __name__ == "__main__":
    main()
