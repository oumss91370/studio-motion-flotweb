# Cubisme

## 1. Identité

- **Nom** : Cubisme (cubisme analytique, vers 1912).
- **Inspiration** : le cubisme analytique : un sujet vu de plusieurs côtés à la fois, découpé en plans qui se traversent, dans des bruns et des gris ; lettres au pochoir, faux bois, morceau de journal collé. « Cubisme » désigne le mouvement ; on ne reproduit aucun tableau.
- **Ce qui le fait reconnaître** : des **plans semi-transparents qui se chevauchent**, chacun avec un côté clair et un côté sombre ; une palette **terreuse** ; de longues lignes droites qui traversent tout ; le sujet **découpé en facettes triangulaires** dont certaines dépassent du contour ; un œil de face sur un visage de profil ; des lettres au pochoir.
- **Marche pour** : portrait d'artiste ou de créateur, sujet « vu sous plusieurs angles », musique, café, littérature, ouverture d'un contenu culturel, visuel d'ambiance pour une marque d'art.
- **Ne marche pas pour** : tout ce qui doit être compris vite : tutoriel, chiffres, produit à reconnaître, texte à lire. Usage **ponctuel** : un plan ou une séquence, rarement un film entier. Défaut connu de la source : rendu trop clair par rapport aux originaux, il faut assombrir.

## 2. Palette, typographie, matières

| Rôle | Couleur |
|---|---|
| Papier | `#d6c8ac` |
| Crème | `#ece3cf` |
| Ocre | `#b8975f` |
| Brun / brun profond | `#6e5538` / `#3a2c1e` |
| Gris / gris sombre | `#a8a395` / `#5a5852` |
| Gris-bleu | `#8e9eab` |
| Vue par la fenêtre (bleus gris) | `#c9d3da`, `#8fa3b3`, `#6f8597`, `#5f7385` |
| Chair / cheveux clairs | `#e2cfae` / `#c9a256` |
| Vêtement, deux valeurs | `#6a7a8b` et `#3c4857` |

- Deux éléments qui se touchent doivent avoir des **valeurs différentes** (une manche plus sombre que la robe), sinon ils fondent l'un dans l'autre une fois découpés en facettes.
- **Polices** (libres) : Alfa Slab One pour les lettres au pochoir (104 px dans la source), Libre Baskerville 700 pour le faux journal.
- **Police de repli** (fournie par HyperFrames, se charge par son nom) : Archivo Black à la place d'Alfa Slab One ; EB Garamond à la place de Libre Baskerville. Graisses fournies : 400 et 700 (900 pour quelques familles), romain seulement, pas d'italique ; liste exacte dans le skill `rendu`, section « Polices ».
- **Où la prendre** : `@fontsource/alfa-slab-one`, `@fontsource/libre-baskerville` (paquets vérifiés par `npm view` le 11/11/2026 ; accents français présents dans les fichiers) ; copier les `.woff2` dans `assets/fonts/` et les déclarer en `@font-face`.
- **Matières** : plans en dégradé (25 % de crème d'un côté, 40 % de brun profond de l'autre, opacité de 0,18 à 0,7) ; quelques plans pointillés (grille en losange de 9 px) et hachurés (lignes à 7 px) ; des milliers de petits traits courts (3 à 8 px) qui donnent une texture de « brique » ; faux bois (lignes ondulées avec des nœuds) ; chaise cannée (points en losange).

## 3. Composition 9:16

- Le fond est construit en couches : une quinzaine de **grands plans placés à la main**, des éventails de plans qui rayonnent depuis un point bas, puis 70 petits triangles et quadrilatères au hasard (avec une graine), puis une quarantaine de **lignes droites fines qui traversent toute l'image**.
- En vertical : empiler les motifs (une fenêtre en haut, le sujet au centre entre y 500 et y 1300, une table et ses objets en bas) et laisser les lignes traverser de haut en bas.
- Le sujet reste **identifiable par sa silhouette** : taille des facettes d'environ 58 px pour un personnage, 26 px pour les petites zones (cheveux, animal). Plus fin, on obtient un modèle 3D en polygones, pas du cubisme.
- **Texte** : un mot court au pochoir (4 à 6 lettres), 110 à 150 px, dans une zone dégagée du haut de l'image. Ce style ne porte pas de phrase : la voix ou un sous-titre sobre (bandeau crème, texte brun, 48 px, entre y 1400 et y 1540) s'en charge.
- Garder une zone calme sans petits fragments là où se pose le texte.

## 4. Ce qui bouge

- **Action principale** : les points de vue glissent. Une même vue (une fenêtre, un paysage) est montrée dans quatre cases, chacune décalée différemment (±18 px à l'horizontale, ±8 px à la verticale) : c'est l'assemblage de plusieurs regards.
- **Boucles de fond** : (1) les lettres au pochoir sautent 10 fois par seconde (chaque lettre bouge de ±13 px et tourne de ±6° : petite surface seulement, un mot de 4 à 6 lettres) et **changent d'ordre 3 fois par seconde au plus** ; (2) les facettes du sujet « bouillonnent » 10 fois par seconde **par leur géométrie** (sommets déplacés de ±8 % de la cellule), mais leurs **changements de valeur** (16 à 35 % des triangles, ±12 %) se font **3 fois par seconde au plus**. Pourquoi : la source faisait tout changer 8 et 12 fois par seconde ; un changement de luminosité répété plus de 3 fois par seconde sur une grande surface est un clignotement, risque pour les personnes photosensibles. (10 par seconde = une image sur trois à 30 i/s.)
- **Autorisés** : éclatement `#142` et réassemblage, tremblement du trait `#136`, style image par image `#128`, texte brouillé `#129`, double exposition `#120`, plan fixe `#175`, coupe par morphing `#186`, tremblement `#124` léger (le journal frémit, son coin se replie).
- **Interdits** : orbite 3D `#030` (le cubisme montre plusieurs angles **à plat**), flou de profondeur `#105`, lueur `#022`, couleurs saturées, rebond `#123`, zoom rapide `#020`.
- Quelques plans transparents posés **par-dessus** le sujet glissent lentement (±8 px) : ils l'incrustent dans l'espace au lieu de le laisser collé sur le fond.

## 5. Rythme et montage

- Contemplatif et saccadé à la fois : la caméra ne bouge pas, ce sont les fragments qui frémissent, 10 fois par seconde (géométrie seulement ; les valeurs changent 3 fois par seconde au plus).
- Plans de 3 à 6 s.
- **Transition signature** : l'image se brise en fragments qui se réassemblent en la suivante (environ 0,25 s).
- Convient à une séquence de 5 à 15 s dans un film plus classique.

## 6. Recette technique

- **Moteur** : HyperFrames, canvas 2D avec `dessiner(t)`.
- **Structure** : fond mis en cache une fois ; vue « fenêtre » dans une image à part ; calque du sujet dessiné en aplats, puis passé dans le découpeur en facettes ; retouches de structure par-dessus.

```js
function plan(ctx, pts, couleur, alpha) {                 // un plan = un dégradé clair → sombre
  const g = ctx.createLinearGradient(pts[0].x, pts[0].y, pts[autre].x, pts[autre].y);
  g.addColorStop(0, melange(couleur, "#ece3cf", .25)); g.addColorStop(.5, couleur); g.addColorStop(1, melange(couleur, "#3a2c1e", .4));
  ctx.globalAlpha = alpha; ctx.fillStyle = g; tracer(ctx, pts); ctx.fill();
}
// découpeur : le sujet en aplats → triangles colorés au centre, NON rognés (ils débordent du contour)
function facettes(calque, cellule, t) {
  const pas = Math.floor(t * 10);                          // bouillonnement de la géométrie, 10 par seconde, tiré à la graine
  const pasValeur = Math.floor(t * 3);                     // changements de valeur : 3 par seconde au plus (sécurité)
  maillageTriangles(calque, cellule, pas).forEach(tri => { if (alphaAuCentre(calque, tri) >= 120) peindre(tri, couleurAuCentre(calque, tri)); });
}
```

- **Techniques clés** : après le découpage, **redonner de la structure** : deux plans de chair clair et sombre sur le visage, l'œil de face, des lignes de contour droites dont chaque bout dépasse de 10 à 16 px ; lettres au pochoir obtenues en creusant des fentes dans les lettres (`destination-out`), ce qui laisse voir les plans derrière.
- **Pièges** : **non-déterminisme** : un calque hors écran qu'on relit en pixels ne donne pas la même première image que les suivantes ; créer ce calque avec l'option de lecture fréquente et le **réinitialiser entièrement** à chaque image (pixels et état), pas seulement l'effacer ; cellule trop petite (34 px) = aspect « polygones 3D » ; un second découpage fin par zone ronde déborde sur le visage (filtrer par couleur).

## 7. Son

- **Musique** : piano seul, guitare, clarinette ou accordéon, dans un esprit de café du début du XXᵉ siècle ; phrases courtes, interrompues, reprises décalées, comme les fragments de l'image.
- **Bruitages** : papier journal froissé, tasse et soucoupe, chaise en bois, pochoir et brosse, fragments qui s'entrechoquent comme du carton.
- **Silence** : une respiration entière avant le réassemblage.
- **Voix** : posée, proche, peu de mots.
- **Sons absents de la banque** : la banque du plugin n'a ni matières, ni instruments, ni musique. Pour chaque son demandé ci-dessus, suivre `skills/son/references/sons-manquants.md` (chercher le vrai son, sinon le plus proche, sinon rien) ; pour un fond sonore de repli quand le film n'a ni voix ni musique, `skills/son/fonds/`. Le niveau final se règle après le rendu avec `skills/son/scripts/finaliser.py`.

## 8. Erreurs fréquentes et liste de contrôle

- [ ] La palette est terreuse (bruns, ocres, gris, gris-bleu) et assez sombre.
- [ ] Les plans sont semi-transparents et se chevauchent ; chacun a un côté clair et un côté sombre.
- [ ] De longues lignes droites traversent toute l'image.
- [ ] Le sujet se reconnaît en silhouette, et des facettes dépassent de son contour.
- [ ] Au moins un détail montre deux points de vue (œil de face sur profil, vue répétée et décalée).
- [ ] Les lettres au pochoir et les facettes bougent par à-coups ; la caméra ne tourne jamais autour du sujet.
- [ ] La même seconde rendue trois fois donne trois images identiques.

**Réglages des contrôles**
- Mouvement : calme
- Caméra : fixe
- Couleurs max : 16
- Bleu-violet : interdit
- Texte vivant : oui
- Taille mini du texte : 48

## 9. Aperçu

- Planche d'ensemble des styles d'origine (image fixe, 16:9) : https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg
- Film de démonstration complet : https://github.com/alchaincyf/huashu-art-motion/releases
- Crédit : 花叔 Huashu (alchaincyf), https://github.com/alchaincyf/huashu-art-motion. Style noté 2 étoiles sur 3 par son auteur (reconnaissable, avec des défauts). Planche donnée en lien seulement.

## 10. Origine

- Dépôt `alchaincyf/huashu-art-motion`, commit `1468196` (version 1.3.0), fichiers `references/风格配方/11_cubism.md` et `scripts/engine/scenes/11_cubism.js`.
- Licence : MIT (© 2026 alchaincyf, 花叔). Polices Alfa Slab One et Libre Baskerville : OFL 1.1.
- Adaptation Flot Web : traduction du chinois, retrait de la scène et des personnages de la démo, composition verticale, portage vers HyperFrames, numéros de mouvements, section son.
