# Les contrôles : porte de livraison, planches, tours de correction, note

Ordre : porte de livraison → planches regardées → visionnage à vitesse réelle → relecteur indépendant → 3 corrections → on recommence → note de livraison.

Une porte verte ne dit pas que la vidéo est bonne. Elle dit qu'elle n'a pas les défauts qu'une machine sait mesurer. Le reste se regarde.

## 1. La porte de livraison

```
PYTHONDONTWRITEBYTECODE=1 python3 scripts/porte_livraison.py renders/final-livre.mp4 \
  --fiche <chemin de la fiche STYLE.md du style> --textes textes.json --json revue/porte.json
```

**Quel fichier ?** Le MP4 **livré** (`*-livre.mp4`, produit par `skills/son/scripts/finaliser.py`), pas le rendu brut : c'est lui qui a le bon niveau sonore, et c'est lui que le client reçoit.

**`--fiche`** fait lire à la porte le bloc « Réglages des contrôles » qui termine la section 8 de la fiche du style (mouvement calme / normal / vif, dérogation bleu-violet, texte vivant, taille mini du texte). Sans l'option : mouvement normal, bleu-violet interdit, texte vivant non, 50 px. Passe-la toujours : `lint_storyboard.py`, `relever_textes.py` et `controle_textes.py` la prennent aussi. `python3 scripts/fiche_reglages.py <fiche>` montre ce qui sera lu.

| Contrôle | Rouge | Jaune | Comment c'est mesuré |
|---|---|---|---|
| Diaporama | temps vivant sous 20 % (calme : 10 % ; vif : 35 %) | sous 35 % (calme : 20 % ; vif : 50 %) | part du temps où quelque chose bouge **dans** les plans : voir ci-dessous |
| Clignotement | plus de 3 changements brusques par seconde sur 25 % de l'image ou plus | exactement 3, ou plus de 3 sur 10 à 25 % de l'image | 30 images/s, grille 18 × 32 ; saut de luminance de 25 niveaux ou de couleur de 45 ; un éclair (aller-retour ≤ 0,12 s) compte pour un |
| Écran vide | 0,3 s ou plus | | image presque sans contour (moins de 0,2 % de pixels avec un bord), hors première et dernière demi-seconde |
| Bleu-violet « look IA » | 30 % du film ou plus | 12 % ou plus | pixels de teinte 225–300°, saturation ≥ 0,30 ; une image en a 30 % ou plus = image bleu-violet. Le bleu marine en aplat (≈ 210°) passe |
| Texte hors zone sûre | un texte dépasse | | relevé `textes.json` contre la zone sûre |
| Temps de lecture | un texte trop bref | | relevé `textes.json` |
| Volume | verdict rouge de `son/scripts/niveau.py` | son verdict jaune (film sans voix ni musique, `--sans-fond`) | la porte appelle `niveau.py mesurer --json` : `ffmpeg -af ebur128=peak=true`, bloc « Summary » |
| Texte trop petit | | sous la taille mini de la fiche (50 px sans fiche) | relevé `textes.json` |
| Image figée | | plus de 3 s | seule la tenue finale peut être immobile |
| Format, cadence, film court | | différent de 1080×1920 ou de 30 i/s ; 12 s ou moins | information |

Codes de sortie : 0 (vert ou jaune), 2 (rouge), 1 (film illisible ou outil manquant).

### Ce que mesure « diaporama »

La question posée est : **est-ce une suite d'images fixes ?** La porte lit 12 images par seconde à 180 px de large (bas de l'image masqué), et entre deux images voisines :

1. elle compte la **part de pixels qui changent** (plus de 6 niveaux sur 255 après un léger flou ; si l'image a du grain, 4 fois ce grain) : un grain qui grouille ne compte pas ;
2. elle retire ce qu'explique un **mouvement d'ensemble** (glissé, zoom, rotation, lumière qui monte ou descend partout) : une poussée de caméra sur une image fixe n'est pas une action ;
3. si au moins 0,2 % des pixels changent encore, cet instant est **vivant**.

Le chiffre jugé est la **part du temps vivant à l'intérieur des plans**. Ne comptent pas dans ce temps : les coupes franches, et les passages d'une image fixe à une autre (fondu, volet, glissé de 1,5 s au plus, immobile avant et après, plus de 30 % de l'image changée). Un éclair, une secousse, un changement de couleur ne sont pas des coupes.

Le chiffre ne dépend ni du contraste ni de la surface : un trait fin qui se dessine sur du blanc vaut autant qu'un aplat qui traverse l'écran. L'ancienne mesure (différence moyenne de toute l'image) refusait à tort les styles à plat.

Repères mesurés (novembre 2026) : les 12 films d'essai du studio vont de 31 % à 97 % (avec leur fiche : aucun rouge, aucun jaune) ; 7 diaporamas fabriqués pour l'essai (images fixes en coupes franches, en fondus, avec grain animé, avec zoom lent façon Ken Burns sur une ou plusieurs photos, avec ou sans fondus) sortent entre 0 % et 5 %, rouge ; un fond fixe avec quatre textes qui arrivent en fondu sort à 15 % (rouge en « normal » pour un film de plus de 12 s, jaune pour ce film d'essai de 10 s ; jaune en « calme »).

**Mouvement : calme** (fiche du style) abaisse les seuils, sans jamais les supprimer : un style à plans fixes doit quand même vivre un dixième du temps.

### Lire le résultat

**Diaporama rouge.** La vidéo change d'image mais rien ne bouge dedans. Ne règle pas ça en ajoutant une poussée de caméra à chaque plan (la porte la retire du compte) : donne à chaque plan **une action** (quelque chose tombe, se plie, grandit, se transforme), fais vivre le fond, remplace un fondu par une transformation. Si le message dit « l'image entière bouge X % du temps mais rien ne bouge dedans », c'est exactement ce cas. Film de plus de 10 s : regarde la « pire fenêtre de 10 s », c'est là que la vidéo meurt.

**Clignotement rouge.** Espace les éclairs et les changements de couleur (3 par seconde au plus), ou réduis leur surface sous un quart de l'image. C'est une règle de sécurité (personnes photosensibles), pas de goût : elle ne se discute pas avec le client.

**Écran vide rouge.** Le héros ou l'objet a quitté l'image (noir entre deux scènes, flash blanc, plan de respiration vide). Garde-le à l'écran : pour respirer, il s'arrête, la caméra recule, ou elle glisse vers l'objet suivant.

**Bleu-violet rouge.** Change la palette (celles de la fiche « ma chaîne », ou les palettes du style). Si la fiche du style porte « Bleu-violet : dérogation », le rouge devient jaune tout seul avec `--fiche`. Si c'est le client qui a demandé cette couleur : `--autoriser-bleu-violet "sa raison"`, recopiée dans la note de livraison. N'utilise jamais cette option de ta propre initiative.

**Volume rouge.** Passe le rendu par `skills/son/scripts/finaliser.py` et contrôle le fichier livré. Film sans voix ni musique : `--sans-fond` (à la porte comme à `finaliser.py`) ; la cible −14 LUFS ne s'applique plus, le feu est jaune si la règle « sans fond » du skill `son` est tenue, et tu l'écris dans la note. La porte, `niveau.py` et `rendu/scripts/verifier-export.py` mesurent de la même façon (`ebur128=peak=true`) : s'ils ne donnent pas le même chiffre au dixième, c'est qu'ils ne lisent pas le même fichier.

**Jaune.** Va voir le passage, puis écris dans la note pourquoi c'est acceptable. Un jaune non regardé est un défaut.

**Film de 12 s ou moins.** Un rouge « diaporama » proche du seuil (au-dessus de sa moitié) devient jaune : il y a peu d'images pour juger. Un film court franchement fixe reste rouge.

### Limites connues (à dire si on te le demande)

Ce que la mesure « diaporama » distingue : une suite d'images fixes (coupes, fondus, volets), même avec du grain, même avec un zoom ou un glissé lent sur chaque image ; un film où des choses bougent, même petites et peu contrastées.

Ce qu'elle ne distingue pas :
- **une image fixe avec une boucle de fond** (une lueur qui pulse, des particules) : ça bouge tout le temps, la porte dit vert. C'est la planche contact (cases voisines identiques) et le relecteur qui l'attrapent ;
- **un mouvement utile d'un mouvement décoratif** : elle sait que ça bouge, pas que ça raconte ;
- **une caméra en parallaxe sur des calques fixes** : les calques ne bougent pas tous pareil, donc ce n'est pas un mouvement d'ensemble : compté comme vivant ;
- **un zoom ou un glissé très rapide** (plus de 2 px par douzième de seconde à 180 px, soit environ 150 px/s sur l'image finale) ou une déformation (perspective, bascule 3D) sur une image fixe : le recalage décroche, c'est compté comme vivant ;
- **un mouvement très lent pendant un mouvement de caméra** (moins de 25 px/s environ) : confondu avec le recalage, non compté ;
- **des tableaux fixes reliés par de grandes transformations courtes** : une transformation de 1,5 s au plus qui change plus de 30 % de l'image entre deux tenues est prise pour un passage et n'est pas comptée ; un film fait seulement de cela sort bas, à tort ou à raison (c'est un diaporama à belles transitions).
- Les seuils (20 % / 35 %, etc.) sont calés sur 12 films et 7 diaporamas : c'est peu. Ils sont à recaler quand le studio aura plus de films jugés.

Clignotement : un balayage très rapide sur un motif très contrasté (mire de test) peut être compté ; à l'inverse un clignotement sur moins de 10 % de l'image n'est pas signalé. Le seuil de couleur (45) est un choix du studio, pas une norme : la norme d'accessibilité (WCAG 2.3.1) parle de luminance et de rouge saturé.

Écran vide et bleu-violet : seuils du projet huashu-art-motion, calés par son auteur sur ses propres films (88 pour la couleur).

La porte ne voit pas : un rythme qui s'essouffle, une vidéo qui bouge sans rien raconter, un cadre de page fixe, une image laide.

## 2. Le relevé des textes

La zone sûre et le temps de lecture se contrôlent à partir d'un relevé `textes.json` : pour chaque texte, ce qu'il dit, quand il est entier et lisible, et où sont ses lettres.

### Film en HTML : `relever_textes.py`

```
PYTHONDONTWRITEBYTECODE=1 python3 scripts/relever_textes.py <dossier du projet HyperFrames> \
  -o textes.json --fiche <fiche STYLE.md>
PYTHONDONTWRITEBYTECODE=1 python3 scripts/controle_textes.py textes.json --fiche <fiche STYLE.md>
```

Rien à charger dans la page, pas de fonction à écrire : l'outil lance l'aperçu de HyperFrames, ouvre le film dans un navigateur sans fenêtre (Playwright), le place à chaque quinzième de seconde avec le moteur du rendu (`__player.renderSeek(t)`), mesure, arrête l'aperçu et écrit `textes.json`. Compter 15 à 30 s pour un film de 10 s. Besoin : `pip install playwright` ; le Chrome utilisé est celui de Playwright ou, à défaut, celui que HyperFrames a déjà téléchargé.

Dans le film, marque chaque texte :

| Attribut | Pour |
|---|---|
| `data-texte="accroche"` | tout texte à contrôler (l'identifiant est libre) |
| `data-sous-titre` | un sous-titre calé sur la voix (ses mots arrivent un à un : il compte dès le premier) |
| `data-passage` | un texte de décor que le spectateur n'a pas à lire. Jamais pour un texte dont la vidéo a besoin |
| `data-texte-vivant` | un texte qui tremble ou flotte par style (onomatopée, carton de film muet) |

Sans aucun `data-texte` (ou avec `--auto`), l'outil relève tous les blocs de texte et les nomme `auto-1`, `auto-2`… : utile pour un premier passage, à relire.

Ce que l'outil sait faire, et qui manquait à l'ancien `releve_textes.js` :

- **`SplitText`** : chaque ligne, mot ou lettre est mesuré à part ; le texte n'est « entier » que quand tous ses morceaux sont arrivés.
- **Masques** : un morceau coupé par un parent `overflow: hidden / clip` (dont `mask: "lines"` de `SplitText`) ou par `clip-path: inset(...)` n'est pas visible. Les autres `clip-path` et les `mask-image` ne sont pas calculés : le texte porte alors `"masque_non_calcule": true`, vérifie ses temps sur une bande d'images.
- **Glyphes** : la boîte relevée est celle des lettres, pas celle de l'élément (marges et fond exclus). La taille est la taille de police multipliée par l'échelle de l'élément.
- **Toutes les présences** : un texte qui part et revient, ou que la caméra déplace, donne plusieurs entrées du même `id`. Le contrôle juge la zone sûre sur chacune et le temps de lecture sur la plus longue.
- **Caméra qui dérive** : un texte reste « posé » tant qu'il ne va pas plus vite que 60 px/s (`--vitesse`). Sa boîte contient toutes ses positions ; `derive_px` dit de combien il a bougé.
- **Texte vivant** (`data-texte-vivant`, `--vivant`, ou fiche « Texte vivant : oui ») : il peut trembler dans un rayon de 24 px (`--tolerance-vivant`) et son opacité descendre à 0,6. Sans cela, un carton qui scintille n'est jamais « posé » et sort avec une tenue fausse.
- **Compteur qui défile** : chaque valeur est un texte différent ; seule la valeur tenue est gardée.
- **Même résultat d'une fois sur l'autre** : polices chargées avant de mesurer, premier passage à blanc, mesure répétée jusqu'à être stable (vérifié : 6 relevés de suite identiques au bit près sur un film à sous-compositions).

Si l'outil imprime « texte(s) vus mais jamais posés », le texte bouge tout le temps : soit c'est un défaut (personne ne peut le lire), soit c'est un texte vivant non déclaré.

Mode de repli `--mode direct` (sans serveur d'aperçu) : ouvre `index.html` en fichier, avance les timelines de `window.__timelines` par `seek(t, false)` (avec `false` : sinon les `onUpdate`, donc les compteurs, ne tournent pas), cache les `.clip` hors de leur plage, envoie l'évènement `hf-seek`. Il ne charge pas les sous-compositions (`data-composition-src`) : à réserver aux films d'un seul fichier.

### Film dessiné dans un canvas

Le navigateur ne sait pas lire un texte peint dans un `<canvas>` (pixel art, cartoon tracé, Three.js) : `relever_textes.py` le signale (`"canvas_sans_texte_declare": true`, jaune à la porte) et il faut lui donner les textes. Deux voies :

1. **Le film déclare ses textes** (le mieux quand le code connaît leurs positions) :
   ```js
   window.__textes = (t) => [
     { id: "accroche", texte: "3 € PAR JOUR", x0: 96, y0: 320, x1: 576, y1: 376, taille_px: 78, opacite: 1 },
   ];   // seulement les textes visibles à l'instant t, boîtes en pixels de l'image finale
   ```
   `relever_textes.py` appelle cette fonction à chaque pas et suit ces textes comme les autres (champs facultatifs : `sous_titre`, `passage`, `vivant`). Le canvas avance par l'évènement `hf-seek` : voir « Film en canvas piloté par `hf-seek` » dans `skills/rendu/SKILL.md`.
2. **À la main** : copie `gabarits/textes-canvas.json` en `textes.json` et remplis-le. Le mode d'emploi est dans le fichier : une entrée par texte ; `debut` et `fin` lus dans le code (fin de l'animation d'entrée, début de la sortie) ; boîte des lettres en pixels de l'image finale (pixel art : case × taille d'une case) ; `taille_px` ≈ hauteur d'une majuscule × 1,4. Vérifie chaque boîte sur une bande d'images (`planche_contact.py --bande`), et écris dans la note de livraison que le relevé est fait à la main.

### Règles appliquées par `controle_textes.py`

| Règle | Valeur |
|---|---|
| Zone sûre, vertical 1080×1920 | rien dans les 160 px du haut, 360 px du bas, 135 px de droite, 60 px de gauche (table de référence : `rendu/references/zones-interface.md`) |
| Zone sûre, autres formats | marge de 5 % |
| Temps de lecture, vidéo courte (par défaut) | 1 s + 0,25 s par mot au-delà de 3 ; 2 s au moins pour le dernier texte |
| Temps de lecture, explicatif posé (`--strict`) | caractères ÷ 15 + 1,5 s, jamais moins de 1,5 s |
| Texte vivant de 1 ou 2 mots | 0,8 s suffisent ; au-delà de 2 mots, la règle normale, sans rabais |
| Sous-titres calés sur la voix (`"sous_titre": true`) | 0,7 s au moins, 17 caractères par seconde au plus |
| Taille | sous la « Taille mini du texte » de la fiche (50 px sans `--fiche`), pour 1080 de large : jaune |
| Texte de décor (`"passage": true`) | listé, pas jugé |

Sans relevé, la porte marque zone sûre et temps de lecture « NON CONTRÔLÉ ». Ce n'est pas un succès : la note de livraison le dira. Une vidéo sans aucun texte : écris-le dans « Non vérifié ».

Dans le doute, tiens le texte plus longtemps et anime moins.

## 3. Les planches : à regarder, pas seulement à produire

```
PYTHONDONTWRITEBYTECODE=1 python3 scripts/planche_contact.py renders/final-livre.mp4 revue/ --bande 3.2 --bande 12.4
```

**`planche.jpg`, une image par seconde.** La case n° k (ligne par ligne, à partir de 0) est l'image du film à k secondes pile ; son temps est écrit dans son coin. Cherche :
- deux cases voisines presque identiques (temps mort) ;
- toutes les cases au même cadrage (diaporama) ;
- un sujet trop petit, collé au bord, trop sombre, ou une couleur posée sur la même couleur ;
- une case vide ou presque ;
- la première case : est-ce une vraie image (c'est souvent la miniature) ?
- l'histoire se comprend-elle en lisant la planche seule ?

**`telephone.jpg`, à 360 px de large : le test téléphone.** C'est la taille réelle chez le spectateur. Chaque texte utile se lit ; chaque expression de personnage se comprend ; le héros se repère en un coup d'œil. Ce qui ne passe pas ici ne passe pas.

**`bande-<t>.jpg`, 12 images serrées autour d'un instant** (une tous les 1/15 s, de t − 0,4 s à t + 0,33 s, temps écrit en centièmes de seconde sur chaque image). `--bande` se répète : une par transition et par mouvement rapide. Cherche : textes qui se chevauchent pendant l'échange, image blanche isolée, saut, objet qui se téléporte, pose qui change sans passage. La planche ne montre pas la fin du film après la dernière seconde entière : ajoute une bande sur la dernière seconde.

**Puis un visionnage complet à vitesse réelle, avec le son.** Si tu ne peux pas voir ou entendre la vidéo, écris-le dans « Non vérifié » de la note.

## 4. Les corrections : trois par tour, trois tours

1. Avec ta revue et celle du relecteur, écris **les 3 pires défauts**, chacun avec son moment (« 12,4 s : le texte sort avant qu'on l'ait lu »).
2. Corrige ces trois-là. Pas dix : trois vraies corrections valent mieux que dix retouches, et tu ne casses pas ce qui marchait.
3. Re-rends seulement les secondes touchées, puis la vidéo entière une fois à la fin du tour.
4. Relance la porte et les planches, **regarde** le résultat, refais relire.
5. Ne touche pas aux plans notés 9 ou plus.

Après **trois tours**, si une note reste sous 8 : arrête. Dis au client quel défaut résiste et propose deux issues (reprendre le plan au storyboard, ou livrer en le sachant). S'il accepte de recevoir la vidéo ainsi, passe `--accord-client "…"` à la note : sa décision y est recopiée.

Une note prise comme un symptôme : « rends ça plus dynamique » peut vouloir dire un plan trop long, un fond mort ou un son absent. Trouve la cause avant de changer quoi que ce soit.

## 5. La note de livraison

```
PYTHONDONTWRITEBYTECODE=1 python3 scripts/note_livraison.py renders/final-livre.mp4 --porte revue/porte.json --relecture relecture/tour-2.md \
  --plan-faible "Plan 6 (14–17 s) : la carte reste presque immobile" \
  --corrige "texte du plan 3 tenu 0,8 s de plus ; fond du plan 5 animé" \
  --non-verifie "je n'ai pas pu écouter le mix" --tour 2
```

- Les **faits** (format, porte, notes du relecteur, plan le plus faible) sont écrits par le script et portent une empreinte. `--verifier` détecte une modification après coup. Tu ne les réécris pas.
- Le script **refuse** d'écrire la note si : porte rouge ou absente ; pas de relecture ; un critère sans note ; une note sous 8 sans accord du client ; plan le plus faible non nommé.
- **Le plan le plus faible est toujours nommé.** Toute vidéo en a un. Le dire au client lui donne le premier endroit à regarder et montre que tu as jugé ton travail.
- Tu complètes « Notes du réalisateur » : ce qu'est la vidéo, pourquoi chaque jaune est acceptable, les deux directions de look écartées, ce que tu changerais avec un tour de plus.

Avec la vidéo, le client reçoit aussi la liste des éléments tiers utilisés (sons, polices, images, musique) avec source et licence, et le rappel qu'il est responsable des éléments qu'il a fournis.

La mesure « diaporama » (part de pixels, part du temps, retrait du mouvement d'ensemble), le clignotement et `relever_textes.py` sont écrits pour ce plugin.

Sources : `film_gate.py`, `deliver.py` et le protocole de relecture de huashu-art-motion (alchaincyf, MIT) ; `readcheck.mjs` et DIRECTOR.md §10–§11 de lemo-opuscar (LemoLab, MIT) ; boucle de critique de claude-motion-design (Howseen AI, MIT) ; revue d'animate (cth9191, MIT) ; règle de tenue de lecture de claude-motion (whaleyxbt, MIT). Réécrit.
