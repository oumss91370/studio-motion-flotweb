# Briques jouet

## 1. Identité

- **Nom** : Briques jouet.
- **Inspiration** : les films d'animation image par image faits avec des briques emboîtables sur un coin de table (personnages qui avancent par à-coups, caméra fluide) et la photo de jouets en macro (boîtes à lumière sur plastique brillant, faible profondeur de champ, objets réels comme paysage). On n'en copie ni les personnages, ni les décors, ni la musique.
- **Ce que c'est** : un monde de briques sur une **vraie surface** (bureau en bois, table de cuisine, rebord de fenêtre), filmé en **macro** et animé **en stop-motion**. Le charme tient à la tension entre le monde-jouet et la vraie pièce. Traits lisibles d'un coup d'œil : plastique brillant à reflets rectangulaires nets ; tenons sur chaque face supérieure ; joints assombris par l'ombre de contact ; objets réels flous derrière ; personnages en poses tenues.
- **Marques : interdit absolu.** Jamais le nom, le logo ni la silhouette de la figurine du fabricant de briques le plus connu. Les personnages sont **construits en briques** (colonnes 1×1 pour les jambes, brique 2×2 pour le torse, briques rondes pour les bras, casque rond 2×2). Les tenons ne portent aucune inscription.
- **Marche pour** : une entreprise qui assemble son premier produit, un projet qui s'écroule et dont les pièces servent à autre chose, une recette montée ingrédient par ingrédient, une reconversion (« les mêmes pièces, autrement »), une démonstration de science pour enfants, un bilan d'année.
- **Ne marche pas pour** : émotion fine sur un visage, sujet luxueux, données chiffrées, tout ce qui doit se déformer (les briques sont rigides).

## 2. Palette, typographie, matières

| Rôle | Hex |
|---|---|
| Rouge / bleu / jaune / vert | `#C91A09` · `#0055BF` · `#F2CD37` · `#237841` |
| Blanc / noir | `#F2F2EE` · `#1B2A34` |
| Compléments | orange, gris clair et foncé, beige, azur |
| Lumière principale | blanc chaud `#FFF4E8` |

- **Palette de jouet** : quelques primaires saturées + blanc, noir, gris, beige. Chaque objet construit a **une couleur dominante** et une ou deux couleurs de finition ; personnages et objets héros prennent les plus saturées.
- **Le monde réel reste naturel et éteint** (bois, papier, céramique, lumière du jour) : la couleur saturée appartient aux jouets.
- **Les blancs doivent rester blancs** : étalonnage légèrement froid, contraste doux, saturation +10 %.
- Pièces translucides (orange, jaune, incolore, bleu) réservées aux effets : feu, lumière, eau, vitre.
- **Typographie** : **Fredoka** (OFL) pour titres et sous-titres.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Fredoka. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/fredoka` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : plastique à vernis fort (≈ 0,85, rugosité du vernis ≈ 0,07), carte de rugosité avec légères traces de doigts et rayures (base ≈ 0,17), arêtes biseautées pour accrocher un reflet. Unité = un pas de tenon (8 mm) ; hauteur d'une brique 1,2 ; d'une plaque 0,4. Les grandes plaques de base sont **mates**.
- **Les effets sont des briques** : feu, fumée, eau, lumière, météo, astres sont faits de plaques, de briques rondes et de pièces translucides, bougées ou reconstruites à chaque pose. Aucune particule, aucun dégradé doux.

## 3. Composition 9:16

- Le bureau est filmé en **plongée plus marquée** qu'en 16:9 : la construction occupe le tiers central (y 600 à 1300), le plateau de la table monte derrière elle, les objets réels flous ferment le haut du cadre (y 160 à 600) et un objet flou en amorce peut border le bas.
- Personnage : ≥ 1/3 de la hauteur dans les plans de jeu (contre-plongée à hauteur de figurine pour le rendre héroïque) ; plan large en plongée pour la révélation d'échelle (« c'était un jouet »).
- Une tour, une fusée, un phare en briques conviennent très bien au format haut.
- **Sous-titres sur un élément de jouet** : pastille sombre arrondie `rgba(18,20,26,.62)` centrée vers y 1450, Fredoka 600 à 50 px, blanc, petite icône de brique à gauche ; 2 lignes au plus. Un second locuteur (radio, appareil) a sa couleur d'icône.
- Titre : 110 à 140 px, entre y 220 et 480, qui surgit « en deux », comme une pièce qu'on pose.
- Garde les piles de pièces hors des bords : elles adorent boucher l'objectif.

## 4. Ce qui bouge

- **Action principale** : **construire**. Les pièces arrivent en arc et **claquent** en place avec un minuscule dépassement (une fraction de tenon → 0 en ≈ 4 images).
- **Boucle de fond 1** : flammes, fumée ou eau en briques, reconstruites à chaque pose.
- **Boucle de fond 2** : personnage au repos qui change de pose tenue (regard, bras), infimes imperfections d'une pose à l'autre.
- **Autorisés** : `#128` allure image par image, `#126` trajectoire en arc, `#010` dépassement à l'emboîtement, `#033` bascule de point entre un objet réel et une brique, `#184` très gros plan sur un tenon, `#177` contre-plongée, `#181` vue du dessus (plan, tri des pièces), `#030` orbite autour d'une construction finie, `#029` travelling à côté d'un objet qui avance, `#024` secousse à l'impact, `#143` vue éclatée.
- **Interdits** : `#011` écrasement et étirement, `#012` métamorphose (les briques ne se déforment jamais), `#015` particules, `#044` fondu enchaîné, membres qui plient (bras et jambes tournent à leurs articulations), caméra saccadée.
- Personnages : **grandes poses lisibles** tenues plusieurs dessins : bras en V (fierté), bras en l'air (alarme), tête baissée (tristesse), petit saut (joie). Marche : jambes à ± 0,55 rad, léger rebond.
- Écroulements : **vraie physique de corps rigides**, précalculée (gravité un peu plus faible que la vraie, rebond ≈ 0,3).

## 5. Rythme et montage

- Personnages et briques « en deux » ; caméra, mise au point, feu et engins volants fluides.
- Coupes sur les temps ; **un claquement d'emboîtement peut servir de point de coupe**. Transitions du style : une brique posée devant l'objectif, un filé le long du bureau, un recul qui sort d'un décor pour entrer dans le suivant.
- **Chaque emboîtement est un clic** dans la bande-son.
- Silence net sur un échec ou une surprise : ne restent que le ton de la pièce et un petit son réel (une horloge, un frigo, un oiseau au loin).
- Plans de 2 à 5 s ; durée conseillée 20 à 50 s.
- **Version courte (8 à 12 s)** : un seul objet en deux plans : les pièces arrivent et claquent (5 s), l'objet fini fait son action (4 s) ; couper la démolition et la reconstruction.

## 6. Recette technique

**Moteur conseillé : Blender** (connecteur MCP `blender`). Three.js possible pour une scène simple.

| | Blender (conseillé) | Three.js (léger) |
|---|---|---|
| Plastique | Principled avec couche de vernis ; reflets de boîtes à lumière exacts | `MeshPhysicalMaterial` (clearcoat) ; reflets par lumières rectangulaires |
| Joints et contact | occlusion et ombres de contact données par le rendu | **occlusion ambiante à ajouter** (rayon de quelques tenons), sinon les briques semblent collées |
| Décor réel | bois, tasse, lampe et ciel de studio importés (`search_assets`, Poly Haven, CC0) | mêmes ressources en glTF et HDRI, à charger soi-même |
| Écroulement | simulation de corps rigides intégrée, à figer avant le rendu | physique à écrire et à précalculer |
| Flou macro | profondeur de champ de la caméra | passe de flou à écrire ; rendu 2× obligatoire |
| Durée | minutes par plan | rapide |

- **Structure** : `briques` (brique, plaque, brique ronde, tenons, matières), `acteurs` (personnage en briques, poses, cycle de marche), `plateau` (bureau, ciel de studio, accessoires à l'échelle, boîtes à lumière), `effets` (feu, fumée en briques, physique précalculée), `film` (jeu, caméras, point, sous-titres, évènements sonores).
- **Techniques clés** :
  ```python
  # Blender : poses tenues, sans interpolation, une image sur deux
  for fc in obj.animation_data.action.fcurves:
      for k in fc.keyframe_points: k.interpolation = 'CONSTANT'
  # échelle réelle : 1 tenon = 8 mm ; une figurine ≈ 4 cm ; caméra macro, ouverture selon le plan
  ```
  - **Ciel de studio neutre, lumière du jour** : jamais un intérieur au tungstène (les briques blanches virent à l'orange). Environnement bas (≈ 0,45) pour le contraste.
  - Une lumière principale directionnelle d'un côté en haut + 2 ou 3 **boîtes à lumière rectangulaires** (face, liseré froid derrière, une au-dessus d'un grand décor).
  - **Ouverture selon la taille du plan** : la plus grande pour les gros plans, la plus petite pour un plan large. Le point est toujours sur la tête d'un personnage ou sur la brique qu'on pose.
- **Pièges** : vernis sur une grande plaque de base = reflet coloré envahissant (matifie-la) ; objet rapide qui devient un point sur un mur vide (suis-le et garde sa destination dans le cadre) ; accessoire réel placé pour un plan qui s'invite au fond d'un autre (vérifie chaque accessoire contre chaque caméra) ; premier rendu plat et crénelé (lumière égale, pas d'occlusion, caméra saccadée).

## 7. Son

- **Musique** : petite, acoustique, joueuse : glockenspiel, piano jouet, pizzicati, ukulélé, sifflement, claquements de mains ; un élan de cuivres pour l'échelle ; un tambour-battement de cœur pour le suspense. Montée sur l'image (coupée sur les mesures), pas bouclée dessous.
- **Bruitages** (≈ 5 par 10 s, **vrais enregistrements de briques en plastique** de préférence) : clic d'emboîtement, craquement de plastique avant un échec, petits pas en plastique, fracas de nombreux claquements, tas de pièces qu'on remue, brique qui glisse sur le papier, « ding » de découverte.
- **Ton de pièce** réel sous les silences.
- **Voix** : conteur chaleureux, peu de phrases ; voix secondaires à travers un filtre d'appareil (≈ 380 à 2 800 Hz). −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Tenons visibles sur les faces supérieures ; joints assombris entre les briques.
- [ ] Reflets rectangulaires nets sur le plastique ; les briques blanches sont blanches.
- [ ] Le décor est un vrai lieu flou (bois, objets du quotidien), moins saturé que les jouets.
- [ ] Personnages et briques avancent par poses tenues ; caméra et mise au point fluides.
- [ ] Rien ne se déforme ; feu, fumée et eau sont faits de pièces.
- [ ] Chaque emboîtement visible a son clic.
- [ ] Sujet net, ≥ 1/3 de la hauteur aux moments clés, hors zones d'interface.
- [ ] Aucun nom, logo, inscription sur les tenons ni silhouette de figurine d'un fabricant.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 7
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Film de démo d'origine *Rocket from Spare Parts* (54 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/brick-toy.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/brick-toy.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/brick-toy/STYLE.md`, `DEMO.md`, `demo/bricks.js`, `actors.js`, `set.js`, `rockets.js`, `main.js` (moteur d'origine : three.js). Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Police Fredoka (SIL OFL 1.1) ; accessoires et ciel Poly Haven (CC0).
- Connecteur Blender : ahujasid/mcp-for-blender, commit `2e4b0bc`, MIT.
- Adaptation Flot Web : traduction, composition 9:16, voie Blender et tableau comparatif (non testés par un rendu), numéros du dictionnaire.
