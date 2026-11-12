# Partir d'une vidéo de référence : mesurer, implanter, comparer

Commun aux formats `fait-3d-en-coupe`, `science-pixel-art`, `histoire-2d-interactive` et `recreation-reel`. Ce protocole vient de dizaines d'épisodes où presque toutes les retouches avaient la même cause : **une référence imaginée au lieu d'être mesurée**, et des défauts vus seulement après le rendu complet.

**Pour aller plus loin que ce protocole** : quand il faut reprendre le *rendu* d'une référence (le trait d'un personnage, son ombrage, ses couleurs exactes, le contour d'un sous-titre) et pas seulement ses plans, passer au skill `reproduire-reel`. Il apporte ce que ce document ne fait pas : la vérification de chaque coupe à l'image, la lecture continue de toutes les images, la mesure au pixel (`mesurer.py`), la fiche de style chiffrée et le tableau « référence / nous / écart » avec tolérances. Ce document garde le tableau des plans, les tailles sur grille, le plan d'implantation et les règles de relecture.

## 1. Ce qu'on reprend, ce qu'on ne reprend jamais

| On reprend (la forme) | On ne reprend jamais (l'œuvre) |
|---|---|
| le sujet et son principe d'accroche | le texte, mot pour mot ou presque |
| la structure, le rythme, la densité visuelle | les plans recopiés un par un avec juste un personnage changé |
| la grammaire d'animation, les transitions, les mouvements de caméra | les personnages, mascottes, logos, voix, musiques d'un autre créateur |
| le niveau de finition | ses chiffres sans les avoir vérifiés soi-même |

- On fait **sa propre version du même sujet** : son texte, ses plans, son storytelling, avec les personnages et les couleurs de la fiche « ma chaîne ».
- Si le client demande « exactement la même vidéo », le lui dire en une phrase et proposer sa version : c'est l'œuvre d'un autre créateur.
- **Exception, le format `recreation-reel`** : là, on calque exactement la *forme* (rythme, courbes, mise en page, caméra) parce que c'est l'objet du format ; textes, marques, visages, voix et musique sont quand même remplacés par ceux du client.
- La vidéo de référence est fournie par le client (fichier joint). On garde l'original intact et on travaille sur une copie. Le texte de l'interface de l'application n'est pas dans la vidéo : on ne le reproduit pas.

## 2. Mesurer au lieu d'imaginer

Avant d'écrire une ligne de scène :

1. **En continu** : regarder la vidéo en entier, pour les mouvements, les vitesses, les ralentis, les transitions.
2. **Planche à pas fixe** : une image toutes les 0,5 s (une planche à 1 image par seconde rate les flashs et les plans de 2 à 5 images).
3. **Une image à chaque changement de plan**, puis les images voisines de chaque coupe, une par une.
4. **Une image en GRAND de chaque plan** (pleine résolution), jamais seulement des vignettes.
5. **Les 3 premières secondes image par image, sans exception** ; les 10 premières à une image toutes les 0,5 s.

Passe automatique : `scripts/analyse_reference.sh <video> <dossier> [dossier de travail, facultatif]` (coupes par deux détecteurs, évènements, planches, bandes d'images autour des évènements, une image de début, milieu et fin par plan, son en 16 kHz pour la transcription). Lire ensuite ses sorties **à l'œil**.

À savoir : la carte des évènements et le relevé du look viennent des commandes `hyperframes measure` et `hyperframes beats`, **qui existent bien dans HyperFrames 0.9.33** (essayées une à une le 11/11/2026 : `measure probe`, `cuts`, `events`, `frames`, `look` et `beats` répondent `"ok": true`). Le script garde un repli par ffmpeg (coupes, planches, bandes d'images autour des coupes, images par plan), qu'il note dans `REPLI.txt` ; on le force par `ANALYSE_SANS_MEASURE=1`. En repli, les évènements, leur synchronisation avec le son et le look se relèvent à l'œil, sur les planches et les bandes.

### Le tableau des plans (obligatoire)

| Colonne | Contenu |
|---|---|
| Début / fin | temps dans la référence, et la phrase de **notre** script qui tombera dessus |
| Point de vue | de face, de côté, trois quarts, plongée, contre-plongée, du dessus |
| Distance | large / moyen / serré ; quelle part de la largeur occupe l'objet |
| Repères en hauteur | à quelle hauteur de l'image (en %) se trouvent le haut de l'objet, son pied, le sol |
| Entièrement visible | ce qu'on doit voir en entier à ce moment |
| Mouvement | caméra fixe, travelling, orbite, zoom ; vitesse ; ralenti oui ou non, et sa durée |
| Ce qui apparaît | l'élément nouveau du plan et comment (surgit, pousse, tombe) |
| Transition de sortie | type exact et durée en images |

- **Mesurer la taille réelle de chaque élément** : sur une image par plan, tracer une grille de 10 % et relever la boîte de chaque élément important (main, personnage, animal, véhicule, objet vedette). Ces mesures fixent nos tailles et positions. Sans elles, on dessine tout trois fois trop petit et les plans paraissent « très reculés ».
- **Respecter la mesure sans arrondir vers le haut.** Si l'élément change de taille dans la référence (on s'approche), suivre la courbe, pas une taille fixe.
- **Relever les transitions et mouvements de caméra en lecture continue, et les recréer** : zoom qui entre dans un objet pour passer à l'intérieur, poussée vers un détail, travelling qui suit l'action. Une coupe sèche avec un fondu au noir ne les remplace pas.
- **Fiche des personnages et objets vedettes** : couleur exacte relevée à la pipette sur une image pleine taille (jamais « au feeling »), proportions, toutes les positions prises (couché, assis, debout, en marche). Pour l'épaisseur du trait, l'ombrage et les reflets, la pipette ne suffit pas : skill `reproduire-reel`, étape 4.
- **Identifier l'accroche** : écrire en une phrase ce qui accroche dans les 10 premières secondes (« une maison qui penche au bord d'une falaise », pas « une maison »). Notre ouverture doit faire passer la même idée, avec nos propres plans.
- Ce tableau est le modèle : on ne change ni un plan, ni une vitesse, ni un ralenti qui n'y est pas, sauf demande du client.

## 3. Le plan d'implantation vu de dessus (avant tout décor)

Dessiner une carte simple vue de dessus avec **la zone de chaque élément** et **le moment où il existe dans l'histoire**.

- **Quand un élément arrive, il libère sa zone** : tout ce qui s'y trouvait est retiré ou raccourci (pelouse, clôture, arbres, talus, marquage).
- **Rien de décoratif dans une zone réservée** : aucun arbre, buisson, poteau ou pilier placé au hasard là où quelque chose doit arriver.
- **Ce qui arrive quelque part arrive au bon endroit, de façon continue** : un escalier arrive sur un palier, une rampe part d'une voie et finit sur une voie, à la même hauteur, sans marche.
- **Toute structure en hauteur a ses supports jusqu'au sol**, et ne traverse rien.
- **Personnages et véhicules sont toujours sur une surface où ils peuvent être.**
- **Rien n'apparaît avant son moment** : la visibilité de chaque élément est liée à la chronologie.

## 4. Règles de caméra tirées des références

- Le plan de base est celui de la référence, **assez reculé pour voir l'objet entier et son contexte**.
- Les zooms sont légers et **ne coupent jamais l'élément dont parle la voix**.
- Les transitions de caméra durent environ une seconde, sans saut.
- **Aucun plan n'est bouché** par un arbre, un véhicule, une clôture au premier plan : le héros est visible à chaque instant de son plan ; s'il se déplace beaucoup, la caméra le suit.
- Le héros a **une couleur unique** dans la scène.
- Tester chaque cadrage seul, en image fixe pleine taille, avant le rendu.

## 5. Vérifier avant le rendu complet (obligatoire)

1. **Planche de comparaison** : pour chaque plan, une image de la référence à côté de la nôtre au même instant. Comparer **les boîtes mesurées**, pas l'impression générale. Corriger chaque écart de point de vue, de distance, de repères en hauteur.
2. **Les 10 premières secondes** de notre version, une image toutes les 0,5 s, en taille lisible : l'accroche se lit tout de suite, le bon sujet au premier plan, les bonnes couleurs. Sinon : corriger avant toute autre chose.
3. **Contrôle en grand** à chaque changement de décor et à chaque élément qui apparaît (recadrage d'environ 800 px autour de la zone) : objets qui se traversent, élément qui part du vide, raccord avec une marche, support manquant, élément visible trop tôt.
4. **Gros plan de chaque personnage dans chaque position** : membres attachés au corps et posés au sol, rien qui flotte ou traverse, visage lisible, couleur conforme à la fiche.
5. **Scintillement** : comparer des images consécutives sur les surfaces fixes ; une surface qui change sans mouvement est un défaut.
6. **Montrer la planche de comparaison au client** avant le rendu complet (sauf s'il a dit de ne pas l'attendre).

## 6. Rendre par scène, corriger par scène

- Rendre par segments, puis assembler. Si une scène a un défaut, ne refaire que ses images et recoller **par numéro d'image**.
- Garder les versions précédentes pour pouvoir revenir en arrière.
- **Quand le client demande une retouche, on ne touche qu'à ce qu'il cite.** En voulant changer un cadrage, ne pas accélérer, retirer un ralenti ou modifier d'autres plans. En cas de doute, revoir la référence.

## 7. Relire sa propre vidéo, en boucle

Après l'encodage et **avant toute livraison** :
1. **Lecture continue** : planche à 1 image par seconde + extraits en mouvement aux transitions (rythme, cohérence, synchro voix / sous-titres / sons).
2. **Lecture image par image** par lots (planches de 30 images consécutives), plus en pleine taille : chaque changement de position d'un personnage, chaque apparition d'élément, les 10 premières secondes. Chercher : membre détaché, objet qui traverse, saut d'une image à l'autre, élément coupé par le cadre, mauvaise couleur, clignotement, sous-titre mal placé.
3. **Boucle** : au moindre défaut, corriger la scène, re-rendre seulement les images concernées, réencoder, puis **refaire les étapes 1 et 2 en entier**. On ne livre jamais « en espérant que ça passe ».
4. Contrôle automatique : `python3 scripts/controle_rendu.py notre.mp4 [--ref reference.mp4] [--allow 3.2-4.0]` sur un rendu **sans grain** (le grain cache les images figées) : aucune image figée plus de 0,5 s hors tenue voulue, aucun couple de plans semblables, et avec `--ref` : même découpage et énergie de mouvement comparable, plan par plan.
5. Dire au client ce qui a été vérifié (lecture continue, image par image, nombre de passes, défauts corrigés).

Puis la porte de livraison et le relecteur du skill `studio-coeur`.

## 8. Les erreurs déjà faites (à cocher avant chaque rendu complet)

**Fidélité**
- [ ] Tailles mesurées sur la grille et respectées (pas d'arrondi vers le haut).
- [ ] Chaque transition et mouvement de caméra de la référence recréé, relevé en lecture continue.
- [ ] Points de vue, distances et ordre des plans conformes au tableau ; aucun cadrage inventé.
- [ ] Ralentis et vitesses conservés.
- [ ] Une retouche demandée n'a changé que ce que le client a cité.
- [ ] Ni zoom trop profond, ni caméra trop reculée.

**Lisibilité**
- [ ] Les éléments se reconnaissent dans les plans larges.
- [ ] Le héros est visible tout au long de son plan, d'une couleur unique, suivi par la caméra s'il se déplace.
- [ ] Aucun titre affiché plus longtemps que sa phrase ; aucun texte sur un visage ou dans une zone d'interface.

**Implantation**
- [ ] Rien n'apparaît avant son moment.
- [ ] Aucun chemin ou rampe qui démarre ou finit dans le vide ; aucune marche de hauteur dans un raccord.
- [ ] Aucun élément décoratif dans une zone réservée ou sur un passage.
- [ ] Toute structure en hauteur a ses supports.
- [ ] Aucun personnage ou véhicule hors de sa surface ou dans un obstacle.

**Rendu**
- [ ] Aucun clignotement ni scintillement de surface.
- [ ] Chocs et impacts bien marqués quand le script le dit.
- [ ] Texte, personnages et couleurs sont ceux du client ; rien d'un autre créateur.

Quand le client signale une nouvelle erreur, l'ajouter à sa fiche « ma chaîne » (rubrique « Jamais ») pour ne plus la refaire.

Origine : skills du plugin Flot Web (protocole de reproduction d'une référence, fiches de production des formats, skill de recréation de reel), généralisés ; aucune référence aux séries d'origine.
