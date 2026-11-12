---
name: personnages
description: "Créer des personnages 2D en pièces (SVG), leur planche d'expressions, les monter dans Blender (plans à matériau émissif avec ombre de contact) ou en calques HyperFrames, et les faire jouer (ligne de jeu par plan, 31 émotions). À utiliser dès qu'une vidéo a un personnage dessiné, une mascotte ou un narrateur à l'écran."
---

# Personnages 2D en pièces

Un personnage du studio est un **jeu de pièces plates** (tête, corps, bras, jambes, costume) et une **planche d'expressions** (yeux, bouches, extras) qu'on échange, comme dans l'animation par remplacement. On le dessine une fois, on le fait jouer dans toutes les vidéos de la chaîne.

Ce skill couvre quatre choses :

1. dessiner les pièces en SVG ;
2. faire la planche d'expressions ;
3. monter le personnage, dans Blender (2.5D) ou dans HyperFrames (2D) ;
4. le **faire jouer**, ce qui compte le plus.

Le parcours général vient de `studio-coeur`. Si la fiche « ma chaîne » (skill `marque`) décrit déjà un personnage, partir d'elle. Les principes de mouvement viennent de `principes-mouvement`.

## Règles de dessin (valables pour tous les styles)

- **Aplats de couleur**, un seul poids de contour sombre, pas de dégradé, pas de texture, pas d'ombrage réaliste. Le contour est épais par défaut (12 à 16 unités du gabarit), **mais la fiche de style l'emporte** : quand le `STYLE.md` choisi donne une épaisseur de trait, une couleur d'encre ou une matière de trait (3 à 5 px avec des manques pour `cartoon-annees-50`, par exemple), c'est elle qu'on applique au personnage, et on la note dans sa `fiche.md`. Voir `references/pieces-svg.md`, « Pièces SVG dans un style au trait propre ». Personne n'attend de réalisme d'un personnage à tête ronde : rien ne peut donc sembler étrange.
- **Silhouette lisible à 200 px de haut** : une forme de tête, un élément de costume reconnaissable (chapeau, col, tablier), une couleur d'accent que le décor n'utilise pas.
- Le noir pur et le blanc pur sont évités : une encre très sombre et un blanc cassé.
- **Personnage original.** Ne jamais reprendre le personnage, la mascotte ou le dessin d'une autre chaîne, d'une marque ou d'un jeu. On peut étudier la grammaire d'un style, jamais copier un personnage.
- 2 à 4 personnages par vidéo au maximum ; les figurants sont des variantes (même corps, autre costume, autre couleur).

## Personnage éclairé : trait à pleins et déliés, ombrage, lumière (valeurs mesurées)

Les règles ci-dessus donnent un personnage plat, à trait constant. Quand le style demande un personnage **éclairé** (catégorie `styles-2-5d`, ou un reel étudié avec le skill `reproduire-reel`), le studio a mesuré au pixel un rendu de référence et l'a contrôlé sur ses propres personnages. Sept points, détaillés dans `references/trait-et-lumiere-mesures.md` (D = diamètre de la tête) :

1. **Le contour suit une loi, pas une épaisseur** : `épaisseur = 0,044 D − 0,028 D × cos(angle depuis la lumière)`, soit 0,018 D côté lumière et 0,07 D côté ombre. On le construit comme un disque d'encre et un disque de peau plus petit, décalé de 0,028 D vers la lumière. Même règle pour le torse et les coiffes.
2. **La direction de la lumière à l'écran est un paramètre obligatoire de chaque plan.** Elle commande le côté du plein, du croissant d'ombre, du filet de lumière et de l'ombre au sol. Sans elle, le rendu retombe sur un trait constant.
3. **La tête n'est pas un aplat** : peau en aplat, plus un croissant d'ombre à bord doux (décalage 0,24 rayon, flou 0,02 D) du côté opposé à la lumière, plus un filet de lumière effilé (0,021 D de large, à 0,033 D du trait) du côté éclairé. Une bande horizontale n'apparaît que sous une coiffe à bord.
4. **Une palette par ambiance** (plein jour, coucher de soleil, intérieur, nuit) pour l'encre, les membres, la peau, le croissant et le filet. On change la palette de la peau et du trait, **pas la couleur du costume** ; de nuit la peau reste crème.
5. **Épaisseurs** : membres 0,056 D, constants ; traits fins du visage 0,0235 D ; sourcils en formes pleines de 0,05 D ; anneau de l'œil 0,22 D, intérieur de la couleur de la peau.
6. **Une tête légèrement irrégulière** (rapport d'axes 0,91 à 0,98), fixe par personnage.
7. **La limite ne bouge pas** : on reprend une technique de rendu, jamais un personnage, un costume ou un accessoire d'une autre chaîne.

**Ce qui est vérifié** : le plein jour et le coucher de soleil, sur nos plans de test, avec un contrôle chiffré (35 grandeurs sur 51 dans la tolérance, les autres tenant surtout à la forme propre du dessin de référence). **La nuit et l'intérieur ne sont pas vérifiés** : leurs valeurs sont dans la référence, aucun de nos plans ne les a encore utilisées. Les coiffes éclairées (trois tons) et la jambe du second plan éclaircie ne sont pas faites.

## Étape 1 : les pièces

Détail, gabarit et conventions de nommage : `references/pieces-svg.md`.

| Pièce | Fichier | Pivot |
|---|---|---|
| Tête (une forme ronde, sans visage) | `tete.svg` | bas de la tête (le cou) |
| Corps | `corps.svg` | bas du corps (le bassin) |
| Bras gauche, bras droit | `bras-g.svg`, `bras-d.svg` | l'épaule |
| Jambe gauche, jambe droite | `jambe-g.svg`, `jambe-d.svg` | la hanche |
| Costume (chapeau, coiffe, cape, accessoire de rôle) | `costume-<nom>.svg` | selon la pièce qui le porte |

Chaque pièce est un fichier SVG à fond transparent, dessiné dans le même repère que les autres (on peut les empiler sans les déplacer). Le visage n'est **pas** dessiné sur la tête : il vient de la planche d'expressions.

## Étape 2 : la planche d'expressions

Jeu minimal (celui du cours 2.5D), un fichier par élément :

| Famille | Éléments |
|---|---|
| Yeux | `neutre`, `grands`, `plisses`, `fermes`, `regard-cote` |
| Bouches | `fermee`, `petite-ouverte`, `grande-ouverte`, `moue`, `sourire` |
| Extras | `goutte` (sueur), `rouge-joues` |

Avec 5 yeux, 5 bouches et 2 extras, on couvre déjà la plupart des 31 émotions décrites dans `references/31-emotions.md`. Ajouter un élément seulement quand une ligne de jeu le réclame (yeux en larmes, sourcils froncés, point d'exclamation).

Assembler ensuite une **planche de contrôle** : une image avec le personnage complet dans 8 à 12 expressions, sur fond neutre, et la montrer au client avant d'animer.

## Étape 3 : monter le personnage

| Vidéo | Montage | Référence |
|---|---|---|
| 2.5D : le personnage est **dans** un décor 3D | Plans dans Blender, matériau émissif, ombre de contact | `references/import-blender.md` |
| 2D, ou plan fixe sur une image de décor | Calques HyperFrames animés avec GSAP | `references/calques-hyperframes.md` |

Dans les deux cas : mêmes pièces, mêmes noms, mêmes pivots, mêmes numéros d'image.

Pour la 2.5D, le kit de la catégorie `styles-2-5d` fournit deux pantins :

- **le générateur paramétré de la chaîne mesurée** (`kit/pantin.py`) : le client décrit ses personnages (couleurs du costume, coiffe, accessoire, proportions) et le générateur les dessine au rendu mesuré ci-dessus, de face et de trois quarts, avec coude, genou, mains, expressions et une classe `Anim` pour le jeu (`snap` : pose en une image ; `va` : geste ; `cligne` : clignement de 3 images). Chaque pose reçoit l'ambiance (`amb`) et la direction de la lumière (`lum`). Il ne contient aucun personnage tout fait. C'est celui du style `tete-ronde-trait-plein-delie` ;
- **le pantin à plans émissifs** de l'ancienne chaîne (`kit/personnages.py` dessine les pièces et écrit `rig.json` ; la classe `Perso` de `kit/bl_lib.py` le monte dans Blender) : plat, à trait constant, une seule vue. Il sert à `theatre-de-papier`. Son personnage d'exemple est à remplacer par un dessin original.

## Les limites du pantin (à lire avant d'écrire la liste de plans)

Un film réel de 36 plans et huit pantins, fabriqué par le studio le 11/11/2026, a montré où le pantin s'arrête. Détail, contournements et marche à suivre : `references/limites-du-pantin.md`.

| Il sait | Il ne sait pas |
|---|---|
| rester plat et à sa couleur, posé au sol par son ombre | être vu autrement que **de face** : ni trois quarts, ni profil, ni dos |
| faire face à la caméra | tourner la tête (le regard est un glissement du visage) |
| changer d'yeux et de bouche, cligner | **pointer** : le bras est une pièce raide sans coude, la main n'a pas de doigt, il ne désigne que dans le plan de l'image |
| incliner la tête, pencher le tronc, lever un bras avec anticipation et tenue | **tenir** un objet (aucun point d'attache : un pinceau tenait debout à 40 cm de la main) |
| glisser d'un point à un autre et s'arrêter net (clé d'arrivée tenue) | **marcher** : les jambes sont une seule pièce, `marche()` n'est qu'un rebond du tronc |
| servir de figurant en changeant couleurs et hauteur | s'asseoir, se pencher en avant, passer un bras derrière le corps |

Conséquences pour la liste de plans : le personnage **réagit**, l'objet héros **agit** ; on varie par le cadre, pas par la pose ; on désigne un objet placé à côté du personnage dans l'image ; on coupe sur un personnage déjà arrivé plutôt que de le faire marcher ; pas plus de deux plans de suite dans le même axe.

**Ajouter une vue**, en bref : un second jeu de pièces dans le même repère (mêmes noms, même hauteur, même trait), ses propres visages, une entrée de plus dans `rig.json`, une planche de comparaison validée, puis l'échange des deux vues **à une coupe**, jamais pendant un plan. Le kit sait monter cette seconde vue et la retourner en miroir ; le dessin reste à faire. Aucune vue de profil, de trois quarts ou de dos n'est fournie.

Trois règles pour la 2.5D :

1. **Le décor n'ombre jamais le personnage.** Matériau émissif : les lumières du décor ne changent pas ses couleurs. Un personnage éclairé comme un objet 3D casse le style.
2. **Une ombre de contact douce sous les pieds**, sinon il flotte.
3. **Il est placé à la marque de mise au point** du plan (skill `blender`), donc net pendant que le fond est flou.

## Étape 4 : le faire jouer

Détail et exemples : `references/jeu-d-acteur.md`.

Le signe le plus rapide d'une animation générée : **le personnage ne pense jamais.** Il rebondit, salue, sourit, mais rien ne se passe sur son visage avant qu'il bouge.

Avant d'animer, écrire **une ligne de jeu par plan** :

```
PLAN 07 (2,1 s, images 372-434)  « toute la cour a ri »
  pensée        l'inventeur sait qu'il a raison
  anticipation  les yeux se plissent d'abord, 4 images avant tout autre mouvement (image 380)
  action        la tête se tourne vers la caméra sur le mot « ri » (image 396)
  tenue         rester sur le regard 10 images pour qu'il se lise (396-406)
```

Les quatre champs :

| Champ | Ce qu'on écrit | Règle |
|---|---|---|
| **Pensée** | Ce que le personnage comprend, veut ou décide dans ce plan. | Une seule par plan. Pas de pensée, pas de plan avec ce personnage. |
| **Anticipation** | Le petit mouvement qui précède : toujours **un regard d'abord**. | Les yeux bougent 3 à 6 images avant le reste. |
| **Action** | Le mouvement principal, calé sur **un mot** de la voix. | Un seul mouvement principal par plan. |
| **Tenue** | Le temps où l'on reste sur la pose pour qu'elle se lise. | 8 à 12 images au minimum (24 pour une réaction importante). |

Règles fermes :

- **Pas de rebond gratuit.** Aucun balancement, sautillement ou hochement en boucle sans raison. Au repos, le personnage respire à peine (1 à 2 % d'échelle verticale, cycle de 3 à 4 s) et cligne des yeux.
- **Deux registres, un seul par vidéo** (détail dans `references/31-emotions.md`) : le **jeu sobre** est le défaut, et il est obligatoire pour `styles-2-5d` et tout style au ton réaliste : aucune boucle de corps. Le **jeu cartoon** vaut pour la catégorie `styles-cartoon`, les mascottes et les vidéos musicales : le corps peut bouger en boucle, mais **seulement calé sur le tempo de la musique** (un rebond par temps), jamais sur une boucle libre. Dans les deux registres, les autres règles tiennent : une pensée par plan, un regard d'abord, anticipation, tenue.
- **Tout mouvement commence par un regard.**
- **Les bouches ne changent que sur les mots accentués** de la voix (2 à 4 par phrase), pas sur chaque syllabe. Entre deux, bouche fermée.
- **Les visages ne claquent pas** : un changement d'expression passe par un plissement des yeux (2 à 3 images), l'échange sous le plissement, puis une petite réaction du corps dont la taille dépend de l'émotion.
- **Pas de jumeaux** : les deux bras ne font pas la même chose, deux personnages ne bougent pas en même temps.
- Les poses clés doivent se lire **en image fixe** avant qu'on ajoute le mouvement entre elles.

## Les 31 émotions

`references/31-emotions.md` liste 31 émotions jouées, en six familles, chacune décrite par ses yeux, sa bouche, sa couleur ou son accessoire, sa manière de bouger et la taille de sa réaction.

| Famille | Émotions |
|---|---|
| Joie | joyeux, excité, rire, amoureux, fier, émerveillé, taquin, plein d'espoir, soulagé |
| Malice | suffisant, décontracté, espiègle, méfiant |
| Bas | triste, en pleurs, ennuyé, endormi, K.-O. |
| Chaud | en colère, furieux, déterminé, dégoûté |
| Alerte | effrayé, nerveux, surpris, perplexe, étourdi |
| Esprit | neutre, pensif, idée, timide |

Dans la liste de plans, la colonne « personnage » nomme une de ces émotions ; la ligne de jeu dit quand on y entre.

## Contrôle visuel

On ne voit pas un mouvement en lisant du code. Pour chaque plan avec un personnage :

1. **Poses clés en images fixes** (début, action, tenue) : se lisent-elles sans le mouvement ?
2. **Bande d'images** autour de l'action (toutes les images sur une demi-seconde) : y a-t-il une anticipation ? Un saut ou un claquement ? Les parties bougent-elles à des instants différents ?
3. **Gros plan du visage** à pleine résolution pour chaque réaction qui porte l'histoire.
4. **Contacts** : les pieds touchent le sol, ce qui est tenu touche la main.

Dans Blender : `look(mode="frames", frames=[…], view="camera")`. Dans HyperFrames : les images de contrôle du skill `rendu`.

## Liste de contrôle

- [ ] Pièces séparées, fond transparent, un seul poids de contour (celui de la fiche de style si elle en donne un), aplats.
- [ ] Personnage éclairé : la direction de la lumière est déclarée pour chaque plan ; plein, croissant et ombre au sol sont du côté opposé, filet du côté éclairé ; nuit et intérieur signalés comme non vérifiés.
- [ ] Planche d'expressions validée par le client.
- [ ] Personnage original (aucun personnage tiers).
- [ ] 2.5D : matériau émissif, ombre de contact, placé à la marque de mise au point.
- [ ] Une ligne de jeu par plan, avec ses quatre champs et ses numéros d'image.
- [ ] Jeu sobre : aucun rebond en boucle. Jeu cartoon : boucle du corps calée sur le tempo, jamais libre. Dans les deux cas, un regard avant chaque mouvement.
- [ ] Bouches échangées seulement sur les mots accentués.
- [ ] Poses clés lisibles en image fixe ; tenue d'au moins 8 images.
- [ ] Personnage assez grand : au moins un quart de la hauteur du cadre en plan moyen.
- [ ] Aucun plan ne demande ce que le pantin ne sait pas faire (autre vue que celles dessinées, main qui pointe vers le fond, objet tenu sans attache, marche en plan moyen) ; aucun déplacement sans clé d'arrivée tenue.

## Références

- `references/pieces-svg.md` : gabarit, nommage, pivots, export.
- `references/trait-et-lumiere-mesures.md` : loi du contour, direction de la lumière, ombrage de la tête et du torse, palettes par ambiance, épaisseurs, ombre au sol ; ce qui est vérifié et ce qui ne l'est pas.
- `references/31-emotions.md` : les 31 émotions jouées, décrites une par une.
- `references/jeu-d-acteur.md` : la ligne de jeu, les changements d'expression, les bouches, les erreurs.
- `references/import-blender.md` : plans à matériau émissif, ombre de contact, échange d'expressions.
- `references/limites-du-pantin.md` : ce que le pantin du kit sait et ne sait pas faire, comment écrire les plans avec, comment ajouter une vue.
- `references/calques-hyperframes.md` : le même personnage en calques HyperFrames.

Crédits : voir `licenses/personnages.md` à la racine du plugin.
