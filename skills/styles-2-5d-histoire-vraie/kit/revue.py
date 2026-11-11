"""Planches de revue d'une version du film, et consigne pour la critique.

  python outils/revue.py <video.mp4> <etiquette>          exemple :  python outils/revue.py sortie/episode.mp4 tour1

Écrit dans revue/ :
  <etiquette>-contact.jpg      une image par seconde, toute la vidéo sur une planche
  <etiquette>-telephone.jpg    une image toutes les 3 s, à 360 px de large (ce qu'on lit vraiment sur un téléphone)
  <etiquette>-plein/           trois images PLEINE TAILLE par plan (début, milieu, fin), sous-titres compris
  <etiquette>-consigne-critique.md   la consigne à donner à un relecteur qui n'a PAS fabriqué le film

Le script VÉRIFIE que les images pleine taille existent, ne sont pas vides et ont la taille de la vidéo. Il sort en
erreur sinon : au premier tour du rendu réel du 11/11/2026, l'extraction avait échoué en silence, le dossier était
vide et la critique a jugé des rendus bruts sans sous-titres.
"""
import json, math, pathlib, subprocess, sys
from PIL import Image
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import reglages as R
import plans

QUESTIONS = [
    "L'action centrale de l'histoire se voit-elle ? Le sujet est de face ou de profil franc, rien ne le cache, il est assez grand dans le cadre.",
    "Un double de l'objet héros (une autre bille, une autre porte, un autre exemplaire) reste-t-il dans le cadre et contredit-il l'action ?",
    "Quelque chose d'important est-il coupé par un bord ou placé dans une zone d'interface : objet, personnage, bras tendu ? Le sujet tient-il dans les 65 % du haut ?",
    "Un personnage glisse-t-il au lieu de s'arrêter, ou part-il vers sa place du plan suivant avant la coupe ?",
    "Chaque personnage est-il posé au sol (ombre de contact) et plat (aucun ombrage du décor) ? Ce qui est tenu touche-t-il la main ? Rien ne flotte, rien ne dépasse d'un meuble ?",
    "Le jeu se lit-il ? Un regard précède chaque geste, les pupilles visent l'objet, aucun trait du dessin (barbe, sourcil, col) ne se lit à contresens de l'émotion, aucun rebond en boucle.",
    "Les sous-titres : couvrent-ils un visage, l'objet héros ou une action ? Ont-ils tous la même taille ? Se lisent-ils sur la planche « téléphone » ? Disent-ils exactement la voix ?",
    "L'image de chaque plan se lit-elle d'un coup d'œil : profondeur (plusieurs couches), silhouette, ni blanc brûlé ni noir bouché, pas de motif en damier ni de tramage, pas deux plans voisins au même cadrage, aucun plan de plus de 3 s sans idée nouvelle ?",
    "Depuis le tour précédent : chaque correction est-elle faite, et a-t-elle cassé autre chose dans le même plan (un personnage sorti du cadre après un recadrage, par exemple) ?",
]


def sonde(video):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,avg_frame_rate,nb_frames:format=duration",
                        "-of", "json", str(video)], capture_output=True, text=True, check=True)
    j = json.loads(r.stdout)
    st = j["streams"][0]
    return st["width"], st["height"], st["avg_frame_rate"], float(j["format"]["duration"])


def ff(*args):
    subprocess.run(["ffmpeg", "-y", "-v", "error", *[str(a) for a in args]], check=True)


def main(video, etiquette):
    video = pathlib.Path(video)
    if not video.exists():
        raise SystemExit(f"vidéo introuvable : {video}")
    R.REVUE.mkdir(parents=True, exist_ok=True)
    w, h, ips, duree = sonde(video)
    n1 = max(1, math.ceil(duree))
    contact = R.REVUE / f"{etiquette}-contact.jpg"
    ff("-i", video, "-vf", f"fps=1,scale=240:-1,tile=8x{math.ceil(n1 / 8)}:padding=4:color=black", "-frames:v", 1, "-q:v", 3, contact)
    n3 = max(1, math.ceil(duree / 3))
    telephone = R.REVUE / f"{etiquette}-telephone.jpg"
    ff("-i", video, "-vf", f"fps=1/3,scale=360:-1,tile={min(6, n3)}x{math.ceil(n3 / 6)}:padding=4:color=black", "-frames:v", 1, "-q:v", 3, telephone)

    plein = R.REVUE / f"{etiquette}-plein"
    plein.mkdir(exist_ok=True)
    attendues = []
    for p in plans.P:
        for pos, f in (("a", p["a"] + 1), ("b", (p["a"] + p["b"]) // 2), ("c", p["b"] - 2)):
            f = min(max(f, p["a"]), p["b"] - 1)
            sortie = plein / f"p{p['id']:02d}{pos}_{f:0{R.CHIFFRES}d}.jpg"
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{(f + 0.25) / R.IPS:.4f}", "-i", str(video), "-frames:v", "1", "-q:v", "2", str(sortie)])
            attendues.append(sortie)

    # ---------- vérification AVANT d'envoyer à la critique
    pb = []
    for f in [contact, telephone] + attendues:
        if not f.exists() or f.stat().st_size < 1000:
            pb.append(f"absente ou vide : {f.relative_to(R.RACINE)}")
    for f in attendues:
        if f.exists() and f.stat().st_size >= 1000:
            with Image.open(f) as im:
                if im.size != (w, h):
                    pb.append(f"taille {im.size} au lieu de {(w, h)} : {f.name}")
    if (w, h) != (R.LARGEUR, R.HAUTEUR):
        pb.append(f"la vidéo fait {w}×{h} au lieu de {R.LARGEUR}×{R.HAUTEUR}")
    if abs(duree - plans.TOTAL / R.IPS) > 0.05:
        pb.append(f"la vidéo dure {duree:.2f} s, la liste de plans {plans.TOTAL / R.IPS:.2f} s")

    rel = lambda f: f.relative_to(R.RACINE).as_posix()
    L = [f"# Consigne de critique — {etiquette}", "",
         "Tu es le directeur d'animation le plus sévère qui soit, et **tu n'as pas fabriqué ce film**. Lecture seule : tu ne modifies rien.", "",
         "## Ce que tu regardes",
         f"- `{rel(contact)}` : une image par seconde.",
         f"- `{rel(telephone)}` : le film à la taille d'un téléphone.",
         f"- `{rel(plein)}/` : {len(attendues)} images pleine taille avec les sous-titres (trois par plan : `pNNa` début, `pNNb` milieu, `pNNc` fin ; le nombre final est le numéro d'image).",
         "- `plans.md` : ce que chaque plan devait montrer, et ses bornes en numéros d'image.",
         "- `sources.md` : la source de chaque affirmation.", "",
         "## Les 9 questions", ""]
    L += [f"{i}. {q}" for i, q in enumerate(QUESTIONS, 1)]
    L += ["", "## Ce que tu rends", "",
          "La liste de TOUS les problèmes, du plus grave au moins grave (ordre : ce qui est faux ou manquant, la lisibilité, le rythme, le détail). "
          "Pour chacun, quatre champs :", "",
          "| # | OÙ (plan, images) | PROBLÈME (ce qu'on voit, avec les nombres) | CHANGEMENT (la seule chose à modifier) | À GARDER (ce qui ne doit pas bouger) |",
          "|---|---|---|---|---|", "",
          "Désigne les trois pires. On en corrige trois par tour, on ne re-rend que les plans touchés, puis on te renvoie de nouvelles planches.",
          "Ne juge pas le son : tu ne l'entends pas. Ne propose pas de refaire le film."]
    consigne = R.REVUE / f"{etiquette}-consigne-critique.md"
    consigne.write_text("\n".join(L) + "\n", encoding="utf-8")

    print(f"vidéo : {w}×{h}, {ips} i/s, {duree:.3f} s")
    print(f"planches : {rel(contact)}, {rel(telephone)}")
    print(f"images pleine taille : {sum(1 for f in attendues if f.exists())} / {len(attendues)} dans {rel(plein)}/")
    print(f"consigne : {rel(consigne)}")
    if pb:
        print("\nNE PAS ENVOYER À LA CRITIQUE, corriger d'abord :")
        for x in pb:
            print("  -", x)
        raise SystemExit(1)
    print("Vérifié : toutes les images existent, à la taille de la vidéo. Ouvrir une image pleine taille soi-même avant d'envoyer.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    main(sys.argv[1], sys.argv[2])
