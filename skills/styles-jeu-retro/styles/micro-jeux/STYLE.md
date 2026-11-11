# Micro-jeux en rafale

## 1. Identité

- **Nom** : Micro-jeux en rafale.
- **Inspiration** : les jeux de fête faits de mini-épreuves de quelques secondes qui s'enchaînent de plus en plus vite. On reprend la grammaire du genre, jamais le nom d'une série, ses personnages, son interface, ses épreuves ou sa musique.
- **Ce que c'est** :
  - **Un micro-jeu = un mot d'ordre crié + 2,5 à 4 s + une action + un résultat** (réussite, ou échec drôle).
  - **Chaque micro-jeu est dessiné dans une matière différente** (craie grasse, lavis d'encre, terminal, risographie, pixel, plan d'architecte, typographie suisse, pâte à modeler, papier découpé…). Le choc de chaque changement est à la fois le gag et le temps fort.
  - **Un décor fixe « maison »** tient le film : un plateau avec un animateur, un compteur de vies et un numéro de manche, où l'on revient entre les jeux.
  - **Ça accélère** : tous les quelques jeux, tempo, durée des jeux, temps sur le plateau, tenue du mot d'ordre et cadence d'animation montent ensemble.
  - **Le héros survit à toutes les matières** grâce à deux ou trois marques de silhouette.
- **Marche pour** : les étapes d'un métier ou d'une recette, une journée heure par heure, les fonctions d'une appli, une liste de conseils, une semaine avant une échéance.
- **Ne marche pas pour** : film long (dès que la rafale ne monte plus, on arrête), sujet grave, message unique à développer, client qui veut une seule identité visuelle. Ce n'est ni un jeu télé à manches (un seul style), ni un échantillonneur de styles (chaque jeu a un enjeu, les vies les relient).

## 2. Palette, typographie, matières

- **Plateau maison** : dessin plat, contour presque noir `#1A1030` de 7 px, aplats, **une ombre à bord dur** (remplir la forme en couleur d'ombre, la découper, la remplir de nouveau décalée de 9 px en haut à gauche).

| Rôle (plateau) | Hex |
|---|---|
| Fond et soleil tournant | violet `#2A0F5C` · `#3D168F` |
| Accents | magenta `#FF2E88` · or `#FFC928` (foncé `#E08A00`) · cyan `#1FD1D1` |
| Réussite / échec (tampons et vies seulement) | `#3BDC5A` · `#FF3B3B` |

  Ce fond violet relève de l'interdit bleu-violet s'il occupe trop d'images : préfère une des autres gammes (fond sarcelle avec corail et citron ; scène noire avec orange vif et bleu électrique), ou garde le plateau à l'écran moins de 30 % du temps.
- **Chaque matière apporte sa palette** (couleurs de cire, encre + vermillon, phosphore ambre, trois encres riso, palette pixel limitée, blanc sur bleu, noir-blanc-rouge). Ne teinte jamais une matière avec la palette du plateau.
- **Un accent suit le héros** d'une matière à l'autre quand c'est possible (un point vermillon dans l'encre, un caractère inversé dans un terminal, un rond rouge en typographie suisse).
- **Typographie** (OFL) : mot d'ordre en **Titan One**, blanc à gros contour encre, ombre colorée, éclat derrière, incliné de quelques degrés ; cartons en **Lilita One** ≈ 50 px. Dans un jeu, tout texte utilise **la typographie de la matière**.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Archivo Black à la place de Titan One et de Lilita One. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/titan-one`, `@fontsource/lilita-one` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Chaque matière repose sur une astuce de canal** qui la rend lisible d'un coup d'œil : pression contre le grain du papier (craie), encre humide et sèche (lavis), densité par plaque avec surimpression et repérage faux (riso), image basse résolution agrandie (pixel, terminal), systèmes de traits (plan, suisse). Compte 100 à 200 lignes de code par matière.

## 3. Composition 9:16

- **L'écran dans l'écran** (téléviseur, borne, téléphone, fenêtre) est le lieu des jeux. En vertical, prends un **cadre portrait** (un téléphone géant, une borne d'arcade) de 840×1120 px, posé x 60 à 900, y 300 à 1420, sur le plateau.
- Pendant un jeu, le cadre s'agrandit jusqu'à remplir l'image ; au retour, il rétrécit avec un tampon ✓ ou ✗.
- **Compteur de vies** en haut à gauche (y 180 à 260), **numéro de manche** en haut à droite mais à gauche de x = 945. **Mèche du chrono** horizontale sous le jeu (y ≈ 1470), un nœud par temps.
- **Mot d'ordre** : 150 à 200 px, centré vers y 800, claque en ≈ 3 images, tient, puis **rétrécit en étiquette dans un coin avant la première action** : le résultat n'est jamais couvert.
- L'animateur se tient en bas à gauche du plateau (y 1150 à 1500).
- 16:9 : écran de jeu ≈ 40 % de la largeur, au centre du plateau.

## 4. Ce qui bouge

- **Action principale** : une action par jeu, puis son résultat. **L'échec se joue** : l'action dépasse, s'écrase, cogne ou roule hors champ ; la physique de la matière fait le gag.
- **Boucle de fond 1** : l'animateur bat **chaque temps** (une aiguille, un pied, un hochement). L'arrêter net est l'outil émotionnel le plus fort.
- **Boucle de fond 2** : soleil qui tourne derrière le plateau, étincelle du chrono qui passe chaque nœud pile sur le temps.
- **Autorisés** : `#010` dépassement (mot d'ordre), `#020` zoom à travers l'écran (entrée ≈ 0,25 s, sortie ≈ 0,33 s), `#144` écran partagé (deux matières côte à côte), `#040` arrêt sur image et `#037` ralenti (replay d'un échec), `#038` rampe de vitesse, `#184` très gros plan sur le bouton de départ, `#021` retournement de tuiles, `#046` coupe sèche, `#164` compte à rebours.
- **Interdits** : `#044` fondu enchaîné, `#187` fondu au noir, image vide entre deux jeux, flash blanc à 100 % (plafonne à ≈ 60 %, sinon il se lit comme une image vide), étiquettes de mot d'ordre qui s'empilent.
- La cadence fait partie de l'échelle : personnages saccadés au début, plus fluides ensuite, à pleine cadence au sommet. Caméra, transitions et étincelle du chrono toujours fluides.

## 5. Rythme et montage

- **Cinq choses accélèrent ensemble** à chaque palier : tempo, durée du jeu, temps sur le plateau, tenue du mot d'ordre, cadence des personnages.
- Format court : 20 à 45 s, 5 à 9 jeux, 2 paliers d'accélération. Exemple à 30 i/s : 120 BPM (4 s par jeu) → 150 BPM (3,2 s) → 180 BPM (10 images par temps ; 2,7 s).
- **Les vies racontent** : 3 → 2 → 1 (qui clignote) monte la tension sans narration.
- **L'échec devient la solution** : la matière d'un échec revient dans le dernier jeu comme réponse. **Le dernier jeu mélange les règles** des précédents.
- **Au moins un vrai silence** avant le plus gros coup ; le moment le plus fort vient juste après le plus long silence.
- Replay pour un échec qu'il faut comprendre : arrêt, demi-vitesse, avancée, bandes noires, légende dans la typographie de la matière.
- **Version courte (8 à 12 s)** : trois jeux à 150 BPM (3,2 s chacun) : mot d'ordre, action, résultat ; couper les paliers d'accélération et l'intermède de score.

## 6. Recette technique

- **Moteur** : HyperFrames ; canvas 2D pour le plateau, un tampon hors écran par jeu, et des shaders WebGL2 pour transformer les canaux en matière (riso, craie, tube cathodique, encre, papier de plan).
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `timeline.js` (grille de tempo et segments, **source unique**), `plateau.js` + `affichage.js` (plateau, chrono, mot d'ordre, tampons, vies, cartons), `persos.js` (animateur, héros), `matieres.js` (shaders), un `jeu_<matiere>.js` par matière (`scene(g, tLocal)` + la traduction du héros), `film.js` (transitions à travers l'écran).
- **Techniques clés** :
  ```js
  // un jeu = une fonction pure de son temps local, dessinée dans SON canvas
  function jeuCraie(g, tl) { /* ... */ }
  definirContexte(tampon.getContext("2d"));   // puis le restaurer :
  // les aides de dessin à contexte global dessinent sinon sur le mauvais canvas
  ```
  - **Feuille de modèle du héros dans chaque matière** avant d'animer : il est redessiné de zéro à chaque fois, mais les mêmes marques survivent (une forme de casque, un point de couleur, un numéro).
  - Une image mêlant plusieurs matières garde **une seule chaîne de regard** (A mène à B mène à C).
  - Mot d'ordre dans les sous-titres exportés seulement, jamais incrusté deux fois.
- **Pièges** : personnage en caractères de terminal fait d'une rampe de luminosité = bouillie (dessine-le à la main) ; formes à l'encre lues comme de la fumée (dessine la silhouette) ; échec illisible à haut tempo (fais dépasser l'action, ou replay) ; matières « à couverture » qui laissent voir le fond par les trous (pose une base pleine) ; voix de synthèse qui allonge un mot seul (génère deux mots, coupe après le premier).

## 7. Son

- **Musique d'abord** : grille de tempo et table d'évènements avant toute animation.
- **Un groove constant + un instrument de couleur par matière** : piano jouet pour la craie, flûte ou cithare pour l'encre, bips carrés pour le terminal, vibraphone pour l'impression, arpèges pulsés pour le pixel, machine à écrire pour le plan, claves pour le suisse, kalimba pour la pâte à modeler.
- **Bruitages selon la matière** (≈ 5 par 10 s, vrais enregistrements quand ils existent) : cire qui couine, éclaboussure, relais de téléscripteur, papier froissé, cliquets, tampons. Plateau : clic de ressort, verre fêlé pour une vie perdue, cartes retournées.
- **Accélération** : montée de cuivres avant chaque palier, tonalité qui monte d'un ton par manche, groove réduit à un battement de cœur sur la dernière vie.
- **Voix** : un animateur qui crie chaque ordre **un cheveu après** le coup de cuivres ; un héros qui dit très peu. Musique baissée d'environ 11 dB sous la voix. −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : matières teintées par la palette du plateau, héros méconnaissable d'un jeu à l'autre, pas d'accélération, mot d'ordre qui cache le résultat, film qui continue après le sommet.

- [ ] Chaque jeu : un mot d'ordre, 2,5 à 4 s (moins après accélération), une action, un résultat visible.
- [ ] Deux jeux voisins ne partagent jamais la même matière.
- [ ] Les marques de silhouette du héros se retrouvent dans chaque matière.
- [ ] Le compteur de vies change au moins deux fois.
- [ ] Au moins un palier où tempo, durée et cadence montent ensemble.
- [ ] Le chrono est visible et son étincelle tombe sur les temps.
- [ ] Aucune image vide ni fondu entre un jeu et le plateau.
- [ ] Un silence avant le coup le plus fort ; le film s'arrête dès que la rafale ne monte plus.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 9
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Film de démo d'origine *Five-Second Astronaut* (60 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/microgame.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/microgame.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/microgame/STYLE.md`, `DEMO.md`, `demo/timeline.js`, `toon.js`, `stage.js`, `hud.js`, `chars.js`, `glpass.js`, `g_*.js`, `film.js`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Polices : Titan One, Lilita One (SIL OFL 1.1).
- Adaptation Flot Web : traduction, cadre portrait et positions 9:16, exemple de paliers à 30 i/s, mise en garde bleu-violet, numéros du dictionnaire.
