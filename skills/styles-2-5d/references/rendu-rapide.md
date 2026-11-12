# Rendre plus vite : une plaque de décor par tronçon de caméra

Méthode de la chaîne mesurée du kit (`kit/plaque.py`, branché dans `kit/bl_decor.py`, `kit/compo.py` et `kit/lancer.py`). Les seuils sont dans `kit/regles.py` (`PLAQUE`). Tous les chiffres viennent d'un essai chronométré du studio, le 12/11/2026, sur un PC à carte graphique intégrée. Ce qui n'a pas été mesuré est dit « non mesuré ».

## 1. Le principe

- Les personnages sont dessinés en 2D et posés à l'assemblage. Le décor, lui, sort de Blender.
- Quand la caméra ne fait que dériver, le décor change à peine. Le recalculer à chaque image ne sert à rien.
- On rend donc **une seule image de décor par tronçon de caméra** : une « plaque ». À l'assemblage, on la recadre pour chaque image du film.
- Seuls les vrais déplacements de caméra restent rendus image par image.

## 2. Par tronçon, pas par plan

Le kit coupe chaque plan **aux stations de la caméra**. Il classe chaque tronçon d'après sa **parallaxe**, puis réunit les tronçons voisins tant que la parallaxe de l'ensemble reste sous le seuil.

- **Parallaxe**, en pixels : de combien un objet proche glisse par rapport au lointain, entre la pose de la plaque et la pose la plus éloignée de la caméra. L'objet proche est pris à 0,6 fois la distance du sujet.
- **Pourquoi par tronçon.** Un plan pris en entier a une parallaxe énorme : 790 à 2 060 px sur les 4 plans d'essai. Il enchaîne de vrais déplacements (une dizaine d'images, 370 à 1 350 px) et des tenues en dérive (14 à 112 px). Classé en entier, tout plan partirait en 3D.

| Mode | Quand | Ce qui est rendu |
|---|---|---|
| `fixe` | caméra immobile | une plaque |
| `plaque` | parallaxe de 12 px au plus | une plaque, recadrée par homographie |
| `couches` | parallaxe de 12 à 120 px | la même plaque, chaque pixel déplacé selon SA profondeur, lue dans la passe de données. C'est l'équivalent continu de 2 à 4 couches. Ce qui était caché derrière un objet proche est étiré |
| `3d` | au-delà de 120 px, ou décor animé (`anime=True`) | image par image |

La plaque est rendue à la pose **la plus centrale** du tronçon, avec une focale plus courte (marge de 4 %) et une taille plus grande (jusqu'à 2 fois le cadre). Elle couvre ainsi le mouvement et le zoom.

## 3. Ce qui est fait une fois, ce qui est refait à chaque image

| Une fois, sur la plaque | À chaque image du film |
|---|---|
| les trois passes du décor | le recadrage de la plaque |
| la lumière de l'ambiance | la profondeur de champ |
| les contours du décor | les bords assombris |
| le ciel | les personnages et leur ombre |
| les halos des lampes | les sous-titres |

## 4. Voir et forcer

```
python outils/lancer.py plans      les tronçons de chaque plan, leur mode, la raison, la taille de la plaque
```

La dernière ligne donne le nombre de rendus Blender pour le nombre d'images du film.

| Pour… | On écrit |
|---|---|
| forcer le mode d'un plan | la clé `mode` du plan : `mode="3d"`, `"couches"`, `"plaque"` ou `"fixe"` |
| dire qu'un objet du décor bouge dans le plan | la clé `anime=True` du plan : il est rendu en 3D |
| tout rendre image par image | la variable d'environnement `EPISODE_MODE=3d` |

## 5. Les temps mesurés

Essai du 12/11/2026 : 4 plans de test d'un décor lourd (3 656 objets réunis en 535), 256 images.

| Mesure | Valeur |
|---|---|
| Rendu image par image, pleine taille (rechronométré ce jour sur 24 images) | 5,29 s par image (couleur 1,69 ; lumière 2,74 ; données 0,86) ; 22,6 min pour les 256 images. La veille, le même rendu avait pris 9,2 s par image (machine plus chargée) |
| Rendu image par image, demi-taille | 3,38 s par image (−36 %) |
| Une plaque (un peu plus grande que le cadre : 1 124 à 1 406 px de large) | 6,1 s en moyenne |
| Mode par tronçons, seuils 12 et 120 px | 107 images en 3D + 5 plaques pour 256 images : 9,9 min, soit 2,33 s par image (2,3 fois plus vite). Un des 4 plans (54 images) reste en 3D parce qu'un objet du décor y bouge ; sans lui : 53 images en 3D sur 202 |
| Reprojection d'une image | 0,94 s (mesurée machine chargée) |

Sur le film d'exemple du kit (3 plans, 229 images avec les images de contrôle) : 70 rendus Blender au lieu de 229, à 4,6 à 5,0 s par rendu.

## 6. Ce que ça coûte à l'image

L'écart est la moyenne de l'écart absolu par pixel avec le rendu image par image, en niveaux sur 255.

| Mode | Écart mesuré |
|---|---|
| `couches` | 0,13 à 0,52 pour 17 à 112 px de parallaxe ; 99e centile 1,4 à 6,5. C'est le niveau de bruit entre deux rendus identiques (0,08 à 0,32 à parallaxe nulle) |
| `plaque` (homographie seule) | 0,46 à 0,74 à 14–18 px ; 0,74 à 1,06 à 18–23 px ; 1,4 à 2,9 à 40–50 px (99e centile jusqu'à 52) ; 7,6 à 112 px : tout le cadre se décale |

D'où les deux seuils : l'homographie seule jusqu'à 12 px, la profondeur jusqu'à 120 px.

## 7. Où ça trahit

| Cas | Ce qu'on voit | Mesure | Quoi faire |
|---|---|---|---|
| Parallaxe trop forte en mode `couches` | les touffes du premier plan sont étirées ou dédoublées | à 307 px : 0,94 en moyenne, 1,63 au pire, 99e centile 25,7 | 3D |
| Décor animé | l'objet reste figé | écart de 1,3 à 4,5, 99e centile jusqu'à 131 | 3D obligatoire : `anime=True` |
| Ombres et lampes qui bougeraient pendant le tronçon | elles ne bougent pas | non mesuré | 3D sur ce plan |
| Tronçons réunis juste sous le seuil | étirements possibles près des objets proches | 119 px sur un plan d'essai ; validé image par image jusqu'à 112 px seulement | regarder ces images ; au moindre doute, `mode="3d"` |

## 8. Les autres gains

| Levier | Mesure |
|---|---|
| Plans de test en demi-taille | 3,38 s par image au lieu de 5,29 (−36 %). Pour régler le cadrage, la caméra et le jeu. Les images montrées au client et le contrôle chiffré restent à la taille finale |
| Assemblage en parallèle | 210 images en 15 min avec 2 processus, en 12 min avec 3 (même PC, mesuré plus tôt). Sur le film d'exemple : environ 4 s par image de film avec 5 ou 6 processus (109 images en 396 à 433 s) |
| Réglage d'ambiance sans Blender | lumière, contours, flou, personnages et sous-titres se refont à l'assemblage seul |
| Un seul Blender | pas un gain, une règle : deux rendus à la fois plantent le pilote d'une carte intégrée (skill `blender`, `references/rendu-long-et-fiable.md`) |

## 9. Estimation pour un film d'une minute

C'est une **estimation**, pas une mesure. Film de 61,5 s, soit 1 845 images.

| | Calcul | Durée |
|---|---|---|
| Avant (la veille) | 15 s par image, tout compris | 7 h 40 |
| Blender, par tronçons | un tiers des images en 3D (31 % sur l'exemple du kit, 26 à 42 % sur les plans d'essai) : environ 650 images en 3D (57 min) et une centaine de plaques (10 min) | environ 1 h 10 |
| Assemblage | 4 s par image | environ 2 h |
| **Total** | | **environ 3 h 10** |

C'est maintenant l'assemblage qui pèse le plus.

## 10. Ce qui n'est pas mesuré

- Les passes regroupées en un seul rendu : non mesuré.
- Une carte graphique dédiée : non mesuré.
- L'écart sur les ombres et les lampes qui bougent pendant un tronçon : non mesuré (le défaut est connu, pas chiffré).
- Un tronçon réuni entre 112 et 120 px de parallaxe : non validé image par image.
- Un film entier d'une minute rendu par tronçons : estimé (§ 9), non mesuré.
