# Keynote sombre

## 1. Identité

- **Nom** : Keynote sombre (film de lancement de logiciel sur scène noire).
- **Inspiration** : les présentations de produit sur scène noire (balayages de lumière, une phrase par écran, un chiffre géant seul), les vidéos de lancement d'outils pour développeurs (mouvement accroché à une grille, filets de 1 px, un seul accent), la musique répétitive à processus, les inserts très courts du cinéma de comédie. On n'en reprend ni nom, ni interface, ni police, ni commande système, ni mélodie, ni logo.
- **Ce qui le fait reconnaître** : il n'y a **pas d'objet physique** : le héros est **l'interface elle-même** (un curseur, des fenêtres, des notifications, des tuiles, un nombre), **entièrement dessinée en code**, sur une scène presque noire éclairée d'une lumière douce et froide, avec **un seul accent de marque** réservé à l'élément le plus important. Tout s'accroche à une grille ; tout mouvement arrive sur un temps ; tous les sons appartiennent à une même famille.
- **Le ressort dramatique** : le désordre montré comme une interface générée en masse, une action décisive, puis le vide.
- **Marche pour** : lancement d'un logiciel ou d'une application, annonce de fonction, ouverture d'une présentation, « avant c'était le chaos, maintenant c'est rangé ».
- **Ne marche pas pour** : montrer le vrai produit écran par écran (voir `keynote-produit` avec de vraies captures, ou `screencast-vivant`), un produit physique, une mauvaise nouvelle, un sujet non technique. Ce n'est pas un hologramme (pas de lignes de balayage) ni un film de graphiques (un nombre, pas un graphique).

## 2. Palette, typographie, matières

- **Une échelle de neutres froids** seulement : scène presque noire, trois niveaux de surface, texte en trois gris (principal, secondaire, étiquette). Les neutres tirent légèrement vers le bleu, jamais vers le brun.

| Rôle | Exemple |
|---|---|
| Scène | `#07080b`, relevée par un halo radial en haut au centre |
| Surfaces (3 niveaux) | `#0f1115`, `#15181e`, `#1c2027` |
| Bordure / reflet intérieur | blanc à 8 % / blanc à 6 %, 1 px |
| Texte principal / secondaire / étiquette | `#f2f4f8` / `#a4abb8` / `#6b7280` |
| Grille | blanc à 3 % ; une ligne sur quatre à 6 % ; module de 48 px |
| **Accent (un seul par film)** | citron vert `#B7F34A`, ou violet électrique `#8B7CFF`, ou orange signal `#FF7A1A` |
| Couleur du problème | un rouge, tant que le problème existe |

(Neutres : valeurs d'exemple ; accents : ceux de la source. En pratique l'accent est la couleur de marque du client.)

- **Un seul accent**, saturé, lumineux, avec sa propre lueur, réservé à ce que le produit **est** ou **fait**. Si deux choses sont de la couleur d'accent, l'une des deux est une erreur.
- **La couleur du problème** n'existe que tant que le problème existe ; après le retournement, elle ne revient jamais. Problème = bruit ; accent = produit.
- Attention à la règle commune du plugin : pas plus de 30 % d'images dominées par le bleu-violet. Avec un accent violet, le garder petit.
- **Polices** (libres) : Inter (interface, sous-titres, titres), Inter Tight 600 pour les nombres géants (interlettrage d'environ −4,5 %), JetBrains Mono pour les étiquettes, noms de fichier et textes d'état.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place d'Inter Tight ; Inter, JetBrains Mono : déjà fournies. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/inter-tight` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Interface, toute originale** : fenêtres arrondies (barre de titre avec seulement un petit signe et un titre ; **jamais** de boutons de fenêtre colorés, de barre de menus ni de barre d'icônes d'un vrai système), cartes de notification, icônes de fichier, vignettes, lignes de liste, onglets, pastilles, barres, tuiles.
- **Scène** : un grand halo froid à quelques pour cent d'opacité, décentré ; un assombrissement des coins de 50 à 55 %. Pas de grain.
- **La lumière est l'outil de révélation** : seuls les pixels que la lumière a traversés s'allument.

## 3. Composition 9:16

- **Beaucoup de vide, un seul point d'attention, l'accent sur ce point.**
- Grille de 48 px : 22 colonnes sur 1080, tout s'y accroche.
- Les mouvements d'accumulation et de rangement fonctionnent très bien en hauteur : une colonne de notifications qui s'empile, puis une grille de 4 colonnes sur 6 à 8 rangées qui se forme d'un coup.
- **Une phrase par écran** pour les titres : Inter 600, 84 à 110 px, 2 lignes au plus, entre y 600 et y 1000.
- **Le grand nombre a son propre écran**, 300 à 420 px de haut, centré vers y 800, **sans sous-titre par-dessus** : le nombre est le message.
- **Les sous-titres sont un composant d'interface** : une notification en bas au centre (pilule sombre translucide, bordure claire de 1 px, ombre douce, Inter 500 de 46 à 50 px, un petit point d'accent « en train de parler »), entre y 1400 et y 1540. Elle entre en montant un peu, en 0,16 s environ.
- **Le texte tapé est son propre sous-titre** : ce que le curseur tape dans l'image n'est pas écrit une seconde fois.
- Remonter le contenu quand un sous-titre est affiché ; rien d'important à droite de x 945.
- Angle penché et tremblement : seulement pour le désordre.

## 4. Ce qui bouge

- **Action principale** : une accumulation générée par règle (de plus en plus vite, des centaines d'éléments), puis **l'accroche à la grille** : tout vole à sa place en un temps.
- **Boucles de fond** : (1) le curseur (ou le plus petit élément vivant du produit) qui clignote : c'est le métronome et la marque ; (2) un tremblement de quelques pixels sur les éléments sous tension, ou la lueur de l'accent qui respire.
- **Autorisés** : apparition éclair `#001`, dépassement `#010` (un seul petit dépassement, puis arrêt immédiat), décalage en cascade `#002`, reflet de lumière `#022`, brouillage de texte `#129` (les chiffres se brouillent et se verrouillent un par double croche), compteur `#007`, machine à écrire `#006`, arrêt sur image `#040`, zoom à travers `#020`, raccord de forme `#042`, panoramique filé `#043`, parallaxe `#016` (caméra 2,5D), anticipation `#121` (au moins 8 images d'élan pour l'élément vivant), très gros plan `#184`, vue du dessus `#181`.
- **Interdits** : fondu enchaîné `#044` et image vide, flottement sinusoïdal `#096`, rebond mou `#123`, saccade ou tremblement du trait `#136`, grain `#118`, dégradés de couleur vifs `#095`, reflet blanc dur.
- Les apparitions sont courtes et typées (chute et rebond, lancer, glissement, surgissement ; 0,2 à 0,3 s), **un mouvement par type d'élément**.
- Les vols suivent des courbes ; les éléments d'un même type courbent dans le même sens et ne se croisent jamais.
- **Disparaître se dessine** : replier une partie par temps, ou s'écraser en un point comme un vieil écran qui s'éteint. Rien ne s'efface simplement.
- La scène et la grille ne bougent jamais seules : seule la caméra les déplace.

## 5. Rythme et montage

- 30 images par seconde, fluide, aucune saccade : c'est de la précision, pas de l'artisanat.
- **Tout atterrit sur la grille et sur le temps.** Un mouvement part un temps avant et arrive dessus.
- Plans de 2 à 5 s ; inserts d'une demi-seconde pour la surcharge.
- **Transitions = une interface qui s'ouvre ou se referme** : chaque changement de plan est un élément qui s'étend jusqu'à remplir le cadre, ou le cadre qui se replie dans un élément. Une ouverture calée sur un temps part une image avant, pour être ouverte à 80 % sur le temps.
- **Le gel** : tout s'arrête en l'air et le son tombe à zéro. La caméra peut avancer dans l'image figée.
- Revenir à un cadrage du début pour montrer ce qui a changé.

## 6. Recette technique

- **Moteur** : HyperFrames. Deux voies : éléments HTML/CSS animés par GSAP (jusqu'à une centaine d'éléments, texte net, modifiable) ; canvas 2D avec `dessiner(t)` pour les accumulations de plusieurs centaines d'éléments.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `scene.js` (fond, grille, halo), `interface.js` (les composants), `vol.js` (trajectoires courbes, destinations typées), `lumiere.js`, `camera.js`, `film.js`. Les événements visuels peuvent naître sur les notes de la musique, depuis une même table de notes.

```js
// caméra 2,5D : un élément à la profondeur z est grossi (et flouté) selon sa proximité
const echelle = (zoom, z) => 1 / (1 / zoom - z);
// accroche à la grille : chaque élément a une case de destination selon son TYPE, trajet courbe, arrivée sur le temps
tl.to(".tuile", { x: i => cases[i].x, y: i => cases[i].y, rotation: 0, duration: 0.5, ease: "back.out(1.3)",
                  stagger: { each: 0.004, from: "edges" } }, temps(16) - 0.5);
// révélation par la lumière : front doux, reflet ≤ 20 %, durée ≤ 1,3 s
const allume = (x, t) => adoucir(borner((front(t) - x) / 180));
```

- **Techniques clés** : générer le désordre par règle, puis **ajuster le nombre d'éléments au nombre exact de cases** de chaque groupe ; pour une rotation en perspective, projeter la surface **opaque** puis l'éclairer ; les chiffres en largeur fixe pour qu'un compteur ne tremble pas.
- **Pièges** : une accroche « à la case la plus proche » ressemble à un clignotement, pas à un rangement ; trop peu d'éléments laissent des trous dans la grille qui se lisent comme une erreur ; un rectangle teinté plat pour « fermer » ressemble à un élément manquant (écraser la vraie surface) ; une surface translucide découpée en bandes pour la perspective montre des coutures.

## 7. Son

- **Musique** : percussions accordées et nappes : marimba, vibraphone, glockenspiel, célesta, nappe ou bourdon de synthétiseur, pulsation grave, piano feutré. Propre, sec, minimal.
- **La musique est un processus visible** : deux voix sur un même motif dont l'une se décale ; une note ajoutée par mesure ; des notes retirées jusqu'à n'en laisser qu'une ; ou un seul accord sur lequel tout atterrit.
- **Deux familles de sons = l'histoire** : le désordre sonne **épars** (désaccordé, placé au hasard dans l'espace, un timbre par source) ; les sons du produit forment **une seule famille** (tics feutrés, verre, tous dans le même mode, centrés), si bien que beaucoup d'atterrissages donnent un seul scintillement juste. Ces sons-là sont dessinés : la synthèse est ici à sa place, avec des échantillons réels pour le clavier et les clics.
- **Bruitages** : tic de curseur, touches plates, verre de notification, fichier qui tombe, fenêtre qui glisse, empilements sourds, scintillement du balayage de lumière, grains de chiffres. Pour une accumulation de centaines d'éléments, un seul lit sonore qui s'épaissit, pas un son par élément.
- **Ambiance** : une pièce calme, un ventilateur d'ordinateur. À garder bas tant qu'une phrase n'est pas finie.
- **Silence** : zéro absolu sur toutes les pistes quand l'écran se fige. Le premier son d'après est le plus important.
- **Voix** : assurée et retenue, phrases courtes et affirmatives.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Un seul accent à l'écran, sur l'élément le plus important.
- [ ] Aucune commande d'un vrai système d'exploitation, aucune capture d'écran : toute l'interface est dessinée.
- [ ] La couleur du problème ne revient plus après le retournement.
- [ ] Chaque élément est sur la grille de 48 px ; chaque arrivée tombe sur un temps.
- [ ] Aucun fondu, aucune image vide entre deux plans.
- [ ] Le grand nombre est seul à l'écran, sans sous-titre.
- [ ] Le fond n'est pas mort : curseur, lueur ou tremblement vivent pendant les tenues.
- [ ] La grille finale n'a ni trou ni élément en trop.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 10
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Film de démo d'origine, *Room to Think* (42 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/dark-keynote.mp4
- Affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/dark-keynote.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, film et images sous CC BY 4.0.

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichiers `styles/dark-keynote/STYLE.md`, `DEMO.md`, `demo/engine.js`, `demo/world.js`, `demo/film.js`.
- Licence : MIT pour le code et les textes (© 2026 LemoLab), CC BY 4.0 pour le film et ses images. Polices Inter, Inter Tight, JetBrains Mono : OFL 1.1.
- Adaptation Flot Web : traduction, composition verticale, neutres d'exemple, portage vers HyperFrames, numéros de mouvements, règles de son du plugin. Fiche sœur : `keynote-produit` (vraies captures du produit).
