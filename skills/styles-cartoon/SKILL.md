---
name: styles-cartoon
description: "Catégorie de styles « Cartoon » du studio motion (tuyau de caoutchouc années 1930, animé sur cellulo années 80, sitcom SF, cartoon plat années 50, comics cosmique, papier découpé satirique). À utiliser quand le client veut une vidéo en dessin animé, avec des personnages originaux qui jouent, ou dit « style cartoon », « style animé », « style comics »."
---

# Styles Cartoon (catégorie 6)

Six styles de dessin animé en 2D, tous rendus avec HyperFrames (canvas piloté par le temps). Ils ont un point commun : **le personnage joue**. Si la vidéo n'a ni personnage ni objet vivant, regarde plutôt les catégories « Graphique et typo » ou « Explicatif ».

Le skill `studio-coeur` pilote le parcours (questions, histoire, look, storyboard, construction, revue, livraison). Les skills `principes-mouvement` (dictionnaire des mouvements, cités ici par leur numéro `#NNN`), `rendu` (HyperFrames, export) et `son` (mix à −14 LUFS, vrais enregistrements d'abord, environ 5 bruitages par 10 s) s'appliquent à tous les styles. Cette catégorie ne décrit que ce qui est propre à chaque look.

## Les styles

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `tuyau-caoutchouc-1930` | Tuyau de caoutchouc années 1930 | Noir et blanc encré, membres en tuyau, tout le décor respire sur un orchestre de jazz | hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/rubber-hose.mp4) (LemoLab, CC BY 4.0) |
| `anime-cellulo-80` | Animé sur cellulo années 80 | Aplats deux tons sur décors à l'aérographe, néons qui traversent l'image, lu sur cassette et tube cathodique | hyperframes (canvas + passe WebGL) | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/cel-anime-80s.mp4) (LemoLab, CC BY 4.0) |
| `sitcom-sf` | Sitcom SF (série animée pour adultes) | Gros contours qui frémissent, aplats, duo aux réactions opposées, un portail lumineux | hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/scifi-toon.mp4) (LemoLab, CC BY 4.0) |
| `cartoon-annees-50` | Cartoon plat années 50 | Couleur imprimée à côté du trait, corps fixe et mains qui travaillent : le style du mode d'emploi | hyperframes | facile | [film](https://lemomo-ai.github.io/lemo-opuscar/films/midcentury-toon.mp4) (LemoLab, CC BY 4.0) |
| `comics-cosmique` | Comics cosmique (style Kirby) | Quadrichromie tramée, gros noirs, bulles d'énergie, onomatopées en relief, cases | hyperframes | moyenne | pas d'aperçu isolé (voir la fiche) |
| `papier-decoupe-satirique` | Papier découpé satirique (style série animée) | Personnages en papier découpé, jeu limité, yeux collés, humour sec | hyperframes | facile | pas d'aperçu isolé (voir la fiche) |

Deux fiches fusionnent deux sources : `tuyau-caoutchouc-1930` (lemo-opuscar + carte huashu) et `sitcom-sf` (lemo-opuscar + carte huashu « cartoon plat à contour fin »). Une seule fiche par style.

## Comment choisir

- **Une marque veut de la bonne humeur et de la musique** : `tuyau-caoutchouc-1930`. Le style vit du rythme ; sans musique calée, il est mort.
- **Un tutoriel, une recette, une notice, des règles** : `cartoon-annees-50`. C'est le seul qui apprend à *faire* quelque chose étape par étape.
- **Un dialogue drôle, une comparaison de versions, un avant/après absurde** : `sitcom-sf`.
- **De l'émotion, de la nuit, de la vitesse, de la nostalgie** : `anime-cellulo-80`. Le plus beau, le plus long à faire.
- **Une annonce choc, un lancement, un chiffre qui frappe** : `comics-cosmique`.
- **Une satire, une scène de bureau, un petit sketch à peu de moyens** : `papier-decoupe-satirique`.

Débutant : commence par `cartoon-annees-50` ou `papier-decoupe-satirique`.

## Règles communes à la catégorie

1. **Aucun personnage existant.** Tu inventes la distribution : silhouettes, couleurs, noms, accessoires. On ne recopie ni un héros de dessin animé, ni une combinaison de couleurs reconnaissable, ni un logo, ni une mélodie, ni une réplique culte. Le nom d'une série ou d'un studio n'apparaît jamais dans la vidéo ; « style … » sert seulement à se comprendre avec le client.
2. **Feuille de modèle avant d'animer** : face, trois quarts, profil, 3 ou 4 expressions, 2 ou 3 poses, palette. Toute la vidéo dessine le personnage avec la même fonction.
3. **Animation « en deux »** : les poses, les bouches, les clignements ne changent qu'une image sur deux (parfois une sur trois) ; la caméra, les volets et la lumière restent fluides à 30 i/s. Une caméra saccadée se lit comme un bug.
   ```js
   const tq = Math.floor(t * 15) / 15;   // temps des dessins : 15 par seconde à 30 i/s
   // personnages : dessiner(tq) ; caméra et lumière : utiliser t
   ```
   Les sources ont été réglées à 24 i/s, où « en deux » = 12 dessins par seconde et « en trois » = 8. À 30 i/s, quand une fiche dit « 12 », prends **15** ; quand elle dit « 8 », prends **10**. Ne garde pas 12 à 30 i/s : la cadence devient irrégulière (2 images, puis 3). Si le client accepte un film à 24 i/s, garde les valeurs d'origine. (Même règle pour tout le plugin : `principes-mouvement`, « Cadence saccadée à 30 i/s ».)
4. **Trait d'épaisseur constante à l'écran** : on transforme les points, puis on trace sans transformation. Un gros plan est « redessiné », pas agrandi.
5. **Jamais de bascule sèche entre deux poses** : anticipation (`#121`), action, suivi (`#122`). Les sourcils se définissent par leur bout intérieur (près du nez) et extérieur, pas « gauche / droite », sinon « triste » devient « fâché ».
6. **Réaction après chaque image absurde** : le rire est sur le visage. Sujet à au moins 1/3 de la hauteur aux moments clés.
7. **Zone sûre 9:16** (1080×1920) : rien d'important au-dessus de y = 160, en dessous de y = 1560, ni à droite de x = 945 (table : `rendu/references/zones-interface.md`). Les visages restent hors de la bande des sous-titres.
8. **Jeu d'acteur : registre « jeu cartoon »** du skill `personnages` (`references/31-emotions.md`, `references/jeu-d-acteur.md`). C'est la seule catégorie où le corps peut rebondir en boucle, et seulement **calé sur le tempo** (un rebond par temps, tempo à nombre entier d'images) ; un sautillement libre reste interdit. Le reste du jeu ne change pas : une pensée par plan, un regard d'abord, anticipation, tenue. `papier-decoupe-satirique` (jeu limité) et `sitcom-sf` (poses tenues) n'ont pas de boucle du corps : suis leur fiche. Hors de cette catégorie (2.5D « histoire vraie » en particulier), le défaut est le jeu sobre.
9. **Canvas ou pièces SVG ?** Les fiches décrivent un dessin en canvas ; le skill `personnages` fournit des pièces SVG. Les deux se marient : en SVG en ligne, on donne aux pièces le trait de la fiche (voie rendue et vérifiée le 11/11/2026 sur `cartoon-annees-50`) ; en canvas, on trace les chemins des pièces avec le trait du style. **L'épaisseur et la matière du trait sont celles de la fiche de style**, pas le contour épais par défaut des pièces. Marche à suivre : `personnages/references/pieces-svg.md`, « Pièces SVG dans un style au trait propre ».

## Brancher un moteur de dessin sur HyperFrames

Tous ces styles se dessinent dans un `<canvas>` par une fonction du temps, sans horloge ni hasard libre (hasard à graine uniquement). Détails dans le skill `rendu`.

```html
<canvas id="scene" width="1080" height="1920"></canvas>
<script>
  function renderAt(t) { /* dessine l'image de l'instant t, à partir de t seul */ }
  window.addEventListener("hf-seek", (e) => renderAt(e.detail.time));
  renderAt(0);
</script>
```

**Timeline à enregistrer.** Un film dessiné par `hf-seek` doit quand même enregistrer une timeline, même vide, après le script du dessin : `window.__timelines = window.__timelines || {}; window.__timelines["main"] = gsap.timeline({ paused: true });` (GSAP chargé dans le `<head>`). Sans elle, `lint` sort l'erreur `missing_timeline_registry`. Ne pas écrire `data-no-timeline` : il fait taire le contrôle qui détecte un film figé. Recette complète : skill `rendu`, section « Film en canvas piloté par `hf-seek` » (vérifiée en rendu réel le 11/11/2026).

Les valeurs animées (caméra, ouverture d'un portail, volets) peuvent venir d'une timeline GSAP en pause que l'on place à `t` ; les dessins restent une fonction pure de `tq`. Le grain et les rayures de pellicule se composent en dernière passe, jamais dans la scène.

## Pour produire

1. Lis la fiche : `styles/<identifiant>/STYLE.md`. Elle est figée : look, couleur, typo, mouvement, caméra, son, pièges.
2. L'histoire, les plans et la durée viennent du sujet du client, jamais de la démo d'origine. Au moins 4 éléments sur 6 doivent différer de la démo : structure, ouverture, plan signature, trajet de caméra, forme de la musique, fin.
3. Rends une image de style en 1080×1920 avant d'animer, et fais-la valider.
4. Applique la liste de contrôle de la fiche, puis la porte de livraison de `studio-coeur`.

## Crédits

Sources, commits et licences : `licenses/styles-cartoon.md` à la racine du plugin. Les films d'aperçu de LemoLab sont sous CC BY 4.0 : on les montre avec le crédit « LemoLab » et le lien du dépôt, on ne les réutilise pas dans une vidéo client.
