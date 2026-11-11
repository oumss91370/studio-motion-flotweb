# Les 31 émotions jouées

Source : table des émotions du kit ClaudeAnimationBase de John Heibel (MIT), fichier `src/clawd.js` et `ANIMATION_GUIDE.md`. Les descriptions ci-dessous traduisent cette table (yeux, bouche, teinte, marque, mouvement du corps, taille de la réaction) pour **n'importe quel personnage du client**. Le personnage du kit d'origine n'est pas repris.

## Comment lire une émotion

Une émotion, c'est cinq choses à la fois :

| Élément | Rôle |
|---|---|
| **Yeux** et **bouche** | pris dans la planche d'expressions |
| **Teinte ou accessoire** | une couleur qui glisse sur le visage (pâle, rouge, bleu, rosé, vert, doré), des joues rouges, un front assombri |
| **Marque** | un petit dessin près de la tête : `!`, `?`, zzz, goutte, étincelle, cœurs, veine de colère, vapeur, ampoule, points de suspension, notes, étoiles, nuage |
| **Corps** | une manière de se tenir et de bouger |
| **Réaction** | la taille du sursaut quand on **entre** dans l'émotion : de 0,2 (à peine) à 1,3 (très fort) |

**Deux niveaux d'intensité du corps :**

- **Jeu sobre** (défaut pour la 2.5D « histoire vraie » et tout style réaliste dans le ton) : on garde les yeux, la bouche, la pose et **une** réaction à l'entrée ; au repos, seulement la respiration. Pas de rebond en boucle.
- **Jeu cartoon** (catégorie `styles-cartoon`, mascottes, vidéos musicales) : le mouvement de fond décrit ci-dessous tourne en continu, calé sur le tempo. Sans musique à tempo net, revenir au jeu sobre.

## Joie (9)

| Émotion | Yeux | Bouche | Teinte / marque | Corps | Réaction |
|---|---|---|---|---|---|
| **Joyeux** | en arc, souriants | sourire | joues un peu roses | léger rebond sur chaque temps, bras qui se balancent en alternance | 0,6 |
| **Excité** | grands | ouverte | étincelles | petits sauts deux fois par temps, bras levés qui s'agitent | 1,0 |
| **Rire** | plissés fermés | rire, grande ouverte | joues roses | secousses rapides (5 par seconde), buste un peu en arrière, bras serrés contre soi | 0,8 |
| **Amoureux** | en cœur | petit sourire « en w » | joues très rouges, teinte rosée, cœurs | balancement latéral lent, penche d'un côté puis de l'autre | 0,7 |
| **Fier** | fermés | sourire | teinte dorée, étincelle | étiré vers le haut, torse bombé, mains sur les hanches, presque immobile | 0,5 |
| **Émerveillé** | pleins d'étoiles | ouverte | teinte dorée | petits sauts, les deux bras levés ensemble | 1,0 |
| **Taquin** | clin d'œil | langue tirée | aucune | saute d'un côté à l'autre à chaque temps en se penchant | 0,6 |
| **Plein d'espoir** | brillants | petit sourire « en w » | joues un peu roses | étiré, regard vers le haut, bras à demi levés, oscillation lente | 0,5 |
| **Soulagé** | fermés | sourire | goutte de sueur | longue expiration : le corps s'affaisse et remonte lentement, bras qui retombent | 0,4 |

## Malice (4)

| Émotion | Yeux | Bouche | Teinte / marque | Corps | Réaction |
|---|---|---|---|---|---|
| **Suffisant** | mi-clos | sourire en coin | aucune | regard de côté, penché, une main sur la hanche, l'autre levée | 0,4 |
| **Décontracté** | lunettes noires | sourire en coin | notes de musique | hoche sur le temps, un bras levé, l'autre le long du corps | 0,4 |
| **Espiègle** | mi-clos | large sourire | front assombri | tassé, légèrement penché, mains qui se frottent (4 fois par seconde) | 0,5 |
| **Méfiant** | mi-clos | plate | aucune | le regard balaie lentement de gauche à droite, le corps suit en glissant | 0,4 |

## Bas (5)

| Émotion | Yeux | Bouche | Teinte / marque | Corps | Réaction |
|---|---|---|---|---|---|
| **Triste** | tombants | moue | teinte bleue, front assombri, petit nuage | tassé, bras pendants, regard vers le bas, balancement très lent | 0,3 |
| **En pleurs** | en larmes | grande ouverte, plainte | teinte bleutée | sanglots : un sursaut à chaque temps qui s'amortit, bras levés qui tremblent | 0,8 |
| **Ennuyé** | mi-clos | plate | aucune | soupir : gonfle puis retombe sur quatre temps, regard bas et de côté, bras pendants | 0,2 |
| **Endormi** | lourds, presque fermés | petit rond | zzz | respiration très lente, dodeline | 0,2 |
| **K.-O.** | en croix | tremblante | pâle, étoiles | écrasé, de travers, bras tombés, ne bouge presque plus | 1,0 |

## Chaud (4)

| Émotion | Yeux | Bouche | Teinte / marque | Corps | Réaction |
|---|---|---|---|---|---|
| **En colère** | sourcils froncés | dents serrées | teinte rouge, veine de colère | tremblement latéral rapide, s'écrase sur chaque temps | 0,8 |
| **Furieux** | rouges | grande ouverte, cri | très rouge, vapeur | tremblement fort, tape du pied, bras levés qui battent | 1,2 |
| **Déterminé** | sourcils droits, regard fixe | plate | aucune | penché en avant, poings qui montent en alternance | 0,7 |
| **Dégoûté** | plissés fermés | tremblante | teinte verte | recule en se penchant, frisson bref qui s'amortit | 0,8 |

## Alerte (5)

| Émotion | Yeux | Bouche | Teinte / marque | Corps | Réaction |
|---|---|---|---|---|---|
| **Effrayé** | écarquillés, pupille minuscule | tremblante | pâle, goutte de sueur | tremblement très rapide, étiré, bras levés, le regard saute d'un côté à l'autre | 1,1 |
| **Nerveux** | regard fuyant | tremblante | un peu pâle, goutte de sueur | le regard change de côté à chaque temps, se dandine, mains qui s'agitent | 0,5 |
| **Surpris** | grands | en O | `!` qui s'efface | étiré d'un coup, décollé du sol, bras levés | 1,3 |
| **Perplexe** | un œil plissé, un œil grand | tremblante | `?` | la tête penche lentement d'un côté à l'autre, une main se gratte la tête | 0,6 |
| **Étourdi** | en spirale | tremblante | étoiles | tangue en cercle, bras désordonnés | 0,7 |

## Esprit (4)

| Émotion | Yeux | Bouche | Teinte / marque | Corps | Réaction |
|---|---|---|---|---|---|
| **Neutre** | normaux | aucune ou fermée | aucune | respiration légère, bras presque immobiles | 0,3 |
| **Pensif** | regard en haut et de côté | plate | points de suspension | un peu penché, une main au menton, l'autre bras bat lentement | 0,4 |
| **Idée** | brillants | grand sourire | ampoule | sursaut vers le haut, un bras pointé en l'air | 1,1 |
| **Timide** | regard bas et de côté | tremblante | joues très rouges | tassé, penché, bras ramenés devant soi qui se tortillent | 0,3 |

## Changer d'émotion (ne jamais claquer)

Le kit d'origine ne remplace jamais un visage d'une image à l'autre. Autour de chaque changement, dans l'ordre (l'ordre vient du kit ; les nombres d'images sont des valeurs de départ du studio, à 30 i/s) :

1. **Anticipation** : les yeux se plissent et le corps s'écrase très légèrement, 2 à 4 images avant.
2. **Échange** du visage pendant que les yeux sont plissés (le changement est caché).
3. **Réaction** : un sursaut dont la taille est celle de la nouvelle émotion (colonne « Réaction »). 0,2 : à peine un frémissement ; 1,3 : tout le corps s'étire d'un coup.
4. **Stabilisation** : le corps dépasse un peu sa pose puis s'y pose (6 à 10 images).
5. La teinte passe de l'ancienne à la nouvelle en fondu ; la marque apparaît à la fin.

Les émotions se planifient **sur toute la vidéo**, pas plan par plan : le personnage a un parcours (par exemple : pensif → déterminé → nerveux → soulagé → fier).

## Correspondance avec la planche minimale

| Yeux de la planche | Émotions servies |
|---|---|
| `neutre` | neutre, déterminé (avec sourcils), joyeux |
| `grands` | surpris, excité, effrayé, émerveillé, idée |
| `plisses` | suffisant, espiègle, méfiant, ennuyé, rire, dégoûté, toute anticipation |
| `fermes` | fier, soulagé, endormi, clignement |
| `regard-cote` | pensif, timide, nerveux, méfiant |

| Bouche de la planche | Émotions servies |
|---|---|
| `fermee` | neutre, pensif, méfiant, ennuyé, déterminé |
| `petite-ouverte` | endormi, parole, perplexe |
| `grande-ouverte` | surpris, excité, rire, en pleurs, furieux, émerveillé |
| `moue` | triste, dégoûté, nerveux, timide |
| `sourire` | joyeux, fier, soulagé, suffisant, espiègle, idée |

Éléments à dessiner en plus si l'histoire les demande : yeux en cœur, en larmes, en croix, en spirale, brillants, sourcils froncés ; bouche tremblante, dents serrées, langue tirée ; les marques.

## Listes d'origine (pour étendre la planche)

- **Yeux (24)** : normaux, regard dirigé, grands, souriants, fermés, endormis, clin d'œil, mi-clos, en colère, déterminés, tristes, larmoyants, en pleurs, plissés fermés, brillants, effrayés, vides, étoilés, rouges, en cœur, en croix, en spirale, point, lunettes noires. On peut dépareiller les deux yeux.
- **Bouches (16)** : petit rond, grand O, sourire, large sourire, plate, tremblante, « en w », moue, sourire en coin, rire, ouverte, plainte, dents, langue, boudeuse, bâillement.
- **Marques (18)** : `!`, `?`, `!!`, `!?`, zzz, goutte, étincelle, cœur, cœurs, veine de colère, vapeur, ampoule, points de suspension, gribouillis, notes, spirale, étoiles, nuage.
- **Teintes** : pâle (peur), rouge (colère), bleu (tristesse), rosé (amour), vert (dégoût), doré (fierté).
