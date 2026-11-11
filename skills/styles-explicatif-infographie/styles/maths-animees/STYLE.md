# Maths animées (style 3Blue1Brown)

## 1. Identité

- **Nom** : Maths animées. « Style 3Blue1Brown » désigne une inspiration (la vulgarisation mathématique animée sur fond noir, faite avec la bibliothèque libre manim) ; ce n'est ni un contenu officiel, ni une affiliation.
- **Fiche fusionnée** de deux sources : la grammaire « transformation » de huashu (ce qu'on montre et dans quel ordre) et le style « math » du plugin animate de cth9191 (typographie, liste de contrôle, mise en page verticale).
- **La règle en une phrase** : sur fond noir, **on ne montre que la chose dont on parle** ; une **transformation lisse** change directement l'idée précédente en la suivante ; **une couleur = le nom d'un concept** ; presque aucune coupe.
- **Marche pour** : un mécanisme qui « devient autre chose étape par étape » (réseau de neurones, attention, transformation de matrice, descente de gradient, probabilités, déroulé d'un algorithme) ; une idée qui a une image (une formule, une preuve, une fonction, un taux, un fait de géométrie). Idéal quand la voix dit des **phrases d'action** : « on aplatit cette image en une colonne », « chaque pixel est multiplié par un poids ». Une phrase = une transformation.
- **Ne marche pas pour** : un lancement de produit ou un film d'émotion (fond noir et traits fins : trop froid, trop lent) ; une vraie tendance chiffrée (voir `graphique-anime`) ; une opinion, une histoire, une phrase choc (rien à transformer : voir `typo-cinetique` ou `tableau-blanc-a-la-main`) ; un montage très rapide.
- **Le look promet la rigueur** : il ne marche que si les maths à l'écran sont vraies.

## 2. Palette, typographie, matières

| Rôle | Couleur |
|---|---|
| Fond | noir pur `#000000` (variante douce : `#0E0E10`). Jamais un bleu marine en dégradé |
| Bleu | `#58C4DD` |
| Rouge | `#FC6255` |
| Jaune | `#F7D96F` (le jaune pur `#FFFF00` : seulement pour un éclair) |
| Vert | `#83C167` |
| Sarcelle | `#5CD0B3` |
| Gris (axes, repères, guides) | `#BBBBBB`, `#888888`, `#444444` |
| Blanc (opérateurs `+ = ( )`, texte neutre) | `#FFFFFF` |
| Lignes du quadrillage | bleu `#29ABCA` à 14 à 42 % d'opacité |

- **Saturation** : la source d'origine pousse la saturation de l'ensemble à 1,5 à l'export ; utilisées telles quelles sur fond noir, ces couleurs paraissent grises. Pousser la saturation à l'export (voir `rendu`), pas dans les codes.
- **Une couleur = un concept, pour tout le film** : la même dans la formule, sur la figure, dans les étiquettes, les valeurs affichées et les sous-titres. **Quatre couleurs de sens au plus.** Exemple : jaune = signal ou résultat, bleu = poids positif ou paramètre, rouge = poids négatif ou grandeur 1, vert = grandeur 2. **Écrire ce tableau avant de commencer.**
- Remplissages : la couleur du trait à 14 à 35 % d'opacité.
- **Polices** (libres) : une police à empattement de type « Computer Modern » pour formules et texte (Latin Modern Roman, CMU Serif ou STIX Two Text ; il faut une **vraie italique**) ; JetBrains Mono pour le code.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de STIX Two Text ; JetBrains Mono : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/stix-two-text` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. Latin Modern Roman et CMU Serif n'ont pas de paquet `@fontsource` (404 le 11/11/2026) : à vérifier, sinon STIX Two Text.
- **Conventions des formules** : variables en italique ; chiffres, noms de fonctions (`cos`, `sin`, `log`) et unités en romain ; espaces autour des opérateurs ; exposants à 0,6 de la taille ; un vrai signe moins « − » ; virgule décimale en français.
- **Traits** : 4 px par défaut ; axes et liaisons 2 px ; subdivisions 1 px à 25 % d'opacité. Dans un réseau : neurone = cercle à bord blanc de 2 px dont **l'opacité de remplissage est la valeur d'activation** ; épaisseur d'une liaison selon la force du poids.
- **Matières** : aucune. Ni grain, ni tremblement, ni ombre, ni dégradé derrière les maths, ni texture. **Presque aucune lueur** : l'impression de lumière vient de traits fins très saturés sur du noir.
- **Personnage** : facultatif. Si l'on veut un témoin qui regarde les maths, dessiner **son propre** petit personnage géométrique (la mascotte en forme de lettre pi est la signature de la chaîne d'origine : on ne la reprend pas). Sa couleur n'est jamais celle d'une grandeur.

## 3. Composition 9:16

- **Tout tient dans x 60 à 940, y 250 à 1500.**
- **De haut en bas** : la formule en haut (y 280 à 480) ; la figure au milieu (y 520 à 1200) ; les valeurs affichées en bas à gauche ; le personnage éventuel en bas à droite (à gauche de x 940) ; le sous-titre centré à y 1440, sur un rectangle noir à 75 % d'opacité.
- **Tailles** : formule principale 90 à 110 px ; seconde ligne 60 à 70 px ; étiquettes sur une figure 40 à 52 px ; graduations 28 à 32 px ; sous-titres 50 px. **Rien sous 28 px.**
- **Une idée par image** : une formule qui s'écrit, une figure qui se construit, ou une transformation. Si deux choses bougent, c'est la même étape sous deux formes (l'équation et son image).
- **Pas plus de deux points à l'écran** à la fois : avant le troisième, les précédents deviennent une image ou s'en vont. Des points écrits en liste, c'est un diaporama sur fond noir.
- **La première image est l'objet** (repère, quadrillage, courbe) ; le titre et la formule viennent après.
- Aucune étiquette sur un trait ni sur une autre étiquette ; elles se placent du côté du segment qui s'éloigne de la figure.
- **Une vie de fond discrète et vraie** : quadrillage pâle, graduations, cases unité, marque d'angle droit, repère de section : trois éléments au moins, tous à faible contraste.

## 4. Ce qui bouge

- **Action principale** : une **transformation** : deux formes rééchantillonnées au même nombre de points, départs alignés, interpolées point par point avec leur couleur (une grille de carrés devient une colonne de cercles ; le carré construit sur un côté devient un cercle). Pour chaque plan, **écrire « qui devient quoi »** ; si l'on ne peut pas, ce n'est pas le bon style.
- **Boucles de fond** : (1) un point traceur qui parcourt une courbe, avec sa valeur affichée recalculée à chaque image ; (2) un signal qui court le long des liaisons (une copie jaune, un peu plus épaisse, dont on ne voit qu'un tronçon). **Pendant une pause, l'image est immobile** : ni poussée lente, ni respiration, ni flottement. C'est la grande différence avec une keynote.
- **Autorisés** : morphing de forme `#012`, tracé de ligne `#004` (axes d'abord, graduations ensuite, étiquettes en dernier ; une forme fermée trace son bord puis se remplit), courbes d'accélération `#009`, décalage en cascade `#002`, trajectoire `#126`, compteur `#007` (valeur honnête, à la précision affichée), travelling avant `#027` (un seul, lent, vers l'objet suivant, puis arrêt ; une poussée rapide de 0,28 s seulement quand une conclusion tombe), zoom à travers `#020`, orbite `#030` très lente (1° par seconde) uniquement pour une relation dans l'espace, plan fixe `#175`.
- **Interdits** : lueur diffuse et dégradés de fond, particules `#015`, rebond `#123` et dépassement `#010`, tremblement `#124`, texte tapé comme dans un terminal `#006`, apparition éclair `#001` d'une formule, mouvement linéaire (sauf l'écriture et une valeur pilotée), fondu enchaîné `#044` entre deux idées qui pourraient se transformer.
- **Courbe par défaut** : la courbe « lisse » de manim, `6t⁵ − 15t⁴ + 10t³` (vitesse et accélération nulles aux deux bouts), pour presque tout.
- **Écrire** : chaque caractère trace d'abord son contour (première moitié), puis se remplit (seconde moitié), de gauche à droite. Les formules s'écrivent ; elles ne surgissent jamais.
- **Transformer une équation** : les termes qui restent glissent à leur nouvelle place ; ceux qui changent se fondent en chemin ; un terme qui change d'identité garde sa couleur.
- **Souligner** : teinter en jaune avec un aller-retour d'échelle ; pas de halo.

## 5. Rythme et montage

- **Une animation de 1 à 3 s, puis 1 s d'arrêt.** Durées types : écriture 0,7 à 1 s ; tracé 0,5 à 1 s ; transformation 0,8 à 1 s ; apparition 0,3 à 0,5 s ; éclair 0,4 à 0,5 s. Décalage entre objets frères : la moitié de la durée.
- Un concept occupe 8 à 20 s. Trois concepts en 8 s est un maximum de démonstration : dans une vraie vidéo, **compter 2 à 3 fois plus long**.
- **Une phrase = une animation** : elle commence quand la voix dit le verbe d'action ; à la fin de la phrase, 1 s d'arrêt pour regarder.
- La question s'écrit **avant** l'action (on demande, puis on montre) ; la formule apparaît avec la figure, dans les mêmes couleurs ; une valeur n'arrive pas avant l'image qui la justifie.
- **Transitions** : (1) **la transformation continue** : la dernière image d'un plan est la première du suivant, au pixel près (c'est la transition principale) ; (2) **zoom à travers** un objet dont le bord s'ouvre sur la nouvelle image (annoncer d'abord l'objet en le teintant de jaune 0,3 s) ; (3) tout part vers le haut en fondu, le nouveau arrive du bas, pour changer de sujet ; (4) les symboles de l'ancienne formule glissent vers leurs homologues de la nouvelle.
- Tempo conseillé à 30 images par seconde : 150 battements par minute (une croche = 6 images) ou 120 en restant sur les temps (15 images).
- « Chaque mouvement à l'écran doit être voulu et avoir un but identifiable » : ce qui n'explique rien se supprime.
- **Version courte (8 à 12 s)** : un seul concept : une écriture (1 s), une transformation (1 s), 1 s d'arrêt, le résultat encadré tenu 2 s ; couper la seconde ligne de calcul et le zoom à travers. Accroche : la formule s'écrit dès l'image 0.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D avec `dessiner(t)` (ou SVG pour des figures simples). Unité de dessin : la hauteur de la zone utile = 8 unités.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `couleurs.js` (le tableau grandeur → couleur), `maths.js` (mise en page des formules par jetons, écriture, transformation par identifiant de terme), `traits.js` (segment, tracé progressif, flèche, accolade, angle droit, arc), `reperes.js` (axes, quadrillage, courbe, lignes de rappel), `traceur.js` (point, valeur affichée), `film.js`.

```js
const lisse = t => t * t * t * (t * (6 * t - 15) + 10);                       // la courbe par défaut
const decale = (p, i, n, r = 0.1) => borner(p * (1 + (n - 1) * r) - i * r);   // départs en cascade
// transformation : deux contours au même nombre de points, départs alignés (haut-gauche, sens horaire)
const morph = (A, B, u) => A.map((a, i) => ({ x: a.x + (B[i].x - a.x) * lisse(u), y: a.y + (B[i].y - a.y) * lisse(u) }));
// écrire un caractère : contour (première moitié), puis remplissage (seconde moitié)
function ecrire(ctx, glyphe, p) { tracerContour(ctx, glyphe, borner(p * 2)); ctx.globalAlpha = borner(p * 2 - 1); remplir(ctx, glyphe); }
// la valeur affichée vient du MÊME traceur que le point
const theta = cle([[0, 0], [4, Math.PI / 2]])(t); point(cos(theta), sin(theta)); afficher("cos²θ + sin²θ", arrondir(cos(theta) ** 2, 2) + (1 - arrondir(cos(theta) ** 2, 2)));
```

- **Techniques clés** : chiffres à largeur fixe ; arrondir de façon que **le calcul affiché tombe juste** ; construire la figure dans l'ordre du raisonnement (côtés, carrés, cases, compte, somme) ; relier deux parties par une forme qui **est** l'idée suivante.
- **Pièges** : ajouter des lueurs et un fond bleu « pour faire comme l'original » (l'original est noir, net, presque sans lueur : avec des lueurs, on obtient un diaporama « technologique ») ; tout en linéaire, vite et trop ; une couleur qui change de sens en cours de route ; une étiquette de graduation là où la courbe coupe l'axe ; une erreur de logique dans ce qu'on dessine (relire ce que chaque objet représente : un relecteur l'a trouvée dans la démo d'origine).

## 7. Son

- **Musique** : calme et régulière : piano, cordes légères, nappe douce ; elle laisse toute la place à la voix.
- **Bruitages** : très peu, très discrets : un frottement de craie ou de crayon sur une écriture, une note douce quand une transformation se pose, un tintement sur l'éclair du résultat. Deux ou trois pour 10 s.
- **Silence** : la seconde d'arrêt après chaque animation est un vrai repos sonore (musique seule, bas).
- **Voix** : c'est elle qui porte ; posée, curieuse. La méthode d'origine : régler les animations d'abord, enregistrer la voix ensuite.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Fond noir uni ; aucune lueur diffuse, aucun dégradé, aucune texture.
- [ ] Chaque grandeur a une seule couleur, la même partout ; quatre couleurs de sens au plus.
- [ ] Une idée par image ; deux points de texte au plus à l'écran.
- [ ] Les formules sont écrites (contour puis remplissage), composées proprement : italique, exposants, vrai signe moins.
- [ ] Les nombres affichés sont ceux que montre la figure, et le calcul arrondi tombe juste.
- [ ] Chaque mouvement correspond à une étape du raisonnement.
- [ ] L'image est immobile pendant les pauses ; une animation de 1 à 3 s puis 1 s d'arrêt.
- [ ] Tout tient dans x 60 à 940, y 250 à 1500 ; rien sous 28 px.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 13
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu

- Grammaire « transformation », planche de la démo (une image par plan, 16:9) : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/t1_3b1b_总览.jpg — crédit : 花叔 Huashu (alchaincyf).
- Style « math » en vertical, image d'exemple (540×960) : https://github.com/cth9191/animate/blob/main/plugins/animate/skills/animate/styles/math/sample.png — crédit : cth9191.

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichiers `references/动画语法/t1_3b1b.md`, `scripts/engine/demos/t1_3b1b/`, `scripts/engine/lib/diagram.js`, `motion.js`. Licence MIT (© 2026 alchaincyf, 花叔).
- Dépôt `cth9191/animate`, commit `7e5eb56` (version 0.4.0), fichiers `plugins/animate/skills/animate/styles/math/STYLE.md`, `kit.js`, `demo/`. Licence MIT (© 2026 cth9191).
- Couleurs et courbe « lisse » : constantes de la bibliothèque manim (licence MIT).
- Adaptation Flot Web : fusion des deux sources, traduction du chinois et de l'anglais, mascotte d'origine retirée, tempo à 30 images par seconde, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
