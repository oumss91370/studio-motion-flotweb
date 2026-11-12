---
name: styles-papier-impression
description: "Catégorie de styles « Papier et impression » du studio motion (risographie, dossier tramé rétro, gravure sur bois, gravure sur cuivre, affiche sérigraphiée, plan-séquence gravé, papier découpé de collage, papiers découpés style Matisse, pop tramé). À utiliser quand le client veut une vidéo qui a l'air imprimée, gravée ou découpée dans du papier, ou dit « style riso », « style affiche », « style gravure », « style collage », « style pop art », « style BD tramée »."
---

# Styles Papier et impression (catégorie 3)

Neuf styles où **l'image sort d'un procédé d'atelier** : une encre posée par une machine, un bloc taillé, un écran de soie, une feuille coupée aux ciseaux. Leur point commun : **rien n'est peint**. On empile des couches (des « passages » d'encre, des feuilles de papier), et les défauts du procédé (repérage décalé, trame, manques d'encre, bords déchirés) sont ce qui donne la vie.

Le skill `studio-coeur` pilote le parcours (questions, histoire, look, storyboard, construction, revue, livraison). Les skills `principes-mouvement` (dictionnaire des mouvements, cités ici par leur numéro `#NNN`), `rendu` (HyperFrames, export), `son` (mix à −14 LUFS, vrais enregistrements d'abord, environ 5 bruitages par 10 s) et `blender` (pour le plan-séquence gravé) s'appliquent à tous les styles. Cette catégorie ne décrit que ce qui est propre à chaque look.

## Les styles

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `risographie` | Risographie | 2 ou 3 encres translucides superposées, trame, grain, repérage jamais parfait | hyperframes (canvas + passe WebGL) | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/risograph.mp4) (LemoLab, CC BY 4.0) |
| `dossier-trame` | Dossier tramé rétro | Papier crème, trames, gros titres décalés, tampons qui claquent : un dossier lu pièce par pièce | hyperframes (HTML, SVG, GSAP) | facile | [film](https://lemomo-ai.github.io/lemo-opuscar/films/halftone-dossier.mp4) (LemoLab, CC BY 4.0) |
| `gravure-sur-bois` | Gravure sur bois | Bloc noir qui se taille seul : la lumière n'existe que là où le couteau a creusé ; une couleur au plus | hyperframes (canvas + passe WebGL) | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/woodcut.mp4) (LemoLab, CC BY 4.0) |
| `gravure-cuivre` | Gravure sur cuivre | Planche de naturaliste qui se grave : contour, hachures, contre-hachures, lettres gravées, lavis final | hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/engraving.mp4) (LemoLab, CC BY 4.0) |
| `affiche-serigraphie` | Affiche sérigraphiée | 4 à 6 encres opaques posées une à une, ciels en bandes, jours de papier au repérage | hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/silkscreen-poster.mp4) (LemoLab, CC BY 4.0) |
| `plan-sequence-grave` | Plan-séquence gravé | Monde 3D rendu en carte à gratter (encre, papier, un rouge), traversé par un seul mouvement de caméra | blender (recommandé) ou three | très élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/printed-long-take.mp4) (LemoLab, CC BY 4.0, image seule) |
| `papier-decoupe-collage` | Papier découpé, collage | Papiers déchirés, ombres portées, crayon gras, motifs ; des mondes pleins de petite vie | hyperframes | facile | image `styles/cut-paper/sample.png` du dépôt animate (MIT) |
| `papiers-decoupes-matisse` | Papiers découpés (style Matisse) | Grandes formes aux ciseaux, aplats de gouache saturés, feuilles épinglées qui bougent | hyperframes | facile | pas d'aperçu isolé (voir la fiche) |
| `pop-trame` | Pop tramé (style BD des années 60) | Points de trame, gros cernes noirs, couleurs primaires, onomatopées, cases qui changent de couleur | hyperframes | facile | pas d'aperçu isolé (voir la fiche) |

Fusion : `risographie` réunit le style « Risograph Print » de lemo-opuscar et le style « riso » d'animate. **Une seule fiche**, qui cite ses deux origines.

**Voir aussi (fiches portées par une autre catégorie)**, pour ne pas faire de doublon :

- Les **affiches** de huashu-art-motion (Art nouveau, constructiviste, Bauhaus) sont dans `styles-graphique-typo` (`styles-graphique-typo/styles/art-nouveau/STYLE.md`, `…/constructivisme/STYLE.md`, `…/bauhaus/STYLE.md`). Dans cette catégorie, l'affiche est `affiche-serigraphie`.
- Le **papier découpé rouge** traditionnel et la **lanterne de papier** sont dans `styles-encre-asie` (`papier-decoupe-rouge`, `lanterne-papier`) ; le **livre pop-up** dans `styles-matieres-3d` (`livre-pop-up`) ; le **théâtre de papier** dans `styles-2-5d` (`theatre-de-papier`) ; le **papier découpé satirique** et le **comics cosmique** dans `styles-cartoon` (`papier-decoupe-satirique`, `comics-cosmique`).

## Comment choisir

- **Une marque créative, un café, un festival, un fanzine, un ton décontracté** : `risographie`.
- **Un « dossier », une enquête drôle, une liste de preuves, un classement, un produit « mis en accusation »** : `dossier-trame`.
- **Un récit grave, un effort long, une lumière qui arrive, un hommage** : `gravure-sur-bois`.
- **Une fiche de musée, « une minute sur… », une planche d'anatomie d'un objet, une carte ancienne** : `gravure-cuivre`.
- **Un lieu à visiter, un événement avec date et lieu, une gamme de couleurs, des horaires** : `affiche-serigraphie`.
- **Un grand paysage traversé d'un souffle, un récit de nature, une ouverture de film** : `plan-sequence-grave`.
- **Une histoire avec un personnage attachant, une chronologie racontée par des objets** : `papier-decoupe-collage`.
- **Une identité joyeuse et colorée, de la danse, de la musique, une marque de mode ou de décoration** : `papiers-decoupes-matisse`.
- **Une annonce choc, une promo, une réaction, une punchline** : `pop-trame`.

Débutant : commence par `dossier-trame`, `pop-trame` ou `papier-decoupe-collage`. `plan-sequence-grave` est le style le plus exigeant du catalogue.

## Niveau de maturité des sources

- Les six styles de lemo-opuscar reposent sur un film de démo complet.
- `papier-decoupe-collage` (animate) est éprouvé sur un film de 60 s ; le volet animate de `risographie` sur une étude de 6 s calée image par image.
- `papiers-decoupes-matisse` et `pop-trame` viennent de cartes huashu **notées trois étoiles** par leur auteur, tournées sur une seule scène d'intérieur : on garde le moteur, pas la composition.

## Règles communes à la catégorie

1. **Une couche = un passage.** Chaque couleur est une encre ou une feuille posée séparément ; les couleurs ne se mélangent que par superposition (encres translucides) ou recouvrement (encres opaques, papier). **Aucun dégradé lisse** : la nuance vient d'une trame, de bandes en paliers, de hachures ou d'une autre feuille.
2. **Peu de couleurs, choisies avant de dessiner** : 2 ou 3 encres (riso), 4 à 6 (sérigraphie), deux valeurs et une couleur (gravures), une dizaine de papiers (collage). Chaque couleur a un rôle.
3. **Le papier est le blanc.** On ne peint pas de blanc : c'est une réserve, un trou, une zone non imprimée.
4. **Le défaut est réglé, pas tiré au hasard à chaque image.** Un décalage de repérage par plan (1 à 4 px), avec une secousse sur un accent ; un grain qui ne change que partiellement. Un défaut qui change à chaque image scintille et fait exploser le poids du fichier.
5. **Rien n'apparaît en fondu.** Une encre est tirée, un bloc est taillé, une feuille est posée, un tampon claque. Les transitions sont des gestes d'atelier.
6. **Le texte est imprimé avec le reste** : sur une plaque, dans une marge, sur une étiquette de papier. Jamais une légende flottante générique.
7. **Zone sûre 9:16** (1080×1920) : rien d'important au-dessus de y = 160, en dessous de y = 1560, ni à droite de x = 945. Affiche, planche, page de dossier, feuille de carnet : ces formats sont naturellement verticaux.
8. **Aucune marque de machine ou d'atelier réelle**, aucune affiche, planche ou case existante recopiée. « Style Matisse » et « style BD des années 60 » désignent une manière, pas une œuvre ; le nom d'un artiste n'apparaît jamais dans la vidéo.

## Brancher un moteur de dessin sur HyperFrames

```html
<canvas id="scene" width="1080" height="1920"></canvas>
<script>
  function renderAt(t) { /* dessine l'image de l'instant t, à partir de t seul */ }
  window.addEventListener("hf-seek", (e) => renderAt(e.detail.time));
  renderAt(0);
</script>
```

**Timeline à enregistrer.** Un film dessiné par `hf-seek` doit quand même enregistrer une timeline, même vide, après le script du dessin : `window.__timelines = window.__timelines || {}; window.__timelines["main"] = gsap.timeline({ paused: true });` (GSAP chargé dans le `<head>`). Sans elle, `lint` sort l'erreur `missing_timeline_registry`. Ne pas écrire `data-no-timeline` : il fait taire le contrôle qui détecte un film figé. Recette complète : skill `rendu`, section « Film en canvas piloté par `hf-seek` » (vérifiée en rendu réel le 11/11/2026).

- Hasard à graine uniquement, aucune horloge. Papier, plaques terminées et blocs taillés sont mis en cache.
- Les styles tramés supportent mal la compression : exporte avec un débit élevé, et vérifie le moiré à 100 % et à 50 % de la taille. **N'ajoute pas de grain à l'encodage** : il est déjà dans l'impression.
- `dossier-trame` se construit en éléments HTML et SVG animés par une timeline GSAP : c'est le plus proche d'une composition HyperFrames ordinaire.
- `plan-sequence-grave` : scène construite dans Blender par le connecteur MCP (skill `blender`), séquence d'images ramenée dans HyperFrames pour la passe « papier », le texte et le montage.

## Pour produire

1. Lis la fiche : `styles/<identifiant>/STYLE.md`. Elle est figée : look, couleur, typo, mouvement, caméra, son, pièges.
2. L'histoire, les plans et la durée viennent du sujet du client, jamais de la démo d'origine. Au moins 4 éléments sur 6 doivent différer de la démo : structure, ouverture, plan signature, trajet de caméra, forme de la musique, fin.
3. Rends une image de style en 1080×1920 avec le vrai code de dessin avant d'animer, et fais-la valider.
4. Applique la liste de contrôle de la fiche, puis la porte de livraison de `studio-coeur`.

## Crédits

Sources, commits et licences : `licenses/styles-papier-impression.md` à la racine du plugin. Les films d'aperçu de LemoLab sont sous CC BY 4.0 : on les montre avec le crédit « LemoLab » et le lien du dépôt, on ne les réutilise pas dans une vidéo client. La piste de voix du film `printed-long-take` est exclue de cette licence : on le montre sans le son, ou on renvoie vers la galerie officielle.
