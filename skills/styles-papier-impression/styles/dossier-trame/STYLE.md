# Dossier tramé rétro

## 1. Identité

- **Nom** : Dossier tramé rétro (« Halftone Dossier »).
- **Inspiration** : l'impression à points des bandes dessinées des années 60 (la densité de points fait l'ombre), les fanzines en surimpression (couches multipliées, repérage décalé), les fiches d'identité judiciaire et les chemises de dossier (le dispositif), les bandeaux de mots-clés des émissions de variétés. Grammaire seulement, rien n'est copié.
- **Ce que c'est** : **tout le film est du papier**. Une feuille crème, des **trames de points surimprimées** en quelques encres plates, d'énormes titres gras aux ombres décalées, des **tampons qui claquent**, des personnages à gros contour. Le film est **un dossier qu'on lit, une pièce à la fois**. L'appareil bureaucratique (numéros de dossier, pièces numérotées, toise, plaque de nom, tampons) est le cadre ; le sujet peut être grave ou dérisoire, et le décalage fait l'humour.
- **Fort mais lisible** : une idée par carte de 2 à 4 s, un gros titre, un gag visuel ou une pièce à conviction, une ligne de légende.
- **Marche pour** : « le dossier de… », un produit ou une habitude « mis en accusation », 3 à 5 preuves, un classement, un vrai-faux, un bilan, un sujet d'actualité léger, une vidéo **sans voix**.
- **Ne marche pas pour** : émotion sincère, luxe, tutoriel pas à pas, sujet réellement judiciaire ou une personne réelle « accusée » (à éviter).
- **À ne pas confondre** : pas la `risographie` (ici pas de grain riso plein cadre) ; pas le `pop-trame` (pas de cases de BD ni d'héroïne) ; pas de la typo suisse. Points, papier et tampons doivent être visibles **dans chaque image**.

## 2. Palette, typographie, matières

- **Un fond papier, une encre sombre, et quatre ou cinq encres plates.** L'encre sombre porte tous les contours, le texte courant et la barre de légende ; c'est aussi la couleur de sortie.
- Une encre est **l'ombre de surimpression** (décalages, ombres des légendes) ; une est **le surligneur** des mots-clés et des chiffres ; **un rouge chaud est réservé aux tampons et aux alertes**.

| Jeu d'exemple | Papier | Sombre | Ombre | Surligneur | Autre | Tampon |
|---|---|---|---|---|---|---|
| Crème / marine | `#f3ead6` | marine `#1c2452` | cobalt `#2f55c8` | jaune `#f6cf3a` | rose vif `#ff4f9a` | rouge `#d8322a` |
| Kraft / sépia | `#e9d9b4` | sépia `#2b1d14` | sarcelle `#2a8a86` | moutarde `#d9a441` | — | vermillon `#d9432b` |
| Blanc cassé / forêt | `#f4f0e4` | vert forêt `#1f4a3a` | ciel `#7fb6d9` | ocre `#d8a13a` | tomate `#e2553a` | tomate |

- Encres plates seulement. **Le ton vient de la taille des points et de la surimpression.** Scènes de nuit ou « secrètes » : fond en encre sombre avec une trame plus claire de la même famille, toujours multipliée par le papier.
- **Typographie** (OFL) : titres en serif **très grasse** (une slab noire, par exemple **Alfa Slab One** ou **Rozha One**), 130 à 260 px en vertical, alignés à gauche, avec **ombre de repérage** (+8 / +8 px dans l'encre d'ombre, multipliée) ; noms et gros chiffres en display ronde et grasse (**Bagel Fat One**) ; interjections en écriture enjouée à gros contour ; données en chasse fixe grasse (**JetBrains Mono 800**) ; légendes et tampons en sans-serif noire.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Archivo Black à la place d'Alfa Slab One et de Rozha One ; JetBrains Mono : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/alfa-slab-one`, `@fontsource/rozha-one` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** :
  - *Papier* (une couche multipliée sur tout, construite une fois) : marbrure, bruit légèrement chaud, vignettage, un faible pli central.
  - *Poussière* : quelques centaines de points couleur papier et moins de points d'encre, retirés toutes les 2 images.
  - *Trame* : grille tournée de cercles, pas de 20 à 26 px (**jamais sous 14 px** : moiré après encodage), rayon = densité × pas × 0,6 à 0,72 (vers 0,7 les points fusionnent en aplat). Champs de densité : radial (halo), bord (points serrés contre le cadre), rampe linéaire.
  - *Chiffres géants tramés* : aplat + trame plus sombre découpée dans le glyphe ; ils peuvent sortir du cadre.
  - *Tampons* : double rectangle arrondi et texte gras, passés dans un filtre de grain et de déplacement (bords rugueux, encre tachée), opacité ≈ 93 %, penchés de ±10°.
  - *Personnages* : formes trapues à gros contour (≈ 7 px), aplats, yeux brillants ; un seul rig de tête pour toutes les poses.

## 3. Composition 9:16

- Compose **comme une page imprimée**, verticale : pastilles de dossier en haut (numéro et chapitre à gauche, statut et date au centre-gauche ; rien dans le coin droit au-delà de x = 945), **titre en haut à gauche** (y 220 à 620), **sujet au centre** (y 620 à 1320), **barre de légende en bas** (y ≈ 1400 à 1500).
- **La barre de légende est le sous-titre** : pastille arrondie en encre sombre, ombre décalée, texte couleur papier 46 à 52 px, **le mot-clé dans l'encre surligneur**. Elle arrive après le titre et tient ≥ max(1,8 s ; réplique + 0,6 s). Avec une voix, elle porte la phrase dite.
- Chiffre géant de pièce à conviction (« 1 », « 2 »…) derrière le sujet, 700 à 1100 px de haut, tramé.
- Photo d'identité : sujet de face, toise graduée derrière, plaque de nom, éclair.
- En français, les titres sont plus longs que dans la démo d'origine : 2 ou 3 lignes de 1 à 3 mots, tampons d'un ou deux mots (VALIDÉ, CLASSÉ, COUPABLE, EXPIRÉ).
- 16:9 : titre à gauche, sujet à droite.

## 4. Ce qui bouge

- **Action principale** : une carte arrive, le titre tombe lettre par lettre, la pièce à conviction entre, **le tampon claque**.
- **Boucle de fond 1** : le **frémissement du trait** des personnages et accessoires dessinés (≈ 10 fois par seconde, déplacement ≈ 5 px ; petite surface seulement : des traits, jamais un aplat ni un fond) : le dessin respire pendant que les positions restent fluides. **Jamais** sur le texte, la trame, les pastilles ou les légendes.
- **Boucle de fond 2** : vie au repos : respiration, queue ou cheveux, clignements, voyant d'enregistrement ou deux-points d'horloge qui clignotent, léger battement de la page sur le temps (≈ 0,6 %).
- **Gestes natifs** : le cadre d'accusation ; les pièces numérotées ; **le tampon** ; la photo d'identité ; le tableau de preuves (pièces punaisées reliées par une ficelle) ; **la densité de points = l'émotion** (halo qui gonfle, points qui se serrent au bord pour la tension) ; le caviardage (des barres noires qui se lèvent une à une).
- **Chiffres** : tout **entre avec un dépassement** (0,3 à 0,45 s), en montant du bas ou depuis l'échelle zéro ; rien n'apparaît en fondu. Titre : chaque lettre tombe de 30 à 100 px et s'écrase à l'arrivée, décalage 0,05 à 0,08 s. **Tampon** : ≈ 0,09 s de 2,6 × à 1 ×, petit rebond amorti ; secousse, éclair et son **sur la même image**.
- **Autorisés** : `#001` apparition en rebond, `#010` dépassement, `#002` décalage en cascade, `#011` écrasement à l'atterrissage (volume conservé), `#024` secousse d'impact (5 à 26 px, décroissance rapide), `#136` trait qui frémit, `#027` avancée lente (1 → 1,05 à 1,08), `#018` transition par formes (volet de points), `#046` coupe franche sur un gros coup, `#080` surlignage.
- **Interdits** : `#044` fondu, dégradés, transparences progressives, éclair blanc à 100 % (il se lit comme une image manquante : plafonne à ≈ 0,5), frémissement sur le texte, plus de cinq encres.

## 5. Rythme et montage

- 30 i/s ; cartes de **2 à 4 s**. La durée grandit avec le nombre de pièces : chacune a besoin de son temps de lecture. 4 pièces ≈ 25 à 30 s.
- **Volet de points** : une grille de cercles grandit jusqu'à tout couvrir puis rétrécit (≈ 0,44 s) avec un retard diagonal ; la scène change pendant qu'elle est couverte. La coupe franche est l'outil de contraste, sur un gros coup.
- **Silence avant le tampon** : vide la musique juste avant le verdict pour qu'il tombe seul.
- Le film marche sans voix : les cartes portent tout.
- **Version courte (8 à 12 s)** : une seule carte : le titre lettre par lettre, une pièce à conviction, le tampon ; couper les autres pièces.

## 6. Recette technique

- **Moteur** : HyperFrames **en éléments HTML et SVG animés par GSAP** (pas besoin de canvas plein cadre) : c'est le style le plus simple à monter. Papier et poussière sur deux canvas par-dessus.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `page.html` (scènes à fenêtres de temps), `trame.js` (cercles en un seul tracé, champs de densité), `texte.js` (lettres séparées + chute), `tampon.js`, `legende.js`, `mascotte.js` (rig + visages), `volets.js`, `papier.js`.
- **Techniques clés** :
  ```js
  // trame : rayon = densité(x, y) * pas * k ; la 2e couche est multipliée (surimpression)
  for (const [x, y] of grilleTournee(pas, angle)) chemin += cercle(x, y, dens(x, y) * pas * 0.66);
  // tampon : claque en 0,09 s, puis secousse + éclair + son sur la même image
  tl.fromTo(tampon, { scale: 2.6, opacity: 0 }, { scale: 1, opacity: 0.93, duration: 0.09, ease: "power2.in" }, tT)
    .add(() => secousse(18), tT + 0.09);
  // atterrissage : volume conservé
  el.style.transform = `scale(${1 / sq}, ${sq})`;
  ```
  - Frémissement : un filtre de turbulence + déplacement dont la graine change 10 fois par seconde, **uniquement** sur le groupe des personnages.
- **Pièges** :
  - **Polices pas encore chargées au moment de la mise en page** : les positions par lettre sont calculées avec la police de secours, les glyphes se chevauchent. Précharge toutes les familles avant de mesurer.
  - Les identifiants de découpe sont globaux : chaque chiffre découpé a le sien.
  - Scènes à fenêtres de temps : un élément invisible avant son repère a besoin d'une opacité 0 explicite avant `t0`.
  - Un volet de points qui ne couvre pas tout au moment de la coupe montre le changement : le rayon maximal doit couvrir la diagonale d'une case.
  - Points trop petits : moiré.

## 7. Son

- **Musique** : boîte à outils « pop imprimée » : grosse caisse, caisse claire, claps, charleston de synthé ; basse carrée en croches ; un pincé façon marimba pour la mélodie ; pizzicato et claquements de doigts pour une scène furtive ; clochette de boîte à musique pour la tendresse.
- **Bruitages** (≈ 5 par 10 s, garde les plus lisibles) : **tampon** = boum qui descend + clic ; déclencheur d'appareil photo ; glissement de papier, rabat de chemise ; machine à écrire ; souffle avant un volet ; petits « pop » groupés sur un titre (un par mot plutôt qu'un par lettre) ; « boing » pour un personnage.
- **Voix** facultative : sèche, pince-sans-rire, ton de rapport, jamais essoufflée.
- Bruitages devant la musique sur les impacts. Mix −14 LUFS, crête ≤ −1 dB.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : dégradés ; trop d'encres ; texte qui frémit ; cartes surchargées ; fondus ; éclair blanc total.

- [ ] Points de trame, papier et au moins un élément de dossier visibles dans chaque image.
- [ ] Une idée, un titre, une pièce, une légende par carte ; carte de 2 à 4 s.
- [ ] Les titres ont leur ombre décalée dans l'encre d'ombre.
- [ ] Cinq encres au plus, plus le papier ; le rouge ne sert qu'aux tampons et alertes.
- [ ] Tout entre avec un dépassement ; aucun fondu.
- [ ] Le tampon claque en moins de 0,1 s, avec secousse et son sur la même image, après un court silence.
- [ ] Le frémissement ne touche que les personnages et accessoires dessinés.
- [ ] Barre de légende avec un mot-clé surligné, hors y > 1560 ; rien d'important à droite de x = 945.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 7
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Film de démo d'origine (30 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/halftone-dossier.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/halftone-dossier.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/halftone-dossier.jpg · galerie : https://lemomo-ai.github.io/lemo-opuscar/#print-printmaking
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre le sujet, la mascotte ni les cartes.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/halftone-dossier/STYLE.md`, `DEMO.md`, `demo/index.html` (tout le moteur), `music.py`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0.
- Adaptation Flot Web : traduction, mise en page verticale, typographie latine (la démo est en chinois), valeurs hex d'exemple proposées par Flot Web (la source nomme les encres), budget de bruitages, numéros du dictionnaire de mouvements, mise en garde sur les personnes réelles.
