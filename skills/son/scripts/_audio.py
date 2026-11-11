"""Fonctions communes des scripts du skill son : décodage par ffmpeg, enveloppe, conversions. Python standard."""
import array, math, subprocess, sys
sys.dont_write_bytecode = True   # aucun __pycache__ dans le plugin


def decoder(chemin, sr=22050, debut=None, duree=None):
    """Renvoie (échantillons mono en flottants -1..1, fréquence). Tout fichier lisible par ffmpeg (audio ou vidéo)."""
    cmd = ["ffmpeg", "-v", "error"]
    if debut is not None:
        cmd += ["-ss", str(debut)]
    if duree is not None:
        cmd += ["-t", str(duree)]
    cmd += ["-i", chemin, "-vn", "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"]
    try:
        p = subprocess.run(cmd, capture_output=True)
    except FileNotFoundError:
        sys.exit("ffmpeg est introuvable : l'installer (voir le skill rendu, installation).")
    if p.returncode != 0 or not p.stdout:
        sys.exit(f"Lecture impossible : {chemin} ({p.stderr.decode('utf-8', 'replace').strip() or 'pas de son'})")
    a = array.array("h")
    a.frombytes(p.stdout[: len(p.stdout) // 2 * 2])
    if sys.byteorder == "big":
        a.byteswap()
    return [s / 32768.0 for s in a], sr


def rms_fenetres(x, sr, pas_s):
    """Niveau RMS par fenêtre de pas_s secondes (valeurs linéaires)."""
    n = max(1, int(sr * pas_s))
    out = []
    for i in range(0, len(x) - n + 1, n):
        acc = 0.0
        for v in x[i:i + n]:
            acc += v * v
        out.append(math.sqrt(acc / n))
    return out


def passe_bas(x, sr, fc):
    """Filtre passe-bas à un pôle (suffisant pour suivre l'énergie des graves)."""
    a = 1.0 - math.exp(-2 * math.pi * fc / sr)
    y, out = 0.0, []
    for v in x:
        y += a * (v - y)
        out.append(y)
    return out


def db(v):
    return 20 * math.log10(v) if v > 1e-9 else -180.0


def moments(x, sr):
    """Attaque (premier passage à 20 % du pic RMS 5 ms), pic, fin (queue 40 dB sous le pic), durée, en secondes."""
    pas = 0.005
    env = rms_fenetres(x, sr, pas)
    if not env or max(env) <= 1e-6:
        return None
    pic_v = max(env)
    i_pic = env.index(pic_v)
    i_att = next(i for i, v in enumerate(env) if v >= 0.2 * pic_v)
    seuil = pic_v * 10 ** (-40 / 20)
    i_fin = len(env) - 1
    while i_fin > i_pic and env[i_fin] < seuil:
        i_fin -= 1
    return {"attaque_s": round(i_att * pas, 3), "pic_s": round((i_pic + 0.5) * pas, 3),
            "fin_s": round((i_fin + 1) * pas, 3), "duree_s": round(len(x) / sr, 3),
            "pic_dbfs": round(db(max(abs(v) for v in x)), 1)}


def dynamique(x, sr):
    """Mesures de dynamique d'un signal mono (fenêtres RMS de 50 ms), en dBFS.
    plancher  : niveau du 10e centile des fenêtres (ce qu'on entend ENTRE les sons : souffle, ton de pièce) ;
    fort      : fenêtre la plus forte ; ecart_fond = fort - plancher ;
    facteur_crete      : crête - RMS de tout le fichier (très grand pour des coups isolés dans du silence) ;
    facteur_crete_fort : crête - RMS dans les 400 ms les plus fortes (baisse quand un limiteur écrase les coups) ;
    silence   : part du temps sous -60 dBFS."""
    pas = 0.05
    env = rms_fenetres(x, sr, pas)
    if not env:
        return None
    tri = sorted(env)
    plancher, fort = db(tri[int(0.10 * (len(tri) - 1))]), db(tri[-1])
    crete = db(max(abs(v) for v in x))
    rms = db(math.sqrt(sum(v * v for v in x) / len(x)))
    k, meilleur, i_fort = 8, -1.0, 0                      # 8 fenêtres de 50 ms = 400 ms
    for i in range(0, max(1, len(env) - k + 1)):
        e = sum(v * v for v in env[i:i + k])
        if e > meilleur:
            meilleur, i_fort = e, i
    n = int(sr * pas)
    bloc = x[i_fort * n:(i_fort + k) * n] or x
    rms_fort = db(math.sqrt(sum(v * v for v in bloc) / len(bloc)))
    crete_fort = db(max(abs(v) for v in bloc))
    return {"plancher_dbfs": round(plancher, 1), "fort_dbfs": round(fort, 1), "ecart_fond_db": round(fort - plancher, 1),
            "rms_dbfs": round(rms, 1), "crete_dbfs": round(crete, 1), "facteur_crete_db": round(crete - rms, 1),
            "facteur_crete_fort_db": round(crete_fort - rms_fort, 1),
            "silence": round(sum(1 for v in env if db(v) < -60) / len(env), 2)}


def reduction(avant, apres, gain_db, sr=22050):
    """Ce qu'un limiteur a retiré : compare `avant` (+ gain_db) et `apres` par fenêtres de 10 ms.
    Renvoie la réduction maximale (dB), la part du temps où elle dépasse 1 dB, et la plus longue durée d'affilée (s)."""
    a, _ = decoder(avant, sr)
    b, _ = decoder(apres, sr)
    ea, eb = rms_fenetres(a, sr, 0.01), rms_fenetres(b, sr, 0.01)
    n = min(len(ea), len(eb))
    maxi, nb, suite, plus_longue = 0.0, 0, 0, 0
    for i in range(n):
        niv = db(ea[i]) + gain_db
        r = niv - db(eb[i]) if niv > -50 else 0.0
        maxi = max(maxi, r)
        if r > 1.0:
            nb += 1; suite += 1; plus_longue = max(plus_longue, suite)
        else:
            suite = 0
    return {"reduction_max_db": round(maxi, 1), "part_temps_reduit": round(nb / n, 3) if n else 0.0,
            "plus_longue_reduction_s": round(plus_longue * 0.01, 2)}


def utf8():
    for s in (sys.stdout, sys.stderr):
        if hasattr(s, "reconfigure"):
            s.reconfigure(encoding="utf-8")
