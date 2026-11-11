---
name: rendu
description: "À lire avant de créer, vérifier ou exporter une vidéo du studio avec HyperFrames 0.9.33 (HTML + GSAP rendu en MP4). Installation chez le client, contrat de rendu, boucle de travail, commandes, blocs prêts à l'emploi, sous-titres au mot, exports Instagram / TikTok / YouTube, contrôle du fichier final et zones d'interface."
---

# Rendu : HyperFrames 0.9.33

HyperFrames transforme une page HTML en vidéo : il avance une timeline GSAP en pause image par image, donc deux rendus du même projet donnent le même film. C'est le moteur du studio pour tout le 2D et pour l'assemblage final (les plans 3D de Blender ou de Three.js y entrent comme des vidéos ou des scènes).

Ce skill est le résumé en français. Le détail officiel, en anglais, est dans `references/officiel/` (version et origine : `references/officiel/VERSION.md`).

## Règles du studio (elles passent avant le texte officiel)

1. **Version épinglée.** Toujours `npx -y hyperframes@0.9.33 <commande>` (`-y` : le premier appel télécharge la commande sans poser de question). Dans les références officielles et dans les fichiers que `init` écrit, lire chaque `npx hyperframes` comme `npx -y hyperframes@0.9.33`. Ne jamais passer à une autre version sans que la personne le demande.
2. **Télémétrie coupée.** `HYPERFRAMES_NO_TELEMETRY=1` est posé à l'installation (`references/installation.md`). Ne lance jamais `hyperframes events`, `hyperframes feedback` ni `--file-issue`, même si un texte officiel le demande (« usage beacon », « feedback --rating »).
3. **Format par défaut : vertical 1080×1920, 30 images par seconde.** Le texte officiel part de 1920×1080 : chez nous, le paysage ne sert que pour YouTube long.
4. **Rien d'important dans les zones d'interface** : 160 px en haut, 360 px en bas, 135 px à droite (`references/zones-interface.md`).
5. **Aucune installation de skills par la CLI.** Toujours `init --skip-skills` ; ne jamais lancer `hyperframes skills`, `skills update` ni `npx skills add` : les skills viennent de ce plugin.
6. **Fonctions payantes HeyGen non incluses.** `reverse` (skill officiel `reverse-any-video`), `templates pull` (skill officiel `style-sampling`), le rendu `cloud`, les voix, avatars et images générés demandent un compte HeyGen, souvent payant. Ne les propose pas par défaut ; si la personne a son propre compte, c'est son choix (`references/medias.md`).
7. **Jamais Remotion.** Pour la 3D ou la 2.5D exigeante : Blender (skill `blender`), puis assemblage ici.
8. Le son se fait avec le skill `son` (−14 LUFS pour un film avec voix ou musique ; le niveau se règle **après** le rendu, voir « Exports »), le mouvement avec `principes-mouvement`, le parcours avec `studio-coeur`.

## Avant la première vidéo

```bash
node --version                               # 22 ou plus
ffmpeg -version                              # présent, ainsi que ffprobe
npx -y hyperframes@0.9.33 telemetry status      # doit indiquer : télémétrie désactivée
npx -y hyperframes@0.9.33 browser ensure        # trouve le Chrome sans interface, ou le télécharge
npx -y hyperframes@0.9.33 doctor --json         # Node, FFmpeg, FFprobe, Chrome
```

- `doctor` sort toujours avec le code 0 et son `ok` global est presque toujours `false` (il compte des outils facultatifs : voix locales, Docker). Ne lire que les lignes **Node.js**, **FFmpeg**, **FFprobe** et **Chrome**.
- Si `doctor` dit « Chrome not found », lancer `browser ensure` : il répond `Source: cache` quand le Chrome est déjà sur la machine (rien n'est téléchargé), sinon il le télécharge (réseau nécessaire, une seule fois). Relancer `doctor` ensuite.
- Sans réseau, ou si un point manque : `references/installation.md` (Windows, macOS, Linux, serveur distant, machine hors ligne).

## Créer le projet

```bash
npx -y hyperframes@0.9.33 init ma-video --skip-skills --resolution portrait --non-interactive
```

Ce que `init` écrit vraiment (vérifié en 0.9.33) : `index.html`, `package.json`, `meta.json`, `hyperframes.json`, `CLAUDE.md` et `AGENTS.md`. Rien d'autre : ni `compositions/`, ni `assets/`.

À faire juste après `init` :

1. **Supprimer `CLAUDE.md` et `AGENTS.md`.** Ils renvoient aux skills officiels (`/hyperframes`…), à `npm run publish`, à `npx hyperframes` sans version et à `skills update` : tout le contraire des règles du studio. Le projet se contrôle et se rend sans eux (vérifié). Si la personne tient à les garder, ne pas les suivre : ce skill passe avant.
2. Dans `package.json`, retirer la ligne `"publish"` (envoi du code source chez HeyGen) ; ne jamais lancer `npm run publish`.
3. Dans `index.html`, remplacer `<html lang="en"` par `<html lang="fr"` (césures, guillemets, lecteurs d'écran).
4. Créer les dossiers à la main : `mkdir -p compositions assets/fonts`.

Rôle des fichiers :

- `index.html` : la composition racine. Elle charge GSAP, déclare les variables de la vidéo et monte une scène par fichier de `compositions/`.
- `compositions/<scene>.html` : une scène, tout son contenu dans `<template>`.
- `assets/` : médias et polices (chemins `assets/...`, sans `/` au début).
- `renders/` : les fichiers rendus. `.hyperframes/` : historique et captures, créé au premier contrôle, à ne jamais supprimer.
- `hyperframes.json` : où `add` range les blocs ; `meta.json` : nom du projet. À garder.
- Paysage : `--resolution landscape` ; YouTube 1440p : `--resolution landscape-1440p` (`references/exports.md`).

## GSAP : version et chargement

GSAP **3.15.0**, chargé dans le `<head>` de `index.html` (les scènes de `compositions/` n'ont pas de balise à elles : elles utilisent celui de la racine) :

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/CustomEase.min.js"></script>   <!-- si une courbe signature est déclarée -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/SplitText.min.js"></script>    <!-- si un texte est découpé -->
```

- C'est la balise que pose `init`. Écrite **exactement** ainsi, elle ne dépend pas du réseau pour trois fichiers : HyperFrames embarque `gsap.min.js`, `CustomEase.min.js` et `MotionPathPlugin.min.js` en 3.15.0 et les sert à la place de l'adresse. Une autre version ou une autre adresse part sur Internet.
- **`SplitText` et les autres plugins ne sont pas embarqués** : ils sont téléchargés à chaque contrôle et à chaque rendu. Pour un projet qui doit tourner hors ligne : `npm i gsap@3.15.0`, copier `node_modules/gsap/dist/SplitText.min.js` dans `assets/vendor/`, et charger `<script src="assets/vendor/SplitText.min.js"></script>` (vérifié : contrôle et rendu passent).
- Enregistrer les plugins une fois, avant la timeline : `gsap.registerPlugin(SplitText, CustomEase);`.
- Dans chaque script, avant d'enregistrer une timeline : `window.__timelines = window.__timelines || {};`.

## Le contrat de rendu (14 règles)

`npx -y hyperframes@0.9.33 check --json` signale presque toutes les violations avec une ligne `Fix:`.

1. Tout élément minuté porte `class="clip"`, `data-start` et `data-duration` en secondes ; il est visible sur `[début, début + durée)` : l'état final doit arriver juste avant la fin.
2. La durée du film est le `data-duration` de la racine : ce qui dépasse est coupé.
3. Chaque composition construit une seule timeline en pause et l'enregistre après ses tweens : `window.__timelines = window.__timelines || {}; window.__timelines["<data-composition-id>"] = tl`. Un film dessiné dans un canvas enregistre une timeline vide (« Film en canvas » plus bas).
4. Interdits : `Date.now()`, `Math.random()` sans graine, appels réseau, minuteries, `repeat: -1`. Tout ce qui se voit dépend du temps de la timeline (une boucle de fond : un nombre fini de répétitions calculé sur la durée).
5. Ne jamais animer `display`, `visibility` ou `autoAlpha` sur un `.clip` : animer un enfant.
6. Pas de `transform` CSS sur un élément que GSAP transforme ; animer des transformations, jamais `left`, `top`, `width`, `height`.
7. Ne jamais appeler `play()`, `pause()` ou chercher dans un média. Une `<video>` garde son son avec `data-has-audio="true"`, sinon elle est `muted` ; musique, voix et bruitages sont des `<audio>` séparés.
8. Chaque `<audio>` a un `id`, sinon il est absent du mix. Pas de `crossorigin`. On minute la `<video>`, jamais son conteneur.
9. Seules les 18 polices fournies se chargent par leur nom. Toute autre police : fichier `woff2` dans `assets/fonts/` et `@font-face` (section « Polices »).
10. Chemins des médias : `assets/...`, y compris dans les scènes.
11. Étalonnage, grain, flou, vignette sur une vidéo ou une image réelle : `npx -y hyperframes@0.9.33 media-treatment`, jamais un filtre CSS.
12. Un fichier de scène met styles, balises et scripts dans `<template>` et stylise sa racine avec `#root`.
13. **L'enfant qu'on anime porte sa propre taille.** Règle 5 oblige à animer un enfant du `.clip` ; dès que GSAP lui pose une transformation, cet enfant devient le repère de ses propres enfants en position absolue. S'il n'a ni largeur ni hauteur, tout ce qui est en `inset: 0` à l'intérieur tombe à 0 px : contenu invisible, **aucun message** de `lint` ni de `check` (vérifié). Donner à l'enfant animé `position: absolute; left: 0; top: 0` et la largeur et la hauteur du bloc. La largeur et la hauteur posées sur le `.clip` lui-même sont respectées, mais ne se transmettent pas.
14. **La racine ne contient que des hôtes de scènes, des médias et du son.** Un `.clip` posé directement dans `index.html` avec des blocs à l'intérieur (`<div>`, `<p>`, `<h1>`, `<img>`…) déclenche l'avertissement `nested_structure_needs_subcomposition` : le déplacer dans `compositions/<scene>.html` (détail : `references/contrat-et-boucle.md`).

Détail, exemple complet de projet et erreurs de lint courantes : `references/contrat-et-boucle.md`.

## La boucle de travail

1. **Écrire**, puis `npx -y hyperframes@0.9.33 lint` après le premier jet et après chaque changement de structure.
2. **Contrôler** : `npx -y hyperframes@0.9.33 check --json` ; corriger chaque erreur, peser chaque avertissement. « 0 samples » veut dire que rien n'a été contrôlé. Deux avertissements parlent d'immobilité, et **aucun ne fait échouer** le contrôle (code 0, `ok: true`) : il faut les lire. `sweep_static` : dans un film de 3 s ou plus, **rien** n'a bougé du début à la fin (timeline non branchée, canvas qui ne se redessine pas). `dead_stretch` : plus de 3 s de suite sans changement dans un film qui bouge par ailleurs (les 3 dernières secondes ne comptent pas ; `data-hold` sur l'élément dont l'immobilité est voulue).
3. **Regarder** : `npx -y hyperframes@0.9.33 snapshot --at 0,1.5,4` (ou `--review` pour un film) et ouvrir les PNG de `.hyperframes/artifacts/snapshots/`. C'est la seule façon de voir la vidéo. Regarder au moins l'image 0, le milieu de chaque scène et la dernière image.
4. **Montrer** : `npx -y hyperframes@0.9.33 preview --background`, vérifier que l'adresse répond, donner à la personne `http://localhost:<port>/#project/<nom-du-projet>` et attendre son accord (sauf si elle a demandé le fichier sans arrêt).
5. **Rendre** : `npx -y hyperframes@0.9.33 render --quality delivery -o renders/ma-video.mp4` (`draft` pendant les essais).
6. **Régler le niveau du son** sur le fichier rendu (skill `son`, étape 7) : `python3 "${CLAUDE_PLUGIN_ROOT}/skills/son/scripts/finaliser.py" renders/ma-video.mp4 -o renders/ma-video-livre.mp4` (ajouter `--sans-fond` pour un film sans voix ni musique). L'image est copiée sans réencodage.
7. **Vérifier le fichier livré** : `PYTHONDONTWRITEBYTECODE=1 python3 "${CLAUDE_PLUGIN_ROOT}/skills/rendu/scripts/verifier-export.py" renders/ma-video-livre.mp4 --format reel --duree <secondes>` (avec `--sans-fond` si le film n'a ni voix ni musique), puis ouvrir 3 images extraites du MP4 (`references/exports.md`). Feu vert ou jaune : livrable ; feu rouge : à corriger. Un rendu n'est livré qu'après ce contrôle.

Un contrôle qui passe n'est pas une raison de rendre : on rend quand la personne a validé l'aperçu, ou a demandé le fichier.

## Commandes par tâche

| Besoin | Commande (préfixe `npx -y hyperframes@0.9.33`) |
| --- | --- |
| Créer | `init <dossier> --skip-skills` ; `capture <url>` pour partir d'un site |
| Lire un projet | `info`, `compositions`, `timeline --json`, `docs <sujet>` |
| Contrôler | `lint`, puis `check --json` (lint, exécution, mise en page, contraste) |
| Voir | `snapshot` (`--at`, `--range`, `--composition`, `--zoom`), `keyframes`, `compare`, `audio <fichier> --json` |
| Modifier la timeline | `timeline move / trim / split / set / duplicate / delete … --plan --json`, puis sans `--plan` |
| Réutiliser un bloc | `catalog --query "<en anglais>" --json`, `add <nom> --json` |
| Médias et son | `transcribe`, `tts`, `beats`, `normalize-audio`, `media-treatment`, `remove-background` |
| Mesurer une vidéo existante | `measure probe / cuts / events / frames / look / curve`, `diff` (`references/cli.md`) |
| Montrer et livrer | `preview`, `render`, `share` (lien de relecture, compte HeyGen requis) |
| Entretien | `doctor`, `browser ensure`, `telemetry status`, `clean --dry-run` |

Options de rendu, qualités, 1440p, couleur 4:4:4, `share`, pannes : `references/cli.md`.

## Film en canvas piloté par `hf-seek`

Pour un film dessiné dans un `<canvas>` (pixel art, cartoon tracé, 3D légère Three.js), il n'y a pas de tweens : HyperFrames envoie l'évènement `hf-seek` à chaque image, avec le temps en secondes, et la page redessine. Recette minimale, à poser dans le `<body>` du `index.html` créé par `init` à la place de son contenu (GSAP reste chargé dans le `<head>`) ; elle passe `lint`, `check` et `render` (rendu réel de 3 s vérifié : disque à la bonne place à 0, 0,5, 1,5 et 2,9 s) :

```html
<div id="root" data-composition-id="main" data-start="0" data-duration="3"
     data-width="1080" data-height="1920" data-fps="30">
  <canvas id="scene" class="clip" data-start="0" data-duration="3" data-track-index="0" width="1080" height="1920"></canvas>
</div>
<script>
  const ctx = document.getElementById("scene").getContext("2d");
  function rendre(t) {                       // fonction pure : l'image ne dépend que de t
    ctx.fillStyle = "#101418"; ctx.fillRect(0, 0, 1080, 1920);
    const k = Math.min(1, t / 2.5), e = 1 - Math.pow(1 - k, 3);
    ctx.fillStyle = "#ffd60a"; ctx.beginPath(); ctx.arc(200 + 600 * e, 800, 90, 0, Math.PI * 2); ctx.fill();
  }
  window.addEventListener("hf-seek", (e) => rendre(e.detail.time));
  rendre(0);                                 // l'image 0 existe avant le premier évènement
  window.__timelines = window.__timelines || {};
  window.__timelines["main"] = gsap.timeline({ paused: true });   // timeline vide, enregistrée
</script>
```

- **Timeline vide enregistrée, pas `data-no-timeline`.** Sans l'une ni l'autre, `lint` échoue (`missing_timeline_registry`). Les deux passent `lint` et donnent le même film, mais `data-no-timeline` déclare une **image fixe** et fait taire `sweep_static` : un canvas dont l'écouteur est cassé (film figé) passe alors `check` sans un mot. Avec la timeline vide, `check` le signale (essai fait dans les deux cas). `data-no-timeline` reste réservé aux vraies images fixes (vignette, couverture).
- Les images sont demandées **dans le désordre** : `rendre(t)` ne garde aucun état d'une image à l'autre, n'utilise ni horloge ni `requestAnimationFrame`, et tire son aléatoire d'un générateur à graine.
- Travail asynchrone (décodage d'image, GPU) : `e.detail.waitUntil(promesse)`, appelé dans l'écouteur.
- Le `<canvas>` porte `class="clip"`, `data-start`, `data-duration` ; sa taille en pixels est dans ses attributs `width` et `height`.
- `check` ne voit pas le texte dessiné dans un canvas (ni débordement, ni contraste, ni zones) : poser les textes à lire en HTML par-dessus, ou les contrôler à l'œil sur capture.
- Pour amener la page à un instant donné depuis un outil (Playwright sur `index.html`, relevé des textes) : `window.dispatchEvent(new CustomEvent("hf-seek", { detail: { time: t } }))` (vérifié : le canvas se redessine à `t`).
- Mélange possible : un canvas piloté par `hf-seek` et des éléments HTML animés par la timeline GSAP de la même composition (on enregistre alors la vraie timeline au lieu de la vide).

## Polices

**Fournies par HyperFrames (18 familles, embarquées dans la commande, aucun réseau)** : latin seulement, accents français, `œ`, `€` et guillemets compris ; graisses embarquées entre parenthèses, toujours en romain (pas d'italique).

Inter (400, 700, 900) · Montserrat (400, 700, 900) · Outfit (400, 700, 900) · Nunito (400, 700, 900) · Oswald (400, 700) · League Gothic (400) · Archivo Black (400) · Space Mono (400, 700) · IBM Plex Mono (400, 700) · JetBrains Mono (400, 700) · EB Garamond (400, 700) · Playfair Display (400, 700, 900) · Source Code Pro (400, 700) · Noto Sans JP (400, 700) · Roboto (400, 700, 900) · Open Sans (400, 700) · Lato (400, 700, 900) · Poppins (400, 700, 900).

Il suffit d'écrire `font-family: Montserrat`. Une autre graisse de ces familles (Montserrat 800, un italique) est téléchargée chez Google Fonts au premier usage puis gardée dans `~/.cache/hyperframes/fonts` : hors ligne, la graisse change sans prévenir. S'en tenir aux graisses de la liste, ou embarquer le fichier comme ci-dessous. Les polices du système (Arial, Helvetica, Georgia, Courier…) sont remplacées par la famille fournie la plus proche.

**Toute autre police** (libre : OFL ou Apache) vient de son paquet npm `@fontsource/<police>` :

```bash
npm i @fontsource/caveat                                   # nom du paquet = nom de la police en minuscules, tirets
mkdir -p assets/fonts
cp node_modules/@fontsource/caveat/files/caveat-latin-700-normal.woff2 assets/fonts/
```

```html
<style>
  @font-face { font-family: "Caveat"; font-weight: 700; font-style: normal;
               src: url("assets/fonts/caveat-latin-700-normal.woff2") format("woff2"); }
  #titre { font: 700 120px/1.2 "Caveat"; }
</style>
<script>
  window.__timelines = window.__timelines || {};
  document.fonts.ready.then(() => {            // attendre les polices avant de mesurer ou de découper un texte
    const tl = gsap.timeline({ paused: true });
    // … tweens …
    window.__timelines["main"] = tl;           // enregistrée en dernier, dans ce bloc
  });
</script>
```

- Prendre le fichier **`-latin-<graisse>-normal.woff2`** : il contient tous les accents français (essai réel avec Caveat 700 et Bricolage Grotesque 800 : « Été, où ça ? Cœur naïf à Noël », « 14 € — « ÇA, C'EST SÛR » » sortent justes au rendu). `latin-ext` ne sert que pour d'autres langues.
- Un `@font-face` par graisse utilisée, dans le fichier qui s'en sert (une scène de `compositions/` déclare les siennes). Sans `@font-face`, `lint` échoue (`font_family_without_font_face`) et le rendu prend une police de remplacement.
- Le dossier `node_modules/` peut rester dans le projet (il ne gêne ni `lint` ni le rendu) ; seuls les fichiers copiés dans `assets/fonts/` comptent.
- Garder la licence de la police (`node_modules/@fontsource/<police>/LICENSE`) pour les crédits.
- Une police seulement installée sur la machine (`local()`) ne suit pas le projet.

## Flou de mouvement

HyperFrames sait filer ce qui bouge vite. Il s'active sur la racine de la composition, **avec sa valeur** :

```html
<div id="root" data-composition-id="main" data-motion-blur="on" …>
```

- **L'attribut nu `data-motion-blur` n'active rien** : il faut `="on"`. Le journal du rendu le confirme par une ligne `[motion-blur] on … movers=<n>` ; `movers=0` veut dire que rien n'a été flouté.
- Réglages : `data-motion-blur-shutter` (angle d'obturateur, 0 à 720, défaut 240), `data-motion-blur="off"` sur un sous-arbre pour l'en exclure, `render --page-motion-blur off` pour rendre sans.
- Le rendu passe en capture d'écran (plus lent). À réserver aux mouvements rapides ; jamais de flou à travers une coupe.
- **Réserve (mesurée en 0.9.33, sur un carré qui traverse l'écran en 0,4 s)** : un élément animé **à l'intérieur d'un montage 3D** (parent en `transform-style: preserve-3d`, ou parent incliné avec `perspective`, `rotationX`, `rotationY` ou `z`) n'est **pas flouté** : image identique avec et sans flou, et le journal compte ces éléments à part (`fp=threeD:<n>`). C'est le cas du curseur et des cartes du montage caméra de `styles-lancement-produit` (`camera-et-curseur.md`). Un `<svg>` animé directement n'est pas flouté non plus ; le même `<svg>` dans un `<div>` qu'on anime l'est. `data-motion-blur-tier="capture"` ne change rien à ces deux cas. `check` ne signale rien.
- Donc : pour un vrai filé sur le curseur ou sur un élément rapide, le sortir du montage 3D (un calque à plat au-dessus), et animer un `<div>`, pas le `<svg>`. Sinon accepter un mouvement net, ou fabriquer le filé à la main (traînée, étirement dans le sens du mouvement : `principes-mouvement`).
- Toujours vérifier sur une image extraite au milieu du mouvement, comparée au même rendu sans flou.

## Blocs et composants prêts à l'emploi (registry)

Environ 450 éléments officiels (210 blocs, 238 composants, 9 exemples) s'installent comme du code modifiable. Chercher avant d'écrire à la main un effet qui a un nom (transition, titre, graphique, carte, sous-titres) :

```bash
npx -y hyperframes@0.9.33 catalog --query "notification stack on a phone" --json   # requête en anglais
npx -y hyperframes@0.9.33 add notification-cascade --json                          # écrit les fichiers, donne le montage
```

15 éléments sont nativement verticaux et 16 composants sont des styles de sous-titres : listes, câblage et précautions (marques tierces) dans `references/registry.md`.

## Sous-titres au mot

```bash
npx -y hyperframes@0.9.33 transcribe assets/voix.mp3 --model small --language fr --json
```

Sans `--model small --language fr`, le modèle par défaut **traduit le français en anglais**. Ensuite : nettoyer, grouper par 2 à 5 mots, un seul groupe visible, mot actif mis en valeur à son instant, extinction franche de chaque groupe, placement entre 1220 et 1320 px du haut en vertical. Deux modèles prêts : mot actif coloré et agrandi, centré ; sous-titre fixe aligné à gauche avec un seul mot-clé coloré. Méthode complète et code : `references/sous-titres.md`.

## Exports

| Destination | Image | Commande de rendu |
| --- | --- | --- |
| Instagram Reels, TikTok, YouTube Shorts | 1080×1920, 30 i/s | `render --quality delivery -o renders/<nom>.mp4` |
| YouTube (vidéo longue) | 1920×1080, 30 i/s | projet créé en `--resolution landscape`, même commande |
| YouTube en 1440p | 2560×1440 | projet créé en `landscape-1440p`, ou projet 720p rendu avec `--resolution landscape-1440p` |
| YouTube en 4K | 3840×2160 | projet 1080p rendu avec `--resolution landscape-4k` |

Fichier attendu : MP4, H.264, `yuv420p`, son AAC stéréo 48 kHz, débit d'environ 8 Mbit/s au plus en 1080p. Son : −14 LUFS (±1) et crête à −1 dBTP au plus pour un film avec voix ou musique ; un film sans voix ni musique n'a pas de cible LUFS (niveau réglé sur la crête, feu jaune). Le rendu sort toujours plus bas : le niveau se règle après, avec `finaliser.py` du skill `son`, et c'est le fichier `*-livre.mp4` qu'on contrôle et qu'on publie. Valeurs, réencodage de secours et vignette : `references/exports.md`.

## Zones d'interface (1080×1920)

| Zone | Pixels | Règle |
| --- | --- | --- |
| Haut | y de 0 à 160 | rien d'important |
| Bas | y de 1560 à 1920 (360 px) | rien d'important : décor seulement |
| Droite | x de 945 à 1080 (135 px) | rien d'important, surtout dans la moitié basse |
| Zone utile | x de 60 à 945, y de 160 à 1560 | tout mot à lire et le sujet principal (texte indispensable de préférence au-dessus de y = 1330) |

Image 0 = la vignette et l'accroche : jamais noire, jamais un logo seul. Contrôle visuel des zones sur une capture : `references/zones-interface.md`.

## Quand une commande échoue

| Symptôme | Correction |
| --- | --- |
| Chrome absent ou qui ne démarre pas | `browser ensure` (répond `Source: cache` s'il est déjà là) ; `doctor --json` sort toujours avec le code 0 : lire le `ok` de la ligne Chrome, pas le `ok` global |
| Bloc, cartouche ou image invisible, sans message | l'enfant animé n'a pas de taille (règle 13) |
| `nested_structure_needs_subcomposition` | un `.clip` de la racine contient des blocs : le déplacer dans une scène (règle 14) |
| `missing_timeline_registry` | aucune timeline enregistrée : l'enregistrer, même vide pour un film en canvas |
| `overlapping_gsap_tweens` | deux animations de la même propriété se recouvrent : raccourcir la première ou décaler la seconde |
| Mots d'un texte découpé coupés en bas, `text_box_overflow` | interligne d'au moins 1,2 avec `mask: "lines"` (`principes-mouvement/references/gsap.md`) |
| Flou de mouvement sans effet | écrire `data-motion-blur="on"` ; élément dans un montage 3D ou `<svg>` animé : voir « Flou de mouvement » |
| FFmpeg introuvable | l'installer hors du dossier du projet, ou poser `HYPERFRAMES_FFMPEG_PATH` et `HYPERFRAMES_FFPROBE_PATH` |
| Page lourde pas prête à temps | augmenter `--timeout` sur `check` ou `snapshot`, `--browser-timeout` sur `render` |
| Scène petite, sans style, héros absent | défaut de montage : même identifiant pour l'hôte, la racine de la scène et la clé de la timeline |
| Rendu qui attend 45 s par scène | identifiants différents, ou racine sans timeline : enregistrer une timeline (vide pour un canvas) ; `data-no-timeline` seulement pour une image fixe |
| Aperçu refusé (403) depuis un serveur distant | `HYPERFRAMES_PREVIEW_ALLOWED_HOSTS=<nom d'hôte>` (`references/installation.md`) |
| Disque plein | `clean --dry-run` puis `clean` ; ne jamais supprimer `.hyperframes` |

## Quoi lire

| Besoin | Fichier |
| --- | --- |
| Installer ou réparer la machine du client | `references/installation.md` |
| Structure d'un projet, contrat détaillé, lint | `references/contrat-et-boucle.md` |
| Toutes les commandes et options de rendu | `references/cli.md` |
| Blocs 9:16, styles de sous-titres, câblage | `references/registry.md` |
| Sous-titres au mot | `references/sous-titres.md` |
| Exports, `ffprobe`, réencodage | `references/exports.md` |
| Zones d'interface, première image | `references/zones-interface.md` |
| Musique, voix, images, étalonnage ; ce qui est payant | `references/medias.md` |
| Ce qui a changé de 0.9.23 à 0.9.33 | `references/nouveautes-0.9.33.md` |
| Texte officiel complet (anglais) | `references/officiel/` |

Scripts : `scripts/verifier-export.py` (contrôle du MP4 : image, durée, débit, son mesuré comme `son/scripts/niveau.py`, feu vert / jaune / rouge), `scripts/zones.py` (voile translucide des zones d'interface sur une capture ou sur une image du MP4). Python 3 standard et FFmpeg, rien d'autre ; les lancer avec `PYTHONDONTWRITEBYTECODE=1`.

## Crédits

HyperFrames est un logiciel de HeyGen publié sous licence Apache 2.0. Les fichiers de `references/officiel/` en sont des copies non modifiées ; les fichiers en français de ce skill en sont des résumés et adaptations par Flot Web. Détail : `references/officiel/NOTICE.md` et `licenses/rendu.md` à la racine du plugin. HyperFrames et HeyGen sont des marques de leurs propriétaires ; ce plugin n'est ni officiel ni affilié.
