# Crédits du skill `styles-explicatif-infographie`

Les 17 fiches de style et le fichier `references/effets.md` sont des textes écrits en français par Flot Web à partir des sources ci-dessous (traduction, fusion, adaptation au format vertical 1080×1920, au moteur HyperFrames et aux règles de son du plugin). Aucun fichier des dépôts n'est copié tel quel dans le plugin ; les courts extraits de code sont réécrits. Dépôts sous licence MIT : la mention de droit d'auteur et le texte de la licence sont à joindre une fois dans la NOTICE du plugin.

## Sources

| Source | Auteur, licence | Commit lu | Ce qui est repris | Fiches |
|---|---|---|---|---|
| [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | © 2026 LemoLab. Code et textes : MIT. Films de démo et images : CC BY 4.0, **sauf 6 pistes de voix** | `9eb7739a0fca4c6990fe966cb8b87b1930f7193a` | Le contenu de 8 `STYLE.md` de la catégorie « Information & Keynote », plus des valeurs relevées dans les `DEMO.md` et le code des démos | `donnees-crayon` (`dataviz`), `infographie-isometrique` (`iso-infographic`), `keynote-sombre` (`dark-keynote`), `screencast-vivant` (`living-screencast`), `hologramme-hud` (`hologram-hud`), `plan-de-metro` (`transit-map`), `livre-isometrique` (`isometric-picture-book`), `circuit-imprime` (`circuit-board`) |
| [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | © 2026 alchaincyf (花叔 · 花生), MIT, avec exclusions | `1468196505a51728686db118d52561aa27a25124` (version 1.3.0) | Le contenu de 8 cartes de grammaire (`references/动画语法/`), traduites du chinois : quand l'utiliser, composition, couleurs mesurées, trajectoires et durées, transitions, calage sur la voix, erreurs fréquentes, corrections après relecture ; la règle bleu-violet de `references/色板.md` | `maths-animees` (`t1_3b1b`), `keynote-produit` (`t2_keynote_ui`), `graphique-anime` (`t3_finance_chart`), `science-a-plat` (`y1_kurzgesagt`), `collage-enquete` (`y2_vox`), `tableau-blanc-a-la-main` (`y3_whiteboard`), `recit-dessine` (`y4_storytime`), `presentateur` (`y6_presenter_explainer`) |
| [cth9191/animate](https://github.com/cth9191/animate) | © 2026 cth9191, MIT | `7e5eb56feb2dd573f890e1b7b34748af43d58263` (version 0.4.0) | Style `math` (`plugins/animate/skills/animate/styles/math/STYLE.md`, `kit.js`) : couleurs et leur sens, conventions de composition des formules, tailles en 1080×1920, zone sûre, durées, liste de contrôle | `maths-animees` |
| [charlie947/motion-graphics-skills](https://github.com/charlie947/motion-graphics-skills) | © 2026 Charlie Hills, MIT | `229022ebca76972e119e36ada23a1648d51665ab` | Skills `vox-explainer`, `apple-launch-film`, `animated-chart`, `milestone-reveal` (questions à poser, règles de relecture, minutage, pièges) ; skill `motion-effects` et son fichier `references/effects.md` (les 16 recettes, traduites en entier) | `collage-enquete`, `keynote-produit`, `graphique-anime`, `nombre-jalon`, `references/effets.md` |
| manim (constantes de couleur, courbe « lisse ») | 3Blue1Brown, LLC et la communauté manim, MIT | cité d'après les deux cartes ci-dessus | Codes de couleur et formule `6t⁵ − 15t⁴ + 10t³` | `maths-animees` |
| [showheyohtaki/motion-prompt](https://github.com/showheyohtaki/motion-prompt) | © 2026 Shohei Ohtaki, MIT | `7819d38` | Seulement les **numéros** des mouvements cités ; le dictionnaire est dans `principes-mouvement` | toutes |

## Fiches fusionnées (une seule fiche par style)

| Fiche | Sources fusionnées | Règle en cas de désaccord |
|---|---|---|
| `maths-animees` | huashu `t1_3b1b` + animate `math` | Grammaire et rythme : huashu. Typographie, tailles verticales, liste de contrôle : animate. Jaune : celui d'animate (`#F7D96F`), le jaune pur réservé aux éclairs |
| `keynote-produit` | huashu `t2_keynote_ui` + charlie `apple-launch-film` | Le produit réel en grand (huashu) prime ; la « pastille qui grandit en widgets » (charlie) est une variante, redessinée en interface générique |
| `graphique-anime` | huashu `t3_finance_chart` + charlie `animated-chart` | Mise en page et calage sur la voix : huashu. Mode boucle et valeurs intouchables : charlie. Couleurs de hausse et de baisse : convention française (la carte chinoise utilise l'inverse) |
| `collage-enquete` | huashu `y2_vox` + charlie `vox-explainer` | Les mesures de huashu priment (grain de papier fixe, photos présentes dès la coupe, pas de déchirure de papier). Types de plans, faits sourcés et relecture : charlie |

Styles de la même famille dont la fiche unique est ailleurs : la typo cinétique (huashu `y5_kinetic_type`) est dans `styles-graphique-typo` ; l'isométrique au trait fin (animate `isometric`) est dans `styles-matieres-3d`.

## Aperçus (liens seulement, rien n'est copié dans le plugin)

| Fiches | Aperçu | Crédit à afficher | Restrictions |
|---|---|---|---|
| `donnees-crayon`, `infographie-isometrique`, `keynote-sombre`, `hologramme-hud`, `plan-de-metro` | `https://lemomo-ai.github.io/lemo-opuscar/films/<slug>.mp4` et `…/posters/<slug>.jpg` | « LemoLab, https://github.com/lemomo-ai/lemo-opuscar, CC BY 4.0 » ; dire si l'image a été modifiée | Les données montrées (`dataviz`, `transit-map`) gardent leurs propres sources : voir le fichier `CREDITS` de chaque démo |
| `livre-isometrique`, `circuit-imprime` | idem | idem | **Voix exclue de la licence CC BY 4.0** (voix d'un service en ligne) : lien seulement, ou image sans le son. Ne jamais réutiliser ces voix |
| `screencast-vivant` | idem | idem | **Film de fan** : mascotte et interface d'une marque tierce, non affiliée. Lien seulement, jamais comme visuel de vente ; ni la mascotte ni l'interface ne sont reprises |
| 7 fiches huashu avec démo | Planches `assets/动画语法/<id>_总览.jpg` | « 花叔 Huashu (alchaincyf), https://github.com/alchaincyf/huashu-art-motion » | Quatre démos (`y1`, `y2`, `y3`, `y4`) montrent le personnage de l'auteur, **exclu de la licence MIT** : lien seulement |
| `presentateur` | aucun (la source n'a pas de démo) | | Aperçu maison à produire |
| `maths-animees` | en plus : `plugins/animate/skills/animate/styles/math/sample.png` | « cth9191, https://github.com/cth9191/animate » | MIT |
| `nombre-jalon`, `keynote-produit`, `references/effets.md` | `assets/readme/demo-milestone.gif`, `assets/readme/demo-launch.gif` | « Charlie Hills, https://github.com/charlie947/motion-graphics-skills » | MIT |

## Ce qui n'est pas repris

- **Histoires, plans et personnages des démos**, y compris la mascotte tierce de `living-screencast` et le personnage de l'auteur de huashu.
- **La mascotte en forme de lettre pi** du style `math` d'animate (signature de la chaîne dont le style s'inspire) : la fiche demande un personnage original.
- **Le code de référence de la grammaire « présentateur »** (`scripts/engine/reference_films/spacex/`) : dossier au nom d'une marque tierce, contenant des données de tracé sous une autre licence.
- **Les éléments d'un système d'exploitation réel** du skill `apple-launch-film` (barre de menus, encoche, mot d'accueil manuscrit) : remplacés par une barre et une pastille génériques.
- **Les règles bilingues chinois-anglais** de trois fiches lemo (`transit-map`, `isometric-picture-book`, `circuit-board`) et le tracé manuel des caractères chinois : remplacés par une seule langue, avec les accents du français.
- **Le fond violet en dégradé** relevé sur les originaux par la carte `y1_kurzgesagt` : la carte elle-même le déconseille ; la fiche donne un fond sombre uni.
- **Les marques citées comme inspiration** (3Blue1Brown, Vox, Kurzgesagt, Apple) : aucun logo, personnage, police maison ni couleur de marque n'est repris. Les mentions « style … » désignent une inspiration, jamais un contenu officiel ni une affiliation.

## Polices citées (nommées, non distribuées)

Caveat, Newsreader, IBM Plex Mono, Jost, Inter, Inter Tight, JetBrains Mono, Rajdhani, Share Tech Mono, Major Mono Display, Roboto Condensed, Noto Sans, Latin Modern Roman, CMU Serif, STIX Two Text, Patrick Hand, Architects Daughter, Kalam, Oswald, Bebas Neue, Anton, Libre Baskerville, Playfair Display, Special Elite, Courier Prime, Nunito, Poppins, Baloo 2, Archivo, Anybody : publiées sous SIL Open Font License 1.1 (Roboto Condensed : Apache 2.0 ou OFL selon la version ; Latin Modern : GUST Font License). À revérifier police par police au moment de les embarquer dans un projet.

## Ajouts de Flot Web (à ne pas attribuer aux sources)

- Toutes les sections « Composition 9:16 », les tailles en pixels pour 1080×1920, les limites de zone utile, les nombres de colonnes, de barres et de points recalculés.
- Les numéros de mouvements autorisés et interdits.
- Les sections « Son » des fiches huashu et charlie quand la source n'en a pas ou presque (`maths-animees`, `keynote-produit`, `graphique-anime`, `nombre-jalon`, `science-a-plat`, `presentateur`), et l'adaptation au budget de bruitages du plugin partout.
- Des codes de couleur donnés **en exemple** quand la source ne donne qu'une règle : `donnees-crayon` (papier, encre, mines), `keynote-sombre` (les neutres), `screencast-vivant` (toute la table), `hologramme-hud` (les codes des trois couples), `nombre-jalon` (toute la table), `science-a-plat` (fond et second plan), `presentateur` (toute la table). Chaque fiche le signale.
- Pour `presentateur` : la composition, la palette, la recette et le son sont en grande partie de Flot Web, la carte d'origine tenant en une page.
- Les tempos conseillés à 30 images par seconde (les sources travaillent à 24 ou 60).
