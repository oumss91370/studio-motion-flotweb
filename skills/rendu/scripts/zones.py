#!/usr/bin/env python3
"""Dessine les zones d'interface sur une capture 1080x1920 pour contrôle visuel (ffmpeg, Python standard).

Usage :
  python3 zones.py capture.png [-o capture-zones.png]
  python3 zones.py video.mp4 --a 0 [-o image0-zones.png]     # une image de la vidéo à l'instant --a (secondes)

Voile rouge translucide (30 %) : zones où rien d'important ne doit se trouver (haut 160 px, bas 360 px, droite 135 px).
L'image reste lisible sous le voile, que la source soit une capture PNG ou une image tirée du MP4.
Cadre vert : zone utile (x 60 à 945, y 160 à 1560). Trait jaune : y = 1330 (texte indispensable de préférence au-dessus).
Valeurs : table de référence de references/zones-interface.md (les mêmes que la porte de livraison de studio-coeur).
L'image produite sert seulement au contrôle : ne jamais dessiner ces guides dans la composition.
"""
import sys
sys.dont_write_bytecode = True
import argparse, os, subprocess

HAUT, BAS, DROITE = 160, 360, 135
VOILE = 0.30   # opacité du rouge
TX0, TX1, TY0, TY1 = 60, 945, 160, 1560
Y_CONSEIL = 1330


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source"); ap.add_argument("-o", "--out")
    ap.add_argument("--a", type=float, default=None, help="instant en secondes si la source est une vidéo")
    o = ap.parse_args()
    out = o.out or os.path.splitext(o.source)[0] + "-zones.png"
    # tout est exprimé en proportion de 1080x1920 pour accepter une capture à une autre échelle
    fx, fy = "iw/1080", "ih/1920"
    vf = ",".join([
        # passage en RVB d'abord : sur une image YUV (tirée d'un MP4), drawbox remplace la couleur au lieu de la
        # mélanger et le rouge sort presque opaque
        "format=rgb24",
        f"drawbox=x=0:y=0:w=iw:h={HAUT}*{fy}:color=red@{VOILE}:t=fill",
        f"drawbox=x=0:y=ih-{BAS}*{fy}:w=iw:h={BAS}*{fy}:color=red@{VOILE}:t=fill",
        f"drawbox=x=iw-{DROITE}*{fx}:y={HAUT}*{fy}:w={DROITE}*{fx}:h=ih-{HAUT + BAS}*{fy}:color=red@{VOILE}:t=fill",
        f"drawbox=x={TX0}*{fx}:y={TY0}*{fy}:w={TX1 - TX0}*{fx}:h={TY1 - TY0}*{fy}:color=lime@0.9:t=4",
        f"drawbox=x={TX0}*{fx}:y={Y_CONSEIL}*{fy}:w={TX1 - TX0}*{fx}:h=3:color=yellow@0.9:t=fill",
    ])
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
    if o.a is not None:
        cmd += ["-ss", str(o.a)]
    cmd += ["-i", o.source, "-frames:v", "1", "-vf", vf, out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("ffmpeg a échoué : " + r.stderr.strip())
    print("Écrit :", out, "- l'ouvrir et vérifier qu'aucun mot ni élément clé ne touche le rouge.")


if __name__ == "__main__":
    main()
