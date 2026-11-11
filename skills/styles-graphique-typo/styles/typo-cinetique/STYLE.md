# Typo cinétique

## 1. Identité

- **Nom** : Typo cinétique (le mot est l'acteur).
- **Inspiration** : les génériques de film à lettres animées de la fin des années 1950, puis les vidéos de paroles et de citations animées des années 2000 et 2010, devenues la grammaire courante des ouvertures, listes et chiffres-chocs.
- **La règle en une phrase** : chaque mot clé tombe sur un accent ; le mot principal est assez gros pour être lu d'un coup d'œil ; les autres mots montent de derrière un masque pour accompagner l'oreille ; **il n'y a jamais qu'un seul point d'attention** ; la caméra et le fond bougent toujours, **le mot, une fois posé, ne bouge plus**.
- **Marche pour** : ouverture et cartes de chapitre (« 3 raisons », « 5 étapes »), citation ou phrase choc, chiffre (un chiffre = un plan), phrase de voix off qui contient un mot accentué (« ce n'est pas écrire du code, c'est **dire ce qu'on veut** »).
- **Ne marche pas pour** : raconter une histoire ou une émotion (pas de visage), accompagner une longue explication (le spectateur lit au lieu d'écouter), liste de plus de 5 éléments. Au-delà de 30 à 60 s de texte seul, changer de style ou intercaler une image ou une « pièce à conviction » (capture, carte, bulle de discussion) toutes les deux pages.
- Fiche commune aux catégories « Graphique et typo » et « Explicatif et infographie ».

## 2. Palette, typographie, matières

**Un fond plein écran par chapitre** : changer de chapitre, c'est changer de fond (la couleur est le numéro du chapitre). Quatre fonds + encre + blanc, et **un seul accent à la fois**.

| Plan | Fond | Mot principal | Accent |
|---|---|---|---|
| Titre | jaune `#FFD23F` | encre `#111111` | disque corail `#FF5A36` avec un chiffre blanc |
| Chapitre 1 | corail `#FF5A36` | blanc | surligneur jaune `#FFD23F` |
| Chapitre 2 | bleu nuit `#14213D` | jaune | surligneur jaune, bulle bleue `#3A86FF` |
| Chapitre 3 | crème `#F4EFE6` | encre | soulignement corail, coche verte `#2BB673` |

- **Police** : une grotesque très grasse en quatre graisses (Noto Sans ou Inter : 900, 800, 700, 500). Police à chasse fixe pour un bloc de code (JetBrains Mono).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place de Noto Sans ; Inter, JetBrains Mono : déjà fournies. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/noto-sans` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Formes** : la lettre est la plus grande forme. En appui, seulement des rectangles arrondis (carte rayon 26, bulle rayon 30, touche rayon 22), des disques (fond de chiffre) et des blocs en biais (surligneur, pente de 0,18).
- **Fond** : une trame de points espacés de 64 px, opacité de 6 à 10 %.
- Pas de lettres à contour, pas de lettres ombrées. La seule ombre : un décalage de 8 à 18 % sous les cartes.

## 3. Composition 9:16

- **Un écran, un mot principal.** En vertical : le mot principal ferré à gauche entre y 520 et y 900 ; la phrase d'appui juste en dessous ; la pièce à conviction (carte, bulle, liste) dans la moitié basse, entre y 1000 et y 1500 ; l'étiquette de chapitre (« ÉTAPE 01 ») et la **piste de progression** en haut, entre y 180 et y 260. Marges de 80 px au moins ; rien à droite de x 945.
- **Échelle des tailles** (rapport 3,4 : 1 : 0,4) :

| Rôle | Taille en 1080 de large | Limite |
|---|---|---|
| Mot principal | 240 à 300 px | 1 ou 2 mots, 8 lettres au plus ; lu en 0,3 s |
| Phrase d'appui | 72 à 84 px | 6 à 7 mots |
| Étiquette | 34 à 40 px, interlettrage 6 px | |
| Chiffre de chapitre géant en fond | 800 à 900 px, opacité 5 à 13 % | |

- Si ça ne rentre pas, **on coupe en deux pages**, on ne réduit pas la taille.
- **Jamais plus de 3 pages de suite avec la même mise en page** : intercaler une page « chiffre qui tombe », une pièce à conviction, ou une transition qui fonce dans un bloc de couleur.

## 4. Ce qui bouge

- **Action principale** : le mot principal **tombe** sur le temps fort (il passe de 1,7 fois à sa taille, opacité de 0 à 1 dans les 0,06 premières secondes, ressort avec un dépassement d'environ 8 %, immobile en 0,35 s).
- **Boucles de fond** : (1) une dérive de caméra très légère (5 px, périodes de 7 s et 2,7 s, rotation de ±0,5°) et un **petit coup de zoom sur chaque temps** (1,2 %, amorti en 0,12 s) ; (2) la trame de points qui glisse en biais (36 px par seconde).

| Élément | Entrée | Courbe et durée |
|---|---|---|
| Mot principal | il tombe (1,7 → 1) | ressort, 0,35 s |
| Phrase d'appui, étiquette | **monte de derrière un masque** (de 1,2 hauteur de lettre) | sortie exponentielle, 0,30 à 0,35 s |
| Chiffre, icône, bulle, touche | surgit (0 → 1) | dépassement de 17 à 20 %, 0,30 à 0,42 s |
| Carte | glisse (de 700 px ou du bas), tournée de 3,4° puis redressée | sortie exponentielle, 0,40 s |
| Texte tapé | caractère par caractère | 26 caractères par seconde, curseur à 2 clignotements par seconde |
| Surligneur, soulignement | se peint de gauche à droite | 0,30 s, une à trois croches **après** le mot |
| Mot clé | grossit à 1,35 fois et reste, sur le temps d'accent | ressort |
| Coche | le trait se dessine, la case fait 1 → 1,25 → 1 | 0,22 s |

- **Autorisés** : typo cinétique `#008`, révélation par masque `#005`, apparition éclair `#001`, dépassement `#010`, machine à écrire `#006`, compteur `#007`, surligneur `#080`, soulignement `#086`, décalage en cascade `#002`, zoom à travers `#020`, poussée `#137`, transition par masque `#017`, secousse d'impact `#024`.
- **Interdits** : texte en vague `#130`, flottement `#096`, tremblement `#124` ou « respiration » d'un mot posé, fondu enchaîné `#044`, lettres à contour ou ombrées, plusieurs entrées en même temps.
- **Sorties** : plus rapides que les entrées (0,18 s, en accélérant), décalées de 0,03 s, en rétrécissant à 0,6 et en descendant de 60 px.
- Décalage entre les mots d'une ligne : une croche (0,25 s à 120 battements par minute).

## 5. Rythme et montage

- **120 battements par minute, une mesure par plan** (2 s). Dans chaque plan, toujours les mêmes places : temps 1 le mot principal ; temps 1,5 la pièce à conviction ; temps 2 la phrase d'appui ; temps 3 l'action de la pièce ; temps 3,5 le mot clé qui grossit et le surligneur ; temps 4 respiration ou sortie. Dès le deuxième plan, le spectateur « sait où tombera le prochain coup ».
- Un événement visuel par croche dans une ouverture de 8 s ; un par temps dans un film plus long.
- **Temps de lecture** : mot principal d'un ou deux mots, 0,5 s au moins ; phrase d'appui de 6 à 7 mots, 1 à 1,5 s au moins.
- **Transitions** : (1) **zoom à travers** : la caméra fonce dans une forme du plan (le disque du chiffre) dont la couleur est le fond du plan suivant ; (2) **bandes** : trois bandes en biais se relaient de gauche à droite, la dernière est le nouveau fond (0,5 s) ; (3) **poussée** : l'ancien et le nouveau glissent ensemble (0,35 s) ; (4) volet par masque ; (5) une lettre grossit jusqu'à devenir le fond.
- **Le calage qui compte** : l'accent n'est pas le début de la transition mais l'image où **le nouveau plan se découvre**. Début du plan = barre de mesure − (point de découverte × durée de la transition). Points de découverte : 0,55 pour le zoom à travers, 0,6 pour les bandes, 0,58 pour la poussée.
- Avec une voix : le mot principal est le mot accentué de la phrase ; l'image peut avoir **une image d'avance au plus**, jamais de retard.
- Fin : un dernier coup sur le temps 16 (la caméra recule de 6 %), puis 0,5 s d'immobilité.

## 6. Recette technique

- **Moteur** : HyperFrames, éléments HTML animés par GSAP : c'est le style le plus simple à construire et à corriger (chaque mot est une balise, le texte est une variable).
- **Structure** : un fichier de scène par plan ; une fonction `temps(n)` ; la piste de progression dans un calque fixe au-dessus de toutes les scènes (elle ne doit pas glisser avec les pages).

```js
const BPM = 120, temps = n => (n - 1) * 60 / BPM;            // tous les points d'arrivée s'écrivent en temps
// le mot principal tombe sur le temps 1 du plan
tl.fromTo("#mot", { scale: 1.7, opacity: 0 }, { scale: 1, duration: 0.35, ease: "back.out(1.6)" }, temps(1))
  .to("#mot", { opacity: 1, duration: 0.06 }, temps(1));
// la phrase d'appui monte de derrière son masque (parent en overflow:hidden) sur le temps 2
tl.fromTo("#appui span", { yPercent: 120 }, { yPercent: 0, duration: 0.32, ease: "expo.out" }, temps(2));
// petit coup de zoom de toute la scène sur chaque temps
for (let n = 1; n <= 4; n++) tl.fromTo("#scene", { scale: 1.012 }, { scale: 1, duration: 0.12, ease: "power3.out" }, temps(n));
```

- **Pièges** : faire partir la transition sur la barre de mesure (elle doit s'y **découvrir**) ; une piste de progression dessinée dans chaque scène saute au changement de page ; un bloc de code dans une police proportionnelle ; des éléments « terminés » qui deviennent gris (les passer en vert, ils restent positifs).

## 7. Son

- **Musique** : rythmique simple et nette : grosse caisse sur chaque temps, clap sur les temps 2 et 4, charleston à contretemps, basse en croches.
- **Un son par point d'arrivée** : mot principal = coup grave ; petit élément = « pop » ; texte tapé = clics ; coche = « pop » plus aigu ; 0,3 s avant une transition = un souffle montant. Ici le budget habituel d'environ 5 bruitages pour 10 s peut être dépassé, à condition que les petits « pops » restent très en retrait dans le mixage.
- **Silence** : une croche de vide avant le dernier coup.
- **Voix** : facultative ; si elle existe, c'est elle qui fixe la grille, et chaque mot accentué a son mot à l'écran.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Les trois fautes les plus courantes : tous les mots de la même taille et qui bougent ensemble ; des mots qui flottent pendant qu'on les lit ; des animations hors du temps, ou calées sur le début de la transition.

- [ ] Rapport d'au moins 3 pour 1 entre le mot principal et la phrase d'appui.
- [ ] Un seul élément en train d'entrer à chaque instant.
- [ ] Un mot posé ne bouge plus (seuls la caméra, le fond et les nouveaux arrivants bougent).
- [ ] Chaque arrivée tombe sur un temps ou une croche, ou sur le mot dit par la voix.
- [ ] Le nouveau plan se découvre sur la barre de mesure.
- [ ] Jamais plus de 3 pages de suite avec la même mise en page.
- [ ] Mot principal de 8 lettres au plus ; phrase d'appui visible au moins 1 s.
- [ ] Un seul accent de couleur par plan ; aucun bord noir visible pendant les transitions.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 7
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 34

## 9. Aperçu

- Planche de la démo d'origine (une image par plan, 16:9) : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/y5_kinetic_type_总览.jpg
- Crédit : 花叔 Huashu (alchaincyf), https://github.com/alchaincyf/huashu-art-motion. La démo (8,5 s, 120 battements par minute) n'est pas publiée en vidéo séparée ; elle se reconstruit depuis `scripts/engine/demos/y5_kinetic_type/`.

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichiers `references/动画语法/y5_kinetic_type.md`, `scripts/engine/demos/y5_kinetic_type/`, `scripts/engine/lib/typo.js`, `motion.js`, `transitions`.
- Licence : MIT (© 2026 alchaincyf, 花叔).
- Adaptation Flot Web : traduction du chinois, tailles et limites de mots recalculées pour le français et le format vertical, portage vers HyperFrames et GSAP, numéros de mouvements, règles de son du plugin.
