# Rêve surréaliste

## 1. Identité

- **Nom** : Rêve surréaliste (dans l'esprit du surréalisme des années 1930). Aucun nom d'artiste dans l'offre ni dans la vidéo ; aucune toile ni motif célèbre recopié tel quel.
- **Inspiration** : la peinture surréaliste « à l'ancienne » : une plaine vide sous un ciel immense, une lumière rasante, des objets durs devenus mous, des ombres démesurées, le tout peint avec le lisse d'un tableau d'académie.
- **Ce que c'est** : un rêve **peint très proprement**. Aucun trait de contour : chaque volume est un dégradé avec une ombre intérieure. Trois ingrédients : **l'espace vide** (horizon bas, ciel en dégradé), **les ombres très longues** qui s'allongent encore, et **un objet rigide qui coule** (montre, téléphone, bâtiment, logo) posé sur un bord et qui pend.
- **Marche pour** : le temps qui passe, la mémoire, la procrastination, le sommeil, une échéance, une idée absurde, un teaser énigmatique.
- **Ne marche pas pour** : explication claire, produit à montrer tel qu'il est, humour léger, enfants, texte abondant.
- **À ne pas confondre** : `lumiere-diner-americain` est réaliste et quotidien ; ici la physique est fausse, mais la lumière est juste.

## 2. Palette, typographie, matières

| Rôle | Hex (source) |
|---|---|
| Ciel, du haut vers l'horizon | `#22407c` → `#5f88bd` → `#e9dcae` |
| Mer ou lointain | `#8aa6b8` → `#4f6f86` |
| Rochers : lumière / ombre | `#e8c27a` / `#9a6a34` |
| Sol | `#d2ad70` → `#7a5129` |
| Mur ou bloc clair | `#f4ead2` → `#cdbf9f` |
| Métal doré de l'objet / son cadran | `#f0d27c` · `#9a7426` / `#f6efd6` |
| Ombres portées | noir à 55 %, floues de 1,5 px |

- **Typographie** : serif fine classique (**Cormorant Garamond**, OFL), crème avec ombre portée sombre sur le ciel, ou brun profond sur le sol. Très peu de mots.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de Cormorant Garamond. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/cormorant-garamond` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : lisse. Chaque forme = dégradé linéaire + **ombre intérieure** floue le long du bord (c'est ce qui donne le rond « académique »). Pas de grain visible, pas de touche. Rayures et détails en traits flous de 2 px.

## 3. Composition 9:16

- **Horizon bas** : vers y ≈ 1050 à 1150. Au-dessus, un grand ciel en dégradé (bleu profond en haut, jaune pâle à l'horizon) ; en dessous, une plaine nue.
- Trois à cinq éléments **isolés**, loin les uns des autres : un bloc ou un pan de mur au premier plan (support de l'objet mou), une branche morte, une petite silhouette étrange sur l'horizon (créature à pattes d'échasses).
- **Soleil bas, devant à gauche** : les ombres partent vers l'arrière droit. En vertical, elles montent vers l'horizon : c'est très lisible.
- L'objet qui coule : sur un bord, 1/5 à 1/4 de la largeur du cadre (rayon 130 à 180 px), dans la zone y 700 à 1300.
- Sous-titres : serif 46 à 52 px, brun profond sur le sol clair ou crème sur une ombre, y ≈ 1400 à 1520. Rien d'important à droite de x = 945.

## 4. Ce qui bouge

- **Action principale** : **l'objet coule** : son affaissement passe de 0,1 à 1,4 en ≈ 1,2 s puis continue lentement ; ses aiguilles ou ses détails tournent à des vitesses différentes (4,5 à 6,5 rad/s).
- **Boucle de fond 1** : **les ombres s'allongent** : l'étirement passe de 0,85 à 1,45 sur la durée du plan.
- **Boucle de fond 2** : **la vie étrange** : une créature à longues pattes traverse l'horizon (≈ 70 px/s, quatre pattes en décalage d'un quart de cycle), des fourmis tournent en ellipse autour d'un petit objet, une queue ou un tissu se ramollit.
- **Autorisés** : `#013` mouvement liquide, `#012` métamorphose lente, `#019` transition liquide (gouttes), `#027` avancée lente, `#037` ralenti, `#039` passage du temps (ombres), `#175` plan fixe, `#183` plan d'ensemble.
- **Interdits** : contour, `#024` secousse, `#043` panoramique filé, montage rapide, objets entassés, ombres courtes, texture de touche.
- **Transition signature** : des gouttes coulent du haut du cadre et emportent l'image.

## 5. Rythme et montage

- Lent et inquiétant : plans de 5 à 9 s, caméra fixe ou en très lente avancée.
- Le temps est élastique : un ralenti franc, puis une ombre qui file. Un seul événement par plan.
- Peu ou pas de coupes ; transition par les gouttes.
- **Version courte (8 à 12 s)** : un seul plan : l'élément impossible fait son geste avant 3 s, la caméra avance très lentement, deux ou trois mots tenus 2 s.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D ; ≈ 47 ms par image.
- **Ordre des couches** (les ombres doivent se glisser **entre** les couches) : fond en cache (ciel, mer, rochers, sol) → **ombres** (chaque image) → mur ou bloc de premier plan (cache) → support (cache) → objets mous → sujet.
- **Techniques clés** :
  ```js
  // remplissage en volume : dégradé + ombre intérieure
  function volume(c, chemin, grad, sombre, flou) {
    c.fillStyle = grad; c.fill(chemin);
    c.save(); c.clip(chemin); c.shadowColor = sombre; c.shadowBlur = flou;
    c.lineWidth = 2; c.strokeStyle = sombre; c.stroke(chemin); c.restore();
  }
  // ombre longue : silhouette projetée au sol par cisaillement autour de la ligne d'appui yg
  c.setTransform(1, 0, -kx, ky, kx * yg, yg * (1 - ky));   // kx = 0.85 + 0.6 * ease(t / 1.2)
  ```
  - Dessine **toutes** les silhouettes d'ombre en noir plein sur un calque, puis pose ce calque une seule fois à 55 % : les ombres qui se croisent ne foncent pas.
  - **Objet mou** : une seule fonction transforme les coordonnées du disque (u, v) vers l'écran. La partie posée est écrasée (hauteur × 0,3) ; la partie qui dépasse le bord tombe, s'évase et ondule. Bord, cadran, graduations, aiguilles et reflet **passent tous par cette même fonction**.
  - Évasement **négatif** (−0,12) : la partie qui pend s'étale comme un tissu, bas arrondi.
- **Pièges** :
  - Ombres projetées vers le spectateur : elles sortent par le bas du cadre. Soleil devant à gauche, ombres vers l'arrière.
  - Une ombre est **sur le sol** : elle se dessine sous le mur et le support. D'où le fond en plusieurs caches.
  - Évasement positif + beaucoup de coulure = cornet de glace.
  - Affaissement trop timide (0,35 → 1,0) : « on ne voit pas que ça coule ».
  - Texte sombre sur ciel bleu profond : illisible ; crème avec ombre.

## 7. Son

- **Ambiance** : vent sur une plaine, très large ; mer très lointaine ; aucune présence humaine.
- **Musique** : piano préparé, cordes tenues en harmoniques, boîte à musique ralentie et désaccordée, tic-tac irrégulier.
- **Bruitages** (≈ 3 à 5 par 10 s) : étirement visqueux pour la coulure, tic-tac qui ralentit, petits pas secs sur le sable, une cloche très lointaine.
- Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défaut connu de la source (deux étoiles) : figure encore trop « illustration vectorielle » ; ajoute des reflets fins et une lumière renvoyée dans les ombres. Erreurs : contours ; scène encombrée ; ombres courtes ; objet qui ne coule pas assez.

- [ ] Aucun trait de contour ; chaque volume a une ombre intérieure.
- [ ] Horizon dans le tiers bas du cadre, plaine vide.
- [ ] Toutes les ombres vont dans la même direction et s'allongent pendant le plan.
- [ ] Les ombres passent sous les objets et ne foncent pas en se croisant.
- [ ] L'objet mou coule visiblement en moins de 2 s ; tous ses détails suivent la déformation.
- [ ] Trois à cinq éléments isolés, pas plus.
- [ ] Aucun motif célèbre recopié ; aucun nom d'artiste.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : fixe
- Couleurs max : 14
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt. Planche commune `assets/全风格总览.jpg` : composition empruntée, à ne pas utiliser comme vitrine. Film complet : Releases de https://github.com/alchaincyf/huashu-art-motion. Image fixe possible avec le moteur d'origine (`render.py --solo 23_dali --stills`, non exécuté ici).
- À produire : notre propre aperçu 9:16.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/23_dali.md` (deux étoiles), `scripts/engine/scenes/23_dali.js`. Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : carte traduite et généralisée ; style **renommé** (l'original porte le nom d'un artiste dont les droits sont actifs) et motifs célèbres remplacés par « un objet rigide du sujet qui coule ». Section 9:16, son.
