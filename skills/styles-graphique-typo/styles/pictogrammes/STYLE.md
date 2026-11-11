# Pictogrammes en rythme

## 1. Identité

- **Nom** : Pictogrammes en rythme.
- **Inspiration** : les pictogrammes sportifs géométriques des années 1970, les identités visuelles de grands événements multisports (un motif modulaire et un jeu de couleurs utilisés partout), l'habillage télévisé sportif (petits textes à chasse fixe, barre de progression à crans). On apprend la grammaire ; on ne recopie les pictogrammes, l'emblème, le slogan, le motif ni les noms de couleurs d'aucun événement réel.
- **Ce qui le fait reconnaître** : (1) un **motif en grille carrée** fait de disques, demi-disques et petites cellules à motif, en **cinq tons d'une même teinte**, dont des **rangées entières glissent de côté** ; (2) des **pictogrammes géométriques** (objets, véhicules, météo, panneaux, et un personnage à tête ronde si besoin) faits de barres à bouts ronds, de disques et de capsules ; (3) une **typo très grasse** qui monte de derrière un masque ; (4) **chaque coupe tombe sur un coup de batterie**.
- **Deux formes de film** : un **catalogue** (N produits, plats, étapes, espèces, une carte à la fois, vite, sur le temps) ou une **histoire en pictogrammes** (un pictogramme héros, un but, un retournement, une fin).
- **Marche pour** : « les 10 outils de… », toutes les étapes d'une recette, la gamme d'une marque, les règles d'un sport, un bilan d'année, un compte à rebours, un contenu bilingue.
- **Ne marche pas pour** : émotion fine, portrait, démonstration de logiciel, graphique de données (ici les nombres sont des étiquettes). Les pictogrammes n'ont jamais d'expression ni de visage.

## 2. Palette, typographie, matières

- **Un jeu de cinq teintes + un neutre sombre**, chaque teinte en **cinq tons** (du plus sombre au plus clair, celui du milieu est la base). Un chapitre = une teinte.
- Une seule crème et une seule encre servent toutes les teintes. Aucun contour, aucun reflet, sauf un balayage de lumière doux (le seul dégradé).

| Jeu d'exemple | Teintes |
|---|---|
| Fête chaude | rouge, violet, vert forêt, or, ocre |
| Littoral | marine, sarcelle, corail, sable, ciel |
| Cuisine | tomate, basilic, safran, aubergine, crème de farine |

Exemple chiffré pour une teinte « tomate » : `#5e1a12`, `#8f2a1c`, `#c8402a` (base), `#e2735a`, `#f3b3a0` ; crème `#f4ecdc` ; encre `#16130f`. Choisis le jeu d'après le sujet et invente tes propres noms de couleurs.

- **Sur une teinte claire** : texte et pictogrammes sombres, disque de scène dans le ton plus clair. **Sur une teinte sombre** : crème. Sur le neutre sombre, le disque prend un ton plus clair, sinon il disparaît.
- Sous le texte, le motif tourne à **faible contraste** ; sur les cartes de chapitre, à **plein contraste**.
- **Polices** (libres) : Inter Tight 900 (titre), DM Mono (méta-textes, étiquettes, compteur).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place d'Inter Tight ; IBM Plex Mono à la place de DM Mono. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/inter-tight`, `@fontsource/dm-mono` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Pictogrammes** : une seule famille d'épaisseur de trait par film, bouts ronds, aplats, deux tons au plus par pictogramme. Tout ce qui ne se lit pas comme un signe à 60 px est supprimé.
- **Personnage** (facultatif) : sans visage, tête en disque, barres arrondies ; les membres du côté éloigné sont mélangés à environ 40 % vers le fond.

## 3. Composition 9:16

- **Une grille carrée** règle tout : cellule de 180 px (6 colonnes sur 1080, soit environ un dixième de la hauteur).
- La carte horizontale « pictogramme à côté du titre » devient une carte **empilée** : la scène (pictogramme sur son grand **disque soleil**) entre y 260 et y 1000 ; le bloc de titre entre y 1040 et y 1500.
- **Titre** : 150 à 260 px, graisse 900, interlettrage serré, ajusté automatiquement à la largeur (900 px au plus). Deuxième ligne (deuxième langue ou précision) en dessous, en gras, 60 à 80 px. Méta en chasse fixe de 28 à 30 px (jamais moins : 28 px est le plancher de lecture du studio).
- **Habillage** dans les coins hauts (sous y 160) : index « 07 / N » et **barre de progression à N crans** (le courant est haut, les passés atténués, les suivants pâles). Rien dans la colonne de droite au-delà de x 945.
- Le texte et le pictogramme ne se chevauchent jamais. Une pose horizontale (nager, ramper) pousse la scène vers l'extérieur.
- La carte **est** la couche de texte. Avec une voix off, les sous-titres vont sur une bande pleine dans le ton le plus sombre du chapitre, en bas à gauche au-dessus de y 1560, jamais sur le titre. Une carte qu'il faut lire (un chiffre, une caractéristique) tient au moins 1,6 s.

## 4. Ce qui bouge

- **Action principale** : une carte = un élément = **un seul verbe** (le pictogramme fait une action lisible en une mesure : un engrenage tourne, une tasse verse).
- **Boucles de fond** : (1) les rangées du motif dérivent en sens alternés, et sautent d'un quart de cellule sur les temps dans les cartes de chapitre ; (2) le balayage de lumière doux sur le disque soleil.
- **Autorisés** : révélation par masque `#005` (titre, puis deuxième ligne 0,08 s après, puis l'étiquette), machine à écrire `#006` sans curseur pour les méta, décalage en cascade `#002`, compteur `#007` (un grand nombre roule jusqu'à sa valeur sur une mesure), poussée `#137`, stores `#138` (rangées qui glissent), iris `#188`, retournement de tuiles `#021`, panoramique filé `#043` d'un écran par temps, écran partagé `#144` le long d'une ligne de grille, plan fixe `#175`.
- **Interdits** : fondu enchaîné `#044`, mouvement de caméra 3D `#030`, caméra à l'épaule `#034`, flou de profondeur `#105`, écrasement `#011` sur les pictogrammes, expressions de visage.
- Courbes : sortie exponentielle pour les entrées, entrée-sortie exponentielle pour les filés et volets ; un dépassement `#010` une seule fois au plus dans le film.
- **Assemblage** : le pictogramme et sa scène arrivent en bandes horizontales qui glissent en place depuis des côtés alternés.
- Flou de mouvement seulement dans les transitions et les filés.

## 5. Rythme et montage

- **Une grille de temps** : un tempo pour tout le film ; chaque plan commence sur un temps, chaque moment clé d'une pose (lâcher, contact, réception) tombe sur un temps entier.
- **Échelle de cadence** : une carte normale dure une mesure ; les sous-éléments proches passent en rafale à demi-durée. On obtient un second tempo en divisant le temps, jamais en changeant de tempo.
- Les transitions s'accrochent à la grille et durent quelques images autour de la coupe ; on les fait tourner.
- Fin possible : le mur de pictogrammes (tous reviennent en grille et prennent une seule couleur).
- **Version courte (8 à 12 s)** : un seul chapitre (une teinte) : quatre cartes d'une mesure (2 s) et une rafale à demi-durée ; couper le titre long. Accroche : la première carte agit dès le premier temps.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D avec `dessiner(t)` (le motif en éléments HTML serait trop lourd).
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `moteur.js` (palette, motif avec décalage par rangée, bibliothèque de motifs, pictogrammes, texte masqué, courbes), `film.js` (liste des plans en secondes, événements sonores, habillage, transitions sur grille). La liste des plans est la **source unique** : la musique et les bruitages lisent les mêmes temps.

```js
// motif : plus large que l'écran, pour qu'une rangée puisse glisser d'une cellule
function motif(ctx, teinte, graine, decalages) {
  for (let r = 0; r < RANGS; r++) { ctx.save(); ctx.translate(decalages[r] * CELL, r * CELL); rangee(ctx, r, teinte, graine); ctx.restore(); }
}
const surTemps = n => n * 60 / BPM;                 // tout départ de plan = surTemps(entier)
```

- **Techniques clés** : motifs choisis dans une bibliothèque de géométrie générique (quarts de disque, vagues en écailles, arcs concentriques, damiers, croissants), tournés par multiples de 90°, jamais de mascotte ni de monument ; environnement du pictogramme (eau, pluie, rails) dans un calque à part, estompé avant la colonne de texte.
- **Pièges** : crème sur teinte claire = contraste raté ; le disque soleil disparaît sur le neutre sombre ; les motifs sont grands et tirés au sort par carte, il faut un cache borné, sinon la mémoire sature au rendu ; une imitation trop proche d'une identité réelle (inventer sa palette, sa marque et son slogan).

## 7. Son

- La typo et la musique peuvent porter le film seules ; la voix est facultative, calme, une ou deux phrases par chapitre.
- **La percussion est la colonne vertébrale** : choisir une famille de tambours adaptée au sujet (tambours sur cadre, taïko, caisses claires, percussions corporelles, kit électronique), plus clics de baguette, claps, shakers.
- Par-dessus : cordes pincées, marimba, glockenspiel, basse synthétique, montées.
- **Un accent par plan, choisi par chapitre** : une éclaboussure, un « poc », un cliquetis, un grésillement. Le bruitage dit la matière du chapitre. Vérifier chaque départ à ±15 ms.
- **Silence** : un demi-temps sans batterie ni basse avant un grand coup, ou une mesure entière réduite à un seul tic sous un décompte.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Chaque carte montre un pictogramme, une action, un grand titre, un index « n / N ».
- [ ] Le motif est en cinq tons d'une seule teinte, et au moins une rangée glisse.
- [ ] Tous les pictogrammes partagent la même épaisseur de trait et se lisent à 60 px.
- [ ] Chaque coupe tombe sur un temps (écart de moins d'une image).
- [ ] Le texte et le pictogramme ne se touchent jamais.
- [ ] Le contraste texte/fond est juste sur les teintes claires comme sur les sombres.
- [ ] Aucun visage, aucune profondeur 3D, aucun fondu.
- [ ] La barre de progression compte bien N éléments et reste sous y 160 à gauche de x 945.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 12
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu

- Film de démo d'origine, *Left Behind* (50 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/pictogram-motion.mp4
- Affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/pictogram-motion.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, film et images sous CC BY 4.0.

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichiers `styles/pictogram-motion/STYLE.md`, `DEMO.md`, `demo/engine.js`, `demo/film.js`, `demo/mix.py`.
- Licence : MIT pour le code et les textes (© 2026 LemoLab), CC BY 4.0 pour le film et ses images. Polices Inter Tight et DM Mono : OFL 1.1.
- Adaptation Flot Web : traduction, carte empilée verticale, exemple de teinte chiffré, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
