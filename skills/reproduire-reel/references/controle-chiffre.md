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
