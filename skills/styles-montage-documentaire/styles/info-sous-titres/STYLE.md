# Info sous-titres (actu lisible sans le son)

## 1. Identité
- **Nom** : Info sous-titres. Identifiant : `info-sous-titres`.
- **Inspiration** : l'info « réseaux sociaux » du milieu des années 2010, où l'on comprend tout sans le son, et les explicatifs horizontaux qui posent une grosse typo sur des images. Grammaire seulement : aucun logo, aucune police, aucun habillage de média réel, et on ne les nomme jamais dans la vidéo.
- **Principe** : le sous-titre est le plan. Une phrase énorme, claquée par blocs de 2 ou 3 mots, avec un seul mot-clé sur un pavé jaune. Chaque chiffre arrive avec sa source ; le document d'origine est montré et surligné avant qu'on croie le chiffre. Le plus gros chiffre du film tombe dans les 0,15 premières secondes. Un seul retournement : la mauvaise nouvelle du hook est relue par un fait qui en change le sens.
- **Pour quels sujets** : actu d'un secteur, explication d'un rapport ou d'une étude, court de données, « le chiffre de la semaine » d'une niche.
- **Ne marche pas pour** : un récit sans chiffres ni documents, un tutoriel, un sujet où le client n'a ni images ni source vérifiable. Ce n'est pas un film de données (les graphiques sont de courts inserts), ni un JT (pas de présentateur, pas de bandeau défilant), ni une présentation (pas de titres centrés, pas de puces).

## 2. Palette, typographie, matières
| Rôle | Valeur |
|---|---|
| Texte des sous-titres (ivoire) | `#F7F5EF` |
| Mot-clé, gains, point à retenir (miel) | `#FFC21A`, texte posé dessus `#0E0E0C` |
| Pertes, pic, mauvais chiffre | `#FF4A3D` |
| Libellés et unités | `#8D8B83` ; barres secondaires `#5E5C55` |
| Fond des cartes de données (« registre ») | `#151512`, lignes réglées tous les 54 px (blanc à 4,5 %), double marge rouge fine à gauche |

- **Polices libres** : sous-titres en sans très gras (Inter Tight 800 ou Montserrat ExtraBold) ; chiffres en Inter Tight 800 **à chasse fixe** (chaque chiffre dans une case de largeur égale, sinon le compteur tremble) ; libellés en Inter Tight 500.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Inter à la place d'Inter Tight ; Montserrat : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/inter-tight` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La police de la marque ou de la chaîne vient du client : à vérifier (licence, accents français).
- **Matières** : vraies images, photos et pages de document. Étalonnage unique pour toutes les images : `contrast(1.07) saturate(0.92) brightness(0.98)` + voile chaud à 6 % (4 % sur les documents). Les textes, chiffres et graphiques sont toujours vectoriels, jamais une image agrandie.
- La couleur d'accent peut devenir celle de la fiche « ma chaîne » du client, à condition de n'en garder qu'une.

## 3. Composition 9:16
Le vertical est une autre mise en page, pas un recadrage du 16:9.
- **Bande image** : 1080×1560 en haut (une source horizontale s'agrandit de 1,5× au plus ; au-delà, bandes floues interdites : recadrer ou changer de plan).
- **Sous-titre** : sous la bande image, entre y 1230 et y 1500, aligné à gauche à x 90, sur **deux lignes** de 2 à 3 mots (la règle « une seule ligne » vaut pour le 16:9). Corps 84 à 96 px, 110 px pour la phrase de verdict. **Chaque ligne, pavé jaune compris, s'arrête avant x 945** : au rendu réel, un compteur dépassait de 2 px et un pavé « 10 % » de 19 px, tous deux refusés ; mesurer la boîte entière, pas les lettres. Le sous-titre passe la ligne conseillée y 1330 : c'est voulu par ce style, et il reste au-dessus de y 1560.
- **Pastille de chaîne** : en haut à gauche, sous y 170 (zone d'interface du haut ≈ 160 px), 46 px de haut : pavé jaune + nom de l'émission du client.
- **Étiquette de source** : juste sous la pastille, 34 px minimum (taille déclarée dans les réglages de la section 8), seulement sur les plans de chiffres et de documents ; elle glisse en 0,2 s.
- **Crédit d'image** : en haut à droite mais à gauche de x 945 (colonne de boutons ≈ 135 px), 28 px minimum sur pastille sombre à 50 % (à 24 px, le contrôle `check` le refuse : constaté au rendu réel du 11/11/2026).
- Rien d'important sous y 1560 (zone basse 360 px) ni à droite de x 945. Dégradé sombre sous le sous-titre (0 → 84 %) ; dégradé en haut sous la pastille.
- **16:9** : sous-titre sur une seule ligne, aligné à x 120, ligne de base y ≈ 948 ; graphiques à droite du centre, titre et source en haut à gauche, jamais centrés.

## 4. Ce qui bouge
- **Action principale** : le claquement du sous-titre. Chaque bloc entre 0,12 s après le précédent : échelle 1,3 → 1 en 0,13 s (retour avec dépassement 1,6), opacité pleine en 0,04 s. Le pavé jaune s'essuie de gauche à droite en 0,12 s derrière le mot-clé (un seul par sous-titre).
- **Boucles de fond** : (1) poussée lente dans chaque carte (×1,025 à ×1,03 sur la durée du plan) ; (2) compteurs qui roulent en ralentissant et changent de couleur à l'arrivée.
- **Autorisés** (dictionnaire `principes-mouvement`) : #007 compteur, #010 dépassement, #004 tracé de ligne, #080 surligneur, #040 arrêt sur image, #144 écran partagé, #017 transition par masque (une photo qui sort de la forme d'une région sur la carte), #046 coupe sèche, #047 J-cut.
- **Interdits** : #044 fondu enchaîné, #140 page qui tourne, #021 retournement 3D, #006 machine à écrire, tout sous-titre qui bouge pendant qu'on le lit.

## 5. Rythme et montage
- Coupes sur une grille de demi-temps à 120 BPM (chaque coupe à un multiple de 0,5 s). Plans d'images 1,5 à 3 s ; cartes de données et documents 3 à 4,5 s ; une comparaison reste jusqu'à ce que chaque élément ait été entièrement visible 2,5 s.
- **Les sous-titres traversent les coupes** : l'image change, pas les mots. Un sous-titre change au plus toutes les ~2,5 s, reste ≥ 1,8 s et idéalement la durée de la phrase dite + 0,6 s.
- **Ordre d'un fait** : image (l'émotion) → le chiffre sur une carte → la ligne du document qui le dit → la conséquence. Jamais un chiffre sans son étiquette de source dans le même plan.
- Transitions, peu et fixes : coupe sèche (défaut) ; flash blanc de 1 à 2 images sur le retournement et l'arrêt sur image ; carte qui glisse de la droite en 0,18 s ; écran partagé qui s'ouvre depuis son séparateur ; panneaux de grille qui montent décalés de 0,1 s ; coup de zoom (0,3 s, jusqu'à ~1,25×) sur le coupable.
- Une action forte dans la première demi-seconde de chaque plan ; rien de figé plus d'1 s ; une respiration de 2 à 3 s après le retournement ; deux vrais silences.
- **Version courte (8 à 12 s)** : quatre plans de 1,5 à 3 s, trois sous-titres (1,8 s au moins chacun), une seule carte de données ; le chiffre énorme est à l'écran dès l'image 0. (Découpage tenu dans le rendu réel du 11/11/2026.)

## 6. Recette technique
- **Moteur** : HyperFrames. Les rushes passent par `<video class="clip" data-start data-duration>` ; les sous-titres, cartes et graphiques sont du HTML/SVG animé par une timeline GSAP en pause.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : un fichier `timeline.json` unique (texte de chaque sous-titre découpé en blocs, mot-clé, heure de début de la voix, silences, impacts) lu par la page, par le sous-titrage `.srt` et par le mix.
- **Sous-titre par blocs** :
```js
blocs.forEach((b, i) => tl.fromTo(b, {scale: 1.3, opacity: 0},
  {scale: 1, opacity: 1, duration: 0.13, ease: "back.out(1.6)"}, debut + i * 0.12));
tl.fromTo(pave, {scaleX: 0}, {scaleX: 1, transformOrigin: "left", duration: 0.12}, debut + 0.1);
tl.set(groupe, {opacity: 0, visibility: "hidden"}, fin); // un seul groupe visible à la fois
```
- **Document surligné** : rendre la page du PDF en image à 220 dpi, la poser comme une feuille blanche sur un bureau sombre (inclinaison ±1 à 2°), placer les rectangles de surlignage d'après les coordonnées du texte (`pdftotext -bbox`, 1 pt = 3,0556 px à 220 dpi), les balayer de gauche à droite en 0,3 à 0,5 s, puis reposer le chiffre lu en gros pavé jaune à côté. Ce qui doit être lu est recomposé en typo ; le texte imprimé reste une image.
- **Limites d'agrandissement** : image récente ≤ 1,5× ; photo ≤ 1:1 ; archive ≤ 2,5× après débruitage. Préparer les plans à leur taille finale avec ffmpeg (recadrage, `lanczos`, `unsharp=5:5:0.45`).
- **Vérifié par le rendu réel du 11/11/2026** : sous-titres en blocs claqués à gauche sur deux lignes, un seul pavé jaune par sous-titre, chiffre énorme dès l'image 0, carte lignée, page surlignée. Un pavé ou un chiffre doit rester posé 1 s au moins ; le texte imprimé d'un document (une image) se marque `data-passage` pour ne pas être compté comme texte à lire ; chaque `<audio>` porte `data-duration`.
- **Pièges** : commencer l'animation d'un écran partagé ou d'une grille 0,1 à 0,15 s avant la coupe (sinon première image vide) ; recadrer les logos de chaîne au lieu de les couvrir ; flouter numéros de téléphone, plaques et noms lisibles ; écarter les plans au texte incrusté ; `mix-blend-mode: multiply` du surligneur seulement sur la feuille, pas sur une couche plein écran.

## 7. Son
- **Voix** : un narrateur vif (débit un peu rapide), chiffres écrits en toutes lettres dans le texte de la voix, voix ≈ 8 dB au-dessus de la musique.
- **Musique** : pulsation à 120 BPM (grosse caisse sur le temps, basse en croches, ostinato de marimba, accents de cuivres sur les gros chiffres). Arrêt net dans le silence avant le retournement ; retour sur un accord majeur.
- **Bruitages** (budget du skill `son` : environ 5 par 10 s, vrais enregistrements d'abord) : claquement du bloc de texte, cliquetis de compteur, souffle d'entrée d'une carte, crissement du surligneur, obturateur sur l'arrêt sur image. Choisir les plus parlants, pas tous.
- **Son naturel** du sujet en J-cut 0,3 s avant l'arrêt sur image. Master −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
Erreurs : texte illisible dans la durée du plan ; voix qui finit pile sur la coupe (raccourcir la phrase) ; mots plus forts que la source (« facteur de stress » n'est pas « tueur ») ; image d'illustration présentée comme le lieu du sujet.
- [ ] La vidéo se comprend sans le son (visionnage muet complet).
- [ ] Le plus gros chiffre est lisible avant 0,2 s et l'image 0 n'est ni noire ni un logo.
- [ ] Chaque chiffre a son étiquette de source dans le même plan, et un fichier `FAITS.md` donne l'adresse et la phrase citée.
- [ ] Un seul mot-clé jaune par sous-titre ; chaque sous-titre tient ≥ 1,8 s.
- [ ] Aucun plan agrandi au-delà de sa limite ; aucun logo tiers à l'écran.
- [ ] Chaque plan sous licence CC BY porte son crédit à l'écran ; tous les crédits sont dans `CREDITS`.
- [ ] Rien d'important dans les zones d'interface (haut 160, bas 360, droite 135).
- [ ] −14 LUFS mesuré sur le fichier final.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 7
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu
- Film de démo d'origine : https://lemomo-ai.github.io/lemo-opuscar/films/caption-news.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/caption-news.jpg
- Crédit : « The Bee Ledger », LemoLab, CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Le film contient des images et photos de tiers sous leur propre licence : **lien seulement**, ne pas en extraire de plans. La démo est en 16:9 et bilingue ; notre version verticale en français reste à produire.

## 10. Origine
- Dépôt : lemomo-ai/lemo-opuscar, commit `9eb7739`. Fichiers : `styles/caption-news/STYLE.md`, `style.json`, `demo/main.js` (fonctions `hook()`, `capCard()`, `paper()`, `shotSplit()`, `shotGrid()`).
- Licence : MIT (© 2026 LemoLab) pour le texte et le code ; films et images de démo CC BY 4.0.
- Adaptations Flot Web : passage en français et en une seule langue, mise en page 9:16, moteur HyperFrames, budget de bruitages du skill `son`. Matériel : voir `references/materiel-et-droits.md`.
- Vérifié par un rendu réel le 11/11/2026 (HyperFrames 0.9.33) : ça marche avec corrections (trois boîtes de texte ramenées dans la zone, crédit passé à 28 px) ; 12 textes contrôlés sans refus ; son hors cible faute de voix et de musique.
