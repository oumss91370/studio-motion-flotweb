# Isométrique au trait fin

## 1. Identité

- **Nom** : Isométrique au trait fin.
- **Inspiration** : les figures isométriques au trait des documentations de produits techniques : objets en perspective isométrique 2:1 sur fond blanc, dessinés seulement en traits fins constants. La source a étudié des figures sous licence libre sans les recopier ; on ne prétend reproduire aucune marque.
- **Ce que c'est** : une illustration de produit **calme et précise**. Silhouettes et arêtes grises, lignes intérieures et fuyantes plus claires, **faces remplies de blanc** pour que les objets proches cachent les lignes lointaines. Dalles et plaques arrondies à épaisseur visible, couches empilées, grilles de pièces répétées (touches, ouïes, piliers, ports), et **un seul minuscule accent sombre par image**. Mouvement fluide qui se pose sur un ressort ; sinon, immobile.
- **Marche pour** : expliquer un produit, un appareil, une infrastructure (serveurs, réseau, entrepôt), une architecture logicielle en couches, un parcours « de l'ordinateur au serveur », une notice sobre, une page d'accueil.
- **Ne marche pas pour** : émotion, personnages, sujet organique (nourriture, nature, corps), public enfant, tout ce qui demande de la couleur.
- C'est le style le plus simple de la catégorie : aucun rendu 3D, aucun moteur à installer.

## 2. Palette, typographie, matières

| Rôle | Fond clair | Variante fond sombre |
|---|---|---|
| Papier et **toutes les faces** | `#FFFFFF` | `#101014` |
| Arêtes : silhouettes, face tournée vers nous, arêtes vives, câbles | `#A4A4AC` | `#8E8E9A` |
| Lignes intérieures et fuyantes : plis des coins arrondis, cadres, ouïes | `#C8C8D0` | `#44444E` |
| **Accent** : le point d'attention (curseur, voyant actif). **Un par image.** | `#232327` | `#F4F4F6` (l'accent devient le plus clair) |
| Texte / texte discret | `#5C5C64` / `#9A9AA2` | `#B4B4BE` |

- **Pourquoi `#C8C8D0` et non le `#E0E0E4` de la source** : à 360 px de large (un téléphone), un trait de 2 px devient 0,67 px et pâlit d'environ 40 % (mesuré sur le MP4 du 11/11/2026 : gris médian du trait 175 → 207 sur 255). Les arêtes `#A4A4AC` tiennent de peu ; les lignes intérieures `#E0E0E4` disparaissaient presque (cadre d'écran, pavé tactile, ouïes). Avec `#C8C8D0`, elles restent visibles et nettement plus claires que les arêtes (comparaison faite sur une capture réduite à 360 px ; pas de nouveau film rendu). La variante sombre est relevée dans la même proportion (calcul, non rendue).
- Un fond blanc occupe ≈ 97 % de l'image : c'est voulu. Les remplissages blancs font le travail des lignes cachées.
- **Trait : 2,0 px constants pour une image de 1080 px de large**, la même graisse partout ; seule la couleur change (arête ou ligne intérieure). Jonctions et bouts ronds. Aucun tremblement, aucun frémissement.
- **Avec la marque du client** : l'accent peut prendre la couleur de la marque ; rien d'autre ne se colore.
- **Typographie** : une linéale pour les légendes (46 px, centrée, un filet de 44 px au-dessus) ; une chasse fixe pour étiquettes et textes tapés. Polices libres conseillées : **Inter** et **JetBrains Mono** (OFL). Les étiquettes posées sur un objet sont **inscrites dans la face** (les lettres suivent l'inclinaison du plan).
- **Police de repli** : aucune à prévoir, Inter et JetBrains Mono sont fournies par HyperFrames et se chargent par leur nom. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : rien à télécharger ; pour embarquer quand même le fichier, `@fontsource/inter`, `@fontsource/jetbrains-mono` (vérifié par `npm view` le 11/11/2026).
- **Matières** : aucune. Ni ombre, ni dégradé, ni grain, ni couleur. Le détail vient de la **répétition** (une grille de touches, d'ouïes, de ports, de plaques), pas de la texture ; les grandes faces restent vides.

## 3. Composition 9:16

- **Un groupe d'objets au milieu**, dont la silhouette occupe ≈ 75 à 80 % de la largeur (≈ 800 px) ; du blanc tout autour ; rien ne touche le bord.
- En vertical, **empile** : un ordinateur sur un socle à couches, une baie de serveurs, une pile de plaques, un immeuble en étages. L'objet se place entre y 420 et 1250.
- **Légende** bien en dessous de l'objet (y 1340 à 1500, entre x 100 et x 905), 46 px, deux lignes au plus (taille déclarée dans les réglages de la section 8 ; tenue ≥ 1,25 s, 2 s pour la dernière). **Étiquette numérotée** (chiffre + mot en chasse fixe) près de la partie concernée.
- Projection **dimétrique 2:1** : les arêtes montent d'un demi-pixel par pixel (26,57°).
- Dalles : épaisseur de 2 à 5 % de l'objet, coins arrondis de 5 à 10 % du grand côté. Les empilements montrent leurs couches (un écart ou un retrait entre les plaques).
- 16:9 : même règle, l'objet à ≈ 45 % de la largeur ou deux groupes côte à côte.

## 4. Ce qui bouge

- **Action principale** : un objet **se pose, s'ouvre ou glisse**, et se stabilise sur un ressort (un ordinateur qui s'ouvre, une lame qui sort d'une baie).
- **Boucle de fond 1** : un voyant qui bascule une fois par seconde (entre contour et gris, jamais sombre : le sombre est réservé à l'accent).
- **Boucle de fond 2** : une vie minuscule : vapeur d'une tasse, feuille qui oscille, léger flottement du petit héros.
- **Autorisés** : `#010` dépassement sur ressort, `#002` apparitions en cascade **le long de la diagonale isométrique** (touches qui montent en vague, 28 ms d'écart par rang), `#006` texte tapé, `#004` trait qui se dessine, `#012` métamorphose d'une face en une autre (le curseur sombre devient la façade d'un serveur), `#143` vue éclatée par couches, `#027` avancée lente de quelques pour cent (zoom ≤ 1,05), `#175` plan fixe.
- **Interdits** : `#024` secousse, `#028` coups de zoom, `#136` trait qui frémit, `#015` particules, `#016` parallaxe, `#022` balayage de lumière, ombres, couleur, tout apparaître en même temps, un second élément sombre pour « insister » (on **déplace** l'accent).
- Les choses **tombent en place** (plaques, accessoires), **montent** (touches), **s'ouvrent** (un couvercle sur sa charnière), **glissent** (une lame hors d'une baie). Entre deux mouvements, **l'image est vraiment immobile** : le film se déclare « Mouvement : calme » et « Caméra : fixe » (section 8), pour que les contrôles n'exigent pas un mouvement que le style interdit.
- Petit héros possible : un cube arrondi à deux yeux sombres qui clignent, une antenne qui oscille après un saut.

## 5. Rythme et montage

- Mouvement à pleine cadence, sans saccade. Tempo de référence 120 BPM ; chaque mouvement part sur un temps et se pose en 0,4 à 0,8 s.
- Un plan = une idée, 3 à 6 s : arrivée, pose, tenue immobile, légende.
- Transition du style : la **métamorphose de forme** entre deux objets dans le même plan incliné ; sinon coupe franche.
- Durée conseillée : 10 à 40 s. Le style supporte très bien la boucle.
- **Version courte (8 à 12 s)** : deux plans de 5 s, un objet et une idée chacun : arrivée, pose sur ressort, légende (1,25 s au moins ; 2 s pour la dernière) ; ramener la tenue immobile à 0,8 s. Accroche : le premier objet se pose dès la première seconde. (Découpage tenu dans le rendu réel du 11/11/2026.)

## 6. Recette technique

**Moteur : HyperFrames, dessin 2D en canvas.** Pas de moteur 3D : l'isométrie est une simple projection, et le trait constant est plus net ainsi.

| | Canvas 2D (conseillé) | Three.js | Blender |
|---|---|---|---|
| Quand | toujours, par défaut | objet complexe qui doit tourner | objet du client fourni en modèle 3D |
| Comment | projection à la main, ordre du peintre | caméra orthographique + matériau blanc + contours d'arêtes | caméra orthographique + rendu de lignes |
| Ce qui change | contrôle total du trait ; formes à construire en dalles | lignes cachées gérées par la profondeur ; épaisseur de trait moins maîtrisée | très fidèle à la géométrie ; trait à régler longuement, rendu lent |

- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `iso.js` (projection, trait constant, dalles, boîtes, cylindres, piles de plaques, grilles), `faces.js` (dessin et texte inscrits dans une face), `ressort.js`, `accessoires.js`, `scenes.js`.
- **Techniques clés** :
  ```js
  // projection dimétrique 2:1 (u = taille d'une unité à l'écran)
  const iso = (x, y, z) => [ox + (x - y) * u, oy + (x + y) * u / 2 - z * 1.2247 * u];
  // trait constant : diviser l'épaisseur par l'échelle courante de la transformation
  ctx.lineWidth = 2.0 / echelleCourante();
  // ressort sans état (fonction du temps seul) : 0 -> 1 avec dépassement amorti. Oscillateur sous-amorti, forme fermée ;
  // w = raideur (pulsation, en rad/s), am = amortissement entre 0 et 1. Vérifié par le rendu réel du 11/11/2026.
  const ressort = (t, t0, w = 15, am = 0.5) => {
    const s = t - t0; if (s <= 0) return 0;
    const wd = w * Math.sqrt(1 - am * am);
    return 1 - Math.exp(-am * w * s) * (Math.cos(wd * s) + (am * w / wd) * Math.sin(wd * s));
  };
  // réglages employés : chute d'un objet (13 ; 0,5), couvercle qui s'ouvre (11 ; 0,55), touches en vague (20 ; 0,45), lame qui glisse (12 ; 0,6)
  // un aller-retour = différence de deux ressorts : ressort(t, 6.55, 12, 0.6) - ressort(t, 7.75, 12, 0.6)
  ```
  - Un solide = un rectangle arrondi extrudé : remplissage blanc de la silhouette, trait de silhouette, contour de la face avant, et **une seule** ligne d'extrusion au coin le plus proche (claire si le coin est arrondi, grise s'il est vif).
  - **Lignes cachées par l'ordre du peintre** : de l'arrière vers l'avant (x + y croissant ; z croissant dans une pile). Ce qui est posé sur un objet se dessine en dernier.
  - Ne trace jamais à l'intérieur d'une transformation inclinée (l'épaisseur s'inclinerait aussi) : projette les points, puis trace.
  - Une forme en L se construit avec deux dalles.
- **Pièges** : trait plus fin ou plus clair que 2 px gris moyen : il disparaît sur un téléphone après compression (vérifié : voir la note sous la palette) ; texte inscrit dans une face inclinée : il se lit mal s'il ne suit pas exactement les deux axes de la face (au rendu d'essai, le mot tapé sur l'écran penchait) ; un objet large frôle la limite droite (x 945) : garder 20 px de marge ; une ligne visible à travers un solide (ordre du peintre faux) ; arêtes hors des axes isométriques ; métamorphose qui se pince quand une petite forme devient longue et fine.

## 7. Son

- **Musique** : discrète et précise : nappe douce, pulsation légère, quelques notes de marimba ou de piano électrique ; ou presque rien.
- **Bruitages** (≈ 3 à 5 par 10 s, vrais enregistrements feutrés) : pose mate d'un objet sur une table, charnière qui s'ouvre, clics de clavier, glissière d'un tiroir ou d'une lame, bip doux d'un voyant.
- Le silence fait partie du style : entre deux mouvements, seulement un ton de pièce très bas.
- **Voix** : posée, explicative, phrases courtes. −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Chaque arête suit un axe isométrique (pente ±0,5 ou verticale), sauf une pièce qui tourne visiblement.
- [ ] Traits constants à tout niveau de zoom, même graisse partout (2,0 px à 1080) ; seule la couleur change.
- [ ] Les faces proches sont blanches et cachent ce qui est derrière : aucune ligne à travers un solide.
- [ ] Un seul accent sombre, et c'est le point d'attention.
- [ ] Le détail vient de la répétition ; les grandes faces restent vides.
- [ ] Dalles épaisses à coins arrondis ; les piles montrent leurs couches.
- [ ] Du blanc autour de l'objet ; légende bien en dessous ; rien ne touche le bord ni les zones d'interface.
- [ ] Chaque mouvement se pose sur un ressort puis l'image reste immobile ; ni ombre, ni dégradé, ni grain, ni couleur.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : fixe
- Couleurs max : 11
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Image d'exemple d'origine (540×960) : https://github.com/cth9191/animate/blob/main/plugins/animate/skills/animate/styles/isometric/sample.png · planche des 7 styles : https://github.com/cth9191/animate/blob/main/docs/styles.png (© 2026 cth9191, MIT).
- Pas de vidéo dans le dépôt d'origine (démo de 6 s à construire). Style « éprouvé sur sa démo seulement » selon son auteur.

## 10. Origine

- **cth9191/animate**, commit `7e5eb56` (0.4.0) : `plugins/animate/skills/animate/styles/isometric/STYLE.md`, `kit.js`, `demo/`, `demo-dark/`. Licence MIT, © 2026 cth9191.
- Voisins dans lemo-opuscar, non repris ici (autres catégories) : infographie isométrique et livre d'images isométrique.
- Adaptation Flot Web : traduction, composition 9:16 et 16:9, polices libres conseillées (la source utilise des polices système), tableau des moteurs (voies Three.js et Blender non testées), sections rythme et son, numéros du dictionnaire.
- Vérifié par un rendu réel le 11/11/2026 (HyperFrames 0.9.33) : image conforme ; le trait de 2 px reste lisible de peu à 360 px de large, les lignes intérieures trop pâles ont été foncées ; style immobile refusé par l'ancienne porte, d'où « Mouvement : calme ».
