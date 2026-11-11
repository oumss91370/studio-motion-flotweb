# Tableau blanc

## 1. Identité

- **Nom** : Tableau blanc (« Whiteboard Explainer »).
- **Inspiration** : les conférences dessinées sur un seul grand tableau où la caméra voyage au lieu de couper, les chaînes de vulgarisation « une phrase = un dessin, la géométrie la plus simple qui porte l'idée », la musique répétitive à deux tempos comme structure. On emprunte la grammaire, jamais un dessin, un personnage, une main ou une musique.
- **Ce que c'est** : **un vrai tableau blanc brillant**. Tout ce que le spectateur apprend est dessiné au feutre effaçable devant lui, dans l'ordre réel de l'écriture. **Le tableau est une carte** : chaque idée a sa région ; la caméra voyage de l'une à l'autre, souvent menée par le feutre. La distance sur le tableau = la distance dans le raisonnement. **Pas de main** : les feutres flottent avec une vraie ombre portée, se garent hors cadre entre deux phrases et reviennent. Aimants et effaceur bougent seuls.
- **Marche pour** : « comment ça marche », science, finance personnelle, processus, comparaison de deux options, résumé d'un sujet en une image.
- **Ne marche pas pour** : émotion pure, produit à montrer en photo, humour visuel de personnages, vidéo sans voix.
- **À ne pas confondre** : pas un plan d'architecte bleu ; pas de la craie grasse ; pas de la typo animée (le texte est écrit trait par trait, jamais animé par blocs). Le tableau noir (`tableau-noir-craie`) traite **une** idée sur une ardoise propre ; ici on relie plusieurs idées sur une grande surface.

## 2. Palette, typographie, matières

- **Trois couleurs de feutre au maximum**, chacune avec un sens tenu tout le film : une encre sombre pour les choses et la structure, une pour les signaux, mesures et processus, un accent pour ce qui compte (un accent par région).
- Jeux d'exemple : noir `#23262c` / bleu `#2a5cb3` / rouge `#c8363a` ; noir / vert `#2e8b57` / rouge `#c8363a` ; marine `#1f2a44` / sarcelle `#1f8a8a` / violet `#7a4fb3`. Tableau : blanc chaud `#f7f6f2` à `#eceae4`. Variante monochrome : tout à l'encre sombre, un seul élément en accent.
- **Typographie** (OFL) : écriture **monoligne** (police à trait unique, par exemple la famille EMS) pour tout le texte du tableau ; sous-titres en **Architects Daughter**.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place d'Architects Daughter. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/architects-daughter` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La famille EMS (trait unique) n'a pas de paquet `@fontsource` : à vérifier ; à défaut, tracer les lettres par le moteur de trait.
- **Matières** :
  - *Tableau* : dégradé blanc chaud, fines rayures, quelques dizaines de **fantômes** (anciens mots, cercles, flèches) à 5-10 % en gris ou bleu pâle, et un **reflet de fenêtre** diagonal (blanc, 10-16 %) qui se déplace à ≈ 0,35 × la caméra : ce seul détail vend le « brillant ».
  - *Encre* : opacité ≈ 0,94, composée en **multiplication** pour que les croisements foncent. Épaisseur 8 à 14 px pour le dessin en 1080 de large, ≈ 13 % de la hauteur de capitale pour le lettrage.
  - *Caractère du trait* : tremblé lent le long de la normale, pointe biseautée (largeur selon la direction), appui au départ, petit effilé à la fin ; les cercles **dépassent leur fermeture** ; les rectangles sont quatre traits qui débordent un peu aux coins ; un point d'encre plus sombre **à l'intérieur** du départ des longs traits.
  - *Feutre sec* : une texture de mouchetis et de stries soustraite de l'encre, fixée au tableau.
  - *Accessoires* : feutres (corps blanc, bague et capuchon de la couleur de l'encre), effaceur en feutrine, aimants brillants avec reflet et ombre douce.

## 3. Composition 9:16

- Le tableau est bien plus grand que le cadre (par exemple 4500 × 8000 unités, en hauteur). En vertical, **empile les régions de haut en bas** ou en lacets ; chaque région tient dans un cadre 1080×1920 avec sa marge.
- **Bas du cadre réservé aux sous-titres dans chaque plan** : rien à lire sur le tableau sous y = 1340.
- Titres : hauteur de capitale 140 à 220 px ; étiquettes 44 à 80 px. Une étiquette est **entièrement dans le cadre ou entièrement dehors**, jamais coupée.
- **Sous-titres incrustés** : étiquette arrondie blanc cassé (≈ 90 %), Architects Daughter ≈ 50 px, texte sombre, un petit tiret de feutre dans la couleur d'accent ; coupés aux propositions, ≤ 30 caractères par ligne en vertical, vers y ≈ 1400 à 1520. Tenue ≥ max(1,8 s ; réplique + 0,6 s).
- Titre et carton de fin sont écrits sur le tableau, de la même main.
- 16:9 : tableau 8000 × 4500, 44 caractères par ligne, 12 % du bas réservés.

## 4. Ce qui bouge

- **Action principale** : l'écriture dans l'ordre des traits ; **un terme finit de s'écrire exactement quand la voix le prononce**.
- **Boucle de fond 1** : les feutres qui sautent d'un trait à l'autre (ils se soulèvent en proportion de la distance, l'ombre glisse et se floute) et vont se garer hors cadre.
- **Boucle de fond 2** : le reflet de fenêtre qui dérive plus lentement que le tableau.
- **Gestes natifs** : le feutre mène la caméra ; **les aimants** (les seules choses qui ont le droit de bouger sur un tableau : confie le héros à un aimant) ; **l'effaceur remonte le temps** (il laisse toujours un fantôme, à ≈ 90 % de force) ; deux feutres à la fois pour comparer ; les fantômes d'une ancienne leçon ; la vue du tableau entier.
- **Autorisés** : `#004` tracé de ligne, `#006` texte tracé caractère par caractère (ici trait par trait), `#126` trajet (aimant), `#027` avancée lente vers un symbole, `#029` travelling le long d'un schéma, `#043` panoramique filé vers une nouvelle région (c'est la seule « coupe »), `#175` plan fixe pour lire, `#183` plan d'ensemble final.
- **Interdits** : `#001` apparition en rebond d'un bloc, `#008` typo cinétique, `#044` fondu, `#041` coupe sur le tableau, toute main, tout bras, tout curseur.
- Vitesse de la main : chaque trait est lent-rapide-lent. Plus rapide qu'une vraie main, jamais au point de perdre l'ordre des traits : une étiquette ≈ 0,3 à 0,8 s, un titre ≈ 3 s.

## 5. Rythme et montage

- La durée suit le nombre d'idées : compte 6 à 10 s par région. Pour un Short, 3 à 4 régions.
- **Chaque dessin a une échéance** : on fixe la fenêtre de temps, le moteur en déduit la vitesse, l'écriture finit toujours à l'heure.
- Transitions : la caméra suit la ligne que le feutre trace vers la région suivante ; panoramique filé avec flou de mouvement (quand la caméra bouge de plus de ≈ 14 px par image) ; retour sur une région déjà vue (un rappel gratuit).
- Un arrêt complet dans le silence avant une surprise.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D, `renderAt(t)`.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `feutre.js` (formes dessinées à la main : ligne, courbe, arc, cercle, rectangle, flèche, pointillés, hachures ; texte en ordre d'écriture depuis une police monoligne), `timeline.js` (planifie un dessin jusqu'à une échéance, effacements, repères), `camera.js`, `tableau.js` (encre en multiplication, texture sèche, effaceurs, reflet, accessoires).
- **Techniques clés** :
  ```js
  const u = (t - t0) / (t1 - t0);                                  // avancement d'un trait
  const p = u - 0.8 * Math.sin(2 * Math.PI * u) / (2 * Math.PI);   // main : lent, rapide, lent
  ctx.globalCompositeOperation = "multiply";                       // les croisements foncent
  const zoom = 1 / mix(1 / z0, 1 / z1, e);                         // zoom interpolé en 1/z : l'avancée ressemble à un travelling
  ```
  - Symboles absents de la police (μ ≈ → × − ✓ ² ° ±) : dessine-les comme des traits.
  - Flou de mouvement : rends et moyenne des sous-images espacées de ≤ 4 px.
- **Pièges** :
  - **Un seul feutre pour trop de tâches** prend du retard : donne une échéance à chaque dessin et confie les tâches qui se chevauchent à un autre feutre.
  - Une ligne pointillée met des secondes si chaque tiret a une durée minimale : les tirets ont leur propre plancher.
  - Un point d'encre plus gros que le départ du trait fait des halos sur chaque lettre.
  - La ponctuation disparaît (un point de police = un trait de 1 px) : rends les traits minuscules comme des points.
  - Une avancée qui coupe une étiquette en deux fait négligé.
  - Un trajet d'effaceur qui traverse une étiquette à garder.

## 7. Son

- **Chaque trait a un son**, mais on ne mixe pas tout au même niveau : un frottement de feutre sur surface brillante dont l'enveloppe suit la vitesse du trait, un petit tic au départ, et sur quelques longs traits le **couinement** du feutre. Traite l'écriture comme une texture continue et basse, et garde le budget (≈ 5 par 10 s) pour les événements : aimant sur l'acier (clic + choc sourd du tableau), effaceur, capuchon, signal.
- **Pièce** : ton de salle très bas ; un seul objet sonore (horloge, ventilateur) peut habiter un silence.
- **Musique** (au choix) : motif de piano seul ; petit trio avec balais ; cordes pincées et kalimba ; arpège de synthé pour un sujet technique ; minimalisme d'horloger (marimba, pizzicato, woodblock, glockenspiel). Techniques : un instrument de plus par étape d'un mécanisme ; arrêt complet avant la surprise ; deux copies d'un motif à deux tempos pour ce qui diverge, qui se rejoignent à la résolution.
- **Voix** au-dessus de tout, musique nettement dessous, bruitages ≈ 11 dB sous la voix. Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : texte qui apparaît d'un bloc ; une main ; plus de trois couleurs ; trait parfait de logiciel ; tableau mat sans reflet ; étiquettes coupées ; écriture en retard sur la voix.

- [ ] Tout le texte est écrit trait par trait dans l'ordre d'écriture.
- [ ] Trois couleurs de feutre au plus ; l'accent a le même sens du début à la fin.
- [ ] Les croisements de traits sont plus sombres ; les cercles dépassent leur fermeture.
- [ ] Le reflet de fenêtre bouge plus lentement que le tableau.
- [ ] Aucune main, aucun curseur ; les feutres ont une ombre qui grandit quand ils se lèvent.
- [ ] Chaque terme finit de s'écrire sur le mot prononcé (±0,2 s).
- [ ] Aucune étiquette coupée par le cadre ; rien à lire sous y = 1340 ni à droite de x = 945.
- [ ] Une vue d'ensemble du tableau au moins une fois.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 9
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 44

## 9. Aperçu

- Film de démo d'origine (111 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/whiteboard.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/whiteboard.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/whiteboard.jpg
- Galerie : https://lemomo-ai.github.io/lemo-opuscar/#hand-drawn-painting
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. Le titre de la démo cite un physicien célèbre : à montrer comme exemple de style avec le crédit, pas comme visuel promotionnel de l'offre.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/whiteboard/STYLE.md`, `DEMO.md`, `demo/engine/wb.js`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0.
- La carte « tableau blanc » de huashu-art-motion (grammaire explicative `y3_whiteboard`) est traitée dans la catégorie `styles-explicatif-infographie`.
- Adaptation Flot Web : traduction, mise en page verticale, budget de bruitages, numéros du dictionnaire de mouvements. L'orange d'accent de l'exemple d'origine a été remplacé par un rouge.
