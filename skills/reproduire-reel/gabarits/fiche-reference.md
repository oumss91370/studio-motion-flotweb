# Fiche de style de la référence : <nom court>

> Gabarit. Remplace chaque `…`. **Aucune ligne sans chiffre ni image** : la colonne « Preuve » cite le fichier de mesure, la planche ou le numéro d'image. Une case non mesurée porte « non mesuré », jamais une valeur plausible. Cette fiche ne contient que des chiffres, des lois et des descriptions : aucune image de la référence.

- **Référence** : fichier `…`, fourni par `…` le `…`. Reste sur la machine du client, pour l'étude.
- **Format** : `…` × `…` px, `…` i/s, `…` images, `…` s, codec `…`. Source : fichier d'origine / enregistrement d'écran.
- **Analyse du** `…`, par `…`. Temps passé : `…`.
- **Précision** : bords lus au quart de pixel, fiables au demi-pixel (vidéo compressée). `…`

## En cinq lignes : ce qui fait le style
1. `…` (chiffre, image)
2. `…`
3. `…`
4. `…`
5. `…`

## 1. Découpage et rythme

| Grandeur | Valeur | Preuve |
|---|---|---|
| Nombre de plans (ou de stations) | `…` | `analyse/decoupage/plans.md` |
| Vraies coupes / fondus / déplacements de caméra / raccords dans un objet | `…` / `…` / `…` / `…` | `survol-N.jpg` et `bornes-a-verifier-N.jpg`, vérifié à l'image |
| Durée d'un plan : médiane, plus court, plus long | `…` s, `…` s, `…` s | `plans.md` |
| Transitions : types et durées | `…` (en images) | images `…` |
| L'accroche (0 à 3 s), image par image | `…` | bande `…` |
| Structure | `…` | — |

Tableau des plans : `analyse/decoupage/plans.md` (bornes en numéros d'image, cadrage, mouvement, transition de sortie).

## 2. Rendu des éléments dessinés (mesuré au pixel)

Grandeur de référence : **`…` = `…`** (par exemple D = diamètre de la tête). Images mesurées : `…` (ambiance, type de plan, netteté).

| N° | Grandeur | Mesure | En fraction de la référence | Preuve |
|---|---|---|---|---|
| 1 | Contour, côté fin (délié) | `…` px (`loi_simple.delie_px`) | `…` | `ref_…_<forme>_bords.jpg` |
| 2 | Contour, côté épais (plein) | `…` px (`loi_simple.plein_px`, pas le maximum brut) | `…` | `…` |
| 3 | **Loi du contour** | épaisseur = `…` − `…` × cos(angle depuis le côté du délié) | `…` | `synthese_formes.md` (loi commune), `synthese_epaisseur.png`, `…` formes |
| 4 | De quoi dépend le côté du plein | `…` (la lumière ? le bas ? rien ?) : comparer « Plein vers » et « Clair de l'ombrage vers » ; écart médian `…`° | — | colonnes de `synthese_formes.md` |
| 5 | Couleur du trait | `…` | — | `…` |
| 6 | Dureté du bord | transition `…` px ; accentuation ±`…` niveaux ; halo `…` | — | `…` |
| 7 | Régularité de la forme | écart type autour de la loi `…` px ; rapport d'axes `…` | `…` | `…` |
| 8 | Ombrage du remplissage | `…` (aplat, zone d'ombre, dégradé) ; part `…` % ; saut `…` niveaux ; bord doux `…` | `…` | `…_carte.png`, `…_profils.png` |
| 9 | Reflets, filets de lumière | largeur `…` px, à `…` px du trait, couleur `…` | `…` | coupe `…` |
| 10 | Traits d'épaisseur constante (membres, lignes) | `…` px, écart type `…`, effilement `…` | `…` | `…` |
| 11 | Détails fins (visage, coutures) | `…` px | `…` | `details_internes` de `…` |
| 12 | Grain, texture | écart type `…` niveaux : `…` | — | `…` |
| 13 | Ombre au sol | sol `…` → ombre `…` ; facteur par canal `…` ; flou du bord `…` px | `…` | `…` |

**Construction** (comment refaire, déduit des lois) : `…`

### Palette par ambiance

| Ambiance | Trait | Remplissage clair | Remplissage à l'ombre | Reflet | Traits constants | Sol éclairé → à l'ombre | Images |
|---|---|---|---|---|---|---|---|
| `…` | `#……` | `#……` | `#……` | `#……` | `#……` | `#……` → `#……` | `…` |
| `…` | | | | | | | |

Ce qui change avec l'ambiance, ce qui ne change pas : `…`

## 3. Jeu et mouvement (lecture continue)

Catalogue des durées, en nombre d'images. Preuve : `analyse/lecture-continue/…`, avec les numéros d'image.

| Action | Durée mesurée | Images d'exemple |
|---|---|---|
| Changement d'expression | `…` | `…` |
| Clignement | `…` ; un toutes les `…` images | `…` |
| Anticipation avant un geste | `…` | `…` |
| Geste rapide / geste large | `…` / `…` | `…` |
| Dépassement et retour | `…` | `…` |
| Tenue après une action | `…` | `…` |
| Marche (images par pas, longueur du pas) | `…` | `…` |
| Chute, impact | `…` | `…` |
| Action par rapport au mot | `…` images après / avant | `…` |
| Animation à l'image ou par paliers | `…` | `…` |

**Catalogue des poses** : `…`
**Catalogue des expressions** (yeux, bouches, signes) : `…`
**Ce qui rend le jeu efficace** (une phrase par idée, avec ses images) : `…`

## 4. Décors

| Ambiance | Couleurs dominantes (part) | Luminance / contraste / saturation | Ombres | Contours | Preuve |
|---|---|---|---|---|---|
| `…` | `#……` (`…` %), `#……`, `#……` | `…` / `…` / `…` | `…` | `…` | `analyse/palettes/….json` |

- Type de rendu : `…`
- Profondeur de champ : netteté du sujet `…`, du fond `…` (rapport `…`) ; ce qui est flou : `…`
- Grain, texture : `…`

## 5. Caméra et cadrage

| Grandeur | Valeur | Preuve |
|---|---|---|
| Cadrage dominant | `…` (sujet à `…` % de la hauteur) | images `…` |
| Types de cadrage vus | `…` | `planche-plans.jpg` |
| Durée d'une tenue / d'un déplacement | `…` / `…` images | `…` |
| Départ et freinage d'un déplacement | `…` / `…` images | `…` |
| Dérive pendant les tenues | `…` px par seconde | `…` |
| Coups de zoom, secousses | `…` | `…` |

## 6. Sous-titres

| Grandeur | Valeur | Preuve |
|---|---|---|
| Famille de police, casse | `…` | image `…` |
| Hauteur des lettres | `…` px (`…` % de la hauteur du cadre) | `…` |
| Position | centre à x `…`, y `…` (`…` % de la hauteur) | `…` |
| Couleur du texte / du contour | `#……` / `#……` | `…` |
| Contour | `…` px ; ombre décalée de `…` px vers `…`° | `…` |
| Mots par carton | `…` (de `…` à `…`) | bandes `…` |
| Durée d'un carton | `…` images (de `…` à `…`) | `…` |
| Animation | `…` | `…` |

## 7. Son

| Grandeur | Valeur | Preuve |
|---|---|---|
| Niveau | `…` LUFS, crête `…` dBTP, LRA `…` | `ffmpeg ebur128` |
| Voix | `…` mots en `…` s = `…` mots par seconde ; pauses `…` | `…` |
| Musique | `…` ; `…` dB sous la voix | `…` |
| Bruitages | `…` par 10 s ; calés à `…` ms du geste | `…` |
| Action et mot | `…` | `…` |

## 8. Ce qu'on reprend / ce qu'on ne reprend pas

| On reprend (la technique) | Chiffre ou loi | On ne reprend pas (l'œuvre) | Ce qu'on met à la place |
|---|---|---|---|
| `…` | `…` | les personnages : `…` | les personnages du client : `…` |
| `…` | `…` | les costumes, les accessoires : `…` | `…` |
| `…` | `…` | le texte, la voix | le script et la voix du client |
| `…` | `…` | la musique, les bruitages | `…` |
| `…` | `…` | le logo, le nom | ceux du client |
| `…` | `…` | le sujet, l'histoire | `…` |
| `…` | `…` | les irrégularités d'un dessin précis | la loi, appliquée à nos formes |

Confirmé par le client le `…`.

## 9. Limites de cette fiche
- Non mesuré : `…`
- Mesuré sur une seule image (à confirmer) : `…`
- Mesures fragiles (élément caché, image en mouvement, peu d'orientations valides) : `…`
- Corrections apportées par la mesure à une première lecture à l'œil : `…`
