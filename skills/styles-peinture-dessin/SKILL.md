---
name: styles-peinture-dessin
description: "Catégorie de styles « Peinture et dessin » du studio motion (craie grasse, aquarelle, huile au couteau, trait continu, tableau blanc, tableau noir, croquis urbain, carnet de croquis, encre et hachures, et les styles de peinture d'histoire de l'art : tourbillons style Van Gogh, impressionnisme, nénuphars, pointillisme, période dorée, clair-obscur, sfumato, expressionnisme, surréalisme, lumière de diner, enluminure). À utiliser quand le client veut une vidéo qui a l'air peinte ou dessinée à la main, ou dit « style peinture », « style aquarelle », « dessiné au tableau », « style Van Gogh »."
---

# Styles Peinture et dessin (catégorie 1)

Vingt styles où **l'image est faite à la main sous les yeux du spectateur** : un trait qui s'écrit, une touche qui se pose, un lavis qui s'étale. Le geste de fabrication est le spectacle. Si le client veut des aplats propres et de la typo, regarde plutôt « Graphique et typo » ; s'il veut de l'encre de Chine ou une estampe, « Encre et Asie » ; s'il veut une image imprimée (trame, gravure, sérigraphie), « Papier et impression ».

Le skill `studio-coeur` pilote le parcours (questions, histoire, look, storyboard, construction, revue, livraison). Les skills `principes-mouvement` (dictionnaire des mouvements, cités ici par leur numéro `#NNN`), `rendu` (HyperFrames, export) et `son` (mix à −14 LUFS, vrais enregistrements d'abord, environ 5 bruitages par 10 s) s'appliquent à tous les styles. Cette catégorie ne décrit que ce qui est propre à chaque look.

## Les styles

### Dessin (le trait raconte)

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `craie-grasse-album` | Craie grasse, album jeunesse | Page d'album dessinée en direct à la craie grasse ; un lavis révèle ce que la craie blanche cachait | hyperframes (canvas + passe WebGL) | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/crayon-book.mp4) (LemoLab, CC BY 4.0) |
| `trait-continu` | Trait continu | Une seule ligne d'encre qui ne quitte jamais le papier ; pas de coupe, les scènes se métamorphosent | hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/one-line.mp4) (LemoLab, CC BY 4.0) |
| `tableau-blanc` | Tableau blanc | Explication écrite trait par trait au feutre, sans main, aimants, effaceur, caméra qui voyage | hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/whiteboard.mp4) (LemoLab, CC BY 4.0) |
| `tableau-noir-craie` | Tableau noir à la craie | La craie écrit seule ; on écrit l'idée reçue, on l'efface d'un passage, on écrit le vrai | hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/chalkboard.mp4) (LemoLab, CC BY 4.0, image seule) |
| `croquis-urbain` | Croquis urbain, plume et lavis | Feutre sépia tremblé qui ne ferme pas ses formes, aquarelle posée un peu à côté du trait | hyperframes (canvas + passe WebGL) | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/urban-sketch.mp4) (LemoLab, CC BY 4.0) |
| `carnet-de-croquis` | Carnet de croquis | Crayonné, puis encré, puis colorié d'un gribouillis ; le lettrage manuscrit fait la narration | hyperframes | facile | image `styles/sketchbook/sample.png` du dépôt animate (MIT) |
| `encre-hachures` | Encre et hachures | Trait d'encre qui frémit, ombres en hachures et crayon de couleur ; le jour sur papier crème, « dans la machine » en bleu nuit | hyperframes | facile | image `styles/crosshatch/sample.png` du dépôt animate (MIT) |

### Peinture (la matière raconte)

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `aquarelle-carnet` | Aquarelle, carnet de naturaliste | Touches transparentes et brosse sèche sur papier coton, notes manuscrites, aucun trait vectoriel | hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/watercolor.mp4) (LemoLab, CC BY 4.0) |
| `huile-couteau` | Huile au couteau | Grands aplats nets en pâte épaisse, éclairés en lumière rasante ; les valeurs avant la texture | hyperframes (WebGL) | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/impasto.mp4) (LemoLab, CC BY 4.0) |
| `tourbillons-van-gogh` | Tourbillons (style Van Gogh) | Touches épaisses qui suivent un champ de directions : ciel qui tourne, halos en anneaux | hyperframes | élevée | pas d'aperçu isolé (voir la fiche) |
| `impressionnisme` | Impressionnisme | Petites touches pastel sans contour, taches de soleil qui dérivent et scintillent | hyperframes | moyenne | pas d'aperçu isolé (voir la fiche) |
| `nympheas` | Nénuphars (style Monet) | Touches horizontales sur l'eau, reflets qui tremblent, nénuphars qui dérivent | hyperframes | moyenne | pas d'aperçu réutilisable (voir la fiche) |
| `pointillisme` | Pointillisme | Points de couleurs pures de même taille, mélange dans l'œil, points complémentaires | hyperframes | moyenne | pas d'aperçu isolé |
| `periode-doree` | Période dorée (style Klimt) | Feuille d'or, motifs en spirales et en yeux, visage réaliste dans un vêtement plat | hyperframes | moyenne | pas d'aperçu isolé |
| `clair-obscur` | Clair-obscur (style Rembrandt) | Pièce sombre, une fenêtre et une bougie : la carte de lumière fait tout | hyperframes, ou blender si le sujet a du volume | élevée | pas d'aperçu isolé |
| `sfumato` | Sfumato (Renaissance) | Contours fondus, lointain bleuté, vernis jauni et craquelures | hyperframes | moyenne | pas d'aperçu isolé |
| `expressionnisme` | Expressionnisme (style Munch) | Longues touches fluides sans contour, ciel en bandes qui coulent, tout le cadre ondule | hyperframes | moyenne | pas d'aperçu isolé |
| `reve-surrealiste` | Rêve surréaliste | Plaine vide, ombres immenses, objets durs qui coulent, lumière d'atelier lisse | hyperframes | moyenne | pas d'aperçu isolé |
| `lumiere-diner-americain` | Lumière de diner américain | Pan de soleil à bord franc qui glisse sur un mur et un visage ; le silence d'une pièce | hyperframes | facile | pas d'aperçu isolé |
| `enluminure-doree` | Enluminure dorée | Page de manuscrit : parchemin, feuille d'or qui accroche un reflet, vignes dans la marge | hyperframes | moyenne | pas d'aperçu isolé |

**Voir aussi (fiches portées par une autre catégorie)**, une seule fiche par style dans tout le plugin :

- `lavis-encre` : le lavis à l'encre de Chine (8ᵉ style « Hand-drawn & Painting » de lemo-opuscar) est dans `styles-encre-asie/styles/lavis-encre/STYLE.md`, où il fusionne avec la carte « lavis » de huashu ;
- `tableau-blanc-a-la-main` (une main écrit et dessine pendant que la voix parle ; ici, `tableau-blanc` est sans main) : `styles-explicatif-infographie/styles/tableau-blanc-a-la-main/STYLE.md` ;
- les affiches et mouvements d'art graphiques `art-nouveau`, `bauhaus`, `constructivisme`, `cubisme`, `art-deco` : `styles-graphique-typo/styles/<identifiant>/STYLE.md`.

## Comment choisir

- **Expliquer une idée, une formule, un mécanisme** : `tableau-blanc` (plusieurs idées reliées sur une grande surface) ou `tableau-noir-craie` (une seule idée, une erreur corrigée).
- **Raconter à des enfants, ou avec tendresse** : `craie-grasse-album`.
- **Un trajet, une chronologie, une vie en un geste** : `trait-continu`.
- **Un lieu, un voyage, un commerce de quartier** : `croquis-urbain` ; plus calme et documenté : `aquarelle-carnet`.
- **Une petite explication chaleureuse sans voix** : `carnet-de-croquis` ; un sujet technique ou logiciel : `encre-hachures`.
- **De l'émotion, une ambiance, une marque d'artisan** : `huile-couteau`, `impressionnisme`, `nympheas`.
- **Un moment spectaculaire, une nuit, de l'énergie** : `tourbillons-van-gogh`.
- **Du luxe, un bijou, un parfum, une célébration** : `periode-doree`, `enluminure-doree`.
- **Du mystère, un portrait, un secret** : `clair-obscur`, `sfumato`.
- **Angoisse, alerte, sujet de société** : `expressionnisme`. **Temps, mémoire, absurde** : `reve-surrealiste`. **Solitude, attente, ville** : `lumiere-diner-americain`.
- **Des données fines, beaucoup de petit texte** : aucun style peint ne convient ; garde `tableau-blanc`, ou change de catégorie.

Débutant : commence par `carnet-de-croquis`, `encre-hachures` ou `lumiere-diner-americain`. Les styles notés « élevée » demandent une passe WebGL ou un rendu lourd.

## Niveau de maturité des sources

- Les fiches issues de **lemo-opuscar** décrivent un style éprouvé par un film complet.
- Les fiches issues de **huashu-art-motion** viennent de cartes de style notées par leur auteur : trois étoiles (reconnaissable et utilisable) pour `tourbillons-van-gogh`, `periode-doree`, `lumiere-diner-americain`, `enluminure-doree` ; deux étoiles (reconnaissable, avec un défaut connu) pour `impressionnisme`, `nympheas`, `pointillisme`, `sfumato`, `expressionnisme`, `reve-surrealiste` ; une étoile pour `clair-obscur` (les personnages y étaient plats : la fiche dit comment éviter ce défaut). Chaque fiche nomme son défaut connu dans la section 8 : c'est la première chose à dépasser.
- Les cartes huashu ont toutes été faites sur la même pièce (une fenêtre, une table, une jeune fille, un chat). **Ne reprends jamais cette composition** : on garde le moteur de rendu, la touche, la logique de couleur et les mouvements, et on compose pour le sujet du client.

## Règles communes à la catégorie

1. **Le procédé physique est le moteur.** On ne « fait pas un style » avec du bruit posé sur des formes vectorielles. Chaque fiche dit quel geste (écrire, poser une touche, laver, gratter) produit l'image, et c'est ce geste qu'on code.
2. **Forme propre d'abord, matière ensuite.** Dessine les masses et les valeurs à plat (lisible à 480 px de large), puis passe-les dans le moteur de touches. Une image illisible à plat ne sera pas sauvée par la texture.
3. **Texture ancrée au monde.** Le grain du papier, la toile, les craquelures bougent avec la caméra. Une texture fixe à l'écran pendant que l'image glisse dessous trahit le numérique (sauf la trame d'une impression, voir la catégorie « Papier et impression »).
4. **Hasard à graine, jamais libre.** Une touche tirée au hasard à chaque image fait bouillir tout l'écran. Les positions sont fixes ; seul un frémissement choisi change, 6 à 12 fois par seconde. La caméra, elle, reste fluide à 30 i/s. Les fiches donnent les cadences des sources (24 i/s) : à 30 i/s, joue 15 quand la fiche dit 12 et 10 quand elle dit 8 (`principes-mouvement`, « Cadence saccadée à 30 i/s »).
5. **Vieillissement jamais sur le sujet** : craquelures, écaillage et taches restent sur le fond ; le visage et l'objet principal sont protégés.
6. **Zone sûre 9:16** (1080×1920) : rien d'important au-dessus de y = 160, en dessous de y = 1560, ni à droite de x = 945. Les sous-titres vivent entre y ≈ 1380 et 1540, dans la matière du style (papier, plaque, marge), jamais dans une boîte générique.
7. **Aucune œuvre recopiée.** « Style Van Gogh », « style Klimt », « style Monet » désignent une touche, pas un tableau : on ne reproduit ni une toile, ni sa composition, ni un personnage. Le nom du peintre n'apparaît jamais dans la vidéo, et le style n'est jamais présenté comme officiel ou affilié.

## Brancher un moteur de dessin sur HyperFrames

Tous ces styles se dessinent dans un `<canvas>` par une fonction du temps, sans horloge ni hasard libre. Détails dans le skill `rendu`.

```html
<canvas id="scene" width="1080" height="1920"></canvas>
<script>
  function renderAt(t) { /* dessine l'image de l'instant t, à partir de t seul */ }
  window.addEventListener("hf-seek", (e) => renderAt(e.detail.time));
  renderAt(0);
</script>
```

**Timeline à enregistrer.** Un film dessiné par `hf-seek` doit quand même enregistrer une timeline, même vide, après le script du dessin : `window.__timelines = window.__timelines || {}; window.__timelines["main"] = gsap.timeline({ paused: true });` (GSAP chargé dans le `<head>`). Sans elle, `lint` sort l'erreur `missing_timeline_registry`. Ne pas écrire `data-no-timeline` : il fait taire le contrôle qui détecte un film figé. Recette complète : skill `rendu`, section « Film en canvas piloté par `hf-seek` » (vérifiée en rendu réel le 11/11/2026).

- Ce qui ne change pas (papier, fond déjà peint, objets terminés) est dessiné une fois dans un canvas hors écran et recopié ; on ne redessine trait par trait que ce qui est en train d'apparaître.
- Les valeurs animées (caméra, avancée d'un lavis, lumière) peuvent venir d'une timeline GSAP en pause que l'on place à `t`.
- Le grain de film s'ajoute à l'encodage, jamais dans la page. Plusieurs styles l'interdisent (huile au couteau, trait continu) : le papier ou la pâte sont déjà le grain.
- Une préparation lourde (milliers de touches, compilation d'un shader) se déclare au moteur comme le demande le skill `rendu`, pour que la première image n'arrive pas vide.

## Pour produire

1. Lis la fiche : `styles/<identifiant>/STYLE.md`. Elle est figée : look, couleur, typo, mouvement, caméra, son, pièges.
2. L'histoire, les plans et la durée viennent du sujet du client, jamais de la démo d'origine. Au moins 4 éléments sur 6 doivent différer de la démo : structure, ouverture, plan signature, trajet de caméra, forme de la musique, fin.
3. Rends une image de style en 1080×1920 avec le vrai code de dessin avant d'animer, et fais-la valider.
4. Applique la liste de contrôle de la fiche, puis la porte de livraison de `studio-coeur`.

## Crédits

Sources, commits et licences : `licenses/styles-peinture-dessin.md` à la racine du plugin. Les films d'aperçu de LemoLab sont sous CC BY 4.0 : on les montre avec le crédit « LemoLab » et le lien du dépôt, on ne les réutilise pas dans une vidéo client. La piste de voix du film `chalkboard` est exclue de cette licence : on le montre sans le son, ou on renvoie vers la galerie officielle.
