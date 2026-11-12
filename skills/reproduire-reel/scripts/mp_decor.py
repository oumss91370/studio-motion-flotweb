"""Mesures au pixel du DÉCOR : matières, contours, ombres, lumières, palette, densité, netteté, optique.

Mêmes fonctions pour la référence et pour nos rendus (contrôle chiffré). Chaque fonction renvoie un dictionnaire de
chiffres simples (JSON). Conventions de mp_base : x vers la droite, y vers le bas, luminance Rec. 709 sur sRVB 0–255.

`bande` désigne partout une bande horizontale à exclure des mesures globales : (y0, y1) en pixels, typiquement celle des
sous-titres. None = rien d'exclu. La même bande doit être exclue des DEUX côtés d'une comparaison.

Mesures ciblées (une cible posée à la main) : bord, trait, texture, zone, details, halo, optique, nettete_boite.
Mesures globales (image entière) : palette, regions, degrade, densite, grain, vignettage, nettete_carte, nettete_resume.
Écrit par Flot Web (skill `reproduire-reel`).
"""
import sys
sys.dont_write_bytecode = True
import math
import numpy as np
import cv2
from mp_base import luma, hexa, de_hexa, lab, de2000, tsl

# ------------------------------------------------------------------ outils
def masque_global(h, w, bande=None):
    """Masque des pixels comptés dans les mesures globales (tout, sauf la bande exclue)."""
    m = np.ones((h, w), bool)
    if bande:
        m[max(0, int(bande[0])):max(0, int(bande[1])), :] = False
    return m

def _echant(img, xs, ys):
    return cv2.remap(img, xs.astype(np.float32), ys.astype(np.float32), cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)

def coupe(img, a, b, larg=9, pas=0.25):
    """Profil RVB le long du segment a → b, moyenné sur `larg` px en travers. Renvoie (abscisses en px, rvb (n, 3))."""
    (x0, y0), (x1, y1) = a, b
    L = math.hypot(x1 - x0, y1 - y0)
    if L < 2:
        raise ValueError("les deux bouts du segment sont au même point")
    n = max(8, int(L / pas))
    t = np.linspace(0, 1, n)
    ux, uy = (x1 - x0) / L, (y1 - y0) / L
    k = np.arange(larg) - (larg - 1) / 2
    xs = x0 + (x1 - x0) * t[None, :] + (-uy) * k[:, None]
    ys = y0 + (y1 - y0) * t[None, :] + (ux) * k[:, None]
    return t * L, _echant(img, xs, ys).mean(axis=0)

def _lisse(v, n):
    if n <= 1:
        return v
    k = np.ones(n) / n
    return np.convolve(np.pad(v, (n // 2, n - 1 - n // 2), mode="edge"), k, mode="valid")

def _croise(s, v, niveau, pres):
    """Abscisse où v croise `niveau`, au plus près de l'indice `pres` (interpolation linéaire)."""
    d = v - niveau
    idx = np.where(d[:-1] * d[1:] <= 0)[0]
    if len(idx) == 0:
        return None
    i = idx[np.argmin(np.abs(idx - pres))]
    den = v[i + 1] - v[i]
    return float(s[i] + (s[i + 1] - s[i]) * ((niveau - v[i]) / den if den else 0.0))

def _boite(img, boite):
    h, w = img.shape[:2]
    x0, y0, x1, y1 = [int(round(v)) for v in boite]
    x0, x1 = sorted((max(0, min(w, x0)), max(0, min(w, x1)))); y0, y1 = sorted((max(0, min(h, y0)), max(0, min(h, y1))))
    if x1 - x0 < 4 or y1 - y0 < 4:
        raise ValueError(f"la boîte {list(boite)} est vide ou hors de l'image ({w} × {h})")
    return x0, y0, x1, y1

def _patch(img, boite, angle=0.0):
    x0, y0, x1, y1 = _boite(img, boite)
    if angle:
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        M = cv2.getRotationMatrix2D((cx, cy), -angle, 1.0)       # redresse des lignes penchées de `angle` degrés
        img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    return img[y0:y1, x0:x1]

# ------------------------------------------------------------------ mesures ciblées
def bord(img, a, b, larg=9):
    """Transition entre deux plages (bord d'une ombre portée, bord flou d'un objet du fond) : couleurs des deux côtés,
    largeur 10–90 %, dépassement (accentuation), décalage rouge / bleu (aberration chromatique), facteur par canal."""
    s, rvb = coupe(img, a, b, larg)
    v = _lisse(luma(rvb), 5)
    n = len(v); q = max(4, n // 7)
    c0, c1 = np.median(rvb[:q], axis=0), np.median(rvb[-q:], axis=0)
    p0, p1 = float(np.median(v[:q])), float(np.median(v[-q:]))
    amp = p1 - p0
    if abs(amp) < 3:
        return dict(erreur="pas de contraste entre les deux bouts du segment", cote_a=hexa(c0), cote_b=hexa(c1))
    g = np.abs(np.gradient(_lisse(v, 9)))
    i50 = int(np.argmax(g))
    x10, x90 = (_croise(s, v, p0 + amp * f, i50) for f in (0.1, 0.9))
    larg1090 = abs(x90 - x10) if x10 is not None and x90 is not None else None
    hi, lo = max(p0, p1), min(p0, p1)
    xr = _croise(s, _lisse(rvb[:, 0], 5), (c0[0] + c1[0]) / 2, i50) if abs(c1[0] - c0[0]) > 6 else None
    xb = _croise(s, _lisse(rvb[:, 2], 5), (c0[2] + c1[2]) / 2, i50) if abs(c1[2] - c0[2]) > 6 else None
    sombre, clair = (c0, c1) if p0 < p1 else (c1, c0)
    ts, tc = tsl(sombre), tsl(clair)
    return dict(cote_a=hexa(c0), cote_b=hexa(c1), luminance_a=round(p0, 1), luminance_b=round(p1, 1),
                cote_clair=hexa(clair), cote_sombre=hexa(sombre),
                largeur_10_90_px=None if larg1090 is None else round(larg1090, 2),
                depassement_clair=round(float(v.max() - hi), 1), depassement_sombre=round(float(lo - v.min()), 1),
                decalage_rouge_bleu_px=None if xr is None or xb is None else round(xr - xb, 2),
                facteur_rvb=[round(float(sombre[i] / max(clair[i], 1)), 2) for i in range(3)],
                rapport_luminance=round(lo / max(hi, 1), 3),
                ecart_tsl=dict(teinte=round(((ts[0] - tc[0] + 180) % 360) - 180, 1), saturation=round(ts[1] - tc[1], 1), luminosite=round(ts[2] - tc[2], 1)),
                delta_e=round(de2000(c0, c1), 1))

def trait(img, a, b, larg=7, clair=False):
    """Trait sombre (contour dessiné, joint) traversé par le segment a → b : épaisseur à mi-profondeur, couleur, plages voisines.
    clair=True : liseré clair (arêtes éclairées de nuit) au lieu d'un trait sombre."""
    s, rvb = coupe(img, a, b, larg)
    v = _lisse(luma(rvb), 3)
    if clair:
        v = 255.0 - v
    n = len(v); q = max(4, n // 6)
    p0, p1 = float(np.median(v[:q])), float(np.median(v[-q:]))
    i = int(np.argmin(v[q // 2:n - q // 2])) + q // 2
    vmin = float(v[i])
    prof = min(p0, p1) - vmin
    ca, cb = hexa(np.median(rvb[:q], axis=0)), hexa(np.median(rvb[-q:], axis=0))
    if prof < 6:
        return dict(trait=False, profondeur=round(prof, 1), cote_a=ca, cote_b=cb)
    xa = _croise(s[:i + 1], v[:i + 1], (p0 + vmin) / 2, i)
    xb = _croise(s[i:], v[i:], (p1 + vmin) / 2, 0)
    coeur = v <= vmin + 0.25 * prof
    coeur[:max(0, i - 200)] = False
    return dict(trait=True, epaisseur_px=None if xa is None or xb is None else round(xb - xa, 2), couleur=hexa(np.median(rvb[coeur], axis=0)),
                luminance_trait=round(vmin if not clair else 255.0 - vmin, 1), profondeur=round(prof, 1), cote_a=ca, cote_b=cb)

def texture(img, boite, axe="x", angle=0.0):
    """Texture d'une matière dans un rectangle. `axe` = direction dans laquelle on TRAVERSE les lignes (planches verticales → "x").
    Sort : contraste (écart type et p95–p5 après retrait des basses fréquences), période dominante (autocorrélation),
    lignes sombres (nombre, épaisseur, espacement, profondeur, couleur), grain fin, dégradé de lumière sur la zone."""
    p = _patch(img, boite, angle)
    L = luma(p)
    bas = cv2.GaussianBlur(L, (0, 0), 25)
    d = L - bas
    fin = L - cv2.GaussianBlur(L, (0, 0), 1.2)
    prof_rvb = p.mean(axis=0 if axe == "x" else 1)
    prof = luma(prof_rvb)
    n = len(prof)
    pd = prof - _lisse(prof, max(9, n // 4) | 1)
    ac = np.correlate(pd, pd, mode="full")[n - 1:]
    ac = ac / (ac[0] + 1e-9)
    periode, force = None, 0.0
    for k in range(3, n // 2):
        if ac[k] > ac[k - 1] and ac[k] >= ac[k + 1] and ac[k] > 0.12:
            if ac[k] > force * 1.15:
                periode, force = k, float(ac[k])
            if periode and k > periode * 1.6:
                break
    med = float(np.median(pd)); mn = float(np.percentile(pd, 2))
    seuil = med - max(2.5, 0.5 * (med - mn))
    sous = pd < seuil
    lignes, i = [], 0
    while i < n:
        if sous[i]:
            j = i
            while j < n and sous[j]:
                j += 1
            if 0 < i and j < n:
                lignes.append((i, j))
            i = j
        else:
            i += 1
    larg = [j - i for i, j in lignes]
    centres = [(i + j) / 2 for i, j in lignes]
    esp = np.diff(centres) if len(centres) > 1 else []
    idx = np.zeros(n, bool)
    for i, j in lignes:
        idx[i:j] = True
    return dict(taille=[int(p.shape[1]), int(p.shape[0])], couleur_mediane=hexa(np.median(p.reshape(-1, 3), axis=0)),
                contraste_ecart_type=round(float(d.std()), 2), contraste_p95_p5=round(float(np.percentile(d, 95) - np.percentile(d, 5)), 1),
                profil_p95_p5=round(float(np.percentile(pd, 95) - np.percentile(pd, 5)), 1),
                periode_px=periode, force_periode=round(force, 2),
                lignes=len(lignes), ligne_epaisseur_px=round(float(np.median(larg)), 1) if larg else None,
                ligne_espacement_px=round(float(np.median(esp)), 1) if len(esp) else None,
                ligne_profondeur=round(float(med - pd[idx].mean()), 1) if idx.any() else None,
                couleur_lignes=hexa(prof_rvb[idx].mean(axis=0)) if idx.any() else None,
                couleur_fond=hexa(prof_rvb[~idx].mean(axis=0)) if (~idx).any() else None,
                grain_fin=round(float(fin.std()), 2),
                degrade_niveaux=round(float(np.percentile(bas, 98) - np.percentile(bas, 2)), 1))

def zone(img, boite):
    """Couleur médiane d'un rectangle (sol éclairé, sol à l'ombre, face d'un volume, ciel)."""
    p = _patch(img, boite).reshape(-1, 3)
    c = np.median(p, axis=0)
    return dict(couleur=hexa(c), luminance=round(float(luma(c)), 1), ecart_type=round(float(luma(p).std()), 2), tsl=[round(x, 1) for x in tsl(c)])

def details(img, boite, D):
    """Petits détails posés sur une surface (cailloux, touffes, papiers, taches) : nombre, taille (en D), densité par D².
    D = grandeur de référence en px (diamètre de la tête du personnage)."""
    if not D:
        raise ValueError("la mesure « details » a besoin de la grandeur de référence D (champ \"reference\" du fichier de cibles, ou \"D\" dans la cible)")
    p = _patch(img, boite)
    fond = cv2.medianBlur(np.clip(p, 0, 255).astype(np.uint8), 51).astype(np.float32)
    ecart = np.linalg.norm(lab(p) - lab(fond), axis=-1)
    m = (ecart > 7).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    n, _, st, _ = cv2.connectedComponentsWithStats(m, connectivity=8)
    aires = st[1:, cv2.CC_STAT_AREA]
    ok = aires[(aires >= 12) & (aires <= 0.02 * m.size)]
    diam = np.sqrt(4 * ok / math.pi) if len(ok) else np.array([])
    surf_D2 = m.size / (D * D)
    return dict(nombre=int(len(ok)), diametre_median_px=round(float(np.median(diam)), 1) if len(diam) else None,
                diametre_median_D=round(float(np.median(diam) / D), 3) if len(diam) else None,
                diametre_max_D=round(float(diam.max() / D), 3) if len(diam) else None,
                densite_par_D2=round(len(ok) / surf_D2, 2), part_couverte_pct=round(float(100 * ok.sum() / m.size), 2),
                contraste_fond=round(float(luma(p - fond).std()), 2))

def halo(img, centre, rmax):
    """Lumière ponctuelle (lampe, soleil) : profil radial de luminance, rayon à mi-hauteur, couleur au cœur, à mi-rayon, au bord."""
    cx, cy = centre
    h, w = img.shape[:2]
    if rmax < 12:
        raise ValueError("rmax trop petit (12 px au moins)")
    yy, xx = np.mgrid[max(0, int(cy - rmax)):min(h, int(cy + rmax)), max(0, int(cx - rmax)):min(w, int(cx + rmax))]
    if yy.size == 0:
        raise ValueError(f"le centre {list(centre)} est hors de l'image ({w} × {h})")
    r = np.hypot(xx - cx, yy - cy)
    sub = img[yy, xx]
    Ls = luma(sub)
    prof = np.array([Ls[(r >= k) & (r < k + 2)].mean() if ((r >= k) & (r < k + 2)).any() else np.nan for k in range(0, int(rmax) - 2, 2)])
    fond, coeur = float(np.nanmean(prof[-5:])), float(np.nanmean(prof[:3]))
    mi = fond + (coeur - fond) / 2
    k = next((i for i, v in enumerate(prof) if v < mi), len(prof) - 1)
    def med(m):
        return hexa(np.median(sub[m], axis=0)) if m.any() else None
    return dict(luminance_coeur=round(coeur, 1), luminance_fond=round(fond, 1), rayon_mi_hauteur_px=k * 2,
                couleur_coeur=med(r < 6), couleur_mi_rayon=med((r > k * 2 - 3) & (r < k * 2 + 3)), couleur_fond=med((r > rmax - 8) & (r < rmax)))

def fuite(l1, l2):
    """Point de fuite de deux droites (chacune = deux points)."""
    def droite(p, q):
        return np.cross([p[0], p[1], 1.0], [q[0], q[1], 1.0])
    v = np.cross(droite(*l1), droite(*l2))
    return None if abs(v[2]) < 1e-9 else (float(v[0] / v[2]), float(v[1] / v[2]))

def optique(verticales, horizon_y, h, w):
    """Focale à partir de deux verticales du décor (chacune = deux points) et de la ligne d'horizon : f² = −(yh − cy)(yv − cy).
    Renvoie la focale en px et en mm pour un capteur de 36 mm sur la HAUTEUR de l'image, le champ vertical et l'inclinaison.
    Non calculable quand la caméra est à l'horizontale (verticales parallèles) : seule la convergence est rendue."""
    pv = fuite(*verticales)
    ang = [math.degrees(math.atan2(q[0] - p[0], q[1] - p[1])) for p, q in verticales]
    out = dict(angle_verticales_deg=[round(a, 2) for a in ang], convergence_deg=round(abs(ang[0] - ang[1]), 2),
               horizon_pct_de_la_hauteur=round(100 * horizon_y / h, 1))
    if pv is None:
        return out
    cy = h / 2
    prod = -(horizon_y - cy) * (pv[1] - cy)
    out["point_de_fuite_vertical"] = [round(pv[0]), round(pv[1])]
    if prod > 0:
        f = math.sqrt(prod)
        out.update(focale_px=round(f), focale_mm_capteur36_vertical=round(f * 36 / h, 1), champ_vertical_deg=round(2 * math.degrees(math.atan(h / 2 / f)), 1),
                   inclinaison_deg=round(math.degrees(math.atan((horizon_y - cy) / f)), 1))
    return out

# ------------------------------------------------------------------ mesures globales (sans cible)
def _kmeans_palette(px, k, graine=3):
    L = lab(px).astype(np.float32)
    crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 40, 0.5)
    cv2.setRNGSeed(graine)
    k = max(1, min(k, len(px)))
    _, etiq, _ = cv2.kmeans(L, k, None, crit, 4, cv2.KMEANS_PP_CENTERS)
    etiq = etiq.ravel()
    out = [dict(couleur=hexa(np.median(px[etiq == i], axis=0)), part_pct=round(100 * float((etiq == i).mean()), 1)) for i in range(k) if (etiq == i).any()]
    out.sort(key=lambda d: -d["part_pct"])
    return out

def palette(img, k=10, graine=3, bande=None):
    """Couleurs dominantes (k-moyennes en Lab), part de l'image, saturation et luminance moyennes, contraste, dominante chaude."""
    h, w = img.shape[:2]
    m = masque_global(h, w, bande)
    px = img[m][::7]
    hsv = cv2.cvtColor(np.clip(img, 0, 255).astype(np.uint8), cv2.COLOR_RGB2HSV)
    Lm = luma(img)[m]
    r, g, b = (img[..., i][m].mean() for i in range(3))
    return dict(dominantes=_kmeans_palette(px, k, graine), saturation_moyenne=round(float(hsv[..., 1][m].mean() / 255), 3),
                luminance_moyenne=round(float(Lm.mean()), 1), contraste=round(float(Lm.std()), 1),
                dominante_chaude=round(float(r - b), 1), moyenne=hexa((r, g, b)))

def palette_commune(images, k=10, graine=3, bande=None, pas=23):
    """Palette d'une AMBIANCE : k-moyennes sur les pixels de plusieurs images réunies (chaque image compte à égalité de pixels)."""
    px = np.concatenate([im[masque_global(im.shape[0], im.shape[1], bande)][::pas] for im in images])
    return _kmeans_palette(px, k, graine)

def regions(img, graines, tol=11.0):
    """Part de l'image par famille (ciel, sol, murs…) : croissance de région depuis des graines, sur l'image lissée
    (écart Lab à la graine inférieur à `tol` ; plusieurs graines par famille pour suivre les dégradés). Approché à ± 5 points."""
    h, w = img.shape[:2]
    e = 4
    petit = cv2.resize(cv2.GaussianBlur(img, (0, 0), 3), (w // e, h // e), interpolation=cv2.INTER_AREA)
    L = lab(petit).astype(np.float32)
    pris = np.zeros((h // e, w // e), np.uint8)
    out, cartes = {}, {}
    for nom, pts in graines.items():
        tot = np.zeros_like(pris)
        for (x, y) in pts:
            if not (0 <= x < w and 0 <= y < h):
                raise ValueError(f"graine {[x, y]} de « {nom} » hors de l'image ({w} × {h})")
            masque = np.zeros((h // e + 2, w // e + 2), np.uint8)
            cv2.floodFill(L.copy(), masque, (min(w // e - 1, int(x / e)), min(h // e - 1, int(y / e))), 0, (tol,) * 3, (tol,) * 3,
                          4 | cv2.FLOODFILL_MASK_ONLY | cv2.FLOODFILL_FIXED_RANGE | (255 << 8))
            tot |= (masque[1:-1, 1:-1] > 0).astype(np.uint8)
        tot &= (1 - pris)
        pris |= tot
        out[nom] = round(100 * float(tot.mean()), 1)
        cartes[nom] = cv2.resize(tot, (w, h), interpolation=cv2.INTER_NEAREST).astype(bool)
    out["reste"] = round(100 - sum(out.values()), 1)
    return out, cartes

def degrade(img, masque, axe="y"):
    """Dégradé d'une famille (ciel, sol) : couleur médiane de cinq tranches le long de l'axe (de haut en bas pour "y")."""
    idx = np.where(masque.any(axis=1 if axe == "y" else 0))[0]
    if len(idx) < 10:
        return None
    a, b = idx[0], idx[-1]
    tr = []
    for i in range(5):
        u0, u1 = int(a + (b - a) * i / 5), int(a + (b - a) * (i + 1) / 5) + 1
        sl = (slice(u0, u1), slice(None)) if axe == "y" else (slice(None), slice(u0, u1))
        px = img[sl][masque[sl]]
        if len(px):
            tr.append(hexa(np.median(px, axis=0)))
    return dict(de=int(a), a=int(b), tranches=tr, mediane=hexa(np.median(img[masque], axis=0)))

def densite(img, k=12, bande=None):
    """Indicateurs de densité, identiques des deux côtés d'une comparaison :
    - segments : zones connexes de couleur homogène (image lissée, quantifiée en k couleurs) de plus de 0,02 % de l'image ;
    - petits segments : entre 0,005 % et 0,02 % ;
    - bords nets : part des pixels dont le gradient de luminance dépasse 25 niveaux (traits, joints) ; bords doux : entre 6 et 25
      (texture, dégradés).
    Ce sont des comptes de ZONES de couleur, pas d'objets : un fil du bois très marqué fait monter le nombre de segments."""
    h, w = img.shape[:2]
    u8 = np.clip(img, 0, 255).astype(np.uint8)
    lis = cv2.bilateralFilter(u8, 9, 30, 7)
    L = lab(lis[::2, ::2].astype(np.float32)).astype(np.float32)
    crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.5)
    cv2.setRNGSeed(5)
    ech = L.reshape(-1, 3)[::5].copy()
    _, etiq, cent = cv2.kmeans(ech, k, None, crit, 3, cv2.KMEANS_PP_CENTERS)
    dist = ((L[:, :, None, :] - cent[None, None]) ** 2).sum(-1)
    lab_ = dist.argmin(-1).astype(np.int32)
    if bande:
        lab_[max(0, int(bande[0])) // 2:max(0, int(bande[1])) // 2] = -1
    gros = petits = 0
    tot = lab_.size
    for i in range(k):
        m = (lab_ == i).astype(np.uint8)
        n, _, st, _ = cv2.connectedComponentsWithStats(m, connectivity=4)
        a = st[1:, cv2.CC_STAT_AREA] / tot
        gros += int((a >= 0.0002).sum()); petits += int(((a >= 0.00005) & (a < 0.0002)).sum())
    Lm = luma(img)
    gx, gy = cv2.Sobel(Lm, cv2.CV_32F, 1, 0, ksize=3) / 4, cv2.Sobel(Lm, cv2.CV_32F, 0, 1, ksize=3) / 4
    g = np.hypot(gx, gy)
    mg = masque_global(h, w, bande)
    return dict(segments=gros, petits_segments=petits, part_bords_pct=round(100 * float((g[mg] > 25).mean()), 2),
                part_bords_doux_pct=round(100 * float(((g[mg] > 6) & (g[mg] <= 25)).mean()), 2), gradient_moyen=round(float(g[mg].mean()), 2))

def grain(img, bande=None):
    """Grain : écart type du résidu haute fréquence dans les 15 % de blocs 32 × 32 les plus plats. Sous 1 : aucun grain ajouté."""
    L = luma(img)
    r = L - cv2.GaussianBlur(L, (0, 0), 1.5)
    h, w = L.shape
    v = []
    for y in range(0, h - 32, 32):
        if bande and bande[0] - 32 < y < bande[1]:
            continue
        for x in range(0, w - 32, 32):
            b = L[y:y + 32, x:x + 32]
            v.append((float(np.abs(np.gradient(cv2.GaussianBlur(b, (0, 0), 2))[0]).mean() + b.std() * 0.2), float(r[y:y + 32, x:x + 32].std())))
    if not v:
        return None
    v.sort()
    return round(float(np.median([b for _, b in v[:max(4, len(v) * 15 // 100)]])), 2)

def vignettage(img, masque):
    """Luminance de la famille `masque` selon la distance au centre (en fraction de la demi-diagonale) : assombrissement des bords."""
    h, w = img.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.hypot(xx - w / 2, yy - h / 2) / math.hypot(w / 2, h / 2)
    L = luma(img)
    out = []
    for a in (0.0, 0.25, 0.5, 0.7, 0.85):
        s = masque & (r >= a) & (r < a + (0.25 if a < 0.5 else 0.15))
        out.append(round(float(L[s].mean()), 1) if s.sum() > 500 else None)
    return dict(rayons=[0.12, 0.37, 0.6, 0.77, 0.92], luminance=out)

def nettete_carte(img, pas=48):
    """Carte de netteté : largeur des transitions (px) estimée par bloc de `pas` px = amplitude locale / gradient maximal.
    Petit = net (≈ 2 px pour un dessin net) ; NaN = bloc sans contraste, où la netteté ne se lit pas."""
    L = cv2.GaussianBlur(luma(img), (0, 0), 0.7)
    gx, gy = cv2.Sobel(L, cv2.CV_32F, 1, 0, ksize=3) / 8, cv2.Sobel(L, cv2.CV_32F, 0, 1, ksize=3) / 8
    g = np.hypot(gx, gy)
    h, w = L.shape
    carte = np.full((h // pas, w // pas), np.nan, np.float32)
    for j in range(h // pas):
        for i in range(w // pas):
            b = L[j * pas:(j + 1) * pas, i * pas:(i + 1) * pas]; gb = g[j * pas:(j + 1) * pas, i * pas:(i + 1) * pas]
            amp = float(np.percentile(b, 98) - np.percentile(b, 2))
            if amp > 18:
                carte[j, i] = amp / max(float(np.percentile(gb, 99.5)), 1e-3)
    return carte

def _nan(f, a, *args):
    a = np.asarray(a, dtype=np.float32)
    return None if a.size == 0 or np.isnan(a).all() else round(float(f(a, *args)), 2)

def nettete_resume(carte, bandes=8):
    """Résumé de la carte : médiane, 10e et 90e centiles, médiane par tiers de la hauteur, et pour chacune des `bandes`
    bandes horizontales égales (de haut en bas) la largeur des transitions les PLUS NETTES de la bande (10e centile)."""
    n = carte.shape[0]
    return dict(mediane_px=_nan(np.nanmedian, carte), p10_px=_nan(np.nanpercentile, carte, 10), p90_px=_nan(np.nanpercentile, carte, 90),
                par_tiers_vertical=[_nan(np.nanmedian, carte[i * n // 3:(i + 1) * n // 3]) for i in range(3)],
                net_par_bande=[_nan(np.nanpercentile, carte[i * n // bandes:(i + 1) * n // bandes], 10) for i in range(bandes)])

def nettete_boite(carte, boite, pas=48):
    """Netteté d'une zone (le sol sous le sujet, le fond) : 10e centile et médiane de la carte dans la boîte [x0, y0, x1, y1]."""
    x0, y0, x1, y1 = boite
    sub = carte[max(0, int(y0) // pas):max(1, int(math.ceil(y1 / pas))), max(0, int(x0) // pas):max(1, int(math.ceil(x1 / pas)))]
    if sub.size == 0 or np.isnan(sub).all():
        return dict(erreur="aucun bloc contrasté dans cette boîte : la netteté ne s'y lit pas (poser la boîte sur une zone texturée)")
    return dict(transitions_les_plus_nettes_px=_nan(np.nanpercentile, sub, 10), transition_mediane_px=_nan(np.nanmedian, sub),
                blocs_lus=int((~np.isnan(sub)).sum()), blocs=int(sub.size))

def ecart_palettes(ref, nous):
    """Pour chaque dominante de la référence : la couleur la plus proche chez nous (ΔE2000) et la part de nos couleurs qui
    lui reviennent (chaque couleur de chez nous va à la dominante de référence la plus proche)."""
    cr = [de_hexa(d["couleur"]) for d in ref]; cn = [de_hexa(d["couleur"]) for d in nous]
    part_n = [0.0] * len(ref)
    for d, c in zip(nous, cn):
        part_n[int(np.argmin([de2000(c, x) for x in cr]))] += d["part_pct"]
    out = []
    for i, (d, c) in enumerate(zip(ref, cr)):
        des = [de2000(c, x) for x in cn]
        j = int(np.argmin(des))
        out.append(dict(ref=d["couleur"], part_ref=d["part_pct"], nous=nous[j]["couleur"], part_nous_proches=round(part_n[i], 1),
                        delta_e=round(des[j], 1), ecart_part=round(part_n[i] - d["part_pct"], 1)))
    return out
