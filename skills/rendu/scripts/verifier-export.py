#!/usr/bin/env python3
"""Contrôle d'un fichier vidéo avant publication (ffprobe + ffmpeg, Python standard).

Usage :
  python3 verifier-export.py video.mp4 --format reel [--duree 18.0] [--sans-fond | --muet] [--lufs -14] [--json]

Formats : reel (Instagram), tiktok, short (YouTube Shorts) = 1080x1920 ;
          youtube = 1920x1080 ; youtube-1440p = 2560x1440 ; youtube-4k = 3840x2160.
Sortie : une ligne par contrôle (OK / ATTENTION / ECHEC), puis un feu :
          VERT (tout est OK), JAUNE (au moins une ATTENTION : livrable, à écrire dans la note de livraison),
          ROUGE (au moins un ECHEC : code de sortie 1).
Rien n'est modifié : le script ne fait que mesurer.

MESURE DU SON : la même que skills/son/scripts/niveau.py (la seule méthode du studio)
    ffmpeg -hide_banner -nostats -i <fichier> -map 0:a:0 -af ebur128=peak=true -f null -
  puis lecture du bloc « Summary » : « I: » = niveau intégré (LUFS), « LRA: » = plage dynamique (LU),
  « Peak: » = crête vraie (dBTP). On ne mesure PAS avec loudnorm=print_format=json : sur un film de 10 s il
  s'écarte jusqu'à 0,8 LU de la norme.

SEUILS DU SON (ceux de niveau.py, fichier publié)
  Film avec voix ou musique (par défaut) : -14 LUFS ± 1 et crête <= -1,0 dBTP. Sinon ECHEC.
  Film sans voix ni musique (--sans-fond) : pas de cible LUFS. Crête du bruitage le plus fort entre -3 et
    -1 dBTP, niveau jamais au-dessus de -14 LUFS (+1). Règle tenue : ATTENTION (feu jaune), jamais OK.
    Le contrôle du fond entre les bruitages se fait avec niveau.py mesurer --sans-fond.
  Tolérance de lecture sur la crête : 0,05 dB.

DÉBIT : ATTENTION au-delà d'environ 8 Mbit/s en 1080p (16 en 1440p, 35 en 4K). Un fichier bien plus lourd
  (grain, bruit, trame fine animée) est long à envoyer et sera de toute façon recompressé par la plateforme.
"""
import sys
sys.dont_write_bytecode = True
import argparse, json, re, subprocess

FORMATS = {
    "reel": (1080, 1920), "tiktok": (1080, 1920), "short": (1080, 1920),
    "youtube": (1920, 1080), "youtube-1440p": (2560, 1440), "youtube-4k": (3840, 2160),
}
DEBIT_MAX = {"youtube-1440p": 16.0, "youtube-4k": 35.0}   # Mbit/s ; 8 pour tous les formats 1080p
TOLERANCE_LU, PLAFOND_DBTP, CRETE_MIN_SANS_FOND, LECTURE = 1.0, -1.0, -3.0, 0.05


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def mesurer_son(chemin):
    """Niveau intégré, crête vraie, plage dynamique : même commande et même lecture que niveau.py."""
    p = run(["ffmpeg", "-hide_banner", "-nostats", "-i", chemin, "-map", "0:a:0", "-af", "ebur128=peak=true",
             "-f", "null", "-"])
    bloc = p.stderr[p.stderr.rfind("Summary:"):] if "Summary:" in p.stderr else ""

    def lire(motif):
        m = re.search(motif, bloc)
        if not m:
            return None
        return float("-inf") if "inf" in m.group(1) else float(m.group(1))

    i = lire(r"\bI:\s*(-?[\d.]+|-?inf)\s*LUFS")
    lra = lire(r"LRA:\s*(-?[\d.]+|-?inf)\s*LU")
    tp = lire(r"Peak:\s*(-?[\d.]+|-?inf)\s*dBFS")
    if i is None or tp is None:
        return None
    if i <= -70:
        i = float("-inf")
    return {"lufs": i, "tp": tp, "lra": lra or 0.0}


def main():
    ap = argparse.ArgumentParser(description="Contrôle d'un export vidéo avec ffprobe et ffmpeg.")
    ap.add_argument("video")
    ap.add_argument("--format", choices=sorted(FORMATS), default="reel")
    ap.add_argument("--duree", type=float, help="durée attendue en secondes (data-duration de la racine)")
    ap.add_argument("--fps", type=float, default=30.0)
    ap.add_argument("--lufs", type=float, default=-14.0, help="niveau sonore cible (défaut -14)")
    ap.add_argument("--sans-fond", action="store_true",
                    help="film sans voix ni musique : pas de cible LUFS, niveau jugé sur la crête, feu jaune")
    ap.add_argument("--muet", action="store_true", help="la vidéo est volontairement sans piste son")
    ap.add_argument("--debit-max", type=float, help="débit en Mbit/s au-delà duquel le script prévient (défaut : 8 en 1080p)")
    ap.add_argument("--json", action="store_true")
    o = ap.parse_args()

    p = run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", o.video])
    if p.returncode != 0:
        sys.exit(f"ffprobe ne lit pas {o.video} : {p.stderr.strip() or 'fichier absent ou illisible'}")
    info = json.loads(p.stdout)
    v = next((s for s in info.get("streams", []) if s.get("codec_type") == "video"), None)
    a = next((s for s in info.get("streams", []) if s.get("codec_type") == "audio"), None)
    fmt = info.get("format", {})
    res = []

    def note(etat, nom, detail):
        res.append({"etat": etat, "controle": nom, "detail": detail})

    if v is None:
        note("ECHEC", "image", "aucune piste vidéo")
    else:
        w, h = FORMATS[o.format]
        note("OK" if (v.get("width"), v.get("height")) == (w, h) else "ECHEC", "taille",
             f"{v.get('width')}x{v.get('height')} (attendu {w}x{h})")
        note("OK" if v.get("codec_name") == "h264" else "ECHEC", "codec image", f"{v.get('codec_name')} (attendu h264)")
        pf = v.get("pix_fmt")
        note("OK" if pf == "yuv420p" else "ECHEC", "couleur",
             f"{pf} (attendu yuv420p ; un fichier 4:4:4 ou 10 bits n'est pas lu partout)")
        num, _, den = (v.get("avg_frame_rate") or "0/1").partition("/")
        fps = float(num) / float(den or 1) if float(den or 1) else 0.0
        note("OK" if abs(fps - o.fps) < 0.02 else "ECHEC", "images par seconde", f"{fps:.3f} (attendu {o.fps:g})")
        sar = v.get("sample_aspect_ratio", "1:1")
        if sar not in ("1:1", "0:1", None):
            note("ECHEC", "pixels", f"pixels non carrés ({sar})")

    dur = float(fmt.get("duration") or 0)
    if o.duree is not None:
        tol = 1.5 / o.fps
        note("OK" if abs(dur - o.duree) <= tol else "ECHEC", "durée", f"{dur:.3f} s (attendu {o.duree:.3f} s, tolérance {tol:.3f} s)")
    else:
        note("OK" if dur > 0 else "ECHEC", "durée", f"{dur:.3f} s (donner --duree pour comparer à la composition)")
    if v is not None and a is not None:
        dv, da = float(v.get("duration") or dur), float(a.get("duration") or dur)
        note("OK" if abs(dv - da) <= 0.1 else "ATTENTION", "image et son", f"image {dv:.3f} s, son {da:.3f} s")
    taille = int(fmt.get("size") or 0)
    note("OK" if taille > 10000 else "ECHEC", "poids", f"{taille / 1e6:.2f} Mo")
    if dur > 0 and taille > 10000:
        debit = taille * 8 / dur / 1e6
        plafond_debit = o.debit_max if o.debit_max is not None else DEBIT_MAX.get(o.format, 8.0)
        if debit <= plafond_debit:
            note("OK", "débit", f"{debit:.1f} Mbit/s (repère : {plafond_debit:g} au plus)")
        else:
            note("ATTENTION", "débit", f"{debit:.1f} Mbit/s, au-dessus du repère de {plafond_debit:g} : fichier lourd "
                 f"({taille / 1e6:.0f} Mo), long à envoyer et recompressé par la plateforme. Cause habituelle : grain, "
                 f"bruit ou trame fine animés. Rendre avec --max-bitrate {plafond_debit:g}M --buffer-size {2 * plafond_debit:g}M, "
                 "ou réencoder (references/exports.md), puis regarder le grain sur trois images")

    mesure = None
    if a is None:
        note("OK" if o.muet else "ECHEC", "son", "aucune piste son" + ("" if o.muet else " (ajouter --muet si c'est voulu)"))
    else:
        note("OK" if a.get("codec_name") == "aac" else "ATTENTION", "codec son", f"{a.get('codec_name')} (attendu aac)")
        sr = int(a.get("sample_rate") or 0)
        note("OK" if sr == 48000 else "ATTENTION", "fréquence", f"{sr} Hz (48000 conseillé)")
        note("OK" if int(a.get("channels") or 0) == 2 else "ATTENTION", "canaux", f"{a.get('channels')} (2 attendu)")
        mesure = mesurer_son(o.video)
        if mesure is None:
            note("ATTENTION", "niveau sonore", "mesure impossible (son trop court ?)")
        elif mesure["lufs"] == float("-inf"):
            note("OK" if o.muet else "ECHEC", "niveau sonore", "piste son silencieuse" + ("" if o.muet else " (ajouter --muet si c'est voulu)"))
        else:
            i, tp, lra = mesure["lufs"], mesure["tp"], mesure["lra"]
            if o.sans_fond:
                if i > o.lufs + TOLERANCE_LU:
                    note("ECHEC", "niveau sonore", f"{i:.1f} LUFS, au-dessus de {o.lufs:g} : baisser par un gain constant")
                elif tp < CRETE_MIN_SANS_FOND - LECTURE and i < o.lufs - TOLERANCE_LU:
                    note("ECHEC", "niveau sonore", f"{i:.1f} LUFS et crête {tp:.1f} dBTP : trop bas, la crête du bruitage le plus "
                         f"fort doit être entre {CRETE_MIN_SANS_FOND:g} et {PLAFOND_DBTP:g} dBTP (skill son : finaliser.py --sans-fond)")
                else:
                    note("ATTENTION", "niveau sonore", f"{i:.1f} LUFS ; film sans voix ni musique : la cible {o.lufs:g} LUFS ne "
                         f"s'applique pas, niveau jugé sur la crête ({tp:.1f} dBTP). À écrire dans la note de livraison ; "
                         "fond entre les bruitages à contrôler avec niveau.py mesurer --sans-fond")
            else:
                ecart = abs(i - o.lufs)
                suite = "" if ecart <= TOLERANCE_LU else (" : régler le niveau après le rendu (skill son, finaliser.py). "
                                                         "Film sans voix ni musique : relancer avec --sans-fond")
                note("OK" if ecart <= TOLERANCE_LU else "ECHEC", "niveau sonore",
                     f"{i:.1f} LUFS (cible {o.lufs:g} ± {TOLERANCE_LU:g}) ; plage {lra:.1f} LU{suite}")
            note("OK" if tp <= PLAFOND_DBTP + LECTURE else "ECHEC", "crête", f"{tp:.1f} dBTP (plafond {PLAFOND_DBTP:g})")

    if v is not None:
        b = run(["ffmpeg", "-hide_banner", "-nostats", "-i", o.video, "-frames:v", "1", "-vf",
                 "signalstats,metadata=print:file=-", "-f", "null", "-"])
        y = re.search(r"YAVG=([0-9.]+)", b.stdout + b.stderr)
        if y:
            lum = float(y.group(1))
            note("OK" if lum >= 20 else "ECHEC", "première image", f"luminosité moyenne {lum:.0f}/255 (noire sous 20 : l'image 0 est la vignette)")
        with open(o.video, "rb") as f:
            head = f.read(4096)
        note("OK" if b"moov" in head else "ATTENTION", "lecture immédiate",
             "index en tête de fichier" if b"moov" in head else "index en fin de fichier (réencoder avec -movflags +faststart)")

    echec = any(r["etat"] == "ECHEC" for r in res)
    reserve = any(r["etat"] == "ATTENTION" for r in res)
    feu = "rouge" if echec else ("jaune" if reserve else "vert")
    if o.json:
        son = None
        if mesure is not None:
            son = {"lufs": None if mesure["lufs"] == float("-inf") else mesure["lufs"], "crete_dbtp": mesure["tp"],
                   "lra": mesure["lra"], "profil": "sans-fond" if o.sans_fond else "voix-ou-musique",
                   "methode": "ffmpeg ebur128=peak=true, bloc Summary"}
        print(json.dumps({"fichier": o.video, "format": o.format, "ok": not echec, "feu": feu, "son": son, "controles": res},
                         ensure_ascii=False, indent=1))
    else:
        for r in res:
            print(f"{r['etat']:<9} {r['controle']:<20} {r['detail']}")
        fin = {"rouge": "FEU ROUGE : à corriger avant publication",
               "jaune": "FEU JAUNE : livrable, chaque ligne ATTENTION est à écrire dans la note de livraison (regarder aussi 3 images extraites du fichier)",
               "vert": "FEU VERT : conforme (regarder aussi 3 images extraites du fichier)"}[feu]
        print("\nRésultat :", fin)
    sys.exit(1 if echec else 0)


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        if hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8")
    main()
