#!/usr/bin/env python3
"""Contrôle chiffré du DÉCOR : tableau « référence / nous / écart / tolérance / verdict », piloté par un fichier de paires.

  python comparer_decor.py <paires-decor.json> <dossier de sortie> [--ref DOSSIER] [--nous DOSSIER] [--nom controle_decor] [--tour N]

Les chiffres des deux côtés viennent du MÊME script (mesurer_decor.py → <id>_decor.json), sur des images à cadrage comparable
(même type de plan, même ambiance). --ref et --nous : dossiers où sont ces fichiers (défaut : le dossier du fichier de paires).

Le fichier de paires (gabarit : gabarits/paires-decor.json) :
  { "tolerances": {"contour": {"abs": 1}},                          facultatif : remplace les valeurs par défaut
    "lignes": [
      {"famille": "Palette", "type": "palette", "grandeur": "extérieur au couchant", "ref": ["ref_0990", "ref_0795"], "nous": ["nous_0120", "nous_0200"]},
      {"famille": "Ombres",  "type": "couleur", "grandeur": "Sol à l'ombre", "ref": ["ref_0990", "sol à l'ombre", "couleur"], "nous": ["nous_0120", "sol à l'ombre", "couleur"], "tolerance": "ombre_delta_e"},
      {"famille": "Ombres",  "grandeur": "Dureté du bord de l'ombre", "ref": ["ref_0990", "ombre : bord", "largeur_10_90_px"], "nous": ["nous_0120", "ombre : bord", "largeur_10_90_px"], "tolerance": "durete"},
      {"famille": "Texture", "grandeur": "Plancher : espacement des joints", "ref": ["ref_1400", "plancher", "ligne_espacement_px"], "nous": ["nous_0040", "plancher", "periode_px"], "tolerance": "frequence"},
      {"famille": "Densité", "type": "global", "grandeur": "Segments", "ref": ["ref_1400", "densite.segments"], "nous": ["nous_0040", "densite.segments"], "tolerance": "densite"},
      {"famille": "Flou",    "type": "global", "grandeur": "Netteté du sol sous le sujet", "ref": ["ref_0990", "nettete.net_par_bande.6"], "nous": ["nous_0120", "nettete.net_par_bande.6"], "tolerance": "nettete_sol", "unite": "px"}
    ] }

Types de ligne :
  (défaut) mesure   ref et nous = [id de l'image, nom de la mesure ciblée, clé du résultat]. Une clé en « _px » est comparée EN D :
                    la valeur de la référence est ramenée à notre échelle (× D nous / D réf) ; "en_D": false pour l'empêcher.
  couleur           ref et nous = "#rrvvbb" ou [id, nom de la mesure, clé] ; écart en ΔE2000.
  global            ref et nous = [id, chemin.dans.le.fichier] (densite.segments, nettete.net_par_bande.6, palette.luminance_moyenne…).
  palette           ref et nous = listes d'ids d'une même ambiance : 10 dominantes sur les pixels réunis, appariées au plus proche ;
                    plus la saturation et la luminance moyennes.
Dans tous les types, ref peut aussi être un nombre ou une couleur donnés à la main (une valeur de la fiche de style).
"tolerance" : un nom de la table ci-dessous, ou {"abs": x}, ou {"rel": x} (0,25 = ± 25 %), ou un nombre (ΔE pour une couleur).

Tolérances par défaut (TOLERANCES) : palette ΔE < 8 et parts ± 8 points ; couleur d'ombre ΔE < 6, dureté ± 30 % ; texture :
fréquence ± 20 %, contraste ± 6 niveaux ; contours ± 1 px ; flou de profondeur ± 25 % ; densité ± 25 % ; netteté du sol ± 1 px.
Sorties : <nom>.md et <nom>.json ; avec --tour N, une copie dans tours/decor_tourN.md et le suivi tours/suivi_decor.json
(quatre tours de correction au plus). Dépendances : Python 3.9+, numpy, Pillow, opencv-python. Écrit par Flot Web.
"""
import sys
sys.dont_write_bytecode = True
import argparse, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np
import mp_base as B, mp_decor as MD

TOLERANCES = dict(palette_delta_e=8.0, palette_part_pt=8.0, saturation={"abs": 0.08}, luminance={"abs": 15},
                  ombre_delta_e=6.0, couleur_delta_e=6.0, durete={"rel": 0.30}, frequence={"rel": 0.20}, contraste={"abs": 6},
                  contour={"abs": 1}, flou={"rel": 0.25}, densite={"rel": 0.25}, nettete_sol={"abs": 1.0})
TOURS_MAX = 4

def _fmt(v, unite=""):
    if v is None:
        return "—"
    if isinstance(v, str):
        return f"`{v}`"
    return (f"{v:.3g} {unite}" if abs(v) < 100 else f"{v:.0f} {unite}").strip().replace(".", ",")

class Tableau:
    def __init__(s, dossier_ref, dossier_nous, tol):
        s.dref, s.dnous, s.tol, s.lignes, s._cache = pathlib.Path(dossier_ref), pathlib.Path(dossier_nous), tol, [], {}

    def charger(s, cote, ident):
        cle = (cote, ident)
        if cle not in s._cache:
            d = s.dref if cote == "ref" else s.dnous
            f = d / f"{ident}_decor.json"
            if not f.exists():
                raise FileNotFoundError(f"{f.name} absent de {d} (lancer mesurer_decor.py sur cette image)")
            s._cache[cle] = B.lire_json(f)
        return s._cache[cle]

    def valeur(s, cote, spec):
        """spec = [id, nom de mesure, clé] → (valeur, D de la mesure)."""
        js = s.charger(cote, spec[0])
        for m in js["mesures"]:
            if m["nom"] == spec[1]:
                if m["resultat"].get("erreur"):
                    raise KeyError(f"{spec[0]} : mesure « {spec[1]} » en erreur ({m['resultat']['erreur']})")
                return m["resultat"].get(spec[2]), m.get("D_px") or js.get("D_px")
        raise KeyError(f"{spec[0]} : mesure « {spec[1]} » absente")

    def chemin(s, cote, spec):
        """spec = [id, "densite.segments"] → valeur."""
        v = s.charger(cote, spec[0])
        for bout in str(spec[1]).split("."):
            v = v[int(bout)] if isinstance(v, list) else v[bout]
        return v

    def tolerance(s, t, defaut):
        t = defaut if t is None else t
        if isinstance(t, str):
            if t not in s.tol:
                raise KeyError(f"tolérance inconnue : {t} (connues : {', '.join(sorted(s.tol))})")
            t = s.tol[t]
        return t

    def _ajoute(s, famille, grandeur, ref, nous, ecart, tol, ok, note=""):
        s.lignes.append(dict(famille=famille, grandeur=grandeur, reference=ref, nous=nous, ecart=ecart, tolerance=tol,
                             verdict=None if ok is None else bool(ok), note=note))

    def nombre(s, famille, grandeur, ref, nous, tol, unite="", note=""):
        """ref et nous : nombres déjà à la même échelle. tol = {"abs": x} ou {"rel": x}."""
        if ref is None or nous is None:
            return s._ajoute(famille, grandeur, _fmt(ref, unite), _fmt(nous, unite), "—", "—", None, note or "mesure absente d'un côté")
        e = nous - ref
        if "abs" in tol:
            ok, t, ec = abs(e) <= tol["abs"], f"± {tol['abs']:g} {unite}".strip(), f"{e:+.3g} {unite}".strip()
        else:
            ok, t = abs(e) <= tol["rel"] * abs(ref), f"± {tol['rel'] * 100:.0f} %"
            ec = f"{100 * e / ref:+.0f} %" if ref else "—"
        s._ajoute(famille, grandeur, _fmt(ref, unite), _fmt(nous, unite), ec.replace(".", ","), t.replace(".", ","), ok, note)

    def mesure(s, l):
        fam, gr, note = l.get("famille", ""), l.get("grandeur", ""), l.get("note", "")
        tol = s.tolerance(l.get("tolerance"), {"abs": 1})
        try:
            vn, dn = s.valeur("nous", l["nous"])
            if isinstance(l["ref"], (int, float)):
                vr, dr, cle_r = float(l["ref"]), None, ""
            else:
                (vr, dr), cle_r = s.valeur("ref", l["ref"]), l["ref"][2]
        except (KeyError, FileNotFoundError, IndexError) as e:
            return s._ajoute(fam, gr, "—", "—", "—", "—", None, str(e).strip("'\""))
        en_D = l.get("en_D", str(cle_r).endswith("_px"))
        unite = l.get("unite", "px" if str(l["nous"][2]).endswith("_px") else "")
        if en_D and vr is not None:
            if dr and dn:
                note = (note + " ; " if note else "") + f"réf. {vr:.3g} px pour D = {dr:g}, soit {vr / dr:.3f} D ; nous D = {dn:g}"
                vr = vr / dr * dn
            elif not (dr is None and isinstance(l["ref"], (int, float))):
                note = (note + " ; " if note else "") + "D absent d'un côté : comparé en pixels bruts, à n'accepter que si les deux images sont à la même échelle"
        s.nombre(fam, gr, vr, vn, tol, unite, note)

    def globale(s, l):
        fam, gr = l.get("famille", ""), l.get("grandeur", "")
        tol = s.tolerance(l.get("tolerance"), {"rel": 0.25})
        try:
            vr = float(l["ref"]) if isinstance(l["ref"], (int, float)) else s.chemin("ref", l["ref"])
            vn = s.chemin("nous", l["nous"])
        except (KeyError, FileNotFoundError, IndexError, ValueError, TypeError) as e:
            return s._ajoute(fam, gr, "—", "—", "—", "—", None, str(e).strip("'\""))
        s.nombre(fam, gr, vr, vn, tol, l.get("unite", ""), l.get("note", ""))

    def couleur(s, l):
        fam, gr, note = l.get("famille", ""), l.get("grandeur", ""), l.get("note", "")
        tol = s.tolerance(l.get("tolerance"), "couleur_delta_e")
        tol = float(tol["abs"]) if isinstance(tol, dict) else float(tol)
        try:
            a = l["ref"] if isinstance(l["ref"], str) else s.valeur("ref", l["ref"])[0]
            b = l["nous"] if isinstance(l["nous"], str) else s.valeur("nous", l["nous"])[0]
        except (KeyError, FileNotFoundError, IndexError) as e:
            return s._ajoute(fam, gr, "—", "—", "—", "—", None, str(e).strip("'\""))
        if not a or not b:
            return s._ajoute(fam, gr, _fmt(a), _fmt(b), "—", "—", None, note or "mesure absente d'un côté")
        d = B.de2000(B.de_hexa(a), B.de_hexa(b))
        s._ajoute(fam, gr, f"`{a}`", f"`{b}`", f"ΔE {d:.1f}".replace(".", ","), f"ΔE < {tol:g}", d < tol, note)

    def _palette_de(s, cote, ids):
        js = [s.charger(cote, i) for i in sorted(ids)]              # ordre fixe : les k-moyennes dépendent de l'ordre des pixels
        bandes = {tuple(j["bande_exclue"]) if j.get("bande_exclue") else None for j in js}
        if len(js) == 1:
            dom = js[0]["palette"]["dominantes"]
        else:
            ims = []
            for j in js:
                im = B.lire(j["image_lue"])
                ims.append((im, j.get("bande_exclue")))
            px = np.concatenate([im[MD.masque_global(im.shape[0], im.shape[1], b)][::23] for im, b in ims])
            dom = MD._kmeans_palette(px, 10)
        moy = lambda cle: float(np.mean([j["palette"][cle] for j in js]))
        return dom, moy("saturation_moyenne"), moy("luminance_moyenne"), bandes

    def palette(s, l):
        fam, gr = l.get("famille", "Palette"), l.get("grandeur", "")
        try:
            pr, sr, lr, br = s._palette_de("ref", l["ref"])
            pn, sn, ln, bn = s._palette_de("nous", l["nous"])
        except (KeyError, FileNotFoundError, OSError, ValueError) as e:
            return s._ajoute(fam, f"Palette ({gr})", "—", "—", "—", "—", None, str(e).strip("'\""))
        tde, tpt = float(s.tol["palette_delta_e"]), float(s.tol["palette_part_pt"])
        note = "" if br == bn else "ATTENTION : la bande exclue n'est pas la même des deux côtés"
        for i, a in enumerate(MD.ecart_palettes(pr, pn), 1):
            ok = a["delta_e"] < tde and abs(a["ecart_part"]) <= tpt
            s._ajoute(fam, f"Dominante {i} ({gr})", f"`{a['ref']}` {a['part_ref']:.0f} %", f"`{a['nous']}` ; part des couleurs proches {a['part_nous_proches']:.0f} %",
                      f"ΔE {a['delta_e']:.1f} ; part {a['ecart_part']:+.0f} pt".replace(".", ","), f"ΔE < {tde:g} ; ± {tpt:g} pt", ok, note)
        s.nombre(fam, f"Saturation moyenne ({gr})", round(sr, 3), round(sn, 3), s.tolerance("saturation", None), "", "tolérance fixée lors de l'essai du studio")
        s.nombre(fam, f"Luminance moyenne ({gr})", round(lr, 1), round(ln, 1), s.tolerance("luminance", None), "", "tolérance fixée lors de l'essai du studio")

    def bilan(s):
        return (sum(1 for l in s.lignes if l["verdict"] is True), sum(1 for l in s.lignes if l["verdict"] is False),
                sum(1 for l in s.lignes if l["verdict"] is None))

    def ecrire(s, sortie, nom, titre):
        ok, ko, nc = s.bilan()
        t = [f"# {titre}", "", f"**{ok} grandeurs dans la tolérance, {ko} hors tolérance, {nc} non mesurées.**", "",
             "| Famille | Grandeur | Référence | Nous | Écart | Tolérance | Verdict | Remarque |", "|---|---|---|---|---|---|---|---|"]
        for l in s.lignes:
            v = "non mesuré" if l["verdict"] is None else "dans la tolérance" if l["verdict"] else "**hors tolérance**"
            t.append(f"| {l['famille']} | {l['grandeur']} | {l['reference']} | {l['nous']} | {l['ecart']} | {l['tolerance']} | {v} | {l['note']} |")
        fam = {}
        for l in s.lignes:
            f = fam.setdefault(l["famille"], [0, 0, 0])
            f[0 if l["verdict"] is True else 1 if l["verdict"] is False else 2] += 1
        t += ["", "Bilan par famille (dans la tolérance / hors / non mesuré) : " + " ; ".join(f"{k} {a} / {b} / {c}" for k, (a, b, c) in fam.items()) + ".", "",
              "Dans la colonne « Référence », une valeur en pixels est ramenée à notre échelle (le détail en D est dans la remarque)."]
        sortie = pathlib.Path(sortie); sortie.mkdir(parents=True, exist_ok=True)
        (sortie / f"{nom}.md").write_text("\n".join(t) + "\n", encoding="utf-8")
        (sortie / f"{nom}.json").write_text(json.dumps(dict(dans=ok, hors=ko, non_mesure=nc, par_famille=fam, lignes=s.lignes), indent=1, ensure_ascii=False), encoding="utf-8")
        return ok, ko, nc

def comparer(paires_path, sortie, dref=None, dnous=None, nom="controle_decor", tour=None):
    paires_path = pathlib.Path(paires_path)
    cfg = B.lire_json(paires_path)
    if not isinstance(cfg.get("lignes"), list) or not cfg["lignes"]:
        raise SystemExit(f"{paires_path} : il manque la liste \"lignes\" (voir gabarits/paires-decor.json)")
    tol = dict(TOLERANCES); tol.update(cfg.get("tolerances") or {})
    t = Tableau(dref or paires_path.parent, dnous or dref or paires_path.parent, tol)
    for i, l in enumerate(cfg["lignes"], 1):
        try:
            if "ref" not in l or "nous" not in l:
                raise KeyError("champs \"ref\" et \"nous\" obligatoires")
            {"palette": t.palette, "couleur": t.couleur, "global": t.globale, "mesure": t.mesure}[l.get("type", "mesure")](l)
        except (KeyError, ValueError, TypeError) as e:
            t._ajoute(l.get("famille", ""), l.get("grandeur", f"ligne {i}"), "—", "—", "—", "—", None, f"ligne {i} mal écrite : {str(e).strip(chr(39))}")
    titre = "Contrôle chiffré du décor" + (f" — tour {tour}" if tour is not None else "")
    ok, ko, nc = t.ecrire(sortie, nom, titre)
    if tour is not None:
        d = pathlib.Path(sortie) / "tours"; d.mkdir(exist_ok=True)
        (d / f"decor_tour{tour}.md").write_text((pathlib.Path(sortie) / f"{nom}.md").read_text(encoding="utf-8"), encoding="utf-8")
        f = d / "suivi_decor.json"
        suivi = B.lire_json(f) if f.exists() else {}
        suivi[str(tour)] = dict(dans=ok, hors=ko, non_mesure=nc)
        f.write_text(json.dumps(suivi, indent=1, ensure_ascii=False), encoding="utf-8")
        if int(tour) > TOURS_MAX:
            print(f"ATTENTION : tour {tour} ; la règle est de {TOURS_MAX} tours de correction au plus. Ce qui reste hors tolérance s'écrit dans le compte rendu, avec sa raison.")
    return t, (ok, ko, nc)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paires"); ap.add_argument("sortie")
    ap.add_argument("--ref", help="dossier des <id>_decor.json de la référence (défaut : celui du fichier de paires)")
    ap.add_argument("--nous", help="dossier des <id>_decor.json de nos images (défaut : comme --ref)")
    ap.add_argument("--nom", default="controle_decor")
    ap.add_argument("--tour", type=int)
    a = ap.parse_args()
    t, (ok, ko, nc) = comparer(a.paires, a.sortie, a.ref, a.nous, a.nom, a.tour)
    for l in t.lignes:
        v = "?   " if l["verdict"] is None else "ok  " if l["verdict"] else "HORS"
        print(f"  [{v}] {l['famille']} | {l['grandeur']} | réf {l['reference']} | nous {l['nous']} | {l['ecart']}" + (f" | {l['note'][:90]}" if l["verdict"] is None else ""))
    print(f"{ok} dans la tolérance, {ko} hors tolérance, {nc} non mesurée(s) → {pathlib.Path(a.sortie) / (a.nom + '.md')}")

if __name__ == "__main__":
    main()
