# Pixel art 8 bits

## 1. Identité

- **Nom** : Pixel art 8 bits.
- **Inspiration** : les consoles de salon et consoles portables du milieu des années 80 : gros pixels carrés, quelques couleurs, tramage en damier à la place des dégradés, police en grille de points, affichage de score. On reprend le vocabulaire générique de l'arcade (pièces, briques, score, cœurs), jamais les personnages, logos ou blocs emblématiques d'un jeu précis.
- **Ce que c'est** : chaque image est dessinée à une **basse résolution interne**, avec des primitives en pixels entiers et une palette limitée, puis agrandie au plus proche voisin. Effets d'écran qui appartiennent à un appareil : grille LCD pour une portable, lignes de balayage et coins assombris pour une borne. **La résolution peut dire le temps** : une époque ancienne est plus grossière qu'une récente ; une chronologie devient plus nette en avançant.
- **Marche pour** : histoire d'une technologie ou d'une marque, leçon courte et ludique, annonce de communauté, compteur ou objectif à atteindre, boucle d'ambiance.
- **Ne marche pas pour** : visages expressifs, produit à montrer fidèlement, texte long (9 à 30 caractères par ligne seulement), élégance.
- Différence avec `pixel-rpg-16-bits` : ici pas de système de jeu complet ni de palette indexée animée ; c'est le style pixel le plus simple, celui du débutant.

## 2. Palette, typographie, matières

**Palette 16 couleurs** (une par époque « borne d'arcade ») :

| Nom | Hex | Nom | Hex |
|---|---|---|---|
| encre | `#14101E` | vert | `#2E8A4A` |
| nuit | `#232A4E` | citron vert | `#8AD04A` |
| bleu | `#2F5FA8` | jaune | `#F6D64A` |
| ciel | `#5FB4E6` | orange (**corps du héros**) | `#F08A32` |
| glace | `#A8F0F0` | rouge | `#D83A3A` |
| blanc | `#F4F0E6` | rose | `#F07AA8` |
| gris | `#8A8CA0` | violet | `#6A3A8A` |
| ardoise | `#4A4E66` | brun | `#7A4A2A` |

**Palette portable 4 verts** (du plus sombre au plus clair) : `#0F2A14` · `#306A2E` · `#8AAC2A` · `#C4D870`. Dans une telle époque, tout (ciel, arbres, héros, texte) est l'un de ces quatre.

- **Trois couleurs à garder en petites surfaces** : encre `#14101E`, nuit `#232A4E` et violet `#6A3A8A` sont des bleu-violet sombres. Elles servent aux contours, aux ombres, aux yeux, à un objet : jamais à un ciel ou à un fond plein cadre. Un ciel de nuit fait avec encre et nuit a donné 50 % d'images « bleu-violet » et un feu rouge à la porte de livraison (rendu d'essai du 11/11/2026) ; le même film avec un ciel bleu / ciel / glace : 0 %. **Ce style n'a pas droit à la dérogation bleu-violet** (il n'est pas dans le tableau de `references/derogation-bleu-violet.md`) : une époque « de nuit » se fait au crépuscule (ciel bleu `#2F5FA8`, étoiles blanches, fenêtres jaunes), pas en noir-violet.
- **Une palette par époque**, appliquée de force : après le dessin, chaque pixel est ramené à la couleur de palette la plus proche. Jamais deux palettes mélangées dans une époque.
- Ciel en dégradé « à l'ancienne » : les 3 bleus **de la palette**, bleu `#2F5FA8` / ciel `#5FB4E6` / glace `#A8F0F0`, avec, à chaque frontière, une bande en damier `(x + y) % 2`. (La source utilisait trois autres bleus, hors palette : la palette forcée les aurait de toute façon ramenés à ceux-ci.)
- **Typographie** : police bitmap **5×7 à dessiner dans le code** (A-Z, 0-9, ponctuation, **et les capitales accentuées du français** : voir la section 6 ; un caractère avance de 6 px), en rectangles de pixels entiers, toujours à la résolution de l'époque. Elle n'est pas fournie par le plugin. Pour un affichage de score en pleine résolution : **Press Start 2P** (OFL), avec ombre noire décalée. Jamais une police système.
- **Police de repli** : aucune pour le texte du jeu (il est dessiné en pixels). Pour un affichage en pleine résolution quand Press Start 2P manque : Space Mono, fournie par HyperFrames. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/press-start-2p` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : aucune. Ombrage des formes rondes : clair en haut à gauche, sombre en bas à droite, tramé à la frontière. Forme sombre sur fond sombre (une grotte, une ombre) : **un liseré clair d'1 px**.

## 3. Composition 9:16

Résolutions internes qui divisent exactement 1080×1920 :

| Résolution | Taille du pixel | Évoque | Caractères par ligne |
|---|---|---|---|
| 54×96 / 72×128 | 20 / 15 px | les toutes premières époques | 9 / 12 |
| 90×160 | 12 px | portable 4 couleurs | 15 |
| 135×240 | 8 px | première console de salon | 22 |
| 180×320 | 6 px | arcade 16 couleurs | 30 |
| 270×480 | 4 px | époque tardive et détaillée | 45 |

- Garde **au moins un facteur 2** entre deux époques voisines pour que le changement se lise sur un téléphone.
- **Monde plein cadre** : ciel, horizon et sol jusqu'aux bords ; les panneaux (étiquettes, légendes, score) se posent dessus.
- **Zone sûre** : étiquettes, légendes, score et héros dans x 60 à 940, y 250 à 1500. **Le panneau entier compte**, bord et curseur-bloc compris, pas seulement les lettres : dans le rendu d'essai, un panneau de 11 caractères à 12 px par point débordait jusqu'à x 984. Nombre de caractères par ligne dans la zone utile = 885 ÷ (6 × taille du point), moins 2 pour les bords et 1 pour le curseur : **9 caractères** quand le point fait 12 px, **21** quand il fait 6 px.
- **Taille du texte** : une lettre fait 7 points de haut. Point de 12 px : 84 px ; point de 6 px : 42 px ; point de 4 px (270×480) : 28 px, trop petit pour une légende : dans cette résolution, dessine le texte à lire avec un point double (56 px).
- Légende : panneau à bord d'1 px et coins coupés, texte tapé avec curseur-bloc clignotant. Étiquette : surgit en taille double pendant un dessin. Score et cœurs : en haut de la zone sûre, **juste en dessous de y 250** (entre y 250 et y 340), jamais au-dessus.
- Vérifie la scène **à sa taille interne** (90×160, c'est minuscule) : héros, objet-pont et légende doivent s'y lire comme des formes.
- 16:9 : 240×135 (pixel de 8) ou 320×180 (pixel de 6).

## 4. Ce qui bouge

- **Action principale** : un héros qui **agit** : il regarde les choses, a une humeur, sautille, et une bulle « ! » quand il remarque quelque chose.
- **Boucles de fond (3 détails de vie au moins)** : étoiles ou fenêtres qui clignotent (de petits points, deux fois par seconde au plus), nuage qui avance d'1 px tous les 2 dessins, petite bête qui patrouille, touffes d'herbe qui changent d'image sur le temps.
- **Autorisés** : `#128` allure image par image, `#141` pixellisation (transition par blocs qui grossissent puis rétrécissent), `#006` texte tapé, `#127` boucle aller-retour à 2 images, `#123` saut en parabole de pixels entiers (l'ombre rétrécit dessous), `#046` coupe sèche vers une résolution plus fine (c'est le « zoom » du style), `#012` métamorphose en gros pixels tramés d'un objet-pont entre deux époques.
- **Interdits** : tout déplacement d'une fraction de pixel, `#028` zoom de caméra (les pixels deviendraient inégaux), `#044` fondu et toute rampe de transparence, `#011` écrasement lissé, `#016` parallaxe lissée, arcs, traits et textes lissés, dégradés.
- **Sur les deux** : 15 dessins par seconde à 30 i/s. Un déplacement d'1 px par dessin donne une vitesse régulière. Les sprites ont 2 images qui s'échangent sur le temps ; une rotation passe par 4 à 6 largeurs.
- **Pas de caméra** : on déplace le monde, par pixels entiers.

## 5. Rythme et montage

- Du nouveau toutes les 2 à 4 s. Une époque = 4 à 8 s.
- **Chronologie en chaîne** : l'ancienne époque se referme dans une fenêtre en escalier, un objet-pont (la lune devient une pièce) se métamorphose pendant que sa grille passe d'une taille de pixel à l'autre (12 → 10 → 8 → 6), la nouvelle époque s'ouvre. L'objet-pont garde sa position et sa taille à l'écran ; seul son pixel change.
- Les choses **clignotent** au lieu de fondre : étoiles, lucioles, curseurs, par tout ou rien sur le temps.
- Petites boucles lisibles en un quart de seconde : queue en 4 poses, cœur du score qui clignote, bloc qui libère une pièce (demi-sinus de 9 px).
- **Version courte (8 à 12 s)** : deux époques de 5 s reliées par la mosaïque, **un seul panneau de texte par époque** (2 à 3 mots, tenu 1,5 s au moins) ; couper toute époque supplémentaire. Accroche : le héros agit (marche, bulle « ! ») dès la première seconde. (Découpage tenu dans le rendu réel du 11/11/2026.)

## 6. Recette technique

- **Moteur** : HyperFrames ; canvas basse résolution agrandi sans lissage (voir `SKILL.md`).
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `pixel.js` (primitives : point, rectangle, ligne de Bresenham, ellipse, polygone, tramage, halo tramé), `palette.js` (palettes, couleur la plus proche), `police.js` (5×7), `sprites.js` (sprites depuis des tableaux de chaînes), `heros.js`, `epoques.js` (résolution, palette et effets d'écran par époque), `scenes.js`.
- **Techniques clés** :
  ```js
  const B = Math.floor(t * 15);                    // numéro du dessin
  const x = 20 + B;                                // 1 px par dessin
  const bayer = [0,8,2,10, 12,4,14,6, 3,11,1,9, 15,7,13,5];
  const seuil = (x, y) => (bayer[(y & 3) * 4 + (x & 3)] + 0.5) / 16;
  // dégradé = deux couleurs + tramage : couleur B là où f(x, y) > seuil(x, y)
  ```
  - **Personnage dessiné par pièces, chacune avec son contour noir d'1 px** (bras arrière, corps, cheveux, visage, bras avant) : un seul contour global fond tout en une masse.
  - Passage en sprite d'une forme lissée : alpha < 110 → transparent ; le reste → couleur de palette la plus proche ; contour = tout pixel transparent voisin d'un pixel plein.
  - Yeux, bouche, petits objets (une tasse de 6×5) : **posés pixel par pixel**, pas réduits depuis un dessin lissé.
  - **Police 5×7 et accents français** (à écrire par l'agent : aucune police bitmap n'est fournie). Chaque caractère est une table de 7 rangées de 5 points. Pour une capitale accentuée, **l'accent prend les 2 rangées du haut et la lettre se tasse sur 5 rangées**. É et È ainsi construits ont été rendus et lus à 360 px de large le 11/11/2026 ; les autres suivent la même construction et ont été rendus le même jour dans une capture HyperFrames (une image fixe, pas un film) : accents lisibles, « Œ » serré.
  ```js
  const ACC = { aigu: ["00010", "00100"], grave: ["01000", "00100"], circ: ["00100", "01010"], trema: ["01010", "00000"] };
  const COURT = {                                   // capitales tassées sur 5 rangées
    A: ["01110", "10001", "11111", "10001", "10001"], E: ["11111", "10000", "11110", "10000", "11111"],
    I: ["01110", "00100", "00100", "00100", "01110"], O: ["01110", "10001", "10001", "10001", "01110"],
    U: ["10001", "10001", "10001", "10001", "01110"] };
  const ACCENTUEES = { "É": ["E", "aigu"], "È": ["E", "grave"], "Ê": ["E", "circ"], "Ë": ["E", "trema"], "À": ["A", "grave"], "Â": ["A", "circ"],
                       "Î": ["I", "circ"], "Ï": ["I", "trema"], "Ô": ["O", "circ"], "Ù": ["U", "grave"], "Û": ["U", "circ"], "Ü": ["U", "trema"] };
  for (const [c, [lettre, acc]] of Object.entries(ACCENTUEES)) G[c] = [...ACC[acc], ...COURT[lettre]];
  G["Ç"] = ["01110", "10001", "10000", "10000", "10001", "01110", "00100"];   // cédille sur la dernière rangée
  G["Œ"] = ["01111", "10100", "10100", "10111", "10100", "10100", "01111"];
  function texte(g, s, x, y, couleur, e = 1) {      // e = taille du point, en pixels entiers de la grille
    g.fillStyle = couleur;
    [...s].forEach((ch, i) => { const gl = G[ch] || G[" "];
      for (let r = 0; r < 7; r++) for (let c = 0; c < 5; c++) if (gl[r][c] === "1") g.fillRect(x + (i * 6 + c) * e, y + r * e, e, e); });
  }
  ```
  - **Brancher sur HyperFrames** : le dessin écoute `hf-seek`, et l'on enregistre une **timeline vide** après le script du dessin (`window.__timelines["main"] = gsap.timeline({ paused: true });`). Sans elle, `lint` sort l'erreur `missing_timeline_registry`. Ne pas écrire `data-no-timeline` : il fait taire aussi le contrôle qui détecte un film figé (le film d'essai du 11/11/2026 l'utilisait ; la voie retenue depuis est la timeline vide). Exemple complet dans le `SKILL.md` de la catégorie et dans le skill `rendu`, section « Film en canvas piloté par `hf-seek` ».
  - Effets d'époque déterministes : sur l'image basse résolution (palette forcée, bruit, blocs aplatis) ; sur l'écran (lignes de balayage = tiers bas de chaque rangée assombri, grille LCD, coins assombris tramés).
- **Pièges** : `arc`, `stroke`, `fillText`, filtres ou transparence dans la passe basse résolution ; sprite agrandi d'un facteur non entier ; texte d'affichage trop large (48 px en Press Start 2P pour 1080 de large) ; palette brisée par un flou (un flou « d'époque » ne se permet que dans une seule époque).

## 7. Son

- **Musique de puce** originale : deux voix carrées, une basse triangle, percussions de bruit ; en mono pour une époque portable. Un motif court qui change d'instrument d'une époque à l'autre.
- **Bruitages synthétisés** (c'est le son juste ici ; ≈ 5 par 10 s) : pièce, saut, bip de texte, « power-up » montant, bloc cogné.
- Aucun bruitage ni jingle tiré d'un jeu existant.
- **Voix** (option) : courte, claire, légèrement réduite en bande pour rester dans l'appareil. −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Agrandie à 100 %, chaque arête est un escalier de carrés égaux : aucun lissage, aucun arc, aucun texte système.
- [ ] Palette limitée par époque (4 ou 16 couleurs), imposée après dessin ; mélanges par tramage, jamais par fondu.
- [ ] Silhouettes lisibles à la résolution interne.
- [ ] Un héros qui agit (regard, humeur, saut).
- [ ] Au moins 3 détails de vie en fond.
- [ ] Monde plein cadre ; panneaux natifs en pixels (bord d'1 px, coins coupés, police bitmap).
- [ ] Les époques tardives sont plus fines ; facteur ≥ 2 entre voisines.
- [ ] Étiquettes, légendes, score et héros dans x 60 à 940, y 250 à 1500, panneaux et curseur compris ; rien d'un jeu existant.
- [ ] Aucun ciel ni fond plein cadre en encre, nuit ou violet ; les accents français sont dessinés (É, È, À, Ç…).

**Réglages des contrôles**
- Mouvement : normal
- Caméra : fixe
- Couleurs max : 16
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 42

## 9. Aperçu

- Image d'exemple d'origine (540×960) : https://github.com/cth9191/animate/blob/main/plugins/animate/skills/animate/styles/pixel/sample.png · planche des 7 styles : https://github.com/cth9191/animate/blob/main/docs/styles.png (© 2026 cth9191, MIT).
- Carte huashu : animation `assets/showcase/pixel.gif` du dépôt, à consulter seulement (composition reprise d'un film tiers).

## 10. Origine

- **cth9191/animate**, commit `7e5eb56` (0.4.0) : `plugins/animate/skills/animate/styles/pixel/STYLE.md`, `kit.js` (résolutions, palettes, police, tramage, habitudes de mouvement, liste de contrôle). Licence MIT, © 2026 cth9191.
- **alchaincyf/huashu-art-motion**, commit `1468196` : `references/风格配方/14_8bit.md` (traduit du chinois), `scripts/engine/scenes/14_8bit.js` (contour par pièce, passage en sprite, ciel à 3 bleus, petites boucles). Licence MIT, © 花叔 Huashu. Carte notée ★★★ par son auteur.
- Police Press Start 2P : SIL OFL 1.1.
- Adaptation Flot Web : fusion des deux sources, cadence à 30 i/s, numéros du dictionnaire.
- Vérifié par un rendu réel le 11/11/2026 (HyperFrames 0.9.33) : ça marche avec corrections ; pixels nets après encodage (PSNR 43,4 dB) ; la version à ciel de nuit a été refusée (50 % d'images bleu-violet) et remplacée par un ciel de jour (0 %).
