"""Mesure d'une forme cernée d'un trait : contour (épaisseur du trait selon l'orientation du bord, couleur, dureté du bord)
et ombrage du remplissage (zones, frontière, profils de luminance, reflets, liseré, grain), plus les détails dessinés dedans.

La forme est désignée par une cible (voir references/fichier-de-cibles.md) :
  cercle     {"type": "cercle", "centre": [x, y], "rayon": r}            modèle : un cercle est ajusté, ce qui s'en écarte est écarté
  ellipse    {"type": "ellipse", "centre": [x, y], "axes": [a, b], "angle": 0}    modèle : une ellipse est ajustée
  rectangle  {"type": "rectangle", "boite": [x0, y0, x1, y1]}            lasso : on cherche le remplissage dans la boîte
  polygone   {"type": "polygone", "points": [[x, y], …]}                 lasso
  masque     {"type": "masque", "fichier": "masque.png"}                 lasso (blanc = dedans), image de la taille de l'image mesurée

Méthode du contour (la même pour toutes les formes)
  1. le remplissage est la zone de couleur proche de celle lue à la graine, limitée par le trait ;
  2. le long de son bord, tous les pixels (ou tous les degrés pour un cercle), une coupe est lue en travers du bord, dans la
     direction de la normale, tous les 0,25 px (interpolation bilinéaire) ;
  3. bord intérieur du trait = passage à mi-chemin entre la couleur du remplissage (palier lu 3 à 10 px dedans) et celle de
     l'encre ; bord extérieur = passage à mi-chemin entre l'encre et le décor (palier lu 3 à 10 px dehors).
     Épaisseur = bord extérieur − bord intérieur. Largeur de transition = distance entre 10 % et 90 % ;
  4. chaque coupe est rangée selon l'ORIENTATION de la normale (0° = le bord regarde à droite, 90° = en haut, 180° = à gauche,
     270° = en bas). Valeur publiée tous les 5° = médiane des coupes à ±2,5°. Pour un cercle, c'est l'angle autour du centre ;
  5. une coupe est écartée, avec son motif, si un autre objet passe devant la forme, si le décor est aussi sombre que le trait,
     si le remplissage est trop étroit, ou si la cible la coupe.
Écrit par Flot Web (skill `reproduire-reel`), d'après les scripts de mesure du prototype 2.5D du studio.
"""
import sys
sys.dont_write_bytecode = True
import math
import numpy as np
import cv2
from PIL import Image, ImageDraw
import mp_base as B

PAS = 0.25
K3, K10, K15 = int(3 / PAS), int(10 / PAS), int(1.5 / PAS)
SEUIL_INTERIEUR, SEUIL_SORTIE = 70.0, 60.0     # écarts de couleur (RVB, 0–441) : palier minimal côté remplissage et décor ; sortie du trait

def _r(v, n=1):
    try:
        v = float(v)
    except (TypeError, ValueError):
        return None
    return None if not np.isfinite(v) else round(v, n)

# ====================================================================== cible -> lasso, graine, remplissage
def _lasso(forme, H, W, dossier=None):
    """Masque (uint8) de la zone où chercher le remplissage, et graine par défaut."""
    t = forme.get("type", "cercle")
    m = np.zeros((H, W), np.uint8)
    if t == "cercle":
        (gx, gy), gr = forme["centre"], float(forme["rayon"])
        x0, x1, y0, y1 = int(max(0, gx - 2.6 * gr)), int(min(W, gx + 2.6 * gr)), int(max(0, gy - 2.6 * gr)), int(min(H, gy + 2.6 * gr))
        m[y0:y1, x0:x1] = 1
        return m, (gx, gy)
    if t == "ellipse":
        (gx, gy), (a, b) = forme["centre"], forme["axes"]
        cv2.ellipse(m, (int(round(gx)), int(round(gy))), (int(round(a * 1.5)), int(round(b * 1.5))), -float(forme.get("angle", 0)), 0, 360, 1, -1)
        return m, (gx, gy)
    if t == "rectangle":
        x0, y0, x1, y1 = [int(round(v)) for v in forme["boite"]]
        m[max(0, y0):min(H, y1), max(0, x0):min(W, x1)] = 1
        return m, ((x0 + x1) / 2, (y0 + y1) / 2)
    if t == "polygone":
        pts = np.array(forme["points"], dtype=np.float64)
        cv2.fillPoly(m, [np.round(pts).astype(np.int32)], 1)
        mo = cv2.moments(m, binaryImage=True)
        return m, ((mo["m10"] / max(mo["m00"], 1), mo["m01"] / max(mo["m00"], 1)))
    if t == "masque":
        import pathlib
        f = pathlib.Path(forme["fichier"])
        if not f.is_absolute() and dossier is not None:
            f = pathlib.Path(dossier) / f
        im = np.asarray(Image.open(f).convert("L"))
        if im.shape != (H, W):
            raise ValueError(f"le masque {f.name} fait {im.shape[1]}×{im.shape[0]}, l'image {W}×{H} : ils doivent avoir la même taille")
        m = (im > 127).astype(np.uint8)
        mo = cv2.moments(m, binaryImage=True)
        return m, ((mo["m10"] / max(mo["m00"], 1), mo["m01"] / max(mo["m00"], 1)))
    raise ValueError(f"type de forme inconnu : {t} (cercle, ellipse, rectangle, polygone, masque)")

def remplissage(rgb, forme, dossier=None):
    """Détoure le remplissage de la forme. Renvoie masque, couleur du remplissage F, première estimation de l'encre, lasso."""
    H, W = rgb.shape[:2]
    L = B.luma(rgb)
    lasso, graine = _lasso(forme, H, W, dossier)
    graine = tuple(forme.get("graine", graine))[:2]
    t = forme.get("type", "cercle")
    toutes = forme.get("composantes", "graine") == "toutes"
    clair_trait = forme.get("trait", "sombre") == "clair"
    yy, xx = np.mgrid[0:H, 0:W]
    dd = np.hypot(xx - graine[0], yy - graine[1])
    dans = lasso > 0
    if not dans.any():
        raise ValueError(f"forme « {forme.get('nom')} » : la cible est hors de l'image")
    # couleur du remplissage
    if isinstance(forme.get("remplissage"), str) and forme["remplissage"].startswith("#"):
        F = B.de_hexa(forme["remplissage"])
    elif toutes and "graine" not in forme:
        lum = L[dans]
        if forme.get("remplissage", "clair") == "sombre":
            F = np.median(rgb[dans][lum <= np.percentile(lum, 10)], 0)
        else:
            F = np.median(rgb[dans][lum >= np.percentile(lum, 90)], 0)
    else:
        rho = float(forme.get("rayon_graine", 0.5 * forme["rayon"] if t == "cercle" else (0.5 * min(forme["axes"]) if t == "ellipse" else 8)))
        z = dans & (dd < rho)
        if z.sum() < 9:
            raise ValueError(f"forme « {forme.get('nom')} » : la graine {graine} n'est pas dans la cible")
        lum = L[z]
        lo, hi = np.percentile(lum, 50), np.percentile(lum, 80)
        k = (lum >= lo) & (lum <= hi)
        F = np.median(rgb[z][k if k.sum() >= 5 else slice(None)], 0)
    # première estimation de l'encre : le 1 % le plus sombre (ou le plus clair) autour de la forme
    if isinstance(forme.get("encre"), str):
        encre0 = B.de_hexa(forme["encre"])
    else:
        z = dans & (dd < 1.1 * forme["rayon"]) if t == "cercle" else dans
        lum = L[z]
        sel = lum >= np.percentile(lum, 99.0) if clair_trait else lum <= np.percentile(lum, 1.0)
        encre0 = np.median(rgb[z][sel], 0)
    dF = float(np.linalg.norm(F - encre0))
    if dF < 60:
        raise ValueError(f"forme « {forme.get('nom')} » : contraste insuffisant entre le remplissage {B.hexa(F)} et le trait {B.hexa(encre0)} "
                         f"(écart {dF:.0f}, il en faut 60). Donner \"encre\": \"#rrvvbb\" ou \"trait\": \"clair\" dans la cible.")
    # un texte est un aplat : en plusieurs morceaux, on ne garde que ce qui est tout près de la couleur du remplissage
    tol = float(forme.get("tolerance_couleur", 0.3 if toutes else 0.75))
    cand = dans & (np.linalg.norm(rgb - encre0, axis=-1) > 0.5 * dF) & (np.linalg.norm(rgb - F, axis=-1) < tol * dF)
    n, lab, st, _ = cv2.connectedComponentsWithStats(cand.astype(np.uint8), connectivity=4)
    if n <= 1:
        raise ValueError(f"forme « {forme.get('nom')} » : aucun remplissage trouvé dans la cible")
    if toutes:
        amin = max(12, int(forme.get("aire_min", 20)))
        bord = cv2.dilate((lasso == 0).astype(np.uint8), np.ones((3, 3), np.uint8)) > 0      # ce qui touche le bord du lasso est du décor, pas une lettre
        bord[0, :] = True; bord[-1, :] = True; bord[:, 0] = True; bord[:, -1] = True
        touche = set(np.unique(lab[bord & cand]).tolist())
        garde = [i for i in range(1, n) if st[i, cv2.CC_STAT_AREA] >= amin and i not in touche]
        if not garde:
            raise ValueError(f"forme « {forme.get('nom')} » : aucun morceau de la couleur du remplissage {B.hexa(F)} n'est entièrement dans la cible "
                             "(agrandir la boîte, ou donner la couleur du remplissage en #rrvvbb)")
        masque = np.isin(lab, garde)
    else:
        ys, xs = np.where(cand)
        i = int(np.argmin((xs - graine[0]) ** 2 + (ys - graine[1]) ** 2))
        masque = lab == lab[ys[i], xs[i]]
    return dict(masque=masque, F=F, encre0=encre0, dF=dF, lasso=lasso, graine=graine, L=L, toutes=toutes)

# ====================================================================== ajustements
def _cercle_3(p):
    (x1, y1), (x2, y2), (x3, y3) = p
    a = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if abs(a) < 1e-6:
        return None
    s1, s2, s3 = x1 * x1 + y1 * y1, x2 * x2 + y2 * y2, x3 * x3 + y3 * y3
    ux = (s1 * (y2 - y3) + s2 * (y3 - y1) + s3 * (y1 - y2)) / a
    uy = (s1 * (x3 - x2) + s2 * (x1 - x3) + s3 * (x2 - x1)) / a
    return ux, uy, math.hypot(x1 - ux, y1 - uy)

def _cercle_mc(pts):
    A = np.c_[2 * pts[:, 0], 2 * pts[:, 1], np.ones(len(pts))]
    b = (pts ** 2).sum(1)
    (cx, cy, c), *_ = np.linalg.lstsq(A, b, rcond=None)
    return float(cx), float(cy), float(math.sqrt(max(c + cx * cx + cy * cy, 1e-6)))

def _ajuste_cercle(pts, rng, gx, gy, gr, tol=1.5, essais=6000):
    """Cercle qui passe par le plus de points (RANSAC, tolérance 1,5 px), puis moindres carrés sur ces points."""
    best, nb = None, -1
    for _ in range(essais):
        c = _cercle_3(pts[rng.choice(len(pts), 3, replace=False)])
        if c is None or not (0.45 * gr < c[2] < 2.2 * gr) or math.hypot(c[0] - gx, c[1] - gy) > 1.3 * gr:
            continue
        ok = np.abs(np.hypot(pts[:, 0] - c[0], pts[:, 1] - c[1]) - c[2]) < tol
        if ok.sum() > nb:
            nb, best = int(ok.sum()), ok
    if best is None:
        raise ValueError("aucun cercle ne s'ajuste sur le bord du remplissage : vérifier le centre et le rayon de la cible")
    for _ in range(3):
        cx, cy, r = _cercle_mc(pts[best])
        best = np.abs(np.hypot(pts[:, 0] - cx, pts[:, 1] - cy) - r) < tol
    return cx, cy, r, int(best.sum())

def harmoniques(ang_deg, val, ordre=3):
    """Ajuste val(θ) = a0 + Σ ak cos kθ + bk sin kθ sur les points valides. Renvoie (coefs, fonction, résidu σ)."""
    val = np.asarray(val, dtype=float)
    ok = np.isfinite(val)
    th = np.radians(np.asarray(ang_deg, dtype=float))
    def base(t):
        cols = [np.ones_like(t)]
        for k in range(1, ordre + 1):
            cols += [np.cos(k * t), np.sin(k * t)]
        return np.stack(cols, 1)
    if ok.sum() < 2 * ordre + 4:
        return None, None, float("nan")
    co, *_ = np.linalg.lstsq(base(th[ok]), val[ok], rcond=None)
    f = lambda a: base(np.radians(np.atleast_1d(np.asarray(a, dtype=float)))) @ co
    return co, f, float(np.std(val[ok] - f(np.asarray(ang_deg)[ok])))

# ====================================================================== une coupe en travers du bord
def _une_coupe(rho, p, e, ib, portee_px, kin_px=10.0, s_int=SEUIL_INTERIEUR, s_sort=SEUIL_SORTIE):
    """rho : positions le long de la normale (croissantes vers l'extérieur) ; p : luminance ; e : écart de couleur à l'encre ;
    ib : indice du bout du remplissage. Renvoie un dict (motif non vide = coupe écartée)."""
    o = dict(motif="", ep=np.nan, rin=np.nan, rout=np.nan, tin=np.nan, tout=np.nan, lmin=np.nan, lin=np.nan, lout=np.nan,
             lplat=np.nan, sur_clair=np.nan, sous_sombre=np.nan, rm=np.nan)
    kin = max(K3 + 1, int(round(kin_px / PAS)))
    if ib <= kin + 4 or ib >= len(rho) - 2 * K10:
        o["motif"] = "hors cadre ou remplissage interrompu"
        return o
    ei = float(np.median(e[ib - kin:ib - K3 + 1])); li = float(np.median(p[ib - kin:ib - K3 + 1]))
    if ei < s_int:
        o["motif"] = "intérieur aussi sombre que le trait (autre objet, cheveux)"
        return o
    d0 = ib - int(2 / PAS)
    ri = B.croisement(rho, e, 0.5 * ei, d0, +1)
    if ri is None or abs(ri - rho[ib]) > 3:
        o["motif"] = "pas de trait au bout du remplissage"
        return o
    ia = int(round((ri - rho[0]) / PAS))
    r90 = B.croisement(rho, e, 0.9 * ei, ia, -1)
    o["rin"], o["lin"] = ri, li
    if r90 is not None:
        o["tin"] = 2 * abs(ri - r90)
    o["sur_clair"] = float(p[max(0, ia - int(4 / PAS)):ia].max() - li) if ia > 0 else np.nan
    lim = min(len(e) - K10 - K15 - 1, ia + int(portee_px / PAS))
    jf = None
    for j in range(ia + int(1 / PAS), lim):
        if e[j] > s_sort and e[j:j + K15].min() > s_sort:
            jf = j
            break
    fin = jf or lim
    coeur = p[ia + int(0.3 * max(1, fin - ia)):ia + int(0.7 * max(1, fin - ia)) + 1]
    o["lplat"] = float(np.median(coeur)) if len(coeur) else float(p[ia])
    o["lmin"] = float(p[ia:fin + 1].min())
    if jf is None:
        o["motif"] = "décor aussi sombre que le trait"
        o["rm"] = ri + 2.0
        return o
    eo = float(np.median(e[jf + K3:jf + K10])); o["lout"] = float(np.median(p[jf + K3:jf + K10]))
    if eo < s_int:
        o["motif"] = "décor aussi sombre que le trait"
        o["rm"] = (ri + rho[jf]) / 2
        return o
    ro = B.croisement(rho, e, 0.5 * eo, jf + K15, -1)
    if ro is None or ro < ri:
        o["motif"] = "mesure instable"
        return o
    o["rout"], o["ep"] = ro, ro - ri
    io = int(round((ro - rho[0]) / PAS))
    q90 = B.croisement(rho, e, 0.9 * eo, io, +1)
    if q90 is not None and q90 - ro < 8:
        o["tout"] = 2 * abs(q90 - ro)
    o["sous_sombre"] = o["lplat"] - o["lmin"]
    o["rm"] = (ri + ro) / 2
    return o

def _lire(img, xs, ys):
    return B.echantillons(img, xs, ys)

def _lire_rvb(rgb, xs, ys):
    return np.stack([_lire(np.ascontiguousarray(rgb[..., k]), xs, ys) for k in range(3)], -1)

CHAMPS = ("ep", "rin", "rout", "tin", "tout", "lmin", "lin", "lout", "lplat", "sur_clair", "sous_sombre")

def _range(c, sorties, prgb, rho):
    """Range les résultats des coupes dans le dict c et lit la couleur au milieu du trait."""
    n = len(sorties)
    for k in CHAMPS:
        c[k] = np.array([s[k] for s in sorties], dtype=float)
    c["motif"] = [s["motif"] for s in sorties]
    coul = np.full((n, 3), np.nan)
    for i, s in enumerate(sorties):
        if np.isfinite(s["rm"]):
            j = int(round((s["rm"] - rho[0]) / PAS))
            if 0 <= j < prgb.shape[1]:
                coul[i] = prgb[i, j]
    c["coul"] = coul
    # rejet des valeurs isolées : écart à la médiane glissante (±6 coupes) de plus de 35 % et de plus de 1,5 px
    ep0 = c["ep"].copy()
    for i in range(n):
        if np.isfinite(ep0[i]):
            v = ep0[[(i + d) % n for d in range(-6, 7)]]
            if np.isfinite(v).sum() >= 5:
                m = np.nanmedian(v)
                if abs(ep0[i] - m) > max(1.5, 0.35 * m):
                    c["ep"][i] = np.nan; c["rout"][i] = np.nan; c["motif"][i] = "trait collé à un autre objet (valeur isolée)"

def _exclus(forme, P, ang):
    """Motif d'exclusion demandé par la cible pour chaque point (zones rectangulaires, plages d'angles)."""
    out = [""] * len(P)
    for (x0, y0, x1, y1) in forme.get("exclure", []):
        for i in np.where((P[:, 0] >= x0) & (P[:, 0] <= x1) & (P[:, 1] >= y0) & (P[:, 1] <= y1))[0]:
            out[i] = "zone exclue par la cible"
    for (a0, a1) in forme.get("exclure_angles", []):
        for i in range(len(P)):
            a = ang[i] % 360
            if (a0 <= a <= a1) or (a1 < a0 and (a >= a0 or a <= a1)):
                out[i] = "angles exclus par la cible"
    return out

# ====================================================================== contour : cercle
def _contour_cercle(rgb, forme, R):
    L, masque = R["L"], R["masque"]
    H, W = L.shape
    (gx, gy), gr = forme["centre"], float(forme["rayon"])
    cts, _ = cv2.findContours(masque.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    pts = max(cts, key=len)[:, 0, :].astype(np.float64)
    pts = pts[(pts[:, 0] > 1) & (pts[:, 0] < W - 2) & (pts[:, 1] > 1) & (pts[:, 1] < H - 2)]      # le bord du cadre n'est pas un bord de forme
    if len(pts) > 2500:
        pts = pts[:: len(pts) // 2500 + 1]
    cx, cy, r, nb = _ajuste_cercle(pts, np.random.default_rng(7), gx, gy, gr)
    n = 360
    rho = np.arange(0.3 * r, 1.6 * r, PAS, dtype=np.float32)
    th = np.radians(np.arange(n)).astype(np.float32)
    N = np.stack([np.cos(th), -np.sin(th)], 1)
    xs = cx + np.outer(N[:, 0], rho); ys = cy + np.outer(N[:, 1], rho)
    pr = _lire(L, xs, ys); pm = _lire(masque.astype(np.float32), xs, ys); prgb = _lire_rvb(rgb, xs, ys)
    bout = np.full(n, np.nan)
    for i in range(n):
        w = np.where(pm[i] > 0.5)[0]
        if len(w) and w[-1] < len(rho) - K10 - 2:
            bout[i] = rho[w[-1]]
    # forme lisse (cercle + 5 harmoniques) : ce qui s'en écarte est un autre objet
    ok = np.isfinite(bout) & (np.abs(bout - r) < max(2.5, 0.025 * r))
    for _ in range(6):
        if ok.sum() < 30:
            break
        _, lisse, _ = harmoniques(np.arange(n)[ok], bout[ok], 5)
        ok = np.isfinite(bout) & (np.abs(bout - lisse(np.arange(n))) < max(2.5, 0.02 * r))
    ech = []
    for i in np.where(ok)[0]:
        j = int(round((bout[i] + 1.75 - rho[0]) / PAS))
        if j < prgb.shape[1]:
            ech.append(prgb[i, j])
    encre = np.median(np.array(ech), 0) if len(ech) >= 10 else R["encre0"]
    E = np.sqrt(((prgb - encre) ** 2).sum(-1))
    ang = np.arange(n, dtype=float)
    orig = np.tile(np.array([[cx, cy]]), (n, 1))
    excl = _exclus(forme, orig + N * r, ang)
    vide = _une_coupe(rho, pr[0], E[0], 0, 1)
    sorties = []
    for i in range(n):
        if excl[i]:
            sorties.append(dict(vide, motif=excl[i]))
        elif not np.isfinite(bout[i]):
            sorties.append(dict(vide, motif="hors cadre ou remplissage interrompu"))
        elif not ok[i]:
            sorties.append(dict(vide, motif="autre objet devant la forme (chapeau, visière, accessoire)"))
        else:
            sorties.append(_une_coupe(rho, pr[i], E[i], int(round((bout[i] - rho[0]) / PAS)), 0.3 * r))
    # bord coupé par le cadre : la coupe doit rester dans l'image jusqu'au palier du décor (10 px après le bord extérieur du trait),
    # sinon les pixels « lus » hors de l'image ne sont que la répétition du dernier pixel et l'épaisseur est fausse
    hors = (xs < 0) | (xs > W - 1) | (ys < 0) | (ys > H - 1)
    for i in range(n):
        s = sorties[i]
        if np.isfinite(s["rout"]):
            j = int(round((s["rout"] - rho[0]) / PAS)) + K10 + K15
            if hors[i, :min(len(rho), j + 1)].any():
                sorties[i] = dict(vide, motif="bord coupé par le cadre")
        elif np.isfinite(bout[i]) and not excl[i] and hors[i, :min(len(rho), int(round((bout[i] - rho[0]) / PAS)) + 2 * K10)].any():
            sorties[i] = dict(vide, motif="bord coupé par le cadre")
    c = dict(type="cercle", cx=cx, cy=cy, r=r, nb_points=nb, nb_bord=len(pts), ang=ang, orig=orig, N=N, rho=rho, profils=pr, encre=encre)
    _range(c, sorties, prgb, rho)
    return c

# ====================================================================== contour : forme quelconque
def _courbes(masque, trous, lissage):
    """Bords du remplissage, lissés et rééchantillonnés tous les pixels : points P et normales N tournées vers l'extérieur."""
    m = masque.astype(np.uint8)
    cts, _ = cv2.findContours(m, cv2.RETR_CCOMP if trous else cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    mf = m.astype(np.float32)
    Ps, Ns = [], []
    rayon = max(1, int(round(3 * lissage)))
    g = np.exp(-0.5 * (np.arange(-rayon, rayon + 1) / max(lissage, 1e-3)) ** 2); g /= g.sum()
    for ct in cts:
        if len(ct) < 24:
            continue
        pts = ct[:, 0, :].astype(np.float64)
        ext = np.r_[pts[-rayon:], pts, pts[:rayon]]
        liss = np.stack([np.convolve(ext[:, k], g, mode="valid") for k in range(2)], 1)
        seg = np.hypot(*np.diff(np.r_[liss, liss[:1]], axis=0).T)
        s = np.r_[0, np.cumsum(seg)]
        cible = np.arange(0, s[-1], 1.0)
        fer = np.r_[liss, liss[:1]]
        P = np.stack([np.interp(cible, s, fer[:, k]) for k in range(2)], 1)
        if len(P) < 12:
            continue
        T = np.roll(P, -2, 0) - np.roll(P, 2, 0)
        T /= np.maximum(np.hypot(T[:, 0], T[:, 1])[:, None], 1e-6)
        N = np.stack([T[:, 1], -T[:, 0]], 1)
        dehors = _lire(mf, (P[:, 0] + 2.5 * N[:, 0])[None], (P[:, 1] + 2.5 * N[:, 1])[None])[0]
        dedans = _lire(mf, (P[:, 0] - 2.5 * N[:, 0])[None], (P[:, 1] - 2.5 * N[:, 1])[None])[0]
        if np.mean(dehors) > np.mean(dedans):          # la normale pointe vers le remplissage : on la retourne
            N = -N
        Ps.append(P); Ns.append(N)
    if not Ps:
        raise ValueError("le remplissage trouvé est trop petit pour être mesuré (moins de 24 px de bord)")
    return np.concatenate(Ps), np.concatenate(Ns)

def _ecart_ellipse(pts, el):
    (ex, ey), (d1, d2), an = el
    t = math.radians(an)
    dx, dy = pts[:, 0] - ex, pts[:, 1] - ey
    u = dx * math.cos(t) + dy * math.sin(t); v = -dx * math.sin(t) + dy * math.cos(t)
    q = np.hypot(u / (d1 / 2), v / (d2 / 2))
    return (q - 1) * np.hypot(dx, dy) / np.maximum(q, 1e-6)

def _contour_general(rgb, forme, R):
    L, masque = R["L"], R["masque"]
    H, W = L.shape
    toutes = R["toutes"]
    trous = bool(forme.get("trous", toutes))
    lissage = float(forme.get("lissage", 2.0))
    P, N = _courbes(masque, trous, lissage)
    n = len(P)
    dt = cv2.distanceTransform(masque.astype(np.uint8), cv2.DIST_L2, 5)
    inr = float(dt.max())                                # rayon du plus grand cercle inscrit dans le remplissage
    portee = float(forme.get("portee_trait", max(0.3 * inr, 24.0)))
    s_in, s_out = 14.0, max(0.6 * inr, portee + 26.0)
    rho = np.arange(-s_in, s_out, PAS, dtype=np.float32)
    xs = P[:, 0:1] + np.outer(N[:, 0], rho); ys = P[:, 1:2] + np.outer(N[:, 1], rho)
    pr = _lire(L, xs, ys); pm = _lire(masque.astype(np.float32), xs, ys); prgb = _lire_rvb(rgb, xs, ys)
    lasso_f = R["lasso"].astype(np.float32)
    bout = np.full(n, np.nan); prof = np.zeros(n)
    for i in range(n):
        d = pm[i] > 0.5
        tr = np.where(d[:-1] & ~d[1:])[0]                 # passages dedans -> dehors
        tr = tr[np.abs(rho[tr]) <= 4.0]
        if not len(tr):
            continue
        j = int(tr[np.argmin(np.abs(rho[tr]))])
        bout[i] = rho[j]
        k = j
        while k > 0 and d[k - 1]:
            k -= 1
        prof[i] = rho[j] - rho[k]
    ang = (np.degrees(np.arctan2(-N[:, 1], N[:, 0])) % 360)
    excl = _exclus(forme, P, ang)
    # bord coupé par la cible ou par le cadre
    xo, yo = P[:, 0] + 3 * N[:, 0], P[:, 1] + 3 * N[:, 1]
    coupe = (xo < 1) | (yo < 1) | (xo > W - 2) | (yo > H - 2)
    coupe |= _lire(lasso_f, xo[None], yo[None])[0] < 0.5
    ok = np.isfinite(bout) & ~coupe
    el = None
    if forme.get("type") == "ellipse":                    # modèle : ellipse ajustée, ce qui s'en écarte est un autre objet
        pb = P + N * np.nan_to_num(bout)[:, None]
        bon = ok.copy()
        for _ in range(5):
            if bon.sum() < 20:
                break
            el = cv2.fitEllipse(pb[bon].astype(np.float32))
            bon = ok & (np.abs(_ecart_ellipse(pb, el)) < max(2.5, 0.02 * (el[1][0] + el[1][1]) / 4))
        modele = bon
    else:
        modele = np.ones(n, bool)
    ech = []
    for i in np.where(ok & modele)[0]:
        j = int(round((bout[i] + 1.75 - rho[0]) / PAS))
        if j < prgb.shape[1]:
            ech.append(prgb[i, j])
    encre = np.median(np.array(ech), 0) if len(ech) >= 10 else R["encre0"]
    if isinstance(forme.get("encre"), str):
        encre = B.de_hexa(forme["encre"])
    E = np.sqrt(((prgb - encre) ** 2).sum(-1))
    seuils = forme.get("seuils", {})
    s_int, s_sort = float(seuils.get("interieur", SEUIL_INTERIEUR)), float(seuils.get("sortie", SEUIL_SORTIE))
    vide = _une_coupe(rho, pr[0], E[0], 0, 1)
    sorties = []
    for i in range(n):
        if excl[i]:
            sorties.append(dict(vide, motif=excl[i]))
        elif coupe[i]:
            sorties.append(dict(vide, motif="bord coupé par la cible ou par le cadre"))
        elif not np.isfinite(bout[i]):
            sorties.append(dict(vide, motif="bord non retrouvé après lissage"))
        elif not modele[i]:
            sorties.append(dict(vide, motif="autre objet devant la forme (chapeau, visière, accessoire)"))
        elif prof[i] < 4.5:
            sorties.append(dict(vide, motif="remplissage trop étroit (moins de 4,5 px)"))
        else:
            sorties.append(_une_coupe(rho, pr[i], E[i], int(round((bout[i] - rho[0]) / PAS)), portee,
                                      kin_px=min(10.0, prof[i] - 1.5), s_int=s_int, s_sort=s_sort))
    ys_, xs_ = np.where(masque)
    c = dict(type=forme.get("type"), cx=float(xs_.mean()), cy=float(ys_.mean()), r=inr, nb_points=int((ok & modele).sum()), nb_bord=n,
             ang=ang, orig=P, N=N, rho=rho, profils=pr, encre=encre, ellipse=el,
             boite=[int(xs_.min()), int(ys_.min()), int(xs_.max()) + 1, int(ys_.max()) + 1])
    _range(c, sorties, prgb, rho)
    return c

def contour(rgb, forme, dossier=None):
    """Mesure le contour d'une forme. Renvoie le dict de travail (tableaux par coupe) utilisé par resume_contour et ombrage."""
    R = remplissage(rgb, forme, dossier)
    c = _contour_cercle(rgb, forme, R) if forme.get("type", "cercle") == "cercle" else _contour_general(rgb, forme, R)
    c.update(masque=R["masque"], L=R["L"], F=R["F"], toutes=R["toutes"], dF=float(np.linalg.norm(R["F"] - c["encre"])), nom=forme.get("nom"))
    return c

# ====================================================================== chiffres publiables du contour
def _par5(ang, v, mini=3):
    """Médiane par tranche de 5° d'orientation (72 valeurs)."""
    out = np.full(72, np.nan)
    k = np.round(np.asarray(ang) / 5.0).astype(int) % 72
    for b in range(72):
        x = v[k == b]
        if np.isfinite(x).sum() >= mini:
            out[b] = np.nanmedian(x)
    return out

def _points(c, s):
    return c["orig"] + c["N"] * s[:, None]

def resume_contour(c):
    """Chiffres publiables du contour. Pour un cercle, D = 2 × rayon du bord extérieur du trait."""
    ang5 = np.arange(0, 360, 5)
    a = c["ang"]
    ep5 = _par5(a, c["ep"])
    ok = np.isfinite(ep5)
    co, f, sig = harmoniques(ang5, ep5, 2)
    res = dict(type=c["type"], angles_valides=int(ok.sum()), angles_total=72, coupes_valides=int(np.isfinite(c["ep"]).sum()), coupes_total=int(len(a)))
    if c["type"] == "cercle":
        rin_m = float(np.nanmedian(c["rin"])) if np.isfinite(c["rin"]).any() else c["r"]
        rout_m = float(np.nanmedian(c["rout"])) if np.isfinite(c["rout"]).any() else float("nan")
        D = 2 * rout_m if (np.isfinite(rout_m) and ok.sum() >= 6) else None      # pas de diamètre sans bord extérieur mesuré
        res.update(D_px=_r(D) if D else None, centre=[_r(c["cx"]), _r(c["cy"])], rayon_ext_px=_r(rout_m), rayon_int_px=_r(rin_m),
                   rayon_du_remplissage_px=_r(c["r"]))
        if D is None:
            res["avertissement"] = ("moins de 6 orientations mesurables : le diamètre D n'est pas donné et cette forme ne peut pas servir de grandeur de "
                                    "référence. Causes fréquentes : forme trop petite (rayon sous 20 px), fond transparent ou aussi sombre que le trait, cible mal posée")
    else:
        x0, y0, x1, y1 = c["boite"]
        D = None
        res.update(D_px=None, centre=[_r(c["cx"]), _r(c["cy"])], boite_remplissage=[x0, y0, x1, y1], largeur_px=x1 - x0, hauteur_px=y1 - y0,
                   aire_px=int(c["masque"].sum()), rayon_inscrit_px=_r(c["r"]), perimetre_px=int(len(a)))
    sect = {}
    for nom, a0, a1 in (("droite (315–45°)", 315, 405), ("haut (45–135°)", 45, 135), ("gauche (135–225°)", 135, 225), ("bas (225–315°)", 225, 315)):
        m = np.array([(x >= a0 and x < a1) or (x + 360 >= a0 and x + 360 < a1) for x in ang5])
        v = ep5[m]
        sect[nom] = dict(moyenne_px=_r(np.nanmean(v)) if np.isfinite(v).any() else None, valides=int(np.isfinite(v).sum()), sur=int(len(v)))
    if ok.sum() >= 6:
        imin, imax = int(np.nanargmin(ep5)), int(np.nanargmax(ep5))
        res.update(epaisseur_moy_px=_r(np.nanmean(ep5)), epaisseur_med_px=_r(np.nanmedian(ep5)), epaisseur_min_px=_r(ep5[imin]),
                   angle_min=int(ang5[imin]), epaisseur_max_px=_r(ep5[imax]), angle_max=int(ang5[imax]),
                   ecart_type_px=_r(np.nanstd(ep5)), rapport_max_min=_r(ep5[imax] / max(ep5[imin], 1e-6), 2))
        if D:
            res.update(epaisseur_moy_D=_r(np.nanmean(ep5) / D, 4), epaisseur_min_D=_r(ep5[imin] / D, 4), epaisseur_max_D=_r(ep5[imax] / D, 4))
    elif np.isfinite(c["ep"]).sum() >= 3:
        res.update(epaisseur_moy_px=_r(np.nanmean(c["ep"])), epaisseur_med_px=_r(np.nanmedian(c["ep"])))
    if co is not None:
        a1 = math.hypot(co[1], co[2]); ph1 = math.degrees(math.atan2(co[2], co[1])) % 360
        a2 = math.hypot(co[3], co[4])
        loi = dict(a0_px=_r(co[0], 2), h1_amplitude_px=_r(a1, 2), h1_plein_vers_deg=_r(ph1, 0), h2_amplitude_px=_r(a2, 2), coefs=[_r(x, 3) for x in co])
        if D:
            loi["coefs_D"] = [_r(x / D, 5) for x in co]
        res.update(loi=loi, tremble_px=_r(sig, 2))
        if D:
            res["tremble_D"] = _r(sig / D, 4)
        co1, _, sig1 = harmoniques(ang5, ep5, 1)            # la loi simple : un plein et un délié. C'est elle qui va dans la fiche et la synthèse
        if co1 is not None:
            b1 = math.hypot(co1[1], co1[2])
            l1 = dict(a0_px=_r(co1[0], 2), h1_px=_r(b1, 2), plein_vers_deg=_r(math.degrees(math.atan2(co1[2], co1[1])) % 360, 0),
                      delie_px=_r(co1[0] - b1, 2), plein_px=_r(co1[0] + b1, 2), residu_px=_r(sig1, 2),
                      note="épaisseur = a0 + h1 × cos(orientation − plein_vers). plein_px et delie_px viennent de la loi : ils ne sont pas "
                           "gonflés par un endroit où le trait touche un autre trait, au contraire de epaisseur_max_px")
            if D:
                l1.update(a0_D=_r(co1[0] / D, 4), h1_D=_r(b1 / D, 4), delie_D=_r((co1[0] - b1) / D, 4), plein_D=_r((co1[0] + b1) / D, 4))
            res["loi_simple"] = l1
    if c["type"] == "cercle":
        for nom, v in (("ondulation_bord_ext_px", c["rout"]), ("ondulation_bord_int_px", c["rin"])):
            _, _, s = harmoniques(a, v, 2)
            res[nom] = _r(s, 2)
    pe = _points(c, np.where(np.isfinite(c["rout"]), c["rout"], 0))[np.isfinite(c["rout"])]
    if len(pe) >= 30:
        (_, _), (ax1, ax2), _an = cv2.fitEllipse(pe.astype(np.float32))
        res["ovale"] = dict(grand_axe_px=_r(max(ax1, ax2)), petit_axe_px=_r(min(ax1, ax2)), rapport=_r(min(ax1, ax2) / max(ax1, ax2), 3))
    okc = np.isfinite(c["coul"][:, 0])
    if okc.sum():
        cm = np.median(c["coul"][okc], 0)
        lum = B.luma(c["coul"][okc])
        res["trait"] = dict(mediane_rvb=[int(round(v)) for v in cm], hex=B.hexa(cm), luminance_mediane=_r(np.median(lum)),
                            luminance_p10=_r(np.percentile(lum, 10)), luminance_p90=_r(np.percentile(lum, 90)),
                            ecart_type_rvb=[_r(v) for v in np.std(c["coul"][okc], 0)], coeur_luminance=_r(np.nanmedian(c["lplat"])),
                            minimum_luminance=_r(np.nanmedian(c["lmin"])))
        q = {}
        for nom, a0, a1 in (("droite", 315, 405), ("haut", 45, 135), ("gauche", 135, 225), ("bas", 225, 315)):
            m = okc & (((a >= a0) & (a < a1)) | ((a + 360 >= a0) & (a + 360 < a1)))
            if m.sum():
                q[nom] = B.hexa(np.median(c["coul"][m], 0))
        res["trait"]["par_quadrant"] = q
    res["remplissage_hex"] = B.hexa(c["F"])
    fin = lambda k: np.isfinite(c[k]).any()
    res["bord"] = dict(transition_int_px=_r(np.nanmedian(c["tin"]), 2) if fin("tin") else None,
                       transition_ext_px=_r(np.nanmedian(c["tout"]), 2) if fin("tout") else None,
                       transition_int_p90_px=_r(np.nanpercentile(c["tin"], 90), 2) if fin("tin") else None,
                       note="largeur 10–90 % estimée par 2 × la demi-transition côté clair (50 → 90 %)")
    med = lambda k: _r(np.nanmedian(c[k])) if fin(k) else None
    res["accentuation"] = dict(sur_brillance_cote_remplissage=med("sur_clair"), creux_dans_le_trait=med("sous_sombre"),
                               coeur_du_trait_luminance=med("lplat"), remplissage_au_bord_luminance=med("lin"))
    # halo : luminance juste dehors (1,5–4 px) moins plus loin (10–18 px), sur les coupes valides
    rho, pr = c["rho"], c["profils"]
    hal = []
    for i in np.where(np.isfinite(c["rout"]))[0]:
        ro = c["rout"][i]
        pres = pr[i][(rho > ro + 1.5) & (rho < ro + 4)]; loin = pr[i][(rho > ro + 10) & (rho < ro + 18)]
        if len(pres) and len(loin):
            hal.append(float(pres.mean() - loin.mean()))
    res["halo_luminance"] = dict(median=_r(np.median(hal)) if hal else None, p10=_r(np.percentile(hal, 10)) if hal else None,
                                 p90=_r(np.percentile(hal, 90)) if hal else None)
    res["secteurs"] = sect
    res["courbe_5deg"] = [None if not np.isfinite(v) else _r(v, 2) for v in ep5]
    motifs = {}
    k5 = np.round(a / 5.0).astype(int) % 72
    for b in range(72):
        if not np.isfinite(ep5[b]):
            ms = [c["motif"][i] for i in np.where(k5 == b)[0] if c["motif"][i]]
            nb = int((k5 == b).sum())
            if ms:
                m = max(set(ms), key=ms.count)
            elif nb == 0:
                m = "aucun bord dans cette orientation"
            elif nb < 3:
                m = "trop peu de bord dans cette orientation (moins de 3 px : coin ou petite forme)"
            else:
                m = "mesure instable"
            motifs.setdefault(m, []).append(int(ang5[b]))
    res["angles_ecartes"] = motifs
    return res

# ====================================================================== ombrage du remplissage
def _plein(masque):
    """Remplissage sans ses trous (les détails dessinés dedans sont des trous)."""
    m = masque.astype(np.uint8)
    cts, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    out = np.zeros_like(m)
    cv2.drawContours(out, cts, -1, 1, -1)
    return out

def _zone_ombrage(c, rgb):
    """Remplissage érodé, sans les détails à l'encre."""
    cercle = c["type"] == "cercle"
    rin = float(np.nanmedian(c["rin"])) if cercle and np.isfinite(c["rin"]).any() else c["r"]
    marge = int(max(2, round(0.012 * rin)))
    E = np.linalg.norm(rgb - c["encre"], axis=-1)
    encre = (E < 0.62 * c["dF"]).astype(np.uint8)
    k = marge * 2 + 1
    el = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, k))
    encre = cv2.dilate(encre, el)
    dans = (cv2.erode(c["masque"].astype(np.uint8), el) > 0) & (encre == 0)
    if c["toutes"]:
        return dans, rin
    n, lab, stats, _ = cv2.connectedComponentsWithStats(dans.astype(np.uint8), connectivity=4)
    if n <= 1:
        return dans, rin
    g = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    return lab == g, rin

def ombrage(c, rgb):
    """Ombrage du remplissage. Longueurs en R : rayon extérieur pour un cercle, demi-grande dimension du remplissage sinon."""
    peau, rin = _zone_ombrage(c, rgb)
    L = c["L"]; cx, cy = c["cx"], c["cy"]
    cercle = c["type"] == "cercle"
    if cercle:
        rext = float(np.nanmedian(c["rout"])) if np.isfinite(c["rout"]).any() else rin * 1.05
        aire_ref = math.pi * rin * rin
    else:
        x0, y0, x1, y1 = c["boite"]
        rext = max(x1 - x0, y1 - y0) / 2.0
        aire_ref = float(_plein(c["masque"]).sum())
    D = 2 * rext
    ys, xs = np.where(peau)
    if len(xs) < 200:
        return dict(erreur="remplissage trop petit pour mesurer l'ombrage (moins de 200 px)"), None
    u, v = (xs - cx) / rext, (cy - ys) / rext
    lum = L[ys, xs]; col = rgb[ys, xs]
    res = dict(pixels=int(len(xs)), part_de_la_forme=_r(len(xs) / max(aire_ref, 1), 3), R_px=_r(rext))
    res["remplissage_median"] = dict(hex=B.hexa(np.median(col, 0)), luminance=_r(np.median(lum)), luminance_p2=_r(np.percentile(lum, 2)),
                                     luminance_p98=_r(np.percentile(lum, 98)), ecart_type_luminance=_r(lum.std(), 2))
    A = np.c_[np.ones_like(u), u, v]
    co, *_ = np.linalg.lstsq(A, lum, rcond=None)
    r2 = 1 - ((lum - A @ co) ** 2).sum() / max(((lum - lum.mean()) ** 2).sum(), 1e-6)
    res["degrade_lineaire"] = dict(amplitude_sur_2R=_r(2 * math.hypot(co[1], co[2])), vers_le_clair_deg=_r(math.degrees(math.atan2(co[2], co[1])) % 360, 0), r2=_r(r2, 3))
    A2 = np.c_[np.ones_like(u), u * u + v * v]
    co2, *_ = np.linalg.lstsq(A2, lum, rcond=None)
    r2b = 1 - ((lum - A2 @ co2) ** 2).sum() / max(((lum - lum.mean()) ** 2).sum(), 1e-6)
    res["degrade_radial"] = dict(centre_moins_bord=_r(-co2[1]), r2=_r(r2b, 3))
    # deux zones (k-moyennes en Lab)
    labs = B.lab(col).astype(np.float32)
    ech = labs[:: max(1, len(labs) // 40000)]
    cv2.setRNGSeed(7)
    _, _, centres = cv2.kmeans(ech, 2, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 40, 0.1), 4, cv2.KMEANS_PP_CENTERS)
    et = np.concatenate([np.argmin(((labs[i:i + 200000, None, :] - centres[None]) ** 2).sum(-1), 1) for i in range(0, len(labs), 200000)])
    clair = int(np.argmax(centres[:, 0]))
    zc, zs = et == clair, et != clair
    if zc.sum() < 20 or zs.sum() < 20:
        res["deux_zones"] = dict(note="une seule zone : aplat")
        return res, dict(peau=peau, zones=(ys, xs, zc), rext=rext, rin=rin)
    cc, cs = np.median(col[zc], 0), np.median(col[zs], 0)
    res["deux_zones"] = dict(
        claire=dict(hex=B.hexa(cc), part=_r(zc.mean(), 3), luminance=_r(np.median(lum[zc])), ecart_type_luminance=_r(lum[zc].std(), 2),
                    centre_uv=[_r(u[zc].mean(), 3), _r(v[zc].mean(), 3)]),
        sombre=dict(hex=B.hexa(cs), part=_r(zs.mean(), 3), luminance=_r(np.median(lum[zs])), ecart_type_luminance=_r(lum[zs].std(), 2),
                    centre_uv=[_r(u[zs].mean(), 3), _r(v[zs].mean(), 3)]),
        delta_e=_r(B.de2000(cc, cs), 1), ecart_tsl_sombre_vs_claire=B.ecart_tsl(cc, cs))
    # laquelle est la couleur de base ? la plus étendue. L'autre est une ombre (plus sombre) ou une lumière (plus claire)
    part_s = float(zs.mean())
    if part_s <= 0.5:
        nature = "liseré ou détail plus sombre (trop petit pour être une ombre propre)" if part_s < 0.08 else "ombre propre"
        res["deux_zones"].update(base="claire", zone_secondaire="sombre", part_secondaire=_r(part_s, 3),
                                 lecture=f"la couleur de base est la zone claire ; la zone sombre ({100 * part_s:.0f} %) : {nature}")
    else:
        nature = "reflet ou liseré de lumière" if 1 - part_s < 0.08 else "bande ou plage plus claire (lumière)"
        res["deux_zones"].update(base="sombre", zone_secondaire="claire", part_secondaire=_r(1 - part_s, 3),
                                 lecture=f"la couleur de base est la zone SOMBRE ; la zone claire ({100 * (1 - part_s):.0f} %) : {nature}. Ce n'est pas une ombre")
    # frontière : axe = du centre de la zone sombre vers celui de la zone claire
    dx, dy = u[zc].mean() - u[zs].mean(), v[zc].mean() - v[zs].mean()
    nrm = math.hypot(dx, dy) or 1.0
    ax = (dx / nrm, dy / nrm)
    s = u * ax[0] + v * ax[1]; t = -u * ax[1] + v * ax[0]
    front = []
    for tb in np.arange(-0.8, 0.81, 0.08):
        m = np.abs(t - tb) < 0.04
        if m.sum() < 30 or zc[m].sum() < 5 or zs[m].sum() < 5:
            continue
        ss = np.sort(s[m]); grille = np.linspace(ss[0], ss[-1], 60)
        err = [((s[m] < g) & zc[m]).sum() + ((s[m] >= g) & zs[m]).sum() for g in grille]
        front.append((tb, float(grille[int(np.argmin(err))]), min(err) / m.sum()))
    fr = dict(axe_vers_le_clair_deg=_r(math.degrees(math.atan2(ax[1], ax[0])) % 360, 0))
    if len(front) >= 5:
        ft = np.array(front)
        pc = np.polyfit(ft[:, 0], ft[:, 1], 2)
        fr.update(position_au_centre_R=_r(pc[2], 3), pente=_r(pc[1], 3), courbure=_r(pc[0], 3),
                  ecart_type_R=_r(np.std(ft[:, 1] - np.polyval(pc, ft[:, 0])), 3), melange=_r(ft[:, 2].mean(), 3))
        sr = s - np.polyval(pc, t)
        m = (np.abs(t) < 0.6) & (np.abs(sr) < 0.5)
        bins = np.arange(-0.5, 0.5001, 2.0 / D)          # 1 px
        idx = np.digitize(sr[m], bins)
        prof = np.array([np.median(lum[m][idx == i]) if (idx == i).sum() > 5 else np.nan for i in range(1, len(bins))])
        pos = (bins[:-1] + bins[1:]) / 2
        okp = np.isfinite(prof)
        if okp.sum() > 20:
            pos, prof = pos[okp], prof[okp]
            if (pos < -0.2).any() and (pos > 0.2).any():
                lo, hi = np.median(prof[pos < -0.2]), np.median(prof[pos > 0.2])
                p10 = B.croisement(pos, prof, lo + 0.1 * (hi - lo), 0, +1); p90 = B.croisement(pos, prof, lo + 0.9 * (hi - lo), len(pos) - 1, -1)
                if p10 is not None and p90 is not None:
                    fr.update(saut_luminance=_r(hi - lo), transition_px=_r(abs(p90 - p10) * D / 2, 1), transition_D=_r(abs(p90 - p10) / 2, 4))
            fr["profil_travers"] = dict(pos_R=[_r(x, 4) for x in pos], lum=[_r(x, 1) for x in prof])
    res["frontiere"] = fr
    for nom, z in (("claire", zc), ("sombre", zs)):
        if z.sum() > 50:
            Az = np.c_[np.ones(z.sum()), u[z], v[z]]
            cz, *_ = np.linalg.lstsq(Az, lum[z], rcond=None)
            res["deux_zones"][nom]["degrade_interne_sur_2R"] = _r(2 * math.hypot(cz[1], cz[2]))
            res["deux_zones"][nom]["degrade_vers_le_clair_deg"] = _r(math.degrees(math.atan2(cz[2], cz[1])) % 360, 0)
    # reflets : composantes nettement plus claires que la zone claire
    carte = np.zeros(L.shape, np.uint8)
    seuil_r = float(np.median(lum[zc]) + max(5.0, 2.5 * lum[zc].std()))
    carte[ys, xs] = (lum > seuil_r).astype(np.uint8)
    n, lb, st, cen = cv2.connectedComponentsWithStats(carte, connectivity=8)
    reflets = []
    aire_d = math.pi * rext * rext if cercle else aire_ref
    for i in range(1, n):
        a = st[i, cv2.CC_STAT_AREA]
        if a < max(12, 0.0008 * aire_d):
            continue
        m = lb == i
        uu, vv = (cen[i][0] - cx) / rext, (cy - cen[i][1]) / rext
        reflets.append(dict(centre_uv=[_r(uu, 3), _r(vv, 3)], rayon_R=_r(math.hypot(uu, vv), 3), angle_deg=_r(math.degrees(math.atan2(vv, uu)) % 360, 0),
                            aire_pct=_r(100 * a / aire_d, 2), largeur_2R=_r(st[i, cv2.CC_STAT_WIDTH] / D, 3), hauteur_2R=_r(st[i, cv2.CC_STAT_HEIGHT] / D, 3),
                            hex=B.hexa(np.median(rgb[m], 0)), gain_luminance=_r(np.median(L[m]) - np.median(lum[zc]))))
    reflets.sort(key=lambda r: -r["aire_pct"])
    res["reflets"] = dict(seuil_luminance=_r(seuil_r), liste=reflets[:6])
    # liseré : bande juste sous le trait comparée à l'intérieur, par orientation
    dd = np.hypot(xs - cx, ys - cy); an = (np.degrees(np.arctan2(cy - ys, xs - cx)) % 360)
    sect = np.round(an / 5).astype(int) % 72
    if cercle:
        z1 = (dd > rin - 0.07 * rext) & (dd < rin - 0.02 * rext); z2 = (dd > 0.45 * rext) & (dd < 0.70 * rext)
    else:
        prof = cv2.distanceTransform(_plein(c["masque"]), cv2.DIST_L2, 5)[ys, xs]
        z1 = (prof > 0.04 * c["r"] + 1) & (prof < 0.14 * c["r"] + 3); z2 = prof > 0.45 * c["r"]
    lis = []
    for k in range(72):
        b1 = z1 & (sect == k); b2 = z2 & (sect == k)
        lis.append((float(np.median(lum[b1])) if b1.sum() >= 5 else np.nan, float(np.median(lum[b2])) if b2.sum() >= 5 else np.nan))
    lis = np.array(lis)
    dl = lis[:, 0] - lis[:, 1]
    fin = np.isfinite(dl).any()
    res["lisere"] = dict(bord_moins_interieur_median=_r(np.nanmedian(dl)) if fin else None, max=_r(np.nanmax(dl)) if fin else None,
                         angle_du_max=int(np.nanargmax(dl) * 5) if fin else None, min=_r(np.nanmin(dl)) if fin else None,
                         angle_du_min=int(np.nanargmin(dl) * 5) if fin else None,
                         bord_5deg=[_r(x) for x in lis[:, 0]], interieur_5deg=[_r(x) for x in lis[:, 1]])
    # profils de luminance le long de 4 droites passant par le centre (201 points de −1 à +1, moyenne sur 5 px de large)
    pos = np.linspace(-1, 1, 201)
    profils, demi = {}, {}
    pm = peau.astype(np.float32)
    for nom, a in (("horizontal (0°)", 0), ("diagonale (45°)", 45), ("vertical (90°)", 90), ("diagonale (135°)", 135)):
        ca, sa = math.cos(math.radians(a)), math.sin(math.radians(a))
        lg = rin if cercle else float(np.abs((xs - cx) * ca - (ys - cy) * sa).max())
        acc = np.zeros(len(pos)); cnt = np.zeros(len(pos))
        for o in (-2, -1, 0, 1, 2):
            x = cx + pos * lg * ca + o * sa; y = cy - pos * lg * sa + o * ca
            l = B.echantillons(L, x[None], y[None])[0]; mk = B.echantillons(pm, x[None], y[None])[0] > 0.99
            acc += np.where(mk, l, 0); cnt += mk
        profils[nom] = [None if n_ < 3 else _r(a_ / n_, 1) for a_, n_ in zip(acc, cnt)]
        demi[nom] = _r(lg)
    res["profils_diametres"] = dict(pos_R=[_r(p, 2) for p in pos], **profils)
    res["profils_demi_longueur_px"] = demi
    # grain : écart type de (luminance − flou gaussien σ 2,5) sur le remplissage érodé
    er = cv2.erode(peau.astype(np.uint8), np.ones((9, 9), np.uint8)).astype(bool)
    hp = L - cv2.GaussianBlur(L, (0, 0), 2.5)
    res["grain_ecart_type"] = _r(hp[er].std(), 2) if er.sum() > 50 else None
    return res, dict(peau=peau, zones=(ys, xs, zc), rext=rext, rin=rin)

# ====================================================================== détails dessinés dans la forme
def details_internes(c, rgb):
    """Composantes d'encre à l'intérieur de la forme (traits du visage, boutons, coutures…) : position, taille,
    épaisseur (2 × aire / périmètre), couleur. Longueurs rapportées à 2R (D pour un cercle)."""
    L = c["L"]; cx, cy = c["cx"], c["cy"]
    cercle = c["type"] == "cercle"
    if cercle:
        rext = float(np.nanmedian(c["rout"])) if np.isfinite(c["rout"]).any() else c["r"] * 1.05
    else:
        x0, y0, x1, y1 = c["boite"]; rext = max(x1 - x0, y1 - y0) / 2.0
    D = 2 * rext
    marge = int(max(3, round(0.03 * c["r"])))
    if c["type"] in ("cercle", "ellipse"):
        ys, xs = np.where(c["masque"])
        env = cv2.convexHull(np.stack([xs, ys], 1).astype(np.int32))          # enveloppe : les détails sont dedans
        dedans = np.zeros(L.shape, np.uint8)
        cv2.fillPoly(dedans, [env], 1)
    else:
        dedans = _plein(c["masque"])
    dedans = cv2.erode(dedans, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * marge + 1, 2 * marge + 1)))
    E = np.linalg.norm(rgb - c["encre"], axis=-1)
    sombre = ((E < 0.5 * c["dF"]) & (dedans > 0)).astype(np.uint8)
    n, lab, st, cen = cv2.connectedComponentsWithStats(sombre, connectivity=8)
    alpha = np.clip(1 - E / max(c["dF"], 1), 0, 1)
    out = []
    for i in range(1, n):
        a = st[i, cv2.CC_STAT_AREA]
        if a < max(8, 0.00015 * D * D):
            continue
        m = (lab == i).astype(np.uint8)
        cts, hier = cv2.findContours(m, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
        per = sum(cv2.arcLength(ct, True) for ct in cts)
        trou = any(h[3] >= 0 and cv2.contourArea(ct) > 0.15 * a for ct, h in zip(cts, hier[0]))
        aire = float(alpha[cv2.dilate(m, np.ones((3, 3), np.uint8)) > 0].sum())
        w, h = st[i, cv2.CC_STAT_WIDTH], st[i, cv2.CC_STAT_HEIGHT]
        t = 2 * aire / max(per, 1e-3)
        if not trou:
            for _ in range(6):
                t = 2 * aire / max(per - 2 * t, 1e-3)
        plein = (not trou) and t > 0.45 * min(w, h)
        coeur = cv2.erode(m, np.ones((3, 3), np.uint8)) > 0
        cm = np.median(rgb[coeur], 0) if coeur.sum() >= 4 else np.median(rgb[m > 0], 0)
        uu, vv = (cen[i][0] - cx) / rext, (cy - cen[i][1]) / rext
        out.append(dict(centre_uv=[_r(uu, 3), _r(vv, 3)], largeur_px=int(w), hauteur_px=int(h), largeur_2R=_r(w / D, 3), hauteur_2R=_r(h / D, 3),
                        forme="anneau" if trou else ("plein" if plein else "trait"), epaisseur_px=None if plein else _r(t, 1),
                        epaisseur_2R=None if plein else _r(t / D, 4), couleur=B.hexa(cm), luminance=_r(B.luma(cm)), aire_px=_r(aire, 0)))
    out.sort(key=lambda o: (-o["centre_uv"][1], o["centre_uv"][0]))
    return out[:40]

def composantes(c):
    """Pour une forme en plusieurs morceaux (texte) : nombre de morceaux, hauteurs, boîte d'ensemble."""
    n, lab, st, _ = cv2.connectedComponentsWithStats(c["masque"].astype(np.uint8), connectivity=8)
    if n <= 1:
        return None
    h = st[1:, cv2.CC_STAT_HEIGHT]; w = st[1:, cv2.CC_STAT_WIDTH]
    x0, y0, x1, y1 = c["boite"]
    hautes = h[h >= 0.85 * h.max()]; basses = h[(h < 0.85 * h.max()) & (h >= 0.5 * h.max())]
    return dict(nombre=int(n - 1), hauteur_max_px=int(h.max()), hauteur_des_grandes_lettres_px=_r(np.median(hautes)),
                hauteur_des_petites_lettres_px=_r(np.median(basses)) if len(basses) else None, largeur_mediane_px=_r(np.median(w)),
                hauteurs_px=sorted(int(v) for v in h), boite=[x0, y0, x1, y1], centre=[_r((x0 + x1) / 2), _r((y0 + y1) / 2)],
                note="boite et centre sont ceux des morceaux retenus (le texte), pas ceux de la cible ; les morceaux qui touchent le bord de la cible sont écartés")

# ====================================================================== figures
def fig_courbe(res, titre, autres=None):
    ang = np.arange(0, 360, 5)
    ep = np.array([np.nan if v is None else v for v in res["courbe_5deg"]])
    series = [(titre, ang, ep, (214, 39, 40))]
    if res.get("loi"):
        co = np.array(res["loi"]["coefs"]); th = np.radians(np.arange(0, 360, 1))
        loi = co[0] + co[1] * np.cos(th) + co[2] * np.sin(th) + co[3] * np.cos(2 * th) + co[4] * np.sin(2 * th)
        series.append(("loi ajustée (2 harmoniques)", np.arange(0, 360, 1), loi, (120, 120, 120), "tirets"))
    for nom, v, col in autres or []:
        series.append((nom, ang, np.array([np.nan if x is None else x for x in v]), col))
    tout = np.concatenate([np.asarray(s[2], dtype=float) for s in series])
    ymax = max(2.0, float(np.nanmax(tout)) * 1.25) if np.isfinite(tout).any() else 2.0
    return B.courbe(series, "épaisseur du contour = f(orientation du bord)", "orientation (°) : 0 = droite, 90 = haut, 180 = gauche, 270 = bas", "px",
                    xlim=(0, 360), ylim=(0, ymax), xticks=list(range(0, 361, 45)), bandes=[(45, 135, "haut"), (225, 315, "bas")])

def fig_profils(omb, titre="luminance"):
    p = omb["profils_diametres"]; pos = p["pos_R"]
    series = [(k, pos, [np.nan if v is None else v for v in p[k]]) for k in p if k != "pos_R"]
    return B.courbe(series, titre, "position (−1 = bord gauche / bas, +1 = bord droit / haut)", "lum.", xlim=(-1, 1))

def _cadre(c, rgb, marge):
    if c["type"] == "cercle":
        r = c["r"] * marge
        x0, x1, y0, y1 = c["cx"] - r, c["cx"] + r, c["cy"] - r, c["cy"] + r
    else:
        bx0, by0, bx1, by1 = c["boite"]
        m = (marge - 1) * max(bx1 - bx0, by1 - by0) / 2 + 12
        x0, x1, y0, y1 = bx0 - m, bx1 + m, by0 - m, by1 + m
    return int(max(0, x0)), int(min(rgb.shape[1], x1)), int(max(0, y0)), int(min(rgb.shape[0], y1))

def fig_carte(c, rgb, extra, k_min=420):
    """Carte en fausses couleurs de la luminance du remplissage + carte des deux zones + forme contrastée."""
    peau = extra["peau"]
    x0, x1, y0, y1 = _cadre(c, rgb, 1.08)
    L = c["L"][y0:y1, x0:x1]; pm = peau[y0:y1, x0:x1]
    lo, hi = np.percentile(L[pm], 1), np.percentile(L[pm], 99)
    n = np.clip((L - lo) / max(hi - lo, 1e-3), 0, 1)
    fc = cv2.applyColorMap((n * 255).astype(np.uint8), cv2.COLORMAP_TURBO)[..., ::-1].copy()
    fc[~pm] = (40, 40, 40)
    zones = np.full(L.shape + (3,), 40, np.uint8)
    ys, xs, zc = extra["zones"]
    oky = (ys >= y0) & (ys < y1) & (xs >= x0) & (xs < x1)
    zones[ys[oky] - y0, xs[oky] - x0] = np.where(zc[oky, None], np.array([255, 214, 90]), np.array([60, 110, 220]))
    cont = rgb[y0:y1, x0:x1].copy()
    med = np.median(cont[pm], 0)
    cont = np.clip(med + (cont - med) * 4.0, 0, 255)
    k = max(1, int(round(k_min / max(L.shape))))
    ims = [B.agrandir(a, k) for a in (fc, zones, cont)]
    leg = B.texte_img([f"fausses couleurs : luminance de {lo:.0f} (bleu) à {hi:.0f} (rouge)  |  deux zones (k-moyennes Lab) : jaune = claire, bleu = sombre  |  écarts de couleur × 4"],
                      largeur=sum(i.width for i in ims) + 32, t=14)
    return B.empiler([B.empiler(ims, horizontal=True), leg])

def fig_annotee(c, rgb, res, cible=1300):
    """Image de contrôle : la forme agrandie, les deux bords du trait retrouvés (rouge = bord intérieur, cyan = bord extérieur),
    le cercle ajusté pour un cercle, l'épaisseur écrite tous les 30° d'orientation, les orientations écartées en gris."""
    x0, x1, y0, y1 = _cadre(c, rgb, 1.42)
    k = max(2, int(round(cible / max(x1 - x0, y1 - y0, 1))))
    im = B.agrandir(rgb[y0:y1, x0:x1], k); d = ImageDraw.Draw(im)
    f = B.police(max(15, 5 * k), True); fl = B.police(max(14, 4 * k))
    T = lambda p: ((p[0] - x0) * k, (p[1] - y0) * k)
    cercle = c["type"] == "cercle"
    rp = max(1.5, 0.55 * k)                                  # rayon des points : visibles sans agrandir l'image
    def point(p, coul):
        d.ellipse((p[0] - rp, p[1] - rp, p[0] + rp, p[1] + rp), fill=coul)
    if cercle:
        cx, cy = T((c["cx"], c["cy"])); rr = c["r"] * k
        d.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), outline=(255, 255, 255), width=1)       # cercle ajusté (bord du remplissage)
        d.line((cx - 8, cy, cx + 8, cy), fill=(255, 255, 255)); d.line((cx, cy - 8, cx, cy + 8), fill=(255, 255, 255))
    pin = _points(c, np.nan_to_num(c["rin"])); pout = _points(c, np.nan_to_num(c["rout"]))
    pas = 1 if cercle else max(1, int(round(4 / k)))
    for i in range(0, len(c["ang"]), pas):
        if np.isfinite(c["rin"][i]):
            point(T(pin[i]), (255, 40, 40))
        if np.isfinite(c["rout"][i]):
            point(T(pout[i]), (0, 230, 255))
        elif c["motif"][i]:
            point(T(c["orig"][i] + c["N"][i] * (c["r"] if cercle else 0.0)), (150, 150, 150))
    ep5 = res["courbe_5deg"]
    ech = c["r"] if cercle else max(x1 - x0, y1 - y0) / 2
    for a in range(0, 360, 30):
        v = ep5[a // 5]
        if cercle:
            i = a
        else:                                               # le point valide de cette orientation le plus éloigné du centre (bord extérieur de la forme)
            dist = np.abs(((c["ang"] - a + 180) % 360) - 180)
            cand = np.where((dist <= 2.5) & np.isfinite(c["rout"]))[0]
            if not len(cand):
                continue
            i = int(cand[np.argmax(np.hypot(c["orig"][cand, 0] - c["cx"], c["orig"][cand, 1] - c["cy"]))])
        base = c["rout"][i] if np.isfinite(c["rout"][i]) else (c["r"] if cercle else 0.0)
        p0 = T(c["orig"][i] + c["N"][i] * (base + 0.04 * ech)); p1 = T(c["orig"][i] + c["N"][i] * (base + 0.10 * ech))
        d.line((p0, p1), fill=(255, 255, 0), width=max(2, k // 2))
        t = f"{a}° : " + ("écarté" if v is None else f"{v:.1f} px")
        d.text(T(c["orig"][i] + c["N"][i] * (base + 0.21 * ech)), t, fill=(255, 255, 0), font=f, anchor="mm", stroke_width=3, stroke_fill=(0, 0, 0))
    leg = f"×{k}  rouge = bord intérieur du trait, cyan = bord extérieur, gris = écarté" + (", blanc = cercle ajusté" if cercle else "")
    d.text((6, 4), leg, fill=(255, 255, 255), font=fl, stroke_width=3, stroke_fill=(0, 0, 0))
    d.text((6, im.height - 8), "orientations : 0° = à droite, 90° = en haut, 180° = à gauche, 270° = en bas", fill=(255, 255, 255), font=fl,
           anchor="ls", stroke_width=3, stroke_fill=(0, 0, 0))
    return im
