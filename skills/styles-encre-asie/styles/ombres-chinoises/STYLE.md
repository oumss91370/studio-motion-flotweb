# Ombres chinoises

## 1. Identité

- **Nom** : Ombres chinoises (théâtre d'ombres en cuir teinté).
- **Inspiration** : les films de silhouettes découpées des années 1920 (jeu de profil, décors en dentelle) et le théâtre d'ombres du nord de la Chine (ciselure, couleur, rythme de gongs et de tambours). On ne reproduit jamais une marionnette historique, une mélodie ou un enregistrement.
- **Ce que c'est** : un écran de toile blanche ; derrière, des marionnettes plates en **cuir translucide teinté**, éclairées par une **lampe à huile**. La couleur arrive **par transparence** : les teintures brillent comme un vitrail, **les trous ciselés sont ce qu'il y a de plus clair**, les superpositions foncent. Les marionnettes sont articulées par des **rivets de fil visibles** et mues par de **fines tiges** qui se voient en lignes grises. C'est du théâtre vivant : l'écran **vacille avec la flamme**, les marionnettes **tremblent dans la main**, les pièces libres **se balancent sur leurs rivets**.
- **Marche pour** : conte, légende, fable morale, histoire d'une marque « racontée au coin du feu », lumières d'une ville, « qui tire les ficelles », spectacle.
- **Ne marche pas pour** : produit réel à montrer, texte long, sujet moderne et froid, visages expressifs (un visage de marionnette ne change jamais).
- **À ne pas confondre** : pas un film de silhouettes noires (la couleur est le second héros) ; pas du papier découpé (ici la lumière **traverse**) ; pas un vitrail (pas de plombs ; les pièces bougent et se chevauchent).

## 2. Palette, typographie, matières

| Rôle | Hex (carte huashu) |
|---|---|
| Écran, du centre de la lampe vers les bords | `#fff6d6` → `#f2d7a0` → `#cf9a58` → `#7a4a20` |
| Teintures | rouge `#c0352a`, vert `#2f7d4c`, ambre `#d99a2e`, jaune `#e2bd4a`, bleu `#2c5a8a`, orange `#d9782a` |
| Contour ciselé, tiges | brun profond `#3a160a` |
| Cuir brut (le neutre) | beige translucide `#e6cf9c` |

- **3 à 5 teintures saturées + le cuir brut + l'encre** (contours, cheveux, bottes). Toute couleur est **transmise** : rien n'est plus clair que la lampe, toute teinte tire vers le chaud.
- **La luminosité vient du nombre de lampes**, pas de l'étalonnage. La nuit = moins de lampes, jamais du bleu ajouté.
- Les choses fines qui doivent se lire (fils, hampes, texte) sont **sombres** : une pièce pâle disparaît sur l'écran clair.
- Jeux d'exemple : *cour* (vermillon, ocre, vert malachite) ; *rivière* (indigo, jade, un ocre) ; *moisson* (orange flamme, or, un vert).
- **Typographie** : sous-titres sur une **pancarte de conteur** : planchette de laque sombre, filet d'or, petit sceau ciselé ; serif classique (**Cormorant Garamond 600**, OFL), crème sur sombre. **Les titres sont des marionnettes** : plaques de cuir sombre aux lettres découpées (les mots brillent), bordure ciselée, portées par des tiges.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de Cormorant Garamond. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/cormorant-garamond` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** :
  - *Toile* : tissage procédural, mouchetis de fibres, taches de densité, bords plus sombres près du cadre.
  - *Ciselure = densité* : on laisse de fines bandes, on enlève la plus grande partie de la surface. Vocabulaire : rangées de croissants (écailles, tuiles), treillis de losanges, trous « pièce de monnaie », volutes de nuages, fentes effilées (fissures, pluie, poils), petits points, rosaces à cinq pétales. Contour sombre ciselé (2 à 3,5 px) autour de chaque région.
  - *Personnages* : 8 à 12 pièces, tête ≈ 1,2 × la taille naturelle avec une grande coiffe, manches d'une autre teinture que le torse, lobes ronds aux articulations avec rivet (anneau sombre + nœud pâle). Les personnages sympathiques ont un **visage ajouré** (les traits sont de fines bandes autour d'un trou) ; les antagonistes un visage plein.
  - **Tout ce qui est blanc dans le sujet devient un évidement** cerné d'une bordure de cuir (un plastron blanc, des pattes blanches) : la règle vaut pour tous les styles de silhouette.
  - *Décor* : pièces ciselées sur une toile surtout vide. Feu, fumée et eau sont des **pièces ciselées sur tiges**, échangées et secouées, jamais des particules.

## 3. Composition 9:16

- L'écran de toile occupe tout le cadre vertical, ou s'inscrit dans un **cadre de bois laqué** (linteau en haut vers y 160 à 240, montants sur les côtés). **La lampe est derrière la toile**, vers le centre haut (x 540, y 700) : c'est le point le plus clair ; les bords tombent dans le brun chaud.
- **Bande de sol ciselée étroite** vers y ≈ 1380 ; les marionnettes y posent les pieds. Sous cette bande : la pancarte du conteur (y 1400 à 1540).
- Personnages **de profil**, un ou deux par plan en vertical, ≥ 1/3 de la hauteur ; la plus grande partie de la toile reste vide.
- Tiges : elles partent de la nuque et des mains **vers le bas et l'extérieur**, sans croiser un autre personnage.
- Texte de pancarte 46 à 54 px ; plaques de titre 110 à 160 px de haut de lettre, dans le tiers haut. Rien d'important à droite de x = 945.
- En zoom, borne la caméra au rectangle de l'écran (pas de bandes noires).

## 4. Ce qui bouge

- **Action principale** : phrasé d'opéra : course à petits pas → saut → accroupi → **pose figée sur un accent de percussion** (≈ 1 s, seules les pièces libres frémissent) → tour de tête. Les visages ne changent jamais : l'attitude = angle de la tête + inclinaison du corps (levée = résolution, baissée = chagrin).
- **Boucle de fond 1** : **la flamme** : chaque lampe a un large lobe et un point chaud (≈ 6 pour 1) qui vacillent séparément (quelques % de bruit à ≈ 7 Hz) ; le centre de lumière dérive de quelques dizaines de pixels.
- **Boucle de fond 2** : **la main du montreur** : tremblement de chaque marionnette (quelques pixels, ≈ 0,02 rad, lent), plus fort sous tension ; jambes, plumets, glands, queue en segments simulés comme des pendules entraînés par l'accélération du corps (chaque segment en retard sur le précédent).
- **Gestes natifs** : la lumière est le monde (le nombre de lampes fait la chaleur) ; **loin de la toile = grand et flou** (une pièce tirée vers la lampe grossit et se floute ; les entrées arrivent grandes et floues et claquent nettes en ≈ 0,5 s, les sorties grossissent et s'effacent en ≈ 1 s) ; passer derrière l'écran (lampe, mains, tiges) ; l'échange de pièce ; la bande de décor qu'on soulève.
- **Autorisés** : `#027` avancée à travers le cadre vers la toile, `#025` panoramique sur une toile large, `#174` suivi d'une marionnette, `#028`/zoom éclair de quelques images sur un coup de tambour, `#043` panoramique filé le long d'une pièce en mouvement, `#175` plan large fixe, `#040` pose figée, `#124` tremblement continu, `#122` suivi des pièces libres.
- **Interdits** : `#044` fondu générique, `#045` volet numérique, `#012` métamorphose, `#011` écrasement, particules, changement d'expression, toile ou cadre qui bougent, bleu pour la nuit.

## 5. Rythme et montage

- Marionnettes et caméra **fluides** à 30 i/s ; seules les pièces d'effet échangées (feu, eau) changent par paliers (15 par seconde à 30 i/s). (La carte huashu fait jouer les gestes à 10 par seconde : variante plus « artisanale », à tester.)
- Le montage suit la percussion : un coup = une pose, un pas ou une coupe.
- Transitions : lampes qu'on baisse, un pilier flou de premier plan qui passe, une pièce qui se décolle dans la lumière, un éclair blanc chaud.
- Un arrêt net (tout coupé, queues de son comprises) avant le coup décisif.
- **Version courte (8 à 12 s)** : une seule phrase d'opéra (course, saut, pose figée 1 s, tour de tête) et la pancarte tenue 2 s ; couper l'allumage lent de la lampe et le second personnage. Accroche avant 3 s : la marionnette entre en courant dès la première seconde.

## 6. Recette technique

- **Moteur** : HyperFrames ; canvas 2D pour ciseler les pièces, passe WebGL pour la lumière. Lourd (≈ 120 ms par image si chaque pièce a son calque) : mets en cache tout ce qui est fixe.
- **Modèle de rendu**, par pixel : `image = courbe( lumièreDesLampes × transmissionDuCuir × toile )`.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `ciseler.js` (pièces, découpes, bibliothèque de motifs, texture de cuir, rivets), `lumiere.glsl` (lampes × transmission × toile, vue miroir, halo, fondu chaud), `scene.js` (cadre, spectateurs, plaques de titre), `coulisses.js` (silhouettes à liseré chaud, flamme, fumée), `rig.js` (articulations, bras à deux segments, pendules).
- **Techniques clés** :
  ```js
  // transmission : un canvas BLANC ; chaque pièce est posée en multiplication
  T.fillStyle = "#fff"; T.fillRect(0, 0, W, H);
  T.globalCompositeOperation = "multiply";
  // une pièce : aplat, découpes en "destination-out" (fillStyle noir opaque d'abord !),
  // bordure de la même teinte pour que la ciselure ne perce pas le contour, puis trait brun
  // pose sur la toile : d'abord une ombre douce décalée (pièce pas tout à fait plaquée)
  T.filter = "blur(6px)"; T.globalAlpha = 0.28; T.drawImage(piece, 7, 5);
  T.filter = "none"; T.globalAlpha = 1; T.drawImage(piece, 0, 0);
  ```
  ```glsl
  vec3 img = 1.0 - exp(-lampes * transmission * toile);   // l'exposition baisse en 1/sqrt(nombre de lampes)
  ```
- **Pièges** :
  - Aspect « clip-art » plat : texture de cuir, ciselure plus dense, teintures plus profondes, contours ciselés partout.
  - Figure illisible de profil : tête plus grosse, bas du corps plus plein, col, manches contrastées.
  - **Rouge × vert ≈ noir** : la superposition fonce, c'est juste, mais pas au point d'intérêt de l'image ; écarte les pièces.
  - Formes rayonnantes = lames de scie ou pétales : flammes à base épaisse, ventre et pointe crochue.
  - Coins gris en surexposition : vignettage **chaud** (vers le brun).
  - Fumée en mode additif : invisible sur la toile claire ; volutes sombres.
  - Avancée centrée sur une lampe de bord : les figures sortent du cadre ; avance sur le centre.
  - Tiges qui traversent le sujet : fouillis.

## 7. Son

- **Les percussions d'abord, pas piano et cordes** : tambour grave, tambour aigu et sec (ou woodblock), cymbales, petit gong qui monte, grand gong qui descend ; claquoir de bambou, luth à trois cordes pincé, flûte de bambou pour le calme. Une vièle nasillarde à deux cordes pour le chant ; un hautbois strident **une seule fois** au plus.
- **Techniques** : un seul coup dans un silence ; un grand gong par coup décisif ; tambour-battement de cœur sous l'angoisse ; roulement qui accélère avant une entrée ; un coup par étape visuelle.
- **Bruitages** (≈ 5 par 10 s) : claquoir de bois du conteur, allumette, lampe qui s'allume (« fwoump ») ou qu'on souffle, tiges qui tapent la toile, cuir sec qui claque au décollage, pas de cuir, froissement de tissu, ton de coulisses.
- **Voix** : un conteur, quelques phrases courtes, réverbération de petite salle ; nettement au-dessus du reste. Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défauts connus de la carte huashu (trois étoiles) : zones superposées trop noires, rendu lent. Erreurs : silhouettes noires ; pièces non ciselées ; nuit bleue ; particules ; expressions qui changent.

- [ ] La couleur traverse : les trous sont les points les plus clairs, les chevauchements plus sombres.
- [ ] Chaque pièce est ciselée (au moins deux motifs) et cernée d'un contour sombre.
- [ ] Rivets et tiges visibles ; les tiges ne croisent pas un autre personnage.
- [ ] L'écran vacille ; les marionnettes tremblent ; les pièces libres pendulent.
- [ ] Au moins une pose figée sur un accent de percussion.
- [ ] Une entrée « grande et floue qui claque nette ».
- [ ] La nuit est faite avec moins de lampes, pas avec du bleu.
- [ ] Pancarte et plaques dans le style ; rien d'important sous y = 1560 ni à droite de x = 945.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 12
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Film de démo d'origine (54 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/shadow-puppet.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/shadow-puppet.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/shadow-puppet.jpg · galerie : https://lemomo-ai.github.io/lemo-opuscar/#east-asian-traditions
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre la légende, les marionnettes ni les plans.
- Carte huashu : pas d'aperçu isolé (planche commune `assets/全风格总览.jpg`, à ne pas utiliser comme vitrine).

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/shadow-puppet/STYLE.md`, `DEMO.md`, `demo/carve.js`, `gl.js`, `stage.js`, `backstage.js`, `scenery.js`, `hud.js`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0.
- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/34_shadowpuppet.md` (trois étoiles), `scripts/engine/scenes/34_shadowpuppet.js` : fonction de pièce (bordure qui protège le contour), ombre douce décalée, teintures en hex, règle « le blanc devient un évidement », queue en segments retardés. Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : fiche fusionnée et traduite, section 9:16, numéros du dictionnaire de mouvements, budget de bruitages.
