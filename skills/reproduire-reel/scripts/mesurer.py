#!/usr/bin/env python3
"""Mesure au pixel : lance toutes les mesures décrites dans un fichier de cibles, écrit les chiffres, les courbes et la planche annotée.

  python mesurer.py <cibles.json> <dossier de sortie>

Le fichier de cibles désigne ce qu'on mesure sur UNE image (coordonnées en pixels de l'image, posées à la main avec grille.py) :
des formes cernées d'un trait (cercle, ellipse, rectangle, polygone, masque), des coupes en travers d'un trait, des traits
d'épaisseur constante (membres, tiges), des bouts de trait, des zones de couleur, des ombres au sol.
Format complet et exemples : references/fichier-de-cibles.md.

Les mêmes scripts servent pour la référence et pour nos rendus : seul le fichier de cibles change.
Sorties : <id>.json (tous les chiffres), <id>_planche.jpg (planche d'ensemble), et par forme <id>_<forme>_bords.jpg
(l'image de contrôle : à ouvrir pour vérifier que les points suivent bien les deux bords du trait), _courbe.png,
_profils.png, _carte.png.
Dépendances : Python 3.9+, numpy, Pillow, opencv-python (ou opencv-python-headless). Écrit par Flot Web.
"""
import sys
sys.dont_write_bytecode = True
import json, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np
import cv2
from PIL import Image, ImageDraw
import mp_base as B, mp_forme as T, mp_coupes as C

ERREURS = (ValueError, KeyError, IndexError, TypeError, cv2.error)      # une cible mal écrite ne doit pas arrêter la mesure des autres
NOMS ={"C": "coupe", "M": "trait", "B": "bout", "Z": "zone", "O": "ombre"}
TEINTES = {"C": (255, 255, 0), "M": (0, 255, 120), "B": (255, 140, 0), "Z": (255, 255, 255), "O": (0, 220, 255)}

def _pc(v):
    return "—" if v is None else f"{100 * v:.1f} %".replace(".", ",")

def _fichier(nom):
    return re.sub(r"[^0-9A-Za-zÀ-ÿ_-]+", "-", str(nom)).strip("-")

def _formes(cfg):
    """Formes de la cible ; accepte l'ancienne écriture "tetes": [{"nom", "graine": [x, y, rayon]}]."""
    out = list(cfg.get("formes", []))
    for t in cfg.get("tetes", []):
        x, y, r = t["graine"]
        out.append(dict(nom=t["nom"], type="cercle", centre=[x, y], rayon=r))
    return out

def mesurer(cfg_path, sortie):
    cfg_path = pathlib.Path(cfg_path); sortie = pathlib.Path(sortie); sortie.mkdir(parents=True, exist_ok=True)
    cfg = B.lire_json(cfg_path)
    if "image" not in cfg:
        raise SystemExit(f"{cfg_path} : il manque le champ \"image\" (chemin de l'image à mesurer, relatif au fichier de cibles)")
    img = str(cfg["image"])
    base = img.rsplit("@", 1)[0] if "@" in img and img.rsplit("@", 1)[1].isdigit() else img
    if not pathlib.Path(base).is_absolute():
        img = str((cfg_path.parent / base).resolve()) + img[len(base):]
    rgb = B.lire(img)
    ident = cfg.get("id") or cfg_path.stem
    res = dict(id=ident, image=str(cfg["image"]),
               taille=[rgb.shape[1], rgb.shape[0]], ambiance=cfg.get("ambiance"), plan=cfg.get("plan"),
               note=cfg.get("note"), formes={}, coupes={}, membres={}, bouts={}, zones={}, ombres={})
    planches, erreurs = [], {}
    encre = np.array([45.0, 28, 42])
    ref = cfg.get("reference") or {}                      # grandeur de référence : {"nom": "D", "forme": "tete-a"} ou {"nom": "hauteur de capitale", "px": 53}
    if not isinstance(ref, dict):
        raise SystemExit(f"{cfg_path} : \"reference\" s'écrit {{\"nom\": \"D\", \"forme\": \"<nom d'un cercle>\"}} ou {{\"nom\": \"…\", \"px\": 53}}")
    ref = dict(ref)
    D = float(ref["px"]) if ref.get("px") else None
    premiere_encre = True

    def erreur(rubrique, nom, e, type_=None):
        msg = f"{type(e).__name__} : {e}" if not isinstance(e, ValueError) else str(e)
        if isinstance(e, KeyError):
            msg = f"champ manquant dans la cible : {e}"
        erreurs[f"{rubrique} « {nom} »"] = msg
        res[rubrique][nom] = dict(erreur=msg, **({"type": type_} if type_ else {}))
        print(f"  ! {rubrique} « {nom} » non mesurée : {msg}")

    def une_forme(fo, nom):
        nonlocal D, encre, premiere_encre
        c = T.contour(rgb, fo, cfg_path.parent)
        rc = T.resume_contour(c)
        bloc = dict(type=c["type"], contour=rc)
        veut_ombrage = fo.get("ombrage", not c["toutes"])
        omb, extra = (T.ombrage(c, rgb) if veut_ombrage else (None, None))
        if omb is not None:
            bloc["ombrage"] = omb
        if not c["toutes"] and fo.get("details", True):
            bloc["details_internes"] = T.details_internes(c, rgb)
        if c["toutes"]:
            bloc["composantes"] = T.composantes(c)
        res["formes"][nom] = bloc
        if premiere_encre:
            encre = c["encre"]; premiere_encre = False
        if D is None and rc.get("D_px") and (ref.get("forme") in (None, nom)):
            D = rc["D_px"]; ref.setdefault("nom", "D (diamètre de la forme « " + nom + " »)"); ref["forme"] = nom
        if rc.get("avertissement"):
            print(f"  ! forme « {nom} » : {rc['avertissement']}")
        base_f = f"{ident}_{_fichier(nom)}"
        titre_c = f"{ident} · {nom}" + (f" · D = {rc['D_px']} px" if rc.get("D_px") else "")
        f_c = T.fig_courbe(rc, titre_c); f_c.save(sortie / f"{base_f}_courbe.png")
        f_a = T.fig_annotee(c, rgb, rc)
        f_a.save(sortie / f"{base_f}_bords.jpg", quality=90)       # l'image de contrôle, à ouvrir seule : les points y sont lisibles
        if f_a.width > 800:
            f_a = f_a.resize((800, int(f_a.height * 800 / f_a.width)), Image.LANCZOS)
        f_p = f_k = None
        if omb is not None and extra is not None and "profils_diametres" in omb:
            f_p = T.fig_profils(omb); f_p.save(sortie / f"{base_f}_profils.png")
            f_k = T.fig_carte(c, rgb, extra); f_k.save(sortie / f"{base_f}_carte.png")
        tr = rc.get("trait", {}); ls = rc.get("loi_simple", {})
        taille = f"D = {rc['D_px']} px" if rc.get("D_px") else f"remplissage {rc.get('largeur_px')} × {rc.get('hauteur_px')} px"
        lignes = [
            f"{taille} ; orientations mesurées : {rc['angles_valides']}/72 ({rc['coupes_valides']} coupes sur {rc['coupes_total']}) ; ovale {rc.get('ovale', {}).get('rapport')}",
            f"épaisseur : moy {rc.get('epaisseur_moy_px')} px, min {rc.get('epaisseur_min_px')} px à {rc.get('angle_min')}°, max {rc.get('epaisseur_max_px')} px à {rc.get('angle_max')}°",
            f"loi simple : a0 {ls.get('a0_px')} px, h1 {ls.get('h1_px')} px, plein vers {ls.get('plein_vers_deg')}° : délié {ls.get('delie_px')} px, plein {ls.get('plein_px')} px"
            + (f" (soit {ls.get('delie_D')} D et {ls.get('plein_D')} D)" if ls.get("plein_D") else "") + f" ; écart type autour de la loi à 2 harmoniques {rc.get('tremble_px')} px",
            f"trait : {tr.get('hex')} (luminance {tr.get('luminance_mediane')}) ; remplissage {rc.get('remplissage_hex')} ; bord : transition {rc['bord']['transition_int_px']} px (int.), {rc['bord']['transition_ext_px']} px (ext.)",
            f"accentuation : +{rc['accentuation']['sur_brillance_cote_remplissage']} côté remplissage, −{rc['accentuation']['creux_dans_le_trait']} dans le trait ; halo {rc['halo_luminance']['median']}",
        ]
        if omb is not None and "deux_zones" in omb and "claire" in omb["deux_zones"]:
            dz = omb["deux_zones"]; fr = omb.get("frontiere", {})
            lignes += [
                f"remplissage : zone claire {dz['claire']['hex']} ({_pc(dz['claire']['part'])}), zone sombre {dz['sombre']['hex']} ({_pc(dz['sombre']['part'])}), ΔE {dz['delta_e']} : {dz.get('lecture')}",
                f"frontière : le clair est vers {fr.get('axe_vers_le_clair_deg')}° ; "
                + (f"saut {fr.get('saut_luminance')} niveaux sur {fr.get('transition_px')} px" if fr.get("saut_luminance") is not None
                   else "saut non mesuré (zone secondaire trop petite ou frontière introuvable)") + f" ; grain σ {omb.get('grain_ecart_type')}",
                "reflets : " + (" ; ".join(f"{r['hex']} à {r['rayon_R']} R, {r['angle_deg']}°, {r['aire_pct']} %" for r in omb["reflets"]["liste"][:3]) or "aucun"),
            ]
        if bloc.get("composantes"):
            k = bloc["composantes"]
            lignes.append(f"morceaux : {k['nombre']} ; grandes lettres (capitales, hampes) : {k['hauteur_des_grandes_lettres_px']} px ; petites lettres : "
                          f"{k['hauteur_des_petites_lettres_px']} px ; boîte du texte {k['boite']} ; centre {k['centre']}")
        if rc.get("angles_ecartes"):
            lignes.append("écartés : " + " ; ".join(f"{m} ({len(a)} orientations)" for m, a in rc["angles_ecartes"].items()))
        titre = f"{ident} · forme « {nom} » ({c['type']}) · {cfg.get('ambiance') or ''} · {cfg.get('plan') or ''}"
        rang = [B.texte_img(lignes, largeur=1700, titre=titre), B.empiler([x for x in (f_a, f_k) if x is not None], horizontal=True),
                B.empiler([x for x in (f_c, f_p) if x is not None], horizontal=True)]
        planches.append(B.empiler(rang))

    for k_f, fo in enumerate(_formes(cfg)):
        nom = str(fo.get("nom") or f"forme-{k_f + 1}")
        try:
            une_forme(fo, nom)
        except ERREURS as e:
            erreur("formes", nom, e, fo.get("type", "cercle"))

    def enD(px, n=4):
        return round(px / D, n) if D and px else None
    H_, W_ = rgb.shape[:2]
    def dans_l_image(*pts):
        for p in pts:
            if not (0 <= p[0] < W_ and 0 <= p[1] < H_):
                raise ValueError(f"le point {list(p)} est hors de l'image ({W_} × {H_})")
        if len(pts) == 2 and list(pts[0]) == list(pts[1]):
            raise ValueError("les deux bouts du segment sont au même point")
    marques = []
    for k_c, cdef in enumerate(cfg.get("coupes", [])):
        nom = str(cdef.get("nom") or f"coupe-{k_c + 1}")
        try:
            dans_l_image(cdef["a"], cdef["b"])
            sq = C.sequence(rgb, cdef["a"], cdef["b"])
            for e in sq:
                if D and e["largeur_px"]:
                    e["largeur_D"] = enD(e["largeur_px"])
            res["coupes"][nom] = dict(groupe=cdef.get("groupe"), sequence=sq, bande=C.bande(rgb, cdef["a"], cdef["b"]))
            marques.append(("C", nom, cdef["a"], cdef["b"], " | ".join(e["couleur"] + (f" {e['largeur_px']} px" if e["largeur_px"] else "") for e in sq)))
        except ERREURS as e:
            erreur("coupes", nom, e)
    for k_c, m in enumerate(cfg.get("membres", []) + cfg.get("traits", [])):
        nom = str(m.get("nom") or f"trait-{k_c + 1}")
        try:
            dans_l_image(m["a"], m["b"])
            r = C.membre(rgb, m["a"], m["b"], m.get("n", 9), m.get("demi"))
            if D and r.get("largeur_mediane_px"):
                r["largeur_D"] = enD(r["largeur_mediane_px"]); r["longueur_D"] = enD(r["longueur_px"], 3)
            res["membres"][nom] = r
            marques.append(("M", nom, m["a"], m["b"],
                            f"{r.get('largeur_mediane_px', '—')} px (σ {r.get('ecart_type_px', '—')}, effilement {r.get('effilement_px_du_debut_a_la_fin', '—')}) {r.get('couleur', '')}"))
        except ERREURS as e:
            erreur("membres", nom, e)
    for k_c, m in enumerate(cfg.get("bouts", [])):
        nom = str(m.get("nom") or f"bout-{k_c + 1}")
        try:
            dans_l_image(m["a"], m["b"])
            r = C.bout(rgb, m["a"], m["b"], m["largeur"])
            res["bouts"][nom] = r
            marques.append(("B", nom, m["a"], m["b"], f"{r.get('forme', '—')} (arrondi sur {r.get('longueur_arrondi_en_largeur', '—')} largeur)"))
        except ERREURS as e:
            erreur("bouts", nom, e)
    for k_c, z in enumerate(cfg.get("zones", [])):
        nom = str(z.get("nom") or f"zone-{k_c + 1}")
        try:
            r = C.zone(rgb, z["poly"], B.de_hexa(z["encre"]) if z.get("encre") else encre, z.get("k", 3))
            res["zones"][nom] = r
            marques.append(("Z", nom, z["poly"], None, " / ".join(f"{c['hex']} {_pc(c['part'])}" for c in r.get("couleurs", [])) or r.get("erreur", "")))
        except ERREURS as e:
            erreur("zones", nom, e)
    for k_c, o in enumerate(cfg.get("ombres", [])):
        nom = str(o.get("nom") or f"ombre-{k_c + 1}")
        try:
            dans_l_image(o["a"], o["b"])
            r = C.ombre_sol(rgb, o["a"], o["b"])
            if D and r.get("flou_du_bord_10_90_px"):
                r["flou_D"] = enD(r["flou_du_bord_10_90_px"])
            res["ombres"][nom] = r
            marques.append(("O", nom, o["a"], o["b"],
                            f"{r.get('sol_eclaire', '')} → {r.get('sol_a_l_ombre', '')}, facteur {r.get('facteur_rvb', '')}, flou {r.get('flou_du_bord_10_90_px', '—')} px {r.get('erreur', '')}"))
        except ERREURS as e:
            erreur("ombres", nom, e)
    if marques:
        planches.append(_planche_reste(rgb, marques, ident))
    res["reference"] = dict(nom=ref.get("nom"), px=D, forme=ref.get("forme")) if D else None
    res["D_px"] = D
    if D:                                                   # tout exprimer en fraction de la grandeur de référence
        for nom, bloc in res["formes"].items():
            rc = bloc.get("contour")
            if not rc:
                continue
            er = {k.replace("_px", "_ref"): enD(rc[k]) for k in ("epaisseur_moy_px", "epaisseur_min_px", "epaisseur_max_px", "largeur_px", "hauteur_px") if rc.get(k)}
            if rc.get("loi_simple"):
                er.update(a0_ref=enD(rc["loi_simple"]["a0_px"], 5), h1_ref=enD(rc["loi_simple"]["h1_px"], 5),
                          delie_ref=enD(rc["loi_simple"]["delie_px"], 5), plein_ref=enD(rc["loi_simple"]["plein_px"], 5))
            er["rapporte_a"] = f"{ref.get('nom')} = {D} px" + (f" (forme « {ref.get('forme')} »)" if ref.get("forme") else "")
            er["note"] = "une seule grandeur de référence par image ; pour un cercle, les valeurs _D sont rapportées à SON propre diamètre"
            rc["en_reference"] = er
    if erreurs:
        res["erreurs"] = erreurs
    (sortie / f"{ident}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    res["planche"] = bool(planches)
    if planches:
        B.empiler(planches).save(sortie / f"{ident}_planche.jpg", quality=88)
    (sortie / f"{ident}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    return res

def _planche_reste(rgb, marques, ident):
    pts = []
    for kind, nom, a, b, txt in marques:
        pts += a if kind == "Z" else [a, b]
    pts = np.array(pts)
    x0, y0 = np.maximum(pts.min(0) - 60, 0).astype(int)
    x1, y1 = np.minimum(pts.max(0) + 60, [rgb.shape[1], rgb.shape[0]]).astype(int)
    im = B.agrandir(rgb[y0:y1, x0:x1], 1); d = ImageDraw.Draw(im); f = B.police(14, True)
    lignes = []
    for i, (kind, nom, a, b, txt) in enumerate(marques, 1):
        col = TEINTES[kind]
        if kind == "Z":
            pp = [(x - x0, y - y0) for x, y in a]
            d.line(pp + [pp[0]], fill=col, width=1); pos = pp[0]
        else:
            d.line((a[0] - x0, a[1] - y0, b[0] - x0, b[1] - y0), fill=col, width=2 if kind == "M" else 1)
            pos = (a[0] - x0, a[1] - y0)
        d.text(pos, str(i), fill=col, font=f, anchor="mm", stroke_width=3, stroke_fill=(0, 0, 0))
        lignes.append(f"{i}. [{NOMS[kind]}] {nom} : {txt}")
    if im.height > 1300:
        k = 1300 / im.height
        im = im.resize((int(im.width * k), 1300), Image.LANCZOS)
    return B.empiler([im, B.texte_img(lignes, largeur=1100, t=14, titre=f"{ident} · coupes, traits, zones, ombres")], horizontal=True)

def main():
    if len(sys.argv) < 3 or sys.argv[1] in ("-h", "--help"):
        print(__doc__); sys.exit(0 if len(sys.argv) > 1 else 2)
    r = mesurer(sys.argv[1], sys.argv[2])
    for nom, t in r["formes"].items():
        c = t.get("contour")
        if not c:
            continue
        print(f"{r['id']} · {nom} ({t['type']}) : " + (f"D {c['D_px']} px, " if c.get("D_px") else "")
              + f"{c['angles_valides']}/72 orientations, ép. moy {c.get('epaisseur_moy_px')} px, min {c.get('epaisseur_min_px')} à {c.get('angle_min')}°, "
              f"max {c.get('epaisseur_max_px')} à {c.get('angle_max')}°, trait {c.get('trait', {}).get('hex')}, remplissage {c.get('remplissage_hex')}")
    print(f"écrit : {pathlib.Path(sys.argv[2]) / (r['id'] + '.json')}" + (f", {r['id']}_planche.jpg et une image de contrôle _bords.jpg par forme" if r.get("planche") else
                                                                         " (aucune planche : rien n'a pu être mesuré)"))
    if r.get("erreurs"):
        print(f"{len(r['erreurs'])} cible(s) non mesurée(s) : voir « erreurs » dans le fichier, corriger la cible et relancer")

if __name__ == "__main__":
    main()
