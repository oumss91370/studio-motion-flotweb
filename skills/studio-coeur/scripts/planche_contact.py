#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""planche_contact.py : les images à REGARDER avant de dire qu'un film est fini.

Usage :
    python3 planche_contact.py film.mp4 [dossier_de_sortie] [--bande 12.4] [--bande 18] [--colonnes 5]

Produit dans le dossier (par défaut `revue/` à côté du film) :
  - planche.jpg    : une image par seconde, 5 par ligne, 270 px de large. Vue d'ensemble : rythme, variété des
                     cadrages, plans qui se ressemblent, trous. La case n° k (en lisant ligne par ligne, à partir
                     de 0) est l'image du film à k secondes pile (0 s, 1 s, 2 s…) ; son temps est écrit dans son
                     coin. La fin du film (après la dernière seconde entière) n'y est pas : pour la voir,
                     ajouter une --bande sur la dernière seconde.
  - telephone.jpg  : les mêmes images à 360 px de large, la taille réelle sur un téléphone. Si un texte ou une
                     expression ne se lit pas ici, il ne se lit pas chez le spectateur.
  - bande-<t>.jpg  : avec --bande t, 12 images serrées (une tous les 1/15 s, de t − 0,4 s à t + 0,33 s) autour de
                     l'instant t, pour juger un mouvement rapide ou une transition (texte qui se chevauche, image
                     blanche, saut). L'option se répète : --bande 3.2 --bande 7 --bande 12.4 fait trois bandes.

Besoin : ffmpeg et ffprobe. Ce script ne juge rien : c'est à l'agent d'ouvrir les images et de les regarder.

Inspiration : boucle de critique de claude-motion-design (Howseen AI, MIT, commit 3d90d34) et `phone.jpg`
d'animate (cth9191, MIT, commit 7e5eb56). Réécrit.
"""
import math
import subprocess
import sys
from pathlib import Path


def duree(film):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", str(film)]).strip())


def lancer(cmd_sans_etiquette, filtre, etiquette, sortie):
    """Lance ffmpeg avec l'étiquette de temps ; si l'écriture de texte est impossible (pas de police), sans."""
    for f in ([filtre.replace("@ETIQ@", etiquette)] if etiquette else []) + [filtre.replace("@ETIQ@", "")]:
        r = subprocess.run(cmd_sans_etiquette + ["-vf", f, "-frames:v", "1", "-q:v", "3", str(sortie)],
                           capture_output=True, text=True)
        if r.returncode == 0 and Path(sortie).exists():
            return bool(etiquette) and "drawtext" in f
    raise subprocess.CalledProcessError(r.returncode, "ffmpeg", stderr=r.stderr)


def etiquette(taille, decalage=0.0, decimales=0):
    """Le temps de l'image, écrit en bas à gauche de la case (blanc sur bandeau noir)."""
    temps = "%{eif\\:t\\:d} s" if not decimales else f"%{{eif\\:(t+{decalage:.3f})*100\\:d}} cs"
    return (f",drawtext=text='{temps}':fontsize={taille}:fontcolor=white:box=1:boxcolor=black@0.75:boxborderw=5:"
            "x=6:y=h-th-8")


def planche(film, sortie, largeur, colonnes, cases):
    """Une image par seconde pile. `fps=1:round=up` garde, pour la case k, l'image dont le temps est k s
    (l'arrondi par défaut gardait la dernière image avant k + 0,5 s : la case k montrait k + 0,5 s)."""
    lignes = max(1, math.ceil(cases / colonnes))
    filtre = (f"fps=1:round=up,scale={largeur}:-2@ETIQ@,"
              f"tile={colonnes}x{lignes}:padding=6:margin=6:color=white")
    return lancer(["ffmpeg", "-y", "-v", "error", "-i", str(film)], filtre, etiquette(max(16, largeur // 11)), sortie)


def bande(film, sortie, t):
    depart = max(0.0, t - 0.4)
    filtre = "fps=15:round=up,scale=240:-2@ETIQ@,tile=12x1:padding=4:color=white"
    lancer(["ffmpeg", "-y", "-v", "error", "-ss", f"{depart:.3f}", "-i", str(film)], filtre,
           etiquette(20, depart, 2), sortie)
    return depart


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 1
    film = Path(args[0])
    avec_valeur = ("--bande", "--colonnes")
    positionnels = [a for i, a in enumerate(args[1:], 1) if not a.startswith("--") and args[i - 1] not in avec_valeur]
    dossier = Path(positionnels[0]) if positionnels else film.parent / "revue"
    dossier.mkdir(parents=True, exist_ok=True)
    try:
        colonnes = int(args[args.index("--colonnes") + 1]) if "--colonnes" in args else 5
        bandes = [float(args[i + 1].replace(",", ".")) for i, a in enumerate(args) if a == "--bande"]
        d = duree(film)
        cases = max(1, math.floor(d - 0.02) + 1)                        # images à 0 s, 1 s … dernière seconde entière
        numerote = planche(film, dossier / "planche.jpg", 270, colonnes, cases)
        planche(film, dossier / "telephone.jpg", 360, colonnes, cases)
        print(f"{dossier / 'planche.jpg'}   ({cases} images, {colonnes} par ligne, case k = image à k s pile, "
              f"film de {d:.2f} s"
              + ("" if numerote else " ; temps non écrits sur les cases : ffmpeg sans police") + ")")
        print(f"{dossier / 'telephone.jpg'} (taille réelle sur téléphone : tout texte utile doit s'y lire)")
        for t in bandes:
            nom = dossier / f"bande-{t:g}.jpg"
            depart = bande(film, nom, t)
            print(f"{nom}   (12 images, une tous les 1/15 s, de {depart:.2f} s à {depart + 11 / 15:.2f} s ; "
                  "temps écrits en centièmes de seconde)")
    except (OSError, subprocess.CalledProcessError, ValueError, IndexError) as e:
        print(f"Impossible de faire la planche : {e}" + (f"\n{e.stderr.strip()[-300:]}" if getattr(e, "stderr", None) else ""))
        return 1
    print("À faire maintenant : ouvrir ces images et les regarder. Une planche non regardée ne compte pas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
