# Tête ronde, trait plein et délié

> Fiche du rendu 2.5D mesuré par le studio. Elle résume ; **le détail chiffré, règle par règle, est dans `references/prompt-maitre.md`** (à lire en entier avant de produire). Unité : D = diamètre de la tête du personnage, contour compris. Outils : chaîne mesurée du kit (`kit/LISEZMOI.md`).

## 1. Identité

- **Nom** : Tête ronde, trait plein et délié.
- **Inspiration** : la famille des courts récits animés verticaux où des bonshommes plats à tête ronde jouent dans un décor 3D peint. On en reprend la technique, mesurée au pixel (trait, lumière, rythme, caméra), jamais un personnage, un décor, un texte ni un sujet existant.
- **Pour quels sujets** : tout récit porté par des personnages. Histoire vraie, fiction courte, sketch, explication guidée par un personnage. Idéal quand il y a une réaction forte à jouer (stupeur, panique, indifférence) et un lieu à montrer.
- **À vous de le rendre vôtre** : « tête ronde » décrit une famille de dessin, pas un personnage. Le client décrit les siens (couleurs, coiffe, accessoire) ; le générateur du kit ne contient aucun personnage tout fait.
- **Ne marche pas pour** : l'actualité chaude et les sujets graves (le ton bonhomme les trahit), un tutoriel pas à pas à l'écran, un sujet sans lieu ni personnage, plus de 4 personnages, une histoire donnée pour vraie sans sources.

## 2. Palette, typographie, matières

Encre et peau des personnages, par ambiance (mesurées) :

| Ambiance | Encre du contour | Membres | Peau | Croissant d'ombre | Filet de lumière | Ombre au sol |
|---|---|---|---|---|---|---|
| Plein jour | `#2d2336` | `#3a3357` | `#fcf7f2` | `#ede4ef` | blanc, très fin | sol mélangé à 72 % avec `#4664b8` |
| Coucher de soleil | `#301c2c` | `#2c1a29` | `#ffe4bb` | `#f4c49b` | `#ffc368` | sol mélangé à 87 % avec `#202d6c` |
| Intérieur chaud | `#2b1623` | `#2b1623` | `#fddab3` | `#f2beac` | clair, discret | projetée à l'opposé de la lampe, vers `#26112f` |
| Nuit bleue | `#241731` | `#1a1436` | `#ffe2bc` | `#f2cfbc` | `#fec47c` | tache floue sous les pieds |

Décor, par ambiance (dominantes mesurées ; les couleurs locales du client les remplacent en gardant saturation, luminance et opposition de teintes) :

| Ambiance | Deux familles opposées | Saturation / luminance | Ciel, de haut en bas |
|---|---|---|---|
| Plein jour | sable `#d9b387` et bleu `#258cfb` | 0,43 / 138 | `#1f8af8` vers `#a8daff` |
| Coucher de soleil | orange `#e3994a` et bleu-violet `#484671` | 0,45 / 114 | `#4968b2`, `#8a92b9`, `#ffb771` |
| Intérieur chaud | rouge-brun `#7b3120` et prune `#251023`, contrepoint froid `#503056` | 0,58 / 61 | nuit bleue par les fenêtres |
| Nuit bleue | bleu `#0c154d` et rose-brun `#9a6768` | 0,73 / 52 | `#030e53` vers `#031c9f` |

- **Typographie** (polices libres) : sous-titres en Montserrat 900 ou une grotesque très grasse équivalente, minuscules avec capitale initiale. Aucun autre texte à l'image, sauf un chiffre ou une date sourcés. Police fournie par HyperFrames : voir le skill `rendu`, section « Polices ».
- **Personnages** : aplats sans texture ni grain ; contour prune, jamais noir ; tête à croissant d'ombre et filet de lumière ; coiffe à trois tons francs ; costume dont les couleurs changent très peu d'une ambiance à l'autre.
- **Décor** : textures **peintes**, jamais photographiques ni en aplat. Planches et lames à joints sombres tous les 0,32 D (joint de 0,02 D, 11 à 17 niveaux plus sombre), bois dessiné par script, sans bruit étiré (une veine ondulée tous les 0,06 D, trait de 0,013 D, nœuds et cernes ; contraste de 18 à 21 niveaux, grain fin de 8,5 à 12,7), sol meuble à taches douces (3 à 8 niveaux), métal et verre en 2 ou 3 tons avec un reflet en trait.
- **Intérieur : sombre, à touches froides.** Luminance 61 ± 15, saturation 0,58 ± 0,08 ; prune très sombre (`#251023`, `#3a1828`) sur 48 % ± 12 de l'image ; UNE dominante chaude (bruns-rouges `#7b3120`, `#9f4723`) sur 20 % ± 8, pas une salle toute en brun ; froid obligatoire (`#503056`, `#312e79`) sur 6 à 9 %, par les fenêtres et dans les ombres. Loi de lumière : prompt maître, 3.7.

## 3. Composition 9:16

- 1080 × 1920, rendu à la taille exacte.
- **Zones du studio** (`skills/rendu/references/zones-interface.md`) : rien d'important au-dessus de y = 160, sous y = 1 560, à droite de x = 945.
- **Cadrage dominant : plan en pied serré**, personnage à 60 à 73 % de la hauteur, légère contre-plongée, pieds visibles. Plan à deux : 46 à 61 %. Plan d'ensemble : 8 à 25 %. Gros plan : la tête seule prend 27 à 36 % de la hauteur.
- **Caméra** à environ 1,9 D du sol, tenue à l'horizontale ; focale de 25 mm pour 36 mm de capteur en hauteur ; horizon à 50 à 58 % de la hauteur sur un plan large.
- **Profondeur** en quatre couches : premier plan flou, sujet et sol sous ses pieds nets, fond proche flou (bord de 0,14 D), lointain peint.
- **Sous-titres** : 1 à 2 mots (3 au plus), corps d'environ 78 px (capitales d'environ 55 px), blanc, contour sombre de 6 px et ombre décalée de 4 à 5 px en bas à droite, **centre à y = 1 350**, bloc entre y ≈ 1 300 et 1 400, sur les jambes du personnage. Apparition et disparition sèches.
- **Pourquoi cette position** : elle est dans la zone utile (jusqu'à y = 1 560), mais plus basse que le repère conseillé par `skills/rendu/references/sous-titres.md` (bas du bloc entre 1 220 et 1 320). C'est une dérogation de cette fiche, permise par ce fichier : le cadrage en pied place le visage au-dessus et les jambes à cette hauteur. Entre 1 330 et 1 560, la légende dépliée peut recouvrir le texte ; pour une publicité, remonter au repère et resserrer le cadrage.
- **En intérieur** : cadrer serré devant un fond sombre et flou ; murs meublés à la hauteur du champ (boiserie, tentures, panneaux, rayonnages) : 35 % au plus de décor plat derrière la tête et le torse ; aucun pixel du personnage à moins de 3 px des bords gauche, droit et haut ; 2 silhouettes d'objets coupées par le cadre au plus.
- 16:9 : même décor, cadrages refaits (ne pas recadrer le vertical).

## 4. Ce qui bouge

- **Action principale** : un seul personnage joue par plan. Sa pose change **en une image**, puis elle est tenue, totalement figée (13 à 160 images).
- **Deux boucles de fond** : (1) la dérive de la caméra pendant les tenues (20 à 30 px par seconde, ou +0,27 % d'échelle par image) ; (2) les clignements du personnage au repos (3 images, un toutes les 13 à 25 images). Pas de respiration, pas de rebond.
- **Durées clés** (en images) : anticipation 1 à 2 ; geste large 10, dépassement 3, retour 4 ; stupeur tenue 39 ; chute à plat 14, sans rebond, puis 75 au sol ; marche lente 11 par pas ; action 2 à 4 après le mot. Table complète : prompt maître, rubrique « Jeu ».

| Autorisés (dictionnaire `principes-mouvement`) | Interdits |
|---|---|
| `#027` avancée de caméra, freinée (départ 2 images, freinage 9 à 10) | `#001` apparition en rebond |
| `#029` travelling d'accompagnement (la caméra part avec l'action) | `#024` secousse d'impact |
| `#033` bascule de mise au point | `#030` orbite permanente |
| `#043` panoramique filé, une image, entre deux stations | `#034` caméra à l'épaule |
| `#010` dépassement, sur un geste large seulement | `#023` effet de parasite, `#036` cadre penché |

Interdits propres au style : interpolation douce entre deux poses, plusieurs personnages qui jouent ensemble, bouche calée sur la voix off, écrasement à l'impact, flou de mouvement.

## 5. Rythme et montage

- **Quasi plan-séquence** : presque aucune coupe franche. Les stations se raccordent par des déplacements de caméra (9 à 64 images) et des fondus enchaînés de 6 à 11 images, le plan entrant déjà en mouvement.
- **Une station toutes les 1,1 s environ** ; tenues de 3 à 27 images, 50 pour le plan final.
- Une ou deux fois par film : un coup de zoom (4 images, +4 % puis +2 %), un filé d'une image, un raccord à travers un objet.
- Structure : accroche dès l'image 0, retournement aux deux tiers, chute tenue. Voix à 3,0 à 3,6 mots par seconde, sans pause de plus de 0,3 s.
- **Version courte (8 à 12 s)** : 2 décors, 6 à 9 stations, une seule réaction forte tenue 30 à 40 images, changement d'ambiance entre les deux décors.

## 6. Recette technique

- **Moteur** : Blender pour le décor (skill `blender`), Python pour l'assemblage ; HyperFrames en option pour le montage final et le son (skill `rendu`).
- **Chaîne mesurée du kit** (`kit/LISEZMOI.md`) : `regles.py` (les valeurs), `pantin.py` (personnages), `film.py` (personnages, plans, caméras, jeu, cartons), `bl_decor.py` et `bl_scene.py` (décor), `compo.py` (assemblage), `lancer.py` (enchaînement), `controle.py` (mesures).
- **Trois passes par image, pas de lumière cuite** : couleur peinte sans lumière ; lumière en canaux séparés (soleil, lampes, occlusion) ; normale et profondeur. Détail : `skills/blender/references/trois-passes-et-matieres-peintes.md`.
- **À l'assemblage**, dans cet ordre : lumière de l'ambiance (ombres en mélange, flaques, occlusion), contours du décor (silhouette 0,03 D, arête 0,012 D, plus épais vers le bas), ciel peint et brume, halos des lampes, profondeur de champ, assombrissement des bords, personnages et leur ombre, accentuation, sous-titres.
- **Personnage** : dessiné en vectoriel à la taille du plan, avec deux paramètres par plan, l'ambiance et la direction de la lumière à l'écran :

```python
import pantin
p = pantin.pose(amb="soir", lum=12, yeux="cercle", bouche="grand_o")   # lum : 0 = de la droite, 90 = du haut
image, ancre = pantin.rendre("gardienne", p, zoom=1.0)
```

- **Pose en intérieur** : le plan donne sa lampe principale, de côté (`source=(x, y, z)`). L'assemblage en tire l'ombre projetée à l'opposé (teinte `#26112f`, force 0,84, 0,7 à 1,0 D, contact sous chaque pied), le liseré de lumière côté lampe (`#ffae5c`, jamais sur l'encre) et un accord de teinte qui épargne les hautes lumières : les blancs restent blancs.
- **Rendu par tronçons** : le décor est rendu une fois par tronçon de caméra quand elle ne fait que dériver. Parallaxe de 12 px au plus : plaque recadrée ; de 12 à 120 px : plaque déplacée selon la profondeur ; au-delà, ou décor animé : image par image. Mesuré : 2,3 fois plus vite sur 4 plans de test. `python outils/lancer.py plans` ; détail : `references/rendu-rapide.md`.
- **Profondeur de champ** : flou = 0,055 D × |distance du point de netteté / distance de l'objet − 1|, zone nette de 10 % derrière et 45 % devant, mise au point sur le personnage le plus proche.
- **Pièges** : part de soleil reconstruite après coup au lieu d'être calculée dans la matière (le signe se perd quand la caméra lève le nez) ; milliers d'objets non réunis par matière (30 s par image au lieu de 9) ; deux Blender en même temps ; personnage du fond aussi net que celui de devant ; accord de teinte qui salit les blancs ; lampes carrées (taches de lumière rectangulaires) ; objet coupé par le bord du cadre ; fil du bois en bruit étiré ; décor recalculé à chaque image pendant une tenue ; plaque gardée alors qu'un objet du décor bouge.

## 7. Son

- **Voix** : une seule, humaine de préférence, 3,0 à 3,6 mots par seconde, sans pause de plus de 0,3 s.
- **Musique** : continue, environ 18 dB sous la voix ; elle ne s'arrête jamais.
- **Bruitages** : 1 à 2 par 10 s, sur ce qui est physique seulement ; pic à moins d'une image du geste. Une séquence d'action peut en porter davantage, une fois. Le contrôle de budget du skill `son` dira « film calme » : c'est attendu.
- **Ambiance** : aucune, ou très basse.
- **Niveau** : −14 LUFS, crête à −1 dBTP ou moins, mesurés sur le fichier livré (`skills/son/scripts/finaliser.py`).
- **Sons absents de la banque** : suivre `skills/son/references/sons-manquants.md`.

## 8. Erreurs fréquentes et liste de contrôle

Erreurs : trait constant ; noir pur ; tête en aplat ; ombre grise ou décollée des pieds ; sol flou sous les pieds ; décor vide ou en aplats ; personnage qui rebondit ; poses interpolées ; coupes franches en série ; sous-titres en phrases ; salle toute en brun ; mur nu derrière un personnage ; décor recalculé à chaque image pendant une tenue. La liste complète, avec la mesure qui a montré chaque défaut : prompt maître, rubrique « Interdits ».

- [ ] Contour de la tête et du torse : délié de 0,014 à 0,022 D côté lumière, plein de 0,066 à 0,073 D côté ombre, à ±1 px ; plein à l'opposé de la lumière du plan, à ±10°.
- [ ] Encre, peau, croissant et membres aux couleurs de l'ambiance (ΔE < 6) ; aucun noir pur ; croissant d'ombre et filet de lumière présents.
- [ ] Ombre au sol attachée aux pieds, en mélange vers le bleu-violet (le bleu monte dans l'ombre), bord flou de 0,11 à 0,13 D.
- [ ] Sol net sous les pieds (transitions de 2,0 à 2,3 px, à ±1 px) ; fond flou sur 0,14 D (±25 %).
- [ ] Aucune matière en aplat : joints tous les 0,32 D (±20 %), contraste des matières à ±6 niveaux ; 30 à 45 objets par plan, rien de nu derrière un personnage.
- [ ] En intérieur : luminance 61 ± 15, saturation 0,58 ± 0,08, prune 48 % ± 12, bruns 20 % ± 8, froid 4 à 12 % ; ombre du personnage à 0,35 à 0,80 de la luminance du sol voisin, à ±25° de l'opposé de la lampe ; 35 % au plus de décor plat derrière lui.
- [ ] Tronçons de caméra classés (`lancer.py plans`) : aucune tenue rendue image par image sans raison, aucune plaque au-delà de 120 px ni sur un décor animé.
- [ ] Chaque changement de pose tient en une image ; un seul personnage joue ; action 2 à 4 images après le mot.
- [ ] Sous-titres de 1 à 2 mots, centre à y = 1 350, dans la zone utile, jamais sur un visage.
- [ ] Contrôle chiffré fait, critique indépendante notée, note écrite telle quelle ; sources notées si l'histoire se dit vraie.

**Réglages des contrôles**
- Mouvement : normal
- Caméra : mobile
- Couleurs max : 12
- Bleu-violet : dérogation
- Texte vivant : non
- Taille mini du texte : 78

Le bleu-violet est en dérogation parce que les ombres du style le sont (mélange vers `#202d6c` ou `#4664b8`) et que deux ambiances sur quatre en font leur dominante.

## 9. Aperçu

Pas d'aperçu tiers : la vidéo qui a servi à mesurer le style n'est ni reprise, ni montrée, ni liée. L'aperçu est le film d'essai du kit, sur un sujet neutre et original.

Film d'essai du studio, le 12/11/2026 (non fourni dans le plugin ; l'exemple du kit le refait : `python outils/lancer.py tout`). Avec le seul kit, sur un sujet inventé pour l'occasion (une gardienne de phare attend une lettre, le facteur arrive) : un film de 7 s, 210 images, 2 plans (un intérieur chaud, un extérieur au couchant), 2 personnages décrits en données, sans son. Contrôle chiffré automatique (`controle.py`) : **57 lignes dans la tolérance, 4 hors, aucune non mesurée** sur 61 (hors tolérance : la densité de deux images, et le contour relu dans le film encodé sur une pose où la coiffe et un bras levé touchent la tête). Critique d'un agent indépendant qui n'avait que le prompt maître et le film : **5 sur 10** avant corrections, **7 sur 10** après un tour (personnages 8, jeu 8, décor 6, caméra et montage 7, sous-titres 8,5, histoire 7,5 ; plus aucun défaut bloquant).

## 10. Origine

- **Mesures du studio (Flot Web)** sur une vidéo de référence étudiée en interne, avec la méthode et les scripts du skill `reproduire-reel` : lecture continue image par image, mesure au pixel des personnages (contour, ombrage, membres, visage, ombre au sol) puis du décor (parallaxe, matières, contours, ombres, palette, optique, densité). Ce sont des lois chiffrées ; aucun personnage, costume, accessoire, décor, texte, son ni sujet de cette vidéo n'est repris, ici ou dans le kit.
- **Essais du studio** des 11 et 12/11/2026 : plans de test, contrôle chiffré référence / nous, critiques indépendantes. Les notes et ce qui reste différent sont dits dans le `SKILL.md` de la catégorie.
- Kit (`kit/`) : écrit par le studio. Connecteur : `ahujasid/mcp-for-blender`, commit `2e4b0bc`, MIT.
- Crédits : `licenses/styles-2-5d.md`.
