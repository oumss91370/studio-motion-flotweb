# Références officielles HyperFrames : version et origine

| | |
| --- | --- |
| Logiciel | HyperFrames, © HeyGen Inc., licence Apache 2.0 (`LICENSE` dans ce dossier) |
| Dépôt | https://github.com/heygen-com/hyperframes |
| Version | **0.9.33** (version déclarée par `packages/cli/package.json`) |
| Commit copié | `ffb13c3b62a1b8ed98fdcd835f15412d0a7ca7e6`, du 11/11/2026 |
| Copie faite le | 11/11/2026, par Flot Web |
| Langue | anglais, **fichiers non modifiés** (fins de ligne LF d'origine) |

## Contenu

| Dossier | Origine dans le dépôt | Fichiers |
| --- | --- | --- |
| `hyperframes/` | `skills/hyperframes/` : `SKILL.md`, `references/` | contrat, format, mouvement, sous-titres, types de vidéos |
| `hyperframes-cli/` | `skills/hyperframes-cli/` : `SKILL.md`, `references/` | commandes |
| `hyperframes-registry/` | `skills/hyperframes-registry/` : `SKILL.md`, `references/`, `examples/` | blocs et composants |
| `media-use/` | `skills/media-use/` : `SKILL.md`, `references/`, `audio/references/` | médias, voix, étalonnage, mixage |
| `LICENSE`, `CREDITS.md` | racine du dépôt | licence Apache 2.0 et crédits des composants tiers |

## Ce qui n'a pas été copié, et pourquoi

- Scripts (`scripts/`), tests, tables de couleurs (`luts/`), chartes `assets/frame-presets/` : fournis chez le client par le paquet npm `hyperframes@0.9.33` ; les versions du dépôt sont en partie des relais vers la CLI.
- Bruitages `media-use/audio/assets/sfx/*.mp3` : licence Pixabay, redistribution isolée interdite.
- Skills `reverse-any-video` et `style-sampling` : fonctions de l'abonnement HyperFrames Pro, non redistribuées ; simplement mentionnées dans `../medias.md`.
- Skills `figma`, `slideshow`, `remotion-to-hyperframes` et skills internes de l'équipe : hors du périmètre du studio.

## Écart connu avec le paquet npm 0.9.33

Le commit copié est légèrement en avance sur le paquet npm `hyperframes@0.9.33` pour quatre fichiers de documentation : `hyperframes/references/plugin-installation.md`, `hyperframes-cli/references/doctor-browser.md` (FFmpeg hors du dossier du projet), `media-use/references/audio.md` et `media-use/references/operations.md` (`HYPERFRAMES_CLI_ENTRY`). Les consignes du studio (`../installation.md`) sont valables dans les deux cas.

## Comment lire ces fichiers

- Lire `npx hyperframes` comme `npx hyperframes@0.9.33`.
- Les règles du studio (`../../SKILL.md`) passent avant ces textes : format vertical par défaut, télémétrie coupée (ne pas exécuter les lignes « Usage beacon » ni `feedback`), pas d'installation de skills par la CLI, pas de fonctions payantes sans demande.
- Les liens `/hyperframes`, `/hyperframes-cli`, `/hyperframes-registry`, `/media-use` désignent les dossiers voisins ; `/reverse-any-video`, `/style-sampling`, `/figma`, `/slideshow`, `/remotion-to-hyperframes` ne sont pas fournis.
- Les chemins `scripts/…` et `assets/…` cités renvoient au paquet npm, pas à ce plugin.
