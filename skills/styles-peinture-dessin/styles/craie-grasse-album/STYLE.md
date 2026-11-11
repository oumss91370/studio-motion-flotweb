# Craie grasse, album jeunesse

## 1. Identité

- **Nom** : Craie grasse, album jeunesse (« Crayon Picture Book »).
- **Inspiration** : les albums pour enfants dessinés à la craie grasse et les films d'animation à texture crayonnée des années 1980 (images qui respirent, tendresse sans paroles, un passage lyrique porté par une seule mélodie). On emprunte la grammaire, jamais un personnage, une chanson ou une image.
- **Ce que c'est** : une page d'album **en train d'être dessinée** : craie grasse sur papier chaud à gros grain, une petite boîte de craies, une perspective d'enfant, la couleur qui déborde du contour, et chaque trait qui frémit parce que chaque image est un nouveau dessin. Dessiner et colorier **sont** l'histoire : n'importe quel sujet devient « une page qu'on termine ».
- **Marche pour** : histoire pour enfants, message d'association ou d'école, remerciement, bilan d'une année, produit familial, souvenir, mot doux d'une marque.
- **Ne marche pas pour** : données chiffrées, interface logicielle, luxe, sujet anxiogène, texte abondant.
- **À ne pas confondre** : ce n'est pas du vectoriel mignon avec un filtre ; pas un tableau blanc (ni feutre ni main) ; pas une aquarelle (le lavis est l'invité, la craie est l'hôte).

## 2. Palette, typographie, matières

- **Une boîte d'une douzaine de craies au maximum.** Contours dans **une** couleur sombre (indigo, brun foncé, prune), **jamais en noir**. Une craie blanche réservée à l'effet de réserve.
- **Une seule aquarelle par vidéo**, choisie pour ce qu'elle révèle (outremer pour la nuit, rose pour l'aube, vert sève pour la pluie). Elle ne peint jamais les personnages.
- Exemples de boîtes : *bord de mer* : trait marine `#26315f`, corail `#ec6f5a`, sable `#e8d3a2`, sarcelle `#2f8f8a`, turquoise `#63c7c2`, citron `#f6dc5a`, blanc ; *verger* : trait brun `#4a3428`, roux `#b5562c`, rouge pomme `#cf3a2e`, moutarde `#d9a441`, olive `#7d8a3a`, prune `#6a3b5c`, crème `#f3ead6`, blanc. Papier : `#f4efe3`.
- **Typographie** (polices libres OFL) : sous-titres en **Patrick Hand**, titres lettrés à la main en **Gaegu Bold**.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Patrick Hand et de Gaegu. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/patrick-hand`, `@fontsource/gaegu` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers, sauf mention ci-après) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. Attention : Gaegu n'a aucune lettre accentuée (fichier latin du paquet : 98 caractères, contrôlé le 11/11/2026) : pour un titre en français, prendre Patrick Hand ou Caveat.
- **Matières** (le cœur du style est une physique, pas un filtre) :
  - *Papier* : grain à trois octaves de bruit plus un terme de fibres horizontales, **ancré à la page** (il suit la caméra), léger relief éclairé d'en haut à gauche, marbrure ±2 %, vignettage chaud.
  - *Adhérence de la cire* : chaque couche de craie est un canvas où la couleur est dans RVB et la **pression dans l'alpha**. La cire ne se dépose que sur les sommets du grain : pression légère = sommets mouchetés ; pression forte = presque plein, un peu plus sombre.
  - *Trait* : ruban au tremblé basse fréquence (1 à 2 px), largeur ±15 %, bouts effilés, cœur plus dense.
  - *Coloriage* : hachures en zigzag avec un jour visible, chaque passe à une pression différente, **débord de quelques pixels** hors du contour.
  - *Lavis* : canvas de densité multiplié sur la page ; le pigment s'accumule au bord, granule dans les creux, et **est repoussé par la cire** (densité × (1 − 0,9 × couverture de cire)).
  - *Personnages* : un adulte habile qui imite un enfant : tête ronde (≈ 2,5 têtes de haut), yeux en points avec un reflet de cire blanche, joues roses, membres en tubes, moufles. Maison = pignon de face + mur de côté penché ; les gens sont plus grands que les portes.

## 3. Composition 9:16

- La page est une **feuille verticale** plus grande que le cadre ; la caméra s'y promène. Un album tient très bien en hauteur : ciel en haut, sol au tiers bas.
- Personnage principal ≥ 1/4 de la hauteur en plan rapproché (≥ 480 px), visage entre y = 500 et y = 1100.
- **Garde du papier nu en bas** (y 1340 à 1560) pour les mots imprimés de l'album : ce sont les sous-titres. Patrick Hand 56 à 64 px, couleur du contour, centrés, chaque lettre un peu penchée, écrits de gauche à droite en ≈ 0,35 s, sur une tache de papier vierge aux bords irréguliers (jamais une boîte sombre). Tenue ≥ max(1,8 s ; durée de la réplique + 0,6 s). Aucun mot pendant un passage musical sans paroles.
- Rien d'important à droite de x = 945 ni au-dessus de y = 160. 16:9 : même page, cadrée en largeur, mots en bas au centre.

## 4. Ce qui bouge

- **Action principale** : le monde se dessine juste devant le héros, puis se colorie ; **colorier est une action** (un manteau gribouillé = on l'enfile ; un gribouillis rose = on rougit ; un lavis = la nuit tombe).
- **Boucle de fond 1** : frémissement du trait : chaque trait retire son décalage (< 1 px) et ses rangs de hachures toutes les 2 images (petite surface seulement : des traits). Personnages à 100 %, traits du décor à 60 %, coloriage du décor **immobile**. On le calme de moitié quand le film se tait.
- **Boucle de fond 2** : petite vie du papier : un scintillement d'étoile, le bord humide du lavis qui avance.
- **Jeu** : par substitution, un nouveau dessin par pose, sur le temps ; deux dessins qui alternent pour une action répétée. Grandes poses simples : un dessin d'enfant n'a pas d'intervalles.
- **Autorisés** : `#004` tracé de ligne (0,4 à 0,9 s par trait), `#136` trait qui frémit, `#128` saccadé façon image par image (15 dessins par seconde), `#140` page qui tourne, `#027` avancée vers un personnage, `#026` panoramique vertical le long d'un regard, `#029` travelling serré qui suit, `#175` plan fixe pendant que le pinceau passe.
- **Interdits** : `#044` fondu enchaîné, `#012` métamorphose lisse, `#010` dépassement élastique d'interface, `#022` balayage de lumière, `#015` particules. Un titre ne s'efface pas en fondu : on ne peut pas faire disparaître de la craie. Il sort parce que la caméra le quitte, qu'une page tourne ou qu'on colorie par-dessus.

## 5. Rythme et montage

- Tout ce qui est dessiné avance à **15 dessins par seconde** (à 30 i/s : une image sur deux ; 12 seulement dans un film livré à 24 i/s) ; la caméra, le bord du lavis et les scintillements sont fluides à 30 i/s.
- Plans de 4 à 8 s, lents et menés par la musique. Quelques phrases de narration seulement.
- Transitions propres au style : un tracé, un coloriage par-dessus, le lavis, un panoramique, une page qui tourne. Jamais de fondu.
- Un silence d'un temps entier après un échec ; une respiration avant un passage sans paroles.
- Place l'effet de réserve (le message à la craie blanche que le lavis révèle) au pic émotionnel, et cache-le dans l'image dès la première seconde.
- **Version courte (8 à 12 s)** : deux plans de 4 à 5 s (ou une page et son coloriage) et une seule phrase de narration. Accroche : le premier trait de craie à l'image 0.

## 6. Recette technique

- **Moteur** : HyperFrames ; canvas 2D pour les couches de craie, puis une passe WebGL2 qui compose papier, adhérence, réserve et lavis. `renderAt(t)` comme dans le `SKILL.md` de la catégorie.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `papier.js` (grain ancré), `craie.js` (rubans effilés, hachures avec débord, texte), `rig.js` (pièces qui s'occultent, membres en tubes), `compose.glsl` (cire, lavis, relief), `scenes.js`, `timeline.js`.
- **Techniques clés** :
  ```glsl
  // la cire accroche les sommets du grain : pression dans l'alpha de la couche
  float depot = smoothstep(1.0 - k * pression, 1.0 - k * pression + 0.08, grain);
  // le lavis est repoussé par la cire
  float lavis = densite * (1.0 - 0.9 * couvertureCire);
  ```
  ```js
  const tq = Math.floor(t * 15) / 15;              // temps des dessins
  const graine = Math.floor(t * 15);               // frémissement : toutes les 2 images à 30 i/s
  ```
  - *Occultation* : une pièce de devant efface ce qui est derrière elle à l'intérieur de son contour ; un personnage « garde le papier blanc » derrière lui (comme un enfant qui dessine le bonhomme d'abord et colorie autour).
  - Dessine la feuille de modèle du personnage avec le vrai moteur avant le premier plan.
- **Pièges** :
  - Jours entre deux bandes de lavis = rayures blanches : fais chevaucher les bandes.
  - Coloriage à pression légère sous un lavis = boue : pression ≥ 0,8 ou double hachure là où le lavis passe.
  - Un texte placé sur le trajet du lavis lui survit (la cire résiste) : place-le ailleurs.
  - Les personnages disparaissent sous le lavis : compose-les **après**.
  - Contour sur les cheveux = serre-tête : ne trace que le bord extérieur de la masse.
  - Grain fixe à l'écran ou coloriage du décor qui frémit : le fichier gonfle et l'image grouille.

## 7. Son

- **Musique** : petits instruments de bois et de lames, **ni cordes ni piano à queue** : ukulélé ou guitare nylon, clarinette ou basson (basse, humour), boîte à musique (qui peut ralentir en baissant de ton), glockenspiel ou célesta (une note par étincelle), piano jouet (une note par chose comptée), flûte à bec comme voix qui chante, shaker, woodblock. Un thème simple, joué en entier une seule fois.
- **Bruitages** (≈ 5 par 10 s) : la craie = frottement granuleux dont le grain suit la vitesse du trait (colorier = frottements rythmés) ; pinceau mouillé = souffle doux, placé à gauche ou à droite selon le geste ; une craie qu'on pose, un taille-crayon, une page qui tourne. Ambiance très basse : grillons ou oiseaux, pièce calme.
- **Voix** : une conteuse douce, phrases courtes avec des respirations ; quelques décibels au-dessus de la musique, jamais plus. Évite les formules de livres célèbres. Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : filtre « crayon » sur du vectoriel ; contours noirs ; trop de couleurs ; tout qui frémit autant ; fondus ; texte typographié.

- [ ] Douze craies au plus, contour d'une seule couleur sombre, aucun noir.
- [ ] En gros plan, le grain du papier se voit **à travers** la craie légère.
- [ ] La couleur déborde du contour de quelques pixels.
- [ ] Le grain suit la caméra (arrêt sur deux images d'un panoramique : le grain a bougé avec la page).
- [ ] Les personnages frémissent, le coloriage du décor est immobile.
- [ ] Une seule aquarelle, jamais sur un personnage ; la craie blanche repousse le lavis.
- [ ] Les mots sont sur du papier nu en bas, écrits lettre à lettre, hors de la zone y > 1560.
- [ ] Aucun fondu enchaîné.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 14
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Film de démo d'origine *The Moon Can't Sleep* (52 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/crayon-book.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/crayon-book.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/crayon-book.jpg
- Galerie : https://lemomo-ai.github.io/lemo-opuscar/#hand-drawn-painting
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre l'histoire, les plans ni les personnages.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/crayon-book/STYLE.md`, `DEMO.md`, `demo/gl.js` (compositeur : papier, cire, réserve, lavis), `crayon.js`, `rig.js`, `sheet.js`, `end.js`. Licence MIT (code et textes), © 2026 LemoLab ; film et images CC BY 4.0.
- Adaptation Flot Web : traduction, section 9:16, numéros du dictionnaire de mouvements, budget de bruitages.
