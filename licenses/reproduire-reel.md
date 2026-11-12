# Crédits du skill `reproduire-reel`

## Origine

Le skill, ses références, ses gabarits et ses scripts sont un **travail du studio Flot Web**. Ils viennent d'un essai interne mené les 11 et 12 novembre 2026 : l'analyse d'un reel de référence en lecture continue, puis sa mesure au pixel, pour refaire sa technique avec les personnages et l'histoire d'un film du studio. La méthode a ensuite été rejouée de zéro, par un agent qui ne connaissait que ce skill, sur la même vidéo ; les chiffres obtenus concordent avec ceux de la première mesure, et les défauts trouvés ont été corrigés.

| Fichier | Origine |
|---|---|
| `SKILL.md`, `references/`, `gabarits/` | écrits par Flot Web d'après les comptes rendus de l'essai |
| `scripts/mp_base.py`, `mp_coupes.py`, `mesurer.py`, `extraire.py`, `grille.py` | scripts de mesure de l'essai (Flot Web), nettoyés de tout chemin et de toute référence au film étudié |
| `scripts/mp_forme.py` | réécriture généralisée du module de mesure d'une tête ronde de l'essai : cercle, ellipse, rectangle, polygone, masque |
| `scripts/comparer.py`, `synthese.py` | réécritures génériques des scripts de contrôle et de synthèse de l'essai |
| `scripts/bandes.py` | script de bandes de lecture continue de l'essai |
| `scripts/decouper.py`, `palette.py`, `cote_a_cote.py` | écrits pour ce skill ; l'idée du découpage par deux détecteurs et de l'image par plan vient de `formats-flotweb/scripts/analyse_reference.sh` (Flot Web) |

Aucun code de tiers n'est copié.

## Outils et méthodes de tiers

- **FFmpeg** (https://ffmpeg.org, LGPL / GPL selon la compilation) : lecture des images et mesure du niveau sonore, appelé en ligne de commande. Non redistribué : il s'installe chez le client.
- **NumPy** (BSD 3 clauses), **Pillow** (licence MIT-CMU), **OpenCV** (Apache 2.0) : bibliothèques Python appelées par les scripts. Non redistribuées.
- **Écart de couleur CIEDE2000** : formule publiée par la Commission internationale de l'éclairage (Sharma, Wu et Dalal, 2005, pour la mise en œuvre de référence) ; réécrite dans `mp_base.py`.
- **Luminance Rec. 709** : coefficients de la recommandation UIT-R BT.709.
- **Critique par un agent indépendant, quatre champs OÙ / PROBLÈME / CHANGEMENT / À GARDER** : méthode du skill `studio-coeur` (voir `licenses/studio-coeur.md`).

## Ce que le skill ne contient pas

- **Aucune image, aucun son, aucun texte de la vidéo étudiée pendant l'essai.** Ni son nom, ni celui de sa chaîne, ni un lien vers elle. Les exemples chiffrés du skill (épaisseurs en fraction du diamètre de la tête, durées en images) décrivent une technique, pas une œuvre.
- Aucun personnage, costume, accessoire ou logo d'un tiers.
- Aucun chemin de dossier, aucun compte, aucune clé, aucun identifiant.

## Vérification du studio

Essai réel du 12 novembre 2026 : découpage, lecture continue de 3 plans, mesure de 4 images (6 formes rondes, un polygone, un texte), fiche remplie, par un agent neuf, en 20 minutes ; puis un essai à vérité connue sur des formes dessinées (cercle à pleins et déliés, ellipse, masque, contour clair, trait constant), retrouvées à 0,2 px près ; puis une relecture indépendante du code, dont les deux défauts bloquants et les quatre défauts sérieux ont été corrigés et rejoués. Essais sous Windows seulement. Ce qui n'a pas été essayé est listé dans `skills/reproduire-reel/references/fichier-de-cibles.md`, section 7.
