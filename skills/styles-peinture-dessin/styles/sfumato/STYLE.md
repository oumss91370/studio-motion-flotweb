# Sfumato (Renaissance)

## 1. Identité

- **Nom** : Sfumato (Haute Renaissance, vers 1500). Inspiration seulement : aucun tableau recopié.
- **Inspiration** : le portrait italien du début du XVIᵉ siècle : contours « enfumés », lointain bleuté derrière une fenêtre en arc, vernis jauni, fines craquelures ; et les carnets d'inventeur de la même époque.
- **Ce que c'est** : une image **sans trait** : les formes se modèlent par dégradés et les bords se fondent. Derrière le sujet, un **paysage en perspective atmosphérique** : plus c'est loin, plus c'est bleu et pâle. Par-dessus, tout ce qui fait « tableau ancien » : trame de toile, voile de touches d'huile, vernis jaune, craquelures.
- **Marche pour** : portrait calme, patrimoine, musée, savoir-faire ancien, invention, vin, sujet d'histoire, « l'origine de… ».
- **Ne marche pas pour** : énergie, humour, technologie récente, couleurs de marque vives, texte abondant.
- **À ne pas confondre** : `clair-obscur` oppose noir et flaques de lumière ; ici tout est en demi-teintes douces.

## 2. Palette, typographie, matières

| Rôle | Hex (source) |
|---|---|
| Mur sombre | `#43321f` → `#22180e` |
| Lointain : montagnes, de la plus proche à la plus lointaine | `#7d9294` → `#9fb4b8` |
| Vallée | gris-vert → ocre chaud `#b08a5a` |
| Rivière | blanc argenté `#e6ebe6` (3 à 16 px de large selon la distance) |
| Sol en damier | `#a88c64` et `#5c2418` |
| Tissus : pli clair / pli sombre | `rgba(200,70,60,.3)` / `rgba(40,0,0,.45)` |
| Vernis | jaune à 7 % ; vignettage 30 % au milieu, 80 % au bord |

- **Typographie** : capitales romaines (**Cinzel**) ou serif d'époque (**EB Garamond**, **IM Fell English**), OFL, en ocre clair, petites. Une écriture de carnet (cursive penchée) pour une note d'inventeur.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Playfair Display à la place de Cinzel ; EB Garamond à la place d'IM Fell English ; EB Garamond : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/cinzel`, `@fontsource/im-fell-english` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** :
  - *Sfumato général* : tout le décor fixe est dessiné puis recopié avec un **flou de 1,3 px**.
  - *Sfumato du sujet* : dessiné à part ; recopié d'abord flou de **1,6 px** en pleine opacité, puis net à **82 %**. Bords doux, traits lisibles. (Les valeurs d'origine, 2,6 px et 38 %, rendaient le sujet plus flou que le paysage : profondeur inversée.)
  - *Voile de tableau* : trame de toile (un fil tous les 3 px), ≈ 9 000 touches très pâles (opacité 0,022 à 0,028, 5 à 10 px de large, **directions au hasard**), craquelures à 32 % doublées d'un filet clair décalé de 1 px (la peinture qui se soulève).

## 3. Composition 9:16

- Portrait en buste ou à mi-corps de trois quarts, mains visibles, devant un mur sombre percé d'une **fenêtre en arc** (haut du cadre, vers y 220 à 700) qui ouvre sur le paysage.
- Lumière d'un seul côté (gauche), douce. Le sol, s'il se voit, est sombre sauf la flaque de lumière de la fenêtre.
- Visage vers y 520 à 820, tête ≥ 260 px. Le sujet reste **plus net que le paysage**.
- Sous-titres : serif crème 46 à 52 px, sur le bas sombre du cadre, y ≈ 1400 à 1520. Rien d'important à droite de x = 945.
- 16:9 : sujet à droite, fenêtre et paysage à gauche.

## 4. Ce qui bouge

- **Action principale** : un geste retenu (porter une coupe aux lèvres, tourner une page, lever les yeux).
- **Boucle de fond 1** : **le paysage vit** dans la fenêtre : ≈ 24 éclats de lumière descendent la rivière, une quinzaine d'oiseaux passent, l'ombre d'un nuage glisse sur la vallée ; une **machine volante** d'inventeur peut traverser le ciel (ailes à nervures en éventail qui battent, corps qui tangue).
- **Boucle de fond 2** : **le faisceau de la fenêtre** dont l'intensité varie (0,75 ± 0,35 quand un nuage passe) et ≈ 70 poussières qui montent lentement dedans.
- **Autorisés** : `#027` avancée très lente, `#033` bascule de mise au point du paysage vers le visage, `#175` plan fixe, `#096` flottement, `#112` vignettage.
- **Interdits** : trait de contour, `#136` frémissement, `#011` écrasement, coupes rapides, couleur saturée, voile de touches orienté (il se transforme en tourbillons).
- **Transition signature** : un rayon de lumière qui tombe de la fenêtre et blanchit l'image.

## 5. Rythme et montage

- Lent : plans de 6 à 9 s. C'est un style **naturellement statique** : vise au moins trois mouvements simultanés (rivière, faisceau, sujet).
- Entrée par une avancée depuis le tableau entier (cadre doré possible) vers le visage.
- Musique d'abord, peu de coupes.
- **Version courte (8 à 12 s)** : un seul plan de 8 à 10 s, avec ses trois mouvements simultanés dès l'image 0 ; la bascule de mise au point vers le visage a lieu avant 3 s.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D ; rapide (≈ 16 à 37 ms par image).
- **Chaîne de rendu** :
  1. Calque fixe (en cache, flouté de 1,3 px) : mur, fenêtre en arc et son encadrement de pierre éclairé d'un côté, sol en perspective, mobilier.
  2. Lointain : trois rangées de montagnes au contour bruité, de plus en plus bleues et pâles ; lac, vallée, rivière sinueuse, arbres, pont.
  3. À chaque image, dans la fenêtre : éclats de rivière, oiseaux, machine volante.
  4. Sujet (calque à part, deux passes floue et nette). **Aucun trait** : plis en bandes claires et sombres, bande de lumière le long des manches, visage éclairé d'un côté avec l'ombre des orbites.
  5. Faisceau (coin flouté de 28 px, en cache, mode « écran ») et poussières.
  6. Voile de tableau (en cache, une seule copie par image).
- **Techniques clés** :
  ```js
  // bords fondus mais visage lisible
  ctx.filter = "blur(1.6px)"; ctx.drawImage(sujet, 0, 0);
  ctx.filter = "none"; ctx.globalAlpha = 0.82; ctx.drawImage(sujet, 0, 0); ctx.globalAlpha = 1;
  // sol en damier : vraie projection, y = horizon + f * h / Z, x = centre + f * X / Z
  ```
- **Pièges** :
  - Voile de 26 000 touches à 5 % qui suivent un bruit : tout le mur devient un tourbillon post-impressionniste. 9 000 touches, 2,5 %, directions au hasard.
  - Sol trop clair et contrasté = illustration vectorielle : assombris tout autour, ne garde que la flaque de lumière.
  - Assombrissement intérieur trop fort au bord d'une forme claire (26 px, 45 %) = cloche de verre : 14 px, 22 %.
  - Un faisceau rempli directement à chaque image a deux bords durs : floute-le et mets-le en cache.
  - Machine volante dessinée comme un avion en papier : on ne la reconnaît pas ; il faut le longeron, les nervures et le bord festonné.

## 7. Son

- **Ambiance** : atelier de pierre, écho court, oiseaux lointains par la fenêtre, eau.
- **Musique** : luth, viole de gambe, flûte à bec, voix seule sans paroles ; polyphonie lente.
- **Bruitages** (≈ 3 à 5 par 10 s) : étoffe, métal d'une coupe, plume sur papier, battement d'ailes de toile et de bois au passage de la machine.
- Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défauts connus de la source (deux étoiles) : **statique**, et sujet secondaire trop « cartoon ». Erreurs : contours ; sujet plus flou que le fond ; voile qui tourbillonne ; sol trop clair.

- [ ] Aucun trait de contour ; les volumes viennent des dégradés.
- [ ] Le sujet est plus net que le paysage.
- [ ] Trois plans de lointain, de plus en plus bleus et pâles.
- [ ] Craquelures et vernis visibles sur le fond, discrets sur le visage.
- [ ] Au moins trois mouvements en même temps.
- [ ] Le faisceau varie d'intensité ; poussières dedans seulement.
- [ ] Texte en serif ancien, hors y > 1560 et x > 945.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 8
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt. Planche commune `assets/全风格总览.jpg` : composition empruntée, à ne pas utiliser comme vitrine. Film complet : Releases de https://github.com/alchaincyf/huashu-art-motion. Image fixe possible avec le moteur d'origine (`render.py --solo 06_renaissance --stills`, non exécuté ici).
- À produire : notre propre aperçu 9:16.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/06_renaissance.md` (deux étoiles), `scripts/engine/scenes/06_renaissance.js`. Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : carte traduite et généralisée (valeurs de la deuxième version, après relecture indépendante), section 9:16, son.
