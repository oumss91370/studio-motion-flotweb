# La commande `hyperframes` (0.9.33), par tâche

> Fichier modifié : résumé et adaptation en français, par Flot Web (2026), de la documentation HyperFrames 0.9.33 (Copyright 2026 HeyGen, Inc., licence Apache 2.0). Originaux non modifiés dans `officiel/`. Voir `NOTICE` à la racine du plugin.

Résumé en français de `officiel/hyperframes-cli/` (SKILL.md et références). Toutes les commandes s'écrivent `npx -y hyperframes@0.9.33 <commande>` ; ci-dessous le préfixe est abrégé en `hf` (ce n'est pas une commande réelle : toujours écrire le préfixe complet). Chaque commande accepte `--help` ; la plupart acceptent `--json`. Un échec affiche `✗ …`, une ligne `Fix:` et sort avec un code non nul.

Un résultat `--json` peut contenir `_meta.updateNotice` (nouvelle version disponible) : ne pas mettre à jour, le studio est épinglé.

## Créer

```bash
hf init ma-video --skip-skills --resolution portrait --non-interactive   # vertical vide
hf init ma-video --skip-skills --resolution portrait --audio voix.mp3 --model small --language fr
hf init ma-video --skip-skills --resolution landscape-1440p              # YouTube 1440p
hf capture https://exemple.fr --json -o capture-exemple                  # un site comme matière première
```

- Préréglages de `--resolution` : `landscape` (1920×1080), `portrait` (1080×1920), `square` (1080×1080), `landscape-1440p` (2560×1440), `portrait-1440p` (1440×2560), `square-1440p`, `landscape-4k`, `portrait-4k`, `square-4k`. Alias : `1080p`, `1440p`, `qhd`, `4k`, `uhd`.
- `--audio` ou `--video` transcrit le fichier à la création : toujours donner `--model small --language fr` pour du français (ou `--skip-transcribe`).
- Modèles d'exemple (`--example <nom>`, seulement si la personne le demande) : `blank`, `warm-grain`, `play-mode`, `swiss-grid`, `vignelli` (vertical), `decision-tree`, `kinetic-type`, `product-promo`, `nyt-graph`.
- `init` écrit `index.html`, `package.json`, `meta.json`, `hyperframes.json`, `CLAUDE.md` et `AGENTS.md`, et rien d'autre. Supprimer les deux derniers, retirer `"publish"` de `package.json`, passer `lang` à `fr`, créer `compositions/` et `assets/` (`../SKILL.md`, « Créer le projet »).
- `capture` : code de sortie non nul, `ok: false` ou fichier `BLOCKED.md` = arrêt net. Ne rien reprendre d'une capture bloquée ; réessayer dans un nouveau dossier `-o`.

## Lire un projet

```bash
hf info --json            # résolution, durée, nombre d'éléments, poids
hf compositions --json    # chaque composition avec durée et taille
hf timeline --json        # tous les clips : absStart, absEnd, file, src, volume
hf docs rendering         # documentation dans le terminal (sujets : data-attributes, examples, rendering, gsap, troubleshooting, compositions)
```

`timeline --json` ne lit qu'un niveau d'imbrication (`children=unread` au-delà). Toujours comparer avec `absStart` / `absEnd`, pas `start` / `end`.

## Contrôler

```bash
hf lint                   # pendant l'écriture
hf check --json           # la porte : lint, exécution, mise en page, contraste
hf check --json --timeout 60000   # page lourde
```

`validate`, `inspect` et `layout` sont d'anciens noms de `check` : ne pas les utiliser.

- `check` sort avec le code 1 seulement s'il reste une **erreur**. Les avertissements (`sweep_static`, `dead_stretch`, `nested_structure_needs_subcomposition`, `first_frame_empty`, `overlapping_gsap_tweens`…) laissent le code à 0 et `ok: true` : les lire dans `lint.findings`, `layout.findings` et `craft.findings`. `--strict` fait échouer aussi sur les avertissements (sauf ceux de `craft`).
- Options utiles : `--samples 15` (grille plus dense, 9 par défaut), `--at 1.5,4` (instants choisis), `--at-transitions`, `--snapshots` (images annotées), `--no-contrast` pendant les essais.
- Le rapport complet est aussi écrit dans `.hyperframes/artifacts/checks/`.

## Voir

```bash
hf snapshot --at 0,1.5,4            # images à ces secondes
hf snapshot --range 3,5             # une plage
hf snapshot --composition intro     # une scène
hf snapshot --review                # planche de relecture d'un film
hf snapshot --at 2 --zoom "#titre"  # détail agrandi (sélecteur CSS ou région x,y,l,h)
hf snapshot --against reference.mp4 # comparaison avec une vidéo de référence
hf keyframes                        # voir le mouvement (officiel/hyperframes/references/motion.md)
hf compare projet-a projet-b --at 2 --labels avant,apres --out compare.png   # deux versions, même instant
hf audio renders/ma-video.mp4 --json   # son présent, instants des attaques et des pics, silences
```

Le niveau sonore de référence du studio ne se lit pas dans `hf audio` mais avec `son/scripts/niveau.py` ou `scripts/verifier-export.py` (même mesure, `ebur128`).

Les PNG sont dans `.hyperframes/artifacts/snapshots/`. Les ouvrir : une capture non regardée ne vaut rien.

## Mesurer une vidéo existante : `measure`, `beats`, `diff`

Ces commandes lisent un **fichier vidéo** (une référence à étudier, ou son propre rendu) ; elles n'ont pas besoin d'un projet. Elles existent bien en 0.9.33 (liste de `--help` et essai réel sur un MP4 de test le 11/11). Sortie toujours en JSON pour `measure`. Aucune ne demande de compte.

```bash
hf measure probe video.mp4                                  # taille, cadence, durée, son, ce qu'il faut corriger avant de mesurer
hf measure cuts video.mp4                                   # coupes franches et plans ; éclairs et filés listés à part (not_cuts)
hf measure events video.mp4 --map --out analyse/events      # ce qui change à l'écran, avec les attaques du son et les fenêtres à regarder
hf measure frames video.mp4 --every 0.5 --width 270 --out analyse/planche    # planche : une image toutes les 0,5 s
hf measure frames video.mp4 --events --max 16 --width 270 --out analyse/bandes   # une bande d'images par évènement
hf measure frames video.mp4 --range 3.2,3.9 --out analyse/plan3              # images consécutives d'un passage
hf measure look video.mp4                                   # luminosité, contraste, saturation, part de noir et blanc, chaleur
hf beats video.mp4 --json                                   # temps de la musique d'un fichier (bpm, beatTimes)
```

| Sous-commande | Ce qu'elle mesure | Options principales |
| --- | --- | --- |
| `measure probe <vidéo>` | taille affichée, cadence, durée, présence de son, cadence variable ou HDR | `--normalize <fichier>` écrit une copie à cadence constante |
| `measure cuts <vidéo>` | coupes franches (différence d'image à image) et plans | `--start`, `--end` |
| `measure events <vidéo>` | coupes, éclairs, apparitions, disparitions, changements, tenues | `--map` (grille 4×4 + son), `--roi x,y,l,h`, `--grid 6x10`, `--thr` (défaut 5), `--out` |
| `measure frames <vidéo>` | images : instants choisis, planche, passage, bandes par évènement | `--at 1.2,3.4`, `--every N`, `--range a,b`, `--events`, `--max` (12), `--width` (360), `--roi`, `--out` |
| `measure extract <vidéo> --out <fichier>` | une image (`--at`) ou un extrait (`--from`, `--to`) recadré, comme média du projet | `--roi`, `--audio`, `--crf` (14) |
| `measure curve <vidéo>` | chaque mouvement d'un élément sur fond uni : départ, durée, dépassement, courbe GSAP la plus proche | `--roi` (obligatoire en pratique), `--start`, `--end`, `--bg`, `--compare <rendu>` |
| `measure energy <référence> <la-sienne>` | quantité de mouvement de deux vidéos et leur simultanéité | `--start`, `--seconds`, `--roi` |
| `measure ink <vidéo>` | boîte, taille et lignes d'un texte dans une région d'une image | `--at`, `--roi` |
| `measure look <vidéo>` | luminosité, contraste, saturation, chaleur d'une fenêtre | `--start`, `--end`, `--fps` (2), `--roi`, `--compare <autre vidéo>`, `--at` + `--grid 8x6` |
| `measure face`, `measure sync` | taille et place d'un visage ; décalage bouche / voix | `--samples`, `--roi` (bouche, obligatoire pour `sync`) |
| `beats [dossier ou fichier]` | temps de la musique : sur un projet, écrit `beats/<son>.json` pour la piste `data-timeline-role="music"` ; sur un fichier, imprime le résultat | `--json` |
| `diff <référence> [rendu ou projet]` | ressemblance image par image avec une référence (SSIM), pires instants | `--at`, `--range`, `--offset`, `--worst`, `--sbs`, `--out` |

- Chiffres relevés sur un film de test de 9 s (`pop-trame`) : `probe` donne 1080×1920, 30 i/s, 9,002 s ; `cuts` 7 coupes ; `events` 7 coupes, 4 apparitions, 14 changements ; `look` luminosité 157,9, saturation 0,536 ; `beats` 0 temps (film sans musique : `bpm: null`, ce n'est pas une panne).
- Sans `--out`, les images vont dans `.hyperframes/measure/<opération>` du dossier courant.
- Le script `formats-flotweb/scripts/analyse_reference.sh` enchaîne `probe`, `cuts`, `events`, `frames`, `beats` et `look` sur une vidéo de référence (73 s pour le film de 9 s), avec un repli FFmpeg si `measure` ne répond pas.
- `measure face`, `measure sync` et `diff --segments` servent surtout au parcours officiel « reverse » (payant) : le studio ne s'en sert pas par défaut. `reverse` et `templates` restent hors périmètre (règle 6).

## Modifier la timeline (ce que fait l'éditeur lui-même)

```bash
hf timeline ids                                   # pose les id manquants
hf timeline move "#outro" 9 --plan --json         # prévisualise ; relancer sans --plan pour appliquer
hf timeline move "#outro" after:#intro            # temps : 4.5, +1, 30f, end, after:#id, before:#id
hf timeline trim "#titre" --duration 2            # ou --start / --end
hf timeline split "#outro" 6.5
hf timeline set "#musique" volume=0.5             # volume, rate ou track
hf timeline delete "#outro" --json
hf timeline apply plan.json --json                # plusieurs modifications : [{"verb":"move","ref":"#outro","time":"9"}]
hf timeline undo recu.json                        # défait d'après le reçu imprimé
```

Une modification est refusée si le clip chevaucherait un voisin (`--overwrite`, ou déplacer le voisin d'abord) ou finirait après sa composition : monter d'abord le `data-duration` de la racine (aucune commande ne le change).

Historique du projet : `hf history begin --who <agent> --label "<plan>"` au début d'un tour, `hf history --since mine --who <agent>` pour voir les modifications de la personne, `hf history undo --who <agent>` si un contrôle échoue, `hf history end` à la fin.

## Aperçu

```bash
hf preview --background              # session persistante, port 3002 par défaut
hf preview --background --port 4567
hf preview --stop
hf preview --context --json --context-fields selection   # « cet élément » : ce que la personne a sélectionné
hf play                              # lecteur léger, port 3003, sans éditeur
```

Donner à la personne l'adresse du projet dans l'éditeur, pas le fichier `index.html` : `http://localhost:<port>/#project/<nom-du-dossier>`. Vérifier d'abord qu'elle répond (code 200) et la garder ouverte pendant toute la relecture. `no-selection` : demander à la personne de cliquer l'élément.

L'application de bureau HyperFrames (`hf open`) est une autre façon de continuer à modifier ; la proposer comme option, jamais comme obligation.

## Rendu

```bash
hf render --quality draft -o renders/essai.mp4        # essais rapides
hf render --quality delivery -o renders/final.mp4     # livraison
hf render -c compositions/intro.html -o intro.mp4     # une seule scène
hf render --variables-file valeurs.json -o v2.mp4     # autre texte, mêmes animations
hf render --batch lignes.json -o "renders/{name}.mp4" # série
hf render --format webm -o surimpression.webm         # fond transparent
```

| Option | Valeurs | Défaut | Remarque |
| --- | --- | --- | --- |
| `--quality` | `draft`, `looks`, `delivery` (anciens noms `standard`, `high`) | `looks` | `looks` = CRF 16 ; `delivery` pour le fichier final |
| `--fps` | 1 à 240 | `data-fps` de la racine, sinon 30 | 60 double le temps de rendu |
| `--format` | `mp4`, `webm`, `mov`, `gif`, `png-sequence`, `hls` | `mp4` | `webm` et `mov` gardent la transparence |
| `--resolution` | préréglages ci-dessus | — | sur-échantillonnage : même rapport d'image, facteur entier |
| `--crf` / `--video-bitrate` | 0 à 51 / `10M` | — | l'un ou l'autre |
| `--max-bitrate`, `--buffer-size` | `8M`, `16M` | — | MP4 : plafond de débit |
| `--keyframe-interval` | secondes | — | MP4 : une image clé au moins toutes les N secondes |
| `--chroma-subsampling` | `420`, `444` | `420` | nouveau en 0.9.32, voir plus bas |
| `--workers` | nombre ou `auto` | `auto` | un Chrome (≈ 256 Mo) par processus |
| `--browser-timeout` | secondes | 60 | page d'entrée lourde |
| `--strict`, `--strict-all` | — | non | échoue sur erreurs (et avertissements) de lint |
| `--docker` | — | non | sortie identique d'une machine à l'autre (Docker requis) |
| `--gpu` | — | non | encodage FFmpeg par la carte graphique |

Sans `-o`, le fichier va dans `renders/<projet>_<date>_<heure>.mp4`.

**1440p (nouveau en 0.9.26).** `landscape-1440p` (2560×1440), `portrait-1440p` (1440×2560), `square-1440p` ; alias `1440p` et `qhd` selon l'orientation du projet. Un projet 720p monte à 1440p (×2) ; un projet 4K y descend. **Un projet 1080p ne peut pas monter à 1440p** (4/3 n'est pas un facteur entier) : créer le projet en 1440p, ou rendre en 4K (`--resolution landscape-4k`) et réduire ensuite avec FFmpeg.

**Couleur 4:4:4 (nouveau en 0.9.32).** `--chroma-subsampling 444` garde toute la couleur (texte fin coloré, interfaces) pour un fichier maître qui sera réencodé. MP4 SDR et encodeur logiciel seulement ; refusé avec `--gpu` et `--hdr`. **Ne jamais publier ce fichier tel quel** : beaucoup de lecteurs et de plateformes ne lisent pas le 4:4:4. Le fichier publié reste en `420` (`yuv420p`).

**Lire la deuxième ligne du résumé.** Après le chemin et le poids, `render` imprime le mode de capture et les durées par étape, par exemple `beginframe capture · software gpu · compile 0.7s · setup 1.1s · capture 8.1s · encode 5.8s`. `screenshot capture` + `software gpu` sous Linux = chemin lent.

**Durée.** Un film de 30 s se rend en une à deux minutes : le lancer au premier plan. Ne détacher (`HYPERFRAMES_RENDER_DETACHED=1`, sortie dans un journal) que si le rendu dépasse le délai de l'outil, et attendre avec `until grep -qE 'Render (complete|failed)' render.log; do sleep 5; done` (jamais `pgrep -f`). Depuis la 0.9.27, un seul rendu à la fois par machine, que ce soit la CLI ou l'éditeur.

**Flou de mouvement.** Il se déclare dans la composition (`data-motion-blur="on"` sur la racine) ; `--page-motion-blur off` rend sans lui, pour comparer. Limites : `../SKILL.md`, « Flou de mouvement ».

**Débit.** `delivery` ne plafonne pas le débit : un film à grain ou à trame fine animée peut dépasser 30 Mbit/s (42 Mo pour 10 s sur un film de test). Pour un fichier publié : `--max-bitrate 8M --buffer-size 16M`.

Après le rendu : fichier non vide, durée `ffprobe` égale au `data-duration` de la racine, niveau du son réglé avec `son/scripts/finaliser.py`, fichier livré contrôlé, images décodées regardées (`exports.md`).

## Partager pour relecture : `share` (nouveau, remplace `publish`)

```bash
hf auth login                      # compte HeyGen (gratuit) : à faire par la personne
hf share --invite-only             # premier partage : --private, --invite-only, --team ou --public
hf share --status --json           # « ready: true » avant de dire que la vidéo est visible
hf share --update                  # renvoie une nouvelle version
```

- `share` envoie la vidéo sur les serveurs de HeyGen et donne un lien de relecture. **Ce n'est jamais automatique** : la personne doit le demander, avoir un compte, et choisir l'audience. `--public` (toute personne ayant le lien) seulement si elle le dit explicitement ; `--yes` ne vaut pas accord sur l'audience.
- Relancer `share` redonne le lien existant. Cinq projets gratuits gardés par espace de travail ; les versions ne consomment pas d'emplacement ; une limite horaire de versions existe.
- `publish` est l'ancien système (pages `/p/`, envoi du **code source**) : il reste disponible pendant une fenêtre de transition de 60 jours dont la date de début n'est pas encore fixée. Ne plus l'utiliser.
- Pour une simple relecture, préférer l'aperçu local ou l'envoi du MP4 : rien ne quitte la machine.

## Rendu ailleurs que sur la machine

`cloud render` (serveurs HeyGen, selon l'abonnement), `lambda render` (AWS de la personne), `cloudrun render` (GCP de la personne) : non utilisés par défaut par le studio. Références officielles : `officiel/hyperframes-cli/references/cloud.md`, `lambda.md`, `cloudrun.md`.

## Entretien

```bash
hf doctor --json          # toujours code 0 ; ok global presque toujours false (outils facultatifs) : lire Node.js, FFmpeg, FFprobe, Chrome
hf browser ensure         # « Source: cache » : Chrome déjà là, rien de téléchargé ; sinon téléchargement (réseau)
hf browser ensure --force # efface un téléchargement abîmé et recommence
hf browser path           # chemin du Chrome
hf telemetry status
hf clean --dry-run        # puis hf clean ; ne jamais supprimer .hyperframes
```

Ne pas lancer : `upgrade` (version épinglée), `skills`, `events`, `feedback`, `usage` (lit les identifiants de l'agent pour afficher un quota : inutile ici).

## Pannes

| Symptôme | Correction |
| --- | --- |
| `doctor` dit « Chrome not found » | `hf browser ensure` : il le retrouve en cache ou le télécharge ; relancer `doctor`. Sans réseau : `installation.md`, « Machine sans réseau » |
| Chrome qui ne démarre pas | `hf browser ensure --force` ; bibliothèques système manquantes sous Linux (`doctor` les nomme) ; ou `HYPERFRAMES_BROWSER_PATH` vers un Chrome qui marche |
| Page lourde pas prête | `--timeout` sur `check` / `snapshot` ; `--browser-timeout` sur `render` |
| Codec inhabituel, image vide | laisser `--proxy` actif (défaut) |
| Film long qui échouait avant la première image | corrigé en 0.9.32 (attente jusqu'à 15 min) |
| Voix coupée avant la fin (WAV mal étiqueté) | corrigé en 0.9.33 ; sinon reconvertir : `ffmpeg -i voix.wav -c:a pcm_s16le -ar 48000 voix-ok.wav` |
| Dernière image perdue sur une vidéo d'iPhone | corrigé en 0.9.28 |
| Deux rendus différents du même projet | corrigé en 0.9.25 (valeurs aléatoires à graine) ; vérifier l'absence de `Math.random()` sans graine |
| Aperçu 403 à distance | `HYPERFRAMES_PREVIEW_ALLOWED_HOSTS` |
| Mémoire insuffisante | fermer les autres Chrome, `--workers 1`, `--quality draft` |

Références officielles par commande : `officiel/hyperframes-cli/SKILL.md` (table « References »).
