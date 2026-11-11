# Expressionnisme (style Munch)

## 1. Identité

- **Nom** : Expressionnisme (style Munch, Europe du Nord vers 1893). Inspiration seulement : aucune toile recopiée, aucune figure célèbre reproduite.
- **Inspiration** : la peinture de l'angoisse de la fin du XIXᵉ siècle : un ciel en bandes rouge sang qui coulent, un paysage qui ondule, des figures simplifiées, une peinture mince en longues traînées.
- **Ce que c'est** : **le monde entier est déformé par l'émotion**. De longues touches fluides et **translucides, sans contour**, suivent un champ de directions qui se tord avec le temps ; le ciel est fait de bandes de couleurs chaudes qui ondulent ; et à la fin, **toute l'image** est décalée ligne par ligne par une onde : personnages, objets et décor ondulent ensemble.
- **Marche pour** : alerte, stress, burn-out, climat, bruit, sujet de société, « ce que tu ressens quand… », bande-annonce inquiète, Halloween.
- **Ne marche pas pour** : marque rassurante, produit, tutoriel, texte à lire, enfants.
- **À ne pas confondre** : `tourbillons-van-gogh` a des touches **courtes, épaisses, cernées** ; si ton mur ressemble à des chenilles, tu es tombé dedans (c'est le défaut connu de la source). Ici : touches **longues (200 à 300 px), larges, minces, sans contour**.

## 2. Palette, typographie, matières

| Rôle | Hex (source) |
|---|---|
| Ciel, 7 teintes en boucle | `#e2541c` `#f08a24` `#f4c03a` `#c8301e` `#e8743a` `#f6a63a` `#b82a1e` |
| Mur ou masse chaude (aplat sous les touches) | `#a8401e` → `#5a1a14` |
| Eau, lointain | bleus sombres et verts d'encre `#1f3a5a` `#2a5a52` |
| Ombre de visage | jaune-vert `rgba(120,150,70,.4)`, floue |
| Sombre général | brun-noir `#1c1414`, jamais noir pur |

- Sous les touches, un aplat de la **même famille** de couleur : ce qui se voit dans les interstices est de la couleur, pas du noir.
- **Typographie** : serif ancienne un peu irrégulière (**IM Fell English**, OFL). Pas d'écriture « bande dessinée » : elle casse le ton. Le texte peut onduler légèrement avec l'image.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place d'IM Fell English. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/im-fell-english` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : touches par zone, sous la forme *[nombre de pas, longueur du pas, largeur, opacité]* : ciel [32, 7, 10, 0,78] ; eau [26, 6, 9, 0,78] ; mur [42, 7, 13, 0,5] ; sol [32, 8, 12, 0,55]. ≈ 3 600 départs de touches sur une grille de 24 px légèrement décalée. Une touche **s'arrête en sortant de sa zone** : les frontières restent propres.

## 3. Composition 9:16

- **Grand ciel en bandes** sur la moitié haute, une **diagonale forte** (pont, route, barrière, quai) qui part d'un coin bas et file vers un point de fuite haut (vers x 560, y 760), et une figure au premier plan, bas du cadre, coupée à la taille ou aux épaules.
- Figure principale ≥ 1/3 de la hauteur, visage simplifié (ovale, yeux et bouche en taches). Deux petites silhouettes lointaines sur la diagonale renforcent le malaise.
- Bandes du ciel de ≈ 28 px de haut, ondulantes.
- **Marge de sécurité** : la déformation décale les lignes jusqu'à 13 px ; étire le dessin de 2 × cette marge sur les côtés, sinon des trous sombres apparaissent aux bords.
- Sous-titres : serif crème 48 à 54 px sur bande sombre, y ≈ 1400 à 1520. Rien d'important à droite de x = 945.

## 4. Ce qui bouge

- **Action principale** : la figure réagit (mains aux joues, bouche qui s'ouvre et se ferme, corps qui oscille de ±0,12 rad).
- **Boucle de fond 1** : **le ciel coule** : la bande de couleur d'un point dépend de `y + 22·sin(x·0,014 − 2,2·t)` ; les bandes glissent et se tordent.
- **Boucle de fond 2** : **tout ondule** : chaque ligne de l'image est décalée de `9·sin(y·0,012 + 4,2·t) + 4·sin(y·0,031 − 6·t)` px, chaque colonne de `6·sin(x·0,009 − 3,6·t)` px. C'est bien moins coûteux que de dessiner chaque objet tremblant.
- **Détails** : cheveux en onde qui descend, pieds de table et de chaise en lignes tremblées, un animal qui ouvre la bouche « contaminé » par le cri.
- **Autorisés** : `#013` mouvement liquide, `#130` texte en vague, `#032` travelling compensé (le fond se rapproche, le sujet garde sa taille), `#036` cadre penché, `#027` avancée lente, `#184` très gros plan, `#019` transition liquide.
- **Interdits** : contours nets, touches courtes cernées, `#001` rebond joyeux, `#022` balayage de lumière, image stable (rien ne doit être parfaitement immobile), ciel bleu.
- **Transition signature** : une bande du ciel rouge **descend** et recouvre l'image.

## 5. Rythme et montage

- Plans de 3 à 6 s ; une lente montée, puis une coupe sèche sur le cri ou le silence.
- L'onde globale ne s'arrête jamais ; tu peux augmenter son amplitude (×1,5) au pic.
- Un seul plan large tenu vaut mieux que plusieurs petits.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D ; ≈ 90 à 140 ms par image en 1080p.
- **Chaîne de rendu** :
  1. Aplats par zone (même famille de couleur que les touches).
  2. **Lignes de courant** : depuis chaque départ, avancer pas à pas le long du champ de directions de la zone, tracer un ruban translucide, s'arrêter à la frontière de la zone.
  3. Champ : ciel `0,55·sin(x·0,011 + y·0,018 − 2,4·t)` ; eau = tangente autour d'un centre ; mur = vertical ± 0,5 en sinus ; sol = vers le point de fuite.
  4. Figures et objets par-dessus (aplats simples, ombres de visage jaune-vert floues).
  5. **Déformation finale** de toute l'image, par bandes de 4 px de haut puis de large.
- **Techniques clés** :
  ```js
  for (let y = 0; y < H; y += 4) {                       // ondulation par lignes
    const dx = 9 * Math.sin(y * 0.012 + 4.2 * t) + 4 * Math.sin(y * 0.031 - 6 * t);
    out.drawImage(img, -M, y, W + 2 * M, 4, dx - M, y, W + 2 * M, 4);   // M = marge >= décalage maxi
  }
  const bande = Math.floor((y + 22 * Math.sin(x * 0.014 - 2.2 * t)) / 28) % 7;   // couleur du ciel
  ```
- **Pièges** :
  - Reprendre le contour sombre des touches « Van Gogh » : le mur devient une suite de chenilles. **Pas de contour**, touches 2 à 3 fois plus longues, opacité plus basse.
  - Après la déformation, les bords gauche et droit montrent des trous sombres : prévois la marge.
  - En mode trait, un bras levé est traversé par le trait du torse : redessine le bras proche par-dessus.

## 7. Son

- **Ambiance** : vent grave, eau lourde, ville lointaine étouffée ; une note tenue dissonante.
- **Musique** : cordes graves en glissando, harmonium ou orgue, une montée sans résolution ; ou presque rien.
- **Bruitages** (≈ 3 à 5 par 10 s) : un souffle qui enfle, bois qui grince (pont), battement de cœur, puis **un silence net** juste avant le pic. Le cri lui-même peut rester muet : c'est souvent plus fort.
- Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défaut connu de la source (deux étoiles) : **le mur lu comme du Van Gogh**. Erreurs : touches courtes ; contours ; image stable ; trous aux bords ; composition d'une toile célèbre recopiée.

- [ ] Touches longues (≥ 200 px), translucides, sans contour.
- [ ] Le ciel est en bandes chaudes qui ondulent et glissent.
- [ ] Toute l'image ondule (figures comprises) ; aucun trou aux bords.
- [ ] Les interstices montrent de la couleur, pas du noir.
- [ ] Une diagonale forte et une figure coupée au premier plan.
- [ ] Un silence avant le pic.
- [ ] Aucune toile ni figure célèbre reconnaissable.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 12
- Bleu-violet : interdit
- Texte vivant : oui
- Taille mini du texte : 48

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt. Planche commune `assets/全风格总览.jpg` : composition empruntée, à ne pas utiliser comme vitrine. Film complet : Releases de https://github.com/alchaincyf/huashu-art-motion. Image fixe possible avec le moteur d'origine (`render.py --solo 19_munch --stills`, non exécuté ici).
- À produire : notre propre aperçu 9:16.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/19_munch.md` (deux étoiles), `scripts/engine/scenes/19_munch.js`. Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : carte traduite et généralisée ; la carte reproduisait la figure d'un tableau célèbre : non repris, la fiche demande une figure originale. Section 9:16, son.
