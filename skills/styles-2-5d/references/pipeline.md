# Parcours de production d'une vidéo 2.5D

> **À lire d'abord : deux chaînes de fabrication dans le kit.**
> - **La chaîne mesurée** (`kit/lancer.py`, `kit/compo.py`, `kit/pantin.py`, `kit/bl_decor.py`, `kit/controle.py`) est celle du style `tete-ronde-trait-plein-delie`. Ses règles chiffrées sont dans `references/prompt-maitre.md`, son mode d'emploi dans `kit/LISEZMOI.md`. Pour ce style, ce document vaut pour **l'histoire, les sources, la liste de plans, la voix, le son et la revue** (étapes 1 à 4 et 6 à 9) ; l'étape 5 (fabriquer) et l'étape 8 (assembler) se font avec la chaîne mesurée, et les sous-titres suivent le prompt maître (1 à 2 mots, minuscules, centre à y = 1 350), pas la bande décrite à l'étape 6.
> - **La chaîne à plans émissifs** (`kit/plans.py`, `kit/bl_film.py`, `kit/rendre.py`…) est celle que décrivent les étapes Blender ci-dessous, avec les règles marquées « rendu réel du 11/11/2026 ». Elle sert à `theatre-de-papier` et garde la boucle de rendu long.
>
> **Registres.** La catégorie ne se limite plus aux histoires vraies : fiction, humour et explication suivent le même parcours. **La règle des sources (étape 2) reste obligatoire dès que l'histoire se dit vraie**, et pour chaque fait énoncé dans une explication. Une fiction saute le tableau des sources, et ne se présente jamais comme vraie.

Source : cours « How to build a 2.5D motion studio » (parties 3 à 9), adapté au studio : assemblage dans HyperFrames (jamais Remotion), son à −14 LUFS, tout en français.

`studio-coeur` pilote les validations avec le client. Ce document dit **quoi produire** à chaque étape.

**Règles tirées d'un rendu réel.** Les passages marqués « rendu réel du 11/11/2026 » viennent d'un film complet de 61,5 s (36 plans, 1 845 images, trois décors, huit personnages plats, un objet héros) fabriqué de bout en bout par le studio sur un PC Windows à carte graphique intégrée, avec Blender 5.3 (EEVEE), le connecteur MCP et HyperFrames, puis critiqué deux fois par un agent qui ne l'avait pas fabriqué. Ce film est un essai interne, non publié et non fourni. Ses outils, débarrassés de tout ce qui lui était propre, forment le **kit de départ** : `kit/` (lire `kit/LISEZMOI.md`). Les étapes ci-dessous disent à chaque fois quel outil du kit sert.

## Dossier de l'épisode

Tout l'épisode vit dans un dossier, qui sert de modèle au suivant :

```
<episode>/
  script.md          le texte de la voix
  sources.md         une source par affirmation
  plans.md           la liste de plans et les temps clés
  sons.md            la liste des sons, en numéros d'image
  personnages/       pièces, expressions, fiches
  decors/            un fichier .blend par décor
  rendus/            images des plans
  plans/             un fichier vidéo par plan
  voix/              enregistrement et temps mot à mot
  revue/             planches et notes de revue
  sortie/            la vidéo finale
```

**Avec le kit**, le dossier a la même allure, à trois différences près (rendu réel du 11/11/2026) :

- `outils/` contient le kit, et **`outils/plans.py` est la source de la liste de plans** : `plans.md` et `son/reperes.json` sont écrits par lui. Blender lit le même fichier, donc la liste et l'animation ne peuvent pas diverger.
- **tout le film est une seule scène**, `decors/film.blend` : les décors sont construits loin les uns des autres dans la même scène, la ligne de temps de Blender est le film (image 0 = première image), une caméra par plan est liée à un repère. Une correction devient un numéro d'image et on ne re-rend que les images touchées. « Un fichier par décor » reste possible pour un film fait à la main, sans le kit.
- `rendus/` contient **toutes les images du film** sous un seul nom (`f_0000.jpg` à `f_NNNN.jpg`) ; il n'y a plus de dossier `plans/` : le film est encodé d'un bloc. Ce que les outils écartent va dans `_a_supprimer/` (ils ne suppriment jamais rien).

## Format fixe

1080×1920, 30 i/s, 55 à 70 s. Rendu à la taille exacte, jamais recadré ni agrandi.
Image = secondes × 30 ; la vidéo commence à l'image 0. **Tous les documents parlent en numéros d'image.**

---

## Étape 1 : choisir l'histoire

Pour une histoire vraie ou une explication, proposer **5 histoires vraies** (histoire, science, objets, inventions) qui tiennent dans l'un de ces titres (pour une fiction ou un sketch : 5 situations, chacune en une ligne, avec le personnage, le lieu et la chute) :

- « Le/La [objet] qui [a fait quelque chose de surprenant] »
- « Pourquoi [chose] fait toujours [X] »
- une question : pourquoi, comment, que s'est-il vraiment passé.

Pour chacune : l'histoire en une ligne, pourquoi un enfant de 12 ans et un adulte de 50 ans la répéteraient tous les deux, et, si elle se dit vraie, **2 sources ouvrables**.

Test : si l'histoire ne fait pas dire « attends, vraiment ? », elle n'arrêtera pas un inconnu qui fait défiler son fil.

**Validation : le client choisit.**

## Étape 2 : le texte et les sources

`script.md` :

- **150 à 170 mots** (une voix posée lit environ 160 mots en 65 s ; c'est tout le budget) ;
- un seul narrateur, langue parlée, phrases courtes ;
- la **première phrase est l'accroche** et fait une promesse ;
- un **retournement vers la 40e seconde** ;
- la **dernière phrase tient la promesse** de la première ;
- compter les mots et l'écrire en tête du fichier.

`sources.md`, une ligne par affirmation :

```
| # | Affirmation (mots du texte) | Source | Lien | Vérifié par le client |
|---|---|---|---|---|
| 1 | « en l'an 132 » | Encyclopédie X, article … | https://… | oui / non |
```

Règles :

- **Toute affirmation factuelle du texte a une source.** Dates, chiffres, noms, lieux, « le premier », « le plus grand ».
- Tout nombre ou toute affirmation **affiché à l'écran** doit être dans `sources.md`.
- Deux sources indépendantes pour le fait central.
- Ce qui est incertain ou légendaire se dit comme tel dans le texte (« selon la chronique… »).
- **Le client ouvre et vérifie lui-même les sources.** C'est la seule étape qu'on ne lui retire jamais : une date fausse dans les commentaires coûte plus de confiance que n'importe quel rendu n'en rapporte.

**Vérification fait par fait (rendu réel du 11/11/2026).** Le tableau ci-dessus ne suffit pas quand les sources ne disent pas toutes la même chose. Ce qui a marché sur un texte de 170 mots (20 affirmations, 15 minutes) :

1. **Trois sources de natures différentes** : la source la plus proche du fait (texte d'époque, publication d'origine, registre), une synthèse de référence, un article de presse ou de musée. Leur donner un sigle en tête de `sources.md`.
2. **Une ligne par affirmation, dans l'ordre du texte**, avec les sigles qui l'appuient et **la phrase exacte** de la source (citation courte, dans sa langue) :

```
| # | Dans le film | Source | Appui |
|---|---|---|---|
| 7 | « loin à l'ouest » | B, C | B : « … from the west … ». Nuance : A dit « nord-ouest » ; le lieu est à l'ouest-nord-ouest. On dit « à l'ouest », vrai dans les deux lectures. |
```

3. **Les nuances s'écrivent, dans `sources.md` et dans le texte.** Trois cas rencontrés : un mot traduit de deux façons (on garde le mot courant et on note l'autre) ; une direction ou une date sur laquelle les sources divergent (on choisit la formule vraie dans toutes les lectures) ; un chiffre qui va du simple au double (on ne donne **aucun chiffre** : « des centaines de kilomètres »).
4. **Une section « Ce que le film ne dit pas (et pourquoi) »** : ce qui est incertain ou reconstitué (un mécanisme, une date, un objet disparu) n'est ni dit ni montré. Cela décide aussi de l'image : pas de plan sur ce qu'aucune source ne décrit.
5. Une affirmation appuyée par une seule source reste possible si c'est la source d'origine ; le noter.
6. Une traduction faite pour l'épisode est une traduction de travail : la faire relire avant publication.

**Validation : texte et sources.**

## Étape 3 : la liste de plans

**La liste de plans s'écrit comme des données** (rendu réel du 11/11/2026) : dans `outils/plans.py` du kit, un dictionnaire par plan (bornes en numéros d'image, mots couverts, décor, caméra et sa raison, personnage, objet, son, ligne de jeu). `python outils/plans.py` vérifie que les bornes se suivent sans trou et écrit `plans.md`. Le moteur lit ce même fichier pour poser les caméras et l'animation : on ne recopie jamais une borne à la main.

`plans.md`. **Un plan par idée** du texte, 1,5 à 3 s chacun (une trentaine de plans pour 65 s, une coupe environ toutes les 2 s). Un plan nouveau arrive sur une idée nouvelle, jamais sur un minuteur.

Pour chaque plan :

```
PLAN 18   images 1215-1265 (1,7 s)   « …et à cinq heures, le marteau est tombé. »
  DÉCOR       décor 2 (chambre de l'horloger), côté fenêtre, près de l'établi
  CAMÉRA      large sur le réveil, avancée lente ; raison : on attend avec la maison endormie
  PERSONNAGE  aucun
  OBJET       le réveil (objet héros, en 3D) ; le marteau frappe la cloche
  SON         déclic du ressort, puis coup de cloche
```

Champs :

| Champ | Contenu |
|---|---|
| numéro, images, durée, mots couverts | le plan est attaché aux mots qu'il illustre |
| **DÉCOR** | lequel, et où dans le décor |
| **CAMÉRA** | cadrage + mouvement (fixe, avancée, travelling) **et sa raison** |
| **PERSONNAGE** | qui, quelle pose, quelle expression de la planche |
| **OBJET** | l'objet héros s'il est à l'image (toujours construit en 3D, jamais dessiné) |
| **SON** | seulement si quelque chose de physique se passe |

**Réutiliser les décors : 3 à 5 pour tout l'épisode, pas 30.** Un même décor donne plusieurs plans en changeant de caméra, de focale, d'heure ou de lumière.

Contrôles de la liste :

- aucun plan de plus de 3 s sans idée nouvelle ;
- deux plans voisins n'ont jamais le même cadrage ;
- l'objet héros a au moins un gros plan ;
- le premier plan montre l'accroche, pas un titre ;
- un personnage à l'écran a toujours quelque chose à penser (skill `personnages`).

Trois contrôles ajoutés après le rendu réel du 11/11/2026 (c'est la critique qui les a trouvés, pas le fabricant) :

- **Le sujet tient dans les 65 % du haut de l'image** (au-dessus de y ≈ 1250 sur 1920) : visage, objet héros, action. Plus bas, les sous-titres au mot le couvrent. En plan taille, cadrer le personnage plus haut qu'on ne le ferait sans sous-titres. Le kit le mesure à la construction (`controle_sujet`, ligne « cadre plan … ok / À REVOIR »).
- **Aucun double de l'objet héros dans le cadre ne contredit l'action.** Si l'objet existe en plusieurs exemplaires (huit clochettes identiques sur une étagère, deux portes, une rangée de lampes) et que l'histoire dit « une seule sonne », un voisin resté en place dans le cadre fait lire « rien ne s'est passé ». Choisir l'axe de caméra qui n'en montre qu'un (un profil, un cadre plus serré), ou sortir les voisins du champ. À vérifier sur l'image du contact et sur la dernière image du plan.
- **L'action centrale a une arrivée visible** : on voit où l'objet va, pas seulement d'où il part (une chute filmée de dos ne prouve rien).

Durées constatées : 36 plans pour 61,5 s, soit 1,71 s en moyenne ; six plans de 1,3 à 1,5 s (l'idée tenait en trois mots), aucun au-dessus de 2,5 s.

## Étape 4 : les temps clés en numéros d'image

Pour chaque moment important, un tableau **en images, pas en secondes**. Exemple (valeurs de départ pour notre propre version d'une histoire, non mesurées sur une vidéo existante) :

```
IMAGE   TEMPS    ÉVÉNEMENT
1215    40,5 s   PLAN 18 commence : large sur le réveil, nuit, la maison dort
1230    41,0 s   l'avancée commence, échelle 1,00 → 1,06 sur 60 images
1248    41,6 s   le ressort se détend
1254    41,8 s   le marteau part
1262    42,1 s   le marteau touche la cloche (son du coup sur cette image)
1266    42,2 s   COUPE vers PLAN 19 : les yeux de l'horloger s'ouvrent
1272    42,4 s   sous-titre « tombé » entièrement lisible
1290    43,0 s   fin de la tenue, coupe
```

- **La physique tient honnête** : une chute de 30 cm dure environ un quart de seconde, soit 7 à 8 images à 30 i/s. Plus lente, elle paraît flotter, et le spectateur le sent sans savoir le dire.
- Désormais, chaque correction est un nombre. « Déplacer le coup à 1260 » ne peut pas être mal compris.

**Validation : liste de plans et temps clés** (avec, si le client le souhaite, la passe 1 d'un décor et la planche du personnage : voir étape 5).

## Étape 5 : fabriquer

Dans cet ordre, avec un contrôle visuel après chaque sous-étape.

1. **Décors** (skill `blender`, `references/decor-3-passes.md`) : formes et caméras, lumière motivée, habillage. Montrer au client la planche des caméras (passe 1) et trois images éclairées (passe 2).
2. **Objet héros** (skill `blender`, `references/objet-heros.md`) : construit à part, planche 6 angles, puis posé sur sa marque.
3. **Personnages** (skill `personnages`) : pièces SVG, planche d'expressions validée, import en plans à matériau émissif avec ombre de contact, à la marque de mise au point.
4. **Ligne de jeu** pour chaque plan avec personnage (pensée, anticipation, action, tenue), puis animation : poses clés d'abord, mouvement ensuite.
5. **Animation des objets** selon les temps clés.

Avec le kit : `python outils/personnages.py` (pièces, `rig.json`, planche d'expressions), puis `bl_film.py` construit décor, objet héros, caméras et animation en trois passes (`python outils/rendre.py --construire --passe 1`, puis `2`, puis `3`), et `python outils/rendre.py --controle …` rend les planches à basse résolution. On relit des **rendus** en planche, pas la vue 3D : eux seuls montrent les plans émissifs et la profondeur de champ.

Règles de fabrication :

- **une clé de déplacement se tient** (rendu réel du 11/11/2026) : à la fin d'un déplacement, la clé d'arrivée est en interpolation constante. Sinon le personnage continue de glisser vers sa position du plan suivant (un personnage qui ne s'arrêtait pas à son arrivée, trois autres qui sortaient du cadre). Le kit le fait dans `Perso.deplace()` et le contrôle à la construction (ligne « glissements 0 ») ;
- les lumières du décor n'ombrent jamais un personnage ;
- chaque personnage a son ombre de contact ;
- matières avec usure et variation, rien de parfaitement propre ;
- caméra : avancée ou travelling lents, avec la raison notée dans la liste de plans.

## Étape 6 : la voix et les sous-titres

**Voix.** Recommander au client d'**enregistrer le texte lui-même** : une vraie voix, avec ses respirations, est le plus fort signal de confiance du format, et elle évite toute question de voix clonée. S'il préfère une voix de synthèse, n'utiliser qu'une voix sur laquelle il a les droits (skill `son`). Une seule voix pour toute la vidéo.

**Temps mot à mot.** Transcrire la voix avec horodatage par mot :

```bash
whisper voix/voix.wav --model small --language fr --word_timestamps True --output_format json --output_dir voix/
```

Convertir chaque début de mot en numéro d'image (secondes × 30, arrondi).

**Quel outil pour l'horodatage (rendu réel du 11/11/2026).** Il faut un début de mot juste à une image près (33 ms).

| Outil | Constat |
|---|---|
| faster-whisper avec horodatage au mot, ou un **alignement forcé** du texte connu sur le son | À utiliser. C'est aussi la voie du skill `rendu` (`references/sous-titres.md`). Non installé sur le poste du rendu réel : non essayé ce jour-là. |
| whisper.cpp appelé par ffmpeg | **Trop grossier** : le texte entendu était juste, les horodatages au mot inutilisables. Sert à vérifier que la voix dit bien le texte, pas à caler. |
| Repères de mots fournis par une voix de synthèse | Utilisables, **après contrôle** (ci-dessous). |

**Voix de synthèse : contrôler l'écart entre les repères et le son.** Les repères de mots livrés avec une voix de synthèse ne sont pas forcément calés sur le son. Constat du rendu réel : le son était **en retard de 107 ms** sur les repères (dit autrement : les repères avaient 107 ms d'avance), de façon constante sur les 16 répliques. Trois images : assez pour que chaque sous-titre et chaque coupe arrive avant la voix.

1. Mesurer : `python outils/ecart_voix.py` compare, pour chaque début de réplique, le repère au vrai début de la parole **lu sur la forme d'onde**. C'est la forme d'onde qui arbitre, pas une seconde transcription.
2. Écart médian sous 33 ms : ne rien faire.
3. Écart constant (dispersion faible) : le corriger **une seule fois, à un seul endroit**. Le plus simple est d'avancer la voix au mixage (`voix.avance_s` dans `son/design.json`) : l'image et les sous-titres ne bougent pas.
4. Écart variable : les repères sont faux, refaire l'alignement.
5. Refaire la mesure à chaque changement de voix, et remettre `avance_s` à 0 pour une voix enregistrée.

Le fichier attendu par le kit est `voix/mots.json` : `[{"text": "…", "start": 0.12, "end": 0.31, "line": 0}, …]` (secondes ; `line` = numéro de la réplique).

**Recaler les coupes.** Chaque coupe de `plans.md` se place sur le début du mot qui ouvre l'idée du plan. Mettre à jour les numéros d'image de la liste de plans et des temps clés **avant** de rendre.

**Sous-titres** (skill `rendu`) :

- **1 à 2 mots à l'écran à la fois**, changement exactement sur le début de chaque mot ;
- gras, blanc, contour sombre, centré, **dans la bande y = 1385 à 1515** (voir l'encadré ci-dessous) ;
- **une seule taille** (96 px) : un groupe trop long est coupé en deux, jamais rétréci ; un article se colle au mot plein qui suit si l'ensemble fait 10 lettres au plus ;
- **pas d'animation d'apparition sur chaque mot** : seulement sur les mots accentués ;
- les chiffres s'écrivent en chiffres ;
- jamais par-dessus le visage d'un personnage ou l'objet héros.

**La bande des sous-titres au mot : y = 1385 à 1515 (rendu réel du 11/11/2026).** Le repère général de HyperFrames et du skill `rendu` (bas du bloc entre y = 1220 et 1320, soit 600 à 700 px du bas) **tombe sur les sujets en plan taille** : d'abord placés à y = 1215, les sous-titres couvraient les personnages sur six plans, et c'est la critique qui l'a vu. Descendus à 1385–1515, ils passent sous les sujets.

Cohérence avec `skills/rendu/references/zones-interface.md`, vérifiée à la lecture :

- la bande est **dans la zone utile** (y de 160 à 1560, la seule limite que contrôle la porte de livraison) : son bas, 1515, reste 45 px au-dessus de la zone basse de l'application ;
- elle est **plus basse que le placement conseillé** par ce même fichier (sous-titres entre 1220 et 1320 ; texte indispensable de préférence au-dessus de 1330). C'est une dérogation voulue, que `sous-titres.md` autorise (« une fiche de style peut déplacer la zone […] en restant dans la zone utile ») ;
- ce qu'on accepte en échange : entre y = 1330 et 1560, la légende dépliée ou une publicité peut recouvrir le texte. Ici le sous-titre répète la voix, la perte est tolérable. **Pour une publicité**, garder le repère de `rendu` (au-dessus de y = 1250) et remonter les sujets d'autant ;
- la bande ne tient que si **le sujet reste dans les 65 % du haut** (étape 3). Les deux règles vont ensemble.

Le kit écrit ces sous-titres : `python outils/hf_build.py` (bande, taille et police dans `outils/reglages.py`). À savoir : `lint` signale `timeline_track_too_dense` (tous les sous-titres dans un fichier) et `check` peut signaler des contrastes faibles sur la couche du contour ; ce sont des avertissements, le rendu se fait.

## Étape 7 : le son

Skill `son`. Règles propres au format :

- la voix est toujours au-dessus ; la musique reste dessous ;
- **un bruitage seulement là où quelque chose de physique se passe** (un marteau frappe, une porte claque) ; **1 à 2 bruitages par 10 s** (voir ci-dessous) ;
- aucun « whoosh » répété plus de deux fois, et jamais un whoosh sur chaque coupe ;
- la musique **se résout sur la dernière image** ;
- vrais enregistrements d'abord, synthèse en repli ; niveau final −14 LUFS.

`sons.md`, dans les mêmes numéros d'image que l'image :

```
MARTEAU PART       image 1254   petit déclic de métal
COUP               image 1262   tintement de cloche, pic le plus fort ici
YEUX S'OUVRENT     image 1266   la musique s'efface pendant 20 images
DERNIÈRE PHRASE    image 1920   la musique se résout
```

**Budget de bruitages d'une histoire narrée : 1 à 2 par 10 s (rendu réel du 11/11/2026).** Le budget général du skill `son` (environ 5 par 10 s, plage 3 à 8) est calibré pour du motion design, où le son porte le mouvement. Ici la voix porte tout et les coupes sont muettes : le film réel compte 9 bruitages pour 61,5 s, soit 1,5 par 10 s, tous sur un événement physique, tous à moins de 100 ms de leur image (écart médian mesuré : 12 ms). Le script `budget.py` du skill `son` signalera « film calme » sous 3 par 10 s : c'est attendu, ce n'est pas un refus. Ce chiffre est mesuré, pas écouté : le faire juger à l'oreille par le client.

**Musique : la règle sur les instruments virtuels.** Entre « vrai enregistrement » et « synthèse » il y a un troisième cas : un instrument virtuel (banque d'échantillons d'un vrai instrument) joué par un musicien. Pour un instrument d'époque ou d'un pays, c'est souvent tout ce qui existe en licence libre (le rendu réel n'a trouvé aucun enregistrement acoustique libre de l'instrument voulu, après 45 minutes de recherche). Règle :

- **permis** si la licence du morceau est claire (CC0, CC BY ou licence commerciale écrite) et qu'elle couvre un usage monétisé ;
- **à créditer**, même en CC0 : titre, auteur, adresse de la page, licence, et la mention « instrument virtuel » dans `audio/CREDITS.md` ;
- ne jamais l'appeler « enregistrement d'époque » ni « instrument authentique » dans la description de la vidéo ;
- la synthèse pure (onde fabriquée par code) reste le dernier repli, comme pour les bruitages ;
- un bruitage de remplacement (des cailloux dans une tasse en métal à la place d'un tintement de cloche introuvable) se note de la même façon : ce que c'est vraiment, pas ce qu'il imite.

Avec le kit : décrire le mix dans `son/design.json` (modèle en tête de `outils/mix.py`), puis `python outils/mix.py`. Il pose l'attaque de chaque bruitage sur son image, fixe son niveau par rapport au fond de la seconde d'avant, fait plier la musique sous la voix et vise −14 LUFS. Constat du rendu réel : avec une voix de synthèse très régulière, la plage dynamique reste faible (2,2 LU).

Un son qui démarre en douceur décale son impact audible : repérer le pic sur la forme d'onde et décaler le fichier pour que **le pic** tombe sur l'image. Faire écouter le mix par l'outil d'écoute du skill `son` et le comparer à `plans.md`.

## Étape 8 : assembler

1. Rendre chaque plan en suite d'images (skill `blender`, `references/rendu-et-export.md`), l'encoder.
2. Monter les plans dans HyperFrames à leurs numéros d'image, ajouter sous-titres, voix, musique et bruitages (skill `rendu`).
3. Exporter dans `sortie/`.

Avec le kit (rendu réel du 11/11/2026) :

1. **Profiler avant de rendre** : `python outils/rendre.py --profiler` rend quelques images à pleine taille et annonce la durée du film. Lire le skill `blender`, `references/rendu-long-et-fiable.md` : c'est là que se gagne ou se perd une heure.
2. **Rendre** : `python outils/rendre.py`. La boucle saute les images déjà faites et repart seule après un plantage (neuf plantages du pilote graphique repris sans intervention sur le film réel). Un seul Blender à la fois. Arrêt : `python outils/rendre.py --arreter`.
3. **Assembler** : `python outils/hf_build.py` encode les images en un seul film muet et écrit le projet HyperFrames (film, sous-titres, voix, fond). Puis `lint`, `check`, `render` dans `hf/` (skill `rendu`).
4. **Régler le niveau final après le rendu** (skill `son`, `scripts/finaliser.py`) : le mixeur de HyperFrames ne rend pas exactement le niveau du mix (essai du kit : −15,1 LUFS en sortie pour −14,0 en entrée).
5. HyperFrames ne lit pas les repères de Blender : les bornes des plans passent par `outils/plans.py`.

## Étape 9 : la revue

On ne regarde jamais dix fois un export complet. On regarde des planches.

```bash
# planche contact : une image par seconde, tout l'épisode sur une image
ffmpeg -i sortie/episode.mp4 -vf "fps=1,scale=240:-1,tile=8x9" -frames:v 1 revue/contact.png

# test téléphone : comment ça se lit à 360 px de large
ffmpeg -i sortie/episode.mp4 -vf "fps=1/3,scale=360:-1,tile=6x4" -frames:v 1 revue/telephone.png
```

Avec le kit, une seule commande fait les deux planches, **trois images pleine taille par plan** (début, milieu, fin) et la consigne de critique : `python outils/revue.py sortie/episode.mp4 tour1`.

**Avant d'envoyer à la critique : vérifier que les images existent (rendu réel du 11/11/2026).** Au premier tour, le script d'extraction avait échoué en silence : le dossier des images pleine taille était **vide**, et le relecteur s'est rabattu sur les rendus bruts de Blender, sans sous-titres. Il a donc jugé un film que personne ne verra. Depuis :

- `revue.py` compte les fichiers attendus, refuse les fichiers vides, compare leur taille à celle de la vidéo, et sort en erreur avec « NE PAS ENVOYER À LA CRITIQUE » ;
- les images viennent **du MP4 final**, sous-titres compris, jamais du dossier `rendus/` ;
- le fabricant **ouvre lui-même une image pleine taille** avant d'envoyer la consigne ;
- la planche contact ne suffit pas : le tramage des aplats sombres et un sous-titre posé sur un visage ne se voient qu'en pleine taille.

**Critique.** Confier les deux planches à un relecteur qui **n'a pas fabriqué** la vidéo (le relecteur indépendant de `studio-coeur`), avec la consigne d'être le directeur d'animation le plus sévère. Questions :

- chaque personnage est-il posé au sol (ombre de contact) ?
- un personnage est-il éclairé comme un objet 3D ?
- un plan dure-t-il plus de 3 s sans idée nouvelle ?
- les sous-titres se lisent-ils à la taille d'un téléphone ?
- une affirmation à l'écran manque-t-elle dans `sources.md` ?
- un personnage bouge-t-il sans avoir regardé d'abord ? rebondit-il sans raison ?
- la caméra dérive-t-elle sans motif ?
- quelque chose d'important est-il dans une zone d'interface ?

**Les 9 questions du rendu réel du 11/11/2026.** Elles sont tirées des neuf corrections que deux tours de critique ont imposées à ce film (`revue.py` les écrit dans la consigne). La revue d'origine consigne des corrections, pas une liste de questions : cette formulation est celle du studio.

1. **L'action centrale se voit-elle ?** Le sujet est de face ou de profil franc, rien ne le cache, il est assez grand dans le cadre. (La preuve du film était filmée de dos ; une chute de nuit était minuscule.)
2. **Un double de l'objet héros contredit-il l'action ?** (Un exemplaire voisin, resté intact dans le cadre, faisait lire « rien n'est tombé ».)
3. **Quelque chose d'important est-il coupé par un bord ou dans une zone d'interface ?** Objet, personnage, bras tendu ; le sujet tient-il dans les 65 % du haut ? (Un bras pointé sortait du cadre.)
4. **Un personnage glisse-t-il au lieu de s'arrêter ?** (Une clé non tenue l'emmenait vers sa place du plan suivant.)
5. **Tout est-il posé et tenu ?** Ombre de contact, personnage plat, ce qui est tenu touche la main, rien ne flotte ni ne dépasse d'un meuble. (Un pinceau tenait debout à 40 cm de la main.)
6. **Le jeu se lit-il ?** Un regard avant chaque geste, les pupilles visent l'objet, aucun trait du dessin ne se lit à contresens de l'émotion. (Une barbe en arc se lisait comme un grand sourire.)
7. **Les sous-titres** couvrent-ils un visage, l'objet ou une action ? Ont-ils tous la même taille ? Se lisent-ils à 360 px ?
8. **L'image se lit-elle d'un coup d'œil ?** Profondeur en plusieurs couches, silhouette, ni blanc brûlé ni noir bouché, ni damier ni tramage, pas deux plans voisins au même cadrage. (Une seule colline pour dire un lointain de plusieurs centaines de kilomètres.)
9. **La correction du tour précédent a-t-elle cassé autre chose ?** (Après un recadrage, un personnage était coupé par le bord opposé.) On recontrôle toujours la version corrigée.

Le relecteur **liste chaque problème avec son numéro d'image**. Ordre de grandeur constaté : 31 points à la première critique ; 9 corrigés en deux tours ; 955 images re-rendues sur 1 845 ; une liste écrite de ce qui reste ouvert, classée du plus au moins gênant.

**Trois corrections par tour.** On corrige les 3 pires, on ne rend que les secondes concernées, on refait la planche, on recommence. Ordre de priorité :

1. ce qui est faux ou manquant ;
2. la lisibilité ;
3. le rythme ;
4. le détail visuel.

**Une correction s'écrit en 4 champs.** Un agent qui reçoit une correction bornée ne s'égare pas :

```
Corriger le PLAN 18 d'après plans.md.
OÙ           images 1248 à 1266
PROBLÈME     le marteau touche la cloche à 1268, 6 images après le son du coup (1262)
CHANGEMENT   seulement la course du marteau : départ 1254, contact 1262, accélération, pas de rebond
À GARDER     l'avancée de caméra, la coupe à 1266, les sous-titres, tous les autres plans

Rendre les images 1254, 1258, 1262, 1266 et un aperçu de 1215 à 1290.
Vérifier qu'il n'y a pas de saut entre les images. Dire ce qui a changé et où sont les fichiers.
```

| Champ | Contenu |
|---|---|
| **OÙ** | le plan et la plage d'images |
| **PROBLÈME** | ce qui ne va pas, avec les nombres observés |
| **CHANGEMENT** | la seule chose à modifier, avec les nouvelles valeurs |
| **À GARDER** | tout ce qui ne doit pas bouger |

Rendus partiels :

```bash
blender -b decors/decor2.blend -o //../rendus/controle_#### -F PNG -x 1 -f 1262
blender -b decors/decor2.blend -o //../rendus/plan18_#### -F PNG -x 1 -s 1215 -e 1290 -a
```

Avec le kit : corriger `outils/bl_film.py`, reconstruire la scène (`python outils/rendre.py --construire`), contrôler le plan corrigé à basse résolution (`python outils/rendre.py --controle images c_ 25 1254,1258,1262,1266`), puis **re-rendre par plages d'images** : `python outils/refaire.py tour1 1215-1289`. Les anciennes images sont déplacées dans `_a_supprimer/tour1/`, la boucle comble les trous, et le film se recolle tout seul puisque les fichiers gardent leurs noms. Re-rendre le plan entier que touche la correction, puis refaire l'assemblage et la revue. Sur carte graphique intégrée, compter 10 à 20 minutes par tour de correction.

**Regarder comme un spectateur**, une fois les planches propres : à vitesse normale, sur un téléphone, avec le son. Puis une fois les yeux fermés.

**Contrôle du fichier final :**

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=width,height,avg_frame_rate,duration -of json sortie/episode.mp4
```

On doit lire 1080, 1920, `30/1` et la durée prévue. Puis la porte de livraison de `studio-coeur`.

## Temps réels mesurés (rendu réel du 11/11/2026)

À donner au client **avant** de commencer. Un film de 61,5 s, 36 plans, sur un PC à carte graphique intégrée, par un agent qui connaissait la méthode mais partait d'un script et d'une voix déjà faits. Durée totale : 4 h 10 d'horloge.

| Étape | Temps | Remarque |
|---|---|---|
| Reprise : lecture de la méthode et du travail existant | 10 min | script, voix et recherche gardés d'une première session |
| 1. Histoire, sources, script | 15 min | trois recherches, tableau fait par fait |
| 2. Liste de plans | 15 min | écrite comme données, lue par Blender |
| 3. Objet héros | 15 min | deux versions, planche 6 angles |
| 3. Décors, 3 passes | 45 min | passe 1 refaite une fois, passe 3 en trois allers-retours |
| 4. Personnages | 10 min | 61 pièces, planche d'expressions |
| 5. Jeu et animation | 30 min | écrit plan par plan |
| Réglage du rendu et incidents | 40 min | profilage, plantages du pilote, boucle de rendu fantôme |
| **Rendu complet** | **1 h 50 de machine** | 3,6 s par image, 9 plantages repris automatiquement |
| 6. Voix, horodatage, sous-titres | 20 min | voix déjà faite ; contrôle de l'écart |
| 7. Son | 45 min de recherche + 15 min | 41 prises libres écoutées, mixage en deux essais |
| 8. Revue, deux tours | 1 h | dont 40 min de re-rendu |
| 9. Export, contrôles, documents | 15 min | |

Ce qu'il faut en retenir :

- plusieurs étapes se recouvrent (le son et les documents pendant le rendu) : **environ 2 h 30 de travail utile, le reste est de l'attente de rendu** ;
- le rendu est le poste le plus lourd et le moins prévisible : le profiler d'abord ;
- chaque tour de correction coûte 10 à 20 minutes de re-rendu sur carte intégrée ; une carte dédiée rendrait la revue confortable (estimation du compte rendu, non mesurée : cinq à dix fois plus rapide) ;
- ces temps n'incluent ni le choix de l'histoire avec le client, ni l'écriture du texte, ni l'enregistrement d'une vraie voix, ni les validations ;
- un premier épisode, sans kit ni décor réutilisable, prendra plus longtemps. Noter ses propres temps dès le premier.

## Ce qui a été essayé pour de vrai

Deux essais distincts, à ne pas confondre.

**Le film d'origine (11/11/2026)** : toute la chaîne, sur Windows, Blender 5.3, EEVEE sur carte graphique intégrée, connecteur MCP, HyperFrames. Contrôles du fichier final : 1080×1920, 30 i/s, 61,5 s, −14,1 LUFS, crête −2,0 dBTP. Le compte rendu de ce film dit lui-même ce qui n'est pas au niveau d'une vidéo publiable (voir le `SKILL.md` de la catégorie).

**Le kit générique (même jour)**, sur une machine Linux **sans carte graphique**, avec le module Python `bpy` 5.3 et l'exemple neutre de 2 plans :

| Essayé, et le résultat | |
|---|---|
| `plans.py`, `personnages.py` | plans vérifiés, 15 pièces dessinées, planches écrites |
| `bl_film.py` en passes 1, 2 et 3 | scène construite et enregistrée ; cadres « ok », 0 glissement |
| Rendus de contrôle et planches (`bl_cli.py`, `planche.py`) | une image par plan, images choisies, objet héros sous 6 angles |
| Boucle de rendu (`rendre.py`) en Cycles sur processeur, à 25 % de la taille | deux rendus complets de 90 images : le premier avec **4 arrêts brutaux simulés** (toutes les 20 images), le second avec 2 (toutes les 35) ; autant de reprises, 0 image manquante, aucune refaite ; 4,3 s par image à cette taille |
| Verrou et arrêt | une deuxième boucle est refusée ; `--arreter` arrête la boucle puis son Blender ; aucun processus restant |
| `refaire.py` | 8 images déplacées dans `_a_supprimer/`, re-rendues, les autres intactes |
| `--profiler` à pleine taille | 65 s par image en Cycles sur 2 cœurs : inutilisable pour un film, ce que le profilage sert justement à dire |
| Une image en EEVEE, rendu logiciel sans carte | l'image sort (35 s à 25 %) : les réglages EEVEE du kit sont acceptés par Blender 5.3 |
| Contrôle de glissement, chute réelle | une clé non tenue est signalée ; 30 cm = 8 images, 76 cm = 12 images |
| `ecart_voix.py` sur un signal d'essai décalé de 107 ms | mesure 105 ms (pas de 5 ms), dispersion 3 ms |
| `mix.py` sur des signaux d'essai | −14,0 LUFS ; attaque du bruitage à l'image 56,2 pour 56 demandée |
| `hf_build.py`, puis HyperFrames 0.9.33 | `lint` 0 erreur (1 avertissement attendu : tous les sous-titres dans un fichier), `check` bon (3 avertissements de contraste sur la couche du contour), `render` : MP4 de 3,000 s, 1080×1920, 30 i/s, 90 images, avec piste son |
| Niveau du MP4 final | **−15,1 LUFS** mesurés après le rendu HyperFrames, pour −14,0 en sortie de `mix.py` (film d'essai de 3 s, signaux d'essai) : le niveau final se règle après le rendu, avec `skills/son/scripts/finaliser.py` |
| `revue.py` sur ce MP4 | 2 planches, 6 images pleine taille avec sous-titres, vérifiées ; avec une extraction volontairement cassée, le script sort en erreur (« NE PAS ENVOYER À LA CRITIQUE ») |
| Seconde vue d'un personnage (mécanique) | un double du personnage déclaré comme autre vue, avec ses propres visages, monté en miroir et échangé à une coupe : fonctionne. Aucun profil n'a été dessiné |

**Pas essayé** avec le kit générique, donc à vérifier au premier usage : le programme `blender` en ligne de commande (seul le module `bpy` était disponible ; les deux voies passent par la même fonction, mais une seule a tourné), le connecteur MCP, Windows et macOS (recherche de Blender, contrôle du processus par `tasklist`, chemins avec espaces), EEVEE sur une vraie carte graphique avec les réglages du profil `integree` à pleine taille, la brume volumétrique, un film de plus de 2 plans, un mix avec de vrais enregistrements, une vraie voix. L'exemple a été rendu à un quart de la taille puis agrandi pour essayer l'assemblage : il n'est pas livrable.

## Rester du bon côté des plateformes

- **Prendre la grammaire, jamais le contenu.** On étudie comment une chaîne cadre, coupe et sous-titre ; on ne copie ni ses personnages, ni ses dessins, ni ses textes, ni la structure d'un de ses épisodes.
- **Et pas la grammaire reconnaissable d'une seule chaîne.** Mélanger des décors éclairés et des personnages plats est une technique ; le dessin d'un bonhomme précis, ses sujets, son ton et sa façon de sous-titrer, pris ensemble, sont l'identité de quelqu'un. Le client choisit ses propres sujets et un dessin de personnage original (voir le `SKILL.md` de la catégorie, « Mise en garde »).
- **Des épisodes originaux, pas un moule.** Les plateformes visent le contenu produit en masse et répétitif. Une vraie histoire, la voix du client et des décors nouveaux protègent la chaîne.
- **Étiquette « contenu généré ».** Elle concerne surtout le contenu réaliste modifié ; une animation clairement irréaliste en est en général dispensée. Si une image peut être prise pour une vraie prise de vue, l'étiqueter. Le client vérifie la règle en vigueur sur sa plateforme.
- **Les faits restent des faits.** `sources.md` n'est pas de la paperasse.

## Analyser une référence (facultatif)

Quand le client apporte une vidéo dont il aime le format, on l'analyse **comme un format, pas comme un contenu à copier** :

```bash
ffmpeg -i reference.mp4 -vf "fps=2,scale=540:-2" images/ref-%04d.jpg
```

Écrire `REFERENCE.md` : chaque coupe (temps et image), ce qui est 2D et ce qui est 3D dans chaque plan, le mouvement de caméra et son sens, le style des sous-titres (mots par carton, position, moment du changement), la phrase d'accroche et l'endroit du retournement.

Étiqueter **chaque valeur** : `MESURÉ` (lu sur une image), `ESTIMÉ` (à l'œil) ou `DÉCISION` (notre choix pour notre version). Pour ce qui est incertain, nommer les images à vérifier. Terminer par 5 décisions pour notre propre épisode original.

## Après la mise en ligne

- Noter les heures passées par étape (histoire, décors, personnages, animation, voix, son, revue) : le deuxième épisode dira ce que le premier a vraiment coûté.
- Lire la courbe de rétention : elle montre la seconde exacte où les gens partent. Corriger ce type de plan dans l'épisode suivant.
- Faire un épisode de bout en bout avant de planifier une chaîne.
