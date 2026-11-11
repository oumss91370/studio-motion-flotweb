"""Réglages de l'épisode : le seul fichier à ouvrir pour changer un chemin, un format ou un profil de rendu.

Importé par tous les autres outils, y compris ceux qui tournent dans Blender (bibliothèque standard seulement).
Tous les chemins sont relatifs au dossier de l'épisode : le dossier qui contient `outils/`.
"""
import os, pathlib, shutil, sys, glob

# ----------------------------------------------------------------- dossier de l'épisode
OUTILS = pathlib.Path(__file__).resolve().parent
RACINE = pathlib.Path(os.environ.get("EPISODE_RACINE", OUTILS.parent)).resolve()

# ----------------------------------------------------------------- format (ne pas changer sans raison)
LARGEUR, HAUTEUR, IPS = 1080, 1920, 30

# ----------------------------------------------------------------- dossiers et fichiers
BLEND = RACINE / "decors" / "film.blend"        # tout le film dans une seule scène Blender
RENDUS = RACINE / "rendus"                      # f_0000.jpg, f_0001.jpg… (numéro = image de la vidéo)
PREFIXE, EXT, CHIFFRES = "f_", "jpg", 4
REVUE = RACINE / "revue"
PERSONNAGES = RACINE / "personnages"
VOIX = RACINE / "voix"                          # voix.wav, mots.json, texte.txt
SON = RACINE / "son"                            # reperes.json, design.json, mix.wav
HF = RACINE / "hf"                              # projet HyperFrames
SORTIE = RACINE / "sortie"
A_SUPPRIMER = RACINE / "_a_supprimer"           # on ne supprime jamais : on déplace ici, la personne supprime

# ----------------------------------------------------------------- rendu
# Profil : "integree" (carte graphique intégrée), "dediee" (carte dédiée), "processeur" (Cycles sans carte).
# Les valeurs « integree » sont celles du rendu réel du 11/11/2026 (3,6 s par image en 1080×1920).
PROFIL = os.environ.get("EPISODE_PROFIL", "integree")
PROFILS = {
    "integree":   dict(moteur="EEVEE",  echantillons=8,  ombres=0.5, portee_lumieres=11.0, brume=True),
    "dediee":     dict(moteur="EEVEE",  echantillons=32, ombres=1.0, portee_lumieres=None, brume=True),
    "processeur": dict(moteur="CYCLES", echantillons=16, ombres=1.0, portee_lumieres=None, brume=False),
}
VUE = "Standard"            # « Standard » : les aplats des personnages sortent à la couleur du dessin (AgX les grise)
QUALITE_JPEG = 96
ESSAIS_MAX = 40             # nombre de relances de la boucle de rendu après plantage

# ----------------------------------------------------------------- composition verticale
SUJET_BAS_MAX = 0.65        # le sujet tient dans les 65 % du haut de l'image (sinon les sous-titres le couvrent)
SOUS_TITRES = dict(haut=1385, hauteur=130,     # bande y = 1385 à 1515, dans la zone utile (jusqu'à y = 1560)
                   taille=96, police="Montserrat", graisse=900,
                   couleur="#ffffff", contour="#15100c", contour_px=18,
                   lettres_max_paire=10)       # un petit mot se colle au mot plein qui suit si l'ensemble tient

# ----------------------------------------------------------------- son
CIBLE_LUFS = -14.0
BRUITAGES_PAR_10S = (1.0, 2.0)   # histoire narrée : 1 à 2 par 10 s


def image(n, dossier=None):
    """Chemin du fichier de l'image n."""
    return (dossier or RENDUS) / f"{PREFIXE}{n:0{CHIFFRES}d}.{EXT}"


def trouver_blender():
    """Chemin du programme Blender, ou None. Ordre : variable BLENDER, PATH, emplacements habituels."""
    cand = [os.environ.get("BLENDER"), shutil.which("blender"), shutil.which("blender.exe")]
    cand += sorted(glob.glob(r"C:\Program Files\Blender Foundation\Blender*\blender.exe"), reverse=True)
    cand += ["/Applications/Blender.app/Contents/MacOS/Blender"]
    cand += sorted(glob.glob(os.path.expanduser("~/blender*/blender")), reverse=True)
    for c in cand:
        if c and pathlib.Path(c).is_file():
            return str(c)
    return None


def module_bpy():
    """Vrai si le module Python `bpy` est installé pour ce Python (Blender sans interface)."""
    import importlib.util
    return importlib.util.find_spec("bpy") is not None


def commande_blender(script, args=(), ouvrir=True):
    """Commande qui exécute `script` dans Blender sans interface.

    Avec le programme Blender : blender -b film.blend --python script -- args
    Sans lui, avec le module bpy : python script -- args (le script ouvre lui-même film.blend).
    """
    script = str(OUTILS / script)
    exe = trouver_blender()
    if exe:
        return [exe, "-b"] + ([str(BLEND)] if ouvrir and BLEND.exists() else []) + ["--python", script, "--"] + [str(a) for a in args]
    if module_bpy():
        return [sys.executable, script, "--"] + [str(a) for a in args]
    raise SystemExit("Blender introuvable : installer Blender, ou donner son chemin dans la variable BLENDER "
                     "(exemple Windows : set BLENDER=C:\\Program Files\\Blender Foundation\\Blender 5.3\\blender.exe).")


def arguments():
    """Arguments du script, qu'il soit lancé par Blender (après « -- ») ou par Python."""
    return sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]


if __name__ == "__main__":
    print("épisode  :", RACINE)
    print("blender  :", trouver_blender() or ("module bpy" if module_bpy() else "INTROUVABLE"))
    print("profil   :", PROFIL, PROFILS[PROFIL])
    print("format   :", LARGEUR, "x", HAUTEUR, "à", IPS, "i/s")
