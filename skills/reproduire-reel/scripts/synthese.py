#!/usr/bin/env python3
"""Synthèse des mesures d'une référence : un tableau par forme mesurée, la LOI commune du contour, la palette par ambiance.

  python synthese.py <dossier des mesures> [--prefixe ref_] [--mini 27] [--sans ref_0512] [--sortie <dossier>]
      lit tous les <prefixe>*.json écrits par mesurer.py ; --mini : nombre minimal d'orientations valides (sur 72) pour qu'un
      cercle entre dans le calcul de la loi ; --sans : écarte une image (en mouvement) ou une forme (ref_0990:tete-b).

Ce que donne la loi. Pour chaque forme ronde, l'épaisseur du contour (en fraction de son diamètre D) est ajustée par
  épaisseur = a0 + h1 × cos(orientation − direction du plein)          (la « loi_simple » du fichier de mesure).
Deux choses se lisent ensuite :
  - a0 et h1 sont-ils les mêmes d'une forme à l'autre, à toutes les tailles ? Alors le contour suit une règle proportionnelle ;
  - le côté fin du trait est-il le côté clair de l'ombrage (colonne « Écart délié / clair », mesure indépendante) ? Alors la
    règle est « trait fin côté lumière, épais côté ombre ».
C'est cette règle qu'on reproduit, pas les bosses de chaque dessin. La courbe superposée est recalée sur le côté du délié :
elle montre la hauteur et l'amplitude communes, elle ne prouve pas à elle seule le lien avec la lumière.
Sorties : synthese.json, synthese_formes.md, synthese_palettes.md, synthese_epaisseur.png.
Dépendances : Python 3.9+, numpy, Pillow, opencv-python. Écrit par Flot Web.
"""
import sys
sys.dont_write_bytecode = True
import argparse, json, math, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np
import mp_base as B, mp_forme as T

def _arr(v):
    return np.array([np.nan if x is None else x for x in v], dtype=float)

def _mediane_hex(liste):
    return B.hexa(np.median(np.array([B.de_hexa(h) for h in liste]), 0)) if liste else None

def synthese(dossier, prefixe="ref_", mini=27, sortie=None, sans=()):
    S = pathlib.Path(dossier); sortie = pathlib.Path(sortie or dossier); sortie.mkdir(parents=True, exist_ok=True)
    sans = set(sans)
    lignes, series, lois, pal = [], [], [], {}
    ang = np.arange(0, 360, 5)
    for f in sorted(S.glob(f"{prefixe}*.json")):
        r = json.loads(f.read_text(encoding="utf-8-sig"))
        if "formes" not in r:
            continue
        amb = r.get("ambiance") or "non précisée"
        P = pal.setdefault(amb, dict(images=[], trait=[], clair=[], sombre=[], traits_constants=[], sols=[]))
        P["images"].append(r["id"])
        for m in r.get("membres", {}).values():
            if m.get("couleur"):
                P["traits_constants"].append(m["couleur"])
        for o in r.get("ombres", {}).values():
            if o.get("sol_eclaire"):
                P["sols"].append((o["sol_eclaire"], o["sol_a_l_ombre"]))
        for nom, t in r["formes"].items():
            c, o = t.get("contour"), t.get("ombrage") or {}
            if not c:
                continue
            dz = o.get("deux_zones") or {}; fr = o.get("frontiere") or {}
            d = dict(image=r["id"], forme=nom, type=c["type"], ambiance=amb, D_px=c.get("D_px"), angles_valides=c["angles_valides"],
                     ep_moy_px=c.get("epaisseur_moy_px"), ep_moy_D=c.get("epaisseur_moy_D"), ep_min_D=c.get("epaisseur_min_D"), ep_max_D=c.get("epaisseur_max_D"),
                     trait=(c.get("trait") or {}).get("hex"), bord_int_px=c["bord"].get("transition_int_px"),
                     sur_brillance=c["accentuation"].get("sur_brillance_cote_remplissage"), creux=c["accentuation"].get("creux_dans_le_trait"),
                     halo=c["halo_luminance"].get("median"), ovale=(c.get("ovale") or {}).get("rapport"),
                     clair=(dz.get("claire") or {}).get("hex") or c.get("remplissage_hex"), sombre=(dz.get("sombre") or {}).get("hex"),
                     part_sombre=(dz.get("sombre") or {}).get("part"), saut_lum=fr.get("saut_luminance"), bord_doux=fr.get("transition_D"),
                     grain=o.get("grain_ecart_type"))
            if d["trait"]:
                P["trait"].append(d["trait"])
            if c["type"] == "cercle" and d["clair"]:
                P["clair"].append(d["clair"])
                if d["sombre"] and d["part_sombre"] and 0.08 <= d["part_sombre"] <= 0.45:
                    P["sombre"].append(d["sombre"])
            d["clair_vers_deg"] = fr.get("axe_vers_le_clair_deg") if (dz.get("base") == "claire" and (dz.get("part_secondaire") or 0) >= 0.08) else None
            if c["type"] == "cercle" and c.get("D_px"):
                e = _arr(c["courbe_5deg"]) / c["D_px"]
                co, fl, sig = T.harmoniques(ang, e, 1)          # la même loi simple que « loi_simple » du fichier de mesure
                if co is not None:
                    a1 = math.hypot(co[1], co[2]); plein = math.degrees(math.atan2(co[2], co[1])) % 360
                    d.update(loi_a0_D=round(float(co[0]), 4), loi_h1_D=round(a1, 4), plein_deg=round(plein), oppose_du_plein_deg=round((plein + 180) % 360), residu_D=round(sig, 4))
                    if d["clair_vers_deg"] is not None:         # le délié est-il du côté éclairé de l'ombrage ? (mesure indépendante du contour)
                        d["ecart_delie_clair_deg"] = round(abs(((plein + 180 - d["clair_vers_deg"] + 180) % 360) - 180))
                    motif = None
                    if r["id"] in sans or f"{r['id']}:{nom}" in sans:
                        motif = "écartée à la demande (--sans)"
                    elif c["angles_valides"] < mini:
                        motif = f"moins de {mini} orientations mesurables"
                    elif not (0.4 * a1 < co[0] and a1 < 3 * max(co[0], 1e-6)):
                        motif = "loi incohérente (trait collé à un autre objet sur un grand secteur)"
                    d["dans_la_loi"] = motif is None; d["motif_hors_loi"] = motif
                    if motif is None:
                        lois.append((co[0], a1))
                        rel = (ang - plein + 180) % 360          # 0° = côté du délié
                        k = np.argsort(rel)
                        series.append((f"{r['id']} {nom}", rel[k], e[k]))
            lignes.append(d)
    res = dict(formes=lignes)
    if lois:
        a0s, h1s = np.array([l[0] for l in lois]), np.array([l[1] for l in lois])
        gard = (np.abs(a0s - np.median(a0s)) < 0.5 * np.median(a0s))        # écarte les formes dont le trait est collé à autre chose
        a0, h1 = float(np.median(a0s[gard])), float(np.median(h1s[gard]))
        ec = [l["ecart_delie_clair_deg"] for l in lignes if l.get("dans_la_loi") and l.get("ecart_delie_clair_deg") is not None]
        res["loi"] = dict(a0_D=round(a0, 4), h1_D=round(h1, 4), delie_D=round(a0 - h1, 4), plein_D=round(a0 + h1, 4), formes=int(gard.sum()),
                          a0_D_etendue=[round(float(a0s[gard].min()), 4), round(float(a0s[gard].max()), 4)],
                          h1_D_etendue=[round(float(h1s[gard].min()), 4), round(float(h1s[gard].max()), 4)],
                          lecture="épaisseur = a0 − h1 × cos(angle compté depuis le côté du délié), en fraction de D ; "
                                  "construction : un disque d'encre de diamètre D et un disque de remplissage de rayon (0,5 − a0) D, décalé de h1 × D vers le côté du délié",
                          delie_du_cote_eclaire=dict(formes=len(ec), ecart_median_deg=round(float(np.median(ec))) if ec else None, ecarts_deg=ec,
                                                     lecture="écart entre le côté du délié (contour) et le côté clair de l'ombrage (mesure indépendante) : "
                                                             "sous 45°, le trait est fin côté lumière et épais côté ombre ; non mesuré si aucune forme n'a d'ombre propre"))
        th = np.arange(0, 361, 2)
        series.append((f"loi : {a0:.4f} − {h1:.4f} · cos(angle)".replace(".", ","), th, a0 - h1 * np.cos(np.radians(th)), (0, 0, 0), "tirets"))
        ymax = min(0.3, max(0.08, float(np.nanmax(np.concatenate([np.asarray(s[2], dtype=float) for s in series]))) * 1.1))
        B.courbe(series, "épaisseur du contour / D, angle compté depuis le côté du délié", "angle (°) : 0 = délié, 180 = plein. Les courbes sont recalées : seules leur hauteur et leur amplitude se comparent", "en D",
                 taille=(1500, 560), xlim=(0, 360), ylim=(0, ymax), xticks=list(range(0, 361, 45)), points=True).save(sortie / "synthese_epaisseur.png")
    palettes = {}
    for amb, P in pal.items():
        palettes[amb] = dict(images=P["images"], trait=_mediane_hex(P["trait"]), remplissage_clair=_mediane_hex(P["clair"]), remplissage_ombre=_mediane_hex(P["sombre"]),
                             traits_constants=_mediane_hex(P["traits_constants"]), sol_eclaire=_mediane_hex([s[0] for s in P["sols"]]),
                             sol_a_l_ombre=_mediane_hex([s[1] for s in P["sols"]]), nombre_de_formes=len(P["trait"]))
    res["palettes"] = palettes
    (sortie / "synthese.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    def p(v, n=3):
        return "—" if v is None else f"{v:.{n}f}".replace(".", ",")
    def h(v):
        return f"`{v}`" if v else "—"
    md = ["| Image | Forme | Type | Ambiance | D (px) | Orientations | Ép. moy. | Mini brut | Maxi brut | a0 (loi) | h1 (loi) | Plein vers | Clair de l'ombrage vers | Écart délié / clair | Trait | Zone claire | Zone sombre | Part sombre | Bord doux |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    def deg(v):
        return "—" if v is None else f"{round(float(v))}°"
    for l in lignes:
        ep = f"{p(l['ep_moy_D'])} D" if l.get("ep_moy_D") else (f"{p(l['ep_moy_px'], 1)} px" if l.get("ep_moy_px") else "—")
        md.append(f"| {l['image']} | {l['forme']} | {l['type']} | {l['ambiance']} | {p(l['D_px'], 0)} | {l['angles_valides']}/72 | {ep} | "
                  f"{p(l.get('ep_min_D'))} | {p(l.get('ep_max_D'))} | {p(l.get('loi_a0_D'))}{'' if l.get('dans_la_loi', True) else ' *'} | {p(l.get('loi_h1_D'))} | "
                  f"{deg(l.get('plein_deg'))} | {deg(l.get('clair_vers_deg'))} | {deg(l.get('ecart_delie_clair_deg'))} | {h(l['trait'])} | {h(l['clair'])} | {h(l['sombre'])} | "
                  f"{p(100 * l['part_sombre'], 0) + ' %' if l.get('part_sombre') is not None else '—'} | {p(l.get('bord_doux'))} |")
    md += ["", "Lecture des colonnes :",
           "- « a0 », « h1 », « Plein vers » : la loi simple `épaisseur = a0 + h1 × cos(orientation − plein)`, en fraction de D. Ce sont les valeurs `loi_simple` du fichier de mesure. "
           "Délié = a0 − h1, plein = a0 + h1.",
           "- « Mini brut », « Maxi brut » : extrêmes de la courbe. Le maxi brut est souvent gonflé par un endroit où le trait touche un autre trait (cou, main, chapeau) : préférer a0 + h1.",
           "- « Clair de l'ombrage vers » : direction du côté clair du remplissage, mesurée sur l'ombrage (indépendante du contour) ; vide si la forme n'a pas d'ombre propre mesurable.",
           "- « Écart délié / clair » : angle entre le côté fin du trait et le côté clair de l'ombrage. Sous 45° : le trait est fin côté lumière.",
           "- « Zone sombre » n'est une ombre que si sa part est entre 8 et 50 % : au-dessous c'est un liseré, au-dessus c'est la couleur de base (voir `lecture` dans le fichier de mesure).",
           "", "\\* forme écartée du calcul de la loi : " + ("; ".join(f"{l['image']} {l['forme']} ({l['motif_hors_loi']})" for l in lignes if l.get("motif_hors_loi")) or "aucune") + "."]
    if res.get("loi"):
        L = res["loi"]
        md += ["", f"**Loi commune** ({L['formes']} formes rondes) : épaisseur = {p(L['a0_D'], 4)} D − {p(L['h1_D'], 4)} D × cos(angle depuis le côté du délié) ; "
               f"délié {p(L['delie_D'], 4)} D, plein {p(L['plein_D'], 4)} D. a0 va de {p(L['a0_D_etendue'][0], 4)} à {p(L['a0_D_etendue'][1], 4)} D, "
               f"h1 de {p(L['h1_D_etendue'][0], 4)} à {p(L['h1_D_etendue'][1], 4)} D.",
               f"Le délié est-il du côté éclairé ? Écart médian {deg(L['delie_du_cote_eclaire']['ecart_median_deg'])} sur {L['delie_du_cote_eclaire']['formes']} formes "
               f"(écarts : {L['delie_du_cote_eclaire']['ecarts_deg']}).",
               "Une image en mouvement ou une forme peu mesurable s'écarte avec `--sans ref_0512` ou `--sans ref_0990:tete-b`."]
    (sortie / "synthese_formes.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    mp = ["| Ambiance | Images | Trait | Remplissage clair | Remplissage à l'ombre | Traits constants (membres) | Sol éclairé | Sol à l'ombre |", "|---|---|---|---|---|---|---|---|"]
    for amb, P in palettes.items():
        mp.append(f"| {amb} | {', '.join(P['images'])} | {h(P['trait'])} | {h(P['remplissage_clair'])} | {h(P['remplissage_ombre'])} | {h(P['traits_constants'])} | {h(P['sol_eclaire'])} | {h(P['sol_a_l_ombre'])} |")
    mp += ["", "Médianes par ambiance des formes rondes mesurées. Une case vide = non mesuré dans cette ambiance : ne rien inventer, mesurer une image de plus."]
    (sortie / "synthese_palettes.md").write_text("\n".join(mp) + "\n", encoding="utf-8")
    return res

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dossier"); ap.add_argument("--prefixe", default="ref_"); ap.add_argument("--mini", type=int, default=27); ap.add_argument("--sortie")
    ap.add_argument("--sans", action="append", default=[], help="image ou forme à écarter de la loi : ref_0512 ou ref_0990:tete-b (option répétable)")
    a = ap.parse_args()
    r = synthese(a.dossier, a.prefixe, a.mini, a.sortie, a.sans)
    print(f"{len(r['formes'])} formes ; loi : {json.dumps(r.get('loi'), ensure_ascii=False)}")
    for amb, P in r["palettes"].items():
        print(f"  {amb} : trait {P['trait']}, clair {P['remplissage_clair']}, ombre {P['remplissage_ombre']}")
