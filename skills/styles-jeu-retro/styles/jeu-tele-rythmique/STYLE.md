# Jeu télé rythmique

## 1. Identité

- **Nom** : Jeu télé rythmique.
- **Inspiration** : les jeux de rythme en mini-épreuves (un signal, une réponse, un carton de manche, un mot de verdict) et les habillages d'émissions de variétés japonaises (gros sous-titres à contour épais, décors à rayures et à soleils). On reprend la grammaire, jamais les noms, personnages, interfaces, niveaux ou musiques.
- **Ce que c'est** :
  - **Tout est sur la grille.** Un tempo fixe et rapide. Chaque apparition, chute, tampon, caractère tapé et coup de caméra est placé à (mesure, temps) et est aussi un évènement sonore : la musique est générée depuis la timeline de l'image, elles ne peuvent pas dériver.
  - **Un seul kit de dessin, plusieurs décors.** Aplats, un gros contour d'encre, bouts ronds, ombres dures décalées ; chaque manche a une nouvelle couleur de fond saturée et un nouveau motif.
  - **Les personnages sont des jouets** : un seul corps pour toute la distribution, distingués par la couleur, une tache sur le ventre, un accessoire de tête et une étiquette de nom.
  - **Une manche = un verbe répétable + une victoire** lue d'un coup d'œil.
- **Marche pour** : bilan d'année, classement, étapes d'une recette ou d'un parcours, progression d'une collecte, comparaison de concurrents (sans leurs logos), présentation d'une équipe, quiz.
- **Ne marche pas pour** : émotion, récit avec des personnages qui jouent, explication fine, marque sobre. Ce n'est ni des micro-jeux en rafale (pas de chrono, pas de changement de style par manche), ni un cartoon années 50, ni une présentation de lancement (rien de lent, aucun dégradé).
- La narration est facultative : le style tient sur des cris courts et des textes à l'écran.

## 2. Palette, typographie, matières

| Rôle | Hex |
|---|---|
| Encre / blanc / crème (cartes) | `#1B1B1B` · `#FFFFFF` · `#FFF6E5` |
| Bonbons | jaune `#FFD23F` · orange `#FF8C42` · rouge `#FF5A5F` · rose `#FF8FB1` · vert `#5BD68A` · citron vert `#C6F16D` · ciel `#8ED1FC` · bleu `#4D7CFE` |
| Décors profonds (nuit, final) | sarcelle `#3FB8AF` / `#2B8F88` · marine `#26264A` · (violet `#6B4FBB` / `#46318F` : à éviter ou à garder très court, interdit bleu-violet) |
| Accessoires | bois `#C98A52` · gris `#C3CAD9` · peau `#FFD1A8` |

- **Un décor = une teinte** : fond, motif (un cran plus clair) et carton de manche partagent la teinte. Deux manches voisines ne partagent jamais la même. Exemple : fond mandarine `#FFB870` à rayures `#FFA85A`.
- **Chaque personnage possède sa couleur**, qui ne change jamais et diffère du décor où il se tient.
- **Motifs** : rayures diagonales (qui défilent lentement), pois décalés (≈ 20 % de blanc), soleil tournant. Une bande de sol plus foncée avec un trait d'encre ancre les personnages.
- **Typographie** (OFL) : **Fredoka 700** pour tout ; une police manuscrite seulement pour les accessoires écrits à la main. Texte blanc ou jaune avec **contour d'encre ≈ 14 % de la taille, peint sous le remplissage** (`paint-order: stroke`).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Fredoka. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/fredoka` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : aucune. Pas de dégradé, de flou, de texture, d'ombre douce. La profondeur est une **ombre dure décalée** : la même forme en encre, décalée de ≈ 10 px (autocollants, bandeaux) à ≈ 14 px (cartes).
- Contours : 8 px sur personnages et accessoires, 5 à 7 px sur les petites pièces.

## 3. Composition 9:16

- Scène frontale et symétrique, comme un plateau vu de face. En vertical : **sol vers y 1300**, personnages-jouets de 300 à 420 px de haut sur la bande de sol, 3 de front au maximum (les foules s'empilent sur 2 ou 3 rangées).
- **Bandeau de manche** en haut à gauche (y 180 à 320), **mot de verdict** au centre haut (y 380 à 640, 160 à 220 px, incliné), **tableau des scores** entre les deux ou en colonne à gauche.
- **Les textes à l'écran sont les sous-titres** : cartons, bandeaux, étiquettes, verdicts. Garde-les courts : ≤ 14 caractères par ligne de bandeau à 72 px. Avec narration : plaques en bas (y 1400 à 1540) dans la même typographie à contour, jamais une légende fine générique.
- Le vertical convient au **défilement du sol vers le ciel** (classement, tour d'objets, croissance).
- Scène coupée en deux : en 9:16, **haut / bas** plutôt que gauche / droite.
- 16:9 : format d'origine, jusqu'à 6 personnages de front.

## 4. Ce qui bouge

- **Action principale** : le verbe de la manche, répété sur le temps (signal → réponse), jusqu'au verdict.
- **Boucle de fond 1** : **repos = petit saut sur le temps** (une parabole par temps, 8 à 30 px) ; les voisins sautent à contretemps, la foule ondule.
- **Boucle de fond 2** : rayures qui défilent ou soleil qui tourne ; petit écrasement sur chaque premier temps.
- **Autorisés** : `#001` apparition avec rebond (cartes, autocollants, tampons, mots), `#123` rebond, `#011` écrasement à l'impact (oscillation amortie ≈ 0,35 s), `#002` entrées en cascade (une par temps ou demi-temps), `#006` texte tapé sur des fractions de temps, `#007` compteur qui monte, `#125` pulsation, `#003` éclat (étoile + anneau + traits), `#046` coupe sèche sur la barre de mesure, `#144` scène partagée, `#028` zoom sec sur un accessoire.
- **Interdits** : `#044` fondu enchaîné, apparition lente en fondu (les choses sont là ou elles surgissent), dégradés, flou, `#016` parallaxe, mouvement hors grille, jeu d'acteur nuancé.
- **Coup de caméra sur le temps** : zoom de 0,8 à 5 % autour du centre, qui retombe en ≈ 0,16 s. Somme des coups simultanés < 6 %, sinon le bord de l'image apparaît.
- Entrées : chute du ciel, accélérée, qui atterrit pile sur son temps. Pose de cri : bras levés + bouche ouverte, un demi-temps.

## 5. Rythme et montage

- **Tempo fixe** où un temps est un nombre entier d'images : à 30 i/s, 150 BPM (12 images) ou 120 BPM (15 images).
- **Structure en manches** : carton d'une mesure (numéro + nom + une étiquette), jingle, puis les mesures de jeu. La durée du film suit le nombre de manches : 3 manches ≈ 25 à 40 s.
- Changements de scène : **coupes sèches sur les barres de mesure**, avec un flash blanc très court. Un fondu, à la rigueur, tout à la fin.
- Accélérer le motif (noires → croches) **est** l'intrigue.
- Variations d'intensité : batterie seule une mesure avant un gros coup, une mesure de silence brisée par un seul cri, final transposé plus haut.
- Chaque texte tient ≥ max(1,8 s ; voix + 0,6 s) ; un mot de verdict peut être plus court.
- **Version courte (8 à 12 s)** : une seule manche : carton d'une mesure, trois mesures de jeu, verdict tenu 1 s ; couper le jingle et le tableau des scores.

## 6. Recette technique

- **Moteur** : HyperFrames, en SVG ou canvas ; c'est le style le plus naturel pour une timeline GSAP.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `grille.js` (`a(mesure, temps)` → secondes ; `evenement()` pour le son), `kit.js` (contour, ombre dure, motifs, éclat, verdict, bandeau, carton), `persos.js` (corps-haricot + poses), `scenes.js` (`scene(t0, t1, construire)`), `evenements.json` (exporté pour la musique et les bruitages).
- **Techniques clés** :
  ```js
  const BPM = 150, T = 60 / BPM;                 // 12 images à 30 i/s
  const a = (mesure, temps) => ((mesure - 1) * 4 + (temps - 1)) * T;
  const saut = (t) => { const u = (t / T) % 1; return -24 * 4 * u * (1 - u); };
  tl.from(".carton", { scale: 0, duration: 0.25, ease: "back.out(2.2)" }, a(3, 1));
  ```
  - Contrat : une scène construit ses éléments une fois ; la mise à jour ne fait que **poser des attributs calculés depuis `t`**, jamais depuis l'image précédente (sinon un rendu en parallèle démarre faux).
  - Flashs de coupe, jingles et arrangement viennent **d'une seule table**.
  - Charge les polices **avant** de mesurer les textes, sinon ils débordent des plaques.
  - Titres construits lettre par lettre pour que chaque caractère puisse surgir.
- **Pièges** : état conservé d'une image à l'autre ; listes d'évènements écrites à la main qui dérivent ; chiffres et symboles mal lus par la voix de synthèse (écris-les en lettres) ; **produits réels en personnages** : noms sur des étiquettes, mascottes originales, **aucun logo ni interface réelle** ; personnes réelles seulement en silhouettes génériques.

## 7. Son

- **Tout part des évènements de l'image.** Musique pop majeure sur une courte boucle d'accords, un accord par mesure ; chaque manche a sa couleur (funk, quiz, électro, rêve…), pas une nouvelle chanson.
- **Bruitages-jouets accordés** (un par évènement important, ≈ 5 par 10 s après tri) : pop, « plop + boing » d'atterrissage, tampon, clic de machine à écrire, buzzer, ding. Des bips accordés peuvent épeler une mélodie quand une foule tombe.
- **Des cris, pas des phrases** : un à trois mots (« Hé ! », un nombre, un verdict), placés 20 à 30 ms **avant** le temps pour que la consonne tombe dessus. Cri de foule : plusieurs voix différentes décalées de quelques millisecondes et réparties en stéréo.
- Mix : voix et bruitages sur leur propre groupe, la musique baisse sous eux ; −14 LUFS, crête ≤ −1 dB.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : évènement hors grille, dégradés ou ombres douces, texte long, logos réels, apparitions en fondu, deux manches de la même couleur.

- [ ] Chaque apparition, chute et tampon tombe sur un temps ou une subdivision (vérifié image par image sur 3 évènements).
- [ ] Aucun dégradé, flou ou ombre douce ; toutes les ombres sont dures et décalées.
- [ ] Contour d'encre partout ; texte avec contour sous le remplissage.
- [ ] Les personnages au repos sautillent sur le temps, à contretemps de leurs voisins.
- [ ] Deux manches voisines ont des teintes différentes ; aucun personnage sur un fond de sa couleur.
- [ ] Chaque manche finit par un mot de verdict lisible en une seconde.
- [ ] Changements de scène en coupe sèche sur la barre de mesure.
- [ ] Aucun logo, interface ou personnage réels.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 21
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Film de démo d'origine *Rhythm of AI, 1997 → 2026* (149 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/game-show.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/game-show.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. **Cette démo met en scène des produits et sociétés tiers** : à consulter pour comprendre le style, à ne pas afficher sur une page de vente.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/game-show/STYLE.md`, `DEMO.md`, `demo/frame_head.html`, `main_v1.js`, `main_b.js`, `music.py`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Police Fredoka (SIL OFL 1.1).
- Adaptation Flot Web : traduction, mise en page 9:16, tempos à 30 i/s, extrait GSAP, numéros du dictionnaire ; les couleurs de personnages liées à des marques dans la démo ne sont pas reprises.
