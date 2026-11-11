---
name: styles-encre-asie
description: "Catégorie de styles « Encre et Asie » du studio motion (lavis à l'encre de Chine, ombres chinoises, estampe japonaise, papier découpé rouge, lanterne de papier découpé, fresques de Dunhuang, aquarelle d'animation style Ghibli, lumière d'anime style Shinkai). À utiliser quand le client veut une vidéo à l'encre, en estampe, en théâtre d'ombres, ou dit « style japonais », « style chinois », « style Ghibli », « style Shinkai », « style anime poétique »."
---

# Styles Encre et Asie (catégorie 2)

Huit styles issus des traditions visuelles d'Asie de l'Est et de l'animation japonaise contemporaine. Leur point commun : **le vide compte autant que le plein**. Le papier nu, l'écran éclairé, le ciel, la marge sont de la matière ; on enlève plutôt qu'on n'ajoute.

Le skill `studio-coeur` pilote le parcours (questions, histoire, look, storyboard, construction, revue, livraison). Les skills `principes-mouvement` (dictionnaire des mouvements, cités ici par leur numéro `#NNN`), `rendu` (HyperFrames, export), `son` (mix à −14 LUFS, vrais enregistrements d'abord, environ 5 bruitages par 10 s) et `blender` (pour la lanterne de papier) s'appliquent à tous les styles. Cette catégorie ne décrit que ce qui est propre à chaque look.

## Les styles

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `lavis-encre` | Lavis à l'encre de Chine | Cinq tons d'encre sur papier de riz, un seul rouge (le sceau) ; un coup de pinceau = une montagne, une vague, un geste | hyperframes (canvas + passe WebGL) | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/ink-wash.mp4) (LemoLab, CC BY 4.0) |
| `ombres-chinoises` | Ombres chinoises | Marionnettes de cuir teinté ajouré contre un écran de coton, éclairées par des lampes à huile | hyperframes (canvas + passe WebGL) | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/shadow-puppet.mp4) (LemoLab, CC BY 4.0) |
| `estampe-japonaise` | Estampe japonaise | Aplats imprimés bloc par bloc, trait gravé, ciels en dégradé essuyé, caméra qui déroule un rouleau | hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/ukiyoe.mp4) (LemoLab, CC BY 4.0) |
| `papier-decoupe-rouge` | Papier découpé rouge | Découpages rouges articulés sur fond de papier : la découpe est le dessin, les trous laissent passer la lumière | hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/papercut-red.mp4) (LemoLab, CC BY 4.0) |
| `lanterne-papier` | Lanterne de papier découpé | Boîte à ombres : 6 à 9 feuilles découpées rétroéclairées, lumière chaude par les trous, ombres entre les couches | blender (recommandé) ou three | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/paper-lantern.mp4) (LemoLab, CC BY 4.0) |
| `fresques-dunhuang` | Fresques de Dunhuang | Mur de terre rouge, couleurs minérales, trait de fer, rubans qui volent, peinture qui s'écaille | hyperframes | moyenne | pas d'aperçu isolé (voir la fiche) |
| `aquarelle-ghibli` | Aquarelle d'animation (style Ghibli) | Décors à l'aquarelle lumineuse, personnages en deux tons, le vent qui passe dans tout | hyperframes | moyenne | pas d'aperçu isolé (voir la fiche) |
| `lumiere-shinkai` | Lumière d'anime (style Shinkai) | Cumulus géants, rayons de soleil, reflets d'objectif, ombres franches : la lumière est le sujet | hyperframes | moyenne | pas d'aperçu isolé (voir la fiche) |

Fusions : `lavis-encre` réunit le style « Chinese Ink Wash » de lemo-opuscar et la carte « lavis » de huashu-art-motion ; `ombres-chinoises` réunit le style « Shadow Puppetry » de lemo-opuscar et la carte « théâtre d'ombres » de huashu. **Une seule fiche par style**, qui cite ses deux origines.

Précision : huashu-art-motion ne contient pas de carte « estampe » (ukiyo-e) ; la fiche `estampe-japonaise` vient donc de lemo-opuscar seul. Les papiers découpés de style Matisse et le papier découpé de collage sont dans la catégorie `styles-papier-impression`.

## Comment choisir

- **Silence, sagesse, récit lent, marque de thé, arts martiaux, méditation** : `lavis-encre`.
- **Un conte, une légende, une fable avec des gentils et des méchants, du spectacle vivant** : `ombres-chinoises`.
- **Un voyage en étapes, une série de lieux, les saisons, un produit dans plusieurs décors** : `estampe-japonaise`.
- **Une fête, le Nouvel An, une tradition, « un seul geste qui se multiplie »** : `papier-decoupe-rouge`.
- **Un souvenir, une histoire de nuit, deux lieux reliés, un objet qu'on garde** : `lanterne-papier`.
- **Un sujet spirituel, historique, la route de la soie, une musique, une danse** : `fresques-dunhuang`.
- **La douceur du quotidien, la campagne, l'enfance, une marque artisanale** : `aquarelle-ghibli`.
- **L'adolescence, la nostalgie, un rendez-vous manqué, un ciel d'été** : `lumiere-shinkai`.

Débutant : commence par `estampe-japonaise` ou `papier-decoupe-rouge` (canvas 2D seul, formes plates). `lavis-encre` et `ombres-chinoises` demandent une passe WebGL ; `lanterne-papier` demande Blender.

## Niveau de maturité des sources

- Les quatre styles de lemo-opuscar (et les deux fusions) reposent sur un film de démo complet.
- `fresques-dunhuang`, `aquarelle-ghibli`, `lumiere-shinkai` viennent de cartes huashu **notées deux étoiles** par leur auteur (reconnaissables, avec un défaut connu), tournées sur une seule scène d'intérieur. Leur fiche nomme le défaut en section 8 et dit comment le contourner. Ne reprends jamais la composition de cette scène (une fenêtre, une table, une jeune fille, un chat).

## Règles communes à la catégorie

1. **Le vide est de la matière.** Vise 50 à 80 % de surface calme (papier, écran, ciel) selon le style. Si une image devient chargée, on enlève.
2. **Respect des traditions.** Ces styles sont des arts vivants. On en apprend la grammaire (matière, geste, composition) ; on ne recopie ni une estampe célèbre, ni une marionnette historique, ni un motif de fresque précis, ni un personnage de film. Tout motif est généré par le code ou dessiné pour le sujet.
3. **Écriture et sceaux.** N'écris des caractères chinois ou japonais que si le client fournit le texte exact et sa traduction : un caractère faux se voit tout de suite pour qui sait lire. Par défaut : texte français dans une serif classique, et un **sceau abstrait** (formes géométriques découpées dans un carré rouge irrégulier), jamais un faux idéogramme.
4. **« Style Ghibli », « style Shinkai »** sont des repères d'inspiration pour se comprendre avec le client. On ne reprend aucun personnage, décor ou plan de film, le nom n'apparaît jamais dans la vidéo, et le style n'est jamais présenté comme officiel ou affilié.
5. **Personnages articulés, pas déformés** (ombres, papier découpé, lanterne) : des pièces rigides qui tournent sur un rivet. Jamais d'écrasement ni de métamorphose.
6. **Deux cadences** : les personnages et le trait avancent par paliers (8 à 15 dessins par seconde selon le style) ; la caméra, la lumière et les fluides restent fluides à 30 i/s. Les fiches donnent les cadences des sources (24 i/s) : à 30 i/s, joue 15 quand la fiche dit 12 et 10 quand elle dit 8 (`principes-mouvement`, « Cadence saccadée à 30 i/s »).
7. **Zone sûre 9:16** (1080×1920) : rien d'important au-dessus de y = 160, en dessous de y = 1560, ni à droite de x = 945. Le format vertical est celui du **rouleau suspendu** : ces styles y sont à l'aise.

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

- Hasard à graine uniquement ; aucune horloge. Le papier, les décors finis et les pièces de marionnette sont mis en cache.
- Les passes WebGL (diffusion de l'encre, lumière à travers le cuir) lisent des canvas 2D comme textures ; déclare leur préparation comme le demande le skill `rendu`.
- Le grain de film s'ajoute à l'encodage, jamais dans la page ; l'estampe et le papier découpé n'en veulent **aucun** (le papier est le grain).
- `lanterne-papier` : la scène se construit dans Blender par le connecteur MCP (skill `blender`), le rendu revient dans HyperFrames pour le texte et le montage.

## Pour produire

1. Lis la fiche : `styles/<identifiant>/STYLE.md`. Elle est figée : look, couleur, typo, mouvement, caméra, son, pièges.
2. L'histoire, les plans et la durée viennent du sujet du client, jamais de la démo d'origine. Au moins 4 éléments sur 6 doivent différer de la démo : structure, ouverture, plan signature, trajet de caméra, forme de la musique, fin.
3. Rends une image de style en 1080×1920 avec le vrai code de dessin avant d'animer, et fais-la valider.
4. Applique la liste de contrôle de la fiche, puis la porte de livraison de `studio-coeur`.

## Crédits

Sources, commits et licences : `licenses/styles-encre-asie.md` à la racine du plugin. Les films d'aperçu de LemoLab sont sous CC BY 4.0 : on les montre avec le crédit « LemoLab » et le lien du dépôt, on ne les réutilise pas dans une vidéo client.
