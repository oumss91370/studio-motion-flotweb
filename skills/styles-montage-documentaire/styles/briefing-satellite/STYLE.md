# Briefing satellite

## 1. Identité
- **Nom** : Briefing satellite. Identifiant : `briefing-satellite`.
- **Inspiration** : les enquêtes en sources ouvertes qui annotent des images satellite (traits fins, une affirmation par écran, la mesure comme intrigue), les films de changement d'échelle continu avec relevé, les séries « un lieu, le temps qui passe » des agences spatiales. Grammaire seulement : ni mise en page, ni police, ni icône, ni musique reprise, aucun nom cité.
- **Principe** : de vraies images satellite d'un vrai lieu, ramenées au gris d'un analyste, avec de fines lignes blanches de mesure posées sur le sol : un viseur qui accroche, des contours, une ligne de distance, **un seul relevé**. Un zoom continu, fait de plaques d'images emboîtées, emmène de l'orbite au sol et retour ; le temps peut défiler dans un cadre verrouillé.
- **Cinq règles** : le sol est une photographie (rien n'y est dessiné, stylisé ni généré) ; deux couches, deux vérités (l'image = ce que le satellite a vu, les traits = ce que l'analyste a mesuré) ; l'étalonnage suit l'histoire (couleur vraie en orbite, gris pour l'analyse, couleur seulement là où l'histoire tourne) ; l'échelle est la caméra ; un constat par écran, dans l'unique couleur d'accent.
- **Pour quels sujets** : un lac qui recule, une ville qui s'étend, un glacier, une forêt, un chantier vu du ciel, vérifier ce qu'affirme une carte ou un plan, « à quelle distance ? ».
- **Ne marche pas pour** : un sujet sans lieu précis, un intérieur, un lieu sans imagerie libre de droits à la bonne résolution. Ce n'est pas un hologramme de science-fiction (pas de fil de fer lumineux), ni une infographie isométrique, ni une présentation.

## 2. Palette, typographie, matières
- **Sol** : gris neutre, de ~3 % à ~65 % en valeur, teinté bleu-noir → argent froid, un cinquième de la saturation d'origine. **Le blanc est réservé aux marques** : il signifie « mesuré ».
- **Un accent chaud** (ambre) pour le seul relevé à l'écran, jamais en décoration. Une seconde teinte, plate et cartographique, peut marquer l'**affirmation** que l'image met à l'épreuve (une carte, un plan, une promesse), jamais rien de mesuré.
- Exemple de la démo : sol `#070B0E` → `#A1A7A9`, marques `#F2F5F6`, relevé `#FFBE55`, bleu de carte `rgb(46,112,206)`.
- Pas de fausses couleurs en dégradé sur l'imagerie.
- **Polices libres** : relevé en grotesque condensée légère (Barlow Condensed) ; instruments et dates en IBM Plex Mono ; libellés en sans ; serif seulement pour la couche « affirmation » et le titre.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Oswald à la place de Barlow Condensed ; IBM Plex Mono : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/barlow-condensed` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Marques** : traits fins de 1,2 à 2,6 px avec halo sombre, tirets pour l'historique et les affirmations, crochets, graduations, traits de rappel. Elles passent par la **même fonction monde → écran** que l'image.
- **Finition** : grain léger à l'encodage, vignette, flou directionnel seulement sur les panoramiques filés.

## 3. Composition 9:16
- **Imagerie plein cadre.** Le vertical convient bien aux sujets allongés nord-sud (fleuve, côte, vallée) ; orienter la caméra (cap) pour que le sujet occupe la hauteur.
- Aux moments clés, le sujet remplit un tiers de la hauteur du cadre, centré entre y 500 et y 1100.
- **Relevé** : dans le tiers bas-gauche de la zone utile (y 1150 à y 1400, x 70), à côté de ce qu'il mesure : libellé au-dessus (34 px), nombre 120 à 150 px, note de source dessous (« Landsat, mesuré », 28 px).
- **Instruments** (espace écran, fixes) : altitude en haut à gauche sous y 170 ; barre d'échelle en bas à gauche au-dessus de y 1540 ; crédit de l'imagerie lisible (28 px minimum) à côté de la barre d'échelle.
- **Bande de transcription** (sous-titres) : y 1420 à y 1540, filet blanc de 2 px, plaque sombre qui s'estompe vers la droite, alignée à gauche, une ou deux lignes de 40 px.
- **Libellés attachés au sol** par un trait de rappel ; ils restent à gauche de x 945.
- Zones d'interface : haut 160, bas 360, droite 135.
- **16:9** : relevé dans le tiers droit, sous-titres en bas à gauche, instruments dans les coins.

## 4. Ce qui bouge
- **Action principale** : la plongée. Un seul zoom de l'orbite au sol, distance interpolée **en échelle logarithmique**, inclinaison qui passe à la verticale ; les plaques plus fines apparaissent en fondu de bord à mesure que la caméra descend.
- **Boucles de fond** : (1) la caméra ne s'arrête jamais : pendant les tenues, une dérive de 2 à 5 % ou une rotation lente ; (2) le relevé d'altitude et la barre d'échelle qui suivent la caméra.
- **Les marques arrivent en se faisant** : une ligne pousse, un contour s'imprime derrière le balayage, un compteur roule et se pose avec un petit sursaut, un viseur claque avec dépassement.
- **Le temps change par balayage**, jamais par fondu : front doux (le passage d'un satellite), du nord au sud en avant, du sud au nord pour un retour en arrière. Chaque date laisse son contour ; la bande perdue entre deux contours clignote.
- **Gestes** : la carte contre la photo (la caméra tombe dans la carte imprimée de l'affirmation, une barre de scanner l'arrache, le sol est dessous, le nom survit à la page) ; la ligne de distance (marquer la destination, faire pousser une ligne graduée de A à B, suivre sa pointe pendant que le relevé compte, se poser sur le nombre, reculer pour voir toute la distance) ; la couleur revient là où l'histoire tourne ; le viseur devient le cadre du titre.
- **Autorisés** : #027 travelling avant, #030 orbite oblique, #181 vue à la verticale, #029 suivi le long d'une ligne, #043 panoramique filé (nouveau sujet à la même altitude), #031 remontée, #004 tracé de ligne, #007 compteur, #010 dépassement (viseur).
- **Interdits** : #044 fondu entre deux lieux sans rapport, coupe sèche à l'intérieur d'un zoom, image figée plus d'1 s, sol qui bouge sous ses annotations, instruments qui changent de place.

## 5. Rythme et montage
- Trois structures : time-lapse verrouillé d'un lieu qui finit en poussée ; un fleuve suivi de la source à l'embouchure avec un relevé à chaque arrêt ; deux lieux comparés à la même échelle par panoramiques filés.
- L'espacement des balayages de dates dit la vitesse ; la caméra bouge avec eux (elle accélère quand les pas raccourcissent, freine sur le dernier).
- Transitions : balayages, couche de carte qu'on éteint, traversée de plaques, panoramique filé, viseur qui s'ouvre en carton.
- Sous-titre ≥ max(1,8 s ; parole + 0,6 s) ; un compteur annonce sa valeur d'arrivée ; un libellé reste (lettres ÷ 15 + 1,5) s.
- **Version courte (8 à 12 s)** : la plongée seule (6 à 7 s), puis le relevé tenu (nombre et libellé) ; couper les couches suivantes et le retour en orbite.

## 6. Recette technique
- **Moteur** : HyperFrames + Three.js (plan ou sphère texturés, caméra pilotée depuis `hf-seek`). Version légère sans globe : plaques en `<img>` empilées dans un conteneur dont on anime l'échelle en log. **Blender** par le connecteur `blender` si l'ouverture en orbite doit être de qualité cinéma (sphère, atmosphère, limbe).
```js
// zoom en log : l'altitude d, pas l'échelle, est interpolée linéairement en log
const d = Math.exp(lerp(Math.log(D_ORBITE), Math.log(D_SOL), ease(u)));
monde.style.transform = `translate(${cx}px, ${cy}px) scale(${D_REF / d}) translate(${-px}px, ${-py}px)`;
// même fonction pour les marques : ecran = (pointSol - [px, py]) * (D_REF / d) + [cx, cy]
```
- **Plaques** : images géoréférencées avec leur boîte longitude/latitude, emboîtées par résolution (monde → région → détail), bords adoucis. Dates sur la même grille.
- **Étalonnage d'analyste** : une seule variable de la couleur au gris ; contraste local renforcé, épaule pour que sel, neige et nuages restent sous le blanc.
- **Où trouver l'imagerie** (domaine public ou libre avec crédit) : Landsat de l'USGS (depuis 1972, monde entier), NAIP (États-Unis, ~1 m), Blue Marble, MODIS, VIIRS de la NASA ; recherche par zone et date dans le catalogue ouvert Planetary Computer (Landsat, Sentinel-2) ; traits de côte, lacs et rivières de Natural Earth. **Interdits** : captures de Google Earth/Maps, Bing, Esri, Mapbox, imagerie commerciale, photos de presse, images générées. Données Sentinel brutes : mention « Contient des données Copernicus Sentinel modifiées [année] ». La mosaïque Sentinel-2 « sans nuages » n'est en CC BY que pour 2016.
- **Pièges** : raccords entre passages pris à des dates différentes (une date par passage, gains accordés sur la terre stable, trous comblés avec la même année) ; vieux capteurs (lignes manquantes, pas de bleu) ; panaches et brume (changer de date plutôt que retoucher) ; bouillie grise de près (monter le contraste local à cette altitude seulement) ; nuages lus comme des reliefs en gris (prendre la saison sèche) ; calcul de la sphère en double précision.

## 7. Son
- **Télémétrie** : « ping » d'accrochage (à faire revenir), tics secs sur la grille qui se divisent pour accélérer, balayages de bruit (montants pour un retour en arrière), cliquet pour la ligne de distance.
- **Poids** : timbales, grosse caisse, cymbale frottée ; les mesures se posent sur un coup accordé.
- **Lits** : bourdonnement d'orbite, souffle radio ; l'ambiance propre du lieu (vent, eau), avec parcimonie, en J-cut ou L-cut.
- **Silence** : musique et bruitages s'arrêtent, un lit mince reste ; le premier son après est le retournement. Un court creux (0,2 à 0,45 s) avant les impacts les plus lourds.
- Budget de bruitages du skill `son` ; voix d'analyste calme, phrases déclaratives courtes, ≈ 10 dB au-dessus de la musique ; −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Toute l'imagerie est réelle, de licence claire, et son crédit est lisible dans l'image et listé dans `CREDITS`.
- [ ] Rien n'est dessiné sur le sol ; les marques sont blanches, fines, rares, et collées à leurs coordonnées pendant tout mouvement de caméra (contrôle sur 3 instants d'un zoom).
- [ ] Un seul relevé en couleur d'accent par écran.
- [ ] La mesure est faite sur la date montrée ; méthode, identifiants de scènes et dates dans `FAITS.md`.
- [ ] La couleur vraie n'apparaît qu'en orbite et là où l'histoire tourne.
- [ ] Aucune image figée plus d'1 s ; aucun fondu pour un changement de date.
- [ ] Rien sous 28 px en 9:16, crédit compris ; zones d'interface respectées.
- [ ] Aucun vide comblé par une image générée présentée comme une preuve.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 4
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Film de démo d'origine : https://lemomo-ai.github.io/lemo-opuscar/films/satellite-briefing.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/satellite-briefing.jpg
- Crédit : « The Map Still Says Sea », LemoLab, CC BY 4.0 ; imagerie de tiers (domaine public et licences propres) : **lien seulement**. Démo en 16:9.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/satellite-briefing/STYLE.md`, `style.json`, `demo/engine.js` (`makeCamera()`, `project()`), `demo/overlay.js`, `demo/tools/` (`fetch_landsat.py`, `plates.py`, `vectors.py`).
- Licence : MIT (© 2026 LemoLab) ; film de démo CC BY 4.0.
- Adaptations Flot Web : français, mise en page 9:16, HyperFrames + Three.js, Blender en option.
