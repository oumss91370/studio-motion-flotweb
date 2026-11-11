# Film muet des années 1920

## 1. Identité

- **Nom** : Film muet des années 1920.
- **Inspiration** : le burlesque muet (le gag entier dans un seul plan large fixe, un visage impassible, un corps qui joue, le « presque raté »), les films à trucs des débuts (l'iris, la substitution), les feuilles de musique des pianistes de salle (une musique par humeur, le piano qui fait les bruitages), et les hommages modernes qui montrent combien peu de cartons suffisent. On n'utilise jamais l'allure d'un comique célèbre (chapeau melon, petite moustache, canne), ni un gag de vrai film, ni une mélodie publiée.
- **Ce que c'est** : un film d'une bobine **tel qu'on le verrait projeté** :
  - une copie 4:3 dans une fenêtre, entre des rideaux de salle ;
  - un **dessin à l'encre avec gris lavés et hachures**, tiré sur pellicule argentique qui scintille, flotte, se raye et brûle aux bords ;
  - **personne ne parle** : l'action en plans larges et des **cartons** racontent ;
  - le seul son est **un instrument de salle** (piano, orgue) et le projecteur.
- **Marche pour** : réaction en chaîne (une chaîne logistique qui déraille, une rumeur), démonstration muette d'un produit par l'absurde, archive d'entreprise ou film de famille « redessiné », annonce à chute, hommage, journal d'actualités à l'ancienne.
- **Ne marche pas pour** : contenu dense (trop d'étapes tue un film muet), explication parlée, gros plans d'émotion, client pressé de lire un message en 3 s.
- Ce n'est ni un film noir (pas d'ombres dures comme ambiance, pas de voix off), ni un filtre sépia sur une animation moderne (le dessin lui-même est gravé et encré).

## 2. Palette, typographie, matières

- **Argent monochrome**, teinté seulement par le tirage. Densités d'impression : encre 0,07 ; tissu sombre 0,15 à 0,30 ; bois moyen 0,45 à 0,60 ; peau 0,80 ; linge blanc 0,90 à 0,95. Noir du tirage ≈ 0,055, blanc ≈ 0,93.

| Rôle | Valeur |
|---|---|
| Noir du tirage / blanc du tirage | `#0E0E0E` / `#EDEDED` (avant virage) |
| Virage sépia (dose 0,10 à 0,36) | tend vers `#E8DCC4` dans les clairs, `#1A1410` dans les sombres (indicatif) |
| Teintes de section (variante au sépia) | ambre pour les intérieurs de jour, bleu pour la nuit, rose pour la tendresse : **une teinte par section** |
| Rideaux de salle | velours rouge sombre `#3A0E12` éclairé par l'écran et par la rampe (indicatif) |

- **Teinte et dégâts sont des réglages d'humeur** : plus froid et plus abîmé (moins de sépia) quand tout va mal, plus chaud et plus propre quand le film devient tendre.
- **Une couleur au plus** : un élément dessiné dans un masque à part garde sa teinte à travers le tirage (il reçoit quand même grain, scintillement et vignettage). On l'emploie pour la seule chose dont parle le film, ou pas du tout.
- **Typographie** (OFL) : **Playfair Display SC** pour titres et cris ; **Old Standard TT Italic** pour narration et dialogue.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Playfair Display à la place de Playfair Display SC ; EB Garamond à la place d'Old Standard TT. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/playfair-display-sc`, `@fontsource/old-standard-tt` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Cartons** : carton noir peint à bordure Art déco dont l'ornement suit l'émotion : un filet lourd pour un cri (le texte tremble), double filet à coins en gradins et éventails pour la narration, lianes et petites fleurs pour la tendresse.
- **Personnages** : proportions réalistes (adultes de 7,5 têtes, enfants ≈ 5), maquillage d'époque (peau pâle, paupières et lèvres sombres), identité par marques de silhouette (un chapeau, un vêtement, un outil).

## 3. Composition 9:16

- Original : fenêtre 1440×1080 au centre d'un cadre 16:9, la salle sur les côtés. En vertical (mise en page tenue au rendu réel du 11/11/2026) : **fenêtre de projection 1000×750** (4:3, coins arrondis de 22 px, bord sombre adouci) posée en x 40, y 420 à 1170. La fenêtre déborde de la zone utile à droite (x 945 à 1040 passe sous les boutons des applications) : **le texte d'un carton et le moment clé du gag tiennent entre x 60 et x 945** ; la bande de droite ne porte que du décor ou une sortie de champ. **La salle occupe le haut et le bas** : lambrequin de velours au-dessus (y 160 à 420), rampe de scène, têtes de spectateurs en silhouette ou clavier du pianiste en dessous (y 1170 à 1560). Les rideaux peuvent s'ouvrir au début et se fermer à la fin.
- Variante plus lisible sur téléphone : fenêtre 1000×1250 (4:5) en y 200 à 1450, rideaux étroits de chaque côté. On perd le format d'époque, on gagne en taille : à proposer au client. Dans la fenêtre 4:3, un personnage au tiers de la hauteur ne fait que 262 px, soit 87 px sur un téléphone de 360 px de large (mesuré au rendu) : dès que le jeu du personnage compte, prendre la variante 4:5.
- **Plans larges et moyens** : le gag se lit dans un plan fixe. Sujet à au moins 1/3 de la hauteur de la fenêtre au moment clé. Un gros plan de visage ressemble à un mannequin : garde-le petit ou dans un iris.
- **Cartons** : plein cadre de la fenêtre, texte entre x 100 et x 905, 3 à 8 mots, 54 à 64 px (titres 80 px). Trois à cinq cartons par film court. Un carton n'explique jamais ce que l'image montre déjà.
- 16:9 : fenêtre 1440×1080, rideaux sur les côtés.

## 4. Ce qui bouge

- **Action principale** : un gag ou un geste lisible dans un plan fixe : A déclenche B, B sort du cadre, le public attend, B revient et heurte C.
- **Boucle de fond 1** : défauts de la pellicule, renouvelés à chaque image : scintillement (faible : ±5 % de luminosité au plus, pas plus de 3 creux marqués par seconde ; voir la section 6), flottement de fenêtre avec de rares sauts de perforation, rayures verticales interrompues (blanches = émulsion grattée, sombres = saleté du négatif), grain d'argent, poussières, un poil dans la fenêtre.
- **Boucle de fond 2** : les hachures du dessin sont retracées toutes les deux images ; les rideaux respirent sous la lumière de l'écran.
- **Autorisés** : `#175` plan fixe, `#188` fermeture et ouverture à l'iris (un iris à demi ouvert, tenu, pour un regard au public), `#029` travelling avec premier plan qui défile (poursuite), `#027` avancée lente et motivée (tendresse), `#187` fondu au noir, `#144` écran partagé et `#120` double exposition (trucage, rêve), `#038` variation de vitesse (accéléré de la manivelle), `#121` anticipation (accroupi avant l'effort), `#040` pose tenue.
- **Interdits** : `#043` panoramique filé, `#044` fondu enchaîné à l'intérieur d'une scène, `#034` caméra à l'épaule, `#028` zoom, `#022` balayage de lumière, flou de mouvement moderne, couleur (hors l'unique masque), tout son d'ambiance réaliste.
- **Jeu impassible** : le visage change à peine, le corps joue. Les objets jouent aussi (un vacillement avant la chute).
- Poses par listes de clés interpolées ; seuls les gags voulus claquent (le sursaut en deux images).

## 5. Rythme et montage

- **Échantillonnage « à la manivelle »** : personnages et caméra à **16 poses par seconde** (18 ou plus pour accélérer une scène rapide) ; à 30 i/s, prends **15 poses par seconde** (une image sur deux) et 20 pour l'accéléré. Scintillement, grain et rayures changent à chaque image de sortie. Ce mélange donne l'air « projeté » plutôt que « saccadé ».
- **La vitesse est une émotion** : accélère poursuites et paniques (mouvement et scintillement plus rapides) ; reviens à la cadence normale et à un tirage plus calme pour les scènes tendres.
- Plans de 4 à 10 s ; un carton tient 2,5 à 3,75 s (≥ temps de lecture + 0,6 s).
- Transitions : iris, fondu au noir, coupe franche, rideau.
- Film court : **une seule chaîne lisible avec une pause au milieu** vaut mieux que trois chaînes chargées. Durée conseillée 30 à 60 s.
- Le geste du début, refait par quelqu'un d'autre à la fin avec un nouveau sens.
- **Version courte (8 à 12 s)** : une seule chaîne de gag en un ou deux plans fixes et **un seul carton** de 3 à 5 mots tenu 2,5 s ; couper les autres cartons, le titre et la reprise du geste final ; fermer par un iris de 1 s au plus (au-delà, la fin est presque noire sur téléphone). Accroche avant 3 s : A déclenche B dans les deux premières secondes. (Découpage tenu dans le rendu réel du 11/11/2026.)

## 6. Recette technique

- **Moteur** : HyperFrames. Chaîne en trois temps : (1) peinture tonale en gris dans un canvas 2D ; (2) passe **« redessin »** en WebGL2 qui encre toute l'image ; (3) passe **« tirage »** (pellicule) puis dégâts ; cartons, iris et salle par-dessus.
- **Personnages** : rig 2.5D (articulations résolues en 3D, projetées avec un angle de lacet). Pour un plan héros à plusieurs personnages, on peut poser et rendre les corps dans **Blender** (connecteur MCP `blender`, rendu gris sans texture) et les passer dans le redessin : même main que le reste. Three.js n'apporte rien de plus ici.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `encre.js` (formes tonales, trait, lavis, hachures), `redessin.js` (passe d'encrage), `pellicule.js` (tirage + dégâts, avec masque de couleur facultatif), `cartons.js` (intertitres, bordures, iris, salle), `figure.js` + `tetes.js` (rig), `timeline.js` (une feuille de repères qui pilote image **et** musique).
- **Passe « redessin » et « tirage » : méthode réellement utilisée** (rendu réel du 11/11/2026, un seul fragment shader WebGL2, écrit par l'agent d'essai ; rien n'est fourni par le plugin). La peinture tonale (canvas 2D, 1000×750, gris seulement) est envoyée en texture à chaque image ; le shader la redessine puis la « tire ».
  ```js
  const gl = cv.getContext("webgl2", { preserveDrawingBuffer: true, antialias: false });
  gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false);          // laisser à false : voir le piège « image à l'envers »
  // à chaque image : gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, peinture) puis un rectangle plein cadre
  ```
  ```glsl
  // v : coordonnées 0..1 du rectangle ; T : la peinture ; img : numéro d'image ; hach = floor(img / 2.0) ; flot : flottement en px
  vec2 px = vec2(v.x, 1.0 - v.y) * RES;                    // le seul retournement vertical, fait ici
  vec2 uv = (px + flot) / RES;
  float fin = flou(uv, 0.9), large = flou(uv, 2.6);        // deux flous gaussiens 5×5 de la luminance
  float encre = smoothstep(0.012, 0.05, large - fin);      // contour : du côté sombre de chaque arête
  float l = fin * 4.0;
  float pal = (floor(l) + smoothstep(0.32, 0.68, fract(l))) / 4.0;          // 5 paliers doux
  vec2 q = px + flot + vec2(hach * 3.7, hach * 1.9);       // les hachures se décalent toutes les 2 images
  float w1 = sin(q.y * 0.07 + hach) * 1.6;
  float h1 = 1.0 - smoothstep(0.16, 0.30, abs(fract((q.x + q.y + w1) / 9.0) - 0.5));   // hachures à 45°
  float h2 = 1.0 - smoothstep(0.16, 0.30, abs(fract((q.x - q.y - w1) / 9.0) - 0.5));   // croisées
  float d = pal;
  d *= 1.0 - 0.42 * h1 * (1.0 - smoothstep(0.30, 0.62, fin));   // dans les sombres
  d *= 1.0 - 0.45 * h2 * (1.0 - smoothstep(0.12, 0.34, fin));   // dans les plus sombres
  d = mix(d, 0.07, encre);
  // tirage : courbe en S, noirs à 0,055 et blancs à 0,93, densité inégale, scintillement, vignettage, grain
  d = smoothstep(0.0, 1.0, d); d = 0.055 + d * 0.875;
  d *= 0.94 + 0.06 * sin(px.x * 0.011 + img * 0.9) * sin(px.y * 0.017 - img * 0.6);
  d *= scint;                                              // voir « scintillement » ci-dessous
  vec2 c = v - 0.5; d *= 1.0 - dot(c, c) * 1.25;
  d += (h21(px + img * 17.0) - 0.5) * 0.10 + (h21(floor(px / 3.0) + img * 29.0) - 0.5) * 0.07;   // grain à deux échelles
  vec3 col = mix(vec3(d), mix(vec3(0.102, 0.078, 0.063), vec3(0.910, 0.863, 0.769), d), sepia * 2.6);   // sepia = 0,26
  ```
  Rayures (4 traits verticaux interrompus, blancs ou sombres), poussières (7 disques tirés à la graine de l'image), brûlure des bords et iris s'ajoutent ensuite dans le même shader. `flou` est une moyenne gaussienne 5×5 ; `h21` un hachage à deux entrées.
  - **Scintillement** : `scint` multiplie toute la fenêtre à chaque image. Reste à **±5 % au plus** (`0.95 + 0.10 * hasard(img)`), et pas plus de **3 creux marqués par seconde** : c'est une variation de luminosité sur une grande surface, et au-delà c'est un clignotement, risque pour les personnes photosensibles. Le film d'essai allait de 0,90 à 1,06 avec des creux de 0,12 : valeurs réduites ici par prudence, non re-rendues. Les hachures retracées toutes les 2 images sont des traits fins : petite surface seulement.
  - **Carton en HTML** : pour qu'il vive avec la pellicule, lui appliquer le même flottement (`transform: translate(fx, fy)`) et une opacité liée au scintillement. Un tel texte n'est jamais « immobile » pour le relevé automatique (tenue mesurée : 0,00 s) : le film déclare « Texte vivant : oui » (section 8) ; à défaut, écrire le relevé du carton à la main (début, fin, boîte).
- **Techniques clés** :
  ```js
  const tPose = Math.floor(t * 15) / 15;        // personnages et caméra « à la manivelle »
  const img   = Math.round(t * 30);             // graine des défauts : change à chaque image
  // redessin : contours = différence de deux flous gaussiens, du côté sombre de chaque arête ;
  // luminance ramenée à ~5 paliers doux ; hachures à 45° (puis croisées) dans les sombres,
  // retracées toutes les 2 images
  ```
  - **De vraies images vidéo peuvent passer par le même redessin** : une archive du client devient un dessin d'époque, de la même main que l'animation.
  - Tirage : ton argent + sépia, courbe en S, halo sur les lumières, densité inégale, brûlure brune qui monte des bords, vignettage, grain à deux échelles.
  - Un iris suit sa cible **en coordonnées du film**, après tout zoom de caméra.
- **Pièges** : bras de pantin (lever le bras de côté d'abord, laisser l'épaule monter, cacher le contour du bras là où il passe sur le torse) ; pose qui saute (jamais de bascule conditionnelle, toujours des clés interpolées) ; accessoire qui flotte (tenu entre les paumes ; un objet qui roule tourne de distance ÷ rayon) ; une main doit être **exactement** où est l'objet au temps de la prise ; rideaux fermés éclairés par un écran noir = noir total (ajoute la rampe) ; grain lourd = fichier énorme (voir « Encodage du grain ») ; **image à l'envers** : retourner la texture à la fois par `UNPACK_FLIP_Y_WEBGL` et dans le shader la remet la tête en bas ; un seul retournement, dans le shader ; **deux tons voisins dans le même palier** : une peau à 0,80 sur un ciel à 0,86 tombent dans le même des 5 paliers et la tête disparaît ; écarter les tons d'au moins 0,25 ou cerner la forme d'un contour d'encre peint ; **rendu lent** : WebGL sans carte graphique rend 5 à 10 fois plus lentement (2 min 30 à 2 min 54 pour 10 s, contre 30 s pour un film en canvas 2D) ; **fichier lourd** : le grain renouvelé à chaque image coûte très cher à l'encodage (42 Mo pour 10 s, 33,7 Mbit/s, en `--quality delivery`).
- **Encodage du grain** (essais du 11/11/2026 sur ce film de 10 s) : réencoder le rendu avec `ffmpeg -i rendu.mp4 -c:v libx264 -preset slow -crf 26 -tune grain -pix_fmt yuv420p -c:a copy film.mp4` : **9,7 Mo, 7,7 Mbit/s**, grain conservé à l'œil (ressemblance mesurée avec le rendu : 0,961). À `-crf 23` : 19 Mo, 15,2 Mbit/s ; à `-crf 20` : 31,6 Mo. Sans `-tune grain`, `-crf 23` donne aussi 9,5 Mo mais le grain fond en aplats. Pour alléger à la source : ramener le grain fin de 0,10 à 0,06.

## 7. Son

**Règle propre au style : aucun bruitage, aucune voix.** Le budget « environ 5 bruitages par 10 s » du studio ne s'applique pas : c'est l'instrument qui joue chaque évènement.

- **L'instrument est le bruitage** : piano droit (ou harmonium, orgue de cinéma, violon, petit ensemble). Vocabulaire : marche chromatique dans le grave (quelqu'un se faufile), petite note d'ornement (un clin d'œil), grappe de l'avant-bras (un fracas), trémolo diminué qui enfle (une attente), trémolo grave (un orage, une machine), « plink… plonk » (le vide), accord roulé (une porte, une révélation), glissando descendant (une chute), trille nerveux (l'hésitation), seconde mineure (quelque chose casse).
- **Musique par humeur**, à la manière des feuilles de repères : pressé, mystérieux, agité, tendre, majestueux ; un thème qui revient changé. Musique originale uniquement. Un vrai piano enregistré vaut mieux qu'un piano de synthèse.
- **Le projecteur est l'ambiance** : clic de la lampe, moteur qui se lance, ronron de la griffe, film qui bat sur la bobine.
- **Silence** : la musique s'arrête, le projecteur reste seul ; il encadre un moment tenu.
- Mix : dompter les attaques du piano par une compression légère, puis −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : filtre sépia sur un dessin vectoriel, trop d'étapes, gros plans de visages, cartons bavards, bruitages réalistes, fondus enchaînés, personnage qui rappelle un comique célèbre.

- [ ] L'image est une fenêtre de projection (4:3 ou la variante validée) entourée de la salle ; rien d'important hors zone sûre.
- [ ] Le dessin est encré et hachuré (contours du côté sombre, hachures dans les sombres), pas seulement désaturé.
- [ ] Les défauts de pellicule changent à chaque image ; personnages et caméra à 15 poses par seconde.
- [ ] Aucune voix, aucun bruitage : un instrument et le projecteur seulement.
- [ ] 3 à 5 cartons, 3 à 8 mots chacun, tenus ≥ 2,5 s ; aucun ne répète l'image.
- [ ] Le gag principal se comprend sur une vignette de la taille d'un pouce.
- [ ] Au plus une couleur dans tout le film.
- [ ] Aucune allure, aucun gag ni aucune mélodie d'un film existant.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : fixe
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : oui
- Taille mini du texte : 50

## 9. Aperçu

- Film de démo d'origine *The Runaway Loaf* (54 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/silent-film.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/silent-film.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/silent-film/STYLE.md`, `DEMO.md`, `demo/engine/ink.js`, `redraw.js`, `film.js`, `cards.js`, `figure.js`, `heads.js`, `demo/timeline.js`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Polices : Playfair Display SC, Old Standard TT (SIL OFL 1.1).
- Adaptation Flot Web : traduction, deux mises en page 9:16, cadence à 30 i/s, voie Blender pour les corps (non testée), valeurs hex indicatives (la source donne des densités), numéros du dictionnaire ; les noms de cinéastes et de films cités par la source ont été retirés.
- Vérifié par un rendu réel le 11/11/2026 (HyperFrames 0.9.33) : ça marche avec corrections ; export conforme (−13,7 LUFS) mais 42 Mo pour 10 s et un rendu de 2 min 30 à cause du grain et de WebGL ; le relevé du carton est à écrire à la main.
