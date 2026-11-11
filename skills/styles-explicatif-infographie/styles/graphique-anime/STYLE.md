# Graphique animé

## 1. Identité

- **Nom** : Graphique animé (graphiques de presse économique).
- **Fiche fusionnée** de deux sources : la grammaire « graphiques financiers » de huashu (mise en page de presse, ordre d'apparition, annotation unique, calage sur la voix) et le « graphique animé en boucle » de Charlie Hills (quatre états, valeurs intouchables, boucle sans saut).
- **Inspiration** : les graphiques des grands hebdomadaires et quotidiens économiques (un fin filet de couleur en haut, un titre qui est une conclusion, une seule couleur pour le héros, la source en bas) et les vidéos de données de leurs chaînes. On n'en reprend ni la police maison, ni le logo, ni le rouge de marque exact.
- **La règle en une phrase** : **on pose d'abord le repère, puis les données « poussent », puis on n'annote qu'une seule chose** ; une couleur pour le héros, le reste en gris ; **les valeurs sont toujours honnêtes** (barres depuis zéro, unité et source sur le graphique) : l'animation décide **comment** ça apparaît, jamais **combien**.
- **Marche pour** : croissance du chiffre d'affaires, des bénéfices ou du nombre d'utilisateurs ; cours d'une action ; parts de marché et classements ; comparaison de régions ; point de bascule avant/après un événement. Dès que la voix dit **un chiffre précis, une date, une comparaison**. Et tout passage qui doit être « crédible » (le spectateur fera une capture et vérifiera).
- **Ne marche pas pour** : un seul nombre (voir `nombre-jalon`) ; des données peu fiables ou sans source (mieux vaut pas de graphique) ; expliquer un principe (voir `maths-animees`) ; raconter des données avec une échelle humaine et des notes (voir `donnees-crayon`).

## 2. Palette, typographie, matières

| Rôle | Thème clair | Thème sombre |
|---|---|---|
| Fond | blanc `#FFFFFF` ou rose saumon `#FFF1E5` | `#0E1116` |
| Filet du haut et petit drapeau | rouge `#E3120B` (ou la couleur du client) | idem |
| Héros | bleu `#006BA2` | cyan `#3EBCD2` |
| Secondaires, avant de passer au gris | vert `#379A8B`, jaune `#EBB434` | idem |
| **Tout ce qui n'est pas le héros** | gris clair `#C6D2D8` | gris sombre |
| Gris neutre / noir | `#758D99` / `#0C0C0C` | texte clair |

- **Mettre en avant = une couleur pour le héros, le reste passe au gris.**
- **Hausse et baisse** : pour un public français, **vert = hausse, rouge = baisse** (la source d'origine, chinoise, utilise l'inverse). Variante lisible par les daltoniens : bleu et orange, avec les signes ▲ et ▼.
- **Polices** (libres) : Roboto Condensed (chiffres, axes) ; Inter ou Noto Sans (titres en 700, sous-titre et axes en 400). Les étiquettes d'axe sont les plus petites ; la source est la plus petite et la plus pâle.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : **Inter avec `font-variant-numeric: tabular-nums`** pour tout, chiffres compris (c'est le repli utilisé dans le rendu réel du 11/11/2026 : les compteurs ne tremblent pas) ; Oswald si l'on tient à des chiffres condensés. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/roboto-condensed`, `@fontsource/noto-sans` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Grille** : seulement des lignes horizontales, fines et grises (13 % d'opacité, 1,5 px) ; **seule la ligne de base zéro est un trait noir plein** (3 px) ; les valeurs de l'axe se posent au-dessus des lignes, côté droit.
- **Traits** : courbe principale 5 px ; moyenne 4 px ; trait de rappel d'une annotation 2 px.
- **Formes** : barres rectangulaires ; courbe terminée par un point rond ; chandeliers (corps et mèches) ; petit point avec trait de rappel.
- **Matières** : aucune. Pas de dégradé (sauf l'aire sous une courbe, de 14 % à 0 %), pas de lueur, pas de rebond.
- **Le graphique reste dans le monde du film** : son fond est de la même famille que les plans voisins. Dans un film sombre, thème sombre. Un graphique blanc qui surgit au milieu d'un film de nuit paraît « détaché ». Mieux : le poser **sur un objet du film** (un écran, un tableau, une feuille).

## 3. Composition 9:16

- **Mise en page de presse, adaptée au vertical** : filet de couleur de 8 px en haut de la zone utile (y 170) ; petit drapeau (96 × 22 px) à gauche ; **titre en gras = la conclusion, en une phrase** (64 à 76 px, 2 ou 3 lignes, y 220 à 480) ; sous-titre = l'indicateur et l'unité (38 à 42 px) ; graphique entre y 560 et y 1280, x 80 à 930 ; source en bas à gauche (28 px, jamais moins, y 1320 à 1360) ; mention **« Données d'exemple »** en bas à droite sur chaque image si les chiffres sont inventés.
- **En vertical, limiter le nombre de marques** : 5 à 7 barres verticales au plus ; au-delà, **barres horizontales** (étiquettes à gauche, valeurs au bout), jusqu'à 10. Étiquettes d'axe à 28 px au moins ; valeurs sur les barres à 36 px au moins. Ces tailles (28 à 44 px) sont sous les 50 px habituels du studio : c'est la taille d'un graphique de presse, déclarée dans les réglages de la section 8 (taille mini 28) ; tout le texte reste entre x 80 et x 930.
- **Le titre, les étiquettes et les axes ne bougent jamais l'un par rapport à l'autre.** Seul le graphique change. Quand une avancée `#027` ou un zoom `#020` est permis (section 4), c'est **le panneau entier** qui avance, d'un bloc : titre, axes, étiquettes et données ensemble, comme une feuille qu'on approche. On n'anime jamais un axe ou une étiquette seuls.
- **Écrire d'abord la « seule chose » de chaque graphique** : le titre est cette conclusion, l'annotation ne désigne qu'elle. Si l'on ne peut pas l'écrire, pas de graphique : un grand nombre, ou un autre style.
- **Les chiffres se recoupent** : un multiple annoncé dans le titre se recalcule avec les nombres du graphique (107,9 ÷ 12,4 = 8,70), et l'on écrit ce calcul dans l'annotation. Distinguer « **multiplié par** 8,7 » de « **augmenté de** 8,7 fois » : ce n'est pas la même chose (la source s'est fait reprendre là-dessus).
- Si l'axe ne part pas de zéro (pour une courbe), l'écrire dans le sous-titre.
- Pas plus de **3 graphiques de suite** avec la même mise en page : intercaler une poussée sur un détail, un grand nombre qui tombe, ou un retour à une image réelle.

## 4. Ce qui bouge

- **Action principale** : la donnée pousse. **Barres** : depuis la ligne zéro, avec une forte décélération, l'une après l'autre (décalage de 0,22 s, 1,3 s au total) ; l'étiquette de valeur suit le sommet et compte en même temps. **Courbe** : elle avance **selon le temps (l'axe horizontal), pas selon la longueur du trait** : le temps s'écoule à vitesse constante, donc une pente raide se trace vite et on **lit** l'envolée ; un point rond de 9 px et une étiquette de valeur suivent la tête.
- **Boucles de fond** : (1) pendant la tenue, quelque chose de petit vit : le point de tête qui bat doucement, l'anneau de l'annotation ; (2) en mode boucle, le retour en douceur à l'état de départ. **Pas de poussée de caméra lente et continue.**
- **Autorisés** : tracé de ligne `#004`, décalage en cascade `#002`, compteur `#007` (0,9 à 1,3 s, forte décélération, chiffres à largeur fixe), morphing de forme `#012` **entre deux formes d'une même donnée** (les barres s'amincissent en fils, puis une courbe se trace par leurs sommets), dépassement `#010` uniquement pour le point d'une annotation (ressort léger), pulsation `#125`, travelling avant `#027` **du panneau entier** (lent, environ 1 s, quand la voix désigne une zone ; 0,28 s seulement pour le chiffre le plus important du film ; jamais pour « faire bouger » un graphique qui se suffit), zoom à travers `#020` vers un détail, poussée `#137` entre deux panneaux, plan fixe `#175`.
- **Interdits** : rebond `#123` des barres, lueur et dégradés décoratifs, perspective 3D, barres qui ne partent pas de zéro, morphing entre **deux indicateurs différents** (une barre de chiffre d'affaires qui devient une courbe de cours laisse croire qu'ils ont la même unité), fondu qui remplace un graphique par un autre, toutes les barres d'un classement qui changent de place en même temps.
- **Ordre d'apparition** : mise en page (0 à 0,5 s) → lignes de grille une à une de gauche à droite (décalage de 0,12 s) → étiquettes de l'axe horizontal → données → le reste passe au gris → annotation. Chaque étape : 0,5 à 1,3 s.
- **Annotation** : elle se déclenche **à l'instant où la tête de la courbe passe l'événement** : le point surgit avec un anneau, le trait de rappel se trace 0,12 s après, le texte apparaît 0,3 s après. **Une seule annotation par plan.**
- **Chandeliers** : un par un (décalage de 0,06 s), le corps pousse de l'ouverture à la clôture, les mèches suivent.
- **Classement animé** : changements de rang d'environ 0,5 s, décalés entre eux ; 10 à 12 barres au plus.

## 5. Rythme et montage

- **Un graphique : 2,5 à 6 s**, avec une ou deux phrases de voix. Structure d'un passage : mise en place, déclencheur, sommet, retombée.
- **Le chiffre se pose à l'instant où il est dit** : on fixe d'abord les temps de la voix, puis on en déduit le début de chaque animation. Pour des barres, **un repère par barre** : chacune ne pousse que lorsqu'on en parle.
- **Après l'arrivée d'un chiffre, tenir au moins 0,5 s** sans rien bouger.
- **Transitions** : (1) le nouveau panneau pousse l'ancien, mené par une barre verticale de couleur (0,5 s) ; (2) poussée dans un détail (la caméra avance de 6 fois vers le dernier point, la vue rapprochée apparaît) ; (3) morphing entre deux formes de la même donnée ; (4) changer l'échelle d'abord (anciennes graduations qui s'effacent, nouvelles qui arrivent), les données ensuite ; (5) coupe sèche avec la mise en page immobile : seul le contenu change.
- **Mode boucle** (publication seule, 8 s) : quatre états : départ ; changement (environ 2 s, **rien ne s'efface pour être remplacé**) ; tenue (environ 4 s, la valeur principale étiquetée) ; retour (environ 1,5 s). La dernière image est identique à la première.
- **Version courte (8 à 12 s)** : un seul graphique : titre-conclusion et repère dès l'image 0, les barres ou la courbe avant 3 s, une annotation, tenue finale de 2 s ; couper le passage vers un second panneau. (Découpage tenu dans le rendu réel du 11/11/2026.)

## 6. Recette technique

- **Moteur** : HyperFrames. SVG animé par GSAP pour les graphiques simples (texte net, modifiable) ; canvas 2D avec `dessiner(t)` pour les chandeliers et les classements animés.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `donnees.json` (valeurs **exactes** du client, unité, source, indication « réel » ou « exemple »), `graphique.js` (échelle linéaire et son inverse, graduations en 1, 2, 2,5 ou 5 × 10ⁿ, grille, barres, courbe, chandeliers, annotation, drapeau, mention d'exemple), `film.js`.

```js
// barres : depuis zéro, forte décélération, en cascade ; l'étiquette compte la MÊME valeur
const quintOut = u => 1 - Math.pow(1 - u, 5);
barres.forEach((b, i) => { const p = quintOut(borner((t - b.tDit + 0.9) / 0.9));        // posée quand la voix dit le chiffre
  dessinerBarre(b.x, y(0), y(b.valeur * p)); etiquette(format(b.valeur * p), b.x, y(b.valeur * p) - 14); });
// courbe : on avance selon x (le temps), pas selon la longueur du trait
const xTete = x0 + (x1 - x0) * lisse(borner((t - t0) / 1.5)); tracerJusqua(serie, xTete); point(xTete, yDe(serie, xTete));
// annotation : déclenchée quand la tête passe l'événement (on inverse la courbe d'animation par dichotomie)
const tPassage = t0 + 1.5 * inverse(lisse, (xEvenement - x0) / (x1 - x0));
```

- **Extrait vérifié par un rendu réel** (11/11/2026) : barres et valeurs en SVG, un objet relais par barre, `onUpdate` et `gsap.set`. La barre et son étiquette lisent la même valeur, juste sur toutes les images du MP4.

```js
DONNEES.forEach((valeur, i) => {
  const etat = { v: 0 };                                  // objet relais : c'est lui que GSAP anime
  const maj = () => { const h = etat.v * PX;              // PX = pixels par unité
    gsap.set("#b" + i, { attr: { y: Y0 - h, height: h } });
    gsap.set("#v" + i, { attr: { y: Y0 - h - 16 }, textContent: String(Math.round(etat.v)) }); };
  tl.to(etat, { v: valeur, duration: 0.9, ease: "power4.out", onUpdate: maj }, debut + i * 0.22);
});
```

- **Piège du compteur** : `tl.seek(t)` n'appelle pas `onUpdate` (les évènements sont coupés par défaut) : un outil maison qui cherche dans la timeline doit écrire `tl.seek(t, false)`, sinon il voit un compteur à 0 et des barres vides. Le rendu HyperFrames, lui, déclenche bien `onUpdate`.
- **Style à plat et porte de livraison** : après l'arrivée, l'image s'arrête, et c'est la règle. Le film se déclare « Mouvement : calme » (section 8) ; n'ajoute pas de mouvement de caméra pour « passer » un contrôle.
- **Techniques clés** : ne jamais arrondir, reformater ni ajouter un nombre ; toutes les données inventées viennent d'un tirage à graine et portent la mention d'exemple ; les chiffres qui défilent sont à largeur fixe.
- **Pièges** : le titre qui apparaît à 0 s puis toutes les barres d'un coup ; un même nombre qui diffère entre deux plans ; une échelle changée en même temps que les données ; une vue rapprochée qui arrive comme une petite carte flottant au milieu ; un compteur qui saute sur sa dernière image ; une unité collée au nombre.
- **Contrôle** (mode boucle) : capturer les images à 0, 1, 2, 4 et 7 s ; vérifier que les valeurs sont restées les mêmes, que rien ne se chevauche ni n'est coupé, que chaque élément n'apparaît que quand il faut. Ne signaler que les problèmes réellement observés.

## 7. Son

- **Musique** : sobre, régulière, un peu « journal télévisé » : pulsation discrète, piano ou synthétiseur doux.
- **Bruitages** : un glissement feutré pour la grille, **un seul son continu** (frottement ou tics fins) pendant qu'une courbe se trace ou qu'un compteur tourne, un coup feutré quand le chiffre se pose, un « pop » pour le point de l'annotation. Pas un son par barre : un son pour la série, un accent sur le héros.
- **Silence** : une respiration juste avant le chiffre principal, puis la tenue de 0,5 s presque sans son.
- **Voix** : claire et factuelle ; les nombres dits en entier, avec leur unité.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Le titre est une conclusion en une phrase, et l'unique annotation désigne cette conclusion.
- [ ] Les barres partent de zéro ; l'unité et la source sont sur le graphique.
- [ ] Chaque valeur à l'écran est exactement celle fournie ; les données inventées sont marquées « Données d'exemple » sur chaque image.
- [ ] Une seule couleur pour le héros ; tout le reste est gris.
- [ ] Le repère arrive avant les données ; titre, axes et étiquettes ne bougent plus ensuite.
- [ ] Chaque chiffre se pose à l'instant où la voix le dit, puis l'image tient 0,5 s.
- [ ] Vert pour la hausse, rouge pour la baisse (ou bleu et orange avec ▲ ▼).
- [ ] 5 à 7 barres verticales au plus ; aucune étiquette sous 28 px.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : fixe
- Couleurs max : 11
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 28

## 9. Aperçu

- Grammaire « graphiques financiers », planche de la démo (une image par plan, 16:9, données fictives) : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/t3_finance_chart_总览.jpg — crédit : 花叔 Huashu (alchaincyf).
- Graphique animé en boucle : pas d'aperçu propre dans le dépôt ; présentation de l'auteur sur https://github.com/charlie947/motion-graphics-skills — crédit : Charlie Hills. Voir aussi l'effet 05 « Barres → courbe » dans `references/effets.md`.

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichiers `references/动画语法/t3_finance_chart.md`, `scripts/engine/demos/t3_finance_chart/`, `scripts/engine/lib/chart.js`. Licence MIT (© 2026 alchaincyf, 花叔).
- Dépôt `charlie947/motion-graphics-skills`, commit `229022e`, fichier `skills/animated-chart/SKILL.md`. Licence MIT (© 2026 Charlie Hills).
- Polices Roboto Condensed, Inter, Noto Sans : Apache 2.0 ou OFL 1.1.
- Adaptation Flot Web : fusion des deux sources, traduction, convention française des couleurs de hausse et de baisse, mise en page verticale et limites de marques, portage vers HyperFrames, numéros de mouvements, règles de son du plugin.
- Vérifié par un rendu réel le 11/11/2026 (HyperFrames 0.9.33) : image conforme et chiffres justes sur toutes les images ; l'ancienne porte de livraison refusait ce style à plat (mouvement mesuré 0,0 %), d'où le réglage « Mouvement : calme ».
