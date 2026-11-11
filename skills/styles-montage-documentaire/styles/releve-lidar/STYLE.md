# Relevé LiDAR (nuage de points)

## 1. Identité
- **Nom** : Relevé LiDAR. Identifiant : `releve-lidar`.
- **Inspiration** : les visualisations de relevés laser en topographie et en archéologie (la couleur comme hauteur, la canopée qu'on retire), les coupes d'architecte cotées, la cadence des films de musée (un relevé tenu par écran). Grammaire seulement, aucun nom cité.
- **Principe** : de vrais points laser aéroportés d'un vrai lieu, flottant dans le noir comme un nuage mesuré ; une ligne de balayage ou un plan de coupe les traverse et les points **se condensent en surface pleine**, éclairée en lumière rasante, qu'on mesure ensuite au trait fin. Un seul mouvement de caméra dessiné porte tout le film : le nuage est quelque chose qu'on traverse, pas une image qu'on regarde.
- **Cinq règles** : le nuage est la donnée (chaque point est un vrai retour à sa position mesurée ; on ne déplace jamais des points pour former une figure) ; les points deviennent une surface derrière un front ; la classification est un levier (sol, végétation, bâtiments, eau : des couches à peler, isoler, recolorer) ; la mesure au trait fin, un relevé à la fois ; sombre, calme, exact.
- **Pour quels sujets** : archéologie sous la forêt, sentier caché, chenaux de crue, hauteur d'une digue, gabarit sous un pont, volume réel d'une carrière, relevé d'un bâtiment, visite de site avant un projet.
- **Ne marche pas pour** : un lieu sans relevé laser public (ou sans relevé du client), un sujet humain, un lieu habité précis (vie privée). Ce n'est pas un hologramme de science-fiction (points réels, clairsemés là où le relevé l'était), ni le briefing satellite (photos vues du ciel).

## 2. Palette, typographie, matières
- **Fond** presque noir à dominante froide ; jamais noir pur, jamais de ciel en dégradé.
- **Points** : un seul dégradé par hauteur ou par classe, désaturé (vert-sarcelle profond → pâle, ou gris → blanc) ; l'intensité du retour module la valeur, pas la teinte. **Pas de dégradé arc-en-ciel.**
- **Front et joints** : un blanc froid ; c'est de la lumière, pas une couleur. Aucun halo ailleurs.
- **Surface pleine** : neutre chaud (pierre, argile, plâtre), éclairée ; elle ne concurrence jamais l'accent.
- **Un accent (ambre)** réservé à ce qui a été trouvé et mesuré : éléments tracés, relevé, ligne de coupe. Une seconde teinte plus froide seulement dans un graphique de comparaison.
- Exemple de la démo : fond `#05080A`, canopée `#1F3F35` → `#5C9A7A` → `#E2F3DC`, retours du sol `#C8B38C`, surface `#BDB5A6`, front `#D4FFF0`, accent `#FFB347`.
- **Polices libres** : chiffres condensés légers pour les relevés (Barlow Condensed 300) ; mono pour instruments, coordonnées, comptes et lignes de source (IBM Plex Mono) ; sans pour les libellés.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Oswald à la place de Barlow Condensed ; IBM Plex Mono : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/barlow-condensed` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Points** : disques doux dimensionnés en unités du monde (0,12 à 0,3 m), au moins un pixel, opaques ; brouillard de distance. **Pas de grain** (les points sont déjà du détail fin).

## 3. Composition 9:16
- Le vertical sert bien ce style : la hauteur (canopée, falaise, façade) lit dans le sens du cadre. Aux moments clés, le sujet occupe au moins un tiers de la hauteur, entre y 400 et y 1150.
- **Relevé** : sous le sujet, à gauche (x 70, y 1160 à y 1400) : libellé 34 px, nombre 120 à 140 px, ligne de source/méthode 28 px ; trait de rappel quand l'élément est dans le cadre.
- **Instruments** dans un seul coin, en haut à gauche sous y 170 : lieu, coordonnées, surface, source des données, nombre de points, exagération éventuelle (28 px minimum).
- **Règle de hauteur** du plan de coupe : sur le bord gauche (pas à droite : colonne de boutons).
- **Bande de transcription** : y 1420 à y 1540, filet de 2 px, plaque qui s'estompe à droite, alignée à gauche.
- **Fenêtre de relevé** : hors de la zone mesurée, le nuage reste en points pâles au lieu de finir dans le noir.
- Zones d'interface : haut 160, bas 360, droite 135.
- **16:9** : relevés dans le tiers droit, instruments dans un coin, rien dans la bande de sous-titres.

## 4. Ce qui bouge
- **Action principale** : la condensation. Un front (un seul plan dans l'espace du monde, partagé par les points et la surface) avance : devant lui les points s'éclaircissent, un joint mince brille derrière, et la surface se remplit sur quelques dizaines de mètres. Les éléments trouvés s'allument ensuite le long de leur longueur, dans l'ordre.
- **Boucles de fond** : (1) la caméra ne s'arrête jamais (orbite lente pendant les tenues) ; (2) fin crépitement visuel des points qui arrivent derrière le front.
- **Gestes** : de la photo aux points (une ligne de balayage traverse une photo aérienne, derrière elle le lieu est en points) ; **le pelage de la canopée** (un plan descend par hauteur au-dessus du sol, les retours au-dessus se soulèvent et s'effacent couche par couche, une règle suit, un anneau brille là où il coupe les arbres) ; la coupe (un plan traverse un élément, le profil brille et un graphique coté des vrais retours s'accroche à côté) ; la repousse (la couche retirée revient en fantôme sur ce qu'on a trouvé).
- **Mouvements de caméra** : verticale verrouillée avec poussée lente (« voilà ce que montre une photo ») ; grue descendante avec bascule en oblique (entrer dans la donnée) ; oblique basse près du nuage (10 à 20° d'inclinaison, 90 à 150 m) ; recul montant (révéler l'échelle de ce qu'on a trouvé) ; travelling latéral le long d'un mur, d'une route, d'une côte.
- **Autorisés** : #181 vue à la verticale, #031 grue, #030 orbite, #029 travelling latéral, #176 traversée, #027 poussée vers une coupe, #004 tracé, #007 compteur, #143 vue éclatée (couches soulevées).
- **Interdits** : points qui bougent les uns par rapport aux autres (ni tremblement ni déplacement par bruit), apparition par fondu aléatoire sur tout le cadre, #044 fondu et coupe sèche à l'intérieur du nuage, dégradé arc-en-ciel, halo généralisé.

## 5. Rythme et montage
- 30 i/s (la source était à 24 i/s ; rien dans le style n'en dépend), animation à chaque image. Le front avance sur un amorti, **au plus lent là où est le sujet** ; un plan de coupe avance par paliers sur le temps (paliers amortis, courtes tenues) pour que les couches se lisent.
- Les transitions sont des fronts et des plans, jamais des fondus.
- Un relevé à la fois ; il se pose avec un petit sursaut ; un compteur annonce sa valeur d'arrivée.
- Presque silence avant la révélation principale.
- Sous-titre ≥ max(1,8 s ; parole + 0,6 s) ; libellé (lettres ÷ 15 + 1,5) s.
- **Version courte (8 à 12 s)** : un seul passage du front sur le sujet (6 s) et un relevé tenu.

## 6. Recette technique
- **Moteur** : Three.js dans HyperFrames (`THREE.Points` + matériau à shader, caméra et uniformes pilotés depuis `hf-seek`). **Blender** par le connecteur `blender` (nuage importé, nœuds de géométrie pour le front) si l'on veut une lumière rasante et un flou de profondeur de qualité.
```js
// un seul uniforme de front, partagé par les points et la surface
window.addEventListener("hf-seek", (e) => {
  const t = e.detail.time;
  U.uFront.value = lerp(X0, X1, easeLentSurSujet(t));     // position du plan, en mètres
  U.uCoupe.value = hauteurDeCoupe(t);                     // plan de coupe par hauteur au-dessus du sol
  poserCamera(camAt(t));                                  // spline cible / distance / cap / inclinaison
  renderer.render(scene, camera);
});
// shader des points : if (hauteurSol > uCoupe) { position.y += souleve; alpha *= fondu; }
```
- **Préparation des données** (hors page) : découper un sous-ensemble par boîte ; convertir en repère local est/nord/haut ; calculer pour chaque retour sa **hauteur au-dessus du sol** (moins un modèle de sol triangulé depuis les retours classés « sol ») ; quantifier (positions sur 16 bits + un octet chacun pour hauteur, classe, intensité, graine).
- **Surface** : maillage de 0,5 à 1 m, normales lissées, occlusion ambiante cuite, soleil bas rasant (20 à 35°), courbes de niveau discrètes. Exagération du micro-relief (×2 à 3) seulement avec une note à l'écran ; mesurer sur la donnée non déformée.
- **Où trouver un relevé** : programme 3DEP de l'USGS (États-Unis), OpenTopography (licence par jeu de données), **LiDAR HD de l'IGN (France, Licence Ouverte)**, AHN (Pays-Bas, CC0), portails nationaux (Angleterre, Espagne, Finlande, Nouvelle-Zélande…). Lire les conditions de chaque portail. Demander d'abord au client son propre relevé (drone, scanner, maquette numérique).
- **Pièges** : un nuage dense vu de loin fait tapis plat (aller près et bas) ; la classification est celle du fournisseur (bruit à écarter, végétation basse qui reste en rayures) ; relevé « sans feuilles » ou « avec feuilles » (dire la saison) ; vérifier le niveau vertical sur un sol connu ; les éléments tracés sont une **interprétation** : écrire « tracé », garder le tracé dans un fichier, écarter les candidats douteux.

## 7. Son
- **Sons d'instrument** : « pings », fin crépitement quand les points arrivent, balayage de bruit lié au front, tics qui se divisent pour accélérer, une note descendante par couche pelée, « ping » quand un relevé se pose.
- **Poids** : timbales et grosse caisse pour les condensations et les coupes, montée inversée vers l'impact principal.
- **Sec puis humide** : électronique tant que le sujet est en points ; un seul timbre organique (marimba, vibraphone frotté) pour les éléments trouvés une fois la surface là.
- **Lits** : l'ambiance propre du lieu (vent dans les feuilles, eau) au début et à la fin, en J-cut et L-cut.
- Budget de bruitages du skill `son` ; voix calme, ≈ 10 dB au-dessus de la musique ; −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Tous les points sont de vrais retours ; aucun nuage inventé ou généré ; licence et crédit dans `CREDITS`.
- [ ] Aucun point ne bouge par rapport aux autres ; ils n'apparaissent que derrière un front ou par hauteur.
- [ ] Un seul dégradé désaturé pour les points ; l'ambre seulement sur le trouvé et le mesuré.
- [ ] Un relevé à la fois, attaché à ce qu'il mesure ; nombres tirés des points ou d'une source officielle (`FAITS.md` avec la méthode).
- [ ] Toute exagération du relief est écrite à l'écran.
- [ ] Les éléments interprétés portent le mot « tracé ».
- [ ] Maisons et jardins hors cadre ; la fenêtre de relevé reste sur du terrain public ou inhabité.
- [ ] Rien sous 28 px en 9:16 ; zones d'interface respectées.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 8
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Film de démo d'origine : https://lemomo-ai.github.io/lemo-opuscar/films/lidar-survey.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/lidar-survey.jpg
- Crédit : « The Fields Under the Forest », LemoLab, CC BY 4.0 ; données de relevé de tiers : **lien seulement**. Démo en 16:9.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/lidar-survey/STYLE.md`, `style.json`, `demo/film.js` (shaders de points et de surface, `camAt`, `reading`, `drawSection`), `demo/tools/` (`fetch_ept.py`, `terrain.py`, `trace.py`, `profile.py`).
- Licence : MIT (© 2026 LemoLab) ; film de démo CC BY 4.0.
- Adaptations Flot Web : français, mise en page 9:16, Three.js dans HyperFrames, Blender en option, source française (IGN) mise en avant.
