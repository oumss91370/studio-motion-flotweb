# GSAP pour la vidéo : pièges et bonnes pratiques

GSAP est la bibliothèque d'animation utilisée par HyperFrames. Ce document ne garde que ce qui sert à une vidéo rendue **image par image** : le moteur met la timeline en pause et la place à un instant précis pour chaque image, parfois dans le désordre. Tout ce qui dépend d'une horloge, d'un geste de l'utilisateur ou d'un défilement est hors sujet.

Le contrat exact du moteur (attributs, enregistrement de la timeline, commandes) est dans le skill `rendu`. En cas de désaccord, **c'est le skill `rendu` qui a raison**.

Sommaire : 1. les règles vitales — 2. tweens — 3. timeline — 4. courbes — 5. texte et SVG (plugins) — 6. utilitaires — 7. tableau des pannes — 8. hors sujet.

---

## 1. Les règles vitales

1. **Une timeline en pause par composition**, construite d'un bloc, **enregistrée en dernier** (après tous les tweens, et après tout chargement de police ou découpage de texte).
2. **Tout est fonction du temps de la timeline.** Pas de `Date.now()`, pas de `setTimeout`, pas de `requestAnimationFrame`, pas de mesure de mise en page dans un `onUpdate`.
3. **Aucun aléatoire sans graine.** `Math.random()`, `gsap.utils.random()` et la chaîne `"random(…)"` donnent un résultat différent à chaque rendu : interdit. Utilise un générateur à graine (voir section 6).
4. **Pas de répétition infinie** (`repeat: -1`). Calcule un nombre fini : `repeat: Math.max(0, Math.floor(dureeScene / cycle) - 1)`.
5. **Position sur la timeline plutôt que `delay`.**
6. **Transformations par les alias GSAP** (`x`, `y`, `scale`, `rotation`…), jamais par `left` / `top` / `width` / `height`, et **aucun `transform` CSS** sur un élément que GSAP transforme.
7. **Une propriété d'un élément n'est pilotée que par une seule timeline.**

---

## 2. Tweens

### Les quatre méthodes

| Méthode | Ce qu'elle fait | Piège |
|---|---|---|
| `to(cible, vars)` | de l'état actuel vers `vars` | l'état de départ est lu au moment où le tween démarre |
| `from(cible, vars)` | de `vars` vers l'état **actuel** | l'état de départ est appliqué **tout de suite** (`immediateRender`) |
| `fromTo(cible, de, vers)` | les deux bouts sont explicites | le plus sûr quand un élément est animé plusieurs fois |
| `set(cible, vars)` | pose une valeur sans durée | à placer sur la timeline (`tl.set(…, temps)`) pour qu'elle soit rejouée au bon instant |

### Le piège `immediateRender`

`from()` et `fromTo()` appliquent leur état de départ dès leur création. Si deux `from()` visent **la même propriété du même élément**, le second fige une mauvaise valeur d'arrivée et l'animation devient invisible ou saute.

```js
// Faux : le deuxième from() lit un état déjà modifié par le premier
tl.from(".titre", { y: 80, duration: 0.6 }, 0.2)
  .from(".titre", { y: -80, duration: 0.6 }, 3.0);

// Juste : états explicites
tl.fromTo(".titre", { y: 80 }, { y: 0, duration: 0.6, ease: "expo.out" }, 0.2)
  .fromTo(".titre", { y: 0 }, { y: -80, duration: 0.33, ease: "expo.in", immediateRender: false }, 3.0);
```

Règle simple : **un élément animé plus d'une fois sur la même propriété → `fromTo()` partout, et `immediateRender: false` sur tous sauf le premier.**

### Transformations

- Alias : `x`, `y`, `xPercent`, `yPercent`, `scale`, `scaleX`, `scaleY`, `rotation`, `rotationX`, `rotationY`, `skewX`, `transformOrigin`.
- `xPercent` / `yPercent` pour centrer ou sortir un élément de sa propre taille (`yPercent: 105` sous un masque).
- Sur un SVG : `svgOrigin` (coordonnées du SVG) **ou** `transformOrigin`, jamais les deux sur le même élément.
- Rotation avec sens imposé : `rotation: "-170_short"` (chemin le plus court), `"_cw"` (sens horaire), `"_ccw"`.
- Valeurs relatives : `x: "+=100"`, `rotation: "-=30"`.
- Perspective pour un léger effet 3D : `transformPerspective` sur l'élément (voir `camera.md`).
- N'anime pas `width`, `height`, `top`, `left`, `margin` quand une transformation suffit : c'est plus lent à rendre et moins net.
- `will-change` seulement sur ce qui s'anime — et **jamais** sur un élément que la caméra agrandit (le texte devient flou).

### Opacité et visibilité

- `autoAlpha` (opacité + `visibility: hidden` à 0) est pratique pour les éléments internes.
- Sur un élément de scène géré par le moteur (un clip), n'anime pas la visibilité : utilise `opacity`. Voir le skill `rendu`.

### Chevauchements

Deux tweens qui se recouvrent sur la même propriété provoquent une saccade. Soit tu les sépares dans le temps, soit tu ajoutes `overwrite: "auto"` au second.

### Décalages (`stagger`)

```js
tl.from(".mot", { y: 40, autoAlpha: 0, duration: 0.6, ease: "expo.out", stagger: 0.1 }, "frappe");
tl.from(".case", { scale: 0, duration: 0.4, stagger: { each: 0.04, from: "center", grid: "auto" } }, "grille");
```

- `stagger: 0.1` = 3 images à 30 i/s. Garde le total sous 0,5 s (`amount: 0.5` répartit automatiquement).
- `from` : `"start"`, `"center"`, `"edges"`, `"end"` ou un indice.
- Préfère un `stagger` à une série de tweens à délais manuels.

### Valeurs par fonction

`x: (i, el) => i * 40` calcule une valeur par cible. La fonction doit être **déterministe** (pas d'aléatoire sans graine).

---

## 3. Timeline

### Paramètre de position

C'est le troisième argument ; c'est lui qui écrit le montage.

| Position | Sens |
|---|---|
| `1.5` | à 1,5 s du début de la timeline |
| `"<"` | en même temps que le début du tween précédent |
| `"<0.2"` | 0,2 s après le début du précédent |
| `">"` | à la fin du précédent |
| `">-0.1"` ou `"-=0.1"` | 0,1 s avant la fin : chevauchement |
| `"+=0.5"` | 0,5 s après la fin : pause |
| `"revelation"` | sur une étiquette |
| `"revelation+=0.3"` | 0,3 s après l'étiquette |

### Étiquettes

Nomme les temps forts et cale tout dessus : c'est lisible, et un changement de rythme ne demande que de déplacer l'étiquette.

```js
const tl = gsap.timeline({ paused: true, defaults: { duration: 0.6, ease: "expo.out" } });
tl.addLabel("accroche", 0.2)
  .addLabel("revelation", 4.0)
  .addLabel("appel", 8.5);
```

Pour le son : l'impact visuel est sur l'étiquette, et l'**attaque** du bruitage tombe sur cette même image, à `étiquette + 0,008 s` : jamais avant. C'est la règle du skill `son` (attaque sur l'impact, +8 ms) ; son script `caler.py` lit les instants dans le code et écrit les balises `<audio>`. Seuls un souffle ou une montée commencent avant l'étiquette, pour que leur pic ou leur fin tombe dessus.

### Valeurs par défaut

`defaults: { duration, ease }` évite de répéter. **Chaque style a les siennes**, données par sa fiche (courbe signature et durées) ; ne laisse pas `power2.out` à 0,5 s par habitude.

### Imbrication

Une fonction par scène qui renvoie une timeline, ajoutée à la timeline principale : `maitre.add(sceneAccroche(), "accroche")`. La durée d'une timeline est celle de ses enfants ; on ne la fixe pas dans le constructeur.

Limites à connaître : une timeline de scène n'atteint pas les éléments d'un autre fichier, et deux timelines ne doivent pas animer la même propriété du même élément.

### Tenir une durée exacte

Si la scène doit durer exactement N secondes, termine par un tween vide ou un `tl.set({}, {}, N)` pour que la timeline atteigne bien cette durée.

---

## 4. Courbes

| Famille | Caractère | Usage vidéo |
|---|---|---|
| `power1` à `power4` | de la plus douce à la plus raide | déplacements ; `power2.inOut` pour la caméra |
| `expo` | départ ou arrivée très marqués | entrées (`expo.out`) et sorties (`expo.in`) nettes |
| `circ` | proche d'`expo`, plus rond | variantes |
| `sine` | très doux | boucles d'ambiance (`sine.inOut`) |
| `back` | dépasse puis revient | arrivées vivantes : `back.out(1.2)` discret, `back.out(1.7)` par défaut, au-delà de 2 cartoon |
| `elastic` | oscille | **un moment héros** : `elastic.out(1, 0.5)` ; `(1, 0.3)` est très nerveux |
| `bounce` | rebondit au sol | chute d'objet seulement |
| `steps(n)` | par paliers | styles « en 2 », pixel art, image par image (#128) |
| `none` | vitesse constante | rotation continue, dérive, défilement, barre de progression |

Chaque famille existe en `.in`, `.out`, `.inOut`.

- **`CustomEase`** : `CustomEase.create("signature", "0.16, 1, 0.3, 1")` accepte les quatre nombres d'un cubic-bezier (ou un tracé SVG). C'est ainsi qu'on déclare la **courbe signature** d'un style, puis `ease: "signature"`.
- **`CustomWiggle`** : tremblement réglable (nombre d'oscillations, type). **`CustomBounce`** : rebond réglable, avec la courbe d'écrasement associée.
- Rappel : jamais `none` sur un déplacement, une échelle ou une opacité (voir `principes.md`).

---

## 5. Texte et SVG (plugins)

Tous les plugins GSAP sont aujourd'hui gratuits, y compris en usage commercial, et se chargent depuis le même paquet que GSAP : pas de clé, pas de registre privé. Enregistre-les une fois : `gsap.registerPlugin(SplitText, DrawSVGPlugin, …)`.

Version et balises : **GSAP 3.15.0**, celle que donne le skill `rendu` (`rendu/SKILL.md`, « GSAP : version et chargement »). Un plugin se charge après GSAP, à la même version :

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/SplitText.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/CustomEase.min.js"></script>
```

Seuls `gsap.min.js`, `CustomEase.min.js` et `MotionPathPlugin.min.js` sont embarqués par HyperFrames ; les autres plugins sont téléchargés à chaque rendu, ou copiés dans `assets/vendor/` pour un projet hors ligne (même section du skill `rendu`).

### SplitText (texte mot par mot, ligne par ligne)

```js
document.fonts.ready.then(() => {
  const decoupe = SplitText.create(".titre", { type: "lines, words", mask: "lines" });
  tl.from(decoupe.words, { yPercent: 105, duration: 0.67, ease: "expo.out", stagger: 0.1 }, "accroche");
  // …puis seulement ensuite, enregistrer la timeline
});
```

- **Découper après le chargement des polices** (`document.fonts.ready`), sinon les coupures de lignes sont fausses. La timeline est enregistrée **après** ce bloc, pas avant.
- `mask: "lines"` crée le masque de la révélation (#005) sans balisage supplémentaire.
- **Avec `mask: "lines"`, interligne d'au moins 1,2** (`line-height: 1.2`, soit 115 px pour un corps de 96 px). Chaque ligne est enfermée dans une boîte de la hauteur de l'interligne : plus serré, le masque coupe les jambages (g, p, q, y, la virgule) et les accents des capitales, et `check` sort des erreurs `text_box_overflow`. Essai en Montserrat 900 à 96 px : interligne 1,04 → 5 erreurs, contrôle en échec ; interligne 1,2 → contrôle bon, jambages entiers.
- `font-kerning: none` sur le texte découpé, sinon les lettres bougent d'un poil au découpage.
- **Pas de `text-wrap: balance`** sur un texte découpé.
- Ne gère pas le `<text>` d'un SVG.
- Écritures liées (arabe, etc.) : découpe **par mot**, jamais par lettre.
- Décalages : mots 0,06 à 0,12 s, lettres 1 image (0,033 s).

### ScrambleText

Texte qui se brouille puis se fixe (#129). L'aléatoire interne n'a pas de graine : pour un rendu reproductible, préfère une version maison pilotée par le temps et un générateur à graine.

### DrawSVG (tracé de ligne, #004)

```js
tl.fromTo(".courbe", { drawSVG: "0% 0%" }, { drawSVG: "0% 100%", duration: 1.5, ease: "power2.inOut" }, "trace");
```

Agit sur le **contour** (`stroke`), pas sur le remplissage. Fonctionne le mieux sur des chemins d'un seul segment ; pour effacer par le début : `drawSVG: "100% 100%"`.

### MorphSVG (morphing de forme, #012)

`MorphSVGPlugin.convertToPath("circle, rect")` transforme les formes simples en chemins. Si le morphing se tord : `type: "rotational"` ou régler `shapeIndex`.

### MotionPath (trajectoire, #126)

```js
tl.to(".avion", { motionPath: { path: "#trajet", align: "#trajet", alignOrigin: [0.5, 0.5], autoRotate: true },
                  duration: 3, ease: "power1.inOut" }, "vol");
```

Sert aussi à donner un **arc** à un déplacement simple.

### Flip

Calcule le passage d'une mise en page à une autre (élément partagé entre deux écrans, #161). En vidéo, on obtient souvent le même résultat plus simplement avec un `fromTo` sur `x`, `y`, `scale` d'un seul élément persistant.

### Physics2D, PhysicsProps

Vitesse, angle, gravité pour des objets lancés (#123, #015). Déterministes si les valeurs de départ le sont.

---

## 6. Utilitaires (`gsap.utils`)

| Fonction | Usage vidéo |
|---|---|
| `clamp(min, max, v)` | borner une valeur (toujours borner ce qui est calculé) |
| `mapRange(a1, a2, b1, b2, v)` | convertir une progression en valeur (0–1 → 0–360°) |
| `normalize(min, max, v)` | ramener une valeur entre 0 et 1 |
| `interpolate(a, b, p)` | mélanger nombres, couleurs, objets |
| `snap(pas, v)` | caler sur une grille : pixel art, images entières (`snap(1/30)`) |
| `wrap(min, max, v)` | boucler une valeur : bandeau défilant (#094), motif répété |
| `wrapYoyo(min, max, v)` | aller-retour (#127) |
| `distribute({ … })` | répartir une valeur sur un groupe (décalages, positions) |
| `pipe(f1, f2, …)` | enchaîner des transformations |
| `toArray(sel)` | obtenir un vrai tableau d'éléments |
| `splitColor`, `getUnit`, `unitize` | couleurs et unités |
| `shuffle(tab)` | **aléatoire sans graine : à éviter** |
| `random(…)` | **aléatoire sans graine : interdit en rendu** |

En omettant la dernière valeur, la plupart renvoient une fonction réutilisable : `const versAngle = gsap.utils.mapRange(0, 1, 0, 360)`.

`mapRange` et `normalize` travaillent sur des nombres, pas sur des unités.

### Aléatoire reproductible

```js
function generateur(graine) {            // mulberry32
  return function () {
    let t = (graine += 0x6d2b79f5);
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
const alea = generateur(42);
const decalages = Array.from({ length: 30 }, () => gsap.utils.mapRange(0, 1, -40, 40, alea()));
```

Tire toutes les valeurs **une fois, à la construction**, dans un ordre fixe ; ne tire jamais dans un `onUpdate`.

### Valeur calculée à partir du temps

Pour une formule (ressort exact, somme de sinus, trajectoire), anime un objet relais et calcule dans `onUpdate` à partir de **sa** valeur :

```js
const etat = { t: 0 };
tl.to(etat, { t: 1.2, duration: 1.2, ease: "none",
  onUpdate: () => gsap.set(".icone", { scale: 1 - Math.exp(-6.5 * etat.t) * Math.cos(15 * etat.t) }) }, "pop");
```

Ici `ease: "none"` est correct : c'est le temps qui avance, la formule fait la courbe.

### Compteur, et le piège de `seek`

Un compteur est le cas le plus courant d'objet relais : on anime un nombre, et `onUpdate` l'écrit dans la page.

```js
const cpt = document.getElementById("compteur"), etat = { v: 0 };
const ecrire = () => { cpt.textContent = Math.round(etat.v).toLocaleString("fr-FR"); };
tl.to(etat, { v: 1500, duration: 2, ease: "power2.out", onUpdate: ecrire }, 0.3);
```

Chiffres à chasse fixe (`font-variant-numeric: tabular-nums`), sinon le nombre tremble. Au rendu, HyperFrames place la timeline lui-même et `onUpdate` est bien appelé (vérifié : 1 313 affiché à 1,3 s).

**Le piège est dans tes propres appels.** `tl.seek(t)` supprime les rappels par défaut : la valeur avance, mais `onUpdate` n'est **pas** appelé, et l'affichage reste sur l'ancienne valeur. Essai en GSAP 3.15.0 : après `tl.seek(1.5)`, `etat.v` vaut 1 313 et l'écran montre encore « 0 » ; après `tl.seek(1.6, false)`, l'écran montre 1 363. Donc, partout où tu places la timeline à la main (auto-contrôle en fin de script, relevé des textes, capture avec un outil) :

```js
tl.seek(t, false);     // false = ne pas supprimer les rappels : onUpdate, onStart, onComplete sont appelés
```

Termine toujours un auto-contrôle par `tl.seek(0, false)` pour remettre l'affichage à l'image 0.

---

## 7. Tableau des pannes

| Symptôme | Cause probable | Correction |
|---|---|---|
| Scène vide ou figée | timeline enregistrée avant la fin d'une construction asynchrone (polices, découpage) | enregistrer en dernier, dans le même bloc |
| Élément visible avant son entrée | `from()` créé hors timeline, ou `set` hors timeline | tout placer sur la timeline ; état initial en CSS ou `tl.set(…, 0)` |
| Animation invisible ou qui saute | deux `from()` sur la même propriété | `fromTo()` + `immediateRender: false` |
| Saccade | deux tweens ou deux timelines sur la même propriété | séparer, ou `overwrite: "auto"` |
| Rendu différent d'une fois à l'autre | aléatoire sans graine, horloge, mesure dans `onUpdate` | générateur à graine, tout en fonction du temps |
| Élément décalé ou déformé | `transform` CSS + alias GSAP sur le même élément | retirer le `transform` CSS, tout poser avec `gsap.set` |
| Texte découpé mal coupé ou qui tremble | découpage avant les polices, crénage actif, `text-wrap: balance` | `document.fonts.ready`, `font-kerning: none`, retirer `balance` |
| Jambages ou accents coupés sous un masque de lignes, `text_box_overflow` | interligne trop serré avec `mask: "lines"` | interligne d'au moins 1,2 |
| Compteur ou valeur calculée figés après un `seek` | `tl.seek(t)` n'appelle pas `onUpdate` | `tl.seek(t, false)` |
| `overlapping_gsap_tweens` au lint | deux tweens de la même propriété se recouvrent, même de 0,02 s | finir le premier avant le début du second, ou `overwrite: "auto"` |
| Enfant en `inset: 0` invisible dès qu'on anime son parent | le parent transformé devient le repère et n'a pas de taille | donner largeur et hauteur à l'élément animé (skill `rendu`, règle 13) |
| Texte flou pendant un zoom | `will-change` ou échelle sur un calque pixellisé | retirer `will-change`, agrandir le conteneur plutôt que le texte rendu |
| Rotation qui part du mauvais côté | chemin le plus long | suffixe `_short`, `_cw`, `_ccw` |
| SVG qui tourne autour du mauvais point | `transformOrigin` et `svgOrigin` mélangés | n'en garder qu'un |
| Boucle qui s'arrête ou déborde | `repeat: -1` ou mauvais compte | nombre fini calculé depuis la durée de la scène |
| Vidéo trop courte | la timeline finit avant la durée voulue | tween vide final à la durée exacte |
| Mouvement « mécanique » | `ease: "none"` ou courbe par défaut partout | courbe signature du style, voir `principes.md` |

Avant de dire « c'est corrigé » : re-rends les secondes touchées et regarde les images.

---

## 8. Hors sujet pour une vidéo

À ne pas utiliser, même si la documentation GSAP en parle :

- **ScrollTrigger, ScrollSmoother, ScrollTo** : animation liée au défilement d'une page ;
- **Draggable, Observer, Inertia, `quickTo`** : gestes et suivi de souris ;
- **`gsap.matchMedia()`**, préférences de mouvement réduit : adaptation à l'appareil du visiteur ;
- **intégrations React, Vue, Svelte, Nuxt** (`useGSAP`, nettoyage de composants) ;
- **GSDevTools** : outil de mise au point en direct ;
- conseils de fluidité à 60 i/s en temps réel : en rendu image par image, seule compte la durée du rendu.

Un défilement ou un survol **montré** dans une vidéo est un tween ordinaire sur la timeline (voir les packs `ui`, `lp`, `lp2` du dictionnaire).

---

## Source

Adapté de **greensock/gsap-skills** (MIT, © 2026 GreenSock, commit `aed9cfd`) : skills `gsap-core`, `gsap-timeline`, `gsap-plugins`, `gsap-utils`. Les parties défilement, React et frameworks sont volontairement écartées. Les contraintes de rendu image par image viennent du moteur HyperFrames (Apache 2.0, HeyGen). La bibliothèque GSAP elle-même est distribuée sous sa propre licence gratuite (« Standard No-Charge License »).
