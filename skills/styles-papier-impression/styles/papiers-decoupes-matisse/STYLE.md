# Papiers découpés (style Matisse)

## 1. Identité

- **Nom** : Papiers découpés (style Matisse, gouaches découpées des années 1940). Inspiration seulement : aucune œuvre recopiée, jamais présenté comme officiel ; le nom n'apparaît pas dans la vidéo.
- **Inspiration** : les grandes compositions en papiers gouachés découpés : des formes simples taillées directement aux ciseaux, des couleurs pures côte à côte, des algues et des feuilles, des figures réduites à une silhouette, un damier de deux bleus.
- **Ce que c'est** : **« dessiner avec des ciseaux »**. Chaque forme est une feuille de papier peinte à la gouache, découpée d'un geste, **épinglée** sur le fond. Trois signes : le **bord aux ciseaux** (une suite de petits segments droits, jamais une courbe lisse) ; l'**ombre d'épingle** (une ombre courte et douce : le papier n'est pas collé à plat) ; les **traces de brosse** de la gouache dans les aplats saturés.
- **Marche pour** : identité joyeuse, mode, décoration, musique, danse, été, festival, carte de vœux, fond animé pour une citation, logo qui se compose.
- **Ne marche pas pour** : explication, données, visage reconnaissable, sujet grave, texte abondant.
- **À ne pas confondre** : `papier-decoupe-collage` a des bords **déchirés**, des motifs, des personnages à visage et une narration ; ici : **ciseaux**, aplats purs, formes presque abstraites. L'illustration plate contemporaine est dans `styles-graphique-typo`.

## 2. Palette, typographie, matières

| Rôle | Hex (source) |
|---|---|
| Deux bleus du damier | `#1d4fb8`, `#4f95dc` |
| Vert émeraude | `#1f9a5a` |
| Bleu de cobalt (fond d'un panneau) | `#1e44a8` |
| Noir (silhouette, bande) | `#141414` |
| Rouge (un cœur, une jupe) | `#d8322a` |
| Jaune (étoiles, siège) | `#f4c81e` |
| Blanc de papier (oiseaux, chemise) | `#fbf8f0` |
| Rose (une feuille qui tombe) | `#f2a0b4` |

- **Aplats saturés, posés bord à bord.** 5 à 7 couleurs par plan, dont le noir et le blanc. Pas de dégradé, pas de contour.
- **Attention à la porte de livraison** : le damier bleu peut dominer. Ce sont des bleus francs (≈ 215°), pas du bleu-violet ; équilibre tout de même avec le vert, le jaune et le rouge.
- **Typographie** : lettres **découpées** : capitales simples un peu irrégulières (pars d'une sans-serif grasse comme **Jost 800** ou **Outfit 800**, OFL, et passe le contour dans la fonction « ciseaux »), ou une écriture au pinceau (**Caveat Brush**). Le texte repose sur un **morceau de papier blanc découpé**, sinon il se perd sur le bleu.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Outfit à la place de Jost ; Nunito à la place de Caveat Brush ; Outfit : déjà fournie. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/jost`, `@fontsource/caveat-brush` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** :
  - *Bord aux ciseaux* : un point tous les 14 à 24 px le long du contour, décalé de ±2 à 2,5 px (graine fixe), reliés **en ligne droite**.
  - *Ombre d'épingle* : décalage (5, 6) px, flou 4 px, `rgba(10,20,40,.3)`.
  - *Gouache* : ≈ 2 600 traces longues (60 à 300 px, 6 à 22 px de large, moitié claires moitié sombres, opacité 0,04 à 0,13, légèrement penchées), mises en cache et posées sur toute l'image en mode « incrustation ». Reste léger : c'est le défaut connu (traces trop lourdes).
  - *Figures* : silhouettes ; un visage se réduit à des **fragments de papier** (œil en amande noir, bouche en triangle rouge, joue en rond rose).

## 3. Composition 9:16

- **Panneaux** : le vertical se découpe bien en 2 ou 3 grands rectangles de couleur empilés (un damier de deux bleus en haut, un panneau cobalt au milieu, une bande verte et une bande noire en bas). Cases du damier ≈ 240 px.
- Sur ces fonds, **6 à 12 grandes formes** : algues, feuilles, étoiles, oiseaux, une silhouette. Formes **grandes** (200 à 500 px), espacées, qui se touchent rarement.
- **Algue** (forme signature) : une tige effilée + des « doigts » arrondis alternés à gauche et à droite ; tous réunis en une seule forme.
- Sujet principal ≥ 1/3 de la hauteur, au centre gauche. Rien d'important à droite de x = 945.
- Texte sur un papier blanc découpé, y ≈ 1380 à 1520, 56 à 72 px, peu de mots.

## 4. Ce qui bouge

- **Action principale** : les papiers **arrivent et se posent** (glissent, tournent, se retournent), ou une silhouette danse par grandes poses.
- **Boucle de fond 1** : **les algues se balancent comme du papier** autour de leur pied (`sin(2,8·t + φ)·0,13` rad) ; leur bord « respire » (largeur entre 0,93 et 1).
- **Boucle de fond 2** : étoiles qui tournent et scintillent (échelle `0,82 + 0,22·sin(7·t + 1,9·k)`), un cœur qui bat (`1 + 0,18·max(0, sin(9·t))`), des oiseaux blancs qui battent des ailes (hauteur `0,55 + 0,45·cos(13·t)`), **une feuille de papier qui tombe en se retournant** (largeur = `cos(6·t)`).
- **Autorisés** : `#021` retournement d'une feuille, `#096` flottement, `#127` va-et-vient (balancement), `#125` pulsation, `#001` apparition en rebond léger, `#018` transition par forme (un grand papier balaie le cadre), `#012` métamorphose **par remplacement de papiers**, `#175` plan fixe, `#027` avancée lente.
- **Interdits** : courbes lisses de vecteur, dégradés, contours, ombres longues, `#016` parallaxe profonde, `#022` balayage de lumière, flous, petits détails.
- **Transition signature** : **un grand papier bleu, avec ses découpes épinglées, traverse le cadre** et laisse la scène suivante.

## 5. Rythme et montage

- Dansant : plans de 3 à 6 s, calés sur une musique à pulsation claire.
- Les formes peuvent bouger par paliers (15 par seconde à 30 i/s) pour un effet « posé à la main », ou en fluide pour un effet « flottant » ; choisis l'un et tiens-le.
- Entrées en cascade : une forme par temps ou demi-temps, la plus grande d'abord.
- Très bon en boucle parfaite (fond animé).

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D ; léger (≈ 25 ms par image).
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `ciseaux.js` (contour → segments droits décalés), `formes.js` (algue, feuille, étoile irrégulière, oiseau, silhouette), `papier.js` (ombre d'épingle, couche de gouache en cache), `scenes.js`.
- **Techniques clés** :
  ```js
  // bord aux ciseaux : rééchantillonner le contour, décaler chaque point, relier en droites
  function ciseaux(pts, graine) {
    return reechantillonner(pts, 14, 24, graine).map((p, i) => decaler(p, 2.5 * (hash(graine, i) - 0.5) * 2));
  }
  // algue : tige + doigts en capsules à bout rond, TOUS ajoutés au même tracé, remplis en une fois
  for (let i = 0; i < 2 * lobes; i++) tige.addPath(capsule(base(i), angle(i), longueur(i), largeur(i)));
  ctx.shadowOffsetX = 5; ctx.shadowOffsetY = 6; ctx.shadowBlur = 4; ctx.shadowColor = "rgba(10,20,40,.3)";
  ctx.fill(tige, "nonzero");                          // une seule union, une seule ombre
  ```
  - Pour une figure dessinée avec un rig courbe, donne-lui le bord « ciseaux » en déplaçant les pixels de son calque par un bruit large et fixe (≈ 9 px).
- **Pièges** :
  - **Algue faite en modulant la largeur le long d'une ligne** : on obtient une chenille ou un éclair en zigzag. Il faut la tige + les doigts en capsules.
  - Chaque doigt rempli séparément : les ombres se superposent ; réunis tout dans un seul tracé.
  - Une feuille qui tombe en passant devant le visage du sujet : déplace sa trajectoire.
  - Texte noir directement sur le cobalt : illisible ; glisse un papier blanc dessous.
  - Traces de gouache trop marquées : l'image a l'air sale.

## 7. Son

- **Musique** : jazz léger (contrebasse, balais, piano, clarinette ou trompette avec sourdine), ou percussions et marimba ; pulsation nette, humeur ensoleillée.
- **Bruitages** (≈ 5 par 10 s) : **coup de ciseaux** pour une forme qui apparaît, papier qui glisse ou se pose, petite épingle, froissement doux pour la feuille qui tombe.
- Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défaut connu de la source (trois étoiles) : traces de gouache trop lourdes. Erreurs : courbes lisses ; dégradés ; trop de petites formes ; composition d'une œuvre connue recopiée.

- [ ] En zoom, chaque bord est une suite de petits segments droits.
- [ ] Chaque papier a son ombre d'épingle courte.
- [ ] 5 à 7 couleurs saturées, sans dégradé ni contour.
- [ ] 6 à 12 grandes formes ; aucune forme utile sous 80 px.
- [ ] Les algues ont des doigts arrondis et se balancent autour de leur pied.
- [ ] Au moins trois mouvements de fond (balancement, scintillement, feuille qui tombe).
- [ ] Texte sur un papier blanc découpé, hors y > 1560 et x > 945.
- [ ] Aucune composition existante reconnaissable ; aucun nom d'artiste à l'image.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 9
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt. Planche commune `assets/全风格总览.jpg` : composition empruntée, à ne pas utiliser comme vitrine. Film complet : Releases de https://github.com/alchaincyf/huashu-art-motion. Image fixe possible avec le moteur d'origine (`render.py --solo 30_matisse --stills`, non exécuté ici).
- À produire : notre propre aperçu 9:16.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/30_matisse.md` (trois étoiles), `scripts/engine/scenes/30_matisse.js`. Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : carte traduite et généralisée (la carte citait des œuvres précises pour ses panneaux : non repris), valeurs hex complétées par Flot Web quand la carte ne donnait que des noms de couleurs, section 9:16, son.
