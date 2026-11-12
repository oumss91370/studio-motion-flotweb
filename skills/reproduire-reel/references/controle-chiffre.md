# Le contrôle chiffré : référence / nous / écart

Une fiche de style bien mesurée ne prouve pas que notre rendu la respecte. Le contrôle chiffré repasse **exactement les mêmes scripts** sur notre image et compare, ligne par ligne.

## 1. Le rendu de contrôle

- **Un élément, à la même taille que dans la référence.** Choisis l'image de référence la plus propre (élément grand, net, dégagé) : c'est l'image de contrôle. Rends un de **nos** éléments (un de nos personnages, notre titre) à la même taille en pixels : même diamètre de tête, même hauteur de lettres. Le lissage du bord et le filtre de netteté ne se remettent pas à l'échelle : une comparaison à des tailles différentes est fausse.
- **Même ambiance** de lumière, même direction de lumière, fond comparable (un bord extérieur se mesure contre le décor). **Pas de fond transparent** : le script poserait l'image sur un gris et le bord extérieur ne voudrait plus rien dire.
- **Même chaîne de finition** que le film : mêmes filtres, même accentuation, en PNG. Puis, une fois, la même mesure sur une image du film encodé, pour voir ce que la compression change.
- Si un accessoire de notre personnage cache une partie du contour, fais un second rendu sans lui, **pour le contrôle seulement** (une « tête nue ») : il vérifie la loi sur tout le tour.
- C'est notre élément, avec notre costume et notre visage. On ne refait pas celui de la référence pour mieux coller.

## 2. Mesurer notre image

Écris un fichier de cibles pour notre image, avec les **mêmes rubriques** que celui de l'image de contrôle (mêmes formes, coupes aux mêmes endroits du corps, même ombre), puis :
```
python $S/mesurer.py controle/cibles/nous.json controle
```

## 3. Le fichier de paires

`comparer.py` compare ce qui porte le même nom des deux côtés. Dès que les noms diffèrent, écris `controle/paires.json` (gabarit `gabarits/paires.json`) :

```json
{
  "formes":  [{"ref": "tete-a", "nous": "tete", "exclure_angles": [[255, 290]]}],
  "coupes":  [{"ref": "contour du torse, côté ombre", "nous": "torse ombre", "bande": "sombre"},
              {"ref": "contour du torse, côté lumière", "nous": "torse lumière", "bande": "claire", "nom": "filet de lumière du torse"}],
  "membres": [{"ref": "jambe gauche", "nous": "jambe"}],
  "zones":   [{"ref": "torse", "nous": "torse"}],
  "ombres":  [{"ref": "ombre au sol", "nous": "ombre", "melange": {"teinte": "#202d6c", "force": 0.87}}],
  "tolerances": {"epaisseur_px": 1, "delta_e": 6, "luminance": 8}
}
```

| Champ | Rôle |
|---|---|
| `exclure_angles` | orientations à ignorer dans la comparaison à la loi (le secteur du cou, où le contour touche le torse des deux côtés) |
| `bande` | dans une coupe : `"sombre"` compare le plateau le plus sombre (le trait), `"claire"` le plateau clair et fin (un filet de lumière) |
| `melange` | pour une ombre teintée : notre réglage (couleur et force du mélange) est appliqué au sol **de la référence** et comparé à l'ombre mesurée. C'est la bonne comparaison quand nos sols n'ont pas la même couleur |
| `tolerances` | remplace les valeurs par défaut |
| `echelle` | force le rapport d'échelle (sinon : rapport des grandeurs de référence) |

```
python $S/comparer.py analyse/mesures/ref_0990.json controle/nous.json controle --paires controle/paires.json --tour 1
```
Sorties : `controle_ecarts.md` (le tableau), `controle_ecarts.json`, `controle_courbes.png` (courbes du contour superposées, avec la loi de la référence), `controle_profils.png` (profils de luminance superposés), et `tours/tour1_ecarts.md`, `tours/suivi.json`.

## 4. Les tolérances

| Grandeur | Tolérance par défaut | Clé |
|---|---|---|
| Épaisseurs (contour, traits, filets) | ±1 px | `epaisseur_px` |
| Couleurs | ΔE2000 < 6 | `delta_e` |
| Luminance (profils, accentuation, halo, saut d'ombre) | ±8 niveaux | `luminance` |
| Direction du plein | ±10° | `angle_deg` |
| Largeur de transition du bord intérieur | ±0,5 px | `bord_px` |
| Part de la zone d'ombre | ±6 % | `part_pct` |
| Position de la frontière d'ombre | ±0,1 R | `frontiere_R` |
| Direction de la frontière | ±15° | `direction_frontiere_deg` |
| Largeur du bord doux de l'ombre | ±0,04 (en 2R) | `bord_doux` |
| Flou du bord de l'ombre au sol | ±8 px | `flou_ombre_px` |

Les trois premières sont celles du studio. Les autres ont été fixées lors de l'essai : dis-le dans le compte rendu si tu les changes.

## 5. Les tours de correction

1. Lis les lignes « hors tolérance », de la plus grosse à la plus petite.
2. Corrige **dans le kit** (une épaisseur, une couleur, un décalage), pas dans l'image.
3. Re-rends, re-mesure, recompare avec `--tour 2`, puis 3, puis 4.
4. **Quatre tours au plus.** Ce qui reste hors tolérance après le quatrième s'écrit dans le compte rendu, avec sa raison.

Dans l'essai du studio : 26 lignes dans la tolérance et 19 hors au tour 0, puis 35 et 16, 36 et 15, 38 et 13.

## 6. Lire les lignes rouges

Toutes les lignes hors tolérance ne sont pas des défauts à corriger.

| Ligne rouge | Ce qu'elle dit souvent | Que faire |
|---|---|---|
| Courbe du contour contre la **courbe brute** de la référence | la référence est tracée à la main : sa courbe a des bosses propres à ce dessin, et des pics là où le trait touche un autre trait | **ne pas corriger** : regarder la ligne « contre la LOI de la référence ». Reproduire les bosses serait recopier le dessin |
| Maximum d'un profil de luminance | un filet de lumière décalé d'un pixel suffit à faire 20 niveaux d'écart en un point | regarder la moyenne et le 90e centile du même profil |
| Part et position de la zone d'ombre | le découpage automatique en deux zones ne coupe pas au même endroit dans un dégradé doux | regarder le saut de luminance et la largeur du bord doux, mesurés sur les profils |
| Bord extérieur du trait | dépend du flou du décor derrière | comparer sur un fond de même netteté |
| Épaisseur maximale brute | endroit où le trait touche un col, un chapeau, une main | regarder le plein mesuré loin de tout autre trait |

Écris pour chaque ligne rouge restante : la valeur, la raison, et si c'est un choix (« assumé ») ou un reste à faire.

## 7. La planche côte à côte

```
python $S/cote_a_cote.py --ref analyse/images/ref_0990.png --nous controle/nous.png -o revue/element-ref-vs-nous.jpg \
       --zoom-ref 351,840,110 --zoom-nous 400,700,110 --k 4
```
Recadrages à la même échelle, agrandis ×4 au plus proche voisin : on voit les pixels d'origine. Ajoute des détails ×8 (côté lumière, côté ombre) avec un fichier de planche (`gabarits/planche.json`). Cette planche accompagne le tableau dans le compte rendu.

## 8. Le contrôle dans le film

Le rendu de contrôle est propre. Le film passe par une mise en perspective, un assemblage, un encodage. Une fois les plans de test rendus, repasse la mesure sur **une image du film** (`"image": "out/test.mp4@1285"`) : le contour, les couleurs et l'ombrage doivent rester dans les mêmes tolérances, à un demi-pixel près. Note l'écart.

## 9. Le contrôle chiffré du décor

Même principe, avec `mesurer_decor.py` des deux côtés et `comparer_decor.py`. Deux différences avec le contrôle d'un élément dessiné.

**On compare des images à cadrage comparable, pas un élément isolé.** Pour chaque ambiance de la référence, choisis une de ses images mesurées et rends un de nos plans **du même type** (plan large contre plan large, plan moyen contre plan moyen), dans la même ambiance, avec le sujet à une taille voisine. Deux à quatre couples suffisent : un intérieur net pour les textures et les contours, un plan moyen pour les ombres et le flou, un plan large pour la densité et le lointain. Ajoute une ou deux images fixes rendues pour le contrôle si le film ne montre pas l'élément dégagé.

**On compare en D.** Les deux images n'ont pas la même échelle : une longueur de la référence est ramenée à la nôtre (× D nous ÷ D référence), et la remarque de chaque ligne donne le détail. Donne donc D dans les deux fichiers de cibles.

Marche à suivre :
1. Un fichier de cibles par image de chez nous, avec **les mêmes mesures aux mêmes endroits du décor** (la silhouette d'un gros objet, une arête, le bord d'une ombre à mi-longueur, le sol éclairé et le sol à l'ombre, la texture du sol, une arête du fond, les détails au sol) et **la même `bande_exclue`** que la référence, même si nos sous-titres ne sont pas encore posés.
2. `python $S/mesurer_decor.py controle/cibles/nous_0120.json controle/mesures`
3. Le fichier de paires, d'après `gabarits/paires-decor.json` : une ligne par grandeur, avec sa famille et le nom de sa tolérance.
4. `python $S/comparer_decor.py controle/paires-decor.json controle --ref analyse/mesures --nous controle/mesures --tour 1`
5. Lis `controle/controle_decor.md` : le tableau, puis le bilan par famille. Corrige, re-rends, re-mesure : **4 tours au plus**. Le suivi s'écrit dans `controle/tours/`.

### Tolérances du décor

| Famille | Grandeur | Tolérance | Nom dans le fichier de paires |
|---|---|---|---|
| Palette | chaque dominante de la référence : couleur la plus proche chez nous, et part de nos couleurs qui lui reviennent | ΔE < 8 **et** part à ± 8 points | `palette_delta_e`, `palette_part_pt` |
| Palette | saturation moyenne ; luminance moyenne | ± 0,08 ; ± 15 niveaux | `saturation`, `luminance` |
| Ombres | couleur du sol éclairé, du sol à l'ombre | ΔE < 6 | `ombre_delta_e` |
| Ombres | dureté du bord (largeur 10–90 %) | ± 30 % | `durete` |
| Texture | fréquence (espacement des joints, période), en D | ± 20 % | `frequence` |
| Texture | contraste, profondeur des joints, grain fin | ± 6 niveaux | `contraste` |
| Contours | épaisseur d'un trait (silhouette, arête), à notre échelle | ± 1 px | `contour` |
| Contours | couleur du trait | ΔE < 6 | `couleur_delta_e` |
| Flou | flou de profondeur (largeur d'un bord du fond) | ± 25 % | `flou` |
| Flou | netteté du sol sous le sujet | ± 1 px | `nettete_sol` |
| Densité | segments, petits segments, détails par D², diamètre des détails | ± 25 % | `densite` |

Celles de la palette, des ombres, de la texture, des contours, du flou et de la densité sont celles du studio. Celles de la saturation, de la luminance et de la netteté du sol ont été fixées lors de l'essai : dis-le si tu les changes.

### Pièges, tirés de l'essai

| Piège | Ce qui se passe | Que faire |
|---|---|---|
| **Le fil du bois compté comme des joints** | notre plancher a un fil marqué : `ligne_espacement_px` rend 22 px au lieu de 92, parce que chaque veine est comptée comme une ligne | comparer la **période d'autocorrélation** (`periode_px`) chez nous à l'espacement des lignes de la référence, sur un plan où les lames filent comme dans la référence ; l'écrire dans la `note` de la ligne |
| **« Segments » compte des zones, pas des objets** | une pièce trop bavarde au sol dépasse de +54 à +133 % ; un plan moyen avec un seul personnage devant un fond flou manque de −45 à −67 % ; aucun des deux chiffres ne dit « ajoute des objets » | lire l'indicateur avec le compte d'objets à l'œil et la planche : il dit **où** l'image est trop chargée ou trop vide, pas quoi poser |
| **Cadrages non comparables** | un gros plan devant un fond noir et flou contre une grande salle éclairée : 9 dominantes sur 10 hors tolérance, alors que la saturation et la luminance moyennes concordent | comparer une ambiance à une ambiance **au même type de plan** ; sinon, l'écrire et juger sur les ombres, les textures et les contours |
| **Bande exclue différente** | les sous-titres ajoutent des segments, des bords nets et deux dominantes | même `bande_exclue` des deux côtés ; le script le signale dans la remarque quand elles diffèrent |
| **Image d'origine contre image du film encodé** | petits segments +9 à +28 %, détails par D² +11 à +25 % ; les couleurs, les flous, les contours et les textures bougent peu (1 à 2 niveaux, 3 %, 0,05 px) | comparer des images du même état ; pour la densité, mesurer notre image **dans le film encodé**, comme celle de la référence |
| **Deux traits confondus** | un socle dont la silhouette touche une arête : 9,1 px au lieu de 4,6 | poser la coupe là où le trait est seul ; sinon écrire « non mesurable ici » |
| **Une valeur au bord de la tolérance** | −0,072 arrondi à −0,08 change un verdict | ne pas arrondir avant de comparer ; ne pas régler le kit pour passer une ligne de justesse |
| **Corriger en post-traitement ce qui vient du rendu** | les ombres longues restent deux fois trop dures (−48 %) après quatre tours de réglage de l'assemblage | quand une ligne ne bouge plus, la cause est en amont (la source de lumière, la matière) : le dire et la reporter |

### Ce que le tableau ne voit pas : la liste de contrôle par plan

Le tableau a validé, dans l'essai, le flou, les ombres et le plancher ; le critique a vu le reste. Avant de lui montrer un plan, vérifie à l'œil :

- [ ] **Rien de nu derrière les personnages** : pas de grand mur vide, des objets dans le champ de **ce** plan (un décor très meublé hors champ ne compte pas).
- [ ] **Une source de lumière visible** ou lisible (une lampe, une fenêtre, le soleil), et sa flaque sur le sol ou le mur.
- [ ] **Un contrepoint froid dans une ambiance chaude** (et l'inverse) : une fenêtre sur la nuit, une ombre bleutée.
- [ ] **Aucun objet coupé par le cadre** de façon gênante, aucune masse inexpliquée au bord.
- [ ] **Des formes contrastées dans le fond**, pour que le flou reste lisible : un fond flou et sombre sans silhouettes devient un aplat bouché.
- [ ] **Le sol net sous les pieds**, et le personnage **posé** : son ombre part de ses pieds, dans la direction et la couleur des ombres du décor.
- [ ] **Les personnages accordés à l'ambiance** (palette de l'ambiance, sans salir les blancs), et flous comme le décor s'ils sont hors du plan de netteté.
- [ ] **Le trait du décor et celui des personnages de la même main** : même encre, épaisseurs voisines.

Une correction peut introduire un défaut (dans l'essai : une mise au point passée sur le mauvais personnage, des blancs salis par une teinte d'ambiance) : **après un tour de corrections, repasse le contrôle et redemande une note.**
