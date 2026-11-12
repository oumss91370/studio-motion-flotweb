# Lecture continue : lire le mouvement image par image

Une planche toutes les 0,5 s montre **quoi** se passe. Elle ne montre pas **comment** : une pose qui change en une seule image, un clignement de trois images, deux images d'anticipation avant un geste, un freinage de caméra de dix images. Or c'est là que se trouve le style d'un jeu et d'une caméra. La lecture continue regarde **toutes** les images.

## 1. Extraire

```
python $S/bandes.py reference/ref.mp4 analyse/bandes/P07.jpg --plans analyse/decoupage/plans.json --plan P07
python $S/bandes.py reference/ref.mp4 analyse/bandes/tout.jpg 0 1681 --max 48          # tout le film, 48 images par planche
python $S/bandes.py reference/ref.mp4 analyse/bandes/P07-visage.jpg 412 429 --crop 250,180,560,560 --larg 320 --cols 6
```
- La bande d'ensemble (vignettes de 216 px) donne le mouvement du corps et de la caméra.
- La bande **recadrée** (`--crop x,y,largeur,hauteur`, en pixels de la source) suit un visage, une main, un objet : indispensable pour les yeux et la bouche.
- Chaque vignette porte son **numéro d'image** : c'est l'unité de toutes tes durées.
- Pour une mesure de distance (amplitude d'un hochement, longueur d'un pas), extrais deux images en pleine résolution (`extraire.py`) et mesure sur la grille (`grille.py`).

## 2. Lire et décrire

Remplis `gabarits/lecture-continue.md`, une ligne par évènement, dans l'ordre. Pour chaque plan, cherche :

| Question | Ce qu'on note |
|---|---|
| Y a-t-il une **anticipation** ? | combien d'images avant le geste, et quoi (un regard, un recul, des yeux qui se ferment) |
| Combien d'images dure **chaque geste** ? | départ, milieu, arrivée ; images lentes, rapides, de freinage |
| Y a-t-il un **dépassement** et un retour ? | amplitude, nombre d'images |
| Combien de temps dure la **tenue** ? | nombre d'images strictement figées ; ce qui vit pendant la tenue (clignement, respiration, rien) |
| Le changement d'expression passe-t-il par des **images intermédiaires** ? | « 1 image, sans intermédiaire », ou la liste des images de passage |
| **Clignements** | nombre d'images, fréquence au repos, absents pendant quoi |
| **Étirement, écrasement** | en % de la taille, sur combien d'images ; ou « aucun » |
| **Qui joue** dans un plan à plusieurs ? | un seul à la fois ? décalage en images entre deux réactions |
| **Caméra** | fixe, dérive (px par image), déplacement : images de départ, de croisière, de freinage ; coup de zoom (%, images) |
| **Transition** d'entrée et de sortie | type exact, durée en images ; le plan entrant est-il déjà en mouvement ? |
| **Effets** | traînées, lignes de vitesse, poussière, étincelles : durée en images, taille |
| **Action et mot** | l'action tombe combien d'images avant ou après l'apparition du mot du sous-titre |
| **Animation par paliers** | une pose nouvelle par image, ou tenue 2 ou 3 images (animation « en deux », « en trois ») |

Règles d'écriture :
- des **nombres d'images**, jamais « rapide » ou « un instant » ;
- le **numéro de l'image** où l'évènement commence, pour pouvoir y retourner ;
- « mesuré » (relevé sur une image pleine résolution, avec la grille), « lu » (vu sur une bande réduite), « lu sur bande recadrée » (bande `--crop`, plus fiable pour un visage) ou « supposé » : écris lequel ;
- la taille du sujet dans le cadre (« à 62 % de la hauteur ») se mesure sur l'image nette du plan avec `grille.py` ; estimée sur une vignette, elle porte « lu » ;
- ce qui **ne bouge pas** compte autant que ce qui bouge (un personnage figé 160 images est un choix de style).

## 3. Du relevé au catalogue

Regroupe ensuite les relevés par type d'action et donne la fourchette : « changement d'expression : 1 image, sans intermédiaire (4 cas) », « clignement : 3 images, un toutes les 13 à 25 images au repos », « tenue avant un geste : 13 à 46 images ». Ce catalogue des poses et des durées va dans la fiche de la référence (section 3), avec les numéros d'image d'exemple. C'est lui qui règle ensuite le jeu de nos personnages.

Cherche aussi **ce qui rend le jeu efficace** (contraste entre un personnage qui surjoue et un autre figé, tenue longue après une chute, regard caméra) : une phrase par idée, chacune appuyée sur des images.

## 4. Partager le travail

Un reel d'une minute fait près de 1 700 images, soit une trentaine de planches. Pour aller vite :
- coupe le film en tranches qui se recouvrent de 20 à 30 images, une par sous-agent (quatre tranches pour une minute) ;
- donne à chacun la même consigne, le gabarit, sa plage d'images et les bornes des plans ;
- demande à chacun un fichier `lecture-continue/partie-X.md` et la liste des images qu'il a dû regarder en grand ;
- un sous-agent de plus pour le son (skill `son`) ;
- toi, tu assembles le catalogue et tu vérifies sur les bandes les trois chiffres les plus surprenants de chaque partie.

Dans l'essai du studio, cette lecture complète a pris une trentaine de minutes à quatre agents, plus un pour le son.

## 5. Ce que la lecture continue ne donne pas

Elle donne des durées et une description. Elle ne donne **ni épaisseur, ni couleur, ni forme d'ombrage fiables** : sur des vignettes de 216 px, un trait à pleins et déliés ressemble à un trait constant, et l'ombre d'un chapeau à un dégradé de la tête. Dans l'essai du studio, trois affirmations de cette étape ont été corrigées ensuite par la mesure au pixel. Tout ce qui touche au rendu se mesure à l'étape 4.
