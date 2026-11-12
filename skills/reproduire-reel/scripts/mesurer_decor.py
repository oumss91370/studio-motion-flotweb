#!/usr/bin/env python3
"""Mesure au pixel du DÉCOR d'une image, d'après la rubrique "decor" du fichier de cibles (le même fichier que mesurer.py).

  python mesurer_decor.py <cibles.json> <dossier de sortie> [--bande y0,y1]

Sans rubrique "decor", les mesures globales sont faites quand même : palette (10 dominantes), densité (segments, bords),
grain, netteté par bande. La rubrique "decor" ajoute les mesures ciblées, posées à la main avec grille.py :

  "decor": {
    "bande_exclue": [1285, 1415],                        bande horizontale ignorée par les mesures globales (les sous-titres)
    "graines": {"sol": [[540, 1600]], "ciel": [[300, 150]], "murs": [[150, 900]]},      parts de l'image, dégradés, bords assombris
    "mesures": [
      {"nom": "plancher : lames",        "type": "texture", "boite": [350, 1500, 750, 1600], "axe": "x", "famille": "sol"},
      {"nom": "poteau : silhouette",     "type": "trait",   "a": [650, 900], "b": [700, 900], "famille": "contour"},
      {"nom": "ombre portée : bord",     "type": "bord",    "a": [470, 1090], "b": [470, 1200], "famille": "ombre"},
      {"nom": "sol éclairé",             "type": "zone",    "boite": [600, 1050, 800, 1150]},
      {"nom": "cailloux",                "type": "details", "boite": [300, 1300, 1000, 1880]},
      {"nom": "lampe",                   "type": "halo",    "centre": [400, 1105], "rmax": 230},
      {"nom": "sol sous le sujet",       "type": "nettete", "boite": [0, 1440, 1080, 1680]},
      {"nom": "focale",                  "type": "optique", "verticales": [[[100, 300], [108, 1500]], [[960, 300], [950, 1500]]], "horizon_y": 1000}
    ]
  }

La grandeur de référence D (diamètre de la tête du personnage, en px) vient du champ "reference" du fichier de cibles :
{"px": 312} (valeur donnée), ou {"forme": "tete-a"} (lue dans <id>.json si mesurer.py est déjà passé dans ce dossier, sinon
mesurée ici). Une cible peut porter son propre "D" (objet à une autre profondeur). Toutes les longueurs sortent aussi en D.
Format complet et lecture des sorties : references/fichier-de-cibles.md, § 8.

Les mêmes scripts servent pour la référence et pour nos rendus : seul le fichier de cibles change.
Sorties : <id>_decor.json (chiffres) et <id>_decor_planche.jpg (image annotée : cibles numérotées, palette, légende).
Dépendances : Python 3.9+, numpy, Pillow, opencv-python (ou opencv-python-headless). Écrit par Flot Web.
"""
import sys
sys.dont_write_bytecode = True
import argparse, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np
import cv2
from PIL import Image, ImageDraw
import mp_base as B, mp_decor as MD

ERREURS = (ValueError, KeyError, IndexError, TypeError, ZeroDivisionError, cv2.error)   # une cible mal posée ne doit pas faire perdre les autres
COUL = dict(bord=(255, 60, 60), trait=(60, 255, 90), texture=(255, 220, 0), zone=(0, 220, 255), details=(255, 120, 255), halo=(255, 160, 0),
            optique=(255, 255, 255), nettete=(150, 200, 255))
EN_D = ("largeur_10_90_px", "epaisseur_px", "periode_px", "ligne_epaisseur_px", "ligne_espacement_px", "rayon_mi_hauteur_px")
TYPES = "bord, trait, texture, zone, details, halo, nettete, optique"

def chemin_image(cfg, cfg_path):
    """Chemin de l'image (relatif au fichier de cibles, ou absolu ; « video.mp4@990 » accepté), comme dans mesurer.py."""
    if "image" not in cfg:
        raise SystemExit(f"{cfg_path} : il manque le champ \"image\" (chemin de l'image à mesurer, relatif au fichier de cibles)")
    img = str(cfg["image"])
    base = img.rsplit("@", 1)[0] if "@" in img and img.rsplit("@", 1)[1].isdigit() else img
    if not pathlib.Path(base).is_absolute():
        img = str((pathlib.Path(cfg_path).parent / base).resolve()) + img[len(base):]
    return img

def grandeur_de_reference(cfg, cfg_path, rgb, sortie, ident):
    """D en px et d'où il vient : "reference": {"px": …} ; sinon <id>.json déjà écrit par mesurer.py ; sinon mesure de la forme."""
    ref = cfg.get("reference") or {}
    if not isinstance(ref, dict):
        raise SystemExit(f"{cfg_path} : \"reference\" s'écrit {{\"nom\": \"D\", \"forme\": \"<nom d'un cercle>\"}} ou {{\"nom\": \"…\", \"px\": 312}}")
    if ref.get("px"):
        return float(ref["px"]), "valeur donnée dans le fichier de cibles"
    deja = pathlib.Path(sortie) / f"{ident}.json"
    if deja.exists():
        try:
            d = B.lire_json(deja).get("D_px")
            if d:
                return float(d), f"lue dans {deja.name} (mesurer.py)"
        except (ValueError, OSError):
            pass
    formes = [f for f in cfg.get("formes", []) if f.get("type", "cercle") == "cercle"]
    voulue = ref.get("forme")
    for fo in formes:
        if voulue in (None, fo.get("nom")):
            try:
                import mp_forme as T
                rc = T.resume_contour(T.contour(rgb, fo, pathlib.Path(cfg_path).parent))
                if rc.get("D_px"):
                    return float(rc["D_px"]), f"mesurée sur la forme « {fo.get('nom')} »"
            except ERREURS as e:
                print(f"  ! grandeur de référence : la forme « {fo.get('nom')} » n'a pas pu être mesurée ({e})")
    return None, None

def une_mesure(rgb, c, D, carte):
    t = c.get("type")
    if t == "bord":
        return MD.bord(rgb, c["a"], c["b"], c.get("larg", 9))
    if t == "trait":
        return MD.trait(rgb, c["a"], c["b"], c.get("larg", 7), bool(c.get("clair", False)))
    if t == "texture":
        return MD.texture(rgb, c["boite"], c.get("axe", "x"), float(c.get("angle", 0.0)))
    if t == "zone":
        return MD.zone(rgb, c["boite"])
    if t == "details":
        return MD.details(rgb, c["boite"], D)
    if t == "halo":
        return MD.halo(rgb, c["centre"], c["rmax"])
    if t == "nettete":
        return MD.nettete_boite(carte, c["boite"])
    if t == "optique":
        return MD.optique(c["verticales"], c["horizon_y"], rgb.shape[0], rgb.shape[1])
    raise ValueError(f"type de mesure inconnu : {t!r} (types : {TYPES})")

def mesurer(cfg_path, sortie, bande=None):
    cfg_path = pathlib.Path(cfg_path); sortie = pathlib.Path(sortie); sortie.mkdir(parents=True, exist_ok=True)
    cfg = B.lire_json(cfg_path)
    img = chemin_image(cfg, cfg_path)
    rgb = B.lire(img)
    h, w = rgb.shape[:2]
    ident = cfg.get("id") or cfg_path.stem
    dec = cfg.get("decor") or {}
    if not isinstance(dec, dict):
        raise SystemExit(f"{cfg_path} : \"decor\" est un objet {{\"bande_exclue\": …, \"graines\": …, \"mesures\": […]}}")
    if bande is None:
        bande = dec.get("bande_exclue")
    if bande is not None and (len(bande) != 2 or bande[0] >= bande[1]):
        raise SystemExit(f"{cfg_path} : \"bande_exclue\" s'écrit [y_haut, y_bas], en pixels")
    D, origine = grandeur_de_reference(cfg, cfg_path, rgb, sortie, ident)
    if dec.get("D"):
        D, origine = float(dec["D"]), "valeur \"D\" de la rubrique decor"
    res = dict(id=ident, image=str(cfg["image"]), image_lue=img, taille=[w, h], ambiance=cfg.get("ambiance"), plan=cfg.get("plan"), note=cfg.get("note"),
               D_px=D, D_origine=origine, bande_exclue=list(bande) if bande else None)
    res["palette"] = MD.palette(rgb, bande=bande)
    res["densite"] = MD.densite(rgb, bande=bande)
    res["grain"] = MD.grain(rgb, bande=bande)
    carte = MD.nettete_carte(rgb)
    res["nettete"] = MD.nettete_resume(carte)
    erreurs, cartes = {}, {}
    if dec.get("graines"):
        try:
            res["parts_pct"], cartes = MD.regions(rgb, dec["graines"], float(dec.get("tolerance_graines", 11.0)))
            res["degrades"] = {k: MD.degrade(rgb, m) for k, m in cartes.items()}
            res["vignettage"] = {k: MD.vignettage(rgb, m) for k, m in cartes.items()}
        except ERREURS as e:
            erreurs["graines"] = str(e); print(f"  ! graines non mesurées : {e}")
    res["mesures"] = []
    for i, c in enumerate(dec.get("mesures", []), 1):
        nom = str(c.get("nom") or f"mesure-{i}")
        Dc = c.get("D") or D
        try:
            for cle in ("a", "b", "centre"):
                if cle in c and not (0 <= c[cle][0] < w and 0 <= c[cle][1] < h):
                    raise ValueError(f"le point {list(c[cle])} est hors de l'image ({w} × {h})")
            r = une_mesure(rgb, c, Dc, carte)
        except ERREURS as e:
            msg = f"champ manquant dans la cible : {e}" if isinstance(e, KeyError) else str(e) if isinstance(e, ValueError) else f"{type(e).__name__} : {e}"
            r = dict(erreur=msg)
        if r.get("erreur"):
            erreurs[f"mesure « {nom} »"] = r["erreur"]; print(f"  ! mesure « {nom} » : {r['erreur']}")
        if Dc:
            for cle in EN_D:
                if r.get(cle) is not None:
                    r[cle.replace("_px", "_D")] = round(r[cle] / Dc, 4)
        res["mesures"].append(dict(n=i, nom=nom, type=c.get("type"), famille=c.get("famille"), D_px=Dc, resultat=r))
    if erreurs:
        res["erreurs"] = erreurs
    (sortie / f"{ident}_decor.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    planche(rgb, dec, res, cartes, sortie / f"{ident}_decor_planche.jpg")
    return res

def planche(rgb, dec, res, cartes, chemin):
    h, w = rgb.shape[:2]
    base = rgb.copy()
    teintes = dict(ciel=(60, 120, 255), sol=(255, 200, 60), murs=(255, 80, 200), plafond=(140, 255, 140))
    for k, m in cartes.items():                                   # familles en liseré coloré
        bordure = m ^ np.roll(m, 3, 0) | m ^ np.roll(m, 3, 1)
        base[bordure] = np.array(teintes.get(k, (255, 255, 255)), np.float32)
    if res.get("bande_exclue"):
        y0, y1 = [int(v) for v in res["bande_exclue"]]
        base[max(0, y0):max(0, y1)] = base[max(0, y0):max(0, y1)] * 0.45
    e = h / 1920                                                  # la planche est dessinée pour une image de 1 920 px de haut
    colw = int(900 * e)
    toile = Image.new("RGB", (w + colw, h), (24, 24, 28))
    toile.paste(Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)), (0, 0))
    d = ImageDraw.Draw(toile)
    f1, f2 = B.police(max(11, int(26 * e)), True), B.police(max(9, int(19 * e)), True)
    ep = max(1, int(3 * e))
    for i, c in enumerate(dec.get("mesures", []), 1):
        col = COUL.get(c.get("type"), (255, 255, 255))
        try:
            if "a" in c and "b" in c:
                d.line([tuple(c["a"]), tuple(c["b"])], fill=col, width=ep); pos = c["a"]
            elif "boite" in c:
                x0, y0, x1, y1 = c["boite"]
                d.rectangle((min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1)), outline=col, width=ep); pos = (min(x0, x1), min(y0, y1))
            elif "centre" in c:
                x, y = c["centre"]; r = c["rmax"]; d.ellipse((x - r, y - r, x + r, y + r), outline=col, width=ep); pos = (x - r, y - r)
            elif "verticales" in c:
                for p, q in c["verticales"]:
                    d.line([tuple(p), tuple(q)], fill=col, width=ep)
                d.line([(0, c["horizon_y"]), (w, c["horizon_y"])], fill=col, width=max(1, ep - 1)); pos = c["verticales"][0][0]
            else:
                continue
            d.text((pos[0] + 4, pos[1] - int(30 * e)), str(i), font=f1, fill=col, stroke_width=ep, stroke_fill=(0, 0, 0))
        except ERREURS:
            continue
    x0c, y = w + int(14 * e), int(12 * e)
    p = res["palette"]
    d.text((x0c, y), f"{res['id']} — {res.get('ambiance') or ''} — {res.get('plan') or ''}"[:70], font=f1, fill=(255, 255, 255)); y += int(38 * e)
    x = x0c
    for c in p["dominantes"]:
        lg = max(4, int((colw - 40 * e) * c["part_pct"] / 100))
        d.rectangle((x, y, x + lg, y + int(46 * e)), fill=c["couleur"])
        x += lg
    y += int(52 * e)
    d.text((x0c, y), "  ".join(f"{c['couleur']} {c['part_pct']:.0f}%" for c in p["dominantes"][:6]), font=f2, fill=(230, 230, 230)); y += int(24 * e)
    d.text((x0c, y), "  ".join(f"{c['couleur']} {c['part_pct']:.0f}%" for c in p["dominantes"][6:]), font=f2, fill=(230, 230, 230)); y += int(28 * e)
    lignes = [f"saturation {p['saturation_moyenne']}  luminance {p['luminance_moyenne']}  contraste {p['contraste']}  grain {res['grain']}",
              f"segments {res['densite']['segments']} (+{res['densite']['petits_segments']} petits)  bords nets {res['densite']['part_bords_pct']} %  doux {res['densite']['part_bords_doux_pct']} %",
              f"netteté : médiane {res['nettete']['mediane_px']} px ; par bande (haut → bas) {res['nettete']['net_par_bande']}",
              f"D = {res['D_px']} px ({res['D_origine']})" if res.get("D_px") else "D non donné : pas de valeurs en D"]
    if "parts_pct" in res:
        lignes.append("parts : " + "  ".join(f"{k} {v} %" for k, v in res["parts_pct"].items()))
    for l in lignes:
        d.text((x0c, y), l[:100], font=f2, fill=(200, 220, 255)); y += int(24 * e)
    y += int(8 * e)
    cles = dict(bord=("cote_a", "cote_b", "largeur_10_90_px", "largeur_10_90_D", "facteur_rvb"), trait=("epaisseur_px", "epaisseur_D", "couleur", "cote_a", "cote_b"),
                texture=("couleur_mediane", "contraste_ecart_type", "periode_px", "ligne_epaisseur_px", "ligne_espacement_px", "ligne_espacement_D", "ligne_profondeur", "grain_fin"),
                zone=("couleur", "ecart_type"), details=("nombre", "diametre_median_D", "densite_par_D2"), halo=("rayon_mi_hauteur_px", "couleur_coeur", "couleur_fond"),
                nettete=("transitions_les_plus_nettes_px", "transition_mediane_px"), optique=("convergence_deg", "focale_mm_capteur36_vertical", "inclinaison_deg"))
    court = (("_px", "px"), ("largeur_10_90", "l1090"), ("epaisseur", "ép"), ("contraste_ecart_type", "σ"), ("ligne_", "l."), ("transitions_les_plus_nettes", "net"))
    for m in res["mesures"]:
        if y > h - int(50 * e):
            break
        col = COUL.get(m["type"], (255, 255, 255))
        r = m["resultat"]
        bouts = []
        for k in cles.get(m["type"], ()):
            if r.get(k) is not None:
                nomk = k
                for a_, b_ in court:
                    nomk = nomk.replace(a_, b_)
                bouts.append(f"{nomk}={r[k]}")
        d.text((x0c, y), f"{m['n']}. {m['nom']}"[:96], font=f2, fill=col); y += int(22 * e)
        d.text((x0c + int(20 * e), y), (" ".join(bouts) or str(r.get("erreur", "")))[:96], font=f2, fill=(225, 225, 225)); y += int(26 * e)
    toile.save(chemin, quality=88)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cibles", help="fichier de cibles JSON (le même que pour mesurer.py)")
    ap.add_argument("sortie", help="dossier de sortie")
    ap.add_argument("--bande", help="bande horizontale à exclure des mesures globales, y0,y1 en pixels (remplace \"bande_exclue\")")
    a = ap.parse_args()
    bande = [int(v) for v in a.bande.split(",")] if a.bande else None
    r = mesurer(a.cibles, a.sortie, bande)
    p = r["palette"]
    print(f"{r['id']} : saturation {p['saturation_moyenne']}, luminance {p['luminance_moyenne']}, segments {r['densite']['segments']} "
          f"(+{r['densite']['petits_segments']} petits), netteté par bande {r['nettete']['net_par_bande']}, {len(r['mesures'])} mesure(s) ciblée(s)"
          + (f", D = {r['D_px']} px" if r.get("D_px") else ", D non donné"))
    print(f"écrit : {pathlib.Path(a.sortie) / (r['id'] + '_decor.json')} et {r['id']}_decor_planche.jpg")
    if r.get("erreurs"):
        print(f"{len(r['erreurs'])} cible(s) non mesurée(s) : voir « erreurs » dans le fichier, corriger la cible et relancer")

if __name__ == "__main__":
    main()
