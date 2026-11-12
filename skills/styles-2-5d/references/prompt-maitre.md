# Prompt maître du style 2.5D « tête ronde, trait plein et délié »

## Mode d'emploi

- **À quoi il sert.** Ce texte contient toutes les règles chiffrées du style. Donné tel quel à un agent, il lui permet de produire ce rendu sans référence sous les yeux : personnages plats dessinés, décor 3D peint, caméra mobile, sous-titres courts.
- **Comment le donner.** Copie tout ce qui suit la ligne « DÉBUT DU PROMPT » et ajoute à la fin le sujet du client : histoire, lieu, époque, personnages, ambiance. Rien d'autre n'est nécessaire.
- **D'où viennent les chiffres.** Mesures au pixel faites par le studio sur une vidéo de référence étudiée en interne (méthode du skill `reproduire-reel`), puis essayées sur des plans de test. Ce sont des lois de dessin et de lumière. Aucun personnage, décor, texte ou sujet d'une œuvre existante n'y figure.
- **Avec le kit.** Les mêmes valeurs sont en données dans `kit/regles.py` ; le kit les applique (`kit/LISEZMOI.md`). Sans le kit, l'agent les applique à la main.
- **Dix rubriques, plus la rubrique 0.** Personnages, jeu, décor, caméra et montage, sous-titres, son, histoire, production, interdits, contrôles. La méthode de rendu de la rubrique « Production » est détaillée dans `references/rendu-rapide.md`.
- **Unité.** D = diamètre de la tête du personnage, contour compris. Tout ce qui est en D se recalcule à chaque plan : c'est ce qui rend le style transposable à toute taille.

---

DÉBUT DU PROMPT

Tu produis une vidéo verticale (1080 × 1920, 30 images par seconde) dans un style précis : des personnages plats, dessinés, posés dans un décor 3D peint, filmés par une caméra qui ne s'arrête presque jamais. Les règles ci-dessous sont mesurées. Applique les valeurs, ne les arrondis pas à l'œil.

## 0. Ce qui t'appartient et ce qui ne t'appartient pas

1. **Les personnages, les décors, le sujet et le texte sont ceux du client.** Tu les inventes avec lui : forme de coiffe, couleurs, accessoire, lieu, époque, histoire.
2. **Tu ne reprends aucun personnage, costume, accessoire, décor, texte ni sujet d'une chaîne ou d'une œuvre existante.** Ces règles décrivent une technique (comment on trace, on éclaire, on anime, on cadre), pas une œuvre.
3. Si le client demande « le même personnage que telle chaîne », tu refuses cette partie en une phrase et tu dessines le sien dans cette technique.
4. Si l'histoire se dit vraie, chaque affirmation a sa source (rubrique 7).
5. Unité : **D = diamètre de la tête, contour compris.** Angles à l'écran : 0° = vers la droite, 90° = vers le haut.

## 1. Personnages

### 1.1 Proportions

| Élément | Valeur | Pourquoi |
|---|---|---|
| Tête | disque de 1 D, posé sur le torse, qu'il recouvre de 0,03 D ; pas de cou | toute l'expression est là : elle doit dominer la silhouette |
| Forme de la tête | pas un cercle parfait : petit axe / grand axe de 0,91 à 0,98, ondulation fixe par personnage | un cercle parfait fait « icône » ; l'irrégularité fait « dessiné » |
| Torse | gélule de 0,72 D de large sur 1,0 D de haut | lisible de loin, facile à pencher d'un bloc |
| Jambes | traits de 1,3 D de long | silhouette haute, pieds visibles en plan en pied serré |
| Bras | traits de 0,72 à 0,88 D selon la pose | assez longs pour pointer et se lever au-dessus de la tête |
| Pieds | trait horizontal de 0,18 D, posé à plat | ancre le personnage au sol |
| Hauteur totale, sans coiffe | 3,2 D | rapport tête / corps du style |
| Mains | absentes au repos (le trait s'arrête, bout rond) ; levées : 3 ou 4 petits traits de doigts ; fermées : une boule de 0,10 à 0,11 D | une main détaillée attire l'œil au mauvais endroit |
| Genoux, coudes | droits à l'appui ; pliés en angle vif seulement en repli (marche, course) | le corps reste raide : c'est l'effet qui s'exagère, pas la forme |

### 1.2 Taille dans le cadre

| Type de plan | Hauteur du personnage (en % des 1 920 px) | Diamètre de la tête |
|---|---|---|
| Plan d'ensemble | 8 à 25 % | 30 à 100 px |
| Plan en pied à deux | 46 à 61 % | 290 à 300 px |
| **Plan en pied serré, légère contre-plongée (le plus fréquent)** | **60 à 73 %** | 380 à 450 px |
| Plan poitrine ou taille | tête seule : 27 à 36 % de la hauteur | 525 à 685 px |
| Très gros plan | tête plus large que le cadre | 770 à 845 px |

Pourquoi le plan en pied serré : les pieds restent visibles et les sous-titres passent sur les jambes, jamais sur le visage.

### 1.3 Le contour : un plein et un délié réglés par la lumière

| Règle | Valeur | Pourquoi |
|---|---|---|
| Loi | **épaisseur = 0,044 D − 0,028 D × cos(angle compté depuis la direction de la lumière)** | le trait dit d'où vient la lumière : il modèle la forme sans ombrage lourd |
| Délié (côté lumière) | 0,014 à 0,022 D, médiane 0,018 D | |
| Plein (côté ombre) | 0,066 à 0,073 D | |
| Construction | un disque d'encre de rayon 0,5 D ; par-dessus, un disque de peau de rayon 0,456 D dont le centre est **décalé de 0,028 D vers la lumière** | donne exactement la loi en cosinus, en deux formes |
| Où est le plein | toujours à l'opposé de la lumière du plan, pas « en bas » | soleil en haut à droite : plein en bas à gauche ; lampe à gauche : plein à droite |
| Torse | même loi : 0,019 D côté lumière, 0,058 à 0,071 D côté ombre | une seule main dessine tout le personnage |
| Coiffes et accessoires | contour régulier de 0,029 à 0,035 D | l'objet posé se distingue du corps |
| Bord du trait | net, lissé sur 0,85 à 0,95 px ; aucun tremblé à petite échelle (écart type sous 0,010 D) | le dessin est propre, pas crayonné |
| Couleur | un prune très sombre, **jamais noir**, uniforme le long du trait | le noir pur durcit l'image et se détache du décor |

Encre selon l'ambiance :

| Ambiance | Contour | Membres |
|---|---|---|
| Plein jour | `#2d2336` | `#3a3357` (plus clairs et plus bleus) |
| Coucher de soleil | `#301c2c` | `#2c1a29` |
| Intérieur chaud | `#2b1623` | `#2b1623` |
| Nuit bleue | `#241731` | `#1a1436` |

### 1.4 Ombrage de la tête

| Règle | Valeur | Pourquoi |
|---|---|---|
| Peau claire | presque plate (écart type de 1,7 à 5 niveaux) ; léger dégradé de 7 niveaux le long de l'axe de la lumière | la tête n'est ni un aplat ni une boule en dégradé |
| Croissant d'ombre | du côté opposé à la lumière ; 15 à 27 % du disque ; 18 à 34 niveaux plus sombre ; teinte tirée vers le rose (−8 à −34°), saturation −16 à −44 | donne le volume avec une seule forme |
| Construction du croissant | le disque de peau moins le même disque décalé de 0,24 rayon vers la lumière | le croissant s'amincit tout seul aux deux bouts |
| Bord du croissant | doux : transition 10–90 % de 0,05 à 0,13 D | un bord franc ferait un masque |
| Filet de lumière | du côté éclairé : arc de 0,013 à 0,022 D de large, posé à 0,033 D du trait, effilé aux deux bouts, sur un cercle plus petit que la tête | la touche qui fait « lumière chaude » |
| Reflets ponctuels, grain, texture de papier | aucun (grain mesuré : 0,3 à 1,8 niveau, soit le bruit de compression) | l'image reste lisse |
| Sous une coiffe à bord | la moitié haute de la tête passe dans l'ombre du bord (51 à 53 % du disque), frontière presque horizontale, très douce (0,20 D) | n'existe que s'il y a un bord au-dessus du visage |

Peau, croissant et filet selon l'ambiance :

| Ambiance | Peau | Croissant | Filet |
|---|---|---|---|
| Plein jour | `#fcf7f2` | `#ede4ef` | pas de filet coloré (reflets blancs très fins) |
| Coucher de soleil | `#ffe4bb` | `#f4c49b` | `#ffc368` |
| Intérieur chaud | `#fddab3` | `#f2beac` | clair, peu marqué |
| Nuit bleue | `#ffe2bc` | `#f2cfbc` | `#fec47c` |

**De nuit, la peau reste crème.** Le personnage n'est jamais teinté globalement par le décor : seuls changent le trait, le croissant, le filet, la couleur des membres et le côté du plein.

### 1.5 Torse, coiffes, accessoires

| Règle | Valeur | Pourquoi |
|---|---|---|
| Torse | aplat au centre | |
| Ombre propre du torse | une bande de 16 à 21 % de la surface, le long du bord éclairé, derrière le filet ; luminosité −11 à −17, saturation −15 à −24, teinte −4 à −5° | |
| Filet de lumière du torse | 0,022 D de large, à 0,034 D du trait, `#ff9d4c` au couchant et de nuit | |
| Couleurs du costume | elles changent très peu d'une ambiance à l'autre (quelques niveaux) | le personnage reste reconnaissable dans tous les décors |
| Coiffe | **trois tons francs** (clair, moyen, bandeau), sans dégradé | |
| Petits détails clairs du costume (galons, boutons, rayures) | traits de 0,015 à 0,018 D, espacés d'au moins 0,040 D | en dessous, le détail disparaît à petite taille |
| Texture des aplats | aucune (0,3 à 1,4 niveau) | |

### 1.6 Visage

Tous les traits fins du visage ont la couleur du contour et une épaisseur constante de **0,021 à 0,025 D**. Sourcils et grosses moustaches sont des formes pleines.

| Élément | Valeur |
|---|---|
| Œil ordinaire | demi-disque plein de 0,09 D de large, sous un trait de paupière droit et horizontal |
| Œil cerclé (peur, stupeur) | anneau de 0,22 à 0,23 D hors tout, trait de 0,024 D, **intérieur couleur peau** (pas de blanc), pupille de 0,06 D |
| Écart entre les yeux | 0,26 D d'axe en axe |
| Sourcil | forme pleine de 0,13 à 0,18 D de long sur 0,042 à 0,067 D d'épaisseur |
| Bouche | trait de 0,021 à 0,024 D |

Catalogue des yeux :

| Forme | Dessin | Emploi |
|---|---|---|
| Blasé | demi-disque sous une paupière droite | état de base du personnage calme, tenu longtemps |
| Cerclé | anneau, pupille en point | peur, stupeur |
| Fermé | deux traits légèrement courbes | clignement, effort, bâillement |
| Ovale écrasé | anneau tassé, une seule image | passage de « fermé » à « cerclé » |
| Chevron | « > » | douleur, œil frotté |
| En coin | pupille poussée d'un côté, paupière mi-close | regard vers l'autre personnage |

Sourcils : plats = blasé ; baissés au centre = colère ; relevés au centre = peur ; un seul baissé en biais = air suffisant.

Catalogue des bouches : petit trait ; arc triste ; ondulée ; sourire en coin ; large sourire (une image de passage) ; **dents serrées** (rectangle arrondi blanc, grille de 2 rangées de 4 dents) ; petite ronde ; rectangle arrondi sombre (parole, mastication) ; **grande ouverte** (ovale vertical sombre, bande claire en haut pour les dents, langue rose en bas) ; langue tirée. Pour une réplique à l'image : environ 6 formes tenues 2 à 3 images chacune. La bouche ne suit jamais la voix off.

Vues : de face et de trois quarts. De trois quarts, les traits du visage glissent sur la boule de 0,23 D au plus vers le côté regardé, et l'œil du côté fuyant se tasse de 30 %.

### 1.7 Signes

| Signe | Valeur | Comportement |
|---|---|---|
| Goutte de sueur | 0,12 × 0,14 D, bleu clair `#8cc2d2`, contour de l'encre | apparaît à pleine taille en 1 à 3 images, **reste collée à la tempe sans couler**, disparaît en 1 image |
| Rougeur | deux ellipses de 0,14 × 0,08 D sous les yeux, teinte de la peau tirée vers le rose | joie, gêne |
| Traits de surprise | 3 traits courts de 0,03 D d'épaisseur au-dessus de la tête | 3 images, puis plus rien |
| Souffle | petite bulle claire cernée, près de la bouche | 4 images |
| Lignes de vitesse, étoile d'impact | traits pleins, 2 à 4 images | sur un geste foudroyant ou un choc |

### 1.8 Membres

| Règle | Valeur | Pourquoi |
|---|---|---|
| Épaisseur | 0,054 à 0,061 D, **constante** (écart type de 0,1 à 0,4 px), aucun effilement | environ trois fois le délié de la tête : le membre est un trait, pas un volume |
| Ombre propre | aucune | |
| Bouts | arrondis | |
| **Jambe du second plan** | éclaircie vers la teinte du décor (mesuré : `#937f89` pour la jambe du fond contre `#3b3a63` pour celle de devant) | sépare les deux jambes sans les cerner |

### 1.9 Ombre au sol

| Ambiance | Forme | Couleur | Bord flou (10–90 %) |
|---|---|---|---|
| Plein jour | tache courte qui part des pieds, moins d'une demi-hauteur | sol **mélangé à 72 % avec `#4664b8`** | 0,11 D à mi-longueur (0,07 D au contact) |
| Coucher de soleil | silhouette projetée, longue (3 à 4 fois la hauteur), vers la caméra ou de côté | sol **mélangé à 87 % avec `#202d6c`** | 0,13 D à mi-longueur, 0,2 à 0,5 D au bout |
| Nuit bleue | tache ovale sous les pieds | sol assombri vers le bleu nuit | 0,36 à 0,63 D |
| Intérieur chaud | silhouette projetée au sol, **à l'opposé de la lampe principale**, longue de 0,7 à 1,0 D, plus un contact sous chaque pied (détail en 1.10) | sol mélangé vers le prune `#26112f`, force 0,84 | 0,03 D au contact, 0,10 D au bout |

- **C'est un mélange, jamais une multiplication** : dans l'ombre, le bleu monte (facteur par canal de 0,27 à 0,50 pour le rouge, 0,41 à 0,70 pour le vert, **1,24 à 1,69 pour le bleu**). Une ombre multipliée sort grise ou brune.
- L'ombre **part des pieds**, sans écart. Une ellipse de contact discrète (1 D de large, 0,16 D de haut) évite l'effet « flottant » ; pas de seconde ombre visible.
- Le personnage passe derrière les objets placés devant lui et porte son ombre sur le sol du décor.

### 1.10 Le personnage en intérieur : ombre, liseré, accord

En intérieur, chaque plan donne la position de sa **lampe principale**. Trois réglages en découlent. Sans eux, le personnage a l'air collé sur le décor.

| Règle | Valeur | Pourquoi |
|---|---|---|
| Lampe principale | une par plan, placée **de côté** | l'ombre reste dans le cadre et le trait a un côté clair lisible |
| Ombre projetée | à l'opposé de la lampe ; teinte `#26112f`, force 0,84 ; longueur 0,7 à 1,0 D | une tache douce sous les pieds a été jugée trop timide et sans direction lisible |
| Flou de l'ombre | 0,03 D au contact, 0,10 D au bout | elle s'adoucit en s'éloignant des pieds |
| Contact | une ombre de contact sous **chaque** pied | ancre les deux pieds |
| Ombre lisible | sa luminance vaut 0,35 à 0,80 de celle du sol voisin ; sa direction est à ±25° de l'opposé de la lampe | au-dessus de 0,80 on ne la voit pas ; le sol doit être clair et dégagé sous les pieds |
| Liseré de lumière | du côté de la lampe, teinte `#ffae5c`, en retrait de 0,012 D du bord, large de 0,055 D, force 0,72 | dit d'où vient la lumière ; c'est une touche **sur** le personnage, pas un halo autour |
| Limites du liseré | jamais sur l'encre ; il n'assombrit jamais | sinon il casse le trait et salit la peau |
| Accord de teinte à la pièce | facteurs (0,95 ; 0,89 ; 0,86) ; −22 % vers les pieds | le personnage prend la pièce sans changer de couleurs |
| Hautes lumières | l'accord est retiré à 85 % entre 165 et 235 de luminance | **les blancs restent blancs** |
| Côté du plein | à l'opposé de la lampe principale (règle 1.3) | une seule lumière règle le trait, l'ombre et le liseré |

### 1.11 Finition

| Règle | Valeur | Pourquoi |
|---|---|---|
| Accentuation finale | sur l'image entière : un pixel plus clair côté peau (+16 niveaux), un pixel plus sombre dans le trait (−17), sur 1 px | donne le piqué du trait |
| Grain, texture de papier, halo ou contour clair autour du personnage | aucun (halo mesuré : −0,1 à +1,8 niveau) ; seule exception : le liseré de lumière de l'intérieur (1.10) | |
| Flou de mouvement sur le personnage | aucun | les poses changent en une image |
| Personnage hors du plan de netteté | flouté comme le décor à la même profondeur | sinon il se détache comme un autocollant |

### 1.12 Ce qui n'est pas vérifié

- **Nuit** : les lois sont mesurées (peau crème, tache sous les pieds, liseré clair sur les arêtes du décor) mais n'ont pas été essayées dans nos rendus.
- **Intérieur chaud** : la pose (1.10) a été essayée sur 2 plans. Mesuré : ombre à 0,65 et 0,67 de la luminance du sol, à 7° et 1° de l'opposé de la lampe, blancs conservés (ΔE 1,3). Le critique note l'intégration du personnage 6 puis 6,5 sur 10. Ce qui reste : le liseré est presque invisible sur la peau, et rien ne passe devant le personnage. Un intérieur à plusieurs personnages n'a pas été essayé.
- **Vues** : face et trois quarts seulement. Ni profil strict ni dos.
- Le bout arrondi des membres est lu à l'œil, la mesure automatique n'a pas conclu.

## 2. Jeu

**Règle d'or : une pose change en une seule image, puis elle est tenue, totalement figée.** Pas d'interpolation douce, pas d'animation par paliers de 2 ou 3 images, pas de respiration ni de rebond permanent. C'est la caméra qui fait vivre l'image (rubrique 4).

| Action | Durée, en images (30 par seconde) |
|---|---|
| Changement d'expression | 1, sans intermédiaire |
| Changement caché | derrière un clignement de 3 à 4 images |
| Clignement | 3 (mi-clos, fermé, mi-clos) ; un toutes les 13 à 25 images au repos ; aucun pendant une panique |
| Tenue avant un geste | 13 à 46, visage figé |
| Anticipation | 1 à 2 (le membre part à l'opposé) |
| Geste rapide | anticipation 2, armé 3, tenue 8, frappe 5, gel 13 ; le membre devient une traînée pendant 3 images |
| Geste foudroyant | 4 en tout, avec traînées dessinées |
| Geste large (bras levés) | environ 10, puis dépassement 3 et retour 4 ; accent sur la tête : +7 % en largeur, −5 % en hauteur pendant 2 à 3 images |
| Hochement de tête | 13 de descente (6 lentes, 4 rapides, 3 de freinage), 5 tenues, 8 de remontée ; amplitude 0,25 D ; aucun dépassement |
| Sursaut | 1 image yeux fermés, pose extrême en 1 image, figé 13 |
| Stupeur | 2 images yeux fermés, 1 image d'ovale écrasé, puis anneaux d'un coup ; recul de 0,1 D en 3 images, retour partiel en 5 ; **tenue de 39**, dont 14 totalement figées |
| Réaction à deux | départ sur la même image, second temps décalé de 6 |
| Réaction en cascade | un personnage toutes les 17 |
| Chute à plat | recul 7, bascule 14 (accélérée, de 5 à 91 px par image), corps raide qui pivote sur les pieds, **0 image de rebond** |
| Étirement avant le contact | tête +17 % dans l'axe de la chute pendant 2 images ; pas d'écrasement à l'impact |
| Tenue au sol après la chute | 75 avant le premier mouvement (17 yeux fermés, puis 58 yeux ouverts avec 3 clignements) |
| Chute lourde | 3 lentes, 4 d'accélération, tassement en 6 |
| Marche lente | 11 par pas, 22 par cycle, une pose nouvelle par image ; pas de 0,65 D ; la tête monte et descend de 0,17 D ; pied posé à plat ; torse penché d'environ 20° |
| Marche pressée | 5 à 6 par pas, torse rigide |
| Goutte de sueur | apparaît en 1 à 3, tient jusqu'à 84, disparaît en 1 |
| **Action par rapport au mot** | **2 à 4 images après** l'apparition du sous-titre |

Principes :

1. **Un seul personnage joue dans un plan à deux.** L'autre ne bouge pas (jusqu'à 160 images sur la même pose, avec 2 clignements). Le comique vient du contraste entre celui qui surjoue et celui qui reste blasé.
2. **La tenue fait le gag** : on attend, immobile, après l'action.
3. **Regard caméra** sur la pose forte, au pire moment pour le personnage.
4. **On exagère l'effet, pas la forme** : poussière, étincelles, coiffe qui reste en l'air (35 images en l'air quand le corps tombe en 14). Les corps restent rigides.
5. **Pas d'amorti** : aucune secousse de caméra à l'impact ; la poussière (37 images) et les cailloux (14 images) font le choc.
6. Dépassement seulement sur les gestes larges.

## 3. Décor

### 3.1 Ce qui est en volume, ce qui est peint

| Règle | Valeur | Pourquoi |
|---|---|---|
| Tout ce qui est proche est en vrais volumes 3D | sol, murs, façades, poteaux, mobilier, accessoires | la caméra se déplace vraiment : la parallaxe mesurée est de 1 à 12 px de résidu médian entre deux images, jusqu'à 75 px au premier plan |
| Seul le lointain est fait de plans peints | ciel en dégradé, nuages, relief lointain en 2 rangs, disque du soleil | ils ne montrent aucune parallaxe |
| Les personnages | dessins 2D placés dans la scène : ils reçoivent et portent des ombres, passent derrière les objets | |
| Quatre couches de profondeur par plan | 1. premier plan flou ; 2. plan du sujet, net ; 3. fond proche, flou ; 4. lointain peint | donne la profondeur sans effet |

### 3.2 Densité et vocabulaire

| Règle | Valeur | Pourquoi |
|---|---|---|
| Objets distincts par plan | **30 à 45** (20 au minimum sur le plan large le plus dépouillé) | un décor vide fait carton |
| Zones de couleur par image (indicateur du script de mesure) | 140 à 200 segments, plus 110 à 200 petits | l'indicateur compte des zones, pas des objets : il sert à comparer |
| Petits détails au sol | 5 à 11 par D² autour du sujet ; diamètre médian 0,03 D ; les plus gros de 0,07 à 0,26 D | |
| Touffes, petits objets posés | 0,25 à 0,5 D, un tous les 2 à 3 D | |
| Rien de nu derrière un personnage | un mur porte des planches, une cimaise, des objets accrochés | un grand mur vide se voit tout de suite |
| Ligne d'horizon, plan large | à 50 à 58 % de la hauteur ; ciel dans le tiers haut | |

Tailles utiles : planche de mur ou lame de plancher 0,32 à 0,33 D de large ; clin de façade 0,16 D ; lambris bas 0,17 D ; poteau 0,30 D de côté ; lampe 0,6 D de haut ; panneau suspendu 0,6 × 1,2 D.

### 3.3 Matières : dessinées, jamais en aplat

| Règle | Valeur | Pourquoi |
|---|---|---|
| Aucune matière en aplat | même une surface « unie » varie de 2,5 à 8 niveaux en taches larges et douces | l'œil doit avoir quelque chose à lire |
| Joints de planches | un trait sombre tous les **0,32 à 0,33 D**, épais de **0,016 à 0,024 D**, **11 à 17 niveaux** plus sombre que le bois | c'est le rythme qui fait « plancher » |
| Couleur des joints | version sombre et violacée de la teinte locale | les joints sont dessinés, pas modelés |
| Fil du bois | veines qui ondulent, nœuds et cernes **dessinés** : contraste (écart type) **18 à 21 niveaux**, grain fin 8,5 à 12,7 ; réglages en 3.7 | un bruit étiré se lit comme un rideau de fils |
| Sol meuble (sable, terre) | taches peintes douces, 3 à 8 niveaux de près, 2,5 à 4 au loin, aucune ligne | |
| Métal, verre, tissu | aplats à 2 ou 3 tons avec un reflet clair en trait | |
| La texture s'efface | avec le flou, la distance et l'ombre (contraste de 2,6 à 6,5) | ne pas sur-texturer les fonds |
| Texture photographique, bruit | aucun | |

### 3.4 Contours du décor

| Règle | Valeur | Pourquoi |
|---|---|---|
| Silhouette d'un objet | **0,02 à 0,034 D** | |
| Arête intérieure | **0,009 D**, soit deux à trois fois plus fine | hiérarchie : la silhouette d'abord |
| Plein et délié | plus épais en bas et du côté opposé à la lumière (jusqu'à 0,045 D en bas) | la règle des personnages, appliquée au décor |
| Couleur | l'encre de l'ambiance pour le mobilier et les accessoires (`#2f2030` de jour) ; une version sombre de la teinte locale pour les petits objets | personnages et décor de la même main |
| Petits détails au sol | liseré de 0,006 à 0,021 D, brun, en bas ; il s'efface entre 8 et 17 D de la caméra | au loin, il ferait des points noirs |
| De nuit | le trait sombre devient un **liseré clair** bleu `#2048d2`, de 0,016 à 0,036 D, sur les arêtes qui prennent la lumière | |
| Objets lointains | ils gardent leur contour ; le flou de profondeur le dissout | |

### 3.5 Lumière

| Règle | Valeur | Pourquoi |
|---|---|---|
| Deux tons par face | chaque face d'un volume est un aplat texturé ; face à l'ombre = **0,72 ×** la face éclairée | pas de dégradé de modelé |
| Face dans une ombre portée | 0,5 × avec un virage au violet (teinte −36 à −42°) | |
| Ombres portées : couleur | **mélange** de la surface vers un bleu-violet : 72 % de `#4664b8` de jour, 87 % de `#202d6c` au couchant ; sur une façade, 70 % pour garder la couleur locale | le bleu monte dans l'ombre (× 1,24 à 1,69) |
| Ombres portées : dureté | bord flou de 0,05 à 0,07 D au contact, **0,14 D** à mi-longueur, 0,2 à 0,5 D au bout d'une ombre longue | pénombre d'un soleil large (3,5° de diamètre apparent dans nos rendus) |
| Ombres portées : longueur | moins d'une demi-hauteur de jour ; 3 à 4 fois la hauteur au couchant | |
| Dégradés de lumière | **18 à 45 niveaux** sur un grand mur ou un sol | une grande surface n'est jamais uniforme |
| Flaques de lumière | autour de chaque lampe, le mur ou le sol s'éclaircit sur environ 1 D ; cœur de la flamme : rayon de 0,06 D | une source visible doit éclairer quelque chose |
| Lampes | géométrie **ronde** (un globe) ; floues dans le fond, ce sont des disques à bord doux | le halo est la surface qui brille, étalée : une lampe carrée donne une tache rectangulaire |
| Occlusion | une bande sombre de 0,15 à 0,25 D au pied des murs et sous les meubles ; pas d'occlusion diffuse | |
| Deux températures | chaque ambiance tient sur deux familles de teintes opposées | |

Direction de la lumière : de jour, en haut à droite, ombres courtes ; au couchant, soleil bas dans le champ ou de côté, ombres longues vers la caméra ; en intérieur, des lampes ponctuelles dont une lampe principale par plan, placée de côté : le personnage porte son ombre à l'opposé (1.10) ; de nuit, une source latérale, cônes et flaques.

### 3.6 Palette par ambiance

| Ambiance | Saturation moyenne | Luminance moyenne | Dominantes (part de l'image) |
|---|---|---|---|
| Plein jour | 0,43 | 138 | `#d9b387` 22 %, `#bc9576` 20 %, `#3c293b` 13 %, `#258cfb` 12 %, `#6dbaff` 8 %, `#8e8082` 7 %, `#794d41` 6 % |
| Coucher de soleil | 0,45 | 114 | `#484671` 23 %, `#e3994a` 15 %, `#bb7d4e` 12 %, `#6174b2` 11 %, `#8186ad` 10 %, `#30202f` 9 %, `#683d34` 7 % |
| Intérieur chaud | 0,58 | 61 | `#251023` 25 %, `#3a1828` 23 %, `#592227` 12 %, `#7b3120` 10 %, `#9f4723` 10 %, `#fdd8bc` 6 %, `#503056` 6 %, `#312e79` 3 % |
| Nuit bleue | 0,73 | 52 | `#0c154d` 28 %, `#051b6a` 16 %, `#070e2e` 13 %, `#0e248e` 12 %, `#454c93` 10 %, `#765573` 7 %, `#9a6768` 6 % |

- Les deux premières couleurs ne dépassent pas **42 à 48 %** de l'image.
- Familles opposées : sable et bleu de jour ; orange et bleu-violet au couchant ; rouge-brun et prune en intérieur, avec un **contrepoint froid** obligatoire (violet `#503056`, bleu de nuit par les fenêtres) ; bleu et rose-brun de nuit.
- Un intérieur chaud est sombre : luminance moyenne de 61, près de la moitié de l'image en prune très sombre. Ses règles complètes sont en 3.7.
- Ces palettes donnent des rapports. Les couleurs locales du client (ses murs, ses costumes) les remplacent en gardant la saturation, la luminance et l'opposition de teintes.

### 3.7 Intérieur : sombre, à touches froides

Un intérieur réussi n'est pas « une salle chaude ». C'est une salle **sombre**, avec une seule dominante chaude et des touches froides.

Palette :

| Règle | Valeur | Pourquoi |
|---|---|---|
| Luminance moyenne | **61 ± 15** | une salle claire (125 dans notre essai raté) perd l'ambiance |
| Saturation moyenne | **0,58 ± 0,08** | sombre, mais pas terne |
| Prune très sombre | `#251023` et `#3a1828` : **48 % ± 12** de l'image | c'est le fond : près de la moitié du cadre |
| UNE dominante chaude | bruns-rouges moyens `#7b3120` et `#9f4723` : **20 % ± 8** | pas une salle toute en brun |
| Contrepoint froid, obligatoire | violet `#503056` et bleu de nuit `#312e79` : **6 à 9 %** (toléré 4 à 12) | par les fenêtres et dans les ombres ; sans lui l'image est monochrome |
| Cadrage | serré, devant un fond sombre et flou | un plancher éclairé qui prend trop de cadre fait sortir la palette (mesuré sur un plan de face : prune 28 %, bruns 34,1 %) |

Loi de lumière, posée à l'assemblage :

| Règle | Valeur | Pourquoi |
|---|---|---|
| Pénombre (hors des flaques de lampe) | mélange à 70 % vers `#251023`, facteur 0,58 | l'ombre de la pièce est prune, pas noire |
| Flaque de lampe | **(1 − exp(−lampe / 0,085))²**, où « lampe » est la part de lumière reçue des lampes | cœur plein, bord qui tombe vite |
| Teinte de la lumière | lumière × (1,06 ; 0,90 ; 0,74) | chaude, sans virer à l'orange |
| Occlusion (creux, pieds de murs) | tirée vers `#312e79` à 45 % | le froid se loge dans les ombres |
| Fond | tiré vers `#503056` jusqu'à 34 %, à partir de 3,2 m | le lointain de la pièce vire au violet |
| Bords de l'image | assombris de 0,66, vers `#251023` | plus fort qu'en extérieur, vers le prune et non vers le noir |

Murs meublés dans le champ :

| Règle | Valeur | Pourquoi |
|---|---|---|
| Ce qui habille un mur | boiserie à la hauteur du champ (jusqu'à 2,25 m dans notre essai), tentures, panneaux, rayonnages | un mur nu derrière un personnage se voit tout de suite |
| Décor plat derrière la tête et le torse | **35 % au plus** ; un pixel est « plat » si la luminance varie de moins de 6 niveaux dans une fenêtre de 0,35 D ; zone examinée : la tête et le torse, élargis de 0,5 D | chiffre le « mur nu » |
| Personnage et bords du cadre | aucun pixel du personnage à moins de 3 px des bords gauche, droit et haut | un membre coupé par le cadre |
| Objets coupés par le cadre | 2 silhouettes au plus ; la cible est zéro | un objet coupé fait décor mal cadré |

Bois dessiné (par script : veines ondulées, nœuds, cernes ; plus de bruit étiré) :

| Règle | Valeur | Pourquoi |
|---|---|---|
| Veines | une tous les 0,06 D ; trait de 0,013 D | |
| Ondulation | 2,4 D de long | des veines droites font « rayures » |
| Nœuds | un par cellule de 2,6 × 0,9 D ; 45 % des cellules sans nœud | rares et irréguliers |
| Cibles | contraste 18 à 21 (± 6) ; grain fin 8,5 à 12,7 (± 4) | les valeurs mesurées du bois net et éclairé |
| Plancher | dessin 3 fois plus large ; un joint tous les 0,32 D | les joints doivent rester le premier rythme |

Technique :

| Règle | Valeur | Pourquoi |
|---|---|---|
| Lampes | en géométrie ronde (un globe) | halos ronds |
| Soleil | 3,5° de diamètre apparent | les ombres longues s'adoucissent avec la distance |
| Liseré peint des cailloux | il s'efface entre 8 et 17 D | plus de points noirs au loin |
| Mise au point | sur le personnage le plus proche | |
| Cadre | aucun objet coupé | |

Le personnage posé dans cet intérieur : règles 1.10.

### 3.8 Lointain et traitement final

| Élément | Valeur |
|---|---|
| Ciel de jour, de haut en bas | `#1f8af8`, `#3f9dff`, `#5db3ff`, `#84caff`, `#a8daff` ; nuages plats `#f1f5fc` |
| Ciel du couchant | `#4968b2`, `#6a80b9`, `#8a92b9`, `#eaab71`, `#ffb771` ; nuages rares, orangés près du soleil |
| Ciel de nuit | `#030e53` vers `#031c9f` ; aucun nuage |
| Soleil couchant | cœur `#ffd08a`, rayon à mi-hauteur 0,86 D, halo `#f5ac64` fondu sur environ 3 D |
| Écart ciel / sol, de jour | le ciel est plus sombre que le sol de 56 niveaux, à 180° de teinte |
| Brume de distance | les objets lointains s'éclaircissent de **+46 niveaux** vers un gris-mauve ; bande pâle à l'horizon |
| Assombrissement des bords | **−21 %** de luminance entre le centre et les coins ; plus fort en intérieur, vers le prune et non vers le noir |
| Grain | aucun (0,06 à 0,34 niveau) |
| Aberration chromatique | aucune (décalage rouge / bleu sous 0,6 px) |
| Particules | quelques points clairs flottants au couchant et en intérieur ; nuage de poussière en aplats à l'impact ; rien en plein jour |

### 3.9 Ce qui n'est pas vérifié pour le décor

- **Plein jour et nuit** : lois mesurées, non essayées dans nos décors refaits.
- Sur nos plans de test, un critique indépendant a noté le décor **7 sur 10 pour l'extérieur au couchant** (la référence : 9). **L'intérieur**, noté 5 avant les règles 3.7, est noté **6,5 puis 7** après (décor 6,5 puis 7).
- Ce qui reste sous la référence en intérieur : rien ne passe devant le personnage ; la lampe ne fait pas de tache nette au sol ni sur la table ; les objets nets proches ont des faces trop noires et un trait plus mou que celui du personnage ; un objet encore coupé par le cadre ; la palette du plan de face (prune 28 %, bruns 34,1 %).
- Écrit sans mesure : la pénombre du soleil à 3,5° et l'effacement du liseré des cailloux (rendus, pas mesurés).
- Bois dessiné : sur une table, contraste 16,8 et grain fin 7,9 ; sur le plancher, contraste 15 et un joint tous les 0,334 D. Dans la tolérance, sous la cible.
- Le trait du décor, tiré de la profondeur, est légèrement tremblé ; celui des personnages est vectoriel. La cible est un seul trait.
- Les arêtes intérieures sont trop discrètes dans nos rendus.

## 4. Caméra et montage

| Règle | Valeur | Pourquoi |
|---|---|---|
| Structure | **quasi plan-séquence** : presque aucune coupe franche ; les plans se raccordent par des déplacements rapides de caméra et des fondus courts | le film ne s'arrête jamais |
| Stations | une tenue ou un mouvement toutes les **1,1 s** environ ; tenues de 3 à 27 images (50 pour le plan final) | |
| Déplacements | 9 à 64 images | |
| Profil d'un déplacement | départ en 2 images, **freinage en 9 à 10**, arrêt de 1 à 5 ; le freinage est toujours plus long que l'accélération | arrivée « posée » |
| Fondus enchaînés | 6 à 11 images ; le plan entrant est déjà en mouvement | |
| Autres raccords | un filé d'une image ; un raccord à travers un objet (une fenêtre, une pupille) | une ou deux fois par film |
| Coup de zoom | poussée de 4 images (+4 %, puis +2 %) avec lignes de vitesse, avant un recul de 12 images | ponctue une révélation |
| Dérive pendant les tenues | **20 à 30 px par seconde** ; ou une avancée régulière de +0,27 % par image | la caméra n'est presque jamais immobile |
| Accompagnement | la caméra part avec le corps qui tombe, suit l'objet lancé | |
| Secousse à l'impact | aucune | |
| Flou de mouvement de caméra | aucun | |
| Focale | **25 mm pour un capteur de 36 mm en hauteur** (champ vertical de 71°) | focale courte : perspective marquée, décor présent |
| Hauteur de caméra | environ **1,9 D** au-dessus du sol (entre la hanche et la poitrine du personnage), caméra tenue à l'horizontale ; ras du sol pour les plans d'objet | |
| Convergence des verticales | 0,4 à 1,8° à hauteur d'homme ; 2,9° en contre-plongée | |
| Profondeur de champ | **flou (écart type) = 0,055 D × \|distance du point de netteté / distance de l'objet − 1\|** | donne un bord de 0,14 D sur le fond lointain, en plan moyen comme en plan large |
| Zone nette | autour du sujet : 10 % derrière, 45 % devant ; mise au point sur le personnage le plus proche | |
| **Sol sous les pieds** | **net** : transitions de 2,0 à 2,3 px, comme le personnage | un sol flou sous les pieds fait « autocollant » |
| Fond, plan moyen | bord 10–90 % de 0,14 D | |
| Tout premier plan | flou léger (transitions de 6 à 8 px) | |
| Petit intérieur en plan large | aucun flou (2,0 à 2,9 px partout) | tout est dans la zone nette |
| Forme du flou | proche d'une gaussienne | |
| Cadrage dominant | plan en pied serré : personnage à 60 à 73 % de la hauteur, légère contre-plongée | |
| Autres cadrages | contre-plongée serrée sur le torse, très gros plan d'objet, plongée sur un groupe, ras du sol, plan large à personnage de 8 %, vue à travers une ouverture | |
| Vérifier le champ | aucun objet coupé par le bord du cadre, aucun mur nu, une source de lumière visible, des formes contrastées dans le fond | le flou doit rester lisible |

## 5. Sous-titres

| Règle | Valeur | Pourquoi |
|---|---|---|
| Police | grotesque très grasse (libre : Montserrat 900 ou équivalent) | |
| Casse | minuscules, capitale initiale, ponctuation | plus posé que des capitales |
| Taille | corps d'environ **78 px**, soit des capitales d'environ 55 px (2,8 % de la hauteur) | |
| Position | centre à **y = 1 350** (70 % de la hauteur), x = 540 ; le bloc tient entre y ≈ 1 300 et 1 400 | sur les jambes du personnage, jamais sur un visage |
| Zone | dans la zone utile du studio (x de 60 à 945, y de 160 à 1 560) ; plus bas que le repère conseillé (bas du bloc entre 1 220 et 1 320) | dérogation de la fiche du style ; pour une publicité, remonter au repère |
| Couleur | blanc pur | |
| Contour | sombre, 6 px, plus une ombre décalée de 4 à 5 px en bas à droite | lisible sur tout décor |
| Mots par carton | **1 à 2**, 3 au plus (1,36 en moyenne) | |
| Durée d'un carton | 3 à 22 images, 10 en moyenne | |
| Animation | aucune : apparition et disparition sèches, sur le début du mot | |
| Synchronisation | l'action à l'image arrive **2 à 4 images après** le mot | le spectateur lit, puis voit |
| Autre texte à l'image | aucun, sauf un chiffre ou une date sourcés | |

## 6. Son

| Règle | Valeur | Pourquoi |
|---|---|---|
| Voix | **une seule**, de préférence humaine | |
| Débit | en français, viser **3,0 à 3,6 mots par seconde** | sous 2,8, le film paraît lent |
| Pauses | aucune de plus de 0,3 s | |
| Musique | **continue**, environ **18 dB sous la voix** ; elle ne s'arrête jamais, même avant une chute | |
| Bruitages | **1 à 2 par 10 s** pour une histoire narrée ; seulement sur ce qui est physique (un objet tombe, une porte, un impact) | le budget général du studio (environ 5 par 10 s) vise le motion design |
| Place d'un bruitage | pic à **moins d'une image** du geste (mesuré : −9 à +24 ms) | |
| Rafale | une séquence d'action peut en porter jusqu'à 14 en 10 s, une seule fois | |
| Ambiance | aucune, ou très basse | |
| Niveau final | **−14 LUFS** intégrés (±1), crête à **−1 dBTP ou moins**, mesurés sur le fichier livré | |
| Dynamique | faible (plage d'environ 2 LU) | la voix reste devant du début à la fin |
| Sons d'une œuvre existante | jamais : ni musique, ni voix, ni bruitage extrait | |

## 7. Histoire

| Règle | Valeur |
|---|---|
| Accroche | dès l'image 0 : la première phrase commence tout de suite, le personnage est déjà à l'écran dans une pose forte ; ni titre, ni logo, ni fondu depuis le noir |
| Trois premières secondes | au moins trois stations de caméra et une réaction |
| Structure | accroche, développement en un fil unique, retournement aux deux tiers, chute tenue ; la dernière phrase tient la promesse de la première |
| Longueur du script | durée × débit : 30 s = 90 à 110 mots ; 45 s = 135 à 160 ; 60 s = 180 à 215 |
| Découpage | une idée par station ; écris la liste des stations avec, pour chacune, les mots couverts, le cadrage, qui joue, la pose forte |
| Personnages | 1 à 4 ; un seul joue à la fois |
| Lieux | 2 à 4, chacun avec son ambiance de lumière ; change d'ambiance au moins une fois dans le film |
| Registre | histoire vraie, fiction, humour ou explication : le style sert aux quatre |
| **Si l'histoire se dit vraie** | chaque affirmation et chaque chiffre a sa source dans un tableau fait par fait, avec ses nuances ; ce qui n'est pas sourcé est retiré ou présenté comme une légende |
| Si c'est une fiction | ne pas la présenter comme vraie |
| Sujet | celui du client ; jamais un sujet déjà traité par une chaîne du même format |

## 8. Production

Les personnages sont dessinés en 2D et posés à l'assemblage. Le décor n'a donc pas besoin d'être recalculé à chaque image quand la caméra ne fait que dériver : on le rend **une fois par tronçon de caméra** (une « plaque »), et on le recadre.

### 8.1 Classer chaque tronçon de caméra

| Règle | Valeur | Pourquoi |
|---|---|---|
| Tronçon | on coupe chaque plan aux stations de la caméra ; on réunit les tronçons voisins tant que la parallaxe de l'ensemble reste sous le seuil | un plan enchaîne de vrais déplacements et des tenues en dérive |
| On classe par tronçon, jamais par plan | plan entier : parallaxe de 790 à 2 060 px (4 plans d'essai) ; déplacements : une dizaine d'images, 370 à 1 350 px ; tenues en dérive : 14 à 112 px | pris en entier, tout plan partirait en 3D |
| Parallaxe | en pixels : de combien un objet proche glisse par rapport au lointain, entre la pose de la plaque et la pose la plus éloignée ; objet proche pris à 0,6 fois la distance du sujet | c'est ce que la plaque ne sait pas refaire |
| Pose de la plaque | la pose la plus centrale du tronçon | elle réduit le trajet à rattraper |
| Champ et taille de la plaque | focale plus courte (marge de 4 %) ; taille jusqu'à 2 fois le cadre | couvre le mouvement et le zoom |

Les quatre modes :

| Mode | Quand | Ce qu'on rend |
|---|---|---|
| `fixe` | caméra immobile | une plaque |
| `plaque` | parallaxe de **12 px au plus** | une plaque, recadrée par homographie |
| `couches` | parallaxe de **12 à 120 px** | la même plaque, chaque pixel déplacé selon SA profondeur (lue dans la passe de données) : l'équivalent continu de 2 à 4 couches ; ce qui était caché derrière un objet proche est étiré |
| `3d` | au-delà de **120 px**, ou décor animé | image par image |

Avec le kit : `python outils/lancer.py plans` affiche les tronçons et leur mode ; on force un mode par la clé `mode` du plan, ou tout le film par la variable `EPISODE_MODE=3d` ; un plan dont le décor bouge porte `anime=True`.

### 8.2 Ce qu'on rend une fois, ce qu'on refait à chaque image

| Une fois par tronçon, sur la plaque | À chaque image du film |
|---|---|
| les trois passes du décor (couleur, lumière, données) | le recadrage de la plaque |
| la lumière de l'ambiance | la profondeur de champ |
| les contours du décor | l'assombrissement des bords |
| le ciel | les personnages et leur ombre |
| les halos des lampes | les sous-titres |

### 8.3 Quand le 3D est obligatoire

| Cas | La mesure | Ce qu'on fait |
|---|---|---|
| Parallaxe au-delà de 120 px | à 307 px en mode `couches` : écart de 0,94 en moyenne, 1,63 au pire, 99e centile 25,7 ; les touffes du premier plan sont étirées ou dédoublées | 3D image par image |
| Décor animé (un objet bouge) | l'objet reste figé sur la plaque : écart de 1,3 à 4,5, 99e centile jusqu'à 131 | 3D ; dire `anime=True` dans le plan |
| Ombre ou lampe qui bouge pendant le tronçon | sur une plaque, elle ne bouge pas | 3D |
| Tronçons réunis juste sous le seuil | 119 px sur un plan d'essai ; la méthode n'est validée image par image que jusqu'à 112 px | regarder ces images ; au moindre étirement, forcer le 3D |

Écart = moyenne de l'écart absolu par pixel avec le rendu image par image, en niveaux sur 255.

| Mode | Écart mesuré |
|---|---|
| `couches` | 0,13 à 0,52 pour 17 à 112 px de parallaxe (99e centile 1,4 à 6,5) : c'est le bruit entre deux rendus identiques (0,08 à 0,32 à parallaxe nulle) |
| `plaque` (homographie seule) | 0,46 à 0,74 à 14–18 px ; 0,74 à 1,06 à 18–23 px ; 1,4 à 2,9 à 40–50 px (99e centile jusqu'à 52) ; 7,6 à 112 px : tout le cadre se décale |

### 8.4 Conduire le rendu

| Règle | Valeur | Pourquoi |
|---|---|---|
| Plans de test | en **demi-taille** tant qu'on règle le cadrage, la caméra et le jeu : 3,38 s par image au lieu de 5,29 (−36 %) | les images montrées au client et le contrôle chiffré restent à la taille finale |
| Un seul Blender | jamais deux rendus en même temps | sur une carte graphique intégrée, le pilote plante |
| Assemblage | en plusieurs processus à la fois : 210 images en 15 min avec 2 processus, en 12 min avec 3 | l'assemblage n'utilise pas Blender |
| Changer une ambiance, un contour, le flou, un personnage, un sous-titre | aucun rendu Blender : on refait l'assemblage | la lumière se pose à l'assemblage |
| Avant de lancer | annoncer le temps prévu, d'après le nombre de rendus (images en 3D + plaques) | |

### 8.5 Temps mesurés

Essai chronométré du 12/11/2026 : 4 plans de test d'un décor lourd (3 656 objets réunis en 535), 256 images, PC à carte graphique intégrée.

| Mesure | Valeur |
|---|---|
| Rendu image par image, pleine taille (24 images) | 5,29 s par image (couleur 1,69 ; lumière 2,74 ; données 0,86) ; 22,6 min pour les 256 images. La veille, machine plus chargée : 9,2 s par image |
| Rendu image par image, demi-taille | 3,38 s par image (−36 %) |
| Une plaque (1 124 à 1 406 px de large) | 6,1 s en moyenne |
| Rendu par tronçons, seuils 12 et 120 px | 107 images en 3D et 5 plaques pour 256 images : 9,9 min, soit 2,33 s par image (**2,3 fois plus vite**) |
| Part du 3D | 107 images sur 256 ; un des 4 plans (54 images) reste en 3D parce qu'un objet du décor y bouge ; sans lui : 53 sur 202 |
| Reprojection d'une image | 0,94 s (machine chargée) |
| Assemblage | environ 4 s par image de film avec 5 ou 6 processus (109 images en 396 à 433 s) |
| Film d'exemple (3 plans, 229 images avec les images de contrôle) | 70 rendus Blender au lieu de 229 ; 4,6 à 5,0 s par rendu |
| Passes regroupées en un seul rendu | non mesuré |
| Carte graphique dédiée | non mesuré |

**Estimation** pour un film de 61,5 s (1 845 images) ; ce n'est pas une mesure. Avant : 15 s par image tout compris, soit 7 h 40. Par tronçons, en comptant un tiers des images en 3D (31 % sur le film d'exemple, 26 à 42 % sur les plans d'essai) : environ 650 images en 3D (57 min) et une centaine de plaques (10 min), soit environ 1 h 10 de Blender ; assemblage à 4 s par image : environ 2 h. **Total : environ 3 h 10.** C'est maintenant l'assemblage qui pèse le plus.

## 9. Interdits : ce qui casse le style

| Interdit | La mesure qui l'a montré |
|---|---|
| Trait d'épaisseur constante sur la tête et le torse | la loi mesurée va de 0,018 D côté lumière à 0,07 D côté ombre ; un essai à trait constant a été jugé « loin de l'original » |
| Noir pur pour le trait | toutes les encres mesurées sont des prunes de luminance 26 à 39 |
| Tête en aplat | croissant d'ombre sur 15 à 27 % du disque, 18 à 34 niveaux plus sombre, plus un filet de lumière |
| Tête en dégradé de boule | un dégradé linéaire n'explique que 19 à 47 % de la variance : c'est un aplat et un croissant |
| Cercle parfait pour la tête | rapport d'axes mesuré de 0,91 à 0,98 |
| Blanc dans l'œil cerclé | l'intérieur de l'anneau a la couleur de la peau |
| Membres effilés ou modelés | épaisseur constante à 0,1 à 0,4 px près, couleur uniforme |
| Teinte globale posée sur le personnage | la peau reste crème de nuit ; chez nous, un accord chaud appliqué partout a sali les blancs en intérieur |
| Halo, contour clair, grain ou texture de papier sur le personnage | halo de −0,1 à +1,8 niveau ; grain de 0,3 à 1,8 niveau (le liseré de lumière de l'intérieur, règle 1.10, n'est pas un halo : il est en retrait du bord, côté lampe seulement) |
| Ombre multipliée (grise ou brune) | dans l'ombre mesurée, le bleu est multiplié par 1,24 à 1,69 : c'est un mélange |
| Ombre décollée des pieds, disque noir flou sous le personnage | l'ombre mesurée part des pieds et a la forme de la silhouette |
| Sol flou sous les pieds | 17 px de transition dans notre essai raté, contre 2,0 à 2,3 px mesurés |
| Flou sans rapport avec la distance | fond à 0,03 D dans notre essai raté, contre 0,14 D mesuré |
| Décor vide | 20 à 47 petits segments par image dans notre essai raté, contre 112 à 202 |
| Matières en aplat ou tachées au hasard | contraste de 1,6 à 2,6 niveaux dans notre essai raté, contre 8 à 21 ; aucun joint, contre un tous les 0,32 D |
| Fil du bois en bruit étiré | contraste de 10,9 contre 20,8 ; lu comme « un rideau de fils » par le critique |
| Contour du décor uniforme | 0,047 D partout dans notre essai raté, contre 0,02 à 0,034 D en silhouette et 0,009 D sur les arêtes |
| Lumière qui ne modèle rien | dégradés de 1 à 13 niveaux dans notre essai raté, contre 18 à 45 ; aucune ombre d'un objet sur un autre |
| Lampe sans halo ni flaque | toute lampe mesurée éclaircit ce qui l'entoure sur environ 1 D |
| Intérieur trop clair | luminance moyenne de 125 dans notre essai raté, contre 61 |
| Salle toute en brun | un seul brun moyen couvrait 35 % de l’image dans notre essai raté, contre 10 % pour cette même teinte dans la mesure (20 % pour tous les bruns-rouges moyens réunis) ; notée « monochrome » par le critique |
| Mur nu derrière un personnage | contraste du mur de 0,7 dans notre essai raté, contre 8,5 mesurés sur un mur de planches ; 12,8 et 12,1 une fois le mur meublé |
| Tache douce sans direction sous un personnage en intérieur | jugée trop timide et sans direction lisible ; l'ombre projetée mesurée ensuite : 0,65 et 0,67 de la luminance du sol, à 7° et 1° de l'opposé de la lampe |
| Décor recalculé à chaque image pendant une tenue | 5,29 s par image, alors qu'une plaque de 6,1 s vaut pour tout le tronçon ; écart de 0,13 à 0,52 niveau jusqu'à 112 px de parallaxe, soit le bruit entre deux rendus identiques |
| Plaque gardée quand le décor bouge, ou au-delà de 120 px de parallaxe | objet figé (écart jusqu'à 4,5, 99e centile jusqu'à 131) ; premier plan étiré ou dédoublé à 307 px |
| Pas de lointain | ni ciel en dégradé, ni brume (+46 niveaux), ni assombrissement des bords (−21 %) dans notre essai raté |
| Rendu réaliste : textures photographiques, brume volumétrique, reflets spéculaires | aucune matière mesurée n'a de bruit photographique ; grain du décor de 0,06 à 0,34 niveau |
| Personnage qui rebondit ou respire en continu | tenues de 13 à 160 images strictement figées |
| Interpolation douce entre deux poses | changement en 1 image, sans intermédiaire ; seul le clignement a une image de passage |
| Plusieurs personnages qui jouent en même temps | un seul joue ; les réactions se décalent de 6 ou de 17 images |
| Rebond ou écrasement à l'impact, secousse de caméra | 0 image de rebond mesurée ; aucune secousse |
| Bouche synchronisée sur la voix off | la bouche ne suit jamais la voix |
| Coupes franches en série, caméra fixe | une station toutes les 1,1 s, reliées par des déplacements et des fondus |
| Action sur le mot, ou avant | 2 à 4 images après le mot |
| Sous-titres en phrases, en capitales, animés | 1,36 mot par carton, minuscules, apparition sèche |
| Musique qui s'arrête pour souligner | elle est continue sur toute la durée |
| Bruitage sur chaque geste | 1 à 2 par 10 s hors séquence d'action |
| Personnage, costume, décor, texte ou sujet repris d'une chaîne existante | règle de droit et de métier, sans exception |

## 10. Contrôles avant de livrer

Mesure tes images avec les mêmes scripts que ceux qui ont établi ces règles (skill `reproduire-reel` ; avec le kit, `kit/controle.py`). Un élément se contrôle à la taille où il est dans le film.

| Famille | Ce qu'on mesure | Tolérance |
|---|---|---|
| Contour des personnages | loi du trait (terme constant et amplitude), délié, plein, épaisseur des membres et des traits fins | ±1 px |
| | direction du plein, par rapport à la direction de la lumière du plan | ±10° |
| | largeur de transition du bord du trait | ±0,5 px |
| Couleurs des personnages | encre, peau, croissant, filet, membres, pour l'ambiance du plan | ΔE2000 < 6 |
| Ombrage | saut de luminance du croissant, accentuation, halo | ±8 niveaux |
| | part du croissant dans le disque | ±6 points |
| Ombre au sol | couleur du sol à l'ombre, pour le mélange de l'ambiance | ΔE2000 < 6 |
| | flou du bord | ±8 px (personnage), ±30 % (décor) |
| Matières | espacement des joints | ±20 % |
| | contraste, profondeur des joints, grain fin | ±6 niveaux |
| Contours du décor | silhouette, arête | ±1 px |
| Profondeur de champ | bord du fond flou | ±25 % |
| | netteté du sol sous les pieds | ±1 px |
| Densité | segments, petits segments, détails au sol par D² | ±25 % |
| Palette | dominantes de l'ambiance | ΔE2000 < 8 et part à ±8 points |
| | saturation et luminance moyennes | ±0,08 et ±15 niveaux |
| Intérieur | luminance et saturation moyennes | 61 ± 15 ; 0,58 ± 0,08 |
| | part du prune très sombre ; part des bruns-rouges moyens | 48 % ± 12 ; 20 % ± 8 |
| | part du froid (violet, bleu de nuit) | 6 à 9 % ; toléré de 4 à 12 % |
| | ombre du personnage : luminance de l'ombre / luminance du sol voisin | 0,35 à 0,80 |
| | direction de l'ombre, par rapport à l'opposé de la lampe | ±25° |
| | bois dessiné : contraste ; grain fin | 18 à 21, ± 6 ; 8,5 à 12,7, ± 4 |
| Champ | décor plat derrière la tête et le torse | 35 % au plus |
| | pixels du personnage à moins de 3 px des bords gauche, droit et haut | aucun |
| | silhouettes d'objets coupées par le cadre | 2 au plus |
| Production | mode de chaque tronçon de caméra | aucune tenue rendue en 3D sans raison écrite ; aucune plaque au-delà de 120 px de parallaxe ni sur un décor animé |
| Jeu | durées relevées image par image sur les plans où ça joue | la table de la rubrique 2, à l'image près |
| Sous-titres | hauteur des capitales, centre, contour, mots par carton | ±3 px, ±10 px, ±1 px, 3 mots au plus |
| Son | niveau intégré, crête, bruitages par 10 s, écart entre le son et le geste | −14 LUFS ±1 ; −1 dBTP ou moins ; 1 à 2 ; moins d'une image |

Méthode :

1. **Quatre tours de correction au plus**, puis tu écris ce qui reste hors tolérance et pourquoi.
2. **Critique indépendante** par un agent qui n'a pas fait le travail : il a ce texte et le film, il dit quelles règles sont violées et note sur 10. Tu écris sa note telle quelle. Un tour de corrections, puis une nouvelle note.
3. **Quand le critique et la mesure se contredisent, la mesure tranche.**
4. **Ce que la mesure voit mal**, et que le critique attrape : un personnage mal posé dans le décor (effet autocollant), un fond bouché ou illisible, un jeu sans intention, un gag qui ne tombe pas, un défaut introduit par une correction, un étirement local sur une plaque. Le mur vide et l'objet coupé par le cadre se mesurent maintenant (famille « Champ ») ; le critique les regarde quand même.
5. **Pièges de mesure** : le compte des lignes prend un fil du bois marqué pour des joints (prendre alors la période d'autocorrélation) ; l'indicateur « segments » compte des zones de couleur, pas des objets ; une image de vidéo compressée n'est fiable qu'au demi-pixel et à 2 ou 3 niveaux.
6. Avant de rendre la main : aucune tâche ne tourne, le temps réel est écrit, la liste de ce qui n'est pas vérifié est écrite.

FIN DU PROMPT

---

## État des essais

Ce qui a été essayé dans nos rendus, à la date de cette version : personnages au couchant et en intérieur chaud ; décor extérieur au couchant et intérieur chaud ; quatre plans de test de 8 s. Ce qui est mesuré mais non essayé : décor de plein jour, nuit, profil strict et dos des personnages.

**Essai du kit, le 12/11/2026.** Avec le seul kit, sur un sujet inventé pour l'occasion (une gardienne de phare attend une lettre, le facteur arrive) : un film de 7 s, 210 images, 2 plans (un intérieur chaud, un extérieur au couchant), 2 personnages décrits en données, sans son. Contrôle chiffré automatique (`controle.py`) : **57 lignes dans la tolérance, 4 hors, aucune non mesurée** sur 61 (hors tolérance : la densité de deux images, et le contour relu dans le film encodé sur une pose où la coiffe et un bras levé touchent la tête). Critique d'un agent indépendant qui n'avait que le prompt maître et le film : **5 sur 10** avant corrections, **7 sur 10** après un tour (personnages 8, jeu 8, décor 6, caméra et montage 7, sous-titres 8,5, histoire 7,5 ; plus aucun défaut bloquant). Ce qui reste, d'après lui : caméra trop calme sur les plans d'extérieur (3 à 9 px par seconde pour 20 à 30 demandés), un doigt coupé par le bord du cadre pendant une tenue, des objets du décor coupés par le cadre, un fil du bois qui reste un bruit étiré, des bords trop peu assombris en extérieur, un soleil pâle, un trait de décor crénelé. Ambiances essayées par cet essai : intérieur chaud et couchant, comme sur les plans de test ; le plein jour et la nuit restent à essayer.

**Essais du 12/11/2026 : l'intérieur sombre et le rendu par tronçons.** Deux chantiers ont suivi, sur des sujets inventés.

- **Intérieur (rubriques 1.10 et 3.7).** Deux plans d'intérieur. Contrôle : **28 lignes sur 30 dans la tolérance**. Plan serré de trois quarts : luminance 53,8, saturation 0,582, prune 41,8 %, bruns 23,3 %, froid 7,4 % : tout dans la tolérance. Plan de face : luminance 58,5, saturation 0,586, froid 10,8 % dans la tolérance ; prune 28 % et bruns 34,1 % **hors tolérance** (le plancher éclairé prend trop de cadre). Ombre / sol : 0,65 et 0,67 ; direction à 7° et 1° ; décor plat derrière le personnage : 0 % ; contraste du mur derrière le personnage : 12,8 et 12,1 (0,7 à l'essai précédent) ; bois d'une table : contraste 16,8, grain fin 7,9 ; plancher : contraste 15, joints tous les 0,334 D ; blancs du personnage : ΔE 1,3. Notes d'un critique indépendant, telles quelles (la salle était notée 5 avant ; la référence : 9) : **ensemble 6,5 puis 7 ; décor 6,5 puis 7 ; intégration du personnage 6 puis 6,5.** Ce qui reste sous la référence : rien ne passe devant le personnage ; la lampe ne fait pas de tache nette au sol ni sur la table ; le liseré est presque invisible sur la peau ; les objets nets proches ont des faces trop noires et un trait plus mou que celui du personnage ; un objet encore coupé par le cadre ; la palette du plan de face. Écrit sans mesure : la pénombre du soleil à 3,5° et l'effacement du liseré des cailloux (rendus, pas mesurés).
- **Rendu par tronçons (rubrique 8).** Quatre plans de test d'un décor lourd (3 656 objets réunis en 535), 256 images, PC à carte graphique intégrée. Image par image : 5,29 s par image, 22,6 min. Par tronçons, seuils 12 et 120 px : 107 images en 3D et 5 plaques, **9,9 min, soit 2,33 s par image (2,3 fois plus vite)**. Écart en mode `couches` : 0,13 à 0,52 niveau jusqu'à 112 px de parallaxe, soit le bruit entre deux rendus identiques. Où ça trahit : à 307 px (premier plan étiré ou dédoublé), sur un décor animé (l'objet reste figé), sur les ombres et les lampes qui bougeraient. Limite : des tronçons réunis peuvent arriver juste sous le seuil (119 px sur un plan d'essai) ; la validation image par image s'arrête à 112 px. Non mesuré : les passes regroupées en un seul rendu, une carte graphique dédiée. Détail : `references/rendu-rapide.md`.
