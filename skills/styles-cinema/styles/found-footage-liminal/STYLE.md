# Found footage liminal

## 1. Identité

- **Nom** : Found footage liminal (cassette retrouvée dans un lieu vide).
- **Inspiration** : le folklore d'Internet des espaces vides sans fin, l'horreur « à règles » et l'étrange contemporain ; les images de caméscope grand public des années 90. **Jamais** dans le film : le nom que la communauté donne à ces lieux, ses numéros de « niveaux », ses noms d'entités, ni une organisation ou un logo existants. Tout ce qui est à l'écran (règles, formulaires, voix de l'entreprise, présence éventuelle) est original.
- **Ce que c'est** :
  - **un seul enregistrement de caméscope à la première personne** (VHS années 90, 4:3), à la main, continu ;
  - **un intérieur vide, familier mais faux**, qui se répète : bureaux, étage d'hôtel, école, centre commercial, parking, aile d'hôpital ; néons qui bourdonnent, personne ;
  - **l'angoisse vient du vide, de la répétition, des règles bureaucratiques et de la machinerie de la caméra qui lâche au mauvais moment**. Rien ne poursuit personne. Un frisson dans la nuque, pas un sursaut ;
  - **le support raconte** : mise au point, exposition, dégâts de bande et affichage à l'écran portent l'intrigue.
- **Marche pour** : série à suspense, annonce énigmatique, visite d'un lieu après la fermeture, « règlement » qui dérape, compte de fiction ou de jeu, teaser.
- **Ne marche pas pour** : marque rassurante, public enfant, explication, produit à montrer sous son meilleur jour, humour. Le style s'essouffle dès que plus rien de nouveau ne va de travers : film court.
- Ce n'est pas un film d'horreur (aucun monstre en gros plan, aucun sang, aucun sursaut, aucun coup de musique), ni une œuvre « terminal cathodique » (les défauts sont ceux de la bande et de l'objectif), ni une ruine (**le propre fait partie du style**).

## 2. Palette, typographie, matières

- **Une teinte dominante maladive** venue des matériaux du lieu, avec une plinthe plus sombre et un sol tacheté de la même famille ; plafond et dalles lumineuses presque blancs, un peu chauds.

| Lieu (exemples) | Matériaux |
|---|---|
| Bureaux | papier peint moutarde `#D5BD66` à rayures plus sombres, plinthe `#4D3D26`, moquette `#8C763C`, dalle de plafond `#D9D3B8`, diffuseur `#FBFAF0` |
| Piscine | carrelage `#9FC7C0`, joints `#E6ECE6`, eau `#5E8F96` |
| Couloir d'école | murs `#B9C49A`, casiers `#6F7F66`, lino `#A89A7D` |

- **Exactement une couleur saturée** : un signal (lampe d'alarme rouge, panneau de secours vert, voyant orange). Exemple : rouge `#FF2A1A`. C'est la seule chose qui fait de la lueur ; pousse son émission très haut (un rouge pur à faible émission ne « bave » jamais).
- La balance des blancs dérive ; la couleur n'est jamais étalonnée propre.
- **Typographie** (OFL) : sous-titres codés en **IBM Plex Mono 600** ; affichettes en **IBM Plex Sans Condensed** (titres) et **IBM Plex Sans 600** (règles numérotées) ; **affichage du caméscope dans une police bitmap 5×7 dessinée à la main**, à contour noir.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Oswald à la place d'IBM Plex Sans Condensed ; Inter à la place d'IBM Plex Sans ; IBM Plex Mono : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/ibm-plex-sans-condensed`, `@fontsource/ibm-plex-sans` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : cloisons, faux plafond à dalles, luminaires encastrés à intervalles réguliers. **Usure retenue**, en pourcentages à un chiffre : auréoles d'eau au pied de certains murs, bande jaunie sous le plafond, rares lés décollés, quelques dalles jaunies ou manquantes, insectes morts dans les diffuseurs.
- **Imprimés** : impression laser de bureau sur papier jauni, numéros de formulaire et de révision, règles numérotées, formule de politesse finale signée « La Direction ». Punaisés ou scotchés.

## 3. Composition 9:16

- Original : image 4:3 entre deux bandes noires dans un cadre 16:9. En vertical, deux mises en page (à vérifier par rendu) :
  1. **Fidèle** : image 4:3 de 1000×750 en x 40, y 440 à 1190, noir autour (l'affichage du caméscope et les sous-titres restent entre x 60 et x 945). L'affichage du caméscope reste dans l'image. Sous-titres codés dans la bande noire du bas (y 1230 à 1500). Très « cassette », mais petit.
  2. **Caméscope tenu à la verticale** (recommandée pour les réseaux) : image 3:4 de 1000×1333 en x 40, y 200 à 1533 (affichage du caméscope et sous-titres entre x 60 et x 945). Les couloirs, les portes et le faux plafond se prêtent au format haut. Prévenir le client que ce n'est pas le format d'époque.
- **Affichage** : `● REC` en haut à gauche, batterie en haut à droite (à gauche de x = 945), heure et date en bas à droite de l'image, au-dessus de y = 1560. Distorsion en barillet et vignettage s'appliquent à l'image, **pas** à l'affichage.
- **Sous-titres codés** : blanc sur boîte noire pleine par ligne, ≈ 44 px, 32 caractères par ligne au plus (24 en vertical), centrés ; intacts (c'est le téléviseur qui les décode). Marques : `[HAUT-PARLEUR]` pour les annonces, italique pour l'opérateur, descriptions entre crochets (`[LES NÉONS VACILLENT]`, `[SILENCE]`).
- **Les règles affichées ne sont pas sous-titrées** : elles sont l'image. Lisibles, découvertes au moins 3 à 4 s. Pour un gros plan, **baisse la caméra jusqu'à ce que l'objectif soit parallèle à la feuille** : plonger sur une feuille verticale incline les mots en faux italique.
- Toute présence : petite, loin, dans une zone de néons morts.

## 4. Ce qui bouge

- **Action principale** : une marche à la première personne où une règle est lue, suivie, puis contredite.
- **Boucle de fond 1** : **caméra à la main** = démarche (balancement de la tête de quelques centimètres, léger roulis) + respiration (≈ 0,27 Hz) + tremblement dont l'amplitude suit une **courbe de peur**. Sur un souffle retenu, **tout se fige**.
- **Boucle de fond 2** : néons : variations de quelques pour cent, extinctions brèves (≈ 0,1 s) ; l'exposition automatique rattrape avec retard (≈ 0,45 s) et le bruit de gain pompe.
- **Autorisés** : `#179` vue subjective, `#034` caméra à l'épaule, `#172` plan-séquence, `#033` bascule de point (la mise au point automatique cherche : flou → net → décroche → net), `#028` zoom avec recherche du point, `#027` avancée lente sans son, `#043` panoramique filé vers un bruit (puis rien), `#023` déchirure de bande (seule « coupe » permise), `#175` caméra posée qui enregistre seule.
- **Interdits** : toute coupe de montage classique (`#041`, `#046`, `#044`, `#045`), `#037` ralenti, musique d'accompagnement, sursaut, lignes de balayage et masque de tube (ce n'est pas un téléviseur), `#015` particules, lueur généralisée, mouvement brusque d'un objet (une porte met plus d'une seconde, en douceur).
- Regarder vers le bas ne montre que le bout des chaussures et le sol, jamais les jambes.

## 5. Rythme et montage

- **Une prise continue.** Les coupes n'arrivent que là où la bande casse : mise en route, déchirure de suivi, arrêt de l'enregistrement.
- **La déchirure est une coupe faite par l'univers** : même cadrage après, mais l'horloge a sauté, la batterie a baissé, un néon est mort.
- **L'affichage est une preuve** : enregistrement, batterie, date et heure font avancer l'intrigue.
- Les consignes commencent ordinaires, dérivent, se contredisent, et finissent par s'adresser au spectateur.
- **Le silence numérique total** (une seconde ou plus, queues comprises, sous-titré `[SILENCE]`) est l'outil le plus fort. Au plus un effroi doux : tout qui se rallume d'un coup au retour du son.
- Durée conseillée : 20 à 60 s. Bruit de bande à la cadence vidéo (30 par seconde).
- **Version courte (8 à 12 s)** : une prise de 8 à 10 s : la mise en route, une règle lue, une contradiction ; une seule déchirure ; ramener le silence numérique à 0,5 s et couper les consignes suivantes. Accroche avant 3 s : l'affichage qui démarre, puis l'affichette qui entre dans le cadre.

## 6. Recette technique

**Moteur conseillé : Blender** (connecteur MCP `blender`) pour un lieu riche et un rendu fiable ; **Three.js** pour un couloir simple en temps réel. Dans les deux cas : rendu **basse résolution** (720×540, ou 540×720 en vertical), puis **passe caméscope** et affichage dans HyperFrames. La basse résolution fait partie du look et cache la propreté de la synthèse.

| | Blender (qualité) | Three.js (léger) |
|---|---|---|
| Quand | plusieurs pièces, affichettes lisibles, usure, silhouette lointaine | un couloir et une pièce, délai court |
| Espace | cloisons sur une grille de 2,4 m générées en Python (`execute_blender_code`), plafond à 2,70 m, dalles 0,6×1,2 m | mêmes mesures, géométrie instanciée |
| Lumière | dalles émissives ; le rendu calcule rebonds et occultations : **baisse l'occultation** (lumière plate, sans ombres portées marquées) | aucune ombre : couleur et intensité de chaque dalle dans une texture ; chaque pixel additionne les dalles voisines (5×5) + un terme de rebond ; occlusion ambiante dans les angles |
| Brouillard | volume dont la densité de lumière suit l'éclairage local | couleur du brouillard × (lumière locale ÷ moyenne) |
| Caméra | clés + bruit de démarche et de tremblement sur la caméra ; mise au point animée | même rig, calculé depuis `t` |
| Sortie | suite d'images 720×540 → vidéo de fond dans HyperFrames | canvas WebGL piloté par `hf-seek` |
| Contrôle | outil `look` en vue caméra à chaque étape du trajet | captures fixes à chaque repère |

- **Techniques clés (les deux moteurs)** :
  - **Le brouillard suit la lumière locale** : là où les néons sont morts, la brume est sombre ; une silhouette s'y lit comme un **trou dans la lumière**. Fond de scène = brouillard × ≈ 0,15 : les couloirs se dissolvent dans le noir, jamais dans un mur clair.
  - **Trajet écrit à la main dans un espace rempli par programme** : chaque porte montre encore du vide.
  - Variation par luminaire : ±8 % chaud ou froid, un peu de vert, ≈ 3,5 % de néons morts, ≈ 2,5 % qui clignotent.
  - **Passe caméscope** (ce n'est pas un tube) : léger tremblement de ligne (ondulation ≤ 0,25 px, sinon le texte se couche), bande de commutation de tête sur les 8 dernières lignes, déchirure à la demande, barillet 0,07 et vignettage 0,42, flou de luminance + liseré de netteté, chrominance étalée et décalée vers la droite, traînée des lumières vives, balance qui dérive, bruit de gain dans les sombres, noirs relevés.
  ```js
  // mise au point automatique : distance de point animée avec dépassement
  // flou -> net -> décroche -> net ; le flou vient d'un point tiré trop PRÈS
  const peur = courbePeur(t);                    // 0..1, pilote tremblement et souffle
  ```
- **Pièges** : scène entièrement claire = couloir d'hôpital (cloisons à trous, lointains sombres) ; lumière qui traverse les murs (une zone morte exige tous les néons morts à ±5 m) ; rectangle clair au bout du couloir ; brouillard uniforme qui grise les silhouettes ; personnage en formes simples = jouet (silhouette organique dessinée sur un plan, fausse de 15 à 40 % : petite tête, long cou, épaules hautes et étroites, longs bras) ; réverbération lourde qui rend l'annonce inintelligible ; comprimer le temps d'une timeline finie (toutes les clés passent par une seule fonction de déformation).

## 7. Son

**Règle propre au style : aucune musique d'accompagnement.** Seulement ce que la cassette aurait enregistré. Une musique n'existe que dans le monde (musique d'attente, radio à travers un mur, jingle de haut-parleur), filtrée, réverbérée, qui peut ralentir avec le pleurage de la bande.

- **Lit de néons** : bourdonnement à 100 Hz et ses harmoniques (secteur à 50 Hz en Europe ; 120 Hz pour un lieu américain) avec une composante grésillante, un léger sifflement de ballast, des salves de tube défaillant ; il suit la même courbe de lumière que l'image ; plus proche dans les petites pièces. Un vrai enregistrement de néon est idéal.
- **Voix du haut-parleur** : calme, d'entreprise, à travers un haut-parleur de plafond (bande ≈ 300 à 3 500 Hz, saturation, réverbération de salle), assez sèche pour rester intelligible. Un court carillon original avant chaque annonce ; après un saut de temps, carillon et voix peuvent sonner un peu faux.
- **Opérateur** : quelques phrases courtes à voix basse, souffle dont le rythme suit la peur ; un souffle retenu, puis une longue expiration.
- **Bruitages par matière** (≈ 5 par 10 s, vrais enregistrements) : pas sur moquette ou crissements sur sol dur, froissement de tissu, clac et moteur du caméscope, moteur du zoom, tintement de ballast sur un clignotement, gond qui accroche, quelque chose qu'on traîne au-dessus.
- Mix : lit et musique du monde ≈ 8 dB sous les voix ; −14 LUFS ; aucun grain ajouté (le bruit est dans l'image).
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : monstre montré, sursaut, musique angoissante, lieu en ruine, coupes de montage, lignes de téléviseur, plusieurs couleurs vives, texte incliné en faux italique.

- [ ] Une prise continue ; les seules ruptures sont des évènements de bande.
- [ ] Le lieu est propre, vide et répétitif ; l'usure reste rare.
- [ ] Une seule couleur saturée dans tout le film, et elle seule fait de la lueur.
- [ ] Les lointains tombent dans le noir ; aucun rectangle clair au bout d'un couloir.
- [ ] L'affichage (enregistrement, batterie, date) change au moins une fois de façon significative.
- [ ] Au moins une affichette de règles lisible, tenue 3 s ou plus, texte droit.
- [ ] Aucune musique d'accompagnement ; au moins un silence total sous-titré.
- [ ] Aucun mot, numéro, nom ou logo du folklore du genre ou d'une organisation réelle ; toute présence reste petite et lointaine.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 44

## 9. Aperçu

- Film de démo d'origine *Night Shift Orientation* (60 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/backrooms.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/backrooms.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/backrooms/STYLE.md`, `DEMO.md`, `demo/world.js`, `tex.js`, `vhs.js`, `osd.js`, `subs.js`, `thing2d.js`, `story.js` (moteur d'origine : three.js). Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Polices : IBM Plex Sans, Sans Condensed, Mono (SIL OFL 1.1).
- Connecteur Blender : ahujasid/mcp-for-blender, commit `2e4b0bc`, MIT.
- Adaptation Flot Web : traduction, nom descriptif, deux mises en page 9:16, voie Blender et tableau comparatif (non testés par un rendu), fréquence du secteur en Europe, numéros du dictionnaire.
