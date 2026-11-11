# Diorama Memphis

## 1. Identité

- **Nom** : Diorama Memphis. (« Memphis » désigne le mouvement de design italien des années 80, pas une marque.)
- **Inspiration** : ce mouvement de design (primaires saturées à côté de pastels ; pois, zigzags et éclats de terrazzo sur chaque surface), les maquettes d'architecture et de train (un lieu entier vu d'en haut, d'un coup), les villes des livres d'images (chaque fenêtre a sa jardinière, il se passe quelque chose à chaque coin), la trame de risographie (l'ombre comme un champ de points). On n'en reprend ni les objets, ni les plans, ni les palettes, ni la musique.
- **Ce que c'est** :
  - **du papier et un cadre granuleux** : fond blanc chaud ; l'image vit dans un cadre arrondi et organique dont le bord se dissout en grain ; il s'ouvre depuis le centre au début, se referme à la fin ;
  - **de la couleur plate** : primaires saturées et pastels, aplats, aucun dégradé ; contour d'encre indigo profond ; petits motifs sur les surfaces ;
  - **l'œil du maquettiste** : vues hautes de trois quarts, du dessus ou en coupe. Le film regarde toujours un **lieu**, jamais une personne ;
  - **de petits mouvements partout** : eau, vent dans les arbres, ombres de nuages, oiseaux, bateaux, passants, lumières qui s'allument une à une ;
  - **trois lignes de texte sous le cadre**, sous trois marques (un point jaune, un triangle rose, un zigzag bleu).
- Calme, lumineux, chaleureux : un lieu qu'on regarde, pas une histoire qu'on suit.
- **Marche pour** : un quartier, un village, un site d'entreprise, les saisons d'un lieu, la nuit qui tombe rue par rue, une carte de couverture ou de livraison, le fonctionnement d'un bâtiment en coupe, une boucle d'ambiance pour un site ou un direct.
- **Ne marche pas pour** : personnages qui jouent (les visages et les gestes faits en code sont toujours raides : ce style ne les montre jamais), récit à suspense, produit en gros plan, humour de dialogue.
- Ce n'est ni une infographie isométrique (froide, schématique), ni du tilt-shift (ni photo ni flou), ni du low-poly (ni facettes ni reflets plastiques).

## 2. Palette, typographie, matières

| Rôle | Hex |
|---|---|
| Papier (tout ce qui est hors du cadre) | `#FFFCF6` |
| Encre (contours, texte, pneus, cadres de fenêtres) | `#25214A` |
| Lumière des fenêtres et des lampes | `#FFD36E` |
| Voile du crépuscule | `#FF9E7A` |
| Exemple de gamme | jaune `#FFD234` · rose `#FF7EB3` · ciel `#5CC8FF` · menthe `#5EDFB0` · lilas `#B9A0FF` · pêche `#FF9C6B` · cobalt `#2F5BFF` · corail `#FF5A5F` · vert `#2FCB7A` |

- **5 à 7 teintes saturées + 2 ou 3 pastels** portent l'image. **Regroupe la couleur par zones** : blocs voisins de teintes différentes, part de chaque couleur maîtrisée. Laisse de **grandes zones calmes** d'une seule couleur (eau, champ, place).
- **Trois tons seulement** par objet : dessus le plus clair, côtés au soleil à la couleur de base, faces à l'ombre à ×0,5-0,95. Arêtes dures.
- **Ombres dures**, jamais floues, teintées d'un **violet froid** (ombre ≈ base × (0,70 ; 0,58 ; 0,90)) ; la direction du soleil ne change jamais dans un film. **Trame de points dans l'ombre** : elle change les zones sombres en texture au lieu de saleté.
- **La nuit est un glissement de luminance vers le violet**, pas un assombrissement général (les jaunes ne virent pas à l'olive). Une scène de nuit entière tombe dans la zone bleu-violet : garde-la **courte**, pleine de lumières chaudes, ou prévois la dérogation (`styles-jeu-retro/references/derogation-bleu-violet.md`).
- Saisons et heures ne changent que les grandes surfaces (sol, feuillages, toits, eau). L'hiver n'est pas tout blanc : feuillages lilas pâle, bleu glacier et menthe à pois blancs ; les maisons gardent leurs couleurs.
- **Typographie** (OFL) : **Inter Tight** (texte), **IBM Plex Mono** (données).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place d'Inter Tight ; IBM Plex Mono : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/inter-tight` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Le détail se construit, il ne se texture pas** : une maison = un socle, des murs à rayures de planches, des chaînages d'angle blancs, deux pans de toit et un faîtage, un pignon à fenêtre ronde, des fenêtres à volets et jardinières, une porte avec sa marche, son auvent et sa lampe. Un arbre = un tronc et une grappe de lobes, plus des lobes clairs côté soleil ; **au moins cinq formes de couronne**.
- **Jamais** : profondeur de champ, vrais reflets, lueur, flou de mouvement, lumière volumétrique. Une lampe allumée = une couleur chaude plate + une flaque de lumière chaude à bord dur sur le sol.

## 3. Composition 9:16

- Original : cadre d'environ 1520×744 px, un peu au-dessus du centre d'une image 16:9, texte en dessous. En vertical (à vérifier par rendu) : **cadre organique de 960×1180 px**, centré en x 540, de y 220 à 1400, sur papier blanc chaud ; **les trois lignes de texte entre y 1420 et 1540**, sous les trois marques.
- Le lieu se construit pour la hauteur : une rue qui monte, une rivière qui traverse l'image de haut en bas, une colline, un immeuble en coupe.
- **Trois lignes centrées sous le cadre** : ligne 1, le titre (graisse 600, ≈ 36 px, sombre) ; ligne 2, une phrase (graisse 400, ≈ 30 px, gris) ; ligne 3, une petite donnée en chasse fixe (heure, lieu, coordonnées ; 28 px, gris clair). La source descendait à 26 et 22 px : relevé, 28 px étant le plancher de lecture du studio. Les lignes 2 et 3 sont facultatives ; une ligne vide laisse sa place vide. Elles ne bougent jamais ; quand une ligne change, l'ancienne s'efface et la nouvelle apparaît (≈ 0,4 s chacune).
- En général **pas de voix : le texte est la narration.** Avec une voix : sous-titres simples en bas, sans boîte stylisée.
- **Étiquettes** d'explication : pastille arrondie avec filet et point, qui jaillit de la maquette avec un dépassement et s'efface ensuite.
- Les gens sont un **décor lointain** : petits, en cycle de marche, un cerf-volant, une barque. Aucun gros plan.

## 4. Ce qui bouge

- **Action principale** : **la vague** : un anneau s'étend depuis un point ; tout ce qu'il traverse passe à son état suivant (les couleurs changent à l'intérieur du rayon ; les objets poussent, s'ouvrent, tombent ou s'allument quand l'anneau les atteint).
- **Boucles de fond** (toutes procédurales et bouclées, chacune avec sa phase) : eau, arbres, ombres de nuages, feuilles, neige, fumée, vols d'oiseaux, véhicules qui accélèrent, freinent et piquent du nez.
- **Autorisés** : `#030` orbite ou dérive haute et lente, `#181` vue du dessus qui tourne lentement, `#175` cadre fixe de trois quarts, `#027` avancée lente vers un détail, `#174` suivi d'un véhicule, `#017` transition par masque (le cadre se referme et se rouvre), `#010` dépassement des choses qui apparaissent, `#121` anticipation (**un repère s'écrase puis se détend** avant tout changement d'état), `#127` boucle parfaite, `#143` coupe du sol ou d'un bâtiment (en deux temps).
- **Interdits** : `#046` coupe sèche rapide, flash blanc, rotation de transition, `#105` flou d'arrière-plan, `#022` balayage de lumière, lueur, flou de mouvement, jeu d'acteur, saccade (seul le grain du cadre frémit « en deux »), apparition sèche (les choses poussent ou rebondissent en place), caméra qui traverse un objet.
- **Les formes peuvent être simples ; le mouvement, non.** Tout est amorti ; les virages suivent des courbes, jamais des lignes brisées.
- **Ne bougent jamais** : la position du cadre, celle du texte, le papier, la direction du soleil.

## 5. Rythme et montage

- **Préfère une seule prise continue**, assez lente pour que le spectateur puisse s'arrêter sur n'importe quel coin. Quand un long plan doit tenir une composition, ralentis la caméra plutôt que de laisser le lieu sortir du cadre.
- **Trois transitions seulement** : le cadre se referme et se rouvre ; une vague balaie (couleur, lumière, saison) ; le sol est ouvert en coupe.
- Un changement d'état est **annoncé** : un repère (une fontaine, une cheminée, une horloge) s'écrase, se détend, et la vague part de lui. C'est la façon de dire « ceci cause cela » sans personnage.
- Une saison ou un état : 8 à 12 s. Film : 20 à 45 s, ou boucle sans fin.
- **Version courte (8 à 12 s)** : un seul état et une seule vague, en une prise continue ; le titre seul (ligne 1). Accroche : l'anneau de la vague part avant 3 s.

## 6. Recette technique

**Moteur conseillé : Three.js** : le style n'utilise **aucune lumière réaliste** ; tout repose sur un matériau plat à trois tons, une passe de contour et des motifs calculés dans l'espace du monde. **Blender** (connecteur MCP `blender`) seulement pour un lieu très riche, avec un rendu « dessin » (ombrage plat, contours).

| | Three.js (conseillé) | Blender |
|---|---|---|
| Matériau | shader plat maison : 3 tons par face, ombre violette dure, trame de points dans l'ombre, motifs (pois, rayures, zigzag, hachures) en coordonnées du monde | ombrage « toon » à paliers par nœuds ; motifs par textures procédurales en coordonnées objet |
| Contour | passe d'écran depuis les normales et la profondeur, ≈ 2 px indigo à 1080 de large | contours de rendu (lignes calculées), plus lents |
| Vague | deux couleurs par matériau + un rayon : échange par pixel | à animer objet par objet ou par nœuds pilotés par la distance |
| Cadre et texte | cadre granuleux et 3 lignes dessinés en 2D par-dessus | à ajouter dans HyperFrames par-dessus la suite d'images |
| Coût | rapide, déterministe | plus long, sans gain visible sur ce style |

- **Structure** : `memphis` (matériau plat, contour, cadre, texte du bas), `passants` (marcheur lointain), `lieu` (maisons, arbres, eau, véhicules : propre à chaque film), `film` (caméra, vagues, saisons).
- **Techniques clés** :
  ```js
  // un matériau porte son état suivant ; la vague l'échange à l'intérieur d'un rayon
  const herbe = plat("#6FD889", { col2: "#D6E68E", motif: "pois", motifCol: "#9DE8A6" });
  vague.centre.set(x, z); vague.rayon = rayonMax * easeInOut(u);   // u : 0 -> 1
  // nuit ou jour par zones = la même vague, avec couleur de nuit et couleur de jour
  ```
  - **Les motifs appartiennent au monde** : calculés en coordonnées du monde, ils restent sur l'objet qui bouge ; leur échelle grandit avec la distance pour que le lointain ne fourmille pas.
  - Cônes de lumière, particules (pluie, neige, pétales, fumée) et tiges fines **sans contour** : un objet fin tout en contour se lit comme un gribouillis.
  - **Les objets héros ne reçoivent pas d'ombre** quand ils passent dans une zone ombrée, sinon ils ont l'air sales.
  - **Coupe : à construire soi-même.** La partie proche est son propre groupe (un mur de façade, un toit, une tranche de sol épaisse) ; ce qui est derrière est modélisé pour de bon (étages meublés, couches de sol, tuyaux) ; les faces coupées sont hachurées, un cran plus foncées. La partie proche s'en va **en deux temps** (monter puis reculer, ou s'enfoncer droit), et revient en sens inverse.
- **Pièges** : jour gris au lieu de « réconfortant » (monte la saturation, réchauffe, ombres violettes) ; couleurs semées au hasard ; tous les arbres pareils ; grandes ombres lues comme de la saleté ; long plan qui dérive jusqu'à perdre le sujet ; changement d'état qui arrive « tout seul ».

## 7. Son

- **Chaud, doux et continu** : piano, piano électrique, marimba, célesta, boîte à musique, basse synthétique douce, nappe chaude, balais et shaker.
- **Un seul morceau, pas un pot-pourri** : quand le lieu change (saison, jour vers nuit), garde harmonie et tempo, change seulement l'épaisseur de l'accompagnement.
- **Les bruitages sont le son des petites choses**, sous la musique (vrais enregistrements ; ≈ 5 par 10 s) : oiseaux, canards, eau, sonnette de vélo, gouttes, feuilles, vent, neige, le « ting » d'une lumière qui s'allume (accordé sur l'accord en cours).
- **Le même évènement fait toujours le même son** : si chaque changement d'état commence par un écrasement, chaque écrasement a le même choc sourd, le même ressort, la même harpe montante.
- Le silence est permis, avec un léger ton de pièce dessous. −14 LUFS, crête ≤ −1 dB ; les fondus suivent l'ouverture et la fermeture du cadre.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Fond papier blanc chaud ; l'image vit dans un cadre organique à bord granuleux qui s'ouvre et se referme.
- [ ] Aplats, contour indigo, ombres dures violettes avec trame de points ; aucun dégradé, flou ou lueur.
- [ ] Aucun personnage en gros plan, aucun jeu d'acteur.
- [ ] Au moins cinq petits mouvements bouclés visibles en même temps, chacun à sa phase.
- [ ] Tout changement d'état est annoncé par un repère qui s'écrase et se détend, puis se propage en vague.
- [ ] De grandes zones calmes d'une seule couleur ; couleurs regroupées par zones.
- [ ] Texte sous le cadre, immobile, hors zones d'interface ; au plus trois lignes.
- [ ] Part de nuit mesurée (interdit bleu-violet) ; aucune coupe sèche rapide.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 13
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu

- Film de démo d'origine *Four Seasons in Pomelo Town* (45 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/memphis-diorama.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/memphis-diorama.jpg
- Crédit : style et démo par **Eian** (https://github.com/YIAN6557), contribution à Lemo-Opuscar ; LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/memphis-diorama/STYLE.md`, `DEMO.md`, `demo/memphis.js`, `people.js`, `demo/CREDITS` (moteur d'origine : three.js r170). Style contribué par Eian. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Polices Inter Tight, IBM Plex Mono (SIL OFL 1.1).
- Adaptation Flot Web : traduction, cadre et tailles de texte 9:16, texte en une seule langue (la source prévoit un couple chinois / anglais), tableau des moteurs (voie Blender non testée), mise en garde bleu-violet, numéros du dictionnaire.
