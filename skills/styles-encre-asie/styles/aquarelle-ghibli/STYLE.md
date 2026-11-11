# Aquarelle d'animation (style Ghibli)

## 1. Identité

- **Nom** : Aquarelle d'animation (style Ghibli). « Style Ghibli » est un repère d'inspiration : aucun personnage, décor ou plan de film n'est repris, le nom n'apparaît jamais dans la vidéo, et le style n'est jamais présenté comme officiel ou affilié.
- **Inspiration** : les longs métrages d'animation japonais aux décors peints à la main : des intérieurs clairs et habités, une campagne ou une ville observées avec précision, des gestes du quotidien, et le vent partout.
- **Ce que c'est** : **un décor à l'aquarelle lumineuse** (lavis transparents superposés, bord d'eau plus sombre là où le pigment s'est déposé, grain de papier) et **des personnages en deux tons** (une couleur de base, un croissant d'ombre, un trait brun chaud). Ce qui fait le style, plus que la technique :
  1. silhouettes, expressions et gestes clairs ; un décor qui a sa propre observation ;
  2. personnage et décor **compatibles** (même perspective, même direction de lumière, ombre de contact, couleurs accordées), sans avoir la même texture ;
  3. des **gestes de la vie** justes : le poids du corps, l'ordre dans lequel on utilise un objet, la réaction ;
  4. un mouvement d'environnement qui a **une cause** (le vent, la gravité, un contact) ;
  5. un lieu **où l'on pourrait vivre**.
- **Le sujet est libre** : la forêt, la maison de campagne, la jeune fille, le chat, le balai et les gros nuages **ne sont pas obligatoires**. Un atelier de réparation en ville, un arrêt de bus la nuit, une laverie fonctionnent. Et « sentiment de vie » ne veut pas dire lenteur : une scène tendue demande aussi des actions exactes.
- **Marche pour** : quotidien, artisan, boulangerie, ferme, enfance, souvenir, marque douce et sincère, « une journée de… ».
- **Ne marche pas pour** : sujet agressif, technologie froide, données, texte abondant.
- **À ne pas confondre** : `aquarelle-carnet` (catégorie « Peinture et dessin ») n'a pas de personnage ni de trait ; `lumiere-shinkai` est photographique, à ombres franches et reflets d'objectif.

## 2. Palette, typographie, matières

| Rôle | Hex (source) |
|---|---|
| Mur clair : près de la fenêtre → dans le coin | `#fbf3e0` → `#dcc49a` |
| Taches de couleur dans les lavis | jaune chaud, rose, gris-bleu, vert pâle, en alternance, très légers |
| Trait des personnages | brun chaud `#6a4a38` (plus doux que `#4a3428`) |
| Lumière sous les arbres | jaune chaud en taches, mode « écran » |
| Verts de campagne (exemple) | `#8fbf6a`, `#5f9a4f`, `#3f6f4a` |
| Ciel et nuages (exemple) | `#8fc4ea`, blanc `#fdfdf8`, ventre gris-bleu `#b9c8dc` |

- **Les pièces sont claires** : c'est une règle. Des lavis trop chargés donnent un vieux parchemin moisi.
- **Typographie** : sans-serif ronde et calme (**Zen Maru Gothic** ou **Nunito**, OFL) ou serif douce ; blanc cassé avec une ombre brune légère, ou brun sur une zone claire.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Zen Maru Gothic ; Nunito : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/zen-maru-gothic` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** :
  - *Forme d'aquarelle* : le contour de chaque zone est **déformé par déplacement des milieux** (3 passes), puis chaque couche est redéformée un peu : aucun bord n'est droit.
  - *Lavis* : plusieurs couches en multiplication à faible opacité (les pigments transparents se superposent) ; chaque couche trace un fin liseré de sa couleur : en s'additionnant, ces liserés font le **bord d'eau**.
  - Réglages types : grand mur : 5 couches, opacité 0,4, déformation 12 ; tache de couleur : 3 couches, opacité 0,045, déformation 40 ; planche de bois : 3 couches, opacité 0,5, déformation 3, liseré 0,14 ; blancs opaques (cadre de fenêtre, nappe, nuage) : mode normal, opacité 0,9 à 0,95.
  - Lambris et plancher **teintés planche par planche**. Grain de papier fin en multiplication (≈ 30 %) sur tout le décor.
  - *Nuages* : boules blanches opaques, puis ventre gris-bleu limité à leur silhouette.
  - *Personnages* : deux tons + trait de 2,4 px ; puis **un voile d'aquarelle limité à leur silhouette** (grain + taches de couleur très légères) pour qu'ils appartiennent au décor.

## 3. Composition 9:16

- Un lieu **habité** : une fenêtre ou une ouverture qui donne sur l'extérieur (haut du cadre), un plan de travail ou une table (milieu), un sol avec des objets qui racontent (bas).
- En vertical : extérieur lumineux dans le tiers haut (ciel, arbre, colline), personnage au milieu (≥ 1/3 de la hauteur, visage vers y 600 à 900), sol et petits objets en bas.
- Lumière d'un seul côté, cohérente sur le décor **et** le personnage ; une **ombre de contact** sous chaque objet et sous les pieds.
- Laisse respirer : 30 à 40 % de surfaces calmes (mur, ciel).
- Sous-titres 46 à 52 px sur une zone claire unie ou avec ombre brune, y ≈ 1400 à 1520. Rien d'important à droite de x = 945.

## 4. Ce qui bouge

- **Action principale** : un **geste de la vie** décomposé juste : saisir, soulever (le poids), utiliser, reposer, réagir. C'est lui qui porte le style.
- **Boucle de fond 1** : **le vent par rafales** : des voilages dont le bas se gonfle (`q²·(60 + 150·rafale)`, rafale = `0,55 + 0,45·sin(5,4·t + phase)`), plus une petite ondulation ; dehors, des centaines de brins d'herbe dont la phase avance le long de la pente : **on voit une vague de vent traverser la colline** (`0,5 + 0,5·sin(3,1·t − 0,018·x)`).
- **Boucle de fond 2** : nuages qui dérivent (22 à 30 px/s), cime d'arbre qui se balance (±0,025 rad), **taches de soleil sous les feuilles** (une trentaine, qui dérivent et scintillent), fleurs qui hochent, cheveux et rubans dans le vent, bord de nappe qui bouge.
- **Autorisés** : `#096` flottement, `#016` parallaxe douce, `#027` avancée lente, `#025` panoramique lent, `#031` grue qui monte vers le ciel, `#121` anticipation, `#122` suivi (cheveux, tissu), `#175` plan fixe, `#103` lumière dorée.
- **Interdits** : bords d'aquarelle qui frémissent (les lavis ont des graines fixes), `#023` glitch, `#024` secousse gratuite, `#022` balayage de lumière, dégradés numériques lisses, un même dessin de personnage simplement déplacé pour faire un demi-tour ou une interaction (il faut de vraies poses).
- **Transition signature** : le papier mouillé qui s'étale (la couleur de la scène suivante fleurit depuis un point).

## 5. Rythme et montage

- Calme mais **précis** : plans de 4 à 8 s. Un plan = un geste complet, avec son temps de réaction.
- Un plan « de respiration » sans personnage (le vent dans l'herbe, un nuage) entre deux actions : c'est une signature.
- Personnages à 15 dessins par seconde (à 30 i/s : une image sur deux ; 12 seulement dans un film livré à 24 i/s) ; décor, vent et caméra fluides.
- Coupes franches douces ; la transition par lavis pour un changement de lieu ou de temps.
- **Version courte (8 à 12 s)** : un plan de respiration de 2 s, puis **un geste complet** de 6 à 8 s (saisir, soulever, reposer, réagir) ; couper la transition par lavis. Accroche avant 3 s : le vent bouge dès l'image 0 et le personnage entre avant la troisième seconde.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D. Le décor à l'aquarelle se calcule une fois (≈ 0,6 s) et se met en cache ; ensuite ≈ 17 ms par image.
- **Méthode** : pars de **l'espace et de la lumière** de la scène ; dessine le personnage à part (proportions, silhouette, expressions) ; fabrique ses poses avec le skill `personnages` ; assemble.
- **Techniques clés** :
  ```js
  // lavis : contour déformé, couches en multiplication, liseré qui s'accumule
  function lavis(g, pts, couleur, { couches = 5, alpha = 0.4, amp = 12, bord = 0.1, graine }) {
    const base = deformer(pts, 3, amp, graine);
    g.globalCompositeOperation = "multiply";
    for (let i = 0; i < couches; i++) {
      const p = deformer(base, 2, amp * 0.5, graine + i);
      remplir(g, p, couleur, alpha / couches * 2); tracer(g, p, couleur, bord, 1.6);
    }
  }
  // personnage en deux tons : remplir en ombre, puis recopier la base décalée vers la lumière
  function deuxTons(c, forme, base, ombre, dx, dy) { /* reste un croissant d'ombre côté opposé */ }
  ```
- **Pièges** :
  - **« Le décor est réussi, le personnage est un vecteur plat »** : c'est le défaut connu. Ajoute le voile d'aquarelle limité à la silhouette, adoucis le trait, donne une ombre de contact.
  - Taches de couleur trop fortes (opacité 0,07 × 4 couches) + grain à 50 % : mur moisi. Reste à 0,045 × 3, et éclaircis.
  - Deux rectangles de lavis juxtaposés font une couture nette : assombris avec de grandes formes très déformées, jamais des rectangles.
  - Voilage qui « ne flotte pas » : augmente la fréquence des rafales et l'amplitude du gonflement.
  - Multiplier tout le personnage par un grain de papier ne suffit pas à l'intégrer.

## 7. Son

- **Ambiance d'abord** : c'est un style d'ambiances : vent dans les feuilles, cigales ou oiseaux, bois de la maison, ville lointaine, pluie.
- **Musique** : piano simple, cordes chaleureuses, bois (hautbois, clarinette), accordéon ou guitare ; mélodie chantable, tempo de marche tranquille. Sais aussi t'en passer : un plan de respiration peut n'avoir que le vent.
- **Bruitages** (≈ 5 par 10 s) : des sons **d'objets vrais**, précis et proches : porcelaine, pas sur le plancher, tissu, eau qui coule, outil ; chacun au moment exact du contact.
- Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défaut connu de la source (deux étoiles) : **les personnages sont moins bons que le décor**. La carte précise aussi que sa scène prouve une technique de décor, pas « tout le style ». Erreurs : pièce sombre ; lavis sales ; gestes vagues ; personnage qui glisse ; décor-carte postale sans usage.

- [ ] Le décor est clair ; les lavis ont un bord d'eau visible et aucun bord droit.
- [ ] Personnage en deux tons, trait brun, voile d'aquarelle, ombre de contact.
- [ ] Même direction de lumière sur le décor et le personnage.
- [ ] Le geste principal a ses étapes (saisir, poids, usage, réaction).
- [ ] Le vent est visible dans au moins trois éléments, par rafales.
- [ ] Un plan de respiration sans personnage.
- [ ] Les bords d'aquarelle ne frémissent pas.
- [ ] Aucun personnage, décor ou objet emblématique d'un film ; aucun nom de studio à l'image.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 10
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt. Planche commune `assets/全风格总览.jpg` : composition empruntée, à ne pas utiliser comme vitrine. Film complet : Releases de https://github.com/alchaincyf/huashu-art-motion. Images fixes possibles avec le moteur d'origine (`render.py --solo 25_ghibli --stills` ; scène d'étude en ville : `--film style_studies --solo 54_ghibli_lab` ; non exécutés ici).
- À produire : notre propre aperçu 9:16, sur un lieu qui n'est ni une forêt ni une chambre.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/25_ghibli.md` (décor à l'aquarelle noté deux étoiles ; étude du langage d'ensemble encore « à valider » selon l'auteur), `scripts/engine/scenes/25_ghibli.js`, `54_ghibli_lab.js`. Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : carte traduite et généralisée ; les clins d'œil à un film précis (nœud rouge, balai) ne sont pas repris ; section 9:16, numéros du dictionnaire de mouvements, son.
