"""Re-rend seulement des plages d'images, puis le film se recolle tout seul (mêmes noms de fichiers).

  python outils/refaire.py <etiquette> A-B [A-B …] [--pct 25] [--dossier chemin]
  python outils/refaire.py tour1 914-983 1242-1287

Les anciennes images des plages sont DÉPLACÉES dans _a_supprimer/<etiquette>/ (jamais supprimées : on peut revenir
en arrière, et la personne supprime elle-même le dossier), puis `rendre.py` comble les trous de tout le film.
Avant de lancer : corriger bl_film.py, puis  python outils/rendre.py --construire  (le rendu lit le fichier sur le disque).
Une correction = le plan entier qu'elle touche : relire les bornes dans plans.md.
"""
import pathlib, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import reglages as R
import plans, rendre

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 2:
        raise SystemExit(__doc__)
    etiquette = args[0]
    dossier = pathlib.Path(rendre.option(args, "--dossier", R.RENDUS))
    if rendre.boucle_active(dossier):
        raise SystemExit("Un rendu est en cours : l'arrêter d'abord (python outils/rendre.py --arreter).")
    plages = []
    for x in args[1:]:
        if x.startswith("--"):
            break
        a, b = (int(v) for v in x.split("-"))
        if not 0 <= a <= b < plans.TOTAL:
            raise SystemExit(f"plage {x} hors du film (0 à {plans.TOTAL - 1})")
        plages.append((a, b))
    corbeille = R.A_SUPPRIMER / etiquette
    corbeille.mkdir(parents=True, exist_ok=True)
    n = 0
    for a, b in plages:
        for i in range(a, b + 1):
            f = R.image(i, dossier)
            if f.exists():
                cible = corbeille / f.name
                k = 1
                while cible.exists():              # même étiquette réutilisée : ne rien écraser
                    k += 1
                    cible = corbeille / f"{f.stem}_v{k}{f.suffix}"
                shutil.move(str(f), str(cible))
                n += 1
    print(f"{n} anciennes images déplacées dans {corbeille}")
    ok = rendre.rendre(0, plans.TOTAL - 1, dossier, int(rendre.option(args, "--pct", 100)), 0, rendre.option(args, "--profil"))
    sys.exit(0 if ok else 1)
