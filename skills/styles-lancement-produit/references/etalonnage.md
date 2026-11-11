# Étalonnage et finition d'une vidéo de produit

Règle d'or : **c'est un étalonnage, pas un filtre. Si le spectateur peut nommer l'effet, il est trop fort.** Personne ne doit finir la vidéo en pensant « joli grain ».

Les couleurs d'exemple (violet `#b04adc`, orange `#ff7247`) sont celles du film d'origine : remplace-les par la palette de la fiche « ma chaîne » en suivant la section 7.

## 1. Les fonds d'abord, les effets ensuite

Construire les **deux registres** avec zéro effet par-dessus : un étalonnage ne sauve pas un fond plat, il le rend juste granuleux.

- **Registre clair (le produit)** : une couleur de base presque blanche, deux nappes radiales de marque très douces dans les deux coins du haut, et en option une grille de points à ~3 % d'encre.
```css
.fond       { position:absolute; inset:0; background:#fafafb; overflow:hidden; }
.fond-nappe { position:absolute; inset:0; background:
    radial-gradient(ellipse 62% 52% at 20% 10%, rgba(176,74,220,0.06), transparent 60%),
    radial-gradient(ellipse 52% 46% at 88%  8%, rgba(255,114,71,0.05), transparent 65%); }
.fond-points{ position:absolute; inset:0; background-size:28px 28px;
    background-image: radial-gradient(circle, rgba(16,14,25,0.03) 1px, transparent 1px); }
```
- **Registre sombre (l'argument : affirmation, preuve, appel à l'action)** : base presque noire, une nappe de marque qui tombe d'au-dessus du cadre, et une grande ellipse douce qui fait du cadre une scène éclairée.
```css
.fond--sombre { position:absolute; inset:0; background:
    radial-gradient(ellipse 78% 74% at 50%  44%, rgba(0,0,0,0) 42%, rgba(0,0,0,0.34) 100%),
    radial-gradient(ellipse 66% 52% at 50% -14%, rgba(176,74,220,0.11) 0%, rgba(176,74,220,0) 62%),
    #100e19; }   /* pas #000 : voir « noirs relevés » */
```

Ces opacités (0,06 ; 0,05 ; 0,03) paraissent absurdes écrites, et elles sont justes : c'est une décision de **lumière**, on ne doit pas pouvoir montrer du doigt où elle commence.

- **Deux fonds, pas trois.** Chaque plan est l'un ou l'autre ; la bascule de l'un à l'autre est elle-même un temps fort.
- **De la lumière, pas une capture floutée** : une capture floutée reste reconnaissable, le spectateur essaie de la lire, et elle change à chaque plan.
- Le fond est dans **son propre calque**, jamais sur le nœud que la caméra déplace (sinon la lumière glisse).

## 2. Aurore (pour un long plan de texte seul)

Trois larges nappes aux teintes de la marque, débordant du cadre (`inset:-8%`), avec **une seule** dérive lente amortie aux deux bouts : environ 28 px en quatre secondes. Si on la voit bouger, elle est trop rapide. Elle bat les particules et les formes flottantes parce qu'elle ne peut pas croiser le texte : elle **est** son fond, à 11-20 % d'opacité, sans bord dur.

## 3. Du verre qui se rend vraiment

`backdrop-filter: blur()` ne sert à rien quand chaque piste se compose à part : il n'y a rien derrière à flouter. Le remplaçant : **deux anneaux** dessinés avec l'astuce `padding` + masque (`mask-composite: exclude`), pour ne peindre que la bande de marge : une bande irisée douce de 14 px pour le givre, plus un filet dégradé de 1,5 px au bord. Le verre vit **à l'intérieur** de la boîte de la carte, pas en plaque derrière elle (une plaque extérieure agrandit les limites visuelles et peut sortir de la zone sûre pendant une poussée). On anime son opacité, pas sa géométrie.

## 4. La passe d'étalonnage : trois traitements sur une seule piste

Une piste de surimpression couvrant tout le film, posée après l'assemblage. Elle relève tous les plans d'un coup.

| Traitement | Corrige | Force qui se lit |
|---|---|---|
| Grain qui bouge | l'aplat numérique « image de synthèse propre » | opacité 0,1 sur une plaque de mouchetures noires |
| Vignette | l'œil qui se promène, les coins ouverts | 0,15 dans les coins (0,06 à 78 % du rayon) |
| Balayage spéculaire | des temps forts sans ponctuation | pic de blanc 0,11 ; trois passages en 45 s |

```html
<div id="etalonnage" class="clip" data-start="0" data-duration="45" data-track-index="990"
     style="position:absolute;inset:0;z-index:9000;pointer-events:none">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse 78% 74% at 50% 48%,
       rgba(8,6,14,0) 44%, rgba(8,6,14,0.060) 78%, rgba(8,6,14,0.15) 100%)"></div>
  <div id="balayage" style="position:absolute;top:-24%;left:0;width:40%;height:148%;opacity:0;
       background:linear-gradient(90deg, rgba(255,255,255,0), rgba(255,255,255,0.11) 50%, rgba(255,255,255,0))"></div>
  <svg id="grain" width="1080" height="1920" style="position:absolute;inset:0;opacity:0.1">
    <filter id="bruit" x="0" y="0" width="100%" height="100%">
      <feTurbulence id="turb" type="fractalNoise" baseFrequency="0.82" numOctaves="1" seed="1" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0.34 0.34 0.34 0 0"/>
    </filter>
    <rect width="1080" height="1920" filter="url(#bruit)"/>
  </svg>
</div>
```

**Lire la matrice de couleur** : les trois premières lignes à zéro forcent le rouge, le vert et le bleu au noir ; la quatrième envoie **la luminance du bruit dans la transparence**. Le bruit clair devient une moucheture noire opaque, le bruit sombre devient transparent : la composition simple fait alors le travail qu'on demanderait à un mode « multiplier ». `numOctaves=1` garde le grain fin ; `baseFrequency` plus bas se lit comme de la fumée.

Garder la vignette faible : la même piste couvre aussi le registre clair, où une vignette lourde fait sale.

## 5. Le piège des modes de fusion

**Aucun `mix-blend-mode` dans une piste de surimpression. Composition par transparence seulement.**

Chaque piste `.clip` se compose comme son propre calque : une piste de surimpression n'a **pas le film derrière elle**, elle se mélange à de la transparence. Une vignette en « multiplier » sur rien ne fonce rien : elle peint sa propre couleur. La première version du film d'origine a rendu **le film entier en voile blanc** à cause d'une seule déclaration.

Même raisonnement pour : `backdrop-filter` (rien à filtrer derrière), `filter: contrast()` / `saturate()` posé sur la surimpression (il filtre la surimpression, pas le film), et les reflets en mode écran, incrustation ou lumière douce. Si l'on veut un mode de fusion, on déplace l'effet **dans le plan**, là où il a un fond, ou on le réécrit en transparence comme le grain.

## 6. Grain contre compression

**Changer la graine du grain à 12 Hz, pas à chaque image.** Une graine par image a fait passer un rendu de ~9 Mo à **85 Mo** et se lisait comme un grésillement électronique : un bruit neuf à chaque image détruit la compression entre images. Le vrai grain de pellicule tient plus d'une image : 12 Hz est à la fois le look honnête et le moins cher. La graine se calcule depuis la tête de lecture :

```js
const horloge = {t: 0}; let derniere = -1;
tl.to(horloge, {t: TOTAL, duration: TOTAL, ease: "none", onUpdate() {
  const graine = Math.floor(horloge.t * 12) % 12;          // fonction pure du temps
  if (graine !== derniere) { derniere = graine; turb.setAttribute("seed", String(graine)); }
}}, 0);
```

**Réencoder le master** : `-c:v libx264 -preset slow -crf 19 -tune film` a fait passer un rendu de 68 Mo à **38 Mo sans perte visible** (`-tune film` préserve le grain au lieu de l'étaler). Le faire dans la même passe que la normalisation du son (voir `son-et-mastering.md`).

## 7. Contrôle du contraste : étalonnage coupé, livraison étalonnage allumé

Une surimpression plein cadre fausse la mesure automatique du contraste (le film d'origine a obtenu 1,06:1 sur un texte parfaitement lisible). Ne pas affaiblir l'étalonnage, ne pas désactiver le contrôle : **contrôler le contraste sans la piste d'étalonnage, livrer avec.** Prévoir donc de pouvoir retirer et remettre la piste en une commande.

## 8. Les balayages spéculaires sont de la ponctuation

Un passage par **temps fort nommé de l'histoire**, jamais une boucle. Trois en 45 secondes : l'affirmation, la preuve, l'appel à l'action. Un balayage sur minuterie est un écran de veille ; un balayage sur un temps fort est une ponctuation.

```js
gsap.set(balayage, {skewX: -14});
[{t: 7.92, d: 0.90}, {t: 24.62, d: 0.90}, {t: 40.17, d: 0.95}].forEach(s => {
  tl.fromTo(balayage, {opacity: 0}, {opacity: 1, duration: 0.14}, s.t);
  tl.fromTo(balayage, {xPercent: -140}, {xPercent: 260, duration: s.d, ease: "power2.inOut"}, s.t);
  tl.to(balayage, {opacity: 0, duration: 0.2}, s.t + s.d - 0.2);
});
```

**L'astuce de l'inclinaison** : ne pas incliner le dégradé (un axe à 115° donne une couture dure en diagonale). Garder l'axe du dégradé à **90°** et incliner **l'élément** (`skewX: -14`), avec `top:-24%; height:148%` pour que les coins inclinés n'entrent jamais dans le cadre. Le trajet de −140 à 260 % sur une boîte large de 40 % va d'un hors-champ à l'autre.

Le balayage marche aussi **dans** un plan, à l'échelle d'une carte : une barre blanche de 110 px, une seule fois, quand la carte se pose.

## 9. Règles de retenue

- **Le halo lumineux sur une interface presque blanche explose** (nuage blanc illisible) : le garder pour le registre sombre.
- **Aberration chromatique** : seulement sur un filé rapide, une traversée d'échelle ou une seule image d'impact, à une force qu'il faut chercher pour la voir. Jamais sur du texte tenu.
- **Noirs relevés** : aucun noir pur. Fond sombre `#100e19`, encre de vignette `rgba(8,6,14,…)`, tous deux légèrement bleutés. Les noirs écrasés sont le signe le plus net du « fait dans un navigateur ».
- **La courbe de contraste vit dans le plan**, sur son fond ou sa scène, pas sur la surimpression. Le mieux : aucune courbe, le contraste vient de la palette à deux registres (cela ne peut pas sortir le texte des seuils de lisibilité).

## 10. Dériver sa palette depuis la marque

| Emplacement | Comment le dériver | Exemple |
|---|---|---|
| Accent | la couleur principale de la marque | `#b04adc` |
| Accent 2 | la secondaire, ou la principale tournée vers un complément chaud ; **en dégradé seulement**, jamais en aplat seul | `#ff7247` |
| Accent clair | la principale éclaircie de ~15 % (troisième nappe de l'aurore) | `#c77dea` |
| Encre | la principale désaturée et foncée jusqu'au presque noir | `#100e19` |
| Fond clair | blanc cassé portant une trace de la teinte de l'encre ; garder `#fff` pour les cartes | `#fafafb` |
| Gris de texte | un seul neutre pour tout le texte secondaire | `#4b5563` |
| Accent lisible | l'accent foncé jusqu'à passer 4,5:1 sur blanc : petits textes et surtitres | `#9a3fc4` |

- **L'accent lisible n'est pas optionnel** : la plupart des couleurs de marque échouent à 4,5:1 sur blanc.
- **Une troisième teinte est presque toujours une erreur** : un plan qui semble demander une autre couleur demande en général une autre **valeur** (un ton plus clair de l'accent, ou le gris). Seuls ajouts légitimes : un vert de succès, un rouge d'erreur, une fois chacun dans tout le film.
- Marque à une seule couleur : pas d'accent 2 ; dégradés accent → accent clair → blanc. Ne jamais inventer une seconde couleur de marque.

Origine : AbubakrChan/product-launch-motion, commit `edbfb10`, `legacy/references/06-look-and-grade.md` (MIT). Réécrit en français par Flot Web ; dimensions adaptées au 1080×1920.
