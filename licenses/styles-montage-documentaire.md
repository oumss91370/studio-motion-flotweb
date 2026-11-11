# Crédits et licences : styles-montage-documentaire

Les fiches de cette catégorie sont des adaptations en français par Flot Web (traduction, généralisation, mise en page 9:16, numéros du dictionnaire de mouvements, moteur HyperFrames ou Blender, règles de son du plugin). Aucun code source des dépôts n'est recopié tel quel : les extraits des fiches sont des réécritures courtes des techniques décrites.

## lemomo-ai/lemo-opuscar

- Dépôt : https://github.com/lemomo-ai/lemo-opuscar · commit `9eb7739a0fca4c6990fe966cb8b87b1930f7193a`
- Code et textes (dont les `STYLE.md`) : **licence MIT**, © 2026 LemoLab. La notice MIT complète doit figurer dans les licences du plugin.
- Films et images de démo : **CC BY 4.0** (https://creativecommons.org/licenses/by/4.0/). Crédit à afficher : « LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0 ». Signaler toute modification.
- **Matériel de tiers dans les démos de ces deux catégories** (rushes, photos, archives, imagerie, données, fichiers de matériel ouvert) : il garde sa propre licence, avec attribution par plan dans le `demo/CREDITS` de chaque style. Les fiches n'en reprennent rien ; les films ne sont cités que par un lien. Ne pas en extraire de plans, ne pas les réhéberger.
- **Exclusion de voix** : la piste de voix du film `news-package` n'est pas couverte par la CC BY 4.0 (voix d'un service en ligne). Ne pas rediffuser ce film avec son son ; la fiche `habillage-jt` ne renvoie qu'à l'affiche et à la galerie.
- **Marques et noms réels dans les démos** (exemples de style, jamais visuels promotionnels) : `news-package` (sociétés et médias cités), `telestrator` (club, diffuseur), `countdown` (agence spatiale). Ne pas les afficher en vitrine.

| Fiche | Source |
|---|---|
| `info-sous-titres` | `styles/caption-news/` |
| `actualites-1920` | `styles/newsreel/` |
| `compte-a-rebours-direct` | `styles/countdown/` |
| `symphonie-time-lapse` | `styles/city-symphony/` |
| `enquete-visuelle` | `styles/visual-investigation/` |
| `montage-constructiviste` | `styles/kino-montage/` |
| `palette-tactique-sport` | `styles/telestrator/` |
| `habillage-jt` | `styles/news-package/` |
| `briefing-satellite` | `styles/satellite-briefing/` |
| `tableau-de-briefing` | `styles/briefing-board/` |
| `releve-lidar` | `styles/lidar-survey/` |
| `maquette-blanche-projetee` | `styles/white-model/` |
| `donnees-en-objets` | `styles/data-physical/` |
| `vue-eclatee` | `styles/teardown/` |
| `recit-au-microscope` | `styles/microscope/` |
| `table-lumineuse-archives` | `styles/archive-lighttable/` |

`references/materiel-et-droits.md` réunit les sections « Material », « Footage », « Facts » et « Pitfalls » de ces seize fiches, plus DIRECTOR.md (temps de lecture, cartes, droits).

## nateherkai/hyperframes-student-kit (« Herk Edit Kit »)

- Dépôt : https://github.com/nateherkai/hyperframes-student-kit · commit `10511e5af86fc47756ea89803b397422e2d89284` (14/10/2026)
- Kit d'origine : **licence MIT**, © 2026 Nate Herk.
- Ajouts « pipeline » (skills de montage, flux court, playbook) : permission d'usage du kit, **à conserver telle quelle lors de toute redistribution** :

> Herk Edit Kit Use Permission
>
> Copyright 2026 the contributors to this teaching kit.
>
> Permission is granted to students and other recipients to use, copy, modify, and share the original teaching-kit code, templates, and documentation, and to use them to produce personal or commercial videos. Retain this notice when redistributing the kit or substantial portions of its source materials.
>
> Third-party software, fonts, and assets remain subject to their respective licenses. No rights to third-party trademarks, likenesses, or excluded media are granted. See THIRD_PARTY_NOTICES.md.
>
> THE MATERIAL IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND. THE CONTRIBUTORS ARE NOT LIABLE FOR CLAIMS OR DAMAGES ARISING FROM ITS USE.

- **Non repris** : les copies des skills HyperFrames et GSAP du kit (anciennes), la marque et les éléments visuels de l'auteur, les vidéos d'exemple et de vitrine (droits réservés), les noms de styles qui citent des tiers, les scripts (seuls les règles et les seuils sont repris), l'obligation de services payants.

| Fiche | Source |
|---|---|
| `derushage-silences-rates` | `.claude/skills/cut-silences/SKILL.md`, `.claude/skills/cut-mistakes/SKILL.md`, `docs/EDITING-PLAYBOOK.md` |
| `reel-face-cam` | `.claude/skills/short-form-edit/SKILL.md` et ses `references/`, `docs/EDITING-PLAYBOOK.md`, `docs/SHORT-FORM.md` |

## Barty-Bart/motion-graphics

- Dépôt : https://github.com/Barty-Bart/motion-graphics · commit `3d83d987d658601d8a1269eb691622bdcd427335` (13/10/2026)
- **Licence MIT**, © 2026 Bart. Polices Geist : SIL Open Font License. Tracés d'icônes adaptés de Lucide (ISC).
- Aperçus : GIF du dossier `docs/` du dépôt, cités par un lien.
- **Non repris** : le moteur de rendu propre au dépôt (les fiches sont réécrites pour HyperFrames), le code Python de détourage (décrit par étapes). Le modèle de segmentation est téléchargé à l'exécution chez le client, sous sa propre licence.

| Fiche | Source |
|---|---|
| `animations-sur-la-voix` | `skills/motion-broll/SKILL.md`, `skills/motion-broll/reference/engine-api.md` |
| `detourage-sujet` | `skills/object-separation/SKILL.md` |

## heygen-com/hyperframes

- Règles de zone sûre verticale, de sous-titres et de transcription reprises par l'intermédiaire du skill `rendu` (Apache 2.0, voir `licenses/rendu.md`).

## showheyohtaki/motion-prompt

- Numéros de mouvements `#001` à `#192` : dictionnaire du skill `principes-mouvement` (MIT, voir `licenses/principes-mouvement.md`).
