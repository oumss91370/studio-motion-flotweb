# Tourbillons (style Van Gogh)

## 1. Identité

- **Nom** : Tourbillons (style Van Gogh, post-impressionnisme). Inspiration seulement : jamais présenté comme officiel, aucune toile recopiée.
- **Inspiration** : la touche épaisse et orientée de la fin du XIXᵉ siècle : des bâtonnets de pâte qui suivent un courant, un ciel qui tourne, des halos en anneaux autour des lumières, un contour bleu sombre.
- **Ce que c'est** : toute l'image est repeinte en **touches courtes et épaisses qui suivent un champ de directions**. Les murs sont peints en longues touches verticales, le sol en touches qui filent vers le point de fuite, le ciel le long de tourbillons. Chaque zone a **sa propre palette d'une dizaine de teintes** : c'est cela qui fait le style, pas un bruit de couleur.
- **Marche pour** : une nuit, un moment de bascule, de l'énergie, une marque créative, un sujet d'art ou de culture, une ouverture spectaculaire.
- **Ne marche pas pour** : petit texte, visages à reconnaître, produit à montrer net, sujet calme et sobre, vidéo longue (c'est le rendu le plus lourd de la catégorie).
- **À ne pas confondre** : `huile-couteau` a des aplats nets et une peinture immobile ; `expressionnisme` a de longues touches fluides **sans** contour ; `impressionnisme` a de petites touches pastel sans contour.

## 2. Palette, typographie, matières

Une palette **par zone** (valeurs de la source, à adapter au sujet) :

| Zone | Teintes |
|---|---|
| Mur, grande surface froide | `#7f9be6` `#5f7fd8` `#a7bbf2` `#6c6fd2` `#8ad0e6` `#c3cbf6` `#4f6cc8` `#9a8fe0` |
| Ciel de nuit | `#22339a` `#2f4fb8` `#5c86dc` `#8fb6ee` `#1b2a78` `#3c6bd0` |
| Sol, grande surface chaude | `#c0573c` `#a8453a` `#d7774a` `#8e3b30` `#5f8f6a` `#c96a52` `#e08a5c` |
| Contour | bleu profond `#1f2a66`, 4 à 5 px |
| Lumières (étoiles, lampe) | jaunes `#f6d24a` `#fbe79a`, blanc chaud `#fff6d8` |

- Règle : froid dominant (bleus, violets) contre un chaud complémentaire (orangés, jaunes) ; la touche est mélangée à 30-45 % avec la couleur de l'aplat qu'elle recouvre.
- **Attention à la porte de livraison** : ce style est naturellement bleu-violet. Garde une grande surface chaude (sol, champ, lumière) dans chaque plan, ou déclare la dérogation (`styles-jeu-retro/references/derogation-bleu-violet.md` ; option `--autoriser-bleu-violet` de la porte de `studio-coeur`).
- **Typographie** : un titre lettré à la brosse, peint dans l'image (par exemple **Caveat Brush**, OFL) ; sous-titres en serif simple sur un bandeau peint.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Caveat Brush. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/caveat-brush` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : pâte épaisse en bâtonnets. Contour de chaque touche légèrement plus sombre (mêlé de 40 à 45 % de bleu profond). Le fond d'aplat reste visible dans les interstices.

## 3. Composition 9:16

- Le vertical est idéal : **2/3 de ciel en haut** (tourbillons), une bande de sol ou de toits en bas. Place 2 ou 3 centres de tourbillon, dont un dans le tiers haut (vers x 380, y 520).
- Sujet (silhouette, bâtiment, objet) entre y = 900 et y = 1500, à ≥ 1/3 de la hauteur aux moments clés, **toujours traité à part** (voir la recette) pour rester lisible.
- Taille des touches en 1080 de large : zone libre ≈ 22 px de long × 6,5 de large ; murs ≈ 64 × 8 ; sol ≈ 46 × 8. Ne réduis pas : en dessous, on ne voit plus la touche sur un téléphone.
- Sous-titres : bandeau peint d'une teinte unie sombre, texte crème 48 à 54 px, vers y ≈ 1400 à 1520. Rien d'important à droite de x = 945.
- 16:9 : ciel sur la moitié haute, point de fuite du sol au centre.

## 4. Ce qui bouge

- **Action principale** : le sujet joué (un geste simple) pendant que le ciel tourne.
- **Boucle de fond 1** : **le ciel en tourbillons** : la direction des touches suit la tangente du tourbillon le plus proche et tourne lentement (≈ 0,3 rad/s).
- **Boucle de fond 2** : **halos qui s'élargissent** en anneaux pointillés autour des lumières, étoiles qui clignotent, flammes ou fumées qui ondulent comme le champ de directions.
- **Frémissement** : la graine des touches change 10 fois par seconde (une image sur trois à 30 i/s ; 8 dans la source), **en position et en angle seulement, à couleur constante**, y compris pour le trait de contour du décor. Faible amplitude seulement : aucune zone ne doit changer de luminosité d'ensemble à cette cadence (ce serait un clignotement sur grande surface). Si l'image paraît grouiller, garde les positions fixes et ne fais frémir que le ciel.
- **Autorisés** : `#136` trait qui frémit, `#135` motif tournant (tourbillon), `#125` pulsation (halo), `#027` avancée lente, `#026` panoramique vertical du sol vers le ciel, `#020` traversée d'un tourbillon comme transition, `#175` plan fixe.
- **Interdits** : `#044` fondu enchaîné long, `#022` balayage de lumière, `#023` glitch, aplats nets sans touche, caméra rapide (les touches deviennent du bruit).
- **Transition signature** : l'image est **aspirée dans un tourbillon** ; la suivante en sort.

## 5. Rythme et montage

- Plans de 4 à 7 s, caméra lente. 2 ou 3 plans dans ce style suffisent pour un Short ; il sert très bien d'ouverture ou de pic.
- Entrée et sortie par le tourbillon (≈ 0,5 s), calées sur un temps fort.
- Laisse au moins 1,5 s de plan fixe pour que l'œil lise la touche.
- **Version courte (8 à 12 s)** : un ou deux plans : l'entrée par le tourbillon (0,5 s) sert d'accroche, puis 1,5 s de plan fixe pour lire la touche.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D, `renderAt(t)`. Compter ≈ 110 à 120 ms par image en 1080p : c'est lourd, prévois le temps de rendu.
- **Chaîne de rendu** (l'ordre compte) :
  1. Esquisse en **aplats** (grandes surfaces).
  2. **Trois passes de touches** selon un champ de directions, chacune avec sa palette de zone : murs, sol, tout le reste.
  3. **Calque d'objets** (mobilier, objets, lampes) : petites touches, limitées à leur silhouette.
  4. Trait de contour du décor (bleu profond, 4,5 px), qui frémit 10 fois par seconde.
  5. Personnage ou sujet : aplat → petites touches limitées à sa silhouette → traits et détails par-dessus.
  6. Lumières animées : anneaux pointillés qui s'écartent, étoiles, vapeur.
- **Techniques clés** :
  ```js
  // champ de directions par zone
  const angle = zone === "mur"  ? -Math.PI / 2 + 0.22 * bruit(x, y)
              : zone === "sol"  ? Math.atan2(fuite.y - y, fuite.x - x)
              : zone === "ciel" ? tangente(tourbillonProche(x, y)) + 0.3 * t
              : champLibre(x, y);
  // graine des touches : 8 changements par seconde
  const graine = Math.floor(t * 10);
  ctx.globalCompositeOperation = "source-atop";   // touches limitées à la silhouette de l'objet
  ```
- **Pièges** :
  - **Un seul réglage pour toute l'image donne une moquette** : murs, sol et reste doivent être trois passes.
  - **Les petits objets sont broyés par les grandes touches** : mets-les sur leur propre calque.
  - **Varier seulement la luminosité d'un bleu donne « du bruit bleu »** : l'effet vient d'une dizaine de teintes différentes par zone.
  - Un trait de contour ajouté en dernier par-dessus tout traverse les parties cachées : trace les traits pièce par pièce, dans l'ordre d'empilement.

## 7. Son

- **Ambiance** : nuit de campagne ou de ville lointaine, vent large.
- **Musique** : cordes en mouvement circulaire (arpèges qui tournent), piano, une montée qui accompagne le tourbillon ; éviter la nappe figée.
- **Bruitages** (≈ 5 par 10 s) : frottement de brosse épaisse sur toile à l'entrée, souffle grave qui tourne pour le tourbillon (placé de gauche à droite), petit tintement par étoile qui s'allume, grésillement de lampe.
- Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défaut connu de la source : rendu le plus lourd du catalogue (≈ 120 ms par image). Erreurs : moquette uniforme ; objets illisibles ; palette d'une seule teinte ; tout qui grouille ; composition recopiée d'une toile célèbre.

- [ ] Trois passes de touches distinctes (murs, sol, reste), directions différentes visibles.
- [ ] Chaque zone utilise au moins 6 teintes différentes.
- [ ] Le sujet et les objets sont lisibles en vignette (calque à part).
- [ ] Le ciel tourne ; au moins un halo s'élargit.
- [ ] Une surface chaude dans chaque plan ; l'image n'est pas bleu-violet à plus de 30 % sans dérogation notée.
- [ ] Au moins 1,5 s de plan fixe par plan.
- [ ] Aucune toile existante reconnaissable ; aucun nom de peintre à l'image.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 25
- Bleu-violet : dérogation
- Texte vivant : non
- Taille mini du texte : 48

## 9. Aperçu

- Pas d'aperçu isolé réutilisable dans le dépôt. Le seul GIF de ce style dans `assets/showcase/` met en scène la mascotte d'une marque tierce : **à ne pas montrer**. La planche commune `assets/全风格总览.jpg` reprend une composition empruntée à un autre créateur : à ne pas utiliser comme vitrine.
- Film complet de l'auteur : Releases de https://github.com/alchaincyf/huashu-art-motion. Une image fixe du style se rend avec le moteur d'origine (`render.py --solo 09_postimp --stills`, non exécuté ici).
- À produire : notre propre aperçu 9:16.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/09_postimp.md` (carte étalon, notée trois étoiles par l'auteur), `scripts/engine/scenes/09_postimp.js`. Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : carte traduite du chinois et généralisée (la carte décrivait une pièce précise), section 9:16, numéros du dictionnaire de mouvements, son.
