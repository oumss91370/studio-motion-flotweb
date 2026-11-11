"""Personnages plats en pièces : dessine chaque pièce (SVG + PNG), écrit le montage (`rig.json`) et les planches.

  python outils/personnages.py

Sorties :
  personnages/svg/<nom>/<piece>.svg      la source, modifiable dans un éditeur de dessin
  personnages/png/<nom>/<piece>.png      la même pièce en PNG ×2, lue par Blender
  personnages/svg/_visages/, png/_visages/   yeux, bouches, extras (communs à tous les personnages)
  personnages/rig.json                   boîte et pivot de chaque pièce, hauteur réelle du personnage
  revue/personnages-distribution.png, revue/personnages-expressions.png

Toutes les pièces sont décrites dans un même repère de 600 × 1000 unités (pieds posés sur y = 980, axe du corps
sur x = 300). Une pièce est une liste de formes simples ; le même tableau produit le SVG et le PNG, sans autre
dépendance que Pillow.

Le kit ne dessine qu'UNE VUE : de face. Pour le trois quarts, le profil ou le dos, voir le skill `personnages`,
`references/limites-du-pantin.md`.

EXEMPLE NEUTRE À REMPLACER : « Galet » est un personnage d'exemple (tête en galet carré, yeux en traits verticaux,
blouse trapèze). Dessinez le vôtre : un personnage de chaîne doit être original et reconnaissable comme le vôtre.
"""
import json, math, pathlib, sys
from PIL import Image, ImageDraw
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import reglages as R

SVG, PNG = R.PERSONNAGES / "svg", R.PERSONNAGES / "png"
TOILE = (600, 1000)
SOL_Y = 980          # y des pieds dans le repère du dessin
ECHELLE = 2          # PNG exportés en ×2
LISSAGE = 3          # dessin en ×3 puis réduction, pour des bords propres
ENCRE = "#1F2433"    # couleur unique du contour
TRAIT = 14           # épaisseur unique du contour

# ----------------------------------------------------------------- formes
# ("ellipse", cx, cy, rx, ry, couleur)        ("rrect", x0, y0, x1, y1, rayon, couleur)
# ("poly", [(x, y), …], couleur)              ("trait", [(x, y), …], épaisseur)       ("point", cx, cy, rayon)
# Toute forme pleine reçoit le contour ENCRE d'épaisseur TRAIT ; "trait" et "point" sont à l'encre.

def _rgb(c):
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4)) + (255,)


def en_svg(formes, boite):
    x0, y0, x1, y1 = boite
    st = f'stroke="{ENCRE}" stroke-width="{TRAIT}" stroke-linejoin="round" stroke-linecap="round"'
    out = []
    for f in formes:
        k = f[0]
        if k == "ellipse":
            out.append(f'<ellipse cx="{f[1]}" cy="{f[2]}" rx="{f[3]}" ry="{f[4]}" fill="{f[5]}" {st}/>')
        elif k == "rrect":
            out.append(f'<rect x="{f[1]}" y="{f[2]}" width="{f[3] - f[1]}" height="{f[4] - f[2]}" rx="{f[5]}" fill="{f[6]}" {st}/>')
        elif k == "poly":
            pts = " ".join(f"{x},{y}" for x, y in f[1])
            out.append(f'<polygon points="{pts}" fill="{f[2]}" {st}/>')
        elif k == "trait":
            pts = " ".join(f"{x},{y}" for x, y in f[1])
            out.append(f'<polyline points="{pts}" fill="none" stroke="{ENCRE}" stroke-width="{f[2]}" stroke-linejoin="round" stroke-linecap="round"/>')
        elif k == "point":
            out.append(f'<circle cx="{f[1]}" cy="{f[2]}" r="{f[3]}" fill="{ENCRE}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x0} {y0} {x1 - x0} {y1 - y0}" '
            f'width="{(x1 - x0) * ECHELLE}" height="{(y1 - y0) * ECHELLE}">\n  ' + "\n  ".join(out) + "\n</svg>\n")


def en_png(formes, boite):
    x0, y0, x1, y1 = boite
    s = ECHELLE * LISSAGE
    im = Image.new("RGBA", ((x1 - x0) * s, (y1 - y0) * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    X = lambda x: (x - x0) * s
    Y = lambda y: (y - y0) * s
    encre, t = _rgb(ENCRE), TRAIT * s

    def ligne(pts, w, ferme=False):
        p = [(X(x), Y(y)) for x, y in pts]
        if ferme:
            p = p + [p[0], p[1]]
        d.line(p, fill=encre, width=int(w), joint="curve")
        for x, y in p:                      # bouts et angles ronds
            d.ellipse((x - w / 2, y - w / 2, x + w / 2, y + w / 2), fill=encre)

    for f in formes:
        k = f[0]
        if k == "ellipse":
            _, cx, cy, rx, ry, c = f
            d.ellipse((X(cx - rx), Y(cy - ry), X(cx + rx), Y(cy + ry)), fill=_rgb(c))
            h = TRAIT / 2
            d.ellipse((X(cx - rx - h), Y(cy - ry - h), X(cx + rx + h), Y(cy + ry + h)), outline=encre, width=int(t))
        elif k == "rrect":
            _, a, b, c2, e, r, c = f
            d.rounded_rectangle((X(a), Y(b), X(c2), Y(e)), radius=r * s, fill=_rgb(c))
            h = TRAIT / 2
            d.rounded_rectangle((X(a - h), Y(b - h), X(c2 + h), Y(e + h)), radius=(r + h) * s, outline=encre, width=int(t))
        elif k == "poly":
            d.polygon([(X(x), Y(y)) for x, y in f[1]], fill=_rgb(f[2]))
            ligne(f[1], t, ferme=True)
        elif k == "trait":
            ligne(f[1], f[2] * s)
        elif k == "point":
            _, cx, cy, r = f
            d.ellipse((X(cx - r), Y(cy - r), X(cx + r), Y(cy + r)), fill=encre)
    return im.resize(((x1 - x0) * ECHELLE, (y1 - y0) * ECHELLE), Image.LANCZOS)


def arc(cx, cy, rx, ry, a0, a1, n=12):
    """Points d'un arc d'ellipse (angles en degrés, 0 = droite, 90 = bas)."""
    return [(round(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)), 1),
             round(cy + ry * math.sin(math.radians(a0 + (a1 - a0) * i / n)), 1)) for i in range(n + 1)]


# ----------------------------------------------------------------- le personnage d'exemple
PERSOS = {
    # h : hauteur réelle en mètres, du sol au sommet du dessin. Un figurant = une autre entrée, d'autres couleurs.
    "galet": dict(h=1.50, tete="#EFE4CF", blouse="#2F8F83", poche="#49AD9E", jambes="#2B3A4A", coiffe="#E0683A"),
}


def pieces(c):
    """Pièces d'un personnage : nom -> (formes, boîte, pivot). Le pivot est le point autour duquel la pièce tourne."""
    P = {}
    P["jambes"] = ([("rrect", 232, 790, 282, 962, 22, c["jambes"]), ("rrect", 318, 790, 368, 962, 22, c["jambes"]),
                    ("ellipse", 252, 955, 36, 18, c["jambes"]), ("ellipse", 348, 955, 36, 18, c["jambes"])],
                   (190, 770, 410, 990), (300, SOL_Y))
    P["corps"] = ([("poly", [(224, 500), (376, 500), (424, 850), (176, 850)], c["blouse"]),
                   ("rrect", 300, 700, 362, 772, 12, c["poche"])],
                  (150, 480, 450, 870), (300, 850))
    for nom, x in (("bras_g", 196), ("bras_d", 404)):
        P[nom] = ([("rrect", x - 30, 525, x + 30, 762, 30, c["blouse"]), ("ellipse", x, 772, 30, 30, c["tete"])],
                  (x - 60, 500, x + 60, 820), (x, 548))
    P["tete"] = ([("rrect", 118, 222, 482, 486, 78, c["tete"]),
                  ("ellipse", 300, 226, 148, 50, c["coiffe"]), ("trait", [(300, 180), (316, 158)], 16)],
                 (95, 140, 505, 505), (300, 490))
    return P


# Visages : communs à tous les personnages, échangés image par image (un seul visible à la fois).
BOITE_YEUX = (170, 285, 430, 400)
BOITE_BOUCHE = (230, 395, 370, 470)
BOITE_EXTRA = (380, 220, 500, 340)
YEUX = {
    "neutre":  [("trait", [(240, 318), (240, 366)], 20), ("trait", [(360, 318), (360, 366)], 20)],
    "cote":    [("trait", [(268, 318), (268, 366)], 20), ("trait", [(388, 318), (388, 366)], 20)],
    "grands":  [("ellipse", 240, 342, 24, 32, "#FFFFFF"), ("point", 240, 342, 10),
                ("ellipse", 360, 342, 24, 32, "#FFFFFF"), ("point", 360, 342, 10)],
    "plisses": [("trait", [(240, 334), (240, 352)], 20), ("trait", [(360, 334), (360, 352)], 20)],
    "fermes":  [("trait", [(216, 346), (264, 346)], 16), ("trait", [(336, 346), (384, 346)], 16)],
}
BOUCHES = {
    "fermee":  [("trait", [(278, 430), (322, 430)], 13)],
    "ouverte": [("ellipse", 300, 432, 18, 22, "#6B2F2F")],
    "sourire": [("trait", arc(300, 418, 36, 24, 20, 160), 13)],
    "moue":    [("trait", arc(300, 448, 30, 18, 200, 340), 13)],
}
EXTRAS = {
    "goutte":  [("poly", [(440, 240), (462, 290), (440, 312), (418, 290)], "#9FD3F0")],
}


def main():
    rig = {"toile": list(TOILE), "sol_y": SOL_Y, "echelle": ECHELLE, "vues": ["face"], "persos": {}, "visages": {}}
    img = {}

    def sauver(dossier, nom, formes, boite):
        (SVG / dossier).mkdir(parents=True, exist_ok=True)
        (PNG / dossier).mkdir(parents=True, exist_ok=True)
        (SVG / dossier / f"{nom}.svg").write_text(en_svg(formes, boite), encoding="utf-8")
        im = en_png(formes, boite)
        im.save(PNG / dossier / f"{nom}.png")
        return im

    for fam, table, boite in (("yeux", YEUX, BOITE_YEUX), ("bouche", BOUCHES, BOITE_BOUCHE), ("extra", EXTRAS, BOITE_EXTRA)):
        for k, formes in table.items():
            img[f"{fam}_{k}"] = sauver("_visages", f"{fam}_{k}", formes, boite)
            rig["visages"][f"{fam}_{k}"] = {"boite": list(boite)}
    for nom, c in PERSOS.items():
        P = pieces(c)
        haut = min(b[1] for _, b, _ in P.values())
        rig["persos"][nom] = {"h": c["h"], "haut_y": haut, "pieces": {}}
        for pn, (formes, boite, pivot) in P.items():
            img[f"{nom}/{pn}"] = sauver(nom, pn, formes, boite)
            rig["persos"][nom]["pieces"][pn] = {"boite": list(boite), "pivot": list(pivot)}
    (R.PERSONNAGES / "rig.json").write_text(json.dumps(rig, indent=1), encoding="utf-8")

    # ---------- planches de contrôle
    def compose(nom, yeux="neutre", bouche="fermee", extra=None):
        im = Image.new("RGBA", (TOILE[0] * ECHELLE, TOILE[1] * ECHELLE), (0, 0, 0, 0))
        def pose(cle, boite):
            im.alpha_composite(img[cle], (boite[0] * ECHELLE, boite[1] * ECHELLE))
        P = rig["persos"][nom]["pieces"]
        for pn in ("jambes", "corps", "tete"):
            pose(f"{nom}/{pn}", P[pn]["boite"])
        pose("yeux_" + yeux, BOITE_YEUX)
        pose("bouche_" + bouche, BOITE_BOUCHE)
        if extra:
            pose("extra_" + extra, BOITE_EXTRA)
        for pn in ("bras_g", "bras_d"):
            pose(f"{nom}/{pn}", P[pn]["boite"])
        return im

    R.REVUE.mkdir(parents=True, exist_ok=True)
    FOND = (226, 222, 212, 255)
    noms = list(PERSOS)
    planche = Image.new("RGBA", (300 * len(noms), 500), FOND)
    for i, n in enumerate(noms):
        planche.alpha_composite(compose(n).resize((300, 500), Image.LANCZOS), (i * 300, 0))
    planche.convert("RGB").save(R.REVUE / "personnages-distribution.png")

    combos = [(y, "fermee", None) for y in YEUX] + [("neutre", b, None) for b in BOUCHES] + \
             [("grands", "ouverte", None), ("plisses", "sourire", None), ("grands", "moue", "goutte")]
    cols, cw = 4, 300
    rows = (len(combos) + cols - 1) // cols
    sh = Image.new("RGBA", (cw * cols, cw * rows), FOND)
    for i, (y, b, e) in enumerate(combos):
        tete = compose(noms[0], y, b, e).crop((60 * ECHELLE, 120 * ECHELLE, 540 * ECHELLE, 600 * ECHELLE)).resize((cw, cw), Image.LANCZOS)
        sh.alpha_composite(tete, ((i % cols) * cw, (i // cols) * cw))
    sh.convert("RGB").save(R.REVUE / "personnages-expressions.png")
    print(f"pièces : {len(img)} | personnages : {len(PERSOS)} | yeux : {len(YEUX)} | bouches : {len(BOUCHES)} | extras : {len(EXTRAS)}")
    print("écrit :", R.PERSONNAGES / "rig.json", "et", R.REVUE / "personnages-*.png")


if __name__ == "__main__":
    main()
