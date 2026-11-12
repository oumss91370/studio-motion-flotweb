# Mesure au pixel : choisir les images, écrire le fichier de cibles, lire les sorties

`mesurer.py` ne devine pas ce qu'il doit mesurer : tu le lui désignes dans un **fichier de cibles**, un fichier JSON par image. Tout le reste (bords du trait, épaisseurs, couleurs, ombrage) est mesuré. Les mêmes scripts servent pour la référence et pour nos rendus : seul le fichier de cibles change.

## 1. Choisir les images à mesurer

| Critère | Pourquoi | Comment le vérifier |
|---|---|---|
| L'élément est **grand** | un trait de moins de 4 px se confond avec le lissage ; un remplissage de moins de 9 px de large n'est pas mesuré | plan en pied ou plus serré ; tête d'au moins 200 px de diamètre |
| L'image est **nette** | le flou de mouvement élargit les bords | `<prefixe>_nettete.json` de `extraire.py` : sous 4 = figé, au-dessus de 10 = en mouvement |
| **Toutes les ambiances** | la palette et le côté de l'ombre changent avec la lumière | au moins une image par ambiance, deux si possible |
| Des **gros plans** et des **plans d'ensemble** | une épaisseur proportionnelle à la taille ne se prouve que sur plusieurs tailles | au moins 2 de chaque |
| L'élément est **dégagé** | un chapeau, une main ou un col collé au contour cache le trait | chercher au moins une image où il est nu (tête sans chapeau) |

Compte 8 à 12 images pour un reel d'une minute. Note pour chacune : ambiance, type de plan, netteté, ce qui gêne (chapeau, décor flou, caméra en mouvement).

Une vidéo en ligne est compressée : les bords sont lus au quart de pixel mais ne sont fiables qu'au demi-pixel. Écris-le dans la fiche.

## 2. Poser les cibles

```
python $S/grille.py analyse/images/ref_0990.png analyse/cibles/grille_0990.jpg 150 600 600 1300 --k 2 --pas 50
```
Ouvre la grille, lis les coordonnées (x vers la droite, y vers le bas, en pixels de l'image d'origine) et écris le fichier. Commence par une grille de l'image entière (sans boîte), puis une grille agrandie de chaque élément.

Règles de pose, tirées de l'essai :

| Cible | Comment la poser |
|---|---|
| Cercle | centre et rayon à 10 ou 15 % près : le script ajuste un cercle sur le bord du remplissage. **Tête coiffée d'un chapeau** : déduis le centre du bas et de la largeur visibles ; le cercle ajusté est dessiné en blanc sur l'image de contrôle, vérifie-le là |
| Polygone, rectangle, masque (lassos) | 20 à 40 px au large de la forme. Le lasso peut mordre sur une forme voisine **d'une autre couleur** (elle est ignorée) ; un objet de même couleur ou posé sur le contour s'écarte par une boîte `exclure` |
| Texte (`"composantes": "toutes"`) | une boîte large suffit : seuls les morceaux de la couleur du texte **entièrement dans la boîte** sont gardés, le décor clair autour ne compte pas |
| Coupe | les deux bouts **sur des aplats**, de part et d'autre du trait, à 30 px au moins du trait. Nomme-la par sa position (« torse, bord gauche ») : le côté ombre et le côté lumière se décident après la mesure |
| Trait constant (`membres`) | les deux bouts sur l'axe du trait ; `demi` est la demi-longueur des coupes en travers, **en pixels** : 1,5 fois l'épaisseur du trait au moins (28 pour un trait de 18 px). Arrête le segment avant qu'il ne passe devant une ombre ou un objet sombre |
| Ombre | `a` sur le sol éclairé, `b` dans l'ombre, à 0,3 D environ de part et d'autre du bord (une centaine de pixels pour une tête de 300 px) : le flou du bord doit tenir entre les deux |

## 3. Format du fichier de cibles

```json
{
  "id": "ref_0990",
  "image": "../images/ref_0990.png",
  "ambiance": "coucher de soleil",
  "plan": "plan en pied à deux",
  "note": "plan figé ; décor flou derrière",
  "reference": {"nom": "D (diamètre de la tête)", "forme": "tete-a"},
  "formes":  [ … ],
  "coupes":  [ {"nom": "contour du torse, côté ombre", "groupe": "torse", "a": [200, 1120], "b": [300, 1120]} ],
  "membres": [ {"nom": "jambe gauche", "a": [312, 1340], "b": [312, 1600], "n": 9, "demi": 28} ],
  "bouts":   [ {"nom": "bout du pied", "a": [300, 1650], "b": [360, 1650], "largeur": 18} ],
  "zones":   [ {"nom": "torse", "poly": [[260, 1060], [420, 1060], [420, 1200], [260, 1200]], "k": 3} ],
  "ombres":  [ {"nom": "ombre au sol", "a": [620, 1560], "b": [480, 1560]} ]
}
```

| Champ | Contenu |
|---|---|
| `id` | nom des fichiers de sortie. Garde un préfixe commun pour la référence (`ref_…`) : `synthese.py` s'en sert |
| `image` | chemin relatif **au fichier de cibles**, ou absolu ; `video.mp4@990` prend l'image 990 de la vidéo |
| `ambiance`, `plan`, `note` | texte libre, recopié dans les sorties ; `ambiance` regroupe les palettes dans la synthèse |
| `reference` | la grandeur de référence : `{"nom": …, "forme": "<nom d'un cercle>"}` (son diamètre D, mesuré) ou `{"nom": "hauteur de capitale", "px": 53}` (valeur donnée). Sans ce champ : le premier cercle mesuré |

Toutes les rubriques sont facultatives. `"traits"` est un autre nom de `"membres"`.

### Les formes

Une forme est une **surface remplie, cernée d'un trait**. Cinq façons de la désigner :

| Type | Écriture | Ce que fait le script |
|---|---|---|
| `cercle` | `{"nom": "tete-a", "type": "cercle", "centre": [351, 840], "rayon": 148}` | **modèle** : il ajuste un cercle sur le bord du remplissage ; ce qui s'en écarte (chapeau, main, bord du cadre) est écarté, avec son motif |
| `ellipse` | `{"nom": "ecusson", "type": "ellipse", "centre": [540, 300], "axes": [120, 80], "angle": 0}` | **modèle** : une ellipse est ajustée (`axes` = demi-axes en px, `angle` en degrés, sens trigonométrique) |
| `rectangle` | `{"nom": "sous-titre", "type": "rectangle", "boite": [240, 1300, 840, 1400]}` | **lasso** : le remplissage est cherché dans la boîte |
| `polygone` | `{"nom": "torse", "type": "polygone", "points": [[215, 1010], [490, 1010], [490, 1330], [215, 1330]], "graine": [330, 1180]}` | **lasso** de forme libre |
| `masque` | `{"nom": "manteau", "type": "masque", "fichier": "masques/manteau.png", "graine": [700, 1150]}` | **lasso** peint : image de la taille de l'image mesurée, blanc = dedans |

Un **modèle** sait dire qu'un autre objet passe devant la forme. Un **lasso** dit seulement où chercher : trace-le large (20 à 40 px autour de la forme), il ne doit pas couper le trait. Un bord que le lasso coupe est écarté (« bord coupé par la cible »).

Options d'une forme (toutes facultatives) :

| Option | Défaut | Rôle |
|---|---|---|
| `graine` | centre du cercle ou de l'ellipse, centre de gravité du lasso | un point `[x, y]` **dans le remplissage**, sur sa couleur dominante. À donner dès que le centre du lasso tombe sur un détail (bouton, œil) |
| `rayon_graine` | moitié du rayon (cercle), moitié du petit demi-axe (ellipse), 8 px sinon | rayon de la pastille où la couleur du remplissage est lue |
| `composantes` | `"graine"` | `"toutes"` : tous les morceaux de la couleur du remplissage dans le lasso (les lettres d'un texte) |
| `remplissage` | `"clair"` | avec `"composantes": "toutes"` et sans graine : `"clair"`, `"sombre"`, ou une couleur `"#rrvvbb"` |
| `trait` | `"sombre"` | `"clair"` si le contour est plus clair que le remplissage |
| `encre` | mesurée | couleur du trait `"#rrvvbb"`, à donner quand le plus sombre de la zone n'est pas le trait |
| `exclure` | aucune | boîtes `[[x0, y0, x1, y1], …]` où le bord ne doit pas être mesuré (accessoire qui touche la forme) |
| `exclure_angles` | aucun | plages d'orientation `[[255, 290], …]` à ignorer (le cou, par exemple) |
| `trous` | non (oui avec `"toutes"`) | mesurer aussi le bord des trous du remplissage (l'intérieur d'un « o ») |
| `portee_trait` | 30 % du rayon inscrit, 24 px au moins | épaisseur maximale de trait cherchée, en px |
| `tolerance_couleur` | 0,75 (0,3 avec `"toutes"`) | part de l'écart remplissage → encre au-delà de laquelle une couleur ne fait plus partie du remplissage (monter à 0,9 pour un remplissage très dégradé) |
| `aire_min` | 20 | avec `"toutes"` : aire minimale d'un morceau, en px (écarte les poussières) |
| `lissage` | 2 | lissage du bord en px avant de calculer les normales (lassos) |
| `ombrage` | oui (non avec `"toutes"`) | mesurer l'ombrage du remplissage |
| `details` | oui (sans objet avec `"toutes"`) | relever les détails dessinés dans la forme |
| `seuils` | `{"interieur": 70, "sortie": 60}` | écarts de couleur minimaux (0 à 441) ; à baisser pour un trait peu contrasté |

L'ancienne écriture `"tetes": [{"nom": "a", "graine": [x, y, rayon]}]` est encore lue comme un cercle.

### Les autres cibles

| Rubrique | Écriture | Ce qui sort |
|---|---|---|
| `coupes` | segment `a` → `b` **en travers** d'un trait ou d'une bande, bouts posés sur des aplats | la suite des aplats traversés (couleur, largeur) : trait, filet de lumière, bande d'ombre ; et la bande la plus marquée avec ses largeurs de transition |
| `membres` (ou `traits`) | segment `a` → `b` posé **sur l'axe** d'un trait d'épaisseur constante ; `n` coupes, `demi` = demi-longueur des coupes | épaisseur médiane, écart type, effilement du début à la fin, couleur |
| `bouts` | `a` dans le trait, `b` au-delà du bout, `largeur` du trait | forme de l'extrémité (rond, carré). Mesure fragile : confirmer à l'œil sur la planche |
| `zones` | polygone `poly` dans un aplat, `k` couleurs | couleurs dominantes et leurs parts, écart teinte / saturation / luminosité entre elles, dégradé, grain |
| `ombres` | `a` sur le sol éclairé, `b` dans l'ombre | les deux couleurs, le facteur par canal (rouge, vert, bleu), le flou du bord (10–90 %) |

## 4. Ce que mesure le script sur une forme

Le long du bord du remplissage (tous les degrés pour un cercle, tous les pixels sinon), une coupe est lue **en travers du bord**, tous les 0,25 px.
- **Bord intérieur du trait** : là où la couleur est à mi-chemin entre le remplissage et l'encre. **Bord extérieur** : à mi-chemin entre l'encre et le décor. **Épaisseur** = l'un moins l'autre.
- Chaque coupe est rangée selon **l'orientation du bord** : 0° = le bord regarde à droite, 90° = en haut, 180° = à gauche, 270° = en bas. La valeur publiée tous les 5° est la médiane des coupes à ±2,5°. Pour un cercle, c'est l'angle autour du centre.
- **La loi simple** (`loi_simple`) : `épaisseur = a0 + h1 × cos(orientation − direction du plein)`. `a0` est l'épaisseur moyenne, `h1` l'amplitude plein / délié, la direction du plein dit de quel côté le trait est le plus épais ; `delie_px = a0 − h1`, `plein_px = a0 + h1`. **C'est elle qui va dans la fiche**, et c'est la même que dans `synthese_formes.md`. Lecture géométrique : un fond d'encre, et par-dessus le remplissage **décalé de `h1` vers le côté du délié**. Pour un texte, le même calcul donne le contour (`a0`) et le demi-décalage de l'ombre portée (`h1` et sa direction).
- Le champ `loi` (deux harmoniques) sert seulement à mesurer la régularité du trait (`tremble_px`) : sa deuxième harmonique est propre à chaque dessin. Ne recopie pas ses coefficients dans la fiche.
- **Coupes écartées**, avec leur motif dans `angles_ecartes` : autre objet devant la forme ; décor aussi sombre que le trait ; intérieur aussi sombre que le trait ; remplissage trop étroit ; bord coupé par la cible ou par le cadre ; trop peu de bord dans cette orientation (coin, petite forme) ; valeur isolée (trait collé à un autre objet).
- **Une cible mal écrite n'arrête pas les autres** : son message va dans `erreurs`, en fin de fichier, et s'affiche à l'écran. Un cercle qui n'a pas 6 orientations mesurables ne donne pas de diamètre et ne peut pas servir de grandeur de référence (`avertissement`).

Sorties, dans le dossier donné :

| Fichier | Contenu |
|---|---|
| `<id>.json` | tous les chiffres : `formes.<nom>.contour` (taille, `courbe_5deg`, `loi_simple`, `loi`, `secteurs`, `trait`, `bord`, `accentuation`, `halo_luminance`, `angles_ecartes`, `en_reference`), `.ombrage` (`deux_zones`, `frontiere`, `profils_diametres`, `reflets`, `lisere`, `grain_ecart_type`), `.details_internes`, `.composantes` ; puis `coupes`, `membres`, `bouts`, `zones`, `ombres`, `reference` |
| `<id>_<forme>_bords.jpg` | **l'image de contrôle, à ouvrir à chaque fois** : la forme agrandie, points rouges sur le bord intérieur du trait, cyan sur le bord extérieur, gris pour les orientations écartées, cercle ajusté en blanc, épaisseur écrite tous les 30° |
| `<id>_planche.jpg` | la planche d'ensemble (toutes les formes, courbes, cartes, coupes) : pour le dossier, trop grande pour vérifier les points |
| `<id>_<forme>_courbe.png` | épaisseur du contour selon l'orientation, avec la loi ajustée |
| `<id>_<forme>_profils.png` | luminance le long de quatre droites par le centre |
| `<id>_<forme>_carte.png` | fausses couleurs de la luminance, carte des deux zones, écarts de couleur × 4 |

Lecture des principaux chiffres :

| Chiffre | Ce qu'il dit |
|---|---|
| `loi_simple.delie_px`, `plein_px` (et `_D`) | le côté fin et le côté épais du trait, lus sur la loi : à préférer aux extrêmes bruts |
| `epaisseur_min_px`, `epaisseur_max_px`, `rapport_max_min` | extrêmes bruts de la courbe : trait constant (rapport proche de 1) ou à pleins et déliés (rapport de 3 à 5). Le maximum brut est souvent gonflé par un trait voisin |
| `loi_simple.plein_vers_deg` | côté du plein. À comparer à `ombrage.frontiere.axe_vers_le_clair_deg`, le côté clair mesuré sur l'ombrage : si le plein est à l'opposé du clair, le trait est épais côté ombre |
| `en_reference` | les mêmes longueurs divisées par la grandeur de référence de l'image, rappelée dans `rapporte_a` |
| `tremble_px` | écart type autour de la loi : trait régulier (moins de 1 px) ou tracé à la main |
| `ovale.rapport` | 1 = cercle parfait ; 0,91 à 0,98 = forme dessinée à la main |
| `bord.transition_int_px` | dureté du bord : ≈ 1 px = net et lissé ; 2 à 4 px = bord doux ou flou |
| `accentuation` | un pixel plus clair côté remplissage, un pixel plus sombre dans le trait : signature d'un filtre de netteté sur l'image finale |
| `halo_luminance.median` | proche de 0 = pas de halo ni de contour clair autour de la forme |
| `deux_zones` | couleur et part de la zone claire et de la zone sombre du remplissage ; `delta_e` entre les deux. **Lis `lecture`** : « zone sombre » ne veut pas dire « ombre ». La couleur de base est la zone la plus étendue (`base`) ; l'autre est une ombre propre (plus sombre, 8 à 50 %), un liseré (moins de 8 %) ou une plage de lumière (plus claire) |
| `composantes` (texte) | nombre de morceaux, `hauteur_des_grandes_lettres_px` (capitales et lettres à hampe), `hauteur_des_petites_lettres_px`, `boite` et `centre` **du texte** (pas de la cible) |
| `frontiere` | où passe la limite d'ombre (`position_au_centre_R`), de quel côté est le clair, le saut de luminance, la largeur du bord doux (`transition_D`) |
| `degrade_lineaire.r2`, `degrade_radial.r2` | proche de 1 = c'est un dégradé ; faible = ce n'en est pas un (aplat + ombre) |
| `grain_ecart_type` | sous 2 = aucun grain (bruit de compression) ; au-dessus de 4 = grain ou texture |
| `details_internes` | chaque détail dessiné dans la forme : anneau, trait ou forme pleine, sa taille et son épaisseur |
| `ombres.<nom>.facteur_rvb` | une vraie multiplication baisse les trois canaux ; un facteur bleu supérieur à 1 signale une ombre **teintée** (un mélange avec une couleur) |

## 5. Vérifier avant de croire

1. Ouvre `<id>_<forme>_bords.jpg` : les points rouges (bord intérieur) et cyan (bord extérieur) suivent-ils le trait ? Le cercle blanc épouse-t-il la forme ? Un nuage de points sur un accessoire = une boîte `exclure`.
2. **Un maximum très au-dessus des autres** est presque toujours un endroit où le trait touche un autre trait (le cou, une main, un chapeau) : sur l'image de contrôle, les points cyan y suivent l'autre trait. Lis l'orientation sur les étiquettes jaunes (tous les 30°), exclus le secteur entier (`"exclure_angles": [[235, 290]]` pour un cou), relance. Si le maximum ne fait que se déplacer au bord du secteur, élargis-le. Dans tous les cas, **le plein de la fiche est `loi_simple.plein_px`**, pas le maximum brut.
3. Regarde `angles_valides` : sous 27 orientations sur 72, la loi de cette forme est fragile ; `synthese.py` l'écarte et le dit.
4. Un cercle dont le haut est caché a un diamètre surestimé de quelques pour cent : dis-le.
5. Une image en mouvement (netteté au-dessus de 10) n'entre pas dans la loi : `synthese.py --sans ref_0512`.
6. Refais une mesure douteuse sur une deuxième image avant de l'écrire dans la fiche.

## 6. Limites connues

- Forme ronde de moins de 20 px de rayon : aucune orientation mesurable (le script le dit). Prendre une image où elle est plus grande.
- Remplissage de moins de 9 px de large (lettres fines, traits) : pas de mesure de contour ; utiliser une `coupe`.
- Image à fond transparent : elle est posée sur un gris moyen, avec un avertissement ; le bord extérieur du trait se mesure alors contre ce gris, pas contre un décor. Pour un contrôle chiffré, rendre sur un fond.
- Vidéo HDR (certains téléphones) : convertie sans correction, les couleurs lues sont fausses. Demander un export SDR.
- Contour moins contrasté que 60 (écart de couleur) avec le remplissage : erreur explicite ; donner `encre` ou baisser `seuils`.
- Les angles d'un rectangle et les pointes : peu de coupes par orientation, valeurs écartées.
- Deux formes de même couleur qui se touchent sans trait entre elles sont prises pour une seule : les séparer par un lasso plus serré ou un masque.
- La mesure du bout d'un trait (`bouts`) est peu fiable.
- Le contour d'un polygone est mesuré sur tout le bord du remplissage, y compris les encoches que font les détails posés sur le bord (franges, ceinture) : exclure ces zones, ou préférer deux `coupes` pour un chiffre net.

## 7. Ce qui a été essayé

Essai du studio du 12/11/2026, sur un reel en 1080 × 1920 compressé en VP9, par un agent qui ne connaissait que ce skill.

| Cas | Résultat |
|---|---|
| `cercle` : 6 têtes sur 4 images (plein jour, coucher de soleil, nuit) | concorde avec une mesure indépendante faite avec d'autres scripts : diamètre à 0,5 px près, loi (`a0`, `h1`) à 0,3 px près, direction du plein à 2° près, couleurs identiques ou à un niveau près |
| `polygone` : un torse | contour mesuré sur 35 orientations sur 72 ; les deux `coupes` posées sur ses bords concordent à 0,4 px près avec la mesure indépendante |
| `rectangle` avec `"composantes": "toutes"` : un sous-titre | après correction du script (le décor clair de la boîte était compté comme du texte) : hauteur des capitales, centre et contour concordent avec un relevé à la main |
| `coupes`, `membres`, `ombres` | concordent (épaisseur d'une jambe à 0,01 px près ; ombre au sol : même conclusion, valeurs différentes parce que la coupe n'était pas au même endroit) |
| `ellipse`, `masque`, option `"trait": "clair"`, trait constant, ombre floue | essayés sur des **formes dessinées à épaisseur connue** (pas sur une vraie vidéo) : cercle 13 − 8 cos retrouvé à 12,9 − 8,0 ; ellipse de 10 px à 9,8 ; masque de 14 px à 14,0 ; contour clair de 9 px à 9,0 ; trait de 18 px à 18,0 ; flou d'ombre de 31 px à 31,8 |
| `zones`, `bouts` | repris des scripts d'origine, non rejoués dans cet essai |
| Cas limites, rejoués après une relecture indépendante du code | vidéo avec rotation, cadence variable, 8 images ; cercle coupé par le cadre (les orientations coupées sont écartées, le reste est juste) ; image à fond transparent ; fichier de cibles enregistré avec une marque d'ordre des octets ; cible incomplète |
| Non essayé | macOS et Linux (essais sous Windows seulement) ; Python 3.9 (syntaxe vérifiée, non exécuté) ; FFmpeg 5 et 6 (essais avec une version récente) ; vidéo HDR ; enregistrement d'écran |
