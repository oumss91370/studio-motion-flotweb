---
name: son
description: "À utiliser dès qu'une vidéo du studio a besoin de son (bruitages, ambiance, musique, mixage, niveau final) ou que la personne dit que le son est trop chargé, en retard, répétitif, pas adapté ou trop faible. Vrais enregistrements d'abord, environ 5 bruitages par 10 s calés sur l'image de l'impact, synthèse en repli, calage sur le beat et le drop, niveau final réglé après le rendu (−14 LUFS avec voix ou musique, règle de crête sans), écoute et correction mesurées avec earshot."
---

# Son : équilibré, calé sur l'image, mesuré

Tu ne peux pas entendre. Chaque décision sur le son s'appuie sur une mesure, et le rapport cite le chiffre (« −14,1 LUFS, crête −1,8 dBTP ; décalage +12 ms ; 4,6 bruitages par 10 s »). Ne dis jamais qu'un son « sonne bien » : dis ce qui a été mesuré, et que cela a été mesuré, pas écouté.

Ce skill s'applique à toutes les vidéos du studio ; la fiche de chaque style (section 7, « Son ») précise l'ambiance, les matières et la musique propres au style. Le rendu et le mixage dans la composition relèvent du skill `rendu`.

## Les 12 règles

1. **Vrais enregistrements d'abord.** Banque CC0 fournie (`banque-cc0/`), puis sources libres vérifiées (`references/sources-libres.md`). La synthèse est un repli, jamais le premier choix (règle 12).
2. **Pas un son par événement.** Chaque son a une cause visible à l'écran, mais tout événement n'a pas de son. Budget : **environ 5 bruitages par 10 s** (plage normale 3 à 8), regroupés là où la voix et la musique laissent de la place, plus rares après le moment fort.
3. **Coupes muettes par défaut** : environ 85 % des coupes n'ont pas de son à elles. **Whoosh : 2 à 3 par vidéo**, sur les vrais grands mouvements (balayage, zoom, transition majeure).
4. **Une seule palette de matières** par vidéo (bois et tissu, verre et plastique, métal et air…). **Le clic d'interface est l'exception à la règle 5** : même prise et même niveau à chaque clic du film (un bouton ne change pas de voix).
5. **Varier sans hasard** : toute autre action répétée (pop, impact, pas, whoosh) puise dans 2 à 4 prises ou plus, jamais deux fois la même de suite, ±1 à 2 dB, ±0,5 demi-ton au plus. Une série qui monte (cartes qui arrivent) monte de 1 à 3 demi-tons. Jamais le même son en mitraillette.
6. **Taille de la cause = taille du son** : un détail chuchote, le moment fort frappe. Le moment le plus fort tombe sur le sommet du film (entre 30 et 60 % de la durée), jamais sur la fin ni sur le logo.
7. **Silences voulus** : un vrai silence avant le moment fort ; le premier son après un silence compte double. Pas de bruitage fort sous les premiers mots de la voix.
8. **Calage : attaque sur l'impact, +8 ms, jamais avant.** L'attaque d'un coup, d'un clic, d'un pop se pose 8 ms après l'image du contact (ou à 50 % du trajet d'une apparition). Au contrôle du rendu, une attaque mesurée avant l'image (au-delà des 10 ms de précision de la mesure) ou plus de 75 ms après se recale. Seuls les sons qui s'établissent lentement commencent avant : le whoosh, dont le **pic** tombe sur le pic de vitesse du mouvement, et la montée, qui **finit** 30 à 250 ms avant l'impact. Les instants viennent du **code de la vidéo**, jamais d'un nombre tapé au jugé.
9. **Niveaux par rapport au fond, pas fixes** : chaque bruitage 3 à 10 dB au-dessus de la musique ou de l'ambiance à l'instant où il tombe ; baisser la musique de 6 à 12 dB pendant 0,3 à 0,5 s avant un impact ou un drop, pas sous chaque bruitage. Sous une voix : musique environ 11 dB dessous (9 à 14).
10. **Rien d'agressif entre 2 et 6 kHz** (fatigue sur téléphone) ; un fond dont l'énergie est presque toute sous 150 Hz ne s'entend pas sur un téléphone. Bruitages secs, mono, centrés ; seuls whoosh, montées, ambiances et musique sont larges.
11. **Niveau final, réglé après le rendu (étape 7).** Film **avec voix ou musique** : −14 LUFS intégrés (±1), crête à −1 dBTP ou moins sur le MP4 publié (−1,5 sur le fichier maître). Film **sans voix ni musique** : pas de cible LUFS ; un gain constant qui amène la crête du bruitage le plus fort entre −3 et −1 dBTP, jamais au-dessus de −14 LUFS, aucun limiteur, et le fond entre les sons au moins 20 dB sous le son le plus fort (on ne remonte pas le silence) ; ce film sort en **jaune**. Fin : une queue qui s'éteint dans le silence, jamais un son coupé net.
12. **Synthèse en repli seulement** : quand aucun enregistrement libre ne convient ou qu'il n'y a pas de réseau. Moteur `scripts/sfx/` (Python standard). Le dire dans la note de livraison.

Détail, valeurs et sources de chaque règle : `references/regles.md`.

## Deux parcours

| | Parcours simple (par défaut) | Parcours complet |
| --- | --- | --- |
| Pour | vidéo courte, peu de sons, machine modeste | film soigné, musique montée à l'image, plusieurs tours de critique |
| Outils | FFmpeg, Python standard, CLI HyperFrames | earshot + la chaîne « real-sound » (Python 3.10+, environ 2 Go de modèles) |
| Mixage | balises `<audio>` dans la composition | fichier de conception JSON, mixeur déterministe, contrôles reliés à chaque placement |
| Lire | la suite de ce fichier | `references/chaine-complete.md`, `references/earshot.md` |

Dans les deux cas : mêmes règles, même cible, mêmes étapes.

## Les étapes

Les scripts sont dans `${CLAUDE_PLUGIN_ROOT}/skills/son/scripts/` ; les fichiers de travail vont dans le dossier `audio/` du projet vidéo.

### 1. Liste des événements (`audio/cues.json`)

Tirer du code de la vidéo (timeline GSAP, images clés Blender) chaque instant utile : contact, apparition (50 % du trajet), pic de vitesse d'un mouvement, coupe, moment fort, mot clé de la voix. Un identifiant stable par événement, de la forme `action:objet:numéro` (`pop:carte:2`). Format : `references/regles.md` (« Liste des événements »).

### 2. Brief et budget (`audio/BRIEF-SON.md`)

Pour chaque événement : le son voulu **ou « rien »**. Fixer la palette de matières, l'ambiance, la musique (tempo, moment où elle change), le moment fort. Compter avant de chercher des sons : bruitages par tranche de 10 s, whoosh, coupes sonorisées. Budget dépassé : retirer d'abord les sons des coupes et des petits mouvements. Montrer le brief à la personne pour une vidéo nouvelle.

### 3. Trouver les sons (vrais enregistrements d'abord)

1. `${CLAUDE_PLUGIN_ROOT}/skills/son/banque-cc0/` : 109 sons CC0 (clic, pop, whoosh, transition, montée, impact, tintement, frappe, signal d'interface, glitch, ambiance), prêts à copier dans `assets/sfx/` du projet. Index : `${CLAUDE_PLUGIN_ROOT}/skills/son/banque-cc0/LISEZMOI.md`. La banque n'a ni matières (tasse, pas, papier, bois), ni instruments, ni musique : quand une fiche de style en demande, `references/sons-manquants.md` donne le plus proche, une recette, ou l'endroit où chercher.
2. Sinon : Freesound (CC0 de préférence, CC BY avec crédit), Kenney, musique d'auteurs en CC BY ; Mixkit et Pixabay sont permis **dans la vidéo** mais se téléchargent chez la personne, pour ce projet seulement. Licence lue sur la page du fichier et notée (`references/sources-libres.md`).
3. Mesurer chaque candidat : `python3 "${CLAUDE_PLUGIN_ROOT}/skills/son/scripts/caler.py" attaque <fichier>` (attaque, pic, fin, durée) ou `npx hyperframes@0.9.33 audio <fichier> --json`. Avec earshot : `earshot rank`, `find`, `realness`.
4. Rien ne convient : synthèse en repli (`references/synthese-repli.md`).

Interdits : extraire le son d'une vidéo d'autrui ; licence NC, ND, SA ou inconnue ; garder ou republier les fichiers Mixkit ou Pixabay hors du projet.

### 4. Caler et placer

Écrire `audio/plan.json` (événement, instant, fichier, type, gain), puis :

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/son/scripts/caler.py" placer audio/plan.json --html --out audio/placements.json
python3 "${CLAUDE_PLUGIN_ROOT}/skills/son/scripts/budget.py" audio/placements.json --duree <durée du film en s>
```

Les commandes se lancent depuis le dossier du projet, avec `PYTHONDONTWRITEBYTECODE=1` dans l'environnement. Dans le plan, `fichier` est un chemin depuis le dossier du projet (`assets/sfx/pop.ogg`).

`caler.py` calcule le début de chaque fichier pour que son attaque (ou son pic, ou sa fin) tombe au bon endroit (règle 8) et imprime les balises `<audio>` prêtes à coller dans `index.html` : `src` relatif à `index.html`, `data-duration` mesurée, une piste par son à partir de `--piste` (20 par défaut ; changer si l'image occupe déjà ces pistes). Collées telles quelles, elles ne donnent aucun avertissement audio à `lint` ni à `check` (vérifié en 0.9.33). Types reconnus : sons à attaque (`impact`, `clic`, `pop`, `bip`, `pose`, `tic`, `ding`…), `whoosh` / `transition` (pic), `montee` (fin), `ambiance` / `musique` / `fond` (début) ; un type inconnu est traité comme un son à attaque et signalé. `budget.py` refuse un mix trop chargé (plus de 8 par 10 s), trop de whoosh, une prise répétée (hors clic), une mitraillette ; sous 3 par 10 s il signale un film calme sans le refuser.

Musique : `data-timeline-role="music"` sur sa balise ; la poser pour que son drop tombe sur le moment fort (`references/beat-et-drop.md`) :

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/son/scripts/trouver-drop.py" assets/musique.mp3 --drop-film <instant du moment fort>
npx hyperframes@0.9.33 beats --json
```

### 5. Mixer

Dans la composition : `data-volume` par son (gains du plan), enveloppe `data-automation` sur la musique pour la baisser sous la voix et avant l'impact, `data-fade-out` en fin de film. Niveaux de départ : musique seule 0,5 ; musique sous une voix 0,14 à 0,25 ; bruitages 0,25 à 0,6 ; ambiance 0,1 à 0,2. Puis ajuster par la mesure (règle 9), pas à l'oreille supposée.

Ici on règle l'**équilibre** entre les sons, pas le niveau du film : le mixeur de HyperFrames plafonne la crête à −1 dBTP, et monter tous les `data-volume` ne mène pas plus haut qu'environ −19,5 LUFS (mesuré). Le niveau final se fait à l'étape 7, après le rendu. Un ton de pièce de la banque (−35 LUFS) reste à `data-volume` 1 au plus : monté pour « remplir », il devient du souffle.

**Pas de musique ni de voix ?** Trois issues, à choisir au brief : une vraie musique libre (`references/sources-libres.md`) ; un fond de repli du studio (`${CLAUDE_PLUGIN_ROOT}/skills/son/fonds/` : nappe calme, pulsation légère, tension, rétro « puce », bouclables, à copier dans `assets/musique/` ; qualité de repli, à dire dans la note) ; ou aucun fond, et le film suit la règle « sans voix ni musique » (règle 11, feu jaune).

### 6. Écouter et corriger (au moins 2 tours)

Rendre un brouillon (`render --quality draft`), puis mesurer **le fichier rendu** :

```bash
npx hyperframes@0.9.33 audio renders/essai.mp4 --json                       # son présent, attaques, niveau
npx hyperframes@0.9.33 audio --range 7,9 --only onsets                      # les coups autour d'un événement
python3 "${CLAUDE_PLUGIN_ROOT}/skills/son/scripts/niveau.py" mesurer renders/essai.mp4      # équilibre et crête ; le niveau du film se règle à l'étape 7
```

Avec earshot (recommandé dès qu'il est installé, `references/earshot.md`) :

```bash
earshot timeline renders/essai.mp4 --cues audio/cues.json --json --out audio/ecoute.json
earshot sheet renders/essai.mp4 -o audio/ecoute.png --cues audio/cues.json      # OUVRIR la planche
python3 "${CLAUDE_PLUGIN_ROOT}/skills/son/scripts/recaler.py" audio/ecoute.json audio/placements.json          # corrige les décalages mesurés
```

| Constat | Correction |
| --- | --- |
| Attaque avant l'image (plus de 10 ms) ou plus de 75 ms après | déplacer **le son**, pas l'image, de l'écart mesuré (`recaler.py`) |
| Trop chargé | retirer les sons les moins utiles : coupes, petits mouvements, doublons |
| Masqué (moins de +3 dB au-dessus du fond) | monter, éclaircir, ou déplacer hors de la voix |
| Pas adapté (matière hors palette) | changer de prise |
| Répétitif | alterner les prises, varier de ±1 à 2 dB |
| Trop faible ou trop fort | étape 7 |

Changer une chose à la fois, puis mesurer de nouveau.

### 7. Niveau final et contrôle (après le rendu final)

Une commande : elle extrait le son du MP4 rendu, règle le niveau, remonte le son sur l'image **copiée sans réencodage**, vérifie que l'image est restée identique et imprime les mesures avant / après.

```bash
S="${CLAUDE_PLUGIN_ROOT}/skills/son/scripts"
# film avec voix ou musique : -14 LUFS, crête <= -1 dBTP
PYTHONDONTWRITEBYTECODE=1 python3 "$S/finaliser.py" renders/final.mp4 -o renders/final-livre.mp4
# film sans voix ni musique : gain constant seul, feu jaune
PYTHONDONTWRITEBYTECODE=1 python3 "$S/finaliser.py" renders/final.mp4 -o renders/final-livre.mp4 --sans-fond
# film sans musique auquel on ajoute un fond au dernier moment (en boucle, 10 dB sous le son le plus fort)
PYTHONDONTWRITEBYTECODE=1 python3 "$S/finaliser.py" renders/final.mp4 -o renders/final-livre.mp4 --fond assets/musique/nappe-calme.ogg
```

Les mêmes étapes à la main (ce que fait le script) :

```bash
ffmpeg -y -i renders/final.mp4 -map 0:a:0 -vn -ar 48000 -c:a pcm_s24le audio/extrait.wav          # 1. extraire
python3 "$S/niveau.py" masteriser audio/extrait.wav -o audio/maitre.wav                           # 2. régler (ajouter --sans-fond s'il n'y a ni voix ni musique)
ffmpeg -y -i renders/final.mp4 -i audio/maitre.wav -map 0:v:0 -map 1:a:0 -c:v copy \
       -c:a aac -b:a 192k -ar 48000 -movflags +faststart renders/final-livre.mp4                  # 3. remonter, image copiée
python3 "$S/niveau.py" mesurer renders/final-livre.mp4                                            # 4. mesurer le fichier livré (ajouter --sans-fond si c'est le cas)
```

Si à l'étape 4 la crête dépasse −1 dBTP (l'AAC déplace les crêtes, jusqu'à +1,7 dB mesuré), refaire 2 et 3 avec `--plafond -2.5`. `finaliser.py` fait cette boucle seul.

| Ce que dit le script | Décision |
| --- | --- |
| FEU VERT | livrer `final-livre.mp4` ; recopier les chiffres dans la note |
| « le limiteur devrait retirer plus de 6 dB », film sous la cible, FEU ROUGE | le mix est trop creux pour −14 LUFS : ajouter un fond (dans la composition de préférence, sinon `--fond`), ou le déclarer `--sans-fond`. `--forcer` atteint −14 mais écrase : sur les films de test, plancher remonté de 14 à 17 dB, facteur de crête des coups réduit de 7 à 11 dB, limiteur actif jusqu'à 34 % du temps |
| FEU JAUNE (`--sans-fond`) | livrable ; écrire dans la note « film sans voix ni musique : niveau réglé sur la crête, x LUFS » |
| « silence remonté » (`--sans-fond`) | le ton de pièce est à moins de 20 dB sous le son le plus fort : le baisser dans la composition (`data-volume` 1 au plus) et rendre à nouveau |

Méthode de mesure (la même partout, décrite en tête de `niveau.py`) : `ffmpeg -i <fichier> -map 0:a:0 -af ebur128=peak=true -f null -`, lignes `I:`, `LRA:` et `Peak:` du résumé. Ne pas se fier à `loudnorm` pour mesurer un film court (jusqu'à 0,8 LU d'écart). Chiffres des essais et effets attendus à l'écoute : `references/regles.md` (« Niveau final »).

### 8. Crédits et note de livraison

`audio/CREDITS.md` : pour chaque son utilisé, titre, auteur, adresse de la page, licence, « modifié ». Les crédits CC BY vont **dans la description de la vidéo**. Note : budget réel (bruitages par 10 s, whoosh), événements recalés, niveaux mesurés sur le MP4 livré (LUFS, crête, profil « avec voix ou musique » ou « sans »), part de synthèse et fond de repli s'il y en a un, et la phrase « niveaux mesurés, non écoutés ».

## Fichiers du skill

| Chemin | Rôle |
| --- | --- |
| `scripts/caler.py` | mesure d'un son ; calage sur l'image ; balises `<audio>` |
| `scripts/budget.py` | contrôle du budget de bruitages |
| `scripts/trouver-drop.py` | drop d'une musique par l'énergie ; où poser la musique |
| `scripts/niveau.py` | mesure LUFS / crête vraie / plancher (méthode de référence) ; réglage par gain constant, plafond tenu ; règle `--sans-fond` |
| `scripts/finaliser.py` | niveau final en une commande : MP4 rendu → MP4 livré (image copiée), mesures avant / après |
| `fonds/` | 4 fonds de repli bouclables fabriqués par le studio (`LISEZMOI.md`, `fabriquer.py`) |
| `scripts/recaler.py` | correction des décalages d'après l'écoute earshot |
| `scripts/sfx/` | moteur de synthèse de repli (whaleyxbt, MIT), exemple dans `scripts/exemples/` |
| `banque-cc0/` | 109 bruitages CC0 redistribuables (banque de Bart, sources Kenney et Freesound) |
| `references/regles.md` | les règles en détail, la carte « image → son », la liste des événements |
| `references/sources-libres.md` | où chercher, quelles licences, comment créditer |
| `references/beat-et-drop.md` | caler le film sur la musique |
| `references/synthese-repli.md` | quand et comment synthétiser |
| `references/sons-manquants.md` | son demandé par une fiche → son de la banque le plus proche, recette de synthèse, ou où le chercher |
| `references/earshot.md` | installer earshot, l'utiliser, lire ses chiffres |
| `references/chaine-complete.md` | la chaîne « real-sound » résumée |
| `references/officiel/` | earshot et real-sound d'origine, en anglais (version dans `VERSION.md`) |

Tous les scripts de `scripts/` (hors `references/officiel/`) n'utilisent que Python 3 standard et FFmpeg.

## Erreurs fréquentes

- Un son sur chaque coupe et chaque apparition : le premier signe d'un montage automatique.
- Le même whoosh à chaque transition.
- Un son placé par le début de son fichier alors que son attaque est 40 ms plus loin : mesurer, puis caler.
- Une musique qui démarre sur son introduction calme : entrer sur sa partie la plus forte, drop sur le moment fort.
- Un mix de coups isolés poussé à −14 LUFS par un limiteur (`--forcer`) ou par un ton de pièce monté : ajouter un vrai fond, ou appliquer la règle « sans voix ni musique ».
- Chercher −14 LUFS en montant les `data-volume` : plafond vers −19,5 LUFS ; le niveau se règle après le rendu (étape 7).
- Un son posé « un peu avant pour anticiper » : jamais avant l'image.
- Niveau mesuré sur le WAV et pas sur le MP4 publié.
- Fichiers Mixkit ou Pixabay copiés dans un modèle, un dépôt ou un autre projet.

## Crédits

Règles et scripts : Flot Web, d'après earshot et real-sound (Leon Lin, MIT), claude-motion (whaleyxbt, MIT), claude-motion-design (Howseen AI, MIT), motion-graphics (Bart, MIT ; sons CC0), HyperFrames (HeyGen, Apache 2.0). Détail : `licenses/son.md` à la racine du plugin.
