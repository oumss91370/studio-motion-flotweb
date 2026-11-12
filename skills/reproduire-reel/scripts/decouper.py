#!/usr/bin/env python3
"""Découpage d'une vidéo de référence en plans : bornes en numéros d'image, une image nette par plan, planche numérotée,
et de quoi VÉRIFIER chaque borne à l'image.

  python decouper.py <video> <dossier>                                première passe automatique
  python decouper.py <video> <dossier> --bornes 24:fondu,33,84:filé   bornes corrigées à la main : numéro de la PREMIÈRE image
                                                                      de chaque plan, suivi si on veut de « :type de transition »
  python decouper.py <video> <dossier> --plans plans.json             repart d'un plans.json retouché (champs debut, entree, note)
      --mini 6        durée minimale d'un plan, en images (deux bornes plus proches sont fusionnées)
      --larg 270      largeur des vignettes de la planche
      --sans-images   n'extrait pas l'image nette pleine résolution de chaque plan

Comment il coupe. Le mouvement est mesuré entre chaque image et la précédente (différence moyenne, vidéo réduite à 96 px).
  - « coupe »     : un pic isolé d'une image, avec un changement net de la répartition des gris ;
  - « saut »      : le même pic sans changement des gris (saut de cadre, flash, geste brusque) ;
  - « mouvement » : au moins 4 images de suite de fort mouvement (panoramique filé, zoom, geste ample). Ce N'EST PAS forcément un
                    changement de plan ;
  - « fondu »     : l'image change beaucoup en 12 images alors que chaque image diffère peu de la précédente (fondu enchaîné).
Toutes les bornes sauf les coupes franches sont marquées « à vérifier ».

Ce que le script NE voit PAS : un fondu de 2 à 4 images, une transition entre deux plans de même palette, un fondu noyé dans
un geste. Un film peut aussi être un quasi plan-séquence relié par des déplacements de caméra. Donc, toujours :
  1. ouvrir `survol-N.jpg` (tout le film, une image sur six) et chercher les changements de décor SANS borne ;
  2. ouvrir `bornes-a-verifier-N.jpg` (4 images avant, 4 après chaque borne) et trancher chaque borne ;
  3. relancer avec --bornes. Les numéros d'image sont ceux de bandes.py et d'extraire.py (à partir de 0).

Sorties dans <dossier> : plans.json, plans.md, planche-plans.jpg, survol-N.jpg, bornes-a-verifier-N.jpg, mouvement.png,
mouvement.csv, plans/Pxx_iNNNN.png (image nette pleine résolution de chaque plan ; celles d'une passe précédente sont
déplacées dans plans/_passe-precedente/).
Dépendances : Python 3.9+, numpy, Pillow, FFmpeg (ffmpeg et ffprobe). Écrit par Flot Web.
"""
import sys
sys.dont_write_bytecode = True
import argparse, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import numpy as np
from PIL import Image, ImageDraw
import mp_base as B

K_LENT = 6            # un fondu se cherche en comparant l'image i − 6 à l'image i + 6
PRIORITE = {"coupe": 0, "fondu": 1, "saut": 2, "mouvement": 3}

def mouvement(video):
    """Par image : d = différence moyenne avec la précédente ; h = changement de la répartition des gris (0 à 1) ;
    dk = différence entre l'image i − 6 et l'image i + 6 ; r = dk / plus forte différence image à image sur ces 12 images."""
    g = B.lire_gris(video)
    n = len(g)
    d = np.zeros(n); h = np.zeros(n); dk = np.zeros(n); r = np.zeros(n)
    hist = np.stack([np.bincount(f.ravel() >> 3, minlength=32) for f in g]).astype(np.float64)
    hist /= np.maximum(hist.sum(1, keepdims=True), 1)
    gi = g.astype(np.int16)
    for i in range(1, n):
        d[i] = np.abs(gi[i] - gi[i - 1]).mean()
        h[i] = 1.0 - np.minimum(hist[i], hist[i - 1]).sum()
    K = K_LENT
    for i in range(K, n - K):
        dk[i] = np.abs(gi[i + K] - gi[i - K]).mean()
        r[i] = dk[i] / max(float(d[i - K + 1:i + K + 1].max()), 0.5)
    return d, h, dk, r

def detecter(d, h, dk, r, mini=6):
    """Bornes candidates : [(image, type, à vérifier, note)]."""
    n = len(d)
    med = float(np.median(d[1:])) if n > 1 else 0.0
    bornes = []
    for i in range(1, n):                              # coupes et sauts : pic isolé
        v = np.r_[d[max(1, i - 6):i], d[i + 1:i + 7]]
        local = float(np.median(v)) if len(v) else 0.0
        voisins = max(d[i - 1] if i > 1 else 0.0, d[i + 1] if i + 1 < n else 0.0)
        if d[i] >= max(10.0, 4.0 * local) and d[i] >= 2.5 * voisins:
            franche = h[i] >= 0.35
            bornes.append((i, "coupe" if franche else "saut", not franche,
                           f"pic de mouvement {d[i]:.1f} (voisines {voisins:.1f}), changement des gris {h[i]:.2f}"))
    lent = (dk >= 30.0) & (r >= 4.0)                   # fondus enchaînés : grand changement en 12 images, petit d'une image à l'autre
    i = 0
    while i < n:
        if lent[i]:
            j = i
            while j + 1 < n and (lent[j + 1] or (j + 2 < n and lent[j + 2]) or (j + 3 < n and lent[j + 3])):
                j += 1
            k = i + int(np.argmax(r[i:j + 1]))
            bornes.append((k, "fondu", True, f"changement lent autour des images {i} à {j} : {dk[k]:.0f} en 12 images pour {dk[k] / r[k]:.1f} au plus d'une image à l'autre "
                                             "(fondu enchaîné probable)"))
            i = j + 1
        else:
            i += 1
    seuil = max(6.0, 3.0 * med)                        # mouvements rapides : au moins 4 images de suite (un trou d'une image toléré)
    fort = d >= seuil
    i = 1
    while i < n:
        if fort[i]:
            j = i
            while j + 1 < n and (fort[j + 1] or (j + 2 < n and fort[j + 2])):
                j += 1
            if j - i + 1 >= 4:
                k = i + int(np.argmax(d[i:j + 1]))
                if not any(abs(k - b[0]) <= 2 for b in bornes):
                    bornes.append((k, "mouvement", True, f"mouvement fort de l'image {i} à {j} ({j - i + 1} images, maximum {d[k]:.1f}) : déplacement de caméra, zoom, "
                                                         "geste ample ou fondu rapide"))
            i = j + 1
        else:
            i += 1
    bornes.sort()
    out = []
    for b in bornes:                                   # fusion des bornes trop proches : la coupe l'emporte, puis le fondu
        if b[0] < mini or b[0] > n - mini:
            continue
        if out and b[0] - out[-1][0] < mini:
            if PRIORITE[b[1]] < PRIORITE[out[-1][1]]:
                out[-1] = b
            continue
        out.append(b)
    return out, dict(mediane=round(med, 2), seuil_mouvement=round(seuil, 2), fondu="dk >= 30 et dk / max(d) >= 4 sur 12 images")

def plans_depuis_bornes(bornes, n, d, ips):
    """bornes : [(image de début, type, à vérifier, note)] sans le 0. Renvoie la liste des plans."""
    debuts = [(0, "début du film", False, "")] + list(bornes)
    plans = []
    for k, (a, typ, verif, note) in enumerate(debuts):
        b = (debuts[k + 1][0] - 1) if k + 1 < len(debuts) else n - 1
        if b - a >= 3:
            cout = d[a + 1:b] + d[a + 2:b + 1]             # mouvement avant + après chaque image intérieure
            nette = a + 1 + int(np.argmin(cout))
        else:
            nette = (a + b) // 2
        plans.append(dict(id=f"P{k + 1:02d}", debut=int(a), fin=int(b), images=int(b - a + 1), duree_s=round((b - a + 1) / ips, 3),
                          debut_s=round(a / ips, 3), entree=typ, a_verifier=bool(verif), note=note, image_nette=int(nette),
                          mouvement_moyen=round(float(d[a + 1:b + 1].mean()), 2) if b > a else 0.0,
                          part_figee=round(float((d[a + 1:b + 1] < 1.0).mean()), 2) if b > a else 1.0))
    return plans

def _planches(rangs, dossier, nom, par=6):
    """Empile des rangées d'images en planches <nom>-N.jpg ; met de côté les planches en trop d'une passe précédente."""
    nb = 0
    for k in range(0, len(rangs), par):
        lot = rangs[k:k + par]
        w = max(r.width for r in lot)
        out = Image.new("RGB", (w, sum(r.height for r in lot)), (24, 24, 24)); y = 0
        for r in lot:
            out.paste(r, (0, y)); y += r.height
        nb += 1
        out.save(dossier / f"{nom}-{nb}.jpg", quality=86)
    for vieux in dossier.glob(f"{nom}-*.jpg"):
        num = vieux.stem.rsplit("-", 1)[1]
        if num.isdigit() and int(num) > nb:
            vieux.replace(vieux.with_name(vieux.stem + ".ancien.jpg"))
    return nb

def ecrire(video, dossier, plans, sig, inf, seuils, larg=270, images=True, origine="automatique"):
    d, h, dk, r = sig
    dossier = pathlib.Path(dossier); dossier.mkdir(parents=True, exist_ok=True)
    n = len(d); ips = inf["ips"]
    compte = {}
    for p in plans[1:]:
        compte[p["entree"]] = compte.get(p["entree"], 0) + 1
    nb_coupes = compte.get("coupe", 0)
    avert = []
    if inf.get("cadence_variable"):
        avert.append(f"Cadence variable ou mal annoncée par le fichier : les durées en secondes sont calculées à la cadence moyenne réelle ({inf['ips']} i/s) "
                     "et restent approximatives ; les numéros d'image font foi.")
    if inf.get("rotation"):
        avert.append(f"Vidéo enregistrée avec une rotation de {inf['rotation']}° : les images sont lues redressées ({inf['largeur']} × {inf['hauteur']}).")
    if origine == "automatique":
        if inf["duree_s"] >= 8 and nb_coupes <= inf["duree_s"] / 8:
            avert.append(f"Peu de coupes franches ({nb_coupes} en {inf['duree_s']:.0f} s) : ce film est peut-être un quasi plan-séquence relié par des déplacements "
                         "de caméra et des fondus. Découper alors par STATIONS (une tenue de caméra, puis ce qui mène à la suivante).")
        avert.append("Le détecteur ne voit pas tout (fondu de 2 à 4 images, transition entre deux plans de même palette) : ouvrir survol-N.jpg et chercher "
                     "les changements de décor sans borne, puis bornes-a-verifier-N.jpg pour trancher chaque borne, et relancer avec --bornes.")
    data = dict(video=pathlib.Path(video).name, infos=inf, origine=origine, seuils=seuils, avertissements=avert, plans=plans)
    (dossier / "plans.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    detail = ", ".join(f"{v} × {k}" for k, v in sorted(compte.items())) or "aucune borne"
    md = [f"# Plans de {pathlib.Path(video).name}", "",
          f"{inf['largeur']}×{inf['hauteur']}, {inf['ips']} i/s, {inf['images']} images, {inf['duree_s']} s. Découpage {origine} : {len(plans)} plans. Entrées : {detail}.", ""]
    md += [f"> {a}" for a in avert] + ([""] if avert else [])
    md += ["| Plan | Images | Durée | Entrée (transition) | À vérifier | Image nette | Mouvement moyen | Part figée | Note |", "|---|---|---|---|---|---|---|---|---|"]
    for p in plans:
        md.append(f"| {p['id']} | {p['debut']}–{p['fin']} ({p['images']}) | {p['duree_s']:.2f} s | {p['entree']} | {'oui' if p['a_verifier'] else ''} | "
                  f"i{p['image_nette']} | {p['mouvement_moyen']} | {int(100 * p['part_figee'])} % | {p['note']} |")
    durees = [p["duree_s"] for p in plans]
    md += ["", f"Durée des plans : médiane {np.median(durees):.2f} s, de {min(durees):.2f} à {max(durees):.2f} s.",
           "", "« Entrée » est la transition par laquelle on ENTRE dans le plan. « Part figée » : part des images qui ne diffèrent presque pas de la précédente."]
    (dossier / "plans.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    with open(dossier / "mouvement.csv", "w", encoding="utf-8") as f:
        f.write("image;instant_s;mouvement;changement_gris;changement_sur_12_images;rapport_lent\n")
        for i in range(n):
            f.write(f"{i};{i / ips:.3f};{d[i]:.3f};{h[i]:.4f};{dk[i]:.2f};{r[i]:.2f}\n")
    fig = B.courbe([("mouvement (différence moyenne avec l'image précédente)", np.arange(n), d, (31, 119, 180))], "mouvement = f(image)", "numéro d'image", "niv.",
                   taille=(1600, 420), xlim=(0, max(n - 1, 1)), ylim=(0, max(12.0, float(np.percentile(d, 99.5)) * 1.2)))
    dr = ImageDraw.Draw(fig); ml, mr, mt, mb = 62, 16, 34, 46
    for p in plans[1:]:
        x = ml + p["debut"] / max(n - 1, 1) * (fig.width - ml - mr)
        dr.line((x, mt, x, fig.height - mb), fill=(214, 39, 40) if p["entree"] == "coupe" else (255, 140, 0), width=1)
        dr.text((x + 2, mt + 2), p["id"], fill=(120, 40, 40), font=B.police(11))
    fig.save(dossier / "mouvement.png")
    # planche des plans : l'image nette de chaque plan
    nettes = sorted(set(p["image_nette"] for p in plans))
    vign = B.lire_images(video, nettes, larg=larg)
    cases = []
    for p in plans:
        if p["image_nette"] not in vign:
            continue
        c = B.etiquette(vign[p["image_nette"]], f"{p['id']} i{p['debut']}–{p['fin']} {p['duree_s']:.2f}s", t=13, haut=36)
        ImageDraw.Draw(c).text((3, 18), f"net i{p['image_nette']} · {p['entree']}" + (" · À VÉRIFIER" if p["a_verifier"] else ""),
                               fill=(255, 190, 90) if p["a_verifier"] else (190, 190, 190), font=B.police(12))
        cases.append(c)
    lots = [cases[i:i + 40] for i in range(0, len(cases), 40)]
    for k, lot in enumerate(lots):
        B.mosaique(lot, 8).save(dossier / ("planche-plans.jpg" if len(lots) == 1 else f"planche-plans-{k + 1}.jpg"), quality=88)
    # survol : tout le film, une image sur six environ, le début de chaque plan encadré
    pas = max(1, int(round(ips / 5)))
    nums = list(range(0, n, pas))
    sv = B.lire_images(video, nums, larg=132)
    debut_de = {}
    for p in plans[1:]:
        debut_de[min(nums, key=lambda x: abs(x - p["debut"]))] = p
    rangs, ligne = [], []
    for i in nums:
        if i not in sv:
            continue
        p = debut_de.get(i)
        im = B.etiquette(sv[i], f"i{i}" + (f" {p['id']}" if p else ""), t=12, haut=17, fond=(110, 40, 40) if p else (24, 24, 24))
        ligne.append(im)
        if len(ligne) == 12:
            rangs.append(B.mosaique(ligne, 12, marge=2)); ligne = []
    if ligne:
        rangs.append(B.mosaique(ligne, 12, marge=2))
    nb_survol = _planches(rangs, dossier, "survol", par=4)
    # bandes autour des bornes : 4 images avant, 4 après
    bornes = plans[1:]
    veux = sorted(set(i for p in bornes for i in range(p["debut"] - 4, p["debut"] + 4) if 0 <= i < n))
    autour = B.lire_images(video, veux, larg=200) if veux else {}
    rangs = []
    for p in bornes:
        ims = []
        for i in range(p["debut"] - 4, p["debut"] + 4):
            if i in autour:
                im = B.etiquette(autour[i], f"i{i}" + ("  ◄ début " + p["id"] if i == p["debut"] else ""), t=13)
                if i == p["debut"]:
                    ImageDraw.Draw(im).rectangle((0, 0, im.width - 1, im.height - 1), outline=(255, 60, 60), width=3)
                ims.append(im)
        if ims:
            rang = B.mosaique(ims, len(ims))
            rangs.append(B.etiquette(rang, f"{p['id']} commence à i{p['debut']} · {p['entree']} · {p['note']}", t=13, haut=20, fond=(60, 30, 30) if p["a_verifier"] else (24, 24, 24)))
    nb_bornes = _planches(rangs, dossier, "bornes-a-verifier", par=6)
    if images:
        dp = dossier / "plans"; dp.mkdir(exist_ok=True)
        vieux = list(dp.glob("P*_i*.png"))
        if vieux:                                           # images d'une passe précédente : mises de côté, pas supprimées
            (dp / "_passe-precedente").mkdir(exist_ok=True)
            for f in vieux:
                f.replace(dp / "_passe-precedente" / f.name)
        plein = B.lire_images(video, nettes)
        for p in plans:
            if p["image_nette"] in plein:
                plein[p["image_nette"]].save(dp / f"{p['id']}_i{p['image_nette']:04d}.png")
    return data, compte, nb_survol, nb_bornes

def lire_bornes(texte, auto):
    """« 24:fondu,33,84:filé » -> [(image, type, à vérifier, note)]. Sans type : celui du détecteur s'il a vu cette borne."""
    vus = {b[0]: b for b in auto}
    out = {}
    for bout in texte.split(","):
        bout = bout.strip()
        if not bout:
            continue
        num, _, typ = bout.partition(":")
        x = int(num)
        if x <= 0:
            continue
        proche = next((vus[k] for k in vus if abs(k - x) <= 2), None)
        if typ.strip():
            out[x] = (x, typ.strip(), False, "type donné à la main" + (f" ; détecteur : {proche[1]}" if proche else " ; non vue par le détecteur"))
        elif proche:
            out[x] = (x, proche[1], False, proche[3] + " ; borne confirmée à la main")
        else:
            out[x] = (x, "posée à la main (type à préciser)", False, "non vue par le détecteur")
    return [out[k] for k in sorted(out)]

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("video"); ap.add_argument("dossier")
    ap.add_argument("--bornes"); ap.add_argument("--plans")
    ap.add_argument("--mini", type=int, default=6); ap.add_argument("--larg", type=int, default=270)
    ap.add_argument("--sans-images", action="store_true")
    a = ap.parse_args()
    inf = B.infos_video(a.video)
    sig = mouvement(a.video)
    d = sig[0]
    inf["images"] = int(len(d)); inf["images_exactes"] = True         # le nombre d'images réellement décodées fait foi
    if inf["duree_s"] > 0:
        reelle = len(d) / inf["duree_s"]                    # cadence réelle : les durées en secondes en dépendent
        if abs(reelle - inf["ips"]) > 0.02 * inf["ips"]:
            inf["ips_annoncee"] = inf["ips"]; inf["cadence_variable"] = True
            inf["ips"] = round(reelle, 3)
    auto, seuils = detecter(*sig, a.mini)
    if a.bornes:
        bornes, origine = lire_bornes(a.bornes, auto), "corrigé à la main"
    elif a.plans:
        vieux = json.loads(pathlib.Path(a.plans).read_text(encoding="utf-8-sig"))["plans"]
        bornes = [(int(p["debut"]), p.get("entree", "posée à la main"), bool(p.get("a_verifier", False)), p.get("note", "")) for p in vieux if int(p["debut"]) > 0]
        origine = "repris d'un plans.json retouché"
    else:
        bornes, origine = auto, "automatique"
    plans = plans_depuis_bornes(bornes, len(d), d, inf["ips"])
    data, compte, nb_survol, nb_bornes = ecrire(a.video, a.dossier, plans, sig, inf, seuils, a.larg, not a.sans_images, origine)
    detail = ", ".join(f"{v} × {k}" for k, v in sorted(compte.items())) or "aucune borne"
    print(f"{len(plans)} plans ({origine}). Entrées : {detail}.")
    if origine == "automatique" and nb_bornes == 0:
        print(f"Aucune borne proposée : chercher les transitions à l'œil dans survol-1 à {nb_survol}.jpg.")
    elif origine == "automatique":
        print(f"{sum(1 for p in plans if p['a_verifier'])} bornes à vérifier à l'image dans bornes-a-verifier-1 à {nb_bornes}.jpg ; "
              f"chercher aussi les transitions NON détectées dans survol-1 à {nb_survol}.jpg.")
    else:
        print(f"Planches réécrites pour contrôle : bornes-a-verifier-1 à {nb_bornes}.jpg (regarder que chaque borne tombe au bon endroit), survol-1 à {nb_survol}.jpg.")
    for av in data["avertissements"]:
        print("ATTENTION :", av)
    print(f"écrit dans {a.dossier} : plans.json, plans.md, planche-plans.jpg, survol-N.jpg, bornes-a-verifier-N.jpg, mouvement.png, mouvement.csv"
          + ("" if a.sans_images else ", plans/"))

if __name__ == "__main__":
    main()
