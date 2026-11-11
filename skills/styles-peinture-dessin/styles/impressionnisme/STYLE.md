# Impressionnisme

## 1. Identité

- **Nom** : Impressionnisme.
- **Inspiration** : la peinture de plein air des années 1870 : petites touches côte à côte, couleurs claires, pas de contour, la lumière comme vrai sujet.
- **Ce que c'est** : l'image entière est refaite en **touches courtes pastel dont la position ne change jamais**. Ce qui vit, ce n'est pas la touche : c'est **la lumière** : des taches de soleil qui dérivent et s'allument, des fleurs qui se balancent, des nuages qui passent. Aucun contour : les formes se séparent par la couleur.
- **Marche pour** : douceur, printemps, jardin, famille, bien-être, artisanat, fleuriste, mariage, souvenir heureux.
- **Ne marche pas pour** : texte à lire, schéma, visage à reconnaître (défaut connu : les touches cassent visages et mains), sujet sombre ou technique.
- **À ne pas confondre** : `tourbillons-van-gogh` a un contour et des directions marquées ; `pointillisme` a des points ronds de même taille ; `nympheas` est la variante « eau » de ce style.

## 2. Palette, typographie, matières

- Palettes par zone (valeurs de la source) : mur ou fond clair en dégradé `#d8bede` → `#f0c8cc` → `#f2c4d4` ; mur au soleil : 7 jaunes crème ; sol : 7 roses, orangés et violets ; ciel, vert d'herbe, rideau lilas, nappe bleu-violet : un jeu chacun. Toile sous les touches : `#f2e6ee` (elle se voit dans les interstices).
- Lumière : touches jaune-blanc très claires `#fffbe8` `#fdf0d0`.
- **Les ombres sont colorées** (violettes, bleues), jamais grises ni noires. Les rouges vifs (coquelicots) gardent leur couleur d'origine : on ne les repasse pas dans la palette.
- **Typographie** : serif douce (**Cormorant Garamond**, OFL) sur une bande de toile claire ; pas de texte peint en touches.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de Cormorant Garamond. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/cormorant-garamond` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : touches ≈ 20 px de long × 7 de large pour l'image principale, ≈ 11 × 4,5 pour les lointains et les détails (fenêtre, tableau dans le tableau). Variation de couleur forte d'une touche à l'autre. **Aucun contour.**

## 3. Composition 9:16

- Lumière qui vient d'un coin haut : une grande zone ensoleillée (diagonale) et une zone d'ombre colorée. Horizon ou ligne de table vers y ≈ 1100.
- Un lointain détaillé (jardin, rue, rivage) dans le tiers haut, peint en **touches deux fois plus petites** pour rester lisible.
- Sujet ≥ 1/3 de la hauteur ; garde les visages **assez grands** (tête ≥ 220 px) et n'y mets que les traits essentiels, en fin trait lilas.
- 20 à 30 taches de soleil : la plupart sur le sol et la table (y 1000 à 1500), quelques-unes sur le sujet.
- Sous-titres : serif 48 à 54 px, texte sombre sur bande claire unie, y ≈ 1400 à 1520. Rien d'important à droite de x = 945.

## 4. Ce qui bouge

- **Action principale** : le geste du sujet (servir, cueillir, marcher), simple et lent.
- **Boucle de fond 1** : **les taches de soleil** : chacune a une intensité `0,5 + 0,5·sin(t·v + φ)·sin(t·v·0,53 + 2φ)` (rythme irrégulier), dérive lentement de côté (±10 à ±44 px), et est faite d'une quarantaine de courtes touches jaune-blanc.
- **Boucle de fond 2** : le vent : fleurs dont la tête se balance (la base de la tige reste fixe), nuages qui glissent (≈ 45 px/s), rideau ou feuillage qui ondule, ruban qui flotte.
- **Autorisés** : `#096` flottement doux, `#016` parallaxe légère entre lointain et premier plan, `#027` avancée lente, `#025` panoramique lent, `#175` plan fixe, `#103` lumière dorée.
- **Interdits** : frémissement de toute l'image (`#136` appliqué partout), `#046` coupe brutale, `#024` secousse, contours, noir pur, `#022` balayage de lumière dur.
- **Transition signature** : des touches de couleur recouvrent l'image jusqu'à la remplacer.

## 5. Rythme et montage

- Calme : plans de 5 à 8 s, caméra presque immobile.
- Transition par recouvrement de touches (≈ 0,6 s) ou coupe douce sur un temps faible.
- Le « vivant » vient des mouvements locaux, jamais du grouillement : vise un écart moyen entre deux images consécutives **faible et régulier**.
- **Version courte (8 à 12 s)** : un seul plan de 8 à 10 s : la lumière change avant 3 s (les touches basculent de teinte), un passant ou un reflet traverse ; pas de transition.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D. ≈ 70 ms par image en 1080p (deux passes plein écran + une passe sujet).
- **Chaîne de rendu** :
  1. Esquisse en aplats, **redessinée à chaque image** (fleurs, nuages, rideaux bougent).
  2. Touches en **deux passes** : image principale (grosses touches) avec un masque qui exclut les lointains ; puis lointains et détails (petites touches) dans ce masque.
  3. Champ de directions : mur en biais vers la lumière, sol presque horizontal, tissus verticaux, plante en rayons depuis son pot, ciel horizontal.
  4. Sujet : aplat, puis petites touches limitées à sa silhouette, puis les traits du visage en fin trait lilas.
  5. Taches de soleil et reflets par-dessus, en opacité forte (≈ 0,95) : en mode « écran » sur fond clair, elles ne se voient pas.
- **Techniques clés** :
  ```js
  // position des touches FIXE : un tirage par case, indépendant de la couleur dessous
  const h = hash(i, j);                       // i, j = indices de la case de la grille
  const teinte = palette[Math.floor(h * palette.length)];
  // tache de soleil : rythme irrégulier
  const I = clamp(0.5 + 0.5 * Math.sin(t * v + ph) * Math.sin(t * v * 0.53 + 2 * ph), 0, 1);
  ```
- **Pièges** :
  - **Graine fixe ne suffit pas** : si le tirage au hasard dépend de la couleur de l'esquisse, une fleur qui bouge décale tous les tirages suivants et tout l'écran se relave. Un tirage **par case**.
  - Une seule passe de grosses touches efface les lointains : deux passes.
  - Les blancs (cadre de fenêtre, robe) sont repeints de la couleur du mur : détecte-les et ramène-les au blanc.
  - Un trait sombre par défaut laisse des barres noires près du visage : règle la couleur de trait sur celle des cheveux ou du vêtement.

## 7. Son

- **Ambiance** : jardin, oiseaux, feuillage, eau lointaine, pièce ouverte.
- **Musique** : piano clair, harpe, flûte, cordes légères ; tempo lent, harmonie lumineuse.
- **Bruitages** (≈ 5 par 10 s) : tissu, porcelaine, pas dans l'herbe, un souffle de vent quand une tache de soleil passe sur le sujet.
- Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défaut connu de la source (noté deux étoiles) : **visages et mains cassés par les touches**. Erreurs : tout l'écran qui se relave ; lointains illisibles ; ombres grises ; contours.

- [ ] Sur un plan fixe, les touches du fond ne changent pas d'une image à l'autre.
- [ ] Les lointains sont peints en touches deux fois plus petites et restent lisibles.
- [ ] Aucun contour ; aucune ombre grise ou noire.
- [ ] Les taches de soleil s'allument à un rythme irrégulier et dérivent.
- [ ] Visage ≥ 220 px, traits fins ajoutés après les touches.
- [ ] Les blancs sont restés blancs.
- [ ] Au moins deux mouvements de vent différents dans chaque plan.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : fixe
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 48

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt. Planche commune `assets/全风格总览.jpg` : composition empruntée, à ne pas utiliser comme vitrine. Film complet : Releases de https://github.com/alchaincyf/huashu-art-motion. Image fixe possible avec le moteur d'origine (`render.py --solo 08_impressionism --stills`, non exécuté ici).
- À produire : notre propre aperçu 9:16.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/08_impressionism.md` (deux étoiles), `scripts/engine/scenes/08_impressionism.js`. Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : carte traduite et généralisée (elle décrivait une pièce précise et rendait hommage à des toiles : non repris), section 9:16, numéros du dictionnaire de mouvements, son.
