# Pop tramé (style BD des années 60)

## 1. Identité

- **Nom** : Pop tramé (pop art, style bande dessinée imprimée des années 1960). Aucun nom d'artiste dans l'offre ni dans la vidéo ; aucune œuvre, case ou personnage recopié.
- **Inspiration** : le pop art américain qui agrandit la bande dessinée imprimée : **points de trame** réguliers, **gros cernes noirs**, couleurs primaires, bulles et onomatopées ; et les portraits sérigraphiés répétés en plusieurs couleurs.
- **Ce que c'est** : une **case de BD géante**. Tout est « cerne noir épais + aplat » ; les demi-tons (peau, mur) sont des **points de trame à 45°** ; les ombres sont des **hachures noires** ; les reflets, de courts traits blancs. Les émotions sont écrites : bulle de pensée, cartouche « PENDANT CE TEMPS… », onomatopée dans une étoile éclatée.
- **Marche pour** : annonce choc, promotion, lancement, réaction, punchline, avant / après, teaser, vignette de vidéo, « 3 erreurs à éviter ».
- **Ne marche pas pour** : sujet délicat, luxe discret, explication longue, émotion subtile.
- **Atout** : c'est le style le plus **rapide à rendre** du catalogue (≈ 6 ms par image) et l'un des plus faciles.
- **À ne pas confondre** : `dossier-trame` (papier d'archive, tampons, pas de cases) ; `risographie` (encres translucides, sans cerne) ; le comics cosmique (`styles-cartoon`, quadrichromie décalée et bulles d'énergie).

## 2. Palette, typographie, matières

| Rôle | Hex (source) |
|---|---|
| Noir du cerne | `#141414` |
| Papier | `#f3eedb` |
| Bleu | `#2f5cc8` |
| Jaune | `#f7d52c` |
| Rouge / rouge sombre | `#d8232a` / `#a8161c` |
| Blanc | `#fbf8ee` |
| Peau : fond / points | `#fae0cc` / `#e2483c` |
| Cheveux clairs : base / ombre | `#f8d62c` / `#d9a514` |
| Fonds de la grille de portraits | `#9ccf3a`, `#e0359a`, `#2fc0b0`, `#f08a2a` |

- **Trois primaires + noir + blanc**, plus les quatre fonds acides pour la grille répétée. Rien d'autre.
- **Typographie** (OFL) : lettrage de BD en capitales (**Bangers**) pour onomatopées et cartouches : onomatopée rouge avec **contour noir de 12 px** et ombre portée noire de 4 px ; cartouche sur fond jaune cerné de 5 px. Texte courant en capitales de BD plus sages (**Comic Neue Bold** ou **Bangers** réduit).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Archivo Black à la place de Bangers ; Nunito à la place de Comic Neue. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/bangers`, `@fontsource/comic-neue` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** :
  - *Points de trame* : un petit motif répété (une tuile avec un point à chaque coin et un au centre = grille à 45°). Mur : pas de 24 px, rayon 5,6 px, points bleus sur blanc ; peau : pas de 13 px, rayon 3,3 px, points rouges sur fond chair ; grand aplat jaune : points très discrets (pas 14 px, rayon 2,2 px, opacité 0,18). En vertical 1080, augmente ces valeurs d'environ 20 %.
  - *Cerne* : 5 à 6 px partout ; cadre de case de 6 px.
  - *Ombres* : hachures noires de 3,5 px tous les 10 px, découpées dans une ellipse.
  - *Reflets* : gros traits blancs courts.
  - *Chevelure signature* : une masse + des **boucles rondes** ; on trace **tout en noir épais d'abord, puis on remplit tout** : il ne reste que le contour de l'ensemble ; dans chaque boucle, un arc noir en C et un arc doré.
  - Grain de papier léger sur le tout.

## 3. Composition 9:16

- **Une case verticale** cernée de noir (6 px), posée à ≈ 30 px des bords (le cadre est du décor ; tout texte reste dans x 60 à 945, y 160 à 1560), ou **deux à trois cases empilées** séparées par une gouttière blanche de 16 à 20 px.
- Zones : **cartouche de récit** en haut à gauche (y 200 à 300), sujet en plan rapproché au centre (visage ou objet ≥ 1/3 de la hauteur), **onomatopée** dans une étoile éclatée (14 pointes, 420 à 560 px de large) qui déborde d'une case, **bulle** à gauche du sujet (à droite, elle tomberait dans la zone d'interface).
- **Grille de portraits répétés** (2 × 2) : le même visage ou le même produit en quatre jeux de couleurs ; très efficace en vertical dans un carré de 900 px.
- Fond : mur à points bleus, ou jaune uni, avec une bande de couleur au sol.
- Sous-titres : cartouche jaune cerné, capitales 46 à 52 px, y ≈ 1400 à 1520. Rien d'important à droite de x = 945.

## 4. Ce qui bouge

- **Action principale** : une réaction jouée gros (yeux, bouche, geste), ou un objet qui se prépare à bondir : anticipation marquée, puis l'onomatopée explose.
- **Boucle de fond 1** : **la grille de portraits change de couleurs** : les quatre jeux tournent **3 fois par seconde au plus** (case *i* = jeu *(i + pas) modulo 4*). Ne jamais aller plus vite : un changement de couleurs saturées sur une grande surface au-delà de 3 fois par seconde est un clignotement dangereux pour les personnes photosensibles (la source tournait à ≈ 11 par seconde, valeur écartée).
- **Boucle de fond 2** : **les trois points de la bulle de pensée s'allument l'un après l'autre** (cycle de 12 images ; chaque point grossit et saute de 6 px pendant 4 images) ; **l'onomatopée tremble à son arrivée, puis se pose** : pendant 4 images, l'étoile et le mot sautent ensemble (décalage de ±8 px et ±0,03 rad retiré à chaque image), puis le mot **reste immobile au moins 1 s** pour être lu ; ensuite seule l'étoile, derrière lui, peut continuer de trembler faiblement (±3 px, une image sur deux), jamais les lettres. (Au rendu réel du 11/11/2026, un tremblement de 7 images laissait le mot lisible 0,93 s : refusé par le contrôle des textes ; à 4 images, il passe.) ; des traits d'action autour qui pulsent (`0,85 + 0,25·sin(40·t)`).
- **Détails** : vapeur en deux traits noirs ondulés, traits de mouvement en arcs près d'un objet qui remue (≈ 6 allers-retours par seconde).
- **Autorisés** : `#001` apparition en rebond, `#003` éclat, `#024` secousse d'impact, `#121` anticipation, `#124` tremblement (4 images à l'arrivée de l'onomatopée ; ensuite l'étoile seule), `#011` écrasement et étirement, `#144` écran divisé en cases, `#046` coupe sèche, `#008` typo cinétique (onomatopées), `#184` très gros plan sur les yeux.
- **Interdits** : dégradés, ombres douces, `#044` fondu, flou, `#136` trait qui frémit sur tout, trame qui se déplace avec le personnage (elle est **fixe à l'écran**), couleurs pastel, texte en minuscules fines.
- **Transition signature** : **un éclair jaune**, puis l'image se décompose en gros points de trame (≈ 0,16 s).

## 5. Rythme et montage

- **Rapide** : plans de 0,5 à 2,5 s ; c'est un style de **ponctuation**. Dans une vidéo, 1 à 3 cases suffisent ; une vidéo entière fait 8 à 15 s.
- Tout tombe sur le temps : entrée d'une case, onomatopée, changement de couleur de la grille.
- Structure type : cartouche (« PENDANT CE TEMPS… ») → situation → réaction en gros plan → onomatopée → grille de portraits ou produit répété.
- Une tenue de **1 s au moins**, mot immobile, sur l'onomatopée pour qu'on la lise (la source disait 0,8 s : trop court pour le contrôle de lecture du studio). Le film déclare « Texte vivant : oui » (section 8) parce que le mot tremble à son arrivée.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D ; très léger. Le fond de case (cadre, mur, sol, cartouche) est mis en cache.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `trame.js` (tuiles de points), `encrer.js` (une seule fonction « cerne + aplat »), `bulles.js` (bulle de pensée, cartouche, étoile éclatée), `portraits.js` (grille à 4 jeux de couleurs), `scenes.js`.
- **Techniques clés** :
  ```js
  // trame = motif répété : gratuit, et fixe à l'écran (elle ne « nage » pas avec le personnage)
  const tuile = new OffscreenCanvas(pas, pas), g = tuile.getContext("2d");
  for (const [x, y] of [[0, 0], [pas, 0], [0, pas], [pas, pas], [pas / 2, pas / 2]]) disque(g, x, y, r);
  ctx.fillStyle = ctx.createPattern(tuile, "repeat"); ctx.fill(formePeau);
  // union de formes : tracer TOUT en noir épais, puis remplir TOUT
  formes.forEach(f => trait(ctx, f, 11, NOIR)); formes.forEach(f => remplir(ctx, f, BLANC));
  // grille de portraits
  const pas4 = Math.floor(t * 3); const jeu = (i + pas4) % 4;     // 3 changements par seconde au plus (sécurité, voir section 4)
  ```
- **Pièges** :
  - Calculer la trame pixel par pixel : cent fois plus lent, et les points suivent le personnage ; utilise un motif répété.
  - Chevelure en une seule masse ondulée : on dirait un tissu posé sur la tête ; il faut les boucles et les arcs noirs.
  - Une tête dessinée à sa place d'origine au-dessus d'un corps aplati : elle flotte ; redescends-la dans le corps.
  - Points trop petits après encodage : moiré ; reste au-dessus de 12 px de pas. Mesuré au rendu réel du 11/11/2026 (6,5 Mbit/s) : avec des pas de 16, 17 et 29 px, aucune bande de moiré à 360 px de large ; un léger motif apparaît à 270 px sur le pas de 29 px.
  - **Contour épais du lettrage** : `-webkit-text-stroke: 12px #111` avec `paint-order: stroke fill` sur le texte HTML (le contour passe sous le remplissage, les lettres ne maigrissent pas) ; recette utilisée au rendu réel.

## 7. Son

- **Musique** : rock'n'roll ou surf des années 60, orgue électrique, cuivres courts, claquements de mains ; ou une rythmique sèche et rapide.
- **Bruitages** (≈ 5 par 10 s, bien choisis) : un impact « de BD » pour l'onomatopée (c'est le son le plus fort), un déclic sec pour chaque changement de case, un petit « pop » pour les points de la bulle, un éclair pour la transition.
- **Voix** : dynamique, phrases très courtes ; ou aucune, les cartouches suffisent.
- Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : dégradés ; cernes fins ; trop de couleurs ; trame qui bouge avec le sujet ; onomatopée illisible ; case d'une œuvre connue recopiée.

- [ ] Tout est « cerne noir de 5 à 6 px + aplat » ; aucun dégradé.
- [ ] Trois primaires + noir + blanc (plus les fonds acides de la grille).
- [ ] La peau et un grand fond sont en points de trame à 45°, fixes à l'écran.
- [ ] Les ombres sont des hachures noires ; les reflets, des traits blancs.
- [ ] Au moins une onomatopée ou un cartouche, lisible ≥ 0,8 s, en capitales.
- [ ] La grille de portraits ou les points de la bulle animent le plan.
- [ ] Cadre de case noir ; rien d'important sous y = 1560 ni à droite de x = 945.
- [ ] Aucun personnage, visage célèbre ou case existante.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 15
- Bleu-violet : interdit
- Texte vivant : oui
- Taille mini du texte : 46

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt. Planche commune `assets/全风格总览.jpg` : composition empruntée, à ne pas utiliser comme vitrine. Film complet : Releases de https://github.com/alchaincyf/huashu-art-motion. Image fixe possible avec le moteur d'origine (`render.py --solo 13_pop --stills`, non exécuté ici).
- À produire : notre propre aperçu 9:16 (style simple et rapide : bon candidat pour le premier rendu de contrôle de la catégorie).

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/13_pop.md` (trois étoiles), `scripts/engine/scenes/13_pop.js`. Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : carte traduite et généralisée ; style **renommé** (la carte porte les noms de deux artistes dont les droits sont actifs) ; les textes anglais des cartouches sont traduits ; section 9:16, numéros du dictionnaire de mouvements, son.
- Vérifié par un rendu réel le 11/11/2026 (HyperFrames 0.9.33) : ça marche avec corrections ; aucun moiré à 360 px de large ; changement de couleurs de la grille ramené à 3 par seconde et onomatopée tenue 1 s.
