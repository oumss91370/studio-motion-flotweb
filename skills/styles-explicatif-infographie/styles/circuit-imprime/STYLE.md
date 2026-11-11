# Circuit imprimé

## 1. Identité

- **Nom** : Circuit imprimé (le sujet dessiné comme une carte électronique vue du dessus).
- **Inspiration** : les vrais fichiers de conception et plans de montage de cartes électroniques (couches, isolements, repères, encadrés de détail), la macrophotographie de cartes (faible profondeur de champ, reflet de l'or, lumière douce), les schémas électriques (un symbole = une fonction). On dessine ses propres cartes : jamais la copie d'un vrai tracé, d'un logo ni d'un marquage de composant.
- **Ce qui le fait reconnaître** : **une carte vue de dessus dans chaque image** : le monde est du **cuivre sous un vernis vert**, les trajets sont des **pistes** (segments à 0°, 45° ou 90°), les lieux sont des **pastilles dorées**, les mots sont de la **sérigraphie blanche**, et **ce qui circule (énergie, eau, signaux, marchandises) est de la lumière qui court sur le cuivre**. Rien n'est en perspective.
- **Deux échelles sur une même carte** : des régions entières (une carte, une chaîne logistique, une ville) sont dessinées dans le même langage que des composants isolés, et la caméra passe de l'une à l'autre sans changer de médium.
- **Seules les choses réelles sont dessinées** : chaque piste, pastille et étiquette représente quelque chose du sujet.
- **Marche pour** : énergie, réseaux, chaînes d'approvisionnement, trajet d'un signal ou d'un paiement, fonctionnement d'un appareil, « ce qui se passe en sept millisecondes ».
- **Ne marche pas pour** : un sujet sans flux, un sujet humain ou sensible, un récit avec des personnages. Ce n'est pas un `plan-bleu` (ni papier ni trait blanc sur bleu), ni un `hologramme-hud` (ni verre ni panneaux flottants), ni une « ville-circuit » en 3D.

## 2. Palette, typographie, matières

| Rôle | Couleur (exemple de la source) |
|---|---|
| Stratifié (fond vert sombre) | `#05190F` |
| Plan de cuivre sous vernis | `#1C6A44` |
| Liseré / piste | `#4AA977` |
| Or (pastilles, traversées) | `#D9B25B` |
| Sérigraphie | `#F2EEE1` |
| **Lumière du courant** (ambre, cœur presque blanc) | rvb (255, 190, 84) |
| **Lumière du second flux** (argent-cyan : eau, données, marchandises) | rvb (170, 214, 226) |
| Défaut | rouge, une fois au plus |

- **Le film est vert** : on ne recolore jamais le vernis d'une scène à l'autre.
- **La lumière porte le sens et c'est la seule couleur saturée.** Un troisième flux n'a sa couleur que s'il faut vraiment le distinguer.
- Le sombre (stratifié nu, mer, trous) est ce qui est absent.

**Couches, du bas vers le haut :**
1. **Stratifié** : vert sombre, texture de tissage de verre.
2. **Plan de cuivre** : il remplit la carte ; tout est un **isolement** découpé dedans (canaux, lacs, mer, zones autour des composants et des pistes). Chaque bord de cuivre a un liseré biseauté. Une marbrure douce (un vernis n'est jamais parfaitement plat).
3. **Pistes** : trait de liseré + trait de remplissage plus étroit, bouts ronds, avec un canal de stratifié nu de chaque côté.
4. **Métal nu** : pastilles dorées (rectangulaires, rondes, carrées) avec une bande de reflet sur le tiers haut et un trou sombre ; traversées = anneaux dorés ; cuivre nu saumon pour **une** pièce lourde et spéciale au plus.
5. **Sérigraphie** : traits blanc cassé d'épaisseur constante, très légèrement flous.
6. **Lumière** : calque additif, deux flous (environ 24 px et 5 px) sous une copie nette.
7. **Espace écran** : lumière principale douce et chaude venue d'en haut à gauche, faible profondeur de champ (bandes floues en haut et en bas, plus fortes en macro, faibles ou coupées quand il faut lire), grains de lumière flous en parallaxe devant la carte, coins assombris.

- **Police** : une police **à trait unique routée comme des pistes** (segments à 0°, 45°, 90°, angles chanfreinés, bouts ronds), dessinée en code. Solution simple et libre : Share Tech Mono ou Major Mono Display en capitales ; pour une version fidèle, tracer son alphabet (majuscules, chiffres, signes, **lettres accentuées du français**).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Space Mono à la place de Share Tech Mono et de Major Mono Display. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/share-tech-mono`, `@fontsource/major-mono-display` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Vérifier chaque caractère** : un caractère absent de la police routée s'affiche « ? » sans erreur.

## 3. Composition 9:16

- Dessiner la carte **en portrait** : le flux principal descend (de la source en haut à l'arrivée en bas) ou monte.
- **Le sujet éclairé est sur un tiers**, ou au centre exact pour un symbole. Autour de lui, **au moins deux couches de détail** : en fond le cuivre, les traversées, d'autres pistes éteintes ; devant, les grains de lumière ou le flou.
- **Le bord de la carte n'apparaît que lorsque la carte entière est le sujet** (posée sur un bureau).
- **Texte** : ancré au monde, **tracé trait par trait**, il reste sur la carte quand la caméra recule. Titres en capitales d'au moins 80 px ; étiquettes de 40 px au moins ; micro-texture (repères, notes de révision) libre de passer sous la taille de lecture.
- **Jamais de texte dans les bandes floues** du haut et du bas, ni coupé par le bord du cadre dans un plan tenu. En vertical, cela veut dire : étiquettes à lire entre y 300 et y 1300.
- Avant de tracer une étiquette, vérifier où le trajet de la caméra l'emmène pendant tout son temps de lecture.
- **Sous-titres** (avec une voix) : plaque sombre translucide entre y 1400 et y 1540, **une ligne en français**, police sans empattement libre, 46 px. La carte n'imprime alors que les **mots clés et les nombres**, jamais des phrases.
- Rien d'important à droite de x 945.

## 4. Ce qui bouge

- **Action principale** : la lumière court sur le cuivre et la caméra la chevauche. **La façon dont la lumière bouge est l'explication.**
- **Boucles de fond** : (1) les grains de lumière flous qui dérivent devant la carte, la lumière principale qui glisse lentement ; (2) la lueur stable des pastilles déjà atteintes et la rémanence qui s'éteint derrière la tête d'un flux.

| Type de flux | Comment la lumière bouge |
|---|---|
| Alternatif | de courts tirets qui **vont et viennent** le long de la piste, sur une ligne faiblement éclairée |
| Continu, à sens unique | un **courant continu** derrière une tête qui avance, avec une rémanence lente |
| Abaissement | la piste s'amincit et les tirets rapetissent |
| Eau, second flux | plusieurs filets parallèles de tirets à des vitesses différentes, plus rapides au milieu, avec de courts éclats |

- **Autorisés** : tracé de ligne `#004` (la sérigraphie n'apparaît qu'en se traçant), traînée de mouvement `#014`, pulsation `#125`, travelling de suivi `#029` (la caméra verrouillée sur la tête, placée sur un tiers), zoom arrière `#028` pendant le suivi (jusqu'à voir les deux bouts), zoom brutal `#020` sur une pastille, panoramique filé `#043` le long d'une piste, raccord de forme `#042` sur un symbole centré (même symbole, même taille, le monde autour change d'échelle), vue du dessus `#181`, très gros plan `#184`, bascule de mise au point `#033`, flou d'arrière-plan `#105`, plan fixe `#175`.
- **Interdits** : perspective et inclinaison (caméra toujours à la verticale ; une petite rotation autour de l'axe de vue est permise), fondu `#044`, volet `#045`, tourné de page `#140`, bâtiments qui s'élèvent, panneaux d'interface flottants, pistes décoratives qui ne représentent rien, cuivre ou pastilles qui « surgissent ».
- Les pastilles **lancent un éclair à l'arrivée** (une floraison vive, puis une lueur stable). Les composants « conduisent » : les arêtes internes du symbole s'illuminent au passage.
- **Plonger par un trou** : tenir d'abord le plan sur le trou, puis plonger (au moins 0,6 s) ; ressortir par un autre trou, dans l'autre sens.
- Ce qui ne bouge jamais : la carte elle-même.

## 5. Rythme et montage

- 30 images par seconde, fluide ; flou de mouvement tiré du mouvement réel à l'écran, jamais à travers une coupe.
- **Chaque phrase de voix a une action d'image** : une pastille s'allume, un flux change de forme, une étiquette se trace.
- Plans de 3 à 8 s ; un long suivi peut durer 10 s si la lumière change de forme en route.
- Transitions : mouvement dans mouvement et raccords de forme. Jamais de fondu.
- Temps de lecture d'une étiquette : 1,5 s + 1 s par tranche de 15 caractères, entièrement dans le cadre.
- Avant un verdict : retirer le rythme, ne garder que des notes longues.
- **Version courte (8 à 12 s)** : un seul trajet de lumière de 6 à 8 s et deux étiquettes (1,5 s + 1 s par tranche de 15 caractères chacune) ; couper les embranchements. Accroche : la lumière part dès la première seconde.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D en couches + traitement final (flou, lumière, grain à l'export). `blender` n'est pas nécessaire : rien n'est en perspective.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `rendu.js` (dessine une carte pour une caméra `{x, y, zoom, rotation}`), `geo.js` (routage à 0°, 45°, 90° par des points de passage, longueur d'arc, sous-chemin), `composants.js` (empreintes : pastilles, sérigraphie, zone d'isolement, chemins de conduction), `police.js`, `niveaux.js` (cartes emboîtées), `post.js`, puis **un module « monde » par carte** (contour, pistes, pastilles, étiquettes, isolements) et `film.js`.

```js
// une scène est un simple objet lu à chaque image
const scene = { t, etiquettes: { titre: 0.6 }, alternatif: [], continu: [], lueurs: [], eclairs: [] };
// flux continu : une tête en s (longueur d'arc), un courant derrière, une rémanence qui décroît
scene.continu.push({ piste: "ligne1", tete: v * (t - t0), depuis: 0, declin: 0.35, lueurTete: 1 });
// flux alternatif : des tirets qui vont et viennent
scene.alternatif.push({ piste: "ligne2", de: 0, a: L, longueurOnde: 28, amplitude: 9, phase: Math.sin(2 * Math.PI * 1.2 * t) });
// second flux, sans toucher au moteur : découper la piste en morceaux et les pousser comme lueurs argentées
for (const [a, b] of tirets(t)) scene.lueurs.push({ pts: sousChemin(piste, a, b), largeur: 4, alpha: .8, couleur: ARGENT });
```

- **Techniques clés** : le plan de cuivre rendu deux fois (passe de liseré, puis remplissage avec un isolement agrandi d'environ 1,6 px) ; les textures s'enchaînent entre octaves et les petits détails s'effacent avant de devenir plus petits qu'un pixel, donc les zooms ne scintillent pas ; les **cartes emboîtées** (un module posé sur une carte est une carte complète) permettent un zoom continu sur six ordres de grandeur.
- **Pièges** : **plan de cuivre plat** = diapositive vide (le remplir de ce que les cartes ont vraiment : traversées de couture, rangées de traversées le long des isolements, marbrure, micro-sérigraphie) ; **routage décoratif** ; **deux pistes ne se croisent pas sur une même couche** (passer par une traversée, ou contourner) ; **lumière brûlée** : des pistes larges en mode additif deviennent des barres blanches (plafonner les largeurs de lueur en pixels) ; zoomer un seul système de coordonnées sur trop d'ordres de grandeur casse la transformation ; une vue proche du contour montre soudain le bureau noir.

## 7. Son

- **Tout est synthétisé, et c'est voulu** : c'est le son de l'électricité (exception assumée à la règle « vrais enregistrements d'abord »). Sons purs et en dents de scie, ondes carrées, cloches, clics de relais, grosse caisse douce, bruit filtré.
- Accorder le bourdon sur le **ronflement du secteur** (50 Hz, proche d'un sol grave), pour qu'il appartienne à la tonalité.
- **Une règle que l'oreille suit** : une note au **trémolo haché = alternatif** ; une **note tenue = continu** ; un composant qui convertit l'un en l'autre s'entend comme le trémolo qui se lisse en note longue.
- Les arrivées sont des clics de relais ou une bouffée de bruit filtré ; un abaissement, un relais un ton plus bas à chaque fois ; le tracé de la sérigraphie, un léger grattement.
- Les sons du dehors (eau, insectes, circulation) seulement **derrière un filtre**, comme entendus à travers un mur.
- **Voix** : calme et claire, elle mène ; nombres et unités dits en entier.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Chaque image est une carte vue de dessus, sans perspective.
- [ ] Toutes les pistes sont à 0°, 45° ou 90°, et aucune ne croise une autre sur la même couche.
- [ ] Chaque piste, pastille et étiquette représente quelque chose de réel du sujet.
- [ ] La lumière est la seule couleur saturée ; ambre pour l'énergie, argent pour un second flux.
- [ ] On distingue les types de flux à leur mouvement, sans légende.
- [ ] Le cuivre n'est jamais vide et plat : traversées, marbrure, autres pistes.
- [ ] Aucune étiquette dans les bandes floues ni coupée par le bord ; tous les caractères (accents compris) existent dans la police.
- [ ] La lumière n'est jamais brûlée en barres blanches.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 5
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 40

## 9. Aperçu

- Film de démo d'origine, *Seven Milliseconds* (60 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/circuit-board.mp4
- Affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/circuit-board.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, images sous CC BY 4.0. **La piste de voix de ce film est exclue de la licence CC BY 4.0** (voix d'un service en ligne) : donner le film en lien seulement, ou le montrer **sans le son** ; ne jamais réutiliser sa voix.

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichiers `styles/circuit-board/STYLE.md`, `DEMO.md`, `demo/src/render.js`, `geo.js`, `parts.js`, `font.js`, `levels.js`, `post.js`, `loss.js`.
- Licence : MIT pour le code et les textes (© 2026 LemoLab), CC BY 4.0 pour les images du film (voix exclue).
- Adaptation Flot Web : traduction, carte en portrait, textes en une seule langue avec les accents du français (la partie sur le tracé des caractères chinois est retirée), polices de remplacement, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
