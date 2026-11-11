"""Mixage de la bande-son d'une histoire narrée, à partir de `son/design.json`.

  python outils/mix.py        écrit hf/assets/voix.wav, hf/assets/fond.wav, son/mix.wav, son/placements.json

Voix et fond sortent séparés : on peut remplacer la voix sans refaire le reste. Règles appliquées :
- la voix est toujours au-dessus ; la musique plie sous la voix et avant un impact marqué ;
- l'ATTAQUE de chaque bruitage tombe sur son image de contact (pas le début du fichier) ;
- le niveau d'un bruitage est fixé PAR RAPPORT AU FOND mesuré la seconde d'avant ;
- un seul gain global vers −14 LUFS, puis un limiteur de crête ;
- budget d'une histoire narrée : 1 à 2 bruitages par 10 s (le script l'annonce).
Rien n'est écouté : tous les chiffres imprimés sont des mesures. Pour l'écoute et le contrôle final, skill `son`.

`son/design.json` (tout est facultatif sauf les fichiers cités ; chemins relatifs au dossier de l'épisode) :
{
  "cible_lufs": -14.0,
  "voix": {"fichier": "voix/voix.wav", "gain_db": 0, "avance_s": 0.0},
  "musique": {"fichier": "son/sources/theme.wav", "gain_db": -20, "sous_voix_db": 6, "debut_s": 0, "fin_s": 61.5,
              "fondu_entree": 1.5, "fondu_sortie": 3.0, "trous": [{"image": 1464, "images": 20}]},
  "ambiances": [{"fichier": "son/sources/salle.wav", "de_image": 0, "a_image": 600, "gain_db": -30}],
  "bruitages": [{"id": "tintement", "image": 56, "fichier": "son/sources/tintement.wav", "au_dessus_db": 12,
                 "type": "impact", "plie_db": 4, "duree_s": 3}]
}
`avance_s` : écart mesuré par ecart_voix.py quand le son de la voix est en retard sur ses repères de mots.
"""
import json, pathlib, subprocess, sys
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import reglages as R
import plans

FE, IPS = 48000, R.IPS
DUREE = plans.TOTAL / IPS
N = int(round(FE * DUREE))


def charger(chemin, mono=False):
    f = R.RACINE / chemin
    if not f.exists():
        raise SystemExit(f"fichier son introuvable : {chemin}")
    brut = subprocess.run(["ffmpeg", "-v", "error", "-i", str(f), "-f", "f32le", "-ac", "2", "-ar", str(FE), "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(brut, dtype=np.float32).reshape(-1, 2).copy()
    if mono:
        x[:] = x.mean(axis=1, keepdims=True)
    return x


def db(g):
    return 10 ** (g / 20)


def rms_db(x):
    return 20 * np.log10(max(1e-7, float(np.sqrt(np.mean(x ** 2))))) if len(x) else -140.0


def fondu(x, entree=0.0, sortie=0.0):
    n = len(x)
    if entree:
        k = min(n, int(entree * FE))
        x[:k] *= np.linspace(0, 1, k)[:, None] ** 2
    if sortie:
        k = min(n, int(sortie * FE))
        x[n - k:] *= np.linspace(1, 0, k)[:, None] ** 2
    return x


def poser(bus, x, t0):
    a = int(round(t0 * FE))
    if a < 0:
        x, a = x[-a:], 0
    b = min(N, a + len(x))
    if b > a:
        bus[a:b] += x[: b - a]


def lisse(y, k):
    k = max(1, int(k))
    c = np.concatenate([[0.0], np.cumsum(y, dtype=np.float64)])
    n = len(y)
    i = np.arange(n)
    a, b = np.clip(i - k // 2, 0, n), np.clip(i + k - k // 2, 0, n)
    return ((c[b] - c[a]) / np.maximum(1, b - a)).astype(np.float32)


def enveloppe(x, fen=0.05):
    return np.sqrt(np.maximum(0, lisse((x ** 2).mean(axis=1), fen * FE)))


def lufs(x):
    p = subprocess.run(["ffmpeg", "-v", "info", "-f", "f32le", "-ar", str(FE), "-ac", "2", "-i", "-", "-af", "ebur128=peak=true", "-f", "null", "-"],
                       input=x.astype(np.float32).tobytes(), capture_output=True)
    fin = p.stderr.decode("utf-8", "replace")
    fin = fin[fin.rfind("Summary:"):]
    val = lambda cle: float(fin.split(cle)[1].split()[0])
    return val("I:"), val("LRA:"), val("Peak:")


def ecrire(chemin, x):
    f = R.RACINE / chemin
    f.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "f32le", "-ar", str(FE), "-ac", "2", "-i", "-", "-c:a", "pcm_s24le", str(f)],
                   input=x.astype(np.float32).tobytes(), check=True)


def main():
    fd = R.SON / "design.json"
    if not fd.exists():
        raise SystemExit("son/design.json absent : voir le modèle en tête de ce fichier.")
    D = json.loads(fd.read_text(encoding="utf-8"))
    cible = D.get("cible_lufs", R.CIBLE_LUFS)

    # ---------- voix (avancée de l'écart mesuré entre ses repères de mots et le son réel)
    voix = np.zeros((N, 2), np.float32)
    v = D.get("voix")
    if v:
        poser(voix, charger(v["fichier"], mono=True) * db(v.get("gain_db", 0)), -v.get("avance_s", 0.0))
    ve = enveloppe(voix, 0.12)
    parle = np.clip(ve / max(1e-6, np.percentile(ve, 90)) * 3, 0, 1) if v else np.zeros(N, np.float32)
    parle = lisse(parle, 0.25 * FE)

    # ---------- fond : musique + ambiances
    fond = np.zeros((N, 2), np.float32)
    m = D.get("musique")
    if m:
        x = charger(m["fichier"])[int(m.get("depuis_s", 0) * FE):]
        x = fondu(x[: int((m.get("fin_s", DUREE) - m.get("debut_s", 0)) * FE)].copy(), m.get("fondu_entree", 1.5), m.get("fondu_sortie", 3.0)) * db(m["gain_db"])
        mus = np.zeros((N, 2), np.float32)
        poser(mus, x, m.get("debut_s", 0))
        g = np.ones(N, np.float32)
        for tr in m.get("trous", []):                 # silence voulu : la musique s'efface puis revient
            a, b = int(tr["image"] / IPS * FE), min(N, int((tr["image"] + tr["images"]) / IPS * FE))
            k = int(0.12 * FE)
            g[a:b] = 0
            g[max(0, a - k):a] = np.minimum(g[max(0, a - k):a], np.linspace(1, 0, min(k, a)))
            g[b:b + 4 * k] = np.minimum(g[b:b + 4 * k], np.linspace(0, 1, len(g[b:b + 4 * k])))
        for c in D.get("bruitages", []):              # la musique plie avant un impact marqué
            if c.get("plie_db"):
                t = c["image"] / IPS
                a, b = max(0, int((t - 0.4) * FE)), min(N, int((t + 0.5) * FE))
                k = min(int(0.25 * FE), (b - a) // 2)
                fen = np.ones(b - a) * db(-c["plie_db"])
                fen[:k] = np.linspace(1, db(-c["plie_db"]), k)
                fen[-k:] = np.linspace(db(-c["plie_db"]), 1, k)
                g[a:b] = np.minimum(g[a:b], fen)
        mus *= (g * (1 - parle * (1 - db(-m.get("sous_voix_db", 6)))))[:, None]
        fond += mus
    for am in D.get("ambiances", []):
        x = charger(am["fichier"])
        besoin = int((am["a_image"] - am["de_image"]) / IPS * FE) + int(0.6 * FE)
        x = np.concatenate([x] * int(np.ceil(besoin / len(x))))[:besoin]
        poser(fond, fondu(x.copy(), 0.25, 0.35) * db(am["gain_db"]), am["de_image"] / IPS - 0.12)
    fond_seul = fond.copy()

    # ---------- bruitages : attaque sur l'image, niveau relatif au fond de la seconde d'avant
    placements, sfx = [], np.zeros((N, 2), np.float32)
    for c in D.get("bruitages", []):
        x = charger(c["fichier"], mono=not c.get("large", False))
        a = int(c.get("depuis_s", 0) * FE)
        x = fondu(x[a: a + int(c.get("duree_s", 10) * FE)].copy(), c.get("fondu_entree", 0.004), c.get("fondu_sortie", 0.25))
        e = enveloppe(x, 0.02)
        k_att = int(np.argmax(e > 0.5 * e.max())) if c.get("type", "impact") == "impact" else int(np.argmax(e))
        att = c.get("attaque_s", k_att / FE)          # instant de l'attaque (ou du sommet) dans le fichier
        t = c["image"] / IPS
        ref = max(rms_db(fond_seul[max(0, int((t - 1.0) * FE)): max(1, int(t * FE))]), -48.0)   # plancher : sur un vrai silence on ne chuchote pas
        j, k = int(np.argmax(e)), int(0.1 * FE)
        gain = ref + c["au_dessus_db"] - rms_db(x[max(0, j - k // 2): j + k // 2])
        poser(sfx, x * db(gain), t - att)
        placements.append({"id": c["id"], "image": c["image"], "t": round(t, 3), "attaque_dans_fichier_s": round(att, 3), "fond_db": round(ref, 1),
                           "niveau_db": round(ref + c["au_dessus_db"], 1), "gain_applique_db": round(gain, 1), "fichier": c["fichier"]})
    fond_total = fond + sfx

    # ---------- niveau global : un seul gain vers la cible, puis plafond de crête
    total = voix + fond_total
    if float(np.abs(total).max()) < 1e-6:
        raise SystemExit("le mix est vide : aucun son dans design.json")
    I, _, _ = lufs(total)
    G = cible - I
    voix_f, fond_f = voix * db(G), fond_total * db(G)
    total = voix_f + fond_f
    plafond = db(-2.2)                               # en crête échantillon ; la crête vraie finit vers −1,5 dBTP
    if float(np.abs(total).max()) > plafond:         # limiteur par blocs de 2 ms avec anticipation : seules les crêtes plient
        B = 96
        nb = len(total) // B + 1
        pad = np.zeros(nb * B, np.float32)
        pad[:len(total)] = np.abs(total).max(axis=1)
        gb = np.minimum(1.0, plafond / np.maximum(pad.reshape(nb, B).max(axis=1), 1e-9))
        gb = np.minimum.reduce([np.roll(gb, k) for k in (-2, -1, 0, 1, 2)])
        gain = np.minimum(np.interp(np.arange(len(total)), np.arange(nb) * B + B / 2, gb), np.repeat(gb, B)[:len(total)]).astype(np.float32)
        voix_f, fond_f = voix_f * gain[:, None], fond_f * gain[:, None]
        total = voix_f + fond_f
    I2, LRA2, PK2 = lufs(total)
    if v:
        ecrire("hf/assets/voix.wav", voix_f)
    ecrire("hf/assets/fond.wav", fond_f)
    ecrire("son/mix.wav", total)
    (R.SON / "placements.json").write_text(json.dumps(placements, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"avant gain : {I:.1f} LUFS | gain global {G:+.1f} dB | après : {I2:.1f} LUFS (cible {cible:g}), LRA {LRA2:.1f} LU, crête vraie {PK2:.1f} dBTP")
    if v and (parle > 0.5).any() and (parle < 0.05).any():
        vdb, fdb = rms_db(voix_f[parle > 0.5]), rms_db(fond_f[parle < 0.05])
        print(f"voix (quand elle parle) {vdb:.1f} dB RMS | fond entre les répliques {fdb:.1f} dB RMS | écart {vdb - fdb:.1f} dB")
    par10 = len(placements) / DUREE * 10
    lo, hi = R.BRUITAGES_PAR_10S
    avis = "" if DUREE < 20 or lo <= par10 <= hi else f"  <- hors du budget d'une histoire narrée ({lo:g} à {hi:g})"
    print(f"bruitages : {len(placements)} ({par10:.1f} par 10 s){avis}")
    for p in placements:
        print(f"  {p['id']:<24} image {p['image']:>5}  fond {p['fond_db']:>6} dB  ->  {p['niveau_db']:>6} dB  (gain {p['gain_applique_db']:+.1f})")
    print("Niveaux mesurés, non écoutés.")


if __name__ == "__main__":
    main()
