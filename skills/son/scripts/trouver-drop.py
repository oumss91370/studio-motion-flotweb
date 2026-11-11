#!/usr/bin/env python3
"""Trouver le drop d'une musique par l'énergie, et dire où poser la musique dans le film (ffmpeg + Python standard).

  python3 trouver-drop.py musique.mp3 [--drop-film 12.4] [--bpm 120] [--top 3]

Méthode (d'après howseen-ai/claude-motion-design, MIT) : ne jamais se fier à une grille de temps automatique ;
mesurer l'énergie (bande entière et graves) par demi-seconde, chercher le plus grand saut durable, puis affiner
dans des fenêtres de 25 ms autour du saut.
--drop-film : instant du film (en s) où le drop doit tomber (révélation, logo, moment fort) ; le script donne alors
les attributs à écrire sur la balise <audio> de la musique.
--bpm : si connu (npx hyperframes beats --json), affiche aussi la durée d'un temps et d'une mesure.
"""
import argparse, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audio import decoder, rms_fenetres, passe_bas, db, utf8


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("musique"); ap.add_argument("--drop-film", type=float); ap.add_argument("--bpm", type=float)
    ap.add_argument("--top", type=int, default=3); ap.add_argument("--json", action="store_true")
    o = ap.parse_args()
    sr = 11025
    x, sr = decoder(o.musique, sr=sr)
    duree = len(x) / sr
    pas = 0.5
    plein = [db(v) for v in rms_fenetres(x, sr, pas)]
    grave = [db(v) for v in rms_fenetres(passe_bas(passe_bas(x, sr, 150), sr, 150), sr, pas)]
    n = len(plein)
    if n < 10:
        sys.exit("Musique trop courte pour chercher un drop (moins de 5 s).")
    k = 4  # 2 s avant, 2 s après
    cands = []
    for i in range(k, n - k):
        av_p, ap_p = sum(plein[i - k:i]) / k, sum(plein[i:i + k]) / k
        av_g, ap_g = sum(grave[i - k:i]) / k, sum(grave[i:i + k]) / k
        saut = 0.5 * (ap_p - av_p) + 0.5 * (ap_g - av_g)
        cands.append((saut, i, ap_p - av_p, ap_g - av_g))
    cands.sort(reverse=True)
    choisis = []
    for c in cands:
        if choisis and c[0] < 1.5:
            break
        if all(abs(c[1] - d[1]) * pas > 4.0 for d in choisis):
            choisis.append(c)
        if len(choisis) >= o.top:
            break
    res = []
    for saut, i, dp, dg in choisis:
        # affinage : première fenêtre de 25 ms dont le niveau rejoint le niveau d'après le saut
        t0 = max(0.0, i * pas - 0.75)
        seg = x[int(t0 * sr): int((t0 + 1.5) * sr)]
        fin = rms_fenetres(seg, sr, 0.025)
        apres = sum(sorted(fin)[-max(1, len(fin) // 4):]) / max(1, len(fin) // 4)
        j = next((q for q, v in enumerate(fin) if v >= 0.6 * apres), 0)
        res.append({"t": round(t0 + j * 0.025, 3), "saut_db": round(saut, 1), "saut_plein_db": round(dp, 1), "saut_grave_db": round(dg, 1)})
    sortie = {"fichier": o.musique, "duree_s": round(duree, 2), "candidats": res}
    if not o.json:
        print(f"{o.musique} : {duree:.1f} s")
        for r, c in enumerate(res, 1):
            fiab = "net" if c["saut_db"] >= 6 else ("modéré" if c["saut_db"] >= 3 else "faible : cette musique n'a peut-être pas de drop")
            print(f"  {r}. drop probable à {c['t']:.3f} s (saut {c['saut_db']:+.1f} dB ; plein {c['saut_plein_db']:+.1f}, graves {c['saut_grave_db']:+.1f}) : {fiab}")
        print("  Profil (dB par demi-seconde, bande entière) :")
        for a in range(0, min(n, 120), 12):
            print("   " + " ".join(f"{a * pas + q * pas:5.1f}:{plein[a + q]:5.1f}" for q in range(min(12, n - a))))
    if o.bpm:
        temps = 60.0 / o.bpm
        sortie["temps_s"], sortie["mesure_s"] = round(temps, 4), round(temps * 4, 4)
        if not o.json:
            print(f"  À {o.bpm:g} BPM : un temps = {temps:.3f} s, une mesure (4 temps) = {temps * 4:.3f} s")
    if o.drop_film is not None and res:
        d = res[0]["t"]
        if d >= o.drop_film:
            sortie["audio"] = {"data-start": 0, "data-media-start": round(d - o.drop_film, 3)}
            msg = f'data-start="0" data-media-start="{d - o.drop_film:.3f}"  (la musique entre {d - o.drop_film:.3f} s après son propre début)'
        else:
            sortie["audio"] = {"data-start": round(o.drop_film - d, 3), "data-media-start": 0}
            msg = f'data-start="{o.drop_film - d:.3f}"  (la musique commence {o.drop_film - d:.3f} s après le début du film ; prévoir autre chose avant : ambiance, silence voulu)'
        if not o.json:
            print(f"\nPour que le drop ({d:.3f} s dans la musique) tombe à {o.drop_film:.3f} s du film :\n  <audio id=\"musique\" … {msg}>")
            print("  Puis vérifier sur le rendu : npx hyperframes@0.9.33 audio renders/<film>.mp4 --range "
                  f"{max(0, o.drop_film - 1):.1f},{o.drop_film + 1:.1f} --only onsets")
    if o.json:
        print(json.dumps(sortie, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    utf8()
    main()
