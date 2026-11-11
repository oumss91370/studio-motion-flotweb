#!/usr/bin/env python3
"""Mesurer et régler le niveau sonore final (ffmpeg + Python standard).

MÉTHODE DE MESURE (la seule du studio ; tout autre contrôle doit donner les mêmes chiffres)
-----------------------------------------------------------------------------------------
    ffmpeg -hide_banner -nostats -i <fichier> -map 0:a:0 -af ebur128=peak=true -f null -

  et lecture du bloc « Summary » imprimé à la fin :
    - niveau intégré  = ligne « I: »    (LUFS, norme ITU-R BS.1770 / EBU R128, avec ses deux portes) ;
    - plage dynamique = ligne « LRA: »  (LU) ;
    - crête vraie     = ligne « Peak: » (dBTP ; ffmpeg écrit « dBFS », mais avec peak=true c'est la crête
      vraie, suréchantillonnée, la plus haute des canaux).
  Précision : le dixième. La mesure se fait sur le fichier tel qu'il sera publié (le MP4, donc après AAC),
  première piste audio, tous canaux, durée entière, sans conversion préalable.

  NE PAS mesurer avec « loudnorm=print_format=json » (input_i) : sur un film de 10 s il s'écarte jusqu'à 0,8 LU
  (film de test pixel-8-bits : loudnorm -15,3 ; ebur128 -16,0 ; calcul BS.1770 indépendant en Python -16,01).

  Mesures complémentaires (Python, sur le son décodé en mono 22 050 Hz, fenêtres RMS de 50 ms) :
    - plancher = 10e centile des fenêtres, en dBFS (ce qu'on entend entre les sons) ;
    - passage le plus fort = fenêtre la plus forte ; écart fond = fort - plancher ;
    - facteur de crête = crête - RMS (fichier entier, et dans les 400 ms les plus fortes).

SEUILS
------
  Film AVEC voix ou musique (par défaut) :
    fichier publié (mp4, mov, m4a, aac, mp3, webm) : -14 LUFS ± 1 ; crête <= -1,0 dBTP ;
    fichier maître (wav, flac)                      : -14 LUFS ± 0,5 ; crête <= -1,5 dBTP.
    Dans la plage : VERT. Hors plage : ROUGE (code 1).
  Film SANS voix ni musique (option explicite --sans-fond) : la cible -14 LUFS ne s'applique pas.
    1. un seul gain constant, aucun limiteur : le silence reste du silence ;
    2. crête du bruitage le plus fort entre -3 et -1 dBTP sur le fichier publié (maître : -3,5 à -1,5) ;
    3. niveau intégré jamais au-dessus de -14 LUFS (bruitages denses : on s'arrête à -14, la crête peut
       alors rester sous -3) ;
    4. le fond entre les bruitages (plancher) reste au moins 20 dB sous le passage le plus fort : un ton de
       pièce monté pour gonfler le chiffre est du souffle, pas un fond.
    Règle tenue : JAUNE (code 0), à écrire dans la note de livraison. Règle non tenue : ROUGE (code 1).
  Tolérance de lecture sur la crête : 0,05 dB (affichage au dixième).

COMMANDES
---------
  python3 niveau.py mesurer fichier.(wav|mp4) [--cible -14] [--sans-fond] [--json]
  python3 niveau.py masteriser mix.wav -o bande-son.wav [--cible -14] [--plafond -1.5] [--sans-fond]
                                                        [--max-limiteur 6] [--forcer]
      Avec voix ou musique : UN gain constant vers la cible ; un limiteur seulement si la crête dépasserait le
      plafond. Le plafond est tenu en crête vraie : limiteur à 192 kHz, puis mesure du fichier écrit et nouveau
      passage tant que la crête mesurée dépasse (le plafond annoncé est le plafond mesuré). Si le limiteur
      devait retirer plus de --max-limiteur dB aux crêtes, le fichier sort plus bas que la cible et le script le
      dit (ajouter un fond, ou film « sans fond ») ; --forcer passe outre.
      --sans-fond : gain constant seul = min(cible - niveau, plafond - crête). Jamais de limiteur.
  Le parcours complet sur un MP4 rendu (extraire, masteriser, remonter sur l'image) : finaliser.py.
"""
import sys
sys.dont_write_bytecode = True
import argparse, json, os, re, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audio import decoder, dynamique, reduction

PUBLIE = (".mp4", ".mov", ".m4a", ".aac", ".mp3", ".webm", ".ogg", ".opus")
ECART_FOND_MIN = 20.0       # dB entre le passage le plus fort et le plancher (film sans fond)
CRETE_MIN_SANS_FOND = -3.0  # dBTP, fichier publié


def _ffmpeg(args):
    try:
        return subprocess.run(["ffmpeg", "-hide_banner", "-nostats"] + args, capture_output=True, text=True,
                              encoding="utf-8", errors="replace")
    except FileNotFoundError:
        sys.exit("ffmpeg est introuvable : l'installer (voir le skill rendu, installation).")


def mesurer(chemin):
    """Niveau intégré (LUFS), crête vraie (dBTP), plage dynamique (LU) : méthode décrite en tête de fichier."""
    p = _ffmpeg(["-i", chemin, "-map", "0:a:0", "-af", "ebur128=peak=true", "-f", "null", "-"])
    bloc = p.stderr[p.stderr.rfind("Summary:"):] if "Summary:" in p.stderr else ""
    def lire(motif):
        m = re.search(motif, bloc)
        if not m:
            return None
        v = m.group(1)
        return float("-inf") if "inf" in v else float(v)
    i, lra, tp = lire(r"\bI:\s*(-?[\d.]+|-?inf)\s*LUFS"), lire(r"LRA:\s*(-?[\d.]+|-?inf)\s*LU"), lire(r"Peak:\s*(-?[\d.]+|-?inf)\s*dBFS")
    if i is None or tp is None:
        sys.exit(f"Mesure impossible sur {chemin} (pas de son ?) : {p.stderr.strip()[-300:]}")
    if i <= -70:
        i = float("-inf")
    return {"lufs": i, "tp": tp, "lra": lra or 0.0}


def mesurer_dynamique(chemin):
    x, sr = decoder(chemin)
    return dynamique(x, sr)


def juger(m, dyn, publie, cible=-14.0, sans_fond=False):
    """Renvoie (feu, plafond, tolérance, remarques). feu = 'vert', 'jaune' ou 'rouge'."""
    tol, plafond = (1.0, -1.0) if publie else (0.5, -1.5)
    rq, rouge = [], False
    if m["tp"] > plafond + 0.05:
        rouge = True
        rq.append(f"crête {m['tp']:.1f} dBTP au-dessus du plafond {plafond:g} : remasteriser (finaliser.py).")
    if not sans_fond:
        if m["lufs"] < cible - tol:
            rouge = True
            rq.append("trop bas pour un film avec voix ou musique : régler le niveau après le rendu (finaliser.py). "
                      "Si le film n'a ni voix ni musique : lui ajouter un fond (dossier fonds/, ou finaliser.py --fond), "
                      "ou le déclarer avec --sans-fond.")
        elif m["lufs"] > cible + tol:
            rouge = True
            rq.append("trop fort : la plateforme baissera le son ; remasteriser à la cible.")
        return ("rouge" if rouge else "vert"), plafond, tol, rq
    if m["lufs"] > cible + tol:
        rouge = True
        rq.append(f"niveau au-dessus de {cible:g} LUFS : baisser par un gain constant.")
    crete_min = CRETE_MIN_SANS_FOND + (0.0 if publie else -0.5)
    if m["tp"] < crete_min - 0.05 and m["lufs"] < cible - tol:
        rouge = True
        rq.append(f"trop bas : la crête du bruitage le plus fort est à {m['tp']:.1f} dBTP (attendu entre {crete_min:g} "
                  f"et {plafond:g}) : remonter par un gain constant (finaliser.py --sans-fond).")
    if dyn and dyn["silence"] < 0.5 and dyn["ecart_fond_db"] < ECART_FOND_MIN:
        rouge = True
        rq.append(f"silence remonté : le fond entre les bruitages ({dyn['plancher_dbfs']:.1f} dBFS) n'est qu'à "
                  f"{dyn['ecart_fond_db']:.1f} dB sous le passage le plus fort ({dyn['fort_dbfs']:.1f} dBFS), il en faut "
                  f"{ECART_FOND_MIN:g} : baisser le ton de pièce dans la composition (ou poser un vrai fond et "
                  "retirer --sans-fond).")
    if not rouge:
        rq.append(f"film sans voix ni musique : la cible {cible:g} LUFS ne s'applique pas ; niveau réglé sur la crête. "
                  "À écrire dans la note de livraison.")
    return ("rouge" if rouge else "jaune"), plafond, tol, rq


def cmd_mesurer(o):
    m, dyn = mesurer(o.fichier), mesurer_dynamique(o.fichier)
    publie = o.fichier.lower().endswith(PUBLIE)
    feu, plafond, tol, rq = juger(m, dyn, publie, o.cible, o.sans_fond)
    if o.json:
        print(json.dumps({"fichier": o.fichier, "feu": feu, "profil": "sans-fond" if o.sans_fond else "voix-ou-musique",
                          "lufs": m["lufs"], "crete_dbtp": m["tp"], "lra": m["lra"], "cible": o.cible, "tolerance": tol,
                          "plafond_dbtp": plafond, "dynamique": dyn, "remarques": rq,
                          "methode": "ffmpeg ebur128=peak=true, bloc Summary"}, ensure_ascii=False, indent=1))
        sys.exit(1 if feu == "rouge" else 0)
    ok_tp = m["tp"] <= plafond + 0.05
    if o.sans_fond:
        ligne = f"niveau {m['lufs']:.1f} LUFS (sans voix ni musique : pas de cible, maximum {o.cible:g})"
    else:
        ligne = f"niveau {m['lufs']:.1f} LUFS (cible {o.cible:g} ± {tol:g}) : {'OK' if abs(m['lufs'] - o.cible) <= tol else 'HORS CIBLE'}"
    print(f"{o.fichier}\n  {ligne}\n  crête {m['tp']:.1f} dBTP (plafond {plafond:g}) : {'OK' if ok_tp else 'TROP HAUTE'}"
          f"\n  plage dynamique {m['lra']:.1f} LU")
    if dyn:
        print(f"  plancher {dyn['plancher_dbfs']:.1f} dBFS ; passage le plus fort {dyn['fort_dbfs']:.1f} dBFS ; écart {dyn['ecart_fond_db']:.1f} dB ; "
              f"facteur de crête {dyn['facteur_crete_db']:.1f} dB (passage fort : {dyn['facteur_crete_fort_db']:.1f} dB) ; "
              f"silence {dyn['silence'] * 100:.0f} % du temps")
    for r in rq:
        print("  -", r)
    print(f"  FEU {feu.upper()}")
    sys.exit(1 if feu == "rouge" else 0)


def _ecrire(entree, sortie, filtres):
    r = _ffmpeg(["-loglevel", "error", "-y", "-i", entree, "-map", "0:a:0", "-af", ",".join(filtres),
                 "-ar", "48000", "-c:a", "pcm_s24le", sortie])
    if r.returncode != 0:
        sys.exit("ffmpeg a échoué : " + r.stderr.strip())


def masteriser(entree, sortie, cible=-14.0, plafond=-1.5, sans_fond=False, max_limiteur=6.0, forcer=False, dire=print):
    """Écrit `sortie` (WAV 48 kHz, 24 bits). Renvoie un dictionnaire de mesures avant / après."""
    m = mesurer(entree)
    if m["lufs"] == float("-inf"):
        sys.exit(f"{entree} : silence, rien à régler.")
    gain = cible - m["lufs"]
    info = {"avant": m, "limiteur": False, "plafond": plafond, "cible": cible}
    if sans_fond:
        gain = min(gain, plafond - m["tp"])
        for _ in range(4):
            _ecrire(entree, sortie, [f"volume={gain:.2f}dB"])
            f = mesurer(sortie)
            if f["tp"] <= plafond + 0.05:
                break
            gain -= f["tp"] - plafond + 0.05
        dire(f"Film sans fond : gain constant {gain:+.1f} dB, aucun limiteur.")
    else:
        depassement = m["tp"] + gain - plafond
        if depassement <= 0:
            _ecrire(entree, sortie, [f"volume={gain:.2f}dB"])
            f = mesurer(sortie)
            if f["tp"] > plafond + 0.05:               # arrondi de mesure : rattraper par le gain
                gain -= f["tp"] - plafond + 0.05
                _ecrire(entree, sortie, [f"volume={gain:.2f}dB"]); f = mesurer(sortie)
        else:
            if depassement > max_limiteur and not forcer:
                dire(f"Pour {cible:g} LUFS le limiteur devrait retirer {depassement:.1f} dB aux crêtes (maximum admis "
                     f"{max_limiteur:g}) : gain réduit, le fichier sortira sous la cible. Le mix est trop creux : ajouter un "
                     "fond continu (dossier fonds/), ou déclarer le film --sans-fond ; --forcer pour passer outre.")
                gain -= depassement - max_limiteur
            elif depassement > max_limiteur:
                dire(f"ATTENTION (--forcer) : le limiteur retire {depassement:.1f} dB aux crêtes : coups écrasés, fond remonté.")
            info["limiteur"] = True
            limite_db, ecart_cible = plafond - 0.1, 0.0
            for passe in range(8):
                lim = max(0.0625, 10 ** (limite_db / 20))
                _ecrire(entree, sortie, [f"volume={gain:.2f}dB", "aresample=192000",
                                         f"alimiter=limit={lim:.5f}:attack=5:release=50:level=false:latency=true",
                                         "aresample=48000"])
                f = mesurer(sortie)
                if f["tp"] > plafond + 0.05:           # le plafond doit être tenu sur le fichier écrit
                    limite_db -= f["tp"] - plafond + 0.1
                    continue
                ecart_cible = cible - f["lufs"]        # le limiteur a fait perdre du niveau : le rendre par le gain
                reste = max_limiteur - (m["tp"] + gain - plafond)
                if ecart_cible > 0.25 and (forcer or reste > 0.25) and passe < 7:
                    gain += ecart_cible if forcer else min(ecart_cible, reste)
                    continue
                break
            info.update(reduction(entree, sortie, gain))
            dire(f"Limiteur : crêtes réduites de {info['reduction_max_db']:.1f} dB au plus, pendant {info['part_temps_reduit'] * 100:.1f} % "
                 f"du temps (plus longue réduction d'affilée : {info['plus_longue_reduction_s']:.2f} s).")
    info.update({"apres": f, "gain_db": round(gain, 2), "sortie": sortie})
    dire(f"Avant : {m['lufs']:.1f} LUFS, {m['tp']:.1f} dBTP, LRA {m['lra']:.1f} | gain {gain:+.1f} dB\n"
         f"Après : {f['lufs']:.1f} LUFS, {f['tp']:.1f} dBTP, LRA {f['lra']:.1f} -> {sortie}")
    if f["tp"] > plafond + 0.05:
        dire(f"ATTENTION : crête mesurée {f['tp']:.1f} dBTP au-dessus du plafond {plafond:g} malgré les passages.")
    if not sans_fond and abs(f["lufs"] - cible) > 0.5:
        dire(f"Écart {f['lufs'] - cible:+.1f} LU avec la cible : le mix est trop creux pour {cible:g} LUFS sans écraser.")
    if m["lra"] - f["lra"] > 3:
        dire("ATTENTION : la plage dynamique a perdu plus de 3 LU : le limiteur travaille trop.")
    return info


def cmd_masteriser(o):
    masteriser(o.entree, o.out, o.cible, o.plafond, o.sans_fond, o.max_limiteur, o.forcer)


def main():
    ap = argparse.ArgumentParser(description="Niveau sonore : mesurer, masteriser à -14 LUFS (ou règle « sans fond »).")
    sp = ap.add_subparsers(dest="cmd", required=True)
    a = sp.add_parser("mesurer"); a.add_argument("fichier"); a.add_argument("--cible", type=float, default=-14.0)
    a.add_argument("--sans-fond", action="store_true", help="film sans voix ni musique : règle de crête, feu jaune")
    a.add_argument("--json", action="store_true"); a.set_defaults(f=cmd_mesurer)
    b = sp.add_parser("masteriser"); b.add_argument("entree"); b.add_argument("-o", "--out", required=True)
    b.add_argument("--cible", type=float, default=-14.0); b.add_argument("--plafond", type=float, default=-1.5)
    b.add_argument("--sans-fond", action="store_true", help="gain constant seul, jamais de limiteur")
    b.add_argument("--max-limiteur", type=float, default=6.0, help="dB que le limiteur peut retirer aux crêtes (défaut 6)")
    b.add_argument("--forcer", action="store_true", help="atteindre la cible même si le limiteur écrase")
    b.set_defaults(f=cmd_masteriser)
    o = ap.parse_args()
    o.f(o)


if __name__ == "__main__":
    for s in (sys.stdout, sys.stderr):
        if hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8")
    main()
