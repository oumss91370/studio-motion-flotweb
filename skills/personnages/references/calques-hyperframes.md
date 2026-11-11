# Le même personnage en calques HyperFrames

À utiliser quand la vidéo est en 2D, ou quand un plan est fixe sur une image de décor (rendue par Blender ou dessinée). Les pièces, les noms et les pivots sont ceux de `pieces-svg.md`.

Pour la syntaxe exacte d'une composition (éléments minutés, ligne de temps, rendu), suivre le skill `rendu`. Ce document ne décrit que le personnage.

## Structure

Un conteneur par personnage, dans le repère du gabarit (600 × 1000), qu'on place et qu'on met à l'échelle d'un bloc. À l'intérieur, un calque par pièce, tous de la même taille, superposés.

```html
<div class="perso" id="inventeur" style="width:600px;height:1000px;position:absolute;left:240px;top:520px;transform-origin:300px 980px;">
  <img class="ombre"   src="personnages/inventeur/ombre.svg">
  <img class="jambe-g" src="personnages/inventeur/pieces/jambe-g.svg">
  <img class="jambe-d" src="personnages/inventeur/pieces/jambe-d.svg">
  <div class="corps">
    <img src="personnages/inventeur/pieces/corps.svg">
    <img class="bras-g" src="personnages/inventeur/pieces/bras-g.svg">
    <img class="bras-d" src="personnages/inventeur/pieces/bras-d.svg">
    <div class="tete">
      <img src="personnages/inventeur/pieces/tete.svg">
      <img class="yeux"   data-nom="neutre"  src="personnages/inventeur/expressions/yeux-neutre.svg">
      <img class="yeux"   data-nom="plisses" src="personnages/inventeur/expressions/yeux-plisses.svg">
      <img class="bouche" data-nom="fermee"  src="personnages/inventeur/expressions/bouche-fermee.svg">
      <img class="bouche" data-nom="petite-ouverte" src="personnages/inventeur/expressions/bouche-petite-ouverte.svg">
      <img class="costume" src="personnages/inventeur/pieces/costume-coiffe.svg">
    </div>
  </div>
</div>
```

```css
.perso img, .perso div { position: absolute; left: 0; top: 0; width: 600px; height: 1000px; }
.perso .corps  { transform-origin: 300px 700px; }   /* bassin */
.perso .tete   { transform-origin: 300px 420px; }   /* cou */
.perso .bras-g { transform-origin: 215px 470px; }   /* épaule */
.perso .bras-d { transform-origin: 385px 470px; }
.perso .jambe-g{ transform-origin: 265px 700px; }
.perso .jambe-d{ transform-origin: 335px 700px; }
.perso .yeux, .perso .bouche { opacity: 0; }
```

Les `transform-origin` sont les pivots de la fiche du personnage.

## Échanger les expressions

Un échange est un changement instantané d'opacité, placé à une image précise de la ligne de temps (temps en secondes = image ÷ 30).

```js
function montrer(tl, perso, famille, nom, image) {
  const t = image / 30;
  tl.set(`#${perso} .${famille}`, { opacity: 0 }, t);
  tl.set(`#${perso} .${famille}[data-nom="${nom}"]`, { opacity: 1 }, t);
}
montrer(tl, "inventeur", "yeux", "neutre", 0);
montrer(tl, "inventeur", "bouche", "fermee", 0);
montrer(tl, "inventeur", "yeux", "plisses", 380);   // anticipation
```

Pas de fondu entre deux expressions : l'échange est net, caché sous le plissement des yeux (voir `31-emotions.md`).

## Une ligne de jeu en GSAP

```js
// PLAN 07 : anticipation 380, action 396, tenue jusqu'à 406
const f = n => n / 30;
montrer(tl, "inventeur", "yeux", "plisses", 380);
tl.to("#inventeur .corps", { scaleY: 0.98, duration: f(4), ease: "power1.out" }, f(380));      // léger tassement
tl.to("#inventeur .tete",  { rotation: -8, x: 14, duration: f(6), ease: "power2.out" }, f(396)); // action sur le mot
tl.to("#inventeur .corps", { scaleY: 1, duration: f(8), ease: "back.out(1.6)" }, f(396));        // stabilisation
montrer(tl, "inventeur", "yeux", "neutre", 398);
// tenue : rien ne bouge d'important de 396 à 406
```

Respiration au repos, discrète et sans rebond :

```js
tl.to("#inventeur .corps", { scaleY: 1.015, duration: 1.8, ease: "sine.inOut", yoyo: true, repeat: 5, transformOrigin: "300px 700px" }, 0);
```

Arrêter la respiration pendant une action (ne pas animer deux fois la même propriété au même moment : voir les pièges GSAP du skill `principes-mouvement`).

## Poser le personnage sur un décor

- **Sur une image de décor rendue par Blender** (plan fixe) : placer les pieds sur le sol de l'image, mettre à l'échelle d'après un repère du décor (une porte fait 2,1 m), ajouter l'ombre de contact (une ellipse noire floue, opacité 0,35 à 0,5, sous les pieds).
- Le personnage reste **net** ; si le décor a de la profondeur de champ, c'est le fond qui est flou.
- Si la caméra du décor bouge (travelling), ou si un objet doit passer devant le personnage, **monter le personnage dans Blender** : en calque, il glisserait sur le décor.
- Une avancée de caméra très lente peut se faire en mettant décor et personnage dans le même conteneur mis à l'échelle (de 1,00 à 1,06 sur 2 s), mais sans parallaxe : à réserver aux plans courts.

## Zones sûres et taille

En vertical 1080×1920 : rien d'important dans les 160 px du haut, les 360 px du bas et les 135 px de droite. Le visage du personnage reste dans la moitié haute de la zone utile ; ses pieds peuvent descendre dans la zone du bas si rien d'important ne s'y joue.

## Contrôles

- Une image fixe par pose clé.
- Une bande d'images autour de chaque action.
- Un agrandissement du visage sur chaque réaction importante.
- Vérifier qu'une rotation de bras ou de tête ne découvre aucun trou entre deux pièces.
