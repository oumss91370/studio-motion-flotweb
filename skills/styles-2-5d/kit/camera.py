"""Caméra par stations et projection : une seule source pour Blender (bl_decor.py) et pour l'assemblage (compo.py).

Bibliothèque standard seulement. Un plan de film.py porte une liste de stations :
    cam=[(image, position (x, y, z), point visé (x, y, z), focale en mm, mode), …]
mode = "arrivee" : on arrive à cette station en freinant (départ sec, long freinage) ; "derive" : glissement régulier
jusqu'à cette station (la caméra n'est jamais immobile). Capteur de 36 mm dans la HAUTEUR de l'image.
"""
import math
import regles as R

LARG, HAUT = R.LARGEUR, R.HAUTEUR


def _frein(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def _mix(a, b, t):
    return tuple(x + (y - x) * t for x, y in zip(a, b))


def camera(plan, f):
    """(position, point visé, focale en mm) à l'image f du plan."""
    cles = plan["cam"]
    if f <= cles[0][0]:
        return cles[0][1], cles[0][2], cles[0][3]
    for (f0, p0, l0, z0, _), (f1, p1, l1, z1, mode) in zip(cles, cles[1:]):
        if f0 <= f <= f1:
            t = (f - f0) / (f1 - f0)
            if mode == "arrivee":
                t = _frein(t)
            return _mix(p0, p1, t), _mix(l0, l1, t), z0 + (z1 - z0) * t
    return cles[-1][1], cles[-1][2], cles[-1][3]


def base(plan, f):
    """(position, droite, haut, avant, focale) : le repère de la caméra, tenue à l'horizontale (pas de roulis)."""
    pos, vis, foc = camera(plan, f)
    fx, fy, fz = (vis[i] - pos[i] for i in range(3))
    n = math.sqrt(fx * fx + fy * fy + fz * fz)
    fwd = (fx / n, fy / n, fz / n)
    rx, ry = fwd[1], -fwd[0]
    n = math.sqrt(rx * rx + ry * ry) or 1.0
    right = (rx / n, ry / n, 0.0)
    up = (right[1] * fwd[2] - right[2] * fwd[1], right[2] * fwd[0] - right[0] * fwd[2], right[0] * fwd[1] - right[1] * fwd[0])
    return pos, right, up, fwd, foc


def projette(b, p):
    """Point du monde -> (x écran, y écran, profondeur en m)."""
    pos, right, up, fwd, foc = b
    d = (p[0] - pos[0], p[1] - pos[1], p[2] - pos[2])
    x = sum(u * v for u, v in zip(d, right)); y = sum(u * v for u, v in zip(d, up)); z = sum(u * v for u, v in zip(d, fwd))
    z = max(z, 1e-3)
    k = (foc / 18.0) * (HAUT / 2)
    return LARG / 2 + x / z * k, HAUT / 2 - y / z * k, z


def d_px(b, z):
    """Diamètre d'une tête de personnage (en px) à la profondeur z : l'unité de toutes les règles du style."""
    return R.D_MONDE * (b[4] / 18.0) * (HAUT / 2) / max(z, 1e-3)


def plans_de(film, f):
    """Plans actifs à l'image f, avec leur poids : un seul hors fondu, deux pendant un fondu enchaîné."""
    actifs = [k for k in film.ORDRE if film.PLANS[k]["a"] <= f < film.PLANS[k]["b"]]
    if len(actifs) < 2:
        return [(k, 1.0) for k in actifs]
    k0, k1 = actifs[0], actifs[1]
    a, b = film.PLANS[k1]["a"], film.PLANS[k0]["b"]            # le fondu dure de a à b
    t = (f - a + 0.5) / max(b - a, 1)
    return [(k0, 1 - t), (k1, t)]


def images(film, fixes=True):
    """Toutes les paires (plan, image) à rendre."""
    out = [(k, f) for k in film.ORDRE for f in range(film.PLANS[k]["a"], film.PLANS[k]["b"])]
    if fixes:
        out += [(k, film.PLANS[k]["a"]) for k in getattr(film, "FIXES", [])]
    return out
