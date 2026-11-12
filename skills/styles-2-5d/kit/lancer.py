"""Lanceur de la chaîne mesurée : construire le décor, rendre les passes, assembler, encoder. Un seul Blender à la fois, reprise automatique.

  python outils/lancer.py construire        bl_scene.py -> decors/decor.blend
  python outils/lancer.py rendre [quoi]     les trois passes de chaque image (quoi : tout | film | A:12,L:9001) ; reprend après un plantage
  python outils/lancer.py assembler         compo.py : images finales, puis sortie/film.mp4
  python outils/lancer.py tout              les trois à la suite
  python outils/lancer.py arreter           arrête proprement le rendu en cours (par son numéro de processus)
  python outils/lancer.py etat              où en est le rendu
  python outils/lancer.py plans             les tronçons de caméra de chaque plan et leur mode de rendu (plaque, couches, 3d)

Rendu rapide : le décor n'est rendu qu'UNE fois par tronçon de caméra quand la caméra ne fait que dériver (plaque.py) ; seuls les
vrais déplacements sont rendus image par image. Pour tout rendre image par image : variable EPISODE_MODE=3d.

Règles tirées des essais : UN SEUL Blender qui rend (un verrou refuse une deuxième boucle) ; on arrête une boucle par son numéro
de processus, jamais en tuant « tout ce qui s'appelle blender » (on tuerait aussi le Blender ouvert et le pont du connecteur) ;
ne pas rendre la main tant que le rendu tourne. Dossier de l'épisode : celui qui contient outils/, ou la variable EPISODE_RACINE.
Écrit par Flot Web.
"""
import json, os, pathlib, subprocess, sys, time
sys.dont_write_bytecode = True
ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import reglages
import camera as C
import plaque as PQ
import film as F

RAC = pathlib.Path(os.environ.get("EPISODE_RACINE", ICI.parent)).resolve()
BLEND, PASSES, VERROU = RAC / "decors" / "decor.blend", RAC / "passes", RAC / "passes" / ".verrou"
ESSAIS_MAX = 25


def _env():
    return dict(os.environ, EPISODE_RACINE=str(RAC), PYTHONDONTWRITEBYTECODE="1")

def _blender():
    exe = reglages.trouver_blender()
    if not exe:
        raise SystemExit("Blender introuvable : l'installer, ou donner son chemin dans la variable BLENDER.")
    return exe

def _vivant(pid):
    try:
        if os.name == "nt":
            return str(pid) in subprocess.run(["tasklist", "/FI", f"PID eq {pid}", "/NH"], capture_output=True, text=True).stdout
        os.kill(pid, 0)
        return True
    except (OSError, ValueError):
        return False

def manquantes(quoi="tout"):
    if quoi in ("tout", "film"):
        noms = []
        for k in list(F.ORDRE) + (list(getattr(F, "FIXES", [])) if quoi == "tout" else []):
            for t in PQ.preparer(F)[k]:
                noms += [f"{k}_{f:04d}" for f in range(t["a"], t["b"])] if t["mode"] == "3d" else [t["nom"]]
    else:
        noms = [f"{x.split(':')[0]}_{int(x.split(':')[1]):04d}" for x in quoi.split(",")]
    return [n for n in noms if not all((PASSES / d / f"{n}.png").exists() for d in ("albedo", "lum", "data"))]

def plans():
    """Affiche, pour chaque plan, ses tronçons de caméra et le mode de rendu choisi (plaque.py)."""
    tot = img = 0
    for k, ts in PQ.preparer(F).items():
        for t in ts:
            n = t["b"] - t["a"]
            r = n if t["mode"] == "3d" else 1
            tot += r; img += n
            extra = "" if t["mode"] == "3d" else f" ; plaque de {t['taille'][0]} × {t['taille'][1]} px, focale {t['focale']:.1f} mm"
            print(f"{t['nom']:6s} images {t['a']:4d} à {t['b'] - 1:4d} ({n:3d}) : {t['mode']:8s} ({t['raison']}){extra}")
    print(f"{tot} rendus Blender pour {img} images (image par image : {img})")

def construire():
    t = time.time()
    r = subprocess.run([_blender(), "-b", "--python", str(ICI / "bl_scene.py"), "--", "construire"], env=_env(), capture_output=True, text=True, errors="replace")
    for l in r.stdout.splitlines():
        if any(m in l for m in ("construit", "fusion", "Error", "Traceback", "ATTENTION")):
            print(l)
    if not BLEND.exists() or "Traceback" in r.stdout + r.stderr:
        print((r.stdout + r.stderr)[-3000:])
        raise SystemExit("la construction a échoué")
    print(f"construction : {time.time() - t:.0f} s")

def rendre(quoi="tout"):
    PASSES.mkdir(parents=True, exist_ok=True)
    if VERROU.exists():
        v = json.loads(VERROU.read_text())
        if _vivant(v.get("boucle", -1)):
            raise SystemExit(f"un rendu tourne déjà (boucle {v['boucle']}, Blender {v.get('blender')}) : un seul Blender à la fois. Pour l'arrêter : python outils/lancer.py arreter")
        VERROU.unlink()
    if not BLEND.exists():
        construire()
    total = len(manquantes(quoi))
    t0 = time.time()
    try:
        for essai in range(1, ESSAIS_MAX + 1):
            reste = len(manquantes(quoi))
            print(f"essai {essai} : {total - reste} / {total} images ({time.strftime('%H:%M:%S')})", flush=True)
            if not reste:
                break
            proc = subprocess.Popen([_blender(), "-b", str(BLEND), "--python", str(ICI / "bl_scene.py"), "--", "rendre", "100", quoi], env=_env(),
                                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            VERROU.write_text(json.dumps({"boucle": os.getpid(), "blender": proc.pid}))
            proc.wait()
            if (PASSES / ".arret").exists():
                (PASSES / ".arret").unlink()
                print("rendu arrêté à la demande")
                return False
    finally:
        if VERROU.exists():
            VERROU.unlink()
    reste = len(manquantes(quoi))
    dt = time.time() - t0
    print(("RENDU TERMINÉ" if not reste else f"RENDU INCOMPLET : {reste} images manquent") + f" en {dt / 60:.1f} min" + (f" ({dt / total:.1f} s par image)" if total else ""))
    return not reste

def arreter():
    if not VERROU.exists():
        print("aucun rendu en cours"); return
    v = json.loads(VERROU.read_text())
    (PASSES / ".arret").write_text("arret")
    pid = v.get("blender")
    if pid and _vivant(pid):
        if os.name == "nt":
            subprocess.run(["taskkill", "/PID", str(pid), "/F"], capture_output=True)
        else:
            os.kill(pid, 15)
    print(f"arrêt demandé : Blender {pid} arrêté, la boucle {v.get('boucle')} s'arrête sans le relancer")

def assembler():
    r = subprocess.run([sys.executable, str(ICI / "compo.py"), "film"], env=_env())
    if r.returncode:
        raise SystemExit("l'assemblage a échoué")

def etat():
    m = manquantes("tout")
    tot = len(C.images(F))
    print(f"passes : {tot - len(m)} / {tot} images rendues ; rendu en cours : {'oui' if VERROU.exists() else 'non'}")
    faites = sum(1 for f in range(F.TOTAL) if (RAC / "images" / f"f_{f:04d}.jpg").exists())
    print(f"images finales : {faites} / {F.TOTAL} ; film : {'oui' if (RAC / 'sortie' / 'film.mp4').exists() else 'non'}")

if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    a = sys.argv[1] if len(sys.argv) > 1 else "-h"
    if a in ("-h", "--help"):
        print(__doc__)
    elif a == "construire":
        construire()
    elif a == "rendre":
        sys.exit(0 if rendre(sys.argv[2] if len(sys.argv) > 2 else "tout") else 1)
    elif a == "assembler":
        assembler()
    elif a == "tout":
        construire()
        if rendre("tout"):
            assembler()
    elif a == "arreter":
        arreter()
    elif a == "etat":
        etat()
    elif a == "plans":
        plans()
    else:
        raise SystemExit(f"commande inconnue : {a} (voir -h)")
