#!/usr/bin/env python3
"""Niveau final d'un film rendu, en une commande : MP4 rendu -> MP4 livré, image copiée sans réencodage.

  python3 finaliser.py renders/film.mp4 [-o renders/film-livre.mp4]
                       [--sans-fond] [--fond fonds/nappe-calme.ogg [--fond-ecart 10]]
                       [--cible -14] [--plafond -1] [--max-limiteur 6] [--forcer] [--rapport audio/niveau-final.json]

Pourquoi : le mixeur de HyperFrames plafonne la crête à -1 dBTP ; monter les data-volume ne dépasse pas environ
-19,5 LUFS. Le niveau final se règle donc APRÈS le rendu, sur le son seul, puis on le remonte sur l'image.

Ce que fait le script (les mêmes étapes à la main sont dans SKILL.md, étape 7) :
  1. mesure le MP4 rendu (méthode de niveau.py : ebur128=peak=true) ;
  2. extrait le son en WAV 48 kHz 24 bits ;
  3. --fond : mélange un fond en boucle sous le film (fondu d'entrée 0,3 s, de sortie 1,2 s), son niveau moyen
     posé --fond-ecart dB sous le passage le plus fort des bruitages ;
  4. règle le niveau (niveau.py masteriser) :
       - film avec voix ou musique (par défaut) : gain constant vers -14 LUFS, limiteur seulement sur les crêtes,
         au plus --max-limiteur dB retirés (au-delà le film sort plus bas, sauf --forcer) ;
       - --sans-fond (ni voix ni musique) : gain constant seul, crête du plus fort bruitage au plafond, jamais
         de limiteur, jamais au-dessus de -14 LUFS ;
  5. remonte le son sur l'image (vidéo copiée, AAC 192 kbit/s), mesure le MP4 produit, et recommence l'étape 4
     avec un plafond plus bas tant que la crête du MP4 dépasse le plafond publié (l'AAC déplace les crêtes) ;
  6. vérifie que l'image est restée identique (empreinte MD5 des paquets vidéo) et imprime avant / après :
     LUFS, crête, plage dynamique, plancher, facteur de crête, travail du limiteur.
Code de sortie : 0 (feu vert ou jaune), 1 (feu rouge : voir les remarques).
"""
import sys
sys.dont_write_bytecode = True
import argparse, json, os, shutil, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import niveau
from _audio import decoder, dynamique


def ff(args, quoi):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode != 0:
        sys.exit(f"ffmpeg a échoué ({quoi}) : {r.stderr.strip()[-400:]}")
    return r


def md5_image(chemin):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", chemin, "-map", "0:v:0", "-c", "copy", "-f", "md5", "-"],
                       capture_output=True, text=True)
    return r.stdout.strip()


def duree(chemin):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", chemin],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def etat(chemin):
    m = niveau.mesurer(chemin)
    x, sr = decoder(chemin)
    m["dyn"] = dynamique(x, sr)
    return m


def ligne(nom, e):
    d = e["dyn"]
    plancher = "silence     " if d["plancher_dbfs"] < -120 else f"{d['plancher_dbfs']:6.1f} dBFS"
    return (f"  {nom:6s} {e['lufs']:6.1f} LUFS | crête {e['tp']:5.1f} dBTP | LRA {e['lra']:4.1f} LU | plancher {plancher} | "
            f"passage fort {d['fort_dbfs']:5.1f} dBFS | facteur de crête {d['facteur_crete_db']:4.1f} dB (passage fort {d['facteur_crete_fort_db']:4.1f})")


def main():
    ap = argparse.ArgumentParser(description="Niveau final d'un MP4 rendu : extraire, régler, remonter sur l'image copiée.")
    ap.add_argument("entree"); ap.add_argument("-o", "--out")
    ap.add_argument("--sans-fond", action="store_true", help="film sans voix ni musique : gain constant seul, feu jaune")
    ap.add_argument("--fond", help="fichier de fond (musique, nappe) à mélanger en boucle sous le film")
    ap.add_argument("--fond-ecart", type=float, default=10.0, help="dB entre le passage le plus fort et le niveau moyen du fond (défaut 10)")
    ap.add_argument("--cible", type=float, default=-14.0); ap.add_argument("--plafond", type=float, default=-1.0, help="crête du MP4 livré, dBTP")
    ap.add_argument("--max-limiteur", type=float, default=6.0); ap.add_argument("--forcer", action="store_true")
    ap.add_argument("--rapport", help="écrire les mesures en JSON")
    o = ap.parse_args()
    if o.sans_fond and o.fond:
        sys.exit("--sans-fond et --fond ne vont pas ensemble : avec un fond, le film vise la cible.")
    racine, _ = os.path.splitext(o.entree)
    sortie = o.out or racine + "-livre.mp4"
    if os.path.abspath(sortie) == os.path.abspath(o.entree):
        sys.exit("La sortie doit être un autre fichier que l'entrée.")
    avant = etat(o.entree)
    tmp = tempfile.mkdtemp(prefix="finaliser-")
    try:
        extrait, maitre = os.path.join(tmp, "extrait.wav"), os.path.join(tmp, "maitre.wav")
        ff(["-i", o.entree, "-map", "0:a:0", "-vn", "-ar", "48000", "-c:a", "pcm_s24le", extrait], "extraction du son")
        source, gain_fond = extrait, None
        if o.fond:
            xf, srf = decoder(o.fond)
            df = dynamique(xf, srf)
            gain_fond = (avant["dyn"]["fort_dbfs"] - o.fond_ecart) - df["rms_dbfs"]
            d = duree(extrait)
            source = os.path.join(tmp, "avec-fond.wav")
            ff(["-i", extrait, "-stream_loop", "-1", "-i", o.fond, "-filter_complex",
                f"[1:a]aresample=48000,atrim=0:{d:.3f},volume={gain_fond:.2f}dB,afade=t=in:d=0.3,"
                f"afade=t=out:st={max(0, d - 1.2):.3f}:d=1.2[f];[0:a][f]amix=inputs=2:normalize=0:duration=first[m]",
                "-map", "[m]", "-ar", "48000", "-c:a", "pcm_s24le", source], "mélange du fond")
            print(f"Fond {os.path.basename(o.fond)} : gain {gain_fond:+.1f} dB (niveau moyen {o.fond_ecart:g} dB sous le passage le plus fort).")
        plafond_maitre, info, apres = o.plafond - 0.5, None, None
        print("Réglage du son extrait" + (" (fond compris)" if o.fond else "") + " :")
        for passe in range(5):
            info = niveau.masteriser(source, maitre, o.cible, plafond_maitre, o.sans_fond, o.max_limiteur, o.forcer,
                                     dire=(print if passe == 0 else (lambda *_: None)))
            ff(["-i", o.entree, "-i", maitre, "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-c:a", "aac",
                "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", sortie], "remontage sur l'image")
            apres = etat(sortie)
            if apres["tp"] <= o.plafond + 0.05:
                break
            plafond_maitre -= apres["tp"] - o.plafond + 0.2
            print(f"Après AAC la crête est à {apres['tp']:.1f} dBTP : nouveau passage, plafond du maître {plafond_maitre:.1f} dBTP.")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    image_ok = md5_image(o.entree) == md5_image(sortie)
    feu, plafond, tol, rq = niveau.juger(apres, apres["dyn"], True, o.cible, o.sans_fond)
    if not image_ok:
        feu = "rouge"; rq.append("l'image du fichier livré diffère de l'image rendue : ne pas livrer, chercher pourquoi.")
    print("\nAvant / après (mesurés sur les MP4, non écoutés) :")
    print(ligne("rendu", avant)); print(ligne("livré", apres))
    da, db_ = avant["dyn"], apres["dyn"]
    if da["plancher_dbfs"] < -120:
        plancher = "plancher : silence numérique avant" + (" et après" if db_["plancher_dbfs"] < -120 else f", {db_['plancher_dbfs']:.1f} dBFS après")
    else:
        plancher = f"plancher {db_['plancher_dbfs'] - da['plancher_dbfs']:+.1f} dB"
    print(f"  {plancher} ; facteur de crête du passage fort "
          f"{db_['facteur_crete_fort_db'] - da['facteur_crete_fort_db']:+.1f} dB ; gain appliqué {info['gain_db']:+.1f} dB"
          + (f" ; limiteur : {info['reduction_max_db']:.1f} dB au plus, {info['part_temps_reduit'] * 100:.1f} % du temps" if info.get("limiteur") else " ; pas de limiteur"))
    if info.get("limiteur") and info["reduction_max_db"] > 6:
        print("  À l'oreille (déduit des mesures) : coups nettement écrasés et fond remonté d'autant que le gain ; "
              "préférer un fond (--fond) ou la règle --sans-fond.")
    if info.get("limiteur") and info["part_temps_reduit"] > 0.10:
        print("  À l'oreille (déduit des mesures) : le limiteur travaille plus de 10 % du temps, risque de pompage du fond.")
    print(f"  image : {'identique (paquets vidéo copiés, même empreinte MD5)' if image_ok else 'DIFFÉRENTE'}")
    for r in rq:
        print("  -", r)
    print(f"FEU {feu.upper()} -> {sortie}")
    if o.rapport:
        os.makedirs(os.path.dirname(os.path.abspath(o.rapport)), exist_ok=True)
        json.dump({"entree": o.entree, "sortie": sortie, "profil": "sans-fond" if o.sans_fond else "voix-ou-musique",
                   "fond": o.fond, "gain_fond_db": gain_fond, "feu": feu, "avant": avant, "apres": apres,
                   "gain_db": info["gain_db"], "limiteur": {k: info.get(k) for k in ("limiteur", "reduction_max_db", "part_temps_reduit", "plus_longue_reduction_s")},
                   "image_identique": image_ok, "remarques": rq, "methode": "ffmpeg ebur128=peak=true, bloc Summary"},
                  open(o.rapport, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    sys.exit(1 if feu == "rouge" else 0)


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        if hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8")
    main()
