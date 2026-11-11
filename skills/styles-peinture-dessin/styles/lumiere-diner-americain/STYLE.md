# Lumière de diner américain

## 1. Identité

- **Nom** : Lumière de diner américain (réalisme américain des années 1940). Aucun nom d'artiste dans l'offre ni dans la vidéo ; aucune toile recopiée.
- **Inspiration** : la peinture réaliste américaine du milieu du XXᵉ siècle : des intérieurs presque vides, un **pan de soleil à bord franc** sur un mur, une personne seule, une rue de briques par la fenêtre, le silence.
- **Ce que c'est** : des aplats sobres et une seule vedette : **la lumière en blocs durs**. Chaque surface existe en deux versions, **à l'ombre** (froide) et **au soleil** (chaude). Un polygone de lumière se déplace lentement et découpe la version chaude dans la version froide. Quand le bord du soleil traverse un visage, tout est dit.
- **Marche pour** : solitude, attente, télétravail, café, hôtel, petit matin, ville, témoignage posé, marque sobre, « un moment de calme ».
- **Ne marche pas pour** : énergie, fête, explication, enfants, beaucoup de texte.
- **Atout** : c'est le style le plus **léger à rendre** de la catégorie (≈ 13 ms par image) et l'un des plus simples à réussir.
- **À ne pas confondre** : `clair-obscur` est sombre, à la bougie ; ici il fait jour et la lumière a un bord net.

## 2. Palette, typographie, matières

| Surface | À l'ombre | Au soleil |
|---|---|---|
| Mur | `#5d8679` | `#efcf8f` |
| Soubassement | `#4b6d63` | `#d8ad68` |
| Sol | `#5b3d2b` | `#c98b52` |
| Vêtement (exemple rouge) | `#7a2c2a` | `#cc4a3c` |
| Cheveux clairs | `#a8893f` | `#f3d67e` |
| Blanc (tissu, pelage) | `#dcd6c8` | `#fbf6ea` |
| Brique de la rue | `#8a4230` | `#b4553a` |
| Peau | `#a9826c` | `#f1c49b` |
| Bois (table, comptoir, chaise) | `#6a4630` | `#d79a5e` |
| Bois foncé (pieds, chants) | `#4f3424` | `#b27643` |

Les trois dernières lignes (peau, bois) ne viennent pas de la source, qui n'en donnait pas : ce sont les teintes posées et jugées justes dans le rendu réel du 11/11/2026, construites sur la même règle. Pour une autre matière (métal, cuir, plante), fais de même : une version assombrie et tirée vers le vert, une version éclaircie et tirée vers le jaune.

- Règle : **ombre froide et verte, lumière chaude et jaune**, sur toute l'image. Jamais de noir pur.
- **Typographie** : sans-serif sobre et large (**Jost** ou **Outfit**, OFL) ou serif de journal (**Libre Caslon**) ; texte posé **dans le pan d'ombre**, clair, ou dans le pan de lumière, sombre.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Outfit à la place de Jost ; EB Garamond à la place de Libre Caslon ; Outfit : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/jost`, `@fontsource/libre-caslon-text` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : presque rien. Une trace de pinceau à peine visible : bruit étiré **verticalement**, calculé au quart de la résolution, en lumière douce à 20 %. Le mur est plat.

## 3. Composition 9:16

- Une pièce vue de face, un mur, un sol, une **fenêtre hors cadre ou sur un côté** d'où vient le soleil. En vertical : mur sur les 2/3 hauts, sol sur le tiers bas (ligne de sol vers y ≈ 1280).
- **Pan de lumière** : un grand quadrilatère sur le mur, prolongé par un autre sur le sol ; il doit couvrir 25 à 40 % du cadre et **traverser le sujet**.
- Sujet immobile, assis ou debout, ≥ 1/3 de la hauteur, de trois quarts ou de profil, regard hors champ. Beaucoup de vide autour.
- Par la fenêtre : une façade de briques, des fenêtres à stores tirés à des hauteurs différentes, une ombre dure de 10 px à droite de chaque ouverture.
- Sous-titres : sans-serif 46 à 52 px, crème, dans la partie ombrée du bas, y ≈ 1400 à 1520. Rien d'important à droite de x = 945.

## 4. Ce qui bouge

- **Action principale** : **le pan de soleil glisse** (≈ 95 px en 1,2 s dans la source ; plus lentement sur un plan long). Son bord traverse le visage : de moitié à l'ombre à entièrement éclairé.
- **Boucle de fond 1** : **l'ombre du sujet sur le mur** : sa silhouette, décalée (≈ +150, +18 px), apparaît en « mur à l'ombre » à l'intérieur du pan de lumière, et suit ses gestes.
- **Boucle de fond 2** : la rue et les détails : une enseigne à rayures qui tourne (≈ 60 px/s), le cordon d'un store qui se balance (±0,07 rad), ≈ 26 poussières visibles seulement dans la lumière, la vapeur d'une tasse.
- **Geste** : un seul, lent (porter une tasse à ses lèvres, tourner la tête vers la fenêtre).
- **Autorisés** : `#039` passage du temps (soleil qui tourne), `#175` plan fixe, `#027` avancée très lente, `#045` volet à bord net (comme transition : un bord de soleil qui balaie), `#182` tout net.
- **Interdits** : dégradés d'ombre, bords de lumière flous, `#024` secousse, `#043` panoramique filé, `#136` frémissement, grain fort, foule, sourire appuyé.
- **Transition signature** : un bord de soleil franc balaie le cadre et laisse la scène suivante derrière lui.

## 5. Rythme et montage

- Très posé : plans de 5 à 10 s, fixes. Une vidéo entière peut tenir en 3 ou 4 plans. La règle du studio « accroche avant 3 s » se tient ici **dans le plan**, par un évènement (le pan de soleil qui atteint le visage, un geste, un texte court), pas par une coupe.
- Le déplacement de la lumière **est** le rythme : cale l'arrivée du bord sur le visage avec le mot ou la note qui compte.
- Coupes franches, rares ; ou le volet de soleil.
- **Version courte (8 à 12 s)** : deux plans fixes de 4 à 5 s (ou trois de 3 s) ; dans chacun, le pan de soleil glisse dès la première image et **un seul geste** a lieu (une tasse levée, un store) ; la chute en texte tient 2 s. Accroche : un texte court à l'image 0 et le premier geste avant 3 s. (Découpage tenu dans le rendu réel du 11/11/2026.)

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D. Très léger.
- **Méthode « deux versions, une découpe »** :
  1. Une fonction `piece(g, K)` dessine le décor avec un jeu de couleurs `K`. On l'appelle deux fois, dans deux caches : version ombre et version soleil.
  2. À chaque image : dessiner la version ombre, puis **découper** la version soleil par les polygones de lumière (mur, sol).
  3. Le sujet et les meubles : dessinés une fois en couleurs d'ombre, puis redessinés en couleurs de soleil à l'intérieur de la bande de lumière.
  4. Ombres de croisillons de fenêtre : une barre verticale (≈ 24 px) et une barre parallèle au bord haut du pan.
  5. Ombre du sujet sur le mur : sa silhouette décalée, remplie avec la version ombre, à l'intérieur du pan.
- **Techniques clés** :
  ```js
  ctx.drawImage(OMBRE, 0, 0);                              // version à l'ombre
  ctx.save(); ctx.beginPath(); polygone(ctx, panMur(t)); polygone(ctx, panSol(t)); ctx.clip();
  ctx.drawImage(SOLEIL, 0, 0);                             // version au soleil, bord dur gratuit
  ctx.restore();
  const dx = 30 - 95 * easeInOut(t / dureePlan);           // le pan glisse
  ```
- **Pièges** :
  - Trace de pinceau horizontale à 35 % : le mur ressemble à du marbre veiné. Verticale, 20 %, à peine visible.
  - Sujet habillé et coiffé « adulte sévère » alors qu'on voulait quelqu'un de jeune : la silhouette (cheveux longs, un ruban) fait l'âge, pas le visage.
  - Blanc à l'ombre trop gris : il se lit comme un objet gris. Reste clair (`#dcd6c8`).
  - Un sujet entièrement dans l'ombre tout le plan reste terne : fais-le toucher par la lumière au moins une fois.

## 7. Son

- **Ambiance** : pièce silencieuse, rue lointaine (une voiture, un store qui claque), horloge, réfrigérateur.
- **Musique** : trompette avec sourdine ou saxophone seul, piano rare, contrebasse ; ou silence.
- **Bruitages** (≈ 3 par 10 s, volontairement peu) : tasse sur soucoupe, chaise, pas dans la rue, journal qu'on plie.
- Mix −14 LUFS ; laisse de vrais silences.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défaut connu de la source (trois étoiles) : un sujet secondaire resté dans l'ombre tout le plan. Erreurs : ombres en dégradé ; bord de lumière flou ; décor chargé ; noir pur ; mur texturé.

- [ ] Le bord entre ombre et lumière est net, partout.
- [ ] Chaque surface a deux couleurs : froide à l'ombre, chaude au soleil.
- [ ] Le pan de lumière se déplace pendant le plan et traverse le sujet.
- [ ] L'ombre du sujet est visible sur le mur éclairé et suit ses gestes.
- [ ] Les poussières ne sont visibles que dans la lumière.
- [ ] Au moins 40 % du cadre est vide (mur, sol).
- [ ] Texte sobre, dans une zone unie, hors y > 1560 et x > 945.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : fixe
- Couleurs max : 20
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt. Planche commune `assets/全风格总览.jpg` : composition empruntée, à ne pas utiliser comme vitrine. Film complet : Releases de https://github.com/alchaincyf/huashu-art-motion. Image fixe possible avec le moteur d'origine (`render.py --solo 24_hopper --stills`, non exécuté ici).
- À produire : notre propre aperçu 9:16 (style simple : bon candidat pour le premier rendu de contrôle de la catégorie).

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/24_hopper.md` (trois étoiles), `scripts/engine/scenes/24_hopper.js`. Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : carte traduite et généralisée ; style **renommé** (l'original porte le nom d'un peintre dont les droits sont encore actifs en Europe). Section 9:16, son.
- Vérifié par un rendu réel le 11/11/2026 (HyperFrames 0.9.33) : image conforme au style ; plans fixes et lumière lente refusés par l'ancienne porte (mouvement 1,7 %), d'où « Mouvement : calme » ; couleurs de peau et de bois ajoutées à la palette.
