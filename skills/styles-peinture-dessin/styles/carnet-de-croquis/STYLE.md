# Carnet de croquis

## 1. Identité

- **Nom** : Carnet de croquis (« Sketchbook »).
- **Inspiration** : les petites vidéos explicatives dessinées dans un carnet à spirale : du graphite, une seule couleur d'accent, un lettrage à la main qui raconte à la place d'une voix.
- **Ce que c'est** : graphite et **un seul accent** sur une page de carnet chaude. Chaque ligne est tracée à la main et frémit. Les choses sont **crayonnées, puis encrées, puis coloriées d'un gribouillis rapide**, et le lettrage manuscrit fait la narration. **La page est le monde** : sa grille de points, sa spirale, ses traces de gomme et son rond de café restent visibles ; la caméra se déplace **sur la page** au lieu de couper.
- **Marche pour** : petite explication chaleureuse de 10 à 30 s, astuce, « comment j'ai fait », idée qui naît, liste courte, vidéo **sans voix off**, créateur solo.
- **Ne marche pas pour** : sujet luxueux, données précises, longue narration, image photo-réaliste.
- **À ne pas confondre** : `croquis-urbain` dessine un lieu réel à la plume et au lavis ; `encre-hachures` remplit tout de hachures et oppose deux mondes ; `tableau-blanc` est un schéma au feutre. Ici : un carnet, du crayon, un petit héros.

## 2. Palette, typographie, matières

| Rôle | Hex | Usage |
|---|---|---|
| Papier | `#f2ead8` | la page ; aussi la feuille vierge d'une métamorphose |
| Encre | `#2a2420` | lignes décidées, lettrage, yeux |
| Graphite (clair) | `#6f6a63` (`#9a948b`) | lignes de construction, le fouillis, les hachures, ce qui n'est pas encore décidé |
| **Accent : le héros, et lui seul** | par défaut bleu canard `#2a7f8e` (ombre `#1f5f6b`) | remplace-le par la couleur de la fiche « ma chaîne » du client |
| Surligneur | `#f7d64a` | **le** mot à lire ; un seul objet lumineux (ampoule, soleil) |
| Feutre rouge | `#e0483a` | un soulignement de titre ou un tampon, une fois par scène |
| Vert | `#4f9d5d` | une coche (fait, correct) |
| Petits objets réels du bureau | crayon `#f1bf2c`, bois `#ecc995`, gomme `#ef9aa6`, ruban `#efe2b4`, fiche `#fffdf6` | gardés petits |

- La source utilisait un accent terre cuite, très proche d'une identité de marque connue : **remplacé ici**. Si une deuxième chose prend la couleur d'accent, elle ne veut plus dire « le héros ».
- **Typographie** : écriture manuscrite libre (**Caveat** ou **Patrick Hand**, OFL) pour le lettrage ; **Permanent Marker** (Apache 2.0) pour les mots au feutre. Chaque lettre est posée séparément, avec un léger décalage qui frémit, et un contour au poids du stylo pour rester lisible sur téléphone.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Caveat et de Patrick Hand ; Archivo Black à la place de Permanent Marker. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/caveat`, `@fontsource/patrick-hand`, `@fontsource/permanent-marker` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La police de la marque ou de la chaîne vient du client : à vérifier (licence, accents français).
- **Matières** :
  - *Deux outils* : l'**encre** = un trait assuré + un second passage fin qui ne coïncide pas tout à fait ; le **graphite** = deux passages légers, plus lâches. Graphite pour le provisoire, encre une fois que c'est décidé.
  - *La couleur est à côté du trait* : aplat posé à quelques pixels de l'encre, comme un coloriage rapide qui rate le contour.
  - *L'ombre est une hachure*, jamais un dégradé ; un objet rond garde un cercle clair en haut à gauche.
  - *La couleur est un gribouillis* : un va-et-vient d'une seule couleur sur un lavis très pâle ; il peut s'écrire progressivement.
  - *La page* (construite une fois, en cache) : grain, fibres, vignettage, grille de points (ou lignes), traces de graphite, fantômes de lignes gommées, rond de café, tranche des pages du dessous, **spirale le long du haut**.
  - *Dépassements* : les cercles passent leur point de départ et dérivent vers l'extérieur ; les cadres finissent un peu après leur coin.

## 3. Composition 9:16

- Style pensé pour le vertical. **Zone de contenu : x 60 à 940, y 250 à 1500.** La spirale du carnet longe le haut (au-dessus de y = 250).
- Étiquette de page (le thème, 2 ou 3 mots) vers y ≈ 340.
- **Légende manuscrite** : ≈ 20 caractères par ligne, **deux lignes au plus**, 80 px, centrée, entre y ≈ 1330 et 1420. Elle dit l'étape ; on doit pouvoir la lire sur téléphone **sans regarder l'image**. Un coup de surligneur sur **un** mot, après que la ligne est écrite.
- Un sujet au centre (y 500 à 1200), le héros à côté ou dessous, ≥ 180 px.
- **De la page dans chaque image** : grille, spirale, trace ou bord. Rien ne couvre la page d'un bord à l'autre. Ne remplis pas le cadre de dessin : laisse du papier.
- 16:9 : même page en paysage, légende en bas au centre, spirale à gauche.

## 4. Ce qui bouge

- **Action principale** : **les choses sont dessinées, pas posées** : crayonné, encre par-dessus, gribouillis de couleur ; le crayon (un petit accessoire) suit la ligne en train de se tracer. Effacer se fait avec la gomme et ses miettes.
- **Boucle de fond 1** : **tout frémit** : le tremblé change toutes les 2 images, y compris le grain de la page (petite surface et faible amplitude seulement : des traits et un grain fin ; la luminosité d'ensemble de la page ne varie pas). La **structure** (où va un gribouillis, la longueur d'une hachure) est fixée par une graine et ne bouge jamais ; seul le tremblé change.
- **Boucle de fond 2** : petite vie en graphite dans les marges : un avion en papier qui boucle, une fourmi sur une ligne, des étoiles qui clignotent, une fumée de cheminée, des oiseaux.
- **Le héros** joue : écrasement et étirement, petit saut sur le temps, yeux qui regardent le sujet et clignent, humeur (calme, ébahi, content, perplexe). De petites marques de graphite disent ce qu'il ressent : `?`, `!`, goutte de sueur, étincelle.
- **Autorisés** : `#004` tracé de ligne, `#136` trait qui frémit, `#128` saccadé (un dessin toutes les 2 images), `#011` écrasement et étirement (héros), `#080` surlignage, `#012` métamorphose sur la page nue, `#027` la caméra se penche sur le sujet, `#028` puis recule, `#001` apparition en rebond **seulement pour une réaction** (un `!`, un tampon, un saut).
- **Interdits** : `#044` fondu, ombres portées plates (utilise une trace de graphite), dégradés, second accent, texte typographié, glissement lisse de quoi que ce soit (sauf la caméra), image plein cadre.

## 5. Rythme et montage

- Un dessin toutes les 2 images (15 par seconde à 30 i/s). Cale tout sur une grille musicale où une double-croche fait un nombre entier d'images : par exemple **112,5 BPM à 30 i/s** (temps = 16 images, croche = 8, double-croche = 4).
- **Un sujet, un geste** à la fois : une seule chose est en train d'être dessinée, et le crayon est dessus.
- Les coupes rapides sont **les étapes d'un seul mouvement** : une rafale de coupes à la double-croche forme un geste, pas des plans séparés.
- Du nouveau toutes les 2 à 4 s. Durée type : 10 à 20 s.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D, `renderAt(t)`.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `page.js` (page en cache, depuis un hasard à graine), `traits.js` (encre, graphite, tracé progressif, position de la pointe), `couleur.js` (aplat décalé, hachure dans une découpe, gribouillis), `lettrage.js` (lettre à lettre, surligneur, soulignement), `accessoires.js` (crayon, gomme, fiche, ruban, tampon, coche), `heros.js`, `scenes.js`.
- **Techniques clés** :
  ```js
  const B = Math.floor(t * 15);                     // pas de frémissement : toutes les 2 images
  // tremblé : la phase dépend de B, la structure dépend de la clé seulement
  const dx = amp * Math.sin(i * 0.9 + hash(cle, B) * 6.28);
  // ordre d'apparition d'un objet
  graphite(P, { part: p1 });  encre(P, { part: p2 });  gribouillis(P, accent, { part: p3 });
  crayon(pointeDe(P, p2));                           // l'accessoire suit la ligne
  ```
  - Donne un aplat couleur papier à une maison ou à un feuillage **avant** son encre, sinon le graphite de derrière transparaît.
  - Chaque valeur aléatoire a une clé : clé seule pour la structure, clé + `B` pour le tremblé.
- **Pièges** : un second accent ; une ombre en dégradé ; une ombre portée plate ; un texte qui a l'air typographié ; un dessin qui remplit la page jusqu'aux bords ; une légende de plus de deux lignes.

## 7. Son

- **Musique** : petite formation acoustique enjouée (ukulélé, guitare, claquements de doigts, glockenspiel) ou piano droit ; tempo calé sur la grille d'images.
- **Bruitages** (≈ 5 par 10 s) : crayon sur papier (texture continue, basse), **un** coup de surligneur par légende, tampon, gomme, page qui se tourne, petit « pop » pour une réaction du héros.
- Le style marche sans voix : la légende porte le sens. Si une voix est ajoutée, elle dit autre chose que la légende ne répète pas mot pour mot. Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] **Le graphite porte tout** : compte les couleurs. Encre et graphite font l'essentiel ; l'accent n'est que sur le héros ; le jaune seulement sur le mot à lire ou l'unique objet lumineux.
- [ ] **Le lettrage est le narrateur** : légende ≤ 20 caractères par ligne, 2 lignes au plus, un mot surligné, lisible sans l'image.
- [ ] **La page est le monde** : de la page visible dans chaque image.
- [ ] **Tracé plutôt qu'apparition** : crayon, puis encre, puis couleur.
- [ ] **Le fouillis est en graphite, le résultat est à l'encre**, net et rare.
- [ ] **Tout frémit, rien ne nage** : la structure reste fixe.
- [ ] **Un sujet, un geste** ; la vie de fond est en graphite et petite.
- [ ] **Zone sûre** : contenu dans x 60 à 940, y 250 à 1500.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 14
- Bleu-violet : interdit
- Texte vivant : oui
- Taille mini du texte : 50

## 9. Aperçu

- Image d'exemple d'origine : `plugins/animate/skills/animate/styles/sketchbook/sample.png` (540×960) et planche des sept styles `docs/styles.png`, dépôt https://github.com/cth9191/animate (MIT, © 2026 cth9191). Démo construisible `styles/sketchbook/demo/` (6 s ; pas de vidéo dans le dépôt).
- L'image d'origine montre le héros terre cuite : à ne pas utiliser comme vitrine ; produire notre propre aperçu 9:16 avec l'accent de remplacement.

## 10. Origine

- **cth9191/animate**, commit `7e5eb56` (version 0.4.0) : `plugins/animate/skills/animate/styles/sketchbook/STYLE.md`, `kit.js`, `grammar/FRAME.md`. Licence MIT, © 2026 cth9191.
- Adaptation Flot Web : traduction, **couleur d'accent et héros changés**, polices libres à la place des polices système, tempo recalculé pour 30 i/s, portage prévu vers HyperFrames, numéros du dictionnaire de mouvements.
