# Montage constructiviste

## 1. Identité
- **Nom** : Montage constructiviste. Identifiant : `montage-constructiviste`.
- **Inspiration** : le cinéma de montage des années 1920 (écrans divisés, comptage, rythme de machine, deux images qui se heurtent pour produire une idée) et les affiches et photomontages constructivistes (rouge, noir, papier, diagonales raides, typo qui fait structure). Grammaire seulement : aucun plan, slogan ou lettrage repris, aucun nom cité dans la vidéo.
- **Principe** : de vraies archives filmées, photos et documents, imprimés comme **une seule affiche encre et papier avec un seul rouge**, et coupés sur un temps de machine. Des bandes diagonales portent le texte ; des fenêtres taillées le long de l'axe tiennent le film ; des personnes découpées aux ciseaux s'empilent en structures ; les chiffres comptent ; les documents sont marqués en rouge. Le collectif avant l'individu : foules, mains, machines ; un visage seul n'est jamais le héros.
- **Pour quels sujets** : histoire d'un chantier ou d'une industrie, anniversaire d'entreprise, grand événement de masse, inauguration, effort collectif : « beaucoup de gens, un rythme de machine », avec archives et documents à l'appui.
- **Ne marche pas pour** : portrait intime, produit numérique, sujet sans archives. Ce n'est pas un film de données, pas du graphisme suisse (rien de symétrique, pas de vide blanc), pas un diaporama de musée (l'archive n'est jamais montrée « telle quelle » dans un cadre neutre).

## 2. Palette, typographie, matières
| Rôle | Valeur | Usage |
|---|---|---|
| Rouge | `#D52B1E` | bandes, coins, blocs, le chiffre clé, barres de marqueur, cercles, le seul gagnant d'une comparaison |
| Encre | `#141210` | typo, poutres, bordures de fenêtres, fonds sombres |
| Papier | `#EDE4D0` | fond, typo en réserve, liseré des découpes |

Jamais de rouge sur rouge (un bloc rouge sur fond rouge passe en encre). Alterner les fonds pour que les coupes claquent : papier → encre → papier.
- **Quatre éléments seulement** : bandes, fenêtres (rectangles ou parallélogrammes), découpes (personnes avec liseré papier de 7 px), blocs de texte. Plus une fibre de papier fixe multipliée sur tout (opacité 0,5).
- **Tirage unique** pour film, photos et documents : luminance → étirement par percentiles (**une paire par plan**, sinon ça pompe) → courbe en S → projection encre → papier. Le film d'archive garde un scintillement de ±2,5 % par image dans sa fenêtre ; photos et documents non.
- **Polices libres** : titres en sans ultra-gras ; chiffres et lignes en capitales en Oswald 600 à 700 ; étiquettes de source en Space Mono Bold sur onglet encre ou rouge.
- **Police de repli** : aucune à prévoir, Oswald et Space Mono sont fournies par HyperFrames et se chargent par leur nom. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : rien à télécharger ; pour embarquer quand même le fichier, `@fontsource/oswald`, `@fontsource/space-mono` (vérifié par `npm view` le 11/11/2026).

## 3. Composition 9:16
- **Axe à −18°** (réglable de −15° à −30°) : en vertical, la diagonale monte du bas gauche vers le haut droit ; les bandes font 180 à 260 px d'épaisseur. Le texte se place depuis la ligne centrale de la bande (point + décalage sur la normale), jamais à l'œil.
- **Titre vertical** : en 9:16, c'est le format roi : lettres empilées de haut en bas (150 à 170 px par caractère) à côté d'une haute fenêtre.
- **Chiffres** : 230 à 440 px, plus gros que les mots qui les expliquent ; ils peuvent couper le cadre à gauche mais leur partie lisible reste à gauche de x 945.
- **Fenêtres d'archive** : largeur ≤ 1000 px ; un transfert de film ancien ne remplit pas tout l'écran, on le fenêtre (≤ 2,5× ses pixels).
- **Étiquettes** : chaque fenêtre d'archive porte son étiquette (`FILM · titre · lieu année`, `PHOTO · auteur année`), chaque fait son étiquette de source, 28 px minimum.
- **Sous-titres** : en bas à gauche, entre y 1380 et y 1540, barre encre à 90 % avec un tiret rouge ; le texte clé reste au-dessus de y 1340 pendant la narration.
- Zones d'interface : haut 160, bas 360, droite 135.
- **16:9** : sous-titres dans une bande de 960 à 1056 px de large en bas à gauche ; texte clé au-dessus de y 930.

## 4. Ce qui bouge
- **Action principale** : le claquement (« slam »). L'élément arrive de l'extérieur le long de l'axe en 0,08 à 0,2 s, décélère, s'arrête net, et le cadre tremble (3 à 18 px, amortissement `exp(−14·Δt)`).
- **Boucles de fond** : (1) le film qui tourne et scintille dans ses fenêtres ; (2) un compteur piloté par les coupes.
- **Gestes** : le document est marqué, pas cité (barre rouge sur la phrase exacte, puis le chiffre devient un bloc rouge) ; le document devient le graphique (ses dessins se décollent de la page et se posent à l'échelle sur une ligne de sol) ; A + B → idée (deux types d'images alternent de plus en plus vite jusqu'à ce qu'un carton dise ce que le choc voulait dire) ; la tour de photomontage (des étages de bandes de film claquent de côtés alternés, une poutre sous chacun, un ouvrier découpé sur un étage sur deux, la caméra grimpe).
- **Autorisés** : #024 secousse d'impact, #045 volet (bande rouge de 260 px à 72° en 0,25 s), #188/#017 iris (un cercle rouge tracé sur une carte devient une ouverture), #040 arrêt sur image, #041 saut dans le même plan (recadrage 1,2×), #144 écran partagé en bandes, #120 double exposition, #007 compteur, #192 montage, #046 coupe sèche, #080 marqueur.
- **Interdits** : #044 fondu, texte flottant ou centré, #010 rebond élastique, #016 parallaxe douce, lignes fines décoratives, or, deux documents papier de suite.

## 5. Rythme et montage
- **Le temps est le monteur** : un seul tempo pour l'image et la musique (120 BPM : temps 0,5 s, mesure 2 s ; réglable de 100 à 140). Chaque coupe, claquement, volet et comptage tombe sur un temps, un demi-temps ou une double-croche.
- Plans de 0,5 à 2 s, une idée par plan. Une partie accélère en divisant par deux : 0,5 → 0,25 → 0,125 s (jamais moins de 3 images). **Sécurité** : au-delà de 3 coupes par seconde (plans de moins de 10 images), n'enchaîner que des images de luminosité voisine (même papier, même encre), pendant 1 s au plus, et jamais une alternance clair / sombre ou rouge / blanc en plein cadre : c'est un clignotement, risque pour les personnes photosensibles.
- **Règle de coupe** : deux plans voisins s'opposent sur au moins un point : direction (claquement gauche / droite), valeur (fond papier / encre) ou géométrie (bande diagonale / fenêtre droite).
- Rien de figé plus d'1 s, sauf la tenue de comparaison, un temps de silence et le carton de fin.
- **Deux silences** : un où l'orchestre s'arrête et où seul un enregistrement d'origine reste ; un vrai demi-mesure de rien (cadre encre, un point rouge) avant le coup le plus lourd.
- Pas de texte dans les coupes à la double-croche : le résultat va dans un bloc tenu après.

## 6. Recette technique
- **Moteur** : HyperFrames. Bandes et blocs en `div` tournés (`rotate(-18deg)`), fenêtres en `clip-path: polygon(...)` autour d'une `<video class="clip">` ou d'une séquence d'images, découpes en PNG transparents, fibre de papier en image fixe au-dessus (`mix-blend-mode: multiply` sur la scène, pas sur une couche d'étalonnage plein écran).
```js
const slam = (el, t, dx) => tl.fromTo(el, {x: dx, opacity: 1}, {x: 0, duration: 0.14, ease: "power3.out"}, t)
  .fromTo("#scene", {y: 12}, {y: 0, duration: 0.3, ease: "elastic.out(1, 0.3)"}, t + 0.14);
// volet rouge : la nouvelle scène est révélée derrière la bande
tl.fromTo("#bande", {xPercent: -130}, {xPercent: 130, duration: 0.25, ease: "none"}, T);
```
- **Tirage encre/papier** : à préparer hors page (script ou ffmpeg) puis à livrer en séquences d'images à 30 i/s, la cadence du film (la source était à 24 i/s), ou approché en CSS par `grayscale(1) contrast(1.3)` + calque de teinte en `multiply`/`screen` à l'intérieur de la fenêtre.
- **Découpes** : détourage de personne (voir la fiche `detourage-sujet`), seuil, plus grand composant, liseré papier de 7 px dilaté hors du masque : le liseré est le look du médium et cache les erreurs de bord. Les photos de groupe se détourent mal : les utiliser entières en fenêtre.
- **Graphique tiré du document** : extraire les dessins de la page en les séparant de leur papier (`alpha = (205 − luminance) / 90`), les mettre à l'échelle pour que hauteur = valeur × pixels par unité, teinter le gagnant en rouge.
- **Pièges** : archive agrandie en plein cadre = bouillie (fenêtrer) ; un compteur se lit comme un fait (seules sa valeur finale et ses étapes datées sont des faits ; arrêter le compteur sur la valeur du libellé tant que le libellé est à l'écran) ; chaque compteur porte son unité ; un texte encre qui dépasse sur une fenêtre sombre disparaît (onglet papier) ; un coup à l'échantillon 0 sature à l'encodage (fondu de 25 ms).

## 7. Son
- **Musique** : ostinato de machine original en croches, mineur, violoncelles en spiccato et basson, tuba/trombone sur le temps, caisse claire en doubles croches, xylophone pour les comptages (une note qui monte par case ou par étage), roulement de timbales aux changements de partie, grosse caisse + gong sur le coup le plus lourd. Pas de nappe piano-cordes.
- **Le son d'origine alterne avec la musique** : dans une partie, l'orchestre s'arrête et un vrai enregistrement (machine, foule) porte seul le montage, amené un temps en avance (J-cut).
- **Bruitages** (budget du skill `son`) : claquement = coup sourd + choc d'acier ; tampon ; souffle du volet ; frottement du marqueur ; papier.
- Narration éventuelle : phrases déclaratives courtes, jamais plus d'une par format ; chiffres en lettres pour la voix. Musique ≈ 10 dB sous la voix ; crêtes limitées à −1,8 dBFS ; −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] Trois couleurs exactement (rouge, encre, papier) ; aucun rouge sur rouge.
- [ ] Tout le matériel est réel et tiré comme une seule affiche ; une paire de percentiles par plan.
- [ ] Chaque coupe et chaque claquement sur la grille (écart < 1 image).
- [ ] Deux plans voisins s'opposent en direction, valeur ou géométrie ; jamais deux documents de suite.
- [ ] Une seule phrase marquée par plan de document.
- [ ] Aucun visage d'anonyme en héros (pas de gros plan ni de ralenti).
- [ ] Une image qui ne montre pas le sujet lui-même (autre ville, autre année) le dit dans son étiquette.
- [ ] Texte sur bande entièrement dans le cadre et hors zones d'interface ; deux silences présents.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 3
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Film de démo d'origine : https://lemomo-ai.github.io/lemo-opuscar/films/kino-montage.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/kino-montage.jpg
- Crédit : « 410 Days », LemoLab, CC BY 4.0. Archives et photos de tiers : **lien seulement**. Démo en 16:9.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/kino-montage/STYLE.md`, `style.json`, `demo/index.html` (`slam()`, `slant()`, `flash()`, `shake()`, `clipImg()`), `demo/tools/prep.py`.
- Licence : MIT (© 2026 LemoLab) ; film de démo CC BY 4.0.
- Adaptations Flot Web : français, titre vertical mis en avant pour le 9:16, HyperFrames. Sources et droits : `references/materiel-et-droits.md`.
