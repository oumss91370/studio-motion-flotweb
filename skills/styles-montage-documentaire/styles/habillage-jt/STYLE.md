# Habillage de journal télévisé

## 1. Identité
- **Nom** : Habillage de journal télévisé. Identifiant : `habillage-jt`.
- **Inspiration** : les sommaires des journaux du soir, les graphiques des chaînes financières, les cartes explicatives des chaînes d'info, les fiches techniques des rubriques « tech ». Grammaire seulement : jamais le logo, le décor, les polices, les couleurs, la musique ou le jingle d'une chaîne réelle, aucun nom cité.
- **Principe** : l'habillage complet d'une rédaction, fait entièrement en code : un jingle qui devient la pastille de chaîne, un sommaire qui ouvre et ferme le journal, un bandeau de titre qui ne quitte jamais le bas de l'image, et des graphiques plein cadre qui portent les faits (tableau à palettes pour les prix, courbe qui casse un seuil, carte explicative, documents qui s'envolent d'une ville, carte citation, fiche technique à barres de proportion, tampons). **Le style est le système d'habillage et ses règles de coupe**, pas un style de dessin.
- **Cinq règles** : un seul système de pièces, toujours le même ; l'ordre du journal (jingle → sommaire → sujets → retour au sommaire coché → signature) ; un fait par écran ; le bandeau porte le titre ; cadre propre (ni texte défilant, ni sous-titres incrustés en 16:9).
- **Pour quels sujets** : récapitulatif hebdomadaire d'une niche (« les 4 actus de la semaine »), bulletin de marché, flash d'annonces d'une marque, veille d'un secteur.
- **Ne marche pas pour** : un seul sujet raconté en longueur, un sujet émotionnel, un tutoriel. Ce n'est pas l'« info sous-titres » (ici la typo est petite et ordonnée, les graphiques mènent), ni un plateau virtuel (pas de décor 3D, pas de présentateur).

## 2. Palette, typographie, matières
| Rôle | Valeur | Usage |
|---|---|---|
| encre | `#121417` (`#1B1E23`, `#22262C`) | fonds, panneaux, cartes, terres sur les cartes |
| accent (citron) | `#F2CF1D` (clair `#F8DE4A`, foncé `#D8B30C`) | plaque, onglets, volet, barres, tampons, la courbe qui casse |
| or | `#D4B064` | seuils, lignes de date, lignes de source, badges |
| papier | `#F4F1E8` | bandeau, documents, courbe |
| alerte | `#FE6B3D` | réservé à « DERNIÈRE MINUTE » et « DIRECT » ; un récapitulatif n'en a pas |

Structure à garder en passant aux couleurs du client : **un accent + un second ton façon or + papier + encre + une couleur d'alerte réservée**. Texte encre sur l'accent ; sur papier, lignes secondaires en olive foncé `#6E5A1E` (l'or y est trop faible).
- **Polices libres** : titres et bandeau en sans ultra-gras ; chiffres, noms et plaque en Barlow Condensed 800 ; lignes de date, sources et axes en IBM Plex Mono 500, capitales espacées. Aucune police manuscrite.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Oswald à la place de Barlow Condensed ; IBM Plex Mono : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/barlow-condensed` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Pièces du système** : plaque de marque (parallélogramme, dégradé d'accent, barres encre et or à gauche) ; onglet d'accent ; bandeau papier ; cartes encre à bord supérieur d'accent ; lignes de date en mono ; tampons.
- **Couche image** : sans vraies images, des graphiques dessinés en code et au plus quelques **planches d'illustration**, chacune étiquetée « ILLUSTRATION » tant qu'elle est à l'écran ; elles posent une ambiance, elles ne remplacent jamais l'événement, le lieu ou les personnes. Étalonnage unique en deux tons (`#0E1013` → `#ECE7D8`), grain 7 % sur les planches seulement.

## 3. Composition 9:16
- **Contenu** (le graphique plein cadre) : x 60 à 945, y 180 à 1230.
- **Bandeau de titre** : onglet de catégorie (accent, 44 px de haut) à y 1270, bandeau papier de 885×150 à y 1314 (titre sur deux lignes, 46 à 54 px), bloc d'encre au bout. Rien d'important sous y 1560.
- **Ligne de source** : au-dessus de l'onglet, alignée à gauche, mono 28 px minimum, 36 caractères au plus.
- **Pastille de chaîne** : en haut à gauche sous y 170, la plaque du jingle réduite (≈ 0,33).
- **Étiquette de coin** (« ILLUSTRATION » ou « SCHÉMA ») : sous la pastille.
- **Sous-titres** : en vertical ils sont attendus par le public ; les placer entre le graphique et le bandeau ne laisse pas de place, donc **le bandeau fait office de sous-titre de titre** et la voix est sous-titrée dans une bande y 1470 à y 1550, une ligne, 38 px. À défaut, livrer le `.srt` à part.
- **Sommaire** : bloc date en haut (gros chiffres), puis trois ou quatre rangées de 885×150, numéro dans un bloc d'accent.
- Zones d'interface : haut 160, bas 360, droite 135.
- **16:9** : contenu x 96 à 1824, y 56 à 840 ; onglet à y 856, bandeau 1250×104 à y 904 ; pastille en haut à droite ; cadre sans sous-titres incrustés.

## 4. Ce qui bouge
- **Action principale** : le jingle qui devient la pastille (1,5 s). Deux traits d'accent (0,04 et 0,10 s) → la plaque claque avec dépassement, anneau d'impact et secousse → les lettres tombent une à une → un reflet → la plaque vole vers le coin et **devient la pastille** pendant qu'un volet vertical ouvre le premier plan. Un impact dans les 0,4 premières secondes.
- **Boucles de fond** : (1) le bandeau, présent du premier sujet au récapitulatif, dont les mots basculent verticalement (nouveaux mots qui montent, anciens qui sortent par le haut, 0,32 s ; l'onglet flashe en blanc quand la catégorie change) ; (2) une action d'habillage toutes les 0,5 à 1 s dans chaque plan (bascule, comptage, tampon, coche, lumière sur la carte, pas de la courbe).
- **Gestes** : tableau à palettes avant/après (ancienne et nouvelle valeur sur le même tableau) ; casser le seuil (la courbe avance d'une période par pas vers un seuil en tirets or ; la musique s'arrête un temps avant le dernier pas) ; documents qui s'envolent de la ville sur un arc (0,5 s, échelle 0,08 → 1) ; carte citation (grand guillemet d'accent d'abord, lignes poussées une à une à 0,18 s d'écart, puis nom, occasion et date) ; fiche technique (barres de proportion sur une seule échelle) ; tampon (tombe de 1,9× en 0,16 s, incliné de −6 à −10°, un par sujet au plus).
- **Autorisés** : #045 volet vertical (bande d'accent 84 px + encre + or, 0,3 s), #021 bascule verticale des mots du bandeau, #007 compteur, #004 tracé de courbe, #005 révélation par masque, #010 dépassement (plaque, tampon), #024 secousse (jingle, seuil cassé), #022 reflet, #046 coupe sèche + timbale dans un sujet.
- **Interdits** : #044 fondu, #139 cube et retournements 3D, #140 page qui tourne, #176 traversée de décor, texte défilant, bandeau qui sort en cours de journal.

## 5. Rythme et montage
- **Grille à 120 BPM**, temps 0 à la fin du jingle (1,5 s). Chaque coupe et chaque volet sur un temps ou un demi-temps.
- Durées : jingle 1,5 s ; sommaire 4 à 5 s ; plans de sujet 3 à 7 s ; un plan-séquence de carte (6 à 12 s) comme respiration du journal ; une comparaison reste jusqu'à ce que chaque élément ait été entièrement visible ≥ 2,5 s.
- **Dater chaque sujet** : la date est dans la rangée du sommaire, la ligne d'en-tête du graphique ou le document.
- **Ordre dans un sujet** : quoi (le nom ou le chiffre) → de quelle ampleur (courbe, barres, tableau de prix) → qui est touché ou qui l'a dit (barres, documents, citation) → le tampon de verdict.
- Volet entre les sujets et les parties ; coupe sèche à l'intérieur d'un sujet.
- **Version courte (8 à 12 s)** : le jingle (1,5 s), un seul titre de sujet avec sa plaque (5 s), la pastille de fin ; couper le sommaire et la carte.

## 6. Recette technique
- **Moteur** : HyperFrames, tout en HTML/SVG + GSAP : c'est le style du lot le plus simple à porter (aucun rush obligatoire).
- **Le calque d'habillage voyage avec son image** : sous un volet, chaque côté dessine ses propres mots de bandeau, onglet, ligne de source et étiquette de coin. Structure : une scène = `<section class="clip">` contenant son graphique **et** sa copie du bandeau ; le volet révèle la section suivante par `clip-path`.
```js
tl.fromTo(next, {clipPath: "inset(0 100% 0 0)"}, {clipPath: "inset(0 0% 0 0)", duration: 0.3, ease: "power2.inOut"}, T)
  .fromTo("#volet", {xPercent: -100}, {xPercent: 1200, duration: 0.3, ease: "power2.inOut"}, T);
// l'animation d'entrée de la scène suivante démarre sous le volet : sa première image révélée a déjà du contenu
tl.add(entreeScene(next), T - 0.1);
```
- **Palettes** : chaque tuile a une moitié haute et une moitié basse rognées séparément ; la moitié haute de l'ancienne valeur bascule (`rotationX` 0 → −90), puis la moitié basse de la nouvelle (90 → 0).
- **Carte** : une seule projection et une seule fonction monde → écran, pour que libellés et documents restent accrochés pendant la poussée et le panoramique. Pas de frontières contestées dans le cadre.
- **Barres** : une seule échelle pour toutes les barres d'une fiche, sinon la proportion est fausse.
- **Pièges** : un titre poussé depuis un masque montre son bord avant de bouger (le faire partir entièrement dessous) ; un compteur qui roule sur un cours de clôture affiche des valeurs qui n'ont jamais existé (poser la valeur par poussée de masque) ; ne pas graduer un axe que les données ne soutiennent pas ; nommer la référence d'un seuil sur l'axe (« −20 % depuis quel sommet ? ») ; or sur papier illisible.

## 7. Son
- **Voix** : un narrateur, une phrase par graphique, qui démarre 0,1 s après la coupe ; noms de marques et sigles écrits comme ils doivent sonner dans le texte de la voix, vraie orthographe à l'écran.
- **Thème d'info** à 120 BPM, mineur : violons en spiccato, basse en pizzicato sur le temps, nappe de cors, grosse caisse sur 1 et 3. Ambiances par rubrique (marchés : pulsation « battement de cœur » ; réglementation : pizzicato et cors seuls).
- **Coups signature** : tutti du jingle ; notes de glockenspiel quand les rangées du sommaire se posent ; timbale sur les coupes sèches ; **un temps de silence avant la plus grosse cassure**, puis le coup le plus lourd du film.
- **Bruitages** (budget du skill `son`) : souffle des volets, cliquetis des palettes, coup + claquement du tampon, tic par pays allumé. Un tampon ne doit pas masquer un mot clé de la voix.
- Musique ≈ 7 dB sous la voix ; −14 LUFS, crête −1,2 dBTP.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Toutes les pièces viennent du même système (plaque, onglet, bandeau, carte encre, ligne mono, tampon).
- [ ] Sous chaque volet, l'ancien titre reste du côté de l'ancienne image (contrôle image par image sur 0,3 s).
- [ ] Un fait par écran ; chaque sujet est daté.
- [ ] Les mots ne sont pas plus forts que la source (« demande d'information » n'est pas « enquête ») ; ce que seul un article affirme est attribué (« selon … »).
- [ ] Chaque chiffre vient de la page source ; `FAITS.md` à jour.
- [ ] Toute planche générée ou d'illustration porte « ILLUSTRATION » pendant toute sa durée.
- [ ] La couleur d'alerte n'apparaît pas hors « dernière minute ».
- [ ] Aucune marque de chaîne réelle ; nom et plaque viennent de la fiche « ma chaîne ». Zones d'interface respectées.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 7
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Affiche d'origine : https://lemomo-ai.github.io/lemo-opuscar/posters/news-package.jpg · galerie : https://lemomo-ai.github.io/lemo-opuscar/#edit-documentary
- Crédit : « The Week in AI », LemoLab, CC BY 4.0 **pour l'image seulement** : la piste de voix de ce film est exclue de la licence, et le film cite des marques réelles. Ne pas rediffuser le film avec son ; renvoyer vers la galerie officielle. Démo en 16:9.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/news-package/STYLE.md`, `style.json`, `demo/main.js`, `demo/tools/prep.py`.
- Licence : MIT (© 2026 LemoLab) pour le texte et le code ; image du film de démo CC BY 4.0, voix exclue.
- Adaptations Flot Web : français, une seule langue par libellé, mise en page 9:16 avec sous-titres, HyperFrames.
