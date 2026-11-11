---
name: formats-flotweb
description: "Catégorie « Formats Flot Web » du studio motion : cinq formats de vidéo complets et éprouvés, prêts à adapter à la chaîne du client : fait insolite en 3D vue en coupe, leçon en pixel art (rater le niveau puis le réussir), science en pixel art (une histoire vraie puis le principe), histoire 2D interactive dont la communauté vote la suite, et recréation du motion design d'un reel. À utiliser quand le client veut un format de série récurrent, dit « un fait en 3D », « vue en coupe », « pixel art », « une histoire à épisodes », « le public vote », ou envoie un reel avec « refais-moi ça », « même accroche », « mêmes animations »."
---

# Formats Flot Web (catégorie 12)

Cinq **formats**, pas seulement des looks : chacun vient avec sa structure d'épisode, ses règles d'écriture, sa recette et sa liste d'erreurs déjà faites. Ils ont été rodés sur des dizaines d'épisodes publiés, puis **rendus génériques** : aucun personnage, aucune voix, aucun compte ni aucun réglage de marque n'y est attaché.

**Chaque format lit la fiche « ma chaîne » du client** (skill `marque`) : le sujet de la chaîne, le ton, la voix, la palette, la police, les personnages récurrents, la formule d'ouverture ou de chute, la durée. Si la fiche n'existe pas, `studio-coeur` la construit d'abord (au moins le paramétrage express).

Le skill `studio-coeur` pilote le parcours. `principes-mouvement` (mouvements cités par leur numéro `#NNN`), `rendu` (HyperFrames, export), `son` (−14 LUFS, vrais enregistrements d'abord, environ 5 bruitages par 10 s), `personnages` (héros, mascotte, jeu d'acteur) et `blender` (3D par le connecteur `blender`) s'appliquent.

## Les formats

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `fait-3d-en-coupe` | Fait insolite en 3D vue en coupe | Un bloc de terrain coupé, une scène qui se transforme étape par étape, chaque élément surgit sur son mot | three dans hyperframes (blender en option) | élevée | à produire |
| `lecon-pixel-art` | Leçon en pixel art | La leçon comme un niveau de jeu : niveau raté, leçon, objets à ramasser, niveau réussi | hyperframes (canvas 135×240) | moyenne | à produire |
| `science-pixel-art` | Science en pixel art | Une histoire vraie et surprenante, puis le principe ; un visuel littéral par phrase ; boucle parfaite | hyperframes (canvas 270×480) | élevée | à produire |
| `histoire-2d-interactive` | Histoire 2D interactive | Une série à suspense en 2D à contours d'encre ; chaque épisode finit sur un vote entre deux options | hyperframes (SVG) + `personnages` | élevée | à produire |
| `recreation-reel` | Recréation de reel | On mesure un reel, on écrit un cahier chiffré, on reconstruit, on prouve la ressemblance ; textes, marques et voix remplacés | hyperframes (+ three / blender) | élevée | à produire |

Ce sont des formats maison : il n'y a pas d'aperçu de tiers à citer. Les aperçus seront produits avec le plugin.

## Comment choisir

| Le client veut… | Format |
|---|---|
| Expliquer un objet, un lieu, une construction ; « comment ça marche », « ce qu'il y a dessous » | `fait-3d-en-coupe` |
| Apprendre à faire quelque chose : la mauvaise façon, puis la bonne | `lecon-pixel-art` |
| Vulgariser un principe par une histoire vraie, avec des chiffres sourcés | `science-pixel-art` |
| Fidéliser avec une histoire à épisodes où le public décide | `histoire-2d-interactive` |
| Reprendre la forme d'un reel qui marche, avec ses propres contenus | `recreation-reel` |

Questions qui tranchent : **le client a-t-il une vidéo de référence ?** (oui → `recreation-reel`, ou le format le plus proche avec `references/mesurer-une-reference.md`) · **explique-t-il, ou raconte-t-il ?** (explique → 3D en coupe, leçon, science ; raconte → histoire interactive) · **peut-il publier une suite ?** (non → pas d'histoire interactive).

Débutant : `lecon-pixel-art` (aucune 3D, structure fixe). Le format 3D demande une machine capable de longs rendus, ou Blender.

## Ce que chaque format demande à la fiche « ma chaîne »

| Rubrique de la fiche | 3D en coupe | Leçon pixel | Science pixel | Histoire 2D | Recréation |
|---|---|---|---|---|---|
| Niche et sujet | le fait du jour | la leçon | le principe | le genre | les contenus de remplacement |
| Persona, voix, tu ou vous | oui | oui (souvent la voix du client) | oui | narrateur + voix des personnages | oui |
| Palette et police | habillage | l'univers du jeu | couleurs de marque en cinq rôles | palette de l'histoire | si elle remplace celle de la référence |
| Personnages récurrents | mascotte (facultative) | le héros | le présentateur | narrateur ou personnage qui revient | ceux qui remplacent ceux de la référence |
| Formules | chute | accroche parlée, annonce de la suite | accroche au tableau, phrase d'abonnement | formule d'ouverture, façon de voter | selon la référence |
| Durée et rythme | 50 à 60 s | 50 à 110 s | ~2 min, ou ~70 s | ~1 min 50 par épisode | celle de la référence |
| Jamais | à respecter dans tous les formats | | | | |

S'il manque un personnage récurrent, le créer avec le skill `personnages`, le faire valider, puis **l'enregistrer dans la fiche** : il ne change plus d'un épisode à l'autre.

## Règles communes à la catégorie

1. **La fiche « ma chaîne » d'abord.** Aucun format ne choisit seul une voix, une couleur de marque, un personnage ou une formule : il les lit dans la fiche, ou propose et fait valider.
2. **Adapter sans copier.** D'une référence on reprend la structure, le rythme et la grammaire visuelle ; on réécrit textes, noms et chiffres ; on ne reproduit aucun personnage, logo ni musique d'un autre créateur. Détail : `references/mesurer-une-reference.md` §1.
3. **Rien de deviné quand une référence existe** : tableau des plans mesuré, tailles relevées sur une grille, couleurs à la pipette, planche de comparaison.
4. **Il se passe quelque chose dans chaque plan, rien n'est figé, chaque plan diffère du précédent.** Contrôles image par image obligatoires avant livraison.
5. **Une ouverture neuve à chaque épisode** : jamais les mêmes plans, cadrages ou enchaînements que l'épisode précédent.
6. **Les faits sont vérifiés** : chaque chiffre a sa source ; un point incertain ne s'affiche jamais à l'écran. Sujets dangereux refusés.
7. **Zones d'interface** (1080×1920) : rien d'important au-dessus de y = 160, en dessous de y = 1560, ni à droite de x = 945 ; **le décor va jusqu'aux bords**, jamais de bandes ni d'image réduite. Les fiches pixel art donnent les mêmes zones dans leur grille.
8. **Pixel art = pixels entiers** : on dessine plus petit, on ne réduit jamais l'image ; agrandissement au plus proche voisin par un facteur entier.
9. **Son** : skill `son`. Les anciennes habitudes « un souffle à chaque mouvement » et « un son pour chaque action » sont remplacées par le budget : chaque son a une cause visible, mais toute action n'a pas de son. Bruitages de jeu synthétisés dans les formats pixel art (c'est le son juste du genre).
10. **Une couverture par épisode**, faite exprès sur l'accroche : titre lisible et sujet dans le **centre 3:4** de l'image verticale, rien derrière le titre.
11. **Chaque remarque du client devient une règle** : l'ajouter à sa fiche « ma chaîne » (rubrique « Jamais » ou notes du format), pour ne jamais la recevoir deux fois.
12. **Quand le client demande une retouche, on ne touche qu'à ce qu'il cite.**
13. **Rien ne se publie sans l'accord explicite du client** pour cette vidéo ; les réponses aux commentaires aussi.

## Déroulé d'un épisode (tous formats)

1. Lire la fiche « ma chaîne » et les scripts des épisodes précédents du client ; pour une série à votes, lire et compter les votes.
2. Référence éventuelle : `references/mesurer-une-reference.md`.
3. Histoire : `references/histoire.md` de `studio-coeur` ; pour une série, `references/serie-a-votes.md` (bible, scripts de tous les épisodes, relecture par un regard neuf). Validation du client.
4. Storyboard en planches (rendues avec le vrai code de dessin). Validation du client.
5. Voix, calage au mot, animation, son.
6. Rendu, couverture, **relecture complète en boucle** (lecture continue + image par image), `scripts/controle_rendu.py`, puis la porte de livraison et le relecteur de `studio-coeur`.
7. Livraison : vidéo, couverture, légende prête à copier, et ce qui a été vérifié.

## Références et scripts de la catégorie

| Fichier | Contenu |
|---|---|
| `references/mesurer-une-reference.md` | ce qu'on reprend ou non, tableau des plans, mesures sur grille, plan d'implantation vu de dessus, règles de caméra, vérifications avant rendu, relecture en boucle, liste des erreurs déjà faites |
| `references/serie-a-votes.md` | bible de série, échelle des révélations, ouvertures neuves, écriture et comptage du vote, branches, relecture par un regard neuf |
| `scripts/analyse_reference.sh` | passe d'analyse automatique d'une vidéo de référence (coupes, évènements, planches, images par plan) ; repli ffmpeg si `hyperframes measure` est absent (cas de la 0.9.33), sans carte des évènements |
| `scripts/controle_rendu.py` | images figées, plans trop semblables, comparaison du découpage et de l'énergie de mouvement avec la référence |

## Fiches

`styles/<identifiant>/STYLE.md`, dix sections fixes. Crédits : `licenses/formats-flotweb.md` à la racine du plugin.
