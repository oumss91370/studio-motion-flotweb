"""Boucle de rendu avec reprise : rend le film image par image, saute ce qui est déjà fait, repart après un plantage.

  python outils/rendre.py                      tout le film (images 0 à TOTAL − 1)
  python outils/rendre.py 120 260              seulement cette plage (bornes incluses)
  python outils/rendre.py --construire [--passe 1|2|3]     (re)construit decors/film.blend avec bl_film.py
  python outils/rendre.py --controle planche p_ 25         rendus de contrôle (voir bl_cli.py)
  python outils/rendre.py --profiler           temps par image AVANT le rendu complet, et durée estimée du film
  python outils/rendre.py --arreter            arrête proprement la boucle en cours (la boucle d'abord, Blender ensuite)

Options de rendu : --pct 25 (essai à taille réduite), --dossier chemin, --profil processeur,
                   --simuler-plantage N (ESSAI : Blender s'arrête brutalement toutes les N images, pour voir la reprise).

Règles tirées du rendu réel du 11/11/2026 :
- UN SEUL Blender à la fois. Le verrou `rendus/.verrou` refuse une deuxième boucle (deux rendus en parallèle
  font planter une carte graphique intégrée, et mélangent des images de deux versions de la scène).
- Pour arrêter : `--arreter`, jamais « tuer Blender ». Si on tue Blender seul, la boucle le relance (boucle fantôme).
  Ne jamais arrêter des processus par un filtre sur le nom (« tout ce qui contient blender ») : on tue aussi le pont
  du connecteur MCP. Ce script n'arrête que le processus qu'il a lancé lui-même.
- Le rendu lit decors/film.blend SUR LE DISQUE : enregistrer avant de lancer.
"""
import json, os, pathlib, subprocess, sys, time
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import reglages as R
import plans


def manquantes(a, z, dossier):
    return [i for i in range(a, z + 1) if not R.image(i, dossier).exists()]


def vivant(pid):
    """Le processus `pid` existe-t-il ? (Sous Windows, os.kill(pid, 0) le tuerait : on passe par tasklist.)"""
    if not pid:
        return False
    if os.name == "nt":
        r = subprocess.run(["tasklist", "/FI", f"PID eq {pid}", "/NH"], capture_output=True, text=True)
        return str(pid) in r.stdout
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


def verrou(dossier):
    return pathlib.Path(dossier) / ".verrou"


def arret(dossier):
    return pathlib.Path(dossier) / "ARRET"


def boucle_active(dossier):
    """PID de la boucle qui tourne dans ce dossier, ou 0."""
    v = verrou(dossier)
    if not v.exists():
        return 0
    try:
        pid = json.loads(v.read_text())["boucle"]
    except Exception:
        return 0
    return pid if vivant(pid) else 0


def option(args, nom, defaut=None):
    return args[args.index(nom) + 1] if nom in args else defaut


def lancer(script, args, ouvrir=True):
    cmd = R.commande_blender(script, args, ouvrir)
    env = dict(os.environ, EPISODE_RACINE=str(R.RACINE), EPISODE_PROFIL=R.PROFIL, PYTHONIOENCODING="utf-8")
    return subprocess.Popen(cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace")


def suivre(proc, filtre=None, dossier=None):
    """Affiche les lignes utiles du processus ; s'arrête si le fichier ARRET apparaît. Renvoie le code de sortie."""
    import threading
    def lire():
        for ligne in proc.stdout:
            ligne = ligne.rstrip()
            if filtre is None or any(m in ligne for m in filtre):
                print("   ", ligne, flush=True)
    t = threading.Thread(target=lire, daemon=True)
    t.start()
    while proc.poll() is None:
        if dossier and arret(dossier).exists():
            print("ARRET demandé : fin de Blender", flush=True)
            proc.terminate()
            try:
                proc.wait(15)
            except subprocess.TimeoutExpired:
                proc.kill()
            break
        time.sleep(0.5)
    t.join(2)
    return proc.wait()


def rendre(a, z, dossier, pct=100, plantage=0, profil=None):
    dossier = pathlib.Path(dossier)
    dossier.mkdir(parents=True, exist_ok=True)
    if not R.BLEND.exists():
        raise SystemExit(f"{R.BLEND} absent : lancer d'abord  python outils/rendre.py --construire")
    pid = boucle_active(dossier)
    if pid:
        raise SystemExit(f"Une boucle de rendu tourne déjà (processus {pid}). Un seul Blender à la fois.\n"
                         "Pour l'arrêter :  python outils/rendre.py --arreter")
    if arret(dossier).exists():
        arret(dossier).unlink()
    if pct != 100:
        print(f"ESSAI à {pct} % : ces images ne sont pas livrables (le film se rend à 100 %, sans agrandir ensuite).")
    debut, sans_progres, reprises = time.time(), 0, 0
    au_depart = len(manquantes(a, z, dossier))
    try:
        for essai in range(1, R.ESSAIS_MAX + 1):
            m = manquantes(a, z, dossier)
            print(f"essai {essai} : {len(m)} images à rendre ({time.strftime('%H:%M:%S')})", flush=True)
            if not m or arret(dossier).exists():
                break
            args = [a, z, "--pct", pct, "--dossier", dossier] + (["--plantage", plantage] if plantage else []) + (["--profil", profil] if profil else [])
            proc = lancer("bl_plage.py", args)
            verrou(dossier).write_text(json.dumps({"boucle": os.getpid(), "blender": proc.pid}))
            code = suivre(proc, ("Error", "Erreur", "Segmentation", "ESSAI", "bl_plage", "Traceback"), dossier)
            reste = len(manquantes(a, z, dossier))
            if code != 0 and reste and not arret(dossier).exists():
                reprises += 1
                print(f"    Blender s'est arrêté (code {code}) : reprise", flush=True)
            sans_progres = sans_progres + 1 if reste == len(m) else 0
            if sans_progres >= 3:
                print("ARRÊT : trois essais de suite sans aucune image nouvelle. Lire l'erreur ci-dessus (scène, chemin, pilote).")
                break
    finally:
        if verrou(dossier).exists():
            verrou(dossier).unlink()
    reste = manquantes(a, z, dossier)
    faites = au_depart - len(reste)
    duree = time.time() - debut
    print(f"RENDU {'TERMINÉ' if not reste else 'INCOMPLET'} ({time.strftime('%H:%M:%S')}) : {faites} images en {duree:.0f} s"
          + (f", soit {duree / faites:.2f} s par image" if faites else "") + f", {reprises} reprise(s), {len(reste)} manquante(s)")
    return not reste


def arreter(dossier):
    pid = boucle_active(dossier)
    if not pid:
        for f in (verrou(dossier), arret(dossier)):
            if f.exists():
                f.unlink()
        print("Aucune boucle de rendu active dans", dossier)
        return
    arret(dossier).write_text("arrêt demandé\n")
    print(f"Arrêt demandé à la boucle {pid} (elle arrête elle-même son Blender)…")
    for _ in range(120):
        if not boucle_active(dossier):
            break
        time.sleep(0.5)
    if boucle_active(dossier):
        print("La boucle ne répond pas. Fermer SA fenêtre de terminal ; ne pas arrêter des processus par leur nom.")
    else:
        if arret(dossier).exists():
            arret(dossier).unlink()
        print("Boucle arrêtée, plus aucun rendu en cours. Images présentes :", len(list(pathlib.Path(dossier).glob(f"{R.PREFIXE}*.{R.EXT}"))))


def profiler():
    """Rend quelques images à pleine taille et annonce la durée du film AVANT de lancer le rendu complet."""
    P = plans.P
    choix = P if len(P) <= 6 else [P[round(i * (len(P) - 1) / 5)] for i in range(6)]
    images = ",".join(str((p["a"] + p["b"]) // 2) for p in choix)
    proc = lancer("bl_cli.py", ["images", "profil_", 100, images])
    temps = []
    for ligne in proc.stdout:
        if "s/image" in ligne:
            temps.append(float(ligne.split(" en ")[1].split()[0]))
            print("   ", ligne.rstrip(), flush=True)
        elif "Error" in ligne or "Traceback" in ligne:
            print("   ", ligne.rstrip(), flush=True)
    proc.wait()
    if not temps:
        raise SystemExit("aucune image rendue : relancer avec  python outils/rendre.py --controle images x_ 100 0  pour lire l'erreur")
    moy = sum(temps) / len(temps)
    total = moy * plans.TOTAL
    print(f"profil « {R.PROFIL} » : {moy:.2f} s par image en moyenne (de {min(temps):.2f} à {max(temps):.2f}) sur {len(temps)} images")
    print(f"film de {plans.TOTAL} images : environ {total / 60:.0f} min de rendu ({total / 3600:.1f} h), sans compter les reprises")
    print("Au-delà de 2 s par image, alléger avant de lancer : voir le skill blender, references/rendu-long-et-fiable.md")


if __name__ == "__main__":
    args = sys.argv[1:]
    dossier = pathlib.Path(option(args, "--dossier", R.RENDUS))
    if "--arreter" in args:
        arreter(dossier)
    elif "--construire" in args:
        if boucle_active(dossier):
            raise SystemExit("Un rendu est en cours : l'arrêter avant de reconstruire la scène (python outils/rendre.py --arreter).")
        sys.exit(suivre(lancer("bl_film.py", [x for x in args if x != "--construire"], ouvrir=False),
                        ("cadre", "film construit", "enregistré", "GLISSEMENT", "Error", "Traceback", "réglage ignoré", "absent")))
    elif "--controle" in args:
        sys.exit(suivre(lancer("bl_cli.py", args[args.index("--controle") + 1:]), ("écrit", "terminé", "Error", "Traceback", "inconnu")))
    elif "--profiler" in args:
        profiler()
    else:
        nums = []
        i = 0
        while i < len(args):                    # les nombres nus sont les bornes ; ceux qui suivent une option lui appartiennent
            if args[i].startswith("--"):
                i += 2
            else:
                nums.append(int(args[i]))
                i += 1
        a, z = (nums + [0, plans.TOTAL - 1])[:2] if len(nums) >= 2 else (0, plans.TOTAL - 1)
        ok = rendre(a, z, dossier, int(option(args, "--pct", 100)), int(option(args, "--simuler-plantage", 0)), option(args, "--profil"))
        sys.exit(0 if ok else 1)
