# Données au crayon

## 1. Identité

- **Nom** : Données au crayon (le graphique qui raconte).
- **Inspiration** : les présentations de données où un point devient un personnage, les « bandes de réchauffement » (une échelle de couleurs centrée sur une moyenne de référence, sans axes), le journalisme de données à faire défiler (une idée à la fois, des axes qui poussent, des notes épinglées). On n'en recopie ni graphique, ni mise en page, ni police.
- **La règle** : **le graphique est le film**. Chaque marque est un vrai nombre ; chaque mouvement est une opération de graphique qui a un sens (une marque se pose, un axe pousse, l'échelle change, une série se transforme, une note s'épingle). Les données sont réelles, sous licence ouverte, traçables. **On change le cadrage, jamais les nombres.**
- **Trois couches en font une histoire** : une **échelle humaine** (notes manuscrites épinglées aux marques), un **interprète** (un vrai crayon rouge et bleu qui trace chaque marque), et la **sonification** (chaque marque est une note : on entend la tendance avant de la lire).
- **Marche pour** : journalisme de données, rapport annuel, climat et science, bilan d'une activité sur plusieurs années, « un chiffre que les gens croient faux ».
- **Ne marche pas pour** : un sujet sans vraies données, un seul chiffre (voir `nombre-jalon`), un tableau de bord avec dix indicateurs, une présentation commerciale à diapositives (voir `graphique-anime`).

## 2. Palette, typographie, matières

- **La couleur code une seule chose : la valeur.** Données qui s'écartent d'un centre : une échelle divergente bleu-rouge, centrée sur la moyenne d'une période de référence qui a un sens, avec une étendue symétrique. Données sans centre : une seule échelle en dégradé. Tout le reste est de l'encre sur du papier crème.
- **L'honnêteté avant le spectacle** : une valeur pâle reste pâle ; on n'étire jamais l'échelle pour grossir un changement.

| Rôle | Exemple |
|---|---|
| Papier crème | `#f4eedf` |
| Encre chaude (axes, séries) | `#2b2622` |
| Gris chaud pâle (grille, ligne zéro) | `#d8d0c0` |
| Échelle divergente (du froid au chaud) | `#2166ac`, `#67a9cf`, `#f7f7f7`, `#ef8a62`, `#b2182b` |
| Mine bleue / mine rouge | `#2f5fb3` / `#c8332b` |

(Papier, encre et mines : valeurs d'exemple ; l'échelle est la famille bleu-rouge de ColorBrewer.)

- **Les deux mines ont un sens** : **bleu pour les souvenirs et les notes humaines, rouge pour les records et les alertes**. Un changement de mine marque un tournant.
- **Polices** (libres) : Caveat (écriture manuscrite), Newsreader (titre et légende), IBM Plex Mono (graduations, petit repère de période).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Caveat ; EB Garamond à la place de Newsreader ; IBM Plex Mono : déjà fournie. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/caveat`, `@fontsource/newsreader` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : papier crème avec un bruit de fibres fixe et une trame de points très pâle ; chaque point de donnée porte un fin anneau d'encre (les valeurs pâles restent visibles) ; écriture au graphite avec un léger tremblement par lettre ; traits de rappel ondulés qui finissent par un **anneau non fermé** autour de la marque.
- **Le crayon** : corps hexagonal, moitié bleue, moitié rouge, cône de bois taillé. On n'en voit que la pointe, qui entre par le bas à droite ; son ombre s'éloigne et s'adoucit quand il se lève.

## 3. Composition 9:16

- Le cadre vertical est étroit : **choisir le graphique qui tient en hauteur**. Barres horizontales classées, série de points qui monte, bandes empilées, graphique en pente : oui. Longue série chronologique : la faire défiler (la caméra suit la marque la plus récente).
- **Zones** : titre du graphique (c'est le titre du film) entre y 180 et y 380 ; zone de tracé entre y 420 et y 1250, x de 110 à 930 ; **zone mémoire** pour les premières notes, au-dessus ou à gauche du tracé ; bande de légende entre y 1330 et y 1540.
- **Le sous-titre est la légende de la figure** : Newsreader, couleur d'encre, ferré à gauche sur le bord du graphique, 2 lignes au plus, 46 à 52 px, un filet fin au-dessus et un petit repère en chasse fixe (la période tracée jusqu'ici). Les mots apparaissent au moment où ils sont dits.
- Graduations à 28 px au moins ; notes manuscrites à 44 px au moins.
- Quand l'axe réel sort de l'écran, épingler ses graduations sur une bande de papier au bord du cadre (volet figé).
- Pas de légende par-dessus une opération signature ni pendant un silence.

**Choisir le graphique d'après les données :**

| Les données parlent de… | Graphique |
|---|---|
| comparer des catégories, classer | barres, course de barres classées |
| un lien entre deux mesures | nuage de points ou bulles (un point peut être un personnage) |
| un lieu | carte, points sur une carte |
| des parts d'un tout, des nombres de personnes | graphique en unités (gaufre), carrés proportionnels |
| avant → après | graphique en pente, haltères |
| une répartition | histogramme, essaim de points |
| où vont les choses | diagramme de flux |
| une évolution dans le temps | ligne, série de points, bandes, aire |

## 4. Ce qui bouge

- **Action principale** : le crayon pose les marques une à une, au rythme des données.
- **Boucles de fond** : (1) le crayon vit entre deux marques (il se lève avant chaque touche, se pose quand son ombre rejoint la pointe, petit rebond) ; (2) les notes déjà écrites restent épinglées et suivent leur marque à chaque changement d'échelle.
- **Autorisés** : tracé de ligne `#004`, apparition éclair `#001` (une marque se pose avec un petit éclat et une fine onde), compteur `#007`, décalage en cascade `#002`, morphing de forme `#012` (des barres deviennent une gaufre, une carte devient un classement), très gros plan `#184`, travelling de suivi `#029`, zoom `#028` par paliers (crans de cliquet), secousse d'impact `#024` (une valeur crève le cadre), angle penché `#036` qui s'installe peu à peu, plan fixe `#175`.
- **Interdits** : fondu au blanc ou fondu enchaîné `#044`, barres qui poussent toutes ensemble sans ordre, perspective 3D, lueur `#022`, rebond décoratif `#123` sur les données, extrapolation (aucune marque inventée).
- **Jeu du crayon** : il se presse quand les données se resserrent, tremble comme une aiguille de sismographe à un pic ; il peut **sursauter** (recul et arrêt), **hésiter** (planer avant une marque) et **sortir** (laisser l'histoire au spectateur).
- **Casser le cadre** : une valeur hors norme perce le haut du graphique ; l'état percé est tenu au moins un demi-temps avant le changement d'échelle, et le bord déchiré reste comme une cicatrice.
- **La case vide** : un emplacement en pointillés pour la valeur que personne ne connaît encore.

## 5. Rythme et montage

- **Le rythme des données est le rythme du film.** Les marques sont placées sur une grille musicale ; pour accélérer, on divise le temps au lieu de changer de tempo. Choisir un tempo dont la plus petite subdivision tombe sur des images entières (à 30 images par seconde : 120 ou 150 battements par minute).
- Le film est **un seul plan** sur une seule feuille ; une coupe sèche est rare et porte un sens.
- Transitions = opérations de graphique : un axe qui pousse, un recul, un changement d'échelle, un morphing, une case qui s'élargit jusqu'à devenir l'image suivante.
- La voix ne parle jamais par-dessus une accélération, un silence ou un morphing.
- **Version courte (8 à 12 s)** : un seul graphique : le repère (1 s), les marques posées au rythme des données (5 à 6 s), la note manuscrite finale tenue 2 s ; couper les métamorphoses vers un autre graphique. Accroche : la première marque avant 2 s.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D avec `dessiner(t)` ; unités du monde = pixels du graphique à zoom 1 ; caméra 2D `{x, y, zoom, inclinaison}`.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `donnees/` (fichier source + `SOURCES.md` : lien, licence, date), `moteur.js` (papier, caméra, échelles de couleur, trait de crayon, formes à l'encre, texte manuscrit, point de donnée, morphing, notes, crayon, légende), `film.js` (timeline), `partition` (sonification).

```js
// une note est épinglée dans l'espace des DONNÉES : elle survit à tout changement d'échelle
const note = { valeur: { x: 1976, y: 31.2 }, decalage: { dx: 40, dy: -90 }, texte: "l'été de mes dix ans", mine: "bleu" };
const posNote = n => { const p = versEcran(n.valeur); return { x: p.x + n.decalage.dx, y: p.y + n.decalage.dy }; };
// changement d'échelle en crans de cliquet : 4 paliers, chacun amorti
const echelle = p => { const k = Math.min(3, Math.floor(p * 4)); return (k + adoucir(p * 4 - k)) / 4; };
```

- **Pièges** : choisir les colonnes par leur nom, jamais par leur rang, et imprimer chaque fait que la voix affirme pour le vérifier ; des notes placées en pixels percutent les données suivantes ; un cadre percé puis recadré trop vite ne se voit pas ; une note alignée à droite s'écrit quand même de gauche à droite (le crayon saute à la première lettre) ; dans les passages denses, le corps du crayon recouvre les marques fraîches (le redresser) ; une fonction qui règle l'opacité doit multiplier l'opacité reçue, sinon elle échappe aux fondus.

## 7. Son

- **La sonification est la musique** : hauteur = valeur, rythme = densité dans le temps. Les valeurs basses s'accrochent à une gamme pentatonique, les moyennes aux demi-tons, les extrêmes restent libres. Timbre : une note courte et boisée qui devient métallique quand la valeur monte.
- **Fond** : nappe douce, grosse caisse feutrée, shaker, basse très grave ; l'harmonie peut s'assombrir ou s'éclaircir avec les données.
- **Bruitages** (graphite, papier, bois) : touche de crayon sur papier, grattement de l'écriture, règle qui glisse pour un axe, papier percé pour le cadre cassé, clic de bois quand le crayon se retourne, dents de cliquet pour un changement d'échelle.
- **Ambiance** : celle des lieux que les notes évoquent ; elle entre avant l'image et sort après.
- **Silence** : zéro absolu sur toutes les pistes là où la donnée doit s'entendre seule, avant une marque clé, un morphing ou un verdict.
- **Voix** : calme et neutre. Les sons humains de synthèse (un rire) dérangent : préférer un son doux non humain.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Chaque marque correspond à une valeur du fichier source ; la source et sa licence sont notées.
- [ ] La couleur ne code que la valeur ; l'échelle n'est pas étirée.
- [ ] Une idée à la fois : jamais deux graphiques à l'écran.
- [ ] Les axes arrivent quand la voix nomme l'unité, pas avant.
- [ ] Les notes restent accrochées à leur marque après chaque changement d'échelle.
- [ ] Aucun fondu : toutes les transitions sont des opérations de graphique.
- [ ] Le graphique choisi tient en hauteur ; graduations d'au moins 28 px.
- [ ] Les marques tombent sur la grille musicale, sans dérive entre l'image et le son.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 10
- Bleu-violet : interdit
- Texte vivant : oui
- Taille mini du texte : 28

## 9. Aperçu

- Film de démo d'origine, *A Hundred Summers* (50 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/dataviz.mp4
- Affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/dataviz.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, film et images sous CC BY 4.0 (les données de la démo gardent leur propre licence, voir son fichier `CREDITS`).

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichiers `styles/dataviz/STYLE.md`, `DEMO.md`, `demo/engine.js`, `demo/film.js`, `demo/music/score.py`.
- Licence : MIT pour le code et les textes (© 2026 LemoLab), CC BY 4.0 pour le film et ses images. Polices Caveat, Newsreader, IBM Plex Mono : OFL 1.1.
- Adaptation Flot Web : traduction, mise en page verticale, exemples de couleurs, tempo à 30 images par seconde, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
