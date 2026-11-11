# Comics cosmique (style Kirby)

## 1. Identité

- **Nom** : Comics cosmique. Pour se comprendre avec le client : « style comics de super-héros des années 60, façon Kirby ».
- **Inspiration** : les comics américains du milieu des années 60 imprimés en quadrichromie bon marché : trames de points, repérage des couleurs légèrement faux, gros aplats noirs, hachures « en plumes », bulles d'énergie, onomatopées en volume, découpage en cases. On reprend le procédé d'impression et le langage graphique, aucun héros, costume, logo ou titre.
- **Ce que c'est** : une page de bande dessinée qui bouge. **La même géométrie est dessinée deux fois** : une couche couleur (papier + aplats + trames de points) décalée de quelques pixels, et une couche d'encre multipliée par-dessus. L'énergie est faite de grappes de ronds noirs qui pulsent.
- **Marche pour** : annonce choc, lancement, « avant / après » spectaculaire, chiffre ou mot qui frappe, portrait de fondateur en héros du quotidien, bande-annonce.
- **Ne marche pas pour** : explication longue et calme, sujet sensible, marque très sobre, contenu sans moment fort.
- **État de la source** : carte notée ★★ par son auteur (« reconnaissable avec défauts ») : son rendu tire vers le « pop art propre ». Pour sonner juste, pousse ce qui manque : mains aux doigts carrés, perspective exagérée (poing vers la caméra), tension des poses.

## 2. Palette, typographie, matières

| Rôle | Hex |
|---|---|
| Papier | `#F4ECD6` |
| Encre | `#141212` |
| Cyan / bleu | `#2A9FD8` · `#1F3F9E` |
| Magenta / rouge | `#E0287A` · `#E3262D` |
| Jaune / orange | `#FFD62A` · `#F6921E` (foncé `#D2541C`) |
| Peau | `#FBD9B8` avec points rouges `#EF8A8A` |
| Espace | `#121A52` · planète `#B04AC8` |
| Énergie | cœur `#FFE14A`, bord `#FF8A2A` |

- **Trames de points** (pas, rayon, angle) : fond clair, points cyan : 9 px, 2,7 px, 15° ; fond sombre, points violets `#7A2A9A` : 9 px, 3,2 px, 75° ; peau, points rouges : 7 px, 1,5 px, 75°. En 1080 de large, garde ces valeurs : les points doivent rester visibles sur un téléphone.
- **Repérage faux** : toute la couche couleur est dessinée décalée de (4, 3) px sous l'encre.
- **Typographie** : **Bangers** (OFL) pour onomatopées et titres ; récitatifs (cartouches) en capitales Bangers sur fond jaune à filet noir avec ombre noire décalée.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Archivo Black à la place de Bangers. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/bangers` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : papier journal crème, aucun dégradé, aucune ombre douce. Le noir sert de modelé : **croissant noir** du côté opposé à la lumière + **bande de hachures parallèles** dans le sens de la lumière.
- Les violets et bleus de l'espace restent minoritaires ; si un plan « cosmos » domine le film, déclare la dérogation bleu-violet (`styles-jeu-retro/references/derogation-bleu-violet.md`).

## 3. Composition 9:16

- Une page verticale découpée en **2 ou 3 cases empilées** séparées par une gouttière papier de 24 px : grande case d'action en haut (y 160 à 1000), case de réaction ou de gros plan en dessous (y 1024 à 1540). La case de réaction peut avoir un fond magenta à points jaunes et des triangles noirs convergents.
- Personnage principal à au moins 1/3 de la hauteur de sa case, en perspective forcée (main ou objet vers la caméra).
- **Onomatopée** : 150 à 220 px, inclinée, posée sur un éclat à ≈ 26 pointes, jamais sur un visage (c'est le piège numéro un de la source). **Récitatifs** : 40 à 48 px, en haut à gauche de la case (« PENDANT CE TEMPS… ») et en bas (« MAIS… »), 8 mots maximum.
- Sous-titres de voix : cartouche jaune à filet noir vers y 1440, texte encre 46 px.
- 16:9 : grande case à gauche (≈ 80 % de la largeur), colonne de petites cases à droite.

## 4. Ce qui bouge

- **Action principale** : un geste fort par case (frapper, brandir, boire, appuyer), avec lignes de vitesse et onomatopée qui jaillit.
- **Boucle de fond 1** : **bulles d'énergie** : grappes de 16 à 26 ronds noirs, plus gros au centre, dont la disposition change « en deux » et le rayon pulse ; 6 grappes qui suivent un flux d'énergie en S (ruban jaune à bord orange et contour d'encre en dents de scie).
- **Boucle de fond 2** : triangles de focalisation qui changent derrière le gros plan, tremblement de ±3 px de l'onomatopée.
- **Autorisés** : `#001` apparition avec rebond (onomatopée), `#003` éclat, `#024` secousse à l'impact, `#046` coupe sèche, `#144` écran partagé en cases, `#184` très gros plan (yeux), `#014` traînée, `#177` contre-plongée, `#028` zoom rapide.
- **Interdits** : `#044` fondu enchaîné, dégradés, flou, `#016` parallaxe douce, `#136` trait qui frémit en continu (ici le trait est net, seuls les effets changent), mouvement fluide des personnages (ils passent de pose en pose).
- Lignes de vitesse : 9 traits noirs derrière l'objet qui bouge, longueur proportionnelle à la vitesse, qui tremblent « en deux » ; deux arcs d'action derrière le coude.

## 5. Rythme et montage

- Une case = une idée, 1,5 à 3 s. Les cases s'allument l'une après l'autre (la page se lit de haut en bas), puis coupe sèche vers la page suivante.
- Rythme en trois temps : pose d'attente, impact (onomatopée + secousse), gros plan de réaction.
- Transition du style : flash blanc d'une image puis trame de points qui grossit jusqu'à remplir le cadre ; ou la gouttière qui s'élargit et pousse la page.
- Au plus une onomatopée toutes les 3 s ; sinon plus rien ne frappe.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D ; deux canvas hors écran (couleur, encre) composés à chaque image.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `formes.js` (la géométrie, dessinée deux fois), `trames.js` (motifs de points), `ombres.js` (croissant noir + hachures), `energie.js` (bulles, flux), `lettrage.js` (onomatopées en volume, cartouches), `page.js` (cases).
- **Techniques clés** :
  ```js
  // 1. couche couleur décalée, 2. couche encre multipliée
  ctx.drawImage(couleur, 4, 3);
  ctx.globalCompositeOperation = "multiply";
  ctx.drawImage(encre, 0, 0);            // fond blanc = transparent

  // ombre « en plumes » pour n'importe quelle forme (lumière L, d1 < d2)
  // croissant noir = forme ∩ non(forme décalée de L·d1)
  // bande de hachures = même découpe avec d2, remplie de traits parallèles à L
  ```
  - Couche encre : pour chaque pièce, « remplir en blanc → ombre → contour noir 6 px ». Le blanc d'une pièce efface les traits des pièces qu'elle cache : inutile de calculer les lignes visibles.
  - Distances d1 / d2 de la source : robe 16 / 34, torse 14 / 30, manche 10 / 22, cheveux 12 / 26, dessus de table 10 / 18. Hachures espacées de 9 px, épaisseur 2,6 px.
  - Bulle d'énergie : distance au centre `R × hasard^0,7`, rayon `R × (0,05 + 0,2 × (1 − d/R))`.
  - Onomatopée en volume : 7 couches noires décalées de (0,8 d ; d), face rouge, bande supérieure jaune par découpe.
- **Pièges** : un anneau de planète doit être dessiné en deux moitiés (arrière avant la planète, avant après) ; un gros aplat noir sur un visage change le personnage (garde un croissant étroit collé au bord) ; trames trop fines qui disparaissent à l'encodage (vérifie sur l'export, pas dans le navigateur).

## 7. Son

- **Musique** : fanfare d'aventure années 60 : cuivres, timbales, orgue électrique, guitare twang ; ou un thème de générique original très court, répété.
- **Bruitages** (≈ 5 par 10 s) : un impact grave par onomatopée, sifflement d'énergie, craquement électrique des bulles, « tchac » de papier pour le passage de case.
- **Voix** : narrateur emphatique de bande-annonce, phrases courtes en écho des récitatifs. −14 LUFS.
- Un temps de silence avant le plus gros impact.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : rendu trop propre (pop art lisse), onomatopée sur le visage, points de trame invisibles, dégradés, personnage ou costume qui rappelle un héros existant.

- [ ] La couche couleur est visiblement décalée de l'encre (≈ 4 px).
- [ ] Au moins deux trames de points différentes, visibles sur un téléphone.
- [ ] Chaque forme principale porte un croissant noir et une bande de hachures du même côté.
- [ ] Au moins une grappe de bulles d'énergie qui change « en deux ».
- [ ] L'image est découpée en cases avec gouttière ; au moins un récitatif.
- [ ] Aucune onomatopée ne couvre un visage ; une onomatopée toutes les 3 s au plus.
- [ ] Aucun dégradé, aucun flou.
- [ ] Aucun héros, costume, emblème ou titre existant.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 17
- Bleu-violet : dérogation
- Texte vivant : non
- Taille mini du texte : 40

## 9. Aperçu

- Pas d'aperçu isolé de ce style dans le dépôt d'origine. Planche commune des styles : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg (© 花叔 Huashu ; à consulter, pas à réutiliser comme vitrine : sa composition reprend l'idée d'un film tiers).
- Aperçu à produire par un rendu réel 9:16 avec le plugin.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/27_kirby.md` (carte traduite du chinois), `scripts/engine/scenes/27_kirby.js` (valeurs de couleurs et de trames). Licence MIT, © 花叔 Huashu.
- Police Bangers : SIL OFL 1.1.
- Adaptation Flot Web : traduction, nom descriptif, mise en page en cases verticales, numéros du dictionnaire.
