# Contrat de rendu et boucle de travail (détail)

> Fichier modifié : résumé et adaptation en français, par Flot Web (2026), de la documentation HyperFrames 0.9.33 (Copyright 2026 HeyGen, Inc., licence Apache 2.0). Originaux non modifiés dans `officiel/`. Voir `NOTICE` à la racine du plugin.

Résumé en français de `officiel/hyperframes/SKILL.md` et `officiel/hyperframes/references/format.md` (0.9.33), adapté au format vertical du studio. En cas de doute, le texte officiel fait foi pour la technique, les règles du studio (`../SKILL.md`) pour le reste.

## Forme d'un projet vertical

Exemple complet : ces deux fichiers, recopiés tels quels, passent `lint` (0 erreur, 0 avertissement), `check --json` (`ok: true`) et `render` (MP4 de 4,000 s, 1080×1920, 30 i/s). Essai refait le 11/11 en 0.9.33.

```html
<!doctype html>
<!-- index.html : document normal ; déclare les variables, charge GSAP, monte les scènes -->
<html lang="fr" data-resolution="portrait"
      data-composition-variables='[{"id":"accroche","type":"string","label":"Accroche","default":"Trois idées à retenir"}]'>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: 1080px; height: 1920px; overflow: hidden; background: #101418; }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="4"
         data-width="1080" data-height="1920" data-fps="30">
      <div id="intro" data-composition-id="intro" data-composition-src="compositions/intro.html"
           data-start="0" data-duration="4" data-track-index="1" data-track-kind="graphics"
           data-width="1080" data-height="1920"></div>
    </div>
    <script>
      window.__timelines = window.__timelines || {};
      window.__timelines["main"] = gsap.timeline({ paused: true });
    </script>
  </body>
</html>
```

```html
<!-- compositions/intro.html : tout dans <template> -->
<template>
  <style>
    #root { position: absolute; inset: 0; }
    #intro-bloc { position: absolute; left: 90px; right: 135px; top: 520px; }
    #intro-titre { margin: 0; font: 900 96px/1.1 Montserrat; color: #ffffff; }
    #intro-trait { margin-top: 36px; width: 240px; height: 12px; background: #ffd60a; transform-origin: 0 50%; }
  </style>
  <div id="root" data-composition-id="intro" data-width="1080" data-height="1920">
    <div id="intro-bloc" class="clip" data-start="0" data-duration="4">
      <h1 id="intro-titre" data-var-text="accroche">Trois idées à retenir</h1>
      <div id="intro-trait"></div>
    </div>
  </div>
  <script>
    window.__timelines = window.__timelines || {};
    const tl = gsap.timeline({ paused: true });
    // le titre est déjà lisible à l'image 0 (la vignette) : il se pose, il n'apparaît pas
    tl.fromTo("#intro-titre", { scale: 1.12 }, { scale: 1, duration: 0.35, ease: "power3.out" }, 0);
    tl.fromTo("#intro-trait", { scaleX: 0.2 }, { scaleX: 1, duration: 3.6, ease: "power1.inOut" }, 0.2);
    window.__timelines["intro"] = tl;
  </script>
</template>
```

À retenir de cet exemple :

- **GSAP 3.15.0 se charge dans le `<head>` de `index.html`**, par la balise exacte que pose `init`. Les scènes n'ont pas de balise à elles. Plugins (`CustomEase`, `SplitText`) et usage hors ligne : `../SKILL.md`, « GSAP : version et chargement ».
- **`window.__timelines = window.__timelines || {};`** avant chaque enregistrement, dans la racine comme dans les scènes.
- La racine enregistre une timeline, même vide : elle ne contient que des hôtes de scènes.
- Le son s'ajoute dans la racine, à côté des hôtes : `<audio id="musique" class="clip" src="assets/musique.mp3" data-start="0" data-duration="4" data-track-index="20" data-volume="0.5" data-timeline-role="music"></audio>`. Le script `caler.py --html` du skill `son` écrit ces balises (une piste par son à partir de la piste 20, `data-duration`, `src` relatif à `index.html`).
- `lang="fr"` sur `<html>` : `init` écrit `lang="en"`.

Points qui cassent un rendu sans message clair :

- **Même identifiant** pour l'hôte (`id` et `data-composition-id`), la racine de la scène et la clé de `window.__timelines`. Sinon chaque rendu attend 45 s par scène puis montre des images fixes.
- Styles et scripts **hors** de `<template>` dans un fichier de scène : ignorés.
- Racine de scène dimensionnée par `inset: 0`, jamais en pixels fixes.
- Identifiants uniques dans toute la page assemblée : préfixer (`#intro-titre`).
- Dans une scène, `fromTo`, pas `from` : la scène est re-positionnée à chaque affichage et `from` dérive.
- Ne jamais ajouter la timeline d'une scène à celle de la racine (`add()`), ni appeler `tl.play()`.
- Titre présent à l'image 0 : un `.clip` qui commence à 0 et dont l'animation part d'un état déjà lisible (ci-dessus : un enfant du `.clip` qui se pose). L'image 0 est la vignette.
- **L'enfant animé sans taille** (règle 13 du contrat). Essai : `<div class="carte clip"><div id="g"><div class="c"></div></div></div>` avec `.carte { width: 400px; height: 200px }` et `.c { position: absolute; inset: 0; background: … }`. Tant que `#g` n'est pas animé, la carte se voit. Dès que la timeline anime `#g` (`y`, `scale`…), `#g` devient le repère de `.c`, et comme `#g` n'a pas de taille, `.c` fait 0 px : carte invisible, `lint` et `check` muets. Correction : `.carte > div { position: absolute; left: 0; top: 0; width: 400px; height: 200px; }`. Ce n'est pas la classe `clip` qui écrase la taille : une largeur et une hauteur posées sur le `.clip` sont bien appliquées (mesuré en capture et en rendu).

## L'avertissement `nested_structure_needs_subcomposition`

Message : « `<div id="x">` is a timeline element that contains nested `<div id="y">` … the root composition is built only from sub-compositions ».

- **Quand il sort** : seulement dans `index.html`, pour un élément minuté posé directement dans la racine qui contient autre chose que du texte. Sont tolérés à l'intérieur : `span`, `b`, `i`, `em`, `strong`, `small`, `sub`, `sup`, `mark`, `a`, `code`, `br`. Tout le reste le déclenche : `div`, `p`, `h1`, `img`, `ul`… Un élément minuté qui est lui-même un `<svg>`, un `<canvas>`, une `<video>` ou un `<audio>` ne le déclenche jamais, quel que soit son contenu. Les fichiers de `compositions/` ne sont pas concernés.
- **Gravité** : avertissement en ligne de commande (`check` reste `ok: true`), mais **erreur dans l'éditeur** de l'aperçu, qui n'affiche qu'une ligne par élément de la racine. Un film court à plat dans `index.html` se rend quand même ; il n'est simplement plus modifiable proprement dans l'éditeur.
- **Corriger** : déplacer le bloc dans un fichier de scène et le monter (exemple vérifié : ajouté au projet du haut de page, `lint` 0 avertissement, `check` bon, rendu de 5 s).

```html
<!-- avant, dans index.html -->
<div id="carton" class="clip" data-start="2" data-duration="3"><div id="carton-g"><p>Plus tard…</p></div></div>

<!-- après, dans index.html : un hôte vide -->
<div id="carton" data-composition-id="carton" data-composition-src="compositions/carton.html"
     data-start="2" data-duration="3" data-track-index="2" data-track-kind="graphics"
     data-width="1080" data-height="1920"></div>
```

```html
<!-- compositions/carton.html : les temps repartent de 0 -->
<template>
  <style>
    #root { position: absolute; inset: 0; }
    #carton-bloc { position: absolute; left: 90px; top: 1100px; }
    #carton-g { width: 855px; }                      /* l'enfant animé porte sa taille (règle 13) */
    #carton-g p { margin: 0; font: 700 72px/1.2 Inter; color: #ffffff; }
  </style>
  <div id="root" data-composition-id="carton" data-width="1080" data-height="1920">
    <div id="carton-bloc" class="clip" data-start="0" data-duration="3"><div id="carton-g"><p>Plus tard…</p></div></div>
  </div>
  <script>
    window.__timelines = window.__timelines || {};
    const tl = gsap.timeline({ paused: true });
    // tweens de la scène, en temps local (0 = début de la scène)
    tl.fromTo("#carton-g", { y: 30 }, { y: 0, duration: 0.5, ease: "power3.out" }, 0);
    window.__timelines["carton"] = tl;
  </script>
</template>
```

- Règle pratique : **une scène par fichier** dès le départ (un hôte par scène dans la racine), y compris pour les fiches de style qui décrivent « une `<section class="clip">` par scène ». Les seuls éléments minutés qui restent dans `index.html` sont les hôtes, un `<canvas>` ou un `<svg>` plein cadre, les `<video>`, les `<img>` et les `<audio>`.
- Film entièrement en canvas (`hf-seek`) : le `<canvas>` reste dans la racine ; les légendes HTML posées par-dessus vont dans une scène si elles contiennent des blocs, ou s'écrivent comme de simples `<p class="clip">` de texte.

## Attributs les plus utiles

| Attribut | Sens |
| --- | --- |
| `data-start`, `data-duration` | secondes, relatives au fichier qui déclare l'élément |
| `data-track-index` | simple ligne dans l'éditeur ; l'ordre d'affichage est le `z-index` CSS |
| `data-track-kind` | `graphics` sur les hôtes de scènes, `captions` sur l'unique hôte des sous-titres |
| `data-composition-src`, `data-variable-values` | monter un fichier de scène ; valeurs de variables pour ce montage (objet JSON) |
| `data-media-start` | décalage dans le média source (rognage du début) |
| `data-playback-rate` | vitesse constante, 0,1 à 10 |
| `data-has-audio="true"` | la `<video>` garde son son ; sinon `muted` |
| `data-volume`, `data-fade-in`, `data-fade-out` | gain (1 = 0 dB) et fondus aux bords ; enveloppes avec `data-automation` |
| `data-timeline-role="music"` | désigne la musique pour `beats` |
| `data-no-timeline` | racine d'une composition **fixe** (vignette, couverture) : pas de timeline à attendre, et `check` ne cherche plus de mouvement. Jamais sur un film, même en canvas |
| `data-hold` | immobilité voulue : tant que l'élément est à l'écran, `dead_stretch` ne compte pas le temps |
| `data-motion-blur="on"` | sur la racine : flou de mouvement (`../SKILL.md`, « Flou de mouvement ») |

Temps : un clip est visible sur `[début, début + durée)`, l'image posée exactement sur la fin n'est jamais rendue. Une `<video>` ou un `<audio>` sans `data-duration` joue toute sa longueur ; une `<img>` sans durée dure 3 s. `data-start="intro + 0.5"` démarre après la fin de `intro` (espaces obligatoires) ; une faute de frappe vaut 0 sans prévenir : vérifier par une capture.

## Variables

Déclarées sur `<html>` (tableau `{id, type, label, default}` ; types `string`, `number`, `color`, `boolean`, `enum`). Liaison sans script : `data-var-text="id"`, `data-var-src="id"`, `var(--id)` en CSS. Texte, couleurs de marque et médias échangeables doivent être des variables : c'est ce qui permet de refaire la vidéo pour un autre sujet (`render --variables-file valeurs.json`) ou une série (`render --batch lignes.json`).

## Garder le projet modifiable

- Une scène par fichier, identifiants courts et lisibles ; la racine ne contient que les hôtes de scènes, les médias et le son.
- Les éléments minutés sont écrits dans le HTML, pas créés par script, chacun avec un `id` stable.
- Un seul type par piste : `graphics` pour les scènes et surimpressions, `captions` pour l'hôte unique des sous-titres.
- Ne jamais dessiner soi-même les guides de zones dans la composition (l'éditeur les affiche ; pour un contrôle : `zones-interface.md`).

## Polices

Liste exacte des 18 familles fournies avec leurs graisses, et voie `@fontsource` pour toutes les autres (paquet npm, `woff2` copié dans `assets/fonts/`, `@font-face`, `document.fonts.ready`) : `../SKILL.md`, section « Polices ». À retenir ici : une graisse absente de la liste est téléchargée au premier usage (un premier rendu hors connexion change de graisse sans prévenir) ; une police sans `@font-face` fait échouer le lint (`font_family_without_font_face`) ; une police seulement installée sur la machine (`local()`) ne suit pas le projet.

## Ajouter un média

- `id`, `class="clip"`, `data-start` (jamais un 0 mis par défaut), `data-track-index`. Vidéo avec son : `playsinline data-has-audio="true"` ; vidéo muette : `muted playsinline` ; son : `data-volume="1"`.
- Image ou vidéo plein cadre : `position: absolute; left: 0; top: 0`, largeur et hauteur du canevas, `object-fit: cover` en vertical si la source est plus large (recadrage assumé) ou `contain` pour tout garder.
- Monter le `data-duration` de la racine pour couvrir la fin du nouveau clip, sinon il ne joue pas.
- Un plan rendu par Blender entre comme une `<video muted playsinline class="clip">` ; son étalonnage passe par `media-treatment` (règle 11).

## Dérogations de mise en page

`check` mesure les boîtes à des instants choisis ; `overflow: hidden` ne fait pas taire un constat. Utiliser la dérogation la plus étroite :

| Attribut | Fait taire |
| --- | --- |
| `data-layout-allow-overflow` | débordement de l'élément et de ses enfants (à poser sur le plus petit conteneur décoratif) |
| `data-layout-bleed="true"` | un recadrage voulu d'un texte principal |
| `data-layout-allow-overlap` | superposition voulue de textes, sur ce bloc seulement |
| `data-layout-allow-occlusion` | un élément fait pour couvrir du texte (détourage devant un mot) |
| `data-layout-allow-caption-zone` | texte voulu dans la bande des sous-titres |
| `data-layout-ignore` | élément jamais contrôlé (ni débordement, ni recouvrement, ni contraste, ni taille minimale) |

Deux cas courants de `data-layout-ignore`, rencontrés en rendu réel :

- **Chiffres ou mots sous un masque** (compteur à rouleaux, colonne de chiffres qui défile derrière une fenêtre `overflow: hidden`, mots en attente sous un masque de révélation) : les valeurs cachées sont vues comme du texte recouvert (`text_occluded`, erreur). Poser `data-layout-ignore` sur la bande qui défile, pas sur la fenêtre.
- **Texte à deux plaques** (la même ligne posée deux fois avec un décalage : ombre dure, hors repérage d'impression) : la copie du dessous déclenche `content_overlap` et `contrast_aa_failure`. Poser `data-layout-ignore` sur la copie décorative seulement ; la plaque du dessus reste contrôlée.

L'attribut retire l'élément de tous les contrôles : il ne va jamais sur un texte que la personne doit lire, ni sur un conteneur de scène.

## Erreurs de lint rencontrées en premier

| Règle | Correction |
| --- | --- |
| `video_missing_muted` | une `<video>` minutée reçoit `data-has-audio="true"` ou `muted` |
| `gsap_css_transform_conflict` | poser le départ dans le tween (`gsap.fromTo`) au lieu d'un `transform` CSS |
| `gsap_animates_clip_element` | animer un enfant du `.clip` |
| `video_nested_in_timed_element` | minuter la `<video>`, pas son conteneur |
| `media_missing_id`, `media_crossorigin_breaks_preview` | un `id` sur chaque `<audio>` ; retirer `crossorigin` |
| `gsap_timeline_registered_before_async_build` | enregistrer la timeline à la fin de la fonction asynchrone |
| `standalone_composition_wrapped_in_template` | seuls les fichiers de scène utilisent `<template>` |
| `subcomposition_root_styled_by_class` | styliser la racine de scène avec `#root` |
| `clip_ends_past_root_duration` | monter le `data-duration` de la racine |
| `sweep_static` (avertissement de `check`, code 0) | film de 3 s ou plus où **rien** n'a bougé du début à la fin : timeline non branchée, canvas sans écouteur `hf-seek`. Il devient une erreur seulement si une animation de la page n'a pas avancé sous le contrôle. `data-no-timeline` pour une image fixe voulue |
| `dead_stretch` (avertissement de `check`, code 0) | plus de 3 s de suite sans changement dans un film qui bouge (essai : trou de 6,13 s signalé). Relancer avant 3 s, ou `data-hold` sur l'élément immobile exprès ; les 3 dernières secondes ne comptent pas |
| `missing_timeline_registry` (erreur) | aucune timeline enregistrée : `window.__timelines["<id>"] = tl`, vide pour un film en canvas |
| `missing_data_no_timeline` | racine ou hôte sans timeline : enregistrer une timeline ; `data-no-timeline` seulement pour une image fixe |
| `nested_structure_needs_subcomposition` (avertissement) | un `.clip` de la racine contient des blocs : le déplacer dans une scène (section plus haut) |
| `overlapping_gsap_tweens` (avertissement) | deux tweens de la même propriété se recouvrent : raccourcir le premier, décaler le second, ou `overwrite: "auto"` |
| `font_family_without_font_face` (erreur) | police hors des 18 fournies : `@font-face` vers `assets/fonts/` |
| `text_box_overflow` sur un texte découpé | interligne d'au moins 1,2 avec `mask: "lines"` |
| script qui appelle `gsap` avant son chargement (nouveau en 0.9.32) | charger GSAP avant le script de la scène |

## Boucle de travail, en détail

1. **Projet existant** : `npx -y hyperframes@0.9.33 timeline --json` dit ce qui joue quand (lire `absStart`, `absEnd`, `file`). Avant toute modification, `history --since mine --who <agent>` montre ce que la personne a changé depuis le dernier tour : construire dessus, ne jamais l'écraser.
2. **Nouveau film de plus de 15 s** : le parcours (histoire, look, storyboard) est celui du skill `studio-coeur` ; il remplace les étapes `story.md` et `spec.md` du texte officiel, dont on garde l'exigence : chaque adjectif devient un nombre, chaque plan est décrit à l'image près avant d'écrire le code.
3. **Après la dernière modification** : `check --json`. Un code 0 ne suffit pas : lire aussi les avertissements, en particulier `sweep_static` et `dead_stretch` (immobilité), qui ne font jamais échouer la commande sans `--strict`. Tant qu'une erreur de lint reste, les contrôles de mise en page et de contraste ne tournent pas. Un échec de contraste donne une `suggestedColor`. Depuis la 0.9.25, `check` rejoue la dernière passe d'un projet inchangé (rapide).
4. **Voir** : `snapshot --review` pour un film (planche d'images), `snapshot --at 0,2.5,7` ou `--range 3,5` ou `--composition intro` pour une retouche. Lire les PNG. Avec des scènes, capturer le milieu de chacune.
5. **Relecture** : la porte de livraison et le relecteur indépendant sont ceux de `studio-coeur` ; `officiel/hyperframes/references/review.md` donne la grille technique (lisibilité, rythme, images mortes).
6. **Aperçu, accord, rendu, contrôle du fichier** : `cli.md` et `exports.md`.

Annuler proprement : `history undo --who <agent>` (jamais une remise à la main). Chaque modification de timeline par la CLI imprime un reçu ; `timeline undo recu.json` la défait.

## Quand le texte officiel et le studio diffèrent

| Sujet | Texte officiel | Studio |
| --- | --- | --- |
| Format d'une nouvelle vidéo | 1920×1080 | 1080×1920 |
| Zones du vertical | haut 168 px, texte jusqu'à 1330 px | haut 160, bas 360, droite 135, gauche 60 interdits ; texte indispensable de préférence au-dessus de 1330 (table unique : `zones-interface.md`) |
| Niveau sonore | −16 à −14 LUFS | −14 LUFS ±1 avec voix ou musique, réglé après le rendu ; sans voix ni musique : niveau jugé sur la crête, feu jaune (skill `son`) |
| Fichiers posés par `init` | `CLAUDE.md`, `AGENTS.md`, `npm run publish` | supprimés après `init` (`../SKILL.md`, « Créer le projet ») |
| Bruitages | « pas de sons synthétisés » | vrais enregistrements d'abord, synthèse en repli seulement (skill `son`) |
| Télémétrie, `events`, `feedback` | actifs par défaut | coupés |
| Histoire et cahier des charges | `story.md`, `spec.md` | `studio-coeur` |
| Copier une vidéo, épisode dans un style | `/reverse-any-video`, `/style-sampling` (payants) | catégories de styles du plugin |
