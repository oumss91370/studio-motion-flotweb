# Grille suisse

## 1. Identité

- **Nom** : Grille suisse (typographie suisse en mouvement).
- **Inspiration** : les affiches zurichoises des années 1950 à 1970 (grille modulaire, texte ferré à gauche, contraste d'échelle) et les identités de marque animées d'aujourd'hui, qui claquent sur le temps. On apprend la grammaire, on ne recopie aucune affiche historique (pas de cercles concentriques ni de compositions en éventail reprises telles quelles) et on n'utilise ni Helvetica ni Akzidenz.
- **Ce qui le fait reconnaître** : du papier plat, du noir, un gris très clair et **une seule** couleur vive ; tout est posé sur une grille ; tout mouvement arrive sur un temps ; rien ne rebondit ; un chiffre géant à côté de notes minuscules. Et une exception : un seul élément désobéit à la grille, et devient le personnage.
- **Marche pour** : identité de marque, annonce d'événement, règles ou étapes numérotées, comparaison avant/après, leçon de design, programme, horaires.
- **Ne marche pas pour** : une histoire à émotion ou à personnage, un produit qu'il faut montrer en volume, un public enfant. Ce n'est pas non plus une keynote (pas de dégradé ni de lueur), ni de la typo cinétique de clip (les mots ne volent pas, ne tournent pas), ni un graphique de données.

## 2. Palette, typographie, matières

Papier, encre, gris, et **une** couleur signal choisie pour le sujet, jamais une deuxième. Une seule chose porte la couleur : c'est le héros, et le seul élément qui a le droit d'être inexact. Le noir peut être imprimé par-dessus la couleur.

| Jeu | Page | Papier | Encre | Signal |
|---|---|---|---|---|
| Rouge | `#EAE9E5` | `#FFFFFF` | `#111111` | `#E30613` |
| Orange | `#F2F0EA` | `#FFFFFF` | `#141414` | `#FF5A00` |
| Outremer | `#E9ECEF` | `#FFFFFF` | `#0B0B0B` | `#1F3FFF` |

- **Police** : une seule famille pour tout le film, une grotesque libre (Archivo, Inter, Schibsted Grotesk, Instrument Sans), en plusieurs graisses. Interlettrage d'environ −2 % au-dessus de 90 px. Les titres peuvent être en minuscules.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place d'Archivo et de Schibsted Grotesk et d'Instrument Sans ; Inter : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/archivo`, `@fontsource/schibsted-grotesk`, `@fontsource/instrument-sans` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : aucune. Pas de dégradé, pas d'ombre, pas de particule, pas de grain. Les lignes de grille existent en deux ou trois gris clairs. Une « seconde voix » est possible avec des éléments gris clair placés sous les noirs.

## 3. Composition 9:16

- **Grille verticale** : 6 colonnes sur 1080 px, marges de 72 px, gouttières de 24 px, ligne de base de 24 px : chaque colonne fait 136 px, la n-ième commence à x = 72 + (n − 1) × 160. (En 16:9 : 12 colonnes, marges de 96 px.)
- **La 6e colonne ne porte que du décor** : elle va de x 872 à x 1008 et sort de la zone utile (x ≤ 945, sous la colonne de boutons des applications). Tout texte à lire tient dans les colonnes 1 à 5 (x 72 à 848) ; un texte qui commence en colonne 5 s'arrête à x 945. Seuls une ligne de grille, un filet, un aplat ou un objet décoratif vont en colonne 6.
- **La double page devient un empilement** : en haut le « programme » (chiffre géant, règle, notes), en bas « l'objet » fabriqué par la règle. La cause est en haut, l'effet en bas.
- Zone utile : y de 160 à 1560, x de 72 à 945 (la marge gauche de la grille, 72 px, est à l'intérieur de la limite du studio, x 60). Le chiffre géant peut dépasser du cadre à gauche ou en haut : c'est un fond perdu voulu.
- **Tailles** : chiffre géant 500 à 900 px ; affirmation en gras 96 à 140 px ; amorce grise 40 à 48 px ; notes techniques 28 à 30 px avec un filet de 1 px au-dessus (jamais sous 28 px : c'est le plancher du contrôle `check` ; la source descendait à 26). Ces notes sont des cartels, plus petits que les 50 px habituels du studio : c'est voulu, et déclaré dans les réglages de la section 8. Une note qui ne fait que passer (relevé de coordonnées qui défile) se marque `data-passage`.
- **Sous-titres dans la mise en page** : pas de bandeau en bas. Chaque phrase se pose au début d'une colonne de la composition en cours (petite amorce grise + grande affirmation en gras, ou une légende façon cartel de musée).
- Tout ferré à gauche, en drapeau à droite. Les chiffres géants sont alignés **optiquement** (on retire l'approche gauche du glyphe). Le blanc fait partie de la composition.

## 4. Ce qui bouge

- **Action principale** : une règle s'applique à l'objet, et la grille le recompose. Chaque arrivée est un claquement sur le temps.
- **Boucles de fond** : (1) une tête de lecture ou un compteur de mesures qui avance en linéaire dans un coin ; (2) l'exception, seul élément qui dérive lentement hors grille, avec un relevé de coordonnées qui passe de « sur grille » à « hors grille ».
- **Autorisés** : révélation par masque `#005`, tracé de ligne `#004`, décalage en cascade `#002`, compteur `#007`, panoramique sec d'une page ou d'une colonne `#025`, volet `#045`, poussée `#137`, écran partagé en cellules égales `#144`, plan fixe `#175`.
- **Interdits** : dépassement `#010`, rebond `#123`, écrasement `#011`, tremblement `#124`, fondu enchaîné `#044`, particules `#015`, parallaxe `#016`, caméra à l'épaule `#034`.
- Deux courbes seulement : `cubic-bezier(.7,0,.2,1)` pour les claquements, linéaire pour les lignes qui se tracent, la tête de lecture et l'exception.
- Les entrées sont des volets ou des masques, jamais des fondus : les mots montent de sous leur ligne de base et sortent par le haut ; les lignes poussent dans leur longueur ; les chiffres grimpent par paliers, un module à la fois.
- **Suppression au couteau** : une ligne fine traverse l'élément, puis il s'effondre sur sa médiane.
- Les réactions en chaîne partent du plus proche de la cause vers le plus loin.

## 5. Rythme et montage

- Les durées sont des valeurs de notes au tempo du film. Un claquement **part une valeur de note avant et atterrit sur le temps**.
- Plans de 2 à 6 s, un par règle ou par étape. Animation fluide à 30 images par seconde, aucune saccade : c'est une précision de machine, pas de fait main.
- Transitions : volets, coupes au couteau, déplacements de caméra sur la grille, recomposition. Jamais de fondu.
- Un seul vrai changement de régime : le moment de l'exception (la batterie se tait, l'élément se déplace en linéaire).
- Ordre conseillé dans un plan : faire pivoter, tenir, puis seulement étiqueter. Faire les deux à la fois se lit comme du bruit.
- **Version courte (8 à 12 s)** : trois règles au plus (2,5 à 3 s chacune) et l'exception pour finir ; couper les notes techniques secondaires et la tête de lecture. (Découpage tenu dans le rendu réel du 11/11/2026.)

## 6. Recette technique

- **Moteur** : HyperFrames. Deux voies : éléments HTML/CSS animés par GSAP (le plus simple, texte net), ou canvas avec `dessiner(t)` si les barres sont nombreuses.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `grille.js` (colonnes, lignes, fonction `col(n)` et `ligne(n)`), `scene-*.html` (une règle par scène), un fichier de données commun à l'image et à la musique (une colonne = une hauteur de note, une ligne = un départ).

```js
gsap.registerPlugin(CustomEase, SplitText);
CustomEase.create("net", ".7,0,.2,1");                 // suffit : la courbe s'appelle ensuite par ease: "net"
const temps = n => n * 60 / BPM;                       // n en temps
// le mot monte hors de son masque et atterrit sur le temps 4
tl.fromTo("#mot1 span", { yPercent: 110 }, { yPercent: 0, duration: temps(0.5), ease: "net" }, temps(4) - temps(0.5));
// suppression au couteau
tl.fromTo("#trait", { scaleX: 0 }, { scaleX: 1, duration: temps(0.25), ease: "none" }, temps(8))
  .to("#bloc", { scaleY: 0, transformOrigin: "50% 50%", duration: temps(0.25), ease: "net" });
```

- **Extrait vérifié par un rendu réel** (11/11/2026, GSAP 3.15.0 et `SplitText` 3.15.0, fichiers `gsap.min.js`, `CustomEase.min.js` et `SplitText.min.js` du même dossier `dist/` ; **`SplitText` n'est pas embarqué par HyperFrames**, contrairement à GSAP et CustomEase : il vient du réseau, ou d'une copie posée dans `assets/vendor/`, voir le skill `rendu`, section « GSAP : version et chargement ») : le texte se découpe **après** le chargement des polices, et la timeline ne s'enregistre qu'ensuite ; `check`, `snapshot` et `render` attendent cet enregistrement tardif.

```js
document.fonts.ready.then(() => {
  const decoupe = SplitText.create("#regle-1", { type: "lines, words", mask: "lines" });
  tl.from(decoupe.words, { yPercent: 105, duration: temps(0.5), ease: "net", stagger: 0.05 }, temps(4));   // entrée
  tl.to(decoupe.words, { yPercent: -105, duration: temps(0.5), ease: "net" }, temps(9) - temps(0.5));     // sortie par le haut
  tl.set({}, {}, DUREE);                       // la timeline dure tout le film
  window.__timelines["main"] = tl;            // enregistrée seulement maintenant
});
```

- **Interligne d'au moins 1,2 avec `mask: "lines"`** : à 96 px de corps et 100 px d'interligne, le masque coupe les jambages (g, q, p, virgule) et `check` sort `text_box_overflow` ; à 118 px d'interligne, plus rien n'est coupé (mesuré sur le rendu).
- **Techniques clés** : le masque est un parent en `overflow:hidden` ; les cellules voisines d'une même unité fusionnent en une barre ; une caméra 2D (centre, échelle, rotation) appliquée à un seul conteneur.
- **Pièges** : les barres fusionnées montrent des fentes après rotation ou mise à l'échelle, il faut les recouvrir de 1 px ; un départ visuel placé entre deux images clignote, il faut le caler sur une image entière ; trop de colonnes fines donnent l'air d'un graphique, il faut moins de modules et plus larges ; charger chaque graisse avant de mesurer un texte.

## 7. Son

- **Musique** : une pulsation régulière dont les subdivisions donnent les durées des claquements. Pistes possibles : batterie et basse « motorik », techno minimale, motifs de marimba ou de vibraphone, ostinato de piano mécanique, boîte à rythmes et glockenspiel. Ajouter un instrument par règle donne une montée claire.
- **Bruitages** (secs, proches, sans réverbération, la matière de l'imprimerie) : claquement de presse typographique, tire-ligne, massicot, feuille qui claque ou glisse, tampon, retour de chariot de machine à écrire, coup feutré pour un atterrissage.
- **Silence** : arrêt net de tout sur un temps fort ; le claquement suivant devient un événement. L'exception peut être le seul élément qui « chante » (une note tenue qui suit sa position).
- **Voix** : froide, nette, phrases courtes en forme de règles.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Une seule famille de police et une seule couleur vive dans tout le film.
- [ ] Chaque élément est posé sur une ligne de grille (sauf l'exception, s'il y en a une).
- [ ] Aucun fondu, aucun rebond, aucun dépassement : deux courbes seulement.
- [ ] Chaque arrivée tombe sur un temps de la musique (écart de moins d'une image).
- [ ] Le contraste d'échelle est extrême : le plus grand élément fait au moins 15 fois le plus petit.
- [ ] Les modules ont de la masse : l'image ne ressemble pas à un graphique.
- [ ] Les sous-titres sont dans la composition, à un début de colonne, et restent lisibles au moins 1,8 s.
- [ ] Rien d'important au-dessus de y 160, en dessous de y 1560, ni à droite de x 945 : la 6e colonne de la grille ne porte aucun texte.
- [ ] Aucun texte sous 28 px ; interligne d'au moins 1,2 sur tout texte révélé par masque de lignes.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : fixe
- Couleurs max : 4
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu

- Film de démo d'origine, *Five Rules for a Poster* (44 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/swiss-motion.mp4
- Affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/swiss-motion.jpg
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, film et images sous CC BY 4.0. Aperçu non modifié ; notre mise en page verticale est une adaptation.

## 10. Origine

- Dépôt `lemomo-ai/lemo-opuscar`, commit `9eb7739`, fichiers `styles/swiss-motion/STYLE.md`, `DEMO.md`, `demo/ease.js`, `demo/film.js`, `demo/score.json`.
- Licence : MIT pour le code et les textes (© 2026 LemoLab), CC BY 4.0 pour le film et ses images.
- Adaptation Flot Web : traduction, section verticale, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
- Vérifié par un rendu réel le 11/11/2026 (HyperFrames 0.9.33) : ça marche avec corrections (interligne du texte découpé, son) ; film de 10 s, textes tous lisibles, contraste 28 sur 28 ; niveau sonore hors cible faute de musique.
