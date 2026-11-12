---
name: reproduire-reel
description: "Analyser un reel de référence fourni par le client et en reproduire la technique (découpage, rythme, caméra, rendu des personnages et des décors, sous-titres, son) dans une vidéo à lui, avec son contenu. À utiliser quand le client envoie une vidéo ou un lien et dit « refais-moi ça », « je veux ce style », « même rendu que ce reel », ou quand une première version est jugée « loin de l'original ». Méthode : découpage en plans, lecture continue image par image, zoom et mesure au pixel, fiche de style chiffrée, contrôle chiffré référence / nous, plans de test critiqués par un agent indépendant."
---

# Reproduire un reel : mesurer la technique, la refaire avec le contenu du client

Tu reçois un reel que le client admire. Ton travail : comprendre **comment il est fait**, au pixel et à l'image près, puis refaire **cette technique** dans une vidéo du client, avec ses personnages, son histoire, sa voix. Ce skill marche pour tout reel : motion design, 2D, 2.5D, 3D, face caméra habillée.

Il vient d'un essai réel du studio. Une première version jugée à l'œil a été dite « loin de l'original ». Une analyse en lecture continue l'a rapprochée. Une mesure au pixel a trouvé ce que l'œil n'avait pas vu, et a corrigé deux erreurs de l'analyse à l'œil. D'où la règle du skill : **on mesure, on ne devine pas.**

## Les quatre règles écrites noir sur blanc

1. **On reprend la technique, pas l'œuvre.** Jamais les personnages, les costumes, les accessoires, le texte, la voix, la musique, le logo ni le sujet du reel étudié. Les personnages et l'histoire sont ceux du client. Si le client demande de recopier un personnage ou un logo reconnaissable, **refuse cette partie et dis-le-lui en une phrase** : « Je reprends la façon dont c'est dessiné, animé et monté, pas ce personnage ni ce logo : ils appartiennent à leur auteur. On fait les tiens dans cette technique. » Ne reproduis pas non plus les irrégularités d'un dessin précis (les bosses d'un trait tracé à la main, une tache, une mèche) : ce serait recopier le dessin. **Tires-en une loi** et applique la loi. Détail : `references/droits-et-limites.md`.
2. **Pas d'impression sans mesure.** Chaque affirmation de la fiche de style renvoie à un chiffre et à une image (numéro d'image, fichier de mesure, planche). « Le trait est épais » n'existe pas ; « 0,07 D côté ombre, image 990, `ref_0990_planche.jpg` » existe.
3. **Dis franchement la note du critique et ce qui reste différent.** Si le critique indépendant met 6,5 sur 10, tu écris 6,5 sur 10, puis la liste de ce qui trahit encore la différence et pourquoi.
4. **Annonce au client le temps que ça prend**, avant de commencer (tableau ci-dessous).

Deux règles de conduite apprises à nos dépens : **ne rends jamais la main pendant qu'un rendu ou une mesure tourne** (un tour s'est terminé ainsi sans critique ni compte rendu) ; **quand le critique et la mesure se contredisent, la mesure tranche.**

## Le temps que ça prend (temps réels de l'essai du studio)

Reel de 56 s, 1 682 images, un agent et ses sous-agents, sur un PC de bureau.

| Tour | Ce qui a été fait | Temps réel |
|---|---|---|
| Lecture continue et premier kit | découpage, lecture des 1 682 images par quatre agents en parallèle, écoute du son, fiche de style, nouveau kit de personnages, 4 plans de test (8 s) | ≈ 1 h 10, dont ≈ 30 min d'analyse |
| Mesure au pixel et second kit | scripts de mesure (≈ 25 min, déjà écrits ici), mesure de 11 images (≈ 10 min), kit refait et contrôle chiffré en 4 tours (≈ 15 min), deux rendus de 9 min des plans de test (≈ 20 min), critique et corrections | ≈ 1 h 15 |
| Mesure et reconstruction du décor | choix et extraction de 20 images (≈ 10 min) ; scripts de mesure du décor, pose des cibles, mesures, parallaxe, focale (≈ 25 min, scripts déjà écrits ici) ; scène 3D de deux lieux, matières dessinées, passes, assemblage, 12 essais (≈ 55 min) ; rendus des 4 plans de test, dont deux interrompus (≈ 60 min, le bon : 39 min 40 s pour 258 images) ; contrôle chiffré en 4 tours et planches (≈ 30 min) ; assemblage du film de test, deux fois (≈ 45 min, en partie en parallèle) ; critique, corrections, nouvelle notation (≈ 20 min) | ≈ 3 h 40 |

À dire au client : **compte 2 heures pour l'analyse et des plans de test fidèles** d'un reel d'une minute quand le décor est simple ou déjà construit, et **une demi-journée de plus quand il faut mesurer et reconstruire un décor en volume** (une demi-journée par lieu supplémentaire) ; le film entier vient ensuite, avec son propre temps de rendu. Avec les scripts fournis, la mesure au pixel elle-même est courte : c'est le choix des images, la pose des cibles, la construction et les tours de correction qui prennent le temps.

Résultat à annoncer sans l'embellir : après ce tour, le décor reconstruit a été noté **6 sur 10** par le critique indépendant (un extérieur à 7, un intérieur à 5), contre 3,5 avant la mesure et 9 pour la référence, avec 34 grandeurs sur 61 dans la tolérance. La mesure rapproche nettement ; elle ne suffit pas à atteindre la référence en un tour.

Repère tiré de l'essai de ce skill par un agent seul, sur le même reel : découpage vérifié à l'image, lecture continue de 3 plans, mesure de 4 images (6 têtes, un torse, un sous-titre), fiche remplie : **20 minutes**. Les scripts comptent pour moins de 4 minutes là-dedans (découpage 1 à 2 min, extraction de 4 images ≈ 25 s, mesure 3 à 7 s par image).

## Ce skill et les autres

| Besoin | Skill |
|---|---|
| Le parcours d'une vidéo (questions, histoire, storyboard, revue, livraison) | `studio-coeur` |
| Le cahier de recréation plan par plan, le contrôle du rythme (`controle_rendu.py`) | `formats-flotweb`, fiche `recreation-reel` |
| Construire les personnages | `personnages` |
| Décors, objets et rendus 3D ou 2.5D | `blender`, `styles-2-5d` (kit) |
| Assembler, sous-titrer, exporter | `rendu` |
| Écouter et refaire le son | `son` |

Partage des rôles : **ce skill mesure la référence et prouve la ressemblance par des chiffres** ; la fiche `recreation-reel` écrit le cahier plan par plan et contrôle le rythme du film fini. Les deux s'emploient ensemble.

## Outils

Scripts dans `scripts/`, en Python (Windows, macOS, Linux). Il faut Python 3.9 ou plus, `numpy`, `Pillow`, `opencv-python` (ou `opencv-python-headless`) et FFmpeg **5.1 ou plus** (`ffmpeg`, `ffprobe` ; vérifier par `ffmpeg -version`). S'il en manque un : `pip install numpy pillow opencv-python`, et le skill `installation` pour FFmpeg. Ne remplace jamais une mesure par une impression parce qu'un outil manque.

Ce que les scripts gèrent : une vidéo de téléphone enregistrée avec une rotation (elle est lue redressée), une cadence variable (les numéros d'image font foi, les secondes sont approximatives), une image à fond transparent (posée sur un gris, avec un avertissement). Ce qu'ils ne gèrent pas : une vidéo HDR (les couleurs lues sont fausses : demander un export SDR) et une source de moins de 720 px de large.

Lance-les depuis le dossier de travail du client, avec `PYTHONDONTWRITEBYTECODE=1` (sinon Python laisse des `__pycache__` dans le plugin). Dans les commandes ci-dessous, `$S` est `"${CLAUDE_PLUGIN_ROOT}/skills/reproduire-reel/scripts"` et `python` s'écrit `python3` sur macOS et Linux. Chaque script affiche son mode d'emploi avec `-h`.

| Script | Rôle | Étape |
|---|---|---|
| `decouper.py` | bornes des plans en numéros d'image, une image nette par plan, planche numérotée, images autour de chaque borne à vérifier | 2 |
| `bandes.py` | bandes de lecture continue (toutes les images d'un passage, numérotées) | 3 |
| `extraire.py` | images PNG pleine résolution, sans redimensionnement, avec leur netteté | 4 |
| `grille.py` | recadrage avec grille de coordonnées, pour poser les cibles | 4 |
| `mesurer.py` | mesure au pixel d'après un fichier de cibles : chiffres, courbes, planche annotée | 4 et 8 |
| `synthese.py` | tableau de toutes les formes mesurées, loi commune du contour, palette par ambiance | 4 et 6 |
| `palette.py` | palette et look d'une image ou d'une zone (contrôle rapide, netteté d'une zone) | 5 |
| `mesurer_decor.py` | mesure au pixel du **décor**, d'après la rubrique `decor` du même fichier de cibles : matières, contours, ombres, lampes, détails au sol, netteté, plus la palette, la densité et le grain de l'image | 5 et 8 |
| `synthese_decor.py` | palette commune et indicateurs par ambiance, relevé de toutes les mesures du décor en D | 5 et 6 |
| `parallaxe.py` | ce qui est en volume et ce qui est peint, entre deux images d'un mouvement de caméra | 5 |
| `focale.py` | focale apparente et tenue de la caméra, par les points de fuite | 5 |
| `comparer.py` | tableau « référence / nous / écart » avec tolérances, courbes superposées, suivi des tours | 8 |
| `comparer_decor.py` | le même tableau pour le décor, d'après un fichier de paires, avec les tolérances du décor et le bilan par famille | 8 |
| `cote_a_cote.py` | planche de comparaison à deux ou trois colonnes, recadrages agrandis | 8 et 9 |

Dossier de travail : `reproductions/<nom-court>/` dans le dossier du client, avec `reference/` (la vidéo), `analyse/` (`decoupage/`, `bandes/`, `lecture-continue/`, `images/`, `cibles/`, `mesures/`, `parallaxe/`, `palettes/`), `fiche-reference.md`, `controle/`, `revue/`.

## Le parcours

### 1. Récupérer la référence
- **Le client fournit le fichier** : c'est le cas simple. Range-le dans `reference/`, ne le modifie pas.
- **Le client donne un lien** : la vidéo se récupère avec **l'outil du client, sur sa machine**, dans le respect des conditions de la plateforme (son propre contenu, un export proposé par la plateforme, ou une autorisation de l'auteur). Tu ne télécharges rien à sa place sans qu'il le demande et tu ne contournes aucune protection. S'il ne peut pas l'obtenir, demande-lui un enregistrement d'écran de la vidéo : la mesure marche aussi, avec une précision moindre (note-le dans la fiche).
- **La vidéo reste sur sa machine, sert d'étude, n'est jamais republiée ni redistribuée** : pas dans le film, pas dans un aperçu, pas dans un dépôt. Les images extraites non plus.
- Relève d'abord le format : `ffprobe` (taille, cadence, nombre d'images). Une source de moins de 720 px de large ne permet pas la mesure au pixel du trait : dis-le.

### 2. Découpage en plans
```
PYTHONDONTWRITEBYTECODE=1 python $S/decouper.py reference/ref.mp4 analyse/decoupage
```
Tu obtiens `plans.json` et `plans.md` (bornes **en numéros d'image**, durée, transition d'entrée), `planche-plans.jpg` (une image nette par plan, numérotée), `plans/Pxx_iNNNN.png` (cette image en pleine résolution), `survol-N.jpg` (tout le film, une image sur six), `bornes-a-verifier-N.jpg` (4 images avant et 4 après chaque borne), `mouvement.png`. Compte une à deux minutes de calcul pour un reel d'une minute.

**Piège appris : un film peut être un quasi plan-séquence**, relié par des déplacements rapides de caméra et des fondus. Dans notre essai, deux détecteurs du commerce annonçaient 4 coupes en 56 s ; la lecture à l'image n'en a confirmé **aucune** : 8 fondus enchaînés, 9 déplacements de caméra, 2 raccords dans un objet. **Aucun détecteur n'a raison tout seul**, celui-ci non plus : il propose des bornes (`coupe`, `saut`, `mouvement`, `fondu`) et il en rate (un fondu de 2 à 4 images, une transition entre deux plans de même palette). Donc :

1. **Cherche ce qu'il a raté** : ouvre chaque `survol-N.jpg` et repère tout changement de décor, de lumière ou de cadrage **sans borne** (une case rouge marque le début de chaque plan). Sur chaque passage suspect, fais une bande image par image (`bandes.py`, 16 images autour).
2. **Tranche chaque borne proposée** sur `bornes-a-verifier-N.jpg` :

| Ce que tu vois sur les 8 images | C'est |
|---|---|
| tout change d'une image à la suivante | une **coupe** |
| deux images superposées en transparence pendant 2 à 12 images | un **fondu enchaîné** |
| le même décor qui glisse, flou dans le sens du mouvement | un **filé** (panoramique rapide) |
| le même décor qui grossit ou rétrécit | un **zoom** ou un travelling |
| l'image traverse un objet (une pupille, une fenêtre) et ressort ailleurs | un **raccord dans un objet** |
| même décor, même cadre : un geste, une chute, un flash | **rien** : retire cette borne |

3. **Pose les bornes** : au milieu d'un fondu, au plus fort d'un déplacement de caméra. Quand le script signale « peu de coupes franches », tu découpes par **stations** : une tenue de caméra, puis ce qui mène à la suivante.
4. **Relance avec tes bornes et leur type** : `python $S/decouper.py reference/ref.mp4 analyse/decoupage --bornes 24:fondu,33:filé,84:zoom,254:fondu,…` (numéro de la première image de chaque plan, sans le 0). Le type s'écrit dans la colonne « Entrée » de `plans.md`. Les images nettes de la passe précédente sont déplacées dans `plans/_passe-precedente/` ; garde une copie du premier `plans.md` si tu veux comparer.
5. Si `hyperframes measure` est disponible, `formats-flotweb/scripts/analyse_reference.sh` ajoute la carte des évènements et le relevé du look : croise ses coupes avec les tiennes, à l'image.

Dans la fiche, écris le compte : tant de coupes, de fondus, de déplacements, **vérifiés à l'image**.

### 3. Lecture continue
Les planches à pas fixe ratent ce qui fait le style d'un jeu : un changement de pose en une image, un clignement de trois images, une anticipation de deux. **Extrais toutes les images des plans où ça joue**, sans en sauter :
```
python $S/bandes.py reference/ref.mp4 analyse/bandes/P07.jpg --plans analyse/decoupage/plans.json --plan P07
python $S/bandes.py reference/ref.mp4 analyse/bandes/P07-visage.jpg 412 429 --crop 250,180,560,560 --larg 320 --cols 6
```
Lis chaque bande et décris le mouvement **image par image** dans `analyse/lecture-continue/lecture.md`, d'après `gabarits/lecture-continue.md` : anticipation, durée de chaque geste, tenues, changements en une image, clignements, caméra (départ, vitesse, freinage, dérive), effets, instant de l'action par rapport au mot du sous-titre. Toutes les durées en nombre d'images. Méthode, questions à se poser, partage entre sous-agents pour un film long : `references/lecture-continue.md`.

Minimum : tous les plans de l'accroche (0 à 3 s), plus chaque plan où un personnage joue ou où la caméra fait un mouvement marqué ; au moins 12 plans pour un reel d'une minute.

### 4. Zoom et mesure au pixel
C'est l'étape qui a fait la différence. Détail complet et format du fichier de cibles : `references/fichier-de-cibles.md`.

1. **Choisir les images** : l'élément est **grand** (un trait de moins de 4 px ne se mesure pas), **net** (plan figé), et **toutes les ambiances** de lumière du reel sont représentées. Compte 8 à 12 images pour un reel d'une minute, dont des gros plans et des plans d'ensemble.
2. **Extraire en pleine résolution, sans redimensionnement** : `python $S/extraire.py reference/ref.mp4 analyse/images 8,290,512,990 ref`. Le fichier `ref_nettete.json` dit si chaque image est figée (écart avec ses voisines sous 4) ou en mouvement (au-dessus de 10). Une image en mouvement se mesure quand même si elle est la seule à montrer l'élément dégagé, mais **elle n'entre pas dans la loi** (`synthese.py --sans ref_0512`) tant qu'une image figée ne la confirme pas, et la fiche le dit.
3. **Poser les cibles** : `python $S/grille.py analyse/images/ref_0990.png analyse/cibles/grille_0990.jpg 150 600 600 1300 --k 2`, lire les coordonnées sur la grille, écrire `analyse/cibles/ref_0990.json` d'après `gabarits/cibles.json`. Une cible désigne une **forme** (cercle, ellipse, rectangle, polygone ou masque : une tête, un torse, un chapeau, un bouton, un titre, un sous-titre), une **coupe** en travers d'un trait, un **trait** d'épaisseur constante (membre, tige, ligne), une **zone** de couleur ou une **ombre** au sol.
4. **Mesurer** : `python $S/mesurer.py analyse/cibles/ref_0990.json analyse/mesures`.
5. **Vérifier avant de croire** : ouvre l'image de contrôle de chaque forme, `ref_0990_<forme>_bords.jpg`. Les points **rouges** doivent suivre le bord intérieur du trait, les **cyan** son bord extérieur ; le cercle blanc est le cercle ajusté ; les points gris sont les orientations écartées. Là où les points cyan partent sur un autre trait (le cou, une main, un chapeau), la mesure est celle de deux traits collés : exclus ce secteur avec `"exclure_angles": [[235, 290]]` (les étiquettes jaunes donnent l'orientation tous les 30°) et relance.
6. **Lire les chiffres** : épaisseur du contour selon l'orientation du bord (courbe tous les 5°), **la loi simple** (`loi_simple` : `a0`, `h1`, côté du plein, d'où le délié `a0 − h1` et le plein `a0 + h1`), couleur exacte du trait et du remplissage, ombrage (deux zones et leur lecture, frontière, profils de luminance), reflets et liserés, dureté des bords (largeur de transition), accentuation, halo, grain, détails dessinés dedans, ombre au sol (couleurs, facteur par canal, flou du bord). Pour le plein et le délié, prends ceux de la loi : le maximum brut est presque toujours gonflé par un trait voisin.
7. **Tout exprimer en fraction d'une grandeur de référence** : le diamètre de la tête (D), la hauteur d'un titre, la largeur d'un objet. C'est ce qui permet de refaire à toute taille. Pour un cercle, les valeurs `_D` sont rapportées à son propre diamètre ; les valeurs `_ref` de toutes les formes sont rapportées à la grandeur désignée par le champ `"reference"` du fichier de cibles (une seule par image, rappelée dans `rapporte_a`).
8. **Chercher la loi** : `python $S/synthese.py analyse/mesures --prefixe ref_`. Deux questions : `a0` et `h1` sont-ils les mêmes, en fraction de D, d'une forme à l'autre et d'une taille à l'autre ? Le côté fin du trait est-il le côté clair de l'ombrage (colonne « Écart délié / clair », une mesure indépendante du contour) ? Dans notre essai : oui deux fois (écart médian de 8°), d'où la règle « trait fin côté lumière, épais côté ombre, en simple cosinus ». **C'est la règle qu'on reproduit**, pas la courbe d'une image.

### 5. Décors, caméra, montage, sous-titres, son
Ce qu'on mesure et comment : `references/decors-camera-montage-son.md`.

**Le décor se mesure comme les personnages**, avant de le construire. Dans notre essai, un décor fait d'après l'idée générale (« aplats saturés, contour, ombre bleue ») était noté 3,5 sur 10 ; ses matières avaient 2 niveaux de contraste là où la référence en a 8 à 21. Compte 15 à 20 images (toutes les ambiances ; un plan large, un plan moyen et un gros plan par ambiance), note D sur chacune, pose les cibles dans la rubrique `"decor"` du fichier de cibles (`references/fichier-de-cibles.md`, § 8), puis :
```
python $S/parallaxe.py reference/ref.mp4 analyse/parallaxe 688:690,1379:1380 --bande 1270,1430
python $S/mesurer_decor.py analyse/cibles/ref_1400.json analyse/mesures
python $S/synthese_decor.py analyse/mesures --prefixe ref_
python $S/focale.py analyse/images/ref_1650.png --bande 1270,1430
```
Neuf familles, toutes exprimées **en D** (`references/decors-camera-montage-son.md`, § 1) :

| N° | Famille | Ce qu'on relève |
|---|---|---|
| 1 | Volume ou peint | par la parallaxe : ce qui est un vrai volume, ce qui est un plan peint lointain ; les couches de profondeur par ambiance |
| 2 | Densité et vocabulaire | segments et bords par image, objets comptés à l'œil et leurs familles, parts de l'image, tailles en D |
| 3 | Matières | aplat ou texture ; fréquence des joints, contraste, fil, couleur des lignes |
| 4 | Contours du décor | silhouette et arêtes : épaisseurs, couleur, côté épais |
| 5 | Lumière et ombres | couleur des ombres (un bleu qui **augmente** = un mélange vers une teinte, pas une multiplication), dureté du bord au contact et au loin, tons par face, dégradés, lampes et flaques |
| 6 | Palette par ambiance | 10 dominantes, saturation, luminance, les deux familles de teintes opposées |
| 7 | Optique | focale, hauteur de caméra, flou du fond, **netteté du sol sous le sujet**, règle de flou selon la distance |
| 8 | Finitions au sol | détails par D², diamètre, nature |
| 9 | Lointain et traitement final | ciel, soleil, brume, bords assombris, grain |

Exclus la bande des sous-titres des mesures globales (`"bande_exclue"`), et ouvre chaque `<id>_decor_planche.jpg`. Le § 1.11 de la référence donne **le diagnostic type** : les six causes, dans l'ordre, d'un décor qui ne ressemble pas, avec la mesure qui révèle chacune.

Le reste, en bref :
- **Profondeur de champ, contrôle rapide** (reel sans décor construit) : la netteté d'une zone du sujet comparée à celle du fond (`palette.py --boite`), et la largeur de transition des bords.
- **Caméra et cadrage** : type de cadrage et taille du sujet dans le cadre par plan, durée des tenues et des déplacements, freinage, dérive en pixels par seconde, lus sur les bandes et sur `mouvement.csv`.
- **Montage** : durée des plans (médiane, extrêmes), type et durée de chaque transition, en images.
- **Sous-titres** : une cible `rectangle` avec `"composantes": "toutes"`, tracée large autour du texte, donne la hauteur des lettres, la boîte et le centre du texte, la couleur du remplissage et du contour, l'épaisseur du contour dans chaque direction (un contour plus épais en bas à droite révèle une ombre décalée) ; le nombre de mots et la durée de chaque carton se comptent sur les bandes.
- **Son** : niveau (`ffmpeg -i reference/ref.mp4 -map 0:a:0 -af ebur128=peak=true -f null -`), place de chaque bruitage **par rapport au geste** (en millisecondes), présence et niveau de la musique, débit de la voix ; avec l'écoute mesurée du skill `son` quand elle est installée.

### 6. La fiche de style de la référence
Remplis `gabarits/fiche-reference.md` : les chiffres, les lois, les palettes par ambiance, le catalogue des poses et des durées, les sous-titres, le son, et le tableau **« ce qu'on reprend / ce qu'on ne reprend pas »**. Chaque ligne cite sa mesure et son image. Une case sans mesure reste vide et porte « non mesuré », elle ne reçoit pas une valeur plausible.

Montre la fiche au client en cinq lignes (ce qui fait le style, chiffré) et fais-lui confirmer le tableau « on reprend / on ne reprend pas ».

### 7. Reproduire
Construis le kit **d'après les mesures**, avec le contenu du client :
- **personnages** : skill `personnages` (pièces, expressions, jeu), avec les rapports mesurés (épaisseurs en fraction de D, loi du contour, palettes par ambiance, direction de la lumière par plan) ; pour la 2.5D, le kit de `styles-2-5d` ;
- **décors et objets** : skill `blender` (3D, 2.5D) ou `rendu` (2D). Chaque famille mesurée devient un réglage, en D :
  - **ce qui est en volume** se construit en volume, **ce qui est peint** se pose en plans peints lointains ;
  - **matières dessinées** à la fréquence et au contraste mesurés (joints, fil dans le sens de la pièce), jamais un aplat taché ;
  - **contours** à deux épaisseurs (silhouette, arête), dans l'encre de l'ambiance, plus épais en bas et côté ombre ;
  - **ombres par mélange** vers la teinte mesurée, à la force mesurée, bord de plus en plus doux en s'éloignant de l'objet ; deux tons par face ; flaques de lumière autour des lampes ;
  - **palette de l'ambiance**, avec son contrepoint ;
  - **profondeur de champ** selon la règle mesurée, mise au point sur le sujet, **sol net sous ses pieds** ;
  - **finitions au sol** à la densité et à la taille mesurées ; **ciel, brume, bords assombris** aux valeurs mesurées.

  Deux conseils de l'essai : **sépare la couleur de la lumière** au rendu (une passe de couleur peinte, une passe de lumière, une passe de profondeur et de normales), pour régler une ambiance en quelques secondes au lieu de relancer le rendu ; et **meuble le champ de chaque plan** : un décor riche hors champ ne compte pas. Les lieux, les bâtiments, les meubles et les accessoires sont ceux de l'histoire du client, jamais ceux de la référence ;
- **sous-titres** : skill `rendu`, avec la hauteur, la position, le contour et le nombre de mots mesurés ;
- **jeu et caméra** : les durées du catalogue (en images), pas des valeurs par défaut ;
- **son** : skill `son` : nos sons, calés sur nos gestes avec le décalage mesuré ; jamais la musique ni la voix de la référence.

Le sujet, l'histoire et le texte viennent du parcours de `studio-coeur` (étapes 1 et 2) : ce n'est pas le reel qui les donne.

### 8. Le contrôle chiffré
Méthode complète : `references/controle-chiffre.md`.
1. **Rends un élément à la même taille que dans la référence**, sous la même ambiance (même diamètre de tête en pixels, même hauteur de titre), sur un fond comparable, en PNG.
2. **Repasse EXACTEMENT les mêmes scripts** : un fichier de cibles pour ton image, `mesurer.py`, puis
   `python $S/comparer.py analyse/mesures/ref_0990.json controle/nous.json controle --paires controle/paires.json --tour 1`.
3. Lis le tableau **« référence / nous / écart »**. Tolérances : **épaisseurs ±1 px, couleurs ΔE < 6, luminance ±8 niveaux** (les autres sont dans `comparer.py` et se changent dans `paires.json`).
4. Corrige le kit, re-rends, re-mesure, recompare : **4 tours au plus** (`--tour 1` à `--tour 4`, le suivi s'écrit dans `controle/tours/`).
5. Une ligne hors tolérance qui vient de la forme propre d'un dessin (bosses d'un trait fait à la main, objet qui touche le contour) **ne se corrige pas** : compare alors ta courbe à **la loi** de la référence, et écris pourquoi la ligne reste rouge.
6. Planche côte à côte agrandie : `python $S/cote_a_cote.py --ref analyse/images/ref_0990.png --nous controle/nous.png -o revue/element-ref-vs-nous.jpg --zoom-ref 351,840,110 --zoom-nous 400,700,110 --k 4`.

**Le décor a son propre contrôle** (`references/controle-chiffre.md`, § 9), sur des images **à cadrage comparable** (même ambiance, même type de plan), comparées **en D** :
```
python $S/mesurer_decor.py controle/cibles/nous_0120.json controle/mesures
python $S/comparer_decor.py controle/paires-decor.json controle --ref analyse/mesures --nous controle/mesures --tour 1
```
Tolérances : **palette ΔE < 8 et parts à ± 8 points ; couleur d'ombre ΔE < 6, dureté ± 30 % ; texture : fréquence ± 20 %, contraste ± 6 niveaux ; contours ± 1 px ; flou de profondeur ± 25 % ; netteté du sol ± 1 px ; densité ± 25 %.** Quatre tours au plus, là aussi. Trois pièges : un fil du bois marqué est compté comme des joints (compare la période d'autocorrélation) ; l'indicateur « segments » compte des zones de couleur, pas des objets ; une ligne qui ne bouge plus après deux tours de réglage a sa cause en amont, dans le rendu. Dans notre essai : 23 lignes dans la tolérance sur 59 au premier assemblage, 37 sur 61 au quatrième tour, 34 après les corrections demandées par le critique (elles ont fait perdre trois lignes, et l'œil y a gagné : c'est un choix, on l'écrit).

Puis la **liste de contrôle par plan**, que le tableau ne remplace pas : rien de nu derrière les personnages, une source de lumière visible, un contrepoint froid dans une ambiance chaude, aucun objet coupé par le cadre, des formes contrastées dans le fond, le sol net et le personnage posé.

### 9. Plans de test, puis critique indépendante
Détail et consigne du critique : `references/plans-de-test-et-critique.md`.
1. **Avant le film entier, rends 3 à 5 plans de test** (8 à 10 s) qui couvrent les ambiances et les types de cadrage. Lance les rendus au premier plan et attends-les.
2. **Planche à trois colonnes** (référence au cadrage le plus proche / version précédente / nouvelle version), avec un recadrage agrandi de l'élément clé : `python $S/cote_a_cote.py revue/planche.json` (gabarit `gabarits/planche.json`).
3. **Critique par un agent indépendant**, qui n'a pas fait le travail, **avec la référence sous les yeux** : donne-lui `gabarits/consigne-critique.md`, les plans de test, la planche et les images pleine résolution. Il note sur 10 et liste ce qui trahit la différence.
4. **Trie ses remarques avec la mesure.** Pour chacune : retenue, non retenue, reportée, avec la raison. **Quand le critique et la mesure se contredisent, la mesure tranche** : dans notre essai, deux remarques sur dix ont été démenties par les chiffres (un rapport d'épaisseur « vu » trop faible, une ombre « vue » du mauvais côté). À l'inverse, ce que la mesure ne couvre pas (une ombre qui flotte, un effet autocollant) se corrige sur la foi du critique.
5. Un tour de corrections, puis une seconde critique si le temps le permet. Sinon, dis que la note porte sur l'état d'avant corrections.

### 10. Validation par le client, puis le film entier
Montre au client : les plans de test, la planche à trois colonnes, **la note du critique telle quelle**, le tableau d'écart, ce qui reste différent et pourquoi, et le temps que prendra le film entier. Il valide, demande un tour de plus, ou change de cap.

Après son accord seulement, le film entier suit le parcours de `studio-coeur` à partir de l'étape 4 (storyboard validé, construction, revue, livraison), avec la fiche `recreation-reel` pour le cahier plan par plan et le contrôle du rythme.

Écris le compte rendu d'après `gabarits/compte-rendu.md`.

## Liste de contrôle

- [ ] La référence est restée chez le client ; aucune image d'elle dans le film, un aperçu ou un dépôt.
- [ ] Chaque borne de plan a été vérifiée à l'image, et le survol a été regardé pour les transitions non détectées ; le découpage dit s'il s'agit de coupes ou de stations.
- [ ] Lecture continue faite sur l'accroche et sur chaque plan où ça joue, durées en images.
- [ ] Images mesurées : grandes, nettes, toutes les ambiances ; netteté notée ; aucune image en mouvement dans la loi sans confirmation.
- [ ] Sur chaque image de contrôle (`_bords.jpg`), les points suivent bien les bords du trait ; les secteurs collés à un autre trait sont exclus.
- [ ] Tout est exprimé en fraction d'une grandeur de référence.
- [ ] Fiche de style : aucune ligne sans chiffre ni image ; tableau « on reprend / on ne reprend pas » confirmé par le client.
- [ ] Aucun personnage, costume, accessoire, texte, voix, musique, logo ni sujet du reel étudié.
- [ ] Contrôle chiffré fait avec les mêmes scripts, élément rendu à la même taille ; 4 tours au plus ; lignes rouges expliquées.
- [ ] Décor : mesuré avant d'être construit (parallaxe, matières, contours, ombres, palette, optique, finitions, lointain), toutes les ambiances, tout en D ; la même bande exclue des deux côtés ; chaque planche `_decor_planche.jpg` ouverte.
- [ ] Décor : contrôle chiffré sur des images à cadrage comparable, bilan par famille écrit ; liste de contrôle par plan passée ; aucun lieu, bâtiment, meuble ni accessoire de la référence.
- [ ] Plans de test critiqués par un agent indépendant ; remarques triées avec la mesure ; note écrite telle quelle.
- [ ] Temps annoncé avant, temps réel écrit après.
- [ ] Aucune tâche ne tourne quand tu rends la main.

## Fichiers

| Fichier | Contenu | Quand le lire |
|---|---|---|
| `references/droits-et-limites.md` | ce qu'on reprend, ce qu'on refuse, comment le dire, récupérer la référence | avant de commencer |
| `references/lecture-continue.md` | lire une bande, mesurer des durées, partager le travail | étape 3 |
| `references/fichier-de-cibles.md` | choisir les images, format du fichier de cibles, lire les sorties, limites de la mesure ; § 8 : la rubrique `decor` | étapes 4 et 5 |
| `references/decors-camera-montage-son.md` | § 1 : la méthode complète du décor (neuf familles) et le diagnostic type « pourquoi mon décor ne ressemble pas » ; puis caméra, montage, sous-titres, son | étape 5 |
| `references/controle-chiffre.md` | rendu de contrôle, fichier de paires, tolérances, tours ; § 9 : le contrôle du décor, ses tolérances, ses pièges, la liste de contrôle par plan | étape 8 |
| `references/plans-de-test-et-critique.md` | plans de test, planche à trois colonnes, consigne et tri de la critique | étape 9 |
| `gabarits/lecture-continue.md` | tableau image par image à remplir | étape 3 |
| `gabarits/cibles.json`, `paires.json`, `paires-decor.json`, `planche.json` | fichiers d'exemple à adapter (les coordonnées sont des exemples) | étapes 4, 5, 8, 9 |
| `gabarits/fiche-reference.md` | la fiche de style de la référence | étape 6 |
| `gabarits/consigne-critique.md` | consigne à donner au critique indépendant | étape 9 |
| `gabarits/compte-rendu.md` | compte rendu au client | étape 10 |

Crédits : `licenses/reproduire-reel.md` à la racine du plugin.
