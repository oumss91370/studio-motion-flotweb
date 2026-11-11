# Lanterne de papier découpé

## 1. Identité

- **Nom** : Lanterne de papier découpé (boîte à ombres rétroéclairée, « Paper-cut Lightbox »).
- **Inspiration** : les lampes en papier sculpté du commerce (un empilement de feuilles découpées dans un cadre, éclairé par derrière), les films de silhouettes articulées des années 1920 (quand il y a des personnages), et les motifs du découpage chinois (nuages, avant-toits, montagnes) comme vocabulaire possible. Aucun modèle de lampe, aucune image de film, aucun personnage recopié.
- **Ce que c'est** : chaque plan est fait d'**un seul objet physique** : une boîte peu profonde (cavité d'environ 56 × 33 cm, 16 cm de profondeur en paysage) qui contient des feuilles de papier découpé parallèles. Tout ce qu'on voit est l'une de ces trois choses :
  1. **Une couche de papier** : une feuille plate d'une seule couleur, avec son grain, un **mince liseré de lumière sur son bord haut** et une **bande sombre sur son bord bas**. Couches du fond claires et froides, celle de devant presque noire : cette **échelle de valeurs est la profondeur**.
  2. **La lumière à travers le papier** : translucidité chaude et nuageuse, plus forte près de la source. Fenêtres, lanternes, traînées de lumière sont des **trous** qui brûlent et rayonnent.
  3. **Les ombres** : une lampe en haut projette des **ombres douces** de chaque couche sur celles de derrière. C'est ce qui vend « du vrai papier dans une vraie boîte » : ne les coupe jamais.
- Deux cadrages valides : **boîte dans le cadre** (on voit le bord de la lampe) et **plein cadre** (l'objectif est dans la boîte).
- **Marche pour** : souvenir, histoire du soir, deux lieux reliés par une même lumière, voyage de nuit, anniversaire, objet qu'on garde, ouverture d'une boutique à l'aube.
- **Ne marche pas pour** : plein jour cru, explication, humour vif, interface, mouvement rapide.
- **À ne pas confondre** : pas du papier découpé à plat (ici : profondeur, contre-jour, ombres portées) ; pas des ombres chinoises (pas d'écran unique, pas de tiges) ; pas un diorama 3D (chaque élément est une feuille plate parallèle à la face de la boîte).

## 2. Palette, typographie, matières

Échelles de valeurs d'exemple, du ciel vers l'avant :

| Scène | Ciel → lointain → milieu → avant | Lumière / accent |
|---|---|---|
| Village la nuit | `#0a1330` → `#6a86c2` → `#3f5a92` → `#0e1532` | fenêtres `#ffb862` |
| Caravane au désert | `#f0c890` → `#c07850` → `#6a3020` → `#1e0e08` | feux `#ffd080` |
| Forêt d'hiver | `#dfe6ee` → `#9aaec4` → `#4a6078` → `#101820` | une écharpe rouge |

- **Fond clair et translucide, avant sombre et opaque** : ne casse jamais cette échelle (une couche pâle devant aplatit la boîte).
- **Une température par empilement** ; changer d'échelle, c'est dire « un autre lieu ».
- **La lumière est chaude** (ambre à or) et c'est le seul élément saturé, avec **un accent** (un rouge de sceau, la couleur d'un objet). Un second accent seulement si l'histoire a deux camps.
- **Attention** : l'échelle « village la nuit » est bleue ; garde les bleus sombres et peu saturés et laisse la lumière chaude occuper une vraie part du cadre.
- **Typographie** : **le texte dans l'image est du papier** : titres et lettres sont des bandes découpées dans la boîte, qui poussent depuis un bord d'ancrage. Serif libre (**Cormorant**, OFL). **Un mot qui apparaît en papier n'est pas sous-titré** : jamais les mêmes mots deux fois.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de Cormorant. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/cormorant` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : grain de fibres sur chaque feuille ; translucidité par couche de ≈ 0,9 (fond) à ≈ 0,05 (avant) ; texture de pâte nuageuse dans la lumière ; faible profondeur de champ, halo, léger vignettage.

## 3. Composition 9:16

- En vertical, **tourne la boîte** : cavité d'environ 33 × 56 cm, 16 cm de profondeur, 6 à 9 feuilles de z = −0,14 m (ciel) à 0 (avant). Caméra à 0,2 à 0,56 m, focale longue (champ ≈ 26° sur le petit côté).
- Le vertical convient très bien à un **empilement en hauteur** : ciel et lune (haut), montagnes ou toits, rue, sol sombre (bas). La couche avant, presque noire, occupe naturellement le bas : c'est là que vont les sous-titres.
- **La couche de l'histoire est nette** ; avant-plan et lointain sont doux. Les bords de la boîte sont **entièrement hors cadre** (dedans) ou **clairement dans le cadre** (dehors), jamais à moitié.
- En cadrage « boîte », les feuilles ne dépassent **jamais** la cavité. En plein cadre qui voyage, une couche peut être une longue bande qui défile, et le panneau de ciel suit la caméra.
- **Sous-titres** : serif blanc chaud 46 à 52 px, ombre douce, sur la bande la plus sombre du bas (y ≈ 1400 à 1520), jamais sur une figure, une fenêtre éclairée ou une lumière ; une bande sombre très légère derrière est permise. Pas de retour à la ligne : une ligne trop longue devient deux sous-titres. Tenue ≥ max(1,8 s ; réplique + 0,6 s).
- Tout point lumineux reste à l'écart du texte en papier (la lumière lave les lettres).

## 4. Ce qui bouge

- **Action principale** : **les lumières sont le grand mouvement** : la source d'abord, puis la translucidité de chaque couche avec un décalage de ≈ 0,4 s, puis les fenêtres une à une, puis un léger scintillement (`1 + 0,06·sin(7,3·t)·sin(3,1·t)`).
- **Boucle de fond 1** : micro-dérive de caméra à main levée (≈ 0,6 mm) : un plan fixe reste vivant.
- **Boucle de fond 2** : couches qui glissent à des vitesses proportionnelles à leur profondeur (voyage), scintillement des fenêtres.
- **Tout bouge comme du papier sur une baguette** : les couches glissent, tournent autour d'un pivot, **poussent depuis zéro le long d'un axe** (« s'écrivent »), ou s'allument. Les personnages sont **facultatifs** (fenêtres, véhicules, lampes suffisent) ; s'il y en a, ce sont des silhouettes articulées : une feuille de corps + des feuilles de membres ancrées à l'articulation, **en rotation seulement**.
- **Gestes natifs** : la lampe s'allume ; deux fenêtres, une lumière ; la profondeur comme distance ; le papier qui s'écrit sur le mot prononcé ; la boîte comme souvenir (la caméra trouve la vraie lampe dans une pièce) ; l'éclat de lumière d'une chose qu'on ouvre ; une silhouette dans une fenêtre.
- **Autorisés** : `#027` avancée lente presque frontale, `#028` recul lent, `#033` bascule de mise au point entre couches, `#029` travelling latéral avec parallaxe, `#016` parallaxe, `#181` vue du dessus de l'empilement, `#026` panoramique vertical, `#175` plan fixe où seule la lumière change, `#044` fondu (ici permis, 0,5 à 1,2 s), `#188` iris, `#034` très léger tremblé de main.
- **Interdits** : `#011` écrasement et étirement, `#012` métamorphose, pliage du papier, `#043` panoramique filé, zoom numérique, saccadé (tout est fluide à 30 i/s), ombres coupées.

## 5. Rythme et montage

- Lent : plans de 5 à 9 s ; **mouvements courts** (l'objectif est petit, la boîte peu profonde).
- Les actions franches tombent **sur les mots prononcés** (un objet claque, une lumière s'allume sur son mot).
- Transitions : fondu, iris, lumière éteinte puis rallumée, **rideau de premier plan** dont les deux moitiés se rejoignent exactement.
- Silence = la lampe éteinte : tout sauf un ton de pièce disparaît, puis revient avec la lumière.
- **Version courte (8 à 12 s)** : un plan : la source s'allume avant 2 s, puis les couches et deux fenêtres ; un second plan court seulement si l'histoire l'exige ; couper le rideau de premier plan et le silence « lampe éteinte ». L'accroche est l'allumage, pas une coupe.

## 6. Recette technique

- **Moteur recommandé : Blender** (connecteur MCP, skill `blender`) : c'est un vrai objet avec de vraies ombres douces et une vraie profondeur de champ.
  - Chaque feuille = un plan avec une image découpée (canal alpha) ; matériau : couleur plate + grain, **translucidité** réglée par couche, un peu de diffusion.
  - Une lumière de zone **derrière** l'empilement (chaude), une lampe **en haut** qui projette les ombres douces, émission pour les fenêtres (pilotée par une valeur 0 → 1 « allumé »).
  - Caméra à focale longue, faible profondeur de champ avec mise au point animée ; halo et vignettage en composition.
  - Les découpes se dessinent en SVG ou sur un canvas 2D (trous francs), puis s'importent comme textures.
  - Rends la séquence d'images, puis monte texte et sous-titres dans HyperFrames.
- **Variante légère : Three.js dans HyperFrames** (comme l'original) : plans texturés par des canvas 2D, un shader de contre-jour, ombres douces, profondeur de champ et halo en post-traitement, rendu en double résolution.
  ```glsl
  // contre-jour d'une feuille
  emissif += albedo * couleurLumiere * translucidite * allume * decroissance * (base + nuage);
  ```
- **Structure** (variante Three.js ; fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `feuille.js` (une couche éclairée, carte de lueur, uniformes de révélation), `scene.js` (lampe du haut, contre-jour, caméra), `post.js` (profondeur de champ, halo, transitions, étalonnage), `motifs.js`, `plans.js` (chaque plan : construction, mise à jour, étalonnage).
- **Pièges** :
  - Un trou percé avec une couleur semi-transparente est à moitié coupé : couleur **opaque** avant de percer.
  - Les ombres douces bavent : une couche qui ne doit pas participer doit ne **ni projeter ni recevoir**.
  - Une lueur faite d'un dégradé radial sur une image transparente montre un bord carré : fais la lueur par le calcul.
  - Rideau dont les moitiés ne se rejoignent pas à leur bord avant : une fente montre l'ancien plan.
  - **L'étalonnage ne doit pas se transmettre d'un plan à l'autre** : chaque réglage absent revient à sa valeur par défaut à chaque image, sinon le rendu dépend de l'ordre de calcul.
  - Sous-titres sur une fenêtre éclairée : contraste perdu.

## 7. Son

- **Instruments** qui se posent comme une lumière derrière du papier : piano feutré, boîte à musique, célesta, harpe ou cithares pincées, flûtes de bambou, cordes douces ; un instrument soliste de la culture du sujet. Pas de batterie ; percussion seulement en coups isolés et doux.
- **Bruitages : papier et lumière** (≈ 5 par 10 s) : clic d'interrupteur + scintillement qui monte quand une lumière s'allume, froissement et glissement de papier, tape de carton, couvercle, carillon sur une révélation, souffle doux pour un rideau ; ambiance de la scène (rivière, rails, ville, grillons, vent de neige).
- **Voix** : chaleureuse, un conteur à table, pas un annonceur ; devant, musique baissée de 5 à 6 dB sous la parole. Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : couches sans ombres ; avant-plan clair ; papier qui se tord ; lumière froide ; bord de boîte coupé à moitié ; texte doublé (papier + sous-titre).

- [ ] 6 à 9 couches, de claires et translucides au fond à presque noires devant.
- [ ] Chaque couche a son liseré clair en haut, sa bande sombre en bas et projette une ombre douce.
- [ ] La lumière est chaude ; les fenêtres rayonnent ; un seul accent.
- [ ] Les lumières s'allument en cascade (source, couches, fenêtres).
- [ ] La mise au point désigne la couche de l'histoire.
- [ ] Rien ne s'écrase ni ne se déforme : glissement, rotation, pousse, allumage.
- [ ] Sous-titres sur la bande sombre du bas, hors y > 1560 ; aucun mot en double.
- [ ] Le bord de la boîte est soit absent, soit nettement visible.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Film de démo d'origine *The Last Night Train* (51 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/paper-lantern.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/paper-lantern.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/paper-lantern.jpg · galerie : https://lemomo-ai.github.io/lemo-opuscar/#east-asian-traditions
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre l'histoire (un train de nuit), ses plans ni ses accessoires.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/paper-lantern/STYLE.md`, `DEMO.md`, `demo/src/paper.js`, `stage.js`, `post.js`, `world.js`, `shots.js`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0.
- Adaptation Flot Web : traduction, boîte tournée pour le vertical, **voie Blender ajoutée** (l'original est en three.js), numéros du dictionnaire de mouvements, règles de texte en français seul.
