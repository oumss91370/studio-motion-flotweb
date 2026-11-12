# Décors, caméra, montage, sous-titres, son : ce qu'on mesure et comment

La mesure au pixel des formes (étape 4) donne le rendu des éléments dessinés. Cette étape relève le reste. Même règle : un chiffre et une image par affirmation.

## 1. Décors

| Ce qu'on mesure | Outil | Ce qu'on écrit |
|---|---|---|
| **Palette par ambiance** | `python $S/palette.py analyse/decoupage/plans/P03_i0179.png analyse/palettes/jour.json --nom "plein jour" --k 6` sur une image nette de chaque ambiance | 3 à 6 couleurs avec leur part, luminance moyenne, contraste, saturation, dominante chaude ou froide |
| **Rôle de chaque couleur** | même script avec `--boite x0,y0,x1,y1` sur le ciel, le sol, un mur | ciel (haut et horizon), sol, murs, accent |
| **Traitement des ombres** | cible `ombres` de `mesurer.py` : `a` sur le sol éclairé, `b` dans l'ombre | les deux couleurs, le facteur par canal, le flou du bord. Facteur bleu au-dessus de 1 = ombre teintée (mélange avec une couleur), pas une multiplication |
| **Contours du décor** | cibles `coupes` en travers d'une arête | épaisseur, couleur (une version sombre de la teinte locale ? un liseré clair de nuit ?) |
| **Matière** | cible `zones` dans un aplat | grain (écart type), dégradé, nombre de tons |
| **Type de rendu** | regard sur l'image pleine résolution, appuyé sur les mesures | aplats, textures peintes, rendu réaliste, 3D au rendu dessin animé… |

Unités du « look » de `palette.py` : `luminance_moyenne` de 0 à 255 ; `contraste` = écart type de la luminance, en niveaux ; `saturation_moyenne` de 0 à 1 ; `dominante_chaude` = moyenne de (rouge − bleu), en niveaux, positive pour une image chaude, négative pour une image froide ; `nettete` sans échelle absolue (voir § 2).

Si la palette du client doit remplacer celle de la référence, garde les **rapports** mesurés : écart de luminance entre sol éclairé et ombre, saturation moyenne, nombre de teintes dominantes par ambiance.

## 2. Profondeur de champ et netteté

- Compare la netteté de deux zones de la même image : `palette.py … --boite` sur le sujet puis sur le fond ; le champ `look.nettete` (énergie des contours) chute sur une zone floue. Ce nombre ne se compare qu'entre deux zones d'une **même** image. Un rapport de 3 ou plus = profondeur de champ courte (15 dans notre essai : sujet 51,8, fond 3,4).
- La largeur de transition du bord extérieur d'une forme (`bord.transition_ext_px`) grandit devant un fond flou ; celle du bord intérieur reste celle du dessin.
- Note où est le plan net (sujet), ce qui est flou (fond, premier plan), et s'il y a du flou de mouvement (comparer une image en plein déplacement de caméra à une image figée).

## 3. Caméra et cadrage

Par plan (ou par station), dans le tableau des plans de la fiche :

| Colonne | Comment la relever |
|---|---|
| Type de cadrage | plan d'ensemble, en pied, taille, gros plan, très gros plan ; plongée, contre-plongée, ras du sol |
| Taille du sujet | hauteur du sujet en % de la hauteur du cadre, sur l'image nette du plan (`grille.py`) |
| Position | où sont la tête, les pieds, l'horizon, en % de la hauteur |
| Mouvement | fixe, dérive, panoramique, travelling, zoom, coup de zoom |
| Vitesse et durée | images de départ, de croisière, de freinage, lues sur les bandes ; `mouvement.csv` donne l'intensité image par image |
| Dérive pendant les tenues | déplacement d'un point fixe du décor entre deux images éloignées de 30, en px par seconde |

Cherche le **cadrage dominant** (celui qui revient le plus) et **où passent les sous-titres** par rapport au sujet.

## 4. Montage

- Durée des plans ou des stations : médiane, plus court, plus long (`plans.md`).
- Chaque transition : type exact (coupe, fondu, filé, zoom traversant, raccord dans un objet) et durée en images, vérifiée sur `bornes-a-verifier-N.jpg`.
- Le plan entrant est-il déjà en mouvement ? La transition est-elle la sortie du plan ?
- Structure : accroche, développement, chute ; ce qui se passe dans les 3 premières secondes, image par image.

Le cahier plan par plan (une fiche par plan, critères d'acceptation) et le contrôle du rythme du film fini sont décrits dans la fiche `recreation-reel` du skill `formats-flotweb` : ne les réécris pas ici.

## 5. Sous-titres

1. Extrais une image où un carton est bien visible, en pleine résolution.
2. Cible :
```json
{"nom": "sous-titre", "type": "rectangle", "boite": [240, 1290, 840, 1410], "composantes": "toutes", "remplissage": "clair"}
```
   (`"remplissage": "sombre"` pour un texte sombre, `"trait": "clair"` pour un contour clair.)
3. Lis dans la sortie :

| Grandeur | Champ |
|---|---|
| Hauteur des lettres | `composantes.hauteur_des_grandes_lettres_px` (capitales et lettres à hampe), `hauteur_des_petites_lettres_px` |
| Position | `composantes.centre` et `boite` : ceux **du texte**, à rapporter à la largeur et à la hauteur du cadre (en %) |
| Couleur du texte et du contour | `contour.remplissage_hex`, `contour.trait.hex` |
| Épaisseur du contour | `contour.loi_simple.a0_px` (moyenne) et `secteurs` (haut, bas, gauche, droite) |
| Ombre portée | `contour.loi_simple.h1_px` = demi-décalage, `plein_vers_deg` = sa direction. Contour plus épais en bas à droite = ombre décalée vers le bas à droite. Sous 0,5 px : pas d'ombre décalée |
| Netteté du bord | `contour.bord.transition_int_px` |

Vérifie sur `<id>_sous-titre_bords.jpg` que seules les lettres sont cernées de points. Les valeurs `_ref` d'un texte sont rapportées à la grandeur de référence de l'image (souvent une tête) : pour un sous-titre, rapporte plutôt le contour à la hauteur des lettres, à la main.

4. Sur les bandes de lecture continue, compte : le nombre de mots par carton (moyenne, extrêmes), la durée d'un carton en images, l'animation d'entrée et de sortie (aucune, saut, échelle), la casse et la ponctuation.
5. La police : décris la famille (grotesque grasse, condensée, ronde…) et prends la police libre la plus proche ou celle du client (skill `rendu`, section des polices). On ne cherche pas à identifier ni à reprendre une police propriétaire.

## 6. Son

| Ce qu'on mesure | Comment |
|---|---|
| Niveau | `ffmpeg -i reference/ref.mp4 -map 0:a:0 -af ebur128=peak=true -f null -` : dans le résumé final, lignes `I:` (niveau intégré, en LUFS), `LRA:` (dynamique, en LU) et, sous « True peak », `Peak:` : c'est la crête vraie, que FFmpeg écrit en dBFS et qu'on note en dBTP |
| Place des bruitages | avec l'écoute mesurée du skill `son` : chaque évènement sonore et son instant ; puis l'écart avec l'image du geste, relevée en lecture continue (en millisecondes, avant ou après) |
| Densité | nombre de bruitages par tranche de 10 s |
| Musique | continue ou non, s'arrête-t-elle avant une chute, niveau par rapport à la voix (en dB) |
| Voix | nombre de mots, débit en mots par seconde, pauses de plus de 0,3 s |
| Action et mot | décalage entre le mot prononcé et l'action à l'image (en images) |

Une vidéo sans piste son fait échouer la commande (« matches no streams ») : écris alors « pas de son » dans la fiche.

Sans l'écoute mesurée : extrais la forme d'onde autour d'un geste (`ffmpeg -ss <t> -t 1 -i … -filter_complex showwavespic`) et lis l'attaque à l'œil ; écris « lu sur la forme d'onde ».

On relève **la place et le rôle** des sons. On ne reprend ni la musique, ni la voix, ni un bruitage extrait de la référence.
