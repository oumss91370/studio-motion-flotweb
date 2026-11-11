# Île low-poly isométrique

## 1. Identité

- **Nom** : Île low-poly isométrique.
- **Inspiration** : les jeux de construction contemplatifs où bâtir est le spectacle (chaque pièce se pose avec un rebond élastique et un son, des détails poussent tout seuls) et les jeux d'énigmes en géométrie isométrique (palettes pastel, ciels en dégradé, rythme calme, beaucoup de vide). On n'en copie ni les grilles, ni les bâtiments, ni les personnages, ni l'interface, et on ne les nomme pas à l'écran.
- **Ce que c'est** : un monde miniature en **géométrie à facettes** (colonnes hexagonales, maisons-boîtes à toits en prisme, arbres en cônes et en icosaèdres) qui flotte dans une mer à facettes ou dans le vide, vu par une **caméra orthographique** en angle isométrique. Ni perspective ni horizon : le lointain se dissout dans un **dégradé de ciel plaqué à l'écran**, comme une maquette suspendue dans la couleur. **La lumière, pas la texture, dit l'heure** : chaque facette change de couleur quand le soleil tourne ; dans le noir, seuls les blocs lumineux gardent leur couleur.
- **Marche pour** : la première année d'une entreprise, un quartier ou un produit qui se construit pièce par pièce, un réseau qui s'allume, un utilisateur parmi des millions (changement d'échelle par zoom), une journée ou une saison en accéléré.
- **Ne marche pas pour** : personnages et dialogue, texte dense, réalisme, sujet nerveux.
- Ce n'est ni un jeu en voxels, ni une photo tilt-shift (pas de perspective, pas de détail photo), ni un cartoon 3D lissé.

## 2. Palette, typographie, matières

Pastel, peu contrasté, une poignée de teintes. Exemple (démo) :

| Rôle | Hex |
|---|---|
| Sable (dessus / côté) | `#F3DFAB` / `#E2C68E` |
| Herbe | `#93C96C` · `#7FBD62` ; côté terre `#C99C6E` |
| Roche | `#B4B8BD` / `#8F949C` |
| Murs | `#FBF3E6` `#F5C2B0` `#B5DCCB` `#A9CBE8` `#F7DF8F` `#E9C9E6` |
| Toits | `#D9644A` `#4F7FB8` `#E0874F` `#3F8F86` |
| Arbres | pins `#3F8A5A` ; feuillus `#7FC36A` `#9AD06F` |
| Fenêtres allumées | `#FFC676` |

**L'heure est un jeu de couleurs à clés**, interpolé (zénith / horizon / mer profonde / hauts-fonds) :

| Heure | Zénith | Horizon | Mer profonde | Hauts-fonds |
|---|---|---|---|---|
| Aube | `#9FB6CF` | `#F3D2C4` | `#4F8EA3` | `#8FC9C4` |
| Jour | `#88C8E8` | `#EAF5F2` | `#38A5BC` | `#86E2D4` |
| Crépuscule | `#6F6FA8` | `#FFA888` | `#5A6A9E` | `#B08AA6` |
| Nuit | `#12163A` | `#4A4478` | `#23264A` | `#363A66` |

- La nuit et le crépuscule tirent vers le bleu-violet : garde-les **courts** (moins de 30 % du film) et pleins de fenêtres chaudes, ou prévois la dérogation (`styles-jeu-retro/references/derogation-bleu-violet.md`).
- Aucun contour, aucun noir : ombres et occlusion sont les seuls sombres.
- **Typographie** (OFL) : **Quicksand 600** pour les sous-titres ; **Josefin Sans** en capitales très espacées pour les titres.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Quicksand ; Outfit à la place de Josefin Sans. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/quicksand`, `@fontsource/josefin-sans` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : facettes plates, rugosité ≈ 0,9, **aucune texture**. La clarté de chaque tuile varie de ±4 % pour que le sol ne ressemble pas à un tableur. Un petit écart (1,5 %) entre les tuiles : l'occlusion y dessine les joints.

## 3. Composition 9:16

- L'île se cadre au **centre bas** (y 700 à 1400), le dégradé de ciel occupe le haut : en vertical, on a naturellement « beaucoup de vide », c'est le style.
- **La hauteur du cadre orthographique est le zoom** : quelques unités pour un gros plan (une pièce qui arrive), une douzaine pour le monde entier, des centaines pour la révélation d'échelle. Une tuile = une unité.
- Élévation basse (20-25°) : large bande de ciel, étoiles ; élévation haute (≈ 50°) : lecture « carte ».
- Construis **en hauteur** quand c'est possible (phare, tour, colline en gradins) : le format le demande.
- **Sous-titres sans boîte** : blanc chaud avec ombre portée bleu foncé douce, 48 px, centrés vers y 1460 ; à côté, une petite tuile à facettes dont le dessus suit l'heure.
- **Les titres se comportent comme des tuiles** : les lettres montent une à une de sous la ligne d'eau, dépassent et se posent ; entre y 220 et 480.
- Un carton de texte par-dessus le monde laisse une ouverture où le monde reste visible.

## 4. Ce qui bouge

- **Action principale** : **la croissance** : les tuiles montent, les étages s'empilent, les arbres surgissent ; chaque arrivée joue une note.
- **Boucle de fond 1** : mer à facettes (somme de sinus), bateaux qui tanguent avec la même fonction de vague.
- **Boucle de fond 2** : moulin qui tourne, fumée en bouffées, oiseaux qui tournent en rond.
- **Autorisés** : `#010` dépassement, `#123` rebond, `#011` écrasement à volume constant sur les pièces qui tombent, `#001` surgissement (arbres, lampes : ≈ 25 % de dépassement), `#002` arrivées en cascade sur la grille musicale, `#030` orbite en plateau tournant, `#028` zoom orthographique pur, `#039` accéléré du soleil caméra fixe, `#175` plan fixe de trois quarts, `#046` coupe sèche sur le temps.
- **Interdits** : toute perspective et tout changement de focale (**la projection ne bouge jamais**), `#044` fondu enchaîné, `#043` panoramique filé, contours, textures, grain (les aplats scintillent avec du grain), saccade d'animation.
- Courbes d'arrivée :
  - **monter d'en dessous** : montée de 0,5 s, puis dépassement en sinus amorti ; anneau d'éclaboussure à la sortie de l'eau ;
  - **tomber et s'empiler** : chute rapide accélérée (0,22 s), rebond amorti, écrasement puis étirement ;
  - **surgir** : échelle `1 − e^(−9s) · cos(17s)`.

## 5. Rythme et montage

- Mouvement fluide à pleine cadence ; le charme est dans les **courbes d'arrivée**.
- **Programme la croissance sur la grille musicale** : au plus une pièce par plus petite case, pour que chaque évènement garde sa note. On accélère par la **densité** (blanches → noires → croches), pas par le tempo.
- Alterne plan large et gros plan sur les temps : le large montre la forme qui grandit, le gros plan vend le rebond.
- Transitions : coupe sèche sur le temps, changement d'heure, zoom à travers le ciel.
- **Construire, c'est composer** : un balayage final peut rejouer les notes dans l'ordre de l'espace, comme une mélodie achevée.
- Durée conseillée : 20 à 45 s.
- **Version courte (8 à 12 s)** : une seule heure du jour : la croissance (tuiles, étages, arbres) en 6 s, puis 2 s de tenue ; couper le changement d'heure.

## 6. Recette technique

**Moteur conseillé : Three.js** : pas de textures, pas de reflets, géométrie simple, évènements très nombreux à caler sur la musique. **Blender** (connecteur MCP `blender`) si l'on veut une mer et une lumière plus riches ou une île très détaillée.

| | Three.js (conseillé) | Blender |
|---|---|---|
| Géométrie | `CylinderGeometry(r, r, h, 6)`, boîtes, prismes, cônes, icosaèdres, `flatShading: true` | mêmes primitives en Python, ombrage plat |
| Caméra | `OrthographicCamera` ; la hauteur du cadre fait le zoom | caméra orthographique, échelle animée |
| Joints entre tuiles | **occlusion ambiante en passe, obligatoire** | donnée par le rendu |
| Ciel sans horizon | passe d'écran : profondeur linéarisée, fondu des lointains dans un dégradé vertical | brume de profondeur au compositeur + dégradé de fond |
| Évènements sonores | exportés directement depuis le planning de croissance | à exporter à part depuis le script |
| Coût | rapide ; rendu 2× puis réduction | plus long, peu de gain visible |

- **Structure** : `monde` (pavage hexagonal, accessoires, planning de croissance → évènements avec notes, courbes d'arrivée), `mer` (vagues à facettes, carte des hauts-fonds), `finition` (occlusion → ciel et brume → léger flou de bord → lueur → étalonnage pastel), `recit` (grille de temps, clés d'heure, plans).
- **Techniques clés** :
  ```js
  // pavage hexagonal « pointe en haut » : coordonnées axiales (q, r) -> monde
  const x = Math.sqrt(3) * (q + r / 2), z = 1.5 * r;
  // arrivée par en dessous (s = secondes depuis le départ)
  const u = Math.min(1, s / 0.5);                       // montée de 0,5 s, ralentie à la fin
  const v = Math.max(0, s - 0.5);                       // puis dépassement amorti
  const y = h * (1 - (1 - u) ** 3) + 0.18 * Math.sin(13 * v) * Math.exp(-7 * v);
  ```
  - Un mince **chapeau** séparé au-dessus d'une colonne de côté plus foncée ; **enfonce le haut de la colonne sous le chapeau**, sinon les deux surfaces se battent.
  - Parties lumineuses (fenêtres, lampes) : un matériau par objet, pour les allumer une à une.
  - Caméra à **au moins 3 fois la hauteur du cadre** de distance, sinon le bas de l'image passe sous la mer.
  - Soleil de côté par rapport à la caméra dans les plans clés : un soleil bas derrière la cible change la mer à facettes en éblouissement.
- **Pièges** : en orthographique, la profondeur ne se convertit pas comme en perspective (utilise la conversion orthographique dans la finition) ; l'occlusion rend les objets transparents comme des carrés pleins (cache-les pendant cette passe) ; un cône lumineux à deux faces se lit comme deux traits blancs (ruban face caméra à profil doux + halo) ; deux pièces dans la même case de temps brouillent la mélodie.

## 7. Son

- **La musique peut naître des évènements** : chaque arrivée porte une note, jouée à son instant exact : l'image écrit l'air. Percussions accordées : marimba, kalimba, woodblock, cloches, vibraphone, célesta, steel-drum ; dessous, une nappe douce, un ostinato léger. Gamme pentatonique ou modale : n'importe quel ordre de notes reste harmonieux. **Ni piano ni cordes.**
- **Une seule note peut être un motif** : un son qui appartient au monde (une cloche, une corne) et qui revient changé.
- **Bruitages selon la matière** (≈ 5 par 10 s après tri ; les arrivées trop nombreuses sont portées par les notes) : bulles et éclaboussure pour une tuile qui monte (plus grosse = plus grave), coup de bois pour un étage, claquement de céramique pour un toit, « tink » de verre, choc sourd de pierre.
- **Lits** : eau, oiseaux, bois qui craque, grillons ou vent la nuit. Voix douce et claire, peu de phrases. −14 LUFS, **aucun grain**.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Caméra orthographique : aucune ligne de fuite, aucun horizon.
- [ ] Facettes plates partout ; aucune texture, aucun contour, aucun noir.
- [ ] Les joints entre tuiles se voient (occlusion).
- [ ] Chaque pièce arrive avec un dépassement ou un rebond, sur un temps, avec sa note.
- [ ] Jamais deux arrivées dans la même case de la grille.
- [ ] L'heure se lit par la couleur des facettes ; la nuit, seuls les blocs lumineux sont vifs.
- [ ] Le lointain se fond dans un dégradé de ciel ; le bas de l'image ne passe pas sous la mer.
- [ ] Part de nuit et de crépuscule mesurée (interdit bleu-violet) ; aucun bâtiment ni personnage d'un jeu existant.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 16
- Bleu-violet : dérogation
- Texte vivant : non
- Taille mini du texte : 48

## 9. Aperçu

- Film de démo d'origine *The Island That Grew* (53 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/lowpoly-island.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/lowpoly-island.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/lowpoly-island/STYLE.md`, `DEMO.md`, `demo/world.js`, `sea.js`, `post.js`, `story.js`, `main.js`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Polices Quicksand, Josefin Sans (SIL OFL 1.1).
- Simulations three.js pilotées par le temps (contrat « l'image est une fonction du temps », relecture par planche d'images à chaque temps fort) : whaleyxbt/claude-motion, commit `6f80380`, `.claude/skills/web-sims/SKILL.md`, licence MIT, © 2026 whaleyxbt.
- Adaptation Flot Web : traduction, composition 9:16, tableau des moteurs (voie Blender non testée), mise en garde bleu-violet, numéros du dictionnaire.
