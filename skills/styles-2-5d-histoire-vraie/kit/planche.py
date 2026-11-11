"""Assemble des images en une planche de contrôle (le nom de chaque fichier est écrit sous sa vignette).

  python outils/planche.py <sortie.jpg> <colonnes> <largeur de vignette> <image1> <image2> …
  python outils/planche.py revue/plans.jpg 6 270 revue/tmp/p*.jpg        (les jokers sont développés, y compris sous Windows)
"""
import glob, pathlib, sys
from PIL import Image, ImageDraw, ImageFont


def planche(sortie, colonnes, largeur, fichiers):
    fichiers = [pathlib.Path(p) for p in fichiers]
    if not fichiers:
        raise SystemExit("aucune image à assembler")
    ims = [Image.open(p).convert("RGB") for p in fichiers]
    th = round(largeur * ims[0].height / ims[0].width)
    lignes = (len(ims) + colonnes - 1) // colonnes
    bande = 26
    feuille = Image.new("RGB", (colonnes * largeur, lignes * (th + bande)), (18, 18, 18))
    police = ImageFont.load_default()
    for nom in ("DejaVuSans-Bold.ttf", "arialbd.ttf", "Arial Bold.ttf"):
        try:
            police = ImageFont.truetype(nom, 16)
            break
        except OSError:
            pass
    d = ImageDraw.Draw(feuille)
    for i, (p, im) in enumerate(zip(fichiers, ims)):
        x, y = (i % colonnes) * largeur, (i // colonnes) * (th + bande)
        feuille.paste(im.resize((largeur, th), Image.LANCZOS), (x, y))
        d.text((x + 6, y + th + 4), p.stem, fill=(235, 235, 235), font=police)
    pathlib.Path(sortie).parent.mkdir(parents=True, exist_ok=True)
    feuille.save(sortie, quality=90)
    return feuille.size


if __name__ == "__main__":
    if len(sys.argv) < 5:
        raise SystemExit(__doc__)
    fichiers = []
    for motif in sys.argv[4:]:
        fichiers += sorted(glob.glob(motif)) or [motif]
    print(sys.argv[1], planche(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), fichiers))
