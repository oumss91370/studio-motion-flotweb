# Art nouveau

## 1. Identité

- **Nom** : Art nouveau (affiche lithographiée des années 1890).
- **Inspiration** : les affiches Art nouveau de la fin du XIXᵉ siècle : figure féminine couronnée d'un halo circulaire, chevelure en volutes, fleurs, cadre ornemental, trait souple dont l'épaisseur varie. Ces affichistes sont dans le domaine public ; on reprend le vocabulaire, on ne reproduit aucune affiche.
- **Ce qui le fait reconnaître** : la **ligne en coup de fouet** (une courbe en S, fine aux bouts, épaisse au milieu, souvent terminée en spirale) ; un **contour extérieur épais et des lignes intérieures fines** ; un **halo circulaire** derrière la tête ; des fleurs et des tiges qui encadrent ; des tons pastel chauds et de l'or ; un cadre doré et un titre dans un bandeau.
- **Marche pour** : beauté, parfum, thé, fleurs, bijou, bien-être, artisanat, portrait d'une personne mise à l'honneur, invitation, saison (printemps, automne), affiche d'événement culturel.
- **Ne marche pas pour** : technologie, données, humour rapide, sujet masculin et brut. À ne pas confondre avec `art-deco` (géométrie, symétrie mécanique, or sur noir) ni avec `vitrail` (verre éclairé par-derrière).

## 2. Palette, typographie, matières

| Rôle | Couleur |
|---|---|
| Fond (dégradé vertical en trois tons) | `#b9cba0` → `#cfd3a6` → `#ecc9a2` |
| Trait | brun `#4e3320` |
| Or | `#c9a24a`, ombre `#9c7a2e` |
| Crème | `#f6eedb` |
| Chair | `#f6dcc4` |
| Cheveux (base / reflet / ombre) | `#e8bf55` / `#f6dc8a` / `#b9862a` |
| Rose (étoffe / plis) | `#e6aaa5` / `#d48e8c` |
| Fleurs rouges / cœur | `#d9706a`, `#b4504b` / `#3f6a4a` |
| Vert (bandeau, ferronnerie) | `#8fac80`, `#3d7763` |
| Halo | rose `#ebb8b2`, anneau vert d'eau `#5f9a8a` |

- **Police** : Marcellus (libre) pour le titre, 76 px dans la source, interlettrage large (12 px), d'abord un contour brun de 7 px puis un remplissage crème. Pour aller plus loin : dessiner ses propres lettres arrondies.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Playfair Display à la place de Marcellus. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/marcellus` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : marbrure de pierre lithographique (petit bruit agrandi, 50 % d'opacité) ; semis de petits anneaux en quinconce dans le fond (opacité de 38 %) ; bande de carreaux de mosaïque de 9 couleurs ; grain chaud à 5 % par-dessus tout ; cadre doré de 6 px entre deux filets bruns de 2 px.

## 3. Composition 9:16

- Le format affiche en hauteur est le format d'origine du style : il s'y installe sans effort.
- **De haut en bas** : le cadre doré (marge de 34 px, à tenir à gauche de x 945) ; une **arche** ou une fenêtre en haut (y 180 à 700) avec le soleil ou un motif rayonnant ; la **figure et son halo** (rayon d'environ 170 px, centre vers y 620) ; les fleurs de part et d'autre, tiges montant du bas ; le **bandeau de titre** entre y 1300 et y 1500.
- Symétrie souple : l'ensemble est centré, mais les deux côtés ne sont pas des miroirs (les deux bouquets oscillent en phases opposées).
- **Chevelure** : une masse de base, puis 7 à 9 mèches en S terminées par une spirale ; largeur de 14 à 18 px au départ, 2,5 px au bout. Jamais des bandes larges et régulières.
- **Texte** : un titre court (1 à 3 mots) dans le bandeau, lettres de 80 à 110 px. Sous-titres de 46 à 52 px en crème sur le bandeau vert ou sous le cadre, au-dessus de y 1560.

## 4. Ce qui bouge

- **Action principale** : quelque chose **pousse ou se lève** lentement : un soleil qui monte derrière une colline (environ 290 px par seconde dans la démo très courte de la source ; ralentir pour un plan de plusieurs secondes), une tige qui grandit, un ruban qui se déroule.
- **Boucles de fond** : (1) les halos tournent : 18 clous dorés dans un sens, 32 pétales de rosace dans l'autre, plus lentement ; (2) fleurs et chevelure ondulent : chaque fleur balance de 13 px avec une seconde onde plus lente de 5 px, les feuilles à 30 % de cette amplitude, et une onde descend le long de chaque mèche.
- **Autorisés** : tracé de ligne `#004` (la volute qui se dessine), texte sur un chemin `#131`, trajectoire `#126`, continuation du mouvement `#122` (cheveux, étoffes), pulsation `#125`, flottement `#096`, reflet de lumière `#022` sur l'or, transition liquide `#019`, travelling avant lent `#027`, panoramique vertical `#026`, plan fixe `#175`.
- **Interdits** : angles vifs et mouvements secs, coupe sèche `#046`, secousse `#024`, glitch `#023`, rebond élastique `#123`, caméra à l'épaule `#034`, lignes droites animées.
- **Vapeur, fumée, parfum** : trois rubans crème en S (largeurs de 26, 20 et 14 px, cernés d'un trait brun fin), parcourus par une onde, qui s'écartent en montant et finissent en spirale. Ils se penchent pour **ne jamais passer devant le visage**.
- Les rayons d'une verrière peuvent tourner lentement avec le soleil : toute la fenêtre change.

## 5. Rythme et montage

- Lent et continu : plans de 4 à 8 s, mouvements amples, aucune saccade (30 images par seconde).
- Chaque plan est une affiche qui vit : on installe, on laisse respirer, on passe.
- **Transition signature** : une forme organique dorée qui pousse depuis le halo et recouvre l'image (environ 0,25 s dans la source, 0,5 à 0,8 s conseillé).
- Un seul mouvement de caméra par plan, très lent.
- **Version courte (8 à 12 s)** : un seul plan-affiche de 8 à 10 s : la volute se trace dès l'image 0, la figure ou le soleil se lève, le titre se remplit ; couper la transition dorée. L'accroche est le tracé, pas une coupe.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D avec `dessiner(t)` (les rubans à épaisseur variable sont plus simples en canvas qu'en SVG).
- **Structure** : fond mis en cache (dégradé, semis, marbrure, mosaïque, cadre, bandeau, titre) ; calque des figures ; éléments animés (soleil, halos, fleurs, mèches, vapeur) ; grain en dernier.

```js
// le ruban : une ligne dont l'épaisseur respire. Points lissés, décalés de ±l/2 sur la normale, puis remplis.
function ruban(ctx, pts, largeur) {
  const P = lisser(pts), G = [], D = [];
  P.forEach((p, i) => { const q = i / (P.length - 1), n = normale(P, i), l = largeur(q) / 2;
    G.push({ x: p.x + n.x * l, y: p.y + n.y * l }); D.unshift({ x: p.x - n.x * l, y: p.y - n.y * l }); });
  remplir(ctx, G.concat(D));
}
const fuseau = max => q => max * Math.sin(Math.PI * q);            // fin aux bouts, épais au milieu
// mèche : une onde qui descend, de plus en plus ample
const dx = (q, t, phase) => Math.sin(7.4 * q + phase - 7 * t) * (6 + 20 * q);
```

- **Contour épais dehors, fin dedans** (la technique clé) : dessiner toutes les figures dans un calque avec des traits intérieurs de 2 px ; copier ce calque, le teindre en brun, et le glisser **sous** l'original à trois décalages : (−1,5 ; −1,5), (3,5 ; 4,5), (2 ; 2,5). Résultat : un liseré de 1,5 px en haut à gauche, un bord de 4 à 5 px en bas à droite, et des traits intérieurs intacts.
- **Pièges** : tracer les contours en dernier par-dessus tout fait apparaître les parties cachées à travers le corps (dessiner pièce par pièce, dans l'ordre) ; une chevelure faite de larges bandes ressemble à des saucisses ou des nouilles ; calculer la marbrure en plein écran à chaque image est des centaines de fois plus lent que d'agrandir un petit bruit ; une vapeur verticale traverse le visage quand le personnage porte la tasse à ses lèvres.

## 7. Son

- **Musique** : harpe, flûte, cordes légères, célesta, piano au toucher doux ; valse lente ou barcarolle ; lignes mélodiques longues, comme le trait.
- **Bruitages** : étoffe, feuillage, eau qui coule ou tasse qu'on pose, carillon léger, oiseaux, froissement de papier épais. Peu nombreux et doux.
- **Silence** : une suspension avant que la forme dorée ne recouvre l'image.
- **Voix** : douce, lente, phrases courtes ; laisser de longues plages sans voix.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Aucune ligne droite ni angle vif dans les figures : tout est courbe en S.
- [ ] Les lignes varient d'épaisseur (fines aux bouts, épaisses au milieu).
- [ ] Contour extérieur épais, lignes intérieures fines.
- [ ] Un halo circulaire derrière le sujet principal, et il tourne.
- [ ] Les fleurs et les cheveux ondulent ; rien n'est figé plus de 3 s.
- [ ] La palette est pastel et chaude, avec de l'or ; pas de noir pur, pas de couleur fluo.
- [ ] La vapeur ou les rubans ne passent jamais devant un visage.
- [ ] Le cadre doré et le bandeau de titre tiennent dans la zone utile.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 20
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Planche d'ensemble des styles d'origine (image fixe, 16:9) : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg
- Film de démonstration complet : https://github.com/alchaincyf/huashu-art-motion/releases
- Crédit : 花叔 Huashu (alchaincyf), https://github.com/alchaincyf/huashu-art-motion. Pas d'aperçu séparé pour ce style ; planche donnée en lien seulement.

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichiers `references/风格配方/10_nouveau.md` et `scripts/engine/scenes/10_nouveau.js`.
- Licence : MIT (© 2026 alchaincyf, 花叔). Police Marcellus : OFL 1.1.
- Adaptation Flot Web : traduction du chinois, retrait de la scène et des personnages de la démo, composition verticale, durées allongées pour des plans de plusieurs secondes, portage vers HyperFrames, numéros de mouvements, section son.
