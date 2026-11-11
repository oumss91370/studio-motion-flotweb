# Animé sur cellulo années 80

## 1. Identité

- **Nom** : Animé sur cellulo années 80.
- **Inspiration** : l'animation japonaise peinte à la main de la fin des années 80 (films vidéo et séries), dans son ensemble : contraste décor peint / cellulo plat, lumière qui traverse l'image, dessins tenus, grammaire de la vitesse, génériques « city pop ». On emprunte le métier de l'époque, jamais les personnages, engins, logos, lieux ou plans d'une œuvre précise.
- **Ce que c'est** : quatre couches, et c'est leur contraste qui fait le look.
  1. **Décor peint** : dégradés à l'aérographe, fenêtres allumées, reflets mouillés ; peint une fois, puis seulement glissé.
  2. **Cellulo** (personnages, véhicules, objets) : aplats, ombre et lumière à **bord dur**, contours **colorés**, jamais noir pur ; 15 ou 10 dessins par seconde à 30 i/s (12 ou 8 dans un film livré à 24 i/s).
  3. **Lumière** : enseignes, lampes, titres qui brillent *à travers* l'image ; reflets d'objectif, halo.
  4. **Lecture** : cassette vidéo sur tube cathodique (bavure de couleur, lignes, lueur de phosphore, coins assombris).
- Si l'image ressemble à de l'animé numérique moderne, il manque une couche.
- **Marche pour** : nuit en ville, voyage, course, souvenir, premier jour dans un grand lieu, annonce d'un résultat, musique et nostalgie.
- **Ne marche pas pour** : tutoriel pas à pas, données, humour de dialogue rapide, sujet enfantin, client qui veut un rendu « propre et net ». Ce n'est pas du « moe » (yeux ronds géants), ni du vectoriel, ni un pastiche de pellicule (pas de rayures : c'est une cassette).

## 2. Palette, typographie, matières

Chaque heure du jour a son **modèle de couleurs** complet (jamais un filtre posé sur l'image). Exemples :

| Ambiance | Couleurs (indicatives) |
|---|---|
| Nuit en ville | indigo `#1B1A4A`, violet profond `#3A1F66`, magenta néon `#FF3FA4`, cyan `#3FE0F0`, or des fenêtres `#FFC860` |
| Aube | pervenche `#8E9BE0`, rose `#F29BB2`, pêche `#FFC9A3`, or pâle `#FFE6A8` |
| Midi au bord de mer | cobalt, cumulus blancs, sable, corail |

- Dérivation depuis le modèle « jour » : nuit éclairée ×[0,78 ; 0,74 ; 1,0], nuit ombre ×[0,58 ; 0,52 ; 0,92], aube éclairée ×[1,04 ; 0,9 ; 0,84]. **La peau a sa propre couleur dans chaque modèle** (sinon les visages virent au rose sous un néon). Trait de peau ≈ `#5A2E2E`, trait des cheveux violet foncé ; seuls les objets durs ont un trait presque noir.
- Le héros porte **une couleur d'accent** (une écharpe corail, par exemple) lisible dans tous les modèles.
- Cette palette nocturne est bleu-violet par nature : voir la dérogation décrite dans `styles-jeu-retro/references/derogation-bleu-violet.md` (catégorie « Jeu vidéo et rétro »), à déclarer de la même façon à la porte de livraison.
- **Typographie** (OFL) : sous-titres en **Barlow Semi Condensed 600**, jaune crème `#FFF0A0`, contour sombre épais ; titre en italique gras à dégradé chromé (ciel → ligne d'horizon blanche → violet → rose → or) avec double contour sombre et néon ; ligne décorative possible en **Dela Gothic One** ; **Kanit** pour les étiquettes.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Oswald à la place de Barlow Semi Condensed. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/barlow-semi-condensed` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Dessin des visages** : tête construite (sphère + mâchoire), visage en œuf allongé, yeux en amande au milieu de la tête, cil supérieur épais qui remonte vers l'extérieur, iris ovale en couches, deux reflets, sourcils longs et fins, nez = un plan d'ombre + un trait. Cheveux en mèches qui se chevauchent, avec un reflet continu en zigzag.

## 3. Composition 9:16

- Le vertical convient très bien aux **décors hauts** : descente de grue le long d'une tour, d'un phare, d'une falaise. Peins les décors en 1080×2600 ou plus pour pouvoir glisser dessus.
- Petit héros plat dans un grand monde peint : personnage à 1/3 de la hauteur dans les plans de jeu, gros plan des yeux en bandeau horizontal (y 600 à 1000) pour les décisions.
- Sous-titres 50 à 56 px, composés **dans la passe cathodique**, centrés vers y ≈ 1480 ; garder vide y > 1560 et x > 945. Un second personnage peut avoir une seconde couleur (cyan `#8FF4FF`) et une petite étiquette encadrée.
- Titre : 130 à 170 px sur deux lignes, entre y 300 et 700, qui s'allume par paliers, 15 par seconde, avec un balayage de lumière.
- 16:9 : plein cadre ; bandes 4:3 possibles pour un parfum « vidéo ».

## 4. Ce qui bouge

- **Action principale** : un trajet ou une attente dont l'enjeu est une décision (partir, sauter, appeler).
- **Boucle de fond 1** : cheveux et tissus en rubans pilotés par une onde qui se déplace, cycle de 4 dessins (6 quand c'est calme).
- **Boucle de fond 2** : lumière qui bouge sur un dessin tenu (bandes colorées qui balaient le cellulo), pluie, scintillement des enseignes.
- **Autorisés** : `#016` parallaxe (3 ou 4 couches en travelling latéral), `#031` grue sur un décor haut, `#022` balayage de lumière, `#040` arrêt sur image d'un temps, `#184` très gros plan des yeux, `#033` bascule de point, `#109` reflet d'objectif, `#111` bavure de couleur (dans la passe cassette seulement), `#024` secousse à l'impact.
- **Interdits** : `#044` fondu enchaîné et `#045` volet numériques, `#011` écrasement et étirement cartoon, `#136` trait qui frémit, rayures et flottement de pellicule, dégradé à l'intérieur d'un cellulo (une seule exception : une image peinte « tenue » au sommet émotionnel).
- **Image d'impact** : 2 images d'une silhouette inversée ou monochrome sur lignes radiales, puis le résultat.
- Clignement rapide (un seul dessin fermé, à 10 dessins par seconde), ouverture des yeux en 3 dessins, bouche en 3 ou 4 formes à 10 dessins par seconde qui finit sur une expression tenue.

## 5. Rythme et montage

- Coupes sur les mesures. Plans tenus de 3 à 6 s ; le sommet émotionnel est une image peinte avec un lent panoramique où seuls les cycles bougent.
- Transitions : coupe, flash blanc, image d'impact, parasite de cassette à un moment lié à la bande. Deux accents possibles : **mise sous tension** (point → ligne → image) en ouverture, **bruit de tracking** (quelques images de déchirure) une fois.
- Un temps de vrai silence avant le sommet.
- **Version courte (8 à 12 s)** : deux plans : le trajet ou l'attente (4 à 5 s), puis le gros plan des yeux sur la décision ; couper l'image peinte en panoramique, ramener le temps de silence à 0,5 s, réduire le titre à un mot (ou l'enlever). Accroche avant 3 s : la mise sous tension de l'écran ou un flash blanc.

## 6. Recette technique

- **Moteur** : HyperFrames ; deux canvas 2D hors écran (couleur + **plaque émissive**) composés par une passe WebGL finale (lueur, étalonnage, cassette, tube, sous-titres).
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `cellulo.js` (formes, ombrage automatique, rubans), `palettes.js` (modèles de couleurs), `tete.js` (tête 3 vues × expressions), `decors.js` (plaques couleur + émissive, reflets mouillés), `effets.js` (pluie, lignes de vitesse, reflets), `post.js` (passe finale).
- **Techniques clés** :
  - Ombrage d'un cellulo : remplir, puis découper `forme − forme décalée vers la lumière` (règle pair-impair) avec la couleur d'ombre ; même chose à l'opposé pour la lumière et pour un **liseré néon** de 2 à 4 px.
  - Tamponner la silhouette de chaque cellulo **en noir sur la plaque émissive** : la lueur ne traverse jamais un personnage.
  - Lueur forte depuis la plaque émissive, faible depuis la couleur au-dessus de 0,9 ; la lueur la plus large teintée rouge orangé.
  - Sol mouillé : copie retournée, floutée et striée du décor, assombrie par des bandes d'ondulation.
  - Cassette et tube (valeurs de la démo) : flou de chrominance ≈ 7 px, lignes de période 3 px à force 0,18, lueur de phosphore 0,35. À 1080 px de large, vérifie le moiré sur une réduction à 360 px.
- **Pièges** : cellulos blancs qui virent au rose (lueur depuis l'émissif seulement) ; néon qui traverse les personnages ; liseré trop épais qui avale les formes fines ; visage de face (le dessin le plus dur : cache-le derrière une visière, un pare-brise, un contre-jour) ; police non chargée avant de peindre (le canvas retombe sur une police à empattements) ; détail cathodique qui gonfle le fichier (bruit dans le shader, pas à l'encodage).

## 7. Son

- **Musique** : pop de générique, city pop, funk synthétique : saxophone ou cuivre synthétique, piano électrique FM, basse slappée, guitare en double croches, caisse claire à réverbération coupée, arpège de synthé analogique, nappe de cordes. Harmonie jazz-pop (accords de septième majeure, de neuvième).
- **Idées de mise en scène sonore** : la musique passe en « cassette / radio » quand une source à l'image la joue, puis s'ouvre ; un coup de cuivre sur le titre ; un demi-ton plus haut pour le dernier refrain.
- **Bruitages** : moteur, pluie, pneus sur route mouillée, vent, grésillement radio, clic de cassette, pas sur le trottoir mouillé. Les accents de cassette ont leur propre son (clac, sifflement).
- **Voix** : répliques courtes ; une seconde voix « au téléphone » (bande 380 à 2 800 Hz). Voix ≈ 10 dB au-dessus de la musique baissée. −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : yeux ronds « moe », traits noirs uniformes, dégradés dans les formes, visage en masque de papier, cheveux en tentacules, filtre de couleur global au lieu d'un modèle par lumière.

- [ ] Les quatre couches sont présentes : décor peint, cellulo plat, lumière traversante, lecture cassette.
- [ ] Aucun dégradé dans un cellulo ; ombres et lumières à bord dur.
- [ ] Contours colorés (aucun noir pur sur la peau et les cheveux).
- [ ] La lueur des néons ne passe à travers aucun personnage.
- [ ] La peau garde une couleur naturelle dans chaque modèle de couleurs.
- [ ] Personnages à 15 ou 10 dessins par seconde, caméra et lumière fluides.
- [ ] Aucun défaut de pellicule (rayures, flottement) ; aucun fondu ou volet numérique.
- [ ] Mots d'enseignes génériques, aucune marque ; dérogation bleu-violet déclarée si la palette est nocturne.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 9
- Bleu-violet : dérogation
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Film de démo d'origine *City Lights, 1987* (59 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/cel-anime-80s.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/cel-anime-80s.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/cel-anime-80s/STYLE.md`, `DEMO.md`, `demo/cel.js`, `pal.js`, `head80.js`, `bg.js`, `fx.js`, `post.js`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Polices de la démo : Dela Gothic One, Kanit, Barlow Semi Condensed (SIL OFL 1.1).
- Adaptation Flot Web : traduction, section 9:16, valeurs hex indicatives de palette (la source donne des noms de couleurs et des multiplicateurs), numéros du dictionnaire.
