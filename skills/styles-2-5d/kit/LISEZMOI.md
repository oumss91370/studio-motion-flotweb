# Kit de production 2.5D

Des outils prêts à copier dans le dossier d'un film. Le kit contient **deux chaînes** :

| Chaîne | Pour quel style | Fichiers |
|---|---|---|
| **Chaîne mesurée** (celle-ci, à prendre par défaut) | `tete-ronde-trait-plein-delie` : personnages à trait plein et délié, décor 3D dessiné, lumière posée à l'assemblage | `regles.py`, `pantin.py`, `camera.py`, `plaque.py`, `film.py`, `bl_decor.py`, `bl_scene.py`, `compo.py`, `lancer.py`, `controle.py` |
| Chaîne à plans émissifs (plus ancienne) | `theatre-de-papier`, et tout style où le personnage est un plan posé dans Blender | `plans.py`, `personnages.py`, `bl_lib.py`, `bl_film.py`, `bl_cli.py`, `bl_plage.py`, `rendre.py`, `refaire.py`, `suivi.py` (voir « L'ancienne chaîne » en bas de page) |
| Communs | les deux | `reglages.py`, `mix.py`, `ecart_voix.py`, `hf_build.py`, `revue.py`, `planche.py` |

Les règles du style sont dans `references/prompt-maitre.md` ; les mêmes valeurs sont en données dans `regles.py`. **Aucun personnage n'est fourni** : vous décrivez les vôtres, le kit les dessine.

> **Vos sujets, votre dessin.** L'exemple (une gardienne de phare attend une lettre, le facteur arrive) est un sujet inventé pour ce kit : il est à remplacer en entier. Ne reprenez jamais un personnage, un costume, un décor ni un sujet d'une chaîne existante.

## Ce qu'il faut sur la machine

| Outil | Pour quoi | Remarque |
|---|---|---|
| Python 3.10 ou plus récent | tous les scripts | `pip install pillow numpy opencv-python resvg-py` |
| Blender 4.2 ou plus récent (essayé avec 5.3) | les trois passes du décor | trouvé tout seul, ou chemin dans la variable `BLENDER` |
| ffmpeg | encodage | dans le `PATH` |
| Une police grasse | sous-titres | Montserrat Black de préférence ; déposez le fichier `.ttf` dans `<film>/polices/`. Sinon le kit prend une police grasse du système |
| Le skill `reproduire-reel` du plugin | `controle.py` s'appuie sur ses scripts de mesure | trouvé dans le plugin, ou dossier dans la variable `MESURE_SCRIPTS` |

## Installer le kit dans un film

Copier les fichiers de la chaîne mesurée et `reglages.py` dans `<film>/outils/`. Tout le reste est écrit par les outils.

```
<film>/
  outils/            le kit
  polices/           (facultatif) la police des sous-titres
  decors/decor.blend la scène, écrite par bl_scene.py
  passes/            albedo/, lum/, data/ : trois images par rendu (une image du film, ou la plaque d'un tronçon), écrites par Blender
  images/            f_0000.jpg… : les images finales, écrites par compo.py
  son/mix.wav        (facultatif) le son, ajouté à l'encodage
  sortie/film.mp4    le film
  controle/          le contrôle chiffré
  revue/             les planches de personnages
```

## L'ordre des étapes

Toutes les commandes se lancent depuis le dossier du film.

| # | Étape | Commande | Ce qu'on regarde avant de continuer |
|---|---|---|---|
| 1 | Décrire les personnages | modifier `PERSOS` dans `film.py`, puis `python outils/pantin.py` | `revue/personnages-distribution.png` (les quatre ambiances, face et trois quarts), `-expressions.png`, `-poses.png` |
| 2 | Construire les décors | modifier `bl_scene.py`, puis `python outils/lancer.py construire` | « construit : decor.blend », aucune matière manquante |
| 3 | Régler les caméras | modifier `PLANS` dans `film.py`, puis `python outils/lancer.py rendre A:0,A:60,B:150` et `python outils/compo.py A:0,A:60,B:150` | `images/A_0060.jpg` : cadrage, personnage posé, rien de nu derrière lui, aucun objet coupé par le cadre |
| 4 | **Montrer 3 ou 4 images au client** | les images de l'étape 3 | il les critique avant tout rendu long (règle de `studio-coeur`) |
| 5 | Écrire le jeu et les sous-titres | fonctions de jeu et `CARTONS` dans `film.py` | les durées de `regles.JEU` |
| 6 | Rendre | `python outils/lancer.py rendre` | « RENDU TERMINÉ » ; un rendu interrompu reprend où il s'était arrêté |
| 7 | Assembler | `python outils/lancer.py assembler` | `sortie/film.mp4` |
| 8 | Contrôler | `python outils/controle.py` | `controle/controle.md` : chaque ligne hors tolérance est corrigée ou expliquée |
| 9 | Critique indépendante | un agent qui n'a pas fait le film reçoit `references/prompt-maitre.md` et le film | sa note, telle quelle ; un tour de corrections ; nouvelle note |
| 10 | Son | `mix.py` (étapes du son dans `references/pipeline.md`), puis relancer l'étape 7 | −14 LUFS mesurés sur le MP4 |

`python outils/lancer.py tout` enchaîne les étapes 2, 6 et 7. `python outils/lancer.py etat` dit où en est le rendu ; `python outils/lancer.py arreter` l'arrête proprement. `python outils/lancer.py plans` affiche les tronçons de caméra de chaque plan et leur mode de rendu : à lancer avant l'étape 6.

**Changer une ambiance, une ombre, un contour, le flou, un personnage ou un sous-titre ne demande aucun rendu Blender** : écarter les images concernées de `images/` et relancer l'étape 7. Seul un changement de décor ou de caméra redemande les passes (écarter alors les fichiers du plan de `passes/`).

## Rendre vite : une plaque de décor par tronçon de caméra

Les personnages sont posés à l'assemblage : quand la caméra ne fait que dériver, le décor n'est rendu qu'**une fois** pour tout le tronçon (une « plaque »), puis recadré à chaque image. `plaque.py` coupe chaque plan aux stations de la caméra, classe chaque tronçon d'après sa parallaxe (de combien un objet proche glisse par rapport au lointain, en pixels) et réunit les tronçons voisins tant qu'elle reste sous le seuil. Rien à écrire : `lancer.py rendre` et `compo.py` s'en servent tout seuls.

| Mode | Quand | Ce que Blender rend |
|---|---|---|
| `fixe` | caméra immobile | une plaque |
| `plaque` | parallaxe de 12 px au plus | une plaque, recadrée par homographie |
| `couches` | parallaxe de 12 à 120 px | la même plaque, chaque pixel déplacé selon sa profondeur |
| `3d` | au-delà de 120 px, ou décor animé | chaque image |

| Pour… | On écrit |
|---|---|
| voir les tronçons, leur mode, la raison, la taille des plaques et le nombre de rendus | `python outils/lancer.py plans` |
| forcer le mode d'un plan | la clé `mode` du plan dans `film.py` : `mode="3d"` (ou `"couches"`, `"plaque"`, `"fixe"`) |
| dire qu'un objet du décor bouge dans un plan | la clé `anime=True` du plan : il est rendu image par image (sur une plaque, l'objet resterait figé) |
| tout rendre image par image | la variable d'environnement `EPISODE_MODE=3d` devant la commande de rendu et celle d'assemblage |

- Seuils et marges : `regles.PLAQUE` (12 et 120 px ; marge de champ de 4 % ; plaque de 2 fois le cadre au plus).
- À forcer en 3D : un plan où une ombre ou une lampe bouge ; un tronçon dont la parallaxe approche 120 px si l'on voit un étirement près d'un objet proche (validé image par image jusqu'à 112 px).
- Mesuré le 12/11/2026 sur 4 plans de test (256 images, décor de 3 656 objets réunis en 535) : 107 images en 3D et 5 plaques, 9,9 min au lieu de 22,6 (2,3 fois plus vite) ; une plaque : 6,1 s ; une image : 5,29 s. Méthode, écarts et limites : `references/rendu-rapide.md`.

## Ce que fait chaque fichier

| Fichier | Rôle | On le modifie ? |
|---|---|---|
| `regles.py` | Toutes les constantes du style : loi du contour, palettes des quatre ambiances, ombre au sol, contours et matières du décor, optique, sous-titres, durées du jeu, tolérances du contrôle. `essaye=False` marque une ambiance mesurée mais pas encore refaite chez nous. | non, sauf décision de style écrite |
| `pantin.py` | Le générateur de personnages : `definir()` reçoit vos fiches, `pose()` décrit une pose, `rendre()` dessine. Contour à pleins et déliés selon `lum`, palettes selon `amb`, tête à croissant et filet, coiffes à trois tons, jambe du second plan éclaircie. Classe `Anim` (`snap`, `va`, `cligne`, `geste`) et 16 expressions (`EXPR`). | non |
| `camera.py` | Caméra par stations et projection, communes à Blender et à l'assemblage. | non |
| `plaque.py` | Le rendu rapide : découpe chaque plan en tronçons de caméra, classe chacun par sa parallaxe (`fixe`, `plaque`, `couches`, `3d`), calcule la caméra et la taille de la plaque, et la recadre à l'assemblage (`reprojeter`). Lit les clés `mode` et `anime` des plans et la variable `EPISODE_MODE`. | non |
| `film.py` | **Le film** : personnages, plans, caméras, jeu, sous-titres, soleil, cibles du contrôle. Clés facultatives d'un plan : `source` (lampe principale en intérieur), `mode` (forcer le mode de rendu), `anime` (le décor bouge). | oui : entièrement |
| `bl_decor.py` | Bibliothèque Blender : matières dessinées (`matiere`, `bois`), bois dessiné à veines, nœuds et cernes (`NT.bois_dessine`), formes (`boite`, `cylindre`, `sphere`, `toit`), semis de cailloux et de touffes, `soleil` (pénombre réglable), `lampe`, `globe` (source ronde), fusion par matière, rendu des trois passes avec reprise, pour une image du film ou pour la plaque d'un tronçon. | non |
| `bl_scene.py` | **Les décors** de l'exemple : une cuisine le soir, la cour d'un phare au couchant. | oui : entièrement |
| `compo.py` | L'assemblage : lumière de l'ambiance (ombres en mélange, flaques des lampes, occlusion), contours du décor, ciel peint, brume, halos, profondeur de champ à sol net, bords sombres, personnages et leur ombre, accentuation, sous-titres, fondus entre plans, encodage. Sur un tronçon en plaque, la lumière, les contours, le ciel et les halos sont posés une fois ; par image il reste le recadrage, la profondeur de champ, les bords, les personnages et les sous-titres. | non |
| `lancer.py` | Enchaîne construire, rendre, assembler ; verrou « un seul Blender » ; reprise après plantage ; arrêt par numéro de processus ; `plans` affiche les tronçons de caméra et leur mode. | non |
| `controle.py` | Le tableau « règle du prompt maître / mesuré sur le film / dans la tolérance ? », sans cible posée à la main. Il vérifie aussi ce qui entre dans le champ (`film.CONTROLE_CHAMP`) et, en intérieur, la palette et l'ombre du personnage. | non |

## Décrire un personnage

```python
PERSOS = pantin.definir({
    "lea": dict(couleur="#2a6f97",                    # couleur du torse (l'ombre propre est calculée)
                torse="gelule",                       # "gelule" (0,72 × 1,0 D) ou "cloche" (manteau long, robe)
                col="rond", boutons=2, ceinture="#6b3f2a", garniture="#f4ead2", bande_bas=False,
                coiffe=dict(type="bonnet", tons=("#e8503a", "#bf3a2e", "#f4ead2")),    # clair, moyen (côté ombre), bandeau
                cheveux="#5a3020",
                accessoire="echarpe", accessoire_couleur="#f2b632",
                pilosite=None, poil=None, sourcil=None,
                h=1.60, jambes=1.2, torse_h=1.0, torse_l=0.72),      # taille en mètres ; jambes et torse en D
})
```

| Clé | Valeurs |
|---|---|
| `coiffe` → `type` | `cheveux`, `chignon`, `bonnet`, `casquette`, `beret`, `fichu`, `cloche` ; ou `None` |
| `accessoire` | `sacoche`, `echarpe`, `tablier` ; ou `None` |
| `pilosite` | `moustache`, `barbiche`, `chaume`, `barbe` ; ou `None` |
| `col` | `rond`, `v` ; ou `None` |

Une clé inconnue est refusée avec un message. Pour une coiffe ou un accessoire qui n'existe pas, ajoutez un cas dans `_coiffe()` ou `_torse()` de `pantin.py` en gardant la règle : contour régulier de 0,032 D, trois tons francs (`tons()`), aucun dégradé.

## Écrire le jeu

```python
a = Anim("lea", **EXPR["neutre blasé"])       # la pose de base, tenue
a.cligne(22)                                   # clignement de 3 images
a.snap(67, ty=0.03, bras_g=(2, 0))             # anticipation : 2 images avant la pose forte
a.geste(69, depasse=dict(bras_g=(66, 44)), final=dict(bras_g=(74, 36)),
        bras_g=(78, 30), main_g="doigts", **EXPR["stupeur"])      # pose forte en 1 image, dépassement 3, retour 4
```

- `snap(f, …)` : la pose change à l'image `f`, sans intermédiaire, et tient. C'est le geste de base.
- `va(f0, f1, …)` : glissement ; à réserver au dépassement et au retour d'un geste large, et aux mouvements secondaires (un pan d'écharpe).
- L'action se pose **2 à 4 images après** le début du carton qui la nomme.
- Dans un plan à deux, un seul personnage a des `snap` ; l'autre garde sa pose et cligne.

## Construire un décor

Dans `bl_scene.py`, garder l'ordre : `B.init()`, `B.soleil(…)`, les matières, la géométrie, `B.fond()`, `B.orienter_fil(…)`, `B.fusionner(…)`, `B.camera_film()`, `B.enregistrer(…)`.

```python
PL, JT = R.DECOR["planche"] * D, R.DECOR["joint"] * D          # 0,32 D et 0,021 D
B.matiere("plancher", "#b4602f", "#7c361c", fibre="y", coords="monde", veine="#4a1d16",
          planches=("x", PL, JT, "#33121a"), fil=1.6, net=0.05, var=0.7)       # lames dans la longueur, joints en travers
B.bois("bois", "#8a4a30", "#55291e", "#2f1418")                 # le fil suivra le grand côté de chaque objet
B.matiere("lampe", "#ffd08a", emissif=True)                     # brille : halo ajouté à l'assemblage
B.matiere("caillou", "#f0c090", "#e0ae7c", a_plat=True, lisere="#8a5632")
```

Règles de construction, tirées des mesures et des critiques :

- **30 à 45 objets distincts dans le champ** de chaque plan ; rien de nu derrière un personnage.
- Une **source de lumière visible** par lieu, **ronde** : `B.globe(nom, rayon, position, matière émissive, energie=…)`. Le halo posé à l'assemblage est la surface qui brille, étalée : une sphère donne un disque, une boîte une tache rectangulaire. Jamais de boîte émissive pour une lampe.
- Un **contrepoint froid** dans une ambiance chaude : une fenêtre bleu de nuit (matière émissive froide : elle baigne le mur autour d'elle), des tentures violettes.
- **Bois** : `B.bois()` et `B.matiere(…, fibre=…)` dessinent un vrai bois (veines qui ondulent, nœuds, cernes ; réglages dans `regles.BOIS`). Plafond et poutres compris : pas d'aplat.
- **Soleil** : `B.soleil(direction, penombre=degrés)` ; par défaut 3,5°, qui adoucit les ombres avec la distance (0,5 D au bout d'une ombre longue).
- Dehors : `B.semer()` (cailloux) et `B.touffes()`, en laissant libre le sol sous les pieds.
- Aucun objet coupé par le bord du cadre ; des formes contrastées dans le fond, pour que le flou reste lisible.

### Un intérieur (règles de `regles.INTERIEUR`)

- **Sombre** : luminance moyenne de 61 (± 15), saturation de 0,58 (± 0,08), près de la moitié de l'image en prune très sombre (`#251023`, `#3a1828`), **une seule** dominante chaude (bruns-rouges moyens, un cinquième de l'image), 6 à 9 % de froid (violet `#503056`, bleu de nuit `#312e79`) par les fenêtres et dans les ombres. La loi est dans `compo.eclairer` ; ses réglages dans `regles.AMBIANCES["interieur"]["decor"]`.
- **Cadrer serré devant un fond sombre et flou** ; une lampe principale par plan.
- **Murs meublés à la hauteur du champ** : boiserie jusqu'à 2,25 m, rayonnage, tentures, cadres. Jamais de mur nu derrière un personnage.
- **Donner la lampe principale de chaque plan** : `source=(x, y, z)` dans le plan (`film.py`). L'assemblage en déduit l'ombre du personnage (projetée au sol à l'opposé de la lampe), le liseré de lumière chaud côté lampe et le côté du délié du trait (`lum_perso`, qu'on peut toujours forcer). Le sol doit être clair et dégagé sous les pieds : une ombre ne se lit pas sur un tapis sombre.
- `python outils/controle.py` vérifie tout cela sur les images de `film.CONTROLE_CHAMP` : part de décor plat derrière la tête et le torse (35 % au plus), aucun membre contre le bord gauche, droit ou haut du cadre, objets coupés par les bords, palette, ombre lisible et bien orientée.
- Les lieux sont construits loin les uns des autres dans la même scène (l'extérieur de l'exemple est à y = −60).

## Limites connues

- **Ambiances** : `soir` (extérieur au couchant) et `interieur` (intérieur chaud) sont essayées. `jour` et `nuit` sont en données dans `regles.py` d'après les mesures, **non essayées** : le liseré clair des arêtes de nuit n'est pas fait. À contrôler avant de livrer.
- **Personnages** : vues de face et de trois quarts. Ni profil strict ni dos.
- **Trait du décor** : tiré de la profondeur, pixel par pixel, donc un peu moins régulier que celui des personnages.
- **Objet héros** : rien de prévu au-delà des formes simples ; pour un objet complexe, voir le skill `blender`.
- **Son, voix, alignement des mots** : hors de la chaîne mesurée ; `mix.py`, `ecart_voix.py` et `references/pipeline.md`.
- **Assemblage HyperFrames** : la chaîne mesurée pose elle-même les sous-titres et encode avec ffmpeg. Pour un habillage en plus (titres, logo), passer `sortie/film.mp4` au skill `rendu`.

## Ce qui a été essayé

Le 12/11/2026, sous Windows, avec Blender 5.3 (carte graphique intégrée) et Python 3.13, depuis un dossier neuf où seul ce kit avait été copié.

- Avec le seul kit, sur un sujet inventé pour l'occasion (une gardienne de phare attend une lettre, le facteur arrive) : un film de 7 s, 210 images, 2 plans (un intérieur chaud, un extérieur au couchant), 2 personnages décrits en données, sans son. Les chiffres de ce premier essai datent d'avant l'intérieur sombre (voir plus bas).
- Rendu Blender : 4,2 s par image pour les trois passes (220 images en 15,6 min, scène de 1 270 objets réunis en 60). Assemblage : 8 à 10 s par image et par processus (210 images en 12 min avec trois processus). Construction de la scène : 13 s.
- Contrôle chiffré automatique (`controle.py`) : **57 lignes dans la tolérance, 4 hors, aucune non mesurée** sur 61 (hors tolérance : la densité de deux images, et le contour relu dans le film encodé sur une pose où la coiffe et un bras levé touchent la tête).
- Critique d'un agent indépendant qui n'avait que le prompt maître et le film : **5 sur 10** avant corrections, **7 sur 10** après un tour (personnages 8, jeu 8, décor 6, caméra et montage 7, sous-titres 8,5, histoire 7,5 ; plus aucun défaut bloquant).
- Ce qui reste, d'après lui : caméra trop calme sur les plans d'extérieur (3 à 9 px par seconde pour 20 à 30 demandés), un doigt coupé par le bord du cadre pendant une tenue, des objets du décor coupés par le cadre, un fil du bois qui reste un bruit étiré, des bords trop peu assombris en extérieur, un soleil pâle, un trait de décor crénelé.
- Le contrôle a trouvé un défaut que l'œil avait laissé passer : deux sols à la même hauteur (celui de l'extérieur passait sous l'intérieur) se mélangeaient au rendu, une image sur deux. D'où la règle : chaque lieu a son sol, et les sols ne se recouvrent pas.
- **Non essayé** : les ambiances `jour` et `nuit` ; macOS et Linux ; le module `bpy` sans le programme Blender ; une carte graphique dédiée ; un film de plus de deux plans ; le son (`mix.py`) branché sur cette chaîne ; `lancer.py arreter` sur un vrai rendu en cours (la reprise après arrêt, elle, a servi) ; les coiffes `beret`, `fichu`, `cloche`, `chignon` et les accessoires `tablier`, `sacoche` au-delà des planches de personnages (la sacoche est dans le film).

### Essai de l'intérieur sombre, le 12/11/2026

Même machine. La cuisine de l'exemple refaite selon `regles.INTERIEUR`, deux plans d'intérieur de 1,9 s (57 et 59 images), le film d'exemple passant à 3 plans.

- Rendu : 26 rendus Blender pour les deux plans d'intérieur et trois images fixes (20 images de déplacement, 3 plaques, 3 fixes), 2,0 min, soit 4,6 s par rendu ; le film entier : 70 rendus pour 229 images. Assemblage : 109 images en 6,6 à 7,2 min avec 5 ou 6 processus. Construction de la scène : 16 à 50 s (la première fois, les matières sont compilées).
- Mesures sur une image de chaque plan (`controle.interieur`, `controle.champ`) : 28 lignes dans la tolérance sur 30. Luminance 58,5 et 53,8 (cible 61), saturation 0,586 et 0,582 (0,58), froid 10,8 et 7,4 % (6 à 9, tolérance 4 à 12), ombre du personnage à 0,65 et 0,67 de la luminance du sol, à 7° et 1° de l'opposé de la lampe, aucun décor plat derrière la tête et le torse, blancs du personnage conservés (ΔE 1,3). Bois de la table : contraste 16,8 (18 à 21, ± 6), grain fin 7,9 (8,5 à 12,7, ± 4) ; plancher : contraste 15, un joint tous les 0,334 D.
- **Hors tolérance** : sur le plan de face, le prune très sombre ne fait que 28 % de l'image (36 à 60 attendus) et les bruns-rouges moyens 34 % (12 à 28) : le plancher éclairé occupe trop de cadre. L'indicateur « segments » reste à 302 et 322 pour 159 mesurés.
- `controle.py` sur le film entier (3 plans) : **91 lignes dans la tolérance, 7 hors** sur 98 (le prune du plan de face, la densité de deux images, le contour relu dans le film encodé, une jambe mesurée devant un pied de table, six silhouettes coupées par les bords du plan d'extérieur).
- Critique d'un agent indépendant (le prompt maître, une image d'intérieur de référence, les deux plans) : **6,5 sur 10** avant corrections, **7 sur 10** après un tour (décor 7, intégration du personnage 6,5 ; l'essai précédent : 5). Un réglage a suivi la note sans être renoté : le liseré ne peut plus assombrir la peau (il faisait échouer deux lignes du contrôle de la tête).
- Ce qui reste, d'après lui : aucun meuble ne passe devant le personnage ; la lampe ne fait pas de tache claire au sol ni sur la table ; les objets nets proches sont trop noirs et leur trait est mou ; un panier coupé par le cadre ; une seule vraie source de lumière ; des coins encore trop clairs ; des particules posées devant le costume.
- `lancer.py arreter` a servi sur un vrai rendu en cours. **Non essayé** : la pénombre du soleil (`soleil_deg`) et l'effacement du liseré des cailloux n'ont pas été mesurés ; les plans d'intérieur sans clé `source` (l'ancienne tache sous les pieds) n'ont pas été rendus de nouveau ; un intérieur à plusieurs personnages.

## L'ancienne chaîne (plans émissifs)

Elle monte le personnage comme un plan à matériau émissif dans Blender et rend l'image finale en une passe. Elle garde son intérêt pour `theatre-de-papier`, et sa boucle de rendu long (`rendre.py`, `refaire.py`, `suivi.py`) est décrite dans le skill `blender`, `references/rendu-long-et-fiable.md`.

| Étape | Commande |
|---|---|
| Vérifier la machine | `python outils/reglages.py` |
| Liste de plans | `python outils/plans.py` |
| Personnages (pièces SVG, une vue de face) | `python outils/personnages.py` |
| Décor, passes 1 à 3 | `python outils/rendre.py --construire --passe 1` (puis 2, puis sans `--passe`) ; contrôle : `python outils/rendre.py --controle planche passe1_ 25` |
| Profilage, rendu, suivi | `python outils/rendre.py --profiler`, `python outils/rendre.py`, `python outils/suivi.py --boucle` |
| Reprise de plages | `python outils/refaire.py tour1 A-B` |
| Voix, son, assemblage, revue | `ecart_voix.py`, `mix.py`, `hf_build.py`, `revue.py` |

Son exemple (un personnage nommé « Galet », 2 plans) est lui aussi à remplacer. Trois règles valent pour les deux chaînes : un seul Blender qui rend à la fois ; on arrête une boucle par sa commande d'arrêt, jamais en tuant Blender ; le connecteur construit et regarde, la ligne de commande rend.
