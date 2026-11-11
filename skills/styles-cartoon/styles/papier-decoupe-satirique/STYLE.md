# Papier découpé satirique (style série animée)

> **État : style à valider.** La source est une « recette de recherche » : son auteur l'a notée ≈ 75/100, un relecteur indépendant ≈ 63/100 (seuil d'entrée au catalogue : 80). La fiche est utilisable, mais fais valider une image de style et un test de 6 s avant de la proposer comme style fini.

## 1. Identité

- **Nom** : Papier découpé satirique. Pour se comprendre avec le client : « style série animée en papier découpé ».
- **Inspiration** : les séries satiriques pour adultes animées en papier découpé (reconstruit en numérique) : grandes silhouettes géométriques, peu de traits de visage, jeu limité. On étudie le langage visuel, on ne reprend ni les personnages, ni la ville, ni les objets, ni les répliques ; et le look n'oblige pas à l'humour offensant.
- **Ce que c'est** : des **plaques de papier plates empilées**. Corps en trapèze, grosse tête ronde, **deux ovales blancs collés avec un point noir** pour les yeux, jambes en courts poteaux noirs, aplats avec fin contour noir, bords légèrement tremblés comme coupés aux ciseaux, fibres de papier discrètes. Les pièces **se déplacent d'un bloc ou pivotent autour d'un point** (cou, épaule).
- **Marche pour** : petit sketch, satire de bureau ou de voisinage, « ce que dit le client / ce qu'il veut dire », rappel de règles sur un ton pince-sans-rire, vidéo à faire vite avec peu de moyens.
- **Ne marche pas pour** : émotion sincère, beauté, produit haut de gamme, mouvement complexe (course, danse), scène à plus de 4 personnages en vertical.
- À ne pas confondre avec le `sitcom-sf` (trait qui frémit, personnages souples) ni avec les ombres chinoises (matière translucide, tiges).

## 2. Palette, typographie, matières

Valeurs relevées dans la scène d'essai de la source (indicatives, à adapter au sujet) :

| Rôle | Hex |
|---|---|
| Contour et jambes | `#14120F` · `#1C1A18` |
| Papier clair (neige, murs) | `#F6EFE0` · `#F2EDE0` · `#E9EEF0` |
| Ciel et lointains | `#BCD3E0` · `#A9B9C6` |
| Gris (route, mobilier) | `#8C9296` · `#D9D2C0` |
| Peau | `#F5CFA8` |
| Accents des vêtements | jaune `#F0B92A` · orange `#D6803A` · rose `#D65A7A` · sable `#E8D9A0` |

- **Chaque personnage a son identifiant de costume** (une couleur de bonnet, une forme de col), avec des proportions à lui. Évite les combinaisons de couleurs des personnages connus du genre.
- **Typographie** : une linéale grasse arrondie libre (**Baloo 2** ou **Fredoka**, OFL) pour sous-titres et cartons ; pas de lettrage d'effet.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Baloo 2 et de Fredoka. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/baloo-2`, `@fontsource/fredoka` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : grain de fibres de papier **attaché à chaque pièce** (il se déplace avec elle), ombre portée très courte et dure entre deux plaques (2 à 4 px), aucune lumière réaliste. Le papier ne devient ni de la 3D lisse ni une sculpture épaisse.

## 3. Composition 9:16

- Décor = quelques plaques : un sol, un fond, un ou deux éléments qui disent le lieu (arrêt de bus, comptoir, bureau). Personnages et objets partagent **la même échelle plate**, posés sur la même ligne de sol.
- Vertical : ligne de sol vers y 1250 ; **2 ou 3 personnages** de face côte à côte, hauts de 520 à 640 px (au moins 1/3 de la hauteur utile) ; têtes entre y 600 et 900.
- Pour un échange, alterne des plans à un seul personnage centré (tête ≈ 420 px de large) plutôt qu'un plan large.
- Sous-titres 54 px, blancs à contour noir 8 px, deux lignes maximum, vers y 1440. Carton de lieu ou de titre en haut (y 200 à 380), texte 80 à 100 px sur une plaque de papier.
- 16:9 : jusqu'à 5 personnages en ligne, plan fixe de face.

## 4. Ce qui bouge

- **Action principale** : un évènement simple et lisible (une porte qui s'ouvre d'un coup, un objet qui jaillit, un personnage qui saute dans un véhicule) suivi d'une réaction muette.
- **Boucle de fond 1** : une chute lente d'éléments de décor (neige, feuilles, papiers) animée « en deux ».
- **Boucle de fond 2** : clignements et petits déplacements de pupilles pendant l'écoute ; un élément du décor qui oscille (enseigne, feu).
- **Autorisés** : `#128` allure image par image, `#041` coupe sautée, `#046` coupe sèche, `#175` plan fixe, déplacement d'un bloc, pivot autour d'un point, petit saut vertical pour marcher, `#024` secousse courte à l'impact, `#189` plan de coupe sur un objet.
- **Interdits** : `#011` écrasement et étirement, `#136` trait qui frémit, `#016` parallaxe, mouvements de caméra amples, `#044` fondu enchaîné, dégradés, flou de mouvement, interpolations douces (une pièce saute d'une position à l'autre en 1 ou 2 dessins).
- **Bouche** : demi-ovale noir qui s'ouvre et se ferme sur les syllabes ; quelques formes suffisent, mais elles doivent suivre la voix.
- Jeu limité ne veut pas dire glissade de marionnette : l'information passe par les **changements de pose, le regard et les pauses**. Un pas a un état d'appui, pas seulement une translation du groupe.

## 5. Rythme et montage

- Plans fixes de 2 à 4 s, coupes sèches. Le montage fait le rythme, pas la caméra.
- Structure courte en trois temps : situation banale, évènement, réaction (un regard caméra tenu 1 s vaut une réplique).
- La vitesse des actions suit le récit : le calme de l'image n'impose pas le ralenti. Un geste brusque en 2 dessins après une longue immobilité est le ressort comique du style.
- Durée conseillée : 15 à 40 s.
- **Version courte (8 à 12 s)** : trois plans fixes : situation (3 s), évènement (2 s), réaction avec regard caméra tenu 1 s ; couper le carton de lieu et le second échange. Accroche avant 3 s : si la situation dure 3 s, l'évènement commence dans ce même plan.

## 6. Recette technique

- **Moteur** : HyperFrames. Deux voies : canvas 2D (une fonction par pièce), ou pièces en SVG / `<div>` positionnées par une timeline GSAP en pas francs (`ease: "steps(1)"`).
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `papier.js` (découpe à bord tremblé, fibres), `perso.js` (pièces, pivots, états d'expression), `decor.js`, `scenes.js`.
- **Techniques clés** :
  ```js
  // bord « aux ciseaux » : décaler chaque point du contour avec un hasard à graine
  // attaché à la pièce (le bord ne change pas d'une image à l'autre)
  function decoupe(points, graine, amp = 1.6) { /* renvoie un Path2D */ }

  // personnage = pièces + pivots ; l'animation ne touche que des angles et des décalages
  perso({ tete: { rot: -0.08 }, brasG: { rot: 0.6, pivot: "epaule" }, bouche: ouverture(tq) });
  ```
  - Yeux : deux ovales blancs qui se touchent, collés sur le visage ; pupille = un point noir dont seule la position change.
  - Ordre d'empilement fixe : jambes, corps, bras, tête, yeux, coiffe.
  - Hasard toujours à graine : la même image rendue deux fois doit être identique au pixel.
- **Pièges** (relevés par l'auteur de la source) : tous les personnages sortent du même moule (varie tailles, largeurs et costumes) ; monter dans un véhicule réduit à une translation plus un saut ; bouche qui ne suit pas le dialogue. Texture de papier qui « glisse » sous la pièce si elle est attachée à l'écran au lieu de la pièce.

## 7. Son

- **Voix** : c'est un style parlé. Débit rapide, ton plat ; une voix par personnage, nettement différentes.
- **Musique** : presque rien : un court jingle guilleret au début (guitare acoustique, banjo ou piano droit) et à la fin ; silence ou ton de pièce pendant le dialogue.
- **Bruitages** (≈ 3 à 5 par 10 s) : secs et réalistes, en décalage avec l'image naïve : porte, bip, « pop », pas dans la neige ou sur le lino, objet qui tombe.
- **Ambiance** : extérieur calme (vent, oiseaux lointains) ou intérieur (néon, ventilation). −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : interpolations douces qui donnent un rendu « animation vectorielle », personnages clonés, glissade sans appui, bords trop nets, volume ou ombres réalistes.

- [ ] Chaque forme a un bord légèrement irrégulier et un grain de papier qui la suit.
- [ ] Les yeux sont deux ovales blancs à point noir, sans reflet.
- [ ] Les pièces changent de position par sauts de 1 ou 2 dessins, sans interpolation longue.
- [ ] Aucun écrasement, aucun étirement, aucun dégradé.
- [ ] La bouche s'ouvre sur les syllabes de la voix.
- [ ] Au moins trois personnages se distinguent par la taille, la largeur et le costume.
- [ ] Plans fixes ; au plus un mouvement de caméra dans tout le film.
- [ ] Aucun personnage, lieu ou costume d'une série existante ; test de 6 s validé par un regard neuf.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : fixe
- Couleurs max : 14
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Aucun aperçu publié pour ce style dans le dépôt d'origine (recette de recherche). Aperçu à produire par un rendu réel 9:16 avec le plugin.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/52_south_park.md` (carte traduite du chinois, sections « langage visuel transférable » et « v2 »), `scripts/engine/scenes/52_south_park.js` (couleurs relevées). Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : traduction, nom descriptif, composition 9:16, voie GSAP en pas francs, numéros du dictionnaire. Les sections 3, 5 et 7 sont des propositions de Flot Web, la source ne les fixe pas.
