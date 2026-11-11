# Science à plat (style Kurzgesagt)

## 1. Identité

- **Nom** : Science à plat. « Style Kurzgesagt » désigne une inspiration (la vulgarisation scientifique en aplats lumineux et arrondis) ; ce n'est ni un contenu officiel, ni une affiliation.
- **La règle en une phrase** : on dessine **une idée abstraite comme un objet concret**, on le place dans un monde lumineux où l'on peut **zoomer à l'infini**, et la caméra voyage entre les échelles ; la couche d'ambiance (étoiles, particules) peut bouger doucement en continu ; **le sujet et l'information changent aux moments où la voix le dit, puis s'arrêtent**.
- **Marche pour** : parler d'échelle et de « ce qu'il y a dedans » (de la cellule à la galaxie, d'un pixel à un modèle) ; expliquer un mécanisme ou un système en rendant visible l'invisible par des particules et des liaisons lumineuses ; un ton « sérieux mais mignon », sur une voix posée (environ deux phrases par plan).
- **Ne marche pas pour** : de vraies personnes, de vrais événements, des preuves d'archives (le dessin plat affaiblit la crédibilité : voir `collage-enquete`) ; des étapes de raisonnement (voir `tableau-blanc-a-la-main`) ; **un petit budget de temps** : la qualité de ce style tient au fait que « quelque chose bouge dans chaque image » ; fait à l'économie, il ressemble à un diaporama bon marché.
- **Avant tout, écrire la métaphore visuelle** de chaque passage : l'idée abstraite devient **quel objet** (une cellule, un engrenage, un tuyau, une ville, une goutte) ? Si l'on ne peut pas l'écrire, on n'a pas de plan : pas question de poser une boule lumineuse avec trois étiquettes.
- On ne reprend pas les personnages-signatures de la chaîne d'origine (ses oiseaux en forme d'œuf) : on dessine les siens (skill `personnages`).

## 2. Palette, typographie, matières

- **Choisir une ambiance et s'y tenir par partie** : sombre (plus de 60 % de pixels sombres, couleurs très saturées) ou claire (fond gris-blanc, peu saturé). On peut changer **tout le jeu de couleurs** en changeant de partie, jamais au milieu.
- **Règle** : **un fond sombre + 2 ou 3 accents très saturés, qui s'opposent** (orange contre bleu, cyan contre magenta).

| Rôle | Jeu conseillé (aplats sombres, sans violet) |
|---|---|
| Fond | encre `#0c1016` ou bleu marine en aplat `#0f2136` |
| Second plan | `#16324f`, `#1f4a6e` |
| Accent cyan | `#32BAEE`, `#7DD3DC` |
| Accent orangé (corps lumineux) | `#F48301`, `#E07919`, `#FACC12` ; cœur de la lueur `#F9EF93` |
| Accent magenta (petites touches) | `#BE3A95` |
| Reflets et texte blanc | `#E7DFE1`, `#F9FCFB` |

- **Attention** : les originaux récents utilisent un fond violet profond en dégradé (`#05020F`, `#0E0631`, `#25155E`). **Ne pas le recopier** : c'est aujourd'hui la marque la plus visible des vidéos faites par une machine, et la règle commune du plugin limite à 30 % les images dominées par le bleu-violet. Garder la règle (fond sombre + accents), changer le fond.
- **Formes** : **aucun contour**. L'ombre est un aplat de la même teinte un cran plus sombre ; le reflet est une ellipse blanche ou un arc. **Des coins arrondis partout** : les êtres vivants sont des masses organiques, les têtes sont rondes, les membres sont des tubes à bouts ronds.
- **Deux tons par forme** : dans chaque forme, une bande d'ombre en bas à droite (décalage d'environ 10 à 12 px) et un fin liseré de lumière en haut à gauche (4 à 5 px). Les personnages passent par le même traitement que le décor : ils ne paraissent pas collés.
- **Tout corps lumineux a un halo radial** : c'est la raison d'être du fond sombre.
- **Étiquettes** : pilules à grand rayon, couleur pleine et saturée, texte gras sans empattement.
- **Polices** (libres) : Nunito, Poppins ou Baloo 2 : rondes et grasses.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Baloo 2 ; Nunito, Poppins : déjà fournies. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/baloo-2` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Personnages** : corps simple (goutte, œuf, boîte arrondie), **grands yeux blancs**, petite pupille noire ; clignement de 5 images pour fermer, 10 pour rouvrir, à intervalles irréguliers ; **l'œil ne se réduit jamais à zéro**.

## 3. Composition 9:16

- **Le sujet est au centre, un peu bas** (sur le tiers inférieur : y 900 à 1250) ; **au-dessus, le ciel** laisse la place aux étoiles et aux annotations. Le vertical convient très bien à ce cadrage.
- **5 à 6 couches de parallaxe** : ciel étoilé (profondeur 0,05), astre lointain (0,12), reliefs lointains (0,3), pente proche (0,65), sujet (1,0), feuillage de premier plan (1,5, **flou et sombre**).
- **Annotation** : un fin trait de rappel blanc se trace, puis le texte s'écrit caractère par caractère (environ 40 caractères par seconde) ; **une annotation par phrase de la voix** ; elle reste environ 3 s puis s'efface caractère par caractère.
- **Tailles** : titre de chapitre plein écran 90 à 120 px, mot par mot, fond flouté ; étiquettes en pilule 40 à 48 px ; annotations 36 à 44 px.
- **Structure type « ce qu'il y a dedans »** : un objet central et ses satellites. Elle convient aux explications en couches ; si le sujet n'a pas cette forme, composer ses propres plans plutôt que de le forcer.
- Zone utile : x 60 à 945, y 160 à 1560. Annotations à gauche de x 945.

## 4. Ce qui bouge

- **Action principale** : **au moins un changement d'état par phrase de la voix** : une étiquette surgit, une forme se transforme, la caméra plonge ou recule. Compter phrase par phrase : deux phrases de suite sans changement, on ajoute un événement (pas un flottement ni une poussée lente).
- **Boucles de fond** (la couche d'ambiance, autorisée à bouger en continu) : (1) les étoiles qui scintillent chacune à sa phase, les particules qui dérivent ; (2) la vie du décor : herbes qui balancent, impulsions qui courent le long des liaisons, halo qui respire. **Le sujet et les étiquettes, une fois posés, ne flottent pas et ne respirent pas.**
- **Autorisés** : apparition éclair `#001` avec dépassement `#010` (une carte atteint 90 % en 0,25 s, dépasse à 108 %, revient à 100 % vers 0,5 s), décalage en cascade `#002` (éléments d'un même groupe : 10 à 20 images d'écart à 60 images par seconde, soit 0,17 à 0,33 s ; membres d'un corps : 0,05 à 0,07 s), morphing de forme `#012`, mouvement liquide `#013`, particules `#015`, parallaxe `#016`, zoom à travers `#020`, zoom `#028` (interpolé en logarithme), travelling avant `#027`, tracé de ligne `#004`, machine à écrire `#006` pour les annotations, répéteur `#134` (se multiplier jusqu'à remplir l'écran), flottement `#096` **pour l'ambiance seulement**, reflet de lumière `#022`.
- **Interdits** : contours noirs, mouvement linéaire, sujet qui flotte ou « respire » pour meubler, poussée lente et continue, coupes sèches en rafale, textures photo, fond en dégradé bleu-violet.
- **Courbes d'origine** : mouvement courant d'environ 0,83 s ; plus vif : 0,5 s, 0,33 s, 0,17 s ; surgissement : 0,08 à 0,17 s. Courbe type : `cubic-bezier(.75,0,.25,1)` (départ très doux, milieu rapide, fin très douce) ; pour les boucles : `cubic-bezier(.333,0,.667,1)`. Une pause d'environ 0,33 s entre deux actions.
- **Caméra** : arrêt, poussée lente d'environ 0,9 s vers ce dont on parle, arrêt ; 0,7 s pour passer à un autre élément ; poussée rapide (0,28 s) ou chute (0,17 s) seulement pour une révélation. Après une plongée, **on rend l'échelle par un recul**.
- **Avant de plonger dans un objet, s'arrêter** : l'objet reste immobile 0,3 s au moins et **s'illumine**, pour que le spectateur sache où l'on entre.

## 5. Rythme et montage

- **Un plan : 7 à 9 s**, mais **« l'unité visuelle » change toutes les 4,6 à 6,7 s**, par une transition dessinée.
- **Peu de coupes sèches** (environ 5 par minute), placées 0 à 0,2 s avant le début d'une phrase. Les autres changements sont des transitions dessinées de 0,3 à 0,6 s.
- **Transitions** : (1) **la traversée d'échelle** : la caméra fonce dans un objet jusqu'à ce que sa couleur remplisse l'écran, puis la nouvelle scène apparaît (environ 1,4 s ; accélérer puis ralentir ; ne pas démarrer avec une courbe trop brutale, qui avale la moitié de l'échelle dès la première image) ; (2) **entrer dans l'objet** : la scène suivante n'est visible que dans un cercle qui grandit avec la poussée, bordé d'un anneau lumineux (environ 1 s) ; (3) **recul rapide qui révèle** (0,2 à 2 s, départ vif, longue fin), pour relier le microscopique au gigantesque ; (4) une lumière de la scène qui remplit l'écran (0,5 s) ; (5) un objet ou une bande de lumière qui balaie l'image en biais (0,4 s) ; (6) **se multiplier jusqu'à remplir l'écran**, pour « il y en a tellement que… » (3 à 6 s).
- La musique se compose après le montage de l'image, calé sur la voix.
- **Version courte (8 à 12 s)** : un plan de 8 à 10 s fait de deux unités visuelles reliées par une transition dessinée (0,5 s) ; couper la traversée d'échelle (1,4 s). Accroche : une étiquette surgit avant 2 s.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D avec `dessiner(t)` (couches, parallaxe, halos) ; SVG possible pour un plan simple. Pour une vraie profondeur avec flou de premier plan, les couches peuvent aussi être assemblées dans `blender`, mais ce n'est pas nécessaire.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `palette.js`, `formes.js` (aplat à deux tons, halo, pilule, trait de rappel), `monde.js` (couches et profondeurs), `camera.js` (zoom en logarithme), `ambiance.js` (étoiles, particules à graine), `film.js`.

```js
// aplat à deux tons, sans contour : une bande d'ombre en bas à droite, un liseré de lumière en haut à gauche
function aplat(ctx, forme, couleur, ombre, lumiere, v = { x: 10, y: 12 }, w = { x: 4, y: 5 }) {
  ctx.save(); ctx.clip(forme);
  ctx.fillStyle = ombre;   ctx.fill(forme);
  ctx.fillStyle = couleur; ctx.translate(-v.x, -v.y); ctx.fill(forme); ctx.translate(v.x, v.y);
  ctx.globalCompositeOperation = "source-atop"; ctx.fillStyle = lumiere; liserer(ctx, forme, w);
  ctx.restore();
}
const zoomLog = (z0, z1, p) => z0 * Math.pow(z1 / z0, p);                    // vitesse perçue constante
const parallaxe = (x, profondeur, camX) => x - camX * profondeur;            // 0,05 ciel … 1,5 premier plan
const etoile = (i, t) => 0.5 + 0.5 * Math.sin(t * (1 + 2.5 * hasard(i)) + 6.28 * hasard(i + 99));   // scintillement à graine
```

- **Techniques clés** : pour une traversée, faire coïncider un reflet des deux côtés (même coin, même forme) pour que la jointure ne se voie pas ; premier plan flouté d'environ 7 px.
- **Pièges** : une boule lumineuse et trois étiquettes à la place d'une métaphore ; des personnages dessinés autrement que le décor ; une traversée lancée avec une courbe trop brutale ; un fond violet « par défaut » ; un sujet qui flotte ; un œil qui disparaît au clignement.

## 7. Son

- **Musique** : électronique douce et mélodique, nappes chaleureuses, arpèges, petites percussions ; composée (ou choisie) **après** le montage.
- **Bruitages** : des sons ronds et doux, accordés à la musique : « pop » d'une étiquette, bulle, souffle long d'une traversée d'échelle, scintillement d'un corps lumineux, petite voix ou piaillement pour un personnage. Environ 5 pour 10 s.
- **Ambiance** : un fond spatial ou organique très léger qui change avec l'échelle.
- **Silence** : une courte suspension juste avant une plongée.
- **Voix** : posée, bienveillante, un peu d'humour ; c'est elle qui fixe le minutage.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Chaque passage a une métaphore écrite : l'idée est un objet concret.
- [ ] Aucun contour : ombres en aplat de la même teinte, reflets blancs, coins arrondis.
- [ ] Un fond sombre uni (pas de dégradé bleu-violet) et 2 ou 3 accents saturés qui s'opposent.
- [ ] Au moins un changement d'état par phrase de la voix.
- [ ] L'ambiance bouge ; le sujet et les étiquettes, une fois posés, ne bougent plus.
- [ ] Avant une plongée, l'objet visé s'arrête et s'illumine ; le zoom est interpolé en logarithme.
- [ ] Les personnages ont le même traitement à deux tons que le décor.
- [ ] Une annotation par phrase, visible environ 3 s, dans la zone utile.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 16
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 36

## 9. Aperçu

- Planche de la démo d'origine (une image par plan, 16:9) : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/y1_kurzgesagt_总览.jpg
- Crédit : 花叔 Huashu (alchaincyf), https://github.com/alchaincyf/huashu-art-motion. La démo contient le personnage de son auteur (exclu de la licence) et un fond violet déconseillé : lien seulement.

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichiers `references/动画语法/y1_kurzgesagt.md`, `references/色板.md`, `scripts/engine/demos/y1_kurzgesagt/`, `scripts/engine/lib/toon.js`, `camera.js`. Licence MIT (© 2026 alchaincyf, 花叔), hors personnage de l'auteur.
- Adaptation Flot Web : traduction du chinois, jeu de couleurs sans violet (les codes du fond et du second plan sont des exemples), composition verticale, durées converties en secondes, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
