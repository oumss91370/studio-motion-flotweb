# Estampe japonaise

## 1. Identité

- **Nom** : Estampe japonaise (ukiyo-e, gravure sur bois de l'époque d'Edo).
- **Inspiration** : les grandes séries de paysages du XIXᵉ siècle (un sujet constant placé différemment à chaque vue ; cadrages audacieux ; petites figures, lignes de pluie, premier plan extrême) et l'animation japonaise qui garde la texture de l'estampe en mouvement. **On ne reproduit jamais une estampe célèbre** (ni la grande vague, ni la montagne rouge, ni l'averse sur le pont), ni un personnage, ni une composition.
- **Ce que c'est** : **chaque plan est une estampe complète** : une feuille de papier japonais, un double filet d'encre, des aplats de couleur imprimés chacun par son bloc, un trait noir par-dessus, un cartouche de titre vertical et un sceau rouge. **Le monde est plat exprès** : la profondeur vient de bandes horizontales empilées, de bandes de brume et de cadrages hardis, jamais de la perspective, de l'éclairage ou de l'ombrage.
- **Ce qui fait « imprimé » et non « vectoriel »** : le papier toujours visible (fibres longues, bords vieillis) ; chaque couleur **légèrement hors repérage** (1,5 à 2,5 px) ; dans les grands aplats, **veines du bois** et traces de frottoir ; **dégradés essuyés à la main** dans les ciels et l'eau.
- **Marche pour** : voyage, étapes d'un parcours, saisons, un produit dans plusieurs lieux, tourisme, restauration japonaise, thé, « une série de vues ».
- **Ne marche pas pour** : interface, visages expressifs, action continue, sujet technique.
- **À ne pas confondre** : pas du lavis (la couleur est imprimée, rien ne diffuse) ; pas du cellulo d'anime (aucune ombre sur les formes) ; pas une affiche sérigraphiée (ici il y a un trait).

## 2. Palette, typographie, matières

- **Un jeu de pigments, pas une roue chromatique** : 6 à 9 teintes plates, chacune son bloc, sur le fond papier. Aucun dégradé sauf le dégradé essuyé ; aucune ombre sur les formes.
- **Trait à l'encre** par-dessus tout ; **le papier est le blanc** (écume, neige, brume, ciel vide : papier non imprimé).
- **Une famille dominante** porte ciel et eau (le bleu de Prusse des estampes du XIXᵉ) ; **le rouge est rare** : sceaux, un soleil, un vêtement.

| Jeu « paysage indigo » (exemple) | Hex |
|---|---|
| Papier | `#efe4cc` |
| Bleu de Prusse, bleu pâle | `#1f4e79`, `#a9c4d8` |
| Rouge de carthame (sceaux, soleil) | `#c8402f` |
| Ocre, vert, vert sombre | `#d6a85a`, `#7c9a6a`, `#3f5f4a` |
| Encre | `#1c1a18` |

  Autres jeux : *intérieur* (rose pâle, mauve, gris-vert, noir de laque, fond gris nacré) ; *automne* (kaki, ocre, gris-vert, brun profond, un bleu).
- Lointain pâle et peu contrasté ; proche saturé avec un trait sombre.
- **Typographie** : serif à l'esprit de pinceau pour le français (**Shippori Mincho**, OFL, ou **Cormorant Garamond**), en encre, dans des cartouches. Titres : dans un cartouche vertical à double filet. N'écris des caractères japonais que si le client fournit le texte ; sinon, un sceau abstrait.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de Shippori Mincho et de Cormorant Garamond. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/shippori-mincho`, `@fontsource/cormorant-garamond` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : veines du bois = lignes de niveau d'un champ de bruit déformé (plus fortes dans le ciel et l'eau) ; frottoir = arcs circulaires flous et stries en zigzag ; mouchetis de manques d'encre (opacité ≈ 0,3) ; fibres claires par-dessus la feuille finie (≈ 0,09). Trait : 3 à 4 px en 1080 de large ; les grands contours sont des traits remplis de largeur variable (±20 à 35 %), effilés aux deux bouts. Motifs du médium : brume en longues bandes plates arrondies ; pins à coussins d'aiguilles aplatis ; champs en couches parallèles et **obliques, jamais convergentes** ; pluie en deux jeux de fines lignes droites ; eau en bandes de bleus.

## 3. Composition 9:16

- **La feuille est le cadre**, et l'estampe verticale est un format historique. Feuille de ≈ 1000 × 1640 centrée (x 40 à 1040, y 160 à 1800) ; double filet (épais + fin) ; marge de papier autour. La feuille dépasse de la zone utile à droite et en bas : c'est du décor. **Tout ce qui se lit** (cartouches, sceau, sous-titre, figure principale) reste dans x 60 à 945, y 160 à 1560.
- Empile **4 à 6 bandes horizontales** : ciel en dégradé essuyé (haut), lointain, brume, plan moyen, sol, premier plan. Un **élément de premier plan extrême** qui traverse le cadre (branche, poteau, lanterne) est natif.
- Figures **petites** dans le paysage (120 à 200 px), plates, silhouette claire, visage en quelques traits.
- **Cartouche de vue** : vertical, en haut à **gauche** (x 80 à 190, y 220 à 620), sceau à côté ; c'est le « point final » de chaque vue.
- **Sous-titre = cartouche horizontal** : bande crème à double filet, petit sceau rouge à gauche, texte encre 44 à 50 px, centré vers y ≈ 1400 à 1520, entre x 80 et x 925 ; il couvre ≈ 150 px : garde lignes de sol et figures au-dessus. Il « s'imprime » et s'efface. Tenue ≥ max(1,8 s ; réplique + 0,6 s).
- Plusieurs feuilles montées sur un long **rouleau** (papier plus foncé) : la caméra glisse de l'une à l'autre. En vertical, monte-les en colonne et fais défiler de bas en haut, ou garde le glissement latéral court.

## 4. Ce qui bouge

- **Action principale** : **l'impression bloc par bloc** : le trait d'abord, puis chaque couleur arrive en ≈ 0,3 s par un balayage diagonal au bord irrégulier, en glissant de 5 à 6 px jusqu'à son repérage.
- **Boucle de fond 1** : une ou deux petites actions par vue : vapeur, pluie, lanterne, feuille qui tombe, oiseau. **La plus grande partie du cadre ne bouge pas.**
- **Boucle de fond 2** : l'eau en bandes qui glissent, la brume qui dérive.
- **Gestes natifs** : la série de vues (un même sujet, placé ailleurs à chaque fois) ; le rouleau ; le papier est le blanc (une neige qui efface tout) ; **le cadre est un objet** (quelque chose d'assez grand sort du filet et déborde dans la marge) ; les tirages alternés (même trait, autres couleurs : jour → nuit) ; le triptyque.
- **Autorisés** : `#175` plan fixe sur une feuille, `#137` poussée latérale (glissement du rouleau), `#027` avancée très lente vers une fenêtre ou un éventail, `#028` recul d'une feuille vers plusieurs, `#184` plongée dans la texture, `#005` révélation par masque (impression), `#128` saccadé, `#046` coupe sèche vers une feuille vide (un souffle retenu).
- **Interdits** : `#044` fondu enchaîné, `#139`/`#021` retournements 3D, rotation 3D dans une estampe, perspective, ombres sur les formes, dégradés autres qu'essuyés, `#022` balayage de lumière.

## 5. Rythme et montage

- **Trois cadences** : figures et nature à **10 dessins par seconde** ; pluie et eau rapide à **15** (à 30 i/s : une image sur trois et une sur deux ; la source, à 24 i/s, donnait 8 et 12, qui deviennent irréguliers à 30) ; caméra **fluide** à chaque image (une caméra saccadée tremble).
- Plans de 4 à 7 s. Un geste natif a besoin d'**environ une seconde tenue** pour être lu.
- Transitions : glissement du rouleau, impression, lavage jusqu'au papier, coupe vers le vide. Un sceau **se tamponne** (échelle 1,35 → 1 en 0,2 s). Un cartouche tombe (fondu + court glissement).
- Le silence complet est un outil (queues de réverbération coupées).
- **Version courte (8 à 12 s)** : deux vues de 4 à 5 s (ou une vue et son retirage de nuit) : impression bloc par bloc en 1,5 s, un geste natif tenu 1 s, le sceau ; couper le glissement de rouleau entre les vues et le cartouche de sous-titre. Accroche avant 3 s : le premier bloc de couleur s'imprime dès la première seconde (ne pas ouvrir sur 3 s de trait seul). (Découpage tenu dans le rendu réel du 11/11/2026.)

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `impression.js` (papier, veines, frottoir, mouchetis, blocs, dégradé essuyé, traits gravés, masques d'impression, cartouche, sceaux : le cœur réutilisable), `nature.js`, `eau.js`, `figure.js`, `vues.js` (chaque estampe en blocs mis en cache + ce qui se peint à chaque image), `main.js` (caméra, rouleau, impression, sous-titres).
- **Extrait vérifié par un rendu réel** (11/11/2026) : le cœur de l'impression tient en trois fonctions, écrites pour le film d'essai (un seul fichier d'environ 230 lignes, sans Blender). Chaque bloc de couleur est un canvas hors écran dessiné une fois ; `poser` le révèle par un masque diagonal au bord irrégulier pendant qu'il glisse jusqu'à son repérage.
  ```js
  const DECAL = { trait: [0, 0], bleus: [2, -1.5], verts: [-1.5, 2], ocres: [1.5, 1.5], rouges: [1.5, 2] };
  const sort = x => 1 - Math.pow(1 - Math.max(0, Math.min(1, x)), 3);
  function masque(g, p, graine) {                    // p de 0 à 1 : front diagonal qui traverse la feuille
    const d = -300 + (W + H * 0.5 + 600) * p;
    g.beginPath(); g.moveTo(-50, -50); g.lineTo(d, -50);
    for (let y = 0; y <= H; y += 40) g.lineTo(d - y * 0.5 + 46 * (bruit(y / 55, graine) - 0.5), y);   // bord irrégulier
    g.lineTo(-50, H + 50); g.closePath(); g.clip();
  }
  function poser(g, bloc, nom, p, graine, dessin) {  // p = (t - t0) / 0.35 ; `dessin` : ce qui se repeint à chaque image
    if (p <= 0) return; const d = DECAL[nom], k = 1 - sort(p);
    g.save(); if (p < 1) masque(g, p, graine);
    g.translate(d[0] + 6 * k, d[1] + 5 * k);         // glisse de 6 px jusqu'à son repérage
    if (bloc) g.drawImage(bloc, 0, 0); if (dessin) dessin(g); g.restore();
  }
  function texturer(c, graine, fort) {               // sur chaque bloc, une seule fois : veines, puis manques d'encre
    const g = c.getContext("2d"), r = alea(graine);
    g.globalCompositeOperation = "source-atop"; g.strokeStyle = `rgba(20,16,10,${fort ? 0.13 : 0.07})`; g.lineWidth = 2;
    for (let i = 0; i < 74; i++) { g.beginPath();
      for (let x = 0; x <= W; x += 30) { const y = i * 26 + 34 * bruit(x / 260 + i * 0.07, graine) + 9 * bruit(x / 60, graine + i); x ? g.lineTo(x, y) : g.moveTo(x, y); }
      g.stroke(); }
    g.globalCompositeOperation = "destination-out"; g.fillStyle = "rgba(0,0,0,0.3)";
    for (let i = 0; i < 520; i++) { g.beginPath(); g.arc(r() * W, r() * H, 0.8 + r() * 1.8, 0, 6.2832); g.fill(); }
    g.globalCompositeOperation = "source-over";
  }
  // une vue : papier, blocs dans l'ordre (un toutes les 0,5 s), trait, figures, fibres, filet
  poser(g, JOUR.bleus, "bleus", (t - 0.35) / 0.35, 1); poser(g, JOUR.verts, "verts", (t - 0.85) / 0.35, 2);
  ```
  `alea(graine)` est un tirage à graine, `bruit(x, graine)` un bruit lissé à une dimension : à écrire aussi (dix lignes). Mesuré sur ce film : part d'images en mouvement 14,4 %, donc le style passe la porte de livraison sans rien ajouter.
- **Techniques clés** :
  ```js
  // un canvas hors écran par bloc de couleur, mis en cache ; pose avec un décalage fixe
  const DECAL = { trait: [0, 0], bleus: [2, -1.5], verts: [-1.5, 2], rouges: [1.5, 2] };
  // texture de chaque bloc : veines ("source-atop"), puis frottoir et mouchetis ("destination-out")
  // dégradé essuyé : calculé pixel par pixel, bord haut qui ondule de ±20 à 30 px par colonne
  const haut = y0 + 25 * bruitBasseFrequence(x);
  const tq = Math.floor(t * 10) / 10;        // figures et nature
  ```
- **Pièges** :
  - **Cartouche ou sceau en HTML invisible** (constaté au rendu du 11/11/2026) : un enfant animé par GSAP doit avoir **sa propre taille** (largeur et hauteur écrites sur lui), sinon ses enfants en `inset: 0` tombent à 0 px. Donne une taille explicite à chaque élément animé, pas seulement à son parent `.clip` (règle du contrat de rendu, skill `rendu`).
  - Dégradé fait de bandes rectangulaires : raccords verticaux visibles. Pixel par pixel.
  - Trop de mouchetis ou de fibres : papier de verre ou film rayé.
  - Une grille en perspective pour des champs fait « numérique » : couches parallèles obliques.
  - Pins en demi-disques = parasols : coussins plats avec des éventails d'aiguilles.
  - Un bord d'impression en bruit pur ressemble à de la moisissure : balayage diagonal.
  - Pour sortir de l'estampe, il faut échapper **à la fois** à la découpe de la feuille et à celle du filet.
  - Un sceau posé en multiplication disparaît sur fond sombre.

## 7. Son

- **Instruments japonais, pas piano et nappes** : luth à trois cordes (avec son léger grésillement), flûte de bambou soufflée, cithare, grand tambour et petit tambour, claquoirs de bois, clochette. Longs sons soufflés qui glissent vers la note ; le luth peut tenir une pulsation.
- **Techniques** : silence absolu ; une seule note laissée à résonner ; claquoirs qui accélèrent ; battement de tambour qui se resserre en roulement ; glissando de cithare pour un changement de saison.
- **Bruitages** (≈ 5 par 10 s) : le papier (frottoir qui tourne, glissement du rouleau, sceau = choc sourd + décollement collant), le bois (bloc qu'on pose, pas creux), carillon de verre, eau, oiseaux et insectes de la saison.
- **Voix** : calme, peu de phrases courtes, comme un poème à côté de l'image. Musique baissée d'environ 8 dB sous la voix. Mix −14 LUFS, **aucun grain ajouté**.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : aplats vectoriels propres ; perspective ; ombres ; trop de teintes ; copie d'une estampe connue ; caméra saccadée ; faux caractères.

- [ ] Filet double, marge de papier, cartouche et sceau présents sur chaque vue.
- [ ] Chaque couleur est décalée du trait de 1,5 à 2,5 px.
- [ ] Les grands aplats montrent des veines de bois ; le ciel a un dégradé essuyé irrégulier.
- [ ] Le blanc est du papier non imprimé.
- [ ] 6 à 9 teintes ; rouge rare. (Le contrôle du storyboard accepte ce nombre : il lit « Couleurs max » ci-dessous.)
- [ ] Aucune perspective, aucune ombre sur les formes.
- [ ] Figures à 10 dessins par seconde, caméra fluide.
- [ ] Aucune estampe célèbre reconnaissable ; pas de caractères inventés.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 9
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 44

## 9. Aperçu

- Film de démo d'origine *Toward the Mountain* (44 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/ukiyoe.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/ukiyoe.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/ukiyoe.jpg · galerie : https://lemomo-ai.github.io/lemo-opuscar/#east-asian-traditions
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre les vues ni l'histoire.

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/ukiyoe/STYLE.md`, `DEMO.md`, `demo/print.js`, `nature.js`, `wave.js`, `traveler.js`, `views.js`, `main.js`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0.
- huashu-art-motion ne contient pas de carte d'estampe (seule sa bande-son de démo évoque le genre) : fiche issue d'une seule source.
- Adaptation Flot Web : traduction, mise en page verticale, valeurs hex d'exemple proposées par Flot Web (la source nomme les pigments), numéros du dictionnaire de mouvements.
- Vérifié par un rendu réel le 11/11/2026 (HyperFrames 0.9.33) : ça marche avec corrections, en canvas 2D sans Blender ; porte de livraison verte après mastering du son (mouvement 14,4 %, −14,8 LUFS).
