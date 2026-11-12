"""Mesures hors contour de forme : coupes en travers d'un trait, traits d'épaisseur constante (membres, tiges, lignes), bouts de trait, zones de couleur, ombre au sol.

Une « coupe » est un segment [a, b] tracé en travers d'un trait (ou d'une bande claire), dont les deux bouts sont posés
sur des aplats. La couleur est lue tous les 0,25 px, moyennée sur 3 px de large. La bande est l'endroit où la couleur
s'écarte le plus des deux aplats ; ses bords sont placés à mi-niveau (distance de couleur à la bande = moitié de celle
de l'aplat voisin). Même méthode que pour le contour d'une forme (mp_forme.py), donc les chiffres sont comparables.
"""
import sys
sys.dont_write_bytecode = True
import math
import numpy as np
import cv2
import mp_base as B

PAS = 0.25

def profil(rgb, a, b, large=3):
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    lg = float(np.hypot(*(b - a)))
    pos = np.arange(0, lg, PAS)
    u = (b - a) / lg; nrm = np.array([-u[1], u[0]])
    acc = 0
    offs = np.arange(large) - (large - 1) / 2
    for o in offs:
        x = a[0] + pos * u[0] + o * nrm[0]; y = a[1] + pos * u[1] + o * nrm[1]
        acc = acc + np.stack([B.echantillons(np.ascontiguousarray(rgb[..., k]), x[None], y[None])[0] for k in range(3)], -1)
    return pos, acc / len(offs)

def _r(v, n=1):
    v = float(v)
    return None if not np.isfinite(v) else round(v, n)

def bande(rgb, a, b, large=3):
    """Mesure la bande (trait sombre ou filet clair) traversée par le segment a→b."""
    pos, c = profil(rgb, a, b, large)
    n = len(pos)
    if n < 24:
        return dict(erreur="coupe trop courte")
    k = max(3, n // 6)
    cg, cd = np.median(c[:k], 0), np.median(c[-k:], 0)
    d = np.minimum(np.linalg.norm(c - cg, axis=1), np.linalg.norm(c - cd, axis=1))
    ds = np.convolve(d, np.ones(5) / 5, mode="same")
    im = int(np.argmax(ds[k:-k])) + k
    if ds[im] < 25:
        return dict(erreur="pas de bande nette", ecart_max=_r(ds[im]))
    coeur = d > 0.7 * d.max()
    # ne garder que le morceau du cœur qui contient le maximum
    i0 = im
    while i0 > 0 and coeur[i0 - 1]:
        i0 -= 1
    i1 = im
    while i1 < n - 1 and coeur[i1 + 1]:
        i1 += 1
    cb = np.median(c[i0:i1 + 1], 0)
    e = np.linalg.norm(c - cb, axis=1)
    eg, ed = float(np.median(e[:k])), float(np.median(e[-k:]))
    xg = B.croisement(pos, e, 0.5 * eg, 0, +1) if eg > 20 else None
    xd = B.croisement(pos, e, 0.5 * ed, n - 1, -1) if ed > 20 else None
    res = dict(couleur=B.hexa(cb), luminance=_r(B.luma(cb)), cote_a=B.hexa(cg), cote_b=B.hexa(cd), contraste_a=_r(eg), contraste_b=_r(ed))
    if xg is None or xd is None or xd <= xg:
        res["erreur"] = "un des deux côtés est aussi sombre que la bande"
        return res
    res["largeur_px"] = _r(xd - xg, 2)
    g90 = B.croisement(pos, e, 0.9 * eg, int(xg / PAS), -1); d90 = B.croisement(pos, e, 0.9 * ed, int(xd / PAS), +1)
    res["transition_a_px"] = _r(2 * (xg - g90), 2) if g90 is not None else None
    res["transition_b_px"] = _r(2 * (d90 - xd), 2) if d90 is not None else None
    res["bords"] = [_r(xg, 2), _r(xd, 2)]
    return res

def sequence(rgb, a, b, large=3):
    """Tout ce que traverse le segment a→b : suite d'aplats (couleur, largeur). Un aplat = au moins 1,25 px où la couleur
    ne bouge pas ; deux aplats voisins de même couleur (écart < 28) sont fusionnés ; la limite entre deux aplats est
    placée là où la couleur est à égale distance des deux."""
    pos, c = profil(rgb, a, b, large)
    n = len(pos)
    g = np.zeros(n)
    g[2:-2] = np.linalg.norm(c[4:] - c[:-4], axis=1)
    plat = g < 14
    runs = []
    i = 0
    while i < n:
        if plat[i]:
            j = i
            while j + 1 < n and plat[j + 1]:
                j += 1
            if j - i + 1 >= 5:
                runs.append([i, j, np.median(c[i:j + 1], 0)])
            i = j + 1
        else:
            i += 1
    fus = []
    for r in runs:
        if fus and np.linalg.norm(fus[-1][2] - r[2]) < 28:
            fus[-1][1] = r[1]; fus[-1][2] = np.median(c[fus[-1][0]:r[1] + 1], 0)
        else:
            fus.append(r)
    lim = []
    for r1, r2 in zip(fus, fus[1:]):
        d = np.linalg.norm(c - r1[2], axis=1) - np.linalg.norm(c - r2[2], axis=1)
        x = B.croisement(pos, d, 0.0, r1[1], +1)
        lim.append(x if x is not None else (pos[r1[1]] + pos[r2[0]]) / 2)
    out = []
    for k, r in enumerate(fus):
        w = lim[k] - lim[k - 1] if 0 < k < len(fus) - 1 else None
        out.append(dict(couleur=B.hexa(r[2]), luminance=_r(B.luma(r[2])), largeur_px=_r(w, 2) if w is not None else None))
    return out

def membre(rgb, a, b, n=9, demi=None):
    """n coupes perpendiculaires réparties le long du segment a→b posé sur l'axe d'un membre."""
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    lg = float(np.hypot(*(b - a))); u = (b - a) / lg; nrm = np.array([-u[1], u[0]])
    demi = demi or 28
    out = []
    for t in np.linspace(0.06, 0.94, n):
        p = a + u * lg * t
        r = bande(rgb, p - nrm * demi, p + nrm * demi, large=5)
        out.append((float(t), r.get("largeur_px"), r.get("couleur"), r.get("transition_a_px")))
    w = np.array([np.nan if o[1] is None else o[1] for o in out])
    ok = np.isfinite(w)
    res = dict(longueur_px=_r(lg), coupes=[dict(position=_r(o[0], 2), largeur_px=o[1], couleur=o[2]) for o in out])
    if ok.sum() >= 3:
        med = float(np.median(w[ok]))
        bon = ok & (np.abs(w - med) < 0.35 * med)          # écarte les coupes qui croisent autre chose
        pente = np.polyfit(np.array([o[0] for o in out])[bon], w[bon], 1)[0] if bon.sum() >= 3 else float("nan")
        cs = [B.de_hexa(o[2]) for o, k in zip(out, bon) if k and o[2]]
        res.update(largeur_mediane_px=_r(med, 2), largeur_min_px=_r(w[bon].min(), 2), largeur_max_px=_r(w[bon].max(), 2),
                   ecart_type_px=_r(w[bon].std(), 2), effilement_px_du_debut_a_la_fin=_r(pente, 2), coupes_valides=int(bon.sum()),
                   couleur=B.hexa(np.median(np.array(cs), 0)) if cs else None,
                   transition_px=_r(np.nanmedian([np.nan if o[3] is None else o[3] for o in out]), 2))
    return res

def bout(rgb, a, b, largeur, demi=None):
    """Forme de l'extrémité d'un trait : a est dans le trait, b au-delà du bout. Mesure la largeur du trait tous les 0,5 px en
    approchant du bout. Bout rond = la largeur tombe de 90 % à 10 % sur environ 0,3 à 0,5 largeur ; bout carré = sur < 0,15."""
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    lg = float(np.hypot(*(b - a))); u = (b - a) / lg; nrm = np.array([-u[1], u[0]])
    demi = demi or max(12, largeur * 1.6)
    xs, ws = [], []
    for s in np.arange(0, lg, 0.5):
        p = a + u * s
        r = bande(rgb, p - nrm * demi, p + nrm * demi, large=1)
        xs.append(s); ws.append(r.get("largeur_px") or 0.0)
    ws = np.array(ws); xs = np.array(xs)
    x90 = next((x for x, w in zip(xs, ws) if w < 0.9 * largeur), None)
    x10 = next((x for x, w in zip(xs, ws) if w < 0.1 * largeur), None)
    res = dict(largeur_ref_px=_r(largeur, 2))
    if x90 is not None and x10 is not None:
        res.update(longueur_arrondi_px=_r(x10 - x90, 1), longueur_arrondi_en_largeur=_r((x10 - x90) / largeur, 2),
                   forme="rond" if (x10 - x90) / largeur > 0.25 else "carré ou tronqué")
    return res

def zone(rgb, poly, encre_rgb, k=3):
    """Couleurs d'une zone (polygone) hors trait : k-moyennes en Lab, parts, écarts TSL à la couleur dominante, dégradé."""
    H, W = rgb.shape[:2]
    m = np.zeros((H, W), np.uint8)
    cv2.fillPoly(m, [np.array(poly, dtype=np.int32)], 1)
    L = B.luma(rgb)
    e = np.linalg.norm(rgb - np.asarray(encre_rgb, dtype=np.float32), axis=-1)
    trait = cv2.dilate((e < 70).astype(np.uint8), np.ones((3, 3), np.uint8))
    ok = (m > 0) & (trait == 0)
    ys, xs = np.where(ok)
    if len(xs) < 60:
        return dict(erreur="zone trop petite")
    col = rgb[ys, xs]
    labs = B.lab(col).astype(np.float32)
    k = max(1, min(int(k), len(labs)))
    cv2.setRNGSeed(7)
    _, et, _ = cv2.kmeans(labs, k, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 40, 0.1), 4, cv2.KMEANS_PP_CENTERS)
    et = et.ravel()
    ordre = sorted(range(k), key=lambda i: -(et == i).sum())
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    base = np.median(col[et == ordre[0]], 0)
    cl = []
    for i in ordre:
        z = et == i
        if z.sum() < 10:
            continue
        cm = np.median(col[z], 0)
        cl.append(dict(hex=B.hexa(cm), part=_r(z.mean(), 3), luminance=_r(B.luma(cm)),
                       centre_dans_la_zone=[_r((xs[z].mean() - x0) / max(1, x1 - x0), 2), _r((ys[z].mean() - y0) / max(1, y1 - y0), 2)],
                       ecart_tsl_a_la_dominante=B.ecart_tsl(base, cm), delta_e_a_la_dominante=_r(B.de2000(base, cm), 1)))
    z = et == ordre[0]
    u, v = (xs[z] - x0) / max(1, x1 - x0), (ys[z] - y0) / max(1, y1 - y0)
    A = np.c_[np.ones(z.sum()), u, v]
    lum = L[ys[z], xs[z]]
    co, *_ = np.linalg.lstsq(A, lum, rcond=None)
    r2 = 1 - ((lum - A @ co) ** 2).sum() / max(((lum - lum.mean()) ** 2).sum(), 1e-6)
    hp = L - cv2.GaussianBlur(L, (0, 0), 2.5)
    er = cv2.erode(ok.astype(np.uint8), np.ones((7, 7), np.uint8)).astype(bool)
    return dict(pixels=int(len(xs)), mediane=B.hexa(np.median(col, 0)), couleurs=cl,
                dominante=dict(ecart_type_luminance=_r(lum.std(), 2), degrade_gauche_droite=_r(co[1]), degrade_haut_bas=_r(co[2]), r2=_r(r2, 3)),
                grain_ecart_type=_r(hp[er].std(), 2) if er.sum() > 40 else None)

def ombre_sol(rgb, a, b, large=9):
    """Coupe du sol éclairé (a) vers l'ombre (b) : couleurs, facteur par canal, largeur du flou du bord."""
    pos, c = profil(rgb, a, b, large)
    n = len(pos); k = max(4, n // 5)
    cl, co = np.median(c[:k], 0), np.median(c[-k:], 0)
    axe = co - cl
    nn = float(np.linalg.norm(axe))
    if nn < 12:
        return dict(erreur="pas d'ombre nette sur cette coupe", sol=B.hexa(cl), autre=B.hexa(co))
    t = (c - cl) @ axe / (nn * nn)
    t = np.convolve(np.pad(t, 4, mode="edge"), np.ones(9) / 9, mode="valid")
    p10 = B.croisement(pos, t, 0.1, 0, +1); p90 = B.croisement(pos, t, 0.9, n - 1, -1); p50 = B.croisement(pos, t, 0.5, 0, +1)
    f = co / np.maximum(cl, 1)
    return dict(sol_eclaire=B.hexa(cl), sol_a_l_ombre=B.hexa(co), facteur_rvb=[_r(v, 3) for v in f],
                ecart_luminance=_r(B.luma(co) - B.luma(cl)), delta_e=_r(B.de2000(cl, co), 1), ecart_tsl=B.ecart_tsl(cl, co),
                flou_du_bord_10_90_px=_r(abs(p90 - p10), 1) if p10 is not None and p90 is not None else None,
                position_du_bord_px=_r(p50, 1) if p50 is not None else None, longueur_coupe_px=_r(pos[-1]))
