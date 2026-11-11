# Encre et hachures

## 1. Identité

- **Nom** : Encre et hachures (« Crosshatch ink »).
- **Inspiration** : l'illustration à la plume des livres et de la presse : un trait d'encre nerveux, des ombres en hachures croisées, un peu de crayon de couleur.
- **Ce que c'est** : un trait d'encre **qui frémit même en plan fixe**, des formes ombrées par des **hachures, des hachures croisées, du crayon de couleur ou du pointillé**, toujours à l'intérieur de la forme, un grain de papier. **Deux mondes** bien distincts : le **monde de jour** (papier crème, bois, encre brune) et le **monde de nuit**, « à l'intérieur de la machine » (bleu nuit, lignes pervenche, accents lumineux). On passe de l'un à l'autre par un **iris**.
- **Marche pour** : expliquer un logiciel, une automatisation, « ce qui se passe quand tu cliques », un avant/après, une mission pas à pas, un sujet technique rendu chaleureux.
- **Ne marche pas pour** : luxe, émotion pure, photo de produit, sujet enfantin.
- **Héros changé** : la source mettait en scène un point terre cuite marqué d'un astérisque, très proche de l'identité d'une marque d'IA connue. **Il n'est pas repris.** Le héros de cette fiche est une **petite plume d'encre** (une goutte à pointe, avec deux yeux), dans la couleur d'accent de la chaîne du client.

## 2. Palette, typographie, matières

| Monde de jour | Hex | Monde de nuit | Hex |
|---|---|---|---|
| Encre | `#3a2417` | Fond | `#0c0d1c` / `#15173a` |
| Papier / crème | `#f4ecd9` / `#efe5cf` | Lignes | pervenche `#c8d0f0` |
| Bois | `#d6a466` | Accent froid | cyan `#52d6c4` |
| Jaune, vert | `#f0c55a`, `#5f9c5c` | Accent chaud | magenta `#e0368f` |
| Rouge, ciel, rose | `#d4382c`, `#9cc4d6`, `#d98b8b` | Lueur | vert `#5de37a` |

- **Héros (plume d'encre)** : par défaut vert sapin `#2f7d5c` le jour, `#5de3a8` avec un halo la nuit ; remplace par la couleur de la fiche « ma chaîne ». Cette couleur n'est utilisée **que** pour lui.
- **Les tirets de crayon rouge** `rgba(212,56,44,0.92)` veulent dire **« un plan »** (ce qu'on prévoit), jamais autre chose.
- **Attention à la porte de livraison** : le monde de nuit est bleu nuit, pas bleu-violet saturé ; garde les fonds très sombres et peu saturés, et limite le magenta à un accent.
- **Typographie** (OFL) : écriture manuscrite (**Caveat** ou **Patrick Hand**) pour les notes et légendes ; une police à chasse fixe (**JetBrains Mono** ou **IBM Plex Mono**) pour le code tapé caractère par caractère.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Caveat et de Patrick Hand ; JetBrains Mono, IBM Plex Mono : déjà fournies. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/caveat`, `@fontsource/patrick-hand` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La police de la marque ou de la chaîne vient du client : à vérifier (licence, accents français).
- **Matières** :
  - *Trait* : tracé tremblé retiré au hasard à chaque pas de frémissement ; il peut s'écrire progressivement ; double passage possible.
  - *Remplissage* : aplat, puis textures **découpées dans la forme** (hachure avec angle, écart et longueur de tiret ; hachure croisée ; crayon de couleur ; pointillé), puis le contour à l'encre.
  - **Ombre par densité** : la hachure se resserre selon une fonction de la position ; lumière en haut à gauche, plus dense vers le bas à droite. Jamais d'aplat seul, sauf le papier.
  - *Grain* de papier sur chaque image.

## 3. Composition 9:16

- Zone de contenu : **x 60 à 940, y 250 à 1500**.
- Monde de jour : un plan de travail vu de face ou de dessus (bureau, feuille, tasse, écran dessiné), sujet au centre.
- Monde de nuit : gros plans **agrandis d'environ 1,2×** pour remplir la zone lisible d'un téléphone ; lignes claires sur fond sombre, peu d'éléments.
- **Étiquettes d'action** : de petites pastilles qui nomment ce que fait la machine (« Lire », « Chercher », « Écrire » + le nom du fichier ou de l'objet). Elles rendent les étapes lisibles, et **doivent être vraies**.
- Légende manuscrite sur une bande de papier : 60 à 72 px, 2 lignes au plus, y ≈ 1340 à 1480. Texte dans le monde ≥ 50 px.
- Le héros garde sa couleur dans les deux mondes ; ≥ 120 px.

## 4. Ce qui bouge

- **Action principale** : montrer **le plan d'abord** (tirets rouges), puis **la même chose faite pour de vrai** (encre). Ce doublet est la signature narrative du style.
- **Boucle de fond 1** : **le trait frémit** toutes les 2 images (petite surface seulement : des traits, jamais un aplat), même en plan fixe : le dessin vit quand rien ne bouge.
- **Boucle de fond 2** : dans le monde de nuit, des accents qui pulsent (lueur verte, curseur, signaux le long d'une ligne) ; dans le monde de jour, vapeur d'une tasse, lumière qui tourne.
- **Autorisés** : `#004` tracé de ligne (lignes, plans, écriture), `#006` machine à écrire (code), `#136` trait qui frémit, `#128` saccadé, `#188` iris (entrée et sortie du monde sombre), `#017` transition par masque rond, `#003` éclat (au résultat), `#046` coupe franche sur le temps.
- **Interdits** : aplat sans texture, trait parfaitement immobile, `#044` fondu, dégradé lisse, faire disparaître un objet en le rendant transparent (les textures cassent la transparence : on le retire d'une image à l'autre), pastilles d'action inventées.

## 5. Rythme et montage

- Un dessin toutes les 2 images. Montage **sur le temps** : choisis un tempo où la croche tombe sur un nombre entier d'images (à 30 i/s : 112,5 BPM, croche = 8 images ; ou 150 BPM, croche = 6 images).
- Coupes sur les croches ; doubles-croches dans les passages pressés.
- Plans de 1,5 à 4 s ; durée type 15 à 35 s. Structure éprouvée : une **mission** (un but, une aide, des étapes, une échéance).
- Iris vers le monde sombre quand on « entre dans la machine », iris retour pour le résultat.
- **Version courte (8 à 12 s)** : la mission en trois plans : le but (2 s), une étape (3 s), l'échéance tenue (3 s).

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D, `renderAt(t)`.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `encre.js` (trait tremblé, tracé progressif), `peindre.js` (aplat + textures découpées + contour), `textures.js` (hachure, croisée, crayon, pointillé, grain), `mondes.js` (feuille, bois, monde sombre, iris), `accessoires.js` (tasse, tissu rayé, fiche, pastille d'action, plan en tirets), `heros.js`, `scenes.js`.
- **Techniques clés** :
  ```js
  const B = Math.floor(t * 15);                                   // frémissement toutes les 2 images
  encre(points, { w: 4, couleur: ENCRE, tremble: 1.5, cle: "tasse", part: p });
  peindre(points, { fond: BOIS, tex: [
    { type: "hachure", angle: -0.6, ecart: 9, dens: (x, y) => clamp((x + y) / 900, 0, 1) },
    { type: "crayon", couleur: JAUNE } ] });
  // texture ancrée au monde : sa clé ne dépend pas de la position à l'écran
  ```
- **Pièges** :
  - Les fonctions de remplissage et de hachure remettent la transparence à 1 : on ne fait pas un fondu d'objet avec elles.
  - Une texture dont la clé dépend de l'écran « glisse » pendant un panoramique : ancre-la au monde.
  - Les deux mondes qui se ressemblent sur la planche de contrôle : vérifie qu'on les distingue d'un coup d'œil.

## 7. Son

- **Musique** : rythmique légère et précise (basse ronde, claquements, clavier électrique), calée sur la grille d'images ; elle se resserre dans le passage pressé.
- **Bruitages** (≈ 5 par 10 s) : plume qui gratte (texture basse), touches de clavier pour le code, « clic » feutré pour une pastille d'action, souffle grave à l'iris, petit éclat au résultat.
- **Silence avant le résultat** : baisse nette juste avant, le résultat tombe seul.
- Voix off possible, posée ; chaque étape démarre ≈ 0,3 s après la fin d'une phrase. Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] **Chaque forme remplie a une texture** (hachure, croisée, crayon ou pointillé) modelée par la lumière ; aucun aplat sauf le papier.
- [ ] **Le trait frémit** : jamais une ligne parfaitement fixe dans un plan tenu.
- [ ] **Les pastilles d'action sont lisibles et vraies.**
- [ ] **Les deux mondes se distinguent** sur une planche : bleu nuit + lignes pervenche dedans, crème + encre dehors.
- [ ] **Le héros garde sa couleur** dans les deux mondes (avec un halo dans le sombre) ; ce n'est **ni** un point terre cuite **ni** un astérisque.
- [ ] **Textures ancrées au monde** pendant les mouvements de caméra.
- [ ] Le plan (tirets rouges) est montré avant l'action (encre).
- [ ] Contenu dans x 60 à 940, y 250 à 1500 ; gros plans sombres agrandis ≈ 1,2×.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 9
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Image d'exemple d'origine : `plugins/animate/skills/animate/styles/crosshatch/sample.png` (540×960), planche `docs/styles.png`, dépôt https://github.com/cth9191/animate (MIT, © 2026 cth9191). Démo construisible `styles/crosshatch/demo/` (6 s ; pas de vidéo dans le dépôt).
- L'image d'origine et l'exemple `examples/history-of-ai` montrent le héros d'origine et citent des produits tiers : **à ne pas utiliser comme vitrine**. Produire notre propre aperçu 9:16 avec le nouveau héros.

## 10. Origine

- **cth9191/animate**, commit `7e5eb56` (version 0.4.0) : `plugins/animate/skills/animate/styles/crosshatch/STYLE.md`, `kit.js`, `kit/core.js`, `grammar/FRAME.md`. Licence MIT, © 2026 cth9191.
- Adaptation Flot Web : traduction, **héros remplacé** (forme et couleur), pastilles d'action généralisées (la source les liait à un outil précis), polices libres, tempo recalculé pour 30 i/s, portage prévu vers HyperFrames, numéros du dictionnaire de mouvements.
