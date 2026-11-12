# Décors, caméra, montage, sous-titres, son : ce qu'on mesure et comment

La mesure au pixel des formes (étape 4) donne le rendu des éléments dessinés. Cette étape relève le reste. Même règle : un chiffre et une image par affirmation.

## 1. Décors : la méthode complète

Un décor « fait à l'œil » d'après l'idée générale d'un reel (« aplats saturés, contour, ombre bleue ») ne ressemble pas. Dans l'essai du studio, un décor refait d'après neuf familles de mesures est passé, pour le critique indépendant, de 3,5 à 6 sur 10 (la référence étant notée 9) : c'est mieux, ce n'est pas encore le niveau de la référence, et le contrôle chiffré dit où (§ 1.11). Les neuf familles, dans l'ordre où on les relève :

| N° | Famille | Question | Outil | § |
|---|---|---|---|---|
| 1 | Volume ou peint | qu'est-ce qui est un vrai volume, qu'est-ce qui est un plan peint ? | `parallaxe.py` | 1.2 |
| 2 | Densité et vocabulaire | combien d'éléments par image, de quelles familles, de quelle taille ? | `mesurer_decor.py` (global, `details`) et compte à l'œil | 1.3 |
| 3 | Matières | aplat ou texture ? quelle fréquence, quel contraste ? | cibles `texture` | 1.4 |
| 4 | Contours du décor | y a-t-il un trait ? où, de quelle épaisseur, de quelle couleur ? | cibles `trait` | 1.5 |
| 5 | Lumière et ombres | couleur, dureté et mélange des ombres ; tons par face ; lampes | cibles `bord`, `zone`, `halo` | 1.6 |
| 6 | Palette par ambiance | quelles dominantes, quelle saturation, quelle luminance ? | `synthese_decor.py` | 1.7 |
| 7 | Optique | focale, hauteur de caméra, profondeur de champ, **netteté du sol sous le sujet** | `focale.py`, cibles `bord`, `nettete`, `optique` | 1.8 |
| 8 | Finitions au sol | cailloux, touffes, traces : combien par D², de quelle taille ? | cibles `details` | 1.9 |
| 9 | Lointain et traitement final | ciel, soleil, brume, bords assombris, grain, accentuation | `graines`, cibles `zone`, `bord`, `halo` | 1.10 |

**Tout s'exprime en D**, le diamètre de la tête du personnage principal à l'image (ou une autre grandeur de référence : hauteur d'un titre, largeur d'un objet). C'est ce qui rend une mesure transposable d'un plan à l'autre et de la référence à nos scènes : une lame de plancher de 61 px quand la tête en fait 190, c'est 0,32 D, et ça se refait à toute échelle.

### 1.1 Choisir les images et lancer la mesure

- **15 à 20 images** pour un reel d'une minute : **toutes les ambiances** de lumière (au moins 2 images chacune), et pour chaque ambiance un plan large, un plan moyen, un gros plan. Ajoute les plans au ras du sol (finitions) et, s'il existe, **un intérieur net sur toute sa profondeur** : c'est lui qui donne les textures et les contours sans flou.
- Extraction sans redimensionnement (`extraire.py`) ; `<préfixe>_nettete.json` dit si l'image est figée. Une image prise pendant un mouvement de caméra reste utilisable pour le décor **si la référence n'a pas de flou de mouvement** (vérifie-le : largeur d'un bord net sur une image figée et sur une image en mouvement).
- Note pour chaque image : ambiance, type de plan, **D en pixels** (mesuré par une forme `cercle`, ou lu sur la grille).
- Pose les cibles dans la rubrique `"decor"` du fichier de cibles de l'image (format : `fichier-de-cibles.md`, § 8), puis :
```
python $S/mesurer_decor.py analyse/cibles/ref_1400.json analyse/mesures
python $S/synthese_decor.py analyse/mesures --prefixe ref_
```
- **Exclus la bande des sous-titres** des mesures globales (`"bande_exclue": [y_haut, y_bas]`), et exclus **la même bande** sur nos rendus : des sous-titres blancs cernés de noir ajoutent des segments, des bords nets et deux dominantes. Dans l'essai : 180 segments avec la bande exclue, 197 sans.
- Ouvre `<id>_decor_planche.jpg` : chaque cible y est numérotée, avec son résultat. Une cible qui tombe à côté se voit là.

### 1.2 Ce qui est en volume et ce qui est peint (parallaxe)

```
python $S/parallaxe.py reference/ref.mp4 analyse/parallaxe 688:690,1379:1380 --bande 1270,1430
```
Deux images d'un **même plan**, prises **pendant un déplacement de caméra**, écartées de 1 à 10 images (vise 10 à 50 px de déplacement du décor). Le script calcule le flot optique, ajuste **une** homographie sur tout le flot et rend ce qui reste : le **résidu**.

| Ce qu'on lit | Ce que ça veut dire |
|---|---|
| Résidu médian sous 1 px, 90e centile sous 3 px | décor plat (toile peinte), ou caméra qui ne fait que pivoter ou zoomer |
| Résidu de plusieurs pixels, différent d'une zone à l'autre | volumes à des profondeurs différentes, vus par une caméra qui **se déplace** |
| Une zone qui bouge d'un bloc et très peu (le haut de l'image) | plan peint lointain : ciel, nuages, reliefs, soleil |
| Flot médian sous 3 px | non concluant : prends des images plus écartées |

Lis la planche (`<a>_<b>_parallaxe.jpg` : image, norme du flot, résidu), pas seulement le chiffre : un personnage qui bouge laisse lui aussi un résidu. Fais **une paire par ambiance** au moins.

Essai du studio (11 paires) : résidus médians de 1,1 à 12,5 px, 90e centile de 7 à 76 px. Dans une rue, trois vitesses nettes : poteaux (≈ 20 px), façade derrière (≈ 26 px), cailloux du premier plan (≈ 40 px). Dans une pièce, le mur du fond est le plan dominant (résidu ≈ 0) et le plancher s'en écarte jusqu'à 13 px vers le bas. Conclusion : **tout ce qui est proche est en vrais volumes ; seuls le ciel, les nuages, le relief lointain et le soleil sont des plans peints ; les personnages sont des dessins plats posés dans la scène** (ils reçoivent et portent des ombres, passent derrière les poteaux).

Écris ensuite, par ambiance, les **couches de profondeur** : 1. premier plan (flou), 2. plan du sujet (net), 3. fond proche (flou léger à fort), 4. lointain (plans peints).

### 1.3 Densité et vocabulaire

Quatre relevés, qui ne disent pas la même chose :

| Relevé | Outil | Essai du studio |
|---|---|---|
| **Segments** et **petits segments** : zones de couleur homogène de plus de 0,02 % de l'image, et de 0,005 à 0,02 % | `densite` (global) | 144 à 196 segments et 112 à 202 petits par image, selon l'ambiance ; le plan le plus dépouillé en a encore 65 |
| **Bords nets** (gradient au-dessus de 25 niveaux : traits, joints) et **bords doux** (6 à 25 : texture, dégradés) | `densite` (global) | 2,6 à 5,9 % de bords nets ; 9 à 16 % de bords doux (4,6 % en intérieur sombre) |
| **Objets distincts**, comptés à l'œil sur l'image pleine résolution, par familles | toi | 30 à 45 objets par plan ; ≈ 20 pour un plan large, plus le sol |
| **Parts de l'image** (ciel, sol, murs) | `graines` | plan large : ciel 22 à 35 %, sol 30 à 45 % ; l'horizon à 50 à 58 % de la hauteur |

**Piège : « segments » compte des zones de couleur, pas des objets.** Un fil du bois très marqué fait monter le compte ; un fond sombre et flou le fait baisser. Il sert à comparer deux images **avec le même outil, au même cadrage**, jamais comme un but. Le compte d'objets à l'œil et la liste des familles (mobilier, luminaires, objets posés, ouvertures, détails au sol) sont ce qu'on reproduit.

Relève aussi les **tailles en D** des éléments récurrents : largeur d'une lame, côté d'un poteau, hauteur d'une lampe, diamètre d'un caillou. Dans l'essai : lame de plancher et planche de mur 0,32 à 0,33 D ; clin de façade 0,16 D ; poteau 0,30 D ; lampe ≈ 0,6 D ; touffe d'herbe 0,25 à 0,5 D.

### 1.4 Matières : fréquence et contraste

Cible `texture` : un rectangle **dans une seule matière**, sur une zone nette, avec l'axe dans lequel on **traverse** les lignes (`"axe": "x"` pour des planches verticales, `"y"` pour des lames qui filent en travers ; `"angle"` pour redresser des lignes penchées).

| Champ | Ce qu'il dit | Repères de l'essai |
|---|---|---|
| `contraste_ecart_type` | écart type de la luminance après retrait des grandes variations. Sous 3 : aplat ; 3 à 8 : taches douces ; 8 à 21 : matière dessinée | bois 18 à 21 ; plancher 18 ; mur de planches 8,5 à 18 ; sable 3 à 8 |
| `ligne_espacement_px` (et `_D`) | espacement médian des lignes sombres : la **fréquence** des joints | un joint tous les **0,32 à 0,33 D** |
| `ligne_epaisseur_px`, `ligne_profondeur` | épaisseur du joint, et de combien il est plus sombre que la matière | 0,016 à 0,024 D ; 11 à 17 niveaux |
| `couleur_lignes`, `couleur_fond` | couleur du joint et de la matière | le joint est une version sombre et **violacée** de la teinte locale |
| `periode_px`, `force_periode` | période dominante par autocorrélation : à préférer quand un fil fin est compté comme autant de lignes | — |
| `grain_fin` | énergie des détails d'un à deux pixels : le **fil** du bois | 8,5 à 12,7 sur un bois net ; sous 1 sur un sable |
| `degrade_niveaux` | ampleur du dégradé de lumière sur la zone | 18 à 45 niveaux sur un mur ou un sol |

Ce que l'essai a établi, et qui se vérifie sur toute référence : **aucune matière n'est un aplat** (même un sable « uni » varie de 2,5 à 8 niveaux) ; le bois porte **deux dessins superposés** (des joints réguliers et un fil en traînées fines) ; les joints sont **dessinés, pas modelés** ; la texture **s'efface avec le flou, la distance et l'ombre** (un clin flou : 3,6 à 6,5 ; un plancher dans l'ombre : 4,9). Mesure donc chaque matière sur sa zone **nette et éclairée**, et note à part ce qu'elle devient dans le flou.

Les matières trop petites à l'image (métal, verre, tissu) ne se mesurent pas en texture : décris-les en tons (cible `zone` sur chaque ton) et en reflets.

### 1.5 Contours du décor

Cible `trait` : un segment court **en travers** du trait, les deux bouts sur des plages unies (`"clair": true` pour un liseré clair). Sortie : `epaisseur_px` (à mi-profondeur), `couleur`, les deux plages voisines. Si le script répond `"trait": false`, il n'y a pas de trait à cet endroit (profondeur sous 6 niveaux) : c'est une information.

Pose au moins : la **silhouette** d'un gros objet, d'un objet moyen, d'un petit ; une **arête intérieure** ; le même objet **en haut, en bas, côté lumière, côté ombre** ; un objet du fond flou ; un petit détail au sol.

| Question | Essai du studio |
|---|---|
| Silhouette | 0,02 à 0,034 D |
| Arêtes intérieures | tracées elles aussi, deux à trois fois plus fines : ≈ 0,009 D |
| Couleur | la même encre que les personnages pour le mobilier (un prune très sombre, jamais noir) ; une version sombre de la teinte locale pour les petits objets |
| Plein et délié | plus épais **en bas et du côté opposé à la lumière** (un panneau : 0,011 D à gauche, 0,045 D en bas) : la loi des personnages, appliquée au décor |
| De nuit | le trait sombre devient un **liseré clair** sur les arêtes qui prennent la lumière (0,016 à 0,036 D) |
| Au loin | le contour reste, le flou de profondeur le dissout |

### 1.6 Lumière et ombres : couleur, dureté, mélange

**Ombres portées.** Cible `bord` : `a` sur le sol éclairé, `b` dans l'ombre (ou l'inverse), le segment **en travers du bord**, assez long pour que tout le flou tienne dedans. Pose-en une **au contact** de l'objet, une **à mi-longueur**, une **au bout**. Ajoute deux cibles `zone` sur les pleins (sol éclairé, sol à l'ombre).

| Champ | Ce qu'il dit | Essai du studio |
|---|---|---|
| `cote_clair`, `cote_sombre` | les deux couleurs | au couchant : sol `#de9346`, ombre `#373666` |
| `facteur_rvb` | ombre ÷ lumière, canal par canal. **Bleu au-dessus de 1 : ce n'est pas une multiplication, c'est un mélange vers une teinte** | 0,32 à 0,57 / 0,47 à 0,65 / **1,24 à 1,69** |
| `rapport_luminance` | l'opacité de l'ombre | 0,37 à 0,53 |
| `largeur_10_90_px` (et `_D`) | la **dureté** : largeur du bord flou | 0,05 à 0,07 D au contact, 0,14 D à mi-longueur, 0,2 à 0,5 D au bout d'une ombre longue |

**Retrouver le mélange.** Si l'ombre est un mélange `ombre = sol × (1 − force) + teinte × force`, deux couples (sol, ombre) mesurés sur des sols de couleurs différentes donnent la teinte et la force ; avec un seul couple, essaie des forces de 0,6 à 0,9 et garde celle dont la teinte reste la même d'une image à l'autre. Dans l'essai : 87 % d'un bleu-violet au couchant, 72 % d'un bleu plus clair de jour. Vérifie la loi en l'appliquant au sol d'une autre image de la même ambiance (ΔE sous 3). C'est la teinte et la force qu'on reprend, par ambiance.

**Direction et longueur** : note d'où vient la lumière par ambiance (les ombres et le côté épais du trait le disent) et la longueur d'une ombre en hauteurs d'objet (moins d'une demie de jour, 3 à 4 au couchant dans l'essai).

**Ombre propre des volumes.** Deux cibles `zone` sur deux faces d'un même volume : rapport par canal. Dans l'essai : **deux tons par face, pas de dégradé de modelé** ; la face à l'ombre vaut 0,72 × la face éclairée quand elle voit encore le ciel, 0,5 × avec un virage au violet dans une ombre portée.

**Dégradés de lumière.** `degrade_niveaux` d'une cible `texture`, ou deux `zone` aux deux bouts d'une grande surface : 18 à 45 niveaux dans l'essai (un mur plus clair près de la lampe, un sol plus clair au centre). Un décor dont les grandes surfaces sont plates (moins de 10 niveaux) paraît en carton.

**Lumières ponctuelles.** Cible `halo` (centre et rayon de recherche) : `couleur_coeur`, `rayon_mi_hauteur_px`, `couleur_mi_rayon`, `couleur_fond`. Relève aussi, par deux `zone`, de combien la surface voisine s'éclaircit et sur quelle distance en D (≈ 1 D autour d'une lampe de table dans l'essai), et la **flaque** qu'elle pose au sol ou sur un mur.

**Occlusion** : une bande sombre au pied des murs et sous les meubles (0,15 à 0,25 D dans l'essai, lue à l'œil) ; note-la.

### 1.7 Palette par ambiance

`synthese_decor.py` réunit les pixels de toutes les images d'une ambiance (champ `"ambiance"` du fichier de cibles, écrit **à l'identique** d'une image à l'autre) et sort **10 dominantes** avec leur part, la saturation et la luminance moyennes, le contraste, la dominante chaude.

Ce qu'on écrit dans la fiche, par ambiance :
- les 10 dominantes et leur part ; la **part des deux premières** (42 à 48 % dans l'essai : au-delà de 55 %, l'image est dominée par deux aplats) ;
- saturation et luminance moyennes (dans l'essai : intérieur chaud 0,58 et 61 ; couchant 0,45 et 114 ; plein jour 0,43 et 138 ; nuit 0,73 et 52) ;
- **les deux familles de teintes opposées** qui tiennent l'ambiance (sable et bleu de jour, orange et bleu-violet au couchant, rouge-brun et prune en intérieur, bleu et rose-brun de nuit) : une ambiance chaude sans son contrepoint froid paraît monochrome ;
- le rôle de chaque couleur (cibles `zone` sur le ciel, le sol, un mur, un accent).

`palette.py` reste l'outil rapide pour une image ou une boîte (3 à 6 couleurs, look). Si la palette du client remplace celle de la référence, garde les **rapports** : écart de luminance entre sol éclairé et ombre, saturation moyenne, part des deux premières couleurs, présence du contrepoint.

### 1.8 Optique : focale, hauteur de caméra, profondeur de champ, sol net

| Grandeur | Comment | Essai du studio |
|---|---|---|
| **Focale** | `python $S/focale.py analyse/images/ref_1650.png --bande 1270,1430` : points de fuite des verticales et d'une famille de fuyantes. Ne marche que si la caméra est **levée ou baissée** de quelques degrés ; exige 15 segments accordés de chaque côté ; à confirmer sur une deuxième image. À la main : cible `optique` (deux verticales et la ligne d'horizon) | 25 mm pour un capteur de 36 mm **en hauteur** (champ vertical 71°), sur une seule image : ailleurs la caméra est à l'horizontale |
| **Tenue de la caméra** | `convergence_bord_a_bord_deg` : sous 2°, la caméra est à l'horizontale | 0,4 à 1,8° à hauteur d'homme ; 2,9° en contre-plongée |
| **Hauteur de caméra** | où la ligne d'horizon coupe un personnage debout (grille) | entre la hanche et la poitrine : ≈ 1,9 D au-dessus du sol ; ras du sol pour les plans d'objet |
| **Ligne d'horizon** | en % de la hauteur de l'image (champ `horizon_pct_de_la_hauteur` d'une cible `optique`, ou la grille) | 50 à 58 % sur les plans larges |
| **Netteté du sol sous le sujet** | `nettete.net_par_bande` (8 bandes égales de haut en bas : largeur, en px, des transitions les plus nettes de la bande), ou une cible `nettete` sur la boîte où sont les pieds | **2,0 à 2,3 px : aussi net que le personnage** |
| **Flou du fond** | cibles `bord` en travers d'une arête du fond (un toit sur le ciel, un montant de porte) : `largeur_10_90_D` | 0,14 D en plan moyen, 0,15 D en plan large |
| **Flou du premier plan** | `net_par_bande` de la bande du bas, ou une cible `bord` | 6 à 8 px : le tout premier plan est flou aussi |
| **Forme du flou** | profil d'un `bord` : sans plateau = gaussien ; une lampe floue donne un disque à bord doux | gaussien |

**La règle à chercher** relie le flou à la distance. Dans l'essai : `flou (écart type) ≈ 0,055 D × |distance du point ÷ distance du sujet − 1|`, avec une zone nette autour du sujet. Elle donne 0,14 D sur un fond lointain quel que soit le plan, ce qu'on mesure. **Le point à ne pas rater : le sol reste net sous les pieds.** Un sol flou dès le premier mètre donne un effet d'autocollant, que le critique voit avant tout le reste. Note aussi le cas de l'intérieur petit, en plan large : aucun flou (2,0 à 2,9 px du haut en bas), parce que toute la pièce est dans la zone nette.

### 1.9 Finitions au sol

Cible `details` : une boîte sur le sol, autour du sujet, **sans personnage ni ombre portée dedans**. Sortie : `nombre`, `diametre_median_D`, `diametre_max_D`, `densite_par_D2`, `part_couverte_pct`.

| Relevé | Essai du studio |
|---|---|
| Densité autour du sujet | 5 à 11 petits éléments par D² ; jusqu'à 45 au ras du sol |
| Taille | diamètre médian 0,03 D ; les plus gros 0,07 à 0,26 D |
| Nature (à l'œil) | cailloux ovales **plus clairs que le sol**, cernés d'un trait en bas ; touffes de 5 à 8 brins, une tous les 2 à 3 D ; ornières, empreintes, taches ; en intérieur : papiers, nœuds du bois |
| Usure, reflets, particules (à l'œil, avec une `zone` ou un `trait` à l'appui) | bords de marches clairs, taches sur les joints ; un trait clair sur les arêtes éclairées, pas de reflet réaliste ; quelques points clairs flottants dans les ambiances chaudes |

**Mesure fragile** : le compte dépend de la compression (dans l'essai, +11 à +25 % entre une image d'origine et la même lue dans le film encodé) et du cadrage. Compare à ± 25 %, sur des images du même état (les deux encodées, ou les deux d'origine), et ne compte pas des morceaux de joints ou d'ombre pour des objets : regarde la planche.

### 1.10 Lointain et traitement final

| Élément | Mesure | Essai du studio |
|---|---|---|
| **Ciel** | graines `ciel` : `degrades.ciel.tranches` donne 5 couleurs de haut en bas | un dégradé à 5 tons par ambiance ; des nuages en aplats |
| **Soleil, lune** | cible `halo` | disque de 0,86 D de rayon à mi-hauteur, halo fondu sur ≈ 3 D |
| **Brume de distance** | deux `zone` sur la même matière, près et loin | +46 niveaux vers un gris-mauve le long d'une rue ; une bande pâle à l'horizon |
| **Écart ciel / sol** | deux `zone` | de jour, le ciel est **plus sombre** que le sol (56 niveaux) |
| **Bords assombris** | `vignettage.<famille>` : luminance du sol ou du ciel selon la distance au centre | −21 % dans les coins |
| **Grain** | `grain` (global) | 0,06 à 0,34 niveau : aucun grain ajouté (sous 1, c'est le bruit de compression) |
| **Aberration chromatique** | `decalage_rouge_bleu_px` d'un `bord` net | −0,1 à −0,6 px : aucune |
| **Accentuation** | `depassement_clair`, `depassement_sombre` d'un `bord` net ; et la mesure des formes (étape 4) | 0,3 à 2 niveaux sur le décor flou ; ± 16 niveaux sur les traits nets des personnages |

### 1.11 Le diagnostic type : « pourquoi mon décor ne ressemble pas »

Passe **les mêmes scripts** sur ton décor et sur la référence, à cadrage comparable (`controle-chiffre.md`, § 9), puis lis les six causes **dans cet ordre** : c'est celui de leur poids à l'œil dans l'essai du studio. La colonne « décor fait à l'œil » donne les chiffres d'un décor construit sans mesure.

| N° | Cause | La mesure qui la révèle | Référence de l'essai | Décor fait à l'œil | Correctif |
|---|---|---|---|---|---|
| 1 | **Matières en aplats tachés** au lieu de textures dessinées | `texture` : `contraste_ecart_type`, `ligne_espacement_D`, `grain_fin` | contraste 8 à 21, un joint tous les 0,32 D, grain fin 8,5 à 12,7 | contraste 1,6 à 2,6, aucune ligne, grain fin 0,1 à 0,6 | dessiner les matières : joints à la fréquence mesurée, fil dans le sens de la pièce, contraste visé |
| 2 | **Décor vide** | `densite` : petits segments, bords doux ; `details` ; parts de l'image (un grand mur nu) | 112 à 202 petits segments, 30 à 45 objets, 5 à 11 détails par D² | 20 à 47 petits segments, murs nus, rien au sol | meubler **dans le champ de chaque plan** ; semer le sol |
| 3 | **Lumière qui ne modèle rien** | `bord` sur les ombres ; `degrade_niveaux` ; `halo` | ombres portées douces partout, dégradés de 18 à 45 niveaux, flaques autour des lampes | aucune ombre d'un objet sur un autre, dégradés de 1 à 13 niveaux | ombres par mélange vers la teinte mesurée, bord doux en D, flaques de lumière |
| 4 | **Profondeur de champ à l'envers** | `nettete.net_par_bande` aux pieds ; `bord` sur le fond | sol net sous les pieds (2,0 à 2,3 px), fond flou sur 0,14 D | sol flou dès le premier mètre (17 px dans la bande du bas) | flou selon la distance au sujet, **sol net sous les pieds** |
| 5 | **Contour uniforme, de la mauvaise couleur** | `trait` sur une silhouette et sur une arête | silhouette 0,02 à 0,034 D, arête 0,009 D, encre des personnages, plus épais côté ombre | 0,047 D partout, d'une autre couleur | deux épaisseurs, l'encre de l'ambiance, plus épais en bas et côté ombre |
| 6 | **Ni lointain ni traitement final** | graines `ciel` ; `vignettage` ; brume par deux `zone` ; luminance moyenne | ciel en dégradé, soleil, brume (+46 niveaux), coins à −21 % | un aplat derrière une ouverture ; intérieur deux fois trop clair | ciel, soleil et lointain en plans peints ; brume ; bords assombris ; palette de l'ambiance |

Chacune se corrige avec un chiffre. Le contrôle chiffré, lui, ne voit pas tout : dans l'essai, il a validé le flou, les ombres et le plancher ; le critique indépendant a vu ce qu'il ne mesure pas (personnages mal posés dans la pièce, mur vide derrière eux, fonds bouchés). Il faut les deux.

### 1.12 Ce qu'on reprend du décor, ce qu'on ne reprend pas

On reprend : les lois (fréquence des joints en D, contraste, épaisseurs de trait, mélange des ombres, règle de flou, densité), les rapports de palette, la construction (volumes proches, lointain peint). On ne reprend **jamais** un bâtiment, une enseigne, un meuble, un accessoire, un texte ni un lieu de la référence : les décors sont ceux de l'histoire du client, construits avec ces lois.

## 2. Profondeur de champ et netteté : le contrôle rapide

Le détail est au § 1.8. Pour un reel sans décor construit (motion design, face caméra habillée), le relevé rapide suffit :
- compare la netteté de deux zones de la même image : `palette.py … --boite` sur le sujet puis sur le fond ; le champ `look.nettete` (énergie des contours) chute sur une zone floue. Ce nombre ne se compare qu'entre deux zones d'une **même** image. Un rapport de 3 ou plus = profondeur de champ courte (15 dans notre essai : sujet 51,8, fond 3,4) ;
- la largeur de transition du bord extérieur d'une forme (`bord.transition_ext_px`) grandit devant un fond flou ; celle du bord intérieur reste celle du dessin ;
- note où est le plan net (sujet), ce qui est flou (fond, premier plan), et s'il y a du flou de mouvement (comparer une image en plein déplacement de caméra à une image figée).

Unités du « look » de `palette.py` : `luminance_moyenne` de 0 à 255 ; `contraste` = écart type de la luminance, en niveaux ; `saturation_moyenne` de 0 à 1 ; `dominante_chaude` = moyenne de (rouge − bleu), en niveaux, positive pour une image chaude, négative pour une image froide ; `nettete` sans échelle absolue.

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
