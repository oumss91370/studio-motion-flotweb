# Pâte à modeler

## 1. Identité

- **Nom** : Pâte à modeler (stop-motion d'argile).
- **Inspiration** : l'animation en pâte à modeler image par image des studios artisanaux : une marionnette bosselée sur une petite maquette de table, une caméra fixe à faible profondeur de champ, un animateur qui pousse l'argile entre deux prises. On ne reprend aucun personnage existant.
- **Ce que c'est** : un film court (≈ 20 s) fait d'une **maquette de table construite en mètres réels**, d'une **marionnette en formes d'argile bosselées**, d'une **caméra verrouillée** et d'une animation qui avance **par poses tenues**. Rien n'est parfaitement lisse ni parfaitement droit. On doit croire qu'un vrai studio l'a fabriqué à la main.
- **Marche pour** : une mascotte, un petit personnage attachant, une carte de vœux, une annonce tendre, une courte fable (un réveil, une découverte, un salut), un objet du quotidien qui prend vie sur un bureau.
- **Ne marche pas pour** : explication, texte, données, produit technique, action rapide, plusieurs décors (une seule maquette par film), délai très court (rendu lent).
- Différence avec `briques-jouet` : ici la matière **se déforme** (écrasement, étirement, empreintes) ; les briques, jamais.

## 2. Palette, typographie, matières

- **Couleurs de pâte à modeler** : teintes franches un peu sourdes, 4 à 6 par film, sur un fond de monde sombre et neutre. L'argile **perd sa couleur et vire au pastel dès qu'elle est surexposée** : c'est l'erreur numéro un.

| Rôle | Valeur |
|---|---|
| Fond de monde | gris-bleu sombre : (0,05 ; 0,06 ; 0,07) en valeurs linéaires, soit ≈ `#3F454B` à l'écran ; force 0,4 |
| Lumière principale | chaude (indicatif : blanc doré `#FFE2B8`) ; appoint froid (indicatif : `#BFD4FF`) à un dixième de la principale |
| Yeux | perles noires brillantes |
| Pâtes (exemple indicatif) | corail `#D9603B`, moutarde `#E0B03A`, sarcelle `#2F8C86`, crème `#EFE4CF`, bleu nuit `#27405E` |

- **Matière « argile »** : rugosité 0,5 à 0,7, reflet ≈ 0,35, **un peu** de diffusion sous la surface (poids 0,03 à 0,15, échelle 4 mm) : trop, et c'est de la cire ou un bonbon gélifié. Surface : bosses à basse fréquence + **empreintes de doigts** (cellules étirées dans le relief), à la taille d'un bout de doigt par rapport à l'objet. Marbrure de couleur de ±10 %, comme une pâte malaxée. Déplacement « bosselé » de la géométrie par-dessus : les silhouettes ne sont jamais parfaites. Les boîtes ont toujours un biseau.
- **Rendu** : courbe de tons de type « AgX », contraste moyen-fort, **exposition de −0,45 à −1,0**.
- **Typographie** : presque aucune à l'image. Titre et sous-titres ajoutés dans HyperFrames : une ronde chaleureuse (**Fredoka** ou **Baloo 2**, OFL), blanc cassé, ombre douce. Un titre « en pâte » (lettres modelées) est possible mais coûteux.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Fredoka et de Baloo 2. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/fredoka`, `@fontsource/baloo-2` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Visages par pièces de rechange** : clignements et expressions sont des pièces qu'on échange (une courbe d'œil fermé remplace la perle), comme en vrai stop-motion.

## 3. Composition 9:16

- **Maquette de table en mètres** : personnage de 5 à 10 cm, caméra à 0,5 à 0,9 m, objectif de 50 mm, toile de fond 0,3 à 0,6 m derrière l'action. Une seule caméra verrouillée.
- Rendu vertical : **1080×1920** (ou 720×1280 puis agrandi si le rendu est lent). Sol de la maquette vers y 1250 ; personnage entre y 700 et 1250, soit ≥ 1/3 de la hauteur ; les yeux doivent se lire à taille de vignette.
- Le vertical convient à un décor **haut et proche** : un igloo, une pile de livres, une porte, une étagère. Laisse de l'**espace devant le regard** du personnage ; la fin se joue face caméra.
- Lumières de fond floues (petites sphères lumineuses de 3 à 8 mm, 0,5 à 1 m derrière le sujet) dans le haut de l'image : elles remplissent la zone y 200 à 600 sans rien y mettre d'important.
- Sous-titres (si voix) : 48 px, vers y 1450, sur une bande sombre douce.
- 16:9 : format d'origine (1600×900).

## 4. Ce qui bouge

- **Action principale** : un personnage fait **deux ou trois petites choses** (il sort, découvre, salue), chacune avec anticipation, action et repos, et finit sur une pose heureuse tenue.
- **Boucle de fond 1** : **le frémissement de l'argile** : ≈ 0,2 mm et 0,2° de décalage aléatoire (à graine) par pose sur la racine de chaque marionnette : les mains de l'animateur entre deux prises. **Il continue pendant les poses tenues.** Le décor, lui, reste immobile.
- **Boucle de fond 2** : **scintillement de la lumière principale** de ±1 à 2 % par pose (un vrai plateau scintille) ; les lumières du décor (lanterne, lueur) peuvent varier de ±10 %.
- **Autorisés** : `#128` allure image par image, `#011` écrasement et étirement à volume à peu près constant (écrasement 12-18 % avant un saut, étirement 8-15 % en l'air, écrasement à l'atterrissage), `#121` anticipation, `#122` suivi et repos, `#010` dépassement pour les apparitions, `#123` saut, `#175` caméra verrouillée, `#105` flou d'arrière-plan, `#040` pose tenue 4 à 8 poses.
- **Interdits** : **toute interpolation douce** (c'est le premier signe de l'image de synthèse), mouvement de caméra, `#044` fondu enchaîné dans la scène, `#015` particules, `#022` balayage de lumière, flou de mouvement, surfaces lisses ou droites.
- **Cycles par paliers** : un dandinement change de pose toutes les 3 poses, pas à chaque pose. **Clignement = 2 poses.**
- Calcule le point le plus bas de tout ce qui change de forme, pour qu'il **repose sur le sol** au lieu de flotter ou de s'enfoncer.

## 5. Rythme et montage

- **15 poses par seconde** pour une livraison à 30 i/s (une image sur deux). La source animait à 12 poses par seconde dans un film à 24 i/s : ne garde 12 que si le film est livré à 24 i/s ; à 30 i/s, 12 donne des tenues irrégulières de 3 puis 2 images (mesuré sur un rendu réel le 11/11/2026).
- Film de 20 s = 300 poses à 15 par seconde (240 à 12 par seconde en 24 i/s). Écris un **découpage en numéros de pose** : plan d'installation tenu (≈ 35 poses), révélation du personnage, deux ou trois temps d'histoire, une fin « bouton » (pose heureuse, clignement, tenue).
- **Un seul plan**, caméra fixe. S'il faut plusieurs plans : coupes franches, une maquette par plan, 2 plans au plus.
- Poses clés tenues 4 à 8 poses pour que le public les lise.
- Grain léger et vignettage ajoutés à l'encodage.
- **Version courte (8 à 12 s)** : 10 s = 150 poses à 15 par seconde : installation tenue 15 poses (1 s), **une seule action** avec anticipation et repos, pose finale tenue 20 poses ; couper la deuxième et la troisième petite chose.

## 6. Recette technique

**Moteur : Blender, obligatoire** (connecteur MCP `blender`, rendu Cycles). Three.js n'est pas conseillé : sans diffusion sous la surface, sans vraies ombres douces ni flou d'objectif, l'argile ressemble à du plastique.

| | Blender / Cycles | Three.js (repli, déconseillé) |
|---|---|---|
| Argile | Principled : rugosité, diffusion sous la surface, relief d'empreintes, déplacement bosselé | matériau standard + carte de relief : pas de diffusion, aspect plastique mat |
| Lumière | lampes de surface (principale, appoint, contre-jour) + une source du décor ; ombres douces réelles | ombres dures ou floutées, occlusion à ajouter |
| Flou de maquette | profondeur de champ de la caméra, ouverture f/3 à f/5 | passe de flou à écrire |
| Animation | clés sur chaque pose, **interpolation constante** | poses calculées depuis le numéro de pose |
| Durée | ≈ 6-7 s par image en 1600×900 sur une machine récente (≈ 25-30 min pour 240 images) ; moitié de résolution et d'échantillons sans carte graphique | temps réel |

- **Structure d'un script de scène** : préparer le rendu (résolution, échantillons, monde) → **décor** (matières d'argile, sphères, boîtes arrondies, cylindres, tous bosselés) → **marionnette** (formes simples attachées à des pivots : racine aux pieds, pivot du corps, pivot de la tête ; les membres pendent à des pivots, les poses ne sont que des rotations) → **lumières et caméra** → **animation** (une boucle sur les poses) → interpolation constante → rendu.
- **Techniques clés** :
  ```python
  # une clé sur CHAQUE pose, puis aucune interpolation
  for f in range(1, 241):
      pose = calculer_pose(f)                 # courbes d'aisance, dépassements
      poser(marionnette, f, pose, bruit=frémissement(f))   # ≈ 0,2 mm et 0,2° à graine
      lampe_principale.data.energy = E * (1 + 0.012 * alea(f))
  for fc in toutes_les_courbes(): 
      for k in fc.keyframe_points: k.interpolation = 'CONSTANT'
  # pièce de rechange : on « cache » un œil en le mettant à l'échelle 0,0001
  ```
  - Avec le connecteur : envoie le script par `execute_blender_code`, contrôle avec `look` (vue caméra ; bande d'images pour l'animation) avant tout rendu long.
  - **Images d'essai d'abord** : 4 à 6 poses aux temps forts, en 960×540 et 32 échantillons. Vérifie : **exposition** (argile délavée = trop clair), **contact** (pieds et membres touchent le sol), **yeux** lisibles en vignette, **cadrage**, **flou** (les lumières du fond en disques doux).
  - Un seul rendu à la fois par carte graphique. Après une correction, ne relance que la plage d'images touchée.
  - Planche de contrôle de toutes les poses avant livraison : chaque temps se lit, rien ne saute, ne flotte ni ne se traverse.
- **Pièges** : interpolation lisse oubliée sur une courbe ; frémissement appliqué au décor ; trop de diffusion (cire) ; empreintes trop grosses sur un petit personnage ; personnage qui s'enfonce dans le sol pendant un écrasement ; durée de rendu sous-estimée.

## 7. Son

- **Musique** : petite, artisanale : ukulélé, glockenspiel, piano droit, sifflement, contrebasse pincée ; ou rien, avec seulement l'ambiance.
- **Bruitages** (≈ 5 par 10 s, **vrais enregistrements** : la matière molle se capte très bien) : pâte qu'on presse, petits pas feutrés ou mouillés, « pop » d'une apparition, frottement de tissu, objet posé sur du bois, un souffle, un petit rire.
- **Ambiance** : ton d'atelier (léger ronflement de lampes), ou l'extérieur du décor (vent, neige).
- **Voix** : facultative ; le personnage s'exprime mieux par des sons (babils, soupirs) que par des phrases.
- Pas de bruit de pellicule ; −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Aucune interpolation douce : les poses sautent, 15 par seconde à 30 i/s (12 à 24 i/s).
- [ ] La marionnette frémit légèrement même en pose tenue ; le décor est immobile.
- [ ] L'argile garde sa couleur (pas de pastel délavé) ; empreintes et bosses visibles en gros plan.
- [ ] Rien n'est parfaitement lisse ni droit ; les silhouettes sont irrégulières.
- [ ] Pieds et membres touchent le sol à chaque pose.
- [ ] Les yeux se lisent à taille de vignette ; clignements de 2 poses par pièce de rechange.
- [ ] Caméra verrouillée, faible profondeur de champ, au moins une lumière motivée par le décor.
- [ ] Chaque temps de l'histoire a son anticipation et son repos ; fin tenue face caméra ; aucun personnage existant.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : fixe
- Couleurs max : 8
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 48

## 9. Aperçu

- Le dépôt d'origine ne publie pas de vidéo : il fournit deux scènes d'exemple à rendre (un petit animal qui sort d'un igloo ; une boule d'argile qui s'éveille sur un bureau). Page du projet : https://github.com/angrypenguinpng/blender-claymation-skill (© 2026 angrypenguinpng, MIT).
- Aperçu à produire par un rendu réel 9:16 avec le plugin.

## 10. Origine

- **angrypenguinpng/blender-claymation-skill**, commit `0be7cc0` : `SKILL.md`, `references/look-guide.md`, `scripts/claylib.py` (matière d'argile, formes bosselées, lumières, caméra, courbes, frémissement, interpolation constante), `scripts/encode.sh`, `examples/igloo.py`, `examples/clay_spark.py`. Licence MIT, © 2026 angrypenguinpng. Aucun script n'a été exécuté.
- Connecteur Blender : ahujasid/mcp-for-blender, commit `2e4b0bc`, MIT (la source lance Blender sans interface ; ici on passe par le connecteur).
- Adaptation Flot Web : traduction, format 9:16, cadence à 30 i/s, palette d'exemple, sections son et typographie (non fixées par la source), numéros du dictionnaire.
