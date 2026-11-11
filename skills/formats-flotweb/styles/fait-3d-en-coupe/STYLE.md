# Fait insolite en 3D vue en coupe

## 1. Identité
- **Nom** : Fait insolite en 3D vue en coupe. Identifiant : `fait-3d-en-coupe`.
- **Inspiration** : les comptes de « faits étonnants expliqués en 3D », où l'on voit une maison, un terrain ou un objet tranché comme une maquette. On en reprend le format, jamais un texte, un plan ni un personnage.
- **Principe** : un **bloc de terrain coupé net, la terre visible en bas**, posé comme une maquette vue de face. Dessus, une scène (une maison et son jardin, un immeuble, une cabane, un chantier) qui **se transforme étape par étape** pendant qu'une voix raconte un fait : un problème, puis la solution, puis le suivant. Chaque élément nouveau surgit avec un petit « pop », pile sur le mot qui le nomme.
- **Pour quels sujets** : « comment on construit… », « pourquoi… ne s'effondre pas », « ce qu'il y a sous… », un objet ou un lieu du quotidien vu de l'intérieur, une suite de problèmes et de solutions.
- **Ne marche pas pour** : une idée abstraite sans lieu ni objet, un portrait, un sujet qui tient en une image. Sujets à refuser : tout ce qui reviendrait à un mode d'emploi dangereux.
- **Ce que la fiche « ma chaîne » fournit** : le ton et la personne grammaticale de la voix, la voix, la palette d'habillage (sous-titres, cartes), la police, la **mascotte** récurrente s'il y en a une (rubrique « personnages récurrents »), la formule de chute, la durée.

## 2. Palette, typographie, matières
- **Décor en couleurs naturelles, vives et saturées** : façades claires (crème `#F3E6CC`, pas de beige olive), pelouse rayée, herbe sauvage, toits de tuiles, bois, brique, **terre brune de la coupe avec ses racines**. Ciel en dégradé avec un soleil, brouillard léger, ombres douces.
- **La terre de la coupe est légèrement auto-éclairée** pour rester brune même à contre-jour ; le bloc de terre est assez profond pour qu'on ne voie jamais dessous.
- **Habillage** aux couleurs de la fiche « ma chaîne » ; à défaut : sous-titres blancs à contour noir, cartes d'information crème arrondies, mot de chute dans une couleur d'accent chaude (`#FFC857`).
- **Police** : celle de la chaîne ; à défaut une ronde très grasse et libre (Fredoka, Baloo 2).
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Fredoka et de Baloo 2. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/fredoka`, `@fontsource/baloo-2` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`. La police de la marque ou de la chaîne vient du client : à vérifier (licence, accents français).
- **Mascotte** (facultative) : celle du client, présente dans chaque scène, dans une zone où elle peut tenir debout. Sans mascotte : un petit personnage simple créé avec le skill `personnages`, ou aucun.
- **Couleurs relevées, jamais devinées** : pour tout animal, personnage ou objet vedette, relever la couleur exacte sur la référence et la noter dans une fiche.

## 3. Composition 9:16
- **Plan de base = de face, léger trois quarts, assez reculé** : la scène entière en haut (le toit et sa cheminée compris), tout le terrain et ses limites au milieu, **la coupe de terre en bas**. Repère de départ : caméra à (5 ; 10,5 ; 29), cible (−1 ; 1,8 ; 4), champ 50°.
- **En vertical le champ horizontal est étroit** : préférer un champ de 50 à 55° plutôt que de rapprocher la caméra.
- **Sous-titres : un mot à la fois**, en capitales, au centre de l'écran (vers y 960), 90 à 120 px, avec un petit « pop ».
- **Étiquettes 3D et cartes** : nettement **au-dessus ou au-dessous du centre**, jamais sur le sous-titre ; cartes d'information en haut, sous y 170.
- **Le décor va jusqu'aux bords** ; rien d'important au-dessus de y 160, sous y 1560, à droite de x 945. La coupe de terre peut descendre dans la zone basse : c'est du décor.
- **Couverture** : 1080×1920 composée pour un affichage recadré en 3:4 (zone utile y 240 à y 1680), plan large de face qui montre le plus d'éléments, accroche en haut, mot de chute en couleur en bas.

## 4. Ce qui bouge
- **Action principale** : l'élément qui apparaît sur son mot, avec un petit « pop » (amorti avec léger dépassement), et la scène qui se transforme.
- **Boucles de fond** : (1) dérive lente de la caméra (~5 %) pendant chaque plan ; (2) la vie du décor : nuages, fumée de cheminée, feuillage, eau, la mascotte qui respire et réagit.
- **Caméra** : **zooms légers** (on se rapproche d'un élément, mais tout ce qui compte reste dans le cadre ; on ne coupe jamais l'objet dont on parle) ; **transitions douces** de 0,8 à 1,2 s en accélération-décélération. Jamais de coupe brutale ni de plongée profonde. Aucun plan bouché par une clôture ou un arbre au premier plan.
- **La mascotte joue** : elle arrive, a peur, glisse, se réjouit ; une réaction par étape. À la fin, elle est **visible et devant** (pas cachée sous un toit).
- **Autorisés** : #001 apparition en pop, #010 dépassement, #027 travelling avant léger, #025 panoramique doux, #016 parallaxe (naturelle en 3D), #002 décalage en cascade, #121 anticipation (mascotte), #011 écrasement et étirement (mascotte), #007 compteur sur une carte.
- **Interdits** : #046 coupe sèche et #043 filé entre plans, plongée ou zoom profonds, #034 caméra qui tremble, plans de côté inventés, élément visible avant son mot, objets qui se traversent.

## 5. Rythme et montage
- **50 à 60 s**, environ **150 à 170 mots** de voix.
- **Structure** : accroche forte (une situation, pas un objet) → étapes « problème → solution » enchaînées, chacune ajoutant un élément à la scène → chute (la formule de la chaîne).
- **L'accroche se lit dans les 10 premières secondes** : le bon sujet au premier plan, tout de suite.
- **Tout est calé sur la voix** : une table de chronologie donne l'instant de chaque apparition d'après les mots horodatés.
- Un plan de caméra par étape ; la scène n'est jamais figée.
- Si l'on part d'une référence : protocole `references/mesurer-une-reference.md` (notre propre version du sujet, tableau des plans, plan d'implantation).
- **Version courte (8 à 12 s)** : garder l'accroche et **une seule étape** « problème → solution » (deux éléments qui apparaissent chacun sur leur mot), en deux plans de caméra ; couper les autres étapes, la carte d'information et la chute longue. Accroche avant 3 s : le sujet au premier plan et le premier élément qui surgit dès la première phrase.

## 6. Recette technique
- **Moteur** : **Three.js** piloté image par image (éprouvé sur ce format : la scène se reconstruit à chaque étape et se cale au mot), intégré à HyperFrames par `hf-seek`. **Blender** par le connecteur `blender` quand le client veut des matières et une lumière de qualité supérieure : même plan d'implantation, mêmes règles de caméra, rendu en séquence d'images, sous-titres et cartes ajoutés dans HyperFrames.
- **Avant toute 3D : le plan d'implantation** vu de dessus, étape par étape (`references/mesurer-une-reference.md` §3) : zones réservées, points d'arrivée, supports, positions praticables de la mascotte.
```js
const T = { piscine: mot("piscine").debut, toit: mot("toit").debut };              // chronologie calée sur la voix
const CLES = [[0, [5,10.5,29], [-1,1.8,4], 50], [6.2, [3,8,22], [-2,1.5,3], 52]];   // [t, position, cible, champ]
const pop = (t, t0) => backOut(clamp((t - t0) / 0.35, 0, 1));                      // 0 avant son mot
window.addEventListener("hf-seek", (e) => {
  const t = e.detail.time;
  piscine.visible = t >= T.piscine; piscine.scale.setScalar(pop(t, T.piscine));
  poserCamera(interpoler(CLES, t, 1.0));        // transitions d'environ 1 s, lissées, + dérive de 5 %
  composer.render();
});
```
- **Couleurs vives (réglage par défaut)** : **soleil de face, du côté de la caméra**, pour que les façades et le sujet soient éclairés avec de vraies ombres portées (soleil derrière la scène = tout ce qu'on filme est à l'ombre et terne) ; **courbe de tons neutre** (la courbe « cinéma » délave les couleurs) ; saturation ≈ 1,4, contraste léger, tons un peu chauds, vignette ≈ 0,14 ; matériaux clairs et saturés. Comparer avant / après sur deux images si l'on touche à la lumière.
- **Finition** : éclairage d'environnement tiré du ciel, ombres de contact (occlusion ambiante), exposition un peu relevée. Masquer les éléments plats du ciel (nuages, fumée) pendant la passe d'ombres de contact, sinon des rectangles sombres apparaissent.
- **Anti-clignotement** : tampon de profondeur logarithmique ; **jamais deux faces dans le même plan qui se chevauchent** (décaler de 0,02).
- **Personnages** : construire les membres **comme enfants du corps**, pas de la racine, sinon ils se détachent quand le corps bascule.
- **Tester chaque cadrage** en image fixe basse résolution, à côté de l'image de la référence au même instant, avant le rendu complet.
- **Rendu** : long avec la finition (compter plusieurs secondes par image) : prévenir le client de la durée réelle dès le début ; rendu reprenable (les images existantes sont sautées) ; pour corriger une scène, ne supprimer que ses images. Grain éventuel à l'encodage, jamais dans la page.
- **Pièges vécus** : eau très fine qui disparaît d'un coup entre deux images (faire un fondu d'opacité sous un certain niveau) ; pluie trop dense près de la caméra (limiter sa zone en profondeur, opacité ~0,3) ; mise à l'échelle non uniforme d'un objet dont la géométrie n'est pas centrée (il part ailleurs) ; personnage trop petit derrière un garde-corps vitré ; ciel dessiné par-dessus les effets.

## 7. Son
- **Vrais enregistrements** (skill `son`) : à l'écoute, des bruitages fabriqués en code sonnent « plastique ». Synthèse en repli seulement, pour un son introuvable.
- Une ambiance de fond discrète ; **un bruitage par évènement important de la chronologie**, attaque calée sur l'image, hauteur légèrement variée pour éviter la répétition ; 2 ou 3 souffles de caméra par vidéo, pas un à chaque mouvement (budget : environ 5 bruitages par 10 s).
- **Toujours couper chaque son à sa durée utile** : certains fichiers de banque sont des boucles de plusieurs minutes ; chargé en entier, un son tourne jusqu'à la fin de la vidéo. Moteurs et bourdonnements : très bas, et seulement pendant leur plan.
- Voix au-dessus de tout (baisse automatique du reste sous elle) ; **−14 LUFS**.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle
- [ ] L'accroche se lit dans les 10 premières secondes (une image toutes les 0,5 s regardée en taille lisible) : bon sujet au premier plan, bonnes couleurs.
- [ ] Plan d'implantation respecté : rien dans une zone réservée, chaque chose arrive au bon endroit, toute structure en hauteur a ses supports.
- [ ] Rien n'est visible avant son mot.
- [ ] Gros plan de chaque personnage dans chaque position : membres attachés et posés, rien qui flotte ni traverse, couleur conforme à la fiche.
- [ ] La scène entière reste dans le cadre de base ; aucun zoom ne coupe l'objet dont on parle ; aucune coupe brutale.
- [ ] Aucun clignotement sur les surfaces fixes (comparaison d'images consécutives).
- [ ] Étiquettes jamais sur le sous-titre ; rien d'important dans les zones d'interface.
- [ ] Façades et sujet éclairés (soleil de face), couleurs vives ; relecture complète image par image faite, en boucle, avant livraison.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 12
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 50

## 9. Aperçu
- Format maison Flot Web : pas d'aperçu de tiers. Aperçu à produire avec le plugin (un bon candidat de vitrine).

## 10. Origine
- Source : format de production « fait du jour en 3D vue en coupe » du plugin Flot Web (fiche de série et son moteur), **rendu générique** : toute référence à la série, à sa mascotte, à ses comptes, à sa voix, à ses dossiers et à ses outils de publication a été retirée ; le format lit la fiche « ma chaîne » du client.
- Bibliothèque : three.js (MIT). Aucun code de tiers recopié.
- Adaptations : intégration HyperFrames (`hf-seek`), Blender en option, budget de bruitages et −14 LUFS du skill `son`.
