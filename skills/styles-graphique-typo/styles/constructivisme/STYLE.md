# Constructivisme

## 1. Identité

- **Nom** : Constructivisme (affiche d'avant-garde des années 1920).
- **Inspiration** : les affiches constructivistes des années 1920 : photomontage, coin rouge qui enfonce un cercle, lettrage géométrique en blocs, diagonales. On reprend la grammaire visuelle (formes, trame, mise en page), pas les slogans ni les symboles politiques d'origine, et on ne recopie aucune affiche.
- **Ce qui le fait reconnaître** : **rouge, noir et papier crème** ; tout est **en diagonale** ; des **photos découpées et tramées à 45°** collées à côté d'aplats de papier ; un grand cercle noir derrière le sujet ; un **slogan en lettres-blocs tamponné lettre par lettre**.
- **Marche pour** : annonce qui doit frapper, appel à l'action, manifeste de marque, ouverture d'événement, promotion (« dernier jour »), sujet d'histoire du XXᵉ siècle, contenu engagé ou militant assumé par le client.
- **Ne marche pas pour** : douceur, bien-être, luxe, explication pas à pas, sujet pour enfants. L'usage est **restreint** : le style crie, il ne murmure pas. À ne pas confondre avec `bauhaus` (formes primaires calmes, trois couleurs) ni avec la catégorie montage (vrai montage de rushes).

## 2. Palette, typographie, matières

| Rôle | Couleur |
|---|---|
| Papier vieilli | `#e9dfc4`, zones sombres `#d9c9a4` |
| Rouge | `#c8231c`, ombre `#8f1711` |
| Noir | `#151311` |
| Crème (bord des découpes) | `#f4ecd6` |
| Photo tramée | gris de `#fafafa` à `#9c9c9c`, puis trame noire |
| Une touche chaude facultative | or `#e3b03e`, orange `#e2741c` |

- **Lettrage** : des lettres-blocs construites sur un module de 5 × 7 carrés, chaque lettre faite de rectangles et de polygones (diagonales en quadrilatères). Pour un client francophone, **lettres latines** ; police de secours libre et proche : Anton ou Bebas Neue. Capitales uniquement.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : League Gothic à la place d'Anton et de Bebas Neue. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/anton`, `@fontsource/bebas-neue` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : papier crème texturé ; aplats de papier découpé cernés d'un trait noir de 3 px ; **photo tramée** : points sur une grille tournée à 45°, diamètre proportionnel à l'ombre ; ombres des aplats faites de points de trame, pas de dégradés.
- **Le collage** : chaque morceau de photo garde un **liseré crème de 7 px**, comme une découpe aux ciseaux. Les traits du visage et les détails importants sont repris d'un trait noir net par-dessus la trame.

## 3. Composition 9:16

- Aucun élément majeur à l'horizontale ou à la verticale : barres, blocs de texte et sol sont inclinés (de 0,26 à 0,5 radian, soit 15° à 29°).
- **Recette de base** : un grand cercle noir (rayon d'environ 220 px) derrière le sujet, vers le tiers haut ; un sol rouge en biais dans le bas de l'image, bordé d'un trait noir de 12 px ; une barre noire en biais et un carré rouge en contrepoids ; cinq petites barres noires en guise de « texte courant ».
- Le vertical accentue la diagonale : faire monter la composition du bas gauche vers le haut droit.
- **Slogan** : deux ou trois mots, lettres-blocs de 110 à 160 px, posé sur le sol rouge entre y 1250 et y 1500, **par-dessus les personnages** (sur une affiche, la lettre passe devant). Chaque quatrième lettre peut être noire.
- Un mot court peut aussi être posé à la verticale dans une barre noire.
- Rien d'important à droite de x 945, au-dessus de y 160 ni en dessous de y 1560.

## 4. Ce qui bouge

- **Action principale** : le slogan se tamponne lettre par lettre (chaque lettre part avec 0,045 s de décalage, passe de 1,5 fois à sa taille en 0,12 s), puis toute la ligne ondule (les lettres sautent de 10 px en vague).
- **Boucles de fond** : (1) le coin rouge qui va et vient dans le cercle noir, le long de son axe (course de 70 px, environ 1,6 aller-retour par seconde) ; (2) un anneau en tirets rouges qui tourne autour du cercle, ou des ondes radio (quatre arcs rouges qui s'élargissent et s'effacent).
- **Autorisés** : apparition éclair `#001` (tampon), décalage en cascade `#002`, texte en vague `#130`, pulsation `#125`, répéteur `#134` (ondes), bichromie `#116`, angle penché `#036`, coupe sèche `#046`, zoom `#028` brutal, écran partagé en biais `#144`, style image par image `#128` pour les collages.
- **Interdits** : fondu enchaîné `#044`, mouvement doux et flottant `#096`, dégradés, flou de profondeur `#105`, parallaxe lente `#016`, rebond élastique `#123`.
- Les collages peuvent sauter d'une position à l'autre sans interpolation (comme du papier qu'on déplace).

## 5. Rythme et montage

- Rapide et frappé : plans de 1 à 3 s, coupes sèches sur les temps.
- Une entrée = un coup. On enchaîne trois ou quatre coups, puis on tient l'affiche complète 1,5 à 2 s pour la lire.
- Transition propre au style : une barre ou un coin rouge traverse l'écran en diagonale et laisse la nouvelle image derrière lui.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D avec `dessiner(t)` (pour la trame). Les aplats et le slogan peuvent rester en SVG animé par GSAP.
- **Structure** : fond mis en cache (papier, barres, cercle, sol), calque « photo » tramé une fois, puis éléments animés.

```js
// trame : grille tournée de 45°, diamètre = cellule × gain × √(1 − luminosité)
function tramer(ctx, src, cellule = 7, gain = 0.8, angle = Math.PI / 4) {
  ctx.beginPath();
  pourChaquePointDeGrille(src, cellule, angle, (x, y, L, alpha) => {
    if (alpha > 128) { const r = cellule * gain * Math.sqrt(1 - L) / 2; ctx.moveTo(x + r, y); ctx.arc(x, y, r, 0, 6.2832); }
  });
  ctx.fill();                       // TOUS les points dans un seul chemin, un seul remplissage
}
// tampon du slogan : lettre k
const s = k => 1 + 0.5 * (1 - Math.min(1, Math.max(0, (t - 0.045 * k) / 0.12)));
```

- **Techniques clés** : pour un visage ou une main, cellule de 4,6 px et gain de 0,74 ; pour un grand fond, cellule de 7 px. Sous la trame, un fond crème ; autour, le liseré de 7 px. Si le client fournit de vraies photos (produit, équipe), ce sont elles qu'on trame : la matière réelle passe avant le dessin.
- **Pièges** : une lettre faite de pièces qui se chevauchent dans un même chemin se troue (remplir chaque pièce séparément) ; un accent ou un signe dessiné au-dessus de la case est caché par la lettre voisine en pose verticale (tout tenir dans les 7 modules) ; positionner le slogan par le centre des lettres, sinon le bas sort du cadre ; une ombre trop forte dans la source grise devient une barbe une fois tramée (diviser l'opacité par deux).

## 7. Son

- **Musique** : percussions martelées, cuivres courts, piano dans le grave, chœur d'hommes ou accordéon selon le sujet ; rythme de marche ou de machine. Composition originale.
- **Bruitages** : tampon encreur, presse d'imprimerie, papier qu'on déchire et qu'on claque, sirène d'usine lointaine, marteau sur métal, grésillement de radio.
- **Silence** : un demi-temps de vide avant le dernier mot du slogan.
- **Voix** : affirmée, phrases de trois à six mots, sur les temps.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Rouge, noir, crème : aucune autre grande surface de couleur.
- [ ] Les lignes de force sont en diagonale.
- [ ] Au moins un élément est une photo ou une forme tramée à 45°, avec son liseré crème.
- [ ] Le slogan est en lettres-blocs, lisible, tamponné lettre par lettre, et passe devant le sujet.
- [ ] Le coin rouge et l'anneau (ou les ondes) bougent pendant tout le plan.
- [ ] Aucun dégradé, aucun fondu.
- [ ] Le slogan ne reprend aucun mot d'ordre historique et tient dans la zone utile.

**Réglages des contrôles**
- Mouvement : vif
- Caméra : mobile
- Couleurs max : 10
- Bleu-violet : interdit
- Texte vivant : oui
- Taille mini du texte : 50

## 9. Aperçu

- Planche d'ensemble des styles d'origine (image fixe, 16:9) : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg
- Film de démonstration complet : https://github.com/alchaincyf/huashu-art-motion/releases
- Crédit : 花叔 Huashu (alchaincyf), https://github.com/alchaincyf/huashu-art-motion. Pas d'aperçu séparé pour ce style ; planche donnée en lien seulement (sa composition s'inspire d'un film tiers).

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichiers `references/风格配方/22_constructivism.md` et `scripts/engine/scenes/22_constructivism.js`.
- Licence : MIT (© 2026 alchaincyf, 花叔).
- Adaptation Flot Web : traduction du chinois, lettrage latin à la place du cyrillique, retrait de la scène et des personnages de la démo, composition verticale, portage vers HyperFrames, numéros de mouvements, section son.
