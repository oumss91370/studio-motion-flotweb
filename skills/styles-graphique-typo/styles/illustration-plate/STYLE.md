# Illustration plate à grain

## 1. Identité

- **Nom** : Illustration plate à grain (illustration vectorielle contemporaine).
- **Inspiration** : l'illustration plate des années 2020 qu'on voit dans les applications, les sites et les magazines en ligne : aplats sans contour, personnages à grosse tête, grain pointilliste qui donne du volume, petits signes décoratifs. Aucun illustrateur ni studio précis n'est imité.
- **Ce qui le fait reconnaître** : **des blocs de couleur pure, sans aucun contour** ; les volumes sont séparés par un bloc de la même teinte un cran plus sombre ; un **grain de petits points** plus dense vers le bas ou vers l'ombre ; des personnages simples qui **jouent vraiment** (préparation, action, réaction).
- **Marche pour** : petite scène drôle ou tendre, histoire d'utilisateur, présentation d'un service, vidéo de bienvenue, conseil du quotidien, chute comique en fin de vidéo. C'est le style le plus « passe-partout » de la catégorie.
- **Ne marche pas pour** : sujet grave ou luxueux, démonstration technique précise, données. Sans jeu d'acteur, le style devient un diaporama d'illustrations de banque d'images.

## 2. Palette, typographie, matières

Palette douce, 5 à 6 teintes, chacune en deux valeurs (lumière et ombre). Valeurs relevées dans la source et jeu conseillé :

| Rôle | Couleur |
|---|---|
| Fond clair | crème `#f6efe2` |
| Grande forme de décor | rose poudré `#f4b8b0`, lilas pâle `#d9cdea` |
| Vêtement (lumière / ombre) | `#f08b7d` / un cran plus sombre |
| Animal ou objet chaud (lumière / ombre) | `#f3ad4c` / un arc plus sombre |
| Encre des détails (yeux, bouche) | brun-noir `#2b2320` |
| Lignes d'émotion | rose pâle → rouge vif (elles rougissent avec la tension) |

(Seuls `#f08b7d` et `#f3ad4c` viennent de la source ; le reste est un jeu d'exemple.) Jamais plus de 30 % de l'image en bleu-violet saturé.

- **Polices** (libres) : Caveat 600 pour une signature ou un mot manuscrit ; Poppins ou Nunito pour un titre.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Nunito à la place de Caveat ; Poppins, Nunito : déjà fournies. Aucune police manuscrite n'est fournie : Nunito est un repli de lisibilité, il ne remplace pas l'écriture à la main. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/caveat` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Grain, deux usages** : (1) dans les grandes formes du décor, des points carrés de 2 px dont la **densité dépend de la position** (par exemple de 12 % en haut à près de 90 % en bas d'un disque) ; (2) sur les personnages, une texture de grain fixe appliquée seulement sur eux (5 % de points sombres, 3,5 % de points clairs).
- **Cône de lumière** d'une lampe : des milliers de points, plus denses au centre, qui s'effacent vers le bas.
- **Proportions** : tête agrandie d'environ 1,2 fois autour du cou. Yeux en points ou en arcs, bouche simple, joues roses.

## 3. Composition 9:16

- Une scène simple : un fond uni, une ou deux grandes formes géométriques douces derrière le sujet (disque, bloc arrondi), un sol ou une table, un ou deux accessoires, une plante, une lampe.
- Le personnage principal occupe 40 à 55 % de la hauteur, centré entre y 450 et y 1350. L'objet avec lequel il joue reste dans le même cadre, à moins d'une largeur de personnage.
- Garder de l'air : un tiers de l'image vide ou presque.
- Une quinzaine de **petits signes décoratifs** (croix, points, traits) flottent dans le fond.
- **Texte** : très peu. Un titre de 80 à 110 px en haut (y 200 à 420) ou un mot manuscrit en fin de scène ; sous-titres de 48 à 54 px sur un bandeau arrondi, entre y 1400 et y 1540.
- Rien d'important à droite de x 945.

## 4. Ce qui bouge

- **Action principale** : un geste joué en trois temps. Exemple de la source, un saut d'animal : préparation (le corps s'écrase à 86 % de sa hauteur et s'élargit à 107 % en 4 images), détente (étiré à 112 %), trajectoire en arc, réception (écrasé jusqu'à 70 %, élargi à 118 %), puis redressement avec un léger dépassement (107 % puis 100 %).
- **Boucles de fond** : (1) les objets suspendus et les plantes oscillent après chaque choc, en s'amortissant (une lampe : 0,055 radian, période d'environ 0,45 s) ; (2) les petits signes décoratifs frémissent 4 fois par seconde (±1,5 px ; petite surface seulement), les nuages dérivent (15 px par seconde).
- **Autorisés** : anticipation `#121`, écrasement et étirement `#011`, dépassement `#010`, continuation du mouvement `#122`, rebond `#123`, trajectoire `#126`, éclat `#003` (lignes d'impact), secousse d'impact `#024` légère, tracé de ligne `#004` (signature qui s'écrit), iris `#188`.
- **Interdits** : contours noirs, ombres portées floues, lueur `#022`, dégradés lisses (le volume vient du grain), caméra à l'épaule `#034`, flou de profondeur `#105`, mouvement linéaire sans amorti.
- **L'écrasement se fait autour des pieds**, pas autour du centre : le personnage qui se baisse garde les pieds au sol.
- **Gag en trois coups** : chaque coup = préparation (7 images), frappe (4 images), tenue (4 images), retour (8 images). Le troisième coup déclenche la chute.
- **Expressions par remplacement** : yeux fermés en arc, puis yeux ronds et bouche en « o » (qui apparaît avec un dépassement), puis grands yeux et bouche ouverte. Trois lignes de tension rayonnent au-dessus de la tête.
- Un retournement de personnage se fait **en une image**, au moment où il est le plus écrasé.

## 5. Rythme et montage

- Plan-séquence ou presque : la scène entière tient souvent dans un seul cadre de 4 à 8 s.
- Rythme du gag : calme, montée par trois, chute rapide, puis une tenue de 1 à 2 s sur la réaction.
- Un objet qui tombe accélère (gravité), tourne, laisse des gouttes ou des traits derrière lui ; à l'impact : des lignes qui rayonnent pendant 8 images, des éclats en paraboles, une tache qui s'étale.
- **Transition signature** : un iris à trois anneaux de couleur.
- **Version courte (8 à 12 s)** : un seul cadre : une seule montée du gag (pas trois), la chute, la réaction tenue 1 s. Accroche : l'anticipation du geste avant 2 s.

## 6. Recette technique

- **Moteur** : HyperFrames. Formes en SVG ou canvas 2D ; GSAP convient très bien au jeu d'acteur.
- **Structure** (fichiers **à écrire par l'agent, d'après la description ci-dessous** ; aucun n'est fourni par le plugin) : `decor` (fond et grain mis en cache), `poses.js` (bibliothèque de poses : chaque pose est un jeu de points clés dans le repère du personnage), `jeu.js` (minutage image par image), `environnement.js` (oscillations amorties).

```js
// grain pointilliste : densité = fonction de la position, tirage à graine
function grain(ctx, forme, densite) {
  for (const { x, y } of grilleDansForme(forme, 3)) if (hasard(x, y) < densite(x, y)) ctx.fillRect(x, y, 2, 2);
}
// oscillation amortie d'un objet secoué à l'image i0
const amorti = (i, i0, amp, periode, declin) => i < i0 ? 0 : amp * Math.sin(2 * Math.PI * (i - i0) / periode) * Math.exp(-(i - i0) / declin);
// pose intermédiaire : interpolation point par point entre deux poses
const pose = melanger(ASSIS, SAUT, p);
```

- **Techniques clés** : poses interpolées valeur par valeur ; trajectoires passées par des points de contrôle (courbe lisse) ; pour qu'une patte touche bien sa cible alors que le corps se penche, appliquer d'abord l'inclinaison, puis convertir la cible dans le repère du corps.
- **Pièges** : viser la cible sans tenir compte de l'inclinaison fait manquer le geste de plusieurs dizaines de pixels ; un retournement en deux ou trois images fait « feuille de papier » ; un grain recalculé à chaque image scintille (le mettre en cache).

## 7. Son

- **Musique** : légère et acoustique : ukulélé ou guitare en sourdine, marimba, contrebasse en pizzicato, sifflement, petites percussions. Elle s'arrête ou se suspend juste avant la chute.
- **Bruitages** : les sons du geste (pas feutrés, saut, réception), les objets (tasse qui glisse, qui tombe, qui se brise, liquide), les réactions (petit cri, soupir). Un son par temps du gag.
- **Silence** : une demi-seconde entre le dernier coup et l'impact.
- **Voix** : facultative ; le style fonctionne en muet avec des bruitages.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] Aucun contour : toutes les formes sont des aplats.
- [ ] Le volume vient d'un bloc plus sombre et du grain, pas d'un dégradé lisse.
- [ ] Le grain est fixe (il ne scintille pas) et sa densité varie dans les grandes formes.
- [ ] Chaque geste a une préparation, une action et un retour avec dépassement.
- [ ] Les pieds restent au sol quand le personnage s'écrase.
- [ ] Le décor réagit à l'action (lampe, plante, objets) puis se calme.
- [ ] Les expressions changent au moins deux fois dans la scène.
- [ ] Le sujet et l'objet de son action sont dans la zone utile.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : fixe
- Couleurs max : 12
- Bleu-violet : interdit
- Texte vivant : non
- Taille mini du texte : 48

## 9. Aperçu

- Planche d'ensemble des styles d'origine (image fixe, 16:9) : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg
- Film de démonstration complet : https://github.com/alchaincyf/huashu-art-motion/releases
- Crédit : 花叔 Huashu (alchaincyf), https://github.com/alchaincyf/huashu-art-motion. Planche donnée en lien seulement (sa composition et sa scène s'inspirent d'un film tiers ; on ne refait pas cette scène).

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichiers `references/风格配方/16_2026.md` et `scripts/engine/scenes/16_2026.js`.
- Licence : MIT (© 2026 alchaincyf, 花叔). Police Caveat : OFL 1.1.
- Adaptation Flot Web : traduction du chinois, règles de jeu d'acteur généralisées (la scène et les personnages de la démo ne sont pas repris), jeu de couleurs d'exemple, composition verticale, portage vers HyperFrames, numéros de mouvements, section son.
