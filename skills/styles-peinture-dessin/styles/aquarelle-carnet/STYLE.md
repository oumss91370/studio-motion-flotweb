# Aquarelle, carnet de naturaliste

## 1. Identité

- **Nom** : Aquarelle, carnet de naturaliste (« Watercolor Brush »).
- **Inspiration** : les carnets de terrain et planches botaniques (un spécimen + une note), les longs rouleaux peints (un seul monde continu), le schéma de « transect » des manuels (un dégradé lu dans l'espace). On emprunte la grammaire, jamais une œuvre, un personnage ou une mise en page.
- **Ce que c'est** : **une feuille de papier chaud et fibreux** sous tout le reste ; tout est fait de **coups de pinceau individuels** (un ruban de largeur variable à demi transparent, plus quelques traces de poils qui se brisent en tirets : la brosse sèche). Les touches se croisent et foncent là où elles se recouvrent. Aucun contour vectoriel. Les choses **se peignent toutes seules**, la structure avant le détail (tronc → branches → feuilles). Une couche d'annotations manuscrites : étiquettes avec un trait de plume, une valeur mesurée, un titre discret.
- **Ton** : calme, curieux, précis. Les chiffres sont vrais ; la palette peut porter une donnée.
- **Marche pour** : nature, jardin, cuisine et recettes, terroir, tourisme lent, étapes d'un processus, anatomie d'un objet, carte qui change dans le temps, artisan.
- **Ne marche pas pour** : sujet rapide ou comique, interface, promotion agressive, beaucoup de texte.
- **À ne pas confondre** : pas du lavis à l'encre (ici de la couleur, pas de geste calligraphique) ; pas de l'huile (aucune pâte) ; pas un album jeunesse ; pas du vectoriel avec une texture posée dessus.

## 2. Palette, typographie, matières

- **Le papier est le blanc.** On ne peint jamais de blanc pur : la lumière est du papier non peint.
- **Superposition transparente** : plus sombre = plus de passes, pas un pigment plus foncé par-dessus. 3 à 5 teintes par scène, plus l'encre.
- **Encre** (un presque noir chaud `#2b2420` et un brun plus clair `#6a5444`) pour les traits, le texte, les bords et les tiges seulement.
- **Un seul accent** (un vermillon, un bleu de pluie) réservé à un élément qui revient : un tampon, un repère, un objet clé.
- Exemples : *port à l'aube* : ciel `#f3e2c8`, eau `#9fb4c4`, coques `#5f7486`, accent bouées `#c8442a` ; *potager* : terre claire `#e8e0c0`, feuilles `#8ea860`, ombre `#4e6e3c`, accent citrouilles `#d9632e` ; *de l'aride à l'humide* : ocre rouge → sauge → paille → gris-bleu → vert profond.
- **La couleur peut porter la donnée** : ciel, sol et fond se mélangent selon une valeur mesurée. Une rampe découpée en 4 à 6 paliers se lit comme de la peinture ; une rampe continue se lit comme un logiciel.
- **Typographie** (OFL) : **Cormorant Garamond** pour les titres et sous-titres, **Caveat** pour les notes, **IBM Plex Mono** (interlettrage large) pour les petites valeurs mesurées.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de Cormorant Garamond ; Nunito à la place de Caveat ; IBM Plex Mono : déjà fournie. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/cormorant-garamond`, `@fontsource/caveat` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : papier pré-généré (base chaude, bruit doux ±3,5 %, quelques milliers de fibres courbes, grain fin, léger vignettage). *Touche* : ruban dont la largeur suit un profil (pinceau, feuille, régulier, pointe, tronc) avec ≈ ±22 % d'irrégularité, corps à ≈ 0,55-0,6 d'opacité, plus 3 à 9 traces de poils à 30-85 % d'opacité, chacune avec ses tirets et sa fin anticipée. *Lavis* : le même polygone peint en 3 passes aux sommets décalés, un tiers d'opacité chacune : les bords foncent là où les passes ne coïncident pas. *Profondeur* : plusieurs plans ; plus loin = plus petit, plus clair, moins saturé ; bandes de brume couleur papier entre les plans.

## 3. Composition 9:16

- Le monde est **une longue feuille** : en vertical, préfère une feuille haute qu'on descend (recette, strates, arbre du pied à la cime) ou une planche fixe où les choses se peignent. Le long travelling latéral de l'original devient un panoramique vertical ou un travelling plus court.
- Marges de papier généreuses : sujet entre x = 90 et x = 900. Un sujet héros par vue, avec sa note ; **une étiquette ne couvre jamais le sujet**.
- **Sous-titres posés sur le papier**, sans boîte : Cormorant Garamond italique 46 à 52 px, 2 lignes équilibrées au plus, encre à ≈ 78 % sur un halo couleur papier, centrés vers y ≈ 1420. Tenue ≥ max(1,8 s ; réplique + 0,6 s).
- Notes manuscrites : Caveat 44 à 56 px, à gauche ou au-dessus du sujet, jamais dans la bande droite (x > 945). Les nombres s'écrivent en chiffres à l'écran.
- 16:9 : long travelling latéral sur un monde continu, sous-titres centrés en bas.

## 4. Ce qui bouge

- **Action principale** : le **peint-en-direct**. La progression d'un objet dépend de sa place à l'écran ou d'un repère de la timeline ; chaque touche d'une liste prend une tranche de cette progression, donc la structure apparaît d'abord.
- **Boucle de fond 1** : balancement des objets **terminés** seulement : petite inclinaison horizontale, `sin(1,15·t + φ) + 0,4·sin(2,7·t + 2φ)`, amplitude ≈ 0,006 pour un arbre, 0,01 à 0,03 pour de l'herbe.
- **Boucle de fond 2** : brume couleur papier dont le bord ondule, et petites créatures du sujet (oiseau, insecte, goutte) calées sur la musique.
- **Autorisés** : `#004` tracé de ligne (traits de plume, étiquettes), `#005` révélation par masque (étiquette ouverte de gauche à droite), `#016` parallaxe entre plans peints, `#029` travelling latéral, `#026` panoramique vertical, `#027` avancée lente vers un détail, `#140` page qui tourne, `#039` passage du temps sur un plan fixe (saisons).
- **Interdits** : `#046` coupe sèche brutale, `#044` fondu enchaîné entre deux images sans rapport, `#024` secousse d'impact, `#136` trait qui frémit (rien ne tremble ici), `#023` glitch, tout contour vectoriel.
- Courbes douces (accélération et décélération lissées). Rien ne saccade : ici tout est fluide.

## 5. Rythme et montage

- Lent et continu : plans de 6 à 12 s, très peu de coupes. Une rafale (« tout un groupe se peint en moins d'une seconde ») marque le pic.
- Transitions du style : **volet au bord de pinceau** (un bord vertical ondulé révèle la scène), **brume** qui lave tout jusqu'au papier, page qui tourne, mouvement de caméra continu.
- Un silence « pinceau levé » : la musique sort, il ne reste que le papier et la pièce, autour d'un seul moment peint.
- Si la musique est remontée, recalcule les animations calées sur ses temps.
- **Version courte (8 à 12 s)** : un seul plan : le volet au bord de pinceau (1 s), la scène se peint, la « rafale » (un groupe peint en moins d'une seconde) placée avant 3 s en guise d'accroche, une note manuscrite tenue 2 s.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D, `renderAt(t)` (voir le `SKILL.md` de la catégorie).
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `moteur.js` (hasard à graine, bruit, touches, lavis, mise en cache), `sujets.js` (générateurs de plantes et d'objets en coordonnées locales, racine en 0,0), `scene.js` (plans, bandes de lavis, placement, annotations), `main.js` (caméra, brume, sous-titres).
- **Techniques clés** :
  ```js
  // un lavis = 3 passes décalées : le bord fonce tout seul
  for (let i = 0; i < 3; i++) remplir(decaler(poly, 2.5, graine + i), couleur, alpha / 3);
  // un trait peint jusqu'à une fraction p de sa longueur (pointe du pinceau qui avance)
  dessinerTouche(touche, { jusqua: p });
  // balancement d'un objet terminé
  const penche = 0.006 * (Math.sin(1.15 * t + phi) + 0.4 * Math.sin(2.7 * t + 2 * phi));
  ```
  - **Mets en cache les objets terminés** comme images ; ne dessine touche par touche que ce qui est en train d'être peint.
  - Toute touche créée pendant le rendu doit être construite sous une graine fixe.
- **Pièges** :
  - Bandes de lavis hors écran trop courtes : sommets aplatis et raccords visibles lors d'un panoramique vertical. Fais-les dépasser largement du cadre.
  - Un lavis translucide qui s'arrête au bord de son canvas montre une arête : prolonge-le sous le cadre et fonds-le vers la couleur papier.
  - Des milliers de touches par image : trop lent sans cache.
  - Une rampe de couleur continue fait « logiciel » : découpe en paliers.

## 7. Son

- **Musique** : acoustique et douce : piano feutré, guitare en arpèges, bois, cordes légères, glockenspiel, kalimba.
- **Bruitages** (≈ 5 par 10 s, faits de la matière de la scène) : un frôlement de pinceau sur papier pour chaque objet qui se peint, grattement de crayon pour les notes, petit choc mat pour un tampon, page tournée ; puis la nature du sujet (oiseaux, vent, pluie, eau, insectes).
- **Voix** : lecture documentaire chaleureuse et posée, une phrase par idée ; devant la musique de quelques décibels, musique baissée d'environ 4 dB sous la voix. Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : contours nets ; blanc peint ; texture d'aquarelle plaquée sur des aplats ; trop de teintes ; coupes rapides ; étiquette sur le sujet.

- [ ] Aucun contour vectoriel : la seule « ligne » est une touche plus sombre le long d'une forme.
- [ ] Le blanc de l'image est du papier nu.
- [ ] Les bords des lavis sont plus foncés que leur centre.
- [ ] La brosse sèche (tirets) se voit sur les longues touches.
- [ ] 3 à 5 teintes par scène, un seul accent.
- [ ] Les objets se peignent structure d'abord ; ils ne se balancent qu'une fois terminés.
- [ ] Chaque note a son trait de plume vers le sujet et ne le recouvre pas.
- [ ] Aucune coupe sèche ; au moins un volet au pinceau ou une brume.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 10
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 44

## 9. Aperçu

- Film de démo d'origine *Follow the Rain* (114 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/watercolor.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/watercolor.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/watercolor.jpg
- Galerie : https://lemomo-ai.github.io/lemo-opuscar/#hand-drawn-painting
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre l'histoire ni les plans.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/watercolor/STYLE.md`, `DEMO.md`, `demo/engine.js` (touches, lavis, cache), `plants.js`, `scene.js`, `main.js`, `paper.py`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0.
- Adaptation Flot Web : traduction, mise en page verticale, numéros du dictionnaire de mouvements, budget de bruitages, cadence 30 i/s (l'original recommande 60 i/s pour la fluidité du pinceau : à tester si le rendu saccade).
