# Infographie isométrique

## 1. Identité

- **Nom** : Infographie isométrique (diorama de blocs plats à trois tons).
- **Inspiration** : l'architecture en vraie isométrie de certains jeux de réflexion (aplats, trois tons fixes par face, une caméra qui glisse et zoome sans jamais casser la projection), les dioramas en coupe des jeux de gestion de ville (un plateau flottant avec ses couches de sol), la vulgarisation scientifique animée (une question, une métaphore claire par étape, un changement d'échelle quand un nombre est trop grand), les pictogrammes statistiques des années 1930 (des icônes identiques répétées pour dire une quantité). On n'en reprend ni personnage, ni bâtiment, ni icône, ni palette, ni musique.
- **Ce qui le fait reconnaître** : une **isométrie plate et vraie** (aucune perspective, aucun contour sur les solides, seules les trois valeurs de chaque face séparent les formes) ; le **mobilier d'infographie fait partie du monde** (traits de rappel, épingles d'étiquette, lignes de coupe en pointillés, faces de coupe hachurées, anneaux de suivi, légende, tracé d'itinéraire) ; des **nombres construits avec des icônes**, qui tombent juste ; un **plateau flottant** dont les bords montrent la coupe.
- **Marche pour** : expliquer un système ou un parcours (chaîne d'approvisionnement, trajet d'un produit, fonctionnement d'un bâtiment, d'une ville, d'un réseau), rapport annuel, « d'où ça vient et où ça va ».
- **Ne marche pas pour** : émotion et visages (les personnages n'en ont pas), un seul objet à détailler (voir `isometrique-trait-fin` (catégorie « Matières et 3D »)), une règle du quotidien avec des petites gens (voir `livre-isometrique`). Ce n'est pas de la 3D à facettes, ni un plan bleu.

## 2. Palette, typographie, matières

- **Un fond neutre pâle** (crème, gris papier, bleu pâle) et **5 à 7 teintes plates**, chacune avec ses trois tons, plus une couleur d'encre.
- **Trois tons par face**, tirés d'une seule couleur de base : dessus = mélangé à environ 20 % de blanc chaud ; côté gauche = la base ; côté droit = mélangé à environ 22 % d'un sombre froid (`#231A2C`). Les ombres sont donc légèrement froides.
- **La couleur a un sens, comme dans une légende** : une teinte par matière ou par rôle (l'eau a toujours le même bleu, le sujet toujours sa teinte). Jamais la même teinte pour deux sens.
- **La teinte du sujet est réservée** : quand l'histoire dit « celui-ci », tout le reste se désature vers un gris chaud et seul le sujet garde sa couleur.

| Sujet d'exemple | Teintes sur fond pâle |
|---|---|
| Chaîne du recyclage | vert bouteille, brun kraft, bleu argenté, terre, moutarde, sur crème |
| Hôpital | sarcelle, corail, lavande, gris acier, sur gris pâle |
| Centre de données | bleu électrique, ambre, graphite, menthe, sur blanc cassé |

- **Police** : une seule, géométrique (Jost, libre). Titres en 600, capitales, interlettrage d'environ 0,12 em ; nombres en 400, grands ; unités à mi-taille. Tout texte porte un **halo d'environ 7 px** de la couleur du fond.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Outfit à la place de Jost. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/jost` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Encre** : 2 px, uniquement pour les éléments d'infographie.
- **Plateau** : flotte sur le fond pâle, avec un semis de points isométriques très discret et une ombre douce ; ses faces avant montrent les couches (sol, eau, étages, tuyaux).
- **Personnages** : silhouettes minimales (tête ronde, corps fuselé en deux tons, bras en gros trait, un chapeau ou une coiffure pour l'identité), **sans visage**, à 15 dessins par seconde (une image sur deux à 30 i/s).

## 3. Composition 9:16

- Un plateau isométrique est un **losange large** : en vertical, il ne tient pas en entier à grande taille. Deux solutions : **suivre un itinéraire** (la caméra descend le long du parcours, station par station) ou **empiler** (une tour en coupe, des couches de sol, un plateau en haut et un médaillon de gros plan en bas).
- Le sujet occupe au moins un tiers de la hauteur aux moments clés ; les étiquettes ne le recouvrent jamais.
- **Épingles d'étiquette** : point (anneau d'encre, fond pâle), trait vertical, filet horizontal, texte. Elles pointent vers le haut ou le bas, la gauche ou la droite, choisi station par station.
- **Tailles** : titres 70 à 100 px ; nombres 60 à 90 px ; étiquettes 34 à 40 px.
- **Le sous-titre est une étiquette de carte** : carte pâle à petit rayon, bordure d'encre, un mini-cube isométrique en guise de pastille de légende, texte de 46 à 50 px, centré entre y 1380 et y 1540. La bordure se trace d'abord, le texte se découvre ensuite. Garder cette zone libre.
- **La dernière image peut être la légende** : titre, totaux, clé des icônes, mention « échelle non respectée ».
- Rien d'important à droite de x 945.

## 4. Ce qui bouge

- **Action principale** : un objet suivi (avec un anneau « vous êtes ici ») parcourt le système ; les choses **s'ouvrent pour montrer l'intérieur**.
- **Boucles de fond** : (1) les véhicules et les personnages qui circulent le long de tracés, tournés dans le sens de leur route ; (2) la vie des stations (fumée, eau, voyants) et les icônes qui s'accumulent.
- **Autorisés** : tracé de ligne `#004`, vue éclatée `#143` et coupe, apparition éclair `#001` avec dépassement `#010` (les icônes), compteur `#007`, écrasement `#011` à la réception (environ 18 %), travelling de suivi `#029`, zoom `#028` (interpolé en logarithme), plan d'ensemble `#183`, plan fixe `#175`, points d'intérêt `#163`.
- **Interdits** : orbite `#030` et toute rotation ou bascule de la projection, perspective, flou de profondeur `#105`, **solides semi-transparents** (un bloc qui apparaît en fondu ressemble à un fantôme : les solides arrivent **par le mouvement**), contours sur les solides, fondu enchaîné `#044`.
- **Rien ne bouge sans qu'une ligne le précède** : le tracé d'itinéraire se dessine un peu en avance ; un trait de rappel pousse avant qu'un médaillon s'ouvre ; une ligne de coupe se trace avant qu'une paroi glisse.
- **La coupe** : ligne de coupe (environ 0,3 s), la paroi proche glisse le long de sa normale et s'efface (environ 0,35 s), les bords hachurés apparaissent à la fin.
- **Accumuler, c'est accélérer** : arrivées sur les noires, puis les croches, puis par vagues.

## 5. Rythme et montage

- Plans longs : un plan-séquence continu est possible ; sinon, coupe vers un second plateau ou vers un médaillon.
- Une station = 4 à 8 s : arrivée, étiquette, ouverture, nombre.
- Le son de la station suivante entre une demi-seconde avant qu'elle apparaisse.
- Fin type : recul rapide jusqu'à ce que toutes les étiquettes soient à l'écran ; la dernière image est une infographie finie.
- **Version courte (8 à 12 s)** : deux stations de 4 s, puis le recul final sur l'infographie finie (2 s) ; couper les nombres secondaires. Accroche : l'objet suivi part dès la première seconde.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D avec `dessiner(t)` pour le style d'origine (aplats nets, aucune dépendance). Si le client veut des ombres portées et une lumière réaliste, passer par `blender` avec une caméra orthographique (mais ce n'est plus exactement ce style, qui est plat).
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `iso.js` (projection, caméra, file d'attente triée par profondeur, primitives : boîte, prisme, cylindre, cône, toit, sphère, plan, ligne, texte), `infographie.js` (épingle, médaillon, ligne de coupe, hachures, anneau, grille d'icônes, personnage), `monde.js`, `film.js`.

```js
const C30 = Math.cos(Math.PI / 6);
// x descend vers la droite, y descend vers la gauche, z monte ; k = pixels par unité (le zoom)
const projeter = (x, y, z, k) => ({ sx: (x - y) * C30 * k, sy: ((x + y) * 0.5 - z) * k });
const profondeur = (x, y, z) => x + y + z;              // tout est mis en file, trié, puis dessiné
const troisTons = base => ({ dessus: melange(base, "#fff6e8", .20), gauche: base, droite: melange(base, "#231A2C", .22) });
const zoom = (k0, k1, p) => k0 * Math.pow(k1 / k0, adoucir(p));   // zoom interpolé en logarithme
```

- **Pièges** : le tri par profondeur échoue sur les objets composés (une colline en terrasses, une grue au-dessus d'un bateau) : les dessiner comme un seul élément ordonné ; l'ordre des sommets fait disparaître des faces prises pour des faces arrière ; la géométrie du monde derrière un gros plan devient d'énormes disques (sauter les détails au-delà d'un seuil de zoom, peindre un fond plat) ; un recul à travers un objet haut donne une image ratée (faire entrer les objets hauts selon le zoom) ; un objet à la mauvaise silhouette se lit comme autre chose (une boîte blanche à toit rouge est une maison) ; une roue ou une coque qui touche la mauvaise surface se lit comme un accident.

## 7. Son

- **Musique** : acoustique et légère : kalimba, marimba, guitare nylon, pizzicato, wood-block, petites percussions, contrebasse, glockenspiel ; ou une pulsation électronique propre pour un système technique. Un court motif peut marquer le sujet à chaque apparition.
- **Ambiances par station**, enchaînées : vent et oiseaux, port, mer, rumeur de ville, salle des machines.
- **Bruitages par matière** : grains qui coulent, acier des conteneurs, papier, céramique, liquide versé, moteur, clavier. Un son par icône quand un nombre se remplit (très en retrait dans le mixage).
- **Silence** : zéro absolu ou un seul son faible ; le premier son d'après est l'un des plus importants du film.
- **Voix** : claire, amicale, phrases courtes. Garder les ambiances aiguës très basses sous la voix.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] La projection ne tourne jamais et n'a aucune perspective.
- [ ] Aucun contour sur les solides : trois tons par face, côté droit légèrement froid.
- [ ] Chaque teinte a un seul sens dans tout le film.
- [ ] Chaque mouvement est précédé d'une ligne (itinéraire, rappel, coupe).
- [ ] Les nombres sont faits d'icônes identiques, et leur compte est exact.
- [ ] Aucun solide n'apparaît en fondu.
- [ ] Les étiquettes ont leur halo, ne couvrent pas le sujet et font au moins 34 px.
- [ ] Le sujet fait au moins un tiers de la hauteur aux moments clés ; la zone du sous-titre est libre.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 9
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 34

## 9. Aperçu

- Film de démo d'origine, *From Bean to Cup* (59 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/iso-infographic.mp4
- Affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/iso-infographic.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, film et images sous CC BY 4.0.

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichiers `styles/iso-infographic/STYLE.md`, `DEMO.md`, `demo/engine.js`, `demo/world.js`, `demo/film.js`.
- Licence : MIT pour le code et les textes (© 2026 LemoLab), CC BY 4.0 pour le film et ses images. Police Jost : OFL 1.1.
- Adaptation Flot Web : traduction, solutions de cadrage vertical, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
