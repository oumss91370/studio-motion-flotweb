# Caméra, profondeur et curseur (vidéos de produit)

C'est la plus grande différence entre un film qui se lit comme du motion design et une page web avec des fondus. Une surface plate qui apparaît en fondu est une diapositive. La même surface, légèrement tournée dans l'espace, avec une caméra qui s'engage vers ce qu'on démontre, est un plan.

Les extraits sont en GSAP dans HyperFrames. Les ressorts « en forme fermée » de certaines fiches s'appellent depuis un écouteur `hf-seek` (voir la fiche `forme-continue-sur-la-musique`).

## 1. Le montage à deux nœuds

**Ne jamais mettre sur le même élément une rotation de tout le plan et un changement d'échelle en cours de plan** : deux animations écrivent la même transformation, et le mouvement saccade.

```html
<div class="clip cam" id="p06-cam">          <!-- extérieur : le travelling (échelle) -->
  <div class="scene3d" id="p06-scene">       <!-- intérieur : la rotation 3D -->
    <!-- la carte, TOUT son contenu, le curseur et ses ondes -->
  </div>
</div>
```
```css
.scene3d { transform-style: preserve-3d; }
```

Seconde moitié de la règle : **tout ce que la caméra déplace est à l'intérieur du montage**, en coordonnées locales. Un curseur posé par-dessus un plan qui bouge est un curseur qui glisse de sa cible.

## 2. La rotation de tout le plan

Une seule rotation lente sur toute la durée : la surface commence tournée et se redresse ; on lit une caméra qui se pose, pas un objet qui tourne.

```js
gsap.set(scene, {transformPerspective: 2600, transformOrigin: "50% 52%"});
tl.fromTo(scene, {rotationY: -7.2, rotationX: 2.1},
                 {rotationY: -1.3, rotationX: 0.5, duration: DUREE, ease: "power1.inOut"}, 0);
```

| Paramètre | Plage | Note |
|---|---|---|
| `transformPerspective` | 2200 à 2800 | plus bas = grand angle qui déforme ; plus haut = effet aplati |
| `rotationY` au départ | −6° à −10° | négatif = bord gauche vers le spectateur |
| `rotationY` à la fin | −1° à −2° | **jamais 0** : un soupçon d'angle garde la profondeur |
| `rotationX` | 2° → 0,5° | petit ; une bascule verticale se lit vite comme une erreur |

En 9:16, réduire d'un tiers (−5° → −1°) : la carte est plus étroite et la déformation se voit plus.

## 3. Le travelling (poussée en cours de plan)

La poussée sert un propos : l'élément important de la fin du plan est souvent un petit bouton. On pousse pour ce temps-là, puis on relâche.

```js
gsap.set(cam, {transformOrigin: "89.8% 85.7%"});          // le centre exact du bouton cliqué
tl.to(cam, {scale: 1.12, duration: 0.36, ease: "power2.inOut"}, 2.46);
tl.to(cam, {scale: 1,    duration: 0.36, ease: "power2.inOut"}, 3.34);
```

**Autour de l'action, pas dessus** : la poussée est posée **avant** l'arrivée du curseur, immobile pendant le clic, relâchée seulement quand l'état a changé. Une caméra qui bouge pendant un clic vole le clic.

## 4. L'astuce du point fixe

Sous une mise à l'échelle autour de l'origine `O`, un point `P` va en `O + (P − O)·s`. Si `O` est **exactement** le centre du bouton cliqué, ce bouton ne bouge pas du tout : toute coordonnée déjà calculée pour le curseur ou l'onde reste juste pendant toute la poussée.

Origine en pourcentage = (position du point − coin de la carte) ÷ taille de la carte.

## 5. De la profondeur sans moteur 3D

Avec `preserve-3d`, les enfants portent un vrai `z`. Quelques pixels suffisent :

```js
gsap.set(["#reponse", "#reponse-texte"], {z: 16});
gsap.set(["#conditions", "#conditions-bouton"], {z: 22});
```

Valeurs **statiques** de 12 à 22 px : la rotation fournit le mouvement, les `z` fournissent la parallaxe. Mettre au plan proche ce que l'histoire touche (ce qu'on clique, ce qui change d'état) ; laisser le reste au plan de base.

## 6. Bascule de mise au point

Quand la caméra s'engage vers une zone, sortir l'autre du point :

```js
tl.to(planStat, {filter: "blur(2.6px)", opacity: 0.55, duration: 0.44, ease: "power2.inOut"}, 2.10);
tl.to(planStat, {filter: "blur(0px)",   opacity: 1,    duration: 0.34, ease: "power2.inOut"}, 3.30);
```

Donner à l'élément un `filter: blur(0px)` explicite en CSS, sinon la première image saute.

## 7. Parallaxe

Deux plans qui dérivent à des vitesses différentes, **un seul mouvement lent chacun sur tout le plan, en sens opposés**. Jamais une dérive par élément (c'est l'écran de veille).

## 8. Le curseur est un accessoire de scène

À taille réelle, un pointeur fait environ 32 px et disparaît dans tout bouton coloré. Le dessiner comme un accessoire :

- **Environ 44×54 px** en 16:9 ; **60×74 px en 9:16** (il doit se voir sur un téléphone).
- **Remplissage blanc, contour sombre épais, vraie ombre portée** : il survit aux fonds sombres comme aux boutons clairs.
- **Un seul dessin de curseur dans tout le film.**
- **Positionné par sa pointe** : position de l'élément = point de clic − décalage de la pointe ; `transform-origin` sur la pointe, pour que l'appui se fasse autour du point touché.
- **À l'intérieur du montage caméra.**
- **Le faire disparaître quand son travail est fini** : un pointeur garé à l'écran pendant la tenue finale signale que personne n'a regardé le rendu.

## 9. Le clic en trois couches

Un clic, c'est trois couches sur la même image ; une seule se lit comme un défaut.

```js
function clic(n, t) {
  const halo = `#halo-${n}`, onde = `#onde-${n}`;
  tl.fromTo(halo, {opacity: 0, scale: 0.3}, {opacity: 1, scale: 0.62, duration: 0.1}, t - 0.1);   // le halo PRÉCÈDE l'appui de 0,1 s et finit pile à t
  tl.to("#curseur", {scale: 0.86, duration: 0.06, ease: "power2.in"}, t);
  tl.to("#curseur", {scale: 1, duration: 0.26, ease: "back.out(2.4)"}, t + 0.06);
  tl.to(halo, {opacity: 0, scale: 1.15, duration: 0.34}, t);
  tl.fromTo(onde, {opacity: 0.75, scale: 0.34},
            {opacity: 0, scale: 1.5, duration: 0.42, immediateRender: false}, t);
}
```

- `immediateRender: false` sur l'onde, sinon elle est visible à l'image 0 du plan.
- Le halo monte en **0,1 s**, pas plus : il part à `t − 0,1` et son extinction commence à `t`. Avec 0,12 s, les deux animations se recouvrent pendant 0,02 s et le lint sort `overlapping_gsap_tweens` (vérifié en 0.9.33). Le lint ne voit ce défaut que si les sélecteurs sont écrits en clair (`"#halo-1"`) : avec des sélecteurs construits dans une fonction, comme ici, il se tait, donc la règle se tient à la main.
- **Le bouton réagit aussi** : il s'enfonce de 6 % sur l'image du clic et revient en ressort ; l'état change. Le clic est une cause : montrer l'effet.
- Proportionner halo et onde au bouton (un halo plus grand que le bouton se lit comme une auréole).

## 10. Le trajet du curseur

Un trajet en ligne droite avec un seul amorti fait robot.

```js
tl.to("#curseur", {x: -112, y: 146, duration: 0.05}, 1.32);               // petit recul avant de partir
tl.to("#curseur", {x: 0, duration: 0.20, ease: "power2.inOut"}, 1.38);    // x et y sur des amortis
tl.to("#curseur", {y: 0, duration: 0.24, ease: "power1.inOut"}, 1.38);    // différents : la trajectoire se courbe
```

Partir assez tôt pour que **le clic** tombe sur son mot ou son temps : c'est le clic qui est calé, pas le départ. Laisser 0,01 s entre deux animations de la même propriété.

**Flou de mouvement du moteur et montage 3D.** Le flou de HyperFrames s'active par `data-motion-blur="on"` sur la racine (l'attribut nu n'active rien). Mais un élément animé à l'intérieur d'un montage `preserve-3d` (ce curseur, les cartes) n'est pas flouté en 0.9.33, pas plus qu'un `<svg>` animé directement : essai fait, image identique avec et sans flou. Pour un curseur vraiment filé, le poser sur un calque à plat au-dessus du montage et animer un `<div>` qui contient le `<svg>` (il ne suit alors plus la caméra : recalculer sa position à la main) ; sinon garder un curseur net, ce qui est le choix par défaut de cette recette. Détail : skill `rendu`, « Flou de mouvement ».

Version « curseur vivant » (films sur la musique) : inclinaison selon la vitesse horizontale (jusqu'à ±14°), courte traînée, étiquette de nom qui suit avec un léger retard, appui `1 − 0,16·exp(−((t−tc)/0,045)²)`, onde de 0,4 s.

## 11. Budget du mouvement contre les bords

Chaque mouvement de caméra agrandit la boîte du plan. Calculer le plafond avant de choisir l'échelle :

```
bas_après = bas + (bas − origine_y) × (échelle − 1)
```

En 9:16, la limite basse est y = 1560 (zone d'interface de 360 px) et la limite droite x = 945. Faire le même calcul sur les quatre bords. Le nombre est de l'arithmétique, pas du goût.

## 12. Caméra « un seul monde »

Pour les films en plan-séquence : une seule transformation sur un conteneur « monde », position et **zoom interpolé en logarithme** (zoomer linéairement paraît faux). Jamais deux zooms de sens opposés dos à dos. Une image vide est un défaut : cadrer le contenu, puis pousser, filer ou reculer. Les reculs révèlent l'échelle (un message → un mur de centaines).

**Piège majeur** : jamais `will-change` sur ce que la caméra agrandit (le texte devient flou).

Origine : AbubakrChan/product-launch-motion, commit `edbfb10`, `legacy/references/05-camera-3d-cursor.md` et `references/technique.md` (MIT). Réécrit en français, valeurs 9:16 ajoutées par Flot Web.
