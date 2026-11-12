---
name: styles-2-5d
description: "Catégorie de styles 2.5D : des personnages plats, dessinés, dans un décor 3D éclairé, pour toute vidéo verticale racontée (histoire vraie, fiction, humour, explication). À utiliser quand le client veut un récit avec des personnages dessinés dans un décor en relief, un format « bonhomme à tête ronde dans un décor de cinéma », ou demande ce rendu précis : contour à pleins et déliés, décor peint, caméra toujours en mouvement. Contient le prompt maître chiffré et un kit de production."
---

# Styles 2.5D : personnages plats, décor 3D

## À quoi sert la catégorie

Raconter en vertical, avec une seule voix, en mélangeant deux mondes :

- des **personnages volontairement simples** : plats, dessinés, une tête ronde, un torse, des traits pour les membres ;
- des **décors volontairement riches** : en volume, denses, peints, éclairés.

Le contraste fait la signature. Elle sert à quatre registres :

| Registre | Exemple de demande | Ce qui change |
|---|---|---|
| Histoire vraie | « raconte l'invention de la boîte de conserve » | **règle des sources obligatoire** (plus bas) |
| Fiction | « l'histoire d'une gardienne de phare qui attend une lettre » | ne jamais la présenter comme vraie |
| Humour | « un sketch entre un client et un garagiste » | le jeu : un seul personnage surjoue, l'autre reste figé |
| Explication | « pourquoi le pain lève » | un personnage guide, l'objet expliqué est en vrai volume |

Pourquoi le format ne ressemble pas à de l'animation générée : les personnages sont simples exprès, les décors sont riches exprès, chaque plan arrive sur une idée nouvelle du texte, une seule voix raconte.

## Les styles

| Identifiant | Nom | En une ligne | Moteur | Difficulté | Aperçu d'origine |
|---|---|---|---|---|---|
| `tete-ronde-trait-plein-delie` | Tête ronde, trait plein et délié | Personnages à tête ronde dont le contour s'épaissit côté ombre, décor 3D peint à joints dessinés et ombres bleu-violet, caméra en quasi plan-séquence. Toutes les valeurs sont mesurées. | blender | élevée | pas d'aperçu tiers (essai du kit) |
| `theatre-de-papier` | Théâtre de papier | Figurines de carton imprimé à marge blanche sur des décors en plans parallèles, éclairées par une rampe de bougies qui projette leurs ombres. | blender | moyenne | extrait d'un film LemoLab (lien seulement) |

Fiches : `styles/<identifiant>/STYLE.md`.

**Voir aussi (fiches portées par une autre catégorie)** : deux autres styles 2.5D à personnages plats servent à cette catégorie. Une seule fiche par style dans tout le plugin : elles ne sont pas dupliquées ici. Pour un récit dans l'un de ces styles, suivre `references/pipeline.md` de cette catégorie avec la fiche de l'autre.

- `diorama-pixel` (petits personnages en pixel art debout comme des découpes dans une maquette 3D embrumée) : `styles-jeu-retro/styles/diorama-pixel/STYLE.md`.
- `livre-pop-up` (un livre animé filmé sur un bureau, on tourne la page au lieu de couper) : `styles-matieres-3d/styles/livre-pop-up/STYLE.md`. Dans ce style, le carton reçoit la lumière et porte son ombre.

## Comment choisir

| Le client veut… | Style |
|---|---|
| Un récit vif, drôle ou documentaire, avec des personnages qui jouent | `tete-ronde-trait-plein-delie` |
| Une histoire ancienne, du théâtre, de l'humour pince-sans-rire | `theatre-de-papier` |
| Un récit d'aventure, une ambiance de jeu vidéo ou de conte | `diorama-pixel` (catégorie `styles-jeu-retro`) |
| Une vie ou une histoire en chapitres, un ton tendre ou familial | `livre-pop-up` (catégorie `styles-matieres-3d`) |
| Aucune préférence | `tete-ronde-trait-plein-delie` (le seul dont chaque valeur est mesurée et outillée) |

`theatre-de-papier` est le plus simple (tout est plat, la lumière vient d'un seul endroit) : commencer par lui avec un client qui découvre Blender. Un seul style par vidéo ; une série garde le même style d'un épisode à l'autre.

## Le prompt maître

`references/prompt-maitre.md` contient **toutes les règles chiffrées** du style `tete-ronde-trait-plein-delie`, en dix rubriques : personnages, jeu, décor, caméra et montage, sous-titres, son, histoire, production, interdits, contrôles. Chaque règle a sa valeur, son unité (en fraction du diamètre de la tête, D) et sa raison.

- C'est un texte autonome : donné tel quel à un agent, avec le sujet du client, il suffit à produire le rendu sans référence sous les yeux.
- **Lis-le en entier avant de dessiner ou de construire quoi que ce soit dans ce style.** La fiche du style n'en est que le résumé.
- Les mêmes valeurs sont en données dans `kit/regles.py`.
- La rubrique « Production » dit comment rendre vite (une plaque de décor par tronçon de caméra) ; méthode et mesures : `references/rendu-rapide.md`.

## Le parcours

`studio-coeur` pilote : questions, validations, porte de livraison, relecteur indépendant. Cette catégorie fournit le contenu de chaque étape.

### 1. Les questions au client

Quatre au plus à la fois, à choix, comme le demande `studio-coeur`. Il faut repartir avec cinq réponses :

| Question | Ce qu'on en tire |
|---|---|
| **Le sujet** : quelle histoire, et se dit-elle vraie ? | le registre ; si elle se dit vraie, la règle des sources s'applique |
| **Le lieu** : où cela se passe-t-il ? | 2 à 4 décors, leur vocabulaire d'objets (30 à 45 objets par plan) |
| **L'époque** | costumes, matières, sources de lumière (lampe, fenêtre, feu) |
| **Les personnages** : qui, combien (1 à 4), comment les reconnaît-on ? | pour chacun : couleurs du costume, coiffe, un accessoire ; décrits au générateur `kit/pantin.py` |
| **L'ambiance** : quelle lumière ? | une ambiance par lieu parmi plein jour, coucher de soleil, intérieur chaud, nuit bleue |

Dis au client dès cette étape le temps que cela prend (plus bas) et ce qui n'est pas encore au niveau.

### 2. L'histoire

Script selon `references/pipeline.md` (étapes 1 et 2) et la rubrique « Histoire » du prompt maître : accroche dès l'image 0, 3,0 à 3,6 mots par seconde, une idée par station de caméra. **Validation n° 1.**

### 3. Les 3 ou 4 images de SON histoire

C'est la validation n° 2 de `studio-coeur` (`skills/studio-coeur/references/look-et-storyboard.md`) : **3 ou 4 images de l'histoire du client, rendues avec le vrai code, à la taille finale (1080 × 1920)**. Pas de maquette : ce code deviendra la vidéo. Ici :

1. décris ses personnages dans `kit/film.py` et sors leur planche (face, trois quarts, expressions) ;
2. construis un premier décor et rends-en les trois passes sur 3 ou 4 images qui couvrent ses ambiances et ses cadrages (un plan en pied serré, un plan large, un gros plan) ;
3. assemble-les avec `kit/compo.py` et montre-les ;
4. le client critique chaque image, tu refais ce qui ne va pas, on recommence jusqu'à ce que cela lui aille. Aucune vidéo n'est lancée avant.

### 4. Le storyboard

Une image par station, sur une planche numérotée. **Validation n° 3.** Rien n'est animé avant.

### 5. Les plans de test

Avant le film entier : **3 à 5 plans de test** (8 à 10 s) qui couvrent les ambiances et les cadrages. Tant qu'on règle le cadrage, la caméra et le jeu, ils se rendent en demi-taille (−36 % de temps) ; le contrôle et les images montrées au client restent à la taille finale. Puis :

1. le contrôle chiffré (`kit/controle.py`) : tableau « règle du prompt maître / mesuré / dans la tolérance ? » ;
2. une critique par un agent indépendant qui n'a que le prompt maître et les plans : quelles règles sont violées, note sur 10 ;
3. un tour de corrections, une nouvelle note ;
4. tu montres au client les plans, la note telle quelle, ce qui reste différent.

### 6. Le film

Après son accord : rendu complet (`kit/lancer.py`), voix, son (skill `son`), sous-titres, revue et livraison selon `studio-coeur`.

## Règles non négociables

1. **On mesure, on ne devine pas.** Toute valeur du style vient du prompt maître ou de `kit/regles.py`. Une valeur « à l'œil » n'entre pas dans le film.
2. **Tout est exprimé en D** (diamètre de la tête) et recalculé à chaque plan.
3. **Contour à pleins et déliés, réglé par la lumière du plan** ; encre prune, jamais noire.
4. **La tête n'est pas un aplat** : croissant d'ombre et filet de lumière.
5. **Une pose change en une image, puis elle est tenue.** Un seul personnage joue à la fois.
6. **Le décor est en volume, dense et peint** : aucune matière en aplat, 30 à 45 objets par plan, rien de nu derrière un personnage. Un intérieur est sombre, avec une seule dominante chaude et un contrepoint froid.
7. **Les ombres sont un mélange vers un bleu-violet**, jamais une multiplication.
8. **Le sol est net sous les pieds** ; le flou ne touche que le lointain et le tout premier plan.
9. **La caméra ne s'arrête presque jamais** : stations d'environ 1,1 s, reliées par des déplacements et des fondus courts.
10. **Sous-titres de 1 à 2 mots**, secs ; l'action arrive 2 à 4 images après le mot.
11. **Format** : vertical 1080 × 1920, 30 images par seconde, rendu à la taille exacte. Son à −14 LUFS.
12. **Contrôle chiffré et critique indépendante avant de livrer** ; la note s'écrit telle quelle.
13. **L'objet dont parle l'histoire est en vrai volume**, jamais un dessin plat.

`theatre-de-papier` a ses propres règles de dessin et de lumière (sa fiche) ; il garde les règles 10 à 13.

## La règle des sources

**Obligatoire dès que l'histoire se dit vraie**, quel que soit le style.

- Chaque affirmation du texte et chaque chiffre à l'écran a sa source dans `sources.md`, en tableau fait par fait, avec ses nuances (`references/pipeline.md`, étape 2).
- Ce qui n'est pas sourcé est retiré, ou présenté comme une légende.
- Une fiction ne se présente jamais comme vraie : ni « histoire vraie » dans le texte, ni date ou chiffre inventés donnés pour réels.
- Une explication (science, technique) suit la même règle que l'histoire vraie pour chaque fait énoncé.

## Mise en garde : vos sujets, votre dessin

À dire au client dès la première conversation, et à tenir ensuite.

- **Choisir ses propres sujets.** Une histoire déjà racontée par une chaîne du même format n'est pas un sujet : en trouver une autre.
- **Dessiner ses propres personnages.** Coiffe, couleurs, accessoire, proportions du visage : assez différents de tout personnage de chaîne existant pour qu'on ne les confonde pas sur une vignette. Le générateur du kit ne contient aucun personnage tout fait : il dessine ceux que le client décrit.
- **Construire ses propres décors**, avec ses lieux et ses objets.
- **Ne jamais reprendre un personnage, un costume, un accessoire, un décor, un texte ni un sujet d'une chaîne existante.** Personnages plats dans un décor éclairé, trait plein et délié, ombre mélangée : c'est une technique, libre. Le bonhomme d'une chaîne, ses sujets, son ton, pris ensemble : c'est son identité. Si un spectateur peut croire à un épisode de cette chaîne, c'est trop près.
- Si le client demande « la même chose que telle chaîne », propose la technique et refuse la copie. Pour mesurer la technique d'une vidéo qu'il admire : skill `reproduire-reel`.
- Les exemples du kit (la gardienne de phare et le facteur de la chaîne mesurée ; « Galet » dans l'ancienne chaîne) sont eux aussi à remplacer.

Pourquoi cette insistance : les valeurs de ce style viennent de la mesure d'une vidéo existante, étudiée en interne. On en a tiré des lois de dessin, de lumière et de rythme. Rien de son contenu n'est dans le plugin, et rien ne doit y revenir par le client.

## Le kit de production

`kit/` contient deux chaînes (lire `kit/LISEZMOI.md`).

| Chaîne | Pour quel style | Fichiers | Principe |
|---|---|---|---|
| **Chaîne mesurée** | `tete-ronde-trait-plein-delie` | `regles.py`, `pantin.py`, `camera.py`, `plaque.py`, `film.py`, `bl_decor.py`, `bl_scene.py`, `compo.py`, `lancer.py`, `controle.py` | Blender rend le décor en trois passes (couleur peinte, lumière, données), une fois par tronçon de caméra quand elle ne fait que dériver ; l'assemblage pose la lumière de l'ambiance, les contours, le ciel, le flou, les personnages dessinés et leur ombre, l'accentuation, les sous-titres |
| Chaîne à plans émissifs | `theatre-de-papier`, et la boucle de rendu long | `plans.py`, `personnages.py`, `bl_lib.py`, `bl_film.py`, `bl_cli.py`, `bl_plage.py`, `rendre.py`, `refaire.py`, `suivi.py` | les personnages sont des plans dans la scène Blender, tout est rendu d'un coup |
| Outils communs | les deux | `reglages.py`, `mix.py`, `ecart_voix.py`, `hf_build.py`, `revue.py`, `planche.py` | réglages, son, assemblage HyperFrames, planches de revue |

Dans la chaîne mesurée, un épisode devient : **des personnages décrits, une liste de plans, un décor ou deux**. `film.py` et `bl_scene.py` contiennent un exemple neutre de 3 plans (deux en intérieur chaud, un en extérieur au couchant, deux personnages) à remplacer en entier.

## Ce qui n'est pas encore au niveau

Dit sans détour. À dire au client avant de commencer.

| Point faible | Ce qu'on a constaté | Ce qu'on fait en attendant |
|---|---|---|
| **Le décor n'atteint pas encore la référence** | Un critique indépendant note 7 sur 10 l'extérieur au couchant et 7 sur 10 l'intérieur chaud refait (5 avant ; la référence : 9). Contrôle chiffré des premiers plans de test : 34 grandeurs dans la tolérance, 25 hors, 2 non mesurées. | Soigner d'abord ce qui entre dans le champ de chaque plan : boiseries et mobilier derrière les personnages, une source de lumière visible, un contrepoint froid. |
| **Intérieur chaud** | **7 sur 10 maintenant** (6,5 puis 7 ; décor 6,5 puis 7 ; intégration du personnage 6 puis 6,5 ; 5 avant), avec les règles de l'intérieur sombre à touches froides ; 28 lignes sur 30 dans la tolérance. Ce qui reste : rien ne passe devant le personnage ; la lampe ne fait pas de tache nette au sol ni sur la table ; liseré presque invisible sur la peau ; objets nets proches aux faces trop noires et au trait plus mou ; un objet encore coupé par le cadre ; palette hors tolérance sur un plan de face (prune 28 %, bruns 34,1 %). | Cadrer serré devant un fond sombre et flou ; limiter le plancher éclairé dans le cadre ; donner la lampe principale de chaque plan (`source`). |
| **Plein jour et nuit** | Lois mesurées, jamais essayées dans nos décors refaits. | Annoncer un tour de réglage de plus pour ces ambiances. |
| **Fil du bois** | **Dessiné maintenant** par script (veines ondulées, nœuds, cernes), à la place du bruit étiré (contraste de 10,9 contre 20,8). Mesuré : table, contraste 16,8 et grain fin 7,9 ; plancher, contraste 15, un joint tous les 0,334 D. Dans la tolérance, encore sous la cible (18 à 21 ; 8,5 à 12,7). | Utiliser le bois du kit partout, plafond et poutres compris. |
| **Deux natures de trait** | Le contour du décor, tiré de la profondeur, est légèrement tremblé ; celui des personnages est vectoriel. | Assumé pour l'instant. |
| **Vues des personnages** | Face et trois quarts ; ni profil strict ni dos. Skill `personnages`, `references/limites-du-pantin.md`. | Mettre en scène de face ou de trois quarts. |
| **Objet héros complexe** | Les formes tournées et les boîtes sortent bien ; les formes organiques non. | Choisir un objet fait de formes simples, ou prévoir du modelage à la main ; toujours la planche 6 angles (skill `blender`). |
| **Voix de synthèse** | Très régulière ; ses repères de mots peuvent être décalés (107 ms constatés). | Faire enregistrer le client ; sinon contrôler l'écart avec `kit/ecart_voix.py`. |
| **Temps de rendu sur carte graphique intégrée** | Le rendu par tronçons va 2,3 fois plus vite que l'image par image sur 4 plans de test ; un film de 61,5 s est estimé à environ 3 h 10 (7 h 40 avant). C'est l'assemblage qui pèse le plus, à environ 4 s par image. Un film entier n'a pas été chronométré ainsi. | Vérifier les tronçons avec `python outils/lancer.py plans` ; rendre d'abord les plans de test ; tout réglage d'ambiance se fait à l'assemblage, sans relancer Blender. |
| **Plaque de décor** | Elle trahit au-delà de 120 px de parallaxe (premier plan étiré ou dédoublé à 307 px), sur un décor animé (l'objet reste figé) et sur les ombres ou les lampes qui bougent. Des tronçons réunis peuvent arriver juste sous le seuil (119 px), alors que la validation image par image s'arrête à 112 px. | Dire `anime=True` quand le décor bouge ; forcer `mode="3d"` au moindre étirement. |

**Essai du kit, le 12/11/2026.** Avec le seul kit, sur un sujet inventé pour l'occasion (une gardienne de phare attend une lettre, le facteur arrive) : un film de 7 s, 210 images, 2 plans (un intérieur chaud, un extérieur au couchant), 2 personnages décrits en données, sans son. Rendu Blender : 4,2 s par image pour les trois passes (220 images en 15,6 min, scène de 1 270 objets réunis en 60). Assemblage : 8 à 10 s par image et par processus (210 images en 12 min avec trois processus). Contrôle chiffré automatique (`controle.py`) : **57 lignes dans la tolérance, 4 hors, aucune non mesurée** sur 61 (hors tolérance : la densité de deux images, et le contour relu dans le film encodé sur une pose où la coiffe et un bras levé touchent la tête). Critique d'un agent indépendant qui n'avait que le prompt maître et le film : **5 sur 10** avant corrections, **7 sur 10** après un tour (personnages 8, jeu 8, décor 6, caméra et montage 7, sous-titres 8,5, histoire 7,5 ; plus aucun défaut bloquant). Ce qui reste, d'après lui : caméra trop calme sur les plans d'extérieur (3 à 9 px par seconde pour 20 à 30 demandés), un doigt coupé par le bord du cadre pendant une tenue, des objets du décor coupés par le cadre, un fil du bois qui reste un bruit étiré, des bords trop peu assombris en extérieur, un soleil pâle, un trait de décor crénelé. Le film d'essai n'est pas dans le plugin ; l'exemple qui l'a produit y est (`kit/film.py`, `kit/bl_scene.py`).

**Essais du 12/11/2026 : intérieur sombre et rendu par tronçons.** Les chiffres de l'essai ci-dessus datent d'avant ces deux chantiers. Intérieur refait sur 2 plans : notes du critique dans le tableau ci-dessus, écrites telles quelles. Écrit sans mesure : la pénombre du soleil à 3,5° et l'effacement du liseré des cailloux. Rendu par tronçons : mesures dans « Les temps réels » et dans `references/rendu-rapide.md`.

## Les temps réels

Mesurés par le studio sur un PC de bureau à carte graphique intégrée, un agent et ses sous-agents.

| Étape | Temps réel |
|---|---|
| Analyser une vidéo de référence d'une minute et sortir des plans de test fidèles (facultatif, skill `reproduire-reel`) | environ 2 h pour les personnages, 3 h 40 de plus pour le décor |
| Décrire les personnages et sortir leurs planches | quelques minutes |
| Construire un décor avec la bibliothèque du kit, mises au point comprises | environ une demi-journée par lieu la première fois ; la construction de la scène par Blender prend 16 s |
| Rendu Blender image par image, trois passes, 1080 × 1920 | 5,29 s par image (couleur 1,69 ; lumière 2,74 ; données 0,86), décor lourd de 3 656 objets réunis en 535 ; la veille, machine plus chargée : 9,2 s |
| Le même, en demi-taille (plans de test) | 3,38 s par image (−36 %) |
| Une plaque de décor (1 124 à 1 406 px de large) | 6,1 s en moyenne |
| **Rendu par tronçons** (seuils 12 et 120 px), 4 plans de test, 256 images | 107 images en 3D et 5 plaques : **9,9 min, soit 2,33 s par image** (22,6 min image par image : 2,3 fois plus vite) |
| Film d'exemple du kit (3 plans, 229 images avec les images de contrôle) | 70 rendus Blender au lieu de 229, à 4,6 à 5,0 s par rendu |
| **Assemblage** | environ **4 s par image de film** avec 5 ou 6 processus (109 images en 396 à 433 s) ; 210 images en 15 min avec 2 processus, en 12 min avec 3 |
| Avant le rendu par tronçons (la veille) | environ 15 s par image de film, tout compris : 61,5 s de film = environ 7 h 40 |
| **Estimation pour un film de 61,5 s** (1 845 images), non mesurée | un tiers des images en 3D : environ 650 images (57 min) et une centaine de plaques (10 min), soit environ 1 h 10 de Blender ; assemblage : environ 2 h ; **total : environ 3 h 10** |
| Un tour de correction d'ambiance (lumière, contours, flou, palette) | aucun rendu Blender : seulement l'assemblage |
| Contrôle chiffré, critique, corrections | environ 30 min par tour |
| Ancienne chaîne à plans émissifs | 3,6 s par image, soit 1 h 50 pour 61,5 s |

Carte graphique dédiée : non mesuré. Passes regroupées en un seul rendu : non mesuré. Un seul Blender rend à la fois ; ne rends jamais la main pendant qu'un rendu tourne. Méthode, écarts mesurés et limites du rendu par tronçons : `references/rendu-rapide.md`.

## Skills à charger avec cette catégorie

- `studio-coeur` : **pilote le parcours** (questions, validations, porte de livraison, relecteur indépendant).
- `personnages` : pièces, expressions, jeu d'acteur ; `references/trait-et-lumiere-mesures.md` (le trait et la lumière mesurés), `references/limites-du-pantin.md`.
- `blender` : connecteur, décors, objet héros, rendu long ; `references/trois-passes-et-matieres-peintes.md`.
- `rendu` : assemblage HyperFrames, sous-titres, zones d'interface, export.
- `son` : voix, bruitages, musique, −14 LUFS.
- `reproduire-reel` : la méthode de mesure et les scripts du contrôle chiffré ; à charger aussi quand le client arrive avec une vidéo qu'il admire.
- `principes-mouvement` : dictionnaire des mouvements (les fiches citent leurs numéros).
- `marque` : la fiche « ma chaîne » du client.

## Références

- `references/prompt-maitre.md` : toutes les règles chiffrées du style, en un texte autonome.
- `references/rendu-rapide.md` : rendre vite, une plaque de décor par tronçon de caméra (méthode, mesures, où ça trahit, estimation).
- `references/pipeline.md` : le parcours de production détaillé (histoire, sources, liste de plans, voix, son, revue).
- `kit/LISEZMOI.md` : le kit (ordre des étapes, rôle de chaque fichier, ce qu'on change pour un nouvel épisode).
- `styles/tete-ronde-trait-plein-delie/STYLE.md`
- `styles/theatre-de-papier/STYLE.md`
- Fiches voisines : `styles-jeu-retro/styles/diorama-pixel/STYLE.md`, `styles-matieres-3d/styles/livre-pop-up/STYLE.md`

Crédits : voir `licenses/styles-2-5d.md` à la racine du plugin.
