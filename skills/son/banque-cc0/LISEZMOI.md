# Banque de bruitages CC0 (109 sons)

Tous les fichiers de ce dossier sont sous **CC0 1.0** (domaine public) : utilisables, modifiables et redistribuables sans condition, y compris dans une vidéo monétisée ou vendue. Le crédit n'est pas obligatoire ; il est donné quand même, fichier par fichier, dans `LICENSES.md`.

Origine : banque réunie par Bart pour son skill `sound-effects` (dépôt `Barty-Bart/motion-graphics`, commit `3d83d98`, 13/10/2026 ; code sous MIT, `LICENSE-code-MIT.txt`). Sources : paquets audio de Kenney (kenney.nl) et sons Freesound dont la page affichait CC0, vérifiés par lui un à un le 12/10/2026. Fichiers copiés sans modification.

## Contenu

| Dossier | Nombre | Pour |
| --- | --- | --- |
| `kit/` | 6 | un son par usage, choisi en premier : `whoosh`, `click`, `pop`, `riser`, `impact`, `tick` |
| `click/` | 8 | clics, sélections, bascules d'interface |
| `tick/` | 3 | tics très courts (survol, petit élément) |
| `ui-blip/` | 11 | signaux d'interface à hauteur (plutôt styles jeu, rétro, technologie) |
| `pop/` | 15 | apparitions de cartes, pastilles, bulles |
| `ding/` | 9 | tintements, confirmations, verre |
| `whoosh/` | 7 | souffles, mouvements rapides |
| `transition/` | 12 | glissements, balayages, défilements |
| `riser/` | 12 | montées avant un moment fort |
| `impact/` | 11 | coups, impacts graves, explosions sourdes |
| `typing/` | 5 | frappes au clavier (prises longues à découper) |
| `glitch/` | 7 | parasites, rembobinage, bruits d'ordinateur |
| `ambience/` | 3 | silence de pièce (fond très bas, 17 à 20 s) |

`manifest.json` décrit chaque fichier (catégorie, durée, auteur, page d'origine, licence) et propose des catégories de remplacement (`alt_categories`).

## Utiliser

1. Copier les fichiers choisis dans `assets/sfx/` du projet vidéo (un rendu ne lit que les fichiers du projet).
2. Mesurer avant de placer : `python3 ../scripts/caler.py attaque <fichier>`.
3. Caler et vérifier le budget : étapes 4 et suivantes du skill.

Format : OGG Vorbis ; coups isolés rognés et normalisés en crête (jusqu'à 0 dBFS pour certains : toujours régler le gain, ne jamais les poser à plein volume) ; 4 s au plus (montées 6 s, ambiances 20 s à −35 LUFS). Ce sont des aperçus compressés : l'original sans perte se télécharge sur la page d'origine indiquée dans le manifeste.

## Ce que la banque ne contient pas

- **Aucun fichier Mixkit.** La section `runtime` du manifeste liste 40 adresses de sons Mixkit que le skill d'origine télécharge au moment de produire. Leur licence permet l'usage dans une vidéo mais interdit la redistribution : ils ne sont pas ici, et s'ils sont téléchargés chez la personne, ils restent dans son projet (`../references/sources-libres.md`). Le son de frappe « par défaut » du kit d'origine est dans ce cas : utiliser à la place un fichier de `typing/`.
- Pas de bruitages de matières (pas, tissu, bois, eau), pas de voix, pas de musique : à chercher dans les sources libres.

## Limites

Banque pensée pour des vidéos d'interface et d'explication. Beaucoup de sons Kenney sont des sons de jeu, au caractère synthétique : parfaits pour un style rétro ou une interface, à éviter pour un style peint, un conte ou un documentaire, où il faut des matières réelles.
