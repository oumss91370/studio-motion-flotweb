# Le look et le storyboard

## Le style est figé, l'histoire est libre

La fiche `STYLE.md` d'un style fixe son identité, sa palette et sa typo, sa composition 9:16, ce qui bouge, son rythme, sa recette technique, son son et ses erreurs fréquentes. **Tu gardes tout.**

Tout le reste t'appartient et vient du sujet du client : l'histoire, la structure, les personnages, les décors, les plans, les durées, la façon de montrer un chiffre.

Ordre de lecture :
1. la fiche `STYLE.md` : dès le choix du style ;
2. ton histoire : écrite sans avoir vu la démo ;
3. la démo du style : seulement après, pour apprendre une technique (un pinceau, un rig, un mélange), jamais pour son histoire, ses plans, ses accessoires ou ses durées.

Ce que le client peut changer dans un style sans le casser : les couleurs dans la logique de la palette, la police, le tempo, la densité du son, un geste propre au style (un seul). Ce qui change son caractère : la matière, la logique de couleur, la grammaire de caméra (dis-lui ce qu'il perd). Ce qui en fait un autre style : son essence. Propose alors un style plus proche.

## Écart avec la démo : au moins 4 sur 6

Une fois l'histoire validée, ouvre la démo du style et compare six points :

| Point | Question |
|---|---|
| Structure | même forme de récit ? |
| Ouverture | même première image, même type d'accroche ? |
| Plan signature | même plan dont on se souvient ? |
| Trajet de caméra | mêmes mouvements dans le même ordre ? |
| Forme de la musique | même courbe (montée, silence, impact) ? |
| Fin | même dernière image, même type de chute ? |

**Au moins quatre doivent différer.** Repense ceux qui se ressemblent. Le tableau se remplit dans `storyboard.md` et le lint le compte. Avant de livrer, pose ta planche contact à côté de l'aperçu de la démo : dernière vérification.

Un style sans démo (style créé pour le client) : lance le lint avec `--sans-demo`.

## Les 3 ou 4 images de l'histoire (validation n° 2, en boucle)

- **3 ou 4 images de l'histoire du client**, rendues avec le vrai code de dessin, à la taille finale (1080×1920). Pas de maquette : ce code deviendra la vidéo.
- Les moments qui comptent : **l'accroche, le rebondissement, la chute**, et le plan signature du style s'il n'est pas déjà dedans. Varie les échelles : un plan large, un plan moyen, un très gros plan.
- Le client doit y reconnaître **son** histoire : ses personnages, son lieu, son objet, pas une scène d'exemple.
- Avec des personnages : ajoute une planche du personnage (face, profil, 3 expressions, 2 poses) avec le skill `personnages`.
- Avec les captures ou le produit du client : ils sont dans l'image, encadrés à la manière du style.

Vérifie chaque image avant de la montrer :

1. Une chose constante que l'œil tient (le héros, un décor, un objet).
2. Une couleur réservée à ce que l'histoire suit, jamais dépensée en décoration.
3. La matière du style se voit à la taille d'un téléphone. Une image qui pourrait être de n'importe quel style est du clipart.
4. L'idée est jouée, pas étiquetée.
5. Il se passe quelque chose : l'image est un instant d'un changement.
6. Le texte vit dans le monde (une affiche, une étiquette, un écran) ou est composé dans la typo du style. Un seul texte court, 50 px de haut au moins.
7. Les échelles varient d'une image à l'autre.
8. Zone sûre : rien d'important dans les 160 px du haut, les 360 px du bas, les 135 px de droite.
9. La liste de contrôle propre au style (section 8 de sa fiche).
10. Regardée à 360 px de large : on comprend encore.

Montre les images côte à côte, numérotées. Demande **une critique par image** (« garde », « change ceci », « refais ») et un avis d'ensemble (personnages, couleurs, ambiance). Puis :

1. Refais seulement ce qui est critiqué ; ne touche pas à ce qui est gardé.
2. Remontre les images, anciennes et nouvelles côte à côte pour celles qui ont changé.
3. Recommence tant que le client n'a pas dit que ça lui va. Note chaque critique dans `brief.md` : elles valent pour toute la vidéo.
4. Après trois tours sans accord, arrête de retoucher : le problème est le style, pas l'image. Demande ce qui cloche, propose un autre style ou demande une référence.

Aucune animation, aucun rendu de vidéo avant ce « c'est bon ».

## Le storyboard (validation n° 3)

Fichier `storyboard.md`, d'après `gabarits/storyboard.md`.

### Le verrou (quatre lignes avant les tableaux)

```
Style : <identifiant du style> (catégorie)
Palette : 3 à 6 couleurs en hex (ou jusqu'au « Couleurs max » de la fiche du style)
Personnage : aucun / mains seulement / nom du personnage de la fiche « ma chaîne » / kit de personnages
Format : 1080x1920, 30 i/s, <durée> s
```

Deux lignes de plus, seulement dans ces cas :
- `Bleu-violet autorisé : <sa raison>` : le client a demandé cette couleur ;
- `Ouverture en texte : <ce que dit la fiche du style>` : le style ouvre sur une ligne de texte (démo produit, typographie, carton de film muet). Le rouge « le film s'ouvre sur du texte » devient jaune ; la ligne doit quand même poser l'enjeu et il doit lui arriver quelque chose avant 3 s.

Le nombre de couleurs va de 3 au « Couleurs max » de la fiche du style (6 sans fiche).

### Un plan par ligne

| Colonne | Ce qu'on y écrit |
|---|---|
| Temps | début-fin en secondes (`2,5-6`) |
| À l'écran | **la chose** qu'on voit, nommée (« une tasse fêlée sur une facture »), jamais « un titre », « une liste », « un fond » |
| Ce qui se passe | **un verbe d'action** (« la pile bascule »), jamais « apparaît », « s'affiche », « fondu » |
| Caméra | fixe, poussée lente, recul, panoramique, travelling, poussée rapide, coupe |
| Texte à l'écran | 5 mots au mieux, ou `-` |
| Son | le bruitage ou l'état de la musique ; note les silences |
| Rôle | accroche, montée, rebondissement, respiration, plan signature, chute |

### L'accroche avant 3 s, même dans un style à plans longs

La règle ne change pas : **avant 3 s, le spectateur a vu quelque chose se passer et sait de quoi il s'agit.** Mais « avant 3 s » ne veut pas dire « un plan de moins de 3 s ». Dans un style à plans longs (lumière qui glisse, estampe, plan-séquence : plans de 4 à 10 s), le premier plan peut durer, à condition qu'un **évènement** l'accroche dans ses trois premières secondes. Écris-le, daté en temps du film, dans la case « Ce qui se passe » :

```
| 1 | 0-6 | un comptoir de diner, une tasse | à 1,2 s : le néon s'allume et colore la tasse ; à 4 s : une main pousse l'addition | fixe | 6 h 42 | néon qui grésille | accroche |
```

Le lint lit ces « à x s : » : un premier plan qui dépasse 3 s sans évènement daté avant 3 s est rouge ; avec, il passe. Même écriture pour un plan long : avec une fiche « Mouvement : calme », un plan de 8 à 12 s est accepté (jaune) s'il contient au moins deux évènements datés ; au-delà de 12 s, ou sans eux, rouge.

### Ce que vérifie `lint_storyboard.py`

```
PYTHONDONTWRITEBYTECODE=1 python3 scripts/lint_storyboard.py storyboard.md --fiche <fiche STYLE.md> --script script.txt
```

`--fiche` lit dans la fiche du style le nombre de couleurs autorisé, « Caméra : fixe » (un film sans mouvement de caméra est alors normal, et c'est un mouvement de caméra qui est signalé), la dérogation bleu-violet et « Mouvement : calme ».

Feu **rouge** (on ne construit pas) :
- une ligne du verrou manque ; palette de moins de 3 couleurs ; une couleur bleu-violet sans autorisation ;
- tableau d'écart avec la démo absent, incomplet, ou moins de 4 « oui » ;
- un plan sans objet concret, ou qui décrit un écran vide ;
- un plan sans verbe d'action ;
- plus de 7 mots à l'écran ;
- un plan de plus de 8 s (style calme : plus de 12 s, ou 8 à 12 s sans deux évènements datés) ; colonne Temps illisible ;
- le premier plan est du texte, sans ligne « Ouverture en texte » dans le verrou ; l'accroche n'est pas le premier plan, ou dépasse 3 s sans évènement daté avant 3 s ;
- aucun plan « accroche », « rebondissement » ou « chute » ;
- plus de 30 % de plans à dominante texte ;
- un chiffre à l'écran absent du script (avec `--script`).

Feu **jaune** (à regarder) : plus de couleurs que le maximum de la fiche (6 sans fiche) ; 6 ou 7 mots à l'écran ; plan de moins de 1 s ou de 6 à 8 s ; plan long accepté d'un style calme ; ouverture en texte déclarée ; dernier plan en carton de texte ; trois fois la même caméra ; trois poussées d'affilée ; aucune caméra (ou, si la fiche dit « Caméra : fixe », une caméra qui bouge) ; dérogation bleu-violet de la fiche ; trous ou chevauchements dans les temps ; durée différente du format ; colonne Son vide ; chute loin de la fin.

Le lint ne juge pas si l'histoire est bonne. Il attrape ce qui fait un diaporama.

### La planche à montrer

Une image clé par plan, dans le look validé, avec le vrai code, assemblées en une planche numérotée : numéro, durée, son, transition vers le plan suivant. Envoie-la avec l'idée en une phrase et **ce dont tu es le moins sûr**.

Le client répond par numéro de case : pouce en haut ou en bas, et ses remarques. Tu redessines les cases refusées, tu relances le lint, tu remontres. Ces images sont les fonctions de scène de la vidéo : rien ne sera redessiné ensuite.

## Caméra et transitions au storyboard

- La caméra est une ponctuation : elle ne bouge pas quand on lit, ni quand l'image bouge déjà.
- Au moins quatre mouvements différents dans une vidéo, et de vrais changements de cadrage.
- Un aller appelle un retour : pas trois poussées de suite.
- Les transitions viennent du médium (une page qui tourne, une encre qui s'étale) et forment une seule grammaire. Pas de fondu par défaut.
- Aux moments clés, le sujet occupe au moins un tiers de la hauteur.

Les numéros des mouvements autorisés et interdits du style sont dans sa fiche et dans le skill `principes-mouvement`.

Sources : AGENTS.md « Style and story », DIRECTOR.md §5, §8, §11 et MY-STYLES.md de lemo-opuscar (LemoLab, MIT) ; FRAME.md et le storyboard par cases d'animate (cth9191, MIT) ; gabarit de découpage, lint et « trois directions » de huashu-art-motion (alchaincyf, MIT). Réécrit.
