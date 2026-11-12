# Trait à pleins et déliés, ombrage et lumière : les valeurs mesurées

Ce rendu vient d'une mesure au pixel faite par le studio sur un film de référence à personnages « tête ronde » (11 images, 14 têtes, 4 ambiances), puis d'un contrôle chiffré sur nos propres personnages. Il remplace le contour d'épaisseur fixe quand le style demande un personnage **éclairé** : trait qui s'épaissit côté ombre, croissant d'ombre, filet de lumière. La méthode de mesure et le contrôle sont dans le skill `reproduire-reel`.

Toutes les longueurs sont en fraction de **D, le diamètre de la tête** (bord extérieur du trait compris).

**État des vérifications.**

| Point | État |
|---|---|
| Plein jour, coucher de soleil | rendus et contrôlés sur nos personnages (contour, couleurs, croissant, membres, torse, ombre au sol : dans la tolérance de 1 px, ΔE 6, 8 niveaux) |
| Intérieur chaud | essayé sur des plans de test : le trait et la palette tiennent, mais **la pose dans le décor n'est pas au niveau** (§ 7 : ombre timide, pas de liseré de lumière côté lampe, blancs salis par l'accord de teinte) |
| Nuit | **non vérifiée** : valeurs mesurées sur la référence, jamais utilisées dans nos plans |
| Coiffes à trois tons, jambe du second plan éclaircie | fait dans le kit (`kit/pantin.py` de `styles-2-5d`) ; vérifié par l'essai du kit : coiffes à trois tons : oui, sur les deux personnages du film d'essai (un bonnet, une casquette), jugées conformes par le critique, non mesurées par script ; jambe du second plan : dessinée et vue sur les planches de personnages (trois quarts), **absente du film d'essai** (personnages de face) |
| Vues | face et trois quarts ; ni profil strict ni dos |

Ces règles sont appliquées par le générateur de personnages de la chaîne mesurée (`kit/pantin.py`, valeurs dans `kit/regles.py`, catégorie `styles-2-5d`) et reprises, avec leur raison, dans le prompt maître de cette catégorie (`skills/styles-2-5d/references/prompt-maitre.md`).

## 1. Le contour : une loi, pas une épaisseur

L'ancienne règle (« un seul poids de contour ») donne un personnage plat. La règle mesurée :

```
épaisseur = 0,044 D − 0,028 D × cos(angle compté depuis la direction de la lumière)
```

- **Délié** (côté lumière) : 0,014 à 0,022 D, médiane 0,018 D.
- **Plein** (côté ombre) : 0,066 à 0,073 D.
- **Construction** : un disque d'encre de rayon 0,5 D, et par-dessus un disque de peau de rayon 0,456 D, **décalé de 0,028 D vers la lumière**. Pas de trait à dessiner : le trait est ce qui dépasse.
- **Même règle pour le torse et les coiffes** : 0,019 D côté lumière, 0,058 à 0,071 D côté ombre. Le contour d'une coiffe ou d'un accessoire est plus régulier (0,029 à 0,035 D), et la coiffe se peint en **trois tons francs** (clair, moyen, bandeau), sans dégradé.
- Bord du trait : net, lissé sur un pixel environ ; ni halo, ni grain.

## 2. La direction de la lumière : un paramètre obligatoire par plan

Chaque plan déclare **d'où vient la lumière à l'écran** (un angle : 0° = de la droite, 90° = d'en haut). Elle commande d'un coup :

| Élément | Où il se place |
|---|---|
| le plein du contour | à l'opposé de la lumière |
| le croissant d'ombre de la tête | à l'opposé de la lumière |
| le filet de lumière | du côté de la lumière |
| l'ombre au sol | à l'opposé, attachée aux pieds |

Sans ce paramètre, le rendu retombe sur un trait constant. Mesuré : lumière en haut à droite en plein jour (plein en bas à gauche), de la droite au couchant, du côté de la lampe de nuit, du côté de la fenêtre en intérieur.

## 3. L'ombrage de la tête

Trois couches, dans cet ordre :

1. **La peau en aplat** (avec un très léger dégradé le long de l'axe de la lumière : 7 niveaux de luminance d'un bord à l'autre).
2. **Un croissant d'ombre à bord doux**, du côté opposé à la lumière : le disque de peau moins le même disque décalé de 0,24 rayon vers la lumière ; flou du bord 0,02 D (transition lue sur 0,05 à 0,13 D) ; 15 à 27 % du disque ; 18 à 34 niveaux plus sombre que la peau, teinte tirée vers le rose, à peine moins lumineuse.
3. **Un filet de lumière effilé**, du côté de la lumière : 0,021 D de large au plus fort (0,013 à 0,022 D), posé à 0,033 D du trait, aminci aux deux bouts, sur un cercle plus petit que la tête.

La **bande horizontale** (moitié haute de la tête plus froide) n'apparaît que **sous une coiffe à bord** : c'est l'ombre du bord, à limite très douce (0,20 D). Sur une tête nue, elle n'existe pas.

Torse : aplat au centre, **bande d'ombre le long du bord éclairé** (16 à 21 % de la surface, luminosité −11 à −17), derrière un filet de lumière de 0,022 D posé à 0,034 D du trait, et un petit reflet en virgule effilée (0,25 D).

## 4. Les palettes par ambiance

On change la palette **de la peau et du trait** avec l'ambiance. **On ne change pas la couleur du costume**, et on n'applique aucune teinte générale multipliée sur le personnage. De nuit, la peau reste crème : le personnage n'est pas bleui par le décor.

| Ambiance | Encre du contour | Membres | Peau | Croissant d'ombre | Filet de lumière | Vérifié sur nos plans |
|---|---|---|---|---|---|---|
| Plein jour | `#2d2336` | `#3a3357` | `#fcf7f2` | `#ede4ef` | aucun filet coloré (traits blancs très fins) | oui |
| Coucher de soleil | `#301c2c` | `#2c1a29` | `#ffe4bb` | `#f7c9a1` | `#ffc368` (tête), `#ff9d4c` (torse) | oui |
| Intérieur chaud | `#2b1623` | non mesuré (le kit prend l'encre, `#2b1623`) | `#fddab3` | `#f2beac` | clair, peu marqué | essayé, pose à reprendre |
| Nuit | `#241731` | `#1a1436` | `#ffe2bc` | `#f2cfbc` | `#fec47c` | **non** |

Le trait est un prune très sombre, jamais noir. Ces valeurs sont un point de départ : la fiche « ma chaîne » peut les remplacer, en gardant les écarts (croissant à peine plus sombre et plus rose que la peau, encre plus bleue de jour, plus rouge en intérieur, plus violette de nuit).

## 5. Les épaisseurs

| Élément | Valeur |
|---|---|
| Membres (bras, jambes) | trait de 0,056 D, **constant** : aucun effilement, aucune ombre propre |
| Jambe du second plan | même épaisseur, **éclaircie vers la teinte du décor** (mesuré : `#937f89` pour la jambe du fond contre `#3b3a63` pour celle de devant) : elle sépare les deux jambes sans les cerner |
| Traits fins du visage (yeux, bouche, fines moustaches) | 0,0235 D, de la couleur du contour |
| Sourcils, grosses moustaches | formes pleines ; sourcil de 0,05 D d'épaisseur, 0,13 à 0,18 D de long |
| Anneau de l'œil cerclé | diamètre 0,22 D hors tout, trait 0,024 D, **intérieur de la couleur de la peau** (pas de blanc), pupille de 0,06 D |
| Franges, coutures claires | 0,015 à 0,018 D de large, tous les 0,040 D |

## 6. Une tête légèrement irrégulière

La tête n'est pas un cercle parfait : rapport petit axe / grand axe de **0,91 à 0,98**, forme légèrement patatoïde. Elle est **fixe par personnage** (la même à chaque plan) et propre à chacun. Un cercle parfait donne un effet « autocollant ».

## 7. Ombre au sol et finition

- L'ombre au sol est un **mélange du sol avec une teinte** (et non une multiplication) : à 72 % avec `#4664b8` en plein jour, à 87 % avec `#202d6c` au couchant. Elle est **attachée aux pieds**, nette près des semelles, floue avec la distance (bord flou sur 0,11 à 0,13 D), avec une ombre de contact. De nuit : une tache sous les pieds, floue sur 0,36 à 0,63 D (non vérifié sur nos plans).
- **En intérieur chaud**, la référence n'a pas d'ombre portée nette : une tache douce sous les pieds et une ombre de contact. Notre essai (tache, contact, ombre courte très douce à l'opposé de la lampe) a été jugé **trop timide et sans direction lisible** par le critique ; à reprendre.
- **Accord au décor** : par la palette de l'ambiance, jamais par une teinte générale. Un accord chaud appliqué à tout le personnage en intérieur a **sali les blancs** (une barbe et des sourcils clairs ont viré au beige) : s'il faut assombrir ou réchauffer, épargner les hautes lumières.
- Un personnage **hors du plan de netteté** est flouté comme le décor à la même profondeur.
- Accentuation finale de l'image après l'incrustation des personnages et avant les sous-titres : masque flou de rayon 1 px à 70 %.

## 8. La limite

Ces chiffres décrivent **une technique de rendu** : comment un trait s'épaissit, où tombe une ombre, quelle largeur a un filet de lumière. On ne reprend **jamais un personnage, un costume ou un accessoire** du film qui a servi à la mesure, ni d'aucune autre chaîne. Les personnages restent ceux du client. Les bosses propres au trait d'un dessin ne se recopient pas : on applique la loi.

## 9. Contrôler

Avant de valider un style de personnage : rendre une tête à la taille d'une tête de référence (ou à 300 px de diamètre), passer `mesurer.py` du skill `reproduire-reel`, et vérifier dans `loi_simple` que le délié vaut ≈ 0,018 D, le plein ≈ 0,07 D, et que le plein est à l'opposé de la lumière déclarée. Une impression à l'œil ne suffit pas : lors de l'essai, deux remarques d'un critique sur ce rendu ont été démenties par la mesure.
