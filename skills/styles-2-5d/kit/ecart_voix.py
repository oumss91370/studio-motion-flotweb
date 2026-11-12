"""Contrôle de l'écart entre les repères de mots et le son réel de la voix.

  python outils/ecart_voix.py [voix/voix.wav] [voix/mots.json]

Pourquoi : les repères de mots fournis par une voix de synthèse peuvent être décalés par rapport au son. Au rendu
réel du 11/11/2026, ils étaient en avance de 107 ms, de façon constante : sous-titres et coupes arrivaient avant
la voix. Les horodatages de whisper.cpp (via ffmpeg) étaient trop grossiers pour servir d'arbitre ; c'est la FORME
D'ONDE qui a tranché.

Méthode : pour chaque mot qui suit un silence d'au moins 250 ms dans les repères (début de réplique), on cherche
dans le son le vrai début de la parole (l'instant où l'énergie sort du silence), et on compare. On donne la
médiane et la dispersion. Un écart CONSTANT se corrige d'un seul décalage ; un écart qui varie veut dire que les
repères sont faux : refaire l'alignement (faster-whisper avec horodatage au mot, ou alignement forcé).
"""
import json, pathlib, subprocess, sys
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import reglages as R

FE = 16000


def mesurer(wav, mots_json, silence_min=0.25):
    brut = subprocess.run(["ffmpeg", "-v", "error", "-i", str(wav), "-f", "f32le", "-ac", "1", "-ar", str(FE), "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(brut, dtype=np.float32)
    pas = FE // 200                                    # fenêtres de 5 ms
    n = len(x) // pas
    e = np.sqrt((x[:n * pas].reshape(n, pas) ** 2).mean(axis=1))
    seuil = max(np.percentile(e, 95) * 0.06, 1e-4)     # 6 % du niveau de la parole
    actif = e > seuil
    mots = json.loads(pathlib.Path(mots_json).read_text(encoding="utf-8"))
    ecarts, prec_fin = [], -10.0
    for m in mots:
        if m["start"] - prec_fin >= silence_min:
            i0, i1 = int(max(0, m["start"] - 0.4) * 200), int((m["start"] + 0.4) * 200)
            fen = actif[i0:i1]
            if len(fen) > 4 and not fen[:4].any() and fen.any():      # on part bien d'un silence
                vrai = (i0 + int(np.argmax(fen))) / 200
                ecarts.append((m["text"], m["start"], vrai, vrai - m["start"]))
        prec_fin = m["end"]
    return ecarts


if __name__ == "__main__":
    wav = sys.argv[1] if len(sys.argv) > 1 else R.VOIX / "voix.wav"
    mj = sys.argv[2] if len(sys.argv) > 2 else R.VOIX / "mots.json"
    for f in (wav, mj):
        if not pathlib.Path(f).exists():
            raise SystemExit(f"fichier introuvable : {f}")
    ecarts = mesurer(wav, mj)
    if len(ecarts) < 3:
        raise SystemExit(f"seulement {len(ecarts)} début(s) de réplique mesurable(s) : contrôler à l'œil sur la forme d'onde.")
    d = np.array([x[3] for x in ecarts]) * 1000
    for t, rep, vrai, ec in ecarts:
        print(f"  {t:<16} repère {rep:7.3f} s   son {vrai:7.3f} s   écart {ec * 1000:+5.0f} ms")
    med, disp = float(np.median(d)), float(np.percentile(d, 90) - np.percentile(d, 10))
    print(f"{len(d)} débuts de réplique : écart médian {med:+.0f} ms (le son est {'en retard' if med > 0 else 'en avance'} sur les repères), dispersion {disp:.0f} ms")
    if abs(med) <= 33:
        print("Moins d'une image d'écart : rien à corriger.")
    elif disp <= 40:
        print(f"Écart constant : avancer la voix de {med / 1000:.3f} s au mixage (design.json, voix.avance_s), ou décaler tous les repères de {med / 1000:+.3f} s. Pas les deux.")
    else:
        print("Écart variable : les repères ne sont pas fiables. Refaire l'alignement au mot (faster-whisper ou alignement forcé).")
