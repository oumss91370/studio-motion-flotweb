# Tableau blanc à la main

## 1. Identité

- **Nom** : Tableau blanc à la main (explication dessinée par une main sur un grand tableau).
- **Inspiration** : les conférences illustrées au feutre sur un immense tableau blanc, où une main dessine pendant que l'orateur parle, et les courtes vidéos de science dessinées feuille par feuille.
- **La règle en une phrase** : l'orateur dit une phrase, **la main écrit un mot et dessine une image** sur un grand tableau ; la caméra suit le raisonnement en se déplaçant sur le tableau ; à la fin elle recule, et le spectateur voit que **tout le raisonnement est une seule image**.
- **Choisir une des deux grammaires, sans les mélanger** :
  - **Grand tableau** (celle de cette fiche) : un seul tableau, la caméra s'y déplace, environ 5 mouvements par minute.
  - **Feuille par feuille** : une feuille par idée, coupe sèche pour changer de feuille (environ 8 par minute), caméra fixe, traits plus épais, papier légèrement teinté, crayon de couleur pâle.
- **Marche pour** : un raisonnement (conférence, opinion, chaîne de causes, fil historique), des idées **qui ont des liens entre elles** et peuvent se dessiner comme une carte ; une courte explication en une chaîne logique. Voix au débit régulier, mots clés nets.
- **Ne marche pas pour** : des graphiques de données précis (le dessin à la main est imprécis), des mouvements ou des relations complexes dans l'espace (aucune profondeur), une forte intensité émotionnelle (le trait d'une seule couleur exprime peu). À savoir : les études ne montrent pas qu'on **apprend mieux** avec ce format ; sa valeur est de retenir l'attention et de tenir compagnie.
- **À ne pas confondre** avec `tableau-blanc` de la catégorie « Peinture et dessin » (`styles-peinture-dessin`, source lemo-opuscar) : là-bas, pas de main, des feutres qui flottent, jusqu'à trois couleurs de feutre qui ont chacune un sens, un tableau brillant. Ici : **une main visible**, noir et **un seul** accent, écriture calée un peu après la voix, recul final obligatoire. Choisir celui-ci quand on veut la présence d'une personne qui dessine.

## 2. Palette, typographie, matières

| Rôle | Grand tableau | Feuille par feuille |
|---|---|---|
| Fond | blanc `#FBFBFB` | papier beige rosé `#E7DBE1` |
| Trait | noir `#0A0503` | noir |
| **Un seul accent** | orange : texte `#EB701F`, aplat `#F3742D`, surface hachurée claire `#E9A67C` | crayons pâles : jaune `#EDE6A2`, bleu `#B5CBE8` |

- **L'accent couvre environ 22 % de l'encre**, seulement sur les mots clés et les remplissages en hachures.
- **Trait** : 0,6 à 0,7 % de la hauteur, soit **11 à 13 px en 1080×1920** (7 px en 1080 de haut) ; hachures d'ombre deux fois plus fines ; feuille par feuille : 0,8 %.
- **Lettrage** : capitales d'imprimerie tracées à la main, comme dans une bulle de bande dessinée. Polices libres : Patrick Hand, Architects Daughter ou Kalam. Hauteur d'un titre : environ 5,5 % de la hauteur du cadre.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Patrick Hand et d'Architects Daughter et de Kalam. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/patrick-hand`, `@fontsource/architects-daughter`, `@fontsource/kalam` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Types de traits, fixés dès le premier** : **plein = c'est arrivé ; tirets = c'est prévu ; pointillés = un lien qui saute d'une partie à l'autre**.
- **Ce qui est sur le tableau ne peut qu'être effacé ou rester** : jamais de fondu.
- **La main** : une vraie main droite qui tient un marqueur noir, entre par **le bas à droite**, avant-bras en biais ; elle masque 15 à 25 % de l'image ; quand elle ne dessine pas, elle sort du cadre. Elle est à l'écran 40 à 50 % du temps. Utiliser une photo détourée ou un dessin soigné de main (skill `personnages` ou image fournie) ; une main dessinée grossièrement en code gâche tout.
- **Matières** : le tableau est propre ; pas de grain qui bouge.

## 3. Composition 9:16

- **On planifie d'abord l'image finale entière, puis on la dessine « à rebours »** : en vertical, le tableau est une **longue bande qui descend** (ou un grand plan qu'on parcourt en serpentin), pas un rouleau horizontal.
- Chaque cadre contient **3 à 6 groupes** texte-image ; on le remplit, puis on s'en va.
- Un déplacement lisse ne décale que de **0,23 largeur de cadre** : l'ancien et le nouveau se recouvrent à environ 75 %, le spectateur voit toujours le bord du groupe précédent.
- **Le cadrage se calcule à partir de la boîte qui entoure les traits du passage** (on encadre, on laisse une marge) : jamais de coordonnées tapées à la main. Un ancien mot coupé en deux par le bord du cadre est poussé hors champ.
- **Dessiner beaucoup, écrire peu** : pour chaque groupe, décider **d'abord l'objet ou le gag à dessiner**, ensuite le mot. Une phrase manuscrite ne dépasse pas une ligne. Test : si plus de la moitié des mots écrits sont les mots que la voix dit au même instant, on écrit trop.
- **Alterner les gabarits** : le même schéma (« année, objet, étiquette orange ») pas plus de 3 fois ; passer à une comparaison (deux dessins côte à côte), un déroulé (des flèches), un détail agrandi, un grand dessin.
- **Tailles** : titre 100 à 110 px ; mots 60 à 80 px ; rien sous 44 px. Zone utile : x 60 à 945, y 160 à 1560 ; la main entre par le bas à droite, donc **placer le texte important à gauche et en haut du cadre**.
- Vérifier chaque dessin : un objet haut, arrondi au sommet et évasé à la base peut se lire comme une forme déplacée ; le rendre pointu ou à fond plat.

## 4. Ce qui bouge

- **Action principale** : la main trace, et **la pointe du marqueur mène le trait**.
- **Boucles de fond** : (1) la main ne s'arrête pas : même quand la voix marque une pause, elle hachure, souligne, ajoute un détail ; (2) entre deux traits proches, la pointe glisse en arc de la fin de l'un au début de l'autre.
- **Autorisés** : tracé de ligne `#004`, machine à écrire `#006` version manuscrite, apparition éclair `#001` avec dépassement `#010` pour quelques mots clés orange **sans la main** (0,3 s), panoramique `#025` lissé, panoramique filé `#043` avec flou de mouvement pour sauter loin sur le tableau, travelling de suivi `#029`, zoom arrière `#028` final, plan-séquence `#172`, plan d'ensemble `#183`.
- **Interdits** : fondu `#044`, tourné de page `#140`, zoom dans une bulle ou un cadre (absent des originaux), trait qui apparaît d'un coup sans pointe, couleur en plus de l'accent, ombres portées, caméra qui flotte.
- **Vitesses mesurées** : écriture d'environ **16 caractères par seconde** (la vitesse de la parole : comme des sous-titres écrits à la main) ; **le titre deux fois plus lentement** (7,5 caractères par seconde) pour poser le sujet ; un petit pictogramme en 0,5 à 1 s ; un visage en 2 s environ.
- **Un dessin complexe ne se trace pas devant la caméra** : il est déjà là quand la caméra arrive, ou il entre en coupe sèche et la main n'ajoute que la couleur.
- Chaque trait : départ et arrivée ralentis. Écart de moins de 0,25 s entre deux traits : la pointe glisse (en se levant de 30 px). Écart plus long : la main sort par le bas à droite (0,35 s) et revient 0,3 s avant le trait suivant.

## 5. Rythme et montage

- **Durée par cadre** : environ 6,6 s entre deux mouvements de caméra (de 4 à 14 s).
- **Calage sur la voix (le cœur du style)** : on commence à écrire **0,2 à 0,8 s après** le début des mots correspondants, et on finit moins d'une seconde après la fin de la phrase : on écrit en parlant, **un peu en retard, jamais en avance**. Exception : un élément de décor (un flacon, une flèche) peut être dessiné quelques secondes avant que la voix y arrive.
- **Un nouveau cadre = un nouvel argument** : les transitions suivent les idées, pas les silences.
- **Transitions** : (1) **déplacement lisse ou léger zoom** sur le tableau, 1,2 à 2,4 s, accélération et décélération en sinus ; l'idéal : la main trace un trait orange vers la zone suivante et **entraîne la caméra** ; (2) **filé**, environ 0,8 s, pour sauter de 0,5 à 1,2 largeur ; (3) **recul final** : un voile gris très clair, un recul rapide (0,6 s), un long balayage de tout le tableau ; (4) nuage de fumée dessiné qui couvre puis se dissipe (rare) ; (5) coupe sèche vers un dessin déjà fait.
- **Musique** : dans la grammaire « grand tableau », il n'y a **pas de musique** sous la voix ; dans « feuille par feuille », une musique discrète, nettement sous la voix.
- **Version courte (8 à 12 s)** : un seul cadre : un dessin déjà présent, deux mots tracés par la main, un seul déplacement de caméra ; couper les autres cadres. Accroche : la main trace dès la première seconde.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D avec `dessiner(t)` ; ou SVG avec tracés animés par `stroke-dasharray`.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `tableau.js` (tous les traits du tableau final, en coordonnées du monde, groupés par passage, avec leur type de trait), `main.js` (image de la main, ancrée à la pointe), `camera.js` (cadrage calculé sur les boîtes), `film.js` (minutage par phrase).

```js
// durée d'un trait = longueur ÷ vitesse de la pointe ; au moins 0,04 s ; 0,02 s entre deux traits
const duree = trait => Math.max(0.04, longueur(trait) / VITESSE);            // VITESSE ≈ 1300 px du monde par seconde
// cadrage : encadrer la boîte des traits du passage, avec une marge
const cadre = passage => ajuster(boiteEnglobante(passage.traits), { marge: 0.12, format: 9 / 16 });
// révéler un dessin prêt ou un mot : la pointe balaie la zone en zigzag et découvre ce qu'elle a parcouru
function reveler(ctx, zone, p, lignes = 8) { ctx.save(); ctx.clip(masqueZigzag(zone, p, lignes)); dessinerLignes(zone); ctx.restore(); placerMain(pointeZigzag(zone, p, lignes)); }
```

- **Techniques clés** : pour un mot dont on n'a pas l'ordre des traits, un balayage en zigzag de 3 lignes sur chaque lettre, la pointe suivant le va-et-vient, se lit comme une écriture ; flou de mouvement seulement pendant un filé (plusieurs images superposées dans le sens de la vitesse) ; déplacement lisse et recul restent nets.
- **Pièges** : tracer plusieurs parties à la fois pendant que la pointe se promène ailleurs (« la pointe ne mène pas le trait ») ; une vitesse de trait de démonstration (deux fois le réel) dans un vrai film : **ralentir** ; un mot ancien coupé au bord du cadre ; trop de texte recopié de la voix.

## 7. Son

- **Bruitages** : le **frottement du marqueur** sur le tableau est le son du style : un enregistrement réel, découpé sur la durée de chaque trait ou groupe de traits (un son par groupe, pas par trait), plus un capuchon, un coup de chiffon pour un effacement, un « pop » sur un mot clé qui surgit, un souffle sur un filé.
- **Musique** : aucune sous la voix (grand tableau), ou très discrète (feuille par feuille). Une courte phrase musicale peut accompagner le recul final.
- **Silence** : quand la voix se tait, on n'entend que le marqueur.
- **Voix** : c'est un orateur : débit régulier, ton de conversation.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Fond blanc, trait noir, **un seul** accent, qui couvre environ un cinquième de l'encre.
- [ ] La pointe du marqueur est toujours à l'extrémité du trait en train d'apparaître.
- [ ] On dessine plus qu'on n'écrit : chaque groupe a un objet ou un gag ; aucune phrase manuscrite de plus d'une ligne.
- [ ] L'écriture commence un peu après les mots de la voix, jamais avant.
- [ ] La main est à l'écran 40 à 50 % du temps et ne couvre jamais le mot qu'on doit lire.
- [ ] Le même gabarit de groupe ne revient pas plus de 3 fois.
- [ ] Le film se termine par un recul qui montre tout le tableau.
- [ ] Rien n'apparaît ni ne disparaît en fondu ; rien sous 44 px.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 8
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 44

## 9. Aperçu

- Planche de la démo d'origine (une image par plan, 16:9) : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/y3_whiteboard_总览.jpg
- Crédit : 花叔 Huashu (alchaincyf), https://github.com/alchaincyf/huashu-art-motion. La démo contient le personnage de son auteur (exclu de la licence) : planche donnée en lien seulement, personnage non repris.

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichiers `references/动画语法/y3_whiteboard.md`, `scripts/engine/demos/y3_whiteboard/`, `scripts/engine/lib/diagram.js`, `camera.js`.
- Licence : MIT (© 2026 alchaincyf, 花叔), hors personnage de l'auteur.
- Adaptation Flot Web : traduction du chinois, tableau en bande verticale, épaisseurs et tailles recalculées, polices manuscrites libres pour l'alphabet latin, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
