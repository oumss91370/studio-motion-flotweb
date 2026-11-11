# Crédits du skill `styles-graphique-typo`

Les 15 fiches de style sont des textes écrits en français par Flot Web à partir des sources ci-dessous (traduction, adaptation au format vertical 1080×1920, au moteur HyperFrames et aux règles de son du plugin). Aucun fichier des dépôts n'est copié tel quel dans le plugin ; les courts extraits de code des fiches sont réécrits. Dépôts sous licence MIT : la mention de droit d'auteur et le texte de la licence sont à joindre une fois dans la NOTICE du plugin.

## Sources

| Source | Auteur, licence | Commit lu | Ce qui est repris | Fiches |
|---|---|---|---|---|
| [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | © 2026 LemoLab. Code et textes : MIT. Films de démo et images : CC BY 4.0 | `9eb7739a0fca4c6990fe966cb8b87b1930f7193a` | Le contenu de 7 `STYLE.md` de la catégorie « Graphic & Type » (essence, matières, logique des couleurs, typographie, qualité du mouvement, grammaire de caméra, palette sonore, gestes natifs, pièges, description du moteur), plus des valeurs relevées dans les `DEMO.md` et le code des démos (`styles/<slug>/demo/`) | `typo-suisse` (`swiss-motion`), `generique-espion-60` (`spy-titles`), `art-deco` (`art-deco`), `plan-bleu` (`blueprint`), `vitrail` (`stained-glass`), `pictogrammes` (`pictogram-motion`), `terminal-ascii` (`ascii-crt`) |
| [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | © 2026 alchaincyf (花叔 · 花生), MIT, avec exclusions (voir plus bas) | `1468196505a51728686db118d52561aa27a25124` (version 1.3.0) | Le contenu de 7 cartes de style (`references/风格配方/`) et d'une carte de grammaire (`references/动画语法/y5_kinetic_type.md`), traduites du chinois : procédé de rendu, couleurs, façon dont les motifs bougent, transition signature, pièges ; lecture du code `scripts/engine/scenes/<id>.js` et `scripts/engine/demos/y5_kinetic_type/` | `bauhaus` (`12_bauhaus`), `constructivisme` (`22_constructivism`), `cubisme` (`11_cubism`), `illustration-plate` (`16_2026`), `art-nouveau` (`10_nouveau`), `bonshommes-trait-epais` (`31_haring`), `pois-infinis` (`21_kusama`), `typo-cinetique` (`y5_kinetic_type`) |
| [showheyohtaki/motion-prompt](https://github.com/showheyohtaki/motion-prompt) | © 2026 Shohei Ohtaki, MIT | `7819d38` | Seulement les **numéros** des mouvements (`#001` à `#192`) cités dans les sections « Ce qui bouge » ; le dictionnaire lui-même est dans le skill `principes-mouvement` | toutes |

## Aperçus (liens seulement, rien n'est copié dans le plugin)

| Fiches | Aperçu | Crédit à afficher | Licence de l'aperçu |
|---|---|---|---|
| 7 fiches lemo | Film : `https://lemomo-ai.github.io/lemo-opuscar/films/<slug>.mp4` ; 1080p : `https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/<slug>.mp4` ; affiche : `https://lemomo-ai.github.io/lemo-opuscar/posters/<slug>.jpg` | « LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0 » ; dire si l'image a été modifiée | CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Les 7 voix de ces démos sont des voix Kokoro (Apache 2.0) : aucune n'est dans la liste des 6 voix exclues |
| 7 fiches huashu (styles) | Planche commune `assets/全风格总览.jpg` ; film complet sur la page des versions du dépôt | « 花叔 Huashu (alchaincyf), https://github.com/alchaincyf/huashu-art-motion » | MIT. **Lien seulement, pas de visuel de vente** : la composition de la planche (une jeune fille, un chat, une table) s'inspire d'un film tiers, et elle contient des motifs proches d'artistes protégés |
| `typo-cinetique` | Planche `assets/动画语法/y5_kinetic_type_总览.jpg` | idem | MIT |

## Ce qui n'est pas repris

- **Scènes et personnages des démos** : aucune histoire, aucun plan, aucun personnage des films de démonstration (ni ceux de lemo, ni la scène « jeune fille et chat » de huashu, ni le personnage de l'auteur de huashu, exclu de sa licence MIT).
- **Lettrage cyrillique et mots d'ordre** de la carte constructiviste : remplacés par un lettrage latin en blocs.
- **Motifs propres à des artistes** : la fiche `bonshommes-trait-epais` ne reprend aucun personnage ni symbole de Keith Haring (droits gérés par sa fondation) ; la fiche `pois-infinis` ne reprend aucune œuvre de Yayoi Kusama (artiste vivante). Les mentions « style Haring » et « style Kusama » désignent une inspiration, jamais une œuvre officielle ni une affiliation ; les fiches demandent de ne pas nommer ces artistes dans les vidéos.
- **Polices propriétaires** : aucune. Les fiches nomment seulement des polices libres.

## Polices citées (nommées, non distribuées)

Archivo, Inter, Inter Tight, Schibsted Grotesk, Instrument Sans, League Gothic, League Spartan, Limelight, Poiret One, Josefin Sans, Italiana, Architects Daughter, B612, Allura, IM Fell English, Cinzel, DM Mono, VT323, Poppins, Anton, Bebas Neue, Alfa Slab One, Libre Baskerville, Caveat, Nunito, Marcellus, Fredoka, Baloo 2, Noto Sans, JetBrains Mono : publiées sous SIL Open Font License 1.1 (à revérifier police par police au moment de les embarquer dans un projet).

## Ajouts de Flot Web (à ne pas attribuer aux sources)

- Toutes les sections « Composition 9:16 » (les sources sont en 16:9), les tailles en pixels pour 1080×1920, les limites de zone utile.
- Les numéros de mouvements autorisés et interdits.
- Les sections « Son » des 7 fiches huashu (les cartes d'origine n'en ont pas) et l'adaptation au budget de bruitages du plugin pour les fiches lemo.
- Des codes de couleur donnés **en exemple** quand la source ne donne qu'une règle : `vitrail` (toute la table), `pictogrammes` (la teinte « tomate »), `terminal-ascii` (les trois phosphores), `illustration-plate` (tout sauf `#f08b7d` et `#f3ad4c`), `bonshommes-trait-epais` (rouge, bleu, rose), `pois-infinis` (toute la table). Chaque fiche le signale.
- Les durées allongées de `art-nouveau` (la démo d'origine dure 0,7 s par style).
