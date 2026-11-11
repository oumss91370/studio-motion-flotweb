# Lumière d'anime (style Shinkai)

## 1. Identité

- **Nom** : Lumière d'anime (style Shinkai). « Style Shinkai » est un repère d'inspiration : aucun personnage, décor ou plan de film n'est repris, le nom n'apparaît jamais dans la vidéo, et le style n'est jamais présenté comme officiel ou affilié.
- **Inspiration** : l'animation japonaise des années 2010 où **la lumière est le personnage principal** : cumulus d'été gigantesques, rayons qui tombent d'une fenêtre, reflets d'objectif, poussière dorée, décors très réalistes et personnages en aplats aux ombres franches.
- **Ce que c'est** : un **décor quasi photographique** (dégradés chauds et froids, perspective juste, objets du quotidien : fils électriques, toits, calendrier, cadre de fenêtre en aluminium) traversé par une lumière spectaculaire, et des **personnages en cellulo** : couleur de base, **bande d'ombre à bord dur**, **liseré de lumière**, trait fin brun.
- **Marche pour** : nostalgie, adolescence, été, rendez-vous manqué, distance, départ, ville le soir, marque qui parle de temps et de souvenirs, moment de pause dans une vidéo.
- **Ne marche pas pour** : humour, explication, sujet rugueux, intérieur sans fenêtre (le ciel est indispensable).
- **À ne pas confondre** : `aquarelle-ghibli` est peinte à la main, mate, sans effet d'optique ; `lumiere-diner-americain` (catégorie « Peinture et dessin ») a des pans de soleil mais ni ciel, ni reflets, ni cellulo.

## 2. Palette, typographie, matières

| Rôle | Hex (source) |
|---|---|
| Peau : base / ombre | `#ffe8dc` / `#f2b6a8` |
| Cheveux clairs : base / ombre | `#f8d681` / `#d8a050` |
| Blanc d'un vêtement : base / ombre | `#fbfbfe` / `#b9c3dc` |
| Bleu marine : base / ombre | `#2c3a66` / `#1b2446` |
| Trait | `#6a4632`, 2,2 px |
| Nuage : silhouette | `#b7c6e6` → `#8297c6` ; boule de lumière blanche |
| Iris (yeux d'anime) | `#1f3f7a` → `#3f7fd0` → `#9fd4ff` |
| Liseré chaud en contre-jour | `rgba(255,220,160,.55)` |
| Reflet sur les cheveux | `rgba(255,250,226,.85)` |

- Étalonnage final : **séparation chaud / froid** en lumière douce (ombres vers le bleu, lumières vers l'orangé).
- **Attention à la porte de livraison** : ciel bleu et ombres bleutées. Le bleu de ciel (≈ 210°) passe ; évite de tirer les ombres vers le violet, et garde une vraie part de lumière chaude (soleil, mur éclairé, peau).
- **Typographie** : sans-serif fine et moderne (**Zen Kaku Gothic New**, **Noto Sans** léger, OFL), blanche, petite, interlettrage large, posée dans le ciel ; une ligne, deux au plus.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place de Zen Kaku Gothic New et de Noto Sans. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/zen-kaku-gothic-new`, `@fontsource/noto-sans` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : décor lisse aux dégradés propres ; **halo** général (l'image entière, réduite, floutée de 6 px, éclaircie, superposée à ≈ 28 % en mode « écran ») ; poussières lumineuses ; gouttes sur une vitre.

## 3. Composition 9:16

- **Le ciel prend la moitié du cadre ou plus** : le vertical est idéal. Un cumulus géant dans les deux tiers hauts ; en bas, un bord de fenêtre, un toit, une rue, des fils électriques qui traversent.
- Personnage de dos ou de trois quarts, **petit par rapport au ciel** mais ≥ 1/4 de la hauteur ; souvent en contre-jour (liseré chaud sur la tête et les épaules).
- **Le soleil est à l'intérieur de la vitre ou du ciel**, jamais sur un coin de cadre de fenêtre (sinon le halo déborde sur le mur comme une lampe accrochée). Halo du soleil ≤ 130 px de rayon en 16:9 (≈ 160 px en vertical).
- Un **pan de lumière en forme de fenêtre** sur le sol et le mur, avec l'ombre d'un voilage qui bouge dedans.
- Sous-titres : blanc 44 à 50 px avec ombre douce, y ≈ 1400 à 1520, sur une zone sombre du bas. Rien d'important à droite de x = 945.

## 4. Ce qui bouge

- **Action principale** : presque rien : un regard qui se lève, une main sur une vitre, un pas, des cheveux dans le vent. Le plan repose sur la lumière.
- **Boucle de fond 1** : **le nuage vit** : 70 à 80 boules dont le rayon respire (`0,05·sin(1,3·t)`), l'ensemble dérive (≈ 10 px/s).
- **Boucle de fond 2** : **l'optique** : rayons qui s'allument et s'éteignent doucement (`0,75 + 0,25·sin(3,4·t)`), une soixantaine de poussières lumineuses qui scintillent, étoile du soleil qui tourne très lentement (0,25 rad/s), reflets d'objectif alignés.
- **Détails** : traînée d'avion, vol d'oiseaux, une goutte qui glisse sur la vitre en laissant sa trace, voilage blanc et son ombre sur le mur, plante qui bouge.
- **Autorisés** : `#097` contre-jour, `#098` liseré de lumière, `#109` reflet d'objectif, `#103` lumière dorée, `#104` heure bleue, `#105` flou de fond, `#033` bascule de mise au point, `#031` grue qui monte vers le ciel, `#026` panoramique vertical, `#027` avancée lente, `#037` ralenti, `#022` balayage de lumière oblique (comme transition).
- **Interdits** : `#024` secousse, `#043` panoramique filé, trait épais, ombres en dégradé sur les personnages, reflets d'objectif partout, ciel plat sans nuage.
- **Transition signature** : un balayage de lumière oblique qui blanchit le cadre.

## 5. Rythme et montage

- Contemplatif : plans de 4 à 8 s, souvent fixes ou en très lente montée.
- Un montage plus serré de **détails** (3 à 4 plans de 1 à 1,5 s : un fil, une goutte, une main, un panneau) avant le grand plan de ciel : c'est une structure typique.
- Musique en montée ; le plan de ciel tombe sur le temps fort.
- Le mouvement visible ne couvre qu'environ 3 % de l'image : ajoute un geste franc ou un mouvement de caméra pour passer la porte anti-diaporama.
- **Version courte (8 à 12 s)** : le montage serré de trois détails (1 s chacun), puis le grand plan de ciel de 5 à 6 s sur le temps fort ; couper les plans fixes d'installation. L'accroche est la série de détails coupés à la seconde.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D ; ≈ 70 ms par image. Pour un décor très réaliste en profondeur, tu peux construire la pièce dans Blender et ne garder en canvas que le ciel, les personnages et l'optique.
- **Ordre des couches** : intérieur réaliste (cache) → ciel, cumulus, poteaux et fils, toits, avion, oiseaux → gouttes sur la vitre → voilage → pans de lumière au sol et au mur → plantes → personnages (cellulo) → vapeur → rayons et poussières → reflets d'objectif → halo général → séparation chaud / froid.
- **Techniques clés** :
  ```js
  // cellulo : base, ombre = forme MOINS (forme décalée vers la lumière), liseré = forme MOINS (forme décalée à l'opposé)
  function cellulo(c, p, base, ombre, lisere, { sd, rw, lx, ly }) { /* découpes "evenodd" */ }
  // lumière venant de la fenêtre : lx = -1, ly = -0.55 ; sd : grandes pièces 22-30, visage 10, petites 8 ; rw 3-9
  // cumulus : 1) silhouettes gris-bleu  2) une boule blanche décalée vers le soleil dans chaque boule
  //           3) tout le calque flouté de 3 px, plus 55 % du calque net par-dessus
  // halo : image réduite au quart -> flou 6 px, luminosité 1,1 -> "screen" à 0,28
  ```
  - Remplis, ombre, liseré, trait **pièce par pièce dans l'ordre d'empilement** : les recouvrements sont justes sans calcul de lignes cachées.
  - Reflets d'objectif : 5 hexagones sur la droite soleil → centre de l'image, à 0,45 / 0,75 / 1,25 / 1,6 / 2,0 fois la distance, opacité 0,04 à 0,12 ; un trait horizontal fin limité au voisinage du soleil.
  - Rayons : 3 coins floutés de 18 px, en cache, mode « écran ».
- **Pièges** :
  - Nuage fait d'un dégradé radial par boule + un arc « éclairé » : un tas de bulles de savon. Il faut **silhouette + boule de lumière décalée + deux couches floue et nette**.
  - Trait de lumière horizontal de toute la largeur : on dirait un défaut d'affichage. Limite-le près du soleil, opacité ≈ 0,35.
  - Goutte en disque plein : une bulle dans le ciel. Seulement l'arc du bas, un corps à 22 % et un point de reflet.
  - Soleil sur le coin de la fenêtre : lampe accrochée au mur.
  - Deux variables du même nom dans une scène : elle ne se charge plus, parfois sans message. Vérifie la console.

## 7. Son

- **Ambiance** : ville d'été : cigales, passage à niveau lointain, train, vent chaud, pluie qui s'arrête ; puis, sur le plan de ciel, presque plus rien.
- **Musique** : piano avec réverbération, cordes qui montent, guitare acoustique ; une montée vers le plan de ciel.
- **Bruitages** (≈ 3 à 5 par 10 s) : goutte, pas sur le bitume mouillé, sonnerie de passage à niveau, froissement d'un voilage, un souffle d'air au moment où la lumière entre.
- Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défaut connu de la source (deux étoiles) : **décor intérieur pas assez dense**. Ajoute des objets vrais (fils, étiquettes, calendrier, vaisselle) ou construis le décor dans Blender. Erreurs : nuages-bulles ; reflets partout ; ombres douces sur les personnages ; ciel vide.

- [ ] Le ciel occupe au moins la moitié du cadre ; un cumulus a un côté éclairé net et un côté gris-bleu.
- [ ] Personnages : base + bande d'ombre à bord dur + liseré de lumière, trait fin brun.
- [ ] La direction de la lumière est la même pour le décor, les ombres et les liserés.
- [ ] Le soleil et son halo restent dans le ciel ou dans la vitre.
- [ ] Rayons, poussières et reflets : présents, mais discrets (opacités de la recette).
- [ ] Halo général et séparation chaud / froid appliqués.
- [ ] Au moins 8 objets du quotidien identifiables dans le décor.
- [ ] Aucun personnage, lieu ou plan emblématique d'un film ; aucun nom à l'image.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 14
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 44

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt. Planche commune `assets/全风格总览.jpg` : composition empruntée, à ne pas utiliser comme vitrine. Film complet : Releases de https://github.com/alchaincyf/huashu-art-motion. Image fixe possible avec le moteur d'origine (`render.py --solo 35_shinkai --stills`, non exécuté ici).
- À produire : notre propre aperçu 9:16.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/35_shinkai.md` (deux étoiles), `scripts/engine/scenes/35_shinkai.js`. Licence MIT, © 花叔 Huashu.
- Repères de lumière et d'optique : entrées `#097`, `#098`, `#103` à `#105`, `#109` du dictionnaire motion-prompt (© 2026 Shohei Ohtaki, MIT), via le skill `principes-mouvement`.
- Adaptation Flot Web : carte traduite et généralisée (l'uniforme scolaire de la scène d'origine n'est pas repris), section 9:16, option Blender pour le décor, son.
