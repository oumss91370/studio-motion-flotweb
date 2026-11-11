# RPG pixel 16 bits

## 1. Identité

- **Nom** : RPG pixel 16 bits.
- **Inspiration** : les jeux de rôle sur console du milieu des années 90, vus comme un **système** : boîtes de dialogue, menus, combats, carte du monde, points de sauvegarde ; les astuces de palette du matériel indexé (échanges de palette, fondus par paliers) ; l'histoire de la profondeur de couleur (4 teintes → 8 bits → 16 bits). On apprend la grammaire, jamais un nom de jeu, un personnage, un cadre d'interface, une police, un logo, une mélodie ou un bruitage.
- **Ce que c'est** : un film qui a l'air, le son et **le comportement** d'un jeu : tout vit dans une image de 320×180 pixels (texte compris), palette limitée, sprites de 20 à 34 px, visages joués dans des **portraits**, histoire racontée comme un jeu la raconte. Il prend les systèmes du jeu au sérieux, comme un langage pour l'émotion.
- **Marche pour** : parcours de vie ou d'entreprise, versions d'un produit (fichiers de sauvegarde), apprentissage (« niveau supérieur »), crise et reprise (la palette s'effondre puis revient), départ d'un collègue, histoire d'un lieu en plusieurs époques.
- **Ne marche pas pour** : produit à montrer en vrai, sujet qui exige du détail lisible (texte long, schéma), parodie moqueuse, client qui veut du « rétro avec scanlines » (ce n'est ni du diorama 2.5D, ni de la nostalgie cathodique : pas de lignes, pas de grain, pas de flou).

## 2. Palette, typographie, matières

- **Palette maîtresse** d'environ 32 couleurs (une palette libre comme ENDESGA-32) : `#be4a2f #d77643 #ead4aa #e4a672 #b86f50 #733e39 #3e2731 #a22633 #e43b44 #f77622 #feae34 #fee761 #63c74d #3e8948 #265c42 #193c3e #124e89 #0099db #2ce8f5 #ffffff #c0cbdc #8b9bb4 #5a6988 #3a4466 #262b44 #181425 #ff0044 #68386c #b55088 #f6757a #e8b796 #c28569`.
- **Couleurs protégées** : une ou deux couleurs dupliquées qu'aucun effet de palette ne touche (par exemple une écharpe rouge `#e43b44`, un cristal cyan `#2ce8f5`). Elles deviennent le fil du film et permettent les raccords entre époques. Plus de deux, elles ne veulent plus rien dire.
- **Tables de profondeur** calculées depuis la palette maîtresse : 16 bits (identité) ; 8 bits (15 couleurs, avec **un vert foncé et un brun foncé**, sinon l'herbe de nuit vire au bleu) ; 4 couleurs `#1f2a1c #4b5e3a #93a263 #d6dba6` (dessinées nativement en demi-résolution) ; délavé (≈ 7 gris-bleus). Correspondance **par luminance**, jamais par rang.
- **La lumière est un saut d'indice** : des tables « plus clair » / « plus sombre » déplacent chaque couleur d'un cran sur sa rampe ; les halos sont des anneaux tramés. Près d'un feu, on réchauffe (verts → bruns → rouille), on n'éclaircit pas.
- **Tramage** : Bayer 4×4 pour dégradés et halos ; rayons de lumière en damier plat à 50 %.
- **Typographie** : une **police pixel originale** à largeur variable (hauteur de capitale ≈ 7 px) avec ombre d'1 px, dessinée dans l'image. Jamais une police système. Titres : même police ×2, contour encre, dégradé rangée par rangée.
- **Police de repli** : aucune : la police pixel est dessinée dans l'image (voir section 6). Pour un texte HTML hors de l'image (crédit), Space Mono. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/pixelify-sans` (largeur variable, accents français présents, vérifié le 11/11/2026) peut servir de modèle de dessin ; la police du film reste à dessiner.
- **Sprites** : membres en capsules à 3 tons (lumière haut gauche), contour encre d'1 px, tête posée à la main. Le héros a une **marque de silhouette** (un pan de vêtement, un chapeau, une coiffure). Portraits 32×32 de trois quarts : base + calques yeux / sourcils et bouche.

## 3. Composition 9:16

- Image native verticale **180×320**, agrandie ×6 sans lissage (1080×1920). C'est la même densité de pixels que l'original (320×180 ×6).
- **Boîte de dialogue = sous-titre**, dessinée dans l'image : rangées 196 à 258 (soit y ≈ 1176 à 1548 à l'écran), largeur 8 à 150 (elle s'arrête avant la marge droite). Bordure arrondie en couches (encre / blanc / argent), fond bleu sombre tramé, portrait 32×32 à gauche. Environ 20 caractères par ligne, 3 lignes : écris des répliques courtes.
- **Ligne de sol au-dessus de la boîte** : rangée ≈ 180. Personnages de 28 à 34 px de haut ; l'émotion passe par le portrait.
- Messages système et de combat : fenêtre fine en haut, rangées 28 à 44 (sous y = 160).
- Le vertical se prête à : l'ascension d'une tour (défilement vers le haut en pixels entiers), une liste de fichiers de sauvegarde, un menu pleine hauteur avec l'action visible derrière.
- 16:9 : 320×180 ×6, boîte dans le quart bas.

## 4. Ce qui bouge

- **Action principale** : un personnage traverse un système de jeu (un combat, un menu, une sauvegarde) qui dit ce qu'il ressent.
- **Boucle de fond 1** : cycles de sprites (flammes, clignements, respiration = épaules +1 px).
- **Boucle de fond 2** : curseur en forme de main qui oscille d'1 px, et **qui s'arrête quand le personnage hésite** ; ▼ qui clignote en fin de texte.
- **Autorisés** : `#006` texte tapé (≈ 38 à 40 caractères par seconde, avec la voix), `#141` mosaïque (pixellisation), `#016` parallaxe en pixels entiers (chaque couche arrondit son décalage), `#024` secousse d'écran (3-2-1 px sur 8 images), `#042` raccord sur une couleur protégée, `#128` allure image par image, `#026` panoramique vertical le long d'un objet haut, `#175` plan fixe pendant que la palette change.
- **Interdits** : `#044` fondu enchaîné et tout fondu en transparence, `#028` zoom fractionnaire, `#011` écrasement et étirement, flou, lueur, profondeur de champ, lignes de balayage, grain, rotation libre d'un sprite.
- Jeu propre au jeu : petit saut en avant pour agir, pose d'incantation, recul sous le coup, genou à terre, clignotement puis disparition.
- Fenêtres : glissent en ≈ 0,3 s (ralenti à la fin, pixels entiers).

## 5. Rythme et montage

- Plans de 3 à 7 s : le texte doit se taper et se lire. Chaque boîte reste ≥ max(1,8 s ; voix + 0,6 s) ; la boîte suivante remplace la précédente.
- **Transitions** : vignette qui s'agrandit avec mosaïque, mosaïque croisée avec changement de palette au sommet, tourbillon de rencontre (torsion + mosaïque + dissolution tramée vers le blanc), fondus de palette **par 4 paliers**.
- Un geste natif au sommet émotionnel : **effondrement de la palette** (une profondeur de moins par temps) ou **retour de la couleur** par une vague tramée.
- Silence : zéro absolu, queues d'écho comprises.
- **Version courte (8 à 12 s)** : un seul système de jeu (le combat ou le menu) : deux boîtes de 5 à 6 mots (1,8 s au moins chacune) et une action ; couper l'exploration.

## 6. Recette technique

- **Moteur** : HyperFrames ; image indexée (`Uint8Array` d'indices) présentée par une **table de correspondance** indice → couleur, puis agrandie ×6 (voir `SKILL.md`).
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `px.js` (image indexée, palettes et tables de chaque profondeur, tramage, mosaïque), `police.js`, `interface.js` (fenêtres, dialogue, menus, fichiers, barres), `sprites.js` (rig + têtes), `portraits.js`, `scenes.js` (parallaxe, éclairage par indices), `film.js` (plans, transitions, calendrier des palettes, évènements sonores, sous-titres).
- **Techniques clés** :
  ```js
  const img = new Uint8Array(180 * 320);        // indices de palette
  function presenter(table) {                    // table : indice -> [r, v, b]
    for (let i = 0; i < img.length; i++) sortie.set(table[img[i]], i * 4);
  }
  // changer toute la palette en une image : changer de table, jamais d'alpha
  const mod = (n, m) => ((n % m) + m) % m;      // un modulo négatif donne undefined
  ```
  - Dessine les époques à peu de couleurs **nativement**, avec des indices connus : réduire après coup une scène en couleurs donne de la boue.
  - Garde les teintes chaudes (orange, rose, prune) dans les palettes réduites, sinon le premier palier vire au rouge uni.
  - Exporte les sous-titres depuis le tableau qui pilote les boîtes.
- **Pièges** : cheveux en dôme lisse = casque (2 ou 3 grosses mèches) ; vêtement pâle lu comme de la peau ; objet tenu qui passe devant le visage de profil (main arrière) ; porte en planches sombres lue comme une prison (panneaux, clous) ; boîte de dialogue qui couvre les pieds (ligne de sol plus haut) ; raccord sur couleur protégée : calcule les deux positions à l'écran.

## 7. Son

- **Musique de puce** originale : ondes carrées à 12,5 / 25 / 50 %, basse triangle, percussions de bruit, écho court (≈ 180 à 370 ms). La **fidélité peut suivre la profondeur de couleur** : 4 couleurs = mono rugueux ; 16 bits = stéréo avec écho ; présent délavé = la même musique étouffée.
- Idées : l'arrangement perd une couche par palier de palette ; le groupe complet revient avec la couleur ; une fanfare d'objet comme ponctuation.
- **Bruitages** synthétisés (≈ 5 par 10 s) : bip de curseur et de validation, bips de texte (hauteur par personnage), pas avec écho, scintillement de magie, décompte de points de vie, tic de sauvegarde, pièce.
- **Un seul son organique** (un souffle, un battement de cœur) peut rendre un personnage humain à un moment.
- **Voix** (option) : première personne, peu de phrases ; ou seulement les bips de texte. Musique baissée de 7 à 8 dB sous la voix. −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : fondus en transparence, pixels de tailles différentes, police système, lueurs et flous « modernes », interface décorative qui ne raconte rien.

- [ ] Agrandie, chaque arête est un escalier de carrés égaux ; aucun pixel lissé.
- [ ] Le texte est dans la police pixel, à la résolution de l'image.
- [ ] Aucune transparence partielle : fondus par paliers de palette ou mosaïque.
- [ ] Une ou deux couleurs protégées restent intactes pendant tous les effets de palette.
- [ ] Les pieds des personnages restent au-dessus de la boîte de dialogue.
- [ ] Caméra et parallaxe en pixels entiers.
- [ ] Au moins un élément d'interface porte une émotion (un nom grisé, un curseur qui s'arrête, un fichier qu'on refuse d'écraser).
- [ ] Aucun élément repris d'un jeu existant (nom, cadre, police, mélodie, bruitage).

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 32
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu

- Film de démo d'origine *The Last Save Point* (54 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/pixel-rpg.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/pixel-rpg.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/pixel-rpg/STYLE.md`, `DEMO.md`, `demo/px.js`, `font.js`, `ui.js`, `sprites.js`, `portraits.js`, `scenes.js`, `main.js`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Palette ENDESGA-32 : palette libre de son auteur (ENDESGA).
- Adaptation Flot Web : traduction, format natif 180×320 et positions de la boîte de dialogue, numéros du dictionnaire.
