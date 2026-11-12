# Crédits de la catégorie `styles-2-5d`

| Source | Auteur | Dépôt | Commit | Licence | Ce qui est repris |
|---|---|---|---|---|---|
| Cours « How to build a 2.5D motion studio with Opus 5.5 (Full Course) » | article public, auteur non indiqué dans la copie analysée | — | — | — | Anatomie du format, les cinq raisons pour lesquelles il fonctionne, parcours de production (5 histoires sourcées, texte de 150 à 170 mots, `sources.md`, un plan par idée, 3 à 5 décors, temps clés en numéros d'image, voix et temps mot à mot, sous-titres de 1 à 2 mots, planche contact et test téléphone, 3 corrections par tour, correction en 4 champs), règles vis-à-vis des plateformes. Idées et méthode reformulées en français et adaptées (HyperFrames à la place de Remotion, −14 LUFS) ; les exemples chiffrés du cours sont signalés comme valeurs de départ. Aucune vidéo, aucun personnage ni aucun texte de la chaîne étudiée par le cours n'est repris. |
| lemo-opuscar, « OPUSCAR 98 » | LemoLab | https://github.com/lemomo-ai/lemo-opuscar | `9eb7739` | MIT (prompts et documents), CC BY 4.0 (film et images) | Deux prompts de style 2.5D de `styleboard/opuscar98_styles.json` : entrée n° 41 (théâtre-jouet en carton) pour `theatre-de-papier`, entrée n° 67 (livre pop-up filmé sur un bureau) pour `livre-pop-up`, dont la fiche unique est désormais dans `styles-matieres-3d` (voir `licenses/styles-matieres-3d.md`) : couleurs, épaisseurs, lumière, caméra, liste « à éviter ». Titres d'œuvres, personnages et mascotte retirés. Le film n'est cité qu'en lien (les fiches de `styles-cinema`, tirées du même fichier, ne le lient pas : voir `licenses/styles-cinema.md`). © 2026 LemoLab. |
| MCP for Blender | Siddharth Ahuja | https://github.com/ahujasid/mcp-for-blender | `2e4b0bc` | MIT | Outils utilisés par les recettes (voir `licenses/blender.md`). |
| ClaudeAnimationBase | John Heibel | https://github.com/JohnHeibel/ClaudeAnimationBase | `0ac8bf2` | MIT | Jeu d'acteur (voir `licenses/personnages.md`). |
| motion-prompt | showheyohtaki | https://github.com/showheyohtaki/motion-prompt | `7819d38` | MIT | Numéros de mouvements cités dans les fiches (010, 011, 012, 016, 021, 023, 024, 027, 029, 030, 031, 032, 033, 034, 036, 043, 187). |
| Whisper | OpenAI | https://github.com/openai/whisper | — | MIT | Commande d'horodatage mot à mot citée dans le parcours. |

## Origine du style `tete-ronde-trait-plein-delie` et du prompt maître

- **Travail du studio (Flot Web).** Les règles chiffrées de `references/prompt-maitre.md` et de la fiche `tete-ronde-trait-plein-delie` viennent de mesures faites par le studio, les 11 et 12/11/2026, sur une vidéo de référence étudiée en interne : lecture continue image par image (durées, caméra, montage, sous-titres, son), mesure au pixel du rendu des personnages (contour, ombrage, membres, visage, ombre au sol), puis du décor (parallaxe, matières, contours, ombres, palettes, optique, densité).
- **Méthode de mesure** : celle du skill `reproduire-reel`, avec ses scripts (voir `licenses/reproduire-reel.md`). Elle sort des lois (une épaisseur de trait en fonction de la lumière, un mélange de couleurs, une règle de flou, des durées en images), exprimées en fraction du diamètre de la tête.
- **Aucun élément d'œuvre tierce.** La vidéo étudiée n'est ni reprise, ni montrée, ni liée, ni nommée dans le plugin. Aucun de ses personnages, costumes, accessoires, décors, textes, sons ni sujets ne figure dans le prompt maître, les fiches, le kit ou ses exemples. Les couleurs citées sont des relevés de lumière et d'encre (peau, trait, ombre, ciel), donnés comme points de départ que la palette du client remplace. Les irrégularités propres à un dessin ne sont pas recopiées : seules les lois le sont.
- **Essais du studio** : des plans de test fabriqués en interne ont servi au contrôle chiffré et aux critiques indépendantes. Ces plans, leur sujet, leurs personnages et leurs décors sont un essai interne, non publié et non distribué ; rien n'en est repris dans le plugin.

## Origine du kit (`skills/styles-2-5d/kit/`)

Le kit contient deux chaînes, toutes deux écrites par le studio (Flot Web).

**Chaîne mesurée** (`regles.py`, `pantin.py`, `film.py`, `bl_decor.py`, `bl_scene.py`, `compo.py`, `lancer.py`, `controle.py`), écrite le 12/11/2026 :

- version générique des outils des plans de test du studio : générateur de personnages paramétré, bibliothèque de décor peint en trois passes, assemblage, contrôle ;
- **le générateur ne contient aucun personnage** : il dessine ceux que le client décrit. Aucun personnage de la vidéo étudiée ni des plans de test n'y figure ;
- **son exemple est neutre et original** (une gardienne de phare attend une lettre, le facteur arrive : deux plans, deux personnages, un intérieur, un extérieur), dessiné et écrit par le studio pour le kit, fait pour être remplacé ;
- le contrôle s'appuie sur les scripts du skill `reproduire-reel` ;
- aucun code tiers, aucun média tiers. Outils installés à part, non redistribués : Blender (GPL, Blender Foundation), Pillow (MIT-CMU), NumPy (BSD), OpenCV (Apache 2.0), resvg et son module Python `resvg_py` (rendu des dessins vectoriels ; licence à vérifier à l'installation), FFmpeg (LGPL ou GPL selon la compilation).

**Chaîne à plans émissifs** (`plans.py`, `personnages.py`, `bl_lib.py`, `bl_film.py`, `bl_cli.py`, `bl_plage.py`, `rendre.py`, `refaire.py`, `suivi.py`) et outils communs (`reglages.py`, `mix.py`, `ecart_voix.py`, `hf_build.py`, `revue.py`, `planche.py`) :

- **Créés par le studio (Flot Web)** lors de son prototype 2.5D du 11/11/2026 : un film de 61,5 s (36 plans, 1 845 images) produit de bout en bout avec Blender 5.3, le connecteur MCP for Blender et HyperFrames. Les outils de ce film ont été réécrits en version générique, en Python, pour Windows, macOS et Linux.
- **Le prototype lui-même est un test interne, non publié, et il n'est pas distribué** : ni le film, ni son script, ni ses sources, ni ses personnages, ni son objet héros, ni ses décors, ni sa voix, ni ses sons ne figurent dans le plugin. Il suivait de près le sujet et la grammaire d'une chaîne existante, par choix pour un essai interne ; rien de ce contenu n'a été repris dans le kit.
- **Ce que cette chaîne contient en propre** : la mécanique, et un exemple neutre original de 2 plans (un atelier, une sonnette, un personnage d'exemple nommé « Galet »), dessiné et écrit par le studio pour le kit. Cet exemple ne reprend le dessin d'aucune chaîne ni d'aucun personnage tiers ; il est fait pour être remplacé par le personnage du client.
- **Aucun code tiers.** Outils installés à part, non redistribués : Blender, le module Python `bpy`, Pillow, NumPy, FFmpeg, HyperFrames (Apache 2.0, HeyGen ; voir `NOTICE`).
- **Aucun média tiers** : ni son, ni voix, ni texture, ni police. Les fichiers de `kit/exemple/voix/` sont un horodatage d'exemple écrit à la main.
- **Règles marquées « rendu réel du 11/11/2026 »** dans `references/pipeline.md` (bande des sous-titres de cette chaîne, sujet dans les 65 % du haut, budget de bruitages d'un récit narré, instruments virtuels, objet héros sans double, contrôle de la voix de synthèse, vérification fait par fait, questions de critique, temps mesurés) : constats du studio sur ce prototype. Les 9 questions de critique sont une formulation du studio, tirée des neuf corrections consignées dans la revue du prototype.
- **Essai de cette chaîne** : l'exemple a été construit et rendu le 11/11/2026 avec le module `bpy` 5.3.0 sur une machine Linux sans carte graphique (Cycles sur processeur, taille réduite), puis assemblé avec HyperFrames 0.9.33. Ce qui a tourné et ce qui n'a pas été essayé est dit dans `references/pipeline.md`.

Aperçus :

- `theatre-de-papier` et `livre-pop-up` : extraits du film collectif de LemoLab (CC BY 4.0), **en lien seulement** ; ne pas les afficher sur une page de vente (mascotte tierce, œuvres adaptées).
- `tete-ronde-trait-plein-delie` : aucun aperçu tiers. L'aperçu est le film d'essai du kit, sur un sujet neutre et original, produit par le studio. Ni la vidéo étudiée ni les plans de test internes ne sont des aperçus : ils ne sont ni publiés ni distribués.

Crédit à afficher si un extrait LemoLab est montré : « LemoLab, CC BY 4.0, github.com/lemomo-ai/lemo-opuscar », en indiquant toute modification.
