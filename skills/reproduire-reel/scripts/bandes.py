#!/usr/bin/env python3
"""Bandes de lecture continue : TOUTES les images consécutives d'un passage, en planches numérotées, pour lire le mouvement
image par image (anticipation, durée des gestes, tenues, changements en une image, clignements, caméra, effets).

  python bandes.py <video> <sortie.jpg> <début> <fin> [--pas 1] [--cols 8] [--larg 216] [--crop x,y,w,h] [--max 48]
  python bandes.py <video> <sortie.jpg> --plans <plans.json> --plan P03 [mêmes options]
      début, fin : numéros d'image (à partir de 0, fin incluse) ; --plan : prend les bornes du plan dans plans.json (decouper.py)
      --crop : recadrage en pixels de la source avant réduction (pour suivre un visage, une main) ; mettre alors --larg plus grand
      --max  : nombre d'images par planche ; au-delà, écrit sortie-1.jpg, sortie-2.jpg…
Chaque vignette porte son numéro d'image et son instant. On ne saute aucune image : --pas reste à 1 là où ça joue.
Dépendances : Python 3.9+, Pillow, numpy, FFmpeg. Écrit par Flot Web.
"""
import sys
sys.dont_write_bytecode = True
import argparse, json, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import mp_base as B

def bandes(video, sortie, debut, fin, pas=1, cols=8, larg=216, crop=None, maxi=48):
    inf = B.infos_video(video)
    if inf.get("images_exactes"):
        fin = min(fin, inf["images"] - 1)
    nums = list(range(debut, fin + 1, pas))
    ims = B.lire_images(video, nums, larg=larg, crop=crop)
    nums = [n for n in nums if n in ims]
    if not nums:
        sys.exit("aucune image extraite : vérifier les numéros")
    sur = inf.get("images_exactes") and not inf.get("cadence_variable")        # sinon l'instant en secondes serait faux : on n'écrit que le numéro
    if not sur:
        print("cadence variable ou nombre d'images non annoncé par le fichier : les vignettes portent le numéro d'image, sans l'instant en secondes")
    vign = [B.etiquette(ims[n], f"i{n}  {n / inf['ips']:.2f}s" if sur else f"i{n}") for n in nums]
    lots = [vign[i:i + maxi] for i in range(0, len(vign), maxi)]
    sortie = pathlib.Path(sortie); sortie.parent.mkdir(parents=True, exist_ok=True)
    ecrits = []
    for k, lot in enumerate(lots):
        nom = sortie if len(lots) == 1 else sortie.with_name(f"{sortie.stem}-{k + 1}{sortie.suffix}")
        B.mosaique(lot, cols).save(nom, quality=88)
        ecrits.append((str(nom), len(lot), nums[k * maxi], nums[min(len(nums), (k + 1) * maxi) - 1]))
    return ecrits

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("video"); p.add_argument("sortie")
    p.add_argument("debut", type=int, nargs="?"); p.add_argument("fin", type=int, nargs="?")
    p.add_argument("--plans"); p.add_argument("--plan")
    p.add_argument("--pas", type=int, default=1); p.add_argument("--cols", type=int, default=8)
    p.add_argument("--larg", type=int, default=216); p.add_argument("--crop"); p.add_argument("--max", type=int, default=48)
    a = p.parse_args()
    if a.plans and a.plan:
        pl = {x["id"]: x for x in json.loads(pathlib.Path(a.plans).read_text(encoding="utf-8-sig"))["plans"]}
        if a.plan not in pl:
            p.error(f"plan {a.plan} absent de {a.plans} (plans : {', '.join(pl)})")
        a.debut, a.fin = pl[a.plan]["debut"], pl[a.plan]["fin"]
    if a.debut is None or a.fin is None:
        p.error("donner début et fin, ou --plans et --plan")
    crop = [int(v) for v in a.crop.split(",")] if a.crop else None
    for nom, n, d, f in bandes(a.video, a.sortie, a.debut, a.fin, a.pas, a.cols, a.larg, crop, a.max):
        print(f"{nom} : {n} images (i{d} à i{f})")
