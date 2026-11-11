# Clair-obscur (style Rembrandt)

## 1. Identité

- **Nom** : Clair-obscur (style Rembrandt, XVIIᵉ siècle). Inspiration seulement.
- **Inspiration** : la peinture hollandaise à la bougie et à la fenêtre : une pièce presque noire, une source de lumière, un visage qui en sort, des rehauts de pâte épaisse sur ce qui brille.
- **Ce que c'est** : **la lumière fait tout**. On peint la scène comme si elle était entièrement éclairée, puis on la **multiplie par une carte de lumière** presque noire où l'on a ajouté quelques flaques : la fenêtre, un faisceau, le visage, la poitrine, la table, la bougie. Les bords côté ombre se perdent dans le fond. Vernis brun doré et craquelures par-dessus.
- **Marche pour** : portrait, confidence, mystère, histoire, whisky, horlogerie, cuir, livre, « le secret de… », révélation d'un objet.
- **Ne marche pas pour** : sujet joyeux ou enfantin, explication, texte abondant, écran de téléphone en plein soleil sans vérification (image très sombre).
- **Maturité** : c'est la carte la **moins aboutie** de la source (une étoile : personnages plats). Cette fiche garde la méthode de lumière, qui est solide, et impose de donner du volume au sujet. Si le sujet est un visage ou un objet en volume, **passe par Blender** (voir la recette).
- **À ne pas confondre** : `sfumato` est doux, brumeux, sans flaque de lumière dure ; `lumiere-diner-americain` a des pans de soleil à bord net et des couleurs franches.

## 2. Palette, typographie, matières

| Rôle | Valeur (source) |
|---|---|
| Lumière ambiante (fond de la carte de lumière) | `rgb(30,21,13)`, soit ≈ 13 % |
| Fond brun en grandes touches | bruns `#43321f` à `#22180e` |
| Lumière de fenêtre / de bougie | blanc chaud `#f6e6c4` / orangé `#f0a84a` |
| Chairs éclairées | `#f0cfa8` ; rehauts : crème `#fbf0d8` |
| Vernis final | `rgba(200,140,60,0.35)` en lumière douce |

- Très peu de teintes : bruns, ocres, un rouge sourd ou un vert profond pour un tissu, et les blancs chauds des rehauts.
- **Typographie** : serif ancienne (**IM Fell English** ou **EB Garamond**, OFL), crème, petite et rare ; dans l'ombre, jamais dans la flaque de lumière.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place d'IM Fell English ; EB Garamond : déjà fournie. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/im-fell-english` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** :
  - *Fond* : grandes touches brunes (≈ 54 px × 16 px), puis flou de 2,2 px mêlé à 75 % : un fond « frotté ».
  - *Bords perdus* : le sujet est dessiné une fois flou (2,4 px) puis recouvert de sa version nette à 62 % : le côté ombre se fond, les traits restent lisibles.
  - *Pâte épaisse* (soies de pinceau) : une touche = une douzaine de fins poils parallèles, chacun de luminosité légèrement différente (±17), aux bouts raccourcis au hasard, avec une ombre portée dessous (opacité 0,28) et quelques points clairs dessus. **Seulement sur ce qui prend la lumière** : cheveux clairs, col, porcelaine, perle, métal.
  - *Voile final* : craquelures (≈ 0,28), grain léger (densité 0,05, opacité 0,12), vignettage 0,75, vernis doré.

## 3. Composition 9:16

- Le vertical convient au portrait : **fenêtre ou source en haut à gauche** (hors cadre ou vers x 150, y 300), faisceau en diagonale, visage vers x 520, y 620, mains et objet vers y 1100 à 1300.
- **70 à 80 % du cadre reste dans l'ombre.** La lumière dessine un chemin : source → visage → objet.
- **Lumière de séparation** : éclaire faiblement le mur derrière le côté sombre du sujet (flaque large, opacité ≈ 0,35), sinon il se confond avec le fond.
- Sous-titres : crème 46 à 52 px, dans l'ombre du bas, y ≈ 1400 à 1520, avec une très légère ombre portée. Vérifie la lisibilité à faible luminosité d'écran.
- Visage ≥ 280 px de haut ; rien d'important à droite de x = 945.

## 4. Ce qui bouge

- **Action principale** : un geste lent dans la lumière (lever une tasse, ouvrir une boîte, tourner la tête vers la fenêtre).
- **Boucle de fond 1** : **la flamme** : elle penche et change de hauteur ; sa flaque de lumière respire (`0,5·bruit(2,2·t) + 0,25·bruit(6,5·t)`), le centre des flaques dérive de ±14 px.
- **Boucle de fond 2** : **un nuage passe** : la lumière de fenêtre baisse jusqu'à −35 % puis revient ; ≈ 70 poussières flottent **uniquement dans le faisceau** ; vapeur.
- **Autorisés** : `#101` éclairage à 45° (triangle de lumière sur la joue), `#114` image en tons sombres, `#027` avancée très lente, `#033` bascule de mise au point, `#175` plan fixe, `#112` vignettage, `#188` fermeture à l'iris.
- **Interdits** : lumière qui clignote vite, `#022` balayage de lumière, `#024` secousse, couleurs vives, éclairage uniforme, rehauts partout.
- **Transition signature** : un iris de vieux film qui se ferme sur la flamme et se rouvre.

## 5. Rythme et montage

- Très lent : plans de 6 à 10 s. Une seule variation de lumière par plan (le nuage, ou la bougie qu'on approche).
- Coupes rares, sur un silence ; iris pour changer de lieu.
- Le mouvement visible ne couvre qu'environ 8 % de l'image : ajoute un geste franc du sujet pour passer la porte anti-diaporama.
- **Version courte (8 à 12 s)** : un seul plan : la bougie approche ou le nuage passe (la lumière commence à bouger avant 3 s), un regard, le texte dans l'ombre tenu 2 s.

## 6. Recette technique

- **Moteur** :
  - *Sujet en volume (visage, main, objet, bouteille)* : **Blender** par le connecteur MCP. Une pièce simple, une lampe de zone à la fenêtre, une lampe ponctuelle chaude pour la bougie, presque pas de lumière d'ambiance, un peu de volume d'air pour le faisceau. Rends en 1080×1920, puis passe l'image dans HyperFrames pour la toile, les craquelures, le vernis et le texte. C'est la voie qui corrige le défaut « personnages plats ».
  - *Sujet plat ou silhouette* : HyperFrames seul, canvas 2D, ≈ 47 ms par image.
- **Chaîne HyperFrames** : esquisse « tout éclairé » → fond en grandes touches frottées → objets sur leur propre calque, petites touches → sujet (aplat + dégradés de volume + petites touches) → bords perdus → **carte de lumière en multiplication** → vitre éclaircie + ombre de nuage → rehauts de pâte → flamme, poussières, vapeur → craquelures, grain, vignettage, vernis.
- **Techniques clés** :
  ```js
  // carte de lumière : fond presque noir + flaques additives, puis multiplication de toute l'image
  L.fillStyle = "rgb(30,21,13)"; L.fillRect(0, 0, W, H);
  L.globalCompositeOperation = "lighter";
  flaque(L, visage, 250, 0.95); flaque(L, buste, 230, 0.55); flaque(L, table, 280, 0.60);
  flaque(L, bougie, 190 + 40 * fl, 0.6 + 0.4 * fl); flaque(L, murDerriere, 300, 0.35);
  ctx.globalCompositeOperation = "multiply"; ctx.drawImage(L.canvas, 0, 0);
  ```
  - Le faisceau est un coin flouté de 40 px, mis en cache.
- **Pièges** :
  - Rehaut fait de trois traits propres (ombre, touche, arête claire) = autocollant blanc ou pansement : il faut des **soies** irrégulières.
  - Recopier une zone de l'image d'origine pour « sauver » un objet ramène aussi le fond non peint, en rectangle : les objets vont sur leur propre calque, après les touches.
  - Grain trop fort (densité 0,12) = visage sale : 0,05.
  - Ordre de dessin des mains et de l'objet tenu : main, objet, pouce.

## 7. Son

- **Ambiance** : pièce close, bois qui craque, feu ou mèche qui grésille, vent dehors.
- **Musique** : violoncelle ou viole seule, luth, clavecin rare ; ou silence presque complet.
- **Bruitages** (≈ 3 à 5 par 10 s) : allumette, porcelaine posée, étoffe, page tournée, souffle sur la flamme.
- Mix −14 LUFS ; garde de la dynamique (les silences comptent).
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défaut connu de la source (une étoile) : **personnages plats**. Erreurs : image trop éclairée ; sujet collé au fond ; rehauts partout ; texte dans la flaque de lumière.

- [ ] 70 % du cadre au moins est sous 20 % de luminosité.
- [ ] Le sujet a un vrai volume (dégradés ou rendu Blender), pas un aplat éclairé.
- [ ] Le triangle de lumière est visible sur la joue côté ombre (`#101`).
- [ ] Le côté ombre du sujet se fond ; une lumière de séparation le détache du mur.
- [ ] Rehauts de pâte seulement sur 3 à 6 points brillants.
- [ ] La flamme et le nuage font varier la lumière ; poussières dans le faisceau seulement.
- [ ] Sous-titres lisibles à faible luminosité d'écran.
- [ ] Un geste franc du sujet dans chaque plan.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Pas d'aperçu isolé dans le dépôt. Planche commune `assets/全风格总览.jpg` : composition empruntée, à ne pas utiliser comme vitrine. Film complet : Releases de https://github.com/alchaincyf/huashu-art-motion. Image fixe possible avec le moteur d'origine (`render.py --solo 32_rembrandt --stills`, non exécuté ici).
- À produire : notre propre aperçu 9:16, par la voie Blender.

## 10. Origine

- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/32_rembrandt.md` (une étoile : « le plus à refaire »), `scripts/engine/scenes/32_rembrandt.js`. Licence MIT, © 花叔 Huashu.
- Repère d'éclairage : entrée `#101` du dictionnaire motion-prompt (© 2026 Shohei Ohtaki, MIT), via le skill `principes-mouvement`.
- Adaptation Flot Web : carte traduite et généralisée, voie Blender ajoutée pour le volume, section 9:16, son.
