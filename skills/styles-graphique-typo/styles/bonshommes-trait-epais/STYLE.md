# Bonshommes au trait épais (style Haring)

## 1. Identité

- **Nom** : Bonshommes au trait épais. « Style Haring » désigne une inspiration : l'art de rue new-yorkais du début des années 1980. Ce n'est ni une œuvre de cet artiste, ni un produit officiel ou affilié.
- **Inspiration** : des personnages-signes sans visage, tracés d'un seul gros trait noir, entourés de petits traits de mouvement, sur des aplats de couleurs vives. On reprend la grammaire (trait uniforme, aplats, rythme) ; **on ne reproduit aucun personnage, symbole ou composition de l'artiste** (ni bébé rayonnant, ni chien qui aboie, ni cœur porté par deux figures) : on dessine ses propres bonshommes et ses propres signes.
- **Ce qui le fait reconnaître** : un **trait noir épais, à bouts ronds, de la même épaisseur partout** ; des **aplats sans dégradé** ; des figures sans visage ; des **petits traits rayonnants** autour de tout ce qui vit ; et **tout rebondit sur le tempo**.
- **Marche pour** : énergie, fête, danse, sport, musique, message collectif ou solidaire, annonce joyeuse, public jeune, boucle de fond pour un clip.
- **Ne marche pas pour** : sujet sérieux, luxe, détail technique, texte long. Usage **prudent en commercial** : garder le style très générique, ne jamais citer l'artiste dans la vidéo ni dans son titre.

## 2. Palette, typographie, matières

| Rôle | Couleur |
|---|---|
| Mur | jaune `#ffd51c` |
| Sol | vert `#16a54a` |
| Trait | noir `#111111` |
| Figures | rouge `#e8262a`, bleu `#1d5fd0`, rose `#ff6fae`, blanc `#ffffff` |

(Le jaune et le vert viennent de la source ; rouge, bleu et rose sont des exemples.) Trois ou quatre couleurs vives par plan, pas plus.

- **Trait** : 13 px dans la source en 1080 de haut ; **16 à 20 px** en 1080×1920. Bouts ronds, jonctions rondes. Une ligne d'horizon noire de 14 à 18 px sépare le mur du sol.
- **Lettrage** : des capitales tracées avec le même trait (bâtons arrondis). Police de secours libre : Fredoka ou Baloo 2, en très gras, noir.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Fredoka et de Baloo 2. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/fredoka`, `@fontsource/baloo-2` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : aucune. Pas de texture, pas d'ombre, pas de dégradé. À la rigueur un grain de craie très léger ajouté à l'export.
- **Figures** : sept segments en forme de capsule (le tronc, deux bras, deux jambes, et un second segment là où un membre doit plier) et une tête ronde. Pas de visage. Si l'on doit reconnaître quelqu'un : **un point pour l'œil et un trait pour la bouche**, pas plus. Pas de cheveux en traits fins : ils contredisent le trait uniforme.

## 3. Composition 9:16

- Deux bandes de couleur : le mur (y 0 à 1250 environ) et le sol (en dessous), séparés par la ligne d'horizon.
- **Une figure principale** de 600 à 900 px de haut, centrée entre y 400 et y 1400 ; autour, deux à quatre **petites figures** (200 à 300 px) dans d'autres couleurs, avec des phases de danse différentes ; l'une peut être en miroir.
- Remplir l'espace : ce style supporte un cadre plein. Des signes simples (éclair, étoile, spirale, flèche, de son propre dessin) occupent les vides.
- Tout reste à plat : pas de perspective, pas de profondeur.
- **Texte** : un ou deux mots, lettres de 140 à 220 px, entourés de traits rayonnants, en haut (y 200 à 480). Sous-titres : texte noir de 50 px sur bandeau blanc cerné de noir, entre y 1400 et y 1540.
- Rien d'important à droite de x 945.

## 4. Ce qui bouge

- **Action principale** : les bonshommes dansent. **Quatre poses, changées 10 fois par seconde, sans interpolation** (à 30 i/s : une image sur trois ; 8 seulement dans un film livré à 24 i/s) : on passe d'une pose à l'autre d'un coup. C'est ce qui donne le caractère « dessiné à la main ».
- **Boucles de fond** : (1) les **traits rayonnants** : n petits traits (longs de 22 à 34 px, épais de 7 à 9 px) posés sur une ellipse autour de chaque chose vivante, dont l'angle change 10 fois par seconde (petite surface seulement : ce sont des traits de 22 à 34 px ; ne jamais faire changer ainsi un fond ou un aplat) ; (2) **tout suit le tempo** : rebond = |sin(π × temps)| à la puissance 0,6 ; la figure principale monte de 12 px, un second élément est décalé d'un demi-temps, les objets sautent (jusqu'à 26 px), les cadres penchent de ±1,5°.
- **Autorisés** : style image par image `#128`, rebond `#123`, pulsation `#125`, tremblement `#124` (saccadé), écrasement et étirement `#011` (un meuble s'écrase de 7 % et s'élargit de 5 % sur le temps, autour de ses pieds), éclat `#003`, répéteur `#134`, zoom à travers `#020`, plan fixe `#175`.
- **Interdits** : mouvement interpolé lisse sur les poses, courbes d'accélération douces sur les figures, fondu enchaîné `#044`, dégradés, lueur `#022`, flou de mouvement, trait d'épaisseur variable, parallaxe `#016`.
- Un geste important est souligné par deux ou trois **arcs de mouvement** près de la main ou du pied.

## 5. Rythme et montage

- Tout est calé sur un tempo unique (128 battements par minute dans la source). Poses et traits : 10 par seconde (8 dans la source, réglée à 24 i/s). Rebonds : fluides.
- Plans de 2 à 4 s, coupes sèches sur les temps.
- **Transition signature** : la caméra fonce dans une figure qui danse ; le plan suivant apparaît **à l'intérieur de son corps**.
- Monter par accumulation : une figure, puis deux, puis la foule.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D avec `dessiner(t)` ou SVG. Style très léger (quelques millisecondes par image).
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `poses.js` (4 poses par danse : points clés dans le repère de la figure, origine aux pieds), `figure.js` (capsules), `rayons.js`, `tempo.js`.

```js
const BPM = 128;
const rebond = t => Math.pow(Math.abs(Math.sin(t * BPM / 60 * Math.PI)), 0.6);
const pose = (t, phase = 0) => POSES[(Math.floor(t * 10) + phase) % 4];         // 10 poses/s, coupe franche

function figure(ctx, capsules, couleur, L) {
  ctx.lineCap = ctx.lineJoin = "round";
  ctx.strokeStyle = "#111"; ctx.lineWidth = 2 * L;            // 1) TOUT cerner en noir, deux fois l'épaisseur
  capsules.forEach(c => ctx.stroke(c));
  ctx.fillStyle = couleur; capsules.forEach(c => ctx.fill(c)); // 2) PUIS tout remplir : un seul contour autour de l'union
}
function rayons(ctx, cx, cy, rx, ry, n, t) {
  const a0 = hasard(Math.floor(t * 10)) * 0.5;                 // l'angle saute 10 fois par seconde
  for (let i = 0; i < n; i++) { const a = a0 + i * 6.2832 / n; trait(ctx, cx + rx * Math.cos(a), cy + ry * Math.sin(a), a, 28, 8); }
}
```

- **Technique clé** : « cerner tout, puis remplir tout ». Si l'on cerne et remplit membre par membre, les contours se croisent à l'intérieur du corps.
- **Pièges** : des capsules dont un bout est mal fermé laissent un trou aux articulations sous un trait épais ; un élément de décor qui doit passer derrière une figure (barreau de fenêtre) doit être dessiné avant elle ; interpoler les poses « pour faire plus fluide » détruit le style.

## 7. Son

- **Musique** : une boucle rythmique dansante au tempo du film : boîte à rythmes des années 1980, basse funk, claps, cloche. C'est elle qui commande tout.
- **Bruitages** : très peu, percussifs, sur les temps : claquement de mains, « pop », frottement de marqueur ou de craie quand un trait se dessine, sifflet. Ne pas doubler chaque rebond.
- **Silence** : couper la musique un temps entier juste avant la transition « dans le corps ».
- **Voix** : facultative, rythmée, quelques mots sur les temps.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Un seul trait noir, de la même épaisseur partout, à bouts ronds.
- [ ] Aplats purs : aucun dégradé, aucune ombre, aucune texture.
- [ ] Les figures n'ont pas de visage (au plus un point et un trait).
- [ ] Les poses changent 10 fois par seconde, sans interpolation ; seuls des traits changent à cette cadence, jamais la couleur d'un fond.
- [ ] Des traits rayonnants entourent chaque élément vivant, et leur angle change.
- [ ] Tout rebondit sur le même tempo ; au moins un élément est décalé d'un demi-temps.
- [ ] Les figures et les signes sont de notre dessin : aucun motif reconnaissable de l'artiste, son nom n'apparaît nulle part dans la vidéo.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 7
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Planche d'ensemble des styles d'origine (image fixe, 16:9) : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg
- Film de démonstration complet : https://github.com/alchaincyf/huashu-art-motion/releases
- Crédit : 花叔 Huashu (alchaincyf), https://github.com/alchaincyf/huashu-art-motion. Pas d'aperçu séparé pour ce style. La planche contient des motifs proches de ceux de l'artiste : à donner en lien seulement, jamais comme visuel de vente.

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichiers `references/风格配方/31_haring.md` et `scripts/engine/scenes/31_haring.js`.
- Licence : MIT (© 2026 alchaincyf, 花叔).
- Adaptation Flot Web : traduction du chinois, retrait de la scène, des personnages de la démo et des motifs propres à l'artiste, couleurs d'exemple, composition verticale, portage vers HyperFrames, numéros de mouvements, section son.
