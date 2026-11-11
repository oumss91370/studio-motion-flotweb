#!/usr/bin/env python3
"""Caler chaque bruitage sur l'image de son événement (ffmpeg + Python standard).

  python3 caler.py attaque son.ogg [autre.ogg ...]
      Mesure dans le fichier : attaque, pic, fin de la queue, durée.

  python3 caler.py placer audio/plan.json [--index index.html] [--out audio/placements.json] [--html]
                                          [--piste 20] [--html-out audio/balises.html]
      plan.json = [{"id": "impact:logo:1", "t": 4.200, "fichier": "assets/sfx/impact.ogg",
                    "type": "impact", "gain_db": -6}, ...]
      "t" = l'instant de l'événement À L'IMAGE, tiré du code de la vidéo (jamais tapé au jugé).
      "fichier" = chemin depuis le dossier du projet (celui de index.html), ou chemin absolu.
      Règle de calage selon "type" (sans "type", le premier mot de l'identifiant sert de type : « bip:voyant:1 ») :
        - sons à attaque (impact, hit, coup, choc, click, clic, pop, bip, blip, pose, key, touche, tick, tic, snap,
          land, knock, drop, ding, bell, cloche, tintement) : l'attaque du son tombe sur l'image de l'événement
          + 8 ms, jamais avant l'image ;
        - whoosh, swish, souffle, transition, passage : le PIC du son tombe sur l'instant donné (pic de vitesse) ;
        - riser, montee, swell : la FIN du son tombe 100 ms avant l'instant donné (l'impact qui suit) ;
        - ambiance, musique, fond, nappe, bed, voix : début à l'instant donné ;
        - type inconnu : traité comme un son à attaque, et signalé.
      Champs facultatifs : "avance_ms" (remplace la règle), "debut_fichier" (rogner le début du fichier, en s).
      Sortie : placements.json (début du fichier dans le film, en secondes). --html imprime les balises <audio>
      prêtes à coller : src relatif à index.html, data-duration mesurée, une piste par son (--piste = la première).
"""
import sys
sys.dont_write_bytecode = True
import argparse, json, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _audio import decoder, moments, utf8

ATTAQUE = {"impact", "hit", "coup", "choc", "click", "clic", "pop", "bip", "blip", "beep", "pose", "poser", "key", "touche",
           "tick", "tic", "tock", "snap", "land", "knock", "drop", "ding", "bell", "cloche", "tintement"}
SOMMET = {"whoosh", "swish", "souffle", "transition", "passage", "woosh"}
MONTEE = {"riser", "montee", "montée", "swell"}
FOND = {"ambiance", "ambience", "musique", "music", "fond", "nappe", "bed", "voix"}
CIBLE_MS = 8.0


def mesure(chemin, debut=None):
    x, sr = decoder(chemin, sr=44100, debut=debut)
    m = moments(x, sr)
    if m is None:
        sys.exit(f"{chemin} : silence, rien à caler")
    return m


def cmd_attaque(o):
    for f in o.fichiers:
        m = mesure(f)
        print(f"{f}\n  attaque {m['attaque_s']:.3f} s | pic {m['pic_s']:.3f} s | fin {m['fin_s']:.3f} s | durée {m['duree_s']:.3f} s | crête {m['pic_dbfs']} dBFS")


def trouver_index(o):
    """Le dossier de index.html : --index, sinon le dossier courant, sinon le dossier parent du plan, sinon celui du plan."""
    if o.index:
        return os.path.dirname(os.path.abspath(o.index))
    plan = os.path.dirname(os.path.abspath(o.plan))
    for d in (os.getcwd(), os.path.dirname(plan), plan):
        if os.path.exists(os.path.join(d, "index.html")):
            return d
    return os.getcwd()


def cmd_placer(o):
    plan = json.load(open(o.plan, encoding="utf-8"))
    base = os.path.dirname(os.path.abspath(o.plan))
    racine = trouver_index(o)
    sortie, html = [], []
    for k, p in enumerate(plan):
        typ = str(p.get("type") or str(p.get("id", "")).split(":")[0] or "impact").lower()
        chemin = next((c for c in (p["fichier"], os.path.join(racine, p["fichier"]), os.path.join(base, p["fichier"]))
                       if os.path.exists(c)), None)
        if chemin is None:
            sys.exit(f"{p.get('id', k)} : fichier introuvable : {p['fichier']} (cherché depuis {racine} et {base})")
        rogne = float(p.get("debut_fichier", 0) or 0)
        m = mesure(chemin, debut=rogne or None)
        t = float(p["t"])
        note = ""
        if "avance_ms" in p:
            debut, regle = t - float(p["avance_ms"]) / 1000.0, "avance imposée"
        elif typ in SOMMET:
            debut, regle = t - m["pic_s"], "pic sur l'instant"
        elif typ in MONTEE:
            debut, regle = t - 0.100 - m["fin_s"], "fin 100 ms avant l'instant"
        elif typ in FOND:
            debut, regle = t, "début sur l'instant"
        else:
            debut, regle = t + CIBLE_MS / 1000.0 - m["attaque_s"], "attaque sur l'image (+8 ms)"
            if typ not in ATTAQUE:
                note = f" (type « {typ} » inconnu : traité comme un son à attaque)"
        alerte = ""
        if debut < 0:
            alerte = f" ATTENTION : commencerait {-debut:.3f} s avant le film ; rogner le fichier (debut_fichier) ou choisir un son plus court."
            debut = 0.0
        q = dict(p)
        q.update({"type": typ, "t_evenement": t, "t": round(debut, 4), "regle": regle, "duree": m["duree_s"],
                  "attaque_s": m["attaque_s"], "pic_s": m["pic_s"], "fin_s": m["fin_s"], "piste": o.piste + k})
        sortie.append(q)
        print(f"{p.get('id', k)} ({typ}) : événement {t:.3f} s -> début du fichier {debut:.3f} s [{regle}]{note}{alerte}")
        ident = re.sub(r"[^a-zA-Z0-9_-]", "-", str(p.get("id", f"son-{k}")))
        vol = round(10 ** (float(p.get("gain_db", 0)) / 20), 3)
        extra = f' data-media-start="{rogne:g}"' if rogne else ""
        src = os.path.relpath(os.path.abspath(chemin), racine).replace(os.sep, "/")
        if src.startswith(".."):
            print(f"  ATTENTION : {src} est hors du dossier du projet ; un rendu ne lit que les fichiers du projet : le copier dans assets/sfx/.")
        html.append(f'<audio id="sfx-{ident}" class="clip" src="{src}" data-start="{debut:.3f}" data-duration="{m["duree_s"]:.3f}"{extra} '
                    f'data-volume="{vol}" data-track-index="{o.piste + k}"></audio>')
    json.dump(sortie, open(o.out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("Écrit :", o.out)
    if o.html_out:
        open(o.html_out, "w", encoding="utf-8").write("\n".join(html) + "\n")
        print("Écrit :", o.html_out)
    if o.html:
        print(f"\nÀ coller dans la composition racine ({os.path.join(racine, 'index.html')}), puis lint et check :\n" + "\n".join(html))


def main():
    ap = argparse.ArgumentParser(description="Caler les bruitages sur l'image.")
    sp = ap.add_subparsers(dest="cmd", required=True)
    a = sp.add_parser("attaque"); a.add_argument("fichiers", nargs="+"); a.set_defaults(f=cmd_attaque)
    b = sp.add_parser("placer"); b.add_argument("plan"); b.add_argument("--fps", type=float, default=30)
    b.add_argument("--out", default="placements.json"); b.add_argument("--html", action="store_true")
    b.add_argument("--html-out", help="écrire aussi les balises dans ce fichier")
    b.add_argument("--index", help="chemin de index.html (défaut : dossier courant, sinon dossier parent du plan)")
    b.add_argument("--piste", type=int, default=20, help="numéro de la première piste ; une piste par son (défaut 20)")
    b.set_defaults(f=cmd_placer)
    o = ap.parse_args()
    o.f(o)


if __name__ == "__main__":
    utf8()
    main()
