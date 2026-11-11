# Ce qui a changé entre HyperFrames 0.9.23 et 0.9.33

> Fichier modifié : résumé et adaptation en français, par Flot Web (2026), de la documentation HyperFrames 0.9.33 (Copyright 2026 HeyGen, Inc., licence Apache 2.0). Originaux non modifiés dans `officiel/`. Voir `NOTICE` à la racine du plugin.

Neuf versions publiées entre le 8 et le 11 novembre 2026 (0.9.25 à 0.9.33 ; il n'y a pas de 0.9.24). Source : journal officiel (`docs/changelog.mdx` du dépôt `heygen-com/hyperframes`) et comparaison des skills officiels 0.9.23 et 0.9.33. Ne sont listés que les changements qui touchent le travail du studio.

## À faire différemment

| Depuis | Changement | Conséquence pour le studio |
| --- | --- | --- |
| 0.9.32 | La CLI n'exécute plus un FFmpeg placé dans le dossier du projet ou le dossier courant | FFmpeg installé sur la machine, ou `HYPERFRAMES_FFMPEG_PATH` / `HYPERFRAMES_FFPROBE_PATH` vers un dossier hors projet (`installation.md`) |
| 0.9.30, 0.9.31 | L'aperçu et l'éditeur refusent les noms d'hôte inconnus (erreur 403) | à distance : `HYPERFRAMES_PREVIEW_ALLOWED_HOSTS=<hôte>` |
| entre 0.9.23 et 0.9.33 (textes officiels) | Nouvelle commande `share` (lien de relecture) ; `publish` devient l'ancien système | ne plus utiliser `publish` ; `share` seulement sur demande, audience choisie par la personne (`cli.md`) |
| 0.9.27 | Les skills officiels `reverse-any-video` et `style-sampling` entrent dans le jeu installé par défaut | fonctions Pro : non incluses ; toujours `init --skip-skills` |
| 0.9.27 | Un seul rendu à la fois par machine (CLI et éditeur partagent le même verrou) | ne pas lancer deux rendus en parallèle : le second attend |
| 0.9.32 | Le lint signale un script qui appelle `gsap` avant son chargement | charger GSAP avant les scripts de scène |
| 0.9.32 | Une composition ne peut lire que les fichiers de son propre dossier de projet (0.9.33 aussi) | tous les médias dans `assets/` du projet, jamais un chemin vers un autre dossier |

## Nouvelles possibilités

| Depuis | Nouveauté | Usage |
| --- | --- | --- |
| 0.9.26 | Préréglages 1440p : `landscape-1440p` (2560×1440), `portrait-1440p` (1440×2560), `square-1440p` ; alias `1440p`, `qhd` | YouTube en 1440p (`exports.md`) |
| 0.9.32 | `--chroma-subsampling 444` | fichier maître à réencoder ; jamais le fichier publié |
| 0.9.25 | `check` rejoue la dernière passe d'un projet inchangé ; option `--no-craft` | contrôles répétés plus rapides |
| 0.9.28 | La ligne `@hf-result` d'un rendu décrit le résultat du flou de mouvement | information pour un outil hôte |
| 0.9.27 | Le flou de mouvement de page est respecté dans les rendus répartis et par plage | cohérence du flou |
| 0.9.29 | Les prix d'images générées sont affichés comme estimations, avec le coût réel | seulement avec un compte HeyGen |
| 0.9.31 | Le rendu utilise la copie de GSAP fournie avec la CLI quand la page charge le fichier par défaut depuis le CDN | rendu possible sans réseau |

## Corrections qui comptent pour nous

| Version | Correction |
| --- | --- |
| 0.9.25 | Deux rendus du même film avec les mêmes réglages sont identiques (valeurs aléatoires à graine) |
| 0.9.25 | L'image d'une vidéo muette n'attend plus sa propre piste son à une coupe |
| 0.9.27 | Windows : chemins de plus de 260 caractères ; noms des miniatures SVG |
| 0.9.27 | macOS : plus de demande d'installation des outils de développement |
| 0.9.27 | `transcribe` lit les sorties Whisper contenant des valeurs invalides |
| 0.9.28 | Les clips courts de vidéos encodées par Apple (iPhone) gardent leur dernière image |
| 0.9.29 | Moins de rendus refusés à tort comme trop lents ; chaque image d'un clip vidéo montre sa propre image source |
| 0.9.31 | Safari : les longues vidéos ne sont plus chargées en entier dans l'aperçu |
| 0.9.32 | Les films longs, lents à s'ouvrir, n'échouent plus avant la première image (attente jusqu'à 15 min) |
| 0.9.33 | Un clip qui commence au milieu d'un WAV à l'en-tête erroné garde son son jusqu'au bout |
| 0.9.33 | Une vidéo ou un son posé par une variable est rendu à la bonne durée et au bon niveau |

## Différences dans les textes officiels (0.9.23 → 0.9.33)

- `hyperframes/SKILL.md` : trois lignes ajoutées à la table « What to read » (`/reverse-any-video`, `/style-sampling`, `references/look.md` pour reprendre le style d'un autre film sur un nouveau sujet).
- `hyperframes/references/skill-lifecycle.md` : jeu de skills par défaut élargi (voir plus haut).
- `hyperframes/references/plugin-installation.md` : npm est lancé depuis le dossier personnel ; le projet ne choisit plus la CLI.
- `hyperframes/references/motion.md` : une ligne sur le flou de mouvement.
- `hyperframes-cli/SKILL.md` et `references/preview-render.md` : `share`, préréglages 1440p, `--chroma-subsampling`.
- `hyperframes-cli/references/doctor-browser.md` : FFmpeg hors du projet.
- `media-use` : prix des images générées, variable `HYPERFRAMES_CLI_ENTRY` pour les scripts d'aide.
- `hyperframes-registry` : absent de l'ancien plugin en 0.9.23, ajouté ici.

## Reporter une future mise à jour

1. Lire le journal entre l'ancienne et la nouvelle version.
2. Remplacer `references/officiel/` par les fichiers de la nouvelle version, sans les modifier, et mettre à jour `officiel/VERSION.md` et `officiel/NOTICE.md`.
3. Comparer ancien et nouveau (`diff -r --strip-trailing-cr`), reporter les changements dans les fichiers en français et dans ce fichier.
4. Changer le numéro épinglé dans tout le skill, refaire le test de bout en bout de `installation.md` et un rendu vertical de référence.
