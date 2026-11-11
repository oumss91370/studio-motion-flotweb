---
name: styles-graphique-typo
description: "Catégorie de styles « Graphique et typo » (15 styles : grille suisse, générique d'espionnage années 60, Art déco, plan bleu, vitrail, pictogrammes, terminal ASCII, Bauhaus, constructivisme, cubisme, illustration plate, typo cinétique, Art nouveau, bonshommes au trait épais, pois infinis). À utiliser quand le client veut une vidéo dont l'image est faite de formes, de lettres et d'affiches plutôt que de dessin réaliste ou de 3D."
---

# Styles « Graphique et typo »

Cette catégorie regroupe les styles où **la forme graphique et la lettre font l'image** : affiches qui bougent, grilles, pictogrammes, écrans de caractères, mouvements d'art géométriques. Ils sont presque tous en 2D pure, donc rapides à rendre et très lisibles sur téléphone.

Ce skill ne pilote pas la vidéo. Le parcours (questions, histoire, look, storyboard, construction, revue, livraison) est dans `studio-coeur`. Les règles de mouvement et le dictionnaire des 192 mouvements (numéros `#001` à `#192` cités dans les fiches) sont dans `principes-mouvement`. L'export est dans `rendu`, le son dans `son`, la 3D dans `blender`. Ici on trouve seulement **le look et sa recette**.

## Les 15 styles

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `typo-suisse` | Grille suisse | Une grille, une police, une couleur signal, tout claque sur le temps | hyperframes | facile | [film](https://lemomo-ai.github.io/lemo-opuscar/films/swiss-motion.mp4) |
| `generique-espion-60` | Générique d'espionnage années 60 | Papier découpé 4 encres, silhouettes, décors faits de lettres | hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/spy-titles.mp4) |
| `art-deco` | Art déco | Laque noire, filets d'or, axe central, ampoules qui s'allument | hyperframes (blender possible) | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/art-deco.mp4) |
| `plan-bleu` | Plan bleu (dessin technique) | Traits blancs sur papier bleu, tracés dans l'ordre du dessinateur | hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/blueprint.mp4) |
| `vitrail` | Vitrail | Verre coloré serti de plomb, vivant seulement là où passe le soleil | hyperframes (WebGL) | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/stained-glass.mp4) |
| `pictogrammes` | Pictogrammes en rythme | Motif en grille, pictogrammes géométriques, gros titres, une coupe par temps | hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/pictogram-motion.mp4) |
| `terminal-ascii` | Terminal ASCII | Tout est un caractère sur une grille, éclairé par un vieil écran | hyperframes (WebGL) | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/ascii-crt.mp4) |
| `bauhaus` | Bauhaus | Cercle, carré, triangle, trois couleurs primaires, papier vieilli | hyperframes | facile | [planche](https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg) |
| `constructivisme` | Constructivisme | Rouge, noir, diagonales, photo tramée, slogan tamponné | hyperframes | moyenne | [planche](https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg) |
| `cubisme` | Cubisme | Plans transparents qui se croisent, sujet découpé en facettes | hyperframes | élevée | [planche](https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg) |
| `illustration-plate` | Illustration plate à grain | Aplats sans contour, grain pointilliste, vrai jeu d'acteur | hyperframes | moyenne | [planche](https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg) |
| `typo-cinetique` | Typo cinétique | Le mot est l'acteur : il tombe sur le temps, un seul point d'attention | hyperframes | facile | [planche](https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/动画语法/y5_kinetic_type_总览.jpg) |
| `art-nouveau` | Art nouveau | Lignes en coup de fouet, halo, fleurs, contour épais dehors et fin dedans | hyperframes | élevée | [planche](https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg) |
| `bonshommes-trait-epais` | Bonshommes au trait épais (style Haring) | Gros trait noir uniforme, aplats vifs, tout danse à 8 images par seconde | hyperframes | facile | [planche](https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg) |
| `pois-infinis` | Pois infinis (style Kusama) | Tout est couvert de pois qui gonflent en ondes depuis un point | hyperframes | facile | [planche](https://github.com/alchaincyf/huashu-art-motion/blob/main/assets/全风格总览.jpg) |

Les aperçus sont ceux des auteurs d'origine (crédits dans chaque fiche, section 9, et dans `licenses/styles-graphique-typo.md`). Ils sont en 16:9 : ils montrent le look, pas le cadrage vertical. Les noms « style Haring », « style Kusama » désignent une inspiration, jamais une œuvre officielle ni une affiliation.

## Comment choisir

Pose une seule question au client si le style n'est pas déjà choisi : « quel est le sujet, et quelle impression doit rester ? ». Puis :

| Le client veut… | Propose d'abord | Puis |
|---|---|---|
| Une liste, des chiffres, une phrase choc, une ouverture de vidéo | `typo-cinetique` | `typo-suisse`, `pictogrammes` |
| Une identité de marque sobre, un événement culturel, une leçon de design | `typo-suisse` | `bauhaus` |
| Un catalogue (N produits, N étapes, N conseils) | `pictogrammes` | `typo-cinetique` |
| Expliquer comment un objet est fait, un projet, une invention | `plan-bleu` | (catégorie explicatif) |
| Du luxe, une soirée, une invitation, un compte à rebours | `art-deco` | `art-nouveau` |
| Une ouverture de film, une bande-annonce, une poursuite | `generique-espion-60` | `constructivisme` |
| Un conte, une légende, un patrimoine, une histoire en chapitres | `vitrail` | `art-nouveau` |
| Un outil pour développeurs, de la science-fiction, un journal de bord | `terminal-ascii` | |
| Un manifeste, un appel, une annonce qui frappe | `constructivisme` | `bonshommes-trait-epais` |
| Une petite scène drôle avec un personnage | `illustration-plate` | `bonshommes-trait-epais` |
| Beauté, bien-être, thé, parfum, fleurs | `art-nouveau` | |
| De l'énergie, de la danse, de la fête, un public jeune | `bonshommes-trait-epais` | `pois-infinis` |
| Un visuel hypnotique, une boucle, un fond de clip | `pois-infinis` | `cubisme` |
| Un sujet « vu sous plusieurs angles », un portrait d'artiste | `cubisme` | |

Trois règles pour trancher :
1. **Débutant ou délai court** : reste dans les styles « facile » (`typo-cinetique`, `typo-suisse`, `bauhaus`, `bonshommes-trait-epais`, `pois-infinis`).
2. **Un personnage doit jouer** : `illustration-plate`, `generique-espion-60`, `art-deco`, `vitrail`. Les autres n'ont pas de visage.
3. **Beaucoup de texte à lire** : `typo-suisse`, `plan-bleu`, `pictogrammes`. Jamais `cubisme` ni `pois-infinis`.

**Voir aussi (fiches portées par une autre catégorie)**, pour ne pas se tromper de fiche : le montage de vraies images à la manière constructiviste est `montage-constructiviste` dans `styles-montage-documentaire` (ici, `constructivisme` est une affiche dessinée) ; les papiers découpés et les affiches en sérigraphie sont dans `styles-papier-impression` ; le pixel art et le néon sont dans `styles-jeu-retro` ; les deux keynotes (`keynote-sombre`, `keynote-produit`) et le tableau blanc à la main sont dans `styles-explicatif-infographie`. Dans l'autre sens, des fiches d'ici servent à d'autres catégories, qui y renvoient : `typo-cinetique` (`styles-explicatif-infographie`, `styles-lancement-produit`, `styles-montage-documentaire`) ; `art-nouveau`, `bauhaus`, `constructivisme` (`styles-papier-impression`, `styles-peinture-dessin`).

## Ce qui vaut pour toute la catégorie

- **Format** : 1080×1920, 30 images par seconde. Zone utile : x de 60 à 945, y de 160 à 1560 (rien d'important dans les 160 px du haut, les 360 px du bas ni les 135 px de droite). Les sources sont en 16:9 : chaque fiche donne la mise en page verticale, qui est une **nouvelle composition**, jamais un recadrage.
- **Moteur** : HyperFrames. Les styles dessinés sur canvas suivent un seul schéma : une fonction `dessiner(t)` qui ne dépend que du temps, appelée par la timeline.

```html
<canvas id="toile" width="1080" height="1920"></canvas>
<script>
  const etat = { t: 0 }, DUREE = 30;
  const tl = gsap.timeline({ paused: true });
  tl.to(etat, { t: DUREE, duration: DUREE, ease: "none", onUpdate: () => dessiner(etat.t) });
  window.__timelines["scene"] = tl;   // même t = même image, au pixel près
</script>
```

- **Déterminisme** : aucun `Math.random()` sans graine, aucun `Date.now()`, aucun état gardé d'une image à l'autre. Tout tirage au sort passe par une fonction à graine (`hasard(graine)`).
- **Animation « en 2 »** : quand une fiche dit 12 ou 8 images par seconde (valeurs des sources, à 24 i/s), joue 15 ou 10 à 30 i/s (`t2 = Math.floor(t * 15) / 15` ; règle « Cadence saccadée à 30 i/s » de `principes-mouvement`). Seuls les personnages et les objets sont saccadés. La caméra, la lumière et les tracés restent fluides, sinon l'image tremble.
- **Grain et texture de pellicule** : jamais dans la page, toujours à l'export (voir `rendu`).
- **Temps de lecture** : règle commune de la porte de livraison (`studio-coeur/references/controles.md`, section 2). Ces styles posent du texte à lire : lance le contrôle avec `--strict` (caractères ÷ 15 + 1,5 s, jamais moins de 1,5 s, texte entier et immobile). Un sous-titre **en phrase entière** tient en plus la durée de la phrase dite + 0,6 s ; des sous-titres au mot suivent la règle de la porte (0,7 s au moins, 17 caractères par seconde au plus).
- **Son** : mixage à −14 LUFS, vrais enregistrements d'abord, environ 5 bruitages pour 10 secondes, au moins un vrai silence avant le moment fort. Les fiches disent quels sons vont avec la matière du style ; le budget et le mixage sont dans `son`.
- **Droits** : les références citées (affichistes, mouvements, films) servent à comprendre la grammaire. On ne recopie jamais une affiche, un logo, un personnage, un lettrage ou une mélodie existants.
- **Histoire d'abord** : la fiche fixe le look. L'histoire, les plans et la durée viennent du sujet du client, jamais de la démo d'origine.

## Lire une fiche

Chaque style est dans `styles/<identifiant>/STYLE.md`, avec dix sections fixes : identité, palette et matières, composition 9:16, ce qui bouge, rythme, recette technique, son, liste de contrôle, aperçu, origine. Lis la fiche en entier avant d'écrire le storyboard, puis rends **une image de style** (une seule image fixe au vrai format) et vérifie-la avec la liste de contrôle de la section 8 avant d'animer.
