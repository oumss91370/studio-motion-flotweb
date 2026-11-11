# Crédits et licences : formats-flotweb

## Origine

Les cinq formats, leurs deux références et leurs deux scripts sont des créations de **Flot Web**, tirées des formats de production de son studio vidéo et **rendues génériques** : aucune référence à une série, un personnage, un compte, une voix, un dossier, un outil de publication ou un réglage de marque d'origine n'y figure. Chaque format lit la fiche « ma chaîne » du client (skill `marque`).

| Fiche ou fichier | Source (plugin d'origine de Flot Web) |
|---|---|
| `fait-3d-en-coupe` | fiche de production du format « fait en 3D vue en coupe » et son moteur |
| `lecon-pixel-art` | fiche de production du format « leçon en pixel art » |
| `science-pixel-art` | fiche de production du format « science en pixel art » et protocole de reproduction d'une référence |
| `histoire-2d-interactive` | fiche de production du format « histoire interactive en 2D », skill d'écriture d'histoire |
| `recreation-reel` | skill de recréation de reel (analyse, cahier de recréation, reconstruction, contrôles) |
| `references/mesurer-une-reference.md` | protocole de reproduction d'une référence, règles communes de production |
| `references/serie-a-votes.md` | skill d'écriture d'histoire et son gabarit de relecture |
| `scripts/analyse_reference.sh`, `scripts/controle_rendu.py` | scripts écrits par Flot Web (fins de ligne normalisées, en-tête ajusté) |

## Inspirations et outils de tiers

- **Superpowers** (https://github.com/obra/superpowers, commit `22f0b46`, © 2025 Jesse Vincent, MIT) : la méthode « regarder avant de demander, deux ou trois approches, document écrit, relecture par un regard neuf », adaptée au récit dans `references/serie-a-votes.md`. Aucun texte recopié.
- **ClaudeAnimationBase** (https://github.com/JohnHeibel/ClaudeAnimationBase, commit `0ac8bf2`, © 2026 John Heibel, MIT) et **lemo-opuscar** (https://github.com/lemomo-ai/lemo-opuscar, commit `9eb7739`, © 2026 LemoLab, MIT) : principes de jeu d'acteur et de direction cités dans `histoire-2d-interactive` ; ils sont portés par les skills `personnages` et `studio-coeur` (voir leurs fichiers de licences).
- **HyperFrames** (https://github.com/heygen-com/hyperframes, commit `ffb13c3`, Copyright 2026 HeyGen, Inc., Apache 2.0) : moteur et commandes d'analyse appelées par `scripts/analyse_reference.sh`, par l'intermédiaire du skill `rendu` (`licenses/rendu.md`).
- **three.js** (MIT) : bibliothèque 3D citée dans `fait-3d-en-coupe` et `recreation-reel` ; à embarquer avec sa licence dans le projet du client.
- **Polices citées** (Fredoka, Baloo 2, Patrick Hand) : SIL Open Font License.
- Numéros de mouvements `#001` à `#192` : dictionnaire du skill `principes-mouvement` (showheyohtaki/motion-prompt, commit `7819d38`, © 2026 Shohei Ohtaki, MIT).

## Ce que ces formats ne contiennent pas

- Aucun personnage, mascotte, logo, voix, musique ou texte d'un autre créateur : les comptes qui ont inspiré ces formats ne sont ni nommés ni cités en aperçu.
- Aucun aperçu de tiers : les aperçus seront produits avec le plugin.
- Aucun identifiant de voix, de compte ou de service, aucun chemin de dossier, aucun jeton.
