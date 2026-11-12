#!/usr/bin/env python3
"""Contrôle chiffré : tableau « référence / nous / écart » à partir de deux fichiers de mesure écrits par mesurer.py.

  python comparer.py <reference.json> <nous.json> <dossier de sortie> [--paires paires.json] [--nom controle] [--tour N]

Les deux images doivent avoir été mesurées par les MÊMES scripts, l'élément comparé étant rendu à la même taille que dans
la référence (même diamètre de tête, même hauteur de titre). Si les grandeurs de référence diffèrent, nos longueurs sont
remises à l'échelle et le script le dit.

Sans --paires, on compare ce qui porte le même nom des deux côtés (formes, coupes, traits, zones, ombres).
Avec --paires (voir references/controle-chiffre.md) :
  { "formes":  [{"ref": "tete-a", "nous": "tete", "exclure_angles": [[255, 290]]}],
    "coupes":  [{"ref": "torse, côté ombre", "nous": "torse ombre", "bande": "sombre"}],     bande : "sombre" (trait) ou "claire" (filet)
    "membres": [{"ref": "jambe gauche", "nous": "jambe"}],
    "zones":   [{"ref": "torse", "nous": "torse"}],
    "ombres":  [{"ref": "ombre au sol", "nous": "ombre", "melange": {"teinte": "#202d6c", "force": 0.87}}],
    "tolerances": {"epaisseur_px": 1, "delta_e": 6, "luminance": 8} }

Tolérances par défaut : épaisseurs ±1 px, couleurs ΔE2000 < 6, luminance ±8 niveaux (les autres sont dans TOLERANCES).
Sorties : <nom>_ecarts.md et .json, <nom>_courbes.png, <nom>_profils.png ; avec --tour N, une copie dans tours/tourN_ecarts.md
et le suivi tours/suivi.json (quatre tours de correction au plus).
Dépendances : Python 3.9+, numpy, Pillow, opencv-python. Écrit par Flot Web.
"""
import sys
sys.dont_write_bytecode = True
import argparse, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np
import mp_base as B, mp_forme as T

TOLERANCES = dict(epaisseur_px=1.0, delta_e=6.0, luminance=8.0, angle_deg=10.0, bord_px=0.5, part_pct=6.0, frontiere_R=0.1,
                  direction_frontiere_deg=15.0, bord_doux=0.04, flou_ombre_px=8.0)
TOURS_MAX = 4

def _arr(v):
    return np.array([np.nan if x is None else x for x in v], dtype=float)

def _ecart_angle(a, b):
    return ((b - a + 180) % 360) - 180

class Tableau:
    def __init__(self, tol):
        self.lignes, self.tol = [], tol
    def ligne(self, grandeur, r, n, tol=None, unite="", ecart=None, angle=False):
        if r is None or n is None:
            if not (r is None and n is None):
                self.lignes.append(dict(grandeur=grandeur, reference=r, nous=n, ecart=None, tolerance=tol, unite=unite, ok=None,
                                        note="mesurée d'un seul côté"))
            return
        if ecart is None:
            ecart = _ecart_angle(r, n) if angle else n - r
        ok = None if tol is None else bool(abs(ecart) <= tol)
        self.lignes.append(dict(grandeur=grandeur, reference=r, nous=n, ecart=round(float(ecart), 2), tolerance=tol, unite=unite, ok=ok))
    def couleur(self, grandeur, hr, hn):
        if not hr or not hn:
            return
        d = B.de2000(B.de_hexa(hr), B.de_hexa(hn))
        self.lignes.append(dict(grandeur=grandeur, reference=hr, nous=hn, ecart=round(d, 1), tolerance=self.tol["delta_e"], unite="ΔE2000", ok=bool(d < self.tol["delta_e"])))

def _plateau(seq, sorte):
    """Dans la séquence d'une coupe : le plateau le plus sombre (le trait) ou le plus clair et fin (un filet)."""
    c = [e for e in seq if e.get("largeur_px")]
    if not c:
        return None
    if sorte == "claire":
        fins = [e for e in c if e["largeur_px"] < 20]
        return max(fins or c, key=lambda e: e["luminance"])
    return min(c, key=lambda e: e["luminance"])

def comparer_forme(tab, nom, fr, fn, k, tol, excl=None):
    cr, cn = fr.get("contour"), fn.get("contour")
    if not cr or not cn:
        tab.lignes.append(dict(grandeur=f"{nom} : forme non mesurée d'un côté", reference=fr.get("erreur"), nous=fn.get("erreur"), ecart=None, tolerance=None, unite="", ok=None))
        return None
    P = f"{nom} · "
    ang = np.arange(0, 360, 5)
    er, en = _arr(cr["courbe_5deg"]), _arr(cn["courbe_5deg"]) * k
    figs = None
    if cr.get("D_px") and cn.get("D_px"):
        tab.ligne(P + "taille (D)", cr["D_px"], cn["D_px"], None, "px")
    com = np.isfinite(er) & np.isfinite(en)
    if com.sum() >= 6:
        d = np.abs(en[com] - er[com])
        tab.ligne(P + f"courbe du contour contre la courbe brute de la référence : écart moyen ({int(com.sum())} orientations communes)", 0.0, round(float(d.mean()), 2), tol["epaisseur_px"], "px", float(d.mean()))
        tab.ligne(P + "courbe du contour contre la courbe brute : 90e centile", 0.0, round(float(np.percentile(d, 90)), 2), tol["epaisseur_px"], "px", float(np.percentile(d, 90)))
        tab.ligne(P + f"courbe du contour contre la courbe brute : écart maximal (à {int(ang[com][np.argmax(d)])}°)", 0.0, round(float(d.max()), 2), tol["epaisseur_px"], "px", float(d.max()))
    _, f1, _ = T.harmoniques(ang, er, 1)                    # la LOI de la référence : terme constant + 1 harmonique (plein / délié)
    loi1 = None
    if f1 is not None and np.isfinite(en).sum() >= 6:
        loi1 = f1(ang)
        okn = np.isfinite(en)
        for a0, a1 in excl or []:
            okn &= ~(((ang >= a0) & (ang <= a1)) if a0 <= a1 else ((ang >= a0) | (ang <= a1)))
        d1 = np.abs(en[okn] - loi1[okn])
        suf = f" (hors {excl})" if excl else ""
        tab.ligne(P + f"courbe du contour contre la LOI de la référence (1 harmonique){suf} : écart moyen", 0.0, round(float(d1.mean()), 2), tol["epaisseur_px"], "px", float(d1.mean()))
        tab.ligne(P + f"courbe du contour contre la LOI de la référence{suf} : écart maximal", 0.0, round(float(d1.max()), 2), tol["epaisseur_px"], "px", float(d1.max()))
    s = lambda v: None if v is None else round(v * k, 2)
    tab.ligne(P + "épaisseur moyenne du contour", cr.get("epaisseur_moy_px"), s(cn.get("epaisseur_moy_px")), tol["epaisseur_px"], "px")
    tab.ligne(P + "épaisseur minimale brute", cr.get("epaisseur_min_px"), s(cn.get("epaisseur_min_px")), tol["epaisseur_px"], "px")
    tab.ligne(P + "épaisseur maximale brute (souvent gonflée par un trait voisin)", cr.get("epaisseur_max_px"), s(cn.get("epaisseur_max_px")), None, "px")
    def loi_simple(c):                                      # « loi_simple » ; pour un ancien fichier, les mêmes grandeurs sous leur ancien nom
        l = c.get("loi_simple")
        if l:
            return l
        l = c.get("loi") or {}
        return dict(a0_px=l.get("a0_px"), h1_px=l.get("h1_amplitude_px"), plein_vers_deg=l.get("h1_plein_vers_deg"))
    lr, ln = loi_simple(cr), loi_simple(cn)
    tab.ligne(P + "loi : terme constant (a0)", lr.get("a0_px"), s(ln.get("a0_px")), tol["epaisseur_px"], "px")
    tab.ligne(P + "loi : amplitude plein / délié (h1)", lr.get("h1_px"), s(ln.get("h1_px")), tol["epaisseur_px"], "px")
    tab.ligne(P + "loi : délié (a0 − h1)", lr.get("delie_px"), s(ln.get("delie_px")), tol["epaisseur_px"], "px")
    tab.ligne(P + "loi : plein (a0 + h1)", lr.get("plein_px"), s(ln.get("plein_px")), tol["epaisseur_px"], "px")
    tab.ligne(P + "loi : direction du plein", lr.get("plein_vers_deg"), ln.get("plein_vers_deg"), tol["angle_deg"], "°", angle=True)
    for sec in cr.get("secteurs", {}):
        tab.ligne(P + f"épaisseur, secteur {sec}", cr["secteurs"][sec]["moyenne_px"], s(cn.get("secteurs", {}).get(sec, {}).get("moyenne_px")), tol["epaisseur_px"], "px")
    tab.ligne(P + "irrégularité du trait (σ autour de la loi)", cr.get("tremble_px"), s(cn.get("tremble_px")), None, "px")
    tab.couleur(P + "couleur du trait", (cr.get("trait") or {}).get("hex"), (cn.get("trait") or {}).get("hex"))
    tab.ligne(P + "bord intérieur du trait : largeur de transition", cr["bord"].get("transition_int_px"), cn["bord"].get("transition_int_px"), tol["bord_px"], "px")
    tab.ligne(P + "bord extérieur du trait : largeur de transition", cr["bord"].get("transition_ext_px"), cn["bord"].get("transition_ext_px"), None, "px")
    ar, an = cr["accentuation"], cn["accentuation"]
    tab.ligne(P + "accentuation : sur-brillance côté remplissage", ar.get("sur_brillance_cote_remplissage"), an.get("sur_brillance_cote_remplissage"), tol["luminance"], "niveaux")
    tab.ligne(P + "accentuation : creux dans le trait", ar.get("creux_dans_le_trait"), an.get("creux_dans_le_trait"), tol["luminance"], "niveaux")
    tab.ligne(P + "halo autour de la forme", cr["halo_luminance"].get("median"), cn["halo_luminance"].get("median"), tol["luminance"], "niveaux")
    orr, on = fr.get("ombrage") or {}, fn.get("ombrage") or {}
    profs = None
    zr, zn = orr.get("deux_zones") or {}, on.get("deux_zones") or {}
    if "claire" in zr and "claire" in zn:
        tab.couleur(P + "remplissage, zone claire", zr["claire"]["hex"], zn["claire"]["hex"])
        tab.couleur(P + "remplissage, zone sombre", zr["sombre"]["hex"], zn["sombre"]["hex"])
        tab.ligne(P + "part de la zone sombre", round(100 * zr["sombre"]["part"], 1), round(100 * zn["sombre"]["part"], 1), tol["part_pct"], "%")
        qr, qn = orr.get("frontiere") or {}, on.get("frontiere") or {}
        tab.ligne(P + "frontière d'ombre : distance au centre", qr.get("position_au_centre_R"), qn.get("position_au_centre_R"), tol["frontiere_R"], "R")
        tab.ligne(P + "frontière d'ombre : direction du clair", qr.get("axe_vers_le_clair_deg"), qn.get("axe_vers_le_clair_deg"), tol["direction_frontiere_deg"], "°", angle=True)
        tab.ligne(P + "frontière d'ombre : saut de luminance", qr.get("saut_luminance"), qn.get("saut_luminance"), tol["luminance"], "niveaux")
        tab.ligne(P + "frontière d'ombre : largeur du bord doux", qr.get("transition_D"), qn.get("transition_D"), tol["bord_doux"], "× 2R")
    elif zr or zn:
        tab.couleur(P + "remplissage (médiane)", (orr.get("remplissage_median") or {}).get("hex"), (on.get("remplissage_median") or {}).get("hex"))
    else:
        tab.couleur(P + "remplissage", cr.get("remplissage_hex"), cn.get("remplissage_hex"))
    tab.ligne(P + "grain du remplissage (σ)", orr.get("grain_ecart_type"), on.get("grain_ecart_type"), None, "niveaux")
    pr, pn = orr.get("profils_diametres"), on.get("profils_diametres")
    if pr and pn:
        profs = []
        for q in [x for x in pr if x != "pos_R"]:
            a, b = _arr(pr[q]), _arr(pn[q])
            c2 = np.isfinite(a) & np.isfinite(b)
            if c2.sum() < 10:
                continue
            d = np.abs(b[c2] - a[c2])
            tab.ligne(P + f"profil de luminance {q} : écart moyen ({int(c2.sum())} points)", 0.0, round(float(d.mean()), 1), tol["luminance"], "niveaux", float(d.mean()))
            tab.ligne(P + f"profil de luminance {q} : 90e centile", 0.0, round(float(np.percentile(d, 90)), 1), tol["luminance"], "niveaux", float(np.percentile(d, 90)))
            tab.ligne(P + f"profil de luminance {q} : écart maximal", 0.0, round(float(d.max()), 1), tol["luminance"], "niveaux", float(d.max()))
            lo = float(np.nanmin(np.r_[a, b])) - 6; hi = float(np.nanmax(np.r_[a, b])) + 6
            profs.append(B.courbe([("référence", pr["pos_R"], a, (214, 39, 40)), ("nous", pn["pos_R"], b, (31, 119, 180))],
                                  f"{nom} · luminance, {q}", "position (−1 à +1)", "lum.", taille=(650, 330), xlim=(-1, 1), ylim=(lo, hi)))
    series = [(f"{nom} · référence", ang, er, (214, 39, 40)), (f"{nom} · nous", ang, en, (31, 119, 180))]
    if loi1 is not None:
        series.append(("loi de la référence (1 harmonique)", ang, loi1, (130, 130, 130), "tirets"))
    tout = np.concatenate([np.asarray(x[2], dtype=float) for x in series])
    ymax = max(4.0, float(np.nanmax(tout)) * 1.25) if np.isfinite(tout).any() else 4.0
    fig = B.courbe(series, "épaisseur du contour = f(orientation du bord)", "orientation (°) : 0 = droite, 90 = haut, 180 = gauche, 270 = bas", "px",
                   taille=(1300, 460), xlim=(0, 360), ylim=(0, ymax), xticks=list(range(0, 361, 45)))
    return fig, profs

def _paires_auto(ref, nous, cle):
    return [dict(ref=n, nous=n) for n in ref.get(cle, {}) if n in nous.get(cle, {})]

def comparer(ref_path, nous_path, sortie, paires=None, nom="controle", tour=None):
    sortie = pathlib.Path(sortie); sortie.mkdir(parents=True, exist_ok=True)
    ref = json.loads(pathlib.Path(ref_path).read_text(encoding="utf-8-sig")); nous = json.loads(pathlib.Path(nous_path).read_text(encoding="utf-8-sig"))
    for d in (ref, nous):                                   # anciens fichiers : "tetes" au lieu de "formes"
        if "formes" not in d and "tetes" in d:
            d["formes"] = d["tetes"]
    paires = dict(paires or {})
    tol = dict(TOLERANCES, **paires.get("tolerances", {}))
    tab = Tableau(tol)
    Dr, Dn = ref.get("D_px"), nous.get("D_px")
    k = 1.0
    if paires.get("echelle") not in (None, "auto"):
        k = float(paires["echelle"])
    elif Dr and Dn:
        k = Dr / Dn
    avert = []
    if Dr and Dn:
        tab.ligne("grandeur de référence (taille de l'élément comparé)", Dr, Dn, None, "px")
        if abs(k - 1) > 0.03:
            avert.append(f"Les deux éléments n'ont pas la même taille ({Dr} px contre {Dn} px) : nos longueurs sont multipliées par {k:.3f}. "
                         "Refaire le rendu de contrôle à la taille de la référence : le lissage du bord et l'accentuation ne se remettent pas à l'échelle.")
    figs, profs = [], []
    for p in paires.get("formes") or _paires_auto(ref, nous, "formes"):
        if p["ref"] not in ref["formes"] or p["nous"] not in nous["formes"]:
            avert.append(f"forme absente : {p}"); continue
        r = comparer_forme(tab, p.get("nom") or p["ref"], ref["formes"][p["ref"]], nous["formes"][p["nous"]], k, tol, p.get("exclure_angles"))
        if r:
            figs.append(r[0]); profs += r[1] or []
    for p in paires.get("coupes") or _paires_auto(ref, nous, "coupes"):
        if p["ref"] not in ref["coupes"] or p["nous"] not in nous["coupes"]:
            avert.append(f"coupe absente : {p}"); continue
        sorte = p.get("bande", "sombre")
        a, b = _plateau(ref["coupes"][p["ref"]]["sequence"], sorte), _plateau(nous["coupes"][p["nous"]]["sequence"], sorte)
        et = p.get("nom") or p["ref"]
        if a and b:
            tab.ligne(f"coupe « {et} », bande {sorte} : largeur", a["largeur_px"], round(b["largeur_px"] * k, 2), tol["epaisseur_px"], "px")
            tab.couleur(f"coupe « {et} », bande {sorte} : couleur", a["couleur"], b["couleur"])
        else:
            avert.append(f"coupe « {et} » : pas de bande mesurable d'un côté")
    for p in paires.get("membres") or _paires_auto(ref, nous, "membres"):
        if p["ref"] not in ref["membres"] or p["nous"] not in nous["membres"]:
            avert.append(f"trait absent : {p}"); continue
        a, b = ref["membres"][p["ref"]], nous["membres"][p["nous"]]
        et = p.get("nom") or p["ref"]
        tab.ligne(f"trait « {et} » : épaisseur", a.get("largeur_mediane_px"), None if b.get("largeur_mediane_px") is None else round(b["largeur_mediane_px"] * k, 2), tol["epaisseur_px"], "px")
        tab.ligne(f"trait « {et} » : irrégularité (σ)", a.get("ecart_type_px"), b.get("ecart_type_px"), None, "px")
        tab.ligne(f"trait « {et} » : effilement du début à la fin", a.get("effilement_px_du_debut_a_la_fin"), b.get("effilement_px_du_debut_a_la_fin"), tol["epaisseur_px"], "px")
        tab.couleur(f"trait « {et} » : couleur", a.get("couleur"), b.get("couleur"))
    for p in paires.get("zones") or _paires_auto(ref, nous, "zones"):
        if p["ref"] not in ref["zones"] or p["nous"] not in nous["zones"]:
            avert.append(f"zone absente : {p}"); continue
        a, b = ref["zones"][p["ref"]], nous["zones"][p["nous"]]
        et = p.get("nom") or p["ref"]
        if a.get("couleurs") and b.get("couleurs"):
            tab.couleur(f"zone « {et} » : couleur dominante", a["couleurs"][0]["hex"], b["couleurs"][0]["hex"])
            tab.ligne(f"zone « {et} » : part de la couleur dominante", round(100 * a["couleurs"][0]["part"], 1), round(100 * b["couleurs"][0]["part"], 1), None, "%")
            tab.ligne(f"zone « {et} » : grain (σ)", a.get("grain_ecart_type"), b.get("grain_ecart_type"), None, "niveaux")
    for p in paires.get("ombres") or _paires_auto(ref, nous, "ombres"):
        if p["ref"] not in ref["ombres"] or p["nous"] not in nous["ombres"]:
            avert.append(f"ombre absente : {p}"); continue
        a, b = ref["ombres"][p["ref"]], nous["ombres"][p["nous"]]
        et = p.get("nom") or p["ref"]
        fb = b.get("flou_du_bord_10_90_px")
        tab.ligne(f"ombre « {et} » : flou du bord (10–90 %)", a.get("flou_du_bord_10_90_px"), None if fb is None else round(fb * k, 1), tol["flou_ombre_px"], "px")
        tab.ligne(f"ombre « {et} » : chute de luminance", a.get("ecart_luminance"), b.get("ecart_luminance"), None, "niveaux")
        m = p.get("melange")
        if m and a.get("sol_eclaire") and a.get("sol_a_l_ombre"):
            pred = B.de_hexa(a["sol_eclaire"]) * (1 - float(m["force"])) + B.de_hexa(m["teinte"]) * float(m["force"])
            d = B.de2000(B.de_hexa(a["sol_a_l_ombre"]), pred)
            tab.lignes.append(dict(grandeur=f"ombre « {et} » : notre mélange ({m['teinte']} à {int(100 * float(m['force']))} %) appliqué au sol de la référence, contre l'ombre mesurée",
                                   reference=a["sol_a_l_ombre"], nous=B.hexa(pred), ecart=round(d, 1), tolerance=tol["delta_e"], unite="ΔE2000", ok=bool(d < tol["delta_e"])))
    lignes = tab.lignes
    n_ok = sum(1 for l in lignes if l["ok"]); n_ko = sum(1 for l in lignes if l["ok"] is False)
    resume = dict(reference=ref.get("id"), nous=nous.get("id"), echelle=round(k, 4), dans_la_tolerance=n_ok, hors_tolerance=n_ko,
                  sans_tolerance=len(lignes) - n_ok - n_ko, tolerances=tol, avertissements=avert)
    (sortie / f"{nom}_ecarts.json").write_text(json.dumps(dict(resume=resume, lignes=lignes), ensure_ascii=False, indent=1), encoding="utf-8")
    def fr(v):
        return "—" if v is None else (str(v).replace(".", ",") if isinstance(v, (int, float)) else f"`{v}`" if str(v).startswith("#") else str(v))
    md = [f"# Contrôle chiffré : {ref.get('id')} (référence) contre {nous.get('id')} (nous)", "",
          f"**{n_ok} grandeurs dans la tolérance, {n_ko} hors tolérance**, {len(lignes) - n_ok - n_ko} données sans tolérance. Mêmes scripts de mesure des deux côtés."
          + (f" Tour de correction n° {tour} sur {TOURS_MAX}." if tour is not None else ""), ""]
    md += [f"> {a}" for a in avert] + ([""] if avert else [])
    md += ["| Grandeur | Référence | Nous | Écart | Tolérance | Verdict |", "|---|---|---|---|---|---|"]
    for l in lignes:
        v = "—" if l["ok"] is None else ("dans la tolérance" if l["ok"] else "**hors tolérance**")
        t = "—" if l["tolerance"] is None else f"{fr(l['tolerance'])} {l['unite']}"
        e = "—" if l["ecart"] is None else f"{fr(l['ecart'])} {l['unite']}"
        md.append(f"| {l['grandeur']} | {fr(l['reference'])} | {fr(l['nous'])} | {e} | {t} | {v} |")
    md += ["", "Rappel : quand une ligne hors tolérance vient de la forme propre d'un dessin (bosses d'un trait tracé à la main, tache, objet qui touche le contour), "
           "on ne la corrige pas : la reproduire serait recopier le dessin. On la laisse hors tolérance et on écrit pourquoi."]
    (sortie / f"{nom}_ecarts.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    if figs:
        B.empiler(figs).save(sortie / f"{nom}_courbes.png")
    if profs:
        rang = [B.empiler(profs[i:i + 2], horizontal=True) for i in range(0, len(profs), 2)]
        B.empiler(rang).save(sortie / f"{nom}_profils.png")
    if tour is not None:
        td = sortie / "tours"; td.mkdir(exist_ok=True)
        (td / f"tour{tour}_ecarts.md").write_text("\n".join(md) + "\n", encoding="utf-8")
        fs = td / "suivi.json"
        suivi = json.loads(fs.read_text(encoding="utf-8-sig")) if fs.exists() else {}
        suivi[str(tour)] = dict(dans_la_tolerance=n_ok, hors_tolerance=n_ko)
        fs.write_text(json.dumps(suivi, indent=1), encoding="utf-8")
    return resume, lignes

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("reference"); ap.add_argument("nous"); ap.add_argument("sortie")
    ap.add_argument("--paires"); ap.add_argument("--nom", default="controle"); ap.add_argument("--tour", type=int)
    a = ap.parse_args()
    paires = json.loads(pathlib.Path(a.paires).read_text(encoding="utf-8-sig")) if a.paires else None
    resume, lignes = comparer(a.reference, a.nous, a.sortie, paires, a.nom, a.tour)
    print(f"{resume['dans_la_tolerance']} grandeurs dans la tolérance, {resume['hors_tolerance']} hors tolérance ({resume['sans_tolerance']} sans tolérance)")
    for l in lignes:
        if l["ok"] is False:
            print("  HORS :", l["grandeur"], "| réf", l["reference"], "| nous", l["nous"], "| écart", l["ecart"], l["unite"])
    for av in resume["avertissements"]:
        print("ATTENTION :", av)
    if a.tour is not None and a.tour >= TOURS_MAX:
        print(f"Tour {a.tour} : c'est le dernier ({TOURS_MAX} tours de correction au plus). Ce qui reste hors tolérance s'écrit dans le compte rendu, avec sa raison.")
    print(f"écrit : {pathlib.Path(a.sortie) / (a.nom + '_ecarts.md')}")

if __name__ == "__main__":
    main()
