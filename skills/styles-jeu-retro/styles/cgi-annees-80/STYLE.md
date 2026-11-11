# Images de synthèse des années 80

## 1. Identité

- **Nom** : Images de synthèse des années 80 (premiers rendus par lancer de rayons).
- **Inspiration** : les démonstrations d'images de synthèse de la fin des années 80 et du début des années 90 : tout est en plastique brillant, le sol est un damier qui se reflète, une sphère chromée trône quelque part, le terrain apparaît d'abord en fil de fer. Époque collective : aucun film, logo ou personnage précis n'est repris.
- **Ce que c'est** : un monde de **jouets en plastique uniforme** : chaque forme a un reflet blanc dur, un bord assombri, un reflet de couleur venu du mur ; **damier en perspective** avec reflets des objets, **sphère chromée** qui reflète le damier et le ciel, **anneau de billes** qui tourne, **reflet d'objectif** à étoiles, ciel en dégradé rose-violet-orange, montagnes en fil de fer.
- **Marche pour** : clin d'œil à l'histoire de l'informatique, logo ou objet « rendu » façon rétro, générique d'émission techno, anniversaire d'une entreprise du numérique, humour nostalgique.
- **Ne marche pas pour** : personnages attachants (ils ont des jambes en poteaux et un visage de masque : c'est le défaut connu du style), émotion, produit réaliste, élégance contemporaine.
- **État de la source** : carte notée ★★ par son auteur. Le style est solide sur les **objets** ; évite les personnages ou assume le côté pantin articulé (rotules sphériques aux épaules et aux genoux).

## 2. Palette, typographie, matières

| Rôle | Hex |
|---|---|
| Mur (dégradé radial depuis la fenêtre) | `#7DBCB9` → `#64A6A6` → `#3F8285` |
| Ciel (du haut vers l'horizon) | `#A24CC4` → `#DF62AE` → `#F5A08A` → `#F8C070` |
| Bord sombre du plastique | `rgba(10, 0, 30, 0.42)` |
| Reflet d'ambiance (couleur du mur) | `rgba(70, 150, 150, 0.28)` |
| Fil de fer (transition) | vert phosphore `#35FF6A` (indicatif) |
| Damier | deux tons (blanc cassé et bleu ou noir) |
| Plastiques | couleurs primaires saturées : rouge, bleu, jaune, vert |

- Le ciel violet-rose n'occupe qu'une fenêtre ou un bandeau : le film reste en général sous le seuil bleu-violet. S'il domine, applique `../../references/derogation-bleu-violet.md`.
- **Typographie** : une linéale géométrique en capitales, extrudée ou chromée pour un titre (par exemple **Orbitron** ou **Michroma**, OFL) ; textes d'information en police à chasse fixe (**VT323**, OFL), vert ou blanc, façon console.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Outfit à la place d'Orbitron et de Michroma ; Space Mono à la place de VT323. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/orbitron`, `@fontsource/michroma`, `@fontsource/vt323` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers, sauf mention ci-après) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. Attention : Orbitron : sans guillemets « » : s'en passer dans les titres.
- **Matières** : plastique brillant (partout), chrome (une sphère, un titre), verre teinté (un plateau translucide vert à bord épais, avec un reflet oblique qui glisse). Rien de mat, rien de texturé, pas de saleté.

## 3. Composition 9:16

- **Damier en perspective** sur la moitié basse (y 960 à 1920), point de fuite au centre (x 540, y ≈ 860), léger brouillard vers le fond.
- **Objet héros** posé sur le damier entre y 700 et 1350, au moins 1/3 de la hauteur, avec son reflet inversé et atténué en dessous (≈ 34 % d'opacité).
- **Sphère chromée** (160 à 220 px) et **anneau de billes** en accessoires, de part et d'autre du héros, jamais à droite de x 945.
- Fenêtre ou bandeau de ciel en haut (y 200 à 700) : dégradé, montagnes à grille filaire rose, soleil avec reflet d'objectif.
- Titre chromé en haut (y 220 à 420), 110 à 150 px. Texte d'information en bas à gauche vers y 1450, à chasse fixe, 40 px.
- 16:9 : damier sur le tiers bas, objets répartis en largeur.

## 4. Ce qui bouge

- **Action principale** : l'objet héros **tourne lentement sur lui-même** ou la caméra tourne autour, pour que reflets et damier glissent.
- **Boucle de fond 1** : **anneau de 140 billes** qui tourne autour d'un axe vertical incliné (≈ 7 rad/s dans la source ; ralentis à 2 ou 3 rad/s pour un plan long).
- **Boucle de fond 2** : sphère chromée dont le reflet du damier défile ; reflet d'objectif qui pulse (cœur ±8 %, 12 branches qui tournent lentement, 5 images fantômes alignées du soleil vers le centre).
- **Autorisés** : `#030` orbite, `#027` avancée lente, `#022` balayage de lumière (reflet oblique sur le verre), `#109` reflet d'objectif, `#176` survol, `#021` retournement, `#139` transition en cube, `#143` vue éclatée lente.
- **Interdits** : `#011` écrasement et étirement, `#136` trait qui frémit, `#034` caméra à l'épaule, grain, textures, flou de profondeur de champ (tout est net, comme à l'époque), `#046` coupes nerveuses.
- Les mouvements sont **mécaniques** : vitesse constante ou accélération simple, pas de rebond.

## 5. Rythme et montage

- Plans de 4 à 8 s, lents et démonstratifs : on laisse le temps de voir les reflets.
- **Transition signature : fil de fer vert → rendu.** La nouvelle image apparaît d'abord en contours verts sur fond noir, puis se « remplit ». La première image du plan doit donc être complète : ne commence jamais un plan par un fondu ou un écran vide.
- Ouverture possible : une ligne de texte de console (« RENDU EN COURS… 98 % »), puis l'image.
- Durée conseillée : 10 à 30 s.
- **Version courte (8 à 12 s)** : un plan de 8 à 10 s : l'objet tourne dès l'image 0, un reflet le balaie avant 3 s (c'est l'accroche), le titre chromé tient 2 s.

## 6. Recette technique

**Moteur conseillé : HyperFrames en faux 3D** (canvas 2D avec des conventions d'ombrage) pour un plan fixe ; **Three.js** dès que la caméra tourne ; **Blender** (connecteur MCP `blender`) pour un plan héros avec de vrais reflets.

| | Faux 3D canvas (HyperFrames) | Three.js (léger) | Blender (qualité) |
|---|---|---|---|
| Quand | plan fixe, objets simples | orbite, anneau, logo qui tourne | reflets et réfractions exacts, objet du client |
| Plastique | dégradé radial + reflet dur dessinés à la main | `MeshPhongMaterial`, brillance élevée (c'est le modèle d'époque) | Principled lisse (rugosité ≈ 0,15), pas de texture |
| Damier et reflets | damier calculé pixel par pixel, objets redessinés à l'envers à 34 % | plan en damier + `Reflector` ou carte d'environnement | lancer de rayons de Cycles : gratuits et exacts |
| Chrome | carte d'environnement calculée par pixel (bas → damier, haut → ciel) | `MeshStandardMaterial` métal 1, rugosité 0 | métal 1, rugosité 0 |
| Risque | perspective à tenir à la main | rendu trop propre : couper l'anticrénelage fin, pas d'ombres douces | rendu trop réaliste : garder une seule lumière dure, pas d'illumination globale douce |

- **Techniques clés (faux 3D)** :
  ```js
  // plastique : 1 fond, 2 dégradé radial centré sur le point de reflet (hx, hy), rayon R
  //   0 -> blanc .55 ; 0.28 -> blanc .06 ; 0.62 -> transparent ; 1 -> rgba(10,0,30,.42)
  // 3 reflet d'ambiance : contour en addition, rgba(70,150,150,.28), largeur 0.18 R
  // 4 reflet dur : ellipse blanche 0.16 R x 0.09 R, opacité .85  (le détail le plus « d'époque »)
  ```
  - Membre cylindrique : dégradé en travers (sombre → bande blanche étroite à 22 % → sombre) + un fin trait blanc.
  - Damier : pour chaque pixel sous l'horizon, `X = (x − cx) / dy`, `Z = 1 / dy`, parité des cases ; suréchantillonné 2×2 ; mis en cache.
  - Reflets au sol : dessine les objets sur un calque, retourne-le autour de la ligne de contact de chacun, **puis** applique l'opacité au calque entier (sinon 140 billes à 34 % chacune redeviennent opaques).
  - Anneau : billes triées par profondeur, une sous-couche sombre pour qu'elles forment un tube.
- **Pièges** : corps en segments droits qui trahit les arêtes (lisse les contours avant d'ombrer) ; rayures « imprimées sous le plastique » trop nettes (floute-les de 2 px) ; lueur additive qui brûle l'image ; en Three.js ou Blender, la tentation d'ajouter des matières modernes.

## 7. Son

- **Musique** : synthétiseurs numériques d'époque (cloches FM, basse FM, nappes vitreuses), tempo modéré, mélodie simple et optimiste ; ou un silence de salle de machines.
- **Bruitages** (≈ 3 à 5 par 10 s) : ronflement d'ordinateur, bip de fin de rendu, lecteur de disquette, ventilateur, carillon de verre pour un reflet, vrombissement grave de l'anneau.
- **Voix** (option) : présentateur de démonstration technique, posé, un peu solennel. −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : matières réalistes, ombres douces, flou d'arrière-plan, personnage central attachant, mouvement élastique, plan qui commence par du vide.

- [ ] Chaque objet porte un reflet blanc dur et un bord assombri.
- [ ] Le sol est un damier en perspective avec le reflet des objets.
- [ ] Une sphère chromée reflète damier et ciel, et ce reflet bouge.
- [ ] Au moins un élément tourne en continu à vitesse constante.
- [ ] Aucune texture, aucun grain, aucun flou de profondeur.
- [ ] Une transition « fil de fer → rendu », ou un plan d'ouverture en fil de fer.
- [ ] Part d'images bleu-violet mesurée ; dérogation préparée si le ciel domine.
- [ ] Aucun logo, film ou personnage d'époque repris.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 8
- Bleu-violet : dérogation
- Texte vivant : non
- Taille mini du texte : 40

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt d'origine. Planche commune : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg (© 花叔 Huashu ; à consulter, pas à réutiliser en vitrine).
- Aperçu à produire par un rendu réel 9:16 avec le plugin.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/15_raytrace.md` (carte traduite du chinois), `scripts/engine/scenes/15_raytrace.js`. Licence MIT, © 花叔 Huashu.
- Voies Three.js et Blender : propositions de Flot Web (non décrites par la source, non testées par un rendu) ; connecteur ahujasid/mcp-for-blender, commit `2e4b0bc`, MIT.
- Adaptation Flot Web : traduction, nom descriptif, composition 9:16, tableau des moteurs, sections rythme et son, numéros du dictionnaire. Le vert du fil de fer et les polices proposées sont des choix de Flot Web.
