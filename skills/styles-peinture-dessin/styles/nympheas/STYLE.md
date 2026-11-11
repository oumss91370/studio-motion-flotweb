# Nénuphars (style Monet)

## 1. Identité

- **Nom** : Nénuphars (style Monet, jardin d'eau). Inspiration seulement : aucune toile recopiée, jamais présenté comme officiel.
- **Inspiration** : les grands panneaux d'étang de la fin du XIXᵉ siècle : une surface d'eau qui remplit le cadre, des reflets, des nénuphars, un petit pont, des saules.
- **Ce que c'est** : la variante « eau » de l'impressionnisme. Le plan d'eau est peint en **touches horizontales** qui tremblent ; les reflets du ciel y flottent ; des nénuphars dérivent ; des ombres de saule ondulent. Aucun contour. Les ombres sur les personnages sont **colorées** (jaune chaud côté lumière, violet côté ombre).
- **Marche pour** : calme, méditation, spa, bien-être, parfum, thé, jardin, pause dans une vidéo plus vive, fond pour une citation.
- **Ne marche pas pour** : action, texte dense, explication, sujet urbain.
- **À ne pas confondre** : `impressionnisme` traite la lumière sur des surfaces sèches ; ici, tout est construit autour de l'eau.

## 2. Palette, typographie, matières

| Zone | Teintes (source) |
|---|---|
| Eau (dégradé vertical) | `#b9c7e6` → `#8fa6d6` → `#6c84bf` → `#5a72a8` |
| Touches d'eau | `#5b6fb5` `#7d8fd0` `#9db5e0` `#6aa0a8` `#b7a6d8` `#d9c8e8` `#8fb8a8` `#a6c4e8` `#c8b0d8` |
| Feuilles | `#5f8f4a` `#7fae5a` `#3f6f4a` `#9cc070` `#6f9a7a` `#b4cc78` |
| Fleurs | `#f0a0b8` `#f7d0dc` `#fff2f4` `#e88aa0` |
| Reflets de lumière | `#fffbe8` `#fdf0d0` `#f8e0ec` `#e8f4ff` |
| Rive, bois, sol | `#c69a6a` `#b07a5a` `#d8b08a` `#9a6a7a` `#8a7aa8` `#e0bc90` |
| Structure (pont, barrière) | fond sombre `#24452a`, trait `#3f8a62`, lumière `#8fdcae` |

- **Attention à la porte de livraison** : l'eau tire vers le bleu-violet. Équilibre avec les verts des feuilles, les roses des fleurs et une rive chaude ; sinon déclare la dérogation (`styles-jeu-retro/references/derogation-bleu-violet.md`).
- **Typographie** : serif fine (**Cormorant Garamond**, OFL), texte crème sur un halo flou clair-obscur ou sur une feuille de nénuphar agrandie ; le texte posé directement sur les touches ne se lit pas.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de Cormorant Garamond. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/cormorant-garamond` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : touches d'eau ≈ 34 px de long × 6,5 de large, **horizontales** (angle 0 ± 0,06 rad) ; lointain ≈ 13 × 4,5 ; sol ≈ 34 × 8. Nénuphars : une centaine d'ellipses à encoche (demi-largeur 38 à 78 px, demi-hauteur 12 à 21 px), en une dizaine de groupes, 40 % avec une fleur rose ou blanche.

## 3. Composition 9:16

- **L'eau remplit le cadre** : pas d'horizon, ou un horizon très haut (y < 400). Le vertical va très bien : rive et saules en haut, eau au milieu, nénuphars proches et plus grands en bas (ils grossissent en descendant).
- Une structure simple (pont, ponton, barque) dans le tiers haut, **sur son propre calque** avec un fond sombre derrière elle.
- Si un sujet est présent : ≥ 1/3 de la hauteur, côté gauche ou centre, loin de x > 945.
- Sous-titres : crème 48 à 54 px sur halo sombre flou, y ≈ 1400 à 1520 ; prévois une zone d'eau plus sombre à cet endroit.

## 4. Ce qui bouge

- **Action principale** : très peu : un nénuphar poussé, une main dans l'eau, une barque qui glisse, un caillou qui tombe.
- **Boucle de fond 1** : **le scintillement de l'eau** : ≈ 160 courtes touches claires horizontales dont la luminosité suit `sin(t·(5 à 11) + φ)·sin(2,3·t + i)`, qui sautent de ±5 px de côté 10 fois par seconde (petite surface seulement : des touches fines et dispersées, jamais toute l'eau qui s'éclaircit d'un coup).
- **Boucle de fond 2** : les nénuphars dérivent (`x + sin(1,3·t + φ)·7 + 6·t`), les ombres de saule ondulent (bord décalé de `sin(0,03·y − 3,2·t)·14`), 2 ou 3 ronds dans l'eau (ellipses pointillées très aplaties qui s'élargissent et s'effacent), grappes de fleurs qui se balancent.
- **Autorisés** : `#096` flottement, `#085` onde qui s'élargit (rond dans l'eau), `#027` avancée très lente, `#169` montée verticale lente, `#175` plan fixe, `#037` ralenti.
- **Interdits** : frémissement de tout l'écran, `#043` panoramique filé, `#046` coupe brutale, `#024` secousse, contours, noir.
- **Transition signature** : une onde part d'un point de l'eau et la nouvelle image arrive derrière elle.

## 5. Rythme et montage

- Le plus lent de la catégorie : plans de 6 à 10 s, un seul mouvement de caméra par plan.
- Transition par l'onde (≈ 0,7 s). Très bon en boucle parfaite pour un fond.
- L'eau frémit 6 fois par seconde (les touches changent de place, pas de couleur : faible amplitude) ; **le sol, les cadres et les structures ne frémissent pas du tout**.
- **Version courte (8 à 12 s)** : un plan en boucle parfaite de 8 à 10 s : une onde part avant 3 s (une goutte, un poisson), le texte sur son halo tient 2 s.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D. ≈ 105 ms par image en 1080p.
- **Chaîne de rendu** :
  1. Esquisse redessinée à chaque image : dégradé d'eau, 4 reflets de ciel rose-jaune pâle, ombres de saule, nénuphars.
  2. **Quatre passes de touches** : eau (horizontales, frémissement 6 fois par seconde), lointain (petites, obliques en haut, horizontales en bas), sol (sans frémissement), structures (sans frémissement). Aucun contour.
  3. **La structure à part** : un fond sombre derrière, un gros trait de base (≈ 20 px), un trait de lumière, puis de petites touches bleu-vert. Sans cela, elle est avalée par les feuillages.
  4. Sujet : aplat → petites touches dans sa silhouette → **ombre colorée** : dégradé jaune chaud à 22 % côté lumière, violet à 32 % côté ombre → traits du visage en fin trait violet `#5a4f8a`.
- **Techniques clés** :
  ```js
  const angleEau = 0 + 0.06 * (hash(i, j) - 0.5) * 2;            // touches horizontales
  const graineEau = Math.floor(t * 6);                            // l'eau seule frémit
  const scint = clamp(Math.sin(t * v + ph) * Math.sin(2.3 * t + i), 0, 1);
  // rond dans l'eau : ellipse pointillée, ry = rx * 0.22, qui grandit et s'efface
  ```
- **Pièges** :
  - Tout l'écran qui frémit 6 fois par seconde = bruit plein cadre (près de la moitié des pixels changent) : limite le frémissement à l'eau.
  - Des grappes de fleurs tracées en gros traits ressemblent à des gélules : fais-les en suites de points de plus en plus petits.
  - Un texte posé sur les touches est illisible : halo clair ou sombre flou dessous.

## 7. Son

- **Ambiance** : eau calme, clapotis, grenouilles lointaines, insectes, feuillage de saule.
- **Musique** : piano avec beaucoup d'air, harpe, cordes tenues très douces ; pas de pulsation marquée.
- **Bruitages** (≈ 3 à 5 par 10 s, moins que d'habitude) : goutte, petit plouf, rame, froissement de feuille.
- Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défaut connu de la source (deux étoiles) : espace incohérent quand l'eau sert aussi de « mur » ; choisis un vrai plan d'eau vu de haut. Erreurs : tout qui grouille ; structure invisible ; ombres grises ; horizon au milieu.

- [ ] Les touches de l'eau sont horizontales ; celles du sol et des structures ne frémissent pas.
- [ ] Le scintillement est irrégulier (pas de clignotement d'ensemble).
- [ ] La structure (pont, barque) se lit en vignette.
- [ ] Les nénuphars dérivent et grossissent vers le bas du cadre.
- [ ] Ombres colorées sur le sujet (jaune / violet), aucun gris.
- [ ] Pas plus de 30 % de l'image en bleu-violet sans dérogation notée.
- [ ] Le texte repose sur un halo et reste lisible sur téléphone.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 36
- Bleu-violet : dérogation
- Texte vivant : non
- Taille mini du texte : 48

## 9. Aperçu

- Le GIF `assets/showcase/monet.gif` du dépôt montre ce style, mais avec le personnage de l'auteur, **exclu de la licence MIT** : à ne pas réutiliser ni montrer comme vitrine. Planche commune `assets/全风格总览.jpg` : composition empruntée, même réserve.
- Film complet : Releases de https://github.com/alchaincyf/huashu-art-motion. Image fixe possible avec le moteur d'origine (`render.py --solo 28_monet --stills`, non exécuté ici).
- À produire : notre propre aperçu 9:16.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/28_monet.md` (deux étoiles), `scripts/engine/scenes/28_monet.js`. Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : carte traduite et généralisée, section 9:16, numéros du dictionnaire de mouvements, son.
