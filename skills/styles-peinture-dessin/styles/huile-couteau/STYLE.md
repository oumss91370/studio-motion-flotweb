# Huile au couteau

## 1. Identité

- **Nom** : Huile au couteau (« Impasto · Palette Knife »).
- **Inspiration** : la peinture de rue au couteau (mosaïque de touches, reflets verticaux sur sol mouillé, lumières chaudes contre ombres froides), les peintres de la touche franche et de la lumière forte, les génériques de comédie musicale filmés du dessus (une chorégraphie lue comme de la couleur en mouvement), le montage calé sur la musique (une action, un son, une coupe). On emprunte la grammaire, jamais une image, une composition ou une mélodie.
- **Ce que c'est** : une peinture à l'huile qui bouge, faite de **coups de couteau**. Chaque touche est un objet réel : un plan de pâte incliné, une arête où la lame a appuyé, une lèvre où elle a décollé, des stries là où la pâte a manqué, deux couleurs traînées l'une dans l'autre. Le monde est repeint à chaque image, mais **la peinture immobile ne bouge pas** : seul bouge ce que l'histoire fait bouger. Une lumière rasante passe sur un relief : la pâte a du corps.
- **Marche pour** : ambiance, ville sous la pluie, saison, artisan, restaurant, souvenir, relance d'une marque, film musical sans voix.
- **Ne marche pas pour** : petit texte, schéma, interface, sujet très rapide, visages détaillés.
- **À ne pas confondre** : pas un filtre de tourbillons (les touches ne grouillent pas) ; pas une texture de pinceau sur du vectoriel ; pas de l'aquarelle (la pâte est opaque) ; pas un filtre « peinture » sur une photo (les touches sont dessinées, pas tirées du bruit).

## 2. Palette, typographie, matières

- **Les valeurs d'abord** : compose chaque décor comme une illustration à plat en **3 valeurs au minimum**, puis convertis-la en touches. Si elle ne se lit pas à 480 px de large, aucune touche ne la sauvera.
- Structure de température par défaut : **lumière chaude contre ombre froide**. La couleur la plus pure et la plus vive est réservée au sujet (un accessoire, une foule, une source de lumière), jamais au fond.
- Pas de dégradé par mélange de pixels : un dégradé se fait de touche en touche, par paliers.
- Exemples : *coucher de soleil après la pluie* : ciel cobalt `#2f4f9a` → pêche `#f2b38a` → or `#f0c24a`, façades ocre `#c9973f`, accessoires en pleine saturation ; *champ de moisson* : paille `#e3c766`, terre de Sienne `#8a4b2a`, un tracteur vert émeraude `#1f7a5c` ; *cuisine la nuit* : ombres terre d'ombre `#3b2a20`, orange de lampe `#e8892e`, une fenêtre bleu froid `#3a5f9c`.
- **La couleur peut être un événement** : chaque touche garde une version grise et une version couleur. Un monde gris avec une seule exception colorée, ou un monde repeint du gris vers la couleur, est natif.
- **Typographie** : **Cormorant** (OFL) pour les titres, posés au couteau ; le petit texte (crédits, légendes, données) reste du texte net par-dessus la peinture : le couteau ne porte pas les petites lettres.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de Cormorant. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/cormorant` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : touches de couteau plus longues que larges (≈ 1,7 à 3,1 × le rayon en longueur, 0,95 à 1,45 × en largeur), bouts en biais, petite variation d'angle (±13°) et de valeur (±6 %). **Les touches ne franchissent jamais le bord d'un groupe de formes** : les silhouettes restent nettes. Sous-couche fine (l'illustration de référence floutée de ≈ 1,5 px) pour que la toile ne perce jamais en liserés. Reflets (sol mouillé, vitre, eau) = **empilements de petites touches horizontales** sous chaque lumière, jamais un rectangle peint.

## 3. Composition 9:16

- Le vertical convient bien aux **reflets** : lumière en haut, sa colonne de touches reflétées en bas. Horizon vers y ≈ 800 à 900.
- Le sujet reçoit les bords durs et les plus petites touches ; tout le reste reste en grands plans calmes. Sujet ≥ 1/3 de la hauteur aux moments clés.
- **La caméra reste à l'intérieur de la plaque peinte** : prévois une plaque plus grande que 1080×1920 (au moins 1,3× dans le sens du mouvement), sinon la toile apparaît au bord.
- Sous-titres (s'il y a une voix) : serif simple, 46 à 52 px, 2 lignes au plus, **dans un plan de couleur calme** vers y ≈ 1400 à 1520 ; texte net, pas peint. Titre : peint au couteau, 140 à 200 px de haut, dans le tiers haut (y 260 à 620).
- Rien d'important à droite de x = 945. Pas de grain de film.

## 4. Ce qui bouge

- **Action principale** : ce que l'histoire déplace (une silhouette, un parapluie, un ruban, la lumière), chaque geste avec anticipation, action et suivi, posé sur un temps musical.
- **Boucle de fond 1** : la météo ou la lumière (pluie, reflets qui se brisent, soleil qui tourne).
- **Boucle de fond 2** : de petites figures peintes au second plan (passants, feuillage), reconstruites à chaque image à partir de **graines fixes** pour que leur pâte ne grouille pas.
- **Gestes natifs** : la couleur reposée au couteau (une vague repeint du gris vers la couleur, touche par touche) ; l'unique chose colorée ; le mouvement qui peint (un objet qui bouge laisse des touches, vues du dessus ses trajets forment un motif) ; la lumière rasante au pic (elle descend, chaque arête s'allume, puis elle se repose) ; la transition par repeint.
- **Autorisés** : `#027` avancée lente, `#029` travelling, `#026` panoramique vertical depuis un reflet, `#031` grue qui monte en tournant vers une vue du dessus, `#175` plan fixe où seule la lumière bouge, `#043` panoramique filé vers une nouvelle plaque, `#046` coupe sèche sur un temps, `#121` anticipation, `#122` suivi.
- **Interdits** : `#044` fondu enchaîné (deux couches d'arêtes de couteau = boue), `#136` trait qui frémit, `#128` saccadé (ici tout est fluide), `#118` grain de film, `#016` parallaxe de calques nets.

## 5. Rythme et montage

- Fluide, 30 i/s, aucun saccadé : la clarté est la consigne.
- Plans de 3 à 7 s. Option forte : **une action = un son = une coupe**, tout sur la grille musicale.
- Transitions du style : repeint en balayage (les touches du plan suivant se posent sur le précédent en ≈ 1 s, avec un raclement), raclage, coupe franche sur un temps.
- Un vrai silence (musique et ambiance à zéro), contenant au plus un son, juste avant le retour de la couleur ou la lumière rasante.

## 6. Recette technique

- **Moteur** : HyperFrames avec un canvas WebGL : les touches sont dessinées en lots, puis une passe finale applique la lumière rasante sur le relief et l'étalonnage. Rendu en double résolution, réduit ensuite.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `couteau.js` (types de touches : couteau, brosse, tache, ligne ; lots statiques et touches mobiles), `plaque.js` (illustration de référence → touches du grossier au fin, confinées par groupe de formes), `decors.js`, `figures.js` (marche, bras, accessoires en touches à graines fixes), `timeline.js`.
- **Techniques clés** :
  ```js
  // une touche : position, angle, longueur, largeur, couleur, 2e couleur traînée, graine fixe
  touches.push({ x, y, ang, len: 120, wid: 46, c: coul, c2: coul2, type: COUTEAU, graine: i });
  // plaque statique : dessinée une fois, rejouée avec la caméra et un seuil de révélation
  dessinerLot(plaque, { cam, gris: 1, revele: frontDeVague(t) });   // gris → couleur
  dessinerMobiles(figures(t), { gris: 0 });                          // l'exception colorée
  ```
  - Par forme : taille maximale de touche, niveau de détail, direction. Grandes touches dans le ciel et les murs, quelques pixels seulement sur les bords et les visages.
  - Version grise = la luminance des mêmes touches, un peu froide, avec un reste de couleur.
- **Pièges** :
  - Les touches confinées rétrécissent près des bords et laissent un liseré couleur toile : ajoute la sous-couche.
  - L'ordre de peinture compte : peindre le sol après les immeubles couvre leurs pieds.
  - Un rectangle se lit comme un poteau : donne aux silhouettes un fuselage, un bord éclairé et une ou deux touches qui les définissent (épaule, cheveux, poignée).
  - À cette taille de touche, les proportions font l'identité de l'objet : vérifie les silhouettes en vignette.
  - Grain ou compression forte détruisent les arêtes : pas de grain, débit élevé.
  - Touches retirées au hasard à chaque image = grouillement : graines fixes.

## 7. Son

- **Musique** : instruments acoustiques au grain « fait main » : cordes solistes, accordéon, pizzicato, arpèges de harpe, glockenspiel ou célesta pour les éclats, piano, guitare, bois. Un instrument seul pour un monde solitaire, un ensemble pour un monde partagé. Musique et bruitages peuvent porter le film sans narration.
- **Bruitages** (≈ 5 par 10 s) : raclement de couteau à chaque repeint, touches humides, puis les matières de la scène (pierre mouillée, toile, bois, verre). Ambiance en couches : un souffle, des grains proches, un détail distinct.
- **Options** : éclats accordés en arpège montant ; une phrase laissée en suspens que le film résout plus tard ; le son du plan suivant qui entre dans le silence (`#047`).
- Voix éventuelle devant, musique et ambiance baissées d'environ 8 dB. Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : tout qui grouille ; image illisible à plat ; fondus ; grain ; reflets en rectangles ; texte peint trop petit.

- [ ] L'illustration à plat se lit en 3 valeurs à 480 px de large.
- [ ] Une capture agrandie à 100 % montre arêtes, lèvres et stries ; en vignette, l'image reste claire.
- [ ] Deux images consécutives d'un plan fixe : la peinture immobile est identique au pixel près.
- [ ] Les silhouettes sont nettes (aucune touche ne franchit un groupe).
- [ ] La couleur la plus vive est sur le sujet.
- [ ] Les reflets sont des empilements de touches horizontales.
- [ ] Aucun fondu enchaîné, aucun grain ajouté.
- [ ] La toile n'apparaît à aucun bord pendant les mouvements de caméra.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 10
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Film de démo d'origine *The Colour of Rain* (40 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/impasto.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/impasto.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/impasto.jpg
- Galerie : https://lemomo-ai.github.io/lemo-opuscar/#hand-drawn-painting
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre l'histoire ni les plans.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/impasto/STYLE.md`, `DEMO.md`, `demo/engine/impasto.js` (moteur de touches), `demo/engine/plate.js` (référence → touches). Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0.
- Adaptation Flot Web : traduction, section 9:16, numéros du dictionnaire de mouvements, budget de bruitages, cadence 30 i/s (24 i/s dans l'original). L'exemple de code de la source dessinait une étincelle orange à quatre branches : non repris.
