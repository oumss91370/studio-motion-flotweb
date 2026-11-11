# Dérogation à l'interdit bleu-violet

## La règle générale

La porte de livraison du studio (skill `studio-coeur`) refuse les films dominés par le bleu-violet : fonds en dégradé bleu-violet, ciels étoilés violets, lueurs néon cyan-violet, verre dépoli violet. Ce sont les couleurs par défaut d'une animation faite par une IA ; le public les lit ainsi au premier regard.

Mesure (reprise de huashu-art-motion ; fichiers d'origine cités en bas de page) :

- un pixel est « bleu-violet » si sa teinte est entre **225° et 300°** et sa saturation ≥ **0,30** ;
- une image est « bleu-violet » si **30 %** ou plus de ses pixels le sont ;
- un film est **rouge** (non livré) si 30 % ou plus de ses images le sont, **jaune** à partir de 12 %.

Le bleu marine en aplat (teinte ≈ 210°) n'est pas concerné : c'est un fond voulu, ni dégradé ni lumineux.

## Quand la dérogation est permise

Seulement quand **le bleu-violet est le sujet même du style**, et que le client a choisi ce style en le voyant. Dans ce plugin :

| Style | Catégorie | Pourquoi |
|---|---|---|
| `neon-vaporwave` | Jeu vidéo et rétro | Le violet profond, le magenta et le cyan sont la palette du genre |
| `cgi-annees-80` | Jeu vidéo et rétro | Ciel rose-violet et anneau violet des premières images de synthèse (part souvent sous le seuil : mesurer avant de demander) |
| `anime-cellulo-80` (scènes de nuit) | Cartoon | Indigo et violet des nuits de ville peintes |
| `comics-cosmique` (plans d'espace) | Cartoon | Seulement si les plans de cosmos dominent le film |
| `tourbillons-van-gogh` | Peinture et dessin | Nuit étoilée peinte : le ciel bleu-violet est le sujet. D'abord essayer la surface chaude demandée par la fiche |
| `nympheas` | Peinture et dessin | L'eau tire vers le bleu-violet. D'abord équilibrer par les verts, les roses et une rive chaude |
| `ile-low-poly` (nuit, crépuscule) | Matières et 3D | Seulement si la nuit dépasse 30 % du film ; sinon la garder courte |
| Looks 89 et 97 de `styles-cinema/references/98-looks.md` | Cinéma | Looks marqués « Sous dérogation bleu-violet » (clair de lune peint, nuit de néon) |

Les quatre premières lignes sont des styles dont la palette est bleu-violet par nature. Les suivantes sont des styles où la dérogation est un **dernier recours** : la fiche demande d'abord de rester sous le seuil.

Elle n'est **jamais** permise pour « faire moderne », pour un fond d'explication, pour un style qui ne figure pas dans ce tableau, ni parce que le premier rendu est sorti violet.

## Les quatre conditions

1. **Choix explicite** : le client a validé une image de style qui montre cette palette. On garde la trace de cette validation.
2. **Le style entier, pas seulement la couleur** : la dérogation couvre un film qui respecte la fiche (tubes néon dessinés, grille, lecture VHS, trames…). Un dégradé violet nu avec un texte blanc reste refusé, même sous ce nom.
3. **Contrepoids chauds obligatoires** : au moins une couleur chaude saturée présente dans chaque plan (jaune soleil, orange, rose chaud, or), et le texte important en blanc cassé ou en jaune, jamais en violet sur violet.
4. **Raison écrite** dans la note de livraison, dans la partie « faits », sous cette forme :

   > Dérogation bleu-violet : style `neon-vaporwave`, choisi par le client sur l'image de style du [date]. Part d'images bleu-violet mesurée : NN %.

   La porte de livraison passe alors du rouge au **jaune** (jamais au vert) : le film est livré avec la mention.

### Les deux gestes à faire dans `studio-coeur`

- **Au storyboard**, ajouter au verrou la ligne `Bleu-violet autorisé : <raison>` (voir `studio-coeur/references/look-et-storyboard.md`). Sans elle, le contrôle du storyboard refuse la palette.
- **À la livraison**, lancer la porte avec `--autoriser-bleu-violet "<raison>"` (voir `studio-coeur/references/controles.md`). La raison est recopiée dans la note de livraison.

Seuils et définition du pixel bleu-violet : ce sont ceux de `studio-coeur` (`scripts/porte_livraison.py`, `scripts/lint_storyboard.py`) et de `marque` (`scripts/verifier_fiche.py`) ; s'ils changent, ils changent là-bas d'abord.

`studio-coeur` précise que cette option ne s'utilise **jamais de la propre initiative de l'agent**. Choisir un style de ce tableau en ayant vu son image de style **est** la demande du client : c'est pourquoi la condition 1 est obligatoire et doit laisser une trace.

## Ce que la dérogation ne lève pas

- Les autres contrôles restent entiers : anti-diaporama, écrans vides, lisibilité, zones sûres, loudness.
- La lisibilité : contraste du texte ≥ 4,5:1 sur son fond réel ; un texte cyan sur violet échoue presque toujours.
- Le mélange de styles : un seul plan vaporwave dans un film d'un autre style n'ouvre pas droit à la dérogation ; on redessine ce plan dans la palette du film.

## Vérifier soi-même avant la porte

Extraire une image par seconde, les mettre en rang, et regarder : y a-t-il une couleur chaude dans chaque image ? Le texte se lit-il à taille de téléphone ? Si la réponse est non pour une image, la corriger avant de demander la dérogation.

## Origine

Règle et seuils : alchaincyf/huashu-art-motion, commit `1468196`, `scripts/film_gate.py`, `references/色板.md` (licence MIT, © 花叔 Huashu). Conditions 1 à 3 et tableau des styles : ajoutés par Flot Web.
