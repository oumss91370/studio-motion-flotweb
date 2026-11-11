"""Où en est le rendu ? Une ligne, ou une ligne toutes les 3 minutes avec --boucle.

  python outils/suivi.py [--boucle] [--dossier chemin]
"""
import pathlib, sys, time
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import reglages as R
import plans, rendre


def etat(dossier):
    fichiers = [f for f in pathlib.Path(dossier).glob(f"{R.PREFIXE}*.{R.EXT}")]
    n = len(fichiers)
    recents = sum(1 for f in fichiers if time.time() - f.stat().st_mtime < 180)
    actif = rendre.boucle_active(dossier)
    reste = plans.TOTAL - n
    eta = f", fin dans environ {reste / (recents / 180) / 60:.0f} min" if recents and reste > 0 else ""
    print(f"{time.strftime('%H:%M')} : {n} / {plans.TOTAL} images (+{recents} en 3 min){eta} ; boucle de rendu : {'active' if actif else 'ARRÊTÉE'}", flush=True)
    return n, actif


if __name__ == "__main__":
    dossier = rendre.option(sys.argv, "--dossier", R.RENDUS)
    while True:
        n, actif = etat(dossier)
        if "--boucle" not in sys.argv or n >= plans.TOTAL or not actif:
            break
        time.sleep(180)
