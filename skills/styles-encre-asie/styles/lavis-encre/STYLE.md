# Lavis à l'encre de Chine

## 1. Identité

- **Nom** : Lavis à l'encre de Chine (peinture « xieyi », l'idée avant le détail).
- **Inspiration** : les films d'animation à l'encre des studios de Shanghai des années 1980 (l'espace du papier vide, l'encre qui fleurit, le tempo d'une cithare, des figures en quelques coups) ; l'immobilité avant l'action des films de sabre ; les maîtres du lavis libre (oiseau au regard levé, crevettes en quelques segments). On emprunte la grammaire, jamais un personnage, une composition ou une musique.
- **Ce que c'est** : une peinture à l'encre peinte et déroulée sous tes yeux : encre noire sur papier de riz chaud, en **cinq tons**, plus **un seul rouge**, le sceau vermillon. Pas de contour à l'occidentale : les formes sont faites par des **coups de pinceau chargés** dont le bord sombre *est* le contour, par des **lavis humides** qui diffusent dans le papier, et par des **coups secs et rapides** où le papier paraît entre les poils (le « blanc volant »). La plus grande partie du cadre est **du papier vide** : eau, ciel, brume, silence. Les choses sont **peintes à l'existence**, jamais montées en coupe.
- **Marche pour** : récit lent, sagesse, patience, artisanat, thé, arts martiaux, nature, deuil, « un seul geste change tout », chronologie en rouleau.
- **Ne marche pas pour** : produit coloré, humour, interface, données, rythme rapide.
- **À ne pas confondre** : pas de l'aquarelle (aucun lavis de couleur) ; pas du vectoriel à texture de pinceau (ni aplat ni contour fermé) ; pas un générique de calligraphie.

## 2. Palette, typographie, matières

| Ton d'encre | Opacité | Usage |
|---|---|---|
| Brûlé | ≈ 0,96 | calligraphie, lignes les plus nettes, points de mousse |
| Épais | ≈ 0,82 | contours, bord sombre des coups chargés |
| Lourd | ≈ 0,60 | lignes secondaires, plis |
| Clair | ≈ 0,34 | corps des montagnes, lavis des vêtements et des corps |
| Limpide | ≈ 0,16 | montagnes lointaines, visages, brume |

- Papier `#F2ECDE` (ou `#efe6d0`) ; encre `rgb(16,14,12)`, du gris froid à faible densité au noir chaud à pleine densité. **Un seul vermillon** `#B02E22` : le sceau, et au plus un minuscule accent dans l'histoire (un objet que porte le héros). Jamais de lavis rouge, jamais de texte rouge.
- **Variante à couleurs légères** (carte huashu) : trois pigments traditionnels en lavis très dilués, en multiplication : ocre `#c47a3c`, bleu de fleur `#6f8aa0`, jaune gomme-gutte `rgba(226,170,52,.75)` ; un rouge carmin `rgb(190,40,40)` en trois points au plus. À réserver à un sujet qui a besoin d'identifier un personnage ; sinon, reste à l'encre.
- **Typographie** : sous-titres en **inscriptions** : serif classique italique (**Cormorant Garamond italique**, OFL), couleur d'encre, sans boîte. Un petit carré vermillon marque le début de chaque ligne. Titre écrit sur la peinture, dans son vide, avec un **sceau dessiné par le code** (des lignes évidées dans un carré rouge un peu irrégulier, moucheté) : motif abstrait, pas de faux caractères.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : EB Garamond à la place de Cormorant Garamond. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/cormorant-garamond` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** :
  - *Papier* : procédural, jamais une image : marbrure en nuages, longues fibres (≈ 2 600 petits arcs, moitié bruns, moitié clairs), paillettes de pâte, grain qui s'efface quand on dézoome, léger vignettage ; **ancré au monde**.
  - *Coup de pinceau* : ligne centrale × profil de pression × bruit de largeur, plus 4 à 60 **poils** dont la charge d'encre baisse le long du trait et se rompt sur un bruit à grande échelle. Un réglage « sec » va du trait plein et mouillé au blanc volant.
  - *Coup chargé* : poils plus sombres d'un côté : le trait porte son propre contour.
  - *Deux couches* : l'humide diffuse (flou bruité, **accumulation de pigment au bord**, granulation) ; la sèche ne reçoit que le grain du papier.
  - *Eau = papier vide*, animée par de faibles stries sèches et des ronds ouverts. Montagnes qui se dissolvent vers le bas dans des bandes de brume.
  - *Figures* : une masse pâle + deux coups chargés, lignes brûlées pour les membres ; visage en 3 à 5 traits. **Le blanc est une réserve** : museau, col, pattes sont découpés dans le lavis pour laisser voir le papier, jamais peints en blanc.

## 3. Composition 9:16

- Le vertical est le format du **rouleau suspendu** : ciel et brume en haut, étages empilés, sol en bas ; on descend ou on monte en panoramique.
- **60 à 80 % de papier vide.** Sujet décentré (un tiers, un coin) ; une masse sombre peut longer le bas du cadre.
- Figure principale ≥ 1/4 de la hauteur dans les plans d'action ; dans un plan large, une figure minuscule dans le vide dit la solitude, l'accent rouge aide à la trouver.
- **Inscriptions** : 2 lignes au plus, 46 à 52 px, **dans le papier vide de chaque plan** (donc pas toujours en bas) ; en vertical, entre y 200 et 1540, à gauche de x = 900. Elles apparaissent humides et sèchent en une fraction de seconde. Tenue ≥ max(1,8 s ; réplique + 0,6 s).
- Titre en colonne ou en deux lignes courtes dans le vide, sceau dessous.
- **La première image n'est pas une page blanche** : quelques coups sont déjà posés (une page vide ne fait pas une vignette).
- 16:9 : rouleau horizontal, panoramique de droite à gauche.

## 4. Ce qui bouge

- **Action principale** : un coup de pinceau décisif. **Immobilité avant l'action** : on tient (au plus une lente avancée), puis le coup traverse le cadre en quelques images. Les conséquences ne commencent qu'après la fin du coup.
- **Boucle de fond 1** : la brume : bandes couleur papier qui glissent (150 à 270 px/s) et font apparaître et disparaître le lointain.
- **Boucle de fond 2** : le vivant en quelques coups : bambou dont les feuilles tournent, un oiseau qui traverse, des antennes ou des herbes en onde, des ronds dans l'eau, l'encre qui continue de s'étaler lentement autour des masses.
- **Gestes natifs** : un coup est tout ; le vide est de la matière (enlever de l'encre révèle du blanc) ; pinceau = geste = action ; le blanc volant (un coup sec et rapide, plus fort au sortir d'un silence) ; **la fleur d'encre** comme transition (la scène suivante pousse dans une goutte qui s'étale, avec un liseré sombre) ; le rouleau ; la masse fendue en deux.
- **Autorisés** : `#004` tracé (dans l'ordre du pinceau), `#019` transition liquide (fleur d'encre), `#025` panoramique latéral, `#026` panoramique vertical, `#029` travelling avec lointain lent, `#027` avancée dans une brume, `#028` recul jusqu'à ce qu'une marque rejoigne l'ensemble, `#046` coupe sèche vers un très gros plan (la **seule** coupe dure du style), `#040` tenue immobile.
- **Interdits** : `#044` fondu générique, `#045` volet, `#011` écrasement, interpolation de formes vectorielles, aplats, contours fermés, couleur (hors variante), `#022` balayage de lumière.

## 5. Rythme et montage

- Figures à **15 dessins par seconde** (à 30 i/s : une image sur deux ; 12 seulement dans un film livré à 24 i/s) ; position, caméra, fleurs d'encre, ronds et éclaboussures fluides.
- Lent : plans de 5 à 10 s. Durée 30 à 60 s.
- Transitions : fleur d'encre, panoramique le long du rouleau, brume.
- **Le silence est littéral** : tout à zéro (musique, ambiance, queues de réverbération), avec au plus un son dedans (une goutte). Place-le là où l'histoire retient son souffle.
- Les coups peints peuvent tomber chacun sur une note pincée. Rien ne tourne en boucle.
- **Version courte (8 à 12 s)** : un seul plan : 1,5 s d'immobilité, le coup de pinceau décisif **avant 3 s**, ses conséquences (fleur d'encre, éclaboussures), l'inscription tenue 2 s, le sceau ; couper le panoramique le long du rouleau et le long silence.

## 6. Recette technique

- **Moteur** : HyperFrames ; canvas 2D pour les coups, passe WebGL pour le papier, la diffusion et le pigment de bord.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `pinceau.js` (coups, poils, coups chargés, masses, taches), `papier.glsl` (papier, diffusion, bord, fleur), `paysage.js` (montagnes, textures de roche, pins, roseaux, ronds), `figure.js`, `sceau.js`, `inscriptions.js`.
- **Techniques clés** :
  ```js
  // pression le long du trait : attaque, relâché, léger tremblé
  const prof = smooth(0, tete, q) * (1 - 0.7 * smooth(1 - queue, 1, q)) * (0.85 + 0.15 * bruit(q));
  // un poil se rompt (blanc volant) quand le bruit passe sous le seuil de sécheresse
  const rompu = bruit(k * 1.9, i * 0.09) < sec * Math.pow(q, 1.2) * 0.95 + 0.05;
  // lavis qui s'étale : deux passes en multiplication, halo de plus en plus large
  ctx.filter = `blur(${halo * (0.4 + croissance)}px)`;
  ```
  - Rééchantillonne chaque tracé à pas constant (≈ 4 px) : sinon la fréquence du blanc volant change avec la longueur du trait.
  - **Traits stables d'un dessin à l'autre** : graine par indice de trait, ruptures calculées sur la longueur normalisée ; seul un petit frémissement de largeur est permis.
  - Les traits fixes sont peints en direct pendant qu'ils s'écrivent, puis mis en cache.
- **Pièges** :
  - Brosse sèche qui ressemble à des pointillés : ruptures sur un bruit à grande échelle + charge qui baisse.
  - **Chaque poil = un seul tracé continu à bouts plats.** Tracé segment par segment avec des bouts ronds, il fait des nœuds de bambou ou une corde.
  - Coups parallèles translucides = tuyaux d'orgue : une masse + deux coups chargés.
  - Un lavis en multiplication est transparent : la ligne du décor passe à travers un personnage. Remplis d'abord sa silhouette en couleur papier (on « réserve la place »), puis pose le lavis.
  - Découper une calligraphie par le contour d'une police crante les jonctions : la police ne sert que de squelette.
  - Hachures régulières dans une vague = grillage : coups chargés le long de sa face.

## 7. Son

- **Musique** : cithare à cordes pincées en tête, **pas piano et cordes** ; flûte verticale grave et soufflée, gros tambour et timbale pour la masse, tambour sur cadre pour les pas, petit gong pour un sceau. Modes pentatoniques. Pincés libres pour le vide, pulsation pour le mouvement, roulements pour la masse.
- **Bruitages** (≈ 3 à 5 par 10 s) : goutte d'encre (un « tink » court + un choc mouillé doux), air du pinceau (souffle granuleux, jamais un sifflement métallique), pas sur l'eau, éclaboussures, sceau (choc de bois + froissement de papier).
- **Voix** : calme, peu de phrases, comme des inscriptions qui n'expliquent pas l'image. Musique baissée d'environ 8 dB sous la voix. Mix −14 LUFS.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

Défaut connu de la carte huashu (deux étoiles) : figures pas assez libres (trop dessinées). Erreurs : cadre rempli ; contours fermés ; gris uniforme ; rouge décoratif ; faux caractères ; fondus.

- [ ] Au moins 60 % de papier vide dans chaque plan tenu.
- [ ] Les cinq tons sont présents ; le lointain est pâle et flou, le proche sombre et texturé.
- [ ] Les coups rapides montrent du blanc volant ; les lavis ont un bord plus sombre.
- [ ] Un seul rouge : le sceau, plus un accent minuscule au maximum.
- [ ] Les blancs sont des réserves de papier, jamais de la peinture blanche.
- [ ] Les choses sont peintes dans l'ordre du pinceau ; aucun fondu.
- [ ] Une tenue immobile précède le coup décisif ; un vrai silence existe.
- [ ] Inscriptions dans le vide, sans boîte ; aucun faux idéogramme.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : mobile
- Couleurs max : 6
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 46

## 9. Aperçu

- Film de démo d'origine *The Swordsman and the River* (48 s, 16:9) : https://lemomo-ai.github.io/lemo-opuscar/films/ink-wash.mp4 · 1080p : https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/ink-wash.mp4 · affiche : https://lemomo-ai.github.io/lemo-opuscar/posters/ink-wash.jpg · galerie : https://lemomo-ai.github.io/lemo-opuscar/#hand-drawn-painting
- Crédit : LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0. À montrer avec ce crédit ; ne pas en reprendre l'histoire ni les plans.
- Carte huashu : pas d'aperçu isolé (planche commune `assets/全风格总览.jpg`, à ne pas utiliser comme vitrine).

## 10. Origine

- **lemomo-ai/lemo-opuscar**, commit `9eb7739` : `styles/ink-wash/STYLE.md`, `DEMO.md`, `demo/ink.js`, `comp.js`, `land.js`, `wave.js`, `glyph.js`, `seal.js`, `hero.js`, `subs.js`. Licence MIT, © 2026 LemoLab ; film et images CC BY 4.0.
- **alchaincyf/huashu-art-motion**, commit `1468196` (v1.3.0) : `references/风格配方/17_ink.md` (deux étoiles), `scripts/engine/scenes/17_ink.js` : profil de pression, poils continus, lavis en deux passes, réserves, variante à couleurs légères, première image non vide. Voir aussi la recette de recherche `50_ma_yuan.md` (composition « dans un coin », non validée : non reprise). Licence MIT, © 花叔 Huashu.
- Adaptation Flot Web : fiche fusionnée et traduite, section 9:16, sceau abstrait et texte français à la place de la calligraphie, numéros du dictionnaire de mouvements.
