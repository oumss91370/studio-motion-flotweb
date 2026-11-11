# Gravure sur bois

## 1. Identité

- **Nom** : Gravure sur bois (« Woodcut Print », estampe en relief).
- **Inspiration** : les romans sans paroles en gravures sur bois des années 1920 (une suite de planches autonomes), la gravure expressionniste où l'émotion vit dans la direction de la gouge, la gravure d'illustration du XIXᵉ siècle où l'espacement et la direction des tailles construisent la lumière et le volume. On ne copie jamais une planche, une figure, une bordure ou un titre.
- **Ce que c'est** : chaque plan est **une planche imprimée** : encre noire sur papier vergé, encadrée d'une marge de papier. Trois règles de la vraie impression en relief :
  1. **Le noir est le bois, le blanc est ce que le couteau a enlevé.** La lumière est *taillée* : une zone claire = beaucoup de larges tailles ; une zone sombre = du bois intact.
  2. **Les images apparaissent en étant taillées.** Rien n'arrive en fondu : les tailles poussent trait par trait le long de la forme, grosses gouges d'abord, traits fins ensuite.
  3. **Le bloc est un miroir.** Les lettres se lisent à l'envers tant que la feuille n'est pas tirée ; ce retournement est la transition propre au style.
- **Marche pour** : récit grave, mémoire, travail, effort long, lutte, hommage, « la lumière revient », portrait, sujet historique ou social.
- **Ne marche pas pour** : sujet léger, produit coloré, interface, humour, beaucoup de texte.
- **À ne pas confondre** : pas la `gravure-cuivre` (traits noirs sur fond blanc) ; pas une linogravure d'affiche (pas d'aplats de couleur) ; pas une photo passée dans un filtre de seuil (les tailles doivent **suivre la forme**).

## 2. Palette, typographie, matières

| Rôle | Hex |
|---|---|
| Encre (presque noire) | `#15120f` |
| Papier vergé chaud | `#efe6d2` |
| Bois nu (seulement quand on montre le bloc) | `#c9a676` |
| Planche de couleur, **une seule au plus** (exemples) | cuivre brûlé `#c8622a` (chaleur), bleu de Prusse `#1f4e79` (eau, nuit), sang de bœuf `#7a1f1c` (blessure, sceau) |

- **Deux valeurs portent tout.** La couleur n'est imprimée **que là où le blanc a été taillé** : elle luit hors des tailles et ne se pose jamais sur le noir (sur l'encre, elle serait presque invisible).
- La couleur est réservée à **la seule chose qui compte** (une flamme, du métal en fusion, un cœur, un signal). Elle peut s'étendre au pic et se réduire à un seul reflet ensuite ; jamais décorative.
- **Typographie** : **IM Fell English** (OFL), caractère de presse ancienne. **Les légendes sont en typographie dans la marge de papier**, sous la planche ; **les titres sont taillés**, pas tapés (en petites capitales, en miroir si le bloc est montré avant le tirage).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place d'IM Fell English. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/im-fell-english` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : classes d'outils, largeurs en 1080 de large :

| Outil | Largeur | Usage |
|---|---|---|
| Couteau | 1,2 à 2 px | contours ; le filet blanc qui sépare une figure noire d'un fond noir |
| Gouge en V | 2 à 8 px | hachures, cheveux, barbe, lumière fine |
| Gouge en U | 10 à 22 px | rayons, grands balayages de ciel, premier dégrossi |
| Coup de pointe | rayon 3 à 8 px | neige, étincelles, éclats |

  - **La direction suit la forme** (un objet rond est enveloppé d'arcs, une pente suit sa ligne de chute, le feu et la lumière rayonnent, un tissu suit ses plis). **La largeur suit le ton** (clair = tailles larges qui se touchent presque ; demi-ton = tailles fines ; sombre = aucune). Loin = dense et fin ; près = espacé et gros. Chaque ligne est une taille séparée (entrée franche, sortie effilée, bord ébréché), jamais une ligne mécanique continue.
  - *Figures* : silhouette noire + **halo blanc au couteau** + quelques hachures de lumière rasante sur le bord éclairé seulement. **Peau taillée en blanc, traits laissés en noir.**
  - *Tirage* : bavure de couteau sur les bords, encre inégale (±6 %), veines du bois, manques, repérage fixe légèrement décalé pour la planche de couleur.

## 3. Composition 9:16

- **La marge de papier ne bouge jamais.** Planche (zone imprimée) d'environ 960 × 1240 (x 60 à 1020, y 180 à 1420 ; la légende et tout texte s'arrêtent à x 945), au bord **irrégulier** (bord de bloc encré, jamais un rectangle net) ; **marge basse plus large** (y 1420 à 1560) pour la légende.
- **Légende dans la marge** : IM Fell English 46 à 52 px, en encre, passée dans le même rendu d'impression ; elle monte en 0,1 s sans glisser, s'efface en 0,15 s. Elle ne couvre jamais l'image. Tenue ≥ max(1,8 s ; réplique + 0,6 s).
- Masses noires sur blanc taillé, ou blanc sur noir intact : **jamais gris sur gris**. Sujet ≥ 1/3 de la hauteur de la planche.
- Le vertical convient au **cadre dans le cadre** (porte, fenêtre, arche) et aux rayons qui tombent d'en haut.
- Rien d'important à droite de x = 945.

## 4. Ce qui bouge

- **Action principale** : **la taille** : chaque trait a son instant de départ et sa vitesse (0,08 à 0,35 s). Ordre de révélation : par la lumière (zones claires d'abord, du gros au fin), en rayons depuis un point, du haut vers le bas.
- **Boucle de fond 1** : feu et liquides **retaillés toutes les 2 images** (frémissement voulu ; petite surface seulement : jamais un fond entier, jamais une alternance noir / blanc sur une grande zone) ; particules (étincelles, neige) fluides.
- **Boucle de fond 2** : la lumière : une planche de couleur qui respire, des rayons taillés qui s'allongent.
- **Gestes natifs** : la lumière est taillée (une gerbe de tailles depuis un point) ; tailler = le temps (un travail patient, taille après taille) ; **bloc en miroir → tirage à l'endroit** ; les coups de pointe comme matière (des points blancs qu'on peut ré-encrer jusqu'au noir) ; la planche de couleur qui s'étend puis se retire ; la suite de planches sans paroles.
- **Transition du papier** (la seule grammaire de transition avec la coupe) : le rouleau passe l'encre (un reflet humide balaie) → la feuille se pose → le frottoir tourne, l'image transparaît → la feuille se décolle en s'enroulant vers la caméra, lourde puis vive, son dos montrant l'image en miroir.
- **Coupe franche = un nouveau tirage** : deux images de repérage décalé (quelques pixels, puis retour).
- **Autorisés** : `#004` tracé (taille qui pousse), `#128` saccadé (personnages), `#121` anticipation puis frappe en 2 images et `#122` suivi, `#024` courte secousse, `#028` recul continu pendant que les tailles se répandent, `#175` planche fixe, `#027` avancée lente en gros plan, zoom sec tenu, `#031` grue d'un détail vers l'ensemble, `#046` coupe sur le temps, `#140` feuille qui se décolle, `#047`/`#048` son qui passe d'une planche à l'autre.
- **Interdits** : `#044` fondu, dégradés, gris, hachures sur toutes les surfaces (ça fait de la fourrure ou de la pluie), deuxième couleur, texte sur l'image, tailles qui grouillent sur les corps.

## 5. Rythme et montage

- Personnages à **15 poses par seconde** (à 30 i/s : une image sur deux ; 12 seulement dans un film livré à 24 i/s) ; caméra, particules, feu et lumière fluides. Les hachures vivent dans le repère de chaque partie du corps : elles bougent avec le membre et ne grouillent pas.
- Planches de 4 à 8 s ; une série de coupes sur le temps (« une planche par coup ») pour une accumulation.
- **Silence** : presque rien avec une seule ambiance, ou un vrai silence avant le moment le plus fort ; le premier son après est choisi.
- Peu de mots : les planches racontent.
- **Version courte (8 à 12 s)** : une seule planche : encrage, feuille, frottoir et révélation en 4 s, puis la planche tenue avec sa légende. Accroche : le rouleau passe avant 2 s.

## 6. Recette technique

- **Moteur** : HyperFrames ; canvas 2D pour tailler, passe WebGL2 pour imprimer.
- **Principe** : deux canvas : un **masque** (noir = intact, blanc = taillé) et, en option, une **planche de couleur**. Le compositeur imprime le masque (ou montre le bloc de bois encré, brillant, aux sillons clairs).
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `tailler.js` (forme taillée avec halo et hachures qui suivent la forme, trait le long d'un tracé, hachures de zone, coups de pointe, rayons), `imprimer.glsl` (tirage ou bloc), `filtre.js` (image ou relief → tailles), `feuille.js` (transition du décollage), `sculpts.js` (petits reliefs pour les gros plans).
- **Techniques clés** :
  ```js
  // une taille : segment de 30 à 160 px, entrée franche, sortie effilée, bord ébréché
  taille(masque, { de, vers, largeur: L(ton), t0, vitesse });        // largeur selon le ton
  // lumière rasante : seules les faces tournées vers la lumière reçoivent 3 à 6 tailles
  if (dot(normale, lumiere) > seuil) hachurer(bordEclaire);
  // gros plans (mains, objets) : sculpter un petit relief, l'éclairer, puis le convertir en tailles
  // qui suivent les lignes d'égale lumière, comme le ferait un graveur
  ```
- **Pièges** :
  - **Des marques blanches sur du blanc sont invisibles** : les coups de pointe ont besoin d'une masse sombre derrière.
  - **Hachurer toutes les surfaces** = fourrure ou pluie : lumière rasante, 3 à 6 tailles sur le bord éclairé seulement.
  - Visages noirs à tailles blanches : illisibles en petit. Peau blanche, traits noirs, un filet noir autour des parties blanches.
  - Accessoires de gros plan dessinés à la main = moufles et patates : relief + filtre.
  - Hachures courtes avec un ton qui ondule = chevrons en zigzag : tailles longues, une large bande de lumière, un mince liseré.
  - Vapeur ou fumée par-dessus le sujet = des flammes : dessine-la derrière.
  - Hachures fines + bruit d'encre + grain gonflent le fichier : vérifie un recadrage à 100 % après encodage.

## 7. Son

- **Instruments** : cordes graves (contrebasse, violoncelles ; notes piquées, pizzicato), bois et peaux (tambour de bois, woodblock, tambour sur cadre), grosse caisse, timbales, un seul gong ; un bourdon de vielle pour une couleur populaire.
- **Options** : retenir le timbre de l'objet de l'histoire jusqu'à son apparition ; un bourdon sous une planche fixe.
- **Bruitages** (≈ 5 par 10 s) : **le couteau dans le bois** (attaque + fibres qui se déchirent, lié à la vitesse du couteau), copeaux, rouleau qui colle, air du papier, frottoir, **le décollage humide** ; les métaux selon leur taille (grand = grave).
- **Voix** : peu de phrases, basses et simples, comme des légendes dites. Musique et bruitages baissés sous la voix. Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : filtre de seuil sur une image ; gris ; hachures partout ; fondus ; couleur décorative ; légende sur l'image.

- [ ] Deux valeurs seulement (encre, papier) + une planche de couleur au plus.
- [ ] La couleur n'apparaît que dans des zones taillées, sur une seule chose.
- [ ] Les tailles suivent la forme ; leur largeur suit la lumière.
- [ ] Tout apparaît par la taille ; aucun fondu.
- [ ] La marge de papier est fixe ; la légende est dans la marge basse.
- [ ] Figures : silhouette noire, halo blanc, peau blanche et traits noirs.
- [ ] Au moins une transition par décollage de la feuille, ou un tirage en miroir révélé.
- [ ] Rien d'important sous y = 1560 ni à droite de x = 945.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Film de démo d'origine *The Bell Founder* (58 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/woodcut.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/woodcut.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/woodcut.jpg · galerie : https://lemomo-ai.github.io/lemo-opuscar/#print-printmaking
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre l'histoire ni les planches.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/woodcut/STYLE.md`, `DEMO.md`, `demo/engine/index.js` (tailler et imprimer), `demo/trans.js` (décollage), `demo/hands.js` (reliefs). Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0.
- Adaptation Flot Web : traduction, mise en page verticale, valeurs hex d'exemple proposées par Flot Web (la source décrit les teintes), numéros du dictionnaire de mouvements, budget de bruitages.
