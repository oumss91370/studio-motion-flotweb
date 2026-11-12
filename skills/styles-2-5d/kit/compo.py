"""Assemblage : des trois passes de Blender à l'image finale, selon les lois mesurées du style.

  python outils/compo.py                  toutes les images du film -> images/f_####.jpg
  python outils/compo.py film             images manquantes, puis sortie/film.mp4 (avec son/mix.wav s'il existe)
  python outils/compo.py A:40,L:9001      quelques images (contrôle) -> images/<plan>_####.jpg
  python outils/compo.py decor A:40       le décor seul, sans personnage ni sous-titre -> images/decor_<plan>_####.png

Ce qui vient de Blender (bl_decor.py) : volumes, textures peintes, part de soleil, lampes, occlusion, normales, profondeur.
Ce qui est fait ICI, parce que le style le dose en diamètres de tête (D) et par ambiance (regles.py) :
  1. la lumière : une ombre est un MÉLANGE de la couleur vers une teinte (87 % de #202d6c au couchant), jamais une multiplication ;
     en intérieur (regles.INTERIEUR), une pièce SOMBRE : pénombre prune, flaques chaudes autour des lampes, froid dans les creux,
     au fond et autour des fenêtres ; occlusion au pied des murs ;
  2. les contours du décor : silhouettes 0,030 D, arêtes 0,012 D, encre de l'ambiance, plus épais vers le bas ;
  3. le lointain peint : ciel en dégradé, soleil et halo, nuages plats, deux rangs de collines ; la brume de distance ;
  4. les halos des lampes ; 5. la profondeur de champ : flou = 0,055 D × |d point / d objet − 1|, sol NET sous les pieds ;
  6. l'assombrissement des bords ; 7. les personnages (pantin.py), leur ombre au sol, l'accentuation finale, les sous-titres.
     En intérieur, si le plan donne sa lampe principale (clé source=(x, y, z)) : ombre projetée à l'opposé de la lampe, liseré
     de lumière chaud côté lampe, et la direction de la lumière sur le personnage (lum_perso) s'en déduit.
Un réglage d'ambiance ne demande donc aucun nouveau rendu Blender.
Dépendances : numpy, opencv-python, Pillow, resvg-py, ffmpeg. Écrit par Flot Web.
"""
import math, os, pathlib, subprocess, sys
sys.dont_write_bytecode = True
ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import numpy as np
import cv2
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import regles as R
import camera as C
import plaque as PQ
import pantin
import film as F

RAC = pathlib.Path(os.environ.get("EPISODE_RACINE", ICI.parent)).resolve()
PASSES, IMAGES, SORTIE = RAC / "passes", RAC / "images", RAC / "sortie"
W, H = R.LARGEUR, R.HAUTEUR
PROF_MAX = R.PROF_MAX
TD = [W, H]                    # taille de travail du décor : celle du cadre, ou celle de la plaque pendant qu'on la prépare
PROCESSUS = int(os.environ.get("EPISODE_PROCESSUS", "2"))      # l'assemblage prend 5 à 7 s par image et par processus, et 2 à 3 Go chacun


def hx(h):
    return np.array(R.hexa(h), dtype=np.float32)

def _v(t):
    return np.array(t, dtype=np.float32)

def _lisse(v, a, b):
    t = np.clip((v - a) / (b - a), 0, 1)
    return t * t * (3 - 2 * t)

def _gris(c):
    return c[..., 0:1] * 0.3 + c[..., 1:2] * 0.59 + c[..., 2:3] * 0.11


# ====================================================================== passes
def passes(k, f):
    return passes_nom(f"{k}_{f:04d}")

def passes_nom(nom):
    nom = nom + ".png"
    for d in ("albedo", "lum", "data"):
        if not (PASSES / d / nom).exists():
            raise FileNotFoundError(f"passe manquante : passes/{d}/{nom} (lancer le rendu : python outils/lancer.py rendre)")
    a = np.asarray(Image.open(PASSES / "albedo" / nom).convert("RGB"), dtype=np.float32)
    l = cv2.imread(str(PASSES / "lum" / nom), cv2.IMREAD_UNCHANGED)[..., ::-1].astype(np.float32) / 65535.0
    d = cv2.imread(str(PASSES / "data" / nom), cv2.IMREAD_UNCHANGED)[..., ::-1].astype(np.float32) / 65535.0
    return a, l, d

def _rayons(base):
    """Direction du rayon de vue de chaque pixel (composante 1 le long de l'axe de la caméra)."""
    pos, right, up, fwd, foc = base
    w, h = TD
    k = (foc / 18.0) * (h / 2)
    xx, yy = np.meshgrid((np.arange(w, dtype=np.float32) - w / 2) / k, (h / 2 - np.arange(h, dtype=np.float32)) / k)
    return [fwd[i] + xx * right[i] + yy * up[i] for i in range(3)]


# ====================================================================== le lointain peint
def ciel_peint(base, P):
    """Ciel : dégradé selon la hauteur au-dessus de l'horizon, soleil et halo, nuages plats à bord doux, deux rangs de collines.
    Ce sont les seuls éléments plats du style : tout ce qui est proche est en volume."""
    dx, dy, dz = _rayons(base)
    n = np.sqrt(dx * dx + dy * dy + dz * dz)
    el = np.degrees(np.arcsin(np.clip(dz / n, -1, 1)))
    az = np.degrees(np.arctan2(dx, -dy))
    ciel = P["ciel"]
    img = np.zeros((TD[1], TD[0], 3), np.float32)
    e = np.clip(el, 0, ciel[-1][0])
    for (e0, c0), (e1, c1) in zip(ciel, ciel[1:]):
        m = (e >= e0) & (e <= e1)
        t = ((e - e0) / (e1 - e0))[..., None]
        img = np.where(m[..., None], hx(c0) * (1 - t) + hx(c1) * t, img)
    img[el < 0] = hx(ciel[0][1])
    if P.get("soleil"):                                    # disque de 0,86 D de rayon environ, halo fondu sur 3 D
        s = -_v(F.SOLEIL); s /= np.linalg.norm(s)
        ang = np.degrees(np.arccos(np.clip((dx * s[0] + dy * s[1] + dz * s[2]) / n, -1, 1)))
        img = img + (hx(P["soleil"][1]) - img) * np.exp(-(ang / 14.0) ** 2)[..., None] * 0.88
        img = img + (hx(P["soleil"][0]) - img) * _lisse(-ang, -2.6, -2.0)[..., None]
    if P.get("nuages"):
        rng = np.random.default_rng(7)
        nu = np.zeros((TD[1], TD[0]), np.float32)
        for (a0, e0, la, ha) in ((-38, 17, 16, 2.6), (-20, 23, 11, 2.0), (16, 14, 15, 2.4), (40, 20, 12, 2.2), (-64, 12, 14, 2.2), (70, 26, 13, 2.4), (5, 31, 9, 1.8)):
            for _ in range(5):
                ca, ce = a0 + rng.uniform(-la, la) * 0.6, e0 + rng.uniform(-0.6, 1.4) * ha
                r = rng.uniform(0.25, 0.5) * la
                nu = np.maximum(nu, 1 - np.hypot((az - ca) / r, (el - ce) / (ha * rng.uniform(0.7, 1.2))))
        nu = _lisse(nu, 0.0, 0.22)[..., None]
        bas, haut = hx(P["nuages"][0]), hx(P["nuages"][1])
        k = np.clip(el / 30.0, 0, 1)[..., None]
        img = img + (bas * (1 - k) + haut * k - img) * nu * 0.9
    for (h0, amp, per), (coul, op) in zip(((2.6, 1.3, 23.0), (1.3, 0.8, 11.0)), P.get("collines") or ()):
        cr = h0 + amp * (np.sin(np.radians(az) * 360 / per) * 0.6 + np.sin(np.radians(az) * 360 / (per * 0.37) + 1.3) * 0.4)
        img = img + (hx(coul) - img) * _lisse(cr - el, -0.12, 0.12)[..., None] * op
    return img


# ====================================================================== la lumière
def eclairer(k, a, l, d, base):
    """Applique les lois de lumière de l'ambiance du plan. Renvoie (image, profondeur, ciel, émissif, petits détails)."""
    plan = F.PLANS[k]
    amb = plan["ambiance"]
    P = R.AMBIANCES[amb]["decor"]
    pos, right, up, fwd, foc = base
    z = d[..., 2] * PROF_MAX
    ciel = z >= PROF_MAX * 0.985
    emis = (l[..., 0] > 0.95) & ~ciel
    dx, dy, dz = _rayons(base)
    part = l[..., 0] / 0.9                                           # part de soleil reçue, calculée dans la matière
    # pénombre : le bord des ombres portées est adouci en proportion de D (0,14 D à mi-longueur ; plus loin, plus doux)
    dpx = R.D_MONDE * (foc / 18.0) * (TD[1] / 2) / np.maximum(z, 0.05)
    doux = part.copy()
    for d0, d1, kk in ((0, 30, 0.20), (30, 75, 0.17), (75, 170, 0.09), (170, 1e9, 0.05)):
        m = (dpx >= d0) & (dpx < d1) & (z < PROF_MAX * 0.98)
        if m.any():
            doux = np.where(m, cv2.GaussianBlur(part, (0, 0), max(0.8, kk * float(np.median(dpx[m])))), doux)
    eclaire = _lisse(doux, 0.08, 0.92)[..., None]
    au_sol = ((pos[2] + z * dz) < 0.05)[..., None]
    detail = (l[..., 2] < 0.01) & ~ciel & ~emis                      # petits détails posés au sol (cailloux, touffes)
    # un caillou lointain ne fait que 1 à 4 px : sa marque (B = 0) s'y mêle à celle du sol et se lirait comme une forte occlusion,
    # donc un POINT NOIR. Dehors, au sol, un creux d'occlusion plus petit que 7 px est un petit détail, pas une ombre.
    if amb != "interieur":
        occ = l[..., 2]
        petit = ((cv2.morphologyEx(occ, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8)) - occ) > 0.10) & au_sol[..., 0] & ~ciel & ~emis
        detail = detail | petit
    pres = cv2.dilate(detail.astype(np.uint8), np.ones((9, 9), np.uint8)).astype(bool)
    ao = np.where(pres, 1.0, 1 - 0.55 * (1 - l[..., 2]) ** 0.8)[..., None]      # occlusion : bande sombre au pied des murs et sous les meubles
    g = l[..., 1][..., None]
    if amb == "interieur":      # intérieur SOMBRE à touches froides : pénombre prune, flaques chaudes des lampes, froid dans les creux et au fond
        tp, fp, kp = P["penombre"]
        c_pen = (a * (1 - fp) + hx(tp) * fp) * kp
        flaque = (1 - np.exp(-g / P["k_lampe"])) ** P.get("gamma_lampe", 1.0)      # la flaque a un bord : hors d'elle, la pièce reste prune
        img = c_pen + (a * _v(P["lumiere"]) - c_pen) * flaque
        img = img + (a * _v(P["soleil_entrant"]) - img) * eclaire * 0.92
        tc, fc = P.get("creux", ("#000000", 0.0))                     # l'occlusion ne noircit pas : elle tire vers le bleu de nuit
        img = img * ao + hx(tc) * (1 - ao) * fc
        tl, fl, zl0, zlk = P["lointain"]                              # les fonds d'intérieur virent au violet
        vl = (fl * (1 - np.exp(-np.maximum(z - zl0, 0) / zlk)))[..., None] * (1 - np.clip(flaque * 1.5, 0, 1))
        img = img * (1 - vl) + hx(tl) * vl
        dehors = plan.get("dehors", "soir")
    else:                       # extérieur : ombre = mélange vers la teinte de l'ambiance ; le bleu MONTE dans l'ombre
        t, fo_sol, fo_face = P["ombre"]
        fo = np.where(au_sol, fo_sol, fo_face)                        # les façades gardent davantage leur couleur locale
        c_omb = a * (1 - fo) + hx(t) * fo
        a_lit = np.where(au_sol, a * _v(P["sol"]), (a * 0.62 + _gris(a) * 0.38) * _v(P["lumiere"]))
        img = c_omb + (a_lit - c_omb) * eclaire
        img = img + a * _v(P["lampe"]) * np.clip(g * 9.0, 0, 1) * P["force_lampe"] * (1 - eclaire)
        img = img * ao
        tb, fb, z0, zk = P["brume"]                                   # brume de distance
        br = (fb * (1 - np.exp(-np.maximum(z - z0, 0) / zk)))[..., None]
        img = img * (1 - br) + hx(tb) * br
        dehors = amb
    img = np.where(emis[..., None], a, img)
    if ciel.any():
        img = np.where(ciel[..., None], ciel_peint(base, R.AMBIANCES[dehors]["decor"]), img)
    return np.clip(img, 0, 255), z, ciel, emis, detail


# ====================================================================== contours du décor
def contours(img, d, z, exclu, base, encre):
    """Contours dessinés, en D : silhouettes (ruptures de profondeur) et arêtes (ruptures de normale), plus épais vers le bas ;
    l'encre est mêlée à la teinte locale, davantage sur les traits fins."""
    nx, ny = d[..., 0], d[..., 1]
    w = 1.0 / np.maximum(z, 0.05)                                      # 1/z est linéaire à l'écran sur un plan : sa dérivée seconde ne réagit qu'aux ruptures
    lap = np.abs(cv2.Laplacian(w, cv2.CV_32F, ksize=1)) / w
    sil = (lap > 0.012) & ~exclu
    gn = np.abs(cv2.Sobel(nx, cv2.CV_32F, 1, 0, ksize=3)) + np.abs(cv2.Sobel(nx, cv2.CV_32F, 0, 1, ksize=3)) + \
        np.abs(cv2.Sobel(ny, cv2.CV_32F, 1, 0, ksize=3)) + np.abs(cv2.Sobel(ny, cv2.CV_32F, 0, 1, ksize=3))
    are = (gn > 0.9) & ~sil & ~exclu
    zf = cv2.erode(z, np.ones((3, 3), np.uint8))                        # l'arête appartient à l'objet de devant
    dpx = R.D_MONDE * (base[4] / 18.0) * (TD[1] / 2) / np.maximum(zf, 0.05)
    larg = np.where(sil, R.DECOR["silhouette"] * dpx, R.DECOR["arete"] * dpx)
    larg[~(sil | are)] = 0
    masque = np.zeros((TD[1], TD[0]), np.float32)
    fin = np.zeros((TD[1], TD[0]), np.float32)
    # un niveau par pixel d'épaisseur : le trait rendu fait (noyau + 1) px, donc noyau = épaisseur voulue − 1.
    # Des paliers plus grossiers épaississent les petits objets d'un plan large (mesuré : 0,047 D au lieu de 0,03 D).
    for a0, a1, s in ((0.0, 2.5, 0), (2.5, 3.5, 2), (3.5, 4.5, 3), (4.5, 5.5, 4), (5.5, 6.5, 5), (6.5, 7.5, 6), (7.5, 9.0, 7),
                      (9.0, 11.0, 9), (11.0, 14.0, 11), (14.0, 1e9, 14)):
        m = ((larg > a0) & (larg <= a1)).astype(np.float32)
        if not m.any():
            continue
        if s == 0:
            m = m * np.clip((larg - 0.5) / 1.1, 0.0, 1.0)               # très loin : un trait d'un à deux pixels, de plus en plus pâle
            m = cv2.GaussianBlur(m, (0, 0), 0.6) * 1.3
        else:
            m = cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (s, s)))
            m = np.maximum(m, np.roll(m, max(1, int(round(0.3 * s))), axis=0))      # le plein : le trait s'épaissit vers le bas
            m = cv2.GaussianBlur(m, (0, 0), 0.7)
        if s <= 2:
            fin = np.maximum(fin, np.clip(m, 0, 1))
        masque = np.maximum(masque, np.clip(m, 0, 1))
    fin = (fin >= masque - 1e-3)[..., None] * (masque > 0)[..., None]
    masque = masque[..., None] * 0.94
    local = cv2.GaussianBlur(img, (0, 0), 3)
    trait = np.where(fin, encre * 0.30 + local * 0.70 * 0.62, encre * 0.88 + local * 0.12 * 0.45)
    return img * (1 - masque) + trait * masque

def halos(img, a, emis, froid=None, chaud=None):
    """Halo des lampes et des flammes : la couleur des surfaces qui brillent, étalée à deux échelles et ajoutée. Le halo a la forme
    de la surface : une lampe RONDE (sphère) donne un disque, une boîte une tache rectangulaire.
    froid = (force proche, force large) : les surfaces froides qui brillent (une fenêtre sur la nuit) gardent leur teinte et
    baignent le mur autour d'elles : c'est le contrepoint froid d'un intérieur chaud."""
    src = a * emis[..., None]
    e = TD[1] / H
    if froid is None:
        h = cv2.GaussianBlur(src, (0, 0), 14 * e) * 0.55 + cv2.GaussianBlur(src, (0, 0), 55 * e) * 0.9
        return np.clip(img + h * _v((1.0, 0.8, 0.55)), 0, 255)
    est_froid = (a[..., 2:3] > a[..., 0:1] * 1.15)
    ch, fr = src * ~est_froid, src * est_froid
    c1, c2 = chaud or (0.55, 0.9)
    h = (cv2.GaussianBlur(ch, (0, 0), 14 * e) * c1 + cv2.GaussianBlur(ch, (0, 0), 55 * e) * c2) * _v((1.0, 0.8, 0.55))
    h = h + cv2.GaussianBlur(fr, (0, 0), 45 * e) * froid[0] + cv2.GaussianBlur(fr, (0, 0), 150 * e) * froid[1]
    return np.clip(img + h, 0, 255)

def _flou_sigma(zf, z, d_foc):
    """Écart type du flou, en px : nul dans la zone nette autour du sujet, 0,055 D × l'écart relatif au-delà."""
    O = R.OPTIQUE
    e = zf / np.maximum(z, 0.05) - 1.0                              # > 0 devant le sujet, < 0 derrière
    ecart = np.where(e > 0, np.maximum(e - O["net_devant"], 0.0), np.maximum(-e - O["net_derriere"], 0.0) / (1 - O["net_derriere"]))
    return np.clip(O["flou"] * d_foc * ecart, 0, O["flou_max"] * d_foc)

def flou_profondeur(img, z, zf, d_foc, force=1.0):
    """Profondeur de champ : le sol reste net sous les pieds, le fond lointain est flou sur 0,14 D.
    force : 1 par défaut ; un plan peut la baisser (clé "flou" du plan) : dans une petite pièce tout est presque dans la zone nette."""
    s = _flou_sigma(zf, z, d_foc) * force
    s[s < 0.6] = 0.0
    smax = float(s.max())
    if smax < 0.6:
        return img
    niveaux = [0.0] + [smax * q for q in (0.12, 0.28, 0.5, 0.75, 1.0)]
    piles = [img] + [cv2.GaussianBlur(img, (0, 0), v) for v in niveaux[1:]]
    out = img.copy()
    for i in range(len(niveaux) - 1):
        lo, hi = niveaux[i], niveaux[i + 1]
        m = (s > lo) & (s <= hi)
        t = ((s - lo) / (hi - lo))[..., None]
        out = np.where(m[..., None], piles[i] * (1 - t) + piles[i + 1] * t, out)
    return out

def bords_sombres(img, force, teinte=None):
    """Assombrissement des coins et du premier plan (−21 % entre le centre et les coins de jour ; davantage en intérieur chaud, vers le prune)."""
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.hypot((xx - W / 2) / (W / 2), (yy - H / 2) / (H / 2)) / math.sqrt(2)
    v = (1 - force * r ** 2.2 - 0.06 * np.clip((yy - 0.8 * H) / (0.2 * H), 0, 1))[..., None]
    if teinte is None:
        return img * v
    return img * v + hx(teinte) * (1 - v) * 0.75

def _point(k, f, base, liste):
    """Profondeur de mise au point : sur les personnages (à plusieurs, sur le plus proche de la médiane avant), sinon le point donné par le film."""
    zs = sorted(C.projette(base, (p[0], p[1], 0.9))[2] for _, p, _ in liste)
    if zs:
        return zs[0]                    # le point est fait sur le personnage LE PLUS PROCHE
    return C.projette(base, F.mise_au_point(k, f))[2]

def decor_brut(k, a, l, d, base):
    """Le décor éclairé, cerné, avec son lointain et ses halos, à la taille des passes reçues. Renvoie (image, profondeur)."""
    TD[0], TD[1] = a.shape[1], a.shape[0]
    try:
        magenta = float(((a[..., 0] > 240) & (a[..., 1] < 20) & (a[..., 2] > 240)).mean())
        if magenta > 0.01:
            print(f"ATTENTION plan {k} : {magenta:.0%} de magenta (matière non compilée), à re-rendre")
        A = R.AMBIANCES[F.PLANS[k]["ambiance"]]["decor"]
        img, z, ciel, emis, detail = eclairer(k, a, l, d, base)
        exclu = ciel | cv2.dilate(detail.astype(np.uint8), np.ones((11, 11), np.uint8)).astype(bool)
        img = contours(img, d, z, exclu, base, hx(A["encre"]))
        img = img + A["contraste_local"] * (img - cv2.GaussianBlur(img, (0, 0), 4.0 * TD[1] / H))      # contraste local des textures
        return halos(np.clip(img, 0, 255), a, emis, A.get("halo_froid"), A.get("halo_chaud")), z
    finally:
        TD[0], TD[1] = W, H

_TRONCONS = None
_PLAQUES = {}
def troncon(k, f):
    """Le tronçon de caméra de l'image f : il dit si le décor vient d'une plaque ou d'un rendu image par image (plaque.py)."""
    global _TRONCONS
    if _TRONCONS is None:
        _TRONCONS = PQ.preparer(F)
    return PQ.troncon_de(_TRONCONS[k], f)

def plaque_finie(k, t):
    """Le décor de la plaque d'un tronçon, éclairé et cerné UNE fois ; il sera recadré pour chaque image."""
    if t["nom"] not in _PLAQUES:
        if len(_PLAQUES) > 3:
            _PLAQUES.clear()
        a, l, d = passes_nom(t["nom"])
        _PLAQUES[t["nom"]] = decor_brut(k, a, l, d, t["base"])
    return _PLAQUES[t["nom"]]

def decor(k, f, liste=None):
    base = C.base(F.PLANS[k], f)
    A = R.AMBIANCES[F.PLANS[k]["ambiance"]]["decor"]
    t = troncon(k, f)
    def _la(nom):
        return all((PASSES / d_ / f"{nom}.png").exists() for d_ in ("albedo", "lum", "data"))
    if t["mode"] == "3d" or (_la(f"{k}_{f:04d}") and not _la(t["nom"])):      # une image isolée (lancer.py rendre A:40) est rendue en 3D, sans plaque
        img, z = decor_brut(k, *passes(k, f), base)
    else:                       # une plaque pour tout le tronçon : homographie ("plaque", "fixe") ou déplacement selon la profondeur ("couches")
        img_p, z_p = plaque_finie(k, t)
        (img,), z, hors = PQ.reprojeter([img_p], z_p, t["base"], base, profondeur=(t["mode"] == "couches"), z_plan=t["z_sujet"])
        if hors > 0.002:
            print(f"ATTENTION {k}:{f} : {hors:.1%} du cadre sort de la plaque {t['nom']} (augmenter regles.PLAQUE['marge'])")
    zf = _point(k, f, base, F.acteurs(k, f) if liste is None else liste)
    img = flou_profondeur(img, z, zf, C.d_px(base, zf), F.PLANS[k].get("flou", 1.0))
    img = bords_sombres(img, *A["bords"])
    return np.clip(img, 0, 255), z, zf


# ====================================================================== personnages
def _coeffs(dst, src):
    """Coefficients de Image.transform(PERSPECTIVE) : envoie le quadrilatère dst (écran) vers src (image source)."""
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); B.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); B.append(v)
    return np.linalg.solve(np.array(A, dtype=np.float64), np.array(B, dtype=np.float64)).tolist()

def lumiere_ecran(k, base, pos=None):
    """Direction d'où vient la lumière sur les personnages, à l'écran (0° = de la droite, 90° = du haut) : c'est elle qui place
    le délié du trait, le filet de lumière, le liseré, et à l'opposé le plein et le croissant d'ombre.
    Dans l'ordre : la clé lum_perso du plan ; sinon sa lampe principale (clé source=(x, y, z)), vue de la poitrine du personnage
    posé en pos (ou du point de mise au point) ; sinon le soleil du film."""
    plan = F.PLANS[k]
    if "lum_perso" in plan:
        return float(plan["lum_perso"])
    _, right, up, _, _ = base
    if plan.get("source"):
        S = plan["source"]
        q = pos if pos is not None else F.mise_au_point(k, plan["a"])
        v = (S[0] - q[0], S[1] - q[1], S[2] - 2.0 * R.D_MONDE)          # la poitrine est à 2 D du sol environ
        return math.degrees(math.atan2(sum(a * b for a, b in zip(v, up)), sum(a * b for a, b in zip(v, right))))
    L = F.SOLEIL
    return math.degrees(math.atan2(-sum(a * b for a, b in zip(L, up)), -sum(a * b for a, b in zip(L, right))))

def quad_ecran(nom, pos, base):
    """Les quatre coins de la toile utile du personnage, à l'écran, et la fonction dessin -> monde."""
    _, right, _, _, _ = base
    m = pantin.echelle(nom)
    P0 = (pos[0], pos[1], 0.0)
    def monde(ux, uy):
        dx, dz = (ux - pantin.AX) * m, (pantin.AY - uy) * m
        return (P0[0] + right[0] * dx, P0[1] + right[1] * dx, dz)
    coins = [(pantin.AX - 560, pantin.AY - 1180), (pantin.AX + 560, pantin.AY - 1180), (pantin.AX + 560, pantin.AY + 60), (pantin.AX - 560, pantin.AY + 60)]
    ecran = [C.projette(base, monde(*c))[:2] for c in coins]
    return coins, ecran, monde

def silhouette(k, nom, pos, p, base):
    """Le masque du personnage dans le cadre (0 à 1), tel que pose_perso le dessine : sert au contrôle de ce qui entre dans le champ."""
    coins_u, ecran, _ = quad_ecran(nom, pos, base)
    larg = max(math.dist(ecran[0], ecran[1]), math.dist(ecran[3], ecran[2]))
    zoom = max(0.08, min(2.4, larg / 1120 * 1.05))
    spr, _ = pantin.rendre(nom, dict(p, amb=F.PLANS[k]["ambiance"], lum=lumiere_ecran(k, base, pos)), zoom)
    src = [(ux * zoom, uy * zoom) for ux, uy in coins_u]
    al = spr.getchannel("A").transform((W, H), Image.PERSPECTIVE, _coeffs(ecran, src), Image.BILINEAR)
    return np.asarray(al, dtype=np.float32) / 255.0

def pose_perso(img, z, k, nom, pos, p, base, zf=None):
    cam, right, up, fwd, foc = base
    plan = F.PLANS[k]
    amb = plan["ambiance"]
    A = R.AMBIANCES[amb]
    pxs, pys, zc = C.projette(base, (pos[0], pos[1], 0.0))
    coins_u, ecran, monde = quad_ecran(nom, pos, base)
    larg = max(math.dist(ecran[0], ecran[1]), math.dist(ecran[3], ecran[2]))
    zoom = max(0.08, min(2.4, larg / 1120 * 1.05))
    lum = lumiere_ecran(k, base, pos)
    p = dict(p, amb=amb, lum=lum)
    S = plan.get("source") if amb == "interieur" else None            # la lampe principale du plan
    if S and math.hypot(pos[0] - S[0], pos[1] - S[1]) < 0.15:
        S = None                                                        # lampe à la verticale du personnage : pas de direction
    spr, _ = pantin.rendre(nom, p, zoom)
    src = [(ux * zoom, uy * zoom) for ux, uy in coins_u]
    d_px = R.D_DESSIN * larg / 1120.0                                   # diamètre de la tête à l'écran
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    devant = (z > zc - 6.0)
    om = A["ombre_sol"]
    teinte, force = hx(om[1]), om[2]
    if om[0] == "projetee":     # soleil : la silhouette projetée au sol, attachée aux pieds, nette au contact, de plus en plus douce en s'éloignant
        L = F.SOLEIL
        court = om[4]
        def sol(q):
            t = q[2] / -L[2] * court
            return (q[0] + L[0] * t, q[1] + L[1] * t, 0.0)
        while court > 0.15 and min(C.projette(base, sol(monde(*c)))[2] for c in coins_u) < 0.6:
            court *= 0.85                                               # l'ombre vient vers la caméra : on la raccourcit pour qu'elle reste devant l'objectif
        omb = [C.projette(base, sol(monde(*c)))[:2] for c in coins_u]
        try:
            al = spr.getchannel("A").transform((W, H), Image.PERSPECTIVE, _coeffs(omb, src), Image.BILINEAR)
            al = al.point(lambda v: 0 if v < 96 else 255 if v > 160 else int((v - 96) * 255 / 64))
            net = np.asarray(al.filter(ImageFilter.GaussianBlur(max(1.0, 0.02 * d_px))), dtype=np.float32) / 255.0
            doux = np.asarray(al.filter(ImageFilter.GaussianBlur(max(1.0, om[3] * d_px))), dtype=np.float32) / 255.0
            dist = np.hypot(xx - pxs, yy - pys)
            loin = np.clip(dist / (1.4 * d_px), 0, 1)
            al = net * (1 - loin) + doux * loin
            tres_loin = np.clip((dist - 2.0 * d_px) / (3.0 * d_px), 0, 1)
            if tres_loin.max() > 0:
                large = np.asarray(Image.fromarray((np.clip(al, 0, 1) * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.17 * d_px)), dtype=np.float32) / 255.0
                al = al * (1 - tres_loin) + large * tres_loin
            contact = np.exp(-(((xx - pxs) / (0.34 * d_px)) ** 2 + ((yy - pys - 0.015 * d_px) / (0.05 * d_px)) ** 2))
            al = (np.maximum(al, 0.5 * contact) * devant)[..., None] * force
            img[:] = img * (1 - al) + teinte * al
        except np.linalg.LinAlgError:
            pass
    elif S:                     # intérieur, lampe connue : l'ombre est PROJETÉE au sol à l'opposé de la lampe, nette aux pieds, douce et pâle au bout
        O = R.INTERIEUR["ombre"]
        teinte, force = hx(O["teinte"]), O["force"]
        haut = max(monde(*c)[2] for c in coins_u)
        sz = max(S[2], 1.25 * haut)                                     # une lampe basse donnerait une ombre infinie : on la remonte, sa direction reste
        h_p = min(pantin.PERSOS[nom].get("h", 1.65), 0.8 * haut)
        lg = math.hypot(pos[0] - S[0], pos[1] - S[1]) * h_p / (sz - h_p)
        court = min(max(lg, O["longueur"][0] * R.D_MONDE), O["longueur"][1] * R.D_MONDE) / lg
        def sol_s(q):
            t = (sz / (sz - q[2]) - 1.0) * court
            return (q[0] + (q[0] - S[0]) * t, q[1] + (q[1] - S[1]) * t, 0.0)
        while court > 0.1 and min(C.projette(base, sol_s(monde(*c)))[2] for c in coins_u) < 0.6:
            court *= 0.85                                               # l'ombre vient vers la caméra : elle reste devant l'objectif
        al = np.zeros((H, W), np.float32)
        for cote in ("pied_g", "pied_d"):                               # une ombre de contact, plus sombre, sous CHAQUE pied
            jx, jy = p.get(cote, (0.0, 0.0))
            fx, fy, _ = C.projette(base, monde(pantin.AX + (p.get("x", 0.0) + jx) * pantin.D, pantin.AY - jy * pantin.D))
            al = np.maximum(al, O.get("contact", 0.9) * np.exp(-(((xx - fx) / (0.20 * d_px)) ** 2 + ((yy - fy - 0.02 * d_px) / (0.055 * d_px)) ** 2)))
        try:
            omb = [C.projette(base, sol_s(monde(*c)))[:2] for c in coins_u]
            pr = spr.getchannel("A").transform((W, H), Image.PERSPECTIVE, _coeffs(omb, src), Image.BILINEAR)
            pr = pr.point(lambda v: 0 if v < 96 else 255 if v > 160 else int((v - 96) * 255 / 64))
            net = np.asarray(pr.filter(ImageFilter.GaussianBlur(max(1.0, O["flou"][0] * d_px))), dtype=np.float32) / 255.0
            doux = np.asarray(pr.filter(ImageFilter.GaussianBlur(max(1.5, O["flou"][1] * d_px))), dtype=np.float32) / 255.0
            bx, by, _ = C.projette(base, sol_s((pos[0], pos[1], h_p)))  # le bout de l'ombre : celle de la tête
            loin = np.clip(np.hypot(xx - pxs, yy - pys) / max(math.hypot(bx - pxs, by - pys), 1.0), 0, 1)
            al = np.maximum(al, (net * (1 - loin) + doux * loin) * (1 - (1 - O["fin"]) * loin))
        except np.linalg.LinAlgError:
            pass
        au_sol = (cam[2] + z * _rayons(base)[2]) < 0.09                 # l'ombre ne se pose que sur le sol, pas sur un meuble qu'elle traverse
        al = (al * devant * au_sol)[..., None] * force
        img[:] = img * (1 - al) + teinte * al
    else:                       # lampes ou nuit : pas d'ombre nette ; une tache sous les pieds, une ombre de contact, une ombre courte et très douce à l'opposé de la lumière
        tache = np.exp(-(((xx - pxs) / (0.70 * d_px)) ** 2 + ((yy - pys - 0.04 * d_px) / (0.20 * d_px)) ** 2))
        contact = np.exp(-(((xx - pxs) / (0.45 * d_px)) ** 2 + ((yy - pys - 0.015 * d_px) / (0.06 * d_px)) ** 2))
        al = np.maximum(0.95 * tache, contact)
        a_l = math.radians(lum)
        Li = (-math.cos(a_l) * right[0] * 0.55 - fwd[0] * 0.25, -math.cos(a_l) * right[1] * 0.55 - fwd[1] * 0.25, -1.0)
        def sol_i(q):
            t = q[2] * 0.42
            return (q[0] + Li[0] * t, q[1] + Li[1] * t, 0.0)
        try:
            omb = [C.projette(base, sol_i(monde(*c)))[:2] for c in coins_u]
            pr = spr.getchannel("A").transform((W, H), Image.PERSPECTIVE, _coeffs(omb, src), Image.BILINEAR)
            pr = np.asarray(pr.filter(ImageFilter.GaussianBlur(max(2.0, om[3] * d_px))), dtype=np.float32) / 255.0
            al = np.maximum(al, pr)
        except np.linalg.LinAlgError:
            pass
        al = (al * devant)[..., None] * force
        img[:] = img * (1 - al) + teinte * al
    warp = spr.transform((W, H), Image.PERSPECTIVE, _coeffs(ecran, src), Image.BICUBIC)
    if zf:                      # un personnage hors du plan de netteté est flou comme le décor à la même profondeur
        sg = float(_flou_sigma(zf, np.array(zc, dtype=np.float32), C.d_px(base, zf)))
        if sg >= 0.7:
            warp = warp.filter(ImageFilter.GaussianBlur(sg))
    s = np.asarray(warp, dtype=np.float32)
    if amb == "interieur":      # accord à la pièce : un peu plus chaud et plus sombre vers les pieds ; les blancs et les hautes lumières sont épargnés
        ys0 = min(e_[1] for e_ in ecran); haut_p = max(pys - ys0, 1.0)
        bas = np.clip((yy - ys0) / haut_p, 0, 1)[..., None]
        Ac = R.INTERIEUR["accord"]
        clair = _lisse(_gris(s[..., :3]), Ac["clairs"][0], Ac["clairs"][1]) * Ac["clairs"][2]
        accord = _v(Ac["teinte"]) * (1.0 - Ac["bas"] * bas ** 1.6)
        s[..., :3] = s[..., :3] * (accord * (1 - clair) + clair)
        if S:                   # liseré de lumière chaud sur le bord du personnage, du côté de la lampe ; rien sur l'encre (trait, membres)
            Lz = R.INTERIEUR["lisere"]
            a_s = s[..., 3] / 255.0
            ux, uy = math.cos(math.radians(lum)), -math.sin(math.radians(lum))
            def vers(w):        # le masque lu à w D en direction de la lampe
                return cv2.warpAffine(a_s, np.float32([[1, 0, -w * d_px * ux], [0, 1, -w * d_px * uy]]), (W, H), flags=cv2.INTER_LINEAR)
            rim = a_s * vers(Lz["retrait"]) * (1 - vers(Lz["retrait"] + Lz["largeur"]))
            rim = cv2.GaussianBlur(rim, (0, 0), max(0.6, 0.004 * d_px))[..., None] * Lz["force"]
            g_ = _gris(s[..., :3]) / 255.0
            mel = s[..., :3] + (hx(Lz["teinte"]) - s[..., :3]) * rim * np.clip((g_ - 0.14) / 0.25, 0, 1)
            # le liseré réchauffe sans jamais assombrir : sur la peau claire il ne doit pas se lire comme une ombre du côté de la lampe
            s[..., :3] = np.clip(mel * np.maximum(1.0, g_ * 255.0 / np.maximum(_gris(mel), 1.0)), 0, 255)
    al = s[..., 3:4] / 255.0
    al = al * (z[..., None] > zc - 0.35)                              # caché par ce qui est devant lui
    img[:] = img * (1 - al) + s[..., :3] * al


# ====================================================================== sous-titres
_POLICE = None
def police():
    global _POLICE
    if _POLICE is None:
        S = R.SOUS_TITRES
        cand = [str(p) for p in (RAC / "polices").glob("*.ttf")] + list(S["polices"])
        for nom in cand:
            try:
                _POLICE = ImageFont.truetype(nom, S["corps"]); break
            except OSError:
                continue
        if _POLICE is None:
            raise SystemExit("aucune police grasse trouvée : déposer un fichier .ttf (Montserrat Black, par exemple) dans <episode>/polices/")
    return _POLICE

def sous_titre(im, f):
    """1 à 2 mots, minuscules avec capitale initiale, blanc, contour sombre et ombre décalée ; apparition et disparition sèches."""
    S = R.SOUS_TITRES
    for a, b, txt in F.CARTONS:
        if a <= f < b:
            d = ImageDraw.Draw(im)
            x, y = W / 2, S["y_centre"]
            d.text((x + S["ombre"][0], y + S["ombre"][1]), txt, font=police(), fill=S["contour"], anchor="mm", stroke_width=S["contour_px"] + 1, stroke_fill=S["contour"])
            d.text((x, y), txt, font=police(), fill=S["couleur"], anchor="mm", stroke_width=S["contour_px"], stroke_fill=S["contour"])
            return


# ====================================================================== image complète
def particules(img, k, f, d_px):
    """Quelques points clairs qui flottent devant la scène, en intérieur (regles.INTERIEUR["particules"]) : de petits disques doux,
    chauds, qui dérivent lentement. Leur place ne dépend que du plan et de l'image : le film est reproductible."""
    Pa = R.INTERIEUR.get("particules")
    if not Pa or not Pa["n"]:
        return
    rng = np.random.default_rng(sum(ord(c) for c in k) * 131 + 7)
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    t = (f - F.PLANS[k]["a"]) / R.IPS
    voile = np.zeros((H, W), np.float32)
    for _ in range(Pa["n"]):
        x0, y0, r = rng.uniform(0, W), rng.uniform(0.08 * H, 0.8 * H), rng.uniform(*Pa["rayon"]) * d_px
        a, v, ph = rng.uniform(0, 2 * math.pi), rng.uniform(0.4, 1.0) * Pa["derive"] * d_px, rng.uniform(0, 6.28)
        x = x0 + math.cos(a) * v * t + 0.3 * r * math.sin(2.0 * t + ph)
        y = y0 - abs(math.sin(a)) * v * t
        voile = np.maximum(voile, rng.uniform(0.5, 1.0) * np.exp(-((xx - x) ** 2 + (yy - y) ** 2) / (2 * max(r, 1.2) ** 2)))
    img[:] = img + (hx(Pa["teinte"]) - img) * (voile * Pa["force"])[..., None]

def image_plan(k, f, persos=True):
    base = C.base(F.PLANS[k], f)
    liste = F.acteurs(k, f) if persos else []
    img, z, zf = decor(k, f, liste)
    liste = sorted(liste, key=lambda t: -C.projette(base, (t[1][0], t[1][1], 0))[2])      # du plus loin au plus près
    for nom, pos, p in liste:
        pose_perso(img, z, k, nom, pos, p, base, zf)
    if persos and F.PLANS[k]["ambiance"] == "interieur":
        particules(img, k, f, C.d_px(base, zf))
    return img

def image(f, sous_titres=True):
    """Image f du film : un plan, ou le fondu enchaîné de deux plans qui se recouvrent."""
    actifs = C.plans_de(F, f)
    if not actifs:
        raise ValueError(f"aucun plan ne couvre l'image {f}")
    img = sum(image_plan(k, f) * w for k, w in actifs)
    im = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    if R.ACCENTUATION:          # accentuation finale : un pixel plus clair côté aplat, un pixel plus sombre dans le trait
        im = im.filter(ImageFilter.UnsharpMask(radius=1.0, percent=R.ACCENTUATION, threshold=0))
    if sous_titres:
        sous_titre(im, f)
    return im

def image_fixe(k, f, persos=True):
    im = Image.fromarray(np.clip(image_plan(k, f, persos), 0, 255).astype(np.uint8))
    return im.filter(ImageFilter.UnsharpMask(radius=1.0, percent=R.ACCENTUATION, threshold=0)) if R.ACCENTUATION else im

def _une(f):
    import gc, time
    out = IMAGES / f"f_{f:04d}.jpg"
    if out.exists():
        return f
    for essai in range(4):
        try:
            image(f).save(out, quality=95)
            return f
        except MemoryError:
            gc.collect(); time.sleep(3 + 4 * essai)
    raise MemoryError(f"image {f}")

def encoder():
    SORTIE.mkdir(parents=True, exist_ok=True)
    manque = [f for f in range(F.TOTAL) if not (IMAGES / f"f_{f:04d}.jpg").exists()]
    if manque:
        raise SystemExit(f"{len(manque)} images manquent (première : {manque[0]}) : relancer python outils/compo.py")
    cmd = ["ffmpeg", "-v", "error", "-y", "-framerate", str(R.IPS), "-start_number", "0", "-i", str(IMAGES / "f_%04d.jpg")]
    son = RAC / "son" / "mix.wav"
    if son.exists():
        cmd += ["-i", str(son), "-c:a", "aac", "-b:a", "192k", "-shortest"]
    cmd += ["-frames:v", str(F.TOTAL), "-c:v", "libx264", "-preset", "slow", "-crf", "14", "-pix_fmt", "yuv420p", "-r", str(R.IPS),
            "-movflags", "+faststart", str(SORTIE / "film.mp4")]
    subprocess.run(cmd, check=True)
    print("sortie/film.mp4 écrit" + ("" if son.exists() else " (sans son : son/mix.wav absent)"))

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__); return
    IMAGES.mkdir(parents=True, exist_ok=True)
    arg = sys.argv[1] if len(sys.argv) > 1 else "tout"
    if arg == "decor":
        for x in sys.argv[2].split(","):
            k, f = x.split(":")[0], int(x.split(":")[1])
            image_fixe(k, f, persos=False).save(IMAGES / f"decor_{k}_{f:04d}.png")
            print("décor", k, f)
        return
    if arg not in ("tout", "film"):
        for x in arg.split(","):
            k, f = x.split(":")[0], int(x.split(":")[1])
            image_fixe(k, f).save(IMAGES / f"{k}_{f:04d}.jpg", quality=95)
            print("image", k, f)
        return
    from multiprocessing import Pool
    with Pool(PROCESSUS, maxtasksperchild=10) as pool:
        for i, f in enumerate(pool.imap_unordered(_une, range(F.TOTAL))):
            if i % 30 == 0:
                print("image", f, flush=True)
    if arg == "film":
        encoder()

if __name__ == "__main__":
    main()
