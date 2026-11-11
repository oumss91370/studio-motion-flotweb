# Dictionnaire des 192 mouvements

Langue commune entre le client, l'agent et les fiches de style : chaque mouvement a un **numéro fixe** (#001 à #192). Le découpage cite les numéros, les fiches de style autorisent ou interdisent des numéros, le compte rendu final les reprend.

## Origine et licence

- Source : **Motion Prompt**, de Shohei Ohtaki — dépôt `showheyohtaki/motion-prompt`, commit `7819d38`, catalogue version `1.6950972783` (192 éléments, 8 packs de 24). Licence MIT.
- **Copie locale figée** : tout est dans `references/motion-prompt/` (aucun appel au site de l'auteur n'est nécessaire, et il ne faut pas en dépendre : l'auteur peut modifier ou retirer des éléments).
  - `motion-prompt/e/NNN.txt` : un mouvement = sa fiche chiffrée (en anglais) + son code de référence (Canvas 2D, fonction pure du temps).
  - `motion-prompt/kit/<pack>.js` : constantes, palette et fonctions d'aide du pack (courbes, texte, formes).
  - `motion-prompt/catalog.tsv` : index d'origine (une ligne par mouvement).
  - `motion-prompt/LICENSE` et `THIRD-PARTY-NOTICES.md` : licence et notices d'origine.
- **Ligne de licence obligatoire.** Chaque fichier d'élément et chaque kit commence par une ligne de ce type :

  ```
  // Motion Prompt #012 · MIT License (c) 2026 Shohei Ohtaki · https://showheyohtaki.github.io/motion-prompt/#012
  ```

  Dès que tu reprends le code ou les valeurs d'un mouvement dans un fichier du projet du client, **recopie cette ligne (avec le bon numéro) en commentaire au-dessus du code concerné**. C'est l'attribution demandée par l'auteur. Ne la supprime jamais des fichiers de `motion-prompt/`.
- Les noms français, les colonnes « quand l'utiliser » et les équivalents GSAP sont une adaptation Flot Web ; les nombres viennent des fiches d'origine.

## Comment lire les tableaux

- **Durée et courbe typiques** : valeurs de la démonstration d'origine, à garder comme proportions. Les courbes sont notées en vocabulaire GSAP :

  | Fiche d'origine | Équivalent GSAP |
  |---|---|
  | quadratic ease-in-out | `power1.inOut` |
  | cubic ease-in-out, `cubic-bezier(0.65,0,0.35,1)` | `power2.inOut` |
  | cubic ease-out / ease-in | `power2.out` / `power2.in` |
  | quartic, quintic ease-out | `power3.out`, `power4.out` |
  | backOut (s = x) | `back.out(x)` |
  | ressort `1 − e^(−at)·cos(bt)` | ressort amorti : `elastic.out(1, 0.5)` approché, ou la formule exacte dans un `onUpdate` piloté par le temps |
  | vitesse constante | `none` (réservé aux cas listés dans `principes.md`) |

- **Code** : chemin relatif à `references/`. Lis toujours la fiche `e/NNN.txt` avant de porter un mouvement : elle donne l'ordre des phases et tous les nombres.
- **Les démonstrations sont au format carte horizontale** (environ 540 × 200 px). En vertical 1080 × 1920, tu ne recopies pas la mise en page : tu reprends le **timing, la courbe, l'amplitude relative** et tu recomposes pour le 9:16 (voir `principes.md`, section 9:16).

## Règles de portage (à respecter à chaque fois)

1. **Ne jamais inventer un mouvement à partir de son nom.** Ouvre la fiche, reprends ses nombres.
2. **Durées, délais, courbes, dépassements, angles et rapports d'échelle restent ceux de la fiche.** Seuls changent : le texte, les couleurs, les images, la matière (c'est la fiche de style qui décide de la matière).
3. **Pour faire tenir un mouvement dans un plan** : allonge ou raccourcis le **maintien**, jamais l'entrée ni la sortie. Si le plan est plus court que entrée + sortie, mets tout à l'échelle de façon uniforme et signale-le dans le compte rendu.
4. **Boucle ou lecture unique** : une boucle rejoue le cycle ; un titre qui entre et reste s'arrête pendant le maintien, il ne repart pas dans la sortie.
5. **Plusieurs mouvements dans un plan** : chacun sur son temps, un seul mouvement plein cadre à la fois, un maintien après chaque mouvement, une seule famille de courbes par vidéo.
6. **Le choix du client est intangible** : si le client a choisi un numéro, tu ne le remplaces pas en silence. S'il ne convient pas (interdit par la fiche de style, illisible en vertical), tu le dis et tu proposes un numéro voisin.
7. **Deux kits ne se mélangent pas** dans un même fichier (ils déclarent les mêmes noms). En HyperFrames, on porte en général les nombres vers GSAP ; si tu exécutes le code Canvas d'origine, un module par pack.
8. **Styles « en 2 »** (dessin saccadé, pixel art, pâte à modeler) : on ne change pas les durées, on change seulement l'échantillonnage (`steps()`), voir #128. À 30 i/s : 15 poses par seconde là où la source dit 12, 10 là où elle dit 8 (règle complète dans le `SKILL.md` de `principes-mouvement`, « Cadence saccadée à 30 i/s »).
9. **Reculs** : le dictionnaire n'a pas d'entrée « recul ». Quand une fiche de style écrit « #027 recul » ou « #028 recul » (ou « zoom arrière »), c'est le même geste joué à l'envers : #027 pour un travelling arrière (la parallaxe change), #028 pour un zoom arrière (toute l'image rétrécit du même rapport). Mêmes durées, même courbe.

## Vue d'ensemble des packs

| Pack | Numéros | Sujet | Usage dans une vidéo verticale |
|---|---|---|---|
| `motion` | 001–024 | Mouvements de motion design | **Cœur du métier** : entrées, finitions, transitions |
| `camera` | 025–048 | Caméra et raccords | Mouvements de cadre et montage (voir aussi `camera.md`) |
| `ui` | 049–072 | Composants d'interface | Démonstrations d'application ou de site reconstruites en code (clics et curseur simulés par la timeline) |
| `lp` | 073–096 | Effets de page web | Idem : le défilement et le survol sont **simulés** par la timeline, jamais réels |
| `photo` | 097–120 | Lumières, optiques, étalonnages | Vocabulaire de look : éclairage Blender, filtres, prompts d'image. Jamais porter le code d'exemple comme visuel final |
| `motion2` | 121–144 | Motion design, suite | Techniques d'animation, texte et formes, transitions |
| `lp2` | 145–168 | Effets de page web, suite | Comme `lp` |
| `camera2` | 169–192 | Caméra, angles, montage | Comme `camera` |

---

## Pack `motion` — mouvements de motion design (001–024)

Cycle de démonstration : 4,7 s. Kit : `motion-prompt/kit/motion.js`.

| # | Nom français (nom d'origine) | Ce qui bouge | Durée et courbe typiques | Quand l'utiliser | Code |
|---|---|---|---|---|---|
| 001 | Apparition en pop (Pop-in) | Une icône passe de l'échelle 0 à 1 avec un rebond et une petite rotation (−20° → 0) ; un badge surgit 0,34 s plus tard | Entrée ≈ 0,4 s, ressort amorti (pic ≈ 1,26) ; sortie 0,26 s `back.in(2.2)` | Faire entrer un petit élément avec un accent léger : icône, bouton, badge | `motion-prompt/e/001.txt` |
| 002 | Entrée en cascade (Stagger) | Des barres montent l'une après l'autre depuis la gauche ; un point surgit au sommet de chacune | 0,5 s par élément, décalage 0,12 s, `back.out(2.6)` | Listes, barres de graphique, cartes : guider l'œil dans l'ordre | `motion-prompt/e/002.txt` |
| 003 | Éclat (Burst) | Un cœur se contracte puis se remplit ; un anneau, des traits et des points jaillissent au même instant | Anticipation 0,2 s (échelle 1 → 0,7, `power1.inOut`), puis ressort amorti | Marquer l'instant précis d'un déclenchement : like, réussite, bonne réponse | `motion-prompt/e/003.txt` |
| 004 | Tracé de ligne (Line draw) | Une courbe se dessine d'un bout à l'autre, puis s'efface par son début | Axes 0,6 s, courbe 1,55 s, `power2.inOut` ; pointe de flèche 0,3 s `back.out(2.5)` | Quand le trait est le sujet : courbe de graphique, itinéraire, soulignement, cercle à main levée | `motion-prompt/e/004.txt` |
| 005 | Révélation par masque (Mask reveal) | Un titre monte de derrière un bord invisible marqué par un filet ; la seconde ligne descend de l'autre côté | Filet 0,4 s `power2.inOut` ; texte 0,65 s `power4.out`, seconde ligne 0,2 s après | Titres et intertitres qui doivent apparaître de façon nette et posée | `motion-prompt/e/005.txt` |
| 006 | Machine à écrire (Typewriter) | Le texte est tapé caractère par caractère dans un champ, le curseur clignote, le bouton d'envoi s'allume et est pressé | 1 caractère toutes les 0,24 s (démonstration lente) ; curseur : période 0,94 s | Montrer quelqu'un qui tape : prompt, recherche, message | `motion-prompt/e/006.txt` |
| 007 | Compteur (Count-up) | Un nombre défile vers le haut puis se verrouille sur sa valeur finale (changement de couleur, petit rebond) | 2,45 s, `power3.out` (rapide puis lent) ; rebond final de 7 % | Faire sentir qu'un chiffre est gros ou en hausse : chiffre d'affaires, abonnés, taux | `motion-prompt/e/007.txt` |
| 008 | Typographie cinétique (Kinetic typography) | Chaque mot bouge selon son sens : l'un s'étire, l'autre rebondit, tourne, s'écrase | 1,175 s par mot ; sortie 0,2 s `power2.in` (montée de 46 px en fondu) | Rendre mémorables les mots clés d'une voix off ou de paroles | `motion-prompt/e/008.txt` |
| 009 | Courbe de vitesse (Easing) | Deux carrés parcourent la même distance dans le même temps : l'un à vitesse constante, l'autre qui accélère puis ralentit | 1,55 s, `cubic-bezier(.86, 0, .14, 1)` | Sur tout déplacement, changement d'échelle ou rotation, pour éviter l'effet mécanique | `motion-prompt/e/009.txt` |
| 010 | Dépassement (Overshoot) | Une aiguille dépasse sa cible d'environ 25 %, revient et se stabilise | Ressort amorti : pic à ≈ 0,3 s, stable en ≈ 1 s | Donner de l'énergie et du ressort à un élément qui arrive | `motion-prompt/e/010.txt` |
| 011 | Écrasement et étirement (Squash & stretch) | Un personnage rond s'écrase à l'atterrissage (0,52 en hauteur) et s'étire au décollage (1,28) | Un rebond en 1,175 s ; le contact occupe 10 % du rebond | Donner du poids et de la souplesse à un personnage ou à un logo | `motion-prompt/e/011.txt` |
| 012 | Morphing de forme (Shape morph) | Une forme passe du cercle au carré, à l'étoile, au cœur, avec sa couleur | Maintien puis 0,58 s de transformation, `back.out(1.6)` | Transformer une icône ou un logo en un autre sans coupe | `motion-prompt/e/012.txt` |
| 013 | Mouvement liquide (Liquid motion) | Une goutte s'étire, se sépare en gouttelettes puis se reforme | Trajet 1,1 s `cubic-bezier(.7, 0, .2, 1)` ; suiveurs décalés de 0,065 s | Look organique et doux : logos, fonds, liaisons | `motion-prompt/e/013.txt` |
| 014 | Traînée (Motion trail) | Une balle qui décrit un huit laisse derrière elle des copies qui s'estompent | Vitesse constante ; 15 copies espacées de ≈ 0,08 s | Montrer la vitesse ou la trajectoire : objet volant, curseur, point lumineux | `motion-prompt/e/014.txt` |
| 015 | Particules (Particles) | Des particules jaillissent d'un émetteur, s'étalent et retombent | Vie ≤ 1,5 s : apparition 0,06 s, disparition sur les 30 % finaux ; aléatoire à graine fixe | Célébration, vivacité (confettis, étincelles) — à doser, voir les règles anti-motion IA | `motion-prompt/e/015.txt` |
| 016 | Parallaxe (Parallax) | Un paysage défile de côté ; les plans proches bougent plus que les lointains | Va-et-vient sinusoïdal ; facteurs du fond vers l'avant : 0,05 / 0,1 / 0,28 / 0,6 / 1 | Donner de la profondeur à une illustration ou une photo plate | `motion-prompt/e/016.txt` |
| 017 | Transition par masque (Mask transition) | Une fenêtre ronde ou en étoile grandit et montre la scène suivante à l'intérieur | 1,15 s `power2.inOut` | Changer de scène à partir d'un objet du cadre : soleil, logo, bouton | `motion-prompt/e/017.txt` |
| 018 | Transition par formes (Shape transition) | Des bandes colorées en biais balaient le cadre, le couvrent, puis découvrent la scène suivante | Couverture 0,62 s, bandes décalées de 14 %, `power2.inOut` ; la scène change quand tout est couvert | Changement de chapitre ou de sujet aux couleurs de la marque | `motion-prompt/e/018.txt` |
| 019 | Transition liquide (Liquid transition) | Un liquide façon peinture coule du haut, remplit le cadre et devient la scène suivante | Deux couches de ≈ 1,1 s décalées de 0,35 s, `power1.inOut` ; bord ondulé | Changement de scène doux et organique : cuisine, beauté, création | `motion-prompt/e/019.txt` |
| 020 | Zoom traversant (Zoom through) | La caméra plonge dans le trou d'une lettre et ressort dans la scène suivante | 1,4 s : accélération `power2.in` (0,95 s) puis ralenti `power2.out` (0,45 s) ; zoom exponentiel | Plonger dans un logo ou une lettre pour passer à la suite avec de l'élan | `motion-prompt/e/020.txt` |
| 021 | Retournement (Flip) | Une carte pivote autour de son axe vertical et montre son autre face | 180° en 1,05 s, `back.out(1.5)` ; +8 % d'échelle pendant le tour | Deux faces d'une même chose : question et réponse, avant et après | `motion-prompt/e/021.txt` |
| 022 | Balayage lumineux (Light sweep) | Une bande de lumière traverse en biais la surface d'un logo, puis une étincelle | Balayage 1,05 s `power1.inOut` ; étincelle 0,6 s | Finition haut de gamme sur un logo, un badge, un bouton | `motion-prompt/e/022.txt` |
| 023 | Glitch (Glitch) | Des tranches de texte se décalent, les couleurs se séparent, de petites barres apparaissent — sans clignotement de luminosité | 5 à 6 paliers de 0,14 s, par à-coups (pas d'interpolation) ; graine fixe | Ambiance numérique, erreur, malaise ; en accent sur un titre ou une coupe | `motion-prompt/e/023.txt` |
| 024 | Secousse d'impact (Impact shake) | Un bloc de titre tombe lourdement et tout le cadre tremble | Chute 0,32 s `power2.in` ; secousse 1,1 s amortie (≈ 15 px, 5 Hz) | Faire atterrir un titre ou un chiffre important avec du poids | `motion-prompt/e/024.txt` |

## Pack `camera` — caméra et raccords (025–048)

Un passage de démonstration : 4,7 s (cycle du pack : 9,4 s). Kit : `motion-prompt/kit/camera.js`. Vocabulaire français détaillé et dosage : `camera.md`.

| # | Nom français (nom d'origine) | Ce qui bouge | Durée et courbe typiques | Quand l'utiliser | Code |
|---|---|---|---|---|---|
| 025 | Panoramique horizontal (Pan) | La caméra reste en place et pivote de gauche à droite ; tous les plans glissent de la même quantité | 2,9 s `power2.inOut` | Révéler un lieu large, déplacer l'attention d'un côté à l'autre | `motion-prompt/e/025.txt` |
| 026 | Panoramique vertical (Tilt) | La caméra reste en place et pivote vers le haut, d'une personne au sommet d'une tour | 2,9 s `power2.inOut` | Montrer la hauteur ou l'échelle d'un bâtiment, d'un personnage | `motion-prompt/e/026.txt` |
| 027 | Travelling avant (Dolly in) | La caméra avance vers le sujet : le premier plan grossit et sort du cadre, le lointain bouge à peine | 2,9 s `power2.inOut` ; sujet ≈ 3,6 fois plus grand | S'approcher d'une personne ou d'un détail en gardant la profondeur | `motion-prompt/e/027.txt` |
| 028 | Zoom avant (Zoom in) | La caméra ne bouge pas, la focale s'allonge : toute l'image grossit du même rapport | 2,9 s, interpolation exponentielle de la focale | Diriger l'attention sur un point ; plus plat et plus « observateur » qu'un travelling | `motion-prompt/e/028.txt` |
| 029 | Travelling d'accompagnement (Tracking shot) | La caméra se déplace de côté à la vitesse du marcheur : il reste au centre, les poteaux proches défilent vite | Vitesse constante (sans courbe) | Suivre un sujet qui marche ou court en gardant la sensation de mouvement | `motion-prompt/e/029.txt` |
| 030 | Travelling circulaire (Orbit, Arc shot) | La caméra tourne autour du sujet (−54° → +54°) ; le décor défile derrière | 3,1 s `power2.inOut` | Montrer un produit ou une personne en volume, souligner un moment clé | `motion-prompt/e/030.txt` |
| 031 | Grue montante (Crane up) | La caméra s'élève en s'inclinant vers le bas jusqu'à surplomber la personne | 2,9 s `power2.inOut` | Quitter un personnage en fin de scène, révéler la taille du lieu | `motion-prompt/e/031.txt` |
| 032 | Travelling compensé (Dolly zoom, « Vertigo ») | La caméra recule pendant que la focale s'allonge : le sujet garde sa taille, seul le fond se resserre | 2,9 s `power2.inOut` ; fond ≈ 2,2 fois plus gros | Prise de conscience, malaise, choc | `motion-prompt/e/032.txt` |
| 033 | Bascule de point (Rack focus) | La caméra ne bouge pas ; le net passe du premier plan à l'arrière-plan (flou 0 ↔ 7 px) | 1,6 s `power2.inOut` | Déplacer l'attention entre l'avant et l'arrière sans couper | `motion-prompt/e/033.txt` |
| 034 | Caméra à l'épaule (Handheld) | Petit tremblement irrégulier de tout le cadre (sommes de sinus sur lacet, tangage, roulis, hauteur) | Continu, bouclé sans couture | Effet documentaire, sensation d'être sur place | `motion-prompt/e/034.txt` |
| 035 | Plan de drone FPV (FPV drone shot) | Vue subjective en vol bas et rapide entre deux rangées d'arbres, en s'inclinant d'un côté à l'autre | Continu ; deux oscillations par 4,7 s | Vitesse et immersion, traverser un lieu d'un seul geste | `motion-prompt/e/035.txt` |
| 036 | Cadre penché (Dutch angle) | La caméra roule sur l'axe de l'objectif et tient l'horizon en diagonale | 1,6 s `power2.inOut`, puis maintien 2 s | Malaise, tension, « quelque chose cloche » | `motion-prompt/e/036.txt` |
| 037 | Ralenti (Slow motion) | Devant une caméra fixe, un saut et des feuilles qui tombent sont étirés dans le temps | Action étalée sur 3,8 s | Laisser étudier une action ou une expression brève, souligner un pic d'émotion | `motion-prompt/e/037.txt` |
| 038 | Rampe de vitesse (Speed ramp) | Dans un même plan, la vitesse de lecture passe de 2,4× à 0,25× | Transition de 0,7 s `power1.inOut` | Ne ralentir que le moment clé, garder une approche rapide | `motion-prompt/e/038.txt` |
| 039 | Accéléré (Time-lapse) | Caméra fixe : 12 heures défilent en quelques secondes (soleil, nuages, ombres) | 3,7 s `power2.inOut` | Montrer un long laps de temps ou une évolution en peu de temps | `motion-prompt/e/039.txt` |
| 040 | Arrêt sur image (Freeze frame) | L'image se fige au sommet d'un saut, puis reprend à la même image | Gel de 1,4 s ; marqueurs en fondu de 0,12 s | Souligner un instant décisif, poser un nom ou une légende | `motion-prompt/e/040.txt` |
| 041 | Coupe sautée (Jump cut) | Même cadre, même fond ; seuls le personnage et l'horloge sautent dans le temps | Coupe franche (0 image) ; plans de 0,94 s | Resserrer les temps morts, accélérer le rythme | `motion-prompt/e/041.txt` |
| 042 | Raccord de forme (Match cut) | Une balle lancée devient, au plan suivant, un soleil à la même place et de la même taille | Coupe franche ; lancer en `power2.out` | Relier deux scènes éloignées par une forme ou un geste commun | `motion-prompt/e/042.txt` |
| 043 | Panoramique filé (Whip pan) | La caméra pivote très vite et la scène suivante est échangée pendant le flou | 0,8 s (0,4 s de sortie + 0,4 s d'entrée), `power1.inOut`, flou de mouvement | Changer de lieu ou de sujet sans perdre l'énergie | `motion-prompt/e/043.txt` |
| 044 | Fondu enchaîné (Cross dissolve) | L'image suivante se superpose et son opacité monte jusqu'à remplacer la première | 1,5 s `power1.inOut` | Passage doux du temps ou du lieu, entrée dans un souvenir | `motion-prompt/e/044.txt` |
| 045 | Volet (Wipe) | Un bord vertical traverse le cadre ; l'image suivante le remplace derrière lui | 1,1 s `power2.inOut` | Changement net de scène ou de sujet, deux côtés d'une comparaison | `motion-prompt/e/045.txt` |
| 046 | Coupe choc (Smash cut) | Une scène calme coupe sans prévenir sur une scène intense (cadre serré ×2,6, penché de −7°) | Coupe franche ; le contraste fait le travail | Comédie ou choc : écart entre calme et chaos, attente et réalité | `motion-prompt/e/046.txt` |
| 047 | Montage en J (J-cut) | Le son de la scène suivante démarre avant que l'image ne change | Son ≈ 0,7 s avant la coupe image | Créer l'attente, rendre naturel un changement de scène ou d'interlocuteur | `motion-prompt/e/047.txt` |
| 048 | Montage en L (L-cut) | Le son de la scène précédente continue après le changement d'image | Son ≈ 0,7 s après la coupe image | Garder la voix pendant qu'on montre une réaction ou une illustration | `motion-prompt/e/048.txt` |

## Pack `ui` — composants d'interface (049–072)

Cycle : 4,5 s. Kit : `motion-prompt/kit/ui.js`. En vidéo, ces mouvements servent à **rejouer une interface** (démonstration d'application, tutoriel, lancement de produit) : le clic et le curseur sont des tweens placés sur la timeline.

| # | Nom français (nom d'origine) | Ce qui bouge | Durée et courbe typiques | Quand l'utiliser | Code |
|---|---|---|---|---|---|
| 049 | Fenêtre modale (Modal dialog) | La page s'assombrit (voile à 0,42) et une petite fenêtre grandit légèrement au centre | Ouverture 0,32 s `power2.out` ; fermeture 0,28 s `power2.inOut` | L'utilisateur doit s'arrêter sur une chose : confirmation, court formulaire | `motion-prompt/e/049.txt` |
| 050 | Tiroir latéral (Drawer, Off-canvas) | Un panneau haut glisse depuis la gauche ; un clic à côté le renvoie | 0,38 s `power2.out` ; fermeture 0,35 s `power2.inOut` | Navigation ou filtres cachés jusqu'au besoin, surtout sur mobile | `motion-prompt/e/050.txt` |
| 051 | Feuille du bas (Bottom sheet) | Un panneau monte du bas ; on le referme en tirant sa poignée vers le bas | 0,4 s `power2.out` ; fermeture 0,6 s (suit le doigt) | Détails ou choix sur mobile en gardant l'écran en vue | `motion-prompt/e/051.txt` |
| 052 | Accordéon (Accordion) | Un titre cliqué déplie son contenu et pousse les lignes suivantes vers le bas | 0,35 s `power2.inOut` | FAQ, longs détails qu'on ouvre à la demande | `motion-prompt/e/052.txt` |
| 053 | Liste déroulante (Dropdown) | Un champ cliqué déroule quatre options ; le chevron tourne de 180° | 0,25 s `power2.out`, descente de 6 px en fondu | Choisir une valeur dans une liste fixe | `motion-prompt/e/053.txt` |
| 054 | Infobulle (Tooltip) | Au survol d'un « ? », une courte note apparaît dans une bulle sombre | 0,2 s `power2.out`, montée de 6 px | Ajouter un indice d'une ligne sans prendre de place | `motion-prompt/e/054.txt` |
| 055 | Bulle contextuelle (Popover) | Un petit panneau s'ouvre à côté du bouton, avec une pointe vers lui | 0,28 s `power2.out` ; fermeture 0,2 s | Réglage ou confirmation courte, juste à côté du bouton | `motion-prompt/e/055.txt` |
| 056 | Notification éphémère (Toast) | Un message sombre glisse dans le coin, une barre de temps se vide, il repart | Entrée 0,35 s `power2.out` (240 px) ; barre linéaire 1,8 s | Confirmer une sauvegarde ou un envoi sans interrompre | `motion-prompt/e/056.txt` |
| 057 | Onglets (Tabs) | Le soulignement glisse d'un onglet à l'autre et le contenu change | 0,25 s `power2.inOut` | Plusieurs vues liées dans le même espace | `motion-prompt/e/057.txt` |
| 058 | Carrousel (Carousel) | La rangée d'images glisse d'un cran à chaque clic ; le point indicateur suit | 0,4 s `power2.inOut` | Montrer plusieurs images une par une dans peu de place | `motion-prompt/e/058.txt` |
| 059 | Interrupteur (Toggle switch) | Le bouton glisse de 30 px et la piste change de couleur | 0,2 s `power2.out` | Réglage à deux états, à effet immédiat | `motion-prompt/e/059.txt` |
| 060 | Contrôle segmenté (Segmented control) | Une surbrillance glisse entre Jour / Semaine / Mois et le graphique dessous change | 0,25 s `power2.inOut` | Basculer entre 2 à 4 vues d'un même contenu | `motion-prompt/e/060.txt` |
| 061 | Puces de filtre (Filter chips) | La puce cliquée s'élargit, prend une coche et une couleur ; les cartes non concernées s'estompent | 0,15 s `power2.out` | Affiner une liste en combinant quelques filtres | `motion-prompt/e/061.txt` |
| 062 | Curseur de plage (Range slider) | Deux poignées se rapprochent sur une piste pour resserrer une fourchette | 0,35 à 0,6 s `power2.inOut` | Filtrer par prix, date, taille | `motion-prompt/e/062.txt` |
| 063 | Compteur plus / moins (Stepper) | Chaque appui change le nombre de 1, avec un petit pop | Un appui toutes les 0,45 s ; segment teinté 0,2 s | Petites quantités : articles, invités | `motion-prompt/e/063.txt` |
| 064 | Pagination (Pagination) | La pastille de page courante se déplace et la liste change | 0,2 s `power2.inOut` par page | Découper une longue liste en pages numérotées | `motion-prompt/e/064.txt` |
| 065 | Menu hamburger (Hamburger menu) | Les trois traits deviennent une croix et le menu descend sous l'en-tête | 0,3 s `power2.inOut` | Ranger la navigation derrière un bouton sur écran étroit | `motion-prompt/e/065.txt` |
| 066 | Fil d'Ariane (Breadcrumbs) | Un clic sur un niveau remonte dans l'arborescence ; le dernier maillon s'efface | 0,25 s `power2.inOut` | Sites à hiérarchie profonde : situer la page et remonter | `motion-prompt/e/066.txt` |
| 067 | Méga-menu (Mega menu) | Au survol, un large panneau à trois colonnes de liens et une image descend | 0,25 s `power2.out` | Sites à nombreuses rubriques : tout voir d'un coup | `motion-prompt/e/067.txt` |
| 068 | Indicateur d'étapes (Step indicator) | À chaque « Suivant », le cercle devient une coche et la ligne s'allonge jusqu'à l'étape suivante | 0,3 s `power2.inOut` par étape | Parcours en étapes : inscription, paiement | `motion-prompt/e/068.txt` |
| 069 | Écran squelette (Skeleton screen) | Le contenu devient des blocs gris de même forme, balayés par un reflet | Bascule 0,15 s linéaire ; un reflet toutes les 0,9 s | Chargement d'une liste ou de cartes en gardant la mise en page visible | `motion-prompt/e/069.txt` |
| 070 | Indicateur d'attente (Spinner) | Un arc tourne au centre, puis se change en coche qui s'efface | Voile 0,15 s linéaire ; coche 0,25 s `power2.out` (0,7 → 1) | Attente courte de durée inconnue : envoi, sauvegarde | `motion-prompt/e/070.txt` |
| 071 | Pastille de compteur (Badge) | La pastille de la cloche compte 1, 2, 3 ; chaque arrivée fait un pop et une onde | Pop 1,3 → 1 en 0,3 s ; onde 0,5 s | Attirer l'attention sur un nombre : non lus, panier | `motion-prompt/e/071.txt` |
| 072 | État vide (Empty state) | Les lignes supprimées glissent et s'effacent ; un dessin « rien ici » et un bouton apparaissent | Suppression 0,3 s `power2.inOut` ; apparition 0,35 s, montée de 8 px | Premier usage ou absence de résultat : dire quoi faire ensuite | `motion-prompt/e/072.txt` |

## Pack `lp` — effets de page web (073–096)

Cycle : 4,8 s. Kit : `motion-prompt/kit/lp.js`. Le défilement de page est **simulé** : c'est un tween (en général 0,6 à 1,6 s, `power2.inOut`) sur la position de la page.

| # | Nom français (nom d'origine) | Ce qui bouge | Durée et courbe typiques | Quand l'utiliser | Code |
|---|---|---|---|---|---|
| 073 | Défilement en parallaxe (Parallax scrolling) | Le titre monte normalement ; le ciel, les collines lointaines et proches montent plus lentement | Défilement simulé 1,6 s `power2.inOut` | Donner de la profondeur à un visuel d'ouverture | `motion-prompt/e/073.txt` |
| 074 | Apparition au défilement (Fade-in on scroll) | Titre, cartes et texte montent en place et apparaissent quand ils entrent dans la vue | 0,7 s `power2.out`, montée de 28 px | Dévoiler le contenu morceau par morceau | `motion-prompt/e/074.txt` |
| 075 | En-tête collant (Sticky header) | Le bandeau d'annonce part, l'en-tête se fixe en haut et le contenu passe dessous | Défilement 0,9 s `power2.inOut` | Garder le menu et le bouton d'action à portée | `motion-prompt/e/075.txt` |
| 076 | Section épinglée (Pinning) | Une section se fige plein écran ; le défilement fait avancer son contenu 1 → 2 → 3, puis elle repart | Changement d'étape en `power2.inOut` ; le chiffre roule de 52 px | Dérouler des étapes, des fonctions ou un avant/après dans un seul écran | `motion-prompt/e/076.txt` |
| 077 | Défilement horizontal (Horizontal scroll) | La section reste fixe et quatre cartes numérotées partent vers la gauche | Déplacement proportionnel au défilement (sans courbe propre) | Réalisations, études de cas, produits en rangée | `motion-prompt/e/077.txt` |
| 078 | Défilement aimanté (Scroll snap) | Après un petit geste, la page finit seule le trajet jusqu'au haut de la section suivante | Geste 0,4 s puis aimantation 0,6 s, `power2.out` | Page qui se lit un écran à la fois, comme des diapositives | `motion-prompt/e/078.txt` |
| 079 | Barre de progression de lecture (Scroll progress bar) | Un trait en haut grandit depuis la gauche à mesure qu'on lit | Paliers de 0,45 s séparés de 0,4 s de pause | Longs articles : montrer ce qu'il reste | `motion-prompt/e/079.txt` |
| 080 | Surlignage animé (Highlighter animation) | Un trait de surligneur jaune se trace de gauche à droite sous les mots clés | 0,8 s | Faire ressortir la seule phrase qui compte | `motion-prompt/e/080.txt` |
| 081 | Soulèvement au survol (Hover lift) | La carte survolée monte de 10 px et son ombre s'élargit | 0,3 s `power2.out`, retour 0,3 s | Montrer qu'une carte ou un bouton est cliquable | `motion-prompt/e/081.txt` |
| 082 | Zoom d'image au survol (Image zoom on hover) | La photo grossit (1 → 1,15) dans un cadre qui ne change pas | 0,5 s `power2.out` | Grilles de photos : montrer l'élément sur le point d'être choisi | `motion-prompt/e/082.txt` |
| 083 | Suiveur de curseur (Cursor follower) | Un cercle suit le pointeur avec un léger retard | Couvre 12 % de la distance restante à chaque image (lissage exponentiel) | Touche ludique sur un site de marque ou un portfolio | `motion-prompt/e/083.txt` |
| 084 | Bouton magnétique (Magnetic button) | Le bouton est attiré vers le curseur proche (35 % de l'écart), puis revient en oscillant | Retour 1,1 s `elastic.out(1, 0.3)` | Sur le bouton qu'on veut le plus voir cliqué | `motion-prompt/e/084.txt` |
| 085 | Onde de clic (Ripple effect) | Un cercle blanc part du point cliqué, remplit le bouton, puis s'efface | Expansion 0,6 s `power2.out` ; fondu entre 0,3 et 0,8 s | Confirmer un appui à l'endroit où il a eu lieu | `motion-prompt/e/085.txt` |
| 086 | Soulignement animé (Underline animation) | Le trait sous le lien grandit depuis la gauche et repart par la droite | 0,3 s `power2.out` | Liens de menu : montrer discrètement où est le pointeur | `motion-prompt/e/086.txt` |
| 087 | Curseur avant / après (Before/after slider) | Un séparateur glissé de gauche à droite change la part visible de l'« avant » et de l'« après » | Allers de 0,8 à 1,1 s `power2.inOut` | Vendre une transformation : rénovation, beauté, retouche | `motion-prompt/e/087.txt` |
| 088 | Fenêtre d'intention de sortie (Exit-intent popup) | Quand le curseur sort par le haut de la page, elle s'assombrit et une fenêtre « Attendez ! » s'ouvre | 0,4 s `power2.out`, échelle 0,9 → 1 | Dernière offre à un visiteur qui s'en va | `motion-prompt/e/088.txt` |
| 089 | Écran de préchargement (Preloader) | Un compteur va de 0 à 100 % sous le logo, puis l'écran se lève et la page apparaît | Compteur 1,85 s `power2.out` ; levée 0,55 s `power2.inOut` | Transformer une attente en moment de marque | `motion-prompt/e/089.txt` |
| 090 | Chargement différé (Lazy loading) | Les emplacements gris qui entrent dans la vue montrent un indicateur puis l'image en fondu | Indicateur 0,45 s ; colonnes décalées de 0,12 s | Pages riches en images | `motion-prompt/e/090.txt` |
| 091 | Défilement infini (Infinite scroll) | En bas de liste, un indicateur tourne puis trois éléments s'ajoutent | 0,35 s `power2.out`, montée de 10 px | Fils d'actualité qu'on lit sans changer de page | `motion-prompt/e/091.txt` |
| 092 | Transition de page (Page transition) | Un panneau coloré entre par la gauche, couvre tout, la page change, il sort par la droite | 0,4 s + 0,45 s, `power2.inOut` | Relier deux pages d'un site de marque | `motion-prompt/e/092.txt` |
| 093 | Défilement fluide (Smooth scroll) | Un clic dans le menu fait glisser la page jusqu'à la section | 1,05 s `power2.inOut` | Menu interne ou sommaire : montrer où l'on va | `motion-prompt/e/093.txt` |
| 094 | Bandeau défilant (Marquee) | De grands mots ou des logos défilent sans fin vers la gauche | Vitesse constante (une largeur de série par cycle) | Noms de services, logos de clients, slogan | `motion-prompt/e/094.txt` |
| 095 | Dégradé animé (Animated gradient) | Des taches de couleur douces dérivent en ellipses et se mélangent | Un tour par cycle, vitesse constante | Fond vivant sans photo | `motion-prompt/e/095.txt` |
| 096 | Flottement (Floating animation) | Un téléphone, un badge et une puce montent et descendent doucement, en décalé | ±8 px ; périodes 2,4 s et 1,6 s ; sinus | Mouvement discret sur une image de produit ou une maquette | `motion-prompt/e/096.txt` |

## Pack `photo` — lumières, optiques et étalonnages (097–120)

Cycle : 5 s. Kit : `motion-prompt/kit/photo.js`. Dans toutes les démonstrations, **l'effet s'installe en 1 s, tient 2,6 s et repart en 0,8 s, en `power2.inOut`** : la colonne « durée et courbe » donne donc le réglage clé de l'effet. Ce pack est un **vocabulaire de look** : sers-t'en pour éclairer une scène Blender, régler un filtre ou un étalonnage, ou rédiger un prompt d'image. Ne porte pas le dessin d'exemple comme visuel final.

| # | Nom français (nom d'origine) | Ce qui bouge | Durée et courbe typiques | Quand l'utiliser | Code |
|---|---|---|---|---|---|
| 097 | Contre-jour (Backlighting) | Le soleil vient se placer derrière la tête : fin liseré clair, voile chaud, face côté caméra assombrie | Installation 1 s `power2.inOut` | Portraits aériens, image baignée de lumière | `motion-prompt/e/097.txt` |
| 098 | Lumière de contour (Rim light) | Le décor s'assombrit ; deux sources arrière dessinent un liseré sur les deux côtés de la tête et des épaules | Installation 1 s `power2.inOut` | Détacher une personne ou un produit d'un fond sombre | `motion-prompt/e/098.txt` |
| 099 | Silhouette (Silhouette) | L'exposition se cale sur le ciel : personnage, immeubles et arbre deviennent des aplats noirs | Installation 1 s `power2.inOut` | Quand la forme et la pose portent l'image (coucher de soleil, fenêtre) | `motion-prompt/e/099.txt` |
| 100 | Éclairage latéral (Split lighting) | La lumière passe de 20° à 90° sur le côté : l'ombre coupe le visage en deux | Angle 20° → 90° en 1 s | Portrait dramatique, tendu | `motion-prompt/e/100.txt` |
| 101 | Éclairage Rembrandt (Rembrandt lighting) | Lumière à 45° de côté et 45° en hauteur : un petit triangle clair reste sur la joue à l'ombre | Installation 1 s `power2.inOut` | Portrait sculpté, pictural, classique | `motion-prompt/e/101.txt` |
| 102 | Éclairage papillon (Butterfly lighting) | Lumière de face et en hauteur : visage éclairé des deux côtés, petite ombre symétrique dessous | Installation 1 s `power2.inOut` | Beauté et mode : lumière flatteuse | `motion-prompt/e/102.txt` |
| 103 | Heure dorée (Golden hour) | Le soleil descend au ras de l'horizon : tout vire à l'orange, les ombres s'allongent | Installation 1 s `power2.inOut` | Chaleur, nostalgie, douceur | `motion-prompt/e/103.txt` |
| 104 | Heure bleue (Blue hour) | Soleil couché : ciel en deux bandes de bleu profond, fenêtres et lampadaire ambre | Installation 1 s `power2.inOut` | Ville et nuit avec ciel bleu et lumières chaudes | `motion-prompt/e/104.txt` |
| 105 | Bokeh (Bokeh) | Le sujet reste net ; le fond devient flou (0 → 6 px) et les lumières lointaines s'étalent en disques pâles | Flou 0 → 6 px en 1 s | Détacher le sujet, ambiance de soirée | `motion-prompt/e/105.txt` |
| 106 | Effet maquette (Tilt-shift) | Les bandes du haut et du bas deviennent floues ; seule la bande centrale reste nette | Installation 1 s `power2.inOut` | Faire ressembler une ville ou un événement à une maquette | `motion-prompt/e/106.txt` |
| 107 | Pose longue (Long exposure) | La voiture s'efface (opacité 100 → 10 %) et ses feux deviennent des traits continus | Installation 1 s `power2.inOut` | Flux de circulation, eau ou nuages soyeux en une image | `motion-prompt/e/107.txt` |
| 108 | Filé (Panning shot) | La caméra suit la voiture : elle reste nette au centre, le fond se strie sur 46 px | Étirement du fond 0 → 46 px | Montrer la vitesse d'une voiture, d'un vélo, d'un coureur | `motion-prompt/e/108.txt` |
| 109 | Reflet d'objectif (Lens flare) | Le soleil sort de derrière un immeuble : rayons, points, hexagones et anneau en ligne à travers le cadre | Installation 1 s `power2.inOut` | Éblouissement, soleil d'été, lumière « cinéma » | `motion-prompt/e/109.txt` |
| 110 | Objectif fisheye (Fisheye lens) | Le centre de l'image se bombe, les lignes droites se courbent | Installation 1 s `power2.inOut` | Vue audacieuse ou ludique (skate, clip) | `motion-prompt/e/110.txt` |
| 111 | Aberration chromatique (Chromatic aberration) | L'image est séparée en rouge, vert, bleu recollés à des tailles légèrement différentes : franges sur les bords | Écart d'échelle des canaux 0 → 2 % | Imperfection d'un vieil objectif, VHS, glitch — sur un impact seulement | `motion-prompt/e/111.txt` |
| 112 | Vignettage (Vignette) | Le cadre s'assombrit en douceur depuis les coins | Installation 1 s `power2.inOut` | Concentrer le regard sur le sujet | `motion-prompt/e/112.txt` |
| 113 | Tons clairs (High-key) | Les couleurs virent au clair presque blanc, les ombres deviennent très légères | Installation 1 s `power2.inOut` | Produit ou portrait propre, léger, doux | `motion-prompt/e/113.txt` |
| 114 | Tons sombres (Low-key) | Presque tout plonge dans le noir ; seule l'arête éclairée du sujet ressort | Installation 1 s `power2.inOut` | Luxe, tension, mystère | `motion-prompt/e/114.txt` |
| 115 | Noir et blanc (Black and white) | La couleur se retire ; les formes ne se lisent plus que par leur luminosité | Installation 1 s `power2.inOut` | Intemporel ; quand forme et lumière comptent plus que la couleur | `motion-prompt/e/115.txt` |
| 116 | Bichromie (Duotone) | Les couleurs sont remplacées par un dégradé entre deux teintes (ombres indigo, lumières roses) | Installation 1 s `power2.inOut` | Unifier affiches et visuels aux couleurs de la marque | `motion-prompt/e/116.txt` |
| 117 | Sarcelle et orange (Teal and orange) | Les ombres tirent vers le bleu-vert, la peau et les hautes lumières vers l'orange | Installation 1 s `power2.inOut` | Look bande-annonce, fort contraste de couleurs | `motion-prompt/e/117.txt` |
| 118 | Grain de film (Film grain) | Un grain fin recouvre l'image, les couleurs tirent légèrement vers le crème | Installation 1 s `power2.inOut` | Casser le rendu numérique trop propre | `motion-prompt/e/118.txt` |
| 119 | Fuite de lumière (Light leak) | Une bande de lumière jaune pâle à rouge entre par le bord droit et ondule lentement | Installation 1 s `power2.inOut` | Souvenirs d'été, aspect accidentel et nostalgique | `motion-prompt/e/119.txt` |
| 120 | Double exposition (Double exposure) | Le fond devient blanc et un paysage apparaît uniquement dans la silhouette du buste | Installation 1 s `power2.inOut` | Affiche ou couverture qui lie une personne à un lieu, un souvenir | `motion-prompt/e/120.txt` |

## Pack `motion2` — motion design, suite (121–144)

Cycle : 4,7 s. Kit : `motion-prompt/kit/motion2.js`.

| # | Nom français (nom d'origine) | Ce qui bouge | Durée et courbe typiques | Quand l'utiliser | Code |
|---|---|---|---|---|---|
| 121 | Anticipation (Anticipation) | Un carré recule de 44 px à contresens, s'écrase (1,22 × 0,76), puis part d'un coup | Élan 0,75 s `power1.inOut` ; départ 0,43 s `back.out(1.1)` | Juste avant un saut, un départ, un lancement : donner de l'élan et du poids | `motion-prompt/e/121.txt` |
| 122 | Mouvement de suite (Follow-through) | Le corps glisse et s'arrête net ; le drapeau et la queue continuent d'osciller puis se calment | Déplacement 0,7 s ; parties accrochées sur ressorts amortis | Cheveux, vêtements, accessoires, détails d'un logo : faire sentir leur poids | `motion-prompt/e/122.txt` |
| 123 | Rebond (Bounce) | Une balle tombe et rebondit de moins en moins haut jusqu'à l'arrêt | Gravité ; 56 % de la vitesse gardée à chaque rebond ; ≈ 1,7 s au total | Tout ce qui tombe et se pose : icône, mot, produit | `motion-prompt/e/123.txt` |
| 124 | Tremblotement (Wiggle) | Une cloche tremble sans arrêt, de façon irrégulière | Somme de 4 sinus (≈ 5 à 13 Hz), bouclée sans couture | Notification, appel entrant, élément qui doit attirer l'œil | `motion-prompt/e/124.txt` |
| 125 | Pulsation (Pulse) | Un cœur bat en double coup ; des contours s'élargissent autour | Un battement toutes les 1,175 s (+26 % puis +15 %) ; ondes 0,8 s `power2.out` | Like, indicateur de direct ou d'enregistrement, bouton à presser | `motion-prompt/e/125.txt` |
| 126 | Trajectoire (Motion path) | Un avion en papier suit un tracé en pointillés, s'oriente dans le sens du trajet et fait un looping | 4,7 s le long du chemin ; traînée de 24 segments | Tout ce qui suit un itinéraire : objet volant, voiture, trajet sur une carte | `motion-prompt/e/126.txt` |
| 127 | Boucle aller-retour (Ping-pong loop) | Un carré va à un bout puis revient par le même chemin, comme lu à l'envers | 2,35 s aller + 2,35 s retour, progression linéaire | Indicateurs de chargement, animations d'attente | `motion-prompt/e/127.txt` |
| 128 | Style image par image (Stop-motion style) | Une étoile avance par à-coups à environ 8 images par seconde, chaque pose un peu décalée | Chaque pose tenue ≈ 0,124 s (`steps()`), rien entre deux poses | Rendu fait main, pâte à modeler, collage | `motion-prompt/e/128.txt` |
| 129 | Texte brouillé (Text scramble) | Des caractères aléatoires défilent, puis le bon mot se verrouille de gauche à droite | Changement toutes les 0,062 s ; verrouillage décalé de 0,18 s par lettre | Titre, chiffre ou nom de code avec un effet de décodage | `motion-prompt/e/129.txt` |
| 130 | Texte en vague (Wave text) | Les lettres montent et descendent l'une après l'autre | Une vague toutes les 1,57 s, sinus ; lettres étirées de 6 % en haut | Logo, titre court, légende calée sur la musique | `motion-prompt/e/130.txt` |
| 131 | Texte sur un tracé (Text on a path) | Une ligne de texte coule le long d'une courbe, chaque lettre s'oriente | Vitesse constante (une longueur de texte par cycle) | Texte autour d'un logo, le long d'une route, d'une rivière | `motion-prompt/e/131.txt` |
| 132 | Police variable animée (Variable font animation) | La graisse du mot passe de fin à très gras et revient | Deux allers-retours par 4,7 s, courbe en cosinus | Exprimer l'intensité ou l'émotion par la lettre elle-même | `motion-prompt/e/132.txt` |
| 133 | Texte en masque (Text mask) | Une scène animée n'est visible qu'à l'intérieur de grosses lettres, puis s'ouvre en entier | Ouverture 0,4 s (lissée), retour 0,4 s | Mettre une photo ou une vidéo dans un titre ou un nom de marque | `motion-prompt/e/133.txt` |
| 134 | Répéteur (Repeater) | Une forme est dupliquée en cercle (1 → 12) ; les copies tournent et pulsent en décalé | Déploiement 1,35 s `power1.inOut` | Indicateurs de chargement, motifs de fond, fleurs, rayons | `motion-prompt/e/134.txt` |
| 135 | Kaléidoscope (Kaleidoscope) | Un motif à 8 symétries tourne et s'étale depuis le centre | Rotation de 90° par 4,7 s, vitesse constante | Clip musical, fond de scène, changement de scène onirique | `motion-prompt/e/135.txt` |
| 136 | Trait vibrant (Line boil) | Les traits d'un dessin à la main tremblent pendant que le dessin reste en place | Redessin toutes les 0,1 s, écart ≤ ±3,5 px | Illustrations, icônes ou lettrages dessinés à la main | `motion-prompt/e/136.txt` |
| 137 | Transition par poussée (Push transition) | La scène suivante entre par le côté et pousse l'actuelle dehors | 1,15 s `power2.inOut` | Enchaîner diapositives, photos ou étapes avec continuité | `motion-prompt/e/137.txt` |
| 138 | Transition store (Blinds transition) | Les fentes d'une rangée de lamelles s'élargissent jusqu'à ouvrir la scène suivante | 1,25 s `power1.inOut`, 7 lamelles | Bascule nette entre deux scènes (jour / nuit, avant / après), touche rétro | `motion-prompt/e/138.txt` |
| 139 | Transition cube (Cube transition) | Comme un cube qui tourne : la face avant part, la suivante arrive | 90° en 1,15 s `power2.inOut` | Enchaîner produits, offres ou écrans avec de la profondeur | `motion-prompt/e/139.txt` |
| 140 | Page cornée (Page curl) | La page se soulève depuis son coin, se replie et découvre la suivante | 1,4 s `power1.inOut` | Livres, catalogues, albums, changement de chapitre | `motion-prompt/e/140.txt` |
| 141 | Pixellisation (Pixelate) | L'image se change en blocs de plus en plus gros, bascule au plus gros, puis redevient nette | 1,7 s ; blocs de 1 à 27 par paliers | Changement de scène façon jeu vidéo, rétro, numérique | `motion-prompt/e/141.txt` |
| 142 | Bris de verre (Shatter) | L'image se fissure, les éclats s'envolent et découvrent la scène suivante | Fissures 0,35 s ; éclats à 220–480 px/s | Impact, rupture, retournement, juste avant un titre fort | `motion-prompt/e/142.txt` |
| 143 | Vue éclatée (Exploded view) | Un téléphone se sépare en couches, puis se réassemble | 0,75 s par couche, décalage 0,08 s, `back.out(1.3)` | Expliquer d'un coup d'œil ce qu'il y a dans un produit | `motion-prompt/e/143.txt` |
| 144 | Écran partagé (Split screen) | Une scène plein cadre se divise en deux puis en trois panneaux, chacun avec sa scène | 0,5 s par division | Comparer, montrer des actions simultanées, aligner des options | `motion-prompt/e/144.txt` |

## Pack `lp2` — effets de page web, suite (145–168)

Un passage : 4,7 s (cycle du pack : 9,4 s). Kit : `motion-prompt/kit/lp2.js`. Comme pour `lp`, défilement, survol et clic sont simulés sur la timeline.

| # | Nom français (nom d'origine) | Ce qui bouge | Durée et courbe typiques | Quand l'utiliser | Code |
|---|---|---|---|---|---|
| 145 | Frise au défilement (Timeline on scroll) | Une ligne grandit vers le bas ; chaque point atteint se remplit, son année et son événement glissent depuis la droite | Défilement 2 s `power2.inOut` ; éléments en `power2.out` | Histoire d'une entreprise, jalons, processus par étapes | `motion-prompt/e/145.txt` |
| 146 | Révélation de texte au défilement (Scroll text reveal) | Un titre gris clair se fonce caractère par caractère | Piloté par le défilement (2,3 s `power2.inOut`) | Courte déclaration à lire lentement | `motion-prompt/e/146.txt` |
| 147 | Cartes empilées (Stacking cards) | La carte suivante monte et se pose sur la précédente, qui rétrécit et s'assombrit un peu | 0,8 s par carte `power2.inOut` | Étapes, fonctions ou offres montrées une carte à la fois | `motion-prompt/e/147.txt` |
| 148 | Changement de fond au défilement (Background color change on scroll) | Le fond de la page se fond d'une couleur à l'autre à chaque section ; le texte s'inverse sur fond sombre | Mélange `power1.inOut`, piloté par la position | Récit par chapitres, contraste jour / nuit ou saisons | `motion-prompt/e/148.txt` |
| 149 | En-tête escamotable (Hide-on-scroll header) | L'en-tête sort par le haut quand on descend et revient dès qu'on remonte | 0,3 s `power1.inOut`, 36 px | Petits écrans : laisser la place au contenu | `motion-prompt/e/149.txt` |
| 150 | Repère de section (Scrollspy) | Dans le sommaire, l'entrée de la section en cours s'allume ; la surbrillance passe à la suivante | 0,25 s `power2.out` | Longs articles, documentation, FAQ | `motion-prompt/e/150.txt` |
| 151 | Bouton retour en haut (Back-to-top button) | Un bouton rond apparaît en bas à droite après avoir défilé ; un clic ramène en haut | Apparition liée au défilement ; survol 0,2 s | Longues pages | `motion-prompt/e/151.txt` |
| 152 | Zoom au défilement (Zoom on scroll) | Une petite photo au centre grandit jusqu'à remplir la fenêtre ; le texte autour s'efface, un titre apparaît dessus | 2 s `power2.inOut` | Voyage, immobilier, marque : faire entrer dans la photo | `motion-prompt/e/152.txt` |
| 153 | Inclinaison 3D au survol (3D tilt on hover) | La carte s'incline en profondeur selon la position du curseur ; un reflet traverse sa surface | 0,4 s `power2.out`, retour 0,4 s | Cartes de membre, emballages, offres : donner un aspect d'objet | `motion-prompt/e/153.txt` |
| 154 | Projecteur au survol (Spotlight hover) | Sur des cartes sombres, seul un cercle autour du curseur est éclairé ; les bords voisins luisent | Suit le curseur sans retard | Sites sombres avec rangées de cartes | `motion-prompt/e/154.txt` |
| 155 | Changement d'image au survol (Image swap on hover) | La photo de face du produit se fond vers la vue de dos | 0,3 s `power1.inOut` | Boutique en ligne : montrer un autre angle sans quitter la liste | `motion-prompt/e/155.txt` |
| 156 | Texte roulant au survol (Text roll on hover) | Les lettres du mot roulent vers le haut une à une, remplacées par le même mot en couleur | 0,36 s `power2.inOut`, décalage 0,035 s par lettre | Menus et boutons : réponse tactile | `motion-prompt/e/156.txt` |
| 157 | Aperçu d'image au survol (Hover image reveal) | La photo de la ligne survolée apparaît près du curseur et le suit | 0,25 s `power2.out`, échelle 0,85 → 1 | Listes en texte seul (réalisations, biens) avec aperçu à la demande | `motion-prompt/e/157.txt` |
| 158 | Libellé flottant (Floating label) | Le libellé du champ rétrécit (15 → 11,5 px) et monte sur la bordure | 0,24 s `power2.out` | Formulaires à nombreux champs | `motion-prompt/e/158.txt` |
| 159 | Validation en direct (Inline validation) | Pendant la saisie le champ est rouge avec un message ; une fois complet, il passe au vert avec une coche | Changement 0,15 à 0,25 s `power2.out` ; coche en `elastic.out` | Formulaires d'inscription ou de contact | `motion-prompt/e/159.txt` |
| 160 | Bouton de chargement (Loading button) | Le bouton se réduit en cercle avec un indicateur, puis s'élargit en « Terminé » vert | Réduction 0,3 s `power2.inOut` ; indicateur : un tour en 0,7 s | Envoyer, acheter, enregistrer | `motion-prompt/e/160.txt` |
| 161 | Transition d'élément partagé (View transition) | La photo cliquée dans la liste grandit et devient l'image du haut de la page de détail | 0,6 s `power2.inOut` ; le reste se fond autour | Galerie ↔ détail : ne jamais perdre de vue ce qu'on a ouvert | `motion-prompt/e/161.txt` |
| 162 | Visionneuse (Lightbox) | La page s'assombrit (0,82) et la vignette cliquée grandit au centre | Ouverture 0,45 s `power2.out` ; fermeture 0,35 s `power2.inOut` | Voir une image en grand sans quitter la page | `motion-prompt/e/162.txt` |
| 163 | Points d'intérêt (Hotspots) | Des points blancs pulsent sur l'image ; un clic ouvre une note sur la partie concernée | Onde toutes les 1,57 s ; bulle 0,25 s `power2.out` | Produits, plans, cartes : expliquer plusieurs zones d'une image | `motion-prompt/e/163.txt` |
| 164 | Compte à rebours (Countdown timer) | Heures, minutes, secondes décomptent ; seuls les chiffres qui changent glissent | 0,32 s `power2.inOut` par chiffre | Offre limitée, date limite | `motion-prompt/e/164.txt` |
| 165 | Séparateur ondulé animé (Animated shape divider) | À la frontière de deux sections, deux vagues superposées ondulent lentement | Sinus continus en sens opposés, boucle 4,7 s | Bords de section doux (mer, été, enfance) | `motion-prompt/e/165.txt` |
| 166 | Animation du bouton J'aime (Like button animation) | Le cœur se contracte, se remplit, grossit avec ressort ; des particules jaillissent, le compteur augmente | Contraction 0,1 s (0,78) ; pop à 1,45 en 0,12 s `power2.out` ; éclat 0,5 s | Confirmer clairement un j'aime, un favori | `motion-prompt/e/166.txt` |
| 167 | Invitation à défiler (Scroll-down cue) | Le mot « SCROLL », un point dans un contour de souris et des chevrons répètent un mouvement vers le bas | Boucle ; point en `power1.inOut`, chevrons en sinus | Signaler que la page continue plus bas | `motion-prompt/e/167.txt` |
| 168 | Vidéo d'arrière-plan (Background video) | Nuages et vagues bougent derrière un titre et un bouton immobiles | Boucle continue, vitesses constantes | Ouverture d'un site de voyage, d'hôtel, de restaurant | `motion-prompt/e/168.txt` |

## Pack `camera2` — caméra, angles et montage (169–192)

Un passage : 4,7 s (cycle du pack : 9,4 s). Kit : `motion-prompt/kit/camera2.js`. Voir `camera.md`.

| # | Nom français (nom d'origine) | Ce qui bouge | Durée et courbe typiques | Quand l'utiliser | Code |
|---|---|---|---|---|---|
| 169 | Translation verticale (Pedestal) | Toute la caméra monte tout droit sans changer de direction | 2,9 s `power2.inOut` | Parcourir une étagère ou un immeuble de bas en haut sans incliner | `motion-prompt/e/169.txt` |
| 170 | Tonneau (Barrel roll) | La caméra fait un tour complet sur l'axe de l'objectif | 3,1 s `power2.inOut` | Images aériennes énergiques, vertige, confusion | `motion-prompt/e/170.txt` |
| 171 | Hyperlapse (Hyperlapse) | La caméra avance le long d'une rue pendant que soleil, nuages et passants défilent en accéléré | 3,7 s `power2.inOut` | Couvrir une longue distance et une longue durée d'un seul geste | `motion-prompt/e/171.txt` |
| 172 | Plan-séquence (Long take) | Un seul plan continu suit un marcheur, sans aucune coupe | 4,2 s d'un trait | Garder la tension et la présence, montrer une action comme un seul flux | `motion-prompt/e/172.txt` |
| 173 | Plan au stabilisateur (Steadicam) | La caméra glisse derrière un marcheur avec un balancement lent, sans à-coups | Vitesse constante ; balancement ±3,5 cm | Rendre un déplacement à pied fluide et « cinéma » | `motion-prompt/e/173.txt` |
| 174 | Plan de suivi (Follow shot) | La caméra suit de dos, à quelques mètres, un marcheur qui zigzague | 3,9 s `power2.inOut` | Entrer dans un lieu avec un personnage ; vue à la troisième personne | `motion-prompt/e/174.txt` |
| 175 | Plan fixe (Locked-off shot) | La caméra ne bouge pas d'un pixel ; seuls les sujets traversent le cadre | Aucun mouvement de caméra | Faire ressortir le sujet par contraste, observation, base d'un accéléré | `motion-prompt/e/175.txt` |
| 176 | Traversée (Fly-through) | La caméra vole vers un mur percé d'une fenêtre, passe par l'ouverture et débouche de l'autre côté | 3,1 s `power2.inOut` | Entrer dans un bâtiment en ouverture, passer d'un lieu à un autre d'un seul geste | `motion-prompt/e/176.txt` |
| 177 | Contre-plongée (Low angle) | La caméra descend près du sol (0,35 m) et regarde vers le haut (≈ 18°) | 1,6 s `power2.inOut`, puis maintien 2 s | Rendre un personnage puissant, souligner la hauteur | `motion-prompt/e/177.txt` |
| 178 | Plongée (High angle) | La caméra monte (4,5 m) et regarde vers le bas (≈ 29°) | 1,6 s `power2.inOut`, puis maintien 2 s | Rendre un personnage petit ou vulnérable, expliquer une situation vue d'en haut | `motion-prompt/e/178.txt` |
| 179 | Caméra subjective (POV shot) | On voit par les yeux du personnage : balancement de la marche, mains en bas du cadre | 3,9 s `power2.inOut` ; balancement ±3 cm | Mettre le spectateur à la place du personnage | `motion-prompt/e/179.txt` |
| 180 | Par-dessus l'épaule (Over-the-shoulder) | L'arrière de la tête et l'épaule d'un personnage, flous, au bord du cadre ; l'autre est net en face ; lente avancée | 2,9 s `power2.inOut` | Montrer qui parle à qui, se concentrer sur l'expression de l'autre | `motion-prompt/e/180.txt` |
| 181 | Vue zénithale (Bird's-eye view) | Vue à la verticale ; la caméra s'élève (9 → 15 m) et le champ s'élargit | 2,9 s `power2.inOut` | Montrer une disposition, des trajets, comme sur un plan | `motion-prompt/e/181.txt` |
| 182 | Grande profondeur de champ (Deep focus) | Du premier plan au fond, tout devient net en même temps | 2,9 s `power2.inOut` | Laisser le regard libre, montrer plusieurs actions à des profondeurs différentes | `motion-prompt/e/182.txt` |
| 183 | Plan d'ensemble d'ouverture (Establishing shot) | Vue large et haute de toute la ville, lente avancée ; une légende de lieu apparaît en bas à gauche | 3,9 s `power2.inOut` ; légende 0,4 s | Au début d'une scène : dire où l'on est | `motion-prompt/e/183.txt` |
| 184 | Très gros plan (Extreme close-up) | Du gros plan du visage à un cadre rempli par les yeux (focale ×3,3) | Zoom exponentiel, `power2.inOut` | Pic d'émotion, faire remarquer un petit détail | `motion-prompt/e/184.txt` |
| 185 | Plan d'insert (Insert shot) | Un très gros plan d'un détail de la scène (la montre) est inséré 1,3 s, puis retour au même plan | Deux coupes franches | Montrer un petit objet, un geste, un accessoire important | `motion-prompt/e/185.txt` |
| 186 | Coupe fondue (Morph cut) | Deux prises du même personnage sont jointes en interpolant position et pose : rien ne saute | 0,45 s `power1.inOut` | Resserrer une interview, retirer une hésitation sans que ça se voie | `motion-prompt/e/186.txt` |
| 187 | Fondu au noir (Fade to black) | L'image s'enfonce dans le noir, puis la scène suivante en ressort | Fermeture 1,2 s, noir 0,5 s, ouverture 1,2 s, `power1.inOut` | Fin de chapitre, long passage de temps, fin d'histoire | `motion-prompt/e/187.txt` |
| 188 | Fermeture à l'iris (Iris out) | Un cercle se referme sur le personnage jusqu'au noir, puis se rouvre sur la scène suivante | Fermeture 1,4 s, noir 0,4 s, ouverture 1,3 s, `power1.inOut` | Fin façon film muet ou dessin animé, pause ludique | `motion-prompt/e/188.txt` |
| 189 | Plan de coupe (Cutaway) | On passe de l'orateur au public qui écoute, puis on revient | Deux coupes franches ; 1,3 s ailleurs | Montrer une réaction, masquer une ellipse ou une erreur | `motion-prompt/e/189.txt` |
| 190 | Montage alterné (Cross-cutting) | Deux scènes simultanées (un coureur, une voiture) alternent en plans de plus en plus courts | Coupes franches ; plans de 1,1 s → 0,3 s | Faire monter la tension entre deux actions : poursuite, sauvetage | `motion-prompt/e/190.txt` |
| 191 | Temps suspendu (Bullet time) | Au sommet d'un saut, le temps passe à 0,1× pendant 1,8 s et la caméra tourne de ≈ 69° autour du personnage | Rotation en `power2.inOut` | Montrer un instant décisif en volume, clou d'une scène d'action | `motion-prompt/e/191.txt` |
| 192 | Montage-séquence (Montage) | Sept plans courts résument trente jours ; coupes franches, la date saute à chaque plan | Plans de 0,6 à 0,75 s | Condenser une longue période d'effort ou de changement | `motion-prompt/e/192.txt` |

---

## Index par besoin (pour choisir vite)

| Besoin | Numéros à regarder d'abord |
|---|---|
| Faire entrer un titre | 005, 008, 129, 133 |
| Faire entrer un petit élément | 001, 003, 010 |
| Faire entrer une liste, un graphique | 002, 004, 007 |
| Donner du poids, de la vie | 011, 121, 122, 123, 024 |
| Fond qui vit (boucles discrètes) | 016, 095, 096, 136, 165 |
| Insister sur un chiffre | 007, 024, 028, 184 |
| Changer de scène en douceur | 044, 017, 019, 137 |
| Changer de scène avec énergie | 043, 020, 018, 046, 142 |
| Raccord intelligent | 042, 161 |
| Montrer une interface | 049 à 072, 081, 085, 160, 166 |
| Expliquer un objet | 143, 030, 163 |
| Fin de vidéo | 187, 188, 031 |
| Style fait main ou image par image | 128, 136 |
| Style rétro, jeu vidéo | 141, 023 |
