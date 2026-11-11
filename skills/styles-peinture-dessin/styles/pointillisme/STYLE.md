# Pointillisme

## 1. Identité

- **Nom** : Pointillisme (mélange optique, néo-impressionnisme).
- **Inspiration** : la peinture par points des années 1880 : des pastilles de couleurs pures posées côte à côte, que l'œil mélange à distance ; un grand calme, des silhouettes de profil, un bord peint autour de l'image.
- **Ce que c'est** : un moteur de rendu, plus qu'un dessin. L'image à plat est convertie en **≈ 24 000 points de même taille sur une grille hexagonale** (en 1080p), pris dans **21 couleurs pures**. Chaque teinte de l'image est obtenue en **alternant deux couleurs** de la palette dans la bonne proportion. Des points de couleur complémentaire et un liseré de lumière au bord des formes font vibrer l'ensemble.
- **Marche pour** : un moment suspendu, un dimanche, un parc, une foule tranquille, un produit de saison, une idée de « chaque petit geste compte » (les points font l'image).
- **Ne marche pas pour** : action rapide, petit texte, visages expressifs, sujet nerveux. Le style est **immobile par nature** : c'est son défaut connu.
- **À ne pas confondre** : `impressionnisme` a des touches allongées ; `pop-trame` (catégorie « Papier et impression ») a des trames d'imprimerie régulières à une seule couleur par zone.

## 2. Palette, typographie, matières

Les 21 couleurs de la source :

- **14 saturées** : `#1a2058` `#2a3a9a` `#3f6fd0` `#6aaee6` `#1f6a52` `#2f9a5a` `#a8c83a` `#f2cf3a` `#f08a2a` `#e0432a` `#c0306a` `#7a4aa8` `#f8f4e8` `#e8b48a`
- **7 claires** (« mêlées de blanc ») : `#f6e49a` `#f6c48a` `#cfe08a` `#b0cff0` `#f2b8c8` `#c99a4a` `#9a7ac8`

- Sans les teintes claires, un mur lumineux se décompose en blanc + chair + points bleus épars : on dirait de la neige.
- **Bord peint** : une bande bleu profond de ≈ 28 px tout autour, passée elle aussi dans le moteur (elle reçoit donc des points orangés complémentaires).
- **Typographie** : serif classique (**Cormorant Garamond** ou **EB Garamond**, OFL) sur un cartouche uni ; le texte ne passe jamais dans le moteur de points.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de Cormorant Garamond ; EB Garamond : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/cormorant-garamond` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : points ronds de rayon 4,5 px, pas de 10 px, rangées espacées de 8,66 px, décalage fixe de ±1,2 px par point. Sous les points, l'esquisse légèrement floutée, désaturée et éclaircie sert de couche de fond : elle se voit dans les interstices.

## 3. Composition 9:16

- Composition **frontale et calme** : grandes masses simples, silhouettes de profil ou de dos, lumière d'un seul côté, ombres longues.
- Découpe en trois bandes : ciel ou feuillage (haut), eau ou pelouse éclairée (milieu), ombre au premier plan (bas, y > 1300), ce qui donne aussi une zone sombre pour les sous-titres.
- Formes **grandes** : à 10 px de pas, un détail de moins de 40 px disparaît. Sujet ≥ 1/3 de la hauteur ; pas de visage détaillé.
- Garde le bord peint : 28 px, à l'intérieur de la zone sûre (il peut passer sous l'interface).
- Sous-titres : cartouche uni crème ou bleu profond, serif 48 à 54 px, y ≈ 1400 à 1520. Rien d'important à droite de x = 945.

## 4. Ce qui bouge

- **Action principale** : un seul mouvement lent et lisible dans l'image à plat : un voilier qui glisse (≈ 40 px/s), un promeneur, un papillon qui tourne (`sin(2,6·t)·120`), une ombre qui s'allonge.
- **Boucle de fond 1** : **la lumière tremble entre les points** : 6 fois par seconde, ≈ 7 % des points échangent leur couleur avec leur couleur partenaire. Petite surface et faible amplitude seulement : des points isolés, tirés au hasard, jamais une zone entière qui change de couleur en même temps (ce serait un clignotement).
- **Boucle de fond 2** : sur l'eau ou une surface brillante, les points sont retirés au hasard 6 fois par seconde (clapotis de lumière).
- **Autorisés** : `#175` plan fixe (le cas normal), `#027` avancée très lente, `#126` trajet d'un petit objet, `#096` flottement, `#141` pixellisation comme idée de transition (ici : cristallisation en points).
- **Interdits** : caméra rapide, `#043` panoramique filé, `#024` secousse, `#011` écrasement et étirement, grille de points qui se déplace avec les objets (la grille est **fixe à l'écran**, seules les couleurs changent).
- **Transition signature** : l'image précédente **cristallise en points** (le pas grossit puis revient).

## 5. Rythme et montage

- Plans fixes de 5 à 8 s. C'est un style de pause : un ou deux plans dans une vidéo.
- Avec 4 échanges par seconde et 3 % de points, un relecteur a jugé l'image « quasiment figée » ; avec **6 par seconde et 7 %**, elle vit. Ne descends pas en dessous.
- Ajoute toujours un vrai mouvement dans l'image à plat (bateau, fumée, personnage) : le tremblement des points seul ne passe pas la porte anti-diaporama.
- **Version courte (8 à 12 s)** : un seul plan fixe de 8 s ; une figure bouge avant 3 s.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D. ≈ 100 ms par image en 1080p.
- **Chaîne de rendu** :
  1. Image à plat complète, sujet compris.
  2. Fond : cette image floutée de 4 px, un peu désaturée et éclaircie.
  3. Grille hexagonale fixe ; pour chaque point, lire la couleur cible (avec une **petite variation aléatoire fixe**, ≈ ±20 sur 255), choisir la **paire** de couleurs de la palette dont le mélange est le plus proche, puis tirer laquelle des deux poser selon la proportion.
  4. 8 % des points remplacés par leur complémentaire (bleu ↔ orange, vert ↔ rouge-violet, jaune ↔ violet).
  5. Liseré de lumière : si le point situé 14 px en bas à droite est nettement plus sombre, 45 % de chances de poser un point blanc côté clair et bleu profond côté sombre.
  6. Regrouper les points par couleur et remplir chaque couleur en une fois (21 remplissages).
- **Techniques clés** :
  ```js
  // paire (Pi, Pj) : projeter la cible sur le segment, proportion w bornée à [0,2 ; 0,8]
  const cout = dist2(cible, mix(Pj, Pi, w)) + 0.004 * dist2(Pi, Pj);  // pénalise les paires trop éloignées
  const couleur = hash(i, j) < w ? Pi : Pj;                            // tirage fixe par point
  cache.set(quantifier15bits(cible), [Pi, Pj, w]);                     // mémoriser par couleur
  ```
- **Pièges** :
  - Préférer une seule couleur pure découpe un dégradé en bandes verticales : il faut la **variation aléatoire de la cible** avant le choix de la paire.
  - Sans pénalité de distance, le moteur mélange du noir et du blanc pour faire du gris.
  - Palette sans teintes claires = neige.
  - Grille trop régulière : garde le petit décalage fixe par point.

## 7. Son

- **Ambiance** : parc, rivière lente, voix lointaines indistinctes, oiseaux.
- **Musique** : notes détachées (pizzicato, harpe, célesta, piano staccato) : la musique aussi se fait par points.
- **Bruitages** (≈ 3 à 5 par 10 s) : petits tintements groupés à la cristallisation, sirène lointaine d'un bateau, pas sur le gravier.
- Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défauts connus de la source (deux étoiles) : **statique**, grille trop régulière. Erreurs : bandes verticales dans les dégradés ; neige sur les zones claires ; détails trop petits ; aucun mouvement réel.

- [ ] Points de même taille sur une grille fixe à l'écran.
- [ ] Un dégradé agrandi montre deux couleurs qui alternent, sans bande verticale.
- [ ] Des points complémentaires sont visibles dans chaque grande zone.
- [ ] Liseré clair et sombre au bord des formes éclairées.
- [ ] Au moins un vrai mouvement dans l'image, en plus du tremblement (6 par seconde, 7 %).
- [ ] Aucune forme utile de moins de 40 px.
- [ ] Bord peint présent ; texte hors du moteur de points.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : fixe
- Couleurs max : 21
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 48

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt. Planche commune `assets/全风格总览.jpg` : composition empruntée, à ne pas utiliser comme vitrine. Film complet : Releases de https://github.com/alchaincyf/huashu-art-motion. Image fixe possible avec le moteur d'origine (`render.py --solo 29_seurat --stills`, non exécuté ici).
- À produire : notre propre aperçu 9:16.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/29_seurat.md` (deux étoiles), `scripts/engine/scenes/29_seurat.js`. Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : carte traduite et généralisée, section 9:16, numéros du dictionnaire de mouvements, son.
