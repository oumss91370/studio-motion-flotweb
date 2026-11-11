# Affiche sérigraphiée

## 1. Identité

- **Nom** : Affiche sérigraphiée (« Silkscreen Travel Poster »).
- **Inspiration** : les affiches de parcs nationaux sérigraphiées des années 1930-1940 (4 à 6 encres plates, faces éclairées et faces d'ombre, ciels en bandes, bandeau d'information sombre, soleil en anneaux), les séries d'affiches contemporaines sur un même gabarit, et **le procédé physique** : écran à charnière, raclette qui pousse un boudin d'encre, tirages à plusieurs couleurs dans le même passage, stries, trous, liserés de repérage. On ne copie jamais la composition, le nom, le lettrage ou le logo d'une affiche réelle, et on ne nomme aucun organisme réel.
- **Ce que c'est** : une affiche **imprimée devant la caméra**. Chaque couleur est une encre **opaque** posée par son propre passage ; une encre recouvre complètement la précédente. **Ni trame, ni encre fluo, ni trait** : le bord d'une forme est l'endroit où une encre plate s'arrête. **Les dégradés sont interdits** : ciels et brumes sont des **bandes en paliers** (une couleur plate, des rayures qui s'amincissent, la couleur suivante). **L'information se révèle comme l'impression se fait : une couche, un temps.**
- **Ce qui fait « sérigraphie » et non « vectoriel »** : le **repérage** (chaque couche décalée de 1 à 3 px ; une forme en réserve laisse un croissant de papier nu) ; le **bord de surimpression** (un mince liseré plus sombre là où une encre chevauche l'autre) ; **l'épaisseur d'encre** (liseré clair en haut à gauche, sombre en bas à droite ; l'encre fraîche a un reflet humide qui s'éteint en une seconde) ; le **papier** crème à fibres.
- C'est un **style « de scène »** : il fait un travail pratique (voir la section 5) pour un lieu, un événement ou un produit qui a quelques faits.
- **Marche pour** : destination, sentier, événement avec date et lieu, festival, sortie de produit en plusieurs coloris, horaires de saison, série de quartiers.
- **Ne marche pas pour** : récit à personnages, explication technique, visages, texte long.
- **À ne pas confondre** : pas la `risographie` (translucide, tramée) ; pas l'estampe japonaise (trait + dégradé essuyé) ; pas la `gravure-sur-bois` ; pas du low-poly 3D.

## 2. Palette, typographie, matières

- **Une palette par affiche, 6 encres au plus**, par rôle : ciel clair, ciel profond et bandes, lointain, plan moyen, premier plan (le plus sombre ; aussi le bandeau d'information), et **un accent vif**. Une encre « face éclairée » en option.

| Palette (ciel clair → premier plan, puis accent) | Hex |
|---|---|
| Aube | `#F6CD98` `#EE9A73` `#9A7FA8` `#3E7079` `#1E3B3F` · accent `#FBE6B4` |
| Port à midi | `#E8F0F2` `#7FB3C8` `#D9C7A3` `#2F6E8E` `#173247` · accent `#E8553D` |
| Hiver | `#EEF1F4` `#B8C9D9` `#8B9BB0` `#4A5D78` `#1F2A3C` · accent `#F2B134` |

- **Les valeurs vont du clair (loin) au sombre (près)** : la profondeur est une valeur, jamais un flou.
- **L'accent est rare** : le soleil ou la source de lumière, **le** trajet ou **le** produit, le chiffre le plus important.
- **Le papier est une couleur** : une zone non imprimée est la chose la plus claire de la feuille (eau, neige, faisceau).
- **Une série = un gabarit, une nouvelle palette par élément** (heure, saison, coloris, quartier). Ré-encrer la même géométrie dans une autre palette est un message.
- **L'encre du texte se choisit par contraste** avec l'encre du dessous, jamais par une couleur fixe : une palette de nuit ne doit pas avaler un titre.
- **Typographie** (OFL) : display **condensée** pour les noms et les valeurs (**Big Shoulders Display**, **League Gothic**), ajustée à la largeur ; sans-serif géométrique à interlettrage large pour les étiquettes (**Outfit 600**).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : League Gothic à la place de Big Shoulders Display ; League Gothic, Outfit : déjà fournies. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/big-shoulders-display` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : un tracé par couche d'encre, les réserves sont des trous dans le tracé. Budget de texture : fine trame de papier, marbrure à ≈ 55 %, trous d'épingle à ≈ 75 %, visibles seulement sur l'encre. Plus, ça se lit comme de la riso. Crêtes à facette éclairée dentelée, pins d'un seul contour à étages tombants, eau en corps plat avec des barres de reflet.

## 3. Composition 9:16

- **La feuille portrait est le gabarit d'origine** (proportion 2:3) : en 9:16, feuille de ≈ 1000 × 1500 unités placée en x 40 à 1040, y 180 à 1680, sur un établi (la feuille déborde de la zone utile : le nom, les étiquettes et les valeurs restent entre x 60 et x 945, au-dessus de y 1560) ; ou affiche **plein cadre** (l'image va jusqu'aux bords, le nom imprimé dans le ciel, un panneau d'information sombre imprimé en dernier).
- Zones : **nom imprimé dans le ciel** (y 240 à 520, lettres espacées, 150 à 240 px), scène en 4 à 5 plans de valeur (y 520 à 1280), **bandeau d'information sombre au pied** (y 1280 à 1540) : un nom, un chiffre, un filet, une rangée de données ; colonnes dimensionnées par leur contenu.
- **Le texte de l'affiche est le sous-titre.** Aucune narration n'est nécessaire ; s'il y a une voix, les sous-titres sont une **bande imprimée** (un passage de raclette), jamais une légende flottante.
- Tailles en plan large : étiquettes ≥ 28 px, valeurs ≥ 44 px ; un gros plan sur le bandeau garde tout le bandeau dans le cadre avec ≥ 5 % de marge.
- En plein cadre, la caméra reste **dans** l'impression. Une bannière très large devient une lamelle : garde ≈ 4:1 au plus. Rien d'important à droite de x = 945.

## 4. Ce qui bouge

- **Action principale** : **le passage de raclette** : un front irrégulier révèle l'encre (avec une traîne d'environ 30 unités) ; la lame, le boudin d'encre et un bout de manche voyagent dessus. **Les passages sont linéaires et réguliers : une raclette n'accélère ni ne freine.** Les encres d'accent partent un demi-temps après l'encre principale de leur couche.
- **Boucle de fond 1** : le reflet humide de l'encre fraîche qui s'éteint, les filaments visqueux du boudin d'encre, l'ombre de l'écran (un anneau, jamais un rectangle plein).
- **Boucle de fond 2** : la scène terminée qui « s'éveille » (vagues en barres, oiseaux, fumée), en formes plates.
- **Gestes natifs** : **une encre, un temps** (les faits s'impriment en dernier, quand on les lit) ; le **tirage à plusieurs couleurs** dans un seul passage (un ciel entier) ; le **ré-encrage de palette** (une large raclette traverse la feuille en diagonale en ≈ 0,35 s ; la géométrie est identique des deux côtés de la lame, seules les encres changent) ; **le repérage qui glisse puis claque** (les plans flottent en parallaxe, avec des jours de papier et des ombres d'épaisseur, puis **se calent d'un coup**, avant les faits clés) ; le papier comme couleur ; le trajet imprimé segment par segment en pointillés d'accent ; le mur de la série.
- **Levée de l'écran** : le cadre bascule sur sa charnière (écrasement vertical + ombre qui grandit) en ≈ 0,4 s.
- **Autorisés** : `#045` volet à bord net (la raclette), `#029` travelling avec la raclette, léger roulis, `#181` vue du dessus de la feuille entière, `#028` recul rapide quand l'écran se lève, `#027` avancée + bascule vers le bandeau, `#016` parallaxe de plans (avec le claquement de repérage), `#025` travelling lent le long d'une rangée d'affiches, `#184` plongée dans la trame de la soie, `#004` tracé (trajet en pointillés), `#002` cascade (données de gauche à droite).
- **Interdits** : **tout fondu** (`#044`), dégradés, trame, trait de contour, flou de profondeur, accélérations sur la raclette, coupe nue sans geste d'atelier.

## 5. Rythme et montage

- **Un passage, un coup de musique** : chaque encre tombe sur un événement musical ; on accélère en subdivisant, pas en changeant de tempo. Le claquement de repérage est un temps fort appuyé.
- Les données s'impriment de gauche à droite sur des subdivisions du temps.
- **Règle de lecture** : chaque texte reste ≥ (caractères ÷ 12 + 1) s, 1,5 s au minimum, après l'arrivée de son **dernier** élément ; arrondis au temps suivant.

| Usage | Ordre d'impression | Tenue par couche | Durée |
|---|---|---|---|
| Guide de sentier ou de visite | lieu → par étape : scène → nom → difficulté → distance → durée → pied | titre ≈ 3 s ; rangée de données ≥ 2,2 à 3 s | 30 à 40 s, 3 étapes |
| Affiche d'événement | passages de la scène → titre → date → lieu → appel à l'action | titre 2,5 s ; date + lieu 3 s ; final 3 s | 15 à 20 s |
| Série de destinations | un gabarit, une palette par lieu : nom → un fait → mur de la série | 2,5 s par affiche + 4 s de mur | 20 à 30 s |
| Sortie de produit | couches autour d'une silhouette plate → nom → coloris × 3 (ré-encrage) → prix, date | 1,8 s par coloris | 12 à 18 s |
| Horaires de saison | une affiche ré-encrée par saison → saison + horaires | 2 s par changement | 10 à 15 s |

- Changements : couches par la raclette ; affiches par une **silhouette de premier plan** (arbre, lampadaire, voile) qu'on traverse, par un balayage diagonal qui imprime l'affiche suivante derrière la lame, ou par un mouvement sur l'établi. Plan final sur le mur : tenue ≥ 3 s.
- **Version courte (8 à 12 s)** : une seule affiche : trois passages de raclette (le premier avant 2 s), le nom, une rangée de données tenue (caractères ÷ 12 + 1 s) ; couper les étapes suivantes du guide.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `soie.js` (textures, feuille, **encre** : tracé + réserve + couleur + repérage + découpe + reflet + liseré, front de raclette irrégulier, raclette et boudin, cadre d'écran, **bandes en paliers** : le remplaçant du dégradé), `affiche.js` (gabarit, passages partiels, plans flottants, talon de billet, choix d'encre par contraste), `scenes.js` (un lieu = des pièces d'encre dans l'ordre d'impression), `film.js` (timeline, caméras, balayages).
- **Techniques clés** :
  ```js
  // une encre : remplissage opaque, décalage de repérage, découpe par le front de raclette
  encre(ctx, { trace, reserve }, { couleur, decal: [2, -1], decoupe: front(p), reflet: 1 - age });
  const p = (t - t0) / (t1 - t0);                     // passage LINÉAIRE, sans courbe d'accélération
  // ciel sans dégradé : aplat A, puis rayures de B de plus en plus épaisses, puis aplat B
  bandes(ctx, zone, [cielClair, cielProfond], { rayures: 5 });
  // liseré d'épaisseur : remplir, puis remplir décalé à l'intérieur d'une découpe (jamais un trait)
  ```
- **Pièges** :
  - Un effet de bord fait avec un trait dessine des lignes internes sur des tracés réunis : remplissages seulement.
  - Ombre d'écran en rectangle plein : elle salit l'impression ; fais un anneau.
  - Facettes d'ombre froides à côté de l'eau : elles se lisent comme de l'eau ; ombres dans l'encre du premier plan.
  - Boudin d'encre dentelé : il se lit comme un bord de papier ; fais-le rond.
  - **Parallaxe seule = « les montagnes bougent »** : il faut les jours de papier et l'épaisseur pendant que c'est flottant, puis le claquement à zéro avec un son.
  - Un volet par silhouette qui tient un écran sombre vide : centre-le sur le changement (couverture totale ≈ 1 image).
  - Des points de couleur au hasard sur la table = des confettis : fais un vrai établi (planches, veines, taches assourdies, ruban adhésif).
  - Trop d'éléments à des temps de lecture honnêtes : imprime-les côte à côte dans les mêmes passages, ou laisse les secondaires se lire sur le mur final.

## 7. Son

- **Instruments acoustiques joués à la main** : guitare grattée, guitare slide, harmonica, contrebasse, cajón ou balais, banjo, violon, accordéon, ukulélé. Choisis la famille selon le lieu : folk, surf, bossa ou fanfare conviennent.
- **Bruitages par matière** (≈ 5 par 10 s) : **raclette sur la soie** (souffle granuleux ; plus vite = plus clair), encre humide, claquement de l'écran et grincement de charnière, tampons de papier, tics pour un trajet en pointillés, serre-joint bois et métal, pinces du séchoir.
- **Ambiance de l'intérieur de l'image** : une scène finie peut « s'éveiller » (ressac, rue, foule), en entrant avant l'image et en sortant après.
- **Silence** : la musique tombe un temps avant les faits clés ; il reste une ambiance, et le premier son ensuite est un geste décisif (le serre-joint, une longue glissade).
- Musique légèrement baissée sous les bruitages. Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Six encres au plus, opaques ; aucun dégradé, aucune trame, aucun trait de contour.
- [ ] Les ciels sont en bandes en paliers.
- [ ] Chaque couche est décalée de 1 à 3 px ; un croissant de papier se voit autour d'une réserve.
- [ ] Les valeurs vont du clair au loin au sombre au premier plan ; l'accent n'apparaît que sur 1 à 3 éléments.
- [ ] Les passages de raclette sont linéaires ; chaque encre tombe sur un coup de musique.
- [ ] Les faits s'impriment en dernier et restent lisibles (caractères ÷ 12 + 1 s).
- [ ] Aucun fondu ; changements par raclette, silhouette de premier plan ou établi.
- [ ] Encre du texte choisie par contraste ; bandeau d'information au-dessus de y = 1560.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 7
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu

- Film de démo d'origine *The Long Way Home* (50 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/silkscreen-poster.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/silkscreen-poster.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/silkscreen-poster.jpg · galerie : https://lemomo-ai.github.io/lemo-opuscar/#print-printmaking
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre les lieux, les affiches ni la timeline.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/silkscreen-poster/STYLE.md`, `DEMO.md`, `demo/engine/silk.js`, `poster.js`, `scenes.js`, `demo/film.js`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0.
- Les affiches de huashu-art-motion (Art nouveau, constructiviste, Bauhaus) sont traitées dans `styles-graphique-typo` : pas de doublon ici.
- Adaptation Flot Web : traduction, gabarit portrait placé dans le 9:16, tableau d'usages, numéros du dictionnaire de mouvements, budget de bruitages.
