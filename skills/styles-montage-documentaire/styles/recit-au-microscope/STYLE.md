# Récit au microscope

## 1. Identité
- **Nom** : Récit au microscope. Identifiant : `recit-au-microscope`.
- **Inspiration** : les films de changement d'échelle continu avec un relevé qui accompagne ; les films de lancement de microscopes haut de gamme (paillasse sombre, verre qui accroche la lumière, marques retenues, sons d'instrument nets) ; les instruments des visionneuses de lames numériques (barre d'échelle, champ, grossissement). Grammaire seulement, aucun nom cité.
- **Principe** : de vraies images de microscopie, de licence claire, d'un vrai échantillon, vu tel qu'il est, et **un seul changement d'échelle continu** qui emmène de la lame de verre tenue en main jusqu'à une seule cellule. La mise au point respire à chaque changement de grossissement, un plan focal balaie le cadre quand la caméra se pose, et chaque barre d'échelle, champ et relevé vient des métadonnées de l'image.
- **Cinq règles** : l'échantillon est une photographie (rien n'y est dessiné, retouché ou généré) ; l'échelle est la caméra (une plongée en échelle logarithmique à travers des plaques emboîtées du même échantillon) ; la mise au point a une grammaire ; les relevés sont mesurés (taille du pixel × pixels) et l'écran dit comment ; un relevé par écran, en couleur d'accent. **On décrit ce qui est mesuré, on ne pose jamais de diagnostic.**
- **Pour quels sujets** : vulgarisation en biologie, matériau vu de près (revêtement, céramique, fibre, cheveu, peau), contrôle qualité d'un laboratoire ou d'une marque, « traité contre non traité ».
- **Ne marche pas pour** : un sujet sans image de microscopie libre (la plupart sont sous licence non commerciale), un conseil médical, deux images de sources différentes qu'on voudrait enchaîner dans un même zoom. Ce n'est pas le briefing satellite (pas d'étalonnage gris : la coloration garde sa couleur), ni un affichage de science-fiction.

## 2. Palette, typographie, matières
- **Verre** : blanc papier chaud `#F4F1EC`. **Paillasse** : graphite `#0B0D0F` → `#2A3036` sous une lente flaque de lumière ; ombre douce sous la lame.
- **La coloration est une preuve** et garde sa vraie couleur (rouge et bleu d'un trichrome, rose et violet d'une coloration classique). Un seul étalonnage pour toutes les plaques : verre ramené à un blanc chaud, un peu de densité, rien d'autre. Pas de fausses couleurs, pas d'émulation de pellicule.
- **Un accent**, froid et éloigné des teintes de la coloration (menthe contre rouge et bleu ; ambre contre vert ou violet), réservé au relevé mesuré et aux pixels comptés. Exemple : menthe `rgb(120,240,205)` sur la coloration, `rgb(0,122,99)` sur le verre.
- **Panneaux dépolis** (verre sombre translucide `rgba(12,14,17,0.74)` sur une copie floutée de l'image) pour relevés, instruments, sous-titres et crédit : le texte blanc se lit sur le verre comme sur la coloration, rien ne change de couleur en cours de plan.
- **Polices libres** : relevés et barre d'échelle en grotesque condensée légère (Barlow Condensed) ; instruments et comptes de pixels en IBM Plex Mono ; libellés en sans ; serif pour le titre seulement.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Oswald à la place de Barlow Condensed ; IBM Plex Mono : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/barlow-condensed` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Marques** : traits fins de 1,5 à 2,5 px avec halo, cercles tracés en arc avec repères cardinaux, cotes avec butées, traits de rappel à un coude.

## 3. Composition 9:16
- **Échantillon plein cadre.** Aux moments clés, la structure mesurée occupe un tiers de la hauteur ou plus, centrée entre y 450 et y 1100.
- **Instruments** dans un seul panneau dépoli, en haut à gauche sous y 170 : barre d'échelle avec sa valeur, champ, grossissement avec un petit pictogramme de tourelle qui tourne d'un quart à chaque changement (28 px minimum). La barre d'échelle raccourcit puis saute selon la suite 1-2-5.
- **Crédit de la source** : petit panneau dépoli en bas à gauche, au-dessus de y 1550 (28 px minimum).
- **Relevé** : panneau dépoli à côté de ce qu'il mesure, relié par un trait : petit libellé au-dessus (« part de collagène dans la surface du tissu », 30 px), le nombre en grand dans l'accent (90 à 120 px), la méthode ou les comptes bruts dessous (28 px). À gauche de x 945.
- **Annonce du grossissement** : dite une fois, en grand (140 px), au centre, au moment du changement.
- **Sous-titres** : bande dépolie y 1400 à y 1530.
- Zones d'interface : haut 160, bas 360, droite 135.
- **16:9** : instruments dans un coin, crédit dans le coin opposé, sous-titres en bas au centre.

## 4. Ce qui bouge
- **Action principale** : la plongée. La caméra est une similitude (zoom, rotation, position) interpolée en **spirale logarithmique** entre les clés : chaque poussée est une vraie plongée vers un point, et la rotation en fait partie. Les changements de grossissement arrivent là où les plaques changent réellement.
- **Boucles de fond** : (1) dérive de 2 à 5 % pendant les tenues, jamais d'image figée plus d'1 s ; (2) la respiration de la mise au point.
- **Grammaire de la mise au point** : entrée floue qui devient nette au début ; une courte respiration (flou + soupçon de changement de champ) à chaque changement de grossissement, avec clic de tourelle ; un **balayage du plan focal** (front net incliné qui traverse un cadre adouci) quand la caméra se pose.
- **Les marques arrivent en se faisant** : une cote pousse depuis son centre, un cercle se trace en arc, un front de balayage compte les pixels pendant que le relevé roule, le relevé se pose avec un petit ressort.
- **Gestes** : **compter la couleur** (tracer un cercle, le traverser d'un front, allumer chaque pixel compté, faire monter la part jusqu'à sa valeur, montrer les comptes bruts dessous ; les pixels comptés restent en trace légère) ; deux cercles, un verdict (mesurer un endroit, glisser vers un autre à la même échelle, puis cadrer les deux et dire ce qui diffère) ; le balayage focal et l'anneau (entourer une structure et donner sa taille) ; la remontée (retour à l'échelle de l'œil, barre d'échelle qui saute à l'envers, carton titre écrit sur le verre).
- **Autorisés** : #028 zoom continu, #033 bascule de mise au point, #029 glissé latéral à grossissement constant, #004 tracé, #007 compteur, #010 petit ressort d'arrivée, #163 points d'intérêt, #172 plan-séquence.
- **Interdits** : coupes et #044 fondus entre deux échantillons, échantillon qui bouge sous ses marques, instruments qui changent de place, viseurs et fils de fer lumineux, #111 aberration chromatique décorative.

## 5. Rythme et montage
- Une seule prise : plongée → (arrêt, mesure) × 2 ou 3 → verdict → remontée.
- Transitions = changements d'échelle, glissés et mise au point.
- Silence avant le verdict et avant la remontée ; le premier son après est le relevé ou le retournement.
- Libellé tenu (lettres ÷ 15 + 1,5) s ; un relevé qui roule est compté à sa valeur d'arrivée ; sous-titre ≥ max(1,8 s ; parole + 0,6 s).
- **Version courte (8 à 12 s)** : une seule plongée (deux échelles, et non quatre) et un relevé tenu.

## 6. Recette technique
- **Moteur** : HyperFrames. Les niveaux de la pyramide d'image sont des `<img>` dans un seul repère « monde » (pixels du niveau le plus fin) ; un `<canvas>` ou des transformations CSS les dessinent depuis `hf-seek` ; marques en SVG par la même fonction monde → écran ; panneaux dépolis en HTML.
```js
// choix de la plaque : la plus fine qui n'est pas réduite de plus de ~1,45× ; fondu avec la suivante entre 2,2× et 1,45×
function plaques(zoom) {
  const i = niveaux.findIndex(n => n.pxParUnite * zoom <= 1.45);
  return { fine: niveaux[i], melange: clamp((2.2 - ratio(i - 1, zoom)) / (2.2 - 1.45), 0, 1) };
}
// caméra : interpolation log entre deux clés {zoom, angle, cx, cy} autour de leur point fixe commun
const z = Math.exp(lerp(Math.log(a.zoom), Math.log(b.zoom), ease(u)));
```
- **Source idéale** : une image de lame entière (un échantillon, une pyramide déjà recalée du millimètre au micron, la taille du pixel dans ses métadonnées). **Deux échantillons différents ne se zooment jamais l'un dans l'autre** : deux images « de la même chose » à deux échelles sont deux spécimens. S'il faut joindre deux sources, couper sur une respiration de mise au point et le dire.
- **Plaque « à l'œil nu »** : la photo de la lame entière, recalée sur le balayage ; effacer le logo imprimé du fabricant en le comblant de verre dépoli (codes-barres et identifiants font partie de l'objet, pas les logos).
- **Flou de mise au point** : flou gaussien sur une image rendue avec une marge (sinon les bords s'assombrissent).
- **Taille du pixel** : la lire dans le fichier ; **finir la plongée à la résolution réelle du balayage** (au-delà de ~1,6× d'agrandissement, c'est de la bouillie).
- **Où trouver** : jeux de lames entières en CC0, micrographies du domaine public d'organismes publics, collections en CC BY (bibliothèques d'images cellulaires, collections de musées de médecine), Wikimedia Commons filtré par licence. Pour un produit, un laboratoire ou une marque : demander d'abord au client ses propres images (avec leur échelle). Inutilisable : licences non commerciales, figures de revues, images générées.
- **Pièges** : raccords de tuiles du scanner (les cadrer dehors) ; couleur de coloration surinterprétée (elle veut dire ce que dit le protocole, rien de plus) ; part mesurée présentée comme un score clinique (elle vaut pour la zone tracée et le seuil annoncé).

## 7. Son
- **Bruitages d'instrument** (budget du skill `son`) : tourelle d'objectif (clic, cran, petit tintement de métal), servo de mise au point, plume sur verre pour chaque ligne tracée, balayage filtré de gauche à droite avec tics de compteur qui accélèrent, souffle doux pour le plan focal.
- **Musique** : vibraphone en croches et doubles croches, tics de marimba, vibraphone frotté et verres d'eau pour les nappes, glockenspiel à chaque relevé qui se pose ; harmonie ouverte et légère.
- **Lit** : pièce de laboratoire calme (ventilation, léger ronflement).
- Voix calme et exacte, ≈ 10 dB au-dessus de la musique ; nombres en lettres pour la voix, en chiffres à l'écran ; −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] L'échantillon est une vraie image, sous CC0, domaine public ou CC BY, listée dans `CREDITS` ; rien n'y est retouché ni généré.
- [ ] Une seule pyramide du même échantillon pour toute la plongée (ou une jointure annoncée).
- [ ] Barre d'échelle, champ et relevés calculés depuis la taille de pixel du fichier ; la méthode est écrite à l'écran et dans `FAITS.md`.
- [ ] Aucun mot de diagnostic ; on décrit ce qui est mesuré.
- [ ] Un seul relevé en couleur d'accent par écran ; l'accent ne ressemble à aucune teinte de la coloration.
- [ ] Une respiration de mise au point à chaque changement de grossissement ; aucun agrandissement au-delà de la résolution réelle.
- [ ] Aucun logo de fabricant visible sur la lame.
- [ ] Rien sous 28 px en 9:16 ; zones d'interface respectées.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Film de démo d'origine : https://lemomo-ai.github.io/lemo-opuscar/films/microscope.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/microscope.jpg
- Crédit : « Measured Blue », LemoLab, CC BY 4.0 ; image de lame de tiers sous sa propre licence : **lien seulement**. Démo en 16:9.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/microscope/STYLE.md`, `style.json`, `demo/film.js` (`camAt`, `panel()`), `demo/tools/` (`plates.py`, `nucleus.py`).
- Licence : MIT (© 2026 LemoLab) ; film de démo CC BY 4.0.
- Adaptations Flot Web : français, mise en page 9:16, HyperFrames.
