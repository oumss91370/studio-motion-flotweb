# Plan de métro

## 1. Identité

- **Nom** : Plan de métro (schéma de réseau imprimé sur une vraie feuille).
- **Inspiration** : la tradition des schémas de métro à huit directions, le cartouche tamponné des cartes imprimées, la photographie rapprochée de cartes posées sur une table. On n'en recopie ni mise en page, ni police, ni icône, ni pastille de ligne.
- **Ce qui le fait reconnaître** :
  - **Huit directions seulement** : chaque segment de ligne, de berge ou de côte est horizontal, vertical ou à 45° ; chaque virage a le même rayon. Une ligne ne serpente jamais.
  - **Grandir, c'est tracer** : une ligne existe jusqu'où sa **pointe lumineuse** est arrivée ; les arrêts s'allument au passage ; une correspondance n'apparaît que lorsque la seconde ligne arrive vraiment, et elle se pose avec du poids.
  - **De l'encre sur une feuille** : la carte est imprimée sur un papier qui a du grain, éclairée par une lumière rasante, posée sur une table sombre. La **caméra la voit comme un objet** : en perspective, avec du flou de profondeur, et son bord en plan large.
  - **Les mots sont imprimés** ; les nombres qui courent vivent sur un petit **compteur mécanique**.
- **Marche pour** : transports, croissance d'un réseau dans le temps, tout sujet qui se dessine en réseau (feuille de route d'un produit, parcours professionnel, organisation d'une offre), itinéraire arrêt par arrêt.
- **Ne marche pas pour** : un sujet qui n'a ni étapes ni liaisons, une donnée continue (voir `donnees-crayon`), un système en volume (voir `infographie-isometrique`). Ce n'est pas une carte de ville en 3D, ni une présentation à diapositives.

## 2. Palette, typographie, matières

| Rôle | Couleur (démo d'origine) |
|---|---|
| Papier blanc cassé chaud | `#F2EEE5` |
| Encre (texte, contours des correspondances) | `#1B1C1E` |
| Texte secondaire | `#4A4740` |
| Eau / bord de l'eau | `#BCD6EA` / `#8FB5D6` |
| Noms d'eau | `#5F88AD` |
| Accent de l'histoire | `#E3002B` |
| Neutre de comparaison | marine `#24346E` |
| Table | `#1B1918` |

- **Les couleurs des lignes portent l'identité et rien d'autre.** Un vrai réseau garde ses couleurs publiées ; un réseau inventé prend des teintes réparties autour du cercle chromatique, jamais deux voisines semblables.
- **Le mode de transport se lit à la forme du trait, jamais à la teinte** : métro = trait plein ; tram = trait plein fin ; bus = trait creux (deux bords de couleur, cœur de papier) ; bateau = fil fin sur un couloir de papier, sur l'eau ; sous l'eau ou sous terre = trait en tirets avec deux filets d'encre. **Les tirets veulent dire « dessous »** : un bateau n'est jamais en tirets, un tunnel l'est toujours.
- **Le rouge (ou la couleur de la ligne la plus ancienne) est l'accent de l'histoire** : le premier tronçon, le point « vous êtes ici », le tampon d'un verdict.
- Pour mettre une partie en avant : un **voile de papier** (60 %) sur le reste, jamais un voile sombre.
- **Police** : une grotesque neutre (Inter, libre). Une seule langue par ligne de texte.
- **Police de repli** : aucune à prévoir, Inter est fournie par HyperFrames et se charge par son nom. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : rien à télécharger ; pour embarquer quand même le fichier, `@fontsource/inter` (vérifié par `npm view` le 11/11/2026).
- **Papier** : procédural, attaché au monde (il ne glisse jamais), variation de valeur de ±3 % au plus ; l'encre varie de 7 à 10 % avec le grain, elle n'est jamais plate. Plus fort, la feuille ressemble à du plâtre.
- **Lumière** : une lumière rasante depuis un coin, à 33° environ, neutre, fixe pour tout le film. Un reflet léger n'apparaît que lorsque la caméra penche de plus de 30°.
- **L'unité est le pas de grille, G.** Toutes les tailles en découlent :

| Marque | Géométrie (en G) |
|---|---|
| Ligne | largeur 0,15, bouts ronds ; rayon de virage 0,34 |
| Lignes parallèles dans un même couloir | décalées de ±0,10 autour de l'axe commun |
| Arrêt | disque blanc de rayon 0,085, anneau de 0,046 de la couleur de la ligne |
| Correspondance | capsule blanche qui enveloppe tous les points de la station (marge 0,13), contour d'encre de 0,055 ; jamais tournée à 45° |
| Fleuve | bande de 0,76 avec un bord plus sombre de 0,025 |
| Tunnel sous l'eau | tirets de 0,16 espacés de 0,11, deux filets d'encre à 55 % |
| Pointe | cœur blanc de rayon 0,11, anneau de couleur, halo doux de rayon 0,8 |
| Pastille de ligne | disque de rayon 0,25 (métro) ou carré arrondi de 0,48 (bus, bateau), chiffre en très gras |
| Véhicule | capsule blanche de 0,40 × 0,14 à trois fenêtres, environ 2 G par seconde |

## 3. Composition 9:16

- **Dessiner le réseau en hauteur** : un réseau d'environ 22 × 34 G sur une feuille en portrait (avec des marges pour le cartouche). Les lignes qui montent et descendent servent le cadre ; un fleuve qui traverse à l'horizontale donne un seuil à franchir.
- **Le zoom se lit en pixels par G** au point visé. En 1080 de large : 110 à 200 px par G quand on suit une pointe ; 45 à 70 pour le réseau entier.
- **Lisibilité mesurée là où le texte tombe** (taille sur la feuille × zoom, réduite par l'inclinaison) : un texte à lire fait **au moins 28 px** à l'écran. En dessous, on le cache par niveau de détail ou l'on déplace la caméra.
- **Niveaux de détail par le zoom**, jamais par le temps : en reculant, les petits arrêts et leurs noms s'effacent d'abord, puis les noms des correspondances ; les grands pôles gardent leur nom à toute échelle et grossissent.
- **Étiquettes** : halo couleur papier sous chaque nom ; placées **une seule fois, contre le réseau terminé**, avant la première image : un nom ne saute jamais quand une ligne arrive.
- **Le compteur** : une plaque émaillée sombre à rouleaux crème, en haut à gauche, **sous y 160** (largeur d'environ 560 px, rangées de 86 px). Rien d'important dessous.
- **Encadrés imprimés** : une barre de couleur, la date en chiffres très gras, une ligne de texte ; ils se découvrent depuis la barre en 0,5 s environ.
- **Le titre du film est imprimé sur la carte** (le cartouche, une pastille de ligne, une plaque de station près de l'objectif), jamais un carton flottant. **Le film se termine sur le réseau entier**, toutes les lignes tracées, le titre de fin imprimé dans une marge.
- Le sujet est décentré, avec de l'espace devant une pointe qui avance. Sous-titres : sur une bande de papier imprimée, entre y 1400 et y 1540.

## 4. Ce qui bouge

- **Action principale** : une pointe lumineuse trace une ligne à l'allure de la caméra ; les arrêts s'allument derrière elle.
- **Boucles de fond** : (1) les véhicules (capsules blanches à vitesse constante, une tous les 4 G, seulement sur les voies terminées) ; (2) le compteur dont les rouleaux tournent, et l'anneau qui bat autour du point « vous êtes ici ».
- **Autorisés** : tracé de ligne `#004`, apparition éclair `#001` avec dépassement `#010` (arrêt : de 0,6 fois à sa taille en 0,28 s, avec un anneau qui s'élargit), compteur `#007`, suivi `#174` de la pointe (en visant 1,5 G devant elle), travelling de suivi `#029`, grue `#031`, panoramique vertical `#026`, bascule de mise au point `#033` et flou de profondeur `#105`, raccord de forme `#042` sur des formes rondes (un phare, une lampe, une pièce devient un point de station), plan d'ensemble `#183`, vue du dessus `#181`, plan fixe `#175`.
- **Interdits** : roulis de caméra `#170`, fondu au noir `#187` en cours de film, tourné de page `#140`, toute géométrie hors des huit directions, lueur (sauf le halo de la pointe), bâtiments en volume, voile sombre, compteur qui affiche des valeurs intermédiaires lisibles.
- **La correspondance qui tombe** : quand deux lignes se rencontrent pour la première fois, la capsule tombe sur le papier en 0,4 s environ (depuis 3,4 fois sa taille, son ombre décalée et floue, qui se précise à l'atterrissage), puis des anneaux aux couleurs des deux lignes s'élargissent pendant 0,9 s.
- **Le tunnel sous l'eau** : dans la bande d'eau, la ligne passe en tirets ; la caméra descend bas (inclinaison d'environ 60°) pour la regarder traverser.
- **Le compteur ne se pose que sur des valeurs sourcées** ; entre deux, les rouleaux tournent flous. Prévoir environ une valeur posée toutes les 2 s.
- Ce qui ne bouge jamais : ce qui est déjà construit, la position des noms, le papier et sa lumière.

## 5. Rythme et montage

- 30 images par seconde. Une pointe peut ralentir sur une station et accélérer entre deux ; elle ne s'arrête jamais net au milieu d'un segment. Vitesse de la pointe × zoom : pas plus de 500 px par seconde à l'écran.
- **Environ un événement nouveau toutes les 3 à 5 s** : une ligne, une correspondance, une valeur posée, un encadré.
- Plan fixe pour un verdict : tenir 2,5 s au moins avant.
- Transitions : raccord sur des formes rondes, glissement sur la feuille vers un autre encadré, coupe sèche vers un autre panneau.
- **La carte est assez pleine pour porter le film** :

| Sujet | Lignes | Stations nommées | Correspondances | États datés |
|---|---|---|---|---|
| Un réseau entier, 30 à 60 s | 5 au moins | 40 au moins | 8 au moins | 4 au moins, chacun avec une valeur sourcée |
| Une ligne ou un trajet, jusqu'à 20 s | la ligne + 3 qu'elle croise | 8 sur la ligne | 3 au moins | 2 au moins |
| Un sujet dessiné en réseau | 4 au moins | 20 au moins | 4 au moins | 3 au moins |

- **Version courte (8 à 12 s)** : une ligne et deux correspondances : la pointe trace pendant 6 s, deux arrêts s'allument, une valeur se pose, plan fixe du verdict 2,5 s ; couper le réseau entier. Accroche : la pointe part à l'image 0.

## 6. Recette technique

- **Moteur** : HyperFrames en deux passes : un canvas 2D encre la région de la feuille que la caméra voit, puis une passe WebGL la pose sur un plan en perspective, l'imprime sur le papier, l'éclaire et calcule le flou. **Variante `blender`** (conseillée si la qualité du flou et de la lumière compte) : exporter la carte animée en suite d'images, l'appliquer comme texture sur un plan posé sur une table, et animer une vraie caméra à faible profondeur de champ.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `reseau.js` (stations : position en G, nom, niveau ; lignes : liste de stations, couleur, mode ; eau ; liaisons à pied), `moteur.js` (tracé à huit directions, virages, longueur d'arc, formes de lignes, capsules, placement des noms, caméra), `chronologie.js` (phases de tracé, caméra en fonction du temps, repères sonores), `FAITS.md`.

```js
// relier deux points en restant sur les 8 directions : un tronçon droit puis une diagonale (ou l'inverse)
function relier(a, b, diagonaleDabord = false) {
  const dx = b.x - a.x, dy = b.y - a.y, d = Math.min(Math.abs(dx), Math.abs(dy));
  const coude = diagonaleDabord ? { x: a.x + Math.sign(dx) * d, y: a.y + Math.sign(dy) * d }
                                : { x: b.x - Math.sign(dx) * d, y: b.y - Math.sign(dy) * d };
  return [a, coude, b];                      // puis arrondir chaque angle au rayon 0,34 G et VALIDER chaque segment
}
// flou de profondeur calculé : rayon = ouverture × |profondeur − mise au point| ÷ profondeur, plafonné à 26 px
const flou = (ouverture, z, zNet) => Math.min(26, ouverture * Math.abs(z - zNet) / z);
```

- **Caméra** : champ vertical de 32°, visant un point de la feuille ; inclinaison de 0° (vue du dessus, sans flou) à 65° au plus (plus bas, la feuille ne se lit plus comme une carte).
- **Techniques clés** : tout ce qui dépend du temps est calculé une fois avant la première image (quand chaque pointe passe chaque station, quand une station devient correspondance, où vont les noms) ; le papier d'un cœur de bus ou d'un couloir de bateau est **gommé** dans le calque d'encre (`destination-out`), jamais peint ; ordre d'encrage : eau, lignes de surface, lignes de rail, arrêts et capsules, noms.
- **Pièges** : un seul segment hors des huit directions casse le style ; des noms placés contre ce qui est déjà tracé sautent à chaque nouvelle ligne ; une vue du dessus pendant tout le film se lit comme un diaporama (l'inclinaison, le flou et le bord de la feuille font l'objet) ; un compteur qui interpole invente des nombres ; texture d'encre réutilisée sans remise à zéro de la transformation : l'encre de l'image précédente fait un fantôme.

## 7. Son

- **Musique** : percussions accordées (glockenspiel, marimba, vibraphone). Un **carillon de station à deux notes** sert de motif et revient aux tournants.
- **Une voix par ligne** : chaque nouvelle ligne ajoute un instrument à un motif qui tourne (flûte, cordes, xylophone, cor, harpe) : l'arrangement grandit avec le réseau. On accélère en ajoutant des voix, pas en changeant de tempo.
- **Bruitages** : glissement de feutre sous chaque pointe ; roues de train par paires ; cliquetis du compteur ; un mixage filtré, « sous l'eau », pendant qu'une ligne passe sous un fleuve ; un sifflement descendant et un coup grave pour une capsule qui tombe. Un arrêt = une note pincée (c'est la musique, pas un bruitage en plus).
- **Silence** : un temps de quasi-silence avant un verdict ; la fin se réduit à une nappe et au carillon.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Tous les segments sont à 0°, 45° ou 90°, avec le même rayon de virage.
- [ ] Les lignes ne grandissent que par leur pointe ; rien de déjà tracé ne bouge.
- [ ] Le papier a du grain, mais discret ; la feuille est vue au moins une fois inclinée, avec du flou et son bord.
- [ ] Les noms ne sautent jamais et les textes à lire font au moins 28 px.
- [ ] Le mode de transport se lit à la forme du trait, pas à la couleur.
- [ ] Le compteur ne s'arrête que sur des valeurs sourcées, notées dans `FAITS.md`.
- [ ] Le titre est imprimé sur la carte ; le dernier plan montre le réseau entier.
- [ ] Un réseau inventé le dit à l'écran ; un réseau réel n'utilise ni logo ni pastille de marque, et se présente comme un hommage non officiel.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 9
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu

- Film de démo d'origine, *6 Kilometres* (47 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/transit-map.mp4
- Affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/transit-map.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, film et images sous CC BY 4.0 (les données du réseau montré gardent leurs propres sources, voir le fichier `CREDITS` de la démo).

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichiers `styles/transit-map/STYLE.md`, `DEMO.md`, `demo/gl.js`, `demo/film.js`, `demo/net.js`, `demo/timeline.js`.
- Licence : MIT pour le code et les textes (© 2026 LemoLab), CC BY 4.0 pour le film et ses images. Police Inter : OFL 1.1.
- Adaptation Flot Web : traduction, feuille en portrait et seuils de lisibilité recalculés, une seule langue par ligne (la règle bilingue de la démo est retirée), variante Blender, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
