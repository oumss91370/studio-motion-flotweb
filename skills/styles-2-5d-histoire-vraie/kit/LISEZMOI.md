# Kit de départ 2.5D « histoire vraie »

Des outils prêts à copier dans le dossier d'un épisode : **un script, une liste de plans, un décor ou deux, un objet héros**, et le film sort. Ils viennent d'un film réel de 61,5 s (36 plans, 1 845 images) produit par le studio le 11/11/2026, dont on a retiré tout ce qui lui était propre. Ce film d'origine est un essai interne : il n'est ni publié ni fourni.

Le kit contient un **exemple neutre** qui tourne tel quel (2 plans, 3 s) : un personnage d'exemple, « Galet », appuie sur une sonnette dans un atelier. Tout ce qui est marqué `EXEMPLE NEUTRE À REMPLACER` est à vous de refaire : votre histoire, votre personnage, votre décor.

> **Votre chaîne, votre dessin.** Choisissez vos propres sujets et dessinez un personnage original. Ne reprenez jamais le dessin, les sujets ni la grammaire reconnaissable d'une chaîne existante. Galet lui-même n'est qu'un exemple : une chaîne qui le garderait ressemblerait à toutes celles qui ont pris ce kit.

## Ce qu'il faut sur la machine

| Outil | Pour quoi | Remarque |
|---|---|---|
| Python 3.10 ou plus récent, avec `pillow` et `numpy` | tous les scripts | `pip install pillow numpy` |
| Blender 4.2 ou plus récent | construire et rendre | le programme `blender` (trouvé tout seul, ou chemin dans la variable `BLENDER`), **ou** le module Python `bpy` (`pip install bpy`) |
| ffmpeg et ffprobe | encodage, planches, son | dans le `PATH` |
| Node.js et HyperFrames 0.9.33 | assemblage final | skill `rendu` |

Windows, macOS et Linux : tous les outils sont en Python, sans script `.sh`. Sous Windows, si `blender` n'est pas trouvé : `set BLENDER=C:\Program Files\Blender Foundation\Blender 5.3\blender.exe` (PowerShell : `$env:BLENDER = "…"`).

## Installer le kit dans un épisode

Copier le contenu de ce dossier dans `<episode>/outils/`. Tous les chemins sont relatifs au dossier de l'épisode (le dossier qui contient `outils/`). Pour l'exemple, copier aussi `exemple/voix/` dans `<episode>/voix/`.

```
<episode>/
  outils/            ce kit
  script.md          le texte de la voix                  (à écrire)
  sources.md         le tableau fait par fait             (à écrire)
  plans.md           la liste de plans lisible            (écrit par plans.py)
  personnages/       svg/, png/, rig.json                 (écrits par personnages.py)
  decors/film.blend  tout le film dans une scène          (écrit par bl_film.py)
  rendus/            f_0000.jpg, f_0001.jpg…              (écrits par rendre.py)
  voix/              voix.wav, mots.json, texte.txt, accents.txt
  son/               reperes.json, design.json, mix.wav
  hf/                le projet HyperFrames                (écrit par hf_build.py)
  revue/             planches, images pleine taille, consigne de critique
  sortie/            la vidéo finale
  _a_supprimer/      ce que les outils ont écarté (ils ne suppriment jamais rien)
```

## L'ordre des étapes

Toutes les commandes se lancent depuis le dossier de l'épisode. `python` peut s'appeler `python3` ou `py` selon la machine.

| # | Étape | Commande | Ce qu'on regarde avant de continuer |
|---|---|---|---|
| 0 | Vérifier la machine | `python outils/reglages.py` | Blender trouvé, bon profil de rendu |
| 1 | Liste de plans | `python outils/plans.py` | aucune erreur de bornes ; lire `plans.md` |
| 2 | Personnages | `python outils/personnages.py` | `revue/personnages-expressions.png` |
| 3 | Décor, passe 1 | `python outils/rendre.py --construire --passe 1` puis `python outils/rendre.py --controle planche passe1_ 25` puis `python outils/planche.py revue/passe1.jpg 6 270 "revue/tmp/passe1_*.jpg"` | échelle, cadres, lignes « cadre … ok » |
| 4 | Passe 2 (lumière) | idem avec `--passe 2` | ni blanc brûlé ni noir bouché |
| 5 | Objet héros seul | `python outils/rendre.py --controle tour heros_ 25` puis planche | les 6 angles |
| 6 | Passe 3 (matières, flou) | `python outils/rendre.py --construire` puis une planche de tous les plans | la planche entière |
| 7 | Profilage | `python outils/rendre.py --profiler` | secondes par image, durée annoncée du film |
| 8 | Rendu | `python outils/rendre.py` (suivi : `python outils/suivi.py --boucle` dans un autre terminal) | « RENDU TERMINÉ », 0 manquante |
| 9 | Voix | enregistrer `voix/voix.wav`, produire `voix/mots.json`, puis `python outils/ecart_voix.py` | écart médian et dispersion |
| 10 | Son | écrire `son/design.json`, puis `python outils/mix.py` | LUFS, crête, bruitages par 10 s |
| 11 | Assemblage | `python outils/hf_build.py`, puis dans `hf/` : `npx -y hyperframes@0.9.33 lint`, `check`, `render -o ../sortie/episode.mp4` (skill `rendu`) ; puis le niveau final avec `finaliser.py` du skill `son` | le MP4 dans `sortie/` : 1080×1920, 30 i/s, durée prévue, −14 LUFS **mesurés sur le MP4** |
| 12 | Revue | `python outils/revue.py sortie/episode.mp4 tour1` | « Vérifié : toutes les images existent » avant d'envoyer la consigne à un relecteur |
| 13 | Corrections | corriger `bl_film.py`, `python outils/rendre.py --construire`, `python outils/refaire.py tour1 A-B …`, puis étapes 11 et 12 | les seuls plans touchés sont re-rendus |

Arrêter un rendu : `python outils/rendre.py --arreter`. Jamais en tuant Blender (voir « Trois règles »).

## Ce que fait chaque fichier

| Fichier | Rôle | On le modifie ? |
|---|---|---|
| `reglages.py` | Chemins, format, profil de rendu (`integree`, `dediee`, `processeur`), bande des sous-titres, budget de bruitages. Trouve Blender. | oui : le profil |
| `plans.py` | **La liste de plans en données** : bornes en numéros d'image, mots couverts, décor, caméra et sa raison, personnage, objet, son, ligne de jeu ; temps clés ; repères sonores. Vérifie que les bornes se suivent. Écrit `plans.md` et `son/reperes.json`. | oui : entièrement |
| `personnages.py` | Dessine les pièces du pantin (SVG + PNG ×2), les visages échangeables, `rig.json` et deux planches. Une seule vue : de face. | oui : le dessin |
| `bl_lib.py` | Bibliothèque sans rien de propre à un film : formes biseautées, objet tourné, matières à variation, argile des passes 1 et 2, lumière motivée, vacillement, plans émissifs, ombre de contact, pantin (`Perso`), une caméra par plan, chute réelle, réglages de rendu, contrôles de cadre et de glissement. | non (sauf pour ajouter une forme ou une vue) |
| `bl_film.py` | **Le film** : décor, objet héros, caméras, animation plan par plan. Vide le fichier Blender courant puis enregistre `decors/film.blend`. | oui : entièrement |
| `bl_cli.py` | Rendus de contrôle à basse résolution : une image par plan, des images choisies, l'objet héros sous 6 angles. | non |
| `bl_plage.py` | Rend une plage en sautant les images déjà faites. Appelé par `rendre.py`. | non |
| `rendre.py` | La boucle de rendu avec reprise, le verrou « un seul Blender », l'arrêt propre, le profilage, et les raccourcis `--construire` et `--controle`. | non |
| `refaire.py` | Re-rend des plages d'images : déplace les anciennes dans `_a_supprimer/<etiquette>/`, puis comble les trous. Le film se recolle tout seul (mêmes noms de fichiers). | non |
| `suivi.py` | Avancement du rendu, cadence, fin estimée, boucle active ou non. | non |
| `planche.py` | Assemble des images en une planche, le nom sous chaque vignette. | non |
| `ecart_voix.py` | Mesure l'écart entre les repères de mots et le vrai début de la parole, sur la forme d'onde. | non |
| `mix.py` | Mixe voix, musique, ambiances et bruitages d'après `son/design.json` : attaque sur l'image, niveau relatif au fond, −14 LUFS. | non |
| `hf_build.py` | Encode les images en `hf/assets/film.mp4` et écrit le projet HyperFrames avec les sous-titres au mot. | la liste `OUTILS` si la langue change |
| `revue.py` | Planche contact, planche « téléphone », trois images pleine taille par plan, **vérification qu'elles existent**, consigne de critique avec les 9 questions. | les questions, si le format change |
| `exemple/voix/` | Horodatage d'exemple écrit à la main (il n'y a pas de voix d'exemple). | à remplacer |

## Ce qu'on change pour un nouvel épisode

1. **`plans.py`** : `TOTAL`, la liste `P` (un plan par idée, bornes calées sur le début des mots), `TEMPS_CLES`, `REPERES`. Relancer : il refuse des bornes qui ne se suivent pas.
2. **`personnages.py`** : `PERSOS` (couleurs, hauteur) et la fonction `pieces()` (le dessin). Garder les noms des pièces (`jambes`, `corps`, `bras_g`, `bras_d`, `tete`) et les familles de visages (`yeux_…`, `bouche_…`, `extra_…`) : `bl_lib.py` s'appuie dessus.
3. **`bl_film.py`**, entre `LE FILM` et `FIN DU FILM` : les matières, le ou les décors, l'objet héros (dans la collection `HEROS`), les caméras (`L.camera(id, a, b, …)` avec les bornes de `plans.py`), puis l'animation plan par plan. Garder l'en-tête et le bloc de contrôles de la fin, en y mettant vos objets.
4. **`voix/`** : `voix.wav`, `mots.json`, `texte.txt` (une réplique par ligne), `accents.txt` (les mots qui reçoivent le léger « pop » : 2 à 4 par phrase).
5. **`son/design.json`** : modèle en tête de `mix.py`.
6. **`reglages.py`** : `PROFIL` selon la carte graphique. Rien d'autre en général.

Les gestes d'animation à connaître dans `bl_film.py` :

| Besoin | Appel |
|---|---|
| Poser un personnage au début d'un plan | `p.place(a, x, y, vers=(x_camera, y_camera))`, `p.neutre(a)`, `p.visage(a, "neutre", "fermee", None)` |
| Le sortir du film | `p.range_(a)` |
| Un regard, puis un geste tenu | `p.visage(f, yeux="cote")`, `p.tete_(f, dx=14)`, puis `p.geste(f, "d", 0, 62)` |
| Un déplacement | `p.deplace(f0, f1, x=…)` : **la clé d'arrivée est tenue**. Ne pas poser les clés de position à la main. |
| Une chute réelle | `L.chute(objet, f_depart, z0, z1)` renvoie l'image du contact : y poser le son |
| Une clé quelconque | `L.K(objet, "location", f, valeur, "CONSTANT", axe)` ; `CONSTANT` = tenue jusqu'à la clé suivante |

## Trois règles qui évitent les ennuis

1. **Un seul Blender qui rend à la fois.** `rendre.py` pose un verrou et refuse une deuxième boucle. Deux rendus en parallèle font planter une carte graphique intégrée et mélangent les images de deux versions de la scène.
2. **Pour arrêter : `python outils/rendre.py --arreter`.** Si l'on tue Blender seul, la boucle le relance aussitôt (« boucle fantôme »). Et ne jamais arrêter « tout ce qui s'appelle blender » : on tue aussi le pont du connecteur MCP.
3. **Le connecteur MCP construit, la ligne de commande rend.** Par le connecteur : exécuter `bl_film.py` dans un fichier Blender **vide**, regarder, enregistrer. Les rendus de plus de quelques images passent par `rendre.py`. Détail : skill `blender`, `references/rendu-long-et-fiable.md`.

Pour exécuter `bl_film.py` par le connecteur (`execute_blender_code`), dans un fichier vide :

```python
import runpy, sys
sys.argv = ["blender", "--", "--passe", "3"]
runpy.run_path(r"<chemin complet de l'épisode>/outils/bl_film.py", run_name="__main__")
```

## Ce que le kit ne fait pas

- **Une seule vue du personnage** : de face. Pas de trois quarts, de profil ni de dos ; pas de main qui pointe ; pas de cycle de marche (`marche()` n'est qu'un petit rebond du tronc). Voir le skill `personnages`, `references/limites-du-pantin.md`.
- **Pas de textures réelles** : les matières sont procédurales. Avec Poly Haven activé dans le connecteur, importer des textures et un HDRI (skill `blender`).
- **Pas de brume volumétrique** dans l'exemple.
- **Pas d'alignement de la voix** : `voix/mots.json` vient d'ailleurs (faster-whisper ou alignement forcé ; voir `references/pipeline.md`, étape 6). `ecart_voix.py` ne fait que contrôler.
- **Le contrôle « aucun double de l'objet héros dans le cadre »** n'est pas automatique : il se fait à l'œil sur la planche, et la consigne de critique le demande.
- Les contrôles de cadre mesurent des boîtes englobantes : ils préviennent, ils ne remplacent pas la planche.

## Ce qui a été essayé

L'exemple a été construit, rendu (à un quart de la taille, donc non livrable), assemblé avec HyperFrames et passé en revue lors de l'écriture du kit (11/11/2026), sur une machine Linux sans carte graphique, avec le module `bpy` 5.3. Le détail de ce qui a tourné et de ce qui n'a pas pu être essayé (programme `blender` en ligne de commande, connecteur MCP, Windows, macOS, carte graphique) est dans `references/pipeline.md`, section « Ce qui a été essayé pour de vrai ».
