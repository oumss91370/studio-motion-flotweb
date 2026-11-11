# Mosaïque

## 1. Identité

- **Nom** : Mosaïque (tesselles de pierre).
- **Inspiration** : les pavements de mosaïque de l'Antiquité romaine (ceux des villas ensevelies en l'an 79) : tesselles posées en suivant les contours, bordures à motifs de vagues, figures frontales, inscription en capitales. On reprend le procédé, aucune œuvre.
- **Ce que c'est** : une image faite de **milliers de petites pierres carrées** séparées par un joint sombre. L'idée centrale : **les pierres sont fixées au mur ; ce qui bouge, c'est la couleur qui passe d'une pierre à l'autre.** Les tesselles suivent les contours des formes (plusieurs rangs épousent chaque silhouette), les fonds sont posés en rangs droits, chaque figure est entourée d'un liseré clair de pierres.
- **Marche pour** : sujet patrimonial, culinaire, méditerranéen ou artisanal ; logo ou emblème « en pierre » ; générique de documentaire ; un message court gravé ; un portrait d'animal ou d'objet.
- **Ne marche pas pour** : mouvement rapide ou ample (il se perd dans les pierres), petit texte, visages détaillés en petit, sujet moderne et technique, plus de deux ou trois éléments mobiles.
- Carte notée ★★★ par son auteur, « usage restreint » : le style est lourd à calculer et se prête mal aux sujets très animés.
- Ce n'est pas du pixel art : une **grille régulière** est exactement l'erreur à éviter.

## 2. Palette, typographie, matières

Pierre et verre éteints et chauds. Valeurs de la scène d'origine :

| Rôle | Hex |
|---|---|
| Mur (fond) | `#E4DDCD` |
| Liseré clair autour des figures | `#F5F1E8` |
| Trait de contour | `#46322A` |
| Joint (mortier) | `rgb(112, 103, 92)` soit `#70675C`, ±8 de bruit |
| Cadre : rouge / rouge sombre / or | `#A8322A` · `#7C221D` · `#D0A23C` |
| Ciel | `#9EC0D8` → `#D3E3E4` |
| Verts / sol | `#6F9341` · `#92B254` · `#2B5A2F` / `#CBA344` |
| Bleus de montagne (clair, moyen, sombre) | `#7C84B8` · `#4E5796` · `#2F3672` |
| Feu | `#D64A22` · `#F2952C` |
| Orangé / cheveux blonds / jaune vif | `#DC8530` · `#DCAA42` · `#E9C22C` |

- **Variation pierre par pierre** : ±4 à 8 % selon la zone, plus un léger décalage de gris ; 9 % des pierres tirent vers le chaud, 7 % vers le froid ; dans le fond, 7 % des pierres sont assombries de 12 %. C'est ce qui fait « pierre » et non « aplat quadrillé ».
- **Relief de chaque tesselle** : à moins de 2,2 px du bord, la pierre s'éclaircit ou s'assombrit de ±16 % selon que le bord regarde la lumière (haut gauche) ou non ; léger bombé ; grain de ±3 %.
- **Lettrage** : des **capitales dessinées à la main en gros traits de largeur constante**, chaque trait large d'environ **deux tesselles** (trait 14 px, lettre haute de 60 px dans la source). Une police à empattements fins se brise en pierres (un E devient un F). Pas de police de fichier pour le texte en mosaïque.
- **Police de repli** : aucune pour le texte en mosaïque (lettres dessinées, voir ci-dessus) ; pour un sous-titre hors mosaïque, Montserrat. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : sans objet pour le lettrage ; `@fontsource/montserrat` si le sous-titre doit être embarqué.
- **Tailles de tesselles** (pour une image de 1920 px de large ; garde-les en 1080 de large, les pierres doivent rester visibles sur un téléphone) :

| Zone | Côté | Rangs qui suivent le contour |
|---|---|---|
| Fond | 12 px | 1, puis rangs droits |
| Liseré clair | 11 px | tout le liseré |
| Corps, objets | 10 px | tous |
| Visage, tête d'animal | 6 px | tous |
| Cheveux | 8 px | tous |
| Bordure | 7,6 px | rangs le long du bord |
| Lettrage | 7 px | tous |

## 3. Composition 9:16

- Un **panneau** : bordure à motif sur les quatre côtés (≈ 85 px, 11 rangs de pierres), un champ central clair, **une figure principale** grande (au moins la moitié de la hauteur du champ), éventuellement un petit tableau encadré dans le haut et une ligne d'inscription dans le bas.
- En vertical : bordure de x 30 à 1050, y 170 à 1560 (elle longe les marges sans y mettre de sens ; le lettrage, lui, reste entre x 60 et x 945) ; figure entre y 600 et 1350 ; petit tableau ou emblème entre y 280 et 560 ; inscription vers y 1400 à 1480, 2 à 3 mots, lettres hautes de 70 à 90 px.
- **Liseré clair de 44 à 50 px** autour de chaque figure et objet : les pierres s'alignent dessus et détachent la forme du fond.
- Figures **frontales, un peu raides**, aux formes simples et aux grands yeux (un œil = « une pierre blanche + une pierre sombre »). Traits de contour de 8 px pour que les pierres s'y rangent.
- Les détails de visage se perdent en petit : préfère un animal, un objet, un buste large.
- 16:9 : panneau horizontal, figure d'un côté, tableau encadré de l'autre.

## 4. Ce qui bouge

- **Action principale** : un seul geste lent de la figure (lever une coupe, tourner la tête, remuer la queue) : la couleur se déplace à travers des pierres qui, elles, ne bougent pas.
- **Boucle de fond 1** : **le motif de la bordure qui circule** : une frise de vagues enroulées qui glisse dans le sens des aiguilles d'une montre le long des quatre côtés. Le noir et le blanc passent d'une pierre à l'autre : c'est exactement à cela que ressemble une mosaïque qui s'anime.
- **Boucle de fond 2** : dans le petit tableau, une fumée ou des nuages qui dérivent de côté, quelques étincelles ; ou un éclat lent sur les pierres dorées.
- **Autorisés** : `#027` et son inverse, courtes avancées et reculs, `#175` plan fixe, `#094` motif qui défile (bordure), `#022` éclat lent sur l'or, `#125` pulsation d'une lueur, `#021` transition par **retournement des tesselles en vague** (signature du style).
- **Interdits** : déplacement des pierres elles-mêmes (hors transition), `#024` secousse, `#043` filé, `#028` zoom fort (les pierres deviendraient des pavés), `#011` écrasement et étirement, mouvement rapide, dégradés lisses, flou.
- **Amplifie les petits gestes** : avec des pierres de 9 px, une queue ou une main qui bouge de quelques pixels ne se voit pas (la source multiplie l'amplitude par 1,6).
- Un élément qui monte et sort vite du cadre ne se voit pas : fais-le dériver de côté, dans la zone visible.

## 5. Rythme et montage

- Lent et contemplatif. Plans de 4 à 8 s ; un panneau peut tenir tout un film de 10 à 20 s.
- **Transition signature** : les tesselles se retournent une à une, en vague, pour révéler l'image suivante ; ou l'image se « pose » pierre par pierre le long des contours au début.
- Le mouvement vient des **détails** (un geste, une frise, une fumée, un rai de lumière), pas de la caméra.
- La frise de bordure peut accélérer un instant sur un temps fort (une période de plus), puis reprendre sa dérive.
- Clignement d'un œil : la pierre de l'œil prend la couleur de la peau et un trait sombre.
- **Version courte (8 à 12 s)** : un seul panneau de 8 à 10 s : un geste lent de la figure commencé avant 3 s, une frise qui vit, le lettrage tenu 2 s.

## 6. Recette technique

**Moteur : HyperFrames, canvas 2D.** Ce n'est pas un style 3D : aucun besoin de Blender ni de Three.js. (Pour une mosaïque en relief filmée en lumière rasante, on pourrait instancier les tesselles dans Blender ; ce n'est pas la voie décrite ici.)

- **Le rendu se coupe en deux** :
  1. **Une fois, au chargement** (≈ 0,2 s pour ≈ 18 000 pierres) : calculer pour chaque pierre sa position, sa taille, son orientation, les pixels qui lui appartiennent et son relief. On garde deux tableaux : pour chaque pixel, le numéro de sa pierre (−1 = joint) et son facteur de clair-obscur.
  2. **À chaque image** : redessiner le **dessin plat** (aplats simples), lire ses pixels une fois, prendre la couleur au **centre de chaque pierre mobile** (plus la variation fixe de cette pierre), puis remplir chaque pixel avec `couleur × relief`.
- **Pose des pierres le long des contours** :
  - détecter les arêtes du dessin plat (à demi-résolution) ; calculer la **distance à l'arête la plus proche** ;
  - poser des pierres le long des lignes d'égale distance (les « rangs » qui suivent le contour), orientées selon la tangente, espacées d'au moins un côté de pierre ;
  - **boucher les trous** avec des rangs droits en quinconce (lignes et colonnes légèrement décalées au hasard à graine), en ne posant une pierre que si elle respecte la distance minimale aux voisines.
- **Forme des pierres et joint** : chaque pierre est un carré tourné, **un peu plus grand que son espacement** (demi-côtés de 1,08 à 1,28 fois le demi-pas, tirés indépendamment) ; les voisines se « coupent » mutuellement le long de leur médiatrice, ce qui donne des bords irréguliers comme taillés au marteau. Un pixel est du joint s'il est hors de toute pierre ou trop près de la frontière entre deux pierres (joint de 1,5 à 2,5 px).
  ```js
  // à chaque image, pour les pierres de la zone mobile seulement
  const src = plat.getImageData(0, 0, W, H).data;          // dessin plat de l'instant t
  for (const p of pierresMobiles) p.rgb = varier(couleurAu(src, p.cx, p.cy), p.graine);
  for (const i of pixelsMobiles) {                          // id[i] : pierre ; relief[i] : 128 = 1,0
    const p = pierres[id[i]]; ecrire(i, p ? mul(p.rgb, relief[i] / 128) : JOINT);
  }
  tampon.putImageData(img, 0, 0);  ecran.drawImage(tampon, 0, 0);   // jamais putImageData direct à l'écran
  ```
- **Zone mobile** : calcule au chargement le rectangle que balaient les éléments animés (toutes poses confondues), élargi d'environ 60 px ; hors de ce rectangle, la mosaïque de la première image est réutilisée telle quelle. C'est ce qui rend le style calculable (≈ 13 à 17 ms par image dans la source).
- **Pièges** (relevés par l'auteur) :
  - pierres plus petites que leur espacement : le joint couvre 40 % de l'image, tout paraît clairsemé ;
  - formes étroites (une queue de 26 px) sans aucune pierre : ne conditionne le remplissage qu'à la distance minimale ;
  - rectangle mobile trop juste : des pierres à cheval ont une moitié à l'ancienne couleur ;
  - pierres plus petites dans la seule zone d'un geste : au repos, cela fait une pièce rapportée plus claire ; garde une taille uniforme pour tout le fond ;
  - texte en police fine ; fumée qui sort du cadre ; grille trop régulière qui se lit comme du pixel art ; joint clair.
  - Tout est déterministe : hasard à graine, même image rendue deux fois identique.

## 7. Son

- **Musique** : instruments anciens ou qui les évoquent : lyre ou harpe, flûte double, tambour sur cadre, sistre ; modes simples, tempo lent. Ou seulement une ambiance.
- **Bruitages** (≈ 3 à 5 par 10 s, **vrais enregistrements** de pierre et de céramique) : petites pierres qu'on pose, cliquetis de tesselles qui se retournent en vague (la transition), frottement de pierre, goutte d'eau, braises.
- **Ambiance** : cour intérieure (fontaine, cigales, vent léger) ou atelier.
- **Voix** : posée, de documentaire. −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Les pierres restent en place pendant tout le plan ; seule leur couleur change.
- [ ] Autour de chaque forme, plusieurs rangs de pierres en suivent le contour ; aucune grille régulière sur une figure.
- [ ] Le joint est sombre et fin (1,5 à 2,5 px) ; les pierres paraissent serrées.
- [ ] Chaque pierre a sa légère variation de couleur et son relief (clair en haut à gauche).
- [ ] Un liseré de pierres claires détache chaque figure du fond.
- [ ] Le lettrage est en gros traits, chacun large d'environ deux pierres, lisible sur un téléphone.
- [ ] Une bordure à motif circule ; au plus deux ou trois éléments animés ; aucun mouvement rapide.
- [ ] Les pierres se distinguent encore sur l'export à 540 px de large ; aucune œuvre antique recopiée.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : fixe
- Couleurs max : 21
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt d'origine. Planche commune : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg (© 花叔 Huashu ; à consulter, pas à réutiliser en vitrine).
- Aperçu à produire par un rendu réel 9:16 avec le plugin.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/04_roman.md` (carte traduite du chinois : idée centrale, pose le long des contours, forme des pierres et joint, couleurs, animations, pièges), `scripts/engine/scenes/04_roman.js`. Licence MIT, © 花叔 Huashu. La carte cite, pour la pose des pierres, l'article de recherche « Simulating Decorative Mosaics » (2001).
- Adaptation Flot Web : traduction, nom descriptif, panneau 9:16, sections rythme et son (non fixées par la source), numéros du dictionnaire. Le personnage et le chat de la scène d'origine ne sont pas repris.
