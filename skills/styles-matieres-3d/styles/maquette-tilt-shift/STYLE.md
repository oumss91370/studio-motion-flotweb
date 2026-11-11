# Maquette tilt-shift

## 1. Identité

- **Nom** : Maquette tilt-shift (effet miniature).
- **Inspiration** : la photographie en accéléré à objectif décentré : points de vue élevés, bande de netteté, rythme de l'accéléré, ombres de nuages qui balaient les rues. On ne reprend aucun lieu ni aucune musique ; on ne montre aucun monument, marque ou logo réels.
- **Ce que c'est** : un lieu d'aspect **réaliste** vu de haut à travers un objectif décentré : seule une fine bande horizontale est nette, tout ce qui est au-dessus et en dessous fond dans le flou. L'œil lit cela comme une macro sur quelque chose de petit : le monde devient une maquette. Deux autres ingrédients sont obligatoires : **couleur saturée et ensoleillée** (peinture de modélisme) et **accéléré** (véhicules et gens avancent par petits à-coups, comme des jouets mécaniques).
- **Marche pour** : un système vu d'en haut (port, gare, marché, chantier, tournée de livraison), l'heure de pointe, une journée en accéléré, la mise en place d'un évènement, puis **un seul détail humain** sur lequel le temps retombe à vitesse réelle.
- **Ne marche pas pour** : gros plans, dialogue, produit à montrer, sujet abstrait sans lieu, scène d'intérieur.
- Ce n'est ni un rendu jouet ou argile (le monde est réaliste ; seuls l'objectif et l'horloge le rendent petit), ni une vue de dessus de jeu vidéo, ni une prise de drone (la bande, la saturation et la saccade sont obligatoires).

## 2. Palette, typographie, matières

- **« Maquette fraîchement peinte »** : un fond pâle et chaud de bâtiments, quelques accents bonbon, des verts très saturés, des sols sombres pour que marquages blancs et véhicules ressortent.

| Rôle | Valeur |
|---|---|
| Façades | blancs chauds, crème, terre cuite, brique, jaune pâle, menthe, bleu ciel |
| Verdure | `#6FA24A` |
| Chaussée | `#4B4E53` |
| Véhicules | blanc, argent, noir, rouge, bleu, taxis jaunes |
| Appoint de l'aube (côté soleil levant) | `#FFB48C` |

- Autres gammes : port méditerranéen (chaux, volets cobalt, terre cuite, eau turquoise) ; village de ski (blanc, vert sapin, cabines rouges, longues ombres bleues) ; marché du désert (sable, safran, auvents indigo).
- **Les ombres restent bleues et propres**, jamais grises. Nuit et aube sont les seuls états peu saturés ; l'aube doit se lire comme un petit matin (appoint chaud et bas, peu de fenêtres allumées), pas comme minuit.
- **Le sujet à trouver** est la seule chose saturée dans la bande nette, ou celle qui va à contre-courant.
- **Étalonnage** : courbe de tons neutre, saturation ×1,55, contraste doux, lumières un peu chaudes, vignettage 0,3.
- **Typographie** : **Overpass** (OFL, héritière des polices de signalisation routière) ; chiffres de l'horloge en police à chasse fixe.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place d'Overpass. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/overpass` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Détail de maquette** (ce qui sépare « miniature filmée » de « synthèse de jeu ») : façades à plusieurs types de fenêtres, embrasures sombres, salissures, vitrages qui reflètent le ciel, murs qui foncent vers le sol ; encombrement des toits, auvents, enseignes génériques ; marquages usés, taches ; véhicules à vitres sombres avec ombre de contact et feux stop ; occlusion ambiante partout.
- **Personnages** : petites capsules de couleur, comme des figurines de train électrique. Les acteurs vus de près ont un corps organique et sont agrandis de 20 à 30 %.

## 3. Composition 9:16

- **Toujours de haut** : vue oblique à 45-55° d'inclinaison depuis 100 à 200 m, focale plutôt longue ; ou vue droite du dessus (le plus « plateau de jeu »).
- En vertical, la bande nette horizontale laisse **deux grandes zones de flou**, en haut et en bas : c'est idéal, elles tombent sur les zones d'interface. Place la **bande nette entre y 700 et 1100** et le sujet dedans. Demi-hauteur de bande ≈ 5,5 % de l'image (≈ 105 px) ; 3,5 % pour l'intimité.
- Choisis des lieux qui se lisent en hauteur : une rue qui monte, une voie ferrée, une rivière, un quai, une piste.
- Bâtiments bas ou moyens : de grands immeubles avec une plongée faible cachent le sol.
- **Sous-titres dans la signalétique du lieu** : un panneau dans le langage graphique des panneaux de l'endroit (routier, quai de gare, avis de port), posé **dans la bande floue du bas**, vers y 1400 à 1540, texte 46 px.
- **Horloge d'accéléré** avec indication de vitesse (`×24 ACCÉLÉRÉ` / `×1 TEMPS RÉEL`) en haut à gauche sous y 160 : c'est le compteur de vitesse du spectateur.
- Titres dans le monde : lettres sur un toit, une enseigne, un champ.

## 4. Ce qui bouge

- **Action principale** : **la chute de vitesse** (×40 → ×1) : le temps retombe à la vitesse réelle sur un seul détail.
- **Boucle de fond 1** : circulation et piétons simulés (files, feux, foules qui s'amassent au rouge et déferlent au vert).
- **Boucle de fond 2** : ombres de nuages qui traversent la maquette ; soleil qui tourne.
- **Autorisés** : `#106` bande de netteté décentrée, `#039` accéléré, `#038` rampe de vitesse, `#181` vue du dessus qui tourne lentement, `#183` plan d'ensemble en glissé très lent, `#033` bascule de la bande d'un sujet à un autre, `#031` montée verticale (révélation d'échelle), `#029` travelling le long d'une ligne (rail, rivière, route), `#107` traînées lumineuses de pose longue au crépuscule, `#175` cadre fixe sur plusieurs heures.
- **Interdits** : `#044` fondu enchaîné (il trahit le faux objectif), prise de vue depuis la rue (sauf **un** plan intime voulu), caméra saccadée, `#034` caméra à l'épaule, interface de jeu, ombres grises, flou uniforme sans bande.
- **La saccade d'accéléré est l'âme du style** : en avance rapide, tout le monde (véhicules, gens, lumières, soleil) se met à jour à basse cadence et tient chaque position plusieurs images. **La caméra reste fluide.** Sous ≈ ×2, la saccade disparaît et le mouvement devient soyeux : c'est ce qui fait frapper la chute au temps réel.
- Gros plan de jeu : anticipation, étirement, écrasement à l'atterrissage, repos ; un essai raté avant la réussite est le moteur comique.

## 5. Rythme et montage

- Cadences de mise à jour du monde : **8 par seconde** en avance rapide, 12 entre ×2 et ×6, fluide en dessous. À 30 i/s : **10 par seconde** (3 images tenues) puis 15. Choisis la cadence pour que chaque saut tombe sur la grille musicale.
- Chaque clip d'accéléré est son propre plan (3 à 6 s) ; coupes sur le temps, rampes de vitesse, plongées et montées.
- Les cycles des simulations (feux, arrivées) sont décalés pour que les changements tombent sur les barres de mesure. Les acteurs héros suivent des trajets écrits, calés sur les temps, jamais « en espérant » que la simulation tombe juste.
- **Le silence est l'instant où le temps réel arrive** : on coupe la musique, on garde un ou deux sons réels.
- Durée conseillée : 25 à 45 s.
- **Version courte (8 à 12 s)** : deux clips d'accéléré de 3 s, puis la chute de vitesse (×40 → ×1) sur un seul détail (4 s).

## 6. Recette technique

**Moteur conseillé : Blender** (connecteur MCP `blender`) : le style exige un lieu **crédible** (façades détaillées, vraies ombres, occlusion). **Three.js** possible pour un lieu simple et beaucoup d'objets mobiles (c'est le moteur d'origine).

| | Blender (conseillé) | Three.js (léger) |
|---|---|---|
| Lieu | ville ou port générés en Python, détails par nœuds de géométrie, textures et ciels libres importés | ville procédurale en géométrie fusionnée, façades par shader |
| Lumière | soleil dur + ciel ; ombres et occlusion exactes | soleil avec grande carte d'ombre **ajustée à chaque plan**, appoint hémisphérique, occlusion ambiante en passe |
| Bande de netteté | profondeur de champ de la caméra **plus** un flou gradué au compositeur selon la hauteur à l'écran | une seule passe qui mélange flou physique et bande d'écran (voir ci-dessous) |
| Foules et trafic | positions précalculées en Python, instanciées | simulation simple précalculée par clip, instances (attention au plafond d'instances) |
| Coût | long : beaucoup de géométrie, rendu lourd | rapide, mais le « détail de maquette » est à écrire |

- **Techniques clés** :
  ```js
  // rayon de flou en pixels, pour un pixel à la hauteur d'écran dy (0 = centre de la bande)
  // phys = ouverture * (1/point - 1/z)              (flou de profondeur réel)
  // bande = signe(dy) * amp * pow(max(0, |dy| - w) / 0.5, 1.2)
  // flou = melange(phys, bande, 0.55 à 0.7), plafonné à ≈ 30 px     (w ≈ 0.055, amp ≈ 30)
  const tMonde = Math.floor(t * 10) / 10;       // le monde saute ; la caméra utilise t
  ```
  - **Pose la bande sur le sujet** : s'il bouge, projette-le à l'écran à chaque image et fais glisser la bande. Les échantillons lointains ne doivent pas baver sur un premier plan net.
  - **Triche sur l'azimut du soleil à chaque plan** : éclaire de face les façades qu'on voit ; un soleil fixe laisse la moitié du film à contre-jour et grise.
  - Mets à jour les acteurs **avant** la caméra, sinon le point a une image de retard.
- **Pièges** : sujet caché derrière une façade (fais-le passer côté caméra) ; véhicules simulés qui s'arrêtent avant la ligne ; plongée du dessus vers l'oblique qui vrille (oriente la vue du dessus comme le plan d'arrivée) ; gros plan pris de trop haut (descends et approche-toi) ; nuages qui délavent une montée ; aube lue comme minuit.

## 7. Son

- **Ensemble** : les percussions accordées portent le style (marimba, glockenspiel, vibraphone, woodblocks, kalimba, célesta), en pulsations minimalistes (voix ajoutées une à une, accords pulsés, déphasages), plus cordes pincées ou petit pupitre d'anches. Pas de piano-cordes générique.
- Idée : les évènements du monde déclenchent les notes d'une phrase fixe (un véhicule qui franchit une ligne, un feu qui change).
- **Le son suit la vitesse** : en accéléré, la musique d'abord, avec un léger souffle granuleux de « monde accéléré » et des cliquetis. À vitesse réelle, le monde devient soudain réel (**vrais enregistrements**) : moteurs au ralenti, circulation lointaine, oiseaux, petites voix, pas. Un arrêt de bande (la musique ralentit et s'éteint) mène au silence.
- **Voix** : détendue, peu de phrases ; musique baissée d'environ 8 dB. −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Point de vue élevé dans tous les plans (un seul plan bas toléré).
- [ ] Une bande nette horizontale, flou net au-dessus et en dessous ; le sujet est dans la bande.
- [ ] Couleurs saturées et ensoleillées ; ombres bleues, pas grises.
- [ ] En accéléré, le monde avance par à-coups et la caméra reste fluide.
- [ ] Au moins une chute au temps réel, marquée par un silence.
- [ ] Le lieu a du détail de maquette (fenêtres variées, toits encombrés, marquages) et de l'occlusion.
- [ ] L'horloge d'accéléré indique la vitesse quand elle change.
- [ ] Aucun monument, marque ou logo réels.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 12
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Film de démo d'origine *Toy Town Rush Hour* (38 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/tilt-shift.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/tilt-shift.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/tilt-shift/STYLE.md`, `DEMO.md`, `demo/post.js`, `city.js`, `geo.js`, `sky.js`, `traffic.js`, `train.js`, `ducks.js` (moteur d'origine : three.js). Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0. Police Overpass (SIL OFL 1.1).
- Connecteur Blender : ahujasid/mcp-for-blender, commit `2e4b0bc`, MIT.
- Adaptation Flot Web : traduction, composition 9:16, cadences à 30 i/s, voie Blender et tableau comparatif (non testés par un rendu), numéros du dictionnaire ; le nom du film de référence cité par la source a été retiré.
