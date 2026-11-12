---
name: styles-jeu-retro
description: "Catégorie de styles « Jeu vidéo et rétro » du studio motion (RPG pixel 16 bits, diorama pixel 2.5D, micro-jeux en rafale, jeu télé rythmique, pixel art 8 bits, néon vaporwave, images de synthèse des années 80). À utiliser quand le client veut une vidéo qui ressemble à un jeu vidéo ou à un écran rétro, ou dit « pixel art », « rétro », « arcade », « vaporwave », « années 80 »."
---

# Styles Jeu vidéo et rétro (catégorie 7)

Sept styles qui empruntent le langage des jeux et des écrans d'autrefois : menus, boîtes de dialogue, vies, manches, palettes limitées, tubes cathodiques. Ici **l'interface raconte** : un compteur de vies, une barre, un écran de sauvegarde portent l'émotion sans narration.

Le skill `studio-coeur` pilote le parcours. `principes-mouvement` (mouvements cités par leur numéro `#NNN`), `rendu` (HyperFrames, export) et `son` (−14 LUFS, vrais enregistrements d'abord, environ 5 bruitages par 10 s) s'appliquent. Exception sonore de la catégorie : les bruitages de jeu (bips, jingles, puces sonores) sont **synthétisés par nature**, c'est le son juste pour ces styles.

## Les styles

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `pixel-rpg-16-bits` | RPG pixel 16 bits | 320×180 natifs, palette indexée, boîtes de dialogue, menus, sauvegardes, musique de puce | hyperframes | moyenne | [film](https://lemomo-ai.github.io/lemo-opuscar/films/pixel-rpg.mp4) (LemoLab, CC BY 4.0) |
| `diorama-pixel` | Diorama pixel 2.5D | Sprites pixel plats dans une maquette 3D éclairée, vue plongeante, bande de netteté | blender (qualité) ou three (léger) + hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/hd-2d.mp4) (LemoLab, CC BY 4.0) |
| `micro-jeux` | Micro-jeux en rafale | Un ordre, quelques secondes, une action ; chaque jeu dans une matière différente, de plus en plus vite | hyperframes | élevée | [film](https://lemomo-ai.github.io/lemo-opuscar/films/microgame.mp4) (LemoLab, CC BY 4.0) |
| `jeu-tele-rythmique` | Jeu télé rythmique | Vectoriel plat, mascottes-jouets, rayures bonbon, tout sur la grille de tempo | hyperframes | facile | lien dans la fiche (démo avec marques tierces : ne pas afficher en vitrine) |
| `pixel-8-bits` | Pixel art 8 bits | Image basse résolution agrandie sans lissage, tramage, police bitmap ; la résolution raconte le temps | hyperframes | facile | image dans la fiche (animate, MIT) |
| `neon-vaporwave` | Néon vaporwave | Tubes néon, grille en perspective, soleil à bandes, lecture VHS ; dérogation bleu-violet | hyperframes | moyenne | pas d'aperçu isolé (voir la fiche) |
| `cgi-annees-80` | Images de synthèse des années 80 | Plastique brillant, damier réfléchi, sphère chromée, fil de fer vert | hyperframes (faux 3D) ou three / blender | moyenne | pas d'aperçu isolé (voir la fiche) |

## Comment choisir

- **Raconter un parcours, un souvenir, une évolution dans le temps** : `pixel-rpg-16-bits` (émotion par l'interface) ou `pixel-8-bits` (plus simple, la résolution monte avec les époques).
- **Montrer un lieu précieux, un réseau qui s'allume, une petite scène contemplative** : `diorama-pixel`.
- **Une liste de tâches, une journée, une suite d'étapes drôles** : `micro-jeux`.
- **Des chiffres, un classement, un bilan d'année, des manches** : `jeu-tele-rythmique`.
- **Musique, nostalgie, ambiance, visuel d'attente** : `neon-vaporwave`.
- **Clin d'œil aux débuts de l'informatique, objet « rendu » rétro, logo** : `cgi-annees-80`.

Débutant : commence par `jeu-tele-rythmique` ou `pixel-8-bits`.

**Fiche d'ici qui sert aussi à d'autres catégories** : `diorama-pixel` sert à `styles-2-5d` (récit à personnages plats : suivre son `references/pipeline.md` avec la fiche d'ici) et à `styles-matieres-3d`. Une seule fiche par style dans tout le plugin.

**Voir aussi (fiches portées par une autre catégorie)** : les formats complets en pixel art (`lecon-pixel-art`, `science-pixel-art`) sont dans `formats-flotweb/styles/<identifiant>/STYLE.md` ; les styles cartoon couverts par la dérogation bleu-violet (`comics-cosmique`, `anime-cellulo-80`) sont dans `styles-cartoon/styles/<identifiant>/STYLE.md`.

## Règles communes à la catégorie

1. **Aucun jeu existant** : ni nom, ni personnage, ni cadre d'interface, ni police, ni logo, ni mélodie, ni bruitage repris d'un jeu. Le vocabulaire de l'arcade (pièces, briques, score, vies) est générique ; les objets emblématiques d'un jeu précis ne le sont pas.
2. **Pixel art = grille entière.** On dessine à la vraie basse résolution puis on agrandit au plus proche voisin, par un facteur entier. Aucun lissage, aucun déplacement d'une fraction de pixel, aucun dégradé (deux ou trois couleurs et un tramage ordonné). Résolutions verticales exactes pour 1080×1920 : 90×160 (pixel de 12), 135×240 (8), 180×320 (6), 270×480 (4).
3. **Les choses clignotent, elles ne fondent pas** : apparitions et disparitions par tout ou rien, par mosaïque ou par changement de palette. Jamais de fondu en transparence dans un style pixel.
4. **Les sprites sautent d'image en image, la caméra reste régulière.** À 30 i/s : sprites à 10 ou 15 dessins par seconde (les sources disent 8 ou 12 à 24 i/s) ; déplacements de caméra en pixels entiers.
5. **La musique d'abord** : une grille de tempo et une table d'évènements avant toute animation ; chaque choc visuel tombe sur un évènement listé. Choisis un tempo où un temps vaut un nombre entier d'images (à 30 i/s : 120 BPM = 15 images, 150 BPM = 12, 100 BPM = 18).
6. **Zone sûre 9:16** : rien d'important au-dessus de y = 160, en dessous de y = 1560, ni à droite de x = 945. Une boîte de dialogue de jeu se pose donc **au-dessus** de y = 1560, pas tout en bas.
7. **Bleu-violet** : le plugin rejette les films dominés par le bleu-violet (look « fait par une IA »). Deux styles d'ici en ont besoin par nature : lis `references/derogation-bleu-violet.md` avant de les produire.

## Brancher le dessin sur HyperFrames

```html
<div id="root" data-composition-id="main" data-start="0" data-duration="10"
     data-width="1080" data-height="1920" data-fps="30">
  <canvas id="basse" width="180" height="320" hidden></canvas>
  <canvas id="ecran" width="1080" height="1920"></canvas>
</div>
<script>
  const e = document.getElementById("ecran").getContext("2d");
  e.imageSmoothingEnabled = false;
  function renderAt(t) {
    dessiner(basse, t);                          // tout en pixels entiers
    e.drawImage(basse, 0, 0, 1080, 1920);        // agrandi ×6, sans lissage
  }
  window.addEventListener("hf-seek", (ev) => renderAt(ev.detail.time));
  renderAt(0);                                 // l'image 0 existe avant le premier évènement
  window.__timelines = window.__timelines || {};
  window.__timelines["main"] = gsap.timeline({ paused: true });   // timeline vide, enregistrée (GSAP chargé dans le <head>)
</script>
```

**Enregistre une timeline vide, n'écris pas `data-no-timeline`.** Sans l'une ni l'autre, `lint` sort l'erreur `missing_timeline_registry`. Les deux la font taire, mais `data-no-timeline` déclare une image fixe et coupe le contrôle `sweep_static` : un canvas dont l'écouteur est cassé (film figé) passerait `check` sans alerte. Avec la timeline vide, `check` le signale (vérifié en rendu réel le 11/11/2026, HyperFrames 0.9.33). Si le film a aussi des éléments animés par GSAP (un titre HTML), on enregistre la vraie timeline à la place de la vide. Recette complète et pièges : skill `rendu`, section « Film en canvas piloté par `hf-seek` ».

L'image est une fonction du temps seul : pas d'horloge, hasard à graine. Détails dans le skill `rendu`. Pour `diorama-pixel` (et la voie Blender de `cgi-annees-80`), ouvre aussi le skill `blender` : connexion au connecteur MCP, rendu vertical, envoi vers HyperFrames.

## Pour produire

1. Lis la fiche `styles/<identifiant>/STYLE.md` (figée : look, couleur, typo, mouvement, son, pièges).
2. L'histoire et les plans viennent du sujet du client, jamais de la démo d'origine (au moins 4 différences sur 6 : structure, ouverture, plan signature, trajet de caméra, forme de la musique, fin).
3. Rends une image de style 1080×1920 et fais-la valider avant d'animer.
4. Liste de contrôle de la fiche, puis porte de livraison de `studio-coeur`.

## Crédits

Sources, commits et licences : `licenses/styles-jeu-retro.md` à la racine du plugin.
