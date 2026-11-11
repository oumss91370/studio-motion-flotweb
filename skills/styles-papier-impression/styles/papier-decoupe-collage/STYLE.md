# Papier découpé, collage

## 1. Identité

- **Nom** : Papier découpé, collage (« Cut paper »).
- **Inspiration** : l'animation en papiers découpés et collés des livres et films pour la jeunesse : formes déchirées, ombres portées douces, coups de crayon gras, papiers à motifs.
- **Ce que c'est** : des **formes de papier au bord déchiré** avec une ombre portée douce, du grain et du crayon gras dans les aplats, des **motifs** (rayures, pois, vichy, veines de bois), des **mondes en pleine couleur d'un bord à l'autre**, et des **personnages au visage simple**. Du collage animé : joueur, chaleureux, **plein de petite vie**.
- **Le héros** : une petite **fleur de papier** (un cœur rond entouré de pétales, avec un visage) qui traverse l'histoire ; dans une chronologie, **elle gagne un pétale par époque**. Dessine-la dans la couleur de la chaîne du client ; tu peux aussi la remplacer par la mascotte du client, traitée en papier. (La source utilisait une étincelle orange à rayons, trop proche de l'identité d'une marque d'IA connue : non reprise.)
- **Marche pour** : une histoire avec un personnage attachant, une chronologie racontée par des objets, l'histoire d'une marque ou d'une invention, un sujet pour enfants et familles, une vidéo sans voix.
- **Ne marche pas pour** : sujet sérieux ou technique, luxe, données précises, interface réelle.
- **À ne pas confondre** : `papiers-decoupes-matisse` (grandes formes abstraites aux ciseaux, sans personnage ni ombre réaliste) ; le papier découpé rouge traditionnel (`styles-encre-asie`) ; le papier découpé satirique (`styles-cartoon`).

## 2. Palette, typographie, matières

Chaude et saturée, sur fond crème :

| Rôle | Hex (source) |
|---|---|
| Encre, papier, crème | `#2a1d18`, `#fbf6ea`, `#f3ead6` |
| Marine, bois | `#26315f`, `#c08048` |
| Moutarde, jaune | `#d9a441`, `#f6cf55` |
| Sarcelle, menthe | `#3f9f9a`, `#a9d9c6` |
| Rose, ciel | `#f3a3bf`, `#cfe2ee` |
| Violet, bleu, vert | `#8c7ad8`, `#4c6fb5`, `#5aa05a` |
| Papier vierge d'une métamorphose | `#efe5cf` |
| **Couleur du héros, réservée à lui seul** | par défaut framboise `#d94a6a` ; remplace-la par la couleur de la fiche « ma chaîne » |

- La couleur du héros n'est **jamais** utilisée en décoration.
- **Une couleur de mur dominante par scène** : chaque scène se reconnaît d'un coup d'œil sur une planche de contrôle.
- **Typographie** : écriture manuscrite libre (**Patrick Hand**, **Caveat** ou **Gochi Hand**, OFL). **Le texte est lettré à la main sur des étiquettes de papier** (étiquette d'année, bande de légende, petite étiquette), jamais nu.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Patrick Hand et de Caveat et de Gochi Hand. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/patrick-hand`, `@fontsource/caveat`, `@fontsource/gochi-hand` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La police de la marque ou de la chaîne vient du client : à vérifier (licence, accents français).
- **Matières** : chaque forme est du papier déchiré : bord tremblé et déchiré, ombre douce (décalée vers le bas, floue), grain, et en option un gribouillis de crayon gras dans l'aplat. Motifs découpés dans la forme. Visages simples (deux yeux, une bouche), avec des humeurs.

## 3. Composition 9:16

- Style pensé pour le vertical. **Zone de contenu : x 60 à 940, y 250 à 1500** ; les fonds vont jusqu'aux bords.
- **Un monde plein cadre** : un papier peint, un ciel, une table, un vichy, une nuit étoilée, ou une carte de couleur unie pour l'humeur du moment. **Jamais un objet qui flotte sur du papier vide**, sauf si le vide est la scène.
- Construction : un mur (couleur dominante), un sol ou une table, puis les accessoires devant.
- **Trois détails de vie de fond au moins**, qui ne portent pas l'intrigue : un chat qui dort, des oiseaux sur un fil, un papillon de nuit à la lampe, la vapeur d'une tasse, des confettis, une horloge, des notes collées, une guirlande.
- Étiquette d'année ou de thème en haut (y ≈ 300 à 380), bande de légende en bas (y ≈ 1340 à 1480), écriture 60 à 80 px, 2 lignes au plus. Texte dans le monde ≥ 50 px.
- Varie les échelles : au moins un très gros plan dans la vidéo.

## 4. Ce qui bouge

- **Action principale** : **un personnage avec un visage, qui joue** : le héros, une personne, un animal, une tasse avec des yeux. Il lui arrive des choses et il **réagit** (ébahi, triste, ravi, concentré).
- **Boucle de fond 1** : le héros vit tout seul au repos : petit balancement, clignement, pétales qui oscillent.
- **Boucle de fond 2** : la vie de fond (voir plus haut) et le léger frémissement des bords déchirés.
- **Gestes natifs** : les choses arrivent en **« pop »** ; les mots **s'écrivent** ; dans une chronologie, les mondes sont reliés par des **métamorphoses de forme** (le soleil devient un œil, la lune devient une assiette) ; dans une histoire à personnage, coupe franche sur le temps.
- **La fenêtre de métamorphose** est un trou déchiré avec un liseré de papier ; **les métamorphoses se font sur du papier crème vierge**. L'objet-pont est grand et bien dans le cadre au moment du passage.
- **Autorisés** : `#001` apparition en rebond, `#012` métamorphose de forme, `#128` saccadé (tout change toutes les 2 images), `#011` écrasement et étirement (héros), `#004`/`#006` écriture progressive, `#017` ouverture par un trou déchiré, `#046` coupe franche (une seule, sur la chute), `#125` pulsation, `#096` flottement.
- **Interdits** : `#044` fondu ; faire disparaître un accessoire en le rendant transparent (les textures cassent la transparence : on le retire) ; mélanger deux couleurs de mur dans une métamorphose (boue) ; texte nu ; ombres dures ; dégradés.

## 5. Rythme et montage

- **Tout change toutes les 2 images** (frémissement, caméra, déplacements) : 15 paliers par seconde à 30 i/s. Ce sont des déplacements et des bords qui frémissent (faible amplitude) : aucune couleur de fond ne change à cette cadence.
- Du nouveau toutes les 2 à 4 s. Une chronologie de 60 s peut enchaîner une quinzaine de mondes par des métamorphoses, avec **une seule coupe franche**, sur la chute.
- Cale métamorphoses et coupes sur la grille des croches (à 30 i/s : 112,5 BPM, croche = 8 images).
- **Silence avant la chute** ; la fin reprend le début, changé.
- **Version courte (8 à 12 s)** : trois mondes reliés par deux métamorphoses, une étiquette par monde.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D, `renderAt(t)`.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `papier.js` (forme découpée : points, couleur, motif, crayon gras, grain, ombre, déchirure), `motifs.js` (rayures, pois, vichy, bois), `personnages.js` (visage à humeurs, héros à pétales, personne, main, chat, tasse, plante), `etiquettes.js` (année, légende, écriture progressive), `pont.js` (métamorphose de forme dans une fenêtre déchirée), `scenes.js`.
- **Techniques clés** :
  ```js
  const B = Math.floor(t * 15);                                   // palier : toutes les 2 images
  decouper(points, couleur, { motif: rayures(18), crayon: true, grain: 0.3,
                              ombre: { dy: 8, flou: 10 }, dechirure: 2.5 });
  heros(x, y, r, { petales: epoque, humeur: "ebahi", cle: B });   // un pétale de plus par époque
  // pont : interpoler deux contours rééchantillonnés au même nombre de points, sur papier vierge
  ```
- **Pièges** :
  - Un objet seul sur du papier vide : la scène a l'air inachevée.
  - Deux scènes de la même couleur de mur : on ne les distingue plus.
  - Métamorphose entre deux murs colorés : boue. Passe par le papier crème.
  - Objet-pont trop petit ou hors cadre au moment du passage : on ne comprend pas le lien.
  - Trop de vie de fond qui bouge fort : elle vole l'attention ; elle reste petite et lente.

## 7. Son

- **Musique** : joyeuse et faite main : ukulélé, xylophone, claquements de mains, piano droit, sifflement ; tempo calé sur la grille d'images.
- **Bruitages** (≈ 5 par 10 s) : papier qu'on déchire ou qu'on pose (un par arrivée importante, pas par objet), petit « pop », crayon qui écrit, un son doux et montant pour une métamorphose ; un détail de fond peut avoir son petit son, rarement.
- **Arc sonore** : montée, pic, **silence**, cadeau (la chute), au revoir. Le moment le plus chargé n'est pas le plus fort : le plus fort tombe sur la chute, après le silence.
- Sans voix, les étiquettes portent le sens ; avec voix, chaque monde démarre ≈ 0,3 s après la fin d'une phrase. Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] **Un personnage avec un visage, qui joue** et réagit, dans chaque scène.
- [ ] **Un monde plein cadre** : jamais un objet flottant sur du papier vide (sauf scène voulue).
- [ ] **Du papier qu'on sent** : bords déchirés, ombres, crayon gras, au moins un motif par image.
- [ ] **Trois détails de vie de fond au moins**, qui ne portent pas l'intrigue.
- [ ] **Texte lettré à la main sur des étiquettes de papier**, jamais nu.
- [ ] **Le nombre de pétales du héros dit le temps** dans une chronologie ; sa couleur n'est utilisée que pour lui.
- [ ] Une couleur de mur par scène ; métamorphoses sur papier vierge.
- [ ] Contenu dans x 60 à 940, y 250 à 1500.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 16
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Image d'exemple d'origine : `plugins/animate/skills/animate/styles/cut-paper/sample.png` (540×960), planche des sept styles `docs/styles.png`, dépôt https://github.com/cth9191/animate (MIT, © 2026 cth9191). Démo construisible `styles/cut-paper/demo/` (8 s : la lune devient le soleil ; pas de vidéo dans le dépôt).
- L'image d'origine montre le héros d'origine (étincelle orange), et l'exemple long `examples/history-of-ai` cite des produits tiers : à ne pas utiliser comme vitrine. Produire notre propre aperçu 9:16.

## 10. Origine

- **cth9191/animate**, commit `7e5eb56` (version 0.4.0) : `plugins/animate/skills/animate/styles/cut-paper/STYLE.md`, `kit.js`, `kit/morph.js`, `grammar/FRAME.md`, `grammar/FORMATS.md` (format « chronologie en chaîne de métamorphoses », éprouvé). Licence MIT, © 2026 cth9191.
- Adaptation Flot Web : traduction, **héros remplacé** (une fleur à pétales au lieu d'une étincelle orange à rayons), polices libres, tempo recalculé pour 30 i/s, portage prévu vers HyperFrames, numéros du dictionnaire de mouvements.
