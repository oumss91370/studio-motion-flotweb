"""Contrôle chiffré avant livraison : « règle du prompt maître / mesuré sur le film / dans la tolérance ? ».

  python outils/controle.py [dossier des scripts de mesure]

Les mesures sont celles du skill reproduire-reel (mesurer.py pour le trait et l'ombrage des personnages, mp_decor.py pour le
décor) : les mêmes scripts que ceux qui ont mesuré le style. Leur dossier est cherché dans la variable MESURE_SCRIPTS, puis
dans <plugin>/skills/reproduire-reel/scripts, ou donné en argument.
Aucune cible n'est posée à la main : ce script sait où sont la tête, la jambe, l'ombre et le sol de chaque personnage (il les
projette comme compo.py) ; les cibles du décor sont décrites en coordonnées du MONDE dans film.CONTROLES.
Les images mesurées sont assemblées sans sous-titres (controle/<plan>_<image>.png), plus une image relue dans le film encodé.
Sorties : controle/controle.md, controle/controle.json, et les planches de mesurer.py.
Il vérifie aussi ce qui entre dans le champ (film.CONTROLE_CHAMP) : pas de mur nu derrière la tête et le torse d'un personnage,
aucun membre contre le bord gauche, droit ou haut du cadre, peu d'objets coupés par les bords ; et en intérieur la palette
(regles.INTERIEUR) et l'ombre du personnage. Ce qu'il ne voit pas : un personnage mal posé, un fond illisible, le jeu, le rythme. Il faut AUSSI
la critique d'un agent indépendant (references/prompt-maitre.md, rubrique Contrôles). Écrit par Flot Web.
"""
import json, math, os, pathlib, subprocess, sys
sys.dont_write_bytecode = True
ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import numpy as np
from PIL import Image
import regles as R
import camera as C
import pantin
import film as F
import compo

RAC = compo.RAC
SORTIE = RAC / "controle"
T = R.TOLERANCES


def _scripts():
    cand = [sys.argv[1] if len(sys.argv) > 1 else None, os.environ.get("MESURE_SCRIPTS"),
            ICI.parent.parent / "reproduire-reel" / "scripts", ICI.parent.parent.parent / "reproduire-reel" / "scripts"]
    for c in cand:
        if c and (pathlib.Path(c) / "mesurer.py").exists():
            return pathlib.Path(c)
    raise SystemExit("scripts de mesure introuvables : donner le dossier skills/reproduire-reel/scripts en argument ou dans MESURE_SCRIPTS")


class Tableau:
    def __init__(self):
        self.lignes = []

    def ligne(self, famille, regle, attendu, mesure, ok, note=""):
        self.lignes.append(dict(famille=famille, regle=regle, attendu=attendu, mesure=mesure, ok=None if ok is None else bool(ok), note=note))

    def borne(self, famille, regle, v, lo, hi, unite="", note="", n=3):
        att = f"{lo:g} à {hi:g} {unite}".strip()
        if v is None:
            return self.ligne(famille, regle, att, "non mesuré", None, note)
        self.ligne(famille, regle, att, f"{round(v, n):g} {unite}".strip(), lo <= v <= hi, note)

    def couleur(self, famille, regle, attendu, mesure, tol, MB, note=""):
        if not mesure:
            return self.ligne(famille, regle, f"{attendu} (ΔE < {tol:g})", "non mesuré", None, note)
        d = MB.de2000(MB.de_hexa(attendu), MB.de_hexa(mesure))
        self.ligne(famille, regle, f"{attendu} (ΔE < {tol:g})", f"{mesure} (ΔE {d:.1f})", d < tol, note)

    def ecrire(self, titre):
        ok = sum(1 for l in self.lignes if l["ok"]); ko = sum(1 for l in self.lignes if l["ok"] is False); nc = sum(1 for l in self.lignes if l["ok"] is None)
        md = [f"# {titre}", "", f"**{ok} dans la tolérance, {ko} hors tolérance, {nc} non mesurées** sur {len(self.lignes)}.", "",
              "| Famille | Règle du prompt maître | Attendu | Mesuré sur le film | Dans la tolérance ? | Note |", "|---|---|---|---|---|---|"]
        for l in self.lignes:
            v = "non mesuré" if l["ok"] is None else "oui" if l["ok"] else "**non**"
            md.append(f"| {l['famille']} | {l['regle']} | {l['attendu']} | {l['mesure']} | {v} | {l['note']} |")
        SORTIE.mkdir(parents=True, exist_ok=True)
        (SORTIE / "controle.md").write_text("\n".join(md) + "\n", encoding="utf-8")
        (SORTIE / "controle.json").write_text(json.dumps(dict(dans=ok, hors=ko, non_mesure=nc, lignes=self.lignes), ensure_ascii=False, indent=1), encoding="utf-8")
        return ok, ko, nc


def _ecart_angle(a, b):
    return abs(((b - a + 180) % 360) - 180)

def _image(k, f):
    """Image de contrôle : le plan assemblé, accentué, sans sous-titres."""
    SORTIE.mkdir(parents=True, exist_ok=True)
    ch = SORTIE / f"{k}_{f:04d}.png"
    if not ch.exists():
        compo.image_fixe(k, f).save(ch)
    return ch

def _boite(pts, marge=0.0):
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    x0, y0, x1, y1 = max(xs[0], xs[3]) if len(pts) == 4 else min(xs), min(ys), min(xs[1], xs[2]) if len(pts) == 4 else max(xs), max(ys)
    x0, x1 = sorted((x0, x1))
    return [int(max(0, x0 + marge)), int(max(0, y0 + marge)), int(min(R.LARGEUR, x1 - marge)), int(min(R.HAUTEUR, y1 - marge))]


def ombre_au_sol(tab, k, f, MES, MB):
    """Ombre projetée d'un personnage, sur un plan large où l'ombre du torse est dans le cadre : mélange et montée du bleu."""
    plan = F.PLANS[k]
    A = R.AMBIANCES[plan["ambiance"]]
    om = A["ombre_sol"]
    if om[0] != "projetee":
        return
    base = C.base(plan, f)
    nom, pos, p = F.acteurs(k, f)[0]
    coins, ecran, monde = compo.quad_ecran(nom, pos, base)
    c = pantin.PERSOS[nom]
    L = F.SOLEIL
    for part in (0.5, 0.3, 0.12):                # un point dans l'ombre du torse ; plus bas si l'ombre sort du cadre
        q = monde(pantin.AX, pantin.AY - (c["jambes"] + part * c["torse_h"]) * pantin.D)
        t = q[2] / -L[2] * om[4]
        b_ = C.projette(base, (q[0] + L[0] * t, q[1] + L[1] * t, 0.0))
        if 30 < b_[0] < R.LARGEUR - 30 and 30 < b_[1] < R.HAUTEUR - 30:
            break
    dpx = C.d_px(base, b_[2])
    dpx = min(dpx, 0.3 * R.LARGEUR)
    a_ = next(((b_[0] + s * 1.3 * dpx, b_[1]) for s in (1, -1) if 8 < b_[0] + s * 1.3 * dpx < R.LARGEUR - 8), (b_[0], b_[1]))
    fam = f"Personnage ({nom}, {plan['ambiance']}, {k}:{f})"
    ident = f"{k}_{f:04d}_ombre"
    fc = SORTIE / f"{ident}.json.cibles"
    fc.write_text(json.dumps(dict(id=ident, image=str(_image(k, f)), reference=dict(nom="D", px=round(dpx, 1)),
                                  ombres=[dict(nom="ombre", a=[round(a_[0]), round(a_[1])], b=[round(b_[0]), round(b_[1])])]), indent=1), encoding="utf-8")
    o = MES.mesurer(fc, SORTIE)["ombres"].get("ombre", {})
    if o.get("sol_eclaire") and o.get("sol_a_l_ombre"):
        sol = np.array(MB.de_hexa(o["sol_eclaire"]), float)
        att = sol * (1 - om[2]) + np.array(R.hexa(om[1]), float) * om[2]
        tab.couleur(fam, f"Ombre au sol = mélange à {om[2]:.0%} vers {om[1]}, pas une multiplication", MB.hexa(att), o["sol_a_l_ombre"], T["delta_e"], MB,
                    f"sol éclairé {o['sol_eclaire']} ; facteur par canal {o.get('facteur_rvb')}")
        fb = (o.get("facteur_rvb") or [0, 0, 0])[2]
        tab.ligne(fam, "Le bleu monte dans l'ombre (facteur > 1)", "> 1", f"{fb}", fb > 1.0)
        fl = o.get("flou_du_bord_10_90_px")
        tab.borne(fam, "Bord de l'ombre flou sur 0,11 à 0,13 D à mi-longueur (jusqu'à 0,5 D au bout d'une ombre longue)", None if not fl else fl / dpx, 0.06, 0.5, "D", f"{fl} px pour D = {dpx:.0f} px", 3)
    else:
        tab.ligne(fam, "Ombre au sol mélangée", "—", "non mesuré", None, str(o.get("erreur", "")))


def personnage(tab, k, f, nom, pos, p, MES, MB, fam=None):
    """Contour, ombrage, membres et ombre au sol d'un personnage debout (pose sans rotation du corps)."""
    plan = F.PLANS[k]
    amb = plan["ambiance"]
    A = R.AMBIANCES[amb]
    base = C.base(plan, f)
    fam = fam or f"Personnage ({nom}, {amb}, {k}:{f})"
    coins, ecran, monde = compo.quad_ecran(nom, pos, base)
    lum = compo.lumiere_ecran(k, base, pos)
    tx, ty = pantin.tete_dans_le_dessin(nom, p)
    cx, cy, zc = C.projette(base, monde(tx, ty))
    dpx = C.d_px(base, zc) * pantin.echelle(nom) * pantin.D / R.D_MONDE          # diamètre de la tête de CE personnage, à l'écran
    ident = f"{k}_{f:04d}_{nom}"
    c = pantin.PERSOS[nom]
    leg = c["jambes"] * pantin.D
    jx, jy = p["pied_g"]                                                          # la jambe va de la hanche au pied : on la mesure entre 30 % et 62 % de sa longueur
    hanche = (p["x"] * pantin.D - 0.13 * pantin.D, -(p["h"] * leg) - 0.05 * pantin.D)
    pied = (jx * pantin.D, -jy * pantin.D)
    def _sur_jambe(t):
        return C.projette(base, monde(pantin.AX + pied[0] + (hanche[0] - pied[0]) * t, pantin.AY + pied[1] + (hanche[1] - pied[1]) * t))[:2]
    ja, jb = _sur_jambe(0.62), _sur_jambe(0.30)
    # la tête est mesurée SANS coiffe, pour le contrôle seulement : une coiffe cache le côté éclairé du contour, donc le délié
    ch_nue = SORTIE / f"{k}_{f:04d}_{nom}_tete-nue.png"
    if not ch_nue.exists():
        coiffe = c["coiffe"]
        c["coiffe"] = None
        try:
            compo.image_fixe(k, f).save(ch_nue)
        finally:
            c["coiffe"] = coiffe
    cfg = dict(id=ident, image=str(ch_nue), ambiance=amb, plan=f"{k}:{f}", reference=dict(nom="D (diamètre de la tête)", forme="tete"),
               formes=[dict(nom="tete", type="cercle", centre=[round(cx), round(cy)], rayon=round(dpx / 2 * 0.97),
                            graine=[round(cx - 0.31 * dpx), round(cy + 0.19 * dpx)], rayon_graine=max(4, round(0.035 * dpx)),
                            exclure_angles=[[245, 295]])],        # le secteur du cou : le trait de la tête y touche celui du torse
               membres=[dict(nom="jambe", a=[round(ja[0]), round(ja[1])], b=[round(jb[0]), round(jb[1])], n=9, demi=round(max(12, 1.6 * R.CONTOUR["membres"] * dpx)))])
    om = A["ombre_sol"]
    if om[0] == "projetee":         # un point dans l'ombre du torse, un point à côté sur le sol éclairé
        L = F.SOLEIL
        q = monde(pantin.AX, pantin.AY - (leg + 0.5 * c["torse_h"] * pantin.D))
        t = q[2] / -L[2] * om[4]
        b_ = C.projette(base, (q[0] + L[0] * t, q[1] + L[1] * t, 0.0))
        if 0.0 < b_[1] < R.HAUTEUR - 6 and 0 < b_[0] < R.LARGEUR:
            cote = 1 if b_[0] < R.LARGEUR / 2 else -1
            a_ = (b_[0] + cote * 1.25 * dpx, b_[1])
            if 4 < a_[0] < R.LARGEUR - 4:
                cfg["ombres"] = [dict(nom="ombre", a=[round(a_[0]), round(a_[1])], b=[round(b_[0]), round(b_[1])])]
    fc = SORTIE / f"{ident}.json.cibles"
    fc.write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
    res = MES.mesurer(fc, SORTIE)
    tete = res["formes"].get("tete", {})
    rc = tete.get("contour") or {}
    ls = rc.get("loi_simple") or {}
    D_mes = rc.get("D_px")
    note_d = f"tête mesurée sans coiffe ; D mesuré {D_mes} px (attendu {dpx:.0f}) ; {rc.get('angles_valides')}/72 orientations"
    tab.borne(fam, "Délié du contour, côté lumière : 0,014 à 0,022 D", ls.get("delie_D"), *T["delie_D"], "D", note_d, 4)
    tab.borne(fam, "Plein du contour, côté ombre : 0,066 à 0,073 D", ls.get("plein_D"), *T["plein_D"], "D", "lu sur la loi, pas sur le maximum brut", 4)
    if ls.get("plein_vers_deg") is not None:
        e = _ecart_angle(ls["plein_vers_deg"], (lum + 180) % 360)
        tab.ligne(fam, "Le plein est à l'opposé de la lumière", f"{(lum + 180) % 360:.0f}° ± {T['angle_deg']:g}°", f"{ls['plein_vers_deg']:.0f}° (écart {e:.0f}°)", e <= T["angle_deg"])
    else:
        tab.ligne(fam, "Le plein est à l'opposé de la lumière", f"{(lum + 180) % 360:.0f}°", "non mesuré", None)
    tab.couleur(fam, "Encre de l'ambiance, jamais noire", A["encre"], (rc.get("trait") or {}).get("hex"), T["delta_e"], MB)
    acc = rc.get("accentuation") or {}
    tab.borne(fam, "Accentuation : +16 niveaux côté peau, sur 1 px", acc.get("sur_brillance_cote_remplissage"), 8, 24, "niveaux", "", 1)
    tab.borne(fam, "Bord du trait lissé sur 0,85 à 0,95 px", (rc.get("bord") or {}).get("transition_int_px"), 0.6, 1.5, "px", "tolérance élargie : image mise en perspective", 2)
    tab.borne(fam, "Ni halo ni contour clair autour du personnage", (rc.get("halo_luminance") or {}).get("median"), -4, 4, "niveaux", "", 1)
    omb = tete.get("ombrage") or {}
    dz = omb.get("deux_zones") or {}
    fr = omb.get("frontiere") or {}
    part = dz.get("part_secondaire")
    tab.borne(fam, "Tête : croissant d'ombre, 15 à 27 % du disque (pas un aplat)", None if part is None else 100 * part, 8, 35, "%", dz.get("lecture") or dz.get("note") or "", 1)
    if fr.get("axe_vers_le_clair_deg") is not None:
        e = _ecart_angle(fr["axe_vers_le_clair_deg"], lum)
        tab.ligne(fam, "Le côté clair de la tête regarde la lumière", f"{lum:.0f}° ± 30°", f"{fr['axe_vers_le_clair_deg']:.0f}° (écart {e:.0f}°)", e <= 30)
    tab.borne(fam, "Aucun grain sur la peau (écart type < 2)", omb.get("grain_ecart_type"), 0, 2.5, "niveaux", "", 2)
    j = res["membres"].get("jambe", {})
    tab.borne(fam, "Membres : trait constant de 0,054 à 0,061 D", j.get("largeur_D"), *T["membres_D"], "D", f"écart type {j.get('ecart_type_px')} px", 4)
    tab.couleur(fam, "Couleur des membres de l'ambiance", A["membres"], j.get("couleur"), T["delta_e"] + 2, MB)
    if "ombres" in cfg:
        o = res["ombres"].get("ombre", {})
        if o.get("sol_eclaire") and o.get("sol_a_l_ombre"):
            sol = np.array(MB.de_hexa(o["sol_eclaire"]), float)
            att = sol * (1 - om[2]) + np.array(R.hexa(om[1]), float) * om[2]
            tab.couleur(fam, f"Ombre au sol = mélange à {om[2]:.0%} vers {om[1]}, pas une multiplication", MB.hexa(att), o["sol_a_l_ombre"], T["delta_e"], MB,
                        f"sol éclairé {o['sol_eclaire']} ; facteur par canal {o.get('facteur_rvb')}")
            fb = (o.get("facteur_rvb") or [0, 0, 0])[2]
            tab.ligne(fam, "Le bleu monte dans l'ombre (facteur > 1)", "> 1", f"{fb}", fb > 1.0)
        else:
            tab.ligne(fam, "Ombre au sol mélangée", "—", "non mesuré", None, str(o.get("erreur", "")))
    return res


def champ(tab, k, f, MB):
    """Ce qui entre dans le champ, pour l'image f du plan k (regles.CHAMP). Trois vérifications simples :
    1. derrière la tête et le torse de chaque personnage (leur boîte élargie de 0,5 D), la part de décor « plat » : un pixel est plat
       si la luminance du décor seul varie de moins de 6 niveaux dans une fenêtre de 0,35 D. Un mur nu est plat ; une boiserie, un
       rayonnage, une tenture, même flous, ne le sont pas ;
    2. aucun pixel du personnage à moins de 3 px du bord gauche, droit ou haut du cadre (un membre coupé par le cadre) ;
    3. le nombre de silhouettes d'objets du décor que coupe le bord gauche ou droit, dans la zone nette (indicateur : un mur ou
       le sol qui sortent du cadre ne comptent pas, un meuble coupé compte)."""
    import cv2
    Ch = R.CHAMP
    plan = F.PLANS[k]
    base = C.base(plan, f)
    acteurs = F.acteurs(k, f)
    fam = f"Champ ({plan['ambiance']}, {k}:{f})"
    img, z, zf = compo.decor(k, f, acteurs)                           # le décor seul, tel qu'il est derrière les personnages
    L = MB.luma(np.clip(img, 0, 255))
    W, H = R.LARGEUR, R.HAUTEUR
    for nom, pos, p in acteurs:
        al = compo.silhouette(k, nom, pos, p, base)
        coins, ecran, monde = compo.quad_ecran(nom, pos, base)
        c = pantin.PERSOS[nom]
        tx, ty = pantin.tete_dans_le_dessin(nom, p)
        cx, cy, zc = C.projette(base, monde(tx, ty))
        dpx = C.d_px(base, zc) * pantin.echelle(nom) * pantin.D / R.D_MONDE
        _, yb, _ = C.projette(base, monde(pantin.AX, pantin.AY - c["jambes"] * pantin.D * p.get("h", 1.0)))      # le bas du torse
        m = Ch["marge"] * dpx
        x0, x1 = int(max(0, cx - 0.6 * dpx - m)), int(min(W, cx + 0.6 * dpx + m))
        y0, y1 = int(max(0, cy - 0.6 * dpx - m)), int(min(H, max(yb, cy + dpx)))
        if x1 - x0 > 8 and y1 - y0 > 8:
            n = max(3, int(Ch["fenetre"] * dpx) | 1)
            noyau = np.ones((n, n), np.uint8)
            etendue = cv2.dilate(L, noyau) - cv2.erode(L, noyau)
            plat = float((etendue[y0:y1, x0:x1] < Ch["seuil"]).mean())
            tab.borne(fam, f"{nom} : rien de nu derrière la tête et le torse (part de décor plat)", 100 * plat, 0, 100 * Ch["plat_max"], "%",
                      f"boîte [{x0}, {y0}, {x1}, {y1}] ; plat = moins de {Ch['seuil']:g} niveaux d'écart dans {n} px ({Ch['fenetre']:g} D)", 1)
        b = Ch["bord_px"]
        dedans = al > 0.5
        touche = [nm for nm, mk in (("gauche", dedans[:, :b]), ("droit", dedans[:, W - b:]), ("haut", dedans[:b, :])) if mk.any()]
        tab.ligne(fam, f"{nom} : aucun membre contre le bord gauche, droit ou haut du cadre", "aucun", ", ".join(touche) or "aucun", not touche)
    w = 1.0 / np.maximum(z, 0.05)                                     # silhouettes du décor (ruptures de profondeur), comme compo.contours
    sil = (np.abs(cv2.Laplacian(w, cv2.CV_32F, ksize=1)) / w > 0.012) & (z < 1.6 * zf)
    n_coupes = 0
    for x in (2, W - 3):
        col = sil[int(0.12 * H):, x].astype(np.int8)
        n_coupes += int((np.diff(col) == 1).sum())
    tab.borne(fam, "Objets du décor coupés par le bord gauche ou droit, dans la zone nette (indicateur)", n_coupes, 0, Ch["coupes_max"], "", "ruptures de profondeur qui touchent le bord", 0)


def interieur(tab, k, f, MD, MB):
    """Palette d'un plan d'intérieur (regles.INTERIEUR) et ombre du personnage : luminance, saturation, parts de prune sombre, de
    brun-rouge moyen et de froid (chaque dominante de l'image va à la dominante mesurée la plus proche), lisibilité de l'ombre."""
    I = R.INTERIEUR
    plan = F.PLANS[k]
    if plan["ambiance"] != "interieur":
        return
    fam = f"Intérieur ({k}:{f})"
    img = MB.lire(str(_image(k, f)))
    pal = MD.palette(img, k=12)
    tab.borne(fam, "Intérieur sombre : luminance moyenne de 61", pal["luminance_moyenne"], I["luminance"][0] - I["luminance"][1], I["luminance"][0] + I["luminance"][1], "", "", 1)
    tab.borne(fam, "Saturation moyenne de 0,58", pal["saturation_moyenne"], I["saturation"][0] - I["saturation"][1], I["saturation"][0] + I["saturation"][1], "", "", 3)
    ref = list(I["prune"]) + [I["brun_sombre"]] + list(I["chaud"]) + list(I["froid"]) + list(I["clairs"])
    parts = {c: 0.0 for c in ref}
    for d in pal["dominantes"]:
        c = min(ref, key=lambda r_: MB.de2000(MB.de_hexa(r_), MB.de_hexa(d["couleur"])))
        parts[c] += d["part_pct"]
    note = " ; ".join(f"{d['couleur']} {d['part_pct']:g} %" for d in pal["dominantes"][:8])
    pr = sum(parts[c] for c in I["prune"]); ch = sum(parts[c] for c in I["chaud"]); fr = sum(parts[c] for c in I["froid"])
    tab.borne(fam, "Prune très sombre (#251023, #3a1828) : près de la moitié de l'image", pr, 100 * (I["part_prune"][0] - I["part_prune"][1]), 100 * (I["part_prune"][0] + I["part_prune"][1]), "%", note, 1)
    tab.borne(fam, "Une seule dominante chaude, bruns-rouges moyens : un cinquième de l'image", ch, 100 * (I["part_chaud"][0] - I["part_chaud"][1]), 100 * (I["part_chaud"][0] + I["part_chaud"][1]), "%", f"brun sombre {parts[I['brun_sombre']]:.1f} %", 1)
    tab.borne(fam, "Contrepoint froid (violet #503056, bleu de nuit #312e79) : 6 à 9 %", fr, 100 * I["part_froid"][0] - 2.0, 100 * I["part_froid"][1] + 3.0, "%", "tolérance : 4 à 12 %", 1)
    for nom, pos, p in F.acteurs(k, f):
        o = ombre_interieur(k, f, nom, pos, p, MB)
        if o:
            tab.borne(fam, f"{nom} : ombre au sol lisible (luminance de l'ombre / sol voisin)", o["rapport"], *T["ombre_interieur"], "", f"sol {o['sol']:.0f}, ombre {o['ombre']:.0f} niveaux ; {o['pixels']} px", 2)
            if o.get("ecart_deg") is not None:
                tab.ligne(fam, f"{nom} : l'ombre part à l'opposé de la lampe", f"{o['attendu_deg']:.0f}° ± 25°", f"{o['mesure_deg']:.0f}° (écart {o['ecart_deg']:.0f}°)", o["ecart_deg"] <= 25)


def ombre_interieur(k, f, nom, pos, p, MB):
    """Ombre d'un personnage en intérieur, mesurée sur l'image : on compare l'image sans personnage et l'image avec, hors de sa
    silhouette. Renvoie le rapport de luminance ombre / sol, et la direction de l'ombre à l'écran (du pied vers son barycentre)
    comparée à la direction opposée à la lampe du plan (clé source)."""
    plan = F.PLANS[k]
    base = C.base(plan, f)
    liste = F.acteurs(k, f)
    sans, z, zf = compo.decor(k, f, liste)
    avec = sans.copy()
    for n_, q_, p_ in liste:
        compo.pose_perso(avec, z, k, n_, q_, p_, base, zf)
    al = compo.silhouette(k, nom, pos, p, base)
    import cv2
    hors = cv2.dilate((al > 0.02).astype(np.uint8), np.ones((9, 9), np.uint8)) == 0
    La, Ls = MB.luma(avec), MB.luma(sans)
    px, py, zc = C.projette(base, (pos[0], pos[1], 0.0))
    dpx = C.d_px(base, zc)
    yy, xx = np.mgrid[0:R.HAUTEUR, 0:R.LARGEUR]
    pres = np.hypot(xx - px, yy - py) < 4.0 * dpx
    m = hors & pres & (Ls - La > 0.12 * np.maximum(Ls, 20.0))          # assombri d'au moins 12 %
    if m.sum() < 200:
        return dict(rapport=1.0, sol=float(Ls[hors & pres].mean()), ombre=float(La[hors & pres].mean()), pixels=int(m.sum()))
    coeur = m & (Ls - La > 0.6 * np.percentile((Ls - La)[m], 90))
    out = dict(rapport=float(La[coeur].mean() / max(Ls[coeur].mean(), 1.0)), sol=float(Ls[coeur].mean()), ombre=float(La[coeur].mean()), pixels=int(m.sum()))
    S = plan.get("source")
    if S:
        poids = (Ls - La)[m]
        bx, by = float((xx[m] * poids).sum() / poids.sum()), float((yy[m] * poids).sum() / poids.sum())
        mes = math.degrees(math.atan2(-(by - py), bx - px))
        d = (pos[0] - S[0], pos[1] - S[1])
        n = math.hypot(*d) or 1.0
        ex, ey, _ = C.projette(base, (pos[0] + d[0] / n * 0.6, pos[1] + d[1] / n * 0.6, 0.0))
        att = math.degrees(math.atan2(-(ey - py), ex - px))
        out.update(mesure_deg=mes, attendu_deg=att, ecart_deg=_ecart_angle(mes, att))
    return out


def decor_cibles(tab, MD, MB):
    """Cibles du décor décrites dans film.CONTROLES, en coordonnées du monde."""
    cartes = {}
    for c in getattr(F, "CONTROLES", []):
        k, f = c["image"]
        plan = F.PLANS[k]
        base = C.base(plan, f)
        ch = _image(k, f)
        img = MB.lire(str(ch))
        fam = f"Décor ({plan['ambiance']}, {k}:{f})"
        zf = compo._point(k, f, base, F.acteurs(k, f))
        d_suj = C.d_px(base, zf)
        try:
            if c["type"] == "bois":             # une pièce de bois nette et éclairée : (x0, y0, x1, y1) au niveau z
                x0, y0, x1, y1 = c["zone"]; z = c.get("z", 0.0)
                pts = [C.projette(base, q) for q in ((x0, y1, z), (x1, y1, z), (x1, y0, z), (x0, y0, z))]
                bo = _boite([p[:2] for p in pts], 6)
                r = MD.texture(img, bo, c.get("axe", "x"))
                B_ = R.BOIS
                tab.borne(fam, f"{c['nom']} : bois dessiné, contraste du fil de {B_['contraste'][0]:g} à {B_['contraste'][1]:g} niveaux", r.get("contraste_ecart_type"), *T["bois_contraste"], "niveaux",
                          f"boîte {bo} ; couleur {r.get('couleur_mediane')} ; tolérance ± 6", 1)
                tab.borne(fam, f"{c['nom']} : grain fin de {B_['grain_fin'][0]:g} à {B_['grain_fin'][1]:g} niveaux", r.get("grain_fin"), B_["grain_fin"][0] - 4.0, B_["grain_fin"][1] + 4.0, "niveaux",
                          f"{r.get('lignes')} lignes, épaisseur {r.get('ligne_epaisseur_px')} px ; tolérance ± 4", 1)
            elif c["type"] == "texture":        # zone du sol ou d'un mur : (x0, y0, x1, y1) au niveau z
                x0, y0, x1, y1 = c["zone"]; z = c.get("z", 0.0)
                pts = [C.projette(base, q) for q in ((x0, y1, z), (x1, y1, z), (x1, y0, z), (x0, y0, z))]
                bo = _boite([p[:2] for p in pts], 6)
                d_loc = C.d_px(base, sum(p[2] for p in pts) / 4)
                r = MD.texture(img, bo, c.get("axe", "x"))
                tab.borne(fam, f"{c['nom']} : matière dessinée, contraste de 8 à 21 niveaux (un aplat : moins de 3)", r.get("contraste_ecart_type"), *T["contraste_matiere"], "niveaux",
                          f"boîte {bo} ; grain fin {r.get('grain_fin')}", 1)
                if c.get("joints"):
                    per = r.get("periode_px")
                    tab.borne(fam, f"{c['nom']} : un joint tous les 0,32 D", None if not per else per / d_loc, *T["joints_D"], "D",
                              f"période d'autocorrélation {per} px pour D = {d_loc:.0f} px (le fil du bois fausse le compte des lignes)", 3)
            elif c["type"] == "trait":          # segment du monde en travers de la silhouette d'un objet net
                a, b = C.projette(base, c["a"]), C.projette(base, c["b"])
                d_loc = C.d_px(base, min(a[2], b[2]))
                r = MD.trait(img, a[:2], b[:2])
                e = r.get("epaisseur_px") if r.get("trait") else None
                tab.borne(fam, f"{c['nom']} : contour de silhouette de 0,02 à 0,034 D", None if e is None else e / d_loc, *T["silhouette_D"], "D",
                          f"{e} px pour D = {d_loc:.0f} px ; couleur {r.get('couleur')}", 3)
                if r.get("trait"):
                    tab.couleur(fam, f"{c['nom']} : trait à l'encre de l'ambiance", R.AMBIANCES[plan["ambiance"]]["decor"]["encre"], r.get("couleur"), 12.0, MB,
                                "tolérance large : l'encre du décor est mêlée à la teinte locale")
            elif c["type"] == "fond":           # segment du monde en travers d'une arête lointaine : flou de profondeur
                a, b = C.projette(base, c["a"]), C.projette(base, c["b"])
                r = MD.bord(img, a[:2], b[:2])
                l = r.get("largeur_10_90_px")
                sg = float(compo._flou_sigma(zf, np.array((a[2] + b[2]) / 2, dtype=np.float32), d_suj))
                att = 2.563 * sg / d_suj                                  # bord 10–90 % d'un flou gaussien = 2,563 × l'écart type ; 0,14 D pour un fond très lointain
                tab.borne(fam, f"{c['nom']} : flou = 0,055 D × |d point / d objet − 1| (0,14 D sur un fond très lointain)", None if l is None else l / d_suj,
                          round(att * 0.75, 3), round(att * 1.25, 3), "D",
                          f"{l} px pour D du sujet = {d_suj:.0f} px ; objet à {(a[2] + b[2]) / 2:.0f} m, sujet à {zf:.1f} m : la règle donne {att:.3f} D {r.get('erreur', '')}", 3)
            elif c["type"] == "sol_net":        # zone du sol autour des pieds du sujet
                x0, y0, x1, y1 = c["zone"]
                pts = [C.projette(base, q)[:2] for q in ((x0, y1, 0), (x1, y1, 0), (x1, y0, 0), (x0, y0, 0))]
                bo = [int(max(0, min(p[0] for p in pts))), int(max(0, min(p[1] for p in pts))), int(min(R.LARGEUR, max(p[0] for p in pts))), int(min(R.HAUTEUR, max(p[1] for p in pts)))]
                if ch not in cartes:
                    cartes[ch] = MD.nettete_carte(img)
                r = MD.nettete_boite(cartes[ch], bo)
                tab.borne(fam, f"{c['nom']} : sol net sous les pieds (transitions de 2,0 à 2,3 px)", r.get("transitions_les_plus_nettes_px"), 0.3, T["sol_net_px"], "px",
                          f"boîte {bo} ; médiane {r.get('transition_mediane_px')} px {r.get('erreur', '')}", 2)
        except Exception as e:                  # une cible mal posée ne doit pas faire perdre les autres
            tab.ligne(fam, c.get("nom", c["type"]), "—", "non mesuré", None, f"{type(e).__name__} : {e}")
    for k, f in sorted({c["image"] for c in getattr(F, "CONTROLES", []) if c["type"] != "texture"}):
        img = MB.lire(str(_image(k, f)))
        d = MD.densite(img)
        tab.borne(f"Décor ({F.PLANS[k]['ambiance']}, {k}:{f})", "Densité : 112 à 202 petits segments par image", d["petits_segments"], *T["petits_segments"], "",
                  f"segments {d['segments']} ; bords nets {d['part_bords_pct']} %, bords doux {d['part_bords_doux_pct']} %", 0)
        g = MD.grain(img)
        tab.borne(f"Décor ({F.PLANS[k]['ambiance']}, {k}:{f})", "Aucun grain ajouté (0,06 à 0,34 niveau mesuré)", g, 0, 1.0, "niveaux", "", 2)


def film_encode(tab, MES, MB):
    """Une image relue dans le film encodé : la loi du contour doit survivre à la compression."""
    mp4 = RAC / "sortie" / "film.mp4"
    c = getattr(F, "CONTROLE_FILM", None)
    if not mp4.exists() or not c:
        return
    k, f = c
    ch = SORTIE / f"film_{f:04d}.png"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(mp4), "-vf", f"select=eq(n\\,{f})", "-frames:v", "1", str(ch)], check=True)
    nom, pos, p = F.acteurs(k, f)[0]
    base = C.base(F.PLANS[k], f)
    coins, ecran, monde = compo.quad_ecran(nom, pos, base)
    tx, ty = pantin.tete_dans_le_dessin(nom, p)
    cx, cy, zc = C.projette(base, monde(tx, ty))
    dpx = C.d_px(base, zc)
    fc = SORTIE / f"film_{f:04d}.json.cibles"
    fc.write_text(json.dumps(dict(id=f"film_{f:04d}", image=str(ch), formes=[dict(nom="tete", type="cercle", centre=[round(cx), round(cy)], rayon=round(dpx / 2 * 0.97))]), indent=1), encoding="utf-8")
    res = MES.mesurer(fc, SORTIE)
    ls = ((res["formes"].get("tete") or {}).get("contour") or {}).get("loi_simple") or {}
    fam = f"Film encodé (image {f})"
    tab.borne(fam, "Délié du contour après encodage", ls.get("delie_D"), *T["delie_D"], "D", "", 4)
    tab.borne(fam, "Plein du contour après encodage", ls.get("plein_D"), *T["plein_D"], "D", "", 4)


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__); return
    S = _scripts()
    sys.path.insert(0, str(S))
    import mesurer as MES, mp_base as MB, mp_decor as MD
    tab = Tableau()
    SORTIE.mkdir(parents=True, exist_ok=True)
    for k, f in getattr(F, "CONTROLE_PERSONNAGES", []):
        for nom, pos, p in F.acteurs(k, f):
            try:
                personnage(tab, k, f, nom, pos, p, MES, MB)
            except Exception as e:
                tab.ligne(f"Personnage ({nom}, {k}:{f})", "mesure du personnage", "—", "non mesuré", None, f"{type(e).__name__} : {e}")
    for k, f in getattr(F, "CONTROLE_OMBRES", []):
        try:
            ombre_au_sol(tab, k, f, MES, MB)
        except Exception as e:
            tab.ligne(f"Personnage ({k}:{f})", "ombre au sol", "—", "non mesuré", None, f"{type(e).__name__} : {e}")
    decor_cibles(tab, MD, MB)
    for k, f in getattr(F, "CONTROLE_CHAMP", getattr(F, "CONTROLE_PERSONNAGES", [])):
        try:
            champ(tab, k, f, MB)
        except Exception as e:
            tab.ligne(f"Champ ({k}:{f})", "ce qui entre dans le champ", "—", "non mesuré", None, f"{type(e).__name__} : {e}")
        try:
            interieur(tab, k, f, MD, MB)
        except Exception as e:
            tab.ligne(f"Intérieur ({k}:{f})", "palette et ombre", "—", "non mesuré", None, f"{type(e).__name__} : {e}")
    film_encode(tab, MES, MB)
    S_ = R.SOUS_TITRES
    tab.ligne("Sous-titres", "Bloc dans la zone utile (y de 160 à 1 560), 1 à 3 mots", "centre y = 1 350 ; 3 mots au plus",
              f"centre y = {S_['y_centre']} ; {max(len(t.split()) for _, _, t in F.CARTONS)} mots au plus", 160 < S_["y_centre"] - S_["corps"] and S_["y_centre"] + S_["corps"] < 1560 and max(len(t.split()) for _, _, t in F.CARTONS) <= S_["mots_max"],
              "lu dans les données du film, pas mesuré sur l'image")
    ok, ko, nc = tab.ecrire("Contrôle chiffré du film")
    print(f"{ok} dans la tolérance, {ko} hors tolérance, {nc} non mesurées -> {SORTIE / 'controle.md'}")
    for l in tab.lignes:
        v = "?" if l["ok"] is None else "ok" if l["ok"] else "HORS"
        print(f"  [{v:4s}] {l['famille']} | {l['regle']} | attendu {l['attendu']} | mesuré {l['mesure']} | {l['note'][:80]}")


if __name__ == "__main__":
    main()
