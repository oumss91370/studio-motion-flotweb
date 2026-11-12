# Styles partagés entre catégories

Règle : **une seule fiche `STYLE.md` par style dans tout le plugin.** La fiche est rangée dans une catégorie (celle qui la « porte ») ; les autres catégories qui s'en servent y renvoient par une ligne « Voir aussi (fiches portées par une autre catégorie) » dans leur `SKILL.md`, sans recopier la fiche.

Ce tableau sert au serveur pour attacher un style à plusieurs catégories : un client qui a droit à l'une des catégories de la colonne de droite doit pouvoir recevoir la fiche, même s'il n'a pas la catégorie qui la porte.

Chemin d'une fiche : `skills/<catégorie qui porte>/styles/<identifiant>/STYLE.md`.

## Styles partagés

| Style (identifiant) | Catégorie qui porte la fiche | Catégories qui y renvoient | Remarque |
|---|---|---|---|
| `typo-cinetique` | `styles-graphique-typo` | `styles-explicatif-infographie`, `styles-lancement-produit`, `styles-montage-documentaire` | |
| `isometrique-trait-fin` | `styles-matieres-3d` | `styles-explicatif-infographie`, `styles-lancement-produit` | moteur HyperFrames 2D, bien que rangé en « Matières et 3D » |
| `tableau-blanc` | `styles-peinture-dessin` | `styles-explicatif-infographie`, `styles-montage-documentaire` | tableau **sans main**, feutres de couleur (source lemo-opuscar) |
| `tableau-blanc-a-la-main` | `styles-explicatif-infographie` | `styles-peinture-dessin`, `styles-montage-documentaire` | tableau **avec une main** qui dessine (source huashu) ; style distinct du précédent, deux fiches voulues |
| `keynote-sombre` | `styles-explicatif-infographie` | `styles-lancement-produit`, `styles-graphique-typo` | interface entièrement dessinée, sans capture |
| `keynote-produit` | `styles-explicatif-infographie` | `styles-lancement-produit`, `styles-graphique-typo` | vraies captures du produit ; style distinct du précédent, deux fiches voulues |
| `screencast-vivant` | `styles-explicatif-infographie` | `styles-lancement-produit` | |
| `collage-enquete` | `styles-explicatif-infographie` | `styles-montage-documentaire` | |
| `diorama-pixel` | `styles-jeu-retro` | `styles-2-5d`, `styles-matieres-3d` | pour un récit à personnages plats : parcours `styles-2-5d/references/pipeline.md` |
| `livre-pop-up` | `styles-matieres-3d` | `styles-2-5d`, `styles-papier-impression` | fiche fusionnée (film `paper-popup` + look n° 67 d'OPUSCAR 98) ; encadré « Variante histoire vraie » (vaut pour tout récit à personnages plats) |
| `theatre-de-papier` | `styles-2-5d` | `styles-matieres-3d`, `styles-papier-impression` | |
| `lavis-encre` | `styles-encre-asie` | `styles-peinture-dessin` | fiche fusionnée (lemo-opuscar + huashu) |
| `art-nouveau` | `styles-graphique-typo` | `styles-papier-impression`, `styles-peinture-dessin` | affiche |
| `constructivisme` | `styles-graphique-typo` | `styles-papier-impression`, `styles-peinture-dessin`, `styles-montage-documentaire` | affiche dessinée ; ne pas confondre avec `montage-constructiviste` (vraies images) |
| `bauhaus` | `styles-graphique-typo` | `styles-papier-impression`, `styles-peinture-dessin` | affiche |
| `cubisme`, `art-deco` | `styles-graphique-typo` | `styles-peinture-dessin` | |
| `papier-decoupe-rouge`, `lanterne-papier` | `styles-encre-asie` | `styles-papier-impression` | |
| `papier-decoupe-satirique`, `comics-cosmique` | `styles-cartoon` | `styles-papier-impression` | `comics-cosmique` est aussi cité par `styles-jeu-retro` (dérogation bleu-violet) |
| `anime-cellulo-80` | `styles-cartoon` | `styles-jeu-retro` | cité pour la dérogation bleu-violet |
| `montage-constructiviste` | `styles-montage-documentaire` | `styles-graphique-typo` | |
| `verre-produit` | `styles-matieres-3d` | `styles-lancement-produit` | |
| `vue-eclatee`, `donnees-en-objets` | `styles-montage-documentaire` | `styles-matieres-3d` | |
| `lecon-pixel-art`, `science-pixel-art` | `formats-flotweb` | `styles-jeu-retro` | formats complets, pas seulement un look |

## Renvois depuis la bibliothèque de looks

`styles-cinema/references/98-looks.md` renvoie, pour cinq looks, à la fiche complète du même style : `tuyau-caoutchouc-1930`, `cartoon-annees-50`, `comics-cosmique` (`styles-cartoon`), `livre-pop-up`, `mosaique` (`styles-matieres-3d`).

## Paires à ne pas fusionner

Ces fiches se ressemblent par le nom mais décrivent des styles différents ; chacune renvoie à l'autre :

- `tableau-blanc` (sans main) / `tableau-blanc-a-la-main` (avec main) / `tableau-de-briefing` (vrai tableau filmé, `styles-montage-documentaire`) / `tableau-noir-craie` ;
- `keynote-sombre` (interface dessinée) / `keynote-produit` (vraies captures) ;
- `constructivisme` (affiche dessinée) / `montage-constructiviste` (montage de vraies images) ;
- `infographie-isometrique`, `livre-isometrique` (`styles-explicatif-infographie`) / `isometrique-trait-fin` (`styles-matieres-3d`) ;
- `papier-decoupe-collage`, `papiers-decoupes-matisse` (`styles-papier-impression`) / `papier-decoupe-rouge` (`styles-encre-asie`) / `papier-decoupe-satirique` (`styles-cartoon`).

## Tenir ce tableau à jour

Quand une fiche est ajoutée, déplacée ou supprimée : mettre à jour le tableau des styles du `SKILL.md` de la catégorie qui la porte, la ligne « Voir aussi » des catégories qui y renvoient, et ce fichier. Aucun identifiant de style ne doit exister dans deux dossiers `styles/`.
