# Diorama pixel 2.5D

## 1. Identité

- **Nom** : Diorama pixel 2.5D. Le terme anglais courant pour ce look (« HD-2D ») est une marque déposée d'un éditeur de jeux : on ne l'emploie **ni comme titre, ni comme nom de produit, ni dans une vidéo**.
- **Inspiration** : les jeux de rôle récents qui posent des sprites pixel dans des maquettes 3D : sprite dans un diorama, caméra haute de trois quarts, bande de netteté décentrée, lampes qui projettent de vraies ombres, forte lueur, vignettage, boîte de dialogue encadrée. On apprend la grammaire ; jamais leurs personnages, lieux, logos, ornements d'interface ou musique.
- **Ce que c'est** : une **maquette 3D** en boîtes et cylindres habillés de **textures pixel**, peuplée de **sprites 2D plats qui reçoivent la lumière et projettent des ombres**, vue de haut et de loin à travers une **bande de netteté** : le monde se lit comme un jouet sur une table. **La lumière est le sujet.** Contraste clé : les personnages restent plats, basse résolution et saccadés ; caméra, lumière, particules et mise au point glissent à chaque image.
- **Marche pour** : un lieu précieux (une boutique, un atelier, un village), des lumières qui s'allument une à une (utilisateurs, clients, points de vente), un trajet en étapes, l'accueil d'un nouvel arrivant en « chapitres », une veille, une météo qui passe.
- **Ne marche pas pour** : gros plans de visages, texte dense, humour rapide, sujet qui doit être vu à hauteur d'œil, délai très court (c'est le style le plus long de la catégorie).
- Ce n'est ni un jeu en voxels (pas de personnages cubiques), ni un RPG pixel plat (le décor est en vraie 3D avec vraie lumière), ni une photo de vraie maquette (les textures sont des pixels).

## 2. Palette, typographie, matières

- **Deux températures** : une grande ambiance (froide, pâle ou poussiéreuse) contre de petites sources chaudes ou saturées. Les sources portent l'histoire, l'ambiance porte l'humeur.
- Exemple « nuit de port » (démo) : ciel `#050818` → `#101D3E` → horizon `#2C4262`, brume `#16223A`, lumière de lune `#8FA8E0`, feux et fenêtres `#FF9D4A` · `#FFAE55` · `#FF8C3A`, lanterne `#FFB050`, phare `#FFF0C8`, lumière d'appoint froide `#9FB2E8`, encre `#1A1016`.
- Autres gammes : marché d'automne au crépuscule (ciel violet, lanternes roses) ; mine sous la neige à midi (jour gris-blanc, lueur minérale verte). Une nuit bleue reste sous le seuil bleu-violet si les sources chaudes sont présentes à chaque plan ; sinon voir `references/derogation-bleu-violet.md`.
- Le plus sombre est une encre chaude, jamais du noir pur. Chaque décor possède **une** couleur de brume et **une** lumière principale. Le héros porte **la seule couleur saturée qu'aucun décor n'utilise** (une cape cramoisie `#C9503F`, par exemple) : on retrouve le petit sprite dans un plan large.
- **Textures** : dessinées pixel par pixel sur de petits canevas, sans filtrage, à **densité constante** (24 px par mètre) ; couleurs prises dans des rampes de 3 à 6 teintes par un tramage Bayer étroit. Sprites de 34×50 px pour ≈ 1,67 m, contour d'1 px assombri vers l'encre.
- **Typographie** (OFL) : **Cinzel** (capitales, interlettrage large) pour chapitres et titres ; **Cormorant Garamond** (italique pour la narration) pour sous-titres et dialogues. Interface : un seul métal (or, argent ou cuivre) + un blanc papier sur plaque sombre translucide.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Playfair Display à la place de Cinzel ; EB Garamond à la place de Cormorant Garamond. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/cinzel`, `@fontsource/cormorant-garamond` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.

## 3. Composition 9:16

- Toujours regarder **vers le bas** ; jamais à hauteur d'œil. En vertical, la plongée haute fonctionne bien : le décor s'étage en profondeur du bas (proche, flou) vers le haut (loin, flou), la **bande nette au milieu** (entre 20 % et 80 % de la hauteur, elle suit le sujet).
- Personnage : 1/12 à 1/8 de la hauteur dans l'original. En 9:16 sur téléphone, **monte à 1/8 – 1/6** (160 à 300 px de haut) en rapprochant la caméra, sinon le héros disparaît.
- Construis les décors **en hauteur** : ruelle en pente, escalier, quai avec un phare, façade à étages.
- **Carton de chapitre** : Cinzel 56 à 72 px, centré vers y 420. **Boîte de dialogue** : plaque sombre, fin filet métal, plaque du nom sur le bord haut, y 1250 à 1540, largeur x 60 à 940, texte Cormorant 44 px tapé sur ≈ 90 % de la durée de la voix. **Narration** : italique 48 à 54 px sur une bande dégradée sombre, vers y 1460.
- 16:9 : format d'origine ; plans très larges possibles.

## 4. Ce qui bouge

- **Action principale** : une lumière s'allume, se porte ou faiblit, et les ombres des sprites basculent sur le sol.
- **Boucle de fond 1** : **toutes les flammes vacillent** (quelques sinus additionnés, ≈ ±20 %). Le niveau d'une lumière est une seule valeur qui pilote le dessin du sprite, l'intensité de la lampe, l'opacité et la taille du halo.
- **Boucle de fond 2** : particules dans l'air (poussière, brume, pluie oblique), eau à rides quantifiées, feu en atlas pixel à ≈ 10 images par seconde.
- **Autorisés** : `#106` bande de netteté décentrée, `#033` bascule de point entre deux profondeurs, `#027` avancée lente, `#029` travelling latéral (la caméra devance un peu, l'avant-plan passe flou), `#030` demi-orbite autour d'un bâtiment, `#181` vue du dessus, `#183` plan d'ensemble, `#128` sprites image par image, `#187` court fondu au noir entre deux décors.
- **Interdits** : `#045` volets, `#139` rotations 3D de transition, `#034` caméra à l'épaule, tremblement du monde (sauf impact), `#011` écrasement et étirement, grain de pellicule, interpolation douce des poses de sprite, dépassement (« overshoot ») sur la caméra.
- Sprites : marche en 4 dessins à 6-10 par seconde, repos en 2 dessins à 1-2 Hz, changement de pose = coupe franche entre deux dessins. **Les poses sont des données** : un objet de paramètres par dessin.

## 5. Rythme et montage

- Plans longs : 5 à 10 s. Chaque trajectoire de caméra est une courbe monotone à quelques clés ; la mise au point est recalculée à chaque image sur le sujet.
- Transitions : coupe, ou court fondu au noir entre deux décors.
- Grammaire de jeu : carton de chapitre, personnage nommé dans une boîte de dialogue, lieux, repère, carton titre.
- **Silence comme outil** : arrêt net dans une queue de réverbération, ou un seul battement quand la lumière manque de mourir.
- Revenir à un cadrage du début, changé : la rime montre ce qui a changé.
- **Version courte (8 à 12 s)** : un seul plan de 8 à 10 s : la lumière s'allume avant 2 s et les ombres basculent, un sous-titre de 2 s ; couper le second trajet de caméra.

## 6. Recette technique

**Moteur conseillé : Blender** (connecteur MCP `blender`) quand la qualité compte ; **Three.js** pour une scène légère. Assemblage, interface et sous-titres dans HyperFrames dans les deux cas.

| | Blender (qualité) | Three.js (léger) |
|---|---|---|
| Quand | plan héros, lumière volumétrique, ombres douces, décor riche | un seul décor simple, délai court, pas de carte graphique |
| Décor | boîtes et cylindres modélisés en Python (`execute_blender_code`), textures pixel en « Closest » (aucune interpolation) | `BoxGeometry` / `CylinderGeometry`, textures de canevas en `NearestFilter` |
| Sprites | plans texturés, matériau à alpha découpé, **ombres activées** | `Sprite` ou plans éclairés, ombres par `customDepthMaterial` |
| Lumière | lampes ponctuelles + volume de brume, Cycles ou EEVEE | lampes ponctuelles avec ombres (peu nombreuses), brume par `Fog` |
| Netteté | profondeur de champ de la caméra + cadrage haut ; bande décentrée au compositeur | passe maison : flou selon la profondeur **et** la hauteur à l'écran, dans le même calcul |
| Sortie | suite d'images PNG importée comme vidéo de fond dans HyperFrames | canvas WebGL piloté par `hf-seek` dans la composition |
| Contrôle | outil `look` (vue caméra, planche d'angles) à chaque étape | captures d'images fixes à chaque temps fort |

- **Techniques clés (les deux moteurs)** :
  - Une **lumière d'appoint froide** à ≈ 2 m devant le héros : un plan plat éclairé de dos reste noir.
  - Un **halo additif** sur chaque source, pour que la lueur ait quelque chose à saisir.
  - La lumière portée par un sprite se place ≈ 0,45 m vers la caméra, sinon elle brûle le sprite.
  - Bande de tramage étroite : ≈ 0,22 sur les sprites, ≈ 0,45 sur les textures (plus large = damier partout).
  - Chaîne de finition : rendu suréchantillonné → profondeur de champ avec bande décentrée → lueur (force ≈ 0,55, seuil ≈ 0,85) → vignettage et étalonnage → courbe filmique.
  ```python
  # Blender : texture pixel sans lissage, sprite qui projette une ombre
  img_node.interpolation = 'Closest'             # nœud Image Texture, aucun lissage
  # alpha découpé : nœud Math « supérieur à 0,5 » entre l'alpha de l'image et l'alpha du shader
  cam.data.dof.use_dof = True; cam.data.dof.aperture_fstop = 1.4
  ```
- **Pièges** : scène sombre illisible (remonte les tons moyens du décor ×2 à 2,5, sauf au seul moment qui doit être noir) ; halos lointains cachés par la brume ; bande de netteté sans personnage à suivre (hauteur fixe par plan) ; flou décentré fait en passe séparée (il casse les occultations) ; en Three.js, faisceaux en cylindre face caméra qui donnent des valeurs invalides que la lueur étale en blocs noirs (utiliser des cartes plates).

## 7. Son

- **Musique** : couleurs de chambre « fantasy » (harpe, célesta, cordes, cors, chœur grave) ou petits instruments populaires (luth, flûte à bec, tambour à main). Un temps fort peut tomber sur l'image d'un évènement visuel.
- **Bruitages par matière** (≈ 5 par 10 s, vrais enregistrements) : pas selon le sol (bois, terre, pierre, neige), crépitement du feu, tissu, carillon d'interface à l'entrée d'une boîte, clochettes quand quelque chose s'allume, tonnerre après chaque éclair.
- **Ambiance** par décor, en fondu d'un décor à l'autre.
- **Voix** : narrateur de livre de contes, lent ; personnages à l'écran légèrement étouffés (passe-bas ≈ 7 kHz) pour rester « dans le monde ». Musique baissée d'environ 10 dB sous chaque phrase. −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : caméra à hauteur d'œil, héros trop petit en vertical, sprites interpolés, scène trop sombre, tout net (plus d'effet maquette), lumières qui ne projettent pas d'ombres.

- [ ] La caméra regarde vers le bas dans tous les plans.
- [ ] Une bande nette, flou au-dessus et en dessous ; elle suit le sujet.
- [ ] Au moins une source chaude projette l'ombre d'un sprite sur le sol.
- [ ] Les sprites changent de pose par sauts ; caméra et lumière sont fluides.
- [ ] Textures pixel à densité constante, sans lissage.
- [ ] Le héros (≥ 160 px de haut) se repère en moins d'une seconde grâce à sa couleur.
- [ ] Toutes les flammes vacillent ; aucun grain de pellicule.
- [ ] Le terme déposé du genre n'apparaît nulle part ; aucun personnage, lieu ou ornement d'un jeu existant.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 13
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 44

## 9. Aperçu

- Film de démo d'origine *The Lampbearer* (76 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/hd-2d.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/hd-2d.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/hd-2d/STYLE.md`, `DEMO.md`, `demo/px.js`, `kit.js`, `fx.js`, `chars.js`, `post_ts.js`, `ui.js` (moteur d'origine : three.js). Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Polices : Cinzel, Cormorant Garamond (SIL OFL 1.1).
- Connecteur Blender : ahujasid/mcp-for-blender, commit `2e4b0bc`, licence MIT (noms des outils `execute_blender_code`, `look`).
- Adaptation Flot Web : traduction, nom descriptif, voie Blender et tableau comparatif (non testés par un rendu), tailles 9:16, numéros du dictionnaire.
