"""Rendre vite : une image de décor par plan (une « plaque ») au lieu d'une par image du film.

Les personnages sont dessinés en 2D et posés à l'assemblage : tant que la caméra ne fait que glisser un peu, zoomer ou pivoter,
le décor n'a pas besoin d'être recalculé à chaque image. Ce module classe chaque plan d'après sa caméra et dit quoi rendre.

Modes (clé "mode" d'un plan pour forcer, sinon choix automatique par classer()) :
  "fixe"     la caméra ne bouge pas : une plaque, recopiée ;
  "plaque"   glissé court, zoom, léger pivot : une plaque plus large et plus fine que le cadre, recadrée par une homographie ;
  "couches"  déplacement moyen : la même plaque, mais chaque pixel est déplacé selon SA profondeur (la passe de données la donne) :
             c'est l'équivalent continu de 2 à 4 couches de profondeur ; ce qui était caché derrière un objet proche est étiré ;
  "3d"       vrai déplacement à forte parallaxe, ou décor animé (clé anime=True) : rendu image par image, comme avant.

La mesure qui décide est la PARALLAXE du plan, en pixels : de combien un objet proche glisse par rapport au lointain entre la pose
de la plaque et la pose la plus éloignée de la caméra. Seuils : regles.PLAQUE (réglés par l'essai chronométré du studio).
Bibliothèque standard pour classer() et plaque() (lus dans Blender) ; numpy et OpenCV seulement pour reprojeter(). Écrit par Flot Web.
"""
import math, os
import regles as R
import camera as C

W, H = R.LARGEUR, R.HAUTEUR


def _sub(a, b):
    return tuple(x - y for x, y in zip(a, b))

def _dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def classer(plan, bases, z_sujet, z_proche=None):
    """Classe un plan. bases : {image: base de caméra} ; z_sujet : distance du sujet (m) ; z_proche : distance du décor le plus proche
    dans le champ (par défaut 0,6 × la distance du sujet). Renvoie dict(mode, parallaxe_px, image_ref, raison)."""
    P = R.PLAQUE
    fs = sorted(bases)
    cx = [sum(bases[f][0][i] for f in fs) / len(fs) for i in range(3)]
    ref = min(fs, key=lambda f: sum((bases[f][0][i] - cx[i]) ** 2 for i in range(3)))      # la pose la plus centrale : elle minimise le trajet à rattraper
    b0 = bases[ref]
    zp = z_proche or plan.get("proche") or 0.6 * z_sujet
    par = 0.0
    for f in fs:
        pos, right, up, fwd, foc = bases[f]
        k = (foc / 18.0) * (H / 2)
        t = _sub(pos, b0[0])
        lat = math.hypot(_dot(t, b0[1]), _dot(t, b0[2]))            # déplacement de côté : un objet à z glisse de k × lat / z
        av = abs(_dot(t, b0[3]))                                    # avancée : il s'écarte du centre de r × av / z (r = demi-diagonale)
        par = max(par, (k * lat + 0.5 * math.hypot(W, H) * av) / zp)
    bouge = max(max(abs(a - b) for a, b in zip(bases[f][0], b0[0])) for f in fs) > 1e-4 or \
        max(max(abs(a - b) for a, b in zip(bases[f][3], b0[3])) for f in fs) > 1e-5 or max(abs(bases[f][4] - b0[4]) for f in fs) > 1e-3
    if os.environ.get("EPISODE_MODE"):
        mode, raison = os.environ["EPISODE_MODE"], "forcé par la variable EPISODE_MODE"
    elif plan.get("mode"):
        mode, raison = plan["mode"], "forcé dans la liste de plans"
    elif plan.get("anime"):
        mode, raison = "3d", "le décor bouge dans ce plan"
    elif not bouge:
        mode, raison = "fixe", "caméra immobile"
    elif par <= P["seuil_plaque_px"]:
        mode, raison = "plaque", f"parallaxe de {par:.1f} px, sous {P['seuil_plaque_px']} px"
    elif par <= P["seuil_couches_px"]:
        mode, raison = "couches", f"parallaxe de {par:.1f} px, entre {P['seuil_plaque_px']} et {P['seuil_couches_px']} px"
    else:
        mode, raison = "3d", f"parallaxe de {par:.1f} px, au-dessus de {P['seuil_couches_px']} px"
    return dict(mode=mode, parallaxe_px=round(par, 1), image_ref=ref, raison=raison)


def plaque(bases, image_ref, z_sujet):
    """Caméra de la plaque : la pose de l'image de référence, une focale plus courte (marge pour le mouvement) et une taille plus
    grande (assez de pixels pour le zoom le plus fort). Renvoie dict(base, focale, echelle, taille)."""
    P = R.PLAQUE
    pos, right, up, fwd, foc = bases[image_ref]
    tx = ty = 0.0
    kmax = 0.0
    for f, (p, r, u, w, fo) in bases.items():
        k = (fo / 18.0) * (H / 2)
        kmax = max(kmax, k)
        for xn, yn in ((-1, -1), (1, -1), (1, 1), (-1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)):
            d = tuple(w[i] + xn * (W / 2) / k * r[i] + yn * (H / 2) / k * u[i] for i in range(3))
            for dist in (0.5 * z_sujet, z_sujet, 40.0 * z_sujet):        # le bord du cadre, vu à trois profondeurs
                v = tuple(p[i] + dist * d[i] - pos[i] for i in range(3))
                z = _dot(v, fwd)
                if z > 1e-3:
                    tx, ty = max(tx, abs(_dot(v, right)) / z), max(ty, abs(_dot(v, up)) / z)
    t = max(ty, tx * H / W) * (1 + P["marge"])
    focale = 18.0 / t
    echelle = min(P["echelle_max"], max(1.0, kmax / ((focale / 18.0) * (H / 2))))
    return dict(base=(pos, right, up, fwd, focale), focale=focale, echelle=round(echelle, 3),
                taille=(int(round(W * echelle / 2)) * 2, int(round(H * echelle / 2)) * 2))


def troncons(plan, base_de, z_sujet, fusion=True):
    """Découpe un plan en tronçons de caméra et classe chacun. Un plan enchaîne des DÉPLACEMENTS (une dizaine d'images, forte
    parallaxe : rendus en 3D) et des TENUES en dérive (faible parallaxe : une plaque). On coupe aux stations de la caméra, puis on
    réunit les tronçons voisins tant que la parallaxe de l'ensemble reste sous le seuil des couches.
    base_de(image) -> base de caméra. Renvoie une liste de dict(a, b, mode, parallaxe_px, image_ref, raison[, base, focale, echelle, taille])."""
    a0, b0 = plan["a"], plan["b"]
    cles = sorted(set([a0, b0] + [c[0] for c in plan["cam"] if a0 < c[0] < b0]))
    morceaux = [(a, b) for a, b in zip(cles, cles[1:])]
    def classe(a, b):
        bases = {f: base_de(f) for f in range(a, b)}
        c = classer(plan, bases, z_sujet)
        c.update(a=a, b=b)
        return c, bases
    out = []
    i = 0
    while i < len(morceaux):
        a, b = morceaux[i]
        c, bases = classe(a, b)
        while fusion and c["mode"] != "3d" and i + 1 < len(morceaux):          # on essaie d'avaler le tronçon suivant
            c2, bases2 = classe(a, morceaux[i + 1][1])
            if c2["mode"] == "3d" or plan.get("mode") or os.environ.get("EPISODE_MODE"):
                break
            c, bases, b = c2, bases2, morceaux[i + 1][1]
            i += 1
        if c["mode"] != "3d":
            c.update(plaque(bases, c["image_ref"], z_sujet))
        out.append(c)
        i += 1
    return out


def preparer(film):
    """Pour chaque plan du film : la liste de ses tronçons (mode, parallaxe, plaque à rendre). {plan: [tronçon, …]}."""
    out = {}
    for k in list(film.ORDRE) + list(getattr(film, "FIXES", [])):
        plan = film.PLANS[k]
        zs = []
        for f in (plan["a"], (plan["a"] + plan["b"]) // 2, plan["b"] - 1):
            act = film.acteurs(k, f)
            pts = [(p[0], p[1], 0.9) for _, p, _ in act] or [film.mise_au_point(k, f)]
            zs.append(min(C.projette(C.base(plan, f), q)[2] for q in pts))
        z_sujet = min(zs)
        ts = troncons(plan, lambda f: C.base(plan, f), z_sujet)
        for i, t in enumerate(ts):
            t.update(nom=f"{k}p{i}", z_sujet=round(z_sujet, 2))
        out[k] = ts
    return out


def troncon_de(liste, f):
    """Le tronçon qui contient l'image f."""
    for t in liste:
        if t["a"] <= f < t["b"]:
            return t
    return liste[-1]


def reprojeter(couches, z_p, base_p, base_t, taille_t=(W, H), profondeur=True, z_plan=None, tours=4):
    """Recadre la plaque pour la caméra base_t. couches : liste d'images (H, W[, c]) de la plaque ; z_p : sa profondeur (m).
    profondeur=False : homographie sur le plan du sujet (mode "plaque") ; True : chaque pixel est déplacé selon sa profondeur
    (mode "couches"). Renvoie (liste d'images recadrées, profondeur vue de base_t, part du cadre tombée hors de la plaque)."""
    import numpy as np
    import cv2
    Wt, Ht = taille_t
    Hp, Wp = z_p.shape[:2]
    pp, rp, up_, fp, focp = base_p
    pt, rt, ut, ft, foct = base_t
    kp = (focp / 18.0) * (Hp / 2)
    kt = (foct / 18.0) * (Ht / 2)
    xx, yy = np.meshgrid((np.arange(Wt, dtype=np.float32) + 0.5 - Wt / 2) / kt, (Ht / 2 - np.arange(Ht, dtype=np.float32) - 0.5) / kt)
    ray = [ft[i] + xx * rt[i] + yy * ut[i] for i in range(3)]              # composante 1 le long de l'axe de la caméra cible
    dc = [pt[i] - pp[i] for i in range(3)]
    a = [sum(ray[i] * v[i] for i in range(3)) for v in (rp, up_, fp)]      # le rayon, dans le repère de la plaque
    b = [sum(dc[i] * v[i] for i in range(3)) for v in (rp, up_, fp)]       # le déplacement de la caméra, dans ce repère

    def source(d):
        zs = np.maximum(b[2] + d * a[2], 1e-3)
        return (Wp / 2 + (b[0] + d * a[0]) / zs * kp - 0.5).astype(np.float32), (Hp / 2 - (b[1] + d * a[1]) / zs * kp - 0.5).astype(np.float32), zs

    d = np.full((Ht, Wt), float(z_plan or np.median(z_p)), np.float32)
    if profondeur:
        for _ in range(tours):                                             # point fixe : la profondeur lue dans la plaque doit être celle du point visé
            xs, ys, zs = source(d)
            lu = cv2.remap(z_p, xs, ys, cv2.INTER_NEAREST, borderMode=cv2.BORDER_REPLICATE)
            d = np.clip(d * lu / zs, 0.02, 1e5).astype(np.float32)
    xs, ys, zs = source(d)
    out = []
    for im in couches:
        if kp > 1.6 * kt:                                                  # plaque bien plus fine que le cadre : on la lisse avant de l'échantillonner
            im = cv2.GaussianBlur(im, (0, 0), 0.5 * (kp / kt - 1.0))
        out.append(cv2.remap(im, xs, ys, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE))
    lu = cv2.remap(z_p, xs, ys, cv2.INTER_NEAREST, borderMode=cv2.BORDER_REPLICATE)
    z_t = lu * (d / np.maximum(zs, 1e-3))                                  # profondeur le long de l'axe de la caméra cible
    hors = float(((xs < 0) | (xs > Wp - 1) | (ys < 0) | (ys > Hp - 1)).mean())
    return out, z_t.astype(np.float32), hors
