#!/usr/bin/env python3
"""Synthèse du décor par ambiance : palette commune (pixels de toutes les images de l'ambiance), moyennes des indicateurs,
et relevé de toutes les mesures ciblées en fraction de D.

  python synthese_decor.py <dossier des mesures> [--prefixe ref_] [--sortie DOSSIER]

Lit les <id>_decor.json écrits par mesurer_decor.py dont l'id commence par le préfixe, les regroupe par champ "ambiance",
relit les images (chemin noté dans chaque fichier) pour calculer les 10 dominantes de chaque ambiance.
Sorties : synthese_decor_<préfixe>.json et .md (un tableau par ambiance, puis un tableau des mesures ciblées).
Dépendances : Python 3.9+, numpy, Pillow, opencv-python. Écrit par Flot Web.
"""
import sys
sys.dont_write_bytecode = True
import argparse, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np
import mp_base as B, mp_decor as MD

CLES = dict(bord=("cote_clair", "cote_sombre", "facteur_rvb", "largeur_10_90_px", "largeur_10_90_D"), trait=("epaisseur_px", "epaisseur_D", "couleur"),
            texture=("couleur_mediane", "contraste_ecart_type", "ligne_espacement_px", "ligne_espacement_D", "ligne_epaisseur_D", "ligne_profondeur", "periode_D", "grain_fin", "degrade_niveaux"),
            zone=("couleur", "luminance"), details=("nombre", "diametre_median_D", "densite_par_D2", "part_couverte_pct"),
            halo=("couleur_coeur", "rayon_mi_hauteur_px", "rayon_mi_hauteur_D", "couleur_mi_rayon"), nettete=("transitions_les_plus_nettes_px", "transition_mediane_px"),
            optique=("convergence_deg", "focale_mm_capteur36_vertical", "champ_vertical_deg", "inclinaison_deg", "horizon_pct_de_la_hauteur"))

def synthese(dossier, prefixe="ref_", sortie=None):
    dossier = pathlib.Path(dossier); sortie = pathlib.Path(sortie or dossier); sortie.mkdir(parents=True, exist_ok=True)
    groupes, tous = {}, []
    for f in sorted(dossier.glob(f"{prefixe}*_decor.json")):
        r = B.lire_json(f)
        if "palette" in r:
            groupes.setdefault(r.get("ambiance") or "sans ambiance", []).append(r); tous.append(r)
    if not tous:
        raise SystemExit(f"aucun fichier {prefixe}*_decor.json dans {dossier} (lancer mesurer_decor.py d'abord)")
    out = {}
    for amb, rs in groupes.items():
        ims, manque = [], []
        for r in rs:
            try:
                ims.append((B.lire(r["image_lue"]), r.get("bande_exclue")))
            except (OSError, ValueError, KeyError):
                manque.append(r["id"])
        if ims and not manque:
            px = np.concatenate([im[MD.masque_global(im.shape[0], im.shape[1], b)][::23] for im, b in ims])
            dom = MD._kmeans_palette(px, 10)
        else:                                               # image introuvable : on garde la palette de la première image, et on le dit
            dom = rs[0]["palette"]["dominantes"]
        moy = lambda f: round(float(np.mean([f(r) for r in rs])), 2)
        out[amb] = dict(images=[r["id"] for r in rs], images_introuvables=manque, dominantes=dom,
                        saturation=moy(lambda r: r["palette"]["saturation_moyenne"]), luminance=moy(lambda r: r["palette"]["luminance_moyenne"]),
                        contraste=moy(lambda r: r["palette"]["contraste"]), dominante_chaude=moy(lambda r: r["palette"]["dominante_chaude"]),
                        segments=moy(lambda r: r["densite"]["segments"]), petits_segments=moy(lambda r: r["densite"]["petits_segments"]),
                        part_bords_pct=moy(lambda r: r["densite"]["part_bords_pct"]), part_bords_doux_pct=moy(lambda r: r["densite"]["part_bords_doux_pct"]),
                        gradient_moyen=moy(lambda r: r["densite"]["gradient_moyen"]), grain=moy(lambda r: r["grain"] or 0))
    nom = f"synthese_decor_{prefixe.strip('_') or 'tout'}"
    (sortie / f"{nom}.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    l = ["# Synthèse du décor par ambiance", "",
         "| Ambiance | Images | Saturation | Luminance | Contraste | Segments | Petits segments | Bords nets | Bords doux | Grain | Dominantes (part) |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for amb, s in out.items():
        l.append(f"| {amb} | {len(s['images'])} | {s['saturation']} | {s['luminance']} | {s['contraste']} | {s['segments']:.0f} | {s['petits_segments']:.0f} | {s['part_bords_pct']} % | {s['part_bords_doux_pct']} % | {s['grain']} | "
                 + ", ".join(f"`{d['couleur']}` {d['part_pct']:.0f} %" for d in s["dominantes"]) + (" (palette de la première image seulement : images introuvables)" if s["images_introuvables"] else "") + " |")
    l += ["", "# Mesures ciblées", "", "| Image | Ambiance | D (px) | Famille | Type | Mesure | Résultat |", "|---|---|---|---|---|---|---|"]
    for r in tous:
        for m in r.get("mesures", []):
            res = m["resultat"]
            txt = res.get("erreur") or " ; ".join(f"{k} {res[k]}" for k in CLES.get(m["type"], ()) if res.get(k) is not None) or ("pas de trait" if res.get("trait") is False else "—")
            l.append(f"| {r['id']} | {r.get('ambiance') or ''} | {m.get('D_px') or '—'} | {m.get('famille') or ''} | {m['type']} | {m['nom']} | {txt} |")
    (sortie / f"{nom}.md").write_text("\n".join(l) + "\n", encoding="utf-8")
    return out, sortie / f"{nom}.md"

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dossier"); ap.add_argument("--prefixe", default="ref_"); ap.add_argument("--sortie")
    a = ap.parse_args()
    s, f = synthese(a.dossier, a.prefixe, a.sortie)
    for amb, v in s.items():
        print(f"{amb} ({len(v['images'])} image(s)) : saturation {v['saturation']}, luminance {v['luminance']}, segments {v['segments']:.0f} (+{v['petits_segments']:.0f} petits), "
              f"bords nets {v['part_bords_pct']} %, doux {v['part_bords_doux_pct']} %")
        print("    " + " ".join(f"{d['couleur']} {d['part_pct']:.0f}%" for d in v["dominantes"]))
    print(f"écrit : {f}")

if __name__ == "__main__":
    main()
