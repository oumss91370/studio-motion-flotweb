# Risographie

## 1. Identité

- **Nom** : Risographie (impression au duplicateur à pochoir, en tons directs).
- **Inspiration** : l'illustration imprimée en riso (champs de couleur et silhouettes, une petite figure dans un grand monde, des couleurs en plus obtenues par surimpression), la comédie filmée de loin en plan large où les bruits du quotidien font le rythme, et les vraies impressions (encres translucides, repérage décalé, trous d'épingle, stries). Aucun personnage, composition ou palette recopiés. **Jamais** le nom, le logo ou l'habillage d'une marque de machine : les noms d'encres ne sont que des repères de couleur.
- **Ce que c'est** : une animation qui a l'air **imprimée, image par image**. Le procédé imprime **une couleur à la fois** : chaque couleur est sa propre plaque. De ce seul fait vient tout le look :
  - **une palette minuscule** : 2 ou 3 encres sur papier blanc cassé chaud ;
  - **le mélange par surimpression** : les encres se multiplient ; deux encres en font une troisième, les trois approchent le noir ;
  - **le repérage décalé** : chaque plaque tombe à quelques pixels près ; les bords montrent un filet de papier ou un halo coloré ;
  - **la trame** pour les demi-tons, chaque plaque à son angle ; **une encre imparfaite** (trous, stries, densité tachée) ;
  - **des formes plates, sans contour**.
- **La règle unique** : rien n'est peint, tout est imprimé. **Ni encre noire, ni encre blanche.**
- **Marche pour** : marque créative, café, librairie, festival, fanzine, agenda culturel, sujet du quotidien traité avec humour, vidéo sans voix.
- **Ne marche pas pour** : luxe, photo de produit, interface, sujet grave, petit texte.
- **À ne pas confondre** : pas du vectoriel plat avec du bruit ; pas le `pop-trame` (quadrichromie et cerne noir) ; pas l'`affiche-serigraphie` (encres **opaques**, sans trame).

## 2. Palette, typographie, matières

- **2 ou 3 encres, jamais plus**, plus le papier. Choisis des encres dont les paires donnent des couleurs utiles ; au moins une doit pouvoir porter une silhouette seule.

| Jeu d'encres | Hex |
|---|---|
| Bleu + jaune + rose fluo (lemo) | `#0078BF` + `#FFE800` + `#FF48B0` |
| Sarcelle + orange fluo (lemo, 2 encres) | `#00838A` + `#FF7477` |
| Bleu fédéral + rouge + tournesol (lemo) | `#3D5588` + `#FF665E` + `#FFB511` |
| Sarcelle + rose fluo + jaune (animate, valeurs mesurées) | `rgb(54,137,171)` + `rgb(220,68,160)` + `rgb(238,222,30)` |
| Papier | `#F4EEE2` (lemo) ou `#f2ece3` (animate), jamais blanc pur |

- Mélanges du jeu animate : rose + jaune = corail ; sarcelle + jaune = vert ; sarcelle + rose = bleu d'encre violacé ; les trois = noir olive (**jamais `#000`**). Le blanc = le papier (une réserve).
- Peau et surfaces claires : une teinte légère de l'encre la plus pâle. Des points d'une encre saturée sur une peau ressemblent à une éruption.
- Garde la **surimpression complète** (toutes les plaques, mélanges les plus denses) pour le moment qui la mérite.
- **Typographie** (OFL) : grotesque très grasse pour les titres (**Bricolage Grotesque 800**), sans-serif géométrique pour les légendes (**Jost 500 à 700**). **Le texte est imprimé** : il vit sur une plaque, donc il se décale et prend le grain avec elle. Un titre peut être imprimé sur deux plaques avec un décalage visible.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Archivo Black à la place de Bricolage Grotesque ; Outfit à la place de Jost. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/bricolage-grotesque`, `@fontsource/jost` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : trame à points (pas de 9 à 12 px en vertical 1080 ; angles espacés d'au moins 15°, par exemple 15°, 75°, 45°) ; au-dessus de ≈ 90 % de densité, l'encre imprime en plein (c'est ce qui garde texte et lignes nets) ; grain sur le seuil des points, trous d'épingle dans les aplats, stries dans le sens d'entraînement du papier, taches lentes de densité, fibres pâles.

## 3. Composition 9:16

- **Grandes formes plates, beaucoup de papier nu et d'encre pleine.** Un horizon, un grand champ ou un disque, une petite figure ; la tête de la figure contre la couleur la plus plate du cadre.
- **Chaque zone utilise au plus deux plaques, dont une seule en teinte tramée.** Trois trames superposées = de la boue.
- Trame **en paliers** (20 / 40 / 60 / 100 %) pour les ciels, les ombres, le lointain. Le pas de trame suit l'échelle de l'illustration : gros pour un fond lointain, moyen pour le décor, fin pour les petits objets et les étiquettes.
- Les personnages reçoivent un **halo de réserve blanc papier** de 5 à 6 px : les plaques se décalent autour, il prend des franges colorées comme un vrai débord d'impression.
- **Pense à la version à une seule plaque** : chaque couleur principale contient un peu de la première plaque, pour qu'une image à une encre reste une silhouette complète.
- **Sous-titres** : une **bande de réserve blanc papier** (zéro encre, petit arrondi) avec le texte sur une plaque, 48 à 54 px, vers y ≈ 1400 à 1520 ; ses bords attrapent les franges. Tenue ≥ max(1,8 s ; réplique + 0,6 s).
- Contenu dans x 60 à 940, y 250 à 1500 ; les champs de couleur vont jusqu'aux bords. Texte sur du ciel vide ou une bande de réserve.

## 4. Ce qui bouge

- **Action principale** : une petite figure qui traverse un grand cadre, jouée à 15 poses par seconde ; cycles simples sur peu de dessins ; mouvements secondaires (écharpe, drapeau, queue) en onde qui se propage.
- **Boucle de fond 1** : **l'impression respire** : environ un tiers du grain est retiré à chaque « tirage » ; repérage, pression du trait et manques d'encre tournent sur **3 variantes** : l'impression scintille sans ramper.
- **Boucle de fond 2** : reflets en plaques séparées (chaque plaque ondule sur sa propre phase), drapeaux, fumées.
- **Gestes natifs** : **les plaques racontent** (le monde gagne une encre à chaque tournant de l'histoire) ; deux encres, une troisième là où elles se rencontrent ; la **transition par surimpression** (une forme d'une encre grandit sur le cadre, puis rétrécit en la forme clé de la scène suivante) ; **le repérage comme rythme** ; la réserve révélée (une forme faite seulement d'encre manquante ; sa plaque arrive plus tard) ; l'échelle de trame (les points deviennent des formes quand la caméra avance) ; c'est une feuille de papier (on peut l'empiler, la plier, la couper).
- **Repérage** : **un jeu fixe de décalages par plan** (±1 à ±4 px). Une **secousse** (10 à 18 px, amortie en ≈ 0,25 s) sur un accent ; une **dérive** jusqu'à ≈ 30 px pendant un moment tenu, qui claque en place sur le temps fort.
- **Autorisés** : `#128` saccadé (personnages), `#029` travelling latéral large, `#175` plan fixe composé, `#181` vue du dessus, `#042` raccord sur une forme plate, `#046` coupe franche sur un temps, `#018` transition par forme, `#017` ouverture en cercle à liseré rugueux, `#027` avancée dans un champ de trame, `#028` recul qui révèle la feuille.
- **Interdits** : `#044` fondu enchaîné, volet numérique doux, dégradés lisses, ombres portées, flous, contours, noir pur, blanc d'encre, repérage qui tremble à chaque image.

## 5. Rythme et montage

- Personnages à **15 poses par seconde** (à 30 i/s : une image sur deux ; 12 seulement dans un film livré à 24 i/s), **caméra fluide** à chaque image (une caméra saccadée tremble).
- Coupes et événements sur la grille des croches ; choisis un tempo où la croche fait un nombre entier d'images (à 30 i/s : 112,5 BPM = 8 images ; 150 BPM = 6 images).
- **Une impression ne s'efface pas en fondu** : un titre arrive par un balayage de rouleau ou sur un temps, et part sur une coupe.
- Option forte : **chaque nouvelle plaque amène un instrument** ; elles peuvent repartir une à une.
- Un silence d'une mesure, queues de réverbération coupées, accompagne une dérive de repérage ; le claquement ramène tout.

## 6. Recette technique

- **Moteur** : HyperFrames ; canvas 2D pour dessiner les plaques, passe WebGL2 pour « imprimer ».
- **Principe** : dessine chaque image dans **un seul canvas RVB où chaque canal est la densité d'une plaque** (R = encre 1, V = encre 2, B = encre 3). Le dessin normal donne de vraies **réserves** ; le mode additif n'ajoute de l'encre qu'aux canaux choisis : une vraie **surimpression**.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `imprimer.glsl` (plaques, trame, grain, repérage, secousse et dérive, arrivée d'une plaque par balayage de rouleau), `dessiner.js` (densités d'encre, surimpression, halo de réserve, membres), `scenes.js`, `timeline.js`.
- **Techniques clés** :
  ```glsl
  // par plaque : décalage (repérage), trame à son angle, puis composition multiplicative
  vec2 q = rot(angle_i) * (px + decal_i) / pas;
  float point = cos(q.x * 6.2832) * cos(q.y * 6.2832) * 0.5 + 0.5;      // trame ancrée au PAPIER
  float couv = dens_i >= 0.9 ? 1.0 : smoothstep(seuil(dens_i) - aa, seuil(dens_i) + aa, point + grain);
  couleur = papier * mix(vec3(1.0), encre_i / papier, couv);            // répété pour chaque plaque
  ```
  ```js
  ctx.globalCompositeOperation = "lighter";      // surimpression : n'ajoute que dans les canaux choisis
  ```
  - La trame est ancrée **au papier** dans la version lemo (un panoramique fait glisser l'image sous une trame fixe, comme si chaque image était imprimée à neuf) et **à l'illustration** dans la version animate (la trame suit la caméra, comme une impression filmée). Choisis-en une par film ; la première convient aux plans fixes, la seconde aux mouvements de caméra.
- **Pièges** :
  - Un bruit mal mélangé dessine des rayures verticales dans les aplats en 1080p : utilise une fonction de hachage bien répartie.
  - **Captures JPEG : les points saturés bavent.** Images PNG vers un intermédiaire sans perte, encodé une fois ; vérifie à 100 % et à 50 % pour le moiré.
  - Le calque de halo doit copier la transformation du canvas, sinon un plan zoomé dessine le sujet à la mauvaise échelle.
  - Une couleur principale sans la première plaque flotte dans les images à une encre.
  - Marbrure du papier trop forte : elle se lit comme de la saleté sur téléphone.
  - Plusieurs calques plein cadre par image coûtent cher (une passe par pixel chacun) : donne une petite zone aux petits objets.

## 7. Son

- **Musique** : chaude, sèche, faite main, un peu lo-fi : contrebasse ou basse électrique, vibraphone ou marimba, guitare nylon, mélodie sifflée ou fredonnée, piano électrique, piano jouet, balais, shaker, petite boîte à rythmes passée dans une saturation de bande.
- **La machine est le bruitage signature** (≈ 5 par 10 s) : entraînement du papier (« chk »), tambour (« ka-tchonk ») à l'arrivée d'une plaque, ronron du moteur, feuille qui tombe sur une pile, coup de massicot. Les autres bruitages : secs, proches, papier.
- **Voix** : détendue, comme une conversation, phrases courtes. Musique baissée d'environ 8 dB sous la voix. Mix −14 LUFS ; **aucun grain ajouté** à l'encodage.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] **Chaque couleur vient des plaques** : 2 ou 3 encres, aucune valeur RVB libre dans une scène.
- [ ] **Les sombres sont des surimpressions** (noir olive), avec quelques manques ; aucun pixel noir pur.
- [ ] **Le blanc est du papier** (reflets, yeux, texte sur fond sombre : des réserves).
- [ ] **Franges visibles** : en zoomant sur un bord sombre, deux encres dépassent de côtés opposés.
- [ ] **Au plus deux plaques par zone, une seule tramée** ; les points changent de taille le long d'un dégradé.
- [ ] **Le repérage est fixe dans un plan** ; au moins une secousse ou une dérive placée sur la musique.
- [ ] **Le papier est plat** : ni vignettage, ni grain plaqué par-dessus.
- [ ] **Le texte est imprimé** (plein, décalé avec sa plaque) ; contenu dans x 60 à 940, y 250 à 1500.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 4
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 48

## 9. Aperçu

- Film de démo lemo-opuscar *Sunday Ride* (40 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/risograph.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/risograph.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/risograph.jpg · galerie : https://lemomo-ai.github.io/lemo-opuscar/#print-printmaking
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre l'histoire ni les plans.
- Image d'exemple animate (déjà en 9:16) : `plugins/animate/skills/animate/styles/riso/sample.png`, dépôt https://github.com/cth9191/animate (MIT, © 2026 cth9191) ; démo construisible `styles/riso/demo/` (6 s, pas de vidéo dans le dépôt).

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/risograph/STYLE.md`, `DEMO.md`, `demo/riso.js` (shader d'impression), `draw.js`, `sheet.js`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Apport : modèle « un canal par plaque », règles de composition, repérage comme rythme, gestes natifs, son.
- **cth9191/animate**, commit `7e5eb56` (0.4.0) : `plugins/animate/skills/animate/styles/riso/STYLE.md`, `kit.js`. Licence MIT, © 2026 cth9191. Apport : valeurs mesurées sur une vraie impression animée (encres, angles 15° / 75° / 45°, 20 niveaux de ton, pas de trame par échelle, décalages (+4, −3) et (−3, +4), 3 variantes de frémissement), liste de contrôle, zone sûre 9:16.
- Adaptation Flot Web : fiche fusionnée et traduite, choix explicite entre les deux ancrages de trame, tempos recalculés pour 30 i/s, numéros du dictionnaire de mouvements.
