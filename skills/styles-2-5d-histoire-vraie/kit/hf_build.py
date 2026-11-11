"""Assemblage : encode les images en film, puis écrit le projet HyperFrames (film + sous-titres au mot + son).

  python outils/hf_build.py                 encode rendus/ en hf/assets/film.mp4 et (ré)écrit le projet hf/
  python outils/hf_build.py --sans-film     ne refait que les sous-titres et index.html
  python outils/hf_build.py --essai         accepte des images plus petites que 1080×1920 (agrandies : NON LIVRABLE)

Entrées :
  rendus/f_0000.jpg …          toutes les images du film (plans.TOTAL)
  voix/mots.json               [{"text": "Sur", "start": 0.12, "end": 0.31, "line": 0}, …]   temps en secondes
  voix/texte.txt               (facultatif) le texte, une réplique par ligne, pour repérer la ponctuation
  voix/accents.txt             (facultatif) un mot accentué par ligne : seuls ceux-là reçoivent un léger « pop »
  hf/assets/voix.wav, hf/assets/fond.wav   (facultatifs) écrits par mix.py ; ajoutés au projet s'ils existent

Sous-titres (règles du rendu réel du 11/11/2026) : 1 à 2 mots, capitales grasses blanches à contour sombre, bande
y = 1385 à 1515, taille UNIQUE (un groupe trop long est coupé, jamais rétréci), changement sec sur le début du mot.
Ensuite, dans hf/ :  npx -y hyperframes@0.9.33 lint  puis  check  puis  render  (skill `rendu`).
"""
import html, json, pathlib, re, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import reglages as R
import plans

DUREE = plans.TOTAL / R.IPS
ST = R.SOUS_TITRES
# petits mots qui ne restent jamais seuls à l'écran : ils se collent au mot plein qui suit
OUTILS = {"un", "une", "de", "du", "des", "le", "la", "les", "l'", "à", "a", "au", "aux", "en", "et", "que", "qui", "ne", "se", "sa", "son",
          "ses", "si", "ce", "cet", "cette", "ces", "dans", "sur", "sous", "par", "pour", "mais", "ou", "où", "y", "il", "elle", "on",
          "tout", "plus", "dès", "lui", "pas", "est", "ont", "d'un", "d'une", "qu'il", "qu'elle"}


def encoder_film(essai):
    from PIL import Image
    manque = [i for i in range(plans.TOTAL) if not R.image(i).exists()]
    if manque:
        raise SystemExit(f"{len(manque)} images manquent dans {R.RENDUS} (première : {manque[0]}). Lancer  python outils/rendre.py")
    tailles = set()
    for i in (0, plans.TOTAL // 2, plans.TOTAL - 1):
        with Image.open(R.image(i)) as im:
            tailles.add(im.size)
    vf = []
    if tailles != {(R.LARGEUR, R.HAUTEUR)}:
        if not essai:
            raise SystemExit(f"images en {sorted(tailles)} au lieu de {R.LARGEUR}×{R.HAUTEUR}. Rendre à 100 %, ou ajouter --essai (non livrable).")
        print(f"ESSAI : images {sorted(tailles)} agrandies en {R.LARGEUR}×{R.HAUTEUR}. Ce film n'est PAS livrable.")
        vf = ["-vf", f"scale={R.LARGEUR}:{R.HAUTEUR}:flags=lanczos"]
    sortie = R.HF / "assets" / "film.mp4"
    sortie.parent.mkdir(parents=True, exist_ok=True)
    motif = str(R.RENDUS / f"{R.PREFIXE}%0{R.CHIFFRES}d.{R.EXT}")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(R.IPS), "-start_number", "0", "-i", motif, "-frames:v", str(plans.TOTAL), *vf,
                    "-c:v", "libx264", "-crf", "14", "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(sortie)], check=True)
    print("film encodé :", sortie.relative_to(R.RACINE), f"({plans.TOTAL} images)")


def lire_mots():
    f = R.VOIX / "mots.json"
    if not f.exists():
        raise SystemExit("voix/mots.json absent : c'est l'horodatage au mot de la voix (voir references/pipeline.md, étape 6).")
    mots = json.loads(f.read_text(encoding="utf-8"))
    for i, m in enumerate(mots):
        m.setdefault("id", i)
        m.setdefault("line", 0)
        m["ponct"] = bool(re.search(r"[,.;:?!…]$", m["text"]))
        m["text"] = re.sub(r"[,.;:?!…«»\"]+", "", m["text"]).strip()
    texte = R.VOIX / "texte.txt"
    if texte.exists():                 # ponctuation lue dans le texte, quand les mots n'en portent pas
        lignes = [l.strip() for l in texte.read_text(encoding="utf-8").splitlines() if l.strip()]
        for li, ligne in enumerate(lignes):
            pos = 0
            for m in (x for x in mots if x["line"] == li):
                i = ligne.find(m["text"], pos)
                if i < 0:
                    continue
                pos = i + len(m["text"])
                m["ponct"] = m["ponct"] or bool(re.match(r"\s*[,.;:?!…]", ligne[pos:]))
    return [m for m in mots if m["text"]]


def grouper(mots):
    """1 ou 2 mots par groupe. Jamais deux mots séparés par une ponctuation ou une pause ; jamais un petit mot seul si on peut l'éviter."""
    outil = lambda t: t.lower() in OUTILS
    groupes, i = [], 0
    while i < len(mots):
        m = mots[i]
        s = mots[i + 1] if i + 1 < len(mots) else None
        paire = False
        if s and s["line"] == m["line"] and not m["ponct"] and s["start"] - m["end"] < 0.18:
            n = len(m["text"]) + len(s["text"])
            if outil(m["text"]) and not outil(s["text"]) and n <= ST["lettres_max_paire"]:
                paire = True               # « la cour », jamais « à la »
            elif not outil(m["text"]) and not outil(s["text"]) and n <= ST["lettres_max_paire"] - 1:
                paire = True               # deux mots courts qui vont ensemble
        g = [m, s] if paire else [m]
        groupes.append(g)
        i += len(g)
    return groupes


def ecrire_projet():
    mots = lire_mots()
    accents = set()
    fa = R.VOIX / "accents.txt"
    if fa.exists():
        accents = {l.strip().lower() for l in fa.read_text(encoding="utf-8").splitlines() if l.strip()}
    groupes = grouper(mots)
    caps = []
    for k, g in enumerate(groupes):
        debut = max(0.1, g[0]["start"] - 0.02)
        suivant = groupes[k + 1][0]["start"] - 0.02 if k + 1 < len(groupes) else DUREE
        fin = suivant if suivant - g[-1]["end"] < 0.35 else g[-1]["end"] + 0.2     # pas de trou de quelques images entre deux groupes
        fin = min(fin, DUREE)
        caps.append(dict(id=f"c{k}", start=round(debut, 3), dur=round(fin - debut, 3), text=" ".join(x["text"] for x in g).upper(),
                         acc=any(x["text"].lower() in accents for x in g), image=round(g[0]["start"] * R.IPS)))

    lignes = [f'    <div class="cap clip" id="{c["id"]}" data-start="{c["start"]}" data-duration="{c["dur"]}" data-track-index="0">'
              f'<div class="w"><span class="o">{html.escape(c["text"])}</span><span class="f">{html.escape(c["text"])}</span></div></div>' for c in caps]
    pops = "\n".join(f'      tl.fromTo("#{c["id"]} .w", {{ scale: 1.16 }}, {{ scale: 1, duration: 0.14, ease: "power3.out" }}, {c["start"]});' for c in caps if c["acc"])
    W, H = R.LARGEUR, R.HAUTEUR
    captions = f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; }}
    /* Bande y = {ST["haut"]} à {ST["haut"] + ST["hauteur"]} : sous les sujets (qui tiennent dans les 65 % du haut), au-dessus de la zone basse de l'application (y > 1560). */
    .cap {{ position: absolute; left: 0; top: {ST["haut"]}px; width: {W}px; height: {ST["hauteur"]}px; text-align: center; overflow: visible; }}
    .cap .w {{ display: inline-grid; font-family: "{ST["police"]}", sans-serif; font-weight: {ST["graisse"]}; font-size: {ST["taille"]}px; line-height: {ST["hauteur"]}px; letter-spacing: 0.01em; white-space: nowrap; }}
    .cap .w span {{ grid-area: 1 / 1; }}
    .cap .o {{ color: {ST["contour"]}; -webkit-text-stroke: {ST["contour_px"]}px {ST["contour"]}; text-shadow: 0 8px 0 rgba(0, 0, 0, 0.45); }}
    .cap .f {{ color: {ST["couleur"]}; }}
  </style>
  <div id="root" data-composition-id="captions" data-width="{W}" data-height="{H}">
{chr(10).join(lignes)}
  </div>
  <script>
    (function () {{
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      // « pop » réservé aux mots accentués ; les autres sous-titres changent sec, sur le début du mot
{pops}
      window.__timelines["captions"] = tl;
    }})();
  </script>
</template>
"""
    audio = []
    if (R.HF / "assets" / "voix.wav").exists():
        audio.append(f'      <audio id="voix" class="clip" src="assets/voix.wav" data-start="0" data-duration="{DUREE}" data-track-index="20" data-volume="1"></audio>')
    if (R.HF / "assets" / "fond.wav").exists():
        audio.append(f'      <audio id="fond" class="clip" src="assets/fond.wav" data-start="0" data-duration="{DUREE}" data-track-index="21" data-volume="1" data-timeline-role="music"></audio>')
    index = f"""<!doctype html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width={W}, height={H}" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ margin: 0; width: {W}px; height: {H}px; overflow: hidden; background: #000; }}
      #root {{ width: 100%; height: 100%; position: relative; }}
      #film {{ position: absolute; left: 0; top: 0; width: {W}px; height: {H}px; z-index: 1; }}
      #captions {{ z-index: 2; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{DUREE}" data-width="{W}" data-height="{H}">
      <!-- image : rendu Blender {W}x{H}, {R.IPS} i/s, {plans.TOTAL} images -->
      <video id="film" class="clip" src="assets/film.mp4" muted playsinline data-start="0" data-duration="{DUREE}" data-track-index="0"></video>
      <!-- sous-titres au mot -->
      <div id="captions" data-composition-id="captions" data-composition-src="compositions/captions.html" data-track-kind="captions"
           data-start="0" data-duration="{DUREE}" data-track-index="1" data-width="{W}" data-height="{H}"></div>
{chr(10).join(audio) if audio else "      <!-- pas de son : lancer mix.py, puis relancer hf_build.py --sans-film -->"}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
    (R.HF / "compositions").mkdir(parents=True, exist_ok=True)
    (R.HF / "assets").mkdir(exist_ok=True)
    (R.HF / "compositions" / "captions.html").write_text(captions, encoding="utf-8")
    (R.HF / "index.html").write_text(index, encoding="utf-8")
    (R.VOIX / "sous-titres.json").write_text(json.dumps(caps, ensure_ascii=False, indent=1), encoding="utf-8")
    court = [c for c in caps if c["dur"] < 0.2]
    print(f"{len(caps)} sous-titres ; {sum(c['acc'] for c in caps)} accentués ; le plus long : {max(caps, key=lambda c: len(c['text']))['text']} ; son : {len(audio)} piste(s)")
    if court:
        print(f"remarque : {len(court)} sous-titre(s) de moins de 0,2 s :", ", ".join(c["text"] for c in court[:8]))
    print(" | ".join(c["text"] for c in caps[:40]))


if __name__ == "__main__":
    if "--sans-film" not in sys.argv:
        encoder_film("--essai" in sys.argv)
    ecrire_projet()
