# Sous-titres au mot (français, vertical)

> Fichier modifié : résumé et adaptation en français, par Flot Web (2026), de la documentation HyperFrames 0.9.33 (Copyright 2026 HeyGen, Inc., licence Apache 2.0). Originaux non modifiés dans `officiel/`. Voir `NOTICE` à la racine du plugin.

Résumé et adaptation de `officiel/hyperframes/references/captions.md` et `officiel/media-use/audio/references/captions/` (0.9.33). Beaucoup de gens regardent sans le son : toute parole est sous-titrée, et l'image porte l'accroche même muette.

## 1. Obtenir les mots et leurs instants

```bash
npx -y hyperframes@0.9.33 transcribe assets/voix.mp3 --model small --language fr --json
```

- **Toujours** `--model small --language fr`. Le modèle par défaut (`small.en`) **traduit le français en anglais** sans prévenir. Voix sur musique ou son bruité : `--model medium --language fr`.
- Le résultat est écrit dans `assets/transcript.json` (le JSON de sortie nomme le chemin) et **écrasé au prochain appel** : le renommer (`assets/voix-mots.json`). `--to srt` ou `--to vtt` écrit aussi un fichier de sous-titres classique (utile pour YouTube).
- Forme de travail : `[{ "id": "w0", "text": "Bonjour", "start": 0.00, "end": 0.42 }, …]`, un mot par entrée.
- Le premier appel télécharge le modèle (`small` : 466 Mo ; `medium` : 1,5 Go). Tout tourne sur la machine.
- Fichiers `.srt`, `.vtt` ou JSON Whisper existants : `transcribe <fichier>` les convertit.
- Si la voix a été générée à partir d'un texte connu, garder **le texte du script** pour l'orthographe et **la transcription** pour les instants : associer les mots par position, pas par texte (un mot répété prendrait le mauvais instant).

## 2. Nettoyer (obligatoire)

1. Lire la transcription en entier. Plus de 20 % de jetons `♪` ou illisibles, ou des mots sans sens : la transcription a échoué, recommencer avec un modèle plus grand.
2. Whisper invente des mots sur les silences (« Merci. », « Sous-titres réalisés par… ») et répète des lignes sur une fin silencieuse. Repérer les silences puis supprimer les mots qui commencent dedans :

```bash
ffmpeg -i assets/voix.mp3 -af silencedetect=noise=-35dB:d=0.6 -f null - 2>&1 | grep silence_
```

3. Corriger l'orthographe d'après le script : noms propres, chiffres (« 3 000 », « 14 % »), accents, majuscules.
4. Typographie française : l'apostrophe reste collée (« l'idée », « qu'il » = un seul mot affiché) ; `? ! : ;` et `»` restent avec le mot qui précède, `«` avec le mot qui suit (espace insécable), pour ne jamais commencer une ligne par un signe.
5. Jamais deux mots dans une même entrée minutée.

## 3. Grouper

| Ton | Mots par groupe |
| --- | --- |
| Énergie haute (accroche, liste rapide) | 2 à 3 |
| Conversation | 3 à 5 |
| Calme, récit | 4 à 6 |

- Couper à la fin d'une phrase, à une pause de 150 ms ou plus, ou à la limite de mots. Ne pas séparer un article de son nom ni un nombre de son unité.
- **Un seul groupe visible à la fois.** Un groupe s'ouvre à l'instant de son premier mot ou juste avant, se ferme à la fin de son dernier mot ou juste après.
- Durée minimale à l'écran : 0,7 s ; débit maximal d'environ 17 caractères par seconde. Pas de trou de 1 à 3 images entre deux groupes : prolonger le premier.
- Un groupe à 0 s exactement paraît déjà là : démarrer entre 0,1 et 0,3 s (sauf si c'est l'accroche de l'image 0, voulue).
- En vertical : 2 lignes au maximum, environ 5 mots par ligne, jamais sous 42 px.

## 4. Structure dans le projet (modèle A : mot actif coloré et agrandi, centré)

Un seul hôte porte tous les groupes, pour une seule piste de sous-titres dans l'éditeur :

```html
<!-- index.html -->
<div id="sous-titres" data-composition-id="sous-titres" data-composition-src="compositions/sous-titres.html"
     data-start="0" data-duration="18" data-track-index="9" data-track-kind="captions"
     data-width="1080" data-height="1920" style="z-index: 90"></div>
```

```html
<!-- compositions/sous-titres.html -->
<template>
  <style>
    #root { position: absolute; inset: 0; }
    .st-zone { position: absolute; left: 90px; right: 135px; top: 1180px; height: 180px;
               display: flex; align-items: center; justify-content: center; overflow: visible; }
    .st-groupe { position: absolute; left: 0; right: 0; text-align: center; opacity: 0;
                 font-family: Montserrat; font-weight: 900; text-transform: uppercase; line-height: 1.08;
                 color: #fff; -webkit-text-stroke: 0.08em #000; paint-order: stroke fill; }
    /* les mots sont des blocs collés sans espace entre eux : c'est la marge qui fait l'espace */
    .st-mot { display: inline-block; margin: 0 0.22em; }
  </style>
  <div id="root" data-composition-id="sous-titres" data-width="1080" data-height="1920">
    <div class="st-zone" id="st-zone"></div>
  </div>
  <script>
    // GROUPES : produit à l'étape 3 et collé ici (aucun chargement réseau au rendu).
    const GROUPES = [
      { start: 0.20, end: 1.35, mots: [ { t: "Voici", s: 0.20, e: 0.48 }, { t: "l'idée", s: 0.52, e: 1.30 } ] },
      // …
    ];
    const ACCENT = "#FFD60A";            // à relier à la couleur d'accent de la chaîne
    const ECHELLE = 1.12;                // agrandissement maximal du mot actif
    const AVANCE = 0.08;                 // en em : ce que le mot actif peut prendre de chaque côté sur ses voisins
    const zone = document.getElementById("st-zone");
    const tl = gsap.timeline({ paused: true });

    GROUPES.forEach((g, gi) => {
      const el = document.createElement("div");
      el.className = "st-groupe"; el.id = "st-g" + gi;
      g.mots.forEach((m, mi) => {
        const sp = document.createElement("span");
        sp.className = "st-mot"; sp.id = "st-g" + gi + "-m" + mi; sp.textContent = m.t;
        el.appendChild(sp);
      });
      zone.appendChild(el);
      const texte = g.mots.map((m) => m.t).join(" ").toUpperCase();
      // 855 px utiles ; divisé par l'échelle maximale d'un mot accentué (1,12)
      const taille = window.__hyperframes.fitTextFontSize(texte, { fontFamily: "Montserrat", fontWeight: 900, maxWidth: 855 / 1.12 });
      el.style.fontSize = taille.fontSize + "px";

      tl.set(el, { opacity: 1, visibility: "visible" }, g.start);                 // entrée franche du groupe
      g.mots.forEach((m, mi) => {
        const sp = "#st-g" + gi + "-m" + mi;
        // un mot long grossit moins : il ne prend jamais plus de AVANCE em de chaque côté, sinon il touche ses voisins
        const largeur = document.querySelector(sp).offsetWidth || 1;
        const echelle = Math.min(ECHELLE, 1 + (2 * AVANCE * taille.fontSize) / largeur);
        tl.to(sp, { color: ACCENT, scale: echelle, duration: 0.08, ease: "power2.out" }, m.s);   // le mot s'allume à son instant, jamais avant
        if (mi < g.mots.length - 1) tl.to(sp, { color: "#fff", scale: 1, duration: 0.1 }, m.e);
      });
      tl.to(el, { opacity: 0, duration: 0.12, ease: "power2.in" }, g.end - 0.12);
      tl.set(el, { opacity: 0, visibility: "hidden" }, g.end);                     // extinction franche, obligatoire
    });

    window.__timelines = window.__timelines || {};
    window.__timelines["sous-titres"] = tl;
  </script>
</template>
```

À savoir sur ce modèle :

- **Espace entre les mots.** Les mots sont créés par script, sans espace entre eux : seule la marge les sépare. Avec l'ancienne valeur (`margin: 0 0.12em`, contour de 6 px, échelle 1,12 pour tous), le mot actif recouvrait ses voisins : sur une capture de « UNE AUGMENTATION NETTE », 0 px entre les mots. Avec `0 0.22em`, un contour en `em` et l'agrandissement plafonné par `AVANCE`, la même capture laisse 13 à 32 px entre les mots, mot actif compris (rendu réel, mesuré sur 4 images). Ne pas redescendre sous `0.2em`, et garder le plafond si on change `ECHELLE`.
- Les groupes sont créés par script à partir d'un tableau figé : c'est la seule exception admise à « les éléments minutés sont écrits dans le HTML ». Ils ne portent pas la classe `clip` ; c'est la timeline qui les allume et les éteint, et `tl.set` peut poser `visibility` (un basculement instantané, pas une animation).
- Chaque groupe est en position absolue : dans une colonne flex, un groupe caché par `visibility` garde sa place et décale le suivant.
- Conteneur pleine largeur centré par l'alignement du texte. Jamais `left: 50%; transform: translateX(-50%)` (rogne aux bords). `overflow: visible`, sinon les mots agrandis et les lueurs sont coupés.
- Fondre le groupe **ou** ses mots, pas les deux (les opacités se multiplient).
- Un dégradé ou `background-clip: text` va sur le `span` intérieur, pas sur le conteneur transformé.
- Styles tout faits : `npx -y hyperframes@0.9.33 catalog --tag caption-style --json` puis `add <nom>` (liste dans `registry.md`). Un style installé se restyle ; on y injecte le même tableau de groupes.

## 4 bis. Modèle B : sous-titre fixe, un seul mot-clé coloré, aligné à gauche

Pour les styles où « le sous-titre est le plan » (fiche `info-sous-titres` de `styles-montage-documentaire`, explicatif posé) : le groupe entier arrive d'un coup, ne bouge pas pendant qu'on le lit, et un seul passage est coloré. Pas de mot actif, donc aucun risque de mots qui se touchent. Même hôte dans `index.html` que le modèle A. Rendu réel vérifié (`lint` 0 erreur, `check` sans erreur, texte de x = 90 à x = 915, bas du bloc à y = 1320, groupe éteint entre deux sous-titres).

```html
<!-- compositions/sous-titres.html -->
<template>
  <style>
    #root { position: absolute; inset: 0; }
    /* bas du bloc à y = 1320 ; le bloc grandit vers le haut quand il a deux lignes */
    .sf-zone { position: absolute; left: 90px; right: 135px; top: 1060px; height: 260px; overflow: visible; }
    .sf-groupe { position: absolute; left: 0; right: 0; bottom: 0; text-align: left; opacity: 0; visibility: hidden;
                 font-family: Montserrat; font-weight: 900; line-height: 1.16; color: #ffffff;
                 -webkit-text-stroke: 0.08em #000; paint-order: stroke fill; }
    .sf-ligne { display: block; white-space: nowrap; }
    .sf-cle { color: #FFD60A; }          /* à relier à la couleur d'accent de la chaîne */
  </style>
  <div id="root" data-composition-id="sous-titres" data-width="1080" data-height="1920">
    <div class="sf-zone" id="sf-zone"></div>
  </div>
  <script>
    // Un groupe = une ou deux lignes ; « cle » = le seul passage coloré du groupe (recopié à l'identique d'une ligne).
    const GROUPES = [
      { start: 0.20, end: 1.90, lignes: ["Une baguette", "sur dix est jetée"], cle: "sur dix" },
      { start: 2.00, end: 3.90, lignes: ["Soit 150 000 tonnes", "par an, déjà payées"], cle: "150 000 tonnes" },
    ];
    const zone = document.getElementById("sf-zone");
    const tl = gsap.timeline({ paused: true });

    GROUPES.forEach((g, gi) => {
      const el = document.createElement("div");
      el.className = "sf-groupe"; el.id = "sf-g" + gi;
      let taille = 84;                                             // corps de base ; jamais sous 42 px
      g.lignes.forEach((ligne) => {
        const dl = document.createElement("span"); dl.className = "sf-ligne";
        const i = g.cle ? ligne.indexOf(g.cle) : -1;
        if (i < 0) dl.textContent = ligne;
        else {
          const cle = document.createElement("span"); cle.className = "sf-cle"; cle.textContent = g.cle;
          dl.append(ligne.slice(0, i), cle, ligne.slice(i + g.cle.length));
        }
        el.appendChild(dl);
        const f = window.__hyperframes.fitTextFontSize(ligne, { fontFamily: "Montserrat", fontWeight: 900, maxWidth: 840, baseFontSize: 84 });
        taille = Math.min(taille, f.fontSize);                     // même corps pour les deux lignes
      });
      el.style.fontSize = taille + "px";
      zone.appendChild(el);

      tl.set(el, { opacity: 1, visibility: "visible" }, g.start);  // entrée franche : le texte ne bouge pas pendant qu'on le lit
      tl.set(el, { opacity: 0, visibility: "hidden" }, g.end);     // extinction franche, obligatoire
    });

    window.__timelines = window.__timelines || {};
    window.__timelines["sous-titres"] = tl;
  </script>
</template>
```

- **Un seul mot-clé par groupe** : le chiffre, le nom du sujet ou le mot de chute. Un groupe sans mot-clé (`cle` absent) est permis ; deux mots-clés, non.
- Chaque groupe tient au moins 1 s, plus 0,25 s par mot au-delà de trois (règle du temps de lecture) ; une fiche de style peut demander plus (`info-sous-titres` : 1,8 s).
- Fond du mot-clé au lieu d'une couleur de texte (pavé de surligneur) : `background: #FFD60A; color: #111; -webkit-text-stroke: 0; padding: 0 0.08em;` sur `.sf-cle`.
- Une fiche de style peut déplacer la zone ou changer l'entrée (bloc qui claque par 2 ou 3 mots), en restant dans la zone utile de `zones-interface.md` : c'est la fiche qui l'emporte sur ce modèle.
- Sur une image réelle, garder le contour ou poser un dégradé sombre sous le bloc ; ne pas cumuler les deux avec un voile.

## 5. Taille et placement

| | Vertical 1080×1920 | Paysage 1920×1080 |
| --- | --- | --- |
| Position | bas du groupe entre 1220 et 1320 px du haut (600 à 700 px du bas) | 80 à 120 px du bas |
| Largeur utile | 855 px (de x = 90 à x = 945, à l'intérieur de la zone utile 60 à 945 de `zones-interface.md`) | 1600 px |
| Taille | base 78 px, minimum 42 px (`fitTextFontSize`) | idem |

- Jamais sur le visage ni sur la bouche de la personne qui parle, surtout pendant la première seconde ; jamais sous la colonne de boutons de droite ; jamais dans les 360 px du bas.
- Sur une vidéo réelle, choisir d'après la luminosité (0 à 255) derrière le texte : sous 60, fusion `screen` ; de 60 à 180, `overlay` ; au-dessus de 180, couleur opaque. Sous-titres simples sur un fond de luminosité supérieure à 60 : un voile ajusté au texte (30 à 40 %), jamais une barre pleine largeur. Garder **un seul style de fond** pour toute la vidéo.
- Une vidéo source peut déjà contenir des sous-titres incrustés au milieu du plan : regarder une planche à 1 image par seconde avant de poser les siens.
- Mot mis en valeur : couleur d'accent, graisse ou échelle (jusqu'à ×1,15, plafonnée pour les mots longs comme dans le modèle A). Accentuer 5 à 20 % des mots (chiffres, nom du sujet, mot de chute), jamais deux groupes de suite au maximum d'effet.

## 6. Texte derrière la personne (option)

Empiler la vidéo, puis les sous-titres, puis un détourage de la personne (`npx -y hyperframes@0.9.33 remove-background`, 168 Mo au premier lancement, environ 2 images par seconde sur processeur), par `z-index`. Poser `data-layout-allow-occlusion` sur le détourage (sinon `check` signale `text_occluded`) et juger sur capture. Un grand mot derrière la tête se lit bien couvert à 30–55 % ; sous 15 % il flotte, au-delà de 65 % il est mangé.

## 7. Contrôle

1. Auto-contrôle dans le script, avant l'enregistrement de la timeline : positionner la timeline juste après chaque `g.end` et vérifier que le groupe est invisible (modèle dans `officiel/media-use/audio/references/captions/authoring.md`, « Caption Exit Guarantee »), puis `tl.seek(0)`. Si la composition contient un compteur ou une valeur écrite par `onUpdate`, écrire `tl.seek(t, false)` : `seek(t)` seul n'appelle pas `onUpdate` (`principes-mouvement/references/gsap.md`).
2. `npx -y hyperframes@0.9.33 check --json` (contraste, débordement, texte masqué).
3. Captures au milieu de 5 groupes répartis, dont le premier et le dernier : `snapshot --at <instants>` ; le mot allumé doit être celui qui est prononcé à cet instant.
4. Aucun groupe encore visible après la fin de la voix ; durée de la racine bornée à la durée `ffprobe` du son, sinon la vidéo finit sur du noir.

Erreurs fréquentes : mots qui se touchent quand le mot actif grossit (marge trop faible, agrandissement non plafonné) ; transcription en anglais (modèle oublié) ; mots inventés sur le silence final ; groupe resté affiché (extinction franche oubliée) ; mot qui s'allume avant d'être dit ; sous-titres dans la zone basse de l'application ; police de marque non embarquée (remplacée sans prévenir au rendu).
