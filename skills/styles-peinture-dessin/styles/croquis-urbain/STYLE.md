# Croquis urbain, plume et lavis

## 1. Identité

- **Nom** : Croquis urbain, plume et lavis (« Urban Sketch · Pen & Wash »).
- **Inspiration** : les pages de carnet des croqueurs urbains (le trait d'abord, le lavis ensuite ; la couleur décalée ; date et lieu écrits dans un coin ; le bord de page qui se défait en taches), les films où un monde sans couleur contient un seul objet coloré, ceux où un objet est le héros qu'une caméra suit dans la ville, la valse jazz à trois temps. Rien n'est copié : ni personnage, ni mélodie, ni mise en page.
- **Ce que c'est** : un dessin de reportage fait sur place en quelques minutes. Deux couches qui restent **visiblement séparées** :
  1. **L'encre** : un trait fin presque constant, sépia foncé. Il tremble un peu, dépasse les angles de quelques pixels, se casse en plein trait, et **suggère plus qu'il ne décrit** (quelques marques de fenêtres au lieu d'une grille, des festons au lieu d'un contour d'arbre).
  2. **Le lavis** : aquarelle transparente posée par-dessus, **décalée** de 1 à 3 px par rapport au trait, qui déborde parfois, et laisse le papier blanc pour les lumières et les personnages. Bords séchés plus sombres ; le pigment granule dans le grain.
- **La page fait partie de l'image** : papier crème à grain. Rien n'est peint bord à bord ; la peinture s'effiloche en taches et en trous blancs, avec des marges pour l'écriture.
- **Marche pour** : un quartier, un commerce, un voyage, un marché, un événement local, un portrait de lieu, une vidéo sans voix.
- **Ne marche pas pour** : explication technique, chiffres, sujet abstrait, produit numérique.
- **À ne pas confondre** : `aquarelle-carnet` n'a pas de trait d'encre ; `tableau-blanc` est un schéma ; le lavis à l'encre est monochrome. Ici : trait **et** lavis, toujours.

## 2. Palette, typographie, matières

- **L'encre est d'une seule couleur** (sépia foncé `#3b2a1e` ou noir chaud) et ne change jamais.
- **Lavis = couleur locale, légère** : peu de pigments, mélangés sur la page. Les ombres sont la couleur locale tirée vers **un** violet froid commun (`#7c7396`) ; le lointain est tiré vers **une** brume commune.
- **Le blanc du papier est la valeur la plus claire** : réservé, jamais peint. Papier : `#f3ead6`.
- **La couleur peut être retenue** : une page à l'encre seule, où la couleur est un événement.
- Exemples : *parc en été* : pelouse `#c3c96f`, feuilles `#7fa04a`, ciel `#9fbcd6`, pierre `#d8c6a0` ; *port le matin* : mer `#7fa6b8`, coques `#c9573f`, cordages `#c8a86b`, ciel `#bcd0dc` ; *marché d'hiver* : toits `#8b93a6`, lumières `#e2b04a`, auvents `#b8483e`, neige = papier.
- **Typographie** (OFL) : tout le texte est **de l'écriture sur la page** : note de coin en **Reenie Beanie** (jour, heure, météo, lieu), titres et mentions en **Caveat** 500 à 600, alignés à gauche dans la marge vide.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Reenie Beanie et de Caveat. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/reenie-beanie`, `@fontsource/caveat` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : papier à marbrure large + grain multiplié sur tout, personnages compris. Encre à ≈ 96 % de couverture, plus fine au loin, plus épaisse au premier plan (2 à 5 px en 1080 de large), tremblé ≈ 1 px, dépassement 3 à 8 px, un tiers à la moitié des longs traits avec un petit manque. Lavis : 2 à 3 couches aux bords irréguliers, en multiplication, opacité ≈ 0,4 à 0,65, bord séché à 30-40 %. Feuillage : lavis pâle, masses de lumière et d'ombre, petites taches de feuilles, trous au bord, festons d'encre seulement sur le contour. Ciel : quelques grands lavis doux ; les nuages sont des réserves. Personnages : visage laissé vide (un trait de nez de profil), côté ombre mêlé de violet. Foules lointaines : une tache de lavis, deux traits de jambes, un point de tête.

## 3. Composition 9:16

- La page est grande (par exemple 2880 × 5120 en hauteur) ; la caméra s'y déplace. Le vertical va bien aux rues, aux façades, aux arbres, à une grue qui monte.
- **Laisse des marges** : la peinture s'arrête avant le bord de page, avec une frange de taches. En plan large final, la page entière tient dans le cadre avec ses bords effilochés.
- Sujets ≥ 1/3 de la hauteur aux moments clés. Un petit objet clé reçoit un **halo de papier** (réserve) pour se lire sur un feuillage chargé.
- **Sous-titres** (s'il y a une voix) : lignes manuscrites écrites dans la marge basse de la page, jamais une boîte générique ; Caveat 54 à 60 px, vers y ≈ 1400 à 1520. Le style marche très bien **sans voix**.
- Note de coin (date, lieu) : en haut à gauche, sous y = 180. Rien d'important à droite de x = 945.
- 16:9 : page 5120 × 2880, suivi latéral d'un objet à travers la ville.

## 4. Ce qui bouge

- **Action principale** : le stylo dessine un sujet dans l'ordre réel des traits, puis le lavis tombe ; ou la **couleur arrive** depuis une source avec un front humide et peint la page.
- **Boucle de fond 1** : les personnages frémissent à 15 dessins par seconde (tremblé du trait et graines du lavis : petite surface et faible amplitude seulement). **La page immobile ne frémit pas** (c'est une vraie page).
- **Boucle de fond 2** : les forces invisibles sont dessinées : le vent en boucles d'encre qui se tracent et s'effacent par la queue, le son en lignes, la chaleur en traits ondulés.
- **Gestes natifs** : le trait avant la couleur ; la couleur comme arrivée (les personnages restent des dessins au trait figés tant que la couleur ne les touche pas) ; la seule chose colorée ; la page comme cadre ; les foules « en carottes ».
- **Autorisés** : `#004` tracé de ligne, `#136` trait qui frémit (personnages seulement), `#027` avancée, `#174` suivi latéral avec retard élastique, `#031` grue qui monte, `#043` bascule rapide avec léger roulis, `#024` petite secousse sur un impact, `#028` recul jusqu'à la page entière, `#140` page tournée, `#121` anticipation et `#122` suivi pour le jeu.
- **Interdits** : `#044` fondu enchaîné, couleur qui « s'allume » d'un coup (elle fleurit depuis un point ou arrive par le front), peinture bord à bord, contours fermés proprement, `#022` balayage de lumière.

## 5. Rythme et montage

- Caméra fluide à chaque image ; personnages à 15 dessins par seconde (à 30 i/s : une image sur deux ; 12 seulement dans un film livré à 24 i/s) ; pas sur le temps musical.
- Plans de 4 à 8 s, peu de coupes : on voyage sur la page. Transitions : trajet de caméra, page tournée, arrivée de la couleur.
- Fais entendre le son d'un lieu une mesure avant de le voir (`#047`).
- Une mesure de vrai silence (ambiance comprise) au sommet du suspense ; le premier son après est le geste suivant.
- **Version courte (8 à 12 s)** : une seule page : le trait est déjà là à l'image 0, la couleur arrive avant 3 s (c'est l'évènement), une note de coin tenue 2 s.

## 6. Recette technique

- **Moteur** : HyperFrames ; canvas 2D pour tracer, puis une passe WebGL qui compose la page : papier × lavis révélé par un champ d'arrivée × encre révélée par l'ordre des traits.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `plume.js` (trait avec tremblé, dépassement, manques, tracé progressif ; enregistre **l'instant de dessin de chaque pixel**), `lavis.js` (lavis, réserve, taches, feuillage), `arrivee.js` (champ : à quel instant la couleur atteint chaque point, depuis des sources), `page.glsl`, `personnages.js` (squelette simple, poses), `ecriture.js`.
- **Techniques clés** :
  ```glsl
  float encreVisible = step(tempsDuTrait, t);                       // rejoue l'ordre des traits
  float front   = smoothstep(arrivee - 0.25, arrivee, t + bruit);   // front humide irrégulier
  float pigment = lavis * (0.82 + 0.36 * fbm(uv * grainEchelle));   // granulation
  float bande   = front * (1.0 - smoothstep(arrivee, arrivee + 0.4, t)) * 0.2;  // bande sombre derrière le front
  ```
  - Suivi de caméra : un ressort amorti sur une cible placée un peu en avant du sujet.
  - Tout est déterministe : même graine, mêmes marques.
- **Pièges** :
  - Bords droits dans le champ de couleur (découpe par un rectangle) : découpe par la vraie distance bruitée.
  - Un personnage qui perd sa couleur en entrant dans une zone non peinte : lis l'arrivée une seule fois (ou lie-la à l'événement), jamais à sa position courante.
  - L'encre fixe ne peut pas être masquée par un lavis posé après : efface l'encre lointaine à l'intérieur des formes proches avant de dessiner.
  - Une tête de face devient chauve : dessine la masse de cheveux, puis découpes-y le visage.
  - Peindre bord à bord tue l'effet carnet.

## 7. Son

- **Ambiance du lieu** : d'abord le ton d'une pièce et du papier, puis le lieu dès qu'il a de la couleur (oiseaux, circulation, mouettes, brouhaha de marché).
- **Bruitages** (≈ 5 par 10 s hors texture) : le stylo sur papier à grain est une texture continue pendant un croquis rapide (des milliers de petits frottements qui deviennent un souffle) ; pinceau humide pour une floraison de couleur, rinçage dans un bocal, une goutte ; puis les objets à l'échelle du croquis : tissu ou papier qui claque au vent, pas sur le temps, cloche, éclaboussure.
- **Musique** (familles) : valse jazz (contrebasse à trois temps, balais, piano, clarinette ou flûte) ; trio d'accordéon de café ; guitare nylon seule ; quatuor en pizzicato ; fanfare pour une foule. Un instrument de couleur par zone de la page.
- Musique baissée sous les moments clés. Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : trait propre et fermé ; couleur calée exactement sur le trait ; page peinte jusqu'au bord ; visages détaillés ; texte typographié ; tout qui frémit.

- [ ] Le lavis est décalé du trait de 1 à 3 px et déborde par endroits.
- [ ] Les traits dépassent aux angles et certains ont un manque.
- [ ] Le blanc est du papier ; des réserves sont visibles (lumières, personnages).
- [ ] Les bords séchés des lavis sont plus sombres.
- [ ] La page a des marges et un bord effiloché ; note manuscrite dans un coin.
- [ ] Seuls les personnages frémissent ; la page est stable.
- [ ] La couleur n'apparaît jamais d'un coup.
- [ ] Tout le texte est manuscrit, dans la marge, hors y > 1560 et x > 945.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 14
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu

- Film de démo d'origine *Where the Wind Went* (33 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/urban-sketch.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/urban-sketch.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/urban-sketch.jpg
- Galerie : https://lemomo-ai.github.io/lemo-opuscar/#hand-drawn-painting
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre l'histoire ni les plans.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/urban-sketch/STYLE.md`, `DEMO.md`, `demo/engine.js`, `poses.js`, `world.js`, `look.js`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0.
- Adaptation Flot Web : traduction, mise en page verticale, numéros du dictionnaire de mouvements, budget de bruitages.
